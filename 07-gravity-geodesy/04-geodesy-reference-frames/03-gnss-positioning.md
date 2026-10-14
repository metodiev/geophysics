---
id: 07-04-03
title: "GNSS Positioning: Pseudorange, Carrier Phase and Ambiguity Resolution"
level: graduate
prereqs: ["07-04-02", "21-01-02"]
tags: [gravity, geodesy, gnss, positioning, carrier-phase, dop]
---

# GNSS Positioning: Pseudorange, Carrier Phase and Ambiguity Resolution

All models and data in this module are SYNTHETIC, with two exceptions: the speed
of light and the L1 carrier frequency are defining constants, quoted exactly. The
satellite geometry, noise levels, baselines, delays and constellations used below
are chosen teaching values; no real satellite, constellation state or observation
is used.

## Learning objectives

By the end of this lesson you will be able to:

1. **Write** the pseudorange observation equation and **identify** which terms
   cancel in single, double and triple differences.
2. **Build** the geometry matrix and **compute** GDOP, PDOP, VDOP and HDOP for a
   given constellation.
3. **Derive** the position covariance and **verify** the prediction
   $\sigma_{\text{pos}} \approx \sigma_{\text{range}}\times\mathrm{DOP}$ by Monte
   Carlo.
4. **Convert** a carrier frequency to a wavelength and **quantify** the precision
   advantage of phase over code.
5. **Explain** and **implement** integer ambiguity resolution by least squares
   plus rounding, and **measure** the fix rate collapse as noise approaches half a
   cycle.
6. **Demonstrate** why a wrong integer fix can be worse than no fix, and state the
   tests that prevent it.
7. **Interpret** the effect of an unmodelled delay on the horizontal and vertical
   components separately.

## Prerequisites

- [02 Height Systems: Ellipsoidal, Orthometric, Dynamic and Geoid Models](02-height-systems.md) —
  what the height a GNSS receiver reports means.
- [21-01-02 Choosing Probability Models for Earth Data](../../21-statistics-bayesian-ml/01-statistics-in-practice/02-probability-models-earth.md) —
  Gaussian error models and covariance propagation.

## 1. The measurement

A GNSS receiver measures two quantities to each satellite it can see.

- The **pseudorange** $P$ is a code-phase timing measurement: coarse (metre
  level) but unambiguous.
- The **carrier phase** $\Phi$ is a measurement of the phase of the carrier,
  precise (millimetre level) but ambiguous by an unknown integer number of
  wavelengths.

In metres, with the geometric range $\rho$, receiver clock $c\,\delta t$, satellite
clock $c\,\delta t^{s}$, ionospheric $I$, tropospheric $T$ and multipath $M$:

$$P = \rho + c(\delta t - \delta t^{s}) + I + T + M_P + \epsilon_P,$$

$$\Phi = \rho + c(\delta t - \delta t^{s}) - I + T + \lambda N + M_\Phi +
\epsilon_\Phi .$$

The sign difference on $I$ is physical (the ionosphere delays the code and
advances the phase) and is the reason a dual-frequency combination cancels it.
Everything else in this lesson follows from the structure of these two equations:
**common terms cancel in differences, and $\lambda N$ does not**.

## 2. Satellite geometry and DOP

With $\mathbf{u}_i$ the unit vector from the receiver to satellite $i$ (so $-\mathbf{u}_i$
points from the satellite to the receiver), the linearised observation for the
position offset $\mathbf{b}$ and clock error $\delta$ is

$$A = \begin{pmatrix} -\mathbf{u}_1^{\mathsf{T}} & 1 \\ \vdots & \vdots \\
-\mathbf{u}_n^{\mathsf{T}} & 1 \end{pmatrix},
\qquad
\mathrm{cov}\begin{pmatrix}\mathbf{b}\\ \delta\end{pmatrix}
= \sigma^{2}\left(A^{\mathsf{T}}A\right)^{-1}.$$

The dilution of precision is the geometry factor in the square root of the
diagonal blocks. The demonstration uses two synthetic constellations of eight
satellites:

| geometry | GDOP | PDOP | VDOP | HDOP |
|---|---|---|---|---|
| well spread in azimuth and elevation | 1.84 | 0.98 | 1.32 | 0.76 |
| crowded into one direction | 127.51 | 83.32 | 35.69 | 79.28 |

**Geometry, not the number of observations, sets the precision.** Eight
satellites crowded together are worse than four well spread — a fact every
surveyor knows and every simulation should demonstrate.

## 3. The position solution and its error

Solving the linear system for a synthetic truth (position at the origin, receiver
clock $3000\ \mathrm{m}$) with $400$ Monte Carlo realisations per row:

| range noise (m) | geometry | rms horizontal error (m) | rms vertical error (m) | PDOP | VDOP |
|---|---|---|---|---|---|
| 0.5 | good | 0.485 | 0.637 | 0.98 | 1.32 |
| 0.5 | poor | 42.136 | 17.759 | 83.32 | 35.69 |
| 1.0 | good | 0.952 | 1.300 | 0.98 | 1.32 |
| 2.0 | good | 2.019 | 2.593 | 0.98 | 1.32 |

The measured horizontal rms tracks $\sigma\times\mathrm{PDOP}$ and the vertical
$\sigma\times\mathrm{VDOP}$ — the prediction of §2, confirmed by simulation. Note
that the horizontal rms is a two-dimensional radial error and the vertical is
one-dimensional, so they are not directly comparable; the reason the vertical
error is larger is VDOP, not a separate physical effect.

## 4. The carrier phase

With $c = 299792458\ \mathrm{m\,s^{-1}}$ (exact) and
$f_{L1} = 1575.42\ \mathrm{MHz}$,

$$\lambda_{L1} = \frac{c}{f_{L1}} = 0.190294\ \mathrm{m},$$

i.e. one cycle is $19.03\ \mathrm{cm}$ of range. A phase noise of $2\ \mathrm{mm}$
with a PDOP of $0.98$ gives a horizontal position error of order
$0.002\ \mathrm{m}$ — **two orders of magnitude better than code**. The price is
the integer: an error of one cycle in one difference is $19\ \mathrm{cm}$, so the
ambiguities must be resolved as integers, not as real numbers.

## 5. Double differences

Differencing between two receivers and two satellites eliminates the satellite and
receiver clocks, and leaves the geometry, the ionosphere and troposphere
partially, and the integer ambiguities:

$$\nabla\Delta\Phi = -\mathbf{u}_{i}^{\mathsf{T}}\mathbf{b}
+ \lambda\,\nabla\Delta N + \nabla\Delta I + \nabla\Delta T + \epsilon .$$

The demonstration's synthetic problem has $5$ satellites, $4$ double differences
per epoch and $10$ epochs with the constellation turning $36^{\circ}$ in azimuth
and $4^{\circ}$ in elevation per epoch: $40$ observations for $7$ unknowns (three
baseline components and four integer ambiguities). The design matrix has full
rank $7$ and condition number $13.2$, so the float solution determines both.

The demonstration solves for the real-valued ambiguities, rounds them, subtracts
the integer contribution, and re-solves for the baseline:

| phase noise (m) | float rms (m) | fixed rms (m) | fix success (%) |
|---|---|---|---|
| 0.002 | 0.0027 | 0.0014 | 100.0 |
| 0.020 | 0.0277 | 0.0140 | 100.0 |
| 0.060 | 0.0830 | 0.0472 | 98.0 |
| 0.100 | 0.1450 | 0.1238 | 77.0 |
| 0.140 | 0.1904 | 0.1904 | 55.3 |

Three lessons hide in this table.

1. **Ambiguity resolution is a decision, not an estimate.** Rounding is safe while
   the ambiguity scatter is well under half a cycle ($0.02\ \mathrm{m}$ is $0.10$
   of a cycle and fixes $100\%$ of the time).
2. **The fix rate collapses near half a cycle.** At $0.14\ \mathrm{m}$ —
   $0.74$ of a cycle — only $55\%$ of realisations fix correctly.
3. **A wrong fix is not a small error.** Each wrong integer adds $19.0\
   \mathrm{cm}$, so once the fix rate falls, the fixed solution is no better than
   the float one ($0.190\ \mathrm{m}$ against $0.190\ \mathrm{m}$). A fix must
   therefore be *tested* — by comparing the second-best integer candidate
   (ratio test) or by residual inspection — and the float solution kept as
   fallback.

Note also that the geometry changes between epochs while the integers do not: **it
is the change in geometry that makes the integers observable.** A static receiver
and satellite geometry would leave the ambiguity and the baseline confounded.

## 6. What an unmodelled delay does

Adding $3.0\ \mathrm{m}$ of extra path to one satellite of the well-spread
constellation:

| satellite azimuth / elevation (deg) | horizontal error (cm) | vertical error (cm) |
|---|---|---|
| 0 / 75 | 66.7 | $-216.7$ |
| 120 / 30 | 150.1 | 83.7 |

A delay on an **overhead** satellite maps almost entirely into the **height**
($-2.17\ \mathrm{m}$, more than three times the horizontal error); a delay on a
**low** satellite spreads into the horizontal. Two operational
consequences: the vertical is the weakest component of a satellite position, and
tropospheric and ionospheric modelling is mandatory rather than optional — a
$3\ \mathrm{m}$ unmodelled path is entirely plausible for a low-elevation
satellite with no mapping function.

## 7. Worked example

*A $12\ \mathrm{km}$ baseline is observed with $6$ satellites over $5$ epochs,
$\lambda = 0.190294\ \mathrm{m}$; the float ambiguity scatter is
$0.04\ \mathrm{m}$.*

1. **Convert to cycles:** $0.04/0.190294 = 0.21$ cycles. Well under half a cycle
   — fixing should succeed nearly always.
2. **Fixed baseline scattering:** roughly a factor $2$ below the float solution
   because the integer constraints remove four parameters. The demonstration's
   table shows $0.0830\ \mathrm{m}$ floating against $0.0472\ \mathrm{m}$ fixed at
   $0.06\ \mathrm{m}$ noise, a factor $1.76$ — of the same order.
3. **When it fails:** raise the noise to $0.14\ \mathrm{m}$ ($0.74$ cycles) and
   the fix rate is $55\%$, so about half the epochs get a wrong integer, each
   contributing $19\ \mathrm{cm}$. The float solution is then the better product
   until a ratio test can identify the good fixes.
4. **Report:** the baseline, its uncertainty from the fixed solution where the
   fix passed the test, and explicitly the fraction of epochs where it did not.

## 8. Assumptions and regime of validity

1. **Line-of-sight straight lines and vacuum propagation** except for the modelled
   ionosphere and troposphere.
2. **Known satellite orbits and clocks.** Orbit errors map into the solution almost
   one-to-one and are not removed by differencing over long baselines.
3. **Independent, Gaussian, zero-mean observation errors.** With multipath this
   fails badly, and residual correlations inflate the formal errors.
4. **Integer ambiguities are constant** over a continuous lock: a cycle slip
   breaks the assumption and must be detected and repaired.
5. **Differencing removes clock errors but not multipath, not atmospheric
   gradients, not antenna phase-centre variation.** These are the practical error
   floor of centimetre positioning.
6. **The vertical is intrinsically weaker** because all satellites are above the
   receiver, in a hemisphere; VDOP exceeds HDOP in any realistic geometry.

## 9. Physical interpretation

- DOP is a purely geometric statement: it says how a given range error is
  amplified into position error by the *shape* of the constellation. It has
  nothing to do with the signal.
- Differencing is a filtering operation in the observation domain: each difference
  kills a common-mode term and preserves the term that varies between satellites
  or receivers. The ambiguity survives because it belongs to the satellite-receiver
  pair.
- Carrier phase is precise because the wavelength is short compared with the
  code chip; the ambiguity is the price of that precision, and ambiguity
  resolution is the discipline that keeps the price finite.
- The vertical weakness is geometric, not physical: with every satellite above,
  the vertical component is constrained by geometry that is necessarily
  one-sided.

## 10. Python demonstration

`code/gnss_positioning_demo.py` prints:

1. the two constellations with their DOP quartet;
2. the Monte Carlo position errors against $\sigma\times$DOP;
3. the L1 wavelength and the noise comparison;
4. the ambiguity-resolution table with rank, condition number, float, fixed and
   fix rate;
5. the height-versus-horizontal delay table.

All output carries units; the script uses
`np.random.default_rng(20261014)` and exits 0.

## 11. Exercises

See
[`exercises/03-gnss-positioning-exercises.md`](./exercises/03-gnss-positioning-exercises.md)
and
[`exercises/03-gnss-positioning-solutions.md`](./exercises/03-gnss-positioning-solutions.md).

- **★** Write the pseudorange and phase observation equations and mark the terms
  cancelled by a double difference.
- **★** Convert $f = 1575.42\ \mathrm{MHz}$ to a wavelength, and a $0.05\ \mathrm{m}$
  ambiguity scatter to cycles.
- **★★** Given $\sigma = 4\ \mathrm{mm}$ and VDOP $= 2.5$, give the vertical
  uncertainty and the horizontal one for HDOP $= 1.1$.
- **★★** Explain why the design matrix in §5 loses rank if the constellation does
  not move between epochs.
- **★★★** Design an observation strategy that determines the vertical component
  to $1\ \mathrm{cm}$ with a stated constellation and noise level, and state the
  dominant remaining error.

## Mastery checkpoint

Without notes:

> A survey has $8$ satellites, PDOP $1.4$, VDOP $2.6$, code noise
> $0.6\ \mathrm{m}$ and phase noise $3\ \mathrm{mm}$; the float ambiguity scatter
> is $0.06\ \mathrm{m}$.

**(a)** Compute the code-based horizontal and vertical uncertainties.
**(b)** Compute the phase-based vertical uncertainty before fixing.
**(c)** Compute the ambiguity scatter in cycles and decide whether to fix.
**(d)** State what happens to the answer if the fix rate is $70\%$ and each bad
fix costs one cycle.

## Common pitfalls

1. **Reading DOP as a quality measure of the signal.** It is geometry only.
2. **Comparing horizontal and vertical errors directly.** One is radial (2-D),
   the other linear.
3. **Accepting a fix on rounding alone.** Test it, or keep the float solution.
4. **Ignoring the ionosphere.** A metre-level effect that differencing does not
   remove over long baselines.
5. **Assuming the vertical is as good as the horizontal.** VDOP is always worse.
6. **Forgetting that the geometry must change** for ambiguities to be observable.

## 12. Applications

- **Geodetic control and network densification.** Centimetre or millimetre
  positioning depends entirely on ambiguity resolution
  ([04 GNSS for Tectonics, Subsidence and Sea Level](04-gnss-geodesy-applications.md)).
- **Continental reference frames.** Global networks supply the observations from
  which frames are realised
  ([05 ITRF, Plate Motion Models and Frame Transformations](05-itrf-and-plate-models.md)).
- **Height determination.** GNSS heights plus a geoid model displace spirit
  levelling ([07-07-02 Vertical Datum Modernisation and National Height Systems](../07-geoid-and-height-modern/02-vertical-datum-modernisation.md)).
- **Machine control and monitoring.** The same mathematics at centimetre accuracy
  and one-second latency.

## Related modules

- [01 Geodetic Datums, Ellipsoids and Coordinate Frames](01-geodetic-datums.md).
- [02 Height Systems: Ellipsoidal, Orthometric, Dynamic and Geoid Models](02-height-systems.md).
- [04 GNSS for Tectonics, Subsidence and Sea Level](04-gnss-geodesy-applications.md).
- [21-01-02 Choosing Probability Models for Earth Data](../../21-statistics-bayesian-ml/01-statistics-in-practice/02-probability-models-earth.md).

## 13. Self-assessment checklist

- [ ] I can write the two observation equations and say what each difference
      cancels.
- [ ] I can build a geometry matrix and compute the DOP quartet.
- [ ] I can verify the DOP prediction by simulation.
- [ ] I can convert between phase noise in metres and in cycles.
- [ ] I can explain and implement ambiguity resolution, and state why a fix must
      be tested.
- [ ] I can predict the horizontal and vertical signature of an unmodelled delay.
