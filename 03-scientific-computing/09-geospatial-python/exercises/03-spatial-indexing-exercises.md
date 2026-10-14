# Exercises — 03-09-03 Spatial Indexing, Spatial Joins and Performance

Attempt these **closed-book** before opening the
[solutions](./03-spatial-indexing-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems that say "run the demo" refer to
[`../code/spatial_indexing_demo.py`](../code/spatial_indexing_demo.py); report its
**actual** output. **Nothing is timed**: the measurements are predicate evaluations
and candidate pairs, which are machine-independent. All data are **SYNTHETIC**
(2,000 seeded points against a 20 × 20 grid of 2 km cells in UTM zone 12N).

---

## ★ Foundational

**★1.** Write the naive cost of a spatial join of $N$ points against $M$ polygons,
and the indexed cost in terms of the number of candidate pairs $k$.

**★2.** For $N = 2{,}000$ and $M = 400$, compute the naive test count.

**★3.** What does an STRtree store in its internal nodes, and what kind of query
does it answer without evaluating a geometric predicate?

**★4.** Explain in one sentence why a bounding-box-only query is "not wrong, just
unfinished".

---

## ★★ Applied

**★★5.** Run the demo, Sections 2 and 3.
(a) Report the naive test count, the number of matches, and the percentage of tests
that returned nothing.
(b) Report the indexed candidate count, the reduction factor, and whether the
answers are identical.
(c) Report how many candidates the predicate rejected, and state the property of
this dataset that explains it.

**★★6.** Run the demo, Section 4.
(a) Report the band's bounding box dimensions and the ratio of its box area to its
own area.
(b) Report the bbox candidate count, the predicate-confirmed count, and the
percentage rejected.
(c) State what this implies for a dataset of oblique polygons.

**★★7.** Run the demo, Section 7.
(a) Report the point count, the matched count, and the number of locations found by
integer division.
(b) Report the predicate evaluations performed by the grid method.
(c) State the condition under which the grid method is valid.

**★★8.** Run the demo, Section 8.
(a) Report the two quadrat totals and whether the per-cell counts are identical.
(b) Report the mean count, variance and variance/mean ratio, and interpret it for a
uniform sample.

---

## ★★★ Research-oriented

**★★★9.** Clustering degrades an index. Construct a point set concentrated in a
few cells (for example 90 % of points inside 5 % of the cells) and re-run Sections
2 and 3. Report the naive count, the candidate count and the reduction factor for
both the uniform and the clustered sets. Then explain, in terms of the tree's
bounding boxes, why the reduction factor falls.

**★★★10.** Measure the effect of geometry obliqueness on the predicate's cost.
Generate rectangular cells and then rotate the same cells by 0°, 15°, 30° and 45°,
and for each report the bbox candidate count, the confirmed count and the rejected
percentage. Report a table and state the rule that predicts where the bbox filter
stops helping.

**★★★11.** Write a 300–450 word "performance claims" section for a technical report
on a spatial join. It must state the algorithm, the input sizes, the measured
counts, the environment, and the two claims you would *not* make from a single
timing run. Give one example of a claim that the counts support and one that they
do not.
