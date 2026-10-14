---
id: 22-06-01
title: "Running Jobs on HPC Clusters and Schedulers"
level: research
prereqs: ["22-06-03", "22-04-04"]
estimated_minutes: 50
tags: [hpc, schedulers, clusters, job-requests, efficiency]
---

# Running Jobs on HPC Clusters and Schedulers

## Learning objectives

By the end of this lesson you will be able to:

1. **Describe** a cluster as a partition of nodes with a scheduler and a queue, and
   **state** the quantities a job request declares.
2. **Explain** why queueing delay rises with the *product* of requested nodes and
   hours, and **compute** the waiting for a stated job shape.
3. **Compute** the utilization a job mix implies, and **distinguish** a busy cluster
   from a productive one.
4. **Choose** a walltime and node count from the job's structure, and **state** the
   node-hours each choice wastes.
5. **Design** a job script and a job sequence that survive the two real failure modes:
   a killed job and a limit that expires mid-run.
6. **Diagnose** an allocation that is being wasted, from the scheduler's own data.

Job sizes, arrival rates, node counts and limits in this lesson are **SYNTHETIC** with
chosen parameters. No cluster was used, no scheduler's policy is described, and no
system's performance is quoted; the queueing structure and the request arithmetic are
the transferable content.

## Prerequisites

- [22-06-03 Cost, Scaling and Practical Efficiency](./03-cost-and-scaling.md) — the
  scaling laws a job's request should reflect.
- [22-04-04 Big-Data Patterns: Partitioning, Chunking, Out-of-Core](../04-databases-and-large-data/04-big-data-patterns.md) —
  the partitioning that decides how many jobs a problem needs.

## 1. Intuition: you do not buy compute, you request it

A cluster is a shared machine whose scarce resource is the scheduler's attention and
the nodes' time. A job request declares four things — **nodes** (or cores), **walltime**,
**memory**, and **queue or partition** — and the scheduler decides when to start it.
The consequences that surprise newcomers follow directly:

- the request is a **claim on the machine for its whole duration**, so an over-stated
  walltime idles nodes;
- the **wait** depends on how much of the machine the request blocks, not on how long
  the job runs;
- the scheduler starts jobs out of order when it can (backfilling short jobs into gaps),
  which rewards **accurate** requests and punishes guesswork.

## 2. The job mix

The demonstration's **SYNTHETIC** partition has 256 nodes of 32 cores and receives 4 000
jobs at 400 per day with a median requested walltime of 3 hours:

| Quantity | Value |
|---|---|
| median nodes requested | 2 |
| mean nodes requested | 3.0 |
| maximum nodes requested | 70 |
| total core-hours requested | 1 806 755 |

The distribution is the familiar lognormal: a small median, a long tail of large jobs,
and a total dominated by the tail. The scheduler's behaviour is set by that tail, not
by the median job, which is why one group's 70-node job affects everyone's waiting.

## 3. Waiting, and the product rule

A job's obstruction is proportional to the fraction of the machine it claims:

$$\text{obstruction} \approx \frac{\text{nodes} \times \text{hours}}
{\text{nodes}_{\text{total}} \times 24\ \text{h}} .$$

The demonstration models the wait as an increasing function of that fraction:

| Job shape | nodes × hours | Request fraction | Modelled wait (h) |
|---|---|---|---|
| 1 node, 1 h | 1 | 0.000 | 0.54 |
| 1 node, 24 h | 24 | 0.004 | 0.97 |
| 64 nodes, 1 h | 64 | 0.010 | 1.54 |
| 16 nodes, 8 h | 128 | 0.021 | 2.31 |
| 64 nodes, 12 h | 768 | 0.125 | 8.08 |

The numbers are model outputs; the structure is the point. Two jobs with the same
node-hours (24: "1 node for 24 h" and "24 nodes for 1 h") queue differently, because
what the scheduler needs is a *gap* shaped like the request. A long narrow job needs a
single node idle for a day; a short wide job needs a coordinated block of nodes for an
hour. Most clusters satisfy the second far more often, which is why **splitting a long
job into shorter ones**, when the algorithm allows it, reduces waiting.

The second quantity is the **walltime limit**: a limit removes the longest jobs from the
queue, and the demonstration's mix shows what it removes — 3 440 of 4 000 jobs exceed a
1-hour limit (55 293 node-hours), 307 exceed 12 hours (17 189 node-hours), and none
exceeds 48 hours. A limit is a policy that trades the queue's tail against the
feasibility of long jobs.

## 4. Utilization, and what it does not mean

Over the span the jobs span, the partition offers

$$256\ \text{nodes} \times 24\ \text{h} \times \frac{4000}{400}\ \text{days}
= 61\,440\ \text{node-hours},$$

against 56 461 node-hours requested — a **requested utilization of 91.9 %**, leaving
8.1 % available. Two caveats: the figure is *requested*, not *used* (a job that finishes
early releases its claim, and a job that idles inside its allocation still holds it);
and high utilization is not the goal — a cluster can be 92 % busy running jobs that
produce nothing useful. The measurements that matter are the ones attached to work:
completed analyses per node-hour, and the fraction of node-hours spent on jobs that
were later re-run because of a mistake.

## 5. Choosing the request

1. **Measure the job on a small case first**, then estimate. Requests based on hope are
   the source of both lost work and idle nodes.
2. **Set the walltime from the measurement plus a margin** (10–20 %), not from the
   limit. The two failure modes are opposite: too high wastes the allocation, too low
   kills the job.
3. **Request cores, not whole nodes**, unless the code uses the node's memory or its
   interconnect; a single-threaded job occupying 32 cores is the most expensive request
   in the list.
4. **Split long jobs** into restartable pieces where the algorithm allows, so a limit
   or a failure costs one piece.
5. **Use the array or workflow mechanism** for parameter sweeps, so the scheduler sees
   many small jobs and can backfill them.
6. **Checkpoint**, and write output as the job proceeds: a job that produces nothing
   until hour 20 loses 20 hours when it dies at hour 20.
7. **Record the request in the output's provenance**: the nodes, cores, walltime and
   the scheduler's job identifier, so a result can be traced to the run that made it
   ([22-02-05](../02-reproducible-workflows/05-data-versioning.md) §5).

## 6. Practice: a job sequence that survives

- **Idempotent tasks.** Each piece writes its own output; re-submitting a piece
  overwrites it. The same discipline as
  [22-03-03](../03-data-formats-and-engineering/03-data-pipelines.md) §5.
- **A manifest of pieces.** The set of tasks, their parameters and their completion
  state live in a file, so a resubmission can skip finished work.
- **A wrapper script** that catches the scheduler's signals (a near-limit warning, a
  termination) and writes a checkpoint.
- **A test job** at one-hundredth scale, run before the full sweep: it catches the
  errors that would otherwise appear in 200 identical jobs.
- **A log convention** (one file per task, named by the task identifier) so failures
  can be attributed without reading a shared log.

## 7. Worked example: an allocation that looks busy

A group's allocation shows 92 % utilization and their science output is flat.

1. **Check the request shape.** If the jobs request whole nodes for single-threaded
   work, 31 of 32 cores are idle per node-hour — the utilization figure counts node-
   hours, so the waste is invisible in it. Measure the *core* utilization from the
   scheduler's accounting.
2. **Check the walltime accuracy.** If jobs finish in 20 % of their requested walltime,
   the queue is being planned around claims that are five times too large, which
   lengthens every group's wait, including their own.
3. **Check for re-runs.** If a third of the node-hours go to jobs that were re-run
   after a bug, the fix is the test job of §6, not more nodes.
4. **The report.** Nodes requested against cores used, walltime requested against
   runtime, and completed tasks per node-hour — three numbers that make the diagnosis
   visible and checkable.

## Assumptions and regime of validity

1. **Chosen parameters.** The 256 nodes, 400 jobs/day and the wait model's constants are
   teaching values; cluster policies, priorities and backfilling rules differ widely and
   must be read from the site's documentation.
2. **A single partition, no priorities.** Real systems have several partitions, quality
   of service levels and reservation schemes, all of which change the waiting.
3. **No failures.** The model has no node failures or preemptions; a real cluster's
   failure rate is part of the reason for checkpointing.
4. **Utilization as a fraction of a fixed span.** The demonstration divides by a span
   derived from the arrival rate, which is a steady-state device; a bursty workload
   shows different numbers.
5. **No measurement of a real system.** Nothing here describes a particular cluster, and
   no figure should be quoted as a site's behaviour.

## The honest summary

An HPC job request is a claim on the machine, and the claim's shape decides both the
wait and the waste: queueing rises with nodes × hours (0.54 h for a 1-node-hour request
against 8.08 h for 768 node-hours in the model), a walltime limit removes the longest
jobs from the queue, and a mix of 4 000 jobs asks for 91.9 % of a 256-node partition.
The measurements that matter are not the cluster's utilization but the request's
accuracy — cores used against cores claimed, runtime against walltime, completed work
per node-hour — and the practices that follow are unremarkable: measure first, set the
walltime from the measurement, request cores rather than nodes, split long jobs into
restartable pieces, test at small scale, checkpoint, and record the run's parameters
with the result.

## Python demonstration

[`code/cluster_jobs_demo.py`](./code/cluster_jobs_demo.py) prints, with
`np.random.default_rng(20261014)`:

1. the job mix (median 2 nodes, mean 3.0, maximum 70, 1 806 755 core-hours);
2. the wait table by job shape (0.54 h to 8.08 h) and the effect of five walltime limits;
3. the utilization arithmetic (56 461 of 61 440 node-hours, 91.9 %);
4. the four request-shape mistakes and the node-hours each wastes.

```bash
cd 22-data-engineering-reproducibility/06-high-performance-and-cloud/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python cluster_jobs_demo.py
```

## Exercises

Graded problems and worked solutions are in
[`exercises/01-cluster-jobs-exercises.md`](./exercises/01-cluster-jobs-exercises.md)
and
[`exercises/01-cluster-jobs-solutions.md`](./exercises/01-cluster-jobs-solutions.md).

## Mastery checkpoint

Without notes: a 512-node partition receives jobs whose median request is 4 nodes for
6 hours, with a tail reaching 128 nodes and 48 hours.

1. Compute the request fraction of a 64-node, 12-hour job and of a 4-node, 24-hour job,
   and state which waits longer under the product rule.
2. State the two quantities a job request declares that determine its waiting, and the
   two that determine its resource use.
3. Compute the node-hours wasted by requesting 32 cores for a single-threaded job over
   12 hours.
4. State the three numbers you would report to show an allocation is being used well.

## Common pitfalls

1. **Requesting the maximum walltime "to be safe".** It lengthens the queue for everyone
   and idles nodes when the job finishes early.
2. **Whole-node requests for thread-count-1 code.** 31 of 32 cores idle for the job's
   duration.
3. **No intermediate output.** A failure at hour 20 costs 20 hours.
4. **One huge job.** No resumability, and a longer wait than the same work as pieces.
5. **Judging success by utilization.** A busy partition can be producing nothing.
6. **Not recording the run's parameters.** The result cannot be traced to the allocation
   that produced it.

## Where this is used

- **Regional and national clusters** — the daily environment of most computational
  geophysics.
- **Institutional partitions** — where the queue's shape is set by the mix of teaching
  and research jobs.
- **Cloud HPC services** — the same request arithmetic with a bill attached:
  see [22-06-02 Cloud Computing for Geophysical Computation](./02-cloud-computing-research.md).
- **Batch processing of archives** — thousands of independent tasks where the array
  mechanism and idempotence matter most:
  see [22-03-03 Designing Robust Data Pipelines for Earth Data](../03-data-formats-and-engineering/03-data-pipelines.md).

## Related lessons

- [22-06-02 Cloud Computing for Geophysical Computation](./02-cloud-computing-research.md) —
  the same scaling questions with elastic capacity.
- [22-06-03 Cost, Scaling and Practical Efficiency](./03-cost-and-scaling.md) —
  the core-hour arithmetic behind the request.
- [22-04-04 Big-Data Patterns: Partitioning, Chunking, Out-of-Core](../04-databases-and-large-data/04-big-data-patterns.md) —
  how to split a problem into jobs.
- [19-06 HPC and Parallel Computing](../../19-numerical-modeling-hpc/06-hpc-and-parallel-computing/README.md) —
  the algorithms that make a request worth making.

## Self-assessment checklist

- [ ] I can describe a request's four declarations.
- [ ] I can compute the request fraction and compare two job shapes.
- [ ] I can compute a mix's requested utilization and state its limits.
- [ ] I can choose a walltime and node count from a measurement.
- [ ] I can design a job sequence that survives a kill or a limit.
- [ ] I can name the three numbers that show an allocation is used well.
