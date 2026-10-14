---
id: 07-01-05
title: "Units (Gal, mGal), Absolute vs Relative Measurement"
level: intermediate
prereqs: ["07-01-01", "02-01-02", "05-02-02"]
tags: [gravity, geodesy, units, gravimeter, calibration, uncertainty, precision-accuracy]
---

# Units (Gal, mGal), Absolute vs Relative Measurement

**All models and data in this module are SYNTHETIC.** The meter, its calibration
coefficients, the station values and the noise are chosen teaching values. No
instrument model, survey or dataset is reproduced. The only exact quantities are
$G = 6.67430\times10^{-11}\ \mathrm{m^{3}\,kg^{-1}\,s^{-2}}$, the model Earth's
$GM = 3.986004418\times10^{14}\ \mathrm{m^{3}\,s^{-2}}$ (a WGS84 defining
constant) and the unit definitions quoted in Section 2.

## Learning objectives

By the end of this lesson you will be able to:

1. **Convert** a gravity value among $\mathrm{m\,s^{-2}}$, Gal, mGal and µGal, and
   **express** a survey precision as a dimensionless fraction of the field.
2. **Quantify** how small a microgal is, in metres of elevation and in
   $\mathrm{kg\,m^{-3}}$ of density, and **explain** why those equivalences matter
   for survey design.
3. **Distinguish** an absolute from a relative measurement, and **state** which
   quantity each instrument actually produces.
4. **Write down** the meter equation that converts readings into gravity values,
   and **identify** which of its inputs is a measurement and which is a model.
5. **Fit** a calibration by least squares, **report** the slope, intercept, their
   uncertainties and their correlation, and **explain** why a calibration needs a
   wide gravity range.
6. **Propagate** calibration and reading uncertainties into a measured gravity
   difference, and **compare** the two contributions.
7. **Distinguish** precision from accuracy with a numerical experiment, and
   **state** why averaging cannot remove a calibration bias.
8. **Compute** how the uncertainty of a network grows with the number of
   measurement links, and **decide** whether a network is datum-limited or
   survey-limited.

## Prerequisites

- [07-01-01 Newtonian Gravitation, Field and Acceleration](01-newtonian-gravity.md)
  — the field, its units and its vertical gradient.
- [02-01-02 Measurement Uncertainty, Significant Figures and Error Bars](../../02-physics/01-measurement-and-physical-reasoning/02-measurement-uncertainty.md)
  — uncertainty propagation, which this lesson applies.
- [05-02-02 Field Measurement Units](../../05-core-geophysics/02-geophysical-fields-and-observables/02-field-measurement-units.md)
  — why geophysics uses field-specific units at all.

## 1. Why gravity has its own units

The field of the Earth is about $9.8\ \mathrm{m\,s^{-2}}$. The signals that matter
in exploration, geodesy and geodynamics range from a few tens of mGal for a
sedimentary basin to a few microgal for a cavity or a subsidence measurement. In
SI units the interesting part of the field sits in the sixth to ninth decimal
place, which is unreadable. The centimetre–gram–second family fixes this by choosing
a unit of the right size:

| unit | definition | in SI | typical use |
|---|---|---|---|
| 1 Gal | $1\ \mathrm{cm\,s^{-2}}$ | $10^{-2}\ \mathrm{m\,s^{-2}}$ (exact) | the field itself |
| 1 mGal | $10^{-3}$ Gal | $10^{-5}\ \mathrm{m\,s^{-2}}$ (exact) | exploration, regional surveys |
| 1 µGal | $10^{-3}$ mGal | $10^{-8}\ \mathrm{m\,s^{-2}}$ (exact) | geodetic, microgravity, time-variable work |

Because the conversions are exact powers of ten, all arithmetic can be done in mGal
and converted at the end. What is *not* exact is remembering which unit a software
package expects; the demonstration's first table prints the whole field in every
unit precisely so that a factor-of-$10^{5}$ error is visible at a glance:

| value | $\mathrm{m\,s^{-2}}$ | Gal | mGal | µGal |
|---|---|---|---|---|
| model surface $g$ | $9.82025\times10^{0}$ | $9.82025\times10^{2}$ | $9.82025\times10^{5}$ | $9.82025\times10^{8}$ |
| 1 mGal | $1.0\times10^{-5}$ | $1.0\times10^{-3}$ | $1.0$ | $1.0\times10^{3}$ |
| 1 µGal | $1.0\times10^{-8}$ | $1.0\times10^{-6}$ | $1.0\times10^{-3}$ | $1.0$ |
| a good absolute measurement | $5.0\times10^{-8}$ | $5.0\times10^{-6}$ | $5.0\times10^{-3}$ | $5.0$ |

A useful sanity rule: $1\ \mathrm{mGal}$ is $1.018\times10^{-6}$ of the model
surface field, i.e. about **one part per billion**. Gravity is a measurement made
at the ppb level, which is why its instruments look like metrology experiments and
why its error analysis is not optional.

## 2. How small is a mGal?

Three equivalences make the numbers physical.

**As a mass.** A $1000\ \mathrm{kg}$ mass produces $1\ \mathrm{mGal}$ at

$$r = \sqrt{\frac{GM}{g}} = \sqrt{\frac{6.67430\times10^{-11}\times10^{3}}
{10^{-5}}} = 0.0817\ \mathrm{m},$$

and $1\ \mathrm{\mu Gal}$ at $2.5835\ \mathrm{m}$ — a factor of $\sqrt{100} = 10$,
as $r \propto g^{-1/2}$ requires. A useful mental image: a small car one hand's
width away is a milligal.

**As elevation.** With the model gradient $2g/r = 3.083\times10^{-6}\
\mathrm{s^{-2}}$ from lesson [01](01-newtonian-gravity.md),

$$1\ \mathrm{mGal} \;\Longleftrightarrow\; 3.2438\ \mathrm{m}, \qquad
1\ \mathrm{\mu Gal} \;\Longleftrightarrow\; 3.24\ \mathrm{mm}$$

of station height. A microgal-level survey therefore needs millimetre height
control — which is why differential GNSS or precise levelling accompanies such
work, and why the free-air term of lesson [04](04-gravity-reduction.md) requires the
same care.

**As density.** The slab formula ties a microgal to a density–thickness product:

$$1\ \mathrm{\mu Gal} = 2\pi G\,\Delta\rho\,h
\;\Longleftrightarrow\;
\Delta\rho\,h = \frac{10^{-8}}{2\pi G} = 0.0238\ \mathrm{kg\,m^{-2}},$$

i.e. $0.0238\ \mathrm{kg\,m^{-3}}$ acting through $1000\ \mathrm{m}$ of rock, or
$0.2385\ \mathrm{kg\,m^{-3}}$ through $100\ \mathrm{m}$. Gravity responds to the
product, not to density or thickness separately — the ambiguity that module
[03](../03-gravity-anomalies-and-modelling/README.md) develops.

## 3. What a gravimeter actually produces

No gravimeter returns a gravity value. It returns a **reading**: a count, a
voltage, an interferometric fringe number, or a feedback current. The reading
becomes gravity through a **calibration** and a **datum**:

$$\boxed{\;g_i = g_{\text{base}} + c\,\left(R_i - R_{\text{base}}\right)
\;}$$

where $R$ are readings, $g_{\text{base}}$ is a known gravity value at a reference
station and $c$ is the calibration factor in mGal per count. This deceptively
simple equation contains the whole distinction of this lesson:

- $c$ is an **instrument property**, determined by calibration, not by the field;
- $g_{\text{base}}$ is a **datum**, determined by an absolute measurement or by
  convention;
- the *shape* of the field — every difference — comes from $c$ and the readings;
- the *level* of the field comes entirely from $g_{\text{base}}$.

Two instruments of the same type can agree about every difference and disagree
about the level, if their datums differ. Conversely, one instrument can agree with
an absolute meter about the level at the base and disagree about the shape, if its
calibration is wrong.

## 4. Absolute versus relative measurement

**An absolute measurement determines $g$ itself, without reference to another
gravity value.** The classical realisation is a free-fall experiment: a test mass
falls a known distance and the time of fall gives $g$ from $z = z_{0} + v_{0}t +
\tfrac12 gt^{2}$; modern instruments measure the trajectory interferometrically
(module [02](../02-gravity-instruments-and-surveys/README.md) derives the details).
An absolute measurement's uncertainty is quoted with its own value and does not
depend on any other station.

**A relative measurement determines a difference.** It is inherently cheaper,
lighter and more precise *about differences*: a relative meter resolves a few
microgal between two nearby stations, but its value at any station is only as
accurate as the calibration and the datum it inherits. In the demonstration's
SYNTHETIC example, the base is known absolutely to $5.0\ \mathrm{\mu Gal}$ and a
field station lies $6250$ counts away:

$$g_{\text{field}} = 979\,500.0000 + 6.2500 = 979\,506.2500\ \mathrm{mGal}$$

on nominal calibration — a number whose *level* is inherited and whose *difference*
is measured.

The practical consequence is a division of labour that runs through the rest of
this folder:

| question | needs | method |
|---|---|---|
| what is $g$ here, on an absolute scale? | an absolute instrument or a known datum | absolute measurement |
| how does $g$ differ between two points 50 m apart? | calibration and repeatability | relative measurement |
| how does $g$ change with time at one point? | a stable datum and repeatability | relative measurement |
| is my relative meter calibrated correctly? | an absolute station or a tie | calibration experiment |

## 5. Calibrating a relative meter

The meter equation is linear in two unknowns, so $N$ observations at stations with
known values determine them. Writing $y_{i} = g_{i}$ and $x_{i} = R_{i}$,

$$y_{i} = c\,x_{i} + b + \varepsilon_{i},
\qquad \varepsilon_{i} \sim \left(0, \sigma^{2}\right),$$

and the least-squares solution gives $c$, $b$ and their covariance

$$\widehat{\mathbf{p}} = \left(A^{T}A\right)^{-1}A^{T}\mathbf{y},
\qquad
\operatorname{cov}\left(\widehat{\mathbf{p}}\right)
= s^{2}\left(A^{T}A\right)^{-1},
\qquad s^{2} = \frac{\mathbf{r}^{T}\mathbf{r}}{N-2}.$$

**Measured (SYNTHETIC).** Twelve stations spanning a $12\ \mathrm{mGal}$ range,
readings with $0.3$ counts of noise, reference values known to
$5\ \mathrm{\mu Gal}$:

| quantity | value | uncertainty |
|---|---|---|
| slope $c$ | $1.000657\times10^{-3}\ \mathrm{mGal\,count^{-1}}$ | $3.89\times10^{-7}$ ($0.0389\%$) |
| intercept $b$ | $979\,487.6460\ \mathrm{mGal}$ | $0.0050\ \mathrm{mGal}$ ($5.0\ \mathrm{\mu Gal}$) |
| correlation $c$–$b$ | $-0.9565$ | — |
| residual rms | $0.00463\ \mathrm{mGal}$ ($4.6\ \mathrm{\mu Gal}$) | d.o.f. $= 10$ |

The nominal sensitivity was exactly $10^{-3}\ \mathrm{mGal\,count^{-1}}$; the fit
returns $999.344$ counts per mGal, i.e. $0.066\%$ away, which is the honest
accuracy of a calibration limited by $5\ \mathrm{\mu Gal}$ reference values over a
$12\ \mathrm{mGal}$ span.

**Why the correlation matters.** $c$ and $b$ have correlation $-0.9565$ because the
intercept refers to a reading of zero counts, far outside the observed range: an
error in the slope can be absorbed by the intercept. Two consequences:

1. The *differences* computed from the fit remain accurate, because they use
   $c$ over the observed range.
2. A calibration over a *narrow* gravity range would have an even stronger
   $c$–$b$ correlation and a larger slope uncertainty; a calibration must span as
   wide a range as possible, which in practice means tying stations at very
   different elevations. Centring the readings would decorrelate $c$ and $b$
   without changing any difference, which is why software reports the intercept at
   a stated reference reading.

## 6. Propagating the uncertainty into a difference

The quantity a survey actually reports is a difference,
$\Delta g = c\left(R_{2} - R_{1}\right)$, so

$$\sigma_{\Delta g}^{2} =
\underbrace{\left(R_{2}-R_{1}\right)^{2}\sigma_{c}^{2}}_{\text{calibration}}
+ \underbrace{2\,c^{2}\sigma_{R}^{2}}_{\text{readings}},$$

where the factor 2 in the second term is two independent readings.

**Measured (SYNTHETIC).** With a span of $6250$ counts and the fit above:

| contribution | value |
|---|---|
| measured difference | $6.2541\ \mathrm{mGal}$ |
| from the calibration slope | $2.4321\ \mathrm{\mu Gal}$ |
| from the two readings | $0.4245\ \mathrm{\mu Gal}$ |
| combined | $2.4689\ \mathrm{\mu Gal}$ ($0.0395\%$ of the difference) |

The calibration term is nearly six times the reading term. This is the general
pattern for relative gravimeters: **their repeatability is better than their scale
accuracy**, so a difference is more reliable over a short span (where
$\left(R_{2}-R_{1}\right)$ is small) than over a long one. A survey spanning the
whole range of the Earth's field inherits the full calibration error.

## 7. Precision is not accuracy

Two SYNTHETIC meters measuring a $5\ \mathrm{mGal}$ span:

| meter | systematic bias | random error | total | as a fraction of the signal |
|---|---|---|---|---|
| precise but mis-calibrated | $+5.000\ \mathrm{\mu Gal}$ | $0.283\ \mathrm{\mu Gal}$ | $5.008\ \mathrm{\mu Gal}$ | $0.1002\%$ |
| imprecise but unbiased | $0$ | $7.071\ \mathrm{\mu Gal}$ | $7.071\ \mathrm{\mu Gal}$ | $0.1414\%$ |

The first meter has a *smaller* total error yet a *larger* systematic one, and the
two are not interchangeable:

- **Precision** is repeatability: the spread of repeated measurements.
- **Accuracy** is closeness to the true value, which requires an independent
  reference to establish.

Averaging $n$ repeats reduces the random term by $\sqrt{n}$ and leaves the bias
untouched. If the bias is a fraction $\epsilon$ of the span, no amount of
averaging removes it, and the error on the *difference* scales with the difference
itself: short spans are safe, long spans are not. The only cure is an independent
check — an absolute station, a tie, or a known reference value — which is why
calibration loops and base ties appear in every gravity survey procedure
(module [02](../02-gravity-instruments-and-surveys/README.md), lesson 3).

## 8. How uncertainty grows away from the base

A network is tied to an absolute base through a chain of relative measurements. If
each link contributes an independent uncertainty $\sigma_{\ell}$, then after $N$
links the accumulated random uncertainty is $\sqrt{N}\,\sigma_{\ell}$, and the
total is

$$\sigma_{\text{total}}(N) = \sqrt{N\,\sigma_{\ell}^{2} +
\sigma_{\text{abs}}^{2}},$$

because the absolute datum's own uncertainty does not accumulate — it is
correlated across the whole network.

**Measured (SYNTHETIC).** With $\sigma_{\ell} = 8\ \mathrm{\mu Gal}$ and
$\sigma_{\text{abs}} = 5\ \mathrm{\mu Gal}$:

| links from base | $\sqrt{N}\sigma_{\ell}$ (µGal) | total (µGal) |
|---|---|---|
| 1 | 8.000 | 9.434 |
| 2 | 11.314 | 12.369 |
| 5 | 17.889 | 18.574 |
| 10 | 25.298 | 25.788 |
| 25 | 40.000 | 40.311 |
| 100 | 80.000 | 80.156 |

Two design consequences follow directly from the table:

- **It is the number of links that matters, not the distance travelled.** One long
  tie is better than a chain of short ones, because the chain adds variance at every
  step while a single tie adds it once.
- **A network is either datum-limited or survey-limited.** The two terms cross
  where $N\sigma_{\ell}^{2} = \sigma_{\text{abs}}^{2}$, i.e. at
  $N = \left(\sigma_{\text{abs}}/\sigma_{\ell}\right)^{2} = 0.39$ links for the
  numbers above — so here the survey term dominates from the very first link. With
  a quieter meter, $\sigma_{\ell} = 1\ \mathrm{µGal}$, the crossover moves to
  $N = 25$ links, and the same network would be datum-limited for its first
  25 links. Which regime you are in is a computation, not a matter of taste.
  Re-occupying the base during a survey, or adding a second absolute station, adds
  a correlated correction that resets the accumulation.

## 9. Assumptions and regime of validity

1. **Linearity.** The meter equation assumes the reading is proportional to gravity
   over the working range. Real instruments have small non-linearities, so a
   linear calibration is a model that must be checked with residuals, not assumed.
2. **Constant calibration within a survey.** Thermal, ageing and transport effects
   change $c$ and the zero point between and during surveys; those are handled as
   drift in module [02](../02-gravity-instruments-and-surveys/README.md), lesson 3.
3. **Independent errors.** The $\sqrt{N}$ rule assumes independent link errors; a
   shared calibration error is fully correlated and does not average down.
4. **Gaussian errors** for the stated uncertainties and for the least-squares
   standard errors. With few stations, the uncertainty of the uncertainty is large:
   the $s^{2}$ above has only 10 degrees of freedom.
5. **The datum is known, not assumed.** Quoting a network value to microgal
   precision while its datum is known to $5\ \mathrm{\mu Gal}$ is over-precision;
   the demonstration prints the datum uncertainty at every step for that reason.
6. **Units are part of the value.** A number without a unit, or with an unstated
   convention, is not a measurement. Mixing Gal with $\mathrm{m\,s^{-2}}$ is a
   factor of $10^{2}$; mixing mGal with $\mathrm{m\,s^{-2}}$ is $10^{5}$.
7. **Absolute does not mean exact.** An absolute measurement has its own
   uncertainty, typically a few microgal, and it is the *datum*, not the truth.

## 10. Python demonstration

`code/gravity_units_and_instruments_relative_demo.py` prints, with units:

1. the whole field and the interesting differences in every unit, with the
   ppb-scale statement $1\ \mathrm{mGal} = 1.018\times10^{-6}\,g$;
2. the equivalences $1\ \mathrm{mGal} \leftrightarrow 0.0817\ \mathrm{m}$ of
   $1000\ \mathrm{kg}$, $3.2438\ \mathrm{m}$ of elevation,
   $0.0238\ \mathrm{kg\,m^{-3}}$ through $1000\ \mathrm{m}$;
3. an absolute base at $979\,500.0000\ \mathrm{mGal}$ with $5\ \mathrm{\mu Gal}$, and
   a field station $6250$ counts away;
4. a 12-station least-squares calibration, slope and intercept with uncertainties
   and correlation $-0.9565$;
5. the error propagation into a $6.2541\ \mathrm{mGal}$ difference,
   $2.4689\ \mathrm{\mu Gal}$ total;
6. the precision-versus-accuracy experiment;
7. the network accumulation table.

Exercises and solutions:
[`exercises/05-gravity-units-and-instruments-relative-exercises.md`](exercises/05-gravity-units-and-instruments-relative-exercises.md),
[`exercises/05-gravity-units-and-instruments-relative-solutions.md`](exercises/05-gravity-units-and-instruments-relative-solutions.md).

## Mastery checkpoint

Answer without notes.

> A SYNTHETIC relative survey ties a field station to a base whose absolute value
> is $979\,500.0000\ \mathrm{mGal} \pm 5\ \mathrm{\mu Gal}$. The calibration is
> $c = 1.0000\times10^{-3}\ \mathrm{mGal\,count^{-1}}$ with a relative uncertainty
> of $0.040\%$, and the two readings are $12\,345.0$ and $18\,595.0$ counts, each
> repeatable to $0.3$ counts. **(a)** Compute the field station's value and the
> uncertainty of the difference. **(b)** State which term dominates and why.
> **(c)** The station is later found to be $3.2\ \mathrm{m}$ higher than assumed;
> compute the resulting error from the free-air term alone and compare it with (a).
> **(d)** State which of the three errors could be removed by repeating the
> measurement and which could not.

A worked version of (a)–(c) is in the
[solutions](exercises/05-gravity-units-and-instruments-relative-solutions.md).

## Common pitfalls

1. **Reporting counts as gravity.** A reading is not a value until a calibration
   converts it, and quoting the calibration is part of quoting the result.
2. **Quoting more digits than the datum supports.** A microgal-level number tied to
   a $5\ \mathrm{\mu Gal}$ datum inherits that uncertainty.
3. **Treating precision as accuracy.** Averaging repeats cannot remove a
   calibration bias, and the demonstration measures the two failure modes
   side by side.
4. **Calibrating over too narrow a range.** The $c$–$b$ correlation of $-0.9565$
   shows how a slope error hides in the intercept.
5. **Mixing units or ignoring the $h^{2}$ term.** $1\ \mathrm{mGal} = 3.2438\
   \mathrm{m}$ of elevation, so a metre of height error is a third of a milligal.
6. **Assuming a relative network's uncertainty is uniform.** It grows with the
   number of links from the datum.
7. **Forgetting that the free-air term needs the *ellipsoidal* height**, so a
   height-system error propagates into the gravity difference.

## Related modules

- [Module 01 — Gravity Fundamentals](README.md) — this module; lesson
  [01](01-newtonian-gravity.md) supplies the vertical gradient and lesson
  [04](04-gravity-reduction.md) consumes these uncertainties in a reduction.
- [Module 02 — Gravity Instruments and Surveys](../02-gravity-instruments-and-surveys/README.md) —
  the hardware, the free-fall principle and the drift and loop procedures.
- [02-01 Measurement and Physical Reasoning](../../02-physics/01-measurement-and-physical-reasoning/README.md) —
  uncertainty analysis in general.
- [05-02 Fields and Observables](../../05-core-geophysics/02-geophysical-fields-and-observables/README.md) —
  units, noise and drift for geophysical fields.
- [18-06 Uncertainty Quantification](../../18-inverse-problems/06-uncertainty-quantification/README.md) —
  where covariance and correlated errors are treated systematically.
