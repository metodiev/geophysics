---
id: 08-02-01
title: "Fluxgate Magnetometers: Principle and Use"
level: advanced
prereqs: ["02-07-04", "02-07-07", "08-01-01"]
tags: [geomagnetism, instruments, fluxgate, magnetometer, harmonics, cross-axis-error]
---

# Fluxgate Magnetometers: Principle and Use

A total-field magnetometer measures one scalar and needs no orientation. A
fluxgate measures the **components** of the field and therefore needs a frame:
levelling, a heading, and a stable mounting. That extra requirement is the price
of the extra information, and this lesson develops the physics that makes the
fluxgate work — Faraday induction in a saturating core, read at the second
harmonic — and then the engineering consequences: sensitivity, linearity,
first-order cross-axis error and the noise floor.

**All models and data in this module are SYNTHETIC.** The core magnetisation
curve, drive frequency, coil geometry, interference and noise are chosen teaching
values. No instrument, manufacturer or published specification is described. The
only standard constant used is $\mu_0 = 4\pi\times10^{-7}\ \mathrm{H\,m^{-1}}$.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the sense-coil EMF from Faraday's law, $e = -NA\,\mathrm{d}B/\mathrm{d}t$,
   and evaluate it for a stated coil and drive.
2. **Explain** why a saturating core driven symmetrically produces only **odd**
   harmonics, and why the presence of an external field generates the **second**
   harmonic.
3. **Measure** the second-harmonic sensitivity from a synthetic response curve
   and state its units.
4. **Determine** the linearity range of the response from the core's knee field.
5. **Compute** the first-order cross-axis error for a stated mounting
   misalignment.
6. **Budget** the noise floor of a fluxgate reading and state how averaging
   changes it.

## Prerequisites

- [02-07-04 Faraday's Law, Induction and Eddy Currents](../../02-physics/07-electromagnetism/04-em-induction.md)
  — the induction law used throughout.
- [02-07-07 Magnetisation, Susceptibility and Magnetic Materials](../../02-physics/07-electromagnetism/07-magnetisation-materials.md)
  — a saturating $M(H)$ curve and what "saturation" means.
- [08-01-01 Describing the Main Field: Declination, Inclination, Intensity](../01-earth-magnetic-field/01-main-field-description.md)
  — the components and the frame the sensor must supply.

## 1. Why a component sensor is a different machine

A proton or alkali sensor ([08-02-02](02-proton-overhauser.md),
[08-02-03](03-cesium-optically-pumped.md)) measures a **frequency** proportional
to $|\mathbf{B}|$. There is no way to extract components from a scalar: the
information is not there. To measure $(X,Y,Z)$ one needs a sensor whose output
depends on the field *through a direction fixed in the instrument*.

The fluxgate achieves this with a **saturating core** and a **sense coil**:

```
   drive coil  ──►  high-permeability core  ◄──  sense coil
   (AC current)      saturates twice per cycle      (EMF pickup)
```

The core's permeability is high only while it is unsaturated. An external field
along the axis biases the core so that it spends unequal times saturated in the
two directions; the asymmetry appears as a signal at **twice** the drive
frequency, and its magnitude is proportional to the external component along the
axis. The second harmonic is the measurement; the drive frequency is the carrier.

## 2. Faraday's law and the size of the signal

For a sense coil of $N$ turns and area $A$,

$$e(t) = -NA\frac{\mathrm{d}B}{\mathrm{d}t}, \qquad
B = \mu_0\left(H + M(H)\right),$$

so with $M(H) = M_s\tanh(H/H_k)$ for a synthetic core,

$$\frac{\mathrm{d}B}{\mathrm{d}t} = \mu_0\left(1 + \frac{M_s}{H_k}
\operatorname{sech}^{2}\!\frac{H}{H_k}\right)\frac{\mathrm{d}H}{\mathrm{d}t}.$$

The derivative of $M$ is largest near $H = 0$ (the core's knee) and vanishes once
the core is saturated: the signal is generated during the few tens of
microseconds per cycle when the core is switching.

*Worked example.* Drive frequency $1000\ \mathrm{Hz}$, peak drive field
$100\ \mathrm{A\,m^{-1}}$, $N = 50$ turns, $A = 1.0\times10^{-5}\ \mathrm{m^2}$,
$M_s = 1.0\times10^{6}\ \mathrm{A\,m^{-1}}$, $H_k = 20\ \mathrm{A\,m^{-1}}$. The
demonstration reports

$$\left|\frac{\mathrm{d}B}{\mathrm{d}t}\right|_{\max}
= 3.9473\times10^{4}\ \mathrm{T\,s^{-1}}, \qquad
|e|_{\max} = 19.736\ \mathrm{V}.$$

The scale check is worth doing by hand: a flux swing of order
$2\mu_0M_s = 2\times1.2566\times10^{-6}\times10^{6} = 2.513\ \mathrm{T}$
completed in roughly a quarter of a drive period
($250\ \mu\mathrm{s}$) gives $\mathrm{d}B/\mathrm{d}t \sim 10^{4}\
\mathrm{T\,s^{-1}}$, consistent with the measured value. Then
$NA\,\mathrm{d}B/\mathrm{d}t = 50\times10^{-5}\times3.9\times10^{4}
\approx 20\ \mathrm{V}$ ✔.

Two engineering consequences fall straight out of the formula:

- **The signal scales with frequency.** At fixed flux swing, doubling the drive
  frequency doubles the EMF. That is why fluxgates are driven at kilohertz
  rather than at tens of hertz.
- **The signal scales with core volume**, through $M_s$ and $A$. Sensitivity per
  unit mass is bought with permeability and with coil geometry, not with more
  turns alone (more turns raises the EMF but also the inductance and the
  capacitance, which limits the usable frequency).

## 3. Why the second harmonic, and not the first

Let the external component along the sensor axis be $H_e$ and the drive be
$H_d\sin\omega t$, so $H = H_d\sin\omega t + H_e$. The core magnetisation is
$M(H) = M_s\tanh(H/H_k)$.

- **With $H_e = 0$**: $M$ is an odd function of $H$, and $H(t)$ is odd about
  $t = 0$; the induced EMF has period $1/f$ and contains only **odd** harmonics.
  The demonstration's harmonic amplitudes are

$$\begin{array}{c|ccccc}
\text{harmonic} & 1f & 2f & 3f & 4f & 5f \\ \hline
|E| \ \text{(V)} & 4.939890 & 1.19\times10^{-5} & 4.328972 & 1.19\times10^{-5} & 3.404074
\end{array}$$

  The even harmonics are suppressed to $2.4\times10^{-6}$ of the fundamental —
  and that residual is the numerical floor of the symmetric model, not physics.

- **With $H_e \neq 0$**: the drive no longer swings symmetrically about the
  core's centre, so the time spent saturated in one direction differs from the
  other. That asymmetry is *even* in the drive phase and appears as **even**
  harmonics, of which $2f$ is the largest.

This is the design idea: measure at $2f$, where the *drive* contributes nothing,
and where the response vanishes when the external field vanishes. A sensor read at
$1f$ would have to detect a small change in a large carrier.

### 3.1 The measured second-harmonic sensitivity

With the same core, the demonstration sweeps the external field and records the
amplitude at $2f$ (after subtracting the zero-field floor of
$1.1878\times10^{-5}\ \mathrm{V}$):

| $H_e$ (nT) | $H_e$ (A/m) | $A(2f)$ (V) | $A(2f)/H_e$ (V per A/m) |
|---|---|---|---|
| 50.0 | 0.039789 | $3.7859\times10^{-3}$ | 0.0949 |
| 100.0 | 0.079577 | $7.5725\times10^{-3}$ | 0.0950 |
| 200.0 | 0.159155 | $1.5146\times10^{-2}$ | 0.0951 |
| 400.0 | 0.318310 | $3.0292\times10^{-2}$ | 0.0951 |
| 800.0 | 0.636620 | $6.0584\times10^{-2}$ | 0.0951 |
| 1600.0 | 1.273240 | $1.2116\times10^{-1}$ | 0.0951 |
| 3200.0 | 2.546479 | $2.4225\times10^{-1}$ | 0.0951 |

The response is linear to better than **0.35%** over the whole range tested,
with a slight upward curvature that is the next order of the $\tanh$ expansion.
Converting the slope,

$$\frac{\mathrm{d}A(2f)}{\mathrm{d}H_e} = 9.4852\times10^{-2}\
\mathrm{V\,(A\,m^{-1})^{-1}} = 75.4807\ \mu\mathrm{V\,nT^{-1}}.$$

### 3.2 Linearity range from the core parameters

The physical limit is the knee field. Once the external field becomes a
significant fraction of $H_k$, the core is already biased into saturation and the
response rolls off:

$$\mu_0H_k = 4\pi\times10^{-7}\times20 = 2.5133\times10^{-5}\ \mathrm{T}
= 25133\ \mathrm{nT}.$$

That is the natural dynamic range of this design: the response is linear for
external fields small compared with $\mu_0H_k$, and the demonstration's data
confirm it out to $3200\ \mathrm{nT}$, which is 13% of $\mu_0H_k$. **The dynamic
range of a fluxgate is set by the core material, not by the electronics.**

## 4. Cross-axis error: a first-order penalty for a wrong heading

A component sensor responds to the field projection on its axis. If the sense
coil is misaligned by an angle $\alpha$ from the intended axis, then

$$B_{\text{measured}} = B_{\parallel}\cos\alpha + B_{\perp}\sin\alpha.$$

For small $\alpha$ the second term is **first order in $\alpha$**:

| $\alpha$ (°) | $\sin\alpha$ | leaked field from $B_\perp = 50000$ nT |
|---|---|---|
| 0.1 | 0.001745 | 87.266 nT |
| 0.5 | 0.008727 | 436.327 nT |
| 1.0 | 0.017452 | 872.620 nT |
| 2.0 | 0.034899 | 1744.975 nT |

A one-degree mounting error is an $873\ \mathrm{nT}$ error in a
$50000\ \mathrm{nT}$ field, and — crucially — the error is *not random*: it is
proportional to the perpendicular component, so it varies with heading and with
latitude, and it does not average out. Two operational consequences:

- **A fluxgate is only as good as its levelling and heading.** A survey that
  wants 1 nT components needs $\alpha$ below about $0.001^{\circ}$, which is
  unattainable mechanically: component surveys instead *calibrate* the
  misalignment by rotating the sensor in a known field.
- **The $Z$ component is the most robust.** Misalignments in the horizontal plane
  mix $X$ and $Y$ but leak only $\sin(\text{tilt})\times H$ into $Z$; a sensor
  that is levelled well but rotated badly still gives a usable $Z$.

Contrast this with the alkali sensors of [08-02-03](03-cesium-optically-pumped.md),
whose heading error is *second* order: a scalar magnetometer can tolerate a
degrees-level alignment because its error term is $\propto\sin^2\alpha$.

## 5. Noise, bandwidth and the resolution budget

With a synthetic electronics noise density of $3.162\times10^{-4}\
\mathrm{V/\sqrt{Hz}}$ over a $10\ \mathrm{Hz}$ bandwidth the rms noise is
$1.000\times10^{-3}\ \mathrm{V}$, which against the
$75.4807\ \mu\mathrm{V\,nT^{-1}}$ sensitivity is

$$\sigma_B = \frac{1.000\times10^{-3}}{7.54807\times10^{-5}}
= 13.248\ \mathrm{nT} \ \text{for a single reading},$$

falling to $1.325\ \mathrm{nT}$ after averaging 100 independent readings
($1/\sqrt{100}$). Two lessons:

- **Sensitivity is not resolution.** A sensor with $\mu\mathrm{V/nT}$
  sensitivity and $\mathrm{mV}$ noise has a nanotesla-class floor; the two numbers
  must be quoted together.
- **Averaging divides by $\sqrt{N}$ only for independent noise.** Diurnal drift,
  sensor tilt and temperature are correlated between readings, so averaging them
  does not help; they must be modelled or removed.

## 6. Use: what a fluxgate is for

| task | why a fluxgate |
|---|---|
| Observatory variometers | continuous $X$, $Y$, $Z$ for secular-variation studies, checked against absolute instruments |
| Spacecraft magnetometry | compact, low power, three axes, no orientation-sensitive optics |
| Directional drilling | $Z$ for dip and a rough azimuth |
| Base stations and compensation | fast, wide-band, records the *variation* for diurnal correction |
| Gradiometers | paired sensors give a difference that cancels common-mode noise ([08-02-04](04-gradiometers-arrays.md)) |

The pattern: a fluxgate is the instrument of choice when the **components** or
the **variation** matter, and a scalar sensor is chosen when only $|B|$ matters
and the field is weak or the platform is not stable.

## 7. Assumptions and regime of validity

1. **The core curve is a model.** $M = M_s\tanh(H/H_k)$ is a smooth
   approximation; real cores have hysteresis, so the response depends on the
   drive amplitude and on history.
2. **The sense axis is the measured axis.** Section 4 quantifies what happens
   when it is not.
3. **The external field is small compared with $\mu_0H_k$.** Beyond that the
   response is nonlinear and the calibration must be a curve, not a constant.
4. **The drive is a pure sinusoid.** Harmonics in the drive appear in the output
   at the detection frequency; practical instruments use tuned drive and
   synchronous detection at $2f$ with a phase-sensitive detector.
5. **Noise is white and independent between readings.** Averaging claims in
   section 5 depend on it.
6. **Synthetic parameters.** The numbers are teaching values; the relationships
   are the content.

## 8. Python demonstration

`code/fluxgate_demo.py` prints, with units:

1. the peak $\mathrm{d}B/\mathrm{d}t$ and EMF for the stated coil and drive;
2. the harmonic amplitudes with no external field, showing the odd/even
   suppression;
3. the second harmonic versus the external field, the sensitivity in
   $\mu\mathrm{V\,nT^{-1}}$, and the linearity range;
4. the cross-axis leak for four misalignments;
5. the noise floor, the single-reading resolution and the effect of averaging;
6. five seeded random draws, so the run is reproducible.

Exercises and solutions:
[`exercises/01-fluxgate-magnetometers-exercises.md`](./exercises/01-fluxgate-magnetometers-exercises.md),
[`exercises/01-fluxgate-magnetometers-solutions.md`](./exercises/01-fluxgate-magnetometers-solutions.md).

## Mastery checkpoint

1. Compute $|e|_{\max}$ for $N = 200$, $A = 2\times10^{-5}\ \mathrm{m^2}$ and
   the demonstration's $|\mathrm{d}B/\mathrm{d}t|_{\max}$.
2. Explain in two sentences why the second harmonic vanishes with the external
   field and the first does not.
3. Convert the demonstration's sensitivity into nT per volt.
4. Compute the leak into a component reading for $\alpha = 0.3^{\circ}$ with
   $B_\perp = 48000\ \mathrm{nT}$.
5. A field noise of 13.248 nT per reading is too large for a 1 nT survey. State
   two changes that reduce it and one that does not.

## Common pitfalls

1. **Quoting sensitivity without noise.** Section 5 gives both.
2. **Treating the linearity range as an electronic limit.** It is
   $\mu_0H_k$ of the core.
3. **Ignoring cross-axis error because the number is small.** It is
   multiplicative and systematic.
4. **Assuming averaging always helps.** Only for independent noise.
5. **Reading a fluxgate as absolute.** Most are relative instruments; absolute
   components need calibration against a scalar and a reference direction.

## Related modules

- [08-02-02 Proton Precession and Overhauser Magnetometers](02-proton-overhauser.md) —
  the scalar alternative.
- [08-02-04 Gradiometers, Arrays and Noise Rejection](04-gradiometers-arrays.md) —
  what pairs of fluxgates buy.
- [08-01-04 Secular Variation, Jerks and Core Dynamics](../01-earth-magnetic-field/04-secular-variation.md) —
  why observatories want components.
- [02-07 Electromagnetism and Electromagnetic Induction](../../02-physics/07-electromagnetism/README.md) —
  the physics of the drive and the pickup.

## Self-assessment checklist

- [ ] I can derive and evaluate the sense-coil EMF.
- [ ] I can explain the harmonic structure with and without an external field.
- [ ] I can convert a measured sensitivity into a field resolution.
- [ ] I can compute a cross-axis error.
- [ ] I can state what sets the dynamic range and what sets the noise floor.
- [ ] I can say when a fluxgate is the right instrument.
