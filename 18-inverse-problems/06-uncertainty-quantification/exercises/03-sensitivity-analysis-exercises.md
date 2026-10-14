# Exercises — 18-06-03 Sensitivity Analysis: Local, Global, Sobol Indices

Lesson: [03 Sensitivity Analysis](../03-sensitivity-analysis.md). Attempt these
before reading the [solutions](./03-sensitivity-analysis-solutions.md). All models
are **SYNTHETIC** analytic functions.

## ★ Foundational

**★1.** Derive $V_i = \operatorname{Var}_{x_i}(\mathbb{E}[f\mid x_i])$ for the
Sobol' $g$-function factor $g_i(x) = (\lvert 4x-2\rvert + a_i)/(1+a_i)$ on
$\mathcal{U}[0,1]$, and show that it equals $(1/3)/(1+a_i)^2$.

**★2.** Using the demonstration's printed variances, compute $S_3$ and $S_{T3}$ and
check them against the table.

**★3.** State the two inequalities $\sum_i S_i \le 1$ and $S_{Ti} \ge S_i$, and give
the model class for which each becomes an equality.

## ★★ Applied

**★★4.** From the demonstration's estimator table, compute the relative standard
error of $\hat S_1$ and of $\widehat{S_{T1}}$. State which is better determined and
why.

**★★5.** For the additive SYNTHETIC model
$f = 10(x_1-0.5)^2 + x_2 + 0.5x_3$ with $x_i\sim\mathcal{U}[0,1]$, compute the local
derivative with respect to each input at the nominal point $(0.2, 0.5, 0.5)$ and
rank the parameters locally. Compare with the global ranking
$S = (0.8421, 0.1263, 0.0316)$ and explain the difference.

**★★6.** From the convergence table, estimate the number of base samples needed to
reduce the mean absolute index error from $0.000220$ to $0.000020$, and state the
assumption the estimate relies on.

**★★7.** A study reports $S = (0.4, 0.35, 0.3)$ for three inputs and concludes that
the model is additive. State what is wrong with the conclusion and what the study
should have reported.

## ★★★ Research-oriented

**★★★8.** Design a global sensitivity analysis for a 12-parameter groundwater
flow model, given a budget of $1000$ forward solves. State the method, the design,
the number of indices you can estimate, and the standard-error target. Explain what
you would do differently with $10^{5}$ solves.
