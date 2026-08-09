# Contributing

Thank you for taking the time to contribute.

These guidelines keep contributions consistent and easy to review. They are guidance, not hard rules, and maintainers may adapt them when needed.

## Reporting Bugs

Before creating a bug report, search existing issues to avoid duplicates.

When opening a bug report, include enough context for someone else to reproduce the issue and understand the impact.

> [!NOTE]
> If you find a closed issue that looks similar, open a new issue and link the previous one.

### How To Submit a Bug Report

Open a bug report and include:

- A clear, descriptive title
- Reproduction steps (minimal and reliable if possible)
- Current behavior and expected behavior
- Relevant environment details (OS, Python version, `poetry` version)
- Logs, stack traces, or screenshots when useful

If the issue is intermittent, describe how often it happens and known triggers.
If the issue appeared after a change, mention the last known working version or commit if available.

## Suggesting Enhancements

Before submitting an enhancement, check whether a similar request already exists.

Enhancement requests can include new features, changes to existing behavior, usability improvements, or performance improvements.

### How To Submit an Enhancement

Open a feature request and include:

- A clear problem statement
- The proposed solution
- Alternatives considered or current workarounds
- Expected impact (who benefits and how)

Concrete examples or references help when relevant.

## Code Contributions

### Local Development

1. Fork the repository and create a branch for your change.
2. Install the project with `just install`.
3. Run `just check` (lint and tests) before opening a pull request.

The `justfile` is the entry point for every task runner command in this repository.

> [!IMPORTANT]
> Behavioral code changes should include or update tests.

### Branches

Branch names follow the pattern `<type>/<short-description>` using the same type prefixes as commits.
The description should be lowercase kebab-case, brief, and specific enough to identify the change at a glance.

Examples:

```
feat/activate-command-fish-support
fix/relative-location-resolution
docs/update-lookup-hierarchy
refactor/configurator-source-order
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

- **type**: one of the prefixes from the table below
- **scope**: the module, command, or area being changed (e.g. `plugin`, `loader`, `configurator`, `deps`, `ci`); omit when the change is truly cross-cutting
- **subject**: imperative mood, lowercase, no trailing period, 72 characters or fewer
- **body**: optional; use it to explain *why*, not *what*; wrap at 72 characters

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
| `build`    | Changes to the build system or external dependencies (pyproject.toml, poetry.lock, justfile)            |
| `perf`     | A code change that improves performance without altering functionality                                  |
| `style`    | Formatting-only changes (whitespace, semicolons, linting) with no logic changes                         |
| `design`   | Changes to visual or UI design assets and layout                                                        |
| `revert`   | Reverts a previous commit (reference the reverted commit hash in the body)                              |

**Examples**

```
feat(commands): support fish in the activate command
fix(loader): resolve relative location against the working directory
refactor(configurator): align config source precedence
docs(readme): document the lookup hierarchy
```

### Pull Requests

- Fill out the pull request template completely
- Keep the pull request focused and scoped to one change set
- Ensure tests and checks pass before requesting review
- Update documentation when behavior or interfaces change
- Respond to review feedback and keep the branch up to date with the target branch

Maintainers may ask for changes, additional tests, or scope adjustments before merging.
