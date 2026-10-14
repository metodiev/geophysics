# Solutions — 03-08-01 netCDF/HDF5 Formats and Self-Describing Data

> **Read this after attempting the exercises, not before.** Every value attributed
> to "the demo" is its actual output. All data are SYNTHETIC; no number below is
> an observation of the Earth.

---

## ★1 — The data model

1. **Dimension** — a named axis length, e.g. `lat = 121`.
2. **Variable** — a named array naming its dimensions, e.g.
   `anomaly(time, lat, lon)` with `units = "mGal"`.
3. **Coordinate variable** — a variable whose name equals its only dimension,
   e.g. `lon(lon)` with `units = "degrees_east"`. This is the mechanism that makes
   an index into a physical coordinate.
4. **Attribute** — a named metadata value on a variable or on the file, e.g.
   `standard_name = "gravity_anomaly"` on the variable and
   `Conventions = "CF-1.11"` globally.

The demo's header confirms the structure:

```
dims: {'time': 24, 'lat': 121, 'lon': 161}
var lon      float64 dims=('lon',) attrs=['axis', 'standard_name', 'units']
var time     float64 dims=('time',) attrs=['axis', 'calendar', 'units']
var anomaly  float64 dims=('time', 'lat', 'lon') attrs=['coordinates', 'long_name', 'standard_name', 'units']
global attrs: ['Conventions', 'institution', 'title']
```

---

## ★2 — Packing arithmetic

**(a)** `scale_factor` has units `[value]/[code]` = mGal per count; `add_offset`
has units of the value, mGal. Multiplying a dimensionless code by mGal/count gives
mGal, and adding mGal gives mGal.

**(b)** $\text{value} = 0.02 \times 1234 + (-80.0) = 24.68 - 80.0 = -55.32$ mGal.

**(c)** One count is 0.02 mGal, so the smallest representable difference is
**0.02 mGal**; the maximum rounding error is half of that, **0.01 mGal**.

---

## ★3 — File size

$400 \times 300 \times 12 = 1{,}440{,}000$ values × 2 bytes =
**2,880,000 bytes** = **2,812.5 KiB** = **2.747 MiB**. Header and attribute text
add a few kilobytes; the demo's own overhead for a similar grid was 12,566 bytes
on 3,740,352 bytes of payload, i.e. 0.33 %.

---

## ★4 — Representation versus science

| Attribute | About |
|---|---|
| `units` | science (the quantity) |
| `scale_factor` | representation |
| `add_offset` | representation |
| `standard_name` | science (which quantity) |
| `_FillValue` | representation |
| `Conventions` | neither — a claim about which document the file follows |

The interesting case is `units`: it describes the physical quantity, but it is
stored as unvalidated text, so it can disagree with `scale_factor`'s implicit
units and no reader will notice.

---

## ★5 — Quantisation error

**(a)** Measured:

```
half a count = 0.0050 mGal; ideal rms error for uniform rounding = 0.00289 mGal
measured  rms error = 0.00289 mGal
measured  max error = 0.00500 mGal
```

**(b)** $s/\sqrt{12} = 0.01/3.4641 = 0.002887$; $s/2 = 0.005$. The measured values
are 0.00289 and 0.00500.

**(c)** The theoretical value assumes the rounding error is **uniformly
distributed on $[-s/2, s/2]$**. That holds when the values to be rounded are dense
relative to $s$ and not themselves quantised — which is why the agreement to three
significant figures is a *check on the data*, not a coincidence.

**(d)** Defensible here: the anomaly field is a smooth Gaussian plus a linear
trend plus a Gaussian perturbation of standard deviation 0.05 mGal, so the values
are essentially continuous at the 0.01 mGal scale. If the field had been
*synthesised on a 0.01 mGal grid in the first place*, the rounding errors would be
correlated with the values and the rms would be smaller than $s/\sqrt{12}$. The
test is: are there many values per quantisation step? Here $32.69\ \text{mGal} /
0.01 = 3269$ steps over 467,544 values — 143 values per step, so yes.

---

## ★6 — Double packing

**(a)** Measured:

```
max error = 350.18 mGal
stored codes occupied -32764 .. 32744 instead of -2432 .. 837
codes outside the correct range = 441,089 (94.3 % of the grid)
```

**(b)** $350.18 / 0.005 = 70{,}036$ — the error is **70,000× the rounding budget**.

**(c)** Store codes with automatic scaling disabled:

```python
var.set_auto_scale(False)          # netCDF4-python
```

or, better, write physical values and let the library pack them once. The
underlying cause is that a library honouring `scale_factor` packs on *write* as
well as unpacking on *read*, so codes passed through it are transformed twice.

---

## ★7 — Compression

**(a)** Measured:

| Setting | Bytes | Ratio |
|---|---|---|
| none | 3,752,918 | 1.00× |
| zlib level 1 | 3,118,732 | 1.20× |
| zlib level 6 | 3,091,146 | 1.21× |
| chunked 6 × 40 × 60, zlib 4 | 3,187,955 | 1.18× |

**(b)** Deflate wins only 20 % because the field is a smooth Gaussian plus
*seeded Gaussian noise of standard deviation 0.05 mGal* stored at float64
precision. The noise dominates the low-order bits of the mantissa, so 8 bytes per
value carry about 2 bytes of entropy. Compression exploits *redundancy*, and this
array has little at the byte level.

**(c)** **Pack to int16.** Measured: 949,864 bytes instead of 3,752,918, a 3.95×
reduction. The cost is 0.00289 mGal rms of quantisation error, which is 0.009 % of
the field's 32.69 mGal range — acceptable if the instrument's own precision is
0.01 mGal and unacceptable if the survey is a 0.001 mGal gradiometry survey. The
second-best change is `float32`, which halves the size and costs ~7 significant
digits; the demo measures a float32 round-trip error of
$4.761 \times 10^{-7}$ mGal, which is *below* the packing error, so if precision is
the constraint, packing is still the better trade.

---

## ★8 — Hyperslab reads

**(a)** `slab.shape = (121, 161)` = **19,481 values**, which is **4.17 %** of
467,544. Measured mean 0.3640 mGal, standard deviation 2.7904 mGal.

**(b)** Chunk shape `(6, 40, 60)`. Along time the variable has 24 slices, so one
time index falls in chunk 0 only ⇒ **1 chunk in the time direction**. Along lat,
121 rows in 40-row chunks ⇒ 4 chunks (0–39, 40–79, 80–119, 120). Along lon, 161
columns in 60-column chunks ⇒ 3 chunks (0–59, 60–119, 120–160). Total **4 × 3 = 12
chunks**, each 115,200 bytes, so **1,382,400 bytes ≈ 1.32 MiB** to read 4.17 % of
the data.

**(c)** The read costs ~1.4× the whole variable's *data* (3.74 MB uncompressed) in
bytes touched, to return 155,848 bytes of values. The cause is that the chunk shape
is elongated in time: a single time index requires the full lat/lon extent of a
time-chunk. For a "one time step at a time" workflow the correct on-disk chunking
is thin in time, e.g. `(1, 121, 161)` or `(1, 40, 60)`. **Chunk shape is chosen at
write time by the read pattern you expect, and it is invisible from the array.**

---

## ★9 — A defective file

**(a)** `_FillValue = 0.0` is the defect. Zero gravity anomaly is a legal and
common value; the sentinel lies inside the valid range. Both the writer and the
reader will treat any genuine zero as missing.

**(b)** A masked mean becomes a mean over the non-zero anomalies. For a field whose
true mean is near zero, the result is a number that looks plausible and is
systematically wrong; the exact size depends on the zero fraction. In the demo, a
sentinel that masks 3.08 % of the grid moved the mean by 30.125 m for an elevation
field — the mechanism is identical, the magnitude is data-dependent.

**(c)** Two lines:

```python
assert var._FillValue < data.min() or var._FillValue > data.max()
assert not (data == var._FillValue).any()
```

and, at ingestion, `arr.mask.sum()` compared with an expectation. A better fix is
not to use a sentinel at all: store missing data as a separate mask band.

---

## ★10 — Designing a packing scheme

**(a)** Range 670.0 mGal, required resolution 0.005 mGal ⇒ at least
$670/0.005 = 134{,}000$ levels ⇒ 17 bits. `int16` (32,767 levels) is **not
enough**; use `int32`, or accept `scale_factor = 0.02` with int16.

With `scale_factor = 0.005`, `add_offset = -250.0` (the value minimum), the code
range is $0$ to $(420 - (-250))/0.005 = 134{,}000$, and int32's limit of
2,147,483,647 is used to 0.006 %.

Better: centre the offset to halve the excursion:
$(\text{value} + 85.0)/0.005$ gives codes from $-33{,}000$ to $+101{,}000$; int16
still overflows, so int32 it is.

**(b)** rms $= 0.005/\sqrt{12} = 0.00144$ mGal, maximum $= 0.0025$ mGal. The
maximum is below the required resolution, which is the criterion: **the biggest
rounding error must be smaller than the resolution you promise.**

**(c)** Size for int32: $1000 \times 800 \times 4 = 3{,}200{,}000$ bytes. float32
would be the same size **and store more resolution** — 7 significant digits on
values near 400 mGal is $4 \times 10^{-5}$ mGal, 125× finer than needed. So for
this range the correct answer is **float32**, and packing to int32 buys nothing.
Packing only wins when the required resolution is *coarser* than float32 can spare
in the available range, or when the storage is at a premium and a documented
resolution loss is acceptable.

**(d)** Unsupported claims: any statement needing better than 0.0025 mGal
resolution, such as detecting a 0.001 mGal time-lapse signal. Supported claims:
regional field separation, anomaly amplitudes above 0.01 mGal, and survey
comparisons at the 0.01 mGal level.

---

## ★11 — Choosing on-disk chunks

Same cube in all three cases: 480 × 36 × 72, float32, 4,976,640 bytes.

**(a) One grid point's 40-year series.** Read pattern: the full time axis, one
lat/lon cell. Chunk `(480, 1, 1)` — 1,920 bytes per chunk, 2,592 chunks. The read
touches exactly one chunk. Cost: 2,592 chunks means metadata overhead, and any
global-map read touches a slice of all of them (36 × 72 = 2,592 slices of 480
values). A better compromise: `(480, 4, 4)` → 30,720 bytes per chunk, 162 chunks.

**(b) A global map for one month.** Chunk `(1, 36, 72)` — 10,368 bytes, 480
chunks; one chunk per map. This is also the layout that suits zonal and global
means along time reasonably well.

**(c) Zonal mean over all time.** Read pattern: every value, reduced along time
and longitude. Any chunking that keeps whole latitude circles enables the
longitude reduction locally; `(48, 1, 72)` groups longitude conveniently, or
`(48, 36, 72)` = 497,664 bytes lets a full time-block reduce in one task.

**Compromise.** `(48, 4, 72)`: 55,296 bytes per chunk, 10 × 9 × 1 = 90 chunks.
(a) reads 10 chunks instead of 1 (10× the metadata, ~1.1× the bytes);
(b) reads 10 chunks instead of 1; (c) reads all 90 with no cross-chunk reduction
except along time within a chunk. No layout is optimal for all three, and the
measured differences in
[04 Chunking with Dask for Out-of-Core Analysis](../04-dask-chunking.md) — 75 tasks
versus 1102 for the same cube — are the scale of the penalty.

---

## ★12 — A `_FillValue` failure report

A complete answer contains six things:

1. **The grid and the defect.** A synthetic elevation grid on a 30 m raster with
   `nodata = 0.0`, i.e. a sentinel inside the valid range (sea level). Any coastal
   or low-lying cell is a legitimate zero.
2. **The measurement.** Compute the mean with masking on and with
   `mask_and_scale=False`. Expect a difference of the same order as
   $f \times |\text{sentinel} - \text{mean}|$ where $f$ is the masked fraction: a
   3 % masked fraction with a sentinel 9,999 m below the mean moves the mean by
   ~300 m. (The demo's analogous case: 3.08 % masked and a 30.125 m shift with a
   5,000 m sentinel.)
3. **The mechanism.** The sentinel is a number; arithmetic cannot distinguish it
   from data unless the mask is applied, and masking is a *reader* option.
4. **The scale.** Report the difference in the field's units and as a percentage
   of the field's standard deviation, so the reader can see whether it is
   material.
5. **The check.** `assert arr.mask.sum() == expected_missing` at ingestion, plus
   `assert not (data == nodata).any()` before choosing the sentinel. Better: store
   the mask in its own band.
6. **The generalisation.** The same class of error arises with `scale_factor`
   (double packing), with `units` (unvalidated text), and with `Conventions`
   (a claim, not a validation). Metadata is trusted by readers and checked by
   nobody; a pipeline needs its own assertions.
