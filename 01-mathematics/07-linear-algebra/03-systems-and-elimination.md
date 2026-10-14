---
id: 01-07-03
title: "Linear Systems, Gaussian Elimination and LU Factorisation"
level: intermediate
prereqs: ["01-07-02", "01-02-05"]
estimated_minutes: 90
tags: [linear-algebra, elimination, lu-factorisation, tomography]
---

# Linear Systems, Gaussian Elimination and LU Factorisation

## Learning objectives

By the end of this lesson you will be able to:

1. **Read** a linear system in both the row picture (equations) and the column
   picture (a combination of kernels), and say which picture answers which
   question.
2. **Carry out** Gaussian elimination with partial pivoting by hand, and say why
   each row operation preserves the solution set.
3. **Explain** why pivoting is required rather than advisable, and construct a
   system in which the unpivoted algorithm divides by zero.
4. **Factorise** a matrix as $PA = LU$, interpret the entries of $L$ as
   multipliers, and use the factors to solve the same system for several
   right-hand sides.
5. **Count** the cost of elimination, state its leading order, and explain why
   cost growth of order $n^{3}$ makes structure a necessity for large problems.
6. **Compute** a determinant from the pivots, and explain the connection with
   singular matrices.
7. **Distinguish** a small residual from a small solution error and explain, with
   an example, why the first does not imply the second.

## Prerequisites

[01-07-02 Matrices, Matrix Multiplication and Linear Maps](./02-matrices-and-operations.md)
for the matrix-as-map viewpoint, and
[01-02-05 Linear and Nonlinear Systems of Equations](../02-algebra/05-systems-of-equations.md)
for the elementary algebra of simultaneous equations that this lesson organises
into an algorithm.

## 1. Intuition: solving for an Earth model from data

Suppose a region is divided into three cells, and rays traverse it. If a ray spends
a length $L_{ij}$ (km) in cell $j$, and the slowness perturbation in cell $j$ is
$m_j$ ($\mathrm{s/km}$), then the travel-time residual for that ray is

$$d_i = \sum_j L_{ij} m_j .$$

Three rays and three cells give three equations in three unknowns, so the measured
residuals determine the model — provided the geometry is not degenerate. For a
concrete case the path lengths give

$$G = \begin{bmatrix} 2 & 1 & 0 \\ 1 & 2 & 1 \\ 0 & 1 & 2 \end{bmatrix}
\quad\text{km}, \qquad m = \begin{bmatrix} 0.050 \\ -0.020 \\ 0.100 \end{bmatrix}
\ \mathrm{s/km}, \qquad d = \begin{bmatrix} 0.080 \\ 0.110 \\ 0.180 \end{bmatrix}
\ \mathrm{s} .$$

Everything in this lesson is a way of getting $m$ back from $d$ — reliably, cheaply,
and with an honest account of how the rounding errors propagate.

Two questions arise immediately and recur in every later lesson.

**Does the algorithm always work?** No. The textbook elimination procedure can
divide by zero even when the matrix is perfectly invertible. Fixing that is called
pivoting, and it is a small change with a large consequence.

**How does the cost scale?** Elimination costs about $\tfrac{2}{3}n^{3}$
operations. For $n = 10^{3}$ that is $6.7\times10^{8}$; for $n = 10^{5}$ it is
$6.7\times10^{14}$ and no computer will finish. Linear algebra at geophysical scale
is therefore about *exploiting structure*, which is why this module returns to
sparsity in [01-07-09](./09-sparse-matrices.md) and to iterative methods in
[01-07-06](./06-eigenvalues.md) Section 5.

## 2. Precise definitions

### 2.1 The two pictures

The system $Gm = d$ with $G$ being $n \times n$ has two readings:

- **Row picture.** Each of the $n$ equations is a hyperplane in $\mathbb{R}^{n}$.
  The solution is their common intersection: a point if they are independent, a
  line or plane if they are not, empty if they disagree.
- **Column picture.** $Gm = \sum_j m_j g_j$: a weighted combination of the columns
  of $G$ is to reproduce $d$. A solution exists exactly when $d$ lies in the span
  of the columns.

The row picture answers "is there a solution?" and the column picture answers
"which $d$ are reachable?". Both matter, and they are the same statement seen from
two sides.

### 2.2 Elementary row operations, and why they preserve the solution set

Three operations may be applied to the augmented matrix $[G \mid d]$:

1. swap two rows;
2. multiply a row by a nonzero scalar;
3. add a multiple of one row to another.

Each is multiplication on the left by an invertible matrix, so each preserves the
set of solutions of the system. Operation 3 with the multiplier chosen to cancel
one entry is **elimination**.

### 2.3 Elimination, formalised

For $k = 0, \ldots, n-2$, with pivots $G_{kk} \neq 0$, compute
$\ell_{ik} = G_{ik}^{(k)}/G_{kk}^{(k)}$ and update rows $i > k$:

$$G_{ij} \leftarrow G_{ij} - \ell_{ik}G_{kj}, \qquad d_i \leftarrow d_i - \ell_{ik}d_k .$$

The result is an upper triangular system $Ux = y$, solved by **back substitution**:

$$x_i = \frac{1}{U_{ii}}\left( y_i - \sum_{j>i} U_{ij}x_j \right), \qquad i = n-1, \ldots, 0 .$$

The multipliers are worth keeping. Recording them in a unit lower triangular matrix
$L$ with $L_{ik} = \ell_{ik}$ gives the **LU factorisation** $G = LU$ when no row
swaps occur, and $PG = LU$ when they do, with $P$ a permutation matrix.

### 2.4 Partial pivoting

At step $k$, rather than using $G_{kk}$ as the pivot, choose the row $r \ge k$ with
the largest $|G_{rk}|$ and swap rows $k$ and $r$. Two benefits:

- **Division by zero is avoided** whenever the matrix is nonsingular, because a
  nonsingular matrix must have a nonzero entry in the remaining column.
- **Growth of round-off is limited.** The multipliers satisfy $|\ell_{ik}| \le 1$,
  so the elimination step does not amplify the existing entries.

Partial pivoting does not make elimination stable in every conceivable case —
Wilkinson matrices show that growth factors can still be large — but it is the
default in practice and the failure cases are exotic. The full-pivoting variant
that also permutes columns costs $O(n^{3})$ extra comparisons for a bound on the
growth factor that is not worth it.

### 2.5 Cost

At step $k$ there are $n-k-1$ rows to update and $n-k$ entries per row, giving
$(n-k-1)(n-k)$ multiply-adds. Summing, the elimination cost is

$$\sum_{k=0}^{n-2}(n-k-1)(n-k) = \frac{n^{3}}{3} - \frac{n}{3} \sim \frac{n^{3}}{3}
\ \text{multiply-adds},$$

and back substitution costs $n(n+1)/2 \approx n^{2}/2$ more. The dominant term is
cubic; the numbers in Section 5 confirm the ratio of $8$ per doubling of $n$.

### 2.6 Determinant and singular matrices

Row swaps change the sign of the determinant, elimination steps (adding a multiple
of one row to another) do not; the product of the pivots is therefore
$\pm\det G$. Consequently $\det G = 0$ exactly when some pivot is zero at every
possible row choice — that is, when the matrix is singular. Section 5 checks $4.0$
against a cofactor computation for the tomography matrix, and $0$ for the
rank-deficient kernel of [01-07-04](./04-rank-and-nullspace.md).

## 3. Step-by-step derivations

### 3.1 The elimination, traced

Start from

$$\left[\begin{array}{ccc|c} 2 & 1 & 0 & 0.080 \\ 1 & 2 & 1 & 0.110 \\ 0 & 1 & 2 & 0.180 \end{array}\right].$$

**Step 1.** No swap is needed: $|2| \ge |1|$. The multiplier for row 2 is
$1/2 = 0.5$, so subtract $0.5$ times row 1 from row 2. The multiplier for row 3 is
$0/2 = 0$, so nothing changes there:

$$\left[\begin{array}{ccc|c} 2 & 1 & 0 & 0.080 \\ 0 & 1.5 & 1 & 0.070 \\ 0 & 1 & 2 & 0.180 \end{array}\right].$$

**Step 2.** The multiplier is $1/1.5 = 0.6667$:

$$\left[\begin{array}{ccc|c} 2 & 1 & 0 & 0.080 \\ 0 & 1.5 & 1 & 0.070 \\ 0 & 0
& 1.3333 & 0.1333 \end{array}\right].$$

**Back substitution.** From the last row $m_3 = 0.133333/1.333333 = 0.100000$.
Then $m_2 = (0.070000 - 0.100000)/1.500000 = -0.020000$, and
$m_1 = (0.080000 - (-0.020000))/2.000000 = 0.050000$. The recovered model is
$(0.05, -0.02, 0.10)$ $\mathrm{s/km}$ — exactly the model used to generate the data,
with a maximum error of $0$.

The pivots $2$, $1.5$, $4/3$ multiply to $4$, which is $\det G$ by the cofactor
expansion $2(4-1) - 1(2-0) = 4$. A determinant of $4$ means the unit cube of model
perturbations maps to a parallelepiped of volume $4$ in the data space: a healthy,
non-degenerate geometry, and exactly the determinant scale that made
[01-07-05](./05-determinants-inverses.md) Section 6 warn that a determinant is not
a conditioning measure.

### 3.2 The factors, and why they are worth having

The multipliers $0.5$ and $0.6667$ fill the sub-diagonal of $L$:

$$L = \begin{bmatrix} 1 & 0 & 0 \\ 0.5 & 1 & 0 \\ 0 & 0.6667 & 1 \end{bmatrix},
\qquad U = \begin{bmatrix} 2 & 1 & 0 \\ 0 & 1.5 & 1 \\ 0 & 0 & 1.3333 \end{bmatrix}.$$

Here $P = I$ because no swap occurred, and the check $\max|PA - LU|$ returns
$0.000\times10^{0}$. The point of the factorisation is reuse: solving for a second
data vector costs one forward substitution with $L$ and one back substitution with
$U$, that is $n^{2}$ operations, instead of a fresh $n^{3}/3$. When a survey
accumulates data in batches — or when a nonlinear inversion needs a linearised solve
at every iteration — factoring once and reusing is the difference between a
feasible computation and an infeasible one. The same reuse argument is what makes
Newton-like methods affordable in
[01-07-10](./10-matrix-calculus.md).

### 3.3 Where pivoting is mandatory

Take

$$A = \begin{bmatrix} 0 & 2 \\ 1 & 3 \end{bmatrix}, \qquad b = \begin{bmatrix} 4 \\ 4 \end{bmatrix},$$

with exact solution $x = (-2, 2)$: the first equation gives $2x_2 = 4$, so
$x_2 = 2$; the second gives $x_1 + 6 = 4$, so $x_1 = -2$.

The unpivoted algorithm looks at $A_{00} = 0$ and has nothing to divide by. It
fails with a division by zero on step 1 — reported by the demonstration as
"pivot is exactly zero". Swap the rows first and elimination proceeds normally to
give $(-2.0, 2.0)$, which reproduces $b$ when multiplied by $A$.

The physics in this example was never singular — a rotation of the two equations
cannot change what they say. What failed is the *ordering*. That is the general
lesson: many failures of a numerical method are failures of presentation, and
pivoting is the systematic cure for this particular class.

### 3.4 Cost, counted rather than estimated

| $n$ | multiply-adds | ratio to half of $n$ |
|---|---|---|
| 8 | 204 | — |
| 16 | 1 496 | 7.3333 |
| 32 | 11 440 | 7.6471 |
| 64 | 89 440 | 7.8182 |
| 128 | 707 264 | 7.9077 |

The ratios approach $8$ per doubling, which is the signature of cubic growth
($2^{3} = 8$). More precisely, $n^{3}/3 + n^{2}/2$ at $n = 128$ is
$(2.097\times10^{6})/3 + 8256 = 707\,264$, matching the table. Reductions of
geophysical software to sparsity are not cosmetic; they change an $n^{3}$ cost into
an $nnz$-proportional cost, and for a $128^{2}$-node grid ($n$ of order $10^{4}$)
that is the difference between one second and one month.

### 3.5 A small residual with a wrong answer

Consider two rays traversing two cells, with path lengths that differ by
$\delta$ km:

$$G = \begin{bmatrix} 1 & 1 \\ 1 & 1+\delta \end{bmatrix}, \qquad
m_{\text{true}} = \begin{bmatrix} 0.05 \\ -0.02 \end{bmatrix} \ \mathrm{s/km}.$$

Perturb the second travel time by 1 % of its own value and solve. The results:

| $\delta$ (km) | $\|Gm - d\|$ (s) | model error ($\mathrm{s/km}$) |
|---|---|---|
| $10^{-1}$ | $3.47\times10^{-18}$ | 0.0028 |
| $10^{-2}$ | $3.47\times10^{-18}$ | 0.0298 |
| $10^{-3}$ | $6.94\times10^{-18}$ | 0.2998 |
| $10^{-4}$ | $1.98\times10^{-16}$ | 2.9998 |

The residual is at the round-off floor in every row — the solver has done its
arithmetic correctly — while the model error grows by a factor of ten for every
factor of ten by which the geometry becomes more nearly degenerate. **A small
residual certifies that the equations you wrote were solved; it says nothing about
whether the model you obtained resembles the Earth.** Quantifying the gap is the
subject of [01-07-05](./05-determinants-inverses.md), and the mechanism is the
singular value structure of [01-07-08](./08-svd.md).

## 4. Physical interpretation

**Elimination is a systematic way of combining measurements to cancel parameters.**
The multiplier $\ell_{21} = 0.5$ in Section 3.1 means "form the new equation
(row 2) − 0.5 × (row 1)", an equation that no longer involves $m_1$. Ray 2's path
through cell 1 is half of ray 1's, so subtracting half of ray 1's datum removes
cell 1 from ray 2's equation. Every elimination step has this reading: it is a
linear combination of measurements chosen to null one parameter. In continuous
problems the same idea appears as back-projection, and in inversion as the
preconditioner of a Krylov solver.

**Pivoting is choosing which measurement to trust as the reference.** Taking the
largest available coefficient corresponds to using the measurement with the
strongest influence on the remaining unknown, which is also the measurement least
sensitive to round-off in the others. Sorting the data by influence before
combining them is a design principle, not a numerical trick.

**The cost is the reason structure matters.** $n^{3}$ for a dense matrix, $5N$ for a
sparse Laplacian with $N$ unknowns ([01-07-09](./09-sparse-matrices.md)):
the gap at $N = 10^{6}$ is between $3\times10^{17}$ and $5\times10^{6}$ operations.
No algorithmic cleverness closes a gap of eleven orders of magnitude; only changing
which algorithm you consider possible does.

**The LU factors are the inverse, compressed.** Solving with $L$ and $U$ is what
"multiplying by $G^{-1}$" means in practice. Nobody forms $G^{-1}$ numerically, for
the reasons in [01-07-05](./05-determinants-inverses.md): the factors are cheaper,
more stable, and reusable.

## 5. Python demonstration

The companion script is
[`code/elimination_lu_demo.py`](./code/elimination_lu_demo.py), with seven
sections: the physical system, forward elimination and back substitution, the
determinant from the pivots, $LU$ and the $PA = LU$ check, why pivoting is
required, cost counting, and the small-residual trap.

The quantified outputs:

| Section | Observed | Interpretation |
|---|---|---|
| 2, solution | $(0.05, -0.02, 0.1)$ $\mathrm{s/km}$, max error $0.0$ | elimination recovers the model exactly here |
| 2, multipliers | $+0.5000$, $+0.0000$, $+0.6667$ | each is a measurement combination that cancels a parameter |
| 3, determinant | product of pivots $4.000000$, cofactor $4.000000$ | a zero pivot *is* a zero determinant |
| 4, $LU$ | $P = I$, $\max\|PA - LU\| = 0.000\times10^{0}$ | the factorisation is exact for this input |
| 4, reuse | solution via $L$ and $U$ matches to $0.000\times10^{0}$ | factor once, solve many |
| 5, pivoting | no-pivot fails with a zero pivot; pivoted gives $(-2.0, 2.0)$ and $A x = (4.0, 4.0)$ | the failure was ordering, not physics |
| 6, cost | 204, 1 496, 11 440, 89 440, 707 264 for $n = 8 \ldots 128$ | ratios $7.33 \to 7.91$: cubic growth |
| 7, residual trap | residual $\sim10^{-18}$ with model error $0.0028 \to 2.9998$ | consistency is not correctness |

> **Breaking exercise.** In Section 1 change the model to
> $m = (0.05, -0.02, 0.10)$ $\mathrm{s/km}$ but move the third ray so that its path
> lengths become $(1, 1, 0)$ instead of $(0, 1, 2)$. Predict the rank of the new
> $G$ before computing anything (the third row is now a combination of which
> others?), then run the script and see how the elimination behaves. A singular
> system in floating point does not always announce itself with an exact zero
> pivot; you may get a very small one and a very large solution.

## 6. Exercises

Full set and worked solutions:
[`exercises/03-systems-and-elimination-exercises.md`](./exercises/03-systems-and-elimination-exercises.md)
and
[`exercises/03-systems-and-elimination-solutions.md`](./exercises/03-systems-and-elimination-solutions.md).
Four to start with:

**★1.** Solve by Gaussian elimination with partial pivoting, showing the
augmented matrix at each step:
$2x + y = 5$, $x + 3y = 10$. State the multipliers, the pivots and the
determinant.

**★2.** For the tomography system of Section 1, delete the third ray and solve the
resulting $2 \times 2$ system for the first two cells. Then say, in one sentence,
what the third ray contributed.

**★★3.** Factorise
$A = \begin{bmatrix} 0 & 1 & 2 \\ 1 & 2 & 0 \\ 3 & 1 & 1\end{bmatrix}$ as $PA = LU$
with partial pivoting, and verify the factorisation numerically. Report the
permutation, the multipliers, and $\det A$.

**★★4.** The matrix
$A = \begin{bmatrix} \epsilon & 1 \\ 1 & 1 \end{bmatrix}$ with $\epsilon = 10^{-8}$.
(a) Solve $Ax = (1, 2)^\mathsf{T}$ exactly by hand, keeping the terms in
$\epsilon$. (b) Solve the same system by unpivoted elimination in floating point
(i.e. compute the multiplier $1/\epsilon$ and proceed) and compare. (c) Redo it with
partial pivoting and compare again. (d) Explain the difference in terms of the
multiplier magnitude.

**★★★5.** A survey accumulates data in three batches, each giving a $1000 \times
1000$ system with the *same* kernel $G$ but different right-hand sides. Count the
multiply-adds for (a) three separate eliminations, and (b) one $LU$ factorisation
plus three pairs of triangular solves. Report the ratio and the $n$ at which the
saving exceeds a factor of three.

**★★★6.** Construct a $3\times3$ system whose unpivoted elimination succeeds in
exact arithmetic but produces a solution with a relative error above $10^{-3}$ in
double precision, while partial pivoting gives a relative error below
$10^{-12}$. Report the matrix you chose, both solutions, both errors, and the
multipliers in each case. Then explain, in terms of the growth factor, why the
example works.

## 7. Common mistakes

1. **Dividing by a zero pivot and blaming the matrix.** Section 3.3 shows a
   perfectly invertible system that the unpivoted algorithm cannot start. Check the
   pivot, not the physics.
2. **Concluding that a solve is accurate because the residual is small.** Section
   3.5 shows residuals at $10^{-18}$ with model errors growing to $3$
   $\mathrm{s/km}$.
3. **Forming $G^{-1}$ to solve $Gm = d$.** It costs $n^{3}$ extra operations,
   destroys sparsity, and produces a solution no more accurate than solving with
   the factors.
4. **Refactoring for every right-hand side.** One factorisation, many triangular
   solves, is the whole point of $LU$.
5. **Believing pivoting makes elimination always stable.** It bounds the
   multipliers, not the solution error; the conditioning of $G$ still governs the
   latter, as [01-07-05](./05-determinants-inverses.md) shows.
6. **Forgetting that the sign of the determinant changes with each swap.** The
   product of pivots must be multiplied by $(-1)^{\#\text{swaps}}$.
7. **Using dense elimination on a sparse system.** The factors are less sparse than
   the matrix, often much less ([01-07-09](./09-sparse-matrices.md) Section 4).
8. **Assuming a square system has a unique solution.** Square and nonsingular are
   different statements; the differentiation matrix of
   [01-07-02](./02-matrices-and-operations.md) is square and singular.

## 8. Real-world applications

- **Small tomography problems.** A handful of rays through a handful of cells, as in
  Section 1, is solved exactly by elimination. The same $LU$ machinery solves
  layered-medium problems where each layer is a block.
- **Travel-time inversion.** A linearised inversion solves $G^\mathsf{T}G\Delta m =
  G^\mathsf{T}\Delta d$ at every iteration; recognising that $G^\mathsf{T}G$ can be
  factored once when the ray geometry is frozen is a standard optimisation.
  See [18-inverse-problems](../../18-inverse-problems/README.md).
- **Implicit time stepping.** Backward-Euler and Crank–Nicolson schemes for the
  diffusion equation require the solution of a linear system at every time step
  with a *fixed* matrix, so one factorisation serves all of them; in one dimension
  the matrix is tridiagonal and the Thomas algorithm applies
  ([01-07-09](./09-sparse-matrices.md) Section 5).
- **Geodetic network adjustment.** Least-squares adjustment of a survey network
  reduces to a normal-equation system, factored once and solved for many
  observation sets.
- **Spline interpolation and ray tracing.** Cubic splines and two-point ray tracing
  both require banded solves with fixed structure; the cost counting of Section 3.4
  is what decides whether a dense or banded algorithm is used.
- **Assessment of a solver's output.** The residual-versus-error distinction of
  Section 3.5 is the standard sanity check on any inversion result, and *always*
  computing the residual is a professional habit rather than an optional extra.

## 9. Further reading

- **Golub, G. H., & Van Loan, C. F. *Matrix Computations.* Johns Hopkins
  University Press.** Chapter 3 is the definitive account of Gaussian elimination,
  pivoting, growth factors and the error analysis. Level: advanced.
- **Trefethen, L. N., & Bau, D. *Numerical Linear Algebra.* SIAM.** Lectures 20–22
  give the stability argument in the least painful form available. Level:
  intermediate to advanced.
- **Strang, G. *Introduction to Linear Algebra.* Wellesley–Cambridge Press.** The
  row and column pictures, elimination, and $LU$ with a strong geometric bias.
  Level: beginner to intermediate.
- **Higham, N. J. *Accuracy and Stability of Numerical Algorithms.* SIAM.** The
  reference for growth factors and for the cases in which pivoting is not enough.
  Level: advanced.
- **Menke, W. *Geophysical Data Analysis: Discrete Inverse Theory.* Academic
  Press.** The same elimination machinery applied to inverse problems, with the
  residual-versus-error discussion. Level: intermediate.
- **Press, W. H., Teukolsky, S. A., Vetterling, W. T., & Flannery, B. P. *Numerical
  Recipes* (3rd ed.). Cambridge University Press.** Practical notes on when to use
  $LU$ and when to use something structured. Level: intermediate.

> Note on citations: bibliographic details above are given so that you can
> locate the works. This repository does not host or reproduce copyrighted text,
> and you should confirm editions and current availability through your library
> before citing them yourself.

## 10. Self-assessment checklist

- [ ] I can write a linear system in both the row and the column picture and
      explain what each answers.
- [ ] I can perform elimination with partial pivoting on a $3 \times 3$ system by
      hand without error.
- [ ] I can state why each elementary row operation preserves the solution set, and
      give the matrix it corresponds to.
- [ ] I can construct a system in which unpivoted elimination fails on a zero
      pivot, and explain why pivoting repairs it.
- [ ] I can produce $PA = LU$ from scratch and verify it numerically.
- [ ] I can count the multiply-adds of elimination and show the ratio approaching
      eight per doubling of $n$.
- [ ] I can obtain the determinant from the pivots, including the sign convention.
- [ ] I can give an example in which a small residual accompanies a large model
      error, and explain the mechanism.

## 11. Related lessons

- [01-07-02 Matrices, Matrix Multiplication and Linear Maps](./02-matrices-and-operations.md) —
  what the matrix means before it is solved.
- [01-07-04 Rank, Null Space and Solvability](./04-rank-and-nullspace.md) — what
  happens when elimination finds a zero pivot in every permutation.
- [01-07-05 Determinants, Inverses and Matrix Conditioning](./05-determinants-inverses.md) —
  why a solvable system can still be unsolvable in practice.
- [01-07-07 Orthogonality, Projections and Least Squares](./07-orthogonality.md) —
  the overdetermined case, where no exact solution exists and elimination is
  replaced by projection.
- [01-07-08 Singular Value Decomposition and Rank Truncation](./08-svd.md) — the
  diagnosis of the near-singular cases that pivoting cannot cure.
- [01-07-09 Sparse Matrices and Structured Systems](./09-sparse-matrices.md) — the
  algorithms that replace elimination when $n$ is large and the matrix is mostly
  empty.
- [01-01-04 Floating-Point Representation, Round-Off and Catastrophic Cancellation](../01-arithmetic/04-floating-point.md) —
  the arithmetic behind the growth-factor discussion.
