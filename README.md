[![Python Code Quality](https://github.com/danimarin24/python-ci/actions/workflows/code-quality.yml/badge.svg?branch=main)](https://github.com/danimarin24/python-ci/actions/workflows/code-quality.yml)

## python-ci

Opinionated Python CI template using `uv`, `ruff`, `pyright`, `pytest`, and GitHub Actions.

### What it runs
- **Lock**: `uv lock --locked`
- **Lint**: `uvx ruff check .`
- **Format check**: `uvx ruff format --check .`
- **Types**: `uv run pyright .`
- **Tests + Coverage**: `uv run pytest -v --durations=0 --cov --cov-report=xml`
- **Build**: `uv build`

### Local dev
```bash
uv python pin 3.13
uv sync

# Run the same checks locally
uvx ruff check .
uvx ruff format --check .
uv run pyright .
uv run pytest -v --durations=0 --cov --cov-report=xml
uv build
```

### Notes
- CI workflow: `.github/workflows/code-quality.yml`
