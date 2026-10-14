---
id: 12-05-01
title: "Free Oscillations of the Earth (Normal Modes)"
level: research
prereqs: ["02-03-03", "06-01-02", "12-01-01"]
tags: [global-geophysics, earth-interior, normal-modes, free-oscillations, eigenproblem]
---

# Free Oscillations of the Earth (Normal Modes)

**All models and data in this module are SYNTHETIC.** The elastic structure used
below is invented; it is not PREM or any published Earth model, and no measured
mode period is quoted. Every number in this lesson is printed by
[`code/free_oscillations_demo.py`](./code/free_oscillations_demo.py).

## Learning objectives

By the end of this lesson you will be able to:

1. **Formulate** the radial (spheroidal $l = 0$) eigenproblem for a spherically
   symmetric elastic body with a free surface, and **state** its two boundary
   conditions.
2. **Derive** the transcendental eigenvalue equation of a homogeneous elastic
   sphere and **solve** it for the first few roots.
3. **Build** a finite-difference eigenproblem for a layered model and **verify**
   it against the analytic result, measuring the order of convergence.
4. **Explain** the scaling $T \propto R/\alpha$ and **verify** it by computation.
5. **Interpret** a mode's kinetic-energy profile as a sensitivity kernel, and
   **quantify** how a structural perturbation moves a period.
6. **State** which modes are sensitive to which part of the Earth, and why a
   period is a constraint on structure rather than on size alone.
7. **Separate** what a synthetic normal-mode catalog can and cannot tell you
   about the real Earth.

## Prerequisites

- [02-03-03 Coupled Oscillators and Normal Modes](../../02-physics/03-oscillations-and-waves/03-coupled-oscillators.md) —
  the discrete normal-mode idea this lesson makes continuous.
- [06-01-02 P and S Waves](../../06-seismology/01-elastic-wave-propagation/02-p-and-s-waves.md) —
  P and S speeds and their elastic definition.
- [12-01-01 PREM, IASP91 and Reference Earth Models](../01-seismic-structure-of-the-earth/01-prem-and-reference-models.md) —
  the real reference models, whose synthetic analogue is used here.

## 1. Why a whole-Earth mode is special

A body wave samples the Earth along a ray. A **free oscillation** samples it
everywhere at once: the whole planet rings at a discrete set of eigenfrequencies,
each with its own spatial pattern and its own depth sensitivity. That is both the
attraction and the difficulty. The attraction is that a single period is a
weighted average of the structure over the whole body, so a mode constrains the
planet rather than a path. The difficulty is that the weighting — the sensitivity
kernel — depends on the structure you are trying to determine, so the inverse
problem is nonlinear before it starts.

This lesson builds the machinery for the simplest family, the **radial modes**,
for which the equations reduce to one dimension and an analytic check exists.
The general families ($_nS_l$ spheroidal and $_nT_l$ toroidal) add angular
dependence and, for the gravest spheroidal modes, self-gravitation; those
complications are enumerated in §7.

## 2. The radial eigenproblem

Let $U(r)$ be the radial displacement of a spherically symmetric, isotropic
elastic medium of density $\rho(r)$ and Lamé parameters $\lambda(r)$, $\mu(r)$.
For purely radial motion the equation of motion is

$$\frac{\mathrm{d}}{\mathrm{d}r}\left[(\lambda+2\mu)\frac{\mathrm{d}U}{\mathrm{d}r}
+ \frac{2\lambda U}{r}\right] + \frac{4\mu}{r}\left(\frac{\mathrm{d}U}{\mathrm{d}r}
- \frac{U}{r}\right) = -\rho\,\omega^{2}U .$$

The bracket is the radial traction $\sigma_{rr}$; the second term is the
geometric contribution of the spherical geometry. The two boundary conditions are

$$U(0) = 0 \quad\text{(regularity at the centre)}, \qquad
(\lambda+2\mu)\frac{\mathrm{d}U}{\mathrm{d}r}\bigg|_{R} + \frac{2\lambda U(R)}{R}
= 0 \quad\text{(zero traction at the free surface)} .$$

With a time dependence $e^{i\omega t}$, this is a Sturm–Liouville problem: a
discrete, real, positive spectrum $\omega_n^{2}$ with an orthogonal set of
eigenfunctions. For a *constant* $\lambda$, $\mu$, $\rho$ it reduces to

$$U'' + \frac{2}{r}U' - \frac{2}{r^{2}}U = -k^{2}U,\qquad k^{2} = \frac{\rho
\omega^{2}}{\lambda+2\mu} = \frac{\omega^{2}}{\alpha^{2}},$$

whose regular solution is the spherical Bessel function $j_1(kr)$ — note $j_1$,
not $j_0$, because the geometric term brings the same $l(l+1)$ with $l = 1$.

## 3. Derivation: the homogeneous transcendental equation

Take $U = j_1(kr)$. The free-surface condition needs $j_1'(x)$ at $x = kR$; using
$x j_1'(x) = j_0(x) - 2j_1(x)/x$ and $j_1(x) = \sin x/x^{2} - \cos x/x$:

$$(\lambda+2\mu)k\,j_1'(x) + \frac{2\lambda}{R}j_1(x) = 0
\;\Longrightarrow\;
\left[(\lambda+2\mu)x^{2} - 4\mu\right]\sin x + 4\mu x\cos x = 0,$$

and therefore

$$\boxed{\;\tan x = \frac{4\mu\,x}{4\mu - (\lambda+2\mu)x^{2}}\;}$$

The demonstration solves it and prints

| $n$ | $x_n$ | $T_n$ (min) | equation residual |
|---|---|---|---|
| 0 | 2.60263 | 32.0431 | $4.0\times10^{-14}$ |
| 1 | 6.07055 | 13.7378 | $7.4\times10^{-15}$ |
| 2 | 9.28735 | 8.9796 | $3.5\times10^{-14}$ |
| 3 | 12.46435 | 6.6908 | $-1.5\times10^{-15}$ |
| 4 | 15.62673 | 5.3368 | $-4.4\times10^{-14}$ |

with $T_n = 2\pi R/(x_n\alpha)$ and the adopted
$\alpha = 8.0\ \mathrm{km\,s^{-1}}$, $\beta = 4.5\ \mathrm{km\,s^{-1}}$,
$\rho = 4200\ \mathrm{kg\,m^{-3}}$ (giving $\lambda = 9.87\times10^{10}$ Pa and
$\mu = 8.505\times10^{10}$ Pa). The residual column is the check on the root
finder, and it is at machine precision.

Two things to notice. The first root is $x_0 = 2.603$, not the $\pi$ of a naive
"half-wavelength" argument: the free-surface condition is a *traction* condition,
not a displacement node. And the roots are not equally spaced, but their spacing
increases slowly towards $x_{n+1} - x_n \to \pi$ for large $n$, when the
curvature term becomes negligible and the sphere behaves like a flat plate of
thickness $R$.

## 4. A layered model, by finite differences

For a real structure the analytic route disappears and the eigenproblem must be
discretised. The demonstration assembles the strong form on a uniform grid,
imposing $U_0 = 0$ at the centre and zero traction at the surface, and solves the
generalised problem $A\mathbf{U} = \omega^{2}B\mathbf{U}$ with $B =
-\mathrm{diag}(\rho)$. Its synthetic structure has five layers: an outer core
with $\beta = 0$ (no shear support), a lower mantle, a transition zone, an upper
mantle and a crust.

The resulting radial periods and frequencies are

| $n$ | $T_n$ (min) | $f_n$ (mHz) |
|---|---|---|
| 0 | 21.270 | 0.7836 |
| 1 | 10.672 | 1.5617 |
| 2 | 6.476 | 2.5734 |
| 3 | 5.136 | 3.2451 |

**Verification.** The code is checked against the analytic homogeneous solution,
on which it should be exactly second-order accurate:

| $n_{\text{points}}$ | FD period (min) | analytic (min) | relative error |
|---|---|---|---|
| 25 | 32.05120 | 32.04310 | $2.53\times10^{-4}$ |
| 50 | 32.04589 | 32.04310 | $8.71\times10^{-5}$ |
| 100 | 32.04389 | 32.04310 | $2.48\times10^{-5}$ |
| 200 | 32.04331 | 32.04310 | $6.58\times10^{-6}$ |
| 400 | 32.04315 | 32.04310 | $1.69\times10^{-6}$ |

The successive error ratios are 2.90, 3.51 and 3.77 — approaching 4, which is the
signature of a second-order scheme. Applied to the homogeneous model at 400
points, the first three FD periods differ from the analytic ones by
$1.7\times10^{-6}$, $7.6\times10^{-6}$ and $1.9\times10^{-5}$ relative. Two
independent routes agreeing to parts in $10^{5}$ is the only kind of evidence
that a discretisation is correct, and it is the reason the homogeneous case is
kept in the demonstration at all.

On the layered model the interfaces limit the accuracy to about $10^{-3}$: the
fundamental is 21.2695 min at 400 points against a Richardson-extrapolated
21.2631 min, and the error at 100, 200 and 400 points is 0.080%, 0.121% and
0.030%. Finite differences across a discontinuity are first-order accurate
locally, and that is what such a table measures.

## 5. What a mode samples: sensitivity kernels

For each mode the demonstration computes the fraction of the kinetic energy
$\int \rho U^{2}r^{2}\,\mathrm{d}r$ that lies inside $r < 3471$ km (below the
660-km discontinuity):

| mode | energy fraction below 660 km |
|---|---|
| 0 | 0.172 |
| 1 | 0.663 |
| 2 | 0.483 |
| 3 | 0.524 |

The structure of that table is not intuitive and is worth dwelling on. The
**fundamental** radial mode has a long radial wavelength and its displacement is
large in the outer part of the model, so only 17% of its energy is deep. The
first overtone has a radial node near the middle and concentrates its energy
below it: 66%. Higher overtones alternate. So "the gravest mode sees the whole
Earth" is true only in the sense that it is sensitive *everywhere*; its kernel is
concentrated where its displacement is largest.

**Perturbation experiment.** Apply a random multiplicative perturbation to every
layer's $\alpha$ and $\beta$ at level $\epsilon$ and measure the shift in the
fundamental period:

| $\epsilon$ | mean $|\delta T/T|$ (%) | scatter (%) |
|---|---|---|
| 0.002 | 0.170 | 0.207 |
| 0.005 | 0.244 | 0.273 |
| 0.010 | 0.544 | 0.542 |

A 1% velocity perturbation moves the period by about half a per cent, with a
sign that depends on the realisation. This is the practical form of the
statement that a period constrains structure: the kernel (not the period) tells
you which structure, and the kernel is computed from the same model you are
testing.

## 6. The scaling law

Two runs settle the scaling:

$$T(R/2)/T(R) = 0.5000, \qquad T(2\alpha)/T(\alpha) = 0.5000 .$$

$$T \propto \frac{R}{\alpha}$$

is therefore exact for the homogeneous sphere and approximately true for any
model whose shape is unchanged: a period is a *ratio* of a length to a speed, so
a period alone cannot separate a small fast body from a large slow one. Resolving
that degeneracy requires either two different mode families (which weight
$\alpha$ and $\beta$ differently) or an independent constraint on the size, such
as the mass or the moment of inertia from
[12-06 Geodetic Constraints on the Interior](../06-geodesy-constraints-interior/README.md).

## 7. What this lesson omits, and why it matters

1. **Angular dependence.** Spheroidal ($_nS_l$) and toroidal ($_nT_l$) modes with
   $l \ge 1$ bring angular equations and a richer spectrum. The toroidal family
   is insensitive to the fluid outer core; the spheroidal family is not.
2. **Self-gravitation.** For the gravest spheroidal modes the perturbation of the
   gravitational field is comparable to the elastic restoring force, and the mode
   period depends on the density distribution as well as the elastic moduli. A
   purely elastic model gets those modes wrong by tens of per cent.
3. **Attenuation.** Every real mode decays; the decay rate is $Q^{-1}$ and is the
   subject of [02 Tidal Response and the Quality Factor of the Whole Earth](02-tidal-response.md).
4. **Rotation and ellipticity.** Both split each mode into a multiplet whose
   components differ by fractions of a per cent. The splitting is information
   (it constrains the rotation rate and the asphericity) and a complication (it
   must be modelled before the centre frequency is used).
5. **Anisotropy and anelasticity.** Radial anisotropy shifts some modes
   systematically; neglecting it biases the inverted structure.
6. **The synthetic structure.** The layered model here is invented; its periods
   are properties of the teaching model, not of the Earth. The *method* — for
   which the analytic check exists — is the transferable part.

## 8. Mastery checkpoint

Without notes:

> A homogeneous elastic sphere has $R = 6371$ km, $\alpha = 8.0\
> \mathrm{km\,s^{-1}}$, $\beta = 4.5\ \mathrm{km\,s^{-1}}$ and
> $\rho = 4200\ \mathrm{kg\,m^{-3}}$. **(a)** Write the radial equation of motion
> and its two boundary conditions. **(b)** Derive the transcendental eigenvalue
> equation. **(c)** Compute the fundamental period and state why it is not
> $2R/\alpha$. **(d)** Predict what happens to every period if $\alpha$ and
> $\beta$ are both doubled and $R$ is unchanged. **(e)** State which physical
> effects make a real Earth's gravest spheroidal periods different from this
> model's by tens of per cent.

## 9. Common pitfalls

1. **Quoting a period without the model that produced it.** A period is a
   functional of the whole structure.
2. **Assuming the gravest mode sees only the deep Earth.** Its energy fraction
   below 660 km is 17% in the demonstration's model.
3. **Testing a discretisation against itself.** Only an analytic reference, or a
   second independent method, tests a solver.
4. **Using a first-order-accurate interface treatment and expecting
   second-order convergence.** The layered model is limited to about $10^{-3}$
   here.
5. **Forgetting the degeneracy $T \propto R/\alpha$.** One period cannot separate
   size from speed.
6. **Ignoring attenuation when comparing to observations.** A measured peak has a
   width, and the width carries $Q$ information.

## 10. Related modules

- [02 Tidal Response and the Quality Factor of the Whole Earth](02-tidal-response.md) —
  what makes the modes decay.
- [03 Rotation Variations, LOD and Core-Mantle Coupling](03-rotation-and-length-of-day.md) —
  the other global mode family: the rotation.
- [12-01 Seismic Structure of the Earth](../01-seismic-structure-of-the-earth/README.md) —
  the reference models whose synthetic analogue is used here.
- [02-03 Oscillations and Waves](../../02-physics/03-oscillations-and-waves/README.md) —
  the discrete normal-mode theory this lesson makes continuous.
- [12-06 Geodetic Constraints on the Interior](../06-geodesy-constraints-interior/README.md) —
  the independent constraints that break the $T \propto R/\alpha$ degeneracy.
- [19-numerical-modeling-hpc](../../19-numerical-modeling-hpc/README.md) —
  large sparse eigenvalue problems of the kind a real mode catalog needs.
