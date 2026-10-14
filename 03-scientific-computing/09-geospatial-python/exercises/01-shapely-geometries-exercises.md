# Exercises — 03-09-01 Shapely Geometries and Planar Operations

Attempt these **closed-book** before opening the
[solutions](./01-shapely-geometries-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems that say "run the demo" refer to
[`../code/shapely_geometries_demo.py`](../code/shapely_geometries_demo.py); report
its **actual** output. All geometries are **SYNTHETIC** and built in code. No data
is downloaded.

---

## ★ Foundational

**★1.** For `Point`, `LineString` and `Polygon`, state which of `.length` and
`.area` is meaningful, and in what units.

**★2.** A `Polygon` has `area = 3.0000`. Give two different CRSs in which that
number means two different physical areas, and compute both.

**★3.** Convert a 1° separation to kilometres for (a) latitude at 40°N and
(b) longitude at 0°, 40° and 70°N.

**★4.** State the OGC difference between `contains`, `covers` and `intersects` for
a point exactly on a polygon's boundary.

---

## ★★ Applied

**★★5.** Run the demo, Section 2.
(a) Report shapely's distance and the geodesic distance for a 1° longitude
separation at each of the five latitudes.
(b) Report the km-per-degree values.
(c) Explain why a single constant of 111,132 m/deg cannot fix this, quoting the
measured latitude value at 40°N.

**★★6.** Run the demo, Section 4.
(a) Report the two semi-axis lengths of `buffer(0.05)` at 60°N and the percentage
by which the east–west axis is shorter.
(b) Report the degree-buffer area, the analytic ellipse area and a circle's area
for the same radius.
(c) Report the metric buffer's area and its error against $\pi r^{2}$.
(d) State the repair.

**★★7.** Run the demo, Section 5.
(a) Report `is_valid`, the reason string, and the reported area of the bow-tie.
(b) Report what `make_valid` returns and its area.
(c) Report what `buffer(0)` returns and its area.
(d) State which repair you would use and why.

**★★8.** Run the demo, Sections 7 and 8.
(a) Report the number of points tested in one vectorised call and the fraction
inside.
(b) Report the buffer area of a point buffered by 0.01° and compare with
$\pi r^{2}$.
(c) Report the polygon's vertex count, area, vertex mean and centroid, and the
distance between the last two.

---

## ★★★ Research-oriented

**★★★9.** Design a metric "corridor" of width 2 km around a 200 km survey line
given in lon/lat. Specify every step, run it, and report: the number of densified
vertices, the corridor area in km², and the geodesic length of the centreline.
Then compute the same corridor by buffering in degrees and report the area error as
a percentage of the metric value. State the latitude at which you did it.

**★★★10.** The demonstration's 10° segment at 60°N has a geodesic length of
557.469 km, a parallel arc of 558.048 km, a 2-vertex projected length of 558.182 km
and a 201-vertex projected length of 558.717 km. Construct an experiment that
determines how the 2-vertex projection error grows with segment length, from 1° to
40°, at 60°N. Report a table, fit the growth, and state the rule for when
densification is required for a 0.1 % length accuracy.

**★★★11.** Write a 300–450 word methodology section for a paper that reports
polygon areas for 500 catchments spread from 30°N to 70°N. It must specify the CRS
and why, the area algorithm, the expected error, and the check you would run on the
output. Use the measured numbers from the demo and the companion
[02 GeoDataFrame, CRS Handling and Spatial Joins](./02-geopandas-basics-exercises.md)
wherever they apply, and mark where you are reasoning rather than measuring.
