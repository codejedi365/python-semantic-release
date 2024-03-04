from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

# Limitation in pytest-lazy-fixture - see https://stackoverflow.com/a/69884019
from pytest_lazyfixture import lazy_fixture

from semantic_release.version.algorithm import next_version
from semantic_release.version.translator import VersionTranslator
from semantic_release.version.version import Version

from tests.const import (
    ANGULAR_COMMITS_MAJOR,
    ANGULAR_COMMITS_MINOR,
    ANGULAR_COMMITS_PATCH,
    EMOJI_COMMITS_MAJOR,
    EMOJI_COMMITS_MINOR,
    EMOJI_COMMITS_PATCH,
    TAG_COMMITS_MAJOR,
    TAG_COMMITS_MINOR,
    TAG_COMMITS_PATCH,
)
from tests.fixtures import (
    default_tag_parser,
    repo_w_github_flow_w_feature_release_channel_tag_commits,
    repo_with_no_tags_tag_commits,
    repo_with_single_branch_and_prereleases_tag_commits,
    repo_with_single_branch_tag_commits,
    default_angular_parser,
    default_emoji_parser,
    repo_with_git_flow_angular_commits,
    repo_with_git_flow_emoji_commits,
    repo_with_git_flow_scipy_commits,
    repo_with_git_flow_tag_commits,
    repo_with_git_flow_and_release_channels_angular_commits,
    repo_with_git_flow_and_release_channels_emoji_commits,
    repo_with_git_flow_and_release_channels_scipy_commits,
    repo_with_git_flow_and_release_channels_tag_commits,
    default_scipy_parser,
    repo_w_github_flow_w_feature_release_channel_angular_commits,
    repo_with_no_tags_angular_commits,
    repo_with_single_branch_and_prereleases_angular_commits,
    repo_with_single_branch_angular_commits,
    scipy_chore_commits,
    scipy_major_commits,
    scipy_minor_commits,
    scipy_patch_commits,
)
from tests.util import add_text_to_file, xdist_sort_hack

if TYPE_CHECKING:
    from git import Repo


@pytest.fixture
def angular_major_commits():
    return ANGULAR_COMMITS_MAJOR

@pytest.fixture
def angular_minor_commits():
    return ANGULAR_COMMITS_MINOR

@pytest.fixture
def angular_patch_commits():
    return ANGULAR_COMMITS_PATCH


@pytest.fixture
def angular_chore_commits() -> list[str]:
    return ["chore: change dev tool configuration"]


@pytest.fixture
def emoji_major_commits():
    return EMOJI_COMMITS_MAJOR


@pytest.fixture
def emoji_minor_commits():
    return EMOJI_COMMITS_MINOR


@pytest.fixture
def emoji_patch_commits():
    return EMOJI_COMMITS_PATCH


@pytest.fixture
def emoji_chore_commits() -> list[str]:
    return [":broom: change dev tool configuration"]


@pytest.fixture
def tag_patch_commits():
    return TAG_COMMITS_PATCH


@pytest.fixture
def tag_minor_commits():
    return TAG_COMMITS_MINOR


@pytest.fixture
def tag_major_commits():
    return TAG_COMMITS_MAJOR


@pytest.fixture
def tag_chore_commits() -> list[str]:
    return [":broom: change dev tool configuration"]


# TODO: it'd be nice to not hard-code the versions into
# this testing


# NOTE: There is a bit of a corner-case where if we are not doing a
# prerelease, we will get a full version based on already-released commits.
# So for example, commits that wouldn't trigger a release on a prerelease branch
# won't trigger a release if prerelease=true; however, when commits included in a
# prerelease branch are merged to a release branch, prerelease=False - so a feat commit
# which previously triggered a prerelease on a branch will subsequently trigger a full
# release when merged to a full release branch where prerelease=False.
# For this reason a couple of these test cases predict a new version even when the
# commits being added here don't induce a version bump.
@pytest.mark.parametrize(
    "repo, commit_parser, translator, commit_messages,"
    "prerelease, expected_new_version",
    xdist_sort_hack(
        [
            (
                lazy_fixture(repo_fixture_name),
                lazy_fixture(parser_fixture_name),
                translator,
                commit_messages,
                prerelease,
                expected_new_version,
            )
            for (repo_fixture_name, parser_fixture_name, translator), values in {
                # Latest version for repo_with_git_flow is currently 1.2.0-rc.2
                # The last full release version was 1.1.1, so it's had a minor
                # prerelease
                (
                    repo_with_git_flow_angular_commits.__name__,
                    default_angular_parser.__name__,
                    VersionTranslator(prerelease_token="alpha"),
                ): [
                    *(
                        (commits, True, "1.2.0-alpha.2")
                        for commits in (
                            None,
                            lazy_fixture(angular_chore_commits.__name__),
                        )
                    ),
                    # Models a merge of commits from the branch to the main branch, now
                    # that prerelease=False
                    *(
                        (commits, False, "1.2.0")
                        for commits in (
                            None,
                            lazy_fixture(angular_chore_commits.__name__),
                        )
                    ),
                    (lazy_fixture(angular_patch_commits.__name__), False, "1.2.0"),
                    (lazy_fixture(angular_patch_commits.__name__), True, "1.2.0-alpha.3"),
                    (lazy_fixture(angular_minor_commits.__name__), False, "1.2.0"),
                    (lazy_fixture(angular_minor_commits.__name__), True, "1.2.0-alpha.3"),
                    (lazy_fixture(angular_major_commits.__name__), False, "2.0.0"),
                    (lazy_fixture(angular_major_commits.__name__), True, "2.0.0-alpha.1"),
                ],
                # Latest version for repo_with_git_flow_and_release_channels is
                # currently 1.1.0-alpha.3
                # The last full release version was 1.0.0, so it's had a minor
                # prerelease
                (
                    repo_with_git_flow_and_release_channels_angular_commits.__name__,
                    default_angular_parser.__name__,
                    VersionTranslator(prerelease_token="alpha"),
                ): [
                    *(
                        (commits, True, "1.1.0-alpha.3")
                        for commits in (
                            None,
                            lazy_fixture(angular_chore_commits.__name__),
                        )
                    ),
                    # Models a merge of commits from the branch to the main branch, now
                    # that prerelease=False
                    *(
                        (commits, False, "1.1.0")
                        for commits in (
                            None,
                            lazy_fixture(angular_chore_commits.__name__),
                        )
                    ),
                    (lazy_fixture(angular_patch_commits.__name__), False, "1.1.0"),
                    (lazy_fixture(angular_patch_commits.__name__), True, "1.1.0-alpha.4"),
                    (lazy_fixture(angular_minor_commits.__name__), False, "1.1.0"),
                    (lazy_fixture(angular_minor_commits.__name__), True, "1.1.0-alpha.4"),
                    (lazy_fixture(angular_major_commits.__name__), False, "2.0.0"),
                    (lazy_fixture(angular_major_commits.__name__), True, "2.0.0-alpha.1"),
                ],
            }.items()
            for (commit_messages, prerelease, expected_new_version) in values
        ]
    ),
)
@pytest.mark.parametrize("major_on_zero", [True, False])
@pytest.mark.parametrize("allow_zero_version", [True, False])
def test_algorithm_no_zero_dot_versions_angular(
    repo,
    file_in_repo,
    commit_parser,
    translator,
    commit_messages,
    prerelease,
    expected_new_version,
    major_on_zero,
    allow_zero_version,
):
    # Setup
    for commit_message in commit_messages or []:
        add_text_to_file(repo, file_in_repo)
        repo.git.commit(m=commit_message)

    # Action
    new_version = next_version(
        repo, translator, commit_parser, prerelease, major_on_zero, allow_zero_version
    )

    # Verify
    assert expected_new_version == str(new_version)


@pytest.mark.parametrize(
    "repo, commit_parser, translator, commit_messages,"
    "prerelease, expected_new_version",
    xdist_sort_hack(
        [
            (
                lazy_fixture(repo_fixture_name),
                lazy_fixture(parser_fixture_name),
                translator,
                commit_messages,
                prerelease,
                expected_new_version,
            )
            for (repo_fixture_name, parser_fixture_name, translator), values in {
                # Latest version for repo_with_git_flow is currently 1.2.0-alpha.2
                # The last full release version was 1.1.1, so it's had a minor
                # prerelease
                (
                    repo_with_git_flow_emoji_commits.__name__,
                    default_emoji_parser.__name__,
                    VersionTranslator(prerelease_token="alpha"),
                ): [
                    *(
                        (commits, True, "1.2.0-alpha.2")
                        for commits in (
                            None,
                            lazy_fixture(emoji_chore_commits.__name__),
                        )
                    ),
                    # Models a merge of commits from the branch to the main branch, now
                    # that prerelease=False
                    *(
                        (commits, False, "1.2.0")
                        for commits in (
                            None,
                            lazy_fixture(emoji_chore_commits.__name__),
                        )
                    ),
                    (lazy_fixture(emoji_patch_commits.__name__), False, "1.2.0"),
                    (lazy_fixture(emoji_patch_commits.__name__), True, "1.2.0-alpha.3"),
                    (lazy_fixture(emoji_minor_commits.__name__), False, "1.2.0"),
                    (lazy_fixture(emoji_minor_commits.__name__), True, "1.2.0-alpha.3"),
                    (lazy_fixture(emoji_major_commits.__name__), False, "2.0.0"),
                    (lazy_fixture(emoji_major_commits.__name__), True, "2.0.0-alpha.1"),
                ],
                # Latest version for repo_with_git_flow_and_release_channels is
                # currently 1.1.0-alpha.3
                # The last full release version was 1.0.0, so it's had a minor
                # prerelease
                (
                    repo_with_git_flow_and_release_channels_emoji_commits.__name__,
                    default_emoji_parser.__name__,
                    VersionTranslator(prerelease_token="alpha"),
                ): [
                    *(
                        (commits, True, "1.1.0-alpha.3")
                        for commits in (
                            None,
                            lazy_fixture(emoji_chore_commits.__name__),
                        )
                    ),
                    # Models a merge of commits from the branch to the main branch, now
                    # that prerelease=False
                    *(
                        (commits, False, "1.1.0")
                        for commits in (
                            None,
                            lazy_fixture(emoji_chore_commits.__name__),
                        )
                    ),
                    (lazy_fixture(emoji_patch_commits.__name__), False, "1.1.0"),
                    (lazy_fixture(emoji_patch_commits.__name__), True, "1.1.0-alpha.4"),
                    (lazy_fixture(emoji_minor_commits.__name__), False, "1.1.0"),
                    (lazy_fixture(emoji_minor_commits.__name__), True, "1.1.0-alpha.4"),
                    (lazy_fixture(emoji_major_commits.__name__), False, "2.0.0"),
                    (lazy_fixture(emoji_major_commits.__name__), True, "2.0.0-alpha.1"),
                ],
            }.items()
            for (commit_messages, prerelease, expected_new_version) in values
        ]
    ),
)
@pytest.mark.parametrize("major_on_zero", [True, False])
@pytest.mark.parametrize("allow_zero_version", [True, False])
def test_algorithm_no_zero_dot_versions_emoji(
    repo,
    file_in_repo,
    commit_parser,
    translator,
    commit_messages,
    prerelease,
    expected_new_version,
    major_on_zero,
    allow_zero_version,
):
    # Setup
    for commit_message in commit_messages or []:
        add_text_to_file(repo, file_in_repo)
        repo.git.commit(m=commit_message)

    # Action
    new_version = next_version(
        repo, translator, commit_parser, prerelease, major_on_zero, allow_zero_version
    )

    # Verify
    assert expected_new_version == str(new_version)


@pytest.mark.parametrize(
    "repo, commit_parser, translator, commit_messages,"
    "prerelease, expected_new_version",
    xdist_sort_hack(
        [
            (
                lazy_fixture(repo_fixture_name),
                lazy_fixture(parser_fixture_name),
                translator,
                commit_messages,
                prerelease,
                expected_new_version,
            )
            for (repo_fixture_name, parser_fixture_name, translator), values in {
                # Latest version for repo_with_git_flow is currently 1.2.0-alpha.2
                # The last full release version was 1.1.1, so it's had a minor
                # prerelease
                (
                    repo_with_git_flow_scipy_commits.__name__,
                    default_scipy_parser.__name__,
                    VersionTranslator(prerelease_token="alpha"),
                ): [
                    *(
                        (commits, True, "1.2.0-alpha.2")
                        for commits in (
                            None,
                            lazy_fixture(scipy_chore_commits.__name__),
                        )
                    ),
                    # Models a merge of commits from the branch to the main branch, now
                    # that prerelease=False
                    *(
                        (commits, False, "1.2.0")
                        for commits in (
                            None,
                            lazy_fixture(scipy_chore_commits.__name__),
                        )
                    ),
                    (lazy_fixture(scipy_patch_commits.__name__), False, "1.2.0"),
                    (lazy_fixture(scipy_patch_commits.__name__), True, "1.2.0-alpha.3"),
                    (lazy_fixture(scipy_minor_commits.__name__), False, "1.2.0"),
                    (lazy_fixture(scipy_minor_commits.__name__), True, "1.2.0-alpha.3"),
                    (lazy_fixture(scipy_major_commits.__name__), False, "2.0.0"),
                    (lazy_fixture(scipy_major_commits.__name__), True, "2.0.0-alpha.1"),
                ],
                # Latest version for repo_with_git_flow_and_release_channels is
                # currently 1.1.0-alpha.3
                # The last full release version was 1.0.0, so it's had a minor
                # prerelease
                (
                    repo_with_git_flow_and_release_channels_scipy_commits.__name__,
                    default_scipy_parser.__name__,
                    VersionTranslator(prerelease_token="alpha"),
                ): [
                    *(
                        (commits, True, "1.1.0-alpha.3")
                        for commits in (
                            None,
                            lazy_fixture(scipy_chore_commits.__name__),
                        )
                    ),
                    # Models a merge of commits from the branch to the main branch, now
                    # that prerelease=False
                    *(
                        (commits, False, "1.1.0")
                        for commits in (
                            None,
                            lazy_fixture(scipy_chore_commits.__name__),
                        )
                    ),
                    (lazy_fixture(scipy_patch_commits.__name__), False, "1.1.0"),
                    (lazy_fixture(scipy_patch_commits.__name__), True, "1.1.0-alpha.4"),
                    (lazy_fixture(scipy_minor_commits.__name__), False, "1.1.0"),
                    (lazy_fixture(scipy_minor_commits.__name__), True, "1.1.0-alpha.4"),
                    (lazy_fixture(scipy_major_commits.__name__), False, "2.0.0"),
                    (lazy_fixture(scipy_major_commits.__name__), True, "2.0.0-alpha.1"),
                ],
            }.items()
            for (commit_messages, prerelease, expected_new_version) in values
        ]
    ),
)
@pytest.mark.parametrize("major_on_zero", [True, False])
@pytest.mark.parametrize("allow_zero_version", [True, False])
def test_algorithm_no_zero_dot_versions_scipy(
    repo,
    file_in_repo,
    commit_parser,
    translator,
    commit_messages,
    prerelease,
    expected_new_version,
    major_on_zero,
    allow_zero_version,
):
    # Setup
    for commit_message in commit_messages or []:
        add_text_to_file(repo, file_in_repo)
        repo.git.commit(m=commit_message)

    # Action
    new_version = next_version(
        repo, translator, commit_parser, prerelease, major_on_zero, allow_zero_version
    )

    # Verify
    assert expected_new_version == str(new_version)


@pytest.mark.parametrize(
    "repo, commit_parser, translator, commit_messages,"
    "prerelease, expected_new_version",
    xdist_sort_hack(
        [
            (
                lazy_fixture(repo_fixture_name),
                lazy_fixture(parser_fixture_name),
                translator,
                commit_messages,
                prerelease,
                expected_new_version,
            )
            for (repo_fixture_name, parser_fixture_name, translator), values in {
                # Latest version for repo_with_git_flow is currently 1.2.0-rc.2
                # The last full release version was 1.1.1, so it's had a minor
                # prerelease
                (
                    repo_with_git_flow_tag_commits.__name__,
                    default_tag_parser.__name__,
                    VersionTranslator(prerelease_token="alpha"),
                ): [
                    *(
                        (commits, True, "1.2.0-alpha.2")
                        for commits in (
                            None,
                            lazy_fixture(tag_chore_commits.__name__),
                        )
                    ),
                    # Models a merge of commits from the branch to the main branch, now
                    # that prerelease=False
                    *(
                        (commits, False, "1.2.0")
                        for commits in (
                            None,
                            lazy_fixture(tag_chore_commits.__name__),
                        )
                    ),
                    (lazy_fixture(tag_patch_commits.__name__), False, "1.2.0"),
                    (lazy_fixture(tag_patch_commits.__name__), True, "1.2.0-alpha.3"),
                    (lazy_fixture(tag_minor_commits.__name__), False, "1.2.0"),
                    (lazy_fixture(tag_minor_commits.__name__), True, "1.2.0-alpha.3"),
                    (lazy_fixture(tag_major_commits.__name__), False, "2.0.0"),
                    (lazy_fixture(tag_major_commits.__name__), True, "2.0.0-alpha.1"),
                ],
                # Latest version for repo_with_git_flow_and_release_channels is
                # currently 1.1.0-alpha.3
                # The last full release version was 1.0.0, so it's had a minor
                # prerelease
                (
                    repo_with_git_flow_and_release_channels_tag_commits.__name__,
                    default_tag_parser.__name__,
                    VersionTranslator(prerelease_token="alpha"),
                ): [
                    *(
                        (commits, True, "1.1.0-alpha.3")
                        for commits in (
                            None,
                            lazy_fixture(tag_chore_commits.__name__),
                        )
                    ),
                    # Models a merge of commits from the branch to the main branch, now
                    # that prerelease=False
                    *(
                        (commits, False, "1.1.0")
                        for commits in (
                            None,
                            lazy_fixture(tag_chore_commits.__name__),
                        )
                    ),
                    (lazy_fixture(tag_patch_commits.__name__), False, "1.1.0"),
                    (lazy_fixture(tag_patch_commits.__name__), True, "1.1.0-alpha.4"),
                    (lazy_fixture(tag_minor_commits.__name__), False, "1.1.0"),
                    (lazy_fixture(tag_minor_commits.__name__), True, "1.1.0-alpha.4"),
                    (lazy_fixture(tag_major_commits.__name__), False, "2.0.0"),
                    (lazy_fixture(tag_major_commits.__name__), True, "2.0.0-alpha.1"),
                ],
            }.items()
            for (commit_messages, prerelease, expected_new_version) in values
        ]
    ),
)
@pytest.mark.parametrize("major_on_zero", [True, False])
@pytest.mark.parametrize("allow_zero_version", [True, False])
def test_algorithm_no_zero_dot_versions_tag(
    repo,
    file_in_repo,
    commit_parser,
    translator,
    commit_messages,
    prerelease,
    expected_new_version,
    major_on_zero,
    allow_zero_version,
):
    # Setup
    for commit_message in commit_messages or []:
        add_text_to_file(repo, file_in_repo)
        repo.git.commit(m=commit_message)

    # Action
    new_version = next_version(
        repo, translator, commit_parser, prerelease, major_on_zero, allow_zero_version
    )

    # Verify
    assert expected_new_version == str(new_version)


#####
# 0.x.y versions
#####


@pytest.mark.parametrize(
    "repo, commit_parser, translator, commit_messages,"
    "prerelease, major_on_zero, expected_new_version",
    xdist_sort_hack(
        [
            (
                lazy_fixture(repo_fixture_name),
                lazy_fixture(parser_fixture_name),
                translator,
                commit_messages,
                prerelease,
                major_on_zero,
                expected_new_version,
            )
            for (repo_fixture_name, parser_fixture_name, translator), values in {
                # Latest version for repo_with_no_tags is currently 0.0.0 (default)
                # It's biggest change type is minor, so the next version should be 0.1.0
                (
                    repo_with_no_tags_angular_commits.__name__,
                    default_angular_parser.__name__,
                    VersionTranslator(),
                ): [
                    *(
                        (commits, False, major_on_zero, "0.1.0")
                        for major_on_zero in (True, False)
                        for commits in (
                            None,
                            lazy_fixture(angular_chore_commits.__name__),
                            lazy_fixture(angular_patch_commits.__name__),
                            lazy_fixture(angular_minor_commits.__name__),
                        )
                    ),
                    (lazy_fixture(angular_major_commits.__name__), False, False, "0.1.0"),
                    (lazy_fixture(angular_major_commits.__name__), False, True, "1.0.0"),
                ],
                # Latest version for repo_with_single_branch is currently 0.1.1
                # Note repo_with_single_branch isn't modelled with prereleases
                (
                    repo_with_single_branch_angular_commits.__name__,
                    default_angular_parser.__name__,
                    VersionTranslator(),
                ): [
                    *(
                        (commits, False, major_on_zero, "0.1.1")
                        for major_on_zero in (True, False)
                        for commits in (
                            None,
                            lazy_fixture(angular_chore_commits.__name__),
                        )
                    ),
                    *(
                        (lazy_fixture(angular_patch_commits.__name__), False, major_on_zero, "0.1.2")
                        for major_on_zero in (True, False)
                    ),
                    *(
                        (lazy_fixture(angular_minor_commits.__name__), False, major_on_zero, "0.2.0")
                        for major_on_zero in (True, False)
                    ),
                    (lazy_fixture(angular_major_commits.__name__), False, False, "0.2.0"),
                    (lazy_fixture(angular_major_commits.__name__), False, True, "1.0.0"),
                ],
                # Latest version for repo_with_single_branch_and_prereleases is
                # currently 0.2.0
                (
                    repo_with_single_branch_and_prereleases_angular_commits.__name__,
                    default_angular_parser.__name__,
                    VersionTranslator(),
                ): [
                    *(
                        (commits, prerelease, major_on_zero, "0.2.0")
                        for prerelease in (True, False)
                        for major_on_zero in (True, False)
                        for commits in (
                            None,
                            lazy_fixture(angular_chore_commits.__name__)
                        )
                    ),
                    *(
                        (lazy_fixture(angular_patch_commits.__name__), False, major_on_zero, "0.2.1")
                        for major_on_zero in (True, False)
                    ),
                    *(
                        (lazy_fixture(angular_patch_commits.__name__), True, major_on_zero, "0.2.1-rc.1")
                        for major_on_zero in (True, False)
                    ),
                    *(
                        (lazy_fixture(angular_minor_commits.__name__), False, major_on_zero, "0.3.0")
                        for major_on_zero in (True, False)
                    ),
                    *(
                        (lazy_fixture(angular_minor_commits.__name__), True, major_on_zero, "0.3.0-rc.1")
                        for major_on_zero in (True, False)
                    ),
                    (lazy_fixture(angular_major_commits.__name__), False, True, "1.0.0"),
                    (lazy_fixture(angular_major_commits.__name__), True, True, "1.0.0-rc.1"),
                    (lazy_fixture(angular_major_commits.__name__), False, False, "0.3.0"),
                    (lazy_fixture(angular_major_commits.__name__), True, False, "0.3.0-rc.1"),
                ],
                # Latest version for repo_with_main_and_feature_branches is currently
                # 0.3.0-rc.1.
                # The last full release version was 0.2.0, so it's had a minor
                # prerelease
                (
                    repo_w_github_flow_w_feature_release_channel_angular_commits.__name__,
                    default_angular_parser.__name__,
                    VersionTranslator(prerelease_token="beta"),
                ): [
                    *(
                        (commits, True, major_on_zero, "0.3.0-beta.1")
                        for major_on_zero in (True, False)
                        for commits in (None, lazy_fixture(angular_chore_commits.__name__))
                    ),
                    # Models a merge of commits from the branch to the main branch, now
                    # that prerelease=False
                    *(
                        (commits, False, major_on_zero, "0.3.0")
                        for major_on_zero in (True, False)
                        for commits in (None, lazy_fixture(angular_chore_commits.__name__))
                    ),
                    *(
                        (lazy_fixture(angular_patch_commits.__name__), False, major_on_zero, "0.3.0")
                        for major_on_zero in (True, False)
                    ),
                    *(
                        (lazy_fixture(angular_patch_commits.__name__), True, major_on_zero, "0.3.0-beta.2")
                        for major_on_zero in (True, False)
                    ),
                    *(
                        (lazy_fixture(angular_minor_commits.__name__), False, major_on_zero, "0.3.0")
                        for major_on_zero in (True, False)
                    ),
                    *(
                        (lazy_fixture(angular_minor_commits.__name__), True, major_on_zero, "0.3.0-beta.2")
                        for major_on_zero in (True, False)
                    ),
                    (lazy_fixture(angular_major_commits.__name__), False, True, "1.0.0"),
                    (lazy_fixture(angular_major_commits.__name__), True, True, "1.0.0-beta.1"),
                    (lazy_fixture(angular_major_commits.__name__), False, False, "0.3.0"),
                    # Note - since breaking changes are absorbed into the minor digit
                    # with major_on_zero = False, and that's already been incremented
                    # since the last full release, the breaking change here will only
                    # trigger a prerelease revision
                    (lazy_fixture(angular_major_commits.__name__), True, False, "0.3.0-beta.2"),
                ],
            }.items()
            for (
                commit_messages,
                prerelease,
                major_on_zero,
                expected_new_version,
            ) in values
        ]
    ),
)
def test_algorithm_with_zero_dot_versions_angular(
    repo,
    file_in_repo,
    commit_parser,
    translator,
    commit_messages,
    prerelease,
    expected_new_version,
    major_on_zero,
    allow_zero_version,
):
    # Setup
    for commit_message in commit_messages or []:
        add_text_to_file(repo, file_in_repo)
        repo.git.commit(m=commit_message)

    # Action
    new_version = next_version(
        repo, translator, commit_parser, prerelease, major_on_zero, allow_zero_version
    )

    # Verify
    assert expected_new_version == str(new_version)


@pytest.mark.parametrize(
    "repo, commit_parser, translator, commit_messages,"
    "prerelease, major_on_zero, expected_new_version",
    xdist_sort_hack(
        [
            (
                lazy_fixture(repo_fixture_name),
                lazy_fixture(parser_fixture_name),
                translator,
                commit_messages,
                prerelease,
                major_on_zero,
                expected_new_version,
            )
            for (repo_fixture_name, parser_fixture_name, translator), values in {
                # Latest version for repo_with_no_tags is currently 0.0.0 (default)
                # It's biggest change type is minor, so the next version should be 0.1.0
                (
                    "repo_with_no_tags_emoji_commits",
                    "default_emoji_parser",
                    VersionTranslator(),
                ): [
                    *(
                        (commits, False, major_on_zero, "0.1.0")
                        for major_on_zero in (True, False)
                        for commits in (
                            [],
                            ["uninteresting"],
                            lazy_fixture(emoji_patch_commits.__name__),
                            lazy_fixture(emoji_minor_commits.__name__),
                        )
                    ),
                    (lazy_fixture(emoji_major_commits.__name__), False, False, "0.1.0"),
                    (lazy_fixture(emoji_major_commits.__name__), False, True, "1.0.0"),
                ],
                # Latest version for repo_with_single_branch is currently 0.1.1
                # Note repo_with_single_branch isn't modelled with prereleases
                (
                    "repo_with_single_branch_emoji_commits",
                    "default_emoji_parser",
                    VersionTranslator(),
                ): [
                    *(
                        (commits, False, major_on_zero, "0.1.1")
                        for major_on_zero in (True, False)
                        for commits in ([], ["uninteresting"])
                    ),
                    *(
                        (lazy_fixture(emoji_patch_commits.__name__), False, major_on_zero, "0.1.2")
                        for major_on_zero in (True, False)
                    ),
                    *(
                        (lazy_fixture(emoji_minor_commits.__name__), False, major_on_zero, "0.2.0")
                        for major_on_zero in (True, False)
                    ),
                    (lazy_fixture(emoji_major_commits.__name__), False, False, "0.2.0"),
                    (lazy_fixture(emoji_major_commits.__name__), False, True, "1.0.0"),
                ],
                # Latest version for repo_with_single_branch_and_prereleases is
                # currently 0.2.0
                (
                    "repo_with_single_branch_and_prereleases_emoji_commits",
                    "default_emoji_parser",
                    VersionTranslator(),
                ): [
                    *(
                        (commits, prerelease, major_on_zero, "0.2.0")
                        for prerelease in (True, False)
                        for major_on_zero in (True, False)
                        for commits in ([], ["uninteresting"])
                    ),
                    *(
                        (lazy_fixture(emoji_patch_commits.__name__), False, major_on_zero, "0.2.1")
                        for major_on_zero in (True, False)
                    ),
                    *(
                        (lazy_fixture(emoji_patch_commits.__name__), True, major_on_zero, "0.2.1-rc.1")
                        for major_on_zero in (True, False)
                    ),
                    *(
                        (lazy_fixture(emoji_minor_commits.__name__), False, major_on_zero, "0.3.0")
                        for major_on_zero in (True, False)
                    ),
                    *(
                        (lazy_fixture(emoji_minor_commits.__name__), True, major_on_zero, "0.3.0-rc.1")
                        for major_on_zero in (True, False)
                    ),
                    (lazy_fixture(emoji_major_commits.__name__), False, True, "1.0.0"),
                    (lazy_fixture(emoji_major_commits.__name__), True, True, "1.0.0-rc.1"),
                    (lazy_fixture(emoji_major_commits.__name__), False, False, "0.3.0"),
                    (lazy_fixture(emoji_major_commits.__name__), True, False, "0.3.0-rc.1"),
                ],
                # Latest version for repo_with_main_and_feature_branches is currently
                # 0.3.0-beta.1.
                # The last full release version was 0.2.0, so it's had a minor
                # prerelease
                (
                    "repo_w_github_flow_w_feature_release_channel_emoji_commits",
                    "default_emoji_parser",
                    VersionTranslator(prerelease_token="beta"),
                ): [
                    *(
                        (commits, True, major_on_zero, "0.3.0-beta.1")
                        for major_on_zero in (True, False)
                        for commits in ([], ["uninteresting"])
                    ),
                    # Models a merge of commits from the branch to the main branch, now
                    # that prerelease=False
                    *(
                        (commits, False, major_on_zero, "0.3.0")
                        for major_on_zero in (True, False)
                        for commits in ([], ["uninteresting"])
                    ),
                    *(
                        (lazy_fixture(emoji_patch_commits.__name__), False, major_on_zero, "0.3.0")
                        for major_on_zero in (True, False)
                    ),
                    *(
                        (lazy_fixture(emoji_patch_commits.__name__), True, major_on_zero, "0.3.0-beta.2")
                        for major_on_zero in (True, False)
                    ),
                    *(
                        (lazy_fixture(emoji_minor_commits.__name__), False, major_on_zero, "0.3.0")
                        for major_on_zero in (True, False)
                    ),
                    *(
                        (lazy_fixture(emoji_minor_commits.__name__), True, major_on_zero, "0.3.0-beta.2")
                        for major_on_zero in (True, False)
                    ),
                    (lazy_fixture(emoji_major_commits.__name__), False, True, "1.0.0"),
                    (lazy_fixture(emoji_major_commits.__name__), True, True, "1.0.0-beta.1"),
                    (lazy_fixture(emoji_major_commits.__name__), False, False, "0.3.0"),
                    # Note - since breaking changes are absorbed into the minor digit
                    # with major_on_zero = False, and that's already been incremented
                    # since the last full release, the breaking change here will only
                    # trigger a prerelease revision
                    (lazy_fixture(emoji_major_commits.__name__), True, False, "0.3.0-beta.2"),
                ],
            }.items()
            for (
                commit_messages,
                prerelease,
                major_on_zero,
                expected_new_version,
            ) in values
        ]
    ),
)
def test_algorithm_with_zero_dot_versions_emoji(
    repo,
    file_in_repo,
    commit_parser,
    translator,
    commit_messages,
    prerelease,
    expected_new_version,
    major_on_zero,
    allow_zero_version,
):
    # Setup
    for commit_message in commit_messages or []:
        add_text_to_file(repo, file_in_repo)
        repo.git.commit(m=commit_message)

    # Action
    new_version = next_version(
        repo, translator, commit_parser, prerelease, major_on_zero, allow_zero_version
    )

    # Verify
    assert expected_new_version == str(new_version)


@pytest.mark.parametrize(
    "repo, commit_parser, translator, commit_messages,"
    "prerelease, major_on_zero, expected_new_version",
    xdist_sort_hack(
        [
            (
                lazy_fixture(repo_fixture_name),
                lazy_fixture(parser_fixture_name),
                translator,
                commit_messages,
                prerelease,
                major_on_zero,
                expected_new_version,
            )
            for (repo_fixture_name, parser_fixture_name, translator), values in {
                # Latest version for repo_with_no_tags is currently 0.0.0 (default)
                # It's biggest change type is minor, so the next version should be 0.1.0
                (
                    "repo_with_no_tags_scipy_commits",
                    "default_scipy_parser",
                    VersionTranslator(),
                ): [
                    *(
                        (commits, False, major_on_zero, "0.1.0")
                        for major_on_zero in (True, False)
                        for commits in (
                            [],
                            ["uninteresting"],
                            lazy_fixture(scipy_patch_commits.__name__),
                            lazy_fixture(scipy_minor_commits.__name__),
                        )
                    ),
                    (lazy_fixture(scipy_major_commits.__name__), False, False, "0.1.0"),
                    (lazy_fixture(scipy_major_commits.__name__), False, True, "1.0.0"),
                ],
                # Latest version for repo_with_single_branch is currently 0.1.1
                # Note repo_with_single_branch isn't modelled with prereleases
                (
                    "repo_with_single_branch_scipy_commits",
                    "default_scipy_parser",
                    VersionTranslator(),
                ): [
                    *(
                        (commits, False, major_on_zero, "0.1.1")
                        for major_on_zero in (True, False)
                        for commits in ([], ["uninteresting"])
                    ),
                    *(
                        (
                            lazy_fixture(scipy_patch_commits.__name__),
                            False,
                            major_on_zero,
                            "0.1.2",
                        )
                        for major_on_zero in (True, False)
                    ),
                    *(
                        (
                            lazy_fixture(scipy_minor_commits.__name__),
                            False,
                            major_on_zero,
                            "0.2.0",
                        )
                        for major_on_zero in (True, False)
                    ),
                    (lazy_fixture(scipy_major_commits.__name__), False, False, "0.2.0"),
                    (lazy_fixture(scipy_major_commits.__name__), False, True, "1.0.0"),
                ],
                # Latest version for repo_with_single_branch_and_prereleases is
                # currently 0.2.0
                (
                    "repo_with_single_branch_and_prereleases_scipy_commits",
                    "default_scipy_parser",
                    VersionTranslator(),
                ): [
                    *(
                        (commits, prerelease, major_on_zero, "0.2.0")
                        for prerelease in (True, False)
                        for major_on_zero in (True, False)
                        for commits in ([], ["uninteresting"])
                    ),
                    *(
                        (
                            lazy_fixture(scipy_patch_commits.__name__),
                            False,
                            major_on_zero,
                            "0.2.1",
                        )
                        for major_on_zero in (True, False)
                    ),
                    *(
                        (
                            lazy_fixture(scipy_patch_commits.__name__),
                            True,
                            major_on_zero,
                            "0.2.1-rc.1",
                        )
                        for major_on_zero in (True, False)
                    ),
                    *(
                        (
                            lazy_fixture(scipy_minor_commits.__name__),
                            False,
                            major_on_zero,
                            "0.3.0",
                        )
                        for major_on_zero in (True, False)
                    ),
                    *(
                        (
                            lazy_fixture(scipy_minor_commits.__name__),
                            True,
                            major_on_zero,
                            "0.3.0-rc.1",
                        )
                        for major_on_zero in (True, False)
                    ),
                    (lazy_fixture(scipy_major_commits.__name__), False, True, "1.0.0"),
                    (lazy_fixture(scipy_major_commits.__name__), True, True, "1.0.0-rc.1"),
                    (lazy_fixture(scipy_major_commits.__name__), False, False, "0.3.0"),
                    (lazy_fixture(scipy_major_commits.__name__), True, False, "0.3.0-rc.1"),
                ],
                # Latest version for repo_with_main_and_feature_branches is currently
                # 0.3.0-rc.1.
                # The last full release version was 0.2.0, so it's had a minor
                # prerelease
                (
                    "repo_w_github_flow_w_feature_release_channel_scipy_commits",
                    "default_scipy_parser",
                    VersionTranslator(prerelease_token="beta"),
                ): [
                    *(
                        (commits, True, major_on_zero, "0.3.0-beta.1")
                        for major_on_zero in (True, False)
                        for commits in ([], ["uninteresting"])
                    ),
                    # Models a merge of commits from the branch to the main branch, now
                    # that prerelease=False
                    *(
                        (commits, False, major_on_zero, "0.3.0")
                        for major_on_zero in (True, False)
                        for commits in ([], ["uninteresting"])
                    ),
                    *(
                        (
                            lazy_fixture(scipy_patch_commits.__name__),
                            False,
                            major_on_zero,
                            "0.3.0",
                        )
                        for major_on_zero in (True, False)
                    ),
                    *(
                        (
                            lazy_fixture(scipy_patch_commits.__name__),
                            True,
                            major_on_zero,
                            "0.3.0-beta.2",
                        )
                        for major_on_zero in (True, False)
                    ),
                    *(
                        (
                            lazy_fixture(scipy_minor_commits.__name__),
                            False,
                            major_on_zero,
                            "0.3.0",
                        )
                        for major_on_zero in (True, False)
                    ),
                    *(
                        (
                            lazy_fixture(scipy_minor_commits.__name__),
                            True,
                            major_on_zero,
                            "0.3.0-beta.2",
                        )
                        for major_on_zero in (True, False)
                    ),
                    (lazy_fixture(scipy_major_commits.__name__), False, True, "1.0.0"),
                    (lazy_fixture(scipy_major_commits.__name__), True, True, "1.0.0-beta.1"),
                    (lazy_fixture(scipy_major_commits.__name__), False, False, "0.3.0"),
                    # Note - since breaking changes are absorbed into the minor digit
                    # with major_on_zero = False, and that's already been incremented
                    # since the last full release, the breaking change here will only
                    # trigger a prerelease revision
                    (lazy_fixture(scipy_major_commits.__name__), True, False, "0.3.0-beta.2"),
                ],
            }.items()
            for (
                commit_messages,
                prerelease,
                major_on_zero,
                expected_new_version,
            ) in values
        ],
    ),
)
def test_algorithm_with_zero_dot_versions_scipy(
    repo,
    file_in_repo,
    commit_parser,
    translator,
    commit_messages,
    prerelease,
    expected_new_version,
    major_on_zero,
    allow_zero_version,
):
    # Setup
    for commit_message in commit_messages or []:
        add_text_to_file(repo, file_in_repo)
        repo.git.commit(m=commit_message)

    # Action
    new_version = next_version(
        repo, translator, commit_parser, prerelease, major_on_zero, allow_zero_version
    )

    # Verify
    assert expected_new_version == str(new_version)


@pytest.mark.parametrize(
    "repo, commit_parser, translator, commit_messages,"
    "prerelease, major_on_zero, expected_new_version",
    xdist_sort_hack(
        [
            (
                lazy_fixture(repo_fixture_name),
                lazy_fixture(parser_fixture_name),
                translator,
                commit_messages,
                prerelease,
                major_on_zero,
                expected_new_version,
            )
            for (repo_fixture_name, parser_fixture_name, translator), values in {
                # Latest version for repo_with_no_tags is currently 0.0.0 (default)
                # It's biggest change type is minor, so the next version should be 0.1.0
                (
                    "repo_with_no_tags_tag_commits",
                    "default_tag_parser",
                    VersionTranslator(),
                ): [
                    *(
                        (commits, False, major_on_zero, "0.1.0")
                        for major_on_zero in (True, False)
                        for commits in (
                            [],
                            ["uninteresting"],
                            TAG_COMMITS_PATCH,
                            TAG_COMMITS_MINOR,
                        )
                    ),
                    (TAG_COMMITS_MAJOR, False, False, "0.1.0"),
                    (TAG_COMMITS_MAJOR, False, True, "1.0.0"),
                ],
                # Latest version for repo_with_single_branch is currently 0.1.1
                # Note repo_with_single_branch isn't modelled with prereleases
                (
                    "repo_with_single_branch_tag_commits",
                    "default_tag_parser",
                    VersionTranslator(),
                ): [
                    *(
                        (commits, False, major_on_zero, "0.1.1")
                        for major_on_zero in (True, False)
                        for commits in ([], ["uninteresting"])
                    ),
                    *(
                        (TAG_COMMITS_PATCH, False, major_on_zero, "0.1.2")
                        for major_on_zero in (True, False)
                    ),
                    *(
                        (TAG_COMMITS_MINOR, False, major_on_zero, "0.2.0")
                        for major_on_zero in (True, False)
                    ),
                    (TAG_COMMITS_MAJOR, False, False, "0.2.0"),
                    (TAG_COMMITS_MAJOR, False, True, "1.0.0"),
                ],
                # Latest version for repo_with_single_branch_and_prereleases is
                # currently 0.2.0
                (
                    "repo_with_single_branch_and_prereleases_tag_commits",
                    "default_tag_parser",
                    VersionTranslator(),
                ): [
                    *(
                        (commits, prerelease, major_on_zero, "0.2.0")
                        for prerelease in (True, False)
                        for major_on_zero in (True, False)
                        for commits in ([], ["uninteresting"])
                    ),
                    *(
                        (TAG_COMMITS_PATCH, False, major_on_zero, "0.2.1")
                        for major_on_zero in (True, False)
                    ),
                    *(
                        (TAG_COMMITS_PATCH, True, major_on_zero, "0.2.1-rc.1")
                        for major_on_zero in (True, False)
                    ),
                    *(
                        (TAG_COMMITS_MINOR, False, major_on_zero, "0.3.0")
                        for major_on_zero in (True, False)
                    ),
                    *(
                        (TAG_COMMITS_MINOR, True, major_on_zero, "0.3.0-rc.1")
                        for major_on_zero in (True, False)
                    ),
                    (TAG_COMMITS_MAJOR, False, True, "1.0.0"),
                    (TAG_COMMITS_MAJOR, True, True, "1.0.0-rc.1"),
                    (TAG_COMMITS_MAJOR, False, False, "0.3.0"),
                    (TAG_COMMITS_MAJOR, True, False, "0.3.0-rc.1"),
                ],
                # Latest version for repo_with_main_and_feature_branches is currently
                # 0.3.0-beta.1.
                # The last full release version was 0.2.0, so it's had a minor
                # prerelease
                (
                    "repo_w_github_flow_w_feature_release_channel_tag_commits",
                    "default_tag_parser",
                    VersionTranslator(prerelease_token="beta"),
                ): [
                    *(
                        (commits, True, major_on_zero, "0.3.0-beta.1")
                        for major_on_zero in (True, False)
                        for commits in ([], ["uninteresting"])
                    ),
                    # Models a merge of commits from the branch to the main branch, now
                    # that prerelease=False
                    *(
                        (commits, False, major_on_zero, "0.3.0")
                        for major_on_zero in (True, False)

@pytest.mark.parametrize(
    str.join(" ,", [
        "repo",
        "commit_parser",
        "translator",
        "commit_messages",
        "prerelease",
        "major_on_zero",
        "allow_zero_version",
        "expected_new_version",
    ]),
    xdist_sort_hack(
        [
            (
                lazy_fixture(repo_with_no_tags_tag_commits.__name__),
                lazy_fixture(parser_fixture_name),
                translator[0],
                commit_messages,
                prerelease,
                major_on_zero,
                allow_zero_version,
                expected_new_version,
            )
            for translator, values in {
                # Latest version for repo_with_no_tags is currently 0.0.0 (default)
                # It's biggest change type is minor, so the next version should be 0.1.0
                (VersionTranslator(),): [
                    *(
                        # when prerelease is False, major_on_zero is True & False, & allow_zero_version is True
                        # the version should be 0.0.0, when no distintive changes have been made since the
                        # start of the project
                        (commits, parser, prerelease, major_on_zero, True, "0.0.0")
                        for prerelease in (True, False)
                        for major_on_zero in (True, False)
                        for commits, parser in (
                            # No commits added, so base is just initial commit at 0.0.0
                            (None, default_tag_parser.__name__),
                            # Chore like commits also don't trigger a version bump so it stays 0.0.0
                            (
                                lazy_fixture(angular_chore_commits.__name__),
                                default_angular_parser.__name__,
                            ),
                            (
                                lazy_fixture(emoji_chore_commits.__name__),
                                default_emoji_parser.__name__,
                            ),
                            (
                                lazy_fixture(scipy_chore_commits.__name__),
                                default_scipy_parser.__name__,
                            ),
                            (
                                lazy_fixture(tag_chore_commits.__name__),
                                default_tag_parser.__name__,
                            ),
                        )
                    ),
                    *(
                        (commits, parser, True, major_on_zero, True, "0.0.1-rc.1")
                        for major_on_zero in (True, False)
                        for commits, parser in (
                            # when prerelease is True & allow_zero_version is True, the version should be
                            # a patch bump as a prerelease version, because of the patch level commits
                            # major_on_zero is irrelevant here as we are only applying patch commits
                            (
                                lazy_fixture(angular_patch_commits.__name__),
                                default_angular_parser.__name__,
                            ),
                            (
                                lazy_fixture(emoji_patch_commits.__name__),
                                default_emoji_parser.__name__,
                            ),
                            (
                                lazy_fixture(scipy_patch_commits.__name__),
                                default_scipy_parser.__name__,
                            ),
                            (
                                lazy_fixture(tag_patch_commits.__name__),
                                default_tag_parser.__name__,
                            ),
                        )
                    ),
                    *(
                        (commits, parser, False, major_on_zero, True, "0.0.1")
                        for major_on_zero in (True, False)
                        for commits, parser in (
                            # when prerelease is False, & allow_zero_version is True, the version should be
                            # a patch bump because of the patch commits added
                            # major_on_zero is irrelevant here as we are only applying patch commits
                            (
                                lazy_fixture(angular_patch_commits.__name__),
                                default_angular_parser.__name__,
                            ),
                            (
                                lazy_fixture(emoji_patch_commits.__name__),
                                default_emoji_parser.__name__,
                            ),
                            (
                                lazy_fixture(scipy_patch_commits.__name__),
                                default_scipy_parser.__name__,
                            ),
                            (
                                lazy_fixture(tag_patch_commits.__name__),
                                default_tag_parser.__name__,
                            ),
                        )
                    ),
                    *(
                        (commits, parser, True, False, True, "0.1.0-rc.1")
                        for commits, parser in (
                            # when prerelease is False, & major_on_zero is False, the version should be
                            # a minor bump because of the minor commits added
                            (
                                lazy_fixture(angular_minor_commits.__name__),
                                default_angular_parser.__name__,
                            ),
                            (
                                lazy_fixture(emoji_minor_commits.__name__),
                                default_emoji_parser.__name__,
                            ),
                            (
                                lazy_fixture(scipy_minor_commits.__name__),
                                default_scipy_parser.__name__,
                            ),
                            (
                                lazy_fixture(tag_minor_commits.__name__),
                                default_tag_parser.__name__,
                            ),
                            # Given the major_on_zero is False and the version is starting at 0.0.0,
                            # the major level commits are limited to only causing a minor level bump
                            (
                                lazy_fixture(angular_major_commits.__name__),
                                default_angular_parser.__name__,
                            ),
                            (
                                lazy_fixture(emoji_major_commits.__name__),
                                default_emoji_parser.__name__,
                            ),
                            (
                                lazy_fixture(scipy_major_commits.__name__),
                                default_scipy_parser.__name__,
                            ),
                            (
                                lazy_fixture(tag_major_commits.__name__),
                                default_tag_parser.__name__,
                            ),
                        )
                    ),
                    *(
                        (commits, parser, False, False, True, "0.1.0")
                        for commits, parser in (
                            # when prerelease is False,
                            # major_on_zero is False, & allow_zero_version is True
                            # the version should be a minor bump of 0.0.0
                            # because of the minor commits added and zero version is allowed
                            (
                                lazy_fixture(angular_minor_commits.__name__),
                                default_angular_parser.__name__,
                            ),
                            (
                                lazy_fixture(emoji_minor_commits.__name__),
                                default_emoji_parser.__name__,
                            ),
                            (
                                lazy_fixture(scipy_minor_commits.__name__),
                                default_scipy_parser.__name__,
                            ),
                            (
                                lazy_fixture(tag_minor_commits.__name__),
                                default_tag_parser.__name__,
                            ),
                            # Given the major_on_zero is False and the version is starting at 0.0.0,
                            # the major level commits are limited to only causing a minor level bump
                            (
                                lazy_fixture(angular_major_commits.__name__),
                                default_angular_parser.__name__,
                            ),
                            (
                                lazy_fixture(emoji_major_commits.__name__),
                                default_emoji_parser.__name__,
                            ),
                            (
                                lazy_fixture(scipy_major_commits.__name__),
                                default_scipy_parser.__name__,
                            ),
                            (
                                lazy_fixture(tag_major_commits.__name__),
                                default_tag_parser.__name__,
                            ),
                        )
                    ),
                    *(
                        # when prerelease is True, & allow_zero_version is False, the version should be
                        # a prerelease version 1.0.0-rc.1, across the board when any valuable change
                        # is made because of the allow_zero_version is False, major_on_zero is ignored
                        # when allow_zero_version is False (but we still test it)
                        (commits, parser, True, major_on_zero, False, "1.0.0-rc.1")
                        for major_on_zero in (True, False)
                        for commits, parser in (
                            # parser doesn't matter here as long as it detects a NO_RELEASE on Initial Commit
                            (None, default_tag_parser.__name__),
                            (
                                lazy_fixture(angular_chore_commits.__name__),
                                default_angular_parser.__name__,
                            ),
                            (
                                lazy_fixture(angular_patch_commits.__name__),
                                default_angular_parser.__name__,
                            ),
                            (
                                lazy_fixture(angular_minor_commits.__name__),
                                default_angular_parser.__name__,
                            ),
                            (
                                lazy_fixture(angular_major_commits.__name__),
                                default_angular_parser.__name__,
                            ),
                            (
                                lazy_fixture(emoji_chore_commits.__name__),
                                default_emoji_parser.__name__,
                            ),
                            (
                                lazy_fixture(emoji_patch_commits.__name__),
                                default_emoji_parser.__name__,
                            ),
                            (
                                lazy_fixture(emoji_minor_commits.__name__),
                                default_emoji_parser.__name__,
                            ),
                            (
                                lazy_fixture(emoji_major_commits.__name__),
                                default_emoji_parser.__name__,
                            ),
                            (
                                lazy_fixture(scipy_chore_commits.__name__),
                                default_scipy_parser.__name__,
                            ),
                            (
                                lazy_fixture(scipy_patch_commits.__name__),
                                default_scipy_parser.__name__,
                            ),
                            (
                                lazy_fixture(scipy_minor_commits.__name__),
                                default_scipy_parser.__name__,
                            ),
                            (
                                lazy_fixture(scipy_major_commits.__name__),
                                default_scipy_parser.__name__,
                            ),
                            (
                                lazy_fixture(tag_chore_commits.__name__),
                                default_tag_parser.__name__,
                            ),
                            (
                                lazy_fixture(tag_patch_commits.__name__),
                                default_tag_parser.__name__,
                            ),
                            (
                                lazy_fixture(tag_minor_commits.__name__),
                                default_tag_parser.__name__,
                            ),
                            (
                                lazy_fixture(tag_major_commits.__name__),
                                default_tag_parser.__name__,
                            ),
                        )
                    ),
                    *(
                        # when prerelease is True, & allow_zero_version is False, the version should be
                        # 1.0.0, across the board when any valuable change
                        # is made because of the allow_zero_version is False. major_on_zero is ignored
                        # when allow_zero_version is False (but we still test it)
                        (commits, parser, False, major_on_zero, False, "1.0.0")
                        for major_on_zero in (True, False)
                        for commits, parser in (
                            (None, default_tag_parser.__name__),
                            (
                                lazy_fixture(angular_chore_commits.__name__),
                                default_angular_parser.__name__,
                            ),
                            (
                                lazy_fixture(angular_patch_commits.__name__),
                                default_angular_parser.__name__,
                            ),
                            (
                                lazy_fixture(angular_minor_commits.__name__),
                                default_angular_parser.__name__,
                            ),
                            (
                                lazy_fixture(angular_major_commits.__name__),
                                default_angular_parser.__name__,
                            ),
                            (
                                lazy_fixture(emoji_chore_commits.__name__),
                                default_emoji_parser.__name__,
                            ),
                            (
                                lazy_fixture(emoji_patch_commits.__name__),
                                default_emoji_parser.__name__,
                            ),
                            (
                                lazy_fixture(emoji_minor_commits.__name__),
                                default_emoji_parser.__name__,
                            ),
                            (
                                lazy_fixture(emoji_major_commits.__name__),
                                default_emoji_parser.__name__,
                            ),
                            (
                                lazy_fixture(scipy_chore_commits.__name__),
                                default_scipy_parser.__name__,
                            ),
                            (
                                lazy_fixture(scipy_patch_commits.__name__),
                                default_scipy_parser.__name__,
                            ),
                            (
                                lazy_fixture(scipy_minor_commits.__name__),
                                default_scipy_parser.__name__,
                            ),
                            (
                                lazy_fixture(scipy_major_commits.__name__),
                                default_scipy_parser.__name__,
                            ),
                            (
                                lazy_fixture(tag_chore_commits.__name__),
                                default_tag_parser.__name__,
                            ),
                            (
                                lazy_fixture(tag_patch_commits.__name__),
                                default_tag_parser.__name__,
                            ),
                            (
                                lazy_fixture(tag_minor_commits.__name__),
                                default_tag_parser.__name__,
                            ),
                            (
                                lazy_fixture(tag_major_commits.__name__),
                                default_tag_parser.__name__,
                            ),
                        )
                    ),
                ],
            }.items()
            for (
                commit_messages,
                parser_fixture_name,
                prerelease,
                major_on_zero,
                allow_zero_version,
                expected_new_version,
            ) in values
        ],
    ),
)
def test_algorithm_with_zero_dot_versions_minimums(
    repo: Repo,
    file_in_repo,
    commit_parser,
    translator,
    commit_messages,
    prerelease,
    expected_new_version,
    major_on_zero,
    allow_zero_version,
):
    # Setup
    # Move tree down to the Initial Commit
    initial_commit = repo.git.log("--max-parents=0", "--format=%H").strip()
    repo.git.reset("--hard", initial_commit)

    for commit_message in commit_messages or []:
        add_text_to_file(repo, file_in_repo)
        repo.git.commit(m=commit_message)

    # Action
    new_version = next_version(
        repo, translator, commit_parser, prerelease, major_on_zero, allow_zero_version
    )

    # Verify
    assert expected_new_version == str(new_version)
