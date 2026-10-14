# Exercises — 17-07-01 Landsat, Sentinel and MODIS Data Products

Attempt these before reading the
[solutions](./01-landsat-sentinel-solutions.md). The lesson is
[01 Landsat, Sentinel and MODIS Data Products](../01-landsat-sentinel.md). All
models and values are **SYNTHETIC** teaching numbers.

## ★ Foundational

**★1.** A band has $g = 0.020\ \mathrm{W\,m^{-2}\,sr^{-1}\,\mu m^{-1}}$ per
count, $o = -1.00$, $E_s = 1800\ \mathrm{W\,m^{-2}\,\mu m^{-1}}$ and
$\theta = 30^\circ$. For $DN = 2500$, compute the radiance and the
top-of-atmosphere reflectance, showing the units of each step.

**★2.** For $\rho_{\text{red}} = 0.10$ and $\rho_{\text{nir}} = 0.35$, compute
NDVI. State its sign and its range.

**★3.** State the units of $g$, $o$ and $E_s$, and show by dimensional analysis
that $\rho = \pi L d^{2}/(E_s \cos\theta)$ is dimensionless.

## ★★ Applied

**★★4.** A calibration gain is $5\%$ too high ($g \to 1.05\,g$) while the offset
is unchanged. Using $\rho_{\text{red}} = 0.1160$ and $\rho_{\text{nir}} = 0.2653$
as the *reference*, explain in two sentences why the NDVI change is much smaller
than the $5\%$ change in the bands, and why it is not exactly zero.

**★★5.** Two adjacent pixels have $\rho_{\text{red}} = (0.05, 0.25)$ and
$\rho_{\text{nir}} = (0.45, 0.45)$. Compute the per-pixel NDVI values, their
mean, the NDVI of the mean bands, and the difference. Name the effect.

**★★6.** Using the reflectance model $\rho_{\text{nir}} = 0.05 + 0.50\,\mathrm{LAI}/
(\mathrm{LAI}+1)$ with $\rho_{\text{red}} = 0.05$, compute NDVI at
$\mathrm{LAI} = 2$ and $\mathrm{LAI} = 8$, and compare the change with the change
from $\mathrm{LAI} = 0.5$ to $\mathrm{LAI} = 2$. State what this shows.

## ★★★ Research-oriented

**★★★7.** Design a computational experiment to measure how the Jensen gap
between mean-of-NDVI and NDVI-of-mean grows with block size (from $1\times1$ to
$32\times32$). State the scene you would synthesise, the quantity you would
plot, the seed, and the conclusion you would expect. A specification that could
not be executed is a failed answer.

**★★★8.** A colleague argues that because NDVI is invariant to a multiplicative
gain error, calibration metadata can be ignored for index studies. Construct the
strongest correct version of this argument and then state its three failure
modes, each with a one-line counterexample.
