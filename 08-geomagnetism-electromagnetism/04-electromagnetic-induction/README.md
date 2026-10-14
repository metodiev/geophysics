# Module 08-04 — Electromagnetic Induction in the Earth

**Stages:** graduate → research · **Prerequisites:** modules 08-01 and 02-07;
basic complex analysis and least squares.

This module is about a single equation and its consequences. In the Earth at the
periods used by electromagnetic methods, the magnetic field obeys a **diffusion
equation**, so a time-varying field penetrates to a depth set by the period and
the conductivity. Measure the field's amplitude and phase at a range of periods
and you have measured how conductivity varies with depth — with the source
unknown and irrelevant, which is the central practical advantage of
magnetotellurics. Everything else in the module is the working out of that idea:
the impedance tensor, the tipper, the inversion, and the interpretation of what a
conductor is made of.

Two threads run through the module and both are quantitative. The first is
**equivalence**: because the response is controlled by a square root of resistivity
and a square root of period, and because a thin conductor's response depends on
its conductance $h/\rho$ rather than on $h$ and $\rho$ separately, several
different Earths fit the same data. The demonstrations measure the equivalences
and their limits: three models with a conductance of 100 S fit equally, and a
factor-of-two static shift in the impedance is absorbed into a wrong model whose
misfit is *better* than the truth's. The second is **noise**: an impedance is a
ratio of two noisy measurements, magnetic noise biases it by a measurable factor
(a factor of four in apparent resistivity at equal noise power), and the remedies
— a remote reference and a robust estimator — fix different failures and neither
fixes both.

All models and data in this module are **SYNTHETIC**: no station, survey,
observatory or published sounding is used, and every number quoted in a lesson is
printed by a demonstration in `code/`.

## Learning objectives

By the end of this module you will be able to:

1. **Derive** the quasi-static diffusion equation and the skin depth, and
   **verify** the plane-wave solution against an independent time-domain solution.
2. **Compute** skin depths and diffusion times across the periods used by MT and
   long-period induction, and **relate** them to the depths probed.
3. **Derive** the 1-D impedance recursion, **verify** it on a half-space, and
   **compute** apparent resistivity and phase curves for layered models.
4. **Rotate** the impedance tensor, **identify** its invariants, **recover** the
   strike, and **diagnose** dimensionality from the skew and the TE/TM split.
5. **Derive** the bias from noise in the magnetic channel, **verify** the
   $1/(1+\eta_H)^{2}$ law, and **apply** a remote reference and a robust estimator
   to the failures each is designed for.
6. **Implement** a 1-D Occam inversion, **read** its misfit–roughness trade-off,
   and **state** what the data determine (a conductance) and what they do not
   (a thickness).
7. **Compute** melt-fraction and porosity bounds from a measured conductivity and
   **state** which independent observations are needed to choose a mechanism.
8. **Apply** the $k\delta$ criterion to decide when a long-period response may be
   interpreted with a plane-wave source at all.

## Prerequisites

- [08-01 The Earth's Magnetic Field](../01-earth-magnetic-field/README.md) —
  the main field and the long-period variations used as the source.
- [02-07 Electromagnetism](../../02-physics/07-electromagnetism/README.md) —
  Maxwell's equations, induction, and fields in conductors.
- [01-10-02 The Fourier Transform](../../01-mathematics/10-fourier-analysis/02-fourier-transform.md) —
  the transform conventions used to turn time series into transfer functions.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Induction, Skin Depth, Diffusion and Conductivity Structure](01-em-induction-basics.md) | graduate | $\delta = \sqrt{2\rho/(\omega\mu_0)}$; amplitude $e^{-z/\delta}$, phase lag $z/\delta$; verified by a diffusion solver |
| 02 | [Magnetotellurics: Impedance Tensor, Apparent Resistivity, Phase](02-magnetotellurics.md) | doctoral | The recursion, the tensor and its invariants, the tipper, and the static shift that multiplies $\rho_a$ and leaves the phase alone |
| 03 | [MT Processing: Robust Estimation, Remote Reference, Tipper](03-mt-processing.md) | research | $\hat Z = Z/(1+\eta_H)$; spikes need robustness, a local source needs a remote reference |
| 04 | [MT Inversion: 1-D, 2-D and 3-D Approaches](04-mt-inversion.md) | research | The trade-off, the smearing of a thin layer, and a static shift absorbed into structure |
| 05 | [MT Interpretation: Conductors, Fluids, Melts and Frontiers](05-mt-interpretation.md) | research | Archie and Hashin–Shtrikman; connectivity beats fraction; conductance is what the data give |
| 06 | [Geomagnetic Depth Sounding and Long-Period Induction](06-geomagnetic-depth-sounding.md) | doctoral | The C-response and the mantle; and $k\delta$, which decides whether any of it is interpretable |

## Suggested path

**If you are new to EM methods:** lessons 01 and 02 in order, running both
demonstrations. Lesson 01 is where the diffusion character becomes concrete.

**If you already know MT:** start at 03 (processing, where most published errors
are made), then 04 and 06.

**If you are preparing a research project:** 03 §2–6 (noise and its remedies), 04
§3–5 (resolution and equivalence), 06 §6 (the source problem), plus the ★★★
exercises of every lesson.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-em-induction-basics.md`](01-em-induction-basics.md) | Lesson 01 |
| [`02-magnetotellurics.md`](02-magnetotellurics.md) | Lesson 02 |
| [`03-mt-processing.md`](03-mt-processing.md) | Lesson 03 |
| [`04-mt-inversion.md`](04-mt-inversion.md) | Lesson 04 |
| [`05-mt-interpretation.md`](05-mt-interpretation.md) | Lesson 05 |
| [`06-geomagnetic-depth-sounding.md`](06-geomagnetic-depth-sounding.md) | Lesson 06 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Six runnable demonstrations |

All models and data in this module are **SYNTHETIC**.

## How to run the demos

```bash
cd 08-geomagnetism-electromagnetism/04-electromagnetic-induction/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python em_induction_basics_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python magnetotellurics_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python mt_processing_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python mt_inversion_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python mt_interpretation_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python geomagnetic_depth_sounding_demo.py
```

Every demo prints labelled results with units, uses a fixed random seed
(`np.random.default_rng(20261014)`), is print-only and exits 0. No network access
is required.

## Mastery checkpoint

Complete this without notes:

> A **synthetic** MT station in a resistive terrain records
> $\rho_a = 900\ \Omega$m and $\phi = 32^\circ$ at $T = 100$ s. **(a)** State what
> the phase says about the conductivity gradient and why it is below $45^\circ$.
> **(b)** Compute the skin depth for $\rho_a$ at that period and state the depth
> range being sensed. **(c)** A neighbouring station records
> $\rho_a = 225\ \Omega$m with the same phase; state the most likely cause and
> compute the implied multiplier. **(d)** The conductor of interest is at 3 km;
> choose the period band you would acquire and justify it from the diffusion
> time. **(e)** State two quantities a report of this sounding must include, and
> one claim it must not make.

Worked versions of (a)–(c) appear in the lesson-02 and lesson-04 solutions.

## Common pitfalls across this module

1. **Reading $\rho_a$ as a layer resistivity.** It is a weighted average over the
   depth range sensed at that period.
2. **Ignoring the static shift.** It multiplies $\rho_a$ by an unknown constant,
   leaves the phase untouched, and is absorbed into the model by any inversion
   that fits amplitude alone.
3. **Averaging away magnetic noise.** It biases the impedance by $1/(1+\eta_H)$ —
   a factor of four in $\rho_a$ at equal noise power in the demonstration.
4. **Confusing a robust estimator with a remote reference.** Spikes need the
   first; a local artificial source needs the second.
5. **Quoting a thickness from a thin-sheet-regime sounding.** The data give a
   conductance; converting it needs a stated assumption.
6. **Using a plane-wave response at long periods without checking $k\delta$.**
   A 2000 km source at a 1-day period gives $k\delta = 1.47$.

## Related modules

- [08-03 Magnetic Anomalies and Modelling](../03-magnetic-anomalies-and-modelling/README.md) —
  the static half of the folder.
- [02-07 Electromagnetism](../../02-physics/07-electromagnetism/README.md) — the
  physics prerequisites, including induction and fields in conductors.
- [05-04 Rock Physics](../../05-core-geophysics/04-rock-physics/README.md) —
  Archie's law, effective-medium theory and the electrical properties of rocks.
- [18-03 Regularization](../../18-inverse-problems/03-regularization/README.md) —
  the inversion theory that lesson 04 instantiates.
- [09 Electrical and Electromagnetic Methods](../../09-electrical-em-methods/README.md) —
  the controlled-source methods that use the same diffusion physics with a
  known source.
