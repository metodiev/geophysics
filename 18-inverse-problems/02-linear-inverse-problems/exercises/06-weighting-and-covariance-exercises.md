# Exercises — 18-02-06 Data Weighting and Error Covariance Specification

Attempt these before reading the
[solutions](./06-weighting-and-covariance-solutions.md). The lesson is
[06 Data Weighting and Error Covariance](../06-weighting-and-covariance.md). All
models are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** Write the weighted misfit, the normal equations and the estimator
covariance for $\operatorname{Cov}(\mathbf{e}) = C_d$.

**★2.** For an AR(1) covariance with $\sigma = 0.02\ \mathrm{mGal}$ and
$\rho = 0.7$, compute $C_d[0,0]$, $C_d[0,1]$ and the first entry of $C_d^{-1}$.

**★3.** State the two assumptions of ordinary (unweighted) least squares that
processing violates, and give a geophysical example of each.

## ★★ Applied

**★★4.** Whitening: with $L = \operatorname{chol}(C_d)$, show that
$\tilde{G} = L^{-1}G$, $\tilde{\mathbf{d}} = L^{-1}\mathbf{d}$ turn GLS into OLS,
and state the measured agreement with the direct GLS solution.

**★★5.** The demonstration measures sd$(m_3) = 0.000598$ unweighted and $0.000540$
GLS. (a) Compute the variance ratio. (b) Explain why the gain is small for a
quadratic trend with this correlation. (c) Name a survey design for which the gain
would be much larger.

**★★6.** True sd of the unweighted $m_1$ is $0.012983$, while the
independence-assuming value is $0.000391$. (a) Compute the understatement factor.
(b) Explain why this is worse than the efficiency loss of ★5. (c) Give the two
sentences you would put in a review of a paper that made this error.

## ★★★ Research-oriented

**★★★7.** You must estimate $C_d$ from data. Specify the procedure, the estimator
of the marginal variance, the estimator of the correlation, the diagnostics that
would reveal a mis-specified form, and the honest statement of what remains unknown.

**★★★8.** Show that residual-based variance estimation is biased under correlated
noise for the demonstration's design (measured $\hat{\sigma} = 0.014890$ against
$\sigma = 0.020000$). Derive the bias factor analytically for a simple case
(a constant-only model, $N$ points, $\rho$ known) and compare with the measured
$0.7445$.
