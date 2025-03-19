from __future__ import annotations

import os
from typing import TYPE_CHECKING
from unittest import mock

import pytest

from semantic_release.cli.commands.main import main

from tests.const import EXAMPLE_HVCS_DOMAIN, EXAMPLE_REPO_NAME, EXAMPLE_REPO_OWNER, MAIN_PROG_NAME, VERSION_SUBCMD
from tests.fixtures.repos.trunk_based_dev.repo_w_no_tags import repo_w_no_tags_angular_commits
from tests.util import assert_successful_exit_code

if TYPE_CHECKING:
    from unittest.mock import MagicMock

    from click.testing import CliRunner
    from git.repo import Repo
    from requests_mock import Mocker

    from tests.fixtures.example_project import UpdatePyprojectTomlFn, UseHvcsFn


GITLAB_HEADER_NAME_JOB_TOKEN = "JOB-TOKEN"
GITLAB_HEADER_NAME_PAT = "PRIVATE-TOKEN"


@pytest.mark.parametrize(
    "patched_os_environ, token_env_name",
    [
        *[
            (
                {"CI_SERVER_VERSION": gl_version, "GITLAB_TOKEN": "gl_token-PAT", "CI_JOB_TOKEN": "gitlab-job-token"},
                token_name_to_use,
            )
            for gl_version in ["", "16.0.0", "17.1.0", "17.2.0", "17.2.1", "17.3.0", "18.0.0"]
            for token_name_to_use in [
                # When no token configuration, the default token name (GITLAB_TOKEN) is used, no matter the GitLab version
                # or existance of CI_JOB_TOKEN
                None,
                # When configured to use GITLAB_TOKEN, the PAT value is used, no matter the GitLab version
                # or existance of CI_JOB_TOKEN
                "GITLAB_TOKEN"
            ]
        ],
        *[
            # When configured to use CI_JOB_TOKEN, the CI_JOB_TOKEN is used only when GitLab version is 17.2.0 or later
            (
                {"CI_SERVER_VERSION": gl_version, "GITLAB_TOKEN": "gl_token-PAT", "CI_JOB_TOKEN": "gitlab-job-token"},
                "CI_JOB_TOKEN",
            )
            for gl_version in ["17.2.0", "17.2.1", "17.3.0", "18.0.0"]
        ],
    ],
)
@pytest.mark.usefixtures(repo_w_no_tags_angular_commits.__name__)
def test_gitlab_release_tokens(
    patched_os_environ: dict[str, str],
    token_env_name: str | None,
    cli_runner: CliRunner,
    use_gitlab_hvcs: UseHvcsFn,
    update_pyproject_toml: UpdatePyprojectTomlFn,
    mocked_git_push: MagicMock,
    requests_mock: Mocker,
) -> None:
    """Verify that gitlab tokens are used correctly."""
    release_id = 999
    expected_token = patched_os_environ[token_env_name or "GITLAB_TOKEN"]
    expected_header = (
        GITLAB_HEADER_NAME_JOB_TOKEN
        if token_env_name == "CI_JOB_TOKEN"
        else GITLAB_HEADER_NAME_PAT
    )

    # Setup
    use_gitlab_hvcs()
    if token_env_name is not None:
        update_pyproject_toml(
            "tool.semantic_release.remote.token.env",
            token_env_name,
        )

    requests_mock.register_uri(
        "GET",
        f"https://{EXAMPLE_HVCS_DOMAIN}/api/v4/projects/{EXAMPLE_REPO_OWNER}%2F{EXAMPLE_REPO_NAME}",
        json={"id": release_id},
        headers={"Content-Type": "application/json"},
    )

    requests_mock.register_uri(
        "POST",
        f"https://{EXAMPLE_HVCS_DOMAIN}/api/v4/projects/{release_id}/releases",
        json={"id": release_id},
        headers={"Content-Type": "application/json"},
    )

    with mock.patch.dict(os.environ, patched_os_environ, clear=True):
        # Act
        cli_cmd = [MAIN_PROG_NAME, VERSION_SUBCMD, "--vcs-release"]
        result = cli_runner.invoke(main, cli_cmd[1:])

    # Evaluate (expected -> actual)
    assert_successful_exit_code(result, cli_cmd)

    # Verify Git Push of commit and tag
    assert mocked_git_push.call_count == 2  # 1 for commit, 1 for tag
    assert expected_token in mocked_git_push.call_args_list[0].args[0]
    assert expected_token in mocked_git_push.call_args_list[1].args[0]

    # Verify API call for release creation
    assert requests_mock.call_count == 2
    assert requests_mock.last_request is not None
    assert requests_mock.request_history[0].method == "GET"
    assert requests_mock.request_history[1].method == "POST"

    for request in requests_mock.request_history:
        # make sure the correct header key exists
        assert expected_header in request._request.headers

        # make sure the value of the header is correct
        assert expected_token == request._request.headers[expected_header]

        # make sure the other header key does not exist
        assert GITLAB_HEADER_NAME_PAT not in request._request.headers
