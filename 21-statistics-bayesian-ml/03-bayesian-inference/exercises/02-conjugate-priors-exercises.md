# Exercises — 21-03-02 Conjugate Priors and Analytic Posteriors

Attempt these before reading the
[solutions](./02-conjugate-priors-solutions.md). The lesson is
[02 Conjugate Priors](../02-conjugate-priors.md). All data are **SYNTHETIC**;
numbers quoted from the demonstration reproduce its output.

## ★ Foundational

**★1.** A $\mathrm{Beta}(1,3)$ prior is updated with $4$ successes in $16$
trials. Write the posterior and compute its mean, mode and variance.

**★2.** A $\mathcal N(3, 1)$ prior is updated with $n = 25$ observations of known
standard deviation $\sigma = 2$ and sample mean $\bar y = 3.5$. Compute the
posterior mean, the posterior variance and the data weight, and state the
shrinkage relative to the sample mean.

**★3.** A $\mathrm{Gamma}(3, \text{rate }2)$ prior is updated with $8$ events in
$4$ intervals. Write the posterior and compute its mean and standard deviation,
and compare the mean with the maximum-likelihood estimate.

## ★★ Applied

**★★4.** Derive the Normal-Normal posterior by completing the square in the
exponent of $p(\mu)p(\bar y\mid\mu)$, and read off the posterior precision and
mean.

**★★5.** Show that the posterior precision is the sum of the prior and data
precisions and that, as $n\to\infty$, the posterior variance tends to
$\sigma^{2}/n$ while the posterior mean tends to the sample mean. State what this
implies about the influence of a prior with finite precision.

**★★6.** For the demonstration's Normal-Normal case, compute the predictive
distribution of a single future observation and of the mean of ten future
observations. State why the first is wider and by how much.

## ★★★ Research-oriented

**★★★7.** Specify an experiment that replaces the known-variance Normal-Normal
update with a Normal-inverse-gamma prior and an unknown variance, and measures
how much the marginal posterior for the mean **widens** when the variance is
unknown. State the prior, the data sizes, the replicate count, and the predicted
factor by which the credible interval widens at $n = 5$ and $n = 100$. A
specification that could not be executed is a failed answer.

**★★★8.** Design a **simulation-based calibration** study for one of the three
conjugate models: an experiment that verifies the posterior is correct by
sampling parameters from the prior, generating data, and checking the rank of the
true parameter among posterior draws. State the model, the replicate count, the
metric, and the shape of the rank histogram under a correct posterior.
