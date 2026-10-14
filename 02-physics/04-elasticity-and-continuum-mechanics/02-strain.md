---
id: 02-04-02
title: "Strain: Infinitesimal Strain Tensor and Compatibility"
level: advanced
prereqs: ["02-04-01", "01-06-03", "01-07-06"]
estimated_minutes: 90
tags: [strain, kinematics, compatibility, geodesy]
---

# Strain: Infinitesimal Strain Tensor and Compatibility

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the infinitesimal strain tensor and the rotation tensor by
   decomposing the displacement gradient, and state the small-strain assumption
   quantitatively.
2. **Compute** the volumetric strain, the principal strains and the maximum shear
   strain from a displacement field.
3. **Quantify** the failure of the small-strain approximation for a rigid rotation,
   and state the amplitude at which it matters.
4. **State** the Saint-Venant compatibility conditions, and explain why they
   matter when a strain field is *measured* rather than derived from a
   displacement.
5. **Estimate** the accuracy of a strain measurement from finite differences, and
   choose a differencing length for a given displacement precision.
6. **Verify** all of the above numerically, including a measured convergence order
   and a compatibility test that fails as it should.

## Prerequisites

- [02-04-01 Stress: Traction, Cauchy Stress Tensor and Equilibrium](./01-stress.md)
  — the co-tensor of this lesson; stress without strain cannot be interpreted.
- [01-06-03 Jacobians, Coordinate Transformations and Volume Elements](../../01-mathematics/06-multivariable-calculus/03-jacobians.md)
  — the displacement gradient, and volume change as a determinant.
- [01-07-06 Eigenvalues, Eigenvectors and Diagonalisation](../../01-mathematics/07-linear-algebra/06-eigenvalues.md)
  — principal strains.

## 1. Two questions, two tensors

A displacement field $\mathbf{u}(\mathbf{x})$ answers the question "where did each
point go?". It does not answer "what happened to the material?", because a rigid
translation and a rigid rotation move points without deforming anything. Strain is
what remains after the rigid-body motions are removed.

The decomposition is exact for the *gradient* of the displacement, and it is
worth writing once and using everywhere:

$$\frac{\partial u_i}{\partial x_j} = \underbrace{\varepsilon_{ij}}_{\text{strain}}
+ \underbrace{\omega_{ij}}_{\text{rotation}} , \qquad
\varepsilon_{ij} = \tfrac12\left(u_{i,j}+u_{j,i}\right), \qquad
\omega_{ij} = \tfrac12\left(u_{i,j}-u_{j,i}\right) . \tag{1}$$

The symmetric part is strain (nine components, six independent, symmetric); the
antisymmetric part is rotation (three independent components, equivalent to a
pseudo-vector). The split is unique, and it is why the strain tensor has six
independent components rather than nine.

## 2. Precise definitions

**Infinitesimal strain tensor.**
$\varepsilon_{ij} = \tfrac12(u_{i,j}+u_{j,i})$, dimensionless.

**Rotation tensor.** $\omega_{ij} = \tfrac12(u_{i,j}-u_{j,i})$, with the
associated rotation vector $\boldsymbol{\omega} = \tfrac12\nabla\times\mathbf{u}$
whose magnitude is the angle of local rigid rotation (a small angle in the
infinitesimal theory).

**Dilatation (volumetric strain).** $\Delta = \operatorname{tr}\boldsymbol{\varepsilon}
= u_{i,i} = \nabla\cdot\mathbf{u}$: the fractional volume change.

**Principal strains.** The eigenvalues $\varepsilon_1 \ge \varepsilon_2 \ge
\varepsilon_3$ (these can be of either sign; positive is extension in the
geophysical convention adopted here, and the convention must be stated).

**Compatibility conditions.** The differential relations that a symmetric tensor
field must satisfy to be the strain field of some single-valued displacement:
in 2-D, $\varepsilon_{xx,yy} + \varepsilon_{yy,xx} = 2\varepsilon_{xy,xy}$; in
3-D there are six independent conditions.

**Finite strain.** Any measure that is exact for large deformations — the Green
(Lagrangian) strain, the Eulerian strain, or the principal stretches. Needed when
$|\nabla\mathbf{u}|$ is not much less than 1.

## 3. Derivations

### 3.1 Strain from neighbouring points

Take two material points separated by $\delta\mathbf{x}$ in the reference state.
After deformation the separation is

$$\delta u_i = u_i(\mathbf{x}+\delta\mathbf{x}) - u_i(\mathbf{x})
\approx \frac{\partial u_i}{\partial x_j}\delta x_j
= \left(\varepsilon_{ij}+\omega_{ij}\right)\delta x_j . \tag{2}$$

The change in the *length* of the separation,

$$|\delta\mathbf{x}+\delta\mathbf{u}|^2 - |\delta\mathbf{x}|^2
\approx 2\delta x_i\varepsilon_{ij}\delta x_j , \tag{3}$$

depends only on the symmetric part: the antisymmetric part contributes nothing to
the first order. So **strain is what changes lengths and angles; rotation is what
does not.** That is the fundamental reason for the symmetrisation in equation (1).

### 3.2 Dilatation and the Jacobian

The volume of a small parallelepiped transforms with the Jacobian determinant. To
first order,

$$J = \det\left(\delta_{ij}+u_{i,j}\right) = 1 + u_{i,i} + O(\|\nabla\mathbf u\|^2)
= 1 + \Delta + \cdots , \tag{4}$$

so $\Delta = \nabla\cdot\mathbf{u}$ is the fractional volume change. Two
consequences:

- **Incompressible flow** has $\Delta = 0$ identically; the divergence-free
  condition is a kinematic statement about the velocity field, and for a solid
  this is the limit of infinite bulk modulus.
- **The S wave is dilatation-free** and the P wave is rotation-free, which is the
  kinematic content of lesson 02-04-05.

### 3.3 Principal strains and the strain ellipsoid

Because $\boldsymbol{\varepsilon}$ is real symmetric, it has an orthonormal
eigenbasis. In that basis the strain is diagonal and the deformation of a small
sphere is an ellipsoid whose semi-axes are $1+\varepsilon_k$. This is the **strain
ellipsoid**, and it is the geometric reading of the principal strains. The
maximum shear strain is $(\varepsilon_1-\varepsilon_3)/2$ — the strain analogue of
the maximum shear stress, and of the same form, because both tensors are symmetric.

### 3.4 The small-strain assumption, quantified

The infinitesimal tensor is the first-order term of an expansion in
$\|\nabla\mathbf u\|$. Its failure is easiest to see for a **rigid rotation**,
where the true strain is exactly zero for any angle. Rotating a body by angle
$\theta$ about the $z$-axis gives, at the point $(x,y)$,

$$u_x = x(\cos\theta-1) - y\sin\theta, \qquad
u_y = x\sin\theta + y(\cos\theta-1) . \tag{5}$$

The computed strain has

$$\varepsilon_{xx} = \frac{\partial u_x}{\partial x} = \cos\theta - 1
= -\frac{\theta^2}{2} + O(\theta^4) \tag{6}$$

and zero shear, so the infinitesimal theory reports a spurious *contraction* of
order $\theta^2/2$. The demo's numbers: $-1.52\times10^{-5}$ at 1° (relative to
$\theta^2/2 = 1.52\times10^{-4}$... the ratio is $-0.99997$), $-0.0341$ at 15° and
$-0.1340$ at 30°, i.e. a spurious 13 per cent contraction for a 30° rotation.

The practical rule: **the infinitesimal theory is valid when
$\|\nabla\mathbf u\| \ll 1$**, and its error is of order the square of the rotation
angle (or of the strain itself). Seismic waves satisfy this by many orders of
magnitude (strains of $10^{-6}$ or less); tectonic deformation over geological time
does not, which is why finite-strain formulations are used in structural geology
and in geodynamic modelling of large deformation.

### 3.5 Compatibility

Given a displacement field, the strain field automatically satisfies compatibility.
The converse question — given a strain field, does a displacement field exist? —
is answered by the **Saint-Venant compatibility conditions**. In two dimensions
there is one:

$$\frac{\partial^2\varepsilon_{xx}}{\partial y^2}
+\frac{\partial^2\varepsilon_{yy}}{\partial x^2}
= 2\frac{\partial^2\varepsilon_{xy}}{\partial x\partial y} . \tag{7}$$

In three dimensions there are six independent conditions, conventionally written

$$\varepsilon_{ij,kl}+\varepsilon_{kl,ij}-\varepsilon_{ik,jl}-\varepsilon_{jl,ik}
= 0 . \tag{8}$$

Why it matters in practice: modern geodesy *measures* strain, not displacement —
from GNSS velocities interpolated onto a grid, or from InSAR line-of-sight
displacements — and a measured strain field generally violates equation (7)
because of noise. If it is integrated to get a displacement, the answer depends on
the path of integration, which is algebraically the same statement as the
non-integrability of an inexact differential. The demo tests equation (7) on a
strain field derived from a displacement (residual at round-off, $0$ to
$2.8\times10^{-9}$) and on an arbitrary symmetric field (residual 0.4, i.e. it
fails). The lesson: **compatibility is a test that can fail, and therefore a test
worth running.**

### 3.6 Measuring strain by differencing

In practice strain is estimated from displacements at stations separated by $L$,
so

$$\varepsilon \approx \frac{\Delta u}{L} , \qquad
\sigma_\varepsilon \approx \frac{\sqrt2\,\sigma_u}{L} , \tag{9}$$

assuming independent station errors $\sigma_u$. Two features follow:

- **Longer baselines improve precision** linearly but average over more
  heterogeneity; the choice of $L$ is a trade-off between noise and resolution.
- **The error is dominated by the differencing, not by the measurement.** With
  $\sigma_u = 1$ mm and $L = 10$ km, $\sigma_\varepsilon \approx
  1.4\times10^{-7}$ — comparable with the strain accumulation rate of a plate
  boundary over a year, which is why decadal GNSS time series are needed for
  tectonic strain rates while coseismic strain is measurable with a single epoch.

The demo's finite-difference convergence test confirms the second-order accuracy
of the central difference: measured orders 2.000, 2.000, 2.000 for a smooth field
(the errors fall from $2.87\times10^{-8}$ at $h = 10^{-2}$ to
$4.48\times10^{-10}$ at $h = 1.25\times10^{-3}$, with the field scaled so the
strains are of order $10^{-3}$).

## 4. Physical interpretation

**Strain is a length ratio, and nothing else.** Every strain component can be read
as "the change in length per unit length, or the change in angle, of a small
element". Quantities of order $10^{-6}$ (seismic) to $10^{-2}$ (structural, over
geological time) are the working range.

**The strain ellipsoid is the picture.** Three principal axes, three principal
stretches; the deformation of a sphere into an ellipsoid. Structural geologists
read a deformed conglomerate in exactly this way, and the same tensor describes a
seismic wave's particle motion.

**Rotation and strain are separable.** This is why a GNSS network can measure
crustal strain even though the network is also rotating with the Earth and
translating with the plate: the tensor operations remove those motions by
construction.

**Compatibility is the statement that the pieces fit.** A strain field that
violates it cannot be produced by a continuous, single-valued displacement —
there is a dislocation, a crack or a measurement error in it. That makes
compatibility a powerful consistency test on geodetic data, and the inescapable
conclusion about observation errors when it fails.

## 5. Assumptions and regime of validity

| Assumption | Statement | What breaks outside it |
|---|---|---|
| Infinitesimal strain | $\|\nabla\mathbf u\| \ll 1$ | Error of order the square of the rotation/strain (§3.4); use finite strain |
| Small rotations | $|\boldsymbol{\omega}| \ll 1$ | Large rigid rotation contaminates the strain estimate; the split of equation (1) is no longer meaningful |
| Continuum | The displacement field is smooth at the scale of the differencing length | Grain-scale heterogeneity, fractures and faults make the field discontinuous; the measured "strain" is then an average including slip |
| Single-valued displacement | No dislocations or cracks inside the region | A fault inside the network makes the measured strain field incompatible, which is a signal, not an error |
| Elastic (for constitutive use) | Recoverable deformation | Permanent strain requires plasticity; the kinematic tensor is unchanged but the constitutive link is not |

## 6. Units and dimensional analysis

- $\varepsilon_{ij}$: dimensionless ✓. It is often quoted in microstrain
  (1 $\mu\varepsilon$ = $10^{-6}$) or in nanostrain; state which.
- $u_{i,j}$: dimensionless (m m⁻¹) ✓, as is $\omega_{ij}$.
- Equation (4): $J$ is dimensionless, so $\Delta$ must be ✓.
- Equation (7): each term is (dimensionless)/(length²), so the equation is
  dimensionally consistent ✓.
- Equation (9): $[\Delta u/L] = $ m m⁻¹ = dimensionless ✓, and $\sigma_u/L$ is the
  propagated error.
- Strain rates: s⁻¹, usually quoted in $\mu\varepsilon$/yr; a plate velocity of
  40 mm yr⁻¹ across a 100 km boundary is $4\times10^{-7}$ yr⁻¹ =
  1.3×10⁻¹⁴ s⁻¹.

## 7. Python demonstration

[`code/strain_demo.py`](./code/strain_demo.py) computes the strain and rotation
from a displacement field, measures the convergence order, demonstrates the
failure of the small-strain approximation and tests compatibility. Observed
output with $\mathbf u = 0.01(\sin(0.7x)\cos(1.1y),\ e^{0.4y}z,\ 0.1xy)$:

```text
point (x, y, z) = (1.3, -0.7, 2.1), central-difference step 1e-03
strain tensor (numeric):
   [  0.00308430,   0.00302281,  -0.00035000]
   [  0.00302281,   0.00634858,   0.00442892]
   [ -0.00035000,   0.00442892,   0.00000000]
max difference from the analytic strain = 6.096e-10
rotation vector w = (w_x, w_y, w_z) = (0.00312892, -0.00035000, 0.00302281)
dilatation = trace(strain) = 0.00943289
analytic dilatation = a cos(ax)cos(by) + c exp(cy) z = 0.00943289
```

```text
        h    max|error|    order
 1.00e-02     2.868e-08      nan
 5.00e-03     7.170e-09    2.000
 2.50e-03     1.792e-09    2.000
 1.25e-03     4.481e-10    2.000
```

```text
 theta (deg)    theta^2/2    apparent eps_xx    relative
         1.0     0.000152          -0.000152   -0.999975
        15.0     0.034269          -0.034074   -0.994301
        30.0     0.137078          -0.133975   -0.977361
        45.0     0.308425          -0.292893   -0.949641
```

```text
2-D compatibility condition: d2(exx)/dy2 + d2(eyy)/dx2 = 2 d2(exy)/dxdy
           point   residual, compatible   residual, arbitrary
  ( 0.30,  0.70)           0.000000e+00              0.400000
  ( 1.00, -0.50)           6.938894e-10              0.400000
  (-2.00,  1.50)           2.775558e-09              0.400000
```

### What to observe

| Observation | Consequence |
|---|---|
| The numerically differentiated strain matches the analytic value to $6\times10^{-10}$ | The central difference is accurate enough for the strains used in geophysics; the residual scales as $h^2$ |
| The measured convergence order is 2.000 in every row | The difference stencil is verified, not assumed — the standard required before trusting any numerically differentiated field |
| The dilatation equals the analytic trace to nine digits | The trace is a divergence and is computed robustly; it is the single most useful invariant of a strain field |
| A rigid rotation of 1° produces a spurious strain of $-1.5\times10^{-5}$ and 30° produces $-0.134$ | The small-strain error is $\theta^2/2$; a 30° rotation would be completely misinterpreted as a 13 per cent contraction |
| The compatible strain field passes the compatibility test at round-off ($10^{-10}$) | Compatibility is satisfied identically when the strain comes from a displacement; this is the control case |
| The arbitrary symmetric field fails with a residual of 0.4 | Compatibility is a real test with real discriminating power; a measured strain field that fails it either contains a dislocation (a fault) or is too noisy to integrate |

> **Breaking exercise.** Change the differencing step to $h = 1.0$ (a step
> comparable with the field's length scale) and predict, before running, both the
> sign and the rough magnitude of the error in the strain. Then explain why the
> error stops falling as $h^2$ in that regime.

## 8. Common mistakes

1. **Quoting a strain without a sign convention.** Extension-positive versus
   compression-positive reverses every normal strain; state it.
2. **Forgetting that the antisymmetric part contributes nothing to length
   changes.** Symmetrising is not a convenience; it is the definition.
3. **Using the infinitesimal tensor for a large rotation.** A 30° rotation gives a
   spurious 13 per cent strain, as the demo shows.
4. **Treating the dilatation as a strain component.** It is the *trace*, an
   invariant, not one of the six components.
5. **Integrating a measured strain field without testing compatibility.** The
   result is path-dependent; the correct response is to project the field onto a
   compatible subspace (a least-squares fit with constraints) before integrating.
6. **Using a differencing length shorter than the station spacing or the noise
   correlation length.** The estimated strain then measures noise, not deformation;
   and correlated errors do not average down as $1/\sqrt n$.
7. **Confusing the strain ellipsoid with the stress ellipsoid.** They have the same
   eigenvectors only for isotropic elasticity; in an anisotropic medium they do
   not align (lesson 02-04-06).
8. **Assuming a strain rate from one epoch.** Strain rate requires a time series;
   a single displacement measurement gives a coseismic offset, not a rate.

## 9. Real-world applications

- **GNSS and InSAR strain mapping.** Crustal deformation is measured as
  displacement at stations and converted to strain rate; the tensor is then
  inverted for fault slip or compared with a viscoelastic model. Archives:
  [UNAVCO / EarthScope](https://www.unavco.org),
  [EarthScope data](https://www.earthscope.org/data/).
- **Coseismic strain and Coulomb stress transfer.** The strain change from an
  earthquake is computed from a dislocation model, and converting it to a stress
  change (lesson 02-04-03) gives the Coulomb failure function used to assess
  aftershock triggering.
- **Structural geology.** Finite strain measurements in deformed rocks give the
  shape and orientation of the strain ellipsoid, from which the deformation path
  is inferred.
- **Seismic strain.** A seismic wave's amplitude is a strain (of order
  $10^{-6}$ for moderate ground motion), which is why strainmeters and
  fibre-optic sensing (DAS) measure displacement gradients directly.
- **Reservoir and geothermal engineering.** Induced deformation from fluid
  injection or extraction is monitored by InSAR and GNSS and interpreted through
  the strain field; the same tensor connects the observed surface movement to the
  subsurface volume change.
- **Glaciology.** Ice flow is a large-strain problem: the infinitesimal tensor is
  inadequate and the full deformation gradient is used, which is a good reminder
  that this lesson's approximation has a boundary.

## 10. Further reading

- **Jaeger, J. C., Cook, N. G. W., & Zimmerman, R. W. *Fundamentals of Rock
  Mechanics* (Blackwell).** Strain, strain rate and the geological measurement of
  strain, with the conventions stated. Level: advanced.
- **Fung, Y. C. *A First Course in Continuum Mechanics* (Prentice-Hall).** The
  rigorous derivation of the strain and rotation tensors, and of the compatibility
  conditions. Level: advanced.
- **Malvern, L. E. *Introduction to the Mechanics of a Continuous Medium*
  (Prentice-Hall).** Compatibility conditions in full three-dimensional form, with
  the derivation. Level: advanced.
- **Segall, P. *Earthquake and Volcano Deformation* (Princeton University Press).**
  Geodetic strain and its inversion for fault slip; the applied version of this
  lesson. Level: advanced.
- **Sokolnikoff, I. S. *Mathematical Theory of Elasticity* (McGraw-Hill).** The
  classical treatment, including Beltrami-Michell stress compatibility. Level:
  graduate.
- **Ramsay, J. G., & Huber, M. I. *The Techniques of Modern Structural Geology,
  Vol. 1: Strain Analysis* (Academic Press).** Finite strain measurement in rocks,
  the practical counterpoint to the infinitesimal theory. Level: advanced.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 11. Related lessons

- [01 Stress: Traction, Cauchy Stress Tensor and Equilibrium](./01-stress.md) —
  the co-tensor.
- [03 Constitutive Laws and Generalised Hooke's Law](./03-constitutive-laws.md) —
  how strain produces stress.
- [05 Elastodynamic Equation of Motion and Wave Speeds](./05-elastodynamics.md) —
  where the strain tensor appears in the wave equation.
- [02-03-05 Deriving the Wave Equation from Continuum Physics](../03-oscillations-and-waves/05-wave-equation-derivation.md)
  — the one-dimensional kinematics of the same kind.
- [01-06-03 Jacobians, Coordinate Transformations and Volume Elements](../../01-mathematics/06-multivariable-calculus/03-jacobians.md)
  — the determinant identity behind the dilatation.
- [07-gravity-geodesy](../../07-gravity-geodesy/README.md) — deformation measured
  from space.

Exercises:
[`exercises/02-strain-exercises.md`](./exercises/02-strain-exercises.md) and
[`exercises/02-strain-solutions.md`](./exercises/02-strain-solutions.md).

## Self-assessment checklist

- [ ] I can split a displacement gradient into strain and rotation and say what
      each does to a small element. (Section 3.1)
- [ ] I can compute the dilatation and relate it to the Jacobian. (Section 3.2)
- [ ] I can find the principal strains and interpret the strain ellipsoid.
      (Section 3.3)
- [ ] I can quantify the failure of the small-strain approximation for a rigid
      rotation. (Section 3.4)
- [ ] I can write the 2-D compatibility condition and explain what it tests.
      (Section 3.5)
- [ ] I can estimate the uncertainty of a strain from station displacements and
      state how the differencing length trades noise against resolution.
      (Section 3.6)
- [ ] I can state the four regimes in which the infinitesimal theory fails.
      (Section 5)
- [ ] I can name three geophysical measurements that produce a strain field and
      one that produces a strain rate. (Section 9)
