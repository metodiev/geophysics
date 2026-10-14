---
id: 25-05-05
title: "Project: Reproducing a Published Geophysical Result"
level: doctoral
prereqs: ["06-11-02", "21-01-03", "21-03-04", "25-05-04"]
estimated_minutes: 260
tags: [projects, reproducibility, statistics, aftershocks, doctoral]
---

# Project: Reproducing a Published Geophysical Result

## Learning objectives

By the end of this project you will be able to:

1. **Extract** a published quantitative claim and, separately, the *method choices*
   on which it depends, including the ones the paper does not state.
2. **Re-derive** the claim from the data with an independent implementation and
   **compare** the result against both the published uncertainty and your own.
3. **Classify** a reproduction by tier — same code, independent code, different
   method, independent data — and **state** which tier your attempt reaches.
4. **Quantify** a method-dependent spread and compare it with the published
   uncertainty, rather than judging agreement by eye.
5. **Derive** the censored maximum-likelihood estimator for a decay law and
   **explain** why the truncation of a catalogue changes the parameters rather than
   merely their error bars.
6. **Write** a reproduction report that names every choice, reports a goodness-of-fit
   statistic, and states what a disagreement does and does not falsify.
7. **Produce** a defensible negative result: "the claim does not follow from the
   stated method" is a valid outcome, and it must be established, not asserted.

All data in this project are **SYNTHETIC**: an aftershock catalogue generated from a
modified Omori law with known parameters in
[`code/reproduce_result_demo.py`](./code/reproduce_result_demo.py). The workflow is
identical when the catalogue is real, and the real ones are available from the
services listed in `tools/verified_links.tsv` (the ISC and USGS event catalogues at
the FDSN event services <https://service.iris.edu/fdsnws/event/1/query> and
<https://service.iris.edu/fdsnws/station/1/query>).

## Prerequisites

- [06-11-02 Aftershock Sequences and Their Statistics](../../06-seismology/11-earthquake-statistics-and-hazard/02-aftershocks.md) —
  the modified Omori law used as the worked example.
- [21-01-03 Resampling and the Bootstrap](../../21-statistics-bayesian-ml/01-statistics-in-practice/03-resampling.md) —
  how uncertainties in a reproduction are usually obtained.
- [21-03-04 Markov Chain Monte Carlo in Practice](../../21-statistics-bayesian-ml/03-bayesian-inference/04-mcmc-practice.md) —
  the inference machinery behind the maximum-likelihood route.
- [25-05-04 Project: Trans-Dimensional Bayesian Inversion](./04-bayesian-inversion-project.md) —
  the validation discipline this project applies to someone else's conclusion.

## 1. The question

*A published paper reports an aftershock-decay exponent $p = 1.10 \pm 0.03$ for a
sequence, fitted to 30 days of a catalogue complete from the mainshock. Can that
claim be re-derived, and how much of it is the method rather than the data?*

The demonstration makes the answer quantitative. Four defensible-looking routes to
the same exponent, applied to the *same* synthetic catalogue of 956 events generated
with $K = 150$, $c = 0.05$ d and $p = 1.10$:

| route | method | $p$ | against the claim |
|---|---|---|---|
| A | maximum likelihood, complete catalogue | $1.1185 \pm 0.0308$ | $+0.6$ claimed $\sigma$ — reproduced |
| B | binned log–log regression | $1.0213$ | $-2.6$ claimed $\sigma$ — not reproduced |
| C | $c$ fixed at 0.01 d instead of fitted | $0.9592$ | $-4.7$ claimed $\sigma$ |
| D | catalogue censored at 12 h, censored likelihood | $1.2498 \pm 0.1197$ | $+5.0$ claimed $\sigma$, but $\pm 3.9\times$ the standard error |

The routes span $0.2907$ in $p$, which is $4.8$ times the published uncertainty of
$\pm 0.03$. **The method, not the data, decides whether the claim reproduces.**

## 2. Extracting the claim and the choices

A reproduction starts with a two-column list, not with the code.

**The claim.** $p = 1.10 \pm 0.03$, $c$ fixed at $0.05$ d, for this sequence and this
time window; the paper's stated uncertainty is quoted with its meaning (one standard
error, a 95% interval, a bootstrap interval, or a posterior credible interval —
these differ by factors of two and must be identified).

**The choices.** Each of the following changes the answer, and most papers state only
some of them:

1. **Estimator**: maximum likelihood on the unbinned times, least squares on a
   log–log histogram, a Bayesian posterior, or an iterative "shortcut"
   (Utsu–Ogata) that alternates between $\hat c$ and $\hat p$. Route B is the
   classical choice and is still common.
2. **Catalogue completeness**: the start time $t_0$ from which the catalogue is
   complete, and how it was determined. Route D shows what a 12-hour error does.
3. **Which parameters are fitted**: all three, or $c$ held at a plausible value.
   Route C shows the cost of fixing $c$ — $12.8\%$ on the true $p$, because $c$ and
   $p$ are correlated at $+0.81$.
4. **The observation window** $T$: the log-likelihood contains
   $\int_{t_0}^{T}\lambda(t)\,dt$, so $T$ enters the answer, and papers that
   quote a rate without $T$ have quoted an incomplete model.
5. **The magnitude threshold** used to filter the catalogue, and whether the
   threshold itself was estimated (a declining detection threshold after the
   mainshock mimics a steep decay and biases $p$ upward).
6. **The binning** in histogram-based methods, including whether the bins are
   logarithmic and whether empty bins are used.

## 3. The estimator, written down

Modified Omori law, $\lambda(t) = K/(t+c)^p$ for $t > t_0$. For a catalogue of event
times $t_1 < \dots < t_n$ complete from $t_0$, the log-likelihood is

$$\ell(K, c, p) = \sum_{i=1}^{n}\Bigl[\log K - p\log(t_i + c)\Bigr]
- \frac{K}{1-p}\Bigl[(T+c)^{1-p} - (t_0+c)^{1-p}\Bigr],$$

with the $p = 1$ limit $\int K/(t+c)\,dt = K\log\frac{T+c}{t_0+c}$. The second term is
the expected count in the window; **it is the term that couples the parameters to the
window and to the completeness start**, and omitting the correct $t_0$ — using
$t_0 = 0$ while fitting only $t_i \ge 0.5$ d — gives $K = 8500$, $c = 6.3$ d and
$p = 2.31$ on this dataset: a factor of two in the exponent from one subscript.

**Uncertainty.** The standard errors in the table come from the numerical Hessian,
$\mathrm{Cov} \approx \mathbf H^{-1}$ with
$H_{ij} = \partial^2\ell/\partial\theta_i\partial\theta_j$. On route A,
$K = 151.3 \pm 7.7$ (true 150), $c = 0.0529 \pm 0.0102$ (true 0.05) and
$p = 1.1185 \pm 0.0308$ (true 1.10): the estimator is unbiased here, and the
deviation from the claim is $+0.0185 = 0.62$ claimed standard errors. That is what a
successful reproduction looks like — **parameter recovery stated against the truth,
and agreement with the paper stated in the paper's own units.**

## 4. Goodness of fit before parameters

Parameter agreement is not evidence that the model was fitted correctly. Report the
integrated counts:

| subset | observed | expected from the generating model |
|---|---|---|
| full catalogue | 956 | 956.6 |
| censored at 12 h | 519 | 525.1 |

Both are consistent, so the *counts* do not diagnose the problem — the parameters do.
This is the standard trap in reproduction: a model can reproduce the total rate while
getting the decay exponent wrong, because $K$ trades against $p$. Always report at
least one fit-free statistic (total count), one parameter-free shape statistic (the
fraction of events in each time decade), and the parameters.

## 5. Reproduction tiers

A reproduction is only meaningful with the tier stated, because the tiers strengthen
in different directions:

| tier | what is repeated | what it can falsify |
|---|---|---|
| T1 | the authors' code, same data | nothing; it tests the environment |
| T2 | independent code, same method | implementation errors |
| T3 | an independent method, same data | the claim's robustness to the method — **this project's routes B, C and D** |
| T4 | an independent dataset, same method | the generality of the claim |
| T5 | a different question, new data | the claim's importance (replication, not reproduction) |

The demonstration is a T3 attempt: the same synthetic catalogue, four methods. Its
conclusion is *not* "the paper is wrong" — it is "the claim is reproduced only under
the estimator the paper used, and the published uncertainty does not cover the method
dependence". That distinction is the whole point of the exercise, and stating it
correctly is what separates a reproduction report from a criticism.

## 6. The project specification

**Steps.**

1. Choose a published quantitative claim (a fitted parameter, a rate, a coefficient,
   a threshold) and write it down with its uncertainty and the definition of that
   uncertainty.
2. Extract the method choices of §2 into a table; mark every one the paper does not
   state, and choose a value for it explicitly.
3. Write the estimator down (the likelihood, the objective, the estimator equation)
   independently of the paper's description.
4. Obtain or reconstruct the data; document the query, the filters, the thresholds
   and the resulting count.
5. Reproduce the headline number and compare against the published uncertainty
   *and* against your own uncertainty; state both.
6. Repeat with at least two alternative method choices for the two choices that you
   judge least constrained by the paper.
7. Report a fit-free statistic and a shape statistic.
8. Write the reproduction report: claim, choices, method, results, method-dependence
   spectrum, goodness of fit, tier, and a statement of what the disagreement does and
   does not establish.

**Deliverable.** A reproduction report with the claim and choices table, the
independently derived estimator, the reproduced number with its uncertainty, the
method-dependence spectrum, and the tier.

**Success criterion.** The claim and the choices are separated; the estimator is
written independently; the comparison is made in the paper's own uncertainty units;
two method alternatives are quantified; a goodness-of-fit statistic is reported; and
the tier and the limits of the conclusion are stated.

## 7. Failure modes

1. **Reproducing the number by tuning the choices until it agrees.** This is the
   single most common failure, and the method-dependence table of §1 is the antidote:
   declare the alternatives before seeing their results.
2. **Judging agreement by eye** instead of by the published uncertainty and your own.
3. **Confusing the estimator's standard error with the method dependence.** Route D's
   $\pm 0.1197$ is $3.9\times$ route A's; the two are different quantities and both
   belong in the report.
4. **Ignoring catalogue completeness.** The first 12 hours of this catalogue contain
   437 of 956 events, and their absence moves $p$ by $+0.13$.
5. **Fixing a correlated parameter "for stability".** $c$ and $p$ correlate at
   $+0.81$; fixing $c$ moves $p$ by $5.2$ of the MLE's standard errors.
6. **Reporting a disagreement as a refutation.** A T3 disagreement falsifies the
   claim *as stated for the method stated*; it says nothing about the physics until
   T4 (independent data) is attempted.
7. **No goodness-of-fit statistic**, leaving no way to distinguish a wrong model from
   a wrong interpretation.

## 8. Rubric

| Criterion | Weight | Full marks |
|---|---|---|
| Claim and choices separated | 20% | choices table with the unstated ones flagged |
| Estimator derived independently | 20% | likelihood written out, window and completeness explicit |
| Reproduction compared in the right units | 20% | published **and** own uncertainties, both quoted |
| Method-dependence spectrum | 20% | at least two alternatives, spread compared with the published uncertainty |
| Goodness of fit | 10% | a fit-free and a shape statistic |
| Tier and limits of conclusion | 10% | tier stated, disagreement's scope bounded |

## 9. The honest summary

The product is a reproduction report whose result is a *range*, not a number. On this
synthetic catalogue the maximum-likelihood route recovers the generating parameters
($K = 151.3$ against 150, $c = 0.0529$ against 0.05, $p = 1.1185$ against 1.10) and
reproduces the claim to $0.6$ claimed standard errors; the binned regression, the
fixed-$c$ fit and the censored catalogue give $1.0213$, $0.9592$ and $1.2498$, a span
$4.8$ times the published uncertainty. The transferable results are that a claim is
never separable from its estimator, that catalogue completeness is a parameter of the
result rather than a data-quality note, and that a reproduction report earns its
credibility by quantifying the method dependence *before* declaring agreement or
disagreement.

## Python demonstration

[`code/reproduce_result_demo.py`](./code/reproduce_result_demo.py) prints every number
above: the synthetic catalogue, the four estimation routes with their uncertainties
and correlations, the goodness-of-fit counts, and the method-dependence verdict.

```bash
cd 25-projects-capstone/05-doctoral-projects/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python reproduce_result_demo.py
```

Print-only, seeded with `np.random.default_rng(20261014)`, no network, no files, no
plots, exits 0, runs in about $0.2$ s.

## Exercises

Graded problems and worked solutions are in
[`exercises/05-reproduce-published-result-exercises.md`](./exercises/05-reproduce-published-result-exercises.md)
and
[`exercises/05-reproduce-published-result-solutions.md`](./exercises/05-reproduce-published-result-solutions.md).
The ★★★ item asks for a full reproduction plan for a real published claim.

## Mastery checkpoint

Without notes:

1. State the four tiers of reproduction and what each can falsify.
2. Write the modified-Omori log-likelihood, including the window integral, and state
   what happens if $t_0$ is wrong.
3. Explain why fixing a parameter that is correlated with the fitted one biases the
   result, using the $+0.81$ correlation as the example.
4. Compute how many standard errors a method-induced discrepancy is, given both the
   published and the fitted uncertainties.
5. State what a T3 disagreement does and does not establish.

## Common pitfalls

1. Using the authors' code and calling it a reproduction (that is T1).
2. Omitting the completeness start from the estimator while restricting the data.
3. Quoting agreement without a goodness-of-fit check.
4. Treating the method dependence as "systematics to be discussed" instead of a
   quantified range.
5. Reporting a refutation where the correct statement is "the claim is
   method-dependent".

## Where this is used

Reproduction is the closing loop of the research process and the reason the capstone
of [Module 06](../06-capstone-research/README.md) requires a validated, released
analysis. The three skills it develops — separating a claim from its method,
quantifying the method dependence, and writing a bounded conclusion — are the same
ones used in [25-05-03](./03-geodynamic-model-data.md) for model comparison and in
[25-05-04](./04-bayesian-inversion-project.md) for validating a sampler. In
professional practice they are what a referee's replication request tests.

## Related lessons

- [21-02-04 Regression and Its Assumptions](../../21-statistics-bayesian-ml/01-statistics-in-practice/04-regression.md) —
  the assumptions behind the binned route's least squares.
- [21-08-02 Methods of Causal Inference](../../21-statistics-bayesian-ml/08-causal-inference-and-design/02-causal-inference-methods.md) —
  what a method-dependent result does to a causal claim built on it.
- [22-02-01 The Reproducibility Crisis in Geoscience](../../22-data-engineering-reproducibility/02-reproducible-workflows/01-reproducibility-crisis.md) —
  the software side of reaching tier T2.
- [25-05-04 Project: Trans-Dimensional Bayesian Inversion](./04-bayesian-inversion-project.md) —
  validating an inference against a case with a known answer.

## Self-assessment checklist

- [ ] I can separate a published claim from its method choices.
- [ ] I can re-derive an estimator independently of the paper's description.
- [ ] I can compare a reproduction in the paper's own uncertainty units.
- [ ] I can quantify a method-dependence range and compare it with the claim.
- [ ] I can write a bounded negative result.
- [ ] I can state the tier of my own reproduction.
