# Exercises — 03-09-02 GeoDataFrame, CRS Handling and Spatial Joins

Attempt these **closed-book** before opening the
[solutions](./02-geopandas-basics-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems that say "run the demo" refer to
[`../code/geopandas_basics_demo.py`](../code/geopandas_basics_demo.py); report its
**actual** output. All data are **SYNTHETIC**: 600 seeded stations and six
rectangular regions in the western USA. Nothing is downloaded.

---

## ★ Foundational

**★1.** What does a `GeoDataFrame` have that a `DataFrame` does not, and what
property reports it?

**★2.** State which CRS class (geographic/equal-area/conformal/compromise) you
would choose for: (a) areas of catchments; (b) a 10 km distance in one survey;
(c) web map tiles; (d) storage and interchange.

**★3.** `EPSG:4326` is defined by EPSG as latitude-first. What order does GeoPandas
store it in, and which `pyproj` flag makes the convention explicit?

**★4.** State the row-count consequences of `how="inner"` versus `how="left"` in a
spatial join, and what value appears in the unmatched rows.

---

## ★★ Applied

**★★5.** Run the demo, Section 2.
(a) Report the sum of region areas as stored, in UTM zone 12, in UTM zone 11, and
geodesically.
(b) Report the errors of zones 12 and 11 against the geodesic value.
(c) Report the NAD83-versus-WGS84 difference and explain why it is so small here.

**★★6.** Run the demo, Section 3.
(a) Report the four distance values for the same pair of stations and each error
against the geodesic.
(b) Report what a `distance < 0.05` degree tolerance means in kilometres
east–west and north–south.

**★★7.** Run the demo, Section 4.
(a) Report the number of stations with no region and the percentage.
(b) Report the row counts for `how="left"` and `how="inner"`, and verify the
subtraction.
(c) Report the results for a point placed exactly on a shared cell edge under
`within`, `intersects`, `covers` and `touches`.

**★★8.** Run the demo, Section 5.
(a) Report the per-region table and the pooled mean with and without area
weighting.
(b) Report the spread in region areas and in mean $v_p$.
(c) State the sentence that reconciles the small weighting difference with the
general rule.

---

## ★★★ Research-oriented

**★★★9.** Re-run the demonstration with the six regions replaced by six regions of
*vastly* different areas (for example one covering 90 % of the stations' bounding
box). Report the new area-weighted and unweighted means, the difference, and the
change in the naive-versus-weighted gap. Then state the formula that predicts the
gap from the area spread and the variable spread, and test it numerically.

**★★★10.** Design a point-in-polygon partition that guarantees exactly one
assignment per point using half-open boundaries. Implement it three ways — by using
`within` with a nudge, by using a nearest-centroid assignment, and by rasterising
with an explicit cell rule — and report, for 1,000 points on a grid of 100 cells,
the number of unassigned points and the number of duplicated points under each.
State which you would ship and why.

**★★★11.** Write a 300–450 word data-quality report for a delivered point dataset
that arrived with `crs` unset. It must cover: the evidence you would look for to
determine whether the coordinates are degrees or metres, the tests you would run
(the numeric ranges, the total bounds, a distance distribution, a comparison
against a known landmark), the two failure modes of guessing wrong, and the one
line of code you would add to reject the file.
