---
id: 18-06-04
title: "Surrogate Models and Polynomial Chaos for UQ"
level: research
prereqs: ["18-06-03", "18-06-02"]
tags: [inverse-problems, uncertainty-quantification, surrogate-models, polynomial-chaos, spectral-methods]
---

# Surrogate Models and Polynomial Chaos for UQ

All models in this module are **SYNTHETIC**. The two test models below are analytic
functions chosen so that their variance decompositions are known exactly, which is
what allows the surrogate to be scored. Every number quoted is printed by
[`code/surrogate_uq_demo.py`](./code/surrogate_uq_demo.py).

## Learning objectives

By the end of this lesson you will be able to:

1. **Construct** a polynomial chaos expansion in a basis that is orthonormal with
   respect to the input measure, and **explain** why the choice of measure fixes the
   basis.
2. **Derive** the mapping from expansion coefficients to mean, variance and Sobol
   indices, and **state** the conditions under which it is exact.
3. **Demonstrate** that a surrogate truncated one degree short does not merely lose
   accuracy but reports a wrong sensitivity ranking.
4. **Validate** a surrogate on a held-out set, and **distinguish** surrogate error
   from reference error.
5. **Measure** how accuracy depends on the polynomial degree, the training size and
   the conditioning of the regression.
6. **Compute** the number of forward evaluations a surrogate saves, and state the
   condition under which the saving is real.
7. **State** the regime of validity: smoothness, independence, dimension, and where
   polynomial chaos is the wrong tool.

## Prerequisites

- [18-06-03 Sensitivity Analysis: Local, Global, Sobol Indices](03-sensitivity-analysis.md)
  — the indices the surrogate is used to compute.
- [18-06-02 Monte Carlo Propagation and Its Convergence](02-monte-carlo-uq.md) —
  the sampling alternative and its cost.
- [18-05-06 Posterior Summaries](../05-bayesian-inversion/06-posterior-summary.md)
  — what the surrogate's output distribution is used for.

## 1. Intuition: replace the model with a polynomial that is cheap to evaluate

A surrogate is a cheap function fitted to a small number of expensive forward
evaluations. Uncertainty quantification needs thousands or millions of evaluations;
if the forward model is a finite-element solve, that is impossible, and a surrogate
is the standard answer.

Polynomial chaos is the surrogate of choice when the model is smooth in its inputs
and the inputs are independent. Its attraction is not only speed. The expansion is
*orthogonal* with respect to the input measure, and that orthogonality turns the
variance decomposition of lesson [03](03-sensitivity-analysis.md) into bookkeeping:
the mean is one coefficient, the variance is a sum of squares of coefficients, and
each Sobol index is a ratio of sums of squares over groups of coefficients. No extra
sampling, no extra estimator, no extra error.

The price is the usual one for spectral methods: the expansion converges fast for
smooth models and slowly for models with kinks, discontinuities or sharp thresholds,
and the number of basis terms grows combinatorially with dimension unless the
expansion is truncated by total degree, by sparsity, or by the structure of the
model.

## 2. The expansion, and the basis the measure dictates

For independent inputs $x_i$ with probability densities $\rho_i$, expand

$$
f(x) \approx \sum_{\alpha \in \mathcal{A}} c_\alpha \Psi_\alpha(x),
\qquad
\Psi_\alpha(x) = \prod_{i=1}^{d} \psi_{\alpha_i}(x_i),
$$

where the univariate functions are orthonormal with respect to the input measure,

$$
\int \psi_m(x)\,\psi_n(x)\,\rho_i(x)\,\mathrm{d}x = \delta_{mn}.
$$

The measure fixes the basis. Gaussian inputs give Hermite polynomials; uniform
inputs give Legendre; beta inputs give Jacobi. Choosing the wrong family is not a
small error: orthogonality fails, the coefficient squares are no longer variances,
and the indices computed from them are meaningless.

**A worked normalisation.** For $x \sim \mathcal{U}[0,1]$ mapped to
$\xi = 2x - 1 \sim \mathcal{U}[-1,1]$, the measure is $\mathrm{d}\xi/2$. Legendre
polynomials satisfy $\int_{-1}^{1}P_n^2\,\mathrm{d}\xi = 2/(2n+1)$, so the
orthonormal functions are

$$
\psi_n(\xi) = \sqrt{2n+1}\;P_n(\xi).
$$

An easy error is to drop the $\sqrt{2n+1}$ and use $P_n$ directly. That basis is
orthogonal but not normalised, and every coefficient square is then off by a factor
$2n+1$ — a mistake worth checking for explicitly, and the reason the demonstration
prints the exact variance alongside the fitted one.

## 3. From coefficients to moments and indices

With an orthonormal basis and independent inputs,

$$
\mathbb{E}[f] = c_{0}, \qquad
\operatorname{Var}(f) = \sum_{\alpha \ne 0} c_\alpha^2,
$$

and for a total-degree truncation $\mathcal{A} = \{\alpha : \lvert\alpha\rvert \le
p\}$,

$$
S_i = \frac{\sum_{\alpha \in \mathcal{A},\, \alpha_i > 0,\, \lvert\alpha\rvert_0 = 1}
c_\alpha^2}{\operatorname{Var}(f)},
\qquad
S_{Ti} = \frac{\sum_{\alpha \in \mathcal{A},\, \alpha_i > 0} c_\alpha^2}
{\operatorname{Var}(f)} .
$$

The first row of each index is the *main effect*: all coefficients that involve
$x_i$ and no other input. The total index includes every coefficient in which $x_i$
appears, which is exactly the interaction share. Nothing is estimated; these are
algebraic identities.

## 4. Worked example: exactness, and the cost of one degree short

The demonstration first fits a surrogate to model A,

$$
f(x) = 10\,(x_1-0.5)^2 + x_2 + 0.5\,x_3, \qquad x_i \sim \mathcal{U}[0,1],
$$

whose exact variance is $0.659722$ and whose exact indices are
$S = (0.8421,\ 0.1263,\ 0.0316)$, all with $S_T = S$ because the model is additive.
Fitting on $512$ quasi-random training points gives

| degree | basis terms | mean | variance | $S$ | held-out RMSE |
|---|---|---|---|---|---|
| 1 | 4 | 1.58333 | 0.104167 | $(7.5\times10^{-8},\,0.800,\,0.200)$ | $7.5\times10^{-1}$ |
| 2 | 10 | 1.58333 | 0.659722 | $(0.8421,\,0.1263,\,0.0316)$ | $6.6\times10^{-15}$ |
| 3 | 20 | 1.58333 | 0.659722 | $(0.8421,\,0.1263,\,0.0316)$ | $1.3\times10^{-14}$ |
| 4 | 35 | 1.58333 | 0.659722 | $(0.8421,\,0.1263,\,0.0316)$ | $3.3\times10^{-15}$ |
| exact | — | 1.58333 | 0.659722 | $(0.8421,\,0.1263,\,0.0316)$ | $0$ |

Three things are worth extracting.

**Degree 2 is exact, at machine precision.** The model is a degree-2 polynomial in
$x_1$ and degree-1 in the others, so a total-degree-2 expansion *is* the model; the
held-out RMSE is $6.6\times10^{-15}$, which is double-precision regression residual,
not approximation error.

**Degree 1 is worse than inaccurate: it inverts the ranking.** Its variance is
$0.104167$ instead of $0.659722$ — a factor of $6.3$ too small — and it assigns
$x_1$ an index of $7.5\times10^{-8}$, effectively zero, while giving $x_2$ an index
of $0.800$. The most influential parameter is reported as irrelevant, because the
linear term in the expansion cannot represent a parabola whose mean cancels its
first-order moment. A surrogate must be validated against something before its
derived sensitivities are believed.

**The mean is exact at every degree.** The mean is the zero-order coefficient, and
a wrong degree does not bias it here. That is convenient and not general: for a
model whose mean depends on a quadratic term, as this one's does
($10\,\mathbb{E}[(x_1-0.5)^2] = 10/12$), the zero-order coefficient *absorbs* the
effect and is right, but any quantity that mixes orders will not be.

### 4.1 Where the accuracy comes from

Holding the degree at 4 and varying the training size on the same model:

| training points | conditioning of the design | held-out RMSE |
|---|---|---|
| 20 | 11.15 | $1.03\times10^{0}$ |
| 50 | 13.39 | $2.0\times10^{-15}$ |
| 100 | 3.25 | $1.7\times10^{-15}$ |
| 200 | 1.97 | $1.5\times10^{-15}$ |
| 500 | 1.31 | $3.2\times10^{-15}$ |
| 1000 | 1.15 | $1.9\times10^{-15}$ |

At $20$ points with $35$ basis functions the regression is underdetermined, and the
error is of order one; from $50$ points on, the model is reproduced to machine
precision. The conditioning number — the ratio of the largest to the smallest
singular value of the design matrix — is printed because it is the quantity that
decides whether the fitted coefficients mean anything: **a surrogate with more basis
functions than well-placed samples reports coefficients that are not identified, and
an error metric computed on the training set would not reveal it.**

## 5. A genuinely nonlinear model: convergence and its limit

Model B is smooth but not polynomial:

$$
f(x) = e^{-x_1}\left(1 + 0.5\sin(3\pi x_2)\right) + 0.3\,x_3 .
$$

A two-million-draw Monte Carlo reference gives mean $0.849205$ and variance
$0.096848$ with a Monte Carlo standard error of $0.000097$ on the variance. The
expansion, fitted to $1024$ quasi-random points, gives

| degree | basis terms | PCE variance | $\lvert\text{variance} - \text{reference}\rvert$ | held-out RMSE |
|---|---|---|---|---|
| 1 | 4 | 0.046923 | 0.049925 | $2.2\times10^{-1}$ |
| 2 | 10 | 0.064395 | 0.032452 | $1.8\times10^{-1}$ |
| 3 | 20 | 0.065767 | 0.031080 | $1.8\times10^{-1}$ |
| 4 | 35 | 0.092610 | 0.004237 | $6.5\times10^{-2}$ |
| 5 | 56 | 0.094747 | 0.002100 | $4.5\times10^{-2}$ |
| 6 | 84 | 0.096586 | 0.000261 | $1.3\times10^{-2}$ |

The expansion converges toward the reference, and at degree 6 the gap
($0.000261$) is *larger* than the Monte Carlo standard error of the reference
($0.000097$). The residual is therefore genuine truncation error, not noise in the
reference: the honest statement is that the surrogate has not yet reached the
reference's precision, and that its error must be carried alongside the UQ result.
Reporting only the PCE variance would present a $0.27\%$ underestimate as an answer.

The indices at degree 5 are

$$
S = (0.4227,\ 0.4604,\ 0.0794), \qquad
S_T = (0.4602,\ 0.4978,\ 0.0795),
$$

so $x_2$ has the largest main effect, $x_1$ has the largest interaction share
($S_{T1} - S_1 = 0.0375$), and $x_3$ is additive and modest ($S_3 = S_{T3}$ to
three decimals, as an additive term must be). Note that these indices are consistent
with the model's form: $e^{-x_1}$ and $\sin(3\pi x_2)$ multiply each other, which is
an interaction, while $x_3$ enters additively.

## 6. Cost accounting, and when the saving is real

At degree 5 with $56$ coefficients the demonstration needs $1024$ forward
evaluations to fit the surrogate. To estimate the same variance to a $1\%$ relative
standard error, direct Monte Carlo needs $N > 2/0.01^2 = 20\,000$ evaluations,
because $\operatorname{Var}(\hat V)/V^2 \approx 2/N$ for a Gaussian-like output.
The measured saving is a factor of $19.5$.

The saving is real but conditional, and the conditions are the substance of the
method:

- **The model must be smooth in the inputs.** A kinked or discontinuous response
  destroys the spectral convergence; the expansion still fits, but the error falls
  algebraically rather than exponentially, and the required degree may exceed any
  affordable cost.
- **The surrogate is only valid where it was validated.** Extrapolating outside the
  range of the training inputs is not uncertainty quantification; it is a
  polynomial evaluated where nothing constrained it.
- **The surrogate error must be propagated, not ignored.** The degree-6 gap above is
  a real bias in the reported variance.
- **The dimensionality matters.** A total-degree-$p$ expansion in $d$ dimensions has
  $\binom{p+d}{d}$ terms, so $d = 10$ and $p = 5$ already need $3003$
  coefficients. Sparse (hyperbolic-cross) truncations, adaptive bases, or a
  low-rank tensor format are the standard remedies.

## 7. Assumptions and regime of validity

1. **Independence of the inputs.** The product basis and the variance identity both
   rely on it. Correlated inputs require a Nataf or Rosenblatt transform, and the
   simple index formulas no longer apply.
2. **The basis matches the input measure.** Uniform/Legendre, Gaussian/Hermite,
   beta/Jacobi. A mismatch silently invalidates the index arithmetic.
3. **The expansion is truncated by total degree or sparsity, and the choice is
   reported.** The truncation is a modelling decision with a measurable
   consequence, as Section 4 shows.
4. **The regression is well posed.** More coefficients than well-placed samples
   gives unidentifiable coefficients; check the conditioning or the design rank.
5. **Validation is on held-out points drawn from the same measure.** An RMSE on the
   training set measures interpolation, not accuracy.
6. **The reference against which the surrogate is judged has its own error.** At
   degree 6 the residual exceeded the reference's standard error, and only printing
   both makes that visible.
7. **Uniform convergence is not implied by convergence in variance.** A surrogate
   can reproduce the variance while being wrong in a small region that matters for a
   rare-event question.

## 8. Demonstration and exercises

[`code/surrogate_uq_demo.py`](./code/surrogate_uq_demo.py) builds the orthonormal
Legendre basis, fits the expansions by least squares, computes the moment and index
mappings, and prints the validation, convergence and cost tables above. It exits $0$
in about one and a half seconds. Exercises and solutions:
[`exercises/04-surrogate-uq-exercises.md`](./exercises/04-surrogate-uq-exercises.md),
[`exercises/04-surrogate-uq-solutions.md`](./exercises/04-surrogate-uq-solutions.md).

## Mastery checkpoint

**(a)** Show that $\psi_n(\xi) = \sqrt{2n+1}P_n(\xi)$ is orthonormal with respect
to the measure $\mathrm{d}\xi/2$ on $[-1,1]$.
**(b)** For model A, compute the exact coefficient of the $(2,0,0)$ basis function
and verify that its square is $V_1 = 0.555556$.
**(c)** Explain why a degree-1 surrogate of model A reports $x_1$ as inert.
**(d)** State two conditions under which a polynomial-chaos surrogate is the wrong
tool, and one alternative for each.

## Common pitfalls

1. **Using a basis orthogonal but not normalised for the input measure.** Every
   coefficient square is then wrong by the basis norm.
2. **Fitting more coefficients than the design supports.** The measured RMSE at $20$
   points and $35$ terms is $1.03$, and the coefficients are not identified.
3. **Judging a surrogate by its training error.** Always validate on held-out points.
4. **Reporting a truncated expansion's variance as the model's.** The measured gap
   at degree 6 was $0.000261$, larger than the reference's own standard error.
5. **Assuming a smooth model without checking.** The convergence rate is the test.
6. **Ignoring dimensions in the cost.** The number of terms grows combinatorially
   with $d$.
7. **Extrapolating beyond the training range.** A polynomial extrapolates
   confidently and wrongly.

## Further reading

- **Ghanem, R. G., & Spanos, P. D. (1991). *Stochastic Finite Elements: A Spectral
  Approach*. Springer.** Level: research. Polynomial chaos as a stochastic
  finite-element basis.
- **Xiu, D., & Karniadakis, G. E. (2002). The Wiener–Askey polynomial chaos for
  stochastic differential equations. *SIAM Journal on Scientific Computing*, 24(2),
  619–644.** Level: research. The correspondence between input measures and
  polynomial families used in Section 2.
- **Sudret, B. (2008). Global sensitivity analysis using polynomial chaos
  expansions. *Reliability Engineering & System Safety*, 93(7), 964–979.** Level:
  research. The coefficient-to-index mapping of Section 3.
- **Forrester, A., Sobester, A., & Keane, A. (2008). *Engineering Design via
  Surrogate Modelling: A Practical Guide*. Wiley.** Level: research. Practical
  surrogate validation and design of experiments.

## Related modules

- [03 Sensitivity Analysis: Local, Global, Sobol Indices](03-sensitivity-analysis.md)
  — the indices read off the surrogate's coefficients.
- [02 Monte Carlo Propagation and Its Convergence](02-monte-carlo-uq.md) — the
  alternative costing a factor of about 20 more evaluations here.
- [05 Visualising and Communicating Uncertainty](05-uncertainty-visualisation.md) —
  displaying a surrogate's output distribution honestly, including its own error.
- [18-09-01 Learned Inversion: Direct and Iterative Networks](../09-machine-learning-inversion/01-learned-inversion.md)
  — neural surrogates, with the same validation obligations and weaker orthogonality.
- [18-04-02 Gradient, Gauss-Newton and Full Newton Methods](../04-nonlinear-inversion/02-gradient-and-newton.md)
  — where a surrogate gradient is used, and why its error matters.
