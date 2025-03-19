from __future__ import annotations

from abc import ABCMeta, abstractmethod

class ReleaseSupportInterface(metaclass=ABCMeta):

    @classmethod
    def __subclasshook__(cls, subclass) -> bool:
        # Validate that the subclass implements all of the abstract methods.
        # This supports isinstance and issubclass checks.
        return (
            cls is ReleaseSupportInterface
            and all(
                bool(hasattr(subclass, method) and callable(getattr(subclass, method)))
                for method in ReleaseSupportInterface.__abstractmethods__
            )
            or NotImplemented
        )

    @abstractmethod
    def create_release(
        self,
        tag: str,
        release_notes: str,
        prerelease: bool = False,
        assets: list[str] | None = None,
        noop: bool = False,
    ) -> int | str:
        """
        Create a release in a remote VCS, if supported

        Which includes uploading any assets as part of the release
        """
        raise NotImplementedError

    @abstractmethod
    def create_or_update_release(
        self, tag: str, release_notes: str, prerelease: bool = False, noop: bool = False,
    ) -> int | str:
        """
        Create or update a release for the given tag in a remote VCS, attaching the
        given changelog, if supported
        """
        raise NotImplementedError
