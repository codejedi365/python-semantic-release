from __future__ import annotations

from abc import ABCMeta, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Any, Callable


class HvcsChangelogClientInterface(metaclass=ABCMeta):

    @classmethod
    def __subclasshook__(cls, subclass) -> bool:
        # Validate that the subclass implements all of the abstract methods.
        # This supports isinstance and issubclass checks.
        return (
            cls is HvcsChangelogClientInterface
            and all(
                bool(hasattr(subclass, method) and callable(getattr(subclass, method)))
                for method in HvcsChangelogClientInterface.__abstractmethods__
            )
            or NotImplemented
        )

    @abstractmethod
    def get_changelog_context_filters(self) -> tuple[Callable[..., Any], ...]:
        """
        Return a list of functions that can be used as filters in a Jinja2 template

        ex. filters to convert text to URLs for issues and commits
        """
        raise NotImplementedError
