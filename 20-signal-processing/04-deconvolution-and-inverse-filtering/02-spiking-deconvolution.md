---
id: 20-04-02
title: "Spiking (Predictive) Deconvolution and Wavelet Estimation"
level: research
prereqs: ["20-04-01", "20-03-01"]
tags: [signal-processing, deconvolution, spiking-deconvolution, predictive-deconvolution, levinson, minimum-phase, wavelet-estimation, kurtosis]
---

# Spiking (Predictive) Deconvolution and Wavelet Estimation

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the prediction-error filter from the Yule-Walker normal equations and
   **solve** them with the Levinson recursion.
2. **Explain** why a minimum-phase wavelet is required for a causal spiking
   operator to exist, and **demonstrate** the failure with a zero-phase wavelet.
3. **Estimate** a wavelet from the trace autocorrelation by spectral factorisation.
4. **Measure** the spikiness gain of a spiking operator with a kurtosis metric and
   **check** the result against a known reflectivity.
5. **Choose** an operator length relative to the wavelet, and **explain** why extra
   coefficients degrade the result.
6. **Configure** predictive deconvolution with a prediction gap and **show** that a
   wrong gap does not suppress the multiple.

## Prerequisites

- [20-04-01 Deconvolution: Concept, Ill-Posedness and Stabilisation](01-deconvolution-concept.md) —
  the convolutional model and the stability problem.
- [20-03-01 FIR Filter Design: Windows, Parks-McClellan, Least Squares](../03-digital-filtering/01-fir-filters.md) —
  the operator design view of the same filter.

## 1. Intuition: invert the statistics, not the wavelet

The previous lesson assumed the wavelet was known. In practice it is not, and one
of the most useful facts in seismic processing is that **you do not always need
it**. If the reflectivity is white — uncorrelated from one sample to the next —
then the autocorrelation of the trace is the autocorrelation of the wavelet times
a constant:

$$r_{dd}[m] = (w * w)[m]\,\sigma_r^2 \quad\text{(reflectivity white).}$$

The trace's second-order statistics therefore carry the wavelet's *amplitude*
information, and a filter built from them can whiten the trace without ever
naming $w$. The result is a trace whose autocorrelation is a spike, hence
**spiking deconvolution**.

The catch is phase. Amplitude information does not determine a wavelet; infinitely
many wavelets share an amplitude spectrum. To build a causal, stable inverse we
must choose the one whose inverse is also causal and stable: the **minimum-phase**
wavelet. This lesson states that assumption explicitly and measures what happens
when it fails.

All models and data in this module are SYNTHETIC. The wavelet is the impulse
response of a chosen two-pole resonator, not an estimated field wavelet.

## 2. Definitions

### 2.1 Prediction and the prediction-error filter

Given a stationary process $x[n]$, the **forward prediction** of $x[n]$ from its
past is $\hat x[n] = \sum_{k=1}^{p} a_k x[n-k]$. The **prediction error** is
$e[n] = x[n] - \hat x[n]$, and the filter that produces it is

$$a(z) = 1 - \sum_{k=1}^{p} a_k z^{-k}, \qquad e = a * x.$$

Minimising $\mathbb{E}[e^2]$ over $a_k$ gives the **Yule-Walker** normal equations

$$\sum_{k=1}^{p} a_k\, r_{xx}[j-k] = r_{xx}[j], \qquad j = 1,\dots,p,$$

whose solution for a large $p$ whitens $x$. The minimum-phase condition on $a(z)$
(all zeros inside the unit circle) is what makes the operator stable.

### 2.2 Spikiness

The demo measures spikiness with the **kurtosis**

$$\mathrm{kurt}(x) = \frac{\mathbb{E}\left[(x-\bar x)^4\right]}
{\left(\mathbb{E}\left[(x-\bar x)^2\right]\right)^2},$$

which is 3 for a Gaussian and much larger for a sparse spike train. The
synthetic reflectivity has $\mathrm{kurt} = 66.1$, the wavelet-convolved trace has
$\mathrm{kurt} = 11.6$, and the noise has 2.90. A successful spiking operator must
move the trace's kurtosis *towards* the reflectivity's.

### 2.3 Predictive deconvolution

Instead of predicting one sample ahead, predict $\alpha$ samples ahead. The
**prediction gap** $\alpha$ is the design parameter: any periodicity of period
$\alpha$ (a multiple) is predicted and therefore removed by the prediction-error
filter. The operator is

$$f = \left[1,\ \underbrace{0,\dots,0}_{\alpha-1},\ -g_0,\dots,-g_{p-1}\right],$$

where $g$ solves the $\alpha$-step Yule-Walker equations
$R_{xx}g = r_{xx}[\alpha:\alpha+p]$.

## 3. Derivations

### 3.1 The Levinson recursion

The Yule-Walker system is Toeplitz and symmetric, so it can be solved in
$O(p^2)$ rather than $O(p^3)$ by the Levinson-Durbin recursion. With
$a^{(i)}$ the order-$i$ solution and $E_i$ the order-$i$ prediction error power:

$$k_i = -\frac{r[i] + \sum_{j=1}^{i-1} a_j^{(i-1)} r[i-j]}{E_{i-1}},
\quad
a_j^{(i)} = a_j^{(i-1)} + k_i a_{i-j}^{(i-1)},\quad
E_i = E_{i-1}(1-k_i^2).$$

The demo implements this in ten lines. Applied to the synthetic trace's
autocorrelation (the first seven normalised lags are $1.0000$, $0.8358$, $0.4591$,
$0.0262$, $-0.4987$ at lag 5, $0.2324$ at lag 10) it returns, at order 2,

$$a = [1.0000,\ -1.5000,\ 0.7946],$$

against the wavelet's exact two-tap inverse

$$a_{\text{true}} = [1.0000,\ -1.4860,\ 0.7744].$$

The order-2 estimate recovers the wavelet's inverse to two decimal places from the
**trace autocorrelation alone**. That is the mechanism of spiking deconvolution:
the second-order statistics of the trace are, up to a scale, the second-order
statistics of the wavelet.

### 3.2 The measured spikiness gain

| operator length | kurtosis | correlation with true reflectivity |
|---|---|---|
| trace (none) | 11.6 | +0.3407 |
| 2 | **63.7** | **+0.9924** |
| 5 | 63.7 | +0.9921 |
| 10 | 63.7 | +0.9908 |
| 20 | 63.6 | +0.9881 |
| 40 | 62.4 | +0.9775 |
| 80 | 60.4 | +0.9597 |

The order-2 operator already lifts the kurtosis from 11.6 to 63.7 — within 2.5% of
the reflectivity's 66.1 — and correlates with the true reflectivity at 0.9924. The
order-2 operator suffices because the wavelet is exactly a two-pole system: its
inverse is two taps long. **The correct operator length is the length of the
wavelet, not the length of the trace.**

### 3.3 Why minimum phase is essential

The demonstration in §3.2 works because the teaching wavelet is the impulse
response of a causal, stable AR(2) system — hence minimum phase, hence invertible
by a causal stable filter. If instead the wavelet is zero-phase (a symmetric
Ricker, say), its inverse is symmetric about zero, i.e. non-causal, and no causal
FIR operator can realise it. The autocorrelation-derived predictor then does
something else: it finds the *minimum-energy* filter that suppresses the trace
rather than inverting it, and the recovered trace is a phase-distorted,
inverted-looking version of the reflectivity with a correlation near zero. In
practice spiking deconvolution assumes the wavelet is minimum phase, and the
evidence that it works — the measured correlation — is the *test* of that
assumption, not a consequence of it.

### 3.4 Predictive deconvolution and multiples

Set the prediction gap to the multiple period and the operator predicts the
periodic part, which the prediction error then subtracts. The demo builds a trace
with multiples at 1, 2 and 3 periods (amplitudes 0.5, 0.25, 0.125 of the primary)
and measures the normalised autocorrelation at the period lags:

| prediction gap | $\rho_1$ | $\rho_2$ | $\rho_3$ |
|---|---|---|---|
| input | $+0.4613$ | $+0.1173$ | $-0.0522$ |
| 50 ms (half period) | $+0.3896$ | $+0.0970$ | $-0.0262$ |
| **100 ms (= period)** | **$+0.0436$** | $-0.0259$ | $-0.0213$ |
| 200 ms (2 × period) | $+0.3975$ | $+0.0202$ | $-0.0511$ |

Only the gap that equals the period suppresses the periodicity: the correlation at
one period falls from 0.4613 to 0.0436, a factor of 10.6, while the wrong gaps
leave 0.39–0.40. **The gap is the multiple model**, and it must be measured from
the data (from the autocorrelation), not guessed. This also explains why predictive
deconvolution works on water-bottom and peg-leg multiples, whose periods are
roughly constant, but not on aperiodic interbed multiples.

## 4. Worked example (SYNTHETIC)

A marine record has a reverberation with a measured period of 120 ms and a
wavelet of about 80 ms effective length.

1. **Estimate the period** from the trace autocorrelation: look for a secondary
   maximum. Suppose the demo's autocorrelation shows a peak at 120 ms with
   $\rho = 0.4$.
2. **Set the prediction gap** $\alpha = 120$ ms. This must exceed the wavelet
   length, otherwise the operator partly predicts the wavelet itself rather than
   the periodicity. Here 120 ms > 80 ms, so the choice is valid.
3. **Choose the operator length** $p$: long enough to whiten the wavelet (about
   40 ms of coefficients, i.e. $p \approx 40$ at 1 ms sampling), shorter than the
   gap so the filter remains a genuine predictor.
4. **Predict the effect**: the multiple's autocorrelation contribution at the
   gap should fall by roughly an order of magnitude (0.46 to 0.04 in the demo).
5. **Follow with spiking deconvolution** to shorten the wavelet, since predictive
   deconvolution removes the multiples but does not spike.

The order matters: predictive deconvolution (multiple removal) is usually applied
*before* spiking deconvolution (wavelet shortening), because multiples are easier
to measure in a longer wavelet and the spiking step would otherwise redistribute
the multiple energy.

## 5. Assumptions and regime of validity

1. **The reflectivity is white.** This is what makes the trace autocorrelation a
   scaled wavelet autocorrelation. Real reflectivity is nearly white over short
   windows and organised over long ones (a strong reflector dominates the
   autocorrelation), which is why operators are designed on windows.
2. **The wavelet is minimum phase.** §3.3. A mixed-phase or zero-phase wavelet
   breaks the method, and there is no way to fix it from the autocorrelation alone,
   because the autocorrelation carries no phase information.
3. **The wavelet is stationary within the design window.** A wavelet that changes
   with time needs a time-varying operator.
4. **The noise is white or the operator is kept short.** The demo's noise gain is
   ~2 for every length tested (1.95 to 2.09), because the wavelet is short; with a
   longer wavelet the gain grows and the operator must be truncated to the wavelet
   length.
5. **The multiple period is constant.** Predictive deconvolution needs a period to
   predict. A dipping or aperiodic multiple train is not a stationary periodicity
   and the method underperforms — see the f-k and Radon approaches in
   [20-03-06](../03-digital-filtering/06-multichannel-filtering.md).

## 6. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| operator length | $p$ | samples | |
| prediction gap | $\alpha$ | samples | $\ge$ wavelet length |
| autocorrelation | $r[m]$ | (amplitude)$^2$ | $r[0]$ is the variance |
| kurtosis | — | dimensionless | 3 for Gaussian |
| multiple period | — | s | converted to samples via $\Delta t$ |

The gap is a time that must be converted to samples: a 120 ms period at 2 ms
sampling is 60 samples, not 120. Getting this wrong makes the operator predict the
wrong lag, and the failure looks like "predictive deconvolution did not work"
rather than "the units were wrong".

## 7. Python demonstration

`code/spiking_deconvolution_demo.py` generates the trace, computes the
autocorrelation, runs the Levinson recursion, measures the kurtosis and
correlation gain versus operator length, tests the noise gain, and demonstrates
predictive deconvolution with the correct and incorrect gaps. It is
self-contained, seeded with `np.random.default_rng(20261014)`, and exits 0.

What to look for:

1. **section 2** — the order-2 PEF recovering the wavelet inverse.
2. **section 3** — kurtosis 11.6 → 63.7 and correlation 0.9924.
3. **section 4** — the noise gain stays near 2 while kurtosis and correlation
   degrade for long operators.
4. **section 5** — the correlation at one period falling from 0.4613 to 0.0436
   only when the gap equals the period.

## 8. Exercises

Full sets with worked solutions are in
[`exercises/02-spiking-deconvolution-exercises.md`](exercises/02-spiking-deconvolution-exercises.md)
and
[`exercises/02-spiking-deconvolution-solutions.md`](exercises/02-spiking-deconvolution-solutions.md).

- **★** Write the order-2 Yule-Walker equations for a given autocorrelation and
  solve them by hand.
- **★★** From the kurtosis table, choose an operator length for a wavelet whose
  exact length is 30 samples and justify it.
- **★★** Explain why a zero-phase wavelet cannot be spiked by a causal operator,
  using the symmetry of the inverse.
- **★★★** Design a predictive deconvolution for a reverberation whose period
  varies by $\pm$10%, and state two ways the operator can be made robust.

## Mastery checkpoint

Complete this without notes:

> A trace has autocorrelation lags $r[0] = 4.00$, $r[1] = 2.80$, $r[2] = 1.20$.
> **(a)** Solve the order-2 Yule-Walker equations for $a_1, a_2$. **(b)** State
> whether the resulting operator is minimum phase, and how you checked. **(c)**
> State the kurtosis you would expect after spiking if the reflectivity is a
> sparse spike train, and why. **(d)** Explain what changes if the wavelet is
> zero-phase. **(e)** State the one measurement that tests whether the
> minimum-phase assumption was valid.

A worked version appears in the
[solutions](exercises/02-spiking-deconvolution-solutions.md).

## Common pitfalls

1. **Assuming the wavelet is minimum phase because the method assumes it.** Test
   the assumption (against a known reflectivity in a synthetic, or against a
   well-log tie in the field).
2. **Using an operator far longer than the wavelet.** Kurtosis and correlation
   both degrade (63.7 → 60.4 and 0.9924 → 0.9597 by length 80).
3. **Setting the prediction gap to the wavelet length or shorter.** The operator
   then predicts the wavelet, not the multiple.
4. **Confusing the units of the gap.** Convert period in seconds to samples.
5. **Judging success by the spikier appearance of the section.** A spikier
   section can be an over-whitened, noisier section. Check against something
   independent.

## Related modules

- [20-04-01 Deconvolution: Concept, Ill-Posedness and Stabilisation](01-deconvolution-concept.md) —
  the stabilisation this method avoids by staying statistical.
- [20-04-03 Wiener Filtering and Least-Squares Inverse Filters](03-wiener-filtering.md) —
  the supervised form, where the desired output is supplied.
- [20-04-04 Deconvolution in the Presence of Noise](04-deconvolution-noise.md) —
  what limits the spikiness gain.
- [20-03-06 Multichannel and Array Filtering (f-k, Radon)](../03-digital-filtering/06-multichannel-filtering.md) —
  the alternative to predictive deconvolution for multiples.
- [06-09-06 Multiple Elimination](../../06-seismology/09-reflection-seismology/06-multiple-elimination.md) —
  the processing-context view of the same problem.
- [18-03-04 L1 Regularisation, Sparsity and Compressive Sensing](../../18-inverse-problems/03-regularization/04-sparsity.md) —
  the modern route to spikiness that does not assume minimum phase.
