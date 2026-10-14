# Module 23-07 — Field Campaign Case Studies

**Stages:** research · **Prerequisites:** modules 23-01 to 23-06; the reader is expected to have
worked through the method modules whose arithmetic these case studies assemble.

This module is the synthesis. Each of its four lessons is a **complete campaign** — a temporary
seismic array, an ERT survey, a magnetotelluric campaign, a marine cruise — followed from the
science requirement to the report, with every decision expressed as arithmetic that could have
been done before mobilisation. The lessons introduce no new physics: they use the array
resolution relation, the coherence-to-accuracy relation, the CDP fold relation, the
contact-resistance arithmetic, the duty-cycle power budget, the configuration count, the
feathering geometry and the availability model, all of them met in modules 23-01 to 23-06.

The organising idea is that **a campaign is a chain of decisions that are cheap early and
impossible late**. The aperture, the station spacing margin, the duty cycle, the electrode
spacing, the record length, the cable length, the feather tolerance and the model's layer count
are all fixed by the requirement in a single afternoon — and none of them can be recovered in
processing, from a bigger archive or with a cleverer inversion. Each lesson therefore works
out, in order, the requirement, the geometry, the workload, the volume, the schedule, the QC and
the honest limit.

The second theme is **which resource is scarce**. In the array campaign it is crew time and the
access schedule; in the ERT survey it is field time, bought with stacking; in the MT campaign it
is recording time, bought with coherence and a remote reference; in the marine cruise it is
vessel days, against which the entire dataset is a rounding error. Naming the scarce resource
early is what turns a list of good ideas into a schedule — and in all four cases the science
requirement, not the instrument, sets the number that consumes it.

The third theme is the **honest limit**. Every lesson closes with what its campaign cannot
establish: that a station failure costs resolution rather than just data; that a mesh finer than
the data support makes the smoothing the result; that a thin conductor under a conductive cover
cannot have its resistivity measured; that a resolution specification is not a depth-accuracy
specification. Those statements are the deliverable's quality control, and they are the part of
a plan most often left out.

All numbers in this module are **SYNTHETIC**, combined with the standard relations stated in each
lesson (array resolution and aliasing, the binomial availability model, data-rate and duty-cycle
arithmetic, depth of investigation against spread, the four-electrode geometric factor, the
coherence-to-accuracy relation, the half-decade-per-layer rule, two-way travel time, the CDP fold
relation, the feathering geometry). No real campaign, institution, vessel, instrument, vendor
figure or measured dataset is used or reproduced.

## Learning objectives

By the end of this module you will be able to:

1. **Convert** a science requirement — a depth, a resolution, an accuracy — into the geometry of
   a survey, and **state** which parameter buys which.
2. **Compute** the workload, the data volume, the power and the schedule of a campaign, and
   **name** the resource that is actually scarce.
3. **Choose** the margins — aperture, spacing, fold, stacking, recording time, feather tolerance
   — against the failures and the noise the campaign will actually meet.
4. **Design** the QC that runs during acquisition, so that a failure is found while it can still
   be fixed.
5. **Justify** a model's parameterisation from the data and the band rather than from ambition.
6. **Write** the resolution claim with the synthetic test that supports it, and **state** the
   claims the campaign cannot support.

## Prerequisites

- [23-01 to 23-06](../README.md) — the method modules whose arithmetic these campaigns assemble.
- [18-03-01 Why Regularisation Is Justified](../../18-inverse-problems/03-regularization/01-why-regularize.md) —
  the inversion discipline the ERT and MT case studies depend on.
- [15-02-01 Marine Seismic Reflection: Sources, Streamers and Processing](../../15-oceanography-marine/02-marine-geophysics-methods/01-marine-seismic-reflection.md) —
  the marine acquisition method.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Case Study: Deploying a Temporary Seismic Array](01-case-study-seismic-array.md) | research | A 1 km target at 10 km depth with $\lambda = 2$ km fixed a 20 km aperture and 21 stations at 1000 m; 0.90 survival delivered 18.90 stations and a 1064 m resolution cell |
| 02 | [Case Study: An ERT Survey from Design to Report](02-case-study-ert-survey.md) | research | 64 electrodes at 2 m gave a 25.2 m DOI and 2.0 m sampling; the protocol used 0.31 % of the configuration space and the deepest level rested on **three** measurements |
| 03 | [Case Study: A Magnetotelluric Campaign](03-case-study-mt-campaign.md) | research | A 10 Ω·m target at 2 km needed $T > 1.58$ s; coherence 0.99 against 0.90 was 10.5× the recording time, and a remote reference bought 5.71× |
| 04 | [Case Study: A Marine Geophysical Cruise](04-case-study-marine-cruise.md) | research | A 2 km target fixed a 2.60 s record and a 3.00 km cable; 2400 line km was 21.40 days with transit and weather, and the whole dataset was 59.9 GB against a vessel budget of thousands |

## Suggested path

**If you are planning your first campaign:** 01 for a station-based survey, 02 for a
profile-based one; both follow the same seven-step sequence and either can be used as a template.

**If your campaign is dominated by a moving platform:** 04, then 01 §5 for the power and duty
arithmetic that also applies to a towed or autonomous system.

**If your survey's accuracy is limited by noise rather than by geometry:** 03 for the coherence
and recording-time arithmetic, which is the clearest example of a physics-limited schedule.

**If you are writing a data-management or QC plan:** each lesson's QC section is the
"what could still be fixed in the field" list; 02 and 04 have the most direct analogues to a
routine acquisition QC.

**If you are reviewing a campaign plan:** check whether the plan names its scarce resource, its
margins and its model parameterisation justification — those three, or their absence, predict the
outcome more than any instrument list.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-case-study-seismic-array.md`](01-case-study-seismic-array.md) | Lesson 01 |
| [`02-case-study-ert-survey.md`](02-case-study-ert-survey.md) | Lesson 02 |
| [`03-case-study-mt-campaign.md`](03-case-study-mt-campaign.md) | Lesson 03 |
| [`04-case-study-marine-cruise.md`](04-case-study-marine-cruise.md) | Lesson 04 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Four runnable demonstrations |

| Script | What it measures |
|---|---|
| [`code/case_study_seismic_array_demo.py`](code/case_study_seismic_array_demo.py) | Aperture and aliasing from the requirement, workload in station-hours, volume and archive, power and visits, delivered availability and resolution |
| [`code/case_study_ert_survey_demo.py`](code/case_study_ert_survey_demo.py) | Depth of investigation against spread, configuration counts by level, contact and current, stacking cost, model/data ratio with a seeded reciprocal check |
| [`code/case_study_mt_campaign_demo.py`](code/case_study_mt_campaign_demo.py) | Skin-depth band, coherence-to-estimate-count table, remote-reference gains, crew schedule, depth resolution and a synthetic dead band |
| [`code/case_study_marine_cruise_demo.py`](code/case_study_marine_cruise_demo.py) | Record and cable from depth, fold and bin, cruise schedule, volume against day rate, feathering displacements and rejection fractions |

## How to run the demos

Use the project virtual environment:

```bash
cd 23-field-methods-instruments/07-field-campaign-case-studies/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python case_study_seismic_array_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python case_study_ert_survey_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python case_study_mt_campaign_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python case_study_marine_cruise_demo.py
```

Each demo prints labelled results under numbered section banners, starts from
`np.random.default_rng(20261014)` wherever randomness is used, uses no network and no file I/O,
prints a `SYNTHETIC` provenance line and exits 0. All four run in under 0.2 s.

## Mastery checkpoint

Complete this without notes, using the demonstrations only to check arithmetic:

> You must image a 1.5 km deep target — a 500 m wide body with a 3× property contrast — over a
> 5 km × 5 km area, and the funder requires a resolution statement and an uncertainty statement
> for the delivered model. **(a)** Choose the method (seismic reflection, ERT, MT or a
> combination) and justify it from the target's depth-to-size ratio and the property contrast.
> **(b)** For the method chosen, compute the geometry from the requirement: aperture or spread,
> spacing, configuration or fold, and the margins you would carry for failures and noise.
> **(c)** Compute the workload and the volume, and name the scarce resource. **(d)** Compute the
> schedule including transit, weather or access contingency, and the contingency you can absorb
> before the requirement fails. **(e)** Design the QC that runs during acquisition, and the repeat
> measurement that supports a repeatability claim. **(f)** Choose the model parameterisation from
> the data count and the band, and state what the resolution claim rests on. **(g)** Write the two
> sentences the report must contain: the resolution statement and the statement of what the
> campaign cannot establish.

## Common pitfalls across this module

1. **Choosing an instrument before stating the requirement.** Every lesson starts from a depth, a
   resolution or an accuracy, not from a specification.
2. **Confusing resolution with accuracy.** A 20 m resolution and a 125 m depth uncertainty coexist
   in the same marine dataset.
3. **Designing without margins.** Spacing at the aliasing limit, a mesh finer than the data, a
   schedule without contingency — all fail at the first disturbance.
4. **Omitting the terms that are not acquisition.** Transit, turns, access, permissions, mob/demob
   and processing.
5. **Optimising the wrong resource.** Storage in a campaign whose budget is vessel days; the
   transmitter in a survey whose limit is the contact; the stack count where the coherence is the
   problem.
6. **No QC during acquisition.** A failure found in processing is a failure whose data are gone.
7. **A resolution claim with no synthetic test behind it.** The test *is* the claim.
8. **Forgetting the honest-limit paragraph.** It is the part of the report that makes the rest
   credible.

## Related modules

- [23-01 Field Safety, Planning and Logistics](../01-field-safety-and-planning/README.md) —
  the risk assessment and records every campaign in this module assumes.
- [23-02 Seismic Instruments and Fieldwork](../02-seismic-instruments-and-fieldwork/README.md) —
  the station-level design behind Lesson 01.
- [23-03 Gravity and Magnetic Fieldwork](../03-gravity-magnetic-fieldwork/README.md) —
  the potential-field fieldwork that shares this module's QC discipline.
- [23-04 Electrical and EM Fieldwork](../04-electrical-em-fieldwork/README.md) —
  the survey arithmetic behind Lessons 02 and 03.
- [23-05 Instrumentation and Electronics](../05-instrumentation-and-electronics/README.md) —
  the power, timing and calibration budgets the campaigns depend on.
- [23-06 Laboratory Measurements on Rocks and Fluids](../06-laboratory-measurements/README.md) —
  the property values and uncertainties the campaigns' interpretations rest on.
