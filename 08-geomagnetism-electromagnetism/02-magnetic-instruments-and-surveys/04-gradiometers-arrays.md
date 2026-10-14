---
id: 08-02-04
title: "Gradiometers, Arrays and Noise Rejection"
level: advanced
prereqs: ["08-02-01", "08-01-03", "05-02-03"]
tags: [geomagnetism, instruments, gradiometer, gradient-tensor, noise-rejection, common-mode]
---

# Gradiometers, Arrays and Noise Rejection

Two magnetometers separated by a fixed baseline measure a **difference**, and a
difference of two nearby measurements is an approximation to a gradient. The
attraction is that whatever is common to both sensors — the main field, the
regional field, the diurnal variation, much of the instrument noise — cancels.
The price is that the *signal* also falls off faster with distance than the field
does, and that the sensor pair now must know its own geometry to a precision that
makes the baseline a calibration problem in its own right. This lesson develops
the arithmetic of both sides.

**All models and data in this module are SYNTHETIC.** The dipole moments, sensor
separations, noise levels and correlation structure are chosen teaching values.
The only standard constant used is $\mu_0 = 4\pi\times10^{-7}\ \mathrm{H\,m^{-1}}$.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the common-mode noise-rejection relation
   $\sigma_{\text{diff}} = \sqrt{2(1-\rho)}\,\sigma$ and evaluate it for stated
   correlations.
2. **Derive** the dipole scalings $|B|\propto r^{-3}$ and
   $|\partial B/\partial z|\propto r^{-4}$, and the ratio of a gradient to a
   field measurement as a function of distance.
3. **Decide** from stated noise floors whether a total-field or a gradient
   measurement detects a target at a given depth.
4. **Verify** the tracelessness and symmetry of the magnetic gradient tensor and
   state what each property follows from.
5. **Compute** the wavelength response $2\sin(\pi L/\lambda)$ of a gradiometer and
   state its null.
6. **Explain** why a gradient channel is insensitive to diurnal drift but not to
   baseline geometry, and what an array adds to a pair.

## Prerequisites

- [08-02-01 Fluxgate Magnetometers: Principle and Use](01-fluxgate-magnetometers.md) —
  the component sensors a gradiometer is built from.
- [08-01-03 Spherical Harmonic Analysis of the Magnetic Field](../01-earth-magnetic-field/03-spherical-harmonic-magnetic.md) —
  the long-wavelength structure that a gradient rejects.
- [05-02-03 Noise, Drift, Tides and Instrument Bias in Field Data](../../05-core-geophysics/02-geophysical-fields-and-observables/03-noise-and-drift.md)
  — the noise taxonomy used here.

## 1. The idea, and the arithmetic of cancellation

Let two sensors measure $B_1 = s + n_1$ and $B_2 = s + n_2$, where $s$ is the
common signal (main field, regional field, diurnal variation) and $n_i$ the
sensor noise. The difference is

$$B_1 - B_2 = n_1 - n_2,$$

so the common signal cancels **exactly** — no model, no filtering, no
assumption about its shape. What remains is the difference of the noises, whose
variance for correlation coefficient $\rho$ between the two noises is

$$\mathrm{Var}(n_1-n_2) = 2\sigma^{2}(1-\rho)
\quad\Longrightarrow\quad
\boxed{\;\sigma_{\text{diff}} = \sqrt{2(1-\rho)}\,\sigma.\;}$$

The demonstration measures this by Monte Carlo over 20 000 samples with
$\sigma = 1.0\ \mathrm{nT}$:

| $\rho$ | measured $\sigma_{\text{diff}}$ (nT) | rejection factor $\sigma/\sigma_{\text{diff}}$ | model $\sqrt{2(1-\rho)}$ |
|---|---|---|---|
| 0.000 | 1.4053 | 0.71 | 1.4142 |
| 0.500 | 0.9972 | 1.00 | 1.0000 |
| 0.900 | 0.4461 | 2.24 | 0.4472 |
| 0.990 | 0.1413 | 7.08 | 0.1414 |
| 0.999 | 0.0444 | 22.54 | 0.0447 |

Three consequences, all of which are operational:

- **At $\rho = 0$ the difference is worse than either sensor** by $\sqrt{2}$. A
  gradiometer built from two *independent* noisy sensors is a worse field
  instrument than one of them; the whole benefit is the correlation.
- **The benefit is entirely in the correlated part.** It is the main field, the
  regional gradient, the diurnal variation and the common power-supply noise that
  are rejected — physical commonality, not electronics.
- **$\rho$ near 1 is required for a large gain.** At $\rho = 0.99$ the rejection
  is only 7.1; to reach a 20-fold rejection the correlation must exceed 0.999.
  In practice a gradiometer achieves its performance by making the two sensors
  *identical and close*, and its specification is a statement about
  $\rho$, not about either sensor.

## 2. The signal side: how fast the target fades

For a dipole of moment $\mathbf{m}$ at depth $z$ directly below a sensor, the
field on the axis is

$$|\mathbf{B}| = \frac{\mu_0}{4\pi}\frac{2m}{z^{3}},$$

and differentiating along the axis,

$$\left|\frac{\partial B}{\partial z}\right|
= \frac{\mu_0}{4\pi}\frac{3\times2m}{z^{4}}
= \frac{3}{z}\,|\mathbf{B}|.$$

So the gradient does not merely fall faster; it falls as $r^{-4}$ against the
field's $r^{-3}$, and the ratio of the two measurements is $z/3$. The
demonstration's SYNTHETIC dipole ($m = 10\ \mathrm{A\,m^2}$) gives:

| depth (m) | $|B|$ (nT) | $|\partial B/\partial z|$ (nT/m) | $|B|/|\text{grad}|$ (m) |
|---|---|---|---|
| 2.0 | 250.000 | 375.0000 | 0.667 |
| 5.0 | 16.000 | 9.6000 | 1.667 |
| 10.0 | 2.000 | 0.6000 | 3.333 |
| 20.0 | 0.250 | 0.0375 | 6.667 |
| 40.0 | 0.031 | 0.0023 | 13.333 |

The last column is exactly $z/3$ at every line, which is the numerical statement
of the derivation. **The gradient is a short-range measurement.**

## 3. Detection depth: the comparison that decides

Neither scaling alone answers the design question; only the *noise floors* do.
With SYNTHETIC floors of $0.10\ \mathrm{nT}$ for the total field and
$0.010\ \mathrm{nT\,m^{-1}}$ over a $1.0\ \mathrm{m}$ baseline, the demonstration
finds:

| depth (m) | S/N total field | S/N gradient | ratio g/b | detected by |
|---|---|---|---|---|
| 2.0 | 2500.00 | 37500.00 | 15.00 | both |
| 5.0 | 160.00 | 960.00 | 6.00 | both |
| 10.0 | 20.00 | 60.00 | 3.00 | both |
| 20.0 | 2.50 | 3.75 | 1.50 | gradient only |
| 40.0 | 0.31 | 0.23 | 0.75 | neither at 3$\sigma$ |

The gradient's **relative advantage** falls from 15× at 2 m to 1.5× at 20 m and
below 1 at 40 m, exactly as the $r^{-4}$ against $r^{-3}$ scaling requires. There
is no general rule that the gradiometer is the better instrument: it is better
when the target is shallow *and* the components' noise is correlated. A design
must be evaluated at the target depth, with both floors stated.

## 4. Beyond a difference: the gradient tensor

With three (or more) component sensors the full tensor can be measured:

$$G_{ij} = \frac{\partial B_i}{\partial x_j},$$

which has nine components, but two exact mathematical properties reduce it:

- **Traceless:** $G_{xx}+G_{yy}+G_{zz} = 0$, because in a source-free region
  $\nabla\cdot\mathbf{B} = 0$ (equivalently the field is harmonic).
- **Symmetric:** $G_{ij} = G_{ji}$, because $\nabla\times\mathbf{B} = 0$ in a
  current-free region.

The demonstration verifies both for a dipole at $(0.7, -1.1, 3.0)\ \mathrm{m}$:

$$G = \begin{pmatrix}
+18.52905 & +8.64689 & -17.97505\\
+8.64689 & +10.44365 & +28.24651\\
-17.97505 & +28.24651 & -28.97270
\end{pmatrix}\ \mathrm{nT\,m^{-1}},$$

with $\operatorname{tr}G = -1.82\times10^{-8}\ \mathrm{nT\,m^{-1}}$ and
$\max|G_{ij}-G_{ji}| = 1.49\times10^{-7}\ \mathrm{nT\,m^{-1}}$. Both residuals are
the accuracy of the finite-difference differentiator, not a physical asymmetry:
**the properties are an arithmetic check on the instrument, not a measurement of
the target.** And they are useful precisely that way — a tensor gradiometer with
a nonzero trace has a mis-scaled or mis-aligned channel, and the check costs
nothing.

Because of the two properties only **five** of the nine components are
independent, and that is the reason tensor gradiometry is practical at all.

## 5. What a difference does to the spectrum

Consider a field varying sinusoidally with wavelength $\lambda$ along the
baseline $L$. The two sensors see $A\cos(kx)$ and $A\cos(kx+kL)$ with
$k = 2\pi/\lambda$, so their difference has amplitude

$$\left|A\cos(kx) - A\cos(kx+kL)\right|_{\max}
= 2A\left|\sin\frac{kL}{2}\right| = 2A\left|\sin\frac{\pi L}{\lambda}\right|.$$

The demonstration tabulates this response, normalised to the fully resolved value
of 2:

| $L/\lambda$ | response $2\sin(\pi L/\lambda)$ | fraction of full response |
|---|---|---|
| 0.0001 | 0.000628 | 0.0314% |
| 0.0010 | 0.006283 | 0.3142% |
| 0.0100 | 0.062822 | 3.1411% |
| 0.0500 | 0.312869 | 15.6434% |
| 0.1000 | 0.618034 | 30.9017% |
| 0.5000 | 2.000000 | 100.0000% |

Two readings of the same table:

- **This is why the gradiometer removes the main field.** The main field and its
  regional gradient have $L/\lambda \ll 1$, so their response vanishes linearly:
  the gradiometer is a high-pass filter in wavelength with a null at infinite
  wavelength.
- **It also attenuates long-wavelength targets.** A target whose anomaly has
  $\lambda = 10\,L$ is measured at 31% of its true gradient amplitude, and a
  target with $\lambda = 100\,L$ at 3.1%. The instrument cannot distinguish "no
  target" from "a target that is too broad", which is a statement about the
  transfer function, not about the geology.

## 6. Noise spectra, drift, and what a gradient does not need

The demonstration compares a synthetic total-field channel (white noise plus a
slow drift) with a gradient channel formed from two samples of the same noise:

| channel | rms | low-frequency PSD / high-frequency PSD |
|---|---|---|
| total field | 2.1723 | $5.4\times10^{3}$ |
| gradient | 0.5020 | $4.7\times10^{-5}$ |

The total-field channel is dominated by its low-frequency content (the drift);
the gradient channel's spectrum is essentially flat and dominated by the high
frequencies. **A gradiometer is inherently immune to the diurnal variation**,
because the diurnal signal is common to both sensors and has a wavelength of
thousands of kilometres. This is a genuine operational advantage:

- No base station is needed to remove the diurnal variation.
- Instrument drift, which is also common to both sensors, cancels.
- What does **not** cancel is the baseline: an error in the sensor separation of
  $\delta L$ produces a proportional error in the gradient, and a tilt of the
  baseline relative to the intended axis converts a large field component into a
  spurious gradient — a first-order cross-axis problem in the difference rather
  than in a single sensor.

## 7. Arrays

An array generalises the pair in three ways.

- **Spatial derivatives of higher order.** With several sensors the second
  derivatives become measurable, and second derivatives decay as $r^{-5}$: even
  more selective, even more demanding of geometry.
- **Source localisation.** The ratio of a gradient to a field, or the pattern
  across an array, gives the direction and often the depth of a source. For a
  dipole the ratio takes the simple form $|\text{grad}|/|B| = 3/z$ from §2, so a
  measured ratio gives $z$ directly — a depth estimate that requires no model of
  the target's strength.
- **Coherent noise rejection by beamforming.** If the target is a moving source
  (a vehicle passing, a pipeline pig) and the noise is stationary, the array's
  inter-sensor delays separate them. This is the geophysical use of the same
  mathematics as seismic arrays, and it needs a sampling rate high enough to
  resolve the transit time across the array, which is the practical constraint.

The corresponding vulnerability is that arrays are only as good as their geometry
knowledge: all of the above are functions of the *differences* between sensor
positions, so a systematic baseline error maps directly into the derived
quantities.

## 8. Assumptions and regime of validity

1. **The common signal is truly common.** A field that varies between the two
   sensors (a diurnal gradient, a nearby source) does not cancel.
2. **The baseline is small compared with the wavelength of the target anomaly.**
   Otherwise the "difference" is not a derivative and the transfer function of §5
   must be applied explicitly.
3. **The geometry is known.** Baseline length and orientation enter the answer
   linearly; the calibration of the difference channel is as important as the
   calibration of the sensors.
4. **The two sensors match.** A sensitivity mismatch $\epsilon$ leaves a fraction
   $\epsilon$ of the common signal in the difference, which is the most common
   way a real gradiometer fails.
5. **Noise is stationary and the correlation is stable.** $\rho$ that drifts with
   temperature or time changes the noise floor.
6. **Synthetic parameters.** The moments, floors and correlations here are
   teaching values.

## 9. Python demonstration

`code/gradiometers_arrays_demo.py` prints, with units:

1. field and gradient versus depth for a synthetic dipole, with the $z/3$ ratio
   checked in the last column;
2. the measured common-mode rejection versus correlation, against
   $\sqrt{2(1-\rho)}$;
3. detection depth for two stated noise floors, with the gradient-to-field S/N
   ratio;
4. a full gradient tensor with its trace and antisymmetry residuals;
5. the spectra of a total-field and a gradient channel;
6. the wavelength response $2\sin(\pi L/\lambda)$.

Exercises and solutions:
[`exercises/04-gradiometers-arrays-exercises.md`](./exercises/04-gradiometers-arrays-exercises.md),
[`exercises/04-gradiometers-arrays-solutions.md`](./exercises/04-gradiometers-arrays-solutions.md).

## Mastery checkpoint

1. Compute $\sigma_{\text{diff}}/\sigma$ for $\rho = 0.95$ and for
   $\rho = 0.9999$.
2. A dipole lies 15 m below a gradiometer with a 1.5 m baseline. Compute the
   field and gradient magnitudes at the upper sensor, and the S/N of each for
   floors of 0.05 nT and 0.005 nT/m.
3. Show that $\nabla\cdot\mathbf{B} = 0$ implies a traceless gradient tensor, and
   state the corresponding result for $\nabla\times\mathbf{B} = 0$.
4. Compute the gradient response at $L/\lambda = 0.02$ and state the fraction of
   the true gradient amplitude a survey would recover.
5. Explain in two sentences why a gradiometer needs no diurnal correction but
   does need a baseline calibration.

## Common pitfalls

1. **Assuming a gradiometer has less noise.** At $\rho = 0$ it has more, by
   $\sqrt{2}$.
2. **Forgetting the transfer function.** A gradiometer under-reports broad
   anomalies by construction, and the deficit is computable.
3. **Blaming the sensors for a mismatch.** A sensitivity mismatch leaks common
   signal into the difference; that is a *calibration* failure, not noise.
4. **Treating a nonzero tensor trace as a target signature.** It is an instrument
   fault (or a differentiator error).
5. **Quoting a gradient without the baseline.** The unit is nT/m and the
   baseline is part of the datum.
6. **Expecting depth estimates without assumptions.** The clean $z/3$ result
   assumes a dipole on the axis.

## Related modules

- [08-02-01 Fluxgate Magnetometers: Principle and Use](01-fluxgate-magnetometers.md) —
  the sensors a gradiometer is built from.
- [08-02-05 Airborne Magnetic Surveys and Compensation](05-airborne-magnetic-surveys.md) —
  where arrays become practical engineering.
- [08-03 Magnetic Anomalies and Modelling](../03-magnetic-anomalies-and-modelling/README.md) —
  the forward models that make a gradient interpretable.
- [05-02-03 Noise, Drift, Tides and Instrument Bias in Field Data](../../05-core-geophysics/02-geophysical-fields-and-observables/03-noise-and-drift.md) —
  the noise taxonomy.

## Self-assessment checklist

- [ ] I can derive and evaluate the common-mode rejection relation.
- [ ] I can derive the $r^{-3}$ and $r^{-4}$ scalings and the $z/3$ ratio.
- [ ] I can decide between a field and a gradient measurement from stated floors.
- [ ] I can verify the tensor's trace and symmetry numerically.
- [ ] I can compute a gradiometer's wavelength response.
- [ ] I can say what an array adds and what it demands.
