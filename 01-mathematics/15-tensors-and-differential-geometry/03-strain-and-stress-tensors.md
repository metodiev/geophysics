---
id: 01-15-03
title: "Strain and Stress Tensors as Physical Tensors"
level: graduate
prereqs: ["01-15-02", "01-07-06", "01-06-01"]
estimated_minutes: 90
tags: [stress, strain, invariants, principal-axes]
---

# Strain and Stress Tensors as Physical Tensors

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** traction, the Cauchy stress tensor and the infinitesimal strain
   tensor, and state the sign and shear conventions you are using.
2. **Derive** the symmetry of the stress tensor from the balance of angular
   momentum, and say what physical assumption the derivation requires.
3. **Derive** the strain tensor from the change in length of a material line
   element, and explain why the antisymmetric part of the displacement gradient
   cannot appear.
4. **Compute** the principal values and principal axes of a stress state, and the
   three invariants, and state the physical meaning of each.
5. **Split** both tensors into isotropic and deviatoric parts, and interpret the
   split in terms of a rock's volumetric and shear response.
6. **Derive** and use the compatibility conditions, and explain what physical
   state an incompatible strain field would describe.

**Conventions used throughout, stated once.** Stress is **tension positive**, so
the traction on a face with outward unit normal $n_j$ is $t_i = \sigma_{ij}n_j$.
Strain is the **scientific** (tensorial) strain
$e_{ij} = \tfrac{1}{2}(u_{i,j} + u_{j,i})$, so the engineering shear strain is
$\gamma_{ij} = 2e_{ij}$ for $i \neq j$ and carries an extra factor of two. Many
rock-mechanics and earthquake-source texts use **compression positive** instead;
Section 5 states exactly what changes, and the demonstration verifies that the
quadratic invariants do not.

## Prerequisites

- [01-15-02 Tensor Algebra, Transformation Laws and Invariants](./02-tensor-algebra.md)
  — why these objects are tensors at all, and what their invariants mean.
- [01-07-06 Eigenvalues, Eigenvectors and Diagonalisation](../07-linear-algebra/06-eigenvalues.md)
  — the eigenproblem that produces principal stresses.
- [01-06-01 Partial Derivatives, Gradients and Directional Derivatives](../06-multivariable-calculus/01-partial-derivatives.md)
  — the derivative of a vector field, which is what a displacement gradient is.

## 1. Intuition: a vector on every plane

A force is not a stress. Stand on a rock: the rock does not care about your
weight, it cares about how much force each square metre of each oriented surface
must transmit. A surface has an orientation, and the force transmitted through it
depends on that orientation. The object that answers the question

> given any plane with unit normal $\hat n$, what force per unit area crosses it?

is the stress tensor. That is its definition, and everything else about it —
nine components, symmetry, principal axes — follows.

The first observation gives the mathematics. Fix a point and consider all planes
through it. The traction $\mathbf{t}$ depends linearly on $\hat n$, because the
forces on two adjacent area elements must add like the areas. A linear map from
vectors to vectors is a matrix: hence $\mathbf{t} = \boldsymbol{\sigma}\hat n$,
nine components, one tensor.

The second observation gives its symmetry. A small cube of rock would spin up
unless the stress field produced no net torque on it; the only way that can hold
for every cube is $\sigma_{ij} = \sigma_{ji}$, leaving six independent
components.

Strain is the same story told about deformation. If a displacement field
$\mathbf{u}(\mathbf{x})$ is present, the local linear map is the displacement
gradient $u_{i,j}$. Its symmetric part measures the change of *shape and size*;
its antisymmetric part measures *local rotation*, which is not a deformation at
all because it does not change any length. Splitting the gradient into those two
parts is not a mathematical trick: it is the definition of deformation, and it is
why strain has six independent components and rotation three.

## 2. Precise definitions

### 2.1 Traction and the Cauchy stress tensor

Let $d\mathbf{f}$ be the force transmitted across a surface element with outward
normal $\hat n$ and area $dA$. The **traction** is
$\mathbf{t} = d\mathbf{f}/dA$, and **Cauchy's hypothesis** is that it is linear in
$\hat n$:

$$t_i = \sigma_{ij}n_j. \tag{1}$$

$\sigma_{ij}$ is the Cauchy stress tensor. Its components have a direct reading:
$\sigma_{11}$ is the normal traction on the face whose normal is $\hat x_1$ (a
normal stress), and $\sigma_{12}$ is the component of traction in the
$\hat x_2$ direction on that same face (a shear stress). Both are forces per unit
area, in pascals in SI.

The traction on a plane is what a transducer can measure; the tensor is what you
infer from measurements on several planes. **A single measurement cannot
determine a stress tensor.**

### 2.2 Displacement gradient, strain and rotation

Let $\mathbf{u}(\mathbf{x})$ be the displacement of the material point that was at
$\mathbf{x}$. Then

$$u_{i,j} = \tfrac{1}{2}\left(u_{i,j} + u_{j,i}\right)
+ \tfrac{1}{2}\left(u_{i,j} - u_{j,i}\right) \equiv e_{ij} + \omega_{ij}, \tag{2}$$

with the **infinitesimal strain tensor**

$$e_{ij} = \tfrac{1}{2}\left(u_{i,j} + u_{j,i}\right), \qquad e_{ij} = e_{ji},
\tag{3}$$

and the **rotation tensor** $\omega_{ij} = - \omega_{ji}$. The engineering shear
strain for a pair of distinct axes is

$$\gamma_{ij} = 2e_{ij} \quad (i \neq j), \qquad \text{so } e_{12} =
\tfrac{1}{2}\gamma_{12}.$$

This is the convention trap that ruins otherwise correct rotation code, as
demonstrated in [01-15-02](./02-tensor-algebra.md) Section 3.9.

### 2.3 Decompositions

Both tensors split into an isotropic and a deviatoric part:

$$\sigma_{ij} = p\,\delta_{ij} + s_{ij}, \qquad p = \tfrac{1}{3}\sigma_{kk},
\qquad s_{ij} = \sigma_{ij} - p\delta_{ij}, \qquad s_{ii} = 0,$$

$$e_{ij} = \tfrac{1}{3}\Delta\,\delta_{ij} + e'_{ij}, \qquad
\Delta = e_{kk} = \frac{\delta V}{V}, \qquad e'_{ii} = 0. \tag{4}$$

$\Delta$ is the **dilatation**: the fractional volume change. In the
tension-positive convention the pressure is $-p$, so a state of pure pressure has
$\sigma_{ij} = -P\delta_{ij}$ and $s_{ij} = 0$.

### 2.4 Principal values, principal axes and invariants

A symmetric tensor has three real eigenvalues and an orthonormal eigenbasis:

$$\sigma_{ij}n^{(a)}_j = \sigma_a n^{(a)}_i, \qquad a = 1,2,3. \tag{5}$$

The $\sigma_a$ are the **principal stresses** and the $n^{(a)}$ the **principal
axes**; on a plane whose normal is a principal axis the traction is purely normal
and has magnitude $\sigma_a$. The invariants are

$$I_1 = \sigma_{ii}, \qquad
I_2 = \tfrac{1}{2}\left(\sigma_{ii}\sigma_{jj} - \sigma_{ij}\sigma_{ji}\right),
\qquad I_3 = \det\boldsymbol{\sigma}, \tag{6}$$

and the deviatoric invariants are $J_1 = 0$ and

$$J_2 = \tfrac{1}{2}s_{ij}s_{ij}, \qquad
J_3 = \det\mathbf{s} = \tfrac{1}{3}s_{ij}s_{jk}s_{ki}. \tag{7}$$

### 2.5 Compatibility

A symmetric array $e_{ij}$ is a strain field only if a displacement field exists
whose symmetric gradient it is. That requires

$$e_{ij,kl} + e_{kl,ij} - e_{ik,jl} - e_{jl,ik} = 0, \tag{8}$$

the **Saint-Venant compatibility conditions**. There are $3^4 = 81$ index
combinations but only 6 independent equations, because the conditions have the
symmetries of the Riemann curvature tensor of
[01-15-06](./06-differential-geometry-earth.md).

## 3. Derivations

### 3.1 Why the stress tensor is symmetric

Take a small cube of side $\ell$ centred at a point. The force on each face is
traction times area, so it scales as $\ell^2$; the moment of those forces about
the centre also scales as $\ell^2 \cdot \ell = \ell^3$. Any body couple density
$\mathbf{c}$ acts on the volume and produces a moment scaling as $\ell^3$. In the
limit $\ell \to 0$ both terms survive, so balance of angular momentum requires the
two to cancel exactly:

$$0 = \varepsilon_{ijk}\sigma_{jl}\ell_j + c_k \quad\text{per unit volume.}$$

For an ordinary continuum $c_k = 0$ — no distributed couples — and the
first term must vanish on its own:

$$\varepsilon_{ijk}\sigma_{jl}\ell_j \to 0 \quad
\Longrightarrow\quad \varepsilon_{ijk}\sigma_{jk} = 0
\quad \Longrightarrow\quad \sigma_{jk} = \sigma_{kj}. \qquad\square$$

The step from the volume term to the pointwise statement is what uses the
arbitrariness of $\ell_j$ and of the position. The assumption that fails in a
**Cosserat** (micropolar) medium, where grains carry their own couples, is
exactly $c_k = 0$; there the stress tensor is not symmetric, and the antisymmetric
part is balanced by a couple-stress tensor. For ordinary rocks at ordinary strain
rates the assumption holds, and symmetric stress is the working hypothesis.

### 3.2 Why the strain tensor is the symmetric part of the gradient

Consider two material points separated by $d\mathbf{x}$. After the displacement
they are separated by $dx_i + u_{i,j}dx_j$ to first order, so

$$|d\mathbf{x}'|^2 - |d\mathbf{x}|^2
= 2u_{i,j}dx_idx_j + u_{i,j}u_{i,k}dx_jdx_k.$$

Infinitesimal strain means $|u_{i,j}| \ll 1$, so the quadratic term is negligible
and, splitting the gradient,

$$|d\mathbf{x}'|^2 - |d\mathbf{x}|^2
= \left(u_{i,j} + u_{j,i}\right)dx_idx_j
= 2e_{ij}dx_idx_j, \tag{9}$$

because the antisymmetric part contributes nothing to the symmetric product
$dx_idx_j$ (the argument of
[01-15-01](./01-index-notation.md) Section 3.6). Equation (9) is the *definition*
of strain in terms of length changes. Setting $d\mathbf{x} = \ell\hat x_1$ gives
$\ell'^2 - \ell^2 = 2e_{11}\ell^2$, i.e. $e_{11} = \ell'/\ell - 1$: the normal
strain is the fractional extension along that axis.

Volume change requires the full determinant. For a small strain the Jacobian of
the deformation is $\det(\delta_{ij} + u_{i,j}) = 1 + u_{i,i} + O(\varepsilon^2)$,
so

$$\frac{\delta V}{V} = u_{i,i} + O(\varepsilon^2) = e_{ii}, \tag{10}$$

which justifies equation (4). The $O(\varepsilon^2)$ remainder is the subject of
the numerical experiment in Section 6: at a strain of $5\times10^{-3}$ the
relative error of the first-order identity is $5.4\times10^{-3}$, i.e. exactly of
order $\varepsilon$.

### 3.3 Invariants and their physical meaning

**$I_1$: the mean stress.** $\tfrac{1}{3}\sigma_{ii}$ is the pressure (up to
sign). It is what determines volume change in an isotropic material, because the
constitutive law for the isotropic part is $\sigma_{kk} = (3\lambda +
2\mu)e_{kk}$: a purely volumetric response governed by the bulk modulus
$K = \lambda + \tfrac{2}{3}\mu$.

**$J_2$: the shear energy.** The elastic energy density of a deformation
separates into a volumetric and a shear part. With $\sigma_{ij} = p\delta_{ij} +
s_{ij}$ and $e_{ij} = (\Delta/3)\delta_{ij} + e'_{ij}$, contracting gives
$\sigma_{ij}e_{ij} = p\Delta + s_{ij}e'_{ij}$, because the cross terms vanish:
$\delta_{ij}e'_{ij} = 0$ and $s_{ij}\delta_{ij} = 0$. Using $p = K\Delta$ and
$s_{ij} = 2\mu e'_{ij}$, so that $s_{ij}e'_{ij} = J_2/\mu$,

$$W = \tfrac{1}{2}\sigma_{ij}e_{ij}
= \tfrac{1}{2}K\Delta^2 + \frac{J_2}{2\mu}.$$

The two terms depend on the deformation in completely different ways, and the
second is proportional to $J_2$: the **von Mises equivalent stress**
$\sigma_{\mathrm{vm}} = \sqrt{3J_2}$ is a single number that turns a tensor into a
scalar failure criterion. Metals and, approximately, intact rocks at high
confinement fail when $J_2$ reaches a material constant.

The decomposition is exact, and it checks numerically on the strain state of
Section 6: with $\Delta = 10^{-4}$, $K = 43.333333$ GPa and $J_2 = 2.1333\times
10^{14}$ Pa$^2$, the two terms are $216.666667$ and $5333.333333$
J m$^{-3}$, summing to $W = 5550.000000$ J m$^{-3}$ — the same number as
$\tfrac{1}{2}\sigma_{ij}e_{ij}$ computed directly from the components.

**$I_3$: the mode of deformation.** Two stress states with the same pressure and
the same $J_2$ can still differ in the *shape* of their deviator — axisymmetric
compression versus axisymmetric extension versus a state with $\sigma_2$ near
either extreme. That difference is the third invariant. A convenient dimensionless
encoding is the **Lode angle**. With the principal deviatoric stresses ordered
$s_1 \ge s_2 \ge s_3$,

$$s_k = \frac{2\sqrt{J_2}}{\sqrt 3}\cos\!\left(\theta_L -
\frac{2\pi(k-1)}{3}\right), \qquad k = 1,2,3, \tag{11}$$

and $J_3$ is a monotone function of $\theta_L$ at fixed $J_2$. For the stress
state of the demonstration this gives $\theta_L = 0.241125$ rad
$= 13.815466^\circ$, and equation (11) reproduces
$s = (46.004986, -13.205079, -32.799906)$ MPa against the eigenproblem's
$(46.004986, -13.205081, -32.799904)$, and $J_3 = \det\mathbf{s} = 19925.93$
MPa$^3$ against $\tfrac{1}{3}s_{ij}s_{jk}s_{ki} = 19925.93$ MPa$^3$: the same
number twice by two different routes.

**The complete list.** In three dimensions these three invariants are the *only*
frame-independent numbers of a symmetric rank-2 tensor. Everything else about a
stress state is the orientation of its principal axes, and orientation is a
direction, which transforms as a vector — the lesson of
[01-15-02](./02-tensor-algebra.md) Section 3.7.

### 3.4 Mohr's circle is the transformation law

Restrict to a two-dimensional state $(\sigma_{xx}, \sigma_{yy}, \sigma_{xy})$ and
let the plane normal make an angle $\phi$ with the $x$ axis. Then

$$\sigma_n = \frac{\sigma_{xx} + \sigma_{yy}}{2}
+ \frac{\sigma_{xx} - \sigma_{yy}}{2}\cos 2\phi + \sigma_{xy}\sin 2\phi, \qquad
\tau = -\frac{\sigma_{xx} - \sigma_{yy}}{2}\sin 2\phi + \sigma_{xy}\cos 2\phi.$$

Eliminating $\phi$ between these two equations:

$$\left(\sigma_n - \frac{\sigma_{xx}+\sigma_{yy}}{2}\right)^2 + \tau^2
= \left(\frac{\sigma_{xx}-\sigma_{yy}}{2}\right)^2 + \sigma_{xy}^2
\equiv R^2. \tag{12}$$

A circle. Its centre is the mean of the two in-plane normal stresses; its radius
is the maximum in-plane shear; its extreme points are the principal stresses. The
demonstration checks equation (12) at 37 orientations, with the largest departure
$2.05\times10^{-12}$ MPa$^2$ — quadrature-level agreement, since the circle is an
algebraic consequence of the transformation law and not a graphical convenience.

### 3.5 Maximum shear and why principal axes matter

The stationary values of the shear stress over all plane orientations are

$$\tau_{\max} = \frac{\sigma_1 - \sigma_3}{2},$$

attained on the two planes that bisect the planes normal to the largest and
smallest principal stresses. In the demonstration a random search over 400000
normals finds $\tau_{\max} = 39.402333$ MPa against the exact $(I_1 -
3\sigma_2)/2 = 39.402446$ MPa, and the maximising normal is
$(-0.4278, -0.6129, 0.6643)$ against the bisector of the two extreme principal
directions, $(-0.4291, -0.6112, 0.6651)$. The two agree to the resolution of the
search.

This is not an academic result. **Brittle failure of rock occurs on planes close
to the maximum-shear planes**, so knowing the principal axes tells you the
orientation of the faults a stress state will produce — the basis of Anderson's
classification of normal, thrust and strike-slip faulting by which principal
stress is vertical.

### 3.6 Compatibility, and what an incompatible field means

Differentiate $e_{ij} = \tfrac{1}{2}(u_{i,j} + u_{j,i})$ twice and antisymmetrise
in the second derivatives:

$$e_{ij,kl} + e_{kl,ij} - e_{ik,jl} - e_{jl,ik} = 0,$$

because every term is a combination of third derivatives of $u$ whose signs
cancel. The converse — that (8) is also sufficient, on a simply-connected body —
is the classical result of Saint-Venant.

The demonstration computes the residual of (8) for two fields. For a strain
derived from a displacement it is zero to every printed digit (the symmetric
stencil cancels algebraically, so that check is weak evidence — a warning worth
repeating). For the field $e_{xx} = y^2$, $e_{yy} = x^2$, $e_{zz} = 0$ and all
shears zero, the residual is $4.000467$, i.e. the incompatible combination
$e_{xx,yy} + e_{yy,xx} = 2 + 2 = 4$ with no compensating shear term. No
displacement field can produce that strain. Physically it describes a body that
would have to tear apart or overlap to satisfy its own strain: imposing such a
field in a finite-element model produces locking and spurious stresses, and the
constraint must be relaxed (mixed formulations) rather than enforced.

### 3.7 Hooke's law, and the meaning of the split

For an isotropic material,

$$\sigma_{ij} = \lambda e_{kk}\delta_{ij} + 2\mu e_{ij}, \tag{13}$$

which separates the two responses immediately:

$$\sigma_{kk} = (3\lambda + 2\mu)e_{kk}, \qquad
s_{ij} = 2\mu e'_{ij}, \qquad \frac{\delta V}{V} = \frac{p}{K}, \qquad K = \lambda +
\tfrac{2}{3}\mu. \tag{14}$$

The demonstration computes $\sigma$ from a chosen $e$ and finds
$\operatorname{tr}\boldsymbol{\sigma} = 13.000000$ MPa from
$(3\lambda + 2\mu)e_{kk}$ with $\lambda = 30$ GPa, $\mu = 20$ GPa,
$K = 43.333333$ GPa, and verifies that a **pure shear** strain produces
$\operatorname{tr}\boldsymbol{\sigma} = 0$ exactly: shear changes shape and not
volume. It also verifies $\mathbf{s} = 2\mu\mathbf{e}'$ to the printed precision,
which is the mathematical statement that the deviatoric response sees only
$\mu$ and the volumetric response only $K$. That is why the split exists, and why
$P$-wave speed $\alpha = \sqrt{(\lambda+2\mu)/\rho}$ depends on both constants
while $S$-wave speed $\beta = \sqrt{\mu/\rho}$ depends on one.

## 4. Physical interpretation

### 4.1 The magnitude of the two parts in the Earth

At a depth of 40 km in rock of density 2600 kg m$^{-3}$ the lithostatic pressure
is roughly $1$ GPa, because each kilometre of rock weighs about 25.5 MPa. The
deviatoric stresses that tectonics sustains at the same depth are of order
10–100 MPa — one or two orders of magnitude smaller. Every consequence follows:

- Yielding and fracture criteria are written in $s_{ij}$ (or its invariants
  $J_2, J_3$), never in $\sigma_{ij}$, because the pressure term is enormous and
  almost irrelevant to failure.
- Elastic wave speeds depend on the pressure through $\lambda(T,P)$ and $\mu(T,P)$,
  so seismology sees the volumetric response as a *material property* that varies
  with depth.
- Stress inversion from focal mechanisms recovers the orientation of the
  principal axes and the ratio of stress differences, not absolute magnitudes,
  because the pressure is unmeasurable in comparison.

### 4.2 Reading a stress state

For the stress tensor used in the demonstration,

$$\boldsymbol{\sigma} = \begin{pmatrix} 100 & 25 & -10\\ 25 & 60 & 5\\ -10 & 5 &
40\end{pmatrix}\ \text{MPa},$$

the eigenproblem gives principal stresses $(33.866760, 53.461588, 112.671652)$
MPa, mean stress $66.666667$ MPa, $I_1 = 200$ MPa, $I_2 = 11650$ MPa$^2$,
$I_3 = 204000$ MPa$^3$, and the deviatoric state has $J_2 = 1683.333333$
MPa$^2$, equivalent shear stress $\sqrt{3J_2} = 71.063352$ MPa and $I_2(\mathbf{s})
= -1683.333333$ MPa$^2$. Note the identity $I_2(\mathbf{s}) = -J_2$: for a
trace-free tensor the two invariants coincide up to sign, which is why different
texts call the same number by either name.

### 4.3 Two different shear experiments

A **pure shear** strain has $e_{12} = e_{21} \ne 0$ and zero rotation; a **simple
shear** has a displacement gradient with only one nonzero off-diagonal entry, so
it is pure shear plus a rigid rotation. They produce the same stress in an
isotropic material and different microstructures in a rock, because the rotation
part reorients the grains. The split of equation (2) is what lets you say this
precisely: $\omega_{ij}$ is not a deformation, but it is not nothing either — it
is the local rotation rate, and it is what a shear-wave splitting measurement
in an anisotropic medium is sensitive to.

## 5. Assumptions and regime of validity

1. **Infinitesimal strain.** Every formula above drops terms quadratic in the
   displacement gradient. The error is of order $\varepsilon$ relative, verified
   numerically: at $\varepsilon \approx 5\times10^{-3}$ the length-change
   identity (9) is in relative error by $5.4\times10^{-3}$, $5.4\times10^{-4}$ and
   $5.4\times10^{-5}$ as the strain is scaled by $1$, $0.1$ and $0.01$. For
   finite strain the correct objects are the Green–Lagrange or Almansi tensors,
   and (9) must be replaced by the exact expression. Geophysical relevance:
   near-surface soft soils and landslide strains can exceed a per cent, and
   mantle convection uses finite strain, while seismology at depth rarely
   exceeds $10^{-6}$.
2. **No body couples or couple stresses.** Symmetric stress requires the elastic
   continuum assumption. Cosserat/micropolar models (granular media, blocky
   rock masses, some metamaterials) have nonsymmetric stress.
3. **A representative volume element.** "Stress at a point" is an average over a
   volume large enough to contain many grains and small enough that the field
   varies slowly. Below that scale stress is a fluctuating, poorly defined
   quantity; this is the scale separation assumed by every continuum model.
4. **Sign convention.** Tension positive here. Under a global sign flip the
   principal stresses change sign, the mean stress changes sign, and the quadratic
   invariants ($I_2$, $J_2$, and therefore every failure criterion built on them)
   are unchanged — verified numerically in the demonstration. Linear invariants
   ($I_1$, and the von Mises *stress* when the material is in compression) do flip.
   State the convention before comparing with a paper.
5. **Quasi-static equilibrium for the divergence forms.** The equation of motion
   $\sigma_{ij,j} + f_i = \rho\ddot u_i$ reduces to the equilibrium statement
   $\sigma_{ij,j} + f_i = 0$ only when accelerations are negligible. In seismic
   wave propagation they are not.
6. **Compatibility needs simple connectivity and a simply connected body.** On a
   multiply connected body (a cylinder with a hole) the differential conditions
   are necessary but not sufficient, and additional integral (Cesàro) conditions
   are required. Dislocation theory is built on exactly this failure.
7. **Cartesian components.** All of this is written in Cartesian coordinates; the
   physical components in a spherical shell introduce scale factors and extra
   terms, as in [01-15-04](./04-curvilinear-coordinates.md).

## 6. Python demonstration

[`code/stress_strain_demo.py`](./code/stress_strain_demo.py) diagonalises real
stress tensors with a Jacobi solver written from scratch, and computes strains by
central differences from analytic displacement fields. Values are in MPa and in SI
as labelled.

Invariants, principal stresses and the deviatoric split:

```text
  principal stresses (ascending) = ['33.866760', '53.461588', '112.671652'] MPa
  mean stress p = tr(sigma)/3    = 66.666667 MPa
  I1 = tr sigma                  = 200.000000 MPa
  I2 = 1/2[(tr sigma)^2 - tr sigma^2] = 11650.000000 MPa^2
  I3 = det sigma                  = 204000.000000 MPa^3
  tr s            = -1.42e-14   (trace-free by construction)
  J2 = 1/2 s_ij s_ij = 1683.333333 MPa^2
  equivalent shear stress sqrt(3 J2) = 71.063352 MPa
  second invariant of s, I2(s) = -1683.333333 MPa^2
```

Traction, the maximum-shear plane, and the bisector prediction:

```text
  t = sigma n            = ['40.000000', '41.800000', '30.800000'] MPa
  normal stress t.n      = 59.104000 MPa
  shear stress |t - (t.n)n| = 28.330146 MPa
  identity check |t|^2 = sigma_n^2 + tau^2: 4295.8800000000 vs 4295.8800000000
  random search over 400000 normals: max shear = 39.402333 MPa
  exact result (sigma_1 - sigma_3)/2          = 39.402446 MPa
  at n = ['-0.4278', '-0.6129', '0.6643']
  bisector of the sigma_1 and sigma_3 principal directions = ['-0.4291', '-0.6112', '0.6651']
```

Mohr's circle as a checked algebraic identity:

```text
  centre  (sigma_xx + sigma_yy)/2          = 80.000000 MPa
  radius  sqrt[((a-b)/2)^2 + tau_xy^2]     = 32.015621 MPa
  principal stresses from the circle       = 47.984379, 112.015621 MPa
     (sigma_n - centre)^2 + tau^2 = radius^2 for every phi;
     largest departure over 37 angles = 2.046e-12 MPa^2
```

Strain from a displacement field, rotation split off, and the length-change
identity:

```text
  e_ij = 1/2 (u_i,j + u_j,i)
     [       0.001000         0.004500        -0.002000]
     [       0.004500         0.003000         0.003000]
     [      -0.002000         0.003000         0.001000]
  omega_ij = 1/2 (u_i,j - u_j,i)
     [       0.000000         0.001500        -0.000000]
     [      -0.001500         0.000000        -0.001000]
     [       0.000000         0.001000         0.000000]
  tr e = 0.005000   (dilatation; volume change per unit volume)
  strain scaled by  1.00:  relative difference = 5.4e-03
  strain scaled by  0.10:  relative difference = 5.4e-04
  strain scaled by  0.01:  relative difference = 5.4e-05
  max |e_ij| for a rigid rotation = 0.0e+00
  the non-zero part is omega_xy = -1.200000e-03 rad/s (=-Omega_z, as the axial-vector correspondence requires)
```

Compatibility, and the sign-convention check:

```text
  e_xx = y^2, e_yy = x^2, all other components zero:
    max |compatibility residual| = 4.000467
  Compression-positive convention: sigma -> -sigma
    principal stresses ['33.8668', '53.4616', '112.6717'] -> ['-112.6717', '-53.4616', '-33.8668']
    max shear magnitude unchanged: 39.4024 -> 39.4024 MPa
    I2 unchanged: 11650.0000 -> 11650.0000
  deviatoric part of sigma from the deviatoric part of e:
    max |s_ij - 2 mu e'_ij| = 0.0e+00 Pa
```

### What to observe, and why it matters

| Observation | Consequence |
|---|---|
| principal stresses sum to $I_1$ and multiply to $I_3$ exactly | the invariants are the eigenvalues in disguise |
| $I_2(\mathbf{s}) = -J_2$ to six decimals | for a deviator these are one number, not two |
| the random search reaches $(I_1 - 3\sigma_2)/2$ but not more | shear is bounded by half the principal difference |
| the circle residual is $2\times10^{-12}$ | Mohr's circle is the transformation law, not a drawing |
| a rigid rotation gives exactly zero strain | the antisymmetric part is not deformation |
| the incompatible field gives residual 4 | compatibility is a real constraint, not a formality |
| flipping the sign of $\sigma$ leaves $I_2$ and $\tau_{\max}$ alone | quote invariants and you are convention-independent |

> **Breaking exercise.** Replace the pure shear strain of the last block with
> simple shear, $u_1 = \kappa x_2$, $u_2 = 0$, and predict the values of
> $e_{12}$, $\omega_{12}$ and $\operatorname{tr}\mathbf{e}$ before running.
> Then check whether the deviatoric stress changes.

## 7. Exercises

Solutions are in
[`exercises/03-strain-and-stress-tensors-solutions.md`](./exercises/03-strain-and-stress-tensors-solutions.md).

**★ Foundational.** ★1 given a traction on two planes, find $\sigma_{ij}$
components; ★2 compute principal stresses and invariants of a $2\times2$ and a
$3\times3$ state; ★3 split a stress state into isotropic and deviatoric parts and
compute $J_2$; ★4 compute $e_{ij}$ and $\omega_{ij}$ from a given displacement
gradient.

**★★ Applied.** ★★5 derive the symmetry of stress and state where it fails;
★★6 for a strike-slip state with $\sigma_1$ north and $\sigma_3$ east, find the
fault-plane orientations that maximise shear and state the expected type of
faulting; ★★7 show from $|d\mathbf{x}'|^2 - |d\mathbf{x}|^2 = 2e_{ij}dx_idx_j$
that a pure shear preserves volume; ★★8 check the compatibility conditions for
three given strain fields and identify which is impossible.

**★★★ Research-oriented.** ★★★9 implement a Mohr-circle construction for a
three-dimensional state, including the three principal circles, and verify
numerically that a plane on the largest circle can exceed the in-plane 2-D
maximum shear; ★★★10 take a focal-mechanism moment tensor, compute $M_0$,
its isotropic and deviatoric parts, the principal axes and the Lode angle, and
state what a seismologist can and cannot infer from the mechanism alone.

## 8. Common mistakes

1. **Reporting an engineering shear as $e_{ij}$.** A factor of 2 changes
   everything downstream, including invariants.
2. **Thinking the stress tensor is defined by nine measurements.** It is defined
   by the traction on every plane; a single plane gives a vector, not a tensor.
3. **Confusing pressure with the largest principal stress.** The pressure is
   $I_1/3$; the largest principal stress is a direction-dependent quantity.
4. **Using $J_2$ and $I_2$ of the same tensor interchangeably.** They differ by
   sign for the deviator and are unrelated for the full tensor.
5. **Assuming symmetric stress without stating it.** Cosserat continua and
   couple-stress theories exist; the symmetry is a physical assumption.
6. **Imposing an arbitrary strain field on a displacement-based model.** Any
   incompatible part will produce artificial stresses; check (8) or relax the
   constraint.
7. **Applying infinitesimal-strain formulas to a large deformation.** At
   $\varepsilon \sim 0.1$ the error is tens of per cent, not per mil.
8. **Forgetting that principal axes rotate with the material.** In a deforming
   medium the principal axes themselves change with time, and the rate of change
   matters for stress-path dependence.

## 9. Real-world applications

- **Focal mechanisms.** The moment tensor's principal axes give the fault-plane
  orientation and the slip vector; its isotropic part measures the volumetric
  change of the source (non-zero for volcanic and phase-change sources, zero to
  within noise for tectonic earthquakes). Both statements are invariant
  statements of this lesson.
- **Borehole breakouts and drilling-induced fractures.** Breakouts form where
  the circumferential stress concentrates, which is where the maximum shear is;
  the observed azimuth of breakouts therefore records the orientation of the
  horizontal principal stresses.
- **Fault stability.** Coulomb failure on a fault depends on the shear and normal
  traction on the fault plane, i.e. on the projection of the regional stress
  tensor onto that plane. Stress inversion codes search over principal-axis
  orientations and a stress ratio, which are exactly the invariants and axes of
  Sections 3.3 and 3.5.
- **Subsidence and reservoir compaction.** The volumetric response of (14) —
  $\delta V/V = p/K$ — is the mechanism behind compaction that shows up in
  gravity and leveling data.
- **Seismic anisotropy from stress.** Aligned microcracks open in the plane
  normal to the least compressive stress; the resulting anisotropy has symmetry
  axes set by the stress tensor's principal axes, which is the bridge from this
  lesson to [01-15-05](./05-anisotropy-representation.md) and to
  [02-04-06](../../02-physics/04-elasticity-and-continuum-mechanics/06-anisotropic-elasticity.md).
- **Continuum modelling in a spherical shell.** Convection and post-glacial
  rebound codes solve the momentum equation with a stress tensor whose physical
  components need the scale factors of
  [01-15-04](./04-curvilinear-coordinates.md); the invariant statements are the
  same, the bookkeeping is not.

## 10. Further reading

- **Jaeger, J. C., Cook, N. G. W., & Zimmerman, R. W. *Fundamentals of Rock
  Mechanics* (4th ed.). Blackwell.** Chapters 1–2. Level: intermediate. Stress
  and strain in the compression-positive convention used in the earth sciences,
  with the failure criteria built on $J_2$.
- **Aki, K., & Richards, P. G. *Quantitative Seismology* (2nd ed.). University
  Science Books.** Chapter 2 and Section 3.3. Level: advanced. Traction, moment
  tensors and the elastodynamic equation, with careful convention statements.
- **Malvern, L. E. *Introduction to the Mechanics of a Continuous Medium*.
  Prentice-Hall.** Chapters 3–4. Level: advanced. The derivation of stress
  symmetry from angular momentum, including the couple-stress caveat.
- **Timoshenko, S. P., & Goodier, J. N. *Theory of Elasticity* (3rd ed.).
  McGraw-Hill.** Chapters 1–2. Level: intermediate. The classical derivation of
  the compatibility conditions and the isotropic constitutive law.
- **Mase, G. T., Smelser, R. E., & Mase, G. E. *Continuum Mechanics for
  Engineers* (3rd ed.). CRC Press.** Level: intermediate to advanced. Strain from
  the length-change argument with the finite-strain generalisation, and the Lode
  angle with consistent sign conventions.

> Note on citations: bibliographic details are given so you can locate these
> works. This repository does not host or reproduce copyrighted text; confirm
> current editions and availability through your library.

## 11. Related lessons

- [01-15-01 Index Notation, Einstein Summation and Kronecker Delta](./01-index-notation.md)
  — the notation for every derivation here.
- [01-15-02 Tensor Algebra, Transformation Laws and Invariants](./02-tensor-algebra.md)
  — why the invariants quoted throughout are frame-independent.
- [01-15-04 Differential Operators in Curvilinear Coordinates](./04-curvilinear-coordinates.md)
  — the operators acting on stress in spherical or cylindrical geometries.
- [01-15-05 Representing Anisotropy: Voigt Notation and Symmetry Classes](./05-anisotropy-representation.md)
  — what replaces $\lambda$ and $\mu$ when the rock is not isotropic.
- [02-04 Elasticity and Continuum Mechanics](../../02-physics/04-elasticity-and-continuum-mechanics/README.md)
  — the physics module that develops stress and strain alongside this lesson,
  including [02-04-01 Stress](../../02-physics/04-elasticity-and-continuum-mechanics/01-stress.md)
  and [02-04-02 Strain](../../02-physics/04-elasticity-and-continuum-mechanics/02-strain.md).
- [02-04-05 Elastodynamic Equation of Motion and Wave Speeds](../../02-physics/04-elasticity-and-continuum-mechanics/05-elastodynamics.md)
  — where $\sigma_{ij,j} = \rho\ddot u_i$ becomes seismic waves.
- [01-06-08 Potential Fields, Laplace and Poisson Equations](../06-multivariable-calculus/08-potential-theory.md)
  — the trace-free gravity gradient tensor, a second rank-2 example.

## Self-assessment checklist

- [ ] I can define traction and write $t_i = \sigma_{ij}n_j$ with my sign
      convention stated. (Section 2.1)
- [ ] I can derive the symmetry of the stress tensor and name the assumption it
      needs. (Section 3.1)
- [ ] I can derive the strain tensor from the change of a material line element
      and explain why the rotation part drops out. (Section 3.2)
- [ ] I can compute principal stresses, $I_1, I_2, I_3$, $p$, $s_{ij}$, $J_2$
      and $\theta_L$ for a given stress state. (Sections 3.3, 4.2)
- [ ] I can state the physical meaning of the mean stress, $J_2$ and the third
      invariant, and say why failure criteria use the deviator. (Sections 3.3,
      4.1)
- [ ] I can explain Mohr's circle as the transformation law and derive the
      centre-and-radius form. (Section 3.4)
- [ ] I can state and use the compatibility conditions, and explain what an
      incompatible strain field describes. (Section 3.6)
- [ ] I can verify numerically that a strain from a displacement field is
      compatible and that $e_{xx} = y^2$, $e_{yy} = x^2$ is not. (Section 6)
- [ ] I can state what changes under a switch from tension-positive to
      compression-positive conventions, and what does not. (Sections 3.3, 5)
