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
  <a href="https://github.com/semantic-release/semantic-release">
    <img alt="Semantic_Release" src="https://img.shields.io/badge/Semantic_Release-angular-e10079?style=flat-square&logo=semanticrelease&logoColor=white&color=D83A56">
  </a>
  <a href="https://github.com/PyCQA/isort">
    <img alt="Imports" src="https://img.shields.io/badge/Imports-isort-black.svg?style=flat-square&logo=improvmx&logoColor=white&color=637A9F&">
  </a>
  <a href="https://beta.ruff.rs/docs/">
    <img alt="Ruff" src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json&style=flat-square&logoColor=white&color=637A9F">
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
  <a href="https://github.com/pivoshenko/poetry-plugin-dotenv/">
    <img alt="Stars" src="https://img.shields.io/github/stars/pivoshenko/poetry-plugin-dotenv?style=flat-square&logo=apachespark&logoColor=white&color=4856CD&label=Stars">
  </a>
</p>

<p align="center">
  <a href="https://stand-with-ukraine.pp.ua/">
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

- Fully type safe
- Doesn't require any dependencies
- Supports templates, interpolating variables using POSIX variable expansions
- Supports `--directory` - working directory for the `poetry` command
- Supports multiple configuration sources
- Supports configuration auto-completion and validation in IDEs such as Visual Studio Code or PyCharm (part of [JSON Schema Store](https://www.schemastore.org/json))
- Supports both `poetry v1.5+` and `poetry v2+`

## Installation

```bash
poetry self add poetry-plugin-dotenv@latest
```
> [!TIP]
> New releases supports only Python 3.9+.
> If you want to use `poetry-plugin-dotenv` with Python 3.8 please install version `2.4.0` using
> `poetry self add poetry-plugin-dotenv@2.4.0`

## Usage and Configuration

By default, the plugin will load the `.env` file from the current working directory or "higher directories".

#### `ignore`

**Type**: `str`

**Default**: `false`

**Allowed values (as True)**: `y / yes / t / on / 1 / true`

**Allowed values (as False)**: `n / no / f / off / 0 / false`

Prevents `poetry` from loading the dotenv file.

#### `location`

**Type**: `str`

**Default**: `.env`

If your dotenv file is located in a different path or has a different name you may set this parameter.

### Configuration via TOML file

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

As it was mentioned in the **Features** list, the schema of the plugin configuration is now part of the [JSON Schema Store](https://www.schemastore.org/json) which brings auto-completion and validation in IDEs such as Visual Studio Code or PyCharm "out of the box".

https://github.com/pivoshenko/poetry-plugin-dotenv/assets/40499728/15d3a988-a723-49f8-960d-f91cd6bfe536

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
