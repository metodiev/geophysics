---
id: 22-04-05
title: "Cloud-Native Geoscience Data Access"
level: research
prereqs: ["22-04-04", "22-03-02"]
estimated_minutes: 50
tags: [cloud-native, object-store, range-requests, chunking, data-engineering]
---

# Cloud-Native Geoscience Data Access

## Learning objectives

By the end of this lesson you will be able to:

1. **Explain** how an object store differs from a filesystem, and **state** the two costs
   a read pays: bytes and requests.
2. **Compute** the bytes fetched for a windowed read from a chunked object, and **state**
   the amplification relative to the window.
3. **Choose** a chunk size from the window size and the request cost, and **justify** the
   choice with numbers.
4. **Measure** the benefit of an overview pyramid for a viewer, and **state** why
   subsampling a fine level is the wrong implementation.
5. **Estimate** the wall time of a read from the request count, the latency and the
   concurrency, and **state** the ceiling.
6. **Design** a cloud-native layout that is cheap to read, cheap to keep, and reproducible
   from a manifest.

The object sizes, request costs and query windows in this lesson are **SYNTHETIC** and
chosen for teaching. No object store was queried, no cloud service is described, and no
provider's limits or prices are quoted; those change and must be read from the provider's
documentation at the time of use.

## Prerequisites

- [22-04-04 Big-Data Patterns: Partitioning, Chunking, Out-of-Core](./04-big-data-patterns.md) —
  the chunking and partitioning arithmetic this lesson applies to remote storage.
- [22-03-02 Format Trade-Offs: Access Patterns, Compression, Portability](../03-data-formats-and-engineering/02-format-design-tradeoffs.md) —
  the same request-versus-bytes trade on local storage.

## 1. Intuition: an object store is an addressable byte range

Cloud object storage offers three operations that matter: **get an object**, **get a byte
range of an object**, and **list**. It has no directories, no partial writes, no file
handles and no rename. For scientific data the consequences are direct:

- **Layout is everything.** A monolithic object must be fetched whole, so any subset read
  requires the object to be *chunked* into many objects (a chunked array, a tiled image, a
  columnar file with row groups).
- **Requests are a resource.** Each range read has a latency and may be billed; a query
  that touches 10 000 small chunks pays 10 000 latencies, which is what makes the chunk
  size a cost decision and not only a byte decision.
- **Immutability is a gift.** Objects cannot be edited in place, so a versioned,
  content-addressed layout is natural — the practice of
  [22-02-05](../02-reproducible-workflows/05-data-versioning.md) fits the medium.

## 2. Windowed reads from a chunked object

The demonstration's **SYNTHETIC** raster is $16384 \times 16384$ uint16 — **536.87 MB** —
and the queries are square windows:

| Window | Needs | Chunk 512 | Chunk 1024 | Chunk 2048 |
|---|---|---|---|---|
| $256 \times 256$ | 131 kB | 4 chunks, 2.10 MB, **16.00×** | 4 chunks, 8.39 MB, **64.00×** | 4 chunks, 33.55 MB, **256.00×** |
| $1024 \times 1024$ | 2 097 kB | 9 chunks, 4.72 MB, **2.25×** | 4 chunks, 8.39 MB, **4.00×** | 4 chunks, 33.55 MB, **16.00×** |

Two lessons are visible. First, **amplification is the ratio of the chunk size to the
window size, squared**: a $256$ window inside a $2048$ chunk reads 256 times what it
needs, because whole chunks must be fetched. Second, the *number of chunks* behaves in
the opposite direction: 9 chunks of 512 against 4 chunks of 2048. The optimum depends on
which term dominates, exactly as in
[22-03-02](../03-data-formats-and-engineering/02-format-design-tradeoffs.md) §3 — and on an
object store the request term usually does.

At the demonstration's 30 ms per request and 100 MB/s per connection:

| Chunk | Requests | Latency | Transfer | Total |
|---|---|---|---|---|
| 512 | 9 | 0.27 s | 0.047 s | 0.32 s |
| 1024 | 4 | 0.12 s | 0.084 s | 0.20 s |
| 2048 | 4 | 0.12 s | 0.336 s | 0.46 s |

The middle chunk wins for a $1024$ window: the small chunk pays nine latencies, the large
one pays 33 MB of transfer. A designer who chunks "as small as possible" optimises the
wrong term by a factor of four.

## 3. Overviews: reading less, not sampling more

A viewer that displays a whole $16384 \times 16384$ raster needs at most a few thousand
pixels. Fetching the fine level and subsampling transfers the full object; reading a
**coarse overview** transfers what is displayed:

| Level | Resolution | Full-extent bytes |
|---|---|---|
| 0 | 16 384 px | 536.87 MB |
| 1 | 8 192 px | 134.22 MB |
| 2 | 4 096 px | 33.55 MB |
| 3 | 2 048 px | 8.39 MB |
| 4 | 1 024 px | 2.10 MB |
| 5 | 512 px | 0.52 MB |

Each level is a **factor of four** smaller (half the side, both dimensions), so a pyramid
of five overviews costs 1.33× the base level in storage and turns a 537 MB read into a
0.52 MB one for the zoomed-out view. This is the same argument as the aggregate tiers of
[22-04-03](03-timeseries-databases.md) §3, applied to a spatial axis: the overview is
derived data, cheap to keep and safe to rebuild, and it is what makes an interactive
viewer possible on an object store.

## 4. Concurrency: converting latency into throughput

Serial reads of many chunks pay the latency once per chunk. Concurrency overlaps them:

| Requests | Serial | At 16 connections | Speedup |
|---|---|---|---|
| 16 | 0.48 s | 0.03 s | 16.0× |
| 64 | 1.92 s | 0.12 s | 16.0× |
| 256 | 7.68 s | 0.48 s | 16.0× |
| 1 024 | 30.72 s | 1.92 s | 16.0× |

The speedup is the connection count until the bandwidth ceiling is reached, and the
practical ceiling is

$$R_{\max} \approx n_{\text{connections}} \times B_{\text{connection}},$$

plus the client's own CPU for reassembly. Two consequences: a parallel reader is
mandatory for any window that spans many chunks, and beyond the bandwidth ceiling more
connections only increase cost and contention — the same conclusion as the worker-count
arithmetic of
[22-02-03](../02-reproducible-workflows/03-workflow-managers.md) §5.

## 5. Designing the layout

1. **Chunk to the dominant query, then test the request cost.** Start with a chunk near
   the window size; then measure on the target store, because the optimum moves with the
   per-request latency (§2).
2. **Put the metadata in a small leading object.** A store lacks a filesystem, so the
   index, the chunk table, the coordinate arrays and the provenance belong in a compact
   object that is fetched once — not scattered through the data chunks.
3. **Keep the object count sane.** A million small objects makes listing, backup and every
   lifecycle operation expensive; aggregate tiny chunks into larger ones when the queries
   allow it.
4. **Use a pyramid for the viewer and the fine level for the analysis.** Decide which
   consumer each level serves and record it.
5. **Write once, name by content.** Immutability plus content addressing gives a
   versioned, deduplicable archive
   ([22-02-05](../02-reproducible-workflows/05-data-versioning.md)).
6. **Fetch in parallel with a bounded concurrency**, and back off on throttling — a
   runaway retry loop against a store is both slow and antisocial.
7. **Record the manifest**: object names, chunk geometry, checksums, the code that wrote
   them, and the query that the layout was optimised for. Without the last item, a reader
   cannot tell whether their query was the one the layout served.

## 6. Worked example: an interactive map that costs too much

A team serves a 500 GB tiled raster from an object store, and each pan of the map costs
1.20 in request charges and takes 4 s.

1. **Compute the requests.** If each tile read is a separate request, a screen showing
   20 tiles is 20 requests; at 30 ms and a small transfer that is under a second of
   latency — so 4 s means the client is reading far more than 20 chunks, or the tiles are
   large.
2. **Check the amplification.** If the tiles are $2048^2$ but the visible window is
   $256^2$, the amplification is $256\times$: the client fetches 33 MB to display 131 kB.
   The fix is a pyramid, not a faster connection.
3. **Check the request pattern.** A viewer that re-reads the same tiles on every pan
   should cache them client-side; without caching, scrolling a map multiplies both bytes
   and requests.
4. **Check the concurrency.** Serial reads of 20 chunks pay 20 latencies; a bounded
   parallel reader with 8–16 connections reduces the wall time by an order of magnitude.
5. **The arithmetic to report.** Bytes fetched per view, requests per view, wall time, and
   the amplification against the displayed data — the four numbers that make the cost
   explainable.

## Assumptions and regime of validity

1. **Chosen request latency and bandwidth.** Real stores and networks differ by an order
   of magnitude; the optimum and the wall-time estimate move with them, which is why they
   must be measured on the target.
2. **Whole-chunk reads.** The model assumes a chunk must be fetched entirely, which is
   typical for compressed chunks; ranges *within* an uncompressed chunk are cheaper, and
   some formats exploit that.
3. **Independently compressed chunks.** Compression reduces the bytes term but weakens
   within-chunk prediction; both effects must be measured together
   ([22-03-02](../03-data-formats-and-engineering/02-format-design-tradeoffs.md) §4).
4. **A single client.** The estimates are per-client; aggregate behaviour under many
   concurrent clients is a capacity question this lesson does not model.
5. **No provider specifics.** Prices, limits, consistency guarantees and lifecycle
   policies vary by provider and change over time; none is quoted here, and the design
   rules are stated in terms of requests and bytes so that a reader can apply them to
   whichever store they use.

## The honest summary

An object store is a set of addressable byte ranges, so a cloud-native layout is a
chunking decision with two measurable costs: bytes and requests. A $256 \times 256$ window
inside $2048$ chunks fetches $256\times$ what it needs (256.00× amplification), while a
$1024$ window inside $512$ chunks fetches $2.25\times$ over nine requests — and at 30 ms
per request the middle chunk (1024) is the fastest for a $1024$ window at 0.20 s, beating
both the smaller and the larger layouts. A five-level overview pyramid costs 1.33× the
base level and turns a 537 MB read into 0.52 MB for a zoomed-out view, and concurrency
converts latency into throughput at a rate equal to the connection count until the
bandwidth ceiling is reached. The design rules that follow — chunk to the dominant query,
keep the metadata in a small leading object, keep the object count sane, publish a
manifest — are what make an archive an instrument rather than a bucket.

## Python demonstration

[`code/cloud_native_geoscience_demo.py`](./code/cloud_native_geoscience_demo.py) prints,
with `np.random.default_rng(20261014)`:

1. the amplification table for two windows against three chunk sizes (from 2.25× to
   256.00×);
2. the request count, latency, transfer and total time for each chunk size;
3. the overview pyramid from 536.87 MB to 0.52 MB;
4. the concurrency table showing a 16× speedup from 16 connections.

```bash
cd 22-data-engineering-reproducibility/04-databases-and-large-data/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python cloud_native_geoscience_demo.py
```

## Exercises

Graded problems and worked solutions are in
[`exercises/05-cloud-native-geoscience-exercises.md`](./exercises/05-cloud-native-geoscience-exercises.md)
and
[`exercises/05-cloud-native-geoscience-solutions.md`](./exercises/05-cloud-native-geoscience-solutions.md).

## Mastery checkpoint

Without notes: a $8192 \times 8192$ uint16 raster is stored in a chunked object with
$1024^2$ chunks, and a client reads $2048^2$ windows from a store with 25 ms per request
and 80 MB/s per connection.

1. Compute the number of chunks the window touches and the amplification.
2. Compute the latency, transfer and total time serially, and with 8 connections.
3. State the change that would reduce the bytes, and the change that would reduce the
   time if the request count is the problem.
4. State the three items a manifest must record for a reader to reproduce the layout.

## Common pitfalls

1. **Treating an object store as a filesystem.** No partial writes, no rename, and a
   monolithic object cannot be read in part.
2. **Chunking smaller than the query.** It multiplies requests: 9 requests of 512 against
   4 of 1024 for the same window.
3. **Chunking far larger than the query.** 256× amplification for a $256$ window in
   $2048$ chunks.
4. **Subsampling the fine level for a viewer.** A pyramid costs 1.33× storage and saves a
   factor of four per level.
5. **Reading serially.** Concurrency is the difference between 30.72 s and 1.92 s for
   1 024 requests.
6. **No manifest.** Without the chunk geometry and the optimised query, a reader cannot
   tell whether the layout suits them.

## Where this is used

- **Cloud-hosted gridded products** — the standard tiled layout with overviews, read by
  range requests.
- **Federated analysis on large archives** — analysis next to the data, with the client
  fetching windows rather than files.
- **Interactive viewers** — where the pyramid decides whether a pan costs milliseconds or
  megabytes.
- **Cost control** — the requests and bytes per view are the two numbers that appear on a
  bill, and both are layout decisions.

## Related lessons

- [22-03-02 Format Trade-Offs: Access Patterns, Compression, Portability](../03-data-formats-and-engineering/02-format-design-tradeoffs.md) —
  the local-storage version of the same arithmetic.
- [22-04-04 Big-Data Patterns: Partitioning, Chunking, Out-of-Core](./04-big-data-patterns.md) —
  the processing side of a chunked store.
- [22-04-03 Time-Series Databases for Sensor Networks](./03-timeseries-databases.md) —
  the aggregate tiers that play the overview role in time.
- [22-01-05 Licensing, Citation and Software Credit](../01-research-software-engineering/05-licensing-and-citation.md) —
  what distributing a derived archive implies.

## Self-assessment checklist

- [ ] I can explain the three object-store operations and their consequences.
- [ ] I can compute the amplification of a windowed read.
- [ ] I can choose a chunk size from the window and the request cost.
- [ ] I can compute the benefit of an overview pyramid.
- [ ] I can estimate a read's wall time from latency and concurrency.
- [ ] I can list what a layout manifest must record.
