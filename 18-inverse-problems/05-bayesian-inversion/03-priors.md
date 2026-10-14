---
id: 18-05-03
title: "Priors: Informative, Reference and Their Influence"
level: research
prereqs: ["18-05-01", "18-03-01"]
tags: [inverse-problems, bayesian, uncertainty-quantification, priors, reference-priors, regularisation]
---

# Priors: Informative, Reference and Their Influence

All models and data in this module are **SYNTHETIC**. The data values, prior
widths and the physical bound used below are chosen teaching values; every number
quoted is printed by [`code/priors_demo.py`](./code/priors_demo.py).

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the conjugate Gaussian update, and interpret the posterior precision
   as the sum of prior and data precisions.
2. **Compute** the shrinkage factor $\sigma^2/(s_0^2+\sigma^2)$ for a single
   datum and predict how the posterior mean moves as the prior width changes.
3. **Quantify** prior-data conflict in units of the predictive standard deviation,
   and state what a given conflict does to the posterior.
4. **Derive** the Jeffreys prior for a scale parameter from the Fisher
   information, and **demonstrate** its invariance under reparameterisation by
   integrating in a transformed coordinate.
5. **Explain** what happens to a posterior that meets a hard physical bound, and
   the summary that must accompany it.
6. **Decide** whether a prior is strong enough to be doing the work, using the
   measured prior share of the total precision.
7. **State** the regime in which a reference prior is a defensible default, and
   the regime in which it is not.

## Prerequisites

- [18-05-01 Bayes' Theorem as an Inverse-Problem Formulation](01-bayes-inverse-formulation.md)
  — the posterior as prior times likelihood.
- [18-03-01 Why Regularisation Is Physically and Statistically Justified](../03-regularization/01-why-regularize.md)
  — the deterministic face of the same argument.
- [21-03-02 Conjugate Priors](../../21-statistics-bayesian-ml/03-bayesian-inference/02-conjugate-priors.md)
  — the general conjugate family this lesson instantiates.

## 1. Intuition: a prior is a statement about what is admitted

Every inversion admits something. A bounded inversion admits only models inside a
box; a smooth inversion admits only models whose roughness penalty is finite; a
minimum-norm inversion admits the smallest model. These are prior statements that
are usually left implicit, and being implicit they are not audited. Making the
prior explicit has three consequences worth stating at the outset.

- It becomes **auditable**: the admitted set can be written down and checked
  against physics.
- It becomes **falsifiable**: if the data disagree with the prior, the disagreement
  can be measured, and a large disagreement is a finding rather than a nuisance.
- It becomes **unavoidable**: there is no prior-free posterior, only a prior that
  has not been written down. The claim "I used no prior" is a claim to a specific
  (usually flat, often improper) prior with its own consequences.

## 2. Conjugate update for a Gaussian location

Let one datum be observed with known $\sigma$,
$d \mid m \sim \mathcal{N}(m,\sigma^2)$, and let the prior be
$m \sim \mathcal{N}(m_0,s_0^2)$. Multiplying the two Gaussians and completing the
square gives a Gaussian posterior with

$$
\frac{1}{s_{\text{post}}^2} = \frac{1}{s_0^2} + \frac{1}{\sigma^2},
\qquad
m_{\text{post}} = m_0 + K\,(d - m_0),
\qquad
K = \frac{s_0^2}{s_0^2+\sigma^2}.
$$

Two readings of the same formula. As **precision addition**: the posterior
precision is the sum, so each source contributes in proportion to its own
precision. As **shrinkage**: the posterior sits a fraction $K$ of the way from
the prior mean to the datum.

For $N$ independent data with mean $\bar d$, replace $\sigma^2$ by
$\sigma^2/N$ everywhere. Then the prior share of the posterior precision is

$$
\frac{1/s_0^2}{\,1/s_0^2 + N/\sigma^2\,}.
$$

The demonstration reports this share for a SYNTHETIC case with $N = 9$ and
$\sigma = 1$:

| $s_0$ | prior precision | data precision | prior share |
|---|---|---|---|
| 0.1 | 100.000 | 9.000 | $91.74\%$ |
| 0.3 | 11.111 | 9.000 | $55.25\%$ |
| 0.5 | 4.000 | 9.000 | $30.77\%$ |
| 1.0 | 1.000 | 9.000 | $10.00\%$ |
| 2.0 | 0.250 | 9.000 | $2.70\%$ |
| 5.0 | 0.040 | 9.000 | $0.44\%$ |
| 20.0 | 0.003 | 9.000 | $0.03\%$ |

This table is the most useful object in the lesson. It converts a vague statement
("the prior is weak") into a number: **at $s_0 = 1$ the prior carries ten per cent
of the information in the answer, and at $s_0 = 0.3$ it carries more than half.**
A prior that carries half the information must be defended, and a prior that
carries $0.03\%$ cannot stabilise a null direction because it carries no
information there either. That trade-off is the whole difficulty: a prior weak
enough to be uncontroversial is also too weak to regularise.

## 3. Worked example: the shrinkage factor, numerically

The demonstration draws a single SYNTHETIC datum from $\mathcal{N}(1,1)$ and
obtains $d = 0.5291$. With prior mean $m_0 = 0$ and a prior standard deviation
$s_0$, the posterior is $m \sim \mathcal{N}(K d,\ s_0^2\sigma^2/(s_0^2+\sigma^2))$:

| $s_0$ | $K$ | $m_{\text{post}}$ | $s_{\text{post}}$ | $95\%$ interval |
|---|---|---|---|---|
| 0.10 | 0.010 | 0.0052 | 0.0995 | $[-0.190,\,+0.200]$ |
| 0.30 | 0.083 | 0.0437 | 0.2873 | $[-0.520,\,+0.607]$ |
| 0.50 | 0.200 | 0.1058 | 0.4472 | $[-0.771,\,+0.982]$ |
| 1.00 | 0.500 | 0.2645 | 0.7071 | $[-1.121,\,+1.650]$ |
| 2.00 | 0.800 | 0.4233 | 0.8944 | $[-1.330,\,+2.176]$ |
| 5.00 | 0.962 | 0.5087 | 0.9806 | $[-1.413,\,+2.431]$ |
| 20.0 | 0.998 | 0.5277 | 0.9988 | $[-1.430,\,+2.485]$ |

The datum is $0.5291$. A prior with $s_0 = 0.1$ holds the answer at $0.0052$; a
prior with $s_0 = 20$ releases it to $0.5277$. Both are "Bayesian inversions".
The difference between them is $0.52$ in a problem whose measurement standard
deviation is $1$. Nothing in the data distinguishes the two analyses; only the
prior does, and the prior must be reported.

## 4. Prior-data conflict, quantified

A prior can be wrong. The right way to measure how wrong is in units of the
*predictive* standard deviation of the data, $\sqrt{s_0^2 + \sigma^2/N}$, not in
units of the prior alone. With $N = 9$, $\sigma = 1$ so $\sigma/\sqrt N = 0.3333$,
and a data mean $\bar d = 1.4421$, the demonstration reports:

| $m_0$ | $m_{\text{post}}$ | posterior std | standardised mismatch |
|---|---|---|---|
| 0.00 | 0.9983 | 0.2774 | 2.40 |
| 0.50 | 1.1522 | 0.2774 | 1.57 |
| 1.00 | 1.3060 | 0.2774 | 0.74 |
| 2.00 | 1.6137 | 0.2774 | 0.93 |
| 4.00 | 2.2291 | 0.2774 | 4.26 |

With $m_0 = 4$ the mismatch is $4.26$ standard deviations and the posterior mean
is dragged from the data mean $1.4421$ to $2.2291$ — a $55\%$ displacement. A
mismatch of that size is not a reason to discard the analysis; it is a result.
The honest response is to report the posterior under the stated prior *and* the
likelihood alone, so the reader can see how far the prior moved the answer. The
Gibbs-sampling lesson [04](04-mcmc.md) does this routinely by starting chains from
dispersed prior draws.

## 5. Reference priors and invariance

A **reference** (default, or Jeffreys) prior is constructed so that the analysis
is invariant under a change of parameterisation. For a sampling model
$p(d\mid\theta)$, the Jeffreys prior is

$$
\pi(\theta) \propto \sqrt{\det I(\theta)},
\qquad
I(\theta)_{ij} = -\mathbb{E}\!\left[\frac{\partial^2 \ln p(d\mid\theta)}
{\partial \theta_i \partial \theta_j}\right].
$$

For a scale parameter the result is a power law. Take $x_i \sim \mathcal{N}(0,
\sigma^2)$, $i = 1,\dots,n$. Then
$\ln p = \text{const} - n\ln\sigma - \sum x_i^2/(2\sigma^2)$ and

$$
\frac{\partial \ln p}{\partial \sigma} = -\frac{n}{\sigma} + \frac{\sum_i x_i^2}{\sigma^3},
\qquad
\frac{\partial^2 \ln p}{\partial \sigma^2} = \frac{n}{\sigma^2} - \frac{3\sum_i x_i^2}{\sigma^4},
$$

and since $\mathbb{E}\bigl[\sum_i x_i^2\bigr] = n\sigma^2$,

$$
I(\sigma) = -\mathbb{E}\!\left[\frac{\partial^2\ln p}{\partial\sigma^2}\right]
= -\frac{n}{\sigma^2} + \frac{3n\sigma^2}{\sigma^4} = \frac{2n}{\sigma^2},
$$

so $\pi(\sigma) \propto \sqrt{I(\sigma)} \propto 1/\sigma$, which is flat in
$\ln\sigma$.

### 5.1 Measuring the invariance

The demonstration integrates the same posterior on a grid uniform in
$u = \ln\sigma$ so that the change of variable is exact, with $n = 9$ SYNTHETIC
samples ($\sqrt{\sum x_i^2} = 2.9409$, so $\hat\sigma = 0.9803$):

| prior | $95\%$ interval for $\sigma$ |
|---|---|
| flat in $\sigma$ | $[0.7020,\,1.9309]$ |
| Jeffreys, $p(\sigma)\propto 1/\sigma$ | $[0.6742,\,1.7694]$ |
| flat in $u = \ln\sigma$ | $[0.6742,\,1.7694]$ |

The last two rows are identical to four decimals. That is the mathematical
statement that the Jeffreys prior *is* the flat prior on $\log\sigma$: it assigns
the same probability to $\sigma$ and to $1/\sigma$ intervals of equal relative
width. The flat prior on $\sigma$ gives an interval $12.2\%$ wider, because it
prefers large scales — a preference inherited from the arbitrary choice to
parameterise by $\sigma$ rather than by $1/\sigma$.

Reference priors are not a solution to the prior problem, and saying so plainly
matters:

- For a location parameter the Jeffreys prior is flat and improper, so the
  posterior can be improper if the likelihood is also flat. Improper priors
  cannot be sampled from or normalised without a truncation, and any claim about
  their posterior probability content requires stating that truncation.
- In multi-parameter problems the Jeffreys prior depends on which parameters are
  treated as nuisance, and different reference constructions give different
  answers.
- Even a reference prior is a prior: the analysis is still conditional on it.

## 6. Bounds and constraints

Physical parameters have bounds — a velocity is positive, a porosity lies in
$[0,1]$, a thickness cannot exceed the depth of the basin. A bound is a prior with
compact support, and its most important consequence is invisible in the summary
statistics. The demonstration inverts two SYNTHETIC data points with
$\sigma = 0.15$ under a uniform prior on $[0,0.5]$:

| data | posterior mean | posterior std | mass within $0.02$ of the bound |
|---|---|---|---|
| $(0.20,\,0.22)$, inside the bound | 0.2151 | 0.0982 | $0.2\%$ |
| $(0.90,\,0.94)$, above the bound | 0.4759 | 0.0231 | $55.4\%$ |

In the second case the posterior mean sits within $5\%$ of the bound and the
standard deviation collapses from $0.0982$ to $0.0231$ — a four-fold narrowing
produced entirely by the constraint. Reported without the edge mass, that small
standard deviation looks like a precise measurement. It is not: it is a statement
that the data want a value outside the admitted set. **Whenever a posterior
touches a bound, report the mass at the bound.**

## 7. Regime of validity

1. **A prior is a model.** It can be wrong, and a large prior-data conflict is
   evidence about the prior, not about the data.
2. **A prior carries information that must be reported.** Report the prior share
   of precision (Section 2), or equivalently the posterior under two priors.
3. **Wide does not mean neutral.** A very wide Gaussian prior is not the same as
   a flat prior, and neither is invariant: the flat prior on $\sigma$ and the flat
   prior on $\log\sigma$ give different intervals, as measured above.
4. **Improper priors need a stated truncation.** Otherwise the posterior has no
   normalising constant and no credible interval.
5. **Bounds produce boundary mass.** Report it or the summary is misleading.
6. **A prior cannot be chosen after seeing the posterior.** Using a posterior to
   set a prior and then reporting that posterior is circular.
7. **The prior is not a substitute for data.** A prior share above roughly half
   the posterior precision in a study that claims to measure something should be
   justified in its own right.

## 8. Demonstration and exercises

[`code/priors_demo.py`](./code/priors_demo.py) prints the shrinkage table, the
precision shares, the conflict table, the invariance check and the boundary
behaviour, and exits $0$ in a fraction of a second. Problems and worked solutions:
[`exercises/03-priors-exercises.md`](./exercises/03-priors-exercises.md),
[`exercises/03-priors-solutions.md`](./exercises/03-priors-solutions.md).

## Mastery checkpoint

**(a)** A single datum $d = 2.0$ has $\sigma = 0.5$; the prior is
$\mathcal{N}(0, s_0^2)$. Compute $m_{\text{post}}$ and $s_{\text{post}}$ for
$s_0 = 0.25$ and $s_0 = 4$.
**(b)** With $N = 25$ data of $\sigma = 2$, compute the prior standard deviation at
which the prior carries exactly $50\%$ of the posterior precision.
**(c)** Derive the Jeffreys prior for a Poisson rate $\lambda$ from
$p(k\mid\lambda) = \lambda^k e^{-\lambda}/k!$, and state the resulting posterior
for $k_{\text{obs}} = 3$.
**(d)** A posterior for a bounded parameter piles up at the bound with $40\%$ of
its mass. Write the two-sentence report a referee would accept.

## Common pitfalls

1. **Saying "no prior".** Every inversion has one; a flat prior on one
   parameterisation is not flat on another.
2. **Reporting only one prior.** The sensitivity of the answer to the prior is
   part of the answer.
3. **Using a prior to force a physically desired sign.** A prior that excludes a
   sign does not test that sign; it assumes it.
4. **Ignoring the boundary mass.** The most common way a constrained inversion
   produces an over-confident number.
5. **Choosing $s_0$ to make the answer look reasonable.** That is fitting the
   prior to the answer.
6. **Confusing the Jeffreys prior of a scale with the flat prior of that scale.**
   They differ by the Jacobian, as the measured intervals show.

## Further reading

- **Jeffreys, H. (1961). *Theory of Probability* (3rd ed.). Oxford University
  Press.** Level: research. The original invariance argument.
- **Jaynes, E. T. (2003). *Probability Theory: The Logic of Science*. Cambridge
  University Press.** Level: research. Group invariance and the construction of
  priors from symmetries rather than from convenience.
- **Gelman, A., Carlin, J. B., Stern, H. S., Dunson, D. B., Vehtari, A., &
  Rubin, D. B. (2013). *Bayesian Data Analysis* (3rd ed.). CRC Press.**
  Level: research. Weakly informative priors in practice, and prior predictive
  checks.
- **Sivia, D. S., & Skilling, J. (2006). *Data Analysis: A Bayesian Tutorial*
  (2nd ed.). Oxford University Press.** Level: advanced. The scale-parameter
  derivation in a compact form.

## Related modules

- [01 Bayes' Theorem as an Inverse-Problem Formulation](01-bayes-inverse-formulation.md).
- [02 Constructing Likelihoods and Error Models](02-likelihood-models.md) — the
  prior on the noise scale used here.
- [04 Markov Chain Monte Carlo](04-mcmc.md) — sampling a posterior with a
  bounded or truncated prior.
- [07 Bayesian Evidence and Model Selection](07-evidence-and-model-selection.md) —
  how the prior width changes a Bayes factor.
- [18-03-01 Why Regularisation Is Physically and Statistically Justified](../03-regularization/01-why-regularize.md).
- [18-03-06 Physical Constraints, Bounds and Feasible Model Sets](../03-regularization/06-constraints.md).
- [21-03-02 Conjugate Priors](../../21-statistics-bayesian-ml/03-bayesian-inference/02-conjugate-priors.md).
