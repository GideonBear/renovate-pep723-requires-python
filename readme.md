# 40536

Reproduction for [Renovate discussion 40536](https://github.com/renovatebot/renovate/discussions/40536).

## Files

`script.py` has [PEP 723](https://peps.python.org/pep-0723) inline script metadata (`pep723` manager):

```python
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "requests==2.31.0",
# ]
# ///
```

`pyproject.toml` has the same metadata in [PEP 621](https://peps.python.org/pep-0621) format (`pep621` manager), for comparison:

```toml
[project]
name = "example"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = [
  "requests==2.31.0",
]
```

`renovate.json`:

- enables the `pep723` manager for `*.py` files (it is opt-in)
- only enables the `pep621` and `pep723` managers, because otherwise the `poetry` manager supersedes `pep621` for a `pyproject.toml` without a lock file
- sets `rangeStrategy: "bump"` for the `requires-python` depType, so that `>=3.11` gets updated

## Current behavior

- `pyproject.toml` (`pep621`): `requires-python` is extracted as a `python` dependency (since [#35534](https://github.com/renovatebot/renovate/pull/35534)), and Renovate proposes `>=3.11` → `>=3.15.1` on the `renovate/python-3.x` branch.
- `script.py` (`pep723`): only `requests` is extracted.
  `requires-python` is only used as a constraint (`extractedConstraints.python`), so Renovate never proposes an update for it.

## Expected behavior

`script.py` (`pep723`) behaves the same as `pyproject.toml` (`pep621`): `requires-python` is extracted as a `python` dependency, with:

- `depType`: `requires-python`
- `datasource`: `python-version`
- `versioning`: `pep440`

Renovate then proposes `>=3.11` → `>=3.15.1` on the `renovate/python-3.x` branch for both files.
