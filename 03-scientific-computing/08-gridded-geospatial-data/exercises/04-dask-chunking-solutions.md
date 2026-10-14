# Solutions — 03-08-04 Chunking with Dask for Out-of-Core Analysis

> **Read this after attempting the exercises, not before.** Every value attributed
> to "the demo" is its actual output. Nothing below is a wall-clock timing. All
> fields are SYNTHETIC.

---

## ★1 — Three words

- `chunks`: the tuple-of-tuples of chunk lengths along each axis, e.g.
  `((500, 500, 500, 500), (500, 500, 500, 500))`.
- `npartitions`: the number of chunks, the product of the per-axis chunk counts —
  16 in that example.
- `chunksize`: one tuple of representative chunk lengths, `(500, 500)`.

The footprint follows directly:

$$\text{chunk bytes} = \prod_i \text{chunksize}_i \times \text{itemsize}.$$

For 500 × 500 float64: $250{,}000 \times 8 = 2{,}000{,}000$ bytes — the demo's
measured value.

---

## ★2 — A 4000 × 4000 float64 array

**(a)** $4000 \times 4000 \times 8 = 128{,}000{,}000$ bytes (122.1 MiB).

**(b)** $4 \times 4 = 16$ chunks.

**(c)** $1000 \times 1000 \times 8 = 8{,}000{,}000$ bytes $= 7.63$ MiB. The full
array is 16× larger.

---

## ★3 — Why $O(n)$ tasks

Because each chunk is a separate task that must be *produced* (read, generated or
sliced) before it can contribute to the partial reduction, so the graph needs at
least one leaf node per chunk plus the nodes that combine the partials.

Measured scale: 400 chunks cost 939 tasks for a `sum()` on the demo's 2000 × 2000
array, i.e. a little over $2n$ — the extra factor being the tree of partial sums
and each chunk's own creation task.

---

## ★4 — Neighbours and halos

`diff` (a one-sided or central difference along a chunked axis) and
`rolling`/`map_overlap` (a windowed stencil) both need values from adjacent chunks.
The extra data a task must obtain is its **halo** (or **overlap**), of width equal
to the stencil's radius. Halos are why `map_overlap(depth=2)` on a 16-chunk source
produced **436** tasks.

---

## ★5 — Anatomy of a dask graph

**(a)** Measured:

```
shape = (2000, 2000), dtype = float64, nbytes = 32,000,000 bytes
chunks = (500, 500, 500, 500) along axis 0, (500, 500, 500, 500) along axis 1
npartitions = 16, chunk footprint = 2,000,000 bytes
tasks in the graph for the source array itself = 16
tasks for the sum of all cells = 37 (16 source chunks -> 15 partial sums -> 1 final accumulation)
computed sum = 1329.036007
```

**(b)** Measured task counts for `sum()`:

| chunk | chunks | tasks for `sum()` | chunk bytes |
|---|---|---|---|
| 2000 | 1 | 3 | 32,000,000 |
| 1000 | 4 | 9 | 8,000,000 |
| 500 | 16 | 37 | 2,000,000 |
| 250 | 64 | 149 | 500,000 |
| 100 | 400 | 939 | 80,000 |

**(c)** The data volume is constant at 32,000,000 bytes in every row, so the task
count is a pure function of the chunking. It grows slightly faster than linearly
in the chunk count: 400 chunks need 939 tasks, not 400, because each chunk carries
its own creation/slicing node and the reduction combines partials in a tree. The
practical reading: **going from 500 to 100 multiplies the scheduler's work by 25
while dividing the peak memory by 25.**

---

## ★6 — Chunk-invariant reductions

**(a)** Measured:

```
deterministic field: mean = 0.504985168125405 (dimensionless)
rechunked to (100, 100): mean = 0.504985168125405, difference = 1.110e-16
rechunked to (50, 50):   mean = 0.504985168125405, difference = 1.110e-16
rechunked to (400, 500): mean = 0.504985168125405, difference = 0.000e+00
```

**(b)** For a value near 0.5, one ulp of float64 is $2^{-53} \times 0.5 \approx
5.55 \times 10^{-17}$, so 1.11 × 10⁻¹⁶ is **2 ulp**. The reassociation of the sum
changed the answer in the last two bits and nothing else.

**(c)** A strict bit-for-bit policy would **not** survive a chunk change unless the
chunking is pinned, because 2 ulp is a different bit pattern. A policy expressed as
"agreement to 1 × 10⁻¹⁵ relative" would survive. The choice is a policy decision,
and the correct place to record it is beside the pinned dependency versions: **an
archive that claims bit-reproducibility must record the chunk layout.**

---

## ★7 — Chunk-dependent randomness

**(a)** Measured:

```
chunks=(100, 100)   mean = -0.006204922187, tasks = 4
chunks=(50, 50)     mean = -0.008087521525, tasks = 16
chunks=(200, 200)   mean = -0.002474712521, tasks = 1
max absolute difference between two chunkings = 6.0008
```

**(b)** **Generate with NumPy under a fixed seed, then chunk. Never seed a dask
random generator and expect a reproducible array.** A maximum difference of 6.0008
between two draw sets from the same nominal seed means the arrays are not the same
draw at all — they are two different draws that happen to share a seed.

---

## ★8 — Layout versus reduction

**(a)** Measured for a 480 × 36 × 72-equivalent cube of 14,016,000 bytes:

| chunks | npartitions | max chunk | tasks for `polyfit("time")` |
|---|---|---|---|
| `{time: 1, lat: 60, lon: 80}` | 365 | 38,400 B | 1102 |
| `{time: 10, lat: 20, lon: 20}` | 444 | 32,000 B | 987 |
| `{time: 365, lat: 20, lon: 20}` | 12 | 1,168,000 B | 75 |

**(b)** A regression along `time` for each pixel needs the pixel's **complete time
series in one place**. With `time: 1` no chunk holds more than one time step, so
every one of the 365 time-chunks must be gathered and reassembled for each spatial
tile: 365 × spatial tiles of shuffling. With `time: 365` each chunk holds a whole
series, so the fit is purely local and the graph is 15× smaller (1102 → 75).

---

## ★9 — Verifying the halo formula

Expected node counts from the formula are a *lower* bound on the graph size: the
formula counts the cells read, and the graph adds handling nodes. A complete answer
reports both.

For an array of $N \times N$ in $c \times c$ chunks with a halo of $r$:

$$\text{read amplification} = \left(\frac{c + 2r}{c}\right)^{2},$$

| $r$ | $c = 50$ | $c = 100$ | $c = 250$ |
|---|---|---|---|
| 1 | 1.082 | 1.041 | 1.016 |
| 2 | 1.174 | 1.082 | 1.032 |
| 5 | 1.440 | 1.210 | 1.082 |

Measured anchors from the demo: `map_overlap(depth=2)` on a 1000 × 1000 array in
250 × 250 chunks (16 chunks) produced **436** graph nodes, against 16 for the
source — a factor of **27.3**, far above the 1.032 the halo formula predicts for
the *bytes*. The conclusion to draw: **the formula describes the data movement,
and the graph overhead is a separate and usually larger multiplier for small
chunks.** For a pipeline that is scheduler-bound rather than bandwidth-bound, the
graph count is the number to watch; for one that is bandwidth-bound, the formula
is. Both should be reported, and neither should be called "the cost" on its own.

---

## ★10 — Chunk layouts for a 0.25° cube

Cube: 720 × 721 × 1440 float32 = 2,990,131,200 bytes ≈ 2.78 GiB; per-value 4 bytes.

| Query | Layout | Chunk footprint | Chunks | Chunks read |
|---|---|---|---|---|
| (a) pixel series | `(720, 8, 8)` | $720 \times 8 \times 8 \times 4 = 184{,}320$ B = 0.18 MiB | $1 \times 91 \times 180 = 16{,}380$ | **1** |
| (b) daily global map | `(1, 64, 96)` | 24,576 B = 0.023 MiB | $720 \times 12 \times 15 = 129{,}600$ | **180** |
| (c) per-pixel trend | `(720, 16, 16)` | 737,280 B = 0.70 MiB | $1 \times 46 \times 90 = 4{,}140$ | **1** |

A compromise, `(60, 32, 32)` (245,760 bytes, 12 × 23 × 45 = 12,420 chunks):

- (a) reads 12 chunks for the pixel series;
- (b) reads 23 × 45 = 1,035 chunks for a daily map;
- (c) reads 12 chunks per pixel block, all needing a final combine along time.

**Sacrifice (b)**, the daily global map. It is the query that reads every value in
the cube in any layout, so a dedicated pass over the data is needed regardless; the
layout should favour the reductions that are done most often, which are (a) and
(c). A pipeline that needs many daily maps should either write a second, map-ordered
copy of the cube or use a format whose chunking can be chosen per access pattern.

Also worth stating: 129,600 chunks of 24 KiB is *below* the 10–100 MiB guidance in
the lesson for a reason — the guidance optimises scheduler overhead, and this cube
would be read in a distributed setting where many small chunks parallelise well.
The correct answer names the environment.

---

## ★11 — Reproducibility rules for a chunked pipeline

A complete note contains:

1. **Deterministic reductions are chunk-invariant to a few ulp.** Measured: the
   same mean to 1.11 × 10⁻¹⁶ across three chunkings of a field built from
   coordinates. The mechanism is that float64 addition is not associative, so the
   order of partial sums changes; the effect is at the level of 2 ulp.
2. **Dask's random generator is chunk-*dependent*.** Measured: means of
   −0.00620, −0.00809 and −0.00247 for the same nominal seed at three chunkings,
   with a maximum absolute difference of 6.0008 between two of the arrays. The
   mechanism is deliberate: each chunk is seeded from the global seed and the
   chunk index so that recomputing one chunk does not depend on the others.
3. **What an archive must record.** The generator and its seed, the chunk layout,
   the dtype, the library versions, and whether the reduction is deterministic.
   Any of these alone is insufficient: the seed without the layout does not
   reproduce a dask random array, and the layout without the version does not
   reproduce a reduction whose implementation changed.
4. **A concrete failure.** A collaborator changes `chunks=(100,100)` to
   `chunks=(50,50)` in a preprocessing script. Every deterministic statistic is
   unchanged to 1 × 10⁻¹⁶, so their regression tests pass. A synthetic noise field
   generated inside the same script is a *different field*; the inversion's
   regularisation weight was tuned against the old noise, and the published
   uncertainty estimates shift by a few per cent with no code change and no failing
   test. The fix is the rule: **synthetic data are generated before chunking, and
   the chunk layout is an output of the preprocessing step, recorded in the
   provenance.**
