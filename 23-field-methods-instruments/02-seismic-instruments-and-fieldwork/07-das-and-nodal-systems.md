---
id: 23-02-07
title: "Nodal Systems and Distributed Acoustic Sensing in the Field"
level: research
prereqs: ["23-02-04", "06-13-04"]
estimated_minutes: 110
tags: [seismology, DAS, nodal, fibre-optic, acquisition, strain, arrays]
---

# Nodal Systems and Distributed Acoustic Sensing in the Field

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** the gauge-length response of a distributed acoustic sensing (DAS) channel and **locate** its notches.
2. **Compute** the channel spacing required to avoid spatial aliasing of the strain field, and **convert** between channel spacing and channel count per kilometre.
3. **Convert** between strain rate, particle velocity and acceleration for a plane wave, and **state** the frequency and velocity dependence of the conversion.
4. **Compute** a nodal deployment's battery margin under continuous and duty-cycled recording, and **state** what duty cycling costs.
5. **Compare** DAS strain sensitivity with a seismic ambient noise level, and **state** the frequency band in which a fibre can see ambient noise.
6. **Diagnose** a DAS or nodal dataset that has been aliased, notch-filtered or under-sampled, from its geometry and metadata.

All gauge lengths, channel spacings, velocities, battery lifetimes and strain
sensitivities in this lesson are **SYNTHETIC** teaching values printed by the
demonstration. No manufacturer specification, no measured fibre response and no
field figure is used or reproduced.

## Prerequisites

- [04 Active-Source Fieldwork: Sources, Spreads, Shooting Patterns](04-active-source-fieldwork.md) —
  the geometry and sampling arguments this lesson extends to continuous arrays.
- [06-13-04 Distributed Acoustic Sensing: A New Observational Regime](../../06-seismology/13-planetary-and-exploration-seismology/04-distributed-acoustic-sensing.md) —
  the method context.

## 1. Intuition: two ways to get many channels

A classical seismic survey places a discrete sensor at each point. Two modern
technologies change that arithmetic:

- **Nodal systems** remove the cable. Each node is an autonomous unit with its own
  sensor, digitizer, clock and battery, planted in the ground and harvested later.
  The channel count is limited by cost, labour and battery, not by cable length.
- **Distributed acoustic sensing** uses an optical fibre as the sensor: a
  interrogator sends pulses along the fibre and measures the phase of the light
  scattered back from each section. The fibre is not instrumented at points at
  all — it is *sampled* in sections whose length (the **gauge length**) is a
  processing choice, and the sampling interval (the **channel spacing**) is another.

Both change the sampling arguments of
[05-05-03 Spatial Sampling, Wavenumber Aliasing and Reconstruction](../../05-core-geophysics/05-survey-design-and-acquisition/03-spatial-sampling-theory.md)
from "how many sensors can we afford" to "how finely can we sample, and what does
the sampling device do to the signal".

DAS has three properties that make it qualitatively different from a seismometer
array:

1. **It measures strain (or strain rate), not displacement.** The conversion to ground motion involves frequency and the apparent velocity along the fibre.
2. **The gauge length is a filter.** Averaging strain over a length $L$ suppresses
   wavelengths comparable to $L$ and produces notches at $f = kv/L$.
3. **The fibre is one-dimensional.** Sensitivity is to the component of strain along the fibre axis, and a fibre in a conduit, a borehole or a trench has a geometry that must be known to interpret the data.

## 2. The gauge-length response

A DAS channel reports the average strain over its gauge length $L$. For a plane
wave of apparent velocity $v$ along the fibre, the response to a wavenumber $k$ is
the average of $e^{ikx}$ over the gauge,

$$H(k) = \frac{1}{L}\int_{-L/2}^{L/2} e^{ikx}\,\mathrm{d}x
= \operatorname{sinc}\!\left(\frac{kL}{2}\right)
= \frac{\sin(\pi f L/v)}{\pi f L / v},$$

which is zero whenever $f L/v$ is a non-zero integer. The notches are therefore at

$$f_{\text{notch}} = \frac{k v}{L}, \qquad k = 1, 2, 3, \dots$$

The demonstration's values for $v = 1500\ \mathrm{m/s}$:

| gauge (m) | first notch (Hz) | response at 50 Hz | response at 100 Hz |
|---|---|---|---|
| 1 | 1500.0 | 0.9982 | 0.9927 |
| 5 | 300.0 | 0.9549 | 0.8270 |
| 10 | 150.0 | 0.8270 | 0.4135 |
| 20 | 75.0 | 0.4135 | 0.2067 |

Two consequences. First, **choosing a gauge is choosing which frequencies you will
not see**: a 20 m gauge is blind at 75 Hz and attenuates 100 Hz by a factor of 5.
Second, **the gauge and the spacing are different decisions**: the gauge sets the
band-pass, the spacing sets the aliasing limit, and both must be chosen from the
target wavenumbers. A long gauge is attractive because it averages out
instrumental noise and gives a smoother record, and it is exactly that averaging
which removes the high wavenumbers.

## 3. Channel spacing and spatial aliasing

With channel spacing $\Delta x$ and apparent velocity $v$, the wavefield is
unaliased up to

$$f_{\text{alias}} = \frac{v}{2\Delta x},$$

and the channel count per kilometre is $1000/\Delta x$. The demonstration's table:

| $\Delta x$ (m) | $f_{\text{alias}}$ (Hz) | channels per km |
|---|---|---|
| 0.5 | 1500.0 | 2000 |
| 1.0 | 750.0 | 1000 |
| 2.0 | 375.0 | 500 |
| 5.0 | 150.0 | 200 |
| 10.0 | 75.0 | 100 |

Compare this with the gauge notches of Section 2, and a striking redundancy
appears: at $\Delta x = 1\ \mathrm{m}$ the data are unaliased to 750 Hz, while a
5 m gauge has already notched at 300 Hz. **The gauge, not the channel spacing,
usually sets the usable bandwidth**, and increasing the channel density beyond the
point where the gauge has already filtered the signal buys channels rather than
information. The reverse choice — a short gauge with coarse spacing — produces an
aliased record with a wide band.

The practical design rule: choose the gauge so that the notches lie above the
highest frequency of interest with margin, then choose the spacing so that
$v/(2\Delta x)$ also lies above it, and only then count channels and cost.

## 4. Converting between strain rate and ground motion

For a plane wave $u = A e^{i(kx-\omega t)}$ travelling along the fibre axis, the
derived quantities are

$$\text{strain} = kA, \qquad
\text{strain rate} = \omega k A, \qquad
\text{particle velocity} = \omega A, \qquad
\text{acceleration} = \omega^{2} A,$$

so that

$$\text{strain rate} = \frac{\omega^{2} A}{v} = \frac{\text{acceleration}}{v},
\qquad
\text{strain} = \frac{\text{velocity}}{v}.$$

Two features matter for interpretation. The strain-rate-to-acceleration conversion
is a **constant** factor $1/v$, independent of frequency — so DAS strain rate is
proportional to acceleration, and a DAS record can be compared with an
accelerometer by multiplying by $v$. The strain-to-velocity conversion, by
contrast, is also a constant $1/v$; the frequency dependence appears only when
comparing *different* wave types or when the apparent velocity along the fibre
differs from the material velocity.

The demonstration's table for a 1 nm/s particle velocity (the units are chosen):

| $f$ (Hz) | strain rate (1/s) | acceleration (m/s²) |
|---|---|---|
| 1.0 | 4.189e−12 | 6.283e−9 |
| 5.0 | 2.094e−11 | 3.142e−8 |
| 10.0 | 4.189e−11 | 6.283e−8 |
| 50.0 | 2.094e−10 | 3.142e−7 |

Note that a *fixed particle velocity* produces a strain rate that grows with
frequency: at high frequency the same ground motion is a much larger strain rate.
This is why a DAS record looks "blue" compared with a seismometer, and why
comparing spectra between a fibre and a seismometer without the conversion
produces an apparent frequency-dependent site effect that is an artefact of units.

## 5. Nodal deployments: batteries, duty cycles and labour

A node is an autonomous recorder, so its practical limits are the battery, the
storage and the harvest labour. The demonstration's example — 1000 nodes, a 20-day
survey, and a node that records continuously for 30 days on one battery set — gives
a continuous margin of

$$\frac{30}{20} = 1.50\times .$$

Recording can be duty-cycled to extend the margin:

| Duty cycle | battery lifetime (days) | margin | hours recorded per day |
|---|---|---|---|
| 24 on / 0 off | 30.0 | 1.50 | 24.0 |
| 12 on / 12 off | 60.0 | 3.00 | 12.0 |
| 6 on / 18 off | 120.0 | 6.00 | 6.0 |
| 4 on / 20 off | 180.0 | 9.00 | 4.0 |

The arithmetic of the trade is blunt: **duty cycling buys battery margin and
spends the record.** A 6 h/day schedule records a quarter of the time, so it misses
three quarters of any event not predicted in advance, and it cannot be used for
ambient-noise or long-period work at all. It is appropriate for a triggered
network waiting for a known source (a controlled source, a scheduled injection)
and inappropriate for earthquake monitoring.

The real constraints on a nodal survey are not the battery but the **labour and the
logistics of planting and harvesting**: a 1000-node spread planted at 25 m spacing
covers 25 km of line and requires a team-days budget for planting, testing,
harvesting, charging, downloading and re-testing that scales with the channel
count. That budget, not the instrument, is usually what sets the achievable channel
density.

## 6. What DAS can and cannot see

Using the demonstration's chosen sensitivity of 1 nanostrain (a single-sample
level) and $v = 1500\ \mathrm{m/s}$, the equivalent ground motion is

| $f$ (Hz) | equivalent velocity (m/s) | compared with a synthetic ambient model |
|---|---|---|
| 1.0 | 2.387e−7 | 4.01 × ambient |
| 5.0 | 4.775e−8 | 1.59 × ambient |
| 10.0 | 2.387e−8 | 0.83 × ambient |
| 50.0 | 4.775e−9 | 0.18 × ambient |

The equivalent acceleration is frequency-independent at $1.5\times10^{-6}\ \mathrm{m/s^{2}}$
because strain rate and acceleration differ by the constant factor $v$.

Read this table as a band statement. At 1 Hz this fibre's sensitivity is four times
*above* the ambient level, so it cannot resolve ambient noise there; at 10 Hz and
above it is below the ambient level, so the ambient field is measurable. The
crossover is set by the strain sensitivity and by $v$, and it moves with the
apparent velocity of the wave: a wave travelling at 3000 m/s along the fibre halves
the equivalent velocity for the same strain.

This is why DAS is described as a **high-frequency, high-density** instrument: it
provides thousands of channels (see Section 3) with a sensitivity that is
competitive above roughly a few hertz, and it is not a replacement for a broadband
seismometer at long periods. Its strengths are the channel density, the ability to
use existing fibre in a borehole or a pipeline, and the fact that the sensing
medium is already installed.

## 7. Assumptions and regime of validity

1. **A plane wave with a single apparent velocity.** Real wavefields contain multiple arrivals with different apparent velocities, and the gauge response then differs arrival by arrival; the notch of one arrival is not the notch of another.
2. **The fibre is straight and aligned with the wave path.** For a fibre with bends, or for a wave crossing the fibre at an angle, the effective apparent velocity
   along the fibre is $v/\cos\theta$ and the response changes; a fibre in a
   serpentine layout has a spatially varying response.
3. **Ideal sinc response.** Real interrogators have their own noise, a finite spatial resolution and, in some designs, a different weighting than a rectangular average. The measured response is the product of the instrument response and the gauge response.
4. **Perfect coupling to the ground.** A fibre in a loose conduit or a trench backfilled with soft material does not move with the ground, so the installation transfer function multiplies the response — the same problem as
   sensor coupling in [05 Deployment, Orientation, Timing and Metadata](05-seismic-deployment.md),
   with the same remedy: measure it.
5. **The nodal duty cycle and the storage are adequate.** A duty-cycled node
   cannot be used to search for unpredictable events, and a full disk is a gap
   exactly like a dead battery.
6. **The strain sensitivity is a single number.** Real DAS sensitivity varies with
   the interrogation, the fibre type and the distance along the fibre, so a
   campaign should measure it (for example by comparing with a co-located
   seismometer) rather than trusting a specification.

## 8. The honest summary

- The gauge length is a spatial filter: notches at $f = kv/L$ — 150 Hz for a 10 m
  gauge at 1500 m/s.
- The channel spacing sets the alias limit $v/(2\Delta x)$; 1 m gives 1000
  channels/km and 750 Hz.
- The gauge usually sets the usable band; extra channels beyond it buy channels,
  not information.
- Strain rate converts to acceleration by the constant factor $1/v$; the
  frequency dependence in DAS records is a units artefact, not a site effect.
- Duty cycling a nodal system buys battery margin and spends the record: 4 h/day
  records one sixth of the time.
- DAS is a high-frequency, high-density instrument; at this sensitivity it cannot
  resolve ambient noise at 1 Hz.

## 9. Python demonstration

[`code/das_and_nodal_demo.py`](./code/das_and_nodal_demo.py) prints every number
quoted above. It:

1. evaluates the gauge-length response for four gauges and reports the notches and
   the response at 50 and 100 Hz;
2. tabulates the alias frequency and the channel density for five channel spacings;
3. converts a 1 nm/s particle velocity into strain rate and acceleration across
   four frequencies;
4. computes battery lifetime, margin and recorded hours for four nodal duty cycles;
5. converts a 1 nanostrain sensitivity into equivalent ground velocity and
   acceleration and compares it with a synthetic ambient model.

Run it with the project virtual environment:

```bash
cd 23-field-methods-instruments/02-seismic-instruments-and-fieldwork/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python das_and_nodal_demo.py
```

## 10. Exercises

Worked problem sets are in
[`exercises/07-das-and-nodal-systems-exercises.md`](./exercises/07-das-and-nodal-systems-exercises.md)
and
[`exercises/07-das-and-nodal-systems-solutions.md`](./exercises/07-das-and-nodal-systems-solutions.md).

## 11. Mastery checkpoint

Without notes:

1. A 5 m gauge on a fibre with $v = 2000\ \mathrm{m/s}$: compute the first two
   notch frequencies.
2. A fibre is interrogated with a 2 m channel spacing and $v = 1500\ \mathrm{m/s}$:
   compute the alias frequency and the channel count per kilometre.
3. A wave has a particle velocity of 1 µm/s at 5 Hz and an apparent velocity along
   the fibre of 1200 m/s. Compute the strain, the strain rate and the
   acceleration.
4. A 2000-node survey lasts 15 days; a node records 40 days on a battery. Compute
   the continuous margin and the margin at a 6 h/day duty cycle, and state what the
   duty cycle costs.
5. State the band in which the lesson's fibre sensitivity is below the ambient
   model.

## 12. Common pitfalls

1. **Choosing the channel spacing first.** The gauge is usually the binding
   constraint on bandwidth.
2. **Reading a DAS spectrum as a ground-motion spectrum.** Strain rate is not
   velocity; the conversion involves $1/v$.
3. **Treating the fibre as uniformly sensitive.** Sensitivity varies with
   interrogation, fibre type and distance.
4. **Assuming perfect ground coupling for a trenched or conduit fibre.** The
   installation response multiplies the gauge response.
5. **Duty cycling a monitoring network.** It removes three quarters of the record.
6. **Comparing a DAS record with a seismometer without converting units.** The
   apparent frequency-dependent amplitude difference is an artefact.
7. **Forgetting the fibre geometry.** Bends change the apparent velocity and
   therefore the gauge response.

## 13. Where this is used

- Borehole and pipeline monitoring, where an existing fibre becomes a dense array
  without a deployment — see
  [06-13-04 Distributed Acoustic Sensing: A New Observational Regime](../../06-seismology/13-planetary-and-exploration-seismology/04-distributed-acoustic-sensing.md).
- Dense near-surface arrays for active-source acquisition, where nodal systems now
  provide channel counts that cabled systems cannot.
- Microzonation and engineering arrays, where the spatial sampling requirement
  dominates the design (Section 3).
- Induced-seismicity and microseismic monitoring in wells, where the fibre is
  already in place and the gauge and spacing are the design variables.
- Long-duration monitoring with nodes, where the battery and harvest budget, not
  the sensor, sets the channel count.

## 14. Related lessons

- [04 Active-Source Fieldwork: Sources, Spreads, Shooting Patterns](04-active-source-fieldwork.md) —
  fold, offsets and the geometry that both technologies extend.
- [01 Seismometers: Broadband, Short-Period, Geophones, MEMS](01-seismometers.md) —
  the point sensors that DAS and nodes are compared with.
- [05 Deployment, Orientation, Timing and Metadata](05-seismic-deployment.md) —
  the coupling and timing questions that DAS inherits.
- [06 Field QC: Noise Checks, Continuity, Station Uptime](06-seismic-field-qc.md) —
  how a nodal harvest is verified.
- [05-05-03 Spatial Sampling, Wavenumber Aliasing and Reconstruction](../../05-core-geophysics/05-survey-design-and-acquisition/03-spatial-sampling-theory.md) —
  the sampling theory behind Sections 2 and 3.

## 15. Self-assessment checklist

- [ ] I can compute gauge notches and explain what a gauge does to a wavefield.
- [ ] I can compute an alias frequency and a channel density.
- [ ] I can convert between strain rate, velocity and acceleration.
- [ ] I can compute a nodal battery margin under a duty cycle.
- [ ] I can state the band in which a DAS sensitivity can see ambient noise.
- [ ] I can diagnose an aliased or over-filtered fibre dataset from its geometry.
