---
id: 16-05-05
title: "CMIP, Model Intercomparison and Ensemble Design"
level: research
prereqs: ["16-05-01", "16-05-03", "16-04-03"]
tags: [atmosphere, climate, climate-models, ensembles, intercomparison, uncertainty]
---

# CMIP, Model Intercomparison and Ensemble Design

> All models and data in this module are **SYNTHETIC**. Every number below was
> printed by
> [`code/coupled_model_intercomparison_demo.py`](code/coupled_model_intercomparison_demo.py).
> The "models" are chosen response coefficients standing in for climate models;
> no real model and no ensemble size from any real intercomparison is used or
> quoted.

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** internal variability, the forced response and structural
   uncertainty, and **assign** each to the ensemble design that estimates it.
2. **Derive** why the error of an ensemble mean falls as $1/\sqrt{N}$, and
   **measure** that scaling.
3. **Derive** the variance decomposition
   $\mathrm{Var}(\text{total}) = \sigma_{\text{struct}}^{2}
   + \sigma_{\text{internal}}^{2}/N$ and **use** it to explain why more members
   cannot reduce structural spread.
4. **Quantify** the overconfidence of a single-model large ensemble.
5. **Compare** equal-member, equal-model and inverse-variance weighting, and
   **state** the estimator each one corresponds to.
6. **Explain** why the models in an archive are not exchangeable samples of a
   distribution, and **state** what that does to any statement of spread.
7. **Design** an ensemble adequate for a stated question, stating how many
   members, how many models and what the design assumes.

## Prerequisites

- [16-05-01 Model Hierarchy: EBMs, EMICs, GCMs, ESMs](01-climate-model-hierarchy.md) —
  why models differ at all.
- [16-05-03 Model Evaluation, Skill and Benchmarking](03-model-evaluation.md) —
  the metrics used to compare a model with a reference.
- [16-04-03 Climate Sensitivity: Definitions and Estimation](../04-climate-system-and-feedbacks/03-climate-sensitivity.md) —
  the response coefficient used here as the source of structural spread.

## 1. Intuition: three different reasons a forecast is uncertain

Given a forcing change, one model run will differ from another run of the *same*
model with a slightly different initial condition. Different models will differ
from each other for a second and larger reason. And our knowledge of the
forcing, and of the physics, contributes a third. These are not interchangeable,
and they cannot be measured with the same instrument.

This is the reason coordinated model intercomparison projects exist. The
**Coupled Model Intercomparison Project (CMIP)** is a coordinated framework: the
participating centres run a common set of experiments with their own models and
archive the output in a common format, so that differences between the results
are analysable rather than idiosyncratic. The value of the framework is
comparability, not consensus. An archive of models is a set of *opinions about
physics*, not a random sample of possible Earths.

The practical consequence, and the point of this lesson, is that **an ensemble
mean is only as good as the ensemble design**. Averaging many members of one
model estimates the forced response with small internal error and says nothing
about structural error.

## 2. Definitions

- **Internal variability.** The variability a model produces without any change
  in external forcing: weather, ENSO-like modes, ocean eddies. It is sampled by
  running the same model with perturbed initial conditions.
- **Forced response.** The expected change attributable to the forcing, usually
  estimated as the ensemble mean.
- **Structural uncertainty.** The spread between models that arises because they
  parameterise unresolved processes differently (see
  [02 GCMs, Resolution and Parameterisation](02-gcms-and-parameterisation.md)).
- **Initial-condition (single-model) ensemble.** Many runs of one model with
  perturbed initial conditions. Estimates internal variability only.
- **Multi-model ensemble.** Many models, typically one or a few members each.
  Samples structural spread.
- **Ensemble of opportunity.** A set of models that happens to be available,
  with unequal numbers of members and non-independent formulations.
- **Exchangeability.** The assumption that the ensemble members are
  interchangeable draws from a distribution. It is *not* satisfied by real model
  archives, and the arithmetic below should be read with that in mind.

## 3. Derivation: two levels of uncertainty

### 3.1 Internal variability only

Suppose the truth is a constant $\mu$ and each member is
$m_j = \mu + \varepsilon_j$ with $\varepsilon_j$ independent, mean zero and
variance $\sigma_i^{2}$. The ensemble mean is

$$\bar m = \frac1N\sum_{j=1}^{N}(\mu+\varepsilon_j) = \mu + \bar\varepsilon,
\qquad
\mathrm{Var}(\bar m) = \frac{\sigma_i^{2}}{N}.$$

So the error of the ensemble mean is $\sigma_i/\sqrt{N}$: the only part of the
uncertainty that more members can reduce.

### 3.2 Structural plus internal

Let model $k$ have its own mean $M_k$ with variance $\sigma_{\text{struct}}^{2}$
across models, and let members within a model fluctuate with
$\sigma_i^{2}$. An unbiased estimate of the total variance of a single member is
$\sigma_{\text{struct}}^{2} + \sigma_i^{2}$. Averaging $N$ members *within* each
model removes internal variability from the model means but leaves the model
means themselves. So

$$\boxed{\;\sigma_{\text{total}}^{2}(N)
= \sigma_{\text{struct}}^{2} + \frac{\sigma_i^{2}}{N}\;}$$

which tends to $\sigma_{\text{struct}}^{2}$ as $N\to\infty$. **A large ensemble
cannot beat the second term below the first.**

### 3.3 This term, not that one

The decomposition also defines what the ensemble *mean* estimates: the average
of the model means, $\bar M = K^{-1}\sum_k M_k$. If the models are a biased
sample of the plausible physics, $\bar M$ is biased, and no number of members
fixes it.

## 4. Measurement: the $1/\sqrt{N}$ law

The demonstration draws $4000$ synthetic ensembles at each size with
$\sigma_i = 0.30\ \mathrm{K}$ and measures the standard deviation of the ensemble
mean:

| $N$ | measured sd of ensemble mean (K) | $\sigma_i/\sqrt N$ (K) | ratio |
|---|---|---|---|
| 1 | 0.2987 | 0.3000 | 0.996 |
| 5 | 0.1336 | 0.1342 | 0.996 |
| 10 | 0.0955 | 0.0949 | 1.006 |
| 25 | 0.0609 | 0.0600 | 1.014 |
| 50 | 0.0423 | 0.0424 | 0.997 |
| 100 | 0.0302 | 0.0300 | 1.007 |

The ratios scatter within $\pm1.5\%$ of unity, which is sampling variability, not
bias. The law holds. Note what it implies: to halve the internal error you need
**four times** the members.

## 5. Measurement: structural spread does not shrink

Give three synthetic models sensitivities $\lambda = 0.5, 0.8, 1.1\
\mathrm{K\,(W\,m^{-2})^{-1}}$ and apply a forcing
$F = 4.0\ \mathrm{W\,m^{-2}}$. The equilibrium responses are $2.0$, $3.2$ and
$4.4\ \mathrm{K}$, with a structural standard deviation of $1.2000\
\mathrm{K}$. Adding internal variability of $0.30\ \mathrm{K}$ per member gives:

| members per model | internal part (K) | total spread (K) |
|---|---|---|
| 1 | 0.3000 | 1.2369 |
| 10 | 0.0949 | 1.2037 |
| 100 | 0.0300 | 1.2004 |
| 1000 | 0.0095 | 1.2000 |

By $N = 100$ the internal contribution is $2.5\%$ of the structural one, and by
$N = 1000$ it is negligible. Beyond that point, additional members buy nothing:
the uncertainty is not about the weather, it is about the physics.

### 5.1 The overconfidence of a single-model large ensemble

Suppose a modelling group runs one model with $N = 100$ members and reports the
standard error of its ensemble mean, $0.0300\ \mathrm{K}$. The structural spread
across the three models is $1.2000\ \mathrm{K}$ — a factor of **$40.0$** larger.
The reported uncertainty is an honest statement about internal variability and a
gross understatement of the uncertainty of the forced response. This is not
dishonesty; it is a correct calculation of the wrong quantity.

## 6. Weighting: three estimators with one name

| estimator | definition | value in the demonstration (K) |
|---|---|---|
| member-weighted | every member equal (models with more members count more) | 3.2023 |
| model-weighted | every model equal (member counts ignored) | 3.2384 |
| inverse-variance weighted | weights $\propto 1/\sigma_k^{2}$ | 2.8155 |

The demonstration gives the three models internal noise amplitudes in the ratio
$1:1.5:2$, so they are not equally informative, and the three estimators differ
by $0.4229\ \mathrm{K}$ — comparable to the internal variability itself.

Two conclusions:

- **"All members equal" and "all models equal" are different estimators.** The
  first lets a model with a large ensemble dominate; the second gives a
  one-member model the same weight as a hundred-member model. Neither is
  privileged; the choice must be stated, because it moves the answer.
- **Inverse-variance weighting requires knowledge that is usually absent.** It
  needs each model's internal variance, and it assumes the models are
  exchangeable draws with a common mean. In an ensemble of opportunity both
  assumptions are questionable, which is why simple equal-model weighting is
  common in practice despite its inefficiency.

## 7. Worked example: how many members is enough?

*Problem.* A study needs the forced response of the synthetic three-model
ensemble to a $4.0\ \mathrm{W\,m^{-2}}$ forcing, with a total standard
uncertainty no larger than $1.25\ \mathrm{K}$. The structural standard deviation
across models is $1.2000\ \mathrm{K}$ and the internal standard deviation per
member is $0.30\ \mathrm{K}$. How many members per model are needed?

*Solution.* We require

$$\sqrt{1.2000^{2} + \frac{0.30^{2}}{N}} \le 1.25
\quad\Longrightarrow\quad
1.44 + \frac{0.09}{N} \le 1.5625
\quad\Longrightarrow\quad
\frac{0.09}{N} \le 0.1225
\quad\Longrightarrow\quad N \ge 0.735.$$

So $N = 1$ already satisfies the target: with a structural spread of $1.2000\
\mathrm{K}$, single-member models give $1.2369\ \mathrm{K}$, below $1.25\
\mathrm{K}$.

*Interpretation.* The answer is a statement about arithmetic and nothing else,
which is exactly why it is worth doing before requesting computer time. Here the
target is unreachable in a meaningful sense: the stated tolerance of
$1.25\ \mathrm{K}$ is barely above the structural floor of $1.2000\
\mathrm{K}$, so the study is asking the weather to be quiet while leaving the
physics untouched. If the scientific question concerns the forced response, the
useful next step is not more members but more *models* — and a statement of what
the model archive is a sample of.

## 8. Assumptions and regime of validity

1. **Independence of members.** The $1/\sqrt N$ law assumes independent
   perturbations. Members of a coupled ensemble are not fully independent; they
   share the same model, and often the same forced boundary conditions, so the
   effective $N$ is smaller than the member count.
2. **Exchangeability of models.** Real model archives are *not* random samples
   of a distribution. Models share code, parameterisations and institutional
   assumptions; their spread is neither unbiased nor Gaussian, and a
   "model-mean" is a mean of opinions.
3. **A single mean.** The arithmetic above concerns an estimate of a mean
   response. Extremes, trends and spatial patterns have different sampling
   behaviour and cannot be inferred from the mean's standard error.
4. **Forcing uncertainty is excluded.** The analysis assumes the forcing is known
   exactly. Add its uncertainty separately; it will not average out.
5. **Linearity.** The variance decomposition treats the response as a sum of
   independent contributions. For nonlinear responses, spread and mean do not
   separate so cleanly.
6. **One number is not the uncertainty.** Reporting a standard error commits to
   an interpretation (internal only, structural only, or both). Say which.

## 9. Units and dimensional analysis

| quantity | symbol | unit | check |
|---|---|---|---|
| response | $\Delta T$ | K | $\lambda F$ |
| sensitivity | $\lambda$ | $\mathrm{K\,(W\,m^{-2})^{-1}}$ | inverse of a feedback parameter |
| internal sd | $\sigma_i$ | K | |
| standard error | $\sigma_i/\sqrt N$ | K | dimensionless $\sqrt N$ |
| structural sd | $\sigma_{\text{struct}}$ | K | |

Variances add, standard deviations do not: $\sigma_{\text{total}} =
\sqrt{\sigma_{\text{struct}}^{2} + \sigma_i^{2}/N}$. Adding $1.2000$ and $0.0300$
directly would give $1.2300\ \mathrm{K}$ instead of the correct
$1.2004\ \mathrm{K}$ — a $2.5\%$ error that grows as the terms become
comparable.

## 10. Python demonstration

[`code/coupled_model_intercomparison_demo.py`](code/coupled_model_intercomparison_demo.py):

1. measures the standard deviation of an ensemble mean over $4000$ realisations
   for six ensemble sizes and compares it with $\sigma_i/\sqrt N$;
2. builds a three-model ensemble with chosen sensitivities, computes the
   structural standard deviation and tabulates the total spread against member
   count;
3. quantifies the overconfidence factor of a single-model large ensemble;
4. compares member-weighted, model-weighted and inverse-variance-weighted means
   for models with unequal internal noise.

It is print-only, seeded with `np.random.default_rng(20261014)`, and exits 0.
The file deliberately does not name any real model or quote any real ensemble
size, because none is used.

## 11. Exercises

See [`exercises/05-coupled-model-intercomparison-exercises.md`](exercises/05-coupled-model-intercomparison-exercises.md)
and [`exercises/05-coupled-model-intercomparison-solutions.md`](exercises/05-coupled-model-intercomparison-solutions.md).

## Mastery checkpoint

> **(a)** With $\sigma_i = 0.4\ \mathrm{K}$, how many members are needed for the
> standard error of the ensemble mean to fall below $0.05\ \mathrm{K}$?
> **(b)** A three-model ensemble has responses $1.5$, $2.5$ and $5.0\
> \mathrm{K}$ to the same forcing. Compute the structural standard deviation
> (use the sample formula, $N-1$ in the denominator) and the total spread with
> $N = 25$ members per model and $\sigma_i = 0.5\ \mathrm{K}$.
> **(c)** State, in one sentence each, what a 100-member single-model ensemble
> can and cannot tell you about the response to a forcing.
> **(d)** The archive you are using has 8 models, three of which share a common
> atmospheric core. State one way this affects the interpretation of the
> multi-model spread, and one way to quantify the effect.

## Common pitfalls

1. **Reading a multi-model mean as a best estimate.** It is an average of
   opinions; it is not a sample mean with a defensible standard error.
2. **Using internal variability as total uncertainty.** It is the small term.
3. **Assuming more members always helps.** Past the structural floor, additional
   members change nothing.
4. **Ignoring unequal member counts.** Member-weighted and model-weighted means
   differ, and the difference is not noise.
5. **Treating the archive as exchangeable.** Shared code and shared training
   assumptions mean the spread understates the true diversity of plausible
   physics.
6. **Quoting a standard error without saying which uncertainty it measures.**

## Related modules

- [16-05 Climate Models](README.md).
- [16-04-03 Climate Sensitivity: Definitions and Estimation](../04-climate-system-and-feedbacks/03-climate-sensitivity.md) —
  the parameter whose spread dominates Section 5.
- [16-05-06 Emulators and Surrogate Models](06-emulation-and-surrogates.md) —
  how large ensembles become affordable.
- [18-06 Uncertainty Quantification](../../18-inverse-problems/06-uncertainty-quantification/README.md) —
  the taxonomy of uncertainty used informally here.
- [21-03 Bayesian Inference](../../21-statistics-bayesian-ml/03-bayesian-inference/README.md) —
  how a population of models would be treated if exchangeability did hold.
