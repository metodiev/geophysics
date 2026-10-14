---
id: 18-06-03
title: "Sensitivity Analysis: Local, Global, Sobol Indices"
level: research
prereqs: ["18-06-02", "18-04-02"]
tags: [inverse-problems, uncertainty-quantification, sensitivity-analysis, sobol-indices, variance-decomposition]
---

# Sensitivity Analysis: Local, Global, Sobol Indices

All models in this module are **SYNTHETIC**. The test functions used here are
analytic, chosen so that their variance decompositions are known exactly and the
Monte Carlo estimators can be scored against them. Every number quoted is printed
by [`code/sensitivity_analysis_demo.py`](./code/sensitivity_analysis_demo.py).

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the Sobol' variance decomposition of a model output, and the
   definition of the first-order and total sensitivity indices.
2. **Compute** both indices for an analytic test function in closed form, using the
   conditional-expectation argument.
3. **Estimate** the indices by quasi-Monte Carlo with the Saltelli/Jansen
   estimators, and **measure** their error from independent replicates.
4. **Demonstrate** with a measured example that a local (derivative) analysis can
   rank a parameter last that the global analysis ranks first.
5. **Explain** why first-order and total indices must be reported together, and
   what their difference means.
6. **Measure** the convergence rate of the estimator and state the guarantee it
   does and does not provide.
7. **Choose** a sensitivity method for a stated purpose: ranking, factor fixing, or
   interaction detection.

## Prerequisites

- [18-06-02 Monte Carlo Propagation and Its Convergence](02-monte-carlo-uq.md) —
  the sampling machinery and its error.
- [18-04-02 Gradient, Gauss-Newton and Full Newton Methods](../04-nonlinear-inversion/02-gradient-and-newton.md)
  — the derivative quantities a local analysis uses.
- [18-05-06 Posterior Summaries](../05-bayesian-inversion/06-posterior-summary.md)
  — correlations between parameters, which a one-at-a-time analysis ignores.

## 1. Intuition: which input actually matters?

An inversion produces a posterior over many parameters, and a prediction that
depends on them. The question "which parameter matters?" has three distinct
answers, and they are computed differently.

**Local sensitivity** asks how much the output moves when one input is nudged at a
chosen point, with the others held fixed. It is a derivative, it costs one extra
forward model per input, and it is only valid in a neighbourhood of that point.

**Global sensitivity** asks how much of the output *variance* is attributable to
each input over the whole range the input explores. It costs many forward models,
it accounts for interactions, and it is a statement about the model, not about a
point.

**Factor fixing** asks which inputs can be fixed at a nominal value without
changing the output distribution. That is a question about the *total* index, and
it is not answered by the first-order index.

The demonstration measures all three on two analytic test functions.

## 2. Variance decomposition, derived

Let $f(x)$ be a square-integrable function of independent inputs $x_1,\dots,x_d$.
The ANOVA (Sobol') decomposition writes

$$
f(x) = f_0 + \sum_i f_i(x_i) + \sum_{i<j} f_{ij}(x_i,x_j) + \cdots ,
$$

with every term having zero mean and being orthogonal to every other. Squaring and
integrating gives the **variance decomposition**

$$
\operatorname{Var}(f) = \sum_i V_i + \sum_{i<j} V_{ij} + \cdots ,
\qquad
V_i = \operatorname{Var}_{x_i}\!\bigl(\mathbb{E}[f\mid x_i]\bigr).
$$

The **first-order index** is the fraction of variance explained by $x_i$ alone,

$$
S_i = \frac{V_i}{\operatorname{Var}(f)},
$$

and the **total index** is the fraction explained by $x_i$ including every
interaction it takes part in,

$$
S_{Ti} = 1 - \frac{\operatorname{Var}_{x_{\sim i}}\!\bigl(\mathbb{E}[f\mid
x_{\sim i}]\bigr)}{\operatorname{Var}(f)}
= \frac{\mathbb{E}_{x_{\sim i}}\bigl[\operatorname{Var}_{x_i}(f \mid x_{\sim i})\bigr]}
{\operatorname{Var}(f)} .
$$

Two consequences to remember. First, $\sum_i S_i \le 1$, with equality exactly
when the model is additive. Second, $S_{Ti} \ge S_i$ always, and the difference
$S_{Ti} - S_i$ is the share of $x_i$'s influence that depends on the values of the
other inputs. An input with $S_i = 0$ but $S_{Ti} > 0$ has no main effect but
participates in interactions — the classic example being a term like $x_1x_2$, whose
individual main effects vanish when the inputs are centred.

## 3. Exact indices for the demonstration's test function

The demonstration uses the Sobol' $g$-function

$$
f(x) = \prod_{i=1}^{3} \frac{\lvert 4x_i - 2\rvert + a_i}{1 + a_i},
\qquad x_i \sim \mathcal{U}[0,1], \qquad a = (0,\ 0.5,\ 3).
$$

Each factor has mean $\mathbb{E}[g_i] = 1$: the absolute-value term integrates to
$2\int_0^1\lvert 4x-2\rvert\,\mathrm{d}x = 1$, and the denominator normalises it.
Because the factors are independent, $\mathbb{E}[f\mid x_i] = g_i(x_i)\prod_{j\ne i}
\mathbb{E}[g_j] = g_i(x_i)$, so the conditional-expectation variance is just

$$
V_i = \operatorname{Var}[g_i(x_i)] = \frac{1}{3}\cdot\frac{1}{(1+a_i)^2},
\qquad
\operatorname{Var}(f) = \prod_i\left(1+V_i\right) - 1 .
$$

The demonstration prints

| $i$ | $a_i$ | $V_i$ | $S_i$ | $S_{Ti}$ | interaction $S_{Ti}-S_i$ |
|---|---|---|---|---|---|
| 1 | 0.00 | 0.333333 | 0.592322 | 0.694241 | 0.101920 |
| 2 | 0.50 | 0.148148 | 0.263254 | 0.358318 | 0.095064 |
| 3 | 3.00 | 0.020833 | 0.037020 | 0.056673 | 0.019653 |

with $\operatorname{Var}(f) = 0.562757$ and $\sum_i S_i = 0.892596$. The sum is
below one by $0.107$, which is the total interaction share; the three differences
$S_{Ti}-S_i$ sum to $0.2167$, not $0.107$, because each interaction is counted in
the total index of every input that takes part in it. This is exactly why total
indices may sum to more than one and why that is not an error.

Reading the table: $x_1$ alone explains $59\%$ of the variance and $x_1$ in all its
roles explains $69\%$; the small $a_3 = 3$ makes $x_3$ nearly inert at $3.7\%$ main
effect. A ranking by $S_i$ gives $x_1 > x_2 > x_3$ and the same ranking holds for
$S_{Ti}$; a ranking that would change between the two would indicate a parameter
whose importance is almost entirely interaction.

## 4. Estimating the indices, and measuring the estimator

The estimators are the Saltelli/Jansen pair

$$
\hat S_i = \frac{\frac1N\sum_{k} f(B_k)\bigl[f(A^{(i)}_k) - f(A_k)\bigr]}{\widehat{\operatorname{Var}}(f)},
\qquad
\widehat{S_{Ti}} = \frac{\frac1{2N}\sum_{k} \bigl[f(A_k)-f(A^{(i)}_k)\bigr]^2}
{\widehat{\operatorname{Var}}(f)},
$$

where $A$ and $B$ are two independent designs of $N$ points each and
$A^{(i)}$ is $A$ with the $i$-th column replaced by that column of $B$. With $d$
inputs this costs $N(2d+2) = 8N$ evaluations here, so a design of $8192$ base points
costs $65\,536$ forward evaluations per replicate.

Twenty scrambled replicates give

| $i$ | exact $S_i$ | mean estimate | s.d. across replicates | exact $S_{Ti}$ | mean estimate | s.d. |
|---|---|---|---|---|---|---|
| 1 | 0.592322 | 0.592203 | 0.000669 | 0.694241 | 0.694143 | 0.000264 |
| 2 | 0.263254 | 0.263395 | 0.000632 | 0.358318 | 0.358276 | 0.000400 |
| 3 | 0.037020 | 0.037115 | 0.000259 | 0.056673 | 0.056695 | 0.000089 |

The estimates bracket the exact values within the replicate spread, which is the
only meaningful statement: an index quoted without a standard error has unknown
precision, and the standard error must come from independent replicates, not from a
formula that assumes the estimator is a simple mean.

## 5. Where a local analysis misleads: a measured counter-example

Consider the analytically known additive model

$$
f(x) = 10\,(x_1 - 0.5)^2 + x_2 + 0.5\,x_3, \qquad x_i \sim \mathcal{U}[0,1],
$$

for which $V_1 = 100\bigl(\tfrac{1}{80} - \tfrac{1}{144}\bigr) = 0.555556$,
$V_2 = 1/12 = 0.083333$, $V_3 = 0.25/12 = 0.020833$, and hence

$$
S = (0.8421,\ 0.1263,\ 0.0316), \qquad S_T = S \quad\text{(purely additive)}.
$$

The demonstration verifies the total variance by simulation:
$\operatorname{Var}(f) = 0.661102$ over $10^6$ draws against the exact $0.659722$,
a difference consistent with the Monte Carlo error.

Now evaluate the local sensitivities at the nominal point $x_0 = (0.5, 0.5, 0.5)$:

$$
\frac{\partial f}{\partial x_1} = 20(x_1 - 0.5) = 0, \qquad
\frac{\partial f}{\partial x_2} = 1, \qquad
\frac{\partial f}{\partial x_3} = 0.5 .
$$

| parameter | local $\lvert\partial f/\partial x_i\rvert$ | local rank | global $S_i$ | global rank |
|---|---|---|---|---|
| 1 | 0.0000 | 3 | 0.8421 | 1 |
| 2 | 1.0000 | 1 | 0.1263 | 2 |
| 3 | 0.5000 | 2 | 0.0316 | 3 |

The local analysis ranks $x_1$ **last** with a derivative of exactly zero, because
the nominal point sits at the minimum of the parabola. The global analysis ranks it
**first**, with $84\%$ of the variance. Both computations are correct. They answer
different questions, and only the global one describes the model over the range the
parameter actually explores. The lesson is not that derivatives are useless — they
are the basis of the optimisers in
[18-04](../04-nonlinear-inversion/README.md) — but that **a derivative at a nominal
point is not a sensitivity unless the model is linear and the point is typical**.

## 6. Convergence, measured

| base samples $N$ | mean $\lvert\hat S_i - S_i\rvert$ over three parameters |
|---|---|
| 64 | 0.067492 |
| 256 | 0.010381 |
| 1024 | 0.005072 |
| 4096 | 0.000851 |
| 16384 | 0.000220 |

The measured log-log slope is $-1.007$, steeper than the $-0.5$ of plain Monte
Carlo: the quasi-random points fill the space more evenly, so both the constant and
the observed rate improve on this function. The rate is not a guarantee. Quasi-Monte
Carlo relies on the integrand having enough smoothness for its low-discrepancy
structure to help, and this $g$-function has a kink in every input; a rougher or
higher-dimensional integrand returns the plain Monte Carlo rate. What is
transportable is the practice: report a standard error obtained from independent
replicates, as in Section 4.

## 7. Choosing a method

| purpose | method | cost |
|---|---|---|
| quick screening of many inputs | Morris elementary effects, or local derivatives | $O(d)$ |
| ranking by main effect | first-order Sobol indices | $N(2d+2)$ evaluations |
| factor fixing (which inputs can be frozen) | total Sobol indices | same design, free |
| detecting interactions | $S_{Ti}-S_i$; or a two-factor design | same design, free |
| analytic sensitivity of a smooth response | polynomial chaos coefficients (lesson [04](04-surrogate-uq.md)) | $O(\text{basis})$ |

The single most common error in reported sensitivity analyses is to quote
first-order indices and to describe them as "the influence of each parameter". The
correct statement is "the fraction of output variance explained by that parameter
*alone*", and the word *alone* is where the interactions go.

## 8. Assumptions and regime of validity

1. **Independent inputs.** The variance decomposition used here assumes
   independence. Correlated inputs require the Shapley-effect or a
   generalised decomposition, because the ANOVA terms are no longer orthogonal.
2. **A scalar output.** For a vector or functional output, the decomposition must
   be defined on a summary, and the choice of summary changes the indices.
3. **A fixed input distribution.** The indices are defined with respect to the
   input distributions chosen; change a range and the indices change.
4. **The input distribution must be the one used in sampling.** For a Bayesian
   sensitivity analysis, sampling from the posterior already includes correlations,
   which breaks the independence assumption; sample from the prior for a
   prior-based ranking and say which was done.
5. **Estimator bias at small $N$.** The Saltelli/Jansen estimators are biased and
   their bias does not vanish quickly; hence the replicate-based error bars.
6. **A zero index is not a zero effect for all purposes.** A parameter can be
   uncorrelated with the output variance and still control the output mean, or
   matter in a rare region the sampling never visits.

## 9. Demonstration and exercises

[`code/sensitivity_analysis_demo.py`](./code/sensitivity_analysis_demo.py)
computes the analytic indices, verifies them with quasi-Monte Carlo Saltelli
estimators over twenty replicates, measures the local-versus-global ranking
reversal, and measures the convergence rate. It prints all tables above with units
and exits $0$ in about half a second. Exercises and solutions:
[`exercises/03-sensitivity-analysis-exercises.md`](./exercises/03-sensitivity-analysis-exercises.md),
[`exercises/03-sensitivity-analysis-solutions.md`](./exercises/03-sensitivity-analysis-solutions.md).

## Mastery checkpoint

**(a)** Derive $V_i = (1/3)/(1+a_i)^2$ for the $g$-function factor, showing the
integrals.
**(b)** Compute $S_3$ and $S_{T3}$ from the printed variances and check them against
the table.
**(c)** A parameter has $S_i = 0.00$ and $S_{Ti} = 0.25$. State what this means and
give a functional form that produces it.
**(d)** Explain in two sentences why the local derivative at a nominal point
reported $0.0000$ for the most influential parameter in Section 5.

## Common pitfalls

1. **Quoting first-order indices as "the" sensitivity.** Section 3 shows $S_1$
   understates $x_1$'s total influence by $0.102$.
2. **Using derivatives at a nominal point over a wide input range.** The measured
   rank reversal in Section 5 is total.
3. **Ignoring the standard error.** An index is an estimate; twenty replicates here
   give a spread of about $0.0007$ on $S_1$, which is the resolution of the method.
4. **Standardising indices incorrectly.** $S_i$ is dimensionless by construction;
   multiplying by an input standard deviation produces a different quantity.
5. **Applying the ANOVA decomposition to correlated inputs.** Orthogonality fails.
6. **Assuming quasi-Monte Carlo convergence is faster in all problems.** The
   measured rate here is $-1.0$; the guarantee is $-0.5$.
7. **Reporting a sensitivity from a posterior sample when a prior-based ranking was
   intended.** State which measure the inputs were drawn from.

## Further reading

- **Sobol', I. M. (2001). Global sensitivity indices for nonlinear mathematical
  models and their Monte Carlo estimates. *Mathematics and Computers in
  Simulation*, 55(1–3), 271–280.** Level: research. The indices and their
  estimator.
- **Saltelli, A., Ratto, M., Andres, T., Campolongo, F., Cariboni, J., Gatelli, D.,
  Saisana, M., & Tarantola, S. (2008). *Global Sensitivity Analysis: The Primer*.
  Wiley.** Level: research. The design matrices used in Section 4 and the practical
  workflow.
- **Morris, M. D. (1991). Factorial sampling plans for preliminary computational
  experiments. *Technometrics*, 33(2), 161–174.** Level: research. The cheap
  screening method in the Section 7 table.
- **Saltelli, A., Annoni, P., Azzini, I., Campolongo, F., Ratto, M., & Tarantola,
  S. (2010). Variance based sensitivity analysis of model output. Design and
  estimator for the total sensitivity index. *Computer Physics Communications*,
  181(2), 259–270.** Level: research. The specific estimators written out in
  Section 4.

## Related modules

- [02 Monte Carlo Propagation and Its Convergence](02-monte-carlo-uq.md) — the
  sampling on which these estimators are built.
- [04 Surrogate Models and Polynomial Chaos for UQ](04-surrogate-uq.md) — reading
  the indices off a surrogate instead of estimating them.
- [01 Taxonomy of Uncertainty: Aleatory, Epistemic, Structural](01-uncertainty-taxonomy.md)
  — which variance is being decomposed.
- [18-04-02 Gradient, Gauss-Newton and Full Newton Methods](../04-nonlinear-inversion/02-gradient-and-newton.md)
  — the derivatives of the local analysis.
- [18-02-04 SVD Analysis: Model Resolution and Data Importance](../02-linear-inverse-problems/04-svd-analysis-inverse.md)
  — the linear-algebraic view of which data constrain which parameters.
