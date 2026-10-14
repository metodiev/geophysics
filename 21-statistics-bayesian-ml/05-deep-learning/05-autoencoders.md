---
id: 21-05-05
title: "Autoencoders for Compression and Denoising"
level: research
prereqs: ["21-05-01", "21-04-07"]
estimated_minutes: 55
tags: [deep-learning, autoencoders, dimensionality-reduction, denoising, representation-learning]
---

# Autoencoders for Compression and Denoising

## Learning objectives

By the end of this lesson you will be able to:

1. **Write** the autoencoder objective and **explain** what the bottleneck
   enforces.
2. **Show** that a linear autoencoder with squared error spans the same subspace
   as PCA, and **measure** the agreement.
3. **Measure** the gain a nonlinear autoencoder obtains on a curved manifold and
   **state** where the gain comes from.
4. **Explain** denoising by training on corrupted inputs and **measure** the
   improvement over a network trained on clean data.
5. **Choose** the bottleneck dimension and the corruption level from data rather
   than habit.
6. **State** what an autoencoder's latent code does and does not represent.

All data in this lesson are **SYNTHETIC**, generated in the demonstration. No
measured value is used.

## Prerequisites

- [21-05-01 Neural Networks: Architecture, Activation, Backpropagation](01-neural-networks.md) —
  the layers and gradients used here.
- [21-04-07 PCA, ICA and Manifold Learning](../04-machine-learning-fundamentals/07-dimensionality-reduction.md) —
  the linear method the autoencoder generalises.
- [21-01-05 Nonparametric Statistics and Kernel Density Estimation](../01-statistics-in-practice/05-nonparametric-methods.md) —
  the bias-variance view of a smoothing estimate.

## 1. Intuition: force the data through a narrow channel

An autoencoder is trained to reproduce its own input through a bottleneck: an
**encoder** $f_\theta$ maps $x$ to a low-dimensional code $z$, and a **decoder**
$g_\phi$ maps $z$ back to $\hat x$. The loss is reconstruction error,
$\|x - g_\phi(f_\theta(x))\|^{2}$. Nothing in the objective mentions the target
task; structure is learned because the bottleneck makes copying impossible, so the
network must discover the directions in which the data actually vary.

That is exactly the argument that motivates PCA. The difference is that the
encoder and decoder are nonlinear, so the code can follow a curved manifold rather
than a linear subspace. The two ideas coincide in the linear case, and that
coincidence is the best available sanity check on an autoencoder implementation.

## 2. The linear case is PCA

For a linear encoder $z = W_1x$ and decoder $\hat x = W_2z$ with squared error,
the optimum spans the same subspace as the leading principal components of the
centred data. The demonstration measures it: on $500$ samples with a
one-dimensional latent variable embedded in two features, PCA's one-component
reconstruction MSE is $0.010474$ and a $2\to1\to2$ linear autoencoder trained by
gradient descent gives $0.010474$ — a ratio of $1.000000$ to six decimals.

The agreement is not a coincidence but a theorem, and it makes the linear
autoencoder useful as a test: a nonlinear autoencoder that cannot beat its linear
counterpart on a linear data set is not learning anything.

## 3. Where nonlinearity pays

On data that lie near a **curved** manifold the linear method leaves a systematic
residual, because no straight line can follow the curve. The demonstration places
$600$ points on the parabola $y = x^{2}$ with small noise and compares:

| model | reconstruction MSE |
|---|---|
| one-component PCA | $0.046119$ |
| nonlinear autoencoder ($2\to4\to2$, tanh) | $0.000013$ |

The nonlinear encoder learns a coordinate along the curve and reconstructs almost
exactly, a reduction of more than three orders of magnitude. The gain is not from
having more parameters — the bottleneck is still one-dimensional — but from the
bottleneck being able to bend.

## 4. Denoising

A **denoising autoencoder** is trained to map a corrupted input to the clean
target: it sees $x + \eta$ and is asked for $x$. It cannot copy, because the input
contains noise, so the only way to reduce the loss is to learn the structure the
noise does not share. The demonstration trains two identical one-hidden-layer
networks on a noisy sinusoid:

| training target | MSE on the clean signal |
|---|---|
| trained on clean inputs | $0.072169$ |
| trained noisy $\to$ clean | $0.052103$ |

The noisy input itself has MSE $0.082538$ against the clean signal, so the
denoising network removes $36.9\ \%$ of the corruption where the ordinary network
removes $12.6\ \%$. Both networks have the same width and the same bottleneck; the
difference is entirely in what they were asked to predict.

**Choosing the corruption level.** Too little noise and the task is copying; too
much and the input no longer identifies the signal. The useful range is where the
reconstruction error is minimised on *clean* held-out data — the standard
selection criterion, and one that must be evaluated on clean targets to be
meaningful.

## Assumptions and regime of validity

1. **The bottleneck must be tight enough.** A wide bottleneck can copy the input,
   including the noise, and learns nothing.
2. **The corruption model must match the real one.** A denoiser trained on
   Gaussian noise applied to spiky cultural noise removes the wrong thing.
3. **Scaling is required.** Reconstruction error is scale-sensitive; unscaled
   features make the loss a function of units.
4. **The code is not automatically interpretable.** Linearity gives the PCA
   property of orthogonal directions; a nonlinear code has no such structure.
5. **Reconstruction quality is not task quality.** A low reconstruction error
   certifies compression, not that the code is useful for prediction; the test is
   a downstream probe.
6. **Nonlinearity needs data.** A linear autoencoder is fitted from second moments;
   a nonlinear one needs enough samples to learn the manifold.

## The honest summary

An autoencoder is a reconstruction problem with a bottleneck, and its behaviour is
predictable from that description. In the linear case it reproduces PCA exactly —
$0.010474$ against $0.010474$, a ratio of $1.000000$ — which is the calibration
that makes the nonlinear case interpretable: on a parabola the nonlinear network
cut the reconstruction MSE from $0.046119$ to $0.000013$, a gain that comes from
following a curve, not from extra parameters. Denoising improved the clean-signal
MSE from $0.072169$ to $0.052103$ by changing only the training target. What none
of these numbers establish is that the learned code is *useful*: reconstruction
measures compression, and the value of a representation is decided by a downstream
task.

## Python demonstration

[`code/autoencoders_demo.py`](./code/autoencoders_demo.py) prints every number
quoted above. It:

1. trains a linear autoencoder and compares it with PCA;
2. trains a nonlinear autoencoder on a curved manifold;
3. compares a clean-trained and a denoising network on the same data.

```bash
cd 21-statistics-bayesian-ml/05-deep-learning/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python autoencoders_demo.py
```

It runs in about three quarters of a second and prints only text.

## Exercises

Graded problems are in
[`exercises/05-autoencoders-exercises.md`](./exercises/05-autoencoders-exercises.md)
with worked solutions in
[`exercises/05-autoencoders-solutions.md`](./exercises/05-autoencoders-solutions.md).

## Mastery checkpoint

Without notes, a linear autoencoder matches PCA at $0.010474$; a nonlinear
autoencoder reduces a parabola's reconstruction MSE from $0.046119$ to
$0.000013$; and a denoising network reaches $0.052103$ where a clean-trained one
reaches $0.072169$ on the same noisy input of MSE $0.082538$.

1. Compute the percentage of the noisy input's error removed by each network.
2. Compute the ratio of nonlinear to linear reconstruction error on the parabola.
3. State why the linear agreement is a useful test rather than a curiosity.
4. State the criterion for choosing the corruption level and the data it must be
   evaluated on.

## Common pitfalls

1. **A bottleneck that is too wide.** The network copies the noise and learns
   nothing.
2. **Reporting reconstruction error as utility.** It measures compression only.
3. **Mismatched corruption.** A Gaussian-trained denoiser on spiky noise removes
   the wrong structure.
4. **Forgetting to scale features.** The loss becomes a function of units.
5. **Interpreting a nonlinear code.** There is no analogue of the PCA directions.
6. **Evaluating a denoiser on noisy targets.** The criterion must be the clean
   signal.

## Where this is used

- **Seismic compression and reconstruction**: compressing volumes and filling
  gaps.
- **Denoising of geophysical signals**: paired synthetic training, applied to
  field data.
- **Well-log gap filling**: reconstructing missing intervals.
- **Anomaly detection**: high reconstruction error as the anomaly score.
- **Representation learning**: pretraining an encoder before supervised
  fine-tuning, the subject of
  [21-05-07](07-self-supervised.md).

## Related lessons

- [21-04-07 PCA, ICA and Manifold Learning](../04-machine-learning-fundamentals/07-dimensionality-reduction.md) —
  the linear theory and its limits.
- [21-05-06 GANs, VAEs and Diffusion Models](06-generative-models.md) —
  what changes when the code is given a distribution.
- [21-05-07 Self-Supervised Learning with Unlabelled Earth Data](07-self-supervised.md) —
  masked reconstruction as a pretext task.
- [21-05-01 Neural Networks: Architecture, Activation, Backpropagation](01-neural-networks.md) —
  the layers and gradients.
- [21-06-05 ML-Based Denoising of Geophysical Signals](../06-ml-in-geophysics/05-denoising-ml.md) —
  the applied version of the denoising section.

## Self-assessment checklist

- [ ] I can write the autoencoder objective and say what the bottleneck enforces.
- [ ] I can check a linear autoencoder against PCA.
- [ ] I can measure the gain from nonlinearity on a curved manifold.
- [ ] I can train and evaluate a denoising autoencoder.
- [ ] I can choose the bottleneck and the corruption level from data.
- [ ] I can say what a latent code does not guarantee.
