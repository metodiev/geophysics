---
id: 18-09-03
title: "Generative Priors: GANs, VAEs, Diffusion Models"
level: research
prereqs: ["18-09-01", "18-05-03"]
tags: [inverse-problems, machine-learning, generative-models, priors, ensemble]
---

# Generative Priors: GANs, VAEs, Diffusion Models

> All models and data in this module are **SYNTHETIC**. The training ensemble,
> its distribution and the PCA/"generative" model below are chosen teaching
> ingredients. No number is a measurement of geological reality.

## Learning objectives

By the end of this lesson you will be able to:

1. **Describe** a generative prior as a distribution over models learned from an
   ensemble, and **state** how it is used in a Bayesian inversion.
2. **Construct** a tractable generative prior (PCA / factor analysis) from a
   synthetic ensemble and **measure** the variance it explains.
3. **Derive** the posterior precision for a Gaussian prior with a learned mean
   and covariance, and **compare** its in-family error with a smoothness prior.
4. **Quantify** what the prior does in the data's null space, and **state** why
   that is a claim and not a measurement.
5. **Measure** the out-of-family behaviour, including the fraction of recovered
   energy forced into the learned subspace, and **state** why that is the
   systematic effect rather than the aggregate error.
6. **Explain** why richer generative families (GANs, VAEs, diffusion models)
   change the prior's *expressiveness* rather than the nature of the bet.

## Prerequisites

- [18-09-01 Learned Inversion: Direct and Iterative Networks](01-learned-inversion.md) —
  the distributional argument this lesson makes explicit.
- [18-05-03 Priors: Informative, Reference and Their Influence](../05-bayesian-inversion/03-priors.md) —
  what a prior is allowed to do.

## 1. A generative prior is a distribution, applied as a prior

A generative model $g_\phi$ maps a low-dimensional latent variable
$\mathbf{z}\sim p(\mathbf{z})$ to a model $\mathbf{m} = g_\phi(\mathbf{z})$, and
thereby defines a distribution $p_\phi(\mathbf{m})$ over the model space. Used as
a prior in an inversion, the objective becomes

$$\Phi(\mathbf{m}) = \|\mathbf{d} - G\mathbf{m}\|^2_{C_d^{-1}}
- 2\log p_\phi(\mathbf{m}),$$

or, equivalently, the posterior is

$$p(\mathbf{m}\mid\mathbf{d}) \propto
\exp\!\left[-\tfrac12\|\mathbf{d}-G\mathbf{m}\|^2_{C_d^{-1}}\right]
p_\phi(\mathbf{m}).$$

If $p_\phi$ is Gaussian, $\log p_\phi$ is quadratic and the posterior is Gaussian;
if it is a deep generative model, sampling replaces the closed form. The
**information content** is the same in both cases: whatever the ensemble said
about plausible models.

Richer families (a VAE's decoder, a GAN's generator, a diffusion model's score)
differ in how much of model space they can represent and how faithfully they
match the ensemble. They do not change the fact that the prior is a bet on the
ensemble.

## 2. Worked example: a tractable generative prior

`code/generative_priors_demo.py` builds 1500 synthetic "layered" models on a
30-cell grid (random walks with two to three long steps) and fits a linear
generative prior by PCA:

$$p_\phi(\mathbf{m}) = \mathcal{N}\!\left(\boldsymbol{\mu},
V_k\Lambda_k V_k^{T} + \sigma_\perp^2\left(I - V_kV_k^{T}\right)\right).$$

Four components explain $86.53\%$ of the ensemble variance (component fractions
41.2%, 26.7%, 12.9%, 5.8%), with a residual $13.47\%$ outside them. The fitted
scales are $\sigma_\parallel = 1.0273$ along the subspace and
$\sigma_\perp = 0.1480$ orthogonal to it.

Comparing with a smoothness prior on the same 20-observation, $\sigma=0.05$
problem, for 400 in-family test models:

| prior | MSE | rms |
|---|---|---|
| smoothness ($\lambda = 1$) | $8.678\times10^{-2}$ | 0.2946 |
| learned (PCA) generative | $3.130\times10^{-2}$ | 0.1769 |

In-family the learned prior wins by a factor of 1.7 in rms, because the ensemble
it was trained on **is** the population the test models come from.

## 3. What the prior does in the null space

The operator has $30 - 20 = 10$ exact null directions: no observation depends on
them. Their posterior standard deviation is what a modeller is implicitly
claiming to know about parts of the model the data never touch:

| prior | mean null-space posterior $\sigma$ |
|---|---|
| smoothness | 0.5295 |
| learned | 0.1480 |

The learned prior is more confident there, because its ensemble says plausible
models have bounded structure in those directions. **If the ensemble is right,
that confidence is earned; if the target is outside the ensemble, it is
fabricated, and the misfit cannot tell** — no observation depends on those
directions at all. This is the cleanest statement of the prior's power and the
prior's danger in the whole module.

## 4. Out-of-family behaviour

Two families outside the training ensemble: a high-frequency oscillation, and an
isolated spike.

| target | smoothness MSE | learned MSE | ratio | truth energy in subspace → recovered |
|---|---|---|---|---|
| high-frequency oscillation | $4.706\times10^{-1}$ | $5.089\times10^{-1}$ | 1.08 | 0.017 → 0.968 |
| isolated spike | $1.257\times10^{-1}$ | $7.502\times10^{-2}$ | 0.60 | 0.112 → 0.951 |

The aggregate error is not the point: on the oscillation the learned prior is 8%
worse, on the spike it happens to be better. What is **systematic** is where the
recovered energy sits. The last column pairs the fraction of the truth's energy
inside the learned subspace with the fraction of the recovered model's energy
there: whatever the truth is, the prior forces about 95% of the answer into a
four-dimensional subspace that a sparse or oscillatory truth barely occupies.

Reporting the aggregate error alone would hide this completely. Report the
subspace projection.

## 5. What the richer families change

| family | expresses | inversion cost | added failure mode |
|---|---|---|---|
| PCA / factor analysis | linear correlations | closed form | none beyond the ensemble bet |
| VAE | smooth nonlinear manifolds | sampling or optimisation | posterior collapse; blurred modes |
| GAN | sharp modes | optimisation over $\mathbf{z}$ | mode dropping; no likelihood |
| diffusion | complex $p_\phi$ | many network evaluations | slow; score errors appear as artefacts |

For inversion purposes, the practical differences are (i) how well the family
covers the true model distribution, and (ii) whether a likelihood is available.
A GAN gives sharp, plausible-looking outputs and no likelihood; a diffusion model
gives a score and high cost; a VAE gives a likelihood-like bound and typically
blurred structure. None of these properties is about the Earth.

## 6. Numeric demonstration

```bash
cd 18-inverse-problems/09-machine-learning-inversion/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python generative_priors_demo.py
```

Four sections: the ensemble and its subspace; in-family inversion; the null-space
comparison; out-of-family targets and the subspace projection. Print-only, seeded,
exits 0 in under a second.

## 7. Assumptions and regime of validity

1. **The ensemble is the prior, and it is finite.** A 1500-model ensemble cannot
   represent structure absent from it; the 13.47% residual variance is
   *unrepresented by construction*.
2. **The linear prior here is a stand-in.** PCA generalises the *idea* of a
   learned generative prior; the measured effects (prior exploitation, null-space
   confidence, subspace forcing) are structural and recur for deep families.
3. **The data likelihood is assumed correct.** A wrong forward operator is a
   separate error, independent of the prior.
4. **Regularisation is not optional.** A generative prior fills the null space; if
   the truth has structure there, the fill is wrong and invisible in the misfit.
5. **Subspace projection must be measured, not assumed.** On real data, report the
   fraction of recovered energy in the learned subspace and the residual.

## Mastery checkpoint

Without notes: **(a)** Write the posterior for a Gaussian generative prior and
identify which term encodes the ensemble. **(b)** Given the component fractions
41.2/26.7/12.9/5.8%, state what a four-component prior retains and what it
discards. **(c)** Explain the null-space table to someone who asks "why is the
learned prior's uncertainty smaller — is it more accurate?". **(d)** Using the
out-of-family table, state the systematic effect in one sentence and the quantity
that measures it.

## Common pitfalls

1. **Reporting the ensemble-derived model as "geologically realistic".**
   Realism is a statement about the ensemble.
2. **Comparing priors only in-family.** Section 4.
3. **Quoting the aggregate error without the subspace projection.** The
   systematic effect is invisible in the aggregate.
4. **Assuming a likelihood where none exists.** A GAN gives samples, not a
   density; the log-prior term must be replaced by an optimisation.
5. **Forgetting that the null-space confidence is a claim.** Section 3.

## Related modules

- [Learned Inversion: Direct and Iterative Networks](01-learned-inversion.md).
- [Uncertainty in Learned Inversion: Pitfalls and Calibration](04-uncertainty-in-learned-inversion.md).
- [18-05-03 Priors: Informative, Reference and Their Influence](../05-bayesian-inversion/03-priors.md).
- [18-05-08 Trans-Dimensional and Reversible-Jump MCMC](../05-bayesian-inversion/08-trans-dimensional.md) —
  the alternative to a fixed generative prior when structure is unknown.

Code: [`code/generative_priors_demo.py`](code/generative_priors_demo.py).
Exercises: [`exercises/03-generative-models-inversion-exercises.md`](exercises/03-generative-models-inversion-exercises.md).
