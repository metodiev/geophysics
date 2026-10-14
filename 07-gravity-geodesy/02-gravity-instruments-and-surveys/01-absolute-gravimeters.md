---
id: 07-02-01
title: "Absolute Gravimeters: Free-Fall and Interferometry"
level: graduate
prereqs: ["07-01-05", "02-01-02", "02-10-02"]
tags: [gravity, instruments, absolute-gravimeter, free-fall, interferometry, measurement]
---

# Absolute Gravimeters: Free-Fall and Interferometry

**All models and data in this module are SYNTHETIC.** The drop geometry, noise
levels, drag coefficient, laser wavelength and tidal amplitude are chosen teaching
values; no instrument, model number, manufacturer specification or published
measurement is reproduced or implied. The exact quantities used are
$G = 6.67430\times10^{-11}\ \mathrm{m^{3}\,kg^{-1}\,s^{-2}}$, the model Earth's
$GM = 3.986004418\times10^{14}\ \mathrm{m^{3}\,s^{-2}}$, and the unit relations
$1\ \mathrm{mGal} = 10^{-5}\ \mathrm{m\,s^{-2}}$,
$1\ \mathrm{\mu Gal} = 10^{-8}\ \mathrm{m\,s^{-2}}$.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** $g$ from a free-fall trajectory $z(t) = z_{0} + v_{0}t +
   \tfrac12 gt^{2}$ by least squares, and **compute** the formal uncertainty of the
   result from the normal equations.
2. **Measure** how that uncertainty depends on position noise, timing jitter and
   the number of samples, and **state** the scaling law each dependence follows.
3. **Explain** why a constant timing offset cancels exactly in a quadratic fit while
   random jitter does not, and **quantify** both.
4. **Convert** a displacement measurement into an interferometric fringe count, and
   **derive** the wavelength accuracy required for a given gravity accuracy.
5. **Derive** and verify that residual drag biases the fitted $g$ by exactly half its
   terminal acceleration.
6. **Compute** the tidal bias and its change within a drop set, and **decide** from
   measured numbers whether a midpoint correction is adequate.
7. **State** the difference between an absolute gravimeter's *statistical* precision
   from a set of drops and its *systematic* budget, and **explain** why improving
   one does nothing for the other.

## Prerequisites

- [07-01-05 Units (Gal, mGal), Absolute vs Relative Measurement](../01-gravity-fundamentals/05-gravity-units-and-instruments-relative.md)
  — units, calibration, and the absolute/relative distinction this lesson develops.
- [02-01-02 Measurement Uncertainty](../../02-physics/01-measurement-and-physical-reasoning/02-measurement-uncertainty.md)
  — least-squares estimation and error propagation.
- [02-10-02 Interference and Diffraction Optics](../../02-physics/10-optics-and-photometry/02-interference-diffraction-optics.md)
  — the two-beam interference used to measure the falling mass.

## 1. What "absolute" buys, and what it costs

A relative meter measures differences with exquisite precision and inherits its
level from a datum. An absolute gravimeter measures $g$ itself by tracking a
test mass through a known trajectory, so its value does not depend on any other
station. That independence is the whole product, and it is paid for in three
currencies:

- **Time.** A drop lasts about $0.2\ \mathrm{s}$; a set of hundreds of drops takes
  tens of minutes, and the tidal and environmental corrections must be applied to
  the set.
- **Mechanical precision.** The trajectory must be measured to nanometres and timed
  to nanoseconds (Section 3 measures both sensitivities).
- **Model completeness.** Because the answer is absolute, every neglected
  acceleration is a systematic error, not a common-mode error that cancels in a
  difference. Drag, tides, the vertical gradient of $g$, the frequency of the laser
  and the definition of the reference height all enter the answer.

The last point is the theme of this lesson: **an absolute instrument's accuracy is
set by its systematic budget, not by the scatter of its drops.**

## 2. The free-fall model and its least-squares solution

A test mass is released with velocity $v_{0}$ at position $z_{0}$ and falls under
constant acceleration $g$:

$$z(t) = z_{0} + v_{0}t + \tfrac12 g t^{2}.$$

Measuring positions at times $t_{i}$ gives a linear problem in the three unknowns
$\left(g, v_{0}, z_{0}\right)$, with model matrix columns
$\left(\tfrac12 t_{i}^{2},\, t_{i},\, 1\right)$:

$$A = \begin{pmatrix} \tfrac12 t_{1}^{2} & t_{1} & 1\\ \vdots & \vdots & \vdots\\
\tfrac12 t_{N}^{2} & t_{N} & 1\end{pmatrix},
\qquad
\widehat{\mathbf{p}} = \left(A^{T}A\right)^{-1}A^{T}\mathbf{z}.$$

The gravity value is $g = p_{1}$ directly (the factor $\tfrac12$ is already in the
model). With $s^{2} = \mathbf{r}^{T}\mathbf{r}/\left(N-3\right)$ the covariance is
$s^{2}\left(A^{T}A\right)^{-1}$, and $\sigma_{g}$ is the square root of its first
diagonal element.

**One SYNTHETIC drop** (drop height $0.200\ \mathrm{m}$, $N = 700$ samples,
position noise $1\ \mathrm{nm}$):

| quantity | value |
|---|---|
| drop duration $T = \sqrt{2h/g}$ | $0.201822\ \mathrm{s}$ |
| fitted $g$ | $9.820249989\ \mathrm{m\,s^{-2}}$ |
| error from the SYNTHETIC truth | $-1.053\ \mathrm{\mu Gal}$ |
| formal $\sigma_{g}$ | $2.472\ \mathrm{\mu Gal}$ |
| residual rms | $9.935\times10^{-10}\ \mathrm{m}$ ($0.99\,\sigma_{z}$) |

The formal uncertainty is consistent with the realised error, which is what a
correct covariance calculation should produce for one realisation. The residual rms
equal to the input noise is the check that the model has the right number of
parameters: too few and the residuals would exceed the noise, too many and they
would fall below it.

## 3. Where the precision comes from, measured

Two hundred Monte Carlo realisations per configuration, with the drop of
Section 2:

| configuration | $\sigma_{g}$ (µGal) |
|---|---|
| position noise $10^{-10}\ \mathrm{m}$ | 0.252 |
| position noise $10^{-9}\ \mathrm{m}$ | 2.625 |
| position noise $10^{-8}\ \mathrm{m}$ | 24.832 |
| timing jitter $10^{-10}\ \mathrm{s}$ | 0.301 |
| timing jitter $10^{-9}\ \mathrm{s}$ | 3.066 |
| timing jitter $10^{-8}\ \mathrm{s}$ | 28.713 |
| 200 samples ($\sigma_{z} = 1$ nm) | 4.675 |
| 700 samples ($\sigma_{z} = 1$ nm) | 2.490 |
| 2000 samples ($\sigma_{z} = 1$ nm) | 1.519 |

Three measured laws follow:

1. $\sigma_{g} \propto \sigma_{z}$: each factor of ten in the position noise gives a
   factor of ten in the gravity uncertainty ($0.252 \to 2.625 \to 24.832$).
2. $\sigma_{g} \propto \sigma_{t}$: each factor of ten in the timing jitter gives
   about a factor of ten ($0.301 \to 3.066 \to 28.713$).
3. $\sigma_{g}$ falls roughly as $1/\sqrt{N}$: from 200 to 700 samples the measured
   ratio is $4.675/2.490 = 1.88$ against the predicted
   $\sqrt{700/200} = 1.87$; from 700 to 2000 it is $1.64$ against
   $\sqrt{2000/700} = 1.69$. The agreement is close but not exact, because the
   noise realisation changes and the fit is not a simple mean.

The two noise types weigh the same: a nanometre of position noise costs
$2.6\ \mathrm{\mu Gal}$ and a nanosecond of timing jitter costs
$3.1\ \mathrm{\mu Gal}$. Reaching a few microgal from one drop therefore requires
*simultaneously* sub-nanometre position sensing and sub-nanosecond timing, and
averaging many drops only helps the random part of these — not a systematic
timing scale error.

### 3.1 Why a constant time offset is harmless

Shifting the time origin by $\delta t$ transforms the trajectory into

$$z\left(t+\delta t\right) = \tfrac12 g t^{2} + g\,\delta t\, t
+ \tfrac12 g\,\delta t^{2},$$

which is the *same model* with new values of $v_{0}$ and $z_{0}$. The fit therefore
absorbs it exactly: the demonstration measures a residual error of
$+2.1\times10^{-6}\ \mathrm{\mu Gal}$ for a $1\ \mathrm{ns}$ offset and
$+2.7\times10^{-6}\ \mathrm{\mu Gal}$ for a $100\ \mathrm{ns}$ offset, i.e. round-off.
Only jitter *within* the drop (or drift of the clock during the drop) contaminates
$g$. This matters practically: a constant trigger delay does not bias the answer,
but a clock whose rate varies during a $0.2\ \mathrm{s}$ drop does.

## 4. Interferometry: from fringes to metres

The falling mass carries a retroreflector in one arm of an interferometer, so the
optical path change is twice the displacement and each interference fringe
corresponds to a displacement of

$$\frac{\lambda}{2}.$$

**Numerical values (SYNTHETIC wavelength $\lambda = 633.0\ \mathrm{nm}$):**

| quantity | value |
|---|---|
| one fringe | $316.50\ \mathrm{nm}$ |
| fringes over a $0.200\ \mathrm{m}$ drop: $2h/\lambda$ | $631\,912$ |
| resolution at $1/64$ of a fringe | $4.945\ \mathrm{nm}$ |

The wavelength enters $g$ directly: since positions are determined in units of
$\lambda/2$, a relative wavelength error $\delta\lambda/\lambda$ produces a gravity
error of the same relative size,

$$\frac{\delta g}{g} = \frac{\delta\lambda}{\lambda}.$$

| relative wavelength error | resulting error in $g$ |
|---|---|
| $10^{-6}$ | $982.025\ \mathrm{\mu Gal}$ |
| $10^{-8}$ | $9.820\ \mathrm{\mu Gal}$ |
| $10^{-10}$ | $0.098\ \mathrm{\mu Gal}$ |

A microgal therefore requires the wavelength to be known to about one part in
$10^{9}$: the laser frequency must be **absolutely** known, not merely stable. This
is why absolute gravimetry is a frequency-metrology problem, and why the
instrument's reference is a stabilised laser whose frequency is traceable rather
than a convenient laboratory source. It is also why the *stability* of the laser
during a set matters separately: that is a systematic that no number of drops
averages away.

## 5. Residual drag, and an exact bias factor

A residual gas pressure exerts a drag proportional to velocity. Take
$\dot{v} = g - kv$, so with $v_{0} = 0$,

$$z(t) = \frac{g}{k}\left[t - \frac{1 - e^{-kt}}{k}\right]
= \tfrac12 g t^{2} - \frac{g\,k\,t^{3}}{6} + O\left(k^{2}t^{4}\right).$$

The perturbation is **cubic**, and a cubic perturbation is not orthogonal to
$\left\{1, t, t^{2}\right\}$: part of it lands in the quadratic coefficient, i.e. in
$g$. The demonstration measures the bias for three drag coefficients:

| $k$ ($\mathrm{s^{-1}}$) | terminal drag acceleration (µGal) | fitted-$g$ bias (µGal) | ratio |
|---|---|---|---|
| $10^{-5}$ | 1981.9 | $-991.0$ | $-0.5000$ |
| $2\times10^{-5}$ | 3963.9 | $-1981.9$ | $-0.5000$ |
| $4\times10^{-5}$ | 7927.8 | $-3963.9$ | $-0.5000$ |

The ratio is exactly $-0.5$: **the fitted $g$ is biased low by half the drag
acceleration at the end of the drop.** The result was verified independently by
integrating $\dot{v} = g - kv$ numerically and fitting the resulting trajectory,
which reproduces the same bias to four digits. A residual drag of
$200\ \mathrm{\mu Gal}$ at the end of the drop therefore costs
$100\ \mathrm{\mu Gal}$ — the same order as the quantity being measured. This is
why the drop chamber is evacuated and why the residual-gas correction is calibrated
rather than assumed.

## 6. Tides and the vertical gradient during a set

**Tide.** A SYNTHETIC semidiurnal tide of amplitude $120\ \mathrm{\mu Gal}$ and
period $12.4\ \mathrm{h}$ changes the measured acceleration during a set:

| set length | mean tidal acceleration | change within the set | mean minus value at midpoint |
|---|---|---|---|
| 1 min | $0.507\ \mathrm{\mu Gal}$ | $1.013$ | $-0.0000$ |
| 10 min | $5.064$ | $10.122$ | $-0.0015$ |
| 20 min | $10.110$ | $20.172$ | $-0.0120$ |
| 60 min | $29.757$ | $58.236$ | $-0.3209$ |

Two readings of this table matter. First, the tidal acceleration is tens of
microgal during a 20-minute set — far larger than the microgal precision being
claimed — so it must be modelled, not ignored. Second, the *mean* over the set
differs from the value at the set's midpoint by less than $0.013\ \mathrm{\mu Gal}$
for sets up to 20 minutes, so applying a midpoint correction is adequate at the
microgal level for those lengths and inadequate for sets of hours. The last column
is the justification of the practice, and it is a measurement, not a convention.

**Vertical gradient.** The gradient $-\mathrm{d}g/\mathrm{d}r = 2g/r$ at the model
surface is $308.280\ \mathrm{\mu Gal\,m^{-1}}$. Over a $0.2\ \mathrm{m}$ drop, $g$
varies by $61.656\ \mathrm{\mu Gal}$, so the fit returns $g$ at the *origin* of its
parabola, and any statement about a station's gravity must say which height it
refers to. One millimetre of height error is $0.308\ \mathrm{\mu Gal}$.

## 7. From a set of drops to a value with an uncertainty

**Measured (SYNTHETIC, 20 drops, per-drop scatter $2.40\ \mathrm{\mu Gal}$):**

| quantity | value |
|---|---|
| mean | $9.820250011\ \mathrm{m\,s^{-2}}$, error $+1.148\ \mathrm{\mu Gal}$ |
| standard error of the mean | $0.406\ \mathrm{\mu Gal}$ (predicted $2.40/\sqrt{20} = 0.537$) |
| with one drop perturbed by $+1.0\ \mathrm{mGal}$: mean error | $+6.148\ \mathrm{\mu Gal}$ |
| same set, median | $+1.285\ \mathrm{\mu Gal}$ |
| robust sigma from the median absolute deviation | $2.065\ \mathrm{\mu Gal}$ |
| largest deviation | $49.79$ robust sigma |

Three practical conclusions follow.

1. **A single disturbed drop dominates the mean.** One event at the mGal level moves
   the mean of twenty by $5$–$6\ \mathrm{\mu Gal}$, while the median moves by
   $0.14\ \mathrm{\mu Gal}$. Outlier rejection is part of the measurement.
2. **The robust sigma flags it.** With the median absolute deviation scaled to a
   Gaussian equivalent ($1.4826\times$MAD), the disturbed drop stands at
   $49.79$ robust sigma — unmissable, and independent of the mean that the outlier
   itself corrupted.
3. **Statistical precision is not accuracy.** Averaging $n$ drops reduces the random
   term as $1/\sqrt{n}$, but does nothing to the systematic budget of Sections 4–6.
   A set of a thousand drops with a $10^{-8}$ laser wavelength error is a
   $9.8\ \mathrm{\mu Gal}$ error quoted with $0.05\ \mathrm{\mu Gal}$ of statistics.

## 8. Assumptions and regime of validity

1. **Constant $g$ during the drop.** The gradient over $0.2\ \mathrm{m}$ is
   $61.7\ \mathrm{\mu Gal}$; the fit returns a value at a defined height, and the
   gradient must be known to convert between heights.
2. **Vacuum.** Residual drag enters as half its terminal value (measured
   above) and must be below the target uncertainty or corrected.
3. **No horizontal acceleration.** A tilt couples horizontal accelerations into the
   vertical direction; the instrument's level is part of its systematic budget.
4. **A known, stable laser frequency.** A relative wavelength error passes directly
   into $g$ (Section 4).
5. **A deterministic trajectory model.** Rotating or vibrating the drop chamber
   invalidates $z = z_{0}+v_{0}t+\tfrac12 gt^{2}$; the neglected terms are the
   documentation of a real instrument.
6. **Tide and environment modelled.** The solid Earth tide, ocean loading,
   atmospheric pressure and polar motion are corrections applied to the set; each is
   a model with its own uncertainty.
7. **The reference height is defined.** "The gravity at this station" is incomplete
   without the height at which it is quoted.
8. **Absolute means traceable, not exact.** An absolute measurement has a systematic
   budget; comparing two absolute instruments is a metrological exercise in which
   both budgets must be stated.

## 9. Python demonstration

`code/absolute_gravimeters_demo.py` prints, with units:

1. a least-squares free-fall fit with its formal uncertainty and residual rms;
2. the measured scaling of $\sigma_{g}$ with position noise, timing jitter and
   sample count;
3. the cancellation of a constant time offset;
4. the fringe count, half-wavelength and wavelength-accuracy requirement;
5. the drag bias, with the exact ratio $-0.5000$ verified against an independent
   quadrature of the trajectory;
6. the tidal mean, range and midpoint comparison for four set lengths;
7. the vertical gradient and the height-correction arithmetic;
8. the drop-set statistics with an outlier and a robust sigma.

Exercises and solutions:
[`exercises/01-absolute-gravimeters-exercises.md`](exercises/01-absolute-gravimeters-exercises.md),
[`exercises/01-absolute-gravimeters-solutions.md`](exercises/01-absolute-gravimeters-solutions.md).

## Mastery checkpoint

Answer without notes.

> A SYNTHETIC absolute gravimeter drops a mass $0.200\ \mathrm{m}$ with 700
> samples, position noise $1\ \mathrm{nm}$, and a laser wavelength known to
> $10^{-8}$ relative. **(a)** Compute the drop duration and the fringe count.
> **(b)** State the two dominant random contributions to one drop's uncertainty and
> their measured sizes. **(c)** Compute the wavelength systematic in microgal and
> compare it with (b). **(d)** Compute the drag bias if the drag deceleration at the
> end of the drop is $150\ \mathrm{\mu Gal}$. **(e)** State which of (b)–(d) could be
> reduced by running ten times as many drops and which could not.

A worked version is in the
[solutions](exercises/01-absolute-gravimeters-solutions.md).

## Common pitfalls

1. **Quoting a set's standard error as the instrument's accuracy.** It excludes the
   systematic budget (laser, drag, gradient, floor, tilt).
2. **Assuming a wavelength that is stable is a wavelength that is known.** The two
   are different requirements; only the second affects the value of $g$.
3. **Ignoring the vertical gradient.** "The gravity here" is meaningless without a
   height, and a $0.2\ \mathrm{m}$ drop geometry spans $61.7\ \mathrm{\mu Gal}$.
4. **Treating a constant timing offset as an error.** It cancels exactly; jitter and
   clock drift do not.
5. **Correcting the tide at the start or end of a set.** The midpoint is the
   defensible choice, and the demonstration measures the residual.
6. **Combining drops with a plain mean.** One disturbed drop can dominate twenty
   good ones; use a robust estimate and report the outlier.
7. **Believing a low scatter implies a small error.** A repeatable measurement of a
   mis-modelled quantity is repeatably wrong.

## Related modules

- [Module 02 — Gravity Instruments and Surveys](README.md) — this module; lesson
  [02](02-relative-gravimeters.md) covers the relative instruments whose differences
  are tied to these absolute values, and lesson [03](03-survey-procedures.md) the
  field procedures that use them.
- [07-01-05 Units (Gal, mGal), Absolute vs Relative Measurement](../01-gravity-fundamentals/05-gravity-units-and-instruments-relative.md) —
  units, calibration and uncertainty propagation.
- [02-01 Measurement and Physical Reasoning](../../02-physics/01-measurement-and-physical-reasoning/README.md) —
  least-squares estimation and error analysis.
- [02-10 Optics and Photometry](../../02-physics/10-optics-and-photometry/README.md) —
  interferometry and frequency stabilisation.
- [Module 06 — Earth Tides and Rotation](../06-earth-tides-and-rotation/README.md) —
  the tidal corrections applied to a set.
- [Module 23 — Field Methods and Instruments](../../23-field-methods-instruments/README.md) —
  how absolute and relative measurements are combined in practice.
