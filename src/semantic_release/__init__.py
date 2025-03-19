"""Python Semantic Release"""

from __future__ import annotations

__version__ = "9.17.0"


def setup_hook(argv: list[str]) -> None:
    """
    A hook to be used in setup.py to enable `python setup.py publish`.

    :param argv: sys.argv
    """
    if len(argv) > 1 and any(
        cmd in argv for cmd in ["version", "publish", "changelog"]
    ):
        from semantic_release.cli.commands.main import main

        main()
