# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Poetry plugin that automatically loads environment variables from `.env` files before Poetry commands execute. Also provides an `activate` command that loads env vars then spawns a shell. Zero external runtime dependencies beyond Poetry itself.

## Commands

```bash
# Install dependencies
poetry install

# Run tests (pytest with coverage)
just test

# Run linters (ty type checker + ruff)
just lint

# Run formatters (pyupgrade + ruff format)
just format

# Run a single test
poetry run pytest tests/path/test_file.py::test_name -v

# Update dependencies
just update
```

## Architecture

The plugin hooks into Poetry's event system via Cleo's `COMMAND` event:

```
DotenvPlugin (plugin.py)
├── Event listener: intercepts all commands except `activate`
│   └── loader.load() → Configurator → DotEnv → sets env vars
└── Command factory: registers `activate` command
    └── ActivateCommand (commands.py) → loads env vars then os.execvp() into shell
```

**Configuration flow** (`configurator.py`): Environment variables > `[tool.dotenv]` in pyproject.toml > `[tool.poetry.plugins.dotenv]` > defaults. Config fields: `ignore` (bool) and `location` (list of paths, default `.env`).

**Dotenv parsing pipeline** (`dotenv/`):
- `parsers.py`: `Reader` streams characters → `parse_stream()` yields `Binding` objects (key-value pairs with metadata)
- `variables.py`: Resolves POSIX variable expansions (`${VAR:-default}`) into `Variable`/`Literal` atoms
- `core.py`: `DotEnv` class orchestrates parsing, interpolation via `resolve()`, and environment injection

## Code Conventions

- All modules require `from __future__ import annotations`
- Line length: 100 characters
- Type hints required everywhere; checked with `ty`
- Ruff handles both linting and formatting
- Coverage target: 90%
- Conventional Commits: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`, `ci`, `build`, `perf`, `style`, `revert`

## Testing

Tests mirror source structure under `tests/`. Key patterns:
- Temporary `.env` files via `create_dotenv_file`/`dotenv_file` fixtures in `conftest.py`
- Mocked Poetry events and IO objects via `pytest-mock`
- `@mock.patch.dict(os.environ)` for environment variable isolation
- Parametrized tests for config source variants (`test_plugin_toml_config.py`, `test_plugin_os_config.py`)
- `--basetemp=tests/fixtures` for temp file location
