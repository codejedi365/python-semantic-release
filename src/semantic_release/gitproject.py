"""Module for git related operations."""

from __future__ import annotations

from contextlib import contextmanager, nullcontext
from datetime import datetime, timedelta, timezone
from functools import lru_cache
from pathlib import Path
from queue import LifoQueue
from typing import TYPE_CHECKING, Callable, Generator, cast

from git import GitCommandError, Repo, TagObject, TagReference
from pydantic import BaseModel

from semantic_release.cli.masking_filter import MaskingFilter
from semantic_release.cli.util import indented, noop_report
from semantic_release.core.project import Release
from semantic_release.errors import (
    GitAddError,
    GitCommitEmptyIndexError,
    GitCommitError,
    GitPushError,
    GitTagError,
    InternalError,
    InvalidVersion,
)
from semantic_release.globals import logger
from semantic_release.version.translator import SemVerTag2VersionConverter
from semantic_release.version.version import Version

if TYPE_CHECKING:  # pragma: no cover
    from contextlib import _GeneratorContextManager
    from logging import Logger
    from typing import Sequence

    from git import Actor, Commit


class GitRelease(BaseModel):
    tagger: Actor
    committer: Actor
    tagged_date: datetime
    version: Version
    commit: Commit

    @classmethod
    def from_git_reference(
        cls,
        tag: TagReference,
        version_interpreters: Sequence[SemVerTag2VersionConverter],
    ) -> GitRelease:
        """Create a GitRelease instance from a Git tag reference and a version interpreter."""
        if not isinstance(tag, TagReference):
            raise TypeError(f"Expected TagReference, got {type(tag)}")

        for interpreter in version_interpreters:
            try:
                version = interpreter.from_tag(tag.name)
                break
            except InvalidVersion:
                continue
        else:
            msg = f"Could not interpret tag {tag.name} as Version"
            raise InvalidVersion(msg)

        # tag.object is a Commit if the tag is lightweight, otherwise
        # it is a TagObject with additional metadata about the tag
        if not isinstance(tag.object, TagObject):
            # Grab details from lightweight tag
            return cls(
                tagger=tag.object.author,
                committer=tag.object.author,
                tagged_date=datetime.fromtimestamp(
                    tag.object.committed_date,
                    tz=timezone(
                        timedelta(seconds=-1 * tag.object.author_tz_offset)
                    ),
                ),
                version=version,
                commit=tag.commit,
            )

        # Grab details from annotated tag
        return cls(
            tagger=tag.object.tagger,
            committer=tag.object.tagger.committer(),
            tagged_date=datetime.fromtimestamp(
                tag.object.tagged_date,
                tz=timezone(
                    timedelta(seconds=-1 * tag.object.tagger_tz_offset)
                ),
            ),
            version=version,
            commit=tag.commit,
        )


def convert_tag_to_release(
    tag: TagReference,
    version_interpreters: Sequence[SemVerTag2VersionConverter]
) -> GitRelease | None:
    try:
        return GitRelease.from_git_reference(
            tag=tag, version_interpreters=version_interpreters
        )
    except InvalidVersion:
        logger.warning(
            "Tag '%s' determined not to be Version", tag.name,
        )
        return None


class GitProject:
    def __init__(
        self,
        directory: Path | str = ".",
        commit_author: Actor | None = None,
        credential_masker: MaskingFilter | None = None,
    ) -> None:
        self._project_root = Path(directory).resolve()
        self._logger = logger
        self._cred_masker = credential_masker or MaskingFilter()
        self._commit_author = commit_author
        self._releases: tuple[GitRelease, ...] = ()
        self._version_interpreters: Sequence[SemVerTag2VersionConverter] = []
        self._repo: Repo | None = None

    @property
    def project_root(self) -> Path:
        return self._project_root

    @property
    def logger(self) -> Logger:
        return self._logger

    @property
    def version_interpreters(self) -> Sequence[SemVerTag2VersionConverter]:
        return self._version_interpreters

    @property
    def releases(self) -> tuple[GitRelease, ...]:
        """Returns a tuple of Release objects representing the releases in the project in version descending order."""
        if not self._releases:
            with self._ctx_mgr() as repo:
                releases = set(
                    filter(
                        None,
                        map(
                            lambda t, vi=self.version_interpreters: convert_tag_to_release(
                                tag=t,
                                version_interpreters=vi,
                            ),
                            repo.tags
                        )
                    )
                )

            logger.info("found %s version tags", len(releases))
            self._releases = tuple(sorted(iter(releases), reverse=True, key=lambda release: release.version))

        return self._releases

    @lru_cache
    def get_last_release(self, ignore_prereleases: bool | Callable[[Version], bool] = True) -> Release | None:
        """
        Get the last release from the current head of the repository.

        :param ignore_prereleases: If True, ignores pre-release versions. If a callable, it will be used to filter versions.
        :type ignore_prereleases: bool | Callable[[Version], bool]

        :returns: The last release if it exists, otherwise None.
        :rtype: Release | None

        :raises TypeError: If ignore_prereleases is not a boolean or a callable.
        """
        if not (all_releases := self.get_releases_in_history(ignore_prereleases=ignore_prereleases)):
            return None

        last_release = all_releases[0]
        commits = self.get_commit_history(head_commit_sha=last_release.commit.hexsha)

        if len(all_releases) > 1:
            prev_prev_release = all_releases[1]
            prev_prev_commit_shas = {
                commit.hexsha for commit in self.get_commit_history(
                    head_commit_sha=prev_prev_release.commit.hexsha,
                )
            }
            commits = tuple(
                commit for commit in commits
                if commit.hexsha not in prev_prev_commit_shas
            )

        return Release(
            tagger=last_release.tagger,
            committer=last_release.committer,
            release_date=last_release.tagged_date,
            version=last_release.version,
            commit=last_release.commit,
            commits=commits,
        )

    @contextmanager
    def _ctx_mgr(self) -> Generator[Repo, None, None]:
        """
        Context manager to ensure that the git repository is opened and closed properly.
        This is useful for operations that require a git repository context.
        """
        if self._repo:
            # If the repo is already opened, return it
            yield self._repo
            return

        # Otherwise, create a new Repo instance
        with Repo(str(self.project_root)) as repo:
            self._repo = repo
            yield repo

        # After the context manager exits, reset the repo to None
        self._repo = None

    def get_current_branch_name(self) -> str:
        """Returns the name of the current branch in the repository"""
        with self._ctx_mgr() as repo:
            return repo.active_branch.name

    @lru_cache
    def get_releases_in_history(
        self,
        ignore_prereleases: bool | Callable[[Version], bool] = True,
        head_commit_sha: str | None = None,
    ) -> tuple[GitRelease, ...]:
        """
        Returns a tuple of Release objects representing the releases in the current history chain of the project.
        If head_commit_sha is provided, it will only return releases that are reachable from that commit.
        """
        if not any((callable(ignore_prereleases), isinstance(ignore_prereleases, bool))):
            raise TypeError(
                "ignore_prereleases must be a boolean or Callable[[Version], bool]"
            )

        if not (head_sha := head_commit_sha):
            with self._ctx_mgr() as repo:
                head_sha = repo.head.commit.hexsha

        commit_shas = {
            commit.hexsha
            for commit in self.get_commit_history(
                head_commit_sha=head_sha,
            )
        }

        filter_version_fn = cast("Callable[[Version], bool]", (
            lambda version: ignore_prereleases and not version.is_prerelease
            if isinstance(ignore_prereleases, bool)
            else ignore_prereleases
        ))

        def filter_release(release: GitRelease) -> bool:
            return all((
                release.commit.hexsha in commit_shas,
                filter_version_fn(release.version),
            ))

        return tuple(filter(filter_release, self.releases))

    def get_unreleased_commit_history(
        self,
        head_commit_sha: str | None = None,
    ) -> tuple[Commit, ...]:
        """
        Returns a tuple of Commit objects representing the commit history from the given head to the last release commit.
        If head_commit_sha is provided, it will only return commits that are reachable from that commit.
        """
        if not (head_sha := head_commit_sha):
            with self._ctx_mgr() as repo:
                head_sha = repo.head.commit.hexsha

        commits = self.get_commit_history(head_commit_sha=head_sha)

        if not (last_release := self.get_last_release()):
            return commits

        try:
            stop_index = list(commits).index(last_release.git_release.commit)
            return commits[:stop_index]
        except ValueError as err:
            # This really shouldn't happen
            raise InternalError(
                "Last release commit not found in commit history"
            ) from err


    @lru_cache
    def get_commit_history(self, head_commit_sha: str) -> tuple[Commit, ...]:
        """Returns a tuple of Commit objects representing the commit history from the given head to the root commit."""
        return self.traverse_graph_for_commits(
            head_commit_sha=head_commit_sha,
            stop_commit_sha=None,
        )

    @lru_cache
    def traverse_graph_for_commits(
        self,
        head_commit_sha: str,
        stop_commit_sha: str | None = None,
    ) -> tuple[Commit, ...]:
        # Depth-first search
        def dfs(start_commit: Commit, stop_nodes: set[Commit]) -> tuple[Commit, ...]:
            # Create a stack for DFS
            stack: LifoQueue[Commit] = LifoQueue()

            # Create a set to store visited graph nodes (commit objects in this case)
            visited: set[Commit] = set()

            # Initialize the result
            commits: list[Commit] = []

            # Add the source node in the queue to start the search
            stack.put(start_commit)

            # Traverse the git history capturing each commit found before it reaches a stop node
            while not stack.empty():
                if (node := stack.get()) in visited or node in stop_nodes:
                    continue

                visited.add(node)
                commits.append(node)

                # Add all parent commits to the stack from left to right so that the rightmost is popped first
                # as the left side is generally the merged into branch
                for parent in node.parents:
                    stack.put(parent)

            return tuple(commits)

        with self._ctx_mgr() as repo:
            # Run a Depth First Search to find all the commits after a specific commit (default is root commit)
            return dfs(
                start_commit=repo.commit(head_commit_sha),
                stop_nodes=set(
                    # Retrieve all commits before the stop commit as nodes to stop at for the actual search
                    self.traverse_graph_for_commits(head_commit_sha=stop_commit_sha)
                    if stop_commit_sha
                    else []
                ),
            )

    def _get_custom_environment(
        self,
        repo: Repo,
        custom_vars: dict[str, str] | None = None,
    ) -> nullcontext[None] | _GeneratorContextManager[None]:
        """
        git.custom_environment is a context manager but
        is not reentrant, so once we have "used" it
        we need to throw it away and re-create it in
        order to use it again
        """
        author_vars = (
            {
                "GIT_AUTHOR_NAME": self._commit_author.name,
                "GIT_AUTHOR_EMAIL": self._commit_author.email,
                "GIT_COMMITTER_NAME": self._commit_author.name,
                "GIT_COMMITTER_EMAIL": self._commit_author.email,
            }
            if self._commit_author
            else {}
        )

        custom_env_vars = {
            **author_vars,
            **(custom_vars or {}),
        }

        return (
            nullcontext()
            if not custom_env_vars
            else repo.git.custom_environment(**custom_env_vars)
        )

    def is_dirty(self) -> bool:
        with self._ctx_mgr() as repo:
            return repo.is_dirty()

    def git_add(
        self,
        paths: Sequence[Path | str],
        force: bool = False,
        strict: bool = False,
        noop: bool = False,
    ) -> None:
        if noop:
            noop_report(
                indented(
                    f"""\
                    would have run:
                        git add {str.join(" ", [str(Path(p)) for p in paths])}
                    """
                )
            )
            return

        git_args = dict(
            filter(
                lambda k_v: k_v[1],  # if truthy
                {
                    "force": force,
                }.items(),
            )
        )

        with self._ctx_mgr() as repo:
            # TODO: in future this loop should be 1 line:
            # repo.index.add(all_paths_to_add, force=False)  # noqa: ERA001
            # but since 'force' is deliberately ineffective (as in docstring) in gitpython 3.1.18
            # we have to do manually add each filepath, and catch the exception if it is an ignored file
            for updated_path in paths:
                try:
                    repo.git.add(str(Path(updated_path)), **git_args)
                except GitCommandError as err:  # noqa: PERF203, acceptable performance loss
                    err_msg = f"Failed to add path ({updated_path}) to index"
                    if strict:
                        self.logger.exception(str(err))
                        raise GitAddError(err_msg) from err
                    self.logger.warning(err_msg)

    def git_commit(
        self,
        message: str,
        date: int | None = None,
        commit_all: bool = False,
        no_verify: bool = False,
        noop: bool = False,
    ) -> None:
        git_args = dict(
            filter(
                lambda k_v: k_v[1],  # if truthy
                {
                    "a": commit_all,
                    "m": message,
                    "date": date,
                    "no_verify": no_verify,
                }.items(),
            )
        )

        if noop:
            command = (
                f"""\
                GIT_AUTHOR_NAME={self._commit_author.name} \\
                GIT_AUTHOR_EMAIL={self._commit_author.email} \\
                GIT_COMMITTER_NAME={self._commit_author.name} \\
                GIT_COMMITTER_EMAIL={self._commit_author.email} \\
                """
                if self._commit_author
                else ""
            )

            # Indents the newlines so that terminal formatting is happy - note the
            # git commit line of the output is 24 spaces indented too
            # Only this message needs such special handling because of the newlines
            # that might be in a commit message between the subject and body
            indented_commit_message = message.replace("\n\n", "\n\n" + " " * 24)

            command += f"git commit -m '{indented_commit_message}'"
            command += "--all" if commit_all else ""
            command += "--no-verify" if no_verify else ""

            noop_report(
                indented(
                    f"""\
                    would have run:
                        {command}
                    """
                )
            )
            return

        with self._ctx_mgr() as repo:
            has_index_changes = bool(repo.index.diff("HEAD"))
            has_working_changes = self.is_dirty()
            will_commit_files = has_index_changes or (
                has_working_changes and commit_all
            )

            if not will_commit_files:
                raise GitCommitEmptyIndexError("No changes to commit!")

            with self._get_custom_environment(repo):
                try:
                    repo.git.commit(**git_args)
                except GitCommandError as err:
                    self.logger.exception(str(err))
                    raise GitCommitError("Failed to commit changes") from err

    def git_tag(
        self, tag_name: str, message: str, isotimestamp: str, noop: bool = False
    ) -> None:
        try:
            datetime.fromisoformat(isotimestamp)
        except ValueError as err:
            raise ValueError("Invalid timestamp format") from err

        if noop:
            command = str.join(
                " ",
                [
                    f"GIT_COMMITTER_DATE={isotimestamp}",
                    *(
                        [
                            f"GIT_AUTHOR_NAME={self._commit_author.name}",
                            f"GIT_AUTHOR_EMAIL={self._commit_author.email}",
                            f"GIT_COMMITTER_NAME={self._commit_author.name}",
                            f"GIT_COMMITTER_EMAIL={self._commit_author.email}",
                        ]
                        if self._commit_author
                        else [""]
                    ),
                    f"git tag -a {tag_name} -m '{message}'",
                ],
            )

            noop_report(
                indented(
                    f"""\
                    would have run:
                        {command}
                    """
                )
            )
            return

        with self._ctx_mgr() as repo, self._get_custom_environment(
            repo,
            {"GIT_COMMITTER_DATE": isotimestamp},
        ):
            try:
                repo.git.tag("-a", tag_name, m=message)
            except GitCommandError as err:
                self.logger.exception(str(err))
                raise GitTagError(f"Failed to create tag ({tag_name})") from err

    def git_push_branch(self, remote_url: str, branch: str | None, noop: bool = False) -> None:
        with self._ctx_mgr() as repo:
            branch_name = branch or repo.active_branch.name

            if noop:
                noop_report(
                    indented(
                        f"""\
                        would have run:
                            git push {self._cred_masker.mask(remote_url)} {branch_name}
                        """
                    )
                )
                return

            try:
                repo.git.push(remote_url, branch_name)
            except GitCommandError as err:
                self.logger.exception(str(err))
                msg = f"Failed to push branch ({branch_name}) to remote"
                raise GitPushError(msg) from err

    def git_push_tag(self, remote_url: str, tag: str, noop: bool = False) -> None:
        if noop:
            noop_report(
                indented(
                    f"""\
                    would have run:
                        git push {self._cred_masker.mask(remote_url)} tag {tag}
                    """  # noqa: E501
                )
            )
            return

        with self._ctx_mgr() as repo:
            try:
                repo.git.push(remote_url, "tag", tag)
            except GitCommandError as err:
                self.logger.exception(str(err))
                raise GitPushError(f"Failed to push tag ({tag}) to remote") from err

