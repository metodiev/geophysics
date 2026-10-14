---
id: 23-05-02
title: "Amplification, Filtering and Analog-Digital Conversion"
level: graduate
prereqs: ["23-05-01", "23-02-02"]
estimated_minutes: 95
tags: [instrumentation, amplifiers, noise-figure, filters, adc, oversampling]
---

# Amplification, Filtering and Analog-Digital Conversion

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** the input-referred noise of an amplifier plus source and the
   resulting noise figure, and **distinguish** the noise-figure optimum from the
   absolute-noise optimum.
2. **Compute** the noise figure of a two-stage chain with the Friis formula and
   **explain** why the first stage must be the quiet one.
3. **Convert** a measured SINAD into an effective number of bits.
4. **Compute** the bits that oversampling and decimation buy.
5. **Compute** the anti-alias filter order a transition ratio requires.
6. **Compute** the closed-loop bandwidth a gain leaves, and **design** a chain
   around the gain-bandwidth product.

All amplifier noise densities, gains, converter figures, oversampling ratios and
filter specifications in this lesson are **SYNTHETIC** teaching values, combined
with the standard relations quoted in the text. No component data sheet or
manufacturer figure is used or reproduced.

## Prerequisites

- [01 Sensors and Transducers: Principles and Selection](01-sensors-and-transducers.md) —
  the signal source this chain conditions.
- [23-02-02 Digitizers, Dynamic Range, Gain and Anti-Alias Filtering](../02-seismic-instruments-and-fieldwork/02-digitizers-and-gain.md) —
  the quantisation and aliasing arithmetic reused here.

## 1. Intuition: the chain has one quiet place and it must be first

A signal-conditioning chain is an amplifier, a filter, and a converter, in some
order. The order matters more than the individual specifications, because noise
added early is amplified by everything after it, while noise added late is not.
The one result that governs the whole design is the **Friis formula**:

$$F_{\text{total}} = F_1 + \frac{F_2 - 1}{G_1} + \frac{F_3 - 1}{G_1 G_2} + \cdots$$

where $F_i$ are noise factors (linear, not dB) and $G_i$ are the stage gains. The
first stage's noise figure passes through untouched; every later stage's excess
noise is divided by the gain in front of it. Three design consequences follow
immediately: **put the low-noise amplifier first**, **give it enough gain** that the
later stages' contributions become negligible, and **do not add loss before it** (a
long cable, an attenuator, or a badly matched transformer is a lossy stage whose
noise factor appears first).

## 2. Input-referred noise and the noise figure

An amplifier's noise is specified by two densities: a voltage noise $e_n$ and a
current noise $i_n$. With a source resistance $R$, the input-referred noise is

$$v_{\text{in}} = \sqrt{e_n^{2} + (i_n R)^{2} + 4kTR} ,$$

in which the last term is the source's own Johnson noise. With
$e_n = 10\ \mathrm{nV/\sqrt{Hz}}$, $i_n = 1\ \mathrm{pA/\sqrt{Hz}}$ and
$T = 300$ K:

| $R$ (Ω) | source (nV/√Hz) | total (nV/√Hz) | noise figure (dB) |
|---|---|---|---|
| 100 | 1.287 | 10.083 | 17.88 |
| 1 000 | 4.070 | 10.843 | 8.51 |
| 10 000 | 12.872 | 19.123 | 3.44 |
| 100 000 | 40.704 | 108.429 | 8.51 |
| 1 000 000 | 128.716 | 1008.299 | 17.88 |

Two distinct quantities are visible and it is a classic error to conflate them:

- **The absolute input-referred noise falls monotonically as $R$ falls** (at
  $R \to 0$ it is $e_n$). If the goal is the smallest possible noise voltage, a
  low-impedance source and a low-$e_n$ amplifier win.
- **The noise figure is a ratio** — the total noise divided by the source's own
  thermal noise — and it has a minimum at

$$R_{\text{opt}} = \frac{e_n}{i_n} = \frac{10\ \mathrm{nV/\sqrt{Hz}}}
{1\ \mathrm{pA/\sqrt{Hz}}} = 10\ \mathrm{k\Omega},$$

where the table shows 3.44 dB. The noise figure is the right figure of merit when
the source's thermal noise is the reference (radio reception, for example); the
absolute noise is the right one when the question is "what is the smallest signal I
can see" (most geophysical sensors). Choosing an amplifier by its noise figure
without checking the source impedance is how a "0.5 dB" amplifier ends up in a
circuit where it is the dominant noise.

## 3. Two stages, and why order matters

The demonstration's two chains, each with a 20 dB (100×) gain:

| Configuration | $F_1$ | $G_1$ | $F_2$ | $F_{\text{total}}$ | NF (dB) |
|---|---|---|---|---|---|
| low-noise stage first | 1.5 | 100 | 4.0 | 1.5300 | 1.85 |
| noisy stage first | 4.0 | 100 | 1.5 | 4.0050 | 6.03 |

Placing the 1.5 noise factor first gives 1.85 dB overall; placing the 4.0 first
gives 6.03 dB. The 3.5 dB difference is bought by nothing but the order, and it is
larger than the improvement obtainable by upgrading either stage. **Gain is the
tool that makes later noise irrelevant**: with $G_1 = 100$, the second stage's
excess noise factor of 3 contributes only 0.03 to the total.

The corollary is that **a lossy stage first is a disaster**: a passive attenuator
has $G_1 < 1$ and a noise factor equal to its loss, and it multiplies every later
stage's contribution by $1/G_1 > 1$. This is why the cable, the connector and the
input protection must be part of the noise model, not an afterthought.

## 4. From SINAD to effective bits

A converter's *quoted* resolution is the number of bits; its *useful* resolution is
the effective number of bits derived from the measured signal-to-noise-and-distortion
ratio:

$$\text{ENOB} = \frac{\text{SINAD} - 1.76}{6.02}\ \text{bits}.$$

| SINAD (dB) | 60.0 | 70.0 | 90.0 | 110.0 | 130.0 |
|---|---|---|---|---|---|
| ENOB (bits) | 9.67 | 11.34 | 14.66 | 17.98 | 21.30 |

A "24-bit" converter with a measured SINAD of 110 dB delivers **17.98 effective
bits**; the remaining six are lost to thermal noise, distortion and reference noise.
The number that matters for a measurement is the ENOB, and it must be measured at
the *input* of the converter with the *actual* source impedance — the same
distinction as in
[23-05-04 Calibration, Testing and Traceability](04-calibration-and-testing.md).

## 5. Oversampling and decimation

Averaging $N$ samples of white noise reduces the noise by $\sqrt{N}$, so each
doubling of the sample rate buys **0.5 bit**:

| Oversampling ratio | bits bought | 16-bit base |
|---|---|---|
| 1 | 0.00 | 16.00 |
| 4 | 1.00 | 17.00 |
| 16 | 2.00 | 18.00 |
| 64 | 3.00 | 19.00 |
| 256 | 4.00 | 20.00 |
| 1024 | 5.00 | 21.00 |

Two conditions, both routinely violated in practice: the noise must be
**uncorrelated** between samples (quantisation noise and thermal noise are;
1/f noise and coherent interference are not, and are not reduced at all), and the
signal must be **unchanged** over the averaging window (true below the decimated
Nyquist frequency, false above it — where the averaging is aliasing). The gain is
therefore real, but it is not free: the sample rate, the digital filtering and the
power all scale with the ratio.

## 6. Filters, order and the transition ratio

An anti-alias filter is specified by its **transition ratio**: where the stopband
must start, relative to the corner. The Butterworth attenuation is

$$\text{att}(f) = 10\log_{10}\!\left(1 + (f/f_c)^{2n}\right) \approx
20n\log_{10}(f/f_c)\ \mathrm{dB},$$

so the order required for a stated attenuation is inversely proportional to
$\log_{10}(f/f_c)$:

| $f/f_c$ | order for 60 dB | order for 100 dB |
|---|---|---|
| 1.5 | 18 | 29 |
| 2.0 | 10 | 17 |
| 4.0 | 5 | 9 |
| 10.0 | 3 | 5 |

**The order is set by the transition ratio, not by the attenuation alone.** A
filter whose corner sits close to the band edge is expensive — 18 poles for 60 dB
at $f/f_c = 1.5$ — while one with a comfortable transition ratio is cheap. The
design freedom is therefore not the filter order but the *sampling rate*: sampling
much faster than needed moves the fold far from the band and makes the filter easy,
at the cost of data rate and power. That is the same trade as oversampling
(Section 5), seen from the other side.

## 7. Assumptions and regime of validity

1. **Linear, small-signal operation.** Gain compression and slew-rate limiting
   break every relation here, and they produce harmonics that no filter removes.
2. **White noise.** The formulas assume flat noise densities; 1/f noise rises below
   a device-specific corner, and the corner frequency must come from the device's
   own documentation.
3. **Matched, resistive sources.** A reactive source (a piezoelectric sensor, an
   electrode pair) requires the frequency-dependent treatment of
   [01 Sensors and Transducers](01-sensors-and-transducers.md).
4. **Noise factors from the data sheet are typical.** The noise figure of a real
   stage depends on the bias, the temperature and the source impedance; a measured
   value at the intended operating point is the only defensible one.
5. **Oversampling assumes uncorrelated noise and a stationary signal.** Coherent
   interference is not averaged away, and a signal that changes within the window
   is distorted by the decimation filter.
6. **The gain-bandwidth product is a small-signal, single-pole approximation.**
   Real amplifiers have additional poles, and the bandwidth must be verified in the
   loop configuration actually used — including the capacitive load of a long cable.

## 8. The honest summary

- Noise added early is amplified; noise added late is not: put the quiet stage
  first, and never a lossy stage first.
- The input-referred noise falls monotonically with source resistance; the *noise
  figure* has a minimum at $e_n/i_n = 10\ \mathrm{k\Omega}$ here. They are
  different quantities.
- Two stages with the same parts gave 1.85 dB or 6.03 dB depending only on the
  order.
- A "24-bit" converter with 110 dB SINAD delivers 17.98 effective bits.
- Oversampling buys 0.5 bit per doubling; the anti-alias filter order is set by the
  transition ratio, not the attenuation.

## 9. Python demonstration

[`code/signal_conditioning_demo.py`](./code/signal_conditioning_demo.py) prints
every number quoted above. It:

1. tabulates source, total and noise-figure values for five source resistances and
   identifies the noise-figure optimum;
2. applies the Friis formula to two gain orders;
3. converts five SINAD values into ENOB;
4. tabulates the bits bought by six oversampling ratios;
5. computes the filter order for 60 dB and 100 dB at four transition ratios;
6. tabulates the closed-loop bandwidth for five gains at a 10 MHz gain-bandwidth
   product.

Run it with the project virtual environment:

```bash
cd 23-field-methods-instruments/05-instrumentation-and-electronics/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python signal_conditioning_demo.py
```

## 10. Exercises

Worked problem sets are in
[`exercises/02-signal-conditioning-exercises.md`](./exercises/02-signal-conditioning-exercises.md)
and
[`exercises/02-signal-conditioning-solutions.md`](./exercises/02-signal-conditioning-solutions.md).

## 11. Mastery checkpoint

Without notes:

1. An amplifier has $e_n = 5\ \mathrm{nV/\sqrt{Hz}}$ and
   $i_n = 0.5\ \mathrm{pA/\sqrt{Hz}}$. Compute its noise-figure optimum source
   resistance.
2. Compute the input-referred noise at $R = 10\ \mathrm{k\Omega}$, $T = 300$ K.
3. Two stages have $F_1 = 2$, $G_1 = 50$, $F_2 = 10$. Compute $F_{\text{total}}$ in
   linear and dB, and repeat with the stages reversed.
4. A converter has a measured SINAD of 84 dB. Compute its ENOB, and the oversampling
   ratio needed to gain two bits.
5. Compute the Butterworth order for 80 dB attenuation at $f/f_c = 3$.
6. An op-amp has a 5 MHz gain-bandwidth product. Compute the bandwidth at a gain of
   500 and state whether a 20 kHz anti-alias corner is achievable.

## 12. Common pitfalls

1. **Selecting an amplifier by noise figure without checking the source
   impedance.** The optimum is at $e_n/i_n$.
2. **A long cable before the first amplifier.** It is a lossy stage with
   $G < 1$ and it multiplies every later contribution.
3. **Quoting the converter's bits.** Quote the measured ENOB instead.
4. **Assuming oversampling removes coherent interference.** It does not.
5. **Designing the anti-alias filter for a transition ratio of 1.1.** It needs 18
   poles.
6. **Ignoring the gain-bandwidth product.** A large gain may not have the bandwidth
   for the anti-alias corner.
7. **Adding gain in one stage.** Noise and stability are both worse; stage the
   gain.

## 13. Where this is used

- Every instrument front end: seismometers, gravimeters, magnetometers, EM
  receivers, thermometry and pressure systems.
- Data loggers and digitizers, where the converter's ENOB and the anti-alias
  filter set the achievable dynamic range.
- Laboratory measurement systems, where the low-noise first stage is the difference
  between a measurement and a demonstration.
- Sensor networks, where the power budget makes oversampling expensive and the
  filter order a real design driver.
- Any instrument built from discrete parts — the subject of
  [05 Building Low-Cost Instruments for Teaching and Research](05-instrument-design-lowo.md).

## 14. Related lessons

- [01 Sensors and Transducers: Principles and Selection](01-sensors-and-transducers.md) —
  the source that sets the impedance and the noise budget.
- [23-02-02 Digitizers, Dynamic Range, Gain and Anti-Alias Filtering](../02-seismic-instruments-and-fieldwork/02-digitizers-and-gain.md) —
  the same converter arithmetic with a different emphasis.
- [20-03-01 FIR Filter Design](../../20-signal-processing/03-digital-filtering/01-fir-filters.md) —
  the digital side of the same filtering problem.
- [04 Calibration, Testing and Traceability](04-calibration-and-testing.md) —
  how the ENOB and the noise figure are measured rather than assumed.
- [06 IoT and Autonomous Sensor Networks for Earth Monitoring](06-iot-sensor-networks.md) —
  where the power budget meets these choices.

## 15. Self-assessment checklist

- [ ] I can compute input-referred noise and a noise figure.
- [ ] I can distinguish the noise-figure optimum from the absolute-noise optimum.
- [ ] I can apply the Friis formula and argue about stage order.
- [ ] I can convert SINAD to ENOB and compute oversampling gain.
- [ ] I can compute a filter order from a transition ratio.
- [ ] I can check a gain against a gain-bandwidth product.
