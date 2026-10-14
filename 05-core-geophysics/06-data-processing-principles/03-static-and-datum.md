---
id: 05-06-03
title: "Static Corrections, Datum and Elevation Effects"
level: advanced
prereqs: ["05-06-01", "02-03-08"]
tags: [statics, datum, weathering, elevation, refraction, stacking]
---

# Static Corrections, Datum and Elevation Effects

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the weathering-layer static and evaluate it for a given layer
   thickness and velocity pair.
2. **Measure** the stacking attenuation caused by residual statics, and compare it
   with the Gaussian-jitter scaling law and its limits.
3. **Distinguish** elevation, weathering and residual statics, and state which is
   derived from an independent model and which must be estimated from the data.
4. **Explain** the three datums in use (flat, floating, and the seismic reference
   datum) and the consequence of choosing each.
5. **Convert** an elevation error into a travel-time error and a potential-field
   anomaly error, and state which survey types are dominated by which.
6. **Quantify** how accurate a statics solution must be, given the target bandwidth.

## Prerequisites

- [05-06-01 The Processing Pipeline](./01-processing-pipeline-concept.md) — ordering
  and the assumptions-versus-losses bookkeeping.
- [02-03-08 Reflection, Refraction and Snell's Law for Waves](../../02-physics/03-oscillations-and-waves/08-reflection-refraction.md)
  — the two-layer travel-time relation used in Section 2.
- [05-05-04 Positioning with GNSS/DGPS and Static Corrections](../05-survey-design-and-acquisition/04-positioning-gnss.md)
  — the acquisition-side treatment of elevation, including the free-air gradient.

## 1. Intuition: the near surface is a lens you must remove before you can see through it

Two stations one wavelength apart, one on rock and one on 10 m of weathered clay, do
not record the same wavefield even if the reflector below them is perfectly flat. The
difference is a *travel-time* difference of tens of milliseconds — more than a whole
wavelet period at 30 Hz. Stacking misaligned traces attenuates them, so an
uncorrected static does not merely shift the section; it **deletes the reflection**.

Three quantities are involved, and they are often conflated:

- the **elevation** of the station, which changes the path length;
- the **velocity** of the material beneath it, in particular the low-velocity
  weathering layer that varies laterally;
- the **time** at which a reference horizon would arrive, which is what the data
  measure.

Statics correction is the business of converting the first two into the third and
subtracting it.

## 2. Derivation: the weathering-layer static

Consider a two-layer model: a weathering layer of thickness $h$, velocity $v_w$, over
a substrate of velocity $v_r$. A ray that travels down and back through the
weathering layer accumulates vertical two-way time $2h/v_w$; if the same thickness
were replaced by substrate material it would accumulate $2h/v_r$. The **weathering
static** is the difference:

$$\Delta t = \frac{2h}{v_w} - \frac{2h}{v_r}
= 2h\left(\frac{1}{v_w} - \frac{1}{v_r}\right).
\tag{1}$$

With *SYNTHETIC* velocities $v_w = 600\ \mathrm{m\,s^{-1}}$ and
$v_r = 2500\ \mathrm{m\,s^{-1}}$ (a representative contrast for a near-surface
weathering pair; real values must come from a refraction survey or a downhole
measurement), equation (1) gives:

| $h$ (m) | $\Delta t$ (ms) | $\Delta t$ (samples at 2 ms) |
|---|---|---|
| 1.0 | 2.53 | 1.3 |
| 3.0 | 7.60 | 3.8 |
| 5.0 | 12.67 | 6.3 |
| 10.0 | 25.33 | 12.7 |
| 15.0 | 38.00 | 19.0 |

A 10 m thickness produces 25.3 ms, which at 30 Hz is 0.76 of a wavelet period. **A
few metres of weathering material is already more than enough to destroy a
stack**, which is why the near-surface velocity model is not a refinement but a
prerequisite.

### 2.1 Measured: the cost of leaving it uncorrected

[`code/static_correction_demo.py`](./code/static_correction_demo.py) stacks 400
traces carrying a common 30 Hz Ricker wavelet with independent Gaussian static
jitter of standard deviation $\sigma_t$, and measures the retained peak amplitude:

| $\sigma_t$ (ms) | measured attenuation | $\exp(-2\pi^{2}f^{2}\sigma_t^{2})$ at $f = 30$ Hz | frequency implied by the measurement (Hz) |
|---|---|---|---|
| 0.0 | 1.000000 | 1.000000 | — |
| 1.0 | 0.974661 | 0.982392 | 36.06 |
| 2.0 | 0.904066 | 0.931405 | 35.74 |
| 4.0 | 0.703373 | 0.752583 | 33.38 |
| 8.0 | 0.321328 | 0.320787 | 29.98 |
| 12.0 | 0.155605 | 0.077444 | 25.58 |
| 16.0 | 0.059881 | 0.010589 | 23.60 |

The Gaussian-jitter law

$$A(\sigma_t) = \exp\!\left(-2\pi^{2}f^{2}\sigma_t^{2}\right)
\tag{2}$$

is the standard scaling law for statics-induced attenuation, and the measurement
confirms it as a *scaling law* while warning against using it as a *calibration*:

- it depends on the **square** of frequency, so high frequencies die first — a
  bandwidth-limited, "washed out" deep section is the classic signature;
- the frequency implied by the measurement is **36 Hz at small $\sigma_t$**, not 30 Hz,
  because the attenuation moment of a Ricker wavelet is not its peak frequency;
- it **falls to 23.6 Hz at $\sigma_t = 16$ ms**, because the surviving spectrum
  narrows as its high frequencies are removed. So equation (2) taken literally
  *under*-predicts the loss at small jitter and *over*-predicts it at large jitter.
  This is exactly the kind of remembered formula that a measurement corrects.

### 2.2 How accurate must a statics solution be?

The demo applies a static solution that removes a fraction $\phi$ of the true jitter
and measures the stack:

| fraction removed $\phi$ | residual $\sigma_t$ (ms) | measured stack peak | prediction from equation (2) with $\sigma_t$ |
|---|---|---|---|
| 1.00 | 0.0 | 1.001039 | 1.000000 |
| 0.90 | 0.8 | 0.984514 | 0.988695 |
| 0.75 | 2.0 | 0.903591 | 0.931405 |
| 0.50 | 4.0 | 0.682146 | 0.752583 |
| 0.00 | 8.0 | 0.306183 | 0.320787 |

The uncorrected stack retains 0.306 of the amplitude; a **75 % accurate** solution
retains 0.904, and a **90 % accurate** solution retains 0.985. The practical
consequence is a specification: to keep the stack above 0.95 of its ideal amplitude
at 30 Hz, the residual static must satisfy $\exp(-2\pi^{2}30^{2}\sigma_t^{2}) \ge
0.95$, i.e. $\sigma_t \le 1.7$ ms — about 3 m of weathering thickness at the
velocities above. **Statics work is specified in milliseconds, not in "good enough".**

The prediction column is systematically optimistic at mid-range $\phi$ because the
residual jitter is not Gaussian in the same way once the largest statics are
removed; the measurement is the honest number.

## 3. The three statics, and where each comes from

| static | what it corrects | source of the values | estimable from the data alone? |
|---|---|---|---|
| **elevation static** | path length from the station to the datum | measured elevation and a *replacement velocity* | yes, given elevations |
| **weathering static** | low-velocity layer beneath the station | a refraction survey, uphole shots, or first-arrival tomography | yes, from first arrivals |
| **residual static** | everything left, including lateral velocity variation below the weathering and the statics solution's own error | cross-correlation of the data, or a surface-consistent decomposition | yes, but *only* from the data, and therefore only up to an unresolvable long-wavelength component |

The first two are **model-based**: they use an external measurement and are therefore
absolute up to that measurement's accuracy. The third is **data-derived** and is
blind to long-wavelength components, because a static shift common to a whole
spread does not change the stack's alignment. That blindness is why a statics
solution is quoted with a datum: the long-wavelength part is exactly what the datum
choice supplies.

## 4. Datum choice, and its measured consequence

A **datum** is the surface to which all travel times are referenced.

- A **flat datum** (a single elevation chosen for the whole survey) gives a single
  consistent reference, and requires the largest corrections where the topography is
  most extreme.
- A **floating datum** follows a smoothed version of the surface, so the corrections
  are small, and the datum itself carries the long-wavelength component that the
  data cannot determine.
- The **seismic reference datum (SRD)** is a survey-wide agreed elevation, usually
  chosen above the highest receiver; it is the standard reporting convention for
  land data because it makes two surveys comparable.

The demo computes an elevation static to a flat datum and to a floating datum for a
*SYNTHETIC* topography of about $\pm 40$ m relief, with a replacement velocity
$v_r = 2500\ \mathrm{m\,s^{-1}}$ and two-way time $\Delta t = 2z/v_r$:

| quantity | measured |
|---|---|
| surface elevation range | −34.5 to 37.4 m |
| static to a flat datum, spread | 57.6 ms; maximum $\lvert\Delta t\rvert$ = 29.9 ms |
| static to a floating datum (1 km smoothing), spread | 20.9 ms |
| long-wavelength part removed by floating the datum | 44.8 ms |

**The datum choice moves 44.8 ms of travel time in and out of the data**, and that
time is not recoverable from the reflection times. Every later step — velocity
analysis, NMO, depth conversion, inversion — inherits the decision. Therefore the
datum is metadata, not an internal detail: it must be reported with the data.

## 5. Elevation error in the two families of methods

The same elevation error has very different consequences in wavefield and
potential-field methods, and the two must be budgeted separately:

| method | mechanism | conversion | order of magnitude for a 1 m error |
|---|---|---|---|
| reflection seismics | travel time through the replacement medium | $2\Delta z/v_r$ | 0.8 ms at $v_r = 2500\ \mathrm{m\,s^{-1}}$ |
| gravity | free-air gradient | $2g/a$ | 0.31 mGal (derived in [05-05-04](../05-survey-design-and-acquisition/04-positioning-gnss.md)) |
| magnetics | no direct dependence; positioning error enters through the field gradient | $\partial B/\partial x \cdot \delta x$ | from 0.3 to $10^{3}$ nT/m depending on depth |

The gravity row is the one that surprises: a 1 m height error is 0.31 mGal, which is
an order of magnitude larger than any anomaly a detailed survey is looking for. This
is why gravity data are levelled, tie-lined and reduced with more care than their
station spacing would suggest.

## 6. Worked examples

### 6.1 Specifying a statics solution from the target bandwidth

A survey targets a 60 Hz bandwidth. Using equation (2) with $f = 60$ Hz and requiring
$A \ge 0.95$:

$$\sigma_t \le \frac{1}{2\pi f}\sqrt{-\ln 0.95}
= \frac{1}{2\pi \cdot 60}\sqrt{0.0513} = 0.85\ \mathrm{ms}.$$

At $v_w = 600$ and $v_r = 2500\ \mathrm{m\,s^{-1}}$, equation (1) converts 0.85 ms to
$h = 0.34$ m. **The weathering-thickness control must be better than a third of a
metre**, which is why a refraction survey or uphole shooting is required for a
high-bandwidth land survey and why "residual statics" algorithms exist: no
independent near-surface model achieves that accuracy everywhere.

### 6.2 The cost of a wrong replacement velocity

A replacement velocity of 2000 instead of $2500\ \mathrm{m\,s^{-1}}$ for a 30 m
elevation difference gives

$$\Delta t_{\text{error}} = 2 \times 30 \times \left(\frac{1}{2000} - \frac{1}{2500}\right)
= 60 \times 1.0\times10^{-4} = 6.0\ \mathrm{ms},$$

a residual static of 6 ms — by Section 2.2, enough to take the stack to about 0.75 of
its ideal amplitude at 30 Hz. **The replacement velocity must be measured, not
assumed**, and its error propagates linearly into the static.

### 6.3 A floating-datum trap

A floating datum removes the long-wavelength part of the static (44.8 ms in the
measured example). If a later depth conversion uses interval velocities derived from
those travel times, every derived depth inherits a long-wavelength tilt whose size is
$(44.8\ \mathrm{ms}) \times v/2$; at $v = 2500\ \mathrm{m\,s^{-1}}$ that is 56 m. A
56 m systematic depth error is larger than most target thicknesses, and it is
invisible in the data because it is exactly the component the datum removed.

### 6.4 Why the datum is a *reporting* requirement

The measured 44.8 ms of long-wavelength travel time in Section 4 is exactly the
quantity that two surveys must agree on before they can be merged. If one contractor
processes to a floating datum and another to a flat datum, the two datasets differ by a
time shift that varies across the area by tens of milliseconds, and stacking or
merging them will produce a false structure along the boundary — a step that looks
like a fault. The same argument applies to potential fields, where the analogue of the
datum is the *reference level* used for the free-air and Bouguer reductions: two
gravity surveys reduced with different densities or reference ellipsoids differ by a
long-wavelength field that is indistinguishable in shape from a deep basin.

The reporting convention that avoids this is to state, for every processed dataset:

1. the datum elevation (or the reference surface) and its definition;
2. the replacement velocity used above it;
3. the reference ellipsoid and the normal-gravity formula, for potential fields;
4. the correction density used for the Bouguer term, if any.

Items 1–2 for seismic and 3–4 for potential fields are the minimum needed for two
datasets to be compared at all, and they belong in the metadata, not in a processing
report's prose.

## 7. Assumptions

1. **Vertical ray paths in the near surface.** Equation (1) assumes the weathering
   correction is a vertical path. For a refracted or diving first arrival, the
   effective correction differs, and the standard practice of using first-arrival
   tomography avoids the assumption.
2. **A two-layer model.** Real near surfaces are gradational; a single $h$ and $v_w$
   are a parameterisation, and the residual static absorbs the error.
3. **Stationarity across the spread.** Surface-consistent methods assume the static
   depends on the *surface* position of the source or receiver, not on the raypath —
   which fails for long offsets and dipping structure.
4. **Independent, zero-mean residual jitter.** Real residual statics are spatially
   correlated, which means the effective $\sigma_t$ in equation (2) is not the
   pointwise value; correlated statics attenuate the stack more than uncorrelated
   ones of the same standard deviation.
5. **Gaussian jitter for equation (2).** The measurement above shows that even the
   *shape* of the wavelet changes the implied frequency, so the formula is a scaling
   law. A layered or systematic static has a different effect entirely.
6. **Synthetic parameters.** Velocities, thicknesses and noise levels in this lesson
   are stated synthetic values for demonstration.

## 8. Units and dimensional analysis

Equation (1):

$$\left[\frac{h}{v}\right] = \frac{\mathrm{m}}{\mathrm{m\,s^{-1}}} = \mathrm{s},$$

so the static is a time; the factor 2 is the two-way path and is dimensionless. The
argument of equation (2) must be dimensionless:
$[2\pi^{2}f^{2}\sigma_t^{2}] = \mathrm{s^{-2}\cdot s^{2}} = 1$, as required — a
useful check because writing $\sigma_t$ in milliseconds while $f$ is in hertz is a
factor-$10^{6}$ error inside a square root, and it is the most common arithmetic slip
in statics work.

For the elevation conversions in Section 5,
$[2\Delta z/v_r] = \mathrm{m/(m\,s^{-1})} = \mathrm{s}$ and
$[(2g/a)\Delta z] = \mathrm{s^{-2}\cdot m} = \mathrm{m\,s^{-2}}$, i.e. an
acceleration — convert to mGal by dividing by $10^{-5}$.

## 9. Python demonstration

[`code/static_correction_demo.py`](./code/static_correction_demo.py) produces every
number in Sections 2 and 4. The fractional-sample shift is a phase ramp, which keeps
the test free of interpolation artefacts:

```python
def frac_shift(y, shift_samples):                 # zero-phase shift
    k = 2 * np.pi * np.fft.rfftfreq(y.size)
    return np.fft.irfft(np.fft.rfft(y) * np.exp(-1j * k * shift_samples), n=y.size)
```

The statics themselves come from equation (1) and from the two-way elevation time,
so the measured attenuation is not contaminated by a shift implementation that is
inconsistent with the model being tested.

## 10. Exercises, common mistakes, applications

Companion problem sets:
[`exercises/03-static-and-datum-exercises.md`](./exercises/03-static-and-datum-exercises.md)
and [`exercises/03-static-and-datum-solutions.md`](./exercises/03-static-and-datum-solutions.md).

### Common mistakes

1. **Applying statics after stacking.** Alignment must precede averaging; there is no
   second chance.
2. **Assuming a replacement velocity.** Section 6.2: a 20 % error gives a 6 ms static.
3. **Quoting a statics solution without its datum.** The long-wavelength component is
   a datum decision, not a data measurement.
4. **Using the Gaussian formula as a calibration.** The measured implied frequency
   varies from 36 to 24 Hz over the range tested.
5. **Forgetting that residual statics cannot see long wavelengths.** That is a
   property of the method, not a limitation of the software.
6. **Budgeting seismics and gravity with the same elevation tolerance.** 1 m is 0.8 ms
   for one and 0.31 mGal for the other.

### Real-world applications

- **Land seismic processing.** Statics is the first and largest correction applied to
  raw shot gathers, and it is where the majority of processing effort goes in
  areas of rough topography or thick weathering.
- **Refraction statics and first-arrival tomography.** The near-surface velocity model
  is the input to the weathering static; its resolution is the resolution of the
  static.
- **Gravity and magnetic surveys.** Elevation and terrain corrections are the
  potential-field analogue of statics, and the free-air term dominates the error
  budget.
- **4-D and repeat surveys.** The residual static between epochs is a *change*; if it
  is not separated from the 4-D signal, the survey measures its own field crew.

## 11. Further reading

- **Yilmaz, Ö. (2001). *Seismic Data Analysis* (2nd ed.). SEG.** Chapters on statics
  and near-surface corrections; the standard practitioner account of the models in
  Sections 2–4.
- **Sheriff, R. E., & Geldart, L. P. (1995). *Exploration Seismology* (2nd ed.).
  Cambridge University Press.** Statics and datum conventions.
- **Hinze, W. J., von Frese, R. R. B., & Saad, A. H. (2013). *Gravity and Magnetic
  Exploration* (2nd ed.). Cambridge University Press.** Elevation, free-air and
  terrain corrections; the potential-field counterpart.
- **Cox, M. (1999). *Static Corrections for Seismic Reflection Surveys*. SEG
  Geophysical Reference Series.** The dedicated monograph on statics. Level:
  advanced practitioner.
- **USGS, seismic and potential-field method pages** — <https://www.usgs.gov> — for
  documented practice in national-scale surveys.

> Note on citations: bibliographic details are given so you can locate the works.
> This repository does not host or reproduce copyrighted text, and you should
> confirm current availability and editions through your library before citing them.

## 12. Related lessons

- [05-06-01 The Processing Pipeline](./01-processing-pipeline-concept.md) — why statics must precede stacking.
- [05-06-02 Noise Suppression](./02-noise-suppression.md) — the $\sqrt{N}$ gain that statics protect.
- [05-06-04 Gain Control, Amplitude Recovery and True-Amplitude Handling](./04-gain-and-amplitude.md) — the other half of preserving what the stack would otherwise lose.
- [05-05-04 Positioning with GNSS/DGPS and Static Corrections](../05-survey-design-and-acquisition/04-positioning-gnss.md) — the acquisition-side elevation budget.
- [02-03-08 Reflection, Refraction and Snell's Law for Waves](../../02-physics/03-oscillations-and-waves/08-reflection-refraction.md) — the two-layer travel-time relation.

## 13. Self-assessment checklist

- [ ] I can derive the weathering static and evaluate it in milliseconds.
- [ ] I can state the stacking attenuation law and its measured limits.
- [ ] I can specify a required statics accuracy from a target bandwidth.
- [ ] I can distinguish elevation, weathering and residual statics and name the source of each.
- [ ] I can explain why a residual-statics solution is blind to long wavelengths.
- [ ] I can state the three datums and the measured time a datum choice moves.
- [ ] I can convert an elevation error to a seismic time error and to a gravity error.
- [ ] I can list the assumptions of the two-layer static model and say what absorbs their failure.
