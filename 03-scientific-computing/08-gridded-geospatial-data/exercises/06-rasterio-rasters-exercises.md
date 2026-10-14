# Exercises — 03-08-06 rasterio: Rasters, Windows, Masks and Reprojection

Attempt these **closed-book** before opening the
[solutions](./06-rasterio-rasters-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems that say "run the demo" refer to
[`../code/rasterio_rasters_demo.py`](../code/rasterio_rasters_demo.py); report its
**actual** output. The raster is **SYNTHETIC** (a plane, a Gaussian hill and a
ripple in EPSG:32612 with known analytic gradients). Nothing is downloaded and the
GeoTIFF is deleted on exit.

---

## ★ Foundational

**★1.** Write the affine equations for `x` and `y` in terms of `col` and `row`,
using a raster's `transform` coefficients `a`, `b`, `c`, `d`, `e`, `f`.

**★2.** A raster has `transform = (30.0, 0.0, 500000.0, 0.0, -30.0, 4200000.0)`.
(a) What is the coordinate of the corner of pixel (0, 0)?
(b) What is the coordinate of its centre?
(c) Which direction does the row index run?

**★3.** State the units of `res`, `bounds` and `nodata`.

**★4.** Name four resampling methods and give the statistic or data type each is
appropriate for.

---

## ★★ Applied

**★★5.** Run the demo, Sections 2 and 3.
(a) Report the corner and centre coordinates of pixel (0, 0).
(b) Report `y(row 0) - y(row 1)` and `x(0, 1) - x(0, 0)`.
(c) State the single sign error that would mirror the terrain north–south.

**★★6.** Run the demo, Section 4.
(a) Report the median and maximum errors in the recovered `dz/dx`.
(b) The plane's imposed gradient is 0.02000; what is the maximum additional
contribution from the ridge and hill terms?
(c) Explain why the maximum error is an order of magnitude larger than the median.

**★★7.** Run the demo, Section 5.
(a) Report the shapes, means and top-left centres of the correct and swapped
windows.
(b) Report the maximum absolute difference between the two reads.
(c) State the `Window` argument order in words.

**★★8.** Run the demo, Section 6.
(a) Report the masked and unmasked means and the difference.
(b) How many cells are masked, and what fraction of the grid is that?
(c) State why a `nodata` of 0.0 on an elevation grid is a defect.

**★★9.** Run the demo, Sections 8 and 9.
(a) Report the four coarse means and the maximum differences from a true 4 × 4
block mean.
(b) Report the source and target grid sizes and the degree cell size.
(c) Report the ground length of one target cell in each direction and their
percentage difference.

---

## ★★★ Research-oriented

**★★★10.** Reproject the demo's DEM from EPSG:32612 to EPSG:32611 (the neighbouring
UTM zone) instead of to EPSG:4326, and measure: the target grid shape, the cell
size, the valid fraction, and the value range. Compare with the EPSG:4326 case and
explain why the UTM-to-UTM reprojection involves resampling twice whereas the
UTM-to-degrees case involves a domain change. State the scale-factor error you
expect in zone 11 and check it.

**★★★11.** The recovered slope has a maximum bias of 2.124° when the geographic
cell is treated as isotropic. Design and run an experiment that determines the
latitudes at which that bias exceeds 1°, 2° and 5°, for the demonstration's
0.000315° target cell. Report a table and state the practical rule that follows. You
will need to simulate a field whose true slope you know on a geographic grid.

**★★★12.** Write a 300–450 word report on coregistration. Use the demo to place the
same synthetic surface on a grid offset by 0 m, 5 m and 15 m in x, and measure the
resulting difference in the recovered `dz/dx` and in the inferred elevation
difference between the two grids (compute the difference raster and report its mean
and standard deviation). Relate the 15 m case to the half-pixel convention, and
state the coregistration tolerance you would demand for a DEM with 0.5 m vertical
accuracy and slopes up to 30°.
