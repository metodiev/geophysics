# Solutions — 22-04-02 Spatial Databases and PostGIS

> Read after attempting. Numbers are computed here and match the demonstration's
> printed output. Lesson:
> [02 Spatial Databases and PostGIS](../02-spatial-databases.md).

---

## ★1 — The two stages

- **Filter**: the spatial index produces a set of **candidates** whose bounding boxes or
  cells could satisfy the predicate — cheap, approximate, and always a superset.
- **Refine**: an exact geometric predicate (point-in-polygon, exact distance) decides
  membership for each candidate.

The filter is what makes the query sub-linear; the refine step is what makes it correct.
Treating an index hit as a result is the classic spatial-query bug, and it is why the
candidate-to-hit ratio is the metric to watch.

## ★2 — Box query on the demonstration's point set

(a) Box area fraction: the region is $11° \times 10° = 110\ \text{deg}^{2}$ and the box
is $1° \times 1° = 1\ \text{deg}^{2}$, so the fraction is
$1/110 = 0.9091\ \%$ — the printed value.

(b) 1 850 points are returned (the printed value), and without an index the query tests
all 200 000 = **0.20 M** points.

(c) The two are unrelated because a scan's cost is set by the **table size**, while the
answer size is set by the **query extent and the density**; a smaller table and a bigger
box can return the same 1 850 points, and only the box's area fraction connects them.

## ★3 — A 0.5° meridional distance

$0.5° \times 111.19\ \text{km/°} = 55.6$ km. From the lesson's table the planar error is
0.000 % at 0.1° and 0.001 % at 1°, so at 0.5° the error is below 0.001 % — under a metre.
The planar approximation is safe at this scale; the interesting failures are ten times
larger separations or a wrong reference system.

## ★★4 — Choosing a tile

(a) Candidates: $0.1° \to 2\,200$; $0.25° \to 2\,841$; $0.5° \to 4\,091$.

(b) Candidate-to-hit ratios against 1 850 hits: $0.1° \to 1.19$; $0.25° \to 1.54$;
$0.5° \to 2.21$.

(c) Choose **$0.1°$**: it gives the smallest candidate set (ratio 1.19, only 19 % waste)
and is the finest of the three, at the cost of the largest index (11 000 tiles against
440). For a workload dominated by $1°$ boxes, a tile a tenth of the query size keeps the
candidate ratio near one. The $0.05°$ tile (ratio 1.08) buys little more and doubles the
index again, so $0.1°$ is the better point on the curve — unless the tiles are so many
that the index no longer fits in memory, in which case $0.25°$ is the practical choice.

## ★★5 — Candidates in a spatial join

(a) Candidate pairs within a shared $0.25°$ tile: **11.36 million**, against
$2 \times 10^{10}$ for the quadratic baseline — a reduction of **1 760×** (all printed).

(b) The true count is larger because a shared-tile rule misses pairs that lie in
**different tiles** while still being within the distance threshold: two points 30 m
apart across a tile edge are in different tiles. Including the eight neighbouring tiles
multiplies the candidate count by up to **9×** in the worst case (every point compared
against every point in nine tiles), giving up to about 102 million candidates — still
three orders of magnitude better than the baseline, but two orders worse than the
shared-tile figure. In practice the neighbour rule is applied only where the threshold
exceeds a fraction of the tile size.

(c) The refinement predicate is the exact distance test: haversine (or an ellipsoidal
formula) against the threshold, applied to each candidate pair. Optionally, an
inequality filter on squared planar distance is used first when the threshold is much
smaller than a tile, since it avoids the trigonometric evaluation.

## ★★6 — Degrees treated as kilometres

(a) One degree of latitude is about 111.19 km, so treating degrees as kilometres
understates distances by a factor of about **111**. A 25 km threshold then admits
everything within $25°$ — i.e. a large part of the planet — or, read the other way, a
query intended to find points at 25 km finds points at ~2 800 km.

(b) Symptom on the plan: a scan (the predicate is not indexed in a form the planner can
use) or an index scan over a huge candidate set. Symptom in the result: far more rows
than expected, with distances in the output that are obviously wrong when compared with a
map, which is exactly the check that is usually skipped.

(c) The test that catches it: a handful of **known pairs** with distances computed
independently (a few metres, a few kilometres, a few thousand kilometres), asserted
against the query's output, with the formula and the coordinate reference system named in
the test. A single assertion on a 25 km radius with a known station at 20 km and another
at 40 km would fail immediately.

## ★★★7 — A spatial-temporal schema for 50 years of seismicity

**Geometry type.** Point (2-D) for event locations, stored with a declared geographic
reference system in degrees, and separately the depth in a numeric column. If the
catalogue must handle events near the antimeridian, store longitude in a convention that
wraps explicitly (or split the catalogue into two longitude ranges).

**Reference system.** Geodetic (WGS 84 or the regional realisation actually used) for
storage, with the datum named — the source catalogue's datum is usually not changeable,
and converting it silently is a reproducibility hazard. Any distance query states whether
it computes on the sphere or on an ellipsoid.

**Indices.** A spatial index on the geometry for radius and cross-match queries; a
composite index on `time` and `magnitude` for time windows and largest-event queries; a
cell or geohash column (precomputed at $0.1°$) with a plain value index for the coverage
maps and cheap candidate generation; and the primary key for joins.

**Precomputed columns.** Cell key at $0.1°$ and at $1°$; a flag for "reviewed" events;
the source network's identifier and its version; and a coarse region label. These make
the common queries index-only and keep the spatial predicate for the cases that need it.

**The expensive query.** *Catalogue cross-matching with another network at a small
threshold*: the candidate pairs come from the neighbour-tile rule and, with 5 million and
(say) 2 million events, the candidate set is large; the refinement step's cost dominates.
Mitigation: pre-cluster by (time, space) into candidate `(time, space)` buckets, and
restrict the cross-match to events within a few seconds, which is a cheap equality
filter before the geometric test.

**What to measure.** For each query shape, the plan, logical and physical reads, the
number of candidates against the number of hits, and the wall time; report the
candidate ratios, because they are the quantity a schema change moves.

## ★★8 — The leading term of the planar error

Write the planar approximation as scaling the angular difference by the mean latitude,
as the demonstration does. For a point at colatitude offset $\varphi$ (the mean latitude)
and an angular separation $\theta$, the exact central angle under the haversine formula
depends on both the separation and the mean latitude, while the planar formula uses a
single scale factor $\cos\varphi$ applied to the longitude difference. Expanding the
spherical law of cosines to leading order in $\theta$ gives

$$\frac{|\Delta d|}{d} \approx \frac{1}{2}\,\theta^{2}\,\sin^{2}\varphi\;\text{(up to the
form of the longitude/latitude split)},$$

so the relative error grows **quadratically** with the separation and with the square of
the sine of the latitude, and it is zero on the equator and at the poles' meridional
direction.

Check against the table (separations at latitude $\approx 37°$, so
$\sin^{2}\varphi \approx 0.36$):

- $\theta = 1° = 0.01745$ rad: $\frac{1}{2}(0.01745)^{2}(0.36) = 5.5 \times 10^{-5}$
  = 0.0055 % — the table gives 0.001 % for a diagonal path, the right order;
- $\theta = 5° = 0.0873$ rad: $\frac{1}{2}(0.0873)^{2}(0.36) = 1.4 \times 10^{-3}$
  = 0.14 % — the table gives 0.025 %, again the right order (the coefficient depends on
  the azimuth of the path, which this leading-order form ignores);
- $\theta = 45° = 0.7854$ rad: $\frac{1}{2}(0.7854)^{2}(0.36) = 0.111$ = 11 % — larger
  than the tabulated 3 %, confirming that the leading-order expansion is not valid at
  such separations and that the exact comparison is the honest one.

**A 0.1 % tolerance at latitude $45°$** ($\sin^{2}\varphi = 0.5$): solve
$\frac{1}{2}\theta^{2}(0.5) = 10^{-3}$, i.e. $\theta^{2} = 4 \times 10^{-3}$,
$\theta = 0.063$ rad $= 3.6°$. So beyond about **3–4 degrees** of separation the planar
approximation exceeds 0.1 % at mid-latitudes.

**What the derivation ignores.** The azimuth of the path (the figure quoted is a
latitude-only path), the ellipsoidal flattening (up to ~0.5 % in distance, independent of
this error), and the choice of scale factor (a different reference latitude changes the
error by an amount that can be larger than the term above). It is a scaling argument, not
an error budget.

## ★★★9 — The cross-match threshold trade-off

**Quantities that decide the threshold.** (i) The **location uncertainty** of each
catalogue (a distribution, not a single number: reported uncertainties are usually lower
bounds, and they vary with network, magnitude and epoch); (ii) the **event density** in
the region, which sets how many physically distinct events fall within any threshold;
(iii) the **pairing rule** (nearest-neighbour within the threshold, or a mutual-best
rule), which changes both the false-duplicate and false-split rates; (iv) the **cost
asymmetry** — a false duplicate merges two real events (losing one from the catalogue),
a false split doubles one event (inflating rate estimates).

**The measurement.** Estimate (i) from the catalogues themselves: for events reported by
both networks with high-confidence manual locations, the distribution of their offset
gives an **empirical location uncertainty**; for events reported by one network only,
the offset distribution against the nearest event of the other network at increasing
thresholds shows the transition from a peak (true pairs) to a flat background (chance
pairs). Fit a two-component model — a peaked component for true pairs and a
density-scaled uniform component for chance pairs — to that offset distribution; the
threshold at which the chance component starts to dominate is the defensible value.

**What the measurement cannot tell you.** Whether a pair *at* the threshold is a duplicate
or two physically distinct events: at 10–30 km, two small earthquakes can genuinely be
distinct, and no positional information can separate them. Resolving those needs an
independent discriminator — origin time, magnitude consistency, waveform similarity,
or the network's own association records — and the honest report states the threshold,
the estimated rates on each side of it, and the number of ambiguous pairs left for a
human or a waveform test.
