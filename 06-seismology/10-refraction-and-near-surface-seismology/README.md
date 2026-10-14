# Module 06-10 — Refraction and Near-Surface Seismology

**Stages:** intermediate → graduate · **Prerequisites:** modules 06-01 and 06-02;
basic signal processing.

This module takes the seismological measurement that is closest to the ground — the
travel time of the first wiggle across a line of receivers — and follows it all the
way to a number an engineer will build on. Along the way it converts first arrivals
into a layered velocity model, a depth profile, a tomographic image, a shear-velocity
profile from surface waves, a $V_{S30}$ with an uncertainty budget, and finally a
modulus and a site period.

The central honest difficulty is stated once and then measured in every lesson: **a
first-arrival travel time contains no information about anything slow.** A
low-velocity layer between two fast ones is not merely hard to invert — it produces
an exactly two-layer travel-time curve, so the interpretation is perfect and wrong at
the same time. The module quantifies that failure three ways: an exact two-layer fit
with a $+53\%$ depth error, a tomographic inversion that recovers
$729\ \mathrm{m\,s^{-1}}$ where the truth is $250\ \mathrm{m\,s^{-1}}$, and a model
with $1800\ \mathrm{m\,s^{-1}}$ over $400\ \mathrm{m\,s^{-1}}$ in which not one ray
enters the slow layer. The remedy is never a better inversion; it is a different
measurement — a surface-wave sounding or a borehole.

The second difficulty is that non-uniqueness does not disappear when the model is
improved. Refraction tomography replaces three parameters with 120 and gains the
ability to represent gradients, dips and lateral change, but the answer is still
damped, still smeared over the cell size, and still equal to the analyst's starting
guess in every cell that no ray crosses. Surface-wave inversion gives a ridge, not a
point. Two soil profiles with *identical* $V_{S30}$ and *identical* site class have
peak amplifications differing by $43\%$. Throughout, this module reports admitted
sets, coverage maps and error budgets rather than single numbers, and every lesson
states which of its results is exact, which is a convention, and which is an
assumption.

All models and data in this module are **SYNTHETIC**. The velocities, spreads,
boreholes, soil profiles and structures are chosen teaching values. No field site,
survey, station or published geotechnical number is used.

## Learning objectives

By the end of this module you will be able to:

1. Derive the head-wave travel time, the intercept time and the crossover distance
   from ray geometry, and demonstrate that a three-layer first-arrival curve with a
   low-velocity layer is fitted exactly by a two-layer model whose depth is wrong by
   more than $50\%$.
2. Derive the plus and minus terms of the delay-time method, show that the minus
   term cancels the interface shape exactly, and propagate a picking error into a
   depth error with a verified analytic covariance.
3. Formulate first-arrival tomography as a path integral, derive the Fréchet
   derivative from Fermat's principle, and interpret coverage, damping and the
   resolution matrix as the three things that decide which pixels of an inversion
   image mean anything.
4. Derive the Love-wave dispersion relation for one layer over a half-space, show
   that phase velocity is bracketed by the two body-wave velocities, and measure the
   thickness–velocity ridge that makes a $V_S$ profile an acceptable set rather than
   a profile.
5. Define $V_{S30}$ as a travel-time average, derive the exact sensitivity
   $\partial\ln V_{S30}/\partial\ln V_{S,i} = w_i$, and demonstrate two profiles with
   equal $V_{S30}$ and different site response.
6. Convert $V_p$, $V_s$ and $\rho$ into elastic moduli with the exact isotropic
   relations, and state where the exact part ends and the empirical part begins.
7. Quantify an engineering uncertainty budget end to end — survey design, depth
   error, $V_{S30}$, site period, strain — and name the term that dominates each
   one.

## Prerequisites

- [06-01 Elastic Wave Propagation](../01-elastic-wave-propagation/README.md) —
  P and S waves, Rayleigh and Love waves, head waves.
- [06-02 Ray Theory and Travel Times](../02-ray-theory-and-travel-times/README.md) —
  Snell's law, the ray parameter, and travel-time curves.
- [03-10 ObsPy and Seismic Data](../../03-scientific-computing/10-obspy-and-seismic-data/README.md) —
  reading records, filtering, and picking arrivals.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Refraction Survey Geometry and Travel-Time Interpretation](01-refraction-basics.md) | intermediate | The head wave gives $v_1$, $v_2$ and one depth; a low-velocity layer is invisible to it |
| 02 | [Delay-Time (Plus-Minus) Methods and Depth Estimation](02-plus-minus-method.md) | advanced | The minus term cancels the interface shape; the depth is 16 times more sensitive to the overburden velocity than to the refractor |
| 03 | [Refraction Tomography and First-Arrival Inversion](03-tomography-refraction.md) | graduate | A grid buys gradients and dips; it does not buy coverage, and unconstrained cells equal the starting model |
| 04 | [MASW/SASW: Surface-Wave Dispersion and Vs Profiles](04-masw-sasw.md) | advanced | Dispersion is a sounding inside a bracket; the solution is a ridge, not a profile |
| 05 | [Site Characterisation: Vs30 and Site Response](05-seismic-hazards-site.md) | advanced | $V_{S30}$ weights layers by travel time; two profiles with equal $V_{S30}$ respond differently by $43\%$ |
| 06 | [Engineering Seismology Applications](06-engineering-seismics.md) | advanced | Velocity gives a modulus exactly and a design number only through assumptions; the budget is usually geometric |

## Suggested path

**If you are new to near-surface seismology:** lessons 01–02 in order, running each
demonstration. Lesson 02 is where the depth–velocity trade-off becomes an error bar.

**If you already run refraction surveys:** read 01 §6 (the blind zone) and 02 §6–7,
then 03 and 06 — the two lessons that decide what a deliverable can claim.

**If you are preparing a research project:** 03 §5–8 (coverage, damping,
resolution), 04 §4–6 (the Jacobian and the ridge), 05 §4, plus the exercises at ★★★
level.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-refraction-basics.md`](01-refraction-basics.md) | Lesson 01 |
| [`02-plus-minus-method.md`](02-plus-minus-method.md) | Lesson 02 |
| [`03-tomography-refraction.md`](03-tomography-refraction.md) | Lesson 03 |
| [`04-masw-sasw.md`](04-masw-sasw.md) | Lesson 04 |
| [`05-seismic-hazards-site.md`](05-seismic-hazards-site.md) | Lesson 05 |
| [`06-engineering-seismics.md`](06-engineering-seismics.md) | Lesson 06 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for all six lessons |
| [`code/`](code) | Six runnable demonstrations |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib and
ObsPy:

```bash
cd 06-seismology/10-refraction-and-near-surface-seismology/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python refraction_basics_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python delay_time_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python refraction_tomography_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python masw_dispersion_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python seismic_hazards_site_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python engineering_seismics_demo.py
```

Every demo prints labelled results with units, uses a fixed random seed, requires no
network access, and exits 0. They are print-only: no figures are produced, and none
of them writes a file.

| Demo | Lesson | What it computes |
|---|---|---|
| `refraction_basics_demo.py` | 01 | critical angle, head-wave times, crossover three ways, Fermat and eikonal verification, the blind zone |
| `delay_time_demo.py` | 02 | forward and reverse times, reciprocity, the minus and plus terms, error propagation and the error ellipse |
| `refraction_tomography_demo.py` | 03 | shortest-path forward solver plus damped LSQR inversion: two layers, a blind zone, a velocity inversion, depth of investigation, coverage |
| `masw_dispersion_demo.py` | 04 | Love-wave dispersion, its exact limits, the Jacobian, the trade-off ridge and the offset limits |
| `seismic_hazards_site_demo.py` | 05 | $V_{S30}$ and its weights, two profiles with one $V_{S30}$, the SH transfer function, impedance and damping, band averages, a Monte Carlo |
| `engineering_seismics_demo.py` | 06 | survey design, depth error with a Monte Carlo, downhole velocities, moduli, site and structure periods, strain, the $V_{S30}$ budget, the quarter-wavelength limit |

## Mastery checkpoint

Complete this without notes. The values are SYNTHETIC.

> A site is $18\ \mathrm{m}$ of soil over bedrock. A refraction line with reversed
> shots gives $v_1 = 988\ \mathrm{m\,s^{-1}}$ and $v_2 = 3500\ \mathrm{m\,s^{-1}}$,
> with a $1\ \mathrm{ms}$ pick standard deviation. **(a)** Give the crossover, the
> spread you would shoot and the depth error you expect. **(b)** A surface-wave
> survey over the same line reports a $V_S$ profile whose travel-time average is
> $263\ \mathrm{m\,s^{-1}}$ above the bedrock, and $V_{S30} = 290\
> \mathrm{m\,s^{-1}}$ with a $\pm 4\ \mathrm{m\,s^{-1}}$ uncertainty. Compute the
> site class, the site period from the uniform-column rule, and state in one
> sentence why the rule is not the period. **(c)** A tomographic inversion of the
> same first arrivals shows a low-velocity layer
> $6\ \mathrm{m}$ below the surface. State what the first arrivals can and cannot
> say about it, and what measurement would settle it. **(d)** The design event
> produces a surface velocity of $0.15\ \mathrm{m\,s^{-1}}$ in the top layer. State
> the direction of the resulting error in the site period and the two quantities
> that decide its size. **(e)** Two nearby sites share this $V_{S30}$; measurements
> of their transfer functions differ in peak amplitude by $40\%$. Explain how that
> is possible and what it implies for a single-number site factor.

Worked versions of (a)–(b) are in the lesson-06 and lesson-05
solutions under [`exercises/`](exercises); (c) is worked in
[03-tomography-refraction-solutions.md](exercises/03-tomography-refraction-solutions.md)
and (e) in
[05-seismic-hazards-site-solutions.md](exercises/05-seismic-hazards-site-solutions.md).

## Common pitfalls across this module

1. **Reading a zero residual as a correct model.** A low-velocity layer produces an
   exactly two-layer curve; the fit is perfect and the depth is wrong by $53\%$
   (lesson 01).
2. **Quoting a refraction depth without its overburden velocity.** The depth is
   derived from the intercept *given* $v_1$; the sensitivity is $1.0667$ against
   $-0.0667$ for the refractor (lesson 02).
3. **Showing an inversion without its coverage.** Cells the rays never enter keep
   the starting model, and the least-changed cells are the least-covered ones
   (lesson 03).
4. **Reporting one $V_S$ profile from a dispersion curve.** The acceptable set is a
   ridge whose width is set by the noise, the band and the assumed density
   (lesson 04).
5. **Averaging velocities arithmetically.** $V_{S30}$ is a travel-time average;
   the arithmetic mean was $50\%$ higher on one demonstration profile (lesson 05).
6. **Treating a velocity as a design parameter.** $\mu = \rho V_s^{2}$ is exact;
   bearing capacity and liquefaction resistance are correlations (lesson 06).
7. **Spending the budget on better seismograms when the geometry is the error.**
   $62\%$ of one $V_{S30}$ variance budget came from a $0.10\ \mathrm{m}$ boundary
   tolerance (lesson 06).
8. **Forgetting that every number here is small-strain.** The operative modulus at
   strong shaking is smaller and the site period longer; the sign is certain, the
   size is a site-specific modelling choice.

## Related modules

- [06-01 Elastic Wave Propagation](../01-elastic-wave-propagation/README.md) — the
  waves this module measures.
- [06-02 Ray Theory and Travel Times](../02-ray-theory-and-travel-times/README.md) —
  the ray parameter and travel-time curves used throughout.
- [06-06 Seismic Tomography](../06-seismic-tomography/README.md) — the same
  inversion machinery at lithospheric scale, where coverage is again the limiting
  factor.
- [06-09 Reflection Seismology](../09-reflection-seismology/README.md) — near-surface
  refraction supplies the statics that reflection processing needs.
- [06-11 Earthquake Statistics and Hazard](../11-earthquake-statistics-and-hazard/README.md) —
  what a site factor is used for: hazard curves, design spectra and maps.
- [10-04 Near-Surface Seismic and Geotechnical](../../10-gpr-near-surface/04-near-surface-seismic-and-geotechnical/README.md) —
  the geotechnical workflow that consumes these measurements.
- [11-06 Geotechnical and Engineering](../../11-exploration-geophysics/06-geotechnical-and-engineering/README.md) —
  method selection for site investigation.
- [18-inverse-problems](../../18-inverse-problems/README.md) — the systematic
  treatment of non-uniqueness, damping and resolution.
