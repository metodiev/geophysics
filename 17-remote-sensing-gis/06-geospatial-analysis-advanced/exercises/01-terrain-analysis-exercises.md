# Exercises — 17-06-01 Terrain Analysis: Slope, Aspect, Curvature, Flow Accumulation

Attempt these before reading the
[solutions](./01-terrain-analysis-solutions.md). The lesson is
[01 Terrain Analysis](../01-terrain-analysis.md). All models are **SYNTHETIC**.

## ★ Foundational

**★1.** A 3 × 3 block of a DEM with 20 m cells is (rows north to south)
```
10 12 15
11 14 18
13 17 22
```
Compute $g_x$, $g_y$, the slope in degrees and the aspect as a compass azimuth,
using Horn's weights.

**★2.** A synthetic cone is $z = 300 - 0.4r$. State its exact slope everywhere
except the apex, and the one place where the 3 × 3 operator fails.

**★3.** Two headings are 350° and 10°. Compute the arithmetic mean and the
circular mean, and state which one is correct.

## ★★ Applied

**★★4.** A centred difference is taken over a total spacing of 600 m on a surface
whose dominant wavelength is 4 km. Compute the attenuation factor and the
percentage of the gradient that survives.

**★★5.** A D8 accumulation on a 400 × 300 grid gives a maximum of 24 000 cells
with 50 m cells. Convert to an area; then state the conservation identity the
accumulation must satisfy and the two bugs it detects.

**★★6.** A survey reports 40 % of a region steeper than 10° from a 20 m DEM, and
15 % from the same terrain at 100 m. Estimate the fraction at 400 m using the
$\mathrm{sinc}$ attenuation of a 3 km dominant wavelength, and state why the
estimate is only qualitative.

## ★★★ Research-oriented

**★★★7.** Design the processing chain that produces a curvature map from a noisy
DEM, stating the support of each intermediate product, the smoothing decision and
the verification you would run on a synthetic surface with an analytic curvature.

**★★★8.** A steepness threshold is used to define a hazard class. Design the study
that reports the class fraction with its resolution dependence, and state the
recommendation you would give to a user who must apply one threshold across a
mosaic of DEMs at different resolutions.
