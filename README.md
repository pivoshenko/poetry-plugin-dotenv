<div align="center">
    <img alt="logo" src="https://github.com/pivoshenko/poetry-plugin-dotenv/blob/main/docs/assets/logo.svg?raw=True" height=200>
</div>

<br>

<p align="center">
    <a href="https://opensource.org/licenses/MIT">
        <img alt="license" src="https://img.shields.io/pypi/l/poetry-plugin-dotenv?logo=opensourceinitiative">
    </a>
    <a href="https://python-poetry.org">
        <img alt="poetry" src="https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json">
    </a>
    <a href="https://pypi.org/project/poetry-plugin-dotenv">
        <img alt="python" src="https://img.shields.io/pypi/pyversions/poetry-plugin-dotenv?logo=python">
    </a>
    <a href="https://pypi.org/project/poetry-plugin-dotenv">
        <img alt="pypi" src="https://img.shields.io/pypi/v/poetry-plugin-dotenv?logo=pypi">
    </a>
    <a href="https://github.com/pivoshenko/poetry-plugin-dotenv/releases">
        <img alt="release" src="https://img.shields.io/github/v/release/pivoshenko/poetry-plugin-dotenv?logo=github">
    </a>
</p>

<p align="center">
    <a href="https://github.com/psf/black">
        <img alt="black" src="https://img.shields.io/badge/code_style-black-black.svg?logo=windowsterminal">
    </a>
    <a href="https://github.com/PyCQA/isort">
        <img alt="isort" src="https://img.shields.io/badge/imports-isort-black.svg?logo=windowsterminal">
    </a>
    <a href="https://beta.ruff.rs/docs/">
        <img alt="ruff" src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json">
    </a>
    <a href="https://mypy.readthedocs.io/en/stable/index.html">
        <img alt="mypy" src="https://img.shields.io/badge/mypy-checked-success.svg?logo=python">
    </a>
    <a href="https://github.com/semantic-release/semantic-release">
        <img alt="semantic_release" src="https://img.shields.io/badge/semantic_release-angular-e10079?logo=semantic-release">
    </a>
</p>

<p align="center">
    <a href="https://github.com/dependabot">
        <img alt="dependabot" src="https://img.shields.io/badge/dependabot-enable-success?logo=Dependabot">
    </a>
    <a href="https://github.com/pivoshenko/poetry-plugin-dotenv/actions/workflows/ci.yaml">
        <img alt="CI" src="https://img.shields.io/github/actions/workflow/status/pivoshenko/poetry-plugin-dotenv/ci.yaml?label=CI&logo=github">
    </a>
    <a href="https://github.com/pivoshenko/poetry-plugin-dotenv/actions/workflows/cd.yaml">
        <img alt="CD" src="https://img.shields.io/github/actions/workflow/status/pivoshenko/poetry-plugin-dotenv/cd.yaml?label=CD&logo=github">
    </a>
    <a href="https://github.com/pivoshenko/poetry-plugin-dotenv/blob/main/.pre-commit-config.yaml">
        <img alt="hooks" src="https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit">
    </a>
    <a href="https://pypi.org/project/poetry-plugin-dotenv">
        <img alt="wheel" src="https://img.shields.io/pypi/wheel/poetry-plugin-dotenv?logo=pypi">
    </a>
</p>

<p align="center">
    <a href="https://codecov.io/gh/pivoshenko/poetry-plugin-dotenv" >
        <img alt="codecov" src="https://codecov.io/gh/pivoshenko/poetry-plugin-dotenv/graph/badge.svg?token=cqRQxVnDR6"/>
    </a>
    <a href="https://codeclimate.com/github/pivoshenko/poetry-plugin-dotenv/maintainability">
        <img alt="codeclimate" src="https://img.shields.io/codeclimate/maintainability/pivoshenko/poetry-plugin-dotenv?logo=codeclimate">
    </a>
    <a href="https://pypi.org/project/poetry-plugin-dotenv">
        <img alt="downloads" src="https://img.shields.io/pypi/dm/poetry-plugin-dotenv?logo=pypi">
    </a>
    <a href="https://github.com/pivoshenko/poetry-plugin-dotenv/">
        <img alt="stars" src="https://img.shields.io/github/stars/pivoshenko/poetry-plugin-dotenv?style=flat&logo=github">
    </a>
</p>

<p align="center">
    <a href="https://stand-with-ukraine.pp.ua/">
        <img alt="standwithukraine" src="https://img.shields.io/badge/Support-Ukraine-FFD500?style=flat&labelColor=005BBB">
    </a>
    <a href="https://stand-with-ukraine.pp.ua">
        <img alt="standwithukraine" src="https://img.shields.io/badge/made_in-Ukraine-ffd700.svg?labelColor=0057b7">
    </a>
</p>

- [Overview](#overview)
  - [Features](#features)
- [Installation](#installation)
- [Usage and Configuration](#usage-and-configuration)
  - [Configuration via file](#configuration-via-file)
  - [Configuration via environment variables](#configuration-via-environment-variables)
  - [Lookup hierarchy](#lookup-hierarchy)
- [Examples](#examples)

## Overview

`poetry-plugin-dotenv` - is the plugin that automatically loads environment variables from a dotenv file into the environment before `poetry` commands are run.

### Features

- Doesn't require any dependencies
- Supports templates, interpolating variables using POSIX variable expansions
- Fully type safe
- 100% test coverage and "A" grade for maintainability

## Installation

```bash
poetry self add poetry-plugin-dotenv
```

## Usage and Configuration

By default, the plugin will load the `.env` file from the current working directory or "higher directories".

To prevent `poetry` from loading the dotenv file, set the `ignore` option.

If your dotenv file is located in a different path or has a different name you may set the `location`.

`ignore` option can accept the next values:
- As True: `y / yes / t / on / 1 / true`
- As False: `n / no / f / off / 0 / false`

### Configuration via file

The plugin is able to read project-specific default values for its options from a `pyproject.toml` file.
By default, `poetry-plugin-dotenv` looks for `pyproject.toml` containing a `[tool.poetry.plugins.dotenv]` section.

Example `pyproject.toml`:

```toml
[tool.poetry.plugins.dotenv]
ignore = "false"
location = ".env.dev"
```

> [!IMPORTANT]
> Due to the default `poetry` parser, options in the plugins sections should be always strings.

### Configuration via environment variables

`poetry-plugin-dotenv` supports the following configuration options via environment variables.

- `POETRY_PLUGIN_DOTENV_LOCATION`
- `POETRY_PLUGIN_DOTENV_IGNORE`

> [!IMPORTANT]
> Due to the nature of environment variables, options should be always strings.

### Lookup hierarchy

A `pyproject.toml` can override default values. Options provided by the user via environment variables override both.

## Examples

<img alt="demo" src="https://github.com/pivoshenko/poetry-plugin-dotenv/blob/main/docs/assets/demo.gif?raw=True">

```dotenv
# .env
DB__HOST=localhost
DB__DBNAME=local_lakehouse
DB__USER=volodymyr
DB__PASSWORD=super_secret_password
DB__ENGINE=postgresql://${DB__USER}:${DB__PASSWORD}@${DB__HOST}/${DB__DBNAME}
```

```dotenv
# .env.dev
DB__HOST=dev.host
DB__DBNAME=dev_lakehouse
DB__USER=svc_team
DB__PASSWORD=super_secret_password
DB__ENGINE=postgresql://${DB__USER}:${DB__PASSWORD}@${DB__HOST}/${DB__DBNAME}
```

```toml
# pyroject.toml
[tool.poetry.plugins.dotenv]
location = ".env.dev"
```

```python
# main.py
from __future__ import annotations

import os


if __name__ == "__main__":
    try:
        print(f"Host: {os.environ['DB__HOST']!r}")  # noqa: T201
        print(f"Name: {os.environ['DB__DBNAME']!r}")  # noqa: T201
        print(f"Username: {os.environ['DB__USER']!r}")  # noqa: T201
        print(f"Password: {os.environ['DB__PASSWORD']!r}")  # noqa: T201
        print(f"Engine: {os.environ['DB__ENGINE']!r}")  # noqa: T201

    except KeyError:
        print("Environment variables not set!")  # noqa: T201
```

```shell
poetry run -vvv python main.py
# Loading environment variables from '.env'.
# Host: 'localhost'
# Name: 'local_lakehouse'
# Username: 'volodymyr'
# Password: 'super_secret_password'
# Engine: 'postgresql://volodymyr:super_secret_password@localhost/local_lakehouse'

# set location section in pyproject.toml
poetry run -vvv python main.py
# Loading environment variables from '.env.dev'.
# Host: 'dev.host'
# Name: 'dev_lakehouse'
# Username: 'svc_team'
# Password: 'super_secret_password'
# Engine: 'postgresql://svc_team:super_secret_password@dev.host/dev_lakehouse'

# set ignore = "true" in pyproject.toml
poetry run -vvv python main.py
# Not loading environment variables.
# Environment variables not set!

export POETRY_PLUGIN_DOTENV_LOCATION=.env.dev && poetry run -vvv python main.py
# Loading environment variables from '.env.dev'.
# Host: 'dev.host'
# Name: 'dev_lakehouse'
# Username: 'svc_team'
# Password: 'super_secret_password'
# Engine: 'postgresql://svc_team:super_secret_password@dev.host/dev_lakehouse'

export POETRY_PLUGIN_DOTENV_IGNORE=true && poetry run -vvv python main.py
# Not loading environment variables.
# Environment variables not set!
```
