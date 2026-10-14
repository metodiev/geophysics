# Solutions — 22-04-05 Cloud-Native Geoscience Data Access

> Read after attempting. Numbers are computed here and match the demonstration's printed
> output. Lesson:
> [05 Cloud-Native Geoscience Data Access](../05-cloud-native-geoscience.md).

---

## ★1 — Three operations and their consequences

1. **Get an object** — a whole object is the unit of retrieval, so any subset read
   requires the object to be *chunked* into many.
2. **Get a byte range** — ranges make partial reads possible, so the layout must place
   related data contiguously; this is what makes chunked arrays and columnar files
   efficient.
3. **List** — enumeration is a separate, slower operation with its own cost, so the object
   count should stay modest and the index should live in a small dedicated object rather
   than being discovered by listing.

## ★2 — Raster size and window amplification

(a) $16384 \times 16384 \times 2\ \text{B} = 536\,870\,912\ \text{B} =
536.87$ MB — the printed value.

(b) $1024 \times 1024 \times 2\ \text{B} = 2\,097\,152\ \text{B} = 2\,097$ kB.

(c) Chunk 512: the window straddles $3 \times 3 = 9$ chunks of $512^2 \times 2 =
524\,288$ B, so $9 \times 524\,288 = 4.72$ MB and the amplification is
$4.72/2.097 = 2.25\times$. Chunk 2048: the window lies inside $2 \times 2 = 4$ chunks of
$2048^2 \times 2 = 8\,388\,608$ B, so $4 \times 8.39 = 33.55$ MB and the amplification is
$16.00\times$. The difference is the ratio of the chunk side to the window side: whole
chunks must be fetched, so a chunk larger than the window 'over-fetches' by the square of
the size ratio.

## ★3 — Overviews

An **overview** is a precomputed, coarser version of the raster, usually at half the
resolution of the previous level, so that a display can read the level whose pixel size
matches the display's. Each level is four times smaller in bytes:

$$1 + \tfrac14 + \tfrac1{16} + \tfrac1{64} + \tfrac1{256} = 1.328,$$

so five overviews (levels 1–5) cost about **1.33×** the base level — the printed pyramid
falls from 536.87 MB to 0.52 MB, a factor of 1 034 across five levels (four per level,
$4^5 = 1024$).

## ★★4 — A 1024 window against 1024 chunks

(a) Chunks: 4 (the window lies inside a $2 \times 2$ block); amplification 4.00×;
bytes $4 \times 8\,388\,608 = 33.55$ MB... wait — for chunk 1024 the chunk size is
$1024^2 \times 2 = 2.097$ MB, and four chunks are 8.39 MB, giving the amplification
$8.39/2.097 = 4.00\times$ (the printed 4.00×, 8.39 MB, 4 chunks). Latency
$= 4 \times 30\ \text{ms} = 0.12$ s; transfer $= 8.39\ \text{MB}/100\ \text{MB/s} =
0.084$ s; total **0.20 s** serially.

(b) With 16 connections, four requests run in parallel (each still 30 ms), so the latency
term is one round trip: $0.03\ \text{s} + 0.084\ \text{s} \approx 0.11$ s. Since the
requests are independent and all four fit in the connection pool, the wall time is the
maximum of one request's latency plus the transfer, not the sum — the ceiling is the
bandwidth.

(c) The **latency** dominates in the serial case (0.12 s of 0.20 s). At 5 ms per request
the serial total becomes $0.02 + 0.084 = 0.104$ s and the transfer dominates; the optimum
chunk then moves smaller, because the request term has shrunk — which is exactly the point
of the lesson: the chunk size must be chosen for the store's latency, measured, not
assumed.

## ★★5 — A viewer reading 256 windows inside 2048 tiles

(a) Amplification $= (2048/256)^{2} = 64^{2} = 4096$: the client fetches
$2048^2 \times 2 = 8.39$ MB to display $256^2 \times 2 = 131$ kB. The lesson's table shows
the same effect at smaller chunk sizes: 256.00× for a 2048 chunk and a 256 window.

(b) Add an **overview pyramid**: at the display's resolution the client reads a level whose
pixel size matches the screen, turning the 8.39 MB read into roughly $131$ kB plus the
overview's own level (2 kB at level 5). The byte reduction is about 64× per viewed tile
level, and the storage cost is 1.33× the base level in total.

(c) Reduce the **request count** by fetching larger, contiguous ranges that cover the
whole visible window in one or a few requests (for example, read the bounding box's chunks
in one parallel batch, or store the visible region as a single higher-level tile), and by
caching tiles client-side so a pan re-reads only what is new.

## ★★6 — Twenty requests, four seconds, 120 MB per pan

(a) 120 MB for 20 requests is 6 MB per request: the tiles are being fetched whole at
$2048^2$ while the visible window is $256^2$, i.e. the amplification of ★★5(a) — about
4096× (the exact figure depends on the visible window's shape). The 4 s is consistent
with 20 serial requests at ~30 ms plus 120 MB of transfer under a slow connection, or with
a lower per-request latency and a congested link.

(b) The two confirming measurements: **bytes fetched per request** (from the client's own
logs or the store's access logs) and the **window-to-chunk size ratio** in the layout the
client reads. If the bytes per request are ~6 MB while the display needs ~131 kB, the
amplification is confirmed independently of any assumption about the network.

(c) The fix is a **pyramid**: read the overview level matching the display. The change
that would **not** fix it is a faster connection or more concurrency: the bytes are
4 000× what is displayed, so the waste scales with them, and concurrency only shortens the
latency term.

## ★★★7 — A 100 TB tiled raster archive

**Chunk size.** Choose from the dominant query. The training job reads random $512^2$
patches, so a chunk near $512^2$ (or a modest multiple, e.g. $1024^2$) keeps both the
amplification near 1–4× and the object count manageable: with $1024^2$ chunks a 100 TB
archive has about $100\ \text{TB} / (1024^2 \times 2\ \text{B}) \approx 48$ million chunks
— too many. Aggregating to $4096^2$ chunks (33.5 MB) gives about 3 million objects, still
a lot; the honest answer is to partition the archive into **many objects** (one per tile
of, say, $16\,384^2$), each internally chunked at $1024^2$, so the object count is in the
tens of thousands while the chunk geometry serves the patch reads.

**Pyramid.** Five overview levels per tile, at 1.33× storage, serving the viewer:
display resolution maps to a level, and each level is fetched from its own object.

**Object count.** Tens of thousands of tile objects plus overview objects — a count that
listing, backup and lifecycle operations can handle.

**Manifest.** Per tile: the object names, the chunk geometry, the coordinate transform and
reference system, checksums, the code and version that wrote them, the pyramid levels, and
**the query the layout was optimised for** (random $512^2$ patches and regional windows).

**The worst-served access pattern.** *Whole-archive scans* (for example training on the
entire dataset sequentially, or a global statistic): the chunking that serves local reads
adds object overhead to a scan, and the object count multiplies the request count. Serving
a sequential scan well requires a different layout (large sequential objects), which is
why an archive often keeps a second, coarser product for that purpose.

**What to measure.** For each of the three consumers: bytes fetched against bytes used per
query (amplification), request count per query, wall time at a stated concurrency, and the
object count. Report the amplification distribution — the median matters less than the
95th percentile, because a viewer's slow pans come from the tail.

## ★★★8 — Measuring effective bytes per request

**Statistic.** For a fixed logical window, issue the range requests the format requires
and record (i) the requested byte ranges, (ii) the **bytes transferred** as reported by the
client or the store, and (iii) the number of requests. The ratio of transferred bytes to
useful bytes is the effective amplification, and the ratio of useful bytes to requests is
the effective chunk efficiency. Run at both a small and a large window to expose the
size dependence.

**Two formats.** A **compressed chunked array** (where a chunk must be fetched whole and
decompressed, so the transferred bytes are the compressed chunk) against an
**uncompressed chunked array** (where a byte range inside a chunk can be requested, so the
transferred bytes can approach the useful bytes). The comparison shows whether the format
allows sub-chunk ranges to be exploited — often the decisive design question.

**Confounder.** Server-side and intermediary caching: repeated requests for the same range
can be served from a cache, so transferred bytes and latency fall for reasons unrelated to
the layout. Control it by requesting a cold range (a random offset not previously read),
by reporting warm and cold measurements separately, and by stating which one the conclusion
applies to.

**What it cannot tell you.** Anything about a query you have not issued: a different
window size, a different access pattern (sequential rather than random), or a query
touching many objects. The measurement characterises the store and the format at the tested
points; the layout's suitability for a *new* query must be estimated from the chunk
geometry.

## ★★★9 — Reducing a per-request bill

**Layout change.** Increase the chunk size **along the axis the queries span** so that a
query's bytes are covered by fewer requests: if the analysis reads, say, 200 chunks per
run, repacking the archive so the same data are covered by 20 larger objects or chunks
divides the request count by ten — at the cost of more bytes fetched per request, so the
change must be justified by the actual pattern (and measured, per ★★★8).

**Caching change.** Cache the chunks the analysis re-reads, in two places: a
**client-side cache** of the raw fetched ranges (keyed by object name and range), and, where
the analysis reads the same region repeatedly across runs, a **local materialised copy** of
that region so subsequent runs read nothing from the store. The second is the larger saving
and the more dangerous one (below).

**The measurement that shows the result is unchanged.** Re-run the analysis with the cache
enabled and compare the **outputs** — not the logs — bitwise or within the established
numerical tolerance, and record the bytes fetched in both runs. Both numbers are needed:
identical outputs with unchanged fetched bytes means the cache did nothing; identical
outputs with a much smaller byte count is the evidence the change was safe and effective.

**The risk the caching introduces.** A local copy is a **snapshot** of a remote object
that can change: if the archive is immutable, the copy is safe; if the provider reprocesses
or the archive is republished under the same name, the local copy silently diverges and
the analysis's results depend on when the cache was filled. Mitigate by keying the cache on
the object's **version identifier or checksum** rather than its name, and by invalidating
on a mismatch — the same lesson as
[22-03-04](../../03-data-formats-and-engineering/04-getting-earth-data.md) §5, applied to the
cache instead of the fetch.
