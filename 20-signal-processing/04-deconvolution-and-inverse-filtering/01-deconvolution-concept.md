---
id: 20-04-01
title: "Deconvolution: Concept, Ill-Posedness and Stabilisation"
level: doctoral
prereqs: ["20-01-03", "20-03-01", "18-03-02"]
tags: [signal-processing, deconvolution, inverse-problems, tikhonov, water-level, ill-posed, regularisation, conditioning]
---

# Deconvolution: Concept, Ill-Posedness and Stabilisation

## Learning objectives

By the end of this lesson you will be able to:

1. **Write** the convolutional model and **derive** the frequency-domain inverse
   filter from it.
2. **Show** that the convolution operator is ill-conditioned, and **compute** its
   condition number both numerically and over the wavelet's usable band.
3. **Derive** the damped (water-level, Tikhonov) inverse from a least-squares
   problem with a penalty term.
4. **Measure** the three-way trade of resolution, noise gain and forward-model
   bias, and **state** which quantity each curve represents.
5. **Explain** why the optimal damping equals the noise-to-signal power ratio, and
   **verify** it numerically.
6. **Distinguish** the intrinsic band-limit bias from the regularisation bias.

## Prerequisites

- [20-01-03 Convolution, Correlation and Filtering](../01-signals-and-systems/03-convolution-and-filters.md) —
  the convolution sum and the convolution theorem.
- [20-03-01 FIR Filter Design: Windows, Parks-McClellan, Least Squares](../03-digital-filtering/01-fir-filters.md) —
  the least-squares design machinery reused here.
- [18-03-02 Tikhonov Regularisation and the Smoothing Trade-Off](../../18-inverse-problems/03-regularization/02-tikhonov.md) —
  the systematic treatment of the same idea.

## 1. Intuition: division where the divisor vanishes

Deconvolution is the inverse of convolution. A layered Earth convolved the
reflectivity series with a source wavelet; deconvolution tries to undo that
convolution and recover the reflectivity. If the wavelet spectrum $W(f)$ were
bounded away from zero, the inversion would be a division: $R = D/W$. It is not.
A wavelet is band-limited — the Ricker used here has usable energy from 1 to
143.6 Hz and essentially none outside — so $W(f)$ approaches zero at the band
edges and in the gaps. Dividing by a number near zero turns a small amount of
noise into an enormous amount of answer.

This is the whole content of the word *ill-posed*: the answer exists, is unique in
exact arithmetic, and is nonetheless useless because the smallest perturbation of
the data produces a large change in the solution. Everything else in this module
is about how to make it useful again, and at what cost.

All models and data in this module are SYNTHETIC. The wavelet, the reflectivity
and the noise are generated here; no field record is used.

## 2. Definitions

### 2.1 The convolutional model

$$d[n] = (w * r)[n] + e[n]
= \sum_k w[k]\,r[n-k] + e[n],$$

or in the frequency domain

$$D(f) = W(f)\,R(f) + E(f),$$

with $d$ the trace, $w$ the wavelet, $r$ the reflectivity, $e$ the noise. The
**deconvolution problem** is: given $d$ and an assumed $w$, estimate $r$.

### 2.2 Conditioning

For the linear operator $\mathbf{W}$ defined by convolution with $w$, the condition
number is $\kappa = \sigma_{\max}/\sigma_{\min}$ with $\sigma$ the singular values.
Equivalently, in the Fourier basis, $\kappa = \max|W|/\min|W|$ over the sampled
frequencies, and the **noise amplification** of the naive inverse is
$1/\min|W|$.

### 2.3 Tikhonov / water-level inversion

$$R_{\varepsilon}(f) = \frac{D(f)\,W^{*}(f)}{\left|W(f)\right|^2 +
\varepsilon\max_f\left|W(f)\right|^2}.$$

$\varepsilon$ is the **water level** (or damping). It is the single knob of the
method, and §5 shows it is not free.

## 3. Derivations

### 3.1 The inverse filter, and its condition number

Ignoring noise, $R = D/W$. Because $W$ has a null space, the operator is
rank-deficient: the demo's $512\times512$ convolution matrix has largest singular
value $4.6111$ and smallest $1.2511\times10^{-36}$ — a **numerical condition number
of $3.686\times10^{36}$**. That number is partly a statement about floating point
(the smallest singular value is at the level of accumulated round-off) but the
ordering is real: the singular values decay smoothly from $4.6111$ at index 0
through $4.1244$ at index 40, $9.356\times10^{-1}$ at index 150, and
$1.424\times10^{-3}$ at index 300.

The **usable-band condition number** is the honest figure. Restricting to bins
where $|W| > 10^{-3}\max|W|$ (1.0 to 143.6 Hz, 147 of 257 bins) gives

$$\kappa_{\text{usable}} = \frac{\max|W|}{\min|W|}\bigg|_{\text{band}} = 950.2.$$

**Even inside the band the operator amplifies noise by a factor near $10^3$.** That
is the number that sets how much stabilisation is needed.

### 3.2 What the naive inverse does to noise

Substituting the model into the inverse: $R_{\text{est}} = R + E/W$. The error
is $E/W$, amplified pointwise by $1/|W|$. The demo measures this directly:

| input SNR (dB) | error vs band-limited target | noise amplification |
|---|---|---|
| 60 | $6.5\times10^{11}$ | $3.083\times10^{14}$ ($289.8$ dB) |
| 40 | $5.8\times10^{12}$ | $2.774\times10^{14}$ ($288.9$ dB) |
| 20 | $1.4\times10^{13}$ | $6.486\times10^{13}$ ($276.2$ dB) |

The amplification is enormous and, crucially, **almost independent of the noise
level**: improving the input SNR from 20 to 60 dB changes the output error by
less than two orders of magnitude out of thirteen. The naive inverse is limited by
the smallest $|W|$, not by the noise.

### 3.3 Damped inversion as regularised least squares

Minimise the misfit plus a penalty on the solution energy:

$$\min_{r}\ \left\|\mathbf{W}r - d\right\|^2 + \varepsilon\left\|r\right\|^2.$$

Setting the gradient to zero gives $(\mathbf{W}^{\top}\mathbf{W} +
\varepsilon\mathbf{I})r = \mathbf{W}^{\top}d$; in the Fourier basis this is exactly
the water-level formula of §2.3, because $\mathbf{W}^{\top}\mathbf{W}$ is
multiplication by $|W|^2$. So the water level is a **Tikhonov regulariser**, and
$\varepsilon$ is its weight. The interpretation is a Bayesian one: $\varepsilon$ is
the ratio of the noise variance to the prior variance of the reflectivity — the
noise-to-signal ratio.

### 3.4 Two kinds of bias

There are two reasons a damped deconvolution is not the true reflectivity:

- **Band-limit bias** (intrinsic): content outside the wavelet's band cannot be
  recovered by any linear method. The demo's band-limited target satisfies
  $\|r_{\text{ideal}} - r\|/\|r\| = 0.501$ — half the reflectivity's energy is
  simply not in the data.
- **Regularisation bias** (chosen): the penalty term systematically shrinks and
  smooths the solution. It shows up as a growing forward-model residual, which is
  measured in §4.

Separating them matters: the first cannot be reduced, only reported; the second is
the price of stability and should be chosen against the noise.

## 4. The measured trade-off

With a synthetic reflectivity, the true wavelet, and noise giving a 30 dB record
SNR:

| water level | rel. error | noise gain (dB) | forward residual (%) | pulse width (ms) |
|---|---|---|---|---|
| $10^{-10}$ | 167.63 | 68.0 | 1.82 | 44.00 |
| $10^{-8}$ | 12.746 | 45.7 | 1.95 | 40.00 |
| $10^{-6}$ | 1.584 | 27.2 | 2.05 | 32.00 |
| $10^{-5}$ | 0.821 | 19.0 | 2.11 | 24.00 |
| $10^{-4}$ | 0.638 | 10.7 | 2.21 | 24.00 |
| $10^{-3}$ | **0.635** | 1.2 | 2.65 | 12.00 |
| $10^{-2}$ | 0.691 | $-6.9$ | 5.50 | 12.00 |
| $10^{-1}$ | 0.769 | $-15.7$ | 19.82 | 12.00 |

Read the columns together, not separately:

- **noise gain** falls monotonically with $\varepsilon$: $-15.7$ dB at the largest
  level means the noise is attenuated below its input level;
- **pulse width** falls monotonically: the recovered reflectivity gets *sharper*
  as damping increases, because the regulariser suppresses the noisy sidelobes
  that would otherwise lengthen the apparent pulse;
- **forward residual** rises monotonically — 1.82% to 19.82% — and **this is the
  regularisation bias**, the price paid in data-misfit for the stability;
- **relative error** has a clear minimum, $0.635$ at $\varepsilon = 10^{-3}$:
  too little damping is dominated by noise, too much by bias.

That is the resolution / noise / bias trade in one table, and the error column
shows the trade has an interior optimum. Note also that the width column does not
behave the naive way: after regularisation, the dominant effect on the apparent
pulse is *noise sidelobes*, so suppressing them *sharpens* the estimate until the
regulariser's own smoothing takes over.

## 5. Choosing the water level from the noise

The optimum is not found by taste. The demo scans $\varepsilon$ for five noise
levels and compares the best $\varepsilon$ with the noise-to-signal power ratio:

| NSR | best $\varepsilon$ | ratio $\varepsilon/\text{NSR}$ |
|---|---|---|
| $1.00\times10^{-1}$ | $2.371\times10^{-2}$ | 0.2 |
| $1.00\times10^{-2}$ | $1.778\times10^{-3}$ | 0.2 |
| $1.00\times10^{-3}$ | $2.371\times10^{-4}$ | 0.2 |
| $1.003\times10^{-4}$ | $1.334\times10^{-5}$ | 0.1 |
| $1.002\times10^{-5}$ | $2.371\times10^{-6}$ | 0.2 |

Over five orders of magnitude in noise, the optimal damping is a **constant factor
0.1–0.2 times the noise-to-signal power ratio**. The water level is a noise model,
measured from the data, not an aesthetic choice. In practice the NSR is estimated
from a noise window (a quiet part of the record or a pre-first-break segment) and
the factor is calibrated once on synthetic data for the wavelet at hand.

## 6. Worked example (SYNTHETIC)

A reflection survey has a 45 Hz Ricker wavelet, a 2 ms sample interval, and a
noise window whose variance is $10^{-3}$ of the signal window's.

1. **Estimate the NSR**: $10^{-3}$.
2. **Set the water level**: $\varepsilon \approx 0.2 \times 10^{-3} = 2\times10^{-4}$.
3. **Predict the outcome** from the table of §4 (interpolating between
   $10^{-4}$ and $10^{-3}$): relative error near $0.64$, noise gain near $+6$ dB,
   forward residual near 2.4%, recovered pulse width near 20 ms.
4. **State the resolution**: 20 ms is the half-width of the recovered pulse; two
   reflectors 15 ms apart will merge, and no choice of $\varepsilon$ will separate
   them, because the *wavelet's* own width sets that limit.
5. **Sanity check**: convolve the recovered reflectivity with the wavelet and
   compare with the input. A residual near 2.4% is the expected regularisation
   bias; a residual near 20% means $\varepsilon$ is too large, and a residual of a
   few per cent with a wildly oscillating answer means it is too small for the
   noise actually present.

Step 5 is the practical discipline: the forward residual is computable without
knowing the answer, so it is the diagnostic you actually have.

## 7. Assumptions and regime of validity

1. **The wavelet is known and stationary.** If $w$ is wrong, the inversion removes
   the wrong thing; if $w$ changes with time, one filter cannot be right
   everywhere. Wavelet estimation is the subject of
   [02](02-spiking-deconvolution.md).
2. **The model is convolutional.** Multiples, attenuation and mode conversions are
   not convolution with a single wavelet, and their presence violates the model
   more seriously than noise does.
3. **Noise is additive and white (or its spectrum is known).** The NSR rule uses
   the noise power; coloured noise requires the same rule per frequency.
4. **The reflectivity is stationary in the analysis window.** With a random
   reflectivity the statistics are stable; with a strong isolated reflector the
   autocorrelation is dominated by that event.
5. **The linear operator is the right one.** Production deconvolution uses
   finite-length operators (see [03](03-wiener-filtering.md)), which adds a
   length truncation to the regularisation.
6. **Floating point is adequate for the *stabilised* problem.** It is not adequate
   for the undamped one: the demo's condition number $3.7\times10^{36}$ exceeds
   double precision's $10^{16}$ range.

## 8. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| trace, wavelet, reflectivity | $d,w,r$ | dimensionless (scaled) | |
| frequency | $f$ | Hz | |
| water level | $\varepsilon$ | dimensionless | ratio of powers |
| noise gain | — | dB | $20\log_{10}$(ratio) |
| forward residual | — | % | $\|Wr-d\|/\|d\|$ |
| pulse width | — | s | from the envelope |

The water level is dimensionless precisely because it is a ratio of powers; a
dimensional constant added to $|W|^2$ would already be a noise model written down
explicitly. The forward residual is a dimensionless ratio of norms, but is quoted
in per cent because that is how it is judged.

## 9. Python demonstration

`code/deconvolution_concept_demo.py` builds the model, computes the singular-value
spectrum and both condition numbers, measures the naive inverse's amplification,
sweeps the water level, and recovers the NSR rule. It is self-contained, seeded
with `np.random.default_rng(20261014)`, and exits 0.

What to look for:

1. **section 2** — numerical condition number $3.7\times10^{36}$ against
   usable-band $950.2$.
2. **section 3** — the $10^{14}$ noise amplification that barely improves with SNR.
3. **section 4** — the four columns that move in different directions.
4. **section 5** — the ratio $\varepsilon/\text{NSR}$ staying near 0.2 across five
   decades of noise.

## 10. Exercises

Full sets with worked solutions are in
[`exercises/01-deconvolution-concept-exercises.md`](exercises/01-deconvolution-concept-exercises.md)
and
[`exercises/01-deconvolution-concept-solutions.md`](exercises/01-deconvolution-concept-solutions.md).

- **★** Write the water-level formula and identify each symbol, with units.
- **★★** From the table of §4, choose a water level for a survey that must resolve
  a 25 ms pulse with the noise gain below $+12$ dB, and justify it.
- **★★** Compute the noise amplification of the naive inverse for a wavelet whose
  usable-band condition number is 500, and compare with the demo's $950.2$.
- **★★★** Derive the optimal $\varepsilon$ for a scalar (single-frequency) problem
  and show it equals the noise-to-signal power ratio, then explain why the
  measured factor is 0.2 rather than 1.

## Mastery checkpoint

Complete this without notes:

> A trace has a known wavelet with usable band 5–80 Hz and a noise-to-signal
> power ratio of $4\times10^{-3}$. **(a)** Explain in one sentence why
> deconvolution is ill-posed, in terms of the wavelet. **(b)** Compute a water
> level and state the rule you used. **(c)** State whether the recovered
> reflectivity can contain energy at 2 Hz, and why. **(d)** State the two biases
> that limit the answer and which one is removable. **(e)** A colleague sets the
> water level to $10^{-8}$ and shows a much spikier result. Explain what they have
> actually displayed.

A worked version appears in the
[solutions](exercises/01-deconvolution-concept-solutions.md).

## Common pitfalls

1. **Reporting a spikier result as a better result.** A tiny water level sharpens
   the noise as well as the signal; the demo's error at $10^{-10}$ is 167.
2. **Confusing the numerical condition number with the physical one.** Quote the
   usable-band figure and say so.
3. **Treating the water level as a tuning knob to be optimised on the output.**
   It is a noise model; estimate the noise and set it.
4. **Hoping for resolution the wavelet does not have.** Band-limit bias is not
   reducible by any linear method.
5. **Forgetting to whiten.** A first-arrival or ground-roll transient makes the
   record non-stationary; deconvolving without handling it spreads the transient
   across the whole trace.

## Related modules

- [20-04-02 Spiking (Predictive) Deconvolution and Wavelet Estimation](02-spiking-deconvolution.md) —
  the statistical route that needs no known wavelet.
- [20-04-03 Wiener Filtering and Least-Squares Inverse Filters](03-wiener-filtering.md) —
  the finite-length formulation of the same problem.
- [20-04-04 Deconvolution in the Presence of Noise](04-deconvolution-noise.md) —
  the noise-resolved version of this lesson.
- [20-03-04 Phase Response, Zero-Phase Filtering and Distortion](../03-digital-filtering/04-phase-and-zero-phase.md) —
  why the wavelet's phase, not just its magnitude, decides whether a causal
  inverse exists.
- [06-08-01 Receiver Functions: Deconvolution and Ps Conversions](../../06-seismology/08-receiver-functions-and-crustal-structure/01-receiver-function-principle.md) —
  water-level deconvolution in a crustal setting.
- [06-09-02 Reflection Processing Flow: Deconvolution, NMO, Stack, Migration](../../06-seismology/09-reflection-seismology/02-processing-flow.md) —
  where deconvolution sits in the processing sequence.
- [18-03-02 Tikhonov Regularisation and the Smoothing Trade-Off](../../18-inverse-problems/03-regularization/02-tikhonov.md) —
  the general theory.
