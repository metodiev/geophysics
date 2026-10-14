# Exercises — 17-05-04 Map Algebra and Raster Analysis

Attempt these before reading the
[solutions](./04-map-algebra-solutions.md). The lesson is
[04 Map Algebra](../04-map-algebra.md). All models are **SYNTHETIC**.

## ★ Foundational

**★1.** Classify each expression as local, focal, zonal or global, and state what
each depends on: (a) $\text{NDVI}$, (b) a 3 × 3 mean, (c) the mean elevation of
each basin, (d) the maximum of a raster.

**★2.** With per-band noise $\sigma_{\text{NIR}} = \sigma_{\text{red}} = 0.004$ and
reflectances NIR $= 0.30$, red $= 0.10$, compute $\sigma_{\text{NDVI}}$ from the
derivatives and state its units.

**★3.** A $5 \times 5$ focal mean is applied to a white-noise raster with standard
deviation 8. State the surviving standard deviation and the surviving variance.

## ★★ Applied

**★★4.** For the same NDVI, compute $\sigma_{\text{NDVI}}$ at NIR $= 0.10$,
red $= 0.03$ and state the ratio to the answer in ★2. Explain in one sentence why
a single NDVI threshold cannot carry a single uncertainty.

**★★5.** A slope map from a DEM with 100 m cells and a 5 km dominant wavelength is
recomputed with a 9-cell centred difference. Compute the attenuation factor
$\mathrm{sinc}(d/L)$ for $d = 900$ m and predict the ratio of the two mean slopes.

**★★6.** Three zones have 120, 60 and 30 cells with mean elevations of 500, 450 and
600 m. Compute the unweighted mean of the zone means and the area-weighted mean,
and state by how much the reporting choice changes the answer.

## ★★★ Research-oriented

**★★★7.** Design a curvature product robust to 2 m of DEM noise, and justify the
smoothing window from the noise spectrum rather than from appearance. State the
support of the final product and the metric you would use to show that the noise
is suppressed while real short-wavelength structure is retained.

**★★★8.** A weighted overlay of three criteria uses min–max normalisation over the
study area. A single outlier cell is added at the study area edge. Predict the
effect on every score in the map, give the quantity you would compute to bound the
effect, and state the normalisation you would use instead.
