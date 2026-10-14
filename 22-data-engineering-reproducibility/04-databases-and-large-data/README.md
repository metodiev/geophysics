# Module 22-04 — Databases and Large Data Collections

**Stages:** advanced → research · **Prerequisites:** module 22-03 (or equivalent
familiarity with formats, layouts and pipelines).

This module is about finding data at scale: how a database or an object store answers a
query, what that answer costs, and how to design storage so that the queries a project
actually makes are cheap. The organising idea is that **access is chosen from
statistics**, and every statistic is measurable. A relational engine picks a scan or an
index from a selectivity estimate; a spatial index produces candidates that a second
predicate must refine; a time-series store answers window queries from an aggregate tier
60× smaller than the raw data; a cloud-native layout trades requests against bytes, and
the optimal chunk moves when the store's latency does.

The second thread is that scale changes the failure modes rather than only the numbers.
A partition key holding 1.9 % of the rows becomes a task 22.9× the mean; 16 384 partitions
of 1 221 rows spend 99.98 % of their time in overhead; an out-of-core group-by moves twice
the data volume through storage as a shuffle. None of those is visible in a small test, and
each has a measurement that a reader can check before a job is run.

The third thread is the cost of a wrong assumption. A coordinate reference system mismatch
is wrong by the projection's scale factor with no error; a planar distance formula reaches
3 % error at 45° of separation; a raw sensor tier deleted to save 1.69 % of storage cannot
be reprocessed. The lessons pair each of those failures with the arithmetic that exposes it
and the practice that prevents it.

All measurements in this module are **SYNTHETIC** or **exact for a stated model**: tables,
point sets, sensor series, grids and raster layouts are described with chosen page sizes,
latencies and geometries, and the demonstrations compute the consequences. No database,
object store or real catalogue was queried, and no provider limit, price or benchmark is
quoted.

## Learning objectives

By the end of this module you will be able to:

1. Compute the cost of a scan, an index lookup and a join, and choose an access path from
   a selectivity estimate.
2. Design a spatial schema with a declared reference system, a two-stage predicate and a
   tile or tree index, and estimate its candidate ratio.
3. Size a sensor archive, measure its compression, and choose a retention policy from the
   cost of each tier.
4. Decide whether a computation is out-of-core, estimate its passes and its shuffle, and
   identify skew before it dominates the wall time.
5. Lay out data for an object store: chunk to the query, add an overview pyramid, bound
   the concurrency, and publish a manifest.
6. Diagnose the scale-specific failures — wrong plan, sparse index, hot key, request-bound
   read — from measurements rather than from guesswork.

## Prerequisites

- [22-04-01 Relational Databases and SQL for Earth Data](01-relational-databases.md) is the
  entry point; the later lessons assume its access-path vocabulary.
- [22-03-02 Format Trade-Offs: Access Patterns, Compression, Portability](../03-data-formats-and-engineering/02-format-design-tradeoffs.md) —
  chunking and the read cost model.
- [22-03-05 Automated Quality Control and Flagging](../03-data-formats-and-engineering/05-data-quality-control.md) —
  the flags that a time-series store must carry.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Relational Databases and SQL for Earth Data](01-relational-databases.md) | advanced | A scan streams 73 530 pages in 1.5 s; an index wins below ~3 % selectivity, and a 3-level B-tree makes a point lookup 2.40 ms |
| 02 | [Spatial Databases and PostGIS](02-spatial-databases.md) | research | An unindexed $1°$ box tests 200 000 points for 1 850 hits; a sorted join cuts 20 billion pairs to 11.36 million; planar distance errs by 3 % at 45° |
| 03 | [Time-Series Databases for Sensor Networks](03-timeseries-databases.md) | research | Second differences store a sensor series at 4.98× or 10.14×; aggregates cut queries 60× and cost 1.69 % of raw |
| 04 | [Big-Data Patterns: Partitioning, Chunking, Out-of-Core](04-big-data-patterns.md) | research | Passes are set by the statistic, not the volume; a hot key is 22.9× the mean; 16 384 partitions spend 99.98 % of their time starting |
| 05 | [Cloud-Native Geoscience Data Access](05-cloud-native-geoscience.md) | research | A 256 window in 2048 chunks fetches 256×; a five-level pyramid costs 1.33× and saves four per level; concurrency buys 16× |

## Suggested path

**If you are building a catalogue:** read 01 for the access paths, 02 for the spatial
predicates, and 06 of module 22-03 for the metadata. That is the minimum for a queryable
archive.

**If you are building a sensor archive:** read 03 in full, then 04 §2–5 for the
partitioning and skew of the processing that reads it.

**If you are moving data to the cloud:** read 05, then 03 §3 (aggregate tiers, the same
idea in time) and 02 §3 (the reference system questions that follow data everywhere).

**If you are here for the measurements:** every demo is self-contained and runs in well
under a second; use the ★★★ exercises, which ask you to design measurements on data you
choose.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-relational-databases.md`](01-relational-databases.md) | Lesson 01 |
| [`02-spatial-databases.md`](02-spatial-databases.md) | Lesson 02 |
| [`03-timeseries-databases.md`](03-timeseries-databases.md) | Lesson 03 |
| [`04-big-data-patterns.md`](04-big-data-patterns.md) | Lesson 04 |
| [`05-cloud-native-geoscience.md`](05-cloud-native-geoscience.md) | Lesson 05 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Five runnable demonstrations |

| Script | What it measures |
|---|---|
| [`code/relational_databases_demo.py`](code/relational_databases_demo.py) | Page and scan cost, scan-versus-index across selectivities, B-tree depth, join strategies |
| [`code/spatial_databases_demo.py`](code/spatial_databases_demo.py) | Unindexed box cost, tile candidates, spherical versus planar distance, join candidate reduction |
| [`code/timeseries_databases_demo.py`](code/timeseries_databases_demo.py) | Naive storage, second-difference compression on two series, downsampling ratios, retention volumes |
| [`code/big_data_patterns_demo.py`](code/big_data_patterns_demo.py) | Working set and passes, key skew, partition overhead, shuffle traffic |
| [`code/cloud_native_geoscience_demo.py`](code/cloud_native_geoscience_demo.py) | Window amplification, request and transfer costs, overview pyramid, concurrency speedup |

## How to run the demos

```bash
cd 22-data-engineering-reproducibility/04-databases-and-large-data/code

/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python relational_databases_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python spatial_databases_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python timeseries_databases_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python big_data_patterns_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python cloud_native_geoscience_demo.py
```

Every demo prints labelled results with units, seeds its random numbers with
`np.random.default_rng(20261014)`, uses no network access, writes no files and exits 0.
Each runs in well under a second.

## Mastery checkpoint

Complete this without notes, using the demonstrations only to check arithmetic:

> A group operates a 200-station network at 20 Hz, an event catalogue of 50 million rows,
> and a 20 TB tiled raster archive on an object store.
> **(a)** Their catalogue query for one station-year returns 4 000 rows of 50 million;
> state the access path and the reason. **(b)** Their station table has a hot station with
> 6 % of the events; compute the penalty in a partition-by-station job and name two
> mitigations. **(c)** Compute the raw storage per channel-year at 20 Hz with 8-byte values,
> and state the retention decision the arithmetic supports. **(d)** A viewer reads
> $256 \times 256$ windows from $2048^2$ chunks; compute the amplification and the change
> that removes it. **(e)** A distance query returns stations 2 700 km away for a "25 km"
> radius; state the likely cause and the test that would have caught it.
> **(f)** State the one measurement you would take before choosing a chunk size for a new
> cloud archive, and what it decides.

Worked versions of (a)–(f) appear in the lesson solutions at ★★ and ★★★ level.

## Common pitfalls across this module

1. **Trusting a plan without reading it.** Access paths are chosen from estimates; a stale
   statistic or a function-wrapped predicate changes the plan silently.
2. **Ignoring the reference system.** Distances and joins are wrong by a scale factor, with
   no error, whenever systems are mixed.
3. **Deleting the raw tier.** Aggregates cost 1.69 % of raw; the saving is small and the
   loss is permanent.
4. **Reaching for a cluster before measuring.** Volume and skew are separate problems, and
   a chunk loop on one machine solves the first for most datasets.
5. **Optimising bytes when requests dominate.** The optimum chunk size moves with the
   store's latency, so it must be measured on the target.
6. **Reporting an average where the tail decides.** A viewer's worst pan, a job's largest
   partition and a request's slowest range set the experience.

## Related modules

- [22-03 Data Formats and Engineering](../03-data-formats-and-engineering/README.md) —
  the representations and pipelines that feed these stores.
- [22-06 High-Performance and Cloud Computing for Research](../06-high-performance-and-cloud/README.md) —
  where the partitioned jobs run and what they cost.
- [21-02 Geostatistics](../../21-statistics-bayesian-ml/02-geostatistics/README.md) —
  the spatial statistics these stores serve.
- [03-09 Geospatial Python](../../03-scientific-computing/09-geospatial-python/README.md) —
  the library-level spatial tooling.
