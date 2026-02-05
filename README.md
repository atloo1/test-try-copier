# test-try-copier

[![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/atloo1/test-try-copier/ci.yml)](https://github.com/atloo1/test-try-copier/actions/workflows/ci.yml?query=branch%3Amain)
[![Dynamic TOML Badge](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Fatloo1%2Ftest-try-copier%2Frefs%2Fheads%2Fmain%2Fpyproject.toml&query=%24.project.requires-python&label=python)](https://github.com/atloo1/test-try-copier/blob/main/pyproject.toml)
[![Dynamic TOML Badge](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Fatloo1%2Ftest-try-copier%2Frefs%2Fheads%2Fmain%2Fpyproject.toml&query=%24.project.version&label=version)](https://github.com/atloo1/test-try-copier/blob/main/pyproject.toml)
[![GitHub License](https://img.shields.io/github/license/atloo1/test-try-copier)](https://github.com/atloo1/test-try-copier/blob/main/LICENSE)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/atloo1/test-try-copier)

[![Copier](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-purple.json)](https://github.com/copier-org/copier)
[![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=fff)](https://docs.docker.com/get-started/get-docker/)
[![Checked with mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Renovate enabled](https://img.shields.io/badge/renovate-enabled-brightgreen.svg)](https://renovatebot.com/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)

test updating from try-copier

templated from https://github.com/atloo1/try-copier vTODO

## use

### via [Docker](https://docs.docker.com/get-started/get-docker/)

```
docker build . -t test-try-copier
docker run --name test-try-copier test-try-copier
```

### via Python (via [uv](https://docs.astral.sh/uv/getting-started/installation/))

```
uv run python -m src.test_try_copier.main
```

## develop

### setup (requires [uv](https://docs.astral.sh/uv/getting-started/installation/))

```
git clone https://github.com/atloo1/test-try-copier
cd test-try-copier/
uv sync --group dev
uv run pre-commit install
```

### test locally (preemptively pass the corresponding GitHub action)

```
uv run pytest
```

### update template (requires [copier](https://copier.readthedocs.io/en/stable/#installation), preferably via [uv](https://docs.astral.sh/uv/getting-started/installation/))

```
copier update --defaults --trust
```
