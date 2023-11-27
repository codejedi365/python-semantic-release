"""Commit parser which looks for emojis to determine the type of commit"""

from __future__ import annotations

import logging
from re import compile as regexp
from typing import Tuple

from git.objects.commit import Commit
from pydantic.dataclasses import dataclass

from semantic_release.commit_parser._base import CommitParser, ParserOptions
from semantic_release.commit_parser.token import ParsedCommit, ParseResult
from semantic_release.commit_parser.util import parse_paragraphs
from semantic_release.enums import LevelBump

logger = logging.getLogger(__name__)


@dataclass
class EmojiParserOptions(ParserOptions):
    major_tags: Tuple[str, ...] = (":boom:",)
    minor_tags: Tuple[str, ...] = (
        ":sparkles:",
        ":children_crossing:",
        ":lipstick:",
        ":iphone:",
        ":egg:",
        ":chart_with_upwards_trend:",
    )
    patch_tags: Tuple[str, ...] = (
        ":ambulance:",
        ":lock:",
        ":bug:",
        ":zap:",
        ":goal_net:",
        ":alien:",
        ":wheelchair:",
        ":speech_balloon:",
        ":mag:",
        ":apple:",
        ":penguin:",
        ":checkered_flag:",
        ":robot:",
        ":green_apple:",
    )
    default_bump_level: LevelBump = LevelBump.NO_RELEASE


class EmojiCommitParser(CommitParser[ParseResult, EmojiParserOptions]):
    """
    Parse a commit using an emoji in the subject line.
    When multiple emojis are encountered, the one with the highest bump
    level is used. If there are multiple emojis on the same level, the
    we use the one listed earliest in the configuration.
    If the message does not contain any known emojis, then the level to bump
    will be 0 and the type of change "Other". This parser never raises
    UnknownCommitMessageStyleError.
    Emojis are not removed from the description, and will appear alongside
    the commit subject in the changelog.
    """

    # TODO: Deprecate in lieu of get_default_options()
    parser_options = EmojiParserOptions

    def __init__(self, options: EmojiParserOptions | None = None) -> None:
        super().__init__(options)
        # GitHub & Gitea use (#123), GitLab uses (!123), and BitBucket uses (pull request #123)
        self.mr_selector = regexp(
            r"[\t ]\((?:pull request )?(?P<mr_number>[#!]\d+)\)[\t ]*$"
        )

    @staticmethod
    def get_default_options() -> EmojiParserOptions:
        return EmojiParserOptions()

    def parse(self, commit: Commit) -> ParseResult | list[ParseResult]:
        all_emojis = (
            self.options.major_tags + self.options.minor_tags + self.options.patch_tags
        )

        message = str(commit.message)
        subject = message.split("\n")[0]

        linked_merge_request = ""
        if mr_match := self.mr_selector.search(subject):
            linked_merge_request = mr_match.group("mr_number")
            # TODO: breaking change v10, removes PR number from subject/descriptions
            # expects changelog template to format the line accordingly
            # subject = self.mr_selector.sub("", subject).strip()

        # Loop over emojis from most important to least important
        # Therefore, we find the highest level emoji first
        primary_emoji = "Other"
        for emoji in all_emojis:
            if emoji in subject:
                primary_emoji = emoji
                break
        logger.debug("Selected %s as the primary emoji", primary_emoji)

        # Find which level this commit was from
        level_bump = LevelBump.NO_RELEASE
        if primary_emoji in self.options.major_tags:
            level_bump = LevelBump.MAJOR
        elif primary_emoji in self.options.minor_tags:
            level_bump = LevelBump.MINOR
        elif primary_emoji in self.options.patch_tags:
            level_bump = LevelBump.PATCH
        else:
            level_bump = self.options.default_bump_level
            logger.debug(
                "commit %s introduces a level bump of %s due to the default_bump_level",
                commit.hexsha[:8],
                level_bump,
            )

        logger.debug(
            "commit %s introduces a %s level_bump", commit.hexsha[:8], level_bump
        )

        # All emojis will remain part of the returned description
        descriptions = parse_paragraphs(message)
        return ParsedCommit(
            bump=level_bump,
            type=primary_emoji,
            scope="",
            descriptions=descriptions,
            breaking_descriptions=(
                descriptions[1:] if level_bump is LevelBump.MAJOR else []
            ),
            commit=commit,
            linked_merge_request=linked_merge_request,
        )
