# Solutions — 16-07-02 Detection and Attribution of Climate Change

> **Read after attempting the exercises.** Numbers were computed, not estimated by
> hand; the arithmetic is shown.

Lesson: [02 Detection and Attribution](../02-detection-attribution.md).

---


## ★ Foundational

## ★1 — GLS versus OLS standard errors

$$\mathbf{C}^{-1} = \frac{1}{4\cdot4-1\cdot1}\begin{pmatrix}4 & -1\\ -1 & 4\end{pmatrix}
= \frac{1}{15}\begin{pmatrix}4 & -1\\ -1 & 4\end{pmatrix}.$$

Design $\mathbf{X} = (1,1)^{\mathsf{T}}$, so
$\mathbf{X}^{\mathsf{T}}\mathbf{C}^{-1}\mathbf{X} = \frac{1}{15}(4-1-1+4) = \frac{6}{15} = 0.4000$.

$$\hat\beta = \frac{\mathbf{X}^{\mathsf{T}}\mathbf{C}^{-1}\mathbf{y}}
{\mathbf{X}^{\mathsf{T}}\mathbf{C}^{-1}\mathbf{X}}
= \frac{\frac{1}{15}\left[(8-3)+(-2+12)\right]}{0.4}
= \frac{(5+10)/15}{0.4} = \frac{1.0}{0.4} = 2.5000.$$

$$\operatorname{var}(\hat\beta) = \left(\mathbf{X}^{\mathsf{T}}\mathbf{C}^{-1}\mathbf{X}\right)^{-1}
= \frac{1}{0.4} = 2.5000,\qquad \text{SE}_{\text{GLS}} = 1.5811\ \mathrm{K}.$$

OLS uses the sample residual variance, $s^{2} = \frac{1}{2-1}[(2-2.5)^{2}+(3-2.5)^{2}]
= 0.5$, giving $\operatorname{var} = s^{2}/2 = 0.25$ and
$\text{SE}_{\text{OLS}} = 0.5000\ \mathrm{K}$.

The **GLS standard error is 3.16 times larger**. The two observations are
positively correlated, so they carry less independent information than OLS
assumes; the naive estimator treats them as two independent measurements and
understates the uncertainty. The point estimate is identical because the design is
a simple mean.

---

## ★2 — The two null hypotheses

- **Detection:** $H_0: \beta_{\text{signal}} = 0$ — the observed change is
  consistent with internal variability alone. Rejecting it means the observed
  pattern cannot be produced by internal variability at the stated level.
- **Attribution:** $H_0: \beta_{\text{signal}} = 1$ *and* consistency with a
  stated combination of forcings — the observed response matches the model's
  response amplitude to that forcing combination. Rejecting it means the model's
  amplitude is inconsistent with the data; *not* rejecting it means the data are
  consistent with the modelled response, conditional on the noise model and the
  fingerprints.

Rejecting $H_0^{\text{det}}$ says *something external is happening*. Rejecting
$H_0^{\text{attr}}$ says *the model's size for that something is wrong*.

---

## ★3 — GLS in matrix form

$$\hat{\boldsymbol{\beta}} = \left(\mathbf{X}^{\mathsf{T}}\mathbf{C}^{-1}\mathbf{X}\right)^{-1}
\mathbf{X}^{\mathsf{T}}\mathbf{C}^{-1}\mathbf{y},
\qquad \operatorname{cov}(\hat{\boldsymbol{\beta}})
= \left(\mathbf{X}^{\mathsf{T}}\mathbf{C}^{-1}\mathbf{X}\right)^{-1}.$$

The quantity estimated from a control run is $\mathbf{C}$, the covariance of
internal variability (and hence $\mathbf{C}^{-1}$, the whitening operator). The
fingerprints in $\mathbf{X}$ come from forced simulations, and both are model
quantities.

---

## ★★ Applied

## ★★4 — Deriving GLS

Let $J(\boldsymbol{\beta}) = (\mathbf{y}-\mathbf{X}\boldsymbol{\beta})^{\mathsf{T}}
\mathbf{C}^{-1}(\mathbf{y}-\mathbf{X}\boldsymbol{\beta})$. Expanding,

$$J = \mathbf{y}^{\mathsf{T}}\mathbf{C}^{-1}\mathbf{y}
- 2\boldsymbol{\beta}^{\mathsf{T}}\mathbf{X}^{\mathsf{T}}\mathbf{C}^{-1}\mathbf{y}
+ \boldsymbol{\beta}^{\mathsf{T}}\mathbf{X}^{\mathsf{T}}\mathbf{C}^{-1}\mathbf{X}\boldsymbol{\beta}.$$

Differentiating with respect to $\boldsymbol{\beta}$ (using symmetry of
$\mathbf{C}^{-1}$, hence of $\mathbf{X}^{\mathsf{T}}\mathbf{C}^{-1}\mathbf{X}$),

$$\frac{\partial J}{\partial\boldsymbol{\beta}}
= -2\mathbf{X}^{\mathsf{T}}\mathbf{C}^{-1}\mathbf{y}
+ 2\mathbf{X}^{\mathsf{T}}\mathbf{C}^{-1}\mathbf{X}\boldsymbol{\beta}
= \mathbf{0}.$$

Solving the normal equations gives
$\hat{\boldsymbol{\beta}} = (\mathbf{X}^{\mathsf{T}}\mathbf{C}^{-1}\mathbf{X})^{-1}
\mathbf{X}^{\mathsf{T}}\mathbf{C}^{-1}\mathbf{y}$. The estimator is linear in
$\mathbf{y}$, unbiased whenever $\mathbb{E}[\mathbf{y}] = \mathbf{X}\boldsymbol{\beta}$,
and its covariance follows from
$\operatorname{cov}(\hat{\boldsymbol{\beta}}) = \mathbf{A}\mathbf{C}\mathbf{A}^{\mathsf{T}}$
with $\mathbf{A} = (\mathbf{X}^{\mathsf{T}}\mathbf{C}^{-1}\mathbf{X})^{-1}
\mathbf{X}^{\mathsf{T}}\mathbf{C}^{-1}$, which collapses to the stated expression.

---

## ★★5 — Naive inflation versus measured inflation

$$1/(1-\cos^{2}\theta):\quad
\cos\theta = 0.85 \Rightarrow \frac{1}{1-0.7225} = 3.60; \qquad
\cos\theta = 0.95 \Rightarrow \frac{1}{1-0.9025} = 10.26.$$

Measured inflation: $1.53\times$ and $2.73\times$.

The naive formula overestimates because it assumes the patterns are **whitened**
— that is, it uses the raw inner product rather than the inner product under
$\mathbf{C}^{-1}$. The demonstration's patterns are smooth in space, so they
project unevenly onto the noise's modes: the direction in which they are similar
is not the direction in which the noise is large, and the effective overlap is
smaller than the raw cosine suggests. The correct statement of pattern similarity
in this problem is the whitened cosine, which is why a published attribution study
quotes a correlation computed under the analysis's own noise model.

---

## ★★6 — Coverage arithmetic

Nominal 90% over $300$ realisations: expected misses $= 0.10\times300 = 30$.

Measured OLS coverage $0.457$: misses $= (1-0.457)\times300 = 163$ — more than
five times the nominal rate.

A referee-ready sentence: *"Because internal variability is strongly
autocorrelated and a naive ordinary-least-squares calculation assumes independent
residuals, the quoted confidence level substantially overstates the evidence; the
significance must be recomputed with a noise covariance estimated from unforced
control simulations."*

---

## ★★★ Research-oriented

## ★★★7 — Publishing the result

Model answer:

> "The observed pattern of change is inconsistent with internal variability alone
> at the 95% level (detection). Using fingerprints for greenhouse gases and
> volcanic forcing, and a noise covariance estimated from two unforced control
> simulations of 500 years each, the fitted greenhouse-gas scaling factor is
> $\hat\beta = 1.15$ with a 90% uncertainty interval of $[0.95, 1.35]$; the
> observations are therefore consistent with the modelled response amplitude for
> this forcing combination, conditional on the model fingerprints and on the
> control-run estimate of internal variability. The comparison climate is the
> same model run without the greenhouse-gas forcing; the statement is a
> statement about that counterfactual, not a measurement of it."

Sensitivity test to run before submission: re-estimate with the covariance from a
**different model's** control run (or with EOF-truncation changed) and report how
much the interval widens. A result that weakens the claim: an interval that no
longer contains $1$ when the noise model changes — that would show the conclusion
is being driven by the assumed covariance rather than by the data.

---

## ★★★8 — Testing whether $\mathbf{C}$ depends on the mean state (design)

**Data.** From a synthetic model, generate two long control runs at different
mean states — e.g. a "cool" state and a "warm" state produced by different
radiative forcing, each of 1000 years with no interannual forcing. Sample the
same space–time field from both.

**Estimator.** Compute the sample covariance matrix of detrended anomalies
$\mathbf{C}_{\text{cool}}$ and $\mathbf{C}_{\text{warm}}$, using the same EOF
truncation and regularisation for both. Also compute the variability of a scalar
diagnostic — for example the standard deviation of the global-mean annual-mean
temperature anomaly.

**Test statistic.** Two complementary tests:
1. a ratio test on the scalar diagnostic, $\sigma_{\text{warm}}^{2}/\sigma_{\text{cool}}^{2}$
   with a confidence interval from a block bootstrap that preserves temporal
   correlation;
2. a matrix test comparing $\mathbf{C}_{\text{cool}}$ and
   $\mathbf{C}_{\text{warm}}$ — for example the largest eigenvalue of
   $\mathbf{C}_{\text{cool}}^{-1/2}\mathbf{C}_{\text{warm}}\mathbf{C}_{\text{cool}}^{-1/2}$,
   which exceeds $1$ in proportion to the discrepancy, with a null distribution
   from splitting each run into halves and comparing them to itself.

**Falsification.** The stationary-$\mathbf{C}$ assumption is falsified if the
matrix statistic for the cool-versus-warm comparison lies outside the null
distribution obtained by comparing disjoint segments of the *same* run. A result
that is consistent with the same-run null supports the stationary assumption, but
only for the variability this model simulates — a single model cannot establish
it for the Earth.
