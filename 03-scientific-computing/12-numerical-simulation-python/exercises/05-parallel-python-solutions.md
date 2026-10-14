# Solutions — 03-12-05 Parallelism in Python: Multiprocessing, Threads, Numba, JAX

> **Read this after attempting the exercises.** Values attributed to the demo are
> its actual output. Values marked *measured* come from a modified copy with the
> modification stated. No solution quotes a wall-clock time: the exercises are
> designed so that elapsed seconds are never the answer.

---

## ★1 — The mechanisms

| mechanism | shares memory | releases GIL | scales across nodes |
|---|---|---|---|
| `threading` | yes | only in C extensions | no |
| `multiprocessing` | no | yes (separate interpreters) | no |
| `numba` `@njit` | yes | yes (compiled code) | no |
| `jax.jit` | yes | yes (compiled code) | no |
| `mpi4py` | no | yes | **yes** |

---

## ★2 — Why threads help NumPy but not Python

Python bytecodes execute under a global interpreter lock, so only one thread runs
Python at a time: two threads on a pure-Python loop share the GIL and take the
same total time as one, plus overhead. Compiled code — NumPy's C inner loops,
`numba`, `jax`, `mpi4py` — **releases the lock** for the duration of a large
array operation, so several threads can be inside NumPy simultaneously and the
work genuinely parallelises.

The practical rule: **threads are for code that has already left the
interpreter.** If the hot spot is Python, threads cannot help it; either
vectorise it or compile it.

---

## ★3 — The measured machine

```
logical CPUs visible          : 10
start method for processes    : spawn (macOS default for Python 3.8+)
```

The start method matters because `spawn` starts a fresh interpreter and
re-imports the module in each worker. A function defined inside `main()` — a
closure — cannot be pickled and sent to a spawned worker, so `ProcessPoolExecutor`
raises a pickling error. On Linux the default is `fork`, which inherits the
parent's memory and *does* accept closures, so code that works on Linux can fail
on macOS for a reason that has nothing to do with the program's logic. Define
worker functions at the top level.

---

## ★4 — What is installed

| module | status | what it would be for |
|---|---|---|
| `numba` | **not installed** | JIT compilation of Python loops |
| `jax` | **not installed** | compiled array programs, GPU, automatic differentiation |
| `mpi4py` | **not installed** | domain decomposition across nodes |
| `dask` | available | task graphs larger than memory |
| `joblib` | available | process-level parallelism for loops, efficient array serialisation |

Stating what is missing is part of the result: a demonstration that imports
`numba` and fails teaches nothing, while one that reports "not installed" and
states the pattern lets a reader with `numba` apply it.

---

## ★5 — Three questions before parallelising

1. **Is the work released from the GIL?** (If not, threads are useless.)
2. **Is the result order-dependent?** (If so, pin the reduction order.)
3. **Is the partition balanced?** (Arithmetic, computable before running.)

The question before all three is whether there is anything to parallelise at
all, which only a profiler answers.

---

## ★★6 — Bit-identical results across worker counts

The demonstration splits the work by worker count, and the measurement shows
that **two different things** have to be right for the answers to match.

| workers | max abs field diff (halo = 40) | field identical | `fsum` of every value | chunk-partial reduction (difference from serial exact sum) |
|---|---|---|---|---|
| 1 | 0.000e+00 | yes | +3.626637981440e+02 | +5.684e−14 |
| 2 | 0.000e+00 | yes | +3.626637981440e+02 | +5.684e−14 |
| 4 | 0.000e+00 | yes | +3.626637981440e+02 | +5.684e−14 |
| 8 | 0.000e+00 | yes | +3.626637981440e+02 | 0.000e+00 |

Three steps are needed, not one:

1. **A halo.** Each worker needs the `sweeps` = 40 cells of data on either side
   that its stencil reaches, wrapped periodically. With that, the chunked field
   is bit-identical to the serial field — measured 0.000e+00 at every worker
   count. Without it, each chunk wraps at its own seam and the measured error is
   84 cells wrong at two seams, 163 at four, 335 at eight (about 42 per seam,
   i.e. `sweeps` plus the two seam cells), with maximum differences of 3.847e−01,
   3.155e−01 and 7.180e−01.
2. **Identical data.** Each worker must receive the same underlying field, not
   generate its own. An early revision of the demonstration let each worker seed
   its own random field from the chunk offset, so the chunk size changed the
   data; the totals came out as 1.168e+03, 4.084e+02 and 1.652e+02 against a
   serial 3.627e+02. That is a factor-of-three disagreement — a different
   problem, not different arithmetic.
3. **An exactly-rounded accumulator.** `math.fsum` over every computed value
   reproduces the serial exact sum bit for bit at all four worker counts. If the
   *inexact* per-chunk `np.sum` values are reduced instead, the total moves by
   5.684e−14 at 1, 2 and 4 workers (and happens to be exact at 8): the physics is
   right and the number changed, because the summation tree changed.

**On combining partials in completion order:** the answer depends on the
reduction used, and the demonstration measures which ones are vulnerable — over
500 permutations of 100 chunk partials, `math.fsum` gives one distinct total,
`np.sum` gives 43 spread over 6.679e−13, and a manual `+=` loop gives 60 spread
over 1.322e−12. A regression test that hashes the output would fail intermittently
for the last two.

Two things must **not** be inferred from this table, and the demonstration prints
a second table specifically to prevent it:

- **`math.fsum` is the only unconditional guarantee.** It is correctly rounded,
  so it cannot depend on order. That is a statement about the algorithm.
- **The built-in `sum` is not.** It uses Neumaier compensated summation on
  CPython 3.12+, which makes it exact far more often than naive addition, but it
  is not correctly rounded. Whether it is order-independent **depends on the
  data**: measured on two 100-value datasets through the same 200 permutations,
  it gives 1 distinct total on the chunk partials (compensation active — every
  partial already carries ~1e−15 of rounding) and 12 on 100 unit-scale standard
  normals, where its set of totals is *identical* to the manual `+=` loop's
  (compensation inert — `sum()` degenerates to naive addition, to the bit).
  The earlier draft of this solution generalised the first case to the algorithm;
  the second case is the counterexample.
- Compensation is still worth having: `sum([1e16, 1.0, -1e16])` returns **1.0**
  where a manual loop returns **0.0**, and the same holds at $10^{100}$ and
  $10^{300}$ (measured by the demonstration).

---

## ★★7 — Grouping changes the answer

*Measured* on a million standard normal values; the exactly-rounded reference is
`math.fsum(values) = -1.127855489320e+02`:

| grouping | chunks | sum | absolute error | relative error |
|---|---|---|---|---|
| `np.sum` whole array | 1 | −1.127855489320178e+02 | −1.137e−13 | 1.008e−15 |
| chunks of 1000 | 1000 | −1.127855489320178e+02 | −8.527e−14 | 7.560e−16 |
| chunks of 10000 | 100 | −1.127855489320179e+02 | −1.563e−13 | 1.386e−15 |
| chunks of 100000 | 10 | −1.127855489320178e+02 | −1.137e−13 | 1.008e−15 |

Every error is a few ulp: the relative differences are at the $10^{-15}$ level,
one to six times machine epsilon ($2.2\times10^{-16}$).

**Why "agree to ten digits" is not a reproducibility test:** ten significant
digits on a value of magnitude $10^2$ is $10^{-8}$ absolute, and every one of
these sums agrees to that level — while their *bit patterns differ*. A
reproducibility test must compare the full value (a checksum of the bytes, or an
exact-equality assertion), not a rounded print. The errors here are harmless
numerically and fatal to reproducibility, and those two statements are both
true.

Note also that the error does not decrease monotonically with the number of
chunks: 1000 chunks (7.560e−16) is *more* accurate than 100 chunks (1.386e−15).
Chunking happens to align with the pairwise reduction tree in a favourable way.
There is no rule here to exploit — only a reason to use an exactly-rounded
reduction and stop reasoning about it.

---

## ★★8 — Verifying the idle fractions

With $N = 1\,003\,000$ and the remainder given to one worker:

| $W$ | $N \div W$ | remainder | smallest | largest | idle (%) |
|---|---|---|---|---|---|
| 3 | 334333 | 1 | 334333 | 334334 | 0.00020 |
| 7 | 143285 | 5 | 143285 | 143290 | 0.00300 |
| 16 | 62687 | 8 | 62687 | 62695 | 0.01200 |

The formula is
$\text{idle} = (\max - \text{mean})/\max \times 100$ with the mean equal to
$N/W$. For $W = 7$: mean $= 143285.714$, max $= 143290$,
idle $= (143290 - 143285.714)/143290 = 0.0030$ % ✓.

The point of the exercise is not the small numbers but the *method*: this
quantity is computable from the partition alone, before running anything, and is
the same on every machine. Contrast with a speedup measurement, which is a
property of the machine and the load at the moment of measurement.

---

## ★★9 — Which reductions are order-dependent, measured

*Measured*: 100 chunk partials (each a `np.sum` over 10 000 values), permuted
into 500 random orders.

| reduction | distinct totals | spread | equals the sorted result |
|---|---|---|---|
| `math.fsum` | **1** | 0.000e+00 | yes |
| built-in `sum` | **1** | 0.000e+00 | yes |
| `np.sum` of the permuted list | **43** | 6.679e−13 | no |
| manual `+=` loop | **60** | 1.322e−12 | no |

`math.fsum` is *correctly rounded* — the result is the nearest `float64` to the
exact mathematical sum — so there are no intermediate roundings for the order to
affect, and its order-independence is a guarantee. `np.sum` reduces pairwise over
the array it is handed, so permuting the input changes the summation tree.
A manual `+=` loop reduces strictly left to right and is the most sensitive of
the four.

**The trap is the second row.** Reading it as "the built-in `sum` is
order-independent" is a generalisation the measurement does not support, and an
earlier draft of this solution made exactly that mistake. Repeat the same
measurement on two 100-value datasets through the same 200 permutations:

| dataset | `math.fsum` | `sum()` | manual `+=` | `sum()` set == manual set |
|---|---|---|---|---|
| the 100 chunk partials above | 1 | **1** | 48 | False |
| 100 unit-scale standard normals | 1 | **12** | **12** | **True** |

`sum()` uses Neumaier compensated summation on CPython 3.12 and later, which is
*not* the same as correct rounding. On the chunk partials each partial already
carries a rounding error of order $10^{-15}$, so the compensation term is non-zero
and the compensated sum lands on the correctly-rounded answer. On unit-scale data
the compensation term stays zero: `sum()` degenerates to naive addition and
becomes as order-dependent as `+=`, matching it for every permutation. So
"`sum()` is order-independent" is a property of `sum()` *and the data* — which
means it is not a property you can rely on. **Only `math.fsum` supports the
unconditional claim.**

Compensation is still a large improvement where naive addition fails worst:
`sum([1e16, 1.0, -1e16])` returns **1.0** (the exact answer) where a manual loop
returns **0.0**, and the demonstration measures the same at $10^{100}$ and
$10^{300}$.

Finally, note the qualification that `fsum` does **not** remove: the partial sums
themselves are computed with `np.sum`, whose result depends on how the array was
chunked. `fsum` pins the combination, not the per-chunk summation. **Pinning the
grouping and pinning the combination are two separate requirements.**

---

## ★★10 — The condition for thread determinism

The condition is that **the partition is fixed before the threads start** and the
combination order is fixed after. The demonstration splits into four blocks and
sums each block in a thread; the total is then formed with `fsum` in block order.
Measured: identical totals at 1, 2 and 4 threads (`all identical : True`).

What would break it:

- **A dynamic work queue** (`imap_unordered`, `as_completed`) that assigns
  blocks to threads as they become free: the assignment varies between runs, so
  the combination order varies.
- **A reduction inside the workers** (each thread adding into a shared total):
  the interleaving of additions depends on scheduling.
- **A different chunk size at different thread counts**: the grouping of the
  arithmetic changes, so the rounding changes.

Which of those actually costs you the answer depends on the accumulator, and
that is measurable rather than arguable: with `math.fsum` the permuted partials
give one distinct total, with `np.sum` 43, with a manual `+=` loop 60 (★★6).
**Fixing the partition is necessary, but using an exactly-rounded reduction
makes the whole question moot** — and both are one line of code. Note that a
compensated-but-not-correctly-rounded accumulator sits in between and cannot be
trusted without measuring it on your own data, as ★★6 shows.

---

## ★★★11 — Vectorising instead of compiling

*Measured* by replacing the per-chunk Python loop with a NumPy expression that
applies the diffusion sweeps to the whole array using `np.roll`:

| implementation | chunks | 1 worker sum | identical to the loop? |
|---|---|---|---|
| Python loop with `np.roll` per chunk | 1 | +3.626637981440e+02 | — |
| vectorised whole-array expression | 1 | +3.626637981440e+02 | yes (bit-identical here) |

Both values are the demonstration's own 1-worker result: the chunked path with a
halo returns a field whose maximum absolute difference from the serial
whole-array result is exactly 0.0, and `math.fsum` over both fields agrees to the
last bit.

The two agree bit-for-bit on this problem because the arithmetic per element is
the same sequence of operations in the same order — the vectorised version does
not change the *order* of the operations per element, only how many elements are
processed per instruction.

**What I could not measure:** the effect of `numba`. It is not installed, so the
claim "`@njit` removes the interpreter from this loop" is a statement about the
tool, not a result about this code. What I *can* say is what the loop's structure
permits: it has no data-dependent branches, so it is a candidate for both
vectorisation and compilation; and it is already vectorised, so compilation would
add little.

That distinction — between a claim I verified and a claim I am repeating from
documentation — is worth stating explicitly, and it is why the demonstration
prints the installation table.

---

## ★★★12 — A reproducible parallelism experiment

**Work-partition metric.** For $N$ points and $W$ workers, report the chunk
sizes actually used, the largest-to-smallest ratio, and the idle fraction
$(\max - \text{mean})/\max$. These are computable before the run and identical on
every machine.

**Determinism check.** Run at $W = 1, 2, 4, 8$ and assert that every result is
**bit-identical** to the serial one (`==`, not `isclose`). Report the number of
workers, the number of chunks and the assertion's outcome.

**Numerical-identity check.** Compute the same quantity with a *different*
grouping (for example chunk sizes 1000 and 10 000) and report the difference
against an exactly-rounded reference. This quantifies how much the answer depends
on the partition, which bounds the error a future change of worker count would
introduce.

**Why those three characterise correctness but not speed:** they are properties
of the *code* — the partition it produces, the order it reduces in, and the
sensitivity of the result to that order. They are invariant under a change of
machine. Speed is not: it depends on the core count, the memory bandwidth, the
cache hierarchy, the BLAS library and the machine's load at the moment of
measurement. A speedup figure is valid for the machine and the run it was
measured on, and quoting it as a property of the implementation is the mistake
this exercise is designed to prevent.

---

## ★★★13 — A review response in three sentences

"Please state the reduction order and the work partition, because a 3.5×
speedup on 8 cores with different results usually means the parallel version
groups the floating-point arithmetic differently rather than executing the same
arithmetic faster. A bit-identity check at 1, 2 and 4 workers, plus the
difference against an exactly-rounded (`math.fsum`) reference, would resolve
whether the change is rounding or a bug, and my expectation is a difference of a
few ulp with agreement to all printed digits. I would accept the difference if
you show that it is confined to the last two significant figures, that the
quantity of interest changes by less than its stated uncertainty, and that the
serial and parallel versions agree to within that uncertainty on a second,
independent problem — otherwise the parallel result is a different experiment
and should be reported as one."
