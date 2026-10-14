# Module 03-12 — Building Numerical Simulation Code in Python

**Stages:** intermediate → graduate · **Prerequisites:**
[03-02-04 ufuncs, Reductions, Broadcasting and Vectorisation](../02-numpy/04-ufuncs-reductions.md)
for the array operations a solver's inner loop is made of, and
[01-12-01 Root Finding](../../01-mathematics/12-numerical-methods/01-root-finding.md)
for what a numerical method's error and order mean.

Most geophysics is done by simulation, and most simulation code is written once
and used twice. This module teaches the second use. It builds a solver from
scratch, derives and measures its stability limit, refactors it into testable
interfaces, verifies and validates it, and only then considers parallelism.

The module's habit is the one that makes the rest possible: **every claim is
measured.** An order of accuracy is a table of measured orders, not an
adjective. A stability limit is a measured growth rate compared with a von
Neumann prediction, not a remembered inequality. A boundary condition's quality
is a measured reflection coefficient. A parallel run's correctness is a
bit-identity assertion across worker counts.

Two consequences of that habit show up as results rather than as asides:

- The **defective double root** at $r = 1$: the standard stability test
  ($|G| \le 1$) passes while the amplitude grows linearly as $2n-1$, measured.
- An **off-by-one in time** in the module's own boundary condition, which
  changed a measured reflection coefficient from 0.12 % to 34 % — a change of
  conclusion, found by measurement and invisible in the code.

## Scope

| lesson | question it answers |
|---|---|
| 01 | how do I write a finite-difference solver, and how do I know it is right? |
| 02 | when is it stable, how fast does it diverge when it is not, and where is it accurate? |
| 03 | how do I structure the code so that the answers stay testable? |
| 04 | verification versus validation: what exactly am I entitled to claim? |
| 05 | what does parallelism buy, and how do I keep it reproducible? |

## Prerequisites

- NumPy array arithmetic, `np.roll`, broadcasting and reductions.
- Single-variable calculus: Taylor expansions are used for every error term.
- Ordinary and partial differential equations at the level of
  [01-09](../../01-mathematics/09-partial-differential-equations/README.md):
  you should know what $u_{tt} = c^2u_{xx}$ means before discretising it.
- No prior parallelism, and no prior finite-difference experience.

## Lesson map

| # | Lesson | Level | Key idea |
|---|---|---|---|
| 01 | [A 1-D Finite-Difference Solver from Scratch](./01-finite-difference-1d.md) | intermediate | A 30-line scheme; a measured order of 2.0000; and the metric that reports 4.0000 for the same code |
| 02 | [Numerical Stability, CFL Conditions and Convergence Testing](./02-stability-and-cfl.md) | advanced | Measure the growth rate and match it to von Neumann to machine precision; the defective root that passes the test and grows anyway |
| 03 | [Designing Reusable Model Code: Grids, Operators, Boundaries](./03-modular-design.md) | advanced | Four interfaces, four tests, and the bug that only a measurement found |
| 04 | [Verification vs Validation: Benchmarks and Convergence Tests](./04-verification-and-validation.md) | graduate | Manufactured solutions, Richardson, GCI, and two analytic validations the solver was never told |
| 05 | [Parallelism in Python: Multiprocessing, Threads, Numba, JAX](./05-parallel-python.md) | graduate | Determinism, partition and numerical identity — the three things about a parallel run that are not machine-dependent |

## Two facts about the module's structure

First, the lessons are ordered by *claim strength*, not by difficulty of the
geophysics. Lesson 01 makes a statement about accuracy, lesson 02 about
stability, lesson 03 about code structure, lesson 04 about what the two
together entitle you to say, and lesson 05 about what happens when the answer
is too slow. A reader who only needs the verification material can start at
lesson 04 and read backwards when a term is unfamiliar.

Second, the demos deliberately include their own failures. The sign of the
Laplacian, the wrong time level in a boundary condition, the naive energy that
appears to show damping, and the operator test that compared against the wrong
derivative are all in the code that ships, with the measured consequences
printed. A verification lesson whose examples never fail is a lesson that has
hidden the most useful part.

## How to run the demos

All five scripts run with the project virtual environment, print no wall-clock
timings, use fixed seeds where randomness is involved, and exit 0:

```
.venv/bin/python 03-scientific-computing/12-numerical-simulation-python/code/finite_difference_1d_demo.py
.venv/bin/python 03-scientific-computing/12-numerical-simulation-python/code/stability_and_cfl_demo.py
.venv/bin/python 03-scientific-computing/12-numerical-simulation-python/code/modular_design_demo.py
.venv/bin/python 03-scientific-computing/12-numerical-simulation-python/code/verification_and_validation_demo.py
.venv/bin/python 03-scientific-computing/12-numerical-simulation-python/code/parallel_python_demo.py
```

Every number quoted in a lesson is printed by one of these scripts. Where a
lesson quotes a number that the script does not print, the lesson says so and
states that the value came from a modified copy with the modification
described.

## Companion exercises

Each lesson has paired exercise and solution files in
[`exercises/`](./exercises/): `NN-slug-exercises.md` and
`NN-slug-solutions.md`, graded ★ (foundational), ★★ (applied) and ★★★
(research-oriented). The ★★★ problems are the ones that require running
experiments and reporting their results, including one that requires correcting
a claim in the lesson if the measurement disagrees.

## Where this module leads

- [19-numerical-modeling-hpc](../../19-numerical-modeling-hpc/README.md)
  generalises the methods: finite differences, finite elements, spectral
  methods, and the high-performance computing that carries them to three
  dimensions.
- [18-inverse-problems](../../18-inverse-problems/README.md) uses a forward
  solver as the inner loop of an inversion, which is where a solver's speed and
  its accuracy both start to matter.
- [03-13 Testing, Profiling and Packaging](../13-testing-profiling-packaging/README.md)
  turns the measurement habit of this module into a test suite that runs on
  every commit.
