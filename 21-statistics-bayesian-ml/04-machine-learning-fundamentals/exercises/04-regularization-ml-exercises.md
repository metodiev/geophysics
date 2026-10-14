# Exercises — 21-04-04 Regularisation: Ridge, Lasso, Early Stopping

Attempt these before reading the
[solutions](./04-regularization-ml-solutions.md). The lesson is
[04 Regularisation](../04-regularization-ml.md). All data are **SYNTHETIC**.

## ★ Foundational

**★1.** Write the ridge and lasso objectives and state the geometric reason one
produces exact zeros.

**★2.** At $\lambda = 1000$ the ridge coefficients are $0.1372$ and $-0.0723$
where the truth is $2.0$ and $-1.5$. Compute the fraction of each retained and
state what happens to the estimator as $\lambda \to \infty$.

**★3.** A lasso at $\lambda = 0.20$ has five non-zero coefficients out of twenty.
Compute the sparsity and state how many predictors the penalty believes are
active.

## ★★ Applied

**★★4.** Derive the ridge solution from the penalised normal equations and show
that the penalty adds a constant to every eigenvalue of $X^{\mathsf T}X$. State
the consequence for a singular design.

**★★5.** Using $\hat\beta_j = \operatorname{sign}(b_j)\max(|b_j| - \lambda/2, 0)$
for an orthonormal design with least-squares estimates $b_j$, compute the lasso
solution for $b = (3.0, 1.2, -0.4, 0.0)$ and $\lambda = 1.0$, and state which
coefficients are selected.

**★★6.** The demonstration's cross-validation gives CV MSE $0.3817$ at
$\lambda = 0.001$, $0.3647$ at the optimum $\lambda = 1.3335$ and $4.3196$ at
$\lambda = 100$. Compute the percentage penalty for each of these two
misspecifications and state which direction of error is more costly.

## ★★★ Research-oriented

**★★★7.** Specify an experiment comparing ridge, lasso and elastic net on the
demonstration's design as a function of the correlation between predictors. State
the design, the metric, the replicate count, and the predicted ordering at low and
high correlation. A specification that could not be executed is a failed answer.

**★★★8.** Design a study of **early stopping as an implicit penalty**: an
experiment that measures the validation-optimal stopping iteration as a function
of the learning rate and the training-set size, and states the equivalence between
stopping iteration and an explicit $\ell_2$ penalty.
