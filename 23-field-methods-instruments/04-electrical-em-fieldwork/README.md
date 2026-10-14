# Module 23-04 — Electrical and EM Fieldwork

**Stages:** graduate → research · **Prerequisites:** modules 23-01 and 23-03;
[09-02-05 ERT Acquisition and Design](../../09-electrical-em-methods/02-dc-resistivity/05-ert-tomography.md).

This module follows the electromagnetic methods into the field and asks the one
question that decides whether their data mean anything: **what did the geometry and
the noise do to the measurement?** Each lesson takes one family — galvanic (ERT),
inductive (FEM/TEM), natural-source (MT), high-frequency (GPR) and borehole — and
computes the quantities that a field crew must control: the geometric factor and the
contact resistance of an array, the skin depth and the induction number of a coil
pair, the coherence an MT impedance estimate needs, the trace spacing a GPR
migration requires, and the cable stretch that shifts a log's depth scale.

The organising idea is that **these methods fail through geometry and coupling
before they fail through physics**. A 100 kΩ electrode contact costs 53 dB of signal
at a voltage-limited transmitter; a coherent noise source with 0.9 coherence
quadruples an apparent resistivity; a GPR grid paced at five times the required
trace spacing aliases the diffractions that migration exists to collapse; a 500 N
logging tool stretches 2 km of cable by 0.9 m. Every one of those is arithmetic that
can be done before mobilisation, and every one of them is invisible in the processed
product.

The third theme is the cost structure of acquisition time. Stacking buys 3 dB per
doubling of time; a fall in MT coherence from 0.99 to 0.90 costs 11.6× the recording
time; a GPR grid at the theoretical trace spacing is a five-day survey for a 30 m
square. The module therefore pairs every resolution or accuracy claim with the time
it costs, so that a design decision can be made with both numbers on the table.

All numbers in this module are **SYNTHETIC**, combined with the standard relations
stated in each lesson (the four-electrode geometric factor, the skin depth, the
diffusion time, the MT coherence estimator, $\lambda/4$ resolution, the elastic
stretch). No field dataset, instrument specification, commercial protocol or
manufacturer figure is used or reproduced.

## Learning objectives

By the end of this module you will be able to:

1. **Compute** a geometric factor from electrode positions, an apparent resistivity
   and its error, and the injected current a contact resistance allows.
2. **Use** reciprocity as a field test with a stated tolerance.
3. **Compute** skin depths, induction numbers and TDEM diffusion times, and
   **decide** whether an inductive measurement is in its linear regime.
4. **Compute** the coherence an MT accuracy requires, the recording time a weaker
   band costs, and the bias a coherent noise source produces.
5. **Compute** a GPR velocity, resolution, trace spacing and attenuation budget, and
   **calibrate** the depth scale against a known target.
6. **Compute** a logging cable's stretch, a thin-bed response, a logging speed and a
   two-point calibration.
7. **Design** the layout, the checks and the time budget of an electrical or
   electromagnetic survey from its target.
8. **State** the limits that the field method cannot remove — invasion, coupling,
   coherent noise, detector length.

## Prerequisites

- [23-01-03 Field Notebooks, Metadata and Data Provenance](../01-field-safety-and-planning/03-field-notebooks.md) —
  the record that makes the geometry auditable.
- [23-03-04 Field Data QC for Potential-Field Surveys](../03-gravity-magnetic-fieldwork/04-field-data-qc-gravmag.md) —
  the QC framework these methods share.
- [09-02-05 Electrical Resistivity Tomography (ERT) Acquisition and Design](../../09-electrical-em-methods/02-dc-resistivity/05-ert-tomography.md) —
  the ERT design this module equips.
- [09-05-01 TEM Sounding for Aquifers and Mineral Targets](../../09-electrical-em-methods/05-em-methods-applications/01-tem-sounding.md) —
  the inductive sounding method.
- [08-04-02 Magnetotellurics: Impedance Tensor, Apparent Resistivity, Phase](../../08-geomagnetism-electromagnetism/04-electromagnetic-induction/02-magnetotellurics.md) —
  the MT theory behind the field practice.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [ERT Fieldwork: Electrode Layouts, Contact Resistance, Reciprocity](01-ert-fieldwork.md) | graduate | $K$ grew 56× from $n=1$ to $n=6$; a 100 kΩ contact cost 53 dB; a 48-electrode spread allows 194 580 configurations of which a protocol uses under 1 % |
| 02 | [EM Fieldwork: Loop, Coil and Grounded-Source Configurations](02-em-fieldwork.md) | graduate | $\delta = 503.3\sqrt{\rho/f}$ m; the induction number left the linear regime above 1; cultural coupling fell 12 dB per doubling of distance |
| 03 | [MT Fieldwork: Sites, Remote Reference, Noise](03-mt-fieldwork.md) | research | A 1 % impedance accuracy needs coherence 0.998 from 20 estimates; a coherence drop to 0.90 costs 11.6× the recording time; a 0.9-coherence noise source quadruples $\rho_a$ |
| 04 | [GPR Fieldwork: Antenna Choice, Grids, Coupling, Calibration](04-gpr-fieldwork.md) | graduate | A 250 MHz survey in $\varepsilon_r = 9$ resolves 0.10 m; its grid is 9.1 h for 20 m × 20 m; a 10 % permittivity error is 5 % in depth |
| 05 | [Borehole Logging Operations and Tool Calibration](05-borehole-fieldwork.md) | graduate | A 500 N tool stretches 2 km of cable by 0.91 m; a 0.15 m bed in a 0.6 m detector returns 0.25 of its contrast at the detector's apparent thickness |

## Suggested path

**If you are running a near-surface ERT or GPR survey:** 01 for the electrode
geometry, contact resistance and reciprocity, then 04 for the high-frequency
survey at the same site. Both are geometry-first lessons.

**If you are planning an EM or MT campaign:** 02 for skin depth, induction number
and coupling distances, then 03 for the coherence, dead-band and remote-reference
arithmetic that sets the recording time.

**If you are working in boreholes:** 05 for depth control and calibration, and 01
§2–§3 for the surface-to-borehole geometry in a cross-hole survey.

**If you are reviewing someone else's dataset:** each lesson's Section on metadata
and checks lists what must be present for the data to be auditable; start there.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-ert-fieldwork.md`](01-ert-fieldwork.md) | Lesson 01 |
| [`02-em-fieldwork.md`](02-em-fieldwork.md) | Lesson 02 |
| [`03-mt-fieldwork.md`](03-mt-fieldwork.md) | Lesson 03 |
| [`04-gpr-fieldwork.md`](04-gpr-fieldwork.md) | Lesson 04 |
| [`05-borehole-fieldwork.md`](05-borehole-fieldwork.md) | Lesson 05 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Five runnable demonstrations |

| Script | What it measures |
|---|---|
| [`code/ert_fieldwork_demo.py`](code/ert_fieldwork_demo.py) | Exact geometric factors against closed forms, apparent-resistivity error, contact resistance and injected current, reciprocity tolerance, configuration counts |
| [`code/em_fieldwork_demo.py`](code/em_fieldwork_demo.py) | Skin depth, induction number, TDEM diffusion time, orientation conventions, cultural coupling, stacking gain |
| [`code/mt_fieldwork_demo.py`](code/mt_fieldwork_demo.py) | Impedance levels, coherence requirements, dead-band recording time, dipole response, remote-reference bias, site footprint |
| [`code/gpr_fieldwork_demo.py`](code/gpr_fieldwork_demo.py) | Velocity and resolution, hyperbola analysis, migration trace spacing, attenuation budget, grid cost, calibration error |
| [`code/borehole_logging_demo.py`](code/borehole_logging_demo.py) | Cable stretch, thin-bed response, logging speed, two-point calibration, depth matching |

## How to run the demos

Use the project virtual environment:

```bash
cd 23-field-methods-instruments/04-electrical-em-fieldwork/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python ert_fieldwork_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python em_fieldwork_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python mt_fieldwork_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gpr_fieldwork_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python borehole_logging_demo.py
```

Each demo prints labelled results under numbered section banners, starts from
`np.random.default_rng(20261014)`, uses no network and no file I/O, prints a
`SYNTHETIC` provenance line and exits 0. All five run in under 0.2 s.

## Mastery checkpoint

Complete this without notes, using the demonstrations only to check arithmetic:

> You are asked to map a 2 m deep contaminant plume over a 100 m × 100 m site with a
> conductive groundwater body in a sandy soil. **(a)** Choose ERT or EM, and justify
> the choice with a skin-depth and a contact-resistance calculation. **(b)** For the
> method chosen, specify the geometry — electrode spacing and count, or coil
> separation and orientation — from the target depth, and compute the depth of
> investigation you expect. **(c)** Compute the acquisition time from the number of
> configurations or soundings and state the tolerance you would set for the
> reciprocity or induction-number check. **(d)** Name the two noise sources that
> will dominate at this site and state the mitigation for each.

## Common pitfalls across this module

1. **Treating a geometry error as a data-processing problem.** A wrong $K$, a
   mis-recorded coil separation or a mis-placed electrode changes the physics, not
   the processing.
2. **Quoting a small-loop conductivity outside the linear regime.** At an induction
   number above 1 it is not a conductivity.
3. **Underestimating acquisition time.** The MT dead band costs an order of
   magnitude; a GPR grid at the theoretical spacing is days.
4. **Assuming a permittivity or a velocity.** A 10 % error in $\varepsilon_r$ is 5 %
   in depth, and in GPR the depth is the deliverable.
5. **Ignoring coherent noise.** It biases MT impedances and is not removed by
   stacking.
6. **Reading a depth off a logging cable.** Elastic stretch reaches metres and
   changes with the tool and the tension.
7. **Confusing resolution with detection.** A thin bed is *detected* by its
   amplitude and *resolved* only if the detector is short enough.

## Related modules

- [23-03 Gravity and Magnetic Fieldwork](../03-gravity-magnetic-fieldwork/README.md) —
  the potential-field fieldwork this module complements.
- [23-05 Instrumentation and Electronics for Geophysics](../05-instrumentation-and-electronics/README.md) —
  the instruments behind these measurements.
- [23-06 Laboratory Measurements on Rocks and Fluids](../06-laboratory-measurements/README.md) —
  where the properties the methods sense are measured directly.
- [09 Electrical and EM Methods](../../09-electrical-em-methods/README.md) —
  the theory and the processing of these datasets.
- [10 GPR and Near-Surface](../../10-gpr-near-surface/README.md) —
  the shallow high-frequency end in full.
