from semantic_release.hvcs._base import HvcsBase
from typing import Any

class UnsupportedVCS(HvcsBase):
    """This class is used as a fallback when no supported VCS is found."""
    DEFAULT_ENV_TOKEN_NAME = "" # purposely empty

    def __init__(self, remote_url: str, **kwargs: Any) -> None:
        super().__init__(remote_url, **kwargs)
