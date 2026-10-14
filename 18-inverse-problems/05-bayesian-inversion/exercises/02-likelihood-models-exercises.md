# Exercises — 18-05-02 Constructing Likelihoods and Error Models

Lesson: [02 Constructing Likelihoods and Error Models](../02-likelihood-models.md).
Attempt these before reading the [solutions](./02-likelihood-models-solutions.md).
All models are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** For stationary AR(1) errors with $\sigma = 0.2$ and $n = 12$ data points,
compute the exact finite-sample inflation factor of the sample-mean variance, and
the asymptotic factor as $n\to\infty$, for $\rho = 0.9$. By what factor is the
standard error understated if correlation is ignored?

**★2.** The demonstration reports, for the AR(1) data set, a slope of
$0.5240 \pm 0.0167$ under an independent Gaussian likelihood and
$0.5340 \pm 0.0213$ under the correct generalised-least-squares likelihood.
Compute the factor by which the reported uncertainty is understated.

**★3.** Write the negative log likelihood, up to constants, for a Gaussian, a
Laplace and a Student-$t$ (with $\nu$ degrees of freedom) error model on residuals
$r_i$. State which is quadratic, which is linear and which is logarithmic in
$\lvert r_i\rvert$ for large residuals.

## ★★ Applied

**★★4.** Using the demonstration's influence table, compute the ratio of the
Gaussian slope shift to the Laplace shift at $\delta/\sigma = 8$, and the same
ratio for Student-$t$. State in one sentence what the ratio measures.

**★★5.** A gravity survey has $200$ stations along a profile; the reading error is
independent between stations but the Bouguer correction uses a regional density
that is uncertain by $2\%$. Write down the resulting covariance structure for the
data errors and say which off-diagonal entries are non-zero.

**★★6.** Show that with a Gaussian likelihood, a flat prior on the coefficients
and the reference prior $\pi(\sigma)\propto 1/\sigma$, the marginal posterior
variance of a coefficient is inflated relative to the known-$\sigma$ case by
$N/(N-d)$, where $d$ is the number of fitted coefficients. Evaluate for $N = 12$
and $d = 2$.

## ★★★ Research-oriented

**★★★7.** Design an experiment that measures how the reported slope interval
depends on the assumed error model, for three data types: (i) clean Gaussian,
(ii) AR(1) at $\rho = 0.8$, (iii) $10\%$ contamination by outliers of size $5\sigma$.
State the metric, the number of replicates, and the predicted ordering of the three
interval widths under a Gaussian likelihood. Which of the three would a Gaussian
likelihood mis-report most severely, and why?

**★★★8.** A colleague estimates the noise scale from the residuals of the same
fit, then reports the coefficient interval using $\sigma$ fixed at that estimate.
Quantify what is lost, and give the corrected interval for the ★★6 case.
