---
id: 23-02-01
title: "Seismometers: Broadband, Short-Period, Geophones, MEMS"
level: advanced
prereqs: ["20-01-04", "06-01-02"]
estimated_minutes: 90
tags: [seismology, instruments, seismometer, response, noise, geophone]
---

# Seismometers: Broadband, Short-Period, Geophones, MEMS

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the response of a single-degree-of-freedom inertial sensor to
   harmonic ground motion, in displacement, velocity and acceleration form.
2. **Compute** the response magnitude $|H(f)|$ of a sensor with a given natural
   frequency and damping, and **convert** it to decibels.
3. **Distinguish** the corner frequency from the usable low-frequency limit, and
   **compute** the latter from the self-noise and the ambient noise level.
4. **Compute** the input-referred self-noise at any frequency from the output
   noise, the generator constant and the response.
5. **Compute** the clip level, the electronic dynamic range and the usable
   amplitude window of a sensor-plus-digitizer combination.
6. **Choose** among broadband, short-period, geophone and MEMS sensors for a
   stated target band and ground-motion level, and **state** what each cannot do.

Every response, noise level, generator constant and ambient spectrum in this
lesson is **SYNTHETIC**. The sensors are described generically by their natural
frequency, damping and generator constant; no manufacturer model, catalogue
response or measured noise curve is used or reproduced.

## Prerequisites

- [20-01-04 Transfer Functions, Poles and Zeros](../../20-signal-processing/01-signals-and-systems/04-transfer-functions.md) —
  the transfer-function language this lesson applies to an instrument.
- [06-01-02 P and S Waves: Particle Motion, Speeds and Polarisation](../../06-seismology/01-elastic-wave-propagation/02-p-and-s-waves.md) —
  what the ground motion being measured actually is.

## 1. Intuition: an inertial reference

A seismometer does not measure ground motion directly. It measures the motion of
a **proof mass** that is elastically suspended inside a frame that moves with the
ground. Because the mass has inertia, it tends to stay where it was while the
frame accelerates underneath it, and the relative displacement between mass and
frame is what a transducer converts into a voltage.

The consequence is the central idea of this lesson: **the sensor's output depends
on frequency, and at long periods the mass follows the ground so faithfully that
there is nothing left to measure relative to the frame.** Every sensor is
therefore a band-pass device, and the lowest frequency it can usefully record is
determined by the interaction of three things: its own corner, its self-noise and
the noise level of the site.

Three physical arrangements are in common use, and they differ in how the
relative motion is sensed and controlled:

- **Passive short-period and geophone sensors.** A moving coil in a magnet; the
  output voltage is proportional to the *relative velocity* of the mass. Simple,
  cheap, robust, and band-limited at the low end by the corner frequency.
- **Force-feedback broadband sensors.** A feedback network applies a force to
  hold the mass near its rest position; the feedback current, which is
  proportional to ground acceleration over a wide band, is the output. The
  feedback decouples the useful band from the mechanical corner.
- **MEMS accelerometers.** A silicon proof mass on a micromachined spring, sensed
  capacitively. Above the mechanical resonance the output is proportional to
  ground *acceleration*, which makes the sensor flat in acceleration — good for
  strong motion, and with a noise floor that is far above the weak ambient
  signals a broadband sensor is built to resolve.

## 2. The response of a single-degree-of-freedom sensor

Let the frame displacement be $x_g(t)$ and the mass displacement be $x_m(t)$; the
relative displacement is $u = x_m - x_g$. Newton's second law for the mass gives

$$\ddot u + 2h\omega_0 \dot u + \omega_0^{2} u = -\ddot x_g,$$

with $\omega_0 = 2\pi f_0$ the angular natural frequency and $h = c/(2\sqrt{km})$
the damping ratio. For harmonic ground displacement
$x_g = X e^{i\omega t}$, the relative displacement is

$$u(\omega) = \frac{\omega^{2} X}{\omega_0^{2} - \omega^{2} + 2ih\omega_0\omega},$$

so the response to **ground displacement**, normalised to unity at high
frequency, has magnitude

$$|H_d(f)| = \frac{r^{2}}
{\sqrt{(1-r^{2})^{2} + (2hr)^{2}}}, \qquad r = \frac{f}{f_0}.$$

A **velocity transducer** (geophone, short-period sensor) generates a voltage
proportional to $\dot u$, so its response to ground velocity is the same function
multiplied by $\omega/\omega$ — that is, the same expression above. This is the
convenient accident that makes a moving-coil sensor flat in *velocity* above its
corner. A **displacement transducer** outputting $u$ directly is flat in
*displacement*; an **accelerometer** is flat in *acceleration*.

The three limits follow immediately from the formula:

- $r \gg 1$: $|H| \to 1$ — the mass is effectively stationary in space and the
  output tracks the ground.
- $r \approx 1$: $|H| = 1/(2h)$ — a *notch* whose depth is set by the damping.
  For $h = 0.7$, $|H| = 0.7143$, i.e. 2.92 dB down, which is exactly the value
  the table shows at $f = 4.50\ \mathrm{Hz}$ for the geophone. The response
  magnitude of a velocity sensor has no interior maximum: it rises monotonically
  to 1. (The classic resonance *peak* belongs to the displacement response
  $|H|/r^{2}$, which is peakless — maximally flat — at $h = 1/\sqrt{2}$.)
- $r \ll 1$: $|H| \approx r^{2} = (f/f_0)^{2}$ — a 12 dB per octave roll-off.

## 3. The response in numbers

The demonstration evaluates three synthetic sensors. Their response magnitudes,
in dB, are

| $f$ (Hz) | geophone, $f_0 = 4.5$ Hz | short-period, $f_0 = 1$ Hz | broadband, $f_0 = 1/120$ Hz |
|---|---|---|---|
| 0.01 | −106.13 | −80.00 | −1.63 |
| 0.05 | −78.17 | −52.04 | 0.00 |
| 0.10 | −66.13 | −40.00 | 0.00 |
| 0.50 | −38.17 | −12.26 | 0.00 |
| 1.00 | −26.13 | −2.92 | 0.00 |
| 4.50 | −2.92 | −0.00 | 0.00 |
| 10.00 | −0.14 | 0.00 | 0.00 |
| 50.00 | 0.00 | 0.00 | 0.00 |

All three have $h = 0.70$; the −3 dB corner is 4.4552 Hz for the geophone,
0.9900 Hz for the short-period sensor and 0.0083 Hz for the broadband sensor.
Read the first row: at 0.01 Hz the geophone's response is $10^{-106/20}
= 5.0\times10^{-6}$ of its high-frequency value, while the broadband sensor is
still only 1.63 dB down. That factor of about $2\times10^{5}$ is the difference
between a sensor that can record a long-period surface wave and one that cannot.

## 4. Self-noise referred to the input, and why the corner is not the limit

A sensor's output is never clean. Referred to the input, the self-noise is

$$n_{\text{in}}(f) = \frac{n_{\text{out}}}{G\,|H(f)|},$$

with $n_{\text{out}}$ the output noise spectral density in $\mathrm{V/\sqrt{Hz}}$
and $G$ the generator constant in $\mathrm{V/(m/s)}$. Because $|H|$ falls as
$f^{2}$ below the corner, $n_{\text{in}}$ rises as $1/f^{2}$ there. The
demonstration's input-referred self-noise for the geophone
($n_{\text{out}} = 1.5\times10^{-7}\ \mathrm{V/\sqrt{Hz}}$,
$G = 200\ \mathrm{V/(m/s)}$) is

| $f$ (Hz) | 0.01 | 0.05 | 0.10 | 0.50 | 1.00 | 10.0 |
|---|---|---|---|---|---|---|
| $n_{\text{in}}$ (m/s/√Hz) | 1.519e−4 | 6.075e−6 | 1.519e−6 | 6.074e−8 | 1.519e−8 | 7.622e−10 |

Compare this with the demonstration's synthetic ambient ground-velocity model,
which has $2.236\times10^{-5}\ \mathrm{m/s/\sqrt{Hz}}$ at 0.01 Hz,
$4.101\times10^{-7}$ at 0.15 Hz, $5.958\times10^{-8}$ at 1 Hz and
$2.864\times10^{-8}$ at 10 Hz. The geophone's self-noise crosses the ambient model
at **0.2910 Hz**: above that frequency the sensor can see the site's noise, below
it the sensor sees only itself. The short-period and broadband sensors stay below
the ambient model everywhere in the 0.001–50 Hz band modelled here.

This gives the lesson's most important practical statement. A short-period
sensor's *specification* corner is not its *usable* limit; the usable limit is
where its input-referred self-noise meets the ambient noise. A geophone with a
4.5 Hz corner has a usable limit of 0.29 Hz at this site — eleven times below its
corner — and would have a *different* limit at a quieter site, because the
crossing moves. Conversely, at a noisy urban site almost any sensor is adequate
for low frequencies, for the reason that the site's own noise buries the
instrument's.

## 5. Clip level, gain and the amplitude window

The upper end is set by the digitizer range and the gain. For a full-scale range
of $\pm 10\ \mathrm{V}$ and a generator constant $G$, the largest ground velocity
that can be represented without clipping is

$$v_{\text{clip}} = \frac{V_{\text{FS}}}{G},$$

and the smallest resolvable change is set by the quantisation noise. With a
24-bit converter, the demonstration computes
$\text{LSB} = 2 \times 10/2^{24} = 1.1921\times10^{-6}\ \mathrm{V}$,
quantisation noise $= \text{LSB}/\sqrt{12} = 3.4413\times10^{-7}\ \mathrm{V}$ and
an ideal signal-to-noise ratio of $6.02 \times 24 + 1.76 = 146.24\ \mathrm{dB}$.

Assembling the sensor and the converter gives the window between clipping and the
sensor's own noise, expressed as ground velocity in a 1 Hz band:

| sensor | $v_{\text{clip}}$ (m/s) | noise at 1 Hz (m/s) | window (dB) |
|---|---|---|---|
| geophone 4.5 Hz | 0.0500 | 1.519e−8 | 130.35 |
| short-period 1 Hz | 0.0067 | 9.333e−12 | 177.08 |
| broadband 120 s | 0.0067 | 6.667e−12 | 180.00 |

Two features deserve comment. First, the window is far larger than the ~146 dB the
converter provides, because the *velocity* window is measured between two
quantities that the response scales differently; the converter's own quantisation
noise is a fixed voltage, and the sensor's noise is a voltage, so the honest
electronic comparison is voltage-to-voltage, not velocity-to-velocity. Second,
increasing $G$ lowers $v_{\text{clip}}$ by exactly the same factor as it lowers the
noise floor: **gain does not create dynamic range, it moves it.** The range
available is a property of the converter; the gain decides where in ground-motion
units that range sits.

## 6. Choosing a sensor

| Sensor | Typical band | Ground motion | Use it for |
|---|---|---|---|
| Geophone 4.5–10 Hz | ~4.5 Hz to hundreds of Hz | Moderate to strong | Active-source surveys, refraction, microzonation arrays |
| Short-period 1 Hz | ~1 Hz to tens of Hz | Moderate | Local and regional earthquakes, aftershock deployments |
| Broadband, 120 s corner | ~0.008 to 50 Hz | Weak to moderate | Teleseismic and ambient-noise studies, long-period signals |
| MEMS accelerometer | ~0.1 to 1000 Hz (in acceleration) | Strong motion | Dense strong-motion arrays, structural monitoring, low-cost networks |

The choice is made from the *target* band and the *expected* ground motion, not
from the sensor catalogue alone. A MEMS accelerometer converts to velocity by
dividing by $\omega$: at 0.01 Hz that division is a factor of
$1/(2\pi \times 0.01) = 15.9\ \mathrm{s}$, so an acceleration noise of
$10^{-4}\ \mathrm{m/s^{2}/\sqrt{Hz}}$ becomes an equivalent velocity noise of
$1.6\times10^{-3}\ \mathrm{m/s/\sqrt{Hz}}$ — five orders of magnitude above the
ambient model at that frequency. It is not a fault of the instrument; it is the
wrong instrument for that band.

## 7. Assumptions and regime of validity

1. **Single degree of freedom.** Real sensors have additional resonances,
   temperature-dependent springs and, in feedback designs, a control loop with its
   own dynamics. The model above is the leading term and is adequate for band
   planning, not for a response correction.
2. **Linear, time-invariant.** Large motions, a mass hitting its stops or a
   tilting frame all violate this. A clipped or tilted broadband sensor produces a
   long-period transient that is easily mistaken for signal.
3. **Magnitude only.** The demonstration prints $|H(f)|$; the transfer function is
   complex, and correcting a record requires the phase as well as the amplitude.
   Nothing here constrains phase.
4. **A constant generator constant.** $G$ is temperature-dependent and is one of
   the quantities a calibration is for.
5. **The ambient model is synthetic.** The crossover frequencies quoted are
   properties of the chosen model. At a real site the crossing must be computed
   from measured ambient noise, and it will differ.
6. **No coupling or installation term.** The ground under the sensor, the
   sensor's own base and the way it is levelled all enter the transfer function;
   at long periods these can dominate.

## 8. The honest summary

- A seismometer measures relative motion of a proof mass; every sensor is a
  band-pass device.
- Below the corner a velocity sensor rolls off as 12 dB/octave.
- The usable low-frequency limit is where input-referred self-noise meets ambient
  noise — 0.2910 Hz for the geophone in this model, not 4.5 Hz.
- Gain moves the dynamic range; it does not create it.
- Choose from the target band and the expected ground motion, and check the noise
  floor at *both* ends.

## 9. Python demonstration

[`code/seismometers_demo.py`](./code/seismometers_demo.py) prints every number
quoted above. It:

1. evaluates the response magnitude of three synthetic sensors in dB;
2. reports the −3 dB corner of each and the input-referred self-noise from
   0.01 Hz to 10 Hz;
3. evaluates a synthetic ambient ground-velocity model and finds the frequency at
   which each sensor's self-noise falls below it;
4. computes the clip velocity, quantisation noise and usable window for a
   $\pm10\ \mathrm{V}$, 24-bit digitizer.

Run it with the project virtual environment:

```bash
cd 23-field-methods-instruments/02-seismic-instruments-and-fieldwork/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python seismometers_demo.py
```

## 10. Exercises

Worked problem sets are in
[`exercises/01-seismometers-exercises.md`](./exercises/01-seismometers-exercises.md)
and
[`exercises/01-seismometers-solutions.md`](./exercises/01-seismometers-solutions.md).

## 11. Mastery checkpoint

Without notes:

1. A velocity sensor has $f_0 = 2\ \mathrm{Hz}$ and $h = 0.6$. Compute $|H|$ at
   0.5 Hz in absolute terms and in dB.
2. Compute its −3 dB frequency on the low-frequency flank.
3. Its output noise is $2\times10^{-7}\ \mathrm{V/\sqrt{Hz}}$ and
   $G = 100\ \mathrm{V/(m/s)}$. Compute the input-referred self-noise at 0.5 Hz,
   and the frequency at which it equals an ambient level of
   $1\times10^{-7}\ \mathrm{m/s/\sqrt{Hz}}$.
4. State in one sentence why doubling the gain does not double the usable
   dynamic range.

## 12. Common pitfalls

1. **Reading the corner as the usable limit.** For the geophone the two differ by
   a factor of 15.
2. **Assuming a quiet site is a good site for long periods.** At a noisy site the
   ambient noise hides the instrument's; at a quiet site the instrument's own
   noise becomes the limit.
3. **Correcting amplitude without phase.** Response correction is a
   deconvolution, and the phase matters as much as the amplitude.
4. **Installing a broadband sensor on soft, sloping or poorly coupled ground.**
   The installation term can exceed the instrument's specification at long
   periods.
5. **Buying sensitivity with gain and expecting range.** Gain relocates the
   window; the converter's bits set its width.
6. **Comparing sensors by their corners alone.** Two sensors with the same corner
   and different self-noise have different usable bands.

## 13. Where this is used

- Broadband observatory stations for teleseismic, surface-wave and ambient-noise
  work; the metadata that travels with the response is described in
  [03-10-03 StationXML Inventory, Response and Instrument Correction](../../03-scientific-computing/10-obspy-and-seismic-data/03-inventory-and-metadata.md).
- Temporary aftershock deployments with short-period sensors, where the band is
  matched to local magnitudes and the deployment is short.
- Active-source reflection and refraction surveys with geophones, where the
  target band is set by the source spectrum rather than by the Earth's noise.
- Dense arrays and strong-motion networks with MEMS accelerometers — see
  [23-02-07 Nodal Systems and Distributed Acoustic Sensing in the Field](07-das-and-nodal-systems.md).
- Instrument procurement and station design, where the numbers in Sections 4 and 5
  are the specification.

## 14. Related lessons

- [02 Digitizers, Dynamic Range, Gain and Anti-Alias Filtering](02-digitizers-and-gain.md) —
  the converter side of the window computed in Section 5.
- [03 Seismic Network Design and Station Siting](03-seismic-network-design.md) —
  how many sensors, and where.
- [05 Deployment, Orientation, Timing and Metadata](05-seismic-deployment.md) —
  what happens to the response when the sensor is installed in the ground.
- [06 Field QC: Noise Checks, Continuity, Station Uptime](06-seismic-field-qc.md) —
  the field tests that detect the failures listed in Section 12.
- [05-02-03 Noise, Drift, Tides and Instrument Bias in Field Data](../../05-core-geophysics/02-geophysical-fields-and-observables/03-noise-and-drift.md) —
  the noise taxonomy the ambient model stands for.

## 15. Self-assessment checklist

- [ ] I can write the equation of motion of an inertial sensor and its response.
- [ ] I can evaluate $|H(f)|$ and convert between absolute values and dB.
- [ ] I can compute input-referred self-noise and find a crossover frequency.
- [ ] I can compute a clip level and distinguish it from a noise floor.
- [ ] I can explain why gain relocates but does not widen a dynamic range.
- [ ] I can match a sensor family to a target band and ground-motion level.
