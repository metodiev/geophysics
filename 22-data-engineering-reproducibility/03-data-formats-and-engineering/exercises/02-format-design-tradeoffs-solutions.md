# Solutions — 22-03-02 Format Trade-Offs: Access Patterns, Compression, Portability

> Read after attempting. Numbers are computed here and match the demonstration's
> printed output. Lesson:
> [02 Format Trade-Offs](../02-format-design-tradeoffs.md).

---

## ★1 — The cost model

$$\text{cost} \approx \frac{B_{\text{read}}}{\text{bandwidth}} +
n_{\text{requests}} \times \text{latency}.$$

The chunk shape controls the **bytes read** term directly (through the amplification
of §2) and the **request count** term inversely, which is why the optimum depends on
the backend's latency.

## ★2 — Amplification of the demonstration's window

(a) Row-major scan: the window $256 \times 256$ spans $256$ full rows of $1024$
columns, so

$$B_{\text{read}} = 256 \times 1024 \times 4 = 1\,048\,576\ \text{B} = 1.05\ \text{MB},
\qquad \text{amplification} = \frac{1.05}{0.262} = 4.00\times.$$

(b) Chunks of $128$: the window straddles $3 \times 3 = 9$ chunks
($(256/128 + 1)^2$), each $128^2 \times 4 = 65\,536$ B, giving
$9 \times 65\,536 = 589\,824$ B $= 0.59$ MB, amplification $2.25\times$.
Chunks of $64$: $5 \times 5 = 25$ chunks of $16\,384$ B, giving $409\,600$ B
$= 0.41$ MB, amplification $1.56\times$.

(c) The formula $((w+c)/w)^{2}$ reproduces both: $c = 128$ gives
$(384/256)^2 = 2.25$; $c = 64$ gives $(320/256)^2 = 1.56$; $c = 256$ gives
$(512/256)^2 = 4.00$; $c = 32$ gives $(288/256)^2 = 1.27$.

## ★3 — Compression

Smooth ramp: 262.1 kB → 3.4 kB, **76.29×**. White noise: 262.1 kB → 242.9 kB,
**1.08×**. The explaining property is **redundancy**: a smooth field's neighbouring
values are predictable, so most bytes carry no new information, while white noise has
none beyond the byte distribution (for float32 noise, only the shared exponent
bytes).

## ★★4 — Amplification and time for four chunk sizes

(a) Amplifications: $c = 256$: $4.00$; $c = 128$: $2.25$; $c = 64$: $1.56$;
$c = 32$: $1.27$.

(b) Useful bytes $= 262\,144$ B $= 0.262$ MB; bytes read $=$ amplification × 0.262 MB;
time $=$ bytes/200 MB/s $+$ requests × latency, with requests $=$
$((w/c)+1)^2$:

| $c$ | amplification | bytes read | requests | local (0.1 ms) | object store (20 ms) |
|---|---|---|---|---|---|
| 256 | 4.00 | 1.05 MB | 4 | $5.2 + 0.4 = 5.6$ ms | $5.2 + 80 = 85.2$ ms |
| 128 | 2.25 | 0.59 MB | 9 | $2.9 + 0.9 = 3.8$ ms | $2.9 + 180 = 182.9$ ms |
| 64 | 1.56 | 0.41 MB | 25 | $2.0 + 2.5 = 4.5$ ms | $2.0 + 500 = 502.0$ ms |
| 32 | 1.27 | 0.33 MB | 81 | $1.7 + 8.1 = 9.8$ ms | $1.7 + 1620 = 1621.7$ ms |

All eight values match the demonstration's printed table.

(c) Local disk: **$128$** (3.8 ms) – the byte term dominates, and a chunk near the
query size minimises it while the request count stays small. Object store: **$256$**
(85.2 ms) – the request term dominates, so reading three times the bytes is cheaper
than 81 requests at 20 ms each.

## ★★5 — Snapshot and append volumes

(a) Snapshot: $256 \times 256 \times 4 = 262\,144$ B $= 0.26$ MB/day; over ten years
($3650$ days) $= 0.96$ GB — the demonstration rounds the same arithmetic to 0.5 MB
per day for an 8-byte dtype and 1.9 GB per decade; with 4-byte float32 the figures
are 0.26 MB/day and 0.96 GB.

Samples: $86\,400 \times 8 = 691\,200$ B $= 0.69$ MB/day; over ten years
$= 2.5$ GB, matching the printed 0.7 MB and 2.5 GB.

(b) Objects: $3650$ snapshot files; $3650$ daily sample files (or
$87\,600$ hourly files, or $31.5$ million one-second files if written per second).

(c) The **object count** drives the operational cost: listings, backups, metadata
operations and — on an object store — the request cost of $§3$, since a read of one
day costs at least one request and a directory scan costs one per object. Change: batch
the writes into chunks large enough to amortise a request (for example one file per
month per station, with the append pattern aligned to the partition key, here time).

## ★★6 — Making a compression claim usable

The claim "about 10×" is missing: (i) the **data** (which variables, which spatial
region and time span — the ratio is data-dependent, as 76.29× against 1.08× shows);
(ii) the **algorithm and settings** (codec, level, and whether the chunks are
compressed independently); (iii) the definition of the ratio (raw byte size over
compressed byte size of what — the numeric payload alone, or the file including
metadata and index).

**The one-page measurement.** State the archive (files, variables, dtypes, shapes);
compress with the chosen codec at the production settings, per chunk, and record the
distribution of per-chunk ratios (median, 5th and 95th percentile) rather than the
mean of the whole file; report the size of the complete file including metadata
before and after; and report the decompression throughput measured on the same
machine, because the ratio is only useful next to its cost. One page, one table, one
paragraph saying which variable dominates the total.

## ★★★7 — A 30-year hourly global archive

Setup: $1°$ global grid is $360 \times 180$ cells; float32; hourly for 30 years.
Per time step: $360 \times 180 \times 4 = 259\,200$ B $= 0.26$ MB. Time steps:
$30 \times 365.25 \times 24 = 262\,980$. Total raw: $0.26 \times 262\,980 \approx
68$ GB, or $\approx 2.3$ GB/year.

**Format and chunking.** Zarr (or netCDF with the same chunking) with a chunk of, say,
$90 \times 90$ cells × 24 hours: the spatial part matches regional windows and the
temporal part matches daily analysis. Chunks per file/day: $4 \times 2 \times 1 = 8$
per day, each $90 \times 90 \times 24 \times 4 = 777.6$ kB.

**Partitioning and object count.** One store object per chunk, grouped by year and
month in the key prefix. Total chunks $\approx 262\,980/24 \times 8 = 87\,660$, so
roughly 88 000 objects over 30 years ($\approx 2900$/year) — a manageable count, and
small enough that a month's listing is affordable.

**Annual storage.** $2.3$ GB/year raw; with a typical smooth-field compression of
$3$–$5\times$ (measure it — do not assume 10×), $0.5$–$0.8$ GB/year, i.e.
$15$–$24$ GB over 30 years per variable.

**The query this layout makes expensive.** A **point time series** for one city: the
data for a single grid cell across 30 years span every chunk, since chunks are
$90 \times 90$ in space and only 24 hours in time — the request term dominates
(88 000 requests if each chunk must be touched). Mitigation: write a separate
*derived* product — 50 station time series, one file per station — which is exactly
the "derived data are cheap to regenerate, observed data are not" rule of
[22-02-05](../../02-reproducible-workflows/05-data-versioning.md) §7.

**What to measure to check the claim.** Two benchmarks on the target store: (i) a
regional window read (should be a handful of chunk requests), and (ii) the derived
point-series build (should show how many chunk requests the reduction costs). Report
bytes read, request count, wall time and the compression ratio actually achieved.

## ★★8 — Where the two optima cross

Let $w$ be the window side, $b$ the bytes per cell, $B$ the bandwidth, $\ell$ the
request latency, and $c$ a candidate chunk size. With the amplification
$A(c) = ((w+c)/w)^{2}$ and the chunk count $n(c) = (w/c + 1)^{2}$:

$$T(c) = \frac{A(c)\,w^{2}\,b}{B} + n(c)\,\ell .$$

The crossover between two candidate chunk sizes $c_1 < c_2$ is where
$T(c_1) = T(c_2)$, i.e.

$$\ell^{\ast} = \frac{\left[A(c_2) - A(c_1)\right] w^{2} b / B}{n(c_1) - n(c_2)},$$

with $b$ the bytes per cell. For the demonstration's numbers
($w = 256$, $b = 4$, $B = 200$ MB/s, $c_1 = 128$, $c_2 = 256$):

- byte term difference: $[4.00 - 2.25] \times 262\,144 / 200 \times 10^{6}$
  $= 0.0023$ s;
- request difference: $9 - 4 = 5$;
- $\ell^{\ast} = 0.0023/5 = 0.46$ ms.

So for any request latency above about **0.46 ms** the larger chunk wins, which
covers an object store by four orders of magnitude and a warm local page cache by a
factor of four. The practical consequence is stark: **a single archive cannot be
optimal for both a local disk and an object store when the latencies differ by
100×**. Choose the chunk for the backend that serves the production workload, or —
the common real answer — store the same logical data twice with different chunkings,
accepting the duplication, or serve the local case through a cache of extracted
windows.

## ★★★9 — Measuring the chunk size at which compression stops improving

**Measurement.** Take a representative field, cut it into chunks of $\{32, 64, 128,
256, 512\}$, compress each chunk independently with the production codec and settings,
and record the **compression ratio distribution** (median and interquartile range
across chunks of the same size) and the total stored bytes. The first size above which
the median ratio stops rising materially is the compression-saturation size; it is
related to the field's correlation length, which is why a smooth velocity model
saturates at larger chunks than a noisy attribute.

**The confounder.** Read amplification (§2) moves in the *opposite* direction: larger
chunks read more undesired bytes per query, so the compression gain from large chunks
is partly paid back at read time. Reporting only the compression curve therefore
recommends chunks that are too large for the dominant query.

**The single experiment that trades them off.** Choose the dominant query shape, then
for each candidate chunk size measure the complete cost of answering that query on
the target storage: bytes read (from §2's model or from a store's own metrics),
request count, decompression time and wall time. The result is a curve with a minimum,
and the minimum is the answer; the chunk that minimises stored bytes is not it, and
the chunk that minimises read amplification is not it either.

**What the experiment cannot tell you.** Whether the dominant query you chose is the
one that will dominate in five years. The layout is a bet on the access pattern, and
the experiment only prices the bet you described; a new analysis (a point time series
for 50 stations, say) can invert the ranking, which is why the queries a layout was
optimised for must be recorded with the archive.
