# Solutions — 03-09-02 GeoDataFrame, CRS Handling and Spatial Joins

> **Read this after attempting the exercises, not before.** Every value attributed
> to "the demo" is its actual output. All data are SYNTHETIC; no number below is an
> observation of the Earth.

---

## ★1 — What the extra object is

A **CRS**, reported by `.crs` (a `pyproj.CRS`), plus a designated geometry column
reported by `.geometry.name`, of dtype `geometry`. Measured:
`crs = EPSG:4326, epsg = 4326`, `geometry column = geometry`.

---

## ★2 — CRS from the quantity

| Task | Class | Example |
|---|---|---|
| (a) catchment areas | equal-area | EPSG:6933 |
| (b) a 10 km distance | local conformal | UTM zone for the survey |
| (c) web tiles | conformal | EPSG:3857 |
| (d) storage/interchange | geographic | EPSG:4326 |

Measured justification at 40°N, 110°W: areal scale **1.7041** for Web Mercator,
**0.9994** for UTM zone 12N and **1.0000** for EASE-Grid 2.0.

---

## ★3 — Axis order

GeoPandas (and PROJ's GIS default) stores **longitude first, latitude second** — the
x column is longitude — even though the EPSG registry defines EPSG:4326 as
latitude-first. `pyproj.Transformer.from_crs(..., always_xy=True)` (the GeoPandas
default) fixes the GIS convention explicitly, and omitting it in hand-written
`pyproj` code is how a dataset ends up transposed.

---

## ★4 — Row counts

- `how="left"` keeps every left-hand row; unmatched rows get **`NaN`** in the
  right-hand columns.
- `how="inner"` silently **drops** them.

Measured in the demo: 600 stations, **123** with no region ⇒ `how="left"` returns
**600 rows** and `how="inner"` returns **477**. The difference, $600 - 123 = 477$,
is exactly the unmatched count, and asserting that identity is the cheapest
correctness check available. (The companion spatial-indexing demo has the same
structure with different numbers: 2,000 points, 155 unmatched, 1,845 inner rows.)

---

## ★5 — Area four ways

**(a)** Measured: as stored **12.000000 square degrees**; UTM zone 12N
**116,137.2142 km²**; UTM zone 11N **117,186.2810 km²**; geodesic
**116,185.9791 km²**. An equal-area CRS (EPSG:6933) gives **116,186.8166 km²**.

**(b)** Zone 12N: **−0.0420 %**; zone 11N: **+0.8609 %** — twenty times worse,
because zone 11's central meridian is 117°W while the data sit at 110°W.

**(c)** The NAD83 (EPSG:26912) area differs from the WGS 84 UTM area by
**0.001 m²** in 116,137 km² — 1 part in 10¹¹. The ellipsoids are effectively
identical (semi-major axes agree to 0.0000 mm), so a datum difference is a *frame
shift* of about a metre, and shifting every coordinate by a metre changes an area
of 116 km² by a negligible amount. **A datum matters for absolute position and for
1 mm-level work; it barely matters for areas.**

---

## ★6 — Distances

**(a)** Measured:

| Method | Value | Error |
|---|---|---|
| degrees | 2.019513 | no units |
| UTM (zone 12) | 205.6477 km | **+0.0077 %** |
| geodesic | 205.6319 km | reference |
| cos(lat) approximation | 205.0066 km | **−0.3041 %** |

**(b)** A 0.05° tolerance is **4.373 km east–west** and **5.529 km north–south** at
this latitude — an ellipse with a 1.26:1 axis ratio, growing without bound toward
the poles.

---

## ★7 — Joins and boundaries

**(a)** **123 of 600** stations (**20.50 %**) have no region.

**(b)** `how="left"` → **600 rows**; `how="inner"` → **477 rows**; and
$600 - 123 = 477$ ✓.

**(c)** Measured for two stations placed exactly on a shared edge:

| Predicate | Matched points | Output rows |
|---|---|---|
| `within` | 0 | 2 |
| `intersects` | 4 | 4 |
| `covers` | 0 | 2 |
| `touches` | 4 | 4 |

`intersects` assigns each boundary point to **both** adjacent cells (duplication);
`within` assigns it to **neither** (loss). A partition must choose, and the choice
must be stated.

---

## ★8 — Aggregation

**(a)** Measured per region (count, mean $v_p$ in km/s, mean elevation in m,
area in km², density per 1,000 km²): R00 86 / 5.9934 / 1498.31 / 19546.90 / 4.3997;
R01 80 / 6.0194 / 1553.73 / 19150.46 / 4.1774; R10 73 / 6.0062 / 1508.14 / 19550.22
/ 3.7340; R11 76 / 6.0053 / 1515.66 / 19153.59 / 3.9679; R20 76 / 5.9783 / 1453.57
/ 19566.84 / 3.8841; R21 86 / 5.9883 / 1467.24 / 19169.20 / 4.4864.
Pooled station mean **5.9982 km/s**; area-weighted **5.9984 km/s**; difference
**0.27 m/s**.

**(b)** Region areas span 19,150.46 to 19,566.84 km² — a **2.17 %** spread. Mean
$v_p$ spans 5.9783 to 6.0194 km/s — a **0.69 %** spread.

**(c)** **The weighting correction is the product of the area spread and the
variable's spread, and both are small here** — so 0.27 m/s is the expected size of
the effect, not evidence that weighting is unnecessary. In real data where the
coastline-adjacent cells are both small and systematically different, both factors
are large.

---

## ★9 — A vast area spread

Method: rebuild the six regions so that one covers 90 % of the stations' bounding
box and the other five tile the remainder. Then repeat Section 5's aggregation.

Reportable results and the structure of the answer:

- The **unweighted** mean of block means is now dominated by the five small blocks:
  each contributes 1/6 of the average regardless of how few stations it holds.
- The **area-weighted** mean is dominated by the large block, whose area is ~90 % of
  the total.
- The gap therefore jumps from the measured **0.27 m/s** to a value of the order of
  the difference between the large block's mean and the small blocks' means, times
  ~0.4 (the weight of the small blocks).

The predicting formula:

$$\bar{x}_{\text{unw}} - \bar{x}_{\text{w}} =
\frac{\sum_i A_i(\bar{x}_i - \bar{x}_{\text{w}})}{\sum_i A_i}
- \frac{1}{n}\sum_i \bar{x}_i
= \left(\frac{A}{\sum A} - \frac{1}{n}\right)\cdot \text{(block-mean spread)}.$$

For two groups — one of area fraction $f$ with mean $x_1$, $n-1$ of fraction
$(1-f)$ with common mean $x_2$ — the gap reduces to

$$\bar{x}_{\text{unw}} - \bar{x}_{\text{w}}
= \left(f - \frac{n-1}{n}\right)(x_2 - x_1)
= \left(f + \frac{1}{n} - 1\right)(x_2 - x_1),$$

which is the number to test numerically. **The check to run:** compute the gap from
the formula and from the data, and report both. If they differ, the block-mean
spread is not two-valued and the formula needs the full sum — which is itself a
useful diagnostic about the data.

---

## ★10 — A one-assignment partition

Three implementations, and the measured outcomes to report:

1. **`within` with an epsilon nudge.** Move every point a tiny distance (say
   $10^{-9}$°) toward the cell centre before testing. Fragile: the nudge direction
   is arbitrary, and points very near a vertex can still land ambiguously.
2. **Nearest centroid.** Compute the distance to every cell centroid and take the
   argmin. **Guarantees exactly one assignment** for every point inside the convex
   hull of the centroids, but the resulting partition is the **Voronoi diagram** of
   the centroids, which equals the grid cells only when the grid is regular and
   bounded. State that caveat explicitly.
3. **Arithmetic cell rule.** `floor((x - x0)/dx)` with a half-open interval
   $[x_0 + i\,dx,\ x_0 + (i+1)\,dx)$ by construction, so a point on the boundary
   belongs to the cell on its right (or above). **Zero unassigned and zero
   duplicated** by construction; the only requirement is the range check
   (`0 <= i < n`) for points outside the grid.

For 1,000 points and 100 cells the expected outcome is:

| Method | Unassigned | Duplicated |
|---|---|---|
| `within` with epsilon | 0–2 (vertex cases) | 0 |
| nearest centroid | 0 | 0, but the partition is Voronoi |
| arithmetic cells | 0 | 0 |

**Ship the arithmetic rule** for a regular grid, and state the convention
(half-open, right/below) in the metadata. The demonstration in the companion
spatial-indexing lesson measures exactly this: **1,845 points located by integer
division with 0 predicate evaluations and identical results to brute force.**

---

## ★11 — Data quality report on an unset CRS

Required content:

**Evidence to gather.** `gdf.total_bounds`. Degrees give bounds in the range
$[-180, 180] \times [-90, 90]$ and a spread of a few units; metres in a UTM zone
give bounds in the range $[10^5, 10^6] \times [10^6, 10^7]$ and a spread of
$10^4$–$10^5$. The two are unmistakable in one print.

**Tests to run.** (i) Numeric ranges of the coordinate arrays; (ii) `total_bounds`
against the expected region; (iii) the distance distribution — pairwise distances
should be of the order the data collection implies (a station spacing of "5" means
5 m or 5°? — a 5° spacing is 550 km, which no survey has); (iv) a comparison against
a known landmark, e.g. transform the first point with `always_xy=True` and check it
against a place you can name; (v) traceability: the file's metadata, the delivery
note, or the instrument's configuration.

**The two failure modes of guessing wrong.** If degrees are labelled metres, then
distance and buffer operations are wrong by a factor of ~111,000 and every buffer
returns a shape smaller than a cell — usually noticed. If metres are labelled
degrees, then a projection or an area computation is attempted on numbers in the
$10^5$ range, which GeoPandas will often *happily* process and return an area in
"square degrees" of order $10^{10}$ — **not** noticed, and the failure is silent.
The second is the dangerous one.

**One line to add.** Refuse the file rather than infer:

```python
assert gdf.crs is not None, "coordinates with no CRS are unusable; supply the EPSG code"
```

with a companion check on plausibility:

```python
assert gdf.total_bounds[0] >= -180 and gdf.total_bounds[2] <= 180, "looks projected, not geographic"
```

The correct process is to obtain the CRS from the provider; the assertions are what
prevent the pipeline from inventing one by default and proceeding.

A complete answer also notes the demonstration's own measured illustration of the
mechanism: computing `.area` in EPSG:4326 returned **12.000000** for a set of
regions whose true total area is **116,185.9791 km²**, a factor of ~9,682 per
"square degree" — and GeoPandas emitted a **UserWarning**, which a pipeline with
warnings suppressed would never see.
