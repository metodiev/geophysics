# Exercises — 18-09-03 Generative Priors: GANs, VAEs, Diffusion Models

Attempt these before reading the
[solutions](./03-generative-models-inversion-solutions.md). The lesson is
[03 Generative Priors: GANs, VAEs, Diffusion Models](../03-generative-models-inversion.md).
All models are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** Write the posterior for a Gaussian generative prior
$\mathcal{N}(\boldsymbol{\mu},\Sigma_\phi)$ and identify which symbols come from
the ensemble and which from the physics.

**★2.** Four PCA components explain 41.2%, 26.7%, 12.9% and 5.8% of the variance.
Compute the total explained variance and the residual, and state what the
residual represents.

**★3.** State the number of exact null directions of a $20\times30$ operator and
what the posterior variance in those directions describes.

## ★★ Applied

**★★4.** The learned prior gives a mean null-space posterior $\sigma$ of 0.1480
against 0.5295 for smoothness. Write two sentences, one for a reader who believes
the ensemble, one for a reader who does not, describing what that difference
means.

**★★5.** For the spike target, the learned prior has a *lower* MSE than the
smoothness prior (0.0750 vs 0.1257), yet the truth's energy in the learned
subspace is only 0.112 while the recovered model's is 0.951. Explain how both can
hold and why the second number is the more important one.

**★★6.** A study has 2000 training models that are all layered. A reviewer asks
whether the prior is valid for a target that might be faulted. State the answer
you would give and the experiment that would settle it.

## ★★★ Research-oriented

**★★★7.** Design an inversion that uses a generative prior whose ensemble is
deliberately *broad* (covering several structural families) and a second that
uses a narrow ensemble. Specify a metric that would show which is better for a
stated target, and state what the narrow prior gains and loses. A specification
that could not be executed is a failed answer.

**★★★8.** A GAN prior provides samples but no density. Describe two inversion
formulations that work without a likelihood term, and state the guarantee each
loses relative to a likelihood-based posterior.
