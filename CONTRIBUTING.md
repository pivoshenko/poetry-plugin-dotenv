# Contributing

- [Contributing](#contributing)
  - [Reporting Bugs](#reporting-bugs)
    - [How to Submit a Bug Report](#how-to-submit-a-bug-report)
  - [Suggesting Enhancements](#suggesting-enhancements)
    - [How to Submit an Enhancement](#how-to-submit-an-enhancement)
  - [Code Contributions](#code-contributions)
    - [Local Development](#local-development)
    - [CI/CD](#cicd)
    - [Branches](#branches)
    - [Commits](#commits)
    - [Pull Requests](#pull-requests)

Thank you for taking the time to contribute.

These guidelines are intended to make contributions consistent and easy to review across repositories. They are guidance, not hard instructions, and maintainers may adapt them when needed.

## Reporting Bugs

Before creating a bug report, search existing issues to avoid duplicates.

When opening a bug report, include enough context for someone else to reproduce the issue and understand the impact.

> [!NOTE]
> If you find a closed issue that looks similar, open a new issue and link the previous one.

### How to Submit a Bug Report

Open a bug report and provide the following:

- A clear, descriptive title
- Reproduction steps (minimal and reliable if possible)
- Current behavior and expected behavior
- Relevant environment details (for example OS, runtime, browser, framework versions)
- Logs, stack traces, screenshots, or recordings when useful

If the issue is intermittent, describe how often it happens and known triggers.
If the issue appeared after a change, mention the last known working version or commit if available.

## Suggesting Enhancements

Before submitting an enhancement, check whether a similar request already exists.

Enhancement requests can include new features, changes to existing behavior, usability improvements, or performance improvements.

### How to Submit an Enhancement

Open a feature request and provide the following:

- A clear problem statement
- The proposed solution
- Alternatives considered or current workarounds
- Expected impact (who benefits and how)

Concrete examples, API sketches, UI mockups, or references are helpful when relevant.

## Code Contributions

### Local Development

This repo needs Python 3.14, [Poetry](https://python-poetry.org) for dependency management, [uv](https://docs.astral.sh/uv) for the `uvx` tooling, and `just`.

This project uses [`just`](https://github.com/casey/just) as its task runner. Run `just --list` for the full set; these are the ones you need day to day:

| Command | What it does |
| --- | --- |
| `just install` | Installs the project with every dependency group and extra |
| `just format` | Upgrades Python syntax in place with pyupgrade, then applies Ruff autofixes and formatting |
| `just lint` | Lints the project with Ruff and type-checks it with ty |
| `just test` | Runs the test suite with pytest, skipped when the `.no-tests` sentinel is present |
| `just check` | Runs `lint` then `test` in sequence |
| `just update` | Upgrades locked dependencies |

1. Fork the repository and clone your fork locally
2. Create a branch using the naming pattern described below
3. Make your changes, then run `just check` before opening a pull request

> [!IMPORTANT]
> Behavioral code changes should include or update tests.

### CI/CD

Workflows live in `.github/workflows`:

| Workflow | Trigger | What it does |
| --- | --- | --- |
| CI | Push to `main`, pull requests, `workflow_dispatch` | Single `ci` job on `ubuntu-24.04-arm`; sets up just, Python 3.14, Poetry and uv, then installs the project, lints it and runs the test suite |
| Release | `workflow_dispatch` (optional `version` input) | Three chained jobs, all on `ubuntu-24.04-arm`: `tag` resolves the next version from the `version` input or from the commit history via git-cliff, bumps the version in `pyproject.toml`, regenerates `CHANGELOG.md`, then commits and pushes `main` with the new tag; `release` (needs `tag`) publishes the GitHub Release with the generated notes as its body; `publish` (needs `tag` and `release`) builds the package and uploads it to PyPI with OIDC trusted publishing |

CI must be green before a pull request is merged.

### Branches

Branch names follow the pattern `<type>/<short-description>` using the same type prefixes as commits.
The description should be lowercase kebab-case, brief, and specific enough to identify the change at a glance.

Examples:

```
feat/github-token-refresh
fix/private-repo-archive-auth
docs/update-sync-flow-diagram
refactor/mcps-schema-alignment
```

A branch covering multiple unrelated changes should be split. One concern per branch makes review and bisect much easier.

### Commits

Use clear, focused commits with descriptive messages.

This project follows [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/).

**Format**

```
<type>(<scope>): <subject>

[optional body]
```

- **type** - one of the prefixes from the table below
- **scope** - the module, command, or area being changed (e.g. `sync`, `mcps`, `github`, `landing`, `config`); omit when the change is truly cross-cutting
- **subject** - imperative mood, lowercase, no trailing period, 72 characters or fewer
- **body** - optional; use it to explain *why*, not *what*; wrap at 72 characters

**Type prefixes**

| Prefix     | When to use                                                                                             |
| ---------- | ------------------------------------------------------------------------------------------------------- |
| `feat`     | A new feature or user-facing capability                                                                 |
| `fix`      | A bug fix that corrects incorrect behavior                                                              |
| `docs`     | Changes to documentation only (README, comments, guides)                                                |
| `refactor` | Code restructuring that does not change external behavior (renaming, extracting functions, simplifying) |
| `test`     | Adding, updating, or fixing tests without changing production code                                      |
| `chore`    | Maintenance tasks that don't affect source code or tests (dependency bumps, config tweaks, .gitignore)  |
| `ci`       | Changes to CI/CD configuration and scripts (GitHub Actions, workflows, pipelines)                       |
| `build`    | Changes to the build system or external dependencies (Cargo.toml, build scripts, Makefile)              |
| `perf`     | A code change that improves performance without altering functionality                                  |
| `style`    | Formatting-only changes (whitespace, semicolons, linting) with no logic changes                         |
| `design`   | Changes to visual or UI design assets and layout                                                        |
| `revert`   | Reverts a previous commit (reference the reverted commit hash in the body)                              |

**Examples**

```
feat(sync): support skills source sub-directory selection
fix(github): url-encode git refs in API tarball endpoint
refactor(mcps): align mcps[] schema with skills[]
docs(config): document browser URL auto-rewriting for --config
```

### Pull Requests

- Fill out the pull request template completely
- Keep the pull request focused and scoped to one change set
- Ensure tests and checks pass before requesting review
- Update documentation when behavior or interfaces change
- Respond to review feedback and keep the branch up to date with the target branch

Maintainers may ask for changes, additional tests, or scope adjustments before merging.
