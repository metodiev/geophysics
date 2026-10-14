---
id: 20-03-05
title: "Adaptive Filtering and Noise Cancellation"
level: research
prereqs: ["20-03-02", "20-05-02"]
tags: [signal-processing, adaptive-filtering, lms, nlms, noise-cancellation, line-enhancer, convergence]
---

# Adaptive Filtering and Noise Cancellation

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the least-mean-squares (LMS) update rule as a stochastic gradient
   step on the mean squared error, and the normalised LMS (NLMS) rule from it.
2. **State** the optimal (Wiener) coefficient vector $w^{*} = R^{-1}p$ and the step
   size bound under which an adaptive filter converges.
3. **Explain** why an adaptive noise canceller needs a reference channel that is
   correlated with the interference but not with the signal.
4. **Measure** the signal-to-noise improvement as a function of step size and
   filter length, and **interpret** the non-monotonic shape.
5. **Configure** an adaptive line enhancer from a speech-like model and
   **explain** the role of the decorrelation delay.
6. **Diagnose** convergence-versus-misadjustment behaviour from a learning curve.

## Prerequisites

- [20-03-02 IIR Filter Design: Butterworth, Chebyshev, Elliptic](02-iir-filters.md) —
  the fixed filters this lesson makes adaptive.
- [20-05-02 Autocorrelation, Power Spectral Density and Wiener-Khinchin](../05-noise-and-random-signals/02-autocorrelation-spectra.md) —
  the autocorrelation and cross-correlation the normal equations are built from.

## 1. Intuition: let the data set the coefficients

A fixed filter is designed once and applied to everything. An adaptive filter
updates its own coefficients from the data, so it can track an interference path
that is unknown, changing, or different from channel to channel. The classic
geophysical use is **noise cancellation**: a second sensor records the noise but
not the signal (a reference channel), and the adaptive filter learns the transfer
function from the reference to the noise contaminating the signal channel, then
subtracts it.

The demo's synthetic problem is deliberately hard: the desired signal has variance
$0.0056$ and the interference variance $0.0988$, giving an **input SNR of
$-12.46$ dB**. The interference reaches the primary channel through an unknown
path of 6 samples of delay plus 3 filter taps (9 samples total). The adaptive
filter starts with all coefficients at zero and knows nothing about that path.

All models and data in this module are SYNTHETIC. No real seismic or
infrasound array is used.

## 2. Definitions

### 2.1 The canceller configuration

- $d[n]$ — the **primary** input: desired signal plus interference.
- $x[n]$ — the **reference** input: correlated with the interference in $d$, and
  uncorrelated with the desired signal.
- $w[n] \in \mathbb{R}^{M}$ — the adaptive coefficient vector.
- $y[n] = w^{\top}\mathbf{x}[n]$, with
  $\mathbf{x}[n] = (x[n], x[n-1], \dots, x[n-M+1])^{\top}$, the filter output.
- $e[n] = d[n] - y[n]$ — the **error**, which is the cleaned output.

### 2.2 Mean squared error

The cost is $\xi(w) = \mathbb{E}\!\left[e[n]^2\right]$, a quadratic bowl in $w$
with a unique minimum at the Wiener solution

$$w^{*} = R^{-1}p,\qquad R = \mathbb{E}\!\left[\mathbf{x}\mathbf{x}^{\top}\right],
\quad p = \mathbb{E}\!\left[d\,\mathbf{x}\right].$$

## 3. Derivations

### 3.1 The LMS update

Expand the cost:

$$\xi(w) = \mathbb{E}[d^2] - 2w^{\top}p + w^{\top}R w.$$

Its gradient is $\nabla\xi = -2p + 2Rw$. Steepest descent with step $\mu$ gives
$w \leftarrow w + 2\mu(p - Rw)$, which requires $R$ and $p$. The LMS algorithm
replaces the expectations by their instantaneous estimates, $\hat{R} =
\mathbf{x}\mathbf{x}^{\top}$ and $\hat{p} = d\,\mathbf{x}$:

$$w[n+1] = w[n] + 2\mu\,e[n]\,\mathbf{x}[n].$$

That is the whole algorithm: one multiply-add per coefficient per sample.

### 3.2 Normalised LMS

The convergence rate of LMS depends on the power of $\mathbf{x}$. Dividing the
step by that power makes the update scale-free:

$$w[n+1] = w[n] + \mu\,\frac{e[n]\,\mathbf{x}[n]}
{\mathbf{x}[n]^{\top}\mathbf{x}[n] + \varepsilon},$$

with $\varepsilon$ a small constant to guard against a zero-energy input. For
this normalised form the convergence condition is simply

$$0 < \mu < 2,$$

independent of the input power. The demo uses $\varepsilon = 10^{-6}$.

### 3.3 Why the reference must be noise-only

Write $d = s + v$ with $s$ the signal and $v$ the interference, and suppose the
reference contains $v$ but also a small amount of $s$. Then $y$ will adapt to
predict part of $s$ as well as $v$, and $e = d - y$ will contain $s - \hat{s}$:
**the canceller subtracts the signal it is meant to recover.** The
orthogonality principle makes this precise: at the optimum, $e$ is uncorrelated
with $\mathbf{x}$, so whatever part of $s$ is correlated with the reference is
removed from the output. This is the single most important assumption of the
method, and the hardest to guarantee in the field.

### 3.4 Convergence versus misadjustment

A larger step converges faster but leaves a larger steady-state error, because the
instantaneous-gradient estimate is noisy and a large $\mu$ lets that noise move the
coefficients. The excess mean squared error grows roughly as $\mu M\sigma_x^2/2$
for LMS. The result is the non-monotonic improvement the demo measures.

## 4. The measurement

### 4.1 Step size

With $M = 32$, sweeping $\mu$ from 0.002 to 1.0:

| $\mu$ | output SNR (dB) | improvement (dB) |
|---|---|---|
| 0.002 | $-8.99$ | 3.47 |
| 0.005 | $-5.82$ | 6.64 |
| 0.010 | $-3.06$ | 9.40 |
| 0.020 | $-0.42$ | 12.04 |
| 0.050 | $2.47$ | 14.93 |
| 0.100 | $3.41$ | **15.87** |
| 0.300 | $1.85$ | 14.31 |
| 0.600 | $0.27$ | 12.73 |
| 1.000 | $-0.89$ | 11.57 |

The improvement rises steeply, peaks at $\mu \approx 0.1$ (**$+15.87$ dB**, from
$-12.46$ to $+3.41$ dB) and then *falls*. The fall is the misadjustment term
beating the convergence term: a step of 1.0 is still inside the theoretical
stability bound $0<\mu<2$, but it leaves a residual error far above the optimum.
**A step size is not a free "make it work better" knob.**

### 4.2 Filter length

With $\mu = 0.02$:

| $M$ | improvement (dB) |
|---|---|
| 4 | 2.83 |
| 8 | **15.92** |
| 16 | 14.67 |
| 32 | 12.04 |
| 64 | 9.42 |
| 128 | 6.66 |

The best length is $M = 8$, just above the 9-sample interference path. Beyond it
the improvement *decreases*, because for a fixed $\mu$ more coefficients take
longer to converge and leave more excess error. The correct reading is not "longer
is worse" but "the length should match the path, and the step should be retuned
when the length changes".

### 4.3 The adaptive line enhancer

The line enhancer uses a *delayed copy of the clean input itself* as the
reference. The delay decorrelates broadband noise but not a sinusoid, so the
filter learns to predict the periodic part:

| quantity | value |
|---|---|
| periodic component | 25 Hz sinusoid |
| broadband noise | white, $\sigma = 0.496$ |
| input SNR | 3.09 dB |
| output SNR | 15.76 dB |
| improvement | $+12.67$ dB |

Note which signal is the output: for the line enhancer the **filter output $y$** is
the enhanced periodic signal and the error $e$ is the residual noise — the
opposite of the canceller, where $e$ is the cleaned signal. Getting this backwards
is the commonest implementation error.

### 4.4 Convergence curves

Cumulative mean squared error (dB) versus iteration:

| iteration | $\mu = 0.005$ | $\mu = 0.05$ |
|---|---|---|
| 200 | $-10.19$ | $-13.54$ |
| 400 | $-11.06$ | $-16.14$ |
| 800 | $-11.72$ | $-17.70$ |
| 1600 | $-13.06$ | $-18.90$ |
| 3200 | $-14.86$ | $-19.91$ |
| 3999 | $-15.74$ | $-20.87$ |

The larger step reaches 6.6 dB below the smaller one by iteration 400 and stays
ahead, but its floor is only 5 dB lower, consistent with the misadjustment
argument. With a fixed record length the faster step wins; in a non-stationary
setting the excess error would matter more.

## 5. Worked example (SYNTHETIC)

A seismic line records a shot with a nearby pump jack as interference.

1. **Reference**: an auxiliary geophone 2 m from the pump, far enough that the
   pump signal dominates and the seismic signal is weak.
2. **Model**: let the pump contribution to the main channel be the reference passed
   through an unknown $h$, with $M = 64$ taps covering the unknown travel path.
   Choose $\mu = 0.05$ for the normalised update.
3. **Cost**: one complex multiply-add per tap per sample. At 500 Hz, 10 channels
   and 64 taps, that is $500 \times 10 \times 64 = 3.2\times10^5$ operations per
   second — trivial on a modern CPU, and the reason adaptive filters are applied
   per-trace rather than per-section.
4. **Check the assumption**: if the reference also records the reflection (because
   it is not far enough away), the canceller will subtract part of it. Cross-check
   by comparing the output with a stacked section processed without the canceller;
   a systematic loss of coherent energy means the reference is contaminated.
5. **Order of operations**: run the canceller before stacking, per trace, because
   the interference path differs between traces. Stacking first would mix paths,
   and no single filter could remove the average.

## 6. Assumptions and regime of validity

1. **The reference is correlated with the interference and uncorrelated with the
   signal.** This is the load-bearing assumption (§3.3). It cannot be checked from
   the algorithm; it must be argued from the geometry.
2. **The interference path is linear and time-invariant over the adaptation
   window.** A path that changes faster than the filter converges cannot be
   tracked.
3. **The interference is stationary enough to average over.** The steady-state
   misadjustment depends on the statistics being stable.
4. **Enough samples to converge.** $M$ coefficients and a step $\mu$ need roughly
   $M/\mu$ samples to settle; a 4000-sample record with $M=128$ and $\mu=0.02$ is
   marginal, which is exactly the degradation measured in §4.2.
5. **The desired signal is not itself predictable from the reference.** A periodic
   signal in the primary *will* be predicted and removed; the line enhancer exploits
   this deliberately, and the canceller is destroyed by it accidentally.

## 7. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| step size | $\mu$ | dimensionless | NLMS bound $0<\mu<2$ |
| filter length | $M$ | taps | samples of memory |
| variance | $\sigma^2$ | (signal units)$^2$ | |
| SNR | — | dB | $10\log_{10}(\sigma_s^2/\sigma_v^2)$ |
| decorrelation delay | $\Delta$ | samples | |
| arithmetic | — | multiply-adds s$^{-1}$ | $f_s\,M\,N_{\text{chan}}$ |

The step size is dimensionless *only in the normalised form*. For plain LMS it
carries units of inverse power, which is exactly why NLMS is preferred in
practice: it removes one unit-dependent quantity from the analysis.

## 8. Python demonstration

`code/adaptive_filtering_demo.py` implements NLMS from scratch, sweeps the step
size and the filter length, runs an adaptive line enhancer, and prints a
convergence curve. It is self-contained, seeded with
`np.random.default_rng(20261014)`, and exits 0.

What to look for:

1. **section 1** — the $-12.46$ dB input SNR and the 9-sample interference path.
2. **section 2** — the improvement peaking at $\mu \approx 0.1$ and then falling.
3. **section 3** — the best length is 8, just above the path length.
4. **section 4** — the line enhancer improves the SNR by 12.67 dB using the
   filter *output*, not the error.
5. **section 5** — the two learning curves.

## 9. Exercises

Full sets with worked solutions are in
[`exercises/05-adaptive-filtering-exercises.md`](exercises/05-adaptive-filtering-exercises.md)
and
[`exercises/05-adaptive-filtering-solutions.md`](exercises/05-adaptive-filtering-solutions.md).

- **★** Write out the NLMS update for $M = 3$ and one sample, with numbers.
- **★★** Explain, using the measured step-size table, why the improvement is not
  monotonic in $\mu$.
- **★★** Predict what happens if the reference channel contains 10% of the desired
  signal, and design an experiment to detect it.
- **★★★** Derive the excess mean squared error of NLMS to first order in $\mu$ and
  compare it with the measured floor at $\mu = 0.05$ and $0.005$.

## Mastery checkpoint

Complete this without notes:

> A canceller has $M = 32$ taps, a reference channel whose variance is twice the
> interference variance at the primary sensor, and a path of 20 samples. **(a)**
> State the minimum $M$ that can in principle model the path and why more may be
> needed in practice. **(b)** State the NLMS convergence bound for $\mu$ and the
> value you would try first. **(c)** Explain what happens to the output if the
> reference contains 5% of the desired signal. **(d)** Explain whether a bigger
> $\mu$ would improve or degrade the steady-state SNR, and why. **(e)** State the
> one experiment you would run to test the reference-isolation assumption.

A worked version appears in the
[solutions](exercises/05-adaptive-filtering-solutions.md).

## Common pitfalls

1. **Taking the error as the output of a line enhancer.** The enhanced signal is
   $y$; the error $e$ is the noise. The reverse is true for a canceller.
2. **Leaking signal into the reference.** Any signal component in the reference is
   subtracted from the output; this is the failure mode that has no software fix.
3. **Using the largest step that is still stable.** $\mu = 1.0$ is stable and
   4.3 dB worse than $\mu = 0.1$ in the demo.
4. **Choosing $M$ from intuition rather than from the path length.** The demo
   peaks at $M = 8$ and degrades sixfold by $M = 128$.
5. **Forgetting to divide by the input power.** Plain LMS with a fixed step will
   behave completely differently on a record with different amplitude scaling.

## Related modules

- [20-05-04 Noise Reduction Strategies in Practice](../05-noise-and-random-signals/04-noise-reduction.md) —
  where adaptive filtering fits among the alternatives.
- [20-03-04 Phase Response, Zero-Phase Filtering and Distortion](04-phase-and-zero-phase.md) —
  the phase behaviour an adaptive filter does *not* have (it is time-varying, so
  the phase is not even well defined in the usual sense).
- [20-03-06 Multichannel and Array Filtering (f-k, Radon)](06-multichannel-filtering.md) —
  the array-domain alternative to a single-channel canceller.
- [01-14-04 Linear and Nonlinear Least Squares](../../01-mathematics/14-optimization/04-least-squares.md) —
  the optimisation view of the same normal equations.
