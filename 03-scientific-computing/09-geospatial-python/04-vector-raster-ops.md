---
id: 03-09-04
title: "Raster-Vector Integration and Zonal Statistics"
level: advanced
prereqs: ["03-09-02", "03-09-03", "03-08-06"]
tags: [zonal-statistics, rasterize, rasterio, geopandas, masking, resolution, sampling]
---

# Raster-Vector Integration and Zonal Statistics

Most geophysical questions arrive in two data models at once. The measurement is a
raster (a DEM, an anomaly grid, a reflectance band); the region it belongs to is a
vector (a catchment, a lease, a survey block). **Zonal statistics** is the bridge:
one number, or a set of numbers, per polygon, computed from the raster.

The bridge has three load-bearing parts, and each has a measured cost when it is
built wrong: the **boundary rule** (which pixels belong to a polygon), the
**sampling rule** (what a point lookup returns), and the **resolution rule** (what
changing the cell size does to the answer).

> **Every number below is measured output from
> `code/vector_raster_ops_demo.py`.** The raster is SYNTHETIC — a plane, a ridge, a
> basin and a 90 m ripple on a 30 m grid in UTM zone 12N — and the four survey
> blocks are synthetic rectangles deliberately offset 17 m from the pixel grid so
> that no polygon edge is aligned with a cell boundary.

## Learning objectives

By the end of this lesson you will be able to:

1. **Layer** a raster and a vector onto each other and state which CRS governs.
2. **Sample** a raster at a point, say which pixel it returns, and quantify the
   relocation error.
3. **Mask** a polygon onto a raster with `geometry_mask`, and explain the
   `all_touched` flag with measured consequences.
4. **Rasterise** polygons to an integer label grid and check the pixelated areas
   against the true polygon areas.
5. **Compute** zonal statistics with a loop and with a single grouped reduction,
   and show they agree.
6. **Reconstruct** the same statistics from a spatial index and a quadrat count.
7. **Quantify** the sensitivity of zonal statistics to cell size, and separate
   what is conservative from what is not.
8. **Report** three defensible "mean values" for the same raster and explain how
   they differ by 16 m.

## Prerequisites

- [03-09-02 GeoDataFrame, CRS Handling and Spatial Joins](./02-geopandas-basics.md)
  — the polygon side, and why a projected CRS is required.
- [03-09-03 Spatial Indexing, Spatial Joins and Performance](./03-spatial-indexing.md)
  — the alternative (index-based) route to the same statistics.
- [03-08-06 rasterio: Rasters, Windows, Masks and Reprojection](../08-gridded-geospatial-data/06-rasterio-rasters.md)
  — the transform, windows, windows-vs-array indexing, and `nodata`.

## 1. The two grids that are not the same grid

The raster is a 30 m lattice in EPSG:32612 whose pixel centres are at
$x_0 + (j + \tfrac12)\Delta$ and $y_0 - (i + \tfrac12)\Delta$. The polygons are
arbitrary geometry in the same CRS. They agree on the *plane* and on nothing else:

```
raster: 800 x 600 px at 30 m, crs EPSG:32612, nodata -9999.0
extent: 500,000 .. 524,000 E, 4,182,000 .. 4,200,000 N
pixels = 480,000, cell area = 900 m^2 = 0.000900 km^2
polygons: 4 blocks, areas [8.0, 24.0, 16.0, 60.0] km^2
the blocks are offset by 17 m from the pixel grid on purpose: no polygon edge
lies on a pixel boundary, so the boundary rule has to be decided rather than
ignored
```

A 30 m pixel is 0.000900 km², so a 16 km² block "contains" at most
$16 \times 10^{6}/900 = 17{,}778$ pixels. The measured counts are 17,689 with the
centre rule and 18,090 with `all_touched` — both near the bound, and 401 pixels
apart, which is the entire subject of Section 3.

## 2. Point sampling

```
ST00 at (501,000, 4,196,000): nearest = 192.668 m, bilinear = 194.346 m,
                              analytic = 193.584 m
ST01 at (501,400, 4,196,000): nearest = 197.537 m, bilinear = 198.022 m,
                              analytic = 198.886 m
ST02 at (501,800, 4,196,000): nearest = 195.979 m, bilinear = 199.394 m,
                              analytic = 199.200 m
max |nearest  - analytic| = 3.248 m
max |bilinear - analytic| = 1.569 m
```

Three things to read from this.

**The analytic column is the truth**, because the surface is a known function. The
sampling errors are metres, not centimetres, and the reason is stated in the
output: the surface carries a 90 m ripple and the grid samples it only three times
per cycle. Sampling error is a property of the field's roughness relative to the
grid, not of the interpolation routine.

**`rasterio`'s `sample()` has no `resampling` argument.** It always returns the
containing pixel. The demonstration's "bilinear" column is four-neighbour
interpolation written out by hand — which is what every library does internally,
and which is worth writing once so that the half-pixel convention becomes
concrete.

**The relocation error is bounded but real:**

```
at (501,395.0, 4,199,775.0) and 10 m east: 205.110077 and 205.110077
                            -- identical, same pixel
at 30 m east: 208.78511 -- a step of +3.675 m at the pixel edge
```

Ten metres inside a pixel returns the identical value (piecewise constant); one
pixel to the east returns a value 3.675 m different. The requested coordinate is
effectively snapped to the pixel centre, up to $30/\sqrt{2} = 21.2$ m away, and
that horizontal error becomes a vertical error of $21.2 \times \text{slope}$. On a
30 m DEM with a 20° slope that is 7.7 m of elevation error — larger than the
nominal vertical accuracy of most DEMs.

The rule for point sampling: **if the field is smoother than the grid, nearest is
fine and cheap; if it is not, interpolate — and if the point location matters at
all, work out the bound above and state it.**

## 3. The boundary rule: `all_touched`

A polygon edge rarely falls on a pixel boundary, so every pixel on the rim is
partly in and partly out. Two conventions:

- **centre rule** (`all_touched=False`, the default): a pixel belongs to the
  polygon if its *centre* is inside;
- **`all_touched=True`**: a pixel belongs if *any* part of it is inside.

Measured on the four blocks (offset 17 m from the grid deliberately):

| Block | centre pixels | centre area | `all_touched` pixels | all-touched area | polygon area |
|---|---|---|---|---|---|
| B1 (ridge) | 8,911 | 8.0199 km² | 9,112 | 8.2008 km² | 8.0000 km² |
| B2 (basin) | 26,600 | 23.9400 km² | 26,934 | 24.2406 km² | 24.0000 km² |
| B3 (plain) | 17,689 | 15.9201 km² | 18,090 | 16.2810 km² | 16.0000 km² |
| B4 (mixed) | 66,800 | 60.1200 km² | 67,134 | 60.4206 km² | 60.0000 km² |

```
the two boundary rules change the pixel count by up to 401 pixels (2.27 %)
and the mean by up to 0.6377 m
```

Two lessons, one surprising.

**The centre rule is unbiased on average and wrong per polygon.** Its area errors
are +0.249 %, −0.250 %, −0.499 %, +0.200 %: both signs, magnitudes set by how the
specific polygon edges cut the specific pixels. `all_touched` is biased *upward*
for every block, because it counts every partial pixel in full.

**The mean is barely affected on smooth terrain and can be badly affected on
rough terrain.** Here the largest mean shift is 0.6377 m on a field whose
standard deviation inside the block is 49.48 m — 1.3 %. But the rim pixels are not
a random sample: on a DEM, the pixels along a polygon boundary are exactly where
the extremes live (a scarp, a coastline, a cliff). The internal variability here
is dominated by the ridge, not by the edges, which is why the shift is small. On a
fault-scarp DEM, the same 2.27 % of pixels can move the mean by metres.

**The decision procedure.** Ask what the polygon means:

- A **lease or survey block** with legal boundaries: the boundary pixels are
  genuinely ambiguous, so report the statistic under both rules, or report the
  difference as a systematic uncertainty.
- A **catchment** whose boundary follows a ridge: `all_touched` for a maximum,
  the centre rule for a mean, and say which.
- A **land-cover class** where partial pixels have a known fractional mix:
  neither rule is right; the correct object is the fractional coverage
  (`rasterio.features.rasterize` with `merge_alg` and fractional masks, or a
  resampling of the class fractions).

## 4. Window mechanics, and the two bugs that live there

```
window from the polygon bounds: col_off = 33.900, row_off = 400.567,
  size = 133.333 x 133.333 px
read() rounds the window outward: shape = (133, 133)
pixels whose CENTRE is inside: 17,689 = 15.9201 km^2 against a polygon area of
  16.0000 km^2 (-0.499 %)
the window transform is not the raster transform: its origin is
  the window's corner, (501017.0, 4187983.0) instead of (500000.0, 4200000.0)
```

**Bug one: using the raster transform with a windowed array.** The polygon then
lands 1,017 m east and 12,017 m south of where it belongs, and the mask selects
terrain from the wrong part of the raster — with no error, because the shapes
still match. Always use `src.window_transform(win)` for a windowed read.

**Bug two: truncating a fractional window.** The window is 133.333 pixels wide, so
`int(win.width) = 133` cuts a third of a column:

```
full grid       : centre rule 17,689 px, all_touched 18,090 px
window 133x133  : centre rule 17,689 px, all_touched 17,689 px
the centre rule survives truncation unchanged (True),
but all_touched loses 401 rim pixels (2.22 %)
```

The centre rule is insensitive to the cut because no pixel *centre* lies in the
lost 0.33 column; `all_touched` is sensitive because the cut column contained 401
partially covered pixels. **`read(window=...)` rounds outward** (so the array is
complete), but a mask built against a truncated `out_shape` is not. `rasterise` on
the full grid, or round the window outward before masking.

## 5. Rasterising the polygons

The third route makes the raster itself carry the regions:

```
rasterize -> integer label per pixel on the 800 x 600 grid
label 0 (no block): 360,000 pixels (75.00 % of the raster)
label 1 (B1): 8,911 pixels = 8.0199 km^2 vs polygon area 8.0000 km^2 (+0.249 %)
label 2 (B2): 26,600 pixels = 23.9400 km^2 vs polygon area 24.0000 km^2 (-0.250 %)
label 3 (B3): 17,689 pixels = 15.9201 km^2 vs polygon area 16.0000 km^2 (-0.499 %)
label 4 (B4): 66,800 pixels = 60.1200 km^2 vs polygon area 60.0000 km^2 (+0.200 %)
```

Rasterising turns a geometry question into an array question, and the array
question is the one that is fast. The area quantisation error — at most 0.499 %
here — is the price. It is predictable: a polygon boundary crossing $P$ pixels
introduces an error of order $\pm P \times \text{cell area}/2$, and the error
shrinks linearly with cell size. At 30 m on a 4 km block, $P \approx 4 \times
133 = 532$ pixels, so the expected error magnitude is
$532 \times 900/2 \approx 2.4 \times 10^{5}$ m² = 0.24 km², i.e. 1.5 % of a
16 km² block — the measured 0.499 % is smaller because the boundary is axis-aligned
and cuts only the two directions.

Note also the **75.00 % of the raster that belongs to no block**: 360,000 pixels
of terrain that no polygon covers. A "mean elevation of the survey" computed over
the whole raster includes it.

## 6. Two implementations, one answer

**The loop** (per polygon: window, mask, statistics) gives, for each block, the
table in Section 3. **The grouped reduction** works on the whole raster:

```
120,000 labelled pixels grouped with one stable sort
block 1:  8,911 px, mean = 340.7775 m, std = 49.4783 m, min = 247.273, max = 413.604
block 2: 26,600 px, mean = 190.9798 m, std = 26.9827 m, min = 133.948, max = 258.693
block 3: 17,689 px, mean = 184.2993 m, std =  5.9070 m, min = 169.125, max = 202.267
block 4: 66,800 px, mean = 240.0494 m, std = 12.0314 m, min = 212.900, max = 269.188
compared with Section 4, the largest per-block disagreement is 0.00e+00 m
```

Exactly the same numbers, from one stable sort plus a `searchsorted` — no
per-polygon loop, no window arithmetic, no boundary subtlety. This is the pattern
every fast zonal-statistics library uses, and it is worth implementing once to
understand why the library is fast:

```python
order = np.argsort(flat_labels, kind="stable")
bounds = np.searchsorted(flat_labels[order], np.unique(flat_labels))
for i, lo in enumerate(bounds):
    hi = bounds[i + 1] if i + 1 < len(bounds) else order.size
    chunk = flat_values[order][lo:hi]
    ...  # mean, std, min, max, percentiles
```

For percentiles and medians, the sorted array is already half the work.

## 7. What resolution does

```
1x coarser (   30 m cells): 17,689 pixels, mean = 184.3289 m (+0.0000 m), std = 5.6952 m, pixel-area / block-area = 0.995
2x coarser (   60 m cells):  4,356 pixels, mean = 184.3289 m (+0.0000 m), std = 5.5817 m, pixel-area / block-area = 0.980
4x coarser (  120 m cells):  1,089 pixels, mean = 184.3289 m (+0.0000 m), std = 5.5747 m, pixel-area / block-area = 0.980
8x coarser (  240 m cells):    256 pixels, mean = 184.3289 m (+0.0000 m), std = 5.5713 m, pixel-area / block-area = 0.922
```

Three separate behaviours, and it is important not to conflate them.

**The mean is conservative: 184.3289 m at every resolution, to 0.0000 m.** Block
averaging a smooth field and then area-weighting commutes, so a coarsened mean is
the same mean. This is the strongest result in the section and the reason
downsampling is usually safe for a regional average.

**The spatial variability falls, but only partly.**
$\sqrt{5.6952^{2} - 5.5713^{2}} = 1.1817$ m of the standard deviation was removed
by the coarsening — that is the 90 m ripple, which the 240 m cells average away.
The rest of the 5.57 m is the 4 km-scale slope inside the block, which no cell
size removes. **If you report a standard deviation from a coarse raster, say what
part of the variability it represents.**

**The polygon-area estimate drifts by up to 7.8 %.** `pixel-area / block-area`
falls from 0.995 to 0.922 as cells grow, because a coarse cell is either in or out
of the polygon: at 240 m, 256 pixels cover 14.75 km² of a 16 km² block. This is
the same quantisation error as in Section 5, with the cell area $64\times$ larger.
**Areas from a coarse raster are systematically uncertain at the several-per-cent
level, and the uncertainty is not random.**

## 8. Three defensible "mean elevations"

```
block     mean_m    area_m2
   B1 340.777496  8019900.0
   B2 190.979797 23940000.0
   B3 184.299301 15920100.0
   B4 240.049393 60120000.0
mean of the block means            = 239.0265 m
area-weighted mean of the blocks   = 228.4342 m
mean of every finite raster pixel  = 244.7617 m
```

| Statistic | Value | Answers the question |
|---|---|---|
| mean of block means | 239.0265 m | "what is the average of my four survey blocks?" |
| area-weighted mean of blocks | 228.4342 m | "what is the mean elevation of the surveyed area?" |
| mean of every raster pixel | 244.7617 m | "what is the mean elevation of this raster?" |

The spread between the first two is 10.59 m (1059.2 cm), driven by the 7.5×
difference in block area; the third differs by a further 16.33 m because the
raster covers terrain — the ridge, the basin, the 75 % of pixels outside every
block — that no block includes.

All three are in metres, all three are correct, and only one answers the question
you were asked. **State the areal support of any mean**, which means stating the
region, the mask and the weighting.

## 9. Units and dimensional analysis

- **A pixel is an area.** 30 m × 30 m = 900 m² = 0.000900 km². Every count is
  convertible to an area by multiplying, and every area is convertible to a count
  by dividing. Section 5's 0.499 % is the count-to-area error.
- **`all_touched` changes the area, not just the count.** The 401 extra pixels are
  0.3609 km², which is 2.26 % of B3. Counting them in full is a deliberate
  over-estimate.
- **Weights must be dimensionless or consistently scaled.** An unweighted mean of
  block means uses a weight of 1 per block, i.e. it weights each block by
  $1/\text{area}$. That is a statement about the analysis, not a neutral default.
- **Distance and area in a projected CRS are metric, to the scale factor.** UTM's
  $k \approx 0.9996$ makes an area error of order $2(k-1) = -0.08$ %, which is
  small compared with the 0.499 % boundary quantisation and much smaller than a
  degree-based error would be.
- **Sampling error scales with slope × cell size.** The 21.2 m worst-case
  relocation is a *length*, and it becomes a *height* only through a slope, which
  is dimensionless.

## 10. Python demonstration

The full script is
[`code/vector_raster_ops_demo.py`](./code/vector_raster_ops_demo.py):

```bash
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python \
    03-scientific-computing/09-geospatial-python/code/vector_raster_ops_demo.py
```

It writes one GeoTIFF into a throw-away directory inside the module and deletes it
on exit.

### What to observe, and why it matters

| Observation | Consequence |
|---|---|
| sampling error is 3.248 m (nearest) and 1.569 m (bilinear) | the field's roughness, not the interpolator, sets the error |
| 10 m east is identical; 30 m east steps by 3.675 m | a point lookup is a pixel lookup |
| the 133.333-pixel window truncates to 133 | masks from truncated shapes lose rim pixels |
| `all_touched` adds 401 pixels to a 16 km² block | a 2.27 % area difference from one keyword |
| the mean shifts by up to 0.6377 m between rules | small on smooth terrain, not on rough |
| pixelated areas are within 0.499 % of true areas | rasterisation quantises area by ~1 cell per boundary pixel |
| the loop and the grouped reduction agree to 0.00e+00 m | fast zonal statistics is a sort plus a searchsorted |
| the mean is resolution-invariant, the std is not | block averaging is conservative; variability is not |
| the polygon-area estimate drifts by 7.8 % at 8× coarsening | coarse rasters have per-cent area uncertainty |
| three "mean elevations" differ by 10.59 m and 16.33 m | the areal support is part of the answer |

> **Breaking exercise.** Before running, set the raster cell size to 90 m
> (changing `RES` and `NCOL`/`NROW` so the extent is unchanged) and predict
> whether the area quantisation error grows or shrinks. Then measure the four
> pixelated areas and compare them with the 30 m values.

## 11. Common mistakes

1. **Using the raster transform for a windowed array.** The polygon lands 1,017 m
   east and 12,017 m south, with no error raised.
2. **Truncating a fractional window.** 401 rim pixels lost, 2.27 % of the block.
3. **Reporting a zonal statistic without the boundary rule.** The two rules differ
   by 2.27 % in area and up to 0.6377 m in mean here, and by much more on a scarp.
4. **Assuming `all_touched` is more accurate.** It is a *different* estimate, and
   it is biased upward for every block measured.
5. **Using `sample()` for a smooth field.** It is piecewise constant, with up to
   21.2 m of relocation error.
6. **Comparing a coarse-raster area with a polygon area.** Up to 7.8 % here at 8×
   coarsening.
7. **Quoting "the mean" without the areal support.** The three defensible values
   differ by up to 16.33 m.
8. **Forgetting that `nodata` pixels are excluded from some operations and not
   others.** Count them explicitly, as in
   [03-08-06 rasterio: Rasters, Windows, Masks and Reprojection](../08-gridded-geospatial-data/06-rasterio-rasters.md).

## 12. Real-world applications

- **Glacier and ice-cap mass balance.** Elevation change from repeat DEMs,
  averaged over glacier outlines; the outline convention is the boundary rule and
  it is a published methodological choice.
- **Catchment rainfall and runoff.** Area-averaged precipitation from a gridded
  product over catchment polygons; the aggregation is definitionally
  area-weighted.
- **Mineral resource and grade estimation.** Block averages from a drill-hole
  raster over mining leases, where the lease boundary is a legal object.
- **Land-cover change.** Fractional coverage per administrative unit, where
  `all_touched` and fractional rasterisation give different numbers and the
  fractional one is right.
- **Exposure and risk.** Population or asset value summed over hazard polygons;
  the sum is exact and only the *areal* statistics need a boundary rule.

## 13. Further reading

- **Rasterio, *Documentation*: `rasterio.features`.** Level: intermediate.
  <https://rasterio.readthedocs.io> — `geometry_mask`, `rasterize`, `shapes` and
  the `all_touched` parameter.
- **GeoPandas, *Documentation*.** Level: intermediate. <https://geopandas.org> —
  the vector side: CRS handling, clipping and joining.
- **GDAL, *Documentation*.** Level: advanced. <https://gdal.org> — the rasterise
  implementation and its boundary semantics.
- **Xarray, *Documentation*.** Level: intermediate. <https://docs.xarray.dev> —
  `groupby` and `weighted` for the reduction-based route.
- **Samet, H. (1990). *The Design and Analysis of Spatial Data Structures*.** Level:
  advanced. The grid-hash and quadtree theory behind "rasterise instead of index".

> Note on citations: bibliographic details are given so you can locate these
> works. This repository does not host or reproduce copyrighted text.

## 14. Related lessons

- [03 Spatial Indexing, Spatial Joins and Performance](./03-spatial-indexing.md) —
  the index-based route to the same grouping problem.
- [02 GeoDataFrame, CRS Handling and Spatial Joins](./02-geopandas-basics.md) —
  the CRS decisions that must come first.
- [01 Shapely Geometries and Planar Operations](./01-shapely-geometries.md) —
  validity and predicates for the polygon side.
- [03-08-06 rasterio: Rasters, Windows, Masks and Reprojection](../08-gridded-geospatial-data/06-rasterio-rasters.md)
  — the transform and window mechanics used here.
- [03-08-03 Dataset, Alignment, Broadcasting and GroupBy](../08-gridded-geospatial-data/03-xarray-dataset.md)
  — `weighted`, for the case where the zones are a raster of class labels.

## Exercises

[`exercises/04-vector-raster-ops-exercises.md`](./exercises/04-vector-raster-ops-exercises.md),
with full worked answers in
[`exercises/04-vector-raster-ops-solutions.md`](./exercises/04-vector-raster-ops-solutions.md).

## Self-assessment checklist

- [ ] I can state the pixel area of a raster and convert counts to areas.
- [ ] I can describe what `sample()` returns and bound its relocation error.
- [ ] I can explain `all_touched` and quote the measured area and mean
      differences.
- [ ] I can use the window transform correctly and explain what happens if I do
      not.
- [ ] I can rasterise polygons and check the pixelated areas against the true
      ones.
- [ ] I can implement a grouped zonal reduction and show it matches a
      per-polygon loop.
- [ ] I can say which statistics are resolution-invariant and which are not.
- [ ] I can name three defensible "mean values" for one raster and explain how
      they differ.
