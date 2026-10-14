---
id: 20-03-01
title: "FIR Filter Design: Windows, Parks-McClellan, Least Squares"
level: graduate
prereqs: ["20-01-03", "20-01-04", "20-02-01"]
tags: [signal-processing, filtering, fir, window-method, parks-mcclellan, least-squares, linear-phase]
---

# FIR Filter Design: Windows, Parks-McClellan, Least Squares

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the frequency response of a finite impulse response (FIR) filter
   from its coefficients, and **state** the condition on the coefficients that
   makes the phase exactly linear.
2. **Reproduce** the window method from the convolution theorem, and **explain**
   the Gibbs oscillation it leaves behind.
3. **Compute** the transition width and stopband attenuation of a windowed design,
   and **measure** both from the realised filter rather than trusting a rule of
   thumb.
4. **Design** an equiripple filter with the Parks-McClellan algorithm and a
   least-squares filter, and **state** which error norm each one minimises.
5. **Choose** between window, equiripple and least-squares designs for a stated
   geophysical requirement.
6. **Verify** that a symmetric FIR filter has a constant group delay of exactly
   $(N-1)/2$ samples, by measuring the phase derivative.

## Prerequisites

- [20-01-03 Convolution, Correlation and Filtering](../01-signals-and-systems/03-convolution-and-filters.md) —
  the convolution sum and the impulse response.
- [20-01-04 Transfer Functions, Poles and Zeros](../01-signals-and-systems/04-transfer-functions.md) —
  the $z$-transform and the frequency response $H(e^{i\omega})$.
- [20-02-01 Practical DFT/FFT: Normalisation, Units and Pitfalls](../02-fourier-and-spectral-analysis/01-dft-fft-practice.md) —
  how a response is evaluated numerically from coefficients.

## 1. Intuition: design is approximation

An FIR filter is a finite weighted sum of delayed samples,

$$y[n] = \sum_{k=0}^{N-1} b_k\,x[n-k],$$

and its whole character lives in the coefficient vector $b_0,\dots,b_{N-1}$. There
are only two questions in FIR design: *which coefficients?* and *how good is the
result?* The answers are coupled, because a finite impulse response cannot realise
an ideal frequency response. The ideal lowpass — pass everything below $f_p$,
kill everything above $f_s$, with a perfectly flat magnitude and no delay — has an
infinitely long, non-causal impulse response. Any finite filter approximates it,
and every design method is a different answer to *how to distribute the error*.

This matters in geophysics because the specification is usually a band and an
attenuation: "keep 0–40 Hz, remove everything above 60 Hz by at least 60 dB, and
do not distort the waveform." The three methods below meet that specification in
three different ways, and the differences are measurable, not matters of taste.

All models and data in this module are SYNTHETIC. The specification used here
(250 Hz sampling, 40 Hz passband edge, 60 Hz stopband edge) is a chosen teaching
specification, not a measurement from an instrument or survey.

## 2. Definitions

### 2.1 Frequency response and the DTFT

For a coefficient vector $b$, the frequency response is

$$H(e^{i\omega}) = \sum_{k=0}^{N-1} b_k e^{-i\omega k},
\qquad \omega = 2\pi \frac{f}{f_s},$$

with $\omega$ in radians per sample and $f_s$ the sample rate in Hz. We write
$H(e^{i\omega}) = |H|e^{i\phi}$, with $|H|$ the amplitude response and $\phi$ the
phase response. The demo evaluates $H$ on 8192 points from $0$ to $f_s/2$.

### 2.2 Ripple, attenuation, transition width

For a lowpass with passband $[0,f_p]$ and stopband $[f_s,f_s/2]$:

- **passband ripple** $= \max_{f\le f_p}|H|_{\mathrm{dB}} -
  \min_{f\le f_p}|H|_{\mathrm{dB}}$ (in dB);
- **stopband attenuation** $= -\max_{f\ge f_s}|H|_{\mathrm{dB}}$ (in dB, positive
  is good);
- **transition width** is the interval $[f_p,f_s]$ over which the response falls
  from passband to stopband.

Every one of these is measured from the realised $H$, never assumed.

### 2.3 Group delay

The group delay is

$$\tau_g(\omega) = -\frac{\mathrm{d}\phi(\omega)}{\mathrm{d}\omega},$$

in samples. It is the delay experienced by a narrow band of frequencies around
$\omega$. A filter with constant $\tau_g$ delays every frequency equally and
therefore does not disperse a broadband wavelet.

## 3. Derivations

### 3.1 The ideal lowpass and why truncation fails

The ideal lowpass has $H_d(e^{i\omega}) = 1$ for $|\omega|\le\omega_c$ and $0$
otherwise. Its impulse response is the inverse transform of a rectangle,

$$h_d[n] = \frac{\sin(\omega_c n)}{\pi n} = \frac{\omega_c}{\pi}\,\mathrm{sinc}
\left(\frac{\omega_c n}{\pi}\right),$$

which is infinite and non-causal: it decays only as $1/n$. Truncating it to
$N$ samples is multiplication by a rectangular window $w[n]$ in the time domain,
which by the convolution theorem is **convolution with the window's transform in
the frequency domain**:

$$H(e^{i\omega}) = \frac{1}{2\pi}\,H_d * W = \frac{1}{2\pi}\int H_d(\theta)
W(\omega-\theta)\,\mathrm{d}\theta.$$

The rectangular window's transform is a Dirichlet kernel with slowly decaying
ripples; convolving the ideal brick wall with it smears the edge and leaves
oscillations that do not disappear as $N$ grows — they only get narrower. That is
the **Gibbs phenomenon**, and it caps the rectangular-window attenuation at about
21 dB, independent of $N$ (the demo measures $34.1$ dB at a 60 dB threshold for
$N=121$, already better than the naive 21 dB because the measurement threshold and
the finite band edge interact — the honest statement is that no reasonable $N$
gets the rectangular window near 60 dB).

### 3.2 The window method

Replace the rectangular window by a window whose transform has lower sidelobes:

$$b_k = h_d\!\left(k - \frac{N-1}{2}\right) w_k,\qquad k=0,\dots,N-1,$$

where $h_d$ is the ideal response sampled at the symmetric offsets. The window's
sidelobe level becomes the stopband floor, and the window's main-lobe width becomes
the transition width. Hence:

- **the window family sets the attenuation floor**;
- **the filter order sets the transition width**.

The demo confirms both statements from measurement rather than assertion. At
$N = 121$ taps and a cutoff at the band centre (50 Hz):

| window | ripple (dB) | attenuation (dB) | edge at $-60$ dB (Hz) |
|---|---|---|---|
| boxcar | 0.341 | 34.14 | 53.24 |
| Hann | 0.006 | 67.90 | 53.45 |
| Hamming | 0.022 | 58.49 | 53.54 |
| Blackman | 0.002 | 79.11 | 55.21 |
| Blackman-Harris | 0.000 | 111.28 | 56.41 |

The ordering is exactly the ordering of the windows' sidelobe levels, and the
transition edge barely moves because the main-lobe width is nearly the same at
fixed $N$. Then, holding the Kaiser window shape at $\beta = 6.0$ and increasing
the order:

| taps | attenuation (dB) | edge at $-60$ dB (Hz) |
|---|---|---|
| 31 | 25.12 | 65.83 |
| 61 | 65.33 | 57.91 |
| 121 | 71.30 | 53.96 |
| 241 | 76.87 | 51.99 |

The attenuation floor is nearly flat (25 dB for 31 taps is the exception: the
order is too small for the window's own floor to be reached), while the edge moves
steadily toward the passband. Conversely, holding $N = 121$ and raising $\beta$
from 0 to 9 moves the attenuation from 34.14 dB to 94.37 dB while the edge stays
within 53.2–55.3 Hz. **Order and window shape are independent knobs.**

### 3.3 The Kaiser order estimate

Kaiser's empirical relations connect the transition width, the attenuation and the
order. With $A$ the stopband attenuation in dB and $\Delta\omega$ the transition
width in radians per sample, $A \approx 2.285(N-1)\Delta\omega + 8$, and the
required shape parameter is $\beta = 0.1102(A-8.7)$ for $A>50$. For our
specification ($\Delta f = 20$ Hz at $f_s = 250$ Hz,
$\Delta\omega = 2\pi\cdot 20/250 = 0.5027$ rad/sample, $A = 60$ dB),
`kaiserord` returns $N = 47$ taps and $\beta = 5.6533$. The demo measures the
resulting attenuation as $60.44$ dB — the estimate is accurate to under 1 dB.

### 3.4 Linear phase

An FIR filter has exactly linear phase if and only if its coefficients are
symmetric ($b_k = b_{N-1-k}$) or antisymmetric, and then

$$H(e^{i\omega}) = e^{-i\omega (N-1)/2}\,A(\omega),$$

so $\phi = -\omega(N-1)/2$ and the group delay is exactly constant:

$$\tau_g = \frac{N-1}{2}\ \text{samples}.$$

The demonstration measures the passband group delay of a 61-tap Hamming filter as
$30.0000 \pm 3.6\times 10^{-12}$ samples and of a 121-tap filter as
$60.0000 \pm 7.2\times 10^{-12}$ samples — the theoretical $(N-1)/2$ values,
with the residual being floating-point noise in the numerical derivative.

## 4. The other two design methods

### 4.1 Parks-McClellan (equiripple)

The Parks-McClellan algorithm (the Remez exchange applied to filters) minimises
the **weighted Chebyshev** error: the maximum deviation from the desired response,
wherever it occurs,

$$\min_{b}\ \max_{\omega \in \text{bands}} W(\omega)\left|D(\omega) -
H(e^{i\omega})\right|.$$

The result is a response whose error is spread *equally* across the bands, with
equal ripples in passband and stopband. At the same order as the Kaiser design
(47 taps, stopband weighted 20:1), the demo measures $79.22$ dB of stopband
attenuation against the Kaiser window's $60.44$ dB — an **$+18.78$ dB** gain from
distributing the error uniformly instead of concentrating it near the band edge.

### 4.2 Least squares

Least squares minimises the **total** squared error,

$$\min_b \int W(\omega)\left|D(\omega)-H(e^{i\omega})\right|^2 \mathrm{d}\omega.$$

Because it integrates the error, it tolerates large deviations over small
frequency intervals in exchange for small deviations everywhere else. At the same
order the demo measures $63.59$ dB of stopband attenuation and $0.048$ dB of
passband ripple: it beats the window method by a little and loses to equiripple by
a lot, exactly as the norm predicts.

### 4.3 Which norm for which job

- **Equiripple** when the requirement is a hard *worst-case* bound ("no spectral
  leakage above 60 dB anywhere in the stopband").
- **Least squares** when the requirement is a small *average* error and some local
  ringing is acceptable (matched-filter and shaping applications).
- **Window** when you want a closed-form design, an explicit trade of width for
  attenuation, and the ability to reason about it analytically.

## 5. Worked example (SYNTHETIC)

Design a lowpass for $f_s = 250$ Hz, $f_p = 40$ Hz, $f_s^{\text{stop}} = 60$ Hz,
requiring at least 60 dB of stopband attenuation.

1. Transition width $\Delta f = 60 - 40 = 20$ Hz, so
   $\Delta\omega = 2\pi(20)/250 = 0.5027$ rad/sample.
2. Kaiser: $\beta = 0.1102(60-8.7) = 5.653$.
3. Order: $N \approx (A-8)/(2.285\Delta\omega) + 1 = (60-8)/(2.285\cdot 0.5027)+1
   = 51.99/1.1487 + 1 = 45.3 + 1 = 46.3$, so $N = 47$ (the smallest odd order
   $\ge 46.3$; odd keeps the linear-phase type-I symmetry and $N-1$ even).
4. The cutoff is placed at the band centre, $(40+60)/2 = 50$ Hz. Placing it at
   $f_p$ would add passband ripple; at $f_s$ it would lose attenuation. The
   centre splits the transition width symmetrically.
5. The measured attenuation is 60.44 dB and the measured group delay is
   $(47-1)/2 = 23$ samples. At $f_s = 250$ Hz that is
   $23/250 = 92$ ms of delay — the price of linear phase, and the reason
   zero-phase filtering (see [04](04-phase-and-zero-phase.md)) exists.

## 6. Assumptions and regime of validity

1. **The desired response is piecewise constant with specified bands.** All three
   methods assume you can name passbands, stopbands and weights. An arbitrary
   target (say, a measured instrument response) must be discretised onto bands
   first.
2. **The filter is linear and time-invariant.** Coefficients are fixed. Adaptive
   filters ([05](05-adaptive-filtering.md)) violate this deliberately.
3. **Symmetric (or antisymmetric) coefficients for linear phase.** If symmetry is
   broken — for example by windowing a non-symmetric ideal response — the phase
   becomes non-linear and the group delay varies.
4. **Long enough to reach the window's floor.** Below about 40 taps at this
   specification the order, not the window, limits the attenuation (25 dB at
   $N=31$).
5. **The realisation is exact.** Direct-form FIR convolution has no stability
   question (no poles), but coefficient quantisation in fixed-point hardware
   perturbs the response; that is outside this lesson.
6. **Sampling is already correct.** Filtering does not repair aliasing that has
   already happened; see [03](03-filter-applications.md).

## 7. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| sample rate | $f_s$ | Hz | samples s$^{-1}$ |
| normalised frequency | $\omega$ | rad/sample | $2\pi f/f_s$ dimensionless |
| response | $H$ | dimensionless | ratio of output to input amplitude |
| ripple, attenuation | — | dB | $20\log_{10}|H|$, dimensionless |
| group delay | $\tau_g$ | samples | $\mathrm{d}\phi/\mathrm{d}\omega$, rad per (rad/sample) |
| time delay | — | s | $\tau_g / f_s$ |

The only place a unit error hides is the last row: a group delay of 23 samples at
$f_s = 250$ Hz is 92 ms, but at $f_s = 4$ kHz it is 5.75 ms. Always divide by the
sample rate before quoting a time.

## 8. Python demonstration

`code/fir_filters_demo.py` designs all of the filters above and prints the
measured ripple, attenuation, transition edge and group delay. It requires no
network access, uses a fixed seed (`np.random.default_rng(20261014)`) and exits 0.
Run it with the command in the [module README](README.md).

What to look for in its output:

1. **section 2** — the window family table; the attenuation ordering follows the
   sidelobe ordering.
2. **section 3** — order moves the transition edge; $\beta$ moves the floor.
3. **section 4** — Parks-McClellan gains 18.78 dB over Kaiser at the same order.
4. **section 5** — least squares sits between the two.
5. **section 6** — the measured group delay equals $(N-1)/2$ to 12 digits.

## 9. Exercises

Full sets with worked solutions are in
[`exercises/01-fir-filters-exercises.md`](exercises/01-fir-filters-exercises.md) and
[`exercises/01-fir-filters-solutions.md`](exercises/01-fir-filters-solutions.md).

- **★** Compute the ideal lowpass impulse response for $f_c = 50$ Hz at
  $f_s = 250$ Hz and evaluate the first five non-zero samples.
- **★★** Design a 121-tap windowed lowpass and measure its attenuation; explain
  the difference from the table in §3.2.
- **★★** Compare equiripple and least-squares designs at equal order and state
  which norm explains the difference.
- **★★★** Show that breaking coefficient symmetry converts a constant group delay
  into a frequency-dependent one, and measure by how much.

## Mastery checkpoint

Complete this without notes:

> A 200 Hz-sampled record must keep $0$–$20$ Hz and reject everything above
> 35 Hz by at least 55 dB. **(a)** Compute the normalised transition width in
> rad/sample. **(b)** Estimate the Kaiser order and $\beta$. **(c)** State the
> group delay in samples and in milliseconds for the odd order nearest your
> estimate. **(d)** State whether a 30-tap design could meet the specification,
> and why. **(e)** Explain in one sentence why the equiripple design can meet the
> same specification at lower order than the window design.

A worked version appears in the
[solutions](exercises/01-fir-filters-solutions.md).

## Common pitfalls

1. **Trusting the rule of thumb instead of measuring.** The Kaiser estimate is
   good to about 1 dB *for the window it was derived for*; the demo's $N=31$ row
   is 40 dB away from the estimate because the order is too small for the window
   floor to be reached.
2. **Placing the cutoff at the passband edge.** The transition is symmetric about
   the cutoff, so putting the cutoff at $f_p$ costs half the transition width of
   passband.
3. **Forgetting the delay.** A linear-phase FIR of $N$ taps delays the record by
   $(N-1)/2$ samples. Cross-correlating or stacking traces without correcting for
   it introduces a systematic misalignment.
4. **Judging the filter by its stopband alone.** A design that meets the stopband
   by rippling 3 dB in the passband has destroyed amplitudes that a reflection
   coefficient or an AVO analysis depends on.
5. **Confusing ripple in dB with ripple in amplitude.** 1 dB of ripple is about
   12% in amplitude — a large error in an amplitude study.

## Related modules

- [20-01-03 Convolution, Correlation and Filtering](../01-signals-and-systems/03-convolution-and-filters.md) —
  the convolution sum every design assumes.
- [20-02-03 Window Functions and Spectral Leakage Control](../02-fourier-and-spectral-analysis/03-windowing-advanced.md) —
  the window family in its spectral-estimation role.
- [20-03-02 IIR Filter Design: Butterworth, Chebyshev, Elliptic](02-iir-filters.md) —
  recursive filters that buy order at the cost of phase.
- [20-03-04 Phase Response, Zero-Phase Filtering and Distortion](04-phase-and-zero-phase.md) —
  what linear phase is worth, and how to get it without the delay.
- [03-03-05 SciPy for Scientific Computing](../../03-scientific-computing/03-scipy/05-signal.md) —
  the `scipy.signal` design routines used here.
- [01-07-08 Singular Value Decomposition and Rank Truncation](../../01-mathematics/07-linear-algebra/08-svd.md) —
  the least-squares machinery behind `firls`.
