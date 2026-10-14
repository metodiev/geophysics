# Exercises — 17-05-01 GIS Concepts: Layers, Attributes and Topology

Attempt these before reading the
[solutions](./01-gis-concepts-solutions.md). The lesson is
[01 GIS Concepts](../01-gis-concepts.md). All models are **SYNTHETIC** teaching
values.

## ★ Foundational

**★1.** A raster has a transform with $a = 200$ m, $e = -200$ m, $c = 300\,000$ m,
$f = 5\,800\,000$ m, $b = d = 0$. State the coordinate of the centre of the cell
at (row, col) = (0, 0) and at (row, col) = (4, 7), and the coordinate of the
upper-left **corner** of the grid.

**★2.** A layer's geometry column contains 4 polygons with areas 12.0, 7.5, 9.25
and 11.25 km². The union of the four has an area of 39.5 km². State whether the
layer is a valid planar partition, and if not, whether the residual indicates
overlap or gaps. Show the arithmetic.

**★3.** A synthetic 0.2° × 0.2° box is stored in EPSG:4326. State the three
different areas you could compute (planar degrees, projected, geodesic) and say
which one is a physical area.

## ★★ Applied

**★★4.** A digitised coverage divides a 50 km × 20 km area into 10 strips. Each
internal cut is misplaced by 2 m over its full length. Compute the total overlap
area and the total gap area in km², and the percentage of the study area each
represents.

**★★5.** A synthetic point layer has 200 sites, 15 of which lie exactly on a
polygon boundary. State the number of rows produced by a spatial join to the
polygon layer under `within`, under `intersects` and under `touches`, and explain
each.

**★★6.** A colleague reports the area of a lake as "0.008 deg²". Convert that to
km² assuming the lake is at 0° N and that 1° of longitude is 111.319 km and 1° of
latitude is 110.574 km, and state the two assumptions the conversion makes.

## ★★★ Research-oriented

**★★★7.** Design a validation procedure for a digitised coverage of 5 000
polygons that reports gaps, overlaps, slivers and invalid rings separately. State
the metric you compute for each, the threshold you would use to flag a defect, and
how you would order the checks so that the cheapest failure is detected first.

**★★★8.** A study reports a land-cover area in a geographic CRS. Write the
argument you would make for or against accepting it, including one quantity you
would compute to bound the error, and state what additional metadata would settle
the question without recomputation.
