---
id: 15-06-02
title: "Observing Modern Sea Level Rise: Altimetry, Tide Gauges, GRACE"
level: doctoral
prereqs: ["15-06-01", "15-01-05", "07-05-01", "07-03-07"]
tags: [oceanography, marine-geophysics, sea-level-change, altimetry, satellite-gravimetry]
---

# Observing Modern Sea Level Rise: Altimetry, Tide Gauges and GRACE

> **All models and data in this module are SYNTHETIC.** The records, trends,
> uncertainties and budgets below are teaching models with stated noise
> characteristics. No real mission, gauge, station or published trend is quoted,
> and no number comes from a published measurement.

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** the random-error uncertainty of a linear trend from the record
   length, the sampling and the per-point noise, and **show** why it is small.
2. **Quantify** the trend bias produced by a linear instrument drift and by an
   uncorrected vertical land motion, and **rank** the error terms.
3. **Correct** a tide-gauge record for vertical land motion and **state** the error
   budget of the correction itself.
4. **Close** a mass–steric budget, propagate its uncertainties and **interpret** a
   residual consistent with zero but not equal to it.
5. **Convert** a mass rate to an equivalent sea-level rate with the 361 Gt mm⁻¹
   constant, and a mass to a eustatic rise with the ocean-area constant.
6. **Explain** the self-attraction fingerprint and **compute** the distance at
   which the local sea level change changes sign.
7. **Distinguish** what each observing system measures (sea surface, relative sea
   level, mass, temperature/salinity) and name what none of them measures.

## Prerequisites

- [15-06-01 Palaeo Sea Level Reconstruction](01-paleo-sea-level.md) — the same
  budget and equivalent-sea-level ideas applied to the geological record.
- [15-01-05 Sea Level and Tides](../01-physical-oceanography/05-sea-level-and-tides.md) —
  what the sea surface does without any climate change.
- [07-05-01 GRACE and GRACE-FO](../../07-gravity-geodesy/05-satellite-gravimetry/01-grace-gracefo.md) —
  the gravity mission concept.
- [07-03-07 Time-Variable Gravity](../../07-gravity-geodesy/03-gravity-anomalies-and-modelling/07-time-variable-gravity.md) —
  mass redistribution from orbit.

## 1. Intuition: three instruments, three different seas

Three observing systems dominate modern sea-level science and they do **not**
measure the same thing:

- a **satellite altimeter** measures the distance to the sea surface and therefore
  the sea surface height relative to the satellite's orbit, i.e. a geocentric
  quantity;
- a **tide gauge** measures the sea surface relative to the *land* it is bolted to,
  i.e. a relative quantity contaminated by the land's vertical motion;
- **GRACE** measures the time-variable gravity field and therefore the *mass* in
  the ocean, with no ability to distinguish sea level from any other mass
  redistribution unless the geometry is supplied.

Each measurement is precise and each is systematically limited. The point of this
lesson, and the reason the level is doctoral, is that **the precision of modern
observing systems is no longer the limiting factor — the reference frame and the
systematic errors are**. A 20-year altimetric series with millimetre-level
single-point precision gives a random trend error of a tenth of a millimetre per
year, while a 0.1 mm/yr-per-year instrument drift biases the same trend by
1.0 mm/yr, thirty per cent of any plausible signal. The measurement noise has
become irrelevant.

## 2. Precise definitions

**Absolute (geocentric) sea level**: the sea surface height above the centre of
mass of the Earth — what altimetry measures.

**Relative sea level**: the sea surface height above the local solid Earth — what a
tide gauge measures; it changes when the land moves, the water moves, or both.

**Steric sea level**: the change in sea level due to changes in the density
(temperature and salinity) of the water column, at constant mass.

**Ocean mass (barystatic) contribution**: the part of sea-level change due to
added or removed mass, the part GRACE sees.

**Vertical land motion (VLM)**: the vertical velocity of the land at a gauge,
measured by GNSS and used to convert relative to geocentric sea level.

**Instrument drift**: a slow, systematic change in the instrument's response, which
adds a quadratic term to the record and biases a fitted linear trend.

**Sea-level fingerprint**: the geographically varying pattern of sea-level change
produced by self-attraction, loading deformation and rotational feedback.

## 3. Derivations and measurements

### 3.1 The random-error trend uncertainty

For a record of $n$ points at times $t_i$ with independent, identically
distributed errors $\sigma$, the least-squares slope has variance

$$\sigma_b^2=\frac{\sigma^2}{\sum_i(t_i-\bar t)^2} .$$

For $n$ points evenly spaced over a total duration $T$,
$\sum_i(t_i-\bar t)^2\approx nT^2/12$, so

$$\sigma_b\approx\frac{\sigma}{T}\sqrt{\frac{12}{n}} .$$

With $\sigma=10$ mm, $T=20$ yr and $n=240$ monthly means,

$$\sigma_b=\frac{10}{20}\sqrt{\frac{12}{240}}=\frac{10}{20}\times0.2236
=0.1118\ \mathrm{mm\,yr^{-1}} .$$

**The random term is negligible.** Note the two levers: the uncertainty falls with
the *duration* linearly and with the *number of points* only as $1/\sqrt n$.
Doubling the record length halving the error is worth far more than quadrupling the
sampling, which is why mission lifetime, not sampling rate, is the design
variable.

### 3.2 Systematic biases: drift

Model an instrument whose error grows linearly in time,
$\varepsilon(t)=c\,t$. The least-squares slope is biased by

$$b_{\text{bias}}=\frac{\sum_i(t_i-\bar t)\varepsilon(t_i)}{\sum_i(t_i-\bar t)^2}
=c\,\bar t ,$$

because the linear term is orthogonal to the mean but not to the trend. Over a
20-year record the mean time is $\bar t=10$ yr, so

| drift (mm/yr per yr) | trend bias (mm/yr) | fraction of a 3.3 mm/yr trend |
|---|---|---|
| 0.01 | 0.100 | 3.0% |
| 0.05 | 0.498 | 15.1% |
| 0.10 | 0.996 | 30.2% |
| 0.20 | 1.992 | 60.4% |

**A drift of 0.1 mm/yr per year — far too small to see in any single year's
comparison — moves the 20-year trend by a full millimetre per year.** The
comparison with §3.1 is the lesson: the systematic term is nine times the random
one, and it does not improve with more data. Trend statements are statements about
instrument pedigree.

### 3.3 Red noise

Real geophysical series are autocorrelated, and the variance of a mean (or a
trend) is inflated. For a first-order autoregressive process with lag-1
correlation $\rho$, the inflation is $\sqrt{(1+\rho)/(1-\rho)}$:

| $\rho$ | inflation | inflated trend uncertainty (mm/yr) |
|---|---|---|
| 0.0 | 1.00 | 0.1118 |
| 0.3 | 1.36 | 0.1524 |
| 0.5 | 1.73 | 0.1937 |
| 0.7 | 2.38 | 0.2661 |
| 0.9 | 4.36 | 0.4873 |

Even at $\rho=0.9$ the random term stays under 0.5 mm/yr. Autocorrelation matters,
but it does not change the ranking of §3.2.

### 3.4 Tide gauges and vertical land motion

A gauge measures $h_{\text{gauge}}=h_{\text{true}}+\int v_{\text{VLM}}\mathrm{d}t$,
so its trend is the sum of the true rise and the land velocity:

| VLM (mm/yr) | gauge trend (mm/yr) | bias vs a 3.3 mm/yr rise |
|---|---|---|
| −3.0 | 0.3 | −3.0 |
| −1.0 | 2.3 | −1.0 |
| 0.0 | 3.3 | 0.0 |
| +1.0 | 4.3 | +1.0 |

The correction requires a GNSS station at (or transferred to) the gauge, and the
correction carries its own budget:

| term | size (mm/yr) | share of the 0.3 mm/yr budget |
|---|---|---|
| GNSS vertical velocity | 0.300 | 100% |
| frame realisation | 0.200 | 67% |
| gauge datum stability | 0.100 | 33% |
| random trend error (50 annual means, $\sigma=5$ mm) | 0.049 | 16% |

The random trend error of 50 annual means with $\sigma=5$ mm is
$\sigma_b=5\sqrt{12/50}/50=0.049$ mm/yr — 16% of the GNSS correction error. **A
tide-gauge trend is a statement about a terrestrial reference frame as much as
about the sea**: change the frame realisation and a national network's trends shift
by a fifth of the GNSS error.

### 3.5 The mass–steric budget

Altimetry measures the total; GRACE the mass; Argo the steric part. The closure
identity is

$$\dot h_{\text{alt}}=\dot h_{\text{mass}}+\dot h_{\text{steric}}
+\varepsilon ,$$

with $\varepsilon$ the residual. A synthetic 15-year budget:

| component | value (mm/yr) | uncertainty (mm/yr) |
|---|---|---|
| altimetry (total) | 3.40 | 0.40 |
| GRACE (ocean mass) | 1.90 | 0.30 |
| Argo (steric) | 1.40 | 0.20 |
| residual | **+0.10** | **0.54** |

The residual uncertainty is $\sqrt{0.40^2+0.30^2+0.20^2}=0.54$ mm/yr, and the
residual is consistent with zero. **That closure within uncertainty is the
strongest statement the data support** — it is *not* a claim that the budget closes
exactly, and it is not a claim that the residual is meaningless. The phrase to
internalise: *consistent with zero, but not zero, with an uncertainty that is 16%
of the signal.*

The mass term converts with the constant from
[15-06-01](01-paleo-sea-level.md):

$$1\ \mathrm{mm}=361\ \mathrm{Gt},\qquad
0.361\ \mathrm{Gt\,yr^{-1}}\ \text{per}\ \mathrm{mm\,yr^{-1}} ,$$

so 1.9 mm/yr of ocean mass is $0.69\times10^{3}$ Gt/yr and 3.0 mm/yr is
$1.08\times10^{3}$ Gt/yr.

### 3.6 The fingerprint: the eustatic rise is not what any coast sees

Melt ice of mass $M$ and spread it uniformly: the eustatic rise is

$$\bar h=\frac{M}{\rho_{\text{sw}}A_{\text{ocean}}}
=\frac{10^{18}}{1025\times3.61\times10^{14}}=2.70\ \mathrm{m} .$$

But the added mass gravitationally attracts the ocean toward itself, raising the
geoid locally by $GM/(gr)$, while the removal of the ice load unloads the solid
Earth and lets the sea floor rise. Using the point-mass attraction
$GM/(gr)$ with $GM=gR^2$ approximations in the demonstration:

| distance (km) | attraction (m) | net local change (m) |
|---|---|---|
| 500 | 13.61 | −10.91 |
| 1000 | 6.81 | −4.10 |
| 2000 | 3.40 | −0.70 |
| 5000 | 1.36 | +1.34 |
| 10000 | 0.68 | +2.02 |

At 2000 km the attraction (3.40 m) exceeds the eustatic rise (2.70 m), so **sea
level falls near a melting ice sheet while the global mean rises**, crossing over
somewhere between 2000 and 5000 km. The point-mass approximation overstates the
attraction at distances comparable to the ice sheet's own size, so the near-field
entries are indicative only; the *sign* and the *existence of a crossover* are the
robust results. The demonstration also omits the ocean's gravitational
self-interaction, loading deformation and rotational feedback, which change the
pattern by tens of per cent.

## 4. Physical interpretation

- **Precision has stopped being the limit.** 0.11 mm/yr of random error against
  1.0 mm/yr of drift bias: the error budget is a systematic-error stack.
- **Every trend needs a frame.** Altimetric trends need the orbit frame; gauge
  trends need the terrestrial frame; GRACE trends need the gravity field's own
  low-degree handling.
- **The budget's power is its redundancy.** Three independent systems measuring
  overlapping quantities is what makes the closure a test rather than a tautology.
- **Mass and steric are physically different.** Mass is added water; steric is
  the same water expanding. Relating mass to a global mean sea level is a mass
  conversion (§3.5); relating it to a *local* sea level is a fingerprint problem
  (§3.6).
- **Regional patterns are larger than the mean.** The fingerprint amplitude near
  the source is several times the eustatic rise, with the opposite sign. Any
  "sea level rises by X when Y melts" statement without a location is incomplete.
- **Detection requires a drift model.** Because the drift bias is quadratic in
  time, no amount of record length removes it; only independent validation can.

## 5. Assumptions and regime of validity

1. **White noise for §3.1** and a single AR(1) parameter for §3.3. Real series have
   correlated, non-stationary errors and often seasonal and interannual signals;
   §3.3 is a lower-bound correction.
2. **Constant, linear drift.** Real drifts step, change sign and are monotone
   within a mission but not across missions; inter-mission bias is a separate,
   larger problem.
3. **Least-squares estimation of the trend.** A single trend over 20 years assumes
   the rate is constant; real records accelerate, and acceleration and trend are
   strongly correlated when estimated together.
4. **Independent error components in the budget.** Altimetry, GRACE and Argo share
   input data (e.g. the same geophysical corrections, the same leakage
   assumptions), so $\sqrt{\sum\sigma_i^2}$ understates the true uncertainty.
5. **A point-mass attraction for the fingerprint.** Valid only far from the source;
   the demonstration states this limitation, and the near-field entries must not be
   read as predictions.
6. **A rigid, non-rotating, non-self-gravitating ocean in the eustatic term.** The
   real response is a pattern computed with a sea-level equation.
7. **VLM measured by GNSS at one station.** Spatial gradients of VLM, monument
   instability and the transfer of a far GNSS velocity to the gauge each add
   unmodelled error.
8. **Argo's steric estimate is coarse.** It cannot resolve the abyssal and the
   deep ocean, and its salinity calibration is a known issue; a synthetic budget
   with a 0.20 mm/yr steric uncertainty assumes these away.
9. **A 0.4 mm/yr altimetric uncertainty.** Real altimetric budget errors can be
   larger because of the orbit, the radiometer correction and inter-mission bias.

## 6. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| trend | $b$ | mm/yr | |
| trend uncertainty | $\sigma_b$ | mm/yr | $\sigma\sqrt{12/n}/T$ |
| drift | $c$ | mm/yr per yr | |
| drift bias | $c\bar t$ | mm/yr | mm/yr² × yr |
| mass rate | | Gt/yr | 361 Gt per mm |
| mass | | Gt (kg) | 1 Gt $=10^{9}$ kg |
| eustatic rise | | m | $M/(\rho A)$ |
| attraction | | m | $GM/(gr)$ |
| inflation factor | | dimensionless | $\sqrt{(1+\rho)/(1-\rho)}$ |

A useful sanity check: kg/(kg m⁻³ × m²) = m, so a mass over a density and an area
is automatically a height. Getting metres out of Gt requires $10^{12}$ kg/Gt,
and dropping it is the commonest factor-of-a-trillion error in this field.

## 7. Worked examples

All numbers are printed by `code/sea_level_rise_observation_demo.py`.

### Example 1 — the random trend error

240 monthly points over 20 years with 10 mm errors:
$\sigma_b=0.1118$ mm/yr. Compare the drift bias for
$c=0.1$ mm/yr²: $c\bar t=0.996$ mm/yr, which is **8.9 times** the random term.

### Example 2 — the gauge and its correction

A gauge with a true 3.3 mm/yr rise sitting on land subsiding at 1.0 mm/yr reports
2.3 mm/yr; the correction is 1.0 mm/yr, and the GNSS correction's own error is
0.3 mm/yr, three times smaller but not negligible. The random trend error of the
gauge record (50 annual means, $\sigma=5$ mm) is 0.049 mm/yr — 16% of the GNSS
error and 5% of the signal.

### Example 3 — the budget

$3.40-1.90-1.40=+0.10$ mm/yr residual against a $\sqrt{0.40^2+0.30^2+0.20^2}=0.54$
mm/yr uncertainty: consistent with zero at the 0.2$\sigma$ level. The mass term,
1.9 mm/yr, is $1.9\times361=0.69\times10^{3}$ Gt/yr.

### Example 4 — the fingerprint

$10^{18}$ kg melts: eustatic $=10^{18}/(1025\times3.61\times10^{14})=2.70$ m; at
2000 km the attraction is 3.40 m and the net change is −0.70 m, i.e. **sea level
falls by 26% of the global rise** at that distance.

## 8. Python demonstration

`code/sea_level_rise_observation_demo.py` prints, with units:

1. the random trend error, the drift-bias law $c\bar t$ and the AR(1) inflation
   table;
2. the tide-gauge VLM table and the correction error budget;
3. the mass–steric budget, the residual and its uncertainty, and the Gt/yr
   conversions;
4. the melting fingerprint with the crossover and its stated limitations;
5. the worked-example values of Section 7.

```bash
cd 15-oceanography-marine/06-sea-level-change-marine/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python sea_level_rise_observation_demo.py
```

## 9. Exercises

[`exercises/02-sea-level-rise-observation-exercises.md`](./exercises/02-sea-level-rise-observation-exercises.md)
and
[`exercises/02-sea-level-rise-observation-solutions.md`](./exercises/02-sea-level-rise-observation-solutions.md).

## 10. Real-world applications

- **Coastal adaptation.** Local projections must include the fingerprint and the
  vertical land motion, not just a global mean.
- **Sea-level budget assessments.** The closure test is the field's routine
  verification step.
- **Reference-frame maintenance.** Gauge networks drive the requirements on the
  terrestrial reference frame
  ([07-04-04](../../07-gravity-geodesy/04-geodesy-reference-frames/04-gnss-geodesy-applications.md)).
- **Ice-sheet mass balance.** The mass term of the budget is the observable that
  constrains the ice sheets ([15-06-03](03-ice-sheet-marine-margins.md)).
- **Tide-gauge archaeology of past rates.** Long relative records, once corrected,
  extend the altimetric record backwards
  ([15-06-01](01-paleo-sea-level.md)).
- **Calibration of satellite altimetry.** Gauge and GNSS sites provide the in-situ
  bias and drift monitoring.

## 11. Further reading

- **Nerem, R. S., et al., "Climate-change-driven accelerated sea-level rise
  detected in the altimeter era", *PNAS*.** Level: research. The altimetric trend
  and the acceleration-versus-drift debate in one place.
- **Chambers, D. P., et al., "Evaluation of the global mean sea level budget
  between 1993 and 2014", *Surveys in Geophysics*.** Level: research. The
  mass–steric closure methodology and its error terms.
- **Gregory, J. M., et al., "Concepts and terminology for sea level", *Surveys in
  Geophysics*.** Level: graduate. The vocabulary, which is worth getting right.

> Bibliographic details are given so you can locate the works; this repository
> does not host or reproduce copyrighted text.

## Mastery checkpoint
- [ ] I can compute a trend uncertainty from $\sigma$, $T$ and $n$.
- [ ] I can explain and compute the drift bias $c\bar t$.
- [ ] I can correct a gauge trend for VLM and state the correction's error budget.
- [ ] I can close a mass–steric budget and interpret a residual honestly.
- [ ] I can convert mass to equivalent sea level and to a eustatic rise.
- [ ] I can describe the fingerprint and compute its crossover distance.
- [ ] I can say what altimetry, a gauge and GRACE each do and do not measure.
## Common pitfalls
1. **Quoting a random trend error as the uncertainty.** It is the smallest term in
   the budget.
2. **Reporting a tide-gauge trend without its VLM correction.** The bias is the
   same size as the signal.
3. **Treating the residual of a budget as a measured quantity.** It is a
   difference of uncertain terms.
4. **Adding uncertainties in quadrature when the inputs are correlated.** Shared
   corrections make the budget uncertainty larger than $\sqrt{\sum\sigma^2}$.
5. **Converting mass to height without the density and the ocean area.** See §6.
6. **Reading a fingerprint as a uniform offset.** The sign reverses with distance.
7. **Assuming an acceleration is detectable from a longer record alone.** Trend and
   acceleration co-vary strongly in short records, and drift mimics both.
8. **Confusing geocentric with relative sea level** when comparing an altimetric
   grid with a coastal gauge.

## Related modules
- [15-06-01 Palaeo Sea Level Reconstruction](01-paleo-sea-level.md) — the
  geological version of the same budget.
- [15-06-03 Ice Sheet Marine Margins and Stability](03-ice-sheet-marine-margins.md) —
  the source of the mass term.
- [07-05-01 GRACE and GRACE-FO](../../07-gravity-geodesy/05-satellite-gravimetry/01-grace-gracefo.md) —
  mission design and error sources.
- [07-03-07 Time-Variable Gravity](../../07-gravity-geodesy/03-gravity-anomalies-and-modelling/07-time-variable-gravity.md) —
  separating mass from geometry.
- [15-01-05 Sea Level and Tides](../01-physical-oceanography/05-sea-level-and-tides.md) —
  tides and the non-climatic sea surface.
- [07-04-04 GNSS Geodesy Applications](../../07-gravity-geodesy/04-geodesy-reference-frames/04-gnss-geodesy-applications.md) —
  vertical land motion measurement in practice.
