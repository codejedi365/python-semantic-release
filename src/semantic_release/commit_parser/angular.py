"""
Angular commit style parser
https://github.com/angular/angular/blob/master/CONTRIBUTING.md#-commit-message-guidelines
"""

from __future__ import annotations

import logging
import re
from copy import deepcopy
from functools import reduce
from re import compile as regexp
from textwrap import dedent
from typing import TYPE_CHECKING, Tuple

from git.objects.commit import Commit
from pydantic.dataclasses import dataclass

from semantic_release.commit_parser._base import CommitParser, ParserOptions
from semantic_release.commit_parser.token import ParsedCommit, ParseError, ParseResult
from semantic_release.commit_parser.util import breaking_re, parse_paragraphs
from semantic_release.enums import LevelBump

if TYPE_CHECKING:
    from re import Pattern

logger = logging.getLogger(__name__)


def _logged_parse_error(commit: Commit, error: str) -> ParseError:
    logger.debug(error)
    return ParseError(commit, error=error)


# TODO: Remove from here, allow for user customization instead via options
# types with long names in changelog
LONG_TYPE_NAMES = {
    "build": "build system",
    "ci": "continuous integration",
    "chore": "chores",
    "docs": "documentation",
    "feat": "features",
    "fix": "bug fixes",
    "perf": "performance improvements",
    "refactor": "refactoring",
    "style": "code style",
    "test": "testing",
}


@dataclass
class AngularParserOptions(ParserOptions):
    """Options dataclass for AngularCommitParser"""

    minor_tags: Tuple[str, ...] = ("feat",)
    patch_tags: Tuple[str, ...] = ("fix", "perf")
    allowed_tags: Tuple[str, ...] = (
        *minor_tags,
        *patch_tags,
        "build",
        "chore",
        "ci",
        "docs",
        "style",
        "refactor",
        "test",
    )
    default_bump_level: LevelBump = LevelBump.NO_RELEASE
    # TODO: breaking change v10, change default to True
    parse_squash_commits: bool = False

    def __post_init__(self) -> None:
        self.tag_to_level = {tag: self.default_bump_level for tag in self.allowed_tags}
        for tag in self.patch_tags:
            self.tag_to_level[tag] = LevelBump.PATCH
        for tag in self.minor_tags:
            self.tag_to_level[tag] = LevelBump.MINOR


class AngularCommitParser(CommitParser[ParseResult, AngularParserOptions]):
    """
    A commit parser for projects conforming to the angular style of conventional
    commits. See https://www.conventionalcommits.org/en/v1.0.0-beta.4/
    """

    # TODO: Deprecate in lieu of get_default_options()
    parser_options = AngularParserOptions

    def __init__(self, options: AngularParserOptions | None = None) -> None:
        super().__init__(options)
        all_possible_types = str.join("|", self.options.allowed_tags)
        self.re_parser = regexp(
            str.join(
                "",
                [
                    r"(?P<type>%s)" % all_possible_types,
                    r"(?:\((?P<scope>[^\n]+)\))?",
                    # TODO: remove ! support as it is not part of the angular commit spec (its part of conventional commits spec)
                    r"(?P<break>!)?:\s+",
                    r"(?P<subject>[^\n]+)",
                    r"(?:\n\n(?P<text>.+))?",  # commit body
                ],
            ),
            flags=re.DOTALL,
        )
        # GitHub & Gitea use (#123), GitLab uses (!123), and BitBucket uses (pull request #123)
        self.mr_selector = regexp(
            r"[\t ]\((?:pull request )?(?P<mr_number>[#!]\d+)\)[\t ]*$"
        )
        self.issue_selector = regexp(
            str.join("", [
                r"^(?:close[sd]?|fix(?:es|ed)?|resolve[sd]?):[\t ]+(?P<issue_predicate>.+)[\t ]*$"
            ]),
            flags=re.MULTILINE | re.IGNORECASE
        )
        self.commit_prefix = regexp(
            str.join(
                "",
                [
                    r"^(?:%s)" % all_possible_types,
                    r"(?:\([^)]+\))?",  # optional scope
                    # TODO: remove ! support as it is not part of the angular commit spec (its part of conventional commits spec)
                    r"!?:\s+",
                ],
            )
        )
        self.filters = {
            "typo-extra-spaces": (regexp(r"(\S)  +(\S)"), r"\1 \2"),
            "git-header-commit": (
                regexp(r"^[\t ]*commit [0-9a-f]+$\n?", flags=re.MULTILINE),
                "",
            ),
            "git-header-author": (
                regexp(r"^[\t ]*Author: .+$\n?", flags=re.MULTILINE),
                "",
            ),
            "git-header-date": (
                regexp(r"^[\t ]*Date: .+$\n?", flags=re.MULTILINE),
                "",
            ),
            "git-squash-heading": (
                regexp(
                    r"^[\t ]*Squashed commit of the following:.*$\n?",
                    flags=re.MULTILINE,
                ),
                "",
            ),
            "git-squash-commit-prefix": (
                regexp(
                    str.join(
                        "",
                        [
                            r"^(?:[\t ]*[*-][\t ]+|[\t ]+)?",  # bullet points or indentation
                            r"(%s)\b" % all_possible_types,  # prior to commit type
                        ],
                    ),
                    flags=re.MULTILINE,
                ),
                # move commit type to the start of the line
                r"\1",
            ),
        }

    @staticmethod
    def get_default_options() -> AngularParserOptions:
        return AngularParserOptions()

    def commit_body_components_separator(
        self, accumulator: dict[str, list[str]], text: str
    ) -> dict[str, list[str]]:
        if match := breaking_re.match(text):
            accumulator["breaking_descriptions"].append(match.group(1) or "")
            # TODO: breaking change v10, removes breaking change footers from descriptions
            # return accumulator

        elif match := self.issue_selector.search(text):
        # if match := self.issue_selector.search(text):
            predicate = regexp(r" *[,;/ ] *").sub(",", match.group("issue_predicate") or "")
            accumulator["linked_issues"].extend(filter(None, predicate.split(",")))
            # TODO: breaking change v10, removes resolution footers from descriptions
            # return accumulator

        accumulator["descriptions"].append(text)
        return accumulator

    def _parse(self, commit: Commit) -> ParseResult:
        """
        Attempt to parse the commit message with a regular expression into a
        ParseResult
        """
        message = str(commit.message)
        parsed = self.re_parser.match(message)
        if not parsed:
            return _logged_parse_error(
                commit, f"Unable to parse commit message: {message}"
            )
        parsed_break = parsed.group("break")
        parsed_scope = parsed.group("scope")
        parsed_subject = parsed.group("subject")
        parsed_text = parsed.group("text")
        parsed_type = parsed.group("type")

        linked_merge_request = ""
        if mr_match := self.mr_selector.search(parsed_subject):
            linked_merge_request = mr_match.group("mr_number")
            # TODO: breaking change v10, removes PR number from subject/descriptions
            # expects changelog template to format the line accordingly
            # parsed_subject = self.pr_selector.sub("", parsed_subject).strip()

        body_components: dict[str, list[str]] = reduce(
            self.commit_body_components_separator,
            [
                # Insert the subject before the other paragraphs
                parsed_subject,
                *parse_paragraphs(parsed_text or ""),
            ],
            {
                "breaking_descriptions": [],
                "descriptions": [],
                "linked_issues": [],
            },
        )

        level_bump = (
            LevelBump.MAJOR
            # TODO: remove parsed break support as it is not part of the angular commit spec (its part of conventional commits spec)
            if body_components["breaking_descriptions"] or parsed_break
            else self.options.tag_to_level.get(
                parsed_type, self.options.default_bump_level
            )
        )

        logger.debug(
            "commit %s introduces a %s level_bump", commit.hexsha[:8], level_bump
        )

        return ParsedCommit(
            bump=level_bump,
            type=parsed_type,
            category=LONG_TYPE_NAMES.get(parsed_type, parsed_type),
            scope=parsed_scope,
            descriptions=body_components["descriptions"],
            breaking_descriptions=body_components["breaking_descriptions"],
            commit=commit,
            linked_issues=tuple(body_components["linked_issues"]),
            linked_merge_request=linked_merge_request,
        )

    # Maybe this can be cached as an optimisation, similar to how
    # mypy/pytest use their own caching directories, for very large commit
    # histories?
    # The problem is the cache likely won't be present in CI environments
    def parse(self, commit: Commit) -> ParseResult | list[ParseResult]:
        """
        Parse a commit message

        If the commit message is a squashed merge commit, it will be split into
        multiple commits, each of which will be parsed separately. Single commits
        will be returned as a single ParseResult.
        """
        separate_commits: list[Commit] = (
            self.unsquash_commit(commit)
            if self.options.parse_squash_commits
            else [commit]
        )

        # Since we found multiple angular subjects, parse each one individually
        parsed_commits = [
            # parse each of the artificial commits
            self._parse(artificial_commit)
            for artificial_commit in separate_commits
        ]

        lead_commit = parsed_commits[0]

        if isinstance(lead_commit, ParsedCommit) and len(lead_commit.linked_merge_request) > 0:
            # If the first commit has linked merge requests, assume all commits
            # are part of the same PR and add the linked merge requests to all
            # parsed commits
            def add_linked_merge_request(parsed_result: ParseResult) -> ParseResult:
                return (
                    parsed_result
                    if not isinstance(parsed_result, ParsedCommit)
                    else ParsedCommit(
                        **{
                            **parsed_result._asdict(),
                            'linked_merge_request': lead_commit.linked_merge_request,
                        }
                    )
                )

            parsed_commits = [lead_commit, *map(add_linked_merge_request, parsed_commits[1:])]

        return parsed_commits

    def unsquash_commit(self, commit: Commit) -> list[Commit]:
        # GitHub EXAMPLE:
        # feat(changelog): add autofit_text_width filter to template environment (#1062)
        #
        # This change adds an equivalent style formatter that can apply a text alignment
        # to a maximum width and also maintain an indent over paragraphs of text
        #
        # * docs(changelog-templates): add definition & usage of autofit_text_width template filter
        #
        # * test(changelog-context): add test cases to check autofit_text_width filter use
        #
        # `git merge --squash` EXAMPLE:
        # Squashed commit of the following:
        #
        # commit 63ec09b9e844e616dcaa7bae35a0b66671b59fbb
        # Author: codejedi365 <codejedi365@gmail.com>
        # Date:   Sun Oct 13 12:05:23 2024 -0600
        #
        #     feat(release-config): some commit subject
        #
        def text_reducer(text: str, filter_pair: tuple[Pattern[str], str]) -> str:
            """Reduce function to apply mulitple filters to a string"""
            if not text:  # abort if the paragraph is empty
                return text

            filter_pattern, replacement = filter_pair
            return filter_pattern.sub(replacement, text)

        separate_commit_msgs: list[str] = []
        current_msg = ""

        paragraphs = str(commit.message).replace("\r", "").strip().split("\n\n")
        for paragraph in paragraphs:
            # Apply filters to normalize the paragraph
            clean_paragraph = reduce(text_reducer, self.filters.values(), paragraph)

            # remove any filtered (and now empty) paragraphs (ie. the git headers)
            if not clean_paragraph.strip():
                continue

            # Check if the paragraph is the start of a new angular commit
            if not self.commit_prefix.search(clean_paragraph):
                # append the paragraph as part of the previous commit message
                if current_msg:
                    current_msg += f"\n\n{dedent(clean_paragraph)}"
                # else: drop the paragraph
                continue

            # Since we found the start of the new commit, store any previous commit
            # message separately and start the new commit message
            if current_msg:
                separate_commit_msgs.append(current_msg)

            current_msg = clean_paragraph

        # Store the last commit message (if its not empty)
        if current_msg:
            separate_commit_msgs.append(current_msg)

        # Return a list of artificial commits (each with a single commit message)
        return [
            # create a artificial commit object (copy of original but with modified message)
            Commit(
                commit.repo,
                commit.binsha,
                author=deepcopy(commit.author),
                authored_date=commit.authored_date,
                committer=deepcopy(commit.committer),
                committed_date=commit.committed_date,
                message=commit_msg,
                tree=commit.tree,
                parents=commit.parents,
                encoding=commit.encoding,
                gpgsig=commit.gpgsig,
                author_tz_offset=commit.author_tz_offset,
                committer_tz_offset=commit.committer_tz_offset,
            )
            for commit_msg in separate_commit_msgs
        ] or [commit]
