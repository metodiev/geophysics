---
id: 23-05-01
title: "Sensors and Transducers: Principles and Selection"
level: advanced
prereqs: ["02-07-01", "23-02-01"]
estimated_minutes: 95
tags: [instrumentation, sensors, transducers, bridges, noise, selection]
---

# Sensors and Transducers: Principles and Selection

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** the dynamic range of a sensor from its full scale and its
   resolution, and **express** it in bits.
2. **Compute** the output of a resistive strain gauge in a quarter bridge, and
   **state** why the signal is small.
3. **Compute** the high-pass corner of a piezoelectric sensor from its capacitance
   and the amplifier's input resistance, and **state** what such a sensor cannot
   measure.
4. **Compute** the Johnson noise of a resistive sensor and the resolution floor it
   imposes.
5. **Select** a sensing principle for a stated band, range and environment, and
   **state** the limitation each principle brings.
6. **State** what a sensor's data sheet does not tell you and must be measured.

All gauge factors, capacitances, resistances, temperatures and bandwidths in this
lesson are **SYNTHETIC** teaching values, combined with the standard relations
quoted in the text. No component data sheet, manufacturer figure or measured
instrument is used or reproduced.

## Prerequisites

- [02-07-01 Electric Fields, Potential and Conductors](../../02-physics/07-electromagnetism/01-electrostatics.md) —
  the circuit concepts used here.
- [23-02-01 Seismometers: Broadband, Short-Period, Geophones, MEMS](../02-seismic-instruments-and-fieldwork/01-seismometers.md) —
  an inertial sensor worked through in the same style.

## 1. Intuition: a sensor is a converter with two limits

Every sensor converts one physical quantity into another (usually a voltage or a
charge) and every one of them is described by the same four things:

- **Sensitivity** — the output per unit input, with its units.
- **Resolution** — the smallest input change that produces a detectable output
  change, which is set by noise, not by the display.
- **Band** — the range of frequencies over which the sensitivity is defined, and
  the corners that bound it.
- **Environment** — the temperature, humidity, electromagnetic and mechanical
  conditions in which those numbers hold.

The **dynamic range** combines the first two:

$$\text{DR} = 20\log_{10}\frac{\text{full scale}}{\text{resolution}}\ \mathrm{dB},$$

and it is worth expressing in bits, because that is the currency of the digitizer
downstream:

| Sensor | Full scale | Resolution | Range (dB) | Equivalent bits |
|---|---|---|---|---|
| displacement | 1 mm | 1 nm | 120.0 | 19.9 |
| velocity | 10 m/s | 1 nm/s | 200.0 | 33.2 |
| acceleration | 10 g | 1 µg | 159.8 | 26.5 |
| temperature | 1 K | 0.1 mK | 80.0 | 13.3 |

"Equivalent bits" is $\log_2(\text{full scale}/\text{resolution})$, the number of
bits a perfect converter would need. It is a useful sanity check: a claim of 33
equivalent bits requires a converter and an analogue chain that no 24-bit system
provides without oversampling and averaging, so a sensor specification quoted in
those terms should be read with the *measurement* conditions attached.

## 2. Resistive transducers: the bridge

A resistive transducer (a strain gauge, a piezoresistive pressure sensor, a
thermistor) converts the physical quantity into a resistance change. The
measurement is made with a **bridge**, because a bridge converts a small
*relative* resistance change into a voltage while rejecting the common-mode
excitation:

$$\Delta R = G_F R\,\varepsilon, \qquad
V_{\text{out}} = V_{\text{ex}}\frac{\Delta R}{4R}
= \frac{V_{\text{ex}} G_F \varepsilon}{4}$$

for a **quarter bridge** (one active element). The demonstration's values, for a
350 Ω gauge with $G_F = 2.0$ and a 5 V excitation:

| Strain (µε) | $\Delta R$ (Ω) | Output (mV) |
|---|---|---|
| 1 | 0.00070 | 0.0025 |
| 10 | 0.00700 | 0.0250 |
| 100 | 0.07000 | 0.2500 |
| 1000 | 0.7000 | 2.5000 |

The signal is **microvolts per microstrain**. Three consequences follow:

1. **An instrumentation amplifier is mandatory**, with a gain of order $10^{3}$ and
   a common-mode rejection ratio high enough to keep the bridge's 5 V common-mode
   signal out of the output.
2. **The excitation should be a *ratio*, not an absolute voltage.** In a ratiometric
   measurement the digitizer uses the same excitation as its reference, so the
   excitation's own drift cancels; with an independent reference it does not.
3. **Self-heating is a real limit.** The power dissipated in a 350 Ω gauge at 5 V is
   about 71 mW, which warms the gauge and shifts the very resistance being measured;
   lower excitation or a pulsed measurement is the standard remedy.

## 3. Piezoelectric transducers: no DC

A piezoelectric element delivers a charge proportional to the applied force or
strain, so it behaves as a current source into the amplifier's input network. The
combination of the sensor capacitance $C$ and the amplifier input resistance $R$
forms a **high-pass** whose corner is

$$f_c = \frac{1}{2\pi RC} .$$

For $C = 1$ nF and $R = 1$ GΩ the demonstration reports

$$f_c = \frac{1}{2\pi \times 10^{9} \times 10^{-9}} = 0.1592\ \mathrm{Hz},$$

with the response $f/f_c / \sqrt{1+(f/f_c)^{2}}$:

| $f$ (Hz) | 0.01 | 0.05 | 0.16 | 1.00 | 10.0 | 100 |
|---|---|---|---|---|---|---|
| relative response | 0.0627 | 0.2997 | 0.7090 | 0.9876 | 0.9999 | 1.0000 |
| dB | −24.05 | −10.47 | −2.99 | −0.11 | −0.00 | −0.00 |

Three practical statements follow. **A piezoelectric sensor cannot measure a static
quantity** — it is a high-pass device by construction, and this includes a DC
component of a slow signal. **The corner is set by the *system*, not the sensor**:
a longer cable adds capacitance, which raises the corner and reduces the sensitivity
(more charge is shunted into the cable), which is why charge amplifiers with
short, low-capacitance cables and guarded inputs are used. And **the corner moves
with temperature and humidity** at the amplifier's input, which is one reason
piezoelectric sensors are used above a few hertz and in a controlled environment.

## 4. Noise: the resolution floor

The resolution of a resistive sensor is ultimately set by the thermal (Johnson)
noise of its own resistance:

$$v_n = \sqrt{4kTRB},$$

with $k = 1.380649\times10^{-23}$ J/K, $T$ in K and $B$ the measurement bandwidth in
Hz. At $T = 300$ K over $B = 1000$ Hz:

| $R$ (Ω) | $v_n$ (nV) | $v_n/\sqrt{B}$ (nV/√Hz) |
|---|---|---|
| 100 | 40.704 | 1.287 |
| 1 000 | 128.716 | 4.070 |
| 10 000 | 407.035 | 12.872 |
| 100 000 | 1287.159 | 40.704 |
| 1 000 000 | 4070.355 | 128.716 |

The noise rises as $\sqrt{R}$, so a high-resistance sensor is noisier for a
voltage-sensing amplifier — but a higher resistance also means a given *power* or a
given *current* signal is larger, and the choice between voltage and current
amplification is made from the impedance. The engineering rules:

1. **Match the amplifier to the source impedance.** For a low-impedance source
   (a geophone coil, a strain gauge), the amplifier's *voltage* noise matters; for a
   high-impedance source (a piezoelectric element, an electrode pair), its *current*
   noise and its input resistance matter.
2. **Restrict the bandwidth** to what the signal needs: the noise scales as
   $\sqrt{B}$, so bandwidth is noise, and anti-alias filtering is also a noise
   reduction.
3. **Average in time** where the signal is repeatable: the noise falls as
   $\sqrt{N}$, which is the same arithmetic as
   [23-04-02 EM Fieldwork](../04-electrical-em-fieldwork/02-em-fieldwork.md)'s stacking.
4. **Beware of 1/f noise.** The formula above is white noise only; below a corner
   frequency (which is device-specific and must come from the device's own
   documentation) the noise rises, and no amount of averaging at DC removes it.

## 5. Selection

| Principle | Band | Strength | Limitation |
|---|---|---|---|
| Resistive strain | DC to kHz | simple, absolute, rugged | self-heating, thermal drift |
| Piezoelectric | 0.1 Hz to MHz | wide band, high sensitivity | no DC, charge leakage |
| Capacitive | DC to kHz | very high resolution | stray capacitance, humidity |
| Inductive / eddy current | DC to tens of kHz | non-contact, robust | conductive targets only |
| Optical fibre | DC to GHz | immune to EMI, distributed sensing | fragile, higher cost |
| MEMS | DC to tens of kHz | small, cheap, arrayable | higher noise, drift |

The selection is driven by three questions, in this order: **what band** (a static
quantity rules out piezoelectric; a MHz band rules out most resistive sensors),
**what environment** (an electrically noisy site favours optical or
differential-output sensors; a wet site rules out unbuffered capacitive sensors),
and **what dynamic range** (which brings the noise budget of Section 4 into the
choice). No principle wins everywhere, and the same physical quantity — strain —
is measured by four different principles depending on the band and the environment.

## 6. Assumptions and regime of validity

1. **Linear, time-invariant behaviour.** All the relations above are small-signal
   linearisations. Large strain, saturation in a piezoresistive element and
   hysteresis in a magnetostrictive one all break them, and the break is usually
   reported as a calibration error.
2. **A single-degree-of-freedom band model.** The high-pass corner of Section 3 and
   the resonance of an inertial sensor are both single-mode pictures; real devices
   have several.
3. **Known constants.** $G_F$, $C$, $R$ and $k$ are taken as exact; a gauge factor
   known to ±2 % gives a 2 % scale error for free, and $R$ in the noise formula is
   the *physical* resistance including any series and shunt paths.
4. **White noise.** The Johnson formula is the thermal floor; 1/f, shot,
   quantisation, triboelectric and cable-motion noise all add.
5. **A constant environment.** Sensitivity is a function of temperature, and the
   temperature coefficient of the *sensor* and of the *bridge completion* elements
   must both be considered: a bridge with two active elements in opposite arms
   cancels the temperature effect to first order.
6. **The data sheet is a typical specification.** It describes a typical device at
   a stated temperature and a stated drive level. What matters for a measurement is
   the *individual* device in the *actual* environment, which is why calibration
   exists.

## 7. The honest summary

- Dynamic range is $20\log_{10}(\text{full scale}/\text{resolution})$ dB, and it
  converts to equivalent bits; 33 equivalent bits is a claim that needs
  justification.
- A quarter-bridge strain gauge returns microvolts per microstrain: amplification
  and ratiometric excitation are mandatory.
- A piezoelectric sensor's corner is $1/(2\pi RC)$ — 0.159 Hz here — and it cannot
  measure a static quantity.
- Johnson noise is $\sqrt{4kTRB}$: 128.7 nV from a 1 kΩ resistor in a 1 kHz band,
  and it rises as $\sqrt{R}$ and as $\sqrt{B}$.
- Selection follows band, environment and dynamic range, in that order.

## 8. Python demonstration

[`code/sensors_and_transducers_demo.py`](./code/sensors_and_transducers_demo.py)
prints every number quoted above. It:

1. computes the dynamic range and equivalent bits of four sensor specifications;
2. tabulates the resistance change and bridge output for four strains;
3. computes a piezoelectric high-pass corner and its response at six frequencies;
4. tabulates Johnson noise for five resistances;
5. prints a selection table by band, strength and limitation.

Run it with the project virtual environment:

```bash
cd 23-field-methods-instruments/05-instrumentation-and-electronics/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python sensors_and_transducers_demo.py
```

## 9. Exercises

Worked problem sets are in
[`exercises/01-sensors-and-transducers-exercises.md`](./exercises/01-sensors-and-transducers-exercises.md)
and
[`exercises/01-sensors-and-transducers-solutions.md`](./exercises/01-sensors-and-transducers-solutions.md).

## 10. Mastery checkpoint

Without notes:

1. A sensor has a full scale of 2 mm and a resolution of 5 nm. Compute its dynamic
   range in dB and in equivalent bits.
2. A 120 Ω strain gauge with $G_F = 2.1$ is strained by 50 µε. Compute $\Delta R$
   and the quarter-bridge output at 2.5 V excitation.
3. A piezoelectric sensor has $C = 2$ nF and the amplifier's input resistance is
   500 MΩ. Compute the high-pass corner.
4. Compute the Johnson noise of a 5 kΩ resistor in a 100 Hz band at 290 K.
5. State which sensing principle you would choose for a static strain measurement on
   a structure and why.

## 11. Common pitfalls

1. **Reading a resolution from a display.** Noise sets it.
2. **Forgetting the bridge's common-mode voltage.** It is thousands of times the
   signal.
3. **Using a piezoelectric sensor for a quasi-static measurement.** The corner
   imposes a high-pass and the result will look like a drift.
4. **Assuming the data sheet's noise at your bandwidth.** Noise scales as
   $\sqrt{B}$.
5. **Ignoring self-heating in a resistive sensor.** It changes the quantity being
   measured.
6. **Trusting a gauge factor from a data sheet for a quantitative measurement.**
   It must be calibrated for the device in place.
7. **Ignoring the temperature coefficients of the sensor and the bridge.** They
   appear as a drift indistinguishable from a real slow signal.

## 12. Where this is used

- Every geophysical instrument: seismometers, gravimeters, magnetometers,
  electrodes, thermistors, pressure transducers and tiltmeters each use one of the
  principles above.
- Borehole tools, where temperature and pressure are the environment and the
  sensors are packaged for it.
- Laboratory rock-physics apparatus, where strain gauges and LVDTs measure the
  deformation of a sample.
- Monitoring networks, where the long-term drift of a sensor (not its resolution)
  becomes the limiting factor.
- Any instrument the reader builds: the bridge, the corner and the noise floor are
  the three calculations that decide whether it can measure the target.

## 13. Related lessons

- [02 Amplification, Filtering and Analog-Digital Conversion](02-signal-conditioning.md) —
  what happens to the sensor's output next.
- [03 Timing, GNSS Disciplining and Clock Accuracy](03-timing-and-gnss-instruments.md) —
  the other half of an instrument's specification.
- [04 Calibration, Testing and Traceability](04-calibration-and-testing.md) —
  how a sensor's actual sensitivity is established rather than assumed.
- [05 Building Low-Cost Instruments for Teaching and Research](05-instrument-design-lowo.md) —
  these principles applied to a complete instrument.
- [23-02-01 Seismometers: Broadband, Short-Period, Geophones, MEMS](../02-seismic-instruments-and-fieldwork/01-seismometers.md) —
  an inertial sensor treated in the same way.

## 14. Self-assessment checklist

- [ ] I can compute a dynamic range in dB and in bits.
- [ ] I can compute a bridge output from a strain and a gauge factor.
- [ ] I can compute a piezoelectric high-pass corner.
- [ ] I can compute Johnson noise and state how it scales.
- [ ] I can select a sensing principle from band, environment and range.
- [ ] I can state what a data sheet does not tell me.
