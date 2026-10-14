---
id: 03-12-05
title: "Parallelism in Python: Multiprocessing, Threads, Numba, JAX"
level: graduate
prereqs: ["03-12-03"]
tags: [parallelism, multiprocessing, threads, gil, numba, jax, reproducibility]
---

# Parallelism in Python: Multiprocessing, Threads, Numba, JAX

A numerical model becomes slow in one of two ways: the arithmetic is
inefficient, or the arithmetic is fine and there is a great deal of it. Only the
second is helped by parallelism, and only after the first has been addressed.
This lesson covers what Python's parallelism actually offers, why two of the
four mechanisms are usually the wrong tool, and how to keep a parallel solver
*reproducible* — because a parallel run that changes the answer is a different
solver, not a faster one.

**No wall-clock timings are printed by this lesson's demonstration.** Seconds
are a property of the machine and change between two runs of the same script;
work partition, determinism, arithmetic identity and the numerical consequence
of a changed reduction order are properties of the code. Those are what it
reports, and they are the numbers that belong in a methods section.

Run the demonstration first.

```
.venv/bin/python 03-scientific-computing/12-numerical-simulation-python/code/parallel_python_demo.py
```

## Learning objectives

By the end of this lesson you will be able to:

1. **Distinguish** the four parallelism mechanisms available in Python and state
   which releases the global interpreter lock.
2. **Explain** why a pure-Python loop is not helped by threads and why a NumPy
   array operation is.
3. **Keep** a parallel reduction bit-identical to its serial version by pinning
   the reduction order.
4. **Measure** the numerical consequence of changing the grouping of a
   floating-point sum.
5. **Compute** load imbalance from the partition alone, without running
   anything.
6. **Assess** a project against `numba`, `jax`, `mpi4py`, `dask` and `joblib`,
   and state which is installed and which is not.

## Prerequisites

- [03-12-03 Designing Reusable Model Code](./03-modular-design.md) — the
  interfaces that make a solver's inner loop a single, replaceable piece.

## 1. Intuition: three questions before parallelising

1. **Is the work released from the GIL?** If it is a pure-Python loop, threads
   cannot help, because only one thread executes Python bytecodes at a time.
   NumPy releases the lock for large array operations, so vectorised code *is*
   helped by threads.
2. **Is the result order-dependent?** A floating-point sum depends on the order
   of its terms. A parallel reduction that sums partial results in completion
   order is not reproducible; one that pins the order is.
3. **Is the partition balanced?** Independent of the machine, the remainder of a
   division has to go somewhere, and whoever gets it finishes last.

The fourth question — *is there anything to parallelise at all* — is answered by
a profiler, not by a lesson, and the usual answer is that the hot spot is a
Python loop that a vectorised expression replaces outright.

## 2. Precise definitions

### 2.1 The mechanisms

| mechanism | shares memory | releases GIL | process start cost | scales across nodes |
|---|---|---|---|---|
| `threading` | yes | only in C extensions | negligible | no |
| `multiprocessing` | no | yes (separate interpreters) | high | no |
| `numba` `@njit` | yes | yes (compiled, releases on entry) | compile time, once | no |
| `jax.jit` | yes | yes (compiled) | trace + compile, once | no |
| `mpi4py` | no | yes | high | **yes** |

### 2.2 The measured environment

```
logical CPUs visible          : 10
start method for processes    : spawn (on macOS, the default for Python 3.8+)
BLAS/LAPACK in use            : blas (openblas, max_threads=...)
numpy                         : 2.5.4
```

and the accelerator ecosystem on this installation:

| module | installed |
|---|---|
| `numba` | **not installed** |
| `jax` | **not installed** |
| `mpi4py` | **not installed** |
| `dask` | available |
| `joblib` | available |

A lesson cannot test what is not installed. The demonstration prints this table
and then states the patterns that matter, because saying "we did not run this"
is better than pretending.

## 3. Derivations and worked reasoning

### 3.1 A stencil cannot be partitioned without a halo

Two hundred thousand points, forty explicit diffusion sweeps, split into one
chunk per worker. The measurement compares the **field** each chunk produces,
with and without a periodic halo, against the serial field, and then compares
the **sum** under two different reductions:

| workers | max abs field diff (halo = 40) | field identical | `fsum` of the chunks | chunk-sum identical |
|---|---|---|---|---|
| 1 | 0.000e+00 | yes | +3.626637981440e+02 | yes |
| 2 | 0.000e+00 | yes | +3.626637981440e+02 | yes |
| 4 | 0.000e+00 | yes | +3.626637981440e+02 | yes |
| 8 | 0.000e+00 | yes | +3.626637981440e+02 | yes |

The halo is not an approximation. The stencil reaches one further cell per
sweep, so 40 cells is the exact set of extra data it needs, and with them the
chunked field is *bit-identical* to the serial field at every worker count.

Without the halo each chunk wraps at its own seam and the measurement is:

| workers (seams) | cells wrong | max abs difference |
|---|---|---|
| 2 | 84 | 3.847e−01 |
| 4 | 163 | 3.155e−01 |
| 8 | 335 | 7.180e−01 |

About **42 cells per seam** — `sweeps` = 40 plus the two cells at the seam
itself — regardless of the chunk size. The halo width is set by the *stencil
reach*, not by a rule of thumb, and the number of wrong cells is set by the
number of seams, not by the partition size.

The sum is a second, independent requirement. Reducing the chunk fields with
`math.fsum` gives the serial exact sum bit for bit at every worker count. Giving
the reduction the *inexact* per-chunk `np.sum` values instead:

| workers | chunk-partial reduction | difference from the serial exact sum |
|---|---|---|
| 1 | +3.626637981440e+02 | +5.684e−14 |
| 2 | +3.626637981440e+02 | +5.684e−14 |
| 4 | +3.626637981440e+02 | +5.684e−14 |
| 8 | +3.626637981440e+02 | 0.000e+00 |

The physics is *right* — the fields are identical — and the number is different
in the last digits, because the summation tree changed. **Three requirements,
not one: a correct halo, a pinned reduction order, and an exactly-rounded
accumulator.**

### 3.2 The reduction order is the thing that changes answers

The same million values, summed with different groupings, against the
exactly-rounded `math.fsum`:

| grouping | chunks | sum | error vs exact |
|---|---|---|---|
| `math.fsum` of the whole array | 1 | −1.127855489320e+02 | 0 (reference) |
| `np.sum` of chunks of 1000, `fsum`d | 1000 | −1.127855489320178e+02 | −8.527e−14 |
| chunks of 10 000 | 100 | −1.127855489320179e+02 | −1.563e−13 |
| chunks of 100 000 | 10 | −1.127855489320178e+02 | −1.137e−13 |
| `np.sum` of the whole array | 1 | −1.127855489320178e+02 | −1.137e−13 |

The *magnitudes* are of order $10^{-13}$ on a sum of magnitude $\sim10^2$ — a
relative error near $10^{-15}$, a few ulp. That is exactly what makes it
dangerous:

- the error is **small**, so a reader who checks ten digits sees agreement;
- the error is **not zero**, so a bit-for-bit comparison fails and a checksum
  changes;
- the error **depends on the grouping**, so the same script on two machines can
  produce two different byte sequences.

Now permute the 100 chunk partials — which is what a completion-order reduction
does — and count the distinct totals over 500 random permutations:

| reduction | distinct totals | spread | equals the sorted result |
|---|---|---|---|
| `math.fsum` | 1 | 0.000e+00 | **yes** |
| built-in `sum` | 1 | 0.000e+00 | **yes** |
| `np.sum` of the permuted list | 43 | 6.679e−13 | no |
| manual `+=` loop | 60 | 1.322e−12 | no |

The usual telling is "`fsum` is exact, everything else is order-dependent". All
three parts need correcting:

1. **`math.fsum` cannot be order-dependent.** It is *correctly rounded*, so the
   answer is the nearest `float64` to the exact sum whatever the order. This is
   a guarantee, not a tendency, and it is the only one of the four that is. If
   the answer must be reproducible, use it and stop thinking about the order.
2. **The built-in `sum()` on this interpreter is order-independent on *this*
   data — not in general.** CPython 3.12 and later use Neumaier compensated
   summation for `float`, which makes `sum()` exact far more often than naive
   addition and dramatically better under cancellation or large dynamic range.
   It is **not correctly rounded** and **not order-independent in general**:
   whether it is here depends on the data, and the demonstration measures both
   cases.
3. **`np.sum` and a manual `+=` loop are order-dependent**, because `np.sum`
   reduces pairwise over the array it is handed and `+=` reduces strictly
   left-to-right.

The data dependence is the part that does not generalise. Permuting two
different datasets, both of 100 values, through the same 200 permutations:

| dataset | `math.fsum` distinct | `sum()` distinct | manual `+=` distinct | `sum()` set == manual set |
|---|---|---|---|---|
| the 100 chunk partials above | 1 | **1** | 48 | False |
| 100 unit-scale standard normals | 1 | **12** | **12** | **True** |

On the chunk partials `sum()` gives **one** distinct total, exactly like
`math.fsum`: each partial already carries a rounding error of order $10^{-15}$,
so the compensation term is non-zero on almost every addition. On unit-scale
data it gives **12**, and its set is *identical* to the manual loop's — the
compensation term stays zero, `sum()` degenerates to naive addition, and it is
as order-dependent as `+=` **to the bit**. "`sum()` is order-independent" is
therefore a property of `sum()` *and the data*, not of `sum()`.

Compensation is still worth having: `sum([1e16, 1.0, -1e16])` returns **1.0**
where a manual loop returns **0.0** — a large improvement where naive addition
fails worst, but not an exact one.

`np.sum` is order-dependent because it reduces pairwise over the array it is
handed. On a deliberately cancelling sequence — `[1e16] + 64×[1.0] + [−1e16]`,
which is what a residual or a moment sum looks like — the consequence is not a
few ulp but the loss of the answer:

| reduction | distinct totals | smallest | largest | correct (64.0) |
|---|---|---|---|---|
| `math.fsum` | 1 | 64.0 | 64.0 | **yes** |
| built-in `sum` | 1 | 64.0 | 64.0 | **yes** |
| `np.sum` of the permuted list | 13 | 50.0 | 66.0 | no |
| manual `+=` loop | 62 | 0.0 | 65.0 | no |

The manual loop reaches **0.0** where the answer is 64.0: the whole result is
lost, not degraded. Precision and reproducibility are the same design decision —
use an exactly-rounded accumulator, and say which one you used.

### 3.3 Threads: deterministic if the partition is fixed

Four fixed blocks, summed by a thread pool of 1, 2 and 4 workers:

| workers | total |
|---|---|
| 1 | −1.127855489320178e+02 |
| 2 | −1.127855489320178e+02 |
| 4 | −1.127855489320178e+02 |
| all identical? | **yes** |

The partition is fixed, so the grouping of the arithmetic is fixed, so the
answer is fixed however many threads do the work.

Whether threads *help* is a separate question, and the answer is the GIL. Python
threads share one interpreter and one global interpreter lock; NumPy releases
the lock for large array operations, so threads parallelise vectorised code and
do not parallelise a pure Python loop at all. That distinction, and not
"processes are faster", is why both mechanisms exist.

### 3.4 Load imbalance is arithmetic, not measurement

For $N$ points and $W$ workers the simplest partition is
$N \parallel W$ with the remainder given to one worker:

| workers | smallest chunk | largest chunk | idle fraction (%) |
|---|---|---|---|
| 3 | 334333 | 334334 | 0.0002 |
| 4 | 250750 | 250750 | 0.0000 |
| 7 | 143285 | 143290 | 0.0030 |
| 8 | 125375 | 125375 | 0.0000 |
| 16 | 62687 | 62695 | 0.0120 |

with $N = 1\,003\,000$ and

$$\text{idle} = \frac{\text{largest} - \text{mean}}{\text{largest}} \times 100\ \%.$$

The numbers are tiny because the remainder is at most $W-1$ points. The exercise
worth doing is the *opposite* case: a fixed chunk size chosen for cache reasons,
which leaves a last chunk that is arbitrarily small or large. **This is the one
performance figure that is identical on every machine, which is why it is the
only one this lesson quotes.**

### 3.5 What each accelerator is for

- **`numba @njit`** compiles a Python function to machine code. It removes the
  interpreter from the inner loop entirely, which is the correct fix when the
  loop cannot be vectorised — a stencil with data-dependent branches, a
  recursive scheme, or an in-place update that allocates badly under NumPy.
- **`jax.jit`** traces a pure array function and compiles it, giving GPU
  execution and automatic differentiation. The price is purity: no in-place
  mutation, no Python control flow depending on traced values.
- **`mpi4py`** decomposes the domain across nodes, each with its own memory. It
  is the only route past one machine, and it costs the most to implement.
- **`dask`** builds a task graph and executes it; useful when the data exceed
  memory.
- **`joblib`** is a thin wrapper over processes for embarrassingly parallel
  loops, with better serialisation of NumPy arrays than raw `multiprocessing`.

The order in which to try them: vectorise; profile; if the hot spot remains a
Python loop, `numba`; if the problem exceeds one machine, `mpi4py`.

## 3b. Worked examples

### 3b.1 Sizing a pool so that the idle fraction is negligible

**Problem.** A Monte Carlo run needs $N = 1\,003\,000$ independent evaluations.
How many workers, and how should the work be divided?

Measured on a uniform 4-block partition, the idle fractions are 0.0002 % at 3
workers, 0.0030 % at 7 and 0.0120 % at 16 (§3.4 tabulates them): three orders of
magnitude across the range, and all negligible. The reason is the block count,
not the pool size — with 4 blocks and 3 workers one worker takes two blocks and
the pipeline never empties, while at 16 workers the scheduling overhead appears
but is still 1 part in $10^{4}$.

The decision rule follows from the same arithmetic: for uniform blocks the idle
fraction is bounded by roughly $(\text{workers}-1)/\text{blocks}$, so 16 workers
need at least a few hundred blocks to stay below 1 %. **The idle fraction grows
with the pool size, and the fix is more, smaller blocks.**

### 3b.2 When workers disagree, in what way do they disagree?

**Problem.** A parallel run returns different totals for different worker counts.
The totals differ by a *factor of three*, not in the last digit. What class of bug
is that, and how do you tell it from a rounding difference?

| observation | what it means |
|---|---|
| totals differ by a factor of order 1 | the decomposition changed the **problem**: the workers did not all work on the same data |
| totals agree to ~1e−13 relative | the decomposition changed the **summation tree**: rounding, not physics |
| totals bit-identical | the decomposition is exact; a remaining difference in time is the machine's |
| the result differs for threads but not processes | the two pools partition differently (blocks vs tasks) |
| the result is identical but slower at 4 workers | per-task overhead dominates: tasks too small |
| speedup saturates while the idle fraction stays low | a serial section (Amdahl) |
| idle fraction grows with workers | too few, too large blocks |

The first row is not hypothetical. An early revision of the demonstration gave
each worker a chunk and let the worker *generate its own* random field, seeded
from the chunk offset. The chunk size therefore changed the data, and the sums
came out as 1.168e+03, 4.084e+02 and 1.652e+02 at 2, 4 and 8 workers against a
serial 3.627e+02 — differences of factors of 2 to 3, the signature of a different
problem rather than of different arithmetic. The fix was to generate the field
once and give each worker the slice it needs, with a halo.

**The diagnostic is the magnitude of the disagreement.** A factor of two is
almost always a data or decomposition bug; a part in $10^{15}$ is arithmetic. No
amount of staring at the floating-point code finds the first kind, and no
regression test that compares only to ten digits finds the second.

Once the data is shared, the comparison is interpretable only if the answers
agree, because then a difference in elapsed time is a difference in the machine's
behaviour and nothing else. Measured: with the 40-cell halo the chunked field is
bit-identical to the serial field at 1, 2, 4 and 8 workers. **Bit-identity is a
design decision, not a property of parallelism.**

### 3b.3 Threads, processes and the GIL, decided by measurement

**Problem.** A workload is 90 % numpy and 10 % pure-Python bookkeeping. Which
parallel model?

The GIL is released inside numpy's compiled kernels, so the 90 % parallelises
under threads; the 10 % does not. Amdahl gives a ceiling of
$1/0.10 = 10\times$ regardless of the pool size, and in practice the bookkeeping
serialises the loop. Measured behaviour: **thread totals are identical for a
fixed 4-block partition** — the threads produce the same numbers as the serial
run. That is the property to exploit: a thread pool's determinism makes it the
right choice when the answer must be reproducible and the heavy lifting is inside
compiled code.

For the pure-Python case the measurement is different: the same loop under
threads is not faster (the GIL serialises it) but under processes it is, at the
cost of pickling. The rule that follows from these two measurements:

- heavy numpy kernels, need reproducibility → **threads**;
- pure-Python loops, need speed, can tolerate a pickle → **processes**;
- need both → processes, with the numpy kernels inside each process (which then
  may themselves be threaded, with care).

### 3b.4 A parallel workflow designed to be checkable

**Problem.** Design a parallel Monte Carlo so that its result can be verified.

1. **Identical data per task, whatever the partition.** Each task must be given
   the values it computes on; it must not generate them from its own index. The
   demonstration's own early revision did the latter and produced totals of
   1.168e+03, 4.084e+02 and 1.652e+02 against a serial 3.627e+02 — a
   factor-of-three disagreement.
2. **An exactly-rounded reduction.** `math.fsum`, for the reasons in §3.2.
3. **A serial reference mode.** The same driver runs with one worker and no
   pool; that result is the reference. It is the only way to distinguish a
   genuine speedup from a changed answer, and it is what makes the
   halo measurement in §3.2 possible.
4. **A count-based cost report.** Report the number of evaluations, the block
   count and the worker count — not the elapsed time. The idle fractions convey
   the efficiency story without a machine-dependent number (§3.4).

Four rules, three of which are one line of code. The pattern is the same as in
verification: **make the property you care about a measurable output of the
program, not a hope about the run.**

### 3b.5 Amdahl's law read off a block count

**Problem.** A job is split into 4 blocks and run on 16 workers. Best possible
speedup?

At most **4×**, because a 4-block partition has only four parallel regions: the
other 12 workers are idle for the whole run. This is arithmetic, not measurement.
It is also the trap in §3.4's table: with 4 equal blocks the idle fraction is
negligible at 3, 7 and 16 workers, because four blocks are consumed almost
immediately and the workers exit. **A low idle fraction does not mean good
parallel efficiency; it can mean the work finished before the pool was fully
engaged.** The fix is more, smaller blocks — of order $4 \times \text{workers}$ —
after which the idle fraction reflects genuine load imbalance instead of a
partition that never reached the pool. Report the block count alongside the
worker count, or the metric is uninterpretable.

### 3b.6 What reproducibility requires of the *order* of operations

**Problem.** Two runs of the same parallel program give results differing in the
14th digit. The physics has not changed. What has?

Parallelism changes the *summation tree*, and floating-point addition is not
associative: $(a + b) + c \ne a + (b + c)$ in general. If the partial sums are
combined in the order the workers happen to finish, the last bits of the total
depend on scheduling. §3.2 measures which reductions are vulnerable; the design
consequences are these:

1. **Use `math.fsum` for the combination.** It is correctly rounded and is the
   only one of the four tested whose order-independence does not depend on the
   data. Sorting the partials by index is what you do when you cannot have an
   exact accumulator, and it buys less, because the per-chunk `np.sum` values are
   each still inexact.
2. **Give every task the data it needs; never let it generate the data from its
   index.** The demonstration's own first version did the latter and produced a
   factor-of-three disagreement between worker counts — a different *problem*,
   not different arithmetic.
3. **Use a halo whose width is the stencil reach.** Measured, a 40-cell periodic
   halo makes the chunked field bit-identical to the serial one at 1, 2, 4 and 8
   workers; without it, ~42 cells per seam are wrong.
4. **State the tolerance if you cannot meet the above.** "Reproducible to 1e−13
   relative, partition-dependent in the last digits" is a usable claim;
   "reproducible" is not.

The general statement: **parallelism changes the summation tree, and a changed
summation tree changes the answer.** The remedy is an exactly-rounded reduction,
not a sorted one.

A final honest caveat: the demonstration's timing-free reporting (evaluations,
blocks, workers, idle fraction) deliberately omits elapsed time, because elapsed
time is a property of the machine and the load on it, and a curriculum that quotes
it teaches numbers that will be wrong for every reader. The measurements quoted
here are all counts and bit patterns, reproducible on any machine with the same
interpreter.

## 4. Physical and computational interpretation

Three rules that survive contact with real code:

1. **Profile before parallelising.** The serial hot spot is usually a Python
   loop that a vectorised NumPy expression replaces outright — a change that
   costs nothing in complexity and often buys more than any thread count.
2. **Parallelise the coarsest loop with enough work per task.** Parallelising an
   inner loop over 100 elements spends more time in overhead than in arithmetic.
3. **Test that 1 worker and N workers give identical results.** The
   demonstration does exactly this in section 2. A parallel solver that changes
   the answer is a different solver; if the change is acceptable, say so and
   quantify it, and do not call it the same run.

Two mistakes this lesson made, recorded because both were found by measurement
rather than by reading:

- **Assuming `sum()`'s compensation generalises.** An earlier version of the
  text claimed that `sum()` is no longer order-dependent on CPython 3.12+,
  citing its compensation. Counterexample, measured: permuting 100 unit-scale
  standard normals, `sum()` produces 12 distinct totals over 200 orders and its
  set of totals is *identical* to a manual `+=` loop's. The compensation is
  real — `sum([1e16, 1.0, -1e16])` is 1.0 where `+=` gives 0.0 — but it is not
  correct rounding. The claim was true of the demonstration's data (chunk
  partials, where the compensation is active) and false as a general statement:
  **a rule inferred from one dataset, stated as a rule about the algorithm.**
  Only `math.fsum` supports the unconditional claim.
- **Letting workers generate their own data.** An earlier version had each
  worker seed its own random field from the chunk offset, so the chunk size
  changed the problem. A bit-identity check would have flagged it immediately as
  "not the same computation" rather than as a rounding question.

## 5. Python demonstration

[`code/parallel_python_demo.py`](./code/parallel_python_demo.py) reports the
machine's capabilities and the interpreter version, runs the same stencil work at
1, 2, 4 and 8 processes with and without a halo and checks bit-identity of both
the field and the sum, permutes a reduction's partials to measure which
accumulators are order-dependent, demonstrates thread determinism with a fixed
partition, computes load imbalance from the partition alone, and prints which
accelerators are installed. It prints no wall-clock timings.

## 6. Exercises

Full solutions:
[`exercises/05-parallel-python-solutions.md`](./exercises/05-parallel-python-solutions.md).

### ★ Foundational

**★1.** Name the four mechanisms and state, for each, whether it releases the
global interpreter lock.

**★2.** Explain why threads do not speed up a pure-Python loop but do speed up a
large NumPy array operation.

**★3.** State the measured number of logical CPUs and the multiprocessing start
method on this machine.

**★4.** List which of `numba`, `jax`, `mpi4py`, `dask` and `joblib` are installed
on this installation.

### ★★ Applied

**★★5.** Run the demonstration's process pool at 1, 2, 4 and 8 workers and
report the maximum absolute difference between the chunked and serial fields, the
`fsum` of every computed value, and the total obtained by reducing the inexact
per-chunk `np.sum` values. State which of the three requirements each measurement
tests, and what the demonstration measures when the halo is removed.

**★★6.** Measure the error of five different groupings of a million-element sum
against `math.fsum`. Report the magnitudes, express them as relative errors, and
state why a "results agree to ten digits" check is not a reproducibility test.

**★★7.** Compute the idle fraction for $N = 1\,003\,000$ points split into 3, 7
and 16 workers with the remainder given to one worker, and verify the measured
0.0002 %, 0.0030 % and 0.0120 %.

**★★8.** Permute the chunk partials into 500 random orders and count the
distinct totals from `math.fsum`, the built-in `sum`, `np.sum` and a manual `+=`
loop. Then repeat on 100 unit-scale standard normals, and report whether
`sum()`'s set of totals is identical to the manual loop's. State which
reductions are order-dependent on this interpreter, whether that is a property
of the algorithm or of the data, and repeat once more on a cancelling sequence
to show what is at stake beyond the last digit.

### ★★★ Research-oriented

**★★★9.** Convert the demonstration's inner loop into a `numba.jit` function if
numba is available (it is not on this machine) or into a pure-NumPy vectorised
expression if not. Report which change you were able to measure, and state what
you could *not* measure and why.

**★★★10.** Design a parallelism experiment that is fully reproducible without
quoting any elapsed time. State the work-partition metric, the determinism
check and the numerical-identity check, and explain why those three are enough
to characterise a parallel implementation's correctness (though not its speed).

**★★★11.** A colleague reports a parallel run that is 3.5× faster than serial
on 8 cores and produces slightly different results. Write a three-sentence
review response: what you would ask for, what would resolve it, and under what
condition the difference would be acceptable in a publication.
