---
id: 20-08-02
title: "Tidal Harmonic Analysis and Prediction"
level: doctoral
prereqs: ["20-08-01", "20-02-02", "20-01-05"]
tags: [signal-processing, time-series, tides, harmonic-analysis, rayleigh-criterion, aliasing]
---

# Tidal Harmonic Analysis and Prediction

**All models and data in this module are SYNTHETIC.** The tide analysed below is
a sum of chosen constituents with chosen amplitudes and phases. The constituent
speeds are the conventional constants of the standard tidal harmonic convention,
used as model inputs and printed by the demonstration; no tide gauge, port or
published prediction is used.

## Learning objectives

By the end of this lesson you will be able to:

1. **Write** the harmonic tide model with its amplitude–phase parameterisation
   and **explain** why the frequencies are not fitted.
2. **Derive** the Rayleigh criterion $T \ge 1/\lvert f_1 - f_2 \rvert$ and
   **measure** the amplification of noise it predicts for a short record.
3. **Compute** the alias of any constituent for any sampling interval and
   **state** why daily sampling destroys the semidiurnal band.
4. **Explain** why daily sampling makes S2 indistinguishable from the mean and
   M2 indistinguishable from the M2–S2 beat, and **quantify** the resulting
   ill-conditioning.
5. **Choose** a record length from a stated separation requirement, and
   **state** what the choice costs in prediction error.
6. **Validate** a harmonic prediction out of sample rather than by its fit
   residual, and **state** the role of nodal and shallow-water corrections.
7. **State** the assumptions under which a least-squares tidal analysis is
   valid, and the regime in which it is not.

## Prerequisites

- [20-08-01 Detrending, Deseasonalising and Anomalies](01-detrending-seasonality.md)
  — harmonic regression, and the difference between a fitted and a known
  frequency.
- [20-02-02 Spectral Estimation: Periodogram, Welch, Multitaper](../02-fourier-and-spectral-analysis/02-spectral-estimation.md)
  — resolution in frequency, and what sets it.
- [20-01-05 Sampling, Nyquist and Reconstruction](../01-signals-and-systems/05-sampling-theory.md)
  — aliasing from first principles, which §4 applies to a real band structure.

The runnable companion is
[`code/tidal_harmonics_demo.py`](code/tidal_harmonics_demo.py); the graded
problems are in
[`exercises/02-spectral-analysis-tides-exercises.md`](exercises/02-spectral-analysis-tides-exercises.md).

## 1. The model, and why the frequencies are given

A tidal record at a station is modelled as

$$
h(t) = Z_0 + \sum_{c} A_c \cos\!\left(\sigma_c t - \phi_c\right),
$$

where $\sigma_c$ are the **speeds** of the astronomical constituents, in degrees
per hour, and $A_c, \phi_c$ are the station's amplitude and phase (the harmonic
constants). The model is linear in the four parameters $(Z_0, A_c\cos\phi_c,
A_c\sin\phi_c)$ once the $\sigma_c$ are fixed, which is the whole point: the
frequencies come from the orbital mechanics of the Earth–Moon–Sun system, and
only amplitudes and phases are estimated from the record. Fitting frequencies
would be fitting astronomy to a tide gauge.

The demonstration's constituent set (conventional speeds, printed as model
inputs):

| constituent | speed (°/h) | period (h) | amplitude (m) | phase (rad) |
|---|---|---|---|---|
| M2 | 28.9841042 | 12.4206 | 1.200 | 0.400 |
| S2 | 30.0000000 | 12.0000 | 0.350 | 1.100 |
| N2 | 28.4397295 | 12.6583 | 0.250 | 2.300 |
| K1 | 15.0410686 | 23.9345 | 0.200 | 4.000 |
| O1 | 13.9430356 | 25.8193 | 0.150 | 5.100 |

With known frequencies and no noise, least squares recovers the amplitudes to
double precision: the demonstration's errors are between $-7.4\times10^{-15}$ and
$+5.6\times10^{-16}$ m and the residual rms is $1.0\times10^{-14}$ m. **The
analysis is not the hard part.** The hard parts are which constituents to include
and how long the record must be, and both are answered by the same criterion.

## 2. The Rayleigh criterion

Two constituents with speeds $\sigma_1, \sigma_2$ (in °/h) can be separated by a
least-squares fit only if the record is long enough for their phases to differ by
a full cycle:

$$
T \ge \frac{360^{\circ}}{\lvert \sigma_1 - \sigma_2 \rvert} .
$$

Equivalently, in frequency resolution: $\Delta f \ge 1/T$. The criterion is not a
convention but the condition for the two columns of the design matrix
$[\cos \sigma_1 t, \cos \sigma_2 t, \dots]$ to be distinguishable in the presence
of noise. The demonstration computes it for every pair:

| pair | $\lvert \Delta\sigma \rvert$ (°/h) | $T$ (h) | $T$ (days) |
|---|---|---|---|
| M2–S2 | 1.0158958 | 354.367 | 14.765 |
| M2–N2 | 0.5443747 | 661.309 | 27.555 |
| S2–N2 | 1.5602705 | 230.729 | 9.614 |
| K1–O1 | 1.0980330 | 327.859 | 13.661 |
| M2–K1 | 13.9430356 | 25.819 | 1.076 |
| S2–K1 | 14.9589314 | 24.066 | 1.003 |
| M2–O1 | 15.0410686 | 23.934 | 0.997 |
| N2–K1 | 13.3986609 | 26.868 | 1.120 |
| N2–O1 | 14.4966939 | 24.833 | 1.035 |
| S2–O1 | 16.0569644 | 22.420 | 0.934 |

The diurnal–semidiurnal pairs need about a day; the intra-band pairs need weeks:
14.765 days for M2–S2 and 27.555 days for M2–N2. A one-month record is
therefore the shortest that can separate the three principal semidiurnal
constituents, and the widely used 29-day or 30-day analyses are cut to that
cloth.

## 3. What the criterion costs, measured

Fix a signal containing only M2 and N2 and add Gaussian noise with
$\sigma = 0.03$ m. Fit M2 and N2 by least squares over records of increasing
length, 20 realisations each, and measure the scatter of the recovered
amplitudes:

| record (days) | std of M2 error (m) | std of N2 error (m) | $\kappa(G)$ |
|---|---|---|---|
| 2.00 | 0.05648 | 0.04847 | $1.65\times10^{1}$ |
| 5.00 | 0.00972 | 0.01133 | $6.30$ |
| 10.00 | 0.00425 | 0.00483 | $3.17$ |
| 27.55 | 0.00132 | 0.00161 | $1.42$ |
| 40.00 | 0.00116 | 0.00129 | $1.60$ |
| 60.00 | 0.00098 | 0.00073 | $1.47$ |

The noise is the same 0.03 m everywhere. Below the 27.555-day separation time
the two columns of the design matrix are nearly parallel, the problem is
ill-conditioned, and the recovered amplitudes trade against each other: the error
at 2 days is 0.0565 m, **58 times** the 0.00098 m at 60 days. The condition
number tracks it.

This is the honest face of the Rayleigh criterion. It does not say that a short
record *fails*; it says that the noise-to-error gain rises, here by a factor of
58, and that a harmonic constant quoted without its record length is not a
measurement of the station but of the station and the analysis window together.

## 4. Aliasing: what sampling does to a known band structure

A tide gauge sampled at interval $\Delta$ hours has sampling frequency
$f_s = 360/\Delta$ °/h and Nyquist $f_s/2$. Every constituent speed folds into
the band $\left[0, f_s/2\right]$ by subtracting multiples of $f_s$; the
demonstration computes the folded speeds exactly:

| interval | $f_s$ (°/h) | M2 alias | S2 alias | N2 alias | K1 alias | O1 alias |
|---|---|---|---|---|---|---|
| 1 h | 360.00 | 28.98410 | 30.00000 | 28.43973 | 15.04107 | 13.94304 |
| 3 h | 120.00 | 28.98410 | 30.00000 | 28.43973 | 15.04107 | 13.94304 |
| 6 h | 60.00 | 28.98410 | 30.00000 | 28.43973 | 15.04107 | 13.94304 |
| 12 h | 30.00 | **1.01590** | **0.00000** | **1.56027** | 14.95893 | 13.94304 |
| 24 h | 15.00 | **1.01590** | **0.00000** | **1.56027** | **0.04107** | **1.05696** |

Read the last row carefully, because it explains one of the most familiar
features of daily sea-level records:

- **S2 (30.0000 °/h) folds to 0.0000** — the solar semidiurnal constituent
  becomes a constant offset. At daily sampling it is *indistinguishable from the
  mean sea level*.
- **M2 (28.9841 °/h) folds to 1.0159 °/h**, a period of 354.4 h $= 14.77$ days.
- **N2 (28.4397 °/h) folds to 1.5603 °/h**, a period of 9.59 days.
- **K1 (15.0411 °/h) folds to 0.04107 °/h**, a period of 8766 h $\approx$ 1 year:
  the diurnal lunar constituent appears as an annual signal.
- **O1 (13.9430 °/h) folds to 1.0570 °/h**, a period of 14.19 days.

Note the exact arithmetic coincidence: the 14.77-day alias of M2 is the
M2–S2 beat period of §2. The alias is not an analogy for the beat; at daily
sampling the two are the same frequency. This is why the "14.77-day" signal in
daily tide or bottom-pressure records is unremarkable and why a semidiurnal
constituent cannot be extracted from daily data at all.

The consequence for a fit is measured directly. Fitting the full five-constituent
model to **daily** data gives a design matrix whose condition number is
$\kappa(G) = 3.939\times10^{15}$ — numerically singular in double precision — and
the recovered amplitudes are:

| constituent | recovered from daily data (m) | truth (m) |
|---|---|---|
| M2 | 1.2000 | 1.200 |
| S2 | **0.0794** | 0.350 |
| N2 | 0.2500 | 0.250 |
| K1 | 0.2000 | 0.200 |
| O1 | 0.1500 | 0.150 |

S2 has collapsed into the mean and M2 has absorbed the rest. Every other
constituent is recovered, which is exactly what makes the failure dangerous: the
output looks like a successful analysis with one odd number in it. The remedy is
not a better algorithm but hourly data.

### 4.1 Worked example: what daily sampling would tell you

A 60-day record of the same synthetic tide, sampled daily, contains 60 numbers.
Under the alias table those 60 numbers are generated by frequencies
$\{0, 1.0159, 1.5603, 0.04107, 1.0570\}$ °/h, not by the five true constituents.
Any fit that returns five amplitudes is selecting one of infinitely many
parameter sets consistent with the 60 numbers; the condition number
$3.9\times10^{15}$ is the numerical statement that the selection is arbitrary.
**A tidal analysis should therefore always report its sampling interval before
its harmonic constants.**

## 5. Prediction, validated out of sample

Tidal prediction is the extrapolation of the fitted model. Its error is a
measured quantity with a clean structure. The model contains all five
constituents in every case; the record is fitted, then the following 30 days are
predicted and compared with the noise-free truth:

| record | fit residual rms (m) | M2 error (m) | N2 error (m) | prediction rms (m) |
|---|---|---|---|---|
| 7.00 d | 0.0300 | $+0.0179$ | $+0.0161$ | 0.0195 |
| 14.77 d | 0.0304 | $+0.0058$ | $-0.0009$ | 0.0071 |
| 30.00 d | 0.0283 | $+0.0025$ | $+0.0001$ | 0.0030 |
| 60.00 d | 0.0289 | $-0.0012$ | $-0.0001$ | 0.0025 |

Two conclusions, both measurable:

- **The fit residual cannot rank the records.** It is 0.0283–0.0304 m at every
  length, i.e. the noise level, because the model has enough freedom to absorb
  the noise. A residual is a check on the arithmetic, not on the model.
- **The prediction error can.** It falls from 0.0195 m at 7 days to 0.0025 m at
  60 days, a factor of 7.8, and the trend of the M2 error follows it. Prediction
  is the only test here that distinguishes a record that separates the
  constituents from one that does not.

This is why operational tide prediction uses records of a year or more — decades
for the minor constituents — even though a 30-day analysis recovers the five
principal constants to a fraction of a per cent in the ideal case. The record
length is chosen for separability, not for fit.

## 6. Assumptions and regime of validity

1. **The speeds are exact and constant.** The conventional speeds ignore nodal
   modulation of the lunar constituents (an 18.6-year cycle) and the slow
   changes in the lunar orbit; a real analysis applies nodal factors, which
   depend on the epoch and are not part of this model.
2. **The response is linear.** Shallow-water constituents (M4, M6, and the
   compound tides) are generated by nonlinear interaction and are not multiples
   of the astronomical frequencies in a simple way; a least-squares fit with only
   the astronomical set will absorb them into residuals.
3. **The station's constants are stationary.** Harbour works, dredging and
   sea-level rise change the response. A fit over 30 years averages the change
   into a single constant, which is the same averaging problem as §6 of lesson
   01.
4. **Known frequencies.** The entire analysis rests on this. The demonstration's
   §2 result — errors at the $10^{-15}$ level — is a property of the *algorithm*
   applied to a model that satisfies the assumption, not evidence that real tides
   are exactly five sinusoids.
5. **Meteorology is absent.** Storm surge, river discharge and air-pressure
   inverse-barometer effects appear as the irregular component, and in a real
   record they are often larger than the constituents being fitted.
6. **Gauges do not alias.** The alias table of §4 is a property of the sampling;
   a gauge that samples hourly and is then daily-averaged is a different
   operation, and daily means of an hourly record are not the same data set as
   daily spot samples.
7. **Everything here is SYNTHETIC**, with teaching amplitudes of order a metre.

## Mastery checkpoint

Without notes: **(a)** write the harmonic tide model and state which quantities
are given and which are estimated; **(b)** derive the Rayleigh criterion with
units and compute $T$ for two constituents of your choice from the table of §2;
**(c)** compute the alias of M2 for sampling intervals of 8 h and 24 h using the
folding rule and state the periods; **(d)** explain, in terms of columns of the
design matrix, why daily S2 is indistinguishable from the mean; **(e)** from §5,
state the measured prediction error at 7 days and at 60 days and say which
statistic you would report to justify a 30-day analysis; **(f)** name two
assumptions of §6 that an operational prediction would violate and say how each
is handled in practice.

A worked answer to (a)–(d) appears in the
[solutions](exercises/02-spectral-analysis-tides-solutions.md).

## Common pitfalls

1. **Quoting harmonic constants without the record length.** Below the Rayleigh
   separation time the noise-to-error gain rises; it measured 58× between the
   2-day and 60-day fits here.
2. **Judging a tidal analysis by its residual.** The residual measured 0.0283 m
   for a 30-day fit and 0.0300 m for a 7-day fit: indistinguishable.
3. **Fitting semidiurnal constituents to daily data.** The design matrix
   condition number measured $3.9\times10^{15}$ and S2 came back as 0.0794 m
   against a truth of 0.350 m.
4. **Reading a 14.77-day signal as a constituent.** At daily sampling it *is*
   the M2 alias, identical to the M2–S2 beat.
5. **Fitting the frequencies.** They are astronomy; estimating them fits the
   noise and destroys the conditioning.
6. **Forgetting the 18.6-year nodal modulation.** The constants of a lunar
   constituent drift with the node; a constant fitted to one epoch is not
   transferable to another without a nodal factor.
7. **Extrapolating far beyond the record.** Prediction error grows with the
   extrapolation interval; the 30-day prediction measured here is not evidence
   for a 10-year prediction.

## Related modules

- [20-08-01 Detrending, Deseasonalising and Anomalies](01-detrending-seasonality.md)
  — harmonic regression with fitted rather than known frequencies.
- [20-08-03 Geodetic Time Series: Trends, Offsets, Noise Models](03-geodetic-time-series.md)
  — the same least-squares structure with a coloured noise model attached.
- [20-02-02 Spectral Estimation: Periodogram, Welch, Multitaper](../02-fourier-and-spectral-analysis/02-spectral-estimation.md)
  — resolution and leakage, seen from the spectral side.
- [20-01-05 Sampling, Nyquist and Reconstruction](../01-signals-and-systems/05-sampling-theory.md)
  — the general aliasing theorem applied to a real band structure here.
