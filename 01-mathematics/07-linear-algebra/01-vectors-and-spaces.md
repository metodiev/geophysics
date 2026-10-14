---
id: 01-07-01
title: "Vectors, Vector Spaces and Basis"
level: intermediate
prereqs: ["01-01-01", "01-02-01", "01-04-03"]
estimated_minutes: 90
tags: [linear-algebra, vectors, basis, model-space]
---

# Vectors, Vector Spaces and Basis

## Learning objectives

By the end of this lesson you will be able to:

1. **Decide** whether a set of geophysical quantities forms a vector space, by
   checking the axioms rather than by assuming that "a list of numbers" qualifies.
2. **Compute** inner products, norms and angles for a physical vector, and say
   what each quantity means in a measurement.
3. **Test** a set of vectors for linear independence, and **build** an orthonormal
   basis from them by Gram–Schmidt, reporting the numerical rank you actually find.
4. **Express** the same vector in two different bases, and explain why the
   coordinates change while the vector does not.
5. **Explain** why the choice of basis is a modelling decision, and give an example
   in which a bad basis makes an easily solved problem look hard.
6. **State** the difference between linear independence and *numerical* linear
   independence, and choose the tolerance that separates them.

## Prerequisites

[01-01-01 Number Systems, Precision and Scientific Notation](../01-arithmetic/01-number-systems-and-precision.md)
for significant figures and the floating-point floor,
[01-02-01 Algebraic Manipulation and Solving Equations](../02-algebra/01-algebraic-manipulation.md)
for the algebra of simultaneous relations, and
[01-04-03 Cartesian, Cylindrical and Spherical Coordinates](../04-geometry-and-coordinates/03-cartesian-spherical.md)
for the coordinate systems this lesson treats abstractly.

## 1. Intuition: a model is a vector, and the coordinates are not the model

Here is the object this whole module is about. A seismologist records ground
motion on three components. At one instant the sample is

$$\mathbf{u} = (0.80,\ -0.52,\ 1.70) \quad \text{counts, in (N, E, Z)}.$$

A tomographer wants to know the slowness perturbation in each of 400 cells. That
is a list of 400 numbers. A geodesist wants the three components of a station
velocity. That is a list of three numbers.

All three are **vectors**, and in each case the list of numbers is not the thing
itself — it is the thing *in a particular basis*. Rotate the horizontal components
of the seismogram into a ray-based frame and the triple changes while the ground
motion does not. Measure the tomographic model in $\mathrm{s/km}$ instead of
$\mathrm{s/m}$ and every number changes by $10^{3}$ while the Earth stays the
same. If you confuse the vector with its coordinates, you will attribute to the
physics a property that belongs to your notebook.

Two ideas make this precise, and both are used constantly later in the module:

- the **inner product**, which measures agreement between two vectors — not their
  similarity of size, and not their correlation;
- the **basis**, a minimal set of directions in which every vector can be written,
  and the reason "the model" has many equally legal descriptions.

The motivating question of the next several lessons is the one a survey poses:
*which model perturbations does my dataset actually see?* That question is
answered by rank, and rank is a statement about independence — which is what this
lesson defines.

## 2. Precise definitions

### 2.1 Vector spaces

A **vector space** over the real numbers is a set $V$ with two operations,
addition of elements of $V$ and multiplication by real scalars, satisfying the
usual eight axioms: closure, associativity and commutativity of addition, an
additive identity $\mathbf{0}$, additive inverses, and the two distributive laws
plus compatibility of scalar multiplication.

Why bother? Because the axioms are exactly the conditions under which the
machinery of this module works. In geophysics the two spaces that matter are
$\mathbb{R}^{n}$, the model space, and $\mathbb{R}^{m}$, the data space, together
with **function spaces**: the set of all continuous velocity profiles on
$[0, R]$ is a vector space, because a sum of two continuous profiles is
continuous and a scalar multiple is continuous. That is why the same language —
independence, basis, projection — applies to a 400-parameter tomographic model
and to a velocity *function*; the finitely parameterised case is a restriction of
the general one, and the general one is the subject of
[01-16 Functional Analysis for Inverse Problems](../16-functional-analysis/README.md).

Three sets that are **not** vector spaces, and why it matters:

| Set | Fails because |
|---|---|
| Strictly positive densities $\rho > 0$ | no additive identity: $\rho + (-\rho) = 0 \notin V$ |
| Unit vectors in $\mathbb{R}^{3}$ | the sum of two unit vectors generally has length $\neq 1$ |
| Travel times, as functions of offset | closed under addition, but the set of *physical* ones is not (a sum of two travel times need not be a travel time) |

The last row is the important one. The model space is a vector space; the set of
*geologically admissible* models is a subset of it, and the constraint that
distinguishes them is exactly what a regularisation term encodes in
[18-inverse-problems](../../18-inverse-problems/README.md).

### 2.2 Inner product, norm, angle

An **inner product** on a real vector space is a map
$\langle \cdot, \cdot \rangle : V \times V \to \mathbb{R}$ that is symmetric,
linear in each argument, and **positive definite**: $\langle x, x \rangle > 0$
for $x \neq 0$. For $\mathbb{R}^{n}$ with the standard (Euclidean) inner product,

$$\langle x, y \rangle = \sum_{i=1}^{n} x_i y_i .$$

The induced **norm** is $\|x\| = \sqrt{\langle x, x \rangle}$, and the **angle**
between nonzero vectors is defined by

$$\cos\theta = \frac{\langle x, y \rangle}{\|x\|\,\|y\|}, \qquad 0 \le \theta \le \pi .$$

The definition of the angle is only legitimate because of the Cauchy–Schwarz
inequality, proved in Section 3.1. Three consequences are used constantly:

- **Orthogonality** is $\langle x, y \rangle = 0$. It is the only notion of
  "independent directions" the module uses, and least squares is built from it.
- **Length** is a physical statement only after units are attached. The norm of
  the sample above is $\|\mathbf{u}\| = 1.949461$ *counts*; comparing that with a
  velocity vector is meaningless.
- **Scaling is not innocent.** Multiplying columns of a matrix by constants — that
  is, changing the units of individual model parameters — leaves the model space
  unchanged but changes the Euclidean geometry, and therefore changes which model
  a least-squares fit will choose. Section 4 makes this the lesson's main point.

### 2.3 Linear independence, span, basis

Vectors $v_1, \dots, v_k$ are **linearly independent** if
$\sum_i c_i v_i = \mathbf{0}$ has only the trivial solution $c = \mathbf{0}$.
Equivalently, no one of them is a combination of the others. The **span** of a
set is the vector space of all its linear combinations, and a **basis** is an
independent spanning set. Every basis of a vector space has the same number of
elements; that number is the **dimension**, and it is the invariant that rank
generalises to maps in [01-07-04](./04-rank-and-nullspace.md).

Three properties worth stating once and remembering:

- **Existence of coordinates.** If $B = \{b_1,\dots,b_n\}$ is a basis of $V$, every
  $v \in V$ has a *unique* representation $v = \sum_i c_i b_i$. The $c_i$ are the
  *coordinates* of $v$ in $B$.
- **Coordinates depend on the basis; the vector does not.** This is Section 3.3.
- **An orthonormal basis makes coordinates free.** If $\langle b_i, b_j
  \rangle = \delta_{ij}$ then $c_i = \langle v, b_i \rangle$: no linear solve is
  needed. That is why Gram–Schmidt, QR and the SVD, which all build orthonormal
  bases, are worth their cost.

## 3. Step-by-step derivations

### 3.1 Cauchy–Schwarz, and why the angle is well defined

Claim: $|\langle x, y \rangle| \le \|x\|\,\|y\|$ for all $x, y$. Consider

$$0 \le \|x - ty\|^2 = \|x\|^2 - 2t\langle x, y\rangle + t^2\|y\|^2$$

for real $t$. This is a quadratic in $t$ that is never negative, so its
discriminant is at most zero:

$$4\langle x, y\rangle^2 - 4\|x\|^2\|y\|^2 \le 0 ,$$

which is the claim. Equality holds if and only if $x$ and $y$ are parallel, in
which case the quadratic has a double root.

Two consequences, both verified numerically in Section 5:

- **The triangle inequality follows**: $\|x + y\|^2 = \|x\|^2 + 2\langle x,y\rangle
  + \|y\|^2 \le \|x\|^2 + 2\|x\|\|y\| + \|y\|^2 = (\|x\|+\|y\|)^2$.
- **$|\cos\theta| \le 1$**, so $\theta$ is defined for all nonzero vectors.

### 3.2 Gram–Schmidt, with an error estimate

Given independent vectors $v_1, \dots, v_k$, the classical Gram–Schmidt
construction is

$$w_j = v_j - \sum_{i<j} \langle v_j, e_i \rangle e_i , \qquad
e_j = \frac{w_j}{\|w_j\|} .$$

Each step removes from $v_j$ every component already present in the directions
found so far. The result is orthonormal, and the size of the residual $\|w_j\|$
before normalisation measures how much *new* direction $v_j$ contributes.

That residual is also the source of the method's numerical weakness. The inner
products are computed with already-rounded vectors, so the cancellation in
$w_j = v_j - \sum_i (\dots) e_i$ can destroy accuracy when $\|w_j\|$ is small
relative to $\|v_j\|$ — precisely the case in which you are trying to decide
whether the vectors are independent. Using the explicit example of Section 5 with
$v_1 = (2,1,0)$, $v_2 = (1,2,-1)$, $v_3 = (0,1,2)$, all three residuals are large
and the orthonormality check returns off-diagonal inner products of magnitude
$5.6\times 10^{-17}$ — the round-off floor, as expected for a well-conditioned
input.

For a *rank-revealing* factorisation one uses Householder QR with column pivoting
([01-07-07](./07-orthogonality.md)) or the SVD ([01-07-08](./08-svd.md)), both of
which decide rank from the diagonal magnitudes rather than from a difference.
Gram–Schmidt is the version to *understand*; it is not the version to trust at a
rank boundary.

### 3.3 Change of basis worked out

Let basis $A$ be the standard one, $a_1 = (1,0)$, $a_2 = (0,1)$, and let basis
$B$ be the same plane rotated by $30^{\circ}$:

$$b_1 = (\cos 30^{\circ}, \sin 30^{\circ}) = (0.866025,\ 0.500000), \qquad
b_2 = (-\sin 30^{\circ}, \cos 30^{\circ}) = (-0.500000,\ 0.866025).$$

Take the model vector $m = (1,1)$, in $\mathrm{s/km}$. Because $B$ is orthonormal,
the coordinates are inner products:

$$m = \langle m, b_1\rangle b_1 + \langle m, b_2 \rangle b_2, \qquad
\langle m, b_1 \rangle = 1.366025, \qquad \langle m, b_2 \rangle = 0.366025 .$$

So the same model is $(1,1)$ in $A$ and $(1.366025, 0.366025)$ in $B$. The
reconstruction returns $(1.000000000, 1.000000000)$ with error $0$, and
$\|m\| = 1.414214$ in both bases — as it must, because a rotation is an isometry.

Now the point. Suppose the physics is a *directional* property: a dyke striking
NE, or anisotropy aligned with a shear zone. In basis $A$ that property is a
coupled pair of numbers and the natural regularisation — "keep the model small" —
is unrelated to the geology. In basis $B$, aligned with the structure, the
property is one coordinate. The model space is the same; the *statement you can
make* is not. This is why redesigning a parameterisation is the most powerful
single tool in inverse theory, and why
[01-07-07](./07-orthogonality.md) Section 4 insists on centring and scaling.

For a general (non-orthogonal) basis the coordinates are found by solving a
linear system, which is lesson [01-07-03](./03-systems-and-elimination.md)'s
subject:

$$Pc = v, \qquad P = [\,b_1\ b_2\ \cdots\ b_n\,] .$$

### 3.4 Independence is a continuum, not a switch

Two vectors $v = (1,1,0)$ and $w = (1, 1+\delta, 0)$ are independent for *every*
$\delta > 0$: the exact algebraic rank of $\{v, w\}$ is 2 for all $\delta \neq 0$.
But the angle between them is $\arctan$-small, the second vector is a negligible
perturbation of the first, and any algorithm that decides independence from
computed numbers has to choose a threshold. Running the orthonormalisation with a
residual-norm tolerance of $10^{-12}$ gives the following, which is the honest
statement of the situation:

| $\delta$ | numerical rank found | angle (deg) |
|---|---|---|
| $10^{-1}$ | 2 | $2.726\times 10^{0}$ |
| $10^{-3}$ | 2 | $2.863\times 10^{-2}$ |
| $10^{-6}$ | 2 | $2.865\times 10^{-5}$ |
| $10^{-9}$ | 2 | $1.207\times 10^{-6}$ |
| $10^{-12}$ | 1 | $0.000$ |

Note the $10^{-9}$ row: the *angle* is reported as $1.2\times 10^{-6}$ degrees
where the exact value is $2.9\times 10^{-8}$. The angle computation loses accuracy
for nearly parallel vectors because $\arccos$ is ill-conditioned near 1 — a
cancellation, not a bug. So even the diagnostic needs a stable formulation (compute
$\|w\|/\|v\|$ from the orthogonalisation instead of $\arccos$ of a near-unit
cosine; or use the SVD). At $\delta = 10^{-12}$ the residual falls below the
tolerance and the rank is reported as 1.

Practical rule: state the tolerance, and tie it to the data's precision. A rank
decision without a tolerance is not a statement about anything physical.

## 4. Physical interpretation

**Model space and data space are different spaces with different units, and
neither is naturally Euclidean.** The set of models is a vector space, and so is
the set of data, but adding a slowness to a travel time is meaningless. Every
inner product used in this module is therefore a *choice*, and a choice with
physical content:

- $\|m\|$ with all cells in $\mathrm{s/km}$ says that a 1 % change in one cell
  costs the same as a 1 % change in any other, regardless of the cell's size or
  how well it is sampled. That is an assumption about the geology.
- Weighting by measurement uncertainty — the honest inner product for data — is
  $\|d\|_W^2 = d^\mathsf{T}W d$ with $W = C_d^{-1}$. This is the natural
  generalisation, and it is what [01-07-07](./07-orthogonality.md) Section 5
  computes with.

**Independence has a survey meaning.** If two rows of a data kernel are linearly
dependent, two of your measurements say exactly the same thing, and one of them
was wasted — or, if the survey was designed that way deliberately, it is a
repeatability check. In [01-07-04](./04-rank-and-nullspace.md) this becomes a
left null space; in [01-07-08](./08-svd.md) it becomes data leverage.

**A basis is a parameterisation, and a bad parameterisation is a self-inflicted
injury.** Two parameterisations with identical spanning sets can differ by nine
orders of magnitude in condition number (Section 4 of
[01-07-07](./07-orthogonality.md) shows exactly this with a polynomial basis:
$\kappa = 40$ centred and scaled against $\kappa = 3.3\times10^{9}$ in raw
metres). No algorithm can rescue that; only a better basis can.

**Particle motion is the geophysical face of Gram–Schmidt.** Three components of a
seismic arrival are rarely mutually orthogonal in the recorded frame. Rotating to
the principal polarisation directions — P, SV, SH — is an orthonormalisation, and
it is done so that the three resulting traces can be interpreted as distinct
arrivals rather than as mixtures. The order in which you orthogonalise matters
when the vectors are close, which is the same statement as the tolerance problem
of Section 3.4.

## 5. Python demonstration

The companion script is
[`code/vectors_and_spaces_demo.py`](./code/vectors_and_spaces_demo.py), with six
sections: a three-component recording, inner products and the Cauchy–Schwarz
identity, Gram–Schmidt on non-orthogonal vectors, coordinates in the new basis,
two parameterisations of one model, and the numerical independence threshold.

Section 1, on the three-component sample $\mathbf{u} = (0.80, -0.52, 1.70)$:

```
  ||u||            = 1.949461  counts
  u / ||u||        = (0.410370, -0.266740, 0.872036)
  angle to N axis  = 65.7719 deg
  angle to E axis  = 105.4704 deg
  angle to Z axis  = 29.3039 deg
  back azimuth from north      = 326.9761 deg
```

The incidence angle from the vertical is the angle to the $Z$ axis, $29.3039^{\circ}$.
The back azimuth is computed as $\operatorname{atan2}(-E, N) = 326.9761^{\circ}$,
which is consistent with the horizontal part $(0.80, -0.52)$ pointing north-west.
Two independent numbers, an amplitude and a direction, are recovered from three
components: the triple was never three independent numbers.

The quantified outputs of the remaining sections:

| Section | Observed | Interpretation |
|---|---|---|
| 2, Cauchy–Schwarz | $a = (3,-1,2)$, $b = (1,4,-2)$: $a\cdot b = -5$ against $\|a\|\|b\| = 17.146428$ | the bound holds with room, and the angle is obtuse at $106.9541^{\circ}$ |
| 2, triangle | $\|a+b\| = 5.000000 \le \|a\| + \|b\| = 8.324233$ | equality only for parallel vectors |
| 2, parallelogram | $\|a+b\|^2 - (\|a\|^2 + \|b\|^2) = -10.000000 = 2a\cdot b$ | the identity that makes the inner product geometric |
| 3, Gram–Schmidt | $\langle e_i, e_j \rangle$ off-diagonal $= 5.551\times10^{-17}$ | orthonormal to the round-off floor |
| 4, coordinates of $v_3$ | $(0.447214, -0.478091, 2.138090)$ | reconstruction error $0.000$ |
| 5, model in basis $B$ | $(1.366025, 0.366025)$ | same vector, different coordinates |
| 6, rank at $\delta = 10^{-12}$ | 1 (with a warning printout) | independence is threshold-dependent |

> **Breaking exercise.** In Section 3 the vectors are $v_1=(2,1,0)$,
> $v_2=(1,2,-1)$, $v_3=(0,1,2)$ and they come out independent with comfortable
> margins. Replace $v_3$ by $v_1 + v_2 = (3,3,-1)$ and predict, *before running*,
> what the third residual norm will be and what the script will print. Then
> perturb: use $v_1 + v_2 + 10^{-10}\hat{z}$ and see where the tolerance decides.

## 6. Exercises

Full set and worked solutions:
[`exercises/01-vectors-and-spaces-exercises.md`](./exercises/01-vectors-and-spaces-exercises.md)
and
[`exercises/01-vectors-and-spaces-solutions.md`](./exercises/01-vectors-and-spaces-solutions.md).
Four to start with:

**★1.** For $a = (2,-1,2)$ and $b = (1,3,-2)$ compute $\|a\|$, $\|b\|$,
$\langle a, b\rangle$, the angle between them, and $\|a+b\|$. Confirm the
Cauchy–Schwarz inequality and the parallelogram identity
$\|a+b\|^2 + \|a-b\|^2 = 2\|a\|^2 + 2\|b\|^2$.

**★2.** Which of these sets are vector spaces over $\mathbb{R}$? Justify each in
one line. (a) $\{(x, y, z) : x + 2y - z = 0\}$; (b) $\{(x,y,z) : x + 2y - z = 1\}$;
(c) the set of $2\times 2$ matrices with zero trace; (d) the set of invertible
$2\times 2$ matrices.

**★★3.** A three-component recording gives $\mathbf{u} = (1.2, 0.9, -1.4)$ in
(N, E, Z). (a) Compute the incidence angle from the vertical and the back azimuth.
(b) The horizontal components are rotated by $40^{\circ}$ clockwise; write the new
triple. (c) State which quantities in (a) are invariant under that rotation and
which are not, and why.

**★★4.** Orthonormalise $v_1 = (1,1,1)$, $v_2 = (1,-1,0)$, $v_3 = (0,1,-1)$ by
hand, then verify by computing all inner products. Report the residual norm at
each step and explain what the smallest residual tells you about the conditioning
of the set.

**★★★5.** Two candidate parameterisations of the same 2-D model space are
$A = \{(1,0),(0,1)\}$ and $B = \{(1,1)/\sqrt2, (1,-1)/\sqrt2\}$. A model is
$m = (0.05,-0.02)$ in $\mathrm{s/km}$. (a) Give its coordinates in both bases.
(b) Compute $\|m\|$ in both. (c) Suppose a regularisation term penalises
$\|c\|^2$ where $c$ are the coordinates. Compute the penalty for the same model in
each basis and explain why the two differ. (d) Which basis would you choose if the
prior belief were "the two cells are probably perturbed in opposition"?

**★★★6.** Reproduce the rank-versus-$\delta$ table of Section 3.4 with your own
code at tolerances $10^{-8}$, $10^{-12}$ and $10^{-15}$. (a) Report the values of
$\delta$ at which the numerical rank changes in each case. (b) Explain why the
transition $\delta$ scales with the tolerance. (c) The angle column is inaccurate
above $\delta = 10^{-9}$; quantify that by comparing with $\arcsin(\delta/\sqrt2)$
and explain the mechanism.

## 7. Common mistakes

1. **Treating a list of numbers as a vector without checking the axioms.** The
   set of positive densities is not a vector space (no additive identity), and
   neither is the set of unit vectors. Guessing wrong leads to nonsense like
   averaging phases or normalising a model in the wrong norm.
2. **Reading the inner product as similarity.** $\langle a,b \rangle = -5$ says
   the vectors disagree, not that they are unrelated. Correlation removes the
   means first; an inner product does not.
3. **Adding vectors with different units.** $\|m\|$ is meaningful only after every
   component is in the same unit, and $\|d\|$ likewise. Mixing them produces a
   number that no physical comparison can use.
4. **Assuming independence is a yes/no question.** It is a statement about
   $\delta$ versus your tolerance, as the table in Section 3.4 shows.
5. **Trusting a normalised vector at the round-off boundary.** $w/\|w\|$ with
   $\|w\| = 10^{-14}$ amplifies noise by $10^{14}$; every such division needs a
   threshold and a comment.
6. **Forgetting that the basis was a choice.** A model that looks large in one
   parameterisation may be small in another, and a "small-model" regularisation
   silently adopts whatever basis you happen to have.
7. **Confusing dimension with the number of numbers written down.** A
   three-component recording has three components and two independent physical
   quantities (amplitude, direction) at one instant; an $n \times n$ matrix has
   $n^{2}$ entries and only $n(n+1)/2$ independent ones if symmetric.
8. **Thinking orthonormalisation is always safe.** Classical Gram–Schmidt loses
   accuracy exactly when vectors are nearly dependent, which is exactly when you
   need the answer.

## 8. Real-world applications

- **Three-component seismic processing.** Rotation into the ray frame, principal
  polarisation analysis and the estimation of anisotropy all reduce to choosing a
  basis and computing coordinates. The rectilinearity of the eigenvalues of the
  covariance matrix is the standard polarisation diagnostic.
- **Parameterisation of an inversion.** Whether a tomographic model is
  parameterised by cell slowness, by spline knots, or by a truncated spatial
  basis set determines the condition number, the resolution and the meaning of
  the regularisation. Basis choice is the highest-leverage decision in the design
  of an inversion. See [18-inverse-problems](../../18-inverse-problems/README.md).
- **Stress and strain axes.** Principal stresses are coordinates in an
  eigenvector basis; the basis is where the tensor becomes diagonal, and the whole
  calculation is the subject of [01-07-06](./06-eigenvalues.md).
- **Normal-mode and receiver-function analysis.** Spheroidal and toroidal modes,
  or radial and transverse receiver functions, are orthogonal decompositions
  chosen so that physically distinct phenomena appear in distinct coordinates.
  See [06-seismology](../../06-seismology/README.md).
- **Data weighting.** Declaring $W = C_d^{-1}$ is choosing the inner product in
  which the misfit is measured, and therefore choosing which data the inversion
  obeys. This is the arrival-time-versus-amplitude weighting argument in every
  full-waveform inversion paper.
- **Coordinate bases in geodesy.** Converting between geographic, geocentric and
  local topocentric frames is a change of basis applied to station positions and
  velocities, with the same mathematics and different units on each axis.

## 9. Further reading

- **Strang, G. *Introduction to Linear Algebra.* Wellesley–Cambridge Press.** The
  four fundamental subspaces, independence and basis, presented for people who
  want to compute. Level: beginner to intermediate. Any recent edition.
- **Strang, G. *Linear Algebra and Its Applications.* Cengage.** A more
  applications-oriented treatment with the same authorial voice. Level:
  beginner to intermediate.
- **Trefethen, L. N., & Bau, D. *Numerical Linear Algebra.* SIAM.** The source for
  Section 3.4: it explains why classical Gram–Schmidt is not rank-revealing and
  what to use instead. Level: intermediate to advanced. Lecture 7 in particular.
- **Golub, G. H., & Van Loan, C. F. *Matrix Computations.* Johns Hopkins
  University Press.** The reference for the error analysis of the
  orthonormalisations. Level: advanced.
- **Menke, W. *Geophysical Data Analysis: Discrete Inverse Theory.* Academic
  Press.** Introduces model space and data space exactly as this lesson does, and
  immediately uses them for inversion. Level: intermediate. Any recent edition.
- **Aki, K., & Richards, P. G. *Quantitative Seismology.* University Science
  Books.** Chapter 1 for vectors and tensors in a seismological setting, and the
  polarisation material. Level: advanced.

> Note on citations: bibliographic details above are given so that you can
> locate the works. This repository does not host or reproduce copyrighted text,
> and you should confirm editions and current availability through your library
> before citing them yourself.

## 10. Self-assessment checklist

- [ ] I can state the vector-space axioms and use them to *reject* a candidate set.
- [ ] I can compute a norm, an inner product and an angle, and say what each means
      physically for a given measurement.
- [ ] I can prove Cauchy–Schwarz from the non-negativity of a quadratic, and I can
      derive the triangle inequality from it.
- [ ] I can carry out Gram–Schmidt on three 3-D vectors by hand and report the
      residual norms.
- [ ] I can give the coordinates of a vector in two different bases and verify
      that the vector is unchanged.
- [ ] I can explain why an orthonormal basis makes coordinates a matter of inner
      products only.
- [ ] I can state the tolerance I used for a rank decision and justify it from the
      data precision.
- [ ] I can name a case in geophysics where the choice of basis *is* the modelling
      decision.

## 11. Related lessons

- [01-07-02 Matrices, Matrix Multiplication and Linear Maps](./02-matrices-and-operations.md) —
  what happens to these vectors when a matrix acts on them.
- [01-07-04 Rank, Null Space and Solvability](./04-rank-and-nullspace.md) — where
  independence becomes the statement of what an experiment cannot see.
- [01-07-06 Eigenvalues, Eigenvectors and Diagonalisation](./06-eigenvalues.md) —
  the basis that makes a symmetric operator diagonal, and the physical meaning of
  the coordinates in it.
- [01-07-07 Orthogonality, Projections and Least Squares](./07-orthogonality.md) —
  the machinery that turns a basis into a projection, and the centring and scaling
  argument.
- [01-07-08 Singular Value Decomposition and Rank Truncation](./08-svd.md) — the
  two orthonormal bases that a linear map comes with for free, and the reason they
  are the right ones.
- [01-01-04 Floating-Point Representation, Round-Off and Catastrophic Cancellation](../01-arithmetic/04-floating-point.md) —
  the arithmetic behind the tolerance discussion of Section 3.4.
- [01-16 Functional Analysis for Inverse Problems](../16-functional-analysis/README.md) —
  the same concepts when the model space is infinite-dimensional.
