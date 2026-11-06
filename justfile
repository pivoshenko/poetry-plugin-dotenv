default:
    @just --list

install:
    poetry install --all-groups --all-extras

format:
    poetry run ruff check --fix .
    poetry run ruff format .

lint:
    poetry run ruff check .
    poetry run ty check .

test:
    @[ -f .no-tests ] && echo "skipping (.no-tests sentinel)" || poetry run pytest .

check: lint test

update:
    poetry update
