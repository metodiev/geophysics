---
id: 22-04-01
title: "Relational Databases and SQL for Earth Data"
level: advanced
prereqs: ["22-03-03", "22-03-06"]
estimated_minutes: 50
tags: [databases, sql, indexing, query-planning, earth-data]
---

# Relational Databases and SQL for Earth Data

## Learning objectives

By the end of this lesson you will be able to:

1. **Model** a table as pages and rows, and **compute** the cost of a full scan from
   the page count and the read pattern.
2. **Choose** between a scan and an index for a stated selectivity, and **explain**
   why the planner's estimate decides the outcome.
3. **Compute** a B-tree's depth and the cost of a point lookup, and **state** why an
   index is affordable.
4. **Compare** nested-loop and hash joins by table size, and **state** which side to
   build on.
5. **Design** a schema that makes the common query cheap and the wrong result
   impossible, using keys, constraints and types.
6. **Diagnose** a slow query from its plan rather than from its SQL.

The table, page and index numbers in this lesson are **SYNTHETIC**: the demonstration
describes a table and applies a cost model with chosen page sizes and read latencies.
No database was created or queried, and no benchmark of a real engine is quoted.

## Prerequisites

- [22-03-03 Designing Robust Data Pipelines for Earth Data](../03-data-formats-and-engineering/03-data-pipelines.md) —
  the writes, keys and reconciliation that feed the tables.
- [22-03-06 Metadata Standards and Controlled Vocabularies](../03-data-formats-and-engineering/06-metadata-standards.md) —
  the types and vocabularies a schema enforces.

## 1. Intuition: a table is a set with a cost model

SQL describes *what* should be returned; the engine decides *how*, and the how is
chosen from statistics. That separation is the source of both the power and the
surprises: the same query runs in milliseconds or hours depending on an estimate the
analyst never sees unless they ask for the plan. For Earth data — millions of events,
billions of samples, spatially local queries — the cost model is the difference between
an interactive tool and an overnight job.

The two quantities the model rests on are **pages** and **access pattern**. A
sequential page read is cheap; a random one can cost tens of times more. Every
indexing decision is a trade of more random reads now against fewer sequential reads
later, and the balance flips with the *selectivity* of the query.

## 2. Pages, rows and the scan

For a table of $R$ rows of $b$ bytes in pages of $P$ bytes, the page count is

$$N_{\text{pages}} = \left\lceil \frac{R}{\lfloor P/b \rfloor} \right\rceil .$$

The demonstration's **SYNTHETIC** table has $R = 5\times 10^{6}$ rows of $b = 120$ B in
$P = 8$ KiB pages, so $\lfloor 8192/120 \rfloor = 68$ rows per page and
$N_{\text{pages}} = 73\,530$; the table is 0.60 GB. At a chosen 0.02 ms per sequential
page read, a full scan costs **1.5 s**.

That number frames everything else. A scan is *per-row* cheap because it streams, and
it is the right plan when the query returns a large fraction of the table. For a query
returning 50 rows out of 5 million it is absurd, and that is what an index is for.

## 3. Selectivity decides the access path

With an index, the cost of a lookup is the path down the tree plus the leaf pages
touched, all read at the random-access latency:

$$C_{\text{index}} \approx \left(d + \frac{\text{rows}}{68}\right) \times
\ell_{\text{random}} .$$

The demonstration compares the two paths with $\ell_{\text{random}} = 0.6$ ms:

| Selectivity | Rows returned | Scan (s) | Index (s) | Chosen |
|---|---|---|---|---|
| $10^{-5}$ | 50 | 1.5 | 0.00 | index |
| $10^{-4}$ | 500 | 1.5 | 0.01 | index |
| $10^{-3}$ | 5 000 | 1.5 | 0.05 | index |
| $10^{-2}$ | 50 000 | 1.5 | 0.44 | index |
| $10^{-1}$ | 500 000 | 1.5 | 4.41 | **scan** |

The crossover sits between 1 % and 10 % selectivity — the index's leaf reads match the
scan's cost at about $1.7 \times 10^{5}$ rows, i.e. 3.4 % of the table. Below it the
index wins by orders of magnitude; above it the random reads
outweigh the sequential stream. The exact position depends on the latency ratio
(0.6 ms against 0.02 ms here, i.e. 30×) and on how well the rows are clustered: an
index scan over physically sorted rows behaves far better than one over scattered
rows, which is why the *insertion order* of a table matters as much as its indexes.

The practical consequence for the analyst: **the plan is chosen from an estimate of
selectivity**, and a stale or wrong statistic produces the wrong plan — a scan where an
index was needed, or an index where a scan was cheaper. `EXPLAIN`-style plans are
therefore a diagnostic tool, not a curiosity.

## 4. B-trees: why an index is affordable

A B-tree with fan-out $f$ over $R$ rows has depth

$$d = \left\lceil \frac{\ln R}{\ln f} \right\rceil .$$

For $f = 200$ and $R = 5 \times 10^{6}$, $d = 3$ levels: a point lookup touches
**4 pages** (three index levels plus one leaf), costing $4 \times 0.6\ \text{ms} =
2.40$ ms against 1.5 s for a scan — a factor of 625. The index itself is 0.04 GB
(key plus pointer, 8 bytes per row) or **7 % of the table's size**, and it grows with
$\log R$ in depth, so it stays small as the table grows.

Two practical notes. First, an index makes **writes** more expensive: every insert
updates the tree, so a table with six indexes costs several times a bare insert. Second,
a composite index serves only queries whose leading columns are constrained, which is
why the order of columns in the index definition follows the queries, not the schema's
aesthetic.

## 5. Joins: which side to build on

For a match between a large table (5 million rows here) and a smaller one, the two
strategies are:

- **nested loop with an index** on the large table: cost $\approx R_{\text{right}}
  \times (d+1) \times \ell_{\text{random}}$;
- **hash join**: read the smaller side to build a hash table, then read the larger side
  to probe it, both sequentially.

| Right-side rows | Nested loop (s) | Hash join (s) | Chosen |
|---|---|---|---|
| 100 | 0.24 | 1.50 | nested loop |
| 1 000 | 2.40 | 1.50 | hash join |
| 10 000 | 24.00 | 1.50 | hash join |
| 100 000 | 240.00 | 1.53 | hash join |
| 1 000 000 | 2 400.00 | 1.80 | hash join |
| 10 000 000 | 24 000.00 | 4.50 | hash join |

The nested loop wins only for a handful of right-hand rows: it pays one random lookup
per row, while the hash join pays two sequential scans of the tables regardless. The
general rules are that the **smaller relation is the one to build on** (so the hash
table fits in memory) and that the summary statistics must be current, or the planner
builds the wrong side and spills.

## 6. Schemas that prevent wrong answers

Cost is half the subject; the other half is correctness, and it is enforced by
declarations:

1. **Primary keys** on the natural identifier (station, channel, time) make duplicate
   ingestion impossible — the same key that solves
   [22-03-03](../03-data-formats-and-engineering/03-data-pipelines.md) §5.
2. **Foreign keys** between events and stations prevent orphan rows; the check costs a
   lookup per insert and buys the guarantee that a join will not silently drop data.
3. **Types** (`timestamp with time zone`, `numeric` where exact decimal arithmetic
   matters, `text` for codes such as `007`) prevent the class of bug where a code is
   silently converted to a number.
4. **Constraints** (ranges, nullability, vocabulary membership) are the schema-level
   version of the validation gate of
   [22-03-06](../03-data-formats-and-engineering/06-metadata-standards.md) §6.
5. **Units in naming or in a companion table**, because a column called `amplitude` is
   ambiguous and a column called `amplitude_ms2` is not.

## 7. Practice: working with a database rather than against it

1. **Aggregate in the engine.** Pulling 5 million rows into Python to average them
   moves the data instead of the computation.
2. **Write queries that can use the index** (sargable predicates: compare the column to
   a value, do not wrap it in a function).
3. **Ask for the plan** on any query that takes longer than you expect, and read the
   estimated against actual row counts.
4. **Keep statistics fresh** — an explicit analyse step after a bulk load.
5. **Batch inserts in transactions**, and use the pipeline's write-then-rename idea at
   the table level: load into a staging table, validate, then swap or insert-select.
6. **Version the schema** and the migrations, so an analysis can state which schema it
   ran against.

## 8. Worked example: a spatial-temporal query

A query returns the events for one station in one year: about 400 rows out of 5
million ($8 \times 10^{-5}$ selectivity) with a composite index on
`(station, time)`.

1. **Access path.** Selectivity is far below the 1–2 % crossover of §3, so the index is
   the right plan: 400 rows over about 6 leaf pages, plus 4 pages of tree traversal,
   ~6 ms against 1.5 s for a scan.
2. **Clustering.** If the table is physically ordered by `(station, time)` as well, the
   400 rows occupy consecutive pages and the leaf reads become sequential — a further
   substantial gain. This is why ingestion order is a design decision.
3. **Aggregation.** If the answer is a monthly count, the engine should aggregate; the
   400 rows travelling to the client are unnecessary.
4. **What could go wrong.** A predicate written as `date_trunc('year', time) = 2024`
   cannot use the index (the column is wrapped in a function), so the query scans; the
   plan would show it immediately.

## Assumptions and regime of validity

1. **Chosen page sizes and latencies.** Real engines, storages and caches differ by
   factors; the *structure* of the cost model is what transfers, not the constants.
2. **No caching.** The model has no buffer pool, so it overstates repeated-access costs;
   a warm cache changes the index/scan crossover materially.
3. **Uniform rows.** Average row size hides variable-length columns; wide rows lower
   rows-per-page and raise every cost.
4. **Clustered index reads.** The amplification of an index scan depends on how
   correlated the index order is with the physical order; the model uses a single
   random-read latency for both.
5. **No concurrency.** The costs are single-query; under concurrency the limiting
   resource is often the storage device rather than any single plan.

## The honest summary

A relational engine chooses an access path from statistics, and the two paths have
different shapes: the scan streams 73 530 pages in 1.5 s, while an index walk from a
three-level B-tree costs about 2.4 ms for a point lookup and stays cheaper than a scan
until the query returns roughly 3 % of the table. Joins follow the same logic — build
the hash on the smaller side, and use an index-nested-loop only when the other side is
tiny — and the choice rests on estimates that must therefore be maintained. The other
half of the subject is correctness, and it is enforced by declarations: keys, foreign
keys, types, constraints and units in names make the wrong result impossible rather
than unlikely.

## Python demonstration

[`code/relational_databases_demo.py`](./code/relational_databases_demo.py) prints, with
`np.random.default_rng(20261014)`:

1. the table's pages and the 1.5 s scan cost;
2. the scan-versus-index table across five selectivities, with the crossover at 10 %;
3. the three-level B-tree, 4 pages per lookup, 2.40 ms against 1.5 s, and a 7 %-sized
   index;
4. the join strategy table from 100 to 10 million right-hand rows.

```bash
cd 22-data-engineering-reproducibility/04-databases-and-large-data/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python relational_databases_demo.py
```

## Exercises

Graded problems and worked solutions are in
[`exercises/01-relational-databases-exercises.md`](./exercises/01-relational-databases-exercises.md)
and
[`exercises/01-relational-databases-solutions.md`](./exercises/01-relational-databases-solutions.md).

## Mastery checkpoint

Without notes: a table has 20 million rows of 200 B in 8 KiB pages, with a
sequential page cost of 0.02 ms and a random page cost of 0.6 ms.

1. Compute the rows per page, the page count and the scan time.
2. Compute the index-scan cost for a query returning 2 000 rows and for one returning
   400 000 rows, and state which plan you expect.
3. State two predicates that would prevent an index from being used.
4. A nightly load doubles the table and the queries slow down tenfold without any
   change to the SQL. State the most likely cause and the first diagnostic.

## Common pitfalls

1. **Reading a cost model as a benchmark.** The constants here are chosen; the
   crossover's *position* moves with the storage and the cache.
2. **Wrapping a column in a function.** It makes the predicate unusable by the index
   and turns a millisecond query into a scan.
3. **Indexing everything.** Each index slows every insert and consumes space; a table
   with six indexes pays for all of them on every load.
4. **Letting a schema store codes as numbers.** `007` becomes `7` and station joins
   silently lose rows.
5. **Judging a query by its result.** Two queries returning the same rows can differ by
   three orders of magnitude in cost.
6. **Stale statistics.** They are the most common cause of a plan that changes shape
   after a bulk load.

## Where this is used

- **Event catalogues** — the queries are spatial-temporal and the indices are
  composite: see
  [22-04-02 Spatial Databases and PostGIS](02-spatial-databases.md).
- **Sensor archives** — append-heavy tables with time-partitioned indices:
  see [22-04-03 Time-Series Databases for Sensor Networks](03-timeseries-databases.md).
- **Ingestion pipelines** — keys and constraints enforce what the pipeline validates:
  see [22-03-03 Designing Robust Data Pipelines for Earth Data](../03-data-formats-and-engineering/03-data-pipelines.md).
- **Metadata catalogues** — vocabularies as reference tables with foreign keys:
  see [22-03-06 Metadata Standards and Controlled Vocabularies](../03-data-formats-and-engineering/06-metadata-standards.md).

## Related lessons

- [22-04-02 Spatial Databases and PostGIS](02-spatial-databases.md) — the spatial
  equivalent of the index argument.
- [22-04-04 Big-Data Patterns: Partitioning, Chunking, Out-of-Core](04-big-data-patterns.md) —
  what to do when the table no longer fits in the engine's memory.
- [22-04-05 Cloud-Native Geoscience Data Access](05-cloud-native-geoscience.md) —
  range requests as the object-store analogue of the access path.
- [22-03-01 Scientific File Formats](../03-data-formats-and-engineering/01-file-formats-scientific.md) —
  the columnar file formats that share the selectivity argument.

## Self-assessment checklist

- [ ] I can compute a table's page count and scan cost.
- [ ] I can choose between a scan and an index from the selectivity.
- [ ] I can compute a B-tree's depth and lookup cost.
- [ ] I can choose a join strategy and state which side to build on.
- [ ] I can design a schema that prevents duplicate and orphan rows.
- [ ] I can diagnose a slow query from its plan.
