---
id: 22-03-02
title: "Format Trade-Offs: Access Patterns, Compression, Portability"
level: research
prereqs: ["22-03-01", "22-02-05"]
estimated_minutes: 50
tags: [file-formats, chunking, compression, access-patterns, data-engineering]
---

# Format Trade-Offs: Access Patterns, Compression, Portability

## Learning objectives

By the end of this lesson you will be able to:

1. **Model** a read as bytes-plus-requests, and **compute** the bytes a query
   actually reads under a given layout.
2. **Measure** the read amplification of a windowed query against row-major,
   column-major and chunked layouts, and **explain** each factor.
3. **Choose** a chunk shape from the query shape and the storage's per-request cost,
   and **state** why the optimum moves with the backend.
4. **Measure** compression on your own data and **explain** why a ratio cannot be
   assumed from the format name.
5. **Match** a layout to a write pattern — replace versus append — and **compute** the
   storage consequences over a decade.
6. **Judge** a format on portability and state the one dependency that decides
   whether a reader can open the file in ten years.

Sizes, times and compression measurements are **SYNTHETIC**: the grid is generated
by the demonstration, the chunk and latency models use chosen constants, and the
compression ratios are measured with zlib on synthetic smooth and noisy arrays. No
real file store was queried and no library benchmark is quoted.

## Prerequisites

- [22-03-01 Scientific File Formats: CSV, Parquet, HDF5, netCDF, Zarr](./01-file-formats-scientific.md) —
  what the formats are, and what they must carry.
- [22-02-05 Data Versioning and Provenance Tracking](../02-reproducible-workflows/05-data-versioning.md) —
  why the layout interacts with deduplication and storage growth.

## 1. Intuition: a layout is a bet on access patterns

Filesystem and object-store interfaces hand over **bytes at an address**, not
"the window I asked for". Any layout therefore makes some queries cheap and others
expensive, and the layout is a bet about which queries will dominate. The bet is
usually implicit — it is made by the writer, who only ever ran the query that
motivated the format.

Two quantities decide the cost of a read:

$$\text{cost} \approx
\underbrace{\frac{B_{\text{read}}}{\text{bandwidth}}}_{\text{bytes}}
\;+\;
\underbrace{n_{\text{requests}} \times \text{latency}}_{\text{requests}} .$$

Both terms are under the writer's control, and they pull in opposite directions:
smaller chunks reduce bytes read but increase the number of requests.

## 2. The measured grid

The demonstration's **SYNTHETIC** grid is $1024 \times 1024$ float32 (4.2 MB) and
the query is a $256 \times 256$ window (262 kB), read at an arbitrary offset:

| Layout | Bytes read | Amplification |
|---|---|---|
| row-major scan | 1.05 MB | 4.00× |
| column-major scan | 1.05 MB | 4.00× |
| chunks $256 \times 256$ | 1.05 MB | 4.00× |
| chunks $128 \times 128$ | 0.59 MB | 2.25× |
| chunks $64 \times 64$ | 0.41 MB | 1.56× |
| chunks $32 \times 32$ | 0.33 MB | 1.27× |

Two facts deserve emphasis. First, the **unchunked** layouts read four times what
the query needs, and this is a *property of sequential storage*, not a defect of the
file: $256$ rows of $1024$ columns contain the $256 \times 256$ window. Second, the
amplification for a chunk of size $c$ against a window of size $w$ is approximately

$$\text{amplification} \approx \left(\frac{w + c}{w}\right)^{2},$$

which for $c = w$ gives $4$, for $c = w/2$ gives $2.25$, and for $c = w/4$ gives
$1.56$. The formula is the reason a chunk shape matched to the query is the single
most effective layout decision, and it also shows the diminishing return: going from
$c = 32$ to $c = 16$ would move the factor from $1.27$ to $1.14$ at four times the
chunk count.

## 3. Requests cost, and the optimum moves

Bytes are not the whole story. With the demonstration's chosen parameters —
200 MB/s bandwidth, 0.1 ms per request on a local disk, 20 ms per request on an
object store — the same four layouts cost:

| Chunk | Chunks read | Bytes read | Time, local disk | Time, object store |
|---|---|---|---|---|
| $256 \times 256$ | 4.0 | 1.05 MB | 5.6 ms | 85.2 ms |
| $128 \times 128$ | 9.0 | 0.59 MB | 3.8 ms | 182.9 ms |
| $64 \times 64$ | 25.0 | 0.41 MB | 4.5 ms | 502.0 ms |
| $32 \times 32$ | 81.0 | 0.33 MB | 9.8 ms | 1621.7 ms |

The optimum is **$128$** on the local disk and **$256$** on the object store: a
chunk shape is optimal *for a storage backend*, not in general. On the local disk
the byte term dominates and a chunk near the query size wins; on the object store
the request term dominates (81 requests × 20 ms is 1.6 s) and the largest chunk wins
despite reading three times the bytes. This is why a layout chosen on a laptop can
be disastrous on a cloud store, and why the rule "chunk to the query" must be
qualified by the per-request cost.

## 4. Compression: measured, not assumed

Compression reduces the first term of the cost model and adds a decompression cost,
and its return is a property of the **data**, not the format. The demonstration
compresses the raw float32 bytes of two arrays with the same algorithm:

| Data | Raw | Compressed | Ratio |
|---|---|---|---|
| smooth ramp (outer sum of two lines) | 262.1 kB | 3.4 kB | 76.29× |
| white noise | 262.1 kB | 242.9 kB | 1.08× |

The 70-fold difference between two arrays of identical shape and dtype is the
lesson: the ratio is set by how well each value can be predicted from its
neighbours and from the shared dynamic range. Three consequences:

1. **Measure, do not quote.** A ratio belongs in a methods section only with the
   data, the algorithm and its settings named, or with the measurement on the actual
   archive.
2. **Compression interacts with chunking.** Chunks are compressed independently, so
   a chunk smaller than the correlation length of the field loses compression
   efficiency; the same decision that reduces read amplification can reduce the
   compression ratio.
3. **Decompression is not free.** For a compute-bound pipeline the decompression
   cost can exceed the I/O saved; the demonstration's model does not include it and a
   real design must measure it.

## 5. Write patterns decide as much as reads

The layout must also be cheap to *update*. Two archetypes:

| Write pattern | Cheap layout | Cost |
|---|---|---|
| Replace a whole field (a reprocessed snapshot) | one file per snapshot, immutable | storage grows with snapshots |
| Append a slice (a sensor stream, a new day) | chunked array or a table partitioned by time | many small files or chunks to manage |

The demonstration's volumes make the stakes concrete:

- a daily $256 \times 256$ grid snapshot is **0.5 MB** per day, so ten years is
  **1.9 GB**;
- one day of 1 Hz samples at 8 bytes is **0.7 MB**, so ten years is **2.5 GB**.

Neither is alarming in isolation. The costs appear in the *number of objects*: ten
years of daily snapshots is 3650 files, and a ten-year hourly sensor archive is
87 600 files per station. A layout that produces millions of small objects makes
directory listings slow, backups fragile and object-store reads request-bound — the
same request cost that dominated §3. The remedy is to batch writes into chunks large
enough to amortise the request and to keep the append pattern (time) aligned with
the partitioning (time).

## 6. Portability: the test that matters in ten years

Portability has three layers, and they fail independently:

1. **The format specification** — is the container openly specified, or does it
   depend on one implementation? A binary layout defined only by a library is a
   dependency on that library's future.
2. **The library and its version** — can a reader today open a file written five
   years ago? This is the failure that archives actually experience: the file
   survives, the reader does not.
3. **The conventions** — units, coordinate reference systems, missing-value
   sentinels. These fail silently, which makes them worse than a missing library.

The practical test is a **five-year simulation**: hand the file to a colleague who
has only the written record — this lesson's metadata list — and ask them to recover
the values, the units and the coordinates. If the answer requires you to explain
something, that something is missing from the archive.

## 7. Practice: rules that hold across backends

1. **Write down the queries.** The layout is a bet; record which access patterns it
   was optimised for, so the next reader can see whether their query was covered.
2. **Chunk to the query, then correct for the backend.** Start with a chunk near the
   query size, then test the effect of per-request latency on the target store.
3. **Batch small writes.** One chunk per write, sized so that a typical write is a
   few MB, not a few kB.
4. **Measure compression on the archive.** Report the ratio only with the algorithm.
5. **Keep the metadata with the layout.** Chunk shapes, the compression codec and the
   fill value belong in the file's attributes or manifest, not in a README someone
   will lose.
6. **Prefer formats with independent readers.** Two independent implementations of a
   format is the strongest available evidence of portability.
7. **Verify with a round trip on a second machine.** The check that catches the
   silent failures is the one that uses a different environment
   ([22-03-01](01-file-formats-scientific.md) §6).

## 8. Worked example: choosing a layout for a regional model

A group serves a $4096 \times 4096$ velocity model to two consumers: an inversion
that reads $512 \times 512$ windows over the whole grid, and a web viewer that reads
a subsampled full field.

1. **Query shapes.** The inversion's window is $512$; the viewer reads everything, so
   its amplification is $1$ under any layout.
2. **Chunk choice.** From §2, a chunk of $512$ gives amplification
   $((512+512)/512)^2 = 4$; a chunk of $256$ gives $2.25$; the inversion is the
   dominant consumer, so chunk at $256$ or $512$ depending on the backend *after*
   measuring the request cost of §3.
3. **Backend correction.** On an object store, 9 requests of 256 kB is 180 ms of
   latency against 3 ms of transfer; on a local disk it is 1 ms of latency against
   3 ms of transfer. The same chunk yields opposite conclusions.
4. **Compression.** The velocity field is smooth, so expect a good ratio — measure
   it, because the viewer's subsampled read is now request-bound rather than
   byte-bound and the decompression cost is paid in full for each chunk read.

## Assumptions and regime of validity

1. **Sequential storage with a known chunk shape.** The model assumes reads fetch
   whole chunks; formats that support partial-chunk reads change the byte term.
2. **Chosen latency and bandwidth.** The 0.1 ms and 20 ms request costs bracket a
   local disk and an object store; real systems vary by an order of magnitude and
   must be measured.
3. **Independent, uniform query offsets.** Alignment can help or hurt: a window
   aligned to the chunk grid touches four chunks where a straddling window touches
   nine, so the amplification formula is a *typical* value, not a worst case.
4. **Compression measured with one codec at one level.** Other codecs and settings
   give different ratios, and the ordering of the two arrays is what generalises: the
   data's redundancy decides.
5. **No benchmark of a real system.** The times are model outputs; the conclusion to
   carry is that the optimum depends on the backend's request cost, which the model
   makes visible.

## The honest summary

A read costs bytes plus requests, and a layout decides both: a $256 \times 256$
window in a $1024 \times 1024$ grid is read with a $4.00\times$ amplification under
row-major, column-major or a $256$-chunk layout, and $2.25\times$, $1.56\times$ and
$1.27\times$ under chunks of $128$, $64$ and $32$. The best chunk is $128$ on a
local disk and $256$ on an object store under the demonstration's chosen request
costs, because the request term dominates the byte term as latency rises.
Compression must be measured: the same algorithm gives $76.29\times$ on a smooth ramp
and $1.08\times$ on noise. Write patterns matter equally — ten years of daily
$256 \times 256$ snapshots is only 1.9 GB but 3650 objects — and portability rests on
an openly specified container, an independent reader, and conventions that are
recorded rather than remembered.

## Python demonstration

[`code/format_design_tradeoffs_demo.py`](./code/format_design_tradeoffs_demo.py)
prints, with `np.random.default_rng(20261014)`:

1. bytes read and amplification for row-major, column-major and four chunk sizes;
2. the same layouts with a bytes-plus-requests time model for a local disk and an
   object store, showing the optimum moving;
3. zlib compression of the same shape and dtype on a smooth ramp ($76.29\times$) and
   on white noise ($1.08\times$);
4. the storage and object-count implications of snapshot and append patterns.

```bash
cd 22-data-engineering-reproducibility/03-data-formats-and-engineering/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python format_design_tradeoffs_demo.py
```

## Exercises

Graded problems and worked solutions are in
[`exercises/02-format-design-tradeoffs-exercises.md`](./exercises/02-format-design-tradeoffs-exercises.md)
and
[`exercises/02-format-design-tradeoffs-solutions.md`](./exercises/02-format-design-tradeoffs-solutions.md).

## Mastery checkpoint

Without notes: a $2048 \times 2048$ float32 grid is read mostly as $128 \times 128$
windows, on a store with a 15 ms per-request latency and 100 MB/s bandwidth.

1. Compute the amplification for chunk shapes of $256$, $128$ and $64$.
2. Compute the time for each, from the bytes-plus-requests model, and state which
   chunk wins.
3. State what changes if the same data are served from a local disk with 0.1 ms
   requests.
4. State the one thing about the data you would have to measure before assuming any
   compression ratio.

## Common pitfalls

1. **Chunking to the file, not to the query.** An unchunked layout costs the
   demonstration's $4.00\times$ amplification for every windowed read.
2. **Choosing a chunk shape on a laptop and serving it from a store.** The optimum
   moves from $128$ to $256$ as the request cost rises; the layout must be tested on
   the backend that will serve it.
3. **Quoting a compression ratio.** $76.29\times$ and $1.08\times$ come from the same
   code on the same shape and dtype.
4. **Ignoring the object count.** 1.9 GB in 3650 files is a request-bound workload in
   a shop that lists directories.
5. **Assuming chunk size and compression are independent.** Independently compressed
   chunks lose compression as they shrink below the field's correlation length.
6. **Testing portability by re-opening the file in the same environment.** The
   failures that matter appear with a different reader, version or machine.

## Where this is used

- **Cloud-native geoscience** — chunked arrays, range requests and the request/byte
  trade are the core of the access design:
  see [22-04-05 Cloud-Native Geoscience Data Access](../04-databases-and-large-data/05-cloud-native-geoscience.md).
- **Big-data patterns** — partitioning and out-of-core processing are the same
  arithmetic at a larger scale:
  see [22-04-04 Big-Data Patterns: Partitioning, Chunking, Out-of-Core](../04-databases-and-large-data/04-big-data-patterns.md).
- **Sensor archives** — append-aligned partitioning and the cost of many small
  objects: see
  [22-04-03 Time-Series Databases for Sensor Networks](../04-databases-and-large-data/03-timeseries-databases.md).
- **Workflow caching** — chunk-level storage and its effect on recomputation:
  see [22-02-03 Workflow Managers](../02-reproducible-workflows/03-workflow-managers.md) §6.

## Related lessons

- [22-03-01 Scientific File Formats: CSV, Parquet, HDF5, netCDF, Zarr](./01-file-formats-scientific.md) —
  the containers these layouts live in.
- [22-03-03 Designing Robust Data Pipelines for Earth Data](./03-data-pipelines.md) —
  the write patterns that produce these objects.
- [22-02-05 Data Versioning and Provenance Tracking](../02-reproducible-workflows/05-data-versioning.md) —
  deduplication, which depends on chunk granularity.
- [19-06 HPC and Parallel Computing](../../19-numerical-modeling-hpc/06-hpc-and-parallel-computing/README.md) —
  parallel I/O patterns for the same grids.

## Self-assessment checklist

- [ ] I can write a read's cost as bytes plus requests.
- [ ] I can compute the amplification of a window under a layout.
- [ ] I can choose a chunk shape for a backend's request cost.
- [ ] I can measure a compression ratio and report it properly.
- [ ] I can match a layout to a write pattern.
- [ ] I can state the three layers of portability and test them.
