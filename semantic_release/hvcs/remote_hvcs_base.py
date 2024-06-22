"""Common functionality and interface for interacting with Git remote VCS"""

from __future__ import annotations

import logging
from abc import ABCMeta, abstractmethod
from pathlib import PurePosixPath
from typing import TYPE_CHECKING

from urllib3.util.url import Url, parse_url

from semantic_release.hvcs import RvcsInterface

if TYPE_CHECKING:
    from typing import Any


# Globals
logger = logging.getLogger(__name__)


class RemoteHvcsBase(metaclass=ABCMeta):
    """
    Interface for subclasses interacting with a remote VCS

    This abstract class is defined to provide common helper functions and
    a set of basic methods that all remote VCS environments usually support.

    If the remote vcs implementation (via subclass) does not support a functionality
    then it can just call super()'s method which defaults as a non-supported log
    message and empty results.  This is more straightforward than checking for
    NotImplemented around every function call in the core library code.
    """

    DEFAULT_ENV_TOKEN_NAME = "HVCS_TOKEN"  # noqa: S105
