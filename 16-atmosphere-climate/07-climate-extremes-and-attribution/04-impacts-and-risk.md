---
id: 16-07-04
title: "Impacts, Vulnerability and Risk Assessment"
level: doctoral
prereqs: ["16-07-03", "16-07-01", "21-01-07"]
tags: [atmosphere, climate, risk, impacts, exposure, vulnerability, compound-events]
---

# Impacts, Vulnerability and Risk Assessment

> **All models and data in this module are SYNTHETIC.** The hazard distribution,
> damage function, exposure growth and monetary values in
> `code/impacts_and_risk_demo.py` are chosen teaching values in arbitrary monetary
> units (MU). No real asset value, loss, insurance figure, policy target or
> economic estimate is quoted anywhere in this lesson.

A climate impact is not a climate variable. It is the product of three
independent things: a **hazard** (how extreme the physical event is), an
**exposure** (what of value is in the way), and a **vulnerability** (how much
damage a given hazard does to what is exposed). The decomposition
$\text{risk} = f(\text{hazard}, \text{exposure}, \text{vulnerability})$ looks like
a slogan until it is made quantitative, at which point it becomes the most
useful bookkeeping in applied climate science — and the source of most of the
disagreements.

The reason is that the three factors behave differently. The hazard distribution
is a physical quantity that can be measured and modelled; exposure is largely an
economic and demographic quantity that changes for reasons unrelated to climate;
vulnerability is a design and adaptation quantity that is a *choice*. An observed
increase in damage therefore tells you very little on its own. This lesson builds
the arithmetic that separates the three, then shows the two places where the
separation fails: the components interact multiplicatively, and the attribution of
an *impact* carries strictly more uncertainty than the attribution of the hazard
that drove it.

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** risk as a function of hazard, exposure and vulnerability, and
   **write** expected annual damage as an integral over a hazard distribution.
2. **Compute** expected annual damage from a damage function and a lognormal
   hazard, and **state** the units of each factor.
3. **Decompose** a change in risk into hazard, exposure and vulnerability factors,
   and **identify** the interaction term that makes the decomposition
   order-dependent.
4. **Quantify** how a hazard shift changes the return period of a fixed design
   level, and **explain** why an unchanged asset can become under-designed.
5. **Compute** joint exceedance probabilities for compound events under
   independence and under correlation, and **state** why independence is a
   modelling assumption rather than a default.
6. **Propagate** input uncertainty to a damage estimate and **report** the result
   as a distribution rather than a point.
7. **Distinguish** attribution of a hazard from attribution of an impact, and
   **state** the additional uncertainty the latter carries.

## Prerequisites

- [16-07-03 Event Attribution Methodology and Its Limits](03-event-attribution.md) —
  the counterfactual machinery that an impact attribution inherits.
- [16-07-01 Extreme Events: Statistics and Physical Drivers](01-climate-extremes.md) —
  hazard distributions, return periods and tails.
- [21-01-07 Extreme Value Theory for Geohazards](../../21-statistics-bayesian-ml/01-statistics-in-practice/07-extreme-value-theory.md) —
  the tail models used for the hazard.

## 1. Risk as three factors, made quantitative

Let $h$ be a hazard intensity with annual distribution $f(h)$ (a flood depth in
metres, a wind speed, a heat index). Let $V$ be the value exposed, in monetary
units, and $d(h) \in [0,1]$ the **damage function** — the fraction of $V$ lost
when the hazard reaches intensity $h$. Then the **expected annual damage** is

$$\boxed{\;\mathrm{EAD} = V \int_0^{\infty} d(h)\,f(h)\,\mathrm{d}h
= V\,\mathbb{E}\left[d(h)\right].}$$

The three factors appear explicitly: $f$ is the hazard, $V$ is the exposure, and
$d$ is the vulnerability. EAD is in units of value per year.

Two properties of this definition matter later. First, EAD is an *expectation*: it
is the average of a loss over the hazard distribution, not the loss in a typical
year, and a single severe year can exceed it by orders of magnitude. Second, only
the product $V\,d(h)$ enters, so a change in exposure and an equal proportional
change in vulnerability are indistinguishable in EAD alone — a fact that becomes
important in Section 5.

## 2. Worked example — expected damage from a damage function

The demonstration uses a lognormal hazard (annual maximum flood depth) with
median $1.00\ \mathrm{m}$ and log-scale $\sigma = 0.40$, and a damage function

$$d(h) = \left[\operatorname{clip}\!\left(\frac{h-0.5}{3.0-0.5},\,0,\,1\right)\right]^{1.5},$$

so nothing is damaged below $h = 0.5\ \mathrm{m}$ and the damage saturates at
$h = 3.0\ \mathrm{m}$, with a convex ramp between. The exceedance probabilities
and damage fractions are:

| $h$ (m) | 0.5 | 1.0 | 1.5 | 2.0 | 2.5 | 3.0 | 4.0 |
|---|---|---|---|---|---|---|---|
| $d(h)$ | 0.00 | 0.09 | 0.25 | 0.46 | 0.72 | 1.00 | 1.00 |
| $\Pr(h \ge h')$ per year | 0.9584 | 0.5000 | 0.1554 | 0.0416 | 0.0110 | 0.0030 | 0.0003 |

Integrating the product (by Gauss–Hermite quadrature, exactly for this model),
the expected fractional damage is $\mathbb{E}[d] = 0.1362$, so with exposure
$V = 1000\ \mathrm{MU}$ the expected annual damage is

$$\mathrm{EAD}_0 = 1000 \times 0.1362 = 136.2\ \mathrm{MU\,yr^{-1}}.$$

Note the shape of the problem: the median year ($h = 1.0\ \mathrm{m}$) damages
only $9\%$, and the expectation is dominated by the rare deep floods. EAD is a
tail integral wearing the clothes of an average.

## 3. Decomposing a change in risk

Now change all three factors, one at a time, and measure the effect on EAD. The
demonstration uses a $+15\%$ shift of the hazard median, a $2\%\ \mathrm{yr^{-1}}$
exposure growth over $30$ years, and an adaptation that raises the damage
threshold from $0.5$ to $0.7\ \mathrm{m}$:

| Scenario | EAD (MU yr⁻¹) | factor vs baseline |
|---|---|---|
| S0 baseline | 136.2 | 1.000× |
| S1 hazard shift only | 188.7 | 1.386× |
| S2 + exposure growth | 341.9 | 2.510× |
| S3 + adaptation ($h_0 \to 0.7$ m) | 273.6 | 2.009× |

The multiplicative identity holds exactly here:

$$\underbrace{1.386}_{\text{hazard}} \times \underbrace{1.811}_{\text{exposure}}
= 2.510 = \frac{S_2}{S_0}, \qquad
\text{adaptation factor} = \frac{S_3}{S_2} = 0.800.$$

Exposure growth $(1.02)^{30} = 1.811$ is *larger* than the hazard factor. In this
synthetic example most of the increase in expected damage comes from putting more
value in harm's way, not from the hazard change — a result that is frequently
overlooked when an observed loss increase is attributed to climate alone.

**The decomposition is a choice, not a property.** It is exact above because each
factor was applied in turn and the hazard shift was independent of the damage
threshold. If the hazard shift were larger exactly where the damage function is
steepest, or if adaptation changed the exposure (raising the threshold costs
money that would otherwise be assets), the product would no longer separate the
factors. The residual is a genuine **interaction term**, and a report that
presents a three-way decomposition without stating the order of application and
the assumed independence is presenting a choice as a measurement.

## 4. Design events, and why an unchanged asset becomes under-designed

Engineering design is stated as a return period: "protected to the 1-in-50
flood". In the baseline hazard the 1-in-50 depth is

$$h_{50} = \exp\!\left(\ln 1.0 + 0.40\,z_{0.98}\right) = 2.274\ \mathrm{m},$$

where $z_{0.98}$ is the standard normal 98th percentile. After a $\times 1.15$
shift of the hazard median, the annual probability of exceeding that same level is

$$\Pr\!\left(h \ge 2.274\right) = 0.0442\ \mathrm{yr^{-1}},
\qquad \text{new return period} = \frac{1}{0.0442} = 22.6\ \mathrm{yr},$$

a frequency ratio of $2.21$ — the design level is exceeded about $2.2$ times as
often. Nothing about the asset changed. **The asset is now under-designed
relative to the hazard it faces**, and the under-design is a statement about the
hazard distribution, not about the structure. This is the mechanism by which a
modest change in a distribution becomes a large change in risk: the design point
sits in the tail, where a shift of the median is amplified.

## 5. Compound events and dependence

Many impacts require more than one driver to exceed a threshold simultaneously: a
storm surge plus river flooding, a heatwave plus humidity, a drought plus fire
weather. Let $A$ and $B$ be two threshold exceedance events. Then

$$\Pr(A \cup B) = \Pr(A) + \Pr(B) - \Pr(A \cap B),$$

and the joint probability $\Pr(A \cap B)$ is where the dependence lives. The
demonstration models two lognormal drivers — a river discharge and a storm surge —
in the Gaussian copula sense, with marginal exceedance probabilities $0.0238$ and
$0.0181$:

| $\rho$ | $\Pr(A\cap B)$ | $\Pr(A\cup B)$ | $\Pr(A\cap B)/\Pr(A\cup B)$ |
|---|---|---|---|
| 0.0 | 0.0004 | 0.0415 | 0.0104 |
| 0.3 | 0.0018 | 0.0401 | 0.0439 |
| 0.6 | 0.0049 | 0.0370 | 0.1311 |
| 0.9 | 0.0119 | 0.0300 | 0.3988 |

At independence the joint probability is $0.0238 \times 0.0181 = 0.0004$; at
$\rho = 0.9$ it is $0.0119$, **$30$ times larger**. Yet the union probability
*falls* with correlation ($0.0415 \to 0.0300$), because correlated drivers
concentrate both exceedances into the same years and reduce the chance of "one or
the other". So dependence does not simply make compound risk worse: it moves
probability from the union to the intersection. Which of those matters depends
on whether the impact is triggered by both drivers (a compound flood) or by
either (a general inundation).

The demonstration then shifts the surge marginal by a sea-level rise of
$0.30\ \mathrm{m}$, holding the dependence at $\rho = 0.6$: the effective surge
threshold falls from $1.5$ to $1.2\ \mathrm{m}$, and the joint exceedance
probability rises from $0.0049$ to $0.0126$, a factor $2.59$. **A change in the
hazard marginal and a change in the dependence produce different signatures, and
separating them is part of the analysis** (see
[16-09-05 Climate–Geohazard Interactions](../09-geophysics-and-climate/05-climate-geohazards.md)).

## 6. Uncertainty propagation

Every factor in $\mathrm{EAD} = V\,\mathbb{E}[d]$ is uncertain. The demonstration
draws $20000$ Monte Carlo samples with the hazard shift uniform on $[1.00,1.30]$,
exposure growth uniform on $[0,4]\%\ \mathrm{yr^{-1}}$ and the damage threshold
uniform on $[0.5,0.8]\ \mathrm{m}$, and reports quantiles of the resulting EAD:

| quantile | 5% | 25% | median | 75% | 95% |
|---|---|---|---|---|---|
| EAD (MU yr⁻¹) | 146 | 211 | 286 | 388 | 554 |

The 5–95 range spans a factor $3.80$. A single EAD value would be one draw from
this distribution; the *distribution* is the result. The practical rule is the
same one the whole module has been building: state the inputs, their distributions
and their correlations, and report the range. Two analysts who choose different
input ranges are not disagreeing about the physics; they are making different
modelling choices, and the report should make that visible.

## 7. Attributing an impact is harder than attributing a hazard

It is tempting to chain the two: if warming increased the hazard probability by
$\mathrm{FAR}_h$, then the impact increased by the same amount. This is wrong for
three reasons.

1. **The damage function is nonlinear.** Average damage is
   $\mathbb{E}[d(h)]$, and a nonlinear $d$ means the impact response to a hazard
   shift is not the hazard response. The convex ramp used above amplifies changes
   in the deep tail and suppresses changes near the threshold.
2. **Exposure and vulnerability change for non-climatic reasons.** Growth,
   construction standards, land use and adaptation all move $V$ and $d$ on the
   same timescale as the hazard, and the decomposition in Section 3 shows they can
   dominate.
3. **The counterfactual multiplies.** An impact attribution needs a counterfactual
   for the hazard *and* a counterfactual for exposure and vulnerability — the
   latter rarely available and usually assumed. The honest statement is
   conditional: *"under the observed exposure and vulnerability trajectory, the
   modelled change in the hazard distribution increases expected annual damage by
   a factor of ...; the exposure contribution over the same period is ..."*

## 8. Assumptions and regime of validity

1. **The hazard distribution is stationary over the analysis window** unless a
   non-stationary form is fitted, as in
   [16-07-01](01-climate-extremes.md). A trend in the hazard makes EAD
   time-dependent, not a single number.
2. **The damage function is known and convex/concave in a specified way.** Real
   damage functions are empirically uncertain and often piecewise (thresholds,
   saturation); the choice changes the answer's sensitivity to the tail.
3. **Damage is a deterministic function of hazard intensity.** In reality damage
   is itself random (warning time, maintenance, simultaneity with other events);
   treating it as a function understates the spread.
4. **Exposure is countable and homogeneous.** Aggregating heterogeneous assets at
   one intensity is an approximation that can hide strong spatial correlation.
5. **Independence or a stated copula for compound drivers.** Independence is an
   assumption with a large effect, as Section 5 measures.
6. **The monetary unit is a linear measure of value.** Losses are not additive in
   utility; economic and equity considerations are outside this model entirely.

## 9. Reporting a risk assessment

A defensible risk statement names:

1. the **hazard variable**, its distribution and its **trend assumption**;
2. the **exposure**: what is counted, in what units, and how it is projected;
3. the **vulnerability**: the damage function, its thresholds and its source;
4. the **compound structure**: which drivers, and the assumed dependence;
5. the **uncertainty propagation**: input distributions and the resulting range;
6. the **separation** of hazard, exposure and vulnerability contributions,
   including the interaction term and the order of decomposition;
7. a label on each number: **measured**, **modelled** or **chosen**.

## 10. Python demonstration

[`code/impacts_and_risk_demo.py`](code/impacts_and_risk_demo.py) performs the
whole calculation and prints labelled results with units. It:

1. integrates a damage function over a lognormal hazard and reports the expected
   fractional damage and EAD;
2. decomposes a change in EAD into hazard, exposure and vulnerability factors and
   verifies the multiplicative identity;
3. computes the change in return period of a fixed design level under a hazard
   shift;
4. computes joint and union exceedance probabilities for a compound flood under
   four correlations, and the effect of a sea-level shift of the surge marginal;
5. propagates input uncertainty by Monte Carlo and reports quantiles.

Every number in this lesson is printed by that demonstration.

## Mastery checkpoint

> The demonstration's synthetic model has $\mathbb{E}[d] = 0.1362$, exposure
> $1000\ \mathrm{MU}$, a hazard median shift of $\times 1.15$, exposure growth of
> $2\%\ \mathrm{yr^{-1}}$ over $30$ years, and adaptation raising the damage
> threshold from $0.5$ to $0.7\ \mathrm{m}$.
>
> **(a)** Compute EAD for the baseline and state its units.
> **(b)** Verify the multiplicative identity $1.386 \times 1.811 = 2.510$ and
> explain what physical assumption it rests on.
> **(c)** An observed loss increase is ascribed wholly to climate change. Using
> the decomposition, give two alternative explanations with their measured
> factors.
> **(d)** The 1-in-50 depth is $2.274\ \mathrm{m}$. After the hazard shift its
> return period is $22.6$ years. Explain in one sentence why a small change in the
> median produces a large change in risk.
> **(e)** Two compound drivers each have exceedance probability about $0.02$.
> Give the joint probability at independence and at $\rho = 0.6$, and state which
> assumption you would report.

## Common pitfalls

1. **Attributing a loss increase to climate alone.** Exposure growth of $1.811\times$
   exceeded the hazard factor of $1.386\times$ in the demonstration.
2. **Treating the three-way decomposition as exact.** It is exact only under a
   stated order and independence; the interaction term is real.
3. **Reporting one EAD number.** The 5–95 range spanned a factor $3.80$ in the
   demonstration; the distribution is the result.
4. **Assuming independence for compound drivers.** At $\rho = 0.9$ the joint
   probability was $30$ times the independent value.
5. **Confusing the union with the intersection.** Positive dependence lowers
   $\Pr(A\cup B)$ while raising $\Pr(A\cap B)$.
6. **Chaining hazard attribution into impact attribution.** The damage function is
   nonlinear and exposure/vulnerability have their own trajectories.
7. **Quoting a design return period as a property of the asset.** It is a property
   of the hazard distribution at the time of design.

## Related modules

- [16-07-01 Extreme Events: Statistics and Physical Drivers](01-climate-extremes.md) —
  where the hazard distribution comes from.
- [16-07-03 Event Attribution Methodology and Its Limits](03-event-attribution.md) —
  the counterfactual that an impact attribution inherits and extends.
- [16-09-05 Climate–Geohazard Interactions (Sea Level, Permafrost, Slopes)](../09-geophysics-and-climate/05-climate-geohazards.md) —
  the physical mechanisms behind compound coastal and slope hazards.
- [16-08-04 Analysing Climate Data in Python: xarray and CDO](../08-climate-observation-and-data/04-climate-data-analysis-python.md) —
  the data-handling practice the hazard estimates rest on.
- [06-11 Earthquake Statistics and Hazard](../../06-seismology/11-earthquake-statistics-and-hazard/README.md) —
  the hazard-curve and exceedance logic in a fully developed form.
- [11-01 The Exploration Workflow](../../11-exploration-geophysics/01-exploration-workflow/README.md) —
  a parallel treatment of decision-making under uncertainty, including the value
  of information.

## Self-assessment checklist

- [ ] I can write EAD as an integral and state the units.
- [ ] I can decompose a risk change and identify the interaction term.
- [ ] I can compute a design-level return period under a hazard shift.
- [ ] I can compute joint and union exceedance probabilities and explain the
      effect of correlation.
- [ ] I can propagate input uncertainty and report quantiles.
- [ ] I can state why impact attribution is harder than hazard attribution.
