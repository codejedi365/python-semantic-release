"""Common functionality and interface for interacting with Git remote VCS"""

from __future__ import annotations

from abc import ABCMeta, abstractmethod

class RvcsInterface(metaclass=ABCMeta):
    """
    Interface for subclasses interacting with a remote vcs environment

    Methods generally have a base implementation are implemented here but
    likely just provide a not-supported message but return gracefully

    This class cannot be instantiated directly but must be inherited from
    and implement the designated abstract methods.
    """

    @classmethod
    def __subclasshook__(cls, subclass: type) -> bool:
        # Validate that the subclass implements all of the abstract methods.
        # This supports isinstance and issubclass checks.
        return (
            cls is RvcsInterface
            and all(
                bool(hasattr(subclass, method) and callable(getattr(subclass, method)))
                for method in RvcsInterface.__abstractmethods__
            )
            or NotImplemented
        )

    @abstractmethod
    def remote_url(self, use_token: bool) -> str:
        """
        Return the remote URL for the repository, including the token for
        authentication if requested by setting the `use_token` parameter to True,
        """
        raise NotImplementedError

    @abstractmethod
    def get_owner_namespace(self) -> str:
        """
        Return the namespace of the repository
        """
        raise NotImplementedError

    @abstractmethod
    def get_repo_name(self) -> str:
        """
        Return the name of the repository
        """
        raise NotImplementedError
