# Solutions — 03-09-03 Spatial Indexing, Spatial Joins and Performance

> **Read this after attempting the exercises, not before.** Every value attributed
> to "the demo" is its actual output. Nothing below is a wall-clock timing. All data
> are SYNTHETIC.

---

## ★1 — The cost model

$$T_{\text{naive}} = N \times M, \qquad
T_{\text{indexed}} \approx N\log M + k,$$

with $k$ the total number of candidate pairs returned by the tree. The measured
values below calibrate the constants.

---

## ★2 — Naive count

$2{,}000 \times 400 = \mathbf{800{,}000}$ point-in-polygon tests. The demo prints
exactly this.

---

## ★3 — What an STRtree stores

Each **internal node** stores the bounding box that encloses all of its children;
each **leaf** stores one input geometry's bounding box. A query descends only into
subtrees whose boxes intersect the query's box, so it answers a **bounding-box
intersection** query without evaluating any geometric predicate. Producing the
*answer* requires the caller to evaluate the predicate on each candidate.

---

## ★4 — Why bbox-only is unfinished

Because a bounding-box intersection is a **necessary but not sufficient** condition
for a geometric intersection: two boxes can overlap while the geometries inside
them do not, so the candidate set is a superset of the answer and must be filtered
by a predicate.

---

## ★5 — Brute force versus index

**(a)** **800,000** tests → **1,845** matches; the hit rate is **0.2306 %**, so
**798,155** tests returned nothing (99.77 %).

**(b)** Indexed candidate pairs **1,845**; reduction **433.6×**; the answers are
**identical** (`answer identical to brute force: True`).

**(c)** **0** candidates were rejected, because the cells are axis-aligned
non-overlapping rectangles whose bounding boxes *are* their geometries. The
bbox filter is therefore exact for this dataset — a property to verify rather than
assume.

---

## ★6 — Obliqueness

**(a)** The 40 km × 1 km band rotated 20°, and its bounding box is
**37,930 m × 14,620 m**, i.e. **13.9×** its own area.

**(b)** **648** bbox candidates; **46** confirmed; **602 rejected = 92.9 %**.

**(c)** For oblique geometries the bounding box is a poor proxy, so the predicate
carries most of the filtering work and a bbox-only query overstates the answer by
more than an order of magnitude. **The more oblique the data, the more the
predicate matters.**

---

## ★7 — The grid shortcut

**(a)** 2,000 points; **1,845** matched; **1,845** located by integer division.

**(b)** **0** predicate evaluations — two integer divisions and a range check per
point, then `np.bincount`.

**(c)** The grid method is valid when the **polygons are a regular, gap-free,
non-overlapping lattice** whose origin and spacing are known exactly. Then the cell
index is arithmetic, and the "spatial join" contains no geometry. Any irregularity
— a rotated grid, a missing tile, a different projection for the polygons — breaks
it, and the correct fallback is the tree.

---

## ★8 — Quadrat counts

**(a)** Both routes total **1,845** points and the per-cell counts are **identical**
to within integer equality (`True`).

**(b)** Mean **4.612**, variance **4.253**, ratio **0.922**. For a uniform random
sample the ratio is close to 1, and slightly below 1 is what *uniform* (rather than
Poisson) placement gives: a uniform draw is more evenly spread than a Poisson
process. Values well above 1 indicate clustering; values well below 1 indicate
repulsion or systematic spacing (fixed station intervals, for example).

---

## ★9 — What actually degrades the index

The intuitive answer — "clustered points make the tree work harder" — is **wrong for
non-overlapping cells**, and measuring it is the point of the exercise. Measured
with 2,000 points drawn uniformly and then with 90 % of them concentrated inside 20
of the 400 cells:

| Dataset | Candidates | Confirmed | Candidates per query |
|---|---|---|---|
| uniform | 2,000 | 2,000 | 1.000 |
| clustered | 2,000 | 2,000 | 1.000 |

**No degradation.** The reason is structural: a point can lie in exactly one cell,
so the query needs one cell, and the tree finds it in $O(\log M)$ regardless of
where the other points are. Clustering the *queries* does not change the number of
*candidates* per query.

What does degrade the index is the **size of the query geometry relative to the
data spacing**. Measured with the same 500 points, now buffered into disks of
growing radius and queried with `predicate="intersects"`:

| Query radius | Candidates | Per query | Naive count |
|---|---|---|---|
| 10 m | 505 | 1.01 | 200,000 |
| 500 m | 1,030 | 2.06 | 200,000 |
| 1,000 m | 1,808 | 3.62 | 200,000 |
| 2,000 m | 3,838 | 7.68 | 200,000 |
| 5,000 m | 13,318 | 26.6 | 200,000 |
| 10,000 m | 38,424 | 76.9 | 200,000 |

The candidate count grows roughly as the query's **area**, since a disk of radius
$r$ covers $\pi r^{2}/(2{,}000\ 	ext{m})^{2}$ cells. At $r = 10$ km — five cells —
each query touches 77 cells, and the reduction against brute force has fallen from
396× to 5.2×.

**The rule, and the reason the naive intuition fails.** An index prunes using the
*ratio of the query's footprint to the data's local spacing*: the candidate count is
approximately the number of geometries whose boxes the query's box can reach.
Clustering of the **query** features only matters if the query features themselves
become large (a single multipoint spanning the cluster, a bounding box around a
city). So the question to ask before reaching for a tree is not "is my data
clustered?" but **"how many polygons can a single query plausibly touch?"** — and
then measure it.

## ★10 — Rotation and the bbox filter

Generate one grid of axis-aligned cells, then rotate the same geometries about
their centres by 0°, 15°, 30° and 45°. Measured with the same 2,000 points and the
same 400 cells:

| Rotation | box / area | bbox candidates | predicate confirmed | rejected |
|---|---|---|---|---|
| 0° | 1.00 | 2,000 | 2,000 | **0.0 %** |
| 15° | 1.50 | 2,968 | 1,995 | 32.8 % |
| 30° | 1.87 | 3,654 | 1,975 | 45.9 % |
| 45° | 2.00 | 3,924 | 1,982 | **49.5 %** |

Three observations. The **confirmed** counts stay near 2,000 (1,975–2,000) because
rotation moves a few points out of the rotated cells entirely — the answer is a
property of the geometry, not the index. The **candidate** count nearly doubles by
45°, so the predicate's workload nearly doubles with it. And the rejected fraction
rises to 49.5 %, which is exactly what a box-to-area ratio of 2.00 implies: half
the box, half the candidates useful.

For a single *elongated* shape the effect is much larger — the demonstration's
40 km × 1 km band at 20° has a box-to-area ratio of **13.9** and rejects **92.9 %**
of its 648 candidates.

**The rule.** For an isolated square rotated by $\theta$, the bounding box grows to
$1/\cos\theta$ times the area at small angles and exactly $2.00$ at 45° — measured
1.00, 1.50, 1.87, 2.00 for 0°, 15°, 30°, 45°. So *at most* half of a 45°-rotated
square's candidates can be rejected. For elongated or oblique shapes the ratio grows
without bound: the demonstration's 40 km × 1 km band at 20° has a ratio of 13.9 and
rejects 92.9 %. **When the box-to-area ratio exceeds about 3, expect the predicate
to do most of the filtering work**; below about 2, the bounding-box filter is doing
most of it and the predicate is cheap.

---

## ★11 — Reporting performance without timings

Required content:

**Algorithm.** STRtree (Sort-Tile-Recursive packed R-tree) built over the polygons;
`tree.query(points, predicate="within")` as the candidate generator plus predicate
filter.

**Input sizes.** $N = 2{,}000$ points, $M = 400$ polygons, CRS EPSG:32612.

**Measured counts.** Naive: 800,000 predicate evaluations. Indexed: 1,845 candidate
pairs, 1,845 predicate evaluations, 0 rejected. Reduction: 433.6×. Grid: 0
predicates, 1,845 integer divisions. Answers identical across all four routes.

**Environment.** State the Python and library versions and whether the run was
single-threaded; the counts do not depend on these, but a reader needs to know
whether a timing claim that follows is comparable.

**Two claims not to make from a single timing.**

1. **"A 434× speed-up."** The measured number is a 434× reduction in *predicate
   evaluations*. The wall-clock ratio also includes Python overhead per candidate
   (which favours the index less), vectorisation (which favours it more), and the
   tree's build time (which it ignores entirely). The defensible claim is the count.
2. **"The algorithm scales to 10⁷ points."** A single run establishes nothing about
   scaling: the candidate count per query depends on the *density* of the data and
   the sizes of the query geometries, so a 10⁷-point run in a different spatial
   configuration is a different measurement. The defensible claim is asymptotic
   ($N M$ versus $N\log M + k$) plus the measured $k/N = 0.922$ for this dataset.

**One claim the counts do support** (report it): *"For 2,000 points against 400
axis-aligned cells, the index reduces the number of point-in-polygon tests from
800,000 to 1,845, a factor of 433.6, with identical results. For a rotated band of
the same length the bounding-box filter is much weaker: 648 candidates reduced to
46 matches, so 92.9 % of candidate tests are rejected by the predicate."*

**One claim they do not support** (do not report it): *"The join runs in 12 ms, so
this approach is 100× faster than the naive loop."* The naive loop's timing depends
on the Python-level predicate cost; a vectorised Numpy bounding-box pre-filter could
well beat the tree for $M = 400$, and no measurement here settles that.
