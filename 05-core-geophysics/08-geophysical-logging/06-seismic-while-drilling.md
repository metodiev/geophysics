---
id: 05-08-06
title: "Vertical Seismic Profiling and Check Shots"
level: graduate
prereqs: ["05-08-04", "05-07-04", "02-04-05"]
tags: [vsp, check-shot, well-tie, velocity, corridor-stack, time-depth]
---

# Vertical Seismic Profiling and Check Shots

## Learning objectives

By the end of this lesson you will be able to:

1. **Distinguish** a check shot, a VSP and a surface seismic survey by what each
   measures and what each calibrates.
2. **Compute** a time–depth curve from a layered velocity model and recover
   interval velocities by differencing check-shot times, including the precision
   argument that sets the receiver spacing.
3. **Quantify** the depth error produced by a wrong average velocity, and state
   why it is the dominant error in a well tie.
4. **Explain** the VSP geometry — downgoing and upgoing wavefields, the direct
   arrival, and why the offset source makes the raypath non-vertical.
5. **Use** a corridor stack and a VSP-derived velocity to tie a seismic section, and
   state what the tie does and does not calibrate.
6. **Recognise** when a tie discrepancy is a velocity error, a polarity error, a
   datum error, or a real geological difference.

## Prerequisites

- [05-08-04 Density, Neutron and Sonic Porosity Logs](./04-porosity-logs.md)
  — the sonic log whose integral *is* the time–depth curve.
- [05-07-04 Ground Truthing: Boreholes, Outcrop and Drill Core](../07-interpretation-and-integration/04-ground-truthing.md)
  — the tie as a validation experiment, with its scale limits.
- [02-04-05 Elastodynamics: The Equation of Motion and Wave Speeds](../../02-physics/04-elasticity-and-continuum-mechanics/05-elastodynamics.md)
  — the wave-speed relations behind the velocities used here.

## 1. Intuition: three different measurements, three different uses

- A **check shot** is a sparse set of seismic-source-to-receiver travel times, at a
  handful of depths, used to build or check a **time–depth relationship**.
- A **VSP** records the full wavefield at many receiver depths, so it separates
  **downgoing** from **upgoing** arrivals. The upgoing field is a *direct*
  measurement of what the surface seismic will see at that location, one-way
  already deconvolved of the surface-consistent effects.
- **Surface seismic** images the subsurface from above, with a resolution set by
  the surface geometry and a depth scale that requires a velocity model to convert
  times to depths.

The crucial asymmetry: **surface seismic measures time, and depth is an
interpretation; a well measures depth, and time is an interpretation.** The tie is
the reconciliation of those two, and it is where the largest single error in
exploration seismology — velocity-to-depth conversion — is either removed or made
invisible.

The tie also does something subtler than depth conversion: it *validates the
wavelet, the phase and the multiples*. A VSP's upgoing field can be stacked along a
corridor around the direct arrival to give a **corridor stack**, a synthetic
seismic trace at the well that carries the real wavelet and the real multiples.
Comparing it with the surface seismic section is a far stronger test than comparing
a synthetic seismogram computed from the sonic and density logs, because it
contains the actual propagation.

## 2. Precise definitions

### 2.1 Time–depth relationship

A function $t(z)$ giving one-way or two-way time at depth $z$, obtained from
check shots, the sonic log, or a VSP. It is required for every depth conversion,
and its accuracy is the accuracy of the depth scale.

### 2.2 Interval and average velocity

$$v_{\text{int}} = \frac{\Delta z}{\Delta t}, \qquad
v_{\text{avg}} = \frac{z}{t(z)}, \qquad
v_{\text{rms}}^2 = \frac{\sum v_i^2 \Delta t_i}{\sum \Delta t_i}. \tag{1}$$

The three are different numbers for the same interval, and confusing them is a
standard source of tie error. Depth conversion with $v_{\text{avg}}$ is correct
only if $v_{\text{avg}}$ is the average over the path.

### 2.3 Direct arrival

The first arrival at a receiver, along the straightest available path from the
source. With a source offset from the well, this path is not vertical (Section 3.4).

### 2.4 Corridor stack

A stack of upgoing VSP energy in a time window ("corridor") around the direct
arrival, migrated and stacked to give a single trace comparable with surface
seismic.

## 3. Derivations

### 3.1 The time–depth integral

For a layered model with constant velocity $v_i$ between depths,

$$t(z) = \sum_{i} \frac{\Delta z_i}{v_i}
\qquad\text{(one-way)}, \tag{2}$$

which is the same integral as the sonic-log identity of
[05-08-04 §3.4](./04-porosity-logs.md), with velocity instead of slowness. The
demonstration's SYNTHETIC model:

| Layer (m) | $V_p$ (m s⁻¹) | one-way time at base (s) |
|---|---|---|
| 0–400 | 1800 | 0.2222 |
| 400–900 | 2400 | 0.4306 |
| 900–1500 | 3100 | 0.6241 |
| 1500–3000 | 4200 | 0.9812 |

### 3.2 Interval velocity from check shots, and the precision it sets

Differencing gives the interval velocities (measured):

| Depth (m) | One-way time (s) | Interval velocity (m s⁻¹) |
|---|---|---|
| 250 | 0.1389 | — |
| 500 | 0.2639 | 2000.0 |
| 1000 | 0.4628 | 2638.3 |
| 1500 | 0.6241 | 3100.0 |
| 2000 | 0.7432 | 4200.0 |
| 3000 | 0.9812 | 4200.0 |

Note that the *interval* velocity is a difference of two times divided by a
spacing. A timing error $\delta t$ over a spacing $\Delta z$ gives

$$\delta v_{\text{int}} = \frac{\Delta z}{(\Delta t)^2}\delta t
= \frac{v^2}{\Delta z}\delta t , \tag{3}$$

so with $\delta t = 1$ ms and 250 m spacing, $\delta v = 16$ m s⁻¹ at
2400 m s⁻¹ — 0.7 per cent. **State the spacing whenever you quote an interval
velocity**, because the same 1 ms timing precision gives four times the velocity
error at half the spacing.

### 3.3 The depth error from a wrong average velocity

With $z = v_{\text{avg}} t$ and $t$ measured,

$$\frac{\delta z}{z} = \frac{\delta v_{\text{avg}}}{v_{\text{avg}}}. \tag{4}$$

Measured at $z = 2000$ m, where $t = 0.7432$ s and $v_{\text{avg}} = 2691.2$ m s⁻¹:

| Assumed $v_{\text{avg}}$ | Depth error | Error |
|---|---|---|
| 2556.7 | $-100.0$ m | $-5.00$ % |
| 2637.4 | $-40.0$ m | $-2.00$ % |
| 2691.2 | $0.0$ m | $0.00$ % |
| 2825.8 | $+100.0$ m | $+5.00$ % |

A 5 per cent velocity error is 100 m at 2 km, and it is a *systematic* shift, not
scatter: every reflector moves together, the section still ties to itself, and
nothing in the seismic reveals the error. This is precisely the situation in which
a check shot is not optional.

### 3.4 VSP geometry, and why the offset matters

For a source at horizontal offset $X$ and a receiver at depth $z$, the ray path is
inclined; its length exceeds $z$, so the direct arrival is later than the
normal-incidence time. With a straight-ray approximation (stated as an
approximation, not a ray trace) through the layered model, the measured differences
for $X = 1200$ m are:

| Receiver depth (m) | direct arrival (s) | normal incidence (s) | difference (ms) |
|---|---|---|---|
| 250 | 0.6810 | 0.1389 | 542.09 |
| 1000 | 0.7230 | 0.4628 | 260.14 |
| 1750 | 0.8289 | 0.6836 | 145.31 |
| 2500 | 0.9564 | 0.8622 | 94.20 |

The offset both delays the direct arrival and gives the upgoing field a *lateral*
reference point: the reflection measured at the receiver comes from a point on the
reflector between source and receiver. That is why a VSP carries geometrical
information a check shot cannot. It is also why a VSP needs its own geometry
model — the arrivals cannot be interpreted as if the source were at the wellhead.

## 4. Worked examples

### 4.1 Building a tie

**Procedure.**

1. Run the check shot or VSP; obtain $t(z)$.
2. Compare with the sonic-log integral: the difference is the *drift*, and it
   should be smooth and small. A step change means a log interval is wrong; a
   growing drift means a systematic slowness bias.
3. Adjust the velocity model to fit the check shots exactly (integrated time must
   equal the measured time), not to "look right".
4. Build the corridor stack and compare it with the surface section: match
   *phase* and *polarity*, not just reflection positions.
5. Convert depth to time with the calibrated model, and report the residual
   misfit and the depth uncertainty it implies.

**Falsification.** If the corridor stack cannot be made to match the surface
section in wavelet character after the velocity correction, then something other
than velocity is wrong — often a polarity or a datum, sometimes a real 3-D effect
where a 1-D tie does not apply.

### 4.2 Diagnosing a discrepancy

| Symptom | Likely cause |
|---|---|
| Uniform depth shift, all reflectors | Datum or velocity reference error |
| Drift increasing with depth | Velocity model (or a slowness bias) |
| Step shift at one horizon | Mis-tie, log interval, or a real fault cut |
| Reflections reversed | Polarity convention (SEG normal vs reverse) |
| Character mismatch, positions right | Wavelet phase, attenuation, or multiples not modelled |
| Positions right in one well, wrong in the next | 3-D structure; a 1-D tie is an approximation |

### 4.3 What the tie does and does not prove

A successful tie proves that the well's time–depth relationship is consistent with
the seismic at that location, and that the wavelet and polarity are consistent. It
does **not** prove that an amplitude anomaly away from the well is a fluid effect,
nor that a structural interpretation between wells is correct. It calibrates the
*scale*, not the *geology*. Keeping that distinction is the same discipline as
[05-07-04 §2.1](../07-interpretation-and-integration/04-ground-truthing.md): the
well tests what the model predicted for it, and nothing else.

## 5. Assumptions

1. **A one-dimensional (layered) Earth** for the tie. Dip, lateral velocity
   variation and anisotropy all violate it.
2. **Straight-ray or a stated ray-tracing approximation** where a direct-arrival
   path is computed. The demonstration's §3.4 numbers are straight-ray.
3. **Correct polarity convention** throughout the processing chain.
4. **A consistent datum** for the logs, the check shots and the seismic.
5. **Isotropic velocities** unless an anisotropic model is stated; shale anisotropy
   of several per cent is the rule, not the exception, and a purely vertical tie
   cannot measure it.
6. **The sonic log's integrated time is unbiased**, which fails over washed-out or
   missing intervals (the 0.066 ms per lost metre of
   [05-08-04 §3.4](./04-porosity-logs.md)).
7. **The source and receiver are in the positions the geometry model assumes.**
   A check shot's source offset, the receiver depths and the hole deviation all
   enter the time-depth relationship, and an error in any of them appears as a
   velocity error. This is why the deviation survey and the source position are
   part of the check-shot deliverable, not separate data.

Two of these assumptions deserve emphasis because they are the ones that survive
into a final report unexamined. The **one-dimensional assumption** means that a tie
calibrated in one well is a statement about the Earth along a vertical line through
that well, and using it to depth-convert a 3-D seismic volume assumes lateral
invariance that the tie cannot test. The **isotropy assumption** means that any
anisotropy in the overburden — typically several per cent in shales — is absorbed
into the fitted velocities, so a vertical tie cannot detect it and a
non-vertical (walkaway or offset) VSP is required to measure it. Both statements
belong in the uncertainty section of a depth-converted interpretation.

## 6. Units and dimensional analysis

- Depth in m, time in s; seismic sections are often in ms and logs in m, and
  $2\Delta z/v$ mixes the two if the factor of $10^{-3}$ is forgotten.
- Velocity m s⁻¹; slowness µs m⁻¹; the reciprocal relation is
  $\Delta t[\mathrm{\mu s\,m^{-1}}] = 10^{6}/v[\mathrm{m\,s^{-1}}]$. A 2000 m s⁻¹
  layer has a 500 µs m⁻¹ slowness — worth memorising as a sanity anchor.
- Equation (3): m² s⁻¹ / m × s = m s⁻¹ ✓.
- Equation (4) is dimensionless; the same fractional error appears in depth.
- Offset in m, and the total raypath length in m; a VSP with offset 1200 m at
  250 m depth has a path 4.9 times the vertical distance, which is why the direct
  arrival is 0.54 s later.

## 7. Python demonstration

`code/vsp_demo.py` builds the time–depth curve, differences check-shot times, and
computes the tie errors and the VSP geometry.

```python
def vertical_time(z):
    t = 0.0
    for top, base, v in VELOCITIES:
        if z <= top: break
        t += (min(z, base) - top) / v
        if z <= base: break
    return t
```

Measured output, abridged:

```
layer (m)        Vp (m/s)   one-way vertical time at base (s)
     0-   400       1800                         0.2222
   400-   900       2400                         0.4306
   900-  1500       3100                         0.6241
  1500-  3000       4200                         0.9812

depth (m)   check-shot one-way time (s)   interval V from successive shots
      500                         0.2639                       2000.0
     1000                         0.4628                       2638.3
     2000                         0.7432                       4200.0

at z = 2000 m: one-way time 0.7432 s, average velocity 2691.2 m/s
assumed V_avg     depth error (m)   error (per cent)
      2556.7            -100.0             -5.00
      2825.8            +100.0             +5.00

receiver depth (m)   direct-arrival (s)   normal-incidence (s)   difference (ms)
              250               0.6810                 0.1389             542.09
             2500               0.9564                 0.8622              94.20
```

### What to observe, and why it matters

| Observation | Consequence |
|---|---|
| The exact time–depth integral matches the layer model | The tie machinery is verified before use |
| Interval velocities are differences, and 1 ms over 250 m is 0.7 per cent | Quote the spacing with every interval velocity |
| A 5 per cent velocity error is 100 m at 2 km, systematically | The tie is not optional, and the error is invisible without it |
| The offset makes the direct arrival 542 ms later at 250 m | VSP geometry must be modelled; there is no vertical incidence |
| The difference falls to 94 ms at 2500 m | The raypath becomes closer to vertical with depth |

> **Breaking exercise.** Change the source offset to 3000 m and re-run Section 4.
> Predict which rows change most and why, then check. Then state the practical
> consequence for VSP survey design when the target is shallow.

## 8. Exercises

[`exercises/06-seismic-while-drilling-exercises.md`](./exercises/06-seismic-while-drilling-exercises.md)
and
[`exercises/06-seismic-while-drilling-solutions.md`](./exercises/06-seismic-while-drilling-solutions.md).

### ★ Foundational

**★1.** Distinguish a check shot, a VSP and a surface seismic survey by what each
physically measures.

**★2.** Convert 2500 m s⁻¹ to slowness in µs m⁻¹ and compute the two-way time over
a 1 km interval at that velocity.

**★3.** State the difference between $v_{\text{int}}$, $v_{\text{avg}}$ and
$v_{\text{rms}}$ and which one a depth conversion requires.

### ★★ Applied

**★★4.** Run `code/vsp_demo.py` and report the interval velocities for 250 m
receiver spacing and for 100 m spacing. Explain the difference in precision using
equation (3).

**★★5.** A tie shows a smooth drift of $+8$ ms at 2500 m relative to the
check-shot time. Compute the implied average-velocity error and the depth shift it
causes.

**★★6.** For the demonstration's model, compute the two-way time to 2000 m and
state the depth at which the two-way time is exactly 1.500 s.

### ★★★ Research-oriented

**★★★7.** Implement a ray-traced (bending) direct-arrival time for the
demonstration's model at three offsets and compare with the straight-ray times.
Report the offset at which the straight-ray approximation exceeds 1 ms error, and
state what that means for shallow-target VSP design.

**★★★8.** Build a synthetic VSP: generate downgoing and upgoing arrivals for a
reflectivity model, add a corridor stack, and compare it with a surface-seismic
convolutional model. Report the residual after the tie and identify which
assumption dominates the residual.

## 9. Common mistakes

1. **Depth-converting with the wrong velocity type.** Section 2.2.
2. **Quoting an interval velocity without the receiver spacing.**
3. **Assuming vertical incidence in a VSP.** Section 3.4 measures 542 ms at 250 m.
4. **Ignoring polarity conventions** and then "correcting" a tie by shifting
   depths.
5. **Using a 1-D tie where the structure is 3-D**, and attributing the residual to
   velocity.
6. **Believing a tie validates a fluid or structural interpretation elsewhere.**
   It calibrates the scale, not the geology.
7. **Forgetting that the sonic log's integral has its own error** over washed-out
   intervals.

## 10. Real-world applications

- **Every exploration well.** The tie is the bridge between well data and seismic
  interpretation, and the depth scale of every map depends on it.
- **Reservoir modelling.** Time-to-depth conversion for the static model, with the
  tie's uncertainty carried into the depth uncertainty of the surfaces.
- **Amplitude and AVO work.** The corridor stack is the reference for calibrating
  amplitudes and the wavelet
  ([05-04-03 Gassmann Fluid Substitution and Saturation Effects](../04-rock-physics/03-gassmann-fluid-substitution.md)
  for the rock-physics side).
- **Geothermal and mineral drilling.** Velocity calibration for structural targets
  where a 100 m depth error is a missed well.
- **Scientific drilling.** Where the check shot is the primary calibration for
  downhole seismic and for the surface seismic tie.

## 11. Further reading

- **Hardage, B. A. (2000). *Vertical Seismic Profiling: Principles* (3rd ed.).
  Pergamon.** Level: advanced. The standard reference on VSP geometry, upgoing and
  downgoing fields and corridor stacks.
- **Sheriff, R. E. & Geldart, L. P. (1995). *Exploration Seismology* (2nd ed.).
  Cambridge University Press.** Chapters 4–6. Level: intermediate. Velocity
  concepts and time–depth conversion.
- **Yilmaz, Ö. (2001). *Seismic Data Analysis*. SEG.** Chapters on velocity
  analysis and depth conversion. Level: advanced. The processing-side account.
- **Stewart, R. R., Gaiser, J. E., Brown, R. J. & Lawton, D. C. (2002). Converted-
  wave seismic exploration: Applications. *Geophysics*, 67(1), 40–57.** Level:
  advanced. Where the tie must handle more than one wave mode.
- **Ellis, D. V. & Singer, J. M. (2007). *Well Logging for Earth Scientists*
  (2nd ed.). Springer.** Chapter 17. Level: intermediate to advanced. The
  borehole-seismic tools and their acquisition.

> Note on citations: bibliographic details are given so you can locate the works.
> This repository does not host or reproduce copyrighted text.

## 12. Related lessons

- [05-08-04 Density, Neutron and Sonic Porosity Logs](./04-porosity-logs.md)
  — the sonic integral that the check shot corrects.
- [05-08-07 Log Interpretation, Petrophysics and Uncertainty](./07-log-interpretation.md)
  — the full workflow, including depth matching.
- [05-07-04 Ground Truthing: Boreholes, Outcrop and Drill Core](../07-interpretation-and-integration/04-ground-truthing.md)
  — the tie as a validation experiment.
- [06-06-01 Seismic Tomography](../../06-seismology/06-seismic-tomography/README.md)
  — velocity estimation away from wells.
- [23-02-01 Seismometers and Sensor Physics](../../23-field-methods-instruments/02-seismic-instruments-and-fieldwork/01-seismometers.md)
  — the receiver side of the measurement.

## Self-assessment checklist

- [ ] I can distinguish the three measurements and their calibration roles. (§1)
- [ ] I can build a time–depth curve and difference check shots for interval
      velocities. (§3.1–3.2)
- [ ] I can compute the velocity-error-to-depth-error relation and its magnitude.
      (§3.3)
- [ ] I can explain the VSP geometry and compute a direct arrival. (§3.4)
- [ ] I can diagnose a tie discrepancy from its symptom. (§4.2)
- [ ] I can state what a tie does and does not prove. (§4.3)
- [ ] I can run the demonstration and explain every printed number. (§7)
