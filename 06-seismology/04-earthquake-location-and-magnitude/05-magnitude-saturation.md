---
id: 06-04-05
title: "Magnitude Saturation and Why Moment Magnitude Is Preferred"
level: graduate
prereqs: ["06-04-04", "06-03-05", "06-03-03"]
tags: [seismology, magnitude, saturation, catalogue, b-value]
---

# Magnitude Saturation and Why Moment Magnitude Is Preferred

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the size at which a fixed-band magnitude stops tracking the moment,
   from the crossing condition $f_c = f_{\text{band}}$.
2. **Distinguish** the crossing size from a threshold-based "saturation onset"
   and explain why the two differ.
3. **Derive** the recovery of a b-value from an exponential magnitude sample and
   compute the apparent b-value of a saturated scale.
4. **Quantify** the bias created by a linear magnitude conversion fitted at
   small sizes and applied at large ones, in magnitude units and in moment.
5. **Compute** the moment range hidden inside one saturated magnitude value, and
   explain why it is not recoverable by arithmetic.
6. **Compare** a saturated amplitude scale with an energy proxy that does not
   saturate, and decide which quantity a hazard study should use.

## Prerequisites

- [04 Magnitude Scales: Local, Body, Surface, Duration, Moment](04-magnitude-scales.md) —
  the spectrum, the band amplitudes and the two slopes.
- [06-03-05 Source Spectra, Corner Frequency and Stress Drop](../03-earthquake-sources/05-source-spectra.md).
- [06-03-03 Moment Tensors, Decomposition and Physical Meaning](../03-earthquake-sources/03-moment-tensors.md).

## 1. Intuition: the instrument stopped growing, not the earthquake

A magnitude scale built on a fixed frequency band is a probe at one place in the
spectrum. As events grow, the corner frequency of their spectra slides to lower
frequency, and the probe falls off the plateau onto the $f^{-2}$ branch. The
slope $\mathrm{d}M/\mathrm{d}M_w$ then drops from $3/2$ to $1/2$ (lesson
[04](04-magnitude-scales.md) Section 3.3). Nothing happened to the earthquake:
the source is still radiating an energy proportional to its moment. What stopped
growing in proportion is the *reading of the probe*.

This produces three practical consequences, each of which this lesson measures:

1. **The mapping from one scale to another is nonlinear.** A straight-line
   conversion calibrated where the scales agree is wrong where they do not.
2. **A threshold count changes.** "How many events above magnitude 6?" has a
   different answer in $m_b$ and in $M_w$ for the same catalogue.
3. **A b-value fitted to a saturated catalogue is not the b-value of the
   seismicity.** It is a joint property of the seismicity and the scale.

## 2. Where the band crosses the corner

From lesson [04](04-magnitude-scales.md), a self-similar family has

$$
f_c(M_0) = f_{c,\text{ref}}\left(\frac{M_0}{M_{0,\text{ref}}}\right)^{-1/3} ,
$$

so the crossing condition $f_c = f_b$ for a band centre $f_b$ occurs at

$$
M_0^{\text{cross}} = M_{0,\text{ref}}\left(\frac{f_{c,\text{ref}}}{f_b}\right)^{3}
\qquad\Longrightarrow\qquad
M_w^{\text{cross}} = \frac{2}{3}\left(\log_{10} M_0^{\text{cross}} - 9.1\right).
$$

This is a *derived* size: it follows from the model constants and the band, with
no fitting. The demonstration's model uses $f_{c,\text{ref}} = 0.6\ \mathrm{Hz}$
at $M_{0,\text{ref}} = 10^{15}\ \mathrm{N\,m}$, and gives

$$
M_0^{\text{cross}}(m_b) = 2.160\times10^{14}\ \mathrm{N\,m},
\quad M_w^{\text{cross}}(m_b) = 3.49 ,
$$

$$
M_0^{\text{cross}}(M_s) = 1.728\times10^{18}\ \mathrm{N\,m},
\quad M_w^{\text{cross}}(M_s) = 6.09 .
$$

The 1 Hz body-wave band crosses at $M_w = 3.49$; the 20 s surface-wave band
crosses at $M_w = 6.09$. That difference of 2.6 magnitude units is the reason
$m_b$ and $M_s$ appear to "saturate" at different sizes, and it is a statement
about frequencies, not about faulting.

## 3. Why the measured onset is not the crossing

A crossing is a point; a slope is a rate. At $f_c = f_b$ the spectrum is already
mid-bend ($(f/f_c)^{2} = 1$), so the local slope is neither $3/2$ nor $1/2$ but
something in between, and it approaches $1/2$ only asymptotically. Any statement
of the form "saturation begins at magnitude $X$" therefore depends on the
threshold used to declare it. The demonstration declares saturation to have
begun at the first $M_w$ after which the local finite-difference slope stays
below 0.75:

| scale | crossing $M_w$ (derived) | threshold onset $M_w$ (measured) | value there |
|---|---|---|---|
| $m_b$ | 3.49 | 4.00 | 3.98 |
| $M_s$ | 6.09 | 6.60 | 7.31 |

Both numbers are legitimate; they answer different questions. Quote the crossing
when you mean the physics, and the threshold onset when you mean "from here on
the scale is compressed by more than 25 per cent". A paper that reports only one
of them without saying which is not reporting a measurement.

## 4. The saturation curves

| $M_w$ | $m_b$ | $\mathrm{d}m_b/\mathrm{d}M_w$ | $M_s$ | $\mathrm{d}M_s/\mathrm{d}M_w$ |
|---|---|---|---|---|
| 3.00 | 2.99 | 1.245 | 2.54 | 1.499 |
| 4.00 | 3.98 | 0.736 | 4.03 | 1.492 |
| 5.00 | 4.59 | 0.530 | 5.50 | 1.425 |
| 6.00 | 5.10 | 0.503 | 6.78 | 1.053 |
| 7.00 | 5.60 | 0.500 | 7.58 | 0.610 |
| 8.00 | 6.10 | 0.500 | 8.12 | 0.512 |
| 9.00 | 6.60 | 0.500 | 8.63 | 0.501 |
| 9.50 | 6.85 | 0.500 | 8.88 | 0.500 |

Three features are worth naming.

- **The slopes do not go to zero.** Both approach $1/2$. A saturated magnitude
  still grows; it grows at half the rate, because a band on the $f^{-2}$ branch
  sees an amplitude $\propto M_0^{1/3}$.
- **The largest values over the grid are $m_b = 6.85$ and $M_s = 8.88$**, both at
  $M_w = 9.5$. The $m_b$ value never reaches 7 anywhere in the family: the band
  is where the corner frequency already was three decades earlier.
- **The surface-wave column saturates later and more gradually**, because its
  band is three decades lower in frequency.

### 4.1 Deriving the asymptotic slope $1/2$ once more, for use in Section 6

On the $f^{-2}$ branch, $A \propto M_0 f_c^{2}$ and $f_c \propto M_0^{-1/3}$, so
$A \propto M_0^{1/3}$ and $M = \log_{10}A + c = \tfrac{1}{3}\log_{10}M_0 + c$.
Writing $\log_{10}M_0 = \tfrac{3}{2}M_w + 9.1$ gives
$M = \tfrac{1}{2}M_w + \text{const}$, which is the measured 0.500.

## 5. What saturation does to a catalogue

### 5.1 The b-value of a magnitude sample

For a Gutenberg–Richter distribution $N(M) \propto 10^{-bM}$ truncated at
$M_{\min}$, the maximum-likelihood estimate of the b-value is the standard
Aki–Utsu expression

$$
\hat{b} = \frac{\log_{10} e}{\bar{M} - M_{\min}} ,
$$

with $\bar{M}$ the sample mean. The demonstration draws 2000 events in $M_w$ from
a truncated GR law between $M_w = 4.0$ and $8.5$ with $b = 1.00$, then converts
each event to $m_b$ through the saturation curve of Section 4 and refits:

| sample | recovered b |
|---|---|
| $M_w$ | 1.012 |
| $m_b$ | 1.609 |

The same earthquakes produce a b-value of 1.01 or 1.61 depending on which
measurement the catalogue reports. The inflation is not noise: compressing the
large end of the distribution steepens the fitted line. Over the catalogue's
range, $m_b$ spans only 3.98 to 5.80 while $M_w$ spans 4.00 to 7.40.

The threshold counts make the same point in a form no statistic can obscure:

| threshold | events with $M_w \ge$ threshold | events with $m_b \ge$ threshold |
|---|---|---|
| 6.0 | 23 | 0 |
| 6.5 | 5 | 0 |
| 7.0 | 3 | 0 |

A catalogue reporting only $m_b$ would contain no event at all above 6 in this
sample, while three events exceed $M_w = 7$. Any hazard or recurrence calculation
that counts events above a threshold inherits this difference directly.

### 5.2 The cost of a linear conversion

A common shortcut is to fit a straight line to the (small-event) part of the
relation and apply it everywhere. Fitted on $M_w \le 5.0$ in the demonstration,

$$
M_w^{\text{est}} = 1.261\,m_b - 0.935 .
$$

Applying it up the range:

| $M_w$ | $m_b$ | $M_w^{\text{est}}$ | bias | $M_w$ range implied by $m_b \pm 0.2$ |
|---|---|---|---|---|
| 3.0 | 2.99 | 2.83 | $-0.17$ | 0.16 |
| 4.0 | 3.98 | 4.09 | $+0.09$ | 0.55 |
| 5.0 | 4.59 | 4.85 | $-0.15$ | 0.75 |
| 6.0 | 5.10 | 5.50 | $-0.50$ | 0.79 |
| 7.0 | 5.60 | 6.13 | $-0.87$ | 0.80 |
| 8.0 | 6.10 | 6.76 | $-1.24$ | 0.80 |
| 9.0 | 6.60 | 7.39 | $-1.61$ | 0.80 |

Two separate defects, in order of importance:

1. **Bias.** A $M_w = 9.0$ event is reported as $M_w = 7.39$. The bias of
   $-1.61$ magnitude units is a factor of
   $10^{1.5\times1.61} = 261$ in moment. A catalogue that converts this way is
   not merely imprecise; it is *inconsistent with itself* across the size range,
   because the conversion is accurate where it was fitted and wrong elsewhere.
2. **Uncertainty.** Give $m_b$ its own uncertainty — 0.2 magnitude units is the
   value assumed here — and invert exactly. Below the crossing the implied $M_w$
   range is 0.16 to 0.55; above it the range settles near 0.80, because a slope
   of $1/2$ doubles any magnitude uncertainty. The same $m_b$, to within its
   stated uncertainty, is produced by events whose moments differ by a factor of
   about 16, and no arithmetic can undo that.

### 5.3 What is still there: the energy does not saturate

The physical information that $m_b$ loses is not lost by the earthquake. Using
the far-field velocity pulse of the same source family, with

$$
E \propto \int \big(\text{far-field velocity}\big)^{2}\,\mathrm{d}t ,
$$

the demonstration measures

$$
\frac{\mathrm{d}\log_{10} E}{\mathrm{d}M_w} = 1.500
\quad\text{over the whole range and}\quad
1.500 \ \text{in the last magnitude unit},
$$

while $m_b$ has a slope of 0.500 over the same interval. The source radiates
more and more energy while the band-limited magnitude stops keeping pace. That
slope of 1.500 is the exponent of the standard energy–magnitude relation, and
lesson [06](06-energy-moment-calculations.md) derives it from constant stress
drop rather than fitting it.

## 6. Worked examples

### Example 1 — the crossing size, by hand

For the 1 Hz band, $f_{c,\text{ref}}/f_b = 0.6/1.0 = 0.6$, so

$$
M_0^{\text{cross}} = 10^{15}\times0.6^{3} = 10^{15}\times0.216
= 2.16\times10^{14}\ \mathrm{N\,m},
$$

$$
M_w^{\text{cross}} = \tfrac{2}{3}\left(\log_{10}(2.16\times10^{14}) - 9.1\right)
= \tfrac{2}{3}(14.3345 - 9.1) = \tfrac{2}{3}(5.2345) = 3.49 .
$$

For the 0.05 Hz band, $f_{c,\text{ref}}/f_b = 12$, so
$M_0^{\text{cross}} = 10^{15}\times1728 = 1.728\times10^{18}\ \mathrm{N\,m}$ and
$M_w^{\text{cross}} = \tfrac{2}{3}(18.2375-9.1) = 6.09$. Both match the printed
values, which is the point: the two "saturation magnitudes" are arithmetic on the
model constants, not observations.

### Example 2 — one b-value, by hand

Convert the printed $m_b$ range to a mean and apply the estimator. For a sample
with $M_{\min} = 3.98$ and mean $\bar{m}_b$, the fit gives $\hat{b} = 1.609$; with
$\log_{10}e = 0.4343$,

$$
\bar{m}_b - M_{\min} = \frac{0.4343}{1.609} = 0.270 ,
$$

so $\bar{m}_b = 3.98 + 0.270 = 4.25$. The corresponding $M_w$ sample has
$\hat{b} = 1.012$, so $\bar{M}_w - M_{\min} = 0.4343/1.012 = 0.429$ and
$\bar{M}_w = 4.00 + 0.429 = 4.43$ — the samples tell the same physical story,
with means that differ by 0.18 in their own units and b-values that differ by
0.6. This is why the b-value is reported with the magnitude type, always.

### Example 3 — the moment factor behind a bias

A bias of $\Delta M = -1.61$ in moment magnitude corresponds to a moment ratio

$$
\frac{M_0^{\text{true}}}{M_0^{\text{reported}}}
= 10^{1.5\,\Delta M} = 10^{1.5\times1.61} = 10^{2.42} = 261 .
$$

So a catalogue that reports the converted value understates the seismic moment of
a great earthquake by two and a half orders of magnitude. For a tsunami or
ground-motion calculation the difference is not a matter of bookkeeping.

## 7. Assumptions and regime of validity

1. **Self-similarity with constant stress drop.** The whole curve follows from
   $f_c \propto M_0^{-1/3}$. Real stress drops vary, which makes the curve a
   band of curves rather than a line.
2. **Point source.** This is the model's most important limit. A finite fault
   radiates for a duration set by rupture propagation, so a great earthquake's
   20 s surface wave may sample only part of the source; that is an additional,
   independent mechanism for $M_s$ saturation, and it requires a finite-fault
   model. The measured $M_s$ curve here therefore saturates *later* than the real
   one, and the real one saturates more.
3. **A single band centre.** Real scales integrate a response over a band.
4. **A stated event distribution.** The b-value results depend on the GR
   assumption and on the truncation range; a different distribution gives a
   different apparent b-value even with the same saturation curve.
5. **An internal calibration.** The constants are fixed at one event; a real
   scale is calibrated across distances and stations.
6. **One realisation.** The catalogue numbers come from a single seeded
   realisation of 2000 events. The *pattern* of the results is robust; the third
   digit is not.

## 8. The demonstration

```bash
cd 06-seismology/04-earthquake-location-and-magnitude/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python magnitude_saturation_demo.py
```

It prints the saturation curves and their slopes, the crossing and threshold
onsets, the synthetic catalogue with its two b-values and threshold counts, the
conversion bias table, and the energy-proxy slope.

Exercises:
[`exercises/05-magnitude-saturation-exercises.md`](exercises/05-magnitude-saturation-exercises.md)
and
[`exercises/05-magnitude-saturation-solutions.md`](exercises/05-magnitude-saturation-solutions.md).

> All models and data in this module are **SYNTHETIC**. The source family, the
> path, the bands, the calibration and the catalogue are teaching values.

## Mastery checkpoint

Without notes:

1. Derive the crossing size $M_w$ for a band at $f_b$ from
   $f_c \propto M_0^{-1/3}$.
2. Explain why the measured threshold onset is larger than the crossing size.
3. State the asymptotic slope of a saturated band magnitude and derive it.
4. Given $\hat{b}_{m_b} = 1.61$ and $\hat{b}_{M_w} = 1.01$ for the same events,
   explain in one paragraph why both are correct.
5. Convert a bias of $-1.0$ magnitude units into a factor in moment.
6. Name the physical quantity that keeps growing when $m_b$ has stopped, and
   give the measured slope.

## Common pitfalls

1. **Treating saturation as a source property.** It is a property of the band.
2. **Fitting a conversion line at small sizes and applying it at large ones.**
   That is where the largest bias lives.
3. **Reporting a b-value without the magnitude type.** The number is meaningless
   without it, as Section 5.1 shows.
4. **Assuming magnitudes stop growing entirely.** They grow with slope $1/2$.
5. **Using one threshold count as if it were scale-independent.**
   "23 events above 6" and "0 events above 6" can describe the same catalogue.
6. **Neglecting the finite-fault effect on $M_s$.** The point-source model
   understates the real saturation of great earthquakes.

## Related modules

- [04 Magnitude Scales: Local, Body, Surface, Duration, Moment](04-magnitude-scales.md).
- [06 Energy Release, Moment Calculations and Scaling](06-energy-moment-calculations.md) —
  the derivation behind the 1.500 slope.
- [06-11 Earthquake Statistics and Hazard](../11-earthquake-statistics-and-hazard/README.md) —
  where catalogue-scale inconsistency propagates into hazard.
- [21-01-04 Linear, Multiple and Robust Regression](../../21-statistics-bayesian-ml/01-statistics-in-practice/04-regression.md) —
  the fitting machinery behind Section 5.1.
