---
id: 03-09-05
title: "Cartopy: Map Projections and Geographic Plotting"
level: intermediate
prereqs: ["03-09-02", "03-05-03"]
tags: [cartopy, projections, maps, distortion, mercator, equal-area, plotting]
---

# Cartopy: Map Projections and Geographic Plotting

A map is a projection plus a figure. The projection is a mathematical decision
with quantified consequences, and the figure is the part readers see. This lesson
does both, but its centre of gravity is the arithmetic: **how much is a given
projection distorting, at this latitude, for this quantity?** — because that
number is available from `pyproj` and it decides whether the map is honest.

> **Every number below is measured output from `code/maps_cartopy_demo.py`.**
> Projection scale factors come from `pyproj.Proj.get_factors`, geodesic
> distances from `pyproj.Geod`. The two figures are drawn from SYNTHETIC data; no
> dataset is downloaded.

## Learning objectives

By the end of this lesson you will be able to:

1. **Classify** a CRS as geographic or projected and name its units, from its
   EPSG code.
2. **Distinguish** a datum from an ellipsoid, and quote the measured coordinate
   shift between two common datums.
3. **Read** `get_factors()` output — meridian scale, parallel scale, areal scale,
   angular distortion — and interpret each.
4. **Predict** the areal distortion of Web Mercator at a stated latitude and
   explain the polar failure.
5. **Compare** straight-line, geodesic and rhumb-line distances and choose the
   right one.
6. **Plot** lon/lat data on a projected map with Cartopy and explain what is
   reprojected (the points) and what is not (the array).
7. **Choose** a projection from the quantity the map is meant to convey.
8. **State** the one network dependency in the Cartopy workflow and how to work
   without it.

## Prerequisites

- [03-09-02 GeoDataFrame, CRS Handling and Spatial Joins](./02-geopandas-basics.md)
  — CRS arithmetic, areas and distances.
- [03-05-03 Maps, Cross-Sections and Geological Symbology](../05-plotting-and-visualisation/03-maps-and-cross-sections.md)
  — map figure construction and geological symbology.

## 1. Geographic versus projected, and why the distinction is the whole lesson

```
EPSG: 4326 geographic unit = degree   WGS 84
EPSG: 3857 projected  unit = metre    WGS 84 / Pseudo-Mercator
EPSG:32612 projected  unit = metre    WGS 84 / UTM zone 12N
EPSG: 6933 projected  unit = metre    WGS 84 / NSIDC EASE-Grid 2.0 Global
EPSG: 3031 projected  unit = metre    WGS 84 / Antarctic Polar Stereographic
```

A **geographic** CRS assigns coordinates on the ellipsoid: longitude and latitude,
in degrees. A **projected** CRS has already mapped the ellipsoid onto a plane, and
only then do "metre", "area" and "distance" mean what they say. Every projection
distorts something, and the distortion is not a defect to be minimised away; it is
a property to be chosen.

| Quantity | Geographic (EPSG:4326) | Projected (metric) |
|---|---|---|
| a coordinate pair | meaningful | meaningful |
| a distance | needs `Geod` or a local scale factor | approximate, with a known scale factor |
| an area | needs the ellipsoidal band formula | approximate |
| a buffer | an ellipse on the ground | a circle |
| a straight line | a curve on the ground (or a rhumb line) | a curve on the ground |

## 2. Datum versus ellipsoid, measured

```
EPSG:4326 WGS 84
  ellipsoid = WGS 84, a = 6378137.000 m, inv_f = 298.257223563
EPSG:4269 NAD83
  ellipsoid = GRS 1980, a = 6378137.000 m, inv_f = 298.257222101
the semi-major axes agree to 0.0000 mm
Measured at 110 W, 40 N:
  NAD27 -> WGS 84                        shift =   62.172 m
  NAD83 -> WGS 84 (PROJ default pipeline) shift =    0.000 m
  NAD83(HARN) -> WGS 84                  shift =    1.171 m
```

The **ellipsoid** is the shape of the Earth model: semi-major axis and flattening.
WGS 84 and GRS 1980 have identical semi-major axes to a millimetre and flattenings
that differ in the ninth significant figure. The **datum** is the reference frame
in which coordinates live: an origin, an orientation and a scale relative to the
Earth's centre of mass. Changing the datum does not change the shape; it changes
the numbers assigned to a physical point.

The three measured shifts show why this matters in practice:

- **NAD27 → WGS 84 is 62.172 m** (61.814 m east–west, 5.799 m north–south). A
  legacy dataset in NAD27 placed on a modern basemap is off by tens of metres —
  enough to move a well or a station into the wrong polygon.
- **NAD83 → WGS 84 is exactly 0.000 m under PROJ's default pipeline**, because
  the two frames are coincident to within about 2 m and PROJ's default is a null
  transformation. The honest reading is not "NAD83 equals WGS 84" but "**the
  default transformation has a stated accuracy of about 2 m, and here it gives
  0 m**".
- **NAD83(HARN) → WGS 84 is 1.171 m**, because HARN is a different realisation of
  the frame.

The general rule: **a pair of EPSG codes does not specify a transformation.** When
a metre or better matters, choose a transformation with a stated accuracy
(a grid-shift or a Helmert with published parameters), and record which one you
used. `pyproj` exposes this through `Transformer.from_crs(..., accuracy=...)` and
the `TransformerGroup` API.

## 3. Reading the distortion directly

`pyproj.Proj.get_factors(lon, lat)` returns the local Jacobian of the projection:
how much a small length in each direction is stretched, and whether area and angle
are preserved.

```
projection     EPSG  at latitude   meridional  parallel   areal     angular
Web Mercator   3857       0.0     1.000000   1.000000   1.0000     0.0000
Web Mercator   3857      40.0     1.305407   1.305407   1.7041     0.0000
Web Mercator   3857      60.0     2.000000   2.000000   4.0000     0.0000
Web Mercator   3857      70.0     2.923804   2.923804   8.5486     0.0000

UTM 12N       32612       0.0     0.999753   0.999753   0.9995     0.0000
UTM 12N       32612      40.0     0.999690   0.999690   0.9994     0.0000
UTM 12N       32612      60.0     0.999638   0.999638   0.9993     0.0000
UTM 12N       32612      70.0     0.999618   0.999618   0.9992     0.0000

EASE-Grid 2.0  6933       0.0     1.153734   0.866751   1.0000    16.3314
EASE-Grid 2.0  6933      40.0     0.885036   1.129897   1.0000    13.9600
EASE-Grid 2.0  6933      60.0     0.578321   1.729145   1.0000    59.8333
EASE-Grid 2.0  6933      70.0     0.395772   2.526709   1.0000    93.6310
```

Four columns, four meanings:

- **Meridian and parallel scale**: linear stretch along the two directions. Both
  equal ⇒ conformal (angles preserved, shapes locally correct).
- **Areal scale**: the product. It is what multiplies an area to give the mapped
  area.
- **Angular distortion**: 0 for conformal, large for equal-area at high latitude.

Now read the table:

**Web Mercator is conformal and wildly unequal-area.** At 40°N a feature is drawn
1.705× too large in area; at 60°N, 4×; at 70°N, 8.55×. The measured identity
against the sphere formula is exact:

$$\text{meridian scale} = \frac{1}{\cos\phi}, \qquad
\text{areal scale} = \frac{1}{\cos^{2}\phi}:$$

```
Web Mercator at 60.0 N: meridional scale = 2.000000, 1/cos(lat) = 2.000000;
                        areal = 4.0000, 1/cos^2(lat) = 4.0000
Web Mercator at 70.0 N: meridional scale = 2.923804, 1/cos(lat) = 2.923804;
                        areal = 8.5486, 1/cos^2(lat) = 8.5486
```

**UTM is conformal with a scale factor near 1.** $k_0 = 0.9996$ by definition, and
the measured meridian scale is 0.999753 at the equator on the central meridian
falling to 0.999618 at 70°N and rising with distance from the central meridian.
Area error is under 0.1 % inside the zone: this is what "metric" means in practice.

**EASE-Grid 2.0 is equal-area and severely non-conformal.** Areal scale is exactly
1.00000000 at every latitude (a measured equality, not an approximation), while
the two linear scales differ by up to a factor of 6.4 at 70°N and the angular
distortion reaches 93.63°. **Equal-area maps are unusable for measuring angles or
local shapes**, which is the trade in the opposite direction.

## 4. What the distortion does to numbers

### 4.1 Web Mercator area, concretely

```
at  0.0 N: areal scale =    1.000,  so a polygon that renders as 1,000 km^2 is
                                  really   1000.0 km^2
at 40.0 N: areal scale =    1.704, ... really    586.8 km^2
at 60.0 N: areal scale =    4.000, ... really    250.0 km^2
at 85.0 N: areal scale =  131.646, ... really      7.6 km^2
```

A shape that occupies 1,000 mm² on a Web Mercator map at 85°N represents 7.6 km² of
ground; the same 1,000 mm² at the equator represents 1,000 km². That is the
Greenland-versus-Africa effect, with the number attached: **at 85°N the areal
inflation is 131.6×**, and the projection's *linear* scale there is
$\sqrt{131.646} = 11.5$.

### 4.2 The polar failure

```
the south of 60 S cap has ellipsoidal area 34.416 x 10^6 km^2 (6.75 % of the Earth)
and cannot be drawn at all in Web Mercator: latitude 90 S maps to y = -infinity
```

Web Mercator truncates at about ±85.05°, so an Antarctic map in EPSG:3857 either
omits the pole or clips it arbitrarily. The area formula used here is the
ellipsoidal band formula of
[03-08-03 Dataset, Alignment, Broadcasting and GroupBy](../08-gridded-geospatial-data/03-xarray-dataset.md),
verified there against the closed-form total surface area to machine precision.
The south-of-60°S cap is 34.416 × 10⁶ km², 6.75 % of the Earth's surface — a
non-trivial fraction of the planet with no representation.

### 4.3 Distances: four ways, four answers

```
EPSG: 4326: Quito (       -78.5,        -0.2)  Tromso (        19.0,        69.7)
EPSG: 3857: Quito (  -8738580.0,    -27830.0)  Tromso (   2110617.5,  10955743.6)
EPSG:32612: Quito (   4329214.6,    -32808.4)  Tromso (   2246615.2,  11493302.0)
EPSG: 6933: Quito (  -7574173.0,    -31893.2)  Tromso (   1829379.9,   6880229.8)
straight-line distance in the projected plane:
  EPSG: 3857:    15438392.93
  EPSG:32612:    11712746.98
  EPSG: 6933:    11670657.73
true geodesic distance = 10318.84 km
  EPSG: 3857 error = +496.137 % (+5119.56 km)
  EPSG:32612 error = +135.084 % (+1393.91 km)
  EPSG: 6933 error = +131.005 % (+1351.82 km)
```

Every one of those straight-line numbers is useless as a distance, for a different
reason: a straight line *in a projection* is not a path on the Earth. Quito and
Tromsø are 10,318.84 km apart along the geodesic; drawing a straight line between
their projected positions and measuring it in EPSG:3857 gives 15,438 km, an error
of **+496 %**. UTM zone 12 does not contain either city, so its 11,713 km is a
number computed outside the projection's domain — and even the equal-area
EASE-Grid 2.0, which is perfectly good for areas, gives 11,671 km, **+131 %**.

The lesson is not "use the right projection"; it is **"use a geodesic for a
long distance, and a local projection only for a local one"**. Three of these four
numbers are products of a projection used outside its design domain.

### 4.4 Geodesic versus rhumb line

```
geodesic (great circle)     =  10318.84 km
rhumb line (constant course) =  10924.99 km (+5.87 %)
the rhumb constant course   =     44.65 deg
the geodesic leaves Quito at     20.25 deg azimuth
and arrives in Tromso at       -82.99 deg azimuth
a change of 103.24 deg: a geodesic is not a straight line in lon/lat
```

Two candidate "straight lines" on the sphere, and they differ by 5.87 %:

- the **geodesic** (great circle) is the shortest path; its azimuth changes by
  103.24° from Quito to Tromsø;
- the **rhumb line** holds a constant course of 44.65° and is 606 km longer.

A navigation or flight-path question wants one; a "shortest separation" question
wants the other. `Geod.inv` gives the geodesic; the rhumb line is a standard
spherical formula (implemented in the demonstration). And for *drawing*, note that
`Geod.npts` returned 200 intermediate points: a curved path must be plotted as a
polyline in lon/lat, because a two-point `LineString` projected into any
projection is the wrong curve (measured in
[03-09-01 Shapely Geometries and Planar Operations](./01-shapely-geometries.md):
557.469 km geodesic versus 558.717 km for the projected 201-vertex parallel).

## 5. Plotting: what Cartopy changes

Cartopy is a Matplotlib extension that adds projections as first-class axes:

```python
ax = fig.add_subplot(1, 1, 1, projection=ccrs.Robinson())
mesh = ax.pcolormesh(lon2d, lat2d, field, transform=ccrs.PlateCarree(),
                     cmap="viridis", shading="auto")
ax.coastlines(resolution="110m", linewidth=0.4)
ax.gridlines(draw_labels=True, linewidth=0.2, color="grey")
```

Measured output: the Robinson figure is 79,471 bytes on disk and the Lambert
conformal regional figure is 15,098 bytes.

The mental model has three parts:

1. **`projection=` on the axes** sets the map projection. It does not move your
   data.
2. **`transform=` on every plotting call** states the CRS your *data* are in. Here
   the field is on a lon/lat grid, so `ccrs.PlateCarree()`. This is the argument
   that is most often omitted, and omitting it produces a plausible map in the
   wrong place.
3. **The data are not resampled.** `pcolormesh` reprojects the *quadrilaterals*
   (or their vertices) and lets Matplotlib rasterise them; the array's values are
   never interpolated onto the target grid.

> **Rule of thumb.** If you care about the numbers, resample the array in
> projection space with `rasterio.warp.reproject` (see
> [03-08-06 rasterio: Rasters, Windows, Masks and Reprojection](../08-gridded-geospatial-data/06-rasterio-rasters.md))
> and plot the resampled result. If you care about the picture, reproject at
> render time.

A fourth practical point: `coastlines`, `BORDERS`, `STATES` and `LAKES` are
Natural Earth vectors shipped through Cartopy's own data package. The first use
may **download** them — the one network dependency in this workflow. Everything
else in the demonstration is offline: the field is synthetic, and every number
comes from `pyproj`, NumPy or the seeded generator.

## 6. Why a Plate Carree map distorts, measured

```
a 20 x 10 deg box from 55 N to 65 N:
  geodesic area = 1,226,072.6 km^2
  its extent in PlateCarree degrees: 20.0 x 10.0
  drawn as a rectangle it looks like 2.0:1, while on the
  ground it is 1112 km wide and 1114 km tall, i.e. 1.00:1
```

The most familiar map of all — longitude on x, latitude on y, one degree per unit
— draws a 20° × 10° box as a 2:1 rectangle. On the ground that box is essentially
**square**: 1,112 km by 1,114 km, at 60°N. The mapping from degrees to distances is
$\cos\phi$ in one direction and constant in the other, so Plate Carree's aspect
ratio error at latitude $\phi$ is $1/\cos\phi$: 2.0 at 60°N, 2.9 at 70°N, and
undefined at the poles.

This is the cleanest way to state the general principle: **any map drawn in
degrees has a latitude-dependent length scale difference between its axes, and any
landmass drawn on it is distorted accordingly.**

## 7. Choosing a projection from the quantity

```
measured at 40 N, 110 W: areal scale Web Mercator 1.7041,
                         UTM 0.9994, EASE-Grid 2.0 1.0000
```

| Quantity of interest | Projection class | Example | Measured justification |
|---|---|---|---|
| distances in a small survey | local conformal | UTM zone 12N | areal scale 0.9994 at 40°N |
| areas over a region | equal-area | EPSG:6933 | areal scale 1.00000000 |
| a world map for reading | compromise | Robinson | distortion distributed, no pole failure |
| web tiles | Web Mercator | EPSG:3857 | conformal; areal scale 1.7041 at 40°N |
| polar science | polar stereographic | EPSG:3031 | designed for the pole |
| long-distance separation | none — use a geodesic | `Geod.inv` | projected straight lines are +131 to +496 % wrong |

The table's last row is the exception that proves the rule: the right projection
for a 10,000 km separation is *no projection at all*. Use the geodesic, and
project only what you draw.

## 8. Units and dimensional analysis

- **Scale factors are dimensionless.** 1.7041 and 0.9994 are pure numbers; that is
  what makes them comparable across projections.
- **Areal scale is the square of the linear scale only for a conformal
  projection.** Web Mercator: meridian scale 2.000000, areal 4.0000, and
  $2^{2} = 4$ exactly — measured. Equal-area projections break the relation
  ($0.578321 \times 1.729145 = 1.0000$ at 60°N, which is the *product*, not the
  square).
- **Azimuths are in degrees and are not angles on the map.** The geodesic's
  azimuth changes by 103.24° along the path; drawing that as a constant bearing on
  a Mercator map is a *rhumb line* and is 5.87 % longer.
- **A projection's coordinates carry its units.** EPSG:4326 values are degrees;
  EPSG:3857 values are metres. Concatenating them without transformation is a
  type error that no library will catch.
- **Datums are shifts in metres, ellipsoids are shapes.** Measured: 62.172 m for
  NAD27 → WGS 84, and 0.000014 m of semi-minor-axis difference between WGS 84 and
  GRS 1980.

## 9. Python demonstration

The full script is
[`code/maps_cartopy_demo.py`](./code/maps_cartopy_demo.py):

```bash
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python \
    03-scientific-computing/09-geospatial-python/code/maps_cartopy_demo.py
```

It writes two PNGs into a throw-away directory inside the module and deletes them
on exit. It uses the `Agg` backend, so it needs no display.

### What to observe, and why it matters

| Observation | Consequence |
|---|---|
| 4326 is geographic, the others are metric | the classification comes from the CRS, not the file name |
| WGS 84 and GRS 1980 semi-major axes agree to 0.0000 mm | an ellipsoid difference is not a datum difference |
| NAD27 → WGS 84 shifts a point 62.172 m | legacy data on modern basemaps are tens of metres out |
| PROJ's default NAD83 → WGS 84 shift is 0.000 m | the default transformation has an accuracy statement |
| Web Mercator's areal scale is 4.0000 at 60°N | the measured $1/\cos^{2}\phi$ identity |
| UTM's areal scale is within 0.1 % of 1 | "metric" means this |
| EASE-Grid 2.0's areal scale is exactly 1.00000000 | equal-area, with 93.6° of angular distortion at 70°N |
| a 20° × 10° box at 55–65°N is 2:1 on the map and 1.00:1 on the ground | Plate Carree's $\cos\phi$ aspect error |
| the Quito–Tromsø straight line in EPSG:3857 is +496 % wrong | projected straight lines are not distances |
| the rhumb line is 5.87 % longer than the geodesic | "straight" has two meanings |

> **Breaking exercise.** Before running, compute the areal scale of EPSG:3857 at
> 80°N by hand from $1/\cos^{2}\phi$, then read it from the demonstration. Then
> compute the latitude at which the areal scale reaches 100.

## 10. Common mistakes

1. **Omitting `transform=` in a Cartopy plot call.** The data are plotted in the
   axes' projection regardless, so the map is plausible and wrong.
2. **Measuring a distance from projected coordinates over thousands of
   kilometres.** Measured errors of +131 % to +496 %.
3. **Using a UTM zone outside its domain.** Quito is not in zone 12N.
4. **Drawing a geodesic as a two-point line.** Projected, it becomes the wrong
   curve; densify with `npts`.
5. **Reading areas off a Web Mercator map.** 131.6× at 85°N.
6. **Using Web Mercator for polar work.** 90°S maps to $y = -\infty$.
7. **Assuming a CRS pair implies a transformation.** NAD83 → WGS 84 defaulted to a
   null shift; specify the transformation when a metre matters.
8. **Confusing conformal with equal-area.** Web Mercator preserves angles and
   nothing else; EASE-Grid 2.0 preserves area and nothing else.
9. **Assuming Cartopy is offline.** The coastlines and borders come from Natural
   Earth and may be downloaded on first use.

## 11. Real-world applications

- **Global relief and gravity maps.** Published in Robinson or equal-area
  projections precisely because Mercator's high-latitude inflation would
  misrepresent the polar regions and the mid-ocean ridges' relative sizes.
- **Web mapping.** All slippy-map tiles are Web Mercator; the tile pyramid's
  latitude limit of ±85.05° is the projection's, not the data's.
- **Marine navigation.** Rhumb lines were the navigational standard for centuries
  because a constant bearing is easy to follow; the extra 5.87 % measured here is
  the price and the reason great-circle routing is used for fuel planning.
- **Antarctic and Arctic geophysics.** Polar stereographic projections are the
  standard, and the ice-sheet mass-balance literature is unreadable without
  knowing which one a figure uses.
- **GNSS and geodesy.** Datum transformations with stated accuracies are the
  difference between a survey that closes and one that is 62 m out.

## 12. Further reading

- **Cartopy, *Documentation*.** Level: intermediate.
  <https://cartopy.readthedocs.io> — projections, the `transform` argument, and
  `feature` layers.
- **PROJ, *Documentation*.** Level: advanced. <https://proj.org> — projection
  mathematics, datum transformations, and the accuracy of each pipeline.
- **pyproj, *Documentation*.** Level: intermediate.
  <https://pyproj4.github.io/pyproj/> — `Proj.get_factors`, `Geod`, `Transformer`
  and `TransformerGroup`, which are the instruments used throughout this lesson.
- **EPSG.io.** Level: reference. <https://epsg.io> — every CRS's units, area of use
  and datum.
- **Natural Earth, *public-domain map data*.** Level: reference.
  <https://www.naturalearthdata.com> — the source of Cartopy's coastline and
  border vectors, with the scales (110m, 50m, 10m) that the `resolution=` argument
  selects.

> Note on citations: bibliographic details are given so you can locate these
> works. This repository does not host or reproduce copyrighted text.

## 13. Related lessons

- [02 GeoDataFrame, CRS Handling and Spatial Joins](./02-geopandas-basics.md) —
  the same scale factors applied to areas and joins.
- [01 Shapely Geometries and Planar Operations](./01-shapely-geometries.md) —
  densification, buffers and the degree-versus-metre arithmetic.
- [04 Raster-Vector Integration and Zonal Statistics](./04-vector-raster-ops.md)
  — reprojection of arrays, as opposed to plotting.
- [03-08-03 Dataset, Alignment, Broadcasting and GroupBy](../08-gridded-geospatial-data/03-xarray-dataset.md)
  — the ellipsoidal band-area formula used for the polar cap here.
- [03-05-03 Maps, Cross-Sections and Geological Symbology](../05-plotting-and-visualisation/03-maps-and-cross-sections.md)
  — figure construction and the non-projection parts of a good map.

## Exercises

[`exercises/05-maps-cartopy-exercises.md`](./exercises/05-maps-cartopy-exercises.md),
with full worked answers in
[`exercises/05-maps-cartopy-solutions.md`](./exercises/05-maps-cartopy-solutions.md).

## Self-assessment checklist

- [ ] I can classify an EPSG code as geographic or projected and name its units.
- [ ] I can explain the difference between a datum and an ellipsoid and quote the
      measured NAD27 shift.
- [ ] I can read `get_factors()` and say whether a projection is conformal or
      equal-area.
- [ ] I can compute Web Mercator's areal scale at a stated latitude.
- [ ] I can explain why Web Mercator cannot represent the pole.
- [ ] I can choose between a geodesic and a rhumb line and quote the difference.
- [ ] I can plot lon/lat data on a projected map and say what is and is not
      resampled.
- [ ] I can choose a projection from the quantity a map is meant to convey, and
      say which one has no answer.
