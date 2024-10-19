.. _changelog:

=========
CHANGELOG
=========

.. _changelog-v9.12.0:

v9.12.0 (2024-10-18)
====================

✨ Features
-----------

* **changelog**: Add ``autofit_text_width`` filter to template environment (`#1062`_, `83e4b86`_)

🪲 Bug Fixes
------------

* **changelog**: Ignore commit exclusion when a commit causes a version bump (`e8f886e`_)

* **parser-angular**: Change ``Fixes`` commit type heading to ``Bug Fixes`` (`#1064`_, `09e3a4d`_)

* **parser-emoji**: Enable the default bump level option (`bc27995`_)

📖 Documentation
----------------

* **changelog-templates**: Add definition & usage of ``autofit_text_width`` template filter
  (`#1062`_, `83e4b86`_)

* **commit-parsers**: Add deprecation message for the tag parser (`af94540`_)

* **configuration**: Add deprecation message for the tag parser (`a83b7e4`_)

.. _#1062: https://github.com/python-semantic-release/python-semantic-release/pull/1062
.. _#1064: https://github.com/python-semantic-release/python-semantic-release/pull/1064
.. _09e3a4d: https://github.com/python-semantic-release/python-semantic-release/commit/09e3a4da6237740de8e9932d742b18d990e9d079
.. _83e4b86: https://github.com/python-semantic-release/python-semantic-release/commit/83e4b86abd4754c2f95ec2e674f04deb74b9a1e6
.. _a83b7e4: https://github.com/python-semantic-release/python-semantic-release/commit/a83b7e43e4eaa99790969a6c85f44e01cde80d0a
.. _af94540: https://github.com/python-semantic-release/python-semantic-release/commit/af94540f2b1c63bf8a4dc977d5d0f66176962b64
.. _bc27995: https://github.com/python-semantic-release/python-semantic-release/commit/bc27995255a96b9d6cc743186e7c35098822a7f6
.. _e8f886e: https://github.com/python-semantic-release/python-semantic-release/commit/e8f886ef2abe8ceaea0a24a0112b92a167abd6a9


.. _changelog-v9.11.1:

v9.11.1 (2024-10-15)
====================

🪲 Bug Fixes
------------

* **changelog**: Prevent custom template errors when components are in hidden folders (`#1060`_,
  `a7614b0`_)

.. _#1060: https://github.com/python-semantic-release/python-semantic-release/pull/1060
.. _a7614b0: https://github.com/python-semantic-release/python-semantic-release/commit/a7614b0db8ce791e4252209e66f42b5b5275dffd


.. _changelog-v9.11.0:

v9.11.0 (2024-10-12)
====================

✨ Features
-----------

* **changelog**: Add ``convert_md_to_rst`` filter to changelog environment (`#1055`_, `c2e8831`_)

* **changelog**: Add default changelog in re-structured text format, resolves `#399`_ (`#1055`_,
  `c2e8831`_)

* **changelog**: Add default changelog template in reStructuredText format (`#1055`_, `c2e8831`_)

* **config**: Enable default ``changelog.insertion_flag`` based on output format (`#1055`_,
  `c2e8831`_)

* **config**: Enable target changelog filename to trigger RST output format, resolves `#399`_
  (`#1055`_, `c2e8831`_)

🪲 Bug Fixes
------------

* **changelog**: Correct spacing for default markdown template during updates (`#1055`_,
  `c2e8831`_)

📖 Documentation
----------------

* **changelog**: Clarify the ``convert_md_to_rst`` filter added to the template environment
  (`#1055`_, `c2e8831`_)

* **changelog**: Increase detail about configuration options of default changelog creation
  (`#1055`_, `c2e8831`_)

* **configuration**: Update ``changelog_file`` with deprecation notice of setting relocation
  (`#1055`_, `c2e8831`_)

* **configuration**: Update ``output_format`` description for reStructuredText support (`#1055`_,
  `c2e8831`_)

* **configuration**: Update details of ``insertion_flag``'s dynamic defaults with rst (`#1055`_,
  `c2e8831`_)

.. _#1055: https://github.com/python-semantic-release/python-semantic-release/pull/1055
.. _c2e8831: https://github.com/python-semantic-release/python-semantic-release/commit/c2e883104d3c11e56f229638e988d8b571f86e34


.. _changelog-v9.10.1:

v9.10.1 (2024-10-10)
====================

🪲 Bug Fixes
------------

* **config**: Handle branch match regex errors gracefully (`#1054`_, `4d12251`_)

.. _#1054: https://github.com/python-semantic-release/python-semantic-release/pull/1054
.. _4d12251: https://github.com/python-semantic-release/python-semantic-release/commit/4d12251c678a38de6b71cac5b9c1390eb9dd8ad6


.. _changelog-v9.10.0:

v9.10.0 (2024-10-08)
====================

✨ Features
-----------

* **changelog**: Add ``changelog_insertion_flag`` to changelog template context (`#1045`_,
  `c18c245`_)

* **changelog**: Add ``changelog_mode`` to changelog template context (`#1045`_, `c18c245`_)

* **changelog**: Add ``prev_changelog_file`` to changelog template context (`#1045`_, `c18c245`_)

* **changelog**: Add ``read_file`` function to changelog template context (`#1045`_, `c18c245`_)

* **changelog**: Add shorthand ``ctx`` variable to changelog template env (`#1045`_, `c18c245`_)

* **changelog**: Modify changelog template to support changelog updates, resolves `#858`_
  (`#1045`_, `c18c245`_)

* **config**: Add ``changelog.default_templates.output_format`` config option (`#1045`_,
  `c18c245`_)

* **config**: Add ``changelog.insertion_flag`` as configuration option (`#1045`_, `c18c245`_)

* **config**: Add ``changelog.mode`` as configuration option (`#1045`_, `c18c245`_)

* **github-actions**: Add an action ``build`` directive to toggle the ``--skip-build`` option
  (`#1044`_, `26597e2`_)

🪲 Bug Fixes
------------

* **changelog**: Adjust angular heading names for readability (`#1045`_, `c18c245`_)

* **changelog**: Ensure changelog templates can handle complex directory includes (`#1045`_,
  `c18c245`_)

* **changelog**: Only render user templates when files exist (`#1045`_, `c18c245`_)

* **config**: Prevent jinja from autoescaping markdown content by default (`#1045`_, `c18c245`_)

📖 Documentation
----------------

* **changelog-templates**: Improve detail & describe new ``changelog.mode="update"`` (`#1045`_,
  `c18c245`_)

* **commands**: Update definition of the version commands ``--skip-build`` option (`#1044`_,
  `26597e2`_)

* **configuration**: Add ``changelog.mode`` and ``changelog.insertion_flag`` config definitions
  (`#1045`_, `c18c245`_)

* **configuration**: Define the new ``changelog.default_templates.output_format`` option (`#1045`_,
  `c18c245`_)

* **configuration**: Mark version of configuration setting introduction (`#1045`_, `c18c245`_)

* **configuration**: Standardize all true/false to lowercase ensuring toml-compatibility (`#1045`_,
  `c18c245`_)

* **configuration**: Update ``changelog.environment.autoescape`` default to ``false`` to match code
  (`#1045`_, `c18c245`_)

* **github-actions**: Add description of the ``build`` input directive (`#1044`_, `26597e2`_)

* **github-actions**: Update primary example with workflow sha controlled pipeline (`14f04df`_)

* **homepage**: Update custom changelog reference (`#1045`_, `c18c245`_)

.. _#1044: https://github.com/python-semantic-release/python-semantic-release/pull/1044
.. _#1045: https://github.com/python-semantic-release/python-semantic-release/pull/1045
.. _14f04df: https://github.com/python-semantic-release/python-semantic-release/commit/14f04dffc7366142faecebb162d4449501cbf1fd
.. _26597e2: https://github.com/python-semantic-release/python-semantic-release/commit/26597e24a80a37500264aa95a908ba366699099e
.. _c18c245: https://github.com/python-semantic-release/python-semantic-release/commit/c18c245df51a9778af09b9dc7a315e3f11cdcda0


.. _changelog-v9.9.0:

v9.9.0 (2024-09-28)
===================

✨ Features
-----------

* **github-actions**: Add ``is_prerelease`` output to the version action (`#1038`_, `6a5d35d`_)

* docs(github-actions): add description of new ``is_prerelease`` output for version action

📖 Documentation
----------------

* **github-actions**: Clarify & consolidate GitHub Actions usage docs (`#1011`_, `2135c68`_)

Resolves: #907

* docs(automatic-releases): drop extrenous github push configuration

* docs(homepage): remove link to old github config & update token scope config

* docs(github-actions): expand descriptions & clarity of actions configs

* docs(github-actions): add configuration & description of publish action

* docs(github-actions): revert removal of namespace prefix from examples

.. _#1011: https://github.com/python-semantic-release/python-semantic-release/pull/1011
.. _#1038: https://github.com/python-semantic-release/python-semantic-release/pull/1038
.. _2135c68: https://github.com/python-semantic-release/python-semantic-release/commit/2135c68ccbdad94378809902b52fcad546efd5b3
.. _6a5d35d: https://github.com/python-semantic-release/python-semantic-release/commit/6a5d35d0d9124d6a6ee7910711b4154b006b8773


.. _changelog-v9.8.9:

v9.8.9 (2024-09-27)
===================

🪲 Bug Fixes
------------

* **version-cmd**: Improve ``version_variables`` flexibility w/ quotes (ie. json, yaml, etc)
  (`#1028`_, `156915c`_)

* fix(version-cmd): increase ``version_variable`` flexibility with quotations (ie. json, yaml, etc)

Previously json would not work due to the key being wrapped in quotes, yaml also has issues when it
  does not usually use quotes. The regex we created originally only wrapped the version to be
  replaced in quotes but now both the key and version can optionally be wrapped in different kind of
  quotations.

Resolves: #601, #706, #962, #1026

* docs(configuration): add clarity to ``version_variables`` usage & limitations

Ref: #941

* fix(version-cmd): ensure ``version_variables`` do not match partial variable names

* build(deps-test): add ``PyYAML`` as a test dependency

📖 Documentation
----------------

* Update docstrings to resolve sphinx failures (`#1030`_, `d84efc7`_)

set ``ignore-module-all`` for ``autodoc_default_options`` to resolve some Sphinx errors about
  duplicate / ambiguous references
  https://github.com/sphinx-doc/sphinx/issues/4961#issuecomment-1543858623

Standardize some non-standard (Google-ish) docstrings to Sphinx format, to avoid ruff and Sphinx
  arguing about underline length.

Fix indents and other minor whitespace / formatting changes.

Fixes #1029

.. _#1028: https://github.com/python-semantic-release/python-semantic-release/pull/1028
.. _#1030: https://github.com/python-semantic-release/python-semantic-release/pull/1030
.. _156915c: https://github.com/python-semantic-release/python-semantic-release/commit/156915c7d759098f65cf9de7c4e980b40b38d5f1
.. _d84efc7: https://github.com/python-semantic-release/python-semantic-release/commit/d84efc7719a8679e6979d513d1c8c60904af7384


.. _changelog-v9.8.8:

v9.8.8 (2024-09-01)
===================

🪲 Bug Fixes
------------

* **config**: Fix path traversal detection for windows compatibility (`#1014`_, `16e6daa`_)

The original implementation of the path traversal detection expected that ``resolve()`` works the
  same on windows as it does with Linux/Mac. Windows requires the folder paths to exist to be
  resolved and that is not the case when the ``template_dir`` is not being used.

Resolves: #994

📖 Documentation
----------------

* **configuration**: Update ``build_command`` env table for windows to use all capital vars
  (`0e8451c`_)

* **github-actions**: Update version in examples to latest version (`3c894ea`_)

.. _#1014: https://github.com/python-semantic-release/python-semantic-release/pull/1014
.. _0e8451c: https://github.com/python-semantic-release/python-semantic-release/commit/0e8451cf9003c6a3bdcae6878039d7d9a23d6d5b
.. _16e6daa: https://github.com/python-semantic-release/python-semantic-release/commit/16e6daaf851ce1eabf5fbd5aa9fe310a8b0f22b3
.. _3c894ea: https://github.com/python-semantic-release/python-semantic-release/commit/3c894ea8a555d20b454ebf34785e772959bbb4fe


.. _changelog-v9.8.7:

v9.8.7 (2024-08-20)
===================

🪲 Bug Fixes
------------

* Provide ``context.history`` global in release notes templates (`#1005`_, `5bd91b4`_)

* fix(release-notes): provide ``context.history`` global in release note templates

Temporarily return the ``context.history`` variable to release notes generation as many users are
  using it in their release documentation. It was never intended to be provided and will be removed
  in the future.

context was removed in ``v9.8.3`` during a refactor and condensing of changelog and release notes
  functionality.

Resolves: #984

* fix(release-notes): fix noop-changelog to print raw release notes

Some markdown sequences can be interpreted as ansi escape sequences which dilute debugging of
  release note templates by the user. This change ensures the raw content is displayed to the
  console as expected.

📖 Documentation
----------------

* Use pinned version for GHA examples (`#1004`_, `5fdf761`_)

* docs(github-actions): use pinned version for GHA examples

Fixes #1003

* docs(github-actions): adjust formatting & version warning in code snippets

* **changelog**: Clarify description of the default changelog generation process (`399fa65`_)

* **configuration**: Clarify ``changelog_file`` vs ``template_dir`` option usage (`a7199c8`_)

Provided additional description that warns about the mutually-exclusive nature of the
  ``changelog_file`` option and the ``template_dir`` option.

Resolves: #983

* **configuration**: Fix build_command_env table rendering (`#996`_, `a5eff0b`_)

.. _#1004: https://github.com/python-semantic-release/python-semantic-release/pull/1004
.. _#1005: https://github.com/python-semantic-release/python-semantic-release/pull/1005
.. _#996: https://github.com/python-semantic-release/python-semantic-release/pull/996
.. _399fa65: https://github.com/python-semantic-release/python-semantic-release/commit/399fa6521d5c6c4397b1d6e9b13ea7945ae92543
.. _5bd91b4: https://github.com/python-semantic-release/python-semantic-release/commit/5bd91b4d7ac33ddf10446f3e66d7d11e0724aeb2
.. _5fdf761: https://github.com/python-semantic-release/python-semantic-release/commit/5fdf7614c036a77ffb051cd30f57d0a63c062c0d
.. _a5eff0b: https://github.com/python-semantic-release/python-semantic-release/commit/a5eff0bfe41d2fd5d9ead152a132010b718b7772
.. _a7199c8: https://github.com/python-semantic-release/python-semantic-release/commit/a7199c8cd6041a9de017694302e49b139bbcb034


.. _changelog-v9.8.6:

v9.8.6 (2024-07-20)
===================

🪲 Bug Fixes
------------

* **version-cmd**: Resolve build command execution in powershell (`#980`_, `32c8e70`_)

Fixes the command line option for passing a shell command to Powershell. Also included a similar
  shell detection result for pwsh (Powershell Core)

📖 Documentation
----------------

* **configuration**: Correct GHA parameter name for commit email (`#981`_, `ce9ffdb`_)

``git_committer_name`` was repeated; replace one instance of it with ``git_committer_email``

.. _#980: https://github.com/python-semantic-release/python-semantic-release/pull/980
.. _#981: https://github.com/python-semantic-release/python-semantic-release/pull/981
.. _32c8e70: https://github.com/python-semantic-release/python-semantic-release/commit/32c8e70915634d8e560b470c3cf38c27cebd7ae0
.. _ce9ffdb: https://github.com/python-semantic-release/python-semantic-release/commit/ce9ffdb82c2358184b288fa18e83a4075f333277


.. _changelog-v9.8.5:

v9.8.5 (2024-07-06)
===================

🪲 Bug Fixes
------------

* Enable ``--print-last-released*`` when in detached head or non-release branch (`#926`_,
  `782c0a6`_)

* fix(version-cmd): drop branch restriction for ``--print-last-released*`` opts

Resolves: #900

⚡ Performance Improvements
---------------------------

* Improve git history processing for changelog generation (`#972`_, `bfda159`_)

* perf(changelog): improve git history parser changelog generation

This converts the double for-loop (`O(n^2)`) down to ``O(n)`` using a lookup table to match the
  current commit with a known tag rather than iterating through all the tags of the repository every
  time.

* fix(changelog): resolve commit ordering issue when dates are similar

.. _#926: https://github.com/python-semantic-release/python-semantic-release/pull/926
.. _#972: https://github.com/python-semantic-release/python-semantic-release/pull/972
.. _782c0a6: https://github.com/python-semantic-release/python-semantic-release/commit/782c0a6109fb49e168c37f279928c0a4959f8ac6
.. _bfda159: https://github.com/python-semantic-release/python-semantic-release/commit/bfda1593af59e9e728c584dd88d7927fc52c879f


.. _changelog-v9.8.4:

v9.8.4 (2024-07-04)
===================

🪲 Bug Fixes
------------

* **changelog-cmd**: Remove usage strings when error occured (`348a51d`_)

    Resolves: #810

* **changelog-cmd**: Render default changelog when user template directory exist but is empty
  (`bded8de`_)

* **config**: Prevent path traversal manipulation of target changelog location (`43e35d0`_)

* **config**: Prevent path traversal manipulation of target changelog location (`3eb3dba`_)

* **publish-cmd**: Prevent error when provided tag does not exist locally (`16afbbb`_)

* **publish-cmd**: Remove usage strings when error occured (`afbb187`_)

    Resolves: #810

* **version-cmd**: Remove usage strings when error occurred (`a7c17c7`_)

    Resolves: #810

.. _16afbbb: https://github.com/python-semantic-release/python-semantic-release/commit/16afbbb8fbc3a97243e96d7573f4ad2eba09aab9
.. _348a51d: https://github.com/python-semantic-release/python-semantic-release/commit/348a51db8a837d951966aff3789aa0c93d473829
.. _3eb3dba: https://github.com/python-semantic-release/python-semantic-release/commit/3eb3dbafec4223ee463b90e927e551639c69426b
.. _43e35d0: https://github.com/python-semantic-release/python-semantic-release/commit/43e35d0972e8a29239d18ed079d1e2013342fcbd
.. _a7c17c7: https://github.com/python-semantic-release/python-semantic-release/commit/a7c17c73fd7becb6d0e042e45ff6765605187e2a
.. _afbb187: https://github.com/python-semantic-release/python-semantic-release/commit/afbb187d6d405fdf6765082e2a1cecdcd7d357df
.. _bded8de: https://github.com/python-semantic-release/python-semantic-release/commit/bded8deae6c92f6dde9774802d9f3716a5cb5705


.. _changelog-v9.8.3:

v9.8.3 (2024-06-18)
===================

🪲 Bug Fixes
------------

* **parser**: Strip DOS carriage-returns in commits (`#956`_, `0b005df`_)

The default template can result in mixed (UNIX / DOS style) carriage returns in the generated
  changelog. Use a string replace in the commit parser to strip the DOS CRs ("\r"). This is only
  needed in the case when we are *not* byte decoding.

Fixes #955

.. _#956: https://github.com/python-semantic-release/python-semantic-release/pull/956
.. _0b005df: https://github.com/python-semantic-release/python-semantic-release/commit/0b005df0a8c7730ee0c71453c9992d7b5d2400a4


.. _changelog-v9.8.2:

v9.8.2 (2024-06-17)
===================

🪲 Bug Fixes
------------

* **templates**: Suppress extra newlines in default changelog (`#954`_, `7b0079b`_)

Suppress extra newlines in default generated changelog output

.. _#954: https://github.com/python-semantic-release/python-semantic-release/pull/954
.. _7b0079b: https://github.com/python-semantic-release/python-semantic-release/commit/7b0079bf3e17c0f476bff520b77a571aeac469d0


.. _changelog-v9.8.1:

v9.8.1 (2024-06-05)
===================

🪲 Bug Fixes
------------

* Improve build cmd env on windows (`#942`_, `d911fae`_)

* fix(version-cmd): pass windows specific env vars to build cmd when on windows

* docs(configuration): define windows specific env vars for build cmd

.. _#942: https://github.com/python-semantic-release/python-semantic-release/pull/942
.. _d911fae: https://github.com/python-semantic-release/python-semantic-release/commit/d911fae993d41a8cb1497fa8b2a7e823576e0f22


.. _changelog-v9.8.0:

v9.8.0 (2024-05-27)
===================

✨ Features
-----------

* Extend gitlab to edit a previous release if exists (`#934`_, `23e02b9`_)

* feat(hvcs-gitlab): enable gitlab to edit a previous release if found

* fix(hvcs-gitlab): add tag message to release creation

* fix(gitlab): adjust release name to mirror other hvcs release names

* **gha**: Configure ssh signed tags in GitHub Action (`#937`_, `dfb76b9`_)

    Resolves: #936

* **version-cmd**: Add toggle of ``--no-verify`` option to ``git commit`` (`#927`_, `1de6f78`_)

* feat(version-cmd): add toggle of ``--no-verify`` option to ``git commit``

This commit adds a configuration option that toggles the addition of ``--no-verify`` command line
  switch on git commit operations that are run with the ``version`` command.

* docs(configuration): add ``no_git_verify`` description to the configuration page

---------

Co-authored-by: bdorsey <brentadorsey@gmail.com>

📖 Documentation
----------------

* **migration-v8**: Update version references in migration instructions (`#938`_, `d6ba16a`_)

.. _#927: https://github.com/python-semantic-release/python-semantic-release/pull/927
.. _#934: https://github.com/python-semantic-release/python-semantic-release/pull/934
.. _#937: https://github.com/python-semantic-release/python-semantic-release/pull/937
.. _#938: https://github.com/python-semantic-release/python-semantic-release/pull/938
.. _1de6f78: https://github.com/python-semantic-release/python-semantic-release/commit/1de6f7834c6d37a74bc53f91609d40793556b52d
.. _23e02b9: https://github.com/python-semantic-release/python-semantic-release/commit/23e02b96dfb2a58f6b4ecf7b7812e4c1bc50573d
.. _d6ba16a: https://github.com/python-semantic-release/python-semantic-release/commit/d6ba16aa8e01bae1a022a9b06cd0b9162c51c345
.. _dfb76b9: https://github.com/python-semantic-release/python-semantic-release/commit/dfb76b94b859a7f3fa3ad778eec7a86de2874d68


.. _changelog-v9.7.3:

v9.7.3 (2024-05-15)
===================

🪲 Bug Fixes
------------

* Enabled ``prelease-token`` parameter in github action (`#929`_, `1bb26b0`_)

.. _#929: https://github.com/python-semantic-release/python-semantic-release/pull/929
.. _1bb26b0: https://github.com/python-semantic-release/python-semantic-release/commit/1bb26b0762d94efd97c06a3f1b6b10fb76901f6d


.. _changelog-v9.7.2:

v9.7.2 (2024-05-13)
===================

🪲 Bug Fixes
------------

* Enable user configuration of ``build_command`` env vars (`#925`_, `6b5b271`_)

- test(version): add test of user defined env variables in build command

ref: #922

- fix(version): enable user config of ``build_command`` env variables

Resolves: #922

- docs(configuration): document ``build_command_env`` configuration option

📖 Documentation
----------------

* **configuration**: Clarify TOC & alphabetize configuration descriptions (`19add16`_)

* **configuration**: Clarify TOC & standardize heading links (`3a41995`_)

.. _#925: https://github.com/python-semantic-release/python-semantic-release/pull/925
.. _19add16: https://github.com/python-semantic-release/python-semantic-release/commit/19add16dcfdfdb812efafe2d492a933d0856df1d
.. _3a41995: https://github.com/python-semantic-release/python-semantic-release/commit/3a4199542d0ea4dbf88fa35e11bec41d0c27dd17
.. _6b5b271: https://github.com/python-semantic-release/python-semantic-release/commit/6b5b271453874b982fbf2827ec1f6be6db1c2cc7


.. _changelog-v9.7.1:

v9.7.1 (2024-05-07)
===================

🪲 Bug Fixes
------------

* **gha**: Fix missing ``git_committer_*`` definition in action (`#919`_, `ccef9d8`_)

Resolves: #918

.. _#919: https://github.com/python-semantic-release/python-semantic-release/pull/919
.. _ccef9d8: https://github.com/python-semantic-release/python-semantic-release/commit/ccef9d8521be12c0640369b3c3a80b81a7832662


.. _changelog-v9.7.0:

v9.7.0 (2024-05-06)
===================

✨ Features
-----------

* **version-cmd**: Pass ``NEW_VERSION`` & useful env vars to build command (`ee6b246`_)

🪲 Bug Fixes
------------

* **gha**: Add missing ``tag`` option to GitHub Action definition (`#908`_, `6b24288`_)

Resolves: #906

📖 Documentation
----------------

* **configuration**: Add description of build command available env variables (`c882dc6`_)

.. _#908: https://github.com/python-semantic-release/python-semantic-release/pull/908
.. _6b24288: https://github.com/python-semantic-release/python-semantic-release/commit/6b24288a96302cd6982260e46fad128ec4940da9
.. _c882dc6: https://github.com/python-semantic-release/python-semantic-release/commit/c882dc62b860b2aeaa925c21d1524f4ae25ef567
.. _ee6b246: https://github.com/python-semantic-release/python-semantic-release/commit/ee6b246df3bb211ab49c8bce075a4c3f6a68ed77


.. _changelog-v9.6.0:

v9.6.0 (2024-04-29)
===================

✨ Features
-----------

* Changelog filters are specialized per vcs type (`#890`_, `76ed593`_)

* fix(github): correct changelog filter for pull request urls

* feat(changelog): changelog filters are hvcs focused

* feat(changelog-github): add issue url filter to changelog context

* feat(changelog-gitea): add issue url filter to changelog context

* feat(changelog-context): add flag to jinja env for which hvcs is available

* docs(changelog-context): explain new hvcs specific context filters

🪲 Bug Fixes
------------

* Correct version ``--prerelease`` use & enable ``--as-prerelease`` (`#647`_, `2acb5ac`_)

* fix(version-cmd): correct ``--prerelease`` use

Prior to this change, ``--prerelease`` performed the role of converting whichever forced version
  into a prerelease version declaration, which was an unintentional breaking change to the CLI
  compared to v7.

``--prerelease`` now forces the next version to increment the prerelease revision, which makes it
  consistent with `--patch`, ``--minor`` and `--major`. Temporarily disabled the ability to force a
  prerelease.

Resolves: #639

* feat(version-cmd): add ``--as-prerelease`` option to force the next version to be a prerelease

Prior to this change, ``--prerelease`` performed the role that ``--as-prerelease`` now does, which
  was an unintentional breaking change to the CLI compared to v7.

``--prerelease`` is used to force the next version to increment the prerelease revision, which makes
  it consistent with `--patch`, ``--minor`` and `--major`, while ``--as-prerelease`` forces for the
  next version to be converted to a prerelease version type before it is applied to the project
  regardless of the bump level.

Resolves: #639

* docs(commands): update version command options definition about prereleases

---------

Co-authored-by: codejedi365 <codejedi365@gmail.com>

* **parser-custom**: Gracefully handle custom parser import errors (`67f6038`_)

.. _#647: https://github.com/python-semantic-release/python-semantic-release/pull/647
.. _#890: https://github.com/python-semantic-release/python-semantic-release/pull/890
.. _2acb5ac: https://github.com/python-semantic-release/python-semantic-release/commit/2acb5ac35ae79d7ae25ca9a03fb5c6a4a68b3673
.. _67f6038: https://github.com/python-semantic-release/python-semantic-release/commit/67f60389e3f6e93443ea108c0e1b4d30126b8e06
.. _76ed593: https://github.com/python-semantic-release/python-semantic-release/commit/76ed593ea33c851005994f0d1a6a33cc890fb908


.. _changelog-v9.5.0:

v9.5.0 (2024-04-23)
===================

✨ Features
-----------

* Extend support to on-prem GitHub Enterprise Server (`#896`_, `4fcb737`_)

* feat(github): extend support to on-prem GitHub Enterprise Server

Resolves: #895

⚙️ Build System
----------------

* **deps**: Bump ruff from 0.3.5 to 0.3.7 (`#894`_, `6bf2849`_)

.. _#894: https://github.com/python-semantic-release/python-semantic-release/pull/894
.. _#896: https://github.com/python-semantic-release/python-semantic-release/pull/896
.. _4fcb737: https://github.com/python-semantic-release/python-semantic-release/commit/4fcb737958d95d1a3be24db7427e137b46f5075f
.. _6bf2849: https://github.com/python-semantic-release/python-semantic-release/commit/6bf28496d8631ada9009aec5f1000f68b7f7ee16


.. _changelog-v9.4.2:

v9.4.2 (2024-04-14)
===================

🪲 Bug Fixes
------------

* **hvcs**: Allow insecure http connections if configured (`#886`_, `db13438`_)

* fix(gitlab): allow insecure http connections if configured

* fix(gitea): allow insecure http connections if configured

* fix(github): allow insecure http connections if configured

* fix(bitbucket): allow insecure http connections if configured

* fix(config): add flag to allow insecure connections

* fix(version-cmd): handle HTTP exceptions more gracefully

* docs(configuration): update ``remote`` settings section with missing values

Resolves: #868

* **hvcs**: Prevent double url schemes urls in changelog (`#676`_, `5cfdb24`_)

* fix(hvcs): prevent double protocol scheme urls in changelogs

* fix(bitbucket): correct url parsing & prevent double url schemes

* fix(gitea): correct url parsing & prevent double url schemes

* fix(github): correct url parsing & prevent double url schemes

* fix(gitlab): correct url parsing & prevent double url schemes

⚙️ Build System
----------------

* **deps**: Update rich requirement from ~=12.5 to ~=13.0 (`#877`_, `4a22a8c`_)

Resolves: #888

.. _#676: https://github.com/python-semantic-release/python-semantic-release/pull/676
.. _#877: https://github.com/python-semantic-release/python-semantic-release/pull/877
.. _#886: https://github.com/python-semantic-release/python-semantic-release/pull/886
.. _4a22a8c: https://github.com/python-semantic-release/python-semantic-release/commit/4a22a8c1a69bcf7b1ddd6db56e6883c617a892b3
.. _5cfdb24: https://github.com/python-semantic-release/python-semantic-release/commit/5cfdb248c003a2d2be5fe65fb61d41b0d4c45db5
.. _db13438: https://github.com/python-semantic-release/python-semantic-release/commit/db1343890f7e0644bc8457f995f2bd62087513d3


.. _changelog-v9.4.1:

v9.4.1 (2024-04-06)
===================

🪲 Bug Fixes
------------

* **gh-actions-output**: Fixed trailing newline to match GITHUB_OUTPUT format (`#885`_, `2c7b6ec`_)

* fix(gh-actions-output): fixed trailing newline to match GITHUB_OUTPUT format

Resolves: #884

.. _#885: https://github.com/python-semantic-release/python-semantic-release/pull/885
.. _2c7b6ec: https://github.com/python-semantic-release/python-semantic-release/commit/2c7b6ec85b6e3182463d7b695ee48e9669a25b3b


.. _changelog-v9.4.0:

v9.4.0 (2024-03-31)
===================

✨ Features
-----------

* **gitea**: Derives gitea api domain from base domain when unspecified (`#675`_, `2ee3f8a`_)

* feat(gitea): derives gitea api domain from base domain when unspecified

.. _#675: https://github.com/python-semantic-release/python-semantic-release/pull/675
.. _2ee3f8a: https://github.com/python-semantic-release/python-semantic-release/commit/2ee3f8a918d2e5ea9ab64df88f52e62a1f589c38


.. _changelog-v9.3.1:

v9.3.1 (2024-03-24)
===================

🪲 Bug Fixes
------------

* **algorithm**: Handle merge-base errors gracefully (`4c998b7`_)

Merge-base errors generally occur from a shallow clone that is primarily used by CI environments and
  will cause PSR to explode prior to this change. Now it exits with an appropriate error.

Resolves: #724

* **cli-version**: Change implementation to only push the tag we generated (`8a9da4f`_)

Restricts the git push command to only push the explicit tag we created which will eliminate the
  possibility of pushing another tag that could cause an error.

Resolves: #803

⚡ Performance Improvements
---------------------------

* **algorithm**: Simplify logs & use lookup when searching for commit & tag match (`3690b95`_)

.. _3690b95: https://github.com/python-semantic-release/python-semantic-release/commit/3690b9511de633ab38083de4d2505b6d05853346
.. _4c998b7: https://github.com/python-semantic-release/python-semantic-release/commit/4c998b77a3fe5e12783d1ab2d47789a10b83f247
.. _8a9da4f: https://github.com/python-semantic-release/python-semantic-release/commit/8a9da4feb8753e3ab9ea752afa25decd2047675a


.. _changelog-v9.3.0:

v9.3.0 (2024-03-21)
===================

✨ Features
-----------

* **cmd-version**: Changelog available to bundle (`#779`_, `37fdb28`_)

* feat(cmd-version): create changelog prior to build enabling doc bundling

.. _#779: https://github.com/python-semantic-release/python-semantic-release/pull/779
.. _37fdb28: https://github.com/python-semantic-release/python-semantic-release/commit/37fdb28e0eb886d682b5dea4cc83a7c98a099422


.. _changelog-v9.2.2:

v9.2.2 (2024-03-19)
===================

🪲 Bug Fixes
------------

* **cli**: Enable subcommand help even if config is invalid (`91d221a`_)

Refactors configuration loading to use lazy loading by subcommands triggered by the property access
  of the runtime_ctx object. Resolves the issues when running ``--help`` on subcommands when a
  configuration is invalid

Resolves: #840

.. _91d221a: https://github.com/python-semantic-release/python-semantic-release/commit/91d221a01266e5ca6de5c73296b0a90987847494


.. _changelog-v9.2.1:

v9.2.1 (2024-03-19)
===================

🪲 Bug Fixes
------------

* **parse-git-url**: Handle urls with url-safe special characters (`27cd93a`_)

.. _27cd93a: https://github.com/python-semantic-release/python-semantic-release/commit/27cd93a0a65ee3787ca51be4c91c48f6ddb4269c


.. _changelog-v9.2.0:

v9.2.0 (2024-03-18)
===================

✨ Features
-----------

* **version**: Add new version print flags to display the last released version and tag (`814240c`_)

* **version-config**: Add option to disable 0.x.x versions (`dedb3b7`_)

🪲 Bug Fixes
------------

* **changelog**: Make sure default templates render ending in 1 newline (`0b4a45e`_)

* **changelog-generation**: Fix incorrect release timezone determination (`f802446`_)

📖 Documentation
----------------

* **configuration**: Add description of ``allow-zero-version`` configuration option (`4028f83`_)

* **configuration**: Clarify the ``major_on_zero`` configuration option (`f7753cd`_)

⚙️ Build System
----------------

* **deps**: Add click-option-group for grouping exclusive flags (`bd892b8`_)

.. _0b4a45e: https://github.com/python-semantic-release/python-semantic-release/commit/0b4a45e3673d0408016dc8e7b0dce98007a763e3
.. _4028f83: https://github.com/python-semantic-release/python-semantic-release/commit/4028f8384a0181c8d58c81ae81cf0b241a02a710
.. _814240c: https://github.com/python-semantic-release/python-semantic-release/commit/814240c7355df95e9be9a6ed31d004b800584bc0
.. _bd892b8: https://github.com/python-semantic-release/python-semantic-release/commit/bd892b89c26df9fccc9335c84e2b3217e3e02a37
.. _dedb3b7: https://github.com/python-semantic-release/python-semantic-release/commit/dedb3b765c8530379af61d3046c3bb9c160d54e5
.. _f7753cd: https://github.com/python-semantic-release/python-semantic-release/commit/f7753cdabd07e276bc001478d605fca9a4b37ec4
.. _f802446: https://github.com/python-semantic-release/python-semantic-release/commit/f802446bd0693c4c9f6bdfdceae8b89c447827d2


.. _changelog-v9.1.1:

v9.1.1 (2024-02-25)
===================

🪲 Bug Fixes
------------

* **parse_git_url**: Fix bad url with dash (`1c25b8e`_)

.. _1c25b8e: https://github.com/python-semantic-release/python-semantic-release/commit/1c25b8e6f1e43c15ca7d5a59dca0a13767f9bc33


.. _changelog-v9.1.0:

v9.1.0 (2024-02-14)
===================

✨ Features
-----------

* Add bitbucket hvcs (`bbbbfeb`_)

🪲 Bug Fixes
------------

* Remove unofficial environment variables (`a5168e4`_)

📖 Documentation
----------------

* Add bitbucket authentication (`b78a387`_)

* Add bitbucket to token table (`56f146d`_)

* Fix typo (`b240e12`_)

⚙️ Build System
----------------

* **deps**: Bump minimum required ``tomlkit`` to ``>=0.11.0`` (`291aace`_)

TOMLDocument is missing the ``unwrap()`` function in ``v0.10.2`` which causes an AttributeError to
  occur when attempting to read a the text in ``pyproject.toml`` as discovered with #834

Resolves: #834

.. _291aace: https://github.com/python-semantic-release/python-semantic-release/commit/291aacea1d0429a3b27e92b0a20b598f43f6ea6b
.. _56f146d: https://github.com/python-semantic-release/python-semantic-release/commit/56f146d9f4c0fc7f2a84ad11b21c8c45e9221782
.. _a5168e4: https://github.com/python-semantic-release/python-semantic-release/commit/a5168e40b9a14dbd022f62964f382b39faf1e0df
.. _b240e12: https://github.com/python-semantic-release/python-semantic-release/commit/b240e129b180d45c1d63d464283b7dfbcb641d0c
.. _b78a387: https://github.com/python-semantic-release/python-semantic-release/commit/b78a387d8eccbc1a6a424a183254fc576126199c
.. _bbbbfeb: https://github.com/python-semantic-release/python-semantic-release/commit/bbbbfebff33dd24b8aed2d894de958d532eac596


.. _changelog-v9.0.3:

v9.0.3 (2024-02-08)
===================

🪲 Bug Fixes
------------

* **algorithm**: Correct bfs to not abort on previously visited node (`02df305`_)

⚡ Performance Improvements
---------------------------

* **algorithm**: Refactor bfs search to use queue rather than recursion (`8b742d3`_)

.. _02df305: https://github.com/python-semantic-release/python-semantic-release/commit/02df305db43abfc3a1f160a4a52cc2afae5d854f
.. _8b742d3: https://github.com/python-semantic-release/python-semantic-release/commit/8b742d3db6652981a7b5f773a74b0534edc1fc15


.. _changelog-v9.0.2:

v9.0.2 (2024-02-08)
===================

🪲 Bug Fixes
------------

* **util**: Properly parse windows line-endings in commit messages (`70193ba`_)

Due to windows line-endings `\r\n`, it would improperly split the commit description (it failed to
  split at all) and cause detection of Breaking changes to fail. The breaking changes regular
  expression looks to the start of the line for the proper syntax.

Resolves: #820

📖 Documentation
----------------

* Remove duplicate note in configuration.rst (`#807`_, `fb6f243`_)

.. _#807: https://github.com/python-semantic-release/python-semantic-release/pull/807
.. _70193ba: https://github.com/python-semantic-release/python-semantic-release/commit/70193ba117c1a6d3690aed685fee8a734ba174e5
.. _fb6f243: https://github.com/python-semantic-release/python-semantic-release/commit/fb6f243a141642c02469f1080180ecaf4f3cec66


.. _changelog-v9.0.1:

v9.0.1 (2024-02-06)
===================

🪲 Bug Fixes
------------

* **config**: Set commit parser opt defaults based on parser choice (`#782`_, `9c594fb`_)

.. _#782: https://github.com/python-semantic-release/python-semantic-release/pull/782
.. _9c594fb: https://github.com/python-semantic-release/python-semantic-release/commit/9c594fb6efac7e4df2b0bfbd749777d3126d03d7


.. _changelog-v9.0.0:

v9.0.0 (2024-02-06)
===================

💥 Breaking
-----------

* Drop support for Python 3.7 (`#828`_, `ad086f5`_)

.. _#828: https://github.com/python-semantic-release/python-semantic-release/pull/828
.. _ad086f5: https://github.com/python-semantic-release/python-semantic-release/commit/ad086f5993ae4741d6e20fee618d1bce8df394fb


.. _changelog-v8.7.2:

v8.7.2 (2024-01-03)
===================

🪲 Bug Fixes
------------

* **lint**: Correct linter errors (`c9556b0`_)

.. _c9556b0: https://github.com/python-semantic-release/python-semantic-release/commit/c9556b0ca6df6a61e9ce909d18bc5be8b6154bf8


.. _changelog-v8.7.1:

v8.7.1 (2024-01-03)
===================

🪲 Bug Fixes
------------

* **cli-generate-config**: Ensure configuration types are always toml parsable (`#785`_, `758e649`_)

📖 Documentation
----------------

* Add note on default envvar behaviour (`#780`_, `0b07cae`_)

* **configuration**: Change defaults definition of token default to table (`#786`_, `df1df0d`_)

* **contributing**: Add docs-build, testing conf, & build instructions (`#787`_, `011b072`_)

.. _#780: https://github.com/python-semantic-release/python-semantic-release/pull/780
.. _#785: https://github.com/python-semantic-release/python-semantic-release/pull/785
.. _#786: https://github.com/python-semantic-release/python-semantic-release/pull/786
.. _#787: https://github.com/python-semantic-release/python-semantic-release/pull/787
.. _011b072: https://github.com/python-semantic-release/python-semantic-release/commit/011b0729cba3045b4e7291fd970cb17aad7bae60
.. _0b07cae: https://github.com/python-semantic-release/python-semantic-release/commit/0b07cae71915c5c82d7784898b44359249542a64
.. _758e649: https://github.com/python-semantic-release/python-semantic-release/commit/758e64975fe46b961809f35977574729b7c44271
.. _df1df0d: https://github.com/python-semantic-release/python-semantic-release/commit/df1df0de8bc655cbf8f86ae52aff10efdc66e6d2


.. _changelog-v8.7.0:

v8.7.0 (2023-12-22)
===================

✨ Features
-----------

* **config**: Enable default environment token per hvcs (`#774`_, `26528eb`_)

.. _#774: https://github.com/python-semantic-release/python-semantic-release/pull/774
.. _26528eb: https://github.com/python-semantic-release/python-semantic-release/commit/26528eb8794d00dfe985812269702fbc4c4ec788


.. _changelog-v8.6.0:

v8.6.0 (2023-12-22)
===================

✨ Features
-----------

* **utils**: Expand parsable valid git remote url formats (`#771`_, `cf75f23`_)

Git remote url parsing now supports additional formats (ssh, https, file, git)

📖 Documentation
----------------

* Minor correction to commit-parsing documentation (`#777`_, `245e878`_)

.. _#771: https://github.com/python-semantic-release/python-semantic-release/pull/771
.. _#777: https://github.com/python-semantic-release/python-semantic-release/pull/777
.. _245e878: https://github.com/python-semantic-release/python-semantic-release/commit/245e878f02d5cafec6baf0493c921c1e396b56e8
.. _cf75f23: https://github.com/python-semantic-release/python-semantic-release/commit/cf75f237360488ebb0088e5b8aae626e97d9cbdd


.. _changelog-v8.5.2:

v8.5.2 (2023-12-19)
===================

🪲 Bug Fixes
------------

* **cli**: Gracefully output configuration validation errors (`#772`_, `e8c9d51`_)

* fix(cli): gracefully output configuration validation errors

.. _#772: https://github.com/python-semantic-release/python-semantic-release/pull/772
.. _e8c9d51: https://github.com/python-semantic-release/python-semantic-release/commit/e8c9d516c37466a5dce75a73766d5be0f9e74627


.. _changelog-v8.5.1:

v8.5.1 (2023-12-12)
===================

🪲 Bug Fixes
------------

* **cmd-version**: Handle committing of git-ignored file gracefully (`#764`_, `ea89fa7`_)

* fix(version): only commit non git-ignored files during version commit

* **config**: Gracefully fail when repo is in a detached HEAD state (`#765`_, `ac4f9aa`_)

* fix(config): cleanly handle repository in detached HEAD state

📖 Documentation
----------------

* **configuration**: Adjust wording and improve clarity (`#766`_, `6b2fc8c`_)

* docs(configuration): fix typo in text

* docs(configuration): adjust wording and improve clarity

.. _#764: https://github.com/python-semantic-release/python-semantic-release/pull/764
.. _#765: https://github.com/python-semantic-release/python-semantic-release/pull/765
.. _#766: https://github.com/python-semantic-release/python-semantic-release/pull/766
.. _6b2fc8c: https://github.com/python-semantic-release/python-semantic-release/commit/6b2fc8c156e122ee1b43fdb513b2dc3b8fd76724
.. _ac4f9aa: https://github.com/python-semantic-release/python-semantic-release/commit/ac4f9aacb72c99f2479ae33369822faad011a824
.. _ea89fa7: https://github.com/python-semantic-release/python-semantic-release/commit/ea89fa72885e15da91687172355426a22c152513


.. _changelog-v8.5.0:

v8.5.0 (2023-12-07)
===================

✨ Features
-----------

* Allow template directories to contain a '.' at the top-level (`#762`_, `07b232a`_)

.. _#762: https://github.com/python-semantic-release/python-semantic-release/pull/762
.. _07b232a: https://github.com/python-semantic-release/python-semantic-release/commit/07b232a3b34be0b28c6af08aea4852acb1b9bd56


.. _changelog-v8.4.0:

v8.4.0 (2023-12-07)
===================

✨ Features
-----------

* **cmd-version**: Add ``--tag/--no-tag`` option to version command (`#752`_, `de6b9ad`_)

* fix(version): separate push tags from commit push when not committing changes

* feat(version): add ``--no-tag`` option to turn off tag creation

* docs(commands): update ``version`` subcommand options

📖 Documentation
----------------

* **migration**: Fix comments about publish command (`#747`_, `90380d7`_)

.. _#747: https://github.com/python-semantic-release/python-semantic-release/pull/747
.. _#752: https://github.com/python-semantic-release/python-semantic-release/pull/752
.. _90380d7: https://github.com/python-semantic-release/python-semantic-release/commit/90380d797a734dcca5040afc5fa00e3e01f64152
.. _de6b9ad: https://github.com/python-semantic-release/python-semantic-release/commit/de6b9ad921e697b5ea2bb2ea8f180893cecca920


.. _changelog-v8.3.0:

v8.3.0 (2023-10-23)
===================

✨ Features
-----------

* **action**: Use composite action for semantic release (`#692`_, `4648d87`_)

Co-authored-by: Bernard Cooke <bernard-cooke@hotmail.com>

.. _#692: https://github.com/python-semantic-release/python-semantic-release/pull/692
.. _4648d87: https://github.com/python-semantic-release/python-semantic-release/commit/4648d87bac8fb7e6cc361b765b4391b30a8caef8


.. _changelog-v8.2.0:

v8.2.0 (2023-10-23)
===================

✨ Features
-----------

* Allow user customization of release notes template (`#736`_, `94a1311`_)

Signed-off-by: Bryant Finney <bryant.finney@outlook.com>

📖 Documentation
----------------

* Add PYTHONPATH mention for commit parser (`3284258`_)

.. _#736: https://github.com/python-semantic-release/python-semantic-release/pull/736
.. _3284258: https://github.com/python-semantic-release/python-semantic-release/commit/3284258b9fa1a3fe165f336181aff831d50fddd3
.. _94a1311: https://github.com/python-semantic-release/python-semantic-release/commit/94a131167e1b867f8bc112a042b9766e050ccfd1


.. _changelog-v8.1.2:

v8.1.2 (2023-10-13)
===================

🪲 Bug Fixes
------------

* Correct lint errors (`a13a6c3`_)

GitHub.upload_asset now raises ValueError instead of requests.HTTPError

* Error when running build command on windows systems (`#732`_, `2553657`_)

.. _#732: https://github.com/python-semantic-release/python-semantic-release/pull/732
.. _2553657: https://github.com/python-semantic-release/python-semantic-release/commit/25536574760b407410f435441da533fafbf94402
.. _a13a6c3: https://github.com/python-semantic-release/python-semantic-release/commit/a13a6c37e180dc422599939a5725835306c18ff2


.. _changelog-v8.1.1:

v8.1.1 (2023-09-19)
===================

🪲 Bug Fixes
------------

* Attribute error when logging non-strings (`#711`_, `75e6e48`_)

.. _#711: https://github.com/python-semantic-release/python-semantic-release/pull/711
.. _75e6e48: https://github.com/python-semantic-release/python-semantic-release/commit/75e6e48129da8238a62d5eccac1ae55d0fee0f9f


.. _changelog-v8.1.0:

v8.1.0 (2023-09-19)
===================

✨ Features
-----------

* Upgrade pydantic to v2 (`#714`_, `5a5c5d0`_)

📖 Documentation
----------------

* Fix typos (`#708`_, `2698b0e`_)

* Update project urls (`#715`_, `5fd5485`_)

.. _#708: https://github.com/python-semantic-release/python-semantic-release/pull/708
.. _#714: https://github.com/python-semantic-release/python-semantic-release/pull/714
.. _#715: https://github.com/python-semantic-release/python-semantic-release/pull/715
.. _2698b0e: https://github.com/python-semantic-release/python-semantic-release/commit/2698b0e006ff7e175430b98450ba248ed523b341
.. _5a5c5d0: https://github.com/python-semantic-release/python-semantic-release/commit/5a5c5d0ee347750d7c417c3242d52e8ada50b217
.. _5fd5485: https://github.com/python-semantic-release/python-semantic-release/commit/5fd54856dfb6774feffc40d36d5bb0f421f04842


.. _changelog-v8.0.8:

v8.0.8 (2023-08-26)
===================

🪲 Bug Fixes
------------

* Dynamic_import() import path split (`#686`_, `1007a06`_)

.. _#686: https://github.com/python-semantic-release/python-semantic-release/pull/686
.. _1007a06: https://github.com/python-semantic-release/python-semantic-release/commit/1007a06d1e16beef6d18f44ff2e0e09921854b54


.. _changelog-v8.0.7:

v8.0.7 (2023-08-16)
===================

🪲 Bug Fixes
------------

* Use correct upload url for github (`#661`_, `8a515ca`_)

Co-authored-by: github-actions <action@github.com>

.. _#661: https://github.com/python-semantic-release/python-semantic-release/pull/661
.. _8a515ca: https://github.com/python-semantic-release/python-semantic-release/commit/8a515caf1f993aa653e024beda2fdb9e629cc42a


.. _changelog-v8.0.6:

v8.0.6 (2023-08-13)
===================

🪲 Bug Fixes
------------

* **publish**: Improve error message when no tags found (`#683`_, `bdc06ea`_)

.. _#683: https://github.com/python-semantic-release/python-semantic-release/pull/683
.. _bdc06ea: https://github.com/python-semantic-release/python-semantic-release/commit/bdc06ea061c19134d5d74bd9f168700dd5d9bcf5


.. _changelog-v8.0.5:

v8.0.5 (2023-08-10)
===================

🪲 Bug Fixes
------------

* Don't warn about vcs token if ignore_token_for_push is true. (`#670`_, `f1a54a6`_)

* fix: don't warn about vcs token if ignore_token_for_push is true.

* docs: ``password`` should be `token`.

📖 Documentation
----------------

* Fix typo missing 's' in version_variable[s] in configuration.rst (`#668`_, `879186a`_)

.. _#668: https://github.com/python-semantic-release/python-semantic-release/pull/668
.. _#670: https://github.com/python-semantic-release/python-semantic-release/pull/670
.. _879186a: https://github.com/python-semantic-release/python-semantic-release/commit/879186aa09a3bea8bbe2b472f892cf7c0712e557
.. _f1a54a6: https://github.com/python-semantic-release/python-semantic-release/commit/f1a54a6c9a05b225b6474d50cd610eca19ec0c34


.. _changelog-v8.0.4:

v8.0.4 (2023-07-26)
===================

🪲 Bug Fixes
------------

* **changelog**: Use version as semver tag by default (`#653`_, `5984c77`_)

📖 Documentation
----------------

* Add Python 3.11 to classifiers in metadata (`#651`_, `5a32a24`_)

* Clarify usage of assets config option (`#655`_, `efa2b30`_)

.. _#651: https://github.com/python-semantic-release/python-semantic-release/pull/651
.. _#653: https://github.com/python-semantic-release/python-semantic-release/pull/653
.. _#655: https://github.com/python-semantic-release/python-semantic-release/pull/655
.. _5984c77: https://github.com/python-semantic-release/python-semantic-release/commit/5984c7771edc37f0d7d57894adecc2591efc414d
.. _5a32a24: https://github.com/python-semantic-release/python-semantic-release/commit/5a32a24bf4128c39903f0c5d3bd0cb1ccba57e18
.. _efa2b30: https://github.com/python-semantic-release/python-semantic-release/commit/efa2b3019b41eb427f0e1c8faa21ad10664295d0


.. _changelog-v8.0.3:

v8.0.3 (2023-07-21)
===================

🪲 Bug Fixes
------------

* Skip unparseable versions when calculating next version (`#649`_, `88f25ea`_)

.. _#649: https://github.com/python-semantic-release/python-semantic-release/pull/649
.. _88f25ea: https://github.com/python-semantic-release/python-semantic-release/commit/88f25eae62589cdf53dbc3dfcb167a3ae6cba2d3


.. _changelog-v8.0.2:

v8.0.2 (2023-07-18)
===================

🪲 Bug Fixes
------------

* Handle missing configuration (`#644`_, `f15753c`_)

📖 Documentation
----------------

* Better description for tag_format usage (`2129b72`_)

* Clarify v8 breaking changes in GitHub action inputs (`#643`_, `cda050c`_)

* Correct version_toml example in migrating_from_v7.rst (`#641`_, `325d5e0`_)

.. _#641: https://github.com/python-semantic-release/python-semantic-release/pull/641
.. _#643: https://github.com/python-semantic-release/python-semantic-release/pull/643
.. _#644: https://github.com/python-semantic-release/python-semantic-release/pull/644
.. _2129b72: https://github.com/python-semantic-release/python-semantic-release/commit/2129b729837eccc41a33dbb49785a8a30ce6b187
.. _325d5e0: https://github.com/python-semantic-release/python-semantic-release/commit/325d5e048bd89cb2a94c47029d4878b27311c0f0
.. _cda050c: https://github.com/python-semantic-release/python-semantic-release/commit/cda050cd9e789d81458157ee240ff99ec65c6f25
.. _f15753c: https://github.com/python-semantic-release/python-semantic-release/commit/f15753ce652f36cc03b108c667a26ab74bcbf95d


.. _changelog-v8.0.1:

v8.0.1 (2023-07-17)
===================

🪲 Bug Fixes
------------

* Invalid version in Git history should not cause a release failure (`#632`_, `254430b`_)

📖 Documentation
----------------

* Reduce readthedocs formats and add entries to migration from v7 guide (`9b6ddfe`_)

* **migration**: Fix hyperlink (`#631`_, `5fbd52d`_)

.. _#631: https://github.com/python-semantic-release/python-semantic-release/pull/631
.. _#632: https://github.com/python-semantic-release/python-semantic-release/pull/632
.. _254430b: https://github.com/python-semantic-release/python-semantic-release/commit/254430b5cc5f032016b4c73168f0403c4d87541e
.. _5fbd52d: https://github.com/python-semantic-release/python-semantic-release/commit/5fbd52d7de4982b5689651201a0e07b445158645
.. _9b6ddfe: https://github.com/python-semantic-release/python-semantic-release/commit/9b6ddfef448f9de30fa2845034f76655d34a9912


.. _changelog-v8.0.0:

v8.0.0 (2023-07-16)
===================

💥 Breaking
-----------

* V8 (`#619`_, `ec30564`_)

* feat!: 8.0.x (#538)

Co-authored-by: Johan <johanhmr@gmail.com> Co-authored-by: U-NEO\johan <johan.hammar@ombea.com>

* fix: correct Dockerfile CLI command and GHA fetch

* fix: resolve branch checkout logic in GHA

* fix: remove commit amending behaviour

this was not working when there were no source code changes to be made, as it lead to attempting to
  amend a HEAD commit that wasn't produced by PSR

* 8.0.0-alpha.1

Automatically generated by python-semantic-release

* fix: correct logic for generating release notes (#550)

* fix: cleanup comments and unused logic

* fix(action): mark container fs as safe for git to operate on

* fix(action): quotation for git config command

* 8.0.0-alpha.2

Automatically generated by python-semantic-release

* fix: resolve bug in changelog logic, enable upload to pypi

* 8.0.0-alpha.3

Automatically generated by python-semantic-release

* fix: resolve loss of tag_format configuration

* 8.0.0-alpha.4

Automatically generated by python-semantic-release

* feat: various improvements

* Added sorting to test parameterisation, so that pytest-xdist works again - dramatic speedup for
  testing * Reworked the CI verification code so it's a bit prettier * Added more testing for the
  version CLI command, and split some logic out of the command itself * Removed a redundant
  double-regex match in VersionTranslator and Version, for some speedup

* refactor!: remove verify-ci command

* 8.0.0-alpha.5

Automatically generated by python-semantic-release

* fix(docs): fixup docs and remove reference to dist publication

* feat!: remove publication of dists to artefact repository

* feat: rename 'upload' configuration section to 'publish'

* feat!: removed build status checking

* feat: add GitHub Actions output

* fix(action): remove default for 'force'

* fix(ci): different workflow for v8

* fix(action): correct input parsing

* fix: correct handling of build commands

* feat: make it easier to access commit messages in ParsedCommits

* fix: make additional attributes available for template authors

* fix: add logging for token auth, use token for push

* ci: add verbosity

* fix: caching for repo owner and name

* ci: contents permission for workflow

* 8.0.0-alpha.6

Automatically generated by python-semantic-release

* docs: update docs with additional required permissions

* feat: add option to specify tag to publish to in publish command

* feat: add Strict Mode

* docs: convert to Furo theme

* feat: add --skip-build option

* 8.0.0-alpha.7

Automatically generated by python-semantic-release

* ci: pass tag output and conditionally execute publish steps

* fix: correct assets type in configuration (#603)

* change raw config assets type

* fix: correct assets type-annotation for RuntimeContext

---------

Co-authored-by: Bernard Cooke <bernard-cooke@hotmail.com>

* 8.0.0-alpha.8

Automatically generated by python-semantic-release

* fix: pin Debian version in Dockerfile

* feat: promote to rc

* 8.0.0-rc.1

Automatically generated by python-semantic-release

* ci: fix conditionals in workflow and update documentation

* ci: correct conditionals

* fix: only call Github Action output callback once defaults are set

* 8.0.0-rc.2

Automatically generated by python-semantic-release

* fix: create_or_update_release for Gitlab hvcs

* ci: remove separate v8 workflow

* 8.0.0-rc.3

Automatically generated by python-semantic-release

* fix(deps): add types-click, and downgrade sphinx/furo for 3.7

* 8.0.0-rc.4

Automatically generated by python-semantic-release

* docs: fix typo (#623)

* docs: correct typo in docs/changelog_templates.rst

Co-authored-by: Micael Jarniac <micael@jarniac.com>

---------

Co-authored-by: Johan <johanhmr@gmail.com> Co-authored-by: U-NEO\johan <johan.hammar@ombea.com>
  Co-authored-by: semantic-release <semantic-release> Co-authored-by: github-actions
  <action@github.com> Co-authored-by: smeng9 <38666763+smeng9@users.noreply.github.com>
  Co-authored-by: Micael Jarniac <micael@jarniac.com>

.. _#619: https://github.com/python-semantic-release/python-semantic-release/pull/619
.. _ec30564: https://github.com/python-semantic-release/python-semantic-release/commit/ec30564b4ec732c001d76d3c09ba033066d2b6fe


.. _changelog-v7.34.6:

v7.34.6 (2023-06-17)
====================

🪲 Bug Fixes
------------

* Relax invoke dependency constraint (`18ea200`_)

.. _18ea200: https://github.com/python-semantic-release/python-semantic-release/commit/18ea200633fd67e07f3d4121df5aa4c6dd29d154


.. _changelog-v7.34.5:

v7.34.5 (2023-06-17)
====================

🪲 Bug Fixes
------------

* Consider empty commits (`#608`_, `6f2e890`_)

.. _#608: https://github.com/python-semantic-release/python-semantic-release/pull/608
.. _6f2e890: https://github.com/python-semantic-release/python-semantic-release/commit/6f2e8909636595d3cb5e858f42c63820cda45974


.. _changelog-v7.34.4:

v7.34.4 (2023-06-15)
====================

🪲 Bug Fixes
------------

* Docker build fails installing git (`#605`_, `9e3eb97`_)

git was installed from bullseye-backports, but base image is referencing latest python:3.10 since
  bookworm was recently released, this now points at bookworm and installing the backport of git is
  actually trying to downgrade, resulting in this error:

> E: Packages were downgraded and -y was used without --allow-downgrades.

> ERROR: failed to solve: process "/bin/sh -c echo \"deb http://deb.debian.org/debian
  bullseye-backports main\" >> /etc/apt/sources.list; apt-get update; apt-get install -y
  git/bullseye-backports" did not complete successfully: exit code: 100

.. _#605: https://github.com/python-semantic-release/python-semantic-release/pull/605
.. _9e3eb97: https://github.com/python-semantic-release/python-semantic-release/commit/9e3eb979783bc39ca564c2967c6c77eecba682e6


.. _changelog-v7.34.3:

v7.34.3 (2023-06-01)
====================

🪲 Bug Fixes
------------

* Generate markdown linter compliant changelog headers & lists (`#597`_, `cc87400`_)

In #594, I missed that there are 2 places where the version header is formatted

.. _#597: https://github.com/python-semantic-release/python-semantic-release/pull/597
.. _cc87400: https://github.com/python-semantic-release/python-semantic-release/commit/cc87400d4a823350de7d02dc3172d2488c9517db


.. _changelog-v7.34.2:

v7.34.2 (2023-05-29)
====================

🪲 Bug Fixes
------------

* Open all files with explicit utf-8 encoding (`#596`_, `cb71f35`_)

.. _#596: https://github.com/python-semantic-release/python-semantic-release/pull/596
.. _cb71f35: https://github.com/python-semantic-release/python-semantic-release/commit/cb71f35c26c1655e675fa735fa880d39a2c8af9c


.. _changelog-v7.34.1:

v7.34.1 (2023-05-28)
====================

🪲 Bug Fixes
------------

* Generate markdown linter compliant changelog headers & lists (`#594`_, `9d9d403`_)

Add an extra new line after each header and between sections to fix 2 markdownlint errors for
  changelogs generated by this package

.. _#594: https://github.com/python-semantic-release/python-semantic-release/pull/594
.. _9d9d403: https://github.com/python-semantic-release/python-semantic-release/commit/9d9d40305c499c907335abe313e3ed122db0b154


.. _changelog-v7.34.0:

v7.34.0 (2023-05-28)
====================

✨ Features
-----------

* Add option to only parse commits for current working directory (`#509`_, `cdf8116`_)

When running the application from a sub-directory in the VCS, the option use_only_cwd_commits will
  filter out commits that does not changes the current working directory, similar to running
  commands like ``git log -- .`` in a sub-directory.

.. _#509: https://github.com/python-semantic-release/python-semantic-release/pull/509
.. _cdf8116: https://github.com/python-semantic-release/python-semantic-release/commit/cdf8116c1e415363b10a01f541873e04ad874220


.. _changelog-v7.33.5:

v7.33.5 (2023-05-19)
====================

🪲 Bug Fixes
------------

* Update docs and default config for gitmoji changes (`#590`_, `192da6e`_)

* fix: update docs and default config for gitmoji changes

PR #582 updated to the latest Gitmojis release however the documentation and default config options
  still referenced old and unsupported Gitmojis.

* fix: update sphinx dep

I could only build the documentation locally by updating Sphinx to the latest 1.x version.

📖 Documentation
----------------

* Update broken badge and add links (`#591`_, `0c23447`_)

The "Test Status" badge was updated to address a recent breaking change in the GitHub actions API.
  All the badges updated to add links to the appropriate resources for end-user convenience.

.. _#590: https://github.com/python-semantic-release/python-semantic-release/pull/590
.. _#591: https://github.com/python-semantic-release/python-semantic-release/pull/591
.. _0c23447: https://github.com/python-semantic-release/python-semantic-release/commit/0c234475d27ad887b19170c82deb80293b3a95f1
.. _192da6e: https://github.com/python-semantic-release/python-semantic-release/commit/192da6e1352298b48630423d50191070a1c5ab24


.. _changelog-v7.33.4:

v7.33.4 (2023-05-14)
====================

🪲 Bug Fixes
------------

* If prerelease, publish prerelease (`#587`_, `927da9f`_)

Co-authored-by: Ondrej Winter <ondrej.winter@gmail.com>

.. _#587: https://github.com/python-semantic-release/python-semantic-release/pull/587
.. _927da9f: https://github.com/python-semantic-release/python-semantic-release/commit/927da9f8feb881e02bc08b33dc559bd8e7fc41ab


.. _changelog-v7.33.3:

v7.33.3 (2023-04-24)
====================

🪲 Bug Fixes
------------

* Trim emojis from config (`#583`_, `02902f7`_)

* Update Gitmojis according to official node module (`#582`_, `806fcfa`_)

📖 Documentation
----------------

* Grammar in ``docs/troubleshooting.rst`` (`#557`_, `bbe754a`_)

- change contraction to a possessive pronoun

Signed-off-by: Vladislav Doster <mvdoster@gmail.com>

* Spelling and grammar in ``travis.rst`` (`#556`_, `3a76e9d`_)

- spelling - subject-verb agreement - remove verbiage

Signed-off-by: Vladislav Doster <mvdoster@gmail.com>

* Update repository name (`#559`_, `5cdb05e`_)

In order to avoid 'Repository not found: relekang/python-semantic-release.'

.. _#556: https://github.com/python-semantic-release/python-semantic-release/pull/556
.. _#557: https://github.com/python-semantic-release/python-semantic-release/pull/557
.. _#559: https://github.com/python-semantic-release/python-semantic-release/pull/559
.. _#582: https://github.com/python-semantic-release/python-semantic-release/pull/582
.. _#583: https://github.com/python-semantic-release/python-semantic-release/pull/583
.. _02902f7: https://github.com/python-semantic-release/python-semantic-release/commit/02902f73ee961565c2470c000f00947d9ef06cb1
.. _3a76e9d: https://github.com/python-semantic-release/python-semantic-release/commit/3a76e9d7505c421009eb3e953c32cccac2e70e07
.. _5cdb05e: https://github.com/python-semantic-release/python-semantic-release/commit/5cdb05e20f17b12890e1487c42d317dcbadd06c8
.. _806fcfa: https://github.com/python-semantic-release/python-semantic-release/commit/806fcfa4cfdd3df4b380afd015a68dc90d54215a
.. _bbe754a: https://github.com/python-semantic-release/python-semantic-release/commit/bbe754a3db9ce7132749e7902fe118b52f48ee42


.. _changelog-v7.33.2:

v7.33.2 (2023-02-17)
====================

🪲 Bug Fixes
------------

* Inconsistent versioning between print-version and publish (`#524`_, `17d60e9`_)

.. _#524: https://github.com/python-semantic-release/python-semantic-release/pull/524
.. _17d60e9: https://github.com/python-semantic-release/python-semantic-release/commit/17d60e9bf66f62e5845065486c9d5e450f74839a


.. _changelog-v7.33.1:

v7.33.1 (2023-02-01)
====================

🪲 Bug Fixes
------------

* **action**: Mark container fs as safe for git (`#552`_, `2a55f68`_)

See https://github.com/actions/runner-images/issues/6775#issuecomment-1409268124 and
  https://github.com/actions/runner-images/issues/6775#issuecomment-1410270956

.. _#552: https://github.com/python-semantic-release/python-semantic-release/pull/552
.. _2a55f68: https://github.com/python-semantic-release/python-semantic-release/commit/2a55f68e2b3cb9ffa9204c00ddbf12706af5c070


.. _changelog-v7.33.0:

v7.33.0 (2023-01-15)
====================

✨ Features
-----------

* Add signing options to action (`31ad5eb`_)

* Update action with configuration options (`#518`_, `4664afe`_)

Co-authored-by: Kevin Watson <Kevmo92@users.noreply.github.com>

* **repository**: Add support for TWINE_CERT (`#522`_, `d56e85d`_)

    Fixes #521

🪲 Bug Fixes
------------

* Bump Dockerfile to use Python 3.10 image (`#536`_, `8f2185d`_)

Fixes #533

Co-authored-by: Bernard Cooke <bernard.cooke@iotics.com>

* Changelog release commit search logic (`#530`_, `efb3410`_)

* Fixes changelog release commit search logic

Running ``semantic-release changelog`` currently fails to identify "the last commit in [a] release"
  because the compared commit messages have superfluous whitespace. Likely related to the issue
  causing: https://github.com/relekang/python-semantic-release/issues/490

* Removes a couple of extra ``strip()`` function calls

* Fix mypy errors for publish (`b40dd48`_)

* Formatting in docs (`2e8227a`_)

* Update documentaton (`5cbdad2`_)

* **action**: Fix environment variable names (`3c66218`_)

.. _#518: https://github.com/python-semantic-release/python-semantic-release/pull/518
.. _#522: https://github.com/python-semantic-release/python-semantic-release/pull/522
.. _#530: https://github.com/python-semantic-release/python-semantic-release/pull/530
.. _#536: https://github.com/python-semantic-release/python-semantic-release/pull/536
.. _2e8227a: https://github.com/python-semantic-release/python-semantic-release/commit/2e8227a8a933683250f8dace019df15fdb35a857
.. _31ad5eb: https://github.com/python-semantic-release/python-semantic-release/commit/31ad5eb5a25f0ea703afc295351104aefd66cac1
.. _3c66218: https://github.com/python-semantic-release/python-semantic-release/commit/3c66218640044adf263fcf9b2714cfc4b99c2e90
.. _4664afe: https://github.com/python-semantic-release/python-semantic-release/commit/4664afe5f80a04834e398fefb841b166a51d95b7
.. _5cbdad2: https://github.com/python-semantic-release/python-semantic-release/commit/5cbdad296034a792c9bf05e3700eac4f847eb469
.. _8f2185d: https://github.com/python-semantic-release/python-semantic-release/commit/8f2185d570b3966b667ac591ae523812e9d2e00f
.. _b40dd48: https://github.com/python-semantic-release/python-semantic-release/commit/b40dd484387c1b3f78df53ee2d35e281e8e799c8
.. _d56e85d: https://github.com/python-semantic-release/python-semantic-release/commit/d56e85d1f2ac66fb0b59af2178164ca915dbe163
.. _efb3410: https://github.com/python-semantic-release/python-semantic-release/commit/efb341036196c39b4694ca4bfa56c6b3e0827c6c


.. _changelog-v7.32.2:

v7.32.2 (2022-10-22)
====================

🪲 Bug Fixes
------------

* Fix changelog generation in tag-mode (`#171`_, `482a62e`_)

📖 Documentation
----------------

* Fix code blocks (`#506`_, `24b7673`_)

    Previously: https://i.imgur.com/XWFhG7a.png

.. _#171: https://github.com/python-semantic-release/python-semantic-release/pull/171
.. _#506: https://github.com/python-semantic-release/python-semantic-release/pull/506
.. _24b7673: https://github.com/python-semantic-release/python-semantic-release/commit/24b767339fcef1c843f7dd3188900adab05e03b1
.. _482a62e: https://github.com/python-semantic-release/python-semantic-release/commit/482a62ec374208b2d57675cb0b7f0ab9695849b9


.. _changelog-v7.32.1:

v7.32.1 (2022-10-07)
====================

🪲 Bug Fixes
------------

* Corrections for deprecation warnings (`#505`_, `d47afb6`_)

📖 Documentation
----------------

* Correct spelling mistakes (`#504`_, `3717e0d`_)

.. _#504: https://github.com/python-semantic-release/python-semantic-release/pull/504
.. _#505: https://github.com/python-semantic-release/python-semantic-release/pull/505
.. _3717e0d: https://github.com/python-semantic-release/python-semantic-release/commit/3717e0d8810f5d683847c7b0e335eeefebbf2921
.. _d47afb6: https://github.com/python-semantic-release/python-semantic-release/commit/d47afb6516238939e174f946977bf4880062a622


.. _changelog-v7.32.0:

v7.32.0 (2022-09-25)
====================

✨ Features
-----------

* Add setting for enforcing textual changelog sections (`#502`_, `988437d`_)

Resolves #498

Add the ``use_textual_changelog_sections`` setting flag for enforcing that changelog section
  headings will always be regular ASCII when using the Emoji parser.

📖 Documentation
----------------

* Correct documented default behaviour for ``commit_version_number`` (`#497`_, `ffae2dc`_)

.. _#497: https://github.com/python-semantic-release/python-semantic-release/pull/497
.. _#502: https://github.com/python-semantic-release/python-semantic-release/pull/502
.. _988437d: https://github.com/python-semantic-release/python-semantic-release/commit/988437d21e40d3e3b1c95ed66b535bdd523210de
.. _ffae2dc: https://github.com/python-semantic-release/python-semantic-release/commit/ffae2dc68f7f4bc13c5fd015acd43b457e568ada


.. _changelog-v7.31.4:

v7.31.4 (2022-08-23)
====================

🪲 Bug Fixes
------------

* Account for trailing newlines in commit messages (`#495`_, `111b151`_)

    Fixes #490

.. _#495: https://github.com/python-semantic-release/python-semantic-release/pull/495
.. _111b151: https://github.com/python-semantic-release/python-semantic-release/commit/111b1518e8c8e2bd7535bd4c4b126548da384605


.. _changelog-v7.31.3:

v7.31.3 (2022-08-22)
====================

🪲 Bug Fixes
------------

* Use ``commit_subject`` when searching for release commits (`#488`_, `3849ed9`_)

Co-authored-by: Dzmitry Ryzhykau <d.ryzhykau@onesoil.ai>

.. _#488: https://github.com/python-semantic-release/python-semantic-release/pull/488
.. _3849ed9: https://github.com/python-semantic-release/python-semantic-release/commit/3849ed992c3cff9054b8690bcf59e49768f84f47


.. _changelog-v7.31.2:

v7.31.2 (2022-07-29)
====================

🪲 Bug Fixes
------------

* Add better handling of missing changelog placeholder (`e7a0e81`_)

There is still one case where we don't add it, but in those corner cases it would be better to do it
  manually than to make it mangled.

Fixes #454

* Add repo=None when not in git repo (`40be804`_)

    Fixes #422

📖 Documentation
----------------

* Add example for pyproject.toml (`2a4b8af`_)

.. _2a4b8af: https://github.com/python-semantic-release/python-semantic-release/commit/2a4b8af1c2893a769c02476bb92f760c8522bd7a
.. _40be804: https://github.com/python-semantic-release/python-semantic-release/commit/40be804c09ab8a036fb135c9c38a63f206d2742c
.. _e7a0e81: https://github.com/python-semantic-release/python-semantic-release/commit/e7a0e81c004ade73ed927ba4de8c3e3ccaf0047c


.. _changelog-v7.31.1:

v7.31.1 (2022-07-29)
====================

🪲 Bug Fixes
------------

* Update git email in action (`0ece6f2`_)

    Fixes #473

.. _0ece6f2: https://github.com/python-semantic-release/python-semantic-release/commit/0ece6f263ff02a17bb1e00e7ed21c490f72e3d00


.. _changelog-v7.31.0:

v7.31.0 (2022-07-29)
====================

✨ Features
-----------

* Add prerelease-patch and no-prerelease-patch flags for whether to auto-bump prereleases
  (`b4e5b62`_)

* Override repository_url w REPOSITORY_URL env var (`#439`_, `cb7578c`_)

🪲 Bug Fixes
------------

* :bug: fix get_current_release_version for tag_only version_source (`cad09be`_)

.. _#439: https://github.com/python-semantic-release/python-semantic-release/pull/439
.. _b4e5b62: https://github.com/python-semantic-release/python-semantic-release/commit/b4e5b626074f969e4140c75fdac837a0625cfbf6
.. _cad09be: https://github.com/python-semantic-release/python-semantic-release/commit/cad09be9ba067f1c882379c0f4b28115a287fc2b
.. _cb7578c: https://github.com/python-semantic-release/python-semantic-release/commit/cb7578cf005b8bd65d9b988f6f773e4c060982e3


.. _changelog-v7.30.2:

v7.30.2 (2022-07-26)
====================

🪲 Bug Fixes
------------

* Declare additional_options as action inputs (`#481`_, `cb5d8c7`_)

.. _#481: https://github.com/python-semantic-release/python-semantic-release/pull/481
.. _cb5d8c7: https://github.com/python-semantic-release/python-semantic-release/commit/cb5d8c7ce7d013fcfabd7696b5ffb846a8a6f853


.. _changelog-v7.30.1:

v7.30.1 (2022-07-25)
====================

🪲 Bug Fixes
------------

* Don't use commit_subject for tag pattern matching (`#480`_, `ac3f11e`_)

.. _#480: https://github.com/python-semantic-release/python-semantic-release/pull/480
.. _ac3f11e: https://github.com/python-semantic-release/python-semantic-release/commit/ac3f11e689f4a290d20b68b9c5c214098eb61b5f


.. _changelog-v7.30.0:

v7.30.0 (2022-07-25)
====================

✨ Features
-----------

* Add ``additional_options`` input for GitHub Action (`#477`_, `aea60e3`_)

🪲 Bug Fixes
------------

* Allow empty additional options (`#479`_, `c9b2514`_)

.. _#477: https://github.com/python-semantic-release/python-semantic-release/pull/477
.. _#479: https://github.com/python-semantic-release/python-semantic-release/pull/479
.. _aea60e3: https://github.com/python-semantic-release/python-semantic-release/commit/aea60e3d290c6fe3137bff21e0db1ed936233776
.. _c9b2514: https://github.com/python-semantic-release/python-semantic-release/commit/c9b2514d3e164b20e78b33f60989d78c2587e1df


.. _changelog-v7.29.7:

v7.29.7 (2022-07-24)
====================

🪲 Bug Fixes
------------

* Ignore dependency version bumps when parsing version from commit logs (`#476`_, `51bcb78`_)

.. _#476: https://github.com/python-semantic-release/python-semantic-release/pull/476
.. _51bcb78: https://github.com/python-semantic-release/python-semantic-release/commit/51bcb780a9f55fadfaf01612ff65c1f92642c2c1


.. _changelog-v7.29.6:

v7.29.6 (2022-07-15)
====================

🪲 Bug Fixes
------------

* Allow changing prerelease tag using CLI flags (`#466`_, `395bf4f`_)

Delay construction of version and release patterns until runtime. This will allow to use non-default
  prerelease tag.

Co-authored-by: Dzmitry Ryzhykau <d.ryzhykau@onesoil.ai>

.. _#466: https://github.com/python-semantic-release/python-semantic-release/pull/466
.. _395bf4f: https://github.com/python-semantic-release/python-semantic-release/commit/395bf4f2de73663c070f37cced85162d41934213


.. _changelog-v7.29.5:

v7.29.5 (2022-07-14)
====================

🪲 Bug Fixes
------------

* Add packaging module requirement (`#469`_, `b99c9fa`_)

* **publish**: Get version bump for current release (`#467`_, `dd26888`_)

Replicate the behavior of "version" command in version calculation.

Co-authored-by: Dzmitry Ryzhykau <d.ryzhykau@onesoil.ai>

.. _#467: https://github.com/python-semantic-release/python-semantic-release/pull/467
.. _#469: https://github.com/python-semantic-release/python-semantic-release/pull/469
.. _b99c9fa: https://github.com/python-semantic-release/python-semantic-release/commit/b99c9fa88dc25e5ceacb131cd93d9079c4fb2c86
.. _dd26888: https://github.com/python-semantic-release/python-semantic-release/commit/dd26888a923b2f480303c19f1916647de48b02bf


.. _changelog-v7.29.4:

v7.29.4 (2022-06-29)
====================

🪲 Bug Fixes
------------

* Add text for empty ValueError (`#461`_, `733254a`_)

.. _#461: https://github.com/python-semantic-release/python-semantic-release/pull/461
.. _733254a: https://github.com/python-semantic-release/python-semantic-release/commit/733254a99320d8c2f964d799ac4ec29737867faa


.. _changelog-v7.29.3:

v7.29.3 (2022-06-26)
====================

🪲 Bug Fixes
------------

* Ensure that assets can be uploaded successfully on custom GitHub servers (`#458`_, `32b516d`_)

Signed-off-by: Chris Butler <cbutler@australiacloud.com.au>

.. _#458: https://github.com/python-semantic-release/python-semantic-release/pull/458
.. _32b516d: https://github.com/python-semantic-release/python-semantic-release/commit/32b516d7aded4afcafe4aa56d6a5a329b3fc371d


.. _changelog-v7.29.2:

v7.29.2 (2022-06-20)
====================

🪲 Bug Fixes
------------

* Ensure should_bump checks against release version if not prerelease (`#457`_, `da0606f`_)

Co-authored-by: Sebastian Seith <sebastian@vermill.io>

.. _#457: https://github.com/python-semantic-release/python-semantic-release/pull/457
.. _da0606f: https://github.com/python-semantic-release/python-semantic-release/commit/da0606f0d67ada5f097c704b9423ead3b5aca6b2


.. _changelog-v7.29.1:

v7.29.1 (2022-06-01)
====================

🪲 Bug Fixes
------------

* Capture correct release version when patch has more than one digit (`#448`_, `426cdc7`_)

.. _#448: https://github.com/python-semantic-release/python-semantic-release/pull/448
.. _426cdc7: https://github.com/python-semantic-release/python-semantic-release/commit/426cdc7d7e0140da67f33b6853af71b2295aaac2


.. _changelog-v7.29.0:

v7.29.0 (2022-05-27)
====================

✨ Features
-----------

* Allow using ssh-key to push version while using token to publish to hvcs (`#419`_, `7b2dffa`_)

* feat(config): add ignore_token_for_push param

Add ignore_token_for_push parameter that allows using the underlying git authentication mechanism
  for pushing a new version commit and tags while also using an specified token to upload dists

* docs: add documentation for ignore_token_for_push

* fix(test): override GITHUB_ACTOR env

push_new_version is using GITHUB_ACTOR env var but we did not contemplate in our new tests that
  actually Github actions running the tests will populate that var and change the test outcome

Now we control the value of that env var and test for it being present or not

🪲 Bug Fixes
------------

* Fix and refactor prerelease (`#435`_, `94c9494`_)

.. _#419: https://github.com/python-semantic-release/python-semantic-release/pull/419
.. _#435: https://github.com/python-semantic-release/python-semantic-release/pull/435
.. _7b2dffa: https://github.com/python-semantic-release/python-semantic-release/commit/7b2dffadf43c77d5e0eea307aefcee5c7744df5c
.. _94c9494: https://github.com/python-semantic-release/python-semantic-release/commit/94c94942561f85f48433c95fd3467e03e0893ab4


.. _changelog-v7.28.1:

v7.28.1 (2022-04-14)
====================

🪲 Bug Fixes
------------

* Fix getting current version when ``version_source=tag_only`` (`#437`_, `b247936`_)

.. _#437: https://github.com/python-semantic-release/python-semantic-release/pull/437
.. _b247936: https://github.com/python-semantic-release/python-semantic-release/commit/b247936a81c0d859a34bf9f17ab8ca6a80488081


.. _changelog-v7.28.0:

v7.28.0 (2022-04-11)
====================

✨ Features
-----------

* Add ``tag_only`` option for ``version_source`` (`#436`_, `cf74339`_)

    Fixes #354

.. _#436: https://github.com/python-semantic-release/python-semantic-release/pull/436
.. _cf74339: https://github.com/python-semantic-release/python-semantic-release/commit/cf743395456a86c62679c2c0342502af043bfc3b


.. _changelog-v7.27.1:

v7.27.1 (2022-04-03)
====================

🪲 Bug Fixes
------------

* **prerelase**: Pass prerelease option to get_current_version (`#432`_, `aabab0b`_)

The ``get_current_version`` function accepts a ``prerelease`` argument which was never passed.

.. _#432: https://github.com/python-semantic-release/python-semantic-release/pull/432
.. _aabab0b: https://github.com/python-semantic-release/python-semantic-release/commit/aabab0b7ce647d25e0c78ae6566f1132ece9fcb9


.. _changelog-v7.27.0:

v7.27.0 (2022-03-15)
====================

✨ Features
-----------

* Add git-lfs to docker container (`#427`_, `184e365`_)

.. _#427: https://github.com/python-semantic-release/python-semantic-release/pull/427
.. _184e365: https://github.com/python-semantic-release/python-semantic-release/commit/184e3653932979b82e5a62b497f2a46cbe15ba87


.. _changelog-v7.26.0:

v7.26.0 (2022-03-07)
====================

✨ Features
-----------

* Add prerelease functionality (`#413`_, `7064265`_)

* chore: add initial todos * feat: add prerelease tag option * feat: add prerelease cli flag * feat:
  omit_pattern for previouse and current version getters * feat: print_version with prerelease bump
  * feat: make print_version prerelease ready * feat: move prerelease determination to
  get_new_version * test: improve get_last_version test * docs: added basic infos about prereleases
  * feat: add prerelease flag to version and publish * feat: remove leftover todos

Co-authored-by: Mario Jäckle <m.jaeckle@careerpartner.eu>

.. _#413: https://github.com/python-semantic-release/python-semantic-release/pull/413
.. _7064265: https://github.com/python-semantic-release/python-semantic-release/commit/7064265627a2aba09caa2873d823b594e0e23e77


.. _changelog-v7.25.2:

v7.25.2 (2022-02-24)
====================

🪲 Bug Fixes
------------

* **gitea**: Use form-data from asset upload (`#421`_, `e011944`_)

.. _#421: https://github.com/python-semantic-release/python-semantic-release/pull/421
.. _e011944: https://github.com/python-semantic-release/python-semantic-release/commit/e011944987885f75b80fe16a363f4befb2519a91


.. _changelog-v7.25.1:

v7.25.1 (2022-02-23)
====================

🪲 Bug Fixes
------------

* **gitea**: Build status and asset upload (`#420`_, `57db81f`_)

* fix(gitea): handle list build status response * fix(gitea): use form-data for upload_asset

.. _#420: https://github.com/python-semantic-release/python-semantic-release/pull/420
.. _57db81f: https://github.com/python-semantic-release/python-semantic-release/commit/57db81f4c6b96da8259e3bad9137eaccbcd10f6e


.. _changelog-v7.25.0:

v7.25.0 (2022-02-17)
====================

✨ Features
-----------

* **hvcs**: Add gitea support (`#412`_, `b7e7936`_)

📖 Documentation
----------------

* Document tag_commit (`b631ca0`_)

    Fixes #410

.. _#412: https://github.com/python-semantic-release/python-semantic-release/pull/412
.. _b631ca0: https://github.com/python-semantic-release/python-semantic-release/commit/b631ca0a79cb2d5499715d43688fc284cffb3044
.. _b7e7936: https://github.com/python-semantic-release/python-semantic-release/commit/b7e7936331b7939db09abab235c8866d800ddc1a


.. _changelog-v7.24.0:

v7.24.0 (2022-01-24)
====================

✨ Features
-----------

* Include additional changes in release commits (`3e34f95`_)

Add new config keys, ``pre_commit_command`` and `commit_additional_files`, to allow custom file
  changes alongside the release commits.

.. _3e34f95: https://github.com/python-semantic-release/python-semantic-release/commit/3e34f957ff5a3ec6e6f984cc4a79a38ce4391ea9


.. _changelog-v7.23.0:

v7.23.0 (2021-11-30)
====================

✨ Features
-----------

* Support Github Enterprise server (`b4e01f1`_)

.. _b4e01f1: https://github.com/python-semantic-release/python-semantic-release/commit/b4e01f1b7e841263fa84f57f0ac331f7c0b31954


.. _changelog-v7.22.0:

v7.22.0 (2021-11-21)
====================

✨ Features
-----------

* **parser_angular**: Allow customization in parser (`298eebb`_)

- ``parser_angular_allowed_types`` controls allowed types - defaults stay the same: build, chore,
  ci, docs, feat, fix, perf, style, refactor, test - ``parser_angular_default_level_bump`` controls
  the default level to bump the version by - default stays at 0 - ``parser_angular_minor_types``
  controls which types trigger a minor version bump - default stays at only 'feat' -
  ``parser_angular_patch_types`` controls which types trigger a patch version - default stays at
  'fix' or 'perf'

🪲 Bug Fixes
------------

* Address PR feedback for ``parser_angular.py`` (`f7bc458`_)

- ``angular_parser_default_level_bump`` should have plain-english settings - rename ``TYPES``
  variable to ``LONG_TYPE_NAMES``

.. _298eebb: https://github.com/python-semantic-release/python-semantic-release/commit/298eebbfab5c083505036ba1df47a5874a1eed6e
.. _f7bc458: https://github.com/python-semantic-release/python-semantic-release/commit/f7bc45841e6a5c762f99f936c292cee25fabcd02


.. _changelog-v7.21.0:

v7.21.0 (2021-11-21)
====================

✨ Features
-----------

* Use gitlab-ci or github actions env vars (`8ca8dd4`_)

return owner and project name from Gitlab/Github environment variables if available

Issue #363

🪲 Bug Fixes
------------

* Remove invalid repository exception (`746b62d`_)

.. _746b62d: https://github.com/python-semantic-release/python-semantic-release/commit/746b62d4e207a5d491eecd4ca96d096eb22e3bed
.. _8ca8dd4: https://github.com/python-semantic-release/python-semantic-release/commit/8ca8dd40f742f823af147928bd75a9577c50d0fd


.. _changelog-v7.20.0:

v7.20.0 (2021-11-21)
====================

✨ Features
-----------

* Allow custom environment variable names (`#392`_, `372cda3`_)

* GH_TOKEN can now be customized by setting github_token_var * GL_TOKEN can now be customized by
  setting gitlab_token_var * PYPI_PASSWORD can now be customized by setting pypi_pass_var *
  PYPI_TOKEN can now be customized by setting pypi_token_var * PYPI_USERNAME can now be customized
  by setting pypi_user_var

* Rewrite Twine adapter for uploading to artifact repositories (`cfb20af`_)

Artifact upload generalised to fully support custom repositories like GitLab. Rewritten to use twine
  python api instead of running the executable. No-op mode now respected by artifact upload.

🪲 Bug Fixes
------------

* Don't use linux commands on windows (`#393`_, `5bcccd2`_)

* Mypy errors in vcs_helpers (`13ca0fe`_)

* Skip removing the build folder if it doesn't exist (`8e79fdc`_)

https://github.com/relekang/python-semantic-release/issues/391#issuecomment-950667599

📖 Documentation
----------------

* Clean typos and add section for repository upload (`1efa18a`_)

Add more details and external links

.. _#392: https://github.com/python-semantic-release/python-semantic-release/pull/392
.. _#393: https://github.com/python-semantic-release/python-semantic-release/pull/393
.. _13ca0fe: https://github.com/python-semantic-release/python-semantic-release/commit/13ca0fe650125be2f5e953f6193fdc4d44d3c75a
.. _1efa18a: https://github.com/python-semantic-release/python-semantic-release/commit/1efa18a3a55134d6bc6e4572ab025e24082476cd
.. _372cda3: https://github.com/python-semantic-release/python-semantic-release/commit/372cda3497f16ead2209e6e1377d38f497144883
.. _5bcccd2: https://github.com/python-semantic-release/python-semantic-release/commit/5bcccd21cc8be3289db260e645fec8dc6a592abd
.. _8e79fdc: https://github.com/python-semantic-release/python-semantic-release/commit/8e79fdc107ffd852a91dfb5473e7bd1dfaba4ee5
.. _cfb20af: https://github.com/python-semantic-release/python-semantic-release/commit/cfb20af79a8e25a77aee9ff72deedcd63cb7f62f


.. _changelog-v7.19.2:

v7.19.2 (2021-09-04)
====================

🪲 Bug Fixes
------------

* Fixed ImproperConfig import error (`#377`_, `b011a95`_)

.. _#377: https://github.com/python-semantic-release/python-semantic-release/pull/377
.. _b011a95: https://github.com/python-semantic-release/python-semantic-release/commit/b011a9595df4240cb190bfb1ab5b6d170e430dfc


.. _changelog-v7.19.1:

v7.19.1 (2021-08-17)
====================

🪲 Bug Fixes
------------

* Add get_formatted_tag helper instead of hardcoded v-prefix in the git tags (`1a354c8`_)

.. _1a354c8: https://github.com/python-semantic-release/python-semantic-release/commit/1a354c86abad77563ebce9a6944256461006f3c7


.. _changelog-v7.19.0:

v7.19.0 (2021-08-16)
====================

✨ Features
-----------

* Custom git tag format support (`#373`_, `1d76632`_)

* feat: custom git tag format support * test: add git tag format check * docs: add tag_format config
  option

📖 Documentation
----------------

* **parser**: Documentation for scipy-parser (`45ee34a`_)

.. _#373: https://github.com/python-semantic-release/python-semantic-release/pull/373
.. _1d76632: https://github.com/python-semantic-release/python-semantic-release/commit/1d76632043bf0b6076d214a63c92013624f4b95e
.. _45ee34a: https://github.com/python-semantic-release/python-semantic-release/commit/45ee34aa21443860a6c2cd44a52da2f353b960bf


.. _changelog-v7.18.0:

v7.18.0 (2021-08-09)
====================

✨ Features
-----------

* Add support for non-prefixed tags (`#366`_, `0fee4dd`_)

📖 Documentation
----------------

* Clarify second argument of ParsedCommit (`086ddc2`_)

.. _#366: https://github.com/python-semantic-release/python-semantic-release/pull/366
.. _086ddc2: https://github.com/python-semantic-release/python-semantic-release/commit/086ddc28f06522453328f5ea94c873bd202ff496
.. _0fee4dd: https://github.com/python-semantic-release/python-semantic-release/commit/0fee4ddb5baaddf85ed6b76e76a04474a5f97d0a


.. _changelog-v7.17.0:

v7.17.0 (2021-08-07)
====================

✨ Features
-----------

* **parser**: Add scipy style parser (`#369`_, `51a3921`_)

.. _#369: https://github.com/python-semantic-release/python-semantic-release/pull/369
.. _51a3921: https://github.com/python-semantic-release/python-semantic-release/commit/51a39213ea120c4bbd7a57b74d4f0cc3103da9f5


.. _changelog-v7.16.4:

v7.16.4 (2021-08-03)
====================

🪲 Bug Fixes
------------

* Correct rendering of gitlab issue references (`07429ec`_)

    resolves #358

.. _07429ec: https://github.com/python-semantic-release/python-semantic-release/commit/07429ec4a32d32069f25ec77b4bea963bd5d2a00


.. _changelog-v7.16.3:

v7.16.3 (2021-07-29)
====================

🪲 Bug Fixes
------------

* Print right info if token is not set (`#360`_, `a275a7a`_) (#361)

Co-authored-by: Laercio Barbosa <laercio.barbosa@scania.com>

.. _#360: https://github.com/python-semantic-release/python-semantic-release/pull/360
.. _a275a7a: https://github.com/python-semantic-release/python-semantic-release/commit/a275a7a17def85ff0b41d254e4ee42772cce1981


.. _changelog-v7.16.2:

v7.16.2 (2021-06-25)
====================

🪲 Bug Fixes
------------

* Use release-api for gitlab (`1ef5cab`_)

📖 Documentation
----------------

* Recommend setting a concurrency group for GitHub Actions (`34b0735`_)

* Update trove classifiers to reflect supported versions (`#344`_, `7578004`_)

.. _#344: https://github.com/python-semantic-release/python-semantic-release/pull/344
.. _1ef5cab: https://github.com/python-semantic-release/python-semantic-release/commit/1ef5caba2d8dd0f2647bc51ede0ef7152d8b7b8d
.. _34b0735: https://github.com/python-semantic-release/python-semantic-release/commit/34b07357ab3f4f4aa787b71183816ec8aaf334a8
.. _7578004: https://github.com/python-semantic-release/python-semantic-release/commit/7578004ed4b20c2bd553782443dfd77535faa377


.. _changelog-v7.16.1:

v7.16.1 (2021-06-08)
====================

🪲 Bug Fixes
------------

* Tomlkit should stay at 0.7.0 (`769a5f3`_)

See https://github.com/relekang/python-semantic-release/pull/339#discussion_r647629387

.. _769a5f3: https://github.com/python-semantic-release/python-semantic-release/commit/769a5f31115cdb1f43f19a23fe72b96a8c8ba0fc


.. _changelog-v7.16.0:

v7.16.0 (2021-06-08)
====================

✨ Features
-----------

* Add option to omit tagging (`#341`_, `20603e5`_)

.. _#341: https://github.com/python-semantic-release/python-semantic-release/pull/341
.. _20603e5: https://github.com/python-semantic-release/python-semantic-release/commit/20603e53116d4f05e822784ce731b42e8cbc5d8f


.. _changelog-v7.15.6:

v7.15.6 (2021-06-08)
====================

🪲 Bug Fixes
------------

* Update click and tomlkit (`#339`_, `947ea3b`_)

.. _#339: https://github.com/python-semantic-release/python-semantic-release/pull/339
.. _947ea3b: https://github.com/python-semantic-release/python-semantic-release/commit/947ea3bc0750735941446cf4a87bae20e750ba12


.. _changelog-v7.15.5:

v7.15.5 (2021-05-26)
====================

🪲 Bug Fixes
------------

* Pin tomlkit to 0.7.0 (`2cd0db4`_)

.. _2cd0db4: https://github.com/python-semantic-release/python-semantic-release/commit/2cd0db4537bb9497b72eb496f6bab003070672ab


.. _changelog-v7.15.4:

v7.15.4 (2021-04-29)
====================

🪲 Bug Fixes
------------

* Change log level of failed toml loading (`24bb079`_)

    Fixes #235

.. _24bb079: https://github.com/python-semantic-release/python-semantic-release/commit/24bb079cbeff12e7043dd35dd0b5ae03192383bb


.. _changelog-v7.15.3:

v7.15.3 (2021-04-03)
====================

🪲 Bug Fixes
------------

* Add venv to path in github action (`583c5a1`_)

.. _583c5a1: https://github.com/python-semantic-release/python-semantic-release/commit/583c5a13e40061fc544b82decfe27a6c34f6d265


.. _changelog-v7.15.2:

v7.15.2 (2021-04-03)
====================

🪲 Bug Fixes
------------

* Run semantic-release in virtualenv in the github action (`b508ea9`_)

    Fixes #331

* Set correct path for venv in action script (`aac02b5`_)

* Use absolute path for venv in github action (`d4823b3`_)

📖 Documentation
----------------

* Clarify that HVCS should be lowercase (`da0ab0c`_)

    Fixes #330

.. _aac02b5: https://github.com/python-semantic-release/python-semantic-release/commit/aac02b5a44a6959328d5879578aa3536bdf856c2
.. _b508ea9: https://github.com/python-semantic-release/python-semantic-release/commit/b508ea9f411c1cd4f722f929aab9f0efc0890448
.. _d4823b3: https://github.com/python-semantic-release/python-semantic-release/commit/d4823b3b6b1fcd5c33b354f814643c9aaf85a06a
.. _da0ab0c: https://github.com/python-semantic-release/python-semantic-release/commit/da0ab0c62c4ce2fa0d815e5558aeec1a1e23bc89


.. _changelog-v7.15.1:

v7.15.1 (2021-03-26)
====================

🪲 Bug Fixes
------------

* Add support for setting build_command to "false" (`520cf1e`_)

    Fixes #328

* Upgrade python-gitlab range (`abfacc4`_)

Keeping both 1.x and 2.x since only change that is breaking is dropping python 3.6 support. I hope
  that leaving the lower limit will make it still work with python 3.6.

Fixes #329

📖 Documentation
----------------

* Add common options to documentation (`20d79a5`_)

These can be found by running `semantic-release --help`, but including them in the documentation
  will be helpful for CI users who don't have the command installed locally.

Related to #327.

.. _20d79a5: https://github.com/python-semantic-release/python-semantic-release/commit/20d79a51bffa26d40607c1b77d10912992279112
.. _520cf1e: https://github.com/python-semantic-release/python-semantic-release/commit/520cf1eaa7816d0364407dbd17b5bc7c79806086
.. _abfacc4: https://github.com/python-semantic-release/python-semantic-release/commit/abfacc432300941d57488842e41c06d885637e6c


.. _changelog-v7.15.0:

v7.15.0 (2021-02-18)
====================

✨ Features
-----------

* Allow the use of .pypirc for twine uploads (`#325`_, `6bc56b8`_)

📖 Documentation
----------------

* Add documentation for releasing on a Jenkins instance (`#324`_, `77ad988`_)

.. _#324: https://github.com/python-semantic-release/python-semantic-release/pull/324
.. _#325: https://github.com/python-semantic-release/python-semantic-release/pull/325
.. _6bc56b8: https://github.com/python-semantic-release/python-semantic-release/commit/6bc56b8aa63069a25a828a2d1a9038ecd09b7d5d
.. _77ad988: https://github.com/python-semantic-release/python-semantic-release/commit/77ad988a2057be59e4559614a234d6871c06ee37


.. _changelog-v7.14.0:

v7.14.0 (2021-02-11)
====================

✨ Features
-----------

* **checks**: Add support for Jenkins CI (`#322`_, `3e99855`_)

Includes a ci check handler to verify jenkins. Unlike other ci systems jenkins doesn't generally
  prefix things with ``JENKINS`` or simply inject ``JENKINS=true`` Really the only thing that is
  immediately identifiable is ``JENKINS_URL``

📖 Documentation
----------------

* Correct casing on proper nouns (`#320`_, `d51b999`_)

* docs: correcting Semantic Versioning casing

Semantic Versioning is the name of the specification. Therefore it is a proper noun. This patch
  corrects the incorrect casing for Semantic Versioning.

* docs: correcting Python casing

This patch corrects the incorrect casing for Python.

.. _#320: https://github.com/python-semantic-release/python-semantic-release/pull/320
.. _#322: https://github.com/python-semantic-release/python-semantic-release/pull/322
.. _3e99855: https://github.com/python-semantic-release/python-semantic-release/commit/3e99855c6bc72b3e9a572c58cc14e82ddeebfff8
.. _d51b999: https://github.com/python-semantic-release/python-semantic-release/commit/d51b999a245a4e56ff7a09d0495c75336f2f150d


.. _changelog-v7.13.2:

v7.13.2 (2021-01-29)
====================

🪲 Bug Fixes
------------

* Fix crash when TOML has no PSR section (`#319`_, `5f8ab99`_)

* fix: crash when TOML has no PSR section

📖 Documentation
----------------

* Fix ``version_toml`` example for Poetry (`#318`_, `39acb68`_)

.. _#318: https://github.com/python-semantic-release/python-semantic-release/pull/318
.. _#319: https://github.com/python-semantic-release/python-semantic-release/pull/319
.. _39acb68: https://github.com/python-semantic-release/python-semantic-release/commit/39acb68bfffe8242040e476893639ba26fa0d6b5
.. _5f8ab99: https://github.com/python-semantic-release/python-semantic-release/commit/5f8ab99bf7254508f4b38fcddef2bdde8dd15a4c


.. _changelog-v7.13.1:

v7.13.1 (2021-01-26)
====================

🪲 Bug Fixes
------------

* Use multiline version_pattern match in replace (`#315`_, `1a85af4`_)

    Fixes #306

.. _#315: https://github.com/python-semantic-release/python-semantic-release/pull/315
.. _1a85af4: https://github.com/python-semantic-release/python-semantic-release/commit/1a85af434325ce52e11b49895e115f7a936e417e


.. _changelog-v7.13.0:

v7.13.0 (2021-01-26)
====================

✨ Features
-----------

* Support toml files for version declaration (`#307`_, `9b62a7e`_)

This introduce a new ``version_toml`` configuration property that behaves like ``version_pattern``
  and `version_variable`.

For poetry support, user should now set `version_toml = pyproject.toml:tool.poetry.version`.

This introduce an ABC class, `VersionDeclaration`, that can be implemented to add other version
  declarations with ease.

``toml`` dependency has been replaced by `tomlkit`, as this is used the library used by poetry to
  generate the ``pyproject.toml`` file, and is able to keep the ordering of data defined in the
  file.

Existing ``VersionPattern`` class has been renamed to ``PatternVersionDeclaration`` and now
  implements `VersionDeclaration`.

``load_version_patterns()`` function has been renamed to ``load_version_declarations()`` and now
  return a list of ``VersionDeclaration`` implementations.

Close #245 Close #275

.. _#307: https://github.com/python-semantic-release/python-semantic-release/pull/307
.. _9b62a7e: https://github.com/python-semantic-release/python-semantic-release/commit/9b62a7e377378667e716384684a47cdf392093fa


.. _changelog-v7.12.0:

v7.12.0 (2021-01-25)
====================

✨ Features
-----------

* **github**: Retry GitHub API requests on failure (`#314`_, `ac241ed`_)

* fix(github): add retries to github API requests

📖 Documentation
----------------

* **actions**: Pat must be passed to checkout step too (`e2d8e47`_)

    Fixes #311

.. _#314: https://github.com/python-semantic-release/python-semantic-release/pull/314
.. _ac241ed: https://github.com/python-semantic-release/python-semantic-release/commit/ac241edf4de39f4fc0ff561a749fa85caaf9e2ae
.. _e2d8e47: https://github.com/python-semantic-release/python-semantic-release/commit/e2d8e47d2b02860881381318dcc088e150c0fcde


.. _changelog-v7.11.0:

v7.11.0 (2021-01-08)
====================

✨ Features
-----------

* **print-version**: Add print-version command to output version (`512e3d9`_)

This new command can be integrated in the build process before the effective release, ie. to rename
  some files with the version number.

Users may invoke ``VERSION=$(semantic-release print-version)`` to retrieve the version that will be
  generated during the release before it really occurs.

🪲 Bug Fixes
------------

* Add dot to --define option help (`eb4107d`_)

* Avoid Unknown bump level 0 message (`8ab624c`_)

This issue occurs when some commits are available but are all to level 0.

* **actions**: Fix github actions with new main location (`6666672`_)

⚙️ Build System
----------------

* Add __main__.py magic file (`e93f36a`_)

This file allow to run the package from sources properly with `python -m semantic_release`.

.. _512e3d9: https://github.com/python-semantic-release/python-semantic-release/commit/512e3d92706055bdf8d08b7c82927d3530183079
.. _6666672: https://github.com/python-semantic-release/python-semantic-release/commit/6666672d3d97ab7cdf47badfa3663f1a69c2dbdf
.. _8ab624c: https://github.com/python-semantic-release/python-semantic-release/commit/8ab624cf3508b57a9656a0a212bfee59379d6f8b
.. _e93f36a: https://github.com/python-semantic-release/python-semantic-release/commit/e93f36a7a10e48afb42c1dc3d860a5e2a07cf353
.. _eb4107d: https://github.com/python-semantic-release/python-semantic-release/commit/eb4107d2efdf8c885c8ae35f48f1b908d1fced32


.. _changelog-v7.10.0:

v7.10.0 (2021-01-08)
====================

✨ Features
-----------

* **build**: Allow falsy values for build_command to disable build step (`c07a440`_)

📖 Documentation
----------------

* Fix incorrect reference syntax (`42027f0`_)

* Rewrite getting started page (`97a9046`_)

.. _42027f0: https://github.com/python-semantic-release/python-semantic-release/commit/42027f0d2bb64f4c9eaec65112bf7b6f67568e60
.. _97a9046: https://github.com/python-semantic-release/python-semantic-release/commit/97a90463872502d1207890ae1d9dd008b1834385
.. _c07a440: https://github.com/python-semantic-release/python-semantic-release/commit/c07a440f2dfc45a2ad8f7c454aaac180c4651f70


.. _changelog-v7.9.0:

v7.9.0 (2020-12-21)
===================

✨ Features
-----------

* **hvcs**: Add hvcs_domain config option (`ab3061a`_)

While Gitlab already has an env var that should provide the vanity URL, this supports a generic
  'hvcs_domain' parameter that makes the hostname configurable for both GHE and Gitlab.

This will also use the configured hostname (from either source) in the changelog links

Fixes: #277

🪲 Bug Fixes
------------

* **history**: Coerce version to string (`#298`_, `d4cdc3d`_)

The changes in #297 mistakenly omitted coercing the return value to a string. This resulted in
  errors like: "can only concatenate str (not "VersionInfo") to str"

Add test case asserting it's type str

* **history**: Require semver >= 2.10 (`5087e54`_)

This resolves deprecation warnings, and updates this to a more 3.x compatible syntax

.. _#298: https://github.com/python-semantic-release/python-semantic-release/pull/298
.. _5087e54: https://github.com/python-semantic-release/python-semantic-release/commit/5087e549399648cf2e23339a037b33ca8b62d954
.. _ab3061a: https://github.com/python-semantic-release/python-semantic-release/commit/ab3061ae93c49d71afca043b67b361e2eb2919e6
.. _d4cdc3d: https://github.com/python-semantic-release/python-semantic-release/commit/d4cdc3d3cd2d93f2a78f485e3ea107ac816c7d00


.. _changelog-v7.8.2:

v7.8.2 (2020-12-19)
===================

✨ Features
-----------

* **repository**: Add to settings artifact repository (`f4ef373`_)

- Add new config var to set repository (repository_url) - Remove 'Pypi' word when it refers
  generically to an artifact repository system - Depreciate 'PYPI_USERNAME' and 'PYPI_PASSWORD' and
  prefer 'REPOSITORY_USERNAME' and 'REPOSITORY_PASSWORD' env vars - Depreciate every config key with
  'pypi' and prefer repository - Update doc in accordance with those changes

🪲 Bug Fixes
------------

* **cli**: Skip remove_dist where not needed (`04817d4`_)

Skip removing dist files when upload_pypi or upload_release are not set

.. _04817d4: https://github.com/python-semantic-release/python-semantic-release/commit/04817d4ecfc693195e28c80455bfbb127485f36b
.. _f4ef373: https://github.com/python-semantic-release/python-semantic-release/commit/f4ef3733b948282fba5a832c5c0af134609b26d2


.. _changelog-v7.8.1:

v7.8.1 (2020-12-18)
===================

🪲 Bug Fixes
------------

* Filenames with unknown mimetype are now properly uploaded to github release (`f3ece78`_)

When mimetype can't be guessed, content-type header is set to None. But it's mandatory for the file
  upload to work properly. In this case, application/octect-stream is now used as a fallback.

* **logs**: Fix TypeError when enabling debug logs (`2591a94`_)

Some logger invocation were raising the following error: TypeError: not all arguments converted
  during string formatting.

This also refactor some other parts to use f-strings as much as possible.

.. _2591a94: https://github.com/python-semantic-release/python-semantic-release/commit/2591a94115114c4a91a48f5b10b3954f6ac932a1
.. _f3ece78: https://github.com/python-semantic-release/python-semantic-release/commit/f3ece78b2913e70f6b99907b192a1e92bbfd6b77


.. _changelog-v7.8.0:

v7.8.0 (2020-12-18)
===================

✨ Features
-----------

* Add ``upload_to_pypi_glob_patterns`` option (`42305ed`_)

🪲 Bug Fixes
------------

* **changelog**: Use "issues" link vs "pull" (`93e48c9`_)

While, e.g., https://github.com/owner/repos/pull/123 will work,
  https://github.com/owner/repos/issues/123 should be safer / more consistent, and should avoid a
  failure if someone adds an issue link at the end of a PR that is merged via rebase merge or merge
  commit.

* **netrc**: Prefer using token defined in GH_TOKEN instead of .netrc file (`3af32a7`_)

.netrc file will only be used when available and no GH_TOKEN environment variable is defined.

This also add a test to make sure .netrc is used properly when no GH_TOKEN is defined.

.. _3af32a7: https://github.com/python-semantic-release/python-semantic-release/commit/3af32a738f2f2841fd75ec961a8f49a0b1c387cf
.. _42305ed: https://github.com/python-semantic-release/python-semantic-release/commit/42305ed499ca08c819c4e7e65fcfbae913b8e6e1
.. _93e48c9: https://github.com/python-semantic-release/python-semantic-release/commit/93e48c992cb8b763f430ecbb0b7f9c3ca00036e4


.. _changelog-v7.7.0:

v7.7.0 (2020-12-12)
===================

✨ Features
-----------

* **changelog**: Add PR links in markdown (`#282`_, `0448f6c`_)

GitHub release notes automagically link to the PR, but changelog markdown doesn't. Replace a PR
  number at the end of a message with a markdown link.

.. _#282: https://github.com/python-semantic-release/python-semantic-release/pull/282
.. _0448f6c: https://github.com/python-semantic-release/python-semantic-release/commit/0448f6c350bbbf239a81fe13dc5f45761efa7673


.. _changelog-v7.6.0:

v7.6.0 (2020-12-06)
===================

✨ Features
-----------

* Add ``major_on_zero`` option (`d324154`_)

To control if bump major or not when current major version is zero.

📖 Documentation
----------------

* Add documentation for option ``major_on_zero`` (`2e8b26e`_)

.. _2e8b26e: https://github.com/python-semantic-release/python-semantic-release/commit/2e8b26e4ee0316a2cf2a93c09c783024fcd6b3ba
.. _d324154: https://github.com/python-semantic-release/python-semantic-release/commit/d3241540e7640af911eb24c71e66468feebb0d46


.. _changelog-v7.5.0:

v7.5.0 (2020-12-04)
===================

✨ Features
-----------

* **logs**: Include scope in changelogs (`#281`_, `21c96b6`_)

When the scope is set, include it in changelogs, e.g. "feat(x): some description" becomes "**x**:
  some description". This is similar to how the Node semantic release (and
  conventional-changelog-generator) generates changelogs. If scope is not given, it's omitted.

Add a new config parameter changelog_scope to disable this behavior when set to 'False'

.. _#281: https://github.com/python-semantic-release/python-semantic-release/pull/281
.. _21c96b6: https://github.com/python-semantic-release/python-semantic-release/commit/21c96b688cc44cc6f45af962ffe6d1f759783f37


.. _changelog-v7.4.1:

v7.4.1 (2020-12-04)
===================

🪲 Bug Fixes
------------

* Add "changelog_capitalize" to flags (`#279`_, `37716df`_)

    Fixes #278 (or so I hope).

.. _#279: https://github.com/python-semantic-release/python-semantic-release/pull/279
.. _37716df: https://github.com/python-semantic-release/python-semantic-release/commit/37716dfa78eb3f848f57a5100d01d93f5aafc0bf


.. _changelog-v7.4.0:

v7.4.0 (2020-11-24)
===================

✨ Features
-----------

* Add changelog_capitalize configuration (`7cacca1`_)

    Fixes #260

📖 Documentation
----------------

* Fix broken internal references (`#270`_, `da20b9b`_)

* Update links to Github docs (`#268`_, `c53162e`_)

.. _#268: https://github.com/python-semantic-release/python-semantic-release/pull/268
.. _#270: https://github.com/python-semantic-release/python-semantic-release/pull/270
.. _7cacca1: https://github.com/python-semantic-release/python-semantic-release/commit/7cacca1eb436a7166ba8faf643b53c42bc32a6a7
.. _c53162e: https://github.com/python-semantic-release/python-semantic-release/commit/c53162e366304082a3bd5d143b0401da6a16a263
.. _da20b9b: https://github.com/python-semantic-release/python-semantic-release/commit/da20b9bdd3c7c87809c25ccb2a5993a7ea209a22


.. _changelog-v7.3.0:

v7.3.0 (2020-09-28)
===================

✨ Features
-----------

* Generate ``changelog.md`` file (`#266`_, `2587dfe`_)

📖 Documentation
----------------

* Fix docstring (`5a5e2cf`_)

Stumbled upon this docstring which first line seems copy/pasted from the method above.

.. _#266: https://github.com/python-semantic-release/python-semantic-release/pull/266
.. _2587dfe: https://github.com/python-semantic-release/python-semantic-release/commit/2587dfed71338ec6c816f58cdf0882382c533598
.. _5a5e2cf: https://github.com/python-semantic-release/python-semantic-release/commit/5a5e2cfb5e6653fb2e95e6e23e56559953b2c2b4


.. _changelog-v7.2.5:

v7.2.5 (2020-09-16)
===================

🪲 Bug Fixes
------------

* Add required to inputs in action metadata (`#264`_, `e76b255`_)

According to the documentation, ``inputs.<input_id>.required`` is a required field.

.. _#264: https://github.com/python-semantic-release/python-semantic-release/pull/264
.. _e76b255: https://github.com/python-semantic-release/python-semantic-release/commit/e76b255cf7d3d156e3314fc28c54d63fa126e973


.. _changelog-v7.2.4:

v7.2.4 (2020-09-14)
===================

🪲 Bug Fixes
------------

* Use range for toml dependency (`45707e1`_)

    Fixes #241

.. _45707e1: https://github.com/python-semantic-release/python-semantic-release/commit/45707e1b7dcab48103a33de9d7f9fdb5a34dae4a


.. _changelog-v7.2.3:

v7.2.3 (2020-09-12)
===================

🪲 Bug Fixes
------------

* Support multiline version_pattern matching by default (`82f7849`_)

📖 Documentation
----------------

* Create 'getting started' instructions (`#256`_, `5f4d000`_)

* Link to getting started guide in README (`f490e01`_)

.. _#256: https://github.com/python-semantic-release/python-semantic-release/pull/256
.. _5f4d000: https://github.com/python-semantic-release/python-semantic-release/commit/5f4d000c3f153d1d23128acf577e389ae879466e
.. _82f7849: https://github.com/python-semantic-release/python-semantic-release/commit/82f7849dcf29ba658e0cb3b5d21369af8bf3c16f
.. _f490e01: https://github.com/python-semantic-release/python-semantic-release/commit/f490e0194fa818db4d38c185bc5e6245bfde546b


.. _changelog-v7.2.2:

v7.2.2 (2020-07-26)
===================

🪲 Bug Fixes
------------

* **changelog**: Send changelog to stdout (`87e2bb8`_)

    Fixes #250

📖 Documentation
----------------

* Add quotation marks to the pip commands in CONTRIBUTING.rst (`#253`_, `e20fa43`_)

.. _#253: https://github.com/python-semantic-release/python-semantic-release/pull/253
.. _87e2bb8: https://github.com/python-semantic-release/python-semantic-release/commit/87e2bb881387ff3ac245ab9923347a5a616e197b
.. _e20fa43: https://github.com/python-semantic-release/python-semantic-release/commit/e20fa43098c06f5f585c81b9cd7e287dcce3fb5d


.. _changelog-v7.2.1:

v7.2.1 (2020-06-29)
===================

🪲 Bug Fixes
------------

* Commit all files with bumped versions (`#249`_, `b3a1766`_)

📖 Documentation
----------------

* Give example of multiple build commands (`#248`_, `65f1ffc`_)

I had a little trouble figuring out how to use a non-setup.py build command, so I thought it would
  be helpful to update the docs with an example of how to do this.

.. _#248: https://github.com/python-semantic-release/python-semantic-release/pull/248
.. _#249: https://github.com/python-semantic-release/python-semantic-release/pull/249
.. _65f1ffc: https://github.com/python-semantic-release/python-semantic-release/commit/65f1ffcc6cac3bf382f4b821ff2be59d04f9f867
.. _b3a1766: https://github.com/python-semantic-release/python-semantic-release/commit/b3a1766be7edb7d2eb76f2726d35ab8298688b3b


.. _changelog-v7.2.0:

v7.2.0 (2020-06-15)
===================

✨ Features
-----------

* Bump versions in multiple files (`#246`_, `0ba2c47`_)

- Add the ``version_pattern`` setting, which allows version numbers to be identified using arbitrary
  regular expressions. - Refactor the config system to allow non-string data types to be specified
  in `pyproject.toml`. - Multiple files can now be specified by setting ``version_variable`` or
  ``version_pattern`` to a list in `pyproject.toml`.

Fixes #175

.. _#246: https://github.com/python-semantic-release/python-semantic-release/pull/246
.. _0ba2c47: https://github.com/python-semantic-release/python-semantic-release/commit/0ba2c473c6e44cc326b3299b6ea3ddde833bdb37


.. _changelog-v7.1.1:

v7.1.1 (2020-05-28)
===================

🪲 Bug Fixes
------------

* **changelog**: Swap sha and message in table changelog (`6741370`_)

.. _6741370: https://github.com/python-semantic-release/python-semantic-release/commit/6741370ab09b1706ff6e19b9fbe57b4bddefc70d


.. _changelog-v7.1.0:

v7.1.0 (2020-05-24)
===================

✨ Features
-----------

* **changelog**: Add changelog_table component (`#242`_, `fe6a7e7`_)

Add an alternative changelog component which displays each section as a row in a table.

Fixes #237

.. _#242: https://github.com/python-semantic-release/python-semantic-release/pull/242
.. _fe6a7e7: https://github.com/python-semantic-release/python-semantic-release/commit/fe6a7e7fa014ffb827a1430dbcc10d1fc84c886b


.. _changelog-v7.0.0:

v7.0.0 (2020-05-22)
===================

💥 Breaking
-----------

* **changelog**: Add changelog components (`#240`_, `3e17a98`_)

* feat(changelog): add changelog components

Add the ability to configure sections of the changelog using a ``changelog_components`` option.
  Component outputs are separated by a blank line and appear in the same order as they were
  configured.

It is possible to create your own custom components. Each component is a function which returns
  either some text to be added, or None in which case it will be skipped.

BREAKING CHANGE: The ``compare_url`` option has been removed in favor of using
  `changelog_components`. This functionality is now available as the
  ``semantic_release.changelog.compare_url`` component.

* docs: add documentation for changelog_components

* feat: pass changelog_sections to components

Changelog components may now receive the value of `changelog_sections`, split and ready to use.

📖 Documentation
----------------

* Add conda-forge badge (`e9536bb`_)

💥 BREAKING CHANGES
-------------------

* **changelog**: The `compare_url` option has been removed in favor of using `changelog_components`.
  This functionality is now available as the `semantic_release.changelog.compare_url` component.

.. _#240: https://github.com/python-semantic-release/python-semantic-release/pull/240
.. _3e17a98: https://github.com/python-semantic-release/python-semantic-release/commit/3e17a98d7fa8468868a87e62651ac2c010067711
.. _e9536bb: https://github.com/python-semantic-release/python-semantic-release/commit/e9536bbe119c9e3b90c61130c02468e0e1f14141


.. _changelog-v6.4.1:

v6.4.1 (2020-05-15)
===================

🪲 Bug Fixes
------------

* Convert \r\n to \n in commit messages (`34acbbc`_)

    Fixes #239

.. _34acbbc: https://github.com/python-semantic-release/python-semantic-release/commit/34acbbcd25320a9d18dcd1a4f43e1ce1837b2c9f


.. _changelog-v6.4.0:

v6.4.0 (2020-05-15)
===================

💥 Breaking
-----------

* **history**: Create emoji parser (`#238`_, `2e1c50a`_)

Add a commit parser which uses emojis from https://gitmoji.carloscuesta.me/ to determine the type of
  change.

* fix: add emojis to default changelog_sections

* fix: include all parsed types in changelog

This allows emojis to appear in the changelog, as well as configuring other types to appear with the
  Angular parser (I remember someone asking for that feature a while ago). All filtering is now done
  in the markdown_changelog function.

* refactor(history): get breaking changes in parser

Move the task of detecting breaking change descriptions into the commit parser function, instead of
  during changelog generation.

This has allowed the emoji parser to also return the regular descriptions as breaking change
  descriptions for commits with :boom:.

BREAKING CHANGE: Custom commit parser functions are now required to pass a fifth argument to
  `ParsedCommit`, which is a list of breaking change descriptions.

* docs: add documentation for emoji parser

💥 BREAKING CHANGES
-------------------

* **history**: Custom commit parser functions are now required to pass a fifth argument to
  `ParsedCommit`, which is a list of breaking change descriptions.

.. _#238: https://github.com/python-semantic-release/python-semantic-release/pull/238
.. _2e1c50a: https://github.com/python-semantic-release/python-semantic-release/commit/2e1c50a865628b372f48945a039a3edb38a7cdf0


.. _changelog-v6.3.1:

v6.3.1 (2020-05-11)
===================

🪲 Bug Fixes
------------

* Use getboolean for commit_version_number (`a60e0b4`_)

    Fixes #186

.. _a60e0b4: https://github.com/python-semantic-release/python-semantic-release/commit/a60e0b4e3cadf310c3e0ad67ebeb4e69d0ee50cb


.. _changelog-v6.3.0:

v6.3.0 (2020-05-09)
===================

✨ Features
-----------

* **history**: Support linking compare page in changelog (`79a8e02`_)

    Fixes #218

📖 Documentation
----------------

* Document compare_link option (`e52c355`_)

* Rewrite commit-log-parsing.rst (`4c70f4f`_)

.. _4c70f4f: https://github.com/python-semantic-release/python-semantic-release/commit/4c70f4f2aa3343c966d1b7ab8566fcc782242ab9
.. _79a8e02: https://github.com/python-semantic-release/python-semantic-release/commit/79a8e02df82fbc2acecaad9e9ff7368e61df3e54
.. _e52c355: https://github.com/python-semantic-release/python-semantic-release/commit/e52c355c0d742ddd2cfa65d42888296942e5bec5


.. _changelog-v6.2.0:

v6.2.0 (2020-05-02)
===================

✨ Features
-----------

* **history**: Check all paragraphs for breaking changes (`fec08f0`_)

Check each paragraph of the commit's description for breaking changes, instead of only a body and
  footer. This ensures that breaking changes are detected when squashing commits together.

Fixes #200

📖 Documentation
----------------

* Add = to verbosity option (`a0f4c9c`_)

    Fixes #227

* Use references where possible (`f38e5d4`_)

    Fixes #221

.. _a0f4c9c: https://github.com/python-semantic-release/python-semantic-release/commit/a0f4c9cd397fcb98f880097319c08160adb3c3e6
.. _f38e5d4: https://github.com/python-semantic-release/python-semantic-release/commit/f38e5d4a1597cddb69ce47a4d79b8774e796bf41
.. _fec08f0: https://github.com/python-semantic-release/python-semantic-release/commit/fec08f0dbd7ae15f95ca9c41a02c9fe6d448ede0


.. _changelog-v6.1.0:

v6.1.0 (2020-04-26)
===================

✨ Features
-----------

* **actions**: Support PYPI_TOKEN on GitHub Actions (`df2c080`_)

Add support for the new PYPI_TOKEN environment variable to be used on GitHub Actions.

* **pypi**: Support easier use of API tokens (`bac135c`_)

Allow setting the environment variable PYPI_TOKEN to automatically fill the username as __token__.

Fixes #213

📖 Documentation
----------------

* Add documentation for PYPI_TOKEN (`a8263a0`_)

.. _a8263a0: https://github.com/python-semantic-release/python-semantic-release/commit/a8263a066177d1d42f2844e4cb42a76a23588500
.. _bac135c: https://github.com/python-semantic-release/python-semantic-release/commit/bac135c0ae7a6053ecfc7cdf2942c3c89640debf
.. _df2c080: https://github.com/python-semantic-release/python-semantic-release/commit/df2c0806f0a92186e914cfc8cc992171d74422df


.. _changelog-v6.0.1:

v6.0.1 (2020-04-15)
===================

🪲 Bug Fixes
------------

* **hvcs**: Convert get_hvcs to use LoggedFunction (`3084249`_)

This was missed in 213530fb0c914e274b81d1dacf38ea7322b5b91f

.. _3084249: https://github.com/python-semantic-release/python-semantic-release/commit/308424933fd3375ca3730d9eaf8abbad2435830b


.. _changelog-v6.0.0:

v6.0.0 (2020-04-15)
===================

💥 Breaking
-----------

* **debug**: Use logging and click_log instead of ndebug (`15b1f65`_)

BREAKING CHANGE: ``DEBUG="*"`` no longer has an effect, instead use `--verbosity DEBUG`.

📖 Documentation
----------------

* Create Read the Docs config file (`aa5a1b7`_)

* Include README.rst in index.rst (`8673a9d`_)

These files were very similar so it makes sense to simply include one inside the other.

* Move action.rst into main documentation (`509ccaf`_)

* Rewrite README.rst (`e049772`_)

* Rewrite troubleshooting page (`0285de2`_)

💥 BREAKING CHANGES
-------------------

* **debug**: `debug="*"` no longer has an effect, instead use  `--verbosity DEBUG`.

.. _0285de2: https://github.com/python-semantic-release/python-semantic-release/commit/0285de215a8dac3fcc9a51f555fa45d476a56dff
.. _15b1f65: https://github.com/python-semantic-release/python-semantic-release/commit/15b1f650f29761e1ab2a91b767cbff79b2057a4c
.. _509ccaf: https://github.com/python-semantic-release/python-semantic-release/commit/509ccaf307a0998eced69ad9fee1807132babe28
.. _8673a9d: https://github.com/python-semantic-release/python-semantic-release/commit/8673a9d92a9bf348bb3409e002a830741396c8ca
.. _aa5a1b7: https://github.com/python-semantic-release/python-semantic-release/commit/aa5a1b700a1c461c81c6434686cb6f0504c4bece
.. _e049772: https://github.com/python-semantic-release/python-semantic-release/commit/e049772cf14cdd49538cf357db467f0bf3fe9587


.. _changelog-v5.2.0:

v5.2.0 (2020-04-09)
===================

✨ Features
-----------

* **github**: Add tag as default release name (`2997908`_)

📖 Documentation
----------------

* Automate API docs (`7d4fea2`_)

Automatically create pages in the API docs section using sphinx-autodoc. This is added as an event
  handler in conf.py.

.. _2997908: https://github.com/python-semantic-release/python-semantic-release/commit/2997908f80f4fcec56917d237a079b961a06f990
.. _7d4fea2: https://github.com/python-semantic-release/python-semantic-release/commit/7d4fea266cc75007de51609131eb6d1e324da608


.. _changelog-v5.1.0:

v5.1.0 (2020-04-04)
===================

✨ Features
-----------

* **history**: Allow customizing changelog_sections (`#207`_, `d5803d5`_)

📖 Documentation
----------------

* Improve formatting of configuration page (`9a8e22e`_)

* Improve formatting of envvars page (`b376a56`_)

* Update index.rst (`b27c26c`_)

.. _#207: https://github.com/python-semantic-release/python-semantic-release/pull/207
.. _9a8e22e: https://github.com/python-semantic-release/python-semantic-release/commit/9a8e22e838d7dbf3bfd941397c3b39560aca6451
.. _b27c26c: https://github.com/python-semantic-release/python-semantic-release/commit/b27c26c66e7e41843ab29076f7e724908091b46e
.. _b376a56: https://github.com/python-semantic-release/python-semantic-release/commit/b376a567bfd407a507ce0752614b0ca75a0f2973
.. _d5803d5: https://github.com/python-semantic-release/python-semantic-release/commit/d5803d5c1668d86482a31ac0853bac7ecfdc63bc


.. _changelog-v5.0.3:

v5.0.3 (2020-03-26)
===================

🪲 Bug Fixes
------------

* Bump dependencies and fix Windows issues on Development (`#173`_, `0a6f8c3`_)

* Bump dependencies and fix windows issues

* Correctly pass temp dir to test settings

* Remove print call on test settings

* fix: missing mime types on Windows

.. _#173: https://github.com/python-semantic-release/python-semantic-release/pull/173
.. _0a6f8c3: https://github.com/python-semantic-release/python-semantic-release/commit/0a6f8c3842b05f5f424dad5ce1fa5e3823c7e688


.. _changelog-v5.0.2:

v5.0.2 (2020-03-22)
===================

🪲 Bug Fixes
------------

* **history**: Leave case of other characters unchanged (`96ba94c`_)

Previously, use of str.capitalize() would capitalize the first letter as expected, but all
  subsequent letters became lowercase. Now, the other letters remain unchanged.

.. _96ba94c: https://github.com/python-semantic-release/python-semantic-release/commit/96ba94c4b4593997343ec61ecb6c823c1494d0e2


.. _changelog-v5.0.1:

v5.0.1 (2020-03-22)
===================

🪲 Bug Fixes
------------

* Make action use current version of semantic-release (`123984d`_)

This gives two benefits: * In this repo it will work as a smoketest * In other repos when they
  specify version int the github workflow they will get the version they specify.

.. _123984d: https://github.com/python-semantic-release/python-semantic-release/commit/123984d735181c622f3d99088a1ad91321192a11


.. _changelog-v5.0.0:

v5.0.0 (2020-03-22)
===================

💥 Breaking
-----------

* **build**: Allow config setting for build command (`#195`_, `740f4bd`_)

* feat(build): allow config setting for build command

BREAKING CHANGE: Previously the build_commands configuration variable set the types of bundles sent
  to `python setup.py`. It has been replaced by the configuration variable ``build_command`` which
  takes the full command e.g. ``python setup.py sdist`` or `poetry build`.

Closes #188

🪲 Bug Fixes
------------

* Rename default of build_command config (`d5db22f`_)

📖 Documentation
----------------

* **pypi**: Update docstings in pypi.py (`6502d44`_)

💥 BREAKING CHANGES
-------------------

* **build**: Previously the build_commands configuration variable set the types of bundles sent to
  `python setup.py`. It has been replaced by the configuration variable `build_command` which takes
  the full command e.g. `python setup.py sdist` or `poetry build`.

.. _#195: https://github.com/python-semantic-release/python-semantic-release/pull/195
.. _6502d44: https://github.com/python-semantic-release/python-semantic-release/commit/6502d448fa65e5dc100e32595e83fff6f62a881a
.. _740f4bd: https://github.com/python-semantic-release/python-semantic-release/commit/740f4bdb26569362acfc80f7e862fc2c750a46dd
.. _d5db22f: https://github.com/python-semantic-release/python-semantic-release/commit/d5db22f9f7acd05d20fd60a8b4b5a35d4bbfabb8


.. _changelog-v4.11.0:

v4.11.0 (2020-03-22)
====================

✨ Features
-----------

* **actions**: Create GitHub Action (`350245d`_)

📖 Documentation
----------------

* Make AUTHORS.rst dynamic (`db2e076`_)

* **readme**: Fix minor typo (`c22f69f`_)

.. _350245d: https://github.com/python-semantic-release/python-semantic-release/commit/350245dbfb07ed6a1db017b1d9d1072b368b1497
.. _c22f69f: https://github.com/python-semantic-release/python-semantic-release/commit/c22f69f62a215ff65e1ab6dcaa8e7e9662692e64
.. _db2e076: https://github.com/python-semantic-release/python-semantic-release/commit/db2e0762f3189d0f1a6ba29aad32bdefb7e0187f


.. _changelog-v4.10.0:

v4.10.0 (2020-03-03)
====================

✨ Features
-----------

* Make commit message configurable (`#184`_, `eb0762c`_)

.. _#184: https://github.com/python-semantic-release/python-semantic-release/pull/184
.. _eb0762c: https://github.com/python-semantic-release/python-semantic-release/commit/eb0762ca9fea5cecd5c7b182504912a629be473b


.. _changelog-v4.9.0:

v4.9.0 (2020-03-02)
===================

✨ Features
-----------

* **pypi**: Add build_commands config (`22146ea`_)

Add a config option to set the commands passed to setup.py when building distributions. This allows
  for things like adding custom commands to the build process.

🪲 Bug Fixes
------------

* **pypi**: Change bdist_wheels to bdist_wheel (`c4db509`_)

Change the incorrect command bdist_wheels to bdist_wheel.

.. _22146ea: https://github.com/python-semantic-release/python-semantic-release/commit/22146ea4b94466a90d60b94db4cc65f46da19197
.. _c4db509: https://github.com/python-semantic-release/python-semantic-release/commit/c4db50926c03f3d551c8331932c567c7bdaf4f3d


.. _changelog-v4.8.0:

v4.8.0 (2020-02-28)
===================

✨ Features
-----------

* **git**: Add a new config for commit author (`aa2c22c`_)

.. _aa2c22c: https://github.com/python-semantic-release/python-semantic-release/commit/aa2c22c469448fe57f02bea67a02f998ce519ac3


.. _changelog-v4.7.1:

v4.7.1 (2020-02-28)
===================

🪲 Bug Fixes
------------

* Repair parsing of remotes in the gitlab ci format (`0fddbe2`_)

Format is: "https://gitlab-ci-token:MySuperToken@gitlab.example.com/group/project.git"

Problem was due to the regex modification for #179

Fixes #181

.. _0fddbe2: https://github.com/python-semantic-release/python-semantic-release/commit/0fddbe2fb70d24c09ceddb789a159162a45942dc


.. _changelog-v4.7.0:

v4.7.0 (2020-02-28)
===================

✨ Features
-----------

* Upload distribution files to GitHub Releases (`#177`_, `e427658`_)

* feat(github): upload dists to release

Upload Python wheels to the GitHub release. Configured with the option upload_to_release, on by
  default if using GitHub.

* docs: document upload_to_release config option

* fix(github): fix upload of .whl files

Fix uploading of .whl files due to a missing MIME type (defined custom type as
  application/x-wheel+zip). Additionally, continue with other uploads even if one fails.

* refactor(github): move api calls to separate methods

Move each type of GitHub API request into its own method to improve readability.

Re-implementation of #172

* fix: post changelog after PyPI upload

Post the changelog in-between uploading to PyPI and uploading to GitHub Releases. This is so that if
  the PyPI upload fails, GitHub users will not be notified. GitHub uploads still need to be
  processed after creating the changelog as the release notes must be published to upload assets to
  them.

🪲 Bug Fixes
------------

* Support repository owner names containing dots (`a6c4da4`_)

    Fixes #179

* **github**: Use application/octet-stream for .whl files (`90a7e47`_)

application/octet-stream is more generic, but it is better than using a non-official MIME type.

.. _#177: https://github.com/python-semantic-release/python-semantic-release/pull/177
.. _90a7e47: https://github.com/python-semantic-release/python-semantic-release/commit/90a7e476a04d26babc88002e9035cad2ed485b07
.. _a6c4da4: https://github.com/python-semantic-release/python-semantic-release/commit/a6c4da4c0e6bd8a37f64544f7813fa027f5054ed
.. _e427658: https://github.com/python-semantic-release/python-semantic-release/commit/e427658e33abf518191498c3142a0f18d3150e07


.. _changelog-v4.6.0:

v4.6.0 (2020-02-19)
===================

✨ Features
-----------

* **history**: Capitalize changelog messages (`1a8e306`_)

Capitalize the first letter of messages in the changelog regardless of whether they are capitalized
  in the commit itself.

🪲 Bug Fixes
------------

* Add more debug statements in logs (`bc931ec`_)

* Only overwrite with patch if bump is None (`1daa4e2`_)

    Fixes #159

.. _1a8e306: https://github.com/python-semantic-release/python-semantic-release/commit/1a8e3060b8f6d6362c27903dcfc69d17db5f1d36
.. _1daa4e2: https://github.com/python-semantic-release/python-semantic-release/commit/1daa4e23ec2dd40c6b490849276524264787e24e
.. _bc931ec: https://github.com/python-semantic-release/python-semantic-release/commit/bc931ec46795fde4c1ccee004eec83bf73d5de7a


.. _changelog-v4.5.1:

v4.5.1 (2020-02-16)
===================

🪲 Bug Fixes
------------

* **github**: Send token in request header (`be9972a`_)

Use an Authorization header instead of deprecated query parameter authorization.

Fixes relekang/python-semantic-release#167

📖 Documentation
----------------

* Add note about automatic releases in readme (`e606e75`_)

* Fix broken list in readme (`7aa572b`_)

Fix the syntax of a broken bullet-point list in README.rst.

* Update readme and getting started docs (`07b3208`_)

.. _07b3208: https://github.com/python-semantic-release/python-semantic-release/commit/07b3208ff64301e544c4fdcb48314e49078fc479
.. _7aa572b: https://github.com/python-semantic-release/python-semantic-release/commit/7aa572b2a323ddbc69686309226395f40c52b469
.. _be9972a: https://github.com/python-semantic-release/python-semantic-release/commit/be9972a7b1fb183f738fb31bd370adb30281e4d5
.. _e606e75: https://github.com/python-semantic-release/python-semantic-release/commit/e606e7583a30167cf7679c6bcada2f9e768b3abe


.. _changelog-v4.5.0:

v4.5.0 (2020-02-08)
===================

✨ Features
-----------

* **history**: Enable colon defined version (`7837f50`_)

The get_current_version_by_config_file and the replace_version_string methods now check for both
  variables defined as "variable= version" and "variable: version" This allows for using a yaml file
  to store the version.

Closes #165

🪲 Bug Fixes
------------

* Remove erroneous submodule (`762bfda`_)

* **cli**: --noop flag works when before command (`4fcc781`_)

The entry point of the app is changed from main() to entry(). Entry takes any arguments before
  commands and moves them to after commands, then calls main()

Closes #73

.. _4fcc781: https://github.com/python-semantic-release/python-semantic-release/commit/4fcc781d1a3f9235db552f0f4431c9f5e638d298
.. _762bfda: https://github.com/python-semantic-release/python-semantic-release/commit/762bfda728c266b8cd14671d8da9298fc99c63fb
.. _7837f50: https://github.com/python-semantic-release/python-semantic-release/commit/7837f5036269328ef29996b9ea63cccd5a6bc2d5


.. _changelog-v4.4.1:

v4.4.1 (2020-01-18)
===================

🪲 Bug Fixes
------------

* Add quotes around twine arguments (`46a83a9`_)

    Fixes #163

.. _46a83a9: https://github.com/python-semantic-release/python-semantic-release/commit/46a83a94b17c09d8f686c3ae7b199d7fd0e0e5e5


.. _changelog-v4.4.0:

v4.4.0 (2020-01-17)
===================

✨ Features
-----------

* **parser**: Add support for exclamation point for breaking changes (`a4f8a10`_)

According to the documentation for conventional commits, breaking changes can be described using
  exclamation points, just before the colon between type/scope and subject. In that case, the
  breaking change footer is optional, and the subject is used as description of the breaking change.
  If the footer exists, it is used for the description.

Fixes #156

* **parser**: Make BREAKING-CHANGE synonymous with BREAKING CHANGE (`beedccf`_)

According to point 16 in the conventional commit specification, this should be implemented. They
  especially mention the footer, but I kept the body for backwards compatibility. This should
  probably be removed one day. The regex is in the helpers to make it easier to re-use, but I didn't
  updated parser_tag since it looks like a legacy parser.

🪲 Bug Fixes
------------

* **github**: Add check for GITHUB_ACTOR for git push (`#162`_, `c41e9bb`_)

.. _#162: https://github.com/python-semantic-release/python-semantic-release/pull/162
.. _a4f8a10: https://github.com/python-semantic-release/python-semantic-release/commit/a4f8a10afcc358a8fbef83be2041129480350be2
.. _beedccf: https://github.com/python-semantic-release/python-semantic-release/commit/beedccfddfb360aeebef595342ee980446012ec7
.. _c41e9bb: https://github.com/python-semantic-release/python-semantic-release/commit/c41e9bb986d01b92d58419cbdc88489d630a11f1


.. _changelog-v4.3.4:

v4.3.4 (2019-12-17)
===================

🪲 Bug Fixes
------------

* Fallback to whole log if correct tag is not available (`#157`_, `252bffd`_)

The method getting all commits to consider for the release will now test whether the version in
  input is a valid reference. If it is not, it will consider the whole log for the repository.

evaluate_version_bump will still consider a message starting with the version number as a breaking
  condition to stop analyzing.

Fixes #51

.. _#157: https://github.com/python-semantic-release/python-semantic-release/pull/157
.. _252bffd: https://github.com/python-semantic-release/python-semantic-release/commit/252bffd3be7b6dfcfdb384d24cb1cd83d990fc9a


.. _changelog-v4.3.3:

v4.3.3 (2019-11-06)
===================

🪲 Bug Fixes
------------

* Set version of click to >=2.0,<8.0. (`#155`_, `f07c7f6`_)

* fix: Upgrade to click 7.0.

Fixes #117

* fix: Instead of requiring click 7.0, looks like all tests will pass with at least 2.0.

* Upstream is at ~=7.0, so let's set the range to less than 8.0.

* The string template has no variables, so remove the call to .format()

.. _#155: https://github.com/python-semantic-release/python-semantic-release/pull/155
.. _f07c7f6: https://github.com/python-semantic-release/python-semantic-release/commit/f07c7f653be1c018e443f071d9a196d9293e9521


.. _changelog-v4.3.2:

v4.3.2 (2019-10-05)
===================

🪲 Bug Fixes
------------

* Update regex to get repository owner and name for project with dots (`2778e31`_)

Remove the dot from the second capture group to allow project names containing dots to be matched.
  Instead of a greedy '+' operator, use '\*?' to allow the second group to give back the '.git' (to
  avoid including it in the project name)

Fixes #151

.. _2778e31: https://github.com/python-semantic-release/python-semantic-release/commit/2778e316a0c0aa931b1012cb3862d04659c05e73


.. _changelog-v4.3.1:

v4.3.1 (2019-09-29)
===================

🪲 Bug Fixes
------------

* Support repo urls without git terminator (`700e9f1`_)

.. _700e9f1: https://github.com/python-semantic-release/python-semantic-release/commit/700e9f18dafde1833f482272a72bb80b54d56bb3


.. _changelog-v4.3.0:

v4.3.0 (2019-09-06)
===================

✨ Features
-----------

* Add the possibility to load configuration from pyproject.toml (`35f8bfe`_)

Adds the toml library to base requirements. Also adds the related tests and documentation. Also adds
  the description of the version_source configuration option

Relates to #119

* Allow the override of configuration options from cli (`f0ac82f`_)

config can now be overriden with the "-D" flag. Also adds the related tests and documentation.

Also introduces a fixture in tests/__init__.py that reloads module using config. It is necessary
  since all tests run in the same environment. A better way would be to box the execution of tests
  (using the --forked option of pytest for example) but it does not work in non-unix systems. Also
  some tests should not break if config is changed, but it is outside of the scope of this issue.

Fixes #119

* Allow users to get version from tag and write/commit bump to file (`1f9fe1c`_)

Before this commit, version was bumped in the file, but only committed if version was obtained from
  ``version_variable`` (version_source == `commit`). Also added a relevant test and a description
  for this new option.

Fixes #104

* Make the vcs functionalities work with gitlab (`82d555d`_)

Adds python-gitlab as requirement. Refactored github specific methods while keeping default
  behavior. Also removed an unused return value for post_release_changelog. Also refactored the
  secret filtering method. Updated the related tests.

Fixes #121

🪲 Bug Fixes
------------

* Manage subgroups in git remote url (`4b11875`_)

This is a necessary fix for gitlab integration. For an illustration of the need and use for this
  fix, test was edited.

Fixes #139 Fixes #140

* Update list of commit types to include build, ci and perf (`41ea12f`_)

Also added perf to the types that trigger a patch update

Fixes #145

.. _1f9fe1c: https://github.com/python-semantic-release/python-semantic-release/commit/1f9fe1cc7666d47cc0c348c4705b63c39bf10ecc
.. _35f8bfe: https://github.com/python-semantic-release/python-semantic-release/commit/35f8bfef443c8b69560c918f4b13bc766fb3daa2
.. _41ea12f: https://github.com/python-semantic-release/python-semantic-release/commit/41ea12fa91f97c0046178806bce3be57c3bc2308
.. _4b11875: https://github.com/python-semantic-release/python-semantic-release/commit/4b118754729094e330389712cf863e1c6cefee69
.. _82d555d: https://github.com/python-semantic-release/python-semantic-release/commit/82d555d45b9d9e295ef3f9546a6ca2a38ca4522e
.. _f0ac82f: https://github.com/python-semantic-release/python-semantic-release/commit/f0ac82fe59eb59a768a73a1bf2ea934b9d448c58


.. _changelog-v4.2.0:

v4.2.0 (2019-08-05)
===================

✨ Features
-----------

* Add configuration to customize handling of dists (`2af6f41`_)

    Relates to #115

* Add support for configuring branch (`14abb05`_)

    Fixes #43

* Add support for showing unreleased changelog (`41ef794`_)

    Fixes #134

🪲 Bug Fixes
------------

* Add commit hash when generating breaking changes (`0c74faf`_)

    Fixes #120

* Kept setting new version for tag source (`0e24a56`_)

* Remove deletion of build folder (`b45703d`_)

    Fixes #115

* Updated the tag tests (`3303eef`_)

* Upgrade click to 7.0 (`2c5dd80`_)

.. _0c74faf: https://github.com/python-semantic-release/python-semantic-release/commit/0c74fafdfa81cf2e13db8f4dcf0a6f7347552504
.. _0e24a56: https://github.com/python-semantic-release/python-semantic-release/commit/0e24a5633f8f94b48da97b011634d4f9d84f7b4b
.. _14abb05: https://github.com/python-semantic-release/python-semantic-release/commit/14abb05e7f878e88002f896812d66b4ea5c219d4
.. _2af6f41: https://github.com/python-semantic-release/python-semantic-release/commit/2af6f41b21205bdd192514a434fca2feba17725a
.. _2c5dd80: https://github.com/python-semantic-release/python-semantic-release/commit/2c5dd809b84c2157a5e6cdcc773c43ec864f0328
.. _3303eef: https://github.com/python-semantic-release/python-semantic-release/commit/3303eefa49a0474bbd85df10ae186ccbf9090ec1
.. _41ef794: https://github.com/python-semantic-release/python-semantic-release/commit/41ef7947ad8a07392c96c7540980476e989c1d83
.. _b45703d: https://github.com/python-semantic-release/python-semantic-release/commit/b45703dad38c29b28575060b21e5fb0f8482c6b1


.. _changelog-v4.1.2:

v4.1.2 (2019-08-04)
===================

🪲 Bug Fixes
------------

* Correct isort build fail (`0037210`_)

build fail: https://circleci.com/gh/relekang/python-semantic-release/379

* Make sure the history only breaks loop for version commit (`5dc6cfc`_)

    Fixes #135

* **vcs**: Allow cli to be run from subdirectory (`fb7bb14`_)

📖 Documentation
----------------

* **circleci**: Point badge to master branch (`9c7302e`_)

.. _0037210: https://github.com/python-semantic-release/python-semantic-release/commit/00372100b527ff9308d9e43fe5c65cdf179dc4dc
.. _5dc6cfc: https://github.com/python-semantic-release/python-semantic-release/commit/5dc6cfc634254f09997bb3cb0f17abd296e2c01f
.. _9c7302e: https://github.com/python-semantic-release/python-semantic-release/commit/9c7302e184a1bd88f39b3039691b55cd77f0bb07
.. _fb7bb14: https://github.com/python-semantic-release/python-semantic-release/commit/fb7bb14300e483626464795b8ff4f033a194cf6f


.. _changelog-v4.1.1:

v4.1.1 (2019-02-15)
===================

📖 Documentation
----------------

* Correct usage of changelog (`f4f59b0`_)

* Debug usage and related (`f08e594`_)

Debug functionality lack documentation. Thoubleshooting is helped by documenting other environment
  variables as well.

* Describing the commands (`b6fa04d`_)

    The commands is lacking from the documentation.

* Update url for commit guidelinesThe guidelines can now be found in theDEVELOPERS.md in angular.
  (`90c1b21`_)

.. _90c1b21: https://github.com/python-semantic-release/python-semantic-release/commit/90c1b217f86263301b91d19d641c7b348e37d960
.. _b6fa04d: https://github.com/python-semantic-release/python-semantic-release/commit/b6fa04db3044525a1ee1b5952fb175a706842238
.. _f08e594: https://github.com/python-semantic-release/python-semantic-release/commit/f08e5943a9876f2d17a7c02f468720995c7d9ffd
.. _f4f59b0: https://github.com/python-semantic-release/python-semantic-release/commit/f4f59b08c73700c6ee04930221bfcb1355cbc48d


.. _changelog-v4.1.0:

v4.1.0 (2019-01-31)
===================

✨ Features
-----------

* **ci_checks**: Add support for bitbucket (`9fc120d`_)

🪲 Bug Fixes
------------

* Initialize git Repo from current folder (`c7415e6`_)

This allows to run the program also from inner repository folders

* Maintain version variable formatting on bump (`#103`_, `bf63156`_)

Small change to the way the version is written to the config file it is read from. This allows the
  formatting to be the same as before semantic-release changed it.

Prior behavior ``my_version_var="1.2.3"`` => ``my_version_var = '1.2.4'``

New behavior ``my_version_var="1.2.3"`` => ``my_version_var="1.2.4"``

I am using python-semantic-release with a Julia project and this change will allow for consistent
  formatting in my Project.toml file where the version is maintained

* Use same changelog code for command as post (`248f622`_)

    See #27 for background.

📖 Documentation
----------------

* Add installation instructions for development (`#106`_, `9168d0e`_)

* **readme**: Add testing instructions (`bb352f5`_)

.. _#103: https://github.com/python-semantic-release/python-semantic-release/pull/103
.. _#106: https://github.com/python-semantic-release/python-semantic-release/pull/106
.. _248f622: https://github.com/python-semantic-release/python-semantic-release/commit/248f62283c59182868c43ff105a66d85c923a894
.. _9168d0e: https://github.com/python-semantic-release/python-semantic-release/commit/9168d0ea56734319a5d77e890f23ff6ba51cc97d
.. _9fc120d: https://github.com/python-semantic-release/python-semantic-release/commit/9fc120d1a7e4acbbca609628e72651685108b364
.. _bb352f5: https://github.com/python-semantic-release/python-semantic-release/commit/bb352f5b6616cc42c9f2f2487c51dedda1c68295
.. _bf63156: https://github.com/python-semantic-release/python-semantic-release/commit/bf63156f60340614fae94c255fb2f097cf317b2b
.. _c7415e6: https://github.com/python-semantic-release/python-semantic-release/commit/c7415e634c0affbe6396e0aa2bafe7c1b3368914


.. _changelog-v4.0.1:

v4.0.1 (2019-01-12)
===================

🪲 Bug Fixes
------------

* Add better error message when pypi credentials are empty (`c4e5dcb`_)

    Fixes #96

* Clean out dist and build before building (`b628e46`_)

This should fix the problem with uploading old versions.

Fixes #86

* Filter out pypi secrets from exceptions (`5918371`_)

    Fixes #41

* Unfreeze dependencies (`847833b`_)

This uses ~= for most dependencies instead of pinning them.

Fixes #100

* Use correct syntax to exclude tests in package (`3e41e91`_)

This implements #92 without deleting __init__.py files.

* **parser_angular**: Fix non-match when special chars in scope (`8a33123`_)

📖 Documentation
----------------

* Remove reference to gitter (`896e37b`_)

    Fixes #90

.. _3e41e91: https://github.com/python-semantic-release/python-semantic-release/commit/3e41e91c318663085cd28c8165ece21d7e383475
.. _5918371: https://github.com/python-semantic-release/python-semantic-release/commit/5918371c1e82b06606087c9945d8eaf2604a0578
.. _847833b: https://github.com/python-semantic-release/python-semantic-release/commit/847833bf48352a4935f906d0c3f75e1db596ca1c
.. _896e37b: https://github.com/python-semantic-release/python-semantic-release/commit/896e37b95cc43218e8f593325dd4ea63f8b895d9
.. _8a33123: https://github.com/python-semantic-release/python-semantic-release/commit/8a331232621b26767e4268079f9295bf695047ab
.. _b628e46: https://github.com/python-semantic-release/python-semantic-release/commit/b628e466f86bc27cbe45ec27a02d4774a0efd3bb
.. _c4e5dcb: https://github.com/python-semantic-release/python-semantic-release/commit/c4e5dcbeda0ce8f87d25faefb4d9ae3581029a8f


.. _changelog-v4.0.0:

v4.0.0 (2018-11-22)
===================

💥 Breaking
-----------

* Add support for commit_message config variable (`4de5400`_)

This variable can allow you to skip CI pipelines in CI tools like GitLab CI by adding [CI skip] in
  the body. There are likely many uses for this beyond that particular example...

BREAKING CHANGE: If you rely on the commit message to be the version number only, this will break
  your code

re #88 #32

* Remove support for python 2 (`85fe638`_)

BREAKING CHANGE: This will only work with python 3 after this commit.

✨ Features
-----------

* **CI checks**: Add support for GitLab CI checks (`8df5e2b`_)

Check ``GITLAB_CI`` environment variable and then verify ``CI_COMMIT_REF_NAME`` matches the given
  branch.

Includes tests

Closes #88 re #32

🪲 Bug Fixes
------------

* Add check of credentials (`7d945d4`_)

* Add credentials check (`0694604`_)

* Add dists to twine call (`1cec2df`_)

* Change requests from fixed version to version range (`#93`_, `af3ad59`_)

* Change requests version to be more flexible to aid in using this with dev requirements for a
  release.

* revert changes to vcs helpers

* Re-add skip-existing (`366e9c1`_)

* Remove repository argument in twine (`e24543b`_)

* Remove universal from setup config (`18b2402`_)

* Update twine (`c4ae7b8`_)

* Use new interface for twine (`c04872d`_)

* Use twine through cli call (`ab84beb`_)

📖 Documentation
----------------

* Add type hints and more complete docstrings (`a6d5e9b`_)

Includes a few style changes suggested by pylint and type safety checks suggested by mypy

re #81

* Fix typo in documentation index (`da6844b`_)

The word role -- 'an actor's part in a play, movie, etc.' does not fit in this context. "ready to
  roll" is a phrase meaning "fully prepared to start functioning or moving" or simply "ready". I
  believe this is what was meant to be written.

💥 BREAKING CHANGES
-------------------

* If you rely on the commit message to be the version number only, this will break your code

* This will only work with python 3 after this commit.

.. _#93: https://github.com/python-semantic-release/python-semantic-release/pull/93
.. _0694604: https://github.com/python-semantic-release/python-semantic-release/commit/0694604f3b3d2159a4037620605ded09236cdef5
.. _18b2402: https://github.com/python-semantic-release/python-semantic-release/commit/18b24025e397aace03dd5bb9eed46cfdd13491bd
.. _1cec2df: https://github.com/python-semantic-release/python-semantic-release/commit/1cec2df8bcb7f877c813d6470d454244630b050a
.. _366e9c1: https://github.com/python-semantic-release/python-semantic-release/commit/366e9c1d0b9ffcde755407a1de18e8295f6ad3a1
.. _4de5400: https://github.com/python-semantic-release/python-semantic-release/commit/4de540011ab10483ee1865f99c623526cf961bb9
.. _7d945d4: https://github.com/python-semantic-release/python-semantic-release/commit/7d945d44b36b3e8c0b7771570cb2305e9e09d0b2
.. _85fe638: https://github.com/python-semantic-release/python-semantic-release/commit/85fe6384c15db317bc7142f4c8bbf2da58cece58
.. _8df5e2b: https://github.com/python-semantic-release/python-semantic-release/commit/8df5e2bdd33a620e683f3adabe174e94ceaa88d9
.. _a6d5e9b: https://github.com/python-semantic-release/python-semantic-release/commit/a6d5e9b1ccbe75d59e7240528593978a19d8d040
.. _ab84beb: https://github.com/python-semantic-release/python-semantic-release/commit/ab84beb8f809e39ae35cd3ce5c15df698d8712fd
.. _af3ad59: https://github.com/python-semantic-release/python-semantic-release/commit/af3ad59f018876e11cc3acdda0b149f8dd5606bd
.. _c04872d: https://github.com/python-semantic-release/python-semantic-release/commit/c04872d00a26e9bf0f48eeacb360b37ce0fba01e
.. _c4ae7b8: https://github.com/python-semantic-release/python-semantic-release/commit/c4ae7b8ecc682855a8568b247690eaebe62d2d26
.. _da6844b: https://github.com/python-semantic-release/python-semantic-release/commit/da6844bce0070a0020bf13950bd136fe28262602
.. _e24543b: https://github.com/python-semantic-release/python-semantic-release/commit/e24543b96adb208897f4ce3eaab96b2f4df13106


.. _changelog-v3.11.2:

v3.11.2 (2018-06-10)
====================

🪲 Bug Fixes
------------

* Upgrade twine (`9722313`_)

.. _9722313: https://github.com/python-semantic-release/python-semantic-release/commit/9722313eb63c7e2c32c084ad31bed7ee1c48a928


.. _changelog-v3.11.1:

v3.11.1 (2018-06-06)
====================

🪲 Bug Fixes
------------

* Change Gitpython version number (`23c9d4b`_)

Change the Gitpython version number to fix a bug described in #80.

📖 Documentation
----------------

* Add retry option to cli docs (`021da50`_)

.. _021da50: https://github.com/python-semantic-release/python-semantic-release/commit/021da5001934f3199c98d7cf29f62a3ad8c2e56a
.. _23c9d4b: https://github.com/python-semantic-release/python-semantic-release/commit/23c9d4b6a1716e65605ed985881452898d5cf644


.. _changelog-v3.11.0:

v3.11.0 (2018-04-12)
====================

✨ Features
-----------

* Add --retry cli option (`#78`_, `3e312c0`_)

* Add --retry cli option * Post changelog correctly * Add comments * Add --retry to the docs

* Add support to finding previous version from tags if not using commit messages (`#68`_,
  `6786487`_)

* feat: Be a bit more forgiving to find previous tags

Now grabs the previous version from tag names if it can't find it in the commit

* quantifiedcode and flake8 fixes

* Update cli.py

* Switch to ImproperConfigurationError

🪲 Bug Fixes
------------

* Add pytest cache to gitignore (`b8efd5a`_)

* Make repo non if it is not a git repository (`1dc306b`_)

    Fixes #74

📖 Documentation
----------------

* Remove old notes about trello board (`7f50c52`_)

* Update status badges (`cfa13b8`_)

.. _#68: https://github.com/python-semantic-release/python-semantic-release/pull/68
.. _#78: https://github.com/python-semantic-release/python-semantic-release/pull/78
.. _1dc306b: https://github.com/python-semantic-release/python-semantic-release/commit/1dc306b9b1db2ac360211bdc61fd815302d0014c
.. _3e312c0: https://github.com/python-semantic-release/python-semantic-release/commit/3e312c0ce79a78d25016a3b294b772983cfb5e0f
.. _6786487: https://github.com/python-semantic-release/python-semantic-release/commit/6786487ebf4ab481139ef9f43cd74e345debb334
.. _7f50c52: https://github.com/python-semantic-release/python-semantic-release/commit/7f50c521a522bb0c4579332766248778350e205b
.. _b8efd5a: https://github.com/python-semantic-release/python-semantic-release/commit/b8efd5a6249c79c8378bffea3e245657e7094ec9
.. _cfa13b8: https://github.com/python-semantic-release/python-semantic-release/commit/cfa13b8260e3f3b0bfcb395f828ad63c9c5e3ca5


.. _changelog-v3.10.3:

v3.10.3 (2018-01-29)
====================

🪲 Bug Fixes
------------

* Error when not in git repository (`#75`_, `251b190`_)

Fix an error when the program was run in a non-git repository. It would not allow the help options
  to be run.

issue #74

.. _#75: https://github.com/python-semantic-release/python-semantic-release/pull/75
.. _251b190: https://github.com/python-semantic-release/python-semantic-release/commit/251b190a2fd5df68892346926d447cbc1b32475a


.. _changelog-v3.10.2:

v3.10.2 (2017-08-03)
====================

🪲 Bug Fixes
------------

* Update call to upload to work with twine 1.9.1 (`#72`_, `8f47643`_)

.. _#72: https://github.com/python-semantic-release/python-semantic-release/pull/72
.. _8f47643: https://github.com/python-semantic-release/python-semantic-release/commit/8f47643c54996e06c358537115e7e17b77cb02ca


.. _changelog-v3.10.1:

v3.10.1 (2017-07-22)
====================

🪲 Bug Fixes
------------

* Update Twine (`#69`_, `9f268c3`_)

The publishing API is under development and older versions of Twine have problems to deal with newer
  versions of the API. Namely the logic of register/upload has changed (it was simplified).

.. _#69: https://github.com/python-semantic-release/python-semantic-release/pull/69
.. _9f268c3: https://github.com/python-semantic-release/python-semantic-release/commit/9f268c373a932621771abbe9607b739b1e331409


.. _changelog-v3.10.0:

v3.10.0 (2017-05-05)
====================

✨ Features
-----------

* Add git hash to the changelog (`#65`_, `628170e`_)

* feat(*): add git hash to the changelog

Add git hash to the changelog to ease finding the specific commit. The hash now is also easily
  viewable in Github's tag. see #63 for more information.

🪲 Bug Fixes
------------

* Make changelog problems not fail whole publish (`b5a68cf`_)

Can be fixed with changelog command later.

📖 Documentation
----------------

* Fix typo in cli.py docstring (`#64`_, `0d13985`_)

.. _#64: https://github.com/python-semantic-release/python-semantic-release/pull/64
.. _#65: https://github.com/python-semantic-release/python-semantic-release/pull/65
.. _0d13985: https://github.com/python-semantic-release/python-semantic-release/commit/0d139859cd71f2d483f4360f196d6ef7c8726c18
.. _628170e: https://github.com/python-semantic-release/python-semantic-release/commit/628170ebc440fc6abf094dd3e393f40576dedf9b
.. _b5a68cf: https://github.com/python-semantic-release/python-semantic-release/commit/b5a68cf6177dc0ed80eda722605db064f3fe2062


.. _changelog-v3.9.0:

v3.9.0 (2016-07-03)
===================

✨ Features
-----------

* Add option for choosing between versioning by commit or tag (`c0cd1f5`_)

default versioning behaviour is commiting

* Don't use file to track version, only tag to commit for versioning (`cd25862`_)

* Get repo version from historical tags instead of config file (`a45a9bf`_)

repo version will get from historical tags. init 0.0.0 if fail of find any version tag

🪲 Bug Fixes
------------

* Can't get the proper last tag from commit history (`5a0e681`_)

repo.tags returns a list sorted by the name rather than date, fix it by sorting them before
  iteration

.. _5a0e681: https://github.com/python-semantic-release/python-semantic-release/commit/5a0e681e256ec511cd6c6a8edfee9d905891da10
.. _a45a9bf: https://github.com/python-semantic-release/python-semantic-release/commit/a45a9bfb64538efeb7f6f42bb6e7ede86a4ddfa8
.. _c0cd1f5: https://github.com/python-semantic-release/python-semantic-release/commit/c0cd1f5b2e0776d7b636c3dd9e5ae863125219e6
.. _cd25862: https://github.com/python-semantic-release/python-semantic-release/commit/cd258623ee518c009ae921cd6bb3119dafae43dc


.. _changelog-v3.8.1:

v3.8.1 (2016-04-17)
===================

🪲 Bug Fixes
------------

* Add search_parent_directories option to gitpython (`#62`_, `8bf9ce1`_)

.. _#62: https://github.com/python-semantic-release/python-semantic-release/pull/62
.. _8bf9ce1: https://github.com/python-semantic-release/python-semantic-release/commit/8bf9ce11137399906f18bc8b25698b6e03a65034


.. _changelog-v3.8.0:

v3.8.0 (2016-03-21)
===================

✨ Features
-----------

* Add ci checks for circle ci (`151d849`_)

🪲 Bug Fixes
------------

* Add git fetch to frigg after success (`74a6cae`_)

* Make tag parser work correctly with breaking changes (`9496f6a`_)

The tag parser did not work correctly, this went undiscovered for a while because the tests was not
  ran by pytest.

* Refactoring cli.py to improve --help and error messages (`c79fc34`_)

📖 Documentation
----------------

* Add info about correct commit guidelines (`af35413`_)

* Add info about trello board in readme (`5229557`_)

* Fix badges in readme (`7f4e549`_)

* Update info about releases in contributing.md (`466f046`_)

.. _151d849: https://github.com/python-semantic-release/python-semantic-release/commit/151d84964266c8dca206cef8912391cb73c8f206
.. _466f046: https://github.com/python-semantic-release/python-semantic-release/commit/466f0460774cad86e7e828ffb50c7d1332b64e7b
.. _5229557: https://github.com/python-semantic-release/python-semantic-release/commit/5229557099d76b3404ea3677292332442a57ae2e
.. _74a6cae: https://github.com/python-semantic-release/python-semantic-release/commit/74a6cae2b46c5150e63136fde0599d98b9486e36
.. _7f4e549: https://github.com/python-semantic-release/python-semantic-release/commit/7f4e5493edb6b3fb3510d0bb78fcc8d23434837f
.. _9496f6a: https://github.com/python-semantic-release/python-semantic-release/commit/9496f6a502c79ec3acb4e222e190e76264db02cf
.. _af35413: https://github.com/python-semantic-release/python-semantic-release/commit/af35413fae80889e2c5fc6b7d28f77f34b3b4c02
.. _c79fc34: https://github.com/python-semantic-release/python-semantic-release/commit/c79fc3469fb99bf4c7f52434fa9c0891bca757f9


.. _changelog-v3.7.2:

v3.7.2 (2016-03-19)
===================

🪲 Bug Fixes
------------

* Move code around a bit to make flake8 happy (`41463b4`_)

.. _41463b4: https://github.com/python-semantic-release/python-semantic-release/commit/41463b49b5d44fd94c11ab6e0a81e199510fabec


.. _changelog-v3.7.1:

v3.7.1 (2016-03-15)
===================

📖 Documentation
----------------

* **configuration**: Fix typo in setup.cfg section (`725d87d`_)

.. _725d87d: https://github.com/python-semantic-release/python-semantic-release/commit/725d87dc45857ef2f9fb331222845ac83a3af135


.. _changelog-v3.7.0:

v3.7.0 (2016-01-10)
===================

✨ Features
-----------

* Add ci_checks for Frigg CI (`577c374`_)

.. _577c374: https://github.com/python-semantic-release/python-semantic-release/commit/577c374396fe303b6fe7d64630d2959998d3595c


.. _changelog-v3.6.1:

v3.6.1 (2016-01-10)
===================

🪲 Bug Fixes
------------

* Add requests as dependency (`4525a70`_)

.. _4525a70: https://github.com/python-semantic-release/python-semantic-release/commit/4525a70d5520b44720d385b0307e46fae77a7463


.. _changelog-v3.6.0:

v3.6.0 (2015-12-28)
===================

✨ Features
-----------

* Add checks for semaphore (`2d7ef15`_)

    Fixes #44

📖 Documentation
----------------

* Add documentation for configuring on CI (`7806940`_)

* Add note about node semantic release (`0d2866c`_)

* Add step by step guide for configuring travis ci (`6f23414`_)

* Move automatic-releases to subfolder (`ed68e5b`_)

* Remove duplicate readme (`42a9421`_)

It was created by pandoc earlier when the original readme was written in markdown.

.. _0d2866c: https://github.com/python-semantic-release/python-semantic-release/commit/0d2866c528098ecaf1dd81492f28d3022a2a54e0
.. _2d7ef15: https://github.com/python-semantic-release/python-semantic-release/commit/2d7ef157b1250459060e99601ec53a00942b6955
.. _42a9421: https://github.com/python-semantic-release/python-semantic-release/commit/42a942131947cd1864c1ba29b184caf072408742
.. _6f23414: https://github.com/python-semantic-release/python-semantic-release/commit/6f2341442f61f0284b1119a2c49e96f0be678929
.. _7806940: https://github.com/python-semantic-release/python-semantic-release/commit/7806940ae36cb0d6ac0f966e5d6d911bd09a7d11
.. _ed68e5b: https://github.com/python-semantic-release/python-semantic-release/commit/ed68e5b8d3489463e244b078ecce8eab2cba2bb1


.. _changelog-v3.5.0:

v3.5.0 (2015-12-22)
===================

✨ Features
-----------

* Add author in commit (`020efaa`_)

    Fixes #40

* Checkout master before publishing (`dc4077a`_)

    Related to #39

🪲 Bug Fixes
------------

* Remove " from git push command (`031318b`_)

📖 Documentation
----------------

* Convert readme to rst (`e8a8d26`_)

.. _020efaa: https://github.com/python-semantic-release/python-semantic-release/commit/020efaaadf588e3fccd9d2f08a273c37e4158421
.. _031318b: https://github.com/python-semantic-release/python-semantic-release/commit/031318b3268bc37e6847ec049b37425650cebec8
.. _dc4077a: https://github.com/python-semantic-release/python-semantic-release/commit/dc4077a2d07e0522b625336dcf83ee4e0e1640aa
.. _e8a8d26: https://github.com/python-semantic-release/python-semantic-release/commit/e8a8d265aa2147824f18065b39a8e7821acb90ec


.. _changelog-v3.4.0:

v3.4.0 (2015-12-22)
===================

✨ Features
-----------

* Add travis environment checks (`f386db7`_)

These checks will ensure that semantic release only runs against master and not in a pull-request.

.. _f386db7: https://github.com/python-semantic-release/python-semantic-release/commit/f386db75b77acd521d2f5bde2e1dde99924dc096


.. _changelog-v3.3.3:

v3.3.3 (2015-12-22)
===================

🪲 Bug Fixes
------------

* Do git push and git push --tags instead of --follow-tags (`8bc70a1`_)

.. _8bc70a1: https://github.com/python-semantic-release/python-semantic-release/commit/8bc70a183fd72f595c72702382bc0b7c3abe99c8


.. _changelog-v3.3.2:

v3.3.2 (2015-12-21)
===================

🪲 Bug Fixes
------------

* Change build badge (`0dc068f`_)

📖 Documentation
----------------

* Update docstrings for generate_changelog (`987c6a9`_)

.. _0dc068f: https://github.com/python-semantic-release/python-semantic-release/commit/0dc068fff2f8c6914f4abe6c4e5fb2752669159e
.. _987c6a9: https://github.com/python-semantic-release/python-semantic-release/commit/987c6a96d15997e38c93a9d841c618c76a385ce7


.. _changelog-v3.3.1:

v3.3.1 (2015-12-21)
===================

🪲 Bug Fixes
------------

* Add pandoc to travis settings (`17d40a7`_)

* Only list commits from the last version tag (`191369e`_)

    Fixes #28

.. _17d40a7: https://github.com/python-semantic-release/python-semantic-release/commit/17d40a73062ffa774542d0abc0f59fc16b68be37
.. _191369e: https://github.com/python-semantic-release/python-semantic-release/commit/191369ebd68526e5b1afcf563f7d13e18c8ca8bf


.. _changelog-v3.3.0:

v3.3.0 (2015-12-20)
===================

✨ Features
-----------

* Add support for environment variables for pypi credentials (`3b383b9`_)

🪲 Bug Fixes
------------

* Add missing parameters to twine.upload (`4bae22b`_)

* Better filtering of github token in push error (`9b31da4`_)

* Downgrade twine to version 1.5.0 (`66df378`_)

* Make sure the github token is not in the output (`55356b7`_)

* Push to master by default (`a0bb023`_)

.. _3b383b9: https://github.com/python-semantic-release/python-semantic-release/commit/3b383b92376a7530e89b11de481c4dfdfa273f7b
.. _4bae22b: https://github.com/python-semantic-release/python-semantic-release/commit/4bae22bae9b9d9abf669b028ea3af4b3813a1df0
.. _55356b7: https://github.com/python-semantic-release/python-semantic-release/commit/55356b718f74d94dd92e6c2db8a15423a6824eb5
.. _66df378: https://github.com/python-semantic-release/python-semantic-release/commit/66df378330448a313aff7a7c27067adda018904f
.. _9b31da4: https://github.com/python-semantic-release/python-semantic-release/commit/9b31da4dc27edfb01f685e6036ddbd4c715c9f60
.. _a0bb023: https://github.com/python-semantic-release/python-semantic-release/commit/a0bb023438a1503f9fdb690d976d71632f19a21f


.. _changelog-v3.2.1:

v3.2.1 (2015-12-20)
===================

🪲 Bug Fixes
------------

* Add requirements to manifest (`ed25ecb`_)

* **pypi**: Add sdist as default in addition to bdist_wheel (`a1a35f4`_)

There are a lot of outdated pip installations around which leads to confusions if a package have had
  an sdist release at some point and then suddenly is only available as wheel packages, because old
  pip clients will then download the latest sdist package available.

.. _a1a35f4: https://github.com/python-semantic-release/python-semantic-release/commit/a1a35f43175187091f028474db2ebef5bfc77bc0
.. _ed25ecb: https://github.com/python-semantic-release/python-semantic-release/commit/ed25ecbaeec0e20ad3040452a5547bb7d6faf6ad


.. _changelog-v3.2.0:

v3.2.0 (2015-12-20)
===================

✨ Features
-----------

* **angular-parser**: Remove scope requirement (`90c9d8d`_)

* **git**: Add push to GH_TOKEN@github-url (`546b5bf`_)

🪲 Bug Fixes
------------

* **deps**: Use one file for requirements (`4868543`_)

.. _4868543: https://github.com/python-semantic-release/python-semantic-release/commit/486854393b24803bb2356324e045ccab17510d46
.. _546b5bf: https://github.com/python-semantic-release/python-semantic-release/commit/546b5bf15466c6f5dfe93c1c03ca34604b0326f2
.. _90c9d8d: https://github.com/python-semantic-release/python-semantic-release/commit/90c9d8d4cd6d43be094cda86579e00b507571f98


.. _changelog-v3.1.0:

v3.1.0 (2015-08-31)
===================

✨ Features
-----------

* **pypi**: Add option to disable pypi upload (`f5cd079`_)

.. _f5cd079: https://github.com/python-semantic-release/python-semantic-release/commit/f5cd079edb219de5ad03a71448d578f5f477da9c


.. _changelog-v3.0.0:

v3.0.0 (2015-08-25)
===================

✨ Features
-----------

* **parser**: Add tag parser (`a7f392f`_)

This parser is based on the same commit style as 1.x.x of python-semantic-release. However, it
  requires "BREAKING CHANGE: <explanation> for a breaking change

🪲 Bug Fixes
------------

* **errors**: Add exposing of errors in package (`3662d76`_)

* **version**: Parse file instead for version (`005dba0`_)

This makes it possible to use the version command without a setup.py file.

.. _005dba0: https://github.com/python-semantic-release/python-semantic-release/commit/005dba0094eeb4098315ef383a746e139ffb504d
.. _3662d76: https://github.com/python-semantic-release/python-semantic-release/commit/3662d7663291859dd58a91b4b4ccde4f0edc99b2
.. _a7f392f: https://github.com/python-semantic-release/python-semantic-release/commit/a7f392fd4524cc9207899075631032e438e2593c


.. _changelog-v2.1.4:

v2.1.4 (2015-08-24)
===================

🪲 Bug Fixes
------------

* **github**: Fix property calls (`7ecdeb2`_)

    Properties can only be used from instances.

.. _7ecdeb2: https://github.com/python-semantic-release/python-semantic-release/commit/7ecdeb22de96b6b55c5404ebf54a751911c4d8cd


.. _changelog-v2.1.3:

v2.1.3 (2015-08-22)
===================

🪲 Bug Fixes
------------

* **hvcs**: Make Github.token an property (`37d5e31`_)

📖 Documentation
----------------

* **api**: Update apidocs (`6185380`_)

* **parsers**: Add documentation about commit parsers (`9b55422`_)

* **readme**: Update readme with information about the changelog command (`56a745e`_)

.. _37d5e31: https://github.com/python-semantic-release/python-semantic-release/commit/37d5e3110397596a036def5f1dccf0860964332c
.. _56a745e: https://github.com/python-semantic-release/python-semantic-release/commit/56a745ef6fa4edf6f6ba09c78fcc141102cf2871
.. _6185380: https://github.com/python-semantic-release/python-semantic-release/commit/6185380babedbbeab2a2a342f17b4ff3d4df6768
.. _9b55422: https://github.com/python-semantic-release/python-semantic-release/commit/9b554222768036024a133153a559cdfc017c1d91


.. _changelog-v2.1.2:

v2.1.2 (2015-08-20)
===================

🪲 Bug Fixes
------------

* **cli**: Fix call to generate_changelog in publish (`5f8bce4`_)

.. _5f8bce4: https://github.com/python-semantic-release/python-semantic-release/commit/5f8bce4cbb5e1729e674efd6c651e2531aea2a16


.. _changelog-v2.1.1:

v2.1.1 (2015-08-20)
===================

🪲 Bug Fixes
------------

* **history**: Fix issue in get_previous_version (`f961786`_)

.. _f961786: https://github.com/python-semantic-release/python-semantic-release/commit/f961786aa3eaa3a620f47cc09243340fd329b9c2


.. _changelog-v2.1.0:

v2.1.0 (2015-08-20)
===================

✨ Features
-----------

* **cli**: Add the possibility to repost the changelog (`4d028e2`_)

🪲 Bug Fixes
------------

* **cli**: Fix check of token in changelog command (`cc6e6ab`_)

* **github**: Fix the github releases integration (`f0c3c1d`_)

* **history**: Fix changelog generation (`f010272`_)

This enables regeneration of a given versions changelog.

.. _4d028e2: https://github.com/python-semantic-release/python-semantic-release/commit/4d028e21b9da01be8caac8f23f2c11e0c087e485
.. _cc6e6ab: https://github.com/python-semantic-release/python-semantic-release/commit/cc6e6abe1e91d3aa24e8d73e704829669bea5fd7
.. _f010272: https://github.com/python-semantic-release/python-semantic-release/commit/f01027203a8ca69d21b4aff689e60e8c8d6f9af5
.. _f0c3c1d: https://github.com/python-semantic-release/python-semantic-release/commit/f0c3c1db97752b71f2153ae9f623501b0b8e2c98


.. _changelog-v2.0.0:

v2.0.0 (2015-08-19)
===================

💥 Breaking
-----------

* **history**: Set angular parser as the default (`c2cf537`_)

BREAKING CHANGE: This changes the default parser. Thus, the default behaviour of the commit log
  evaluator will change. From now on it will use the angular commit message spec to determine the
  new version.

✨ Features
-----------

* **cli**: Add command for printing the changelog (`336b8bc`_)

Usage: ``semantic_release changelog``

* **github**: Add github release changelog helper (`da18795`_)

* **history**: Add angular parser (`91e4f0f`_)

This adds a parser that follows the angular specification. The parser is not hooked into the history
  evaluation yet. However, it will become the default parser of commit messages when the evaluator
  starts using exchangeable parsers.

Related to #17

* **history**: Add generate_changelog function (`347f21a`_)

It generates a dict with changelog information to each of the given section types.

* **history**: Add markdown changelog formatter (`d77b58d`_)

* **publish**: Add publishing of changelog to github (`74324ba`_)

* **settings**: Add loading of current parser (`7bd0916`_)

🪲 Bug Fixes
------------

* **cli**: Change output indentation on changelog (`2ca41d3`_)

* **history**: Fix level id's in angular parser (`2918d75`_)

* **history**: Fix regex in angular parser (`974ccda`_)

This fixes a problem where multiline commit messages where not correctly parsed.

* **history**: Support unexpected types in changelog generator (`13deacf`_)

💥 BREAKING CHANGES
-------------------

* **history**: This changes the default parser. Thus, the default behaviour of the commit log
  evaluator will change. From now on it will use the angular commit message spec to determine the
  new version.

.. _13deacf: https://github.com/python-semantic-release/python-semantic-release/commit/13deacf5d33ed500e4e94ea702a2a16be2aa7c48
.. _2918d75: https://github.com/python-semantic-release/python-semantic-release/commit/2918d759bf462082280ede971a5222fe01634ed8
.. _2ca41d3: https://github.com/python-semantic-release/python-semantic-release/commit/2ca41d3bd1b8b9d9fe7e162772560e3defe2a41e
.. _336b8bc: https://github.com/python-semantic-release/python-semantic-release/commit/336b8bcc01fc1029ff37a79c92935d4b8ea69203
.. _347f21a: https://github.com/python-semantic-release/python-semantic-release/commit/347f21a1f8d655a71a0e7d58b64d4c6bc6d0bf31
.. _74324ba: https://github.com/python-semantic-release/python-semantic-release/commit/74324ba2749cdbbe80a92b5abbecfeab04617699
.. _7bd0916: https://github.com/python-semantic-release/python-semantic-release/commit/7bd0916f87a1f9fe839c853eab05cae1af420cd2
.. _91e4f0f: https://github.com/python-semantic-release/python-semantic-release/commit/91e4f0f4269d01b255efcd6d7121bbfd5a682e12
.. _974ccda: https://github.com/python-semantic-release/python-semantic-release/commit/974ccdad392d768af5e187dabc184be9ac3e133d
.. _c2cf537: https://github.com/python-semantic-release/python-semantic-release/commit/c2cf537a42beaa60cd372c7c9f8fb45db8085917
.. _d77b58d: https://github.com/python-semantic-release/python-semantic-release/commit/d77b58db4b66aec94200dccab94f483def4dacc9
.. _da18795: https://github.com/python-semantic-release/python-semantic-release/commit/da187951af31f377ac57fe17462551cfd776dc6e


.. _changelog-v1.0.0:

v1.0.0 (2015-08-04)
===================

💥 Breaking
-----------

* Restructure helpers into history and pypi (`00f64e6`_)

📖 Documentation
----------------

* Add automatic publishing documentation, resolves `#18`_ (`58076e6`_)

.. _#18: https://github.com/python-semantic-release/python-semantic-release/issues/18
.. _00f64e6: https://github.com/python-semantic-release/python-semantic-release/commit/00f64e623db0e21470d55488c5081e12d6c11fd3
.. _58076e6: https://github.com/python-semantic-release/python-semantic-release/commit/58076e60bf20a5835b112b5e99a86c7425ffe7d9


.. _changelog-v0.9.1:

v0.9.1 (2015-08-04)
===================

🪲 Bug Fixes
------------

* Fix ``get_current_head_hash`` to ensure it only returns the hash (`7c28832`_)

.. _7c28832: https://github.com/python-semantic-release/python-semantic-release/commit/7c2883209e5bf4a568de60dbdbfc3741d34f38b4


.. _changelog-v0.9.0:

v0.9.0 (2015-08-03)
===================

✨ Features
-----------

* Add Python 2.7 support, resolves `#10`_ (`c05e13f`_)

.. _#10: https://github.com/python-semantic-release/python-semantic-release/issues/10
.. _c05e13f: https://github.com/python-semantic-release/python-semantic-release/commit/c05e13f22163237e963c493ffeda7e140f0202c6


.. _changelog-v0.8.0:

v0.8.0 (2015-08-03)
===================

✨ Features
-----------

* Add ``check_build_status`` option, resolves `#5`_ (`310bb93`_)

* Add ``get_current_head_hash`` in git helpers (`d864282`_)

* Add git helper to get owner and name of repo (`f940b43`_)

.. _#5: https://github.com/python-semantic-release/python-semantic-release/issues/5
.. _310bb93: https://github.com/python-semantic-release/python-semantic-release/commit/310bb9371673fcf9b7b7be48422b89ab99753f04
.. _d864282: https://github.com/python-semantic-release/python-semantic-release/commit/d864282c498f0025224407b3eeac69522c2a7ca0
.. _f940b43: https://github.com/python-semantic-release/python-semantic-release/commit/f940b435537a3c93ab06170d4a57287546bd8d3b


.. _changelog-v0.7.0:

v0.7.0 (2015-08-02)
===================

✨ Features
-----------

* Add ``patch_without_tag`` option, resolves `#6`_ (`3734a88`_)

📖 Documentation
----------------

* Set up sphinx based documentation, resolves `#1`_ (`41fba78`_)

.. _#1: https://github.com/python-semantic-release/python-semantic-release/issues/1
.. _#6: https://github.com/python-semantic-release/python-semantic-release/issues/6
.. _3734a88: https://github.com/python-semantic-release/python-semantic-release/commit/3734a889f753f1b9023876e100031be6475a90d1
.. _41fba78: https://github.com/python-semantic-release/python-semantic-release/commit/41fba78a389a8d841316946757a23a7570763c39


.. _changelog-v0.6.0:

v0.6.0 (2015-08-02)
===================

✨ Features
-----------

* Add twine for uploads to pypi, resolves `#13`_ (`eec2561`_)

.. _#13: https://github.com/python-semantic-release/python-semantic-release/issues/13
.. _eec2561: https://github.com/python-semantic-release/python-semantic-release/commit/eec256115b28b0a18136a26d74cfc3232502f1a6


.. _changelog-v0.5.4:

v0.5.4 (2015-07-29)
===================

🪲 Bug Fixes
------------

* Add python2 not supported warning (`e84c4d8`_)

.. _e84c4d8: https://github.com/python-semantic-release/python-semantic-release/commit/e84c4d8b6f212aec174baccd188185627b5039b6


.. _changelog-v0.5.3:

v0.5.3 (2015-07-28)
===================

⚙️ Build System
---------------

* Add ``wheel`` as a dependency (`971e479`_)

.. _971e479: https://github.com/python-semantic-release/python-semantic-release/commit/971e4795a8b8fea371fcc02dc9221f58a0559f32


.. _changelog-v0.5.2:

v0.5.2 (2015-07-28)
===================

🪲 Bug Fixes
------------

* Fix python wheel tag (`f9ac163`_)

.. _f9ac163: https://github.com/python-semantic-release/python-semantic-release/commit/f9ac163491666022c809ad49846f3c61966e10c1


.. _changelog-v0.5.1:

v0.5.1 (2015-07-28)
===================

🪲 Bug Fixes
------------

* Fix push commands (`8374ef6`_)

.. _8374ef6: https://github.com/python-semantic-release/python-semantic-release/commit/8374ef6bd78eb564a6d846b882c99a67e116394e


.. _changelog-v0.5.0:

v0.5.0 (2015-07-28)
===================

✨ Features
-----------

* Add setup.py hook for the cli interface (`c363bc5`_)

.. _c363bc5: https://github.com/python-semantic-release/python-semantic-release/commit/c363bc5d3cb9e9a113de3cd0c49dd54a5ea9cf35


.. _changelog-v0.4.0:

v0.4.0 (2015-07-28)
===================

✨ Features
-----------

* Add publish command (`d8116c9`_)

.. _d8116c9: https://github.com/python-semantic-release/python-semantic-release/commit/d8116c9dec472d0007973939363388d598697784


.. _changelog-v0.3.2:

v0.3.2 (2015-07-28)
===================

* No change


.. _changelog-v0.3.1:

v0.3.1 (2015-07-28)
===================

🪲 Bug Fixes
------------

* Fix wheel settings (`1e860e8`_)

.. _1e860e8: https://github.com/python-semantic-release/python-semantic-release/commit/1e860e8a4d9ec580449a0b87be9660a9482fa2a4


.. _changelog-v0.3.0:

v0.3.0 (2015-07-27)
===================

✨ Features
-----------

* Add support for tagging releases (`5f4736f`_)

🪲 Bug Fixes
------------

* Fix issue when version should not change (`441798a`_)

.. _441798a: https://github.com/python-semantic-release/python-semantic-release/commit/441798a223195138c0d3d2c51fc916137fef9a6c
.. _5f4736f: https://github.com/python-semantic-release/python-semantic-release/commit/5f4736f4e41bc96d36caa76ca58be0e1e7931069


.. _changelog-v0.2.0:

v0.2.0 (2015-07-27)
===================

✨ Features
-----------

* added no-operation (``--noop``) mode (`44c2039`_)

⚙️ Build System
---------------

* Swapped pygit2 with gitpython to avoid libgit2 dependency (`8165a2e`_)

.. _44c2039: https://github.com/python-semantic-release/python-semantic-release/commit/44c203989aabc9366ba42ed2bc40eaccd7ac891c
.. _8165a2e: https://github.com/python-semantic-release/python-semantic-release/commit/8165a2eef2c6eea88bfa52e6db37abc7374cccba


.. _changelog-v0.1.1:

v0.1.1 (2015-07-27)
===================

🪲 Bug Fixes
------------

* Fix entry point (`bd7ce7f`_)

.. _bd7ce7f: https://github.com/python-semantic-release/python-semantic-release/commit/bd7ce7f47c49e2027767fb770024a0d4033299fa


.. _changelog-v0.1.0:

v0.1.0 (2015-07-27)
===================

* Initial Release
