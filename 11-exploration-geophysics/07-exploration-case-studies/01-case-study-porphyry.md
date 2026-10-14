---
id: 11-07-01
title: "Case Study: Porphyry Copper District"
level: research
prereqs: ["11-01-03", "11-02-01", "11-02-07"]
tags: [exploration-geophysics, case-studies, porphyry, prospectivity, bayes, value-of-information]
---

# Case Study: Porphyry Copper District

## A statement of what this lesson does and does not assert

This lesson is about **how a district-scale targeting argument is structured and
how it fails**. It deliberately quotes **no site-specific numbers** — no grade,
tonnage, depth, anomaly amplitude or discovery rate for any named deposit or
district. That is not an oversight. Every such number comes from a specific
company report, a specific assay protocol and a specific cut-off, and repeating
one from memory would be exactly the failure this curriculum forbids.

Consequently:

- Porphyry systems are described here as an **argument archetype**: a class of
  target with a characteristic alteration geometry, a characteristic set of
  geophysical signatures, and a characteristic set of false positives.
- If a real belt or deposit is named, the naming is illustrative and **no
  factual claim and no site-specific number is made about it**.
- All quantitative content comes from
  `code/case_study_porphyry_demo.py`, whose inputs are **stated SYNTHETIC
  models**.
- To attach real numbers to a real district you must retrieve the primary
  literature and the operator's technical reports yourself.

Writing this lesson any other way would mean presenting remembered constants as
fact, which is worse than writing a shorter lesson.

## Learning objectives

By the end of this lesson you will be able to:

1. **Decompose** a district targeting argument into target, evidence, claimed
   link and alternatives, and say which part each geophysical data set addresses.
2. **Compute** the positive predictive value of a single indicator from a base
   rate and a likelihood ratio, and **interpret** it as a drill count.
3. **Demonstrate** how treating correlated indicators as independent overstates
   the posterior, and **quantify** the bias with the number of indicators.
4. **Derive** the depth estimated from a magnetic profile and **quantify** the
   error made by assuming the wrong source shape.
5. **Compute** the break-even probability of a drillhole from its cost and the
   value of a discovery, and **state** which priors justify which decisions.
6. **Write** a targeting statement that separates measurement, model and
   interpretation.

## Prerequisites

- [11-01-03 Cost, Risk and Value of Information in Exploration](../01-exploration-workflow/03-cost-benefit.md)
  — the decision framework this lesson applies.
- [11-02-01 Geophysical Signatures of Major Deposit Types](../02-mineral-exploration/01-deposit-signatures.md)
  — the signatures used as evidence here.
- [11-02-07 Multi-Method Targeting and Prospectivity Analysis](../02-mineral-exploration/07-multi-method-targeting.md)
  — the method combination whose independence is questioned below.
- [18-05 Bayesian Inversion and Inference](../../18-inverse-problems/05-bayesian-inversion/01-bayes-inverse-formulation.md)
  — the probability calculus in full.

> All models and data in this module are **SYNTHETIC**. No real deposit, district,
> company or hole is used.

## 1. Intuition: every district case study is the same argument

Strip away the geography and every porphyry targeting case study says four
things:

1. **Target.** What is being sought, in what geological setting, at what depth
   range and scale.
2. **Evidence.** The geophysical, geochemical and geological observations, with
   their uncertainties.
3. **Claimed link.** Why the evidence implies the target: an alteration
   zonation, a magnetite association, a conductivity contrast.
4. **Alternatives.** Why the evidence is not something else — the same evidence
   from a barren intrusion, a different sulphide, or a lithological change.

Steps 3 and 4 are where cases differ and where they succeed or fail. Every
geophysical indicator for a porphyry target is a **proxy** for a geological
process, and every proxy has a false-positive population. The district question
is not "is there an anomaly?" but "given this anomaly, and everything else known
about the belt, what is the probability that drilling pays?"

## 2. Precise definitions

### 2.1 Prospectivity and the base rate

- **Base rate (prior) $p$**: the fraction of drilled targets of the type in
  question that prove economic. This is a property of the belt and the economic
  environment, not of the geophysics.
- **Indicator**: a binary (or graded) observation with a detection performance,
  summarised by

$$ \mathrm{TPR} = P(\text{indicator} \mid \text{economic}), \qquad
\mathrm{FPR} = P(\text{indicator} \mid \text{barren}). $$

- **Likelihood ratio** $\mathrm{LR} = \mathrm{TPR}/\mathrm{FPR}$: how much the
  indicator multiplies the odds of the target being economic.

### 2.2 Positive predictive value and drill counts

Bayes' rule gives

$$ \mathrm{PPV} = P(\text{economic} \mid \text{indicator})
= \frac{p\,\mathrm{TPR}}{p\,\mathrm{TPR} + (1-p)\,\mathrm{FPR}}, $$

and $1/\mathrm{PPV}$ is the expected number of drilled anomalies per discovery —
the number an exploration manager actually budgets.

### 2.3 The porphyry signature set as an archetype

A porphyry system, as an **archetype**, is characterised by a zoned alteration
assemblage around an intrusive centre. In words rather than numbers:

| Element | Geophysical proxy | Characteristic false positive |
|---|---|---|
| Potassic core (magnetite-bearing) | Magnetic high | magnetic skarn, magnetic sediments, serpentinite |
| Phyllic / argillic shell (clay) | Conductivity high (EM, MT) | clay-rich host rock, weathered zone |
| Propylitic halo (chlorite, epidote, pyrite) | Elevated chargeability (IP) | abundant pyrite **without copper**, graphite, clay |
| Structural control | Lineament and fabric mapping | pre-existing regional fabric |
| Sulphide-rich shell | Chargeability high | barren pyrite (the single most common false positive) |

The last row is the honest centre of the archetype: **IP responds to sulphide
volume, not to copper grade.** A large pyrite halo with no economic copper is
the designed failure mode of the method, not a malfunction.

## 3. Derivations

### 3.1 One indicator: the prior does the work

Using the demonstration's stated synthetic indicator ($\mathrm{TPR} = 0.70$,
$\mathrm{FPR} = 0.15$, so $\mathrm{LR} = 4.67$):

| Prior $p$ | Posterior | Targets per discovery |
|---|---|---|
| 0.002 | 0.0093 | 107.9 |
| 0.010 | 0.0450 | 22.2 |
| 0.050 | 0.1972 | 5.1 |
| 0.200 | 0.5385 | 1.9 |

The indicator is *identical* in every row; only the belt changed. **A survey
with a fixed detection performance produces 108 holes per discovery in one
terrain and 2 in another.** Any targeting statement that reports the indicator
without the base rate is not a prospectivity statement.

### 3.2 Multiple indicators: the independence assumption

If $n$ indicators are conditionally independent given the state, the
posterior odds are multiplied by $\mathrm{LR}^{n}$:

$$ \frac{P(\text{econ}\mid \text{all})}{P(\text{barren}\mid \text{all})}
= \frac{p}{1-p}\,\mathrm{LR}^{n}. $$

With $p = 0.02$ and $\mathrm{LR} = 4.67$, the demonstration computes:

| $n$ | Fully independent | Half-independent | Strongly correlated |
|---|---|---|---|
| 1 | 0.0870 | 0.0422 | 0.0291 |
| 2 | 0.3077 | 0.0609 | 0.0320 |
| 3 | 0.6747 | 0.0728 | 0.0327 |

The "independent" column rises from 9% to a near-certainty as indicators are
added, because $\mathrm{LR}^{n}$ is a multiplicative explosion. The correlated
columns barely move. **Both cannot be right.** The truth for a real district is
in between, and the modelling question is: which indicators share a cause?

For this archetype, three of the standard indicators share the same cause — the
intrusive and hydrothermal system itself:

- a magnetic high (magnetite in the potassic core),
- a conductivity high (clays in the phyllic shell),
- a radiometric low (potassic alteration visible as a potassium anomaly **only
  if** the potassium is in the altered rock rather than a cover),

all measure *different manifestations of the same body*. Treating them as
independent "confirmation" is the commonest quantitative error in district
targeting, and it inflates the posterior from around 3-7% to 67% in the
demonstration, i.e. from "drill if the programme is large" to "drill
immediately".

**What to do instead.** Ask of each pair of indicators whether a single
geological process could produce both. If yes, treat them as one indicator, or
erect a shared factor model (as the demonstration's shared-risk-factor
calculation does for play elements). Independence must be *argued*, not assumed.

### 3.3 Magnetic depth and the shape ambiguity

For a compact source, the on-axis gradient anomaly in the demonstration is
modelled as a vertical dipole,

$$ B_z(x) = B_0\,\frac{z^{3}}{(x^{2}+z^{2})^{3/2}}, $$

and for a two-dimensional body (a horizontal cylinder) as

$$ B_z(x) = B_0\,\frac{z^{2}}{x^{2}+z^{2}}, $$

with $B_0$ the anomaly at $x = 0$ in each case. Both produce a symmetric
positive anomaly with a single peak. Fitting the **wrong** model to a profile
(the demonstration's exercise) gives:

| Profile generated by | Model fitted | Depth recovered |
|---|---|---|
| horizontal cylinder at 150 m | compact ($z^{-3}$) | 203.2 m |
| compact body at 150 m | cylinder ($z^{-2}$) | 110.1 m |

A 35% depth error in one direction and 27% in the other, from a *perfectly
noiseless* profile. **The geological model, not the measurement, dominates the
depth.** This is why magnetic depth estimates should be quoted as ranges,
cross-checked with a second method (gravity, seismic, drilling) and accompanied
by the shape assumption used.

### 3.4 The drilling decision

Let $C$ be the all-in cost of a hole and $V$ the net value of a discovery. The
expected value of drilling at posterior probability $q$ is

$$ \mathbb{E}[V_{\text{hole}}] = q\,V - C, \qquad
\text{break-even } q^{*} = \frac{C}{V}. $$

With the demonstration's synthetic values ($C = 1$, $V = 40$),
$q^{*} = 0.025$. Combined with the single-indicator posterior:

| Prior $p$ | Posterior | Expected value | Decision |
|---|---|---|---|
| 0.002 | 0.0093 | $-0.63$ | do not drill |
| 0.010 | 0.0450 | $+0.80$ | drill |
| 0.020 | 0.0870 | $+2.48$ | drill |
| 0.050 | 0.1972 | $+6.89$ | drill |

The break-even posterior is shockingly low when a discovery is worth 40 times a
hole — and that is the honest arithmetic behind district-scale porphyry
exploration: it is a *portfolio* business, where many cheap holes and a few large
discoveries are the only way the numbers work, and the destroyer of the
portfolio is the correlated-indicator error of Section 3.2, which makes an
operator drill a *concentrated* bet rather than a portfolio.

## 4. Worked examples

### Example 1 — two belts, one survey

An IP chargeability indicator has $\mathrm{TPR} = 0.70$, $\mathrm{FPR} = 0.15$.
It is flown over a belt with a $1\%$ base rate and over a belt with a $5\%$ base
rate.

$$ \mathrm{PPV}_{1\%} = \frac{0.01(0.70)}{0.01(0.70)+0.99(0.15)} = 0.045, \qquad
\mathrm{PPV}_{5\%} = \frac{0.05(0.70)}{0.05(0.70)+0.95(0.15)} = 0.197. $$

The same anomaly, the same instrument: 22 holes per discovery in the first belt
against 5 in the second. **The belt, not the survey, sets the targeting
efficiency.**

### Example 2 — the correlated-indicator error

An interpreter presents three "independent" indicators, each
$\mathrm{TPR}/\mathrm{FPR} = 0.70/0.15$, on a prospect with a $2\%$ prior, and
concludes a 67% chance of an economic deposit (the $n = 3$ independent value).

Two of the three are the magnetic high and the conductivity high, both caused by
the same intrusive body. If those two are treated as one indicator (so
$n = 2$ effective), the posterior is 30.8%. If all three share the intrusive
cause (the "strongly correlated" column), it is 3.3% — a factor of 20 below the
claim. **The error is not small; it changes the decision.**

### Example 3 — a magnetic depth range from a half-width

A profile over a magnetite-bearing stock has a half-width (the distance from the
peak to the point where the anomaly has fallen to half its peak) of
$x_{1/2} = 250\ \mathrm{m}$. For the two archetype shapes:

- **compact (dipole):** $\frac{z^{3}}{(x^{2}+z^{2})^{3/2}} = \frac12$
  gives $x_{1/2}^{2} = (2^{2/3}-1)z^{2} = 0.5874\,z^{2}$, so
  $z = x_{1/2}/0.766 = 326\ \mathrm{m}$;
- **horizontal cylinder:** $\frac{z^{2}}{x^{2}+z^{2}} = \frac12$ gives
  $x_{1/2} = z$, so $z = 250\ \mathrm{m}$.

The same half-width supports depths of 250 m and 326 m — a 30% difference from
the shape assumption alone. The demonstration's independent shape test (fitting
each model to the other's profile) gives the same conclusion: a cylinder profile
fitted as a compact body returns 203.2 m against a true 150 m, and a compact
profile fitted as a cylinder returns 110.1 m. **Quote the range and the shape
assumption; a single depth overstates what a magnetic profile can support.**

## 5. Assumptions and regime of validity

1. **Base rate $p$ applies to the population drilled.** If the targets are
   pre-selected by the same indicators used in the calculation, the prior is
   already conditioned and the posterior double-counts.
2. **TPR and FPR are stable across the district.** Detection performance depends
   on cover, relief and regolith; a district-wide single value is an
   approximation.
3. **Conditional independence** must be justified pairwise, not asserted for
   three or more indicators.
4. **Dipole and cylinder models** assume a compact or 2-D source, uniform
   magnetisation, and no remanence. Remanence can flip the anomaly's sign and
   defeat both.
5. **Economic model.** $V$ and $C$ are synthetic and include no commodity-price
   uncertainty, no royalties and no discounting. They are placeholders for a
   decision structure, not a valuation.

## 6. Python demonstration

`code/case_study_porphyry_demo.py` prints:

1. PPV and targets-per-discovery for a single indicator across four base rates;
2. the posterior for one, two and three indicators under independence and two
   correlation levels;
3. the depth recovered when the wrong source shape is fitted to a synthetic
   magnetic profile;
4. the expected value of a drillhole and the break-even posterior.

```bash
cd 11-exploration-geophysics/07-exploration-case-studies/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python case_study_porphyry_demo.py
```

Companions:
[`exercises/01-case-study-porphyry-exercises.md`](./exercises/01-case-study-porphyry-exercises.md)
and
[`exercises/01-case-study-porphyry-solutions.md`](./exercises/01-case-study-porphyry-solutions.md).

## Common pitfalls

1. **Reporting the anomaly, not the probability.** A map of anomalies is a
   measurement; a prospectivity statement is a probability with a base rate.
2. **Treating correlated indicators as independent.** The bias grows as
   $\mathrm{LR}^{n}$; it is the largest error in district targeting.
3. **Quoting a magnetic depth from one source shape.** The shape error exceeds
   the measurement error.
4. **Reading IP as a copper indicator.** IP measures sulphide volume; a barren
   pyrite halo is the designed false positive.
5. **Ignoring the portfolio.** With a low base rate, the value comes from many
   cheap holes; a "high-confidence" target built on correlated indicators is a
   concentrated bet with an overstated probability.

## Mastery checkpoint

Complete this without notes:

> A district targeting study has a base rate of $0.015$ and three indicators:
> a magnetic high ($\mathrm{TPR}=0.65$, $\mathrm{FPR}=0.20$), a conductivity high
> ($\mathrm{TPR}=0.60$, $\mathrm{FPR}=0.30$) and an IP high
> ($\mathrm{TPR}=0.75$, $\mathrm{FPR}=0.25$). The magnetic and conductivity
> indicators are both caused by the intrusive body. **(a)** Compute the
> single-indicator posterior for the IP high. **(b)** Compute the posterior if
> all three were independent, and then if the magnetic and conductivity
> indicators were counted as one. **(c)** A hole costs $C$ and a discovery is
> worth $60C$; compute the break-even posterior and decide, using (b), whether
> to drill. **(d)** State the one measurement that would most reduce the largest
> remaining uncertainty.

A worked version of (a)-(c) is in the lesson-07-01
[solutions](./exercises/01-case-study-porphyry-solutions.md).

## Related modules

- [11-02 Mineral Exploration Geophysics](../02-mineral-exploration/README.md) —
  the signatures used as evidence here.
- [11-01-03 Cost, Risk and Value of Information in Exploration](../01-exploration-workflow/03-cost-benefit.md)
  — the decision framework.
- [11-07-02 Case Study: Basin Analysis and Play Assessment](./02-case-study-basin.md)
  — the same probability logic in a sedimentary play.
- [11-07-03 Case Study: Geothermal Field Development](./03-case-study-geothermal.md)
  and [11-07-04 Case Study: Arid-Region Groundwater Exploration](./04-case-study-groundwater.md).
- [18-05 Bayesian Inversion and Inference](../../18-inverse-problems/05-bayesian-inversion/01-bayes-inverse-formulation.md)
  and [21-06-06 Mineral Prospectivity with Machine Learning](../../21-statistics-bayesian-ml/06-ml-in-geophysics/06-mineral-prospectivity-ml.md).

## Self-assessment checklist

- [ ] I can decompose a targeting argument into its four parts.
- [ ] I can compute a PPV and a targets-per-discovery count.
- [ ] I can explain and quantify the correlated-indicator bias.
- [ ] I can state the shape ambiguity in a magnetic depth estimate.
- [ ] I can compute a break-even probability and decide.
- [ ] I can state the false-positive population of each indicator.
