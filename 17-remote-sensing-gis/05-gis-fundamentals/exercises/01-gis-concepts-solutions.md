# Solutions — 17-05-01 GIS Concepts: Layers, Attributes and Topology

> **Read after attempting the exercises.** Where a problem admits more than one
> defensible answer, that is said so. Numbers were computed, not estimated.

Lesson: [01 GIS Concepts](../01-gis-concepts.md).

---

## ★1 — Transform arithmetic

The mapping is $x = a\,\text{col} + c$ and $y = e\,\text{row} + f$ with
$a = 200$, $e = -200$, $c = 300\,000$, $f = 5\,800\,000$.

* Centre of cell (0, 0): add half a cell in each direction,
  $x = 200 \times 0.5 + 300\,000 = 300\,100$ m,
  $y = -200 \times 0.5 + 5\,800\,000 = 5\,799\,900$ m.
* Centre of cell (4, 7): $x = 200 \times 7.5 + 300\,000 = 301\,500$ m,
  $y = -200 \times 4.5 + 5\,800\,000 = 5\,799\,100$ m.
* Upper-left **corner**: $x = c = 300\,000$ m, $y = f = 5\,800\,000$ m.

The distinction between the two conventions is exactly half a cell: 100 m here.

---

## ★2 — Additivity residual

$$\sum A_i = 12.0 + 7.5 + 9.25 + 11.25 = 40.00\ \mathrm{km^2}, \qquad
A_{\text{union}} = 39.50\ \mathrm{km^2},$$
$$\sum A_i - A_{\text{union}} = +0.50\ \mathrm{km^2} = +1.25\%\ \text{of the union}.$$

A positive residual means the sum exceeds the union, so **the coverage has
overlaps**. It is not a valid planar partition. Because a positive residual says
nothing about gaps (they would push the union below the sum too), the next check
is to compare the union with the nominal study area: if the union is smaller than
the nominal area, gaps are also present and the two errors partly cancel.

---

## ★3 — Three areas of one box

* Planar in EPSG:4326: $0.2 \times 0.2 = 0.04\ \mathrm{deg^2}$ — not an area.
* Projected (say UTM 31N): the plane area in the projection's own metric.
* Geodesic: the area on the ellipsoid, computed from the latitudes.

Only the geodesic area is a physical area; the projected area is the area *in the
map's plane*, which is what a plane-geometry buffer or overlay actually operates
on. Both differ, and the difference is the projection distortion — about 0.19 %
for a 0.1° box near the equator (measured in the lesson).

---

## ★4 — Two-metre misplacement of ten cuts

Strip length is 20 km (the cut runs the full 20 km dimension), and there are
9 internal cuts in a 10-strip partition.

Overlap: two strips of 50 km width... rather, each internal cut misplaced by 2 m
in the same direction opens a gap of 2 m × 20 km on one side and an overlap of
the same size on the other:
$$A_{\text{gap}} = A_{\text{overlap}} = 9 \times (0.002\ \mathrm{km} \times
20\ \mathrm{km}) = 9 \times 0.04 = 0.36\ \mathrm{km^2}.$$

Study area $= 50 \times 20 = 1000\ \mathrm{km^2}$, so each error is
$0.36/1000 = 0.036\%$. The sum of the strip areas exceeds the union by
$2 \times 0.36 = 0.72\ \mathrm{km^2}$, and the union falls short of the nominal
area by $0.36\ \mathrm{km^2}$ — the same signature as the lesson's measured
20-strip example.

---

## ★5 — Row counts by predicate

* `within`: 200 rows. The 15 boundary sites match nothing and are kept with a null
  match under a left join; no site can match two polygons, because `within`
  excludes the boundary from both.
* `intersects`: $200 + 15 = 215$ rows, because each boundary site lies in **two**
  polygons.
* `touches`: 0 matched. `touches` requires **disjoint interiors**, and a point's
  interior is empty, so a point cannot touch a polygon — the predicate is not
  applicable to a point-to-polygon join. A tool that accepts it silently returns
  no matches.

The general rule: `within` gives $n$ rows, `intersects` gives $n + m$ for $m$
boundary coincidences, and a predicate whose dimensional preconditions are not
met returns nothing without complaint.

---

## ★6 — From square degrees to square kilometres

$$0.008\ \mathrm{deg^2} = 0.0894° \times 0.0894°\ \text{(if square)},$$

and 1° of longitude is 111.319 km at 0° N while 1° of latitude is 110.574 km, so

$$A \approx 111.319 \times 110.574 \times 0.008 = 98.47\ \mathrm{km^2}.$$

Two assumptions: (i) the conversion is applied at the **equator**, where 1° of
longitude is longest — at 60° N the same 0.008 deg² is about half that, 49.2 km²;
(ii) the shape is irrelevant only because the area element
$\mathrm{d}A = R^2\cos\phi\ \mathrm{d}\phi\,\mathrm{d}\lambda$ is separable, so
the same conversion factor applies to any shape. The correct value is the
geodesic area, and it requires the actual vertex coordinates, not just the area in
degrees.

---

## ★7 — A coverage validation procedure

Order the checks cheapest-first, and report each metric separately:

| order | check | metric | flag |
|---|---|---|---|
| 1 | ring validity | count of `is_valid == False` | any non-zero |
| 2 | coverage closure | $\lvert \sum A_i - A_{\text{union}}\rvert / A_{\text{union}}$ | > 0 (report sign) |
| 3 | union vs nominal extent | gap area and fraction | > 1e-6 of the extent |
| 4 | overlaps | total pairwise intersection area | > snapping tolerance² |
| 5 | slivers | count of polygons with area < tolerance² | report, do not fix silently |
| 6 | Euler count | $V - E + F_{\text{bounded}}$ per connected component | ≠ 1 |

Checks 1 and 2 fail in milliseconds and already exclude most of the field; 4–6
cost more and should run only on the survivors. The snapping tolerance is part of
the *result*: report it, with the count of vertices moved, because the tolerance
is what turns a gap into adjacency.

---

## ★8 — Accepting an area in a geographic CRS

**Against.** The number is not an area: a degree is not a length and a squared
degree is not an area. The error is bounded by the projection's distortion, which
can be computed exactly for a specified projection and latitude band: for a
study area spanning $\Delta\phi$ at latitude $\phi$, the ratio of a projected to
a geodesic area differs by order $(\Delta\phi)^2 \tan\phi$ to leading order, so a
5° box at 50° N carries several per cent.

**For.** If the layer is small (well under 1°) and its centroid latitude is
declared, the conversion factor $R^2\cos\phi$ is accurate to a few parts in 10⁴,
and the reported area can be rehabilitated by multiplying by it. The quantity to
compute is the ratio of the geodesic area (from the layer's true extent) to the
stated planar area; if it is within the study's tolerance, the claim survives with
a correction, not a rewrite.

**What settles it without recomputation.** The layer's CRS, its bounding
coordinates, the grid or resolution, and the projection identifier if one was
used. With those three the correction is arithmetic; without them the number is
unusable, because the latitude (and therefore the factor) is unknown.
