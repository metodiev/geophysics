---
id: 23-05-05
title: "Building Low-Cost Instruments for Teaching and Research"
level: research
prereqs: ["23-05-01", "23-05-02", "23-05-04"]
estimated_minutes: 110
tags: [instrumentation, low-cost, noise-budget, power-budget, design]
---

# Building Low-Cost Instruments for Teaching and Research

## Learning objectives

By the end of this lesson you will be able to:

1. **Write** a measurement requirement as a resolution, a band, a duration and an
   environment, and **state** which of the four binds the design.
2. **Build** a noise budget referred to the sensor output and **identify** the
   dominant term.
3. **Compute** quantization noise as $\mathrm{LSB}/\sqrt{12}$ and **explain** why
   analog gain is often cheaper than more bits.
4. **Verify** a budget against a simulated record, and **state** why that verification
   is mandatory before building.
5. **Compute** an average current, a battery life and the resulting service interval.
6. **Compute** the resynchronisation interval implied by an oscillator's fractional
   error.
7. **Rank** design routes by noise floor per unit of relative cost, and **state** what
   a low-cost build can and cannot deliver.

All component values, currents, oscillator errors and relative costs in this lesson
are **SYNTHETIC** teaching values combined with the standard relations quoted in the
text. No component data sheet, manufacturer figure, price or measured instrument
response is used or reproduced.

## Prerequisites

- [01 Sensors and Transducers: Principles and Selection](01-sensors-and-transducers.md) —
  the sensing principles being built into an instrument.
- [02 Amplification, Filtering and Analog-Digital Conversion](02-signal-conditioning.md) —
  gain, anti-alias filtering and ENOB.
- [04 Calibration, Testing and Traceability](04-calibration-and-testing.md) — the
  calibration and acceptance tests a build must pass.

## 1. Intuition: low cost is a design constraint, not a goal

A commercial instrument packages four things: a **sensing chain** with a documented
response, a **calibration** with a traceable history, **robustness** (sealing,
connectors, shock, temperature, power), and **support** (software, spares, repair,
documentation). A low-cost build can match the first two and almost never the last two.
That is the honest framing: it buys **density** — many stations rather than one
excellent one — and pays for it in robustness and in analyst time, usually the largest
cost of a campaign regardless of the hardware.

The engineering order of work is therefore fixed: write the requirement; budget the
noise from the sensor forward and verify it by simulation before ordering parts;
budget the power (which sets the service interval and hence the crew cost); budget the
timing (the part most often forgotten); and design for calibration and test access,
because an instrument that cannot be checked is not an instrument.

## 2. The requirement, written so that it can be tested

| Part | Example value | What it binds |
|---|---|---|
| Resolution | velocity $1\times10^{-6}$ m/s | the noise budget |
| Band | DC–50 Hz | the noise bandwidth and the sample rate |
| Duration | 6 months unattended | the power budget |
| Environment | −10 to +40 °C, exposed | the enclosure and the drift |

Anything missing from that list will be decided accidentally by whoever buys the parts.
With a synthetic sensor of $30$ V/(m/s), the signal at the requirement is

$$v_{\text{sig}} = S \times v = 30 \times 1\times10^{-6} = 30\ \mathrm{\mu V} ,$$

and every later decision is judged against that number.

## 3. The noise budget, referred to the sensor output

Refer every noise source to one point — the sensor output — so that signal and noise
are comparable. For a moving-coil sensor with a $375\ \Omega$ coil in a $50$ Hz band:

$$v_{\text{Johnson}} = \sqrt{4k_BTRB}
= \sqrt{4(1.380649\times10^{-23})(300)(375)(50)} = 17.63\ \mathrm{nV} .$$

| Term | Expression | Value |
|---|---|---|
| sensor Johnson noise | $\sqrt{4k_BTRB}$ | 17.63 nV |
| amplifier voltage noise | $e_n\sqrt{B} = 10\ \mathrm{nV/\sqrt{Hz}}\times\sqrt{50}$ | 70.71 nV |
| amplifier current noise into 375 Ω | $i_n R\sqrt{B}$ | 2.65 nV |
| quantization, 24-bit at ENOB 20 | $\mathrm{LSB}/\sqrt{12}$ | 1.377 µV |
| quantization, 32-bit sigma-delta at ENOB 22 | $\mathrm{LSB}/\sqrt{12}$ | 0.344 µV |

with $\mathrm{LSB} = 5/2^{20} = 4.768\ \mathrm{\mu V}$ for the 20-effective-bit
converter at 5 V full scale, and the quadrature totals

$$\sigma_{\text{24-bit}} = 1.378\ \mathrm{\mu V} \;\Rightarrow\; \mathrm{SNR} = 21.8
\;(26.8\ \mathrm{dB}),$$

$$\sigma_{\text{32-bit}} = 0.352\ \mathrm{\mu V} \;\Rightarrow\; \mathrm{SNR} = 85.3
\;(38.6\ \mathrm{dB}).$$

Two conclusions, both counter-intuitive. First, **quantization dominates**: the analog
chain contributes 72.9 nV of the 1378 nV total, 0.28 % of the variance, so improving
the pre-amplifier is pointless until the converter is improved or the signal is
amplified before it. Second, **quantization noise is $\mathrm{LSB}/\sqrt{12}$, not the
LSB**: a uniform rounding error of width LSB has rms $0.289\,\mathrm{LSB}$, and
quoting the LSB — let alone the display resolution — as the noise floor overstates it.

## 4. Analog gain versus more bits

The exchange rate follows from the table. A gain of 100 before the converter divides
the referred quantization noise by 100, so the 24-bit chain becomes
$1378/100 = 13.8$ nV — *quieter than the amplifier's own 70.7 nV*. The crossover,
$G^{*} = \sigma_q/(e_n\sqrt{B}) = 1377/70.7 \approx 19$, is the gain at which the
converter and the amplifier contribute equally; a gain of about 20 is therefore enough,
and more is wasted headroom.

Three rules follow. **Compute the crossover** rather than buying bits. **Keep the gain
fixed and known**, because a programmable gain changed in the field is an unknown
scale factor while a fixed measured gain is a calibration. And **watch the dynamic
range, not just the resolution**: a gain that puts the largest expected signal at full
scale leaves no headroom for the unexpected event that is usually the reason the
instrument was deployed. Where 1/f noise or a DC offset is the limit, a chopper or
dither beats more bits, because quantization is not the binding term.

## 5. Verify the budget before building

An analytic budget is a hypothesis. The demonstration tests it by synthesising 2048
samples at 100 Hz of the required signal plus white noise at
$\sigma = 1.378\ \mathrm{\mu V}$ per sample, and comparing the spectral peak with the
median spectral amplitude:

| Quantity | Value |
|---|---|
| spectral peak at the tone | 29.937 µV |
| median spectral amplitude | 0.050 µV |
| measured peak / median | 598.18 (55.5 dB) |
| expected peak / median | 591.50 (55.4 dB) |

The expected value uses the Rayleigh median factor $\sqrt{2\ln 2} = 1.17741$, because
a Fourier bin amplitude of Gaussian noise is Rayleigh distributed, so the median is
1.17741 times the rms bin amplitude. The 1.1 % agreement is the evidence that the
budget's arithmetic and the processing model are consistent — and **simulating the
processing chain, not just the noise, is what makes the test meaningful**, because
peak-over-median is what a detection threshold actually uses.

## 6. Power budget and service interval

Power determines not the instrument but the *campaign*: the service interval, the crew
cost and whether the deployment is feasible at all. With synthetic currents,
$I_{\text{sleep}} = 20\ \mathrm{\mu A}$, $I_{\text{acq}} = 12$ mA and
$I_{\text{tx}} = 120$ mA, a 20 Ah battery of which 70 % is usable, and a duty-cycle
average $\bar I = I_{\text{sleep}} + I_{\text{acq}}D_{\text{acq}}
+ I_{\text{tx}}D_{\text{tx}}$:

| Scenario | Average current | Life |
|---|---|---|
| 10 min + 10 s once a day | 0.117 mA | 4976 days |
| 10 min + 10 s every 6 h | 0.409 mA | 1427 days |
| continuous acquisition | 12.034 mA | 48.5 days |

Three consequences. **Sleep current is the term to attack** — at one visit per day it
is 17 % of the average current, and the trade is between temporal coverage and visits.
**Transmit energy is disproportionate**: a 10 s burst at 120 mA costs the charge of
100 s of acquisition, so compressing, storing or delaying data is usually cheaper than
sending it. And **the life is a usable-charge calculation**: capacity falls with
temperature and age, and a design that relies on the nameplate capacity has no margin.

## 7. Timing without GNSS

With a fractional error $y$ and a tolerance $\tau$, the resynchronisation interval is
$T_{\text{sync}} = \tau/y$; with $\tau = 1$ ms:

| Oscillator | Fractional error | Error per day | Resync interval |
|---|---|---|---|
| uncompensated crystal | 30 ppm | 2592 ms | 33.33 s |
| TCXO | 1 ppm | 86.4 ms | 16.67 min |
| OCXO | 0.005 ppm | 0.432 ms | 55.56 h |

An uncompensated crystal cannot hold a 1 ms *absolute* budget for even a minute, which
is why GNSS disciplining or a deliberately relaxed requirement is unavoidable. The
escape is that most array work needs *relative* timing: if every node is disciplined at
the same moment, or the campaign records a common reference signal, the common part of
the clock error cancels and only the much smaller inter-node time-interval error
remains. Stating which of the two the science needs changes the design by orders of
magnitude.

## 8. Cost-effectiveness, and where a low-cost build wins

Ranking routes by noise floor per unit of *relative* cost makes the trade explicit
(synthetic columns):

| Route | Noise floor | Relative cost | Per unit |
|---|---|---|---|
| bare converter, no gain | 4768.00 nV | 10.0 | 476.800 |
| gain 100 + 24-bit | 47.68 nV | 18.0 | 2.649 |
| gain 1000 + 32-bit sigma-delta | 1.19 nV | 26.0 | 0.046 |
| gain 1000 + 4-sensor array | 0.60 nV | 40.0 | 0.015 |

The ordering is stable and general: **analog gain first, then bit depth, then
averaging several sensors**, because averaging $N$ independent sensors buys only
$\sqrt{N}$.

A low-cost build wins where **density or redundancy is the point** (temporary arrays
for interferometry, pilot surveys, long low-rate monitoring, teaching), and loses
wherever robustness and support dominate: regulatory and legal measurements, absolute
quantities compared across institutions, and harsh, remote or deep-water sites where
the service cost dwarfs the instrument cost.

## 9. Assumptions and regime of validity

1. **The noise is white and Gaussian.** The quadrature sum and the
   $\mathrm{LSB}/\sqrt{12}$ term both assume it; 1/f noise, interference and offsets
   are additive in the value domain and often larger.
2. **Everything is referred to one point**, before being added.
3. **The bandwidth is defined by a filter.** A noise floor without a band is
   meaningless, and a missing anti-alias filter makes the budget a fiction.
4. **The gain is known and stable.** A gain of 100 that is 3 % uncertain contributes a
   scale uncertainty that may exceed the noise floor's share.
5. **The duty cycle is achievable.** Sleep currents quoted warm can be several times
   larger cold, so the power budget is a design target, not a measurement.

## 10. The honest summary

- Resolution, band, duration and environment first; the binding one is usually the one
  that was omitted.
- Here the signal is 30 µV and the noise floor 1.378 µV: 26.8 dB single-sample SNR.
- Quantization noise is $\mathrm{LSB}/\sqrt{12}$ and it dominated the chain 3.8× over
  the analog front end; a gain of ~20 made the amplifier the limit, and more bits alone
  would have bought nothing.
- The budget was verified against a simulated record to 1.1 %; that verification is
  what justifies the build.
- Sleep current and transmit duty cycle set the service interval; the clock decides
  whether the data are usable at all.
- A low-cost instrument buys density and pays in robustness, calibration effort and
  analyst time — say so in the report.

## 11. Python demonstration

[`code/instrument_design_lowo_demo.py`](./code/instrument_design_lowo_demo.py) prints
every number quoted above: the requirement and signal, the four-term noise budget for
two converters, a seeded peak/median detection check against the analytic prediction,
the duty-cycle current and life for three scenarios, the resynchronisation interval for
three oscillators, and the cost-effectiveness ranking.

```bash
cd 23-field-methods-instruments/05-instrumentation-and-electronics/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python instrument_design_lowo_demo.py
```

## 12. Exercises

Worked problem sets are in
[`exercises/05-instrument-design-lowo-exercises.md`](./exercises/05-instrument-design-lowo-exercises.md)
and
[`exercises/05-instrument-design-lowo-solutions.md`](./exercises/05-instrument-design-lowo-solutions.md).

## 13. Mastery checkpoint

Without notes:

1. A synthetic sensor has $40$ V/(m/s) and the requirement is
   $5\times10^{-7}$ m/s. Compute the signal voltage.
2. Compute $\mathrm{LSB}$ and the quantization noise rms for a 16-bit converter at
   $\pm1.25$ V.
3. Compute the total noise for a chain with 20 nV Johnson, 60 nV amplifier voltage,
   5 nV current and 1200 nV quantization, and state the dominant term.
4. Compute the average current for 2 mA acquisition at a 1 % duty cycle over a 30 µA
   sleep current, and the life from 10 Ah usable.
5. State the two halves of a timing requirement and how the design changes between
   them.

## 14. Common pitfalls

1. **Choosing the sensor first.** The requirement chooses the sensor, not the reverse.
2. **Quoting the LSB as the noise floor.** It is $\mathrm{LSB}/\sqrt{12}$, and the
   display is neither.
3. **Adding terms referred to different points.** The dominant term disappears.
4. **Forgetting the anti-alias filter.** The band is then the converter's, not the
   signal's.
5. **Ignoring cold-temperature sleep current.** The power budget fails on the first
   cold night.
6. **A programmable gain with no record.** It becomes an unknown scale factor.
7. **No test access.** An instrument that cannot be checked produces data nobody can
   defend.

## 15. Where this is used

- Teaching laboratories, where the build is the curriculum and the calibration is the
  assessment.
- Dense temporary arrays for noise interferometry and microseismic monitoring, where
  station count matters more than single-station quality — see
  [23-02-03 Seismic Network and Array Design](../02-seismic-instruments-and-fieldwork/03-seismic-network-design.md).
- Pilot and reconnaissance surveys before an expensive campaign.
- Long-duration environmental monitoring, where the same chain runs for years.
- Sensor networks and their power and timing budgets — see
  [06 IoT and Autonomous Sensor Networks](06-iot-sensor-networks.md).

## 16. Related lessons

- [01 Sensors and Transducers: Principles and Selection](01-sensors-and-transducers.md) —
  the terms in the noise budget.
- [02 Amplification, Filtering and Analog-Digital Conversion](02-signal-conditioning.md) —
  gain, filtering and ENOB in detail.
- [04 Calibration, Testing and Traceability](04-calibration-and-testing.md) —
  the acceptance tests a build must pass.
- [06 IoT and Autonomous Sensor Networks](06-iot-sensor-networks.md) —
  the same budgets at network scale.

## 17. Self-assessment checklist

- [ ] I can write a requirement as resolution, band, duration and environment.
- [ ] I can build a noise budget referred to the sensor output.
- [ ] I can compute quantization noise and identify the crossover gain.
- [ ] I can verify a budget against a simulated record.
- [ ] I can compute average current, battery life and the service interval.
- [ ] I can compute a resynchronisation interval from an oscillator error.
- [ ] I can rank design routes by noise floor per unit cost.
