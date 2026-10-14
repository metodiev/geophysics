# Module 06-05 — Attenuation and Anelasticity

**Stages:** graduate → doctoral · **Prerequisites:** modules 06-01 and 06-02;
complex analysis and linear algebra.

This module measures how seismic energy disappears. It is built around one honest
difficulty: **two physically unrelated mechanisms remove amplitude from a direct
arrival in the same way.** Intrinsic attenuation converts organised motion into
heat and is a material property, tied to temperature, fluid and melt. Scattering
moves the same energy into the coda and is a property of the *structure*, not of
the material. A coherent-amplitude measurement sees their sum. Every lesson
either derives that ambiguity, quantifies it, or provides a measurement that
narrows it — and every lesson states which of the three it is doing.

The second difficulty is that $Q$ is not a number in the way a velocity is. A
measured $Q$ is a **band average** of a function that is not flat, and a medium
with frequency-independent $Q$ over all frequencies cannot exist at all: the
Kramers-Kronig relation forces a divergence. So attenuation is inseparable from
dispersion, and any quoted $Q$ carries an implicit statement about the band.
The demonstrations make both statements numerically, not rhetorically.

The third difficulty is the step people actually want: from a $Q$ map to a
temperature map. That step multiplies the quantity by a sensitivity of order
$H^{*}/(RT^{2})$ per kelvin — enormous, and therefore a powerful amplifier of any
error in the activation enthalpy, in the band, or in the scattering correction.
The final lesson carries the arithmetic through and lists the effects that a
low-$Q$ anomaly cannot distinguish.

All models and data in this module are **SYNTHETIC**. No real station, event or
waveform is used, and no observational $Q$ is quoted as a measurement.

## Learning objectives

By the end of this module you will be able to:

1. Derive $\alpha = \pi f/(Q v)$ from the per-cycle energy definition, and
   distinguish $Q$, $\alpha$ and $t^{*}$ with units.
2. Derive the two-station spectral-ratio estimator, state exactly what cancels,
   and compute the standard error of a $Q$ from its fit geometry.
3. Derive the rise-time relation from the causal Lorentzian impulse response, and
   explain why widths adding linearly makes the slope source-independent.
4. Quantify the band-average bias of a quoted $Q$ and explain why constant $Q$
   over an unbounded band is impossible.
5. Derive and test the additivity rule
   $1/Q_{\text{app}} = 1/Q_{\text{int}} + 1/Q_{\text{scat}}$, and measure the
   apparent $Q$ of a purely elastic random medium.
6. Design a two-band frequency test that discriminates scattering from intrinsic
   absorption, including its false-positive and false-negative modes.
7. Formulate and solve the linearised attenuation-tomography problem, exhibit its
   null space, and report an image as a smoothed field with a stated resolution.
8. Derive the temperature sensitivity of an anelastic relaxation and critique the
   inference from a $Q$ anomaly to a temperature anomaly.

## Prerequisites

- [06-01 Elastic Wave Propagation](../01-elastic-wave-propagation/README.md) —
  elastic moduli, P and S waves, scattering and coda.
- [06-02 Ray Theory and Travel Times](../02-ray-theory-and-travel-times/README.md) —
  ray paths, travel time, and the geometric terms that a spectral ratio cancels.
- [03-10 ObsPy and Seismic Data](../../03-scientific-computing/10-obspy-and-seismic-data/README.md) —
  spectra, tapering and filtering of the windows used here.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Measuring Q: Spectral Ratio, Rise Time, Multiple Methods](01-attenuation-measurement.md) | graduate | Derive $\alpha = \pi f/(Qv)$ and $\mathrm{FWHM} = t^{*}$; a $Q$ without its band is not a measurement |
| 02 | [Separating Scattering from Intrinsic Attenuation](02-scattering-vs-intrinsic.md) | doctoral | A purely elastic random stack returns $Q \approx 129$; the two-band test is the first discriminator |
| 03 | [Attenuation Tomography and Temperature Interpretation](03-attenuation-tomography.md) | doctoral | Eight exact null directions in a 30-parameter problem; a $Q$ map is not a temperature map |

## Suggested path

**If you are new to attenuation:** lessons 01–03 in order, running each
demonstration. Read the *tables* before the text: the numbers are the argument.

**If you already measure $Q$:** read 01 §5 (the uncertainty budget), then 02 in
full — the elastic random stack's apparent $Q$ is the result that changes
practice.

**If you are preparing a research project:** 02 §6–§7 and 03 §3–§7, plus the
★★★ exercises for both. The null-space and temperature-sensitivity arithmetic is
the part that ends up in a referee's objection.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-attenuation-measurement.md`](01-attenuation-measurement.md) | Lesson 01 |
| [`02-scattering-vs-intrinsic.md`](02-scattering-vs-intrinsic.md) | Lesson 02 |
| [`03-attenuation-tomography.md`](03-attenuation-tomography.md) | Lesson 03 |
| [`exercises/01-attenuation-measurement-exercises.md`](exercises/01-attenuation-measurement-exercises.md) | Exercises, lesson 01 |
| [`exercises/01-attenuation-measurement-solutions.md`](exercises/01-attenuation-measurement-solutions.md) | Worked solutions, lesson 01 |
| [`exercises/02-scattering-vs-intrinsic-exercises.md`](exercises/02-scattering-vs-intrinsic-exercises.md) | Exercises, lesson 02 |
| [`exercises/02-scattering-vs-intrinsic-solutions.md`](exercises/02-scattering-vs-intrinsic-solutions.md) | Worked solutions, lesson 02 |
| [`exercises/03-attenuation-tomography-exercises.md`](exercises/03-attenuation-tomography-exercises.md) | Exercises, lesson 03 |
| [`exercises/03-attenuation-tomography-solutions.md`](exercises/03-attenuation-tomography-solutions.md) | Worked solutions, lesson 03 |
| [`code/spectral_ratio_q_demo.py`](code/spectral_ratio_q_demo.py) | Two-receiver $Q$, bias, scatter, band penalty, band-average bias |
| [`code/kk_dispersion_causality_demo.py`](code/kk_dispersion_causality_demo.py) | Causality, the Lorentzian pulse, dispersion from the amplitude |
| [`code/scattering_vs_intrinsic_demo.py`](code/scattering_vs_intrinsic_demo.py) | Exact transmission of a random stack; apparent $Q$; two-band test |
| [`code/absorption_band_demo.py`](code/absorption_band_demo.py) | How many relaxations a "constant $Q$" needs; band-edge cost |
| [`code/tstar_tomography_demo.py`](code/tstar_tomography_demo.py) | $t^{*}$ precision, null space, damping |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib and
ObsPy:

```bash
cd 06-seismology/05-attenuation-and-anelasticity/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python spectral_ratio_q_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python kk_dispersion_causality_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python scattering_vs_intrinsic_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python absorption_band_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python tstar_tomography_demo.py
```

Every demo prints labelled results **with units**, uses a fixed random seed, and
exits 0. They are print-only — no plots are produced — and they require no
network access. The scattering demonstration averages 4000 realisations and takes
about $16\ \mathrm{s}$; the others finish in under a second.

## Mastery checkpoint

Complete this without notes:

> A $60\ \mathrm{km}$ path in a medium with $v = 3400\ \mathrm{m\,s^{-1}}$ gives
> a spectral-ratio slope, fitted over $[0.5, 8]\ \mathrm{Hz}$ with
> $\sigma_y = \sqrt{2}$ at 40 frequencies, of $m = 0.55\ \mathrm{Hz^{-1}}$.
> **(a)** Compute $Q_{\text{app}}$, $t^{*}$ and $\alpha$ at $4\ \mathrm{Hz}$,
> with units. **(b)** Predict $\sigma_Q/Q$ from the fit geometry and state whether
> the number is a $1\%$ measurement. **(c)** A companion coda measurement gives
> $Q_{\text{coda}} = 300$; compute $Q_{\text{int}}$ under the stated assumption
> and state the assumption. **(d)** The measured $Q$ implies a temperature
> contrast of $50\ \mathrm{K}$ for $H^{*} = 300\ \mathrm{kJ\,mol^{-1}}$ at
> $1000\ \mathrm{K}$; list the two effects that could produce the same anomaly
> with no temperature change, and the measurement that would test each.

A worked version appears in the lesson-03
[solutions](exercises/03-attenuation-tomography-solutions.md), with the estimator
arithmetic in the lesson-01
[solutions](exercises/01-attenuation-measurement-solutions.md).

## Common pitfalls across this module

1. **Quoting $Q$ without its band.** The band is part of the measurement, not a
   caveat.
2. **Confusing $t^{*}$ with $Q$.** They differ by the travel time, i.e. by a
   velocity model.
3. **Reading an apparent $Q$ as a material property.** $Q_{\text{app}} \le
   Q_{\text{int}}$, and only a discriminator upgrades the bound.
4. **Fitting one band and naming a mechanism.** Two models fit any single-band
   number exactly.
5. **Reporting a pixel value from a damped inversion.** The image is a smoothed
   field.
6. **Mapping $Q$ to temperature without stating the activation enthalpy, the
   band, and the scattering correction.**
7. **Using a non-dispersive propagator with an attenuating model**, producing
   travel times inconsistent with the attenuation.

## Related modules

- [06-01 Elastic Wave Propagation](../01-elastic-wave-propagation/README.md) —
  the elastic moduli whose imaginary parts $Q$ describes.
- [06-06 Seismic Tomography](../06-seismic-tomography/README.md) — travel-time
  tomography, the sibling inverse problem with the same kernels.
- [06-07 Ambient Noise and Seismic Interferometry](../07-ambient-noise-and-interferometry/README.md) —
  coherence-based measurement, one of the scattering discriminators.
- [18-inverse-problems](../../18-inverse-problems/README.md) — the systematic
  treatment of null space, resolution and regularisation.
- [19-numerical-modeling-hpc](../../19-numerical-modeling-hpc/README.md) — the
  cost of implementing a finite absorption band in a wave-propagation code.
