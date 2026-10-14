# Exercises — 03-13-05 Packaging and Distributing a Python Library

Attempt these **closed-book** before opening the
[solutions](./05-packaging-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems marked **[demo]** refer to
[`../code/packaging_demo.py`](../code/packaging_demo.py):

```
.venv/bin/python 03-scientific-computing/13-testing-profiling-packaging/code/packaging_demo.py
```

The lesson is [`../05-packaging.md`](../05-packaging.md).

---

## ★ Foundational

**★1. [demo]** The demo reports, on this machine:

```
  sys.prefix       = /Users/.../geophysics/.venv
  sys.base_prefix  = /opt/homebrew/opt/python@3.14/Frameworks/Python.framework/Versions/3.14
  running in a venv: True
  stdlib directory = /opt/homebrew/opt/python@3.14/.../lib/python3.14
  EXTERNALLY-MANAGED present: True
  marker format   = INI, section [externally-managed], key Error
```

(a) A student's wrapper script refuses to install anything because the marker
file exists. Explain the bug in the script and state the correct predicate.
(b) Name the correct three-command workflow that installs a project's
requirements into an isolated environment.
(c) State what `--break-system-packages` does and why it is not the answer to the
student's problem.

**★2. [demo]** The specifier table is

| specifier | 1.24.4 | 2.5.4 | 2.6.0 | 3.0.0 |
|---|---|---|---|---|
| `==2.5.4` | no | yes | no | no |
| `>=1.26,<3` | no | yes | yes | no |
| `~=2.5.0` | no | yes | no | no |
| `~=2.5` | no | yes | yes | no |

(a) State what `~=2.5` expands to, in `>=`/`==` form.
(b) State what `~=2.5.0` expands to.
(c) A colleague writes `numpy~=2.5` intending "NumPy 2.5.x only". Explain the
error and give the specifier they meant.

**★3.** Name the four tables of a `pyproject.toml` from Section 2 of the lesson,
and for each say in one clause what it declares.

---

## ★★ Applied

**★★4.** Write the `[project]` table for a library called `gravtools` version
`0.4.0` that requires Python 3.11 or newer, depends on `numpy>=1.26,<3` and
`scipy>=1.11`, offers a `test` extra with `pytest>=8`, exposes a console script
`grav=` calling `gravtools.cli:main`, and configures pytest with
`addopts = "-ra --strict-markers"`. State which PEP each part comes from.

**★★5. [demo]** The audit reports:

```
  requirements.txt: 33 requirements
  satisfied: 25   version-mismatch: 0   not installed: 8
    MISSING  pyrocko>=2024.1
    MISSING  simpeg>=0.21
    MISSING  ruff>=0.4
    MISSING  mypy>=1.10
```

(a) Explain why "0 mismatches, 8 absences" is a more useful report than
"8 problems".
(b) `ruff>=0.4` and `mypy>=1.10` are declared. Measured earlier in this module,
`code/code_quality_demo.py` can still demonstrate both tools' function class.
Explain what it is demonstrating and what it is not.
(c) A student installs `simpeg` and re-runs the audit. Which number changes, and
which should they check before believing the install succeeded?

**★★6.** A wheel is a ZIP archive. Using the layout in Section 4 of the lesson:

(a) List the four files inside the `.dist-info` directory and say what each is
for.
(b) Explain why `RECORD` is what makes `pip uninstall` complete.
(c) Explain why a package with a compiled extension cannot ship a single wheel
for all users.

---

## ★★★ Research-oriented

**★★★7.** A paper's methods section says: "We used NumPy and SciPy with recent
versions; code is available at the repository."

(a) State three distinct reasons this is not a reproducibility statement.
(b) Rewrite it as three sentences that would be.
(c) Explain what a lock file adds beyond the rewritten statement, and what
remains unpinned even then.

**★★★8.** You must publish `gravtools` so that a colleague can `pip install` it
from the internet, and the lesson says nothing was published here.

(a) List, in order, the steps that would be required, naming the artefact each
step produces.
(b) State which step is irreversible in practice, and why.
(c) State the three checks you would run before the irreversible step, and what
each one catches.

**★★★9.** The lesson argues that the flat layout is a hazard and that
`src/` removes it.

(a) Explain the mechanism by which a flat layout lets a test pass against
uninstalled source.
(b) This repository has neither layout, and its `code/` tests import their
neighbour module successfully. Name the mechanism that makes that work, and why
it is fragile.
(c) State what a `src/` layout forces a CI job to do that a flat layout lets it
skip, and why that is a feature.
