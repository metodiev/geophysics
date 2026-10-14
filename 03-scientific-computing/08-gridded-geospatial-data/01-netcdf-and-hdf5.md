---
id: 03-08-01
title: "netCDF/HDF5 Formats and Self-Describing Data"
level: intermediate
prereqs: ["03-01-06", "03-02-01", "03-04-01"]
tags: [netcdf, hdf5, cf-conventions, packing, file-io, grid]
---

# netCDF/HDF5 Formats and Self-Describing Data

A gravity grid, a climate reanalysis, a lidar swath and a seismic volume all have
the same shape: numbers on a regular multidimensional lattice. What separates
them from a raw `.npy` dump is **metadata** — which axis is latitude, in what
units, what value means *no data*, and how the numbers were quantised. This
lesson is about the container that carries both, and about the decisions its
author made on your behalf.

> **Every number in this lesson was produced by running the demonstration in
> `code/netcdf_hdf5_demo.py`** against a SYNTHETIC grid built inside the script.
> No dataset is downloaded and no observation of the Earth appears here.

## Learning objectives

By the end of this lesson you will be able to:

1. **Describe** the structural model of netCDF-4: named dimensions, variables
   that name those dimensions, coordinate variables, per-variable attributes and
   global attributes.
2. **Explain** why a netCDF-4 file is an HDF5 file, and what HDF5 adds that
   netCDF-3 lacked (groups, chunked storage, filters).
3. **Read** a variable's storage metadata — dtype, `scale_factor`, `add_offset`,
   `_FillValue`, chunk shape, compression — and predict what a read will return.
4. **Quantify** the information lost by packing: derive the rounding error
   distribution, and check it against the measured error.
5. **Size** a file before writing it, in bytes, from dimensions, dtype, packing
   and compression.
6. **Diagnose** the double-packing trap, in which a library packs values that are
   already codes, by its measured signature.
7. **Explain** what CF conventions add and what they do not guarantee.
8. **Read** a hyperslab without loading the whole variable.

## Prerequisites

- [03-01-06 Files, Paths and I/O](../01-python-fundamentals/06-files-and-io.md)
  — binary versus text files, and why "open and read" is not enough.
- [03-02-01 ndarray Creation, dtypes, Shapes and Strides](../02-numpy/01-ndarray-basics.md)
  — dtypes and `itemsize`, which determine every byte count below.
- [03-04-01 Series, DataFrame and the Labeled-Data Model](../04-pandas/01-series-dataframe.md)
  — the labelled-data idea that netCDF applies to $N$ dimensions.

## 1. Intuition: the file that explains itself

Consider two ways to store a 161×121 gravity anomaly grid.

```python
np.save("anomaly.npy", field)         # 155,848 bytes, no metadata at all
```

The `.npy` file records the shape and dtype and nothing else. Open it in five
years and you must answer, from memory or from a forgotten README: is the first
axis latitude or longitude? Do the longitudes run east or west? Are the values
mGal or µm/s²? Is a zero a real zero or a missing value? Was there a terrain
correction?

The alternative writes the same array plus the answers:

```
dimensions:  time = 24, lat = 121, lon = 161
variables:
    double lon(lon)      units = "degrees_east",  standard_name = "longitude"
    double lat(lat)      units = "degrees_north", standard_name = "latitude"
    double time(time)    units = "days since 2020-01-01 00:00:00"
    double anomaly(time, lat, lon)
                         units = "mGal", standard_name = "gravity_anomaly"
                         _FillValue = -9999.0
global attributes:       Conventions = "CF-1.11", title = "..."
```

That is **self-describing data**, and it is the difference between an archive and
a pile of numbers. The demonstration writes exactly this file.

## 2. Precise definitions

### 2.1 The data model

Four objects, and nothing else:

- A **dimension** is a named axis length: `lat = 121`. Dimensions are shared by
  every variable that uses them, which is what makes a temperature field, an
  elevation field and a land mask line up by construction rather than by
  convention.
- A **variable** is a named array that declares the dimensions it uses, in order:
  `anomaly(time, lat, lon)`.
- A **coordinate variable** is a variable whose name equals its only dimension:
  `lat(lat)`. This is the mechanism by which an index becomes a physical
  coordinate. There is no separate concept of "axis" — a coordinate variable is
  just an array that happens to be named after its axis.
- An **attribute** is a named, typed scalar or list attached to a variable or to
  the file as a whole: `units`, `standard_name`, `scale_factor`, `_FillValue`,
  `Conventions`.

A **group** is a named container that can hold dimensions, variables, attributes
and further groups. NetCDF-4 and HDF5 have groups; netCDF-3 does not.

### 2.2 NetCDF-4 is HDF5 plus conventions

`netCDF4.Dataset(path, "w", format="NETCDF4")` writes an HDF5 file. The
demonstration proves it by reopening the same file with `h5py` and reading the
root group:

```
root group members: ['anomaly', 'lat', 'lon', 'time']
/anomaly  dtype=float64 shape=(24, 121, 161) chunks=None compression=None
/anomaly  attrs=['DIMENSION_LIST', '_Netcdf4Coordinates', '_Netcdf4Dimid', ...]
HDF5 library version = 2.0.0
```

Two things follow. First, **any HDF5 reader can read the bytes**, even one that
has never heard of netCDF: the arrays, their shapes and dtypes are plain HDF5
datasets. Second, **only a netCDF-aware reader can interpret them**: the mapping
of dimension names to axes lives in netCDF-specific HDF5 attributes
(`DIMENSION_LIST`, `_Netcdf4Dimid`). An HDF5-only view gives you arrays in an
order; it does not give you "latitude".

HDF5 contributes what plain netCDF-3 could not express:

| Capability | netCDF-3 (classic) | HDF5 / netCDF-4 |
|---|---|---|
| Groups | no | yes, nested |
| Per-variable chunking | no | yes, any shape |
| Compression and filters | no | deflate, shuffle, and others |
| Unlimited dimensions | one only | many |
| User-defined types | no | yes |

**Chunking** is the on-disk analogue of a tile: the variable is stored as
fixed-shape blocks, and a chunk is the smallest unit of I/O. If your read pattern
is a time series at one pixel and the chunks are shaped along time, you read one
chunk; if the chunks are shaped along space, you read one slice from every
chunk. **Compression** is applied per chunk, which is why chunk shape and
compression ratio are coupled.

The measured file sizes for a 467,544-value float64 grid make this concrete:

```
none          :  3,752,918 bytes  (ratio 1.00x)
zlib level 1  :  3,118,732 bytes  (ratio 1.20x)
zlib level 6  :  3,091,146 bytes  (ratio 1.21x)
chunked 6x40x60:  3,187,955 bytes  (ratio 1.18x)   chunk = 115,200 bytes
```

Note what these numbers say. Deflate gains only 20 % on smooth, mostly random
data, and raising the level from 1 to 6 buys 0.9 %. Compression is not a
substitute for choosing the right dtype; the next section is.

### 2.3 Packing: `scale_factor` and `add_offset`

A gravity anomaly needs about three decimals of a mGal. Storing it as float64
spends 8 bytes per value on a quantity that needs 2. **Packing** stores an
integer code and records the linear map:

$$\text{value} = \texttt{scale\_factor} \times \text{code}
  + \texttt{add\_offset}.$$

CF also defines the inverse, which is how a writer computes codes:

$$\text{code} = \operatorname{round}\!\left(
  \frac{\text{value} - \texttt{add\_offset}}{\texttt{scale\_factor}}\right).$$

For the demonstration, `scale_factor = 0.01 mGal/count` and
`add_offset = 20.0 mGal`, stored as `int16`:

```
int16 code range used = -2432 .. 837 (int16 limits -32767 .. 32767)
on-disk size, packed int16 = 949,864 bytes (3.95x smaller)
```

The int16 range was not a constraint here — the codes used 10 % of the available
range. Had the values needed $|x - 20| > 327.67$ mGal, the codes would have
wrapped, silently, and the file would contain plausible-looking garbage.

### 2.4 `_FillValue` is metadata, not a number

CF uses a specific value as a sentinel for missing data and names it in the
`_FillValue` attribute. The demonstration masks a synthetic ocean corner and
measures:

```
values masked as missing = 14,400 (3.08 % of the grid)
with mask_and_scale=False the raw sentinel survives: min = -9999.0
```

The essential point is that a masked read and an unmasked read return *different
numbers from the same file*. The demonstration's mean elevation is 42.659 m when
the mask is honoured and 12.534 m when it is not — a 30.125 m difference produced
by a metadata attribute, not by data.

## 3. What CF conventions add

**CF** (Climate and Forecast conventions) is a set of agreements about attribute
*values*, layered on top of the netCDF data model:

- `units` is a machine-readable string from a controlled grammar
  (`"mGal"`, `"days since 2020-01-01 00:00:00"`, `"degrees_east"`).
- `standard_name` is drawn from a controlled vocabulary, so that two
  independent files can be compared automatically (`"gravity_anomaly"`,
  `"sea_surface_temperature"`).
- `coordinates` names auxiliary coordinate variables for a data variable.
- `_FillValue`, `scale_factor`, `add_offset`, `valid_min`, `valid_max` describe
  the stored representation.
- The `Conventions` global attribute states which document the file claims to
  follow. If it is absent, nothing is promised.

CF's honesty matters as much as its content: **CF describes the file, it does not
validate the science.** A file can say `units = "mGal"` about a field measured in
µm/s², and no reader will complain. Self-describing means *carrying* a
description, not *proving* one.

## 4. Derivations and worked reasoning

### 4.1 The rounding error of a packed variable

Packing rounds a real value to a multiple of `scale_factor` $s$. Under the usual
assumption that the discarded fractional part is uniform on $[-s/2, s/2]$, the
error $\epsilon$ has mean zero and variance

$$\operatorname{Var}[\epsilon] = \frac{1}{s}\int_{-s/2}^{s/2} \epsilon^{2}\,d\epsilon
= \frac{s^{2}}{12}.$$

The root-mean-square error is therefore $s/\sqrt{12}$, and the maximum error is
$s/2$. For $s = 0.01$ mGal these are $0.01/\sqrt{12} = 0.002887$ mGal and
$0.005$ mGal. The demonstration measures:

```
half a count = 0.0050 mGal; ideal rms error for uniform rounding = 0.00289 mGal
measured  rms error = 0.00289 mGal
measured  max error = 0.00500 mGal
```

Agreement to three significant figures. This is how you choose a scale factor:
decide the largest tolerable error, double it, and that is $s$. If a 0.01 mGal
survey is used, $s = 0.01$ is defensible; if a 0.001 mGal gradiometry survey is
stored with $s = 0.01$, the packing has destroyed the measurement before the file
was closed, and it did so *losslessly reproducibly*, which makes it worse.

The same algebra in reverse sets the storage requirement. Representing values in
$[v_{\min}, v_{\max}]$ with resolution $s$ needs
$N = (v_{\max} - v_{\min})/s$ code levels, hence a dtype with

$$\log_2 N \le \text{bits available}.$$

The demonstration's range is 32.69 mGal of anomaly at $s = 0.01$: $N = 3269$
levels, and $\log_2 3269 = 11.7$, so 12 bits would do and int16 is comfortable.

### 4.2 File size, computed before writing

For $n_t \times n_y \times n_x$ values of $b$ bytes each, the payload is
$n_t n_y n_x b$ bytes and the file adds header, dimension tables and attribute
text. Measured:

| Quantity | Computed | Measured |
|---|---|---|
| grid size | $24 \times 121 \times 161 = 467{,}544$ | `467,544 values` |
| float64 payload | $467{,}544 \times 8 = 3{,}740{,}352$ B | `3,740,352 bytes` in memory |
| float64 file | $3{,}740{,}352 + \text{header}$ | `3,752,918 bytes` |
| packed file | $467{,}544 \times 2 + \text{header}$ | `949,864 bytes` |

The overhead is $3{,}752{,}918 - 3{,}740{,}352 = 12{,}566$ bytes, about 0.33 %:
metadata is cheap, and that is precisely why there is no excuse for omitting it.

### 4.3 The double-packing trap, measured

A library that knows about `scale_factor` may apply it *on write* as well as
unpack on read. Writing already-rounded codes into a `scale_factor`-bearing
variable packs them twice. The demonstration measures the result:

```
writing ALREADY-ROUNDED codes with scale_factor set (the bug):
  max error = 350.18 mGal vs a 0.005 mGal rounding budget
  stored codes occupied -32764 .. 32744 instead of -2432 .. 837
  codes outside the correct range = 441,089 (94.3 % of the grid)
```

Read that carefully. The file is valid. It opens. The values are in a plausible
range. **94.3 % of the stored codes are wrong, and the maximum error is 350
mGal, 70,000 times the rounding budget.** Nothing warns you, because the library
did exactly what the metadata said. The fix is to store codes with automatic
scaling switched off (`set_auto_scale(False)` in `netCDF4`) or to write physical
values and let the library pack. The lesson is general: **when a file format
carries a transform, know which side of it your numbers are on.**

### 4.4 Hyperslab reads

Reading one time step of the demonstration's variable returns $121 \times 161 =
19{,}481$ of 467,544 values — 4.17 % of the data — with a measured mean of
0.3640 mGal and standard deviation 2.7904 mGal. With chunked storage, the bytes
actually read are the chunks that overlap the requested slab, not the slab
itself. If the on-disk chunk shape is `(6, 40, 60)` and you request one time
index, you touch 3 time-slices' worth of chunks in every spatial block: 64
chunks × 115,200 bytes instead of the 155,848 bytes of the slab. Chunk shape is a
read-pattern decision made at write time, and it is invisible from the array.

## 5. Units and dimensional analysis

Units are the one part of the metadata with a formal grammar, so they can be
checked. Three habits worth keeping:

**Carry the unit through the packing arithmetic.** `scale_factor` has units
`[value]/[code]`: here `mGal/count`. `add_offset` has units `[value]`, here mGal.
Multiplying a dimensionless code by `mGal/count` yields mGal, which is why
`value = scale_factor * code + add_offset` is dimensionally consistent and
`value = scale_factor * code * add_offset` is not — it would give mGal²/count.

**Let the units catch a wrong reader.** If a file declares `units = "mGal"` and
your analysis treats the numbers as µm/s², every anomaly is 1000× too large;
the factor between mGal and nm/s² is exactly 1000. A reader that respects units
would refuse the comparison.

**Distinguish a coordinate's unit from its axis's.** `lon` has
`units = "degrees_east"` and `axis = "X"`; `time` has
`units = "days since 2020-01-01 00:00:00"` — a *unit with an epoch*. The epoch
matters: the same stored number means a different instant under a different
epoch, and a file without the epoch is not readable in a physical sense.

## 6. Python demonstration

The full script is
[`code/netcdf_hdf5_demo.py`](./code/netcdf_hdf5_demo.py); run it with the project
interpreter:

```bash
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python \
    03-scientific-computing/08-gridded-geospatial-data/code/netcdf_hdf5_demo.py
```

It writes four files into a throw-away directory inside the module and deletes
them on exit, so nothing is left behind and nothing is committed.

### What to observe, and why it matters

| Observation | Consequence |
|---|---|
| `h5py` lists the same root members as netCDF | netCDF-4 files are HDF5; other tools can read them |
| `/anomaly chunks=None` for the uncompressed file | an unchunked variable is one contiguous block per slice |
| rms packing error $= 0.00289$ mGal $= s/\sqrt{12}$ | the quantisation model is testable, not folklore |
| double packing corrupts 94.3 % of codes | `scale_factor` has two sides; check which one you are on |
| `_FillValue` read changes the mean by 30.125 m | masking is a metadata decision, and it is on by default |
| deflate buys 1.20× on this grid | compression is weak against already-smooth data |
| one time step is 4.17 % of the values | hyperslab reads are cheap only if the chunking agrees |

> **Breaking exercise.** Before running the script, change `scale_factor` to
> `0.001` and predict (a) the new rms error, (b) the new code range, and
> (c) whether the int16 range is still adequate for a 32.69 mGal anomaly. Then
> run it and compare.

## 7. Common mistakes

1. **Assuming `_FillValue` is applied on read.** It is applied by default in
   `netCDF4` and `xarray`, but not by a raw HDF5 read, and not if you pass
   `mask_and_scale=False`. Both behaviours are silent.
2. **Double-packing.** Writing codes into a variable that declares
   `scale_factor`. Measured cost: 350 mGal of error on a 0.005 mGal budget.
3. **Choosing `add_offset` from the wrong statistic.** `add_offset` should sit
   near the middle of the value range. Choosing it at the minimum wastes half
   the code range on values that cannot occur.
4. **Forgetting that `units` is a string.** `"mGal"` and `"mgal"` are different
   strings; readers that compare units will treat them as different quantities.
5. **Chunking for the writer.** A chunk shape chosen to make writes fast can make
   the dominant read pattern absurdly slow, and the choice is baked into the
   file.
6. **Believing `Conventions = "CF-1.11"` is a validation.** It is a claim. Check
   the attributes you depend on.
7. **Storing float64 when 16 bits of packed int16 would do.** Measured here:
   3.95× the file size for digits that the measurement does not support.

## 8. Real-world applications

- **Satellite altimetry and gravimetry.** Marine gravity grids are distributed as
  packed int16 NetCDF with `scale_factor` near 0.1 mGal, because the file size of
  a global 1′ grid is otherwise prohibitive.
- **Climate reanalysis.** ERA5-style products rely on `standard_name` and the
  time epoch for every automated cross-file comparison; a wrong epoch shifts
  every timestamp in a multi-decade series.
- **Seismic volumes.** SEG-Y is the industry container for the same gridded idea
  with a 3200-byte textual header and a 400-byte binary header; reading it is
  1970s-vintage metadata archaeology, and it is why netCDF/HDF5 exports exist.
- **Airborne geophysics.** Survey grids ship as GeoTIFF or NetCDF with a filled
  `_FillValue` for the gaps between flight lines, and the gap fraction is a
  first-order quality metric.
- **Instrument formats.** Many seismographs and magnetometers write HDF5
  directly, so `h5py` is the low-level tool that gets you the raw counts before
  any convention is applied.

## 9. Further reading

- **Unidata, *netCDF4-python documentation*.** Level: reference.
  <https://unidata.github.io/netcdf4-python/> — the authoritative page for
  `set_auto_scale`, `set_auto_mask`, and the packing semantics discussed in
  Section 4.3.
- **CF Conventions Committee, *NetCDF Climate and Forecast (CF) Metadata
  Conventions*.** Level: reference. <https://cfconventions.org> — start with the
  sections on the data model, `units` and packing.
- **The HDF Group, *HDF5 documentation*.** Level: advanced.
  <https://gdal.org> documents the GDAL/HDF5 drivers that many geoscience tools
  go through, and <https://docs.xarray.dev> shows the netCDF layer built on top.
- **Unidata, *NetCDF User's Guide*.** Level: intermediate. The clearest account of
  the classic data model that netCDF-4 extends; available from Unidata.
- **Rew, R. and Davis, G. (1990). NetCDF: an interface for scientific data
  access. *IEEE Computer Graphics and Applications*, 10(4), 76–82.** Level:
  intermediate. The original design paper, and still the best statement of why
  self-describing data won. Check your library for access.

> Note on citations: bibliographic details are given so you can locate these
> works. This repository does not host or reproduce copyrighted text.

## 10. Related lessons

- [02 xarray DataArray, Coordinates and Labeled Dimensions](./02-xarray-dataarray.md)
  — the in-memory object that mirrors this file model.
- [03 Dataset, Alignment, Broadcasting and GroupBy](./03-xarray-dataset.md)
  — where `_FillValue` becomes NaN and weights become areas.
- [06 rasterio: Rasters, Windows, Masks and Reprojection](./06-rasterio-rasters.md)
  — the other major gridded container, with its own transform metadata.
- [03-02-01 ndarray Creation, dtypes, Shapes and Strides](../02-numpy/01-ndarray-basics.md)
  — `itemsize` is what turns a shape into the byte counts above.
- [03-04-03 Cleaning: Missing Values, Duplicates and Outliers](../04-pandas/03-cleaning-data.md)
  — the tabular version of `_FillValue`.

## Exercises

[`exercises/01-netcdf-and-hdf5-exercises.md`](./exercises/01-netcdf-and-hdf5-exercises.md),
with full worked answers in
[`exercises/01-netcdf-and-hdf5-solutions.md`](./exercises/01-netcdf-and-hdf5-solutions.md).

## Self-assessment checklist

- [ ] I can name the four objects of the netCDF data model, and say which one
      makes an index into a physical coordinate.
- [ ] I can explain, in one sentence, why a netCDF-4 file can be opened with
      `h5py` but not fully understood by it.
- [ ] I can compute the rms error of a packed variable from its `scale_factor`
      and say what assumption that calculation makes.
- [ ] I can predict whether int16 is wide enough for a given value range and
      resolution.
- [ ] I can state the exact symptom of double packing and how to prevent it.
- [ ] I can say what a masked read of `_FillValue` changes, and quote the
      measured difference from the demonstration.
- [ ] I can size a file in bytes from dimensions, dtype, packing and
      compression, before writing it.
- [ ] I can explain why compression saved only 20 % on this grid and what to do
      instead.
