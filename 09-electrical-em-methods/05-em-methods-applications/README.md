# Module 09-05 — Applied Electromagnetic Methods

**Stages:** graduate → doctoral · **Prerequisites:** modules 09-01 and 09-02, and
one of 08-04 or 08-05.

This module applies the diffusive electromagnetics of folder 08 to five
operational problems: transient soundings for aquifers and mineral targets,
frequency-domain conductivity mapping, marine CSEM for resistive hydrocarbon and
hydrate targets, geothermal and permafrost surveying, and environmental mapping
of plumes and salinity. The physics in all five is the same — a time-varying
magnetic field diffusing into a conductive earth — so the module is organised
around the three quantities that every one of them depends on: the **diffusion
depth** $\delta = \sqrt{2t/(\mu_0\sigma)}$, the **induction number** that decides
whether a response is linear in conductivity, and the **window** of times or
frequencies that samples a given depth.

Every lesson therefore does three things in the same order. It states the
measurement, computes the layered response from a kernel that has been validated
against closed forms, and then measures how much the data actually constrain —
because in every one of the five applications the honest answer is a range, not a
number. The module's single most repeated result is the **conductance
equivalence**: a thin conductor and a thick, less conductive one are
indistinguishable within any finite band and noise level, so a depth quoted
without an admitted range is a claim the data do not support.

That non-uniqueness is quantified rather than asserted. The transient module
measures the equivalence error at four thickness ratios; the frequency-domain
module shows that grounds differing by a factor of forty in both thickness and
conductivity give apparent conductivities inside a band spanning $71\%$; the
marine lesson shows that a factor $200$ change in reservoir resistivity moves the
response by less than $0.1\%$; and the environmental lesson shows that a factor
ten in plume thickness moves the reported concentration by only $1.5$. Each of
those is a measured number from the demonstration in `code/`, with its band,
geometry and stated noise level.

**All models and data in this module are SYNTHETIC.** No real aquifer, ore body,
prospect, reservoir, field or instrument is modelled or measured, and no
published number is quoted. Physical constants are standard values with units
stated.

## Learning objectives

By the end of this module you will be able to:

1. **Validate** a layered-earth EM forward model against closed forms and
   reduction tests before using it, and **state** the truncation and regime
   limits of the integral.
2. **Derive** the diffusion depth in time and in frequency and **explain** why it
   is not a depth of investigation.
3. **Measure** and **interpret** a median depth of investigation with a stated
   definition, and **report** the measured exponent rather than the naive
   $\delta$ scaling.
4. **Test** a response for the induction-number collapse and **state** the range
   over which a conductivity calibration is valid.
5. **Compute** the normalised magnitude of a marine response, the exact range
   limit of the water column, and the design frequency that balances the two.
6. **Compute** a conductivity from temperature (Arrhenius) or from a
   concentration (molar conductivity plus Archie), and **state** the assumption
   each carries.
7. **Report** any of the five measurements as an admitted range with its band,
   geometry, calibration and noise level.

## Prerequisites

- [09-01 Electrical Properties of Earth Materials](../01-electrical-properties-of-earth/README.md) —
  conductivity, Archie's law, temperature dependence.
- [09-02 DC Resistivity Methods](../02-dc-resistivity/README.md) — the near-surface
  resistivity context.
- [08-04 Electromagnetic Induction](../../08-geomagnetism-electromagnetism/04-electromagnetic-induction/README.md)
  and [08-05 Controlled-Source EM](../../08-geomagnetism-electromagnetism/05-controlled-source-em/README.md) —
  the induction physics and the systems.
- [09-03 Induced Polarisation](../03-induced-polarisation/README.md) — the
  polarisation response that contaminates an EM conductivity measurement.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [TEM Sounding for Aquifers and Mineral Targets](01-tem-sounding.md) | graduate | Validate the kernel; time and frequency are the same window; conductance is the datum |
| 02 | [FEM Conductivity Mapping and Apparent Conductivity](02-fem-conductivity-mapping.md) | advanced | The LIN calibration works over a measured range, and the number it yields is an average |
| 03 | [Marine CSEM for Hydrocarbon and Gas Hydrate Exploration](03-csem-marine.md) | research | Look for a resistor through a conductor; the water sets the range, the target does not |
| 04 | [EM for Geothermal Systems and Permafrost](04-em-geothermal-permafrost.md) | doctoral | Temperature and ice write on one channel; the cap hides the reservoir |
| 05 | [EM for Contaminant Plumes, Salinity and Leachate](05-em-environmental.md) | graduate | The petrophysical filter dominates; the equivalence compresses the answer |

## Suggested path

**If you are new to applied EM:** lessons 01 and 02 in order, running both
demonstrations. Lesson 01 contains the validated kernel that the others reuse.

**If you already use EM systems:** read 01 §3.5 (depth of investigation), 02 §3.3
(where LIN fails) and 02 §3.6 (the equivalence band), then the application that
matches your target.

**If you are preparing a research project:** 03 (marine, with its stated model
omission), 04 (temperature and ice), and the ★★★ exercises in each lesson.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-tem-sounding.md`](01-tem-sounding.md) | Lesson 01 |
| [`02-fem-conductivity-mapping.md`](02-fem-conductivity-mapping.md) | Lesson 02 |
| [`03-csem-marine.md`](03-csem-marine.md) | Lesson 03 |
| [`04-em-geothermal-permafrost.md`](04-em-geothermal-permafrost.md) | Lesson 04 |
| [`05-em-environmental.md`](05-em-environmental.md) | Lesson 05 |
| [`code/`](code) | Five runnable demonstrations |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |

## How to run the demos

```bash
cd 09-electrical-em-methods/05-em-methods-applications/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python tem_sounding_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python fem_conductivity_mapping_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python csem_marine_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python em_geothermal_permafrost_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python em_environmental_demo.py
```

Every demo prints labelled results with units, uses a fixed random seed
(`np.random.default_rng(20261014)`), needs no network access, exits 0, and opens
no plot window.

## Mastery checkpoint

Complete this without notes:

> A loop at $20$ m separation over ground of $0.05$ S/m. **(a)** Compute
> $\delta$ at $1$ ms and at $100$ Hz and state why they agree. **(b)** Compute the
> induction number at $10$ kHz and say whether a LIN conductivity calibration
> applies. **(c)** State the measured median depth of investigation at $100$ Hz
> and compare it with $\delta$. **(d)** A $2$ m layer of $1$ S/m and a $20$ m layer
> of $0.1$ S/m: state the measured rms response difference and what a $5\%$ noise
> level would conclude.

Worked versions appear in the lesson
[solutions](exercises/01-tem-sounding-solutions.md) and in
`solutions` for lesson 02.

## Common pitfalls across this module

1. **Treating $\delta$ as a depth of investigation.** Measured, the median depth
   scales as $\delta^{0.107}$ over three decades in lesson 01.
2. **Calibrating outside the linear regime.** The measured LIN error is $-44\%$
   at $\theta = 0.1$ and changes sign beyond $\theta \approx 1$.
3. **Reading apparent conductivity as a layer conductivity.** Grounds differing
   fortyfold in structure give answers inside a $71\%$ band.
4. **Assuming longer offsets see deeper.** The measured marine signature is
   non-monotone in offset.
5. **Converting a resistivity into temperature, saturation or concentration
   without stating the model.** Each conversion is an assumption the survey does
   not test.
6. **Omitting the geometry from the report.** Height, separation, band and
   threshold together make a number reproducible.

## Related modules

- [09-01 Electrical Properties of Earth Materials](../01-electrical-properties-of-earth/README.md)
- [09-03 Induced Polarisation](../03-induced-polarisation/README.md)
- [09-07 EM Data Processing, QC and Uncertainty](../07-em-data-processing-and-qc/README.md)
- [08-05 Controlled-Source Electromagnetics](../../08-geomagnetism-electromagnetism/05-controlled-source-em/README.md)
- [18-inverse-problems](../../18-inverse-problems/README.md) — non-uniqueness and
  regularisation, the systematic treatment of this module's equivalences.
