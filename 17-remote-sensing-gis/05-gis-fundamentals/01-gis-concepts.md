---
id: 17-05-01
title: "GIS Concepts: Layers, Attributes and Topology"
level: beginner
prereqs: ["03-09-01", "03-09-02"]
tags: [gis, geospatial, remote-sensing, gis-fundamentals, topology, crs, attributes]
---

# GIS Concepts: Layers, Attributes and Topology

A geographic information system is not a map. It is a **database with a coordinate
column**, plus the set of operations that column makes possible. Everything a GIS
does — a polygon overlay, a zonal statistic, a buffer, a suitability map — is
assembled from four ingredients: *layers*, *attributes*, *topology* and a
*coordinate reference system*. This lesson defines each one precisely, measures
what goes wrong when a definition is assumed rather than checked, and shows why
the two silent failures of GIS practice, the misplaced coordinate and the
double-counted polygon, raise no error at all.

All models and data in this module are **SYNTHETIC**. Every coordinate,
polygon and attribute value below is constructed in memory for teaching, not
measured. No real place, dataset or coordinate is used, and no number is quoted
from a published measurement.

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** a GIS layer as a table plus a geometry column, and **identify** the
   attribute half and the geometric half of any given layer.
2. **Interpret** an affine geotransform and a coordinate reference system, and
   **state** the units in which any distance or area is expressed.
3. **Test** whether a set of polygons is a valid planar partition, using area
   additivity and the Euler count, and **explain** what a failure of each
   invariant means.
4. **Quantify** the area error introduced by a digitising tolerance, and
   **separate** the overlap term from the gap term.
5. **Choose and justify** a spatial predicate (`within`, `intersects`,
   `contains`) for a join, and **predict** how the row count changes with it.
6. **Compute** geodesic and projected areas of the same synthetic shape and
   **explain** why their difference is a choice rather than an error.
7. **State** three topology questions that no arithmetic on coordinates can
   answer for you.

## Prerequisites

- [03-09-01 Shapely Geometries](../../03-scientific-computing/09-geospatial-python/01-shapely-geometries.md) —
  points, lines, polygons and the simple-features model.
- [03-09-02 GeoPandas Basics](../../03-scientific-computing/09-geospatial-python/02-geopandas-basics.md) —
  loading a geo-table and reading an attribute column.
- [02-01-01 Physical Quantities](../../02-physics/01-measurement-and-physical-reasoning/01-physical-quantities.md) —
  units and dimensions, used here for every area and distance.

## 1. The four ingredients

### 1.1 Layers

A **layer** (also *feature class* or *coverage*) is a relation in the database
sense whose rows are *features* and whose columns are *attributes*, plus one
special column holding a *geometry* per row. The geometry is a value, not a
separate object type: it has a type tag (Point, LineString, Polygon, and their
Multi- variants) and it is stored in the same table as the rest of the row.

The demonstration builds a four-row layer and prints its schema. The attribute
half is ordinary tabular data — strings, floats, integers — and the geometric
half is one column of type `geometry`:

```
block land_cover  ndvi_mean  n_samples
alpha       bare       0.18        146
 beta  vegetated       0.71        165
gamma      water      -0.05        135
delta       bare       0.22        116
```

An important consequence follows immediately. Because the geometry is a column,
**every tabular operation is available on a layer, and every one of them can
break the geometry's meaning.** A group-by over `land_cover` returns one row per
class; the geometries are gone unless the aggregation redefines them (a
dissolve, a centroid, a convex hull). The demonstration in
[02 Vector Data Model and Attribute Operations](02-vector-data-model.md)
measures exactly this: a group-by that returns three rows from forty, with no
geometry that corresponds to any of them.

### 1.2 Attributes

An attribute is a measurement attached to a feature. Two properties matter for
everything that follows.

* **Type.** An attribute is nominal (a class name), ordinal (a rank),
  interval or ratio (a physical quantity with a unit). `ndvi_mean` is a ratio
  quantity with no unit; `land_cover` is nominal. Arithmetic on a nominal
  attribute is meaningless, and the mean of a class code is a number that is not
  a class — a point developed in
  [04 Map Algebra and Raster Analysis](04-map-algebra.md).
* **Completeness.** Missing values are common, and the default behaviour of
  most libraries is to drop them silently. The raster module shows the same
  failure in the other data model: five missing rows out of forty reduce a
  group-by to 35 rows without a warning.

### 1.3 Topology

**Topology** is the set of relationships between features that survive a
continuous deformation: adjacency, containment, connectivity, and the rules a
coverage must obey. It is the part of GIS that is *not* in the attribute table
and *not* in the coordinates.

The canonical example is a **planar partition** (or *coverage*): a set of
polygons whose interiors are disjoint and whose union is exactly the study area.
The demonstration builds one by slicing a 100 km × 60 km area into four strips:

$$A_{\text{sum}} = \sum_{i=1}^{4} A_i = 6000.000\ \mathrm{km^2},
\qquad A_{\text{union}} = 6000.000\ \mathrm{km^2},
\qquad A_{\text{sum}} - A_{\text{union}} = 0.000\ \mathrm{km^2}.$$

The residual is exactly zero — not approximately — because the shared cuts are
placed at coordinates that are exactly representable in binary floating point
(multiples of 1/4 km). This is the *additivity invariant*:

$$
\sum_i A_i
\begin{cases}
= A_{\text{union}} & \text{valid partition (no gaps, no overlaps)}\\
> A_{\text{union}} & \text{overlaps present}\\
< A_{\text{union}} & \text{gaps present.}
\end{cases}
$$

The sign of the residual therefore tells you *which* topological error you have,
before you look at anything. A coverage with both errors has a residual of
either sign and a union that is smaller than the nominal area — as the next
section measures.

### 1.4 Coordinate reference system

A coordinate reference system (CRS) is the rule that turns the numbers in the
geometry column into positions on the Earth: a datum (which ellipsoid, which
realisation), a projection (how the curved surface is flattened), and a unit.
The unit is the part that gets ignored. The demonstration prints
`EPSG:32633 (units = metre)` for one synthetic layer and measures what happens
when the units are not lengths at all:

| quantity | value |
|---|---|
| planar area of a 0.10° × 0.10° synthetic box in EPSG:4326 | 0.01000000 deg² |
| same box projected to UTM 31N | 123.3211 km² |
| geodesic area on the WGS84 ellipsoid | 123.0907 km² |
| projection distortion | +0.2304 km² (+0.1872 %) |

A degree is not a length. `0.01 deg²` is not an area, and a "distance" computed
in EPSG:4326 is a difference of angles. Both of the meaningful numbers above
differ from each other by 0.19 %, and *both are correct*: they answer different
questions. The geodesic area is the area on the ellipsoid; the projected area is
the area in the map's own plane, which is what a printed map shows and what a
plane-geometry buffer or overlay actually operates on.

## 2. Worked example: the cost of a one-metre digitising error

A digitised boundary is never exact. Suppose a surveyor closes a strip of the
partition 1 m short on each side. The nominal strip is 25 km wide and 60 km long
in the synthetic frame, so the affected cut length is 60 km.

* The **gap area** lost is
  $1\ \mathrm{m} \times 60\ \mathrm{km} = 0.001\ \mathrm{km} \times 60\
  \mathrm{km} = 0.060\ \mathrm{km^2}$ per cut, i.e. $0.120\ \mathrm{km^2}$ for
  two cuts. Relative to the strip area of $25 \times 60 = 1500\ \mathrm{km^2}$:
  $0.120/1500 = 0.008\%$.
* The demonstration prints exactly this: an area error of
  `0.120000 km^2 (0.008000 %)` for both the shrunk and the grown strip.

A 0.008 % area error is negligible. The *topological* consequence is not:

```
shrunk (gap of 1 m each side): touches the neighbours -> False / False
  boundary-to-boundary distance -> 1.000 m, 1.000 m
grown  (overlap 1 m each side): touches the neighbours -> False / False
  boundary-to-boundary distance -> 0.000 m, 0.000 m
```

Three facts, each worth stating separately:

1. **The predicate answers first.** `touches` is the specification "interiors
   are disjoint and boundaries intersect". Neither strip satisfies it. Adjacency
   in a GIS is therefore a *tolerance-dependent* statement: either you snap
   vertices to a grid (and silently move them), or you keep an untidy coverage
   and report slivers and double-counted overlaps. There is no third option.
2. **Distance zero is not adjacency.** The grown strip's boundary distance to
   its neighbours is 0.000 m and it still does not *touch* them, because its
   interior overlaps theirs. A test written as "distance < tolerance → adjacent"
   gives a different answer from the predicate, and both cannot be right.
3. **Gaps and overlaps do not cancel.** The synthetic 20-strip experiment with
   an independent Gaussian vertex error of σ = 3 m on every cut gives:

| quantity | value |
|---|---|
| nominal study area | 6000.000 km² |
| sum of the 20 strip areas | 6000.617 km² (+0.0103 %) |
| union of the 20 strips | 5998.800 km² (−0.0200 %) |
| overlap (sum − union) | 1.817 km² |
| gap (nominal − union) | 1.200 km² |

The sum is *larger* than the nominal area because perturbed neighbours overlap;
the union is *smaller* because the same perturbation opens gaps elsewhere. A
zonal total computed as a sum over strips is biased high by
$(6000.617-5998.800)/5998.800 = +0.0303\%$ of the union area, and the coverage
as drawn does not tile the study area at all. Overlap and gap are independent
errors of opposite sign, and the sum/union pair is what diagnoses them.

## 3. The Euler count: checking a coverage without looking at it

Area additivity detects that *something* is wrong. A topological count says
*what* is wrong. Treat the four-strip partition as a planar graph: two rows of
five grid nodes, ten boundary edges (four along the bottom, four along the top,
two sides) and three internal cuts.

$$
V = 10,\qquad E = E_{\text{boundary}} + E_{\text{internal}} = 10 + 3 = 13,
\qquad F_{\text{bounded}} = 4,
$$

$$
V - E + F_{\text{bounded}} = 1
\quad\text{(on a disk, outer face excluded)},\qquad
V - E + F_{\text{total}} = 2
\quad\text{(the Euler formula, outer face included)}.
$$

The two are the same statement counted two ways, and
$V - E + F_{\text{bounded}}$ is the quantity to compute when validating a
coverage. The incidence identity $2E = 4F + E_{\text{boundary}} = 16 + 10 = 26$
holds because every block is a quad: each internal edge is counted twice, each
boundary edge once.

Why these counts matter in practice: a **sliver** — a hair-thin polygon created
when a boundary does not close — is a bounded face that should not exist. An
unexpected rise in $F_{\text{bounded}}$ above the number of map units is the
signature. The raster and vector modules both revisit the sliver, because it is
the same defect seen in two data models.

## 4. Simple-feature predicates

Topology is queried through **predicates**: named, boolean-valued relationships
whose names are part of a specification (OGC Simple Features).

| predicate | true when |
|---|---|
| `within` | the first geometry's interior lies in the second's interior, and boundaries may touch only partially |
| `intersects` | the geometries share at least one point (interior or boundary) |
| `touches` | interiors are disjoint and boundaries intersect |
| `contains` | the converse of `within` |
| `crosses`, `overlaps` | partial-dimensional and same-dimensional partial overlap |

The demonstration places six synthetic sites and asks which block each is
"in":

```
  site   x (km)   y (km)   within block   on a polygon boundary
  S00     10.0     30.0      alpha       False
  S01     30.0     30.0       beta       False
  S02     50.0     30.0        -          True
  S03      0.0     30.0        -          True
  S04    110.0     30.0        -         False
  S05     75.0     45.0        -          True
```

S02 sits exactly on the shared cut between `beta` and `gamma`; S03 sits exactly
on the outer boundary of `alpha`; S05 on the second internal cut. None is
`within` any block. That is not a bug: `within` requires the point's *interior*
to lie in the polygon's *interior*, and a point on a boundary has empty
interior. A join written with `within` therefore silently drops every
boundary site, and a join written with `intersects` assigns every boundary site
**twice**. Both answers are correct implementations of two different questions.

The right procedure is mechanical:

1. Name the predicate.
2. Predict the row count: for $n$ sites and $m$ boundary coincidences,
   `within` gives $n$ rows (only sites strictly inside), `intersects` gives
   $n + m$ rows.
3. Compare the actual row count with the prediction, and stop if they differ.

Measured on the synthetic layer with 45 sites, five of them on the cut, the
vector-model demonstration reports 45 rows under `within` and 50 under
`intersects` — exactly the predicted counts.

## 5. Representation is not geometry

Two syntactically different geometries can be equal:

```
  signed area of a counter-clockwise ring = +100.0 km^2
  reversed ring signed area               = -100.0 km^2
  equals(...)                             = True
```

Shapely normalises ring orientation on construction, so `Polygon(ring)` and
`Polygon(ring[::-1])` are `equals()` and have the same orientation when printed.
The signed area computed by the shoelace formula does *not* agree, because it is
orientation-sensitive by definition:

$$
2A_{\text{signed}} = \sum_i \left(x_i y_{i+1} - x_{i+1} y_i\right).
$$

This is the mechanism behind the invalid-polygon trap measured in
[02 Vector Data Model and Attribute Operations](02-vector-data-model.md): a
self-intersecting "bow-tie" ring has two lobes of opposite orientation, and its
shoelace sum is exactly 0 for a shape that encloses 2.000000 km². The reported
area is a plausible-looking number and it is meaningless.

## Assumptions and regime of validity

Every result in this lesson rests on the following, and each one fails
somewhere:

1. **Coordinates are in a single CRS, expressed in metres.** The frames used
   here are synthetic local projections with 1 m coordinates. Any result
   expressed in km² assumes exactly that. Real data usually arrive in degrees
   and must be projected before any metric operation.
2. **The plane is a good model of the surface.** Planar geometry
   (`buffer`, `area`, `intersects`) treats the coordinate plane as flat. Over
   the 100 km extent used here the distortion of a projected CRS is small, but
   an overlay spanning several degrees of latitude accumulates it — see the
   degree-versus-metre measurement in §1.4.
3. **Floating-point coordinates are exact enough to compare.** Exact
   predicates (`touches`, `equals`) are only exact with respect to the numbers
   supplied. The 1 m perturbation in §2 is far larger than float64 round-off and
   therefore makes `touches` false; a 1 nm perturbation would too, for the same
   reason. Snapping is a decision, not a repair.
4. **Attributes and geometry are consistent.** A group-by that drops geometry
   breaks this, and nothing raises an error.
5. **Topology is a property of the dataset as a whole.** No single row can be
   checked for validity in isolation: adjacencies, gaps and overlaps are
   relations between rows.

## 7. What a GIS cannot tell you

Three questions recur in every GIS project and none of them is answerable from
the data:

* **Is the coordinate right?** A layer in the wrong CRS is a plausible-looking
  map shifted by kilometres. Only the metadata and a sanity check against an
  independent measurement can detect it.
* **Is the boundary the boundary?** A crisp polygon edge is a *decision* about
  where a gradual transition was placed. The area of the polygon is exact; the
  area of the thing it names is not.
* **Is the coverage complete?** A layer has no way to represent the part of the
  study area that nobody digitised. The gap term in §2 is the only trace it
  leaves.

## Python demonstration

[`code/gis_concepts_demo.py`](code/gis_concepts_demo.py) builds every object in
this lesson in memory and prints labelled results with units. It:

1. prints an attribute schema and a declared CRS with its unit;
2. verifies area additivity on an exact planar partition;
3. measures touching, gap and overlap behaviour under a 1 m digitising error;
4. measures the double-counting and gap bias of a 20-strip synthetic coverage;
5. evaluates five site predicates against two candidate blocks and reports the
   row count each predicate produces;
6. compares planar-degrees, projected and geodesic areas of the same box, and
   prints the length of one degree of longitude at the equator and at 60° N;
7. checks ring-orientation equality and the Euler/incidence counts of the
   partition.

Run it with the project virtual environment:

```bash
cd 17-remote-sensing-gis/05-gis-fundamentals/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gis_concepts_demo.py
```

The demo is print-only: no figures, no files, no network. It requires
`geopandas`, `shapely` and `pyproj`, all of which are in the project
environment. It exits 0.

## Exercises

Full sets with worked solutions are in
[`exercises/01-gis-concepts-exercises.md`](exercises/01-gis-concepts-exercises.md)
and
[`exercises/01-gis-concepts-solutions.md`](exercises/01-gis-concepts-solutions.md).

- **★** Read an affine geotransform and compute a cell centre.
- **★★** Diagnose a coverage from its sum, union and vertex errors.
- **★★★** Design a validation procedure for a digitised coverage that reports
  gaps, overlaps and slivers separately.

## Mastery checkpoint

Without notes:

> A synthetic coverage divides a 40 km × 25 km area into 8 strips. **(a)** What is
> the nominal area, and what are the two invariants you would test on it?
> **(b)** The sum of the strip areas is 1000.60 km² and the union is 999.74 km².
> State how much of the discrepancy is overlap and how much is gap, and which
> sign of each you can infer. **(c)** A site lies exactly on the boundary between
> strips 3 and 4. Under `within` how many rows does it produce, and under
> `intersects` how many? **(d)** Explain in one sentence why a digitising
> tolerance of 1 m cannot be reported as a zero area error.

A worked version of (a)–(c) is in the
[solutions](exercises/01-gis-concepts-solutions.md).

## Common pitfalls

1. **Computing an area or length in a geographic CRS.** The number is
   meaningless and nothing warns you.
2. **Assuming `within` returns every site that looks inside on the map.** Sites
   on a boundary are excluded by specification.
3. **Treating row counts as invariant across a join predicate.** They are not,
   and the difference is exactly the boundary set.
4. **Snapping without recording the tolerance.** The tolerance is part of the
   result.
5. **Judging topology from a rendered map.** Slivers and overlaps are invisible
   at the scales maps are usually printed at.
6. **Measuring the area of a self-intersecting ring.** Arithmetic succeeds and
   the answer is wrong.
7. **Forgetting that a group-by destroys geometry.** The attribute summary and
   the geometry no longer describe the same objects.

## Related modules

- [02 Vector Data Model and Attribute Operations](02-vector-data-model.md) —
  the same layer idea with joins, spatial predicates and validity.
- [03 Raster Data Model, Resolution and Resampling](03-raster-data-model.md) —
  the other data model, where area is counting rather than geometry.
- [06-gis-fundamentals README](README.md) — the module map and run commands.
- [03-09 Geospatial Python](../../03-scientific-computing/09-geospatial-python/README.md) —
  the library-level treatment of Shapely and GeoPandas.
- [03-08 Gridded Geospatial Data](../../03-scientific-computing/08-gridded-geospatial-data/README.md) —
  xarray, NetCDF and rasterio for larger and multidimensional rasters.
- [Advanced Geospatial Analysis](../06-geospatial-analysis-advanced/README.md) —
  what becomes possible once layers and topology are sound.

## Self-assessment checklist

- [ ] I can name the four ingredients of a GIS and say which one carries the
      units.
- [ ] I can read an affine geotransform and find a cell centre and a cell corner.
- [ ] I can compute the sign of the additivity residual and interpret it.
- [ ] I can count $V$, $E$ and $F$ for a simple partition and check the Euler
      identity.
- [ ] I can explain why `within` and `intersects` disagree on a boundary site.
- [ ] I can convert a claimed area in a geographic CRS into a warning.
- [ ] I can state three questions a GIS cannot answer from its own data.

