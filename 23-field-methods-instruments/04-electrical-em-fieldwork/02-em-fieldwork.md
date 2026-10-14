---
id: 23-04-02
title: "EM Fieldwork: Loop, Coil and Grounded-Source Configurations"
level: graduate
prereqs: ["09-05-01", "23-04-01"]
estimated_minutes: 100
tags: [electromagnetics, fieldwork, frequency-domain, time-domain, coupling, skin-depth]
---

# EM Fieldwork: Loop, Coil and Grounded-Source Configurations

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** the electromagnetic skin depth, and **state** the resistivity and frequency ranges in which it is comparable to the survey scale.
2. **Compute** an induction number, and **decide** whether the low-induction-number approximation applies.
3. **Compute** the time-domain diffusion time to a stated depth and the recording
   window it implies.
4. **Compare** coil orientations by their depth of exploration, and **state** the
   convention behind the coefficient.
5. **Compute** the fall-off of cultural coupling with distance and the separation
   a stated suppression requires.
6. **Compute** the stacking gain and its cost in field time, and **state** when the
   gain stops.

All resistivities, spacings, times, orientation coefficients and noise levels in
this lesson are **SYNTHETIC** teaching values printed by the demonstration, or
derived from the definitions stated in the text. No field dataset, instrument
specification or commercial system is used or reproduced.

## Prerequisites

- [01 ERT Fieldwork: Electrode Layouts, Contact Resistance, Reciprocity](01-ert-fieldwork.md) —
  the galvanic configuration this lesson's grounded-source systems extend.
- [09-05-01 TEM Sounding for Aquifers and Mineral Targets](../../09-electrical-em-methods/05-em-methods-applications/01-tem-sounding.md) —
  what the soundings are used for.

## 1. Intuition: two ways to get current into the ground

An electrical method needs current in the ground. There are exactly two ways to
put it there:

- **Galvanically**, through electrodes in contact with the ground — the ERT family,
  and the **grounded-source** EM systems (a long wire or a pair of electrodes, with
  the magnetic field measured as well as the electric).
- **Inductively**, through a coil or a loop, using the ground as a secondary
  winding — the **frequency-domain** systems (a transmitter coil and a receiver
  coil at a fixed separation, or a large loop and a small coil) and the
  **time-domain** systems (a current in a loop switched off, with the decaying
  secondary field measured in time).

The inductive methods have no ground contact and therefore no contact resistance
problem, at the cost of a signal that falls off much faster with distance from the
transmitter and of a depth reach limited by diffusion. The design quantities are
the **skin depth**, the **induction number**, the **time** resolved in a TDEM
window, the **coil separation and orientation**, and the **coupling to culture**.

## 2. Skin depth and induction number

For a plane wave in a homogeneous conductor, the amplitude falls by $1/e$ over the
**skin depth**

$$\delta = \sqrt{\frac{2}{\omega \mu_0 \sigma}}
= \sqrt{\frac{2\rho}{\omega \mu_0}}
= 503.3\sqrt{\frac{\rho}{f}}\ \mathrm{m},$$

with $\rho$ in $\Omega\,\mathrm{m}$ and $f$ in Hz. The coefficient is not a
constant of nature: it is $\sqrt{2/(2\pi\mu_0)}$, and the demonstration prints it
for every row to make that clear. The values:

| $\rho$ (Ω·m) | $\delta$ at 10 Hz | at 100 Hz | at 1000 Hz |
|---|---|---|---|
| 10 | 503.29 m | 159.15 m | 50.33 m |
| 100 | 1591.55 m | 503.29 m | 159.15 m |
| 1000 | 5032.92 m | 1591.55 m | 503.29 m |

Read it as a design table. A 100 Ω·m ground at 100 Hz has a skin depth of 503 m —
so a small-loop system at that frequency sees a *very* large volume and cannot
resolve shallow structure; the same system at 10 000 Hz has
$\delta = 503.3\sqrt{100/10^4} = 50.3$ m, which is the scale of a shallow target.
The Maxwellian scale of the method is set by $\sqrt{\rho/f}$, and both the
frequency and the site resistivity must be known before a sounding can be planned.

The **induction number** compares the coil separation $s$ to the skin depth:

$$B = \frac{s}{\delta} .$$

For $B \ll 1$ the response is approximately proportional to conductivity (the
low-induction-number, LIN, regime), which is why small-loop EMI systems quote a
calibration in conductivity units. The demonstration evaluates $B$ for a 20 m
separation:

| $\rho$ (Ω·m) | 1 kHz | 10 kHz | 100 kHz |
|---|---|---|---|
| 10 | 0.397 | 1.257 | 3.974 |
| 100 | 0.126 | 0.397 | 1.257 |
| 1000 | 0.040 | 0.126 | 0.397 |

With a working threshold of $B < 0.3$, the LIN regime holds for the resistive
ground and the low frequencies, and fails for the conductive ground at high
frequency. **A conductivity map produced by a small-loop system outside its LIN
regime is not a conductivity map**: the response is non-linear in conductivity and
the "apparent conductivity" is a function of both the conductivity and the
geometry. The instrument's own linearity range must be established from its
geometry, not assumed from the presence of a conductivity display.

## 3. Time-domain: diffusion and the recording window

A TDEM system switches off the transmitter current and measures the decaying
secondary field. The current system diffuses downward, and the depth reached at
time $t$ is of order the diffusion depth

$$\delta_t = \sqrt{\frac{2t}{\mu_0 \sigma}},$$

so the time at which the diffusing system reaches a depth $d$ is

$$t \approx \frac{\mu_0 \sigma d^{2}}{2} .$$

The demonstration's table (with $\delta_t$ evaluated at that time, which returns
$d$ by construction):

| $\sigma$ (S/m) | $d = 50$ m | $d = 200$ m | $d = 500$ m |
|---|---|---|---|
| 0.01 | 0.0157 ms | 0.2513 ms | 1.5708 ms |
| 0.1 | 0.1571 ms | 2.5133 ms | 15.708 ms |
| 1.0 | 1.5708 ms | 25.13 ms | 157.08 ms |

The $d^{2}$ and $\sigma$ dependence is the whole design constraint. A 500 m target
in a 0.1 S/m ground needs a window of at least **16 ms**; the same target in a
1 S/m ground needs **157 ms**, and the late-time signal from a deep conductor is
both small and slow — which is why deep TDEM soundings require large transmitter
moments, long windows and very quiet sites. Two consequences for the field:

1. **The window must cover the target depth**, and the late-time channels should
   still be above the noise floor at the end of the window; if they are not, the
   sounding is depth-limited regardless of the transmitter.
2. **Cultural noise is worst at early times** (where the signal is largest) and
   instrumental noise at late times (where the signal is smallest). Recording
   enough stacks for the *late* channels, not the early ones, sets the acquisition
   time.

## 4. Coil orientation and depth of exploration

The depth of exploration of a small-loop system is conventionally of order
0.5–1.5 times the coil separation, with the coefficient depending on the
orientation (horizontal coplanar, vertical coplanar or perpendicular) and on the
target:

| Orientation | Coefficient (convention) | Depth at $s = 20$ m |
|---|---|---|
| horizontal coplanar | 1.5 | 30.0 m |
| vertical coplanar | 1.0 | 20.0 m |
| perpendicular | 0.5 | 10.0 m |

The coefficients are **conventions from the method's practice, not derived here**,
and they vary with the target and the ground; what is derived is the *scaling*: the
depth of exploration is proportional to the coil separation, so a system with a 40 m
separation reaches about twice as deep as one with 20 m, at the cost of a much
weaker signal and a loss of shallow resolution (the large separation averages over a
thicker volume and cannot resolve thin shallow layers). The choice is therefore a
target-depth decision, made before mobilisation.

## 5. Cultural coupling

A power line, a pipeline, a fence or a railway carries or perturbs currents that
induce a voltage in a receiver coil. For a long straight conductor the magnetic
field falls as $1/r$, and the voltage induced in a small loop by that field falls as
$1/r^{2}$ (one factor from the field, one from the area intercepted). The
demonstration states the consequence as a relative coupling:

| Distance $r$ (m) | Relative coupling | dB |
|---|---|---|
| 10 | 1.0000 | 0.0 |
| 20 | 0.2500 | −12.0 |
| 50 | 0.0400 | −28.0 |
| 100 | 0.0100 | −40.0 |
| 200 | 0.0025 | −52.0 |

The exponents are the point, not the level: **doubling the distance costs 12 dB**,
so a 40 dB suppression requires a factor of 100 in distance (10 m → 100 m) or a
different survey location. Practical measures, in the order that a field crew
should apply them:

1. **Increase the distance** from the source, and record the distance. This is the
   only measure that works reliably, and it is free.
2. **Orient the receiver** to minimise the coupling — for a line source, orienting
   the coil plane so that it intercepts the least flux; the reduction is
   orientation-dependent and geometrically calculable but is usually a factor of a
   few at best.
3. **Choose a different time** for the survey: many cultural sources have a
   daily rhythm (irrigation pumps, trains, industrial load), and a night survey can
   be much quieter.
4. **Increase stacking** (Section 6), which reduces the *random* part of the noise
   but not a coherent 50/60 Hz harmonic. A coherent interferer is not removed by
   stacking at all; it must be filtered (and only where the signal band permits) or
   avoided.

## 6. Stacking, and what it costs

Stacking $N$ measurements multiplies the signal-to-noise amplitude ratio by
$\sqrt{N}$, i.e. 3 dB per doubling, at a cost in field time proportional to $N$:

| Stacks | Gain $\sqrt{N}$ | dB | Time at 1 s per stack |
|---|---|---|---|
| 1 | 1.000 | 0.00 | 1 s |
| 4 | 2.000 | 6.02 | 4 s |
| 16 | 4.000 | 12.04 | 16 s |
| 64 | 8.000 | 18.06 | 64 s |
| 256 | 16.000 | 24.08 | 256 s |

Two bounds on this gain are worth stating because both are met in practice:

- **The noise must be uncorrelated between stacks.** A coherent interferer is not
  reduced at all; a slowly varying drift is reduced less than $\sqrt{N}$.
- **The signal must be stationary over the stacks.** In TDEM the late-time signal
  decays with time, so stacking across a window of fixed length is fine, but
  stacking *repeat soundings* taken minutes apart assumes the ground and the
  geometry are unchanged.

The practical rule: choose the number of stacks so that the *weakest* channel of
interest (usually the latest) is above the noise, and no more.

## 7. Assumptions and regime of validity

1. **Homogeneous half-space for the skin depth.** The formula is the uniform-earth
   result; in layered ground the effective depth differs, and the sounding is
   interpreted by forward modelling rather than by a skin-depth rule.
2. **Far-field / plane-wave conditions** for Section 2, which for a small-loop
   system at close range do not hold; the induction number is the check.
3. **A point dipole approximation** for the coil-pair geometry, valid when the
   separation is much larger than the coil radius. A large loop is not a dipole and
   its field falls more slowly near it.
4. **The diffusion-time formula is a scaling, not a solution.** It gives the order
   of the sensing time; the actual sensitivity distribution is computed by forward
   modelling.
5. **The orientation coefficients are conventions.** They must be quoted with the
   system and the target, not treated as physical constants.
6. **$1/r^{2}$ for a line source.** Real sources are neither infinite lines nor
   points, and nearby metallic conductors reradiate; the fall-off is a scaling
   argument for planning the survey's exclusion distances, not a prediction.

## 8. The honest summary

- $\delta = 503.3\sqrt{\rho/f}$ m; a 100 Ω·m ground at 100 Hz has a 503 m skin
  depth.
- The induction number $B = s/\delta$ decides whether a small-loop conductivity
  reading is linear: it exceeded 1 for the conductive ground at 10 kHz in this
  table.
- TDEM sensing time is $t \approx \mu_0\sigma d^{2}/2$: 16 ms for 500 m at
  0.1 S/m, 157 ms for the same depth at 1 S/m.
- Depth of exploration scales with coil separation; the coefficients are
  conventions.
- Cultural coupling falls as $1/r^{2}$: 12 dB per doubling of distance.
- Stacking gives 3 dB per doubling of time, and nothing at all against a coherent
  interferer.

## 9. Python demonstration

[`code/em_fieldwork_demo.py`](./code/em_fieldwork_demo.py) prints every number
quoted above. It:

1. tabulates the skin depth and its coefficient over three resistivities and three
   frequencies;
2. computes the induction number for a 20 m coil separation and marks where the LIN
   approximation fails;
3. tabulates the TDEM diffusion time for three conductivities and three depths;
4. converts three orientation conventions into depths of exploration at a 20 m
   separation;
5. tabulates the $1/r^{2}$ fall-off of cultural coupling to 200 m;
6. tabulates the stacking gain and its cost in time.

Run it with the project virtual environment:

```bash
cd 23-field-methods-instruments/04-electrical-em-fieldwork/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python em_fieldwork_demo.py
```

## 10. Exercises

Worked problem sets are in
[`exercises/02-em-fieldwork-exercises.md`](./exercises/02-em-fieldwork-exercises.md)
and
[`exercises/02-em-fieldwork-solutions.md`](./exercises/02-em-fieldwork-solutions.md).

## 11. Mastery checkpoint

Without notes:

1. Compute the skin depth at 5 kHz in a 30 Ω·m ground, and the frequency at which
   the skin depth is 25 m in that ground.
2. A coil pair has a 40 m separation. Compute the induction number at 3 kHz in a
   20 Ω·m ground and state whether the LIN approximation applies.
3. Compute the TDEM time at which the diffusion reaches 300 m in a 0.2 S/m ground,
   and state the window length required.
4. A power line is 15 m from a planned survey line and its coupling is 40 dB above
   the target signal. Compute the distance that would bring it within 10 dB of the
   target, and state one alternative to moving.
5. Compute the stacking time needed for a 20 dB gain, and state the condition under
   which it would not be achieved.

## 12. Common pitfalls

1. **Using a small-loop conductivity reading outside the LIN regime.** It is not a
   conductivity.
2. **Setting the TDEM window from the shallow target.** The late channels set the
   depth reach.
3. **Treating the depth-of-exploration coefficient as a physical constant.** It is
   a convention.
4. **Stacking against a coherent interferer.** It does not help.
5. **Planning the survey without the site resistivity.** $\delta$ depends on
   $\sqrt{\rho}$.
6. **Ignoring the transmitter–receiver geometry.** An incorrectly recorded
   separation changes every sounding's depth scale.
7. **Recording the late channels before the noise floor allows.** A noisy late
   channel is worse than no late channel, because it is inverted.

## 13. Where this is used

- Groundwater exploration and salinity mapping with TDEM and small-loop EMI.
- Mineral exploration with large-loop TDEM and airborne EM systems.
- Environmental and geotechnical work: landfill delineation, contaminant mapping,
  buried-metal detection.
- Permafrost and geothermal exploration, where the conductivity contrast is tied to
  temperature or ice content.
- Any survey near infrastructure, where the coupling distances of Section 5 decide
  the layout before any physics is involved.

## 14. Related lessons

- [01 ERT Fieldwork: Electrode Layouts, Contact Resistance, Reciprocity](01-ert-fieldwork.md) —
  the galvanic counterpart, and the source of the grounded-source configurations.
- [03 Magnetotelluric Fieldwork: Sites, Remote Reference, Noise](03-mt-fieldwork.md) —
  the natural-source end of the electromagnetic spectrum.
- [04 GPR Fieldwork: Antenna Choice, Grids, Coupling, Calibration](04-gpr-fieldwork.md) —
  the same diffusion physics at five orders of magnitude higher frequency.
- [09-07-01 EM Noise, Coupling and Cultural Effects](../../09-electrical-em-methods/07-em-data-processing-and-qc/01-em-noise-and-coupling.md) —
  the coupling problem in more depth.
- [08-05-01 Frequency-Domain EM (FDEM) Systems and Responses](../../08-geomagnetism-electromagnetism/05-controlled-source-em/01-frequency-domain-em.md) —
  the system modelling behind the LIN regime.

## 15. Self-assessment checklist

- [ ] I can compute a skin depth and use it to size a survey.
- [ ] I can compute an induction number and decide on the LIN regime.
- [ ] I can compute a TDEM diffusion time and a window length.
- [ ] I can compare coil orientations by depth of exploration.
- [ ] I can compute a coupling distance for a stated suppression.
- [ ] I can compute a stacking gain and its time cost.
