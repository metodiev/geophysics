---
id: 19-06-05
title: "Domain Decomposition and Load Balancing"
level: research
prereqs: ["19-06-03", "19-06-01", "19-02-04"]
tags: [numerical-modelling, hpc, domain-decomposition, load-balancing, cfl, scaling]
---

# Domain Decomposition and Load Balancing

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** the halo fraction of a band decomposition and of a block
   decomposition, and explain the difference as surface over volume.
2. **Construct** a per-cell work weight from a physical constraint — the CFL
   condition in a heterogeneous velocity field — and explain why equal
   partitioning is not equal work.
3. **Measure** the work imbalance of an equal-width partition and of a balanced
   one, and **predict** the makespan ratio before running the parallel job.
4. **Verify** that the decomposed solution does not depend on the number of
   ranks, and state what such a test does and does not cover.
5. **Measure** a serial fraction and use it to compute an Amdahl ceiling.
6. **State** when a balanced decomposition is worth the data motion it costs.

## Prerequisites

- [19-06-03 Distributed-Memory Parallelism with MPI](03-mpi-distributed.md) —
  the halo exchange whose cost this lesson shapes.
- [19-06-01 Computer Architecture, Memory Hierarchy and Roofline Thinking](01-hpc-architecture.md) —
  the local cost that the imbalance is measured against.
- [19-02-04 Explicit vs Implicit Time Stepping and Stability Limits](../02-finite-difference-methods/04-fd-time-stepping.md) —
  the CFL condition that makes the work unequal in the first place.

All numbers are **measurements on the machine that ran the demo** or **exact
arithmetic on counted quantities**, printed by
`code/domain_decomposition_demo.py`. The grid, the velocity field and the unit of
work are **SYNTHETIC** teaching values. The emulated ranks are short-lived
bounded threads inside one process; no process, MPI rank or subprocess is
started, and every pool is closed with an explicit join.

All models and data in this module are **SYNTHETIC**.

## 1. The geometry of a decomposition

Grid $512\times512$, and the question is how many cells each rank owns and how
many of them are halo:

| ranks | layout | owned per rank | halo fraction |
|---|---|---|---|
| 4 | bands | $512\times128$ | $1.56\%$ |
| 4 | $2\times2$ blocks | $256\times256$ | $1.56\%$ |
| 16 | bands | $512\times32$ | $6.25\%$ |
| 16 | $4\times4$ blocks | $128\times128$ | $3.12\%$ |
| 64 | bands | $512\times8$ | $25.00\%$ |
| 64 | $8\times8$ blocks | $64\times64$ | $6.25\%$ |

The formulas are exact: $2n/(nb) = 2/b$ for a band of height $b$, and
$4s/s^{2} = 4/s$ for a square block of side $s$. At $4$ ranks the two layouts
coincide ($512\times128$ and $256\times256$ have the same edge-to-area ratio) —
a coincidence worth noticing, because it shows the comparison is about the ratio,
not about the layout's name. At $64$ ranks the band's halo fraction is four times
the block's, and the block's grows only as $\sqrt{p}$ while the band's grows
linearly. **That is why large codes use block or brick decompositions**, and the
cost is more complex neighbour communication.

### 1.1 Geometric against graph partitioning, and what changes in 3-D

The tabulated approach is **geometric**: split a coordinate direction and read off
the halo fraction from the shape. It requires nothing but the grid indices and it
is what every structured-grid code does. The alternative is **graph
partitioning**: build the adjacency graph of cells, assign vertices to $P$ parts
minimising the cut edges subject to a balance constraint, and use a library. The
trade is:

| | geometric | graph |
|---|---|---|
| input needed | coordinates only | the full adjacency structure |
| cost | $O(N)$ arithmetic | $O(N\log N)$ or worse, plus memory for the graph |
| quality on a regular grid | optimal by construction | no better |
| quality on an irregular or adaptively refined grid | poor: a coordinate split ignores connectivity and can cut a thin, heavily connected feature | good: the cut is of the *actual* couplings |
| balance criterion | cells, or a supplied per-cell weight | any vertex weight, plus edge weights if the communication is heterogeneous |

A third option sits between them and is common in geophysics: **weighted geometric
partitioning**, where the coordinate split is kept but the cut position is chosen
from the measured/synthetic per-column costs — which is exactly what Section 3's
greedy balancer does, and what the measured $1.263 \to 1.005$ improvement in
max/mean came from.

**What changes in 3-D:** the halo fraction is a surface-to-volume ratio, so a
brick of side $s$ in a grid with $P = p_xp_yp_z$ parts has a halo fraction
$6s/s^{3} = 6/s^{2}$ — falling *quadratically* with the part size, one power
faster than in 2-D. That is why domain decomposition is more attractive in 3-D
than in 2-D, and why the surface-to-volume table in Section 1 is worth extending
to three dimensions as an arithmetic exercise before choosing a layout.

## 2. A synthetic velocity field, and why the work is unequal

Now put a physical field on the grid. Take
$v(x) = 2.0 + 0.8\sin(2\pi x)\ \mathrm{km\,s^{-1}}$, so $v$ ranges from $1.200$ to
$2.800\ \mathrm{km\,s^{-1}}$, a ratio of $2.333$.

For an explicit wave solver the time step is set by the largest velocity
($\Delta t \le h/v_{\max}$), but the *work per column* depends on how much
evolution that column experiences per unit of simulated time. Taking the local
cost as proportional to $1/v$ — the number of CFL-limited steps a column needs —
gives a cost per column between $0.3571$ and $0.8333$, again a ratio of $2.333$.

This is the whole difficulty of load balancing in a simulation: **a uniform grid
with a non-uniform medium is not uniformly expensive**, and equal-cell
partitioning is equal-*size*, not equal-*work*.

## 3. Equal width against a work-balanced split

| partition | points per rank | work per rank | max/mean |
|---|---|---|---|
| equal width | $[128,128,128,128]$ | $[51.6,\;51.52,\;88.16,\;87.99]$ | **1.263** |
| work balanced | $[157,154,95,106]$ | $[69.45,\;69.84,\;70.18,\;69.81]$ | **1.005** |

Equal width leaves the heaviest rank carrying $26.3\%$ more work than the mean;
balancing reduces that to $0.5\%$. Two observations that a naive optimisation
would miss:

- the balanced partition has **unequal cell counts** ($157$ against $95$ against
  $106$), and that is the point;
- balancing is a *different partition*, so a real code must move data or
  re-partition its mesh. It is not a free improvement, and the trade must be
  measured against the load imbalance it removes.

## 4. The measured makespan, and the prediction

Run both partitions as four emulated ranks, with the work per rank made
proportional to its weight:

| partition | work units per rank | makespan |
|---|---|---|
| equal width | $[22.2,\;22.1,\;37.9,\;37.8]$ | 17.61 ms |
| balanced | $[29.8,\;30.0,\;30.2,\;30.0]$ | 13.18 ms |
| measured ratio | — | **1.336** |
| predicted ratio | $\max/\max$ of the weights | **1.256** |

A rank finishes when **its own** work is done, so the makespan is set by the
largest rank: that single sentence is the whole theory of load imbalance, and the
table is its evidence. The measured ratio ($1.336$) exceeds the predicted one
($1.256$) because the emulation adds thread scheduling and because the balanced
run has slightly more per-rank work to start with; the gap is the honest measure
of how faithful an in-process emulation is, and it is reported rather than
smoothed away.

## 5. The answer must not depend on the number of ranks

Before any performance claim, a decomposition must pass its correctness test: the
decomposed Jacobi update must reproduce the serial one. Measured, on the same
$512^{2}$ test field, comparing against a single-rank computation:

| ranks | $\max|u_{p} - u_{\text{serial}}|$ |
|---|---|
| 1 | $0.000$ |
| 2 | $0.000$ |
| 4 | $0.000$ |
| 8 | $0.000$ |

Bitwise identical, for the same reason as
[03 §2](03-mpi-distributed.md): every rank performs the same arithmetic on the
same neighbours, so the decomposition changes the *schedule*, not the *sum*.

What this test does **not** cover, and must be tested separately:

- **reductions**, whose order changes with the rank count
  ([02 §6](02-shared-memory-parallelism.md));
- **time-dependent boundary conditions**, where a halo exchanged at the wrong
  point in the step is a genuine bug that a one-step comparison can miss;
- **a decomposition that changes the stencil**, e.g. when a halo row is computed
  rather than copied.

## 6. Amdahl's law, from a measured serial fraction

A synthetic job: one unavoidable serial reduction, plus sixteen reducible units.

| quantity | measured |
|---|---|
| serial section | 0.049 ms |
| parallel section | 0.840 ms |
| serial fraction $f$ | **0.0551** |

$$S(p) = \frac{1}{f + (1-f)/p}$$

| ranks | ideal | Amdahl ceiling | efficiency at the ceiling |
|---|---|---|---|
| 2 | 2.0 | 1.90 | 94.8% |
| 4 | 4.0 | 3.43 | 85.8% |
| 8 | 8.0 | 5.77 | 72.2% |
| 16 | 16.0 | 8.76 | 54.7% |
| 64 | 64.0 | 14.31 | 22.4% |

With $5.5\%$ of the time serial, the ceiling at $64$ ranks is $14.31\times$, not
$64\times$. Two caveats go with it: this $f$ belongs to a synthetic job on this
machine, and Amdahl's law applies to a **fixed** problem size, which is the
opposite of the weak-scaling regime in which most large simulations run. Both are
reasons to quote the *arithmetic* and not a remembered curve.

## 7. Assumptions and regime of validity

1. **A structured grid and a stencil.** Unstructured meshes need graph
   partitioning, and the counting changes; the surface-to-volume argument does
   not.
2. **A cost model, not a cost measurement.** The per-column cost is *defined* as
   proportional to $1/v$. A real solver's cost per cell depends on its arithmetic,
   its memory traffic and its boundary-condition logic; the demo's weights are a
   stand-in, stated as such.
3. **Emulated ranks.** Ranks are threads; the measured makespan includes thread
   scheduling that a real MPI run would not have, and excludes network effects
   that it would. It is a fair test of the *scheduling logic*, not of a machine.
4. **Uniform work within a rank.** A rank's items are assumed to run at the same
   rate; a rank whose work is heterogeneous internally has a second, smaller
   imbalance.
5. **One balance criterion.** Balancing by work is not balancing by memory,
   communication volume or I/O. Multi-objective partitioning exists because these
   conflict.
6. **Fixed decomposition over the run.** A decomposition chosen once can become
   unbalanced as the solution evolves; adaptive re-partitioning costs data motion
   and must be justified by the imbalance it removes.

## 8. A fully worked example

Balance four ranks on the $1/v$ weights from Section 2, by hand, for a small
version of the problem: four columns with weights $w = [0.36, 0.83, 0.83, 0.36]$
(a coarse stand-in for the field's two slow patches), total $2.38$, ideal
$0.595$ per rank.

- **Equal partition** into blocks of one column: loads $[0.36, 0.83, 0.83, 0.36]$,
  maximum $0.83$, so the makespan is $0.83$ and the efficiency is
  $0.595/0.83 = 71.7\%$.
- **Balanced partition:** group the two heavy columns with the two light ones:
  $\{0.83, 0.36\}$ and $\{0.83, 0.36\}$ give loads $[1.19, 1.19]$ for two ranks —
  perfect balance, but only two ranks are used. With four ranks the best possible
  maximum is the largest single weight, $0.83$, because an item cannot be split.
  The efficiency ceiling is therefore $71.7\%$ **for any partition**, and that is
  a fact about the item granularity, not about the partitioner.

The general rule: the achievable balance is bounded below by the largest
indivisible item, exactly as in the demo's static schedule, whose largest block
was $33$ units against an ideal of $27$ (bound ratio $1.22$). Increasing the
number of items — refining the sub-domain — is often a better lever than a
cleverer partitioner, and it is computable before the run.

## 9. Python demonstration

`code/domain_decomposition_demo.py` tabulates the halo fractions, builds the
velocity-dependent weights, compares equal-width and balanced partitions in both
counts and measured makespans, verifies the decomposition across rank counts, and
measures a serial fraction for the Amdahl table.

```bash
cd 19-numerical-modeling-hpc/06-hpc-and-parallel-computing/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python domain_decomposition_demo.py
```

## 10. Exercises

Full sets with worked solutions are in
[`exercises/05-domain-decomposition-exercises.md`](./exercises/05-domain-decomposition-exercises.md)
and [`exercises/05-domain-decomposition-solutions.md`](./exercises/05-domain-decomposition-solutions.md).

- **★** Compute the halo fraction for a $1024\times1024$ grid with $16$ bands and
  with a $4\times4$ block layout.
- **★** State the bound on the makespan of a static schedule.
- **★★** From the printed weights, verify the equal-width max/mean of $1.263$.
- **★★** With $f = 0.0551$, find the rank count at which the Amdahl efficiency
  falls below $50\%$.
- **★★★** Design a refinement of the sub-domain count that would remove the
  granularity bound of Section 8, and state what it costs.

## Mastery checkpoint

Without notes:

> A $512^{2}$ explicit solver runs on a velocity field whose cost per column
> varies by $2.333$. Four equal-width bands carry work
> $[51.6, 51.52, 88.16, 87.99]$; a balanced partition carries
> $[69.45, 69.84, 70.18, 69.81]$. **(a)** Compute the imbalance of each and the
> predicted makespan ratio. **(b)** State the measured ratio and explain the
> difference. **(c)** State the correctness test that must pass before either
> partition is believed.

A worked version appears in the lesson-05
[solutions](./exercises/05-domain-decomposition-solutions.md).

## Common pitfalls

1. **Assuming equal cells means equal work.** The measured imbalance was $26.3\%$
   before balancing, from a purely physical cause.
2. **Balancing without paying for it.** A different partition costs data motion;
   the imbalance removed must exceed the cost of moving the data.
3. **Ignoring the granularity bound.** No partitioner beats the largest
   indivisible item, and refining the sub-domains is the lever.
4. **Claiming a speedup before a correctness test.** The rank-count invariance
   check is cheap and catches most decomposition bugs.
5. **Using Amdahl for weak scaling.** The law assumes fixed problem size; large
   runs usually hold work per rank constant instead.
6. **Choosing a layout by habit.** Band and block layouts differ by a factor of
   four in halo fraction at $64$ ranks, and the block layout costs more
   neighbour logic and less communication.

## Related modules

- [03 Distributed-Memory Parallelism with MPI](03-mpi-distributed.md) — the halo
  exchange this lesson sizes.
- [04 GPU Computing: CUDA, OpenCL and Portability Layers](04-gpu-computing.md) —
  decomposition across devices rather than ranks.
- [06 Parallel I/O, Checkpointing and Job Management](06-hpc-io-and-checkpointing.md) —
  the I/O pattern a decomposition imposes.
- [19-02-04 Explicit vs Implicit Time Stepping and Stability Limits](../02-finite-difference-methods/04-fd-time-stepping.md) —
  the CFL condition that creates the imbalance.
- [19-08 Geophysical Simulation Case Studies](../08-geophysical-simulation-case-studies/README.md) —
  decompositions of real geophysical models.
