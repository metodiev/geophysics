---
id: 03-09-03
title: "Spatial Indexing, Spatial Joins and Performance"
level: advanced
prereqs: ["03-09-02", "03-09-01", "03-02-07"]
tags: [spatial-index, strtree, spatial-join, complexity, performance, quadtree]
---

# Spatial Indexing, Spatial Joins and Performance

A spatial join of 2,000 points against 400 polygons is 800,000 containment tests
if you write it naively. The same answer is obtained with 1,845 tests. The factor
is 434, and it grows with the dataset — this lesson is about why, and about
measuring the saving instead of guessing at it.

> **Every number below is measured output from
> `code/spatial_indexing_demo.py`.** Nothing is timed: the demo counts
> *predicate evaluations* and *candidate pairs*, which are machine-independent and
> reproducible. All data are SYNTHETIC — 2,000 seeded points against a 20 × 20
> grid of 2 km cells in UTM zone 12N.

## Learning objectives

By the end of this lesson you will be able to:

1. **State** the complexity of a naive spatial join, and compute its test count
   from the two input sizes.
2. **Explain** what an R-tree/STRtree stores, and why a bounding-box query is a
   candidate generator rather than an answer.
3. **Measure** the reduction factor of an index against brute force, and verify
   that the answers are identical.
4. **Distinguish** bounding-box candidates from predicate-confirmed matches, and
   predict when the difference is large.
5. **Recognise** when a regular grid removes the search entirely, and implement
   the $O(1)$ cell lookup.
6. **Produce** quadrat counts two ways and check them against each other.
7. **Choose** between an index query, a grid hash and a raster for a given
   problem, with the cost model made explicit.
8. **Report** a performance claim without a stopwatch, using counts.

## Prerequisites

- [03-09-02 GeoDataFrame, CRS Handling and Spatial Joins](./02-geopandas-basics.md)
  — `sjoin`, predicates and the CRS decisions that precede any of this.
- [03-09-01 Shapely Geometries and Planar Operations](./01-shapely-geometries.md)
  — predicates, and the boundary behaviour that duplicates or loses points.
- [03-02-07 Memory Layout, Strides and Cache-Aware NumPy](../02-numpy/07-memory-performance.md)
  — why counting operations is a better performance model than counting seconds.

## 1. Intuition: from a product to a sum

Suppose you have $N$ points and $M$ polygons. The question "which polygon contains
each point?" has two cost structures:

$$T_{\text{naive}} = N \times M, \qquad
T_{\text{indexed}} \approx c\,N \quad \text{with } c \approx 1.$$

Measured for the demonstration's $N = 2{,}000$, $M = 400$:

```
a naive nested loop performs 2,000 x 400 = 800,000 point-in-polygon tests
brute force: 800,000 tests -> 1,845 matches
hit rate = 0.2306 % of all tests; 798,155 tests returned nothing
```

**798,155 of 800,000 tests produced nothing.** That is the inefficiency in one
number: 99.77 % of the work was spent proving that a point is not in a polygon.
An index attacks exactly that — it uses the geometry's *position* to avoid
testing pairs that cannot possibly interact.

The measured indexed result:

```
STRtree built over 400 polygons; 2000 query geometries
bounding-box candidates returned = 1,845
candidate pairs per point = 0.922
reduction against brute force = 433.6x fewer predicate evaluations
answer identical to brute force: True
```

434× fewer evaluations, and the answers are *identical*, not similar. This is the
most important property of a good index: **it changes the cost, not the result.**

## 2. What an STRtree is, precisely enough to reason about

An **R-tree** is a balanced tree whose nodes store bounding boxes. Leaves hold the
original geometries' bounding boxes; internal nodes hold the bounding box that
encloses their children. A query descends only into subtrees whose boxes intersect
the query's box. An **STRtree** (Sort-Tile-Recursive) is a particular packing that
produces a well-balanced tree from a static geometry set — which is why shapely's
`STRtree` is built once and queried many times.

Three consequences, all of which show up in the measurements:

1. **The filter is a bounding box, not the geometry.** A candidate pair is one
   whose *boxes* overlap. For the demonstration's axis-aligned rectangular cells,
   box and geometry coincide, so the filter is exact: **0 candidate pairs were
   rejected by the predicate** (measured).
2. **The predicate is still evaluated on candidates.** `tree.query(geoms,
   predicate="within")` runs the filter and then the exact test, so the cost is
   (candidates + predicate evaluations), not (candidates) alone.
3. **Building is $O(M \log M)$-ish and querying is $O(\log M + k)$ per query**
   with $k$ candidates. The index earns its build cost as soon as you have many
   points per polygon.

The measured box-versus-geometry distinction, when the two differ:

```
the band is 40 km x 1 km, rotated 20 deg:
  its bounding box is 37,930 m x 14,620 m, 13.9x its area
  bbox candidates          = 648 points
  predicate confirms       = 46 points
  candidates the predicate rejects = 602 (92.9 %)
```

A rotated sliver has a bounding box 13.9× its area, so 92.9 % of its candidates
are false. **The more oblique your geometries, the more the predicate matters**,
and the more a bounding-box-only query (a common shortcut) overstates the answer.

## 3. The predicate is not optional

```
tree.query without a predicate -> 1,845 bbox candidates (1.00x the matches)
```

In this dataset the box-only query is *exactly* the answer, because the cells are
axis-aligned and non-overlapping. That is a property of the demonstration's
geometry, not of spatial indexing. Two lessons:

- **Always report which of the two you computed.** "1,845 candidate pairs" and
  "1,845 matches" happen to coincide here and mean different things.
- **Run the experiment on your own data.** If your polygons are oblique, the
  box-only count can be an order of magnitude high (measured: 648 vs 46).

## 4. When a grid removes the search

The demonstration's cells are a regular 20 × 20 grid. If the *data* are on that
grid, no tree is needed:

```
floor((x - x0) / dx) locates each point in a cell by arithmetic:
  points located        = 1,845
  predicate evaluations = 0 (integer division plus a range check)
  matches identical to brute force: True
```

Two integer divisions give the cell index, and a 1-D flattening of the 2-D index
gives a flat id for `np.bincount`. Cost: $O(N)$ with a tiny constant, no tree, no
predicate. This is the fastest spatial join available and it is the reason large
gridded datasets are stored as **rasters** rather than as millions of polygons:

```
Counting points per cell: two routes, one answer
  sjoin + groupby total = 1,845 points
  numpy bincount total  = 1,845 points
  identical per-cell counts: True
  busiest cell holds 12 points; 3 cells are empty
  measured mean = 4.612, variance = 4.253, variance/mean = 0.922
```

The two routes agree exactly — one uses a spatial index and a groupby, the other
two multiplications and a histogram. Choose by what you already have: if the
polygons exist only as a grid, generate the ids arithmetically; if they are
irregular, you need the tree.

### 4.1 The quadrat test, as a bonus

The counts also support a standard clustering diagnostic. For a uniform random
process with mean $\lambda$ per cell, the counts are Poisson, so the
variance-to-mean ratio is 1. Measured here: mean 4.612, variance 4.253, ratio
**0.922** — slightly *under*-dispersed, which is what uniform (not Poisson)
sampling gives: a uniform draw is more even than Poisson. The interpretation is
that a ratio near 1 is consistent with a random distribution, a ratio well above 1
indicates clustering, and a ratio well below 1 indicates repulsion or systematic
spacing (a survey with fixed station intervals, for instance).

## 5. Nearest neighbours are a different query

```
STRtree.query_nearest on 5 points INSIDE the tiling -> 5 pairs, distances = [0.] m
5 points WEST of the tiling: nearest-polygon distance = [2500. 2000. 1500. 1000. 500.] m
k=3 nearest polygons per query point, found by predicate='dwithin', distance=9000 m:
  query 0 at (497,500, 4,200,000): 15 candidates, 3 nearest at 2500 m, 3202 m, 4500 m
  query 1 at (498,000, 4,208,000): 32 candidates, 3 nearest at 2000 m, 2000 m, 2828 m
  query 2 at (498,500, 4,216,000): 34 candidates, 3 nearest at 1500 m, 1500 m, 2500 m
  query 3 at (499,000, 4,224,000): 36 candidates, 3 nearest at 1000 m, 1000 m, 2236 m
  query 4 at (499,500, 4,232,000): 38 candidates, 3 nearest at 500 m, 500 m, 2062 m
```

Four observations:

- **A containment query and a nearest query are not the same.** For points inside
  a cell, the nearest polygon distance is 0; the informative questions are about
  points *outside* the layer, where the answers are 500–2,500 m.
- **`query_nearest` requires its own index pass** — the tree knows how to prune by
  distance, which the containment query does not exploit.
- **A $k$-nearest search is a radius search plus a sort.** Measured candidate
  counts of 15–38 for a 9 km radius, reduced to the 3 nearest by an exact sort of
  the candidate distances. The radius must be chosen large enough to contain $k$
  neighbours, and no larger.
- **`query(g, distance=r)` does not expand the search.** The radius predicate is
  `predicate="dwithin", distance=r`. Getting this wrong returns zero candidates
  with no error — a failure mode that looks like "no data nearby".

Note the k-nearest distances: query 1 and query 2 have their first two neighbours
at equal distance (2000 m and 2000 m; 1500 m and 1500 m) because two cells are
simultaneously nearest at those positions. A $k$-nearest implementation must
decide whether ties are broken by index, by distance and then index, or kept. The
API returns both; the analysis decides.

## 6. The same join through three interfaces

The demonstration runs the identical question three ways:

| Route | Work | Result |
|---|---|---|
| brute-force nested loop | 800,000 predicate evaluations | 1,845 matches |
| `tree.query(..., predicate="within")` | 1,845 candidates + 1,845 predicates | 1,845 matches, identical |
| `gpd.sjoin(..., predicate="within", how="inner")` | the same tree, wrapped | 1,845 rows, equal to brute force |
| integer grid lookup | 1,845 divisions, 0 predicates | 1,845 matches, identical |

```
gpd.sjoin(predicate='within', how='inner') -> 1,845 rows
equal to the brute-force match count: True
how='left' -> 2,000 rows, 155 of them with no cell
cells that received at least one point = 397 of 400
```

`gpd.sjoin` is the index-using path, which is why it is fast on data where a
hand-written loop is not. The `how='left'` row count (2,000) minus the unmatched
count (155) is 1,845: the same number by a different route, which is the cheapest
correctness check available.

## 7. A cost model you can use

Before writing a spatial join, estimate:

$$T \approx \underbrace{N M}_{\text{naive}} \quad\text{versus}\quad
\underbrace{N \log M + k}_{\text{indexed}} \quad\text{versus}\quad
\underbrace{N}_{\text{grid}},\qquad k = \text{total candidate pairs}.$$

Measured values to calibrate with:

| Quantity | Measured |
|---|---|
| naive predicate evaluations | 800,000 |
| indexed candidate pairs | 1,845 |
| indexed predicate evaluations | 1,845 |
| candidates per query point | 0.922 |
| grid lookup predicate evaluations | 0 |
| obliqueness penalty (rotated band) | 92.9 % of candidates false |
| unmatched features in the left join | 155 of 2,000 (7.75 %) |

Two further effects to expect on real data:

- **Clustering increases $k$.** Uniformly distributed points give $k/N \approx 1$;
  a dataset concentrated along rivers or coastlines gives far more candidates per
  query, and the index's advantage shrinks.
- **Duplicate and invalid geometries increase $k$** without increasing the answer,
  so `is_valid()` and a deduplication pass before indexing are part of the
  performance story, not just a data-quality one.

## 8. Reporting performance without a stopwatch

Wall-clock timings are not reproducible: they depend on the machine, the thermal
state, the Python build and the scheduler. The measurements here are counts, and
they support every claim a timing would:

- "The index reduces predicate evaluations from 800,000 to 1,845" is a statement
  about asymptotics and constants.
- "Candidate pairs per query point is 0.922, so the tree is doing its job" is
  machine-independent.
- "92.9 % of bbox candidates are rejected by the predicate" tells you where the
  remaining cost is.

If a timing is unavoidable, report the *counts* alongside it and the environment
(interpreter version, single-threaded or not), and never quote a ratio from one
run on one machine as though it were a property of the algorithm.

## 9. Units and dimensional analysis

- **Every distance in a spatial index is in CRS units.** The 2 km cells here are
  metres because the CRS is EPSG:32612. In EPSG:4326 the same cells would be
  0.018° and the *shape* of the search radius would be latitude-dependent.
- **A search radius must be in the same units as the index.** `dwithin` with a
  metre radius against a degree-based tree returns nothing or everything,
  depending on the numbers, and never an error.
- **Cell counts are dimensionless; cell areas are not.** The quadrat statistic
  (variance/mean) is dimensionless and comparable across grid resolutions; the
  mean count is not.
- **A bounding box is a set of four coordinates; its area is in CRS units².** The
  "13.9× its area" figure in Section 2 is a ratio of two areas in the same units,
  which is why it is meaningful.

## 10. Python demonstration

The full script is
[`code/spatial_indexing_demo.py`](./code/spatial_indexing_demo.py):

```bash
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python \
    03-scientific-computing/09-geospatial-python/code/spatial_indexing_demo.py
```

It runs offline, is seeded, and writes nothing.

### What to observe, and why it matters

| Observation | Consequence |
|---|---|
| 800,000 tests, 1,845 matches, 99.77 % of tests empty | the naive join spends almost all its work on "no" |
| index: 1,845 candidates, 434× fewer evaluations, identical answers | indexing changes cost, not results |
| 0 candidates rejected for axis-aligned cells | box and geometry coincide; the filter is exact |
| 602 of 648 candidates rejected for a rotated band | obliqueness is what makes the predicate necessary |
| integer grid lookup: 0 predicates, identical answers | regular grids need no index |
| `sjoin` equals brute force row for row | the library path is the same algorithm |
| `dwithin` is needed for a radius query | `query(distance=r)` silently returns nothing |
| variance/mean = 0.922 | a quadrat diagnostic falls out of the counts for free |

> **Breaking exercise.** Before running, predict the indexed evaluation count if
  the 400 cells are replaced by 100 larger cells covering the same area. Then run
  it and compare with the number of matched points per cell.

## 11. Common mistakes

1. **Writing the nested loop.** It is correct and 434× more evaluations here; on
   10⁶ points it does not finish.
2. **Forgetting the predicate.** A bounding-box-only answer overstates matches by
   0 % on axis-aligned data and by 1,300 % on the rotated band (648 vs 46).
3. **Using `query(g, distance=r)` for a radius search.** The radius predicate is
   `dwithin`; the wrong form returns zero candidates with no error.
4. **Assuming an index removes the need for valid geometry.** Invalid polygons
   inflate candidate counts and produce the area anomalies of lesson 01.
5. **Indexing the wrong side.** Build the tree over the layer you query *many*
   times (usually the polygons) and pass the many geometries as queries.
6. **Quoting a timing instead of a count.** Timings are not reproducible; counts
   are.
7. **Forgetting that an index must be *rebuilt* after geometry changes.** A stale
   `sindex` is a silent correctness bug, not a performance one.
8. **Ignoring the unmatched count.** Measured 155 of 2,000 (7.75 %) here; it is
   the first data-quality number a join produces.

## 12. Real-world applications

- **National-scale point inventories.** Millions of wells, stations or addresses
  against thousands of administrative polygons: the index is the difference
  between seconds and days.
- **Overlay and intersection of map layers.** All overlay operations begin with a
  candidate pair generation step; the STRtree pattern generalises to any of them.
- **Nearest-facility and service-area analysis.** `query_nearest` and `dwithin`
  are the primitives behind "which hospital is closest" and "which stations are
  within 50 km".
- **Ground-motion and exposure joins.** Assigning assets to hazard polygons at
  scale is a spatial join whose row count is a risk-model input.
- **Gravity and magnetic survey cell assignment.** Grid-based physical
  partitioning is the raster case; generating the cell ids arithmetically is what
  makes it fast enough for continent-scale compilations.

## 13. Further reading

- **Shapely, *Documentation*: STRtree.** Level: intermediate.
  <https://shapely.readthedocs.io> — the tree, its query methods, `dwithin`, and
  the index semantics of the returned arrays.
- **GeoPandas, *Documentation*: spatial joins and the spatial index.** Level:
  intermediate. <https://geopandas.org> — `sjoin`, `sindex`, and the
  `predicate`/`how` matrix.
- **Open Geospatial Consortium, *Simple Feature Access* specification.** Level:
  reference. The predicate definitions that decide the candidate counts.
- **Samet, H. (1990). *The Design and Analysis of Spatial Data Structures*.
  Addison-Wesley.** Level: advanced. The definitive treatment of quadtrees,
  R-trees and their analysis; the source of the cost model in Section 7.
- **Leutenegger, S. T., Lopez, M. A. and Edgington, J. (1997). STR: a simple and
  efficient algorithm for R-tree packing. *Proceedings of ICDE*.** Level:
  advanced. The packing algorithm shapely's `STRtree` is named after.

> Note on citations: bibliographic details are given so you can locate these
> works. This repository does not host or reproduce copyrighted text.

## 14. Related lessons

- [02 GeoDataFrame, CRS Handling and Spatial Joins](./02-geopandas-basics.md) —
  the CRS arithmetic that must precede any join.
- [01 Shapely Geometries and Planar Operations](./01-shapely-geometries.md) —
  predicates, validity and vectorised operations.
- [04 Raster-Vector Integration and Zonal Statistics](./04-vector-raster-ops.md)
  — the same grouping problem with the polygons rasterised instead of indexed.
- [03-02-07 Memory Layout, Strides and Cache-Aware NumPy](../02-numpy/07-memory-performance.md)
  — the machine model behind "count operations, not seconds".
- [03-08-04 Chunking with Dask for Out-of-Core Analysis](../08-gridded-geospatial-data/04-dask-chunking.md)
  — the same cost-counting discipline for out-of-core work.

## Exercises

[`exercises/03-spatial-indexing-exercises.md`](./exercises/03-spatial-indexing-exercises.md),
with full worked answers in
[`exercises/03-spatial-indexing-solutions.md`](./exercises/03-spatial-indexing-solutions.md).

## Self-assessment checklist

- [ ] I can compute the naive test count for a join from the input sizes.
- [ ] I can explain what an STRtree stores and why a bbox query is only a
      candidate generator.
- [ ] I can quote the measured reduction factor and confirm the answers match.
- [ ] I can predict when bounding boxes and geometries diverge, and by how much.
- [ ] I can implement an $O(1)$ grid cell lookup and explain when it is valid.
- [ ] I can produce quadrat counts two ways and check them against each other.
- [ ] I can choose between index, grid hash and raster for a stated problem.
- [ ] I can report a performance claim using counts rather than timings.
