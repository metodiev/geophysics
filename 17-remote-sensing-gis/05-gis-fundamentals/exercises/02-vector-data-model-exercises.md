# Exercises — 17-05-02 Vector Data Model and Attribute Operations

Attempt these before reading the
[solutions](./02-vector-data-model-solutions.md). The lesson is
[02 Vector Data Model](../02-vector-data-model.md). All models are **SYNTHETIC**.

## ★ Foundational

**★1.** A layer holds 100 points, 250 lines and 40 polygons. State the total
`.area` a naive sum would report if the polygons total 1 250 km², and explain what
the sum means.

**★2.** A left table has 300 sites; a right table has 900 measurements, of which
a site has either 2 or 5. State the expected joined row count if 60 sites have 5
measurements and the rest have 2.

**★3.** A ring is given by the four vertices (0,0), (4,0), (4,3), (0,3). Compute
its signed area by the shoelace formula, then state what the formula returns if
the vertices are listed in the reverse order.

## ★★ Applied

**★★4.** A join multiplies 300 sites to 900 measurement rows, with the
25 sites that carry 5 measurements having a mean of 15.0 and all others 10.0.
Compute the row-mean and the site-mean and state the bias.

**★★5.** A synthetic point layer has 1 000 sites, 40 of them exactly on polygon
boundaries. Predict the row count of a spatial join under `within` and
`intersects`, and state which one you would use for a per-polygon site count.

**★★6.** A bow-tie ring has lobes of 3.5 and 2.5 km² with opposite orientation.
State the area the shoelace formula returns, the area after repair, and the
number of parts the repaired geometry contains.

## ★★★ Research-oriented

**★★★7.** Design the join sequence for a study that combines a site layer, a
laboratory table with repeated analyses and a polygon layer, so that the unit of
analysis is explicit at every step. State the row count you expect at each step
and the assertion you would place between steps.

**★★★8.** A spatial index is built over a layer of long thin synthetic polygons
(average aspect ratio 20:1). Estimate, to within a factor of two, how the
candidate pair count compares with a layer of compact polygons of the same count
and total area, and state which measurement on the actual data would settle it.
