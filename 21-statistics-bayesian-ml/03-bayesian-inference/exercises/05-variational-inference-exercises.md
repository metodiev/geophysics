# Exercises — 21-03-05 Variational Inference and Scalable Bayes

Attempt these before reading the
[solutions](./05-variational-inference-solutions.md). The lesson is
[05 Variational Inference](../05-variational-inference.md). All models are
**SYNTHETIC**; numbers quoted from the demonstration reproduce its output.

## ★ Foundational

**★1.** Write the evidence lower bound and show, using
$\ln p(y) = \mathcal L(q) + \mathrm{KL}(q\|p(\cdot\mid y))$, that it is a lower
bound.

**★2.** With mean-field standard deviations $0.31544$ and an exact posterior
standard deviation of $0.70883$, compute the ratio and state what fraction of the
true posterior spread the approximation reports.

**★3.** Given an exact log evidence of $-15.88319$ and a converged ELBO of
$-16.69283$, compute the KL divergence and state why it cannot be negative.

## ★★ Applied

**★★4.** For a bivariate Gaussian posterior with correlation $\rho = -0.8955$,
compute the predicted mean-field variance ratio $(1-\rho^{2})$ and compare it with
the demonstration's measured ratio of standard deviations, $0.44502$.

**★★5.** Write the mean-field CAVI update for one coordinate of the
linear-Gaussian model and identify which term plays the role of the data
precision and which of the prior precision.

**★★6.** The demonstration's ELBO rises from $-17.07352$ to $-16.69283$ in
$200$ sweeps. Compute the total improvement, and state the maximum additional
improvement obtainable with more sweeps within the factorised family.

## ★★★ Research-oriented

**★★★7.** Specify a **calibration study** that quantifies the under-statement of
a mean-field approximation as a function of the posterior correlation, using both
an exact Gaussian reference and an MCMC sample. State the design, the metric, the
replicate count and the predicted relationship. A specification that could not be
executed is a failed answer.

**★★★8.** Design a **family-comparison study** that compares mean field, a
full-covariance Gaussian and a normalising-flow approximation on the same
posterior, reporting the ELBO, the KL gap where available, and the cost per
effective sample. State the metric and the predicted ordering.
