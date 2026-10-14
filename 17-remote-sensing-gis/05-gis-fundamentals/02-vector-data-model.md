---
id: 17-05-02
title: "Vector Data Model and Attribute Operations"
level: intermediate
prereqs: ["17-05-01", "03-04-04", "03-09-02"]
tags: [gis, geospatial, remote-sensing, gis-fundamentals, vector-data, joins, spatial-index, validity]
---

# Vector Data Model and Attribute Operations

A vector layer is a table with a geometry column, which means every operation
you know from tabular data is available — and every one of them can change what
the geometry means, usually without saying so. This lesson works through the
operations that matter in practice: filtering, grouping, **joining** (attribute
and spatial), dissolving, and the indexing that makes an $O(n^2)$ geometric
comparison usable at scale. Two failure modes dominate, and this lesson measures
both: a join that silently multiplies rows, and a geometry that is invalid while
every arithmetic operation on it succeeds.

All models and data in this module are **SYNTHETIC**. The 40 synthetic sites,
the laboratory table, the L-shaped polygons and the bow-tie ring below are
constructed in memory for teaching. No real dataset, place or coordinate is
used, and every number is printed by the demonstration in `code/`.

## Learning objectives

By the end of this lesson you will be able to:

1. **Classify** a geometry by its simple-features type and **state** the storage
   cost of a vertex and the cost of an indexed record header.
2. **Apply** filter, assign, group-by and concat operations to a layer and
   **predict** what happens to the geometry column in each.
3. **Detect** and **quantify** row multiplication in an attribute join, and
   **explain** how it biases a summary statistic with unequal group sizes.
4. **Choose** a spatial predicate deliberately and **derive** the resulting row
   count from the number of boundary coincidences.
5. **Explain** why an R-tree index changes cost and not the answer, and
   **quantify** the candidate reduction as a function of feature count.
6. **Test** a geometry for validity, **repair** it, and **state** by how much the
   repaired area differs from the invalid arithmetic.
7. **Justify** filtering by geometry type before any length or area measurement.

## Prerequisites

- [01 GIS Concepts: Layers, Attributes and Topology](01-gis-concepts.md) —
  layers, attributes, predicates and the planar partition.
- [03-04-04 Group-by and Aggregation](../../03-scientific-computing/04-pandas/04-groupby-aggregation.md) —
  the tabular half of every vector operation.
- [03-09-02 GeoPandas Basics](../../03-scientific-computing/09-geospatial-python/02-geopandas-basics.md) —
  reading and writing a geo-table.

## 1. Geometry types and what a vertex costs

The simple-features model has six geometry types, and every one is a coordinate
sequence with a type tag. The demonstration prints them with their dimension,
coordinate count, length and area:

| type | dimension | coordinates | length (m) | area (m²) |
|---|---|---|---|---|
| Point | 0 | 1 | 0.00 | 0.00 |
| MultiPoint | 0 | 3 | 0.00 | 0.00 |
| LineString | 1 | 3 | 10.00 | 0.00 |
| MultiLineString | 1 | 4 | 2.83 | 0.00 |
| Polygon | 2 | 5 | 14.00 | 12.00 |
| MultiPolygon | 2 | 10 | 8.00 | 2.00 |

Three observations:

* **Length, area and centroid are computed, not stored.** They are functions of
  the coordinates. Recomputing them inside a loop over features is the standard
  performance mistake, and the fix is to compute them once in a vectorised pass.
* **Vertices are the cost.** Two float64 ordinates per vertex is 16 bytes, and
  an indexed format such as a shapefile adds a fixed 100-byte header per
  geometry. Both are negligible for thousands of features and decisive for
  hundreds of millions: the reason analysis moves to raster and to spatial
  databases at scale is that a polygon boundary is a *hand-drawn curve*, while a
  raster cell is a *sample*.
* **A polygon's coordinate count includes the closing vertex.** The 4-vertex
  square stores 5 coordinates. That repetition is not cosmetic: any code that
  iterates "over the vertices" without treating the ring as closed will drop the
  last edge.

## 2. Attribute operations, and what happens to the geometry

Six operations cover almost all attribute work, and the geometry behaves
differently in each:

| operation | effect on rows | effect on geometry |
|---|---|---|
| filter (`df[cond]`) | selects rows | rows keep their geometry, and it still matches the attributes |
| assign | same rows, new column | none |
| group-by + aggregate | one row per group | **geometry is gone** unless the aggregation redefines it |
| dissolve | one row per group | geometries are unioned — a new geometry |
| join (attribute) | row count may multiply | the left geometry is repeated |
| concat | row count adds | none, but CRS must match |

The demonstration filters to `rock == 'granite'` and finds 18 of 40 rows with a
mean conductivity of 1.302 mS/m, then groups by rock:

```
          n  mean_cond  max_cond
rock
cover     4      0.756     1.242
granite  18      1.302     5.052
schist   18      1.131     5.286
```

The result has three rows and no geometry. Anything computed from it is an
attribute statistic about *classes*, not a spatial statistic about *places*, and
the two are different objects. Mixing them — printing the group-by table next to
a map of the same layer, as if the table summarised the map — is the commonest
reporting error in attribute GIS.

## 3. Attribute joins multiply rows

An attribute join is a relational join on a key. If the key is not unique on the
right-hand table, each left row is **duplicated** once per matching right row.
This is correct relational algebra and a trap for every downstream statistic.

The demonstration joins 40 sites to a synthetic laboratory table in which ten
sites carry three analyses, twenty-five carry two, and five carry none:

| quantity | value |
|---|---|
| left table rows | 40 |
| right table rows | 80 |
| joined rows (`how='left'`) | 85 |
| sites with no laboratory result | 5 |
| mean of `value` over matched **rows** | 10.0438 |
| mean of per-**site** means | 10.0523 |
| difference produced purely by the join | −0.0086 (−0.085 %) |

The data did not change between the two means; only the *unit of analysis*
did. Ten sites contribute three rows instead of two, so a mean over rows
over-weights them by 50 %. A bias of 0.085 % is small here only because the
laboratory values are synthetic and identically distributed; when the
over-weighted sites are systematically different — a re-visited anomaly, a
densely sampled ore zone — the same mechanism produces a bias of tens of
per cent.

The check is mechanical and costs nothing:

$$
n_{\text{joined}} = \sum_{i=1}^{n_{\text{left}}} \left|\{j : \text{key}_j =
\text{key}_i\}\right| ,
$$

so the expected row count is known before the join is run, and any difference is
a defect in the key, not a surprise to be discovered later. Stating the **unit of
analysis** (row, site, cluster) is the other half of the check.

## 4. Spatial joins: the predicate selects the answer

A spatial join replaces the key comparison with a geometric predicate. The
demonstration joins 45 sites to two blocks with five sites exactly on the shared
cut:

| predicate | result rows | matched to a block |
|---|---|---|
| `within` | 45 | 40 |
| `intersects` | 50 | 50 |
| `contains` | 45 | 0 |

Three readings:

* With `within`, the five boundary sites match nothing, so the join is
  many-to-one and the row count equals the site count. Each of the 40 interior
  sites produces one row; the five boundary sites produce one row each with no
  match.
* With `intersects`, the five boundary sites lie in *both* blocks, so they
  produce ten rows. The count $45 + 5 = 50$ is exactly the prediction from
  §4 of [01 GIS Concepts](01-gis-concepts.md): $n + m$ rows for $m$ boundary
  coincidences.
* `contains` asks whether the **left** geometry contains the right one, so no
  point can ever contain a block. The predicate is not symmetric and swapping
  the arguments changes the join.

The general rule: a spatial join's row count is a *property of the predicate*,
and the analyst's job is to name the predicate and check the count against the
prediction. A one-to-many join that was meant to be one-to-one is invisible in
the result — every row looks valid — and it corrupts every downstream mean.

## 5. Spatial indexing: the idea that makes vector GIS scale

Testing all $\binom{n}{2}$ pairs is $O(n^2)$. With 500 000 features that is
$1.25 \times 10^{11}$ pairs, which is not a slow computation but an impossible
one. An R-tree stores the *bounding boxes* of features in a balanced tree so
that a query returns only the features whose boxes could intersect the query
box. The exact predicate is then applied to that candidate set.

The demonstration measures the whole chain on 30 synthetic L-shaped polygons
(a deliberate choice: an L is **not** its own bounding box, so false positives
are possible):

| quantity | value |
|---|---|
| all unordered pairs (brute force) | 435 |
| pairs admitted by a bounding-box test | 54 |
| pairs actually intersecting | 51 |
| pairs returned by the index query | 51 |
| index agrees with the exact test | True |
| bounding-box false positives (box yes, intersection no) | 3 |
| candidate reduction | 8.5× |

At constant density the reduction grows with $n$, because brute force grows as
$n^2/2$ while the number of near-neighbours grows about linearly:

| n features | all pairs | bbox candidates | reduction |
|---|---|---|---|
| 30 | 435 | 33 | 13.2× |
| 120 | 7 140 | 115 | 62.1× |
| 480 | 114 960 | 513 | 224.1× |

Two honest caveats:

1. **The index does not change the answer.** It is exact here — an R-tree never
   returns a false *negative* for a bounding-box query, which is precisely why it
   is safe as a filter. The false positives it does admit are pruned by the exact
   second stage. That combination, *exact filter then exact test*, is the standard
   architecture of every spatial database.
2. **The candidate count depends on density and on shape.** For long thin
   features — roads, rivers, faults — bounding boxes can be almost the whole
   study area, and the gain collapses. Index performance is a property of the
   geometry as well as of the count, so it must be measured on the actual data.

## 6. Validity: a property no arithmetic can detect

An OGC-valid polygon has a simple, closed, non-self-intersecting boundary. A
bow-tie ring has four vertices, no repeats, and every arithmetic operation on it
succeeds:

| quantity | value |
|---|---|
| shapely reports valid | False |
| reported `.area` | 0.000000 km² |
| area after `make_valid()` | 2.000000 km² |
| type after `make_valid()` | MultiPolygon |
| part areas | 1.0 km², 1.0 km² |

The two lobes have *opposite orientation*, so the shoelace sum cancels exactly.
The reported 0 is not a crash, not a warning and not an obvious absurdity — it
is a plausible-looking number for a shape that encloses 2 km². Validity and
geometry are separate questions in the simple-features model, and validity has
to be asserted explicitly:

```python
from shapely import is_valid, make_valid
assert is_valid(geom) or make_valid(geom).equals(geom)
```

The repaired geometry is a `MultiPolygon` of two parts, so a repair changes the
*type* of the feature as well as its coordinates. Downstream code that assumed
Polygon will now fail, which is a good outcome: the failure is visible.

## 7. Mixed geometry types and missing values

Two silent traps, both measured in the demonstration:

* **Mixed types.** A layer containing points, lines and polygons computes
  `.area` for all of them: `[0.0, 1.0, 0.0]`. A point's area is 0 and a line's
  area is 0, so a sum over the layer is numerically defined and semantically
  meaningless. Filter by geometry type before measuring.
* **Missing values.** Setting five of forty `rock` values to `None` gives
  `{granite: 17, schist: 15, nan: 5, cover: 3}`, and the group-by silently
  returns three groups covering 35 of 40 rows. The count of dropped rows is not
  in the result; it has to be asserted.

These are the mirror image of the join problem: the join *adds* rows without
saying so, the group-by *removes* them without saying so, and both change the
number that gets reported.

## 8. Worked example: two joins and a statistic

A survey has 250 sites. A laboratory table has 600 analyses, and a geology
polygon layer has 40 units; some sites lie exactly on unit boundaries.

1. **Expected attribute-join rows.** If every site has 2 analyses and 30 sites
   have a third, $n_{\text{joined}} = 250 \times 2 + 30 = 530$. If the actual
   join returns 600 rows, the right-hand table has more analyses per site than
   assumed: check the key before analysing.
2. **Row-mean versus site-mean.** Suppose the 30 three-analysis sites have a
   mean value of 15 and all others 10. The row-mean is
   $(30 \times 3 \times 15 + 220 \times 2 \times 10)/(90 + 440) = (1350 +
   4400)/530 = 10.849$; the site-mean is $(30 \times 15 + 220 \times
   10)/250 = 10.600$. The join inflates the reported mean by 2.35 % with no
   change to any measurement.
3. **Expected spatial-join rows.** Of 250 sites, 12 lie exactly on a unit
   boundary. With `within` the row count is 250 (12 unmatched); with
   `intersects` it is $250 + 12 = 262$. A result of 262 rows under `within`
   means the predicate was not the one you thought.

## Assumptions and regime of validity

1. **All layers are in one CRS, in metres.** A join across two CRSs either fails
   or, worse, produces plausible nonsense if the numbers happen to overlap
   numerically.
2. **Predicates are evaluated on the coordinates supplied.** A boundary that is
   geographically shared but digitised twice is *not* shared by the predicate.
   Snapping is a decision (§2 of [01](01-gis-concepts.md)).
3. **Geometry validity is asserted, not assumed.** Every area, length, overlay
   and buffer is undefined on an invalid geometry.
4. **The index is a filter, not an approximation.** Results are exact; only the
   cost changes. An implementation that returns an approximate candidate set
   (some spatial joins in distributed engines do) breaks this and must be
   labelled as approximate.
5. **Rows are independent.** A duplicated row is not a duplicate *feature*: if
   the same site appears twice with the same geometry, nothing in the data model
   prevents it, and the geometry column will not complain.

## Python demonstration

[`code/vector_data_model_demo.py`](code/vector_data_model_demo.py) builds every
object above in memory and prints labelled results. It:

1. prints the six simple-feature types with dimension, coordinate count, length
   and area;
2. applies filter, assign and group-by to a 40-row synthetic layer and shows the
   geometry disappearing;
3. measures row multiplication in an attribute join and the resulting row-mean
   versus site-mean bias;
4. runs the same spatial join under three predicates and reports row counts;
5. builds an R-tree over 30 synthetic L-shaped polygons and reports candidate
   counts, false positives and the reduction factor, repeated at three sizes at
   constant density;
6. shows the bow-tie ring, its reported area of 0, and the 2 km² repaired area;
7. demonstrates mixed geometry types and the silent row loss of a group-by with
   missing values.

```bash
cd 17-remote-sensing-gis/05-gis-fundamentals/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python vector_data_model_demo.py
```

Print-only, no files, no network, exits 0.

## Exercises

[`exercises/02-vector-data-model-exercises.md`](exercises/02-vector-data-model-exercises.md)
and the
[solutions](exercises/02-vector-data-model-solutions.md):

- **★** Predict the row count of an attribute join from key multiplicities.
- **★★** Compute the row-mean/site-mean bias for a stated group-size pattern.
- **★★★** Design an index-and-predicate strategy for a layer of long thin
  features and estimate the candidate count analytically.

## Mastery checkpoint

Without notes:

> A study has 400 sites joined to a table with 900 measurements, and to a
> 30-polygon geology layer; 25 sites lie exactly on unit boundaries. **(a)** Write
> the formula for the expected attribute-join row count and the row count you
> predict for 900 measurements. **(b)** If the join returns 900 rows with a mean
> of 12.0 and per-site means give 11.4, which statistic would you report and why?
> **(c)** State the predicted row count of the spatial join under `within` and
> under `intersects`. **(d)** A colleague reports that the layer's total area is
> 1250 km² for a layer containing 100 polygons, 300 lines and 500 points. What is
> wrong, and what would you compute instead?

A worked version of (a)–(c) is in the
[solutions](exercises/02-vector-data-model-solutions.md).

## Common pitfalls

1. **Interpreting a row-mean as a site-mean.** The join changed the unit of
   analysis and said nothing.
2. **Assuming a spatial join is one-to-one.** It is one-to-many wherever a site
   lies on a boundary.
3. **Measuring area on a mixed-type layer.** Points and lines contribute zero,
   which looks like data rather than an error.
4. **Skipping `is_valid`.** No downstream operation will raise.
5. **Confusing "the boxes intersect" with "the features intersect".** The index
   is allowed false positives by construction and someone must prune them.
6. **Assuming the index helps long thin geometries.** Measure it.
7. **Trusting a group-by to report dropped rows.** It does not.

## Related modules

- [01 GIS Concepts: Layers, Attributes and Topology](01-gis-concepts.md).
- [03 Raster Data Model, Resolution and Resampling](03-raster-data-model.md) —
  the same operations with cells instead of features.
- [06-gis-fundamentals README](README.md).
- [03-09 Geospatial Python](../../03-scientific-computing/09-geospatial-python/README.md) —
  `sjoin`, `overlay` and the spatial index at library level.
- [22-04 Spatial Databases](../../22-data-engineering-reproducibility/04-databases-and-large-data/02-spatial-databases.md) —
  where these ideas live when the layer does not fit in memory.

## Self-assessment checklist

- [ ] I can name the six geometry types and say which have non-zero area.
- [ ] I can predict the row count of an attribute and a spatial join.
- [ ] I can explain, with a number, how a join biases a mean.
- [ ] I can explain what an R-tree guarantees and what it does not.
- [ ] I can detect and repair an invalid polygon and state the area change.
- [ ] I can state three checks I run before reporting any vector statistic.

