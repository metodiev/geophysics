# Module 02-08 — Potential Theory

**Stages:** advanced → doctoral · **Prerequisites:**
[01-06 Multivariable and Vector Calculus](../../01-mathematics/06-multivariable-calculus/README.md)
(gradients, flux integrals, the divergence theorem),
[01-06-08 Potential Fields, Laplace and Poisson Equations](../../01-mathematics/06-multivariable-calculus/08-potential-theory.md)
(the mathematical prerequisite, which this module does not repeat),
[01-07 Linear Algebra](../../01-mathematics/07-linear-algebra/README.md)
(orthogonality and projections, for the spherical harmonic coefficients),
[02-02 Classical Mechanics](../02-classical-mechanics/README.md) (conservative
forces, and the rotation of the Earth for the geoid lesson).

This module is the **mathematical engine of gravity and magnetic methods**. Every
gravity map, every satellite gravity model, every magnetic anomaly and every geoid
computed anywhere rests on the material here: the Newtonian potential, Laplace's
and Poisson's equations, the spherical harmonic expansion, the equivalence between
sources, and the uniqueness theorems that decide what a potential-field
measurement can and cannot determine.

The two features that distinguish this module from a mathematics treatment of the
same equations:

- **The physics is the point.** The mathematics module
  [01-06-08](../../01-mathematics/06-multivariable-calculus/08-potential-theory.md)
  establishes potential theory; this module uses it to answer physical questions —
  what a body's field looks like, what a level surface is, why the geoid is not an
  ellipsoid, and why the same field can be produced by infinitely many different
  mass distributions. Nothing here duplicates that lesson; everything here goes
  further into the physics.
- **Every claim is computed.** The six demonstrations implement the quadratures,
  the level-surface solves and the boundary-value relaxations from scratch in
  standard-library Python. Newton's shell theorem is verified by integrating a
  shell's field over its own surface *without using the theorem*; the
  non-uniqueness of the source is verified by constructing two genuinely different
  distributions whose fields agree to the quadrature floor. Every number quoted in
  the lessons is program output.

## Learning objectives

By the end of this module you will be able to:

1. **Derive** the potential and field of a point mass, a spherical shell, a uniform
   sphere, a point mass at depth and an infinite horizontal cylinder, and state the
   regime of validity of each.
2. **Prove** Newton's shell theorem from Gauss's law, and derive the linear
   interior profile of a uniform sphere.
3. **State and apply** the mean value property, the maximum principle and analytic
   continuation, and explain what each forbids physically.
4. **Separate** Laplace's equation in spherical coordinates, derive the multipole
   expansion, and compute the coefficients of a given body by orthogonality.
5. **Compute** $J_2$ for a homogeneous spheroid and interpret the Earth's value as
   a statement about the concentration of mass.
6. **Evaluate** the field of a general body: the prism closed form, superposition,
   the infinite-slab limit, and the equivalence of a body to a surface layer.
7. **Explain** the geoid as a level surface of the gravity potential, distinguish
   it from the reference ellipsoid, derive Bruns' formula and compute a deflection
   of the vertical.
8. **Prove** uniqueness of the exterior Dirichlet and Neumann problems, include the
   regularity condition correctly, and derive the exterior Neumann existence
   condition.
9. **Derive** the corollary that uniqueness of the field does not imply uniqueness
   of the source, construct the equivalent stratum, and explain why
   potential-field inversion is fundamentally non-unique.

## Lessons

| # | Lesson | Level | Key idea |
|---|---|---|---|
| 01 | [Newtonian Gravitational Potential and Field](./01-gravitational-potential.md) | advanced | $V = GM/r$; the shell theorem; the anomaly profile is a *centre*-depth profile |
| 02 | [Laplace's Equation and Harmonic Functions](./02-laplace-equation.md) | advanced | In a source-free region there is no potential maximum to find |
| 03 | [Spherical Harmonics and Multipole Expansions](./03-spherical-harmonics.md) | graduate | **The mastery lesson**: degree = wavelength = depth, and $J_2$ is a mass moment |
| 04 | [Poisson's Equation and Source Distributions](./04-poisson-equation.md) | advanced | Superposition is exact; so is source equivalence |
| 05 | [Equipotential Surfaces, Geoid and Level Surfaces](./05-equipotentials.md) | graduate | The geoid is a level surface; an ellipsoid is a convention |
| 06 | [Uniqueness Theorems and Boundary Conditions](./06-uniqueness-theorems.md) | graduate | The field is unique, the source is not — and the null space is infinite |

## Suggested path

**If you are working through the physics folder in order:** all six lessons in
numeric order, with lesson 06 read twice. Lessons 01, 02 and 04 form the core
derivation chain; lesson 03 is the basis for every global model; lesson 05 is
where the physics becomes geodesy; lesson 06 is where it becomes inverse theory.

**If you are here for gravity and geodesy:** read
[01](./01-gravitational-potential.md) §3, [02](./02-laplace-equation.md) §3,
[03](./03-spherical-harmonics.md) in full, then
[05](./05-equipotentials.md) in full. That is the shortest route to reading a
gravity model or a geoid computation critically. Then read
[06](./06-uniqueness-theorems.md) before you interpret anything.

**If you are here for magnetics:** read [02](./02-laplace-equation.md) §3.2–3.6,
[03](./03-spherical-harmonics.md) §3.2–3.4, then
[04](./04-poisson-equation.md) §3.5 (the surface-charge equivalence) and
[06](./06-uniqueness-theorems.md) (the ambiguity, which is worse for magnetics
because of remanence).

**If you are here for inverse theory:** read
[06](./06-uniqueness-theorems.md) in full and treat
[01](./01-gravitational-potential.md) and [04](./04-poisson-equation.md) as the
forward operator it analyses. The equivalent stratum of §3.5 is the canonical
example of a non-trivial null space in all of geophysics.

**If you already have a mathematics background:** attempt ★★★9–10 of
[01](./exercises/01-gravitational-potential-exercises.md),
★★★9–10 of [03](./exercises/03-spherical-harmonics-exercises.md) and
★★★9–10 of [06](./exercises/06-uniqueness-theorems-exercises.md) first. If those
come out cleanly, use lessons 01, 02, 04 and 05 as reference.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-gravitational-potential.md`](./01-gravitational-potential.md) … [`06-uniqueness-theorems.md`](./06-uniqueness-theorems.md) | The six lessons |
| [`exercises/01-gravitational-potential-exercises.md`](./exercises/01-gravitational-potential-exercises.md) | Exercises for lesson 01, including the shell-theorem and half-width problems |
| [`exercises/01-gravitational-potential-solutions.md`](./exercises/01-gravitational-potential-solutions.md) | Full worked solutions |
| [`exercises/02-laplace-equation-solutions.md`](./exercises/02-laplace-equation-solutions.md) | Worked solutions including the mean-value expansion and the maximum-principle counterexample |
| [`exercises/03-spherical-harmonics-solutions.md`](./exercises/03-spherical-harmonics-solutions.md) | Worked solutions including the Legendre recurrence and the $J_2$ computation |
| [`exercises/04-poisson-equation-solutions.md`](./exercises/04-poisson-equation-solutions.md) | Worked solutions including the prism formula and the magnetic equivalence |
| [`exercises/05-equipotentials-solutions.md`](./exercises/05-equipotentials-solutions.md) | Worked solutions including the level-surface solve and Bruns' formula |
| [`exercises/06-uniqueness-theorems-solutions.md`](./exercises/06-uniqueness-theorems-solutions.md) | Worked solutions including the exterior Neumann condition and the annihilator |
| [`code/newtonian_potential_demo.py`](./code/newtonian_potential_demo.py) | Point-mass $\mathbf{g} = \nabla V$; **Newton's shell theorem verified by surface quadrature**; the interior profile; point-mass-at-depth versus a finite sphere; the cylinder half-width |
| [`code/laplace_harmonic_demo.py`](./code/laplace_harmonic_demo.py) | Mean value property on and off the source; the maximum principle on a $41^3$ grid; the finite-difference Laplacian; anomaly sharpening with depth |
| [`code/spherical_harmonics_demo.py`](./code/spherical_harmonics_demo.py) | Legendre and associated Legendre functions checked against the Legendre equation; harmonic orthonormality; the multipole series; $J_2$ of a spheroid |
| [`code/poisson_sources_demo.py`](./code/poisson_sources_demo.py) | Superposition, the prism closed form versus quadrature, the slab limit, the magnetic surface-charge equivalence, the thin-body/surface-layer equivalence |
| [`code/equipotential_geoid_demo.py`](./code/equipotential_geoid_demo.py) | Level surfaces of a rotating Earth; flattening and the ellipsoid fit; $J_2$ from the defining data; Bruns' formula; deflection of the vertical |
| [`code/uniqueness_demo.py`](./code/uniqueness_demo.py) | Dirichlet uniqueness by relaxation from two starting points; **the equivalent stratum and the annihilator**; the slab ambiguity |

Every script is standard-library Python, prints its own summary of measured
agreements, and can be run directly:

```text
python3 02-physics/08-potential-theory/code/newtonian_potential_demo.py
```

## Key results, with the numbers the demonstrations produce

| Result | Measured agreement |
|---|---|
| $\mathbf{g} = \nabla V$ for a point mass | relative error $1.0\times10^{-8}$ (central differences) |
| Shell theorem, exterior: $\lvert\mathbf{g}\rvert = GM/r^2$ | worst relative error $5.0\times10^{-15}$ |
| Shell theorem, interior: field vanishes | worst value $2.1\times10^{-15}$ of $GM/a^2$ |
| Interior of a uniform sphere: $g = \tfrac43\pi G\rho r$ | worst relative error $1.6\times10^{-6}$ |
| Cylinder half-width equals depth | $x_{1/2}/h = 1.0000000000$ |
| Mean value property, source-free | relative difference $1.0\times10^{-13}$ |
| Mean value property, source enclosed | relative difference $0.7500$ (fails) |
| Finite-difference Laplacian, harmonic field | residual falls by $4.000$ per halving of $h$ |
| Spherical harmonic orthonormality | worst deviation $1.2\times10^{-14}$ |
| Uniform ball has only $l=0$ | $\lvert C_{l0}/C_{00}\rvert \le 5.2\times10^{-26}$ for $l \le 6$ |
| Homogeneous spheroid $J_2$ vs $(2f-f^2)/5$ | worst relative difference $3.0\times10^{-13}$ |
| Prism closed form vs volume quadrature | worst relative difference $4.2\times10^{-5}$ |
| Magnetised sphere: surface charge vs dipole | worst relative difference $3.2\times10^{-13}$ |
| Bruns' formula vs a solved level surface | worst relative difference $3.5\times10^{-5}$ |
| Dirichlet uniqueness, two starting fields | difference falls to $0$; series agreement $7.2\times10^{-3}$ |
| Equivalent stratum vs line mass | worst relative difference $3.1\times10^{-6}$ (quadrature-limited) |
| Annihilator's field | $2.0\times10^{-12}$ of the peak, while its density is twice the peak |

## Notation

| Symbol | Meaning |
|---|---|
| $V$ | gravitational potential, m$^2$ s$^{-2}$; $\mathbf{g} = \nabla V$ |
| $U$ | gravity potential (gravitation plus centrifugal) |
| $G$ | Newtonian constant of gravitation, $6.674\,30(15)\times10^{-11}$ m$^3$ kg$^{-1}$ s$^{-2}$, **measured** |
| $\rho$, $\sigma$, $\lambda$ | volume, areal and linear density |
| $M$, $GM_\oplus$ | mass; geocentric gravitational constant $3.986\,004\,418\times10^{14}$ m$^3$ s$^{-2}$, **defining** |
| $a$ | reference radius; also the WGS 84 semi-major axis $6\,378\,137$ m, **defining** |
| $f$ | flattening; WGS 84 quotes $1/f = 298.257\,223\,563$, **defining** |
| $\omega$ | angular velocity, $7.292\,115\times10^{-5}$ rad s$^{-1}$, **defining** |
| $Y_{lm}$, $P_l$, $P_l^m$ | spherical harmonics, Legendre and associated Legendre functions |
| $C_{lm}$, $J_l$ | dimensionless gravity field coefficients |
| $T$, $N$, $\gamma$ | disturbing potential, geoid undulation, normal gravity |
| $h$, $z_0$ | depth to a source |

Constants are cited from the
[constant handbook](../../26-reference-library/02-symbols-and-units/03-constant-handbook.md)
with its exact / measured / nominal classification respected: the WGS 84 datum
parameters are *defining* and may be quoted to all their digits; $G$ is *measured*
and must be quoted with its uncertainty; rock densities and mean terrestrial values
are *nominal* and are quoted as ranges or order-of-magnitude anchors with the model
assumption stated.

## What this module deliberately does not do

- It does not reproduce the mathematics module. It assumes
  [01-06-08](../../01-mathematics/06-multivariable-calculus/08-potential-theory.md)
  and goes further into the physics.
- It does not quote gravity or magnetic **coefficients**. Those are data and belong
  to the distributing services — [ICGEM](https://icgem.gfz-potsdam.de/) for gravity,
  [IGRF](https://www.ngdc.noaa.gov/IAGA/vmod/igrf.html) for the magnetic field.
  Where a value is used for comparison it is labelled as a measured input and the
  authoritative source is named.
- It does not treat measurement, instruments or reductions; those are
  [07-gravity-geodesy](../../07-gravity-geodesy/README.md) and
  [08-geomagnetism-electromagnetism](../../08-geomagnetism-electromagnetism/README.md).
- It does not develop the inverse theory itself; that is
  [18-inverse-problems](../../18-inverse-problems/README.md), for which lesson 06
  is the canonical geophysical example.
