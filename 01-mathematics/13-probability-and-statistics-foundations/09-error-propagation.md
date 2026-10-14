---
id: 01-13-09
title: "Error and Uncertainty Propagation (Analytic and Monte Carlo)"
level: advanced
prereqs: ["01-13-07", "01-05-04"]
estimated_minutes: 90
tags: [error-propagation, monte-carlo, uncertainty-budget, covariance, delta-method]
---

# Error and Uncertainty Propagation (Analytic and Monte Carlo)

## Learning objectives

By the end of this lesson you will be able to:

1. **State** the propagation problem precisely: inputs with distributions, a
   derived quantity, and a distribution for the output.
2. **Derive** the first-order propagation formula from a Taylor expansion, in both
   the scalar and the matrix forms, and state the assumptions under which it holds.
3. **Apply** the sum, product, ratio and power rules, and write a budget that
   identifies which input dominates the output uncertainty.
4. **Handle correlation** correctly, including the case in which two measurements
   share a systematic error and the derived quantity is their difference.
5. **Implement** Monte Carlo propagation, choose the number of draws from the
   precision required, and verify the result against an analytic value.
6. **Recognise** the circumstances in which first-order propagation fails —
   strong nonlinearity, error models that violate the physical range of a
   quantity, and moments that do not exist — and measure the size of the failure.
7. **Report** a propagated uncertainty so that the reader can see which assumption
   dominates it.

## Prerequisites

[01-13-07 Confidence Intervals and Their Correct Interpretation](./07-confidence-intervals.md)
for interval interpretation, and
[01-05-04 Taylor Series, Linearisation and Small-Angle
Approximations](../05-single-variable-calculus/04-taylor-series.md) for the
expansion on which the whole of the analytic method rests.

## 1. The propagation problem

A geophysicist computes quantities that were never measured. Density is computed
from a mass and a volume; depth is computed from a travel time and a velocity;
impedance is computed from a density and a velocity; a gravity anomaly is computed
after applying a free-air, Bouguer, terrain and tidal correction, each with its own
uncertainty. In every case:

- a set of **inputs** $X_1, \dots, X_m$ have known or assumed distributions;
- an **output** $Y = g(X_1, \dots, X_m)$ is computed by a known, usually
  differentiable, function;
- the task is to describe the **distribution of $Y$**, or at least its standard
  deviation and a quantile range.

Two methods are available, and they should always be used together:

- **Analytic (first-order) propagation**, which linearises $Y$ about the input
  means and produces a formula for $\operatorname{Var}(Y)$ in terms of input
  variances and covariances. It is fast, gives interpretable contribution terms,
  and states its own limitation through the size of the neglected higher-order
  terms.
- **Monte Carlo propagation**, which samples the inputs and computes $Y$ for each
  sample. It handles arbitrary nonlinearity and arbitrary input distributions, and
  its own error is computable.

The discipline this lesson teaches is to run both and to compare them. Where they
agree, the analytic budget can be used with confidence, and the budget identifies
where to spend effort. Where they disagree, the disagreement is the message: the
linearisation has failed, and the size of the discrepancy tells you how badly.

## 2. First-order propagation

### 2.1 Derivation

Let $\boldsymbol\mu$ be the vector of input means and expand $g$ to first order
about $\boldsymbol\mu$:

$$g(\mathbf{X}) \approx g(\boldsymbol\mu) + \sum_{i=1}^{m}
\frac{\partial g}{\partial x_i}\bigg|_{\boldsymbol\mu}(X_i - \mu_i).$$

This is the linearisation of
[01-05-04](../05-single-variable-calculus/04-taylor-series.md). Taking expectations,

$$E[g(\mathbf{X})] \approx g(\boldsymbol\mu),$$

and taking variances, using $\operatorname{Var}(\sum_i a_i Z_i) = \sum_i \sum_j
a_i a_j \operatorname{Cov}(Z_i, Z_j)$,

$$
\boxed{\ \operatorname{Var}\bigl(g(\mathbf{X})\bigr) \approx
\sum_{i=1}^{m}\left(\frac{\partial g}{\partial x_i}\right)^{2}\sigma_i^{2}
+ 2\sum_{i<j}\frac{\partial g}{\partial x_i}\frac{\partial g}{\partial x_j}
\sigma_{ij}\ }
$$

where all derivatives are evaluated at the input means and $\sigma_{ij} =
\operatorname{Cov}(X_i, X_j)$. In matrix form, with the jacobian row vector
$\mathbf{J}$ whose entries are $\partial g/\partial x_i$ and the input covariance
matrix $\mathbf{C}$,

$$\operatorname{Var}\bigl(g(\mathbf{X})\bigr) \approx \mathbf{J}\,\mathbf{C}\,
\mathbf{J}^{\mathsf T}.$$

This is the same expression that appears in the propagation of a model covariance
through a linear forward operator, $\mathbf{C}_d = G\mathbf{C}_m G^{\mathsf T}$,
which is the working form of the linear inverse problem in
[01-07-08 Singular Value Decomposition and Rank Truncation](../07-linear-algebra/08-svd.md)
and [18 Inverse Problems](../../18-inverse-problems/README.md).

Three things are assumed and should be stated whenever the formula is used:

1. **The expansion is a good approximation**, i.e. the inputs are not uncertain by
   a large fraction of the scale over which $g$ curves.
2. **The inputs have finite variances.** The formula is a statement about variances
   and inherits their existence.
3. **The derivatives are evaluated at the right place** — the input means, not the
   observed values. In practice the observed values are used, which introduces a
   small error of the same order as the linearisation error.

### 2.2 The rules worth memorising

For independent inputs (all $\sigma_{ij} = 0$):

| Function | First-order standard deviation |
|---|---|
| $Y = \sum_i a_i X_i$ | $\sigma_Y = \sqrt{\sum_i a_i^2\sigma_i^2}$ |
| $Y = \prod_i X_i$ | $\dfrac{\sigma_Y}{Y} = \sqrt{\sum_i \left(\dfrac{\sigma_i}{x_i}\right)^2}$ |
| $Y = X_1 / X_2$ | $\dfrac{\sigma_Y}{Y} = \sqrt{\left(\dfrac{\sigma_1}{x_1}\right)^2 + \left(\dfrac{\sigma_2}{x_2}\right)^2}$ |
| $Y = X^{p}$ | $\dfrac{\sigma_Y}{Y} = \left|p\right|\dfrac{\sigma_X}{x}$ |
| $Y = \ln X$ | $\sigma_Y = \dfrac{\sigma_X}{x}$ |

The pattern is worth naming: **absolute uncertainties add in quadrature for sums,
relative uncertainties add in quadrature for products and ratios, and the exponent
multiplies the relative uncertainty for powers.** Every budget in this module is an
application of those three facts.

## 3. Worked examples

### 3.1 A ratio: density from mass and volume

With $m = 2.50 \pm 0.02$ kg and $V = 1.00 \pm 0.03$ L, and with $x$ denoting the
nominal value,

$$\frac{\sigma_\rho}{\rho} = \sqrt{\left(\frac{0.02}{2.50}\right)^{2} +
\left(\frac{0.03}{1.00}\right)^{2}} = \sqrt{0.000064 + 0.0009} = 0.031048,$$

so $\rho = 2.500000$ and $\sigma_\rho = 0.077621$. Monte Carlo with $400\,000$
draws and seed 20240125 gives:

```
    first-order sd = 0.077621
    Monte Carlo sd = 0.077802   (MC standard error 0.000087, difference 2.08 SE)
    Monte Carlo mean = 2.502376 against the nominal 2.500000
```

The two standard deviations agree to $0.2\%$, and the difference is about two Monte
Carlo standard errors — marginal, and consistent with a real but small second-order
effect of the curvature of $1/V$. The **mean** is displaced upward by $0.10\%$,
which is the Jensen effect of lesson 03: $E[m/V] > E[m]/E[V]$ because $1/V$ is
convex. At this level of uncertainty the displacement is thirty times smaller than
the standard deviation and can be ignored; the point is that it has a predictable
sign and magnitude.

### 3.2 A product with unequal contributions: depth from a travel time

$$d = \frac{vT}{2}, \qquad v = 3000 \pm 100\ \mathrm{m/s}, \quad
T = 0.500 \pm 0.005\ \mathrm{s}.$$

$$\frac{\sigma_d}{d} = \sqrt{\left(\frac{100}{3000}\right)^{2} +
\left(\frac{0.005}{0.500}\right)^{2}} = \sqrt{0.0011111 + 0.0001} = 0.034801,$$

so $d = 750.0000$ m and $\sigma_d = 26.1008$ m. The simulation gives $26.0830$ m
with a Monte Carlo standard error of $0.0292$ m — a difference of $0.61$ standard
errors, which is agreement.

**The budget is the useful output.** The velocity term contributes
$100/3000 = 3.333\%$ and the timing term $0.005/0.500 = 1.000\%$; in quadrature
these give $3.480\%$. Because the terms add in quadrature, the smaller term cannot
be ignored — dropping it would change the answer by a factor of $3.333/3.480 =
0.958$, a $4\%$ understatement — but reducing it further would achieve little:
even a perfect travel-time measurement would leave $\sigma_d/d = 3.333\%$.
Conversely, halving the velocity uncertainty to $50$ m/s would give
$\sqrt{0.0002778 + 0.0001} = 0.019436$, reducing $\sigma_d$ from $26.10$ m to
$14.58$ m. **The budget tells you which measurement to improve and by how much is
worth improving it.**

## 4. Correlation, and why differences are special

The cross terms in the propagation formula are not a technicality; they are
frequently the largest effect in the budget.

### 4.1 The difference of two correlated measurements

Let $Y = X_2 - X_1$ with both having variance $\sigma^2$ and covariance
$\rho\sigma^2$. Then

$$\operatorname{Var}(Y) = \sigma^2 + \sigma^2 - 2\rho\sigma^2
= 2\sigma^2(1-\rho).$$

Positive correlation **reduces** the variance of a difference; $\rho = 1$ makes it
zero, because the shared error cancels exactly.

The demonstration sets up two adjacent gravity stations whose readings share a
calibration bias $B$ with standard deviation $0.30$ mGal and have independent
reading noise with standard deviation $1.00$ mGal:

```
  sd of shared calibration bias = 0.3 mGal
  sd of independent reading noise = 1.0 mGal
  correlation implied by the shared bias = 0.082569

  If the readings were treated as independent:
    first-order sd = 1.476482
    Monte Carlo sd = 1.412910   (MC standard error 0.001580, difference 40.24 SE)

  Using Var(g2 - g1) = 2 sigma_i^2, because the bias is common:
    first-order sd = 1.414214
    Monte Carlo sd = 1.412910   (MC standard error 0.001580, difference 0.83 SE)
```

The correlation here is only $0.083$ — the shared bias contributes $9\%$ of the
variance, $\sigma_B^2/(\sigma_B^2+\sigma_i^2) = 0.09/1.09$ — yet ignoring it
overstates the standard deviation of the difference by $4.4\%$, and the discrepancy
is forty standard errors. The correct formula matches to $0.83$ standard errors.

**The physics of this is the single most useful idea in practical uncertainty
analysis.** The shared calibration error cancels in the difference, so the
difference of two readings from the same instrument is more precise than the
independent-error formula suggests. This is why:

- relative gravity surveys tie each station to a base and difference consecutive
  readings, so instrument drift is common-mode;
- differential GNSS differences two receivers, cancelling satellite clock and
  broadcast ephemeris errors;
- differential InSAR differences two acquisitions, cancelling atmospheric delay to
  first order;
- the "repeat station" method differences repeated occupations, cancelling monument
  and instrument offsets.

**The cost of the assumption.** A correlation model must be argued physically. If
the offsets do *not* cancel — two stations measured a year apart, two instruments
with independent calibrations, two epochs with different atmospheric conditions —
then $\rho$ is nearer zero and the independent formula is the right one. Applying
the common-mode formula where the errors are actually independent *understates* the
uncertainty by the same $4.4\%$ in the opposite direction. Neither assumption is
safe by default; both must be justified from the acquisition.

### 4.2 The general rule for a budget

Write the budget as a table with one row per input:

| Input | Nominal | Standard uncertainty | Sensitivity $\partial g/\partial x_i$ | Contribution to $\sigma_g^2$ | Share |
|---|---|---|---|---|---|

The shares sum to one (for independent inputs) and identify the dominant term. Two
practical rules follow:

- **Do not spend effort on terms contributing less than about a tenth of the
  largest.** Because contributions add in quadrature, a term at $10\%$ of the
  largest changes the total by $0.5\%$.
- **A shared error cannot be averaged down.** No amount of repetition of the same
  instrument reduces $\sigma_B$; only an independent determination can.

## 5. Monte Carlo propagation

### 5.1 Procedure

1. **Specify the input distributions**, not merely their standard deviations. A
   Gaussian, a uniform and a triangular distribution with the same standard
   deviation produce different output distributions.
2. **Draw** $N$ independent samples of the inputs, respecting any correlation
   structure (the Cholesky factor of the input covariance matrix is the standard
   device; a shared-component construction like the one in Section 4 is the
   simplest special case).
3. **Evaluate** $g$ for each draw.
4. **Summarise** the output: mean, median, standard deviation, and quantiles. For
   skewed outputs, quote the median and a quantile range rather than the mean and a
   symmetric interval.
5. **Quote the Monte Carlo uncertainty** on each summary.
6. **Verify against an analytic value** where one exists.

### 5.2 How many draws

The Monte Carlo estimates are themselves averages, so the CLT of lesson 05 applies.
For the mean of $N$ output values with standard deviation $s$, the standard error is
$s/\sqrt N$. For a standard deviation estimated from $N$ draws, the asymptotic
standard error is

$$\operatorname{SE}(s) \approx \frac{s}{\sqrt{2(N-1)}},$$

which is why the demonstration reports standard errors of the form
$0.077621 / \sqrt{2 \times 399\,999} = 8.7\times10^{-5}$. A relative precision of
$1\%$ on a standard deviation therefore needs about $N = 5000$, and $0.1\%$ needs
about $500\,000$. Quantiles are estimated with a standard error of order
$\sqrt{p(1-p)/N}/f(q_p)$, which is well behaved in the bulk and deteriorates in the
tail — the practical reason a Monte Carlo tail quantile needs far more draws than a
median.

### 5.3 Random number generation and reproducibility

A Monte Carlo result is an experiment, and it must be reproducible. Report the
generator, the seed, and the number of draws; every demonstration in this module
uses Python's `random` module with an explicit seed, and every quoted figure is
reproducible by rerunning the script. A Monte Carlo figure whose seed is not
recorded is not reproducible in the sense that
[00-03-04 the contribution workflow](../../00-orientation/03-how-to-use-this-repo/04-contribution-workflow.md)
requires.

## 6. Where first-order propagation fails, and by how much

### 6.1 Moderate nonlinearity: a 2% understatement

Return to $g = GM/r^2$ with $r = 1000$ m and $\sigma_r/r = 0.05$, so first-order
propagation gives $\sigma_g/g_0 = 2\sigma_r/r = 0.100000$. The demonstration
computes the exact variance by Simpson quadrature over the input density (truncated
at twelve standard deviations, which removes an irrelevant region — see Section 6.4)
and compares it with a Monte Carlo ensemble:

```
    first-order sd(g)/g0        = 0.100000
    exact sd by quadrature      = 0.102118
    Monte Carlo sd              = 0.102153  (MC standard error 0.000114)
    exact E[g]/g0 by quadrature = 1.007595
    Monte Carlo mean of g/g0    = 1.007702
```

The quadrature and the Monte Carlo agree to $3\times10^{-4}$, and both are $2.1\%$
above the linearised value. The excess is the curvature of $r^{-2}$: the
second-order term of the Taylor expansion contributes $18(\sigma_r/r)^4 = 1.1\times
10^{-4}$ to the relative variance, which accounts precisely for the shift. The mean
is displaced upward by $0.76\%$, again the Jensen effect.

A $2\%$ understatement is negligible for most purposes. The value of having measured
it is that the same machinery now quantifies the failure when the approximation is
pushed further.

### 6.2 Strong nonlinearity, and an error model that breaks the physics

Keep the same function, raise $\sigma_r/r$ to $0.30$, and keep a Gaussian error
model on $r$:

```
    first-order sd(g)/g0        = 0.600000
    Monte Carlo sd              = 53349.404205  (not a meaningful quantity)
    Monte Carlo mean of g/g0    = 160.285441
    Monte Carlo median of g/g0  = 0.998296
    draws with r <= 0           = 184 (0.0460 % of draws)
```

The comparison has collapsed, and the reason is a modelling error, not an
arithmetic one. The integrals for the mean and variance of $GM/r^2$ under a Gaussian
model for $r$ **do not converge**: near $r = 0$ the integrand grows like $r^{-2}$
faster than the Gaussian density decays. With $\sigma_r/r = 0.30$ the Gaussian
places $0.046\%$ of its probability at negative radius — an unphysical region the
model was never meant to describe — and $184$ such draws in $400\,000$ dominate the
sample spread, producing the meaningless figure of $53\,349$ and a mean of $160$
times the nominal value.

**The lesson is about the model, not the arithmetic.** A positive quantity needs a
positive error model. The median of $0.9983$ is stable and useful; the mean and the
standard deviation are not estimates of anything.

### 6.3 The repair: a lognormal error model, and an exact result

Model $r$ as lognormal with median $r_0$ and relative standard deviation $s$. Then
$\ln r \sim \mathcal{N}(\ln r_0, \sigma_L^2)$ with $\sigma_L^2 = \ln(1+s^2)$, and

$$\frac{g}{g_0} = \left(\frac{r_0}{r}\right)^{2} = e^{-2Z}, \qquad
Z \sim \mathcal{N}(0, \sigma_L^2).$$

Since $e^{-2Z}$ is lognormal with parameters $0$ and $\sigma = 2\sigma_L$,

$$E\left[\frac{g}{g_0}\right] = e^{2\sigma_L^2} = (1+s^2)^{2}, \qquad
\operatorname{sd}\left(\frac{g}{g_0}\right) = (1+s^2)^{2}
\sqrt{(1+s^2)^{4} - 1}.$$

Both are exact, and the demonstration checks them against Monte Carlo:

```
       s   first order 2s      exact sd         MC sd     MC mean   exact mean
    0.05         0.100000      0.100689      0.100577    1.005057     1.005006
    0.15         0.300000      0.318979      0.318492    1.044988     1.045506
    0.30         0.600000      0.762221      0.765808    1.189413     1.188100
    0.50         1.000000      1.875915      1.868730    1.560276     1.562500
```

Every Monte Carlo column reproduces the closed form to within a few parts in
$10^3$. The first-order column, by contrast, understates the spread by $0.7\%$ at
$s = 0.05$, $6\%$ at $s = 0.15$, $27\%$ at $s = 0.30$ and $88\%$ at $s = 0.50$.

**The error is one-sided.** Because $g$ is convex in $r$ over the range the
distribution visits, the linearised spread is always too small. A linearised
uncertainty budget for a strongly nonlinear quantity is therefore **optimistic, never
conservative**, and its optimism grows rapidly with the relative uncertainty. That
is the single most important practical statement in the lesson, and it is why the
comparison between the analytic and Monte Carlo numbers belongs in every budget,
not just in teaching examples.

### 6.4 A note on divergences you cannot reach

At $\sigma_r/r = 0.05$ the same non-convergence exists formally — the Gaussian
density at $r = 0$ is smaller than its value at $r_0$ by a factor of
$\exp(-200) \approx 10^{-87}$ — but no finite sample can see it, and the truncated
quadrature reproduces the Monte Carlo result. The divergence is real mathematics and
irrelevant arithmetic, and both facts should be stated: a diverging moment is a
warning that the *model* admits physically impossible values, not a claim that the
computed number is wrong. Where the divergence is reachable, as in Section 6.2, it
is a catastrophe rather than a footnote.

## 7. What to report

A propagated uncertainty should be reported with enough structure that the reader
can see what it depends on. The recommended form:

1. **The derived value and its units**, to the precision the uncertainty justifies.
2. **The uncertainty**: one significant figure, two if the leading digit is below
   three. A standard deviation of $26.1$ m is reported as $26$ m; $0.0776$ kg/L as
   $0.08$ kg/L.
3. **The distributional assumption**, at least as "Gaussian" or "lognormal, median
   and $95\%$ range".
4. **The dominant contribution**, with its share of the variance. "$\sigma_d$ is
   dominated by the velocity assumption, which contributes $92\%$ of the variance"
   is the sentence that makes the result actionable.
5. **The correlation assumptions** for any inputs that share an error source.
6. **The verification**: the analytic value, the Monte Carlo ensemble size, its
   standard error, and their agreement. If the two disagree materially, report
   both and explain.
7. **The seed** if a Monte Carlo figure is quoted, so that it can be reproduced.

## 8. Assumptions and regime of validity

1. **First-order propagation requires small relative uncertainty.** As a working
   rule, treat linearisation as reliable when the input's standard deviation is
   below about a fifth of the scale over which the function is appreciably curved,
   and verify by Monte Carlo; Section 6.3 shows a $27\%$ error at $s = 0.30$.
2. **Variances must exist.** For heavy-tailed inputs, or for functions with
   singularities near the support of the inputs, the propagated variance may not
   exist. Check by re-running the Monte Carlo with a larger ensemble and observing
   whether the answer stabilises.
3. **Errors should be small compared with the quantity's physical range**, or the
   input distribution must be restricted to that range. Gaussian error models on
   strictly positive quantities are the commonest violation.
4. **The input distributions must be right.** The output uncertainty is only as good
   as the input uncertainties, and an omitted systematic error dominates the
   result no matter how careful the propagation.
5. **Correlation must be modelled, not assumed away.** The 44-fold standard-error
   discrepancy of Section 4.1 is not a pathological case; it is what happens
   whenever a shared error is ignored.
6. **Monte Carlo inherits the input model**, including its support restrictions and
   its tails. Sampling from a Gaussian when the quantity is positive reproduces the
   catastrophe of Section 6.2 faithfully.

## 9. Python demonstration

Run

```
python3 error_propagation.py
```

from `code/`. Standard library only; seed 20240125 with $N = 400\,000$ draws per
ensemble. Four sections: a ratio, the nonlinear $r^{-2}$ family with quadrature
comparison and the lognormal repair, a travel-time depth with its budget, and the
common-mode difference. Outputs are quoted verbatim in Sections 3.1, 3.2, 4.1,
6.1, 6.2 and 6.3.

**Reading the standard-error column.** The purpose of quoting the Monte Carlo
standard error is to make the comparison falsifiable. In Section 3.1 the
discrepancy is $2.08$ standard errors, which is marginal evidence of a real
second-order effect; in Section 3.2 it is $0.61$ standard errors, which is
consistent with noise; in Section 4.1 the wrong formula is $40$ standard errors
away while the right one is $0.83$ away. Without the standard error, all three
comparisons would read as "good agreement", which is the sort of vagueness the whole
module exists to remove.

**Breaking exercise.** In the travel-time section, change the velocity uncertainty
from $100$ m/s to $300$ m/s and predict the new $\sigma_d$ from the budget before
running. Then reduce the timing uncertainty to zero and check that $\sigma_d/d$
settles at the velocity-only value. Finally, add a shared velocity error common to
every depth in a profile and explain why the depths become correlated — and why that
correlation matters for the *gradient* of a depth profile, which may be far better
determined than any individual depth.

## 10. Common mistakes

1. **Adding standard deviations instead of variances.** Uncertainties add in
   quadrature; adding them linearly overstates the result, sometimes by a factor of
   two for two comparable terms.
2. **Mixing relative and absolute uncertainties.** The product rule needs relative;
   the sum rule needs absolute. Convert explicitly and carry the units.
3. **Ignoring correlation in a difference.** See Section 4.1.
4. **Using the linearised formula for a strongly nonlinear function.** The error is
   one-sided and optimistic, reaching nearly a factor of two at $s = 0.5$ in Section
   6.3.
5. **Applying a Gaussian error model to a strictly positive quantity** whose
   uncertainty is comparable to its mean. The model then asserts physically
   impossible values, and the propagated moments can diverge.
6. **Omitting a known systematic error** because it is hard to quantify. The
   result is then precise and wrong, which is the worst of both.
7. **Reporting a Monte Carlo uncertainty without its own standard error or its
   seed.** Unreproducible and unverifiable.
8. **Forgetting that the derivatives are evaluated at the means.** Using an observed
   value that lies several standard deviations from the mean introduces a bias of
   the same order as the linearisation error.
9. **Assuming the propagated distribution is Gaussian.** Even for independent
   Gaussian inputs, a ratio or a product is skewed; the symmetric interval then
   misstates the tails.
10. **Treating the budget as arithmetic rather than as a design tool.** Its purpose
    is to say which input to improve.

## 11. Real-world applications

- **Bouguer and free-air corrections.** Each correction — elevation, latitude,
  terrain density, tidal phase — has its own uncertainty, and the terrain-density
  assumption usually dominates. A propagated budget tells the surveyor whether to
  invest in denser elevation data or a denser gravity grid.
- **Depth conversion and reservoir volumetrics.** Depth uncertainty from velocity
  uncertainty, and gross-rock-volume uncertainty from depth, area and porosity
  uncertainties, are the standard propagation chains of exploration; the budget
  usually shows the velocity model and the porosity transform to be dominant.
- **Gravity and magnetic inversion.** Model covariance propagated through the
  forward operator via $\mathbf{C}_d = G\mathbf{C}_m G^{\mathsf T}$, which is
  Section 2.1 in its matrix form.
- **Time-lapse and differential measurements.** Common-mode cancellation is why
  4D seismic, differential InSAR and relative gravity can detect changes far below
  the absolute accuracy of a single measurement, and why the cancellation must be
  argued for each acquisition rather than assumed.
- **Geodetic strain rates.** The uncertainty of a strain rate from differenced GNSS
  velocities depends on the correlation of the velocity errors, which is dominated
  by common-mode signals such as unmodelled loading and satellite orbit error; the
  independent-error propagation of Section 2 overstates the strain-rate uncertainty
  substantially.
- **Machine-learning uncertainty quantification.** Ensemble and Monte Carlo dropout
  methods are, mathematically, Monte Carlo propagation of input and parameter
  uncertainty through a nonlinear model, and they are diagnosed with exactly the
  techniques of this lesson. See
  [21 Statistics, Bayesian Methods and Machine Learning](../../21-statistics-bayesian-ml/README.md).

## 12. Further reading

- **Taylor, J. R. (1997). *An Introduction to Error Analysis* (2nd ed.).
  University Science Books.** Level: beginner to intermediate. Chapters 3 and 4 are
  the clearest exposition of Sections 2 and 3 for laboratory work, including the
  correlation pitfalls.
- **Bevington, P. R. and Robinson, D. K. *Data Reduction and Error Analysis for the
  Physical Sciences*.** Level: intermediate. Propagation through fits and through
  derived quantities, with worked geophysical-style examples.
- **JCGM 100:2008, *Evaluation of Measurement Data — Guide to the Expression of
  Uncertainty in Measurement* (GUM).** Level: reference. The international
  standard for uncertainty budgets; the definitions of standard uncertainty,
  combined and expanded uncertainty come from here, and the document's structure is
  essentially Section 2 of this lesson applied to metrology.
- **JCGM 101:2008, *Supplement 1 to the GUM — Propagation of Distributions using a
  Monte Carlo Method*.** Level: reference. The Monte Carlo route of Section 5,
  standardised, including the draw-count and convergence criteria.
- **Tarantola, A. (2005). *Inverse Problem Theory and Methods for Model Parameter
  Estimation*. SIAM.** Level: graduate. Propagation of probability densities through
  forward models, which is the general form of which linearised propagation is the
  first-order approximation.
- **Smith, R. C. *Uncertainty Quantification: Theory, Implementation and
  Applications*.** Level: graduate. The modern computational treatment, including
  the limits of linearisation and the sampling methods that replace it.

> Note on citations: bibliographic details are given so the works can be located.
> This repository does not host or reproduce copyrighted text; confirm editions
> and availability through your library.

## 13. Related lessons

- [03 Expectation, Variance and Moments](./03-expectation-variance.md) — the
  variance algebra and the Jensen effect used throughout.
- [07 Confidence Intervals and Their Correct Interpretation](./07-confidence-intervals.md)
  — turning a propagated standard deviation into an interval, and the systematic
  error that no interval repairs.
- [08 Hypothesis Testing, p-Values and Power](./08-hypothesis-testing.md) — the
  detection threshold against which a propagated uncertainty is compared.
- [05 Sampling Distributions, Law of Large Numbers and CLT](./05-sampling-and-clt.md)
  — the Monte Carlo standard error and its limitations under heavy tails.
- [01-05-04 Taylor Series, Linearisation and Small-Angle
  Approximations](../05-single-variable-calculus/04-taylor-series.md) — the
  expansion that makes the analytic method possible.
- [01-12-04 Numerical Integration](../12-numerical-methods/04-numerical-integration.md)
  — the quadrature used here to obtain an exact variance for comparison.
- [18 Inverse Problems](../../18-inverse-problems/README.md) — covariance
  propagation, resolution and the model-space view of these budgets.
- [21 Statistics, Bayesian Methods and Machine Learning](../../21-statistics-bayesian-ml/README.md)
  — uncertainty quantification for data-driven models.

## Exercises

[`exercises/09-error-propagation-exercises.md`](./exercises/09-error-propagation-exercises.md),
with solutions in
[`exercises/09-error-propagation-solutions.md`](./exercises/09-error-propagation-solutions.md).

## Self-assessment checklist

- [ ] I can state the propagation problem and the three assumptions of the
      first-order formula.
- [ ] I can derive the propagation formula from a Taylor expansion, in scalar and
      matrix form.
- [ ] I can apply the sum, product, ratio and power rules without consulting a
      table.
- [ ] I can build a budget table, identify the dominant term, and say what would
      have to be improved to reduce the total uncertainty.
- [ ] I can handle a shared systematic error in a difference and explain its
      cancellation physically.
- [ ] I can implement Monte Carlo propagation, choose the number of draws from the
      precision required, and quote the Monte Carlo standard error.
- [ ] I can explain why linearised propagation is optimistic for a convex function,
      and quote the measured understatement at four levels of relative uncertainty.
- [ ] I can recognise an error model that asserts physically impossible values, and
      repair it with a positive model.
- [ ] I have run `code/error_propagation.py` and can point to the two comparisons
      where the Monte Carlo agrees with the analytic value and the two where it does
      not.
