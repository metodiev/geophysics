---
id: 03-13-08
title: "Reproducible Environments: pip-tools, conda, Containers"
level: advanced
prereqs: ["03-13-05", "03-13-07"]
estimated_minutes: 115
tags: [reproducibility, venv, conda, containers, lock-files, blas, determinism]
---

# Reproducible Environments: pip-tools, conda, Containers

"It worked on my machine" is a statement about an environment. This lesson treats
the environment as an object you can print, hash and pin: the interpreter and its
prefix, the packages and their versions, the BLAS the numeric libraries are
linked against, the thread count, and the platform. Three of those five are
pinnable with a lock file; the other two have to be re-tested where the numbers
matter, and knowing which is which is the skill.

The lesson ends with an experiment that many people assert and few measure: does
the thread count change the answer? On this machine and this BLAS the honest
answer is **no**, and the lesson reports the negative result and explains why it
does not license the assumption.

## Learning objectives

By the end of this lesson you will be able to:

1. **Print** an environment's identity and reduce it to a single reviewable hash.
2. **Explain** why identical Python code can differ in the last bits on another
   machine, in terms of the BLAS build and reduction order.
3. **Demonstrate** the effect of reduction order on a sum and a matrix product,
   and quantify it in ulp.
4. **Measure** whether the thread count changes a result, and interpret a
   negative result honestly.
5. **Audit** a repository's environment declaration against what is installed,
   and distinguish a version mismatch from an absence.
6. **Write** a lock file, and state what `--require-hashes` adds and what remains
   unpinned even then.
7. **Choose** between `venv` + pip-tools, conda, and a container, and say what
   each one actually pins.

## Prerequisites

- [03-13-05 Packaging and Distributing a Python Library](./05-packaging.md) —
  PEP 668, virtual environments, specifiers and lock files.
- [03-13-07 Consuming APIs and Web Services for Earth Data](./07-apis-and-web-data.md)
  — a fetched payload is only reproducible together with the environment that
  processed it.

## 1. Printing an environment

Measured on this machine:

```
  sys.version           = 3.14.8 (main, Sep 30 2026, ...) [Clang 21.0.0 ...]
  implementation        = CPython 3.14.8
  sys.executable        = /Users/.../geophysics/.venv/bin/python
  sys.prefix            = /Users/.../geophysics/.venv
  sys.base_prefix       = /opt/homebrew/opt/python@3.14/Frameworks/Python.framework/Versions/3.14
  in a virtual env      = True
  platform              = macOS-27.0.1-arm64-arm-64bit-Mach-O
  machine               = arm64  (10 logical CPUs)
```

Note what is missing from a typical methods section: the interpreter *patch*
version, the executable path, and whether the interpreter is inside an
environment. "Python 3" is not a version; `CPython 3.14.8, arm64, macOS, in a venv`
is. The prefix matters because two interpreters of the same version with
different `site-packages` are different environments, and the failure they
produce is a `ModuleNotFoundError` on somebody else's machine after a successful
local run.

### 1.1 One hash for the whole environment

Measured: 155 distributions are visible to this interpreter. Sorting their
`name==version` pairs and hashing the resulting text gives

```
  fingerprint: sha256(155 pins) = e7ef18127aa9491f58c5aaed4979c37e5e24cebe68fd500bfce870e7a23a7e29
```

with key packages `numpy 2.5.4`, `scipy 1.18.1`, `pandas 3.0.6`,
`matplotlib 3.11.2`, `pytest 9.1.1`, `xarray 2026.9.0`, `obspy 1.5.1`,
`geopandas 1.2.0`, `rasterio 1.5.2`.

The fingerprint is the reviewable artefact. Two people reporting the same hash
were running the same environment whatever their machines; two reporting
different hashes have a concrete difference to look at. It is also, unlike a
runtime, a deterministic function of the thing you want to compare.

## 2. The BLAS is part of the environment

NumPy's array arithmetic is NumPy's; its linear algebra is whatever BLAS and
LAPACK it was built against. Measured here:

```
  numpy version    = 2.5.4
  BLAS  name       = accelerate
  LAPACK name      = accelerate
  SIMD baseline    = ['NEON', 'NEON_FP16', 'NEON_VFPV4', 'ASIMD']
  SIMD found       = ['ASIMDHP', 'ASIMDDP']
  SIMD not found   = ['ASIMDFHM']
```

Accelerate on arm64 means an Apple-supplied BLAS using NEON vector instructions.
A colleague on x86 with OpenBLAS, or with MKL, has a *different* implementation
of every dot product, every matrix multiply and every factorisation.

Why that changes results at all is one sentence long: **a dot product is a
reduction, floating-point addition is not associative, and the order in which a
vectorised kernel accumulates determines the last bits.** Which instruction the
compiler emitted, how the loop was unrolled, how the block was tiled and how many
threads were used all change the order.

## 3. Reduction order, measured in one process

The effect is easy to demonstrate without leaving Python. The same sum of
$10^6$ standard normal deviates, accumulated five ways:

| accumulation | value | difference from `v.sum()` |
|---|---|---|
| `v.sum()` (pairwise) | 998.5706494386213 | — |
| per-row partials, then summed | 998.5706494386211 | $-2.274\times10^{-13}$ |
| `np.add.reduceat` in 1000-blocks | 998.5706494386209 | $-4.547\times10^{-13}$ |
| sorted ascending, then summed | 998.5706494386541 | $+3.274\times10^{-11}$ |

All three differences are about $3.3\times10^{-14}$ relative to a sum of
magnitude $9.99\times10^2$ — a few tens of ulp. A tolerance of $10^{-12}$
relative passes all four; a bitwise comparison fails three of them.

The same effect appears in a matrix product when *you* choose a different
grouping:

```
  full A @ B vs three 200-column partials: identical = False, max |diff| = 1.990e-13
  relative to max|AB| = 121.875: 1.63e-15
```

This is the mechanism by which a different BLAS version, a different
cache-blocking choice, or a different thread count produces a different answer
from the same mathematics. It is not a bug and it cannot be tested away. It can
only be *bounded*: the relative difference is $\mathcal{O}(n u)$ for a length-$n$
reduction, so doubling the problem size roughly doubles the discrepancy, and a
tolerance derived from that bound is the correct response.

## 4. Does the thread count change the answer? (measured)

Many claims circulate about this, including in this repository's own task
descriptions. It is a claim that can be tested in about two seconds, so it should
be tested rather than asserted. Four subprocesses, each with all five relevant
thread-control variables set, compute the same $600\times600$ product and the same
solve, and hash the results:

```
  OMP_NUM_THREADS= 1  matmul 7eb55863a1c9fa5fe23ebf9f  solve 174629238f30b8c7784fb5a1  sum 18149.64711541383
  OMP_NUM_THREADS= 2  matmul 7eb55863a1c9fa5fe23ebf9f  solve 174629238f30b8c7784fb5a1  sum 18149.64711541383
  OMP_NUM_THREADS= 4  matmul 7eb55863a1c9fa5fe23ebf9f  solve 174629238f30b8c7784fb5a1  sum 18149.64711541383
  OMP_NUM_THREADS= 8  matmul 7eb55863a1c9fa5fe23ebf9f  solve 174629238f30b8c7784fb5a1  sum 18149.64711541383
  distinct matmul digests across thread counts: 1
  distinct solve  digests across thread counts: 1
  distinct sums   across thread counts        : 1
```

**Negative result: on this machine, with this BLAS, thread count changed
nothing.** Accelerate's kernels gave identical bytes at 1, 2, 4 and 8 threads for
this problem size.

That does not license the assumption, and the honest wording matters. What the
experiment establishes is:

- **For a fixed thread count, the digest is reproducible.** Both digests repeat
  exactly across four independent processes, so pinning the thread count is a
  legitimate part of "the environment". That is a positive result and it is
  useful.
- **This BLAS did not partition by thread count at this size.** A different BLAS
  (OpenBLAS, MKL), a different problem size, or a different matrix shape may
  partition, and the failure mode is a last-bit difference that can flip a
  comparison and then a branch. The experiment must be re-run on the machine that
  matters.

Reporting this as "threads do not affect results" would be exactly the folklore
this lesson exists to replace. Reporting it as "measured identical on
Accelerate/arm64 for 600×600 matmul and solve at 1/2/4/8 threads; not tested
elsewhere" is a result.

## 5. Auditing a declaration against the environment

The repository's `environment.yml` declares a conda environment. Parsed and
audited against what is installed:

```
  name       = geophysics
  channels   = ['conda-forge', 'defaults']
  conda dependencies: 30
  pip dependencies  : 0
  requirements checked against this environment: 29
    satisfied: 24
    unmet or absent: 5
      ghostscript (absent)
      discretize (absent)
      simpeg (absent)
      ruff (absent)
      mypy (absent)
```

Five absences, no mismatches. Both categories matter and they mean different
things: an **absence** is a preparation gap — the lesson that needs `simpeg` will
not run until it is installed — while a **mismatch** is a contradiction: the
declaration and the environment disagree about a version that *is* present. A
report that merges the two hides the distinction that decides what to do next.

Note that `ruff` and `mypy` are declared and absent, which is why
[03-13-04](./04-code-quality.md) reimplements their checks from `ast` instead of
invoking them. The declaration is a statement of intent; the environment is a
statement of fact.

## 6. Lock files and `--require-hashes`

The three mechanisms, in increasing order of what they pin:

| mechanism | pins | leaves free |
|---|---|---|
| `requirements.txt` with ranges | the *set* of packages | every version |
| lock file with `==` pins | versions of every package | the artefacts, the interpreter, the platform |
| lock file with hashes + pinned interpreter | versions and the exact distribution bytes | the platform, the BLAS, the hardware |
| container image digest | the whole user space | the kernel, the hardware |

A lock file is generated from an abstract input:

```bash
pip-compile --generate-hashes requirements.in -o requirements.lock
pip install --require-hashes -r requirements.lock
```

Both commands are from the pip-tools and pip documentation. **They were not run
here**: this environment is offline and neither pip-tools nor a package index is
available. The *format* is straightforward and is what the demonstration prints:

```
    numpy==2.5.4 \
        --hash=sha256:<64 hex digits> \
        --hash=sha256:<another acceptable wheel>
```

`--require-hashes` turns pip into a verifier: the lock file names the exact
artefacts and their digests, and pip downloads those bytes or nothing. It is the
only pip mode that is genuinely reproducible, and it is the reason a lock file is
a deliverable rather than a convenience. It also has a cost worth stating: with
`--require-hashes` you cannot install anything not in the lock file, so adding one
package means regenerating the lock, reviewing the diff, and re-running the whole
verification.

### 6.1 What a lock file cannot pin

Measured, and this is the list that matters:

- **The interpreter.** Pinning `numpy==2.5.4` does not pin `3.14.8`, and a wheel
  built for another ABI will not install. `requires-python` is a declaration, not
  a check.
- **The BLAS and the SIMD baseline.** `numpy==2.5.4` from PyPI on macOS/arm64 and
  from conda-forge on Linux have different `.so` files and different kernels.
- **The platform.** Record `platform()` and the machine architecture; a
  fingerprint that does not say `arm64` is incomplete.
- **The thread count**, unless you set and record it — see Section 4.
- **The kernel, and therefore the memory allocator behaviour** under a container.
- **The data.** Section 3 of [03-13-07](./07-apis-and-web-data.md) is the analogue
  on the data side: hash the payload.

## 7. Choosing a mechanism

| approach | pins | cost | learn it when |
|---|---|---|---|
| `venv` + lock file | packages and versions | low; one command | always, as the baseline |
| conda / `environment.yml` | packages *and* the interpreter, plus non-Python libraries | medium; a second solver | you need GDAL, GMT, PyGMT or Fortran-adjacent tooling |
| container (`Dockerfile` + digest) | the whole user space | high; builds and image storage | an archive requires a permanently runnable artefact, or the environment is genuinely exotic |

The honest ranking for a research group is: **start with `venv` plus a lock
file**, because it is cheap, it covers the common failure (a wrong NumPy), and it
requires nothing new to be learned. Move to conda when a wheel does not exist for
your platform — which for `PyGMT`, `rasterio` and anything needing the GMT or GDAL
C libraries is the common case, and is why this repository's `environment.yml`
exists alongside `requirements.txt`. Move to a container when the environment
itself must be archived, or when the coupling between the Python stack and system
libraries (a specific PROJ version, a specific BLAS) is part of the result.

A container adds one thing no lock file can: **the same user space everywhere**,
including the shared libraries. That is what makes it the right answer for a
published artefact and the wrong answer for a quick analysis, where the image
build cost exceeds the value.

### 7.1 Container reproducibility, stated carefully

A `Dockerfile` that starts `FROM python:3.12-slim` is not reproducible: the tag
moves. Pinning the *digest* —

```
FROM python:3.12-slim@sha256:<64 hex digits>
```

— makes the base image immutable, and pinning every subsequent `apt-get install`
to a version makes the whole layer deterministic. Nothing in this lesson builds or
runs a container; the statement is a description of the mechanism, and the reader
should verify it on their own platform with their own registry before relying on
it.

## 8. Python demonstration

```bash
.venv/bin/python 03-scientific-computing/13-testing-profiling-packaging/code/environments_demo.py
```

Runs in a few seconds (four subprocesses). It prints the interpreter identity,
the environment fingerprint, the BLAS configuration, the three reduction-order
comparisons, the four-subprocess thread-count experiment, the `environment.yml`
audit, and the lock-file illustration. It installs nothing and touches no network.

Also worth reading alongside it: `code/packaging_demo.py`, which computes the
part of this story that concerns distribution metadata, and
`code/git_workflow_demo.py`, which shows what the repository itself pins.

## 9. Assumptions and limits

- **A fingerprint identifies, it does not guarantee.** Two environments with the
  same 155 pins can differ in the BLAS build or the platform; the fingerprint
  narrows the search, it does not close it.
- **The thread-count experiment is machine-specific.** Measured negative here;
  not measured elsewhere. Do not generalise it.
- **conda's solver is not a proof of reproducibility.** `environment.yml` with
  unpinned package names resolves to different versions on different days.
  Reproducibility needs either pinning or a lock file, whichever the tool offers.
- **Containers trade reproducibility for portability and cost.** A pinned image
  digest is highly reproducible on the registry's terms and does nothing about
  the kernel or the hardware.
- **The environment is only one of three obligations.** The other two are the
  code revision ([03-13-06](./06-git-workflow.md)) and the data
  ([03-13-07](./07-apis-and-web-data.md)). None of the three is sufficient alone,
  and a reproducibility statement that names only the packages is incomplete.

## 10. Common mistakes

1. Reporting "Python 3" instead of a version, an implementation and a platform.
2. Committing `requirements.txt` with ranges and calling the environment pinned.
3. Assuming a lock file pins the interpreter or the BLAS.
4. Believing that a `pip freeze` output is a lock file. It records *what happened
   to be installed*, including transitive packages nothing depends on, and it
   cannot distinguish a deliberate pin from an accident.
5. Generalising a thread-count or BLAS result from one machine.
6. Using a moving container tag, so the "reproducible" environment changes
   silently.
7. Auditing only for *problems*, and so losing the distinction between an absent
   package and a contradictory version.
8. Recording the versions in the paper's methods section but not in the
   repository, so the environment cannot be built.

## 11. Real-world applications

- **A paper's reproducibility package.** A repository with a lock file, a
  recorded fingerprint, a tag and a data DOI is a package a referee can actually
  run. This repository's own `requirements.txt` and `environment.yml` are the
  mechanism, with the quality gate deliberately depending on the standard library
  so that the curriculum can be validated with nothing installed.
- **A processing centre.** A container image digest per processing campaign makes
  "which version produced this image" answerable years later, which is a
  regulatory as well as a scientific requirement in some jurisdictions.
- **A teaching environment.** A pinned environment means the lesson that begins
  "if your output differs from mine, check the version" has an answer.
- **A long-running cluster job.** Recording the thread count and the fingerprint
  in the job log makes an anomalous result investigable rather than mysterious.

## 12. Further reading

- **PEP 668 — Marking Python base environments as "externally managed".**
  <https://peps.python.org/pep-0668/> Level: reference. Repeated from
  [03-13-05](./05-packaging.md) because the venv predicate is the practical
  consequence.
- **Python standard library.** [`venv`](https://docs.python.org/3/library/venv.html),
  [`sysconfig`](https://docs.python.org/3/library/sysconfig.html),
  [`importlib.metadata`](https://docs.python.org/3/library/importlib.metadata.html),
  [`subprocess`](https://docs.python.org/3/library/subprocess.html). Level:
  reference for the measurements in Sections 1 and 4.
- **pip.** [User guide](https://pip.pypa.io/en/stable/user_guide/) Level:
  reference. Requirements files, hash checking and editable installs.
- **conda.** [Managing environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
  Level: reference. The `environment.yml` path of Section 7.
- **NumPy.** [Random generator documentation](https://numpy.org/doc/stable/reference/random/generator.html)
  and [`numpy.sum`](https://numpy.org/doc/stable/reference/generated/numpy.sum.html).
  Level: reference. The pairwise-summation note behind Section 3, and the RNG
  policy behind reproducible sampling.
- **Higham, N. J. (2002). *Accuracy and Stability of Numerical Algorithms*
  (2nd ed.). SIAM.** Chapter 1. Level: advanced. The $nu$ bound used to size the
  differences in Section 3.
- **The Turing Way — Guide for Reproducible Research.** Level: intermediate. The
  practical framing that a reproducible environment is one of several
  obligations, not one of them.

> Note on citations: bibliographic details are given so you can locate the
> works. This repository does not host or reproduce copyrighted text.

## 13. Related lessons

- [03-13-05 Packaging and Distributing a Python Library](./05-packaging.md) —
  `pyproject.toml`, PEP 668 and the venv workflow.
- [03-13-07 Consuming APIs and Web Services for Earth Data](./07-apis-and-web-data.md)
  — the data half of the reproducibility statement.
- [03-13-06 Git for Scientific Collaboration](./06-git-workflow.md) — the code
  half, and why a hash is a citation.
- [03-13-03 Profiling CPU and Memory](./03-profiling.md) — why every timing in
  this module is a property of the machine, and why counts are not.
- [03-02-06 The NumPy Random Module](../02-numpy/06-random-module.md) — seeding,
  reductions and what "reproducible" means for a random stream.

## 14. Self-assessment checklist

- [ ] I can print my environment's identity in a form another person could
      rebuild. (§1)
- [ ] I can compute and report an environment fingerprint. (§1.1)
- [ ] I can explain, in one sentence, why a different BLAS changes the last bits.
      (§2)
- [ ] I can demonstrate a reduction-order difference and quantify it in ulp. (§3)
- [ ] I can test whether the thread count changes a result on my machine, and
      phrase the answer so it is not over-claimed. (§4)
- [ ] I can audit a declaration and distinguish an absence from a mismatch. (§5)
- [ ] I can say what a lock file pins and list three things it does not. (§6.1)
- [ ] I can choose between venv, conda and a container with a stated reason. (§7)
- [ ] I can name the three obligations — code, data, environment — and say which
      one I am currently neglecting. (§11)
