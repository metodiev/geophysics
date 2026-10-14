# Exercises — 18-06-02 Monte Carlo Propagation and Its Convergence

Lesson: [02 Monte Carlo Propagation and Its Convergence](../02-monte-carlo-uq.md).
Attempt these before reading the [solutions](./02-monte-carlo-uq-solutions.md). All
models are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** State the standard error of a Monte Carlo mean. A quantity has a $10\%$
coefficient of variation; how many samples are needed for the mean to be reported to
a relative error of $0.5\%$?

**★2.** The demonstration reports a linearised standard deviation of $0.0152$ mGal
and a Monte Carlo standard deviation of $0.0157$ mGal. Compute the relative
discrepancy, then compute the relative Monte Carlo error of the standard deviation
itself at $N = 2\times10^{6}$ and state whether the discrepancy is explained by it.

**★3.** Explain in two sentences why the number of draws is not a measure of
precision.

## ★★ Applied

**★★4.** The demonstration measures a variance reduction of $20.99\times$ from
antithetic sampling at $N = 2000$. Compute the number of plain Monte Carlo
evaluations that would give the same variance, and state the condition under which
the reduction would not materialise.

**★★5.** For the rare event $P(g > 0.15\ \mathrm{mGal}) = 3.570\times10^{-5}$:
(a) compute the number of draws needed for a $10\%$ relative standard error by plain
Monte Carlo; (b) state the effective sample size from the importance-sampling run
and what it implies about the stability of the weights; (c) say whether the
importance-sampling estimate or the plain one should be reported, and why.

**★★6.** A study reports the mean and the $95\%$ interval but not the $99.9\%$
quantile. Explain why the standard error of that quantile is a much larger
fraction of its own value than the standard error of the mean, and what practical
consequence this has for a threshold-based decision.

**★★7.** The demonstration's variance reduction was measured, not assumed. Design a
one-page experiment that would measure the variance reduction factor for a stated
model and a stated variance-reduction scheme, specifying the metric, the replicate
count and the decision rule.

## ★★★ Research-oriented

**★★★8.** Design a Monte Carlo UQ study for a nonlinear inversion whose forward
solve costs one hour. State how you would allocate a fixed budget of $10^4$ core
hours between sampling, surrogate construction and validation, and what diagnostic
you would report to justify the allocation.
