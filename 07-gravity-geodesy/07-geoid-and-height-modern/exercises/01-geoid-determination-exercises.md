# Exercises — 07-07-01 Determining the Geoid: Stokes, Remove-Restore, Kriging

Attempt these before reading the
[solutions](./01-geoid-determination-solutions.md). The lesson is
[01 Determining the Geoid](../01-geoid-determination.md). **All models and data
in this module are SYNTHETIC.**

Numbers to use (from the demonstration): geoid rms $190.55\ \mathrm{m}$, anomaly
rms $92.42\ \mathrm{mGal}$; band table as in the lesson; reference-model error
$1\%$ coefficient error $\to$ $2.0591\ \mathrm{m}$ geoid rms, $0.1\%\to
0.1328\ \mathrm{m}$, $10\%\to18.4577\ \mathrm{m}$; kernel values as tabulated.

## ★ Foundational

**★1.** Compute $\psi S(\psi)$ at $\psi = 0.02^\circ$, $0.5^\circ$ and
$3^\circ$ from the tabulated $S$ values (or from the formula), and state what its
near-constancy implies about the weighting of nearby gravity data.

**★2.** From the demonstration's band table, compute the share of the geoid
variance in degrees 2–20 and in degrees 21–60, and the corresponding shares of
the anomaly variance.

**★3.** State the units of every factor in $N = \frac{R}{4\pi\gamma}\iint\Delta
g\,S\,\mathrm{d}\Omega$ and verify that the product is a length.

## ★★ Applied

**★★4.** A reference model has a $0.3\%$ relative coefficient error. Using the
demonstration's measured linear relation, estimate the resulting geoid error,
and state the accuracy the coefficients would need for a $1\ \mathrm{cm}$ geoid.

**★★5.** Derive the least-squares collocation estimator from the minimum-variance
argument for a linear estimator $\hat N = \mathbf{w}^{\mathsf T}\mathbf{d}$, and
state precisely which assumption makes the result "optimal".

**★★6.** The covariance model is $\sum_l\sigma_l^2(2l+1)P_l(\cos\psi)$ times the
appropriate degree factors. Explain why a *truncated* covariance can make the
normal matrix ill conditioned, and give two practical remedies.

## ★★★ Research-oriented

**★★★7.** Design a numerical experiment that determines how large a data cap can
be *without* a reference model before the truncation error exceeds a
$5\ \mathrm{cm}$ budget. Specify how the inner zone is handled, how the
band-limited test field is constructed, and what you expect the answer to depend
on.

**★★★8.** Design a validation study for a collocation covariance: specify the
independent data, the diagnostic, and what a wrong covariance would look like in
the residuals.
