# Exercises — 03-13-08 Reproducible Environments: pip-tools, conda, Containers

Attempt these **closed-book** before opening the
[solutions](./08-reproducible-environment-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems marked **[demo]** refer to
[`../code/environments_demo.py`](../code/environments_demo.py), which spawns four
subprocesses and runs in a few seconds:

```
.venv/bin/python 03-scientific-computing/13-testing-profiling-packaging/code/environments_demo.py
```

The lesson is [`../08-reproducible-environment.md`](../08-reproducible-environment.md).

---

## ★ Foundational

**★1. [demo]** The identity section reports:

```
  sys.version           = 3.14.8 (main, Sep 30 2026, ...) [Clang 21.0.0 ...]
  implementation        = CPython 3.14.8
  sys.prefix            = /Users/.../geophysics/.venv
  sys.base_prefix       = /opt/homebrew/opt/python@3.14/...
  in a virtual env      = True
  machine               = arm64  (10 logical CPUs)
```

(a) Rewrite this as a one-sentence methods-section statement, and say which item
a typical methods section omits.
(b) Explain why `sys.prefix` belongs in the statement even though the interpreter
version is already given.
(c) The demo reports 155 distributions and a fingerprint of
`e7ef18127aa9491f58c5aaed4979c37e5e24cebe68fd500bfce870e7a23a7e29`. State what
the fingerprint is a function of, and what it is *not*.

**★2. [demo]** The BLAS section reports `BLAS name = accelerate`,
`LAPACK name = accelerate`, and a SIMD baseline of NEON/ASIMD.

(a) Explain, in one sentence, why a different BLAS changes the last bits of a dot
product.
(b) State which of the following a lock file pins: the BLAS, the NumPy version,
the SIMD instructions used, the interpreter.
(c) A colleague on x86 with OpenBLAS reports a result differing from yours in the
fourteenth significant figure. State whether this is a bug, and what the correct
response is.

**★3.** State which of these are pinned by a lock file with `--require-hashes` and
which are not: (a) the transitive dependency set; (b) the exact distribution bytes;
(c) the interpreter patch version; (d) the platform; (e) the thread count.

---

## ★★ Applied

**★★4. [demo]** The reduction-order measurements are

```
  v.sum()                          = 998.5706494386213
  per-row partials, then summed    = 998.5706494386211  diff -2.274e-13
  reduceat in 1000-blocks          = 998.5706494386209  diff -4.547e-13
  sorted ascending, then summed    = 998.5706494386541  diff +3.274e-11

  full A @ B vs three 200-column partials: identical = False, max |diff| = 1.990e-13
  relative to max|AB| = 121.875: 1.63e-15
```

(a) Compute the relative difference for the sorted sum, given $|{\sum}| = 998.571$.
(b) Estimate the number of ulp each difference represents at that magnitude
($\mathrm{ulp}(1000) \approx 1.14\times10^{-13}$).
(c) State the tolerance you would use for an assertion on this sum, and justify
it from the numbers rather than from taste.

**★★5. [demo]** The thread-count experiment reports **one** distinct digest for
each of matmul, solve and sum, across `OMP_NUM_THREADS` = 1, 2, 4, 8.

(a) State what the experiment establishes and what it does not, in one sentence
each.
(b) Describe the change to the experiment that would most likely reverse the
result, and why.
(c) State how you would phrase the result in a paper's methods section.

**★★6. [demo]** The audit reports:

```
  requirements checked against this environment: 29
    satisfied: 24
    unmet or absent: 5
      ghostscript (absent) ...
```

(a) State the difference between an absence and a version mismatch, and why the
audit should report them separately.
(b) The repository's `requirements.txt` audit gives 25 satisfied, 0 mismatch,
8 absent, while `environment.yml` gives 24 satisfied, 5 absent. Explain why the
two audits differ, and which one is the right one to run.
(c) State what the audit cannot tell you about the environment.

---

## ★★★ Research-oriented

**★★★7.** You are preparing a paper's reproducibility package for a geodynamics
code that needs a Fortran compiler, an MPI library, PETSc, and a specific BLAS.

(a) Choose between `venv` + lock file, conda, and a container, and justify the
choice in terms of what must be pinned.
(b) State the three artefacts you would deposit, and the DOI-bearing archive that
holds each.
(c) State three facts still unpinned after all three artefacts exist, and which of
them you would measure and record in the paper.

**★★★8. [demo]** The reproducibility statement of Section 12 of the lesson names
three obligations: code, data, environment.

(a) For each, name the mechanism from this module that discharges it, and the
identifier that makes it checkable.
(b) State which obligation has no technical solution, and why.
(c) A referee asks you to demonstrate that Figure 3 is reproducible. Describe the
sequence of commands you would run, in the order a stranger would need to run
them.

**★★★9.** The lesson measures a negative result — thread count changed nothing
here — and refuses to generalise it.

(a) Explain the difference between "we measured no difference" and "there is no
difference", and name the statistical concept at issue.
(b) The experiment compares four thread counts at one problem size (600×600) with
one operation. Design the experiment that would be needed to support the stronger
claim, stating the factors and the number of runs.
(c) State one circumstance under which you would *not* bother to run the stronger
experiment, and why that is a defensible decision rather than laziness.
