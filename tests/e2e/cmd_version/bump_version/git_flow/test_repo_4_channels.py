from __future__ import annotations

import os
import shutil
from re import IGNORECASE, compile as regexp
from typing import TYPE_CHECKING

import pytest
import tomlkit
from flatdict import FlatDict
from freezegun import freeze_time

from semantic_release.cli.commands.main import main

from tests.const import (
    MAIN_PROG_NAME,
    VERSION_SUBCMD,
    RepoActionStep,
)
from tests.fixtures.repos.git_flow import (
    repo_w_git_flow_w_beta_alpha_rev_prereleases_n_angular_commits,
    repo_w_git_flow_w_beta_alpha_rev_prereleases_n_emoji_commits,
    repo_w_git_flow_w_beta_alpha_rev_prereleases_n_scipy_commits,
)
from tests.util import assert_successful_exit_code, temporary_working_directory

if TYPE_CHECKING:
    from pathlib import Path
    from unittest.mock import MagicMock

    from click.testing import CliRunner
    from requests_mock import Mocker

    from tests.fixtures.example_project import ExProjectDir
    from tests.fixtures.git_repo import (
        BuildRepoFromDefinitionFn,
        BuildSpecificRepoFn,
        CommitConvention,
        GetGitRepo4DirFn,
        GetVersionsFromRepoBuildDefFn,
        RepoActionConfigure,
        RepoActionRelease,
        RepoActions,
    )


@pytest.mark.parametrize(
    "repo_fixture_name",
    [
        repo_w_git_flow_w_beta_alpha_rev_prereleases_n_angular_commits.__name__,
        repo_w_git_flow_w_beta_alpha_rev_prereleases_n_emoji_commits.__name__,
        repo_w_git_flow_w_beta_alpha_rev_prereleases_n_scipy_commits.__name__,
    ],
)
def test_gitflow_repo_rebuild_4_channels(
    repo_fixture_name: str,
    cli_runner: CliRunner,
    build_git_flow_repo_w_4_release_channels: BuildSpecificRepoFn,
    get_versions_from_repo_build_def: GetVersionsFromRepoBuildDefFn,
    example_project_dir: ExProjectDir,
    git_repo_for_directory: GetGitRepo4DirFn,
    build_repo_from_definition: BuildRepoFromDefinitionFn,
    changelog_md_file: Path,
    changelog_rst_file: Path,
    mocked_git_push: MagicMock,
    post_mocker: Mocker,
    default_tag_format_str: str,
    default_md_changelog_insertion_flag: str,
    default_rst_changelog_insertion_flag: str,
    default_changelog_md_template: Path,
    default_changelog_rst_template: Path,
    changelog_template_dir: Path,
    version_py_file: Path,
):
    # build target repo into a temporary directory
    target_repo_dir = example_project_dir / repo_fixture_name
    commit_type: CommitConvention = repo_fixture_name.split("_")[-2]  # type: ignore[assignment]
    target_repo_definition = build_git_flow_repo_w_4_release_channels(
        repo_name=repo_fixture_name,
        commit_type=commit_type,
        dest_dir=target_repo_dir,
    )
    target_git_repo = git_repo_for_directory(target_repo_dir)
    versions = get_versions_from_repo_build_def(target_repo_definition)
    target_repo_pyproject_toml = FlatDict(
        tomlkit.loads((target_repo_dir / "pyproject.toml").read_text(encoding="utf-8")),
        delimiter=".",
    )
    tag_format_str: str = target_repo_pyproject_toml.get(  # type: ignore[assignment]
        "tool.semantic_release.tag_format",
        default_tag_format_str,
    )

    # split repo actions by release actions
    configuration_step: RepoActionConfigure
    releasetags_2_steps: dict[str, list[RepoActions]] = {}
    next_release_tag_gen = (
        tag_format_str.format(version=version) for version in versions
    )
    curr_release_tag = next(next_release_tag_gen)
    releasetags_2_steps[curr_release_tag] = []
    for step in target_repo_definition:
        if step["action"] == RepoActionStep.CONFIGURE:
            configuration_step = step  # type: ignore[assignment]
            continue

        if step["action"] == RepoActionStep.WRITE_CHANGELOGS:
            continue

        releasetags_2_steps[curr_release_tag].append(step)

        if step["action"] == RepoActionStep.RELEASE:
            try:
                curr_release_tag = next(next_release_tag_gen)
                releasetags_2_steps[curr_release_tag] = []
            except StopIteration:
                curr_release_tag = "Unreleased"
                releasetags_2_steps[curr_release_tag] = []

    if "Unreleased" in releasetags_2_steps and not releasetags_2_steps["Unreleased"]:
        del releasetags_2_steps["Unreleased"]

    # new repo destination
    mirror_repo_dir = example_project_dir / "mirror"

    # Create the mirror repo directory
    mirror_repo_dir.mkdir(exist_ok=True, parents=True)

    # Force custom changelog to be a copy of the default changelog (md and rst)
    shutil.copytree(
        src=default_changelog_md_template.parent,
        dst=mirror_repo_dir / changelog_template_dir,
        dirs_exist_ok=True,
    )
    shutil.copytree(
        src=default_changelog_rst_template.parent,
        dst=mirror_repo_dir / changelog_template_dir,
        dirs_exist_ok=True,
    )

    # Initialize repository
    build_repo_from_definition(
        dest_dir=mirror_repo_dir,
        repo_construction_steps=[configuration_step],
    )
    mirror_git_repo = git_repo_for_directory(mirror_repo_dir)
    mirror_git_repo.git.add(str(changelog_template_dir))

    # rebuild repo from scratch stopping before each release tag
    for curr_release_tag, steps in releasetags_2_steps.items():
        # make sure mocks are clear
        mocked_git_push.reset_mock()
        post_mocker.reset_mock()

        # Capture expected result before running the version command
        target_git_repo.git.checkout(curr_release_tag, detach=True)

        # TODO: v10 change -- default turns to update so this is not needed
        # Because we are in init mode, the insertion flag is not present in the changelog
        # we must take it out manually because our repo generation fixture includes it automatically
        with (target_repo_dir / changelog_md_file).open(newline=os.linesep) as rfd:
            # use os.linesep here because the insertion flag is os-specific
            # but convert the content to universal newlines for comparison
            expected_md_changelog_content = (
                rfd.read()
                .replace(f"{default_md_changelog_insertion_flag}{os.linesep}", "")
                .replace("\r", "")
            )
        with (target_repo_dir / changelog_rst_file).open(newline=os.linesep) as rfd:
            expected_rst_changelog_content = (
                rfd.read()
                .replace(f"{default_rst_changelog_insertion_flag}{os.linesep}", "")
                .replace("\r", "")
            )

        # zeroize the commit hashes
        long_hash_pattern = regexp(r"\b([0-9a-f]{40})\b", IGNORECASE)
        short_hash_pattern = regexp(r"\b([0-9a-f]{7})\b", IGNORECASE)
        rst_short_hash_link_pattern = regexp(r"(_[0-9a-f]{7})\b", IGNORECASE)

        expected_md_changelog_content = long_hash_pattern.sub(
            "0" * 40, expected_md_changelog_content
        )
        expected_md_changelog_content = short_hash_pattern.sub(
            "0" * 7, expected_md_changelog_content
        )
        expected_rst_changelog_content = long_hash_pattern.sub(
            "0" * 40, expected_rst_changelog_content
        )
        expected_rst_changelog_content = short_hash_pattern.sub(
            "0" * 7, expected_rst_changelog_content
        )
        expected_rst_changelog_content = rst_short_hash_link_pattern.sub(
            f'_{"0" * 7}', expected_rst_changelog_content
        )

        expected_pyproject_toml_content = (
            target_repo_dir / "pyproject.toml"
        ).read_text()
        expected_version_file_content = (target_repo_dir / version_py_file).read_text()
        expected_release_commit_text = target_git_repo.head.commit.message

        # In our repo env, start building the repo from the definition
        build_repo_from_definition(
            dest_dir=mirror_repo_dir,
            repo_construction_steps=steps[:-1],  # stop before the release step
        )
        release_action_step: RepoActionRelease = steps[-1]  # type: ignore[assignment]

        # Act: run PSR on the repo instead of the RELEASE step
        with freeze_time(
            release_action_step["details"]["datetime"]
        ), temporary_working_directory(mirror_repo_dir):
            cli_cmd = [MAIN_PROG_NAME, "--strict", VERSION_SUBCMD]
            result = cli_runner.invoke(main, cli_cmd[1:])

        # take measurement after running the version command
        actual_release_commit_text = mirror_git_repo.head.commit.message

        actual_md_changelog_content = (mirror_repo_dir / changelog_md_file).read_text()
        actual_md_changelog_content = long_hash_pattern.sub(
            "0" * 40, actual_md_changelog_content
        )
        actual_md_changelog_content = short_hash_pattern.sub(
            "0" * 7, actual_md_changelog_content
        )

        actual_rst_changelog_content = (
            mirror_repo_dir / changelog_rst_file
        ).read_text()
        actual_rst_changelog_content = long_hash_pattern.sub(
            "0" * 40, actual_rst_changelog_content
        )
        actual_rst_changelog_content = short_hash_pattern.sub(
            "0" * 7, actual_rst_changelog_content
        )
        actual_rst_changelog_content = rst_short_hash_link_pattern.sub(
            f'_{"0" * 7}', actual_rst_changelog_content
        )

        actual_pyproject_toml_content = (mirror_repo_dir / "pyproject.toml").read_text()
        actual_version_file_content = (mirror_repo_dir / version_py_file).read_text()

        # Evaluate (normal release actions should have occurred as expected)
        assert_successful_exit_code(result, cli_cmd)
        # Make sure version file is updated
        assert expected_pyproject_toml_content == actual_pyproject_toml_content
        assert expected_version_file_content == actual_version_file_content
        # Make sure changelog is updated
        assert expected_md_changelog_content == actual_md_changelog_content
        assert expected_rst_changelog_content == actual_rst_changelog_content
        # Make sure commit is created
        assert expected_release_commit_text == actual_release_commit_text
        # Make sure tag is created
        assert curr_release_tag in [tag.name for tag in mirror_git_repo.tags]
        assert mocked_git_push.call_count == 2  # 1 for commit, 1 for tag
        assert post_mocker.call_count == 1  # vcs release creation occured
