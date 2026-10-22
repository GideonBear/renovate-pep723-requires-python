# 40536

Reproduction for [Renovate discussion 40536](https://github.com/renovatebot/renovate/discussions/40536).

## Current behavior

`script.py` has [PEP 723](https://peps.python.org/pep-0723) inline script metadata with a `requires-python` constraint:

```python
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "requests==2.31.0",
# ]
# ///
```

The `pep723` manager only extracts `requests`.
`requires-python` is only used as a constraint (`extractedConstraints.python`), so Renovate never proposes updates for it, even with `rangeStrategy: "bump"` for the `requires-python` depType.

## Expected behavior

Like the `pep621` manager (since [#35534](https://github.com/renovatebot/renovate/pull/35534)), the `pep723` manager extracts `requires-python` as a `python` dependency, with:

- `depType`: `requires-python`
- `datasource`: `python-version`
- `versioning`: `pep440`

With the `packageRules` entry in `renovate.json` (`rangeStrategy: "bump"`), Renovate then proposes updating `>=3.11` to the latest Python version, for example `>=3.15.1`, on the `renovate/python-3.x` branch.
With the default `rangeStrategy`, the dependency is extracted, but `>=3.11` is left as-is because it already allows the latest version, which is also how `pep621` behaves.
