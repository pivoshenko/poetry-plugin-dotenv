<div align="center">
  <img alt="logo" src="https://github.com/pivoshenko/poetry-plugin-dotenv/blob/main/docs/assets/logo.svg?raw=True" height=200>
</div>

<br>

<p align="center">
  <a href="https://opensource.org/licenses/MIT">
    <img alt="License" src="https://img.shields.io/pypi/l/poetry-plugin-dotenv?style=flat-square&logo=opensourceinitiative&logoColor=white&color=0A6847&label=License">
  </a>
  <a href="https://pypi.org/project/poetry-plugin-dotenv">
    <img alt="Python" src="https://img.shields.io/pypi/pyversions/poetry-plugin-dotenv?style=flat-square&logo=python&logoColor=white&color=4856CD&label=Python">
  </a>
  <a href="https://pypi.org/project/poetry-plugin-dotenv">
    <img alt="PyPI" src="https://img.shields.io/pypi/v/poetry-plugin-dotenv?style=flat-square&logo=pypi&logoColor=white&color=4856CD&label=PyPI">
  </a>
  <a href="https://github.com/pivoshenko/poetry-plugin-dotenv/releases">
    <img alt="Release" src="https://img.shields.io/github/v/release/pivoshenko/poetry-plugin-dotenv?style=flat-square&logo=github&logoColor=white&color=4856CD&label=Release">
  </a>
</p>

<p align="center">
  <a href="https://semantic-release.gitbook.io">
    <img alt="Semantic_Release" src="https://img.shields.io/badge/Semantic_Release-angular-e10079?style=flat-square&logo=semanticrelease&logoColor=white&color=D83A56">
  </a>
  <a href="https://pycqa.github.io/isort">
    <img alt="Imports" src="https://img.shields.io/badge/Imports-isort-black.svg?style=flat-square&logo=improvmx&logoColor=white&color=637A9F&">
  </a>
  <a href="https://docs.astral.sh/ruff">
    <img alt="Ruff" src="https://img.shields.io/badge/Style-ruff-black.svg?style=flat-square&logo=ruff&logoColor=white&color=D7FF64">
  </a>
  <a href="https://mypy.readthedocs.io/en/stable/index.html">
    <img alt="mypy" src="https://img.shields.io/badge/mypy-checked-success.svg?style=flat-square&logo=pypy&logoColor=white&color=0A6847">
  </a>
</p>

<p align="center">
  <a href="https://github.com/pivoshenko/poetry-plugin-dotenv/actions/workflows/tests.yaml">
    <img alt="Tests" src="https://img.shields.io/github/actions/workflow/status/pivoshenko/poetry-plugin-dotenv/tests.yaml?label=Tests&style=flat-square&logo=pytest&logoColor=white&color=0A6847">
  </a>
  <a href="https://github.com/pivoshenko/poetry-plugin-dotenv/actions/workflows/linters.yaml">
    <img alt="Linters" src="https://img.shields.io/github/actions/workflow/status/pivoshenko/poetry-plugin-dotenv/linters.yaml?label=Linters&style=flat-square&logo=lintcode&logoColor=white&color=0A6847">
  </a>
  <a href="https://github.com/pivoshenko/poetry-plugin-dotenv/actions/workflows/release.yaml">
    <img alt="Release" src="https://img.shields.io/github/actions/workflow/status/pivoshenko/poetry-plugin-dotenv/release.yaml?label=Release&style=flat-square&logo=pypi&logoColor=white&color=0A6847">
  </a>
  <a href="https://codecov.io/gh/pivoshenko/poetry-plugin-dotenv" >
    <img alt="Codecov" src="https://img.shields.io/codecov/c/gh/pivoshenko/poetry-plugin-dotenv?token=cqRQxVnDR6&style=flat-square&logo=codecov&logoColor=white&color=0A6847&label=Coverage"/>
  </a>
</p>

<p align="center">
  <a href="https://pypi.org/project/poetry-plugin-dotenv">
    <img alt="Downloads" src="https://img.shields.io/pypi/dm/poetry-plugin-dotenv?style=flat-square&logo=pythonanywhere&logoColor=white&color=4856CD&label=Downloads">
  </a>
  <a href="https://github.com/pivoshenko/poetry-plugin-dotenv">
    <img alt="Stars" src="https://img.shields.io/github/stars/pivoshenko/poetry-plugin-dotenv?style=flat-square&logo=apachespark&logoColor=white&color=4856CD&label=Stars">
  </a>
</p>

<p align="center">
  <a href="https://stand-with-ukraine.pp.ua">
    <img alt="StandWithUkraine" src="https://img.shields.io/badge/Support-Ukraine-FFC93C?style=flat-square&labelColor=07689F">
  </a>
  <a href="https://stand-with-ukraine.pp.ua">
    <img alt="StandWithUkraine" src="https://img.shields.io/badge/Made_in-Ukraine-FFC93C.svg?style=flat-square&labelColor=07689F">
  </a>
</p>

- [Overview](#overview)
  - [Features](#features)
- [Installation](#installation)
- [Usage and Configuration](#usage-and-configuration)
    - [`ignore`](#ignore)
    - [`location`](#location)
  - [Configuration via TOML file](#configuration-via-toml-file)
  - [Configuration via environment variables](#configuration-via-environment-variables)
  - [Lookup hierarchy](#lookup-hierarchy)
- [Examples](#examples)

## Overview

`poetry-plugin-dotenv` - is the plugin that automatically loads environment variables from a dotenv file into the environment before `poetry` commands are run.

### Features

- Fully type-safe
- No external dependencies required
- Supports templates and variable interpolation using POSIX variable expansions
- Supports `--directory`, which allows setting the working directory for the `poetry` command
- Supports multiple configuration sources
- Provides configuration auto-completion and validation in IDEs like Visual Studio Code or PyCharm (via [JSON Schema Store](https://www.schemastore.org/json))
- Supports both `poetry v1.5+` and `poetry v2+`

## Installation

```bash
poetry self add poetry-plugin-dotenv@latest
```
> [!TIP]
> New releases support only Python 3.9+.
> If you want to use `poetry-plugin-dotenv` with Python 3.8, please install version `2.4.0` using
> `poetry self add poetry-plugin-dotenv@2.4.0`

## Usage and Configuration

By default, the plugin will load the `.env` file from the current working directory or any higher-level directories.

#### `ignore`

**Type**: `str`

**Default**: `false`

**Allowed values (as True)**: `y / yes / t / on / 1 / true`

**Allowed values (as False)**: `n / no / f / off / 0 / false`

Prevents `poetry` from loading the dotenv file.

#### `location`

**Type**: `str`

**Default**: `.env`

If your dotenv file is located elsewhere or has a different name, you can set this parameter.

### Configuration via TOML file

The plugin can read project-specific default values for its options from a `pyproject.toml` file.
By default, `poetry-plugin-dotenv` looks for a `pyproject.toml` file that includes either a `[tool.dotenv]` or `[tool.poetry.plugins.dotenv]` section.

Example `pyproject.toml`:

```toml
[tool.dotenv]
ignore = "false"
location = ".env.dev"

[tool.poetry.plugins.dotenv]
ignore = "false"
location = ".env.dev"
```

> [!WARNING]
> In upcoming poetry releases, the `[tool.poetry.plugins]` section will be deprecated. Please migrate to `[tool.dotenv]`.

> [!IMPORTANT]
> Due to `poetry`'s default parser, all options in the plugin sections must be specified as strings.

As mentioned in the **Features** list, the schema for the plugin configuration is part of the [JSON Schema Store](https://www.schemastore.org/json), which enables auto-completion and validation in IDEs like Visual Studio Code and PyCharm.

<div align="center">
  <img alt="logo" src="https://github.com/pivoshenko/poetry-plugin-dotenv/blob/main/docs/assets/schema_example.png?raw=True">
</div>

### Configuration via environment variables

`poetry-plugin-dotenv` supports the following configuration options via environment variables:

- `POETRY_PLUGIN_DOTENV_LOCATION`
- `POETRY_PLUGIN_DOTENV_IGNORE`

> [!IMPORTANT]
> As environment variables are always strings, options should always be set as strings.

### Lookup hierarchy

A `pyproject.toml` file can override default values. Options provided via environment variables override both.

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
# pyproject.toml
[tool.dotenv]
location = ".env.dev"
```

```python
# main.py
from __future__ import annotations

import os


if __name__ == "__main__":
    try:
        print(f"Host: {os.environ['DB__HOST']!r}")
        print(f"Name: {os.environ['DB__DBNAME']!r}")
        print(f"Username: {os.environ['DB__USER']!r}")
        print(f"Password: {os.environ['DB__PASSWORD']!r}")
        print(f"Engine: {os.environ['DB__ENGINE']!r}")

    except KeyError:
        print("Environment variables not set!")
```

```shell
poetry run -vvv python main.py
# Loading environment variables: .env
# Host: 'localhost'
# Name: 'local_lakehouse'
# Username: 'volodymyr'
# Password: 'super_secret_password'
# Engine: 'postgresql://volodymyr:super_secret_password@localhost/local_lakehouse'

# Set location section in pyproject.toml
poetry run -vvv python main.py
# Loading environment variables: .env.dev
# Host: 'dev.host'
# Name: 'dev_lakehouse'
# Username: 'svc_team'
# Password: 'super_secret_password'
# Engine: 'postgresql://svc_team:super_secret_password@dev.host/dev_lakehouse'

# Set ignore = "true" in pyproject.toml
poetry run -vvv python main.py
# Not loading environment variables. Ignored by configuration
# Environment variables not set!

export POETRY_PLUGIN_DOTENV_LOCATION=.env.dev && poetry run -vvv python main.py
# Loading environment variables: .env.dev
# Host: 'dev.host'
# Name: 'dev_lakehouse'
# Username: 'svc_team'
# Password: 'super_secret_password'
# Engine: 'postgresql://svc_team:super_secret_password@dev.host/dev_lakehouse'

export POETRY_PLUGIN_DOTENV_IGNORE=true && poetry run -vvv python main.py
# Not loading environment variables. Ignored by configuration
# Environment variables not set!
```
