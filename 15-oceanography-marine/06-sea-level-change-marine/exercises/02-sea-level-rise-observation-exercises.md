# Exercises — Observing Modern Sea Level Rise: Altimetry, Tide Gauges, GRACE

Use the relations of
[`../02-sea-level-rise-observation.md`](../02-sea-level-rise-observation.md) and the
demo `code/sea_level_rise_observation_demo.py`. **All models and data are SYNTHETIC.**

$$\sigma_b\approx\frac{\sigma}{T}\sqrt{12/n},\qquad b_{\text{bias}}=c\bar t,\qquad
\sigma_{\text{inf}}=\sigma_b\sqrt{\frac{1+\rho}{1-\rho}},\qquad 1\ \mathrm{mm}=361\ \mathrm{Gt}.$$

## ★ Foundational

**1.1 — Random trend error.** An altimetric record has 25 years of monthly means
(300 points) with a per-point error of 8 mm. Compute the trend uncertainty. How much
would the error fall if the record were doubled in length at the same sampling?

**1.2 — Drift.** An instrument drifts linearly at 0.08 mm/yr per year over a 30-year
record. Compute the trend bias and express it as a percentage of a 3.4 mm/yr trend.

**1.3 — Gauge and land motion.** A gauge sits on land rising at 2.0 mm/yr. If the
true geocentric rise is 3.4 mm/yr, what trend does the gauge report, and what bias
does that imply?

## ★★ Applied

**2.1 — The correction's own error.** For the gauge of 1.3, the vertical land motion
correction is applied using a remote GNSS station with a velocity uncertainty of
0.3 mm/yr. (a) What is the residual bias if the station's velocity is wrong by
20%? (b) Express the correction error as a percentage of the signal.

**2.2 — Closing a budget.** A 15-year record gives: altimetry
$3.20\pm0.40$ mm/yr, ocean mass (from gravity) $1.70\pm0.25$ mm/yr and steric
$1.60\pm0.20$ mm/yr. Compute the residual, its uncertainty, the significance of the
residual, and the equivalent mass rate in Gt/yr for the mass term.

**2.3 — Red noise.** A 20-year record has a lag-1 autocorrelation of 0.6 and a
white-noise trend uncertainty of 0.064 mm/yr. (a) Compute the inflated uncertainty.
(b) Compare it with the drift bias of 1.2 mm/yr computed in 1.2 and decide which
term must be reduced to improve the trend.

## ★★★ Research-oriented

**3.1 — The fingerprint crossover.** A mass of $2\times10^{18}$ kg is added to the
ocean. (a) Compute the eustatic rise. (b) Using the attraction
$GM/(gr)$ with $g=9.81\ \mathrm{m\,s^{-2}}$ and
$G=6.674\times10^{-11}\ \mathrm{m^3kg^{-1}s^{-2}}$, find the distance at which the
attraction equals the eustatic rise. (c) State two physical effects the point-mass
model omits and the direction in which each would move the crossover.

**3.2 — Systematic versus random.** You have a 15-year record and want to detect an
acceleration of 0.10 mm/yr². (a) Compute the trend change it produces over the
half-record mean time ($\bar t=7.5$ yr) and compare it with a 0.5 mm/yr drift
uncertainty. (b) Explain why a longer record does not resolve the ambiguity even
though the signal grows.

**3.3 — Cross-validation of observing systems.** Altimetry, gravity and
temperature/salinity data share a common source of error: the same geophysical
corrections and the same ocean-area mask. (a) Explain why adding their uncertainties
in quadrature underestimates the budget uncertainty. (b) Propose a test that would
reveal the shared error.
