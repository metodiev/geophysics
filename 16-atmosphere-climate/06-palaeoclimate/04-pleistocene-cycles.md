---
id: 16-06-04
title: "Pleistocene Glacial Cycles and Orbital Forcing"
level: doctoral
prereqs: ["16-06-01", "16-06-03", "13-07-03"]
tags: [atmosphere, climate, palaeoclimate, orbital-forcing, glacial-cycles, milankovitch, nonlinear-response]
---

# Pleistocene Glacial Cycles and Orbital Forcing

> All models and data in this module are **SYNTHETIC**. Every number below was
> printed by
> [`code/pleistocene_cycles_demo.py`](code/pleistocene_cycles_demo.py). The
> forcing amplitudes and phases are chosen; only the *periods* are the standard
> astronomical ones, stated in the code. No real ice-volume or isotope record is
> used, and no published period or spectral peak is quoted.

## Learning objectives

By the end of this lesson you will be able to:

1. **State** the astronomical argument: which orbital elements vary, on what
   periods, and how they change the distribution of insolation.
2. **Construct** a synthetic insolation signal as a sum of orbital terms with an
   amplitude-modulated precession.
3. **Compute** a periodogram and **measure** the fraction of variance in named
   period bands for both forcing and response.
4. **Build** a melt-threshold ice model and **demonstrate** that a nonlinear
   response can concentrate variance at a period the forcing barely contains.
5. **Quantify** the asymmetry (sawtooth shape) of the response and **state** which
   feature of the model produces it.
6. **Explain** why this is a demonstration of a *mechanism* and not an
   explanation of the observed glacial cycles.
7. **State** the assumptions under which a threshold model of this kind is
   defensible, and the observations that would falsify it.

## Prerequisites

- [16-06-01 Palaeoclimate Proxies: Ice Cores, Sediments, Isotopes](01-paleoclimate-proxies.md) —
  how ice-volume histories are reconstructed at all.
- [16-06-03 Abrupt Climate Change and Tipping Elements](03-abrupt-climate-change.md) —
  thresholds, multiple states and nonlinear response.
- [13-07-03 Tectonics-Climate Feedbacks](../../13-geodynamics-tectonics/07-geomorphology-tectonics-climate/03-tectonics-climate-feedback.md) —
  the long-timescale coupling of solid Earth and climate.

## 1. Intuition: a weak forcing with a strong, periodic response

The astronomical (Milankovitch) argument is that the seasonal and latitudinal
distribution of insolation varies as the Earth's orbit and axial tilt change,
and that high-latitude summer insolation controls whether snow survives the
melt season. The total annual insolation changes very little; what changes is
its *geographical and seasonal distribution*, by a few percent in the
high-latitude summer.

A few percent is a small forcing. Yet the geological record shows large,
quasi-periodic ice-volume changes. Whatever the mechanism, it must involve
**amplification** — and the natural candidate is a threshold: ice accumulates
slowly whenever ablation is less than accumulation, and is removed rapidly when
summer insolation crosses a level that melts the seasonal snow cover earlier
than accumulation can rebuild it.

This lesson builds the smallest model with that structure and measures what it
does to the spectrum of the response. The purpose is to demonstrate the
*mechanism*, not to identify the cause of the observed cycles. The question of
which combination of orbital forcing, ice-sheet dynamics, carbon cycle and
ocean circulation produced the observed record is a live research question, and
nothing in this lesson resolves it.

## 2. Definitions

- **Insolation.** The solar irradiance received at the top of the atmosphere on a
  horizontal surface, a function of latitude and season. It is a computed
  quantity, not an observation of surface climate.
- **Orbital elements.** Three matters here: **obliquity** (axial tilt),
  **precession** (the direction of the axis relative to the orbit) and
  **eccentricity** (the shape of the orbit).
- **Amplitude modulation.** A fast oscillation whose amplitude is itself
  oscillating slowly. Precession is modulated by eccentricity, because the
  insolation effect of precession is proportional to eccentricity.
- **Periodogram.** An estimate of the distribution of variance over frequency,
  computed here by the squared modulus of a discrete Fourier transform.
- **Melt threshold.** The insolation level above which ablation exceeds
  accumulation in the model.
- **Phase locking.** A response whose apparent period is set by the forcing even
  though the response is nonlinear.
- **The "100-kyr problem".** The observation that late Pleistocene ice-volume
  variance is concentrated near 100 ka, whereas the orbital forcing at that
  period is weak (eccentricity itself changes insolation only slightly, and only
  through the precession modulation). It is a problem about *mechanism*, and it
  is not settled by a demonstration of one candidate mechanism.

## 3. Deriving the synthetic forcing

### 3.1 Standard astronomical periods

The periods used in the demonstration are the standard values from orbital
mechanics, stated in the code in kiloyears:

| element | period (ka) |
|---|---|
| obliquity | 41 |
| precession (short) | 23 |
| precession (long) | 19 |
| eccentricity | 100 |

Only these four numbers are standard. Everything else — the amplitudes, the
phases and the shape of the response — is a chosen teaching value.

### 3.2 The signal

The demonstration builds a dimensionless mid-latitude summer insolation proxy

$$I(t) = \underbrace{A_o\sin\frac{2\pi t}{41}}_{\text{obliquity}}
+ \underbrace{A_p\left(1 + m\cos\frac{2\pi t}{100}\right)\sin\frac{2\pi t}{23}}_{\text{precession, modulated}}
+ \underbrace{A_q\left(1 + m\cos\frac{2\pi t}{100}\right)\sin\!\left(\frac{2\pi t}{19}+0.9\right)}_{\text{long precession}},$$

with $A_o = 0.50$, $A_p = 0.70$, $A_q = 0.30$ and modulation depth $m = 0.50$.
Over $2400\ \mathrm{ka}$ sampled every $0.25\ \mathrm{ka}$ the forcing has mean
$+0.0061$ and standard deviation $0.6715$ in these dimensionless units.

The product of two sinusoids is the key structural feature: a fast oscillation
multiplied by a slow one produces *sidebands* whose frequencies are the sum and
difference of the two, not the modulation frequency itself. The distortion that
turns those sidebands into power *at* 100 ka is made by the threshold, not by
the modulation.

## 4. Measurement: where the variance is in the forcing

Computing the periodogram of $I(t)$ and summing power over named bands (the
shares are normalised by the total power above frequency zero):

| period band | forcing share | response share (Section 5) |
|---|---|---|
| obliquity (41 ka) | 0.2723 | 0.2042 |
| precession (19–23 ka) | 0.6831 | 0.1536 |
| eccentricity (100 ka) | 0.0026 | 0.3073 |
| long ($>200$ ka) | 0.0017 | 0.0545 |
| all periods $>60$ ka | 0.0084 | 0.4384 |

Two numbers deserve to be read slowly. The forcing has $68.31\%$ of its variance
in the precession band and $0.26\%$ at the eccentricity period; the measured
dominant period of the *forcing* is $23.1\ \mathrm{ka}$. The response, measured
below, puts $30.73\%$ of its variance at 100 ka and has a dominant period of
$100.0\ \mathrm{ka}$. The forcing's long-period share is $0.0084$ and the
response's is $0.4384$ — a factor of $52$ larger, produced by the model and not
by the input.

## 5. Measurement: a melt-threshold ice model

The ice-volume variable $V$ (dimensionless, $0$ to $1$) obeys

$$\frac{\mathrm dV}{\mathrm dt}
= g\,(1-V) - \mu\,\frac{V}{1+\exp\!\bigl[-(I(t)-I_{\text{th}})/w\bigr]},$$

with growth rate $g = 1/60$ per ka, melt rate $\mu = 0.60$ per ka, threshold
$I_{\text{th}} = 0.70$, smoothing $w = 0.06$ and an initial $V = 0.5$.
Accumulation slows as ice grows; melt is switched on by a smooth step in the
forcing. Measured over the run:

| quantity | value |
|---|---|
| ice-volume range | $0.0279$ to $0.6329$ |
| mean | $0.2597$ |
| standard deviation | $0.1495$ |
| fraction of time above $V = 0.5$ | $0.058$ |
| dominant period | $100.0\ \mathrm{ka}$ |
| share of variance at periods $>60$ ka | $0.4384$ |
| fraction of time in slow growth ($\mathrm dV/\mathrm dt > 0$) | $0.797$ |
| skewness of the record | $+0.3026$ |

Four readings:

- **The response period is not a forcing period.** The forcing's dominant period
  is 23.1 ka; the response's is 100.0 ka. In a *linear* system the response
  spectrum equals the forcing spectrum multiplied by the squared modulus of a
  transfer function, so a response peak at a frequency where the forcing has
  $0.26\%$ of its power would require an enormous, and unphysical, resonance.
  The threshold supplies the missing nonlinearity.
- **The response is asymmetric.** It spends $79.7\%$ of its time growing and
  $20.3\%$ declining, and its distribution is positively skewed ($+0.3026$): a
  long slow build-up punctuated by rapid collapses, the shape conventionally
  called a sawtooth.
- **The amplitude is small in absolute terms.** $V$ ranges only from $0.028$ to
  $0.633$ of its nominal maximum, because the melt term is only active in the
  upper part of the forcing range. A model with a lower threshold would produce
  smaller cycles; the sensitivity is quantified next.
- **Phase locking.** Because melt is triggered when the (modulated) precession
  envelope crosses the threshold, the cycles lock to the envelope's period rather
  than to any individual forcing period. This is a general property of
  thresholded oscillators and is the reason a quasi-periodic forcing can produce
  a nearly periodic response.

### 5.1 Sensitivity to the threshold

| melt threshold | mean $V$ | dominant period (ka) | share of variance $>60$ ka |
|---|---|---|---|
| 0.60 | 0.2182 | 100.0 | 0.3598 |
| 0.70 | 0.2597 | 100.0 | 0.4384 |
| 0.80 | 0.3103 | 100.0 | 0.5066 |

The dominant period is robust at 100 ka across this range, while the mean state
and the concentration of variance are not: raising the threshold by $0.2$ raises
the long-period share from $0.360$ to $0.507$. A model that reproduces the period
but not the amplitude distribution has reproduced only part of the record.

## 6. What this does and does not show

**It shows** that a threshold mechanism driven by amplitude-modulated precession
can concentrate variance at a long period that the forcing barely contains, and
can produce the asymmetric sawtooth shape. Both are *necessary* properties of any
explanation of the observed cycles.

**It does not show** that this is what happened. To claim that, one would have to
show, at minimum:

1. that the reconstructed ice volume has the spectral and shape properties the
   model produces, in the same time intervals;
2. that the model's threshold and time constants are constrained by independent
   physics (ice-sheet mass balance, basal sliding, sea level) rather than chosen;
3. that competing mechanisms — ice-sheet internal dynamics, atmospheric
   carbon-dioxide changes, ocean circulation reorganisations and dust/albedo
   feedbacks — do not account for the same features;
4. that the model does not reproduce the record *equally well* under a range of
   parameter choices, which would make it unfalsifiable in its present form.

The honest summary is that the demonstration establishes a *possible* mechanism
and the arithmetic that makes it possible. Distinguishing among mechanisms is
what the proxy record and coupled ice-sheet models are for.

## 7. Worked example: how much amplification is required?

*Problem.* Suppose a linear model is required to produce as much variance at the
100 ka band as the threshold model does. Using the measured shares, what
amplification factor would the transfer function need at that band?

*Solution.*

1. Forcing share at the eccentricity band: $0.0026$.
2. Response share at the same band: $0.3073$.
3. Required power amplification: $0.3073/0.0026 = 118.2$.
4. A transfer function with $|H|^{2} = 118.2$ has $|H| = 10.9$: a response
   amplitude nearly eleven times the forcing amplitude at that frequency.

*Interpretation.* Such a resonance would have to be narrow enough to leave the
precession band's ratio ($0.1536/0.6831 = 0.225$) largely intact, which is a
strong constraint on any linear explanation. This is the quantitative form of
the "100-kyr problem": the forcing's eccentricity-band power is so small that a
linear amplifier is a strained explanation, and the observed concentration of
variance at that band is more naturally produced by a nonlinearity. **The
arithmetic does not identify the nonlinearity.** It only shows that some
nonlinearity — a threshold, a relaxation with state-dependent rate, ice-sheet
internal instability, or a carbon-cycle feedback — is required.

## 8. Assumptions and regime of validity

1. **The forcing is a synthetic dimensionless proxy.** It is not computed
   insolation. The real calculation involves the full orbital solution, the
   precession index, a latitudinal integral and calendar effects.
2. **Four frequencies and one modulation.** The real orbital solution has many
   terms; the demonstration keeps the four standard periods and a single
   modulation frequency.
3. **A single scalar ice-volume variable.** Real ice sheets have geometry,
   multiple domes, isostatic response and regional climates. A scalar cannot
   represent the response's spatial pattern.
4. **Melt controlled by insolation alone.** The model omits CO$_2$, dust,
   albedo, ocean temperature and precipitation changes, some of which are known
   to matter.
5. **Linear accumulation, thresholded ablation.** Both are idealisations;
   ice-sheet dynamics include internal instabilities that can produce cycles
   with no orbital forcing at all.
6. **Periodogram interpretation.** The spectral estimates are limited by the
   record length ($2400\ \mathrm{ka}$) and the frequency resolution; a peak at
   $100.0\ \mathrm{ka}$ in a $2400\ \mathrm{ka}$ record is resolved to about
   $\pm4\%$.
7. **The periods are astronomical, the amplitudes are not.** Do not read the
   amplitudes as statements about the real insolation.

## 9. Units and dimensional analysis

| quantity | symbol | unit | check |
|---|---|---|---|
| time | $t$ | ka | millennial; keep consistent with the periods |
| insolation proxy | $I$ | 1 (dimensionless) | a sum of unitless sines |
| growth rate | $g$ | $\mathrm{ka^{-1}}$ | so $g(1-V)$ is $\mathrm{ka^{-1}}$ |
| melt rate | $\mu$ | $\mathrm{ka^{-1}}$ | same unit as $g$ |
| ice volume | $V$ | 1 | dimensionless, bounded in $[0,1]$ |
| period | $P$ | ka | $1/f$ |

The unit check that matters here is dimensional consistency between the two
terms of $\mathrm dV/\mathrm dt$: both must be per kiloyear. Writing a growth rate
in $\mathrm{a^{-1}}$ while the periods are in ka would produce cycles 1000 times
too fast, and the error is easy to make because both terms are "per unit time".

## 10. Python demonstration

[`code/pleistocene_cycles_demo.py`](code/pleistocene_cycles_demo.py):

1. builds the synthetic forcing from the four standard periods with chosen
   amplitudes, and reports its mean and standard deviation;
2. integrates the melt-threshold ice model and reports the range, mean,
   standard deviation, growth fraction and skewness;
3. computes band-by-band variance shares for forcing and response, and the
   measured dominant period of each;
4. repeats the response calculation for three melt thresholds, showing which
   properties are robust and which are not.

It is print-only, seeded with `np.random.default_rng(20261014)`, and exits 0.

## 11. Exercises

See [`exercises/04-pleistocene-cycles-exercises.md`](exercises/04-pleistocene-cycles-exercises.md)
and [`exercises/04-pleistocene-cycles-solutions.md`](exercises/04-pleistocene-cycles-solutions.md).

## Mastery checkpoint

> **(a)** The forcing has variance shares $0.2723$ (obliquity), $0.6831$
> (precession), $0.0026$ (eccentricity). Verify that these three sum to
> $0.9580$ and state where the remainder lies.
> **(b)** The response shares are $0.2042$, $0.1536$, $0.3073$. Compute the
> response-to-forcing share ratio in each band and state which band shows
> amplification.
> **(c)** A linear response has $|H|^{2}$ independent of frequency within a band.
> Using (b), state whether a single linear transfer function can reproduce the
> response shares, and justify your answer.
> **(d)** The growth fraction is $0.797$ and the skewness $+0.3026$. Sketch the
> expected shape of $V(t)$, and state which term in the model produces it.
> **(e)** Give one observation that would falsify the threshold mechanism as the
> dominant cause of the observed cycles.

## Common pitfalls

1. **Reading a demonstration of a mechanism as an explanation.** Section 6 lists
   what would be needed to move from one to the other.
2. **Assuming eccentricity changes insolation directly.** Its effect is
   primarily through the amplitude of the precession term, which is why the
   forcing's eccentricity-band power is negligible.
3. **Using a linear transfer function to explain a nonlinear response.** The
   required amplification (Section 7) is a symptom of the mismatch.
4. **Treating spectral peaks as exact.** Resolution is limited by record length;
   quote the resolution beside the period.
5. **Forgetting that ice sheets can oscillate without orbital forcing.** Internal
   dynamics are a competing mechanism, not a detail.
6. **Mixing time units.** Growth rates in $\mathrm{ka^{-1}}$ with periods in ka,
   not $\mathrm{a^{-1}}$.

## Related modules

- [16-06 Palaeoclimate](README.md).
- [16-06-03 Abrupt Climate Change and Tipping Elements](03-abrupt-climate-change.md) —
  the threshold and hysteresis machinery used here.
- [16-04-04 Natural Variability: ENSO, NAO, PDO, Solar and Volcanic](../04-climate-system-and-feedbacks/04-natural-variability.md) —
  separating forced from internal variability in a record.
- [16-04-05 The Carbon Cycle](../04-climate-system-and-feedbacks/05-carbon-cycle.md) —
  the competing glacial-interglacial CO$_2$ mechanism.
- [13-07-03 Tectonics-Climate Feedbacks](../../13-geodynamics-tectonics/07-geomorphology-tectonics-climate/03-tectonics-climate-feedback.md).
- [20-02 Fourier and Spectral Analysis](../../20-signal-processing/02-fourier-and-spectral-analysis/README.md) —
  periodograms, leakage and resolution.
