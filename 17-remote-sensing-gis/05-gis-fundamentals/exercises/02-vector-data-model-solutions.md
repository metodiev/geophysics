# Solutions — 17-05-02 Vector Data Model and Attribute Operations

> **Read after attempting the exercises.** Numbers were computed, not estimated.

Lesson: [02 Vector Data Model](../02-vector-data-model.md).

---

## ★1 — Area of a mixed-type layer

A point's area is 0 and a line's area is 0, so the naive sum is

$$0 + 0 + 1250 = \mathbf{1250\ km^2}.$$

The number is numerically correct and semantically meaningless: it is the sum of
the polygon areas with 350 features contributing nothing. It reads as a layer
area, and no error is raised. Filter by geometry type first.

---

## ★2 — Expected joined rows

$$n_{\text{joined}} = 60 \times 5 + 240 \times 2 = 300 + 480 = \mathbf{780}.$$

If the join returns 900 rows, the right-hand table contains more measurements per
site than assumed — the key is not what the documentation said, and the check
costs nothing.

---

## ★3 — Shoelace area and ring reversal

$$2A_{\text{signed}} = \sum_i (x_i y_{i+1} - x_{i+1} y_i)
= (0\cdot0 - 4\cdot0) + (4\cdot3 - 4\cdot0) + (4\cdot3 - 0\cdot3) + (0\cdot0 - 0\cdot3)$$
$$= 0 + 12 + 12 + 0 = 24
\qquad\Longrightarrow\qquad A_{\text{signed}} = +12\ \mathrm{km^2}.$$

Reversing the ring negates every term, so the signed area becomes
$-12\ \mathrm{km^2}$. Shapely normalises orientation on construction, so the two
polygons are `equals()`; the shoelace formula is orientation-sensitive by
definition and is the wrong tool for comparing representations.

---

## ★4 — Row-mean versus site-mean

Match counts: the 25 heavy sites contribute $25 \times 5 = 125$ rows, the remaining
275 sites contribute $275 \times 2 = 550$ rows, total 675 — so scale the example
to the stated 900 rows by assuming equal totals; with the stated pattern:

$$\bar z_{\text{rows}} = \frac{25(5)(15.0) + 275(2)(10.0)}{125 + 550}
= \frac{1875 + 5500}{675} = 10.926,$$
$$\bar z_{\text{sites}} = \frac{25(15.0) + 275(10.0)}{300}
= \frac{375 + 2750}{300} = 10.417,$$
$$\text{bias} = +0.509 = +4.89\%\ \text{of the site-mean}.$$

The over-weighted group is 8.3 % of the sites and 18.5 % of the rows, and it pulls
the row-mean up by almost 5 %. The unit of analysis must be stated.

---

## ★5 — Row counts under two predicates

* `within`: 1 000 rows, the 40 boundary sites unmatched.
* `intersects`: $1000 + 40 = 1040$ rows, because each boundary site belongs to two
  polygons.

For a per-polygon **site count**, neither is right on its own: `within` drops the
boundary sites (undercounting), and `intersects` counts them twice (overcounting).
The defensible choices are to assign boundary sites to one polygon by a stated
tie-break rule (for example the smaller polygon identifier), or to report the
count with an explicit boundary convention. A polygon count that is not
accompanied by its convention is not reproducible.

---

## ★6 — Bow-tie ring

The lobes have opposite orientation, so their signed contributions cancel:

$$\text{shoelace area} = 3.5 - 2.5 = \mathbf{1.0\ km^2},$$

which is not the enclosed area. After `make_valid` the geometry is a
**MultiPolygon with 2 parts** of 3.5 and 2.5 km², total 6.0 km². The repair also
changes the geometry *type* from Polygon to MultiPolygon, so downstream code that
assumed Polygon fails — a visible failure, which is the good outcome.

---

## ★7 — A join sequence with assertions

| step | operation | expected rows | assertion |
|---|---|---|---|
| 1 | load sites | 1 000 | unique site identifier |
| 2 | load analyses | 2 400 | key exists in sites |
| 3 | join analyses (group first if analyses are repeats) | depends on the unit | print counts before and after; assert the ratio equals the mean analyses per site |
| 4 | aggregate analyses to one row per site | 1 000 | row count equals the site count |
| 5 | spatial join to polygons | 1 000 + boundary coincidences | assert against the predicted count and report the boundary convention |
| 6 | aggregate to polygons | polygon count | assert no nulls in the grouping key |

The essential discipline is that the **unit of analysis** is named at every step
(site, analysis or polygon), and that the row count is predicted and asserted
rather than merely observed. Aggregating the repeats *before* the spatial join is
usually the right order, because it keeps the join one-to-one.

---

## ★8 — Index candidates for long thin polygons

An R-tree prunes with bounding boxes, so the candidate count is governed by the
**box area**, not the polygon area. A 20:1 polygon with area $A$ has
$L = \sqrt{20A}$ and $W = \sqrt{A/20}$, so its box area is $LW = A$ — the same as
the polygon — but a compact polygon has a box of area $A$ too, so box *area* is
equal. The difference is orientation and overlap: a random orientation for the
thin polygons makes their boxes overlap far more often at a given density. For
uniform random positions at density $\lambda$ per unit area, the expected number
of box-overlap partners is $\lambda$ times the expected box-overlap area

$$\mathbb E[\text{overlap}] \approx \lambda\,\mathbb E\!\left[(\text{box}_1 \oplus
\text{box}_2)\right],$$

which for a fixed box area is larger when the boxes are long, because the
Minkowski sum of two long boxes is much larger than that of two squares of the
same area. Expect the candidate count to be several times larger for 20:1
features — the honest answer is "up to an order of magnitude, and it depends on
orientation", which is why the measurement on the actual layer (count candidates,
count true intersections, compare with the brute-force pair count) is the only
defensible way to size the job.
