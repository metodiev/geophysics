---
id: 18-06-01
title: "Taxonomy of Uncertainty: Aleatory, Epistemic, Structural"
level: doctoral
prereqs: ["18-05-01", "18-05-02", "18-05-06"]
tags: [inverse-problems, bayesian, uncertainty-quantification, aleatory, epistemic, model-discrepancy]
---

# Taxonomy of Uncertainty: Aleatory, Epistemic, Structural

All models and data in this module are **SYNTHETIC**. Every number quoted in this
lesson is printed by
[`code/uncertainty_taxonomy_demo.py`](./code/uncertainty_taxonomy_demo.py); none
is a measurement. The module README states the same.

## Learning objectives

By the end of this lesson you will be able to:

1. **Separate** total prediction uncertainty into aleatory, epistemic and
   structural components, and state the mathematical object each one is.
2. **Derive** the prediction-error budget for a linear inverse problem and
   **compute** the three components at a chosen prediction location.
3. **Predict** how each component responds to more data, a better design, and a
   better model, and **verify** the predictions numerically.
4. **Explain** why aleatory uncertainty is irreducible by adding observations of
   the same kind, while epistemic uncertainty is not.
5. **Quantify** the effect of an ill-conditioned design on the epistemic term, and
   **measure** how much a single well-placed observation reduces it.
6. **Identify** structural uncertainty as the component no statistical remedy
   reaches, and state what does reach it.
7. **Write** a one-paragraph uncertainty statement that names the components and
   the location to which they apply.

## Prerequisites

- [18-05-01 Bayes' Theorem as an Inverse-Problem Formulation](../05-bayesian-inversion/01-bayes-inverse-formulation.md)
  — the posterior and its covariance.
- [18-05-02 Constructing Likelihoods and Error Models](../05-bayesian-inversion/02-likelihood-models.md)
  — the noise model, which is where aleatory uncertainty enters.
- [18-05-06 Posterior Summaries](../05-bayesian-inversion/06-posterior-summary.md)
  — how to report a posterior as an interval.

## 1. Intuition: three kinds of not-knowing

The word "uncertainty" hides three different things, and they have different
remedies. Confusing them is the commonest reason an uncertainty statement is
either useless or dishonest.

**Aleatory uncertainty** is randomness in the process itself: a measurement error,
a turbulent velocity fluctuation, the position of a fracture. It is a property of
the system, not of our knowledge, and it does not shrink when we learn more, unless
we change the physical situation or average over it.

**Epistemic uncertainty** is ignorance of a fixed but unknown quantity: the average
velocity of a layer, the depth of a contact. It is a property of our knowledge, it
shrinks as data accumulate, and it can be attacked by better design.

**Structural uncertainty** (also called model discrepancy) is the possibility that
the mathematical form of the forward model is wrong: that the true relation is not
$d = Gm$, that a layer is not a layer, that the physics omits a term. It is neither
a variance nor a distribution in general, and no amount of data analysed *inside*
the wrong model will reduce it.

A useful discipline is to write down, for every number reported, which of the three
it belongs to. A prediction interval that quotes only the aleatory part is too
narrow; one that quotes only the epistemic part is answering a different question;
one that omits the structural part is claiming a completeness that no data set can
establish.

## 2. A prediction-error budget, derived

Take a linear model $d = Gm + e$ with $e\sim\mathcal{N}(0,\sigma^2I)$ and a
Gaussian posterior $m \sim \mathcal{N}(m_{\text{post}}, C_{\text{post}})$. We wish
to predict a scalar quantity $y^* = a^{\top}m$ at a location or a weighted
combination $a$. The posterior predictive for a *noisy observation* of $y^*$ is

$$
y^*_{\text{obs}} = a^{\top}m + \varepsilon, \qquad \varepsilon\sim\mathcal{N}(0,\sigma^2),
$$

so

$$
\operatorname{Var}(y^*_{\text{obs}}) = \underbrace{a^{\top}C_{\text{post}}\,a}_{\text{epistemic}}
+ \underbrace{\sigma^2}_{\text{aleatory}} .
$$

This is the whole decomposition for a correctly specified model. If the true
relation is instead $d = Gm + \beta^{\top}\phi(x) + e$, with $\phi$ a term the model
omits, then the *bias* at $a$ is $b(a) = \beta^{\top}\phi(a)$ and the mean square
error of the prediction becomes

$$
\mathbb{E}\bigl[(y^*_{\text{pred}} - y^*_{\text{true}})^2\bigr]
= \underbrace{b(a)^2}_{\text{structural}}
+ \underbrace{a^{\top}C_{\text{post}}\,a}_{\text{epistemic}}
+ \underbrace{\sigma^2}_{\text{aleatory}} .
$$

Three terms, three remedies: physics for the first, design and data for the second,
and nothing for the third except repeated measurement or averaging.

### 2.1 Worked numeric example

The demonstration fits $d = m x$ to eight SYNTHETIC stations at $x = 1,\dots,8$
(units of km) generated from

$$
d(x) = 2.0\,x + 0.005\,x^2 + \mathcal{N}(0, 0.2^2),
$$

so the quadratic term is *structural*: the fitted model does not contain it. The
fit gives $m = 2.0482 \pm 0.0140$ and $\sum x^2 = 204\ \mathrm{km^2}$, so the
epistemic variance at a location $x^*$ is $x^{*2}\sigma^2/\sum x^2 =
x^{*2}(0.04)/204$, and the bias is $0.005x^{*2}$:

| $x^*$ (km) | bias (units) | epistemic s.d. | aleatory s.d. | total RMSE | bias share |
|---|---|---|---|---|---|
| 2.0 | 0.0200 | 0.0280 | 0.2000 | 0.2029 | $1.0\%$ |
| 4.0 | 0.0800 | 0.0560 | 0.2000 | 0.2226 | $12.9\%$ |
| 6.0 | 0.1800 | 0.0840 | 0.2000 | 0.2819 | $40.8\%$ |
| 8.0 | 0.3200 | 0.1120 | 0.2000 | 0.3936 | $66.1\%$ |
| 12.0 | 0.7200 | 0.1680 | 0.2000 | 0.7659 | $88.4\%$ |

At $x^* = 2$ km the budget is essentially all aleatory noise: quoting a total
standard deviation of $0.2029$ is a statement about the instrument. At $x^* = 12$
km the structural bias contributes $88.4\%$ of the mean square error: quoting a
total of $0.7659$ is a statement about the physics, and calling it "noise" would
be wrong. The three columns are printed separately precisely because they have
different names in a report.

## 3. What each component responds to

| component | more data? | better design? | better physics? |
|---|---|---|---|
| aleatory | no | no | no (only by changing the measurement) |
| epistemic | yes, as $1/\sum x_i^2$ | yes, substantially | partly (a tighter prior) |
| structural | no | no | yes, and only by changing the model |

The demonstration makes the design claim concrete with the same number of extra
stations used two ways:

- doubling the station density inside $1$–$8$ km raises $\sum x^2$ from $204$ to
  $398\ \mathrm{km^2}$ and reduces the epistemic variance at $x^* = 4$ km by a
  factor $1.951$;
- extending the aperture to $16$ km instead raises $\sum x^2$ to
  $1496\ \mathrm{km^2}$ and reduces the same variance by a factor $7.333$.

The epistemic standard deviation at $4$ km falls from $0.05601$ to $0.04010$ in the
first case and to $0.02068$ in the second. **The design, not the count, controls
the epistemic term** — and neither choice touches the aleatory $0.2000$ or the
structural bias $0.0800$. A report that says "we collected more data and reduced
the uncertainty" must say which term fell, at which location.

## 4. Ill-conditioning is epistemic, not aleatory

Epistemic uncertainty is not only a matter of how much data there is; it is a
matter of what the data can separate. The demonstration's SYNTHETIC two-parameter
design

$$
G = \begin{bmatrix}1 & 1\\ 1.01 & 1\end{bmatrix}, \qquad \sigma = 0.05
$$

has singular values $2.005$ and $0.005$. The posterior standard deviations are
$7.0711$ and $7.1065$, the posterior correlation is $-1.0000$ to four decimals,
and the standard deviation along the worst direction is $10.0251$ — enormous
compared with the data noise, because the two columns are nearly parallel, so
$m_1 - m_2$ is only weakly constrained.

Adding **one** datum that separates the parameters, $d_3 = m_1 - m_2$, gives
posterior standard deviations $0.0305$ and $0.0306$; the standard deviation along
the previously worst direction falls to $0.0354$, a reduction by a factor of
$283.6$. No extra precision was bought; one well-chosen observation replaced the
information that the design had been hiding. This is the practical content of
[18-02-04 SVD Analysis: Model Resolution and Data Importance](../02-linear-inverse-problems/04-svd-analysis-inverse.md),
expressed as an uncertainty.

## 5. Structural uncertainty: the component statistics cannot touch

The quadratic term in Section 2 is small at $x^* = 2$ and dominant at
$x^*=12$, and no increase in the number of stations *inside the same model*
removes it: the fit improves, the posterior narrows, and the prediction stays
biased. This is the defining property of structural uncertainty and it is why
model validation is a separate discipline, treated in
[19-07-03 Model Validation](../../19-numerical-modeling-hpc/07-verification-validation-uncertainty/03-model-validation.md),
and why a discrepancy term in the likelihood is the honest way to include it when
it cannot be eliminated. Two practical points follow.

- **Report the bias, or model it.** If a structural term is known approximately,
  it can be added to the likelihood as a mean offset with a prior; then it appears
  in the budget as a variance. If it is not known, the honest statement is that an
  unquantified systematic error remains.
- **Synthetic tests can detect it.** Generating data from a *more complete* physics
  than the inversion assumes, and asking whether the inversion recovers the truth,
  is the standard way to expose structural error. This is the workflow of
  [18-08-02 Synthetic Testing, Checkerboards and Recovery Tests](../08-practical-inversion-workflow/02-synthetic-testing.md).

## 6. Reporting: three components, one location

An uncertainty statement that can be checked names the component, the location and
the source of each number. For the extended-aperture case at $x^* = 4$ km the
demonstration prints

| component | value (data units) | source |
|---|---|---|
| aleatory s.d. | 0.200 | the measurement process |
| epistemic s.d. | 0.02068 | the posterior, from 16 stations over 1–16 km |
| structural bias | 0.0800 | the omitted $x^2$ term, $0.005 x^{*2}$ |
| total RMSE | 0.2164 | the three combined in quadrature |

The total is dominated by the aleatory term *at this location*. At $x^* = 12$ km
the ordering reverses. A single number without the location and without the split
cannot be audited.

## 7. Assumptions and regime of validity

1. **The three-way split requires a mean-square-error framework.** If a
   probability statement is required rather than a moment, the components combine
   as distributions, and a sum of variances is no longer the whole story.
2. **Independence of the components is assumed.** Correlated structural error and
   epistemic uncertainty require the cross terms.
3. **The bias is taken as known in the budget.** In practice $\beta$ is unknown;
   then the structural term is itself uncertain, and the budget needs a prior on it
   — a discrepancy model.
4. **The aleatory term is the likelihood's variance.** If the likelihood is
   misspecified, the label is wrong; a correlated-noise model changes which part of
   the residual is called aleatory.
5. **"Irreducible" is a statement about the measurement, not the physics.** Averaging
   many repeated measurements reduces the aleatory contribution to an average, not
   to the individual prediction.
6. **Beyond the data aperture, epistemic growth is an extrapolation.** The
   $x^{*2}$ growth of the epistemic variance follows from the design matrix; a
   different parameterisation gives a different law.

## 8. Demonstration and exercises

[`code/uncertainty_taxonomy_demo.py`](./code/uncertainty_taxonomy_demo.py) computes
the budget, the design comparison and the ill-conditioned example, prints them with
units, and exits $0$ in a fraction of a second. Exercises and worked solutions:
[`exercises/01-uncertainty-taxonomy-exercises.md`](./exercises/01-uncertainty-taxonomy-exercises.md)
and
[`exercises/01-uncertainty-taxonomy-solutions.md`](./exercises/01-uncertainty-taxonomy-solutions.md).

## Mastery checkpoint

**(a)** Write the mean-square-error identity of Section 2 and name each term.
**(b)** At $x^* = 6$ km in the demonstration's budget, compute the total RMSE from
the three components and check it against the printed value.
**(c)** A design has $\sum x_i^2 = 100\ \mathrm{km^2}$ and $\sigma = 0.1$. Compute
the epistemic standard deviation at $x^* = 5$ km, and state what it becomes if the
aperture is doubled while the station count is unchanged.
**(d)** Explain in two sentences why no amount of additional data of the same type
removes a structural bias.

## Common pitfalls

1. **Calling everything "noise".** A bias is not a variance, and it does not add in
   quadrature with one until it is modelled as a distribution.
2. **Quoting a total uncertainty without the location.** The ordering of the three
   components reverses between $x^*=2$ and $x^*=12$ in the measured example.
3. **Assuming more data reduces all uncertainty.** Measured: it leaves the
   aleatory and structural terms unchanged.
4. **Ignoring the design.** One separating datum reduced the worst-direction
   epistemic standard deviation by a factor $283.6$.
5. **Reporting a posterior interval as if it were a prediction interval.** The
   prediction interval includes the aleatory term.
6. **Hiding structural error inside an inflated noise variance.** It then appears
   in the wrong column with the wrong remedy.
7. **Extrapolating the epistemic law beyond the aperture.** Its form depends on the
   parameterisation and the design.

## Further reading

- **Kennedy, M. C., & O'Hagan, A. (2001). Bayesian calibration of computer models.
  *Journal of the Royal Statistical Society: Series B*, 63(3), 425–464.** Level:
  research. The discrepancy term as a statistical object, which is how structural
  uncertainty is given a distribution.
- **Tarantola, A. (2005). *Inverse Problem Theory and Methods for Model Parameter
  Estimation*. SIAM.** Level: research. Model space, data space and the role of
  theory error.
- **Gelman, A., Carlin, J. B., Stern, H. S., Dunson, D. B., Vehtari, A., &
  Rubin, D. B. (2013). *Bayesian Data Analysis* (3rd ed.). CRC Press.** Level:
  research. Posterior predictive distributions and the difference between
  inferring parameters and predicting observations.
- **BIPM, IEC, ISO, IUPAC, IUPAP, & OIML (2008). *Evaluation of Measurement
  Data — Guide to the Expression of Uncertainty in Measurement* (JCGM 100:2008).**
  Level: reference. Type A and Type B uncertainty evaluation, the metrological
  counterpart of the aleatory/epistemic split.

## Related modules

- [02 Monte Carlo Propagation and Its Convergence](02-monte-carlo-uq.md) — how to
  propagate all three components when the forward model is nonlinear.
- [03 Sensitivity Analysis: Local, Global, Sobol Indices](03-sensitivity-analysis.md)
  — which uncertain input drives the epistemic term.
- [05 Visualising and Communicating Uncertainty](05-uncertainty-visualisation.md) —
  the figure-side counterpart of Section 6.
- [06 Decision-Making Under Uncertainty and Value of Information](06-decision-under-uncertainty.md)
  — the components that matter for a decision are not always the largest.
- [18-05-02 Constructing Likelihoods and Error Models](../05-bayesian-inversion/02-likelihood-models.md).
- [18-02-04 SVD Analysis: Model Resolution and Data Importance](../02-linear-inverse-problems/04-svd-analysis-inverse.md).
- [19-07-03 Model Validation](../../19-numerical-modeling-hpc/07-verification-validation-uncertainty/03-model-validation.md).
