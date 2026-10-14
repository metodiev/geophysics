---
id: 08-02-02
title: "Proton Precession and Overhauser Magnetometers"
level: advanced
prereqs: ["08-02-01", "08-01-01", "20-05-01"]
tags: [geomagnetism, instruments, proton-precession, overhauser, larmor-frequency, signal-to-noise]
---

# Proton Precession and Overhauser Magnetometers

The proton magnetometer is the archetype of the scalar sensor: it measures the
**precession frequency** of nuclear spins in the ambient field, and a frequency
can be counted with extraordinary precision. Its weaknesses are all
consequences of the same physics — the signal decays, it must be rebuilt by
polarisation before each reading, and its amplitude is small. This lesson
develops the Larmor relation, the signal-to-noise arithmetic, and the two ways
the instrument is engineered: pulsed free precession, and continuously pumped
Overhauser operation.

**All models and data in this module are SYNTHETIC.** Relaxation times,
polarisation times, signal amplitudes, noise and duty cycles are chosen teaching
values. The standard constants used are the proton gyromagnetic ratio and
$\mu_0$. No instrument, manufacturer or published specification is described.

## Learning objectives

By the end of this lesson you will be able to:

1. **State** the Larmor relation and compute the precession frequency for a given
   field, and the field change for a given frequency change.
2. **Explain** how polarisation and free precession produce a scalar field
   measurement, and why the result is independent of sensor orientation.
3. **Compute** the signal-to-noise ratio of a decaying precession signal from its
   amplitude, decay constant and the noise level.
4. **Measure** the scaling of the frequency-estimation error with SNR and with
   counting time, and explain why the latter saturates.
5. **Compute** the duty cycle of a pulsed instrument and the number of readings
   per hour, and compare with continuously pumped operation.
6. **State** what makes an Overhauser sensor different from both a proton
   precession sensor and an optically pumped alkali sensor.

## Prerequisites

- [08-02-01 Fluxgate Magnetometers: Principle and Use](01-fluxgate-magnetometers.md) —
  the component alternative.
- [08-01-01 Describing the Main Field: Declination, Inclination, Intensity](../01-earth-magnetic-field/01-main-field-description.md)
  — the nT and the field magnitudes involved.
- [20-05-01 Stochastic Processes, Stationarity and Ergodicity](../../20-signal-processing/05-noise-and-random-signals/01-stochastic-processes.md)
  — the noise model behind the Monte Carlo of section 4.

## 1. Precession: the whole idea

A proton has a magnetic moment and an angular momentum; in a field $\mathbf{B}$
the two are coupled so that the moment **precesses** about the field at the
**Larmor frequency**

$$\omega_L = \gamma_p B, \qquad
f_L = \frac{\gamma_p}{2\pi}B, \qquad
\gamma_p = 2.6752218744\times10^{8}\ \mathrm{rad\,s^{-1}\,T^{-1}}.$$

Three properties do all the work:

- **The frequency is proportional to $|\mathbf{B}|$.** The measurement is a
  frequency ratio, which is the most accurately measurable quantity in physics.
- **The frequency does not depend on orientation.** The proton precesses about
  whatever direction the field has, so the sensor needs no levelling, no
  heading, and no calibration of alignment. This is the decisive practical
  advantage over a fluxgate.
- **Nothing in the relation can be adjusted.** $\gamma_p$ is a constant of
  nature, so the instrument's calibration is a frequency counter's calibration.

The scale is the surprise for those used to gyroscopes and fluxgates:
$\gamma_p/2\pi = 42.5775\ \mathrm{MHz\,T^{-1}} = 4.25775\times10^{7}\
\mathrm{Hz\,T^{-1}}$, which is

$$\frac{f_L}{B} = 42.5775\ \mathrm{Hz\,\mu T^{-1}}
= 0.042577\ \mathrm{Hz\,nT^{-1}}.$$

So a change of one nanotesla shifts the precession frequency by only
**42.6 mHz**. The demonstration's table makes the scale concrete:

| $B$ (nT) | $f_L$ (Hz) |
|---|---|
| 10000 | 425.7748 |
| 25000 | 1064.4370 |
| 50000 | 2128.8739 |
| 100000 | 4257.7479 |

A survey-resolution reading of 0.1 nT therefore requires a frequency resolution
of $4.2577\ \mathrm{mHz}$ — four thousandths of a hertz. That is the entire
engineering problem, and everything that follows is about what it costs.

## 2. Polarisation, free precession, and the signal

The equilibrium proton magnetisation in the geomagnetic field is minuscule
because the Zeeman splitting is far below $k_BT$. The instrument therefore
**polarises** the sample: a strong field (or radio-frequency pumping, section 6)
is applied for a few seconds to build up a net magnetisation, then switched off,
and the sample precesses freely in the ambient field. The recorded signal is

$$s(t) = a_0\,e^{-t/T_2^{*}}\sin(2\pi f_L t),$$

with $T_2^{*}$ the free-precession (dephasing) time. Two features matter:

- **The signal decays**, so the useful part of the record is the first few
  multiples of $T_2^{*}$. For the demonstration's synthetic $T_2^{*} = 2.0\
  \mathrm{s}$ and a $2.0\ \mathrm{s}$ acquisition, the amplitude has fallen to
  $e^{-1} = 0.368$ of its initial value by the end of the count.
- **The amplitude is proportional to the polarised magnetisation**, hence roughly
  to the polarising field and to the sample volume. Precision is bought with
  sensor size and with polarisation time, not with clever electronics alone.

**How the frequency is extracted.** The signal is a sinusoid in white noise, so
the optimal estimator is a **matched filter**: correlate the record with the
known envelope $\exp(-t/T_2^{*})$, and locate the peak in frequency. Implementing
it as a zero-padded Fourier transform of the envelope-weighted record gives a
finely sampled peak that can be interpolated below the bin spacing. That is what
the demonstration does, and it is also what a phase-locked counter does in
hardware.

## 3. What precision costs, measured

The demonstration runs a Monte Carlo (400 realisations per point) over a synthetic
signal with amplitude 1, varying the noise to set the SNR, with a
$2.0\ \mathrm{s}$ count at a $50000\ \mathrm{nT}$ field:

| SNR | $\sigma_f$ (Hz) | $\sigma_B$ (nT) |
|---|---|---|
| 1.0 | 0.00552604 | 0.129788 |
| 3.0 | 0.00178494 | 0.041922 |
| 10.0 | 0.00049898 | 0.011719 |
| 30.0 | 0.00017996 | 0.004227 |
| 100.0 | 0.00005598 | 0.001315 |

The log–log slope of $\sigma_f$ against SNR is **$-0.9971$**, i.e. the estimation
error is inversely proportional to the signal-to-noise ratio:

$$\sigma_f \propto \frac{1}{\mathrm{SNR}} \quad\Longrightarrow\quad
\sigma_B \propto \frac{1}{\mathrm{SNR}}.$$

There is no threshold and no cleverness: doubling the signal halves the field
error.

### 3.1 Counting longer: a diminishing return

Now fix SNR $= 10$ and vary the counting time:

| $T_{\text{acq}}$ (s) | $\sigma_f$ (Hz) | $\sigma_B$ (nT) | local log–log slope |
|---|---|---|---|
| 0.25 | 0.00686071 | 0.161135 | — |
| 0.50 | 0.00303727 | 0.071335 | $-1.18$ |
| 1.00 | 0.00113924 | 0.026757 | $-1.41$ |
| 2.00 | 0.00054739 | 0.012856 | $-1.06$ |
| 4.00 | 0.00030574 | 0.007181 | $-0.84$ |
| 8.00 | 0.00026686 | 0.006268 | $-0.20$ |

The error falls steeply at first — near the classical $T^{-3/2}$ of frequency
estimation from a finite record — and then **flattens**: once the count exceeds a
few times $T_2^{*}$, the tail of the record is noise, and the matched filter that
uses it admits that noise along with it. Counting for 8 s instead of 4 s buys
13% of precision, not the 2.8× that a pure $T^{-3/2}$ law would promise.

**The design conclusion** is that polarisation time — which raises $a_0$ — is a
better investment than acquisition time beyond a few $T_2^{*}$. This is exactly
why the pulsed instrument has a duty cycle in the first place.

## 4. Duty cycle, and why the Overhauser sensor exists

A pulsed instrument alternates between polarising and listening. With
$T_{\text{pol}} = 4.0\ \mathrm{s}$ and $T_{\text{acq}} = 2.0\ \mathrm{s}$,

$$\text{cycle} = 6.0\ \mathrm{s}, \qquad
\text{duty cycle} = \frac{2.0}{6.0} = 33.3\%,$$

and the demonstration counts

| overhead per reading (s) | readings per hour |
|---|---|
| 0.0 | 600.00 |
| 0.2 | 580.65 |
| 0.5 | 553.85 |

The cost of pulsed operation is therefore not only lost time: it is that the
instrument cannot observe continuously, so it cannot be used as a **variometer**
for diurnal monitoring, and it cannot track a fast-moving platform without gaps.

**Overhauser operation** removes the alternation. The sample is a free radical
dissolved in a solvent; radio-frequency pumping transfers polarisation from the
unpaired electron to the protons continuously, so the protons stay polarised
while they precess. The consequences are:

- **Duty cycle approaching 100%**, so each reading starts immediately and the
  instrument can be sampled continuously, at any rate the counter allows.
- **No dead time for polarisation**, so the reading rate is set by the desired
  precision rather than by the physics of a two-phase cycle.
- **A different noise-versus-rate trade**: because operation is continuous, the
  precision can be improved simply by observing longer, up to the instrument's
  stability limit.

An Overhauser sensor is *not* an optically pumped alkali sensor
([08-02-03](03-cesium-optically-pumped.md)): it polarises protons, so its
frequency is still set by $\gamma_p$ and its measurement is still a scalar field
reading. The difference is entirely in how the polarisation is maintained.

## 5. What the instrument is good for

| property | consequence |
|---|---|
| Scalar, orientation-independent | usable on unstable platforms and in boreholes; no heading calibration |
| Frequency output | resolution limited by the counter and by SNR, not by analogue linearity |
| Absolute | calibration is $\gamma_p$ and a clock; no field standard needed |
| Slow | its duty cycle and $T_2^{*}$ limit it to a reading every second or so for the pulsed version |
| $|\mathbf{B}|$ only | cannot separate a crustal anomaly from a diurnal change in the same direction |

The last row is the reason a scalar survey still needs a base station
([08-02-06](06-magnetic-survey-procedures.md)) and the second-to-last is the
reason an observatory uses a fluxgate for variation and a scalar for absolute
control.

## 6. Assumptions and regime of validity

1. **The polarising field is removed.** A residual polarising field, or a
   gradient across the sample, broadens the line and shortens $T_2^{*}$, which
   costs precision.
2. **The field is uniform over the sample volume.** A gradient across a large
   sensor dephases the precession; the apparent $T_2^{*}$ is then a property of
   the gradient, not of the fluid.
3. **The noise is white and independent.** The matched filter and the
   $1/\mathrm{SNR}$ scaling assume it; correlated noise (nearby machinery,
   power lines) breaks both.
4. **The frequency counter's reference is stable** over the measurement interval.
   The field resolution cannot be better than the clock's fractional stability
   times $|\mathbf{B}|$.
5. **The proton signal dominates.** In a mixed sample other nuclei with different
   $\gamma$ produce their own lines.
6. **Synthetic parameters.** The relaxation times, amplitudes and noise levels are
   teaching values; the relations are the content.

## 7. Python demonstration

`code/proton_precession_demo.py` prints, with units:

1. the Larmor relation, $\gamma_p/2\pi$ in Hz/T and Hz/nT, and the frequency at
   four fields;
2. free-precession decays at three amplitudes with their SNRs;
3. a Monte Carlo of the frequency-estimation scatter versus SNR;
4. the measured log–log slopes against SNR and against counting time, including
   the saturation of the time gain;
5. the duty cycle of a pulsed sensor and readings per hour for three overheads;
6. the cost of a 0.1 nT target in SNR and in seconds.

Exercises and solutions:
[`exercises/02-proton-overhauser-exercises.md`](./exercises/02-proton-overhauser-exercises.md),
[`exercises/02-proton-overhauser-solutions.md`](./exercises/02-proton-overhauser-solutions.md).

## Mastery checkpoint

1. Compute the precession frequency at $B = 45000\ \mathrm{nT}$.
2. A counter resolves $1\ \mathrm{mHz}$. Compute the corresponding field
   resolution in nT.
3. The measured $\sigma_B$ is 0.1298 nT at SNR $= 1$. What SNR is needed for
   0.01 nT at the same counting time?
4. Explain in two sentences why counting longer eventually stops helping.
5. Compute the duty cycle and readings per hour for $T_{\text{pol}} = 5\
   \mathrm{s}$, $T_{\text{acq}} = 1\ \mathrm{s}$ and 0.3 s of overhead.
6. State the single physical difference between an Overhauser sensor and a
   pulsed proton sensor.

## Common pitfalls

1. **Confusing Hz/T with Hz/nT.** The difference is $10^{9}$; the proton
   constant is 42.5775 Hz per **microtesla**.
2. **Quoting a resolution without an SNR and a counting time.** All three numbers
   are one statement.
3. **Assuming averaging is free.** Beyond a few $T_2^{*}$ the record is noise.
4. **Treating a gradient across the sensor as sensor noise.** It changes $T_2^{*}$
   and is systematic.
5. **Expecting Overhauser operation to need no calibration.** Its frequency is
   still $\gamma_p B$; the calibration and the clock matter exactly as before.

## Related modules

- [08-02-01 Fluxgate Magnetometers: Principle and Use](01-fluxgate-magnetometers.md) —
  components and their orientation problem.
- [08-02-03 Optically Pumped Cesium and Potassium Magnetometers](03-cesium-optically-pumped.md) —
  a different route to a high-resolution scalar.
- [08-02-06 Magnetic Survey Design, Diurnal Correction and Levelling](06-magnetic-survey-procedures.md) —
  what the readings are used for.
- [20-05-01 Stochastic Processes, Stationarity and Ergodicity](../../20-signal-processing/05-noise-and-random-signals/01-stochastic-processes.md) —
  the noise model.

## Self-assessment checklist

- [ ] I can state and use the Larmor relation with correct units.
- [ ] I can explain what the sensor actually measures.
- [ ] I can compute an SNR and the resulting field precision.
- [ ] I can state why the counting-time gain saturates.
- [ ] I can compute duty cycle and reading rate.
- [ ] I can distinguish a proton, an Overhauser and an alkali sensor.
