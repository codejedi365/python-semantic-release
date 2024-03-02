from __future__ import annotations

from functools import reduce
from itertools import zip_longest
from re import (
    compile as regexp,
    error as RegExpError,  # noqa: N812
    escape as regex_escape,
)
from typing import TYPE_CHECKING, ClassVar, cast

from pydantic import field_validator
from pydantic.dataclasses import dataclass
from typing_extensions import TypeAlias

from semantic_release.commit_parser._base import ParserOptions
from semantic_release.enums import LevelBump

if TYPE_CHECKING:  # pragma: no cover
    from typing import Any


# Global type aliases
CommitTypeStr: TypeAlias = str
ScopeStr: TypeAlias = str


@dataclass
class ConventionalCommitParserOptions(ParserOptions):
    """Options dataclass for the ConventionalCommitParser."""

    minor_tags: ClassVar[dict[CommitTypeStr, tuple[ScopeStr, ...]]] = {"feat": (".*?",)}
    """Commit-type prefixes & scopes that should result in a minor release bump."""

    patch_tags: ClassVar[dict[CommitTypeStr, tuple[ScopeStr, ...]]] = {
        "fix": (".*?",),
        "perf": (".*?",),
        "build": ("deps",),
    }
    """Commit-type prefixes & scopes that should result in a patch release bump."""

    other_allowed_tags: ClassVar[dict[CommitTypeStr, tuple[ScopeStr, ...]]] = {
        "build": (".*?",),
        "chore": (".*?",),
        "ci": (".*?",),
        "docs": (".*?",),
        "style": (".*?",),
        "refactor": (".*?",),
        "test": (".*?",),
        "revert": (".*?",),
    }
    """Commit-type prefixes & scopes that are allowed but do not result in a version bump."""

    default_bump_level: LevelBump = LevelBump.NO_RELEASE
    """The minimum bump level to apply to valid commit message."""

    parse_squash_commits: bool = True
    """Toggle flag for whether or not to parse squash commits"""

    ignore_merge_commits: bool = True
    """Toggle flag for whether or not to ignore merge commits"""

    strict_scope: bool = False
    """
    Toggle flag for whether or not to enforce scope validation.

    If enabled, commit types with scopes that are not explicitly defined in the
    `minor_tags`, `patch_tags`, or `other_allowed_tags` mappings will be treated
    as invalid commit messages.
    """

    @classmethod
    @field_validator("minor_tags", "patch_tags", "other_allowed_tags", mode="before")
    def validate_tags_before(
        cls, val: Any
    ) -> dict[CommitTypeStr, tuple[ScopeStr, ...]]:
        if isinstance(val, dict):
            return cast("dict[CommitTypeStr, tuple[ScopeStr, ...]]", val)

        if isinstance(val, (list, tuple)):
            # Convert list/tuple of strings to the expected dict format with wildcard scopes
            return {str(tag): (".*?",) for tag in cast("list[Any]", val)}

        raise ValueError("Tags must be provided as a dict or a list of strings.")

    @classmethod
    @field_validator("minor_tags", "patch_tags", "other_allowed_tags", mode="after")
    def validate_tags_after(
        cls, val: dict[CommitTypeStr, tuple[ScopeStr, ...]]
    ) -> dict[CommitTypeStr, tuple[ScopeStr, ...]]:
        altered_val: dict[CommitTypeStr, tuple[ScopeStr, ...]] = {}

        for tag, scopes in val.items():
            if not isinstance(tag, str) or not tag:
                raise ValueError(
                    f"Invalid commit type tag: {tag}. Must be a non-empty string."
                )

            if not isinstance(scopes, (list, tuple)) or not all(
                isinstance(scope, str) and scope for scope in scopes
            ):
                raise ValueError(
                    f"Invalid scopes for tag '{tag}': {scopes}. Must be a list of non-empty strings."
                )

            altered_scopes: list[str] = []

            for scope in scopes:
                if scope == "*" or scope == ".*":
                    altered_scopes.append(".*?")
                    continue

                if scope.startswith("^") or scope.endswith("$"):
                    raise ValueError(
                        f"Invalid scope '{scope}' for tag '{tag}': Anchors '^' and '$' should not be used at the beginning or end."
                    )

                if scope.startswith("(") or scope.endswith(")"):
                    raise ValueError(
                        f"Invalid scope '{scope}' for tag '{tag}': Do not wrap the scope in parentheses '(' and ')'."
                    )

                test_scope = f"{scope}?" if scope.endswith(".*") else scope
                pattern = rf"{regex_escape(tag)}\({test_scope}\)"

                try:
                    regexp(pattern)
                    altered_scopes.append(test_scope)
                except RegExpError as err:
                    raise ValueError(
                        f"Invalid Regular Expression pattern '{pattern}' for tag '{tag}' and scope '{scope}'."
                    ) from err

            altered_val[tag] = tuple(altered_scopes)

        return altered_val

    @property
    def tag_to_level(self) -> dict[str, LevelBump]:
        """A mapping of commit tags to the level bump they should result in."""
        return self._tag_to_level

    @property
    def allowed_tags(self) -> tuple[str, ...]:
        """
        All commit-type prefixes that are allowed.

        These are used to identify a valid commit message. If a commit message does not start with
        one of these prefixes, it will not be considered a valid commit message.

        :return: A tuple of all allowed commit-type prefixes (ordered from most to least significant)
        """
        cache: set[str] = set()
        result: list[str] = []
        for tag in [
            *self.minor_tags.keys(),
            *self.patch_tags.keys(),
            *self.other_allowed_tags.keys(),
        ]:
            if tag not in cache:
                result.append(tag)
                cache.add(tag)

        return tuple(result)

    def __post_init__(self) -> None:
        def accumulate_regexes(
            acc: set[str], item: tuple[CommitTypeStr, tuple[ScopeStr, ...]]
        ) -> set[str]:
            cmt_type, scopes = item
            return acc | {rf"{regex_escape(cmt_type)}\({scope}\)" for scope in scopes}

        no_release_sets = reduce(
            accumulate_regexes,
            self.other_allowed_tags.items(),
            cast("set[str]", set()),
        )

        patch_sets = reduce(
            accumulate_regexes,
            self.patch_tags.items(),
            cast("set[str]", set()),
        )

        minor_sets = reduce(
            accumulate_regexes,
            self.minor_tags.items(),
            cast("set[str]", set()),
        )

        # We build this from most impactful to least impactful so that when we create the dictionary
        # the first match is always the most impactful one and we don't overwrite it with a less impactful one.
        tag_pattern_str_to_level_list = cast(
            "list[tuple[str, LevelBump]]",
            [
                # we have to do a type ignore as zip_longest provides a type that is not specific enough
                # for our expected output. Due to the empty second array, we know the first is always longest
                # and that means no values in the first entry of the tuples will ever be a LevelBump.
                # Therefore, the cast is safe.
                *zip_longest(minor_sets, (), fillvalue=LevelBump.MINOR),
                *zip_longest(patch_sets, (), fillvalue=LevelBump.PATCH),
                *zip_longest(no_release_sets, (), fillvalue=LevelBump.NO_RELEASE),
            ],
        )

        self._tag_to_level: dict[str, LevelBump] = {}

        # Populate the tag to level mapping, ensuring no overwrites of existing keys
        for tag, level in tag_pattern_str_to_level_list:
            if tag not in self._tag_to_level:
                self._tag_to_level[str(tag)] = level
