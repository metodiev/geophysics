# Exercises — 03-09-04 Raster-Vector Integration and Zonal Statistics

Attempt these **closed-book** before opening the
[solutions](./04-vector-raster-ops-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems that say "run the demo" refer to
[`../code/vector_raster_ops_demo.py`](../code/vector_raster_ops_demo.py); report its
**actual** output. The raster is **SYNTHETIC** (a plane, a ridge, a basin and a
90 m ripple on a 30 m grid in EPSG:32612) and the four survey blocks are synthetic
rectangles offset 17 m from the pixel grid. Nothing is downloaded.

---

## ★ Foundational

**★1.** A raster has 30 m cells. State the area of one cell in m² and in km².

**★2.** State the two boundary conventions for masking a polygon onto a raster, and
what each does with a pixel that is partly covered.

**★3.** Explain why `read(window=...)` and a mask built with `int(win.width)` can
disagree about which pixels belong to a polygon.

**★4.** Give three defensible definitions of "the mean elevation of the survey" and
say what each weights.

---

## ★★ Applied

**★★5.** Run the demo, Section 2.
(a) Report the nearest and bilinear values and the analytic truth at the three
stations.
(b) Report the maximum errors of each method.
(c) Report the values at a point and 10 m east, and at 30 m east, and explain the
pattern.

**★★6.** Run the demo, Section 3.
(a) Report the window offsets and size, and the shape read.
(b) Report the pixel count, the implied area and the error against the polygon area
under the centre rule.
(c) Report the origin of the window transform and of the raster transform, and the
distance between them.

**★★7.** Run the demo, Section 4.
(a) Reproduce the per-block table for the centre rule and the `all_touched` rule.
(b) Report the maximum difference in pixel count and in mean.
(c) State the decision procedure for choosing a rule.

**★★8.** Run the demo, Sections 6 and 7.
(a) Report the mean at each resolution and its deviation from the 1× value.
(b) Report the standard deviation at each resolution and the quadrature difference
between the finest and coarsest.
(c) Report the four pixelated areas and their errors against the true polygon areas.

---

## ★★★ Research-oriented

**★★★9.** Change the raster cell size to 90 m while keeping the extent fixed, and
re-run Sections 4, 5, 6 and 7. Report: the new pixel counts per block, the change in
the boundary-rule difference, the change in the area-quantisation error, and whether
the mean remains invariant. Then state how the expected area error scales with cell
size and whether the measurements follow it.

**★★★10.** Implement a *fractional* coverage zonal statistic: instead of an in/out
mask, compute each pixel's fractional area inside the polygon (for example by
supersampling the polygon at $8 \times 8$ sub-pixel resolution within an enlarged
window) and use the fractions as weights. Report, for the four blocks: the
fraction-weighted mean, the centre-rule mean and the `all_touched` mean, and the
area estimate from the fraction sum. State which of the three is closest to the
undiscretised truth and why the fractional method costs more.

**★★★11.** Write a 300–450 word methods paragraph for a paper reporting
area-averaged elevation change per glacier. It must specify: the CRS and why, the
raster source and its nominal cell size, the glacier-outline source, the boundary
rule and its justification, the treatment of `nodata`, the aggregation weighting,
and the uncertainty introduced by the boundary quantisation (use the demo's measured
numbers). Mark clearly which statements are measurements from the demo and which are
choices.
