---
id: 20-04-04
title: "Deconvolution in the Presence of Noise"
level: research
prereqs: ["20-04-01", "20-04-03", "20-03-04"]
tags: [signal-processing, deconvolution, noise, prewhitening, regularization, noise-gain, resolution, snr]
---

# Deconvolution in the Presence of Noise

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the noise amplification of the inverse filter as a function of
   frequency, and **identify** the exact frequency at which it peaks.
2. **Measure** the deconvolution error versus record SNR for the naive inverse, a
   water level set by the noise-to-signal rule, and the oracle optimum.
3. **Explain** why the naive inverse error barely improves with SNR while the
   stabilised error improves linearly.
4. **Quantify** where in the spectrum the output noise energy comes from, and
   **state** the fraction that an unstabilised inverse puts outside the signal
   band.
5. **Derive** prewhitening as the addition of white noise to the wavelet power
   spectrum and **show** it is the same operation as the water level.
6. **Decide** how much resolution the noise actually allows, and **state** the
   trade numerically.

## Prerequisites

- [20-04-01 Deconvolution: Concept, Ill-Posedness and Stabilisation](01-deconvolution-concept.md) —
  the water-level inverse.
- [20-04-03 Wiener Filtering and Least-Squares Inverse Filters](03-wiener-filtering.md) —
  the same filter derived from least squares.
- [20-03-04 Phase Response, Zero-Phase Filtering and Distortion](../03-digital-filtering/04-phase-and-zero-phase.md) —
  why the *magnitude* spectrum of the wavelet decides the noise gain.

## 1. Intuition: the noise, not the wavelet, sets resolution

It is tempting to think that a sharper wavelet would give sharper deconvolution.
It would not, because deconvolution's limit is not the wavelet's width but the
noise's spectral reach. The inverse filter amplifies each frequency by $1/|W(f)|$.
Where the wavelet is strong, that gain is modest. Where the wavelet is weak — at
the band edges and in the gaps — the gain is enormous, and it amplifies whatever
noise happens to be there into the part of the answer where you needed signal.
For the demo's 45 Hz Ricker the inverse filter's peak gain is
$1.084\times10^{5}$ at 189.2 Hz, a frequency at which the wavelet has
$|W| = 6.6\times10^{-7}$. **The noise is placed, by construction, where there is
nothing to compete with it.**

The practical consequence is a ceiling: for a given noise level there is a best
possible reflectivity estimate, and no operator length, water level or algorithm
can beat it. This lesson measures that ceiling and shows how to reach it.

All models and data in this module are SYNTHETIC.

## 2. Definitions

### 2.1 Record signal-to-noise ratio and noise-to-signal ratio

$$\mathrm{SNR} = 10\log_{10}\frac{\mathrm{var}(d_{\text{clean}})}
{\mathrm{var}(e)}\ \text{(dB)},\qquad
\mathrm{NSR} = \frac{\mathrm{var}(e)}{\mathrm{var}(d_{\text{clean}})}.$$

Note that this is the *broadband* record ratio, and it is not the same as the
signal-to-noise ratio at the deconvolution output, because deconvolution changes
the spectral weighting (see §3.3).

### 2.2 Noise gain

The (power) noise gain of a filter $H$ applied to white noise is
$\|h\|^2$ in the time domain, or $\frac{1}{N}\sum_f|H(f)|^2$ in the frequency
domain. The inverse filter $H = 1/W$ has power gain
$\frac{1}{N}\sum_f 1/|W(f)|^2$, dominated entirely by the smallest $|W|$.

## 3. Derivations

### 3.1 Noise propagation through the inverse

With $d = w * r + e$, the naive inverse gives

$$R_{\text{est}}(f) = R(f) + \frac{E(f)}{W(f)},$$

so the output noise spectrum is $|E/W|^2 = S_{ee}(f)/|W(f)|^2$ for white input
noise of spectrum $S_{ee}$. The **output noise power per unit input noise power**
is therefore $1/|W(f)|^2$ at each frequency, and the total is its sum over the
band. This is exact and needs no simulation: the demo confirms it by injecting
noise and measuring.

### 3.2 Where the output noise lives

For the demo's wavelet:

| frequency | $\|W\|$ | $\|H\| = 1/\|W\|$ |
|---|---|---|
| 10.0 Hz | $5.904\times10^{-1}$ | 1.694 |
| 44.9 Hz | $4.612$ | 0.217 |
| 80.1 Hz | $1.673$ | 0.598 |
| 100.1 Hz | $4.403\times10^{-1}$ | 2.271 |
| 129.9 Hz | $2.517\times10^{-2}$ | 39.72 |
| 159.9 Hz | $5.191\times10^{-4}$ | $1.926\times10^{3}$ |
| 200.0 Hz | $6.594\times10^{-7}$ | $3.038\times10^{4}$ |

The gain rises by five orders of magnitude across the spectrum. The measured
consequence is blunt:

> **fraction of output noise power above 100 Hz: 1.0000**
> fraction of the wavelet's own energy above 100 Hz: 0.0014

The inverse filter puts **all** of its output noise into a band that carries
0.14% of the signal. This single comparison explains why prewhitening works and
why it costs so little: the band being suppressed is almost empty of signal.

### 3.3 The error versus SNR

| record SNR (dB) | naive inverse error | error, $\varepsilon = \mathrm{NSR}$ | oracle $\varepsilon$ | oracle error |
|---|---|---|---|---|
| 10 | $4.633\times10^{13}$ | 0.694 | $1.33\times10^{-2}$ | 0.625 |
| 20 | $1.143\times10^{13}$ | 0.555 | $1.33\times10^{-3}$ | 0.500 |
| 30 | $1.764\times10^{13}$ | 0.439 | $1.78\times10^{-4}$ | 0.392 |
| 40 | $1.256\times10^{12}$ | 0.337 | $1.33\times10^{-5}$ | 0.289 |
| 60 | $3.835\times10^{11}$ | 0.125 | $1.33\times10^{-6}$ | 0.124 |

All errors are relative to the band-limited target, whose own distance from the
true reflectivity is $\|r_{\text{ideal}}-r\|/\|r\| = 0.649$. The naive inverse
error is $\sim10^{13}$ and improves by only a factor of 120 as the record SNR
improves by five orders of magnitude: **it is limited by the smallest $|W|$, not by
the noise.** The stabilised error falls from $0.694$ to $0.125$ — a factor of 5.6
over the same range — and the noise-to-signal rule tracks the oracle optimum to
within about a factor of two in error at every SNR. The rule is not a heuristic
that happens to work; it is the correct scaling.

### 3.4 Prewhitening

Prewhitening adds a white component to the wavelet power spectrum before inverting:

$$|W'(f)|^2 = |W(f)|^2 + \varepsilon\max_f|W(f)|^2,$$

which is exactly the denominator of the water-level inverse. So prewhitening and
the water level are the same operation, seen from opposite ends. The demo measures
both effects as $\varepsilon$ grows:

| prewhitening $\varepsilon$ | peak $\|H\|$ | relative error | output noise above 100 Hz |
|---|---|---|---|
| $10^{-10}$ | 10838.700 | 171.898 | 0.9987 |
| $10^{-6}$ | 108.399 | 2.062 | 0.9421 |
| $2.5\times10^{-4}$ | 6.856 | **0.408** | 0.8045 |
| $10^{-3}$ | 3.428 | 0.447 | 0.6911 |
| $4\times10^{-3}$ | 1.714 | 0.505 | 0.4725 |
| $10^{-2}$ | 1.084 | 0.549 | 0.2886 |

Three things happen together, and only together:

- the peak gain falls by four orders of magnitude — the noise is no longer
  amplified into the spectral gaps;
- the fraction of output noise above 100 Hz falls from 0.9987 to 0.2886 — the
  amplification is being suppressed precisely where it was harmful;
- the error has a minimum near $\varepsilon = \mathrm{NSR}/4$ and rises on either
  side — the familiar resolution/bias trade.

The error minimum is *not* at the smallest $\varepsilon$. That is the entire point
of the lesson: **more resolution is not more information, and past the noise floor
it is less.**

### 3.5 How much resolution the noise allows

There is a compact way to state the trade. The deconvolution can trust a band up
to the frequency where the signal power falls to the noise power:

$$|W(f^{*})|^2 S_{dd} = S_{ee} \quad\Longrightarrow\quad
f^{*} \text{ is the highest usable frequency},$$

and the shortest reliable pulse has width about $1/(2f^{*})$. With the demo's 30 dB
record SNR and the measured spectra, the usable band is essentially the passband;
the recovered pulse is about 12–24 ms wide depending on $\varepsilon$ (§4 of
[20-04-01](01-deconvolution-concept.md)), against a wavelet whose own half-width is
of order 10 ms. The noise has cost a factor of about two in resolution, and no
operator choice recovers it.

## 4. Worked example (SYNTHETIC)

A record has a wavelet with usable band 10–90 Hz and a quiet-window noise power
that is $4\times10^{-3}$ of the signal power.

1. **Record the NSR**: $4\times10^{-3}$.
2. **Set the water level**: the measured rule is $\varepsilon \approx 0.2$–$0.25
   \times \mathrm{NSR}$, so $\varepsilon \approx 10^{-3}$.
3. **Predict the peak gain** from the prewhitening table: an $\varepsilon$ of
   $10^{-3}$ reduces the peak gain by four orders of magnitude relative to
   $\varepsilon = 10^{-10}$. For a wavelet with usable-band condition number $K$,
   the residual peak gain scales as $1/(\varepsilon \cdot \text{scale})$, so state
   it as "of order $\sqrt{\mathrm{NSR}}$-dependent" rather than a fixed number.
4. **Predict the resolution**: the invertible band extends to where the signal
   power equals the noise power. With a 90 Hz top of band and a 40 dB signal-to-
   noise ratio per octave, expect the reliable band to fall short of 90 Hz; the
   recovered pulse will be about twice the wavelet's own width.
5. **Verify with the forward residual**: convolve the result back with the wavelet
   and compare with the input. A residual of a few per cent with a stable answer
   is the target; a residual of a few per cent with an oscillating answer means the
   noise estimate was too low.

## 5. Assumptions and regime of validity

1. **The noise is additive and its power is measurable from a signal-free window.**
   Without a noise estimate there is no rule, only guessing. If no quiet window
   exists, estimate the noise from a high-frequency band where the wavelet has no
   energy — which is exactly what the gain spectrum above tells you is safe.
2. **The noise is white, or its spectrum is known.** For coloured noise the
   regulariser must become frequency-dependent: $\varepsilon(f) = S_{ee}(f)/S_{dd}(f)$.
3. **The wavelet is known and stationary.** Wavelet error and noise trade off
   differently; a wrong wavelet biases the answer even at infinite SNR.
4. **The model is convolutional.** Multiples and mode conversions are not noise
   and are not removed by a smaller water level.
5. **The 100 Hz comparison is a property of this wavelet.** The exact fraction
   where the noise lands depends on the wavelet's band and the sampling; the
   *structure* — noise concentrated where signal is weak — is general.

## 6. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| record SNR | — | dB | $10\log_{10}$ power ratio |
| NSR | — | dimensionless | inverse of the ratio |
| water level | $\varepsilon$ | dimensionless | relative to $\max|W|^2$ |
| noise gain | — | dimensionless | power in/power out |
| usable frequency | $f^{*}$ | Hz | where signal = noise power |
| pulse width | — | s | $\sim 1/(2f^{*})$ |

Because $\varepsilon$ is defined relative to $\max|W|^2$, it is scale-free; that is
what allows a rule like "$\varepsilon = 0.2\,\mathrm{NSR}$" to transfer between
datasets of different amplitude. If you define the water level as an absolute
number added to $|W|^2$, it carries units of the signal power squared and the rule
does not transfer.

## 7. Python demonstration

`code/deconvolution_noise_demo.py` builds the model, checks the noise-free inverse,
measures the error versus record SNR with three water-level choices, reports the
inverse filter's noise-gain spectrum and where the noise lands, and sweeps
prewhitening. It is self-contained, seeded with
`np.random.default_rng(20261014)`, and exits 0.

What to look for:

1. **section 1** — the noise-free in-band error of $1.6\times10^{-14}$, i.e.
   round-off.
2. **section 2** — the naive inverse error nearly constant at $10^{13}$ while the
   NSR rule tracks the oracle.
3. **section 3** — the peak gain at 189.2 Hz and the 1.0000 noise fraction above
   100 Hz.
4. **section 4** — the error minimum and the falling high-frequency noise share as
   $\varepsilon$ grows.

## 8. Exercises

Full sets with worked solutions are in
[`exercises/04-deconvolution-noise-exercises.md`](exercises/04-deconvolution-noise-exercises.md)
and
[`exercises/04-deconvolution-noise-solutions.md`](exercises/04-deconvolution-noise-solutions.md).

- **★** Compute the noise gain of $H = 1/W$ at a frequency where $|W| = 0.01$,
  and state how much a white noise floor of
  $\sigma = 10^{-3}$ contributes there.
- **★★** From the error-versus-SNR table, state the benefit of improving the
   record SNR from 10 to 30 dB, with numbers.
- **★★** Explain, using the 1.0000 noise fraction, why prewhitening costs so
  little resolution.
- **★★★** Derive the optimal frequency-dependent water level for coloured noise
  and show that it reduces to a constant when the noise is white.

## Mastery checkpoint

Complete this without notes:

> A trace has a wavelet with usable band 5–70 Hz and a quiet-window noise power
> 100 times below the signal. **(a)** State the NSR and the water level you would
> use, with the rule you applied. **(b)** State the frequency above which the
> inverse filter's gain exceeds 1000, given a usable-band condition number of
> 2000. **(c)** State whether prewhitening will cost detectable resolution in the
> 5–70 Hz band, and why. **(d)** Explain why the naive inverse error does not
> improve when the record SNR improves by 20 dB. **(e)** State one thing you could
> still improve, and one you cannot.

A worked version appears in the
[solutions](exercises/04-deconvolution-noise-solutions.md).

## Common pitfalls

1. **Believing a noisier-but-spikier section is better.** The naive inverse's
   error is $10^{13}$ while it looks maximally spiky.
2. **Estimating the noise from the whole record.** The signal inflates the
   estimate and the water level comes out too small.
3. **Using a fixed water level across a survey.** The NSR changes with fold,
   source strength and ground coupling; estimate it per ensemble.
4. **Assuming prewhitening is free.** It costs the resolution that the suppressed
   band would have provided; it is cheap here only because the wavelet is weak
   there.
5. **Applying a single water level to a time-varying wavelet.** The trade is
   frequency- and time-dependent.

## Related modules

- [20-04-01 Deconvolution: Concept, Ill-Posedness and Stabilisation](01-deconvolution-concept.md) —
  the trade-off this lesson resolves.
- [20-04-03 Wiener Filtering and Least-Squares Inverse Filters](03-wiener-filtering.md) —
  the least-squares derivation of the same regulariser.
- [20-05-03 Colour of Noise: White, Pink, Red and Geophysical Examples](../05-noise-and-random-signals/03-noise-colour.md) —
  what to do when the noise is not white.
- [20-03-03 Filter Selection for Geophysical Data](../03-digital-filtering/03-filter-applications.md) —
  the pre-processing that sets the noise this lesson has to live with.
- [18-03-01 Why Regularisation Is Physically and Statistically Justified](../../18-inverse-problems/03-regularization/01-why-regularize.md) —
  the statistical framing of the water level.
- [06-08-03 Moho Discontinuity Depth and Sharpness](../../06-seismology/08-receiver-functions-and-crustal-structure/03-moho-interface.md) —
  a crustal application where the water level sets the reported sharpness.
