---
id: 21-04-03
title: "Cross-Validation, Metrics and the Danger of Leakage"
level: graduate
prereqs: ["21-04-02", "21-01-03"]
estimated_minutes: 60
tags: [machine-learning, cross-validation, metrics, leakage, model-assessment]
---

# Cross-Validation, Metrics and the Danger of Leakage

## Learning objectives

By the end of this lesson you will be able to:

1. **Distinguish** a hold-out estimate from a $k$-fold cross-validation estimate
   and **compute** both.
2. **Explain** why cross-validation reports a spread as well as a mean, and
   **state** the two sources of that spread.
3. **Compute** accuracy, precision, recall and the ROC AUC, and **state** which
   is appropriate for an imbalanced problem.
4. **Identify** leakage in a pipeline, and **measure** the inflation it causes.
5. **Choose** a splitting scheme for grouped, spatial or temporal data.
6. **State** what a validation score does and does not estimate.

All data in this lesson are **SYNTHETIC**, generated in the demonstration. No
measured value is used.

## Prerequisites

- [21-04-02 Bias-Variance Trade-Off, Underfitting and Overfitting](02-bias-variance.md) —
  the error being estimated.
- [21-01-03 Resampling: Bootstrap, Jackknife, Permutation Tests](../01-statistics-in-practice/03-resampling.md) —
  the resampling machinery cross-validation belongs to.
- [21-01-05 Nonparametric Statistics and Kernel Density Estimation](../01-statistics-in-practice/05-nonparametric-methods.md) —
  why a single small validation set is a noisy estimate.

## 1. Intuition: the score is an estimate of a different quantity

A model's apparent accuracy on the data it was fitted to is a statement about
memory. The quantity of interest is the error on data the model has never seen,
drawn from the same process. Every validation scheme is an attempt to estimate
that quantity, and every one of them can be defeated — by a validation set that
is too small, by dependence between the training and validation points, or by a
feature that secretly carries the answer.

The organising principle is: **the validation set must be a stand-in for the
future**. If it is not drawn the way future data will be drawn — at different
stations, in a later year, at other locations — then the score measures the wrong
thing, however carefully the arithmetic is done.

## 2. Hold-out and $k$-fold

The **hold-out** estimate uses one split: fit on $\mathcal D_{\text{train}}$, score
on $\mathcal D_{\text{val}}$, report the validation loss. It is cheap and noisy,
because the specific points withheld determine the answer.

**$k$-fold cross-validation** partitions the data into $k$ folds, trains $k$ times
on $k-1$ folds and scores on the held-out one, and reports

$$\widehat{\mathrm{CV}} = \frac1k\sum_{j=1}^{k} \hat L_j, \qquad
\widehat{\mathrm{se}} = \frac{\mathrm{sd}(\hat L_j)}{\sqrt{k}} .$$

For $k = n$ this is **leave-one-out**, which is nearly unbiased but has high
variance and cost $n$ fits. Five or ten folds are the usual compromise: the
bias from training on less data is small, and the $k$ estimates can be
averaged.

**What the spread means.** The $k$ fold estimates are **not independent**, because
their training sets overlap. The naive standard error
$\mathrm{sd}(\hat L_j)/\sqrt k$ therefore understates the uncertainty; the
fold-to-fold spread should be read as a diagnostic of heterogeneity, not as a
rigorous standard error.

## 3. Splitting for dependent data

If the observations are grouped — several measurements per station, several
samples per borehole — then a random split puts sibling points in both training
and validation, and the model can memorise the group. **Grouped
cross-validation** keeps every group entirely in one fold. If the observations
are spatial or temporal, **blocked** or **forward-chaining** splits are needed, so
that validation is always on data later or further away than the training data.
Reporting only a random-split score for such data is the most common serious
error in applied geophysical machine learning.

## 4. Metrics

For binary classification with predicted labels and a score, the confusion counts
give

$$\text{accuracy} = \frac{TP + TN}{n}, \qquad
\text{precision} = \frac{TP}{TP + FP}, \qquad
\text{recall} = \frac{TP}{TP + FN} .$$

Accuracy is misleading under class imbalance: a classifier that always predicts
the majority class attains the base rate by construction. The **ROC AUC** ranks
all pairs of one positive and one negative and measures the probability that the
positive receives the higher score,

$$\mathrm{AUC} = \frac{\sum_{i \in \text{pos}} R_i - n_{\text{pos}}
(n_{\text{pos}}+1)/2}{n_{\text{pos}}\,n_{\text{neg}}},$$

and is threshold-free. It is insensitive to the class balance, which is both its
virtue and its danger: a good AUC can coexist with useless performance at the
operating threshold the application actually needs.

## 5. Leakage

Leakage is any path by which information about the validation target reaches the
model during fitting. It comes in three common forms:

- **Preprocessing outside the fold.** Scaling, imputation, feature selection or
  dimensionality reduction fitted on the full data use the validation points.
- **A feature derived from the target.** A proxy measured after the outcome, or a
  target-derived variable carried in the table.
- **Group or temporal dependence**, as in Section 3.

The demonstration quantifies the second and third forms. Feature selection on the
full data, on a data set with **no signal at all**, produced a validation MSE of
$0.7021$ against $1.1869$ for a leak-free pipeline — a $40.8\ \%$ apparent
improvement on pure noise. The honest estimate exceeds $1$ because selecting
features inside a small training fold adds variance; the leaked estimate is below
$1$ because it has seen the validation responses.

## 6. Worked example

The demonstration uses $120$ samples and $8$ predictors with two true non-zero
coefficients, fitting ridge with penalty $1$.

**Hold-out versus $k$-fold.**

| scheme | MSE |
|---|---|
| single hold-out of $30$ points | $0.1177$ |
| 5-fold cross-validation | $0.2080 \pm 0.0669$ |
| fold values | $0.1253, 0.2794, 0.1556, 0.2644, 0.2155$ |

The hold-out of $0.1177$ is **$43\ \%$ below** the cross-validated mean of
$0.2080$ — a single lucky split. The fold spread of $0.0669$ is the evidence
that the hold-out cannot be trusted on its own, and it is nearly a third of the
mean.

**Classification metrics.**

| quantity | value |
|---|---|
| TP, FP, FN, TN | $151$, $0$, $18$, $331$ |
| accuracy | $0.9640$ |
| precision | $1.0000$ |
| recall | $0.8935$ |
| base rate | $0.3380$ |
| ROC AUC | $1.0000$ |

The threshold used was conservative: nothing false was flagged (precision
$1.0000$) at the cost of missing $18$ true positives (recall $0.8935$). The AUC
of $1.0000$ says the *score* separates the classes perfectly — the losses are
purely a threshold choice, which is precisely the distinction between ranking
quality and operating performance.

**Leakage.** On data with **no signal**, a leak-free pipeline scores
$1.1869$ and a leaked one $0.7021$. The lesson is not that $0.7021$ is good; it
is that the number is meaningless. Since the true expected MSE is $1.0$ (the
noise variance), any result below $1.0$ on this data set is a demonstration of
leakage.

## Assumptions and regime of validity

1. **Exchangeability between validation and deployment.** If future data come
   from a different distribution, no split estimates the deployment error.
2. **Independence of folds.** Groups, spatial proximity and time ordering break
   it; use grouped or blocked splits.
3. **The whole pipeline must be inside the fold.** Scaling, selection,
   imputation and tuning.
4. **The metric must match the decision.** Accuracy for balanced labels, AUC for
   ranking, precision or recall for asymmetric costs.
5. **The fold spread is not a rigorous standard error.** Overlapping training
   sets make the folds dependent.
6. **Repeated splits are cheap insurance.** Report the distribution over several
   partitions, not a single number.

## The honest summary

Validation exists to estimate a quantity the training data cannot see, and the
demonstration shows how easily the estimate is corrupted. A single hold-out came
out $43\ \%$ below the cross-validated mean; a leak-free pipeline scored $1.1869$
and a leaking one $0.7021$ on data with no signal whatever; and a classifier with
an AUC of $1.0000$ still missed $18$ of $169$ positives at its chosen threshold.
What a validation score does **not** estimate is performance on data drawn
differently from the validation set, which is exactly the situation in
geophysics when a model trained in one basin is applied in another.

## Python demonstration

[`code/model_assessment_demo.py`](./code/model_assessment_demo.py) prints every
number quoted above. It:

1. compares a hold-out estimate with 5-fold cross-validation;
2. computes a confusion matrix, accuracy, precision, recall and the ROC AUC;
3. measures the inflation produced by selecting features on the full data.

```bash
cd 21-statistics-bayesian-ml/04-machine-learning-fundamentals/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python model_assessment_demo.py
```

It runs in about half a second and prints only text.

## Exercises

Graded problems are in
[`exercises/03-model-assessment-exercises.md`](./exercises/03-model-assessment-exercises.md)
with worked solutions in
[`exercises/03-model-assessment-solutions.md`](./exercises/03-model-assessment-solutions.md).

## Mastery checkpoint

Without notes, a single hold-out gives MSE $0.1177$, 5-fold cross-validation
gives $0.2080 \pm 0.0669$, and a leak-free pipeline scores $1.1869$ against
$0.7021$ for a pipeline that selects features on the full data.

1. Compute the percentage by which the hold-out understates the cross-validated
   error and state the likely cause.
2. Compute the ratio of the fold spread to the mean and state what it implies for
   a single-split report.
3. State the true expected MSE of the leak experiment and what that makes of both
   numbers.
4. State the splitting scheme you would use for data from $20$ stations with $40$
   records each, and why.

## Common pitfalls

1. **Reporting one hold-out as the model's error.** It is one draw; the fold
   spread here was $32\ \%$ of the mean.
2. **Fitting preprocessing on the full data.** It leaks and inflates the score.
3. **Trusting an AUC without the operating point.** Perfect ranking can coexist
   with a poor threshold.
4. **Random splitting of grouped data.** Siblings in both folds inflate the
   score.
5. **Comparing models on different splits.** The comparison then measures the
   split.
6. **Reading a leaked score as skill.** On noise, the leaked pipeline beat the
   honest one by $40.8\ \%$.

## Where this is used

- **Seismic phase picking**: grouped by event, not by window, so the same event
  does not appear in training and validation.
- **Facies prediction**: blocked by well, and ideally by field.
- **Prospectivity mapping**: spatial blocking, because neighbouring cells are not
  independent.
- **Climate emulation**: forward-chaining in time, never a random split.
- **Any published result**: the split, the metric and the threshold belong in the
  report.

## Related lessons

- [21-04-02 Bias-Variance Trade-Off, Underfitting and Overfitting](02-bias-variance.md) —
  why the validation error has a minimum at all.
- [21-04-06 Feature Engineering for Earth Data](06-feature-engineering.md) —
  where leakage most often enters.
- [21-01-03 Resampling: Bootstrap, Jackknife, Permutation Tests](../01-statistics-in-practice/03-resampling.md) —
  the resampling theory of the estimate.
- [21-06-09 Pitfalls: Spurious Correlations, Non-Stationarity, Extrapolation](../06-ml-in-geophysics/09-ml-pitfalls-geophysics.md) —
  the deployment failures this lesson guards against.
- [21-09-01 Statistical Reproducibility, p-Hacking and Multiple Comparisons](../09-ethical-and-responsible-analytics/01-reproducibility-statistical.md) —
  the reporting standards.

## Self-assessment checklist

- [ ] I can compute a hold-out and a $k$-fold estimate.
- [ ] I can explain the fold spread and its limits.
- [ ] I can compute accuracy, precision, recall and the AUC.
- [ ] I can name three forms of leakage and detect them.
- [ ] I can choose a split for grouped, spatial and temporal data.
- [ ] I can state what a validation score does not estimate.
