from __future__ import annotations

import logging
from re import Pattern, compile as RegExp
from typing import TYPE_CHECKING, Dict, List, Tuple

from pydantic.dataclasses import dataclass

from semantic_release.commit_parser._base import CommitParser
from semantic_release.commit_parser.angular import LONG_TYPE_NAMES, AngularCommitParser, AngularParserOptions
from semantic_release.commit_parser.token import ParsedCommit, ParseError, ParseResult
from semantic_release.commit_parser.util import breaking_re, parse_paragraphs
from semantic_release.enums import LevelBump

if TYPE_CHECKING:
    from git import Commit


log = logging.getLogger(__name__)
CommitTypeStr = str
ScopeStr = str


def _logged_parse_error(commit: Commit, error: str) -> ParseError:
    log.debug(error)
    return ParseError(commit, error=error)


@dataclass
class ScopedAngularParserOptions(AngularParserOptions):
    """Options dataclass for AngularCommitParser"""
    # NOTE: types must be actually imported here because of the way pydantic works
    allowed_tags: tuple[CommitTypeStr, ...] = (
        "build",
        "chore",
        "ci",
        "docs",
        "feat",
        "fix",
        "perf",
        "refactor",
        "style",
        "test"
    )
    allowed_scopes: tuple[ScopeStr, ...] = ("deps", "deps-dev", ".*")
    minor_tags: dict[CommitTypeStr, list[ScopeStr]] = { "feat": [".*"] }
    patch_tags: dict[CommitTypeStr, list[ScopeStr]] = {
        "fix": [".*"],
        "perf": [".*"],
        "build": ["deps"]
    }
    default_bump_level: LevelBump = LevelBump.NO_RELEASE
    ignore_merge_commits: bool = True


class ScopedAngularCommitParser(CommitParser[ParseResult, ScopedAngularParserOptions]):
    """
    An extension of the Angular-style commit message parser that also
    evaluates scope for a determination of choice of bump level.
    """

    parser_options = ScopedAngularParserOptions
    parse = AngularCommitParser.parse

    def __init__(self, options: ScopedAngularParserOptions) -> None:
        super().__init__(options)
        self._base = AngularCommitParser(options)
        self.re_parser = self._base.re_parser
        # self.re_squashed_merge_detection = self._base.re_squashed_merge_detection

        minor_scoped_tags: dict[CommitTypeStr, list[Pattern]] = {}
        patch_scoped_tags: dict[CommitTypeStr, list[Pattern]] = {}

        for k, patterns in self.options.minor_tags.items():
            minor_scoped_tags[k] = list(map(lambda p: RegExp(p), patterns))

        for k, patterns in self.options.patch_tags.items():
            patch_scoped_tags[k] = list(map(lambda p: RegExp(p), patterns))

        self.bump_map: dict[LevelBump, dict[CommitTypeStr, list[Pattern]]] = {
            LevelBump.MINOR: minor_scoped_tags,
            LevelBump.PATCH: patch_scoped_tags,
        }


    def determine_level_bump(self, commit_type: CommitTypeStr, scope: ScopeStr) -> LevelBump:
        """
        Determine the level bump for a commit based on its type and scope.
        """
        for bump_type, scoped_tags in self.bump_map.items():
            for tag, scopes in scoped_tags.items():
                if (
                    commit_type == tag
                    and
                    any(map(lambda regex: regex.match(scope), scopes))
                ):
                    return bump_type

        return self.options.default_bump_level


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

        # Validate scopes
        if parsed_scope not in self.options.allowed_scopes:
            return _logged_parse_error(
                commit, f"Scope {parsed_scope} is not allowed"
            )

        descriptions = parse_paragraphs(parsed_text) if parsed_text else []
        # Insert the subject before the other paragraphs
        descriptions.insert(0, parsed_subject)

        # Look for descriptions of breaking changes
        breaking_descriptions = [
            match.group(1)
            for match in (breaking_re.match(p) for p in descriptions[1:])
            if match
        ]

        # default = NO RELEASE
        level_bump = self.options.default_bump_level

        if parsed_break or breaking_descriptions:
            level_bump = LevelBump.MAJOR
            parsed_type = "breaking"
        else:
            level_bump = self.determine_level_bump(parsed_type, parsed_scope)

        if level_bump == self.options.default_bump_level:
            log.debug(
                "commit %s introduces a level bump of %s due to the default_bump_level",
                commit.hexsha,
                level_bump,
            )
        else:
            log.debug("commit %s introduces a %s level_bump", commit.hexsha, level_bump)

        return ParsedCommit(
            bump=level_bump,
            type=LONG_TYPE_NAMES.get(parsed_type, parsed_type),
            scope=parsed_scope,
            descriptions=descriptions,
            breaking_descriptions=breaking_descriptions,
            commit=commit,
        )
