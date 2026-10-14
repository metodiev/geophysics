---
id: 19-06-01
title: "Computer Architecture, Memory Hierarchy and Roofline Thinking"
level: graduate
prereqs: ["19-01-01", "19-01-02"]
tags: [numerical-modelling, hpc, architecture, memory-hierarchy, roofline, bandwidth]
---

# Computer Architecture, Memory Hierarchy and Roofline Thinking

## Learning objectives

By the end of this lesson you will be able to:

1. **Measure** the sustained bandwidth of a kernel against working-set size and
   identify the overhead regime, the cache-resident regime and the plateau.
2. **Compute** the arithmetic intensity of a kernel from its FLOP and byte
   counts, and predict its rate from another kernel's measured bandwidth.
3. **Verify** the roofline prediction by comparing the measured FLOP-rate ratio
   of two kernels with the ratio of their intensities.
4. **Measure** the cost of a strided access against a contiguous one and explain
   it in terms of cache lines.
5. **Account** for the bytes a numpy expression actually moves, including its
   temporaries, and explain why the obvious removal of temporaries was slower in
   the measurement.
6. **Decide**, for a given kernel, whether parallelism can help at all, from the
   measured plateau rather than from a specification.

## Prerequisites

- [19-01-01 Discretisation: Grids, Nodes, Cells and Degrees of Freedom](../01-numerical-foundations/01-discretisation-concepts.md) —
  the grids whose kernels are measured here.
- [19-01-02 Truncation Error, Order of Accuracy and Convergence Rates](../01-numerical-foundations/02-convergence-and-error.md) —
  the measurement discipline: a claim without a number is not a claim.
- [03-12 Building Numerical Simulation Code in Python](../../03-scientific-computing/12-numerical-simulation-python/README.md) —
  the vectorised solver whose inner loop this lesson makes expensive or cheap.

All models and data in this module are **SYNTHETIC**.  Every number in this
lesson is a **measurement on the machine that ran the
demonstration**, printed by `code/hpc_architecture_demo.py`. All kernels, array
sizes and grids are **SYNTHETIC** teaching values. No hardware model name, no
vendor specification and no published benchmark is quoted, and no cache size is
stated as fact: the demonstration prints the *transitions* it measures, and where
a cache-line size is needed it is labelled an assumption.

## 1. The only two resources

A numerical kernel is limited by one of two things: how fast arithmetic can be
issued, or how fast bytes can be moved. Which one dominates is decided by the
**arithmetic intensity**

$$I = \frac{\text{floating-point operations}}{\text{bytes moved}}
\qquad [\text{flop/byte}],$$

and by the machine's peak values. The roofline picture is

$$\text{achieved rate} \le \min\left(\text{peak flops},\; I \times
\text{peak bandwidth}\right).$$

Nothing in this lesson needs a specification sheet, because both quantities can
be **measured**: the peak bandwidth is what a streaming kernel achieves at a
large working-set size, and the shape of the curve is the memory hierarchy. That
is the whole reason to measure instead of quoting.

## 2. Measuring the hierarchy with one kernel

Use the same kernel at eight sizes: $y \leftarrow a x + y$ (a "triad"),
$\mathrm{float64}$, with the traffic counted as it is *implemented* by numpy —
$x$ is read, the product $a x$ is materialised as a temporary, that temporary is
read, $y$ is read and written: five 8-byte passes, $40$ bytes per element.

| elements | per array | time (ms) | GB/s |
|---|---|---|---|
| 1024 | 8 KB | 0.0009 | 44.72 |
| 8192 | 64 KB | 0.0038 | 85.49 |
| 65536 | 512 KB | 0.0223 | 117.38 |
| 262144 | 2048 KB | 0.0870 | **120.47** |
| 1048576 | 8192 KB | 0.3626 | 115.67 |
| 4194304 | 32768 KB | 1.6736 | 100.25 |
| 8388608 | 65536 KB | 3.1164 | 107.67 |

Three regimes, and the boundaries between them are the measurable content:

- **Overhead regime.** At $8$ KB the measured rate is only $44.7$ GB/s. The
  array is tiny; what is being timed is the per-call cost, not memory.
- **Cache-resident regime.** The maximum, $120.5$ GB/s, occurs at $2$ MB per
  array. The working set fits in the fastest on-chip storage and the rate is set
  by that storage.
- **Plateau.** From $8$ MB to $64$ MB per array the rate sits between $100$ and
  $116$ GB/s — the main-memory rate for this kernel on this machine.

The plateau value is the number the rest of the lesson uses. It is a property of
one machine, one kernel and one run; a reader on other hardware should
expect different numbers and the same shape.

## 3. Roofline thinking without a vendor peak

Two checks make the roofline more than a diagram.

### 3.1 Three kernels, one resource

Traffic and FLOP counts, measured at $8.4\times10^{6}$ elements:

| kernel | flops/elem | passes | bytes/elem | GB/s | GFLOP/s |
|---|---|---|---|---|---|
| copy $y = x$ | 0 | 2 | 16 | 115.45 | — |
| scale $y = ax$ | 1 | 2 | 16 | 105.48 | 6.5924 |
| triad $y = ax + y$ | 2 | 5 | 40 | 107.80 | 5.3899 |

The bandwidth spread across the three is $1.095\times$; the FLOP rate varies by
$6.59/5.39 = 1.22\times$. The intensities are $0/16$, $1/16 = 0.0625$ and
$2/40 = 0.05$ flop/byte, so the predicted FLOP-rate ratio triad/scale is
$0.05/0.0625 = 0.800$. Measured: $0.818$. That is the roofline statement in its
measurable form: **kernels on the same memory system have rates in the ratio of
their arithmetic intensities.**

### 3.2 Predicting one kernel from another

The triad's time predicted from the *copy* kernel, which is an entirely separate
measurement:

$$t_{\text{pred}} = \frac{5 \times 8 \times 8\,388\,608\ \text{bytes}}
{115.45\times10^{9}\ \text{bytes/s}} = 2.906\ \text{ms},$$

against a measured $3.113$ ms — a ratio of $1.071$. No FLOP peak, no vendor
number and no specification appears in that prediction; it uses one measurement
to predict another, which is the form of reasoning this module insists on.

## 4. Access patterns and the cache line

Bandwidth is not the whole story; the *pattern* sets how many bytes must be
fetched to obtain one useful value. Summing $4.19\times10^{6}$ doubles and
comparing per-element cost at various strides:

| stride | elements | time (ms) | time per element, relative to stride 1 |
|---|---|---|---|
| 1 | 4194304 | 0.4942 | 0.93 |
| 2 | 2097152 | 0.3768 | 1.41 |
| 4 | 1048576 | 0.3714 | 2.78 |
| 8 | 524288 | 0.3470 | 5.20 |

Per useful element, a stride-8 sweep costs about $5\times$ a contiguous one. The
explanation needs the **assumption** that a cache line holds $8$ doubles
(64 bytes): then a stride-8 element occupies a whole line, of which one double is
used. The measured penalty is close to that ratio but not equal to it, because a
CPU core also has prefetching and out-of-order execution, and because part of the
strided access still lands in the same line as another element. The demo states
the line size as an assumption precisely because it does not measure it.

## 5. Where the bytes actually go: a stencil

A five-point Laplacian update on a $2048^{2}$ grid touches $4\,186\,116$ interior
points. Ideal counting: five reads and one write, $48$ bytes per point. Numpy's
natural expression,

```python
out[1:-1, 1:-1] = u[:-2, 1:-1] + u[2:, 1:-1] + u[1:-1, :-2] + u[1:-1, 2:] - 4*u[1:-1, 1:-1]
```

materialises four temporaries, so the traffic is closer to
$(5 + 4 + 4 + 1)\times 8 = 112$ bytes per point. Measured:

| implementation | time (ms) | GB/s of ideal bytes | GFLOP/s |
|---|---|---|---|
| naive expression | 8.305 | 24.20 | 2.520 |
| no-temporary rewrite | 9.635 | 20.85 | 2.172 |
| `scipy.ndimage.laplace` | 44.613 | 4.50 | 0.469 |

Three measured facts, and the second is the one that contradicts intuition:

1. The naive and no-temporary forms agree to **0.0** — identical arithmetic,
   different expression.
2. **Removing the temporaries was $1.16\times$ slower.** The rewrite replaces one
   contiguous pass with five strided row-slice passes and five call overheads.
   Numpy has no fused expression evaluator, so "fewer temporaries" and "faster"
   are different sentences.
3. `scipy.ndimage.laplace` is $5.37\times$ slower than the naive expression and
   agrees with it in the interior to $3.6\times10^{-15}$ — the same operator with
   a different boundary treatment at the edges.

Comparing the naive expression with the copy-kernel prediction for its own byte
count, $112$ bytes per point at $115.45$ GB/s gives $4.061$ ms against $8.305$ ms
measured — a ratio of $2.045$. So the stencil reaches about half of its own
bandwidth prediction, and the gap is the cost of strided row slicing rather than
of the arithmetic.

**Why this belongs in a geophysics module.** A 3-D wavefield solver is a stencil
with roughly the same intensity per point. If the measured stencil runs at
$2.5$ GFLOP/s and about $24$ GB/s of ideal traffic on this machine, then the
number of time steps per second is fixed by bytes, not by FLOPs, and a faster
processor changes nothing. Whether threads, a GPU or a vector unit can help is
then decided by whether each of them has *more* bandwidth, not by their peak
FLOP rate.

### 5.1 What would change on another machine, and by how much

The three measured threshold values — the overhead regime, the cache-resident
maximum and the plateau — are what a reader must re-measure. What transfers is the
sensitivity of a conclusion to them. Take the stencil prediction of $4.061$ ms:
it was computed from the plateau ($115.45$ GB/s via the copy kernel) and the byte
count ($112$ per point). On a machine whose plateau is twice as high, the same
arithmetic gives $2.03$ ms; on a machine with half the plateau, $8.12$ ms, which
would make the stencil exactly as fast as the *measured* naive implementation and
therefore hide the stride effect entirely.

That is the useful form of the lesson: **the experiment is portable, the
conclusion is conditional.** A kernel that appears bandwidth limited on one
machine can be latencies-of-the-implementation limited on another, and the
observed order in a size sweep — overhead, then cache, then plateau — is the
diagnostic that tells you which regime your machine is in.

## 6. Assumptions and regime of validity

1. **A single thread, no BLAS.** No measurement here involves threaded BLAS or
   multi-threaded numpy. With those enabled, the numbers above change without any
   change of code, which is itself a reproducibility hazard
   ([07 Reproducibility and Provenance](07-reproducible-hpc.md)).
2. **Timings are this machine's.** The best-of-$N$ timings vary between runs by
   several per cent; the reported values move with them. The *ratios* and the
   *shape* are the transferable content.
3. **A stated traffic model.** Every GB/s figure is a byte-count model times a
   measured time. Section 2 counts five passes for the triad because that is what
   numpy emits; a fused kernel would move it closer to three, and the same wall
   time would then correspond to a lower reported bandwidth.
4. **A stated cache-line assumption.** Section 4's explanation uses 8 doubles per
   line as an assumption; the demonstration measures times, not cache geometry.
5. **`best_of` timings, not means.** The reported numbers are minima, which
   removes scheduling noise but hides variance. A production measurement should
   report both.
6. **One machine, one operating system.** Nothing here extrapolates to a
   multi-socket node or to a GPU; those introduce NUMA effects and a different
   memory system, and both must be measured separately — see
   [04 GPU Computing](04-gpu-computing.md).

## 7. A fully worked example

Take the triad at $8\,388\,608$ elements and check the arithmetic of the model.

- **Bytes:** 5 passes × 8 bytes = 40 bytes per element, so
  $40 \times 8\,388\,608 = 3.355\times10^{8}$ bytes = $335.5$ MB.
- **Measured time:** $3.116$ ms, so the measured bandwidth is
  $3.355\times10^{8} / 3.116\times10^{-3} = 1.077\times10^{11}$ B/s
  $= 107.7$ GB/s, matching the printed value.
- **FLOPs:** 2 per element, so $1.678\times10^{7}$ flops in $3.116$ ms
  $= 5.39$ GFLOP/s, again matching the table.
- **Intensity:** $2/40 = 0.05$ flop/byte.
- **Prediction from the copy kernel:** copy moves $2\times8 = 16$ bytes per
  element at $115.45$ GB/s, i.e. $0.1386$ ns per element; the triad at $40$ bytes
  per element should take $2.5\times$ as long per element, and since there are
  the same number of elements, $2.5 \times 1.202$ ms $= 3.01$ ms against $3.116$
  ms measured.

The agreement is at the $3\%$ level and it is derived entirely from measured
numbers — no specification enters, which is exactly why the check is worth doing.
When it *fails* (as it did for the stencil, by a factor $2.045$), the failure
localises the problem: the kernel is doing more memory traffic than the model
counts, or it is not streaming.

## 8. Python demonstration

`code/hpc_architecture_demo.py` measures the size sweep, the three-kernel table,
the strided comparison and the three stencil implementations, and prints the
predictions next to the measurements.

```bash
cd 19-numerical-modeling-hpc/06-hpc-and-parallel-computing/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python hpc_architecture_demo.py
```

## 9. Exercises

Full sets with worked solutions are in
[`exercises/01-hpc-architecture-exercises.md`](./exercises/01-hpc-architecture-exercises.md)
and [`exercises/01-hpc-architecture-solutions.md`](./exercises/01-hpc-architecture-solutions.md).

- **★** Compute the arithmetic intensity of $y \leftarrow ax + y$ under a
  three-array traffic model and under the five-pass model actually measured.
- **★** From the size table, state the working-set size at which the measured
  rate first exceeds $100$ GB/s.
- **★★** Predict the time of the scale kernel from the copy kernel and compare
  with the table.
- **★★** A kernel performs $20$ flops per element and moves $24$ bytes. State
  whether it is compute bound on this machine, using the measured plateau only.
- **★★★** Design an experiment that separates the two candidate explanations for
  the stencil's $2.045$ ratio: row-slice strides and per-call overhead.

## Mastery checkpoint

Without notes:

> A three-array kernel $y \leftarrow ax + y$ is measured at $3.1$ ms on
> $8.4\times10^{6}$ elements, and a copy kernel at $115.5$ GB/s. **(a)** Compute
> the triad's arithmetic intensity under a three-array model and under the
> five-pass model, and say which the measurement supports. **(b)** Predict the
> triad's FLOP rate from the measured bandwidth. **(c)** State why a kernel that
> already achieves the measured plateau cannot be made faster by adding threads.

A worked version appears in the lesson-01
[solutions](./exercises/01-hpc-architecture-solutions.md).

## Common pitfalls

1. **Quoting a peak from a specification instead of measuring a plateau.** The
   only bandwidth that matters is the one your kernel achieves at its working-set
   size.
2. **Comparing kernels by FLOP rate alone.** Two kernels with different
   intensities have different rates on the same machine by construction.
3. **Counting bytes by array size.** Temporaries, shifted views and reductions
   all add traffic, and the stencil's factor $2.045$ is exactly that effect
   unaccounted for.
4. **Assuming "fewer allocations" means "faster".** It was 16% slower here,
   measured.
5. **Ignoring the overhead regime.** At $8$ KB the kernel ran at $44.7$ GB/s; a
   large fraction of a small workload can be call overhead, and parallelising it
   makes it worse, not better.
6. **Measuring once.** A single timing of a millisecond-scale kernel is a draw
   from a noisy distribution; the demonstration reports the best of several runs
   and says so.

## Related modules

- [02 Shared-Memory Parallelism: OpenMP and Threading](02-shared-memory-parallelism.md) —
  what happens to these numbers when work is split across cores.
- [03 Distributed-Memory Parallelism with MPI](03-mpi-distributed.md) — the same
  question across a network, where the ratio of bytes to arithmetic changes.
- [04 GPU Computing: CUDA, OpenCL and Portability Layers](04-gpu-computing.md) —
  the same intensity argument with a much wider memory bus.
- [19-02 Finite-Difference Methods](../02-finite-difference-methods/README.md) —
  the stencils measured here.
- [03-13 Testing, Profiling and Packaging](../../03-scientific-computing/13-testing-profiling-packaging/README.md) —
  the profiling tools that produce the tables above.
