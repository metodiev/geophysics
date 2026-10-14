# Exercises — 21-03-01 The Bayesian Paradigm and Subjective Probability

Attempt these before reading the
[solutions](./01-bayesian-paradigm-solutions.md). The lesson is
[01 The Bayesian Paradigm](../01-bayesian-paradigm.md). All data are
**SYNTHETIC**; numbers quoted from the demonstration reproduce its output.

## ★ Foundational

**★1.** A $\mathrm{Beta}(3,4)$ prior is updated with $5$ successes in $12$
trials. Write the posterior, and compute its mean, its mode and its variance.

**★2.** Compute the prior-equivalent sample size of the $\mathrm{Beta}(3,4)$
prior, and of the demonstration's three priors.

**★3.** For the posterior of ★1, compute the posterior predictive probability of
a success on the next trial.

## ★★ Applied

**★★4.** Derive the Beta-Binomial conjugate update: show that a
$\mathrm{Beta}(a,b)$ prior with a $\mathrm{Binomial}(n,\theta)$ likelihood gives
a $\mathrm{Beta}(a+k, b+n-k)$ posterior, and state the proportionality constant
you discarded and why it does not affect the posterior.

**★★5.** For one trial with zero successes and a uniform prior, compute the
$95\ \%$ equal-tailed credible interval and compare it with the Clopper-Pearson
$95\ \%$ confidence interval $[0, 1 - 0.025^{1/n}]$. Explain the difference in
meaning, not merely in numbers.

**★★6.** The demonstration's sceptical prior has a prior-equivalent sample size
of $38$ and prior mean $0.5$; the data give a maximum-likelihood estimate of
$0.2333$. Compute the number of additional observations that would bring the
posterior mean within $0.01$ of the maximum-likelihood estimate.

## ★★★ Research-oriented

**★★★7.** Specify a **prior-sensitivity experiment** for a Bayesian estimate of
a fault slip rate: state the priors, the prior-equivalent sample sizes, the
metric, the number of synthetic catalogues, and the criterion for declaring the
result prior-dominated. A specification that could not be executed is a failed
answer.

**★★★8.** Design a **calibration study for credible intervals**: an experiment
that measures the realised coverage of a $95\ \%$ credible interval when the
prior is correct and when it is wrong. State the data-generating process, the
replicate count, the metric, and the predicted coverage in each case.
