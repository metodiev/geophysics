---
id: 03-09-01
title: "Shapely Geometries and Planar Operations"
level: intermediate
prereqs: ["03-01-05", "03-02-03"]
tags: [shapely, geometry, planar, buffer, validity, crs, wkt]
---

# Shapely Geometries and Planar Operations

A vector dataset is a set of geometries with coordinates. Shapely gives you the
geometries and the operations on them — union, intersection, buffer, distance,
validity — and it gives them to you in the coordinate system you handed it.
**Shapely has no concept of a CRS.** That single fact explains every mistake in
this lesson.

> **Every number below is measured output from
> `code/shapely_geometries_demo.py`.** All geometries are SYNTHETIC and built in
> code; `pyproj.Geod` supplies the metric answers used to measure the errors.
> Nothing is downloaded.

## Learning objectives

By the end of this lesson you will be able to:

1. **Build** `Point`, `LineString`, `Polygon` and `MultiPolygon` objects and state
   the units of `.length` and `.area`.
2. **Quantify** the error of treating a degree as a length, as a function of
   latitude.
3. **Explain** why an area in square degrees is not an area, and compute the
   projected and geodesic alternatives.
4. **Demonstrate** that a buffer in degrees is an ellipse in metres, and produce a
   metric buffer by projecting first.
5. **Detect** invalid geometry and say what each repair method returns.
6. **Choose** between `contains`, `covers` and `intersects` from the behaviour you
   want at boundaries.
7. **Use** shapely's vectorised functions on arrays, and explain what that changes
   about algorithm design.
8. **Explain** why the vertex mean and the centroid differ, and which one an
   analysis wants.

## Prerequisites

- [03-01-05 Lists, Tuples, Dictionaries, Sets and Complexity](../01-python-fundamentals/05-data-structures.md)
  — coordinate sequences and the cost of membership tests.
- [03-02-03 Broadcasting, Vectorisation and the `axis` Trap](../02-numpy/03-broadcasting.md)
  — shapely 2 is array-oriented, and the same rules apply.

## 1. Intuition: geometry with no idea where it is

```python
poly = Polygon([(-111.0, 39.0), (-109.0, 39.0), (-109.0, 40.5), (-111.0, 40.5)])
poly.area     # 3.0000
```

Three what? Three *square degrees*, which is not an area. Shapely computed the
shoelace sum in the coordinates it was given. If those coordinates had been UTM
metres, the same call would have returned 3 × 10⁸ m² — 300 km². The code is
identical; the answer differs by a factor of 10¹⁰, and only the CRS differs.

The demonstrated consequences of ignoring this:

| Operation | In degrees | In UTM metres | True (geodesic) |
|---|---|---|---|
| length of a 10° segment | 10.0000 | 558.717 km | 557.469–558.048 km |
| area of a 2° × 1.5° box | 3.0000 | 28,528.20 km² | 28,545.78 km² |
| area of a `buffer(5000)` at 60°N | n/a | 78.414 km² | 78.540 km² |
| distance between two points 1° apart in longitude at 60°N | 1.0000 | 55.80 km | 55.80 km |

The last row is the tell: in degrees, 1° of longitude at 60°N and 1° of longitude
at the equator are the *same number*, and on the ground they differ by 55.80 km
against 111.32 km.

## 2. Precise definitions

### 2.1 The geometry types

| Type | Stores | Has `.area` | Has `.length` |
|---|---|---|---|
| `Point` | one coordinate pair | 0 | 0 |
| `LineString` | an ordered coordinate sequence | 0 | yes |
| `LinearRing` | a closed sequence | 0 | yes |
| `Polygon` | exterior ring, interior rings (holes) | yes | yes (perimeter) |
| `MultiPolygon` | several disjoint polygons | yes (sum) | yes |
| `GeometryCollection` | any mixture | yes (2-D parts) | yes (1-D parts) |

The **dimension** of a geometry (0, 1 or 2) decides which of `area` and `length`
is meaningful, so a mixed collection silently sums the areas of its polygon parts
and the lengths of its line parts into the same number if you call both, or
returns 0 for the other.

### 2.2 Metric quantities in a planar system

In a planar (projected) coordinate system with metric units, everything behaves:

- $\text{distance}(A,B)$ is the Euclidean distance between the nearest points;
- `buffer(r)` is the set of points within $r$ of the geometry;
- `area` is the integral in the plane, and the shoelace formula applies;
- `convex_hull`, `envelope` and the boolean predicates are all the familiar
  planar operations.

None of that is true in a geographic CRS, not even approximately, because the
mapping from the plane of coordinates to the surface of the ellipsoid is
nonlinear.

### 2.3 The degree-to-metre conversion, quantitatively

Two formulas matter:

$$\text{1° of latitude} \approx M(\phi)\,\frac{\pi}{180},\qquad
\text{1° of longitude} \approx N(\phi)\cos\phi\,\frac{\pi}{180},$$

with $M$ the meridional and $N$ the prime-vertical radius of curvature. Measured
on WGS 84 for a 1° separation in longitude:

| Latitude | shapely distance | geodesic distance | km per degree of longitude |
|---|---|---|---|
| 0°N | 1.0000° | 111.32 km | 111.32 |
| 40°N | 1.0000° | 85.39 km | 85.39 |
| 50°N | 1.0000° | 71.70 km | 71.70 |
| 60°N | 1.0000° | 55.80 km | 55.80 |
| 70°N | 1.0000° | 38.19 km | 38.19 |

The shapely answer is 1.0000 in every row. Latitude is nearly constant: 1° N–S at
40°N is 111.044 km, which is 0.99921 of the nominal 111.132 km. So the popular
"multiply degrees by 111,132 to get metres" is right in one direction, wrong by up
to a factor of 3 in the other, and wrong by 0.08 % even in the direction it claims
to be right. It is a *scaling factor*, not a projection, and it cannot be fixed by
choosing a better constant.

## 3. Buffers: the clearest illustration of the problem

```
buffer(0.05) on POINT (-110 60):
  bounds in degrees = (-110.05, 59.95, -109.95, 60.05)
  0.05 deg north-south = 5.571 km
  0.05 deg east-west   = 2.790 km (49.9 % shorter -- the buffer is an ellipse)
  area = 48.748 km^2
  the true shape is an ellipse with semi-axes 5.571 km and 2.790 km,
  area pi*a*b = 48.827 km^2 (-0.16 %)
  a circle of the same radius would be 97.490 km^2, i.e. 2.0x too big
```

`buffer(0.05)` in a geographic CRS produces a shape that is a circle *in degree
space*: ±0.05° in every direction. On the ground that is 5.571 km north–south and
2.790 km east–west at 60°N. The result is an ellipse with a 2:1 aspect ratio.

The area confirms it: 48.748 km² measured, against the ellipse's analytic
$\pi a b = \pi \times 5.571 \times 2.790 = 48.827$ km² (−0.16 %, the small
residual being the polygonal approximation of the outline). A circle of the
nominally intended radius would be 97.490 km² — **the degree buffer is a factor of
two wrong in area**, and it is wrong by a different factor at every latitude.

The repair is the standard one:

```
buffer(5000.0) after projecting to EPSG:32612:
  area = 78.414 km^2 vs pi*r^2 = 78.540 km^2 (-0.161 %)
  converted back to lon/lat its extent is 0.1793 deg of longitude by
  0.0898 deg of latitude, and the ratio 1.997 is 1/cos(60 deg) = 2.000
```

Project to a metric CRS, buffer in metres, convert back. The remaining −0.161 %
is the UTM scale factor at that location, which is a *known* quantity
($k \approx 0.9996$ times a small distance-from-central-meridian term), not an
unknown distortion. Note the round-trip extent: a metric circle is 0.1793° wide
and 0.0898° tall, in the ratio $1/\cos 60° = 2.000$ — the shape that a metric
buffer *must* have in degrees.

## 4. Validity, and what an invalid polygon returns

```
ring = (0,0) (1,1) (1,0) (0,1): is_valid = False,
  reason = Self-intersection[0.5 0.5]
its reported area is 0.0000 -- not 0.5, not 1.0, but ZERO,
  because the two triangles cancel in the shoelace sum
shapely.make_valid -> MultiPolygon of 2 parts, area = 0.5000
the older 'buffer(0)' repair -> Polygon, area = 0.2500 (ONE lobe)
```

A self-intersecting ("bow-tie") ring is the standard invalid polygon. Three
distinct behaviours, all measured:

1. **`area` returns 0.0000.** The signed shoelace sum of the two lobes cancels.
   This is the dangerous case: the number is not obviously wrong (a polygon could
   legitimately be degenerate) and it is not an exception.
2. **`make_valid` returns a `MultiPolygon` of two parts with area 0.5000** — both
   lobes, which is the mathematically intended answer.
3. **`buffer(0)` returns only one lobe, area 0.2500.** The legacy repair is
   *lossy*: it keeps the lobe with the positive winding and discards the other.

The lesson: `is_valid()` is a check, `is_valid_reason()` is a diagnosis, and
`make_valid()` is the fix. `buffer(0)` is a historical idiom that silently halves
your area. Validate at ingestion — after every file read and every coordinate
transform, since transforming a valid polygon can produce a self-intersecting one
near a projection singularity.

## 5. Predicates: the boundary case

```
point interior         -> contains = True,  covers = True,  intersects = True
point on the boundary  -> contains = False, covers = True,  intersects = True
```

OGC predicates distinguish the interior, the boundary and the exterior of a
geometry, and the difference bites at boundaries:

- `contains(A, B)` requires B to be in A's interior and not touch its boundary;
- `covers(A, B)` includes the boundary;
- `intersects(A, B)` includes both;
- `touches(A, B)` requires the intersection to be in both boundaries but neither
  interior.

A point on the shared edge between two adjacent polygons is `within` *neither*,
`intersects` *both*, and `touches` *both*. In a point-in-polygon assignment this
means: `within` loses the point entirely, `intersects` duplicates it. The
companion lesson measures exactly this — two stations placed on a shared cell edge
gave 0 matches under `within` and 4 rows (two stations × two cells) under
`intersects`. Neither behaviour is wrong; **the choice is part of the analysis and
must be stated.**

## 6. Vectorised operations

Shapely 2 moved the operations onto arrays, which changes how you write code:

```
5000 points tested against one box in one call: 860 inside (17.20 %)
shapely.area on a point array = [0.] (points have no area)
buffer of 5 points by 0.01 deg -> [0.000312, 0.000312, 0.000312, 0.000312, 0.000312]
get_coordinates returns a flat float64 array: (5, 2) for the box
```

Three practical consequences:

1. **The loop goes away.** `shapely.within(points_array, polygon)` evaluates all
   5,000 containment tests in one call, and can release the GIL for parallelism.
   Writing a Python `for` loop over `Point` objects produces the same answers and
   two orders of magnitude more overhead.
2. **The results are arrays, not booleans.** You get a boolean mask (or an array
   of geometries), which composes with NumPy indexing and with pandas.
3. **The buffer is a polygon.** `buffer(0.01)` on a point returns a 33-vertex
   polygon whose area is 0.000312 deg² against the analytic
   $\pi r^{2} = \pi \times 0.01^{2} = 0.000314$: the 0.5 % deficit is the
   default `quad_segs=8` polygon, i.e. 4 vertices per quadrant. When a buffer's
   area must be right, raise `quad_segs`.

## 7. Centroid versus vertex mean

```
vertices = 9; area = 50.0000
vertex mean = (7.7779, 6.6667)
centroid    = (6.6667, 3.3333)
the two differ by 3.5137 units
```

Both are "the middle of the polygon" and they disagree by 3.51 coordinate units —
kilometres, if the coordinates are kilometres. The centroid is the area-weighted
first moment, which is the correct "centre" for any process that is distributed
over the polygon's surface. The vertex mean is the arithmetic mean of the ring's
coordinates, which is a statement about how the boundary was digitised.

This matters whenever a polygon represents a *region*: assigning a station to the
nearest polygon centroid, or labelling a region by its mean vertex, introduces a
bias proportional to the asymmetry of the boundary sampling. Polygons digitised
from a coastline have dense vertices where the coast is complex; the vertex mean
of such a polygon sits in the complex part.

## 8. Serialisation and precision

```
WKT    : 59 characters; area preserved exactly: True
WKB    : 93 bytes, 186 hex characters
GeoJSON: 118 characters; CRS is NOT stored in RFC 7946 GeoJSON
round trip difference: 0.000e+00
```

| Format | Size here | Carries CRS | Use for |
|---|---|---|---|
| WKT | 59 chars | no | logs, tests, readability |
| WKB | 93 bytes | no | binary interchange, database columns |
| GeoJSON | 118 chars | no (RFC 7946 mandates WGS 84 lon/lat) | web APIs, GeoPandas I/O |
| GeoPackage | — | yes | archival, multi-layer |
| Shapefile | — | yes (a `.prj` sidecar) | legacy, and to be avoided |

Two rules follow. **Never rely on a geometry to carry its CRS**: WKT, WKB and
GeoJSON do not, so a CRS must travel alongside or in a container that has a
CRS field. And **GeoJSON's implicit WGS 84 is a constraint, not a convenience**:
writing UTM coordinates into GeoJSON produces a file that any other tool will
interpret as degrees.

## 9. Densifying before projecting

```
a 10 deg segment at 60 N: 2 vertices -> 201 after segmentize(max_segment_length=0.05)
geodesic between the endpoints     = 557.469 km (cuts poleward of the parallel)
arc along the 60 N parallel        = 558.048 km (0.58 km longer)
straight 2-vertex chord projected   = 558.182 km
201-vertex curve projected          = 558.717 km
```

A `LineString` is a piecewise-linear object *in the coordinate space it was
written in*. Projecting its two endpoints and drawing a straight line gives a
different curve than projecting the curve the author intended:

- the geodesic between the endpoints is 557.469 km and bows **poleward** of the
  parallel;
- the arc along the 60°N parallel is 558.048 km — $0.58$ km longer, 0.104 %;
- projecting the two endpoints gives 558.182 km in UTM;
- projecting 201 points along the parallel gives 558.717 km, the correct
  representation of the parallel arc under UTM's scale factor.

None of those four numbers is wrong; they answer four different questions. The
practical rule: **densify before projecting when the geometry is meant to follow
a path on the ellipsoid** (a flight line, a river, a survey track), and do not
densify when it is meant to be straight in the projected plane (a survey boundary
digitised in UTM).

## 10. Units and dimensional analysis

- `length` has units of the coordinate system, `area` the square of it. In a
  geographic CRS those units are degrees and square degrees, and neither is a
  physical length or area.
- A ~1° tolerance in a spatial join means 111 km north–south and
  55.8 km east–west at 60°N. If your tolerance came from "within 1 km", it is
  wrong by a latitude-dependent factor.
- `buffer(r)` has units of $r$; the shape it produces has the units of the
  coordinate system. Buffering in degrees produces a physically non-circular
  shape, which is a unit error even though the number is the one you asked for.
- Geodesic areas from `Geod.geometry_area_perimeter` are signed by winding order;
  take `abs()` and state the convention. The demonstration's 2° × 1.5° box has a
  geodesic area of 28,545.7755 km² against a UTM area of 28,528.1956 km², a
  −0.0616 % projection error.

## 11. Python demonstration

The full script is
[`code/shapely_geometries_demo.py`](./code/shapely_geometries_demo.py):

```bash
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python \
    03-scientific-computing/09-geospatial-python/code/shapely_geometries_demo.py
```

It needs no disk writes and no network.

### What to observe, and why it matters

| Observation | Consequence |
|---|---|
| `poly.area` returns 3.0000 for a 3 deg² box | shapely answers in coordinate units, always |
| 1° of longitude is 111.32 km at 0°N and 38.19 km at 70°N | a degree is not a length, and one constant cannot fix it |
| `buffer(0.05)` is 5.571 km × 2.790 km at 60°N | the degree buffer is an ellipse with a 2:1 axis ratio |
| its area is 48.748 km² vs 97.490 km² for a circle | the degree buffer is wrong by a factor of two in area |
| the UTM buffer is 78.414 km² vs $\pi r^2$ = 78.540 | projected buffers are right up to the known scale factor |
| a bow-tie's area is 0.0000 | invalid geometry returns a plausible-looking wrong number |
| `buffer(0)` recovers 0.2500, `make_valid` 0.5000 | the legacy repair is lossy |
| a boundary point is not `contains` but is `covers` | predicate choice decides boundary behaviour |
| centroid and vertex mean differ by 3.5137 units | "the centre" depends on the definition |
| WKB is 93 bytes with no CRS | a geometry cannot carry its own coordinate system |

> **Breaking exercise.** Before running, predict the geodesic area of a
> 2° × 1.5° box centred on 60°N rather than 39–40.5°N, then measure it and
> compare with the UTM value. The projection error should be of similar size, but
> the *absolute* areas should be very different.

## 12. Common mistakes

1. **Computing `.area` or `.length` in a geographic CRS.** Measured: the same
   number means 3 deg² or 300 km² depending on the CRS.
2. **Buffering in degrees.** Measured: a 2:1 ellipse instead of a circle.
3. **Using a single degree-to-metre constant.** Right for latitude, wrong by 3×
   for longitude at high latitude, and 0.08 % off even for latitude.
4. **Trusting an invalid geometry.** The bow-tie's area is 0.0000, and nothing
   raises.
5. **Repairing with `buffer(0)`.** It recovered 0.2500 of a 0.5000 area.
6. **Using `contains` where `covers` or `intersects` was meant.** Boundary points
   disappear from joins.
7. **Letting a `Circle`/"radius" assumption survive projection.** Reversing
   `to_crs` turns the circle back into a 2:1 degree shape, which is correct — and
   surprising if you expected a circle in degrees.
8. **Projecting an unsegmented long line.** A 10° segment is 0.104 % different
   between the parallel arc and the geodesic; for longer lines the difference
   grows.
9. **Assuming a geometry file carries its CRS.** WKT, WKB and GeoJSON do not.

## 13. Real-world applications

- **Survey footprints.** Flight-line and lease polygons are buffered, unioned and
  clipped; buffering in degrees makes the margin latitude-dependent, which is
  indefensible in a contract.
- **Catchment and basin delineation.** Areas are compared across latitudes, so a
  geographic CRS guarantees an area bias that varies from basin to basin.
- **Cross-border infrastructure.** A 1 km corridor specified in degrees is 1 km at
  one latitude and 0.5 km at another.
- **Damage and exposure models.** Buffering a fault trace to represent a
  rupture-zone width is a metric operation; doing it in degrees invalidates the
  hazard statistics.
- **Data conflation.** Two datasets in different CRSs, joined without
  transformation, produce a map that is wrong by hundreds of metres and looks
  entirely plausible.

## 14. Further reading

- **Shapely, *Documentation*.** Level: intermediate.
  <https://shapely.readthedocs.io> — geometry types, predicates, `make_valid`, and
  the shapely 2 array interface.
- **Open Geospatial Consortium, *Simple Feature Access* specification.** Level:
  reference. Defines `contains`, `covers`, `touches` and the rest of the predicate
  set, together with the boundary rules used in Section 5.
- **PROJ, *Documentation*.** Level: advanced. <https://proj.org> — transformations
  and the projections you will project into.
- **EPSG.io.** Level: reference. <https://epsg.io> — find and inspect CRS codes.
- **RFC 7946, *The GeoJSON Format*.** Level: reference.
  <https://datatracker.ietf.org/doc/html/rfc7946> — why GeoJSON is always WGS 84
  lon/lat, and what that implies for interchange.

> Note on citations: bibliographic details are given so you can locate these
> works. This repository does not host or reproduce copyrighted text.

## 15. Related lessons

- [02 GeoDataFrame, CRS Handling and Spatial Joins](./02-geopandas-basics.md) —
  the same geometries with a CRS attached and an index-based join.
- [03 Spatial Indexing, Spatial Joins and Performance](./03-spatial-indexing.md)
  — doing this at scale without an $O(NM)$ loop.
- [05 Cartopy: Map Projections and Geographic Plotting](./05-maps-cartopy.md) —
  the projection scale factors that quantify the distortion used here.
- [03-08-06 rasterio: Rasters, Windows, Masks and Reprojection](../08-gridded-geospatial-data/06-rasterio-rasters.md)
  — the raster equivalent of this lesson's warnings.
- [03-02-03 Broadcasting, Vectorisation and the `axis` Trap](../02-numpy/03-broadcasting.md)
  — the array discipline shapely 2 assumes.

## Exercises

[`exercises/01-shapely-geometries-exercises.md`](./exercises/01-shapely-geometries-exercises.md),
with full worked answers in
[`exercises/01-shapely-geometries-solutions.md`](./exercises/01-shapely-geometries-solutions.md).

## Self-assessment checklist

- [ ] I can state the units of `.length` and `.area` for a geometry I have built.
- [ ] I can convert a degree of longitude to kilometres at a stated latitude.
- [ ] I can explain why a `buffer(0.05)` is an ellipse and compute its axis
      lengths.
- [ ] I can produce a metric buffer and state the residual error.
- [ ] I can detect an invalid polygon, name the reason, and say what each repair
      returns.
- [ ] I can choose between `contains`, `covers` and `intersects` for a boundary
      case and justify the choice.
- [ ] I can explain the difference between the centroid and the vertex mean and
      say which one a regional statistic needs.
- [ ] I know that WKT, WKB and GeoJSON do not carry a CRS.
