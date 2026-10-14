---
id: 03-08-06
title: "rasterio: Rasters, Windows, Masks and Reprojection"
level: advanced
prereqs: ["03-08-01", "03-08-02", "03-02-01"]
tags: [rasterio, geotiff, affine-transform, crs, reprojection, windows, nodata]
---

# rasterio: Rasters, Windows, Masks and Reprojection

GeoTIFF is the container of choice for grids that come from an instrument or a
GIS: DEMs, orthophotos, magnetic and radiometric survey grids, satellite
reflectance. It stores an array plus a **geotransform** — six numbers that say
where the array is — plus a coordinate reference system and a no-data value.

Understanding those six numbers is the whole lesson. Every raster bug in
geophysics is a misunderstanding of the transform, the CRS, or the boundary
between them.

> **All values below are measured output from `code/rasterio_rasters_demo.py`.**
> The DEM is SYNTHETIC — a tilted plane, a Gaussian hill and a ripple — with known
> analytic gradients, so every derived slope and every affine computation can be
> checked against an imposed number. Nothing is downloaded and nothing is
> committed: the GeoTIFF is written into a throw-away directory and deleted.

## Learning objectives

By the end of this lesson you will be able to:

1. **Read** a raster's metadata — `crs`, `transform`, `res`, `bounds`, `nodata`,
   `block_shapes`, `dtypes` — and say what each one means.
2. **Use** the affine transform to convert between `(row, col)` and `(x, y)`, and
   explain the half-pixel convention that puts the transform origin on the
   *corner* of the first pixel.
3. **Recover** a known gradient from a raster by dividing finite differences by
   the correct cell size with the correct sign.
4. **Avoid** the `Window(col_off, row_off, …)` argument-order trap, and quantify
   the error it produces.
5. **Handle** `nodata` as a mask rather than as a number, and state the measured
   cost of getting that wrong.
6. **Choose** a decimation resampling method from the statistic you intend to
   compute, with measured differences between `nearest`, `bilinear`, `average`
   and `cubic`.
7. **Reproject** with `rasterio.warp`, compute the ground size of the target
   cell, and explain why a degree is not a distance.
8. **Explain** why slopes, distances and areas computed from degree cells are
   wrong, with the measured anisotropy.

## Prerequisites

- [03-08-01 netCDF/HDF5 Formats and Self-Describing Data](./01-netcdf-and-hdf5.md)
  — the self-describing-data idea, in a different container.
- [03-08-02 xarray DataArray, Coordinates and Labeled Dimensions](./02-xarray-dataarray.md)
  — labelled dimensions; a raster is a labelled grid with an affine label.
- [03-02-01 ndarray Creation, dtypes, Shapes and Strides](../02-numpy/01-ndarray-basics.md)
  — the `(row, col)` array convention the API inherits.

## 1. Intuition: the six numbers under every raster

```
driver = GTiff, count (bands) = 1, dtypes = ('float32',)
size = 500 columns x 400 rows
crs = EPSG:32612  (EPSG:32612)
crs units = metre, geographic = False
transform = (30.0, 0.0, 500000.0, 0.0, -30.0, 4200000.0)
resolution = (30.000, 30.000) m
bounds = (500000.0, 4188000.0, 515000.0, 4200000.0) (left, bottom, right, top)
nodata = -9999.0
block shapes = [(256, 256)]
```

The `transform` is an affine map in six numbers, in the order
`(a, b, c, d, e, f)`:

$$\begin{pmatrix} x \\ y \end{pmatrix}
= \begin{pmatrix} c \\ f\end{pmatrix}
+ \begin{pmatrix} a & b \\ d & e\end{pmatrix}
\begin{pmatrix} \text{col} \\ \text{row}\end{pmatrix}.$$

Here $a = 30$ m (x increases eastward with column), $e = -30$ m (y *decreases*
as row increases: north-up), $c = 500000$ m and $f = 4200000$ m (the origin).
$b = d = 0$ means the grid is axis-aligned — no rotation or shear.

Two immediate consequences, both measured:

```
transform * (0, 0) -> (500000.0, 4200000.0)
transform * (0, 1) -> (500030.0, 4200000.0)
transform * (1, 0) -> (500000.0, 4199970.0)
```

Row 0 is the northernmost row, so the row index runs *southward*. Column index
runs eastward. A raster stored bottom-up (some formats, some instruments) will
have $e > 0$, and every slope computed from it will be mirrored.

## 2. The half-pixel convention

`transform * (0, 0)` gives a coordinate. Is that the *centre* of pixel (0, 0) or
its *upper-left corner*? The answer is the corner, always, and getting it wrong
moves every sample by half a cell:

```
the ORIGIN (c, f) is the upper-left CORNER of pixel (0, 0)
the CENTRE of pixel (row=0, col=0) is at (500015.0, 4199985.0), i.e. half a pixel
  in from the corner: (+15.0, -15.0) m
rasterio's own helper: src.xy(0, 0) = (500015.0, 4199985.0)
and with offset='ul' it returns the corner: (500000.0, 4200000.0)
```

So the affine that maps *pixel centres* to coordinates is the same matrix with
$c' = c + a/2$ and $f' = f + e/2$ — a half-pixel shift. The demonstration's
generator avoids this class of error by construction: it builds the field from
pixel-centre coordinates,

$$x_j = x_0 + (j + \tfrac12)\Delta x, \qquad
  y_i = y_0 - (i + \tfrac12)\Delta y,$$

which is the only way to write a raster whose pixel values are samples of a
continuous function. For this 30 m DEM the half-pixel shift is 15 m, and a 15 m
horizontal misregistration is a vertical error of $15 \times \text{slope}$. On a
20° slope that is 5.5 m of elevation error — comparable to the vertical accuracy
claimed for many DEM products. This is why the convention is stated in every
raster standard: the ambiguity is not pedantry, it is 5 metres of DEM.

## 3. Recovering a gradient through the transform

Given the raster, the gradient is

$$\frac{\partial z}{\partial x} = \frac{1}{a}\frac{\partial z}{\partial \text{col}},
\qquad
\frac{\partial z}{\partial y} = \frac{1}{e}\frac{\partial z}{\partial \text{row}}
= -\frac{1}{|e|}\frac{\partial z}{\partial \text{row}},$$

with the minus sign coming from the north-up row convention. The demonstration
checks both against the analytic gradient of the synthetic surface it generated:

```
max |dz/dx error| = 1.390e-02 m/m
max |dz/dy error| = 9.749e-03 m/m
median |dz/dx error| = 8.235e-04 m/m
at (row=350, col=200): dz/dx = 0.053307 vs analytic 0.053998 (error -6.91e-04)
                       dz/dy = 0.038439 vs analytic 0.038310 (error +1.30e-04)
slope: raster mean = 3.463 deg, max = 13.232 deg; analytic max = 13.109 deg
```

Three things to take from this. First, the median error is 8 × 10⁻⁴ m/m, which is
the central-difference truncation error $O(\Delta^{2} z''')$ — the transform is
being applied correctly. Second, the *maximum* error is 1.4 × 10⁻² m/m, one
order of magnitude larger, and it occurs where the 90 m ripple is sampled at
30 m: the error is **aliasing**, not affine arithmetic. Third, the mean slope from
the raster is 3.463° and the analytic maximum is 13.109° against the raster's
13.232°: a 0.9 % overestimate from finite differencing on a curved surface.

The imposed plane gradient is $(0.02000, 0.03500)$ and the ridge and hill add up
to 0.1737 m/m on top of it — so a "gradient check" that only looked at the plane
would have validated nothing about the interesting part of the field.

## 4. Windows: the argument order that bites everybody

`rasterio.windows.Window` takes `(col_off, row_off, width, height)`. Note the
order: **column first**. Arrays are indexed `[row, col]`. Measured:

```
correct: shape (rows, cols) = (60, 80), mean = 99.95 m, top-left centre = (503015, 4198485)
swapped: shape (rows, cols) = (60, 80), mean = 17.50 m, top-left centre = (501515, 4196985)
the two windows share no pixel: their origins differ by (-1500, +1500) m
max |difference| = 102.74 m
```

The two windows have the *same shape*, return without error, and contain
completely different terrain: a 102.74 m difference in elevation. A window bug
does not announce itself; it produces a plausible crop of the wrong place.

A second, subtler trap: a window built from geographic bounds has fractional
offsets, and `int(win.width)` truncates. Measured in the vector–raster lesson,
where the polygon bounds gave a 133.333-pixel window:

```
int(win.height) x int(win.width) = 133 x 133 = 17,689 pixels
full grid: 18,090 pixels with all_touched=True
```

Truncating to an integer window silently dropped 401 rim pixels — 2.27 % of the
polygon — because the fractional last column and row lie outside. `read(window=...)`
rounds outward, so the *array* is complete; the *mask* built against the truncated
shape is not. When boundary pixels matter, rasterise on the full grid.

## 5. `nodata` is a mask, not a number

```
masked read: type = MaskedArray, masked cells = 600 (0.30 %)
an UNMASKED read returns -9999 in that corner
mean with masking = 42.659 m; mean without = 12.534 m (difference 30.125 m)
```

0.30 % of the grid is missing, and honouring the mask changes the mean elevation
by **30.125 m** — larger than most terrain corrections. The mechanism is that
$-9999$ is a number like any other and drags the arithmetic mean down by roughly
$0.003 \times 10{,}000$ m. Two habits:

- Read with `masked=True` whenever a `nodata` value is declared, and check
  `arr.mask.sum()` against your expectation. A mask of 0 % on a satellite scene
  is a red flag, not a clean scene.
- Never use a sentinel that is a legal value. `nodata = 0` on an elevation grid
  is a defect: 0 m is sea level and it is inside the valid range.

And note the third option: a *separate* mask band. CF and GeoTIFF both support
"mask as its own band", which keeps the sentinel out of the data entirely and is
the only approach that survives a median filter or an interpolation that is
allowed to touch every value.

## 6. Decimation: four resampling methods, four answers

Reading a 30 m raster at 120 m involves a choice, and the choice changes the
statistic. Measured against a true 4×4 block mean:

| Method | mean (m) | max |difference| from block mean (m) | rms (m) | std (m) |
|---|---|---|---|---|
| `average` | 42.672 | 0.000 | 0.000 | 149.778 |
| `cubic` | 42.672 | 0.608 | 0.191 | 149.786 |
| `bilinear` | 42.696 | 1.179 | 0.281 | 149.713 |
| `nearest` | 42.447 | 3.842 | 0.830 | 149.793 |
| true 4×4 block mean | 42.645 | — | — | 149.802 |

`average` reproduces the block mean **exactly** (max difference 0.000 m), which is
what a conservation-minded workflow needs. `cubic` is within 0.6 m, `bilinear`
within 1.2 m, `nearest` within 3.8 m — and `nearest` does not smooth at all
(std 144.985 m before and after, against 144.968 m for `average`), so it keeps
every artefact of the original sampling while discarding 93.75 % of the values.

One more measured consequence: with `resampling=nearest`, 15 of every 16 source
pixels are **never read**. If those pixels contained the anomaly you are looking
for — a single-cell mineralised intersection, a bad instrument reading — nearest
resampling removes it before you see it.

The rule: **`average` for statistics and conservation, `bilinear` for smooth
fields and visual display, `nearest` for categorical data (land cover,
classification, masks), and `cubic` when the field is smooth and the output grid
is a resampling rather than a summary.**

## 7. Reprojection: degrees are not metres

```
source: EPSG:32612, 500 x 400 px at 30 m
target: EPSG:4326, 541 x 343 px at (0.000315, 0.000315) deg
reprojected: valid cells = 185,019 (99.7 % of the target grid)
at the centre (-110.9147 E, 37.8935 N) one target cell is:
  0.000315 deg of latitude  = 35.01 m of ground distance
  0.000315 deg of longitude = 27.74 m of ground distance
both axes are nominally 'the same' pixel size in degrees, yet on the ground
they differ by 20.75 % at the centre
  a cell of 0.000315 deg of longitude is 27.74 m at 37.9 N
  a cell of 0.000315 deg of longitude is 33.01 m at 20.0 N
  a cell of 0.000315 deg of longitude is 22.61 m at 50.0 N
  a cell of 0.000315 deg of longitude is 12.04 m at 70.0 N
```

This is the arithmetic of the whole lesson. A geographic CRS has **degrees** on
both axes, so a square cell in coordinate space is a rectangle on the ground:

- north–south, one degree is nearly constant: 35.01 m here, and it changes only
  through the ellipsoid's curvature (±0.1 % over a few degrees of latitude);
- east–west, one degree is $1/\cos\phi$ times larger than north–south, so the
  same-degree cell shrinks from 27.74 m at 37.9°N to 12.04 m at 70°N — a factor
  of 2.3 across that range.

**Consequences, each measurable in the same demo:**

- A distance computed as $\sqrt{\Delta\text{lon}^2 + \Delta\text{lat}^2}$ has no
  units and no meaning.
- A slope computed from `np.gradient` on a degree grid treats 27.74 m and 35.01 m
  as the same length. Measured: the *isotropic* assumption gives a mean slope of
  3.096° against the correct 3.449°, a mean bias of −0.353° and a **maximum bias
  of 2.124°**, with the aspect changing by up to 6.65°.
- An area in square degrees is not an area. In the companion lesson the same box
  measured 36.0000 km² in UTM and 36.0815 km² geodesically: a −0.2259 % UTM scale
  factor error. That is small, and it is *bounded* only because UTM's scale factor
  is known; square degrees have no such bound.

The reprojected array also spans a slightly different footprint than the source
(99.7 % of target cells valid), and its value range extends to −326.30 m and
404.23 m, beyond the source plane's range: **reprojection extrapolates at the
edges**, and edge values are the first thing to check in any reprojected product.

### 7.1 What to do instead

1. Work in a projected CRS with metre units whenever you compute a distance,
   slope, area or buffer, and check that the points lie inside the projection's
   design domain (a UTM zone is 6° wide).
2. If a product must be in degrees, convert locally:
   $\Delta x = R\cos\phi \cdot \Delta\lambda \cdot \pi/180$ and
   $\Delta y = M(\phi) \cdot \Delta\phi \cdot \pi/180$ with the meridional radius
   of curvature $M$. For the demonstration's centre, $R\cos\phi = 87{,}900$ m/deg;
   the correct value is 27.74 m per 0.000315°, i.e. 88,063 m/deg — the difference
   between a spherical and an ellipsoidal radius, a further 0.2 %.
3. Prefer an equal-area CRS (e.g. EPSG:6933) when area is the quantity of
   interest; its areal scale factor is exactly 1 (measured in
   [09-05 Cartopy: Map Projections and Geographic Plotting](../09-geospatial-python/05-maps-cartopy.md)).

## 8. Units and dimensional analysis

- **`res` is in CRS units.** `(30.000, 30.000)` means metres because the CRS is
  projected; the printed `crs units = metre, geographic = False` is the evidence.
  After reprojection to EPSG:4326 the same attribute reads degrees and the
  arithmetic above shows why it must not be used as a length.
- **`bounds` is in CRS units too,** ordered `(left, bottom, right, top)`.
  For a 500 × 400 raster at 30 m: right − left = 15,000 m and top − bottom =
  12,000 m, matching $500 \times 30$ and $400 \times 30$. That identity is a useful
  assertion to write: `width * res == right - left`.
- **`nodata` must be in the data's dtype and outside the valid range.** For
  float32 with elevations in metres, −9999.0 works; for int16 codes, use the
  dtype's extreme value and document it.
- **`_FillValue` versus `nodata`.** The two names mean the same thing in different
  containers (NetCDF/CF versus GDAL/GeoTIFF). A conversion between them is a
  metadata translation, and losing it is one of the most common interop bugs.

## 9. Python demonstration

The full script is
[`code/rasterio_rasters_demo.py`](./code/rasterio_rasters_demo.py):

```bash
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python \
    03-scientific-computing/08-gridded-geospatial-data/code/rasterio_rasters_demo.py
```

It writes one GeoTIFF into a throw-away directory inside the module and deletes it
on exit. `pyproj` supplies the geodesic distances used to convert degrees to
metres.

### What to observe, and why it matters

| Observation | Consequence |
|---|---|
| `transform * (0,0)` is a pixel *corner* | the half-pixel convention costs 15 m here |
| `e = -30` (negative) | row index runs south; a missed sign mirrors the terrain |
| raster gradient matches the analytic gradient to 8 × 10⁻⁴ m/m | the affine is being used correctly |
| the max gradient error is 1.4 × 10⁻² m/m | that residual is aliasing, not affine error |
| swapped `Window` arguments give a 102.74 m difference | a window bug returns the wrong crop, silently |
| `nodata` changes the mean by 30.125 m | masking is metadata with metre-scale consequences |
| `average` matches a block mean exactly | conservation needs the right method |
| `nearest` never reads 15 of 16 pixels | decimation can delete the anomaly |
| one degree cell is 27.74 m east–west and 35.01 m north–south | square-in-degrees is not square on the ground |
| isotropic slope bias reaches 2.124° | a slope map in degrees is not a slope map |

> **Breaking exercise.** Before running, set the DEM's origin to
> `(X0 + 15.0, Y0 - 15.0)` while leaving the analytic field unchanged, and predict
> whether the recovered gradient changes by 1 % or by 100 %. Then run it.

## 10. Common mistakes

1. **Treating the transform origin as a pixel centre.** Measured consequence:
   15 m here, and slope × 15 m in elevation.
2. **Omitting the minus sign for `dz/dy`.** The row index runs south; the map
   comes out mirrored and nothing raises.
3. **Swapping `Window` arguments.** Same shape, different place, 102.74 m of
   difference.
4. **Truncating a fractional window.** 401 rim pixels lost, 2.27 % of the polygon.
5. **Ignoring `nodata`.** 30.125 m of spurious mean elevation on a grid that is
   0.30 % missing.
6. **Using `nearest` to summarise a continuous field.** 15 of 16 pixels unread.
7. **Computing slope or distance from a degree grid.** Up to 2.124° of slope bias
   and 20.75 % of cell anisotropy at the demonstration's latitude.
8. **Assuming a reprojected product covers the same area.** 99.7 % valid, with
   extrapolated edges.
9. **Trusting `bounds` without an assertion.** Check
   `width * res == right - left` in metres.

## 11. Real-world applications

- **DEM differencing.** Glacial and volcanic elevation change from repeat DEMs:
  the whole signal is a subtraction of two rasters, so coregistration at the
  half-pixel level is the dominant error term.
- **Airborne magnetics and radiometrics.** Survey grids ship as GeoTIFF with
  `nodata` between flight lines; the tie-line levelling and the gap fraction are
  metadata you must read.
- **Satellite reflectance products.** Banded GeoTIFFs with per-band scale factors
  and offsets, and a QA band that is a mask — the packed-and-masked pattern of
  lesson 01 in another format.
- **Soil, land-cover and geology maps.** Categorical rasters, where `nearest` is
  the only defensible resampling and a bilinear average of two classes is
  meaningless.
- **Slope and aspect products.** Computed by national agencies in a projected CRS
  and reprojected to degrees for delivery; the original metre-based values are the
  ones to use for modelling.

## 12. Further reading

- **Rasterio, *Documentation*.** Level: intermediate.
  <https://rasterio.readthedocs.io> — the windows, transforms, masks, resampling
  and `warp` pages, with worked examples.
- **GDAL, *Documentation*.** Level: advanced. <https://gdal.org> — the library
  under rasterio: geotransform, `nodata`, and the resampling kernel definitions.
- **PROJ, *Documentation*.** Level: advanced. <https://proj.org> — projection
  definitions, transformation pipelines, and why a datum shift is not a
  projection.
- **EPSG.io.** Level: reference. <https://epsg.io> — look up any CRS code,
  including its units and area of use; check that your data lie inside it.
- **van der Walt, S. et al. / GDAL development team, *Resampling methods*.** Level:
  intermediate. The kernel descriptions behind `average`, `bilinear`, `cubic`
  and `nearest`; useful before choosing one for a quantitative product.

> Note on citations: bibliographic details are given so you can locate these
> works. This repository does not host or reproduce copyrighted text.

## 13. Related lessons

- [01 netCDF/HDF5 Formats and Self-Describing Data](./01-netcdf-and-hdf5.md) —
  the same self-describing idea with a different metadata model.
- [02 xarray DataArray, Coordinates and Labeled Dimensions](./02-xarray-dataarray.md)
  — labelled grids in memory; rasters carry the label in six numbers.
- [09-02 GeoDataFrame, CRS Handling and Spatial Joins](../09-geospatial-python/02-geopandas-basics.md)
  — the vector side of the same CRS arithmetic.
- [09-04 Raster-Vector Integration and Zonal Statistics](../09-geospatial-python/04-vector-raster-ops.md)
  — masking, sampling and zonal statistics on top of this API.
- [09-05 Cartopy: Map Projections and Geographic Plotting](../09-geospatial-python/05-maps-cartopy.md)
  — projection scale factors measured directly.

## Exercises

[`exercises/06-rasterio-rasters-exercises.md`](./exercises/06-rasterio-rasters-exercises.md),
with full worked answers in
[`exercises/06-rasterio-rasters-solutions.md`](./exercises/06-rasterio-rasters-solutions.md).

## Self-assessment checklist

- [ ] I can write the affine equations for `x` and `y` from a raster's
      `transform`.
- [ ] I can convert between pixel centres and pixel corners and state the
      half-pixel offset.
- [ ] I can recover `dz/dx` and `dz/dy` from a raster with the correct cell sizes
      and signs.
- [ ] I can state the `Window` argument order and describe the failure mode of
      getting it wrong.
- [ ] I can explain why `nodata` must be honoured and quote the measured cost of
      ignoring it.
- [ ] I can choose a resampling method from the statistic I intend to compute.
- [ ] I can compute the ground size of a degree cell at a given latitude.
- [ ] I can say what reprojection does at the edges of a raster.
