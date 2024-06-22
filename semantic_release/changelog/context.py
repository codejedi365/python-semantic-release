from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Callable

from semantic_release import hvcs

if TYPE_CHECKING:
    from jinja2 import Environment

    from semantic_release.changelog.release_history import ReleaseHistory
    from semantic_release.hvcs.i_changelog_support import HvcsChangelogClientInterface


@dataclass
class ChangelogContext:
    repo_name: str
    # TODO: change repo_owner to repo_namespace
    repo_owner: str
    hvcs_type: str
    history: ReleaseHistory
    filters: tuple[Callable[..., Any], ...] = ()

    def bind_to_environment(self, env: Environment) -> Environment:
        env.globals["context"] = self
        for f in self.filters:
            env.filters[f.__name__] = f
        return env


# TODO: is this even necessary?
def make_changelog_context(
    repo_name: str,
    repo_namespace: str,
    release_history: ReleaseHistory,
    hvcs_client: HvcsChangelogClientInterface | None = None,
) -> ChangelogContext:
    hvcs_filters = () if hvcs_client is None else hvcs_client.get_changelog_context_filters()

    return ChangelogContext(
        repo_name=repo_name,
        repo_owner=repo_namespace,
        history=release_history,
        hvcs_type=(
            str(None).lower()
            if hvcs_client is None
            else hvcs_client.__class__.__name__.lower()
        ),
        filters=(*hvcs_filters,),
    )
