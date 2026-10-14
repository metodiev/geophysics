---
id: 03-09-02
title: "GeoDataFrame, CRS Handling and Spatial Joins"
level: intermediate
prereqs: ["03-09-01", "03-04-01", "03-04-02"]
tags: [geopandas, crs, projection, spatial-join, datum, area, distances]
---

# GeoDataFrame, CRS Handling and Spatial Joins

A `GeoDataFrame` is a pandas `DataFrame` with one column of geometries and, more
importantly, a **CRS**. The CRS is not decoration: it is the difference between an
area that is 0.86 % wrong and one that is 0.04 % wrong, between a distance of
205.65 km and 205.63 km, and between a spatial join that assigns 86 points to a
cell and one that assigns 80.

> **Every number below is measured output from
> `code/geopandas_basics_demo.py`.** All data are SYNTHETIC: 600 seeded stations
> and six rectangular regions in the western USA. `pyproj` supplies the geodesic
> answers used to measure the errors. Nothing is downloaded.

## Learning objectives

By the end of this lesson you will be able to:

1. **Build** a `GeoDataFrame` from coordinates, and read its `crs`, `geometry`
   and `total_bounds`.
2. **Explain** why `EPSG:4326` is stored as lon/lat in GeoPandas although the EPSG
   registry defines it as lat/lon.
3. **Quantify** the error of a planar area in square degrees, and of a projected
   area under the wrong projection, the wrong zone and a different datum.
4. **Choose** a CRS from the quantity being computed: distance, area or
   containment.
5. **Run** a spatial join, predict its row count, and choose `predicate` and
   `how` deliberately.
6. **Demonstrate** the boundary behaviour of `within` versus `intersects` with a
   point placed exactly on a shared edge.
7. **Aggregate** per-region statistics and state when the aggregation must be
   area-weighted.
8. **Explain** what `estimate_utm_crs()` chooses and when it is inappropriate.

## Prerequisites

- [03-09-01 Shapely Geometries and Planar Operations](./01-shapely-geometries.md)
  — the geometries and the degree-versus-metre arithmetic.
- [03-04-01 Series, DataFrame and the Labeled-Data Model](../04-pandas/01-series-dataframe.md)
  — the container being extended.
- [03-04-02 Indexing, Selection, loc/iloc and Boolean Masks](../04-pandas/02-indexing-selection.md)
  — masks and label addressing on the attribute columns.

## 1. What the object is

```
rows = 600, columns = ['station', 'elev_m', 'v_p_kms', 'geometry']
geometry column = geometry, dtype = geometry
crs = EPSG:4326, epsg = 4326
mean elevation = 1501.1 m, mean v_p = 5.998 km/s
bounds = (-112.198, 36.801, -107.807, 40.193) (minx, miny, maxx, maxy)
```

Four facts, in order of how often they are forgotten:

1. **The geometry column is named and typed.** `stations.geometry` is a
   `GeoSeries`; `stations.geometry.dtype` is `geometry`, not `object`.
2. **Attribute statistics work unchanged.** `stations.elev_m.mean()` is an
   ordinary pandas mean, and it is *not* affected by the geometries. Weighting it
   by area is a separate, deliberate step (Section 6).
3. **`total_bounds` is in CRS units** — here degrees: 4.4° of longitude and 3.4°
   of latitude.
4. **`epsg = 4326` is authority-ordered as lat, lon, but GeoPandas stores lon,
   lat.** The x column is longitude. Every point-in-polygon test, every distance
   and every plot assumes this convention, and the EPSG registry's definition of
   4326 as lat-first is a well-known source of confusion when calling `PROJ` or a
   WFS service directly. `always_xy=True` in `pyproj.Transformer` is the flag that
   settles it.

## 2. Area: four answers for the same six rectangles

The regions tile a box; their areas are computed five ways below.

```
sum of region areas as stored = 12.000000 square degrees
after .to_crs('EPSG:32612') = 116137.2142 km^2
after .to_crs('EPSG:26912') = 116137.2142 km^2
  (NAD83 datum: difference 0.001 m^2 over 116137 km^2)
after .to_crs('EPSG:32611') = 117186.2810 km^2 (+0.8609 % true error)
true geodesic area (pyproj Geod)  = 116185.9791 km^2
error of the UTM area (zone 12) = -0.0420 %
```

| Route | Result | Error versus geodesic |
|---|---|---|
| square degrees, as stored | 12.000000 | not an area |
| UTM zone 12N (correct zone) | 116,137.2142 km² | −0.0420 % |
| UTM zone 11N (wrong zone) | 117,186.2810 km² | **+0.8609 %** |
| UTM zone 12N, NAD83 datum | 116,137.2142 km² | −0.0420 % (0.001 m² different) |
| EASE-Grid 2.0 (equal-area) | 116,186.8166 km² | +0.0007 % |

Four lessons in one table.

**Square degrees are not an area.** One square degree here is worth 9,682.2 km²,
and that factor varies with latitude. The degree ratio of the box is
1.295 (4.4°/3.4°) while the metre ratio is 1.056 — a factor of 1.23 between what
the coordinates say and what the ground says.

**Using the wrong UTM zone is a 0.86 % error.** The data span 110°W; zone 11 has
its central meridian at 117°W and zone 12 at 111°W. Zone 12 is correct and its
scale factor averages out to −0.042 % over the box (the negative sign comes from
being near, and partly west of, the central meridian where $k < 1$). Zone 11,
7° away, is off by **+0.861 %** — twenty times worse. A projection is only
metric inside its design domain.

**A datum change is a shift, not a distortion.** NAD83 and WGS 84 differ by about
a metre at this location, and moving the whole dataset by a metre changes an area
of 116,137 km² by 0.001 m² — 1 part in 10¹¹. So the *datum* is irrelevant here and
decisive elsewhere (any computation of a 1 mm-level displacement, or of an area
at the 10⁻¹¹ level). The distinction to hold on to: **the ellipsoid sets the shape
of the Earth model; the datum sets where the origin is.** Both are named in a CRS,
they are not the same thing, and their errors scale completely differently.

**An equal-area projection is the right default for area.** Measured: +0.0007 %
on the same data.

## 3. Distances: three answers for one pair of stations

```
stations SYN000 and SYN001:
  planar distance in degrees = 2.019513 deg
  projected distance in UTM   = 205.6477 km (+0.0077 % from geodesic)
  geodesic distance (pyproj)  = 205.6319 km
  cos(lat) approximation      = 205.0066 km (-0.3041 %)
```

Four numbers for one separation:

| Method | Value | Error |
|---|---|---|
| degrees | 2.019513 | no units |
| UTM metres (correct zone) | 205.6477 km | +0.0077 % |
| geodesic (`Geod.inv`) | 205.6319 km | reference |
| $\sqrt{(\Delta\lambda\cos\phi)^2 + \Delta\phi^2}\times 111{,}320$ | 205.0066 km | **−0.3041 %** |

The practical hierarchy is clear: **project into a suitable metric CRS for
distances (0.008 % here), use the geodesic when the separation spans a projection
boundary or exceeds a few hundred kilometres, and never use the $\cos\phi$
approximation for anything that matters** — 0.30 % on a 200 km baseline is 620 m.

The degree tolerance trap generalises this:

```
a tolerance written as 'distance < 0.05' in degrees means
4.373 km east-west at this latitude and 5.529 km north-south
```

A "0.05" tolerance is an ellipse with a 1.26:1 axis ratio at 38°N, and the ratio
grows without bound toward the poles. When a specification says "within 5 km",
implement it in metres.

## 4. Spatial joins

### 4.1 Row counts are predictable

```
sjoin(predicate='within', how='left'): 600 rows from 600 stations
stations with no region = 123 (20.50 %)
stations per region: {'R00': 86, 'R01': 80, 'R10': 73, 'R11': 76, 'R20': 76, 'R21': 86}
how='inner' -> 477 rows
predicate='intersects' -> 477, 'contains' -> 0,
predicate='within' -> 477, 'touches' -> 0
```

Bookkeeping to do before every join, in this order:

1. **Decide the predicate.** `within` (points in regions), `contains` (regions
   containing points — note it is applied the other way round), `intersects`
   (either), `touches` (boundary-only).
2. **Decide `how`.** `inner` silently drops the 123 stations that fall outside
   every region; `left` keeps them with a `NaN` region. The 477-row inner join is
   the 600 stations minus 123, and that subtraction is the first thing to verify.
3. **Check the output row count against the input.** More rows than inputs means
   at least one left-hand feature matched several right-hand features (the
   boundary case). Fewer means unmatched rows were dropped.
4. **Check the join is one-to-many or many-to-one, and say which.** A
   point-in-polygon join is many-to-one *only if the polygons do not overlap*.
   Overlapping polygons produce many-to-many, which multiplies totals.

### 4.2 The boundary case, measured

```
two stations placed exactly on the shared edge lon = -110.666667:
  predicate='within'     -> 0 matched point(s), 2 output rows
  predicate='intersects' -> 4 matched point(s), 4 output rows
  predicate='covers'     -> 0 matched point(s), 2 output rows
  predicate='touches'    -> 4 matched point(s), 4 output rows
```

Two stations, four rows under `intersects`: **each boundary point is assigned to
both adjacent cells**, and a per-cell count will double-count it. Under `within`,
the same points vanish from every cell, and a per-cell total will lose them.

Neither is a bug. Both are consequences of the OGC predicate definitions, and the
choice has to be made with the data in mind:

- **Physical partitioning** (a raster-like grid of survey cells, no gaps, no
  overlaps) → use the cell rule that guarantees exactly one assignment. A
  half-open convention implemented by hand, or a nearest-centroid assignment, does
  this; `intersects` does not.
- **Overlap questions** ("which monitoring wells lie in any of these protection
  zones?") → `intersects` is exactly right, and duplicates are the point.
- **Strictly interior questions** (a point on the property line is not *in* the
  property) → `within`.

The habit that protects you: assert the output shape against an expected count, and
report it. A join that returns 477 rows when you expected 480 has lost three
points to a boundary, and nothing else will tell you.

## 5. Aggregating per region

```
region   n     v_p       elev    area_km2  density_per_1000km2
R00     86  5.9934  1498.3128  19546.8972               4.3997
R01     80  6.0194  1553.7312  19150.4642               4.1774
R10     73  6.0062  1508.1356  19550.2201               3.7340
R11     76  6.0053  1515.6553  19153.5864               3.9679
R20     76  5.9783  1453.5671  19566.8424               3.8841
R21     86  5.9883  1467.2372  19169.2039               4.4864
mean v_p over stations = 5.9982 km/s
area-weighted by region = 5.9984 km/s (difference 0.27 m/s)
```

Two measured observations.

**The station counts are not proportional to area.** Expected from area alone:
80, 79, 80, 79, 80, 79. Measured: 86, 80, 73, 76, 76, 86. The excess in R00 and
R21 and the deficit in R10 reflects the seeded random draw, and it is the reason
that a station-based statistic and an area-based statistic differ.

**The weighting difference is small here, and that is informative.** The six
regions differ in area by only 2.17 %, and mean $v_p$ varies between them by only
0.7 % (5.9783 to 6.0194 km/s), so weighting changes the pooled mean by
0.27 m/s — 0.005 %. The honest conclusion is not "weighting does not matter"; it
is "**the size of the weighting correction is the product of the area spread and
the variable's spread**, and both are small in this synthetic example". In real
data, where the coastline-adjacent cells are small and systematically different,
both factors are large.

The general formula, and the one to apply whenever a per-region table is pooled:

$$\bar{x}_{\text{area}} = \frac{\sum_i A_i \bar{x}_i}{\sum_i A_i},$$

with $A_i$ in the *same* units for every region — which means a projected or
equal-area CRS, not degrees.

## 6. Buffer in degrees versus buffer in metres

```
buffer(0.1) in degrees then measured in UTM = 308.288 km^2
buffer(11000 m) in UTM                      = 379.522 km^2
ratio = 0.8123; 0.1 deg of longitude is 8.85 km
and 0.1 deg of latitude is 11.10 km, so the degree buffer is an
ellipse of area pi*a*b = 308.5 km^2 against a
11 km circle of area 380.1 km^2, ratio 0.8117 -- the measured value
```

The degree buffer is an ellipse with semi-axes **8.85 km and 11.10 km**; its area
$\pi a b = 308.5$ km² against the 11 km circle's $\pi r^{2} = 380.1$ km², a ratio
of 0.8117 — matching the measured **0.8123**. So a buffer specified in degrees is
**19 % short in area** at this latitude, and short by a different amount at every
other latitude. GeoPandas emits a `UserWarning` for exactly this operation
("Geometry is in a geographic CRS. Results from 'buffer' are likely
incorrect"), and it is one of the few warnings in this ecosystem that should
never be suppressed without a stated reason.

## 7. Choosing the CRS

```
GeoPandas suggests EPSG:32612 for these stations (epsg 32612)
the data span 4.4 deg of longitude; UTM zones are 6 deg wide
EPSG:32612 -> 116137.2142 km^2
EPSG:32611 -> 117186.2810 km^2
EPSG:6933  -> 116186.8166 km^2 (error +0.0007 %)
```

`estimate_utm_crs()` picks a UTM zone from the data's bounds. That is a good
default for a local survey and a poor one for anything wider:

| Task | CRS class | Example | Measured error here |
|---|---|---|---|
| distance, area, buffer within one region | local conformal | UTM zone 12N | −0.0420 % in area |
| area across regions or latitudes | equal-area | EPSG:6933 | +0.0007 % |
| web tiles and display | Web Mercator | EPSG:3857 | areal scale 1.7041 at 40°N |
| storage and interchange | geographic | EPSG:4326 | not metric at all |
| polar work | polar stereographic | EPSG:3031 | designed for it |

**Decide the CRS from the quantity, not from the data.** A dataset does not have
"a" correct projection: it has a correct projection for each question. Storing in
EPSG:4326 and projecting on demand is the arrangement that keeps the choice
visible at the point where it matters.

## 8. Round trips and units

```
lon/lat -> UTM -> lon/lat round trip: max coordinate shift = 0.000e+00 deg
hex WKB of the first region: 93 bytes, no CRS
```

A projection round trip is exact to floating-point precision, so projecting for a
calculation and converting back is safe — *provided the data stay inside the
projection's domain*. Outside it, the transformation is still defined (PROJ will
extrapolate) and the metric error grows without bound. The only guard is a bounds
check:

```python
assert crs.area_of_use is None or crs.area_of_use.contains(lon_min, lat_min, lon_max, lat_max)
```

Units to keep straight throughout:

- `total_bounds` and distances between geometries: CRS units (degrees in 4326).
- `geometry.area`: CRS units² (square degrees in 4326 — not an area).
- a `buffer` radius: CRS units, and the *shape* is a circle in those units.
- a `tolerance` in `sjoin`/`sjoin_nearest`: CRS units, so it is an ellipse on the
  ground in a geographic CRS.
- `how="left"` and `NaN` counts: dimensionless, and the first thing to assert.

## 9. Python demonstration

The full script is
[`code/geopandas_basics_demo.py`](./code/geopandas_basics_demo.py):

```bash
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python \
    03-scientific-computing/09-geospatial-python/code/geopandas_basics_demo.py
```

It needs no disk writes and no network. Two `UserWarning`s are expected and are
part of the lesson: GeoPandas warns when you compute an `area` or a `buffer` in a
geographic CRS.

### What to observe, and why it matters

| Observation | Consequence |
|---|---|
| `.area` in EPSG:4326 returns 12.000000 | square degrees are not an area |
| UTM zone 12 gives −0.0420 %, zone 11 gives +0.8609 % | the zone is part of the answer |
| NAD83 changes the area by 0.001 m² in 116,137 km² | a datum is a shift; its effect depends on the quantity |
| EASE-Grid 2.0 gives +0.0007 % | equal-area is the default for area |
| the $\cos\phi$ distance is −0.3041 % | 620 m on a 200 km baseline |
| 123 of 600 stations fall outside every region | `inner` drops them silently |
| a boundary point matches 0 cells under `within`, 2 under `intersects` | duplicates and losses are predicate choices |
| the degree buffer is 19 % short in area (ratio 0.8123) | the library warns, and is right to |
| `estimate_utm_crs()` picks zone 12 for a 4.4° span | a good local default, a bad global one |

> **Breaking exercise.** Before running, predict the six region areas in
> EPSG:32613 (zone 13N, central meridian 105°W) and compare with zone 11's
> +0.8609 %. Then measure both and explain the asymmetry.

## 10. Common mistakes

1. **Computing `.area` in EPSG:4326.** Square degrees; the factor to km² varies
   from ~9,682 at these latitudes to a few at the poles.
2. **Projecting into a UTM zone that does not contain the data.** Measured:
   +0.8609 % in area, twenty times the correct zone's error.
3. **Confusing the datum with the ellipsoid.** Measured difference between NAD83
   and WGS 84: 0.001 m² in 116,137 km².
4. **Using a `within` join for a partition.** Boundary points vanish; measured 0
   matches for 2 points on a shared edge.
5. **Using an `intersects` join for a partition.** Boundary points are duplicated;
   measured 4 rows for 2 points.
6. **Pooling per-region means without area weights.** Harmless when both the area
   spread and the variable spread are small (0.005 % here), and not otherwise.
7. **Buffering in degrees.** 19 % short in area at 38°N, and latitude-dependent.
8. **Assigning a CRS with `set_crs` when you meant `to_crs`.** `set_crs` relabels
   the coordinates; `to_crs` transforms them. One is metadata, one is arithmetic.
9. **Trusting a join's row count without asserting it.** 477 versus 600 is the
   only signal that 123 features were dropped.

## 11. Real-world applications

- **Seismic station and well inventories.** Assigning stations to basins or
  administrative regions is a point-in-polygon join; the unmatched count is a data
  quality metric.
- **Mineral tenement and licence management.** Areas carry legal meaning, so
  they are computed in a projected CRS with a stated datum, and the difference
  between WGS 84 and NAD83 is a matter of contract.
- **Catchment statistics.** Area-weighted rainfall or land cover from per-catchment
  tables; the weighting is the whole calculation.
- **Marine gravity and bathymetry.** Compilations are stored in lon/lat and must be
  projected into an equal-area CRS before any global average.
- **Hazard and exposure modelling.** Buffers of fault traces and flood extents are
  metric; doing them in degrees changes the hazard zone width with latitude.

## 12. Further reading

- **GeoPandas, *Documentation*.** Level: intermediate. <https://geopandas.org> —
  `to_crs`, `sjoin`, `estimate_utm_crs`, and the CRS-handling notes.
- **Shapely, *Documentation*.** Level: intermediate.
  <https://shapely.readthedocs.io> — the predicates and their boundary
  definitions, which Section 4.2 measures.
- **PROJ, *Documentation*.** Level: advanced. <https://proj.org> — datums,
  transformations and the accuracy statements behind `to_crs`.
- **EPSG.io.** Level: reference. <https://epsg.io> — inspect a CRS's units, area
  of use and datum, which is how the zone-11 error in Section 2 was chosen.
- **Open Geospatial Consortium, *Simple Feature Access* specification.** Level:
  reference. The normative source for `contains`, `covers`, `within`,
  `intersects` and `touches`.

> Note on citations: bibliographic details are given so you can locate these
> works. This repository does not host or reproduce copyrighted text.

## 13. Related lessons

- [01 Shapely Geometries and Planar Operations](./01-shapely-geometries.md) — the
  geometry layer beneath this one.
- [03 Spatial Indexing, Spatial Joins and Performance](./03-spatial-indexing.md)
  — how the join is executed, and why the naive loop is not an option.
- [04 Raster-Vector Integration and Zonal Statistics](./04-vector-raster-ops.md)
  — the raster side of the same CRS decisions.
- [05 Cartopy: Map Projections and Geographic Plotting](./05-maps-cartopy.md) —
  the scale factors that these errors come from.
- [03-08-06 rasterio: Rasters, Windows, Masks and Reprojection](../08-gridded-geospatial-data/06-rasterio-rasters.md)
  — why a square-in-degrees raster is not square on the ground.

## Exercises

[`exercises/02-geopandas-basics-exercises.md`](./exercises/02-geopandas-basics-exercises.md),
with full worked answers in
[`exercises/02-geopandas-basics-solutions.md`](./exercises/02-geopandas-basics-solutions.md).

## Self-assessment checklist

- [ ] I can build a `GeoDataFrame` and state its CRS, bounds and geometry column.
- [ ] I can explain the lon/lat versus lat/lon authority-order issue.
- [ ] I can compute an area four ways and say which answer is the physical one.
- [ ] I can estimate the error of using the wrong UTM zone.
- [ ] I can decide whether a datum change matters for a given quantity.
- [ ] I can predict the row count of a spatial join from the predicates and the
      unmatched count.
- [ ] I can describe what happens to a point on a shared boundary under `within`
      and under `intersects`.
- [ ] I can choose a CRS from the quantity being computed and justify it.
