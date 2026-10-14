---
id: 07-02-03
title: "Survey Procedures: Loops, Drift, Repeatability and Ties"
level: advanced
prereqs: ["07-02-02", "07-01-05", "05-05-05"]
tags: [gravity, surveys, drift, loops, repeatability, ties, least-squares]
---

# Survey Procedures: Loops, Drift, Repeatability and Ties

**All models and data in this module are SYNTHETIC.** The anomaly field, drift
rate, step, noise, survey timing and tie uncertainties are chosen teaching values.
No survey, station, dataset or instrument is reproduced. The only exact quantity
used is $1\ \mathrm{\mu Gal} = 10^{-8}\ \mathrm{m\,s^{-2}}$, together with
$G = 6.67430\times10^{-11}\ \mathrm{m^{3}\,kg^{-1}\,s^{-2}}$ and
$1\ \mathrm{mGal} = 10^{-5}\ \mathrm{m\,s^{-2}}$ where a magnitude is needed.

## Learning objectives

By the end of this lesson you will be able to:

1. **Explain** why a relative survey is a set of *differences* plus a *datum*, and
   **write** the observation equation that relates a reading, a station value and
   the instrument's state.
2. **Correct** drift by base bracketing, piecewise interpolation and a step-aware
   model, and **compare** the three from measured errors.
3. **Explain** why a drift *step* is absorbed into a fitted slope, and **quantify**
   the resulting station error.
4. **Use** loop closure and per-segment slopes as diagnostics, and **state** the
   $\\sqrt{N}$ scaling of a random-walk closure.
5. **Distinguish** repeatability from reproducibility, and **compute** the repeats a
   target uncertainty demands and the point beyond which repeats buy nothing.
6. **Propagate** an absolute tie into the station values, and **explain** which
   errors cancel within a survey and which do not.
7. **Design** a base re-occupation interval from the drift rate and the target, and
   **fit** a joint least-squares adjustment of a loop with two drift models,
   **using the residual rms against the known reading noise as the test**.

## Prerequisites

- [07-02-02 Relative Gravimeters: Springs, LaCoste-Romberg, Scintrex](02-relative-gravimeters.md)
  — the sensor, its drift and its thermal sensitivity, which are the physical origin
  of everything here.
- [07-01-05 Units (Gal, mGal), Absolute vs Relative Measurement](../01-gravity-fundamentals/05-gravity-units-and-instruments-relative.md)
  — calibration, error propagation and network accumulation.
- [05-05-05 Quality Control](../../05-core-geophysics/05-survey-design-and-acquisition/05-quality-control.md)
  — the general survey-quality framework this lesson specialises.

## 1. The observation equation of a relative survey

Every reading of a relative gravimeter is

$$R_{ij} = g_{i} + D\left(t_{j}\right) + \epsilon_{ij},$$

where $g_{i}$ is the true gravity excess at station $i$ relative to the base,
$D(t)$ is the instrument's **state** at time $t$ (its zero reading including drift,
temperature response and any events), and $\epsilon$ is reading noise. The survey
returns $R$; the geology is in $g$; the instrument is in $D$. Everything in this
lesson is about separating them, and the separation is possible only because the
base is occupied repeatedly: at the base, $g = 0$ **by definition**, so repeated
base readings sample $D(t)$ directly.

That gives the structure of a survey procedure: occupy the base often enough to
determine $D(t)$ to the required accuracy, and occupy the stations in between. The
cost is time, and the design question is how that time is best spent.

**Measured (SYNTHETIC loop).** Seven stations at times $0.10$–$1.30\ \mathrm{h}$,
eight base occupations at $0.00$–$1.40\ \mathrm{h}$, a drift of
$15\ \mathrm{\mu Gal\,h^{-1}}$, a $30\ \mathrm{\mu Gal}$ step at $t = 0.55\
\mathrm{h}$ and $3.0\ \mathrm{\mu Gal}$ of reading noise. Without any drift
correction the error at the last station is $49.50\ \mathrm{\mu Gal}$ —
sixteen times the $3.0\ \mathrm{\mu Gal}$ reading noise.

## 2. Correcting drift: three procedures, measured

| procedure | rms station error (µGal) | max | error | (µGal) |
|---|---|---|---|
| no correction | 31.32 | 47.82 |
| one linear bracket (first and last base occupation) | 10.40 | 17.13 |
| piecewise-linear interpolation, all eight base occupations | 8.06 | 17.59 |
| piecewise-linear with one additional base occupation at $0.50\ \mathrm{h}$ | 4.50 | 8.54 |

Three quantitative lessons.

1. **Any drift model is much better than none** ($31.3 \to 10.4\ \mathrm{\mu Gal}$),
   and the single bracket costs only two base occupations.
2. **More base occupations do not fix a step** ($10.4 \to 8.1\ \mathrm{\mu Gal}$).
   The step sits inside one interpolation segment, so that segment's slope absorbs
   it: every station in the segment is mis-corrected, and no amount of extra bases
   elsewhere helps.
3. **A base occupation placed on the other side of the step does fix it**
   ($8.1 \to 4.5\ \mathrm{\mu Gal}$), because it turns an unmodelled event into a
   modelled level shift.

The implied drift rate from the single bracket is $34.79\
\mathrm{\mu Gal\,h^{-1}}$ against the injected $15.0\ \mathrm{\mu Gal\,h^{-1}}$:
the discrepancy is $19.79\ \mathrm{\mu Gal\,h^{-1}}$, i.e. the step divided by the
loop length, $30/1.40 = 21.43\ \mathrm{\mu Gal\,h^{-1}}$. A fitted slope cannot
distinguish "the instrument drifted faster" from "the instrument jumped once"; the
two are degenerate in a single bracket, and only extra observations break the
degeneracy.

### 2.1 Why a step is worse than noise

The step's error is **signed and time-correlated**: every station before the step is
corrected too little, every station after it too much. On a profile that pattern
looks exactly like a geological gradient, which is why it cannot be dismissed as
scatter. This is the operational meaning of the distinction between random and
systematic error made in [lesson 01](01-absolute-gravimeters.md): averaging does not
touch it, and the only cures are detection and a model.

## 3. Closure, and the per-segment slopes that reveal events

**Closure** is the difference between the base's gravity as implied at the end of a
loop and at the start. It is the only part of a loop measurement that is independent
of the anomaly field, so it measures the instrument and the procedure, not the
rocks.

**Measured.** The base reads $+48.71\ \mathrm{\mu Gal}$ higher at the end of
$1.40\ \mathrm{h}$ than at the start, while the drift rate alone predicts
$21.00\ \mathrm{\mu Gal}$: the excess is $+27.71\ \mathrm{\mu Gal}$, which is the
$30\ \mathrm{\mu Gal}$ step plus noise. The closure *test* is thus a comparison with
the prediction of the drift model, and its interpretation requires a drift rate
known independently — from a previous survey, from the instrument's specification,
or from the segment slopes themselves.

**Per-segment slopes** are the more decisive diagnostic when base occupations are
frequent. Measured for the eight-occupation loop:

| segment (h) | implied rate (µGal/h) | departure from $15.0$ |
|---|---|---|
| 0.00–0.20 | $-6.79$ | $-21.79$ |
| 0.20–0.40 | $33.55$ | $+18.55$ |
| **0.40–0.60** | **124.97** | $+109.97$ |
| 0.60–0.80 | $4.52$ | $-10.48$ |
| 0.80–1.00 | $9.01$ | $-5.99$ |
| 1.00–1.20 | $47.77$ | $+32.77$ |
| 1.20–1.40 | $30.50$ | $+15.50$ |

The segment containing the step stands at $124.97\ \mathrm{\mu Gal\,h^{-1}}$
against the $15\ \mathrm{\mu Gal\,h^{-1}}$ of the rest: **the outlier is the
diagnosis**, and it costs nothing except occupying the base more often. Note also
that the *scatter* of the other segments ($-21.79$ to $+32.77$) sets the resolution
of the test: a step of $30\ \mathrm{\mu Gal}$ in a 0.2 h segment is a
$150\ \mathrm{\mu Gal\,h^{-1}}$ slope excursion, far above that scatter, and would
be detected; a step of $3\ \mathrm{\mu Gal}$ would not be.

**Closure scaling.** For a closed loop with $N$ independent readings the expected
closure rms is $\sqrt{N}$ times the reading noise:

| stations in loop | expected closure rms (µGal) |
|---|---|
| 2 | 4.24 |
| 4 | 6.00 |
| 6 | 7.35 |
| 12 | 10.39 |
| 24 | 14.70 |

A closure consistent with this scaling is the expected outcome; a closure that
grows *faster* indicates drift or an event, and one that grows *slower* than
$\sqrt{N}$ is suspicious — correlated readings, or a loop that does not actually
revisit the same point.

## 4. Repeatability, reproducibility, and the limits of averaging

**Measured (SYNTHETIC, ten repeated occupations of one station in a few minutes):**

| quantity | value |
|---|---|
| standard deviation of readings | $2.48\ \mathrm{\mu Gal}$ (injected $3.0$) |
| standard error of the mean | $0.79\ \mathrm{\mu Gal}$ |
| repeats for a $2.0\ \mathrm{\mu Gal}$ standard error | 2 |
| repeats for $1.0\ \mathrm{\mu Gal}$ | 7 |
| repeats for $0.5\ \mathrm{\mu Gal}$ | 25 |

**Repeatability** is this spread over minutes. **Reproducibility** is the spread of
*station values* between days, operators or instruments; it includes drift, the
calibration scale, the tie and the reduction, and it is always the larger number.
Reporting repeatability as the survey's accuracy is the commonest over-claim in
field gravity, and the arithmetic above shows why: 25 repeats of a single occupation
give a $0.5\ \mathrm{\mu Gal}$ *repeatability*, while a $0.04\%$ calibration error
over a $5\ \mathrm{mGal}$ span contributes $2.0\ \mathrm{\mu Gal}$ that no number of
repeats can remove.

**Where averaging stops being useful.** Once the random term falls below the largest
systematic term, further repeats buy nothing. In the SYNTHETIC survey the systematic
terms are the drift model ($4.50\ \mathrm{\mu Gal}$), the calibration scale
($2.00\ \mathrm{\mu Gal}$) and the tie ($5.00\ \mathrm{\mu Gal}$), so repeating
beyond a standard error of about $1\ \mathrm{\mu Gal}$ is wasted effort — the design
should be spent on dense base occupations and a calibration check instead.

## 5. Ties: the datum, and what cancels

A relative survey measures differences. The **tie** to an absolute station supplies
the level, so the station value is

$$g_{i}^{\text{absolute}} = g_{\text{base}}^{\text{absolute}} +
\left(g_{i} - g_{\text{base}}\right)_{\text{survey}},$$

with the uncertainty of the two parts combined in quadrature:

| term | SYNTHETIC value (µGal) | correlated across the survey? |
|---|---|---|
| absolute tie | 5.00 | yes |
| reading noise (4 samples) | 1.50 | no |
| drift model, single bracket | 10.40 | partly (time-dependent) |
| drift model, with a base at the step | 4.50 | partly |
| calibration scale ($0.04\%$ of a $5\ \mathrm{mGal}$ span) | 2.00 | yes |

Totals: $11.81\ \mathrm{\mu Gal}$ for the single bracket and
$7.17\ \mathrm{\mu Gal}$ with the additional base occupation. Two consequences
follow directly from the third column:

- **A correlated error cancels in anomalies.** If every station shares the same tie
  error, then differences *within* the survey — the interpreted quantity — are
  unaffected. This is why a survey can be much more useful than its absolute
  accuracy suggests.
- **A correlated error does not cancel when surveys are compared.** Two surveys with
  different datums differ by the difference of their tie errors, and no analysis of
  either one alone can reveal it.

## 6. Designing the base-occupation interval

The drift-model error grows with the interval over which the model is extrapolated.
Taking, as a SYNTHETIC guide, a model error equal to $8\%$ of the drift accumulated
over the interval (a plausible curvature and settling residual), the station error is

| interval (min) | drift $10\ \mathrm{\mu Gal\,h^{-1}}$ | drift $25\ \mathrm{\mu Gal\,h^{-1}}$ | drift $50\ \mathrm{\mu Gal\,h^{-1}}$ |
|---|---|---|---|
| 10 | 0.13 | 0.33 | 0.67 |
| 20 | 0.27 | 0.67 | 1.33 |
| 30 | 0.40 | 1.00 | 2.00 |
| 60 | 0.80 | 2.00 | 4.00 |
| 120 | 1.60 | 4.00 | 8.00 |

For a $5\ \mathrm{\mu Gal}$ target with a $25\ \mathrm{\mu Gal\,h^{-1}}$ drift the
interval must be under about 25 minutes; with a $10\ \mathrm{\mu Gal\,h^{-1}}$ drift
an hour is comfortable; with $50\ \mathrm{\mu Gal\,h^{-1}}$ even 15 minutes is
marginal. **The interval is a design output, computed from the measured drift rate
and the target, and it should be quoted with the survey result** so that a reader
can judge whether it was adequate.

## 7. A joint least-squares adjustment of the loop

All the observations can be solved at once. With $g_{i}$ the station anomalies
(including the base at $g = 0$), and a drift model with parameters
$\mathbf{p}$, the system is

$$R_{j} = \sum_{i}\delta_{ij}g_{i} + \mathbf{a}_{j}^{T}\mathbf{p} + \epsilon_{j},$$

linear in $\left(g_{i}, \mathbf{p}\right)$, so the weighted least-squares solution
is $\widehat{\mathbf{x}} = \left(A^{T}WA\right)^{-1}A^{T}W\mathbf{R}$ with
$W = \sigma_{\epsilon}^{-2}I$.

**Measured (SYNTHETIC, 16 observations: 7 stations and 9 base occupations; two
models).**

| model | station rms error (µGal) | mean formal $\sigma$ (µGal) | residual rms (µGal) | d.o.f. |
|---|---|---|---|---|
| linear drift | 8.79 | 3.29 | 6.16 | 7 |
| linear drift + step at $0.55\ \mathrm{h}$ | 3.33 | 3.41 | 1.69 | 6 |
| input reading noise | — | — | $3.0$ | — |

The step model also estimates the step itself as $+28.13 \pm 3.56\ \mathrm{\mu Gal}$
against the injected $30\ \mathrm{\mu Gal}$ — a $1.9\sigma$ agreement, which is what
the noise permits.

**How to read this table, and how not to.**

1. **The residual rms is the test.** The linear model leaves
   $6.16\ \mathrm{\mu Gal}$ against a known reading noise of $3.0\
   \mathrm{\mu Gal}$: it is rejected by its own residuals, with no external
   information. The step model leaves $1.69\ \mathrm{\mu Gal}$.
2. **A residual *below* the noise is a warning, not a triumph.** The algebraic
   degrees of freedom are $B - 3$ for $B$ base occupations, because the stations
   contribute unknowns as fast as observations. With nine base occupations there are
   only six degrees of freedom, so the step model's $1.69\ \mathrm{\mu Gal}$ reflects
   over-fitting as much as accuracy. The honest statement is "adequate", not "better
   than the reading noise".
3. **The formal $\sigma$ is the claim.** The station values carry
   $3.3$–$3.4\ \mathrm{\mu Gal}$ formal uncertainties, consistent with the realised
   $3.33\ \mathrm{\mu Gal}$ rms error — a calibration of the uncertainty estimate
   against reality, which is only possible in a synthetic study like this one.
4. **The adjustment does not invent information.** It redistributes the closure
   residual optimally; the step still has to be *modelled*, and the model choice —
   not the algebra — decides the answer.

## 8. Assumptions and regime of validity

1. **The base is revisited at the same point.** A "base" that is re-set with a metre
   of horizontal error has a different gravity; the closure test conflates that with
   instrument drift.
2. **The drift model's functional form is adequate.** Section 7 tests it against the
   reading noise; a model that has never been tested against a known noise level has
   no claim to adequacy.
3. **Reading noise is stationary.** If the noise grows with wind, traffic or
   temperature, the weights $W$ must reflect it; constant weights are a model.
4. **Errors are independent between readings except for the tie.** Correlated
   environmental effects (temperature, pressure) break this and inflate the residuals
   in a time-correlated pattern.
5. **No uncompensated tilt or levelling error.** These are reading errors correlated
   with the station, so they resemble geology and must be controlled mechanically.
6. **The survey geometry is adequate for the anomaly's wavelength.** A drift-corrected
   profile cannot resolve a wavelength shorter than the station spacing; the
   sampling theorem is as binding here as in any method.
7. **The tie is a datum, not a check.** A tie does not verify the survey; it moves
   it. Verification needs a second independent tie or a repeat survey.
8. **Time is the cost.** Every procedure above trades time for accuracy, so the
   design must state its time budget; a procedure that is correct but unaffordable is
   not a design.

## 9. Python demonstration

`code/survey_procedures_demo.py` prints, with units:

1. a SYNTHETIC loop with its noise, drift, step, true anomalies and readings;
2. four drift-correction procedures with their measured rms and maximum errors, and
   the implied-versus-true drift rate;
3. closure, the per-segment slope table that localises the step, and the
   $\sqrt{N}$ closure scaling;
4. repeatability, its standard error, and the repeats a target demands;
5. the tie propagation table with the correlated/independent classification;
6. the design table for base-occupation intervals;
7. the joint least-squares adjustment with two drift models, the step estimate, the
   formal sigmas and the residual test.

Exercises and solutions:
[`exercises/03-survey-procedures-exercises.md`](exercises/03-survey-procedures-exercises.md),
[`exercises/03-survey-procedures-solutions.md`](exercises/03-survey-procedures-solutions.md).

## Mastery checkpoint

Answer without notes.

> A SYNTHETIC survey occupies a base at $t = 0$ and $t = 3.0\ \mathrm{h}$ and ten
> stations in between, with $2\ \mathrm{\mu Gal}$ reading noise and a nominal drift
> rate of $20\ \mathrm{\mu Gal\,h^{-1}}$. The base readings differ by
> $95\ \mathrm{\mu Gal}$. **(a)** Compute the expected difference from the nominal
> drift rate and the closure residual. **(b)** State what the closure residual
> implies and what it cannot distinguish. **(c)** Compute the expected closure rms
> from the reading noise alone, and compare. **(d)** Compute the station error left
> by a single linear bracket if the residual is a step at the midpoint. **(e)** State
> the cheapest procedural change that resolves the ambiguity.

A worked version is in the
[solutions](exercises/03-survey-procedures-solutions.md).

## Common pitfalls

1. **Quoting repeatability as accuracy.** It excludes drift, calibration and the
   tie; the lesson's arithmetic puts the difference at a factor of several.
2. **Fitting a single drift slope and calling it a correction.** A step in the
   record is absorbed into the slope (measured: $34.79$ against
   $15.0\ \mathrm{\mu Gal\,h^{-1}}$).
3. **Treating a closure error as noise.** The closure is the one measurement of the
   procedure; compare it with $\sqrt{N}\sigma$ and with the drift model's prediction.
4. **Occupying the base "about hourly" without arithmetic.** Section 6 shows the
   required interval depends on the drift rate and the target, and spans 10 to 120
   minutes across plausible instruments.
5. **Assuming a residual below the reading noise proves a good model.** With few
   base occupations the residuals are suppressed by over-fitting; count the degrees
   of freedom.
6. **Forgetting that the tie is correlated.** It cancels in anomalies within a
   survey and reappears when two surveys are compared.
7. **Spending the budget on repeats.** Once the random term is below the largest
   systematic, repeats are wasted; re-occupying the base and checking the calibration
   are not.
8. **Recording times, not states.** The drift model needs the reading's *time* (and
   ideally temperature and pressure) recorded with it; a timestamp added later is a
   guess.

## Related modules

- [Module 02 — Gravity Instruments and Surveys](README.md) — this module; lesson
  [01](01-absolute-gravimeters.md) supplies the absolute values used as ties, lesson
  [02](02-relative-gravimeters.md) the sensor whose drift is corrected here, and
  lesson [04](04-corrections-workflow.md) the next step in processing.
- [07-01-05 Units (Gal, mGal), Absolute vs Relative Measurement](../01-gravity-fundamentals/05-gravity-units-and-instruments-relative.md) —
  calibration and error propagation.
- [05-05 Survey Design and Acquisition](../../05-core-geophysics/05-survey-design-and-acquisition/README.md) —
  survey planning, coverage and quality control in general.
- [Module 18 — Inverse Problems](../../18-inverse-problems/README.md) —
  the weighted least-squares formulation in full generality.
- [Module 23 — Field Methods and Instruments](../../23-field-methods-instruments/README.md) —
  field logistics and good practice.
