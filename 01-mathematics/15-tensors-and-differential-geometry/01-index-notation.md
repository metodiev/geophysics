---
id: 01-15-01
title: "Index Notation, Einstein Summation and Kronecker Delta"
level: advanced
prereqs: ["01-06-04", "01-06-07", "01-07-02"]
estimated_minutes: 90
tags: [index-notation, einstein-summation, kronecker-delta, tensors]
---

# Index Notation, Einstein Summation and Kronecker Delta

## Learning objectives

By the end of this lesson you will be able to:

1. **Read and write** any tensor expression in index notation, and state which
   indices are free and which are summed.
2. **Translate** in both directions between index form and matrix form: product,
   transpose, trace, quadratic form, determinant, and the symmetric and
   antisymmetric parts of a matrix.
3. **Apply** the substitution property of the Kronecker delta
   $\delta_{ij}a_j = a_i$ and the contraction $\delta_{ii} = 3$ without hesitating,
   and explain why the number three is the dimension of space.
4. **Derive** the epsilon-delta identity
   $\varepsilon_{ijk}\varepsilon_{ilm} = \delta_{jl}\delta_{km} - \delta_{jm}\delta_{kl}$
   and use it to prove the two structural vector identities
   $\nabla\cdot(\nabla\times\mathbf{F}) = 0$ and
   $\nabla\times(\nabla f) = \mathbf{0}$.
5. **Write** the elastodynamic equation of motion in index form, and reduce it
   to the familiar vector form for an isotropic medium.
6. **Recognise** the four mistakes that make an index expression meaningless,
   and check any expression you write against them.

## Prerequisites

- [01-06-04 Divergence, Curl and Physical Meaning](../06-multivariable-calculus/04-divergence-and-curl.md)
  — the objects being rewritten here. Index notation does not replace the
  meaning of divergence and curl; it makes them computable.
- [01-06-07 Vector Identities and Their Role in Geophysics](../06-multivariable-calculus/07-vector-identities.md)
  — the identities that this lesson finally proves instead of quoting.
- [01-07-02 Matrices and Matrix Operations](../07-linear-algebra/02-matrices-and-operations.md)
  — matrix products, transposes and traces, which index notation reproduces
  exactly.

## 1. Intuition: the notation earns its place

Linear elasticity relates stress to strain through a fourth-rank tensor,

$$\sigma_{ij} = C_{ijkl}\,e_{kl}. \tag{1}$$

Written out, that single line is nine equations, each with nine terms on the
right. The object $C$ carries four indices, so it has
$3^4 = 81$ components, and no two-dimensional array can display it. Try to write
equation (1) without indices and you must either invent a four-dimensional
"matrix" or write nine lines like

$$\sigma_{xx} = C_{xxxx}e_{xx} + C_{xxxy}e_{xy} + \dots$$

which nobody can check and nobody can trust. Index notation is not decoration. It
is the smallest notation in which the physics can be written at all. When general
elasticity is eventually reduced to the 21 independent constants that a real
crystal possesses, the reduction will be done by counting indices, not by
manipulating an 81-element array by hand.

Two rules carry almost all the weight:

1. **A free index appears exactly once in every term** of an equation, and each
   term must carry the same free indices. Free indices are the ones that label
   output components.
2. **An index that appears exactly twice in a term is summed** over its range, in
   this course $1,2,3$ standing for $x,y,z$. Such an index is called a *dummy*
   and may be renamed freely, because the sum does not know its name.

Everything else in this lesson is bookkeeping around those two rules.

## 2. Precise definitions

### 2.1 Indices, free and dummy

Indices are written as subscripts in this course: $a_i$, $A_{ij}$,
$C_{ijkl}$. A term is a product of such objects. In one term:

- an index occurring **once** is free;
- an index occurring **twice** is summed, and only twice — three occurrences make
  the expression meaningless;
- the *number of free indices* is the rank of the resulting object: no free index
  means a scalar, one means a vector, two means a matrix-like object.

For example, in $A_{ij}x_j$ the index $i$ is free and $j$ is summed, so the term
has one free index and represents the vector $A\mathbf{x}$. In $A_{ij}x_i x_j$
both indices are summed, so the term is a scalar: the quadratic form
$\mathbf{x}^{\mathsf T}A\mathbf{x}$.

### 2.2 The summation convention

Any index repeated exactly twice in a term is summed over $1,2,3$. Thus

$$a_ib_i \equiv \sum_{i=1}^{3} a_ib_i = a_1b_1 + a_2b_2 + a_3b_3, \qquad
A_{ii} \equiv \sum_{i=1}^{3} A_{ii} = A_{11} + A_{22} + A_{33}.$$

If a term contains two *distinct* repeated pairs, the sum is a double sum:
$A_{ij}B_{ij}$ means $\sum_{i=1}^{3}\sum_{j=1}^{3}A_{ij}B_{ij}$, a nine-term sum,
not a trace. Two occurrences of the same symbol in three slots, as in
$A_{ii}B_{ii}$, is a mistake: $i$ cannot be summed twice, and the expression must
be rewritten with a fresh name.

When the dimension is not three — electrical resistivity in a 2-D section, for
instance — state the range explicitly, because every contraction changes with it.
The entire difference between plane stress and plane strain, and the reason a 2-D
elastic code cannot simply reuse 3-D constants, is a contraction range.

### 2.3 The Kronecker delta

$$\delta_{ij} = \begin{cases} 1, & i = j,\\ 0, & i \neq j.\end{cases}$$

Its defining property is substitution:

$$\delta_{ij}a_j = a_i, \qquad \delta_{ij}A_{jk} = A_{ik}, \qquad
\delta_{ij}\delta_{jk} = \delta_{ik}. \tag{2}$$

Why: the sum $\delta_{ij}a_j$ has three terms, and all are zero except the one
with $j = i$. The delta renames an index. Contracting its two indices gives the
dimension of the space, $\delta_{ii} = 3$, which is the only number in this
lesson that knows how many dimensions it lives in.

### 2.4 The Levi-Civita symbol

$$\varepsilon_{ijk} = \begin{cases}
+1, & (i,j,k) \text{ an even permutation of } (1,2,3),\\
-1, & (i,j,k) \text{ an odd permutation of } (1,2,3),\\
0, & \text{any index repeated.}
\end{cases}$$

It is totally antisymmetric: swapping any two indices flips the sign, so
$\varepsilon_{ijk} = -\varepsilon_{ikj} = -\varepsilon_{jik}$. It exists only in
three dimensions in this form; the analogous object in $n$ dimensions has $n$
indices. With it, the cross product and the curl become pure algebra:

$$(\mathbf{a}\times\mathbf{b})_i = \varepsilon_{ijk}a_jb_k, \qquad
(\nabla\times\mathbf{F})_i = \varepsilon_{ijk}\frac{\partial F_k}{\partial x_j}
= \varepsilon_{ijk}F_{k,j}. \tag{3}$$

### 2.5 Comma notation

A comma followed by an index means a partial derivative with respect to that
coordinate:

$$u_{i,j} \equiv \frac{\partial u_i}{\partial x_j}, \qquad
u_{i,jj} \equiv \frac{\partial^2 u_i}{\partial x_j\partial x_j}, \qquad
\sigma_{ij,j} \equiv \frac{\partial \sigma_{ij}}{\partial x_j}.$$

The comma is not punctuation; it converts a coordinate label into a derivative
operator. This is the notation in which every equation of continuum mechanics is
published, and it is the only one that stays readable when the material is
anisotropic.

### 2.6 Four rules for manipulating expressions

| Rule | Statement | Example |
|---|---|---|
| Substitution | A delta renames an index | $\delta_{ij}b_{jk} = b_{ik}$ |
| Renaming a dummy | A summed index may be renamed in one term | $a_ib_i = a_jb_j$ |
| Renaming a free index | A free index must be renamed in *every* term | $c_i = a_ib_jx_j \Rightarrow c_k = a_kb_jx_j$ |
| Factoring | Factor only what is common to all terms | $a_ib_i + a_ic_i = a_i(b_i + c_i)$ |

The third rule is where most errors occur. Renaming a free index in one term but
not the others changes the meaning of the equation silently.

## 3. Derivations

### 3.1 The delta substitutes, and the delta's trace is the dimension

Expand the definition:

$$\delta_{ij}a_j = \sum_{j=1}^{3}\delta_{ij}a_j
= \underbrace{0}_{j\neq i} + a_i + \underbrace{0}_{j\neq i} = a_i. \qquad\square$$

Similarly $\delta_{ii} = \delta_{11} + \delta_{22} + \delta_{33} = 3$. Nothing is
hidden: the delta selects, and its trace counts the number of directions it can
select. In $n$ dimensions the same calculation gives $\delta_{ii} = n$, which is
why the combination $3\lambda + 2\mu$ appears in the three-dimensional volumetric
stress-strain relation of Section 3.6 and a different combination would appear in
two dimensions.

### 3.2 The epsilon-delta identity

We prove

$$\varepsilon_{ijk}\varepsilon_{ilm} = \delta_{jl}\delta_{km} - \delta_{jm}\delta_{kl}. \tag{4}$$

*Proof by cases.* First suppose $j = k$. Then the left side contains
$\varepsilon_{ijk}$ with a repeated index and vanishes, and the right side is
$\delta_{jl}\delta_{jm} - \delta_{jm}\delta_{jl} = 0$. Both sides vanish.

Now suppose $j \neq k$. The sum over $i$ then has exactly one nonzero term — the
one in which $i$ is the third value distinct from $j$ and $k$, call it $i_0$ — so
$\varepsilon_{i_0jk} = \pm 1$. The factor $\varepsilon_{i_0lm}$ can be nonzero
only if $\{l,m\} = \{j,k\}$, so if $\{l,m\} \neq \{j,k\}$ both sides vanish again.

It remains to check the two orderings of $(l,m)$ when $\{l,m\} = \{j,k\}$:

- $(l,m) = (j,k)$: left side $= \varepsilon_{i_0jk}\,\varepsilon_{i_0jk} = 1$;
  right side $= \delta_{jj}\delta_{kk} - \delta_{jk}\delta_{kj} = 1 - 0 = 1$.
- $(l,m) = (k,j)$: left side $= \varepsilon_{i_0jk}\,\varepsilon_{i_0kj} = -1$;
  right side $= \delta_{jk}\delta_{kj} - \delta_{jj}\delta_{kk} = 0 - 1 = -1$.

Both sides agree in every case. $\square$

Later you will recognise the right-hand side of (4) as the antisymmetrisation of
$\delta_{jl}\delta_{km}$, which is the structural reason the identity works in any
dimension once the epsilon symbols are given the corresponding number of indices.

Two contractions follow immediately by setting $l = j$ in (4):

$$\varepsilon_{ijk}\varepsilon_{ijm} = 2\delta_{km}, \qquad
\varepsilon_{ijk}\varepsilon_{ijk} = 6 = 3!. \tag{5}$$

### 3.3 Determinants

The determinant of a $3\times3$ matrix is the fully antisymmetrised triple
product of its rows:

$$\det A = \varepsilon_{ijk}A_{1i}A_{2j}A_{3k}, \qquad
\det A = \tfrac{1}{6}\varepsilon_{ijk}\varepsilon_{lmn}A_{il}A_{jm}A_{kn}.$$

The six terms of the cofactor expansion and the six permutations counted by
$\varepsilon$ are the same six terms. This is why the epsilon-delta identity can
be used to prove linear-algebra relations that otherwise require pages of
expansion.

### 3.4 Two structural identities, proved rather than quoted

**Claim 1.** $\nabla\cdot(\nabla\times\mathbf{F}) = 0$. In index form the
divergence of $\varepsilon_{ijk}F_{k,j}$ is
$\varepsilon_{ijk}F_{k,ji}$. The factor $F_{k,ji}$ is symmetric under $i
\leftrightarrow j$ (mixed partial derivatives commute for a twice continuously
differentiable field), while $\varepsilon_{ijk}$ is antisymmetric. A symmetric
object contracted with an antisymmetric one gives zero:

$$\varepsilon_{ijk}F_{k,ji} = -\varepsilon_{jik}F_{k,ji}
= -\varepsilon_{ijk}F_{k,ij} = -\varepsilon_{ijk}F_{k,ji} = 0. \qquad\square$$

The second equality relabels the dummy indices, the third uses symmetry of the
second derivative, and the conclusion is that the expression equals its own
negative.

**Claim 2.** $\nabla\times(\nabla f) = \mathbf{0}$. In index form,
$(\nabla\times\nabla f)_i = \varepsilon_{ijk}f_{,kj}$. The second derivative is
symmetric in $j,k$; the epsilon is antisymmetric. Hence zero. $\square$

**Claim 3.** $\nabla\cdot(\mathbf{a}\times\mathbf{b}) =
\mathbf{b}\cdot(\nabla\times\mathbf{a}) -
\mathbf{a}\cdot(\nabla\times\mathbf{b})$. Differentiate the product:

$$\partial_i\varepsilon_{ijk}a_jb_k
= \varepsilon_{ijk}(\partial_ia_j)b_k + \varepsilon_{ijk}a_j(\partial_ib_k).$$

In the first term, $\varepsilon_{ijk}\partial_ia_j = (\nabla\times\mathbf{a})_k$,
and pairing it with $b_k$ gives the first term on the right. In the second,
$\varepsilon_{ijk}a_j\partial_ib_k = -\varepsilon_{jik}a_j\partial_ib_k
= -a_j(\nabla\times\mathbf{b})_j$. Summing the two gives the claim. $\square$

These are the identities of
[01-06-07](../06-multivariable-calculus/07-vector-identities.md), now obtained in
three lines each instead of by component expansion.

### 3.5 The elastodynamic equation in index form

Conservation of linear momentum for a continuum with density $\rho$ and
displacement $\mathbf{u}$ is

$$\rho\,\ddot{u}_i = \sigma_{ij,j} + f_i, \tag{6}$$

where $\sigma$ is the Cauchy stress of
[01-15-03](./03-strain-and-stress-tensors.md) and $f_i$ is a body force per unit
volume. Inserting Hooke's law (1) with the infinitesimal strain
$e_{kl} = \tfrac{1}{2}(u_{k,l} + u_{l,k})$ gives the general anisotropic
elastodynamic equation

$$\rho\,\ddot{u}_i = \bigl(C_{ijkl}u_{k,l}\bigr)_{,j} + f_i, \tag{7}$$

which is the form implemented in every finite-difference anisotropic modelling
code. For an **isotropic** medium,
$C_{ijkl} = \lambda\delta_{ij}\delta_{kl}
+ \mu(\delta_{ik}\delta_{jl} + \delta_{il}\delta_{jk})$, and the deltas do their
work:

$$C_{ijkl}u_{k,l} = \lambda u_{k,k}\delta_{ij}
+ \mu(u_{i,j} + u_{j,i}) = \lambda u_{k,k}\delta_{ij} + 2\mu u_{(ij)},$$

with $u_{(ij)} \equiv \tfrac{1}{2}(u_{i,j} + u_{j,i})$ the symmetric part.
Differentiating and contracting,

$$\bigl(C_{ijkl}u_{k,l}\bigr)_{,j}
= \lambda u_{k,ki} + \mu\bigl(u_{i,jj} + u_{j,ij}\bigr)
= (\lambda + \mu)u_{j,ji} + \mu u_{i,jj},$$

so that

$$\rho\,\ddot{\mathbf{u}} = (\lambda + \mu)\nabla(\nabla\cdot\mathbf{u})
+ \mu\nabla^2\mathbf{u} + \mathbf{f}, \tag{8}$$

the textbook form. The step that is easy to get wrong is the antisymmetric part
of $u_{k,l}$: it survives in $u_{i,j} + u_{j,i} = 2u_{(ij)}$ only through the
symmetric combination, and Section 3 of the demonstration checks numerically that
the antisymmetric part contributes nothing to a quadratic form, which is the same
statement in another guise.

Taking the divergence and the curl of (8) separately yields the P and S wave
equations with speeds
$\alpha = \sqrt{(\lambda+2\mu)/\rho}$ and $\beta = \sqrt{\mu/\rho}$, the
derivation completed in
[02-04-05](../../02-physics/04-elasticity-and-continuum-mechanics/05-elastodynamics.md).

### 3.6 Symmetric and antisymmetric parts

Any rank-2 object splits into parts with different symmetry:

$$A_{ij} = \underbrace{\tfrac{1}{2}(A_{ij} + A_{ji})}_{S_{ij}}
+ \underbrace{\tfrac{1}{2}(A_{ij} - A_{ji})}_{W_{ij}},
\qquad S_{ij} = S_{ji}, \quad W_{ij} = -W_{ji}.$$

$W$ has zero trace, $W_{ii} = 0$, and it vanishes in any *quadratic* form:

$$W_{ij}x_ix_j = -W_{ji}x_ix_j = -W_{ij}x_ix_j = 0,$$

where the first step swaps the names of the dummy indices and the second uses
antisymmetry. This one-line argument is why only the symmetric part of a
displacement gradient can store strain energy, and why the stress tensor of a
body in equilibrium is symmetric.

## 4. Physical interpretation

Each index operation has a physical reading, and the readings are the reason to
prefer the notation.

| Operation | Index form | Physical content |
|---|---|---|
| Gradient | $f_{,i}$ | the direction of steepest increase |
| Divergence | $v_{i,i}$ | net flux out of a point, per unit volume |
| Curl component | $\varepsilon_{ijk}v_{k,j}$ | twice the local rotation rate |
| Laplacian | $f_{,ii}$ | mismatch between a value and the local mean |
| Trace | $A_{ii}$ | the isotropic part; for strain, the volume change |
| Contraction of two tensors | $A_{ij}B_{ij}$ | a frame-independent scalar built from both |

The pattern to internalise is that **every contraction removes one direction from
the description, and what remains is invariant**. A free index is a direction
still to be specified; a summed index is a direction that has been averaged over.
A scalar has no directions left, which is exactly why it is the same in every
frame — the theme of [01-15-02](./02-tensor-algebra.md).

The Kronecker delta is the statement "do nothing" in algebraic form: it is the
identity tensor, the metric of flat space, and the reason Cartesian coordinates
need no distinction between components with different index positions. The
Levi-Civita symbol is the statement "oriented volume": it changes sign when two
directions are exchanged, which is why it appears wherever handedness matters —
the cross product, angular momentum, the magnetic field treated as a vector, and
the symmetry classes of crystals.

## 5. Assumptions and regime of validity

1. **Cartesian coordinates, orthonormal constant basis.** The comma is an
   ordinary partial derivative only when the basis vectors do not vary in space.
   In cylindrical or spherical coordinates the basis turns, extra terms appear,
   and this notation alone is insufficient — that is
   [01-15-04](./04-curvilinear-coordinates.md).
2. **Euclidean metric, so $\delta_{ij}$ raises and lowers nothing.** In a
   general metric the distinction between upper and lower indices becomes
   physical, and $\delta_{ij}$ must be replaced by $g_{ij}$
   ([01-15-06](./06-differential-geometry-earth.md)).
3. **Index range stated once.** Every contraction is over that range. Changing
   the range changes every contraction, including $\delta_{ii}$.
4. **Differentiability.** Claims 1 and 2 of Section 3.4 use equality of mixed
   partial derivatives, which needs $C^2$. At a material discontinuity the
   differential forms fail and the flux forms must be used instead — the warning
   of
   [01-06-04](../06-multivariable-calculus/04-divergence-and-curl.md).
5. **Three dimensions for $\varepsilon_{ijk}$.** The symbol with three indices is
   a three-dimensional object. In two dimensions the cross product is a scalar
   and $\varepsilon_{ij}$ has two indices.
6. **$\varepsilon$ is not a tensor under all transformations.** It is invariant
   under rotations but changes sign under a reflection, so it is a
   pseudo-tensor. That distinction is treated in
   [01-15-02](./02-tensor-algebra.md) and matters whenever a sign convention
   flips.

## 6. Python demonstration

[`code/index_notation_demo.py`](./code/index_notation_demo.py) evaluates every
identity of this lesson by explicit index loops, with no library calls, using
indices `0, 1, 2` for `x, y, z`. The residuals are therefore limited by the
central-difference step $h = 10^{-4}$, not by the algebra.

The substitution property and the dimension count:

```text
  a                     = [2.0, -5.0, 7.5]
  delta_ij a_j computed for each i:
     i=0: sum_j delta_0j a_j =    2.000   a_0 =    2.000   equal? True
     i=1: sum_j delta_1j a_j =   -5.000   a_1 =   -5.000   equal? True
     i=2: sum_j delta_2j a_j =    7.500   a_2 =    7.500   equal? True
  delta_ii = 3.0   (one term per value of the repeated index)
```

Matrix multiplication, trace and the quadratic form, all as loops:

```text
  C_ik = A_ij B_jk is matrix multiplication, and nothing else:
     [   4.00     9.00    -5.00]
     [  -1.00     1.00    -8.00]
     [  12.00     6.00     5.00]
  A_ii = trace(A)   = 0.0   (double loop, no transpose needed)
  x_i A_ij x_j       = -9.000000   x^T A x = -9.000000
```

The symmetric/antisymmetric split, including the zero that makes strain energy
possible:

```text
  max |A_ij - S_ij - W_ij| = 0.0e+00
  W_ii = 0.0e+00   (an antisymmetric tensor has zero trace)
  x_i S_ij x_j = -9.000000000000000
  x_i W_ij x_j = +0.000e+00   <- identically zero
  x_i A_ij x_j = -9.000000000000000   <- the symmetric part alone
```

The epsilon-delta identity, checked exhaustively over all $3^4 = 81$
combinations of the free indices:

```text
  index combinations tested (j,k,l,m): 81
  mismatches: 0   worst residual: 0.0e+00
  eps_ijk eps_ijk = 6.0   (= 3! = 6)
  eps_ijk eps_ikj = -6.0   (a swap of one pair flips the sign)
  det A via eps_ijk A_1i A_2j A_3k = 47.000000
  det A via cofactor expansion      = 47.000000
```

The two structural identities, where the residuals must be read carefully:

```text
  div(curl F) = -1.110e-12   (eps_ijk d_j d_k F_k = 0 by index exchange)
  curl(grad f) = ['+0.000e+00', '+0.000e+00', '+0.000e+00']
```

The first residual is genuine truncation error: the four terms being combined do
not cancel algebraically. The second is *exactly* zero in floating point, digit
for digit, because a symmetric stencil makes the mixed differences cancel
identically. A zero there is not evidence that the code is right, only that the
stencil is symmetric — the warning given in Section 5.1 of
[01-06-07](../06-multivariable-calculus/07-vector-identities.md). Reading a
numerical check honestly means knowing which of these two situations you are in.

An identity derived with eps rather than quoted, and the elastic operator:

```text
  div(a x b)              = 0.584099994
  b . curl a - a . curl b = 0.584100000
  residual                = 5.85e-09
  (C_ijkl u_k,l),j  (index form, finite differences) =
     ['-1.3700e+10', '1.3300e+10', '-3.2000e+09']
  (lam+mu) grad(div u) + mu laplacian u (analytic)   =
     ['-1.3700e+10', '1.3300e+10', '-3.2000e+09']
  largest residual 1.430e+01 Pa/m, relative to 1.370e+10 Pa/m
  -> 1.0e-09 : truncation-limited agreement, as expected.
```

The last block is the numerical form of Section 3.5: a fourth-rank isotropic
$C_{ijkl}$ contracted into a displacement field and differentiated reproduces
$(\lambda+\mu)\nabla(\nabla\cdot\mathbf{u}) + \mu\nabla^2\mathbf{u}$ to one part
in $10^9$, which is the finite-difference truncation level for $h = 10^{-4}$.

### What to observe, and why it matters

| Observation | Consequence |
|---|---|
| $\delta_{ij}a_j$ reproduces $a_i$ term by term | the delta is a renaming device, never a multiplication |
| `A_ii = 0.0` for a trace-free matrix, computed by a double loop | the trace is an index contraction, not a matrix function |
| the quadratic form is unchanged when $W$ is dropped | only symmetric parts survive in energy expressions |
| 81 index combinations, 0 mismatches for the epsilon-delta identity | the identity is algebraic; verify it once, then use it |
| `curl(grad f)` is exactly 0.0 | a zero residual can be an artefact of the stencil |

> **Breaking exercise.** Change the difference stencil in `div_fd` from central
> to one-sided. Predict, before running, which of the two structural identities
> stops cancelling exactly, and why.

## 7. Exercises

Attempt these closed-book; solutions are in
[`exercises/01-index-notation-solutions.md`](./exercises/01-index-notation-solutions.md).

**★ Foundational.** ★1 write five expressions in index form and five back;
★2 identify free and dummy indices, and reject the invalid expressions;
★3 compute $\delta_{ij}a_j$, $\delta_{ii}$, $\delta_{ij}\delta_{jk}$ and
$\varepsilon_{ijk}\varepsilon_{ijk}$; ★4 convert a matrix product, a trace and a
quadratic form.

**★★ Applied.** ★★5 prove $\varepsilon_{ijk}\varepsilon_{ilm}$ by cases and
derive the two contractions of equation (5); ★★6 reproduce $\nabla\cdot(\nabla
\times\mathbf{F}) = 0$ and $\nabla\times(\nabla f) = \mathbf{0}$; ★★7 expand the
isotropic $C_{ijkl}u_{k,l}$ into $\lambda u_{k,k}\delta_{ij} + \mu(u_{i,j} +
u_{j,i})$ index by index; ★★8 show that the antisymmetric part of a displacement
gradient cannot enter a quadratic energy.

**★★★ Research-oriented.** ★★★9 implement a small index-notation library
(generic contraction over a stated range) and check it against the matrix
operations of this lesson, reporting where it fails; ★★★10 take a published
elastic-moduli equation in index form, expand it in Cartesian components, and
state which contractions would change if the material were two-dimensional.

## 8. Common mistakes

1. **An index appearing three times.** $A_{ii}B_{ii}$ is not a legal expression;
   rename one pair, $A_{ii}B_{jj}$.
2. **Renaming a free index in only one term.** Renaming a free index changes
   which equation you are writing, so it must be done in every term.
3. **Reusing a dummy index in a nested context.** In
   $c_i = A_{ij}B_{jk}d_k$ the index $j$ appears twice and is summed correctly;
   but writing $c_i = A_{ij}B_{ik}d_k$ also sums $j$ correctly and then *subtracts*
   nothing — the two mean different things. Say out loud which index each
   contraction uses.
4. **Confusing $A_{ii}$ with $A_{ij}A_{ij}$.** The first is a sum of three terms,
   the second of nine, and they differ as soon as $A$ is not diagonal.
5. **Forgetting the dimension.** $\delta_{ii} = 3$ in three dimensions and $2$ in
   two. A 2-D elastic code that reuses $3\lambda + 2\mu$ is wrong, not
   approximately right.
6. **Trusting a zero residual.** $\nabla\times\nabla f$ cancels exactly on any
   symmetric stencil, so the check cannot fail. Test the identity where the terms
   do not cancel.
7. **Using index notation in a curvilinear basis.** The comma is a partial
   derivative with respect to a *coordinate*, while a physical component is
   differentiated with respect to an *arc length*. The two differ by the scale
   factors of [01-15-04](./04-curvilinear-coordinates.md).
8. **Treating $\varepsilon_{ijk}$ as an ordinary tensor.** It is invariant under
   proper rotations and flips sign under reflections, which is exactly why
   "axial vector" is a separate category.

## 9. Real-world applications

- **Anisotropic seismic modelling.** Every finite-difference elastic code
  evaluates (7) in index form: two nested loops over the four indices of $C$,
  inner loops for the strain and the divergence of stress. Writing it in index
  form is what makes the code short enough to be checkable.
- **Moment tensors.** An earthquake's source is described by a symmetric
  $M_{ij}$, whose scalar moment is the contraction
  $M_0 = \left(\tfrac{1}{2}M_{ij}M_{ij}\right)^{1/2}$. That is a frame-independent
  number extracted from a tensor by exactly the machinery of this lesson; its
  eigenvectors give the fault plane and slip direction.
- **The gravity gradient tensor.** $T_{ij} = \partial^2 V/\partial x_i\partial x_j$
  is symmetric and, in source-free regions, trace-free because $\nabla^2V = 0$
  ([01-06-08](../06-multivariable-calculus/08-potential-theory.md)). The trace
  being zero is the index statement $\delta_{ij}T_{ij} = 0$, and it is what makes
  a gravity gradiometer's five independent components enough.
- **Least-squares inversion.** The normal equations are
  $(A^{\mathsf T}A)_{ij}m_j = (A^{\mathsf T}d)_i$, i.e.
  $A_{ki}A_{kj}m_j = A_{ki}d_k$: the same contraction pattern, applied to a
  matrix that is far too large to write out.
- **Crystallography.** Elastic and piezoelectric constants are tabulated in
  Voigt notation but derived by the index symmetries of Section 3.6, which is the
  bridge to [01-15-05](./05-anisotropy-representation.md).

## 10. Further reading

- **Aki, K., & Richards, P. G. *Quantitative Seismology* (2nd ed.). University
  Science Books.** Chapters 2–3. Level: advanced. The standard reference for the
  index-notation forms of stress, strain and the elastodynamic equation used
  throughout seismology, with the moment-tensor contraction of Section 9.
- **Nye, J. F. *Physical Properties of Crystals: Their Representation by Tensors
  and Matrices*. Oxford University Press.** Chapters 1–3. Level: intermediate to
  advanced. The clearest treatment of why symmetric and antisymmetric parts
  behave differently in physical properties, and the origin of Voigt notation.
- **Aris, R. *Vectors, Tensors and the Basic Equations of Fluid Mechanics*.
  Dover.** Chapters 1–2. Level: intermediate. A short, precise account of the
  summation convention and the epsilon identities.
- **Jeffreys, H. *Cartesian Tensors*. Cambridge University Press.** Level:
  advanced. A classical, terse treatment of exactly the Cartesian case used here,
  including the pseudo-tensor discussion.
- **Itskov, M. *Tensor Algebra and Tensor Analysis for Engineers*. Springer.**
  Level: advanced. Uses the same index conventions as this lesson, with many
  worked derivations of the epsilon-delta identity.

> Note on citations: bibliographic details are given so you can locate these
> works. This repository does not host or reproduce copyrighted text; confirm
> current editions and availability through your library.

## 11. Related lessons

- [01-15-02 Tensor Algebra, Transformation Laws and Invariants](./02-tensor-algebra.md)
  — what makes a collection of components a tensor, and which combinations
  survive a change of frame.
- [01-15-03 Strain and Stress Tensors as Physical Tensors](./03-strain-and-stress-tensors.md)
  — the objects contracted in this lesson, with their physical invariants.
- [01-15-04 Differential Operators in Curvilinear Coordinates](./04-curvilinear-coordinates.md)
  — what has to be added when the basis vectors vary.
- [01-15-05 Representing Anisotropy: Voigt Notation and Symmetry Classes](./05-anisotropy-representation.md)
  — where the 81 components of $C$ become 21, then 5.
- [01-06-04 Divergence, Curl and Physical Meaning](../06-multivariable-calculus/04-divergence-and-curl.md)
  and [01-06-07 Vector Identities and Their Role in Geophysics](../06-multivariable-calculus/07-vector-identities.md)
  — the prerequisites that this lesson rewrites in a notation that scales.
- [02-04-05 Elastodynamic Equation of Motion and Wave Speeds](../../02-physics/04-elasticity-and-continuum-mechanics/05-elastodynamics.md)
  — where equation (8) becomes P and S waves.

## Self-assessment checklist

- [ ] I can state the two rules of the summation convention without looking them
      up. (Section 1)
- [ ] I can count the free indices in any expression and say what rank the object
      has. (Section 2.1)
- [ ] I can evaluate $\delta_{ij}a_j$, $\delta_{ii}$, $\delta_{ij}\delta_{jk}$
      and $A_{ii}$ correctly, and say which of them depends on dimension.
      (Sections 2.3, 3.1)
- [ ] I can write the determinant and the cross product with $\varepsilon$.
      (Sections 2.4, 3.3)
- [ ] I can prove the epsilon-delta identity by cases and use it to derive the
      two structural identities. (Sections 3.2, 3.4)
- [ ] I can convert between matrix and index form in both directions for
      products, traces, quadratic forms and symmetry splits. (Sections 2.2, 3.6)
- [ ] I can expand $\sigma_{ij} = C_{ijkl}e_{kl}$ for an isotropic medium into
      $\lambda e_{kk}\delta_{ij} + 2\mu e_{ij}$ and explain each step.
      (Section 3.5)
- [ ] I can explain why the antisymmetric part of $u_{k,l}$ cannot store energy.
      (Section 3.6)
- [ ] I know why a zero residual from $\nabla\times\nabla f$ on a symmetric
      stencil proves nothing. (Section 6)
- [ ] I can name the four situations in which index notation as taught here is
      not the right tool. (Section 5)
