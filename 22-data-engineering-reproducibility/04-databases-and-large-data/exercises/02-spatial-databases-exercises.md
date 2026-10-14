# Exercises — 22-04-02 Spatial Databases and PostGIS

Attempt these before reading the
[solutions](./02-spatial-databases-solutions.md). The lesson is
[02 Spatial Databases and PostGIS](../02-spatial-databases.md). All numbers refer to the
**SYNTHETIC** model of `code/spatial_databases_demo.py`: 200 000 points over
$11° \times 10°$, a $1° \times 1°$ query box, tile sizes from $0.05°$ to $1°$, spherical
distances on a 6371.0088 km sphere.

## ★ Foundational

**★1.** State the two-stage structure of a spatial query and the role of each stage.

**★2.** For the demonstration's point set and query box: (a) compute the area fraction
the box covers; (b) state the number of points returned and the number of tests
required without an index; (c) explain in one sentence why the two are unrelated.

**★3.** Compute the spherical distance between two points 0.5° apart in latitude at the
same longitude, using $1° \approx 111.19$ km, and state the planar approximation's error
at that separation (from the lesson's table).

## ★★ Applied

**★★4.** Using the tile table: (a) state the candidate counts for tiles of $0.1°$,
$0.25°$ and $0.5°$; (b) compute the candidate-to-hit ratio for each, given 1 850 hits;
(c) state which tile you would choose for a workload dominated by $1°$ boxes and why.

**★★5.** A spatial join is planned between a 200 000-point set and a 100 000-point set,
keyed by $0.25°$ tiles.

(a) State the candidate count and the reduction against the quadratic baseline.
(b) Explain why the true candidate count is larger once neighbouring tiles are included,
and compute the worst-case multiplication. (c) State the refinement predicate that
decides membership.

**★★6.** A distance query asks for stations within 25 km of a site, and the station
coordinates are stored in degrees while the distance formula treats its inputs as
kilometres.

(a) State the factor by which the answer is wrong. (b) State the observable symptom on
the plan and in the result. (c) State the test that would have caught it.

## ★★★ Research-oriented

**★★★7.** Design a spatial-temporal schema for 50 years of regional seismicity
(5 million events) supporting (i) radius searches around a site, (ii) events in a
time window, (iii) catalogue cross-matching with another network, and (iv) coverage
maps on a $0.1°$ grid. State the geometry type, the reference system, the indices, the
precomputed columns, and the one query your design makes expensive. State what you would
measure.

**★★★8.** The lesson's planar error grows to 3 % at 45° of separation. Derive the
leading term of the planar approximation's relative error as a function of separation
and latitude, check it against the tabulated values, and state the separation at which a
0.1 % tolerance is exceeded at latitude $45°$. State what the derivation ignores.

**★★★9.** A group cross-matches two catalogues by position with a 10 km threshold and
finds that 3 % of their "unique" events are duplicates when the threshold is raised to
30 km. Quantify the trade-off: state the quantities that decide the threshold, design
the measurement that estimates them from the data, and state what the measurement cannot
tell you about the physically distinct pairs near the threshold.
