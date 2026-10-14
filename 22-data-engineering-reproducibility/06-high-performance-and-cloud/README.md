# Module 22-06 — High-Performance and Cloud Computing for Research

**Stages:** research · **Prerequisites:** module 22-02 (containers and workflow managers)
and module 22-04 (partitioning and out-of-core patterns), or equivalent experience
requesting jobs on a shared machine and costing a dataset.

This module is about the two places geophysical computation actually runs, and about the
one quantity that decides between them: **the deadline, priced**. A cluster gives you
capacity in exchange for a queue position; the cloud gives you capacity in exchange for a
bill. Both are governed by the same arithmetic — Amdahl's law sets the ceiling, the
request shape sets the wait, and the serial fraction sets the floor below which no amount
of capacity reaches the deadline.

The first thread is that **a request is a prediction**. You state nodes, cores, memory and
wall time, and the scheduler decides when you get them and whether you get all of them. The
module's SYNTHETIC job mix has a median request of two nodes and a mean of three — with a
maximum of seventy — and the wait grows with the request size from 0.54 h to 8.08 h, so an
overstated request is paid for in queue time. The same logic appears on the cloud as
efficiency: 1 024 workers reach 19.64× against an asymptote of 20×, at 1.9 % efficiency.

The second thread is that **the cost model has three terms and only one of them is
compute**. A 12-hour 64-core run producing two terabytes costs 698.4 units in the
module's teaching rates, of which 38.4 is compute; storage and egress are 95 % of it. In a
project-level view, 65 % of the bill can be storage, movement and recomputation, none of
which a faster solver touches. Those numbers are the reason a costing lesson belongs in a
computing module.

The third thread is that **reliability is designed, not hoped for**. A fleet of 64
instances running for two hours is interrupted with probability 0.864; at 256 instances it
is 0.999. The response is not a bigger fleet but a checkpoint interval chosen against the
work a restart would lose, a completion manifest, and data placed where the compute is.

All measurements in this module are **SYNTHETIC**: job shapes, wait-times, speedups,
interruption rates, capacities and prices are chosen teaching values in arbitrary units.
No cluster, cloud service or provider price list was used or quoted, and no benchmark of a
real system is reported.

## Learning objectives

By the end of this module you will be able to:

1. Describe a job request (nodes, cores, memory, wall time) and predict its effect on the
   queue wait and on the job's chance of completing within the request.
2. Compute strong-scaling speedup and efficiency from a serial fraction, state the
   asymptote, and choose a worker count from a wall-time requirement.
3. Choose a checkpoint interval from an interruption rate, and compute the probability that
   a fleet loses at least one instance.
4. Build a three-term cost model — compute, storage, movement — and compute the break-even
   core count for a deadline against the serial floor.
5. Compute the cost per unit of work under weak scaling, and state why it rises as the
   problem grows.
6. Diagnose the recurring failures: an over-sized request, a serial stage that owns the
   wall time, a checkpoint interval longer than the interruption interval, a fleet whose
   bill is dominated by egress, and a forecast with no failure line.

## Prerequisites

- [22-06-01 Running Jobs on HPC Clusters and Schedulers](01-cluster-jobs.md) is the entry
  point; the cloud and cost lessons assume its request arithmetic.
- [22-02-06 Containers for Computational Reproducibility](../02-reproducible-workflows/06-containers-reproducibility.md) —
  the artefact that makes an instance reproducible.
- [22-04-04 Big-Data Patterns: Partitioning, Chunking, Out-of-Core](../04-databases-and-large-data/04-big-data-patterns.md) —
  the partitioning decisions that a distributed job inherits.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Running Jobs on HPC Clusters and Schedulers](01-cluster-jobs.md) | research | The job mix's median is 2 nodes and its maximum 70; the wait ranges 0.54 → 8.08 h with request size, and utilization is 91.9 % of node-hours |
| 02 | [Cloud Computing for Geophysical Computation](02-cloud-computing-research.md) | research | Amdahl at $p = 0.05$ gives 3.48/9.14/15.42 at 4/16/64 workers against a 20× ceiling; 64 intermittent instances are interrupted with probability 0.864 |
| 03 | [Cost, Scaling and Practical Efficiency](03-cost-and-scaling.md) | research | 38.4 + 480 + 180 = 698.4 units, 95 % of it storage and egress; the same work costs 19.5 % more at 32 768 cores, and the serial floor forbids a 0.5 h deadline |

## Suggested path

**If you run jobs on a shared cluster:** read 01 in full, then 03 §1–4 to price the
request you just learned to make.

**If you are moving work to the cloud:** read 02, then 03 §3–5 for the compression and
aggregate decisions that keep the bill from being an egress bill, and
[22-04-05 Cloud-Native Geoscience Data Access](../04-databases-and-large-data/05-cloud-native-geoscience.md)
for the layouts.

**If you are writing a grant or an allocation request:** read 03 in full; §5's five-line
forecast and the failure line are the parts that reviewers check.

**If you are here for the measurements:** every demo is self-contained, prints labelled
units, and runs in under a second; the ★★★ exercises ask you to design measurements on
systems you choose.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-cluster-jobs.md`](01-cluster-jobs.md) | Lesson 01 |
| [`02-cloud-computing-research.md`](02-cloud-computing-research.md) | Lesson 02 |
| [`03-cost-and-scaling.md`](03-cost-and-scaling.md) | Lesson 03 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Three runnable demonstrations |

| Script | What it measures |
|---|---|
| [`code/cluster_jobs_demo.py`](code/cluster_jobs_demo.py) | Job mix and core-hours, wait against request shape, the effect of wall-time limits, utilization |
| [`code/cloud_computing_research_demo.py`](code/cloud_computing_research_demo.py) | Amdahl table and asymptote, wall time and instance-hours, checkpoint intervals, fleet interruption probabilities |
| [`code/cost_and_scaling_demo.py`](code/cost_and_scaling_demo.py) | The three cost terms, weak-scaling cost per unit of work, the deadline break-even table, the annual cost shares |

## How to run the demos

```bash
cd 22-data-engineering-reproducibility/06-high-performance-and-cloud/code

/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python cluster_jobs_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python cloud_computing_research_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python cost_and_scaling_demo.py
```

Every demo prints labelled results with units, seeds its random numbers with
`np.random.default_rng(20261014)`, uses no network access, writes no files and exits 0.
Each runs in well under a second.

## Mastery checkpoint

Complete this without notes, using the demonstrations only to check arithmetic:

> A group has a modelling code whose serial fraction is 5 %, a 12-hour run at 64 cores, and
> a two-terabyte output they intend to keep for a year. Teaching rates: 0.05 per core-hour,
> 20 per TB-month, 90 per TB egress.
> **(a)** Compute the speedup and efficiency at 256 cores and the asymptote of the code.
> **(b)** Compute the wall time at 256 cores and the instance-hours consumed.
> **(c)** Compute the three cost terms and the total, and state the dominant one.
> **(d)** The run must finish in 3 hours; state the core count, the cost, and why a 0.5-hour
> deadline is out of reach. **(e)** They use interruptible instances at 0.02 interruptions
> per instance-hour; compute the interruption probability for a 2-hour run and choose a
> checkpoint interval, stating the trade. **(f)** State the one line of a grant forecast
> that a faster solver does not reduce, and the measurement that would set it.

Worked versions of (a)–(f) appear in the lesson solutions at ★★ and ★★★ level.

## Common pitfalls across this module

1. **Requesting more than you need.** The queue wait grows with the request; the median
   request in the demonstration's mix is 2 nodes and the wait at the largest shape is
   fifteen times the smallest.
2. **Buying workers to fix a serial fraction.** Efficiency at 1 024 workers is 1.9 %.
3. **Assuming weak scaling is free.** The same work costs 19.5 % more at 32 768 cores than
   at 64, with a wall time that moved by only 20 %.
4. **Checkpointing less often than interruptions occur.** At fleet scale some instance is
   always interrupted; the interval is chosen, not inherited.
5. **Forecasting compute only.** In the demonstration's project decomposition, 65 % of the
   bill sits outside compute.
6. **Quoting a price without a date and a region.** Provider prices change; a cost table
   without them is not evidence.
7. **Letting ephemeral instances hold the only copy.** Durable storage for outputs and
   checkpoints, always.

## Related modules

- [22-02 Reproducible Computational Workflows](../02-reproducible-workflows/README.md) —
  the environments and workflows that the jobs here execute.
- [22-03 Data Formats and Engineering](../03-data-formats-and-engineering/README.md) —
  the layouts that decide how much data has to move.
- [22-04 Databases and Large Data Collections](../04-databases-and-large-data/README.md) —
  the partitioning and out-of-core patterns a distributed job inherits.
- [19-06 HPC and Parallel Computing](../../19-numerical-modeling-hpc/06-hpc-and-parallel-computing/README.md) —
  the algorithms behind the serial fraction.
