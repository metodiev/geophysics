---
id: 01-07-02
title: "Matrices, Matrix Multiplication and Linear Maps"
level: intermediate
prereqs: ["01-07-01"]
estimated_minutes: 90
tags: [linear-algebra, matrices, linear-maps, forward-operator]
---

# Matrices, Matrix Multiplication and Linear Maps

## Learning objectives

By the end of this lesson you will be able to:

1. **Read** a matrix as a linear map rather than a table, and identify the model
   space and the data space of a given forward operator.
2. **Write** a forward model of a geophysical measurement as $d = Gm$, with the
   units of every entry stated.
3. **Multiply** matrices as compositions of maps, and explain why the order
   matters physically.
4. **Use** the transpose as the adjoint, and state why
   $\langle Ax, y \rangle = \langle x, A^\mathsf{T}y \rangle$ is the identity that
   makes gradient-based inversion possible.
5. **Recognise** structured matrices — diagonal, triangular, symmetric,
   orthogonal, permutation, banded, Toeplitz — and say what each structure buys.
6. **Verify** numerically that a matrix representing differentiation annihilates
   constants, and explain the consequence for any inversion of a gradient field.

## Prerequisites

[01-07-01 Vectors, Vector Spaces and Basis](./01-vectors-and-spaces.md) for
vectors, inner products, independence and basis. Nothing else is assumed, although
[01-06-01 Partial Derivatives, Gradients and Directional Derivatives](../06-multivariable-calculus/01-partial-derivatives.md)
explains the derivative that Section 3.4 discretises.

## 1. Intuition: a matrix is the physics, written out

An $m \times n$ matrix $G$ is a map that takes a model vector $m \in
\mathbb{R}^{n}$ to a data vector $d \in \mathbb{R}^{m}$:

$$d = Gm .$$

That is the entire content of most forward modelling. Concretely:

- **Vertical seismic profile.** $m$ = slowness in each of $n$ layers
  ($\mathrm{s/km}$), $G_{ij}$ = path length of ray $i$ in layer $j$ ($\mathrm{km}$),
  so $d$ = travel time ($\mathrm{s}$). Row $i$ is a ray; column $j$ is a layer.
- **Gravity survey over a gridded density model.** $m$ = density contrast in each
  cell, $G_{ij}$ = the vertical gravitational acceleration at station $i$ produced
  by unit density in cell $j$. Fully dense, possibly $10^{4} \times 10^{5}$.
- **Finite-difference differentiation.** $m$ = samples of a velocity profile,
  $G$ = a first-difference stencil, $d$ = approximate gradients. Square, banded,
  and — as Section 3.4 shows — singular.
- **Convolution.** $m$ = a seismic trace, $G$ = a Toeplitz matrix built from the
  filter, $d$ = the filtered trace.

The table of numbers is an artefact of having chosen a basis for the model space
and one for the data space. The *map* is the physics, and Section 3.4 makes the
distinction concrete: change the units of the model and the table changes, while
the map does not.

Two statements about $G$ carry the whole subject forward:

- **Its columns span the set of data that are achievable at all.** If your
  measurements lie outside that span, no model fits them; that is a failure of
  *existence*.
- **Its rows are the data kernels.** Row $i$ says, entry by entry, how much
  influence each model parameter has on datum $i$. If two rows are nearly equal,
  the two measurements carry nearly the same information.

Both become precise in [01-07-04](./04-rank-and-nullspace.md).

## 2. Precise definitions

### 2.1 The map, and what "linear" means

A map $L : V \to W$ between vector spaces is **linear** if
$L(x + y) = L(x) + L(y)$ and $L(\alpha x) = \alpha L(x)$ for all vectors and all
scalars. Equivalently $L(\alpha x + \beta y) = \alpha L(x) + \beta L(y)$.

Once bases are chosen, every linear map is a matrix and every matrix is a linear
map. Concretely, if $G$ has columns $g_1, \dots, g_n$ then

$$Gm = \sum_{j=1}^{n} m_j\, g_j ,$$

so the action of $G$ is *to combine its columns with the model coefficients as
weights*. This single identity explains both the column-space picture and the
superposition principle: the response of a linear system to a sum of sources is
the sum of the responses.

Linearity is an idealisation, and it is worth naming what it costs.
Travel time through a *heterogeneous* medium is not linear in slowness, but the
perturbation of travel time about a reference model is: this is the **Fréchet
derivative**, and it is what a linearised inversion actually inverts. The
linearisation is the subject of [01-07-10](./10-matrix-calculus.md), and its
validity limit is a physics question, not an algebra one.

### 2.2 Matrix multiplication is composition

If $A$ maps $V \to W$ and $B$ maps $U \to V$, then $AB$ maps $U \to W$ and

$$(AB)x = A(Bx) .$$

Element-wise, $(AB)_{ij} = \sum_k A_{ik}B_{kj}$. Three facts follow and all three
are used constantly:

- **Not commutative.** $AB \neq BA$ in general, because doing one thing and then
  another is not the same as the reverse order. Section 3.2 gives the numbers.
- **Associative.** $(AB)C = A(BC)$, so a chain of processing steps can be grouped
  however is cheapest.
- **The identity is neutral.** $IA = A = AI$, so "do nothing" is the identity map.

A useful mental model: the $j$-th column of $AB$ is $A$ applied to the $j$-th
column of $B$. Multiplying on the right by $B$ transforms each column of $A$; that
is the algebra of a change of basis (Section 3.3).

### 2.3 The transpose, and the adjoint identity

The **transpose** $A^\mathsf{T}$ has $(A^\mathsf{T})_{ij} = A_{ji}$. Its defining
property is the **adjoint identity**:

$$\langle Ax, y \rangle_{W} = \langle x, A^\mathsf{T}y \rangle_{V}
\quad\text{for all } x \in V,\ y \in W .$$

Read this as: instead of pushing a model through the map and then comparing, you
can pull the comparison back through the transpose and act on the data side. That
is a statement about dimension — $A^\mathsf{T}y$ lives in the model space, so one
inner product replaces $m$ inner products — and it is the reason a full gradient
of a misfit function costs two solves rather than $m$ solves
([01-07-10](./10-matrix-calculus.md) Section 5). In continuous problems the
transpose becomes the **adjoint operator**, and "is your adjoint right?" is the
first question a reviewer asks about a new inversion code.

### 2.4 Structure, and what it buys

| Structure | Definition | Consequence |
|---|---|---|
| Diagonal | $A_{ij} = 0$ for $i \neq j$ | acts independently on each component; $O(n)$ to invert |
| Triangular | zeros below (or above) the diagonal | solved by substitution in $O(n^{2})$ |
| Symmetric | $A = A^\mathsf{T}$ | real eigenvalues, orthogonal eigenvectors ([01-07-06](./06-eigenvalues.md)) |
| Orthogonal | $Q^\mathsf{T}Q = I$ | preserves norms and angles; $Q^{-1} = Q^\mathsf{T}$ |
| Permutation | one 1 per row and column | relabels; used for pivoting and reordering |
| Banded | $A_{ij} = 0$ for $|i - j| > b$ | elimination fills in only inside the band |
| Toeplitz | constant along each diagonal | is a convolution ([01-07-09](./09-sparse-matrices.md)) |
| Rank one | $A = uv^\mathsf{T}$ | one pattern in, one pattern out; the atom of the SVD |

The last row deserves emphasis. Because
$(uv^\mathsf{T})x = u\,(v^\mathsf{T}x)$, a rank-one matrix replaces the whole model
by a single number — the coefficient of $x$ along $v$ — and then emits a fixed
pattern $u$. The singular value decomposition writes any matrix as a sum of such
terms, ordered by importance. That is [01-07-08](./08-svd.md).

### 2.5 Induced norms

The **induced 2-norm** (spectral norm) of a matrix is

$$\|A\|_2 = \max_{x \neq 0} \frac{\|Ax\|}{\|x\|} ,$$

the largest stretching factor of the map. It equals $\sigma_{\max}(A)$, the largest
singular value, and it satisfies $\|AB\| \le \|A\|\|B\|$ (submultiplicative). The
Frobenius norm $\|A\|_F = \sqrt{\sum_{ij}A_{ij}^{2}}$ is easier to compute but is
*not* induced by a vector norm, and it does not satisfy $\|A\|_F \le \|A\|_2$ — the
reverse holds. Both are used in this module, and choosing the wrong one turns a
correct bound into a false one.

## 3. Step-by-step derivations

### 3.1 A forward model, written and checked

Consider eight gravity stations at elevations $z = 0, 200, \ldots, 1400$ m, with
the model "a residual level plus a linear trend":

$$d_i = m_1 + m_2 z_i , \qquad G = \begin{bmatrix} 1 & 0 \\ 1 & 200 \\ 1 & 400 \\
\vdots & \vdots \\ 1 & 1400\end{bmatrix} .$$

Columns: the first is the pattern "the same at every station" and the second is the
pattern "proportional to elevation". Every achievable dataset is a combination of
those two columns — a line in the 8-dimensional data space. Any measured set of
residuals that is *not* on that line cannot be fitted by this model, however you
choose $(m_1, m_2)$. That is the column-space picture, and it is the reason an
inverse problem can fail before any arithmetic happens.

The 4-station version of this matrix appears in
[`code/matrices_and_maps_demo.py`](./code/matrices_and_maps_demo.py) Section 4,
with $z = 0, 1, 2, 3$ and $m = (0.5, -3.0)$, giving
$d = (0.5, -2.5, -5.5, -8.5)$: the first column of $G$ contributes the constant
$0.5$ to every station and the second contributes $-3.0$ times the station index.
Reading the units off the model — mGal for the level and mGal per unit distance
for the trend — is part of writing the model correctly.

### 3.2 Composition and non-commutativity, in numbers

Take a rotation by $30^{\circ}$,

$$R = \begin{bmatrix} 0.866025 & -0.500000 \\ 0.500000 & 0.866025 \end{bmatrix},
\qquad S = \begin{bmatrix} 1 & 0 \\ 0 & 2 \end{bmatrix},$$

and the model vector $x = (3, 1)$. Then

$$RS = \begin{bmatrix} 0.8660 & -1.0000 \\ 0.5000 & 1.7321 \end{bmatrix}, \qquad
SR = \begin{bmatrix} 0.8660 & -0.5000 \\ 1.0000 & 1.7321 \end{bmatrix},$$

with $\max|RS - SR| = 0.500000$. Applied to $x$ the two products give $(1.598076,
3.232051)$ and $(2.098076, 4.732051)$: different answers from the same two
operations in the other order. Physically: "rotate the survey into the anisotropy
frame, then apply the directional gain" is not "apply the directional gain, then
rotate". Non-commutativity is not an algebraic curiosity; it is the statement that
processing steps do not commute unless they act on independent degrees of freedom.

Note also the two invariants visible in the same output. $R$ leaves the length
unchanged — $\|x\| = \|Rx\| = 3.162278$ — while $S$ does not ($\|Sx\| = 3.605551$).
And the area scale factors, computed from the images of the unit square, are
$1.000000$ for $R$ and $2.000000$ for $S$, equal to the determinants. The
determinant is the volume scale of the map; its vanishing is the failure of the map
to be invertible. That is [01-07-05](./05-determinants-inverses.md).

### 3.3 Change of basis as a pair of matrices

Let $P$ have the new basis vectors as its columns. Then $Pc$ expresses the
coordinate vector $c$ in the old coordinates, and $P^{-1}$ performs the inverse
translation. For a map $A$ in old coordinates, its matrix in the new basis is

$$A' = P^{-1}AP .$$

$A$ and $A'$ are **similar**, they have the same eigenvalues and the same
determinant, and they are the same map. Choosing $P$ to make $A'$ as simple as
possible is diagonalisation, and it succeeds exactly when $P$ can be built from
eigenvectors — [01-07-06](./06-eigenvalues.md). If $P$ is orthogonal (an
orthonormal change of coordinates), then $P^{-1} = P^\mathsf{T}$ and no inversion
is needed.

### 3.4 A derivative operator is a matrix — and it is singular

Sample $v(z) = 1600 + 0.6z + 0.02z^{2} + 0.001z^{3}$ m/s at $z = 0, 1, \ldots, 6$
km and approximate the gradient by central differences in the interior, with
one-sided differences at the two ends. The operator is a $7 \times 7$ matrix whose
rows are stencils of $\pm 1/(2h)$ and $\pm 1/h$.

| $z$ (km) | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| $v$ (m/s) | 1600.000 | 1600.621 | 1601.288 | 1602.007 | 1602.784 | 1603.625 | 1604.536 |
| $Dv$ ($\mathrm{s^{-1}}$) | 0.6210 | 0.6440 | 0.6930 | 0.7480 | 0.8090 | 0.8760 | 0.9110 |
| exact $\mathrm{d}v/\mathrm{d}z$ | 0.6000 | 0.6430 | 0.6920 | 0.7470 | 0.8080 | 0.8750 | 0.9480 |
| error | 0.0210 | 0.0010 | 0.0010 | 0.0010 | 0.0010 | 0.0010 | $-0.0370$ |

Two error structures are visible at once. The interior error is exactly
$+0.0010$ everywhere, because the central-difference truncation term is
$h^{2}v'''/6 = 1^{2}\cdot 0.006/6 = 0.001$ and $v'''$ is constant for a cubic. The
two boundary errors are $O(h)$ with opposite signs, because one-sided differences
are only first-order accurate. **Boundary rows usually govern the global accuracy
of a discretisation**, which is why stencil design is about the edges.

Now the structural fact. Substituting the constant vector $\mathbf{1}$:

$$D\mathbf{1} = \mathbf{0} \quad\text{exactly},$$

and the computed rank of $D$ is $6$ out of $7$. The null space is the set of
constant profiles. A constant added to the whole velocity profile changes no
gradient at all, so no algorithm can recover the absolute level from gradient
data. This is the simplest possible non-uniqueness, and it is the mechanism of
[01-07-04](./04-rank-and-nullspace.md) in miniature. Every field that is inverted
from derivatives — strain rate from GPS, velocity from a travel-time gradient,
geothermal gradient from borehole temperatures — inherits exactly this null space
and must supply the constant from a different measurement.

Finally the second-order claim, verified by refining $h$ at $z = 3$:

| $h$ (km) | central estimate | exact | error | ratio |
|---|---|---|---|---|
| 1.00 | 0.74800000 | 0.74700000 | $1.000\times10^{-3}$ | — |
| 0.50 | 0.74725000 | 0.74700000 | $2.500\times10^{-4}$ | 4.0 |
| 0.25 | 0.74706250 | 0.74700000 | $6.250\times10^{-5}$ | 4.0 |

Halving $h$ quarters the error: $O(h^{2})$, as the Taylor expansion of Section 3 of
[01-05-04](../05-single-variable-calculus/04-taylor-series.md) requires.

### 3.5 Convolution is a matrix product

Take the trace $(1, 2, 4, 3, 1.5)$ and the three-tap smoother
$(\tfrac14, \tfrac12, \tfrac14)$. Building each row of a $5\times5$ matrix from a
shifted copy of the filter gives

$$C = \begin{bmatrix} 0.5 & 0.25 & 0 & 0 & 0 \\ 0.25 & 0.5 & 0.25 & 0 & 0 \\
0 & 0.25 & 0.5 & 0.25 & 0 \\ 0 & 0 & 0.25 & 0.5 & 0.25 \\
0 & 0 & 0 & 0.25 & 0.5 \end{bmatrix},$$

with $C$ applied to the trace giving $(1.0, 2.25, 3.25, 2.875, 1.5)$, identical to
the direct running sum, and $13$ of $25$ entries nonzero. Three readings of the same
arithmetic: a filter, a convolution, a matrix. Only $13$ entries matter, and
recognising the Toeplitz structure is what makes the operation
$O(n \log n)$ by FFT instead of $O(n^{2})$ by matrix product — the subject of
[01-10 Fourier Analysis and Spectral Methods](../10-fourier-analysis/README.md) and
[20-signal-processing](../../20-signal-processing/README.md).

A warning attached to this example: the boundary treatment (zero padding) is part
of the model, not a detail. A different boundary choice gives a different matrix and
a different filtered trace near the ends.

### 3.6 Two nonzero maps that annihilate everything

With

$$A = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}, \qquad
B = \begin{bmatrix} 0 & 0 \\ 0 & 1 \end{bmatrix},$$

the product $AB$ is the zero matrix, verified exactly. $A$ keeps only the
first component; $B$ keeps only the second; the composition keeps nothing. The
consequence is a rule of working practice: **matrix algebra cannot be done entry by
entry.** Facts about products come from structure and factorisation, never from
manipulating individual numbers — which is why the rest of this module is about
factorisations, ranks and spectra rather than about indices.

## 4. Physical interpretation

**A row is a measurement, a column is a parameter, and the entries are physical
influences with units.** Writing down $G$ without units is a common source of
silent error: a cell path length in km multiplied by a slowness in
$\mathrm{s/m}$ yields a travel time 1000 times too small. The units of $G_{ij}$
are always (units of $d_i$) / (units of $m_j$).

**The transpose is the sensitivity map backwards.** $G^\mathsf{T}d$ has the
dimensions of a model-space quantity and is the object an inversion updates; that
is why $G^\mathsf{T}$ appears in every gradient formula, and why the adjoint
identity of Section 2.3 is the load-bearing algebraic fact for practical
inversion.

**Structure is physics.** Banded means a local stencil, so information travels one
grid cell at a time and the system is amenable to relaxation. Toeplitz means
translation invariance, so an FFT applies. Symmetric means the underlying operator
is self-adjoint, so the eigenvalues are real and the eigenvectors orthogonal —
which holds for elastic stiffness, moment of inertia and every $G^\mathsf{T}G$.
Recognising the structure before writing code determines the entire algorithm.

**Composition is a processing sequence.** Migration followed by filtering is not
filtering followed by migration. Non-commutativity is the formal statement of that
commonplace, and it is why the order of operations in a processing flow is a
documented decision rather than an implementation detail.

## 5. Python demonstration

The companion script is
[`code/matrices_and_maps_demo.py`](./code/matrices_and_maps_demo.py), with six
sections: rotation and stretch as maps, composition and non-commutativity, the
finite-difference operator, a design matrix, convolution as a matrix, and two
nonzero matrices whose product is zero.

The quantified outputs:

| Section | Observed | Interpretation |
|---|---|---|
| 1, rotation | $\|x\| = 3.162278$, $\|Rx\| = 3.162278$, $\|Sx\| = 3.605551$ | orthogonal maps preserve length; general maps do not |
| 1, area | image areas $1.000000$ and $2.000000$ | the determinant is the area/volume scale factor |
| 2, order | $\max\|RS - SR\| = 0.500000$ | two processing orders, two different results |
| 3, rank | $\operatorname{rank}(D) = 6$ of $7$ | the derivative operator has a one-dimensional null space |
| 3, null vector | $D\mathbf{1} = \mathbf{0}$ exactly | absolute level is invisible to a gradient |
| 3, order of accuracy | central-difference errors $1.0\times10^{-3}$, $2.5\times10^{-4}$, $6.25\times10^{-5}$ | quartering per halving: $O(h^{2})$ |
| 4, design matrix | $m = (0.5, -3.0) \mapsto d = (0.5, -2.5, -5.5, -8.5)$ | the map in action, with units |
| 5, convolution | matrix product equals direct convolution exactly | 13 of 25 entries nonzero |
| 6, annihilation | $AB = 0$ with $A \neq 0$, $B \neq 0$ | algebra needs structure, not index manipulation |

> **Breaking exercise.** In Section 3 the interior rows use central differences.
> Replace the *first* row only with a second-order one-sided stencil
> $(-3v_0 + 4v_1 - v_2)/(2h)$ and predict the change in the boundary error before
> running the script. Then check whether the rank of $D$ changes. It must not: any
> difference stencil annihilates constants, so every such matrix is singular, and
> that conclusion is structural rather than numerical.

## 6. Exercises

Full set and worked solutions:
[`exercises/02-matrices-and-operations-exercises.md`](./exercises/02-matrices-and-operations-exercises.md)
and
[`exercises/02-matrices-and-operations-solutions.md`](./exercises/02-matrices-and-operations-solutions.md).
Four to start with:

**★1.** Compute $AB$ and $BA$ for
$A = \begin{bmatrix} 2 & 1 \\ 0 & 3\end{bmatrix}$,
$B = \begin{bmatrix} 1 & -1 \\ 4 & 2\end{bmatrix}$, and confirm that they differ.
Give a $2\times2$ example in which they are equal.

**★2.** A two-layer refraction experiment gives two equations,
$t_1 = 0.4\,s_1 + 0.6\,s_2$ and $t_2 = 0.5\,s_1 + 0.5\,s_2$, with $s$ in
$\mathrm{s/km}$ and $t$ in $\mathrm{s}$. Write $G$, state the units of every
entry, and say which of the two rays has more influence on the second layer.

**★★3.** Build the $5\times5$ central-difference matrix for a uniform grid with
spacing $h$ on the interval $[0,4h]$ (one-sided at the ends as usual). (a) Verify
that it annihilates constants. (b) Compute its rank. (c) Show by explicit
computation that the vector $(0, 1, 2, 3, 4)$ and the vector $(5, 6, 7, 8, 9)$
produce identical images and explain the result without appeal to the null space
calculation.

**★★4.** Write the matrix that performs a rotation by $\theta$ in the plane, and
verify symbolically that $R(\theta)R(\phi) = R(\theta + \phi)$ and that
$R(\theta)^{-1} = R(-\theta) = R(\theta)^\mathsf{T}$. Give the value of
$\det R(\theta)$ and explain why orthogonality forces that value.

**★★★5.** For a reflection survey, the travel time as a function of offset is
$T(x) = \sqrt{x^{2} + 4h^{2}}/v$. (a) Write the $6 \times 2$ Jacobian $J$ at
offsets $x = 0, 0.5, \ldots, 3$ km for $(h, v) = (1.2, 3.7)$. (b) Verify that the
linear map $J$ applied to a small change in $(h, v)$ reproduces the true change in
travel time to second order in the perturbation. (c) Compute the determinant of
$J^\mathsf{T}J$ and say what it means about the ability of these six offsets to
determine $h$ and $v$ separately.

**★★★6.** The smoothing matrix $C$ of Section 3.5 is symmetric and Toeplitz.
(a) Verify $\|C\|_2 \le 1$ from the row sums, and say which row achieves the
bound. (b) Compute $\det C$ for the $5\times5$ case and explain why the value is
small but nonzero. (c) Apply $C$ one hundred times to the trace and describe the
result; quantify how many of the original trace's degrees of freedom survive.
(d) Explain the connection with the null space of the derivative operator in
Section 3.4.

## 7. Common mistakes

1. **Treating $G$ as a table of numbers.** Every property that matters — rank,
   null space, conditioning — is a property of the map, and the table depends on
   the basis.
2. **Dropping the units of the entries.** $G_{ij}$ has units of $d_i$ per $m_j$.
   Confusing km with m changes the answer by $10^{3}$ and is invisible in the
   arithmetic.
3. **Assuming $AB = BA$.** It fails for the simplest physical pair, a rotation and
   a stretch, with an error of $0.5$ in the entries (Section 3.2).
4. **Confusing the transpose with the inverse.** $Q^\mathsf{T} = Q^{-1}$ only for
   orthogonal $Q$. For a general matrix the transpose is an adjoint, a different
   map between different spaces.
5. **Using the Frobenius norm where the spectral norm is meant.** They are not
   comparable in the direction usually assumed, and inequalities stated with the
   wrong one are simply false.
6. **Assuming a square system is solvable.** The differentiation matrix of
   Section 3.4 is square, nonsingular-looking and singular. Square says nothing.
7. **Ignoring where the boundary rows came from.** A stencil choice at the edges
   sets the global accuracy of a discretisation; the interior error can be
   $O(h^{2})$ while the boundary error is $O(h)$ (Section 3.4).
8. **Forgetting that linearity is an approximation for real data.** Inverting a
   perturbed travel time is legitimate; inverting a travel time far from the
   reference model is not, whatever the matrix says.

## 8. Real-world applications

- **Forward modelling in every method.** Gravity, magnetics, DC resistivity, EM and
  seismic reflection all produce a $G$ whose columns are the responses to unit
  sources and whose rows are the sensitivity kernels of individual measurements.
- **Finite-difference and finite-element operators.** The stiffness and mass
  matrices of a discretised PDE are structured matrices — banded, block-tridiagonal,
  sparse — and their structure is what makes the simulation feasible
  ([01-07-09](./09-sparse-matrices.md), [19-numerical-modeling-hpc](../../19-numerical-modeling-hpc/README.md)).
- **Filtering and deconvolution.** A convolutional model is a Toeplitz matrix; a
  deconvolution is an attempt to invert one, and it inherits the conditioning of
  the filter's spectrum.
- **Adjoint migration.** The adjoint of the modelling operator is exactly the
  migration operator; the adjoint identity of Section 2.3 is why one code can serve
  both directions. See [06-seismology](../../06-seismology/README.md).
- **Polarisation and rotation of data.** Rotating a three-component recording into
  a ray frame is multiplication by an orthogonal matrix.
- **Error propagation through a chain of maps.** Doing several processing steps in
  the wrong order is a composition in the wrong order, and the resulting data are
  not wrong by a rounding error but by a map.

## 9. Further reading

- **Strang, G. *Introduction to Linear Algebra.* Wellesley–Cambridge Press.** The
  four ways to view matrix multiplication, with the column-space picture front and
  centre. Level: beginner to intermediate.
- **Trefethen, L. N., & Bau, D. *Numerical Linear Algebra.* SIAM.** Chapter 2 for
  the operator viewpoint, and for why structure is the whole story in numerical
  work. Level: intermediate to advanced.
- **Golub, G. H., & Van Loan, C. F. *Matrix Computations.* Johns Hopkins
  University Press.** The catalogue of matrix structures and the algorithms
  adapted to each. Level: advanced.
- **Menke, W. *Geophysical Data Analysis: Discrete Inverse Theory.* Academic
  Press.** $G$, $d$ and $m$ with units, in the notation used throughout this
  module. Level: intermediate.
- **Shewchuk, J. R. *An Introduction to the Conjugate Gradient Method Without the
  Agonizing Pain*.** Available from the author's academic page. The clearest
  treatment anywhere of why the adjoint identity matters in practice. Level:
  intermediate.
- **Telford, W. M., Geldart, L. P., & Sheriff, R. E. (1990). *Applied Geophysics*
  (2nd ed.). Cambridge University Press.** The source of the forward models used
  as examples here, in survey units. Level: intermediate.

> Note on citations: bibliographic details above are given so that you can
> locate the works. This repository does not host or reproduce copyrighted text,
> and you should confirm editions and current availability through your library
> before citing them yourself.

## 10. Self-assessment checklist

- [ ] I can write a geophysical forward model as $d = Gm$ and state the units of
      every entry.
- [ ] I can explain the column-space and row-space readings of the same matrix in
      words.
- [ ] I can compute $AB$ and $BA$ and give a physical reason why they differ.
- [ ] I can state and use the adjoint identity $\langle Ax, y\rangle = \langle x,
      A^\mathsf{T}y\rangle$.
- [ ] I can name four matrix structures and the algorithmic consequence of each.
- [ ] I can show that a difference operator annihilates constants, and explain why
      that makes every gradient-inversion ill-posed without extra information.
- [ ] I can estimate the truncation error of a finite-difference stencil and
      explain why the boundary rows dominate.
- [ ] I can write a convolution as a Toeplitz matrix multiplication and count its
      nonzeros.

## 11. Related lessons

- [01-07-01 Vectors, Vector Spaces and Basis](./01-vectors-and-spaces.md) — the
  spaces this lesson maps between.
- [01-07-03 Linear Systems, Gaussian Elimination and LU Factorisation](./03-systems-and-elimination.md) —
  inverting the map when it can be inverted.
- [01-07-04 Rank, Null Space and Solvability](./04-rank-and-nullspace.md) — what
  the columns span, and what the map destroys.
- [01-07-05 Determinants, Inverses and Matrix Conditioning](./05-determinants-inverses.md) —
  the volume scale factor and its numerical meaning.
- [01-07-06 Eigenvalues, Eigenvectors and Diagonalisation](./06-eigenvalues.md) —
  the structure that makes a map act like a diagonal matrix.
- [01-07-08 Singular Value Decomposition and Rank Truncation](./08-svd.md) — every
  matrix as a sum of rank-one maps.
- [01-07-09 Sparse Matrices and Structured Systems](./09-sparse-matrices.md) —
  taking structure seriously at scale.
- [01-07-10 Matrix Calculus and Sensitivity Derivatives](./10-matrix-calculus.md) —
  differentiating the map to obtain sensitivities and adjoints.
- [01-06-01 Partial Derivatives, Gradients and Directional Derivatives](../06-multivariable-calculus/01-partial-derivatives.md) —
  the continuous operator that this lesson discretises.
- [01-10 Fourier Analysis and Spectral Methods](../10-fourier-analysis/README.md) —
  where a Toeplitz matrix becomes a multiplication.
