---
id: 19-06-02
title: "Shared-Memory Parallelism: OpenMP and Threading"
level: research
prereqs: ["19-06-01", "19-01-03", "19-05-04"]
tags: [numerical-modelling, hpc, threading, openmp, gil, race-condition, load-balancing]
---

# Shared-Memory Parallelism: OpenMP and Threading

## Learning objectives

By the end of this lesson you will be able to:

1. **Explain** what the global interpreter lock does to a pure-Python workload,
   and **measure** the speedup it prevents.
2. **Decide**, from a measurement, whether a kernel can benefit from threads at
   all, by comparing its achieved rate with the single-thread plateau.
3. **Measure** the speedup of a compute-bound kernel and account for the gap from
   the ideal.
4. **Construct** a read-modify-write race and **demonstrate** the lost updates and
   the lock that removes them.
5. **Compare** a static schedule with a dynamic work queue on items of unequal
   cost, and state the bound each one obeys.
6. **Specify** a reduction whose result is independent of the number of workers,
   and name the quantity that must be fixed to achieve it.

## Prerequisites

- [19-06-01 Computer Architecture, Memory Hierarchy and Roofline Thinking](01-hpc-architecture.md) —
  the measured bandwidth plateau that decides whether threads can help.
- [19-01-03 Consistency, Stability and the Lax Equivalence Theorem](../01-numerical-foundations/03-consistency-stability.md) —
  partial updates and ordering, in the numerical setting.
- [19-05-04 Fast Multipole and Hierarchical Acceleration](../05-integral-equation-and-boundary-methods/04-fast-multipole.md) —
  the long-range sums that are the usual customers for a shared-memory pool.

All numbers are **measurements on the machine that ran the demo**, printed by
`code/shared_memory_parallelism_demo.py`. All workloads, chunk counts and item
weights are **SYNTHETIC** teaching values. No hardware model name and no
published scaling figure is quoted.

All models and data in this module are **SYNTHETIC**.

The demonstration starts only short-lived, bounded thread pools, each closed with
an explicit join before the next section. It spawns no process, no subprocess and
no MPI rank, and nothing hung: the whole file runs in about two seconds.

## 1. The lock in the middle

CPython executes bytecode under one lock, the **global interpreter lock** (GIL).
Threads are still *concurrent* — a thread waiting on I/O releases the lock, and
native code inside a numpy kernel releases it — but Python-level arithmetic does
not run in parallel. The measurement, with the same total work split four ways:

| work | serial | 4 threads | speedup |
|---|---|---|---|
| pure-Python `sum(i*i)` over $3.2\times10^{6}$ items | 88.735 ms | 95.399 ms | **0.930×** |

Four threads are slightly *slower* than one: the work is unchanged and the
scheduling is not free. The conclusion is not "threads are useless" — it is that
**the language layer decides**, and the question must be asked per kernel.

## 2. The same experiment on a bandwidth-bound kernel

Now the same pattern on a numpy elementwise kernel, `out = x + 1` over
$4\,194\,304$ doubles, repeated $40$ times (so that start-up, at about a
millisecond per thread, is not the whole story):

| | time | bandwidth |
|---|---|---|
| serial | 29.021 ms | 92.50 GB/s |
| 4 threads (4 chunks) | 95.888 ms | 27.99 GB/s |
| speedup | **0.303×** | |

Threading a bandwidth-bound kernel made it $3.3\times$ slower. Two mechanisms
compound:

1. one thread already reaches $92.5$ GB/s, close to the plateau measured in
   [01 Computer Architecture](01-hpc-architecture.md), so there is very little
   headroom left for the memory system to give;
2. each numpy call releases and re-acquires the GIL, and four threads repeatedly
   contending for it wastes the time the memory system would have used.

The demonstrable rule: **if the single-thread kernel is at the plateau, threads
cannot help it.** The measurement in [01 §2](01-hpc-architecture.md) is what tells
you the plateau; this measurement is what happens when you ignore it.

## 3. The same experiment on a compute-bound kernel

Sort four arrays of $1\,048\,576$ doubles, one per thread:

| | time | speedup | efficiency |
|---|---|---|---|
| serial | 131.088 ms | — | — |
| 4 threads | 34.996 ms | **3.746×** | 93.6% |

A comparison sort moves each element through the cache several times, releases
the GIL, and therefore has work to overlap. The gap from the ideal $4\times$ is
real and expected: the four arrays contend for the same cache levels and the same
memory system, and thread start-up is not zero.

A library-managed pool gives the same lesson with no Python scheduling in the
path at all:

| `scipy.fft.rfft2` on a $2048^{2}$ array | time | speedup |
|---|---|---|
| `workers=1` | 12.931 ms | — |
| `workers=4` | 4.710 ms | **2.746×** |

Three kernels, three outcomes — $0.93\times$, $0.30\times$, $3.75\times$ — and
the only way to know which one you have is to measure it.

## 4. A race, and the lock that removes it

A read-modify-write is three operations, and another thread can run between them.
Four threads, $200$ increments each, on one shared counter:

| variant | final value (of 800) | lost updates |
|---|---|---|
| no lock | 222 | **578** |
| with a `threading.Lock` | 800 | 0 |

The demonstration inserts `time.sleep(0)` between the read and the write purely
to widen the window enough to see the loss in a demo of this length. The window
exists without it; that is why the same bug appears in production codes as a
rare, irreproducible wrong answer, and why it is the hardest class of parallel
bug to reproduce.

Two corollaries used repeatedly in this folder:

- **An accumulator shared between workers needs a reduction, not a lock per
  addition, if it is hot.** Locking every increment is correct and slow; the
  standard remedy is per-worker partials merged at the end.
- **A partial update to a shared field needs a schedule that cannot read a
  half-updated value.** In a Jacobi sweep every point reads only the previous
  sweep's values, so parallelisation is safe without locks; in a Gauss-Seidel
  sweep it is not. That distinction is a property of the *algorithm*, not of the
  language.

## 5. Scheduling: static blocks against a dynamic queue

Twenty-four items with weights $1$–$8$ (three repeats of $[1,\dots,8]$), total
work $108$ units, four workers.

| schedule | makespan | work per block |
|---|---|---|
| static contiguous blocks of 6 | 4.39 ms | $[21, 25, 29, 33]$ |
| dynamic queue, heaviest first | 3.94 ms | — |
| measured ratio static/dynamic | **1.116** | largest block / ideal $= 1.22$ |

The static schedule cannot beat its largest block: $33$ units against an ideal
$27$, a bound of $1.22$. The dynamic queue is bounded only by the largest single
item, here $8$ units. The measured times reflect the bounds (ratio $1.116$
against the bound ratio $1.22$) and are noisy at this scale — Python scheduling
and the thread pool's own bookkeeping are a large fraction of a $4$ ms run.

The OpenMP correspondence is exact: `schedule(static)` assigns contiguous blocks
at compile time, `schedule(dynamic)` and `schedule(guided)` hand out items at run
time. The rule of thumb follows from the bound, not from folklore: **static when
the per-iteration cost is uniform, dynamic when it is not, and never dynamic for
a body whose iteration costs a few nanoseconds**, because the queue overhead then
exceeds the imbalance it removes.

### 5.1 The OpenMP correspondence

Nothing in this lesson used a pragma, and the correspondence with compiled
OpenMP is nevertheless exact in structure:

| this lesson | OpenMP equivalent | the measured fact behind it |
|---|---|---|
| `ThreadPoolExecutor(max_workers=W)` with `pool.submit` | `#pragma omp parallel for` | work split into a fixed number of chunks |
| the four futures joined with `f.result()` | the implicit barrier at the end of the parallel region | the pool is closed before the next section is timed |
| `threading.Lock` around a read-modify-write | `#pragma omp critical` or an `atomic` clause | $578$ of $800$ updates lost without it |
| static blocks of items | `schedule(static)` | makespan bounded by the largest block ($33$ against an ideal $27$) |
| one queue taken item by item | `schedule(dynamic)` | measured ratio $1.116$ against a bound ratio of $1.22$ |
| per-worker partials merged in a fixed order | `reduction(+:x)` | one digest across pool sizes, four across chunk counts |

The one place the correspondence is *not* exact is the GIL: a compiled OpenMP
loop has no interpreter lock, so the $0.930\times$ and $0.303\times$ results of
Sections 1 and 2 are Python-specific. The compute-bound result ($3.746\times$)
is the one that transfers most directly, because it is limited by cache and memory
behaviour rather than by the interpreter.

## 6. Reproducibility: what must be fixed

Reduce an array of $1\,048\,576$ doubles in eight chunks, merging the partial sums
in chunk order, and vary the pool size:

| pool size | digest of the result |
|---|---|
| 1 | `fd08746e9736c23b` |
| 2 | `fd08746e9736c23b` |
| 4 | `fd08746e9736c23b` |
| 8 | `fd08746e9736c23b` |

One distinct digest. Now vary the **number of chunks** instead:

| chunks | digest |
|---|---|
| 1 | `245a8cc32cd14752` |
| 3 | `238fb977da721cc0` |
| 8 | `fd08746e9736c23b` |
| 16 | `99c2fb586effd721` |

Four distinct digests across six chunk counts, and the eight-chunk result differs
from numpy's own pairwise sum by **2.00 ulp**. The conclusion is sharp:

> The **decomposition**, not the number of workers, decides the bits. A
> reproducibility claim must name the decomposition.

This is pursued further in [07 Reproducibility and Provenance in HPC Workflows](07-reproducible-hpc.md),
and it is the reason [19-06-03](03-mpi-distributed.md) treats a reduction's order
as part of its specification.

## 7. Assumptions and regime of validity

1. **CPython, this version, this machine.** The GIL is an implementation detail
   of CPython; other implementations and future versions differ. The *structure*
   of the argument — measure before you parallelise — does not.
2. **Threads share one memory system.** All measured speedups are limited by
   shared bandwidth and shared cache. A NUMA machine adds locality effects that
   must be measured separately.
3. **Bounded pools with explicit joins.** Every pool is closed with a context
   manager, which is also what makes the demo's own timing meaningful. A pool
   left open keeps threads alive and its work may bleed into the next
   measurement.
4. **Small workloads.** Tens of milliseconds is enough to see the effects above
   but not enough to be a benchmark. The numbers include start-up and scheduling
   costs that a long run would amortise.
5. **`time.sleep(0)` in the race demo is a widening device.** The loss is real
   without it; the *magnitude* is not representative.
6. **Correctness is not optional.** A parallel kernel must produce the same
   answer as the serial one, bit for bit or within a stated tolerance. Every
   partitioned scheme in this folder is checked that way — see
   [03 §2](03-mpi-distributed.md) and [05 §5](05-domain-decomposition.md).

## 8. A fully worked example

Four threads, a kernel that takes $29.021$ ms serially, and a measured thread
start-up cost of about $1$ ms per thread. Model the parallel time as

$$t(P) = \frac{t_{\text{work}}}{P} + t_{\text{start}} + t_{\text{contention}} .$$

- Ideal term: $29.021/4 = 7.255$ ms.
- Start-up: $4 \times 1 = 4$ ms, already more than half the ideal parallel time.
- Predicted total without contention: $11.3$ ms, i.e. a speedup of $2.6\times$.
- Measured: $95.888$ ms, a speedup of $0.303\times$.

The prediction fails by a factor of $8.5$, and the failure identifies the missing
term: contention for the GIL and for the memory system, which the model does not
contain. The lesson is not that models are useless; it is that **this** model has
one term too few, and the measurement says so. Add the missing term and the model
becomes the statement "for a kernel already at the bandwidth plateau, threads
cannot help", which is exactly what
[01 Computer Architecture](01-hpc-architecture.md) measured independently.

## 9. Python demonstration

`code/shared_memory_parallelism_demo.py` runs all six sections above: the GIL
comparison, the bandwidth-bound and compute-bound thread comparisons, the
library pool, the race with and without a lock, the two schedules, and the
reduction-digest experiment.

```bash
cd 19-numerical-modeling-hpc/06-hpc-and-parallel-computing/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python shared_memory_parallelism_demo.py
```

## 10. Exercises

Full sets with worked solutions are in
[`exercises/02-shared-memory-parallelism-exercises.md`](./exercises/02-shared-memory-parallelism-exercises.md)
and [`exercises/02-shared-memory-parallelism-solutions.md`](./exercises/02-shared-memory-parallelism-solutions.md).

- **★** From first principles: state why $0.930\times$ is consistent with a lock held for the whole workload.
- **★** Compute the efficiency of the sort speedup $3.746\times$ on four threads.
- **★★** Using the start-up model of Section 8, find the workload size at which
  thread start-up is $10\%$ of the parallel time.
- **★★** A stencil's iteration costs $2.5$ ns per point. State whether
  `schedule(dynamic)` is justified, with a number.
- **★★★** Design the experiment that decides whether the $0.303\times$ result is
  caused by GIL contention or by memory contention, and state the observable
  that separates them.

## Mastery checkpoint

Without notes:

> A code spends $88.7$ ms serially on a pure-Python loop and $131.1$ ms on four
> sorts. **(a)** Predict the four-thread time for each and state which one the
> experiment confirms. **(b)** A reduction gives one digest across pool sizes
> $1\ldots8$ and four digests across chunk counts; state what must be fixed for a
> reproducibility claim. **(c)** A colleague proposes eight threads for a kernel
> already running at $92.5$ GB/s. State the argument that settles the proposal
> before any code is written.

A worked version appears in the lesson-02
[solutions](./exercises/02-shared-memory-parallelism-solutions.md).

## Common pitfalls

1. **Parallelising before measuring the plateau.** If one thread is at the
   bandwidth limit, more threads move less data per unit time.
2. **Assuming "numpy releases the GIL" implies "threads are faster".** It is a
   necessary condition and nothing more; the measurement above shows a
   $3.3\times$ loss.
3. **Locking a hot inner loop.** Correct and slow. Use per-worker partials and
   one merge.
4. **Trusting a race that "never happened".** The window is microseconds wide and
   the failure is a wrong number once in a million iterations.
5. **Choosing a schedule by habit.** Static and dynamic are bounded by different
   quantities; the bounds are computable before the run.
6. **Claiming reproducibility without naming the decomposition.** Pool size did
   not change the digest; chunk count did, by 2 ulp.

## Related modules

- [01 Computer Architecture, Memory Hierarchy and Roofline Thinking](01-hpc-architecture.md) —
  the plateau these measurements are compared against.
- [03 Distributed-Memory Parallelism with MPI](03-mpi-distributed.md) — the same
  arithmetic split across address spaces, where the reduction order is explicit.
- [05 Domain Decomposition and Load Balancing](05-domain-decomposition.md) — the
  scheduling question in its geophysical form.
- [07 Reproducibility and Provenance in HPC Workflows](07-reproducible-hpc.md) —
  what a reproducibility claim must contain.
- [19-05-04 Fast Multipole and Hierarchical Acceleration](../05-integral-equation-and-boundary-methods/04-fast-multipole.md) —
  a workload whose cost distribution is nothing like uniform.
