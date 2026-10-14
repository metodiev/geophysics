---
id: 03-13-05
title: "Packaging and Distributing a Python Library"
level: advanced
prereqs: ["03-13-04", "03-13-01"]
estimated_minutes: 110
tags: [packaging, pyproject-toml, pep517, pep518, pep621, pep668, versioning, venv]
---

# Packaging and Distributing a Python Library

A geophysical research group writes a gravity-processing library. It works on
the machine of the person who wrote it. A year later a new student clones the
repository, runs `pip install -e .`, and is told
`error: externally-managed-environment`. Nothing is broken; the student has met
PEP 668, and the message is the operating system telling them that the system
interpreter is not theirs to modify.

This lesson is about the machinery that turns a directory of modules into
something another person can install and cite: `pyproject.toml` and its four
tables, the PEP 517/518 build protocol, PEP 621 metadata, version specifiers and
why pinning matters for reproducible science, editable installs, and the
externally-managed rule that catches nearly every newcomer. Every claim that can
be checked from inside a running interpreter is checked by
`code/packaging_demo.py`; nothing is installed, built, published or downloaded.

## Learning objectives

By the end of this lesson you will be able to:

1. **Explain** PEP 668, what the `EXTERNALLY-MANAGED` marker does, and why a
   virtual environment is the correct answer rather than an inconvenience.
2. **Write** a `pyproject.toml` with `[build-system]` and `[project]` tables,
   and say what PEP 517, 518 and 621 each contribute.
3. **Evaluate** a version specifier against a set of candidate versions, and
   choose between pinning and a range with a stated justification.
4. **Describe** what a wheel contains, what `.dist-info/RECORD` is for, and why
   a compiled extension forces a per-platform wheel.
5. **Distinguish** an editable install from a regular one, and say when each is
   appropriate.
6. **State** what a lock file changes about reproducibility, and what remains
   unpinned even then.

## Prerequisites

- [03-13-04 Linting, Formatting, Type Hints and Static Analysis](./04-code-quality.md)
  — the `[tool.*]` tables in `pyproject.toml` configure exactly those tools.
- [03-13-01 pytest: Tests, Fixtures, Parametrisation and Approximate Comparisons](./01-pytest-basics.md)
  — an installed package is what CI installs before it can test anything.

## 1. PEP 668, or why the first command fails

The base interpreter in this repository's environment is PEP 668
externally managed: `pip install` into it is refused. That is not a
misconfiguration to work around; it is the packaging ecosystem's answer to a real
problem.

An operating system ships Python to run its own tooling. On macOS that includes
Homebrew's formula tooling; on Debian it includes `apt`'s helpers. If a user
runs `pip install` against that interpreter, pip installs a package that
shadows or upgrades one of the OS's own dependencies, and the next system update
breaks — often in a way that looks like a Python bug but is a packaging
collision. PEP 668 standardises the refusal.

The mechanism is simple enough to read. The interpreter's standard library
directory contains a marker file,
`<stdlib>/EXTERNALLY-MANAGED`, in INI format with a single section and a single
key. Measured on this machine, the file resolves to

```
  stdlib directory = /opt/homebrew/opt/python@3.14/.../lib/python3.14
  EXTERNALLY-MANAGED present: True
  marker format   = INI, section [externally-managed], key Error
  Error= first line = 'To install Python packages system-wide, try brew install'
```

pip reads that key and refuses, unless told to override with
`--break-system-packages`.

### 1.1 A subtlety worth seeing once

The measurement above reports `EXTERNALLY-MANAGED present: True` **while running
inside a virtual environment**, because a venv shares the base installation's
standard library and the marker lives there. A naive check — "does the file
exist?" — would therefore conclude that the venv is externally managed too, and
pip would refuse to install into it. It does not. Measured:

```
  sys.prefix       = /Users/.../geophysics/.venv
  sys.base_prefix  = /opt/homebrew/opt/python@3.14/Frameworks/Python.framework/Versions/3.14
  running in a venv: True
```

The predicate pip uses is `sys.prefix != sys.base_prefix`, not the existence of
the file. Getting this wrong in a wrapper script produces a
"but it works when I run it by hand" bug, which is the worst kind.

The correct workflow, in full:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install --upgrade pip
.venv/bin/python -m pip install -r requirements.txt
```

Two more things to know. First, `pipx` is the correct tool for *applications* —
it gives each one its own environment and puts only the entry points on `PATH`.
Second, `--break-system-packages` is never the right answer, because it trades a
reproducible environment for five seconds of convenience and the failure surfaces
weeks later.

## 2. `pyproject.toml`: four tables, one file

PEP 518 introduced `pyproject.toml` as the place to declare a build's
requirements; PEP 517 defined the hook interface a build backend must implement;
PEP 621 standardised where project metadata lives. Together they replace
`setup.py` for almost every purpose. Measured, parsing this lesson's sample file
with [`tomllib`](https://docs.python.org/3/library/tomllib.html):

```
[build-system] requires     = ['hatchling>=1.24']
[build-system] build-backend= hatchling.build
[project] name        = geophys-tools 0.3.1
[project] requires-python = >=3.11
[project] dependencies = ['numpy>=1.26,<3', 'scipy>=1.11']
[project.optional-dependencies] keys = ['docs', 'test']
[project.scripts] {'geophys': 'geophys_tools.cli:main'}
[tool.pytest.ini_options] {'addopts': '-ra --strict-markers'}
[tool.ruff] line-length = 99
```

Four points.

- **`[build-system]` is a two-part declaration.** `requires` names what must be
  installed to build; `build-backend` names the module that implements the hooks.
  `pip install .` creates an *isolated* environment containing exactly
  `requires`, imports the backend, and calls it. This is why building no longer
  depends on whatever happened to be installed.
- **`[project]` is data, not code.** PEP 621's argument for a declarative table
  is a security argument: a dict cannot execute arbitrary code at install time,
  and an install-time script can. `setup.py` is not forbidden, but every
  `setup.py` that could be a table is a privilege nobody asked for.
- **`[project.optional-dependencies]` are extras.** `pip install
  'geophys-tools[test]'` installs the test dependencies; a library ships its
  runtime dependencies in `dependencies` and everything else as an extra.
- **`[tool.*]` tables hold tool configuration**, so the package, the tests, the
  linter and the docs are described in one file. Reviewed together, diffed
  together, versioned together.

### 2.1 Build backends

You do not have to choose a backend by hand, but you should know the classes:

| backend | good for | notes |
|---|---|---|
| `setuptools.build_meta` | existing projects, extension modules | the default for `setup.py`-era code |
| `hatchling` | pure-Python libraries | declarative, minimal configuration |
| `flit_core` | small pure-Python libraries | requires the module layout to match the name |
| `maturin`, `scikit-build-core` | Rust and C/C++ extensions | the pattern used by NumPy, SciPy and friends |
| `meson-python` | scientific C/Fortran | the backend SciPy moved to |

The choice affects the build, not the resulting metadata: a wheel's `METADATA`
is the same whoever produced it. For a pure-Python geophysics helper library,
`hatchling` or `flit_core` is enough; the moment a Fortran kernel or a Cython
module appears, the backend choice becomes a real engineering decision.

### 2.2 Layout: flat or `src/`

The two conventional layouts are

```
flat:        geophys_tools/__init__.py            src:  src/geophys_tools/__init__.py
             pyproject.toml                            pyproject.toml
```

The difference looks cosmetic and is not. With the flat layout, the package
directory sits in the project root, which is also the directory you run commands
from, which means `import geophys_tools` succeeds **whether or not the package
is installed** — the current directory is on `sys.path`. Tests therefore pass
against the source tree and can fail against the installed wheel, and the
failure appears only after publication. With `src/`, the package is not
importable from the project root at all, so every test necessarily exercises an
installed copy, editable or not.

This repository has neither, and for a reason worth stating: it is a curriculum,
not a library, and its `code/` directories are executed by pytest, which inserts
each test file's directory into `sys.path`. That is exactly the flat-layout
hazard in miniature — measured earlier in this module, `test_pytest_basics.py`
imports `geophys_tools` successfully while neither is on any `PYTHONPATH`,
purely because pytest pre-pended the test file's directory. It works, it is
fragile, and it is the reason a real library uses `src/` and an install step.

`[project.scripts]` is the other half of a professional layout. Declaring

```toml
[project.scripts]
geophys = "geophys_tools.cli:main"
```

makes the build backend generate an `entry_points.txt` inside the wheel's
`.dist-info`, and pip creates a console script on `PATH` that imports
`geophys_tools.cli` and calls `main`. The host application never has to know the
module name — which is the feature that makes a plugin ecosystem possible, and
is how tools such as `pytest` itself discover third-party plugins.

## 3. Version specifiers, evaluated

Specifier semantics are best learned by evaluating them. Measured against four
candidate versions of a package whose installed version is 2.5.4:

| specifier | 1.24.4 | 2.5.4 | 2.6.0 | 3.0.0 |
|---|---|---|---|---|
| `==2.5.4` | no | yes | no | no |
| `>=1.26` | no | yes | yes | yes |
| `>=1.26,<3` | no | yes | yes | no |
| `~=2.5.0` | no | yes | no | no |
| `~=2.5` | no | yes | yes | no |
| `!=2.5.4` | yes | no | yes | yes |
| `>=1.26,!=2.5.0` | no | yes | yes | yes |

The row that surprises people is `~=2.5`. The compatible-release operator pins
the *last* component it is given and lets everything to its right float, so
`~=2.5.0` means `>=2.5.0, ==2.5.*` while `~=2.5` means `>=2.5, ==2.*` — a much
wider range than the number of digits suggests. Read the operator; do not infer
it from the number of dots.

### 3.1 Pinning versus ranges, and why it matters for science

The two styles answer different questions.

| style | question it answers | cost |
|---|---|---|
| `==2.5.4` | "can I get this exact behaviour back?" | cannot receive a security or correctness fix |
| `>=1.26,<3` | "is my library usable by others?" | reproducible only if a lock file also exists |
| `~=2.5.0` | "patch fixes only" | excludes a minor release that may be the fix |

For a published paper the answer is *both, in different files*: the library
metadata that others install from carries ranges, and the repository carries a
lock file with `==` pins that reproduces the environment the figures were made
in. That separation is not a compromise; it is the correct division of labour
between a library and an experiment.

Why it matters specifically in geophysics: a minor NumPy release may change the
result of a reduction at the last bit, and a scipy release may change the
default solver for a function your inversion calls. Neither is a bug in your
code. Both change your numbers. A repository that does not record the versions
under which its figures were produced cannot answer the question a referee will
eventually ask.

## 4. What an installed package is

An installed distribution is a directory tree plus a metadata directory. Measured
for one installed package in this environment:

```
  packaging 26.3: 52 entries in the RECORD
    packaging-26.3.dist-info/INSTALLER
    packaging-26.3.dist-info/METADATA
    packaging-26.3.dist-info/RECORD
    packaging-26.3.dist-info/WHEEL
    packaging-26.3.dist-info/licenses/LICENSE
    packaging/__init__.py
  installed METADATA has 42 top-level fields
```

`RECORD` is the important one: every line is *path, sha256 digest, size*. It is a
manifest and an integrity check in one file, and it is what makes
`pip uninstall` complete and `pip check` possible.

A wheel is a ZIP archive with that layout:

```
geophys_tools/__init__.py
geophys_tools/py.typed
geophys_tools-0.3.1.dist-info/METADATA        <- PEP 621 fields
geophys_tools-0.3.1.dist-info/WHEEL           <- tags, pure-python flag
geophys_tools-0.3.1.dist-info/RECORD          <- hashes
geophys_tools-0.3.1.dist-info/entry_points.txt
```

An **sdist** is a `tar.gz` of the source plus the backend's configuration. Both
are produced by the same command, which in modern scripts is:

```bash
python -m build          # writes dist/*.whl and dist/*.tar.gz
```

`build` is not installed here and this lesson installs nothing, so the command
above is documentation, not a measurement. What *is* measured is the *shape* of
the artefacts, from the installed copies.

The `WHEEL` file carries the tags that decide portability. A pure-Python wheel
is tagged `py3-none-any` and installs anywhere. A wheel with a compiled
extension is tagged with the interpreter version, the ABI and the platform —
which is why a package such as NumPy publishes a different wheel for every
combination of Python version and operating system, and why installing from
source on an unusual platform is slow and sometimes impossible.

## 5. Editable installs

```bash
.venv/bin/python -m pip install -e .
```

An editable install puts a pointer to your source tree into `site-packages`
instead of a copy, so edits take effect without reinstalling. It is the right
mode for developing a package that you also import from a test suite or a
notebook. It is the wrong mode for producing an environment you intend to
archive: an editable install is not reproducible from the same lock file,
because it depends on the source tree staying where it is.

Two adjacent modes are worth naming, because the distinctions cause confusion.
`pip install .` performs a normal (non-editable) install from a *copy*, so later
edits have no effect. `pip install --no-build-isolation .` skips the isolated
build environment and uses whatever is installed — which is faster and can
silently build against a different backend version. Prefer the isolated form
unless you have a measured reason not to.

## 6. Auditing a declaration against an environment

The one question that matters before attempting to reproduce someone else's
result is: does this environment satisfy the declaration? Measured for this
repository's own `requirements.txt`, which declares 33 requirements, against the
155 distributions visible to the project interpreter:

```
  satisfied: 25   version-mismatch: 0   not installed: 8
    MISSING  pyrocko>=2024.1
    MISSING  simpeg>=0.21
    MISSING  disba>=0.6
    MISSING  bruges>=0.5
    MISSING  torch>=2.2
    MISSING  seisbench>=0.6
    MISSING  ruff>=0.4
    MISSING  mypy>=1.10
```

Three observations, all of which generalise.

- **Zero version mismatches, eight absences.** An audit that reports only
  "problems" hides this distinction; absences are preparation gaps, mismatches
  are contradictions. The two need different responses.
- **`ruff` and `mypy` are declared and absent**, which is why
  [03-13-04](./04-code-quality.md) reimplements their checks from `ast` rather
  than invoking them. A declaration is a statement of intent; the environment is
  a statement of fact, and the gap between them is exactly what an audit
  measures.
- **The audit is offline and takes under a second**, using
  [`importlib.metadata`](https://docs.python.org/3/library/importlib.metadata.html)
  and `packaging.specifiers` alone. There is no excuse for skipping it.

## 7. Python demonstration

```bash
.venv/bin/python 03-scientific-computing/13-testing-profiling-packaging/code/packaging_demo.py
```

The script detects the externally-managed marker and explains the venv
predicate, parses a sample `pyproject.toml`, evaluates seven specifiers against
four candidate versions, walks the `RECORD` of an installed distribution, and
audits the repository's own `requirements.txt`. It writes nothing, installs
nothing and touches no network.

It is worth reading `pyproject.toml` of a real project next to Section 2 —
NumPy's own, or SciPy's — to see how quickly a serious scientific project
accumulates backend-specific configuration, `meson` build options, generated
`__config__` modules and per-platform dependency markers. The four tables are
the skeleton; the flesh is all of that.

## 8. Assumptions and limits

- **Nothing here was built or published.** No wheel was created and no index was
  contacted; every claim about build behaviour is from the specifications and
  from inspecting installed artefacts. Treat the build commands as documentation.
- **`requires-python` is a declaration, not a check.** A package that says
  `>=3.11` and uses a 3.12-only feature fails at import on 3.11, and only CI
  matrices catch that.
- **A lock file pins the interpreter's packages, not the interpreter.** The
  Python version, the platform and the BLAS build remain separate concerns; see
  [03-13-08](./08-reproducible-environment.md).
- **Version pinning is not safety.** A pinned version can be a pinned
  vulnerability; the reason to pin is reproducibility, and the reason to
  periodically update is security. Both are needed.
- **Publishing to an index is irreversible in practice.** A name that gets a
  malicious release cannot be unpublished from every mirror. The lesson does not
  cover publishing, deliberately.

## 9. Common mistakes

1. Running `pip install` against the system interpreter and then reaching for
   `--break-system-packages`. The answer is a virtual environment.
2. Testing for the `EXTERNALLY-MANAGED` file's existence rather than the venv
   predicate, which misclassifies every virtual environment.
3. Believing `~=2.5` means `==2.5.*`. It means `>=2.5, ==2.*`.
4. Putting test dependencies in `dependencies` rather than in an extra, so every
   user installs pytest.
5. Committing a `setup.py` that computes metadata at install time when a
   `[project]` table would do.
6. Shipping a package without a `py.typed` marker and then wondering why the
   type checker sees `Any` everywhere in downstream code.
7. Recording versions in the paper's methods section but not in the repository,
   where they can be installed.
8. Assuming that a pure-Python wheel works because it works locally; the local
   install may have picked up an editable source tree instead.

## 10. Real-world applications

- **A group gravity library.** The `pyproject.toml` carries ranges so
  collaborators can install it; the repository carries a lock file so the
  figures in the group's last paper can be regenerated. Both files are
  deliverables.
- **A processing plugin for an observatory pipeline.** An entry-point
  (`[project.scripts]`) lets the host application discover the plugin without
  hard-coding its name, which is the packaging feature that makes an ecosystem
  possible.
- **A teaching repository.** Shipping lessons as an installable package lets
  students `pip install -e .` and import the correct version of the helpers
  rather than copying code out of a lesson.
- **Reproducibility statements.** "numpy 2.5.4, scipy 1.18.1, Python 3.14.4"
  is a sentence that can be checked. "Recent versions of NumPy and SciPy" is
  not.

## 11. Further reading

- **PEP 668 — Marking Python base environments as "externally managed".**
  <https://peps.python.org/pep-0668/> Level: reference. Short, and the source of
  the message in Section 1.
- **PEP 517 — A build-system independent format for source trees.** and
  **PEP 518 — Specifying minimum build system requirements.** and
  **PEP 621 — Storing project metadata in pyproject.toml.**
  <https://peps.python.org/pep-0517/>, <https://peps.python.org/pep-0518/>,
  <https://peps.python.org/pep-0621/>. Level: reference. Read together; they
  partition the problem cleanly.
- **Python Packaging User Guide.**
  [Packaging Python Projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/),
  [pyproject.toml specification](https://packaging.python.org/en/latest/specifications/pyproject-toml/),
  [dependency specifiers](https://packaging.python.org/en/latest/specifications/dependency-specifiers/).
  Level: tutorial to reference. The dependency-specifier page is the authority
  for Section 3's table.
- **Python standard library.**
  [`tomllib`](https://docs.python.org/3/library/tomllib.html),
  [`importlib.metadata`](https://docs.python.org/3/library/importlib.metadata.html),
  [`venv`](https://docs.python.org/3/library/venv.html),
  [`sysconfig`](https://docs.python.org/3/library/sysconfig.html). Level:
  reference.
- **pip documentation.** [User guide](https://pip.pypa.io/en/stable/user_guide/)
  Level: reference. The sections on editable installs and requirements files
  cover Section 5.

> Note on citations: bibliographic details are given so you can locate the
> works. This repository does not host or reproduce copyrighted text.

## 12. Related lessons

- [03-13-04 Linting, Formatting, Type Hints and Static Analysis](./04-code-quality.md)
  — the tools whose configuration lives in the `[tool.*]` tables.
- [03-13-08 Reproducible Environments: pip-tools, conda, Containers](./08-reproducible-environment.md)
  — the next step: pinning the interpreter, the platform and the numeric
  libraries.
- [03-13-06 Git for Scientific Collaboration](./06-git-workflow.md) — what
  belongs in the repository and what belongs in a data archive.
- [03-13-01 pytest: Tests, Fixtures, Parametrisation and Approximate Comparisons](./01-pytest-basics.md)
  — the tests that a CI pipeline installs the package in order to run.
- [00-03-02 Environment Setup](../../00-orientation/03-how-to-use-this-repo/02-environment-setup.md)
  — this repository's own installation path.

## 13. Self-assessment checklist

- [ ] I can explain PEP 668 to a new student in three sentences, and give the
      correct workflow. (§1)
- [ ] I can say why a virtual environment reports the base interpreter's stdlib
      path and still installs. (§1.1)
- [ ] I can write the four tables of a `pyproject.toml` from memory. (§2)
- [ ] I can evaluate `~=2.5`, `~=2.5.0` and `>=1.26,<3` against a candidate
      version without running pip. (§3)
- [ ] I can justify pinning in a lock file and ranges in library metadata, in one
      sentence each. (§3.1)
- [ ] I can describe what `RECORD` contains and why uninstall needs it. (§4)
- [ ] I can say when an editable install is right and when it is wrong. (§5)
- [ ] I can audit a requirements file against an environment and interpret the
      difference between a mismatch and an absence. (§6)
