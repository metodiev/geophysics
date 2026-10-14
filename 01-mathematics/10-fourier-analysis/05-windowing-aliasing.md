---
id: 01-10-05
title: "Sampling, Aliasing, Leakage and Windowing"
level: advanced
prereqs: ["01-10-04"]
estimated_minutes: 90
tags: [aliasing, nyquist, leakage, windowing, sampling]
---

# Sampling, Aliasing, Leakage and Windowing

## Learning objectives

By the end of this lesson you will be able to:

1. **State** the Nyquist relation and compute the apparent frequency of an
   aliased tone, in both time and space.
2. **Explain** why aliasing is a fold of the frequency axis and why it is
   invisible in a time-offset display.
3. **Derive** the resolution relation $df = 1/(N\,dt) = 1/T$ and distinguish it
   from the bin spacing.
4. **Quantify** scalloping loss and the leakage of a trend, and state what
   detrending does to each.
5. **Tabulate** the standard windows by coherent gain, main-lobe width and
   sidelobe level, and choose a window from the physics of the problem.
6. **Explain** why resolution is a threshold choice rather than a property, and
   quote a window-dependent resolution criterion.

## Prerequisites

[01-10-04 Discrete Fourier Transform and the FFT](./04-discrete-fourier.md) —
for the bin layout, the bin spacing $df$, and the distinction between bin spacing
and resolution, which this lesson develops.

## 1. Intuition: two approximations and one exact operation

The DFT is exact but the journey from a physical signal to a DFT is not. Two
approximations are made before the transform is even called:

- **Sampling.** We know the signal only at instants $n\,dt$. Anything the signal
  did between samples is lost, and it does not stay lost quietly: it comes back
  as an *apparent* low frequency. This is aliasing.
- **Truncation.** We know the signal only for a finite time, which is
  mathematically the same as multiplying the true signal by a boxcar. The
  spectrum of a product is the convolution of the spectra, so the measured
  spectrum is the true spectrum smeared by a sinc. This is leakage.

Both are consequences of the same idea — multiplication in one domain is
convolution in the other — and both can be quantified exactly. Neither can be
eliminated; they can only be managed, and the whole of "seismic data
acquisition and processing" is a long conversation about how.

## 2. Sampling and the Nyquist relation

### 2.1 The relation

A signal sampled at interval $dt$ (rate $f_s = 1/dt$) is unambiguous only up to
the **Nyquist frequency**

$$f_N = \frac{1}{2\,dt} = \frac{f_s}{2}.$$

Content above $f_N$ appears at a lower frequency. The **apparent frequency** of a
tone $f$ sampled at $f_s$ is its fold into $[-f_N, f_N]$:

$$f_{\text{app}} = \big((f + f_N) \bmod f_s\big) - f_N .$$

The demo makes the ambiguity concrete with a 10 Hz sampling rate and a
reference tone at 7 Hz:

| true $f$ (Hz) | folded (Hz) | maximum difference from the 7 Hz samples |
|---|---|---|
| 7 | $-3.00$ | $0.0$ |
| $-3$ | $-3.00$ | $5.2\times10^{-14}$ |
| 13 | $3.00$ | $1.4\times10^{-13}$ |
| $-7$ | $3.00$ | $0.0$ |
| 3 | $3.00$ | $5.2\times10^{-14}$ |
| 17 | $-3.00$ | $1.9\times10^{-13}$ |
| 23 | $3.00$ | $1.6\times10^{-13}$ |

Every one of those frequencies produces the *same samples*, to round-off. There
is no algorithm that can distinguish them. Note also that the fold of 7 Hz at
$f_s = 10$ Hz is $-3$ Hz, not $+3$ Hz: the apparent frequency preserves the sense
of the oscillation, which matters when the sign of a slowness or a Doppler shift
is being interpreted.

### 2.2 What a 100 Hz event looks like at different rates

| $f_s$ (Hz) | Nyquist (Hz) | apparent frequency of a 100 Hz event | aliased? |
|---|---|---|---|
| 1000 | 500 | 99.98 | no |
| 400 | 200 | 100.00 | no |
| 250 | 125 | 100.01 | no |
| 200 | 100 | 100.00 | no |
| 125 | 62.5 | 24.99 | **yes** |
| 100 | 50 | 0.01 | **yes** |

At 125 Hz sampling a 100 Hz event appears at 25 Hz — an entirely plausible
frequency for a seismic reflection, and nothing in the record announces the
error. At 100 Hz sampling it appears at 0.01 Hz, i.e. as a slow drift. The
apparent frequencies are found by the demo from the peak of the zero-padded
spectrum, so they are measured, not assumed.

### 2.3 The same rule in space

Replace $t$ by $x$ and $dt$ by $dx$ (receiver spacing) and the rule becomes

$$f_{\text{alias}} = \frac{v}{2\,dx}$$

for an event with apparent velocity $v$ along the line. The demo uses
$dx = 25$ m and $v = 1000$ m/s, so anything above 20 Hz is aliased:

| $f$ (Hz) | true $k$ (rad/m) | phase step between traces (°) | folded step (°) | apparent $k$ (rad/m) | apparent $v$ (m/s) |
|---|---|---|---|---|---|
| 10.0 | 0.0628 | 90.0 | 90.0 | 0.0628 | 1000.0 |
| 20.0 | 0.1257 | 180.0 | $-180.0$ | $-0.1257$ | $-1000.0$ |
| 30.0 | 0.1885 | 270.0 | $-90.0$ | $-0.0628$ | $-3000.0$ |
| 40.0 | 0.2513 | 360.0 | 0.0 | 0.0000 | $\infty$ |

Read the rows: at 20 Hz the phase step is exactly $180^\circ$, the limit of
readability, and is indistinguishable from $-180^\circ$ (the opposite dip at the
same steepness); at 30 Hz the apparent wavenumber flips sign, so a 1000 m/s
event reads as a 3000 m/s event dipping the *other* way; at 40 Hz the step is
zero, so the event reads as flat. Every one of these aliased events looks like a
plausible arrival on a section. Field survey design chooses

$$dx \le \frac{v_{\min}}{2\,f_{\max}}$$

from the slowest (steepest) event that must be recorded and the highest frequency
of interest — the same inequality as the temporal Nyquist relation, with different
symbols.

## 3. Leakage and the resolution relation

### 3.1 Where $df = 1/T$ comes from

A record of $N$ samples at spacing $dt$ spans $T = N\,dt$ and produces bins spaced

$$df = \frac{1}{N\,dt} = \frac{1}{T}.$$

Two tones can be distinguished only if they are separated by more than about one
bin, so the **resolution** of a spectral estimate is also $1/T$. The two numbers
$df$ (bin spacing) and $1/T$ (resolution) coincide for an unpadded transform and
that coincidence is the source of a great deal of confusion: padding changes the
former and not the latter, as
[01-10-04](./04-discrete-fourier.md) Section 6 demonstrates with numbers.

### 3.2 Scalloping loss: reading the nearest bin

A tone exactly on a bin needs one bin and is recovered exactly. A tone between
bins loses amplitude at the nearest bin and spreads across the band. The demo
measures this on a 256-sample record with $T = 1$ s, so $df = 1$ Hz:

| offset (bins) | nearest bin (Hz) | $2\lvert X\rvert/N$ there | $\lvert\mathrm{sinc}\rvert$ | error (dB) | interpolated peak |
|---|---|---|---|---|---|
| 0.00 | 40.000 | 1.000000 | 1.000000 | 0.00 | 1.000000 |
| 0.25 | 40.000 | 0.903087 | 0.900316 | $-0.89$ | 1.003910 |
| 0.50 | 40.000 | 0.634084 | 0.636620 | $-3.96$ | 1.000000 |
| 0.75 | 41.000 | 0.903076 | 0.900316 | $-0.89$ | 1.003909 |
| 1.00 | 41.000 | 1.000000 | 1.000000 | 0.00 | 1.000000 |

The worst case, a tone halfway between two bins, reads

$$\frac{2}{\pi} = 0.636620 \quad\Longrightarrow\quad -3.92\ \mathrm{dB},$$

the classical **scalloping loss** of a rectangular window. Two facts are easy to
get wrong here:

- The measured table gives $-3.96$ dB rather than $-3.92$ dB because at
  $f = 40.5$ Hz the *negative-frequency* lobe, one bin away in the 256-point
  transform, has not yet decayed to nothing and adds a little to the reading. The
  analytic value $2/\pi$ is the asymptotic one.
- **The energy is not lost.** It is spread over neighbouring bins, and the
  interpolated peak (the last column) recovers the amplitude to within 0.4% even
  at the worst offset. Interpolation fixes the amplitude; it does not fix the
  resolution.

### 3.3 Leakage from a trend: the damaging case

The most consequential leakage in geophysics is not from a tone but from a
**trend**, because a linear trend leaks as $1/f$ across the whole band. The demo
measures the fitted power law of a ramp's spectrum over bins 4–40:

| signal | fitted $\lvert X[k]\rvert$ exponent | mean $\lvert X\rvert$ over bins 8–40 |
|---|---|---|
| ramp alone | $-0.996$ | $8.482\times10^{0}$ |
| ramp after removing the best-fit line | $+0.000$ | $0.000\times10^{0}$ |

An exponent of $-0.996$ is $1/f$ to three figures: the ramp's leakage is
distributed, not localised, and it will masquerade as a red-noise background in
any spectral interpretation. Removing the straight line reduces it to round-off.

Detrending is not free, and the demo quantifies the cost. A sampled sinusoid is
not exactly orthogonal to a linear function over a finite record, so subtracting
a fitted line takes a little of the signal with it:

| signal | amplitude recovered at the tone's bin |
|---|---|
| tone alone (12 cycles in the record) | 1.000000 |
| tone + ramp | 0.947052 |
| tone + ramp, after detrending | 0.995794 |

The recovered amplitude after detrending is 0.9958 rather than 1.0000 — a 0.42%
bias — because the least-squares fit "explains" part of the tone as trend. That
overlap falls as $1/N$: for long records it is negligible; for short ones it is a
bias to be aware of. **Every processing step that removes something removes a
little of everything.**

## 4. Windowing

### 4.1 Why and what

The record is the true signal multiplied by a window. If the record were a boxcar
— which is what "no window" means — the measured spectrum is the true spectrum
convolved with a sinc whose sidelobes are only $-13.26$ dB down
([01-10-02](./02-fourier-transform.md) Section 3.2). A tapered window has lower
sidelobes, at the price of a wider main lobe. The demo measures both on a
4096-point window zero-padded to 16384, with the main-lobe width quoted in bins
of the *unpadded* transform:

| window | coherent gain | main lobe (bins) | peak sidelobe (dB) | worst sidelobe 8–30 bins (dB) |
|---|---|---|---|---|
| rectangular | 1.000000 | 2.00 | $-13.46$ | $-17.90$ |
| Hann | 0.500000 | 4.00 | $-32.17$ | $-32.17$ |
| Hamming | 0.540000 | 4.00 | $-42.68$ | $-42.68$ |
| Blackman | 0.420000 | 6.00 | $-58.24$ | $-58.24$ |

The measured peak sidelobes reproduce the values conventionally quoted for these
windows (−13.3, −31.5, −42.7, −58.1 dB) to within a fraction of a decibel.

**The coherent gain must be divided out.** A Hann window halves every amplitude
(gain 0.500000) and a Blackman window scales it by 0.42; forgetting this is a
silent 6 dB error in amplitudes and 12 dB in power. The coherent gain is simply
the mean of the window's samples, which is why it is exactly $1/2$ for Hann and
exactly $0.54$ for Hamming.

**Both good properties cannot be had.** The rectangular window has the narrowest
main lobe and the worst sidelobes; Blackman the reverse. Hamming's *first*
sidelobe is lower than Hann's, but its far sidelobes decay more slowly — visible
in the last column of the table, which is the worst sidelobe between 8 and 30
bins away.

### 4.2 What a window is worth, in dynamic range

The demo places a unit-amplitude strong tone at bin 100.35 — deliberately off the
bin grid so that it leaks — and measures the strong tone's own spectrum at the
position of a weak tone some bins away. The weak-tone threshold is found by
scanning the amplitude until the local peak reaches twice the leakage floor (a
6 dB criterion):

**Separation 3 bins** — inside the main lobe of the wider windows:

| window | floor (relative to peak) | floor (dB) | weakest detectable $a$ |
|---|---|---|---|
| rectangular | $2.122\times10^{-1}$ | $-13.5$ | $5.670\times10^{-1}$ |
| Hann | $1.081\times10^{-1}$ | $-19.3$ | $1.987\times10^{-1}$ |
| Hamming | $6.567\times10^{-2}$ | $-23.7$ | $1.357\times10^{-1}$ |
| Blackman | $2.354\times10^{-1}$ | $-12.6$ | $5.155\times10^{-1}$ |

At three bins, **Blackman is the worst of the four**, because its own main lobe is
six bins wide and covers the weak tone's position. A wide main lobe hides a weak
nearby event just as surely as a high sidelobe does.

**Separation 8 bins** — clear of every main lobe:

| window | floor (relative to peak) | floor (dB) | weakest detectable $a$ |
|---|---|---|---|
| rectangular | $5.269\times10^{-2}$ | $-25.6$ | $1.234\times10^{-1}$ |
| Hann | $1.069\times10^{-3}$ | $-59.4$ | $1.539\times10^{-3}$ |
| Hamming | $6.051\times10^{-3}$ | $-44.4$ | $9.412\times10^{-3}$ |
| Blackman | $3.902\times10^{-4}$ | $-68.2$ | $5.394\times10^{-4}$ |

Now the ordering follows the sidelobe table, and a Hann window improves the
weak-tone threshold by nearly two orders of magnitude over no window at all. The
practical rule: **windowing helps when the interference is a sidelobe and hurts
when it is the main lobe.**

### 4.3 Resolution is a threshold choice

Finally, the demo defines resolution operationally and measures it. Two equal
tones are *resolved* when the spectrum shows two local maxima, each within 1.5
bins of a tone frequency, separated by a valley at least 3 dB below the lower
peak; the separation is scanned in steps of $0.1/T$ to find the threshold.

| window | threshold ($\times 1/T$) | valley depth there (dB) | main lobe (bins) |
|---|---|---|---|
| rectangular | 1.2 | $-12.1$ | 2.0 |
| Hann | 2.3 | $-3.0$ | 4.0 |
| Hamming | 2.2 | $-3.5$ | 4.0 |
| Blackman | 2.5 | $-4.2$ | 6.0 |

The rectangular window resolves at about $1.2/T$, close to the $1/T$ of the
familiar Rayleigh criterion; a tapered window costs resolution in proportion to
its wider main lobe, and Blackman needs $2.5/T$. **Resolution is therefore not a
property of the data alone: it is the separation at which a stated criterion is
met, with a stated window.** A resolution claim without the window and the
threshold is not a claim.

## 5. Python demonstration

[`code/aliasing_leakage_demo.py`](./code/aliasing_leakage_demo.py) produces every
table above and runs in a few seconds:

```text
python3 code/aliasing_leakage_demo.py
```

Three implementation points.

1. **The apparent frequencies in Section 2 are measured**, by finding the peak of
   a zero-padded spectrum of the sampled data — not computed from the formula and
   presented as if measured. That is the difference between demonstrating aliasing
   and restating it.
2. **The tapering in the zero-padding and leakage tests is deliberate and
   labelled.** The two-tone tests use a Hann taper so that leakage does not
   confuse the resolution question; the leakage tests use no taper so that
   leakage is the subject.
3. **The window table's main-lobe width is quoted in unpadded bins**
   ($\mathrm{width} = 2k_{\text{null}}N/N_{\text{pad}}$). Quoting it in padded bins
   makes the width depend on an arbitrary parameter of the analysis rather than on
   the window.

## 6. Common mistakes

1. **Treating aliasing as obvious.** It produces plausible dips, plausible
   frequencies and plausible amplitudes. It is detected by comparing *adjacent*
   traces (a dip that changes direction between adjacent traces is aliased), not
   by looking at the section.
2. **Confusing bin spacing with resolution.** Padding changes $df$; only record
   length changes $1/T$.
3. **Quoting a resolution without the window and the criterion.** Section 4.3
   gives four different answers for one dataset.
4. **Forgetting the coherent gain.** An amplitude spectrum computed from a Hann-
   windowed record is half what it should be, consistently, and the error is
   invisible without a check against a known input.
5. **Choosing a window to make the plot look clean.** The trade is quantifiable
   (Section 4.2); make it deliberately.
6. **Detrending without noting what was removed.** A fitted line removes a little
   of a genuine long-period signal, and a higher-order detrend removes more.
7. **Applying an anti-alias filter after sampling.** It must be analogue and
   before the sampler; nothing downstream can undo the fold.
8. **Assuming a high sample rate fixes everything.** It fixes aliasing; it does
   nothing about leakage, resolution, or the noise the sensor picked up.

## 7. Real-world applications

- **Survey design.** The spatial Nyquist relation $dx \le v_{\min}/(2f_{\max})$
  sets receiver spacing from the steepest event of interest; the temporal one
  sets the sample interval. Both are the same inequality, and both are negotiated
  against cost — which is why aliased ground roll is common in legacy data.
- **Anti-alias filtering in acquisition.** Field systems apply analogue
  low-pass filters before digitising; their corner frequency and slope determine
  how much aliased noise reaches the record.
- **Windowing in seismic processing.** Autocorrelation windows, spectral
  whitening and deconvolution design all use tapers to control the leakage that
  would otherwise bias the estimated operator.
- **Tidal and gravity analysis of short records.** The Rayleigh criterion and the
  noise gain of [01-10-01](./01-fourier-series.md) are the same statement as
  $df = 1/T$: a short record cannot separate close constituents, and its noise
  gain is high.
- **Climate time series.** Detrending and windowing before spectral estimation
  are mandatory: the $\sim 1/f$ leakage of a trend dominates the low-frequency end
  of any temperature, sea-level or ice-volume spectrum, and the seasonal cycle is
  a tone that sits between bins unless the record is an integer number of years.
- **Satellite gravity and topography spectra.** The along-track sampling of an
  altimeter sets a Nyquist wavelength, and the finite width of the filtering
  applied to the altimeter data sets a resolution; both must be reported for a
  spectrum to be interpretable — the subject of
  [01-10-08](./08-spatial-spectra.md).

## 8. Further reading

- **Harris, F. J. (1978). On the use of windows for harmonic analysis with the
  discrete Fourier transform. *Proceedings of the IEEE*, 66(1), 51–83.**
  Level: advanced. The definitive window reference: definitions, coherent gain,
  equivalent noise bandwidth, and measured sidelobe levels. Every number in
  Section 4 can be found or derived from it.
- **Bracewell, R. N. (2000). *The Fourier Transform and Its Applications*
  (3rd ed.). McGraw-Hill.** Chapter 18. Level: intermediate. The sampling theorem
  and aliasing, with the classical proof through the replicated spectrum.
- **Oppenheim, A. V. & Schafer, R. W. (2010). *Discrete-Time Signal Processing*
  (3rd ed.). Pearson.** Chapters 4 and 10. Level: advanced. The rigorous
  statement that a band-limited signal is determined by its samples, and the
  theory of the DFT's leakage.
- **Yilmaz, Ö. (2001). *Seismic Data Analysis*. Society of Exploration
  Geophysicists.** Chapter 1 and the sections on deconvolution. Level:
  intermediate to advanced. Aliasing and windowing as they appear in field
  processing, including the "aliased ground roll" diagnostic.
- **Vermeer, G. J. O. (2012). *3-D Seismic Survey Design* (2nd ed.). Society of
  Exploration Geophysicists.** Level: advanced. Where the spatial Nyquist
  relation of Section 2.3 becomes an engineering discipline.
- **Pugh, D. T. (1987). *Tides, Surges and Mean Sea-Level*. Wiley.** Level:
  intermediate. The Rayleigh criterion and the practical consequences of a
  short tide-gauge record.

> Note on citations: bibliographic details above are given so you can locate the
> works. This repository does not host or reproduce copyrighted text, and you
> should confirm current availability and editions through your library before
> citing them.

## 9. Related lessons

- [04 Discrete Fourier Transform and the FFT](./04-discrete-fourier.md) — the
  bin geometry this lesson's aliasing and leakage live in.
- [06 Hilbert Transform, Analytic Signal and Instantaneous Phase](./06-hilbert-transform.md) —
  which of the aliasing and windowing effects survive into attribute analysis.
- [07 Two-Dimensional Fourier Analysis and Wavenumber Filtering](./07-2d-fourier.md) —
  spatial aliasing and two-dimensional windows, the practical home of Section 2.3.
- [08 Power Spectra, Admittance and Coherence of Geophysical Fields](./08-spatial-spectra.md) —
  where segment averaging makes the periodogram's scatter manageable.
- [01 Fourier Series and Periodic Decomposition](./01-fourier-series.md) — the
  Rayleigh criterion as it appears in tidal analysis.
- [20-signal-processing](../../20-signal-processing/README.md) — the module that
  turns these results into processing sequences.
- [17-remote-sensing-gis](../../17-remote-sensing-gis/README.md) — sampling and
  resolution as they appear in image data.

## 10. Exercises

Ten graded exercises, with full worked solutions, are in
[`exercises/05-windowing-aliasing-exercises.md`](./exercises/05-windowing-aliasing-exercises.md).
Solutions: [`exercises/05-windowing-aliasing-solutions.md`](./exercises/05-windowing-aliasing-solutions.md).

## Self-assessment checklist

- [ ] I can state the Nyquist relation and compute the apparent frequency of an
      aliased tone with the fold formula.
- [ ] I can explain why several different frequencies produce identical samples.
- [ ] I can use the spatial form $dx \le v_{\min}/(2f_{\max})$ to design a
      receiver spacing, and recognise aliasing from a dip reversal.
- [ ] I can derive $df = 1/T$ and distinguish bin spacing from resolution.
- [ ] I can quote the scalloping loss and explain why interpolation fixes
      amplitude but not resolution.
- [ ] I can explain the $1/f$ leakage of a trend and state what detrending costs.
- [ ] I can tabulate the standard windows with their coherent gain, main-lobe
      width and sidelobe levels, and choose between them on quantitative grounds.
- [ ] I can define resolution as a threshold, measure it, and state the window and
      criterion with any resolution claim.
