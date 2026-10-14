---
id: 01-15-02
title: "Tensor Algebra, Transformation Laws and Invariants"
level: graduate
prereqs: ["01-15-01", "01-07-01", "01-07-07"]
estimated_minutes: 90
tags: [tensors, transformation-laws, invariants, rotations]
---

# Tensor Algebra, Transformation Laws and Invariants

## Learning objectives

By the end of this lesson you will be able to:

1. **State** the transformation law for a tensor of any rank, and explain why it,
   rather than the number of components, is the definition.
2. **Decide** whether a given array of numbers is a tensor, by testing the law
   rather than by inspecting the array.
3. **Derive** that the Kronecker delta is the only isotropic rank-2 tensor and
   that an isotropic rank-4 tensor has exactly two independent constants, in the
   form $C_{ijkl} = \lambda\delta_{ij}\delta_{kl} + \mu(\delta_{ik}\delta_{jl} +
   \delta_{il}\delta_{jk})$.
4. **Compute** the three invariants $I_1, I_2, I_3$ of a rank-2 tensor, relate them
   to the coefficients of the characteristic polynomial and to the elementary
   symmetric functions of the eigenvalues, and explain what each one means
   physically.
5. **Convert** between an antisymmetric tensor and its axial vector, and say
   precisely what changes under a reflection.
6. **Identify** two arrays that look like tensors but are not, and state the
   convention error each one causes.

## Prerequisites

- [01-15-01 Index Notation, Einstein Summation and Kronecker Delta](./01-index-notation.md)
  — everything here is written in that notation.
- [01-07-01 Vectors, Spaces and Linear Independence](../07-linear-algebra/01-vectors-and-spaces.md)
  — bases, components and linear maps.
- [01-07-07 Orthogonality, Projections and Least Squares](../07-linear-algebra/07-orthogonality.md)
  — orthogonal matrices, the property $\mathbf{Q}^{\mathsf T}\mathbf{Q} =
  \mathbf{I}$ that the transformation law rests on.

## 1. Intuition: a tensor is what transforms like a tensor

Consider two three-by-three arrays. The first holds the nine components of the
stress tensor at a point in a rock; the second holds nine numbers a survey
recorded, say the travel times of nine shots binned by azimuth. Both are tables
of nine numbers. Only one of them is a tensor, and the difference cannot be seen
in the table.

The difference is that when you rotate your frame of reference, the stress
components change in a definite, predictable way — the traction on any surface
must come out the same physical vector, expressed in the new axes — while the
travel-time table simply becomes a different table with no relation to the old
one. A tensor is an object whose components change together in such a way that the
physical statement they encode does not change at all. That is the entire
definition, and it is why physics is written with tensors: **a tensor equation
that holds in one frame holds in every frame**.

Two consequences follow immediately and organise this lesson:

- Every tensor comes with **invariant** combinations of its components — numbers
  that are literally the same in every frame. These are the physically meaningful
  quantities, because they are what a measurement can return without any
  convention about axes.
- Not every array is a tensor, and the failures are not exotic. Estimating
  shear strain with the engineering convention and then rotating it as if it were
  a tensor is a real, common error with a factor-of-two consequence, and the
  demonstration below exhibits it numerically.

## 2. Precise definitions

### 2.1 Frames and orthogonal transformations

Let $x_i$ and $x'_i$ be the Cartesian coordinates of the same physical point in
two frames with a common origin. A transformation that preserves lengths and
angles has the form

$$x'_i = Q_{ij}x_j, \qquad Q_{ik}Q_{jk} = \delta_{ij},
\qquad \mathbf{Q}^{\mathsf T}\mathbf{Q} = \mathbf{I}, \tag{1}$$

so $\mathbf{Q}^{\mathsf T} = \mathbf{Q}^{-1}$. Such a $\mathbf{Q}$ is
*orthogonal*: a rotation if $\det\mathbf{Q} = +1$, a rotation composed with a
reflection if $\det\mathbf{Q} = -1$.

Two readings of the same transformation must be kept apart. In the **passive**
reading the object stays and the axes move; in the **active** reading the axes
stay and the object is physically rotated. The component formulas are the same for
a rotation and its inverse, because a rotation by $\theta$ and a rotation by
$-\theta$ are both orthogonal — this is what makes the passive/active distinction
harmless in Cartesian frames and dangerous in curvilinear ones.

### 2.2 The transformation law

A **scalar** (rank 0) is a single number unchanged by the transformation,
$\phi' = \phi$. A **vector** (rank 1) obeys

$$v'_i = Q_{ij}v_j. \tag{2}$$

A **rank-2 tensor** obeys

$$T'_{ij} = Q_{ip}Q_{jq}T_{pq}, \tag{3}$$

which in matrix form is $\mathbf{T}' = \mathbf{Q}\mathbf{T}\mathbf{Q}^{\mathsf T}$.
A **rank-$n$ tensor** carries one factor of $\mathbf{Q}$ per index:

$$T'_{i_1\dots i_n} = Q_{i_1j_1}\cdots Q_{i_nj_n}T_{j_1\dots j_n}. \tag{4}$$

The number of components ($3$, $9$, $27$, $81$) is a consequence; the law is the
definition. Note the structure of (4): each index is rotated independently, so a
tensor behaves like an outer product of vectors, and this is why products of
tensors are tensors (Section 3.2).

### 2.3 Covariant and contravariant components

In an orthonormal Cartesian frame the two component types coincide, and this
lesson uses only that case. In a general (curvilinear or non-orthogonal) frame a
vector has two sets of components, $v^i$ transforming with the coordinate
Jacobian and $v_i$ with its inverse transpose, and their inner product
$v^iu_i$ is the invariant. The distinction becomes physical in
[01-15-04](./04-curvilinear-coordinates.md) and
[01-15-06](./06-differential-geometry-earth.md), where it is the difference
between a physical component and a coordinate component.

### 2.4 The algebra of tensors

From (2)–(4) three constructions follow, and they are the whole of tensor algebra
for our purposes:

| Construction | Index form | Rank change |
|---|---|---|
| Sum | $A_{ij} + B_{ij}$ | same rank (requires the same index structure) |
| Outer product | $A_{ij}B_{kl}$ | ranks add: $2 + 2 = 4$ |
| Contraction | $A_{ij}B_{jk}$ | ranks add then subtract two: $2 + 2 - 2 = 2$ |
| Full contraction | $A_{ij}B_{ij}$ | scalar |

Every equation of continuum mechanics is built from these four operations,
together with differentiation, which adds one index (the comma of
[01-15-01](./01-index-notation.md)).

## 3. Derivations

### 3.1 Rotations form a group

Composing $x''_i = Q^{(2)}_{ij}x'_j = Q^{(2)}_{ij}Q^{(1)}_{jk}x_k$ gives
$Q^{(2)}Q^{(1)}$, which is again orthogonal:

$$(Q^{(2)}Q^{(1)})_{ik}(Q^{(2)}Q^{(1)})_{jk}
= Q^{(2)}_{ip}Q^{(1)}_{pk}Q^{(2)}_{iq}Q^{(1)}_{qk}
= Q^{(2)}_{ip}Q^{(2)}_{iq}\underbrace{Q^{(1)}_{pk}Q^{(1)}_{qk}}_{\delta_{pq}}
= \delta_{ij}.$$

The identity is orthogonal, inverses are orthogonal, and the product is
associative, so the set of orthogonal transformations is a group. The
transformation law (4) is then a *representation* of that group: composing
transformations is composing matrices. This is the structural reason a tensor
defined by its transformation law carries consistent physics under any sequence of
frame changes.

### 3.2 Products of tensors are tensors

Suppose $a_i$ and $b_j$ are vectors. Form the array $C_{ij} = a_ib_j$ and
transform it according to (3):

$$Q_{ip}Q_{jq}C_{pq} = Q_{ip}a_p\,Q_{jq}b_q = a'_ia'_j = C'_{ij}.$$

The array $C$ obeys the rank-2 law, so it is a tensor — with no assumption about
the vectors beyond (2). The same argument applies to any product, which is why
outer products can be used to build tensors from vectors and why a tensor's
components can be read as products of components in the principal axes.

### 3.3 Symmetry is preserved

If $T_{ij} = T_{ji}$ then

$$T'_{ij} = Q_{ip}Q_{jq}T_{pq} = Q_{jq}Q_{ip}T_{qp} = T'_{ji},$$

where the second step renames the dummy indices $p \leftrightarrow q$ and the
third uses the symmetry. Symmetry and antisymmetry are frame-independent
properties. This is why "the stress tensor is symmetric" is a statement about
physics and not about the coordinate choice, and why the split of
[01-15-01](./01-index-notation.md) Section 3.6 survives every rotation.

### 3.4 The isotropic rank-2 tensor

Which rank-2 tensors have the *same components in every frame*? Set
$T_{ij} = \delta_{ij}$ in (3):

$$\delta'_{ij} = Q_{ip}Q_{jq}\delta_{pq} = Q_{ip}Q_{jp} = \delta_{ij}.$$

So $\delta$ is invariant, and it is the only rank-2 tensor that is (up to a scale
factor): the invariant subspaces of $\mathbf{Q}\otimes\mathbf{Q}$ for all
orthogonal $\mathbf{Q}$ together reduce to this one direction. The demonstration
checks it over 200 random rotations.

### 3.5 The isotropic rank-4 tensor has two constants

The elastic tensor of an isotropic material must be an isotropic rank-4 tensor
with the minor and major symmetries of
[01-15-05](./05-anisotropy-representation.md). Two independent combinations are
available:

$$I_{ijkl} = \delta_{ij}\delta_{kl}, \qquad
J_{ijkl} = \tfrac{1}{2}\left(\delta_{ik}\delta_{jl} + \delta_{il}\delta_{jk}\right),
\qquad C_{ijkl} = \lambda I_{ijkl} + 2\mu J_{ijkl}. \tag{5}$$

$I$ and $J$ are isotropic because each is built from $\delta$'s, which are; and
they are independent, because contracting shows $I_{iikl} = 3\delta_{kl}$ while
$J_{iikl} = \delta_{kl}$. The demonstration verifies that this combination is
unchanged by random rotations (maximal change $2.3\times10^{-14}$ over fifty of
them), and
[`code/voigt_anisotropy_demo.py`](./code/voigt_anisotropy_demo.py) in
[01-15-05](./05-anisotropy-representation.md) closes the argument by measuring
the dimension of the fixed space of a small generating set of rotations: it is 2.

Two constants, $\lambda$ and $\mu$, and nothing else. The same construction,
applied with the symmetry groups of crystals instead of all rotations, produces
5 constants for transverse isotropy and 3 for cubic symmetry — also counted
explicitly in that companion demonstration.

### 3.6 Invariants of a rank-2 tensor

Because $I_1 = T_{ii}$ is a full contraction,

$$T'_{ii} = Q_{ip}Q_{iq}T_{pq} = \delta_{pq}T_{pq} = T_{ii},$$

so the trace is invariant. The determinant is invariant because
$\det(\mathbf{Q}\mathbf{T}\mathbf{Q}^{\mathsf T}) = \det\mathbf{Q}\det\mathbf{T}
\det\mathbf{Q}^{\mathsf T} = \det\mathbf{T}$. And a third invariant can be
manufactured from the square: the eigenvalues of a matrix are the roots of its
characteristic polynomial

$$\lambda^3 - I_1\lambda^2 + I_2\lambda - I_3 = 0, \qquad
I_1 = T_{ii}, \quad I_2 = \tfrac{1}{2}\left[(\operatorname{tr}\mathbf{T})^2 -
\operatorname{tr}(\mathbf{T}^2)\right], \quad I_3 = \det\mathbf{T}, \tag{6}$$

and since the polynomial is invariant, its roots are: **the eigenvalues are
invariants**. Writing $I_2$ and $I_3$ in index form,

$$I_2 = \tfrac{1}{2}(T_{ii}T_{jj} - T_{ij}T_{ji}), \qquad
I_3 = \tfrac{1}{6}\varepsilon_{ijk}\varepsilon_{lmn}T_{il}T_{jm}T_{kn},$$

makes the invariance evident: every index is summed, so the transformation
matrices contract away.

The eigenvalues can also be seen as the elementary symmetric functions of the
principal values $\lambda_a$:

$$I_1 = \sum_a\lambda_a, \qquad I_2 = \sum_{a<b}\lambda_a\lambda_b, \qquad
I_3 = \lambda_1\lambda_2\lambda_3, \tag{7}$$

which is the numerically verified statement quoted in Section 6. **A tensor with
three invariants has three frame-independent numbers; everything else about it is
orientation.** For a general rank-2 tensor in three dimensions this is the
complete list under rotations.

### 3.7 Why eigenvectors are vectors and eigenvalues are numbers

If $T_{ij}n_j = \lambda n_i$ then, in the primed frame,

$$T'_{ij}n'_j = Q_{ip}Q_{jq}T_{pq}Q_{jr}n_r = Q_{ip}T_{pq}\delta_{qr}n_r
= Q_{ip}(T_{pq}n_q) = \lambda Q_{ip}n_p = \lambda n'_i,$$

using $n'_j = Q_{jr}n_r$. So principal directions transform as vectors and
principal values do not transform at all. A principal axis is a physical
direction in the rock; the number attached to it is a physical property. Neither
statement mentions coordinates, and the demonstration confirms it to
$10^{-16}$ on a randomly rotated tensor.

Two warnings belong here:

1. **A real matrix need not have real eigenvalues.** The rotation matrix of
   Section 1 has eigenvalues $1$ and $e^{\pm i\theta}$. Reality, not symmetry, is
   exceptional: it holds for symmetric (and, over $\mathbb{C}$, Hermitian)
   matrices, and it is the reason stress and strain tensors have real principal
   values.
2. **Invariance is relative to a group.** Under all orthogonal transformations
   the trace, $I_2$ and the determinant are invariant; under the larger group of
   general linear transformations only the *ratios* $I_2/I_1^2$ and
   $I_3/I_1^3$ survive; under a symmetry group of a material, additional
   combinations become invariant. Always ask *invariant under what*.

### 3.8 Antisymmetric tensors and axial vectors

An antisymmetric rank-2 tensor and a vector have the same number of independent
components in three dimensions, $3$, and the correspondence is the epsilon
symbol:

$$W_{ij} = -\varepsilon_{ijk}w_k \qquad\Longleftrightarrow\qquad
w_i = -\tfrac{1}{2}\varepsilon_{ijk}W_{jk}. \tag{8}$$

Substituting one into the other and using the epsilon-delta identity of
[01-15-01](./01-index-notation.md) Section 3.2 recovers the vector unchanged.
Under a proper rotation the correspondence commutes with the transformation law:
the $w$ extracted from $W'$ equals $\mathbf{Q}w$, so $w$ transforms as a vector.
Under a reflection it does **not** behave as a vector: both the extraction (which
uses $\varepsilon$, itself sign-flipped) and the object flip, with the result that
$w'_i = -Q_{ij}w_j$ relative to a vector. Objects with this behaviour are
*pseudo-vectors* or *axial vectors*; angular velocity, vorticity and the magnetic
field (as a vector) are the standard examples. The demonstration exhibits both
the exact vector law under rotations and the failure of the epsilon symbol under
a reflection.

### 3.9 Two arrays that are not tensors

**The Levi-Civita symbol under a reflection.** Transform
$\varepsilon_{ijk}$ as a rank-3 tensor under the reflection
$\operatorname{diag}(1,1,-1)$: some components come back with the opposite sign.
Maximal difference: $2$, i.e. a component whose value changes from $+1$ to $-1$.

**Engineering shear strain.** A pure shear strain $e_{12} = e_{21} = 0.01$ has
engineering representation $\gamma_{12} = 0.02$, and the array with $0.02$ in the
off-diagonal slots is often handled as if it were the component matrix. Rotating
it componentwise by $45^\circ$ about $z$ gives $\operatorname{diag}(0.0200,
-0.0200, 0)$ where the correct engineering array is
$\operatorname{diag}(0.0100, -0.0100, 0)$: wrong by a factor of two on every
entry, verified in the demonstration. Worse, its second invariant $I_2$ is wrong
even before the rotation ($-0.0004$ against $-0.0001$), because $I_2$ sees the
squares of the shear entries.

## 4. Physical interpretation

| Object | Rank | Invariants under rotation | What is lost by quoting components |
|---|---|---|---|
| Potential, temperature | 0 | itself | nothing |
| Velocity, force | 1 | the length | the direction |
| Stress, strain | 2 | $I_1, I_2, I_3$ | orientation of principal axes |
| Elastic stiffness | 4 | many, depending on symmetry class | most of the 21 constants |
| Levi-Civita symbol | 3 | the symbol, as a pseudo-tensor | handedness |

Two physical readings deserve emphasis.

**Invariants are what instruments can measure without a frame convention.** The
mean stress $p = \sigma_{ii}/3$ is the pressure; it does not depend on how the
borehole was oriented. The second invariant of the deviatoric stress,
$J_2 = \tfrac{1}{2}s_{ij}s_{ij}$, is what a von Mises or Drucker–Prager yield
criterion uses, and it is a single number that decides whether a rock fails
regardless of the orientation of the stress axes. The scalar seismic moment
$M_0 = (\tfrac{1}{2}M_{ij}M_{ij})^{1/2}$ is another such contraction, and it is
the number that enters every magnitude scale.

**Isotropy is an invariance statement about a material, not about a frame.** An
isotropic elastic solid is one whose stiffness tensor is invariant under *all*
rotations; a VTI solid is invariant under all rotations about one axis; a cubic
crystal under the 24 rotations (and reflections) of the cube. Two objects that
look identical as arrays can differ in their invariance, and the difference is
physical: the demonstration builds two matrices with the identical
transverse-isotropic zero pattern, one of which is invariant under a six-fold
rotation and one of which is not. Only the first may be used as a hexagonal
stiffness. Misusing the second gives a material whose wave speeds change when you
rotate your survey, which is impossible.

## 5. Assumptions and regime of validity

1. **Cartesian, orthonormal, constant basis.** The laws (2)–(4) use a single
   $\mathbf{Q}$ for the whole region. If the basis varies from point to point the
   transformation is a field $\mathbf{Q}(\mathbf{x})$ and derivatives pick up
   extra terms ([01-15-04](./04-curvilinear-coordinates.md)).
2. **Orthogonal transformations only.** For a general linear transformation
   $x'_i = A_{ij}x_j$ the correct laws are $v'_i = A_{ij}v_j$ and
   $T'_{ij} = A_{ip}A_{jq}T_{pq}$ *only if* the basis change is between
   orthonormal frames; otherwise covariant and contravariant components must be
   distinguished and $A$ appears with its inverse transpose for one index.
3. **Same point, same origin.** A transformation that includes a translation
   changes position vectors but not the components of a stress tensor. Position
   is an affine, not a linear, object.
4. **Eigenvalues real for symmetric tensors only.** The characteristic polynomial
   of a nonsymmetric tensor has complex roots in general, and their imaginary
   parts are not invariant under all similarity transformations — they are
   invariant under orthogonal ones only.
5. **The invariance group matters.** The number of independent invariants of a
   rank-2 tensor is 3 under rotations in three dimensions and 2 in two
   dimensions; of a symmetric rank-4 elastic tensor it is 2 for isotropic, 3 for
   cubic, 5 for transverse isotropy and 21 for triclinic. Quoting an invariant
   without naming the group is meaningless.
6. **Pseudo-tensors need care with handedness.** Under reflections, axial vectors
   and the epsilon symbol do not obey the tensor law; this is not a technicality
   when a coordinate system is left-handed, which does happen in geophysics.

## 6. Python demonstration

[`code/tensor_transformation_demo.py`](./code/tensor_transformation_demo.py)
builds rotations from the Rodrigues formula, transforms tensors by both the matrix
form and the index form, and measures what changes.

The rotation itself, and the group property:

```text
  Q = rotation of +30 deg about z
     [      0.8660       -0.5000        0.0000]
     [      0.5000        0.8660        0.0000]
     [      0.0000        0.0000        1.0000]
  max |Q Q^T - I| = 0.0e+00
  det Q           = 1.000000000000   (a proper rotation, not a reflection)
  max |Q(30 deg) Q(10 deg) - Q(40 deg)| about z = 1.1e-16
```

The rank-2 law in both forms, and the physical test of it:

```text
  max |T'_ij (matrix form) - T'_ij (index form)| = 1.1e-15
  n  = [0.6, 0.0, 0.8]   ->  n'  = [0.519615, 0.3, 0.8]
  t  = [5.6, -0.2, -2.6]
  Q t                      = [4.949742, 2.626795, -2.6]
  T' n'                    = [4.949742, 2.626795, -2.6]
  difference               = 0.0e+00
```

That last comparison is the operational definition of a tensor in action: the
traction computed from the transformed tensor on the transformed plane equals the
transformed traction. If the transformation law were wrong, this physical
identity would fail.

Invariants versus components, over 200 random rotations:

```text
  I1 = tr T                  = 9.000000000000
  I2 = 1/2[(tr T)^2 - tr T^2] = -26.000000000000
  I3 = det T                 = -173.000000000000
    largest change in I1, I2, I3 over all 200 rotations: 7.1e-15, 7.8e-14, 2.8e-13
    largest change in a single component (T'_ii - T_ii): 13.7800
```

A component can move by 13.8 while all three invariants stay put to the
thirteenth decimal. Eigenvalues, principal directions and the elementary
symmetric functions:

```text
  eigenvalues (ascending) = [-4.6398055434, 3.7826295794, 9.857175964]
  same eigenvalues from the rotated tensor: [-4.6398055434, 3.7826295794, 9.857175964]
  residual |T n - lam n| for the largest principal value: 1.8e-15
  principal direction in the new frame, from the eigenproblem: [-0.999269, 0.035044, 0.015306]
  the rotated principal direction Q w                          : [-0.999269, 0.035044, 0.015306]
  difference (up to sign)                                      : 1.1e-16
    sum lam_a            = 9.000000000000   vs I1 = 9.000000000000
    sum lam_a lam_b      = -26.000000000000   vs I2 = -26.000000000000
    product lam_a        = -173.000000000000   vs I3 = -173.000000000000
```

The two arrays that fail the tensor test:

```text
  det(mirror) = -1.0
  max |eps'_ijk - eps_ijk| under the reflection = 2.0
  rotated by -45 deg about z: CORRECT engineering array
     [      0.0100        0.0000        0.0000]
     [      0.0000       -0.0100        0.0000]
     [      0.0000        0.0000        0.0000]
  rotated by -45 deg about z: componentwise rotation of the array
     [      0.0200        0.0000        0.0000]
     [      0.0000       -0.0200        0.0000]
     [      0.0000        0.0000        0.0000]
  largest difference = 0.0100
  I1 of strain = 0.000000   I1 of engineering array = 0.000000   (equal: the diagonal is untouched)
  I2 of strain = -0.000100   I2 of engineering array = -0.000400   (NOT equal: shear is doubled)
```

Isotropy, and the antisymmetric-to-axial-vector correspondence:

```text
  max |Q delta Q^T - delta| over 200 random rotations = 1.1e-15
  max change of C_ijkl = lam dij dkl + mu (dik djl + dil djk) over 50
  random rotations: 2.3e-14
  w_i recovered = [0.7, 2.0, 1.5]
  max |W_ij - axial(w)_ij| = 0.0e+00
  w from the rotated tensor    = [-0.39378222, 2.08205081, 1.5]
  Q w                          = [-0.39378222, 2.08205081, 1.5]
```

### What to observe, and why it matters

| Observation | Consequence |
|---|---|
| the three invariants hold to $10^{-13}$ while a component moves by 13.8 | quote invariants when you want frame-independent physics |
| the traction identity holds exactly | the transformation law is fixed by physics, not by taste |
| the principal direction rotates as a vector, to $10^{-16}$ | principal axes are physical directions |
| the epsilon symbol changes by 2.0 under a reflection | handedness is not preserved by the tensor law |
| the engineering array is wrong by 0.0100 after rotation | state the shear convention before any rotation |
| the isotropic rank-4 tensor is unchanged to $10^{-14}$ | two constants really do describe an isotropic solid |

> **Breaking exercise.** Change `mirror` to a rotation of $180^\circ$ about $z$
> and predict, before running, whether the epsilon-symbol test will pass and what
> the antisymmetric-to-vector extraction will report.

## 7. Exercises

Solutions are in
[`exercises/02-tensor-algebra-solutions.md`](./exercises/02-tensor-algebra-solutions.md).

**★ Foundational.** ★1 transform a vector and a rank-2 tensor by hand through the
$30^\circ$ rotation of the demonstration; ★2 compute $I_1, I_2, I_3$ for a given
symmetric matrix; ★3 verify that a given array is or is not a tensor by testing
the law; ★4 recover the axial vector of a given antisymmetric tensor.

**★★ Applied.** ★★5 prove that symmetry and antisymmetry are preserved by (3);
★★6 show that the trace is invariant and explain why the same argument fails for
a single component; ★★7 build the two isotropic rank-4 tensors of equation (5)
and show they are independent; ★★8 exhibit the factor-of-two error of the
engineering-strain array for a $30^\circ$ rotation and quantify it.

**★★★ Research-oriented.** ★★★9 for a given non-symmetric matrix, compute its
eigenvalues and state which combinations of them are invariant under orthogonal
transformations and which are not, with a numerical experiment; ★★★10 take a
stiffness matrix in Voigt form, build the full tensors for a hexagonal and a
tetragonal case, and demonstrate by explicit rotation which is which and what
goes wrong if the two are confused.

## 8. Common mistakes

1. **Assuming nine numbers form a tensor.** Test the transformation law; do not
   inspect the array.
2. **Rotating an engineering-strain array componentwise.** Only the array with
   halves on the shear terms obeys (3); the engineering array must be converted
   first.
3. **Quoting an invariant without naming the group.** Invariance under rotations
   is not invariance under general linear maps.
4. **Treating the axial vector as a vector.** Under reflections it acquires an
   extra sign, and left-handed coordinate systems are common in geophysics.
5. **Assuming real eigenvalues.** Nonsymmetric matrices have complex eigenvalues;
   only symmetry guarantees reality.
6. **Forgetting that a tensor's transformation includes every index.**
   Transforming a rank-4 stiffness "as a 6×6 matrix" is the error dissected in
   [01-15-05](./05-anisotropy-representation.md).
7. **Confusing $I_2$ of the tensor with $I_2$ of an array of components.**
   Different arrays, different numbers; the demonstration shows a factor of four.
8. **Believing that a change of frame changes physics.** If a result changes under
   a rotation, the error is in the bookkeeping, not in the rock.

## 9. Real-world applications

- **Rotating a stiffness tensor.** Building an HTI medium from a VTI one is
  literally $C'_{ijkl} = Q_{ip}Q_{jq}Q_{kr}Q_{ls}C_{pqrs}$ with a $90^\circ$
  rotation about $y$, as done in
  [02-04-06](../../02-physics/04-elasticity-and-continuum-mechanics/06-anisotropic-elasticity.md)
  and verified in this lesson's companion demonstration for
  [01-15-05](./05-anisotropy-representation.md).
- **Moment tensors between frames.** A focal mechanism is reported in a
  geographic frame (north, east, down) and must be rotated into instrument or
  regional coordinates; the invariants $M_0$ and the isotropic part are the same
  numbers afterwards, which is a free check of the rotation code.
- **Polarisation analysis.** The eigenvectors of a three-component covariance
  matrix give the polarisation directions of a seismic arrival; the eigenvalues
  give the energy on each axis. Both statements are frame-independent only
  because of the eigenvalue theory of this lesson.
- **Magnetotellurics.** The impedance tensor's rotation properties are what make
  the "principal axes" of a 2-D Earth well defined; the rotational invariants of
  the impedance are used to detect dimensionality, and the same algebra appears
  in [01-15-05](./05-anisotropy-representation.md).
- **Gravity gradiometry.** The five independent components of the gravity
  gradient tensor are a traceless symmetric tensor; its invariants are the
  quantities robust to platform orientation, and the trace being zero is why
  gradiometers can be calibrated on a rotating platform.
- **Stress from borehole breakouts.** Failure criteria are written in terms of
  the invariants of the stress deviator precisely because the orientation of the
  principal axes is what one is trying to measure, not what one knows.

## 10. Further reading

- **Nye, J. F. *Physical Properties of Crystals*. Oxford University Press.**
  Chapters 1–2. Level: intermediate to advanced. The canonical account of the
  transformation law, symmetry classes and the pseudo-tensor distinction.
- **Aki, K., & Richards, P. G. *Quantitative Seismology* (2nd ed.). University
  Science Books.** Sections 2.1–2.3. Level: advanced. Moment tensors, principal
  axes, and the conventions used in seismological practice.
- **Goldstein, H., Poole, C. P., & Safko, J. *Classical Mechanics* (3rd ed.).
  Addison-Wesley.** Chapter 4. Level: intermediate. Rotations, Euler angles and
  the pseudo-vector character of angular velocity, with the same algebra applied
  to rigid bodies.
- **Aris, R. *Vectors, Tensors and the Basic Equations of Fluid Mechanics*.
  Dover.** Chapters 2–3. Level: intermediate. Tensors as multilinear maps, with
  the invariance discussion kept concrete.
- **Itskov, M. *Tensor Algebra and Tensor Analysis for Engineers*. Springer.**
  Level: advanced. Chapter 2 contains a systematic treatment of isotropic tensor
  spaces, including proofs of the representation used in Section 3.5.

> Note on citations: bibliographic details are given so you can locate these
> works. This repository does not host or reproduce copyrighted text; confirm
> current editions and availability through your library.

## 11. Related lessons

- [01-15-01 Index Notation, Einstein Summation and Kronecker Delta](./01-index-notation.md)
  — the notation used throughout, including the epsilon-delta identity invoked
  in Section 3.8.
- [01-15-03 Strain and Stress Tensors as Physical Tensors](./03-strain-and-stress-tensors.md)
  — the most important rank-2 tensors in geophysics, with the physical meaning of
  $I_1$, $I_2$ and $I_3$.
- [01-15-05 Representing Anisotropy: Voigt Notation and Symmetry Classes](./05-anisotropy-representation.md)
  — the same invariance logic applied to a rank-4 tensor, using the symmetry
  group rather than the full rotation group.
- [01-15-06 Differential Geometry of the Earth's Surface and Sphere](./06-differential-geometry-earth.md)
  — where the invariant combinations of a general metric tensor are the tools.
- [01-07-06 Eigenvalues, Eigenvectors and Diagonalisation](../07-linear-algebra/06-eigenvalues.md)
  — the linear-algebra background for Sections 3.6 and 3.7.
- [02-04-06 Anisotropic Elasticity (VTI, HTI, Orthorhombic)](../../02-physics/04-elasticity-and-continuum-mechanics/06-anisotropic-elasticity.md)
  — where rotating a rank-4 tensor becomes a routine seismic-modelling operation.

## Self-assessment checklist

- [ ] I can state the transformation law for ranks 1, 2 and $n$, in both index
      and matrix form. (Section 2.2)
- [ ] I can prove that products of tensors are tensors, and that symmetry is
      preserved. (Sections 3.2, 3.3)
- [ ] I can show that $\delta_{ij}$ is isotropic and explain why the isotropic
      rank-4 elastic tensor has two constants. (Sections 3.4, 3.5)
- [ ] I can compute $I_1, I_2, I_3$, connect them to the characteristic
      polynomial and to the elementary symmetric functions of the eigenvalues.
      (Sections 3.6, 6)
- [ ] I can explain why eigenvalues are invariants and eigenvectors are vectors.
      (Section 3.7)
- [ ] I can convert between an antisymmetric tensor and its axial vector, and say
      what a reflection does to each. (Section 3.8)
- [ ] I can name two arrays that are not tensors and describe the error each
      causes. (Section 3.9)
- [ ] I can say what "invariant" means for a material symmetry, and why the
      symmetry group must be named. (Sections 4, 5)
- [ ] I can list the four assumptions under which the transformation law of this
      lesson is the whole story. (Section 5)
