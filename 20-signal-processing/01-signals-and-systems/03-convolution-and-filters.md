---
id: 20-01-03
title: "Convolution, Correlation and Filtering"
level: advanced
prereqs: ["20-01-02", "01-10-03", "06-09-02"]
tags: [signal-processing, convolution, correlation, matched-filter, filtering, fft]
---

# Convolution, Correlation and Filtering

Convolution is the operation that makes LTI systems computable; correlation is
its mirror image and the operation that makes *detection* computable. They differ
by one sign reversal and by one physical intention: convolution asks "what does
this system do to this signal", correlation asks "where in this record does this
shape occur". Almost every geophysical processing chain alternates between them —
a filter is convolution, a pick or a time-shift estimate is correlation — and
almost every implementation bug in such a chain is a bookkeeping error in the
output length, the zero-padding, or the time origin.

**All models and data in this module are SYNTHETIC.** The traces used below are
generated inside `code/convolution_and_filters_demo.py`; no recording is read.

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** a convolution three ways — by definition, with a library call, and
   by FFT — and **explain** why the FFT version needs zero-padding to the length
   $N+M-1$.
2. **State and verify** the algebraic properties of convolution (commutativity,
   associativity, distributivity, the sum rule) and use them to combine systems.
3. **Derive** cross-correlation as convolution with a reversed signal, and
   **estimate** a time shift from a correlation peak with a stated uncertainty.
4. **Derive** the matched filter from the signal-to-noise criterion and
   **verify** the $\sqrt N$ gain law for a rectangular pulse.
5. **Distinguish** 'full', 'same' and 'valid' outputs, and **quantify** the
   wrap-around error that appears when a linear convolution is computed
   circularly.
6. **Derive** the transfer function of a moving average and of a first
   difference, including the exact null positions and the large-$M$ limit of the
   sidelobe level.

## Prerequisites

- [20-01-02 LTI Systems and Impulse Response](02-lti-systems.md) — the system
  view of convolution, and the impulse response.
- [01-10-03 Convolution, Filtering and the Convolution Theorem](../../01-mathematics/10-fourier-analysis/03-convolution.md) —
  convolution as multiplication in the transform domain.
- [06-09-02 Seismic Processing Flow](../../06-seismology/09-reflection-seismology/02-processing-flow.md) —
  where these operations sit in a real processing sequence.

## 1. Intuition: two operations, two questions

Hold a wavelet in one hand and a record in the other.

- **Convolution** slides the wavelet over the record *reversed*, multiplies,
  adds. It answers: what does an instrument with this impulse response output
  when this signal is its input?
- **Correlation** slides the wavelet over the record *unreversed*, multiplies,
  adds. It answers: at which delay does this shape appear in the record, and how
  strongly?

The reversed slide of convolution is what makes filtering smooth a signal: each
output sample is a weighted average of nearby input samples, and weights that are
all positive cannot sharpen anything. The unreversed slide of correlation is what
makes it find a feature: the sum is largest exactly when the template lines up
with the feature.

Both operations are implemented by the same library function with an array
reversal between them, and that is where mistakes live.

## 2. Precise definitions

### 2.1 Convolution

$$y[n] = (x * h)[n] = \sum_{k=-\infty}^{\infty} x[k]\,h[n-k]
= \sum_{k=-\infty}^{\infty} h[k]\,x[n-k].$$

For finite sequences of lengths $N$ and $M$, the support of $y$ is the sum of the
supports, so $y$ has length

$$L = N + M - 1 .$$

**Sum rule.** $\sum_n y[n] = \left(\sum_n x[n]\right)\left(\sum_n h[n]\right)$.
This is the cheapest one-line sanity check in all of signal processing, and the
demonstration verifies it: for the test pair the two sides give $1.500000$.

### 2.2 Cross-correlation, and the two conventions

$$r_{xy}[\ell] = \sum_{n} x[n]\,y[n+\ell]
\qquad\text{(sometimes written } \sum_n x[n]y[n-\ell]\text{)} .$$

The two sign conventions differ by a reflection, so *always state which one you
use* and check it against a known delay. In this module $r_{xy}[\ell]$ is largest
at $\ell = $ (position of the template in the record) $-$ (position of the
template origin). Detectability follows from Cauchy–Schwarz:

$$\lvert r_{xy}[\ell]\rvert \le \lVert x\rVert\,\lVert y\rVert,$$

with equality only for $x \propto y$ shifted. The demonstration's correlation
peak of $3.567618$ is correctly below the bound
$\lVert x\rVert\lVert y\rVert = 4.163274$.

### 2.3 Correlation is convolution with a reversal

Change variables in $r_{xy}$:

$$r_{xy}[\ell] = \sum_n x[n]\,y[n+\ell]
= \sum_m x[m-\ell]\,y[m] = (x^{\text{rev}} * y)[\ell],
\qquad x^{\text{rev}}[n] = x[-n].$$

The demonstration confirms this numerically to $0.000\times10^{0}$: the
cross-correlation array and the convolution with the reversed template are
bit-identical.

## 3. Derivation: the matched filter

Let the record be $x[n] = A\,s[n-n_0] + \nu[n]$ with $\nu$ white noise of variance
$\sigma^{2}$ and known shape $s$ of unit peak. Apply an LTI filter $h$ and read
the output at the correct lag:

$$\text{signal} = A\sum_k h[k]s[k], \qquad
\operatorname{Var}(\text{noise}) = \sigma^{2}\sum_k h^{2}[k].$$

The peak-to-rms ratio is therefore

$$\mathrm{SNR}(h) = \frac{A\sum_k h[k]s[k]}
{\sigma\sqrt{\sum_k h^{2}[k]}}
\le \frac{A\lVert s\rVert}{\sigma},$$

by Cauchy–Schwarz, with equality when $h \propto s^{\text{rev}}$. So the optimal
filter is the **time-reversed template**, and the best attainable peak-to-rms
ratio is

$$\mathrm{SNR}_{\max} = \frac{A\lVert s\rVert}{\sigma},
\qquad\text{gain over a single sample} = \frac{\lVert s\rVert}{\max\lvert s\rvert}.$$

For a rectangular pulse of $N$ unit samples, $\lVert s\rVert = \sqrt N$ and
$\max\lvert s\rvert = 1$, so the gain is exactly $\sqrt N$.

*Numerical check (SYNTHETIC, $200$ realisations, $\sigma = 1$).* The
demonstration measures $\mathrm E[y]/\mathrm{std}(y)$ at the true lag:

| $N$ | $\lVert s\rVert$ | measured gain | $\sqrt N$ |
|---|---|---|---|
| 16 | 4.000 | 3.980 | 4.000 |
| 64 | 8.000 | 8.378 | 8.000 |
| 256 | 16.000 | 15.627 | 16.000 |

The residual few per cent is the ensemble error of a ratio estimated from 200
realisations, not a violation of the law. For a Gaussian pulse of 61 samples the
shape-limited gain is $\lVert s\rVert/\max\lvert s\rvert = 2.9770$, against
$\sqrt{61} = 7.8102$ for a rectangle of the same length: **the filter cannot
create signal-to-noise that the pulse shape does not contain.** A short,
compact wavelet is easier to detect than a long, smooth one of the same energy.

### 3.1 Detection is not estimation

The value of the matched-filter output at a *known* lag has the $\sqrt N$
behaviour above. The *maximum over all lags* does not: with noise only, the
demonstration measures a mean maximum of $12.809$, i.e.
$3.202\,\sigma\sqrt{N}$ for $N = 16$ (spread $0.354$), roughly
$\sqrt{2\ln(\text{number of lags})}$ times the single-lag level. A threshold for
"did I detect something" must be set from the distribution of the maximum over
the searched window, not from the value you would expect at one chosen lag.
(This is the same multiple-comparison inflation that appears in
[21-01 Probability and Random Variables](../../21-statistics-bayesian-ml/README.md).)

## 4. Algebra, and what each property buys

| Property | Statement | Use |
|---|---|---|
| commutative | $x*h = h*x$ | choose the shorter sequence as the kernel |
| associative | $(x*h_1)*h_2 = x*(h_1*h_2)$ | collapse a cascade into one FIR |
| distributive | $x*(h_1+h_2) = x*h_1 + x*h_2$ | combine parallel paths |
| identity | $x*\delta = x$ | delays are convolutions |
| sum rule | $\sum(x*h) = (\sum x)(\sum h)$ | one-line correctness check |
| length | $L = N+M-1$ | buffer sizing; zero-padding |

All four algebraic properties are verified exactly by the demonstration (maximum
residual $0.000\times10^{0}$ for each).

### 4.1 Linear versus circular convolution

The DFT multiplies, so convolution can be done as
$y = \mathrm{IDFT}\{\mathrm{DFT}\{x\}\cdot\mathrm{DFT}\{h\}\}$. But the DFT
implements a **circular** convolution of the array length $N_{\text{FFT}}$: any
energy that runs off the end wraps around to the beginning. Zero-padding both
inputs to at least $N+M-1$ turns the circular product into the linear one. The
demonstration shows both sides of this:

- with padding to $N+M-1$, the FFT result matches the direct sum to
  $8.60\times10^{-16}$ (rounding);
- *without* padding, the difference array has rms $0.189213$ against a signal rms
  of $0.375891$ — **50.3 %** of the output's rms, and a maximum error of
  $0.943834$.

A wrap-around error of that size is not a numerical detail; it is a wrong
answer.

### 4.2 Output modes and the time origin

| mode | length | what happened |
|---|---|---|
| `full` | $N+M-1$ | the honest linear convolution, with transient at both ends |
| `same` | $N$ | the first and last $(M-1)/2$ samples were discarded |
| `valid` | $N-M+1$ | only samples where the kernel fully overlapped the input |

The demonstration confirms that `same` is exactly the central slice of `full`
and `valid` its interior (residual $0$ in both cases). The cost of `same` is not
just the discarded samples: the $ (M-1)/2$-sample delay of the causal filter is
*silently removed*, so a pulse injected at sample $60$ appears at sample $58$ in
a length-5 `same` output. For a $(M-1)/2$ delay of 2 samples at
$\Delta t = 0.002\ \mathrm{s}$ that is $4.000\ \mathrm{ms}$ of arrival time
either accounted for or lost.

## 5. Filters as convolutions

### 5.1 The moving average

$$h[n] = \frac1M\ \text{for } 0 \le n \le M-1,
\qquad
H(e^{i\omega}) = \frac{1}{M}e^{-i\omega(M-1)/2}
\frac{\sin(M\omega/2)}{\sin(\omega/2)} .$$

The nulls are exact: $H = 0$ whenever $M\omega/2$ is a non-zero multiple of
$\pi$, i.e. at

$$\omega = \frac{2\pi k}{M}, \quad k = 1, 2, \dots$$

*Numerical check.* For $M = 5$ the demonstration measures
$\lvert H\rvert = 8.33\times10^{-17}$ at $\omega = 2\pi/5 = 1.2566\ \mathrm{rad}$
and $6.21\times10^{-17}$ at $\omega = 2\pi\cdot2/5 = 2.5133\ \mathrm{rad}$:
zero to double precision. The DC gain is $1.000000$ and the gain at Nyquist is
exactly $1/M = 0.200000$ for odd $M$.

**The $-$13.26 dB sidelobe figure is a limit, not a constant.** Measuring the
highest sidelobe of the Dirichlet kernel gives

| $M$ | 5 | 9 | 21 | 65 | 257 |
|---|---|---|---|---|---|
| highest sidelobe (dB) | $-12.041$ | $-12.896$ | $-13.195$ | $-13.255$ | $-13.261$ |

Only for long windows does the familiar $-13.26\ \mathrm{dB}$ appear; with five
taps the first sidelobe is $-12.04\ \mathrm{dB}$. Quoting the asymptotic number
for a short filter overstates its stopband performance by about $1.2\
\mathrm{dB}$.

### 5.2 The first difference as a differentiator

With $\Delta t$ the sample interval,

$$h = \frac{1}{\Delta t}[1,\ -1], \qquad
\lvert H(e^{i\omega})\rvert = \frac{2}{\Delta t}\left\lvert\sin\frac{\omega}{2}\right\rvert
\;\xrightarrow[\omega \to 0]{}\; \frac{\omega}{\Delta t}.$$

The demonstration measures, at $\Delta t = 0.002\ \mathrm{s}$:

| $\omega$ (rad) | measured $\lvert H\rvert$ (per s) | exact $2\sin(\omega/2)/\Delta t$ | low-$\omega$ limit $\omega/\Delta t$ |
|---|---|---|---|
| 0.10 | 49.9792 | 49.9792 | 50.0000 |
| 0.50 | 247.4040 | 247.4040 | 250.0000 |
| 1.00 | 479.4255 | 479.4255 | 500.0000 |

so the difference operator behaves as a derivative only for
$\omega \ll 1\ \mathrm{rad}$; at the Nyquist frequency its gain saturates at
$2/\Delta t = 1000\ \mathrm{s^{-1}}$ instead of growing without limit. A
"derivative" filter applied to a broadband record is therefore a differentiator
in the passband and a mild amplifier near Nyquist — a fact that matters for
amplitude-versus-offset work, where the derivative is used to isolate gradients.

## 6. Units and dimensional analysis

| quantity | unit | check |
|---|---|---|
| $x$, $y$ | signal unit (m/s) | |
| $h$ | output unit per input unit | dimensionless if both are m/s |
| $\sum_n h[n]$ | output per input | the DC gain |
| $\lVert h\rVert$ | per input unit | matched filter scales with the template |
| $r_{xy}$ | (unit of $x$)×(unit of $y$) | not normalised; divide by $\lVert x\rVert\lVert y\rVert$ for a coefficient |
| $\Delta t\,h$ | dimensionless × signal | a difference is only a derivative after dividing by $\Delta t$ |

The last row is the most commonly dropped factor: $\lvert H\rvert$ for the
first difference above is quoted "per second" only because $h$ was built with
$1/\Delta t$; without it the operator is dimensionless and its output is a
difference, not a rate of change.

## 7. Worked examples

### Example 1 — boxcar convolution by hand

$h = [1,1,1,1]$ (length 4, so $\sum h = 4$):

$$h * h = [1, 2, 3, 4, 3, 2, 1], \qquad \sum = 16 = 4\times4 \ \checkmark,$$

length $4+4-1 = 7$. The demonstration reproduces this exactly (maximum
difference $0.000\times10^{0}$). This triangular pair is the discrete shadow of
the continuous statement "the convolution of two boxcars is a triangle", and it
is the reason a stack of two running means is smoother than one.

### Example 2 — a matched filter, by numbers

A synthetic trace of $1200$ samples has $\sigma = 1$ of white noise and a
rectangular pulse of $N = 64$ unit-amplitude samples at sample 500. Match with
$h[n] = 1$ for $0\le n\le63$:

- $\lVert s\rVert = \sqrt{64} = 8$, so the predicted gain is $8.000000$.
- Output at the true lag: $\mathrm E[y] = \lVert s\rVert^{2} = 64$, measured
  $64.288$ over 200 realisations.
- Output noise: $\sigma\lVert s\rVert = 8$, measured $\mathrm{std}(y) = 7.673$.
- Measured gain $= 64.288/7.673 = 8.378$ against the prediction $8.000$ — a
  $4.7\%$ ensemble fluctuation of a ratio of two estimated moments.

### Example 3 — where the moving-average nulls come from

At $\omega = 2\pi/M$,

$$H = \frac1M\sum_{n=0}^{M-1}e^{-i2\pi n/M}
= \frac1M\cdot\frac{1-e^{-i2\pi}}{1-e^{-i2\pi/M}} = 0,$$

because the $M$ roots of unity sum to zero for $M \ge 2$. For $M = 5$ the
predicted null is exact and the measurement returns $8.33\times10^{-17}$ — the
rounding of a sum that cancels. Practical consequence: a 5-point average removes
a sinusoid of period exactly 5 samples and its harmonics, which is the basis of
"comb" removal of a known periodic interference provided the period is an integer
number of samples. If it is not, the null is not exactly on the interference and
the attenuation is much less (see
[20-02-03](../02-fourier-and-spectral-analysis/03-windowing-advanced.md)).

### Example 4 — sizing the wrap-around error

Forty samples of unit-variance noise convolved with a 5-point boxcar, computed
circularly with $N_{\text{FFT}} = 40$ instead of $44$: the error has rms
$0.189213$ against an output rms of $0.375891$ ($50.3\%$), and a maximum of
$0.943834$. The wrap-around is not confined to the last few samples; because the
boxcar is short it contaminates the whole record. Padding to $N + M - 1 = 44$
reduces the error to rounding ($8.60\times10^{-16}$).

## 8. Python demonstration

`code/convolution_and_filters_demo.py` is print-only, single-process, uses
`numpy` and `scipy.signal`, and runs in under a second. It:

1. convolves by definition, by `numpy.convolve` and by FFT, and compares;
2. verifies the four algebraic properties and the sum rule;
3. measures the `full`/`same`/`valid` relations and the circular-convolution
   wrap-around;
4. locates an injected pulse by cross-correlation and compares the correlation
   with a reversed convolution;
5. measures the matched-filter gain against $\sqrt N$ over 200 realisations, and
   the shape-limited gain for a Gaussian pulse;
6. measures the moving-average DC gain, exact nulls and sidelobe convergence;
7. measures the first-difference gain against the exact closed form;
8. measures the $(M-1)/2$ shift imposed by filtering and what `mode='same'` does
   to it.

```bash
cd 20-signal-processing/01-signals-and-systems/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python convolution_and_filters_demo.py
```

## 9. Assumptions and regime of validity

1. **Linearity and time-invariance.** Every statement here is an LTI statement;
   see [20-01-02 §11](02-lti-systems.md).
2. **Zero-padding must reach $N+M-1$.** Padding to any shorter length leaves
   wrap-around. Padding to a power of two is a speed choice, not a correctness
   one, but it must be at least $N+M-1$.
3. **The matched filter assumes the noise is white.** For coloured noise the
   optimal filter is $h \propto R_\nu^{-1}s$ in matrix form, i.e. whiten *then*
   match; using the plain matched filter on correlated noise loses the gain
   $\sqrt N$ predicts
   ([20-05-04](../05-noise-and-random-signals/04-noise-reduction.md)).
4. **The template must be known.** Estimation of the template from the data
   (as in a cross-correlation picker or a stacking operator) biases the peak
   upward, because the template is fitted to the noise it is later correlated
   with.
5. **The signal must not change shape between the template and the target.**
   Dispersion, attenuation and instrument drift all break this, and the
   correlation peak then measures a compromise delay rather than an arrival.
6. **Correlation coefficients require normalisation.** An unnormalised
   $r_{xy}$ grows with record length and amplitude; only
   $r_{xy}/\lVert x\rVert\lVert y\rVert \in [-1,1]$ is interpretable as a
   similarity.
7. **The delay estimated from a discrete peak is quantised.** Peak-picking on
   the sampled correlogram has resolution $\Delta t$; sub-sample accuracy
   requires interpolating the peak (a parabola through three samples is the usual
   choice) and a stated uncertainty, such as
   $\sigma_\tau \approx \frac{1}{2\pi f_{\text{dom}}\sqrt{\mathrm{SNR}}}$ for a
   narrow-band wavelet of dominant frequency $f_{\text{dom}}$.

## 10. Exercises

- [`exercises/03-convolution-and-filters-exercises.md`](./exercises/03-convolution-and-filters-exercises.md)
- [`exercises/03-convolution-and-filters-solutions.md`](./exercises/03-convolution-and-filters-solutions.md)

## 11. Common pitfalls

1. **Forgetting the reversal.** `np.correlate` and `np.convolve` differ by a
   reflection; confusing them turns a delay estimate into its negative.
2. **Padding to the input length.** `np.fft.irfft(rfft(x)*rfft(h))` without
   padding returns a *circular* convolution; the demonstration measures a 50 %
   rms error for that mistake.
3. **Reading `mode='same'` as acausal.** It is not: the delay was removed by
   trimming, and the end samples are gone.
4. **Assuming $\sqrt N$ from a noise-contaminated template.** The gain is
   $\lVert s\rVert/\max\lvert s\rvert$ for the *shape* you have, which can be far
   below $\sqrt N$.
5. **Thresholding a detection at the single-lag noise level.** Search over $L$
   lags inflates the largest noise value by roughly
   $\sqrt{2\ln L}$; the demonstration measures $3.2$ for $L\approx 1200$.
6. **Trusting a sidelobe specification for a short filter.** For $M = 5$ the
   measured first sidelobe is $-12.04\ \mathrm{dB}$, not $-13.26\
   \mathrm{dB}$.
7. **Treating a difference as a derivative.** Without the $1/\Delta t$ the
   operator has no units, and its gain saturates at Nyquist.

## 12. Mastery checkpoint

Without notes:

**(a)** Convolve $x = [1, 2, -1]$ with $h = [2, 0.5]$; give the output length
and verify the sum rule.
**(b)** Explain in two sentences why an FFT convolution of two 1000-sample
sequences computed with a 1024-point transform gives a wrong answer, and what
length fixes it.
**(c)** A 25-sample rectangular pulse of amplitude 3 in white noise of
$\sigma = 2$ is matched-filtered. Give the attainable peak-to-rms gain, and the
gain if the pulse is instead a Gaussian of the same length and unit peak whose
sample norm is $4.10$.
**(d)** A cross-correlation peaks at lag 227 with a template whose origin is at
index 10. Where is the feature?
**(e)** Derive the null frequencies of an 8-point moving average and state the
gain at Nyquist. Why does the formula differ in form between odd and even $M$?
**(f)** A first-break picker reports an arrival 3 samples later after the record
is low-pass filtered with a causal 7-point boxcar. Is the report consistent with
the known filter delay? What if the filter is applied with `mode='same'`?

Answers for (a)–(e) are in the
[solutions](./exercises/03-convolution-and-filters-solutions.md).

## 13. Related modules

- [20-01-02 LTI Systems and Impulse Response](02-lti-systems.md) — the system
  view, stability and the eigenfunction property.
- [20-01-04 Transfer Functions, Poles and Zeros](04-transfer-functions.md) — the
  design view of $h$, where the sidelobe table of Section 5.1 becomes a
  specification.
- [20-02-01 Practical DFT/FFT](../02-fourier-and-spectral-analysis/01-dft-fft-practice.md) —
  the transform used for the fast convolution, and its normalisation.
- [20-03 Digital Filtering](../03-digital-filtering/README.md) — designed FIR and
  IIR filters rather than ad-hoc kernels.
- [20-04 Deconvolution and Inverse Filtering](../04-deconvolution-and-inverse-filtering/README.md) —
  inverting a convolution, which is an ill-posed problem.
- [01-10 Fourier Analysis and Spectral Methods](../../01-mathematics/10-fourier-analysis/README.md) —
  the convolution theorem and its proofs.
