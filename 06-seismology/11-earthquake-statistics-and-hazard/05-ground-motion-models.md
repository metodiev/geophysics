---
id: 06-11-05
title: "Ground-Motion Prediction Equations and Their Uncertainty"
level: doctoral
prereqs: ["06-11-01", "06-11-04", "06-05-01"]
tags: [seismology, hazard, ground-motion, gmpe, lognormal, uncertainty, residuals]
---

# Ground-Motion Prediction Equations and Their Uncertainty

> **All models and data in this module are SYNTHETIC.** The relation, its
> coefficients and its scatter components are teaching values chosen for
> arithmetic transparency. They are not fitted to any strong-motion dataset and
> no published coefficient is quoted.

## Learning objectives

By the end of this lesson you will be able to:

1. **Write** a ground-motion prediction equation (GMPE) as a median function plus
   a lognormal residual, and **state** what each coefficient does physically.
2. **Decompose** the total scatter into a within-event and a between-event
   component, and **derive** $\sigma^2 = \sigma_\varepsilon^2 + \tau^2$ from the
   law of total variance.
3. **Measure** the two components from a synthetic dataset by comparing the
   scatter of event means with the scatter of records inside an event.
4. **Derive** the lognormal identities $\mathrm{mean}/\mathrm{median}
   = e^{\sigma^2/2}$ and
   $P(IM > z) = 1 - \Phi[\ln(z/\hat z)/\sigma]$, and **distinguish** the mean from
   the value used in hazard.
5. **Quantify** how the scatter enters a hazard calculation, and **prove** that
   increasing $\sigma$ raises the exceedance probability above the median.
6. **Separate** aleatory scatter from epistemic uncertainty of the median, and
   **derive** why more records sharpen the median as $\sigma/\sqrt n$ while
   leaving the scatter unchanged.
7. **Demonstrate**, on the same data, that two relations can be indistinguishable
   inside their fitted range and differ by a factor of 1.7 outside it, and
   **identify** a misspecified functional form from residual structure.

## Prerequisites

- [06-11-01 Gutenberg-Richter, b-Value and Magnitude of Completeness](01-gutenberg-richter.md) —
  the magnitudes that drive the relation.
- [06-11-04 Probabilistic Seismic Hazard Analysis (PSHA) and Its Logic](04-psha.md) —
  where the conditional exceedance probability is consumed.
- [06-05-01 Measuring Q: Spectral Ratio, Rise Time, Multiple Methods](../05-attenuation-and-anelasticity/01-attenuation-measurement.md) —
  the physical attenuation the distance term approximates.

## 1. What a GMPE is, and what it is not

A ground-motion prediction equation is an empirical regression of an intensity
measure (PGA, PGV, spectral acceleration at a period) on source, path and site
variables. In its minimal form:

$$\ln IM \sim \mathcal N\big(\ln \hat z(M,R),\ \sigma^2\big),
\qquad
\ln \hat z(M,R) = c_0 + c_1\,(M - 6) - c_2 \ln(R + R_0) + \text{site terms}.$$

Four properties define its use and its limits:

1. **It predicts a distribution, not a number.** The quantity with physical
   meaning in hazard is the pair $(\hat z, \sigma)$, and hazard is dominated by the
   second at large amplitudes (Section 5).
2. **It is a fit within a stated magnitude–distance–period range.** Outside that
   range it is an extrapolation, and Section 7 shows how large the resulting
   ambiguity is.
3. **The residual is not error.** The scatter is real physical variability — path,
   directivity, site and source effects not represented by the model's variables.
   Removing it is not a matter of better instruments.
4. **The variables are proxies.** $R$ stands for the whole path effect, $M$ for the
   whole source effect. Calling the coefficient $c_1$ "the magnitude scaling" is a
   shorthand, not a mechanism. For the mechanism, see
   [06-03 Earthquake Sources](../03-earthquake-sources/README.md) and
   [06-05 Attenuation and Anelasticity](../05-attenuation-and-anelasticity/README.md).

The synthetic relation used in this module is
$\ln \hat z = 1.411 + 1.00(M-6) - 1.30\ln(R+5)$ with
$\sigma_\text{total} = 0.600$. It gives median PGA of $0.0446\ \mathrm{g}$ for
$M5.0$ at $10\ \mathrm{km}$, $0.3297\ \mathrm{g}$ for $M7.0$ at $10\ \mathrm{km}$
and $0.0263\ \mathrm{g}$ for $M7.0$ at $100\ \mathrm{km}$. One magnitude unit
multiplies the median by $\exp(1.00) = 2.718$; a factor
$\exp(1.30) = 3.669$ in $(R + R_0)$ divides it by the same factor. These are the
numbers to carry in your head when reading a hazard curve.

## 2. Decomposing the scatter

The residual in $\ln IM$ separates into a part common to all records of one event
(an *event term* $\eta$, driven by stress drop, directivity, path average) and a
part that varies record to record within an event (a *within-event* term
$\varepsilon$):

$$\ln IM_{ij} = \ln \hat z(M_i, R_{ij}) + \eta_i + \varepsilon_{ij},
\qquad \eta_i \sim \mathcal N(0, \tau^2), \quad
\varepsilon_{ij} \sim \mathcal N(0, \sigma_\varepsilon^2).$$

Because $\eta$ and $\varepsilon$ are independent, the law of total variance gives

$$\mathrm{Var}(\ln IM) = \underbrace{\mathrm{Var}\big(\mathbb E[\ln IM \mid i]\big)}
_{\tau^2} + \underbrace{\mathbb E\big[\mathrm{Var}(\ln IM \mid i)\big]}
_{\sigma_\varepsilon^2}
\quad\Longrightarrow\quad
\boxed{\ \sigma^2 = \sigma_\varepsilon^2 + \tau^2\ }$$

The demonstration uses $\sigma_\varepsilon = 0.500$ and
$\tau = \sqrt{0.600^2 - 0.500^2} = 0.332$, so that
$\sigma = \sqrt{0.25 + 0.110} = 0.600$ by construction, and then measures the
components back out of a synthetic dataset of 200 events with 20 records each:

| quantity | input | measured |
|---|---|---|
| total s.d. of $\ln PGA$ | 0.600 | 0.596 |
| s.d. of event means ($\tau$) | 0.332 | 0.346 |
| s.d. within events ($\sigma_\varepsilon$) | 0.500 | 0.486 |

### Why the decomposition matters

A single record and the median of a population are different questions. If a
model has an event term, the *median shaking of the next event* at a site is
uncertain only by $\tau$ — the record-to-record $\sigma_\varepsilon$ has already
averaged out. Conversely, the shaking experienced in one event is uncertain by the
full $\sigma$. Hazard calculations are usually written in terms of $\sigma$, but
conditional or scenario analyses often need $\tau$ separately, and confusing the
two changes the answer by tens of per cent.

### Worked example 1 — separating the components from a table

Suppose a dataset reports $\sigma_\text{total} = 0.62$ and $\tau = 0.40$. Then

$$\sigma_\varepsilon = \sqrt{0.62^2 - 0.40^2} = \sqrt{0.3844 - 0.1600}
= \sqrt{0.2244} = 0.474.$$

The within-event scatter is 0.47, smaller than the total: a single record is less
uncertain than the difference between events of the same magnitude and distance.

## 3. The lognormal, used correctly

With $\ln IM \sim \mathcal N(\ln \hat z, \sigma^2)$:

$$\mathrm{mean}(IM) = \hat z\,e^{\sigma^2/2}, \qquad
\mathrm{median}(IM) = \hat z, \qquad
P(IM > z) = 1 - \Phi\!\left(\frac{\ln z - \ln \hat z}{\sigma}\right).$$

The demonstration's scenario is $M6.5$ at $15\ \mathrm{km}$, where
$\hat z = 0.1376\ \mathrm{g}$. Then

$$\frac{\mathrm{mean}}{\mathrm{median}} = e^{0.6^2/2} = e^{0.18} = 1.1972,
\qquad \mathrm{mean} = 0.1647\ \mathrm{g},$$

i.e. the mean is 19.7% above the median. The closed-form exceedance probabilities
at this scenario are

| $z$ (g) | $P(PGA > z)$ | event return level |
|---|---|---|
| 0.2 | 0.2665 | 1 in 4 |
| 0.4 | 0.0377 | 1 in 27 |
| 0.6 | 0.0071 | 1 in 142 |

A useful discipline: **hazard integrates the tail, so the mean is rarely the
quantity you want.** A design value taken from the mean of the distribution would
be exceeded roughly half the time.

### Worked example 2 — the event-term effect on a tail probability

The demonstration measures the frequency of exceeding $0.4\ \mathrm{g}$ at the
scenario as $0.0275$, against the closed-form $0.0377$. The reason is printed
alongside: the 200 randomly drawn event terms averaged $-0.0328$ in $\ln PGA$
against an expected standard error of $0.0235$. Because the exceedance probability
depends exponentially on the median, that 0.033 shift moves the frequency by about
$-27\%$.

This is not a numerical failure; it is the epistemic uncertainty of the median
appearing *inside* an aleatory statistic. With 200 events the median of the
population is known to about $\pm0.024$ in $\ln IM$, and hazard is sensitive to it.

## 4. What more data can and cannot fix

The scatter of an estimate of the median from $n$ records is

$$\mathrm{s.e.}(\widehat{\ln\hat z}) = \frac{\sigma}{\sqrt n},$$

because the mean of $n$ independent normal variables has variance $\sigma^2/n$.
The demonstration verifies it by repeating the estimate 4000 times:

| $n$ records | measured s.d. of the estimate | $\sigma/\sqrt n$ |
|---|---|---|
| 5 | 0.2670 | 0.2683 |
| 20 | 0.1348 | 0.1342 |
| 100 | 0.0600 | 0.0600 |

Two things follow, and they must not be confused:

- **Epistemic**: more records pin down the median. A densely recorded earthquake
  reduces the uncertainty of *the model*, and thus of the hazard curve.
- **Aleatory**: no number of records reduces $\sigma$. A densely recorded
  earthquake says nothing about the ground motion of the next one.

The classic error is to treat a well-recorded sequence as evidence that the next
event's shaking is predictable.

## 5. Why $\sigma$ raises the hazard

Differentiate the tail probability with respect to $\sigma$ at fixed threshold,
writing $d = \ln(z/\hat z) > 0$ (the threshold above the median):

$$\frac{\partial}{\partial\sigma}\left[1 - \Phi\!\left(\frac{d}{\sigma}\right)\right]
= \varphi\!\left(\frac{d}{\sigma}\right)\frac{d}{\sigma^2} > 0,$$

where $\varphi$ is the standard normal density. The probability of exceeding any
level above the median increases with the scatter — the tail is fed by variability,
not by the median.

Numerically, for a threshold of twice the median:

$$P(IM > 2\hat z) = 1 - \Phi\!\left(\frac{\ln 2}{0.3}\right) = 0.0104
\quad\text{at}\ \sigma = 0.30,$$
$$P(IM > 2\hat z) = 1 - \Phi\!\left(\frac{\ln 2}{0.6}\right) = 0.1240
\quad\text{at}\ \sigma = 0.60.$$

Doubling $\sigma$ multiplies the rate of exceedance of twice the median by about
12. In the hazard integration of [lesson 04](04-psha.md) the same effect appears
as a factor of $8.7$ in the rate at $0.4\ \mathrm{g}$ between $\sigma = 0.30$ and
$\sigma = 0.90$. A model that understates $\sigma$ will understate the hazard, and
it will look *better* by every residual-based goodness-of-fit measure because its
predictions are tighter.

## 6. Aleatory and epistemic uncertainty, named

| kind | example | reducible by data? | enters hazard how |
|---|---|---|---|
| aleatory | record-to-record $\sigma_\varepsilon$, event-to-event $\tau$ | no | directly, through the lognormal tail |
| epistemic, parameter | coefficients $c_i$, $\sigma$ itself | yes | through a logic tree over fits |
| epistemic, model | functional form, magnitude scaling, saturation | partly, inside the data range only | largest at the edges of the range |
| epistemic, choice | which GMPE, which site term, which source model | no, by argument only | the dominant spread in practice |

The last row is the one that matters most in engineering practice: different
published relations, all calibrated on real data, can differ by a factor of two in
median amplitude at a given $(M, R)$. The remainder of this lesson is about
*proving* that the data cannot always arbitrate between them.

## 7. Extrapolation: two fits, same data, different worlds

The demonstration fits two standard magnitude scalings to the same seven synthetic
data points between $M4.5$ and $M6.0$ at 20 km with $\ln$-scatter 0.02:

| model | form | in-range RMS |
|---|---|---|
| A | $\ln PGA = 1.0091\,m - 8.8194$ | 0.0157 |
| B | $\ln PGA = 5.2615\ln m - 12.2224$ | 0.0242 |

Inside the data range the two models differ by at most $0.0302$ in $\ln PGA$ — a
factor of $1.031$, *comparable to the observational scatter*. At $M8.0$, 20 km
they predict

$$0.4739\ \mathrm{g} \quad\text{(A)}\qquad\text{versus}\qquad
0.2776\ \mathrm{g} \quad\text{(B)},$$

a ratio of $1.71$. The data cannot choose between them; the choice is made by
physics, by analogy with other regions, or by expert judgement, and it is an
epistemic uncertainty that no additional in-range data can remove.
**This is the single most important sentence in this lesson**, and it is why
hazard studies carry logic trees over GMPEs rather than a single best fit.

## 8. Residual diagnostics: what the data *can* decide

Extrapolation ambiguity does not mean the data are powerless. Structure in the
residuals betrays a wrong functional form. The demonstration fits a synthetic
$(M,r)$ grid twice: once with a magnitude term only, once with a free distance
coefficient.

| model | RMS residual | corr(residual, $\ln r$) |
|---|---|---|
| magnitude only | 0.9824 | $-0.999$ |
| magnitude + free distance term | 0.0499 | $0.000$ |

The fitted distance coefficient is $-1.297$ against a true value of $-1.30$. So
the data can (i) reject a missing distance term by a factor of 20 in RMS and a
correlation of $-0.999$, and (ii) recover the distance exponent to 0.2%. What they
cannot do is decide between two forms that agree inside their range.

The practical rule:

> **Inside the range, the residuals veto wrong forms. Outside the range, only
> assumptions speak.**

## 9. Assumptions and regime of validity

1. **Lognormal residual.** Convenient but not sacred; the upper tail of PGA is
   sometimes heavier, and the assumption matters most exactly where hazard is
   evaluated.
2. **Constant $\sigma$.** Real relations have magnitude-dependent $\sigma$
   (typically larger at small magnitude). Treating it as constant biases the tails
   of the hazard contribution from small events.
3. **Ergodicity.** Within-event variability from one event is treated as the
   variability of an arbitrary event at the site. For a site with strong,
   unmodelled 3D structure this fails silently.
4. **Independence of residuals.** In practice residuals are correlated between
   nearby periods and nearby sites, which matters for multi-period and multi-site
   products.
5. **The variables used are the variables needed.** If the site's $V_{S30}$ is
   outside the calibration range, or the source geometry is mismatched, the model
   is being extrapolated in a way no residual test will reveal.
6. **Calibration range.** The relation is defined on a stated magnitude, distance,
   depth, style-of-faulting and period range. Every use outside it is an
   extrapolation of the kind quantified in Section 7.
7. **A single intensity measure.** Spectral acceleration at one period is one
   number; structural response depends on the spectrum. Extending the machinery
   from PGA to a spectrum is mechanical, but each period carries its own $\sigma$
   and its own extrapolation range.

## 10. Python demonstration

[`code/ground_motion_models_demo.py`](./code/ground_motion_models_demo.py)
evaluates the median relation, measures the scatter decomposition, verifies the
lognormal identities, demonstrates aleatory versus epistemic uncertainty,
constructs the two extrapolating fits and diagnoses the missing distance term.

```bash
cd 06-seismology/11-earthquake-statistics-and-hazard/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python ground_motion_models_demo.py
```

It prints labelled results with units and exits 0. Every number in this lesson is
one of its outputs.

## Mastery checkpoint

Use $\ln \hat z = 1.411 + 1.00(M-6) - 1.30\ln(R+5)$ with $\sigma = 0.60$.

**(a)** Compute the median PGA for $M6.5$ at $25\ \mathrm{km}$, and the probability
that the PGA exceeds $0.3\ \mathrm{g}$ in one record of such an event.
**(b)** A dataset has $\sigma_\text{total} = 0.58$ and $\sigma_\varepsilon = 0.45$.
Compute $\tau$ and state which component a scenario analysis of the *median* of
the next event should use.
**(c)** Compute the mean PGA for (a) and state why it is not the design value.
**(d)** Using the derivation in Section 5, compute the factor by which
$P(IM > 1.5\hat z)$ increases when $\sigma$ rises from 0.4 to 0.7.
**(e)** Two relations fit the same $M4.5$–$M6.0$ data with RMS 0.02 and predict
$0.48\ \mathrm{g}$ and $0.28\ \mathrm{g}$ at $M8$. State what would have to be true
for the data to arbitrate, and what you would report instead.

## Common pitfalls

1. **Quoting a median without $\sigma$.** The distribution is the model.
2. **Using the mean as the design value.** The mean is 1.1972× the median at
   $\sigma = 0.6$, and hazard lives in the tail beyond both.
3. **Reporting $\sigma$ without the decomposition.** Scenario and hazard analyses
   need different components.
4. **Treating the residual as measurement error.** It is physical variability.
5. **Extrapolating without declaring it.** A factor of 1.7 in median amplitude at
   $M8$ from two equally well-fitting forms is the demonstration's central result.
6. **Fitting $\sigma$ on the same data used to select the model.** The apparent
   scatter shrinks and the hazard follows it down.
7. **Assuming a smaller $\sigma$ means a better model.** It means a tighter
   distribution; whether it is right is a separate question, and Section 5 shows
   the hazard consequence of getting it wrong.

## Related modules

- [06-11-04 Probabilistic Seismic Hazard Analysis (PSHA) and Its Logic](04-psha.md) —
  the consumer of this conditional distribution.
- [06-11-06 Hazard Maps, Site Amplification and Design Codes](06-hazard-mapping.md) —
  the site term this lesson leaves out.
- [06-05 Attenuation and Anelasticity](../05-attenuation-and-anelasticity/README.md) —
  the physics behind the distance term.
- [06-03 Earthquake Sources](../03-earthquake-sources/README.md) —
  the physics behind the magnitude term.
- [21-01 Statistics in Geophysical Practice](../../21-statistics-bayesian-ml/01-statistics-in-practice/README.md) —
  regression, heteroscedasticity and model selection.
- [18-06 Uncertainty Quantification](../../18-inverse-problems/06-uncertainty-quantification/README.md) —
  aleatory versus epistemic, formally.

## Exercises

Full problem sets and worked solutions:
[`exercises/05-ground-motion-models-exercises.md`](./exercises/05-ground-motion-models-exercises.md)
and
[`exercises/05-ground-motion-models-solutions.md`](./exercises/05-ground-motion-models-solutions.md).
