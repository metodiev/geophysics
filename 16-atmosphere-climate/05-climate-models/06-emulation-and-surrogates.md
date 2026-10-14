---
id: 16-05-06
title: "Emulators and Surrogate Models for Climate"
level: research
prereqs: ["16-05-01", "16-05-03", "21-04-01"]
tags: [atmosphere, climate, climate-models, emulation, gaussian-process, surrogate, uncertainty]
---

# Emulators and Surrogate Models for Climate

> All models and data in this module are **SYNTHETIC**. Every number below was
> printed by
> [`code/emulation_and_surrogates_demo.py`](code/emulation_and_surrogates_demo.py).
> The "climate model" is a chosen nonlinear algebraic response, used because its
> answer is computable exactly, so that surrogate error can be measured rather
> than estimated.

## Learning objectives

By the end of this lesson you will be able to:

1. **Distinguish** an emulator from a surrogate and from a reduced-order model
   by what each one approximates.
2. **Write down** Gaussian-process regression with an RBF kernel, including the
   marginal likelihood and the predictive mean and variance.
3. **Derive** why the predictive variance returns to the prior far from training
   data, and **state** what that does and does not tell you.
4. **Measure** interpolation and extrapolation error for a fitted emulator and
   for a polynomial surrogate, and **compare** them.
5. **Explain** why an emulator is confidently wrong across an unsampled
   threshold, and **quantify** the miscalibration.
6. **State** the difference between emulator uncertainty and structural model
   error, and why conflating them is a serious error.
7. **Design** a training set for a stated emulation task, including its range and
   the placement of points near transitions.

## Prerequisites

- [16-05-01 Model Hierarchy: EBMs, EMICs, GCMs, ESMs](01-climate-model-hierarchy.md) —
  the simple end of the hierarchy that emulators replace.
- [16-05-03 Model Evaluation, Skill and Benchmarking](03-model-evaluation.md) —
  the metrics used to score an emulator.
- [21-04 Machine Learning Fundamentals](../../21-statistics-bayesian-ml/04-machine-learning-fundamentals/README.md) —
  regression, kernels and generalisation.

## 1. Intuition: paying for speed with assumptions

A climate model is expensive. A study that needs $10^{5}$ model evaluations —
for calibration, for a large ensemble, for uncertainty propagation — cannot
afford them. An **emulator** is a statistical approximation of the model's
input–output map, fast enough to evaluate $10^{5}$ times, trained on a few
hundred to a few thousand model runs.

The trade is explicit. You replace the physics by a smooth statistical surface.
Everything the emulator says inside the training region is an interpolation of
runs you paid for; everything outside is an extrapolation with no physical
content at all. The emulator's own uncertainty is a statement about *distance
from training data*, not about *disagreement with reality* — a point we
quantify in Section 6.

The distinction that matters:

- A **surrogate** is any cheap approximation (polynomial, neural network,
  lookup table).
- An **emulator** is a surrogate that also reports a predictive distribution —
  an estimate and an uncertainty.
- A **reduced-order model** is different in kind: it simplifies the *equations*
  (projecting the state onto a small basis) rather than fitting the input–output
  map.

## 2. Definitions

- **Design.** The set of input points at which the expensive model was run.
- **Gaussian process (GP).** A distribution over functions, specified by a mean
  function and a covariance kernel. Conditioning on data gives a predictive
  distribution at any input.
- **Kernel length scale $\ell$.** The distance over which the function is
  assumed to vary.
- **Marginal likelihood.** The probability of the training targets under the GP
  prior, used to select hyperparameters without a validation set.
- **Predictive variance.** The GP's own uncertainty at a test input; it grows
  with distance from the design.
- **Calibration.** Whether the stated uncertainty is the right size — measured by
  how often the truth falls inside a stated interval.
- **Extrapolation.** Evaluation outside the range of the design. A GP has no
  information there beyond its prior.

## 3. Derivation: Gaussian-process regression

### 3.1 The model

Assume the expensive model $f(\mathbf{x})$ is a draw from a GP,

$$f(\mathbf{x}) \sim \mathcal{GP}\bigl(m(\mathbf{x}), k(\mathbf{x},\mathbf{x}')\bigr),
\qquad
k(\mathbf{x},\mathbf{x}') = \sigma_f^{2}\exp\!\left(-\frac{\|\mathbf{x}-\mathbf{x}'\|^{2}}{2\ell^{2}}\right),$$

with observations $y_i = f(\mathbf{x}_i) + \varepsilon_i$,
$\varepsilon_i \sim \mathcal{N}(0,\sigma_n^{2})$ independent. The RBF kernel
encodes smoothness; $\ell$ is the assumed correlation length.

### 3.2 Conditional distribution

Stack the data in $\mathbf{y}$ and form
$K = [k(\mathbf{x}_i,\mathbf{x}_j)] + \sigma_n^{2}I$ and
$\mathbf{k}_* = [k(\mathbf{x}_i,\mathbf{x}_*)]$. The predictive distribution at
$\mathbf{x}_*$ is Gaussian with

$$\mu_* = \bar y + \mathbf{k}_*^{\mathsf T}K^{-1}(\mathbf{y}-\bar y\mathbf{1}),
\qquad
\sigma_*^{2} = k(\mathbf{x}_*,\mathbf{x}_*) - \mathbf{k}_*^{\mathsf T}K^{-1}\mathbf{k}_*.$$

Two limits are immediate:

- **At a training point**, $\sigma_*^{2}\to\sigma_n^{2}$ (the noise floor): the
  emulator is as uncertain as the data are noisy.
- **Far from all training points**, $\mathbf{k}_*\to\mathbf{0}$, so
  $\mu_*\to\bar y$ and $\sigma_*^{2}\to\sigma_f^{2}$: the emulator returns to
  its prior mean with prior-sized uncertainty in the input direction, *while*
  reporting the mean as if it were a prediction.

### 3.3 Hyperparameters

$\ell$, $\sigma_f$ and $\sigma_n$ are chosen by maximising the log marginal
likelihood

$$\log p(\mathbf{y}) = -\tfrac12(\mathbf{y}-\mu)^{\mathsf T}K^{-1}(\mathbf{y}-\mu)
-\tfrac12\log|K| - \tfrac{n}{2}\log 2\pi.$$

The demonstration selects them by a finite grid search over
$(0.3,0.5,1.0,2.0)\times(0.5,1.0,2.0)\times(0.01,0.05,0.1)$, which is enough to
show the mechanism; real applications optimise continuously and report the
sensitivity of the fit to the optimiser's starting point.

## 4. The expensive model being emulated

The demonstration uses an equilibrium response with a *state-dependent* feedback
parameter

$$\lambda(\Delta T) = 0.8 + 0.6\tanh\!\left(\frac{\Delta T - 1.0}{1.5}\right)
\ \mathrm{W\,m^{-2}\,K^{-1}},
\qquad F = \lambda(\Delta T)\,\Delta T,$$

solved for $\Delta T$ by root finding ($\mathrm{xtol} = 10^{-12}$). The feedback
strengthens with warming, so the response is sublinear:

| $F$ (W/m²) | nonlinear $\Delta T$ (K) | linear $F/0.8$ (K) | difference (K) |
|---|---|---|---|
| 1.0 | 1.1585 | 1.2500 | $-0.0915$ |
| 2.0 | 1.8201 | 2.5000 | $-0.6799$ |
| 4.0 | 3.0210 | 5.0000 | $-1.9790$ |
| 6.0 | 4.3290 | 7.5000 | $-3.1710$ |
| 8.0 | 5.7233 | 10.0000 | $-4.2767$ |
| 12.0 | 8.5717 | 15.0000 | $-6.4283$ |

The nonlinearity is the point: a *linear* surrogate is exact nowhere except at
the origin, and its error grows monotonically. A GP trained on part of this
curve should do much better than the linear surrogate *inside* the design, and
no better *outside* it — because outside, the information is not there.

## 5. Measurement: interpolation versus extrapolation

The demonstration draws 12 training points uniformly on
$F\in[0,6]\ \mathrm{W\,m^{-2}}$, adds noise with $\sigma_n = 0.02\ \mathrm{K}$,
fits a GP, and scores it on a dense grid inside $[0,6]$ and outside, on
$[6,12]$:

| surrogate | RMSE inside (K) | RMSE outside (K) |
|---|---|---|
| GP, 12 points | 0.0830 | 3.2512 |
| linear $F/0.8$ | 1.7186 | 4.9056 |

Three readings:

- **Inside the design, the GP beats the linear surrogate by a factor of $20.7$**
  ($1.7186/0.0830$). Emulation works where the assumption of smoothness is
  supported by data.
- **Outside the design, the GP is only modestly better than the linear
  surrogate** ($3.2512$ vs $4.9056$), and its advantage comes entirely from its
  prior mean rather than from the physics.
- **The worst extrapolation is not where the uncertainty is largest.** At
  $F = 12\ \mathrm{W\,m^{-2}}$ the GP's error is $5.8037\ \mathrm{K}$ while its
  own stated standard deviation is $0.9988\ \mathrm{K}$ — the emulator is wrong
  by nearly six times its claimed uncertainty. It *is* visibly unsure
  ($0.9988 \gg 0.0142\ \mathrm{K}$ inside), but "unsure" is not "unbiased": the
  mean has reverted to the prior while the truth has carried on rising.

Adding training points helps inside and not outside: with $N = 6, 12, 24, 48$
the inside RMSE falls $0.3016 \to 0.1466 \to 0.0277 \to 0.0131\ \mathrm{K}$,
while the outside RMSE shows no such trend
($3.2698, 4.1003, 3.5183, 3.6163\ \mathrm{K}$). **An emulator is no better than
its design.**

## 6. Confidently wrong across a threshold

The sharpest failure is not extrapolation but *interpolation across a feature the
design never sampled*. The demonstration builds a response with a step of
$+1.80\ \mathrm{K}$ at $F = 4.0\ \mathrm{W\,m^{-2}}$, and draws 28 training
points that avoid a window of $\pm0.6\ \mathrm{W\,m^{-2}}$ around the step.

| quantity | value |
|---|---|
| emulator RMSE over the whole range | $0.2506\ \mathrm{K}$ |
| mean absolute error in $\lvert F - 4\rvert < 0.4$ | $0.6944\ \mathrm{K}$ |
| mean stated standard deviation there | $0.0605\ \mathrm{K}$ |
| ratio (error / stated sd) | $11.470$ |

The emulator bridges the two branches smoothly, and inside the gap it is wrong
by **eleven times** its own stated uncertainty. This is the practical warning:
a GP's predictive variance measures distance from training points. It does not
know that the physics has a kink, and it will report interpolation-grade
confidence on the wrong side of a tipping point — which is precisely where the
answer is most consequential, and where a design built from a uniform random
sample is least likely to have placed points.

The remedy is a design decision, not a statistical one: either sample densely
near transitions, or add a mean function carrying the known physics, or use a
kernel that permits non-smoothness. All three require knowing something about
the model before emulating it.

## 7. Worked example: costing a linear surrogate

*Problem.* A study uses the linear surrogate $\Delta T = F/0.8$ for rapid
scenario exploration over $F\in[0,12]\ \mathrm{W\,m^{-2}}$. Quantify its error
at three forcings using the demonstration's model.

*Solution.*

1. $F = 2$: surrogate $2.5000\ \mathrm{K}$, truth $1.8201\ \mathrm{K}$,
   error $+0.6799\ \mathrm{K}$ ($+37.4\%$ of the truth).
2. $F = 4$: surrogate $5.0000\ \mathrm{K}$, truth $3.0210\ \mathrm{K}$,
   error $+1.9790\ \mathrm{K}$ ($+65.5\%$).
3. $F = 12$: surrogate $15.0000\ \mathrm{K}$, truth $8.5717\ \mathrm{K}$,
   error $+6.4283\ \mathrm{K}$ ($+75.0\%$).

*Interpretation.* The surrogate is not merely imprecise; it is **biased in one
direction**, and the bias grows with forcing. Its RMSE inside the range is
$1.7186\ \mathrm{K}$ (Section 5) and outside $4.9056\ \mathrm{K}$. A study that
reports a range of outcomes from such a surrogate has not reported a range of
physical possibilities; it has reported the error of its own approximation. The
same arithmetic applies to any surrogate, including a GP: what matters is
whether the approximation was validated *in the regime where it is used*.

## 8. Assumptions and regime of validity

1. **Smoothness.** The RBF kernel assumes the response is infinitely
   differentiable on the scale $\ell$. A threshold, a regime switch or a
   discontinuity violates this and produces the failure of Section 6.
2. **Stationarity of the response.** The GP assumes one kernel applies
   everywhere. A response whose roughness changes with input requires a
   non-stationary kernel.
3. **Independent Gaussian noise on the training targets.** Real model output has
   correlated and sometimes non-Gaussian error.
4. **The design defines the emulator.** No hyperparameter choice can supply
   information absent from the design.
5. **Emulator uncertainty $\ne$ model error.** The predictive variance is about
   the emulator's knowledge of the *simulator*. It says nothing about how well
   the simulator represents the Earth.
6. **No scenario content.** An emulator cannot interpolate over a mechanism the
   training runs never activated (for example a forcing that only switches on
   above some level).

## 9. Units and dimensional analysis

| quantity | symbol | unit | check |
|---|---|---|---|
| forcing | $F$ | $\mathrm{W\,m^{-2}}$ | |
| warming | $\Delta T$ | K | |
| feedback parameter | $\lambda$ | $\mathrm{W\,m^{-2}\,K^{-1}}$ | $F = \lambda\Delta T$ |
| length scale | $\ell$ | $\mathrm{W\,m^{-2}}$ (here) | same unit as the input |
| signal sd | $\sigma_f$ | K | same unit as the output |
| predictive sd | $\sigma_*$ | K | |

The length scale carries the unit of the *input*, the signal amplitude the unit
of the *output*. A kernel written with $\ell$ in kelvin on a forcing input is a
unit error even though the code will run, because it makes the smoothness
assumption dimensionally meaningless.

## 10. Python demonstration

[`code/emulation_and_surrogates_demo.py`](code/emulation_and_surrogates_demo.py):

1. defines the nonlinear response and tabulates it against a linear surrogate;
2. fits a GP by marginal likelihood over a hyperparameter grid and reports the
   selected values;
3. scores the emulator inside and outside the design, against the linear
   surrogate;
4. repeats the fit for four training-set sizes, showing that only the
   interpolation error improves;
5. trains on a design that excludes a threshold and quantifies the
   miscalibration (error / stated sd).

The GP is implemented directly with `numpy` (Cholesky solves, no libraries
beyond SciPy's `brentq` for the root find). It is print-only, seeded with
`np.random.default_rng(20261014)`, and exits 0.

## 11. Exercises

See [`exercises/06-emulation-and-surrogates-exercises.md`](exercises/06-emulation-and-surrogates-exercises.md)
and [`exercises/06-emulation-and-surrogates-solutions.md`](exercises/06-emulation-and-surrogates-solutions.md).

## Mastery checkpoint

> **(a)** Write the GP predictive mean and variance for a single training point
> $(\mathbf{x}_1,y_1)$ with noise $\sigma_n^{2}$ and RBF kernel with amplitude
> $\sigma_f^{2}$ and length scale $\ell$. Evaluate both at $\mathbf{x}=\mathbf{x}_1$
> and as $\lVert\mathbf{x}-\mathbf{x}_1\rVert\to\infty$.
> **(b)** A GP is trained on $F\in[0,4]$ and asked for $\Delta T$ at
> $F = 8\ \mathrm{W\,m^{-2}}$. It returns $2.0\ \mathrm{K}$ with a stated
> standard deviation of $1.5\ \mathrm{K}$. State what the returned mean is, and
> why the standard deviation gives no protection against being wrong.
> **(c)** The demonstration's step-response emulator has an error-to-uncertainty
> ratio of $11.470$ in the unsampled window. State two design changes that would
> reduce it, and the cost of each.
> **(d)** Give one question for which a linear surrogate of the form
> $\Delta T = F/\lambda_0$ is defensible, and one for which it is not.

## Common pitfalls

1. **Treating the emulator's uncertainty as total uncertainty.** It describes
   ignorance of the simulator, not of the Earth.
2. **Extrapolating.** Outside the design a GP returns its prior mean; the smooth
   curve is an artefact.
3. **Assuming a good interpolation RMSE implies a good emulator.** Section 6 has
   an RMSE of $0.2506\ \mathrm{K}$ and a miscalibration factor of $11.470$ in the
   region that matters.
4. **Trusting a uniform random design near thresholds.** Uniform sampling puts
   few points where the response changes fastest.
5. **Selecting hyperparameters on the test set.** Use the marginal likelihood or
   a held-out split; never tune on the evaluation data.
6. **Forgetting the surrogate's error is systematic.** It does not cancel by
   averaging over many surrogate evaluations.

## Related modules

- [16-05 Climate Models](README.md).
- [16-05-05 CMIP, Model Intercomparison and Ensemble Design](05-coupled-model-intercomparison.md) —
  the ensembles emulators are used to generate.
- [18-06-04 Surrogate Models for Uncertainty Quantification](../../18-inverse-problems/06-uncertainty-quantification/04-surrogate-uq.md) —
  the same machinery for propagating uncertainty.
- [21-04 Machine Learning Fundamentals](../../21-statistics-bayesian-ml/04-machine-learning-fundamentals/README.md).
- [21-03 Bayesian Inference](../../21-statistics-bayesian-ml/03-bayesian-inference/README.md) —
  the probabilistic framework behind the GP.
