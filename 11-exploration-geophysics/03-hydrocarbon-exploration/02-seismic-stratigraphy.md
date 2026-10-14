---
id: 11-03-02
title: "Seismic Stratigraphy and Sequence Interpretation"
level: doctoral
prereqs: ["11-03-01", "06-09-09", "04-03-04", "04-04-02"]
tags: [exploration-geophysics, seismic-stratigraphy, sequence-stratigraphy, interpretation, resolution]
---

# Seismic Stratigraphy and Sequence Interpretation

**All models and data in this module are SYNTHETIC.** The wedge model, the
wavelet, the sea-level curve and the subsidence rates below are chosen teaching
values, not measurements from any basin. No field, well or company is described.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the interference factor $2|\sin(\pi f\Delta t)|$ that governs the
   response of a thin bed, and **explain** why it forces a thickness-dependent
   amplitude.
2. **Compute** the narrow-band tuning condition $\Delta t = 1/(2f_0)$, hence
   $h = \lambda/4$, and **compare** it with the value measured for a chosen
   broadband wavelet.
3. **State** the two different resolution thresholds (amplitude maximum and
   readable thickness) and **use** the right one for a stated question.
4. **Classify** reflection terminations and **explain** why a termination is
   evidence for a surface only in 3-D, migrated data.
5. **Derive** the accommodation balance from eustasy and subsidence and
   **classify** systems tracts from rates rather than from water depth.
6. **Quantify** when an amplitude anomaly is a thickness effect rather than a
   property change, and **state** the assumption that breaks the equivalence.
7. **Interpret** a synthetic wedge, reporting an admitted range rather than a
   single thickness.

## Prerequisites

- [11-03-01 Reflection Seismic in Exploration](01-seismic-in-exploration.md) —
  resolution, Fresnel zone, fold and sampling.
- [06-09-09 Structural and Stratigraphic Interpretation](../../06-seismology/09-reflection-seismology/09-interpretation-reflection.md) —
  the mechanics of picking and mapping reflections.
- [04-03-04 Sedimentary Basins: Formation, Fill and Subsidence](../../04-earth-science-geology/03-geologic-time-and-stratigraphy/04-sedimentary-basins.md) —
  subsidence and accommodation.
- [04-04-02 Fault Geometry, Kinematics and Fault Classification](../../04-earth-science-geology/04-structural-geology/02-faults.md) —
  the structural features that sequence boundaries are mapped against.

## 1. What a seismic surface is

Seismic stratigraphy rests on one strong assumption: **a continuous reflection
approximates a depositional (chronostratigraphic) surface**. The assumption is
not an identity. A reflection is produced wherever acoustic impedance changes,
and impedance changes at a lithological boundary that may cut across time —
a diagenetic front, a fluid contact, an unconformity surface whose own age
varies laterally, or a thin-bed interference pattern that exists only where the
beds happen to be that thickness. The interpreter's craft is largely about
deciding, surface by surface, whether the assumption holds.

There is also a resolution statement attached to the assumption. If a
condensed interval is 5 m thick, in a 30 Hz wavelet with $\lambda/4 = 25$ m at
$3.0\ \mathrm{km\,s^{-1}}$, that interval and the surfaces above and below it
are inside a single wavelet. It is one event. Whether the geologically
meaningful surface is its top, its base or something inside it cannot be
recovered from that wavelet — the answer will change if the acquisition
frequency changes. **A mapped surface is a statement about a wavelet as much as
about a rock**, and the honest interpretation states the wavelet.

## 2. Thin beds: the interference factor

Put two reflectors of opposite sign, $+R$ and $-R$, $\Delta t$ apart, and
convolve with the wavelet $w$:

$$d(t) = R\left[w(t) - w(t-\Delta t)\right].$$

In the frequency domain,

$$D(\omega) = R\,W(\omega)\left(1 - e^{-i\omega\Delta t}\right)
= R\,W(\omega)\,e^{-i\omega\Delta t/2}\,
\underbrace{2i\sin(\omega\Delta t/2)}_{\text{interference factor}} .$$

So the *spectrum* of the composite is the spectrum of the wavelet multiplied by
the oscillating interference factor $2|\sin(\pi f \Delta t)|$. This one relation
explains most of what follows:

- **Amplitude depends on thickness, non-linearly.** For $\Delta t \to 0$ the
  interference factor vanishes and the bed disappears, exactly as the physics
  requires (two equal and opposite reflections cancel).
- **Amplitude is maximal** where $|\sin(\pi f \Delta t)|$ is maximal for the
  frequencies the wavelet actually carries. For a narrow-band wavelet centred on
  $f_0$, that is $\pi f_0 \Delta t = \pi/2$, i.e.

  $$\Delta t = \frac{1}{2f_0} \quad\Longrightarrow\quad
  h_{\text{tune}} = \frac{v}{4f_0} = \frac{\lambda}{4},$$

  which is where the $\lambda/4$ rule of thumb comes from.
- **There are side lobes**: $|\sin(\pi f\Delta t)|$ oscillates, so the amplitude
  vs thickness curve is not monotonic. Interpretation schemes that assume
  amplitude $\propto$ thickness fail once the bed reaches the first side lobe.

### 2.1 What a broadband wavelet actually does

The narrow-band result is exact for an infinite-bandwidth-free wavelet. The
demonstration measures the same thing for a 30 Hz Ricker, $\rho = 3.0\ \mathrm{km\,s^{-1}}$
and $R = \pm0.10$:

| $h$ (m) | true $\Delta t$ (ms) | composite amplitude | read-off $\Delta t$ (ms) |
|---|---|---|---|
| 2.0 | 1.3 | 0.049 | 11.2 |
| 5.0 | 3.3 | 0.119 | 11.2 |
| 10.0 | 6.7 | 0.215 | 11.4 |
| 15.0 | 10.0 | 0.273 | 12.0 |
| 20.0 | 13.3 | 0.289 | 13.0 |
| 25.0 | 16.7 | 0.271 | 15.0 |
| 30.0 | 20.0 | 0.239 | 18.4 |
| 40.0 | 26.7 | 0.204 | 26.4 |
| 50.0 | 33.3 | 0.200 | 33.4 |
| 60.0 | 40.0 | 0.200 | 40.0 |

Three facts must be read off this table together:

1. **The amplitude maximum is at $h = 19.5\ \mathrm{m}$**, and $19.5 = 0.195\,v/f_0
   = 0.78\,\lambda/4$. The broadband coefficient is *below* the narrow-band
   $\lambda/4$, because a broad spectrum contains frequencies that have already
   passed their own interference maximum at that thickness.
2. **The read-off thickness saturates near the wavelet's own peak-to-trough
   separation**: a 5 m bed reads 11.2 ms and a 10 m bed reads 11.4 ms, against
   true values of 3.3 and 6.7 ms. Below tuning, thickness is not measured; a
   number in milliseconds is produced, and it is the wavelet's.
3. **The read-off becomes accurate to 10% at 16.95 m**, i.e. $0.17\,v/f_0 =
   0.68\,\lambda/4$ for this wavelet. The demonstration repeats the measurement
   at 15, 20 and 50 Hz and finds the same two coefficients
   ($0.195\,v/f_0$ and $0.17\,v/f_0$) at every frequency, and the same
   $\lambda/4$ ratio (0.78) for the tuning maximum.

**The rule is therefore:** quote $\lambda/4$ as the order of magnitude, and
quote the *measured* coefficients for the wavelet you are using. A paper that
states "the bed is 12 m thick, below the tuning thickness" without naming the
wavelet has not stated anything reproducible.

### 2.2 Detection is not resolution

The demonstration sets noise at 5% of the thick-bed composite amplitude
(0.0100 for $2R = 0.20$) and measures:

| $h$ (m) | amplitude | amplitude/noise | read-off/true |
|---|---|---|---|
| 0.5 | 0.012 | 1.2 | 33.6 |
| 1.0 | 0.024 | 2.4 | 16.8 |
| 2.0 | 0.049 | 4.9 | 8.4 |
| 5.0 | 0.119 | 11.9 | 3.4 |
| 10.0 | 0.215 | 21.5 | 1.7 |
| 20.0 | 0.289 | 28.9 | 0.98 |
| 50.0 | 0.200 | 20.0 | 1.00 |

A 2 m bed returns an amplitude 4.9× the noise and is entirely unresolvable: the
amplitude says a *sub-tuning* bed is there, and cannot say how thick it is. This
is the quantitative version of the practitioner's rule that thin beds are
"detectable but not resolvable", and it is why amplitude anomalies on a
sub-tuning interval must be inverted jointly for thickness and impedance — the
subject of [11-03-04](04-seismic-inversion-reservoir.md).

## 3. Terminations, and why 3-D is not optional

Seismic stratigraphy classifies the geometric relationships at surfaces:

- **onlap** — younger strata terminate against a surface going updip;
- **downlap** — strata terminate downdip against a surface;
- **toplap** — strata terminate updip beneath a surface by truncation of the
  topset;
- **truncation (erosional)** — older strata are cut off by a younger surface.

Each is a statement about stratal geometry, and each is only as reliable as the
imaging. In 2-D the same feature can be produced by a reflector geometry that is
entirely out of plane: a channel trending obliquely to the line appears as an
onlapping wedge with no channel, and its apparent position moves as the line
spacing changes ([11-03-01 §6](01-seismic-in-exploration.md)). Onlap mapped on
one 2-D line is an hypothesis; the same onlap mapped on a migrated 3-D volume,
where the surface can be followed in closed loops around the feature, is
evidence. This is the interpretation-level reason for the acquisition-level
argument of the previous lesson.

## 4. Accommodation, eustasy and systems tracts

Sequence stratigraphy replaces a list of sea-level positions with a **rate
balance**. Define, for a shelf at a reference datum:

$$\text{accommodation rate} = \frac{\mathrm{d}e}{\mathrm{d}t} + \dot{s},$$

where $e(t)$ is eustatic sea level and $\dot{s}$ is tectonic subsidence (positive
downward). Three regimes follow, and they define the systems tracts:

| condition | regime | tract |
|---|---|---|
| rate $< 0$ (relative sea level falling faster than it can be filled) | forced regression | lowstand / sequence boundary |
| $0 \le$ rate $>$ sediment supply | transgression | transgressive systems tract |
| $0 <$ rate $\le$ sediment supply | normal regression | highstand systems tract |

The demonstration integrates a synthetic 1 Myr cycle: eustatic amplitude 40 m
with a 1 Myr period, subsidence 60 m/Myr, sediment supply 50 m/Myr. Printing the
rate at 0.05 Myr steps gives 10 transgressive steps, 2 highstand steps and 8
forced-regression steps, with the accommodation rate running from
$+307\ \mathrm{m\,Myr^{-1}}$ at the fastest rise to $-187\ \mathrm{m\,Myr^{-1}}$
at the fastest fall.

The result is worth stating as a design principle: **the sequence boundary is
set by whether the fall outpaces subsidence, not by a sea-level value.** With
60 m/Myr of subsidence, an 80 m peak-to-peak eustatic cycle must fall at more
than 60 m/Myr to create a forced regression — which it does near the inflexion
of the sine, and not at the trough, where the rate is zero. An interpreter who
maps sequence boundaries by finding "the lowstand" will place them at the wrong
horizon, because the trough of relative sea level is not the fastest fall.

## 5. Worked examples

### Example 1 — thickness from amplitude, honestly

A 30 Hz wavelet, $v = 3.0\ \mathrm{km\,s^{-1}}$ ($\lambda = 100\ \mathrm{m}$),
$R = \pm 0.10$, noise 5% of the thick-bed amplitude. An anomaly has composite
amplitude 0.119, i.e. 11.9× the noise.

- The demonstration's curve places $h = 5.0\ \mathrm{m}$ at amplitude 0.119.
- But the *same* amplitude is produced by any thickness whose interference
  factor has the same magnitude at the wavelet's frequencies; the curve is not
  monotonic, so a second solution exists and can only be excluded with
  additional information (a lateral thickness trend, a well tie, or a
  higher-frequency dataset).
- The honest statement is: **detected, sub-tuning, thickness in the range
  where the curve is single-valued — here below 20 m — conditional on
  $R = 0.10$.** Change $R$ and the inferred thickness changes, which is the
  second non-uniqueness.

### Example 2 — the smallest resolvable interval at depth

At 2.5 km with $v = 3.0\ \mathrm{km\,s^{-1}}$ and a 30 Hz wavelet,
$\lambda/4 = 25\ \mathrm{m}$. With an overburden attenuation that leaves the
dominant frequency at 20 Hz, $\lambda/4 = 37.5\ \mathrm{m}$; at 15 Hz,
$50\ \mathrm{m}$. The same physical bed that is resolvable at 500 m depth is
not resolvable at 3 km. A sequence-stratigraphic framework built on a shallow
test line and applied to a deep prospect silently changes its resolution limit
by a factor of two; the framework has to be re-measured, not stretched.

### Example 3 — accommodation arithmetic

For $e(t) = 40\sin(2\pi t/1\ \mathrm{Myr})$ m and subsidence 60 m/Myr:

$$\frac{\mathrm{d}e}{\mathrm{d}t} = 80\pi\cos(2\pi t)\ \mathrm{m\,Myr^{-1}},$$

so the accommodation rate is $80\pi\cos(2\pi t) + 60$, which ranges over
$60 - 80\pi = -191.3$ to $60 + 80\pi = +311.3\ \mathrm{m\,Myr^{-1}}$. The
demonstration's step-sampled values, $-187$ to $+307$, bracket inside that
range because a 0.05 Myr sampling misses the exact extremes — a small reminder
that a rate is only ever evaluated where horizons are picked.

## 6. Assumptions and regime of validity

1. **The chronostratigraphic assumption.** A continuous reflection need not be
   a time line; diagenetic fronts, fluid contacts and thin-bed interference all
   violate it locally.
2. **A known, stationary wavelet.** Tuning curves, amplitude maps and inversion
   all assume phase and bandwidth are known and constant. Lateral wavelet
   variation is common and produces lateral amplitude variation that is pure
   artefact.
3. **Two reflectors, one bed.** The interference algebra assumes a single thin
   bed. A thin *package* has many interfering reflections, and its composite
   amplitude is not simply thickness-dependent.
4. **Normal incidence.** The wedge analysis is zero-offset. Angle-dependent
   interference behaves differently, which couples the problem to AVO
   ([06-09-05](../../06-seismology/09-reflection-seismology/05-amplitude-vs-offset.md)).
5. **Rate-based sequence stratigraphy assumes an approximately 1-D shelf.**
   Lateral sediment supply, along-strike transport, and tectonic tilting break
   the accommodation balance.
6. **Systems tracts are model constructs.** They are useful organising
   hypotheses, not observations, and different workers apply different rate
   thresholds.
7. **Migration and 3-D coverage.** Terminations, channels and onlap geometries
   are interpretation-grade only in migrated 3-D data.

## 7. Units and dimensional consistency

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| bed thickness | $h$ | m | |
| two-way time | $\Delta t$ | s | $2h/v$ |
| interference factor | $2\sin(\pi f\Delta t)$ | 1 | argument dimensionless: Hz × s |
| tuning thickness | $v/(4f_0)$ | m | (m/s)/Hz |
| accommodation rate | | m/Myr | length/time |
| eustatic rate | | m/Myr | length/time |

Note that $\pi f \Delta t$ must be dimensionless: if you compute the interference
factor with $\Delta t$ in milliseconds and $f$ in Hz you will be wrong by 10³ in
the argument, and the curve will look plausible.

## 8. Python demonstration

`code/seismic_stratigraphy_demo.py` prints:

1. the wedge table (true $\Delta t$, composite amplitude, read-off $\Delta t$);
2. the measured tuning thickness at 15, 20, 30 and 50 Hz against $\lambda/4$,
   plus the thickness at which the read-off becomes accurate to 10%;
3. the read-off plateau table;
4. the detectability table against a stated 5% noise level;
5. the systems-tract table with the accommodation rate at each step, and the
   count of transgressive, highstand and forced-regression steps.

It is print-only, seeded with `np.random.default_rng(20261014)` and exits 0.
Every number in this lesson is printed by it or derived above.

## 9. Exercises

- [`exercises/02-seismic-stratigraphy-exercises.md`](exercises/02-seismic-stratigraphy-exercises.md)
- [`exercises/02-seismic-stratigraphy-solutions.md`](exercises/02-seismic-stratigraphy-solutions.md)

## Mastery checkpoint

> A wedge of $R = \pm0.10$ in a $3.0\ \mathrm{km\,s^{-1}}$ medium is imaged with
> a 25 Hz Ricker. **(a)** Compute $\lambda/4$ and predict, using the
> demonstration's coefficients, both the tuning thickness and the thickness at
> which the read-off becomes accurate to 10%. **(b)** An amplitude anomaly on the
> wedge is 6× the noise (noise = 5% of the thick-bed amplitude): decide whether
> it is a thick bed or a thin one, and state what additional measurement would
> settle it. **(c)** With subsidence 40 m/Myr and a eustatic cycle of 30 m
> amplitude and 0.5 Myr period, compute the accommodation-rate range and state
> whether forced regression occurs.

## Common pitfalls

1. **Reading thickness from travel time below tuning.** The read-off saturates
   at the wavelet's own peak-to-trough separation; the number produced is the
   wavelet's property, not the bed's.
2. **Assuming amplitude $\propto$ thickness.** The interference factor is
   oscillatory: amplitude is non-monotonic in thickness and also depends on $R$.
3. **Using $\lambda/4$ as if it were exact.** It is the narrow-band condition;
   the measured broadband coefficients here are $0.78\,\lambda/4$ (amplitude
   maximum) and $0.68\,\lambda/4$ (readable thickness).
4. **Mapping terminations on 2-D data.** Out-of-plane geometry produces
   identical apparent terminations.
5. **Placing sequence boundaries at the sea-level minimum.** The boundary is a
   rate condition; the minimum of the curve is not the fastest fall.
6. **Forgetting that a mapped surface inherits the wavelet.** A 5 m surface and
   a 25 m surface are the same event at 30 Hz, and different events at 60 Hz.

## Related modules

- [11-03-01 Reflection Seismic in Exploration](01-seismic-in-exploration.md) —
  the resolution and sampling framework this lesson applies.
- [06-09-09 Structural and Stratigraphic Interpretation](../../06-seismology/09-reflection-seismology/09-interpretation-reflection.md) —
  the mechanics of interpretation, of which this is the stratigraphic half.
- [04-03-04 Sedimentary Basins: Formation, Fill and Subsidence](../../04-earth-science-geology/03-geologic-time-and-stratigraphy/04-sedimentary-basins.md) —
  the subsidence that makes accommodation.
- [04-06-01 Source, Reservoir, Seal and Trap](../../04-earth-science-geology/06-petroleum-and-mineral-systems/01-petroleum-system.md) —
  what the interpreted surfaces are used to define.
- [11-03-03 Reservoir Characterisation and Property Prediction](03-reservoir-characterisation.md) —
  what comes after the surfaces are mapped.
- [11-07-02 Case Study: Basin Analysis and Play Assessment](../07-exploration-case-studies/02-case-study-basin.md) —
  where sequence interpretation is combined with play assessment.

## Further reading

- Sheriff, R. E., & Geldart, L. P. (1995). *Exploration Seismology* (2nd ed.).
  Cambridge University Press. Level: textbook. Resolution, tuning and wavelet
  interference.
- Yilmaz, Ö. (2001). *Seismic Data Analysis*. Society of Exploration
  Geophysicists. Level: reference. Deconvolution and wavelet processing, which
  decide the effective wavelet that the tuning curve must assume.
- Telford, W. M., Geldart, L. P., & Sheriff, R. E. (1990). *Applied
  Geophysics* (2nd ed.). Cambridge University Press. Level: textbook. The
  stratigraphic-interpretation chapter.

> Bibliographic details are given so you can locate the works; this repository
> does not host or reproduce copyrighted text.
