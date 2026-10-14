---
id: 21-02-05
title: "Geostatistics Combined with Geophysical Inversion"
level: research
prereqs: ["21-02-04", "18-02-06"]
estimated_minutes: 80
tags: [geostatistics, inversion, bayesian-inversion, prior-covariance, resolution, cokriging]
---

# Geostatistics Combined with Geophysical Inversion

## Learning objectives

By the end of this lesson you will be able to:

1. **Formulate** a linear geophysical inverse problem with a Gaussian prior whose
   covariance is a variogram model, and **write** the posterior mean and
   covariance.
2. **Show** that the posterior mean is the kriging/cokriging estimator, so that
   geostatistics and Bayesian inversion are the same construction.
3. **Compute** the resolution matrix and **state** what its trace measures.
4. **Explain** the trade between resolution and posterior variance produced by
   the prior range, with numbers.
5. **Compare** a white, a correctly specified and a mis-specified prior, and
   **state** which of the three is best and why the comparison is not as simple
   as it looks.
6. **State** what geostatistical inversion adds beyond kriging and what it
   assumes.

The model, the forward operator and the noise in this lesson are **SYNTHETIC**:
a random field with a stated covariance, a stated boxcar smoothing operator and
a stated noise level. No measured geophysical data are used.

## Prerequisites

- [21-02-04 Conditional Simulation and Uncertainty Realisations](04-simulation-geostatistics.md) —
  the ensemble view of a geostatistical model.
- [18-02-06 Data Weighting and Error Covariance Specification](../../18-inverse-problems/02-linear-inverse-problems/06-weighting-and-covariance.md) —
  the data covariance and weighted least squares.
- [21-02-02 Variograms, Covariance and Model Fitting](02-variograms.md) —
  the covariance model used as a prior.

## 1. Intuition: the prior *is* the geostatistics

A linear inverse problem asks for a model $m$ given data $d = Gm + e$, and it is
usually under-determined: the operator $G$ has a null space, so infinitely many
models fit. Something must choose among them. That something is a prior, and in
geophysics a variogram is the prior. Saying "the property has a range of
$5\ \mathrm{km}$ and a sill of $0.3$" is a statement about which models are
plausible before any data, and writing it as a covariance matrix turns it into
the machinery of Bayes.

The result of doing this is not a new method; it is kriging in disguise.
Kriging is ordinary (or simple) cokriging, and cokriging is the posterior mean of
a linear Gaussian inverse problem. Seeing that equivalence is the point of this
lesson: it removes the apparent choice between "geostatistics" and "inversion"
and replaces it with a single question — is the covariance model right, and does
the data covariance describe the errors?

## 2. The Gaussian linear inverse problem

Take a prior $m \sim \mathcal N(m_0, C_m)$ with $C_m$ the covariance implied by a
variogram model, and data errors $e \sim \mathcal N(0, C_d)$ independent of $m$.
The posterior is Gaussian with

$$\boxed{\;m_{\text{post}} = m_0 + C_m G^{\mathsf T}
\big(G C_m G^{\mathsf T} + C_d\big)^{-1}(d - G m_0),\;}$$

$$C_{\text{post}} = C_m - C_m G^{\mathsf T}\big(G C_m G^{\mathsf T} +
C_d\big)^{-1} G C_m .$$

Writing $A = C_m G^{\mathsf T}(G C_m G^{\mathsf T} + C_d)^{-1}$, so that
$m_{\text{post}} = m_0 + A(d - Gm_0)$, three matrices describe the answer:

- the **resolution matrix** $R = AG$, whose rows show how a unit model perturbation
  is spread over the estimate; $\operatorname{tr}R$ counts the number of
  independent model parameters the data actually determine;
- the **posterior covariance** $C_{\text{post}}$, whose trace is the total
  remaining model variance;
- the **bias**, $m_{\text{post}} - m_{\text{true}} = (R - I)m_{\text{true}} +
  Ae$ under a linear truth, the first term being prior-induced and the second
  noise-induced.

The reciprocal relationship is exact and worth stating: for the same data, a
stronger prior (longer range, larger sill) increases the bias term and decreases
the posterior variance. There is no free lunch, only a choice of how to pay.

## 3. The equivalence with cokriging

If the data are direct observations of the model plus noise, $G = I$ and
$C_d = \sigma^{2}_e I$, the posterior mean becomes

$$m_{\text{post}} = m_0 + C_m\big(C_m + \sigma^{2}_e I\big)^{-1}(d - m_0),$$

which is simple kriging with a measurement-error term — the "filtered kriging" of
[21-02-03](03-kriging.md) §2. If the mean is unknown, augmenting the state with a
constant reproduces ordinary kriging. If the data are a different physical
quantity (seismic amplitude or gravity), the same formula with the cross
covariance between model and data is **cokriging**. Geostatistical inversion is
therefore:

> kriging with a forward operator between the quantity and the measurement,
> plus a complete posterior covariance rather than a pointwise one.

The practical difference from kriging is that the posterior covariance is a full
matrix: it knows that neighbouring cells are correlated, so an exceedance
probability computed from it accounts for spatial structure, while a pointwise
kriging variance does not.

## 4. Worked example

The demonstration inverts a $60$-cell one-dimensional model with a Gaussian
prior whose covariance is exponential with e-folding range $10\ \mathrm m$. The
forward operator is a normalised $5$-cell boxcar (a stand-in for a smoothed
sensing kernel) and the data have noise standard deviation $0.05$, giving a data
variance of $0.5586$ against a model variance of $0.9602$ — the operator removes
$42\ \%$ of the model variance before the data are even formed.

| prior | RMSE vs truth | mean posterior variance | $\operatorname{tr}R/n$ |
|---|---|---|---|
| white ($\lambda \to 0$) | 0.2304 | 0.1511 | 0.8489 |
| true range $10\ \mathrm m$ | 0.1989 | 0.0701 | 0.7095 |
| long range $30\ \mathrm m$ | 0.2281 | 0.0366 | 0.5745 |

Three readings of the table:

1. **The correctly specified prior wins on error** — RMSE $0.1989$ against
   $0.2304$ for the white prior. A wrong prior still helps, but less.
2. **A stronger prior buys certainty, not accuracy.** The long-range prior has
   less than half the posterior variance of the true-range prior
   ($0.0366$ vs $0.0701$) and yet a *larger* error ($0.2281$ vs $0.1989$). It is
   more confident and less right, which is the signature of over-regularisation.
3. **Resolution falls as the prior strengthens.** $\operatorname{tr}R/n$ drops
   from $0.849$ (white) through $0.710$ (true) to $0.575$ (long): the long-range
   prior can resolve only $57\ \%$ of the model parameters, and its posterior
   variance is small precisely because it does not attempt to resolve the rest.

The bias column makes the same point without the noise: the mean bias against
the truth grows monotonically, $-0.0058$, $-0.0069$, $-0.0073$, though all three
are small relative to the noise term, which dominates.

**What no prior would give you.** The unregularised least-squares solution — the
inverse of the boxcar applied to the data — has RMSE $0.8182$, four times the
geostatistical posterior's. The operator is nearly singular, so inverting it
amplifies the $0.05$ data noise into a model error of order $0.8$. The prior is
what makes the problem answerable, and its cost is the bias column above.

## 5. Geostatistical inversion in practice

- **Seismic-to-property inversion**: the model is acoustic impedance or a facies
  indicator, the data are seismic traces, and the variogram sets the vertical and
  lateral continuity. The posterior is sampled by Markov-chain or by
  geostatistical simulation with a likelihood constraint (the "Bayesian
  sequential Gaussian simulation" family).
- **Gravity and magnetics**: the operator is linear in density or susceptibility,
  so the formulas above apply directly.
- **Joint inversion**: several data types share one model; the data covariance
  $C_d$ becomes block-diagonal with the cross terms if errors are correlated, and
  the prior covariance is still one variogram per property.
- **Uncertainty for a decision**: because the posterior is a full covariance, a
  Monte-Carlo ensemble of posterior draws — not merely $\pm 2$ standard
  deviations — is the honest deliverable.

The failure mode to guard against is the same in every case: **the prior range is
chosen from the same data whose resolution it controls.** A range fitted to the
smoothed data is longer than the true range, which over-smooths and understates
the posterior variance, which then understates risk.

## Assumptions and regime of validity

1. **A Gaussian prior and Gaussian errors.** The closed forms need both; for
   facies or bounded properties the same logic holds but the computation becomes
   sampling rather than a matrix inverse.
2. **A linear (or linearised) forward operator.** Nonlinear operators need an
   iterative scheme, and the posterior becomes non-Gaussian.
3. **A correct $C_m$.** A mis-specified range biases the answer, as the table
   shows.
4. **A correct $C_d$.** Under-stated data errors over-regularise and understate
   uncertainty.
5. **$C_d$ invertibility and conditioning.** With very small noise the inversion
   of $G C_m G^{\mathsf T} + C_d$ is ill-conditioned; the covariance prior is what
   regularises it.
6. **The prior is not evidence.** $\operatorname{tr}R/n$ small means the data
   determine little; reporting a small posterior variance in that regime is a
   statement about the prior, not about the Earth.

## The honest summary

Geostatistical inversion is Bayesian linear inversion with a variogram as the
prior covariance, and the demonstration shows the exchange rate it offers. The
correctly specified prior reduced the model error from the white-prior $0.2304$
to $0.1989$ while cutting the posterior variance by more than half; the
over-long-range prior cut the variance further, to $0.0366$, while making the
error *larger*, $0.2281$, and resolving only $57\ \%$ of the model. Without any
prior at all the error was $0.8182$, four times worse, because the operator
amplifies noise. What these numbers do **not** establish is that any of these
priors is right for a real survey: the prior range was imposed here and, in
practice, is usually fitted to data whose resolution it then controls.

## Python demonstration

[`code/geostatistics_inversion_demo.py`](./code/geostatistics_inversion_demo.py)
prints every number quoted above. It:

1. builds the forward problem, the data and the noise;
2. computes the posterior mean, posterior variance and resolution for three
   prior covariances;
3. compares their RMSE, bias and posterior standard deviation with the
   unregularised least-squares solution.

```bash
cd 21-statistics-bayesian-ml/02-geostatistics/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python geostatistics_inversion_demo.py
```

It runs in well under a second and prints only text.

## Exercises

Graded problems are in
[`exercises/05-geostatistics-inversion-exercises.md`](./exercises/05-geostatistics-inversion-exercises.md)
with worked solutions in
[`exercises/05-geostatistics-inversion-solutions.md`](./exercises/05-geostatistics-inversion-solutions.md).
The ★★★ problems ask you to design a prior-sensitivity and a covariance-ensemble
study.

## Mastery checkpoint

Without notes, a linear inversion with a Gaussian prior gives posterior RMSE
$0.1989$, mean posterior variance $0.0701$ and $\operatorname{tr}R/n = 0.7095$;
a longer-range prior gives $0.2281$, $0.0366$ and $0.5745$.

1. State which prior is better and by what criterion.
2. Compute the ratio of posterior variances and the ratio of RMSEs between the
   two priors, and explain why they move in opposite directions.
3. State what $\operatorname{tr}R/n = 0.57$ implies about the data's information
   content.
4. A colleague reports the long-range result as more reliable because its
   uncertainty is smaller. State the error in that inference.

## Common pitfalls

1. **Reading a small posterior variance as accuracy.** Over-regularisation
   produces exactly that, together with a larger error.
2. **Choosing the prior range from the data it regularises.** The range fitted to
   smoothed data is too long, and the uncertainty is then understated.
3. **Confusing a pointwise kriging variance with a posterior covariance.** Only
   the latter carries the spatial correlation needed for exceedance
   probabilities.
4. **Ignoring the bias term.** A strong prior shifts the answer, and the shift is
   not visible in the posterior variance.
5. **Using a Gaussian posterior for a non-Gaussian property.** Facies and bounded
   properties need sampling, not a matrix inverse.
6. **Reporting one posterior realisation.** The deliverable is the ensemble, as in
   [21-02-04](04-simulation-geostatistics.md).

## Where this is used

- **Seismic reservoir characterisation**: impedance and facies with a
  geostatistical prior.
- **Potential-field inversion**: density and susceptibility with covariance
  priors.
- **Hydrological inversion**: transmissivity fields conditioned on head and
  tracer data.
- **Geotechnical site investigation**: combining sparse boreholes with dense
  geophysics.
- **Mineral exploration**: integrating geophysical inversions with assay data for
  prospectivity and uncertainty.

## Related lessons

- [21-02-04 Conditional Simulation and Uncertainty Realisations](04-simulation-geostatistics.md) —
  the sampling route to the same posterior.
- [21-02-03 Kriging: Simple, Ordinary, Universal, Indicator](03-kriging.md) —
  the estimator that the posterior mean reproduces.
- [18-05-01 Bayesian Inversion: Formulation](../../18-inverse-problems/05-bayesian-inversion/README.md) —
  the general inverse-theory treatment of the formulas here.
- [21-03-01 The Bayesian Paradigm and Subjective Probability](../03-bayesian-inference/01-bayesian-paradigm.md) —
  the subjective-probability reading of the prior.
- [21-04-04 Regularisation: Ridge, Lasso, Early Stopping](../04-machine-learning-fundamentals/04-regularization-ml.md) —
  the same trade seen from the machine-learning side.

## Self-assessment checklist

- [ ] I can write the Gaussian posterior mean and covariance.
- [ ] I can compute and interpret a resolution matrix trace.
- [ ] I can state the equivalence between posterior mean and kriging.
- [ ] I can explain the resolution–posterior-variance trade with numbers.
- [ ] I can compare a white, correct and mis-specified prior.
- [ ] I can state what a small posterior variance does and does not mean.
