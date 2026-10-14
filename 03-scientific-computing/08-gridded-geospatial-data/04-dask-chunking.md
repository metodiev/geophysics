---
id: 03-08-04
title: "Chunking with Dask for Out-of-Core Analysis"
level: graduate
prereqs: ["03-08-03", "03-02-07"]
tags: [dask, chunking, out-of-core, lazy-evaluation, task-graph, reproducibility]
---

# Chunking with Dask for Out-of-Core Analysis

A 0.25° global climate product is about 720 × 721 × 1440 float32 values per
variable per decade: tens of gigabytes before you add a second variable. A
regional airborne magnetic survey at 25 m line spacing is larger still. Neither
fits comfortably in a laptop's memory, and both fit comfortably on its disk. The
technique that closes that gap is **chunked, lazy computation**: describe the
whole array, evaluate it one piece at a time.

> **Every number below is measured output from `code/dask_chunking_demo.py`.** The
> measurements are task counts and byte footprints, not wall-clock times, so they
> are reproducible on any machine. All fields are SYNTHETIC.

## Learning objectives

By the end of this lesson you will be able to:

1. **Explain** why a dask array is a graph of tasks rather than an array, and read
   `chunks`, `npartitions` and `chunksize` off an object.
2. **Predict** how the task count grows with the number of chunks for a reduction,
   and quote the measured counts.
3. **State** the two cases in which chunk size changes the numerical result: never
   for a deterministic array, always for dask's own random generator.
4. **Choose** a chunk layout from the reduction you intend to perform, and
   justify the choice with measured task counts.
5. **Explain** why operations that need neighbours (`diff`, `rolling`,
   `map_overlap`) cost more, and how the graph grows.
6. **Estimate** the peak memory of a chunked reduction and show that the full
   array is never materialised.
7. **Decide** between float64 and float32 for a chunk, with the precision
   consequence stated in bits and decimal digits.
8. **Name** the failure modes that chunking introduces: chunk-dependent
   randomness, many-small-tasks overhead, and rechunking cascades.

## Prerequisites

- [03-08-03 Dataset, Alignment, Broadcasting and GroupBy](./03-xarray-dataset.md)
  — the labelled container being chunked.
- [03-02-07 Memory Layout, Strides and Cache-Aware NumPy](../02-numpy/07-memory-performance.md)
  — cache lines, contiguity and why a tile of a big array is a natural I/O unit.

## 1. Intuition: describe the whole, evaluate in pieces

If you must compute the mean of a 512 MB array on a machine with 200 MB free, the
answer is not a cleverer algorithm for the mean. It is to never hold the array:

```python
big = (dsa.cos(dsa.deg2rad(lat))[:, None] ** 2
       + 0.25 * dsa.sin(dsa.deg2rad(lon))[None, :] ** 2)
```

Measured on that object:

```
shape = (8000, 8000), dtype = float64, nbytes = 512,000,000 bytes = 488.3 MiB
chunks = (1000, 1000), chunk footprint = 8,000,000 bytes = 7.6 MiB
ratio full array / chunk = 64x
tasks for mean/std/min/max together = 493
mean = 0.631236151715, std = 0.362423743259,
min = 0.000304624626, max = 1.249999935151
```

The array "exists" as 64 chunks of 7.6 MiB, plus 493 tasks that describe how to
combine them. The peak working set is one chunk plus its partial result, roughly
16 MB, not 488 MiB. For comparison: forming that array in NumPy needs 488 MiB for
the array and up to another 488 MiB for any temporary derived from it.

The word **graph** is literal. Here is the measured anatomy of a simpler case, a
2000 × 2000 float64 array (32,000,000 bytes) in 500 × 500 chunks:

```
npartitions = 16, chunk footprint = 2,000,000 bytes
tasks in the graph for the source array itself = 16
tasks for the sum of all cells = 37 (16 source chunks -> 15 partial sums -> 1 final accumulation)
computed sum = 1329.036007
```

$16 + 15 + 1 = 32$, but the graph has 37 nodes: the extra five are the
`zeros`-creation and reduction-shape tasks dask inserts. The arithmetic worth
remembering is the tree: $n$ chunks cost $n$ leaves and about $n-1$ partial
reductions, i.e. $O(n)$ tasks rather than $O(n)$ *bytes*.

## 2. Task count versus chunk size, measured

Chunking is a trade: fewer, larger chunks mean fewer tasks and more memory per
task; more, smaller chunks mean the reverse. Measured for the same
32,000,000-byte array:

| chunk | chunks | tasks for `sum()` | chunk footprint |
|---|---|---|---|
| 2000 | 1 | 3 | 32,000,000 B |
| 1000 | 4 | 9 | 8,000,000 B |
| 500 | 16 | 37 | 2,000,000 B |
| 250 | 64 | 149 | 500,000 B |
| 100 | 400 | 939 | 80,000 B |

The total data volume is constant in every row. The task count grows a little
faster than linearly in the number of chunks (400 chunks → 939 tasks, not 400),
because each reduction combines per-chunk partials in a tree and each chunk also
carries its own creation/slicing tasks. The practical reading: **going from 500 m
to 100 m chunks multiplies the scheduler's work by 25 while reducing the memory
footprint by 25.** Neither number is free, and the right answer depends on
whether you are limited by memory (choose small) or by scheduler overhead (choose
large).

A defensible default is a target chunk size in the 10–100 MB range:

| target | float64 cells | equivalent square |
|---|---|---|
| 10 MiB | 1,310,720 | 1144 × 1144 |
| 50 MiB | 6,553,600 | 2560 × 2560 |
| 100 MiB | 13,107,200 | 3620 × 3620 |

Those are *cells*, not a rule about grid spacing: a 10 MiB chunk of a 0.25°
climate field is a bigger geographic area than a 10 MiB chunk of a 25 m survey
grid, and the overhead measured above is per chunk, not per cell.

## 3. When chunking changes the answer

This is the part that matters most for reproducibility, and it has two halves.

### 3.1 Deterministic operations: chunk-invariant to machine precision

```
deterministic field: mean = 0.504985168125405 (dimensionless)
rechunked to (100, 100): mean = 0.504985168125405, difference = 1.110e-16
rechunked to (50, 50):  mean = 0.504985168125405, difference = 1.110e-16
rechunked to (400, 500): mean = 0.504985168125405, difference = 0.000e+00
```

Floating-point addition is not associative, so the *order* of the partial sums
differs between chunkings and a few units in the last place move. The measured
spread is 1.11 × 10⁻¹⁶ on a value near 0.5, i.e. a relative difference of
2 × 10⁻¹⁶ — one ulp. For scientific purposes this is exact. It is *not* exact in
the sense a bit-for-bit archive requires, so a reproducibility policy that
compares checksums must pin the chunk layout along with the version numbers.

### 3.2 Dask's random generator: chunk-*dependent* by design

```
chunks=(100, 100)   mean = -0.006204922187
chunks=(50, 50)     mean = -0.008087521525
chunks=(200, 200)   mean = -0.002474712521
max absolute difference between two chunkings = 6.0008
```

The values are **different numbers**, not the same numbers to 10⁻¹⁶. Dask's
`random` seeds each chunk from a mix of the global seed and the chunk index, so
that recomputing one chunk does not depend on the others. This is excellent for
parallel performance and fatal for reproducibility culture.

> **Rule.** Generate with NumPy under a fixed seed, then chunk. Never seed a dask
> generator and expect the array to be reproducible. The demonstration's own
> large field is built from *coordinates* (a cosine of latitude, a sine of
> longitude), which is chunk-invariant by construction.

## 4. Chunk layout must match the reduction

A climate cube has dims `(time, lat, lon)`. Two layouts, two costs, measured:

| chunks | partitions | max chunk | tasks for `polyfit("time")` |
|---|---|---|---|
| `{time: 1, lat: 60, lon: 80}` | 365 | 38,400 B | 1102 |
| `{time: 10, lat: 20, lon: 20}` | 444 | 32,000 B | 987 |
| `{time: 365, lat: 20, lon: 20}` | 12 | 1,168,000 B | 75 |

Each row stores the same 14,016,000 bytes. Chunking along time — one chunk per
pixel's whole series — cuts the task count for a per-pixel time regression by a
factor of 15 (1102 → 75). The reason is structural: a regression along time needs
each pixel's *complete* series in one place, so a layout that fragments time
forces dask to gather and shuffle, while a layout that fragments space does not.
The third row is 14.7× larger per chunk than the first and needs 14.7× fewer
tasks; the layout choice and the task count are the same decision.

**The rule:** chunk the dimension you reduce *over* as little as possible, and
chunk the dimensions you *iterate* over freely. If you will reduce along two
dimensions and iterate over a third, no single layout is optimal and one reduction
will pay a rechunk cost.

## 5. Neighbours cost extra: halos and the graph

```
source tasks = 16
c - c.mean() tasks = 53 (the scalar must be broadcast into every chunk)
dask.roll(c, 3, axis=1) tasks = 56
map_overlap(depth=2) tasks = 436
```

Three separate mechanisms, and it is worth separating them:

1. **Broadcast of a reduced scalar** (`c - c.mean()`) grows the graph from 16 to
   53 nodes. The reduction is added *before* the broadcast, so every chunk waits
   for the scalar.
2. **A shift or roll** needs each chunk to see a value from its neighbour, so the
   graph must carry the neighbour's index.
3. **`map_overlap`** is explicit halo exchange. With `depth=2`, each of the 16
   chunks must obtain a 2-cell border, so the graph acquires boundary, re-chunk,
   and trim steps: **436 tasks, 27× the source count.** Halos are the most
   expensive thing in a chunked pipeline, and they are unavoidable for any
   stencil, filter or finite difference.

The same effect on a 600-point series stored as six chunks of 100:

```
lazy .diff('t') tasks = 78
lazy .rolling(t=11).mean() tasks = 161, and rolling drops 5 samples at each end,
  i.e. 10 NaN in total
```

A first difference crosses chunk boundaries at 5 places; a centred 11-point
window crosses them with a halo of 5 on each side. **Boundary conditions and
NaN counts are chunk-shape dependent in implementation, not in definition** — the
definition of `rolling(t=11)` is the same at every chunk size, and the measured
10 NaN is what that definition implies.

### 5.1 The arithmetic of a halo

A stencil of radius $r$ (a 5-point difference has $r = 1$; a centred 11-point
window has $r = 5$) applied to an $N \times N$ array tiled into $c \times c$
chunks makes every task read $(c + 2r)^{2}$ cells to produce $c^{2}$ outputs. The
**read amplification** is therefore

$$\left(\frac{c + 2r}{c}\right)^{2} = \left(1 + \frac{2r}{c}\right)^{2}.$$

For $r = 2$ this is 3.2 % at $c = 250$ and 17.4 % at $c = 50$: small chunks pay
for their halos, large ones barely notice. The same ratio appears twice, once in
bytes read and once in the task count, which is why the demonstration's
`map_overlap(depth=2)` graph is 436 nodes for a 16-chunk source rather than 16.
The measured `rolling(t=11)` case has $r = 5$: with 100-point chunks the
amplification is $\left(1 + 10/100\right) = 1.10$ per axis, or 21 % more data read
than stored. **Halo cost is a ratio in $r/c$, so the remedy is always the same:
make chunks larger relative to the stencil radius.**

### 5.2 Lazy, computed, persisted

Three states, and the demonstration moves between them explicitly:

```
numpy-backed: type(da.data) = ndarray, nbytes = 9,216,000
.chunk({'time':60,'lat':30,'lon':40}): type = Array
npartitions = 16, chunk footprint = 576,000 bytes
tasks = 16
lazy mean: Array, tasks = 35
after .compute(): type = ndarray, mean = -0.005651 K
```

- `.chunk(...)` converts a NumPy-backed object into a lazy one; `nbytes` and
  `chunksize` are metadata, and no data is touched.
- `.compute()` evaluates and returns NumPy. Suitable for a small result.
- `.persist()` evaluates and *keeps the result in the cluster*, still as a dask
  collection, so that repeated downstream operations do not recompute shared
  ancestors. `persist` is the right call after an expensive selection, and the
  wrong call on the whole array — it is a promise you have the memory for.

## 6. dtype is a chunk-size parameter

```
float64 chunk footprint = 288,000 bytes
float32 chunk footprint = 144,000 bytes (0.14 MiB)
float32 relative precision 2^-24 = 5.960e-08, i.e. about 7 significant decimal digits
```

Halving the dtype halves every footprint, every halo and every shuffle volume,
for free — at a stated cost of about 7 significant decimal digits (float64
carries about 16). The judgement is domain-specific:

- **Temperature in kelvin:** values near 300 K, needing 0.01 K precision. float32
  resolution near 300 is 300 × 6 × 10⁻⁸ ≈ 1.8 × 10⁻⁵ K, i.e. ten thousand times
  better than needed. float32 is unambiguously correct.
- **Gravity at 0.001 mGal precision:** a 1000 mGal field needs a relative
  precision of 10⁻⁶. float32 gives 6 × 10⁻⁸ relative, i.e. 0.06 mGal on a 1000
  mGal field — **60 times too coarse.** float64 or packed int32 is required.

The rule is arithmetic, not taste: compute the required *relative* precision
$p$ and compare with $2^{-24} \approx 5.96 \times 10^{-8}$ for float32 and
$2^{-53} \approx 1.11 \times 10^{-16}$ for float64.

## 7. Units and dimensional analysis

Chunking introduces units of its own, and mixing them is the usual source of
nonsense in a configuration file:

- **bytes per chunk**: cells per chunk × bytes per cell. A `{time: 10, lat: 20,
  lon: 20}` chunk of float64 is $10 \times 20 \times 20 \times 8 = 32{,}000$ bytes
  — measured.
- **tasks per reduction**: $O(\text{chunks})$, dimensionless. Quote it as a count,
  never as a time.
- **chunk coordinates vs cell coordinates**: a chunk boundary is an index, a cell
  centre is a coordinate. Confusing them is exactly the error the halved-pixel
  convention guards against in the raster lessons, in another guise.
- **`nbytes` vs on-disk bytes**: `nbytes` is the uncompressed logical size; the
  file is smaller by the compression ratio. For the demonstration's 512 MB field
  the distinction is a factor of 1.2 to 4 depending on packing — see
  [01 netCDF/HDF5 Formats and Self-Describing Data](./01-netcdf-and-hdf5.md).

## 8. Python demonstration

The full script is
[`code/dask_chunking_demo.py`](./code/dask_chunking_demo.py):

```bash
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python \
    03-scientific-computing/08-gridded-geospatial-data/code/dask_chunking_demo.py
```

It is offline and seeded; the 512 MB field is built lazily from coordinate arrays
and is never materialised. Nothing is written to disk.

### What to observe, and why it matters

| Observation | Consequence |
|---|---|
| `nbytes` is known without computing | dask can size a problem before spending memory on it |
| 400 chunks → 939 tasks for a sum | per-chunk overhead is real and measurable |
| deterministic reduction is chunk-invariant to 1 ulp | chunking does not change science for smooth work |
| dask's `random` mean changes with chunking (−0.00620 vs −0.00809) | chunking can change reproducibility, silently |
| `{time: 365, ...}` needs 75 tasks; `{time: 1, ...}` needs 1102 | layout is chosen by the reduction, not by taste |
| `map_overlap(depth=2)` is 436 tasks from 16 | halos are the expensive part of stencils |
| the 512 MB field reduces with a 7.6 MiB chunk | out-of-core means peak memory ≈ chunk, not array |
| float32 halves every footprint at 7 digits | dtype is the cheapest optimisation available |

> **Breaking exercise.** Change the out-of-core field to
> `chunks=(4000, 4000)` and predict the chunk footprint before running. Then
> predict the number of tasks for `mean/std/min/max`, run it, and compare with the
> measured 493.

## 9. Common mistakes

1. **Seeding a dask random generator and expecting reproducibility.** Measured
   max absolute difference between chunkings: 6.0008.
2. **Calling `.compute()` too early.** Every premature compute materialises an
   array and discards the graph; the whole benefit is in delaying it.
3. **Chunking for the read pattern of yesterday.** See Section 4: the same cube
   costs 75 or 1102 tasks depending on which reduction you intend.
4. **Confusing laziness with cheapness.** A graph with a million tasks is lazy and
   slow; task counts are the measurement to watch.
5. **Ignoring the halo.** A rolling window of length $w$ needs a halo of
   $\lfloor w/2 \rfloor$; the graph cost is measured above.
6. **Assuming float32 is fine because "climate data are float32".** Section 6
   computes when it is not.
7. **Believing that chunked arithmetic is associative.** It is not; the difference
   is 1 ulp and becomes visible in a checksum.
8. **Rechunking in a loop.** Each `rechunk` is a full shuffle; put the layout
   decision at the start of the pipeline, where it costs one pass.

## 10. Real-world applications

- **CMIP6 / ERA5 archives.** Multi-terabyte NetCDF or Zarr stores opened as
  chunked datasets; the chunk layout in the file frequently *is* the chunk layout
  you should use.
- **Airborne and marine surveys.** Tens of gigabytes of line data gridded on
  disk; block-wise statistics (min, max, percentile) on a chunking that matches
  the traverses.
- **Seismic volumes.** A 3-D SEG-Y volume is a chunked array in all but name; its
  inline/crossline/time axis order decides whether a horizon extraction is cheap
  or ruinous.
- **Inversion and optimisation.** Iterative solvers over a chunked grid spend
  most of their graph on stencils; the halo cost in Section 5 is the reason
  domain decomposition exists as a separate discipline.
- **Serverless and cluster execution.** The task graph is what makes the same
  code run on one core or a hundred; it is also what makes the failure modes
  (serialisation, scheduling overhead, chunk-dependent randomness) portable.

## 11. Further reading

- **Dask, *Dask documentation*.** Level: intermediate. <https://docs.dask.org> —
  the array, chunking, `map_overlap` and best-practices pages.
- **Xarray, *Parallel computing with Dask*.** Level: intermediate.
  <https://docs.xarray.dev> — `.chunk()`, `.persist()`, and the interaction with
  the labelled data model.
- **Zarr, *Zarr documentation*.** Level: intermediate.
  <https://zarr.readthedocs.io> — chunked storage as a *format*, so that the
  on-disk chunking and the in-memory chunking can be the same decision.
- **Dask, *Chunking best practices*.** Level: intermediate. The source of the
  10–100 MB guidance; the measurements above are an independent check on it.
- **Rocklin, M. (2015). Dask: Parallel computation with blocked algorithms and
  task scheduling. *Proceedings of the 14th Python in Science Conference*.**
  Level: advanced. The design paper: blocked algorithms, task graphs, and why
  the graph is the interface.

> Note on citations: bibliographic details are given so you can locate these
> works. This repository does not host or reproduce copyrighted text.

## 12. Related lessons

- [03 Dataset, Alignment, Broadcasting and GroupBy](./03-xarray-dataset.md) —
  what is being chunked, and the reductions that decide layouts.
- [01 netCDF/HDF5 Formats and Self-Describing Data](./01-netcdf-and-hdf5.md) —
  on-disk chunking and compression, which the graph inherits.
- [05 Case Study: Analysing a Climate Data Cube](./05-climate-data-cube.md) —
  the analysis a chunked cube exists to support.
- [03-02-07 Memory Layout, Strides and Cache-Aware NumPy](../02-numpy/07-memory-performance.md)
  — why a tile is a better I/O unit than a slab.
- [03-04-07 Performance, dtypes and When to Leave Pandas](../04-pandas/07-performance-pandas.md)
  — the tabular version of "when the in-memory tool is the wrong tool".

## Exercises

[`exercises/04-dask-chunking-exercises.md`](./exercises/04-dask-chunking-exercises.md),
with full worked answers in
[`exercises/04-dask-chunking-solutions.md`](./exercises/04-dask-chunking-solutions.md).

## Self-assessment checklist

- [ ] I can explain what `npartitions`, `chunks` and `chunksize` mean for a given
      object.
- [ ] I can estimate the task count of a reduction from the number of chunks.
- [ ] I can state the one case in which chunk size changes the numerical result,
      and why.
- [ ] I can choose a chunk layout from a stated reduction and defend it with task
      counts.
- [ ] I can explain why `map_overlap` multiplies the graph.
- [ ] I can compute the peak memory of a chunked reduction and compare it with the
      full array.
- [ ] I can decide float32 versus float64 from a required relative precision.
- [ ] I can name three failure modes introduced by chunking and how to detect
      each.
