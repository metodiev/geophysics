---
id: 07-04-04
title: "GNSS for Tectonics, Subsidence and Sea Level"
level: doctoral
prereqs: ["07-04-03", "07-04-02"]
tags: [gravity, geodesy, gnss, tectonics, subsidence, sea-level, time-series]
---

# GNSS for Tectonics, Subsidence and Sea Level

All models and data in this module are SYNTHETIC. The station velocities, noise
amplitudes, strain rates, sea-level records and station geometry used below are
chosen teaching values; no real station, network, earthquake or tide gauge is
used.

## Learning objectives

By the end of this lesson you will be able to:

1. **Fit** a position time series with a trend plus annual and semi-annual terms
   and **state** the formal uncertainty of each parameter.
2. **Demonstrate** that the formal error from a white-noise assumption is wrong
   when the residuals are correlated, and **measure** the inflation factor.
3. **Quantify** how the achievable velocity precision depends on record length
   for white and for power-law noise.
4. **Compute** strain rates from a small station array and **show** that a rigid
   rotation is inseparable from shear in a three-station rosette.
5. **Propagate** velocity uncertainties into strain-rate uncertainties and
   **decide** whether a network can resolve a given tectonic signal.
6. **Convert** a tide-gauge trend to an absolute sea-level trend using collocated
   vertical land motion, and **quantify** the error if it is ignored.
7. **Design** a monitoring experiment for a slow signal, stating the observation
   span, the noise model and the resolution achieved.

## Prerequisites

- [03 GNSS Positioning: Pseudorange, Carrier Phase and Ambiguity Resolution](03-gnss-positioning.md) —
  where the daily positions come from.
- [02 Height Systems: Ellipsoidal, Orthometric, Dynamic and Geoid Models](02-height-systems.md) —
  which height a GNSS time series actually reports.

## 1. From positions to physics

A GNSS time series is a set of daily (or hourly) three-component positions with
respect to a reference frame. Everything geophysical is a *difference* or a
*rate*: a plate velocity, a subsidence rate, an elastic strain accumulation rate,
a co-seismic offset, a seasonal response to water loading. Extracting them
requires a model of the signal and an honest model of the noise, and in this
subject the noise model is usually the harder and more consequential half.

The three standard signal components are:

- a **secular** term — a constant velocity, the quantity of interest;
- **seasonal** terms — annual and semi-annual, driven by surface mass loading,
  thermoelastic effects and, in some settings, real hydrology;
- **offsets** — antenna changes, earthquakes, equipment failures.

## 2. Least squares and the formal error

Model the series as

$$y(t) = a + b\,t + c\cos\frac{2\pi t}{T} + d\sin\frac{2\pi t}{T}
+ e\cos\frac{4\pi t}{T} + f\sin\frac{4\pi t}{T} + \epsilon(t),$$

with $b$ the velocity in $\mathrm{m\,yr^{-1}}$ because $t$ is measured in years.
The ordinary least-squares formal covariance is

$$\widehat{\mathrm{cov}}(\hat{\mathbf{x}}) =
\left(\mathbf{A}^{\mathsf{T}}\mathbf{A}\right)^{-1}s^{2},\qquad
s^{2} = \frac{\left\|\mathbf{y}-\mathbf{A}\hat{\mathbf{x}}\right\|^{2}}{n-p}.$$

*Numerical example (SYNTHETIC).* A $3$-year daily record with a true velocity of
$-2.5\ \mathrm{mm\,yr^{-1}}$, a $4.00\ \mathrm{mm}$ annual term, a
$1.50\ \mathrm{mm}$ semi-annual term and $0.80\ \mathrm{mm}$ rms white noise
gives

- fitted velocity $-2.484\ \mathrm{mm\,yr^{-1}}$ with a formal $1\sigma$ of
  $0.029\ \mathrm{mm\,yr^{-1}}$,
- fitted annual amplitude $4.050\ \mathrm{mm}$ (true $4.00$),
- fitted semi-annual amplitude $1.491\ \mathrm{mm}$ (true $1.50$).

The demonstration prints these. Two remarks: the formal error of
$0.029\ \mathrm{mm\,yr^{-1}}$ is *correct for white noise*, and the seasonal terms
must be **modelled, not smoothed away** — a short record with a large annual
signal leaks that signal into the trend if the season is omitted.

## 3. The noise is not white

Geodetic position series are dominated by temporally correlated noise: monument
instability, multipath changes, reference-frame noise, and real loading effects.
The demonstration replaces the white noise with power-law noise of the *same*
$0.80\ \mathrm{mm}$ rms, exponent $0$ (white), $1$ (flicker) and $2$
(random-walk-like), and runs $200$ realisations:

| exponent | mean velocity (mm/yr) | formal $\sigma$ (mm/yr) | empirical $\sigma$ (mm/yr) |
|---|---|---|---|
| 0.0 | $-2.498$ | 0.029 | 0.029 |
| 1.0 | $-2.467$ | 0.027 | 0.219 |
| 2.0 | $-2.482$ | 0.025 | 0.425 |

The estimator stays unbiased; the *error estimate* does not. With flicker noise
the true scatter is **8 times** the formal error, and with random-walk-like noise
**15 times**. A published velocity uncertainty computed under a white-noise
assumption is therefore not an uncertainty at all — it is an optimism, and the
colour of the noise, not its amplitude, decides how large the correction is.

## 4. How long a record?

Repeating the experiment as a function of record length, with flicker noise and
the same $0.8\ \mathrm{mm}$ rms:

| record (yr) | formal $\sigma$ (mm/yr) | empirical $\sigma$, flicker (mm/yr) |
|---|---|---|
| 1 | 0.291 | 0.714 |
| 2 | 0.057 | 0.385 |
| 5 | 0.013 | 0.123 |
| 10 | 0.005 | 0.057 |
| 20 | 0.002 | 0.028 |

The formal error falls almost exactly as $1/T$; the empirical error falls only as
about $T^{-0.4}$, i.e. as roughly $1/\sqrt{T}$ over this range. The practical
consequence is stark: **a twenty-year record buys about a factor of $25$ in
empirical precision, not a factor of $20^{1}$ in the formal sense, and a
one-year record gives $0.7\ \mathrm{mm\,yr^{-1}}$** — useless for most tectonic
questions. Order-of-magnitude improvements in what a network resolves are bought
with decades, not with better receivers.

## 5. Strain rate from a small array

Take three stations at the corners of a right triangle with $40\ \mathrm{km}$
legs, and a synthetic uniform velocity field with

$$e_{xx} = +20\times10^{-9}\ \mathrm{yr^{-1}},\quad
e_{yy} = -10\times10^{-9}\ \mathrm{yr^{-1}},\quad
e_{xy} = +15\times10^{-9}\ \mathrm{yr^{-1}},$$

plus a rigid rotation of $\omega = 30\times10^{-9}\ \mathrm{rad\,yr^{-1}}$. The
demonstration forms the differences directly:

| quantity | recovered ($10^{-9}\ \mathrm{yr^{-1}}$) | true |
|---|---|---|
| $e_{xx}$ | $+20.0$ | $+20.0$ |
| $e_{yy}$ | $-10.0$ | $-10.0$ |
| $e_{xy}$ (raw) | $+45.0$ | $+15.0$ |
| $e_{xy}$ after removing the rotation | $+15.0$ | $+15.0$ |

A rigid rotation adds exactly $\omega$ to the measured shear and **nothing** to
the diagonal terms. A three-station rosette therefore cannot separate strain from
rotation; this is the ambiguity of
[07-03-05 §5](../03-gravity-anomalies-and-modelling/05-derivatives-and-filters.md)
in a different guise, and it is removed only by having stations in more than three
independent directions, or by referencing the velocities to a frame in which the
rotation is known.

**Error propagation.** With $0.3\ \mathrm{mm\,yr^{-1}}$ of velocity uncertainty on
each station, a single baseline difference over $L = 40\ \mathrm{km}$ carries

$$\sigma_{e} \approx \frac{\sigma_v}{L}
= \frac{0.3\times10^{-3}}{4.0\times10^{4}}
= 7.5\times10^{-9}\ \mathrm{yr^{-1}}
= 7.5\ \mathrm{nstrain\,yr^{-1}},$$

which is the value the demonstration prints; differencing two stations raises it
by a further $\sqrt{2}$. Against a signal of $15\ \mathrm{nstrain\,yr^{-1}}$ that
is a marginal detection, and on a $20\ \mathrm{km}$ baseline the same velocity
error becomes $15\ \mathrm{nstrain\,yr^{-1}}$ — as large as the signal. This is
why strain-rate maps use long baselines, many stations and believable velocity
errors rather than more stations in a small area.

## 6. Sea level and vertical land motion

A tide gauge measures sea level relative to the land. If the land moves, the gauge
records that too:

$$\text{absolute sea level rate} = \text{gauge rate} - \text{land uplift rate}.$$

The demonstration's table (all SYNTHETIC) makes the size of the correction clear:

| gauge trend (mm/yr) | vertical land motion, uplift positive (mm/yr) | absolute sea level (mm/yr) |
|---|---|---|
| 3.00 | 0.00 | 3.00 |
| 3.00 | $-1.50$ | 4.50 |
| 3.00 | $+1.00$ | 2.00 |
| $-1.00$ | $-1.50$ | 0.50 |

A land-motion term of $1.5\ \mathrm{mm\,yr^{-1}}$ is comparable with the signal
being sought, and it changes the *sign* of the apparent change in the third and
fourth rows. Two consequences: a gauge without a collocated GNSS time series
cannot be compared with another gauge without importing that error; and the
uncertainty of the GNSS vertical rate — from §3 and §4, realistically
$0.3$–$1\ \mathrm{mm\,yr^{-1}}$ over a decade under correlated noise — enters the
sea-level budget directly. This is one of the clearest examples in geodesy of a
physical conclusion limited by a noise model rather than by an instrument.

## 7. Worked example

*A coastal station must detect $1\ \mathrm{mm\,yr^{-1}}$ of absolute sea-level
change with $95\%$ confidence over $10$ years.*

1. **Required rate uncertainty.** For a two-sided $95\%$ detection,
   $\sigma_{\text{rate}} \lesssim 1/2\ \mathrm{mm\,yr^{-1}}$.
2. **Gauge precision.** A well-maintained gauge achieves
   $\sim0.5\ \mathrm{mm\,yr^{-1}}$ over a decade (dominated by correlated noise
   and datum stability).
3. **GNSS vertical rate.** From the record-length table, $10$ years under flicker
   noise gives $0.057\ \mathrm{mm\,yr^{-1}}$ *if* the noise is at the
   $0.8\ \mathrm{mm}$ level of the demonstration; a realistic monument and
   atmosphere give $0.3$–$0.5\ \mathrm{mm\,yr^{-1}}$.
4. **Total.** $\sigma = \sqrt{0.5^{2}+0.4^{2}} = 0.64\ \mathrm{mm\,yr^{-1}}$,
   which fails the $\lesssim0.5$ target. The remedy is either a longer record
   (the empirical error falls slowly with $T$) or a site with better monument
   stability and less correlated noise — not a better receiver.
5. **Report:** the rate, the noise model used, the record length, and the
   detection threshold actually achieved.

## 8. Assumptions and regime of validity

1. **A stable, well-defined reference frame.** Frame rotation is
   indistinguishable from a rigid plate rotation — see
   [05 ITRF, Plate Motion Models and Frame Transformations](05-itrf-and-plate-models.md).
2. **Discontinuities identified and removed.** An unmodelled offset biases the
   velocity by its size divided by the record length.
3. **A noise model that matches the residuals.** White-noise formal errors
   understate the truth by up to an order of magnitude.
4. **Rigid blocks in the strain calculation.** Real networks cross faults and
   gradients; a uniform-strain estimate over a large area averages real structure.
5. **Common-mode error removed.** Regional correlation in network solutions
   introduces a spatially coherent error that mimics a rotation — this is exactly
   the constant of §5, and it is why frame realisation matters.
6. **The geophysical signal is linear over the window.** Non-linear transients
   (post-seismic relaxation, groundwater recovery) need their own models.

## 9. Physical interpretation

- A velocity is a *ratio* of a displacement to a time; correlated noise makes the
  effective number of independent samples far smaller than the number of epochs,
  which is why the empirical error falls more slowly than $1/T$.
- Strain rate is a *gradient* of velocity, so it amplifies short-baseline noise:
  the same $0.3\ \mathrm{mm\,yr^{-1}}$ is a serious velocity error and a hopeless
  strain-rate error on a $20\ \mathrm{km}$ baseline.
- Rotation and strain are the symmetric and antisymmetric parts of the velocity
  gradient tensor. Any measurement that samples only a few directions cannot
  separate them; this is linear algebra, not a limitation of the instrument.
- Sea-level change is a difference of two large numbers, one measured by a float
  and one by a satellite antenna, and the smaller of the two — land motion — is
  often the less well known.

## 10. Python demonstration

`code/gnss_geodesy_applications_demo.py` prints:

1. the $3$-year series fit with its formal errors;
2. the white/flicker/random-walk comparison, formal versus empirical;
3. the record-length table;
4. the strain-rate recovery with and without rotation, and the error propagation;
5. the tide-gauge/land-motion table.

Every number in this lesson is from that output; the script uses
`np.random.default_rng(20261014)` and exits 0.

## 11. Exercises

See
[`exercises/04-gnss-geodesy-applications-exercises.md`](./exercises/04-gnss-geodesy-applications-exercises.md)
and
[`exercises/04-gnss-geodesy-applications-solutions.md`](./exercises/04-gnss-geodesy-applications-solutions.md).

- **★** Write the design matrix for a trend plus annual term and state the units
  of the velocity coefficient.
- **★** Convert $0.4\ \mathrm{mm}$ rms of noise to the velocity uncertainty it
  implies for a $5$-year record, assuming the empirical $T^{-0.4}$ scaling
  measured in §4.
- **★★** From the record-length table, estimate the record needed for
  $0.1\ \mathrm{mm\,yr^{-1}}$.
- **★★** Compute the strain-rate uncertainty for a $20\ \mathrm{km}$ baseline with
  $0.4\ \mathrm{mm\,yr^{-1}}$ station velocities.
- **★★★** Design a four-station array that separates strain from rotation, and
  state the geometry condition that makes the separation possible.

## Mastery checkpoint

Without notes:

> A five-year vertical time series has a fitted rate of $-1.2\
> \mathrm{mm\,yr^{-1}}$ with a formal error of $0.08\ \mathrm{mm\,yr^{-1}}$
> computed under a white-noise assumption.

**(a)** Give a realistic uncertainty using the inflations measured in this
lesson.
**(b)** State what would change your answer to (a).
**(c)** Combine with a tide-gauge trend of $+2.0\ \mathrm{mm\,yr^{-1}}$ to give
the absolute sea-level rate, with an uncertainty.
**(d)** State whether the sign of the absolute rate is resolved.

## Common pitfalls

1. **Quoting a white-noise formal error.** It understates by up to $15\times$.
2. **Smoothing away a seasonal term** instead of modelling it, and thereby
   leaking it into the trend.
3. **Ignoring offsets.** One unmodelled step biases the velocity for the whole
   record.
4. **Calling a three-station shear a strain rate** without addressing rotation.
5. **Comparing absolute and relative sea level** without the land-motion term.
6. **Assuming more epochs mean proportionally better precision.** Under
   correlated noise they do not.

## 12. Applications

- **Plate-boundary monitoring.** Continuous networks track interseismic strain
  accumulation, slow slip and post-seismic transients.
- **Subsidence.** Groundwater withdrawal, mining and peat oxidation produce
  centimetre-per-year vertical motion that GNSS resolves directly.
- **Sea-level science.** Land-motion correction is a prerequisite for any
  absolute sea-level statement from gauges
  ([07-07-03 Sea Surface Topography and the Marine Geoid](../07-geoid-and-height-modern/03-sea-surface-topography.md)).
- **Glacial isostatic adjustment.** Vertical velocities from GNSS constrain
  mantle viscosity
  ([07-06-04 Post-Glacial Rebound: Viscosity and Ice History Inference](../06-earth-tides-and-rotation/04-post-glacial-rebound.md)).

## Related modules

- [03 GNSS Positioning: Pseudorange, Carrier Phase and Ambiguity Resolution](03-gnss-positioning.md).
- [05 ITRF, Plate Motion Models and Frame Transformations](05-itrf-and-plate-models.md).
- [21-01-02 Choosing Probability Models for Earth Data](../../21-statistics-bayesian-ml/01-statistics-in-practice/02-probability-models-earth.md) —
  the noise models used here.
- [07-03-07 Time-Variable Gravity: Hydrology, Ice and Mass Redistribution](../03-gravity-anomalies-and-modelling/07-time-variable-gravity.md) —
  the mass changes that load these networks.

## 13. Self-assessment checklist

- [ ] I can fit a trend plus seasonal terms and report formal errors.
- [ ] I can measure the inflation from correlated noise.
- [ ] I can state the record length needed for a target precision.
- [ ] I can compute strain rate and demonstrate the rotation ambiguity.
- [ ] I can propagate velocity errors into strain-rate errors.
- [ ] I can assemble a sea-level budget with the land-motion term.
