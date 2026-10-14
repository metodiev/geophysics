# Exercises — 17-05-03 Raster Data Model, Resolution and Resampling

Attempt these before reading the
[solutions](./03-raster-data-model-solutions.md). The lesson is
[03 Raster Data Model](../03-raster-data-model.md). All models are **SYNTHETIC**.

## ★ Foundational

**★1.** A raster has a 25 m cell, 4 000 columns and 3 000 rows. Compute the cell
area, the total area and the extent in km, and state the size in megabytes of a
float32 array.

**★2.** A transform is (a, b, c, d, e, f) = (25, 0, 500000, 0, −25, 4200000). State
the coordinate of the centre of cell (row, col) = (0, 0) and of cell (10, 20).

**★3.** A 4 km wavelength is sampled on a 1.5 km grid. State the Nyquist
wavelength, whether it is resolved, and the alias wavelength if it is not.

## ★★ Applied

**★★4.** A class occupies 8 % of the cells of a 10 m raster. The raster is
coarsened 8× by majority rule. Estimate the probability that a coarse cell is
classified as that class and state what happens to the class's total reported
area.

**★★5.** A hard classification of a 2 km² lake on a 100 m grid gives 1.88 km².
Compute the perimeter term $P h / (2A)$ that explains the discrepancy and state
whether the reported figure is low or high by chance or by bias.

**★★6.** 4 % of the cells of a raster are NoData. Compute the fraction of 5 × 5
coarse cells that contain at least one NoData cell, and state the two aggregation
policies and their reported usable fractions.

## ★★★ Research-oriented

**★★★7.** A study compares a 30 m and a 250 m land-cover product and finds that
a forest class covers 42 % in one and 31 % in the other. Design the analysis that
separates the four candidate explanations: resolution, resampling statistic, class
definitions and change over time.

**★★★8.** Design a coarsening recipe that preserves a rare class occupying 1 % of
the cells, and state the resolution at which it must fail.
