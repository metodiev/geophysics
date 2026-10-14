---
id: 00-03-02
title: "Setting Up the Python Environment and Tooling"
level: beginner
prereqs: ["00-03-01"]
estimated_minutes: 50
tags: [environment, python, tooling, reproducibility]
---

# Setting Up the Python Environment and Tooling

## Learning objectives

- Explain why this repository has **two** environments: one with no
  dependencies at all, and one scientific stack.
- Create an isolated virtual environment, install the scientific stack from
  `requirements.txt`, and verify the installation.
- Decide which tiers of `requirements.txt` your chosen track actually needs, and
  install heavy or optional packages deliberately rather than by reflex.
- Record your environment so that a result you produce can be reproduced by
  someone else.

## Prerequisites

[Repository Navigation and File Naming Conventions](./01-navigation.md). You
should be able to locate `requirements.txt` and the `tools/` directory.

## 1. Why there are two environments

The repository is designed so that **contributing and validating require nothing
installed**:

| Environment | Contents | Used for |
|---|---|---|
| Quality gate | Python standard library only | `python3 tools/check_all.py`, `python3 tools/build_index.py`, `python3 tools/verify_links.py` |
| Scientific stack | NumPy, SciPy, ObsPy, PyGMT and the rest of `requirements.txt` | Running lesson code, exercises and projects |

This separation is deliberate. The quality gate is what keeps the curriculum
honest — structure, links, formulas, duplicates — and it must run on any machine,
including a fresh container, without a package-resolution step that could fail.
Lesson code, by contrast, needs the real scientific stack.

A practical consequence: **you can start reading and validating immediately, and
install packages only when a lesson imports them.**

## 2. Check what you already have

Start by finding out which interpreter you are actually using. This matters
because a machine often has several, and the one that runs `python` is not always
the one you think.

```bash
python3 --version
python3 -c "import sys; print(sys.executable)"
```

Write the version down. Some scientific packages lag the newest Python releases;
if your interpreter is very new, a wheel may not exist for one of the heavier
dependencies. The `requirements.txt` header notes exactly this situation and
recommends a conda environment as a fallback that can pin an older, fully
supported interpreter. Verify by attempting the install rather than assuming —
the failure message names the missing wheel.

## 3. Create an isolated environment

Never install the scientific stack into your system interpreter. Use a virtual
environment in the repository root:

```bash
cd /path/to/geophysics
python3 -m venv .venv
source .venv/bin/activate           # Windows: .venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Three notes on this sequence:

- **Activation is per shell session.** A new terminal is a new session; re-run
  the activation command before working.
- **Upgrade pip first.** Older pip versions mishandle some modern wheel tags and
  produce confusing resolution errors.
- **The prompt changes.** An activated environment usually prefixes your prompt
  with the environment name. If you cannot see it, you are probably in the system
  interpreter.

The `.venv` directory is ignored by git in this repository, so your environment
never enters version control.

## 4. What is in `requirements.txt`

The file is organised by tier, and the comments in it explain the intent. Read it
before installing: it is short, and it tells you which packages are optional.

| Tier | Packages (as listed in the file) | When you need it |
|---|---|---|
| Core array and numerical | `numpy`, `scipy`, `sympy` | Essentially every quantitative lesson |
| Tabular and labelled data | `pandas`, `xarray`, `netCDF4`, `h5py`, `zarr`, `dask` | Climate, gridded and large-array lessons |
| Plotting and mapping | `matplotlib`, `cartopy`, `pyproj` | Any lesson that asks you to plot or map |
| Geospatial | `geopandas`, `shapely`, `rasterio`, `fiona` | Remote sensing, GIS, geology |
| Seismology | `obspy`, `pyrocko` (optional) | Seismology track |
| Geophysics-specific | `pygmt`, `simpeg`, `disba`, `bruges`, `verde` | Chosen per track; see the notes in the file |
| Machine learning | `scikit-learn`, `torch` (optional), `seisbench` (optional) | Statistics and ML track |
| Notebooks and developer tooling | `jupyterlab`, `ipykernel`, `pytest`, `pytest-cov`, `ruff`, `mypy`, `nbstripout` | Writing, testing and linting code |

The three packages whose installation is least like the others deserve comment,
because the file says so explicitly:

- **PyGMT is a wrapper around GMT.** It needs the GMT C library installed by your
  package manager or by conda. On conda, installing PyGMT from `conda-forge`
  installs both together, which the file describes as the least painful route.
- **PyTorch with GPU support** needs a platform-specific index URL that depends
  on your CUDA (or other accelerator) version. Install it by following the
  official PyTorch instructions rather than from this file.
- **Some packages lag the newest CPython releases.** If a wheel is unavailable on
  a very new interpreter, the file's recommended fallback is a conda environment
  with a supported interpreter version.

## 5. Verify, then verify again

Do not assume an install succeeded because pip printed no error. Check that the
packages import and that the versions are what you expect:

```bash
python -c "import numpy, scipy, matplotlib; print(numpy.__version__, scipy.__version__, matplotlib.__version__)"
```

Then confirm that the quality gate — which needs none of that — runs in the same
environment:

```bash
python3 tools/check_all.py
python3 tools/build_index.py
python3 tools/verify_links.py
```

`check_all.py` should print a summary ending in `RESULT: PASS`; `build_index.py`
regenerates `CURRICULUM.md`; `verify_links.py` audits that every external URL
cited in the Markdown is registered in `tools/verified_links.tsv`, and has a
`--check` mode that re-requests the registered URLs (that mode needs network
access and, unlike the default audit, is not offline).

Reference documentation for the central packages is authoritative and worth
bookmarking: [https://numpy.org](https://numpy.org) for array computing,
[https://scipy.org](https://scipy.org) for algorithms, and
[https://docs.obspy.org](https://docs.obspy.org) for seismological data handling.

## 6. Conda as an alternative

The repository's **primary supported route is `venv` plus `requirements.txt`**,
and that is what the commands in section 3 use. A conda environment file is also
provided alongside the repository at its root, for the cases where conda is the
better tool: it can install GMT and PyGMT together, it can pin an interpreter
version when the newest one has no wheels for a dependency, and `conda-forge`
provides pre-built geospatial binaries (GDAL, rasterio, PROJ) that are otherwise
awkward to compile. The command is:

```bash
conda env create -f environment.yml
conda activate geophysics
```

If you would rather build the environment by hand — or if you are adapting the
repository for a machine where the supplied file does not resolve — create and
use an environment explicitly and install the packages you need into it:

```bash
conda create -n geophysics python=3.12
conda activate geophysics
conda install -c conda-forge numpy scipy matplotlib pandas xarray obspy pygmt
```

Either way, **record what you did**. The reproducibility requirement is not "use
venv" or "use conda"; it is that another person can recreate the environment in
which your result was produced.

## 7. Installing selectively

Installing all of `requirements.txt` is the simplest instruction and the one that
works for most learners. Two situations justify doing less:

- **Constrained machine or slow connection.** Install the core numerical tier
  plus plotting, and add packages when a lesson imports them. A failure message
  naming a missing module is unambiguous feedback about what to install.
- **Track specialisation.** A climate track has little use for a seismic
  processing toolkit and vice versa; the file groups packages precisely so that
  you can make this choice.

Two rules if you install selectively: keep `requirements.txt` as the record of
the full stack (do not delete lines you personally do not use), and if you add a
package that the lessons need, add it to `requirements.txt` in the appropriate
tier so the next person gets it too.

## 8. Developer tooling

The tooling tier is not optional for research-grade work, and it is worth
installing from the start because habits form early:

| Tool | Purpose in this repository |
|---|---|
| `pytest`, `pytest-cov` | Testing lesson code and project code; coverage to see what is untested |
| `ruff` | Linting and formatting; fast, and catches real mistakes such as unused imports |
| `mypy` | Static type checking; catches unit- or shape-confusion bugs before runtime |
| `nbstripout` | Strips notebook outputs before commit, so repositories stay small and diffs readable |
| `jupyterlab`, `ipykernel` | Interactive exploration |

A convention worth adopting immediately: notebooks are for exploration, and any
result you intend to keep moves into a `.py` module with a test. That is the same
distinction the [contribution workflow](./04-contribution-workflow.md) assumes.

## 9. Reproducibility hygiene

Four habits, none of them heavy:

1. **Record exact versions when a result matters.** `python -m pip freeze >
   requirements-lock.txt` in the project that produced the result, so the
   figures can be regenerated later.
2. **Keep the environment out of version control, the specification in it.**
   `.venv` is ignored; `requirements.txt` is tracked.
3. **State the interpreter version** in any report or notebook header.
4. **Use relative paths in code and data references.** Absolute paths in a
   script are the same mistake as absolute paths in Markdown links, and they fail
   in exactly the same way: silently, on someone else's machine.

## 10. A complete worked check

The whole setup, in order, with the expected result of each step:

```bash
python3 --version                              # note the version
python3 tools/check_all.py                     # should end with: RESULT: PASS
python3 -m venv .venv
source .venv/bin/activate                      # Windows: .venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -c "import numpy; print(numpy.__version__)"
python3 tools/build_index.py                   # regenerates CURRICULUM.md
```

If the last command changes `CURRICULUM.md`, that is expected whenever lessons
were added or removed; it is a generated file and its diff is the coverage
report.

## Common mistakes

1. **Installing into the system interpreter.** Breaks other projects, and produces
   "works on my machine" results you cannot reproduce later.
2. **Forgetting to activate.** The classic symptom is `ModuleNotFoundError` right
   after a successful install: the install went to one interpreter and the run
   used another.
3. **Installing all of a heavy tier you do not need.** PyGMT without GMT, or
   GPU PyTorch from the default index, are the two common time sinks.
4. **Assuming the quality gate needs the scientific stack.** It does not, by
   design, and that is what makes it portable.
5. **Not recording versions.** A figure you cannot regenerate is an illustration,
   not a result.
6. **Editing `CURRICULUM.md` by hand** instead of regenerating it.

## Real-world applications

- **Reproducibility requirements.** Journals and funders increasingly require
  code and environment information. The habits in section 9 are what make that
  straightforward rather than a scramble at submission time — see
  [22-data-engineering-reproducibility](../../22-data-engineering-reproducibility/README.md).
- **Onboarding onto a project.** A `requirements.txt` plus a short setup section
  is how a new team member becomes productive on day one instead of day five.
- **Deployment and HPC.** Cluster and container environments pin interpreter and
  library versions for the same reason: an unpinned environment is an
  unreproducible one.
- **Software packaging in research.** Turning analysis code into an installable
  package with tests is a direct extension of the tooling tier.

## Further reading

- Wilson, G., Bryan, J., Cranston, K., Kitzes, J., Nederbragt, L., & Teal, T. K.
  (2017). Good enough practices in scientific computing. *PLOS Computational
  Biology*, 13(6), e1005510. — Short, practical, and directly relevant to
  environment and dependency management.
- Boettiger, C. (2015). An introduction to Docker for reproducible research.
  *ACM SIGOPS Operating Systems Review*, 49(1), 71–79. — The next level beyond
  virtual environments, and a useful mental model of what "the environment" means.
- NumPy, SciPy and ObsPy project documentation, at
  [https://numpy.org](https://numpy.org), [https://scipy.org](https://scipy.org)
  and [https://docs.obspy.org](https://docs.obspy.org) respectively. — Always
  consult the version of the documentation matching your installed version, not a
  tutorial from several releases ago.
  The journal citations are bibliographic records; confirm availability through
  your library or a DOI resolver before citing them yourself.

## Related lessons

- [Repository Navigation and File Naming Conventions](./01-navigation.md)
- [Running the Link, Formula and Duplication Checks](./03-quality-gate.md)
- [Batch Workflow for Adding Lessons and Projects](./04-contribution-workflow.md)
- [Cross-Cutting Skills: Mathematics, Computing, Inverse Theory](../02-curriculum-map/04-cross-cutting.md)
