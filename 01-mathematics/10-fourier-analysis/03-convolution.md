---
id: 01-10-03
title: "Convolution, Filtering and the Convolution Theorem"
level: advanced
prereqs: ["01-10-02", "01-05-05"]
estimated_minutes: 90
tags: [convolution, filtering, deconvolution, instrument-response, inverse-problems]
---

# Convolution, Filtering and the Convolution Theorem

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** convolution for continuous and discrete signals and compute it by
   direct summation.
2. **Prove** the convolution theorem and state the three conditions under which a
   DFT-based convolution reproduces a linear convolution.
3. **Recognise** filtering, instrument response and wavelet convolution as the
   same operation, and predict the effect of a filter from its transfer function.
4. **Explain** the duality between a hard edge in time (sinc response, sidelobes)
   and a hard edge in frequency (ringing in time), and quantify the Gibbs
   overshoot involved.
5. **Compute** the noise-averaging gain of a moving average and check it against
   $1/\sqrt{M}$.
6. **Formulate** deconvolution as a regularised inverse problem, choose a water
   level from the noise, and explain why no deconvolution is correct
   independently of the noise.

## Prerequisites

[01-10-02 The Fourier Transform and Its Properties](./02-fourier-transform.md) —
especially the property table and the normalisation discussion;
[01-05-05 Integration Techniques and Definite Integrals](../05-single-variable-calculus/05-integration.md) —
for the integrals that define the continuous convolution.

## 1. Intuition: what a physical measurement does to a signal

Every measurement in geophysics is a weighted average of the thing being
measured. A gravimeter's spring responds to mass over a finite region with a
sensitivity that falls off with distance. A seismometer's mass-spring system
responds to ground acceleration with a response that rings for a while after the
ground has stopped. A satellite altimeter averages the sea surface over the area
of its footprint. A thermometer's bead has a thermal time constant.

In each case, the recorded quantity $y$ is related to the true quantity $x$ by

$$y(t) = \int_{-\infty}^{\infty} h(\tau)x(t-\tau)\,d\tau \;\equiv\; (h * x)(t),$$

where $h$ is the **impulse response**: what the instrument would record if the
input were an instantaneous spike. And in each case the same problem follows:
what was $x$?

The transform of the equation is where the leverage lies. Convolution becomes
multiplication, so $x$ is recoverable by dividing spectra — until noise is
considered, at which point the division becomes an inverse problem. This lesson
is about the first half; the second half is the rest of the curriculum.

## 2. Definitions

### 2.1 Continuous convolution

$$(x * h)(t) = \int_{-\infty}^{\infty}x(\tau)h(t-\tau)\,d\tau
= \int_{-\infty}^{\infty}h(\tau)x(t-\tau)\,d\tau .$$

The operation flips $h$ in time and slides it across $x$. For a *causal* filter
($h(\tau) = 0$ for $\tau<0$) the output at time $t$ depends only on inputs at
earlier times, which is what physical instruments do, but this is a property of
the particular $h$, not of convolution.

### 2.2 Discrete convolution

$$(x * h)[n] = \sum_{m} x[m]\,h[n-m] .$$

With $x$ of length $N_x$ and $h$ of length $N_h$, the result has length
$N_x+N_h-1$: **convolution lengthens signals.** This elementary fact is the first
thing to break when a filter is implemented with an FFT and the arrays are not
padded.

### 2.3 Basic algebra

Convolution is commutative, associative and distributive:

$$x*h = h*x, \qquad (x*h_1)*h_2 = x*(h_1*h_2), \qquad x*(h_1+h_2) = x*h_1 + x*h_2 .$$

The demo verifies the first two numerically on a 512-sample signal: the maximum
discrepancy is $2.2\times10^{-16}$ for commutativity and $4.4\times10^{-16}$ for
associativity — round-off.

**Associativity is the reason cascaded operations can be lumped.** A source
wavelet, a propagating earth, an instrument response and a recording filter can
be collapsed into one operator $h_{\text{total}} = h_{\text{src}} * h_{\text{path}}
* h_{\text{inst}} * h_{\text{rec}}$, and the transform of that chain is a *product
of transfer functions*. Every amplitude-versus-frequency argument in processing
is a statement about a product.

## 3. The convolution theorem

### 3.1 Statement and proof

$$\mathcal F\{x * h\} = X(f)\,H(f).$$

The proof is three lines of substitution. With
$y(t) = \int x(\tau)h(t-\tau)d\tau$,

$$Y(f) = \int_t\int_\tau x(\tau)h(t-\tau)e^{-2\pi i f t}\,d\tau\,dt
= \int_\tau x(\tau)\underbrace{\int_t h(t-\tau)e^{-2\pi ift}dt}_{H(f)e^{-2\pi i f\tau}}\,d\tau
= H(f)\underbrace{\int_\tau x(\tau)e^{-2\pi i f\tau}d\tau}_{X(f)} .$$

The inner substitution $u = t-\tau$ extracts the shift factor and leaves $H(f)$;
the outer integral is $X(f)$. There is no conjugation and no extra factor, which
is why the sign convention adopted in
[01-10-02](./02-fourier-transform.md) — the same one used everywhere in this
module — makes the theorem read as written.

### 3.2 Verified numerically

The demo convolves a 512-sample pseudo-random signal with a 40-sample decaying
oscillatory response, both zero-padded to 1024, and compares the direct
$O(N^2)$ convolution with the FFT-based one:

| quantity | value |
|---|---|
| max $\lvert$direct $-$ FFT$\rvert$ | $6.0\times10^{-14}$ |
| relative to the peak of the convolution | $2.0\times10^{-14}$ |
| same comparison **without** zero padding | $1.892$, i.e. $0.64\times$ the peak |

The second row is the one to remember. With the padding, the circular
convolution of the DFT equals the linear convolution exactly (to round-off). The
missing samples do not vanish: they **wrap around** to the beginning of the
record, and on this test the resulting error is of the same order as the answer.
The rule is: pad to at least $N_x+N_h-1$, i.e. by the length of the filter.

### 3.3 What a filter does, read off its transfer function

Because convolution multiplies, "what does this filter do?" is answered by
tabulating $\lvert H(f)\rvert$. The demo computes it for four short filters (the
FFT of the zero-padded impulse response):

| $f$ (Hz) | boxcar 5 | boxcar 9 | triangular 9 | Gaussian 9 |
|---|---|---|---|---|
| 0.0 | 1.00000 | 1.00000 | 1.00000 | 1.00000 |
| 10.0 | 0.93784 | 0.80179 | 0.87954 | 0.93273 |
| 20.0 | 0.76443 | 0.34330 | 0.58435 | 0.75571 |
| 25.0 | 0.64660 | 0.11006 | 0.41809 | 0.64447 |
| 40.0 | 0.24461 | 0.22656 | 0.05983 | 0.32110 |
| 50.0 | 0.00026 | 0.11135 | 0.00000 | 0.16764 |
| 62.5 | 0.20000 | 0.11111 | 0.04000 | 0.06262 |

(with $dt = 4$ ms, so the Nyquist frequency is 125 Hz).

Three lessons are visible in that table.

1. **Every one of these filters is a low-pass filter**, even though only the
   Gaussian was designed as one. Smoothing in time is always low-pass filtering
   in frequency; there is no way to smooth locally and preserve the spectrum.
2. **The boxcar has exact zeros.** The 9-point boxcar has its first spectral zero
   at the frequency the demo measures as 27.750 Hz, against the prediction
   $1/(M\,dt) = 27.778$ Hz. At that frequency the output is *identically zero*:
   nothing that follows in the processing chain can recover what the filter
   removed. The 5-point boxcar has a zero at 50 Hz (measured $2.6\times10^{-4}$,
   a discretisation residue) and the triangular filter at 50 Hz as well.
3. **A Gaussian has no zeros** at all. If a later step requires inverting the
   filter, a Gaussian's transfer function can be divided out over the whole band,
   whereas a boxcar's cannot. That is the technical reason tapering and Gaussian
   smoothing are preferred when inversion follows filtering.

### 3.4 Noise averaging

A moving average of $M$ points applied to white noise scales its standard
deviation by $1/\sqrt{M}$. The demo measures this directly with 20 000
pseudo-random samples:

| $M$ | measured $\sigma_{\text{out}}/\sigma_{\text{in}}$ | $1/\sqrt{M}$ |
|---|---|---|
| 3 | 0.57399 | 0.57735 |
| 9 | 0.33275 | 0.33333 |
| 25 | 0.20240 | 0.20000 |

The agreement is to about 1%. Since the gain applies to the *noise* and the
signal is attenuated only according to $\lvert H(f)\rvert$ at its own frequency,
the signal-to-noise ratio improves by roughly $\sqrt{M}$ at frequencies where
$\lvert H\rvert \approx 1$ — the classical reason a long stack beats a short one.

The demo also confirms the transfer-function description on a pure tone: the
measured gain of a 3-point boxcar on a 23 Hz cosine is 0.891685 against a
predicted Dirichlet response $\lvert H(23\,\mathrm{Hz})\rvert = 0.891685$, and
for the 9-point boxcar 0.200548 against 0.200548 — five-figure agreement between
the filter's measured effect and its computed transfer function.

### 3.5 Hard edges in either domain

Section 3.3 and [01-10-02](./02-fourier-transform.md) Section 3.2 give one half
of a duality; the demo gives the other half, quantitatively.

| domain in which the edge is hard | response in the other domain | artefact |
|---|---|---|
| boxcar in time | sinc in frequency | sidelobes at $-13.26$ dB, zeros that destroy information |
| brick wall in frequency | sinc in time | ringing near every edge, overshoot of 8.949% of the jump |

The demo measures the second half twice, once by brick-wall filtering a periodic
square wave and once by evaluating the truncated Fourier series of the same
square wave at the same sample points:

| bins per side | odd harmonics | filter overshoot (% of jump) | series overshoot | difference |
|---|---|---|---|---|
| 1 | 1 | 13.662 | 13.662 | $-0.000$ |
| 3 | 2 | 10.021 | 10.021 | $-0.001$ |
| 5 | 3 | 9.418 | 9.417 | $+0.001$ |
| 9 | 5 | 9.116 | 9.116 | $+0.001$ |
| 17 | 9 | 9.005 | 8.988 | $+0.017$ |
| 33 | 17 | 8.939 | 8.963 | $-0.024$ |
| 65 | 33 | 8.970 | 8.905 | $+0.065$ |
| 129 | 65 | 8.611 | 8.938 | $-0.327$ |

The two columns agree to three decimal places for the narrowest bands and to a
fraction of a per cent at the widest, where the sampled square wave's DFT
coefficients deviate from the continuous $1/n$ (and the jump sits between
samples). The conclusion is exact: **a brick-wall filter is a truncated Fourier
series.** Ringing at an edge is not a defect of a program; it is the price of a
sharp band limit. It is why sharp-cutoff filtering makes seismic data look
"ringy", and why a gap or a steeply truncated array produces spurious amplitudes
at its edges.

## 4. Physical interpretation: filtering, response and the earth

**Filters.** A filter is any operation expressible as a convolution. Its
impulse response is its definition; its transfer function is its character.

**Instrument response.** The sensor's impulse response $h_{\text{inst}}$ is
convolved with the ground motion. The demo models a slow first-order sensor,
$h(t) = (dt/\tau)e^{-t/\tau}$ with $\tau = 0.5$ s, whose continuous transfer
function is $H(f) = 1/(1+2\pi i f\tau)$, truncated to 800 samples (3.2 s). The
demo compares three evaluations of $\lvert H\rvert$:

| $f$ (Hz) | continuous $1/\lvert 1+2\pi if\tau\rvert$ | discrete sum | FFT of $h$ | relative difference | phase (°) |
|---|---|---|---|---|---|
| 0.122 | 0.933696 | 0.938640 | 0.938640 | $5.9\times10^{-3}$ | $-20.83$ |
| 0.488 | 0.546106 | 0.549139 | 0.549139 | $7.8\times10^{-3}$ | $-56.59$ |
| 0.977 | 0.309902 | 0.310786 | 0.310786 | $1.4\times10^{-2}$ | $-71.18$ |
| 5.005 | 0.063472 | 0.063662 | 0.063662 | $6.3\times10^{-2}$ | $-82.75$ |
| 25.024 | 0.012719 | 0.012964 | 0.012964 | $3.2\times10^{-1}$ | $-71.23$ |
| 99.976 | 0.003184 | 0.004217 | 0.004217 | $1.4\times10^{0}$ | $-17.99$ |

The FFT of the stored impulse response and the direct sum agree to round-off.
Both differ from the *continuous* response, increasingly at high frequency,
because of **aliasing**: the discrete-time system's response is the sum of the
continuous response at $f$ and at $f \pm m/dt$. The truncation of $h$ also
matters: the demo reports that the stored 800 samples sum to 1.002337 against
1.004005 for the infinite series, a ratio of $0.998338 = 1-e^{-6.4}$, i.e. the
truncation loses 0.17% of the low-frequency gain. This is exactly why a real
instrument response is stored as **poles and zeros** rather than as a finite
impulse response.

The demo reports a peak input amplitude of 0.9841 against a peak recorded
amplitude of 0.0182: the sensor has attenuated the signal by a factor of 54 and
delayed it, with a phase lag running from $-21^\circ$ at 0.12 Hz to
$-83^\circ$ at 5 Hz. Both effects are in
$H(f)$ and both are removed by the same operation.

**The earth as a filter.** A seismic trace is, to good approximation, the
convolution of a source wavelet, the reflectivity series and the instrument
response. Migration can be described as undoing propagation; deconvolution is
undoing the wavelet. The algebra is identical; only the interpretation of $h$
changes.

## 5. Deconvolution as an inverse problem

### 5.1 The naive inverse and why it fails

Given $y = h * x$ and $Y = HX$, the algebra suggests $\hat X = Y/H$. In the
demo, with no noise at all, this works perfectly: the recovered signal differs
from the true signal by an RMS of $1.8\times10^{-15}$, i.e. round-off, because
the padded circular system is exactly invertible when $H$ has no zeros on the
grid.

Add deterministic "noise" of RMS $4.99\times10^{-4}$ to a signal of RMS
$6.18\times10^{-2}$ (0.81%) and the same division gives:

| water level $\epsilon$ | RMS error | maximum gain $\lvert H\rvert/(\lvert H\rvert^2+\epsilon^2)$ |
|---|---|---|
| 0 (naive) | 0.120002 | 249.42 |
| $10^{-4}$ | 0.119933 | 249.26 |
| $10^{-3}$ | 0.113447 | 234.81 |
| $3\times10^{-3}$ | 0.078982 | 159.90 |
| $10^{-2}$ | **0.023347** | 50.00 |
| $3\times10^{-2}$ | 0.045148 | 16.67 |
| $10^{-1}$ | 0.059738 | 5.00 |
| $0.3$ | 0.061602 | 1.67 |

The naive division is not merely suboptimal, it is the **worst** entry in the
table: its error is five times that of the best regularised inversion, on data
whose noise is under 1% of the signal. The largest $\lvert 1/H\rvert$ on the grid
is 249.4, i.e. 47.9 dB of noise gain at the far end of the band. The optimal
water level here is $\epsilon \approx 10^{-2}$, and the reason is the standard
bias–variance trade: the regularised division

$$\hat X(f) = \frac{\overline{H(f)}\,Y(f)}{\lvert H(f)\rvert^2 + \epsilon^2}$$

reduces to $Y/H$ where $\lvert H\rvert \gg \epsilon$ (unbiased but noisy) and
rolls off to $0$ where $\lvert H\rvert \ll \epsilon$ (biased but quiet).

### 5.2 The answer depends on the noise

The same experiment with a fixed $\epsilon = 10^{-2}$ and four noise levels:

| noise RMS | naive error | regularised error | winner |
|---|---|---|---|
| $10^{-4}$ | 0.012000 | 0.015299 | naive |
| $10^{-3}$ | 0.120002 | 0.023347 | regularised (5×) |
| $10^{-2}$ | 1.200019 | 0.177893 | regularised (7×) |
| $3\times10^{-2}$ | 3.600057 | 0.531946 | regularised (7×) |
| $10^{-1}$ | 12.000190 | 1.772495 | regularised (7×) |

At a noise level of $10^{-4}$ the honest inverse still wins; from $10^{-3}$
upward the regularised inverse is better, by a factor of about 7 at the highest
noise tested. **There is no correct deconvolution independent of the noise, and
no way to choose $\epsilon$ without estimating it.** A deconvolution result
reported without the regularisation used, or without an error bar, cannot be
evaluated by a reader.

This is the same statement as the downward-continuation limit derived in the
exercises of [01-10-02](./02-fourier-transform.md), and the same statement that
[18-inverse-problems](../../18-inverse-problems/README.md) formalises.

## 6. Python demonstration

[`code/convolution_demo.py`](./code/convolution_demo.py) produces every table
above; it runs in about four seconds using only the standard library:

```text
python3 code/convolution_demo.py
```

Implementation notes worth carrying into your own code:

1. **The demo compares a direct convolution with an FFT convolution, with and
   without padding, deliberately.** Reproducing the wrap-around failure
   ($1.892$ absolute error, $0.64$ of the peak) is more instructive than being
   told about it.
2. **The brick-wall test evaluates the truncated Fourier series separately** and
   compares it with the filtered data sample by sample. That is what makes the
   claim "the same operation" a measurement rather than a slogan.
3. **All synthetic signals are labelled and their parameters stated.** The
   sensor's $\tau$, the noise level and the wavelet frequency are inputs, not
   fitted values, so every discrepancy in the tables is a numerical or
   methodological effect rather than a mismatch between model and data.

## 7. Common mistakes

1. **Forgetting to pad.** Convolution lengthens signals by $N_h-1$ samples; a
   circular convolution without padding folds that tail back into the start of
   the record. The error is not small — see Section 3.2.
2. **Treating a filter's *time* extent as its only cost.** Its frequency response
   is a low-pass roll-off and possibly zeros. Check $\lvert H(f)\rvert$ before
   trusting the output.
3. **Assuming deconvolution is division.** It is division plus a regularisation
   whose size is set by the noise, and the noise is usually unmeasured.
4. **Spiking or whitening "for resolution" and calling the result data.** Any
   operation that boosts high frequencies boosts the noise there too.
5. **Using a boxcar filter before an inversion.** Its spectral zeros destroy
   information irrecoverably; a Gaussian has none.
6. **Believing that the convolution theorem makes filtering free.** It makes it
   fast ($O(N\log N)$); the information-theoretic cost of the filter is
   unchanged, and the high-wavenumber content it removes is gone.
7. **Applying a taper *after* the deconvolution, not before.** The taper must act
   on the recorded data where the truncation artefact lives.

## 8. Real-world applications

- **Seismic deconvolution.** Removing the source wavelet and the instrument
  response to sharpen reflections; the regularisation is chosen from the
  pre-signal noise level on each trace.
- **Gravity and magnetic filtering.** Upward continuation, wavelength filtering
  and derivative operators are all convolutions, with transfer functions
  $e^{-kz}$ (downward continuation), $k$ (first vertical derivative) and
  $k^2$ (second) — all amplifying short wavelengths (see the exercises of
  [01-10-02](./02-fourier-transform.md)).
- **Instrument correction of any observatory record.** Broadband seismometers,
  superconducting gravimeters and magnetometers all ship with poles-and-zeros
  response files precisely because a finite impulse response is a truncation of
  an infinite one, as Section 4 shows.
- **Satellite footprint and altimetry.** The measured sea-surface height is the
  true height convolved with the footprint weighting; the resulting
  along-track smoothing sets the shortest resolvable wavelength.
- **Tide-gauge and hydrological response.** The recorded water level is the true
  water level convolved with the stilling-well and sensor response — the same
  first-order low-pass used in the demo.
- **Optical and radar imaging.** A point-spread function *is* an impulse
  response, and image deconvolution is the same inverse problem with the same
  regularisation trade.

## 9. Further reading

- **Bracewell, R. N. (2000). *The Fourier Transform and Its Applications*
  (3rd ed.). McGraw-Hill.** Chapters 3 and 6. Level: intermediate. The
  convolution theorem and the convolution–multiplication duality, with the
  clearest pictures.
- **Sheriff, R. E. & Geldart, L. P. (1995). *Exploration Seismology* (2nd ed.).
  Cambridge University Press.** Chapters 9–10. Level: intermediate. Where
  convolution and deconvolution appear as seismic processing steps rather than
  as mathematics.
- **Yilmaz, Ö. (2001). *Seismic Data Analysis*. Society of Exploration
  Geophysicists.** Chapter 2. Level: intermediate to advanced. The standard
  reference on deconvolution practice: predictive, spiking, surface-consistent,
  and how the operator length and the pre-whitening are chosen.
- **Aster, R. C., Borchers, B. & Thurber, C. H. (2018). *Parameter Estimation
  and Inverse Problems in the Earth Sciences* (2nd ed.). Cambridge University
  Press.** Level: advanced. Tikhonov regularisation, water level, and the
  bias–variance trade, stated for exactly the deconvolution problem above.
- **Claerbout, J. F. (1992). *Earth Soundings Analysis: Processing versus
  Inversion*. Blackwell.** Level: advanced. The most thought-provoking treatment
  of why inversion and processing are not the same thing.

> Note on citations: bibliographic details above are given so you can locate the
> works. This repository does not host or reproduce copyrighted text, and you
> should confirm current availability and editions through your library before
> citing them.

## 10. Related lessons

- [02 The Fourier Transform and Its Properties](./02-fourier-transform.md) — the
  property table this lesson uses.
- [04 Discrete Fourier Transform and the FFT](./04-discrete-fourier.md) — the algorithm
  that makes FFT convolution practical, and the circularity that forces padding.
- [05 Sampling, Aliasing, Leakage and Windowing](./05-windowing-aliasing.md) —
  where the sinc and Dirichlet responses of Section 3 come from, in full.
- [07 Two-Dimensional Fourier Analysis and Wavenumber Filtering](./07-2d-fourier.md) —
  convolution in two dimensions, where the same duality becomes f-k filtering.
- [06-multivariable-calculus/08 Potential Fields, Laplace and Poisson Equations](../06-multivariable-calculus/08-potential-theory.md) —
  the equivalent-source ambiguity that limits how far any potential-field filter
  can be inverted.
- [20-signal-processing](../../20-signal-processing/README.md) — the module where
  these operations are applied to real records.
- [18-inverse-problems](../../18-inverse-problems/README.md) — the general theory
  of the ill-posed problem that Section 5 illustrates.

## 11. Exercises

Ten graded exercises, with full worked solutions, are in
[`exercises/03-convolution-exercises.md`](./exercises/03-convolution-exercises.md).
Solutions: [`exercises/03-convolution-solutions.md`](./exercises/03-convolution-solutions.md).

## Self-assessment checklist

- [ ] I can state the convolution theorem and prove it in three lines.
- [ ] I can compute a short discrete convolution by hand and state the output
      length.
- [ ] I can explain why FFT convolution needs padding, and how much.
- [ ] I can predict the effect of a boxcar, a triangular and a Gaussian filter
      from their transfer functions.
- [ ] I can explain why a boxcar filter's spectral zeros matter for later
      inversion, and why a Gaussian's absence of zeros is an advantage.
- [ ] I can derive the noise-averaging gain $1/\sqrt{M}$ and verify it.
- [ ] I can explain why a brick-wall filter rings and quote the Gibbs overshoot.
- [ ] I can set up Tikhonov-regularised deconvolution, choose a water level from
      the noise level, and explain the bias–variance trade.
- [ ] I can state what is lost when a deconvolution result is reported without
      the regularisation and an uncertainty.
