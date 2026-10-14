---
id: 01-07-05
title: "Determinants, Inverses and Matrix Conditioning"
level: advanced
prereqs: ["01-07-03", "01-01-05"]
estimated_minutes: 90
tags: [linear-algebra, determinant, conditioning, error-propagation]
---

# Determinants, Inverses and Matrix Conditioning

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** the determinant as the volume scale factor of a linear map, and
   **compute** it by cofactor expansion and from the pivots of an elimination.
2. **Use** the product and transpose rules, and explain why
   $\det = 0$ is equivalent to singularity.
3. **Define** the condition number in the 2-norm, compute it from singular values,
   and **state** the error bound that makes it operational.
4. **Explain** why the determinant is not a measure of near-singularity, with a
   counterexample in which a larger determinant accompanies a much worse
   conditioning.
5. **Predict** the accuracy of a solution from the condition number and the
   floating-point precision, and **diagnose** a case in which the prediction is
   attained rather than merely satisfied.
6. **Explain** why forming $G^\mathsf{T}G$ halves the number of usable digits, and
   quantify the threshold at which it fails outright.

## Prerequisites

[01-07-03 Linear Systems, Gaussian Elimination and LU Factorisation](./03-systems-and-elimination.md)
for elimination, pivots and the $LU$ factorisation, and
[01-01-05 Absolute vs Relative Error, Conditioning and Stability](../01-arithmetic/05-error-and-conditioning.md)
for the distinction between the conditioning of a problem and the stability of an
algorithm, which this lesson makes concrete for matrices.

## 1. Intuition: why inverse problems are hard before regularisation

Consider two rays through two cells whose path lengths differ by only
$\delta$ km in the second cell:

$$G = \begin{bmatrix} 1 & 1 \\ 1 & 1+\delta \end{bmatrix}, \qquad
d = Gm, \qquad m = \begin{bmatrix} m_1 \\ m_2 \end{bmatrix} \ \mathrm{s/km}.$$

This matrix is invertible for every $\delta > 0$. It has full rank, its columns are
independent, and there is a unique model fitting any data vector. By any exact
algebraic criterion the problem is perfectly well posed.

And yet, at $\delta = 10^{-4}$ a measurement error of 1 ms in a travel time of
about 30 ms produces a model error of $20$ $\mathrm{s/km}$ in a model whose total
size is $0.054$ $\mathrm{s/km}$. The answer is not merely uncertain; it is
meaningless, and no inversion code can repair it. *This* is what "ill-conditioned"
means, and it is the state of affairs that exists in every real experiment before a
regularisation term is added.

The quantity that measures it is the **condition number**

$$\kappa_2(G) = \frac{\sigma_{\max}}{\sigma_{\min}} ,$$

the ratio of the largest to the smallest singular value. For this geometry
$\kappa_2 = 4/\delta$ to leading order, so at $\delta = 10^{-4}$ we have
$\kappa_2 = 4.0\times10^{4}$: a factor of $40000$ amplification of any relative data
error, with no sign of any pathology in $\det G = \delta$.

Two lessons are contained in that last sentence:

- The determinant is *not* the diagnostic. It changes with units and does not track
  $\kappa$ (Section 3.5).
- The loss of accuracy is a property of the *geometry*, not of the algorithm. The
  right response is to change the experiment or add information, not to buy a
  better solver.

## 2. Precise definitions

### 2.1 The determinant

For a square matrix $A$, the determinant is the unique alternating multilinear
function of the columns normalised so that $\det I = 1$. Three equivalent
characterisations are useful:

- **Volume.** $|\det A|$ is the factor by which $A$ scales volumes: the image of the
  unit cube is a parallelepiped of volume $|\det A|$.
- **Sign.** The sign records whether the map preserves or reverses orientation.
- **Expansion.** $\det A = \sum_{\sigma \in S_n}\operatorname{sgn}(\sigma)\prod_i
  A_{i,\sigma(i)}$, the Leibniz formula, which is the definition but never the
  algorithm for $n$ above a very small value: it costs $n!$ terms.

For $2\times2$, $\det A = A_{11}A_{22} - A_{12}A_{21}$: the oriented area of the
image of the unit square. For $3\times3$ and above, cofactor expansion along a row
or column:

$$\det A = \sum_j (-1)^{i+j}A_{ij}M_{ij},$$

where $M_{ij}$ is the minor obtained by deleting row $i$ and column $j$.

### 2.2 The rules

$$\det(AB) = \det A \det B, \qquad \det A^\mathsf{T} = \det A, \qquad
\det(A^{-1}) = 1/\det A, \qquad \det(\alpha A) = \alpha^{n}\det A.$$

The multiplicative rule is the reason a determinant can be computed from pivots:
elimination performs row additions (which do not change the determinant) and row
swaps (which flip the sign), so

$$\det A = (-1)^{s}\prod_{i} U_{ii},$$

with $s$ the number of swaps. The rule also means $\det$ multiplies across a chain
of maps, so the volume scale of a processing sequence is the product of the
individual scale factors. That is why a filter whose determinant is very small
nearly destroys information, and why cascaded deconvolutions amplify noise.

### 2.3 Inverses

For nonsingular $A$, the **inverse** is the unique $A^{-1}$ with
$AA^{-1} = A^{-1}A = I$, and

$$(A^{-1})_{ij} = \frac{(-1)^{i+j}M_{ji}}{\det A} ,$$

which shows immediately that a small determinant makes the entries of the inverse
large. Two practical warnings follow.

- **Never compute an inverse in order to solve a system.** Solving by
  factorisation costs $\tfrac{n^{3}}{3}$ multiply-adds against roughly $n^{3}$ for
  forming $A^{-1}$ and then $n^{2}$ per solve; the factors are reusable and more
  accurate ([01-07-03](./03-systems-and-elimination.md)).
- **Cofactor expansion is not an algorithm.** Its cost grows factorially; the
  Gauss–Jordan elimination used by the demonstrations costs $n^{3}$.

### 2.4 Norms and the condition number

For a general matrix, with $\|\cdot\|$ an induced norm,

$$\kappa(A) = \|A\|\,\|A^{-1}\| .$$

In the 2-norm, $\|A\|_2 = \sigma_{\max}(A)$ and $\|A^{-1}\|_2 =
1/\sigma_{\min}(A)$, so

$$\kappa_2(A) = \frac{\sigma_{\max}}{\sigma_{\min}} .$$

Properties worth committing to memory:

- $\kappa \ge 1$, with equality for scalar multiples of an orthogonal matrix.
- $\kappa$ is invariant under orthogonal transformations: $\kappa(QA) =
  \kappa(AQ^\mathsf{T}) = \kappa(A)$ for orthogonal $Q$. This is why it is the right
  quantity: a rotation or a change of orthonormal basis cannot change the difficulty
  of a problem.
- $\kappa$ is *not* invariant under general row or column scaling, so a
  diagonally-scaled problem has a different $\kappa$. **Equilibration** — scaling
  rows and columns so that the entries are comparable — is therefore a real
  preconditioning step, and it is standard practice before a large solve.
- $\kappa_2(A^\mathsf{T}A) = \kappa_2(A)^{2}$ for rectangular $A$ of full column
  rank. This single identity explains why the normal equations are a numerical
  liability, and Section 3.6 quantifies the damage.

### 2.5 The error bound

Let $\hat m$ be the computed solution of $Gm = d$ with a perturbation $\delta d$
in the data. Then, exactly,

$$\frac{\|\delta m\|}{\|m\|} \;\le\; \kappa(G)\,\frac{\|\delta d\|}{\|d\|} ,$$

and the bound is attained when the model and the perturbation both lie in the
singular direction of $\sigma_{\min}$. Round-off in the solution of an $n \times n$
system gives approximately $\|\delta m\|/\|m\| \lesssim \kappa(G)\,\epsilon_{\text{mach}}$
with $\epsilon_{\text{mach}} \approx 2.2\times10^{-16}$ for IEEE double precision.

The interpretation is the whole of practical linear algebra: **you lose
$\log_{10}\kappa$ digits**. At $\kappa = 10^{4}$ you keep 12 significant digits; at
$\kappa = 10^{12}$ you keep 4; at $\kappa > 1/\epsilon_{\text{mach}} = 4.5\times10^{15}$
you keep none, and the system is *numerically singular* even though it is exactly
invertible.

## 3. Step-by-step derivations

### 3.1 The determinant of the tomography kernel, two ways

For the tridiagonal kernel of [01-07-03](./03-systems-and-elimination.md),

$$G = \begin{bmatrix} 2 & 1 & 0 \\ 1 & 2 & 1 \\ 0 & 1 & 2 \end{bmatrix},$$

the pivots found by elimination were $2$, $1.5$ and $4/3$, so
$\det G = 2 \times 1.5 \times 4/3 = 4.000000$ with no sign correction. Cofactor
expansion along the first row gives

$$\det G = 2\begin{vmatrix} 2 & 1 \\ 1 & 2 \end{vmatrix}
- 1\begin{vmatrix} 1 & 1 \\ 0 & 2 \end{vmatrix}
+ 0 = 2(4-1) - 1(2) = 4 ,$$

agreeing exactly. A determinant of 4 means the unit cube of slowness perturbations
maps to a parallelepiped of volume 4 in the data space, in the mixed units of
$\mathrm{s/km}\cdot\mathrm{km} = \mathrm{s}$: the geometry is far from degenerate.

The rank-deficient kernel of [01-07-04](./04-rank-and-nullspace.md),
$\begin{bmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 1 & 2 & 1\end{bmatrix}$, gives
$\det = 0.0$ exactly, because its third row is the sum of the first two. And for
the two test matrices of the demonstration,
$A = \begin{bmatrix} 1 & 2 \\ 3 & 4\end{bmatrix}$ and
$B = \begin{bmatrix} 0 & 1 \\ -1 & 2\end{bmatrix}$:

$$\det(AB) = -2.000000 = \det A \det B, \qquad
\det A^\mathsf{T} = -2.000000 = \det A .$$

### 3.2 An inverse that exists and should not be used

For $G(\delta) = \begin{bmatrix} 1 & 1 \\ 1 & 1+\delta\end{bmatrix}$:

| $\delta$ | $\det$ | $\max|(G^{-1})_{ij}|$ | $\max|GG^{-1} - I|$ |
|---|---|---|---|
| $1$ | $1.000\times10^{0}$ | $2.0000\times10^{0}$ | 0 |
| $10^{-1}$ | $1.000\times10^{-1}$ | $1.1000\times10^{1}$ | 0 |
| $10^{-2}$ | $1.000\times10^{-2}$ | $1.0100\times10^{2}$ | 0 |
| $10^{-4}$ | $1.000\times10^{-4}$ | $1.0001\times10^{4}$ | 0 |

The product $GG^{-1}$ is the identity to machine precision in every case, so these
matrices really are invertible and the computed inverse really is correct. The
entries of $G^{-1}$ nevertheless grow like $1/\delta$: an inverse that is
*arithmetically valid* and *physically useless*. This is the case that exposes the
poverty of the phrase "the matrix is invertible" as a statement about a measurement.

The exact inverse is worth writing down:

$$G^{-1} = \frac{1}{\delta}\begin{bmatrix} 1+\delta & -1 \\ -1 & 1 \end{bmatrix}
= \begin{bmatrix} 1 + \tfrac{1}{\delta} & -\tfrac{1}{\delta} \\
-\tfrac{1}{\delta} & \tfrac{1}{\delta} \end{bmatrix},$$

which shows the amplification structure directly: the difference
$(m_1 - m_2)$ is estimated with the coefficient $-\tfrac{1}{\delta}$ acting on
$-(d_1 - d_2)$, so an error in the *difference of the data* is amplified by
$1/\delta$.

### 3.3 The condition number, and its scaling with geometry

| $\delta$ | $\sigma_{\max}$ | $\sigma_{\min}$ | $\kappa_2$ | $\kappa_2\delta$ |
|---|---|---|---|---|
| $10^{-1}$ | 2.051249 | $4.875078\times10^{-2}$ | $4.207623\times10^{1}$ | 4.2076 |
| $10^{-2}$ | 2.005012 | $4.987500\times10^{-3}$ | $4.020075\times10^{2}$ | 4.0201 |
| $10^{-3}$ | 2.000500 | $4.998750\times10^{-4}$ | $4.002001\times10^{3}$ | 4.0020 |
| $10^{-4}$ | 2.000050 | $4.999875\times10^{-5}$ | $4.000200\times10^{4}$ | 4.0002 |
| $10^{-6}$ | 2.000001 | $4.999999\times10^{-7}$ | $4.000002\times10^{6}$ | 4.0000 |
| $10^{-8}$ | 2.000000 | $5.000000\times10^{-9}$ | $4.000000\times10^{8}$ | 4.0000 |
| $10^{-10}$ | 2.000000 | $4.999999\times10^{-11}$ | $4.000001\times10^{10}$ | 4.0000 |

The product $\kappa_2\delta$ is constant, so $\kappa_2 = 4/\delta$: the conditioning
is set by the *ray geometry*, and the constant 4 is a property of this particular
normalisation. Deriving the limit analytically is worth doing, because it shows
where the factor comes from. The eigenvalues of the symmetric matrix
$G(\delta)$ are

$$\lambda_{\pm} = \frac{(2+\delta) \pm \sqrt{4+\delta^{2}}}{2},$$

so $\lambda_{+} \to 2$ and $\lambda_{-} \to \delta/2$, giving $\kappa_2 \to
4/\delta$. The cancellation in computing $\lambda_{-}$ directly is severe — it is a
difference of nearly equal quantities — so the numerically stable form is the
rationalised one:

$$\sigma_{\min} = \lambda_{-} = \frac{2\delta}{(2+\delta) + \sqrt{4+\delta^{2}}} ,$$

which at $\delta = 10^{-8}$ gives exactly $5.000000\times10^{-9}$.

**This is where the demonstration shows something important about algorithms.** The
same table computed through the eigenvalues of $G^\mathsf{T}G$ — the textbook
identity $\sigma^{2} = \lambda(G^\mathsf{T}G)$ — reports $\sigma_{\min} = 0$ and
therefore $\kappa = \infty$ from $\delta = 10^{-8}$ onwards, because
$\kappa_2(G^\mathsf{T}G) = \kappa_2(G)^{2} = 1.6\times10^{17}$ exceeds
$1/\epsilon_{\text{mach}}$. The matrix has not changed; only the route taken to its
singular values. Computing a singular value through $G^\mathsf{T}G$ costs you half
your digits, and the practical SVD of [01-07-08](./08-svd.md) is built specifically
to avoid that step.

### 3.4 The error bound, attained rather than satisfied

At $\delta = 10^{-4}$: $\kappa_2(G) = 4.000200\times10^{4}$ and
$\|G^{-1}\|_2 = 2.000050\times10^{4}$. Perturb the data in the direction of the
smallest left singular vector — the direction that becomes the null space as
$\delta \to 0$, here approximately $(0.7071, -0.7071)$:

| relative data error | $\|\delta m\|/\|m\|$ | bound $\kappa\,\|\delta d\|/\|d\|$ | gain $\|\delta m\|/\|\delta d\|$ |
|---|---|---|---|
| $10^{-6}$ | $1.5757\times10^{-2}$ | $4.0002\times10^{-2}$ | $2.0001\times10^{4}$ |
| $10^{-5}$ | $1.5757\times10^{-1}$ | $4.0002\times10^{-1}$ | $2.0001\times10^{4}$ |
| $10^{-4}$ | $1.5757\times10^{0}$ | $4.0002\times10^{0}$ | $2.0001\times10^{4}$ |
| $10^{-3}$ | $1.5757\times10^{1}$ | $4.0002\times10^{1}$ | $2.0001\times10^{4}$ |

The gain $\|\delta m\|/\|\delta d\|$ equals $\|G^{-1}\|_2 = 1/\sigma_{\min}$ to six
figures: for this perturbation the bound $\|\delta m\| \le \|G^{-1}\|\|\delta d\|$ is
*attained exactly*, not merely satisfied.

Note the subtlety. The relative model error $1.5757\times10^{-2}$ at
$\delta d/\|d\| = 10^{-6}$ is *below* $\kappa \times 10^{-6}
= 4.0\times10^{-2}$: the bound in terms of $\kappa$ cannot be attained unless the
model itself also lies in the worst-resolved direction, and here it does not. The
two bounds are different statements: $\|\delta m\| \le \|G^{-1}\|\|\delta d\|$
concerns the operator norm for a given perturbation direction and is tight; the
$\kappa$-version concerns relative errors and is attained only in the worst case for
both. Both are used, and mixing them up produces either false alarm or false
comfort.

Practically: a 1 ms picking error — routine — in the worst direction moves the
model by $20.0$ $\mathrm{s/km}$ against a total model size of $0.0539$
$\mathrm{s/km}$. Nothing about the inversion code is at fault.

### 3.5 The determinant is not a conditioning measure

$$\begin{aligned}
A = \begin{bmatrix} 1 & 0 \\ 0 & 10^{-3}\end{bmatrix}
&\quad \det = 1.000000\times10^{-3}, \quad \kappa_2 = 1.000000\times10^{3}, \\
A = \begin{bmatrix} 10^{3} & 0 \\ 0 & 10^{-3}\end{bmatrix}
&\quad \det = 1.000000\times10^{0}, \quad \kappa_2 = 1.000000\times10^{6}.
\end{aligned}$$

The second matrix has a *larger* determinant — a thousand times larger — and is
*more than a thousand times worse conditioned*. The determinant cannot be the
diagnostic, and the reason is structural rather than accidental: $\det$ is
multilinear, so expressing a length in metres instead of kilometres multiplies a row
by $10^{3}$ and the determinant by $10^{3}$, while the difficulty of the underlying
problem is unchanged. $\kappa_2$ is invariant under orthogonal transformations, so
it does not suffer this defect.

The historical use of the determinant as a singularity test survives because for
$2\times2$ and $3\times3$ problems with quantities of order 1 it happens to
correlate. Do not carry it further.

### 3.6 Forming $G^\mathsf{T}G$ squares the condition number

Since $\kappa_2(G^\mathsf{T}G) = \kappa_2(G)^{2}$ exactly for a full-column-rank
$G$, the normal equations of [01-07-07](./07-orthogonality.md) double the exponent
of the difficulty:

| $\delta$ | $\kappa_2(G)$ | $\kappa_2(G^\mathsf{T}G)$ | numerically singular ($\kappa > 1/\epsilon$)? |
|---|---|---|---|
| $10^{-2}$ | $4.020075\times10^{2}$ | $1.616100\times10^{5}$ | no |
| $10^{-3}$ | $4.002001\times10^{3}$ | $1.601601\times10^{7}$ | no |
| $10^{-4}$ | $4.000200\times10^{4}$ | $1.600160\times10^{9}$ | no |
| $10^{-5}$ | $4.000020\times10^{5}$ | $1.600016\times10^{11}$ | no |
| $10^{-6}$ | $4.000002\times10^{6}$ | $1.600002\times10^{13}$ | no |
| $10^{-8}$ | $4.000000\times10^{8}$ | $1.600000\times10^{17}$ | **yes** |

The normal equations become numerically singular once $\kappa_2(G)$ passes
$\sqrt{1/\epsilon_{\text{mach}}} \approx 6.7\times10^{7}$, which in this geometry is
$\delta$ of order $10^{-8}$. The geometry is not singular; $G$ is still perfectly
usable at $\kappa = 4\times10^{8}$ (losing eight of sixteen digits). It is the
reformulation that has been destroyed.

### 3.7 A well-posed three-ray experiment, for contrast

The three-ray kernel of [01-07-03](./03-systems-and-elimination.md) has singular
values $3.414214$, $2.000000$ and $0.585786$, hence

$$\kappa_2 = 5.828427 = 3 + 2\sqrt2, \qquad
\frac{1}{\sigma_{\min}} = 1.707107 .$$

Perturbing the data in the worst direction by a relative $1$ % gives a relative
model error of $3.391\times10^{-2}$ — that is, 3.4 % — with the gain again equal to
$1/\sigma_{\min} = 1.707107$ to six figures. Compare this with the $1575$ % model
error of the two-ray case at the same data error: the difference is entirely
geometry, and it was determined when the rays were laid out.

## 4. Physical interpretation

**$\kappa$ is a survey-design number.** It is fixed by the ray geometry, the
station distribution, the parameterisation and the units. It is computable *before*
collecting data, and comparing $\kappa$ across candidate designs is the quantitative
core of survey design. Reducing $\kappa$ from $10^{4}$ to $10$ is worth more than
any improvement in solver.

**The digits you can recover are $\text{precision} - \log_{10}\kappa$.** Double
precision gives about 16 digits; a $\kappa$ of $10^{6}$ leaves 10; a $\kappa$ of
$10^{12}$ leaves 4, and reporting a model to six significant figures from such a
system is a fabrication. This arithmetic should precede any inversion; it takes one
SVD and one logarithm.

**Regularisation is an admission about $\kappa$.** Every regularised inversion
introduces a parameter that limits how much of the small-singular-value directions
it uses, precisely because those directions are dominated by noise. Damping,
truncation, smoothness penalties and Bayesian priors are four names for four
different ways of making the same admission; [01-07-08](./08-svd.md) Section 5 shows
the truncation version quantitatively.

**Units are part of the model, and part of $\kappa$.** A parameter measured in
$\mathrm{s/m}$ and one measured in $\mathrm{km}$ that describe comparable physics
will produce a badly scaled matrix. This is not cosmetic: equilibration is a real
preconditioning step, and it is why dimensionless parameterisation is the standard
first move in setting up an inversion.

**A small determinant is a warning about scale, not about singularity.** It tells
you that the map shrinks volumes, which happens for any map with a small column or a
near-dependent pair of columns, and also for a perfectly well-behaved map expressed
in awkward units.

## 5. Python demonstration

The companion script is
[`code/conditioning_demo.py`](./code/conditioning_demo.py), with seven sections:
the determinant as a volume factor, the usable-but-unusable inverse, the condition
number and its $1/\delta$ scaling, the error-propagation table, the squaring of
$\kappa$ in the normal equations, the determinant counterexample, and the
well-posed three-ray contrast.

The quantified outputs:

| Section | Observed | Interpretation |
|---|---|---|
| 1, volume | $\det G = 4.000000$; rank-deficient kernel $\det = 0.0$ | the determinant measures volume scale, and vanishes at rank loss |
| 1, rules | $\det(AB) = \det A\det B = -2.000000$; $\det A^\mathsf{T} = \det A$ | the multiplicative structure of $\det$ |
| 2, inverse | $\max|(G^{-1})_{ij}| = 2.0,\ 11.0,\ 101.0,\ 10001$ for $\delta = 1,\ 10^{-1},\ 10^{-2},\ 10^{-4}$ | invertible, and unusable |
| 3, scaling | $\kappa_2\delta \approx 4.000$ across six decades | $\kappa_2 = 4/\delta$: the geometry sets the difficulty |
| 3, stable vs naive | $A^\mathsf{T}A$ route gives $\sigma_{\min} = 0$, $\kappa = \infty$ from $\delta = 10^{-8}$; direct route gives $5\times10^{-9}$ | computing through $G^\mathsf{T}G$ costs half the digits |
| 4, propagation | gain $= 2.0001\times10^{4} = 1/\sigma_{\min}$ exactly | the operator-norm bound is attained |
| 5, normal equations | $\kappa(G^\mathsf{T}G) = 1.6\times10^{17}$ at $\delta = 10^{-8} > 1/\epsilon$ | the reformulation, not the problem, becomes singular |
| 6, determinant | $\det$ rises $10^{-3} \to 10^{0}$ while $\kappa$ rises $10^{3} \to 10^{6}$ | determinant does not track difficulty |
| 7, healthy case | $\kappa_2 = 5.828427$; gain $= 1/\sigma_{\min} = 1.707107$ | a good geometry, and the same bound attained |

> **Breaking exercise.** In Section 3, keep the matrix real but *rescale the first
> column* by $10^{6}$, so that the two model parameters are measured in different
> units. Predict, before running, which of $\det G$ and $\kappa_2(G)$ changes.
> Then check your prediction by computing both. The result is the cleanest possible
> demonstration that a determinant is a statement about units as much as about
> geometry.

## 6. Exercises

Full set and worked solutions:
[`exercises/05-determinants-inverses-exercises.md`](./exercises/05-determinants-inverses-exercises.md)
and
[`exercises/05-determinants-inverses-solutions.md`](./exercises/05-determinants-inverses-solutions.md).
Four to start with:

**★1.** Compute the determinant, the adjugate and the inverse of
$A = \begin{bmatrix} 3 & 1 \\ 2 & 4 \end{bmatrix}$, and verify $AA^{-1} = I$ by
hand.

**★2.** For $B = \begin{bmatrix} 1 & 2 & 0 \\ 0 & 3 & 1 \\ 2 & 1 & 1\end{bmatrix}$
compute $\det B$ by (a) cofactor expansion along the first row and (b) elimination
with pivots. Confirm the two agree and state the number of row swaps.

**★★3.** A two-station, two-layer experiment gives
$G = \begin{bmatrix} 1 & 1 \\ 1 & 1.05\end{bmatrix}$ km with travel-time
uncertainty $0.5$ ms. (a) Compute $\kappa_2(G)$ and $\det G$. (b) Give the
worst-case relative model error for a relative data error of $10^{-3}$. (c) Now
express the same physical experiment with distances in metres
($G' = \begin{bmatrix} 1000 & 1000 \\ 1000 & 1050\end{bmatrix}$): compute
$\kappa_2(G')$ and $\det G'$ and discuss which changed. (d) If the second station
could be moved to make the path lengths $(1, 1.5)$, compute the new $\kappa_2$ and
state the reduction factor.

**★★4.** Explain, with a numerical example, why $\kappa_2(G^\mathsf{T}G) =
\kappa_2(G)^{2}$ implies that the normal equations are unusable once
$\kappa_2(G) > 6.7\times10^{7}$. Give the explicit $\delta$ at which this happens
for the two-ray geometry of Section 3 and verify it numerically.

**★★★5.** Equilibration. For
$A = \begin{bmatrix} 10^{3} & 1 \\ 1 & 10^{-3}\end{bmatrix}$, compute $\kappa_2(A)$
and $\kappa_2$ of the row- and column-equilibrated version $D_1AD_2$ with $D_1, D_2$
diagonal and chosen so that all entries of the result have magnitude at most 1.
(a) Report both condition numbers. (b) State whether equilibration can ever change
the *solution* of a consistent system, and why. (c) Explain what equilibration does
change, and why that matters for a parameterised inverse problem.

**★★★6.** Design a numerical experiment measuring the number of correct digits in
the solution of $G(\delta)m = d$ as a function of $\delta$, for $\delta$ from
$10^{-2}$ to $10^{-14}$ in the geometry of Section 1. (a) Plot (or tabulate)
observed relative error against $\kappa_2(G)\epsilon_{\text{mach}}$. (b) Report the
$\delta$ at which all digits are lost. (c) Compare with the theoretical prediction
and state any deviation and its cause. (d) State the limits of your conclusion: does
the answer depend on the right-hand side you chose?

## 7. Common mistakes

1. **Using the determinant to detect ill-conditioning.** Section 3.5 gives a
   counterexample in which a larger determinant accompanies a hundred-fold worse
   conditioning.
2. **Concluding from $GG^{-1} = I$ that the inverse is useful.** Section 3.2 shows
   an exact inverse with entries of order $10^{4}$ for a $2\times2$ matrix.
3. **Reporting more significant figures than $\kappa$ permits.** A $\kappa$ of
   $10^{8}$ in double precision leaves about eight digits in the solution, not
   sixteen.
4. **Forming $G^\mathsf{T}G$ and then wondering why the answer is wrong.** The
   condition number is squared; Section 3.6 gives the threshold.
5. **Mixing norms in an error bound.** $\|\delta m\|_2 \le \|G^{-1}\|_2\|\delta d\|_2$
   is correct; substituting the Frobenius norm or the 1-norm without changing the
   right-hand side is not.
6. **Confusing the $\kappa$ bound with the operator-norm bound.** Section 3.4 shows
   that one is attained and the other is not, in the same table.
7. **Treating conditioning as an algorithmic problem.** No solver improves $\kappa$;
   better geometry, better parameterisation or regularisation does.
8. **Ignoring units when forming $\kappa$.** A model with one parameter in
   $\mathrm{s/m}$ and another in $\mathrm{s/km}$ has an artificially large $\kappa$;
   make the parameterisation dimensionless first.

## 8. Real-world applications

- **Survey design.** Offset range, azimuth coverage, station spacing and receiver
  array geometry are all proposals about $\kappa$. Computing $\kappa$ for a
  candidate geometry before mobilising is standard in exploration seismology; see
  [11-exploration-geophysics](../../11-exploration-geophysics/README.md).
- **Inversion diagnostics.** Every inversion pipeline should report $\kappa$ and the
  number of digits it can support, and should refuse to report more.
- **Regularisation threshold selection.** The truncation criterion of
  [01-07-08](./08-svd.md) and the damping parameter of Tikhonov regularisation are
  both chosen by looking at where $\sigma_i$ approaches the noise-to-signal
  threshold.
- **Velocity–depth trade-off.** The classical trade-off of reflection seismology is
  a direction with a small singular value: increasing depth and increasing velocity
  in the right proportion leaves travel times nearly unchanged, and $\kappa$
  quantifies how nearly. See [06-seismology](../../06-seismology/README.md).
- **Preconditioning large systems.** Equilibration and incomplete factorisation are
  practical attempts to reduce the effective $\kappa$ of a discretised PDE, and the
  iteration count of an iterative solver scales with $\sqrt{\kappa}$
  ([01-07-09](./09-sparse-matrices.md) Section 6).
- **Geodetic network adjustment.** A network with a nearly degenerate geometry — all
  baselines nearly parallel — produces a nearly singular normal matrix; the tell-tale
  is $\kappa$, and the remedy is additional baselines with different orientation.
- **Instrument and unit practice.** Recording slowness in $\mathrm{s/m}$ and depth
  in km in the same matrix guarantees a large $\kappa$ for reasons that have nothing
  to do with the Earth.

## 9. Further reading

- **Trefethen, L. N., & Bau, D. *Numerical Linear Algebra.* SIAM.** Lectures 12 and
  15 on conditioning and on why $\kappa$ is the right measure; the discussion of
  invariant measures is directly relevant to Section 3.5. Level: intermediate to
  advanced.
- **Higham, N. J. *Accuracy and Stability of Numerical Algorithms.* SIAM.** The
  definitive treatment of error bounds for linear systems, including the cases in
  which the $\kappa$ bound is pessimistic. Level: advanced.
- **Golub, G. H., & Van Loan, C. F. *Matrix Computations.* Johns Hopkins
  University Press.** Sections on condition estimation (LAPACK's `gecon`) and on
  equilibration. Level: advanced.
- **Strang, G. *Introduction to Linear Algebra.* Wellesley–Cambridge Press.** The
  determinant as a volume, and the cofactor formula, presented geometrically.
  Level: beginner to intermediate.
- **Menke, W. *Geophysical Data Analysis: Discrete Inverse Theory.* Academic
  Press.** The eigenvalue and singular-value view of instability, with geophysical
  examples of the small-singular-value direction. Level: intermediate.
- **Aster, R. C., Borchers, B., & Thurber, C. H. *Parameter Estimation and Inverse
  Problems.* Academic Press.** Conditioning, regularisation and the practical
  decision of how much of the small-singular-value spectrum to use. Level:
  intermediate to advanced.
- **Hansen, P. C. *Discrete Inverse Problems: Insight and Algorithms.* SIAM.** The
  Picard condition and the L-curve, both of which are about the noise level
  interacting with small singular values. Level: advanced.

> Note on citations: bibliographic details above are given so that you can
> locate the works. This repository does not host or reproduce copyrighted text,
> and you should confirm editions and current availability through your library
> before citing them yourself.

## 10. Self-assessment checklist

- [ ] I can define the determinant geometrically and compute one by two independent
      methods.
- [ ] I can state the product, transpose and scaling rules for determinants.
- [ ] I can compute $\kappa_2$ from singular values and state the error bound it
      controls.
- [ ] I can produce a counterexample showing that the determinant is not a
      conditioning measure.
- [ ] I can quote the number of digits available as $16 - \log_{10}\kappa$ and apply
      it to a given problem.
- [ ] I can explain why $\kappa(G^\mathsf{T}G) = \kappa(G)^{2}$ and at what
      conditioning the normal equations die.
- [ ] I can distinguish the attained operator-norm bound from the worst-case relative
      bound.
- [ ] I can say what equilibration changes and what it cannot change.

## 11. Related lessons

- [01-07-03 Linear Systems, Gaussian Elimination and LU Factorisation](./03-systems-and-elimination.md) —
  the pivots whose product is the determinant.
- [01-07-04 Rank, Null Space and Solvability](./04-rank-and-nullspace.md) — the exact
  version of the failure this lesson measures in degrees.
- [01-07-07 Orthogonality, Projections and Least Squares](./07-orthogonality.md) —
  the normal equations, and the QR alternative that avoids the squaring.
- [01-07-08 Singular Value Decomposition and Rank Truncation](./08-svd.md) — where
  the singular values that define $\kappa$ come from, and how to use them as a
  filter.
- [01-01-04 Floating-Point Representation, Round-Off and Catastrophic Cancellation](../01-arithmetic/04-floating-point.md) —
  the $\epsilon_{\text{mach}}$ that appears in every bound here.
- [01-01-05 Absolute vs Relative Error, Conditioning and Stability](../01-arithmetic/05-error-and-conditioning.md) —
  the general theory of which this lesson is the linear-algebraic case.
- [19-numerical-modeling-hpc](../../19-numerical-modeling-hpc/README.md) —
  preconditioning at scale, where reducing $\kappa$ is the whole game.
