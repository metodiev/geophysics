---
id: 05-05-05
title: "Acquisition QC: Noise Tests, Repeatability, Metadata"
level: advanced
prereqs: ["05-02-03", "01-13-09"]
tags: [quality-control, repeatability, noise-budget, drift, base-station, metadata]
---

# Acquisition QC: Noise Tests, Repeatability, Metadata

## Learning objectives

By the end of this lesson you will be able to:

1. **Build** a noise budget by combining independent contributions in quadrature,
   and identify the term that binds.
2. **Measure** repeatability from repeated occupations, and distinguish the
   repeatability of an instrument from that of a *procedure*.
3. **Derive** the residual error left by drift correction as a function of loop
   length and the number of loops, and check it against measured closures.
4. **Design** the noise tests that must be run in the field, and state what each one
   can and cannot detect.
5. **Propagate** a noise budget into a detectability statement (the link back to
   [05-05-01](./01-survey-planning.md)).
6. **Specify** the metadata that must be recorded so that the survey can be
   reprocessed, and state why each item is needed.

## Prerequisites

- [05-02-03 Noise, Drift, Tides and Instrument Bias in Field Data](../02-geophysical-fields-and-observables/03-noise-and-drift.md)
  — the physical origin of the terms that appear in the budget here.
- [01-13-09 Error and Uncertainty Propagation](../../01-mathematics/13-probability-and-statistics-foundations/09-error-propagation.md)
  — the quadrature rule and the standard error of a mean, used throughout.
- [05-05-04 Positioning with GNSS/DGPS and Static Corrections](./04-positioning-gnss.md)
  — the largest single term in the budget below.

## 1. Intuition: QC is the measurement of your own measurement

A survey's data are only as good as its estimate of their uncertainty. That estimate
cannot be produced afterwards: the information needed to compute it — repeat
occupations, loop closures, instrument self-tests, simultaneous base-station records
— is either acquired in the field or not at all.

Three ideas structure the whole subject:

- **Noise is a budget, and a budget has one binding term.** Adding terms in
  quadrature means the largest term dominates the total variance: in the measured
  budget of Section 3, one term carries 88 % of the variance. Improving anything
  else buys almost nothing.
- **Repeatability is a property of the procedure, not of the instrument.** The
  demo measures a repeated-occupation standard deviation of 0.431 mGal *including*
  drift and 0.0126 mGal after removing a fitted linear drift. The instrument's own
  reading scatter is 0.010 mGal. The factor of 43 between the first and the third
  number is the entire content of drift control.
- **A QC test is a hypothesis test.** A repeatability number comes from a finite
  sample and therefore has its own uncertainty; quoting 0.0126 mGal from 12 repeats
  without an interval is a misuse of the statistic.

## 2. Precise definitions

### 2.1 Terms in the budget

| term | symbol | character | reduced by |
|---|---|---|---|
| instrument reading scatter | $\sigma_{\text{inst}}$ | random | longer occupation, repeats |
| vertical positioning (free-air) | $\sigma_{z} \cdot 2g/a$ | **bias** if the datum is wrong, random if the GNSS noise is random | better positioning, not repeats |
| terrain / near-surface correction residual | $\sigma_{\text{terr}}$ | spatially correlated | better terrain data and modelling |
| tidal correction residual | $\sigma_{\text{tide}}$ | systematic in time | a better Earth-tide model |
| drift residual after ties | $\sigma_{\text{d}} = \dot{d}\,T_{\text{loop}}$ | systematic in time | shorter loops, more loops |
| coupling and setup scatter | $\sigma_{\text{cp}}$ | random | careful field procedure |

Because the terms arise from independent physical processes (to a good
approximation), the total is the quadrature sum

$$\sigma_{\text{tot}}^{2} = \sum_i \sigma_i^{2} .
\tag{1}$$

### 2.2 Repeatability

**Repeatability** is the standard deviation of independent repeated measurements of
the same quantity under the same conditions, at the same place. For a procedure, it
is estimated from $N$ repeated occupations by the sample standard deviation

$$s = \sqrt{\frac{1}{N-1}\sum_{i=1}^{N}(x_i - \bar{x})^{2}} .
\tag{2}$$

### 2.3 Drift

Instrument **drift** is a slow change in the reading that is not caused by the
field. A linear model with rate $\dot{d}$ gives a correction of $\dot{d}t$ at
elapsed time $t$. The rate is estimated from the *closures* of loops that begin and
end at a **base station**, a fixed point occupied repeatedly during the survey.

### 2.4 Ties, looping and absolute measurement

- A **tie** is a measurement that connects two stations through a known relation:
  a base re-occupation (time tie) or a link between two survey networks (datum tie).
- **Looping** is the practice of returning to the base station after a closed
  traverse, so that the accumulated error can be measured as a *misclosure* rather
  than assumed.
- An **absolute** measurement fixes the value in a global reference frame; a
  **relative** measurement fixes differences. Most field instruments are relative,
  and the network borrows its absolute value from a small number of absolute
  stations or from a global model.

## 3. A measured noise budget

[`code/qc_noise_budget_demo.py`](./code/qc_noise_budget_demo.py) assembles a budget
from *SYNTHETIC* component values chosen to represent a levelled relative-gravity
survey, and combines them by equation (1):

| term | value (mGal) | share of total variance |
|---|---|---|
| instrument resolution / repeatability | 0.0100 | 0.4 % |
| vertical positioning (DGPS at 0.5 m, via free-air) | 0.1540 | 87.9 % |
| terrain / near-surface correction residual | 0.0500 | 9.3 % |
| tidal and earth-tide correction residual | 0.0150 | 0.8 % |
| drift residual after ties | 0.0200 | 1.5 % |
| reading noise and coupling scatter | 0.0050 | 0.1 % |
| **total (quadrature)** | **0.1642** | 100 % |

Two lessons follow immediately.

**First: the budget is dominated by one term.** With DGPS-class positioning, 88 % of
the variance is the free-air consequence of the height error, computed with the
gradient derived in [05-05-04](./04-positioning-gnss.md) ($0.30785\ \mathrm{mGal\,m^{-1}}
\times 0.5\ \mathrm{m} = 0.154$ mGal). Buying a better gravimeter, or repeating every
station, would improve the other 12 % of the variance and leave the total at
$\sqrt{0.1642^{2} - 0.01^{2}} = 0.1639$ mGal. The correct action is to upgrade the
positioning.

**Second: a budget predicts the anomaly threshold.** With
$\sigma_{\text{tot}} = 0.1642$ mGal, the $3\sigma$ detection threshold is 0.49 mGal.
Compare the target amplitudes in
[05-05-01](./01-survey-planning.md): the "modest massive body" at 0.0388 mGal is
undetectable by this survey, and no amount of processing changes that. The budget is
therefore the *first* thing to check against the objective, before mobilisation.

## 4. Measured repeatability and the cost of drift

The demo simulates 12 repeated occupations of one station, 4 minutes apart, with a
*SYNTHETIC* linear drift rate of 0.030 mGal/min and 0.010 mGal of reading scatter:

| quantity | measured |
|---|---|
| repeated occupations | 12 |
| interval between repeats | 4.0 min |
| elapsed span | 44.0 min |
| standard deviation of the raw readings | 0.43096 mGal |
| drift rate estimated from the data by least squares | 0.02987 mGal/min |
| standard deviation after removing the fitted drift | 0.01262 mGal |
| ratio raw / corrected | 34.14 |
| accumulated drift over the span | 1.32 mGal |

The estimated rate (0.02987) recovers the true rate (0.03000) to better than 0.5 %,
and the corrected repeatability (0.0126 mGal) approaches the input reading scatter
(0.010 mGal) but does not reach it — the difference is the *error in the estimated
drift rate*, which is a residual covariance between the drift estimate and the
scatter.

The practical statement of this table: **the drift term, not the instrument, sets the
repeatability of an uncorrected occupation.** A survey that does not correct drift
has a repeatability of 0.43 mGal whatever its gravimeter cost.

### 4.1 Loop closures and the length of a loop

Loops return to a base station. If the drift is linear with rate $\dot d$ and the
closure noise is $\sigma_c$, a loop of duration $T$ closes with misclosure

$$\Delta_j = \dot d\,T + \epsilon_j, \qquad \epsilon_j \sim \mathcal{N}(0, \sigma_c^{2}) .
\tag{3}$$

Averaging $m$ loops gives a rate estimate whose standard error is

$$\sigma_{\dot d} = \frac{\sigma_c}{T\sqrt{m}} ,
\tag{4}$$

and applying it leaves a residual at the end of a subsequent loop of duration $T$:

$$\sigma_{\text{residual}} = T\,\sigma_{\dot d} = \frac{\sigma_c}{\sqrt{m}} .
\tag{5}$$

Equation (5) is the design rule: **the residual drift error depends only on the
closure noise and the number of loops, not on the loop length** — but the *residual
within one loop grows linearly with the loop length* because the correction is a
straight line and the true drift need not be.

The demo measures (8 loops of 25 minutes, $\sigma_c = 0.010$ mGal *SYNTHETIC*):

| quantity | measured | prediction |
|---|---|---|
| mean closure misclosure | 0.74495 mGal | $\dot d T = 0.75$ mGal |
| standard deviation of closures | 0.00984 mGal | $\sigma_c = 0.010$ mGal |
| estimated drift rate | 0.02980 mGal/min | 0.03000 mGal/min |
| error in the estimated rate | 0.00020 mGal/min | $\sigma_c/(T\sqrt{m}) = 0.00014$ |
| residual over a 25 min loop | 0.00505 mGal | $\sigma_c/\sqrt{m} = 0.00348$ mGal |

The mean misclosure matches the drift prediction to three figures, and the standard
deviation of the closures recovers the input closure noise. The rate error and the
residual agree with equations (4)–(5) to within the scatter of a single dataset —
which is the honest caveat: one realisation of 8 loops cannot distinguish 0.0051 from
0.0035, and a plan should be based on the prediction with a stated factor, not on one
measured number.

Note the design consequence: halving the residual drift error requires **four times**
as many loops, by equation (5). That is the same square-root tax as every other
averaging scheme.

## 5. The field noise tests

Each test answers a different question, and none substitutes for another.

| test | what it measures | what it cannot see |
|---|---|---|
| **repeat occupation** at one station (10–20 times) | instrument scatter plus setup scatter, at one place | spatial variation; drift over a long day |
| **loop closure** (base re-occupation) | drift, and the closure noise of the whole procedure | errors that are common to the base and the stations |
| **base-station time series** (continuous, simultaneous with the survey) | temporal noise, tides, cultural noise with time structure | anything spatial |
| **calibration / self-test** (a known mass, a tilt or clamp test) | instrument scale, offset, and gross malfunction | field conditions |
| **day/night comparison** over the same station | cultural and anthropogenic noise, which usually has a strong daily cycle | geological signal |
| **repeat of a whole line** | reproducibility of the *entire* procedure | — |

Two points deserve emphasis. First, the **station repeatability test must be run
before the survey, at the survey site, at the same time of day as the survey**, or it
measures the wrong noise. Second, a good test is one whose result is *checked against
a prediction*: the demo's budget predicts a total of 0.1642 mGal, so a measured
repeatability of 0.16 mGal is confirmation and a measured 0.4 mGal means a term in
the budget is wrong (usually the positioning, or drift control, or terrain).

## 6. How many repeats, and how well is repeatability known?

The sample standard deviation of $N$ repeats has relative standard error

$$\frac{\mathrm{se}(s)}{s} \approx \frac{1}{\sqrt{2(N-1)}} ,
\tag{6}$$

a standard result for the normal distribution (see
[01-13-06 Point Estimation, Bias, Consistency and Efficiency](../../01-mathematics/13-probability-and-statistics-foundations/06-estimation-theory.md)).
The consequence is severe and often ignored:

| $N$ | relative standard error of $s$ |
|---|---|
| 5 | 35 % |
| 10 | 24 % |
| 20 | 16 % |
| 50 | 10 % |
| 200 | 5 % |

A repeatability quoted from five repeats is uncertain by a third. **To state a
repeatability to 10 %, fifty repeats are needed.** A survey that reports
"repeatability 0.01 mGal" from five occupations has reported a number with a
plausible range of 0.007–0.014 mGal, and a detection claim built on it inherits that
uncertainty.

## 7. Averaging, measured

The demo measures the standard error of an $N$-trace stack over 40 000 realisations
of unit-variance noise:

| $N$ | measured SEM | $\sigma/\sqrt{N}$ |
|---|---|---|
| 1 | 0.99218 | 1.00000 |
| 2 | 0.70472 | 0.70711 |
| 4 | 0.50141 | 0.50000 |
| 8 | 0.35395 | 0.35355 |
| 16 | 0.25136 | 0.25000 |
| 64 | 0.12575 | 0.12500 |

The measured values track $1/\sqrt{N}$ to within the 0.4 % sampling error expected
from 40 000 realisations — a reminder that the $\sqrt{N}$ law is exact for
independent noise and that any deviation measured in the field is *evidence of
correlated noise*, not of a broken law.

## 8. Metadata: the part that cannot be recovered later

The following must be recorded per station, in machine-readable form, as part of the
acquisition rather than reconstructed from the crew's notebooks:

| item | why |
|---|---|
| station identifier and coordinates | the link between the reading and the ground |
| ellipsoidal height *and* the geoid model used, or the orthometric height with its source | the largest term in the budget depends on it |
| date and time, with time zone and clock source | drift, tide and cultural-noise corrections all need it |
| instrument serial number and calibration date | different instruments have different scales |
| operator, weather, ground condition, and any setup anomaly | the only record of conditions that affect repeatability |
| base-station readings with their times | the drift correction cannot be reconstructed without them |
| raw reading *and* the value after every applied correction, separately | so that a correction can be undone or redone |
| file format version and processing-software versions | needed for the reproducibility statement of [05-06-06](../06-data-processing-principles/06-processing-transparency.md) |

The choices of vocabulary, units and file format are themselves standardised;
the conventions are covered in
[22-03-06 Metadata Standards](../../22-data-engineering-reproducibility/03-data-formats-and-engineering/06-metadata-standards.md)
and the general QC practice in
[22-03-05 Data Quality Control](../../22-data-engineering-reproducibility/03-data-formats-and-engineering/05-data-quality-control.md).

## 9. Assumptions

1. **Independent terms.** Equation (1) requires the terms to be uncorrelated. Two
   terms that are not independent must be added as covariances, not in quadrature:
   for example, a badly modelled terrain correction and a height error are strongly
   correlated, and adding them in quadrature understates the total.
2. **Gaussian noise for the statistical statements.** Equations (2), (4)–(6) assume
   normality. Spiky noise (a passing vehicle, an instrument glitch) inflates the
   sample standard deviation and is better handled by the robust scale estimators
   used in [05-06-01](../06-data-processing-principles/01-processing-pipeline-concept.md).
3. **Linear drift over the loop.** If the drift is nonlinear (thermal, or a
   different instrument regime), the residual after a linear correction is larger
   than equation (5) and loop length becomes more important, not less.
4. **The base station is stable.** A base station that itself moves (subsidence,
   frost heave, a nearby pump) transfers that motion to the survey.
5. **Repeatability is transferable.** The repeatability measured at one station in
   the morning is an estimate of the survey's repeatability; whether it applies at
   another station in the afternoon is an assumption, testable by repeating the test
   at the other station.

## 10. Units and dimensional analysis

Every term in the budget is in the survey's field unit (mGal, nT, m s⁻²), and
equation (1) is a variance sum, so its square root carries the same unit:

$$[\sigma_{\text{tot}}] = \sqrt{\sum_i [\sigma_i]^{2}} = \mathrm{mGal},$$

as required. Equations (3)–(5):

$$[\dot d\,T] = \mathrm{mGal\,min^{-1} \cdot min} = \mathrm{mGal}, \qquad
[\sigma_c/(T\sqrt{m})] = \mathrm{mGal/min}, \qquad
[T\,\sigma_{\dot d}] = \mathrm{mGal}.$$

The square-root law for averaging is dimensionless in its $N$-dependence, so it holds
in every unit.

## 11. Python demonstration

[`code/qc_noise_budget_demo.py`](./code/qc_noise_budget_demo.py) produces every
number in Sections 3, 4 and 7. The budget is four lines:

```python
budget = [("instrument", 0.010), ("vertical positioning", 0.154),
          ("terrain residual", 0.050), ("tide residual", 0.015),
          ("drift residual", 0.020), ("coupling", 0.005)]
total = float(np.sqrt(sum(v ** 2 for _, v in budget)))   # 0.1642 mGal
share = {name: v ** 2 / total ** 2 for name, v in budget}
```

and the drift estimate is a single least-squares fit, so that the residual
repeatability is measured against the same data that produced the estimate.

## 12. Exercises, common mistakes, applications

Companion problem sets:
[`exercises/05-quality-control-exercises.md`](./exercises/05-quality-control-exercises.md)
and [`exercises/05-quality-control-solutions.md`](./exercises/05-quality-control-solutions.md).

### Common mistakes

1. **Reporting a repeatability with no interval.** With five repeats the number is
   uncertain by a third, by equation (6).
2. **Running the noise test at a different site or time from the survey.** Cultural
   noise has a daily cycle; the test must be made under the survey's conditions.
3. **Correcting drift with a nominal rate** (a manufacturer's figure) instead of the
   survey's own closures. Drift is a property of this instrument, this day and this
   temperature history.
4. **Treating the biggest term as somebody else's problem.** The budget in Section 3
   is 88 % positioning; the remedy is in the positioning, however tedious.
5. **Recording metadata after the fact.** The time, the pole height and the setup
   conditions cannot be recovered from memory a month later.
6. **Assuming correlated errors average out.** Position, terrain and near-surface
   errors are correlated over hundreds of metres and produce smooth apparent
   anomalies; repeats cannot distinguish them from geology.

### Real-world applications

- **4-D (time-lapse) gravity and microgravity monitoring.** Repeatability, not
  accuracy, is the whole problem: a fixed monument network and centimetre
  re-occupation are mandatory, and the free-air gradient is why.
- **Aeromagnetic survey QC.** Line-to-line differences and tie-line misclosures play
  the role that loop closures play in ground surveys, and the same algebra applies.
- **Seismic QC.** The noise tests are shot records with the source off, instrument
  polarity checks, and the measurement of line-to-line misties; the
  *stack-and-fold* logic is the same $\sqrt{N}$ law.
- **Long-term observatories.** The metadata problem becomes the whole problem: a
  measurement is worthless to a successor if the instrument, the epoch and the
  corrections are not recorded with it.

## 13. Further reading

- **Hinze, W. J., von Frese, R. R. B., & Saad, A. H. (2013). *Gravity and Magnetic
  Exploration* (2nd ed.). Cambridge University Press.** Chapters on field procedures,
  drift and network adjustment; the definitive treatment of the loop algebra.
- **Telford, W. M., Geldart, L. P., & Sheriff, R. E. (1990). *Applied Geophysics*
  (2nd ed.). Cambridge University Press.** Chapter 2 (gravity field procedure and
  reduction) and Chapter 3 (magnetic procedure).
- **BIPM, JCGM 100:2008, *Evaluation of Measurement Data — Guide to the Expression
  of Uncertainty in Measurement*.** The normative treatment of combining uncertainty
  contributions, including the correlation caveat of Section 9. Freely available from
  the BIPM.
- **NOAA NCEI** — <https://www.ncei.noaa.gov/> — geophysical data archives; useful
  for checking what metadata accompanying archived surveys actually contain.
- **IRIS / EarthScope** — <https://www.earthscope.org/data/> — instrument and
  metadata practice for observatory-class networks.

> Note on citations: bibliographic details are given so you can locate the works.
> This repository does not host or reproduce copyrighted text, and you should
> confirm current availability and editions through your library before citing them.

## 14. Related lessons

- [05-05-04 Positioning with GNSS/DGPS and Static Corrections](./04-positioning-gnss.md) — the free-air term that dominates the budget.
- [05-05-01 Survey Planning](./01-survey-planning.md) — where the budget turns into a detectability statement.
- [05-06-01 The Processing Pipeline](../06-data-processing-principles/01-processing-pipeline-concept.md) — robust scale estimation and the first edit pass.
- [05-06-06 Documenting Processing: Reproducibility in Practice](../06-data-processing-principles/06-processing-transparency.md) — why the metadata must be machine-readable.
- [22-03-05 Data Quality Control](../../22-data-engineering-reproducibility/03-data-formats-and-engineering/05-data-quality-control.md) — the same discipline applied to datasets rather than surveys.

## 15. Self-assessment checklist

- [ ] I can list the terms of a noise budget and combine them in quadrature.
- [ ] I can identify the binding term in a budget and say what to do about it.
- [ ] I can measure repeatability from repeats and quote it with an interval.
- [ ] I can derive the drift-correction residual $\sigma_c/\sqrt{m}$ and explain the loop-length dependence.
- [ ] I can specify the field noise tests and the question each answers.
- [ ] I can explain why a positioning or datum bias does not average out.
- [ ] I can list the metadata items that cannot be recovered after the survey.
- [ ] I can turn a measured budget into a detection threshold and compare it with the objective.
