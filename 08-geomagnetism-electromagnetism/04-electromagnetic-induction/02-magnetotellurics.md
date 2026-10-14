---
id: 08-04-02
title: "Magnetotellurics: Impedance Tensor, Apparent Resistivity, Phase"
level: doctoral
prereqs: ["08-04-01", "01-10-02"]
tags: [electromagnetism, geomagnetism, magnetotellurics, impedance-tensor, tipper, static-shift, dimensionality]
---

# Magnetotellurics: Impedance Tensor, Apparent Resistivity, Phase

Magnetotellurics (MT) uses the Earth's natural magnetic variation as its source
and measures the ratio of the electric to the magnetic field at the surface. That
ratio, the **impedance**, is a transfer function of the subsurface; from it one
obtains an *apparent resistivity* and a *phase* at each period, and from those a
conductivity–depth profile. This lesson develops the 1-D impedance recursion,
verifies it against an exact half-space, then generalises to the $2\times2$
**impedance tensor**, its rotation and invariants, the **tipper**, and the
**static shift** — the multiplicative ambiguity that no amount of processing can
remove.

> All models and data in this module are **SYNTHETIC**.

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** the MT impedance and **derive** the 1-D layered recursion.
2. **Verify** the recursion on a uniform half-space, where
   $\rho_a = \rho$ and the phase is exactly $45^\circ$.
3. **Compute** and **interpret** apparent resistivity and phase curves for a
   layered model, including the phase's departure from $45^\circ$.
4. **Rotate** the impedance tensor, **demonstrate** its rotation invariants, and
   **recover** the strike of a 2-D structure.
5. **Derive** the tipper, **compute** induction-arrow azimuths, and **state**
   what the tipper does and does not determine.
6. **Compute** the effect of a static shift on $\rho_a$ and on the phase, and
   **explain** why the two are independent measurements.
7. **Diagnose** dimensionality from a tensor's skew and the inequality of
   $\rho_{xy}$ and $\rho_{yx}$.

## Prerequisites

- [08-04-01 Induction, Skin Depth and Diffusion](01-em-induction-basics.md) — the
  diffusion equation and the skin depth.
- [01-10-02 The Fourier Transform](../../01-mathematics/10-fourier-analysis/02-fourier-transform.md) —
  how time series become frequency-domain transfer functions.

## 1. The impedance

Write the horizontal electric and magnetic fields at angular frequency $\omega$
as phasors. In a 1-D Earth the two are related by a single complex number,

$$E_x(\omega) = Z(\omega)\,H_y(\omega),\qquad
Z = \frac{E}{H}\ \left(\mathrm{\Omega}\right),$$

and $Z$ is **independent of the source**: whatever the magnetosphere does, the
Earth's transfer function is the same, so the ratio can be estimated from
simultaneous recordings of $E$ and $H$. This is the central practical advantage
of the method — the source is unknown and irrelevant, as long as it is uniform
and contains energy at the period of interest.

For a uniform half-space the plane-wave solution of
[01](01-em-induction-basics.md) gives immediately

$$Z = \sqrt{i\omega\mu_0\rho}, \qquad
\left|Z\right| = \sqrt{\omega\mu_0\rho}, \qquad
\arg Z = 45^\circ .$$

## 2. The 1-D layered recursion

In a layer of resistivity $\rho_i$ the horizontal fields are superpositions of a
downward and an upward decaying part; the impedance is propagated upward by
impedance matching, exactly as in a transmission line. With

$$k_i = \sqrt{\frac{i\omega\mu_0}{\rho_i}}, \qquad
\eta_i = \frac{i\omega\mu_0}{k_i} = \sqrt{i\omega\mu_0\rho_i},$$

the impedance at the top of layer $i$, seen through a layer of thickness $h_i$
lying on the interface with impedance $Z_{i+1}$, is

$$\boxed{\;Z_i = \eta_i\,
\frac{Z_{i+1} + \eta_i\tanh\left(k_ih_i\right)}
{\eta_i + Z_{i+1}\tanh\left(k_ih_i\right)}\;}$$

and the recursion starts from the half-space at the bottom, $Z_N = \eta_N$. This
is the entire forward problem for a 1-D Earth, and it is worth noting how much of
the interpretation of MT rests on it.

*Limit check.* A single layer over a half-space of the same resistivity must
return the half-space value. Setting $Z_{i+1} = \eta_i$ gives
$Z_i = \eta_i\left(\eta_i+\eta_i\tanh\right)/\left(\eta_i+\eta_i\tanh\right) =
\eta_i$: the recursion is insensitive to a layer that does not contrast with what
is below it, as it must be.

**Numerical check.** The demonstration runs the recursion on a uniform
$100\ \Omega$m half-space at $T = 1$ s and at $T = 100$ s and recovers

| Period | $\left|Z\right|$ ($\Omega$) | $\rho_a$ ($\Omega$m) | Phase |
|---|---|---|---|
| 1 s | $2.809926\times10^{-2}$ | 100.0000000000 | $45.0000000000^\circ$ |
| 100 s | $2.809926\times10^{-3}$ | 100.0000000000 | $45.0000000000^\circ$ |

to all printed digits. This is the MT equivalent of "the forward model returns
the input", and every inversion in [04](04-mt-inversion.md) depends on it.

## 3. Apparent resistivity and phase

From $Z$ one defines two real functions of period,

$$\rho_a(\omega) = \frac{\left|Z\right|^{2}}{\omega\mu_0},
\qquad \phi(\omega) = \arg Z(\omega),$$

called the **Cagniard apparent resistivity** and the **phase**. They are not
independent measurements in a 1-D Earth — each determines the other through the
dispersion relation imposed by the diffusion equation — but they are independent
*estimates* of the same structure, and their disagreement is a diagnostic of 2-D
or 3-D structure, noise, or a static shift.

For the demonstration's **synthetic** three-layer model (100 $\Omega$m for 1 km,
10 $\Omega$m for 4 km, 1000 $\Omega$m half-space):

| Period (s) | $\rho_a$ ($\Omega$m) | Phase (deg) |
|---|---|---|
| 0.001 | 99.9993 | 45.0000 |
| 0.010 | 102.6650 | 44.1724 |
| 0.100 | 83.5834 | 61.0409 |
| 1.000 | 27.2967 | 62.3339 |
| 10.000 | 12.4971 | 38.0761 |
| 100.000 | 54.6920 | 14.5454 |
| 1000.000 | 257.3952 | 21.6836 |
| 10000.000 | 610.5584 | 33.6252 |

Read the curve as a sequence of messages, not a profile. At the shortest periods
the skin depth is inside the first layer and the response is that layer's
($\rho_a \to 100$, phase $\to 45^\circ$). The phase rises above $45^\circ$ where
resistivity *falls* with depth (the conductor at 1–5 km) and drops below
$45^\circ$ where it *rises* (the resistive basement). This is a general rule worth
committing to memory: $\phi > 45^\circ$ means conductivity increasing with depth,
$\phi < 45^\circ$ means the reverse, and $\phi = 45^\circ$ means the structure
looks uniform over the depth being sensed.

## 4. The impedance tensor

With arbitrary lateral structure the two horizontal components of each field must
be related by a $2\times2$ tensor:

$$\begin{pmatrix}E_x\\ E_y\end{pmatrix} =
\begin{pmatrix}Z_{xx} & Z_{xy}\\ Z_{yx} & Z_{yy}\end{pmatrix}
\begin{pmatrix}H_x\\ H_y\end{pmatrix}.$$

The tensor contains more than the 1-D impedance, and that is the point: it
diagnoses directionality. Rotating the coordinate frame by angle $\theta$ gives
$\mathbf{Z}' = \mathbf{R}\mathbf{Z}\mathbf{R}^{T}$ with
$\mathbf{R} = \begin{pmatrix}\cos\theta & \sin\theta\\ -\sin\theta &
\cos\theta\end{pmatrix}$, and two quantities are invariant under the rotation:

$$\left|Z_{xy} + Z_{yx}\right| \quad\text{and}\quad
\left|Z_{xy} - Z_{yx}\right| .$$

**Verification (SYNTHETIC).** Take a 2-D tensor in strike coordinates at
$T = 10$ s with $Z_{xy}$ corresponding to $300\ \Omega$m and $Z_{yx}$ to
$180\ \Omega$m:

$$Z_{xy} = 0.011790 + 0.009893i, \qquad Z_{yx} = -0.011203 - 0.004077i\ \Omega,$$

so $\left|Z_{xy}+Z_{yx}\right| = 0.005845$ and
$\left|Z_{xy}-Z_{yx}\right| = 0.026904$. Rotating:

| $\theta$ (deg) | $\left|Z_{xx}\right|$ | $\left|Z_{yy}\right|$ | $\left|Z_{xx}+Z_{yy}\right|$ | $\left|Z_{xy}+Z_{yx}\right|$ | $\left|Z_{xy}-Z_{yx}\right|$ |
|---|---|---|---|---|---|
| 0 | 0.000 | 0.000 | 0.000000 | 0.005845 | 0.026904 |
| 15 | 0.001 | 0.001 | 0.000000 | 0.005062 | 0.026904 |
| 30 | 0.003 | 0.003 | 0.000000 | 0.002923 | 0.026904 |
| 45 | 0.003 | 0.003 | 0.000000 | 0.000000 | 0.026904 |
| 60 | 0.003 | 0.003 | 0.000000 | 0.002923 | 0.026904 |

Two properties of a 2-D tensor are visible. First, the two invariants are
constant to machine precision while the individual elements change. Second,
$Z_{xx} = -Z_{yy}$ in every frame, so $\left|Z_{xx}+Z_{yy}\right| = 0$ identically
— this is the **2-D test**, and it is why the skew is defined as
$\left|Z_{xx}+Z_{yy}\right|/\left|Z_{xy}-Z_{yx}\right|$.

**Strike recovery.** Minimising $\left|Z_{xx}\right|^{2}+\left|Z_{yy}\right|^{2}$
over rotation angle recovers the strike of a synthetic tensor rotated by
$20^\circ$, $35^\circ$ and $55^\circ$ as $20.00^\circ$, $35.00^\circ$ and
$55.00^\circ$ respectively. The axis is determined only up to a sign and a
$90^\circ$ ambiguity, which is inherent to a 2-D tensor and not a defect of the
method: a tensor cannot distinguish a strike from its perpendicular.

## 5. The tipper

The vertical magnetic field is related to the horizontals by the **tipper**:

$$H_z = T_{zx}H_x + T_{zy}H_y .$$

For a 1-D Earth the tipper is zero at every period, because a uniform source
produces no vertical field over a layered Earth. A non-zero tipper is therefore a
statement about **lateral** structure. The real part of the tipper defines an
**induction arrow**: in the Parkinson convention it points from the more
conductive region to the less conductive one (equivalently, towards the
conductor or away from it, depending on the convention in use — state it
explicitly, always).

For a synthetic 2-D structure, the tipper is perpendicular to strike:

| Strike (deg) | $T_{zx}$ | $T_{zy}$ | Arrow azimuth (deg) | $\left|T\right|$ |
|---|---|---|---|---|
| 0 | $+0.0000$ | $+0.3447$ | 90.0 | 0.3500 |
| 30 | $-0.1723$ | $+0.2985$ | 120.0 | 0.3500 |
| 60 | $-0.2985$ | $+0.1723$ | 150.0 | 0.3500 |
| 90 | $-0.3447$ | $+0.0000$ | 180.0 | 0.3500 |

The azimuth stays exactly $90^\circ$ from the strike. Note what the tipper
carries: a direction and a magnitude, at each period. It carries **no depth**. It
is a lateral-structure detector, complementary to the impedance, and it is
essential when the structure is not layered — see
[03 MT Processing](03-mt-processing.md) and
[06 Geomagnetic Depth Sounding](06-geomagnetic-depth-sounding.md).

## 6. The static shift

Suppose the measured impedance is multiplied by a real constant,

$$Z_{\text{obs}} = s\,Z_{\text{true}}, \qquad s \in \mathbb{R},\ s > 0 .$$

This is exactly what a near-surface, galvanically distorting body does to the
electric field over a broad band: it scales $E$ without changing its phase. Then

$$\rho_a^{\text{obs}} = s^{2}\rho_a^{\text{true}}, \qquad
\phi^{\text{obs}} = \phi^{\text{true}} .$$

**Measured (SYNTHETIC),** $T = 10$ s on the three-layer model:

| Multiplier $s$ | $\rho_a$ ($\Omega$m) | Phase (deg) |
|---|---|---|
| 0.5 | 3.124 | 38.076067 |
| 1.0 | 12.497 | 38.076067 |
| 2.0 | 49.988 | 38.076067 |

A factor of two in $Z$ is a factor of four in $\rho_a$ and *nothing at all* in
phase. Two consequences, both central to practice:

1. **The phase constrains the structure; the amplitude constrains it only up to
   $s^{2}$.** This is why MT inversions of the phase alone are stable and
   inversions of $\rho_a$ alone are not.
2. **The shift must be removed by something outside the MT data** — a
   coincident time-domain EM sounding, a transient, or an a priori resistivity —
   or it must be inverted for as an unknown per station, with a prior that
   penalises scattered shifts. It is one of the few problems in this folder that
   *cannot* be solved by more careful processing.

## 7. Dimensionality diagnostics

Three synthetic tensors at $T = 10$ s, with apparent resistivities computed from
the off-diagonal elements:

| Tensor | $\left|Z_{xx}+Z_{yy}\right|$ | $\left|Z_{xy}-Z_{yx}\right|$ | Skew | $\rho_{xy}$ ($\Omega$m) | $\rho_{yx}$ ($\Omega$m) |
|---|---|---|---|---|---|
| 1-D | 0.0000 | 0.0251 | 0.0000 | 200.000 | 200.000 |
| 2-D, strike $30^\circ$ | 0.0000 | 0.0269 | 0.0000 | 261.887 | 201.887 |
| 3-D (synthetic) | 0.0159 | 0.0233 | 0.6834 | 210.000 | 150.000 |

Read the table as a decision procedure. Unequal $\rho_{xy}$ and $\rho_{yx}$ rule
out a 1-D Earth; a non-zero skew rules out a 2-D one as well. A 2-D Earth has
zero skew and two different apparent resistivities (the TE and TM modes), and
interpreting it with a 1-D model produces a curve that depends on the array
orientation — a classic and avoidable error.

## 8. Assumptions and regime of validity

1. **A uniform (plane-wave) source.** The impedance is only source-independent if
   the source is spatially uniform over the array and over a skin depth; the
   $k\delta$ criterion is quantified in
   [06](06-geomagnetic-depth-sounding.md).
2. **The quasi-static approximation.** As in [01](01-em-induction-basics.md).
3. **Linear, time-invariant transfer functions.** Non-linear behaviour
   (e.g. from strong currents) is not modelled.
4. **No noise, or noise handled by the estimator.** The bias from noise is
   derived and measured in [03 MT Processing](03-mt-processing.md); it is not
   small.
5. **The recursion assumes 1-D structure.** For 2-D and 3-D, a numerical forward
   solver is required; the tensor algebra of Sections 4–7 is what one applies to
   *any* tensor, whatever produced it.
6. **$\mu = \mu_0$, scalar $\sigma$, isotropic.** As in [01](01-em-induction-basics.md).
7. **The static shift is a real positive constant over the band.** True for
   galvanic distortion from a shallow body much smaller than the skin depth;
   failures of this assumption produce frequency-dependent shifts that a single
   parameter cannot absorb.

## 9. Python demonstration

`code/magnetotellurics_demo.py`:

1. verifies the 1-D recursion on a half-space at two periods;
2. tabulates $\rho_a$ and phase for a three-layer model and shows the
   $45^\circ$ rule;
3. rotates a synthetic 2-D tensor, checks the invariants to machine precision and
   recovers the strike;
4. prints tipper components, arrow azimuths and magnitudes for four strikes;
5. applies three static-shift factors and shows that the phase does not move;
6. diagnoses the dimensionality of three synthetic tensors.

```bash
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python magnetotellurics_demo.py
```

Fixed seed, print-only, exits 0.

## 10. Exercises

[`exercises/02-magnetotellurics-exercises.md`](./exercises/02-magnetotellurics-exercises.md)
and
[`exercises/02-magnetotellurics-solutions.md`](./exercises/02-magnetotellurics-solutions.md).

## Mastery checkpoint

Without notes:

> **(a)** Compute $Z$ for a uniform $50\ \Omega$m half-space at $T = 20$ s, and
> its phase. **(b)** A two-layer model has $\rho_1 = 50\ \Omega$m for 500 m over a
> $500\ \Omega$m half-space; state whether the phase at short periods is above or
> below $45^\circ$ and why. **(c)** A measured tensor has
> $Z_{xx} = 3+2i$, $Z_{xy} = 40+30i$, $Z_{yx} = -20-15i$, $Z_{yy} = -3-2i$
> (in $10^{-3}\ \Omega$). Compute the skew and decide the dimensionality.
> **(d)** A colleague reports $\rho_a = 400\ \Omega$m from a station and
> $\rho_a = 100\ \Omega$m from a neighbouring station with the same phase. State
> the most likely cause and what you would do. **(e)** State the one thing about
> the source that MT requires, and why.

## Common pitfalls

1. **Reading $\rho_a$ as the resistivity of a layer.** It is a weighted average
   over the depth range sensed at that period.
2. **Using $\rho_a$ alone.** The static shift multiplies it by an unknown
   constant.
3. **Ignoring the tensor off-diagonal structure.** A 2-D data set interpreted as
   1-D gives different answers in different orientations.
4. **Treating the tipper as a depth measurement.** It is a lateral-structure
   measurement.
5. **Assuming the strike is unambiguous.** It is known only up to sign and
   $90^\circ$.
6. **Forgetting the phase convention.** Different sign conventions for
   $E$–$H$ pairs flip the phase quadrant; always state the convention.

## Related modules

- [01 Induction, Skin Depth and Diffusion](01-em-induction-basics.md) — the
  physics behind the impedance.
- [03 MT Processing](03-mt-processing.md) — how $Z$ is estimated from noisy time
  series.
- [04 MT Inversion](04-mt-inversion.md) — turning curves into models.
- [05 MT Interpretation](05-mt-interpretation.md) — what the models mean.
- [06 Geomagnetic Depth Sounding](06-geomagnetic-depth-sounding.md) — the
  long-period limit, where the source is not a plane wave.
