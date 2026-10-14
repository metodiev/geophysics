---
id: 19-06-04
title: "GPU Computing: CUDA, OpenCL and Portability Layers"
level: research
prereqs: ["19-06-01", "19-06-02", "19-02-03"]
tags: [numerical-modelling, hpc, gpu, simt, coalescing, precision, portability]
---

# GPU Computing: CUDA, OpenCL and Portability Layers

## Learning objectives

By the end of this lesson you will be able to:

1. **Express** a stencil as a pure data-parallel kernel, in the two forms a GPU
   programmer chooses between — index gather and shifted slices — and **verify**
   that they compute the same field.
2. **Measure** the cost difference between the two forms and explain it as an
   indexing cost.
3. **Count** the memory transactions a warp of 32 lanes implies for contiguous,
   strided and scattered patterns, and compare that arithmetic with a measured
   CPU penalty.
4. **Measure** the fixed per-call cost of a kernel and compute the array size
   below which that cost dominates.
5. **Measure** the time and the accuracy consequences of single precision,
   including the accumulation error of a reduction.
6. **State** what a portability layer does and does not guarantee.

## Prerequisites

- [19-06-01 Computer Architecture, Memory Hierarchy and Roofline Thinking](01-hpc-architecture.md) —
  intensity, bandwidth and the measured plateau.
- [19-06-02 Shared-Memory Parallelism: OpenMP and Threading](02-shared-memory-parallelism.md) —
  the measurement discipline for a parallel kernel.
- [19-02-03 Boundary Conditions: Dirichlet, Neumann, Absorbing, PML](../02-finite-difference-methods/03-fd-boundary-conditions.md) —
  why the edge treatment of a stencil is a modelling decision and not a detail.

Every number in this lesson is a **CPU measurement** or an **explicit arithmetic
count from a stated assumed geometry**, printed by `code/gpu_computing_demo.py`.
The demo **does not use a GPU**: no CUDA, OpenCL or array-API device is present or
timed, and no GPU timing, vendor figure or hardware model name appears anywhere.
All array sizes, thread geometries and precision examples are **SYNTHETIC**
teaching values.

All models and data in this module are **SYNTHETIC**.

## 1. The SIMT model, in the language you already have

A GPU program is written as an operation applied to every element, with no
communication between iterations. That is exactly a numpy expression, which is why
the GPU programming model can be taught and measured on a CPU — with the caveat
that the *constants* differ by an order of magnitude and the *structure* does not.

The stencil of [01 §5](01-hpc-architecture.md) has two natural expressions:

```python
# index gather: every lane looks up its own four neighbours
nei = np.empty((n*n, 4), dtype=np.int64)      # built once
out[:] = 0.25*(u[nei[:,0]] + u[nei[:,1]] + u[nei[:,2]] + u[nei[:,3]])

# shifted slices: the offsets are arithmetic, not data
out.reshape(n, n)[1:-1, 1:-1] = 0.25*(a[:-2,1:-1] + a[2:,1:-1] + a[1:-1,:-2] + a[1:-1,2:])
```

Measured on a $1024^{2}$ grid:

| expression | time | ratio |
|---|---|---|
| gather-based | 4.708 ms | 2.86× |
| slice-based | 1.646 ms | 1.00× |
| agreement in the interior | **0.000** | — |

Both are data-parallel and both are correct; the gather is $2.86\times$ more
expensive on the CPU because it performs four indirections per element instead of
four arithmetic offsets. On a GPU the same choice appears as coalesced against
uncoalesced loads, which is the next section — and the lesson is that the
*expression* you choose for one kernel decides whether the memory system can help
you at all.

## 2. Coalescing: transactions implied by the access pattern

Assume, because the script does not measure it, that a **warp** is $32$
consecutive lanes and a memory **sector** is $32$ bytes $= 4$ doubles. Then the
number of distinct sectors touched by a 32-lane access is pure arithmetic:

| pattern | distinct sectors | useful doubles per sector |
|---|---|---|
| contiguous (lane $= i$) | 8 | 4.00 |
| stride 2 | 16 | 2.00 |
| stride 4 | 32 | 1.00 |
| stride 8 | 32 | 1.00 |
| scattered (random) | 28 | 1.14 |

A contiguous warp of 32 doubles touches 8 sectors and uses every double in them.
A stride-8 warp touches 32 sectors for the same 32 values and uses one double in
each: **four times the sectors for the same data**. That count is a property of
the geometry and of the assumed sector size, and it does not depend on which
device executes it.

The matching measurement on the CPU, on the same array:

| pattern | time | relative to contiguous |
|---|---|---|
| contiguous | 0.656 ms | 1.00× |
| stride 2 | 0.712 ms | 1.08× |
| stride 8 | 0.727 ms | 1.11× |

The CPU penalty is far smaller than the sector arithmetic would suggest, for
reasons worth naming: a CPU core fetches whole cache lines anyway, it prefetches,
and it executes out of order, so a partly-used line is often already in flight.
**The arithmetic is a transaction count, not a prediction of GPU time** — and
using it as one is exactly the kind of overclaim this module exists to prevent.

## 3. Launch overhead, and the crossover

Every kernel invocation has a fixed cost. On the CPU the analogue is the ufunc
call, measured at $0.37\ \mu\mathrm{s}$ on a $1024$-element array. The same call
on $16\,777\,216$ elements takes $3.100$ ms, i.e. $0.1848$ ns of marginal cost per
element. Dividing gives the size at which the fixed cost stops dominating:

$$\text{crossover} \approx \frac{0.37\ \mu\mathrm{s}}{0.1848\ \text{ns}} \approx 2029\
\text{elements}.$$

Two consequences:

- Below a couple of thousand elements per call, a numpy kernel is measuring call
  overhead, not arithmetic — which is why Section 2 of
  [01 §2](01-hpc-architecture.md) had to explain the $8$ KB row.
- **A kernel that does ten passes pays the fixed cost ten times.** On a GPU that
  fixed cost is the launch overhead, and a deep sequence of small kernels can be
  launch bound even though each one is fast. The standard remedies — fuse the
  passes, batch the small work, or keep the intermediate state on the device —
  are structural, not micro-optimisations. The *value* of the crossover differs
  between a CPU ufunc and a GPU launch; the trade it describes does not.

## 4. Precision: what half the bits cost and buy

Elementwise addition over $4\,194\,304$ values:

| dtype | time | 
|---|---|
| float64 | 1.404 ms |
| float32 | 0.617 ms |
| speedup | 2.274× |

and an accumulation of $10^{6}$ values against an exactly-rounded reference
(`math.fsum`):

| method | value | relative error |
|---|---|---|
| exact (`math.fsum`) | 295.4547659189917 | — |
| float64 pairwise | 295.4547659189916 | $3.848\times10^{-16}$ |
| float32 pairwise | 295.45452880859375 | $8.025\times10^{-7}$ |

The float32 error is about $2.1\times10^{9}$ times the float64 error — four
orders of magnitude of relative accuracy given up for a $2.27\times$ gain in this
kernel's time. That is a good trade for a stencil whose output feeds a nonlinear
step and a terrible one for a long accumulation, which is why mixed-precision
codes keep their **reductions** in double precision while their kernels run in
single. The number to carry away is the error ratio, and the lesson is that
precision is a per-operation decision, not a per-code one.

### 4.1 Occupancy, as a model with stated assumptions

A GPU executes a fixed number of threads at once, and the number that are resident
is limited by registers, shared memory and thread count. The reasoning is a small
arithmetic exercise with stated assumptions, and it is included because it is the
one part of GPU performance that a lesson without a GPU can still make precise:

- assume a device that can hold $2048$ resident threads per processing unit and a
  kernel using $40$ registers per thread;
- a register file of $65\,536$ registers per unit then allows
  $65\,536/40 = 1638$ threads, so occupancy is limited by registers to
  $1638/2048 = 80\%$;
- a block size of $256$ threads gives $6$ resident blocks, i.e. $1536$ threads and
  $75\%$ occupancy; a block size of $512$ gives $3$ blocks, $1536$ threads, the
  same occupancy; a block size of $1024$ gives $1$ block, $1024$ threads, $50\%$.

So above a point, a larger block reduces occupancy rather than improving it, and
the useful block size is the smallest that still amortises the block's own
overhead. **Every number in that paragraph is an assumption, not a measurement**:
the register file size, the per-unit thread limit and the register count all come
from a device this script cannot see. What is transferable is the shape of the
argument and the fact that occupancy is a *derived* quantity — which is exactly
why it belongs in a model, with its inputs on the page, rather than in a rule of
thumb.

## 5. Portability layers: what they guarantee

CUDA, OpenCL, HIP, SYCL and Python-level array APIs differ in syntax and agree on
the model: a grid of thread blocks, each block a set of threads executing the same
code, memory arranged in a hierarchy. A portability layer's job is to express that
model once. What it does **not** guarantee:

- **identical floating-point results.** Reduction orders differ between backends,
  and some compilers reassociate. A kernel that is bitwise reproducible on one
  backend may not be on another; see
  [07 Reproducibility and Provenance](07-reproducible-hpc.md).
- **identical performance.** Memory geometry, occupancy limits and cache
  behaviour are device properties. A kernel tuned for one device's block size is
  untuned on another.
- **identical numerical behaviour at the edges.** A boundary mode, a fused
  multiply-add and a fast-math flag each change the last bits and sometimes the
  physics.

The portability layer guarantees the *expression*; the measurement must be redone
per device. That is the same discipline the rest of this module applies to CPUs.

## 6. Assumptions and regime of validity

1. **No GPU was used.** All timings are CPU timings; every GPU-specific quantity
   is either an explicit arithmetic count from Section 2's assumed geometry or a
   statement of structure.
2. **Assumed thread geometry.** 32 lanes per warp and 32 bytes per sector are
   stated assumptions. A different sector size changes the counts by a constant
   factor and leaves the ordering of the patterns intact.
3. **The CPU is not a slow GPU.** The measured CPU stride penalty ($1.11\times$)
   and the sector count ($4\times$) disagree by a large factor, and both are
   correct statements about their own device. Do not transfer numbers between
   them; transfer the *argument*.
4. **A stencil on a regular grid.** Irregular gathers, atomics and load imbalance
   each change the analysis.
5. **Precision statements are about this accumulation.** Relative error depends
   on the number of terms, the conditioning of the sum and the summation order.
   $10^{-7}$ for a $10^{6}$-term float32 pairwise sum is a measurement, not a law.
6. **Correctness before speed.** A GPU kernel must be compared against a CPU
   reference on the same field; the gather/slice agreement of $0.000$ in Section 1
   is that test, and it is the test that catches a wrong index or a wrong
   boundary, not a performance measurement.

## 7. A fully worked example

Take the stencil of Section 1 on a $1024^{2}$ grid, written as a gather.

- **Work:** $1\,048\,576$ elements, each needing four neighbour loads and one
  store, i.e. five memory accesses and $4$ adds plus $1$ multiply.
- **Measured time:** $4.708$ ms, so the marginal cost is
  $4.708\times10^{-3}/1\,048\,576 = 4.49$ ns per element.
- **The same work in shifted-slice form:** $1.646$ ms, $1.57$ ns per element.
  The difference, $2.92$ ns per element, is the cost of four index-table lookups
  and the resulting non-sequential access.
- **What that implies for a time-stepped solver:** a solver doing $10^{5}$ steps
  on this grid would spend $470$ s in the gather form against $165$ s in the
  slice form, on this machine, for identical answers. That is the size of the
  decision, and it is decided before any GPU is involved.

Now convert it to the GPU-shaped question: if the same kernel were
transaction-limited, the sector arithmetic of Section 2 says the contiguous form
needs $8$ sectors per warp against $32$ for the gather's strided pattern, a factor
of $4$ in traffic. The measured CPU factor is $2.86$. The two agree in *direction
and order of magnitude* and disagree in detail, which is the honest summary:
sector arithmetic bounds the traffic, and it is not a timing model.

## 8. Python demonstration

`code/gpu_computing_demo.py` measures the two stencil expressions, counts sectors
for five access patterns, measures the launch-overhead crossover, and measures
fp32 against fp64 in both time and accuracy.

```bash
cd 19-numerical-modeling-hpc/06-hpc-and-parallel-computing/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gpu_computing_demo.py
```

## 9. Exercises

Full sets with worked solutions are in
[`exercises/04-gpu-computing-exercises.md`](./exercises/04-gpu-computing-exercises.md)
and [`exercises/04-gpu-computing-solutions.md`](./exercises/04-gpu-computing-solutions.md).

- **★** Compute the sector count for a warp accessing every $3$rd double.
- **★** State the crossover size from the two printed numbers.
- **★★** From the fp32/fp64 table, decide the precision of a $10^{6}$-term
  accumulation that must be accurate to $10^{-8}$ relative, and justify it.
- **★★** Explain why the CPU stride penalty and the GPU sector count differ by a
  factor of about four.
- **★★★** Design an experiment using only this demo's tools that decides whether
  the gather stencil's cost is indexing arithmetic or memory transactions.

## Mastery checkpoint

Without notes:

> A stencil is run as an index gather ($4.708$ ms) and as shifted slices
> ($1.646$ ms) on a $1024^{2}$ grid, and a warp of 32 lanes is assumed to fetch
> 32-byte sectors. **(a)** State the per-element cost of each form and the ratio.
> **(b)** Compute the sectors per warp for a contiguous and a stride-8 access, and
> say why the measured CPU ratio is smaller. **(c)** A single-precision
> accumulation of $10^{6}$ terms has relative error $8.0\times10^{-7}$; state
> whether it is acceptable for a residual norm and why.

A worked version appears in the lesson-04
[solutions](./exercises/04-gpu-computing-solutions.md).

## Common pitfalls

1. **Treating a sector count as a timing prediction.** It is a transaction count;
   the measured CPU penalty differs by a factor of four and both are right.
2. **Benchmarking below the crossover.** Anything under a few thousand elements
   measures call overhead, not the kernel.
3. **Using single precision everywhere because it is twice as fast.** The
   accumulation error grew by $2.1\times10^{9}$ in the measured example.
4. **Assuming a portability layer guarantees identical bits.** It guarantees the
   expression; reduction orders and reassociation differ per backend.
5. **Optimising the index arithmetic before checking the access pattern.** The
   gather's cost is dominated by its memory pattern, and the sector arithmetic is
   what localises that.
6. **Skipping the CPU reference.** A GPU kernel's first test is agreement with a
   CPU implementation on the same field; the measured $0.000$ in Section 1 is
   that test.

## Related modules

- [01 Computer Architecture, Memory Hierarchy and Roofline Thinking](01-hpc-architecture.md) —
  the intensity argument that decides whether a GPU is even the right device.
- [02 Shared-Memory Parallelism: OpenMP and Threading](02-shared-memory-parallelism.md) —
  the CPU answer to the same question.
- [05 Domain Decomposition and Load Balancing](05-domain-decomposition.md) —
  the multi-device version of the same decomposition.
- [07 Reproducibility and Provenance in HPC Workflows](07-reproducible-hpc.md) —
  what a mixed-precision, multi-backend code has to record.
- [19-02-05 Finite-Difference Acoustic and Elastic Wave Propagation](../02-finite-difference-methods/05-fd-wave-propagation.md) —
  the stencil that motivates all of this.
