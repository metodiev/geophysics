# Module 19-06 — High-Performance and Parallel Computing

**Stages:** graduate → research · **Prerequisites:** modules 19-01 and 19-02;
basic Python and NumPy; no prior parallelism assumed.

This module is about the distance between what a computer is advertised to do and
what a kernel actually does. Every lesson starts from a **measurement** on the
machine that runs it — a bandwidth plateau, a speedup, a lost update, a digest —
and only then reasons about the architecture. The recurring result is that the
governing quantity is rarely the one on the specification: a kernel already at the
memory plateau gains nothing from threads, a tree code with $115\times$ fewer
interactions ran $6\times$ slower in Python, and removing numpy's temporaries made
a stencil $16\%$ slower.

All models and data in this module are **SYNTHETIC** teaching values. No hardware
model name, vendor figure or published benchmark is used or quoted; the
demonstrations print the logical CPU count reported by the operating system and
nothing else about the machine. Where a model needs a number the script cannot
measure — an interconnect latency, a cache-line size, a machine failure rate —
the number is printed as an **assumed model parameter** and labelled as such.
Timings are machine-dependent; every lesson says so where it quotes one.

The demonstrations obey two hard constraints, stated here because they define the
scope of what this module claims: they **start no subprocess, no MPI rank and no
long-lived thread pool** (only short-lived bounded pools closed with an explicit
join), and they **finish in seconds**. That means the parallelism they demonstrate
is numpy vectorisation and bounded thread pools, and the distributed-memory lesson
emulates ranks in one process. Where a measurement is therefore impossible —
point-to-point deadlock, the latency of a real fabric, GPU timing — the lesson
says so and states the claim as a requirement or a model rather than as a
measurement.

## Learning objectives

By the end of this module you will be able to:

1. **Measure** a machine's bandwidth plateau and **use** the roofline argument to
   decide whether a kernel is limited by bytes or by arithmetic.
2. **Decide** whether shared-memory parallelism can help a kernel, from a
   measurement rather than from a specification, and **detect** the cases where it
   hurts.
3. **Build** a domain decomposition with halo exchange, **verify** that it changes
   no bits, and **model** the communication-to-computation ratio from a measured
   local cost and stated network parameters.
4. **Express** a stencil in the form a GPU wants, **count** the memory
   transactions an access pattern implies, and select a precision per operation.
5. **Balance** work across ranks when the medium makes the cost non-uniform, and
   **bound** the makespan before running the parallel job.
6. **Design** a checkpoint that restarts exactly, survives a torn write, and has
   an interval justified by a measured write cost and a stated failure rate.
7. **Write** a reproducibility claim that is falsifiable, and a provenance record
   that contains the fields the measurements in this module show are needed.

## Prerequisites

- [19-01-01 Discretisation: Grids, Nodes, Cells and Degrees of Freedom](../01-numerical-foundations/01-discretisation-concepts.md) —
  the grids and stencils whose cost is measured here.
- [19-01-02 Truncation Error, Order of Accuracy and Convergence Rates](../01-numerical-foundations/02-convergence-and-error.md) —
  the measurement discipline this module applies to computers rather than to
  discretisations.
- [19-02-04 Explicit vs Implicit Time Stepping and Stability Limits](../02-finite-difference-methods/04-fd-time-stepping.md) —
  the CFL condition that creates load imbalance.
- [03-12 Building Numerical Simulation Code in Python](../../03-scientific-computing/12-numerical-simulation-python/README.md) —
  the vectorised solver whose inner loop these lessons measure.
- [03-13 Testing, Profiling and Packaging](../../03-scientific-computing/13-testing-profiling-packaging/README.md) —
  the profilers that produce the tables this module interprets.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Computer Architecture, Memory Hierarchy and Roofline Thinking](01-hpc-architecture.md) | graduate | Measure the plateau, then predict one kernel from another; the stencil's own rewrite was slower |
| 02 | [Shared-Memory Parallelism: OpenMP and Threading](02-shared-memory-parallelism.md) | research | Three kernels, three speedups: $0.93\times$, $0.30\times$, $3.75\times$ — measure before you parallelise |
| 03 | [Distributed-Memory Parallelism with MPI](03-mpi-distributed.md) | research | Halo exchange changes no bits; the reduction order does; the scaling curve is arithmetic on an assumed fabric |
| 04 | [GPU Computing: CUDA, OpenCL and Portability Layers](04-gpu-computing.md) | research | SIMT in numpy, sector counts as arithmetic, launch-overhead crossover, precision per operation |
| 05 | [Domain Decomposition and Load Balancing](05-domain-decomposition.md) | research | A non-uniform medium makes equal cells unequal work; balance it, and pay for it |
| 06 | [Parallel I/O, Checkpointing and Job Management](06-hpc-io-and-checkpointing.md) | research | Exact restarts, torn writes, and an interval that depends on an assumed failure rate |
| 07 | [Reproducibility and Provenance in HPC Workflows](07-reproducible-hpc.md) | research | The decomposition decides the bits; a claim must name it or it is untestable |

## Suggested path

**If you are new to performance work:** lessons 01, 02 and 05 in order, running
each demo. Lesson 01 establishes the measurement habit; lesson 02 shows what it
costs to skip it.

**If you already run parallel codes:** start at 03 §2 (bitwise identity) and 03 §5
(collectives), then 05 §3–4 (imbalance) and 07 (claims), which are where
production runs usually break.

**If you are preparing a research project:** run the four measurement demos
(01, 02, 04, 05) on your own hardware and the transfer to a cluster, then read
06 and 07 before you write a single checkpoint.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-hpc-architecture.md`](01-hpc-architecture.md) | Lesson 01 |
| [`02-shared-memory-parallelism.md`](02-shared-memory-parallelism.md) | Lesson 02 |
| [`03-mpi-distributed.md`](03-mpi-distributed.md) | Lesson 03 |
| [`04-gpu-computing.md`](04-gpu-computing.md) | Lesson 04 |
| [`05-domain-decomposition.md`](05-domain-decomposition.md) | Lesson 05 |
| [`06-hpc-io-and-checkpointing.md`](06-hpc-io-and-checkpointing.md) | Lesson 06 |
| [`07-reproducible-hpc.md`](07-reproducible-hpc.md) | Lesson 07 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Seven runnable demonstrations |

## How to run the demos

Use the project virtual environment, which provides NumPy and SciPy:

```bash
cd 19-numerical-modeling-hpc/06-hpc-and-parallel-computing/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python hpc_architecture_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python shared_memory_parallelism_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python mpi_distributed_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gpu_computing_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python domain_decomposition_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python hpc_io_and_checkpointing_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python reproducible_hpc_demo.py
```

Every demo prints labelled results, exits 0, and finishes in a few seconds. They
use the fixed seed `np.random.default_rng(20261014)`, need no network, spawn no
process and no MPI rank, and start only bounded thread pools that are joined
before the next section. Timings vary between runs and between machines; the
lessons quote the values measured when they were written and say so.

Two demos write small files: `hpc_io_and_checkpointing_demo.py` writes its
checkpoints into `code/` and deletes them as it finishes, and
`reproducible_hpc_demo.py` does the same with its serialisation test files.
Neither leaves anything behind.

## Mastery checkpoint

Complete this without notes:

> A streaming kernel reaches $92.5$ GB/s on one thread; four threads on the same
> kernel reach $28.0$ GB/s. A sort of four arrays takes $131.1$ ms serially and
> $35.0$ ms on four threads. **(a)** Explain the two directions of the result in
> one sentence each. **(b)** A decomposed Jacobi sweep matches the serial sweep to
> $0.000$ at $p = 1,2,4,8$, while a chunked reduction gives four different
> digests across six chunk counts. State what each observation says about
> parallel correctness. **(c)** State which quantity must be recorded for a
> reproducibility claim, and why a hash of the manifest answers a different
> question from a hash of the result.

A worked version appears in the lesson-02 and lesson-03
[solutions](exercises/03-mpi-distributed-solutions.md).

## Common pitfalls across this module

1. **Parallelising before measuring the plateau.** If one thread is at the
   bandwidth limit, more threads move less data per unit time — measured here as
   $0.303\times$.
2. **Reading a speedup from an operation count.** The tree code had $115\times$
   fewer interactions and ran $6\times$ slower.
3. **Assuming "fewer temporaries" means "faster".** It was $16\%$ slower, and the
   reason is measured.
4. **Quoting a scaling curve without its assumed parameters.** Every
   interconnect number in lesson 03 is a model input, labelled.
5. **Balancing cells instead of work.** A $26.3\%$ imbalance came from a purely
   physical cause.
6. **Claiming reproducibility without naming the decomposition.** Four digests
   across six chunk counts, measured.
7. **Trusting a checkpoint that has never been restarted.** The test is bitwise
   equality with an uninterrupted run, and it is cheap.

## Related modules

- [19-01 Numerical Foundations for Simulation](../01-numerical-foundations/README.md) —
  discretisation and stability, the numerical content this module accelerates.
- [19-05 Integral Equation and Boundary Methods](../05-integral-equation-and-boundary-methods/README.md) —
  the dense operators that make acceleration and parallelism mandatory.
- [19-07 Verification, Validation and Numerical Uncertainty](../07-verification-validation-uncertainty/README.md) —
  what a fast answer is entitled to claim.
- [19-08 Geophysical Simulation Case Studies](../08-geophysical-simulation-case-studies/README.md) —
  these techniques inside complete simulations.
- [22-data-engineering-reproducibility](../../22-data-engineering-reproducibility/README.md) —
  provenance and reproducible workflows as a discipline.
