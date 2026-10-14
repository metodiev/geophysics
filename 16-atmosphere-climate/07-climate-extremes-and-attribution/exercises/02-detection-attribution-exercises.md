# Exercises — 16-07-02 Detection and Attribution of Climate Change

Attempt these before reading the
[solutions](./02-detection-attribution-solutions.md). The lesson is
[02 Detection and Attribution](../02-detection-attribution.md). All models and
numbers are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** Two observations of a signal have noise covariance
$\mathbf{C} = \begin{pmatrix}4 & 1\\ 1 & 4\end{pmatrix}$ (units K²). With the
design $\mathbf{X} = (1,1)^{\mathsf{T}}$ and $\mathbf{y} = (2.0, 3.0)^{\mathsf{T}}$
(K), compute the GLS estimate of $\beta$, its standard error, and the OLS
standard error. State which is larger and why.

**★2.** State the detection null hypothesis and the attribution null hypothesis
for a two-signal analysis, and explain in one sentence what rejecting each means.

**★3.** Write the GLS estimator and its covariance in matrix form, and state
which quantity must be estimated from a control run.

## ★★ Applied

**★★4.** Derive the GLS estimator by minimising
$(\mathbf{y}-\mathbf{X}\boldsymbol{\beta})^{\mathsf{T}}\mathbf{C}^{-1}
(\mathbf{y}-\mathbf{X}\boldsymbol{\beta})$ with respect to
$\boldsymbol{\beta}$.

**★★5.** For unit-norm patterns with inner product $\cos\theta$, the naive
variance inflation is $1/(1-\cos^{2}\theta)$. Evaluate it at
$\cos\theta = 0.85$ and $0.95$ and compare with the demonstration's measured
inflation of $1.53\times$ and $2.73\times$. Explain why the naive formula
overestimates.

**★★6.** In the demonstration, OLS coverage of the nominal 90% interval is
$0.457$ for the anthropogenic signal. How many of the $300$ realisations miss the
true value, and how many would be expected if the interval were calibrated? Give
one sentence a referee would accept as the consequence.

## ★★★ Research-oriented

**★★★7.** An analysis reports $\hat\beta = 1.15$ with a 90% interval
$[0.95, 1.35]$ for the greenhouse-gas fingerprint, using a control run of 500
years. Write the full attribution sentence you would publish, naming the
counterfactual, the noise model and the uncertainty. Then state one sensitivity
test you would run before submission and what result would weaken the claim.

**★★★8.** Design a synthetic experiment to test whether the internal-variability
covariance $\mathbf{C}$ depends on the mean state (that is, whether variability
changes as the climate warms). Specify the data you would generate, the estimator
you would use, the test statistic, and the result that would falsify the
stationary-$\mathbf{C}$ assumption.
