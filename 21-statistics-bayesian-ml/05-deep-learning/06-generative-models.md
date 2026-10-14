---
id: 21-05-06
title: "GANs, VAEs and Diffusion Models"
level: research
prereqs: ["21-05-05", "21-03-05"]
estimated_minutes: 65
tags: [deep-learning, generative-models, vae, gan, diffusion, elbo]
---

# GANs, VAEs and Diffusion Models

## Learning objectives

By the end of this lesson you will be able to:

1. **Write** the variational autoencoder's evidence lower bound and **state** the
   two terms it balances.
2. **Show** that the bound becomes exact when the family contains the true
   posterior, and **compute** the improvement it measures.
3. **Write** the adversarial objective and **interpret** it as a two-sample test.
4. **Measure** a generator's quality with a two-sample statistic and **state** what
   the statistic does and does not establish.
5. **Write** the forward diffusion process and **compute** the
   signal-to-noise ratio schedule.
6. **Choose** between the three families for a stated geophysical purpose, and
   **state** how each is evaluated.

Data in this lesson are **SYNTHETIC**, generated in the demonstration. No measured
value is used.

## Prerequisites

- [21-05-05 Autoencoders for Compression and Denoising](05-autoencoders.md) —
  the reconstruction objective the VAE extends.
- [21-03-05 Variational Inference and Scalable Bayes](../03-bayesian-inference/05-variational-inference.md) —
  the ELBO and its KL gap.
- [21-04-03 Cross-Validation, Metrics and the Danger of Leakage](../04-machine-learning-fundamentals/03-model-assessment.md) —
  the evaluation discipline that generative models strain.

## 1. Intuition: three answers to "where does the data come from?"

A generative model learns the distribution of the data, so that new samples can be
drawn from it. The three families differ in how they make the problem tractable:

- A **variational autoencoder** posits a latent variable $z$ and maximises a
  lower bound on the data likelihood, trading reconstruction against agreement
  between the posterior and the prior.
- A **generative adversarial network** learns a generator by pitting it against a
  discriminator that tries to tell generated samples from real ones; there is no
  likelihood at all.
- A **diffusion model** destroys the data with a fixed noising process and learns
  the reverse step, turning generation into many small denoising problems.

For geophysics the choice is usually made by *what can be evaluated*: a VAE has a
likelihood bound, a GAN has only a two-sample statistic, and a diffusion model has
a well-defined training loss whose sample quality still needs a physical check.

## 2. The variational autoencoder

With a prior $p(z)$, an encoder $q_\phi(z\mid x)$ and a decoder
$p_\theta(x\mid z)$, the objective is

$$\mathcal L = \mathbb E_{q_\phi}\big[\ln p_\theta(x\mid z)\big]
- \mathrm{KL}\big(q_\phi(z\mid x)\,\|\,p(z)\big)
\;\le\; \ln p_\theta(x).$$

The first term rewards reconstruction, the second forces the posterior towards the
prior so that sampling from the prior produces plausible data. The gap to the true
log-likelihood is the KL divergence between the approximate and true posteriors.

The demonstration computes the bound exactly for a one-dimensional
Gaussian problem: $n = 4000$ observations from $\mathcal N(2.0, 1.5^{2})$ with a
unit-variance prior. The exact posterior is
$\mathcal N(1.9872458, 0.0005622)$, and

| parameter setting | ELBO |
|---|---|
| prior, $m = 0$, $s^{2}=1$ | $-11\,682.9057$ |
| sample mean with the posterior variance | $-7\,285.4335$ |
| exact posterior | $-7\,285.4324$ |

The improvement from the prior to the optimum is $4397.4733$ nats, and the
remaining gap of $0.0011$ nats is numerical. Because the Gaussian family contains
the true posterior, the maximum ELBO **equals** the log evidence: the bound is
tight, and the demonstration's two optima agree to four significant figures. That
is the check that a variational implementation is correct.

## 3. Generative adversarial networks

The objective is a minimax game:

$$\min_G \max_D\; \mathbb E_{x\sim p_{\text{data}}}\big[\ln D(x)\big]
+ \mathbb E_{z}\big[\ln\big(1 - D(G(z))\big)\big].$$

For a fixed generator the optimal discriminator is
$D^{*}(x) = p_{\text{data}}(x)/(p_{\text{data}}(x) + p_G(x))$, so the
discriminator is a two-sample test and the generator's job is to make that test
uninformative. The demonstration measures the discriminator by its **AUC**:

| generator | discriminator AUC |
|---|---|
| shifted and mis-scaled | $0.9692$ |
| matched to the data | $0.4857$ |

An AUC of $0.9692$ means the discriminator separates the two samples almost
perfectly — the generator is poor. An AUC of $0.4857$ is indistinguishable from
chance, which is the training objective attained. Two cautions follow: an AUC near
$0.5$ is necessary but not sufficient, since a generator can match the first two
moments while differing in the tail; and a single statistic cannot certify
distributional agreement, so the evaluation needs several.

## 4. Diffusion

Forward diffusion adds Gaussian noise on a fixed schedule:

$$q(x_t\mid x_{t-1}) = \mathcal N\big(\sqrt{1-\beta_t}\,x_{t-1},\
\beta_t I\big), \qquad
\bar\alpha_t = \prod_{s\le t}(1-\beta_s),$$

so that $x_t = \sqrt{\bar\alpha_t}\,x_0 + \sqrt{1-\bar\alpha_t}\,\varepsilon$ and
the signal-to-noise ratio is $\bar\alpha_t/(1-\bar\alpha_t)$. The model learns
only the reverse step, and the schedule decides how hard each step is.

The demonstration's linear schedule from $\beta_1 = 10^{-4}$ to
$\beta_{1000} = 0.02$ gives:

| step | $\bar\alpha_t$ | SNR |
|---|---|---|
| 1 | $0.999900$ | $9999.0000$ |
| 10 | $0.998105$ | $526.7615$ |
| 100 | $0.897018$ | $8.7104$ |
| 500 | $0.078587$ | $0.0853$ |
| 900 | $0.000275$ | $0.0003$ |
| 1000 | $0.000040$ | $\approx 0$ |

The signal and the noise are equal at step **$259$ of $1000$** — the point at
which the data are half destroyed. Forward diffusion requires no training: it
destroys information at a known rate, and the model's task is the reverse step,
whose difficulty is set by the local SNR.

## Assumptions and regime of validity

1. **The prior must be sampled at generation time.** A VAE's samples are limited
   by the prior's support; a poor choice produces plausible-looking but impossible
   fields.
2. **Likelihood and sample quality are different.** A high ELBO bounds the
   likelihood from below; it does not guarantee good samples, and a GAN has no
   likelihood at all.
3. **Evaluation needs physics.** A statistic can be matched while a physical
   property — connectivity, spectral slope, facies proportion — is not.
4. **Training stability.** GAN training oscillates; diffusion is slow at sampling
   (hundreds to thousands of network evaluations); VAEs under-fit sharp structure
   unless the decoder is powerful.
5. **Mode coverage.** A GAN can collapse to a subset of the data; report the
   coverage of the statistics that matter physically, not only the loss.
6. **Leakage and non-stationarity still apply.** A conditional generative model
   used to augment training data must not see the validation region.

## The honest summary

The three families make the generation problem tractable in three different ways,
and their evaluation differs accordingly. The demonstration's VAE has an exact
objective: the ELBO rises by $4397.4733$ nats from the prior to the exact
posterior, and because the family contains the truth the bound is tight to
$0.0011$ nats. Its GAN-equivalent statement is weaker: a matched generator leaves
the discriminator at AUC $0.4857$, which is indistinguishable from chance, while a
poor one leaves it at $0.9692$ — a two-sample test, not a likelihood. The
diffusion schedule fixes everything except the reverse step, and it destroys
$50\ \%$ of the signal by step $259$ of $1000$. What none of these establishes is
that a generated field is *geologically* valid; that requires the physical
statistics of the problem to be checked explicitly.

## Python demonstration

[`code/generative_models_demo.py`](./code/generative_models_demo.py) prints every
number quoted above. It:

1. evaluates the closed-form ELBO at three parameter settings, including the exact
   posterior;
2. measures a discriminator's AUC for a poor and a matched generator;
3. tabulates the forward diffusion signal-to-noise ratio.

```bash
cd 21-statistics-bayesian-ml/05-deep-learning/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python generative_models_demo.py
```

It runs in under a tenth of a second and prints only text.

## Exercises

Graded problems are in
[`exercises/06-generative-models-exercises.md`](./exercises/06-generative-models-exercises.md)
with worked solutions in
[`exercises/06-generative-models-solutions.md`](./exercises/06-generative-models-solutions.md).

## Mastery checkpoint

Without notes, the ELBO is $-11\,682.9057$ at the prior and $-7\,285.4324$ at the
exact posterior; a poor generator gives a discriminator AUC of $0.9692$ and a
matched one $0.4857$; and the diffusion SNR reaches $1$ at step $259$ of $1000$.

1. Compute the ELBO improvement and state why the maximum equals the log evidence
   here.
2. Compute the chance level of the AUC and state what the matched generator's
   $0.4857$ implies.
3. Compute $\bar\alpha_{259}$ at the SNR crossover and verify that
   $\bar\alpha/(1-\bar\alpha) = 1$.
4. State two evaluations a generated seismic volume must pass that no likelihood
   tests.

## Common pitfalls

1. **Reading a high ELBO as good samples.** The bound concerns likelihood, not
   appearance or physics.
2. **Using one statistic to certify a generator.** A discriminator AUC near $0.5$
   is necessary, not sufficient.
3. **Mode collapse.** Report the coverage of physically meaningful statistics.
4. **Comparing a GAN and a VAE by their losses.** The quantities are not
   comparable.
5. **Ignoring the sampling cost of diffusion.** Hundreds of network evaluations
   per sample is a real constraint.
6. **Augmenting training data with a generative model that saw the validation
   set.** That is leakage through a learned map.

## Where this is used

- **Facies and property simulation**: generating geological realisations with
  prescribed statistics.
- **Seismic data augmentation** for classification when labels are scarce.
- **Inverse-problem priors**: a learned prior over models, sampled instead of
  parameterised.
- **Super-resolution and interpolation** of seismic and remote-sensing data.
- **Uncertainty quantification**: ensembles of generated fields as posterior
  samples.

## Related lessons

- [21-05-05 Autoencoders for Compression and Denoising](05-autoencoders.md) —
  the reconstruction model the VAE extends with a distribution.
- [21-03-05 Variational Inference and Scalable Bayes](../03-bayesian-inference/05-variational-inference.md) —
  the ELBO and its KL gap.
- [21-02-04 Conditional Simulation and Uncertainty Realisations](../02-geostatistics/04-simulation-geostatistics.md) —
  the geostatistical route to the same goal.
- [21-05-07 Self-Supervised Learning with Unlabelled Earth Data](07-self-supervised.md) —
  using unlabelled data without generating from them.
- [21-06-05 ML-Based Denoising of Geophysical Signals](../06-ml-in-geophysics/05-denoising-ml.md) —
  a discriminative use of the same architectures.

## Self-assessment checklist

- [ ] I can write and evaluate a VAE objective.
- [ ] I can state when the ELBO is exact.
- [ ] I can read the adversarial objective as a two-sample test.
- [ ] I can compute a diffusion schedule and its SNR.
- [ ] I can choose a family from the available evaluation.
- [ ] I can name a physical check no likelihood provides.
