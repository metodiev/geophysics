# Module 11-04 — Geothermal Exploration Geophysics

**Stages:** doctoral → research · **Prerequisites:** module 05-09 (heat flow and
geothermal methods) and 04-06-03 (geothermal systems); MT theory from 08-04.

This module asks what geophysics can and cannot deliver for a geothermal
prospect, and it is organised around one hard fact: **permeability decides
whether a geothermal system produces, and no surface method measures it.** Every
survey in this module therefore measures a proxy. Heat flow measures the flux of
heat and is the closest thing to a direct measurement; magnetotellurics measures
the conductance of a clay-altered cap and of hot water; gravity measures a
density contrast; microseismicity measures where rock slipped in response to a
pressure change. Each proxy is computed here, its sensitivity is quantified, and
its non-uniqueness is stated rather than hidden.

The three lessons form a sequence in decreasing certainty. Heat flow is direct
and cheap, and its interpretation is a one-dimensional conduction problem with a
stated conductivity. MT reaches kilometres and costs little, but it returns a
*product* — conductance — so thickness and resistivity trade off, and a
near-surface inhomogeneity can multiply apparent resistivity by an unknown
factor while leaving the phase untouched. Microseismic monitoring responds
directly to fluid movement, which makes it uniquely valuable and uniquely easy
to over-interpret: an event cloud is a set of locations with error bars, in an
assumed velocity model, and the magnitudes that populate it are censored by a
distance-dependent detection threshold.

All models and data in this module are **SYNTHETIC**. No field, well, operator,
capacity figure or resource number appears anywhere. Every number quoted in the
lessons is printed by a demonstration that ships with the module.

## Learning objectives

By the end of this module you will be able to:

1. **Compute** a conductive geotherm with radiogenic production and the surface
   heat flow it implies, and **invert** the requirement for a target
   temperature at a stated depth.
2. **Compute** heat in place and the sustained thermal power it implies, and
   **explain** why the answer is not a resource estimate.
3. **Derive** the porous-medium Rayleigh number and **compute** the permeability
   required for convection, with its idealisations stated.
4. **Derive** the MT skin depth and **interpret** a layered apparent-resistivity
   and phase curve in terms of cap, reservoir and basement.
5. **Demonstrate** conductance equivalence and static shift, and **state** which
   band of which curve constrains what.
6. **Compute** the source parameters of a microseismic event and **explain**
   which of them is assumed rather than measured.
7. **Quantify** the detection radius as a function of magnitude and the
   resulting bias in a fitted $b$-value.
8. **Compute** the pressure-diffusion front and **relate** it to where
   seismicity can occur.
9. **Write** an uncertainty statement that a reviewer could check, naming the
   band, the quantity and the assumption.

## Prerequisites

- [05-09 Geothermal and Heat-Flow Methods](../../05-core-geophysics/09-geothermal-and-heat-flow-methods/README.md) —
  heat-flow measurement, thermal conductivity, and the survey-level geothermal
  exploration treatment.
- [04-06-03 Geothermal Systems, Heat Flow and Resource Assessment](../../04-earth-science-geology/06-petroleum-and-mineral-systems/03-geothermal-systems.md) —
  the geological system: heat source, reservoir, fluid and caprock.
- [08-04 Electromagnetic Induction](../../08-geomagnetism-electromagnetism/04-electromagnetic-induction/README.md) —
  MT theory, processing and inversion.
- [11-01 Exploration Workflow](../01-exploration-workflow/README.md) —
  screening, method selection and the cost of being wrong.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Geophysical Signatures of Geothermal Reservoirs](01-geothermal-signatures.md) | doctoral | Heat flow is direct; everything else is a proxy; convection is a permeability threshold, and anomaly amplitude cannot separate source strength from depth |
| 02 | [Magnetotellurics for Geothermal Resource Assessment](02-mt-for-geothermal.md) | research | Skin depth sets the reach; the data constrain conductance, and the band decides what else is recoverable; static shift breaks the amplitude curve, not the phase |
| 03 | [Microseismic Monitoring of Geothermal Fields](03-microseismic-geothermal.md) | doctoral | Moment, stress drop and area trade off; detection is magnitude- and distance-dependent, so $M_c$ is a map; location accuracy is geometry, and its bias is velocity |

## Suggested path

**For a first pass:** lesson 01 §2–4 (geotherm, heat in place, convection),
then 02 §4–5 (reading an MT curve and the equivalence), then 03 §3–4 (detection
and catalogue bias). Run the demos as you go; each prints the numbers the text
quotes.

**If you work with MT data:** 02 in full, especially §5–7 — the conductance
equivalence table and the static-shift arithmetic are the two things most often
left out of a report.

**If you are preparing a monitoring programme:** 03 §3–6 plus the ★★★
exercises, which are network-design specifications.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-geothermal-signatures.md`](01-geothermal-signatures.md) | Lesson 01 |
| [`02-mt-for-geothermal.md`](02-mt-for-geothermal.md) | Lesson 02 |
| [`03-microseismic-geothermal.md`](03-microseismic-geothermal.md) | Lesson 03 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Three runnable demonstrations |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib,
Pandas, ObsPy and SymPy:

```bash
cd 11-exploration-geophysics/04-geothermal-exploration-geophysics/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python geothermal_signatures_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python mt_for_geothermal_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python microseismic_geothermal_demo.py
```

Every demo prints labelled results with units, uses a fixed random seed
(`np.random.default_rng(20261014)`), requires no network access, and exits 0.
None of them opens a window or produces a figure: results are printed.

## Mastery checkpoint

Complete this without notes:

> An area has $T_0 = 12$ °C, a mean conductivity of
> $2.4\ \mathrm{W\,m^{-1}\,K^{-1}}$ and a measured heat flow of
> $110\ \mathrm{mW\,m^{-2}}$. **(a)** Compute the temperature at 2.5 km in the
> conductive, production-free limit and compare it with the 150 °C threshold.
> **(b)** Compute the heat in place for a 2 km × 2 km × 400 m reservoir at that
> temperature with a 50 °C reference and $\phi = 0.06$.
> **(c)** An MT profile shows a 40 S conductor at 800 m depth: state the
> conductance, the two models it admits, and the measurement that would
> distinguish them.
> **(d)** A monitoring array records a $M_w = 1.2$ event with a corner frequency
> of 9 Hz: compute the rupture radius, state the assumed quantity, and state the
> detection consequence of the corner frequency.

Worked versions of (a)–(b) appear in the lesson-01
[solutions](exercises/01-geothermal-signatures-solutions.md), (c) in lesson-02
[solutions](exercises/02-mt-for-geothermal-solutions.md), and (d) in lesson-03
[solutions](exercises/03-microseismic-geothermal-solutions.md).

## Common pitfalls across this module

1. **Quoting a heat in place as a resource.** The recovery fraction is
   engineering, not physics.
2. **Reading a resistivity anomaly as temperature.** Hot water and clay
   alteration give the same signature, and MT measures a product.
3. **Reporting a conductance as a thickness.** They are one measurement and two
   unknowns.
4. **Ignoring static shift.** A factor of two in apparent resistivity is a
   factor of two in every interpreted conductance.
5. **Fitting $b$-values to raw catalogues.** Detectability is
   magnitude- and distance-dependent; the lesson measures a factor-of-three
   error from ignoring it.
6. **Reading an event cloud as a flow path.** It locates slip, in an assumed
   velocity model, with error bars that must be quoted.

## Related modules

- [05-09 Geothermal and Heat-Flow Methods](../../05-core-geophysics/09-geothermal-and-heat-flow-methods/README.md) —
  the measurement side of everything in lesson 01.
- [04-06-03 Geothermal Systems, Heat Flow and Resource Assessment](../../04-earth-science-geology/06-petroleum-and-mineral-systems/03-geothermal-systems.md) —
  the geological system.
- [08-04 Electromagnetic Induction](../../08-geomagnetism-electromagnetism/04-electromagnetic-induction/README.md) —
  MT theory and inversion, which lesson 02 applies.
- [09-05 EM Methods Applications](../../09-electrical-em-methods/05-em-methods-applications/README.md) —
  TEM and CSEM, including the controlled-source sounding that removes static
  shift.
- [06-12 Induced and Triggered Seismicity](../../06-seismology/12-induced-and-triggered-seismicity/README.md) —
  mechanisms and mitigation for the seismicity lesson 03 monitors.
- [11-03 Hydrocarbon Exploration Geophysics](../03-hydrocarbon-exploration/README.md) —
  the same methods where the target is a trap and a fluid rather than heat.
- [11-07 Exploration Case Studies](../07-exploration-case-studies/README.md) —
  the geothermal development case study.
