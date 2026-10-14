# 23 — Field Methods, Instruments and Laboratory Work

**Stages:** beginner → research

This folder is about the part of geophysics that happens outside a notebook: putting
instruments in the ground, planning the campaign that gets them there, keeping the
record straight, and measuring rocks in the laboratory. Its organising principle is
that **every step between a physical quantity and a number is a measurement with its
own error bar**, and that the error bar is almost always computable in advance. A
safety protocol's detection delay is $\tau/2 + g$; a campaign's calendar length is
$D/w$ with a $\sqrt{D(1-w)}/w$ spread; a permission chain is $p^{M}$; a gravimeter's
drift correction leaves a residual set by the tide; a magnetometer's two-tie
correction removes half the diurnal variation; a DAS gauge length notches at $v/L$; a
logging tool's 0.6 m detector reports every thin bed at 0.6 m. None of those is a
warning — each is a number, and each is available before mobilisation.

The second theme follows from the first: **the field is the only place where some
things can be obtained**. Sensor orientation, ground coupling, the actual instrument
serial number, what departed from the plan, the lock state of a clock, the electrode
positions — these are recorded or lost, and no processing recovers them. Half of the
modules here are as much about the record as about the activity, and the folder
therefore contains a lesson on metadata and provenance at its entrance rather than at
its exit.

The third theme is honesty about what the numbers can and cannot say. Risk scores are
ordinal and rank; they do not measure. Permission probabilities model a process, not
anyone's willingness to agree. Consent is an obligation, not a transaction. A sensor
specification describes a device on a bench, not the device in your hole. An
equivalent-bits claim describes an estimation, not an accuracy. Every lesson states
what its numbers do not constrain, and where a real standard or procedure is
discussed the lesson says what is general and refers the specific requirement to the
responsible authority, the community, or the device's own documentation.

All models and data in this folder are **SYNTHETIC**. The demonstrations simulate
instrument response, survey geometry, error propagation, calibration, noise and
scheduling arithmetic from chosen parameters with a fixed seed; no real field data,
instrument specification, commercial rate, catalogue, weather series or measured
noise level is used or reproduced. Where a relation is a standard one — the
free-air gradient, the electromagnetic skin depth, the four-electrode geometric
factor, the Friar noise formula — the lesson states it and computes with it, and the
constants are quoted with their derivations.

## Modules

Modules are in dependency order. Module numbers are *not* difficulty labels.

| # | Module | Focus | Why it matters downstream |
|---|---|---|---|
| 01 | [Field Safety, Planning and Logistics](./01-field-safety-and-planning/README.md) | Risk assessment and remote-area protocols; objectives, permits and logistics; field notebooks and provenance; land access, cultural heritage and ethics | Everything else assumes the crew is safe, the permissions exist, the schedule is costed and the metadata will survive |
| 02 | [Seismic Instruments and Fieldwork](./02-seismic-instruments-and-fieldwork/README.md) | Seismometer response; digitizers, gain and anti-aliasing; network design and siting; active-source geometry; deployment and orientation; field QC; nodal and DAS systems | The instrument and network side of every seismic dataset; the response and metadata chain |
| 03 | [Gravity and Magnetic Fieldwork](./03-gravity-magnetic-fieldwork/README.md) | Loops, drift and base ties; diurnal variation and levelling; positioning and elevation; potential-field QC and error budgets | The corrections that stand between a reading and an anomaly; the positioning specification |
| 04 | [Electrical and EM Fieldwork](./04-electrical-em-fieldwork/README.md) | ERT layouts, contacts and reciprocity; loop, coil and grounded-source EM; MT sites, remote reference and coherence; GPR antennas, grids and calibration; borehole logging operations | The geometric and coupling arithmetic of the galvanic, inductive and high-frequency methods |
| 05 | [Instrumentation and Electronics for Geophysics](./05-instrumentation-and-electronics/README.md) | Sensors and transducers; amplification, filtering and conversion; timing and GNSS disciplining; calibration and traceability; low-cost instrument design; autonomous sensor networks | Why instruments behave as they do, and how to build and trust one |
| 06 | [Laboratory Measurements on Rocks and Fluids](./06-laboratory-measurements/README.md) | Sample preparation; ultrasonic velocity; density, porosity and permeability; electrical, magnetic, thermal and mechanical measurements; uncertainty budgets | The ground truth for the property contrasts the field methods interpret |
| 07 | [Field Campaign Case Studies](./07-field-campaign-case-studies/README.md) | A temporary seismic array, an ERT survey, a magnetotelluric campaign and a marine cruise, end to end | The whole sequence — design, permits, deployment, QC, reporting — carried through |

## The dependency spine

```text
23-01 Safety, planning and logistics ────┬──> 23-02 Seismic instruments and fieldwork
   (risk, schedule, permits, metadata)   │      (sensors, converters, networks,
        │                                │       deployment, QC, DAS)
        │                                │
        ├──> 23-03 Gravity and magnetic  ├──> 23-04 Electrical and EM fieldwork
        │      fieldwork                 │      (ERT, EM, MT, GPR, borehole)
        │      (drift, diurnal,          │            │
        │       positioning, budgets)    │            │
        │                                └──> 23-05 Instrumentation and electronics
        │                                       (sensors, chains, clocks,
        │                                        calibration, networks)
        │                                              │
        └──────────────────────────────────────────────┴──> 23-06 Laboratory measurements
                                                                 (sample preparation, rock
                                                                  properties, uncertainty)
                                                                    │
                                                                    v
                                                            23-07 Field campaign
                                                                  case studies
```

Four rules of thumb follow:

1. **Plan before you measure.** The schedule, the permits and the safety protocol are
   the critical path in most campaigns, and they are decided before the science.
2. **Record what cannot be recovered.** Orientation, coupling, serial numbers,
   deviations and clock states are field-only metadata.
3. **Compute the corrections' residuals, not just the corrections.** A drift
   correction with an unmeasured residual is a claim, not a correction.
4. **Know the instrument's limit at your site.** A specification is a bench number;
   the usable band is where the instrument's noise meets the site's.

## Which modules do you actually need?

| Goal | Minimum path |
|---|---|
| Take students into the field for the first time | 01 in full, then the relevant method module's lesson 01 |
| Deploy a temporary seismic array | 01, 02 (all), 05 §3–§4 |
| Run a gravity or magnetic survey | 01 §2–§3, 03 (all) |
| Run an ERT or GPR survey | 01, 04 §1 and §4, 05 §1–§2 |
| Run a magnetotelluric campaign | 01, 04 §3, 05 §3–§4 |
| Log a borehole and interpret the logs | 04 §5, 05 §1–§2, 06 §3 |
| Measure rock properties in the laboratory | 06 in full, 05 §1 and §4 |
| Prepare a research project with fieldwork | 02 §3 and §6, 03 §4, 06 §8, 07 in full |

## Suggested paths

**If you have never been in the field:** read
[23-01-01](./01-field-safety-and-planning/01-field-safety.md) and
[23-01-03](./01-field-safety-and-planning/03-field-notebooks.md) first, and run their
demonstrations. They cover the two things that go wrong most often — detection and
metadata — and both are cheap to fix before mobilisation.

**If you come from the processing or interpretation side:** start with 03 §2–§4
(drift, diurnal and levelling residuals) and 02 §4 (dynamic range and gain), because
those residuals and limits are what processing inherits; then read the case studies
in 07 to see them assembled.

**If you are an instrument builder:** 05 in full, with 02 §1–§2 and 06 §4–§6 as the
applications that set the requirements.

**If you are preparing a field programme or a proposal:** 01 §2, 02 §3, 03 §4, 04 §2
and 06 §8, plus the ★★★ exercises of the relevant modules, which ask for plans,
budgets and audits rather than for calculations.

## How to run the demonstrations

Every module has a `code/` directory whose scripts are print-only, seeded with
`np.random.default_rng(20261014)`, use no network and no file I/O, print a
`SYNTHETIC` provenance line and exit 0. Use the project virtual environment:

```bash
cd 23-field-methods-instruments/01-field-safety-and-planning/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python field_safety_demo.py
```

Each module README lists its own scripts and what each one measures.

## Mastery checkpoint for the folder

Complete this without notes, using the demonstrations only to check arithmetic:

> You are asked to run a two-week campaign to image a 30 m deep aquifer over 2 km²
> with ERT, in an area 8 km from a railway, on land divided into 40 parcels with a
> single access road, in a season with a 0.6 daily working probability. **(a)**
> Compute the calendar schedule and its 90th percentile, and the probability that the
> permission chain is complete. **(b)** Choose the electrode geometry for the target
> depth and compute the contact-resistance and reciprocity tolerances you will
> enforce. **(c)** State the two noise sources the railway brings, and quantify one of
> them. **(d)** Write the metadata list you would require at demobilisation, mark the
> items that cannot be recovered later, and state the single check that would tell you
> on day two whether the campaign is going to work.

## Related material elsewhere in the curriculum

- [05-05 Survey Design and Acquisition](../05-core-geophysics/05-survey-design-and-acquisition/README.md) —
  the design theory these modules implement.
- [05-06 Data Processing Principles](../05-core-geophysics/06-data-processing-principles/README.md) —
  what happens to the corrected data.
- [22-02 Reproducible Workflows](../22-data-engineering-reproducibility/02-reproducible-workflows/README.md) —
  provenance and versioning after the field.
- [21-09 Ethical and Responsible Analytics](../21-statistics-bayesian-ml/09-ethical-and-responsible-analytics/README.md) —
  the ethics and reporting obligations that begin in the design.
