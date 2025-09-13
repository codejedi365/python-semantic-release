from __future__ import annotations

from abc import ABCMeta, abstractmethod
from typing import TYPE_CHECKING, Callable, Sequence

if TYPE_CHECKING:
    from datetime import datetime
    from pathlib import Path

    from semantic_release.version.version import Version


class LVCSInterface(metaclass=ABCMeta):
    """
    Interface for subclasses that interact with a local Version Control System

    This class cannot be instantiated directly but must be inherited from
    and implement the designated abstract methods.
    """

    @classmethod
    def __subclasshook__(cls, subclass: type) -> bool:
        # Validate that the subclass implements all of the abstract methods.
        # This supports isinstance and issubclass checks.
        return bool(
            cls is LVCSInterface
            and all(
                bool(hasattr(subclass, method) and callable(getattr(subclass, method)))
                for method in LVCSInterface.__abstractmethods__
            )
        )

    @abstractmethod
    def stage_file_changes(self, files: Sequence[Path | str], noop: bool = False) -> None:
        """
        Prepare the specified files for saving to the local VCS.

        :param files: A sequence of file paths (as `Path` or `str`) to stage.
        :param noop: If True, do not actually stage the files, simulate and log the fake action.
        """
        raise NotImplementedError  # pragma: no cover

    @abstractmethod
    def save_file_changes(self, message: str, author: str | None = None, date: datetime | None = None, bypass_verification: bool = False, noop: bool = False) -> None:
        """
        Commit the staged changes to the local VCS with the provided commit message.

        :param message: The commit message to use.
        :type message: str

        :param author: The author of the commit (if supported by the VCS).
        :type author: str | None

        :param date: The date of the commit (if supported by the VCS).
        :type date: datetime | None

        :param bypass_verification: If True, bypass any pre-commit hooks or verification steps.
        :type bypass_verification: bool

        :param noop: If True, do not actually commit the changes, simulate and log the fake action.
        :type noop: bool
        """
        raise NotImplementedError  # pragma: no cover

    # @abstractmethod
    # def tag_release(
    #     self,
    #     release_spec: ReleaseSpec,
    #     message: str | None = None,
    #     noop: bool = False,
    # ) -> None:
    #     """
    #     Tag the current commit in the local VCS with the provided release specification.

    #     :param release_spec: The release specification containing tag details.
    #     :type release_spec: ReleaseSpec

    #     :param message: An optional message for the tag (if supported by the VCS).
    #     :type message: str | None

    #     :param noop: If True, do not actually create the tag, simulate and log the fake action.
    #     :type noop: bool
    #     """
    #     raise NotImplementedError  # pragma: no cover

    # @abstractmethod
    # def publish_release(self, release_spec: ReleaseSpec, noop: bool = False) -> None:
    #     """
    #     Push the committed changes and tags to the remote repository.

    #     :param release_spec: The release specification containing details for publishing.
    #     :type release_spec: ReleaseSpec

    #     :param noop: If True, do not actually push the changes, simulate and log the fake action.
    #     :type noop: bool
    #     """
    #     raise NotImplementedError  # pragma: no cover


    @abstractmethod
    def get_last_release(self, ignore_prereleases: bool | Callable[[Version], bool] = True) -> Release | None:
        """
        Retrieve the most recent release from the local VCS.

        :param ignore_prereleases: If True, ignore pre-release versions when determining the last release.
                                   If a callable is provided, it should accept a Version instance and return
                                   True if the version is a pre-release to be ignored.
        :type ignore_prereleases: bool | Callable[[Version], bool]

        :return: The most recent Release instance or None if no releases are found.
        :rtype: Release | None
        """
        raise NotImplementedError  # pragma: no cover

    # TODO: make less Git specific
    # @abstractmethod
    # def get_unreleased_commit_history(head_commit_sha: str | None = None) -> tuple[Commit, ...]:
    #     """
    #     Retrieve the commit history since the last release up to the specified head commit.

    #     :param head_commit_sha: The SHA of the head commit to stop at. If None, use the latest commit.
    #     :type head_commit_sha: str | None

    #     :return: A tuple of Commit instances representing the unreleased commit history.
    #     :rtype: tuple[Commit, ...]
    #     """
    #     raise NotImplementedError  # pragma: no cover

    @abstractmethod
    def get_current_state_ref_name(self) -> str:
        """
        Retrieve the name of the current branch or reference in the local VCS.

        :return: The name of the current branch or reference.
        :rtype: str
        """
        raise NotImplementedError  # pragma: no cover

    @abstractmethod
    def get_all_releases(self, ignore_prereleases: bool | Callable[[Version], bool] = True) -> Sequence[Release]:
        """
        Retrieve all releases from the local VCS.

        :param ignore_prereleases: If True, ignore pre-release versions when retrieving releases.
                                   If a callable is provided, it should accept a Version instance and return
                                   True if the version is a pre-release to be ignored.
        :type ignore_prereleases: bool | Callable[[Version], bool]

        :return: A sequence of Release instances.
        :rtype: Sequence[Release]
        """
        raise NotImplementedError  # pragma: no cover

    @abstractmethod
    def get_previous_releases(self, ignore_prereleases: bool | Callable[[Version], bool] = True) -> Sequence[Release]:
        """
        Retrieve all previously existing releases within the direct lineage of the current state.

        :param ignore_prereleases: If True, ignore pre-release versions when retrieving releases.
                                   If a callable is provided, it should accept a Version instance and return
                                   True if the version is a pre-release to be ignored.
        :type ignore_prereleases: bool | Callable[[Version], bool]
        :return: A sequence of Release instances.
        :rtype: Sequence[Release]
        """
        raise NotImplementedError  # pragma: no cover
