---
id: 21-08-02
title: "Causal Inference Methods and Counterfactuals"
level: research
prereqs: ["21-08-01", "21-04-02", "21-06-09"]
estimated_minutes: 60
tags: [causal-inference, counterfactual, confounding, identification, teaching]
---

# Causal Inference Methods and Counterfactuals

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** a potential outcome, an average treatment effect and a
   counterfactual, and **state** the two assumptions that connect them to data.
2. **Explain** why a difference in means is an estimate of the treatment effect
   only under exchangeability, and **compute** the bias when it fails.
3. **Estimate** an effect by regression adjustment, inverse-probability weighting
   and stratification, and **state** what all three have in common.
4. **Measure** the bias left by an unmeasured confounder and **derive** it from the
   omitted-variable formula.
5. **Distinguish** an identification problem from an estimation problem, and
   **state** that no estimator repairs the first.
6. **Choose** a design response — randomisation, an instrument, a discontinuity, a
   measured confounder, or a sensitivity analysis — for a stated threat.
7. **Report** a causal claim: the target quantity, the identification argument, the
   estimator, the diagnostics, the sensitivity to unmeasured confounding, and the
   population for which the effect is claimed.

Every unit, treatment, outcome and bias below is **SYNTHETIC**, produced by
[`code/causal_inference_methods_demo.py`](./code/causal_inference_methods_demo.py).
No observational data set, trial or published effect estimate is used.

## Prerequisites

- [21-08-01 Experimental and Survey Design for Earth Studies](./01-experimental-design.md) —
  the design vocabulary that this lesson's remedies belong to.
- [21-04-02 Bias-Variance Trade-Off, Underfitting and Overfitting](../../21-statistics-bayesian-ml/04-machine-learning-fundamentals/02-bias-variance.md) —
  the separation of bias from variance that a confounding bias violates.
- [21-06-09 Pitfalls: Spurious Correlations, Non-Stationarity, Extrapolation](../../21-statistics-bayesian-ml/06-ml-in-geophysics/09-ml-pitfalls-geophysics.md) —
  the spurious correlation a missing variable produces.
- [18-05-01 Bayesian Inversion: The Formulation](../../18-inverse-problems/05-bayesian-inversion/01-bayes-inverse-formulation.md) —
  the inverse-problem view of a parameter that is not identifiable.

## 1. Intuition: a causal effect is a comparison of two worlds

For each unit $i$ there are two **potential outcomes**: $Y_i(1)$ if treated and
$Y_i(0)$ if not. The unit's causal effect is $Y_i(1) - Y_i(0)$, and the quantity
usually estimated is the average

$$\mathrm{ATE} = \mathbb{E}\left[Y(1) - Y(0)\right] .$$

The catch is that only one of the two is ever observed. The observed difference in
means,

$$\mathbb{E}[Y \mid D=1] - \mathbb{E}[Y \mid D=0],$$

equals the ATE only if

$$\mathbb{E}[Y(0) \mid D=1] = \mathbb{E}[Y(0) \mid D=0] \quad\text{and}\quad
\mathbb{E}[Y(1) \mid D=1] = \mathbb{E}[Y(1) \mid D=0],$$

that is, if the treated and untreated groups are **exchangeable** — if the
untreated would have done as well as the treated had they been treated, and vice
versa. Randomisation creates exchangeability by design. Everything else in this
lesson is about what can be recovered when it does not hold.

**The demonstration's headline:** the unadjusted difference is $+3.179$ where the
true effect is $2.0$; three adjusted estimators land between $+2.116$ and
$+2.241$; and when a confounder is left unmeasured, all of them rise to
$+3.233$–$+3.392$. Adjustment helps when the confounder is observed and does
nothing when it is not.

## 2. The synthetic study

| Element | Definition |
|---|---|
| units | $n = 2000$ |
| measured confounder | $Z \sim \mathcal N(0,1)$ |
| unmeasured confounder | $U \sim \mathcal N(0,1)$ (used in §4 only) |
| treatment | $D = \mathbf 1\{Z + U > 0\}$ |
| outcome | $Y = 2.0\,D + 1.0\,Z + \varepsilon$, $\varepsilon \sim \mathcal N(0,1)$ |
| true ATE | $2.000$ |
| treated fraction | $0.499$ |
| confounding imbalance | $\mathbb{E}[Z\mid D=1] - \mathbb{E}[Z\mid D=0] = 1.112$ |

The treatment is assigned *because of* $Z$: units with high $Z$ are more likely
treated, and $Z$ also raises the outcome. That is the definition of confounding, and
it is the situation of every observational geophysical study in which "treatment"
is an injection, a land-use change, a management practice or a hazard exposure.

## 3. Four estimators of the same number

| Estimator | Estimate | 95% interval | Bias |
|---|---|---|---|
| unadjusted difference in means | $+3.179$ | $\pm0.109$ | $+1.179$ |
| regression on $D$ and $Z$ | $+2.116$ | $\pm0.103$ | $+0.116$ |
| inverse-probability weighting | $+2.241$ | $\pm0.150$ (bootstrap) | $+0.241$ |
| stratification on propensity quintiles | $+2.231$ | — | $+0.231$ |

Readings:

1. **Adjustment removes most of the bias.** The unadjusted estimate is $59\%$ too
   large; the adjusted estimates are $6$–$12\%$ too large. The remaining excess is
   finite-sample overlap error, not bias: with propensity scores spanning
   $0.020$–$0.980$, some regions have few units of one arm, and the weighted and
   stratified estimators inherit that.
2. **The three adjusted estimators agree because they condition on the same
   information.** Regression, weighting and stratification are three ways to use
   $Z$; they are not three independent confirmations. A report that presents all
   three as agreement is claiming more than it has.
3. **Regression is the most precise here** ($\pm0.103$ against $\pm0.150$), because
   it uses the continuous $Z$ rather than five strata or weights; that is a
   variance statement, not a bias statement.
4. **The propensity range matters.** Weights near $1/0.02 = 50$ make IPW unstable;
   had the smallest propensity been $0.001$, the IPW interval would be far wider
   than the regression's. Reporting the propensity distribution is part of
   reporting an IPW estimate.

## 4. An unmeasured confounder

Now let the outcome also depend on the unmeasured $U$:
$Y = 2.0D + 1.0Z + 0.8U + \varepsilon$. The estimators become

| Estimator | Estimate | 95% interval | Bias |
|---|---|---|---|
| unadjusted difference in means | $+3.997$ | — | $+1.997$ |
| regression on $D$ and $Z$ | $+3.233$ | $\pm0.124$ | $+1.233$ |
| inverse-probability weighting | $+3.392$ | — | $+1.392$ |
| omitted-variable prediction for the regression | — | — | $+1.284$ predicted |

The omitted-variable formula gives the mechanism exactly: the bias of the
regression coefficient on $D$ equals the unmeasured variable's coefficient on the
outcome times the coefficient of $D$ in a regression of $U$ on $(D, Z)$. Here the
latter is $+1.605$, so the predicted bias is $0.8 \times 1.605 = +1.284$ against a
measured $+1.233$ — agreement to within the sampling error ($\pm0.124$).

Two lessons:

1. **Conditioning on $Z$ makes the residual confounding worse, not better, in one
   specific sense.** The marginal imbalance in $U$ is $+1.083$, but its
   *conditional* coefficient is $+1.605$: because $D$ is a function of $Z+U$,
   holding $Z$ fixed isolates $U$ and exaggerates its role. Adjusting for a
   confounder that is correlated with the unmeasured one changes the bias in a
   direction that must be reasoned about, not assumed.
2. **The bias is $43\%$ of the effect being estimated, against a standard error of
   $0.124$.** The confidence intervals are narrow and centred on the wrong value:
   precision is not validity, and the arithmetic here makes the gap visible.

## 5. Identification versus estimation

| Problem | Fixable by a better estimator? | Example here |
|---|---|---|
| measured confounding | yes | $Z$ in the regression |
| overlap violation (no comparable units) | partly — by changing the estimand to the region of overlap | propensity range $0.020$–$0.980$ |
| unmeasured confounding | **no** | the $0.8U$ term |
| reverse causality | no | if $Y$ caused $D$ |
| selection into the sample | no | if units enter because of $D$ or $Y$ |

The distinction is the point of the lesson. An estimator is a formula; the
identification argument is a claim about the world — that the measured variables
block every back-door path from $D$ to $Y$. When that claim is false, every
estimator consistent with the observed data inherits the bias, and the estimators
*agree with each other* while all being wrong.

## 6. Remedies, in order of strength

1. **Randomise.** Assignment by a coin severs $D$ from every confounder, measured
   or not. The largest single improvement available, and the reason clinical trials
   exist.
2. **Find exogenous variation.** An instrument (something that shifts $D$ and
   affects $Y$ only through $D$), a regression discontinuity (a threshold rule that
   assigns treatment), a difference-in-differences design (a comparison of changes
   across groups), or a natural experiment. Each carries its own assumption, which
   must be stated and, where possible, tested — and each fails silently when the
   assumption is violated.
3. **Measure the confounder.** Turns an unmeasured-confounder problem into a
   measured-confounder problem, which §3 solves.
4. **Bound the bias.** A sensitivity analysis that reports how strong an unmeasured
   confounder would have to be, in the units of the problem, to explain the estimate
   away. Here: an unmeasured variable whose conditional association with the
   treatment is $1.605$ and whose coefficient on the outcome is $0.8$ is enough to
   move the estimate by $1.284$; a report should state the pair of coefficients that
   would reduce the effect to zero, so a reader can judge whether such a variable
   plausibly exists.

## 7. Assumptions and regime of validity

1. **Consistency.** The observed outcome under the received treatment equals the
   potential outcome for that treatment. Violated when "treatment" is a
   heterogeneous bundle (two different injections labelled the same).
2. **Positivity (overlap).** Every unit has a non-zero probability of each
   treatment given its covariates. Violated when some covariate region is
   exclusively treated; the estimand must then be restricted to the overlap region.
3. **No interference.** One unit's treatment does not change another's outcome.
   Elaborately violated in induced seismicity, contaminant plumes and shared
   aquifers — where the subject of interest is exactly the interference.
4. **No unmeasured confounding**, conditional on the covariates. The assumption
   that §4 shows no estimator can relax.
5. **Correct functional form.** The regression's linearity and the propensity
   model's specification are working assumptions; a misspecified propensity model
   biases IPW, and the diagnostics (balance tables) must be reported.

## The honest summary

On a synthetic study of 2000 units with a true average treatment effect of $2.000$,
the unadjusted difference in means is $+3.179$ — a bias of $+1.179$ — and
regression adjustment, inverse-probability weighting and propensity stratification
give $+2.116$, $+2.241$ and $+2.231$ respectively: three routes through the same
information, all recovering the effect to within about $0.1$. Adding an unmeasured
confounder with a coefficient of $0.8$ on the outcome pushes all three to
$+3.233$–$+3.392$, with a regression bias of $+1.233$ matched to within sampling
error by the omitted-variable prediction of $+1.284$, and the bias is $43\%$ of the
effect being estimated against a standard error of $0.124$. The transferable
conclusions: adjustment is a route through measured information, not a truth
machine; agreement among three adjusted estimators is one argument, not three; an
unmeasured confounder is an identification problem that no estimator repairs; and
the remedy is a design change or a stated bound, never a different estimator.

## Python demonstration

[`code/causal_inference_methods_demo.py`](./code/causal_inference_methods_demo.py)
prints every number quoted above. It:

1. generates the study, prints the true effect, the treated fraction and the
   confounding imbalance in $Z$;
2. estimates the effect four ways — unadjusted, regression, inverse-probability
   weighting with a bootstrap interval, and propensity-quintile stratification —
   and prints each estimate with its interval, its bias and the propensity range;
3. regenerates the study with the outcome depending on the unmeasured $U$ and
   prints the same four estimates, plus the omitted-variable prediction of the
   regression's bias computed from a regression of $U$ on $(D, Z)$;
4. prints the design remedies in order of strength and a `SYNTHETIC` provenance
   line.

Run it with the project virtual environment:

```bash
cd 21-statistics-bayesian-ml/08-causal-inference-and-design/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python causal_inference_methods_demo.py
```

It runs in about 1 s (the bootstrap dominates), reads no files, uses no network and
exits 0.

## Exercises

Graded problems and worked solutions are in
[`exercises/02-causal-inference-methods-exercises.md`](./exercises/02-causal-inference-methods-exercises.md)
and [`exercises/02-causal-inference-methods-solutions.md`](./exercises/02-causal-inference-methods-solutions.md).

## Mastery checkpoint

Without notes:

1. Define exchangeability and show algebraically that the difference in means
   equals the ATE exactly when it holds.
2. Compute the unadjusted bias given a confounding imbalance of $+1.112$ in $Z$ and
   a coefficient of $1.0$ on the outcome, and compare with the measured $+1.179$.
3. State the omitted-variable formula and use it to explain why the regression's
   bias is $+1.233$ rather than the $0.8 \times 1.083 = 0.866$ that the marginal
   imbalance would suggest.
4. A colleague reports three adjusted estimators that agree. State the one question
   that decides whether the agreement is evidence.

## Common pitfalls

1. **Reporting an adjusted estimate as if adjustment were a truth machine.** The
   unmeasured case pushes all three estimators to $+3.2$ and $+3.4$.
2. **Presenting regression, weighting and stratification as independent
   confirmations.** They pass through the same information.
3. **Ignoring the propensity range.** Weights of $1/0.02$ are unstable; state the
   distribution.
4. **Assuming that adjusting for a correlated confounder reduces the bias.** The
   conditional imbalance here ($+1.605$) is larger than the marginal one
   ($+1.083$).
5. **Confusing a narrow interval with validity.** The biased estimate's interval is
   $\pm0.124$ and centred $1.233$ away from the truth.
6. **Assuming no interference.** Shared aquifers, induced seismicity and plumes
   violate it by construction.

## Where this is used

- **Induced seismicity and injection studies**, where the treatment is a
  well's operation and the confounder is the local geology
  ([06-12-01](../../06-seismology/12-induced-and-triggered-seismicity/01-induced-seismicity-causes.md)).
- **Land-use, hydrology and water-quality studies**, where treatments are
  assigned by policy or convenience.
- **Natural-hazard exposure and health studies**, the origin of the modern causal
  inference toolkit.
- **Intervention evaluation in monitoring networks**, where a policy change is
  applied at one site and not another.
- **Instrument calibration and processing comparisons**, where the "treatment" is
  a processing choice made by operators with different data.

## Related lessons

- [21-08-01 Experimental and Survey Design for Earth Studies](./01-experimental-design.md) —
  the design that determines whether identification is possible at all.
- [21-08-03 Attribution in Climate and Hazard Science](./03-attribution-methods.md) —
  attribution as a counterfactual comparison with a modelled counterfactual.
- [21-06-09 Pitfalls: Spurious Correlations, Non-Stationarity, Extrapolation](../../21-statistics-bayesian-ml/06-ml-in-geophysics/09-ml-pitfalls-geophysics.md) —
  the spurious correlation that a missing confounder produces.
- [21-09-02 Honest Reporting of Uncertainty and Limitations](../../21-statistics-bayesian-ml/09-ethical-and-responsible-analytics/02-reporting-uncertainty-ethics.md) —
  how to report an effect whose identification is uncertain.
- [18-05-01 Bayesian Inversion: The Formulation](../../18-inverse-problems/05-bayesian-inversion/01-bayes-inverse-formulation.md) —
  identifiability in the inverse-problem language.

## Self-assessment checklist

- [ ] I can define potential outcomes and the ATE.
- [ ] I can state exchangeability and derive the bias when it fails.
- [ ] I can implement three adjustment routes and say what they share.
- [ ] I can apply the omitted-variable formula to a measured case.
- [ ] I can list the design remedies in order of strength.
- [ ] I can list the six items a causal report must contain.
