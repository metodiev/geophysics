---
id: 02-04-01
title: "Stress: Traction, Cauchy Stress Tensor and Equilibrium"
level: advanced
prereqs: ["02-03-05", "01-06-05", "01-07-06"]
estimated_minutes: 90
tags: [stress, cauchy-tensor, continuum-mechanics, mohr-circle]
---

# Stress: Traction, Cauchy Stress Tensor and Equilibrium

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** traction, and derive Cauchy's formula
   $t_i = \sigma_{ij}n_j$ from the balance of forces on a tetrahedron.
2. **State** why the stress tensor is symmetric, and what assumption that
   symmetry depends on.
3. **Derive** the equilibrium condition $\nabla\cdot\boldsymbol{\sigma} +
   \mathbf{f} = \mathbf{0}$ and explain its relation to Newton's second law.
4. **Diagonalise** the stress tensor, interpret the principal stresses and
   directions, and compute the three invariants.
5. **Decompose** a stress state into hydrostatic and deviatoric parts and explain
   why the two drive different physics.
6. **Compute** lithostatic and effective stress at depth, and state the
   pore-pressure assumption being made.
7. **Verify** every one of these numerically, including the Mohr-circle
   construction and the invariant identities.

## Prerequisites

- [02-03-05 Deriving the Wave Equation from Continuum Physics](../03-oscillations-and-waves/05-wave-equation-derivation.md)
  — the continuum hypothesis and the divergence form of a conservation law.
- [01-06-05 Line and Surface Integrals; Flux and Circulation](../../01-mathematics/06-multivariable-calculus/05-line-surface-integrals.md)
  — surface integrals and flux, needed for the traction and equilibrium arguments.
- [01-07-06 Eigenvalues, Eigenvectors and Diagonalisation](../../01-mathematics/07-linear-algebra/06-eigenvalues.md)
  — the symmetric eigenvalue problem.

## 1. Why stress, and not force

A force is a vector attached to a point. The load on a volume of rock is
distributed over its surfaces and its interior, and the same load produces
different effects depending on how it is applied: a block squeezed uniformly
changes volume; squeezed in one direction and held in another, it changes shape;
sheared, it may slide. To say what a material *feels* — and therefore what it does
— requires a quantity that describes the load on every plane through a point.

That quantity is the stress tensor, and the defining insight is that the traction
(force per unit area) on a plane depends on the plane's orientation. Because the
dependence is linear in the normal vector, nine numbers at a point determine the
traction on *every* plane through it. That is Cauchy's theorem, and it is why
stress is a second-rank tensor and not three vectors.

## 2. Precise definitions

**Traction.** The force per unit area exerted *by* the material on the positive
side of a surface *on* the material on the negative side:
$\mathbf{t}(\mathbf{x},\mathbf{n})$, with units Pa. The argument $\mathbf{n}$ is
the unit normal to the surface, and the traction changes sign with $\mathbf{n}$:
$\mathbf{t}(\mathbf{x},-\mathbf{n}) = -\mathbf{t}(\mathbf{x},\mathbf{n})$.

**Cauchy stress tensor.** The second-rank tensor $\boldsymbol{\sigma}$ defined by

$$t_i = \sigma_{ij}n_j \qquad\text{(summation implied)} . \tag{1}$$

$\sigma_{ij}$ is the $i$-th component of traction on the plane whose normal is the
$j$-th coordinate direction. In geophysics, compressive stress is conventionally
**positive** (depth is positive downwards), which is the opposite of the
solid-mechanics convention; state the convention in every calculation.

**Principal stresses.** The eigenvalues $\sigma_1\ge\sigma_2\ge\sigma_3$ of
$\boldsymbol{\sigma}$; the corresponding eigenvectors are the principal
directions, on which the traction is purely normal.

**Invariants.** Combinations unchanged by rotation:
$I_1 = \operatorname{tr}\boldsymbol{\sigma}$,
$I_2 = \tfrac12[(I_1)^2 - \operatorname{tr}(\boldsymbol{\sigma}^2)]$,
$I_3 = \det\boldsymbol{\sigma}$.

**Mean (hydrostatic) stress.** $p = I_1/3$; in the compression-positive
convention this is the confining pressure.

**Deviatoric stress.** $\boldsymbol{\sigma}' =
\boldsymbol{\sigma} - \tfrac13I_1\mathbf{I}$, with $\operatorname{tr}
\boldsymbol{\sigma}' = 0$.

**Effective stress.** $\boldsymbol{\sigma}^{\text{eff}} =
\boldsymbol{\sigma} - p_f\mathbf{I}$ with $p_f$ the pore-fluid pressure; it is the
effective stress, not the total stress, that controls frictional sliding and
fracture.

## 3. Derivations

### 3.1 Cauchy's formula from a tetrahedron

Consider a small tetrahedron with three faces normal to the coordinate axes and a
fourth with unit normal $\mathbf{n}$ and area $A$. The three coordinate faces have
areas $A n_1$, $A n_2$, $A n_3$ (the projections of the oblique face), and their
tractions are $-\boldsymbol{\sigma}^{(1)}$, $-\boldsymbol{\sigma}^{(2)}$,
$-\boldsymbol{\sigma}^{(3)}$ (with the minus because their outward normals are in
the negative coordinate directions).

Balance of forces, including inertia and a body force $\mathbf{f}$ per unit volume:

$$\mathbf{t}(\mathbf{n})A - \sigma_{ij}\mathbf{e}_i\,An_j + \mathbf{f}V
= \rho V\,\mathbf{a} . \tag{2}$$

The volume $V$ scales as $h^3$ while the surface terms scale as $h^2$, so
dividing by $A$ and taking $h\to0$:

$$t_i = \sigma_{ij}n_j , \qquad\text{i.e.}\qquad
\mathbf{t}(\mathbf{n}) = \boldsymbol{\sigma}\mathbf{n} . \tag{3}$$

This is Cauchy's theorem. Three consequences to note:

- **Linearity.** The traction depends linearly on $\mathbf{n}$, which is exactly
  the statement that nine numbers determine it everywhere. No assumption about the
  material has been made: equation (3) is kinematics, true for any continuum.
- **Sign convention.** Equation (3) gives the traction on the positive side.
- **No stress without a surface.** Stress is not a property of a point alone; it
  needs the plane to be specified, and the sensor (a borehole wall, a fracture) is
  what specifies it.

### 3.2 Symmetry of the stress tensor

Take a small cube and balance angular momentum about its centre. The body couple
is zero (no internal torque density is assumed) and the surface couples are the
moments of the tractions on the six faces. The moment of a traction $t$ on a face
at distance $h/2$ scales as $t\,h^2\,h$, and equating the three components of the
couple gives

$$\sigma_{ij} = \sigma_{ji} . \tag{4}$$

The assumption is that there is **no couple stress** — no internal torque that
material elements can transmit independently of force. For ordinary rocks at
ordinary strain rates this is excellent; for media with strongly coupled
microstructure (a suspension of magnetic grains, certain liquid crystals,
granular media at very short times) it fails, and the stress tensor acquires an
antisymmetric part. Also note that the standard derivation is quasi-static: for
rapidly rotating bodies, or in the presence of strong rotation, a more careful
statement is required.

### 3.3 Equilibrium and the equation of motion

Apply the divergence theorem to the force on a volume $V$ with surface $S$:

$$\int_S t_i\,dS = \int_S\sigma_{ij}n_j\,dS = \int_V \partial_j\sigma_{ij}\,dV . \tag{5}$$

Adding the body force $\int_V\rho g_i\,dV$ and equating the total force to the rate
of change of momentum gives, since $V$ is arbitrary,

$$\partial_j\sigma_{ij} + \rho g_i = \rho\ddot u_i , \qquad
\text{and in equilibrium}\qquad
\partial_j\sigma_{ij} + \rho g_i = 0 . \tag{6}$$

Two readings of the same equation are worth keeping side by side:

- **Statics:** the divergence of the stress plus the body force vanishes. This is
  the equation solved by a lithospheric stress model.
- **Dynamics:** the same equation with an acceleration term is the equation of
  motion of a deformable body, and combining it with a constitutive law produces
  the wave equation. This is the route taken in lesson 02-04-05, and it is the
  reason the derivation of the P- and S-wave speeds starts here.

### 3.4 Principal stresses and invariants

Since $\boldsymbol{\sigma}$ is real symmetric, it has three real eigenvalues and
an orthonormal eigenbasis. In that basis the matrix is diagonal and the traction on
the principal plane $\mathbf{n} = \mathbf{v}^{(k)}$ is
$\mathbf{t} = \sigma_k\mathbf{v}^{(k)}$: purely normal, with zero shear. The
eigenvalue problem is

$$\left(\boldsymbol{\sigma} - \sigma\mathbf{I}\right)\mathbf{v} = \mathbf{0},
\qquad
\det\left(\boldsymbol{\sigma}-\sigma\mathbf{I}\right) = 0 , \tag{7}$$

a cubic whose roots are the three principal stresses. Its coefficients are the
invariants:

$$\sigma^3 - I_1\sigma^2 + I_2\sigma - I_3 = 0 . \tag{8}$$

Because the coefficients are rotation-invariant, so are the principal stresses —
which is the statement that the *state* of stress is a physical property while the
components are representation-dependent.

Two bounds that the demo verifies numerically:

$$I_1/3 - \frac{2}{\sqrt3}\sqrt{J_2} \le \sigma \le I_1/3 +
\frac{2}{\sqrt3}\sqrt{J_2} \ \ \text{for the principal values, and} \qquad
\sigma_3 \le \sigma_n \le \sigma_1 \tag{9}$$

for the normal stress $\sigma_n = \mathbf{t}\cdot\mathbf{n}$ on *any* plane. The
second inequality is intuitive — a projection cannot exceed the largest eigenvalue
— and it is a useful sanity check on a computed stress state.

### 3.5 Hydrostatic and deviatoric decomposition

Write

$$\boldsymbol{\sigma} = \frac{I_1}{3}\mathbf{I} + \boldsymbol{\sigma}' , \qquad
\operatorname{tr}\boldsymbol{\sigma}' = 0 . \tag{10}$$

The two parts do different physics, and the separation is not cosmetic:

- The **isotropic** part is the pressure. In a fluid it is the entire stress; in a
  solid it changes volume (through the bulk modulus) and, in a porous rock,
  controls the effective stress.
- The **deviatoric** part changes shape. It is what drives shear failure, plastic
  flow and seismic anisotropy from aligned cracks. It also produces the shear wave
  in an elastic solid.

The magnitude of the deviatoric part is measured by the second invariant

$$J_2 = \tfrac12\sigma'_{ij}\sigma'_{ij} ,
\qquad
\sigma_{\text{vM}} = \sqrt{3J_2} \tag{11}$$

(the von Mises equivalent stress). A rock at 10 km depth carries a lithostatic
pressure well over 200 MPa, but the *deviatoric* stress it can support before
failing is of order tens of MPa — which is why the two parts must be tabulated
separately.

## 4. Physical interpretation

**Stress has no direction; traction does.** The stress tensor is a linear machine
that converts a direction into a force per unit area. Asking "what is the stress
here?" without specifying a plane is asking a question with no answer — the same
question as asking for the projection of a vector without naming the axis.

**Principal axes are the natural axes of a stress state.** On them there is no
shear. Real faults are not principal planes of the regional stress, which is why
they slip: the shear traction on a pre-existing plane is what drives motion
(lesson 02-04-08).

**The invariants are what a material feels.** A constitutive law cannot depend on
the coordinate system, so it can only depend on invariants (or on the tensor in a
rotation-covariant way). This is why isotropic elasticity has two independent
constants, and why failure criteria are written in terms of $I_1$ and $J_2$.

**Pressure and differential stress are decoupled in their effects.** Increasing
confining pressure raises the stress needed to fail a rock, because it raises the
normal stress on every potential plane; increasing the differential stress drives
failure. The two knobs are experimentally separate, and that separation is the
basis of rock-mechanics testing.

## 5. Assumptions and regime of validity

| Assumption | Statement | What breaks outside it |
|---|---|---|
| Continuum | A traction can be defined over an area element of size $a \gg$ microstructure | At grain scale the traction is not a smooth field; the stress tensor is an average |
| No couple stress | No internal torque density | Granular, magnetic and liquid-crystalline media at short times acquire an antisymmetric part |
| Quasi-static balance for symmetry | Rotational inertia negligible | Rapidly rotating bodies need a more careful statement (usually a negligible correction for the Earth's rotation at seismic frequencies) |
| Cauchy stress exists and is bounded | Traction is continuous in $\mathbf{n}$ | Materials with long-range forces (some electro-elastic couplings) require non-local descriptions |
| Pore pressure is a scalar | The fluid pressure is isotropic | Anisotropic permeability or partial saturation at low frequency can make the effective stress more complicated |

**Convention warning.** This curriculum uses compression-positive, depth-positive
stress, as is standard in geophysics. Textbooks on solid mechanics and on rock
mechanics differ, and the sign of every shear component on a Mohr diagram depends
on the convention. State the convention before writing a single equation.

## 6. Units and dimensional analysis

- $\sigma_{ij}$: Pa (N m⁻²) = kg m⁻¹ s⁻². In geophysics, MPa and GPa are the
  working units: 1 MPa = 10⁶ Pa, 1 GPa = 10⁹ Pa.
- $t_i$: Pa, the same as stress, since $n_j$ is dimensionless ✓.
- Equation (6): $\partial_j\sigma_{ij}$ has units Pa m⁻¹ =
  kg m⁻² s⁻², which is a force per unit volume ✓, matching $\rho g_i$ with
  $\rho g$ = kg m⁻³ × m s⁻² = kg m⁻² s⁻² ✓. A quick check that catches the common
  error of forgetting $\rho$ in the body-force term.
- $J_2$: Pa², so $\sqrt{3J_2}$ is a stress ✓.
- Lithostatic gradient: $\rho g$ = 2700 × 9.81 = 26.5 kPa m⁻¹ = 26.5 MPa km⁻¹ —
  a number worth memorising, with the caveat that it is a model gradient for
  constant density.

## 7. Python demonstration

[`code/stress_demo.py`](./code/stress_demo.py) computes tractions, principal
stresses, the Mohr circle and the lithostatic profile. Observed output for the
stress tensor (MPa) with components 120, 30, 0 / 30, 70, −15 / 0, −15, 40:

```text
principal stresses (MPa): s1 = 134.490566, s2 = 63.586042, s3 = 31.923392
                  normal n                      t (MPa)        |t|        t_n      |t_s|
             (1, 0, 0) / 1 ( 120.000,   30.000,    0.000)   123.6932   120.0000    30.0000
             (0, 1, 0) / 1 (  30.000,   70.000,  -15.000)    77.6209    70.0000    33.5410
         (1, 1, 1) / 1.732 (  86.603,   49.075,   14.434)   100.5816    86.6667    51.0446
```

```text
 axis  eigenvalue (MPa)               traction (MPa)         t_n      |t_s|  1^T sigma 1
    1        134.490566 (-120.8157, -58.3563,   9.2638)  134.490566   2.70e-06  1.000000000
    2         63.586042 ( 26.0319, -48.9522,  31.1321)   63.586042   9.54e-07  1.000000000
    3         31.923392 (  5.0890, -14.9409, -27.7484)   31.923392   0.00e+00  1.000000000

invariants from the components:  I1 = 230.000000, I2 = 14875.000000, I3 = 273000.000000
invariants from the eigenvalues: I1 = 230.000000, I2 = 14875.000000, I3 = 273000.000000
mean stress = I1/3 = 76.666667 MPa; deviatoric second invariant J2 = 2758.333333 MPa^2
von Mises equivalent stress = sqrt(3 J2) = 90.967027 MPa
```

```text
Mohr circle centre = 80.000000 MPa, radius = 50.000000 MPa
max deviation from the circle radius = 7.105e-15 MPa
maximum shear over all planes = radius = 50.000000 MPa, = (s1 - s3)/2 with s1 = 130.000000, s3 = 30.000000 MPa
```

```text
 depth (km)  sigma_v (MPa)   p_f (MPa)  sigma_v_eff (MPa)
        1.0         26.487       9.810             16.677
       10.0        264.870      98.100            166.770
       30.0        794.610     294.300            500.310
```

### What to observe

| Observation | Consequence |
|---|---|
| The principal-plane shear stresses are $10^{-6}$ to $10^{-7}$ MPa, i.e. round-off | The eigenvectors really are principal directions; a large residual would indicate an eigen-solver or indexing error |
| The invariants agree between the component and eigenvalue routes to all printed digits | Invariance is exact and is therefore the best numerical test of a diagonalisation |
| $\sigma_3 \le \sigma_n \le \sigma_1$ holds in the traction table (86.67 MPa lies between 31.92 and 134.49) | The projection bound of equation (9) is verified; any tractions outside it indicate a sign error |
| Every scanned plane lies on the Mohr circle to $7\times10^{-15}$ MPa | The Mohr-circle construction is exact for a 2-D state; it is a rotation of coordinates, not an approximation |
| The maximum shear stress equals the circle radius, 50 MPa | The maximum shear over all planes is $(\sigma_1-\sigma_3)/2$, which is the criterion used in failure analysis |
| The lithostatic gradient is 26.5 MPa km⁻¹ and the effective gradient with hydrostatic pore pressure is 16.7 MPa km⁻¹ | The effective stress is about 63 per cent of the total here; using the total stress in a failure calculation overestimates the strength by 60 per cent |

> **Breaking exercise.** Change one off-diagonal component of the stress tensor by
> a factor of two and predict, before running, how the number of Mohr circles
> changes and whether the three principal stresses remain distinct. Then explain
> the answer in terms of the cubic (8).

## 8. Common mistakes

1. **Mixing sign conventions.** Compression-positive versus tension-positive
   flips the sign of every normal component and changes the appearance of a Mohr
   diagram.
2. **Forgetting that traction needs a plane.** Quoting "the stress" as though it
   were a vector is a category error.
3. **Assuming the vertical stress is a principal stress everywhere.** It is a
   principal stress on a flat, laterally homogeneous Earth; on a slope, or near a
   fault, the principal axes are tilted.
4. **Using total stress in a failure criterion.** Effective stress controls
   sliding and fracture; the error can be tens of per cent.
5. **Treating the principal stresses as the stresses on a fault.** A fault plane
   is generally *not* a principal plane; the shear traction on the fault is what
   matters (lesson 02-04-08).
6. **Confusing the invariants $I_2$ and $J_2$.** $I_2$ contains the mean stress;
   $J_2$ is purely deviatoric and is the one in failure criteria.
7. **Assuming the lithostatic gradient is universal.** $\rho g$ with a constant
   density is a model; real density increases with depth and pore pressure is
   often not hydrostatic.
8. **Ignoring the symmetry assumption.** For ordinary rocks it is safe; for the
   media listed in §5 it is not, and the statement of the assumption is part of a
   correct derivation.

## 9. Real-world applications

- **In-situ stress estimation.** Borehole breakouts, drilling-induced fractures
  and focal mechanisms all give information about the orientation of the principal
  stresses; combining them is the standard approach in the petroleum and
  geothermal industries (see
  [05-core-geophysics](../../05-core-geophysics/README.md)).
- **Earthquake mechanics.** The shear and normal tractions on a fault plane, from
  the regional stress tensor and the pore pressure, determine the Coulomb failure
  function; mapping that function is how stress triggering is assessed (see
  [06-seismology](../../06-seismology/README.md)).
- **Borehole stability and mud-weight design.** The stress concentration around a
  borehole (Kirsch solution) sets the mud weight window between breakout and
  fracture — a direct application of Cauchy's formula on a curved surface.
- **Reservoir compaction and subsidence.** The effective-stress change from
  depletion produces compaction, which is a poroelastic problem whose first step
  is the decomposition (10).
- **Tectonic stress maps.** The World Stress Map is a compilation of stress
  orientations from many indicators; interpreting it requires the invariants and
  the convention statements of this lesson.
- **Rock testing.** A triaxial test controls $\sigma_3$ (confining pressure) and
  measures the $\sigma_1$ at failure; the result is a Mohr-Coulomb envelope in the
  Mohr plane, which is the subject of lesson 02-04-08.

## 10. Further reading

- **Jaeger, J. C., Cook, N. G. W., & Zimmerman, R. W. *Fundamentals of Rock
  Mechanics* (Blackwell).** The best treatment at this level: stress, strain,
  failure and in-situ stress measurement, with the geological conventions made
  explicit. Level: advanced.
- **Fung, Y. C. *A First Course in Continuum Mechanics* (Prentice-Hall).** A
  rigorous derivation of Cauchy's theorem, the symmetry argument and the
  equations of motion. Level: advanced.
- **Truesdell, C., & Toupin, R. *The Classical Field Theories* (in *Handbuch der
  Physik*, Vol. III/1).** The canonical treatment of the foundations; consult for
  the couple-stress caveat. Level: graduate.
- **Turcotte, D. L., & Schubert, G. *Geodynamics* (Cambridge University Press).**
  Lithospheric stress states and their tectonic consequences. Level: advanced.
- **Zoback, M. D. *Reservoir Geomechanics* (Cambridge University Press).** The
  applied version: in-situ stress, borehole failure and fault stability, with
  worked field examples. Level: advanced.
- **Engelder, T. *Stress Regimes in the Lithosphere* (Princeton University
  Press).** Stress indicators and their interpretation. Level: advanced.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 11. Related lessons

- [02 Strain: Infinitesimal Strain Tensor and Compatibility](./02-strain.md) —
  the kinematic partner of this lesson.
- [03 Constitutive Laws and Generalised Hooke's Law](./03-constitutive-laws.md) —
  how stress and strain are related.
- [05 Elastodynamic Equation of Motion and Wave Speeds](./05-elastodynamics.md) —
  where the equilibrium equation (6) becomes a wave equation.
- [08 Rock Failure, Fracture and Rate-State Friction](./08-failure-and-friction.md)
  — where the Mohr circle meets a failure envelope.
- [02-03-05 Deriving the Wave Equation from Continuum Physics](../03-oscillations-and-waves/05-wave-equation-derivation.md)
  — the one-dimensional version of the machinery used here.
- [01-06-06 Gauss, Stokes and Green Theorems](../../01-mathematics/06-multivariable-calculus/06-integral-theorems.md)
  — the divergence theorem used in §3.3.

Exercises:
[`exercises/01-stress-exercises.md`](./exercises/01-stress-exercises.md) and
[`exercises/01-stress-solutions.md`](./exercises/01-stress-solutions.md).

## Self-assessment checklist

- [ ] I can define traction and derive Cauchy's formula from a tetrahedron.
      (Section 3.1)
- [ ] I can state the assumption behind the symmetry of the stress tensor and give
      a medium that violates it. (Section 3.2)
- [ ] I can derive the equilibrium equation from the divergence theorem.
      (Section 3.3)
- [ ] I can diagonalise a stress tensor and interpret the results physically.
      (Section 3.4)
- [ ] I can compute the three invariants and say which is used in failure
      criteria. (Sections 3.4, 3.5)
- [ ] I can decompose a stress state into hydrostatic and deviatoric parts and
      explain the different physics of each. (Section 3.5)
- [ ] I can compute lithostatic and effective stress at depth and state the
      pore-pressure assumption. (Sections 2, 7)
- [ ] I can state the sign convention I am using and explain why it matters.
      (Sections 2, 5)
