default:
    @just --list

install:
    poetry install --all-groups --all-extras

format:
    find . -type f -name '*.py' -not -path '*/.venv/*' | xargs uvx pyupgrade --py310-plus
    uvx ruff check --fix .
    uvx ruff format .

lint:
    uvx ruff check .
    uvx ruff format --check .
    uvx ty check

test:
    @[ -f .no-tests ] && echo "skipping (.no-tests sentinel)" || uvx pytest

check: lint test

update:
    poetry update

audit:
    uvx pip-audit
