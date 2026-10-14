---
id: 20-05-03
title: "Colour of Noise: White, Pink, Red and Geophysical Examples"
level: doctoral
prereqs: ["20-05-02", "20-05-01"]
tags: [signal-processing, noise, noise-colour, power-law-spectrum, long-memory, hurst-exponent]
---

# Colour of Noise: White, Pink, Red and Geophysical Examples

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** coloured noise by a power-law PSD $S(f) \propto f^{-\alpha}$ and
   classify white ($\alpha=0$), pink ($\alpha=1$) and red ($\alpha=2$) noise.
2. **Derive** the octave-band energy ratio $2^{1-\alpha}$ and use it to identify
   a colour from band powers alone.
3. **Derive** the structure-function exponent $2H$ for fractional Brownian
   motion and relate it to $\alpha$ through $\alpha = 2H+1$.
4. **Measure** the spectral slope, the octave ratios and the structure function
   on synthetic series, and state each result with its scatter.
5. **Explain** why the effective sample size is not $T/\tau_{\text{int}}$ for
   $\alpha \ge 1$, and **quantify** the resulting error in a standard error.
6. **Decide** whether a stated "noise reduction" claim is achievable on a record
   of a given colour.

All models and data in this module are **SYNTHETIC**. The coloured series below
are filters applied to generated white noise. The geophysical situations
mentioned in Section 6 are described qualitatively; no measured spectrum, band
limit or published value is quoted.

## Prerequisites

- [20-05-02 Autocorrelation, Power Spectral Density and Wiener-Khinchin](02-autocorrelation-spectra.md) —
  the PSD and autocorrelation are a Fourier pair.
- [20-05-01 Stochastic Processes, Stationarity and Ergodicity](01-stochastic-processes.md) —
  stationarity, the integrated correlation time and effective sample size.
- [20-02-02 Spectral Estimation: Periodogram, Welch, Multitaper](../02-fourier-and-spectral-analysis/02-spectral-estimation.md) —
  the estimators used to measure a slope.

## 1. Intuition: not all noise is white

White noise is the default mental model: uncorrelated samples, a flat spectrum,
and an error bar that falls as $1/\sqrt{N}$. Real geophysical records are rarely
white. Their spectra are usually **power laws**, $S(f) \propto f^{-\alpha}$, with
power concentrated at low frequencies. The exponent $\alpha$ is the *colour* of
the noise, and it controls almost everything about how a record must be
analysed: how fast an average converges, whether a long record is a stronger
measurement or just a longer excursion, and whether the signal-to-noise ratio can
be improved by averaging at all.

The lesson is deliberately blunt about the last point. For $\alpha \ge 1$ the
integrated correlation time diverges, so the comfortable formula
$\operatorname{Var}(\bar x) = \sigma^{2}/N_{\text{eff}}$ from
[lesson 05-01](01-stochastic-processes.md) has no finite $\tau_{\text{int}}$ to
use. The honest statement is then that the record length itself becomes part of
the answer.

## 2. Precise definitions

### 2.1 Power-law spectra

Define the **spectral index** $\alpha$ by

$$S(f) = S_0 \left(\frac{f}{f_0}\right)^{-\alpha},
\qquad 0 < \alpha < 3 \ \text{typically},$$

over a band bounded below by $f_{\min}$ and above by Nyquist. The conventional
names are:

| name | $\alpha$ | spectrum | behaviour of the process |
|---|---|---|---|
| white | 0 | flat | stationary, finite $\tau_{\text{int}}$ |
| pink / flicker | 1 | $1/f$ | borderline; long memory, $\tau_{\text{int}}$ logarithmic |
| red / Brownian | 2 | $1/f^{2}$ | non-stationary; a random walk |

A power law with $0<\alpha<2$ and a finite low-frequency cut-off defines
**fractional Brownian motion (fBm)** and its stationary increments; its
**Hurst exponent** $H$ satisfies

$$\boxed{\;\alpha = 2H + 1, \qquad 0 < H < 1 .\;}$$

$H = 1/2$ is ordinary Brownian motion ($\alpha = 2$); $H > 1/2$ is
*persistent* (a large excursion is more likely to be followed by another),
$H < 1/2$ is *anti-persistent*. $H$ and $\alpha$ are two names for the same
number, and every statement below can be made in either.

### 2.2 Octave-band energy

Because a power law is scale-free, the energy in successive **octave bands**
$[f_0, 2f_0)$, $[2f_0, 4f_0)$, ... is a clean diagnostic. For
$S \propto f^{-\alpha}$,

$$\int_{f_0}^{2f_0} S(f)\,\mathrm{d}f \propto
\left[f^{1-\alpha}\right]_{f_0}^{2f_0}
= f_0^{1-\alpha}\left(2^{1-\alpha} - 1\right),$$

so the ratio of successive octave-band powers is

$$\frac{P_{\text{next}}}{P_{\text{current}}} = 2^{\,1-\alpha}.$$

That is the *definition* of pink noise in the audio world: $\alpha = 1$ gives a
ratio of $1$, i.e. equal energy per octave.

### 2.3 The structure function

The **structure function** (or variogram) at separation $T$ is

$$D(T) = \mathbb{E}\!\left[\left(X(t+T) - X(t)\right)^{2}\right].$$

For stationary white noise, $D(T) = 2\sigma^{2}$ for every $T$: excursions do
not grow with the timescale. For fBm the increments are stationary and

$$D(T) \propto T^{2H} = T^{\alpha-1},$$

so $D$ grows linearly for red noise ($\alpha=2$, $H=1/2$) and only
logarithmically at the pink boundary. This single scaling exponent is enough to
identify the colour without any spectral estimation at all.

### 2.4 Why a "colour" needs a band

A pure power law cannot extend to $f=0$: for $\alpha \ge 1$ the integral
$\int_0 S \,\mathrm{d}f$ diverges, so the variance is infinite and no stationary
process exists. Every physical coloured noise is therefore **band-limited**: it
has a lower cut-off, set by the record length or by a physical timescale. The
measurement is a statement about the band you observed, and extrapolating the
slope outside it is an assumption.

## 3. Worked examples from the demonstration

The demonstration imposes the power law by filtering white noise in the frequency
domain with the shape $(f/f_1)^{-\alpha/2}$ and zeroing the DC bin, on records of
65 536 samples at 100 Hz.

### 3.1 Spectral slope

A Welch PSD with 4096-sample segments, fitted over 0.5–40 Hz in log–log space,
returns

| colour | imposed $\alpha$ | measured slope of $\log_{10}S$ vs $\log_{10}f$ |
|---|---|---|
| white | 0.0 | $-0.009$ |
| pink | 1.0 | $-1.004$ |
| red | 2.0 | $-1.999$ |

A single realisation reproduces the imposed exponent to within a few thousandths
because the whole band is used; the residual is estimator scatter, not bias.

### 3.2 Octave-band ratios

The octave-band powers over $[1,2)$, $[2,4)$, $[4,8)$, $[8,16)$, $[16,32)$ Hz and
their successive ratios are:

| colour | successive ratios | predicted $2^{1-\alpha}$ |
|---|---|---|
| white | 1.963, 1.997, 1.915, 2.014 | 2.000 |
| pink | 0.999, 0.913, 1.041, 0.980 | 1.000 |
| red | 0.469, 0.518, 0.491, 0.494 | 0.500 |

White noise doubles its energy per octave, red noise halves it, and pink noise
holds it constant. An analyst with two octave-band powers and no spectrum
estimator can classify the noise with this one number: $2^{1-\alpha}$.

### 3.3 Structure function

Averaging $D(T)$ over 100 realisations of 16 384-sample records:

| colour | $D(4)$ | $D(16)$ | $D(64)$ | $D(256)$ | $D(1024)$ | slope |
|---|---|---|---|---|---|---|
| white | 2.00 | 2.00 | 2.00 | 2.00 | 2.00 | $-0.000$ |
| pink | 0.000761 | 0.0011 | 0.00144 | 0.00178 | 0.00213 | $+0.183$ |
| red | $5.59\times10^{-7}$ | $2.32\times10^{-6}$ | $9.27\times10^{-6}$ | $3.7\times10^{-5}$ | $1.42\times10^{-4}$ | $+0.999$ |

The white value is exactly $2\sigma^{2} = 2$ (the driving noise has unit
variance). The red slope is $0.999$, i.e. $2H \approx 1$ as required by
$H = 1/2$. The pink slope of $0.183$ over this range is the finite-range
signature of logarithmic growth: a fixed slope does not describe it, and fitting
one over a wider band would give a different number. **Report the range with the
slope.**

### 3.4 The consequence for a mean

For a stationary record the standard error of the mean is
$\sigma/\sqrt{N_{\text{eff}}}$ with
$N_{\text{eff}} = T/\tau_{\text{int}}$. The demonstration computes
$\tau_{\text{int}}$ from the observed autocorrelation of a 4096-sample record:

| colour | naive $\sigma/\sqrt{n}$ | $\tau_{\text{int}}$ (samples) | corrected | ratio |
|---|---|---|---|---|
| white | 0.0154 | 1.0 | 0.0153 | 0.99× |
| pink | 0.0003 | 389.9 | 0.0051 | 19.75× |
| red | $3\times10^{-5}$ | 617.7 | 0.0005 | 24.85× |

The corrected value is larger by an order of magnitude. Two cautions follow.
First, the naive answer is not merely inaccurate, it is *wrong in kind*: it
assumes that more samples always buy more information, which is false when the
successive samples carry the same low-frequency excursion. Second, for
$\alpha \ge 1$ the number $\tau_{\text{int}}$ itself depends on the band, so the
corrected value must be reported as conditional on the record length. This is the
`1/f` statistics used in Allan-variance analysis of clocks and in the noise
models of geodetic time series (see
[08-03 Geodetic Time Series](../08-timeseries-analysis-geophysics/03-geodetic-time-series.md)).

## 4. Worked example: how much can averaging help?

A monitoring survey stacks $M$ independent records of the same target to reduce
noise. For white noise the stacked standard error falls as $1/\sqrt{M}$. For
red noise the records are all wandering with the same statistics, and their
low-frequency content does not cancel: averaging $M$ such records reduces the
*random* part as $1/\sqrt{M}$ but leaves the common low-frequency wander. The
demonstration's structure-function table makes the size explicit — with the same
number of samples, the red record's excursions at the longest lag are
$1.42\times10^{-4}/(5.59\times10^{-7}) = 254$ times larger than at the shortest
lag, against a factor of $1$ for white noise. Stacking reduces the high-frequency
part of the error while the low-frequency part survives.

The practical rule: **before promising a noise reduction factor, measure
$\alpha$.** If $\alpha \gtrsim 1$, state the band and the record length over
which the claim holds, and include a low-frequency budget. Noise reduction
strategies for exactly this situation are the subject of
[04 Noise Reduction Strategies in Practice](04-noise-reduction.md).

## 5. Assumptions and regime of validity

1. **A single power law over the observed band.** Many real spectra have several
   slopes (white below some corner, then a power law, then a roll-off at the
   sensor's corner). Fitting one exponent to the whole span reports an average
   that describes neither regime; fit within a stated band.
2. **Enough dynamic range for a slope.** Ten decibels of spectral dynamic range
   and one decade of frequency is the practical minimum; the demonstration uses
   more than $1.5$ decades.
3. **Stationarity of the increments** (for fBm). Estimating $H$ from $D(T)$
   assumes the increment statistics do not drift. A change of regime violates it
   and is the subject of change-point detection.
4. **The DC bin is treated explicitly.** Zeroing it removes the record mean; the
   measured low-frequency power then depends on that choice. State how the mean
   and any trend were removed.
5. **The band-limited nature is part of the answer.** $H$ measured over one band
   is a statement about that band. Flicker noise is scale-free only in the range
   where the power law holds.

## 6. Geophysical situations, qualitatively

The following are *qualitative* descriptions of where the three colours appear.
No numbers are quoted, and the numbers in this lesson come only from the
synthetic demonstration.

- **White-like.** Sensor self-noise and quantisation noise, whose spectra are
  approximately flat across their band, behave like the $\alpha \approx 0$ case.
  They are the easiest to reduce by averaging, and the naive error formula is the
  right one.
- **Pink-like.** Long-period instrument drift, tidal leakage into broadband
  channels, and the low-frequency background of geodetic position series often
  show approximately $1/f$ behaviour. The defining signature is the flat octave
  band power, not the value of any single spectral bin.
- **Red-like.** Random-walk processes — an unconstrained position estimate, an
  integrated velocity, a slowly migrating baseline — show $1/f^{2}$ spectra and
  a structure function growing linearly with lag. They are the reason a
  monitoring series needs a trend model rather than a longer average.
- **Ocean and atmospheric forcing** generally produces a band-limited,
  coloured, non-stationary background whose spectrum is *not* a single power law;
  treating it as one is the commonest error in the class.

The lesson's own numbers are the way to calibrate intuition; the geophysical
attribution requires the actual data and its metadata, and is a research task.

## 7. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| spectral index | $\alpha$ | dimensionless | slope of log-log PSD |
| octave ratio | $2^{1-\alpha}$ | dimensionless | ratio of two integrals |
| Hurst exponent | $H$ | dimensionless | $\alpha = 2H+1$ |
| structure function | $D(T)$ | (signal unit)$^{2}$ | a variance |
| structure slope | $2H$ | dimensionless | log-log slope |

The structure function is a variance, so its square root is an rms displacement;
confusing $D(T)$ with a displacement in the same unit is a factor-of-$\sqrt{\cdot}$
error.

## 8. Python demonstration

[`code/noise_colour_demo.py`](./code/noise_colour_demo.py) generates the series
and prints every number above:

1. shows the spectral-shaping construction and its PSD power law;
2. measures the spectral slope against the imposed exponent;
3. measures octave-band ratios against $2^{1-\alpha}$;
4. measures the structure function and its slope, with scatter over 100
   realisations;
5. shows the inflated standard error of a mean on a coloured record.

```bash
cd 20-signal-processing/05-noise-and-random-signals/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python noise_colour_demo.py
```

## 9. Exercises

[`exercises/03-noise-colour-exercises.md`](./exercises/03-noise-colour-exercises.md)
and
[`exercises/03-noise-colour-solutions.md`](./exercises/03-noise-colour-solutions.md).
The ★★★ problem asks you to design a colour-classification procedure and state
its failure mode.

## 10. Mastery checkpoint

1. A spectrum measured over two decades has a band-power ratio of $2^{1-\alpha} =
   0.5$ between successive octaves. State $\alpha$, $H$, and the name of the
   colour.
2. A structure function grows as $D(T) \propto T^{1}$. State $H$ and $\alpha$,
   and say in one sentence what an analyst should conclude about averaging.
3. A colleague reports a standard error $0.02$ on a mean from a record with an
   observed $\tau_{\text{int}}$ of 400 samples over 4000 samples. Correct the
   number.
4. Explain why a pure $1/f$ process cannot have finite variance without a
   low-frequency cut-off.

## 11. Common pitfalls

1. **Assuming $1/\sqrt{N}$ applies to every record.** It assumes white noise;
   measure $\tau_{\text{int}}$ or $\alpha$ first.
2. **Fitting one slope over two different regimes.** Report the band with the
   exponent, always.
3. **Calling a record "pink" because the low-frequency PSD is large.** Pink is
   defined by the *slope*, not by the level; use the octave ratios or $\alpha$.
4. **Ignoring the low-frequency cut-off.** With no stated $f_{\min}$ the slope
   extrapolates to an infinite variance.
5. **Reporting a single realisation's slope as the result.** Slopes scatter;
   quote the ensemble or a confidence interval.

## 12. Related lessons

- [01 Stochastic Processes, Stationarity and Ergodicity](01-stochastic-processes.md) —
  why the random walk is the canonical non-stationary process.
- [02 Autocorrelation, Power Spectral Density and Wiener-Khinchin](02-autocorrelation-spectra.md) —
  the estimators used to measure the slope.
- [04 Noise Reduction Strategies in Practice](04-noise-reduction.md) — what to do
  once the colour is known.
- [08-03 Geodetic Time Series: Trends, Offsets, Noise Models](../08-timeseries-analysis-geophysics/03-geodetic-time-series.md) —
  coloured noise in deformation monitoring.
- [16-01 Climate Variability and Ocean–Atmosphere Coupling](../../16-atmosphere-climate/README.md) —
  the same spectra driven by physical forcing rather than by instrument noise.

## 13. Further reading

Titles are given so the works can be located; this repository does not host or
reproduce copyrighted text.

- **Beran, *Statistics for Long-Memory Processes*, Chapman & Hall, 1994.**
  Level: research. Estimation of $H$ and the consequences of long memory.
- **Priestley, *Spectral Analysis and Time Series*, Academic Press, 1981.**
  Level: graduate. Power-law spectra and their interpretation.
- **Percival & Walden, *Spectral Analysis for Physical Applications*, Cambridge
  University Press, 1993.** Level: graduate. Estimating power-law slopes
  without fooling yourself.
- **Mandelbrot & Van Ness, "Fractional Brownian motions, fractional noises and
  applications", *SIAM Review*, 1968.** Level: research. The original fBm
  construction behind the $H$–$\alpha$ relation.

## 14. Self-assessment checklist

- [ ] I can name white, pink and red noise by their exponents.
- [ ] I can derive and use the octave ratio $2^{1-\alpha}$.
- [ ] I can relate $\alpha$, $H$ and the structure-function slope.
- [ ] I can measure a slope and state its band and scatter.
- [ ] I can explain why $N_{\text{eff}}$ is not honest for $\alpha \ge 1$.
- [ ] I can state when averaging will and will not reduce an error.
