# Solutions — 22-03-01 Scientific File Formats

> Read after attempting. Numbers are computed here and match the demonstration's
> printed output. Lesson:
> [01 Scientific File Formats](../01-file-formats-scientific.md).

---

## ★1 — What a scientific file must carry

1. Shape and dtype. 2. Units. 3. Coordinates. 4. Missing-value convention.
5. Provenance. 6. Compression and chunking.

Guaranteed by the format itself: **shape and dtype** (in any serious binary or
self-describing format) and **compression and chunking** (as capabilities of the
container). Units, coordinates, missing-value conventions and provenance are the
writer's responsibility in every format — a netCDF file can carry a wrong `units`
attribute just as easily as a CSV can omit one, which is why the lesson treats
"we use netCDF" as a storage choice and not a metadata strategy.

## ★2 — Sizes of the four representations

(a) Bytes per value from the demonstration:

- text, 6 decimals: $2\,375\,126 / 250\,000 = 9.50$ bytes;
- binary float64: $2\,000\,000 / 250\,000 = 8.00$ bytes;
- binary float32: $1\,000\,000 / 250\,000 = 4.00$ bytes.

(b) Text to binary64 ratio $= 2\,375\,126 / 2\,000\,000 = 1.19$. Text is
*19 % larger*, not smaller.

(c) float32 to float64 $= 4.00/8.00 = 0.50$: half the size, with a rounding floor
for this data set of $2.23 \times 10^{-7}$ in the data's units — comparable to
writing six decimals in text ($5.00 \times 10^{-7}$), so the two "lossy" options
are of similar quality and should be compared that way.

## ★3 — Round-trip error versus uncertainty

| Decimals | Max error |
|---|---|
| 3 | $5.00 \times 10^{-4}$ |
| 6 | $5.00 \times 10^{-7}$ |
| 9 | $5.00 \times 10^{-10}$ |

Against a stated uncertainty of $1 \times 10^{-6}$, only **9 decimals**
($5.0 \times 10^{-10}$) is comfortably below it; 6 decimals
($5.0 \times 10^{-7}$) is below by a factor of two, which is too close for comfort
once the quantity spans a range; 3 decimals is 500 times larger than the
uncertainty and would dominate the error budget. The rule is to choose decimals so
the round-trip error is at least an order of magnitude below the uncertainty.

## ★★4 — Exchange of 500 000 values

(a) Sizes, using the per-value figures (values are unit-scale like the
demonstration's):

- text at 6 decimals: $500\,000 \times 9.50 = 4.75$ MB;
- binary float32: $500\,000 \times 4.00 = 2.00$ MB;
- binary float64: $500\,000 \times 8.00 = 4.00$ MB.

(b) Parse times: text $4.75/60 = 0.079$ s; float32 $2.00/2000 = 0.0010$ s;
float64 $4.00/2000 = 0.0020$ s. Text costs about **40–79×** the binary read time,
which matters if the file is read on every pipeline run
([22-02-03](../../02-reproducible-workflows/03-workflow-managers.md) §6).

(c) The two questions: **(i)** what uncertainty does the colleague's analysis
require, and does the error of the chosen representation stay well below it?
**(ii)** does the colleague need to inspect or hand-edit the file (which text makes
possible and binary does not)? The answers decide between text and binary with a
stated decimal count or dtype; the file's size is a consequence, not the criterion.

## ★★5 — A wrong `units` attribute

(a) A downstream user converting with the declared attribute multiplies by the
inverse of 1 m/s when the values are accelerations: a silent factor with the wrong
dimensions, compounding through any derivative or integration (a velocity error
becomes a position error that grows with time).

(b) A round-trip check (read, write, read) compares **values, shapes, dtypes, units
and coordinates** and will confirm that `units = "m/s"` survives the trip — the
attribute is consistent with itself. It detects a *lost* or changed attribute, not a
wrong one, because the check has no independent knowledge of the physics.

(c) The check that detects it is a **dimensional or magnitude test on the values**:
acceleration records from a seismic sensor have magnitudes of order $10^{-6}$ to
$10^{-1}\ \mathrm{m/s^{2}}$, while engineering strains in m/s are of a different
order; an assertion on plausible magnitude bounds and a comparison against a known
reference (a second data set, or a documented physical range in the metadata
standard for the channel type) catches the mismatch. This is the subject of
[22-03-05](../05-data-quality-control.md) and
[22-03-06](../06-metadata-standards.md).

## ★★6 — Compression, data-dependently

(a) The smooth ramp is an outer sum of two linear functions: adjacent 4-byte words
differ in a highly regular way, so a general-purpose compressor (zlib here) finds
long repeated patterns and predicts most bytes — 76.29×. White noise has no
redundancy beyond the byte distribution, so the same algorithm only removes the
redundancy of the float32 exponent bytes — 1.08×.

(b) The two properties to measure: **spatial or temporal smoothness** (how well a
value can be predicted from its neighbours) and **the dynamic range shared by the
values** (how much of each word is redundant exponent). A smooth field with a wide
range compresses differently from a smooth field with a narrow range.

(c) Publishing "we use compression, achieving ≈10×" is not a reproducible statement
unless the data and the algorithm are named; the same code gives 76× or 1.08×
depending on the field. Report the measured ratio on the actual archive, with the
algorithm's settings, or report nothing.

## ★★★7 — A format and metadata policy

**(i) 12-million-row catalogue → Parquet, partitioned by time (and station prefix).**
Metadata: typed schema (station code as string, not integer), units per column, the
time zone and reference epoch, the missing-value sentinel, the source catalogue and
query date, and the checksum of the conversion. Conversion checks: row count,
schema equality, per-column min/max/null counts, and a spot check of 1000 random
rows against the source. Compression: measure; a catalogue's numeric columns
typically compress well and its string columns depend on dictionary size.

**(ii) Daily 2000×2000 grid → netCDF per day (or Zarr for cloud-hosted access).**
Metadata: CF-style coordinate variables, units, the missing-value sentinel, the
processing level, and the version of the model or instrument that produced it.
Chunking to match the dominant query
([22-03-02](../02-format-design-tradeoffs.md)).
Conversion checks: value equality within a stated tolerance, coordinate equality
exactly, and a check that the fill value never collides with a valid value.

**(iii) 400 station parameter files → CSV (or a single Parquet table).**
Metadata: per-column units and conventions, the station-code format, and the
effective date of each parameter. Conversion checks: round trip of every field type,
and a comparison against the previous version to see what changed.

**The decision to revisit on moving to object storage.** The grid format: netCDF
holds one file per day, which is friendly on a filesystem and produces millions of
small objects on a store; Zarr's chunk-per-object layout is what makes range reads
efficient there, so the grid layer must be re-laid-out (and the checksums recomputed)
when the storage moves. The catalogue and the parameter files are unaffected.

## ★★8 — Relative error and decimals for a wide-range quantity

The round-trip error of decimal rounding is **absolute**: writing $d$ decimals gives
an error of at most $0.5 \times 10^{-d}$ regardless of the value's magnitude. For a
value $x$ the relative error is therefore

$$\varepsilon_{\text{rel}}(x) = \frac{0.5 \times 10^{-d}}{|x|},$$

which diverges as $x \to 0$. For an amplitude spectrum spanning four decades
($10^{-4}$ to $1$), six decimals give a relative error of $5 \times 10^{-3}$ at the
small end and $5 \times 10^{-7}$ at the large end — a factor of $10^{4}$ in quality
across one array. A single fixed decimal count therefore guarantees the *large*
values and silently degrades the small ones, which are often the physically
interesting part (a spectral trough, a small residual).

**The rule.** Either (a) choose decimals from the smallest quantity that matters —
which can force an impractical file size — or (b) store the values in binary (where
relative precision is uniform by construction, at $\approx 10^{-7}$ for float32 and
$\approx 10^{-16}$ for float64), and keep the text representation only for
inspection. A third option, used in spectral archives, is to store a logarithmic
quantity (dB or log-amplitude) whose range is narrow and whose rounding error is
therefore uniform in relative terms. What a single fixed decimal count cannot
guarantee is a *stated relative* accuracy across the array; it can only bound the
absolute error.

## ★★★9 — One HDF5 file per project

**Advantages.** (1) The metadata, the parameter files and the grids travel together,
so an archive is a single object to copy, checksum and cite — a real convenience for
distribution and for the versioning of
[22-02-05](../../02-reproducible-workflows/05-data-versioning.md). (2) Cross-dataset
consistency is expressed inside the format: the coordinates, the processing level and
the units of the three data sets can reference one another through groups and
attributes, so drift between them is less likely.

**Costs.** (1) **Granularity**: regenerating yesterday's grid requires rewriting the
file, so the cache unit becomes the whole project — the invalidation behaviour of
[22-02-03](../../02-reproducible-workflows/03-workflow-managers.md) §6 degrades to
"re-run everything". (2) **Size and diffs**: the file grows without bound, cannot be
diffed or partially transferred, and a version-control system cannot store it
sensibly; the three data sets have very different update rates (daily grid, yearly
catalogue, static parameters) and coupling them imposes the fastest rate on all.
(3) **Tooling**: not every reader has the library or the version that wrote the file,
so a reader's failure becomes a project-wide failure instead of a per-dataset one.

**The concurrency failure.** HDF5 files are not generally safe for concurrent
writers: two pipeline runs that open the same project file for writing can corrupt
it or fail with a locking error. On a filesystem with advisory locking the second
run typically blocks or errors, which is at least visible; on a shared or network
filesystem, or with a library that does not lock, the failure can be a silently
truncated or inconsistent file — and it appears only when two people (or two CI jobs)
run at once, which is exactly the situation a single-file design hides during
development. The fix in practice is one file per data set, per processing unit or per
day, with a manifest that lists them — which is the design the lesson recommends and
which the Zarr/Parquet patterns formalise.
