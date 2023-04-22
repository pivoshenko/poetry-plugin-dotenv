# Contributing

- [Contributing](#contributing)
  - [Reporting Bugs](#reporting-bugs)
    - [How Do I Submit a Bug Report?](#how-do-i-submit-a-bug-report)
  - [Suggesting Enhancements](#suggesting-enhancements)
    - [How Do I Submit an Enhancement Suggestion?](#how-do-i-submit-an-enhancement-suggestion)
  - [Contributing to Code](#contributing-to-code)
    - [Dependencies](#dependencies)
    - [Code Formatters](#code-formatters)
    - [Linters](#linters)
    - [Tests](#tests)
    - [Pre-Commit](#pre-commit)
    - [Commits](#commits)
    - [Pull Requests](#pull-requests)

First off, thanks for taking the time to contribute!

The following is a set of guidelines for contributing to `poetry-plugin-dotenv`. These are mostly guidelines,
not rules. Use your best judgement, and feel free to propose changes to this document in a pull
request.

## Reporting Bugs

This section guides you through submitting a bug report for `poetry-plugin-dotenv`. Following these guidelines
helps maintainers and the community understand your report, reproduce the behaviour, and find
related reports.

Before creating bug reports, please check this list to be sure that you need to create one. When you
are creating a bug report, please include as many details as possible. Fill out
the [required template][bug_report] the information it asks helps the maintainers resolve the issue
faster.

> **Note:** If you find a **Closed** issue that seems like it is the same thing that you're
> experiencing, open a new issue and include a link to the original issue in the body of your new
> one.

### How Do I Submit a Bug Report?

Bugs are tracked on the [issue tracker][issues] where you can create a new one and provide
the following information by filling in [the template][bug_report].

Explain the problem and include additional details to help maintainers reproduce the problem:

- **Use a clear and descriptive title** for the issue to identify the problem.
- **Describe the exact steps which reproduce the problem** in as many details as possible.
- **Provide your `pyproject.toml` file** in a [gist][gist] after removing
  potential private information.
- **Provide specific examples to demonstrate the steps to reproduce the issue**. Include links to
  files or GitHub projects, or "copy-paste-able" snippets, which you use in those examples.
- **Describe the behavior you observed after following the steps** and point out what exactly is the
  problem with that behavior.
- **Explain which behavior you expected to see instead and why.**

Provide more context by answering these questions:

- Did the problem start happening recently or was this always a problem?
- If the problem started happening recently, can you reproduce the problem in an older version?
- What's the most recent version in which the problem does not happen?
- Can you reliably reproduce the issue? If not, provide details about how often the problem happens
  and under which conditions it normally happens.

Include details about your configuration and environment.

## Suggesting Enhancements

This section guides you through submitting an enhancement suggestion for `poetry-plugin-dotenv`, including
completely new features and minor improvements to existing functionality. Following these guidelines
helps maintainers and the community understand your suggestion and find related suggestions.

Before creating enhancement suggestions, please check this list as you might find out that you don't
need to create one. When you are creating an enhancement suggestion, please include as many details
as possible. Fill in [the template][feature_request], including the steps that you imagine you would
take if the feature you're requesting existed.

### How Do I Submit an Enhancement Suggestion?

Enhancement suggestions are tracked on the [issue tracker][issues] where you can create a new one
and provide the following information:

- **Use a clear and descriptive title** for the issue to identify the suggestion.
- **Provide a step-by-step description of the suggested enhancement** in as many details as possible.
- **Provide specific examples to demonstrate the steps**.
- **Describe the current behavior** and **explain which behavior you expected to see instead** and why.

## Contributing to Code

### Dependencies

We use `poetry` to manage the [dependencies][poetry].

To install them and activate `virtualenv` you will need to run commands:

```bash
poetry install
poetry bash
```

### Code Formatters

To format code you will need to run command:

```bash
poetry format
```

### Linters

To lint code you will need to run command:

```bash
poetry lint
```

### Tests

To run unit tests:

```bash
poetry tests
```

### Pre-Commit

To make sure that you don't accidentally commit code that does not follow the coding style, you can
install a [`pre-commit`][pre-commit] hook that will check that everything is in order:

```bash
poetry run pre-commit install
```

You can also run it anytime using:

```bash
poetry run pre-commit run --all-files
```

Your code must always be accompanied by corresponding tests, if tests are not present your code will
not be merged.

### Commits

As a standard of commit messages we are using **[conventional commits][commits]**.

### Pull Requests

- Fill in [the required template][pull_request_template].
- Be sure that your pull request contains tests that cover the changed or added code.
- If your changes warrant a documentation change, the pull request must also update the
  documentation.

> **Note:** Make sure your branch is [rebased][rebased] against the latest `main` branch. A
> maintainer might ask you to ensure the branch is up-to-date
> prior to merging your PR if changes have conflicts. All pull requests, unless otherwise
> instructed, need to be first accepted into the `main` branch.

[bug_report]: https://github.com/volopivoshenko/poetry-plugin-dotenv/blob/main/.github/ISSUE_TEMPLATE/bug_report.md

[issues]: https://github.com/volopivoshenko/poetry-plugin-dotenv/issues

[gist]: https://gist.github.com

[feature_request]: https://github.com/volopivoshenko/poetry-plugin-dotenv/blob/main/.github/ISSUE_TEMPLATE/feature_request.md

[poetry]: https://github.com/python-poetry/poetry

[pre-commit]: https://pre-commit.com

[commits]: https://www.conventionalcommits.org/en/v1.0.0

[pull_request_template]: https://github.com/volopivoshenko/poetry-plugin-dotenv/blob/main/.github/PULL_REQUEST_TEMPLATE.md

[rebased]: https://docs.github.com/en/free-pro-team@latest/github/using-git/about-git-rebase
