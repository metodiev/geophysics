---
id: 03-02-07
title: "Memory Layout, Strides and Cache-Aware Performance"
level: advanced
prereqs: ["03-02-01", "03-02-02"]
estimated_minutes: 75
tags: [numpy, memory, cache, strides, performance]
---

# Memory Layout, Strides and Cache-Aware Performance

A modern CPU can execute a few floating-point operations per nanosecond but can
deliver about one cache line — 64 bytes, eight `float64` — per memory latency.
The consequence is that numerical code is usually limited by **how it walks
memory**, not by how much arithmetic it does. A loop that touches $10^9$ elements
in the order they are stored and a loop that touches the same $10^9$ elements one
stride apart can differ by an order of magnitude in runtime while performing the
identical number of additions.

This lesson is about predicting and measuring that difference. It is deliberately
written around one measurement that **contradicts a widely repeated claim**: that
summing along axis 0 of a C-ordered array is much slower than along axis 1. On
this machine, and with the current NumPy reduction kernels, the two are the same
speed (a ratio of 1.04). The large penalty appears somewhere else entirely — in
elementwise traversal of a strided *view*. Reporting both is the point: the
folklore is checkable, and checking it changes what you optimise.

## Learning objectives

By the end of this lesson you will be able to:

1. **Read** an array's strides and state which axis is traversed contiguously and
   what the byte step is along each axis.
2. **Predict**, for a given stride, how many cache lines a traversal touches per
   useful element.
3. **Measure** the cost of a reduction along each axis and **explain** why the
   axis-0 penalty is absent for reductions but present for elementwise traversal.
4. **Measure** the penalty for a strided view and express it as a ratio against a
   contiguous traversal of the same number of elements.
5. **Measure** a row-wise against a column-wise in-place loop and state the
   operation counts that both perform.
6. **Quantify** the cost of `np.ascontiguousarray` and decide when the copy pays
   for itself.
7. **Explain** why BLAS is insensitive to the layout of its operands but sensitive
   to a *mismatch* between them.
8. **Report** a performance result with the element counts and machine, so that
   the claim is reproducible even when the timing is not.

## Prerequisites

- [01 ndarray Creation, dtypes, Shapes and Strides](./01-ndarray-basics.md) — the
  strides model that this lesson measures.
- [02 Indexing, Slicing, Views vs Copies and Fancy Indexing](./02-indexing-slicing.md)
  — how a strided view is created without a copy.
- [19-numerical-modeling-hpc/…](../../19-numerical-modeling-hpc/README.md) —
  the broader performance context (recommended).

## 1. Strides, restated as a memory step

For a C-ordered array the strides are, from the last axis backwards, the
itemsize multiplied by the cumulative product of the faster axis lengths. The
demo prints the two layouts of the same `(4, 5)` array:

```
C-order  shape (4, 5), strides (40, 8) bytes -> fastest axis is axis 1 (columns)
F-order  shape (4, 5), strides (8, 32) bytes -> fastest axis is axis 0 (rows)
a.itemsize = 8 bytes
```

The C-order strides are $(5 \times 8, 8) = (40, 8)$: eight bytes along a row,
forty bytes between rows. The Fortran-order strides are $(8, 4 \times 8) = (8, 32)$:
eight bytes down a column, thirty-two bytes between columns.

the number that matters for performance is the ratio of the stride to the cache
line size. This machine reports a 128-byte cache line
(`sysctl -n hw.cachelinesize` → `128`) and is an Apple M5 with a 64 KiB L1 data
cache, a 6 MiB L2 and 16 GB of RAM; most x86-64 parts use 64-byte lines. If a
traversal steps by 8 bytes, every cache line it loads is fully used: 16 useful
`float64` values per 128-byte line, or 8 per 64-byte line. If a traversal steps
by 128 bytes, every loaded line yields exactly one useful value — a **16× waste of
memory bandwidth** on this machine (8× on a 64-byte-line machine), and that is the
mechanism behind the measurement in §3.

## 2. Reductions: the folklore, tested

The demo allocates a $3000 \times 3000$ `float64` array (72.0 MB), confirms its
strides, and reduces it three ways:

```
arr.shape = (3000, 3000), 72.0 MB, strides = (24000, 8), C-contiguous = True
elements touched by each reduction: 9000000

  arr.sum(axis=1)  (axis 1 contiguous)  :     2.36 ms
  arr.sum(axis=0)  (axis 0 strided)     :     1.39 ms
  arr.sum()        (both axes, one pass):     1.30 ms
  ratio axis0/axis1 = 0.59x   (machine dependent)
```

The ratio came out at 0.59 — axis 0 was **faster** in this run; across repeated
runs on the same machine the ratio ranged from 0.59 to 1.04, always within a
factor of about two in either direction. There is no penalty. This contradicts a
claim that was true of older NumPy builds and is still repeated in tutorials. To
understand why there is no penalty, look at what the kernel does. A reduction
along axis 0 with a C-ordered array walks memory in **row order** — sequentially,
one contiguous row at a time — and adds each row into a length-3000 accumulator
that stays in L1 cache. The memory access pattern is perfectly sequential; the
stride appears only in the *output* index, not in the traversal. A reduction along
axis 1 walks the same sequential memory and reduces within each row. Both are
streaming.

The lesson generalises: **a reduction's cost is governed by the order in which it
touches memory, which is not the same as the axis it reduces.** NumPy chooses the
loop order internally; the `axis` argument selects the result's shape.

The `axis=None` case at 1.30 ms is the fastest of the three in this run, which is
what a single pairwise-blocked pass should be.

The demo also confirms the sums agree, which is the correctness check that must
accompany every performance measurement:

```
  sums agree within 1e-9: True
```

Had the fast version disagreed with the slow one, the speedup would have been a
bug, not an optimisation.

## 3. The real penalty: a strided view

Elementwise operations on a strided view are where the layout cost lands. The
demo builds two views of the same array that contain the **same number of
elements** and adds 1 to each in place:

```python
view = arr[:, ::16]      # (3000, 188), stride 128 bytes
view = arr[::16, :]      # (188, 3000), contiguous rows
```

```
arr[:, ::16].shape = (3000, 188), strides = (24000, 128)
arr[::16, :].shape = (188, 3000), strides = (384000, 8)
elements modified by each : 564000 and 564000

  column-strided (stride 128 B) :    2.290 ms
  row-subset     (contiguous)   :    0.129 ms
  ratio strided/contiguous = 17.8x   (machine dependent)
```

$564\,000$ elements in both cases, $564\,000$ additions in both cases, and a
factor of 17.8 in runtime (17.8–23.9 across repeated runs — the *existence* of the
penalty is reproducible, its magnitude to the last digit is not). The cause is
exactly the arithmetic of §1: the 128-byte stride means every loaded cache line
delivers one useful `float64` — a 16× bandwidth waste — and the extra cost of the
strided addressing arithmetic accounts for the rest.

This pattern is everywhere in geophysics. Any decimation, any gather of every
$n$-th trace, any subsampling of a grid produces a strided view. The remedy is
not to touch the view less often but to **write into a contiguous output array**:

```python
out = arr[::16, :].copy()          # one contiguous pass
# or, better, compute the output grid directly
```

and the demo's section on contiguity quantifies that copy (§5).

## 4. Traversal order in a loop

The textbook demonstration, with the loops written out:

```
n = 2000, 32.0 MB per array
row-wise  for i: a[i, :] += 1.0 :     1.91 ms
col-wise  for j: b[:, j] += 1.0 :     6.32 ms
ratio column/row = 3.30x   (machine dependent)
both loops perform 2000 iterations and 4000000 additions
```

Both loops perform 2000 Python iterations and $4 \times 10^6$ additions. The
row-wise version touches a 16 kB contiguous block per iteration, which fits
comfortably in L1 (64 KiB on the reference machine); the column-wise version
touches 2000 cache lines per iteration in a strided pattern, so the hardware
prefetcher cannot keep up and the effective memory traffic is far higher per
useful element.

Three notes on interpreting 3.30×:

- It is **smaller** than the 17.8× of §3 because the inner operation here is an
  in-place add over 2000 contiguous-looking values per outer iteration — the
  column loop still processes one *element* per row per iteration, but the
  iteration count is 2000 rather than $4 \times 10^6$, so loop overhead is a
  larger fraction and partly masks the memory penalty.
- It is **machine dependent** and varies with array size and cache size. Reduce
  $n$ to 200 and the working set (320 kB) fits in the 6 MiB L2 and the ratio
  collapses towards 1.
- The reproducible content is the *count*: 2000 iterations, $4 \times 10^6$
  additions, $4 \times 10^6 \times 8 = 32$ MB of memory touched, in one of two
  orders.

## 5. The cost of contiguity

```
arr.T is C-contiguous: False  (strides (8, 24000))
np.ascontiguousarray(arr.T) :     8.77 ms  (copies 72.0 MB)
np.ascontiguousarray(arr)   :     0.00 ms  (returns the same object: True)
copying 9000000 elements costs 0.97 ms per 1e6 elements (machine dependent)
```

The copy of 72 MB takes 8.8 ms, i.e. about 1.0 ms per million elements — roughly
the cost of one read plus one write at this machine's memory bandwidth, which is
the definition of a bandwidth-bound operation. When `arr` is already contiguous
the call returns the *same object* (verified by identity, not equality), so a
defensive `np.ascontiguousarray` at the top of a function costs nothing in the
common case.

The decision rule: compare the one-off cost of the copy against the per-pass
penalty multiplied by the number of passes. From §3, a strided pass over
$564\,000$ elements costs $2.29$ ms against $0.13$ ms contiguous — a penalty of
$2.16$ ms per pass. Copying the full array costs $8.8$ ms once. The copy pays for
itself after about four passes. Fewer than four passes: keep the view. This kind
of explicit break-even calculation is the whole craft; there is no way to know
without measuring both.

## 6. Matrix products and BLAS

```
n = 1200, 23.0 MB of operands per multiplication
A @ B   (both C order):     6.77 ms
Af @ Bf (both F order):     6.81 ms
ratio = 1.006x   (machine dependent)
results identical: True
```

The layout of the operands makes no measurable difference here (ratio 1.006; across
runs the value ranged from 0.82 to 1.01) because `A @ B` dispatches to BLAS, which is
*written for* blocked access: it tiles the matrices into cache-sized blocks,
transposes as needed internally, and uses vectorised kernels for the inner
product. Both layouts can be consumed efficiently. The residual differences you
see are at the level of kernel selection and run-to-run variation, not of the
memory model.

The genuine BLAS trap is a **mixed-layout** product: `A @ Bf` where one operand
is C-ordered and the other Fortran-ordered forces the library to make a
corrected copy internally, and the copy appears as an unexplained slowdown
proportional to the operand size. The demo's advice — keep operands in the same
layout — is the rule.

## 7. Physical interpretation

The memory hierarchy is the physical system being optimised: registers (a few
hundred bytes, sub-nanosecond), L1 (tens of kilobytes, a few cycles), L2
(hundreds of kilobytes to several megabytes, tens of cycles), L3 (tens of
megabytes on many parts, a hundred cycles), main memory (gigabytes, hundreds of
cycles). On the machine used here the measured sizes are L1 data = 64 KiB, L2 =
6 MiB, RAM = 16 GB. A geophysical grid is *purpose-built* to be larger than all
of them at once: a $1000^3$ model is $8 \times 10^9$ bytes and no cache holds it.

Given that, the performance model is not "fast arithmetic" but **reuse and
locality**:

- **Locality in space** is what strides describe. Traverse in storage order and
  every cache line is fully used; traverse against storage order and it is not.
- **Reuse in time** is what blocking achieves (in the BLAS sense): process a tile
  that fits in a cache, then move to the next tile, so that the tile's data is
  read once and used many times.

A finite-difference stencil — the workhorse of wave modelling — is a
bandwidth-bound operation with an arithmetic intensity of about one flop per byte
in second order, so it is *purely* governed by the memory model. This is why
"optimised" wave codes use blocking, vectorisation and `float32`, in that order.

## 8. Assumptions and regime of validity

- **Cache line sizes and cache sizes vary by machine.** 64-byte lines on x86-64,
  128 bytes on the Apple Silicon machine used here, so the same stride pattern
  costs a different factor on each. Report the machine with the timing.
- **All timings here are machine-dependent observations.** The reproducible
  content is the element counts, byte counts and strides. A reported speed-up
  without the machine and the array sizes is not reproducible.
- **Memory bandwidth is shared.** Other processes, hyperthreading and the
  operating system's page cache affect measurements by tens of percent. Use
  best-of-several timings, and expect the last digit to move between runs — the
  demo's section 5 reports two runs of the same expression for exactly this
  reason.
- **The folklore is version-dependent.** The axis-0 reduction penalty existed in
  older NumPy builds and may return in future ones. Measure on your NumPy
  version rather than trusting a claim, including this one.
- **Small arrays have no memory penalty.** Below L2 size the whole array is in
  cache and traversal order is irrelevant. Optimising layout for a $200 \times
  200$ array is wasted work.
- **NumPy's kernels may already be optimal.** Before restructuring, check whether
  the operation has a dedicated implementation (`np.dot`, `np.add.reduce`,
  `np.einsum`) that handles the layout for you.
- **`arr.T` is not a performance problem by itself.** It is a stride change; the
  problem is only the *traversal* of a non-contiguous axis.
- **The `order="F"` argument** on `zeros`/`empty`/`array` sets the layout. Using
  it is how you make the *reduction* axis contiguous, which matters when a
  repeated operation is along that axis.
- **Vectorised arithmetic is bandwidth-bound, not flop-bound**, for almost every
  array operation. Reducing the bytes touched (via `float32`, `out=`, or fusion)
  is the highest-leverage optimisation.

## 9. Python demonstration

The script is [`code/memory_performance_demo.py`](./code/memory_performance_demo.py):

```
.venv/bin/python 03-scientific-computing/02-numpy/code/memory_performance_demo.py
```

All arrays are SYNTHETIC (seeded random or constant-filled); no dataset is read.
The header prints the NumPy version, the seed and the array size, and the script
states that timings are machine-dependent, so the numbers below are labelled as
an observation on one machine rather than a law. For the record, that machine is
an Apple M5 (arm64) with 16 GB of RAM, a 128-byte cache line, a 64 KiB L1 data
cache and a 6 MiB L2, running NumPy 2.5.4 under CPython 3.14.

Key output (this machine, NumPy 2.5.4, `N = 3000`):

```
C-order  shape (4, 5), strides (40, 8) bytes -> fastest axis is axis 1 (columns)
F-order  shape (4, 5), strides (8, 32) bytes -> fastest axis is axis 0 (rows)
```

```
  arr.sum(axis=1)  (axis 1 contiguous)  :     2.36 ms
  arr.sum(axis=0)  (axis 0 strided)     :     1.39 ms
  ratio axis0/axis1 = 0.59x   (machine dependent)
```

```
arr[:, ::16].shape = (3000, 188), strides = (24000, 128)
elements modified by each : 564000 and 564000
  column-strided (stride 128 B) :    2.290 ms
  row-subset     (contiguous)   :    0.129 ms
  ratio strided/contiguous = 17.8x   (machine dependent)
```

```
row-wise  for i: a[i, :] += 1.0 :     1.91 ms
col-wise  for j: b[:, j] += 1.0 :     6.32 ms
ratio column/row = 3.30x   (machine dependent)
both loops perform 2000 iterations and 4000000 additions
```

```
np.ascontiguousarray(arr.T) :     8.77 ms  (copies 72.0 MB)
copying 9000000 elements costs 0.97 ms per 1e6 elements (machine dependent)
```

```
A @ B   (both C order):     6.77 ms
Af @ Bf (both F order):     6.81 ms
ratio = 1.006x   (machine dependent)
results identical: True
```

### What to observe

1. The axis-reduction ratio is 0.59 in this run (0.59–1.04 across runs), not the
   "3× slower" of the folklore. This is the headline result of the lesson: the
   folklore is falsifiable, and on this NumPy version it is false.
2. The strided-view ratio is 17.8 on the *same machine, in the same script*
   (17.8–23.9 across runs). The layout cost is real; it lives in a different place
   than the folklore says.
3. The traversal loop ratio (3.30) sits between the two, which is what the
   analysis in §4 predicts: the memory penalty is diluted by loop overhead.
4. `copying 9000000 elements costs 0.97 ms per 1e6 elements` is the bandwidth
   number to remember; it lets you estimate the break-even point of any
   copy-versus-stride decision (§5) without running a benchmark.
5. The matmul ratio 1.006 is within the run-to-run spread; the trustworthy claim
   is that both layouts are handled, and that a *mixed* layout is not.
6. Every performance number is accompanied by an element count or an operation
   count. That is the discipline this lesson is really teaching.

## 10. Common mistakes

1. **Repeating folklore instead of measuring.** Including "axis 0 is slower".
2. **Optimising before profiling.** Most array operations are already limited by
   memory bandwidth; restructuring the arithmetic changes nothing.
3. **Benchmarking once, on a busy machine, with a small array.** Use best-of-several
   and an array larger than L3.
4. **Measuring wall-clock without a correctness check.** A "speedup" that changes
   the answer is a bug.
5. **Copying inside a loop.** `np.ascontiguousarray` on every iteration turns a
   0.1 ms operation into a 12 ms one.
6. **Assuming `arr.T` made a copy.** It did not, and the traversal pays for it.
7. **Mixing layouts in a matrix product** and blaming BLAS.
8. **Fighting the layout with `float64` when `float32` would halve the bytes.**
   Bandwidth is the constraint; the dtype is the lever.
9. **Forgetting that timings are not reproducible.** Report the counts and the
   machine.
10. **Using `time.time()` for short intervals.** Use `time.perf_counter()`, which
    has a monotonic high-resolution clock.

## 11. Real-world applications

- **Finite-difference wave propagation.** Stencils are bandwidth-bound; loop
  order, array layout and blocking dominate the runtime, and the classic
  optimisation is to make the fastest-varying axis the one updated innermost.
- **Migration and reverse-time imaging.** Terabyte-scale wavefields are stored as
  `(x, y, t)` or `(t, x, y)` cubes; the choice determines the access pattern of
  every imaging condition and the achievable runtime.
- **Gravity and magnetic grid processing.** Convolution with a filter kernel is a
  stencil operation; padding and layout decide whether the filter's cache line is
  reused.
- **Seismic data sorting.** Sorting a gather by offset produces a strided gather;
  inverting the sort is a memory-bound permutation whose cost is dominated by the
  gather pattern.
- **Tomography and inversion.** The forward operator touches a sparse set of
  model cells; blocking the model into cache-sized tiles is the standard
  optimisation.
- **Machine learning.** Convolution libraries exist almost entirely to turn
  stencil operations into blocked, vectorised matrix products; the same memory
  argument is why im2col and Winograd transforms exist.

## 12. Further reading

- **Drepper, U. "What Every Programmer Should Know About Memory" (Red Hat
  technical report, 2007).** The cache-hierarchy, prefetching and bandwidth
  background that this lesson summarises. Level: advanced.
- **Patterson, D. A., & Hennessy, J. L. *Computer Organization and Design*
  (Morgan Kaufmann, current edition).** The memory hierarchy chapter, for the
  latency and bandwidth numbers quoted in §7. Level: intermediate.
- **Golub, G. H., & Van Loan, C. F. *Matrix Computations* (4th ed., Johns Hopkins
  University Press, 2013).** The blocked-algorithm discussion that explains why
  BLAS is insensitive to layout. Level: graduate.
- **NumPy documentation, "Internal memory layout of an ndarray".**
  [https://numpy.org](https://numpy.org) — the strides model, C and Fortran
  order, and the `order=` arguments used here. Level: intermediate.
- **SciPy Lecture Notes, "Performance and memory" and "Cython/NumPy
  interoperability".** [https://scipy.org](https://scipy.org) — the practical
  techniques, including `np.einsum` and the `out=` parameter. Level: intermediate.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 13. Related lessons

- [01 ndarray Creation, dtypes, Shapes and Strides](./01-ndarray-basics.md) — the
  strides model.
- [02 Indexing, Slicing, Views vs Copies and Fancy Indexing](./02-indexing-slicing.md)
  — creating strided views without copying.
- [08 Replacing Loops: Vectorisation Patterns and Traps](./08-vectorisation-patterns.md)
  — the memory-bound cases where the vectorised form loses.
- [19-numerical-modeling-hpc/…](../../19-numerical-modeling-hpc/README.md) —
  parallelisation and blocking at the scale of a whole model.
- [20-signal-processing/…](../../20-signal-processing/README.md) — filtering,
  which is a stencil operation.

Exercises:
[`exercises/07-memory-performance-exercises.md`](./exercises/07-memory-performance-exercises.md)
and
[`exercises/07-memory-performance-solutions.md`](./exercises/07-memory-performance-solutions.md).

## Self-assessment checklist

- [ ] I can read strides and say which axis is contiguous and what the byte step
      is. (§1)
- [ ] I can compute how many useful elements a traversal gets per cache line from
      the stride and the line size. (§1)
- [ ] I can explain why a reduction along axis 0 of a C-ordered array is not
      necessarily slow, and name the kernel property that makes it fast. (§2)
- [ ] I can design a measurement that isolates the layout effect and report it
      with element counts. (§3, §4)
- [ ] I can compute the break-even number of passes for a contiguity copy. (§5)
- [ ] I can explain why BLAS is layout-insensitive but a mixed-layout product is
      not. (§6)
- [ ] I can state the memory hierarchy and place a $1000^3$ model within it. (§7)
- [ ] I can name one case in my own work where I optimised arithmetic that was
      already bandwidth-bound. (§10)
