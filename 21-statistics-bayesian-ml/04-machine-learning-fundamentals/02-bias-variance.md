---
id: 21-04-02
title: "Bias-Variance Trade-Off, Underfitting and Overfitting"
level: advanced
prereqs: ["21-04-01", "01-13-03"]
estimated_minutes: 55
tags: [machine-learning, bias-variance, overfitting, underfitting, model-complexity]
---

# Bias-Variance Trade-Off, Underfitting and Overfitting

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the bias-variance decomposition of the expected squared prediction
   error and **name** each of the three terms.
2. **Measure** the decomposition by Monte Carlo at a fixed model complexity.
3. **Explain** why training error decreases monotonically with complexity while
   test error does not, and **identify** the minimum.
4. **Diagnose** underfitting and overfitting from the two error curves.
5. **State** how the decomposition changes for classification and for a
   misspecified model class.
6. **State** which part of the error is reducible and which is not.

All data in this lesson are **SYNTHETIC**: a stated polynomial truth plus
Gaussian noise. No measured value is used, and the measured errors below
constrain only the demonstration's model.

## Prerequisites

- [21-04-01 ML Taxonomy: Supervised, Unsupervised, Reinforcement](01-ml-taxonomy.md) —
  the empirical-risk framework whose error this lesson decomposes.
- [01-13-03 Expectation, Variance and Moments](../../01-mathematics/13-probability-and-statistics-foundations/03-expectation-variance.md) —
  the expectation and variance being decomposed.
- [21-01-04 Linear, Multiple and Robust Regression](../01-statistics-in-practice/04-regression.md) —
  the estimator whose variance grows with the number of parameters.

## 1. Intuition: two ways to be wrong

A model can be wrong because it is **too simple** — it cannot represent the
relationship, so it is wrong on average, which is *bias* — or because it is **too
complex** — it has been fitted to the particular noise in the training sample, so
it is unstable, which is *variance*. Increasing complexity reduces bias and
increases variance, so the total error, their sum, has a minimum in between.

That minimum is not at zero complexity and not at maximum complexity. It is the
point to be found, and the two curves that locate it — training error falling
monotonically and test error U-shaped — are the single most useful diagnostic
picture in predictive modelling.

## 2. The decomposition

Let the training set $\mathcal D$ be drawn from the data-generating process, let
$\hat f_{\mathcal D}$ be the fitted model, and let $x_0$ be a test point with
$y_0 = f(x_0) + \varepsilon$, $\mathbb E[\varepsilon] = 0$,
$\operatorname{Var}\varepsilon = \sigma^{2}$. Then

$$\mathbb E_{\mathcal D, y_0}\big[(y_0 - \hat f_{\mathcal D}(x_0))^{2}\big]
= \underbrace{\big(\mathbb E_{\mathcal D}[\hat f_{\mathcal D}(x_0)] -
f(x_0)\big)^{2}}_{\text{bias}^{2}}
+ \underbrace{\operatorname{Var}_{\mathcal D}\big[\hat f_{\mathcal D}(x_0)\big]}
_{\text{variance}}
+ \underbrace{\sigma^{2}}_{\text{noise}} .$$

The three terms are independent of one another and mean different things:

- **Bias²** is how far the average model over training sets is from the truth;
  it is reduced by a larger hypothesis class.
- **Variance** is how much the model moves when the training set is replaced; it
  grows with the number of parameters and the flexibility of $\mathcal F$.
- **Noise** is irreducible: no model can predict $\varepsilon$.

Only the first two are under the modeller's control, and only through the choice
of $\mathcal F$ and the regulariser.

## 3. Why training error lies

The training error is computed on the same data used to fit the parameters, so
the optimiser can reduce it by fitting noise. For a model with $p$ parameters
fitted to $n$ points by least squares,

$$\mathbb E[\text{train MSE}] = \sigma^{2}\Big(1 - \frac{p}{n}\Big), \qquad
\mathbb E[\text{test MSE}] = \sigma^{2}\Big(1 + \frac{p}{n}\Big)$$ for an
uninformative model — the $p/n$ optimism. Two consequences:

- The training error is **optimistically biased** and falls monotonically with
  $p$; it can never warn you about overfitting.
- The gap between test and train error is itself a signal: a large gap means
  variance, a small gap with high error means bias.

## 4. Worked example

The demonstration generates $y = \sin(2.5x) + 0.3x + \mathcal N(0, 0.3^{2})$ on
$x \in [-1, 1]$, fits polynomial models in a Legendre basis to $25$ training
points, and evaluates them on $400$ test points.

**Train and test error by degree.**

| degree | train MSE | test MSE | parameters |
|---|---|---|---|
| 1 | 0.1870 | 0.1608 | 2 |
| 3 | 0.0714 | 0.1372 | 4 |
| 5 | 0.0617 | **0.1098** | 6 |
| 7 | 0.0523 | 0.6302 | 8 |
| 9 | 0.0477 | 59.1868 | 10 |
| 12 | 0.0366 | 126809.0451 | 13 |

The training error falls monotonically, exactly as the bias argument predicts.
The test error is U-shaped with a minimum of $0.1098$ at degree $5$ — close to
the truth, which needs about two harmonics — and rises by nine orders of
magnitude at degree $12$.

**The decomposition.** Averaged over a grid of $60$ evaluation points and $400$
independent training sets at degree $9$:

| term | value |
|---|---|
| bias² | 0.35657 |
| variance | 293.86961 |
| noise variance | 0.09000 |
| expected MSE | 294.31618 |
| measured test MSE | 293.49150 |

The three terms sum to $294.316$, and the measured test MSE of $293.492$ agrees
to $0.3\ \%$ — within the Monte-Carlo error of $400$ replicates with a relative
standard error of $1/\sqrt{2\times400} = 3.5\ \%$. At degree $9$ the variance
term is **$824$ times** the bias² term: an over-parameterised model is almost
entirely a variance problem.

**Across complexity.**

| degree | bias² | variance | total |
|---|---|---|---|
| 1 | 0.08275 | 0.01543 | 0.18818 |
| 3 | 0.00086 | 0.02216 | 0.11302 |
| 5 | 0.00010 | 0.07772 | 0.16781 |
| 7 | 0.00099 | 11.55342 | 11.64441 |
| 9 | 3.15432 | 816.61429 | 819.85861 |
| 12 | 72.52872 | 78031.50000 | 78104.11872 |

The bias² falls to nearly zero by degree 5 and then *rises* again — a symptom of
an ill-conditioned fit whose variance has become so large that even the average
model is far from the truth. The variance, meanwhile, is flat to degree 3 and
then explodes. The minimum total is at degree 3, a compromise between a bias² of
$0.00086$ and a variance of $0.02216$.

## Assumptions and regime of validity

1. **The decomposition assumes squared error.** For 0–1 classification the
   analogous decomposition includes an irreducible Bayes error and a term
   involving the variance of the probability estimate; the qualitative trade
   survives, the arithmetic does not.
2. **The data-generating process must be fixed.** If the target relationship
   changes between training and test, no decomposition applies.
3. **The training sets must be independent draws.** Resampling the same training
   set does not estimate the variance of the estimator.
4. **The model class must contain a good approximation, or bias² dominates.**
   With a misspecified class the bias cannot be reduced by more data.
5. **Complexity is not only parameter count.** Regularisation, early stopping and
   ensembling all change effective complexity without changing $p$.
6. **Selection on the test set destroys the estimate.** Choosing the degree by
   the test error makes the reported minimum optimistic; use validation data or
   cross-validation.

## The honest summary

Every predictive model trades bias against variance, and the trade is measurable.
In the demonstration the training error fell monotonically from $0.1870$ to
$0.0366$ while the test error rose from $0.1098$ at degree 5 to $1.27\times10^{5}$
at degree 12; a Monte-Carlo decomposition at degree 9 attributed $293.87$ of the
$294.32$ total to variance and $0.36$ to bias². The gap between the two curves is
therefore not a technicality but the entire content of model selection, and the
training error can never reveal it. What the demonstration does **not** establish
is that a U-shaped test curve with a minimum always exists: with a misspecified
model class the bias never vanishes, and the best achievable error is then set by
the class, not by the noise.

## Python demonstration

[`code/bias_variance_demo.py`](./code/bias_variance_demo.py) prints every number
quoted above. It:

1. tabulates train and test MSE against polynomial degree;
2. performs a Monte-Carlo bias-variance decomposition at degree 9;
3. repeats the decomposition across degrees.

```bash
cd 21-statistics-bayesian-ml/04-machine-learning-fundamentals/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python bias_variance_demo.py
```

It runs in about two tenths of a second and prints only text.

## Exercises

Graded problems are in
[`exercises/02-bias-variance-exercises.md`](./exercises/02-bias-variance-exercises.md)
with worked solutions in
[`exercises/02-bias-variance-solutions.md`](./exercises/02-bias-variance-solutions.md).

## Mastery checkpoint

Without notes, a degree-9 polynomial fit to $25$ points gives bias² $= 0.35657$,
variance $= 293.86961$ and noise variance $0.09000$, for an expected MSE of
$294.31618$.

1. State the fraction of the expected error contributed by each term.
2. Compute the expected training MSE from $\sigma^{2}(1 - p/n)$ with $p = 10$ and
   $n = 25$, and compare it with the measured $0.0477$.
3. State which term more data would reduce, and which it would not.
4. A colleague reports the degree-12 test error as evidence that the model is
   "more accurate on the training set". State the error in that inference.

## Common pitfalls

1. **Selecting a model by its training error.** It falls monotonically and cannot
   detect overfitting.
2. **Reading a small gap as a good model.** A biased model can be consistently
   wrong on both sets.
3. **Attributing the whole test error to variance.** At low complexity the bias
   dominates, and adding parameters helps.
4. **Choosing the complexity on the test set.** The reported minimum becomes
   optimistic; use cross-validation.
5. **Assuming more data fixes everything.** It reduces variance, not bias; a
   misspecified class stays wrong.
6. **Ignoring ill-conditioning.** At degree 12 the variance reached
   $7.8\times10^{4}$ from numerical as well as statistical instability.

## Where this is used

- **Choosing model complexity**: polynomial degree, network width, tree depth,
  number of basis functions.
- **Regularisation strength**: the penalty trades bias for variance explicitly.
- **Ensembling**: bagging reduces variance, boosting reduces bias.
- **Survey design**: more data reduce variance, better features or a better model
  class reduce bias.
- **Reporting**: a learning curve separates the two failure modes for a reader.

## Related lessons

- [21-04-04 Regularisation: Ridge, Lasso, Early Stopping](04-regularization-ml.md) —
  the explicit control of the trade.
- [21-04-03 Cross-Validation, Metrics and the Danger of Leakage](03-model-assessment.md) —
  how the test error is estimated honestly.
- [21-04-05 Decision Trees, Random Forests and Gradient Boosting](05-trees-and-ensembles.md) —
  bagging and boosting as the two directions of the trade.
- [21-02-05 Geostatistics Combined with Geophysical Inversion](../02-geostatistics/05-geostatistics-inversion.md) —
  the same bias-variance balance in a prior.
- [21-03-05 Variational Inference and Scalable Bayes](../03-bayesian-inference/05-variational-inference.md) —
  an approximation whose error is a bias-variance choice too.

## Self-assessment checklist

- [ ] I can derive the bias-variance decomposition.
- [ ] I can compute the $p/n$ optimism of a training error.
- [ ] I can read underfitting and overfitting from two error curves.
- [ ] I can measure the decomposition by Monte Carlo.
- [ ] I can state which terms more data and a larger class affect.
- [ ] I can say why the decomposition is different for classification.
