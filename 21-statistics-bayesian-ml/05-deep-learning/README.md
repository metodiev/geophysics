# Module 21-05 — Deep Learning

**Stages:** doctoral → research · **Prerequisites:**
[21-04 Machine Learning Fundamentals](../04-machine-learning-fundamentals/README.md),
[21-03 Bayesian Inference](../03-bayesian-inference/README.md) and
[21-01 Statistics in Geophysical Practice](../01-statistics-in-practice/README.md).

Deep learning is the part of machine learning where the model class stops being
chosen in advance and starts being learned. That single change produces both the
power and the difficulty of the subject: a network with enough parameters can
represent relations no hand-built feature could express, and nothing in the
training loss tells you which of those relations it actually found. This module
therefore treats every architecture as a **statement about the structure of the
data** and then measures what that statement costs. Weight sharing asserts
stationarity; a recurrence asserts that a fixed-size state summarises the past;
attention asserts that any two positions may be related; a generative model
asserts a distribution over the data. In each case the lesson states the
assumption, measures the effect it produces, and names the situation in which it
fails.

The organising idea is that **the architecture is an assumption and the
demonstration is the price of it.** A $32\times32$ image with sixteen $3\times3$
kernels uses $160$ parameters where a fully connected layer to the same output uses
$16\,793\,600$ — a factor of $104\,960$ bought entirely by assuming the same filter
is right everywhere. A recurrent network carries a $40$-step dependence with
$1.48\ \%$ of its gradient intact, and a gate with $g = 0.9959$ carries $84.95\ \%$:
the difference between an assumption that fails and an assumption that is learned.
Attention makes the dependence between any two positions a single step, and pays
$1\,048\,576$ score operations at $T = 128$ where the recurrence pays $524\,288$ —
the crossover is exactly $T = d$, and it is the reason long records are windowed or
downsampled. None of this is folklore in this module; each number is printed by a
demonstration you can run.

A second thread is **evaluation**, which is harder here than anywhere else in the
folder. A network can fit a target it cannot generalise from; a generative model can
match the first two moments of a distribution and produce fields no geologist would
accept; a self-supervised representation can lower its own objective while carrying
no useful information. The module's answer is to always print the comparison that
makes a number interpretable. Linear autoencoders are checked against PCA
($0.010474$ against $0.010474$, a ratio of $1.000000$) so that a nonlinear gain can
be attributed to curvature rather than to the optimiser. A variational bound is
evaluated at the exact posterior ($4\,397.4733$ nats above the prior) so that a
tightness gap of $0.0011$ nats certifies the implementation. A frozen
representation is reported against **raw features**, and in this module it loses —
$0.9133$ against $0.9600$ — which is the result that makes the protocol worth
following.

A third thread is **honesty about what was not measured.** All data in this module
are **SYNTHETIC**; no measured value is used anywhere, and the lessons say so in
every section that quotes a number. Every demonstration generates its data from
stated parameters, implements its models from scratch with NumPy (no scikit-learn or
deep-learning framework), prints the numbers the lessons quote, seeds with
`np.random.default_rng(20261014)`, needs no network, creates no files, produces no
plots, exits 0, and each runs in under three seconds.

## Learning objectives

By the end of this module you will be able to:

1. **Write** the forward pass, the loss and the gradient of a feedforward network,
   **verify** the backward pass by finite differences, and **explain** why a linear
   model cannot fit XOR.
2. **Explain** what weight sharing assumes, **compute** its parameter saving, and
   **measure** translation equivariance and the receptive field of a stack.
3. **Write** the recurrence and the gradient of backpropagation through time,
   **compute** the decay $\rho^{T}$, and **show** what a gate changes.
4. **Write** scaled dot-product attention, **apply** a causal mask, **compute** a
   positional encoding, and **choose** between attention and a recurrence on cost.
5. **Show** that a linear autoencoder spans the PCA subspace, **measure** the gain
   from nonlinearity on a curved manifold, and **train** a denoising autoencoder.
6. **Evaluate** a variational bound, **interpret** a discriminator's AUC as a
   two-sample statistic, and **compute** a diffusion signal-to-noise schedule.
7. **Define** a pretext task, **write** the InfoNCE loss, and **evaluate** a
   representation with a linear probe against honest baselines.

## Prerequisites

- [21-04-02 Bias-Variance Trade-Off, Underfitting and Overfitting](../04-machine-learning-fundamentals/02-bias-variance.md) —
  the ledger that decides whether a deeper model helps.
- [21-04-03 Cross-Validation, Metrics and the Danger of Leakage](../04-machine-learning-fundamentals/03-model-assessment.md) —
  the discipline every network evaluation here inherits.
- [21-04-07 PCA, ICA and Manifold Learning](../04-machine-learning-fundamentals/07-dimensionality-reduction.md) —
  the linear methods the autoencoder generalises.
- [21-03-05 Variational Inference and Scalable Bayes](../03-bayesian-inference/05-variational-inference.md) —
  the ELBO that reappears as a generative objective.
- [21-01-05 Nonparametric Statistics and Kernel Density Estimation](../01-statistics-in-practice/05-nonparametric-methods.md) —
  kernels and smoothing, which attention and convolution both generalise.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Neural Networks: Architecture, Activation, Backpropagation](01-neural-networks.md) | doctoral | A linear model sits at the $\ln 2 = 0.6931$ floor on XOR; four hidden units reach $0.0003$ and the gradient check agrees to $5.72\times10^{-11}$ |
| 02 | [Convolutional Networks for Seismic and Image Data](02-cnns.md) | research | Weight sharing cut the parameters from $16\,793\,600$ to $160$; a three-cell shift moved the response by exactly three cells |
| 03 | [Recurrent Networks and Temporal Earth Data](03-rnns-time-series.md) | research | A $40$-step dependence keeps $1.48\times10^{-2}$ of its gradient at $\rho = 0.9$ and $8.495\times10^{-1}$ behind an open gate |
| 04 | [Attention and Transformers for Geophysical Sequences](04-transformers.md) | research | Every attention row sums to $1.000000$; attention overtakes a recurrence in cost exactly at $T = d = 64$ |
| 05 | [Autoencoders for Compression and Denoising](05-autoencoders.md) | research | A linear autoencoder matched PCA at $0.010474$; nonlinearity cut a parabola's error from $0.046119$ to $0.000013$ |
| 06 | [GANs, VAEs and Diffusion Models](06-generative-models.md) | research | The ELBO improved by $4397.4733$ nats to the exact posterior; the diffusion SNR reaches $1$ at step $259$ of $1000$ |
| 07 | [Self-Supervised Learning with Unlabelled Earth Data](07-self-supervised.md) | research | Masked reconstruction removed $86.9\ \%$ of the error on hidden entries; a frozen random projection still lost to raw features, $0.9133$ against $0.9600$ |

## Suggested path

**If you are new to deep learning:** lessons 01 → 02 → 03, running every
demonstration and reading the finite-difference check and the gradient-decay table
before anything else. Lesson 01's XOR ladder and lesson 03's $\rho^{T}$ table are
the two results that explain most failures of small networks on geophysical data.

**If you work with seismic images or volumes:** lesson 02 in full, then lesson 05,
then 07. Parameter counts, receptive fields and the denoising comparison are the
parts that transfer directly; §5 of lesson 02 on what convolution does not supply
is the part that is usually forgotten.

**If your records are long:** lesson 03 → lesson 04. The comparison of cost at
matched dimension ($T^{2}d$ against $Td^{2}$) decides the architecture, and the
crossover is a number rather than an opinion.

**If you are building a generative model:** lesson 05 → lesson 06. Run the ELBO at
the exact posterior first: an implementation that does not reach the analytic
evidence on a conjugate problem will not be saved by a larger model.

**If labels are scarce:** lesson 07 → lesson 05. Read the linear-probe table
against the raw-feature baseline before pretraining anything, because the protocol
is where most claimed gains are lost.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-neural-networks.md`](01-neural-networks.md) | Lesson 01 |
| [`02-cnns.md`](02-cnns.md) | Lesson 02 |
| [`03-rnns-time-series.md`](03-rnns-time-series.md) | Lesson 03 |
| [`04-transformers.md`](04-transformers.md) | Lesson 04 |
| [`05-autoencoders.md`](05-autoencoders.md) | Lesson 05 |
| [`06-generative-models.md`](06-generative-models.md) | Lesson 06 |
| [`07-self-supervised.md`](07-self-supervised.md) | Lesson 07 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Seven runnable demonstrations |

| Script | What it measures |
|---|---|
| [`code/neural_networks_demo.py`](code/neural_networks_demo.py) | The XOR capacity ladder, a finite-difference gradient check, tanh against ReLU |
| [`code/cnns_demo.py`](code/cnns_demo.py) | A convolution computed directly, convolutional against dense parameter counts, receptive fields and equivariance |
| [`code/rnns_time_series_demo.py`](code/rnns_time_series_demo.py) | BPTT training on a running-mean task, the vanishing-gradient table, a gated recurrence |
| [`code/transformers_demo.py`](code/transformers_demo.py) | Attention weights and causal masking, a sinusoidal encoding and entropy, the cost scaling against $T$ |
| [`code/autoencoders_demo.py`](code/autoencoders_demo.py) | A linear autoencoder against PCA, a nonlinear autoencoder on a parabola, a denoising comparison |
| [`code/generative_models_demo.py`](code/generative_models_demo.py) | A closed-form ELBO, discriminator AUC for two generators, a diffusion signal-to-noise schedule |
| [`code/self_supervised_demo.py`](code/self_supervised_demo.py) | Masked reconstruction against a mean baseline, InfoNCE against negative difficulty, a linear probe at three label budgets |

## How to run the demos

Use the project virtual environment, which provides NumPy and SciPy:

```bash
cd 21-statistics-bayesian-ml/05-deep-learning/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python neural_networks_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python cnns_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python rnns_time_series_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python transformers_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python autoencoders_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python generative_models_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python self_supervised_demo.py
```

Every demo prints labelled results, seeds its random numbers with
`np.random.default_rng(20261014)`, uses no network access, creates no files,
produces no plots and exits 0. All run in under three seconds; the longest,
`rnns_time_series_demo.py`, takes about two and a half seconds because of the
full-batch training runs.

## Mastery checkpoint

Complete this without notes, using the demonstrations only to check arithmetic:

> A colleague trains a convolutional network to pick first arrivals from a
> regional network. **(a)** They report that the model has $160$ parameters in the
> first layer and describe it as "tiny", while the classifier head is fully
> connected to the same spatial size; state the count that makes their comparison
> apples-to-apples. **(b)** Their records are $60\,\mathrm s$ long at
> $100\,\mathrm{Hz}$; they propose a transformer over the full record. State the
> two costs they must budget for and the crossover length for a model dimension of
> $64$. **(c)** Their first attempts converge to a constant output and they blame
> the optimiser; state the diagnostic that separates "cannot represent" from
> "failed to optimise" on a synthetic target. **(d)** They augment their training
> set with a generative model trained on all available data, including the
> validation blocks. State the error and the split protocol that fixes it.
> **(e)** They pretrain on unlabelled records from another network and report a
> linear-probe accuracy of $0.9133$; state the two baselines that must accompany
> that number.

Worked versions of (a)–(e) appear in the lesson solutions at ★★★ level.

## Common pitfalls across this module

1. **Reporting the training loss.** A network can fit a target it cannot
   generalise from; the held-out score is the result.
2. **Assuming the architecture supplies what it does not.** Convolution gives
   equivariance, not invariance to rotation or scale, and no global context.
3. **Blaming the optimiser for a capacity limit — or the reverse.** Separate them
   with restarts, a supervised fit and a longer schedule.
4. **Reading attention weights as explanations.** They are influences under a
   fitted parameterisation, not causes.
5. **Using a wide bottleneck.** An autoencoder that can copy learns nothing; the
   bottleneck is the only pressure in a plain reconstruction objective.
6. **Comparing a GAN and a VAE by their losses.** A likelihood bound and a
   discriminator statistic are not commensurable.
7. **Reporting a probe without baselines.** $0.9133$ sounded like success and was
   a negative result against the raw features at $0.9600$.
8. **Assuming transfer.** Pretraining on one basin, sensor or acquisition does not
   license a claim about another without a blocked test.

## Related modules

- [21-04 Machine Learning Fundamentals](../04-machine-learning-fundamentals/README.md) —
  the estimators, validation discipline and dimensionality reduction this module
  extends.
- [21-01 Statistics in Geophysical Practice](../01-statistics-in-practice/README.md) —
  the uncertainty language used throughout.
- [21-03 Bayesian Inference](../03-bayesian-inference/README.md) — where the ELBO
  and the prior over parameters come from.
- [21-06 Machine Learning in Geophysics](../06-ml-in-geophysics/README.md) — the
  applied versions of every architecture here on real Earth data.
- [21-09 Ethical and Responsible Quantitative Practice](../09-ethical-and-responsible-analytics/README.md) —
  reproducibility and honest reporting of the uncertainties these models carry.
- [20-06 Polarisation and Array Processing](../../20-signal-processing/06-polarisation-and-array-processing/README.md) —
  the classical multichannel view of what a convolutional stack learns.
