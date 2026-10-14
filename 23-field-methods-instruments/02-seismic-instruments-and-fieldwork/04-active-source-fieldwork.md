---
id: 23-02-04
title: "Active-Source Fieldwork: Sources, Spreads, Shooting Patterns"
level: graduate
prereqs: ["06-09-02", "23-02-01"]
estimated_minutes: 100
tags: [seismic, active-source, acquisition, fold, stacking, refraction]
---

# Active-Source Fieldwork: Sources, Spreads, Shooting Patterns

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** the midpoint fold of a split or off-end spread from the channel count, the receiver interval and the shot interval.
2. **Compute** the data volume a shooting pattern produces and **state** the taper at the ends of a line.
3. **Compute** the signal-to-noise gain of stacking $M$ traces, and **quantify**
   how much of it is lost when the noise is correlated between stacks.
4. **Price** fold: compute the cost per decibel of a denser shot interval.
5. **Derive** the crossover distance, the intercept time and the critical angle of a two-layer refraction model, and **invert** the intercept time for depth.
6. **Compute** the sensitivity of that depth to intercept-time and velocity errors, and **state** which dominates.
7. **Choose** a source and a shooting pattern for a stated target, and **state** the regulatory and environmental constraints that can override the choice.

All velocities, thicknesses, costs, fold values and correlation coefficients in
this lesson are **SYNTHETIC** teaching values printed by the demonstration. No
commercial rate, measured velocity or real survey geometry is used or reproduced.

## Prerequisites

- [06-09-02 Reflection Processing Flow: Deconvolution, NMO, Stack, Migration](../../06-seismology/09-reflection-seismology/02-processing-flow.md) —
  what the acquisition geometry has to support.
- [23-02-01 Seismometers: Broadband, Short-Period, Geophones, MEMS](01-seismometers.md) —
  the receivers at the other end of the spread.

## 1. Intuition: acquisition is a geometry problem

An active-source survey spends money to place sources and receivers in patterns.
Everything the processing can later do is bounded by those patterns: the fold
determines the noise rejection, the offsets determine which velocities are
resolvable, the spread length determines the maximum depth, and the source
determines the bandwidth. Processing cannot recover information the geometry never
recorded.

Three quantities are therefore computed before mobilisation, and all three are
cheap arithmetic:

- **fold** — how many traces contribute to each subsurface bin;
- **offsets** — the near and far limits of the source–receiver distances;
- **sources and receivers per unit length** — which sets the cost.

The fourth thing that must be decided is the **source**, and that decision is
often made by the regulator rather than by the geophysicist.

## 2. Sources

| Source | Mode | Typical use | Principal constraint |
|---|---|---|---|
| Sledgehammer on a plate | Impulsive | Very shallow, engineering | Small energy; poor deep penetration |
| Weight drop | Impulsive | Shallow reflection and refraction | Repeatability varies with ground |
| Explosive charge in a shot hole | Impulsive | Deep reflection and refraction | Licensing, storage, handling, landowner consent, safety |
| Airgun | Impulsive | Marine | Environmental regulation, vessel and permit |
| Sparker, boomer | Impulsive | Very shallow marine | Limited penetration |
| Vibrator (sweep) | Controlled, extended | Deep reflection on land | Vehicle access, surface damage, sweep correlation |

Two properties matter for processing. The **bandwidth** of the source sets the
resolvable resolution: a source that emits little below 20 Hz cannot image a deep
target no matter how long the spread is. The **repeatability** sets what stacking
can achieve: a source whose signature varies from shot to shot is a source whose
stacks do not reinforce coherently.

Explosive sources are subject to specific legal regimes covering procurement,
storage, transport, handling by qualified personnel, notification, and
site-specific restrictions, and they require the consent of the landholder. None of
that is negotiable by the survey design, and the permit timelines of
[23-01-04 Permits, Land Access, Cultural Heritage and Ethics](../01-field-safety-and-planning/04-permits-and-ethics.md)
apply in full.

## 3. Spreads, fold and data volume

For a spread of $n$ channels at receiver interval $\Delta x$ and a shot interval
$\Delta s$, the **midpoint fold** of a split spread is the standard relation

$$F = \frac{n\,\Delta x}{2\,\Delta s},$$

and for an off-end spread the same formula *without* the factor 2 applies when the
spread is not centred on the shot. Two properties of this number must be kept in
mind:

1. **It describes the middle of the line.** At both ends the fold ramps from $F$
   down to zero over about half the spread length, so the shallow edge of every line has lower fold and lower reliability. The taper is a geometric fact, not a processing choice.
2. **It is a midpoint statistic.** The *offset* distribution at a given midpoint is a separate matter; a high fold with a narrow offset range cannot be used for velocity analysis.

The demonstration computes both the fold and the data volume for a 48-channel,
25 m split spread over a 5 km line, with 2000 samples per trace at 4 bytes per
sample:

| $\Delta s$ (m) | shots | fold | traces | volume (MB) |
|---|---|---|---|---|
| 25 | 200 | 24.00 | 9600 | 76.8 |
| 50 | 100 | 12.00 | 4800 | 38.4 |
| 100 | 50 | 6.00 | 2400 | 19.2 |

The data volume is not a technicality. 76.8 MB sounds trivial until the campaign
has 20 lines and the processing involves repeated passes over the whole volume;
the planning number belongs in the plan.

## 4. Stacking gain, and what correlation removes

Stacking $M$ traces with uncorrelated noise multiplies the signal-to-noise
amplitude ratio by $\sqrt{M}$, which in decibels is $10\log_{10} M$:

| $M$ | 1 | 4 | 12 | 24 | 48 |
|---|---|---|---|---|---|
| $\sqrt{M}$ | 1.000 | 2.000 | 3.464 | 4.899 | 6.928 |
| gain (dB) | 0.00 | 3.01 | 5.40 | 6.90 | 8.41 |

Real noise is partially correlated between traces — a common microseism field, a
nearby road, a persistent source artefact. If the pairwise correlation of the
noise between stacks is $\rho$, the noise variance after averaging is

$$\operatorname{Var} = \frac{1 + (M-1)\rho}{M},$$

so the achieved gain is $(1/\sqrt{\operatorname{Var}})$ and the **effective**
number of independent stacks is $M_{\text{eff}} = 1/\operatorname{Var}$:

| $M$ | ideal gain | actual gain ($\rho = 0.05$) | $M_{\text{eff}}$ | loss (dB) |
|---|---|---|---|---|
| 4 | 2.000 | 1.865 | 3.48 | −0.61 |
| 12 | 3.464 | 2.782 | 7.74 | −1.90 |
| 24 | 4.899 | 3.341 | 11.16 | −3.32 |
| 48 | 6.928 | 3.785 | 14.33 | −5.25 |

A 5 % correlation costs 1.9 dB at 12 stacks, and beyond $M \approx 1/\rho$ extra
stacks buy almost nothing: the gain saturates at
$\sqrt{(1-\rho)/\rho} \approx 4.4$ (12.8 dB) as $M \to \infty$ for
$\rho = 0.05$. The design implication is that fold has a **ceiling set by the
noise correlation**, and that reducing the correlation (a better source, a
quieter time of day, careful editing) can be worth more than more shots.

## 5. The cost of fold

Fold is bought with shots. Halving the shot interval doubles the number of shots,
doubles the data volume, and — if the extra shots stack as independent traces —
buys $10\log_{10} 2 = 3.01\ \mathrm{dB}$ of stack. The demonstration's cost model
(250 currency units per shot position, 5 km line) gives

| $\Delta s$ (m) | shots | fold | cost (units) | cost/km | cost per dB over the 100 m case |
|---|---|---|---|---|---|
| 100 | 50 | 6.00 | 12 500 | 2500 | — |
| 50 | 100 | 12.00 | 25 000 | 5000 | 8305 |
| 25 | 200 | 24.00 | 50 000 | 10 000 | 12 457 |

Read the last column: the *first* 3 dB costs about 8300 units per dB of additional
gain, and the *second* about 12 500 — the cost per decibel is rising because the
gain is logarithmic and the cost is linear. This is the quantitative reason that
acquisition design trades fold against source strength and against careful noise
reduction rather than treating fold as a free quality knob.

## 6. Refraction geometry: a two-layer model

For a two-layer model with velocities $V_1 < V_2$ and interface depth $h$, the
head wave exists beyond the **critical angle** $\theta_c = \arcsin(V_1/V_2)$, and
its travel time is

$$t(x) = \frac{2h\cos\theta_c}{V_1} + \frac{x}{V_2}
= t_i + \frac{x}{V_2},$$

where the **intercept time** is

$$t_i = \frac{2h\sqrt{V_2^{2} - V_1^{2}}}{V_1 V_2}.$$

The **crossover distance**, where the head wave overtakes the direct wave, is

$$x_c = 2h\sqrt{\frac{V_2 + V_1}{V_2 - V_1}} .$$

With $V_1 = 600\ \mathrm{m/s}$, $V_2 = 2400\ \mathrm{m/s}$ and $h = 10\ \mathrm{m}$
the demonstration reports $\theta_c = 14.48^\circ$, $t_i = 0.032275\ \mathrm{s}
= 32.27\ \mathrm{ms}$ and $x_c = 25.82\ \mathrm{m}$. At a 100 m offset the head
wave arrives at 0.076093 s while the direct wave arrives at 0.166667 s — the
head wave is the first arrival, as it must be beyond the crossover.

Inverting the intercept time for depth,

$$h = \frac{t_i V_1 V_2}{2\sqrt{V_2^{2} - V_1^{2}}},$$

and its sensitivity follows by differentiation:

$$\frac{\partial h}{\partial t_i} = \frac{V_1 V_2}{2\sqrt{V_2^{2} - V_1^{2}}}
= 309.84\ \mathrm{m/s},$$

so a 1 ms intercept-time error costs 0.310 m of depth. The velocity sensitivities
are larger in effect and have opposite signs, because raising $V_1$ shrinks
$\sqrt{V_2^2-V_1^2}$ while raising the numerator:

$$\frac{\partial h}{\partial V_1}
= \frac{t_i V_2^{3}}{2\left(V_2^{2}-V_1^{2}\right)^{3/2}} > 0, \qquad
\frac{\partial h}{\partial V_2}
= -\frac{t_i V_1^{3}}{2\left(V_2^{2}-V_1^{2}\right)^{3/2}} < 0 .$$

The demonstration evaluates the depth at each perturbed velocity directly:

| Perturbation | depth change (m) |
|---|---|
| $t_i$ +1 ms | +0.310 |
| $t_i$ +5 ms | +1.549 |
| $V_1$ +2 % | +0.214 |
| $V_1$ +5 % | +0.536 |
| $V_1$ +10 % | +1.078 |
| $V_2$ +2 % | −0.013 |
| $V_2$ +5 % | −0.031 |
| $V_2$ +10 % | −0.057 |

At this velocity contrast, a 5 % error in $V_1$ moves the depth by 0.54 m while a
5 ms *picking* error moves it by 1.55 m: both matter, and the velocity error is
the one that no amount of careful picking removes. This is the quantitative
statement behind the standard practice of measuring $V_1$ directly — from an
uphole, a downhole, or the direct-wave branch of the same record.

## 7. Assumptions and regime of validity

1. **The fold formula assumes a continuous line of shots** and an idealised
   split spread. Real shooting may skip shot points, omit receivers, and re-shoot;
   the delivered fold must be *recomputed from the actual geometry*
   (see the field QC lesson, [06 Field QC: Noise Checks, Continuity, Station Uptime](06-seismic-field-qc.md)).
2. **The $\sqrt{M}$ law assumes uncorrelated noise** and Section 4 quantifies the
   correction. It also assumes the *signal* is coherent across the stacked traces,
   which fails where statics, NMO stretch or dip break the alignment.
3. **The refraction formulas assume a single horizontal interface** with constant
   velocities and an interface velocity higher than the overburden. A velocity
   inversion (a lower velocity below a higher one) produces no head wave and the
   model is unidentifiable from first arrivals alone.
4. **First arrivals are assumed picked on the true first break.** On noisy records
   the standard practice — and the practical bias — is to pick late, which biases
   $t_i$ and therefore the depth.
5. **The cost model is linear in shots.** Any component with a step (a second
   crew, a permit, a source-qualified specialist) breaks it and must be modelled
   separately.

## 8. The honest summary

- Fold is the plan number; the taper at the ends is a geometric fact.
- Stacking buys $\sqrt{M}$, and 5 % correlation removes 1.9 dB of the 5.4 dB
  available at 12 stacks.
- Fold has a ceiling set by noise correlation; reducing correlation beats buying
  more shots.
- The cost per decibel *rises* as fold increases.
- A two-layer refraction depth is more sensitive to the velocities than to the
  picks, at this contrast: a 5 % $V_1$ error costs 0.53 m and a 5 ms pick error
  1.55 m.
- The source choice is often a regulatory decision, not a geophysical one.

## 9. Python demonstration

[`code/active_source_fieldwork_demo.py`](./code/active_source_fieldwork_demo.py)
prints every number quoted above. It:

1. computes fold, shot count, trace count and data volume for three shot
   intervals;
2. tabulates the stacking gain for uncorrelated noise and the achieved gain,
   effective stack count and loss for a stated correlation;
3. prices three shot intervals and computes the cost per decibel;
4. computes the critical angle, intercept time, crossover distance and branch
   travel times of a two-layer model;
5. computes the depth sensitivity to a 1 ms and 5 ms intercept error and to 2 %,
   5 % and 10 % velocity errors.

Run it with the project virtual environment:

```bash
cd 23-field-methods-instruments/02-seismic-instruments-and-fieldwork/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python active_source_fieldwork_demo.py
```

## 10. Exercises

Worked problem sets are in
[`exercises/04-active-source-fieldwork-exercises.md`](./exercises/04-active-source-fieldwork-exercises.md)
and
[`exercises/04-active-source-fieldwork-solutions.md`](./exercises/04-active-source-fieldwork-solutions.md).

## 11. Mastery checkpoint

Without notes:

1. A split spread has 72 channels at 12.5 m. Compute the fold for shot intervals
   of 25 m and 50 m.
2. The same survey uses 500 shots of 144 traces, 3000 samples, 4 bytes per
   sample. Compute the data volume in MB.
3. Noise is correlated between stacks with $\rho = 0.02$. Compute the achieved
   gain, the effective stack count and the loss in dB at $M = 24$.
4. A two-layer model has $V_1 = 800\ \mathrm{m/s}$, $V_2 = 2800\ \mathrm{m/s}$,
   $h = 15\ \mathrm{m}$. Compute $t_i$, $x_c$ and the depth change produced by a
   1 ms intercept-time error.
5. State the one source-related constraint that can override a geophysical choice.

## 12. Common pitfalls

1. **Quoting the nominal fold.** The end taper and the missed shots are what the
   processor sees.
2. **Assuming the fold gain is free.** It costs shots, and the cost per dB rises.
3. **Ignoring noise correlation.** It caps the stack: beyond $M \approx 1/\rho$
   the gain saturates near 12.8 dB at $\rho = 0.05$.
4. **Confusing fold with offset distribution.** A high fold over a narrow offset
   range cannot resolve velocities.
5. **Picking first breaks late.** The bias goes straight into the intercept time
   and therefore into the depth.
6. **Treating the velocity as known.** At a 4:1 contrast, a 5 % $V_1$ error
   costs 0.53 m of depth; measure the near-surface velocity rather than assuming
   it.
7. **Designing the source before checking the permit.** Explosive and some marine
   sources are regulated, and the timeline is not negotiable.

## 13. Where this is used

- Reflection and refraction surveys for engineering, groundwater, mineral
  exploration and research imaging.
- Near-surface investigations where a two-layer refraction model is the entire
  interpretation — see the module
  [06-10 Refraction and Near-Surface Seismology](../../06-seismology/10-refraction-and-near-surface-seismology/README.md).
- Marine acquisition, where the same fold arithmetic applies with an airgun array
  and a towed streamer.
- Repeat (4-D) surveys, where source and geometry repeatability, not fold,
  determines what can be detected.
- Any survey where the acquisition geometry must be documented in the metadata of
  the resulting dataset.

## 14. Related lessons

- [01 Seismometers: Broadband, Short-Period, Geophones, MEMS](01-seismometers.md) —
  the receiver end of the spread and its band.
- [02 Digitizers, Dynamic Range, Gain and Anti-Alias Filtering](02-digitizers-and-gain.md) —
  the gain question that a strong near-offset source makes acute.
- [05 Deployment, Orientation, Timing and Metadata](05-seismic-deployment.md) —
  how the designed geometry is realised and recorded.
- [06 Field QC: Noise Checks, Continuity, Station Uptime](06-seismic-field-qc.md) —
  how the delivered geometry is verified.
- [05-05-02 Array Geometry, Fold, Offsets and Spatial Sampling](../../05-core-geophysics/05-survey-design-and-acquisition/02-geometry-and-coverage.md) —
  the survey-design side of this lesson.
- [23-01-04 Permits, Land Access, Cultural Heritage and Ethics](../01-field-safety-and-planning/04-permits-and-ethics.md) —
  the constraints the source choice must satisfy.

## 15. Self-assessment checklist

- [ ] I can compute a midpoint fold and a data volume from a shooting pattern.
- [ ] I can compute the stacking gain and correct it for noise correlation.
- [ ] I can compute a cost per decibel for fold.
- [ ] I can derive and invert the two-layer intercept-time relation.
- [ ] I can compute a depth sensitivity to picks and to velocities.
- [ ] I can state the regulatory constraint that can override a design choice.
