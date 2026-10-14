# Exercises — 17-05-05 Spatial Interpolation: IDW, Kriging, Splines

Attempt these before reading the
[solutions](./05-spatial-interpolation-gis-solutions.md). The lesson is
[05 Spatial Interpolation](../05-spatial-interpolation-gis.md). All models are
**SYNTHETIC**.

## ★ Foundational

**★1.** Three samples lie at distances 1.0, 2.0 and 4.0 km from a target with
values 10, 14 and 16. Compute the IDW estimate with $p = 2$ and state the units of
the weights.

**★2.** A spherical variogram has nugget $c_0 = 0.3$, partial sill $c = 1.2$ and
range $a = 6$ km. Compute $\gamma(h)$ at $h = 0$, 3 km and 9 km, and state the
sill.

**★3.** State the expectation of Geary's C under no autocorrelation, and the
expectation of Moran's I for $n = 250$.

## ★★ Applied

**★★4.** A detrended variogram plateaus at 2.0 (mg/kg)² with a nugget of 0.25 and
a range of 5 km. Compute the stationary standard deviation, the standard deviation
you would report 8 km from the nearest sample, and the ratio.

**★★5.** Two spherical models fit a variogram almost equally well: (0.1, 0.9,
4 km) and (0.3, 0.75, 7 km). Compute the sill of each and state whether the
difference in their predicted maps can be resolved by the variogram alone.

**★★6.** A 40-sample survey is clustered with 30 samples inside a 2 km box. State
the direction of the bias in the empirical variogram at short lags, the correction
you would apply, and one number you would report to show the correction worked.

## ★★★ Research-oriented

**★★★7.** Design a sampling campaign that halves the kriging standard deviation at
a specified target location, using the fitted variogram to choose sample
locations, and cost it in samples.

**★★★8.** A colleague reports a variogram range of 8 km with no uncertainty. Write
the response that specifies what must be reported for the number to be usable, and
give the experiment that would put a range on the range.
