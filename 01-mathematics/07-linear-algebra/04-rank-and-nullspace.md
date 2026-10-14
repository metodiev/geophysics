---
id: 01-07-04
title: "Rank, Null Space and Solvability (Existence and Uniqueness)"
level: advanced
prereqs: ["01-07-03"]
estimated_minutes: 90
tags: [linear-algebra, rank, null-space, non-uniqueness]
---

# Rank, Null Space and Solvability (Existence and Uniqueness)

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** the rank of a matrix by row reduction, and use the rank–nullity
   theorem to obtain the dimensions of all four fundamental subspaces.
2. **Decide** whether a linear system is consistent by comparing
   $\operatorname{rank}([G \mid d])$ with $\operatorname{rank}(G)$, and interpret
   an inconsistency as a statement about the data rather than a numerical failure.
3. **Construct** a basis of the null space, and translate a null-space vector into
   a statement about which model perturbation the experiment cannot detect.
4. **Explain** why the null space is the mathematical statement of non-uniqueness,
   and why every member of a family of models fitting the data equally well is
   equally admissible without extra information.
5. **Find** the minimum-norm member of that family, and state what the norm
   asserts physically.
6. **Build** the resolution matrix $R$ and read from it which model combinations
   the data constrain.

## Prerequisites

[01-07-03 Linear Systems, Gaussian Elimination and LU Factorisation](./03-systems-and-elimination.md)
for elimination and the pivots, and
[01-07-01 Vectors, Vector Spaces and Basis](./01-vectors-and-spaces.md) for
independence, span and basis. The rank–nullity theorem is the payoff of the
independence discussion in [01-07-01](./01-vectors-and-spaces.md) Section 2.3.

## 1. Intuition: the mathematics of "the survey cannot see it"

Suppose a survey is designed so that ray 3 traverses exactly the same combination
of cells as rays 1 and 2 together. In path lengths:

$$G = \begin{bmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 1 & 2 & 1 \end{bmatrix}
\ \text{km},$$

and the third row is literally the sum of the first two. Then a model perturbation
that raises cell 1, lowers cell 2 and raises cell 3 all by the same amount,
$m = (1, -1, 1)$ scaled, produces **exactly zero** travel-time change in all three
rays:

$$G \begin{bmatrix} 1 \\ -1 \\ 1 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix}.$$

That vector is a **null-space vector**, and it is the single most useful object in
this lesson. It is not an artefact of arithmetic and not a limitation of your
solver. It is a statement about the experiment: *this* perturbation of the Earth
leaves *this* dataset unchanged, so no processing, no weighting and no amount of
careful arithmetic will recover it. A whole one-parameter family of models fits the
data equally well.

Non-uniqueness in geophysics is usually presented as a philosophical point about
ambiguity. It is not philosophical; it is a rank calculation, and it is done before
you look at the data. Two questions are being asked, and they are different:

- **Existence:** is $d$ in the column space of $G$? If not, no model fits the data
  and the residual is irreducible.
- **Uniqueness:** is the null space of $G$ trivial? If not, infinitely many models
  fit the data exactly.

Both failures are normal in practice, both can be diagnosed, and both have standard
responses: for existence, least squares ([01-07-07](./07-orthogonality.md)); for
uniqueness, a constraint such as minimum norm, smoothness or a prior
([18-inverse-problems](../../18-inverse-problems/README.md)).

## 2. Precise definitions

### 2.1 Rank

The **rank** of $G$ is the dimension of its column space, which equals the
dimension of its row space and equals the number of nonzero pivots in any row
reduction. If $G$ is $m \times n$ then

$$\operatorname{rank}(G) \le \min(m, n),$$

with equality called full rank. Row operations do not change the row space and
never change the rank.

### 2.2 The four fundamental subspaces

| Subspace | Symbol | Lives in | Dimension |
|---|---|---|---|
| Column space (range) | $\mathcal{C}(G)$ | $\mathbb{R}^{m}$ | $r$ |
| Left null space | $\mathcal{N}(G^\mathsf{T})$ | $\mathbb{R}^{m}$ | $m - r$ |
| Row space | $\mathcal{C}(G^\mathsf{T})$ | $\mathbb{R}^{n}$ | $r$ |
| Null space | $\mathcal{N}(G)$ | $\mathbb{R}^{n}$ | $n - r$ |

The **rank–nullity theorem** is the two dimension statements in the last column:

$$r + \dim\mathcal{N}(G) = n, \qquad r + \dim\mathcal{N}(G^\mathsf{T}) = m .$$

The *orthogonality relations* are what make the picture usable: the row space and
the null space are orthogonal complements in the model space, and the column space
and the left null space are orthogonal complements in the data space. A
null-space vector is perpendicular to every row of $G$ — which is precisely why it
contributes nothing to any datum, since each datum is the inner product of a row
with the model.

Geophysical readings:

- $\mathcal{C}(G)$: the set of datasets your model class can produce. Anything
  outside is noise, theory error, or a model deficiency.
- $\mathcal{N}(G)$: the model perturbations your survey is blind to. This is
  non-uniqueness.
- $\mathcal{C}(G^\mathsf{T})$: the model combinations your data *do* constrain.
- $\mathcal{N}(G^\mathsf{T})$: data combinations that must be zero. A left null
  vector is a consistency condition — with clean data it holds exactly, and with
  noisy data it is a check on the noise level.

### 2.3 Consistency, and the test for it

The system $Gm = d$ has a solution **if and only if**

$$\operatorname{rank}([G \mid d]) = \operatorname{rank}(G),$$

because adjoining a column increases the rank exactly when $d$ has a component
outside the column space. When the ranks agree, the solutions form the affine
space

$$m = m_p + \mathcal{N}(G) = \{\, m_p + \alpha_1 n_1 + \cdots + \alpha_k n_k \,\},$$

with $k = n - r$. When they differ, the *augmented* system is inconsistent and the
least-squares solution of [01-07-07](./07-orthogonality.md) is the only useful
answer.

### 2.4 Reduced row echelon form, and the computation of rank

A **leading entry** is the first nonzero entry of a row. A matrix is in **reduced
row echelon form (RREF)** if every leading entry is 1, is the only nonzero entry in
its column, and appears to the right of the leading entry of the row above. The
columns containing leading entries are the **pivot columns**; their number is the
rank; the remaining columns are **free**.

The null space is read directly from the RREF. For each free column $f$, set
$x_f = 1$ and the other free variables to zero, and solve for the pivot variables
from the rows:

$$x_{\text{pivot}(i)} = -\text{(RREF)}_{i f} .$$

That is the algorithm used by every script in this module.

### 2.5 The resolution matrix

Define $R$ as the orthogonal projector onto the row space. For full column rank it
is the identity; in general it is the **model resolution matrix**

$$R = V_r V_r^\mathsf{T},$$

where $V_r$ is an orthonormal basis of the row space (equivalently, the first $r$
right singular vectors of $G$; [01-07-08](./08-svd.md) establishes the
equivalence). Its properties:

- symmetric and idempotent: $R^2 = R = R^\mathsf{T}$;
- $\operatorname{tr}R = r$;
- $R$ annihilates the null space and fixes the row space;
- so the recovered "model" is always $Rm$, and the error is
  $(I - R)m$: the null-space component of the true model.

The diagonal entries $R_{ii}$ are called **resolution** at parameter $i$: a value
of 1 means parameter $i$ is recovered exactly by the projection; a value below 1
means the estimate of that parameter is a weighted average of several true
parameters. This is the standard diagnostic of the tomographic literature.

## 3. Step-by-step derivations

### 3.1 Rank and null space of the redundant-ray kernel

Reduce the augmented matrix of $G$ with the lesson's kernel:

$$\begin{bmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 1 & 2 & 1 \end{bmatrix}
\;\longrightarrow\;
\begin{bmatrix} 1 & 0 & -1 \\ 0 & 1 & 1 \\ 0 & 0 & 0 \end{bmatrix}$$

after eliminating the third row with row 3 − row 1 − row 2 $= \mathbf{0}$. The
pivot columns are 1 and 2, so $r = 2$ and the free column is 3. Setting $x_3 = 1$
gives $x_1 = 1$, $x_2 = -1$, so

$$\mathcal{N}(G) = \operatorname{span}\{(1, -1, 1)^\mathsf{T}\}, \qquad
\|n\| = \sqrt{3}, \qquad \hat{n} = (0.577350,\ -0.577350,\ 0.577350)^\mathsf{T},$$

and $G\hat n = (0,0,0)$ to round-off, as the demonstration verifies. Rank–nullity:
$r + \dim\mathcal{N}(G) = 2 + 1 = 3 = n$, and
$r + \dim\mathcal{N}(G^\mathsf{T}) = 2 + 1 = 3 = m$.

### 3.2 A one-parameter family of models fits the data exactly

Take $d = (1, 0, 1)^\mathsf{T}$ s, which satisfies the consistency condition
$d_3 = d_1 + d_2$ implied by the row relationship, hence is in the column space. A
particular solution is $m_p = (1,0,0)$: rays 1 and 3 see cell 1, and ray 2 sees
nothing. Adding any multiple of $\hat n$ changes the model and changes no datum:

| $\alpha$ | $m_1$ | $m_2$ | $m_3$ | $\|Gm - d\|$ | $\|m\|$ |
|---|---|---|---|---|---|
| $-2.0$ | $-0.154701$ | $1.154701$ | $-1.154701$ | $0$ | $1.640305$ |
| $-1.0$ | $0.422650$ | $0.577350$ | $-0.577350$ | $0$ | $0.919402$ |
| $-0.5$ | $0.711325$ | $0.288675$ | $-0.288675$ | $0$ | $0.820152$ |
| $0.0$ | $1.000000$ | $0.000000$ | $0.000000$ | $0$ | $1.000000$ |
| $0.5$ | $1.288675$ | $-0.288675$ | $0.288675$ | $0$ | $1.351795$ |
| $1.0$ | $1.577350$ | $-0.577350$ | $0.577350$ | $1.1\times10^{-16}$ | $1.776148$ |
| $2.0$ | $2.154701$ | $-1.154701$ | $1.154701$ | $2.2\times10^{-16}$ | $2.703590$ |

Every row fits the data to round-off, and the models differ by up to $2.3$
$\mathrm{s/km}$ in individual cells — comparable to the model values themselves.
No amount of numerical care will select among them, because the data contain no
information that distinguishes them.

### 3.3 Minimum norm: the extra ingredient

The family has a unique member of smallest norm. Minimise
$\|m_p + \alpha\hat n\|^{2}$ over $\alpha$:

$$\frac{d}{d\alpha}\left[\|m_p\|^{2} + 2\alpha\langle m_p, \hat n\rangle +
\alpha^{2}\right] = 0
\;\Longrightarrow\;
\alpha^{*} = -\langle m_p, \hat n \rangle = -0.577350 ,$$

giving $m^{*} = (0.666667,\ 0.333333,\ -0.333333)$ $\mathrm{s/km}$ with
$\|m^{*}\| = 0.816497$, against $\|m_p\| = 1$ and the $\alpha = 2$ member's
$2.703590$. The demonstration verifies that $Rm^{*} = m^{*}$, and that
$Gm^{*} = d$.

That is the entire content of "adding a constraint resolves the non-uniqueness".
The constraint used here is minimum Euclidean norm, which says: *of all models
consistent with the data, prefer the one that perturbs the Earth least, measuring
perturbation as the root-sum-square of cell slownesses in $\mathrm{s/km}$*. That
is a physical assertion about the geology, not a mathematical necessity, and
choosing a different norm — or smoothness rather than smallness — selects a
different model from the same family. Whoever chooses the constraint chooses the
answer, which is why [18-inverse-problems](../../18-inverse-problems/README.md)
devotes so much space to it.

### 3.4 Inconsistency, and its diagnosis

Now test three data vectors against the same $G$:

| $d$ | $\operatorname{rank}([G \mid d])$ | $\operatorname{rank}(G)$ | consistent? |
|---|---|---|---|
| $(1, 0, 0)$ | 3 | 2 | no |
| $(1, 0, 1)$ | 2 | 2 | yes |
| $(0, 1, 1)$ | 2 | 2 | yes |

The first fails because $d_3 \neq d_1 + d_2$: the redundancy in the geometry means
the data must themselves satisfy $d_3 = d_1 + d_2$, and this vector does not. With
real, noisy data that condition never holds exactly, so **exact consistency is not
the practical question**; the practical question is how large the residual is
relative to the noise, which is [01-07-07](./07-orthogonality.md)'s business.

### 3.5 The resolution matrix, computed

Projecting onto the row space — spanned here by $(1,1,0)$ and $(0,1,1)$ — gives

$$R = \frac{1}{3}\begin{bmatrix} 2 & 1 & -1 \\ 1 & 2 & 1 \\ -1 & 1 & 2 \end{bmatrix},
\qquad \operatorname{tr}R = 2 = r,$$

with $\max|R^{2} - R| = 2.22\times10^{-16}$ and $\max|R^\mathsf{T} - R| = 0$
(symmetric, idempotent — a projection, verified numerically). Its action:

| $m$ | $Rm$ | $\|m - Rm\|$ |
|---|---|---|
| $(1, 2, 3)$ | $(0.333333,\ 2.666667,\ 2.333333)$ | $1.154701$ |
| $(1, 0, 0)$ | $(0.666667,\ 0.333333,\ -0.333333)$ | $0.577350$ |
| $m^{*}$ | $(0.666667,\ 0.333333,\ -0.333333)$ | $0$ |

Three readings of the same table. First, $R$ strips out the $(1,-1,1)$ component
from any model: the difference $m - Rm$ is always parallel to $\hat n$ — check
$1.154701 = 2/\sqrt3$ for the first row, which is $|\langle m, \hat n\rangle|$ with
$\langle m, \hat n \rangle = (1 - 2 + 3)/\sqrt3 = 2/\sqrt3$. Second,
$\operatorname{diag}R = (2/3, 2/3, 2/3)$: **no single cell is perfectly resolved**,
each recovered value being a mixture of true values. Third, the minimum-norm
solution is fixed by $R$, because it lies in the row space.

Note carefully what $R = I$ would and would not mean. If $G$ has full column rank,
then $\mathcal{N}(G) = \{0\}$ and $R = I$: every model direction is formally
resolved. That is a statement about exact data. It does **not** say the model is
well determined in the presence of noise — a near-null direction with a tiny
singular value still gives a huge error for a small data error, and the correct
diagnostic there is the covariance, not $R$. [01-07-08](./08-svd.md) Section 4 is
built entirely on this distinction.

### 3.6 The same phenomenon in the simplest operator

The five-point first-difference matrix on a uniform grid of five samples has rank 4
and null space spanned by $(1,1,1,1,1)$: the constant vector. Two velocity profiles
differing by a constant have identical gradients. This is the $n = 5$ instance of
the $n = 7$ calculation in
[01-07-02](./02-matrices-and-operations.md) Section 3.4, and it is the null space
that any inversion of a derivative field must supply externally — from a
reflection, a geoid constraint, or an independent absolute measurement.

## 4. Physical interpretation

**A null space is a statement about the survey, not about the data.** It is
determined by the geometry — which rays traverse which cells, at what angles, with
what path lengths — and it does not change when you collect more data along the
same geometry. Repeating a measurement reduces noise; it does not reduce the null
space. Only new geometries (a different offset range, a different azimuth) change
the rank.

**Left null vectors are consistency relations, and therefore noise tests.** With
one redundant ray, the relation $d_3 = d_1 + d_2$ holds exactly for noise-free
data. With real data the deviation from that relation measures an independent
component of the noise, and it can be used as an estimate of the noise level
without any replica measurements. This is the standard use of cross-checks in
survey design.

**Resolution is a blurring operator.** $Rm$ being a weighted average of true
parameters is why tomographic images look smooth even when the true structure is
sharp: the inversion cannot do better than the projection, and the projection
mixes neighbouring cells. The pattern of the mixing is the resolution matrix, and
publishing it is standard practice — an image without its resolution matrix is an
incomplete result.

**Non-uniqueness has a size, and that size is measurable.** The family of Section
3.2 spans $2.3$ $\mathrm{s/km}$ in individual cells. A useful inversion results
section states the null-space direction *and* the range of model values it
supports; that is the honest form of "the model is non-unique here".

## 5. Python demonstration

The companion script is
[`code/rank_and_nullspace_demo.py`](./code/rank_and_nullspace_demo.py), with six
sections: the redundant-ray geometry, the one-parameter family of models,
inconsistent data, the four subspaces by dimension, the resolution matrix, and the
first-difference operator.

The quantified outputs:

| Section | Observed | Interpretation |
|---|---|---|
| 1, rank | $\operatorname{rank}(G) = 2$, pivot columns $[1,2]$ | one redundant ray |
| 1, null space | basis $(1.0, -1.0, 1.0)$, normalised $(0.577350, -0.577350, 0.577350)$ | the model perturbation every ray is blind to |
| 1, test | $G n = (0.0, 0.0, 0.0)$ | exactly zero, not approximately |
| 2, family | seven distinct models, all with $\|Gm - d\| \le 2.2\times10^{-16}$ | perfect fits, models differing by $2.3$ $\mathrm{s/km}$ |
| 2, minimum norm | $\alpha = -0.577350$, $m^{*} = (0.666667, 0.333333, -0.333333)$, $\|m^{*}\| = 0.816497$ | the constraint selects one member |
| 3, consistency | $d = (1,0,0)$: ranks $3$ and $2$ → inconsistent | the redundancy forces $d_3 = d_1 + d_2$ |
| 4, dimensions | column 2, null 1, row 2, left-null 1 | rank–nullity twice over |
| 4, left null vector | $(-1,-1,1)$, $G^\mathsf{T}$ applied $= (0,0,0)$ | the redundant data combination |
| 5, resolution | $\operatorname{diag}(R) = (0.666667)^{3}$, $\operatorname{tr}R = 2$ | no cell resolved on its own |
| 5, projection | $\max\|R^{2} - R\| = 2.22\times10^{-16}$ | idempotent and symmetric, as a projection must be |
| 6, difference matrix | rank $4$ of $5$; null space $(1,1,1,1,1)$ | constants are invisible to a gradient |

> **Breaking exercise.** In Section 1, change the third row of $G$ to
> $(1, 2, 1.001)$ km so that the redundancy is broken by $0.1$ %. Predict, before
> running, (a) the new rank, (b) the dimension of the null space, (c) whether the
> resolution matrix is now the identity, and (d) whether the model is therefore
> well determined with $1$ ms data. Then compute the condition number and reconcile
> your answer to (d) with the value of $R$. This is the trap that
> [01-07-08](./08-svd.md) exists to disarm.

## 6. Exercises

Full set and worked solutions:
[`exercises/04-rank-and-nullspace-exercises.md`](./exercises/04-rank-and-nullspace-exercises.md)
and
[`exercises/04-rank-and-nullspace-solutions.md`](./exercises/04-rank-and-nullspace-solutions.md).
Four to start with:

**★1.** Find the rank and a basis of the null space of
$A = \begin{bmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \\ 1 & 1 & 1 \end{bmatrix}$. State
which of the two failures — existence or uniqueness — each of $d = (1,2,1)^\mathsf{T}$
and $d = (1,0,0)^\mathsf{T}$ exhibits.

**★2.** For the kernel of Section 1, decide consistency for
$d = (2, -1, 1)^\mathsf{T}$ and for $d = (2, -1, 2)^\mathsf{T}$ using the rank test,
then confirm by attempting to solve.

**★★3.** A cross-hole survey uses four rays through three cells with path lengths
$$G = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \\ 1 & 1 & 1
\end{bmatrix} \ \text{km}.$$
(a) Compute the rank and null space. (b) Which model combinations does the survey
resolve? (c) Now omit the fourth ray. Compute the condition number in both cases
(the three-ray survey and the four-ray survey) and state precisely what the fourth
ray buys — and what it does not. (d) For the full four-ray geometry, compute the
minimum-norm model that fits $d = (0.01, 0.02, 0.03, 0.06)^\mathsf{T}$ s and verify
it satisfies $Gm = d$. Explain why the phrase "minimum norm" is vacuous here.

**★★4.** For the kernel $G$ of Section 1, compute $R$ by hand from the row space
basis and verify (a) $R^2 = R$, (b) $\operatorname{tr}R = 2$, (c) that $m - Rm$ is
parallel to $\hat n$ for $m = (1, 2, 3)^\mathsf{T}$.

**★★★5.** Design a survey that has a two-dimensional null space. (a) Give the
kernel explicitly for a four-cell, four-ray geometry with $r = 2$. (b) Give a basis
of $\mathcal{N}(G)$ and of $\mathcal{N}(G^\mathsf{T})$. (c) State which
consistency conditions the data must satisfy. (d) Explain how you would use the
left null vectors as noise checks.

**★★★6.** The resolution matrix for a full-column-rank $G$ is $I$, yet the model
error in the presence of noise can still be large. (a) Explain why $R = I$ is not
contradictory with a large model error. (b) Compute $R$ and the model covariance
$\sigma_d^{2}(G^\mathsf{T}G)^{-1}$ for
$G = \begin{bmatrix} 1 & 1 \\ 1 & 1.01\end{bmatrix}$ with $\sigma_d = 10^{-3}$ s.
(c) With the same $\sigma_d$, compute the standard deviation of each of the two
parameters and of the difference $m_1 - m_2$. (d) State which of the three is
"resolved" and justify the word.

## 7. Common mistakes

1. **Treating a null space as a numerical artefact.** It is a property of the
   geometry, computable before any data are collected.
2. **Confusing a rank-deficient matrix with a nearly rank-deficient one.** The
   first has an exact null space; the second has a small singular value and no null
   space at all. The consequences are different, and
   [01-07-08](./08-svd.md) is about the difference.
3. **Believing that $R = I$ means the parameters are well determined.** Exact-data
   resolution says nothing about noise amplification.
4. **Reporting a model without its resolution matrix.** The reader cannot tell which
   features are data and which are the parameterisation.
5. **Assuming more data cannot hurt.** More data along the same geometry reduce
   noise but leave the null space untouched; they can also make a nearly-singular
   system appear better conditioned than the geometry warrants.
6. **Choosing a constraint without stating it.** Minimum norm is a physical
   assertion. So is smoothness. Silently preferring one, and presenting the result
   as *the* model, is a misrepresentation.
7. **Using $\operatorname{rank}$ from a computer without a tolerance.** Floating
   point gives you numerical rank, which depends on the threshold you set
   ([01-07-01](./01-vectors-and-spaces.md) Section 3.4).
8. **Forgetting the left null space.** It is the half of the picture that says what
   the data must satisfy, and it is where the noise checks live.

## 8. Real-world applications

- **Tomographic resolution.** Every published tomographic image is accompanied (or
  should be) by a resolution estimate derived from the ray geometry. Null-space
  vectors are why "the anomaly is not resolved below 200 km" is a statement about
  ray paths, not about data quality.
- **Ray-path illumination.** Survey design is largely the problem of making the row
  space as large as possible: adding azimuths and offsets to fill the null space.
  See [11-exploration-geophysics](../../11-exploration-geophysics/README.md) and
  [06-seismology](../../06-seismology/README.md).
- **Potential-field ambiguity.** Gravity data determine mass distributions only up
  to an equivalence class (a body and any body with the same exterior field). The
  continuous version of that statement is an infinite-dimensional null space.
- **Receiver-function and surface-wave inversion.** Velocity–depth trade-offs are
  null-space directions with a precise mathematical statement: a shift of an
  interface down combined with a velocity increase leaves the travel time
  unchanged. See [06-seismology](../../06-seismology/README.md).
- **Error checking in survey practice.** Left null vectors give repeatability
  relations and mis-tie checks without any additional fieldwork.
- **Minimum-norm and minimum-structure inversion.** The standard formulations of
  geophysical inversion are minimum-norm problems in a chosen metric; selecting the
  metric *is* selecting the result. See [18-inverse-problems](../../18-inverse-problems/README.md).

## 9. Further reading

- **Strang, G. *Introduction to Linear Algebra.* Wellesley–Cambridge Press.** The
  four fundamental subspaces, with the clearest diagrams anywhere. Level:
  beginner to intermediate.
- **Strang, G. *Linear Algebra and Its Applications.* Cengage.** The same
  material with the rank–nullity theorem given its due prominence. Level:
  beginner to intermediate.
- **Menke, W. *Geophysical Data Analysis: Discrete Inverse Theory.* Academic
  Press.** Generalised inverses, resolution and the "null space as
  non-uniqueness" idiom in the standard geophysical presentation. Level:
  intermediate.
- **Aster, R. C., Borchers, B., & Thurber, C. H. *Parameter Estimation and Inverse
  Problems.* Academic Press.** The rank, resolution and non-uniqueness discussion
  written for geophysicists, with worked tomographic examples. Level: intermediate
  to advanced.
- **Trefethen, L. N., & Bau, D. *Numerical Linear Algebra.* SIAM.** Lectures 4–5
  on the four subspaces, and the numerical caveats about computing rank. Level:
  intermediate to advanced.
- **Tarantola, A. *Inverse Problem Theory and Methods for Model Parameter
  Estimation.* SIAM.** Null-space and range-space decompositions in the
  probabilistic setting. Level: advanced.

> Note on citations: bibliographic details above are given so that you can
> locate the works. This repository does not host or reproduce copyrighted text,
> and you should confirm editions and current availability through your library
> before citing them yourself.

## 10. Self-assessment checklist

- [ ] I can compute the rank of a small matrix by hand and give the four subspace
      dimensions.
- [ ] I can use the rank test to decide consistency, and explain the result in terms
      of the column space.
- [ ] I can produce a basis of a null space from a reduced row echelon form.
- [ ] I can translate a null-space vector into one English sentence about the
      experiment.
- [ ] I can write the general solution as a particular solution plus the null space,
      and compute the minimum-norm member.
- [ ] I can build a resolution matrix for a small case and interpret its diagonal.
- [ ] I can state the difference between $R = I$ and "well determined", and explain
      which diagnostic belongs to which question.
- [ ] I can explain why repeating measurements along the same geometry cannot reduce
      a null space.

## 11. Related lessons

- [01-07-01 Vectors, Vector Spaces and Basis](./01-vectors-and-spaces.md) — where
  independence and numerical rank are defined.
- [01-07-03 Linear Systems, Gaussian Elimination and LU Factorisation](./03-systems-and-elimination.md) —
  the algorithm whose zero pivots signal the rank deficiency.
- [01-07-05 Determinants, Inverses and Matrix Conditioning](./05-determinants-inverses.md) —
  what happens when the rank is full but the singular values are small.
- [01-07-07 Orthogonality, Projections and Least Squares](./07-orthogonality.md) —
  the answer to the existence question when the data are inconsistent.
- [01-07-08 Singular Value Decomposition and Rank Truncation](./08-svd.md) — the
  single decomposition that exposes all four subspaces at once, and the resolution
  matrix in its natural notation.
- [01-07-10 Matrix Calculus and Sensitivity Derivatives](./10-matrix-calculus.md) —
  what a null space looks like when the forward model is nonlinear.
- [01-16 Functional Analysis for Inverse Problems](../16-functional-analysis/README.md) —
  rank and null space when the model space is infinite-dimensional, where the
  practical non-uniqueness of potential fields lives.
