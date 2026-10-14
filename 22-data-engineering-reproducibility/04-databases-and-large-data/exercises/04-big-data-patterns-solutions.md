# Solutions — 22-04-04 Big-Data Patterns: Partitioning, Chunking, Out-of-Core

> Read after attempting. Numbers are computed here and match the demonstration's
> printed output. Lesson:
> [04 Big-Data Patterns](../04-big-data-patterns.md).

---

## ★1 — The two problems

- **Volume**: the working set does not fit in memory. Decided by the size of the data and
  of the **sufficient statistics** compared with the available memory.
- **Shape**: the work is unevenly distributed across keys. Decided by the histogram of the
  partition key (the ratio of the largest partition to the mean).

A cluster addresses the first and not the second; a chunk loop on one machine addresses
the first and leaves the second alone as well.

## ★2 — Does the field fit?

(a) $4096 \times 4096 \times 64 \times 4\ \text{B} = 4.295 \times 10^{9}\ \text{B} =
4.3$ GB (the printed value).

(b) $512 \times 512 \times 64 \times 4 = 6.71 \times 10^{7}\ \text{B} = 67.1$ MB (the
printed value).

(c) It **fits** in 16 GB, so the chunk loop is a choice about working set and cache
behaviour, not a necessity: the algorithm can read the whole field, and chunking is used
to keep the working set small (a 67 MB chunk with a few megabytes of accumulators) rather
than to overcome a limit. When the field grows past the budget, the same loop keeps
working — which is the reason to write it that way from the start.

## ★3 — Passes by statistic

| Statistic | Passes | Reason |
|---|---|---|
| mean | 1 | sum and count are additive sufficient statistics |
| variance | 1 | via sums of $x$ and $x^{2}$ (or Welford's update) |
| median | 2 or approximation | needs the distribution before selecting |
| count above a threshold | 1 | a count is additive |
| 99th percentile | 2 or approximation | as for the median |

## ★★4 — Skew

(a) $9150/399 = 22.9$ — the printed ratio.

(b) On 40 workers, the job finishes when the largest partition finishes; if each worker
takes one partition, 39 workers idle while one processes a partition 22.9× the mean. The
wall time is therefore close to the serial time of that partition, and adding workers
beyond ~40 changes nothing. In practice a scheduler splits the largest partitions, but
the imbalance remains until the key's granularity changes.

(c) Mitigations:

1. **Finer key**: partition by `(station, month)`, which divides the hot station across
   twelve tasks and reduces the maximum to roughly $9150/12 \approx 763$ rows (near the
   mean) — cost: twelve times as many partitions, and the aggregation must sum the twelve
   partial results (a trivial second stage).
2. **Salting**: hash the station with a small suffix (0–9) so one key becomes ten, with a
   final reduction over the ten partial states — cost: an extra aggregation stage and a
   slightly larger intermediate state, plus the risk of over-splitting a small station if
   the salt is applied blindly.
   Both work by the same mechanism: move work off the hot key, and pay with a second
   aggregation.

## ★★5 — Partition count

(a) Totals: 4 partitions → 21.6 s; 64 → 201.6 s; 1 024 → 3 081.6 s; 16 384 → 49 161.6 s.

(b) At 16 384 partitions the overhead is 49 152 s of 49 161.6 s =
$49\,152/49\,161.6 = 99.98\ \%$.

(c) Choose a count in the **tens to low hundreds** — say 64 to 256 — for a 20-million-row
job. The reasoning: the data time (9.6 s) is constant, so the only variable is the
overhead (3 s per partition). A count of 64 costs 192 s of overhead — still dominating
the data time, which shows that the modelled overhead is high relative to the data; with
a more realistic per-task overhead of ~0.1 s the optimum sits in the hundreds. The
principle to carry is that the count is chosen where the marginal parallelism (more
partitions run concurrently) stops compensating the marginal overhead (one more task
start), and that the right value must be measured on the target system.

## ★★6 — An out-of-core group-by

(a) Input: $2 \times 10^{9} \times 120\ \text{B} = 240$ GB. Output: 1 000 groups, with a
hash table of about $1000 \times 256\ \text{B} = 0.26$ MB (the demonstration prints
0.31 MB for 1 200 groups). Modelled spill traffic: $2 \times 240 = 480$ GB.

(b) **Pre-aggregation on the map side**: sum the rows belonging to the same key within a
chunk before the shuffle. With 1 000 keys and 240 GB of input, each chunk of, say,
128 MB contains about 1.07 million rows spread over 1 000 keys, i.e. ~1 070 rows per
key per chunk; pre-summing reduces each chunk's shuffled output to 1 000 rows of a few
bytes — a reduction of three orders of magnitude in the shuffled volume. It works **here**
because the key cardinality is low relative to the rows per chunk, which is exactly the
situation the demonstration describes; with a high-cardinality key (one group per row)
pre-aggregation achieves nothing.

(c) Once out-of-core, the runtime is set by **storage throughput**: the shuffle's write
and read of 480 GB, plus the sort if the aggregation is sorted. The CPU is idle waiting,
which is why local NVMe storage changes the wall time more than a faster processor.

## ★★★7 — Fifty terabytes of model output

**Chunking.** Chunks of one time step per region ($1000 \times 1000$ cells, 4 MB at
float32) read from a chunked store; the processing iterates over time, keeping
per-cell accumulators (a 4 MB array for the mean, plus a fixed budget for the
percentile structure).

**Pass counts and sufficient statistics.**

1. **Temporal mean**: one pass; keep per-cell `sum` and `count` (8 MB of accumulators at
   float64). Exact.
2. **99th percentile**: two passes with per-cell histograms (a fixed 256-bin histogram per
   cell is $1000 \times 1000 \times 256 \times 4\ \text{B} = 1$ GB — feasible), giving a
   bin-resolved percentile in one pass over the data plus a small second pass. An exact
   percentile would require storing or re-reading the data per cell, which is 50 TB of
   I/O per cell group — unacceptable.
3. **Per-region monthly summary**: this is a *reduction over space and time per month*,
   so it needs one pass per month, or a partition-by-month job with pre-aggregation; the
   output is small (regions × months).

**Intermediate storage.** The accumulators (8 MB + 1 GB of histograms) and the shuffle's
partition files. The histograms are the dominant intermediate; they are the price of the
percentile.

**Shuffle traffic.** If the batch is partitioned by month, the shuffle moves the rows of
each partition once: about 50 TB in the worst case if the partition files are written and
read (100 TB of traffic). Pre-aggregation on the map side reduces this dramatically for
the monthly summary (region-month groups are low-cardinality), and the mean's
accumulators are per-cell, so a spatially partitioned pass avoids a shuffle entirely.

**The dominating step.** The **percentile's histogram pass**: it is the only tier that
requires 50 TB of reads plus a gigabyte of per-cell state, and it is the reason the
archive should be chunked spatially (so a region can be processed with only its own
chunks resident). Everything else is a streaming reduction.

## ★★★8 — Measuring the skew of a key

**Data.** The partition key and the row count per key (from a database's statistics, from
a group-by over a sample, or from a histogram of the key column), for a representative
window rather than the whole history.

**Statistics and the decision each drives.**

1. **Maximum-to-mean ratio**: drives whether the largest task will dominate the wall time
   — the demonstration's 22.9× is the headline number.
2. **Fraction of rows in the top 1 % of keys** (a concentration measure): drives whether
   salting or finer partitioning is worth the extra aggregation. If the top 1 % holds 40 %
   of the rows, the key is concentrated and the remediation is structural.
3. **Number of keys with more than $k$ rows**: drives the partition count needed to keep
   each task above the overhead threshold (>3 s of work, in this lesson's model).
4. **Entropy or a Lorenz curve** of the key distribution: summarises the shape, and makes
   a change between two windows visible (the key distribution of a network changes as
   stations are added).

**What the measurements cannot tell you about the running job.** How the framework
actually splits the work: many systems divide a large partition into tasks of bounded
size, so the observed wall time may be better (or worse, with contention) than the
key-level prediction; and how the shuffle's partitioning interacts with the key
distribution. The measurements are about the data's shape, and the job's behaviour also
depends on the engine's decisions, which must be read from the job's own metrics.

## ★★★9 — Diagnosing 100 000 tasks and eight hours

**Measurements to take first.**

1. **Task count and duration distribution**: the number of tasks, their median and maximum
   duration, and the time spent in scheduling versus execution.
2. **Data volume and throughput**: bytes read and written, and the achieved throughput; a
   byte-per-second figure settles whether the job is I/O-bound.
3. **Key histogram** (★8's statistics): the largest partition against the mean.
4. **Per-task overhead**: the observed time for a task that reads nothing (a no-op task in
   the same framework), giving the framework's own cost per task.

**The arithmetic that distinguishes the causes.** For 100 000 tasks:

- **Overhead**: $100\,000 \times (\text{no-op time})$. At 0.1 s per task that is 2.8 hours
  of aggregate overhead — with any concurrency, the wall-time contribution is
  $2.8\ \text{h}/\text{workers}$; at 20 workers it is 8.4 minutes, at 2 workers 1.4 hours.
  Sum the observed over/under-run of task durations against their work to see whether the
  overhead explains the eight hours at the actual concurrency.
- **Data**: total bytes divided by achieved throughput. If the job reads 50 TB at
  500 MB/s, that is 27.8 hours of single-stream time, i.e. 1.4 hours on 20 streams — if
  the measured throughput is much lower, the storage or the network is the limit.
- **Skew**: the largest partition's time against the mean, with the tail of the task
  duration distribution. A maximum 20× the median is the signature.

**The change for each diagnosis.** Overhead → reduce the task count (coarser partitions,
fewer small files). Data → more parallelism, better locality, or a compressed
representation
([22-03-01](../../03-data-formats-and-engineering/01-file-formats-scientific.md)).
Skew → finer key granularity or salting (§3). If all three look healthy and the job is
still slow, look for **contention**: network saturation, a hot storage node, or a lock.

**The case in which the framework is genuinely necessary.** When the working set cannot be
made to fit **and** the processing must be parallel to meet a deadline **and** the
partitions are balanced: for example, a cross-correlation over 500 TB of waveforms where
the per-chunk state is large and the compute per byte is substantial. If the working set
fits a single machine's memory or its NVMe, the framework's overhead has to buy something
else — operational convenience, reproducibility across sites, or a shared cluster's
queue — and that trade should be stated rather than assumed.
