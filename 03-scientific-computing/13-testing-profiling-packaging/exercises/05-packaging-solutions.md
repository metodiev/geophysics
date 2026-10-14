# Solutions — 03-13-05 Packaging and Distributing a Python Library

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output; derived values are shown with the arithmetic
> that produced them.

---

## ★1 — The PEP 668 marker and the venv predicate

**(a)** The script tests *whether the marker file exists*, which is true inside a
virtual environment as well, because a venv shares the base installation's
standard library and the marker lives there. The measured output shows both facts
at once: `EXTERNALLY-MANAGED present: True` and `running in a venv: True`. pip
does not test the file; it tests the venv predicate
`sys.prefix != sys.base_prefix`. The correct check in a wrapper script is

```python
in_venv = sys.prefix != sys.base_prefix
if not in_venv:
    raise SystemExit("refusing to install into the base interpreter; use a venv")
```

**(b)**

```bash
python3 -m venv .venv
.venv/bin/python -m pip install --upgrade pip
.venv/bin/python -m pip install -r requirements.txt
```

**(c)** It instructs pip to ignore the externally-managed marker and install into
the system interpreter anyway. It is not the answer because the marker exists to
protect a shared interpreter: installing a package that upgrades or shadows one
of the operating system's own dependencies produces a broken system update weeks
later, in a place with no obvious connection to the research code. The cost of
avoiding it is one command, and the benefit is an environment that can be
deleted, archived and reproduced.

---

## ★2 — Compatible-release specifiers

**(a)** `~=2.5` means `>=2.5, ==2.*` — the *major* version is pinned because the
release segment given has one component, and the minor may float. Measured
behaviour: 2.6.0 satisfies it, 3.0.0 does not.

**(b)** `~=2.5.0` means `>=2.5.0, ==2.5.*` — the major *and* minor are pinned
because two components were given. Measured: 2.5.4 satisfies it, 2.6.0 does not.

**(c)** `~=2.5` is much wider than "2.5.x": it admits every 2.x release from 2.5
upward, including a 2.9 that may change a numerical default. The specifier they
meant is `~=2.5.0`, and the general rule is that the operator pins the last
component *written*, so the number of dots is the whole message. This is a
genuine and common error, and it is why the lesson's table is worth reproducing
against your actual pinned version rather than trusting memory.

---

## ★3 — The four tables

| table | declares |
|---|---|
| `[build-system]` | what must be installed to build (`requires`) and which backend implements the hooks (`build-backend`) — PEP 518/517 |
| `[project]` | the distribution's metadata: name, version, description, `requires-python`, `dependencies`, optional extras, entry points, URLs — PEP 621 |
| `[tool.<name>]` | configuration for each tool (pytest, ruff, mypy, coverage), so one file describes the package and its checks |
| `[dependency-groups]` / lock inputs (or an extras section, by convention) | development-only dependencies that are not shipped to users |

The fourth row is the least standardised of the four; the lesson's sample uses
`[project.optional-dependencies]` for the same purpose, which is the
universally understood form.

---

## ★4 — A `[project]` table

```toml
[build-system]
requires = ["hatchling>=1.24"]
build-backend = "hatchling.build"

[project]
name = "gravtools"
version = "0.4.0"
description = "Gravity reduction and anomaly utilities"
requires-python = ">=3.11"
dependencies = [
  "numpy>=1.26,<3",
  "scipy>=1.11",
]

[project.optional-dependencies]
test = ["pytest>=8"]

[project.scripts]
grav = "gravtools.cli:main"

[tool.pytest.ini_options]
addopts = "-ra --strict-markers"
```

Provenance: `[build-system]` is PEP 518 (the requirements) plus PEP 517 (the
backend interface); everything under `[project]` is PEP 621, including the
`optional-dependencies` extras and the `scripts` entry points; `[tool.*]` is a
convention established by `pyproject.toml`'s design rather than a single PEP, and
each tool documents which table it reads. Note `requires-python`, not
`python_requires` — the underscore is the `setup.py` spelling, and mixing them is
a common porting error that produces a silent no-op.

---

## ★5 — Auditing a declaration

**(a)** Because the two categories require different actions. An **absence** means
the environment cannot run some lesson yet, and the fix is to install the package;
it is a preparation gap with no bearing on the correctness of anything already
run. A **mismatch** means the environment has a version that contradicts the
declaration, and the fix is to decide which is right — an installed version that
does not satisfy the declaration can silently change a numerical result. Merging
them into "8 problems" would hide the fact that nothing present is wrong.

**(b)** It is demonstrating the *class of check* — unused imports, mutable
defaults, bare excepts, shadowed builtins, argument counts, annotation
introspection — reimplemented with `ast` and `dis`, which are in the standard
library. It is **not** demonstrating `ruff` or `mypy`: a real linter has hundreds
of rules, per-project configuration, autofix, and years of accumulated edge-case
handling, and a real type checker resolves the whole program's interfaces across
files. The seven checks in the demo establish that the *concept* is reachable
without dependencies; they are not a substitute, and the lesson says so
explicitly.

**(c)** The `not installed` count falls from 8 to 7 (and `satisfied` rises from 25
to 26) if the requirement carries no version constraint; if it does carry one, a
new `version-mismatch` may appear instead. Before believing the install
succeeded, they should re-run the audit and check *which* number moved: a
satisfied count that rose with a `version-mismatch` appearing means an
incompatible version was installed, and pip's success message says nothing about
that. This is the same distinction as (a), used as a verification step.

---

## ★6 — Inside a wheel

**(a)** The four `.dist-info` files:

| file | purpose |
|---|---|
| `METADATA` | the PEP 621 fields as key/value headers, plus `Requires-Dist` and `Requires-Python` |
| `WHEEL` | the wheel format version, the generator, and the compatibility tags (`py3-none-any` for pure Python) |
| `RECORD` | `path, sha256=<digest>, size` for every installed file |
| `entry_points.txt` | console scripts and plugin hooks, which is how `[project.scripts]` reaches `PATH` |

**(b)** Because `RECORD` is the only complete inventory of what the install
*wrote*. Uninstall cannot discover files by looking at the package directory —
data files, compiled extensions, generated scripts and the `.dist-info` itself all
live outside it, and some names are rewritten during install. Reading the manifest
removes exactly those files and leaves everything else alone, which is why
`pip uninstall` is safe on a shared environment and why `pip check` can verify an
installation against its recorded hashes.

**(c)** Because the compiled code is machine-dependent in two ways at once: the
**ABI** (which CPython version and which ABI flags the extension was built
against) and the **platform** (CPU architecture, operating system, C library).
A single wheel would have to contain every binary, which is what a source
distribution does instead — and building from source requires a compiler,
development headers and, often, a Fortran toolchain. This is why NumPy publishes a
matrix of wheels, and why the conda path exists for platforms whose wheels are
missing.

---

## ★7 — Rewriting a reproducibility statement

**(a)** Three distinct reasons:

1. **"Recent versions" is not a version.** A reader cannot install it, and a
   minor release can change a numerical default or a reduction order.
2. **"The repository" is not a revision.** Without a tag or hash, the code
   changes underneath the citation; see the git lesson.
3. **The environment is only one of three obligations.** Nothing is said about
   the Python interpreter, the platform, or the data — and the data is usually
   the thing most likely to be missing.

**(b)** A statement with the same content and no holes:

> "The analysis used CPython 3.14.8 in a virtual environment; the exact package
> versions are pinned in `requirements.lock` (sha256 fingerprint
> `e7ef1812…`) and were installed with `pip install --require-hashes`. The code is
> at tag `v1.2.0`, commit `494c6712f94b6ac8355ca64f08f7e7532c5239d6`. The input
> catalogue was fetched on 2026-07-14 with `scripts/fetch_catalogue.py`; the
> response digest is `sha256:408c5bf4…`."

**(c)** A lock file adds the *exact distribution bytes* for every transitive
dependency, which the statement's pins alone do not: two environments with
`numpy==2.5.4` may differ in BLAS, SIMD baseline or wheel provenance. What
remains unpinned even then, measured in this module: the interpreter patch
version unless pinned separately, the BLAS build, the platform and architecture,
the thread count, and the operating system kernel. Those are the facts Section 4
of the lesson measures rather than asserts, and a statement that claims
bit-for-bit reproducibility without them is over-claiming.

---

## ★8 — Publishing, in order

**(a)**

| # | step | artefact produced |
|---|---|---|
| 1 | choose a name and check it is free on the index | a name that is not squatted |
| 2 | write `pyproject.toml` with a version and metadata | declarative metadata |
| 3 | `python -m build` | `dist/*.whl` and `dist/*.tar.gz` |
| 4 | install both in a clean venv and run the tests | evidence the artefact works as built |
| 5 | `twine check dist/*` | metadata validity for the index |
| 6 | `twine upload --repository testpypi dist/*` | a rehearsal on a scratch index |
| 7 | install from TestPyPI in another clean venv | evidence the published artefact installs |
| 8 | `twine upload dist/*` | the public release, irreversibly |
| 9 | tag the commit, archive to a DOI, add `CITATION.cff` | a citable release |

Steps 3–8 were **not** performed here, and this environment is offline; the table
is the documented sequence, not a measurement.

**(b)** Step 8. A public index does not permit re-uploading a version number
after deletion, and mirrors and caches may retain the artefact even after the
canonical copy is removed. A mistake at that point can be corrected only by
releasing a new version, and a malicious or broken release that was briefly
available imposes a permanent cost on users who pinned it.

**(c)** Three checks before the irreversible step: **(i)** install both the wheel
and the sdist into a *fresh* environment and run the test suite — catches a
missing package data file, a `src/` layout mistake, and a dependency omitted from
`dependencies`; **(ii)** `twine check` on both artefacts — catches a malformed or
incomplete `METADATA` that the index would reject or, worse, accept with the
wrong fields; **(iii)** install the rehearsal release from TestPyPI and import it —
catches the class of error where the artefact is well-formed and simply does not
work when installed rather than checked out.

---

## ★9 — Layout

**(a)** With the flat layout the package directory sits in the project root, which
is also the current working directory when you run pytest or a script. Python puts
the current directory (or, under pytest's import mode, the test file's directory)
on `sys.path`, so `import gravtools` resolves to the *source directory* whether or
not the package is installed. Tests therefore pass against source. The failure
appears only when the installed artefact is tested: a missing subpackage, a data
file not included by the build configuration, or an entry point that was declared
but never generated — none of which the source tree can exhibit.

**(b)** pytest's default `prepend` import mode inserts each test file's directory
at the front of `sys.path` before importing it, which is why
`test_pytest_basics.py` imports `geophys_tools` from the same directory with no
`PYTHONPATH`, no `conftest.py` and no install. It is fragile because that
behaviour is a pytest *mode* rather than a property of the code: it changes with
`--import-mode=importlib`, it does not happen at all when the test file is run
with `python` directly, and it means the test exercises an import path that no
user of the code will ever have. It also fails outright if two test files in
different directories share a module name — a collision `src/` and a single
installed package make impossible.

**(c)** A `src/` layout forces the CI job to **install the package** before the
tests can import anything, i.e. to run the same build path a user runs:

```yaml
      - run: python -m pip install -e .[test]
      - run: python -m pytest -q
```

That is a feature twice over. It makes the CI job test the packaging
configuration on every push, so a broken `[tool.hatch.build]` include list fails
in a pull request rather than at release time; and it makes "works on my machine"
and "works in CI" exercise the same installation, which is the property a
reproducibility argument needs.
