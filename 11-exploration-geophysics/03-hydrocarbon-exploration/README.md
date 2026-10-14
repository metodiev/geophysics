# Module 11-03 — Hydrocarbon Exploration Geophysics

**Stages:** graduate → doctoral · **Prerequisites:** modules 06-09 (reflection
seismology) and 04-06 (petroleum systems), plus a working command of the
rock-physics relations of 05-04.

This module is about what the geophysical methods **add to a geological play**.
The play itself — source, reservoir, seal, trap, migration — belongs to
[04-06-01](../../04-earth-science-geology/06-petroleum-and-mineral-systems/01-petroleum-system.md),
and the reflection theory belongs to
[06-09](../../06-seismology/09-reflection-seismology/README.md). Neither is
re-derived here. What is done here is the step in between: given a play concept,
what can a seismic, gravity or electromagnetic survey actually measure, how
precisely, at what cost in assumptions, and where does the information stop?

The module is organised around one discipline. Every method measures a bulk
property of a volume — impedance, density contrast, resistivity — and every
interpretation is a model with a stated closure. The two central quantities are
therefore not the reflection coefficient and the impedance but the
**resolution** (what size of feature survives the measurement) and the
**non-uniqueness** (how many different Earths produce the same data). Both are
computed, not asserted: the demonstrations count midpoints on a synthetic
acquisition grid, decompose impedance into the part inside and outside the
seismic band, scan rock-physics models for equal-impedance pairs, and count
synthetic prospects to measure how a posterior collapses when the base rate is
low.

All models and data in this module are **SYNTHETIC**. No field, well, basin,
company or production figure appears anywhere. The demonstrations print every
number quoted in the lessons, so a reader can re-run them and check the text
against the output.

## Learning objectives

By the end of this module you will be able to:

1. **Design** a 3-D reflection survey from a stated target: bin size from the
   alias relation, fold from trace density, resolution from wavelength and the
   Fresnel zone.
2. **Measure** the tuning coefficient of a wavelet and **state** why
   $\lambda/4$ is a rule of thumb rather than a constant.
3. **Explain** the accommodation balance and **classify** systems tracts from
   rates rather than from sea-level positions.
4. **Build** a rock-physics model, compute a fluid substitution, and
   **quantify** which attribute carries which information.
5. **Compute** a Bayesian facies posterior and **demonstrate** the base-rate
   effect on precision.
6. **Write** a seismic inversion, **choose** its regularisation against a
   stated noise level, and **quantify** the dominance of the low-frequency model
   over the noise.
7. **Quantify** shear-wave splitting, brittleness and microseismic source
   scaling, and **state** what none of them measures.
8. **Tie** a well to seismic, compute a time-depth conversion, and **report**
   the depth uncertainty that the velocity function, not the wavelet, imposes.

## Prerequisites

- [06-09 Reflection Seismology](../../06-seismology/09-reflection-seismology/README.md) —
  acoustic impedance, the convolution model, processing, velocity analysis,
  migration, AVO, multiples, attributes. This module assumes all of it.
- [04-06 Petroleum, Mineral and Geothermal Systems](../../04-earth-science-geology/06-petroleum-and-mineral-systems/README.md) —
  the play elements that the geophysics is used to constrain.
- [05-04 Rock Physics](../../05-core-geophysics/04-rock-physics/README.md) —
  Gassmann, effective media, anisotropy, electrical properties.
- [05-05 Survey Design and Acquisition](../../05-core-geophysics/05-survey-design-and-acquisition/README.md) —
  the general design principles.
- [11-01 Exploration Workflow](../01-exploration-workflow/README.md) —
  where a survey sits in the exploration sequence, and what it costs.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Reflection Seismic in Exploration: From 2-D to 3-D](01-seismic-in-exploration.md) | graduate | Resolution, Fresnel zone, fold and alias decide visibility; 2-D cannot place out-of-plane energy |
| 02 | [Seismic Stratigraphy and Sequence Interpretation](02-seismic-stratigraphy.md) | doctoral | Thin beds: amplitude is not thickness, and $\lambda/4$ is a rule of thumb; sequence boundaries are rate conditions |
| 03 | [Reservoir Characterisation and Property Prediction](03-reservoir-characterisation.md) | research | Impedance answers porosity; $v_p/v_s$ adds a little about fluid; the prior decides the prospect |
| 04 | [Seismic Inversion for Reservoir Properties](04-seismic-inversion-reservoir.md) | research | 78% of the impedance variance is outside the wavelet's band; the low-frequency model is the answer |
| 05 | [Geophysics for Unconventional Reservoirs](05-unconventional-geophysics.md) | doctoral | Brittleness, splitting and microseismicity are proxies; the stress state decides whether rock slips |
| 06 | [Integrating Borehole Data with Seismic](06-borehole-and-integration.md) | graduate | A tie needs a velocity function, not a shift; Backus averaging is the correct upscaling |

## Suggested path

**If you are new to exploration geophysics:** lessons 01 and 06 first — they
define what a seismic volume is and how it is anchored to rock — then 03, then
02 and 04. Run every demonstration; the numbers in the text are its output.

**If you already work with seismic data:** 02 §2 (tuning), 03 §4–5
(the equal-impedance curve and the posterior) and 04 §3–5 (the low-frequency
problem) are the parts most often skipped in practice.

**If you are preparing research:** 04 and 05 in full, then the ★★★ exercises,
which are written as specifications rather than as calculations.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-seismic-in-exploration.md`](01-seismic-in-exploration.md) | Lesson 01 |
| [`02-seismic-stratigraphy.md`](02-seismic-stratigraphy.md) | Lesson 02 |
| [`03-reservoir-characterisation.md`](03-reservoir-characterisation.md) | Lesson 03 |
| [`04-seismic-inversion-reservoir.md`](04-seismic-inversion-reservoir.md) | Lesson 04 |
| [`05-unconventional-geophysics.md`](05-unconventional-geophysics.md) | Lesson 05 |
| [`06-borehole-and-integration.md`](06-borehole-and-integration.md) | Lesson 06 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Six runnable demonstrations |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib,
Pandas, ObsPy and SymPy:

```bash
cd 11-exploration-geophysics/03-hydrocarbon-exploration/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python seismic_in_exploration_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python seismic_stratigraphy_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python reservoir_characterisation_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python seismic_inversion_reservoir_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python unconventional_geophysics_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python borehole_and_integration_demo.py
```

Every demo prints labelled results with units, uses a fixed random seed
(`np.random.default_rng(20261014)`), requires no network access, and exits 0.
None of them opens a window or produces a figure: results are printed.

## Mastery checkpoint

Complete this without notes:

> A 3-D survey is specified with 25 m groups on nine receiver lines spaced 300 m
> apart, shots every 50 m on 300 m source lines, maximum offsets $\pm3$ km
> inline and $\pm1.2$ km crossline, bin $25\times25$ m, in a section with
> $v = 3.0\ \mathrm{km\,s^{-1}}$ and a 30 Hz wavelet.
> **(a)** Compute the fold and the expected random-noise gain.
> **(b)** Compute $\lambda/4$ and the Fresnel radius at a 2.5 km target.
> **(c)** A 12 ms thick bed is imaged: state what the amplitude and the read-off
> time each measure, and what you would need to invert it for thickness.
> **(d)** The resulting impedance volume shows a low-impedance anomaly. List, in
> order, the checks you would run before calling it a hydrocarbon, naming the
> quantity each check constrains.

A worked version of (a)–(b) appears in the lesson-01
[solutions](exercises/01-seismic-in-exploration-solutions.md), and (c)–(d) draw
on lessons 02–04.

## Common pitfalls across this module

1. **Reporting a depth, a thickness or a saturation without the assumption it
   rests on.** Every quantitative answer here is conditional.
2. **Tuning the processing to taste.** Water levels, regularisation weights and
   gain functions must be chosen against a stated noise metric.
3. **Confusing detection with resolution.** A thin bed is detected long before
   its thickness can be read.
4. **Quoting a noise-driven error bar for a model-driven error.** In inversion
   the background dominates by an order of magnitude.
5. **Treating a proxy as a measurement.** Brittleness, splitting, event clouds
   and net-to-gross estimates are all proxies with non-unique inverses.
6. **Forgetting the scale.** A seismic property is a bulk average over a
   resolution cell containing of order $10^{15}$ grains.

## Related modules

- [06-09 Reflection Seismology](../../06-seismology/09-reflection-seismology/README.md) —
  the theory this module applies.
- [04-06 Petroleum, Mineral and Geothermal Systems](../../04-earth-science-geology/06-petroleum-and-mineral-systems/README.md) —
  the geological systems.
- [05-07 Interpretation and Integration](../../05-core-geophysics/07-interpretation-and-integration/README.md) —
  multi-method integration, ground truthing and honest reporting.
- [11-01 Exploration Workflow](../01-exploration-workflow/README.md) —
  method selection, risk and value of information.
- [11-04 Geothermal Exploration Geophysics](../04-geothermal-exploration-geophysics/README.md) —
  the same physics for a different resource, including the MT and microseismic
  methods used when the target is heat rather than hydrocarbons.
- [11-07 Exploration Case Studies](../07-exploration-case-studies/README.md) —
  basin analysis and play assessment worked end to end.
