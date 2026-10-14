---
id: 21-04-04
title: "Regularisation: Ridge, Lasso, Early Stopping"
level: advanced
prereqs: ["21-04-02", "21-04-03"]
estimated_minutes: 60
tags: [machine-learning, regularization, ridge, lasso, early-stopping, sparsity]
---

# Regularisation: Ridge, Lasso, Early Stopping

## Learning objectives

By the end of this lesson you will be able to:

1. **Write** the ridge and lasso objectives and **state** the geometric reason
   one shrinks smoothly while the other produces exact zeros.
2. **Compute** ridge and lasso solutions for a stated penalty and **interpret**
   the coefficient paths.
3. **Select** a penalty by cross-validation and **state** how flat the optimum is.
4. **Explain** early stopping as an implicit regulariser and **identify** the
   stopping iteration from validation error.
5. **Relate** the penalties to Gaussian and Laplace priors, and **state** what
   each prior asserts.
6. **Diagnose** the failure modes: collinear predictors, a penalty too large, and
   selection performed outside the fold.

All data in this lesson are **SYNTHETIC**: $60$ samples with $20$ predictors of
which four are active. No measured value is used.

## Prerequisites

- [21-04-02 Bias-Variance Trade-Off, Underfitting and Overfitting](02-bias-variance.md) —
  the trade that regularisation controls.
- [21-04-03 Cross-Validation, Metrics and the Danger of Leakage](03-model-assessment.md) —
  the procedure that chooses the penalty.
- [21-01-04 Linear, Multiple and Robust Regression](../01-statistics-in-practice/04-regression.md) —
  the least-squares estimator being penalised.

## 1. Intuition: pay for a smaller model with a bigger bias

Regularisation adds a term to the loss that penalises the size of the
coefficients. Because the loss now trades fit against size, the fitted
coefficients are smaller than least squares would give, and smaller coefficients
mean less variance at the cost of some bias. That is the whole idea: the penalty
is a knob that moves the model along the bias-variance curve of
[21-04-02](02-bias-variance.md).

The two classical penalties differ in the shape of the constraint they impose:

$$\hat\beta_{\text{ridge}} = \arg\min_\beta \|\mathbf y - X\beta\|^{2}
+ \lambda\|\beta\|_2^{2}, \qquad
\hat\beta_{\text{lasso}} = \arg\min_\beta \|\mathbf y - X\beta\|^{2}
+ \lambda\|\beta\|_1 .$$

Ridge constrains the coefficients to a ball; the solution is a smooth shrinkage
of the least-squares solution and no coefficient is ever set exactly to zero.
Lasso constrains them to a diamond; the optimum of a quadratic objective over the
corners of a diamond lands **on a corner** for a whole range of penalties, which
is why it produces exact zeros and therefore selects predictors.

## 2. The closed form for ridge

Setting the gradient to zero gives the linear system

$$(X^{\mathsf T}X + \lambda I)\hat\beta = X^{\mathsf T}\mathbf y
\;\Longrightarrow\;
\hat\beta = (X^{\mathsf T}X + \lambda I)^{-1}X^{\mathsf T}\mathbf y .$$

The penalty adds a constant to every eigenvalue of $X^{\mathsf T}X$, so it
conditions the problem: as $\lambda$ grows the solution tends to zero, and the
condition number of the penalised matrix is bounded by
$(\sigma_{\max}^{2}+\lambda)/(\sigma_{\min}^{2}+\lambda)$. That is why ridge
remains well defined when $X^{\mathsf T}X$ is singular — the case with more
predictors than samples — and why it is the default for collinear designs.

The solution can also be written as a shrunken projection,
$\hat\beta = V\operatorname{diag}\big(\sigma_i^{2}/(\sigma_i^{2}+\lambda)\big)
V^{\mathsf T}\hat\beta_{\text{OLS}}$: each principal direction of the design is
shrunk by a factor that is close to one for well-determined directions and close
to zero for poorly determined ones. Ridge therefore suppresses exactly the
directions the data constrain least.

## 3. Why lasso gives exact zeros

The lasso solution has a soft-threshold form for an orthonormal design,

$$\hat\beta_j = \operatorname{sign}(\hat\beta_j^{\text{OLS}})
\max\big(|\hat\beta_j^{\text{OLS}}| - \lambda/2,\ 0\big),$$

so every coefficient below the threshold is set **exactly** to zero. The
geometric reason is the corner of the $\ell_1$ ball: minimising a smooth convex
function over a polytope generically lands on a vertex, and a vertex has many zero
coordinates. The statistical reason is the prior: an
$\ell_2$ penalty is a maximum-a-posteriori estimate with a Gaussian prior
$\beta_j \sim \mathcal N(0, \tau^{2})$, an $\ell_1$ penalty corresponds to a
Laplace prior, whose sharp peak at zero makes zero the single most probable value.

## 4. Choosing the penalty and stopping early

The penalty is selected by cross-validating the **whole pipeline**, including the
standardisation of predictors, on a grid of $\lambda$ values. Two practical
points matter more than the arithmetic:

- **The curve is flat near its minimum.** A penalty wrong by a factor of two or
  three usually costs little; wrong by two orders of magnitude costs a lot. Report
  the chosen value and the shape of the curve.
- **Penalised scales matter.** The penalty is not scale-invariant, so predictors
  must be standardised before a common $\lambda$ is applied; otherwise the penalty
  is a different constraint on each predictor.

**Early stopping** is a third regulariser with no explicit penalty. Iterative
fitting reduces training error monotonically and passes through a sequence of
increasingly complex effective models; stopping at the iteration that minimises
validation error is equivalent to an $\ell_2$-like penalty whose strength
decreases with the number of iterations. It costs nothing extra because the
validation curve is being computed anyway.

## 5. Worked example

The demonstration fits $60$ samples with $20$ predictors, of which four have
non-zero true coefficients $(2.0, -1.5, 1.0, 0.8)$.

**Ridge paths.** Selected values of $\lambda$:

| $\lambda$ | $\|\beta\|^{2}$ | $\beta_0$ | $\beta_3$ | $\beta_7$ | $\beta_{12}$ |
|---|---|---|---|---|---|
| 0.01 | 7.6661 | 1.8893 | $-1.5735$ | 0.9822 | 0.7403 |
| 1.00 | 7.3740 | 1.8600 | $-1.5370$ | 0.9638 | 0.7220 |
| 10.00 | 5.4167 | 1.6362 | $-1.2760$ | 0.8250 | 0.5911 |
| 100.00 | 1.1056 | 0.7897 | $-0.4983$ | 0.3462 | 0.2078 |
| 1000.00 | 0.0317 | 0.1372 | $-0.0723$ | 0.0518 | 0.0254 |

The shrinkage is smooth and monotone and **no coefficient ever reaches zero** —
at $\lambda = 1000$ the four true coefficients are still $0.137$, $-0.072$,
$0.052$ and $0.025$. Ridge cannot remove a predictor.

**Lasso paths.**

| $\lambda$ | non-zero | $\beta_0$ | $\beta_3$ | $\beta_7$ | $\beta_{12}$ | support |
|---|---|---|---|---|---|---|
| 0.01 | 18 | 1.8889 | $-1.5637$ | 0.9724 | 0.7451 | 4/4 |
| 0.05 | 11 | 1.8709 | $-1.5252$ | 0.9398 | 0.7425 | 4/4 |
| 0.10 | 9 | 1.8506 | $-1.4720$ | 0.9036 | 0.7200 | 4/4 |
| 0.20 | 5 | 1.8136 | $-1.4034$ | 0.8429 | 0.6699 | 4/4 |
| 0.50 | 4 | 1.6966 | $-1.2330$ | 0.6703 | 0.4892 | 4/4 |

The non-zero count falls from $18$ to $4$ — the model **selects** predictors — and
the four true ones are retained at every penalty tested. The remaining non-zeros
at small $\lambda$ are noise predictors that happen to correlate with the target
in this sample, and they disappear as the penalty grows.

**Cross-validation.** Over a grid from $10^{-3}$ to $10^{2}$, the best ridge
penalty is $\lambda = 1.3335$ with a CV MSE of $0.3647$, against $0.3817$ at
$\lambda = 0.001$ and $4.3196$ at $\lambda = 100$. The penalty is therefore chosen
comfortably inside the flat region: the curve varies by only $4.5\ \%$ between
$\lambda = 0.001$ and the optimum, and by a factor of $11.8$ from the optimum to
the over-penalised end. Missing the optimum by a factor of three costs
essentially nothing; over-penalising by two orders of magnitude costs
$11.8\times$.

**Early stopping.** Training on $25$ samples with all $20$ predictors:

| iteration | train MSE | validation MSE |
|---|---|---|
| 1 | 4.6381 | 7.1271 |
| 100 | 0.0885 | 1.4940 |
| 3000 | 0.0144 | 2.0911 |

The best validation MSE is $0.9180$ at iteration $363$. Training error continues
to fall to $0.0144$ — a factor of $64$ below the validation error — while
validation error has more than doubled since its minimum. Early stopping at
iteration $363$ is the regularisation, and it is free because the validation curve
was already being computed.

## Assumptions and regime of validity

1. **The predictors must be standardised** before a common penalty is meaningful.
2. **The penalty is not scale-free in $n$.** With more data the same $\lambda$
   shrinks less; the useful quantity is the ratio of the penalty to the data term.
3. **Lasso selection is unstable under collinearity.** When two predictors carry
   the same information, lasso picks one arbitrarily; the **elastic net**
   ($\ell_1 + \ell_2$) is the standard remedy.
4. **The penalty must be chosen inside the fold.** Selecting $\lambda$ on the full
   data leaks, as in [21-04-03](03-model-assessment.md) §5.
5. **Early stopping needs a validation signal.** Without one there is no stopping
   criterion but a fixed budget.
6. **Regularisation is a modelling choice, not a numerical detail.** The penalty
   asserts something about the coefficients' prior, and the assertion applies
   whether or not it is true.

## The honest summary

Regularisation is the operational form of the bias-variance trade, and the
demonstration measures both of its main forms. Ridge shrank every coefficient
smoothly and never produced a zero, taking $\|\beta\|^{2}$ from $7.67$ to $0.03$
over five decades of penalty; lasso drove the non-zero count from $18$ to $4$,
recovering the four true predictors at every penalty tested. The cross-validated
optimum was flat — a factor-of-three error in $\lambda$ cost a few per cent — and
early stopping found a validation minimum at iteration $363$ while the training
error kept falling to $0.0144$. What the numbers do **not** establish is that the
selected predictors are the *causally* relevant ones: selection finds predictors
that predict, and with collinear features the choice among them is arbitrary.

## Python demonstration

[`code/regularization_ml_demo.py`](./code/regularization_ml_demo.py) prints every
number quoted above. It:

1. computes ridge paths over five decades of penalty;
2. computes lasso paths and the non-zero count;
3. selects the ridge penalty by 5-fold cross-validation;
4. runs gradient descent with early stopping.

```bash
cd 21-statistics-bayesian-ml/04-machine-learning-fundamentals/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python regularization_ml_demo.py
```

It runs in about a fifth of a second and prints only text.

## Exercises

Graded problems are in
[`exercises/04-regularization-ml-exercises.md`](./exercises/04-regularization-ml-exercises.md)
with worked solutions in
[`exercises/04-regularization-ml-solutions.md`](./exercises/04-regularization-ml-solutions.md).

## Mastery checkpoint

Without notes, a ridge fit at $\lambda = 1000$ retains $\beta_0 = 0.1372$ and
$\beta_3 = -0.0723$ where the truth is $2.0$ and $-1.5$; a lasso at
$\lambda = 0.20$ has $5$ non-zeros; and early stopping halts at iteration $363$
with validation MSE $0.9180$.

1. Compute the fraction of each ridge coefficient retained at $\lambda = 1000$.
2. State why ridge cannot produce the lasso's five-non-zero solution.
3. Compute the ratio of the final training MSE ($0.0144$) to the validation MSE
   at the stopping point, and interpret it.
4. State what the lasso's five non-zeros at $\lambda = 0.20$ imply about how many
   predictors the penalty believes are active.

## Common pitfalls

1. **Penalising unstandardised predictors.** The penalty then differs per
   predictor and the comparison is meaningless.
2. **Choosing $\lambda$ on the full data.** Leakage, and an optimistic score.
3. **Reading lasso's selection as causal.** Selection finds predictors, not
   causes, and is unstable under collinearity.
4. **Over-penalising.** The CV curve is flat near its optimum but steep at the
   over-penalised end, where the CV MSE rose from $0.3647$ to $4.3196$.
5. **Stopping gradient descent at a fixed iteration.** The stopping point is a
   property of the data, not of the schedule.
6. **Assuming ridge reduces variance only.** It adds a bias that must be measured
   against the variance saved.

## Where this is used

- **Ill-posed inversion**: Tikhonov regularisation is ridge with a general
  operator; see [18-03-02](../../18-inverse-problems/03-regularization/02-tikhonov.md).
- **Sparse reflectivity**: $\ell_1$ penalties recover sparse spike trains.
- **High-dimensional petrophysics**: more logs than samples, where ridge is the
  default and lasso selects.
- **Neural-network training**: weight decay is ridge and early stopping is
  ubiquitous.
- **Prospectivity mapping**: elastic net over hundreds of correlated evidence
  layers.

## Related lessons

- [21-04-02 Bias-Variance Trade-Off, Underfitting and Overfitting](02-bias-variance.md) —
  the curve the penalty moves along.
- [21-04-03 Cross-Validation, Metrics and the Danger of Leakage](03-model-assessment.md) —
  the fold discipline the penalty selection needs.
- [21-03-02 Conjugate Priors and Analytic Posteriors](../03-bayesian-inference/02-conjugate-priors.md) —
  the priors behind the penalties.
- [18-03-02 Tikhonov Regularisation and the Smoothing Trade-Off](../../18-inverse-problems/03-regularization/02-tikhonov.md) —
  the same mathematics from inverse theory.
- [21-05-01 Neural Networks: Architecture, Activation, Backpropagation](../05-deep-learning/01-neural-networks.md) —
  where weight decay and early stopping are standard.

## Self-assessment checklist

- [ ] I can write the ridge and lasso objectives and solve ridge in closed form.
- [ ] I can explain why lasso produces exact zeros.
- [ ] I can select a penalty by cross-validation and read the curve.
- [ ] I can relate each penalty to a prior.
- [ ] I can identify a stopping iteration from a validation curve.
- [ ] I can name the failure modes and their remedies.
