# Python DevOps Sample Project

This repository was created for a Grad­u­ate Sem­i­nar at the [Department of Atmospheric and Cryospheric Sciences (ACINN)](https://www.uibk.ac.at/en/acinn/) in Innsbruck on May 8th 2024. It serves as a dummy [PyPI package](https://pypi.org/project/velosaurus-calc/) to demonstrate some modern DevOps practices.

- Collaboration (Scrum)
- AI supported development
- Git / PR / Code Review
- CI/CD (Pipelines / IaC)
- UnitTests / Static Linter

## Prerequisites

### Setup Python Environment

```bash
# Create/activate/deactivate venv
python -m venv venv
.\venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux
.\venv\Scripts\deactivate

# Install packages with activated env and check
python -m pip install --upgrade pip
pip install --upgrade -r ./requirements.txt 
pip list
```

## Unit Testst

```bash
python -m unittest discover -s tests -p 'test_*.py'
```

## Generate and test python package locally

```bash
python setup.py sdist bdist_wheel
pip install dist/velosaurus_sum-1.0.4-py3-none-any.whl
```

## Tools

- ruff (linter, formatter)
- mypy (type annotation linter)
  - if **Extension** installed, add rule: Search for mypy in Settings and ad "Mypy-type-checker args": ``"python.linting.mypyArgs": [     "--ignore-missing-imports" ]``
- autoDocstring - Python Docstring Generator
- Jupyter and Python plugins

todo:

- pytest and coverage
- pre-commit instead pipeline test/linter runs

### ruff and mypy

Tools can be applied manualle in console or automatically in pipeline on commit/PR. Configuration for manual/local usage is done in **settings.json**. Configuration for pipeline/build-tool usage is done via **pyproject.toml**.

Use Ruff instead of flake8 (linter), black (formatter) and isort (import sorter) separately.

- in root foler: `python .\run_ruff.py`

- **ruff** (linter / formatter)
  - `ruff check .`   ...basic check (linter)
  - `ruff check --fix .` ...fix basic issues (linter)
  - `ruff format --diff .` (show diffs)
  - `ruff format --check .` (show files)
  - `ruff format .` (apply formatter)

- **mypy** (static type annotations)
  - `mypy --exclude venv .`
