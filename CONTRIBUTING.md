# Contributing

- [Contributing](#contributing)
  - [Reporting Bugs](#reporting-bugs)
    - [How Do I Submit a Bug Report?](#how-do-i-submit-a-bug-report)
  - [Suggesting Enhancements](#suggesting-enhancements)
    - [How Do I Submit A Suggested Enhancement?](#how-do-i-submit-a-suggested-enhancement)
  - [Code Contributions](#code-contributions)
    - [Local Development](#local-development)
    - [Commits](#commits)
    - [Pull Requests](#pull-requests)

First, thank you for taking the time to contribute!

The following guidelines are for contributing to `poetry-plugin-dotenv`. These are mostly guidelines, not strict rules. Use your best judgment, and feel free to propose changes to this document in a pull request.

## Reporting Bugs

This section guides you through submitting a bug report for `poetry-plugin-dotenv`. Following these guidelines will help maintainers and the community understand your report, reproduce the behavior, and find related reports.

Before submitting bug reports, please check if your issue already exists in the issue tracker. When creating a bug report, please include as many details as possible. Filling out the required template will help maintainers resolve the issue faster.

> [!NOTE]
> If you find a **Closed** issue that seems like the one you're experiencing, open a new issue and include a link to the original issue in the body.

### How Do I Submit a Bug Report?

Bugs concerning `poetry-plugin-dotenv` should be submitted to the main issue tracker, using the appropriate issue template.

Please follow these steps to explain the problem clearly and make it easier for others to search for and understand:

- Use a clear and descriptive title to identify the issue
- Describe the exact steps to reproduce the problem in as much detail as possible
- Explain the observed behavior after following the steps, and how it indicates a bug
- Describe the expected behavior and why you think the current behavior is incorrect
- If the problem involves an unexpected error, run the problematic command in debug mode with the `-vvv` flag

Provide detailed steps to reproduce your issue:

- Provide your `pyproject.toml` file in a [Gist](https://gist.github.com) or an example repository, ensuring private information (like private package repositories or names) is removed
- Provide specific examples, such as an example repository or a sequence of steps in a container, to demonstrate the problem
- If the issue is not consistently reproducible, explain how often it occurs and under which conditions

Additional context can help:

- Did the problem start after an update (e.g., to a new version of `poetry-plugin-dotenv`), or was it always present?
- If the problem started recently, can you reproduce it in an older version? Which version was the last working one?
- Are there any unusual aspects of your environment (e.g., special container images or Apple Silicon CPUs)?

Include details about your environment:

- Which version of `poetry` and `poetry-plugin-dotenv` are you using?
- Which version of Python is being used?
- What’s the name and version of your operating system?

To help others understand and reproduce your issue, provide thorough reproduction steps. If possible, ensure others can reproduce the issue in a pristine container or VM and share the steps you performed in that environment.

## Suggesting Enhancements

This section provides guidance on submitting enhancement suggestions for `poetry-plugin-dotenv`, including entirely new features and improvements to existing functionality. Following these guidelines will help maintainers and the community understand your suggestion and identify related suggestions.

Before creating an enhancement suggestion, please check this list to see if your suggestion already exists. When submitting an enhancement, include as many details as possible, and fill out the template with steps you would take if the requested feature were implemented.

### How Do I Submit A Suggested Enhancement?

Enhancement suggestions should be submitted to the main issue tracker, using the appropriate issue template.

- Use a clear and descriptive title for the suggestion
- Provide a detailed description of the proposed enhancement, with specific steps or examples when possible
- Describe the current behavior and explain the behavior you would like to see, and why

## Code Contributions

### Local Development

First, fork the `poetry-plugin-dotenv` repository and clone it locally to make pull requests against the project.

If you're new to `git` and pull request-based development, GitHub offers a helpful [guide](https://docs.github.com/en/get-started/quickstart/contributing-to-projects).

Next, install Poetry’s dependencies and run the test suite to ensure everything is working as expected:

```shell
poetry install
poetry tests
```

When contributing to Poetry, automated tools will be run to ensure your code is mergeable. You must make sure your code passes type checks and is formatted properly:

```shell
poetry format
poetry lint
```

> [!IMPORTANT]
> Your code must always be accompanied by corresponding tests. Code without tests will not be merged.

### Commits

We follow the [conventional commit message syntax](https://www.conventionalcommits.org/en/v1.0.0). For example: `feat: allow provided config object to extend other configs`.

Every feature branch that is squashed onto the `main` branch must follow these rules. The benefits include:

- A standardized way of writing commit messages for all contributors
- Quick identification of what a commit does and which parts of the project it affects
- Automatic changelog generation based on these keywords

Supported keywords (heavily inspired by [`config-conventional`](https://github.com/conventional-changelog/commitlint/tree/master/%40commitlint/config-conventional)):

- `ci`
- `chore`
- `docs`
- `feat`
- `fix`
- `perf`
- `refactor`
- `revert`
- `style`
- `test`

Additionally, all commit messages must be written in lowercase.

> [!NOTE]
> All commits in a pull request are squashed when merged into the `main` branch. This means only the commit message of the squashed branch must follow the conventional commit format. You do not need to follow this convention for commits within a branch, which may include multiple `wip` commits.

### Pull Requests

- Fill out the pull request description completely and accurately, ensuring it reflects the final changes and potential changelog entry
- Ensure your pull request includes tests that cover the changed or added code. Code without tests will not be merged
- Make sure your pull request passes all checks. You can run these tools locally to verify this
- If your changes affect the documentation, ensure the pull request also updates the documentation. Review the documentation preview generated by CI for any rendering issues

> [!NOTE]
> Make sure your branch is rebased against the latest `main` branch. Maintainers may ask you to update your branch before merging (especially if there have been CI changes on `main`), and to resolve any conflicts.

All pull requests will be accepted into the `main` branch unless otherwise instructed. Maintainers will decide if backports to other branches are needed and will handle them accordingly.
