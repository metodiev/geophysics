---
id: 25-02-03
title: "Project: Fourier Analysis of a Geophysical Signal"
level: intermediate
prereqs: ["25-01-01", "20-02-01", "20-02-02", "20-02-03"]
estimated_minutes: 150
tags: [projects, fourier, spectral-analysis, leakage, teaching]
---

# Project: Fourier Analysis of a Geophysical Signal

## Learning objectives

1. **Compute** a one-sided power spectral density with the correct normalisation and **state**
 its unit in terms of the signal's unit.
2. **Verify** the normalisation by Parseval's theorem, and **interpret** a ratio that is not
 exactly 1.
3. **Determine** the spectral resolution from the record length and **state** the frequency and
 period limits it imposes.
4. **Measure** the amplitude of a spectral line from the peak bin and from a lobe sum, and
 **explain** why the two differ by $20\%$.
5. **Quantify** leakage for a rectangular and a Hann window on a deliberately off-bin tone, and
 **state** the trade-off windowing buys.
6. **Calibrate** a detection threshold against a measured noise null rather than against a
 visual gap.

## Prerequisites

- [25-01-01 Project: Units, Conversions and First Scientific Plots](../01-beginner-projects/01-units-and-plotting.md) —
  the unit audit a spectrum must also pass.
- [20-02-01 Practical DFT/FFT: Normalisation, Units and Pitfalls](../../20-signal-processing/02-fourier-and-spectral-analysis/01-dft-fft-practice.md) —
  the transform and its conventions.
- [20-02-02 Spectral Estimation: Periodogram, Welch, Multitaper](../../20-signal-processing/02-fourier-and-spectral-analysis/02-spectral-estimation.md) —
  the estimator used here and its variance.
- [20-02-03 Window Functions and Spectral Leakage Control](../../20-signal-processing/02-fourier-and-spectral-analysis/03-windowing-advanced.md) —
  the window's leakage against its resolution cost.

## 1. The question

*Which frequencies are in this record, with what amplitude, and which of them are
real?*

A spectrum answers the first two parts mechanically and the third part not at
all. Every quantity a spectrum reports — amplitude, frequency, resolution — is a
*derived* quantity that inherits a choice of window, of record length and of
normalisation, and none of those choices announces itself in the output. The
project's deliverable therefore includes, for every peak, the resolution that
limits its frequency, the window that shaped its sidelobes, and the null that
decides whether it is a detection.

## 2. The data

**Synthetic signal.** $f_s = 1.0\ \mathrm{Hz}$, $N = 1024$ samples (1024 s), two
sinusoids at $0.050\ \mathrm{Hz}$ (amplitude 1.00) and $0.110\ \mathrm{Hz}$
(amplitude 0.50) in signal units, plus white noise of standard deviation 0.30.

**Real series for the project itself.** Hourly or daily station series are
available from the NOAA land-based station archive at
<https://www.ncei.noaa.gov/products/land-based-station>. The same estimator is
applied to them; the demonstration's signal is deliberate and noise-free in the
sense that its components are known exactly, which is what makes the measurement
errors measurable.

**Provenance.** SYNTHETIC. The true amplitudes (1.00, 0.50) and the true
frequencies are known by construction and are used only as a reference for the
estimator's error.

## 3. The project specification

**Steps.**

1. State $f_s$, $N$, the duration, the Nyquist frequency and the resolution
   $\Delta f = f_s/N$, and hence the frequency and period limits.
2. Compute the one-sided PSD with a Hann window, using
   $\mathrm{PSD} = 2|X|^{2}/(f_s \sum w^{2})$ away from DC and Nyquist.
3. Check Parseval: integrate the PSD over frequency and compare with the time
   series' variance; report the ratio and the expected variance.
4. Find the local maxima, take the two strongest separated by more than the main
   lobe width, and report each peak's frequency, its amplitude from the peak bin
   and from the lobe sum, and the resolution.
5. Repeat the amplitude measurement with a rectangular window and compare
   leakage on a deliberately off-bin tone.
6. Build a noise null: generate at least 200 pure-noise records, take the maximum
   PSD of each, and calibrate the 95th percentile as the detection threshold.
7. Write the report: the estimator, the window, the resolution, the peaks with
   amplitudes and units, and the threshold the peaks are compared with.

**Deliverable.** A spectrum plot with the resolution element drawn, a peak table,
a window comparison, and the calibrated threshold.

**Success criterion.** The PSD's unit is stated; Parseval's ratio is reported;
each peak's frequency is quoted with the resolution; each detection is quoted
against the measured threshold, not against a visual gap.

## 4. The estimator and its resolution

For a real record $x[n]$ with a window $w[n]$, the one-sided PSD estimate is

$$\widehat{S}(f_k) = \frac{2\,|X_k|^{2}}{f_s \sum_{n} w[n]^{2}},
\qquad
X_k = \sum_{n=0}^{N-1} x[n] w[n] e^{-2\pi i kn/N},$$

with the factor 2 dropped at $k = 0$ and at the Nyquist bin. Because
$|X_k|^{2}$ has the unit of (signal)$^{2}$ and $f_s$ the unit Hz, the PSD's unit
is **(signal unit)² per Hz** — for this project, signal-unit² Hz⁻¹, a spectral
*density* rather than a power.

The frequency grid is $f_k = k f_s/N$, so

$$\Delta f = \frac{f_s}{N} = \frac{1.0}{1024} = 0.000977\ \mathrm{Hz},$$

and the corresponding **period resolution** is $1/\Delta f = 1024\ \mathrm{s}$
at the longest period. The Nyquist frequency is $f_s/2 = 0.5\ \mathrm{Hz}$;
periods shorter than $2/f_s = 2\ \mathrm{s}$ are unrepresentable. Two peaks
separated by less than $\Delta f$ cannot be resolved, and **zero-padding the
record does not help** — it interpolates the same information onto a finer grid.

## 5. Normalisation and Parseval's check

A correct PSD must integrate to the variance. For a discretely sampled signal,

$$\int_0^{f_s/2} \widehat{S}(f)\,\mathrm{d}f \;\approx\;
\sum_k \widehat{S}(f_k)\,\Delta f \;\longrightarrow\; \operatorname{Var}(x).$$

The demonstration measures a time-series variance of
$0.729328\ \text{unit}^{2}$ and a PSD integral of $0.744887\ \text{unit}^{2}$, a
ratio of $1.0213$. The expected variance,
$A_1^{2}/2 + A_2^{2}/2 + \sigma^{2} = 0.5 + 0.125 + 0.09 = 0.715$, agrees with
the measurement to $2\%$.

A ratio within a few percent is the *correct* outcome, and the reason is worth
stating: the Hann window's main lobe spreads each line over three bins, so the
discrete sum slightly over- or under-counts depending on where the line falls
relative to a bin. A ratio of $1.02$ means the normalisation is right; a ratio of
$2$ means a factor of two is missing (usually the one-sided doubling), and a
ratio of $100$ usually means the window's power gain was neglected.

## 6. Amplitudes, and why the peak bin is not the amplitude

For a sinusoid of amplitude $A$ the PSD has a line whose integral is $A^{2}/2$.
The demonstration measures the first component in two ways:

| measurement | value (signal unit) | true |
|---|---|---|
| from the single peak bin, $\sqrt{2\,\widehat{S}\,\Delta f}$ | $0.8042$ | $1.00$ |
| from the five-bin lobe sum, $\sqrt{2\,\Delta f \sum_{\text{lobe}}\widehat{S}}$ | $1.0178$ | $1.00$ |

The single-bin value is **20% low** because the Hann window spreads the line's
power across three bins and the peak bin holds only about two thirds of it. The
lobe sum recovers $1.0178$, within $1.8\%$ of the truth — the residual is the
noise power inside the same band. The second component behaves identically:
$0.3943$ from the peak bin, $0.5265$ from the lobe, against a true $0.50$.

**The rule that follows: integrate the lobe, do not read the peak.** The size of
the error depends on the window and on where the line falls relative to a bin, so
it is not a constant that can be corrected by inspection.

## 7. Leakage, and what a window costs

A tone that does not fall on a bin drives every bin, and the pattern of the
spill is the window's squared amplitude spectrum. The demonstration uses a tone
at $0.1509\ \mathrm{Hz}$ — exactly half a bin between two grid points, the
worst case by construction — and measures the largest sidelobe relative to the
observed peak:

| window | largest sidelobe / peak | in dB |
|---|---|---|
| rectangular | $0.1101$ | $-9.6$ |
| Hann | $0.0008$ | $-30.9$ |

The Hann window suppresses the sidelobe by **$21.3\ \mathrm{dB}$**, a factor of
138 in power. It pays for this with a main lobe twice as wide, so two lines closer
than about $2\Delta f$ merge — the classic leakage-versus-resolution trade.

The practical consequence is that an **unwindowed periodogram invents neighbours**
at the $-10\ \mathrm{dB}$ level, which is exactly the level at which a small real
peak can hide. A rectangular window is defensible only for a signal that is
exactly periodic in the record, which measured data are not.

## 8. Detection needs a null

A peak's height means nothing without a distribution to compare it with. The
demonstration generates 200 pure-noise records of the same length and window, takes
each one's maximum PSD, and reports the 95th percentile:

$$\text{threshold}_{95} = 1.6216\ \text{unit}^{2}\,\mathrm{Hz^{-1}}.$$

The second component's PSD of $79.6003$ is **49.1 times** that threshold, so it
is a detection by a wide margin. Two cautions belong in the report:

1. **The maximum over all bins is the right statistic when you search all bins.**
   A threshold calibrated per-bin (the mean noise level) would be about
   $50$ times lower, and using it would report a false peak in roughly half of
   pure-noise records.
2. **Overlapping windows correlate the trials.** If the "200 null records" reuse
   the same data, the threshold is optimistic; they must be independent draws.

## 9. Failure modes and how to detect them

1. **A PSD whose integral is not the variance.** *Detect:* run Parseval; a ratio
   far from 1 is a normalisation error, not a physical result.
2. **An amplitude read from the peak bin.** *Detect:* compare the single-bin and
   lobe-sum amplitudes; the difference is the window's coherent gain, and it is
   $20\%$ here.
3. **A frequency quoted finer than $\Delta f$.** *Detect:* $0.0498\ \mathrm{Hz}$
   is a bin index; writing $0.04983$ claims resolution the record does not have.
4. **An unwindowed spectrum used for interpretation.** *Detect:* the $-10\
   \mathrm{dB}$ sidelobe.
5. **A peak with no null.** *Detect:* ask for the number of hypotheses searched
   and the threshold at the corresponding percentile.

## 10. Rubric

| Criterion | 4 — exemplary | 3 — competent | 2 — developing | 1 — incomplete |
|---|---|---|---|---|
| Metadata | $f_s$, $N$, duration, $\Delta f$, Nyquist, unit | $f_s$, $N$, unit | $f_s$ only | None |
| Normalisation | Parseval check with the ratio reported | Correct PSD | Unscaled spectrum | Arbitrary units |
| Peaks | Frequency, amplitude by lobe sum, resolution | Frequency and amplitude | Peak locations | Visual |
| Window | Leakage measured for two windows | Window applied | Rectangular only | Absent |
| Detection | Threshold from a stated null and percentile | Threshold stated | "Looks like a peak" | Absent |

## 11. Assumptions and regime of validity

1. **Stationarity.** A PSD assumes the frequency content does not change over the
   record; a trending or transient series needs a time-frequency representation.
2. **Linearity and no aliasing.** A tone above the Nyquist frequency appears
   folded into the band as a genuine-looking peak.
3. **The noise is not the signal.** Parseval holds for any record, but the
   *interpretation* of a peak as a periodic component requires that the record is
   long compared with the period — here $1024$ s for a $20$ s period, which is
   ample.
4. **One realisation.** The periodogram of one record has a variance of about
   $100\%$ per bin, so peak heights scatter; averaging (Welch) or a multitaper
   estimate is required for a stable amplitude.
5. **Leakage is a property of the window, not of the data.** The $-9.6$ and
   $-30.9\ \mathrm{dB}$ numbers are predictions of the window, and they hold
   whatever the record is.

## The honest summary

One estimator, three checks. The PSD integrates to within $2.1\%$ of the
variance ($1.0213$ against an expected $0.715\ \text{unit}^{2}$, measured
$0.729328$); the line amplitudes come out as $1.0178$ and $0.5265$ against true
$1.00$ and $0.50$ when the lobe is summed and $0.8042$ and $0.3943$ when only the
peak bin is read; and the Hann window suppresses the worst-case sidelobe from
$-9.6$ to $-30.9\ \mathrm{dB}$ at the cost of a main lobe twice as wide. The
transferable discipline is that a spectrum is a *derived* quantity: it must be
normalised, checked against Parseval, windowed with the trade stated, and its
peaks tested against a null. The demonstration's own second peak clears its
threshold by a factor of $49.1$, which is what a defensible detection looks
like.

## Python demonstration

[`code/fourier_analysis_signals_demo.py`](./code/fourier_analysis_signals_demo.py) prints every number quoted above, writes no files,
uses no network and exits 0:

```bash
cd 25-projects-capstone/02-intermediate-projects/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python fourier_analysis_signals_demo.py
```

It is seeded with `np.random.default_rng(20261014)` and runs in under a second.
## Exercises

Graded problems and worked solutions are in
[`exercises/03-fourier-analysis-signals-exercises.md`](./exercises/03-fourier-analysis-signals-exercises.md)
and
[`exercises/03-fourier-analysis-signals-solutions.md`](./exercises/03-fourier-analysis-signals-solutions.md).
The ★★★ item asks you to design a detection procedure with a measured false-positive
rate, not to compute one more spectrum.

## Mastery checkpoint

Without notes:

1. State the resolution of a 4096-s record sampled at 1 Hz, and the longest period
   it can resolve.
2. A PSD integrates to twice the signal's variance. Name the missing factor and
   where it belongs.
3. A line's PSD peak bin reads $A = 0.80$ while the true amplitude is $1.00$. Give
   the most likely cause and the fix.
4. Explain in one sentence why a threshold set per-bin is wrong when you search
   the whole spectrum for the largest peak.

## Common pitfalls

1. **Treating a spectrum as a property of the data.** It depends on the window, the trend removal and the record length; the same series gives different peaks.
2. **Reading a peak with no noise reference.** A periodogram peak is a statistic, and its significance requires the null distribution of red noise.
3. **Forgetting the sampling rate.** Every frequency above the Nyquist frequency is aliased, and the aliased peak looks exactly like a real one.
4. **Detrending with a straight line when the series is a random walk.** The trend removal absorbs the low-frequency power that the null would predict.
5. **Comparing amplitude spectra across different windows.** Window normalisation, not the physics, sets the level.

## Where this is used

The same estimator and the same checks underpin every spectral claim later in the
curriculum: the tide and climate spectra of
[20-08-02](../../20-signal-processing/08-timeseries-analysis-geophysics/02-spectral-analysis-tides.md),
the noise-colour measurements of
[20-05-03](../../20-signal-processing/05-noise-and-random-signals/03-noise-colour.md),
and the trend-attribution project of
[25-03-04](../03-advanced-projects/04-climate-data-analysis-project.md). In
professional practice the leakage and detection checks are the difference
between a spectral peak that survives review and one that is re-derived as
window artefacts.

## Related lessons

- [20-05-02 Autocorrelation, Power Spectral Density and Wiener-Khinchin](../../20-signal-processing/05-noise-and-random-signals/02-autocorrelation-spectra.md) —
  the same information viewed in the lag domain.
- [20-02-04 Cross-Spectra, Coherence and Phase Estimation](../../20-signal-processing/02-fourier-and-spectral-analysis/04-cross-spectra-coherence.md) —
  what changes when two series are compared.
- [20-02-05 Time-Frequency Analysis: STFT, Wavelets, Spectrograms](../../20-signal-processing/02-fourier-and-spectral-analysis/05-time-frequency.md) —
  the remedy when the record is not stationary.
- [25-03-04 Project: Climate Data Analysis and Trend Attribution](../03-advanced-projects/04-climate-data-analysis-project.md) —
  spectra and trends on a real climate series.

## Self-assessment checklist

- [ ] I can state a PSD's unit and its resolution for given $f_s$ and $N$.
- [ ] I can run and interpret a Parseval check.
- [ ] I can measure a line's amplitude by integrating its lobe.
- [ ] I can measure leakage for two windows and state the trade.
- [ ] I can build a noise null and calibrate a threshold percentile.
- [ ] I can name the four common defects of a published spectrum.
