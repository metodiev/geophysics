# Solutions — 21-04-04 Regularisation: Ridge, Lasso, Early Stopping

> Read after attempting. Lesson:
> [04 Regularisation](../04-regularization-ml.md). Numbers quoted from the
> demonstration reproduce its output.

---

## ★1 — The two objectives

$$\hat\beta_{\text{ridge}} = \arg\min_\beta \|\mathbf y - X\beta\|^{2}
+ \lambda\|\beta\|_2^{2}, \qquad
\hat\beta_{\text{lasso}} = \arg\min_\beta \|\mathbf y - X\beta\|^{2}
+ \lambda\|\beta\|_1 .$$

Geometrically, the ridge constraint region is a **ball** (smooth, no corners) and
the lasso region is a **diamond** (a polytope with corners on the axes). Minimising
a smooth convex objective over a polytope generically lands on a **vertex** for a
range of penalties, and the vertices of the $\ell_1$ diamond have many zero
coordinates. Hence the exact zeros.

---

## ★2 — Retention fractions at $\lambda = 1000$

$$\frac{0.1372}{2.0} = 0.0686, \qquad
\frac{-0.0723}{-1.5} = 0.0482 .$$

Only $6.9\ \%$ and $4.8\ \%$ of the true coefficients remain. The shrinkage factor
in an orthonormal design is $\sigma_j^{2}/(\sigma_j^{2}+\lambda)$, so as
$\lambda \to \infty$ every coefficient tends to zero and the estimator becomes the
null model — the prediction is the mean of the training target. Ridge therefore
has no limiting model other than "nothing", which is why the CV curve eventually
turns up sharply (Section ★★6).

---

## ★3 — Sparsity at $\lambda = 0.20$

$$5 \text{ non-zero of } 20 \text{ total} = 25\ \% \text{ retained},
\quad 75\ \% \text{ eliminated}.$$

The penalty's model is that exactly **five** predictors matter. In the
demonstration the truth is four, so the lasso at this penalty is over-selecting by
one — a noise predictor that happens to correlate with the target in this sample
of $60$. At $\lambda = 0.50$ the count is four, matching the truth. This is the
usual behaviour of a selection method: the selected set is a function of the
sample, and reporting a single selected set without its sensitivity to the penalty
overstates the certainty of the selection.

---

## ★★4 — Deriving ridge

Differentiate $J(\beta) = \|\mathbf y - X\beta\|^{2} + \lambda\beta^{\mathsf T}\beta$:

$$\nabla J = -2X^{\mathsf T}(\mathbf y - X\beta) + 2\lambda\beta = 0
\;\Longrightarrow\;
(X^{\mathsf T}X + \lambda I)\hat\beta = X^{\mathsf T}\mathbf y .$$

The matrix $X^{\mathsf T}X$ has eigenvalues $\sigma_j^{2} \ge 0$ in the directions
of its right singular vectors $v_j$; adding $\lambda I$ shifts every eigenvalue to
$\sigma_j^{2} + \lambda \ge \lambda > 0$. Three consequences:

- the penalised matrix is **always invertible**, so ridge is defined when $p > n$
  and $X^{\mathsf T}X$ is singular;
- the condition number is bounded by
  $(\sigma_{\max}^{2}+\lambda)/(\sigma_{\min}^{2}+\lambda)$, which improves as
  $\lambda$ grows;
- in the singular directions, where the data say nothing, the estimate is pulled
  to zero rather than blowing up — which is the mechanism by which the prior
  supplies the missing information.

---

## ★★5 — Soft thresholding

$$\hat\beta_j = \operatorname{sign}(b_j)\max(|b_j| - \lambda/2,\ 0),
\qquad \lambda = 1.0 \Rightarrow \lambda/2 = 0.5 .$$

- $b = 3.0$: $3.0 - 0.5 = 2.5$, sign $+$ → $\hat\beta = +2.5$.
- $b = 1.2$: $1.2 - 0.5 = 0.7$, sign $+$ → $\hat\beta = +0.7$.
- $b = -0.4$: $|b| = 0.4 < 0.5$ → $\hat\beta = 0$.
- $b = 0.0$: $\hat\beta = 0$.

**Two coefficients are selected** and two are eliminated. Note that the retained
ones are also shrunk — by $0.5$ each — so the lasso is doing bias-inducing
shrinkage *and* selection at the same time, which is why its estimates are biased
even for the coefficients it keeps.

---

## ★★6 — Cost of misspecifying the penalty

**Under-penalised** ($\lambda = 0.001$):

$$\frac{0.3817 - 0.3647}{0.3647} = \frac{0.0170}{0.3647} = +4.66\ \% .$$

**Over-penalised** ($\lambda = 100$):

$$\frac{4.3196 - 0.3647}{0.3647} = \frac{3.9549}{0.3647} = +1084\ \% .$$

The two directions of error are not symmetric: under-penalising by three orders of
magnitude costs $4.7\ \%$, while over-penalising by a factor of $75$ costs
$1084\ \%$. The CV curve is **flat on the low-penalty side and steep on the high
side**, so the practical rule is to err towards too little penalty, and the honest
report quotes the curve rather than a single $\lambda$.

---

## ★★★7 — Ridge, lasso and elastic net versus predictor correlation

**Design.** $n = 60$ samples, $p = 20$ predictors generated in groups: four active
predictors, each paired with $1$–$2$ correlated companions with correlation
$\rho \in \{0, 0.3, 0.6, 0.9, 0.99\}$, plus noise predictors. Target
$y = X\beta_{\text{true}} + \mathcal N(0, 0.5^{2})$ with the four active
coefficients $(2.0, -1.5, 1.0, 0.8)$.

**Methods.** Ridge, lasso and elastic net with the mixing parameter fixed at
$\alpha = 0.5$, each with its penalty selected by an inner 5-fold
cross-validation.

**Metric.** Test MSE on $500$ independent points; and the **support recovery**,
the number of active predictors correctly selected and the number of spurious
ones.

**Replicates.** $M = 500$ data sets per $\rho$, giving a relative standard error
of about $3\ \%$ on the mean MSE.

**Prediction.** At **low correlation** lasso and elastic net select the correct
support most often (typically $> 90\ \%$ of the four) and beat ridge on MSE,
because ridge keeps all twenty coefficients with non-zero weight. At **high
correlation** lasso's support recovery collapses — with $\rho = 0.99$ it selects
one of each correlated pair essentially at random, and the identity of the
selected predictor changes with the sample — while elastic net retains the pairs
together and ridge, which never selects, is unaffected in MSE and often best. The
headline is the crossing of the two error curves between $\rho = 0.6$ and
$0.9$: selection is a low-correlation strategy.

---

## ★★★8 — Early stopping as an implicit penalty

**Design.** The demonstration's design: $60$ samples, $20$ predictors, four
active. Fit by gradient descent on the squared loss with learning rate
$\eta \in \{0.001, 0.005, 0.01, 0.05, 0.1\}$ and training-set sizes
$n_{\text{train}} \in \{25, 40, 55\}$. Record the validation MSE every iteration on
a held-out set and take the iteration minimising it.

**Metric.** The optimal stopping iteration $\hat t^{*}(\eta, n_{\text{train}})$,
the validation MSE there, and — the point of the study — the explicit ridge
penalty $\lambda^{*}$ whose solution has the same $\|\beta\|_2$ as the early-stopped
iterates.

**Relationship to be tested.** For gradient descent on a quadratic, the iterate
after $t$ steps is $\hat\beta_t = (I - (I - \eta X^{\mathsf T}X)^{t})\hat\beta_{\text{OLS}}$,
which is a shrinkage estimator whose per-direction factors are
$1 - (1-\eta\sigma_j^{2})^{t}$. Matching those factors to ridge's
$\sigma_j^{2}/(\sigma_j^{2}+\lambda)$ gives an equivalent penalty

$$\lambda_{\text{equiv}}(t) \approx \frac{1}{\eta t} \quad \text{for small } \eta t ,$$

so the stopping iteration is **inversely** proportional to an equivalent ridge
penalty. The study's headline is the measured
$\hat t^{*}$ against $\lambda_{\text{equiv}}$ on a log–log plot: a slope near
$-1$ confirms the equivalence, and the constant of proportionality carries the
$\eta$ dependence.

**Replicates.** $M = 200$ data sets per $(\eta, n_{\text{train}})$ cell, so the
median stopping iteration has a bootstrap standard error below $3\ \%$.
