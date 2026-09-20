# CLAUDE.md

`poetry-plugin-dotenv` is a **Poetry application plugin** published to PyPI. It hooks Poetry's console `COMMAND` event and loads a dotenv file into `os.environ` before any `poetry` command runs, and registers one extra command, `poetry activate`, which loads the dotenv file and then replaces the process with a shell inside the activated virtualenv.

It is a plugin, not an app - there is nothing to run locally except the test suite.

`AGENTS.md` is a symlink to this file - edit `CLAUDE.md`, never `AGENTS.md`.

## Invariants

- **Zero runtime dependencies besides `poetry` itself.** `tomlkit` and `cleo` come transitively from Poetry. This is a headline feature of the project; do not add a runtime dependency without a very good reason
- **`just lint` rewrites files** despite its name - `[tool.ruff]` sets `fix = true` and `unsafe-fixes = true`. It is not a read-only check
- the lint tools are invoked through `uvx`, so they resolve from `~/.cache/uv`, not from `.venv`. `poetry install` is still needed for `just test`, since `poetry_plugin_dotenv.__init__` reads its own version through `importlib.metadata` and fails on import if the package is not installed
- **Never hand-edit the version** in `pyproject.toml` or `CHANGELOG.md` - the `Release` workflow resolves and writes both with `git-cliff`
- `src/poetry_plugin_dotenv/dotenv/` is a **fork of `python-dotenv`**, vendored to avoid a runtime dependency. Keep its structure recognisable against upstream so fixes can be ported, and do not restructure it opportunistically
- type checking is `ty` (Astral), **not mypy**
- `README.md` is the user-facing source of truth for configuration options - update it whenever `ignore`/`location` behaviour changes. The configuration schema is published to the [JSON Schema Store](https://www.schemastore.org/json), so a schema change needs a PR there too
- CI runs a single job with no matrix across Python or Poetry versions, so compatibility with the declared floors is only checked by review

`just check` (lint then test) before opening a PR. Recipe table in `CONTRIBUTING.md`, or `just --list`.

## Version Targets

These now agree: the manifest declares a 3.9 floor, and `[tool.ty.environment]`, `[tool.ruff] target-version` and `just format`'s `pyupgrade --py39-plus` all target 3.9. `.python-version`, CI and `CONTRIBUTING.md` run 3.14, and the classifiers list 3.9 through 3.14.

So code is written and checked against 3.9 syntax. **Do not use 3.10+ syntax** - `target-version = "py39"` is set explicitly so ruff's autofix stops rewriting `Optional[Union[...]]` into PEP 604 unions the 3.9 floor cannot evaluate - and keep the Poetry-facing code working on both `poetry v1.5+` and `poetry v2+` - that dual support is an advertised feature.

## Tests

`tests/` mirrors the source layout; `tests/dotenv/` covers the vendored parser and carries most of the assertions.

Repo-specific quirks that will bite you:

- `pyproject.toml` sets `--basetemp=tests/fixtures`, so pytest's `tmp_path` lives **inside the repo**, not in `/tmp`. `tests/fixtures` is gitignored; it accumulates junk and is safe to delete
- `conftest.create_dotenv_file` writes to `tmp_path / ".." / ".." / ".."` - that resolves to the **repository root**. Plugin-level tests really do create `.env` / `.env.dev` at the root and delete them afterwards. A crashed test can leave one behind, which then silently affects the next run
- config-source tests use `@mock.patch.dict(os.environ, {...}, clear=True)` and `@mock.patch("tomlkit.load", return_value=...)` rather than fixture files - follow that pattern for new config cases
- loading mutates the real `os.environ` for the whole session; assert on the specific key you set, never on environment emptiness

## Smoke-Testing a Change by Hand

The plugin only executes inside a host Poetry installation, so the working tree has to be installed into one:

```shell
poetry self add "$PWD"                          # from the repo root
cd docs/examples
cp configs/pyproject.toml pyproject.toml        # untracked - delete it when done
poetry run -vvv python main.py
poetry self remove poetry-plugin-dotenv
```

`-v` is mandatory: every plugin message is logged at `Verbosity.VERBOSE`, and the plugin runs before the main command, so without it there is no output at all. `configs/` holds the `location` and `ignore` variants; `demo.tape` drives the same sequence for the VHS recording.

## Architecture

Runtime flow, all under `src/poetry_plugin_dotenv/`:

```
plugin.py       DotenvPlugin.activate() registers a COMMAND listener + the `activate` command
  -> logging.Logger(event)        writes through cleo io at Verbosity.VERBOSE
  -> configurator.Config(cwd)     resolves ignore/location from all config sources
  -> loader.load(...)             picks the filepaths, then calls dotenv.core.load per file
       -> dotenv/                 vendored parser + interpolation
```

- `configurator.Config.__init__` walks `CONFIG_SOURCES` **in order, each updating over the last**, so precedence is: `[tool.poetry.plugins.dotenv]` < `[tool.dotenv]` < `POETRY_PLUGIN_DOTENV_*` env vars. Values arrive as strings (Poetry's TOML parser and `os.environ` both give strings), so `_as_bool` maps `y/yes/t/on/1/true` and their negatives, and `_as_paths` splits on commas - `location` therefore accepts a comma-separated list of dotenv files, which the README does not mention
- `commands.ActivateCommand` `os.execvp`s a shell, so **the function never returns**; the trailing `return 0` is unreachable and every path is `# pragma: no cover`

## Conventions

- new files start with `from __future__ import annotations`; typing-only imports go under `if typing.TYPE_CHECKING:  # pragma: no cover`
- isort is configured for one import per line, shortest-first within a block - match the existing `import typing` / `import pathlib` ordering rather than alphabetising
- numpydoc-flavoured docstrings on public classes and modules; plain functions need none
- per-file ignores live in `[tool.ruff.lint.per-file-ignores]` - add there rather than scattering `# noqa`
- the package ships `py.typed`; keep annotations complete
- Conventional Commits, branches named `<type>/<kebab-description>` - see `CONTRIBUTING.md`
