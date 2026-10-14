---
id: 09-06-02
title: "Borehole Radar and Directional Probing"
level: doctoral
prereqs: ["09-06-01", "09-05-02"]
tags: [electrical-methods, borehole, radar, tomography, resolution, ambiguity]
---

# Borehole Radar and Directional Probing

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the phase velocity $v = c/\sqrt{\varepsilon_r}$ of a low-loss
   dielectric and **compute** the wavelength and the half-wave resolution limit
   for a given antenna frequency.
2. **Derive** the low-loss attenuation $\alpha = (\sigma/2)\sqrt{\mu/\varepsilon}$
   and **state** the loss-tangent condition under which it holds, checking it
   against the exact complex wavenumber.
3. **Compute** a reflector range from a two-way travel time and **explain** why
   a single borehole cannot determine the reflector's azimuth, quantifying what
   a directional antenna does and does not fix.
4. **Formulate** cross-hole travel-time tomography as a linear system, **state**
   the straight-ray assumption it rests on, and **distinguish** a wave-regime
   measurement from the diffusive DC measurement of module 09-06-01.
5. **Measure** the numerical rank and null space of a cross-hole ray geometry,
   and **construct** a model perturbation that changes the data by
   $10^{-13}$ of the picking error.
6. **Justify** the choice of a damping parameter against the noise level rather
   than against the residual, and **report** the model error that choice buys.
7. **Explain** why adding oblique borehole-to-surface rays improves the
   conditioning, and **state** the limit beyond which more rays do not help.

## Prerequisites

- [09-06-01 Cross-Hole and Borehole-to-Surface Tomography](01-cross-hole-tomography.md) —
  the diffusive-potential counterpart of this method, and the vocabulary of
  sensitivity, rank and null space.
- [09-05-02 FEM Conductivity Mapping and Apparent Conductivity](../05-em-methods-applications/02-fem-conductivity-mapping.md) —
  the surface-geometry EM measurement that borehole radar descends from.
- [03-12 Verification and Validation in Numerical Modelling](../../03-scientific-computing/12-numerical-simulation-python/04-verification-and-validation.md) —
  linear algebra, sparse systems and conditioning.

## 1. Intuition: radar in a hole

In a resistive rock, an electromagnetic wave propagates rather than diffuses,
and the frequency band that penetrates metres to tens of metres of rock is
100 MHz to 1 GHz. A borehole radar antenna is a dipole small compared with the
wavelength, lowered into a hole; it radiates into the formation, and the same or
a second hole hosts the receiver.

Two geometries are standard and they answer different questions:

- **Single-hole reflection.** One hole, one antenna, and the reflections from
  changes in dielectric properties within a few metres of the hole. This gives a
  *range* and, with the right antenna, an *azimuth*; it is a borehole-wall
  imaging method.
- **Cross-hole transmission.** Two holes, transmitter in one and receiver in the
  other, and the travel times between them. This is transmission tomography: it
  measures the *velocity* between the holes, from which a permittivity (and hence
  a water content, if the rock is described by a simple mixing law) can be
  inferred.

This lesson is written around one honest difficulty that appears in both
geometries: **the measurement constrains a subset of what you would like to
know.** A single hole gives range without azimuth. Cross-hole transmission gives
paths that are nearly parallel, so the model it can resolve has fewer degrees of
freedom than the grid it is drawn on. Neither limitation is a defect of the
instrument; both are statements about geometry, and both can be quantified with
the tools of this lesson.

All models and data in this module are **SYNTHETIC**. The borehole geometry, the
dielectric constants and the velocity anomaly are chosen teaching values. The
speed of light and the static permittivity of liquid water are standard
constants.

## 2. Propagation in a low-loss dielectric

### 2.1 Phase velocity and wavelength

For a non-magnetic, insulating medium, Maxwell's equations give a plane wave with

$$v = \frac{1}{\sqrt{\mu\varepsilon}} = \frac{c}{\sqrt{\varepsilon_r}},
\qquad \lambda = \frac{v}{f},
\qquad c = 2.99792458\times10^{8}\ \mathrm{m\,s^{-1}}\ (\text{exact}),$$

where $f$ is the frequency. The half-wavelength, $\lambda/2$, is the standard
statement of the best possible resolution of a wave-based measurement: two
reflectors closer together than $\lambda/2$ cannot be separated by the band
around $f$.

*Numerical check.* With $\varepsilon_r = 6$,
$v = 2.99792458\times10^{8}/\sqrt{6} = 1.2239\times10^{8}\ \mathrm{m\,s^{-1}}
= 0.12239\ \mathrm{m\,ns^{-1}}$, and at 100 MHz
$\lambda = 1.2239\ \mathrm{m}$, so $\lambda/2 = 0.6119\ \mathrm{m}$.

The demonstration prints the same table for a range of dielectric constants,
including vacuum ($\varepsilon_r = 1$, $v = c$ exactly) and liquid water
($\varepsilon_r = 80.1$, the accepted static value at 20 °C), for which
$v = 0.03350\ \mathrm{m\,ns^{-1}}$ — a useful scale: in water, the wavelength at
100 MHz is only 0.335 m.

### 2.2 Attenuation and when it is "low loss"

The exact complex wavenumber of a conducting dielectric is

$$k = \omega\sqrt{\mu\varepsilon}\,\sqrt{1 - \mathrm{i}\frac{\sigma}{\omega\varepsilon}},
\qquad \omega = 2\pi f .$$

The **loss tangent** is $\sigma/(\omega\varepsilon)$. When it is small, the
square root can be expanded, the real part gives $v$ as above, and the imaginary
part gives

$$\boxed{\;\alpha \approx \frac{\sigma}{2}\sqrt{\frac{\mu}{\varepsilon}}\;}
\qquad [\mathrm{Np\,m^{-1}}], \qquad
\alpha_{\mathrm{dB}} = 8.686\,\alpha .$$

*Numerical check.* With $\varepsilon_r = 6$,
$\varepsilon = 6\varepsilon_0 = 5.3125\times10^{-11}\ \mathrm{F\,m^{-1}}$, so
$\sqrt{\mu_0/\varepsilon} = \sqrt{1.2566\times10^{-6}/5.3125\times10^{-11}}
= 153.8\ \Omega$. At $\sigma = 0.01\ \mathrm{S\,m^{-1}}$ this gives
$\alpha = 0.5\times0.01\times153.8 = 0.769\ \mathrm{Np\,m^{-1}}
= 6.68\ \mathrm{dB\,m^{-1}}$, and the loss tangent is
$\sigma/(\omega\varepsilon) = 0.01/(2\pi\cdot10^{8}\cdot5.3125\times10^{-11})
= 0.2996$.

The demonstration compares the approximation with the exact
$-\mathrm{Im}\,k$ across a decade of conductivity:

| $\sigma$ (S/m) | loss tangent | $\alpha$ (Np/m) | $\alpha$ (dB/m) | exact $\alpha$ | ratio |
|---|---|---|---|---|---|
| $10^{-4}$ | 0.0030 | $7.690\times10^{-3}$ | $6.680\times10^{-2}$ | $7.690\times10^{-3}$ | 1.0000 |
| $10^{-3}$ | 0.0300 | $7.690\times10^{-2}$ | $6.680\times10^{-1}$ | $7.689\times10^{-2}$ | 0.9999 |
| $10^{-2}$ | 0.2996 | $7.690\times10^{-1}$ | 6.680 | $7.607\times10^{-1}$ | 0.9892 |
| $5\times10^{-2}$ | 1.4979 | 3.845 | 33.40 | 3.249 | 0.8450 |
| $10^{-1}$ | 2.9959 | 7.690 | 66.80 | 5.333 | 0.6935 |

The approximation is better than $1\%$ while the loss tangent stays below about
$0.45$, and it is $31\%$ too high at a loss tangent of $3$. The lesson is not
that the formula is wrong but that **"low loss" is a statement about the ratio
$\sigma/(\omega\varepsilon)$**, and it must be checked rather than assumed. For
the synthetic host of the demonstration ($\sigma = 0.005\ \mathrm{S\,m^{-1}}$ at
100 MHz) the loss tangent is 0.1498, comfortably low, and the amplitude falls by
a factor $\mathrm{e}$ in $1/\alpha = 2.60\ \mathrm{m}$ — which is the honest
penetration figure for such a rock, not the wavelength.

## 3. Single-hole reflection: range yes, azimuth no

### 3.1 Range from a two-way time

A monostatic measurement records the two-way travel time to a reflector at range
$R$:

$$t = \frac{2R}{v} \quad\Longrightarrow\quad R = \frac{v\,t}{2},
\qquad \frac{\delta R}{R} = -\frac{\delta v}{v}.$$

*Numerical check.* With $v = 1.2239\times10^{8}\ \mathrm{m\,s^{-1}}$ and
$R = 5.0\ \mathrm{m}$: $t = 2\times5.0/1.2239\times10^{8} = 81.71\
\mathrm{ns}$.

The inversion for $R$ is exact given $v$ — and $v$ is *not* measured by a
monostatic reflection survey. It comes from a known permittivity, from a
calibration against a target at known range, or from a cross-hole transmission
measurement. A $10\%$ error in $v$ is a $10\%$ error in every range.

### 3.2 The azimuthal ambiguity

A centred dipole antenna radiates with a pattern that is rotationally symmetric
about the antenna axis. Every azimuth at the same range therefore produces the
same two-way time, so the reflector is known to lie on a **circle** of radius
$R$ around the hole:

$$2\pi R = 31.416\ \mathrm{m}\quad\text{for } R = 5.0\ \mathrm{m}.$$

A directional antenna restricts the azimuth to a beam. The arc left unresolved
is $2R\theta$ for a beam half-angle $\theta$:

| beam half-angle | azimuthal arc at $R = 5$ m |
|---|---|
| $\pm90^\circ$ (omni) | 15.708 m |
| $\pm30^\circ$ | 5.236 m |
| $\pm10^\circ$ | 1.745 m |

Even a $\pm10^\circ$ antenna leaves a 1.7 m arc: **range is measured, position is
not.** What removes the ambiguity is a second geometry — a second borehole, a
set of surface receivers, or a multi-component antenna whose coil orientations
give the direction cosines of the arrival (a vector measurement, not a scalar
one). The demonstration prints these numbers; the honest statement of a
single-hole reflection result always includes the arc, not only the range.

## 4. Cross-hole travel-time tomography

### 4.1 The model

In the ray (high-frequency) limit the travel time along a path is the integral of
slowness. With a grid of cells and straight paths,

$$t_i = \sum_j l_{ij}\,s_j, \qquad s_j = \frac{1}{v_j}\ [\mathrm{s\,m^{-1}}],$$

and $l_{ij}$ is the length of ray $i$ inside cell $j$. This is a linear system
$\mathbf{A}\mathbf{s} = \mathbf{t}$; **the straight-ray assumption is the model
error**, and it fails wherever the velocity contrast is sharp enough to bend a
ray within the cell size, or wherever the Fresnel zone is wider than the feature
of interest.

*Numerical check of the operator.* The demonstration builds $\mathbf{A}$ by
accumulating arc length along each path, then verifies that recomputing travel
times from the true model reproduces the data to machine precision (maximum
relative inconsistency $0.00\times10^{0}$). That is a check of the *operator*,
not of the physics: the physics is the straight-ray assumption.

### 4.2 Geometry, noise, and the two settings

The synthetic model is $10\times8 = 80$ cells spanning $0\le x\le20$ m and
$0\le z\le20$ m, with a +10% velocity lens in a $3\times3$ block. Picking noise
is 0.2 ns. Two acquisition geometries are compared:

| geometry | rays | rays per cell | condition number | numerical rank |
|---|---|---|---|---|
| cross-hole only | 64 | 1–18 (median 11) | $1.4\times10^{16}$ | 59 of 80 |
| cross-hole + surface | 136 | 1–40 (median 20) | $1.5\times10^{16}$ | 76 of 80 |

The condition number is meaningless in both cases — it is the numerical infinity
produced by exactly zero singular values — so the useful numbers are the **rank**
and the **damping behaviour**. With 64 rays and 80 cells the cross-hole problem
is underdetermined before any regularisation: at least 16 of the 80 cell values
are not measured, and in practice 21 are not. The rank rises to 76 of 80 when
oblique borehole-to-surface rays are added.

### 4.3 What the null space means, measured

Take the right-singular vector $\mathbf{v}$ belonging to the smallest singular
value. The demonstration reports

$$\frac{\|\mathbf{A}\mathbf{v}\|}{s_{\max}} = 2.59\times10^{-16},
\qquad \frac{s_{\min}}{s_{\max}} = 7.26\times10^{-17},$$

so $\mathbf{v}$ is a **true null vector of $\mathbf{A}$ to double precision**, not
merely a small singular value; and the deficiency is a property of the ray
geometry, not of the discretisation (rebuilding the path matrix with twice the
sampling density leaves the rank at 59 of 80).

Now perturb the recovered model along that direction by as much as the anomaly
itself, $\|\delta\mathbf{m}\| = 2.23\times10^{-9}\ \mathrm{s\,m^{-1}}$:

$$\|\mathbf{A}\,\delta\mathbf{m}\| = 1.28\times10^{-23}\ \mathrm{s}
\quad\text{against a picking error of}\quad 2.0\times10^{-10}\ \mathrm{s},$$

a ratio of $6.4\times10^{-14}$. The perturbation changes the velocities by up to
$11.8\%$ (rms $3.1\%$) while changing the data by thirteen orders of magnitude
less than the noise. **A model difference larger than the target is completely
invisible to this experiment.** That is what "underdetermined" means
operationally, and it is why the damping parameter, not the data, decides the
image.

### 4.4 Choosing the damping, and what it costs

Tikhonov damping with $\alpha = (k\,s_{\max})^{2}$ gives the following measured
behaviour (model error relative to the anomaly amplitude; the data misfit is a
percentage of the data norm):

| $k$ | cross-hole misfit | cross-hole model error | +surface misfit | +surface model error |
|---|---|---|---|---|
| $10^{-3}$ | 0.036% | 181.1% | 0.070% | 122.3% |
| $10^{-2}$ | 0.053% | 69.6% | 0.101% | 57.2% |
| $3\times10^{-2}$ | 0.277% | 96.1% | 0.528% | 167.8% |
| $10^{-1}$ | 2.165% | 385.7% | 3.926% | 750.2% |
| $3\times10^{-1}$ | 12.278% | 1803.4% | 19.387% | 4662.2% |

Three things are visible in that table and only one of them is reassuring.

1. There is a best choice ($k = 10^{-2}$ in this example) — **but it is not
   accessible from the data**, because finding it required knowing the true
   model. In practice you set the misfit to the noise level ($0.10\%$ of the
   largest datum here) and accept whatever model error that implies.
2. The model error is large everywhere: 57–70% of the anomaly amplitude at the
   best choice. The tomogram recovers the *presence and rough position* of the
   lens, not its amplitude.
3. Adding the surface rays reduces the achievable model error from 69.6% to
   57.2% at the same kind of misfit. The improvement is real, measured and
   modest; it is bounded by the geometry, not by the number of rays.

## 5. Assumptions and regime of validity

1. **Low-loss dielectric.** $\sigma/(\omega\varepsilon)\ll1$. In a saturated
   clay or a saline formation this fails and the propagation becomes diffusive;
   then the DC and EM coupling treatments of module 09-05 apply instead, and the
   travel-time concept dissolves.
2. **Non-magnetic.** $\mu_r = 1$. Magnetic minerals in an ore body break this
   and change both $v$ and the antenna's tuning.
3. **Straight rays.** Valid when the velocity contrast over a cell is small
   compared with the Fresnel scale; invalid at a sharp water table or a cavity
   wall, where diffraction and refraction dominate.
4. **Known antenna time zero and cable length.** A 1 ns error at
   $v = 0.122\ \mathrm{m\,ns^{-1}}$ is a 6 cm range error; in a short-range
   reflection survey that is comparable to the resolution.
5. **Scattering neglected.** The tomographic model has no attenuation term, so
   amplitude information is discarded; adding it would double the parametrisation
   and, as §4 shows, the rank is already short.
6. **Stationary raypaths.** The path matrix is built from the background model;
   a strong lens bends the rays it is imaged with.

## 6. Worked examples

### Example 1 — resolution versus grid size

The half-wave resolution at 100 MHz in $\varepsilon_r = 6$ is 0.612 m, but the
tomographic cells are $2.00\times2.50$ m. The image cannot be better than the
cells, and the cells cannot be much smaller than the ray coverage supports, so
the practical resolution is about *four times coarser* than the wavelength
suggests. Anyone who quotes $\lambda/2$ as the resolution of a tomogram has
confused the resolution of a *wave* with the resolution of an *inverse problem*.

### Example 2 — how much does a picking error cost?

With $\|\mathbf{A}\,\delta\mathbf{m}\| = \sigma_t$, the model perturbation
admitted by the noise is $\delta\mathbf{m} = \mathbf{A}^{+}\delta\mathbf{t}$.
Take a 0.2 ns pick error on a 20 m path whose travel time is 166 ns: that is
$0.12\%$ of the travel time, so the velocity along that single path is uncertain
by $0.12\%$ of $1.22\times10^{8}\ \mathrm{m\,s^{-1}}$, i.e.
$1.5\times10^{5}\ \mathrm{m\,s^{-1}}$. That is already large, and it is only
the *constrained* part. The unconstrained directions multiply it without limit,
because the model perturbation they admit is bounded by nothing in the data — the
demonstration quantifies one such direction as changing the data by
$6.4\times10^{-14}$ of the picking error (§4.3). **Noise never enters the null
space; the model does.**

### Example 3 — two-way time and the velocity

A cross-hole pick of 168.5 ns over a 20.6 m straight path gives
$v = 20.6/168.5\times10^{-9} = 1.223\times10^{8}\ \mathrm{m\,s^{-1}}$, and
$\varepsilon_r = (c/v)^{2} = (2.9979/1.223)^{2} = 6.01$. The permittivity follows
directly — which is why cross-hole radar is used for water-content imaging: a
change from $\varepsilon_r = 6$ to $\varepsilon_r = 20$ changes $v$ by a factor
1.83. Note the *inversion* of this relation: $\varepsilon_r$ is derived from the
assumed mineral and fluid mixture model, and that assumption is not tested by the
travel time.

## 7. Python demonstration

[`code/borehole_radar_demo.py`](./code/borehole_radar_demo.py) prints, with
units:

1. velocity, wavelength and half-wave resolution versus dielectric constant and
   frequency, including the exact value of $c$;
2. attenuation versus the loss tangent, with the exact $-\mathrm{Im}\,k$ beside
   the low-loss approximation;
3. the single-hole range and the azimuthal arc for three antenna beam widths;
4. the two ray geometries: rays, coverage, singular spectrum, numerical rank,
   the damping sweep, and the null-space vector's pattern;
5. the equivalence demonstration of §4.3 and the rank stability check.

```bash
cd 09-electrical-em-methods/06-borehole-electrical/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python borehole_radar_demo.py
```

It takes under half a second, needs no network, uses a fixed seed and exits 0.

## 8. Exercises

See
[`exercises/02-borehole-radar-exercises.md`](./exercises/02-borehole-radar-exercises.md)
and
[`exercises/02-borehole-radar-solutions.md`](./exercises/02-borehole-radar-solutions.md).

- **★** Compute $v$, $\lambda$ and $\lambda/2$ for three dielectric constants at
  two frequencies, and state the resolution in metres.
- **★★** Derive the low-loss attenuation from the exact wavenumber and find the
  loss tangent at which the approximation is 5% low.
- **★★** Given the arc lengths of §3.2, decide whether a $\pm30^\circ$ antenna
  is sufficient to site a borehole to intersect a target at 5 m range, and state
  the criterion you used.
- **★★★** Design a cross-hole radar survey whose ray matrix has rank at least
  90% of the number of cells, and defend the design with the singular spectrum.
  You may not use more than two boreholes.

## 9. Common mistakes

1. **Quoting $\lambda/2$ as the tomogram's resolution.** The tomogram's
   resolution is set by ray coverage and regularisation.
2. **Treating a single-hole range as a position.** It is a circle; report the
   arc.
3. **Calling the straight-ray model "the physics".** It is an approximation with
   a stated regime, and the regime fails where the contrast is sharp.
4. **Choosing damping to minimise the residual.** The residual can always be
   reduced by adding model structure that the geometry cannot see.
5. **Reporting a velocity without the permittivity assumption** that connects it
   to water content.

## Mastery checkpoint

Complete this without notes.

> A cross-hole radar survey in a low-loss rock operates at 250 MHz.
> **(a)** The straight-path travel time over 20.0 m is 164.0 ns. Compute $v$,
> $\varepsilon_r$ and $\lambda$, and state the half-wave resolution.
> **(b)** Compute the low-loss attenuation for $\sigma = 0.004\ \mathrm{S\,m^{-1}}$
> and the loss tangent, and check that the regime is valid. Quote the amplitude
> loss in dB over 20 m.
> **(c)** A single-hole reflection survey in the same rock sees a reflector at
> 81.7 ns. Compute the range and state what is *not* determined; give the arc
> length for a $\pm30^\circ$ antenna.
> **(d)** The cross-hole survey has 80 cells and 64 rays. State the maximum rank
> of the path matrix, the measured rank in the demonstration, and what the
> difference means for a model you report.
> **(e)** Name two measurements that would break the azimuthal ambiguity and two
> that would raise the rank.

A worked version of (a)–(c) appears in the lesson-02
[solutions](./exercises/02-borehole-radar-solutions.md).

## Common pitfalls

1. **Assuming low loss.** Check $\sigma/(\omega\varepsilon)$; write the number.
2. **Forgetting the antenna time zero.** A constant delay is a constant range
   bias and it is invisible in a single trace.
3. **Confusing coverage with resolution.** A cell crossed by many parallel rays
   is not resolved.
4. **Believing the amplitude.** Neither the ray tomogram nor the reflection
   amplitude is calibrated in this lesson; amplitudes require the full
   transmission model.
5. **Reporting a single tomogram.** Give the singular spectrum or the resolution
   estimate beside the image.

## Related modules

- [09-06-01 Cross-Hole and Borehole-to-Surface Tomography](01-cross-hole-tomography.md) —
  the diffusive regime, and the same rank and equivalence arguments in a
  different physics.
- [09-06-03 Downhole EM Logging and Induction Tools](03-downhole-em-logging.md) —
  the low-frequency end of the same spectrum, where diffusion rather than
  propagation applies.
- [09-05 Applied Electromagnetic Methods](../05-em-methods-applications/README.md) —
  the surface geometries and their penetration/resolution trade.
- [10-gpr-near-surface](../../10-gpr-near-surface/README.md) — the same wave
  physics from the surface, with the coupling and antenna problems in full.
