---
id: 03-08-02
title: "xarray DataArray, Coordinates and Labeled Dimensions"
level: intermediate
prereqs: ["03-08-01", "03-02-01", "03-04-02"]
tags: [xarray, dataarray, coordinates, alignment, indexing, broadcasting]
---

# xarray DataArray, Coordinates and Labeled Dimensions

A NumPy array knows its shape. It does not know that axis 0 is latitude or that
the value at index 56 is at 113°W. Every function that touches a geophysical grid
therefore carries two implicit contracts in its docstring: the axis order, and
the coordinate convention. `xarray` makes both explicit, and then uses them.

> **All values quoted below are measured output from
> `code/xarray_dataarray_demo.py`**, which builds a SYNTHETIC Gaussian gravity
> anomaly on a regular lon/lat grid. Nothing is downloaded.

## Learning objectives

By the end of this lesson you will be able to:

1. **Construct** a `DataArray` from an array plus named coordinates, and describe
   its `dims`, `sizes`, `coords`, `dtype` and `attrs`.
2. **Choose** between label-based (`.sel`) and position-based (`.isel`) indexing,
   and explain when each is the only correct one.
3. **Predict** the result of arithmetic on two `DataArray`s with different
   coordinate values, and say which join xarray performs by default.
4. **Diagnose** the silent failure in which a coordinate dtype difference
   destroys almost every label match.
5. **Explain** broadcasting in terms of dimension *names* rather than shapes.
6. **Quantify** the accuracy cost of regridding with `linear` and `cubic`
   interpolation, including the overshoot that cubic produces at a step.
7. **Use** `where`, `resample`, `groupby` and `differentiate` on labelled data
   without breaking the coordinates.
8. **State** what `attrs` are and are not, and why the library will not protect
   you from a wrong unit.

## Prerequisites

- [03-08-01 netCDF/HDF5 Formats and Self-Describing Data](./01-netcdf-and-hdf5.md)
  — the file model this object mirrors.
- [03-02-01 ndarray Creation, dtypes, Shapes and Strides](../02-numpy/01-ndarray-basics.md)
  — the array underneath.
- [03-04-02 Indexing, Selection, loc/iloc and Boolean Masks](../04-pandas/02-indexing-selection.md)
  — the same label-versus-position distinction in one dimension.

## 1. Intuition: an array with a memory

Here is a mistake that has a long and dishonourable history: an analysis reads a
gravity grid, applies a correction along the wrong axis, and produces a map that
is superficially plausible. Nothing raises. The numbers are the right order of
magnitude. The error is discovered months later, if at all.

`xarray` prevents that class of error by attaching names to axes and values to
positions, then using them everywhere:

```python
anomaly = xr.DataArray(field, dims=("lat", "lon"),
                       coords={"lat": lat, "lon": lon}, name="anomaly",
                       attrs={"units": "mGal"})
```

Once this object exists:

- `anomaly.mean("lat")` removes a *named* axis, not axis 0.
- `anomaly.sel(lon=-113.0)` addresses a *physical* coordinate.
- `anomaly * profile` where `profile` has dim `lat` multiplies every longitude
  by the correct latitude factor, because the names say so.
- Two arrays with different longitude grids combine on the *intersection* of
  their labels rather than by silently using index alignment.

The last two behaviours are where xarray's value is concentrated, and they are
also where its sharpest failure modes live: they are silent, and they are
coordinate-shaped.

## 2. Precise definitions

### 2.1 The `DataArray` object

A `DataArray` is five things:

| Part | Meaning | Example (measured) |
|---|---|---|
| `values` | the array | `(121, 161)` float64 |
| `dims` | axis names | `('lat', 'lon')` |
| `coords` | named arrays indexed by the dims | `lat` = 30.0…45.0, `lon` = −120.0…−100.0 |
| `name` | what the values are | `'anomaly'` |
| `attrs` | arbitrary metadata | `{'units': 'mGal', ...}` |

The array has 19,481 values and occupies 155,848 bytes (8 bytes each). The
memory model is the key to the indexing model: a coordinate is a *parallel array*
along an axis, and `sel` works by searching it.

### 2.2 Label versus position

`.isel(lon=56)` means "the 57th longitude". `.sel(lon=-113.0)` means "the
longitude that is −113.0". The demonstration measures that these coincide *here*
because the grid is regular and `−113.0` is exactly representable:

```
positional da.isel(lon=56)  lon label = -113.0000 deg
label      da.sel(lon=-113.0, lat=37.5) value = 0.6029 mGal
the two address the SAME cell: True
```

They coincide by luck, and the luck is bought with a regularity that real data
do not always have. The coordinate values are the physical statement; the index
is an implementation detail.

A partial selection keeps the coordinates it did not reduce:
`da.sel(lon=slice(-113.0, -108.0), lat=slice(35.0, 40.0))` returns shape
`(41, 41)` — 1,681 of 19,481 values, 8.6 % — with mean 4.1404 mGal. Note that a
`slice` in `.sel` is *inclusive* of both endpoints, unlike a Python list slice,
because coordinates are labels.

### 2.3 Alignment: which join, and when

Two `DataArray`s with different coordinate values must be reconciled before
arithmetic. xarray's default for arithmetic is the **intersection** of the
labels:

```
arithmetic_join = inner
da + half (default join='inner') -> shape (121, 0), size 0: an EMPTY result
```

That is not a typo. The demonstration adds two fields whose longitude grids
differ by half a cell (0.0625°); no label is shared, so the result has **zero
columns** and raises nothing. The same operation with an explicit union gives the
full grid:

```
xr.align(da, half, join='outer') -> shape (121, 322)
outer sum NaN count = 38,962 (100.0 % of the result)
```

With an integer-shift pair, where the labels *do* overlap:

```
integer 10-cell shift: inner -> (121, 151), outer -> (121, 161) with 1,210 NaN
```

and `xr.align(da, shifted, join="exact")` raises `AlignmentError` instead of
choosing silently. Three joins, three behaviours, all defensible — and the
default is the one that discards data. **State the join you want.**

**Table of joins.** Alignment is a set operation on coordinate values, and there
are six ways to resolve it. Each is defensible; only one is safe by default for
the question you are asking.

| `join=` | Resulting index | Failure mode | When it is right |
|---|---|---|---|
| `inner` (arithmetic default) | labels in both | discards data; can be empty | comparing coincident samples |
| `outer` (merge default) | labels in either | introduces NaN the size of the union | you want every label kept |
| `left` | labels of the first | asymmetric; order matters | the first array defines the grid |
| `right` | labels of the second | asymmetric in the other direction | the second array defines the grid |
| `exact` | error unless identical | refuses to proceed | you have asserted the grids match |
| `override` | labels of the first, used for both | silently discards the second's labels | one grid is authoritative by design |

The asymmetry of `left` and `right` is worth a moment. `a + b` with
`join="left"` is not the same as `b + a` with `join="left"`: addition is
commutative in value but not in *index*. In a pipeline, this means that the
order of two lines can change which samples exist.

**Alignment arithmetic.** The union of two regular grids with spacings
$\Delta$ and $\Delta$ offset by $k$ cells is a grid with $n_1 + n_2 - n_{\text{overlap}}$
labels, and the NaN count in an outer join equals the number of labels present in
exactly one input, multiplied by the other dimension's size. The demonstration's
numbers check out exactly:

- half-cell offset: overlap $= 0$, union $= 161 + 161 = 322$, NaN $= 121 \times 322 = 38{,}962$,
  which is 100 % of the result — the measured value;
- ten-cell offset: the second grid is a *subset* of the first, so the union is
  the first grid's 161 labels and the extra labels are 10, giving
  NaN $= 121 \times 10 = 1{,}210$, which is 6.2 % of $121 \times 161 = 19{,}481$ —
  again the measured value.

Being able to predict the NaN count before running the code is how you tell an
intentional outer join from an accidental one.

### 2.4 Coordinate dtype is part of the data

A grid whose coordinates are stored as float32 (common: many files store
coordinates as float32 to save space) has labels that are *almost* the same as
their float64 twins. The demonstration measures the gap and its consequence:

```
201 labels at 0.1 deg spacing, stored float64 vs float32
labels that still match after float32 -> float64: 1
largest label shift = 3.052e-06 deg = 0.340 m
a64 = (121, 201), a32 = (121, 201)
a64 + a32  ->  shape (121, 1) with no error and no NaN
```

Two full grids combine into a single column. The 3.05 × 10⁻⁶ degree error is 34
centimetres — geodetically negligible, and completely fatal to a dictionary
lookup. The repair is explicit: `xr.align(a64, a32, join="override")` returns
`(121, 201)`, or convert coordinates with `.assign_coords(lon=lon.astype("float64"))`.
Note also that `a32.sel(lon=-110.0, lat=37.5)` returns 27.9564 mGal without
complaint, because the *key* is cast to the coordinate dtype on the way in. The
trap is between arrays, not inside one.

### 2.5 Broadcasting

Broadcasting in xarray is by dimension name:

```
(lat,lon) * (lat,) -> (121, 161)
row factors: 1.0000 (30 N) .. 1.2000 (45 N)
measured scaling at 45 N = 1.2000 (expected 1.2000)
```

A one-dimensional array with dim `lat` multiplies every column sharing that
latitude. Renaming the dim to `lon` would broadcast along the other axis — or
fail, if the size did not match. In NumPy the same expression broadcasts by
*position* and succeeds or fails for shape reasons; a transposed array is
silently a different computation. Here it is not.

`differentiate("lat")` computes the derivative with respect to the coordinate
and keeps the same dims and coordinates. Note the measured surprise in its
`attrs`: an empty dict. Coordinate metadata travels with the coordinate; value
metadata does not travel automatically through every operation.

### 2.6 Masking and where

```
cells above 5 mGal = 437 (2.2 %)
da.where(mask)          : shape (121, 161), stored values 19,481, NaN 19,044
da.where(mask, drop=True): shape (19, 29), stored values 551
both give the same mean, 13.3502 mGal
memory kept for the mask: 155,848 bytes vs 4,408 bytes (35.4x)
```

`drop=True` removes only rows and columns that became *entirely* NaN, so the mean
is unchanged — what changes is the shape and the memory. It is a representation
choice, not a statistical one. Because the non-NaN cells are contiguous here,
the drop is a factor of 35.4 in memory; on a scattered mask it would save much
less.

## 3. Interpolation: the cost of regridding, measured

Regridding is a modelling decision that is usually presented as a technical one.
The demonstration compares a coarse analytic field (0.25° spacing) interpolated
onto a fine grid (0.125°) against the exact analytic value:

| Method | max error (mGal) | rms error (mGal) |
|---|---|---|
| linear | 0.7097 | 0.0302 |
| cubic | 0.0066 | 0.0003 |

On a smooth Gaussian sampled at twice the target spacing, cubic beats linear by
two orders of magnitude — the *opposite* of a common assumption that higher-order
schemes are risky and rarely worth it. The measured exception is a **step**, where
cubic's wider stencil overshoots:

```
linear  across a 100 m step: min = 0.00 m, max = 100.00 m (overshoot = 0.00 m)
nearest across a 100 m step: min = 0.00 m, max = 100.00 m (overshoot = 0.00 m)
cubic   across a 100 m step: min = -10.76 m, max = 100.00 m (overshoot = 10.76 m)
```

Cubic invented an 10.76 m depression that does not exist in the data. So the rule
is not "use cubic" or "use linear"; it is **choose the method whose assumptions
match the field**. Smooth potential fields: cubic. Sharp interfaces, masked
coasts, fault scarps: linear or nearest, or smooth explicitly before regridding.

## 4. Time coordinates and grouped operations

Time is a coordinate like any other, with the same rules and one extra: it can be
resampled and grouped.

```
60 samples, 2000-01-01 .. 2004-11-05, dtype datetime64[s]
resample(time='YE').mean() -> 5 annual means; first = 0.226 m, last = 0.954 m
groupby('time.month') -> 12 groups, samples per group [6, 4, 6, 5, 5, 5, 5, 5, 5, 5, 5, 4]
the imposed trend is exactly +0.02000 m per sample;
a straight least-squares fit returns 0.02133 m/sample
```

Two measured lessons sit in those lines.

First, the group sizes are **not equal** — the series is 30-day steps, so calendar
months receive 4, 5 or 6 samples. A climatology built from such a series is a
mean of unequally weighted months, which is fine as long as you know it and wrong
if you assume a monthly product is uniform.

Second, fitting a straight line to a series that contains a seasonal cycle gives
0.02133 instead of the imposed 0.02000: a 6.7 % bias from an unfitted term.
**Residuals are not noise.** If your model omits a known periodic component, the
slope absorbs part of it, and no amount of data will fix that particular error.
The remedy is to remove the seasonal cycle first, which is a one-line
`groupby("time.month")` subtraction, as in the demonstration's sister lesson
[05 Case Study: Analysing a Climate Data Cube](./05-climate-data-cube.md).

### 4.1 A worked example: gradients on a labelled grid

Suppose the task is the horizontal gradient of the anomaly in mGal per kilometre.
Two routes exist, and only one is honest.

**Route A, in degrees.** `da.differentiate("lon")` returns mGal per degree. A
degree of longitude is not a fixed distance: the demonstration measures it as
85.39 km at 40°N and 55.80 km at 60°N for a 1° separation. So a gradient in
mGal/degree is a gradient in a unit that changes with latitude, and comparing two
such gradients at different latitudes compares different physical quantities.

**Route B, in metres.** Convert with the local scale factor,

$$\frac{\partial a}{\partial x} = \frac{\partial a}{\partial \lambda}\cdot
  \frac{1}{R\cos\phi \cdot \pi/180},$$

where $R\cos\phi$ is the local parallel radius and the factor $\pi/180$ converts
degrees to radians. Using $R = 6{,}371$ km at 37.5°N the parallel radius is
$6{,}371\cos(37.5°)\ \mathrm{km} = 5{,}054$ km, so one degree of longitude is
88.2 km and the conversion factor is $1/88{,}200$ km⁻¹. A gradient of 0.5 mGal per
degree is 0.0057 mGal/km. Reporting the first number is not wrong; reporting it
without saying that it depends on latitude is.

This is why the resampling and reduction lessons keep returning to area
weighting: on a lon/lat grid, both the cell *area* and the cell *width* vary, and
every operator that touches neighbouring cells — gradients, Laplacians,
smoothing — inherits that variation.

### 4.2 Coordinates that are not one-dimensional

Everything above assumed coordinates are 1-D arrays, one per dimension. Ocean and
weather models on curvilinear grids break that: they carry `lat(y, x)` and
`lon(y, x)` as two-dimensional coordinates. Then

- `.sel(lat=40.0)` is no longer a slice but a search over an unstructured point
  cloud, and xarray will refuse or fall back to nearest-neighbour;
- `.interp(..., method="linear")` requires
  `scipy.interpolate.RegularGridInterpolator`-style 1-D coordinates, so the
  correct tool becomes `xr.DataArray.interp` with
  `scipy.interpolate.griddata` behind a wrapper, or a regridding package;
- `mean("lat")` stops being an average over a latitude line, because a `lat`
  coordinate along `x` no longer indexes one.

The signal that you have this case is a coordinate whose `dims` is not equal to
its name. Check `da.coords["lat"].dims` before writing any reduction.

## 5. Units and dimensional analysis

`attrs` is a plain dictionary, and xarray copies it as text.

```
xr.get_options()['keep_attrs'] = default
da.attrs before arithmetic: ['long_name', 'source', 'units']
(da * 2.0).attrs: ['long_name', 'source', 'units']  <- units kept, magnitudes doubled
with keep_attrs=False: []
(da * 1e6).attrs still claims 'mGal' while the values are 1e6 times larger:
  max = 2.836e+07 labelled 'mGal'
```

Three conclusions, all measured:

1. **Attributes are propagated by default** in the installed xarray (2026.9.0),
   and the default is configurable (`keep_attrs`). Do not assume either
   behaviour from an older tutorial; check
   `xr.get_options()['keep_attrs']` on your own installation.
2. **A propagated unit can become wrong.** Multiplying by 10⁶ produced a field
   whose values are in µGal, still labelled mGal. Nothing checks this.
3. **Nothing enforces dimensional compatibility.** `da_gauss + da_elevation`
   succeeds and produces a number with no meaning. This is the single largest
   difference between xarray and a unit-aware library, and it is a deliberate
   trade for speed and simplicity. If dimensional analysis matters in your
   pipeline, it has to be code you write.

The habit that replaces library enforcement is naming: keep units in the variable
name (`anomaly_mgal`, `elevation_m`) as well as in `attrs`, and assert units at
the boundary of every function that accepts a `DataArray`.

## 6. Python demonstration

The full script is
[`code/xarray_dataarray_demo.py`](./code/xarray_dataarray_demo.py):

```bash
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python \
    03-scientific-computing/08-gridded-geospatial-data/code/xarray_dataarray_demo.py
```

It is offline, seeded (`np.random.default_rng(20260802)`), and prints ten
labelled sections.

### What to observe, and why it matters

| Observation | Consequence in practice |
|---|---|
| `.sel` and `.isel` agree on a regular grid | label addressing is a statement about the *coordinate*, not the index |
| `(lat,lon) * (lat,)` scales the right axis | broadcasting is by name, so transposition cannot silently change the computation |
| arithmetic default join is `inner` | two grids with different labels can combine into an empty array |
| float32 vs float64 coordinates match on 1 of 201 labels | coordinate dtype is part of the grid's identity |
| cubic reduces max error 100× on a smooth field | the interpolator should match the field's smoothness |
| cubic overshoots a step by 10.76 m | the same choice is wrong across a scarp |
| `(da * 1e6).attrs` still says `mGal` | attribute propagation is copy-paste, not analysis |
| `.values` returned a writable view | editing the buffer edits the `DataArray` |

> **Breaking exercise.** Modify the demonstration to give the two grids the same
> float64 longitude values but different latitudes (one starting at 30.0, one at
> 30.5). Predict the shape of `a + b` before running, given that the default join
> is `inner`.

## 7. Common mistakes

1. **Relying on the default join.** `inner` is correct when you want the
   intersection and catastrophic when you wanted the union.
2. **Mixing coordinate dtypes.** Measured here: 1 surviving label out of 201,
   with no warning.
3. **Assuming `attrs` means something.** A unit label is a comment until
   something checks it.
4. **Using `.values` as if it were a copy.** It is the buffer; measured
   mutation propagated back into the `DataArray`. Use `.copy(deep=True)`.
5. **Interpolating a discontinuous field.** Cubic invented 10.76 m where the data
   have a 100 m step.
6. **Forgetting that `.sel` slices are inclusive** at both ends, so
   `slice(35.0, 40.0)` includes 40.0 and the count is one more than you expect.
7. **Fitting a trend to a series that still contains a seasonal cycle.** Measured
   bias: 0.02133 vs 0.02000, i.e. +6.7 %.
8. **Assuming a monthly climatology has equal month lengths.** Group sizes here
   were 4, 5 and 6.

## 8. Real-world applications

- **Gravity and magnetic compilation.** Merging surveys digitised on different
  grids is an alignment problem; making the join explicit is what stops a
  compilation from silently losing its overlap.
- **Climate anomalies.** Removing a seasonal cycle with `groupby("time.month")`
  is the difference between a trend and a trend contaminated by the calendar.
- **Satellite swath mosaics.** Resampling a swath onto a regular grid is cubic
  *for smooth fields* and linear *across clouds*; the choice is scientific.
- **Potential-field derivatives.** `differentiate` on a labelled axis gives the
  derivative you meant, with the units of value-per-degree rather than
  value-per-index.
- **Multi-model comparison.** Curvilinear ocean model grids carry 2-D coordinate
  variables (`lat(y, x)`), which is where pointwise versus multidimensional
  indexing stops being a convenience and becomes a necessity.

## 9. Further reading

- **Xarray, *User Guide*.** Level: intermediate. <https://docs.xarray.dev> —
  the sections on indexing, alignment, computation and reshaping are the
  reference for everything here.
- **Xarray, *Xarray project site*.** Level: beginner. <https://xarray.dev> — the
  overview and the "coming from pandas" material.
- **Pandas, *Indexing and selecting data*.** Level: beginner.
  The one-dimensional original: labels, alignment and reindexing.
- **Hoyer, S. and Hamman, J. (2017). xarray: N-D labeled arrays and datasets in
  Python. *Journal of Open Research Software*, 5(1), 10.** Level: intermediate.
  The design paper: why names beat positional axes in research code.
- **Unidata, *netCDF4-python documentation*.** Level: reference.
  <https://unidata.github.io/netcdf4-python/> — what happens under
  `xr.open_dataset`.

> Note on citations: bibliographic details are given so you can locate these
> works. This repository does not host or reproduce copyrighted text.

## 10. Related lessons

- [01 netCDF/HDF5 Formats and Self-Describing Data](./01-netcdf-and-hdf5.md) —
  the file this object is loaded from and saved to.
- [03 Dataset, Alignment, Broadcasting and GroupBy](./03-xarray-dataset.md) —
  many variables on shared dimensions, and the `weighted` machinery.
- [04 Chunking with Dask for Out-of-Core Analysis](./04-dask-chunking.md) —
  the same object, with a lazily evaluated backend.
- [05 Case Study: Analysing a Climate Data Cube](./05-climate-data-cube.md) —
  the time-coordinate machinery applied to a four-decade synthetic cube.
- [03-02-03 Broadcasting, Vectorisation and the `axis` Trap](../02-numpy/03-broadcasting.md)
  — the positional version of Section 2.5.

## Exercises

[`exercises/02-xarray-dataarray-exercises.md`](./exercises/02-xarray-dataarray-exercises.md),
with full worked answers in
[`exercises/02-xarray-dataarray-solutions.md`](./exercises/02-xarray-dataarray-solutions.md).

## Self-assessment checklist

- [ ] I can build a `DataArray` with named dims and coordinates in one line.
- [ ] I can say when `.sel` and `.isel` give different answers, and why the label
      answer is the physical one.
- [ ] I can predict the shape of `a + b` for two grids with offsets of half a
      cell, ten cells and zero cells.
- [ ] I can explain the float32-coordinate failure and name two repairs.
- [ ] I can explain broadcasting in terms of names, not shapes.
- [ ] I can quote the measured linear and cubic interpolation errors on a smooth
      field and on a step.
- [ ] I can say what `drop=True` changes and what it does not.
- [ ] I know that `attrs` are propagated unverified, and I have a rule for
      keeping units trustworthy in my own code.
