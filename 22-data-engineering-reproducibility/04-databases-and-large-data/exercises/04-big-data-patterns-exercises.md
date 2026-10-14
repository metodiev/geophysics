# Exercises — 22-04-04 Big-Data Patterns: Partitioning, Chunking, Out-of-Core

Attempt these before reading the
[solutions](./04-big-data-patterns-solutions.md). The lesson is
[04 Big-Data Patterns](../04-big-data-patterns.md). Numbers refer to the **SYNTHETIC**
model of `code/big_data_patterns_demo.py`: a $4096 \times 4096 \times 64$ float32 field,
16 GB of memory, lognormal station counts, 3 s of overhead per partition, 20 million
rows of 120 B, and a 2-billion-row group-by.

## ★ Foundational

**★1.** State the two independent problems that "big data" names, and give the single
measurement that decides each.

**★2.** For the demonstration's field: (a) compute its size in GB; (b) compute the size
of a $512 \times 512 \times 64$ chunk; (c) state whether the field fits in the 16 GB
budget and what that implies for the chunk loop.

**★3.** State which of these need one pass, two passes, or an approximation, and why:
a mean, a variance, a median, a count above a threshold, a 99th percentile.

## ★★ Applied

**★★4.** The demonstration's skew model gives a largest station of 9 150 rows against a
mean of 399.

(a) Compute the ratio. (b) State the wall-time consequence for a partition-by-station job
on 40 workers. (c) Propose two mitigations and state the cost of each.

**★★5.** Using the partition-count table: (a) state the total time for 4, 64, 1 024 and
16 384 partitions; (b) compute the fraction of the total that is overhead at 16 384
partitions; (c) state the partition count you would choose for a 20-million-row job and
the reasoning.

**★★6.** A group-by reads 2 billion rows of 120 B and produces 1 000 groups.

(a) Compute the input volume, the output size and the modelled spill traffic. (b) State
the one optimisation that reduces the traffic most and why it works here. (c) State what
limits the job's runtime once it is out-of-core.

## ★★★ Research-oriented

**★★★7.** Design an out-of-core processing plan for 50 TB of gridded model output that
must produce (i) a per-cell temporal mean over the whole archive, (ii) a per-cell 99th
percentile, and (iii) a per-region monthly summary. State the chunking, the pass counts,
the sufficient statistics, the intermediate storage, and the shuffle traffic. State the
step that dominates the cost.

**★★★8.** The lesson's skew model is lognormal. Design a measurement of the actual skew
of a partition key in a dataset you have: state the data, the summary statistics (maximum
to mean, the fraction in the top 1 %, a Lorenz-style concentration), and the operational
decision each statistic drives. State what the measurements cannot tell you about the
running job.

**★★★9.** A pipeline runs on a distributed framework with 100 000 tasks and takes eight
hours. Design the diagnosis: state the measurements you would take first, the arithmetic
that distinguishes overhead from data from skew, and the change you would make for each
diagnosis. State the case in which the framework is genuinely necessary.
