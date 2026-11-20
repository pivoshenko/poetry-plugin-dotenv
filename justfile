default:
    @just --list

install: install-package

install-package:
    poetry install --all-groups --all-extras

format: format-package

format-package:
    poetry run ruff check --fix .
    poetry run ruff format .

lint: lint-package

lint-package:
    poetry run ruff check .
    poetry run ty check .

audit: audit-package

# pipefail so a failed export cannot hand pip-audit an empty list and pass
audit-package:
    #!/usr/bin/env bash
    set -euo pipefail
    uvx --from poetry --with poetry-plugin-export poetry export --format requirements.txt --all-groups --all-extras \
      | uvx pip-audit --requirement /dev/stdin --require-hashes --disable-pip

test: test-package

test-package:
    @[ -f .no-tests ] && echo "skipping (.no-tests sentinel)" || poetry run pytest .

check: lint test

update: update-package

update-package:
    poetry update
