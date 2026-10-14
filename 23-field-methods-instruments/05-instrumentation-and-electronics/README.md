# Module 23-05 — Instrumentation and Electronics for Geophysics

**Stages:** advanced → research · **Prerequisites:** modules 23-01 and 23-02;
[02-07-01 Electric Fields, Potential and Conductors](../../02-physics/07-electromagnetism/01-electrostatics.md).

This module is about the box at the end of the cable. Every geophysical method
senses one physical quantity through a chain — transducer, amplifier, filter,
converter, clock — and every property of that chain either appears in the data as a
number or hides in it as an error. The six lessons follow the chain in the order the
signal does: the **transducer** and its two limits (§1), **gain, filtering and
conversion** (§2), **time** and the clock that stamps every sample (§3), the
**calibration** that gives the numbers a scale and a history (§4), the **design** of a
build from its requirement (§5), and the **network** that many such nodes form (§6).

The organising idea is that **the chain is limited by exactly one element and the
design job is to find it**. A 33-equivalent-bit resolution claim is meaningless while
a 20-effective-bit converter sits behind it; ordering two identical amplifier stages
the wrong way round costs 4.2 dB of noise figure; quantization noise is
$\mathrm{LSB}/\sqrt{12}$ and it dominated one lesson's whole budget by 3.8×; a
calibration's own residual scatter, not the reference standard, is usually the largest
term in a measurement's uncertainty. Every one of those is arithmetic that can be done
before the parts are bought, and every one of them is invisible in the processed
product.

The second theme is **time**, because it is the specification most often written
loosely and fought over later: 1 ppm is 86.4 ms/day, which is 259 m of apparent
distance at 3 km/s; an uncompensated crystal holds a 1 ms budget for 33.33 s; and a
requirement stated as *relative* between nodes rather than *absolute* against UTC
changes the design by orders of magnitude. The third theme is **cost in its three
currencies** — money, energy and crew time — because a low-cost build buys density and
pays in robustness, and a network's real budget is spent in node-days.

All numbers in this module are **SYNTHETIC**, combined with the standard relations
stated in each lesson (Johnson noise, the bridge sensitivity, the
$\mathrm{LSB}/\sqrt{12}$ quantization term, the noise figure and Friis relation, ENOB
from SINAD, Allan-deviation scaling, least-squares standard errors, duty-cycle
averaging, free-space and empirical path loss, the binomial availability model). No
component data sheet, manufacturer figure, price, vendor specification, regulatory
figure or measured instrument response is used or reproduced.

## Learning objectives

By the end of this module you will be able to:

1. **Compute** a sensor's dynamic range in dB and bits, a bridge output, a
   piezoelectric corner and a Johnson noise floor, and **select** a sensing principle
   for a stated band and environment.
2. **Build** an input-referred noise budget, **order** amplifier stages correctly, and
   **convert** a SINAD specification into effective bits.
3. **Compute** accumulated timing error, holdover intervals and the jitter averaging
   that does and does not help.
4. **Fit** a calibration, **compute** its parameter uncertainties, **build** an
   uncertainty budget and **compute** a re-calibration interval from a drift rate.
5. **Write** a measurement requirement and **budget** the noise, the power and the
   timing of a build against it.
6. **Compute** a network's data volume, airtime, detection probability, link range and
   availability, and **state** the consequences for its design.
7. **State** the limits that no instrument can remove: the sensor's band and noise, the
   clock's holdover, the calibration's residual scatter, and the network's coverage.

## Prerequisites

- [23-01-03 Field Notebooks, Metadata and Data Provenance](../01-field-safety-and-planning/03-field-notebooks.md) —
  the record that makes an instrument's settings and calibration auditable.
- [23-02-01 Seismometers: Broadband, Short-Period, Geophones, MEMS](../02-seismic-instruments-and-fieldwork/01-seismometers.md) —
  an inertial sensor worked through in the same style.
- [02-07-01 Electric Fields, Potential and Conductors](../../02-physics/07-electromagnetism/01-electrostatics.md) —
  the circuit concepts the transducer and conditioning lessons assume.
- [03-13-02 Testing Numerical Code Against Analytic Solutions](../../03-scientific-computing/13-testing-profiling-packaging/02-testing-scientific-code.md) —
  the verification discipline applied here to hardware.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Sensors and Transducers: Principles and Selection](01-sensors-and-transducers.md) | advanced | A 120 Ω gauge at 50 µε returns 6.6 µV; the "33 equivalent bits" entry is a resolution claim, not an accuracy one; the piezoelectric corner is $1/(2\pi RC)$ |
| 02 | [Amplification, Filtering and Analog-Digital Conversion](02-signal-conditioning.md) | graduate | Noise added early is amplified and late is not: two identical stages gave 1.85 dB or 6.03 dB depending only on order; 110 dB SINAD is 17.98 effective bits |
| 03 | [Timing, GNSS Disciplining and Clock Accuracy](03-timing-and-gnss-instruments.md) | graduate | 1 ppm is 86.4 ms/day = 259 m at 3 km/s; a 1e−9 holdover sets an 11.6-day re-visit for a 1 ms budget; averaging kills jitter and never an offset |
| 04 | [Calibration, Testing and Traceability](04-calibration-and-testing.md) | research | The fit's residual scatter was 62.2 % of the uncertainty budget against the reference standard's 28.8 %; a 0.005/day drift sets a 10-day interval |
| 05 | [Building Low-Cost Instruments for Teaching and Research](05-instrument-design-lowo.md) | research | A 30 µV signal against a 1.378 µV floor; quantization noise is $\mathrm{LSB}/\sqrt{12}$ and dominated 3.8×; an uncompensated crystal needs resynchronising every 33.33 s |
| 06 | [IoT and Autonomous Sensor Networks for Earth Monitoring](06-iot-sensor-networks.md) | research | The raw stream needs 19.2× the airtime a 1 % duty cycle allows; a 90 % detection probability costs a 64 % duty cycle; two spare nodes return 324 node-days |

## Suggested path

**If you are choosing or buying sensors:** 01 for the selection table and the two
limits (band and resolution), then 02 for what the conditioning chain does to that
choice.

**If you are designing a build:** 05 first for the requirement, the noise budget and
the power budget, then 04 for the calibration and acceptance tests the build must
pass, and 02 for the gain and filtering detail.

**If timing is your problem:** 03 in full, then 06 §7 for what a network can and
cannot afford.

**If you are running a campaign:** 06 for the data, airtime and availability
arithmetic, and 04 for the before-and-after calibration discipline.

**If you are reviewing someone else's dataset:** 04 §7 and 03 §6 list what must be
present in the record for the numbers to be defensible; start there.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-sensors-and-transducers.md`](01-sensors-and-transducers.md) | Lesson 01 |
| [`02-signal-conditioning.md`](02-signal-conditioning.md) | Lesson 02 |
| [`03-timing-and-gnss-instruments.md`](03-timing-and-gnss-instruments.md) | Lesson 03 |
| [`04-calibration-and-testing.md`](04-calibration-and-testing.md) | Lesson 04 |
| [`05-instrument-design-lowo.md`](05-instrument-design-lowo.md) | Lesson 05 |
| [`06-iot-sensor-networks.md`](06-iot-sensor-networks.md) | Lesson 06 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Six runnable demonstrations |

| Script | What it measures |
|---|---|
| [`code/sensors_and_transducers_demo.py`](code/sensors_and_transducers_demo.py) | Dynamic range and equivalent bits, quarter-bridge output, piezoelectric corner, Johnson noise, selection table |
| [`code/signal_conditioning_demo.py`](code/signal_conditioning_demo.py) | Noise figure versus source resistance, stage ordering, SINAD to effective bits, oversampling gain, filter transition ratio |
| [`code/timing_and_gnss_demo.py`](code/timing_and_gnss_demo.py) | Accumulated time error, holdover intervals, PPS jitter averaging, Allan deviation, apparent distance |
| [`code/calibration_demo.py`](code/calibration_demo.py) | Least-squares calibration and residuals, parameter standard errors, uncertainty budget, drift and re-calibration interval, traceability chain |
| [`code/instrument_design_lowo_demo.py`](code/instrument_design_lowo_demo.py) | Requirement and signal, referred noise budget, seeded peak/median detection check, power and service interval, resynchronisation interval, cost-effectiveness |
| [`code/iot_sensor_networks_demo.py`](code/iot_sensor_networks_demo.py) | Data volume and archive, airtime against a duty-cycle limit, detection probability, link budget and range, availability, node-days |

## How to run the demos

Use the project virtual environment:

```bash
cd 23-field-methods-instruments/05-instrumentation-and-electronics/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python sensors_and_transducers_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python signal_conditioning_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python timing_and_gnss_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python calibration_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python instrument_design_lowo_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python iot_sensor_networks_demo.py
```

Each demo prints labelled results under numbered section banners, starts from
`np.random.default_rng(20261014)` wherever randomness is used, uses no network and no
file I/O, prints a `SYNTHETIC` provenance line and exits 0. All six run in under 0.2 s.

## Mastery checkpoint

Complete this without notes, using the demonstrations only to check arithmetic:

> You are deploying 12 autonomous seismic nodes for four months with one visit each.
> Each node has a synthetic sensor of $S = 30$ V/(m/s), a required detection level of
> $1\times10^{-6}$ m/s in the DC–50 Hz band, a 20 Ah battery (70 % usable) and a radio
> with a 1 % duty-cycle limit. **(a)** Write the requirement as resolution, band,
> duration and environment, and compute the signal at the requirement. **(b)** Build
> the noise budget, identify the dominant term, choose a gain and compute the resulting
> SNR. **(c)** Choose a duty cycle and compute the battery life, the service interval
> and the mass of data produced. **(d)** Compute the airtime the full stream needs and
> state what you will transmit instead. **(e)** State the timing requirement and the
> resynchronisation interval, and say whether absolute timing is affordable. **(f)**
> Name the calibration and acceptance tests performed before, during and after the
> deployment, and one quantity you will *not* be able to defend afterwards.

## Common pitfalls across this module

1. **Choosing hardware before writing the requirement.** The resolution, band,
   duration and environment decide the chain; anything else is a preference.
2. **Quoting resolution as accuracy.** Equivalent bits and the LSB are not the noise
   floor, and neither is accuracy.
3. **Adding noise terms referred to different points.** The dominant term disappears
   and the design is optimised in the wrong place.
4. **Getting the stage order wrong.** Noise added early is amplified; an attenuating
   stage first is the worst case.
5. **Treating a "24-bit" converter as 24 effective bits.** SINAD, not the label, sets
   the effective bits.
6. **Confusing absolute and relative timing.** The second is usually what the science
   needs and is orders of magnitude cheaper.
7. **Extending a calibration interval because nothing has failed.** Absence of evidence
   is not evidence of stability.
8. **Planning a radio link from the free-space range.** Use an empirical path-loss model
   with a fade margin.
9. **Hiding the detection probability or the failure modes.** Both are part of the
   result and both belong in the report.

## Related modules

- [23-01 Field Safety, Planning and Logistics](../01-field-safety-and-planning/README.md) —
  the planning and record-keeping these instruments operate inside.
- [23-02 Seismic Instruments and Fieldwork](../02-seismic-instruments-and-fieldwork/README.md) —
  the seismic instruments and deployments built from these principles.
- [23-04 Electrical and EM Fieldwork](../04-electrical-em-fieldwork/README.md) —
  the electrical methods whose instruments this module builds.
- [23-06 Laboratory Measurements on Rocks and Fluids](../06-laboratory-measurements/README.md) —
  the same chain, calibration and uncertainty arithmetic applied in the laboratory.
- [23-07 Field Campaign Case Studies](../07-field-campaign-case-studies/README.md) —
  the campaigns that put these budgets together.
