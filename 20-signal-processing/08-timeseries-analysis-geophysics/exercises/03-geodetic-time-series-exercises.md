# Exercises — 20-08-03 Geodetic Time Series: Trends, Offsets, Noise Models

Attempt these before reading the
[solutions](./03-geodetic-time-series-solutions.md). The lesson is
[03 Geodetic Time Series: Trends, Offsets, Noise Models](../03-geodetic-time-series.md).
All models are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** Write the position model and classify each parameter as measured,
nuisance or assumed.

**★2.** State the relation between the spectral index $\kappa$ and the Allan
slope $\mu$. Compute $\mu$ for $\kappa = 0$, $-1$, $-2$ and predict it for
$\kappa = -3$.

**★3.** From the measured lag-1 autocorrelations of the three noise processes
($-0.010$, $0.810$, $0.999$), explain why this statistic alone cannot classify
the noise.

## ★★ Applied

**★★4.** A velocity of 4.0 mm/yr is estimated with a formal white-noise standard
error of 0.020 mm/yr. Using the measured ratios of true to formal scatter
(0.89 for white, 10.54 for flicker, 21.14 for a random walk), compute the
corrected uncertainty and the significance of the velocity under each noise
model.

**★★5.** A series is fitted with a trend and seasonal terms; the residual rms is
1.978 mm and the estimated trend is $2.4399$ mm/yr against a truth of
$2.5000$ mm/yr. A reviewer says "the fit is good and the trend is right, so the
model is fine". Answer using the demonstration's offset experiment.

**★★6.** The Allan slope measured for a real series is $-0.35$. State the
spectral index that is consistent with it under a single-index power-law model,
and say why the number is not sufficient to choose a noise model on its own.

## ★★★ Research-oriented

**★★★7.** Design a self-contained analysis protocol for a synthetic series that
contains an unknown number of offsets, and specify how you would (a) find the
epochs, (b) account for the multiplicity of the epoch search, and (c) propagate
the noise model into the trend uncertainty. State the output table you would
require, with one row per quantity.

**★★★8.** The demonstration estimates the trend uncertainty by Monte Carlo over
100 realisations at three spectral indices. Design a cheaper estimator that uses
only one realisation: an analytic covariance under a power-law noise model with
the index estimated from the same data. State the approximation you are making
and design the simulation that would measure its error.
