from __future__ import annotations

from collections import defaultdict
from datetime import datetime, timedelta, timezone
from typing import TYPE_CHECKING

from git.objects.tag import TagObject
from git.util import Actor  # noqa: TCH002, required for pydantic
from pydantic import BaseModel, ConfigDict

from semantic_release.commit_parser import (
    ParseResult,  # noqa: TCH001, required for pydantic
)
from semantic_release.errors import InvalidVersion

if TYPE_CHECKING:
    from git import Tag

    from semantic_release.version.translator import VersionTranslator
    from semantic_release.version.version import Version


class Release(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    tagger: Actor
    committer: Actor
    tagged_date: datetime
    elements: defaultdict[str, list[ParseResult]]
    version: Version

    @staticmethod
    def from_git_tag(tag: Tag, translator: VersionTranslator) -> Release:
        """

        Raises
        ------
            InvalidVersion: If the tag name does not match the tag format

        """
        version = translator.from_tag(tag.name)
        if version is None:
            raise InvalidVersion(f"Tag {tag.name} does not match the tag format")

        # Common Args
        release_args = {
            "elements": defaultdict(list),
            "version": version,
        }

        # tag.object is a Commit if the tag is lightweight, otherwise
        # it is a TagObject with additional metadata about the tag
        if not isinstance(tag.object, TagObject):
            # Grab details from lightweight tag
            release_args.update(
                {
                    "committer": tag.object.author,
                    "tagger": tag.object.author,
                    "tagged_date": datetime.fromtimestamp(
                        tag.object.committed_date,
                        tz=timezone(
                            timedelta(seconds=-1 * tag.object.author_tz_offset)
                        ),
                    ),
                }
            )
        else:
            # Grab details from annotated tag
            release_args.update(
                {
                    "committer": tag.object.tagger.committer(),
                    "tagger": tag.object.tagger,
                    "tagged_date": datetime.fromtimestamp(
                        tag.object.tagged_date,
                        tz=timezone(
                            timedelta(seconds=-1 * tag.object.tagger_tz_offset)
                        ),
                    ),
                }
            )

        return Release(**release_args)
