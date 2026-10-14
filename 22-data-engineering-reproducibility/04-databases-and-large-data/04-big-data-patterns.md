---
id: 22-04-04
title: "Big-Data Patterns: Partitioning, Chunking, Out-of-Core"
level: research
prereqs: ["22-04-03", "22-03-02"]
estimated_minutes: 50
tags: [big-data, partitioning, out-of-core, skew, data-engineering]
---

# Big-Data Patterns: Partitioning, Chunking, Out-of-Core

## Learning objectives

By the end of this lesson you will be able to:

1. **Decide** whether a computation fits in memory, and **choose** a chunk loop that
   needs one pass, two passes, or an approximation.
2. **Measure** partition skew and **compute** the wall-time penalty a single hot key
   imposes.
3. **Choose** a partition count from the measured balance of task overhead against
   parallelism.
4. **Estimate** the shuffle traffic of an out-of-core group-by, and **state** the strategy
   that minimises it.
5. **Diagnose** the four out-of-core failures: a silently truncated chunk loop, an
   unbalanced partition, too many small tasks, and a shuffle that exceeds the disk.
6. **Decide** when to reach for a distributed framework and when a single machine with a
   chunk loop is the better engineering.

Numbers in this lesson are **SYNTHETIC**: the grid, partition keys and memory budgets are
chosen teaching values, and the cost models state their assumptions. No array was written
to disk, no cluster was used, and no framework was benchmarked.

## Prerequisites

- [22-04-03 Time-Series Databases for Sensor Networks](./03-timeseries-databases.md) —
  the append-only archive this lesson's processing reads.
- [22-03-02 Format Trade-Offs: Access Patterns, Compression, Portability](../03-data-formats-and-engineering/02-format-design-tradeoffs.md) —
  chunking for query shape, which is the same arithmetic applied to memory.

## 1. Intuition: two independent problems

"Big data" names two problems that people often conflate:

- **Volume**: the dataset does not fit in memory, so the algorithm must be restructured
  into chunks — *out-of-core* computing.
- **Shape**: the work is unevenly distributed across keys, so parallelism does not shrink
  wall time — *skew*.

A single machine with 64 GB of RAM handles many problems that get sold a cluster, and a
cluster does not fix a hot key. The two measurements that decide the tool are therefore
"does the working set fit?" and "is the work balanced?", and both are computable before
any code is written.

## 2. Out-of-core: how many passes?

The demonstration's **SYNTHETIC** field is $4096 \times 4096 \times 64$ float32 —
**4.3 GB** — with a natural chunk of $512 \times 512 \times 64$ (**67.1 MB**) and a memory
budget of 16 GB. Here the whole field fits in memory, and the chunk loop is a choice
rather than a necessity; the interesting question is what changes when it does not.

The operational rule is that the number of passes is set by the **statistic**, not by the
chunking:

| Statistic | Passes | Why |
|---|---|---|
| mean, sum, min, max, counts | 1 | each chunk contributes a partial result |
| variance via sums of squares, histogram | 1 | sufficient statistics are additive |
| median, percentile, exact quantile | 2 (or sampled) | needs the value distribution before selecting |
| global rank, sort | 2–3 | needs a partitioning or sampling pass first |
| correlation between two chunks | 2 | needs both means before the product |

So an algorithm's memory requirement is a property of its **sufficient statistics**: if
the object being accumulated is a fixed-size summary (sums, counts, a histogram), one pass
suffices; if the answer requires selecting a value from the whole distribution, either a
second pass or an approximation (a reservoir, a sketch, a t-digest-style structure) is
needed. The practical discipline is to decide the statistics before the loop, because
adding an exact median later forces a rewrite.

## 3. Skew: the hot key

A partition-by-key pipeline finishes when its **largest** partition finishes, so a key
that is disproportionately common dominates the wall time. The demonstration models event
counts per station as lognormal (a realistic shape for a network) and measures:

| Quantity | Value |
|---|---|
| rows held by the top station | 1.9 % |
| rows held by the top 5 stations | 8.1 % |
| rows held by the top 10 stations | 12.4 % |
| mean rows per station | 399 |
| largest station | 9 150 — **22.9×** the mean |

A partition-by-station job therefore has a task 22.9× larger than average, so the wall
time is that task's time plus the rest, and adding workers does not help beyond the point
where every other partition is done. Three mitigations, in order of preference:

1. **Change the key granularity** — partition by `(station, month)` rather than by station,
   which spreads a hot station across twelve tasks.
2. **Salt the hot key** — hash the key with a small suffix and reduce the partial results
   afterwards, which distributes one key across many tasks at the cost of a second
   aggregation.
3. **Split the outlier explicitly** — detect the top keys and process them separately,
   which is a manual version of (2) with better diagnostics.

## 4. Partition count: overhead against parallelism

Every partition costs a fixed overhead (a task start, a file open, a planning step). The
demonstration models 3 s per partition over 20 million rows:

| Partitions | Rows/partition | Overhead (s) | Data time (s) | Total (s) |
|---|---|---|---|---|
| 4 | 5 000 000 | 12.0 | 9.6 | 21.6 |
| 64 | 312 500 | 192.0 | 9.6 | 201.6 |
| 1 024 | 19 531 | 3 072.0 | 9.6 | 3 081.6 |
| 16 384 | 1 221 | 49 152.0 | 9.6 | 49 161.6 |

The data time is constant; the overhead is linear in the partition count. The optimum is
where the marginal parallelism gained equals the marginal overhead — some tens to a few
hundreds of partitions for most workloads, far below "one partition per key" for a
high-cardinality key. This is the small-files problem of
[22-03-02](../03-data-formats-and-engineering/02-format-design-tradeoffs.md) §5 seen from
the compute side: 16 384 partitions of 1 221 rows each spend 99.98 % of their time in
overhead.

## 5. Shuffles: the cost out-of-core adds

A group-by that does not fit in memory is executed as a **shuffle**: partition the rows by
key, aggregate each partition, merge the partial states. The demonstration's example is
$2 \times 10^{9}$ rows of 120 B — **240 GB** — with a 1 200-group hash table of 0.31 MB
(a group-by whose *output* is tiny and whose *input* is enormous, the common case in
Earth data). The modelled spill traffic is

$$S_{\text{spill}} \approx 2 \times 240\ \text{GB} = 480\ \text{GB},$$

because the worst case writes every partition to storage and reads it back. Three
consequences:

1. **Disk becomes the limit.** The job's runtime is set by the storage's throughput, not
   by the CPU; a machine with fast local NVMe finishes the shuffle far sooner than one
   with a network filesystem.
2. **A larger-than-memory sort is a shuffle twice over** (partition, sort each partition),
   so the traffic roughly doubles again.
3. **Combining early is worth a lot.** A partial aggregation on the map side (pre-summing
   within a partition before the shuffle) can cut the shuffled volume by orders of
   magnitude when the key cardinality is low — which is the situation in the example: 240
   GB in, 0.31 MB out.

## 6. Practice: choosing the engineering

1. **Measure the working set first.** Compute the size of the data, the largest chunk, and
   the sufficient statistics; if they fit, a chunk loop on one machine is the simplest
   correct answer.
2. **Decide the statistics before the loop.** Order statistics force passes; plan for them
   or choose an approximation deliberately.
3. **Partition by the query, not by the key.** Time partitions serve time-window queries;
   a partition-by-key only helps if the workload is per key.
4. **Count the partitions and the overhead.** Tens to hundreds of partitions, not
   thousands; check the smallest partition's size against the per-task overhead.
5. **Detect skew before it bites.** A histogram of the partition key is cheap and shows
   both the hot key and the tail.
6. **Aggregate as early as possible.** Pre-aggregation is the single largest saving in a
   shuffle.
7. **Report the pass count and the traffic**, not just the wall time: they are what a
   reviewer can check.

## 7. Worked example: a 2 TB stack that fits on one machine

A group processes 2 TB of gridded output with a distributed framework and waits eight
hours. The processing is a per-cell temporal mean and a per-cell 95th percentile.

1. **Compute the working set.** The mean needs one floating-point accumulator per cell —
   a 4 KB grid means 2 MB of accumulators — so it is a one-pass stream. The 95th
   percentile needs the distribution per cell; an exact computation requires either two
   passes with sorted samples on disk or an approximation, and the approximation is
   usually the right answer at that scale.
2. **Compute the I/O.** 2 TB at 500 MB/s from local storage is about 67 minutes if read
   once, so the eight hours are not I/O-bound: they are overhead, network or skew.
3. **Check the partition count.** If the framework launched 100 000 tasks of 20 MB each,
   the modelled 3 s per task is 83 hours of overhead across workers — the small-task
   problem, and the likely explanation.
4. **The recommendation.** Repartition to a few hundred tasks of a few GB each, use
   one-pass accumulators for the mean, and an approximate quantile; the same machine
   then does the job in a fraction of the time, with the pass count and the traffic
   measurable.

## Assumptions and regime of validity

1. **Chosen overheads.** The 3 s per partition and the transfer rates are teaching values;
   the structure (overhead linear in the task count, data time constant) is the transferable
   part.
2. **Lognormal key distribution.** Real network event counts are heavy-tailed, but the
   parameters differ; skew must be measured on the data, not assumed.
3. **A shuffle costing 2× the data volume.** Real systems vary with compression, partial
   aggregation and memory; the figure is the worst case's order of magnitude.
4. **No concurrency effects.** The model ignores contention, queueing and the scheduler's
   own overheads, all of which grow with the task count — so it understates the penalty of
   too many partitions.
5. **A chosen memory budget.** Sixteen gigabytes is a laptop-class figure; the arithmetic
   scales, and the conclusion (order statistics and shuffles are the memory-sensitive
   parts) does not depend on the number.

## The honest summary

Out-of-core computing is not about the volume of the data but about the size of the
sufficient statistics: a mean over a 4.3 GB field streamed in 67 MB chunks is a one-pass
problem with a few megabytes of accumulators, while an exact median forces a second pass
or an approximation. Skew is the second independent problem: a key holding 1.9 % of the
rows is 22.9× the mean and sets the wall time, and salting or finer partitioning is the
remedy. Partition counts trade a linear overhead against parallelism — 16 384 partitions
of 1 221 rows spend 99.98 % of their time starting — and an out-of-core group-by pays a
shuffle of about twice the data volume, which early aggregation and a large enough
working set are the ways to avoid.

## Python demonstration

[`code/big_data_patterns_demo.py`](./code/big_data_patterns_demo.py) prints, with
`np.random.default_rng(20261014)`:

1. the 4.3 GB field's chunk size and pass count, and the statistic-to-pass table;
2. the skew measurement: 1.9 %, 8.1 % and 12.4 % for the top 1, 5 and 10 stations, and
   the 22.9× hot task;
3. the partition-count table from 4 to 16 384 partitions, showing the overhead crossing;
4. the group-by arithmetic: 240 GB in, 0.31 MB out, 480 GB of modelled spill traffic.

```bash
cd 22-data-engineering-reproducibility/04-databases-and-large-data/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python big_data_patterns_demo.py
```

## Exercises

Graded problems and worked solutions are in
[`exercises/04-big-data-patterns-exercises.md`](./exercises/04-big-data-patterns-exercises.md)
and
[`exercises/04-big-data-patterns-solutions.md`](./exercises/04-big-data-patterns-solutions.md).

## Mastery checkpoint

Without notes: a 3 TB array of 2 billion rows of 120 B must be grouped by station
(1 000 groups) and reduced to a per-station mean and 99th percentile.

1. State the pass count for each statistic and the sufficient statistics you would keep.
2. State the spill traffic you would budget for.
3. A key holds 8 % of the rows. Compute the hot task's size relative to the mean, and
   state two mitigations.
4. State the partition count you would aim for and the measurement that justifies it.

## Common pitfalls

1. **Reaching for a cluster before measuring.** A 4.3 GB field with 67 MB chunks is one
   pass on a laptop.
2. **Choosing statistics after the loop.** Adding an exact median later forces a rewrite.
3. **Partitioning by a hot key.** The wall time is set by one key: 1.9 % of the rows was
   22.9× the mean in the demonstration's model.
4. **One partition per key.** 16 384 partitions spend 99.98 % of their time in overhead.
5. **Ignoring the shuffle.** Twice the data volume moves through storage in the worst
   case, and early aggregation is the lever.
6. **Assuming balanced keys.** The distribution is a property of the data; measure it with
   a histogram before the job.

## Where this is used

- **Gridded model output** — the temporal-mean and percentile problem of §7 is the
  standard workflow.
- **Catalogue group-bys** — low-cardinality output from high-volume input, the shuffle's
  best case for early aggregation.
- **Cloud-native arrays** — chunked storage makes out-of-core processing natural:
  see [22-04-05 Cloud-Native Geoscience Data Access](./05-cloud-native-geoscience.md).
- **Cluster execution** — the partition count and the shuffle traffic are what the
  scheduler sees: see
  [22-06-01 Running Jobs on HPC Clusters and Schedulers](../06-high-performance-and-cloud/01-cluster-jobs.md).

## Related lessons

- [22-04-03 Time-Series Databases for Sensor Networks](./03-timeseries-databases.md) —
  partitioning by time for append-heavy data.
- [22-03-02 Format Trade-Offs](../03-data-formats-and-engineering/02-format-design-tradeoffs.md) —
  the same granularity argument applied to reads.
- [19-06 HPC and Parallel Computing](../../19-numerical-modeling-hpc/06-hpc-and-parallel-computing/README.md) —
  the algorithms that scale across nodes.
- [22-06-02 Cloud Computing for Geophysical Computation](../06-high-performance-and-cloud/02-cloud-computing-research.md) —
  where the shuffle meets a billed instance.

## Self-assessment checklist

- [ ] I can decide whether a computation is a one-pass, two-pass or approximate problem.
- [ ] I can measure partition skew and compute the hot-task penalty.
- [ ] I can choose a partition count from the overhead balance.
- [ ] I can estimate shuffle traffic.
- [ ] I can name the four out-of-core failures.
- [ ] I can justify a single-machine design over a distributed framework.
