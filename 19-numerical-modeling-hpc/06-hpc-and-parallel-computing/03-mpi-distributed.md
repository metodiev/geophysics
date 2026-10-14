---
id: 19-06-03
title: "Distributed-Memory Parallelism with MPI"
level: research
prereqs: ["19-06-02", "19-06-01", "19-05-01"]
tags: [numerical-modelling, hpc, mpi, distributed-memory, halo-exchange, scaling, collectives]
---

# Distributed-Memory Parallelism with MPI

## Learning objectives

By the end of this lesson you will be able to:

1. **Decompose** a 2-D grid into rank-local strips with halo rows and **verify**
   that the decomposed result is bitwise identical to the serial one.
2. **Count** the messages and bytes a halo exchange moves per sweep, and from the
   count **compute** the communication-to-computation ratio.
3. **Predict** strong-scaling efficiency from a measured local sweep time and two
   stated network parameters, and identify where the model breaks down.
4. **Explain** why the surface-to-volume ratio makes a strip decomposition degrade
   with rank count, and what changes that.
5. **Compare** a pairwise-tree collective with a linear gather: step counts, and
   the fact that the two do not produce the same bits.
6. **State** the deadlock condition of blocking point-to-point communication and
   the ordering rule that avoids it.

## Prerequisites

- [19-06-02 Shared-Memory Parallelism: OpenMP and Threading](02-shared-memory-parallelism.md) —
  the reduction-order question, which becomes sharper across ranks.
- [19-06-01 Computer Architecture, Memory Hierarchy and Roofline Thinking](01-hpc-architecture.md) —
  the measured local cost the communication will be compared with.
- [19-05-01 Volume and Surface Integral Equations](../05-integral-equation-and-boundary-methods/01-integral-equations.md) —
  a workload whose parallel form is a sum over sources rather than a stencil.

All numbers are **measurements of local memory operations** on the machine that
ran the demo, printed by `code/mpi_distributed_demo.py`. The grid, the initial
condition and the interconnect parameters are **SYNTHETIC** teaching values: the
latency and bandwidth used by the scaling model are **assumed model parameters,
stated in the output**, and are not measurements of any real fabric.

All models and data in this module are **SYNTHETIC**.

**What the demonstration does not do:** it does not start MPI, does not call
`mpiexec`, does not spawn a process and does not open a socket. Every "rank" is
an array in one process and every "message" is an array copy. That makes the
decomposition, the halo exchange and the *counting* visible; it makes the
timings local memory measurements, and the lesson says so wherever a number
appears.

## 1. The decomposition, and the halo

Take a $512^{2}$ grid and $p$ ranks, and give each rank a contiguous band of
interior rows. A rank needs its neighbours' rows to update its own boundary rows,
so each band carries **one halo row above and one below**:

| quantity | value |
|---|---|
| grid | $512\times512$, $260\,100$ interior points |
| band for $p = 8$ | $64$ interior rows + $2$ halo rows |
| halo cells per rank | $2 \times 512 = 1024$ doubles |
| halo fraction ($p = 8$) | $2.99\%$ of the owned block |

The halo fraction is a surface-to-volume ratio: for a band of height $b$ and
width $n$ it is exactly $2/b$, and for a square block of side $s$ it is $4/s$.
Section 5 of [05 Domain Decomposition and Load Balancing](05-domain-decomposition.md)
tabulates both.

## 2. Correctness first: the decomposition must not change the answer

Run $20$ Jacobi sweeps serially, then run the same $20$ sweeps as $p$ rank-local
bands with halo rows exchanged as array copies before every sweep, and compare:

| $p$ | $\max|u_{\text{parallel}} - u_{\text{serial}}|$ |
|---|---|
| 1 | **0.000** |
| 2 | **0.000** |
| 4 | **0.000** |
| 8 | **0.000** |

Zero, not "small". Each interior point is computed from the same four neighbours
with the same operations in the same order, because the halo rows *are* those
neighbours. A correct halo exchange changes no bits at all — and this is the
strongest and cheapest test of a decomposition, because it needs no reference
solution other than the one the code already computes serially.

Note what this test does **not** cover: it does not test a reduction, where the
order genuinely changes (Section 4), and it does not test a time-dependent
boundary condition, where a halo updated at the wrong time is a real bug and
still passes a one-sweep comparison. Run it at more than one sweep count.

## 3. Counting messages, bytes and the ratio

For $p$ bands, every sweep exchanges one row with each neighbour: $2(p-1)$
messages of $512$ doubles ($4096$ bytes) each.

| $p$ | messages/sweep | bytes/rank/sweep | bytes/sweep, all ranks | comm/compute |
|---|---|---|---|---|
| 1 | 0 | 0 | 0 | 0.0000 |
| 2 | 2 | 8192 | 16384 | 0.0253 |
| 4 | 6 | 8192 | 32768 | 0.0723 |
| 8 | 14 | 8192 | 65536 | 0.1662 |
| 16 | 30 | 8192 | 131072 | 0.3542 |

with the local sweep measured at $0.461$ ms ($260\,100$ interior points,
$1.771$ ns per point), and the **assumed** parameters
$\alpha = 5.0\ \mu\mathrm{s}$ latency per message and
$\beta = 10.0\ \text{GB/s}$ link bandwidth. The ratio in the last column is

$$\frac{t_{\text{comm}}}{t_{\text{compute}}}
= \frac{2(p-1)\alpha + 2(p-1)\cdot 4096/\beta}{0.461\ \text{ms}} .$$

The point of the column is its *scaling*: computation per rank falls as $1/p$
while the number of messages grows as $p$, so the ratio grows roughly as $p^{2}$
for a fixed global grid. That is the surface-to-volume argument expressed in
units of time.

### 3.1 How the ratio scales with $p$

The algebra is worth doing once, because it predicts the whole table. Write the
band height as $b = n/p$ for an $n\times n$ grid, so computation per rank per
sweep is $c\,n\,b = c\,n^{2}/p$ for a per-point constant $c$, and communication per
rank per sweep is $\alpha + \beta^{-1}\,n\,w$ for $w$ bytes per element. Then

$$\frac{t_{\text{comm}}}{t_{\text{compute}}}
= \frac{p\left(\alpha + nw/\beta\right)}{c\,n^{2}},$$

so with $\alpha$ dominant the ratio grows **linearly** in $p$ for a fixed global
grid (the lesson's table grows from $0.0253$ at $p = 2$ to $0.1662$ at $p = 8$,
i.e. by a factor $6.6$ for a factor $4$ in $p$ — super-linear because the message
count grows as $p$ while each message's size is fixed).

Two consequences that are visible in the table and in the algebra:

- **strong scaling is limited by geometry**, and no amount of code tuning removes
  the $p$-dependence;
- **weak scaling holds $b$ fixed**, so $n$ grows with $p$, the computation per
  rank is constant and the ratio stays constant. The same solver therefore has
  flat efficiency in one experiment and falling efficiency in the other, which is
  why a scaling figure without its regime is uninterpretable.

## 4. A modelled scaling curve, with its assumptions on the table

Using the measured sweep time and $\alpha = 5\ \mu\mathrm{s}$,
$\beta = 10$ GB/s:

| $p$ | ideal speedup | modelled speedup | efficiency | bytes/message |
|---|---|---|---|---|
| 1 | 1.0 | 1.00 | 100.0% | 4096 |
| 2 | 2.0 | 1.91 | 95.5% | 4096 |
| 4 | 4.0 | 3.66 | 91.4% | 4096 |
| 8 | 8.0 | 6.73 | 84.2% | 4096 |
| 16 | 16.0 | 11.63 | 72.7% | 4096 |
| 32 | 32.0 | 18.27 | 57.1% | 4096 |

Two things must be said about this table, in this order: it is **arithmetic**,
and its two inputs are one measurement and one assumption. The arithmetic is
$t(p) = t_{\text{sweep}}(1/p + c)$ with $c$ the comm/compute ratio, so the
efficiency falls because $c$ grows; the model has no other content. Changing
$\alpha$ to $1\ \mu\mathrm{s}$ or $\beta$ to $40$ GB/s moves every number, and a
reader who wants the real curve must measure the real fabric. The transferable
conclusion is the *shape* — efficiency falling with $p$ for fixed problem size —
and the reason: surfaces grow, volumes do not.

## 5. Collectives: the tree against the gather, and the bits

A reduction over $16$ rank-local values, done two ways:

| method | steps | value | same bits as numpy's pairwise sum |
|---|---|---|---|
| pairwise tree | 4 | $-1.6100468382312125$ | yes |
| linear gather | 15 | $-1.6100468382312128$ | no |

The tree needs $\log_2 p$ steps against $p-1$ for the gather, and the difference
in the results is $2.22\times10^{-16}$ — the last bit. An `Allreduce` therefore
has a defined value only once its **reduction order** is defined: "the sum" is
not a specification. The message from
[02 §6](02-shared-memory-parallelism.md) is the same one, in a place where it is
much harder to hide, because the order is determined by the communicator shape.

This is why production codes state the reduction order in their provenance record
([07 Reproducibility and Provenance](07-reproducible-hpc.md)) and why a
reproducibility claim that says "same result" without saying "same decomposition
and same reduction tree" is unfalsifiable.

## 6. Point-to-point ordering and deadlock

Point-to-point blocking communication has a failure mode that cannot be
demonstrated in an in-process emulation, so it is stated rather than measured:

- If two ranks each execute a **blocking send** and then a receive, and the send
  cannot complete until the matching receive is posted, both wait forever. That
  is **deadlock**, and it is not a performance problem; the job hangs.
- The standard remedies: order the communication so that sends and receives
  cannot cyclically wait (respect a rank ordering), use non-blocking
  `Isend`/`Irecv` pairs (which never block on the memory system the way a
  blocking send can), or use a collective the library has already ordered
  correctly.
- A related and subtler mode is **convoying**: messages that consume all buffers
  and serialize internally without hanging.

Because the demonstration deliberately does not start MPI, none of this is
demonstrated by it. It is listed here because a lesson that taught only the halo
pattern would leave the most common way a distributed code fails unmentioned.

### 6.1 Overlapping communication with computation

The scaling model above charges every sweep the full communication time. A real
code can hide part of it:

- **non-blocking exchange.** Post receives and sends for the halos, compute the
  interior before the exchange completes, then consume the halos. The
  communication cost then does not add to the compute time but *overlaps* it, so
  the model becomes
  $t \approx \max(t_{\text{compute}}, t_{\text{comm}}) + t_{\text{unhidden}}$,
  where the unhidden part is the halo consumption which cannot start until the
  message arrives. With $t_{\text{comm}}/t_{\text{compute}} = 0.187$ at $p = 8$,
  perfect overlap would reduce the modelled time from $1.187$ units to about
  $1.0$ plus the halo-consumption fraction, which for one row of $512$ doubles is
  a few microseconds against a $57.8\ \mu\mathrm{s}$ local sweep.
- **the limiting case.** Overlap cannot help when the communication is *already*
  the larger term: at $p \approx 44$ the model gives a ratio of one, and there the
  maximum is the communication time and the efficiency ceiling is set by geometry,
  not by cleverness.

Both statements are arithmetic on the same assumed parameters, and neither is a
measurement. What a reader should take is the structure: overlap converts an
addition into a maximum, and it is worth doing exactly in the regime where the two
terms are comparable.

## 7. Assumptions and regime of validity

1. **Local memory, emulated ranks.** All timings are array copies within one
   process. They measure the *work* of a halo exchange and its relative size,
   not its latency on a real fabric.
2. **Assumed network parameters.** $\alpha = 5\ \mu\mathrm{s}$ and
   $\beta = 10$ GB/s are model inputs. Every table that uses them is arithmetic,
   and the demo prints them next to the columns they produce.
3. **Structured grids, synchronous sweeps.** The model applies to a sweep loop
   with regular communication. Irregular or asynchronous communication,
   overlapping computation and communication, and topology-aware placement each
   require their own measurement.
4. **Fixed problem size.** The table is *strong* scaling. Weak scaling — grow the
   problem with $p$ so that work per rank is constant — keeps the comm/compute
   ratio constant and is the regime where large simulations normally run; the
   model above does not describe it.
5. **One message per boundary.** A real code may exchange a whole slab, combine
   messages, or use `MPI_Neighbor_alltoall`; the count changes and the arithmetic
   must be redone, not extrapolated.
6. **Bitwise identity is not free of preconditions.** It held because the
   arithmetic per point was identical and no reduction was involved. Add a
   reduction, or let a compiler reassociate a loop, and the claim must be
   re-derived and re-measured.

## 8. A fully worked example

Take $p = 8$ bands on the $512^{2}$ grid and work out the model by hand.

- **Computation per rank:** $64 \times 510 \approx 32\,640$ points
  ($64$ interior rows, $510$ interior columns). At the measured $1.771$ ns per
  point in the serial sweep, one local sweep costs
  $32\,640 \times 1.771\ \mathrm{ns} = 57.8\ \mu\mathrm{s}$. (The demo quotes the
  full-grid serial sweep, $0.461$ ms, and divides; using the per-rank figure here
  makes the comparison with communication direct.)
- **Communication per rank per sweep:** $2$ messages of $4096$ bytes, so latency
  cost $2 \times 5\ \mu\mathrm{s} = 10\ \mu\mathrm{s}$ and transfer cost
  $8192 / 10^{10} = 0.82\ \mu\mathrm{s}$; total $\approx 10.8\ \mu\mathrm{s}$.
- **Ratio:** $10.8/57.8 = 0.187$, so a sweep that would take $1$ unit of time
  takes $1.187$ units. At $p = 8$ the ideal speedup is $8$, the modelled speedup
  is $8/1.187 = 6.74$ — matching the table's $6.73$ to two figures.

Now change one assumption and see what the model is worth: if the fabric is
$40$ GB/s instead of $10$ GB/s, the transfer term becomes
$0.21\ \mu\mathrm{s}$ and the total $10.2\ \mu\mathrm{s}$: a $5\%$ change, because
**latency dominates at this message size**. The model's sensitivity to each input
is the useful output, and it says: at $4$ KB per message, buy latency, not
bandwidth. That conclusion is a property of the arithmetic and of the assumed
parameters, and it is exactly the kind of statement that must not be quoted as a
hardware fact.

## 9. Python demonstration

`code/mpi_distributed_demo.py` runs the serial sweep, the decomposition with
bitwise comparison, the message counts and the ratio, the modelled scaling
curve, and the two collectives with their digests.

```bash
cd 19-numerical-modeling-hpc/06-hpc-and-parallel-computing/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python mpi_distributed_demo.py
```

## 10. Exercises

Full sets with worked solutions are in
[`exercises/03-mpi-distributed-exercises.md`](./exercises/03-mpi-distributed-exercises.md)
and [`exercises/03-mpi-distributed-solutions.md`](./exercises/03-mpi-distributed-solutions.md).

- **★** Compute the halo fraction for $p = 16$ bands on the $512^{2}$ grid.
- **★** State why the parallel and serial Jacobi results are bitwise identical.
- **★★** Reproduce the comm/compute ratio at $p = 4$ from the stated parameters
  and the measured sweep time.
- **★★** Find the $p$ at which the modelled comm/compute ratio reaches $1.0$ and
  comment on whether the model is still valid there.
- **★★★** Design a weak-scaling experiment for the same solver, state what should
  stay constant, and predict its efficiency curve from the same parameters.

## Mastery checkpoint

Without notes:

> A $512^{2}$ code runs at $0.461$ ms per serial sweep. With $p = 8$ bands it
> exchanges $14$ messages of $4096$ bytes per sweep, and the model uses
> $\alpha = 5\ \mu\mathrm{s}$, $\beta = 10$ GB/s. **(a)** Compute the
> comm/compute ratio and the modelled efficiency. **(b)** State which of the two
> network parameters dominates at this message size and how you know.
> **(c)** The decomposed and serial results differ by $0.0$; state why, and state
> one change to the experiment that would make them differ by a few ulp.

A worked version appears in the lesson-03
[solutions](./exercises/03-mpi-distributed-solutions.md).

## Common pitfalls

1. **Quoting a scaling curve as a property of MPI.** The curve above is
   arithmetic on an assumed fabric; the only measured input is the local sweep.
2. **Assuming the halo exchange is free because it copies little.** At $4$ KB per
   message the latency term dominates the transfer term by more than $10\times$.
3. **Forgetting that computation per rank falls as $1/p$ while messages grow as
   $p$.** Strong scaling degrades for a reason that is computable in advance.
4. **Believing a decomposition is verified because one sweep agrees.** Run the
   comparison over many sweeps and with time-varying boundaries.
5. **Leaving the reduction order unspecified.** The tree and the gather differ in
   the last bit, and both are "the sum".
6. **Ignoring deadlock until it hangs.** Blocking sends on both sides of a cyclic
   wait are the commonest way a distributed code fails, and the fix is an
   ordering rule or non-blocking communication.

## Related modules

- [02 Shared-Memory Parallelism: OpenMP and Threading](02-shared-memory-parallelism.md) —
  the same arithmetic inside one address space.
- [05 Domain Decomposition and Load Balancing](05-domain-decomposition.md) —
  the decomposition choice and its measured effect on makespan.
- [06 Parallel I/O, Checkpointing and Job Management](06-hpc-io-and-checkpointing.md) —
  what happens when the parallel job must write its state.
- [19-01-03 Consistency, Stability and the Lax Equivalence Theorem](../01-numerical-foundations/03-consistency-stability.md) —
  the numerical setting in which these sweeps run.
- [18-inverse-problems](../../18-inverse-problems/README.md) — a distributed
  forward solver as the inner loop of an inversion.
