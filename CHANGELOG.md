# Changelog

All notable changes to this project will be documented in this file.

## [3.3.1] - 2026-05-31

### Build

- Switch release tooling from semantic-release to git-cliff
- Update dev dependencies
- Update dev dependencies
- Update dev dependencies
- Update dependencies specification
- Update dev dependencies

### CI/CD

- Streamline GitHub workflows and repo metadata
- Simplify CI configuration and use just for tasks
- Add poetry-core to dependencies installation
- Simplify workflows

### Documentation

- Refresh project documentation
- Remove TOC

### Miscellaneous

- Add justfile

### Refactor

- Derive __version__ from package metadata

### Testing

- Replace sh with stdlib subprocess in core tests

## [3.3.0] - 2026-03-14

### Bug fixes

- **ci**: Resolve linter failures in multiple dotenv support

### Build

- **deps-dev**: Bump ty from 0.0.19 to 0.0.21
- Update dev dependencies

### CI/CD

- Lower codecov target to 90%

### Features

- **config**: Support multiple dotenv locations

### Refactor

- Address PR review comments

## [3.2.0] - 2026-03-08

### Bug fixes

- Update metadata

### Build

- **deps**: Bump crazy-max/ghaction-github-labeler from 5 to 6
- **deps-dev**: Bump ty from 0.0.18 to 0.0.19
- Update dev dependencies
- **deps-dev**: Bump ty from 0.0.17 to 0.0.18
- Update dev dependencies
- Replace mypy wit ty

### Miscellaneous

- Update chore files

## [3.1.1] - 2026-01-10

### Build

- Update dev dependencies
- Update dev dependencies
- Update dev dependencies
- Update dev dependencies
- Update dev dependencies
- Update dev dependencies
- Update dev dependencies
- Update dev dependencies

### CI/CD

- Upgrade actions
- Update version of the Checkout action
- Update semantic release action version
- Update codecov actions version

### Documentation

- Update license

### Miscellaneous

- Update .gitignore
- Remove outdated funding links from README and FUNDING.yaml

## [3.1.0] - 2025-10-05

### Bug fixes

- Improve shell detection for activation command

### Build

- Update dev dependencies
- Update dev dependencies
- Update dev dependencies
- Update dev dependencies
- Update dev dependencies
- **deps-dev**: Bump pytest-cov from 6.2.1 to 6.3.0
- **deps**: Bump python-semantic-release/python-semantic-release
- Update dev dependencies
- Update dev dependencies
- **deps**: Bump python-semantic-release/python-semantic-release
- **deps**: Bump actions/checkout from 4 to 5
- Update dev dependencies
- **deps-dev**: Bump python-semantic-release from 10.1.0 to 10.3.1
- Update dev dependencies
- Update dev dependencies
- Update dev dependencies
- Update dev dependencies
- Update dev dependencies

### CI/CD

- Update tests matrix
- Update Poetry version
- Update actions
- **workflow**: Disable force patch

### Miscellaneous

- Remove Codespell linter

## [3.0.1] - 2025-07-19

### CI/CD

- **workflow**: Enable force patch to refresh changelog

## [3.0.0] - 2025-07-19

### Build

- Update dev dependencies
- **deps-dev**: Bump ruff from 0.12.2 to 0.12.3
- Update dev dependencies
- Update dev dependencies
- **deps-dev**: Bump poethepoet from 0.35.0 to 0.36.0

### Features

- Add activate command

## [2.13.0] - 2025-06-29

### Miscellaneous

- **ruff**: Update config

### Refactor

- Replace os with pathlib

## [2.12.1] - 2025-06-29

### Build

- Remove LSPs
- Update dev dependencies
- Update dev dependencies
- **deps-dev**: Bump python-semantic-release from 9.21.0 to 10.1.0
- **deps**: Bump python-semantic-release/python-semantic-release
- Update dev dependencies
- **deps**: Bump urllib3 from 2.4.0 to 2.5.0

### Documentation

- Update contribution guidelines

### Miscellaneous

- Update config
- **ruff**: Update config

## [2.12.0] - 2025-06-15

### Build

- Update dev dependencies

### Miscellaneous

- **mypy**: Update config

### Refactor

- Update docstrings

## [2.11.0] - 2025-06-09

### Refactor

- Run linters

## [2.10.0] - 2025-06-09

### Bug fixes

- Resolve issue with invalid poetry version

### Build

- Update dev dependencies
- **deps-dev**: Bump commitizen from 4.7.1 to 4.7.2
- Update dependencies
- Update dependencies

### CI/CD

- Update test matrix
- Add funding links

### Miscellaneous

- Remove extraneous character

## [2.9.1] - 2025-05-05

### Build

- Update dependencies
- **poetry**: Update dev dependencies
- **poetry**: Update dev dependencies
- **poetry**: Update dev dependencies
- **deps-dev**: Bump ruff from 0.11.2 to 0.11.4
- **deps-dev**: Bump commitizen from 4.4.1 to 4.5.0
- **deps-dev**: Bump pytest-cov from 6.0.0 to 6.1.1
- **deps-dev**: Bump coverage from 7.7.1 to 7.8.0

### CI/CD

- Update labels

### Documentation

- Update contribution guidelines
- Update templates

## [2.9.0] - 2025-03-30

### Build

- **poetry**: Update dev dependencies

### CI/CD

- Remove stale workflows

### Documentation

- **README**: Update badges

### Miscellaneous

- **ruff**: Update config

### Refactor

- Replace isort and black with ruff

### Style

- **CHANGELOG**: Run formatters
- **poetry**: Run formatters

## [2.8.1] - 2025-03-21

### Build

- **poetry**: Remove pre-commit
- **deps-dev**: Bump coverage from 7.6.12 to 7.7.0
- **deps-dev**: Bump poethepoet from 0.33.0 to 0.33.1
- **deps-dev**: Bump ruff from 0.9.10 to 0.11.0
- **poetry**: Update dev dependencies
- **deps-dev**: Bump commitizen from 4.3.0 to 4.4.1
- **deps-dev**: Bump poethepoet from 0.32.2 to 0.33.0
- **deps-dev**: Bump jinja2 from 3.1.5 to 3.1.6
- **deps**: Bump python-semantic-release/python-semantic-release
- **deps-dev**: Bump python-semantic-release from 9.19.1 to 9.21.0

### CI/CD

- Update IDE config
- **pre-commit**: Update hooks
- **workflows**: Update poetry version

### Documentation

- Update contribution guidelines

### Miscellaneous

- Update funding links

### Style

- Run formatters
- Run formatters

## [2.8.0] - 2025-03-01

### Bug fixes

- Update minimum required version of the poetry

### Build

- **poetry**: Update dev dependencies
- **deps**: Bump poetry from 2.0.1 to 2.1.1
- **deps-dev**: Bump ruff-lsp from 0.0.61 to 0.0.62
- **deps-dev**: Bump ruff from 0.9.5 to 0.9.6
- **deps-dev**: Bump coverage from 7.6.11 to 7.6.12
- **deps-dev**: Bump python-semantic-release from 9.18.1 to 9.19.1
- **deps**: Bump python-semantic-release/python-semantic-release
- **poetry**: Downgrade pytest
- **poetry**: Update dev dependencies

### CI/CD

- **pre-commit**: Update hooks
- **workflows**: Remove forced patch release

### Miscellaneous

- **pyright**: Update config

## [2.7.3] - 2025-02-09

### CI/CD

- **workflows**: Remove Poetry v1.5 and v1.6 from the tests matrix
- **workflows**: Update Python version to 3.13

### Documentation

- **assets**: Update demo.gif and schema_example.png
- **examples**: Update TOML configuration examples to use [tool.dotenv] section
- **README**: Update notes with new [tool.dotenv] section and deprecation warning

### Features

- Add support for the [tool.dotenv] section in TOML configuration

### Miscellaneous

- **ruff**: Update config

## [2.7.2] - 2025-02-08

### Bug fixes

- Improve logging messages
- Update copyright year
- **config**: Add correct handling of the bool values
- **dotenv.core**: Partially rollback optimization changes to resolve issue with overriding variables

### Build

- **poetry**: Update dependencies
- **deps-dev**: Bump poethepoet from 0.32.1 to 0.32.2
- **poetry**: Update dependencies
- **deps-dev**: Bump ruff from 0.9.1 to 0.9.2
- **poetry**: Update dependencies
- **deps-dev**: Bump ruff from 0.8.4 to 0.8.6
- **poetry**: Update dependencies
- **deps-dev**: Bump coverage from 7.6.9 to 7.6.10
- **deps-dev**: Bump ipython from 8.18.0 to 8.18.1
- **deps-dev**: Bump poethepoet from 0.31.1 to 0.32.0
- **poetry**: Update dependencies
- **deps-dev**: Bump python-semantic-release from 9.15.1 to 9.15.2
- **deps-dev**: Bump mypy from 1.13.0 to 1.14.0
- **deps-dev**: Bump ruff from 0.8.3 to 0.8.4
- **deps-dev**: Bump deptry from 0.21.1 to 0.21.2
- **deps-dev**: Bump pyupgrade from 3.19.0 to 3.19.1
- **poetry**: Update dependencies
- **deps-dev**: Bump python-semantic-release from 9.15.0 to 9.15.1
- **deps-dev**: Bump ruff from 0.8.1 to 0.8.2
- **deps-dev**: Bump commitizen from 4.0.0 to 4.1.0
- **deps-dev**: Bump coverage from 7.6.8 to 7.6.9
- **deps-dev**: Bump python-semantic-release from 9.14.0 to 9.15.0
- **poetry**: Update dependencies
- **poetry**: Update dependencies
- **deps-dev**: Bump python-lsp-isort from 0.1 to 0.2.0
- **deps-dev**: Bump python-semantic-release from 9.9.0 to 9.11.0
- **deps-dev**: Bump sh from 2.0.7 to 2.1.0
- **deps-dev**: Bump ruff from 0.6.8 to 0.6.9
- **poetry**: Update dependencies
- **deps-dev**: Bump ruff-lsp from 0.0.56 to 0.0.57
- **deps-dev**: Bump ruff from 0.6.5 to 0.6.7
- **poetry**: Update dependencies
- **deps-dev**: Bump ruff-lsp from 0.0.55 to 0.0.56
- **deps-dev**: Bump ruff from 0.6.3 to 0.6.4
- **deps**: Bump cryptography from 43.0.0 to 43.0.1
- **deps-dev**: Bump python-semantic-release from 9.8.7 to 9.8.8
- **poetry**: Update dependencies
- **poetry**: Update dependencies
- **poetry**: Update dependencies
- **deps-dev**: Bump ruff from 0.5.2 to 0.5.5
- **deps-dev**: Bump commitizen from 3.27.0 to 3.28.0
- **deps-dev**: Bump mypy from 1.10.1 to 1.11.0
- **deps-dev**: Bump python-semantic-release from 9.8.5 to 9.8.6
- **deps-dev**: Bump deptry from 0.16.2 to 0.17.0
- **deps-dev**: Bump ruff from 0.5.1 to 0.5.2
- **poetry**: Update dependencies
- **deps-dev**: Bump python-semantic-release from 9.8.3 to 9.8.5
- **deps-dev**: Bump deptry from 0.16.1 to 0.16.2
- **deps-dev**: Bump ruff from 0.5.0 to 0.5.1
- **deps**: Bump certifi from 2024.6.2 to 2024.7.4
- **poetry**: Update dependencies
- **poetry**: Lock dependencies
- **poetry**: Update dependencies
- **deps-dev**: Bump tornado from 6.4 to 6.4.1
- **deps-dev**: Bump ruff from 0.4.5 to 0.4.7
- **deps-dev**: Bump sh from 2.0.6 to 2.0.7
- **deps-dev**: Bump coverage from 7.5.2 to 7.5.3
- **deps-dev**: Bump xdoctest from 1.1.3 to 1.1.4
- **deps-dev**: Bump ruff from 0.4.4 to 0.4.5
- **deps-dev**: Bump commitizen from 3.26.0 to 3.27.0
- **deps-dev**: Bump coverage from 7.5.1 to 7.5.2
- **deps-dev**: Bump commitizen from 3.25.0 to 3.26.0
- **deps-dev**: Bump python-semantic-release from 9.7.1 to 9.7.3
- **deps-dev**: Bump python-semantic-release from 9.7.0 to 9.7.1
- **deps-dev**: Bump ruff from 0.4.3 to 0.4.4
- **deps**: Bump poetry from 1.8.2 to 1.8.3

### CI/CD

- **workflows**: Set force patch release
- **labels**: Update description
- **codecov**: Disable patch status
- **workflows**: Remove MacOS x86_64 from the test matrix
- **workflows**: Remove lockfile check
- **workflows**: Update lock-threads comments for clarity
- **workflows**: Update Python version and add caching
- **workflows**: Lock version of the semantic-release
- **workflows**: Update Poetry versions and add caching
- **dependabot**: Remove redundant configuration lines
- **labels**: Update description
- **actions**: Remove detect-changes
- **workflows**: Update Python version to 3.13
- **actions**: Remove setup-environment
- **pre-commit**: Update hooks
- **pre-commit**: Update hooks
- **pre-commit**: Update hooks
- **pre-commit**: Update hooks
- **pre-commit**: Update hooks
- **pre-commit**: Update hooks
- **pre-commit**: Update hooks
- **workflows**: Add Python 3.13 into the testing grid
- **workflows**: Remove support of the Python 3.8
- **workflows**: Remove schedule from the lock-threads
- **workflows.release**: Removed flag that forced release
- **workflows.release**: Add a flag to force release
- **pre-commit**: Update hooks
- **pre-commit**: Update hooks
- **pre-commit**: Update hooks
- **pre-commit**: Update dependencies
- **labels**: Update color fields
- **labels**: Update color fields
- **workflows**: Update names
- Add CodeCov config
- **workflows**: Update release workflow
- **workflows**: Add workflow that runs linters
- **workflows**: Add workflow that runs tests
- **actions**: Update action that setups environment
- **actions**: Update anchors
- **actions**: Add action that setups env
- **actions**: Add action that setups env
- **actions**: Rename actions
- **workflows**: Update IDs
- **actions**: Remove typo
- **workflows**: Add matrix for tests workflow
- **workflows**: Add `name` field
- **workflows**: Remove CICD workflows
- **workflows**: Add workflow that updates GitHub labels
- **workflows**: Add workflow that updates GitHub labels
- **workflows**: Remove step names
- **workflows**: Add workflow that locks PRs and issues
- **workflows**: Update CodeQL
- **workflows**: Update dependency review
- **dependabot**: Update labels
- **pre-commit**: Update hooks
- **dependabot**: Update labels
- **pre-commit**: Remove `mypy` hook
- **pre-commit**: Update Python version
- Update common IDE config
- **pre-commit**: Update hooks

### Documentation

- **README**: Update examples
- **README**: Update notes
- **TEMPLATES**: Improve clarity and consistency
- **CONTRIBUTING**: Improve clarity and consistency
- **README**: Update list of features
- Update license
- Update PyPI classifiers
- **README**: Update installation notes
- **README**: Update badges
- **CHANGELOG**: Remove typo
- **README**: Update badge colors
- **README**: Update badges
- **README**: Update badges
- **README**: Update examples
- **README**: Update badges
- **templates**: Update issue templates
- **templates**: Update PR template
- **README**: Add preview of schema validation
- **README**: Update "Configuration via TOML file" section
- **README**: Update "Features" section
- **README**: Update description of `location` parameter
- **README**: Update TOC
- **README**: Change headers level
- **README**: Change headers level
- **README**: Break parameters description in "Usage and Configuration" section
- **README**: Update "Usage and Configuration" section
- **README**: Update "Features" section
- **CONTRIBUTING**: Update guidelines
- **LICENSE**: Update copyright year
- **CODE_OF_CONDUCT**: Update formatting
- **CHANGELOG**: Update formatting

### Features

- Add back support of the poetry v1.5+
- Remove support of the Python 3.8
- **poetry**: Downgrade `poetry` version
- Add module for custom exceptions
- Add support of `--directory`

### Miscellaneous

- **codespell**: Update config
- **ruff**: Update config
- **semantic-release**: Update config
- Update tooling config
- Update IDE config
- **ruff**: Update config
- **cov**: Update exclusions
- **semantic-release**: Update config
- Remove `memestra`
- **poetry**: Add config
- **poe**: Remove `tests` task
- **ruff**: Update config
- **poe**: Update `format` tasks
- **mypy**: Update config

### Refactor

- Update docstrings for clarity and consistency
- **tests**: Remove redundant docstrings
- Run linters
- **tests**: Run `ruff`
- **plugin**: Optimize code performance
- **logger**: Optimize code performance
- **config**: Optimize code performance
- **dotenv.core**: Optimize code performance
- **dotenv.parsers**: Optimize code performance
- **dotenv.variables**: Optimize code performance
- **plugin**: Add `nocover`
- **dotenv.core**: Add `nocover`
- **dotenv.parsers**: Remove stale `noqa`
- **config**: Use empty string as `location` default value
- **config**: Replace `pathlib` with `os.path`
- **logger**: Reduce code duplication
- Update type annotations

### Testing

- Split tests based on the config source
- Mock IO options

### Style

- **examples**: Update GIF theme
- **examples**: Remove noqa suppressions
- Run formatter
- **labels**: Update formatting

## [2.1.6] - 2024-05-13

### Documentation

- **README**: Update list of features

## [2.1.5] - 2024-05-09

### Documentation

- **assets**: Make logo transparent

## [2.1.4] - 2024-05-08

### Documentation

- **README**: Update badges order
- **README**: Update logo size

## [2.1.3] - 2024-05-08

### Documentation

- **README**: Remove badges
- **assets**: Update logo colors

## [2.1.2] - 2024-05-08

### Documentation

- **README**: Update logo
- **README**: Update logo

## [2.1.1] - 2024-05-07

### Build

- **deps-dev**: Bump poethepoet from 0.26.0 to 0.26.1
- **deps-dev**: Bump commitizen from 3.24.0 to 3.25.0
- **deps-dev**: Bump coverage from 7.5.0 to 7.5.1
- **deps-dev**: Bump ruff from 0.4.2 to 0.4.3

### Documentation

- **README**: Update demo

## [2.1.0] - 2024-05-06

### Bug fixes

- **pypi**: Update classifiers

### CI/CD

- **workflows.cd**: Remove `force` flag

### Miscellaneous

- **commitizen**: Update config

## [2.0.0] - 2024-05-06

### Build

- **poetry**: Update dependencies
- **pre-commit**: Update dependencies
- **deps-dev**: Bump poethepoet from 0.25.1 to 0.26.0
- **deps-dev**: Bump black from 24.4.1 to 24.4.2

### CI/CD

- **workflows.cd**: Temporary set `force` flag for the current release
- **workflows.cd**: Unbound `python-semantic-release` version
- **workflows.cd**: Lock `python-semantic-release` version
- **CHANGELOG**: Update unreleased notes
- **workflows.ci**: Limit dependency installation for semantic release
- **workflows.ci**: Remove Windows from the strategy for tests to run
- **workflows.ci**: Limit dependency installation for tests
- **workflows.ci**: Remove `architecture` parameter
- **workflows.ci**: Add MacOS and Windows into the strategy for tests to run

### Features

- Move `Logger` into a separate module
- **config**: Replace `tomli` with `tomlkit`

### Miscellaneous

- **semantic-release**: Update config
- **semantic-release**: Update config

### Testing

- **plugin**: Replace mock of `tomli` with `tomlkit`

## [1.0.1] - 2024-04-26

### Build

- **deps-dev**: Bump commitizen from 3.22.0 to 3.24.0

### Documentation

- Update demo example

### Miscellaneous

- **commitizen**: Update config

## [1.0.0] - 2024-04-26

### Bug fixes

- **config**: Update attributes getter

### Build

- **pre-commit**: Update hooks
- **deps-dev**: Bump python-semantic-release from 9.4.1 to 9.4.2
- **deps-dev**: Bump black from 24.3.0 to 24.4.0
- **deps-dev**: Bump commitizen from 3.21.3 to 3.22.0
- **deps-dev**: Bump ruff from 0.3.5 to 0.3.7
- **deps-dev**: Bump poethepoet from 0.25.0 to 0.25.1
- **deps**: Bump idna from 3.6 to 3.7

### CI/CD

- **workflows.ci**: Remove `macos` from tests strategy

### Documentation

- **README**: Update phrasing
- **README**: Update `Usage` section
- Add examples

### Miscellaneous

- **ruff**: Update config

### Refactor

- Remove `Self` type annotation

### Testing

- **plugin**: Update section in `_toml_config` tests

## [0.8.4] - 2024-04-11

### Build

- **deps-dev**: Bump deptry from 0.15.0 to 0.16.1
- **deps-dev**: Bump python-semantic-release from 9.4.0 to 9.4.1
- **deps-dev**: Bump ruff from 0.3.4 to 0.3.5
- **deps-dev**: Bump python-semantic-release from 9.3.1 to 9.4.0
- **poetry**: Update dependencies
- **poetry**: Add `ipython`
- **pre-commit**: Update dependencies
- **poetry**: Update dependencies

### CI/CD

- **.gitignore**: Add `.import_linter_cache`

### Documentation

- **README**: Update badges
- Add examples

### Miscellaneous

- **ruff**: Update config
- **ruff**: Update config

### Refactor

- **dotenv**: Update functions signatures
- **tests**: Update functions signatures

### Testing

- **plugin**: Add `_toml_config` tests
- **config**: Add `test__as_bool`
- Update mocks in order to new configuration keys

### Style

- Add "no coverage" for `TYPE_CHECKING` sections

## [0.8.3] - 2024-03-31

### Documentation

- **README**: Update badges

## [0.8.2] - 2024-03-31

### Documentation

- **README**: Update badges

### Miscellaneous

- **codespell**: Update `ignore-words-list`

## [0.8.1] - 2024-03-31

### Documentation

- Move VHS script

## [0.8.0] - 2024-03-31

### Bug fixes

- **README**: Resovle issue with missing assets

## [0.7.0] - 2024-03-31

### Bug fixes

- Update GitHub username
- Update GitHub username

### Build

- **poetry**: Update dependencies

### CI/CD

- Add Python 3.12
- Remove pipeline that check stale branch
- Remove pipeline that check stale PRs
- Disable force version increment
- Update GitHub username

### Documentation

- Update badges
- Update GitHub username
- Update GitHub username

### Features

- **README**: Update headers

### Miscellaneous

- Move assets into own directory
- Update keywords

## [0.6.33] - 2024-03-30

### Build

- **deps-dev**: Bump pytest-mock from 3.12.0 to 3.14.0

## [0.6.32] - 2024-03-30

### Build

- **deps-dev**: Bump pytest-cov from 4.1.0 to 5.0.0

## [0.6.31] - 2024-03-30

### Build

- **deps-dev**: Bump deptry from 0.14.0 to 0.15.0

## [0.6.30] - 2024-03-30

### Build

- **deps-dev**: Bump commitizen from 3.18.0 to 3.20.0

## [0.6.29] - 2024-03-30

### Build

- **deps-dev**: Bump pylsp-rope from 0.1.15 to 0.1.16

## [0.6.28] - 2024-03-18

### Build

- **deps-dev**: Bump deptry from 0.12.0 to 0.14.0

## [0.6.27] - 2024-03-18

### Build

- **deps-dev**: Bump coverage from 7.4.3 to 7.4.4

## [0.6.26] - 2024-03-18

### Build

- **deps-dev**: Bump pylsp-rope from 0.1.11 to 0.1.15

## [0.6.25] - 2024-03-18

### Build

- **deps-dev**: Bump black from 24.2.0 to 24.3.0

## [0.6.24] - 2024-03-18

### Build

- **deps-dev**: Bump python-lsp-server from 1.10.0 to 1.10.1

## [0.6.23] - 2024-03-11

### Build

- **deps**: Bump crs-k/stale-branches from 4.0.1 to 4.1.0

## [0.6.22] - 2024-03-09

### Build

- **pre-commit**: Update dependencies
- **poetry**: Update dependencies
- **poetry**: Add `commitizen`
- **pre-commit**: Update dependencies
- **poetry**: Update dependencies

### Miscellaneous

- **poe**: Add `lint-imports` task
- **poe**: Add `memestra` task
- **poe**: Add `commitizen` task
- **commitizen**: Add config

## [0.6.21] - 2024-03-04

### Build

- **deps**: Bump poetry from 1.8.1 to 1.8.2

## [0.6.20] - 2024-03-04

### Build

- **deps-dev**: Bump ruff from 0.2.2 to 0.3.0

## [0.6.19] - 2024-02-28

### Build

- **deps**: Bump poetry from 1.7.1 to 1.8.1
- **deps-dev**: Bump coverage from 7.4.1 to 7.4.3
- **deps-dev**: Bump python-semantic-release from 9.1.0 to 9.1.1
- **deps**: Bump crs-k/stale-branches from 3.1.4 to 4.0.1

## [0.6.18] - 2024-02-28

### Build

- **deps-dev**: Bump poethepoet from 0.24.4 to 0.25.0

## [0.6.17] - 2024-02-21

### Build

- **deps**: Bump cryptography from 42.0.2 to 42.0.4

## [0.6.16] - 2024-02-19

### Build

- **deps-dev**: Bump python-semantic-release from 9.0.3 to 9.1.0

## [0.6.15] - 2024-02-19

### Build

- **deps-dev**: Bump black from 24.1.1 to 24.2.0

## [0.6.14] - 2024-02-19

### Build

- **deps-dev**: Bump ruff from 0.2.1 to 0.2.2

## [0.6.13] - 2024-02-19

### Build

- **deps-dev**: Bump pyupgrade from 3.15.0 to 3.15.1

## [0.6.12] - 2024-02-12

### Build

- **deps-dev**: Bump python-semantic-release from 8.7.0 to 9.0.3

## [0.6.11] - 2024-02-07

### Build

- **poetry**: Downgrade `pytest`
- **pre-commit**: Update dependencies
- **poetry**: Remove `nitpick`
- **poetry**: Update dependencies

### CI/CD

- **editorconfig**: Add TOML config

### Miscellaneous

- **ruff**: Update config

### Style

- Run formatters

## [0.6.10] - 2024-02-06

### Build

- **deps-dev**: Bump xdoctest from 1.1.2 to 1.1.3

## [0.6.9] - 2024-02-06

### Build

- **deps**: Bump cryptography from 41.0.7 to 42.0.0

## [0.6.8] - 2024-02-05

### Build

- **deps-dev**: Bump pytest-sugar from 0.9.7 to 1.0.0

## [0.6.7] - 2024-02-05

### Build

- **deps**: Bump codecov/codecov-action from 3 to 4

## [0.6.6] - 2024-02-05

### Build

- **deps**: Bump crs-k/stale-branches from 3.0.0 to 3.1.4
- **deps-dev**: Bump ruff from 0.1.14 to 0.2.0

## [0.6.5] - 2024-02-03

### CI/CD

- **workflows**: Update days before stale
- **workflows**: Add workflow that checks stale PRs
- **workflows**: Add workflow that creates issues for branches that have become stale

## [0.6.4] - 2024-01-29

### Build

- **deps-dev**: Bump coverage from 7.4.0 to 7.4.1
- **deps-dev**: Bump black from 23.12.1 to 24.1.1

## [0.6.3] - 2024-01-22

### Build

- **deps-dev**: Bump ruff from 0.1.13 to 0.1.14
- **deps**: Bump actions/dependency-review-action from 3 to 4

## [0.6.2] - 2024-01-12

### CI/CD

- **CD**: Update steps
- **CD**: Update `semantic-release` config

## [0.6.1] - 2024-01-12

### Bug fixes

- Bump version

### Build

- **poetry**: Update `python-semantic-release`
- **poetry**: Add `ruff` formatter
- **pre-commit**: Update hooks
- **deps-dev**: Bump jinja2 from 3.1.2 to 3.1.3
- **deps-dev**: Bump gitpython from 3.1.40 to 3.1.41
- **deps-dev**: Bump ruff from 0.1.9 to 0.1.11
- **deps-dev**: Bump pytest from 7.4.3 to 7.4.4
- **deps-dev**: Bump nitpick from 0.34.0 to 0.35.0
- **deps-dev**: Bump coverage from 7.3.4 to 7.4.0
- **deps-dev**: Bump mypy from 1.7.1 to 1.8.0
- **deps-dev**: Bump black from 23.12.0 to 23.12.1
- **deps-dev**: Bump python-semantic-release from 8.5.1 to 8.7.0
- **deps-dev**: Bump ruff from 0.1.8 to 0.1.9
- **deps-dev**: Bump coverage from 7.3.3 to 7.3.4
- **deps-dev**: Bump black from 23.11.0 to 23.12.0
- **deps-dev**: Bump ruff from 0.1.7 to 0.1.8
- **deps-dev**: Bump isort from 5.13.0 to 5.13.2
- **deps-dev**: Bump python-semantic-release from 8.5.0 to 8.5.1
- **deps-dev**: Bump coverage from 7.3.2 to 7.3.3
- **deps**: Bump github/codeql-action from 2 to 3
- **deps-dev**: Bump isort from 5.12.0 to 5.13.0
- **deps-dev**: Bump python-semantic-release from 8.3.0 to 8.5.0
- **deps-dev**: Bump ruff from 0.1.6 to 0.1.7
- **deps**: Bump cryptography from 41.0.5 to 41.0.6
- **deps-dev**: Bump mypy from 1.7.0 to 1.7.1
- **deps-dev**: Bump ruff from 0.1.5 to 0.1.6
- **deps**: Bump poetry from 1.7.0 to 1.7.1
- **deps-dev**: Bump poethepoet from 0.24.3 to 0.24.4
- **deps-dev**: Bump poethepoet from 0.24.2 to 0.24.3
- **poetry**: Update dependencies
- **poetry**: Update dependencies
- **deps-dev**: Bump ruff from 0.1.1 to 0.1.4
- **deps**: Bump poetry from 1.6.1 to 1.7.0
- **deps-dev**: Bump poethepoet from 0.24.1 to 0.24.2
- **deps-dev**: Bump pytest from 7.4.2 to 7.4.3
- **deps-dev**: Bump black from 23.10.0 to 23.10.1
- **deps-dev**: Bump xdoctest from 1.1.1 to 1.1.2
- **deps-dev**: Bump python-semantic-release from 8.1.2 to 8.3.0
- **deps-dev**: Bump pytest-mock from 3.11.1 to 3.12.0
- **deps-dev**: Bump mypy from 1.6.0 to 1.6.1
- **deps-dev**: Bump black from 23.9.1 to 23.10.0
- **deps-dev**: Bump ruff from 0.0.291 to 0.1.1
- **deps**: Bump urllib3 from 2.0.6 to 2.0.7
- **deps-dev**: Bump python-semantic-release from 8.1.1 to 8.1.2
- **deps-dev**: Bump mypy from 1.5.1 to 1.6.0
- **deps-dev**: Bump pre-commit from 3.4.0 to 3.5.0
- **deps-dev**: Bump poethepoet from 0.24.0 to 0.24.1
- **codespell**: Update ignored files
- **poetry**: Remove `yesqa`
- **deps-dev**: Bump poethepoet from 0.23.0 to 0.24.0
- **deps**: Bump urllib3 from 2.0.4 to 2.0.6
- **deps-dev**: Bump ruff from 0.0.290 to 0.0.291
- **deps-dev**: Bump python-semantic-release from 8.0.8 to 8.1.1
- **deps-dev**: Bump pyupgrade from 3.11.0 to 3.13.0
- **deps-dev**: Bump poethepoet from 0.22.1 to 0.23.0
- **deps**: Bump cryptography from 41.0.3 to 41.0.4
- **deps-dev**: Bump ruff from 0.0.287 to 0.0.290
- **deps-dev**: Bump black from 23.9.0 to 23.9.1
- **deps-dev**: Bump pyupgrade from 3.10.1 to 3.11.0
- **deps-dev**: Bump gitpython from 3.1.32 to 3.1.35
- **deps-dev**: Bump black from 23.7.0 to 23.9.0
- **deps-dev**: Bump pytest from 7.4.1 to 7.4.2
- **deps-dev**: Bump coverage from 7.3.0 to 7.3.1
- **deps-dev**: Bump poethepoet from 0.22.0 to 0.22.1
- **deps-dev**: Bump ruff from 0.0.286 to 0.0.287
- **deps-dev**: Bump pre-commit from 3.3.3 to 3.4.0
- **deps-dev**: Bump pytest from 7.4.0 to 7.4.1
- **deps-dev**: Bump python-semantic-release from 8.0.6 to 8.0.8
- **poetry**: Update dependencies
- **deps-dev**: Bump mypy from 1.5.0 to 1.5.1
- **deps-dev**: Bump poethepoet from 0.21.1 to 0.22.0
- **deps-dev**: Bump python-semantic-release from 8.0.3 to 8.0.6
- **deps-dev**: Bump mypy from 1.4.1 to 1.5.0
- **deps-dev**: Bump ruff from 0.0.282 to 0.0.284
- **deps-dev**: Bump sh from 2.0.4 to 2.0.6
- **deps-dev**: Bump coverage from 7.2.7 to 7.3.0
- **deps-dev**: Bump ruff from 0.0.280 to 0.0.282

### CI/CD

- **CD**: Remove build command
- Update CD workflow
- Update CD workflow
- Update CD workflow
- Update changelog
- Update CD workflow
- Update changelog
- Update semantic release options
- **hooks**: Update revisions

### Documentation

- **README**: Update style of the GitHub stars badge
- Update assets paths
- Update assets directory
- Update contribution guideline
- **README**: Add `pre-commit` badge
- **README**: Add `poetry` badge

### Features

- Bump version
- **README**: Remove link from the logo

### Miscellaneous

- Add dependabot.yml config entry for github actions
- **deps**: Upgrade github actions

### Style

- Remove unused directive
- **ruff**: Remove stale `noqa` comments
- Update `mypy` ignore comments

## [0.5.2] - 2023-08-05

### Build

- **poetry**: Update dependencies
- **deps-dev**: Bump ruff from 0.0.275 to 0.0.280

### CI/CD

- **pre-commit**: Add `deptry`
- **workflows**: Update trigger events
- **CD**: Update `semantic-release`

### Documentation

- **README**: Add "features" section

### Miscellaneous

- Update `codespell` config

### Style

- **docs**: Run formatters

## [0.5.1] - 2023-07-22

### Build

- **poetry**: Lock `python-semantic-release` version
- **deps-dev**: Bump python-semantic-release from 7.34.6 to 8.0.1
- **deps-dev**: Bump poethepoet from 0.20.0 to 0.21.1
- **deps-dev**: Bump black from 23.3.0 to 23.7.0
- **deps-dev**: Bump mypy from 1.4.0 to 1.4.1
- **poetry**: Update dependencies
- **deps-dev**: Bump pyupgrade from 3.6.0 to 3.7.0
- **deps-dev**: Bump pytest-mock from 3.10.0 to 3.11.1
- **deps-dev**: Bump codespell from 2.2.4 to 2.2.5
- **deps-dev**: Bump python-semantic-release from 7.34.3 to 7.34.6
- **deps-dev**: Bump pre-commit from 3.3.2 to 3.3.3
- **deps-dev**: Bump pyupgrade from 3.4.0 to 3.6.0
- **deps-dev**: Bump yesqa from 1.4.0 to 1.5.0
- **deps-dev**: Bump ruff from 0.0.270 to 0.0.272
- **deps-dev**: Bump pytest from 7.3.1 to 7.3.2

### CI/CD

- **cd**: Add `twine`
- **semantic-release**: Update `commit_auther`
- **semantic-release**: Update TOML keys
- **semantic-release**: Update parser options
- **pre-commit**: Update hooks

### Documentation

- Add `wakatime` badge
- Add `wakatime` badge
- Update badges

## [0.5.0] - 2023-06-02

### Build

- **deps-dev**: Bump coverage from 7.2.5 to 7.2.6
- **deps-dev**: Bump python-semantic-release from 7.33.5 to 7.34.1
- **deps-dev**: Bump pytest-cov from 4.0.0 to 4.1.0
- **deps**: Bump requests from 2.30.0 to 2.31.0
- **deps-dev**: Bump sh from 2.0.3 to 2.0.4
- **deps-dev**: Bump python-semantic-release from 7.33.4 to 7.33.5
- **deps**: Bump poetry from 1.4.2 to 1.5.0
- **deps-dev**: Bump pre-commit from 3.3.1 to 3.3.2
- **deps-dev**: Bump mypy from 1.2.0 to 1.3.0
- **deps-dev**: Bump python-semantic-release from 7.33.3 to 7.33.4
- **deps-dev**: Bump deptry from 0.9.0 to 0.11.0
- **deps-dev**: Bump pyupgrade from 3.3.2 to 3.4.0
- **dependencies**: Update dependencies
- **deps-dev**: Bump coverage from 7.2.3 to 7.2.5
- **deps-dev**: Bump python-semantic-release from 7.33.2 to 7.33.3
- **deps-dev**: Bump ipython from 8.12.0 to 8.12.1
- **nitpick**: Add style
- **dependencies**: Update dependencies
- **deps-dev**: Bump pytest from 7.3.0 to 7.3.1
- **deps-dev**: Bump pytest-sugar from 0.9.6 to 0.9.7
- **dependencies**: Update dependencies versions

### CI/CD

- Update hooks
- Update ignored files
- Update classifiers
- **workflows**: Update secrets name

### Documentation

- Resolve invalid names
- Update badges

### Features

- Update linter

### Style

- Apply formatter

## [0.4.1] - 2023-04-07

### Bug fixes

- **docs**: Add demo

### CI/CD

- **workflows**: Update secrets name

## [0.4.0] - 2023-04-07

### Build

- **dependencies**: Update versions
- **dependencies**: Update versions to the latest
- **deps-dev**: Bump mypy from 1.0.1 to 1.1.1
- **deps-dev**: Bump ipdb from 0.13.11 to 0.13.13
- **deps-dev**: Bump black from 22.12.0 to 23.1.0
- **deps-dev**: Bump pytest from 7.2.1 to 7.2.2
- **deps-dev**: Bump mypy from 0.991 to 1.0.1
- **deps-dev**: Bump pre-commit from 3.1.0 to 3.1.1
- **deps**: Bump poetry from 1.3.2 to 1.4.0
- **deps-dev**: Bump pre-commit from 3.0.4 to 3.1.0
- **deps-dev**: Bump coverage from 7.1.0 to 7.2.1
- **deps-dev**: Bump flake8-pytest-style from 1.7.0 to 1.7.2
- **deps-dev**: Bump flake8-pytest-style from 1.6.0 to 1.7.0
- **deps-dev**: Bump ipython from 8.9.0 to 8.10.0
- **deps**: Bump cryptography from 39.0.0 to 39.0.1
- **deps-dev**: Bump pre-commit from 3.0.2 to 3.0.4
- **deps-dev**: Bump xdoctest from 1.1.0 to 1.1.1
- **deps-dev**: Bump python-semantic-release from 7.33.0 to 7.33.1
- **deps-dev**: Bump pre-commit from 3.0.1 to 3.0.2

### Features

- Rename plugin from `poetry-dotenv` to `poetry-plugin-dotenv`

### Miscellaneous

- Exclude `poetry`

## [0.3.0] - 2023-01-29

### Bug fixes

- Update annotations

### Build

- Update configs
- **dependencies**: Add `nitpick`
- Update tasks
- **dependencies**: Update dependencies
- **deps**: Bump poetry from 1.2.2 to 1.3.1

### CI/CD

- Update CI workflow
- Update annotations formatter
- Update CD workflow
- Update CI workflow
- Update Dependabot workflow
- Update CodeQL workflow
- Add GitHub labels
- Update hooks

### Documentation

- Update README
- Refactor changelog
- Update security notes
- Update license
- Update contributing
- Update code of conduct

### Features

- **dependencies**: Add support of the Python 3.11

### Refactor

- Update license

## [0.2.7] - 2022-12-03

### Bug fixes

- **docs**: Update docs

## [0.2.5] - 2022-11-18

### Bug fixes

- **docs**: Update docs
- **dependencies**: Update dependencies
- **dependencies**: Update base Python version

### Documentation

- Update example

## [0.2.4] - 2022-11-16

### Bug fixes

- **plugin**: Update logger

### Build

- **dependencies**: Update `pytest-sugar`
- **dependencies**: Update dependencies
- **dependencies**: Update dependencies

### CI/CD

- **github**: Update workflows
- **workflows**: Update `codeql` versions
- **workflows**: Update actions version

## [0.2.3] - 2022-11-06

### Bug fixes

- Update classifier

### Build

- **dependencies**: Update dependencies

### Documentation

- Update examples
- Add examples
- Update docstrings
- Update toc

### Refactor

- Update coverage
- **docs**: Refactor
- **docs**: Refactor

## [0.2.2] - 2022-10-30

### Bug fixes

- **plugin**: Add debug logger

### Refactor

- **CHANGELOG**: Resolve typos

## [0.2.1] - 2022-10-29

### Bug fixes

- **plugin**: Resolve issue with debug entry

### Build

- **dependencies**: Remove `pytype`
- Add linters

### CI/CD

- Update CodeQL workflow

### Documentation

- **README**: Add overview section
- **README**: Remove LGTM badge
- **README**: Remove redunant char

### Refactor

- **linters**: Update `mypy` task

## [0.2.0] - 2022-10-22

### Bug fixes

- **dotenv**: Resolve issue with `OrderedDict`
- **dotenv**: Update `OrderedDict`
- **dotenv**: Add parsers
- **dotenv**: Update base models to the `dataclasses`
- **dotenv**: Update f-strings arguments
- **dotenv**: Add models of the variables/literals

### Build

- **dependencies**: Remove `poe` plugin
- **tasks**: Add linter tasks
- **dependencies**: Add linters
- Update groups
- Add `pyupgrade`
- Update versions
- **dependencies**: Add `sh` package
- **dependencies**: Remove unnecessary package
- Remove unnecessary package

### CI/CD

- **pre-commit**: Remove `pyupgrade` hook
- **docs**: Remove `readthedocs` config
- **workflows**: Update OS
- **cd**: Remove slack notifications
- **cd**: Update twine entrypoint

### Documentation

- Add logo
- **docstrings**: Update docstrings
- **plugin**: Update docstrings
- **github**: Update homepage
- **github**: Update homepage
- **github**: Update homepage
- **github**: Format template of the feature request
- **github**: Format contributing guide
- **github**: Format changelog
- **github**: Format security
- **github**: Format changelog
- **github**: Update template of the feature request
- **github**: Update template of the bug report
- **github**: Update template of the bug report

### Features

- **plugin**: Add core dotenv functionality
- **dotenv**: Add core
- **dotenv**: Add core IO functionality
- **dotenv**: Add parsers
- **dotenv**: Add core IO functionality

### Miscellaneous

- **dotenv**: Add skeleton of the core
- Add returns
- Reset
- Reset
- Update exclusions
- **flake8**: Update exclusions
- **mypy**: Update target version
- **flake8**: Update exclusions
- **flake8**: Update exclusions
- **mypy**: Add tests dir
- **flake8**: Update exclusions
- **flake8**: Update exclusions

### Refactor

- Refactor
- **dotenv**: Refactor
- Refactor
- **docs**: Refactor
- **plugin**: Remove outdated logic
- **dotenv**: Refactor
- **tests**: Refactor
- **plugin**: Refactor
- **tests**: Fix grammar mistakes
- **changelog**: Refactor

### Testing

- **dotenv**: Add missing tests
- **dotenv**: Add tests for core IO functionality
- **dotenv**: Add tests for parsers
- **dotenv**: Add dotenv file fixture
- **dotenv**: Add tests for variables/literals
- **plugin**: Add cleanup
- **plugin**: Fix issue with fixtures

## [0.1.0] - 2022-09-21

### Build

- **version**: Bumped version
- **dependencies**: Remove docs group
- **tasks**: Update tasks
- **poetry**: Add tasks plugin
- **docs**: Update theme
- **git**: Add fixtures
- Add plugin

### CI/CD

- **version**: Remove version placeholder
- **cd**: Update semantic-release entrypoint
- **cd**: Update semantic-release entrypoint
- **cd**: Change notification settings
- **ci**: Fix issue with tasks
- **cd**: Update jobs
- **pre-commit**: Remove prettier
- **ci**: Update jobs
- **git**: Update ignored files
- **flkae8**: Update exclusions
- **flake8**: Update exclusions
- Add workflows
- **dependencies**: Add dependabot
- **slack**: Add config
- **docs**: Add read-the-docs config

### Documentation

- **sphinx**: Remove docs
- **docstrings**: Update descriptions
- Add PR
- Add funding
- Add feature request
- Add bug report
- Add readme
- Add contributing guidelines
- Add code of conduct
- **ci**: Add changelog
- Add security policy

### Features

- Add plugin

### Miscellaneous

- **dependencies**: Update Poetry (version 1.2.1)
- **dependencies**: Update dev dependencies
- **dependencies**: Add
- **dependencies**: Add lock file
- Add docs
- Add src
- Add tests
- Add base config
- **git**: Add pre-commit config
- **ide**: Update editor configs
- **git**: Update ignored files

### Refactor

- **ci**: Apply formatter
- **plugin**: Apply formatters
- Apply formatters
- **tests**: Remove fixtures

### Testing

- **plugin**: Update exclusions
- **plugin**: Update tests
- **coverage**: Exclude method
- Add test for the plugin with default dotenv location
- Add config

