from __future__ import annotations

from datetime import datetime
from functools import lru_cache, reduce
from re import compile as regexp
from typing import TYPE_CHECKING, Callable

from git import Actor, Commit, Sequence, TagObject
from pydantic import BaseModel

from semantic_release.changelog.release_history import ReleaseHistory
from semantic_release.cli.config import BranchConfig
from semantic_release.commit_parser._base import CommitParser
from semantic_release.commit_parser.token import ParseError, ParseResult, ParsedCommit
from semantic_release.const import DEFAULT_VERSION_STR
from semantic_release.enums import LevelBump
from semantic_release.errors import InternalError, NoVersionBump, NotAReleaseBranch, UnexpectedResponse
from semantic_release.gitproject import GitProject, GitRelease
from semantic_release.helpers import validate_types_in_sequence
from semantic_release.hvcs.remote_hvcs_base import RemoteHvcsBase
from semantic_release.version.translator import SemVerTag2VersionConverter
from semantic_release.version.version import Version

if TYPE_CHECKING:  # pragma: no cover
    from pathlib import Path
    from typing import Generator

    from semantic_release.cli.config import RawConfig as Config


class ReleaseSpec:

    def __init__(
        self,
        tagger: Actor,
        committer: Actor,
        release_date: datetime,
        version: Version,
        commits: tuple[Commit, ...] = (),
    ) -> None:
        self.tagger = tagger
        self.committer = committer
        self.tagged_date = release_date
        self.version = version
        self.commits = commits


class Release(ReleaseSpec):

    def __init__(
        self,
        tagger: Actor,
        committer: Actor,
        release_date: datetime,
        version: Version,
        commit: Commit,
        commits: tuple[Commit, ...] = (),
    ) -> None:
        # tag: TagObject | None = None
        super().__init__(tagger, committer, release_date, version, commits)
        self.git_release = GitRelease(
            tagger=tagger,
            committer=committer,
            tagged_date=release_date,
            version=version,
            commit=commit,
            commits=commits,
        )


class ParsedReleaseSpec(BaseModel):
    version: Version
    tagger: Actor
    committer: Actor
    release_date: datetime
    commits: tuple[ParseResult, ...] = ()

    class Config:
        arbitrary_types_allowed = True
        frozen = True
        extra = "forbid"

    @property
    def tag_str(self) -> str:
        return self.version.as_tag()

    @property
    def level_bump(self) -> LevelBump:
        return self.determine_level_bump(self.commits)

    @staticmethod
    @lru_cache
    def determine_level_bump(parsed_results: Sequence[ParsedCommit]) -> LevelBump:
        parsed_levels: set[LevelBump] = {
            parsed_result.bump  # type: ignore[union-attr] # too complex for type checkers
            for parsed_result in filter(
                # Filter out any non-ParsedCommit results (i.e. ParseErrors)
                lambda parsed_result: isinstance(parsed_result, ParsedCommit),
                parsed_results,
            )
        }
        return max(parsed_levels, default=LevelBump.NO_RELEASE)

    @staticmethod
    def parse_commits(
        commit_parser: CommitParser, commits: tuple[Commit, ...]
    ) -> tuple[ParseResult, ...]:
        # Step 1A. apply the parser to each commit in the history (could return multiple results per commit)
        parsed_results = list(map(commit_parser.parse, commits))

        # Step 1B. Validation type check for the parser results (important because of possible custom parsers)
        for parsed_result in parsed_results:
            if not any(
                (
                    isinstance(parsed_result, (ParseError, ParsedCommit)),
                    type(parsed_result) == list
                    and validate_types_in_sequence(
                        parsed_result, (ParseError, ParsedCommit)
                    ),
                    type(parsed_result) == tuple
                    and validate_types_in_sequence(
                        parsed_result, (ParseError, ParsedCommit)
                    ),
                )
            ):
                raise TypeError("Unexpected type returned from commit_parser.parse")

        # Step 2. Accumulate all parsed results into a single list accounting for possible multiple results per commit
        consolidated_results: list[ParseResult] = reduce(
            lambda accumulated_results, p_results: [
                *accumulated_results,
                *(
                    # Cast to list if not already a list
                    p_results
                    if isinstance(p_results, list) or type(p_results) == tuple
                    else [p_results]
                ),
            ],
            parsed_results,
            [],
        )

        return tuple(consolidated_results)

    @classmethod
    def from_release_spec(
        cls, release_spec: ReleaseSpec, commit_parser: CommitParser
    ) -> ParsedReleaseSpec:
        return cls(
            version=release_spec.version,
            tagger=release_spec.tagger,
            committer=release_spec.committer,
            release_date=release_spec.tagged_date,
            commits=cls.parse_commits(
                commit_parser, release_spec.commits
            ),
        )


class Project:

    def __init__(
        self,
        directory: Path | str,
        commit_parser: CommitParser,
        version_translator: SemVerTag2VersionConverter,
        allow_zero_version: bool,
        major_on_zero: bool,
        configured_release_branch_definitions: dict[str, BranchConfig] | None = None,
    ) -> None:
        self.vcs = GitProject(
            directory,
            # directory=directory,
            # commit_author=runtime.commit_author,
            # credential_masker=runtime.masker,
        )
        self._commit_parser = commit_parser
        self._history: ReleaseHistory | None = None
        self._releases: tuple[ReleaseSpec, ...] | None = None
        self._version_translator = version_translator
        self._allow_zero_version = allow_zero_version
        self._major_on_zero = major_on_zero
        self._configured_release_branch_definitions: dict[str, BranchConfig] = (
            configured_release_branch_definitions if configured_release_branch_definitions else {}
        )

    @classmethod
    def from_config(
        cls,
        config: Config,
    ) -> Project:

        return cls(
            directory=config.repo_dir,
            commit_parser=config.load_commit_parser(),
            version_translator=SemVerTag2VersionConverter(tag_format=config.tag_format),
            allow_zero_version=config.allow_zero_version,
            major_on_zero=config.major_on_zero,
            configured_release_branch_definitions=config.branches,
        )

    @property
    def prerelease_token(self) -> str:
        return self.determine_prerelease_token()

    @property
    def commit_parser(self) -> CommitParser:
        return self._commit_parser

    @property
    def major_on_zero(self) -> bool:
        return self._major_on_zero

    @property
    def allow_zero_version(self) -> bool:
        return self._allow_zero_version

    @property
    def default_initial_version(self) -> Version:
        """
        Returns the default initial version for the project.
        This is used when no previous releases are found.
        """
        # Default initial version
        # Since the translator is configured by the user, we can't guarantee that it will
        # be able to parse the default version. So we first cast it to a tag using the default
        # value and the users configured tag format, then parse it back to a version object
        if version := self._version_translator.from_tag(
                self._version_translator.str_to_tag(DEFAULT_VERSION_STR)
        ):
            return version

        # This should never happen, but if it does, it's a bug
        raise InternalError(
            "Translator was unable to parse the embedded default version"
        )

    # @property
    # def releases(self) -> tuple[ReleaseSpec, ...]:
    #     """Returns a tuple of Release instances representing the releases in the project."""
    #     if self._releases is None:

    #     return self._releases

    @property
    def history(self) -> ReleaseHistory:
        if self._history is None:
            pass
            # self._history = ReleaseHistory
        return self._history

    def stage_file_changes(self, files: Sequence[Path | str], noop: bool = False) -> None:
        """Stage file changes in the local repository."""
        self.vcs.stage_file_changes(files, noop=noop)

    def save_file_changes(self, message: str, author: str | None = None, date: datetime | None = None, bypass_verification: bool = False, noop: bool = False) -> None:
        """Save file changes in the local repository with a commit."""
        self.vcs.save_file_changes(message, author=author, date=date, bypass_verification=bypass_verification, noop=noop)

    def tag_release(
        self,
        release_spec: ReleaseSpec,
        message: str | None = None,
        noop: bool = False,
    ) -> None:
        """Tag a release in the local repository."""
        self.vcs.tag_release(
            tag_name=version.as_tag(),
            message=message or version.as_tag(),
            author=author,
            date=date,
            noop=noop,
        )

    def publish_release(
        self,
        release_spec: ReleaseSpec,
        rvcs_client: HvcsBase,
        use_vcs: bool = True,
        create_vcs_release: bool = True,
        noop: bool = False,
    ) -> None:
        """Publish the release to the remote repository."""
        # TODO: Add logic to consider:
        # - if a commit was created for the release, then you must push the commit with the vcs
        # - If the vcs client supports it, then don't try to push the tag, just have the VCS do that (via the API)
        # - if not vcs cannot create tags, then push the commit and tag simultaneously to the remote
        # - If we didn't create a commit, then skip the push
        # - if create vcs release is turned off, but the tag was created, then we still need to push the tag via the VCS
        # - whether the release is a draft or not
        if use_vcs:
            self.vcs.publish_release(noop=noop)

        if not create_vcs_release:
            return

        if not isinstance(rvcs_client, RemoteHvcsBase):
            logger.info("Remote does not support releases. Skipping release creation...")
            return

        try:
            rvcs_client.create_release(
                tag=release_spec.version.as_tag(),
                release_notes=release_spec.release_notes,
                prerelease=release_spec.version.is_prerelease,
                assets=release_spec.assets,
                noop=noop,
            )
        except HTTPError as err:
            logger.error("Failed to create release on remote VCS: %s", err)
            raise err # TODO: make a custom error for this
        except UnexpectedResponse as err:
            logger.error("Unexpected response from remote VCS: %s", err)
            raise err # TODO: make a custom error for this

    def parse_releases(self) -> Generator[ParsedReleaseSpec, None, None]:
        pass

    @lru_cache
    def get_last_release(self, ignore_prereleases: bool | Callable[[Version], bool] = True) -> Release | None:
        """Get the last release from the current head of the repository."""
        return self.vcs.get_last_release(ignore_prereleases=ignore_prereleases)

    def calculate_next_version(self, prerelease: bool = False, build_metadata: str | None = None, strict: bool = True) -> Version:

        def _conditionally_apply_build_metadata(version: Version, build_metadata: str | None) -> Version:
            return version.add_build_metadata(build_metadata) if build_metadata else version

        def _ignore_prereleases_by_token(version: Version) -> bool:
            return version.is_prerelease and version.prerelease_token != self.prerelease_token

        last_version = (
            last_release.version
            if (last_release := self.get_last_release(
                ignore_prereleases=True if not prerelease else _ignore_prereleases_by_token
            ))
            else self.default_initial_version
        )

        # logger.info(
        #     f"The last full version in this branch's history was {latest_full_release_version}"
        #     if latest_full_release_version != default_initial_version
        #     else "No full releases found in this branch's history"
        # )

        unreleased_commits = self.vcs.get_unreleased_commit_history()
        # logger.info(
        #     f"Found {len(unreleased_commits)} commits since the last release!"
        #     if len(unreleased_commits) > 0
        #     else "No commits found since the last release!"
        # )

        level_bump = ParsedReleaseSpec.determine_level_bump(
            parsed_results=ParsedReleaseSpec.parse_commits(
                commit_parser=self.commit_parser,
                commits=unreleased_commits,
            )
        )

        # Move this up to the calling function
        # logger.debug("The type of the next release release is: %s", level_bump)

        # TODO: run the increment version logic & raise error if level_bump is NO_RELEASE
        if level_bump == LevelBump.NO_RELEASE:
            if strict:
                msg = "No version bump detected, and strict mode is enabled."
                raise NoVersionBump(last_version, msg)

            return _conditionally_apply_build_metadata(last_version, build_metadata)

        if level_bump == LevelBump.PRERELEASE_REVISION and not prerelease:
            if strict:
                msg = "Cannot bump to a prerelease version without enabling prerelease mode."
                raise ValueError(msg)

            return _conditionally_apply_build_metadata(last_version, build_metadata)

        # Handle variations where the latest version is 0.x.x
        if last_version.major == 0:
            if not self.allow_zero_version:
                # Set up default version to be 1.0.0 if currently 0.x.x which means a commented
                # breaking change is not required to bump to 1.0.0
                # logger.debug(
                #     "Bumping major version as 0.x.x versions are disabled because of allow_zero_version=False"
                # )
                level_bump = LevelBump.MAJOR

            elif not self.major_on_zero:
                # if we are a 0.x.y release and have set `major_on_zero`,
                # breaking changes should increment the minor digit
                # Correspondingly, we reduce the level that we increment the
                # version by.
                # logger.debug(
                #     "reducing version increment due to 0. version and major_on_zero=False"
                # )
                level_bump = min(level_bump, LevelBump.MINOR)


        # TODO: Complete this adjustment


        # if the current version is a prerelease & we want a new prerelease, then
        # figure out if we need to bump the prerelease revision or start a new prerelease
        if last_version.is_prerelease:
            last_full_version = (
                last_full_release.version
                if (last_full_release := self.get_last_release(ignore_prereleases=True))
                else self.default_initial_version
            )
            # find the change since the last full release because if the current version is a prerelease
            # then we need to predict properly the next full version
            diff_with_last_released_version = last_version - last_full_version
            # logger.debug(
            #     "the diff b/w the latest version '%s' and the latest full release version '%s' is: %s",
            #     latest_version,
            #     latest_full_version,
            #     diff_with_last_released_version,
            # )

            # Since the difference is less than or equal to the level bump and we want a new prerelease,
            # we can abort early and just increment the revision
            if level_bump <= diff_with_last_released_version:
                # 6a ii) if level_bump <= the level bump introduced by the previous tag (latest_version)
                if prerelease:
                    # logger.debug(
                    #     "there has already been at least a %s release since the last full release %s",
                    #     level_bump,
                    #     latest_full_version,
                    # )
                    # logger.debug("Incrementing the prerelease revision...")
                    new_revision = last_version.to_prerelease(
                        token=self.prerelease_token,
                        revision=(
                            1
                            if last_version.prerelease_token != self.prerelease_token
                            else (last_version.prerelease_revision or 0) + 1
                        ),
                    )
                    # logger.debug("Incremented %s to %s", base_version, new_revision)
                    return _conditionally_apply_build_metadata(new_revision, build_metadata)

                # When we don't want a prerelease, but the previous version is a prerelease that
                # had a greater bump than we currently are applying, choose the larger bump instead
                # as it consumes this bump
                # logger.debug("Finalizing the prerelease version...")
                new_version = last_version.finalize_version()
                return _conditionally_apply_build_metadata(new_version, build_metadata)

            # Fallthrough to handle all larger level bumps
            # logger.debug(
            #     "this release has a greater bump than any change since the last full release, %s",
            #     latest_full_version,
            # )

            # Fallthrough, if we don't want a prerelease, or if we do but the level bump is greater
            #
            # because the current version is a prerelease, we must start from the last full version
            # Case 1: we identified that the level bump is greater than the change since
            #         the last full release, this will also reset the prerelease revision
            # Case 2: we don't want a prerelease, so consider only the last full version in history
            last_version = last_full_version

        # From the base version, we can now increment the version according to the level bump
        # regardless of the prerelease status as bump() handles the reset and pass through
        # logger.debug("Bumping %s with a %s bump", base_version, level_bump)
        target_next_version = last_version.bump(level_bump)

        # Converting to/from a prerelease if necessary
        target_next_version = (
            target_next_version.to_prerelease(token=self.prerelease_token)
            if prerelease
            else target_next_version.finalize_version()
        )

        # logger.debug("Incremented %s to %s", base_version, target_next_version)
        return _conditionally_apply_build_metadata(target_next_version, build_metadata)

    def get_next_version(self, bump: LevelBump, prerelease: bool, build_metadata: str | None = None) -> Version:
        last_release = self.get_last_release(ignore_prereleases=not prerelease)
        last_version = (
            last_release.version
            if last_release
            else self.default_initial_version
        )
        new_version = last_version.bump(bump)

        if prerelease:
            new_version = new_version.to_prerelease(
                token=self.prerelease_token,
            )

        return (
            new_version.add_build_metadata(build_metadata)
            if build_metadata else new_version
        )

    def is_released(self, version: Version) -> bool:
        return bool(
            version in { release.version for release in self.vcs.releases }
        )

    def determine_prerelease_token(self, branch_name: str | None = None) -> str:
        return self._determine_prerelease_token(
            branch_name or self.vcs.get_current_branch_name()
        )

    @lru_cache
    def _determine_prerelease_token(self, branch_name: str) -> str:
        for branch_config in self._configured_release_branch_definitions.values():
            if regexp(branch_config.match).match(branch_name):
                return branch_config.prerelease_token

        raise NotAReleaseBranch(
            f"branch {branch_name!r} is NOT in any configured release groups"
        )
