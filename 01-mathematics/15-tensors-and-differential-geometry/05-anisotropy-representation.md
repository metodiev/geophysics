---
id: 01-15-05
title: "Representing Anisotropy: Voigt Notation and Symmetry Classes"
level: graduate
prereqs: ["01-15-02", "01-15-03", "01-07-06"]
estimated_minutes: 90
tags: [anisotropy, voigt-notation, symmetry-classes, stiffness-tensor]
---

# Representing Anisotropy: Voigt Notation and Symmetry Classes

## Learning objectives

By the end of this lesson you will be able to:

1. **Count** the independent components of an elastic stiffness tensor: 81 before
   any symmetry, 36 after the two minor symmetries, 21 after the major symmetry,
   and derive each count by explicit construction rather than by quoting a table.
2. **Convert** between $C_{ijkl}$ and the $6\times6$ Voigt matrix $C_{\alpha\beta}$
   in both directions, with the factor of two in the shear convention handled
   correctly and stated explicitly.
3. **Determine** from the structure of the Voigt matrix which symmetry class a
   medium belongs to, and **verify** the claim by testing invariance under the
   group's rotations — not by inspecting the pattern of zeros.
4. **Count** the independent constants of the triclinic, monoclinic,
   orthorhombic, tetragonal, trigonal, hexagonal, cubic and isotropic classes by
   averaging rotations over the point group and measuring the dimension of the
   invariant subspace.
5. **Write** the VTI stiffness matrix, explain what each constant means
   physically, and define the Thomsen parameters.
6. **Explain** why a $6\times6$ matrix cannot be rotated componentwise, and
   quantify the error that doing so produces.

## Prerequisites

- [01-15-02 Tensor Algebra, Transformation Laws and Invariants](./02-tensor-algebra.md)
  — the transformation law for a rank-4 tensor, and the isotropic case with two
  constants.
- [01-15-03 Strain and Stress Tensors as Physical Tensors](./03-strain-and-stress-tensors.md)
  — the symmetric strain and stress tensors whose symmetry gives the minor
  symmetries, and the engineering-versus-scientific shear convention.
- [01-07-06 Eigenvalues, Eigenvectors and Diagonalisation](../07-linear-algebra/06-eigenvalues.md)
  — eigenvalues of the $6\times6$ matrix, used for the positive-definiteness
  check.

## 1. Intuition: how many numbers does a rock need?

An elastic tensor has four indices, so it has $3^4 = 81$ components. No
measurement programme can determine 81 numbers per point, and no inversion can
invert for them. The whole of anisotropic seismology rests on the fact that
**physics removes most of them**:

| Stage | Constraint | Components |
|---|---|---|
| Raw rank-4 tensor | none | 81 |
| Minor symmetries | $\sigma_{ij}$ symmetric, $e_{kl}$ symmetric | 36 |
| Major symmetry | existence of a strain-energy density | 21 |
| Orthorhombic | three perpendicular mirror planes | 9 |
| Tetragonal / hexagonal (VTI) | one four-fold / six-fold axis | 6 / 5 |
| Cubic | four three-fold axes | 3 |
| Isotropic | invariance under all rotations | 2 |

A shale with a single set of aligned vertical fractures is *orthorhombic*, nine
numbers. A stack of flat-lying layers at long wavelength is *transverse
isotropic*, five numbers. A granite with no fabric is isotropic, two. That
reduction from 81 to 2 is not an abstraction: it is why an anisotropic velocity
analysis needs a handful of parameters rather than an unmanageable dataset, and
why the symmetry class matters more than the individual constants for
interpretation.

The representation that makes this practical is **Voigt notation**, which
replaces each symmetric index pair $(ij)$ by a single label $\alpha = 1,\dots,6$,
turning the stiffness into a $6\times6$ matrix. That matrix is a storage
convention, not a tensor, and the factor of two it hides in the shear components
is the source of most of the errors in the field.

## 2. Precise definitions

### 2.1 Generalised Hooke's law

$$\sigma_{ij} = C_{ijkl}e_{kl}, \qquad e_{kl} = \tfrac{1}{2}(u_{k,l} + u_{l,k}),
\tag{1}$$

with 81 components of $C$ in principle independent. Two of the four indices are
tied to the symmetry of $\sigma$, and two to the symmetry of $e$; the remaining
structure comes from thermodynamics.

### 2.2 Minor symmetries

Because $\sigma_{ij} = \sigma_{ji}$ and $e_{kl} = e_{lk}$,

$$C_{ijkl} = C_{jikl} = C_{ijlk}, \tag{2}$$

which is the **minor symmetry**. It reduces the count from 81 to
$6\times 6 = 36$, because only six distinct index *pairs* remain.

### 2.3 Major symmetry

If a strain-energy density $W = \tfrac{1}{2}C_{ijkl}e_{ij}e_{kl}$ exists — which
it does for any elastic (non-dissipative) material — then

$$\sigma_{ij} = \frac{\partial W}{\partial e_{ij}} = C_{ijkl}e_{kl}, \qquad
C_{ijkl} = \frac{\partial^2 W}{\partial e_{ij}\partial e_{kl}}
= C_{klij}, \tag{3}$$

the **major symmetry**. It reduces the count from 36 to $6\cdot 7/2 = 21$. A
material with a strain-energy function is called hyperelastic; the major symmetry
is exactly the statement that the response is conservative.

Stability additionally requires $W > 0$ for every non-zero strain, i.e. $C$ is
positive definite as a $6\times6$ matrix. That condition is *not* implied by the
symmetries; it is checked in Section 6.

### 2.4 Voigt notation

Order the six index pairs as

$$(11)\to 1,\quad (22)\to 2,\quad (33)\to 3,\quad (23)\to 4,\quad
(13)\to 5,\quad (12)\to 6, \tag{4}$$

and define

$$C_{\alpha\beta} := C_{ijkl}, \qquad \alpha \leftrightarrow (ij),\ \beta
\leftrightarrow (kl). \tag{5}$$

Then $C_{\alpha\beta}$ is a symmetric $6\times6$ matrix, and Hooke's law becomes

$$\sigma_\alpha = C_{\alpha\beta}\,\varepsilon_\beta, \qquad
\varepsilon_\alpha = \begin{cases} e_{ij}, & \alpha = 1,2,3,\\
2e_{ij}, & \alpha = 4,5,6,\end{cases} \qquad
\sigma_\alpha = \begin{cases} \sigma_{ij}, & \alpha = 1,2,3,\\
\sigma_{ij}, & \alpha = 4,5,6.\end{cases} \tag{6}$$

**The factor of two sits on the strain side and nowhere else.** With this
convention, no factor appears in $C_{\alpha\beta}$ itself, and the compliance
$S_{\alpha\beta} = (C^{-1})_{\alpha\beta}$ is the ordinary matrix inverse acting
on the same engineering strain vector:

$$\varepsilon_\alpha = S_{\alpha\beta}\sigma_\beta. \tag{7}$$

That is a strong argument for this convention over the alternatives, and it is
verified numerically in Section 6.

### 2.5 Symmetry classes

| Class | Independent constants | Typical cause in rocks |
|---|---|---|
| Triclinic ($1$, $\bar 1$) | 21 | no symmetry at all; rare in rocks |
| Monoclinic ($2$, $m$, $2/m$) | 13 | one mirror plane; some shales, some slates |
| Orthorhombic ($222$, $mm2$, $mmm$) | 9 | layering plus aligned vertical fractures |
| Tetragonal ($4/mmm$ and related) | 6 | not common in rocks |
| Trigonal ($\bar 3m$ and related) | 6 | calcite, quartz |
| Hexagonal ($6/mmm$)\ \ *transverse isotropy* | 5 | layering, or one aligned fracture set |
| Cubic ($m\bar 3 m$ and related) | 3 | olivine, garnet, halite |
| Isotropic | 2 | polycrystalline rocks with no fabric |

The same numbers recur in every standard table (Nye's book is the canonical
source), and they are *derived* in Section 3.5 rather than assumed.

### 2.6 The VTI matrix and Thomsen parameters

With the symmetry axis along $z$ and the ordering (4),

$$\mathbf{C}_V = \begin{pmatrix}
C_{11} & C_{12} & C_{13} & 0 & 0 & 0\\
C_{12} & C_{11} & C_{13} & 0 & 0 & 0\\
C_{13} & C_{13} & C_{33} & 0 & 0 & 0\\
0 & 0 & 0 & C_{44} & 0 & 0\\
0 & 0 & 0 & 0 & C_{44} & 0\\
0 & 0 & 0 & 0 & 0 & C_{66}
\end{pmatrix}, \qquad C_{12} = C_{11} - 2C_{66}, \tag{8}$$

five independent constants $C_{11}$, $C_{33}$, $C_{44}$, $C_{66}$, $C_{13}$. The
constraint on $C_{12}$ is not decoration: it is part of the definition of
hexagonal symmetry, and Section 3.5 derives it.

The **Thomsen parameters** are dimensionless combinations chosen so that weak
anisotropy becomes nearly linear:

$$\epsilon = \frac{C_{11} - C_{33}}{2C_{33}}, \qquad
\gamma = \frac{C_{66} - C_{44}}{2C_{44}}, \qquad
\delta = \frac{(C_{13} + C_{44})^2 - (C_{33} - C_{44})^2}
{2C_{33}(C_{33} - C_{44})}. \tag{9}$$

$\epsilon$ measures the $P$-wave anisotropy between vertical and horizontal
propagation, $\gamma$ measures the shear-wave splitting between the two $S$
polarisations, and $\delta$ controls the near-vertical variation of $P$ and $SV$
speed — the parameter that most affects reflection moveout at moderate offset.

## 3. Derivations

### 3.1 Counting 81 → 36 → 21 without a table

Write the 81 numbers as a vector of length 81 and build the two symmetrising
operations explicitly:

$$(\mathcal{P}_{\min}C)_{ijkl} = \tfrac{1}{4}\left(C_{ijkl} + C_{jikl} +
C_{ijlk} + C_{jilk}\right), \qquad
(\mathcal{P}_{\text{maj}}C)_{ijkl} = \tfrac{1}{2}\left(C_{ijkl} +
C_{klij}\right).$$

Each is a projection, so the dimension of its image is the number of independent
constants in that symmetry class. The demonstration applies both to the 81 unit
tensors and measures the rank:

```text
  rank of P_minor acting on the 81 unit tensors: 36
  rank of P_major P_minor acting on the same:    21
```

It also writes down the bases explicitly: 36 minor-symmetric tensors from the
unordered pairs $(ij)$ and $(kl)$, 21 major-symmetric ones from the combinations
$\alpha \le \beta$, and confirms the spans have dimensions 36 and 21. Counting by
construction, not by assertion.

### 3.2 Why the major symmetry exists, and what breaks it

The elastic energy density of a linear elastic material is

$$W = \tfrac{1}{2}C_{ijkl}e_{ij}e_{kl} + O(e^3).$$

Differentiating with respect to $e_{ij}$ recovers the stress,
$\partial W/\partial e_{ij} = C_{ijkl}e_{kl} = \sigma_{ij}$, and differentiating
again gives the stiffness. Since the order of partial differentiation does not
matter for a twice differentiable $W$,

$$C_{ijkl} = \frac{\partial\sigma_{ij}}{\partial e_{kl}}
= \frac{\partial^2 W}{\partial e_{ij}\partial e_{kl}}
= \frac{\partial^2 W}{\partial e_{kl}\partial e_{ij}} = C_{klij}. \qquad\square$$

Two remarks. First, the derivation *assumes* $W$ exists; a purely elastic
material has one, an anelastic material with a dissipation mechanism need not
(the relaxation tensor of a linear viscoelastic solid satisfies the same
symmetries only when the relaxation mechanism is reciprocal). Second, major
symmetry is not enough for stability: a symmetric matrix can have negative
eigenvalues, and a material whose energy decreases under some deformation is
unstable. Positive definiteness is an independent requirement, checked in
Section 6.

### 3.3 The factor of two, precisely

Start from the tensor form and expand the contract over the six unordered index
pairs:

$$\sigma_{ij} = \sum_{k\le l} \left(\text{coefficient}\right) C_{ijkl}e_{kl}.$$

The sum over $k,l$ runs over nine ordered pairs, which correspond to three
diagonal pairs $(11),(22),(33)$ and three off-diagonal pairs each counted twice
($(23)$ and $(32)$, etc.). Collecting:

$$\sigma_\alpha = \sum_{\beta=1}^{3} C_{\alpha\beta}e_{\beta\beta}
+ \sum_{\beta=4}^{6} C_{\alpha\beta}\cdot 2e_{\beta\beta'},$$

which is (6) with $\varepsilon_\beta = 2e_{ij}$ for $\beta = 4,5,6$. The
demonstration verifies both forms agree for a general $C$ and a general strain to
$0.0\times10^{0}$, and then isolates the factor on a single constant:

```text
  C_1212 = 20 GPa alone, pure shear e_12 = e_21 = 0.01:
    tensor form: sigma_12 = C_1212 e_12 + C_1221 e_21 = 400.0000 MPa
    Voigt with eps_6 = 2 e_12: sigma_6 = C_66 eps_6 = 400.0000 MPa
    Voigt with eps_6 = e_12:   sigma_6 = C_66 eps_6 = 200.0000 MPa   <- a factor of 2 too small
```

Some authors instead keep $\varepsilon_6 = e_{12}$ and define a different
$6\times6$ array with $C_{66} \to 2C_{66}$-like factors, and some split the
factors between $C$ and $S$. All conventions are self-consistent; mixing two of
them is not. State the convention in every table you publish.

### 3.4 Whose symmetry? Material symmetry versus frame invariance

Two different invariances are involved and they must not be confused:

- **Frame invariance** is what makes $C$ a tensor: the components change under a
  rotation of the frame, but the assembled 81 numbers describe the same material,
  as verified in Section 6 ($1.907\times10^{-15}$ GPa change in the Voigt matrix
  when the tensor is rotated by a symmetry of the medium).
- **Material symmetry** is the set of rotations under which the *components* do
  not change. That set is the point group of the rock, and its size determines
  how many constants survive.

So a material's symmetry class is not a property of the array you happen to hold:
it is the statement that some subgroup of the rotation group leaves the tensor
fixed.

### 3.5 Counting symmetry classes by averaging rotations

Let $G$ be the point group of the medium (its rotations, plus reflections where
they apply), and let $R(g)$ denote the action of group element $g$ on rank-4
tensors, $C'_{ijkl} = g_{ip}g_{jq}g_{kr}g_{ls}C_{pqrs}$. The invariant tensors are
the image of the projector

$$\mathcal{P} = \frac{1}{|G|}\sum_{g \in G} R(g).$$

**The number of independent elastic constants of a class is the rank of
$\mathcal{P}$ acting on the 21-dimensional space of elastic tensors.** Averaging
over the group and measuring a rank is completely mechanical, which is why the
demonstration can do it and why the result cannot be bluffed:

```text
  crystal class                            |G|  computed  standard  ok
  triclinic (1, -1)                          1        21        21  yes
  monoclinic (2, m, 2/m)                     2        13        13  yes
  orthorhombic (222, mm2, mmm)               4         9         9  yes
  tetragonal (422, 4mm, -42m, 4/mmm)         8         6         6  yes
  trigonal (32, 3m, -3m)                     6         6         6  yes
  hexagonal (622, 6mm, -6m2, 6/mmm)         12         5         5  yes
  cubic (23, m-3, 432, -43m, m-3m)          24         3         3  yes
```

Every row is a computation. The isotropic count is handled separately because
$SO(3)$ is not finite: a lower bound of 2 comes from exhibiting the two
independent isotropic tensors of
[01-15-02](./02-tensor-algebra.md), and an upper bound of 2 comes from measuring
the fixed space of a small generating set, by stacking the residuals $(I - R)v$
and taking the rank:

```text
    30 deg about z alone: independent constants = 5   (expected 5)
    30 deg about z and 90 deg about y: independent constants = 2   (expected 2)
    cubic generators, for cross-check: independent constants = 3   (expected 3)
```

**Why transverse isotropy has 5 and tetragonal 6.** Decompose the in-plane
part of the tensor by angular weight under rotations about $z$. A rotation by
$\phi$ multiplies a weight-$m$ component by $e^{im\phi}$. A generic $\phi$ (say
$30^\circ$) kills every in-plane weight $m \ne 0$ — including $m = \pm 4$ —
leaving the in-plane part isotropic with two constants ($C_{11}$ and $C_{12}$,
with $C_{66}$ determined):

$$C_{1212} = \tfrac{1}{2}\left(C_{1111} - C_{1122}\right)
\quad\Longrightarrow\quad C_{66} = \tfrac{1}{2}\left(C_{11} - C_{12}\right), \tag{10}$$

the constraint of (8). Adding the components that mix $z$ with the plane leaves
$C_{33}$, $C_{13}$ and $C_{44}$: **five** in total. A rotation by $90^\circ$
behaves differently, because $4\times90^\circ = 360^\circ$ and therefore
$e^{i4\phi} = 1$: the in-plane weight-$4$ combination survives, and one extra
constant remains. **Six** — the tetragonal count. That single sentence is the
difference between the two most-used classes in the subject.

**Notation warning.** This subsection uses the axes-1,2,3 convention where index
$3$ is the symmetry axis, matching the Voigt ordering (4). Other texts number
axes with $1$ as the symmetry axis; the matrices then look different but describe
the same physics. The demonstration's VTI matrix has the axis on index $3$.

### 3.6 Why a pattern of zeros is not a symmetry

Consider two matrices with the identical VTI zero pattern, one with
$C_{12} = C_{11} - 2C_{66} = 10$ GPa and one with $C_{12} = 20$ GPa. Both have
the same non-zero entries, and both give the same axial wave speeds, because
$C_{33}$ and $C_{44}$ are untouched:

```text
  C12 = C11 - 2 C66 = 10 (hexagonal)   max change under 60 deg about z = 1.907e-06   (relative 6.4e-17)
  C12 = 20 (same pattern, wrong value) max change under 60 deg about z = 3.750e+09   (relative 1.3e-01)
```

The first is invariant under a six-fold rotation — to $6.4\times10^{-17}$
relative, i.e. exactly, at round-off. The second changes by 13 per cent of its
own scale. It is **tetragonal, not hexagonal**, and using it as a hexagonal
stiffness produces a material whose wave speeds depend on the azimuth of the
survey. The pattern of zeros is necessary and not sufficient; the algebraic
constraint (10) is part of the definition.

### 3.7 The payoff: Christoffel equation and wave speeds

Plane waves $u_i = U_i\exp[\mathrm{i}\omega(t - n_jx_j/v)]$ in an anisotropic
medium satisfy the Christoffel equation

$$\left[\Gamma_{ij} - \rho v^2\delta_{ij}\right]U_j = 0, \qquad
\Gamma_{ij} = \frac{1}{\rho}C_{ijkl}n_jn_l, \tag{11}$$

so the squared phase velocities are the eigenvalues of $\Gamma$ and the
polarisations its eigenvectors. For VTI, the closed forms at the two extreme
directions are

$$v_p(0) = \sqrt{C_{33}/\rho}, \qquad v_{sv}(0) = \sqrt{C_{44}/\rho}, \qquad
v_p(90^\circ) = \sqrt{C_{11}/\rho}, \qquad v_{sh}(90^\circ) =
\sqrt{C_{66}/\rho}. \tag{12}$$

For the model used in the demonstration — $C_{11} = 30$, $C_{33} = 22$,
$C_{44} = 7$, $C_{66} = 10$, $C_{13} = 12$ GPa, $\rho = 2400$ kg m$^{-3}$ —
formulas (9) and (12) give

$$\epsilon = 0.181818182, \quad \gamma = 0.214285714, \quad \delta = 0.206060606,$$

$$v_p(0) = 3027.6504, \quad v_{sv}(0) = 1707.8251, \quad v_p(90^\circ) =
3535.5339, \quad v_{sh}(90^\circ) = 2041.2415\ \text{m s}^{-1},$$

and the numerical eigenproblem reproduces these values exactly, which is the
check that the representation and the physics are wired together correctly. The
same constants and the same numbers appear in
[02-04-06](../../02-physics/04-elasticity-and-continuum-mechanics/06-anisotropic-elasticity.md),
where the Christoffel problem is studied at intermediate angles.

## 4. Physical interpretation

### 4.1 Which rocks have which symmetry, and why

- **VTI from layering.** A stack of thin isotropic beds is, at wavelengths long
  compared with the bed thickness, equivalent to a transversely isotropic medium
  with a vertical axis. The effective constants are Backus averages: $C_{33}$ is
  the harmonic mean of the layer moduli (constant stress across the layers) and
  $C_{11}$ is close to the arithmetic mean (constant strain along them). This is
  the dominant anisotropy in sedimentary basins and it is a property of
  *geometry*, not of any mineral.
- **HTI from aligned fractures.** A set of parallel vertical cracks makes the
  rock stiffer along the cracks than across them, giving transverse isotropy with
  a horizontal axis. This is the standard model for a fractured reservoir, and it
  is the reason shear waves split.
- **Orthorhombic from both.** A layered shale with a single aligned vertical
  fracture set has *both* symmetries and is orthorhombic — nine constants. It is
  the realistic default for a fractured reservoir, and the reason modern
  anisotropic processing works in nine parameters rather than five.
- **Cubic from crystals.** Olivine and garnet are cubic at the single-crystal
  scale; mantle anisotropy arises when they acquire a crystallographic preferred
  orientation, which is itself a consequence of strain.
- **Isotropy as the no-information limit.** Two constants means the medium
  carries no directional information at all. Every isotropic-inversion artefact
  in an anisotropic medium is a statement that the extra information was
  discarded, and the discarded information is exactly the splitting / azimuthal
  dependence that the class structure predicts.

### 4.2 What each VTI constant means

| Constant | Physical meaning |
|---|---|
| $C_{33}$ | stiffness in compression along the symmetry axis; sets $v_p$ vertically |
| $C_{11}$ | stiffness in compression in the isotropy plane; sets $v_p$ horizontally |
| $C_{44}$ | shear stiffness for a plane containing the axis; sets $v_{sv}$ vertically |
| $C_{66}$ | shear stiffness within the isotropy plane; sets $v_{sh}$ horizontally |
| $C_{13}$ | coupling between axial and lateral compression; controls $\delta$ |

$C_{13}$ is the awkward one: it is not measured by any single-direction
experiment, and it is the constant that $\delta$ is designed to isolate. Almost
all practical disagreement between anisotropic velocity models is disagreement
about $C_{13}$.

### 4.3 What the $6\times6$ matrix is and is not

It is a **storage convention** with three roles: a compact table, a matrix to
invert for the compliance, and a source of the Christoffel matrix after
unpacking. It is **not a tensor**, and it does not transform as one. The
demonstration's check is blunt:

```text
    the 81-component tensor rotated by 60 deg about z changes by 1.907e-06 (relative 6.4e-17): it is the same tensor
    rotating the 6x6 array with the block-diagonal 6x6 rotation gives a
    matrix differing from the true one by up to 16.3923 GPa;
    for instance the (1,2) entry would become -5.0000 GPa instead of 10.0000 GPa.
```

Wrong sign *and* half the magnitude on a single entry. A correct $6\times6$
rotation exists — the Bond transformation — but it is *derived from* the
tensor transformation law of [01-15-02](./02-tensor-algebra.md), including
factors of two in the shear rows and columns. Anyone who rotates a stiffness
matrix by treating it as a $6\times6$ tensor will produce a plausible-looking
matrix that is not a stiffness tensor at all.

## 5. Assumptions and regime of validity

1. **Linearity and hyperelasticity.** Major symmetry, and hence the 21-component
   count, comes from the existence of an elastic potential. Viscoelastic or
   hysteretic media have a relaxation tensor whose symmetry structure must be
   justified separately, and the "constants" become complex functions of
   frequency.
2. **Infinitesimal strain.** The constitutive relation (1) is the first-order
   term of a general expansion; finite strain adds third-order (nonlinear)
   constants and changes the count.
3. **Effective-medium validity.** Backus averaging replaces a layered medium by
   an anisotropic homogeneous one only at wavelengths long compared with the
   layering. At comparable wavelengths the layering scatters, and the effective
   medium description fails — the same scale-separation assumption as everywhere
   else in continuum mechanics.
4. **One Voigt convention, applied consistently.** Engineering shear strain on the
   vector side, as in (6), verified in Section 6; or state the alternative
   explicitly.
5. **The 21 constants are the maximum for a *caustic* material in 3-D.** Lose
   major symmetry and the count is 36; go to a Cosserat medium and the
   question itself changes because couple stresses appear.
6. **Stability is a separate condition.** Positive definiteness of
   $C_{\alpha\beta}$ must be verified, for instance by checking the six
   eigenvalues, and it is not implied by any symmetry.
7. **Symmetry class claims need verification by transformation.** The zero
   pattern and the algebraic constraint must *both* hold, and the check is
   invariance under the group, as in Section 3.6.
8. **Crystal-symmetry tables use their own axis conventions.** Compare the
   matrices, not the labels, and check which index is the symmetry axis.

## 6. Python demonstration

[`code/voigt_anisotropy_demo.py`](./code/voigt_anisotropy_demo.py) builds rank-4
tensors as 81-vectors, symmetrises them, measures ranks, averages rotations over
point groups, and constructs the Voigt matrices by hand. Every component count in
this lesson is produced there rather than quoted.

The counts by construction, and the Voigt identity:

```text
  basis tensors symmetric under i<->j and k<->l, written down: 36
  dimension of their span (Gram-Schmidt): 36
  basis tensors with both minor and major symmetry: 21
  dimension of their span: 21
  rank of P_minor acting on the 81 unit tensors: 36
  rank of P_major P_minor acting on the same:    21
  max |C_ijkl - C_jikl| = 0.0e+00
  max |C_ijkl - C_klij| = 0.0e+00
  sigma_ij = C_ijkl e_kl  versus  sigma_alpha = C_ab eps_b
  largest difference = 0.0e+00
```

The symmetry-class table and the isotropic bracket:

```text
  triclinic (1, -1)                          1        21        21  yes
  monoclinic (2, m, 2/m)                     2        13        13  yes
  orthorhombic (222, mm2, mmm)               4         9         9  yes
  tetragonal (422, 4mm, -42m, 4/mmm)         8         6         6  yes
  trigonal (32, 3m, -3m)                     6         6         6  yes
  hexagonal (622, 6mm, -6m2, 6/mmm)         12         5         5  yes
  cubic (23, m-3, 432, -43m, m-3m)          24         3         3  yes
    30 deg about z alone: independent constants = 5   (expected 5)
    30 deg about z and 90 deg about y: independent constants = 2   (expected 2)
    cubic generators, for cross-check: independent constants = 3   (expected 3)
```

The fake-VTI trap and the rotated-medium symmetry:

```text
  C12 = C11 - 2 C66 = 10 (hexagonal)   max change under 60 deg about z = 1.907e-06   (relative 6.4e-17)
  C12 = 20 (same pattern, wrong value) max change under 60 deg about z = 3.750e+09   (relative 1.3e-01)
  rotating the tensor by 90 deg about y (VTI -> HTI):
    relative change under 60 deg about x (the new axis) = 6.358e-17
    relative change under 60 deg about z (now the hard direction) = 2.000e-01
```

Compliance, stability and the non-tensor warning:

```text
  compliance S = C^-1 in Voigt notation (1/GPa, rounded):
     [  0.04358   -0.00642   -0.02027    0.00000    0.00000    0.00000]
     [ -0.00642    0.04358   -0.02027    0.00000    0.00000    0.00000]
     [ -0.02027   -0.02027    0.06757    0.00000    0.00000    0.00000]
     [  0.00000    0.00000    0.00000    0.14286    0.00000    0.00000]
     [  0.00000    0.00000    0.00000    0.00000    0.14286    0.00000]
     [  0.00000    0.00000    0.00000    0.00000    0.00000    0.10000]
  max |eps_alpha - S_ab sigma_b| = 2.2e-19
  S_44 = 0.14285714 vs 1/C_44 = 0.14285714
  eigenvalues of the 6x6 stiffness matrix (GPa): ['7.000000', '7.000000', '10.000000', '11.790627', '20.000000', '50.209373']
  all six positive: True, so the strain energy
  is positive definite for this model, as a stable material requires.
  the classical necessary conditions also hold: C_44 = 7 > 0,
  C_11 = 30 > |C_12| = 10, and C_33(C_11 + C_12) = 880 > 2 C_13^2 = 288.
```

And the wave-speed payoff:

```text
  Thomsen parameters of the VTI model (constants in GPa):
    epsilon = 0.181818182
    gamma   = 0.214285714
    delta   = 0.206060606
  n = z (vertical)     velocities = [' 1707.8251', ' 1707.8251', ' 3027.6504'] m/s
  n = x (horizontal)   velocities = [' 1707.8251', ' 2041.2415', ' 3535.5339'] m/s
  closed form: v_p(0) = sqrt(C33/rho) = 3027.6504
               v_sv(0) = sqrt(C44/rho) = 1707.8251
               v_p(90) = sqrt(C11/rho) = 3535.5339
               v_sh(90) = sqrt(C66/rho) = 2041.2415
    propagation along the new axis: ['1707.8251', '1707.8251', '3027.6504'] m/s, against ['1707.8251', '1707.8251', '3027.6504'] m/s from the VTI axial values
```

That last line is a genuine invariance statement: after rotating the medium by
$90^\circ$ about $y$, every component of the tensor has changed, yet the
eigenvalue set of the Christoffel matrix along the new axis is *identical* to the
set along the old axis. Symmetry axes and eigenvalues are physics; components are
bookkeeping.

### What to observe, and why it matters

| Observation | Consequence |
|---|---|
| 36 and 21 from two independent constructions | the counts are not conventions or folklore |
| $\sigma_\alpha = C_{\alpha\beta}\varepsilon_\beta$ agrees with the tensor form exactly | the factor of 2 is on the strain side and nowhere else |
| the group-average table reproduces every standard count | symmetry classes are a computation, not a table |
| the wrong $C_{12}$ passes the pattern test and fails the rotation test | verify symmetry by transforming, not by looking |
| the $6\times6$ eigenvalues are all positive | stability is an independent condition that must be checked |
| $S = C^{-1}$ in Voigt and $\varepsilon = S\sigma$ to $10^{-19}$ | the engineering convention buys exact consistency with the inverse |
| the HTI eigenvalue set equals the VTI axial set | rotation moves labels, not physics |

> **Breaking exercise.** Set $C_{13} = 0$ in the VTI model and recompute
> $\delta$. Predict the sign and rough magnitude before running, then check
> whether the resulting constants are positive definite and stable.

## 7. Exercises

Solutions are in
[`exercises/05-anisotropy-representation-solutions.md`](./exercises/05-anisotropy-representation-solutions.md).

**★ Foundational.** ★1 convert a given $C_{ijkl}$ array into Voigt form and
back; ★2 write the VTI stiffness matrix for given constants and verify
$C_{12} = C_{11} - 2C_{66}$; ★3 compute the Thomsen parameters of a model;
★4 count the independent constants of an assumed symmetry by writing out the
relations.

**★★ Applied.** ★★5 verify the factor-of-two rule on a hand-worked pure shear;
★★6 check positive definiteness of three VTI models, including one deliberately
unstable; ★★7 show by explicit rotation that a given matrix with a VTI pattern
and a wrong $C_{12}$ is tetragonal; ★★8 compute $v_p$ vertically and
horizontally for a model and compare with the Thomsen approximations.

**★★★ Research-oriented.** ★★★9 implement the projector $\mathcal{P}$ of
Section 3.5 for a monoclinic group and verify the count of 13 by constructing the
invariant subspace, then exhibit a basis; ★★★10 build a layered medium of two
isotropic constituents, compute its Backus-average stiffness, verify that the
result is VTI with the constraint of (8) satisfied, and compare its Thomsen
parameters with a numerical long-wavelength check.

## 8. Common mistakes

1. **Rotating a $6\times6$ stiffness matrix componentwise.** The demonstration's
   error is a factor of two and a sign on one entry; use the tensor form or a
   correctly derived Bond matrix.
2. **Dropping the factor of 2 on the shear strain.** Halves the shear stress for
   the same strain, silently.
3. **Mixing two conventions in one calculation.** Decide once whether
   $\varepsilon_6 = e_{12}$ or $2e_{12}$ and annotate every table.
4. **Judging the symmetry class from the zero pattern.** The algebraic
   constraint is part of the class definition.
5. **Forgetting the stability condition.** A symmetric $6\times6$ matrix with a
   negative eigenvalue is not a physical stiffness.
6. **Assuming $C_{13}$ is measurable in a single direction.** No single-direction
   speed depends on it, which is why $\delta$ exists and why $C_{13}$ is the
   least-constrained constant in practice.
7. **Confusing the axis convention.** "Index 3 is the symmetry axis" and "index 1
   is the symmetry axis" both occur; check which one a paper uses before copying
   a matrix.
8. **Treating a material symmetry as a frame property.** Material symmetry is
   invariance of components under a group; frame changes act on components too,
   and the two invariances must not be conflated.

## 9. Real-world applications

- **Anisotropic velocity analysis.** Seismic processing in layered basins is
  parameterised by the Thomsen parameters, and depth conversion with an isotropic
  velocity model produces systematic depth errors that grow with offset — the
  practical reason $\delta$ matters.
- **Fractured-reservoir characterisation.** Aligned fractures give HTI, and
  shear-wave splitting or azimuthal $P$-wave velocity variation measures the
  fracture orientation. Orthorhombic is the realistic model when layering is also
  present, and the nine-constant parameterisation is what modern azimuthal
  inversions use.
- **Mantle anisotropy.** Crystallographic preferred orientation of olivine gives
  fast axes aligned with flow; measuring $\xi$ (the splitting) constrains flow
  directions in the upper mantle, with the symmetry arguments of this lesson
  providing the interpretation.
- **Crustal cracks and their alignment with stress.** Crack-induced anisotropy is
  aligned with the principal stress directions of
  [01-15-03](./03-strain-and-stress-tensors.md), which is how seismic anisotropy
  becomes a proxy for the stress field.
- **Mineral physics.** Single-crystal elastic constants of mantle phases are
  tabulated in the Voigt convention, and their aggregates are computed with the
  averaging schemes that give the effective VTI/TI symmetries.
- **Finite-element modelling.** Building a stiffness matrix for an anisotropic
  element requires exactly the $C_{\alpha\beta}$ layout of this lesson; the
  formulation's correctness hinges on the shear convention being consistent with
  the strain-displacement matrix.

## 10. Further reading

- **Nye, J. F. *Physical Properties of Crystals: Their Representation by Tensors
  and Matrices*. Oxford University Press.** Chapters 2–8. Level: intermediate to
  advanced. The canonical derivation of the symmetry-class counts, with every
  matrix written out and the axis conventions stated.
- **Thomsen, L. (1986). Weak elastic anisotropy. *Geophysics*, 51(10),
  1954–1966.** Level: advanced. The origin of the $\epsilon, \delta, \gamma$
  parameterisation and of the weak-anisotropy approximations; the standard
  reference for Section 2.6.
- **Aki, K., & Richards, P. G. *Quantitative Seismology* (2nd ed.). University
  Science Books.** Chapter 2. Level: advanced. The elastic tensor, its symmetries
  and the Christoffel equation in the convention used here.
- **Tsvankin, I. *Seismic Signatures and Analysis of Reflection Data in
  Anisotropic Media* (2nd ed.). SEG.** Level: advanced. Practical consequences of
  the symmetry classes for moveout and amplitude, including the HTI and
  orthorhombic cases.
- **Musgrave, M. J. P. *Crystal Acoustics: Introduction to the Study of Elastic
  Waves in Crystals*. Holden-Day.** Level: doctoral. Rigorous treatment of
  elastic-wave propagation by symmetry class, including all the classical
  degeneracies.
- **Helbig, K. *Foundations of Anisotropy for Exploration Seismics*. Pergamon.**
  Level: advanced. A careful discussion of the $6\times6$ representation, the
  factor-of-two conventions and the Bond transformation.

> Note on citations: bibliographic details are given so you can locate these
> works. This repository does not host or reproduce copyrighted text; confirm
> current editions and availability through your library.

## 11. Related lessons

- [01-15-02 Tensor Algebra, Transformation Laws and Invariants](./02-tensor-algebra.md)
  — the isotropic rank-4 tensor and the transformation law that a stiffness must
  obey.
- [01-15-03 Strain and Stress Tensors as Physical Tensors](./03-strain-and-stress-tensors.md)
  — the symmetric stress and strain that produce the minor symmetries, and the
  engineering-strain convention.
- [01-15-04 Differential Operators in Curvilinear Coordinates](./04-curvilinear-coordinates.md)
  — the operators used when the elastic equation is solved in a spherical shell.
- [02-04-06 Anisotropic Elasticity (VTI, HTI, Orthorhombic)](../../02-physics/04-elasticity-and-continuum-mechanics/06-anisotropic-elasticity.md)
  — the Christoffel problem at intermediate angles, shear-wave splitting, and the
  Thomsen parameters in use.
- [02-04-03 Constitutive Laws and Generalised Hooke's Law](../../02-physics/04-elasticity-and-continuum-mechanics/03-constitutive-laws.md)
  — where the elastic constants are introduced from the physics side.
- [01-07-06 Eigenvalues, Eigenvectors and Diagonalisation](../07-linear-algebra/06-eigenvalues.md)
  — the linear algebra behind the $6\times6$ eigenvalue check.
- [06-seismology](../../06-seismology/README.md) — where the symmetry classes
  become processing and interpretation choices.

## Self-assessment checklist

- [ ] I can derive the counts 36 and 21 by construction, without a table.
      (Section 3.1)
- [ ] I can derive the major symmetry from the strain-energy function and state
      what assumption it needs. (Section 3.2)
- [ ] I can convert between $C_{ijkl}$ and $C_{\alpha\beta}$ with the factor of
      two placed correctly, and say which side it belongs to. (Sections 2.4, 3.3)
- [ ] I can write the VTI stiffness matrix, state its five constants, and verify
      the constraint $C_{12} = C_{11} - 2C_{66}$. (Section 2.6)
- [ ] I can count the constants of any class by averaging rotations, and explain
      why transverse isotropy has 5 and tetragonal 6. (Section 3.5)
- [ ] I can show by a rotation test that a matrix with a VTI pattern is or is not
      hexagonal. (Section 3.6)
- [ ] I can compute Thomsen parameters and the VTI axial and horizontal wave
      speeds, and say which constant each measurement constrains. (Sections 2.6,
      3.7)
- [ ] I can check positive definiteness of a stiffness matrix and explain why
      symmetry does not imply it. (Section 6)
- [ ] I can explain why the $6\times6$ matrix is not a tensor, and quantify the
      error from rotating it as one. (Section 4.3)
