from __future__ import annotations

import re

from semantic_release.const import SEMVER_REGEX
from semantic_release.globals import logger
from semantic_release.helpers import check_tag_format
from semantic_release.version.version import Version


class SemVerTag2VersionConverter:
    """
    Class to handle translation from version tag strings into their corresponding Version
    instances.
    """

    def __init__(
        self,
        tag_format: str = "v{version}",
    ) -> None:
        check_tag_format(tag_format)
        self.tag_format = tag_format
        self.from_tag_re = self._invert_tag_format_to_re(self.tag_format)

    def from_tag(self, tag: str) -> Version | None:
        """
        Return a Version instance from a Git tag, if tag_format matches the format
        which would have generated the tag from a version. Otherwise return None.
        For example, a tag of 'v1.2.3' should be matched if `tag_format = 'v{version}`,
        but not if `tag_format = staging--v{version}`.
        """
        if not (tag_match := self.from_tag_re.match(tag)):
            return None

        return Version.parse(
            tag_match.group("version"),
            tag_format=self.tag_format,
        )

    def str_to_tag(self, version_str: str) -> str:
        """Formats a version string into a tag name"""
        return self.tag_format.format(version=version_str)

    def __repr__(self) -> str:
        return f"{type(self).__qualname__}{{tag_format={self.tag_format}}}"

    @classmethod
    def _invert_tag_format_to_re(cls, tag_format: str) -> re.Pattern[str]:
        r"""
        Unpick the "tag_format" format string and create a regex which can be used to
        convert a tag to a version string.

        The following relationship should always hold true:
        >>> version = "1.2.3-anything.1+at_all.1234"  # doesn't matter
        >>> tag_format = "v-anything_{version}_at-all"  # doesn't matter
        >>> inverted_format = VersionTranslator._invert_tag_format_to_re(tag_format)
        >>> tag = tag_format.format(version=version)
        >>> m = inverted_format.match(tag)
        >>> assert m is not None
        >>> assert m.expand(r"\g<version>") == version
        """
        pattern = re.compile(
            tag_format.replace(r"{version}", r"(?P<version>" + SEMVER_REGEX.pattern + r")"),
            flags=re.VERBOSE,
        )
        logger.debug("inverted tag_format %r to %r", tag_format, pattern.pattern)
        return pattern
