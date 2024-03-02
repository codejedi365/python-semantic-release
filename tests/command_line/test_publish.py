from __future__ import annotations
from typing import TYPE_CHECKING
from unittest import mock

import pytest

from semantic_release.cli import main, publish
from semantic_release.hvcs import Github

if TYPE_CHECKING:
    from click.testing import CliRunner


publish_command = publish.name or publish.__name__


@pytest.mark.usefixtures("repo_with_single_branch_angular_commits")
@pytest.mark.parametrize("cmd_args", [(), ("--tag", "latest")])
def test_publish_latest_uses_latest_tag(
    cli_runner: CliRunner,
    cmd_args: tuple[str],
):
    # Prepare environment by patching the upload_dists method & the tags_and_versions
    # method to not require git interaction
    with mock.patch.object(Github, "upload_dists") as mocked_upload_dists, mock.patch(
        "semantic_release.cli.commands.publish.tags_and_versions",
        return_value=([("v1.0.0", "1.0.0")]),
    ) as mock_tags_and_versions:
        # Execute publish command within the mocked environment
        result = cli_runner.invoke(main, [publish_command, *cmd_args])

        # Evaluate
        assert result.exit_code == 0
        mock_tags_and_versions.assert_called_once()
        mocked_upload_dists.assert_called_once_with(tag="v1.0.0", dist_glob="dist/*")


@pytest.mark.usefixtures("repo_with_single_branch_angular_commits")
def test_publish_to_tag_uses_tag(cli_runner: CliRunner):
    tag = "v99.999.9999+build.1234"

    # Prepare environment by patching the upload_dists method & the tags_and_versions
    # method to not require git interaction
    with mock.patch.object(Github, "upload_dists") as mocked_upload_dists, mock.patch(
        "semantic_release.cli.commands.publish.tags_and_versions",
        return_value=([("v1.0.0", "1.0.0")]),
    ) as mock_tags_and_versions:
        # Execute publish command within the mocked environment
        result = cli_runner.invoke(main, [publish_command, "--tag", tag])

        # Evaluate
        assert result.exit_code == 0
        mock_tags_and_versions.assert_not_called()
        mocked_upload_dists.assert_called_once_with(tag=tag, dist_glob="dist/*")
