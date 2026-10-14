---
id: 24-03-03
title: "Designing Observational, Experimental and Modelling Studies"
level: research
prereqs: ["24-03-02", "21-08-01"]
estimated_minutes: 60
tags: [research, study-design, power, confounding, measurement-error, design]
---

# Designing Observational, Experimental and Modelling Studies

A design is a commitment to numbers made before the data exist. Three of them —
the effect size to be detected, the significance level and the required power —
determine the sample size, and two structural properties — confounding and
measurement error — determine whether the numbers mean anything at all. This
lesson measures each: the power curve and its quadratic cost, a spurious
association produced entirely by an unmeasured common cause, and the exact
attenuation of a slope by unreliable measurement.

The organising idea is that **a design is an argument about what could go wrong,
made in advance**. Observational studies trade control for realism and must
therefore argue about confounding; experiments trade realism for control;
modelling studies trade data for mechanism and must argue about identifiability.
Each has a characteristic failure mode, and each failure mode is measurable.

> **Data provenance.** All numbers are **SYNTHETIC**. Effects are simulated from
> the normal model with chosen parameters; the confounder loadings and
> reliabilities are chosen teaching values. No real survey, experiment or model
> output is analysed.

## Learning objectives

By the end of this lesson you will be able to:

1. **State** the three numbers a design must fix in advance and **compute** the
   implied sample size.
2. **Compute** a power curve by simulation and **compare** it with the analytic
   sample-size formula.
3. **Explain** why power is bought quadratically and **state** the consequence for
   small effects.
4. **Demonstrate** confounding with a measured spurious association and **state**
   what adjustment requires.
5. **Compute** the attenuation of a slope from a stated measurement reliability and
   **correct** an observed slope for it.
6. **Choose** between observational, experimental and modelling designs for a
   stated question and **name** the design's characteristic failure mode.

## Prerequisites

- [24-03-02 Hypotheses, Falsifiability and Testing in Earth Science](02-hypothesis-and-falsifiability.md) —
  the testing logic a design serves.
- [21-08-01 Experimental Design](../../21-statistics-bayesian-ml/08-causal-inference-and-design/01-experimental-design.md) —
  the statistical treatment of randomisation, blocking and power.

## 1. The three numbers and the sample size

For a two-group comparison with a standardised effect $d$,

$$n_{\text{per group}} = \frac{2\left(z_{1-\alpha/2} + z_{1-\beta}\right)^{2}}{d^{2}} .$$

For $d = 0.50$, $\alpha = 0.05$ and $80\%$ power this gives

$$n = \frac{2(1.960 + 0.842)^{2}}{0.25} = 62.8 \approx 63\ \text{per group}.$$

The demonstration's simulated power curve reaches $80\%$ at $n = 64$, confirming
the formula. The important property is in the $d^{2}$ denominator: **halving the
effect size quadruples the sample**. If a reviewer cannot find the three numbers in
a proposal, the study has not been designed, only described.

## 2. The power curve, measured

| $n$ per group | Simulated power | Cost index $n^{2}$ |
|---|---|---|
| $8$ | $16.8\%$ | $64$ |
| $16$ | $29.8\%$ | $256$ |
| $32$ | $51.7\%$ | $1024$ |
| $48$ | $67.6\%$ | $2304$ |
| $64$ | $81.0\%$ | $4096$ |
| $128$ | $97.6\%$ | $16384$ |
| $192$ | $99.8\%$ | $36864$ |

Two design consequences follow. First, the curve is steep in the middle and flat at
both ends, so the marginal value of one more station is largest around the
$50\%$–$80\%$ region and negligible above $98\%$. Second, the cost index grows as
$n^{2}$ for a fixed effect, so a study planning for $d = 0.25$ instead of $0.50$
needs four times the instruments — a decision best made while the array is still
being designed. Using the $d = 0.50$ sample size ($n = 63$ in the formula) for a
true $d = 0.25$ effect yields $25.2\%$ power: a study that will almost certainly
report "no significant difference".

## 3. Confounding: a replicable spurious association

Simulate a confounder $z$ that loads on both the predictor $x$ and the outcome $y$
with loading $0.60$, while the true direct effect of $x$ on $y$ is exactly zero:

| Regression | Slope estimate | Scatter (1 s.d.) | Significant in |
|---|---|---|---|
| $y$ on $x$, unadjusted | $+0.3585$ | $\pm 0.0659$ | $100.0\%$ of replications |
| $y$ on $x$, adjusted for $z$ | $-0.0014$ | $\pm 0.0711$ | $\approx 5\%$ |

The unadjusted association is not an artefact of one sample: it appears in every
replication, and it is entirely produced by the unmeasured common cause. This is
the honest form of the familiar warning: an observational result can be perfectly
reproducible and still be a consequence of the design rather than of the Earth.

**What adjustment requires.** Adjustment works here only because $z$ was measured.
In practice the confounder list must be written before the survey, with a reason
for each variable: a common cause of both the predictor and the outcome, or a
proxy for one. Variables that are merely correlated with the outcome are not
confounders and can make things worse by importing the predictor's variance.

## 4. Measurement error: attenuation

If $x$ is observed with additive noise so that the reliability (the ratio of true
to observed variance) is $\lambda$, then the estimated slope is attenuated by
exactly $\lambda$ for simple linear regression:

$$\hat\beta_{\text{observed}} = \lambda\,\beta_{\text{true}} .$$

The demonstration, with $\beta_{\text{true}} = 1.000$:

| Reliability $\lambda$ | Measured slope | Ratio |
|---|---|---|
| $1.0$ | $1.0009$ | $1.001$ |
| $0.8$ | $0.7997$ | $0.800$ |
| $0.6$ | $0.6008$ | $0.601$ |
| $0.4$ | $0.4040$ | $0.404$ |

At reliability $0.6$ the slope is $60\%$ of the truth, **and no increase in $n$
fixes it**: the bias is multiplicative and systematic, so precision grows while
accuracy does not. The correction is either to estimate $\lambda$ from repeated
measurements and divide by it, or to state the attenuation and interpret the
slope as an attenuated one. Reporting an attenuated slope as if it were the true
effect is a common and entirely avoidable error.

## 5. Choosing the design

| Design | Gains | Gives up | Characteristic failure |
|---|---|---|---|
| Observational | Realism, coverage, cost | Control | Confounding; attenuation |
| Experimental | Control, randomisation | Realism, scale | External validity; unrepresentative sample |
| Modelling | Mechanism, extrapolation | Direct evidence | Identifiability; overfitting to a calibration set |

The choice is not a hierarchy. A well-designed observational study with a
pre-specified confounder list and repeated measurements is stronger evidence than
an experiment on an unrepresentative sample, and a model that is identifiable and
tested against held-out data is stronger than either for questions at scales no
experiment can reach.

**The design review, in five questions:**

1. What is the primary outcome, with its unit?
2. What is the effect size that matters, and where does that number come from?
3. What is the sample size, and what power does it buy?
4. What are the plausible common causes, and which are measured?
5. What is the reliability of each key measurement, and how will it be reported?

## Assumptions and regime of validity

1. **The simulations are normal, homoscedastic and independent.** Real data are
   autocorrelated and heteroscedastic; the effective sample size replaces $n$.
2. **The confounder loading is $0.60$.** The measured spurious slope is a property
   of that loading, not a universal constant.
3. **Attenuation is exact only for simple linear regression with independent
   additive error.** Multiple regression, nonlinear links and error correlated
   with the outcome all change the correction.
4. **Power formulas assume the effect size is known.** It rarely is; the design
   should be repeated for a plausible range and the weakest case reported.
5. **A design cannot fix an ill-posed question.** If the quantity is not
   identifiable from the data, no sample size helps; see
   [24-03-01 Formulating Answerable Research Questions](01-research-questions.md).

## The honest summary

Three numbers fix a design, and their arithmetic is unforgiving: halving the
effect quadruples the sample. Two structural properties decide whether the numbers
mean anything: confounding produced a slope of $+0.36$ with a true effect of zero
in every replication, and a reliability of $0.6$ attenuated a true slope of $1.00$
to $0.60$ at any sample size. Both are arguments to make in the design, not in the
discussion.

## Python demonstration

[`code/study_design_demo.py`](./code/study_design_demo.py) prints four labelled
sections: the simulated power curve against the analytic sample size; the
confounding demonstration with and without adjustment; the attenuation table; and
the three numbers a design must commit to.

```bash
cd 24-research-papers-writing/03-research-methods-and-rigour/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python study_design_demo.py
```

## Exercises

Problems are in
[`exercises/03-study-design-exercises.md`](./exercises/03-study-design-exercises.md),
worked answers in
[`exercises/03-study-design-solutions.md`](./exercises/03-study-design-solutions.md).

## Mastery checkpoint

For a study you are planning:

1. Write the primary outcome with its unit and the effect size that matters, with
   its provenance.
2. Compute the sample size for $80\%$ and $90\%$ power at that effect size.
3. Recompute for an effect half as large and state the cost of being wrong.
4. List the plausible common causes and mark which you will measure; say what
   analysis you would run if one were unmeasurable.
5. State the reliability of each key measurement and how it will be estimated.

## Common pitfalls

1. **Choosing the sample size by availability.** The available instruments are a
   constraint, not a design; state the power they buy.
2. **A single effect size.** Report power across a range, and the weakest case.
3. **Adjusting for everything.** Non-confounders import variance and can bias the
   estimate; justify each adjustment.
4. **Ignoring attenuation.** It does not shrink with $n$ and it is systematic.
5. **Treating a model as evidence.** A model is a mechanism with parameters; its
   parameters need data to be constrained.
6. **Post-hoc power.** Power computed from the observed effect is a restatement of
   the $p$-value; report the design's power instead.

## Where this is used

- **Proposals and protocols:** the five questions of §5 are the review checklist a
  panel applies.
- **Field campaigns:** sample size is chosen by instruments and days, so the
  arithmetic must happen before deployment; see
  [23-02 Seismic Instruments and Fieldwork](../../23-field-methods-instruments/02-seismic-instruments-and-fieldwork/README.md).
- **Modelling studies:** identifiability is the analogue of confounding; see
  [18-01-02 Hadamard's Conditions](../../18-inverse-problems/01-inverse-problem-foundations/02-hadamard-well-posedness.md).
- **Instrument selection:** reliability determines what a design can detect; see
  [23-05 Instrumentation and Electronics](../../23-field-methods-instruments/05-instrumentation-and-electronics/README.md).

## Related lessons

- [24-03-04 Reproducible Research Practice End to End](04-reproducible-research-practice.md) —
  what has to be recorded so the design can be checked.
- [24-03-01 Formulating Answerable Research Questions](01-research-questions.md) —
  the question the design serves.
- [24-02-03 Writing Methods Sections That Can Be Reproduced](../02-scientific-writing/03-writing-methods.md) —
  how the design's decisions are reported.
- [21-01-04 Regression](../../21-statistics-bayesian-ml/01-statistics-in-practice/04-regression.md) —
  the estimation machinery behind adjustment and attenuation.

## Self-assessment checklist

- [ ] I can compute a sample size from the three numbers.
- [ ] I can produce a power curve and read its marginal value.
- [ ] I can explain and demonstrate confounding.
- [ ] I can compute and correct attenuation from a reliability.
- [ ] I can name the characteristic failure of each design type.
- [ ] I can answer the five design-review questions for my own study.
