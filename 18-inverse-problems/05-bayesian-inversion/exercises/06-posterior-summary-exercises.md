# Exercises — 18-05-06 Posterior Summaries: Marginals, Credible Intervals, Correlations

Lesson: [06 Posterior Summaries](../06-posterior-summary.md).
Attempt these before reading the [solutions](./06-posterior-summary-solutions.md).
All models are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** Show by differentiation that $\mathbb{E}[(m-a)^2]$ is minimised at
$a = \mathbb{E}[m]$, and state which loss function is minimised by the median.

**★2.** Define the equal-tailed and highest-posterior-density (HPD) $95\%$
intervals. For the demonstration's skewed posterior, state which interval is
shorter and which tail gains probability mass.

**★3.** Explain in three sentences why a $95\%$ credible interval is not a $95\%$
confidence interval, using the word "conditional" correctly.

## ★★ Applied

**★★4.** For a Gaussian posterior with unit marginal standard deviations and
correlation $\rho = 0.9$, compute the marginal and conditional standard deviations
of the first parameter and their ratio. Give the exact relation in terms of $\rho$.

**★★5.** The demonstration reports Bayesian coverage $0.235$ under the conflicting
prior and $0.953$ under the weak prior. Explain why the second number is close to
$0.95$ and the first is not, and state which one is "wrong".

**★★6.** A quantity of interest is $g(\sigma) = 1/\sigma$, where the posterior for
$\sigma$ is the demonstration's inverse-gamma with $95\%$ equal-tailed interval
$[0.6321, 2.7979]$. Compute the $95\%$ interval for $g$. Then state, with a
calculation, whether $\mathbb{E}[g] = 1/\mathbb{E}[\sigma]$.

**★★7.** Compute the ratio of the joint $95\%$ region area at $\rho = 0.99$ to that
at $\rho = 0$, and compare with the ratio of the product of the marginal interval
widths. State the reporting consequence.

## ★★★ Research-oriented

**★★★8.** Design a coverage study for a real inversion. State the generating
process, the interval construction, the number of replicates needed for a $95\%$
coverage estimate with a standard error below $0.005$, and what a measured coverage
of $0.90$ would tell you about the likelihood rather than about the sampler.
