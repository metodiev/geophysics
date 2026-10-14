# Module 23-02 — Seismic Instruments and Fieldwork

**Stages:** advanced → research · **Prerequisites:** modules 23-01 and 23-04;
[20-01-04 Transfer Functions, Poles and Zeros](../../20-signal-processing/01-signals-and-systems/04-transfer-functions.md).

This module follows the seismic signal from the ground into the archive. Seven lessons, in the
order a campaign meets them: the **seismometer** and its response (§1), the **digitizer**, its
gain and its anti-alias filter (§2), the **network** that the stations form and where they are
sited (§3), the **active-source** geometry of sources and spreads (§4), the **deployment** that
turns a specification into an installed station (§5), the **field QC** that keeps the dataset
alive (§6), and the **nodal and distributed-acoustic** systems that have changed what a "station"
is (§7).

The organising idea is that **every stage of the chain is a filter, and the ones that matter are
the ones nobody writes down**. The sensor is a band-pass device whose usable low-frequency limit
is where its self-noise meets the ambient noise (0.2910 Hz in §1's model, not its 4.5 Hz corner);
the digitizer's resolution is bought with gain, not bits (a 1 mV signal on a ±10 V 24-bit
converter uses 11.21 of its bits); the installation is a mechanical filter (a coupling resonance
at 20 Hz costs −11.1 dB at 10 Hz); the array is a spatial filter (eight stations on a ring give
$\sigma_h = 0.212$ km, on a road 81.2 km); the gauge length is a spatial filter (notches at
$f = kv/L$, 150 Hz for a 10 m gauge at 1500 m/s). Each of those is arithmetic that can be done
before mobilisation, and each of them is invisible in the processed product.

The second theme is **the plan number versus the delivered number**. Fold is planned and the
taper at the ends is a geometric fact; stacking buys $\sqrt{M}$ but only for uncorrelated noise,
and 5 % correlation removes 1.9 dB of the 5.4 dB available at 12 stacks; availability is quoted
as a mean when the tail is what hurts; uptime hides gaps and overlaps. Every lesson therefore
pairs a design quantity with its delivered counterpart and the test that measures the difference.

The third theme is **the irreversible item**. Sensor orientation, coupling, the clock state, the
geometry and the metadata must be recorded when the station is installed, because no later
processing recovers them: 5° of orientation error is −21.2 dB of leakage, and an unmeasured
clock offset is an unresolvable timing error.

All numbers in this module are **SYNTHETIC**, combined with the standard relations stated in each
lesson (the instrument response and self-noise, the quantization and anti-alias relations, the
magnitude-of-completeness model, the array response and azimuthal gap, the fold and stacking
arithmetic, the orientation-leakage and tilt relations, the availability and detection models,
the gauge-length and strain-rate relations). No instrument specification, manufacturer figure or
measured dataset is used or reproduced.

## Learning objectives

By the end of this module you will be able to:

1. **Compute** a seismometer's response, corner and usable low-frequency limit, and **choose** a
   sensor from a target band and an expected ground motion.
2. **Compute** a digitizer's LSB, quantization noise and SNR, and **choose** the gain that puts a
   signal inside the converter's window.
3. **Compute** an array's resolution, azimuthal gap and magnitude of completeness, and **site**
   stations from the marginal contribution to the largest gap.
4. **Compute** fold, taper, stacking gain and refraction depth sensitivity, and **state** the
   ceiling that noise correlation puts on fold.
5. **Measure** orientation, coupling, tilt and clock state, and **state** which items are
   irreversible.
6. **Build** a daily QC loop with metrics, thresholds and actions, and **state** what a mean
   uptime hides.
7. **Compute** gauge-length notches, channel-count and alias limits, and **state** what duty
   cycling spends.

## Prerequisites

- [23-01-03 Field Notebooks, Metadata and Data Provenance](../01-field-safety-and-planning/03-field-notebooks.md) —
  the record that makes a deployment auditable.
- [20-01-04 Transfer Functions, Poles and Zeros](../../20-signal-processing/01-signals-and-systems/04-transfer-functions.md) —
  the physical quantities these instruments measure.
- [23-04-01 ERT Fieldwork: Electrode Layouts, Contact Resistance, Reciprocity](../04-electrical-em-fieldwork/01-ert-fieldwork.md) —
  the geometry-first field discipline shared with this module.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Seismometers: Broadband, Short-Period, Geophones, MEMS](01-seismometers.md) | advanced | Below the corner a velocity sensor rolls off at 12 dB/octave; the usable limit is where self-noise meets ambient noise (0.2910 Hz here, not the 4.5 Hz corner) |
| 02 | [Digitizers, Dynamic Range, Gain and Anti-Alias Filtering](02-digitizers-and-gain.md) | graduate | A 1 mV signal uses 11.21 of a ±10 V 24-bit converter's bits; 54 % of a 1.5× full-scale cycle is clipped and the amplitude is reported at 67 % |
| 03 | [Seismic Network Design and Station Siting](03-seismic-network-design.md) | graduate | Eight stations give $\sigma_h = 0.212$ km on a ring and 81.2 km along a road; $M_c$ is 1.140 at $P = 0.5$ and 1.549 at $P = 0.99$ |
| 04 | [Active-Source Fieldwork: Sources, Spreads, Shooting Patterns](04-active-source-fieldwork.md) | graduate | 5 % noise correlation removes 1.9 dB of the 5.4 dB available at 12 stacks; a 5 % $V_1$ error costs 0.53 m of refraction depth where a 5 ms pick error costs 1.55 m |
| 05 | [Deployment, Orientation, Timing and Metadata](05-seismic-deployment.md) | graduate | 5° of orientation error is −21.2 dB of leakage; a 20 Hz coupling resonance costs −11.1 dB at 10 Hz; 0.2 arcsec of tilt imitates $10^{-6}$ m/s² |
| 06 | [Field QC: Noise Checks, Continuity, Station Uptime](06-seismic-field-qc.md) | graduate | A $z > 3$ threshold flagged 2 clean channels of 56 against 0.1 predicted; cutting repair time raised availability more than tripling the MTBF |
| 07 | [Nodal Systems and Distributed Acoustic Sensing in the Field](07-das-and-nodal-systems.md) | research | The gauge length puts notches at $f = kv/L$ (150 Hz for 10 m at 1500 m/s); 1 m spacing gives 1000 channels/km and a 750 Hz alias limit |

## Suggested path

**If you are buying or specifying instruments:** 01 and 02, in that order, then 07 if the
acquisition will be nodal or fibre.

**If you are designing a network:** 03 for the geometry and the siting criterion, then 05 for
what the installation does to the response and 06 for the QC that keeps it alive.

**If you are planning an active-source survey:** 04 for fold, taper and the refraction
arithmetic, then 02 for the recorder settings.

**If you are running a deployment:** 05 for the installation, orientation and metadata, then 06
for the daily QC loop.

**If you are reviewing someone else's dataset:** 05 §4–§6 and 06 §4 list the items whose absence
cannot be repaired; start there.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-seismometers.md`](01-seismometers.md) | Lesson 01 |
| [`02-digitizers-and-gain.md`](02-digitizers-and-gain.md) | Lesson 02 |
| [`03-seismic-network-design.md`](03-seismic-network-design.md) | Lesson 03 |
| [`04-active-source-fieldwork.md`](04-active-source-fieldwork.md) | Lesson 04 |
| [`05-seismic-deployment.md`](05-seismic-deployment.md) | Lesson 05 |
| [`06-seismic-field-qc.md`](06-seismic-field-qc.md) | Lesson 06 |
| [`07-das-and-nodal-systems.md`](07-das-and-nodal-systems.md) | Lesson 07 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Seven runnable demonstrations |

| Script | What it measures |
|---|---|
| [`code/seismometers_demo.py`](code/seismometers_demo.py) | Sensor response and corners, self-noise against ambient noise, dynamic range, usable band |
| [`code/digitizers_and_gain_demo.py`](code/digitizers_and_gain_demo.py) | LSB and quantization noise, bits used by a small signal, clipping and amplitude error, alias frequencies, averaging gain |
| [`code/seismic_network_design_demo.py`](code/seismic_network_design_demo.py) | Array response and resolution, azimuthal gap, magnitude of completeness against the coincidence threshold, siting by marginal contribution |
| [`code/active_source_fieldwork_demo.py`](code/active_source_fieldwork_demo.py) | Fold and taper, stacking gain against correlation, cost per decibel, refraction depth sensitivity |
| [`code/seismic_deployment_demo.py`](code/seismic_deployment_demo.py) | Orientation leakage, coupling resonance, tilt as an acceleration, clock-lock loss over a deployment |
| [`code/seismic_field_qc_demo.py`](code/seismic_field_qc_demo.py) | Uptime distributions, MTBF against repair time, detection thresholds with a measured null, gap and overlap accounting |
| [`code/das_and_nodal_demo.py`](code/das_and_nodal_demo.py) | Gauge-length notches, channel counts and alias limits, strain rate to acceleration, duty-cycle trade |

## How to run the demos

Use the project virtual environment:

```bash
cd 23-field-methods-instruments/02-seismic-instruments-and-fieldwork/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python seismometers_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python digitizers_and_gain_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python seismic_network_design_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python active_source_fieldwork_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python seismic_deployment_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python seismic_field_qc_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python das_and_nodal_demo.py
```

Each demo prints labelled results under numbered section banners, starts from
`np.random.default_rng(20261014)` wherever randomness is used, uses no network and no file I/O,
prints a `SYNTHETIC` provenance line and exits 0. All seven run in under 0.2 s.

## Mastery checkpoint

Complete this without notes, using the demonstrations only to check arithmetic:

> You are deploying a 20-station, 60-day temporary array to record local earthquakes, with a
> target detection threshold of $M_L$ 0.5 within a 30 km radius and a science requirement of
> 0.5 ms relative timing. **(a)** Choose a sensor for the expected band and compute its usable
> low-frequency limit against the expected ambient noise. **(b)** Choose the digitizer's gain and
> compute the bits a $1\times10^{-6}$ m/s ground motion uses. **(c)** Compute the array's
> resolution on a ring and on a line, and site the stations from the largest azimuthal gap.
> **(d)** Compute the noise level the station must beat and the detection distance for the target
> magnitude from the $M_c$ model. **(e)** Specify the orientation, coupling, tilt and timing
> procedures and state which of them are irreversible. **(f)** Design the daily QC loop with its
> metrics, thresholds and actions. **(g)** State the three items whose absence from the metadata
> would make the dataset unusable.

## Common pitfalls across this module

1. **Reading a corner as a limit.** The usable low-frequency limit is a noise comparison, not a
   specification.
2. **Buying bits instead of gain.** Gain sets where the signal sits in the converter's window;
   bits set the window's width.
3. **Siting to fill an area rather than to close the largest gap.** $\sigma_h$ is dominated by the
   azimuthal distribution, not by the station count.
4. **Buying fold without measuring correlation.** Correlation puts a ceiling on the stacking gain.
5. **Assuming the installation's response.** Coupling and tilt are measured or unknown.
6. **Reporting mean uptime.** The tail, the gaps and the overlaps are what the inversion sees.
7. **Treating a gauge length as a physical channel length.** It is a spatial filter with notches.
8. **Duty cycling without costing the record.** A 4 h/day schedule records one sixth of the time.

## Related modules

- [23-01 Field Safety, Planning and Logistics](../01-field-safety-and-planning/README.md) —
  the planning and record-keeping these deployments operate inside.
- [23-04 Electrical and EM Fieldwork](../04-electrical-em-fieldwork/README.md) —
  the other field methods that share this geometry-first discipline.
- [23-05 Instrumentation and Electronics](../05-instrumentation-and-electronics/README.md) —
  the sensor, conditioning and timing chain in general form.
- [23-06 Laboratory Measurements on Rocks and Fluids](../06-laboratory-measurements/README.md) —
  where the elastic and transport properties sensed in the field are measured.
- [23-07 Field Campaign Case Studies](../07-field-campaign-case-studies/README.md) —
  the campaign that assembles these instruments into a deployment plan.
