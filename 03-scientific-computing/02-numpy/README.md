# Module 03-02 — NumPy and Array Computing

**Stages:** beginner → advanced · **Prerequisites:**
[03-01-05 Lists, Tuples, Dictionaries, Sets and Complexity](../01-python-fundamentals/05-data-structures.md)
and [03-01-04 Functions, Scope, Modules and Packages](../01-python-fundamentals/04-functions-modules.md)
for the Python language itself; [01-07-02 Matrices, Matrix Multiplication and
Linear Maps](../../01-mathematics/07-linear-algebra/02-matrices-and-operations.md)
for the mathematics of the 2-D array, and
[01-07-03 Linear Systems, Gaussian Elimination and LU Factorisation](../../01-mathematics/07-linear-algebra/03-systems-and-elimination.md)
before lesson 05.

NumPy is where a geophysical field becomes a data structure. A gravity survey is
not a list of readings; it is a *field* sampled on a grid, and the `ndarray` is
the object that carries both the values and the geometry. This module teaches the
array as the natural representation of field data, and it does so in the order in
which the concepts bite:

- **Shape is geometry.** A `(north, east)` array and a `(1000, 1000, 1000)` model
  cube are described by a shape and a dtype, and those two numbers decide whether
  a job fits in memory before a single line of physics is written.
- **Strides are memory.** Slicing, views, copies and cache performance are all
  consequences of the byte-level layout introduced in lesson 01.
- **Names of axes are a modelling decision.** The single most common silent bug in
  numerical geophysics is a reduction along the wrong axis, which produces a
  plausible number with no warning. Lesson 04 is written to train that error out.
- **Vectorisation is not free and not always faster.** Lesson 08 contains three
  measured cases where the "vectorised" form is slower than the loop it replaced,
  and one where the ordering is not even stable between runs.

There is a deliberate emphasis on **measurement over folklore**. Lesson 07 tests
the widely repeated claim that summing along axis 0 of a C-ordered array is
several times slower than along axis 1, finds it **false** on the current NumPy
reduction kernels (a ratio of 0.59 to 1.04 across runs, i.e. no penalty in either
direction), and locates the real layout penalty — a 17.8× to 23.9× cost for
elementwise traversal of a 128-byte-strided view — which is a
different phenomenon with the same reputation. Lesson 08 reports a time ratio that
reverses between two consecutive runs and explains why the *memory* claim is the
one that survives.

Two rules apply throughout. First, **every number in every lesson is the actual
output of a demo in [`code/`](./code)**, executed with the project interpreter,
and the lessons state the NumPy version and the machine. Second, **timings are
labelled machine-dependent**; the reproducible claims are the element counts,
operation counts, strides and peak allocations.

## Learning objectives

By the end of this module you will be able to:

1. **Create** arrays that represent a 2-D survey grid and a 3-D model cube, and
   **choose** a dtype from a stated precision requirement, computing the memory of
   a $10^8$-cell model in `float32` and `float64` before allocating it.
2. **Read and predict** an array's `shape`, `strides` and contiguity, and
   **explain** the silent integer-overflow and `float32`-accumulation traps with
   the check that catches each.
3. **Classify** any indexing expression as a view or a copy, **reproduce** the
   silent-corruption bug in which a function meant to return a copy modifies its
   caller's array, and **repair** it three ways.
4. **Apply** the broadcasting rules from the right, subtract a station mean from
   every trace, build an $n \times n$ distance matrix without a loop, and
   **predict** the size of every intermediate the expression will allocate.
5. **State** what `axis=k` removes, **guard** every reduction with a shape
   assertion against the coordinate array it must match, and **choose** correctly
   between propagating and `nan`-aware reductions.
6. **Solve** a least-squares problem three ways, **explain** why the normal
   equations square the condition number, **rescale** a design matrix to fix it,
   and **justify** `solve` over `inv`.
7. **Generate** reproducible synthetic noise from an explicit `Generator`,
   **check** the sample moments against their standard errors, and **use** the
   $1/\sqrt{N}$ law to size an experiment.
8. **Measure** the cost of a strided traversal, **compute** the break-even point
   for a contiguity copy, and **report** a performance result with the operation
   count, the element count and the machine.
9. **Identify** the cases where a full broadcast loses to a loop, name the
   dedicated kernels (`bincount`, `reduceat`, `einsum`, `out=`) that replace the
   generic forms, and **state** the quadratic copy count of array growth in a loop.

## Lessons

| # | Lesson | Level | Key idea |
|---|---|---|---|
| 01 | [ndarray Creation, dtypes, Shapes and Strides](./01-ndarray-basics.md) | beginner | Shape is geometry, dtype is precision, strides are the path through memory |
| 02 | [Indexing, Slicing, Views vs Copies and Fancy Indexing](./02-indexing-slicing.md) | beginner | A slice does not copy — the most productive source of silent bugs in Python numerics |
| 03 | [Broadcasting Rules and Vectorised Thinking](./03-broadcasting.md) | intermediate | Align from the right; the loop disappears into a shape |
| 04 | [Universal Functions, Reductions and Axis Semantics](./04-ufuncs-reductions.md) | intermediate | **`axis=k` removes axis k** — the classic silent error |
| 05 | [Linear Algebra with numpy.linalg](./05-linear-algebra-numpy.md) | intermediate | `solve` beats `inv`; the normal equations square the condition number |
| 06 | [Random Number Generation and Reproducible Seeds](./06-random-module.md) | intermediate | A seed fixes a sequence, not a result |
| 07 | [Memory Layout, Strides and Cache-Aware Performance](./07-memory-performance.md) | advanced | Measure the layout penalty; it is not where the folklore says |
| 08 | [Replacing Loops: Vectorisation Patterns and Traps](./08-vectorisation-patterns.md) | advanced | Three measured cases where the vectorised form loses |

## Suggested path

**If you are working through the computing sequence in order:** lessons 01–08 in
numeric order. Lessons 01–02 are the foundation for everything that follows in
[03 SciPy](../03-scipy/README.md), [04 pandas](../04-pandas/README.md) and
[05 Plotting, Visualisation and Scientific Figures](../05-plotting-and-visualisation/README.md);
lesson 04 is the one used most often downstream.

**If you are here to process field data:** read 01 §3 (dtype choice for a survey
grid), 02 in full (the view/copy discipline that keeps raw data intact), 03 §2
(per-station corrections) and 04 §4 (`nan` handling for missing stations). Then
[04-pandas/03 Cleaning: Missing Values, Duplicates and Outliers](../04-pandas/03-cleaning-data.md).

**If you are here for inversion or modelling:** lessons 01, 03, 05, 07 and 08, in
that order, and then
[18-inverse-problems/…](../../18-inverse-problems/README.md) and
[19-numerical-modeling-hpc/…](../../19-numerical-modeling-hpc/README.md). The
conditioning material of lesson 05 §5 is the prerequisite for every regularisation
discussion that follows.

**If you already have NumPy experience:** attempt ★★★8–9 of
[04](./exercises/04-ufuncs-reductions-exercises.md), ★★★8–9 of
[05](./exercises/05-linear-algebra-numpy-exercises.md) and ★★★8–9 of
[08](./exercises/08-vectorisation-patterns-exercises.md) first. If those close
cleanly, use lessons 01–03 and 06 as reference and read 07 for the measurement
discipline.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-ndarray-basics.md`](./01-ndarray-basics.md) … [`08-vectorisation-patterns.md`](./08-vectorisation-patterns.md) | The eight lessons |
| [`exercises/01-ndarray-basics-exercises.md`](./exercises/01-ndarray-basics-exercises.md) and [`-solutions.md`](./exercises/01-ndarray-basics-solutions.md) | Grid memory, strides, dtype choice, byte order |
| [`exercises/02-indexing-slicing-exercises.md`](./exercises/02-indexing-slicing-exercises.md) and [`-solutions.md`](./exercises/02-indexing-slicing-solutions.md) | View/copy classification, the silent-corruption bug, duplicate indices |
| [`exercises/03-broadcasting-exercises.md`](./exercises/03-broadcasting-exercises.md) and [`-solutions.md`](./exercises/03-broadcasting-solutions.md) | Shape rules, distance-matrix memory, blocked kernels |
| [`exercises/04-ufuncs-reductions-exercises.md`](./exercises/04-ufuncs-reductions-exercises.md) and [`-solutions.md`](./exercises/04-ufuncs-reductions-solutions.md) | Axis semantics, `nan` policy, sum against integral |
| [`exercises/05-linear-algebra-numpy-exercises.md`](./exercises/05-linear-algebra-numpy-exercises.md) and [`-solutions.md`](./exercises/05-linear-algebra-numpy-solutions.md) | Conditioning, weighted least squares, rank deficiency, Tikhonov |
| [`exercises/06-random-module-exercises.md`](./exercises/06-random-module-exercises.md) and [`-solutions.md`](./exercises/06-random-module-solutions.md) | Seeds, standard errors, effective sample size, bootstrap |
| [`exercises/07-memory-performance-exercises.md`](./exercises/07-memory-performance-exercises.md) and [`-solutions.md`](./exercises/07-memory-performance-solutions.md) | Cache arithmetic, break-even copies, stencil benchmarks |
| [`exercises/08-vectorisation-patterns-exercises.md`](./exercises/08-vectorisation-patterns-exercises.md) and [`-solutions.md`](./exercises/08-vectorisation-patterns-solutions.md) | Fused against materialised, blocking, judging a speed-up claim |
| [`code/ndarray_basics_demo.py`](./code/ndarray_basics_demo.py) | Survey grid, dtype catalogue, 3-D cube, strides, overflow and accumulation traps |
| [`code/indexing_slicing_demo.py`](./code/indexing_slicing_demo.py) | The silent-corruption demo, three repairs, an alias audit |
| [`code/broadcasting_demo.py`](./code/broadcasting_demo.py) | Station-mean subtraction, distance matrix, outer product, intermediate sizes |
| [`code/ufuncs_reductions_demo.py`](./code/ufuncs_reductions_demo.py) | Axis shape table, the axis mix-up, `nan` policy, ufunc methods, loop against reduction |
| [`code/linalg_demo.py`](./code/linalg_demo.py) | Least squares three ways, `solve` against `inv`, Hilbert conditioning, Cholesky |
| [`code/random_demo.py`](./code/random_demo.py) | Seed reproducibility, legacy call-order hazard, moment checks, $1/\sqrt{N}$ |
| [`code/memory_performance_demo.py`](./code/memory_performance_demo.py) | Strides, axis reductions, strided view, traversal order, contiguity copy, BLAS |
| [`code/vectorisation_demo.py`](./code/vectorisation_demo.py) | Forward-model speed-up, memory-bound trap, `np.vectorize`, array growth, blocking |

## Running the demos

Every demo needs only NumPy and the standard library, and every one of them
generates its own SYNTHETIC data — no dataset is read and no file is written. Run
them with the project interpreter:

```
.venv/bin/python 03-scientific-computing/02-numpy/code/ndarray_basics_demo.py
.venv/bin/python 03-scientific-computing/02-numpy/code/indexing_slicing_demo.py
.venv/bin/python 03-scientific-computing/02-numpy/code/broadcasting_demo.py
.venv/bin/python 03-scientific-computing/02-numpy/code/ufuncs_reductions_demo.py
.venv/bin/python 03-scientific-computing/02-numpy/code/linalg_demo.py
.venv/bin/python 03-scientific-computing/02-numpy/code/random_demo.py
.venv/bin/python 03-scientific-computing/02-numpy/code/memory_performance_demo.py
.venv/bin/python 03-scientific-computing/02-numpy/code/vectorisation_demo.py
```

The four timing scripts (04, 07, 08 and the timing section of 07) take between a
few seconds and about a minute in total; the other four are effectively
instantaneous. Every stochastic demo prints its seed, so its output is
reproducible exactly; every timing demo prints that its timings are
machine-dependent and states the counts that are not.

## What this module deliberately does not cover

- **Plotting.** Deferred to [05 Plotting, Visualisation and Scientific
  Figures](../05-plotting-and-visualisation/README.md).
- **Labelled tabular data.** `ndarray` has no axis labels; that is what
  [04 pandas](../04-pandas/README.md) supplies.
- **Sparse and structured solvers, quadrature, optimisation.** All
  [03 SciPy](../03-scipy/README.md).
- **Parallelism beyond BLAS.** Deferred to
  [19-numerical-modeling-hpc/…](../../19-numerical-modeling-hpc/README.md).
