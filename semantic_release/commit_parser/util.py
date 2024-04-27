from __future__ import annotations

from re import compile as RegExp
from typing import TYPE_CHECKING, NamedTuple, NoReturn, TypeVar, Union

from semantic_release.errors import CommitParseError

if TYPE_CHECKING:
    from git.objects.commit import Commit

    from semantic_release.enums import LevelBump


# Constants
breaking_regex = RegExp(r"BREAKING[ -]CHANGE:\s?(.*)")


def parse_paragraphs(text: str) -> list[str]:
    r"""
    This will take a text block and return a list containing each
    paragraph with single line breaks collapsed into spaces.

    To handle Windows line endings, carriage returns '\r' are removed before
    separating into paragraphs.

    :param text: The text string to be divided.
    :return: A list of condensed paragraphs, as strings.
    """
    return list(
        filter(
            None,
            [
                paragraph.replace("\n", " ").strip()
                for paragraph in text.replace("\r", "").split("\n\n")
            ],
        )
    )


class ParsedCommit(NamedTuple):
    bump: LevelBump
    type: str
    scope: str
    descriptions: list[str]
    breaking_descriptions: list[str]
    commit: Commit

    @property
    def message(self) -> str:
        m = self.commit.message
        return m.decode("utf-8") if isinstance(m, bytes) else m

    @property
    def hexsha(self) -> str:
        return self.commit.hexsha

    @property
    def short_hash(self) -> str:
        return self.commit.hexsha[:7]


class ParseError(NamedTuple):
    commit: Commit
    error: str

    @property
    def message(self) -> str:
        m = self.commit.message
        return m.decode("utf-8") if isinstance(m, bytes) else m

    @property
    def hexsha(self) -> str:
        return self.commit.hexsha

    @property
    def short_hash(self) -> str:
        return self.commit.hexsha[:7]

    def raise_error(self) -> NoReturn:
        raise CommitParseError(self.error)


_T = TypeVar("_T", bound=ParsedCommit)
_E = TypeVar("_E", bound=ParseError)

# For extensions, this type can be used to build an alias
# for example CustomParseResult = ParseResultType[CustomParsedCommit, ParseError]
ParseResultType = Union[_T, _E]
ParseResult = ParseResultType[ParsedCommit, ParseError]
