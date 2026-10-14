# Solutions — 22-04-01 Relational Databases and SQL for Earth Data

> Read after attempting. Numbers are computed here and match the demonstration's
> printed output. Lesson:
> [01 Relational Databases and SQL for Earth Data](../01-relational-databases.md).

---

## ★1 — Pages and the scan

$$\text{rows per page} = \left\lfloor \frac{P}{b} \right\rfloor = \left\lfloor
\frac{8192}{120} \right\rfloor = 68,$$
$$N_{\text{pages}} = \left\lceil \frac{5\,000\,000}{68} \right\rceil = 73\,530,$$
$$T_{\text{scan}} = 73\,530 \times 0.02\ \text{ms} = 1471\ \text{ms} = 1.5\ \text{s}.$$

All three match the demonstration (68 rows/page, 73 530 pages, 1.5 s).

## ★2 — B-tree depth and lookup cost

$$d = \left\lceil \frac{\ln(5 \times 10^{6})}{\ln 200} \right\rceil =
\left\lceil \frac{15.425}{5.298} \right\rceil = 3.$$

A point lookup touches $d + 1 = 4$ pages: $4 \times 0.6\ \text{ms} = 2.40$ ms against
1.5 s for the scan (a factor of 625). The index is
$5 \times 10^{6} \times 8\ \text{B} = 0.04$ GB, which is
$8/120 = 6.7\ \% \approx 7\ \%$ of the table — small because an index entry is a key
and a pointer, not a row.

## ★3 — Cost and correctness

- **Cost**: the access path and the join strategy, chosen from statistics (§§3–5).
  Example: choosing an index over a scan for a $10^{-3}$-selective query.
- **Correctness**: the declarations that make a wrong state impossible (§6). Example:
  a primary key on `(station, channel, time)`, which turns a duplicate ingestion into a
  rejected write.

## ★★4 — A 250 000-row query

(a) Leaf pages: $250\,000/68 = 3677$; tree traversal: 4 pages (the three levels plus
the first leaf, which the traversal already reaches in the count above — take the
traversal as 3 index pages plus the leaf pages). Cost

$$\left(3 + 3677\right) \times 0.6\ \text{ms} = 3680 \times 0.6 = 2208\ \text{ms}
\approx 2.2\ \text{s}.$$

The scan is 1.5 s.

(b) Expect the **scan**: at 5 % selectivity the random leaf reads cost more than the
sequential stream. This is consistent with the demonstration's table, where 10 %
selectivity gives an index cost of 4.41 s against the scan's 1.5 s, and the crossover
lies near $1.7 \times 10^{5}$ rows (3.4 % of the table) — 250 000 rows is above it.

(c) If the rows are physically clustered by the index key, the leaf reads are
sequential rather than random: at 0.02 ms per page the same 3677 leaf pages cost 74 ms
plus the traversal, so the **index wins by a wide margin** even at 5 % selectivity.
Clustering is therefore as important as indexing, and it is decided by ingestion order.

## ★★5 — A 20-million-row table

(a) Rows per page $= \lfloor 8192/200 \rfloor = 40$; pages
$= \lceil 20\,000\,000/40 \rceil = 500\,000$; scan
$= 500\,000 \times 0.02\ \text{ms} = 10.0$ s.

(b) For 2 000 rows: leaf pages $= 2\,000/40 = 50$; cost
$= (3 + 50) \times 0.6 = 31.8$ ms — the **index** wins by a factor of 314. For 500 000
rows: leaf pages $= 12\,500$; cost $= (3 + 12\,500) \times 0.6 = 7502$ ms $= 7.5$ s —
the **scan** (10.0 s) versus the index (7.5 s) is close, and with any clustering the
index wins; with any cache benefit the scan wins. Call it a coin flip at this
selectivity (2.5 %).

(c) Crossover: the index's leaf cost equals the scan when
$(n_{\text{leaf}} + 3) \times 0.6\ \text{ms} = 10\,000\ \text{ms}$, i.e.
$n_{\text{leaf}} = 16\,664$ pages, or $666\,560$ rows — 3.3 % of the table. Consistent
with the demonstration's 3.4 % at a different table size, because the ratio of random
to sequential latency is the same.

## ★★6 — Ten times slower after a load

(a) The two most likely causes: (i) **stale statistics**, so the planner estimates the
selectivity wrongly and chooses a scan; (ii) **cache pressure**, where the table no
longer fits in the buffer pool and previously cached pages are now read from storage —
which raises the effective random latency of both paths, but hurts the index path more
because it is entirely random.

(b) First diagnostic: request the **plan** for the affected query and compare the
estimated row counts with the actual ones. A large discrepancy (say estimated 100 rows,
actual 500 000) is the signature of stale statistics; matching estimates with slow
execution point instead to the storage or the cache.

(c) Policy change: run an explicit statistics-gathering step after every bulk load, as
part of the pipeline rather than as an operator's habit, and monitor the divergence of
estimated from actual rows for the top queries. If the table's growth makes caching
impossible, the schema change is partitioning by time so that each query touches a
partition small enough to cache.

## ★★★7 — Schema for a 200-million-event catalogue

**Types.** `event_id` (a stable identifier, text or a 64-bit integer from the source);
`time` as `timestamp with time zone` (or a 64-bit epoch, with the epoch documented);
latitude and longitude as `double precision` in a declared geodetic datum (or a spatial
type, which brings its own index machinery — see
[22-04-02](../02-spatial-databases.md)); `depth_km` in
`numeric`/`double precision` with the sign convention documented; `magnitude` with its
*type* in a separate column (a magnitude without its scale is meaningless);
`station` as text.

**Keys and constraints.** Primary key on `event_id`; a unique key on
`(time, latitude, longitude)` if the source can produce duplicates; `check` constraints
on the ranges (latitude $-90$ to $90$, magnitude within the scale's range, depth
$\ge 0$); a foreign key from the station table for any per-station rows.

**Indices.** (i) a composite index on `(time, magnitude DESC)` for time-window queries
and largest-event queries; (ii) a spatial index for radius queries (a spatial column or
an R-tree-style index); (iii) the station table's primary key for the join. Note that
(iii) covers the join in §5's sense: 10 000 rows on the small side is trivial to build,
so a hash join on the station table is what the planner should choose.

**Partitioning.** Range-partition by year (or by decade for very large tables), with a
composite primary key including the partition key, so a time-window query prunes to one
or two partitions. Partition pruning is what keeps the index small enough to cache.

**The expensive query.** *Events within a radius of a point over the whole catalogue* if
the spatial index is poor or the radius is large: a radius covering 5 % of the globe
degenerates to a scan of the spatial index's leaf level. State it explicitly, and offer
a fallback: a precomputed tiling (a separate table of events per grid cell) for the
common radii.

**What to measure.** For each of the four query shapes: the plan (estimated versus
actual rows), logical and physical reads, wall time, and the number of partitions
touched. Report the measurement per query shape, not a single average.

## ★★★8 — Measuring effective random-page latency

**Statistic.** The **effective random read cost** of a workload: run a query whose plan
is known to be an index scan over a large fraction of the table, vary the number of leaf
pages touched, and regress wall time against pages touched. The slope is the effective
per-page cost (random); similarly, regress a scan's time against its page count for the
sequential cost. Report both slopes with their confidence intervals, and the ratio,
which is the quantity the crossover depends on.

**Confounder.** Cache warmth: a repeated experiment warms the buffer pool and the
storage cache, so the second measurement is faster than the first for reasons unrelated
to the design. Control it by (i) introducing a known cold state (a restart, or reading a
large unrelated dataset first), (ii) reporting warm and cold numbers separately, and
(iii) stating which one applies to the conclusion.

**Reporting a crossover a reader can check.** Give the two slopes, their ratio, the
formula for the crossover in pages and in rows, and the table state (row count, row
size, index column). A reader can then recompute the crossover for their own latency
ratio, which is the transferable part.

**What it cannot tell you.** Anything about a query you have not run: a query with a
different plan (a sort, a hash join, a nested loop), a different predicate shape, or
concurrency from other users. The measurement characterises the storage and the engine's
per-page costs, not the workload.

## ★★★9 — Denormalising the catalogue

**Performance case.** Removing the join removes the small-side build and the probe: for
a query returning 1 % of the rows, the join costs a small fraction of the query, but for
a query that returns *many* rows the join's per-row lookup (nested loop, 2.4 ms per row
from §2) dominates. If the workload is dominated by wide retrievals of a whole station's
events, denormalisation can be several times faster, and it also makes a single-table
scan possible.

**Three correctness costs.**

1. **Update anomalies**: a station's coordinates corrected in the station table do not
   propagate to the 200 million copied rows, so the catalogue silently contains two
   versions of the truth — a reproducibility failure, since a query's answer depends on
   when it ran.
2. **Storage and write amplification**: the station metadata is duplicated 200 million
   times, increasing the table (and every index over it) and making bulk loads slower.
3. **Loss of the vocabulary constraint**: a foreign key is what enforces that every
   event names a known station; with the metadata inline, an unknown or misspelled
   station becomes a valid row and the vocabulary of
   [22-03-06](../../03-data-formats-and-engineering/06-metadata-standards.md) is no longer
   enforced by the database.

**The measurement that decides.** Measure the two candidate schemas on the *actual*
workload mix: for the top 10 queries by total time, record wall time, logical reads and
the plan; then compute the workload-average gain against the cost of a metadata
correction (the time to update 200 million rows) and the storage delta. If the gain is
material and the metadata is known to be stable (station coordinates that never change —
rare in geodesy, where reference frames are updated), the denormalisation is defensible;
otherwise the honest alternative is a *materialised view* of the join, which the engine
can refresh, keeping one source of truth and the performance of a single table.
