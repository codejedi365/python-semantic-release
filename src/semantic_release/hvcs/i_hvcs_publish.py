from __future__ import annotations

from abc import ABCMeta, abstractmethod


class HvcsPublishingClientInterface(metaclass=ABCMeta):

    @classmethod
    def __subclasshook__(cls, subclass) -> bool:
        # Validate that the subclass implements all of the abstract methods.
        # This supports isinstance and issubclass checks.
        return (
            cls is HvcsPublishingClientInterface
            and all(
                bool(hasattr(subclass, method) and callable(getattr(subclass, method)))
                for method in HvcsPublishingClientInterface.__abstractmethods__
            )
            or NotImplemented
        )

    @abstractmethod
    def upload_dists(self, tag: str, dist_glob: str) -> int:
        """
        Upload built distributions to a release on a remote VCS that
        supports such uploads
        """
        raise NotImplementedError
