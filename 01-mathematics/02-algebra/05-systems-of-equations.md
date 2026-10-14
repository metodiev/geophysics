---
id: 01-02-05
title: "Linear and Nonlinear Systems of Equations"
level: intermediate
prereqs: ["01-02-04"]
estimated_minutes: 75
tags: [linear-systems, gaussian-elimination, newton-method, underdetermined]
---

# Linear and Nonlinear Systems of Equations

## Learning objectives

By the end of this lesson you will be able to:

1. **Classify** a system of equations as linear or nonlinear, and as exactly
   determined, over-determined or under-determined.
2. **Solve** a small linear system by substitution and by Gaussian elimination with
   partial pivoting, and check the answer with the residual.
3. **Explain** why a small residual does not imply a small error, using the
   condition number.
4. **Solve** a nonlinear system by Newton's method, and say what the Jacobian is
   and how to write the update.
5. **Recognise** under-determination and non-uniqueness in a geophysical inverse
   problem, and describe what additional information would remove it.

## Prerequisites

[01-02-04 Polynomials, Roots and Asymptotic Behaviour](./04-polynomials-roots.md)
for root finding and for the conditioning of roots, and
[01-02-01 Algebraic Manipulation and Solving Equations](./01-algebraic-manipulation.md)
Section 3.5 for simple substitution. The lesson is self-contained on linear
algebra, but readers who have met matrices will move faster.

## 1. Intuition: one equation is the exception, not the rule

A single measurement rarely determines a single unknown. A gravity profile gives
many readings from several bodies; a refraction spread gives several arrival times
for a two-layer model; a well log gives a depth–velocity pair at every sample. The
normal situation in geophysics is a **system**: several equations, several
unknowns, all coupled.

Two things then matter, and they are independent:

1. **Is the system solvable, and is the answer unique?** This is a question about
   the *geometry* of the equations. It has nothing to do with the computer.
2. **How accurately can it be solved?** This is a question about *conditioning* —
   how much the answer amplifies errors in the data — and about the algorithm.

The lesson treats both, for linear systems (Sections 3–4) and nonlinear ones
(Section 5).

## 2. Definitions

**Linear system.** $n$ equations in $m$ unknowns that can be written

$$a_{11}x_1 + \cdots + a_{1m}x_m = b_1, \quad \dots, \quad
a_{n1}x_1 + \cdots + a_{nm}x_m = b_n,$$

i.e. $A\mathbf{x} = \mathbf{b}$. **Linear** means: no products of unknowns, no
functions of unknowns, no unknown in a denominator. The matrix $A$ is the
**forward operator**: it maps a model $\mathbf{x}$ to data $\mathbf{b}$.

**Nonlinear system.** Anything else — for example

$$g_i = \frac{G m_i h_i}{\left(x_i^{2} + h_i^{2}\right)^{3/2}},$$

where the unknowns multiply and appear inside powers. Nonlinear systems can have
**several solutions**, and the one you find depends on where you start.

**Classification by count.**

| case | relationship | typical meaning |
|---|---|---|
| $n = m$ | exactly determined | one candidate solution; may not exist or may not be unique |
| $n > m$ | over-determined | no exact solution in general; fit by least squares |
| $n < m$ | under-determined | infinitely many exact solutions; needs extra information |

Real geophysics is usually **over-determined** (more data than parameters, so the
fit can be tested) or **under-determined** (more parameters than data, so
regularisation is needed) — and almost never exactly determined, which is why
"exactly determined" appears here mainly as a teaching case.

## 3. Solving linear systems

### 3.1 Two unknowns: substitution

Solve one equation for one unknown, substitute into the other, check. This is the
method of
[01-02-01](./01-algebraic-manipulation.md), and it is the fastest route for
$2\times2$ and $3\times3$ systems done by hand.

### 3.2 Gaussian elimination with partial pivoting

For larger systems, and for code, elimination is the standard method:

1. For each column, choose the row with the largest absolute value in that column
   (**partial pivoting**) and swap it into the pivot position.
2. Eliminate the entries below the pivot.
3. Back-substitute.

Partial pivoting is not cosmetic: it keeps the elimination multipliers small and is
what makes the algorithm **backward stable** — the computed solution is the exact
solution of a system whose coefficients differ from the given ones by a relative
amount of order $u$. The demonstration solves

$$A = \begin{pmatrix} 4 & -1 & 0 \\ -1 & 4 & -1 \\ 0 & -1 & 3 \end{pmatrix},
\qquad \mathbf{b} = (15, 10, 10),$$

obtaining $\mathbf{x} = (5, 5, 5)$ with a maximum residual of exactly $0.0$ for
this well-conditioned, exactly representable problem.

### 3.3 A real forward operator

A worked inverse problem makes the structure concrete. Two point masses sit at
horizontal positions $p_j$ and depths $h_j$; two stations read the vertical
attraction. The kernel is

$$K_{ij} = \frac{G\,h_j}{\left[(x_i - p_j)^{2} + h_j^{2}\right]^{3/2}},$$

so $\mathbf{b} = K\mathbf{m}$ with $\mathbf{m}$ the two masses, and the data are
**linear in the masses once the geometry is fixed**. With
$p = (0, 400)$ m, $h = (400, 900)$ m and stations at $x = (0, 400)$ m:

| | body 1 | body 2 |
|---|---|---|
| station $x = 0$ | $4.1712\times10^{-16}$ | $6.2874\times10^{-17}$ |
| station $x = 400$ | $1.4748\times10^{-16}$ | $8.2395\times10^{-17}$ |

Synthetic data from masses $(3\times10^{11}, 8\times10^{11})$ kg are
$(1.754367\times10^{-4}, 1.101588\times10^{-4})$ m/s², and solving the system
recovers both masses exactly, with a maximum residual of $1.4\times10^{-20}$,
$\det K = 2.5097\times10^{-32}$ and $\kappa_\infty(K) = 10.8$. A condition number
of 11 means the problem is mild: about one digit is lost. **The geometry keeps the
two responses distinguishable**, and that is a design statement, not an accident.

## 4. Existence, uniqueness, conditioning

### 4.1 Existence and uniqueness

For a square system, the following are equivalent: $A$ is invertible; $\det A \ne
0$; the columns of $A$ are linearly independent; there is exactly one solution for
every $\mathbf{b}$. When $\det A = 0$ the equations are **dependent** or
**inconsistent**, and either infinitely many solutions or none exist.

Geometric picture: each linear equation is a line (in 2-D) or a plane (in 3-D).
Two lines meet in a point unless they are parallel (no solution) or identical
(infinitely many). In an inverse problem, near-parallel lines are the norm rather
than the exception — and near-parallel is the dangerous case.

### 4.2 Nearly dependent rows

The demonstration solves

$$\begin{pmatrix} 1 & 1+\epsilon \\ 1 & 1-\epsilon \end{pmatrix}\mathbf{x}
= \mathbf{b}, \qquad \epsilon = 10^{-8},$$

| right-hand side | solution |
|---|---|
| $(2,\ 2)$ | $(2.0000,\ -0.0000)$ |
| $(2 + 10^{-8},\ 2)$ | $(1.5000,\ 0.5000)$ |

A relative change of $5\times10^{-9}$ in one datum moves the solution by $0.5$ — an
amplification of about $10^{8}$. Nothing is wrong with the elimination: the
*problem* is ill-conditioned, because the two equations contain nearly the same
information. Ill-conditioning is a property of the equations, and no algorithm can
remove it — the same distinction as in
[01-01-05](../01-arithmetic/05-error-and-conditioning.md), now applied to systems.

### 4.3 Residual versus error

For a computed solution $\hat{\mathbf{x}}$, the **residual** is
$\mathbf{r} = \mathbf{b} - A\hat{\mathbf{x}}$. The bound

$$\frac{\|\Delta \mathbf{x}\|}{\|\mathbf{x}\|} \le \kappa(A)\,
\frac{\|\mathbf{r}\|}{\|\mathbf{b}\|}$$

(up to terms of second order) is why a tiny residual can coexist with a large
error: the missing factor is $\kappa(A)$. Check the residual **and** estimate the
conditioning; either alone is misleading.

## 5. Nonlinear systems

### 5.1 Newton's method for systems

For a vector equation $\mathbf{f}(\mathbf{x}) = \mathbf{0}$, expand to first order
about the current iterate:

$$\mathbf{f}(\mathbf{x} + \boldsymbol{\delta}) \approx
\mathbf{f}(\mathbf{x}) + J(\mathbf{x})\,\boldsymbol{\delta},$$

where $J$ is the **Jacobian** matrix with entries $J_{ij} = \partial f_i/\partial
x_j$. Setting the linearised expression to zero gives the update rule

$$J(\mathbf{x}_k)\,\boldsymbol{\delta}_k = -\mathbf{f}(\mathbf{x}_k), \qquad
\mathbf{x}_{k+1} = \mathbf{x}_k + \boldsymbol{\delta}_k.$$

So each Newton step is a **linear solve** — the machinery of Section 3, applied
repeatedly. Convergence is quadratic near a solution with a nonsingular Jacobian.

### 5.2 Worked example: mass and depth of one body

Two stations observe a point mass at a fixed horizontal position; the unknowns are
its mass $m$ and depth $h$. The demonstration starts from a guess that is wrong by
factors of 5 in mass and 2.3 in depth and converges in seven iterations:

| iteration | max $|$residual$|$ |
|---|---|
| $0$ | $1.060\times10^{-4}$ |
| $2$ | $2.730\times10^{-5}$ |
| $4$ | $8.027\times10^{-8}$ |
| $6$ | $2.473\times10^{-17}$ |

recovering $m = 5.000000\times10^{11}$ kg and $h = 350.000000$ m exactly. The
residual falls by roughly two orders of magnitude per step — quadratic
convergence, visible in the numbers.

### 5.3 Scaling: a practical necessity, not a refinement

The unknowns above were parameterised as $\ln(m/m_0)$ and $\ln(h/h_0)$, not as raw
mass and depth. Two reasons:

- **Scale.** A step in a mass unknown of order $10^{11}$ and a step in a depth
  unknown of order $10^{2}$ cannot be compared in a Jacobian that mixes them; the
  linear solve then sees a badly scaled matrix.
- **Physical constraints.** A logarithm can never produce a negative mass or a
  negative depth, so the iteration cannot wander into unphysical territory where
  the model is meaningless.

Both are standard practice: scale the unknowns so that a unit step is comparable
in each, and parameterise so that the admissible region is automatic. A Jacobian
with entries differing by nine orders of magnitude is a well-known cause of a
Newton iteration that fails for reasons that have nothing to do with the physics.

### 5.4 Non-uniqueness in nonlinear systems

Nonlinear systems may have **several solutions**, and the residual cannot
distinguish between them. The demonstration makes this concrete: with three
unknowns (mass, position, depth) and only two stations, the ratio of the two
readings fixes a one-parameter family of exact solutions:

| assumed position (m) | fitted mass (kg) | fitted depth (m) | max residual |
|---|---|---|---|
| $0$ | $5.000000\times10^{11}$ | $350.0000$ | $2.7\times10^{-20}$ |
| $-60$ | $8.919348\times10^{11}$ | $640.2343$ | $1.4\times10^{-20}$ |
| $-150$ | $1.539019\times10^{12}$ | $909.6703$ | $2.7\times10^{-20}$ |
| $-250$ | $2.280006\times10^{12}$ | $1128.0514$ | $0.0$ |

Every model reproduces the two observations to round-off, yet the models differ in
position by 250 m and in mass by a factor of 4.6. The trade-off is real: moving a
mass deeper requires making it heavier to produce the same anomaly (this is the
classical depth–mass ambiguity of potential-field interpretation). Two
observations cannot fix three unknowns, and the residual is the wrong tool for
detecting it — you must count equations and unknowns, or examine the Jacobian.

**Note the contrast with Section 4.2.** In the linear case, ill-conditioning shows
up as *sensitivity*: a small data change moves the answer. In the nonlinear case,
under-determination shows up as *multiplicity*: different models fit equally well.
Both are reasons to report uncertainty or a family of models rather than a single
number.

## 6. Worked derivations

### 6.1 Why the Jacobian must be recomputed, and when Newton fails

The derivation of the update assumes $J$ is evaluated at the current point. If $J$
is frozen at $\mathbf{x}_0$, the method becomes a fixed linearisation (a quasi-
Newton or modified-Newton scheme): convergence degrades from quadratic to linear,
but each step is cheaper because no new Jacobian is needed. Production codes
choose between the two on cost grounds.

Newton fails when $J$ is singular at the iterate — which happens exactly when the
two curves of the geometric picture become tangent, i.e. when the parameters are
locally degenerate. The remedy is the same as in
[01-02-04](./04-polynomials-roots.md): reparametrise, add a constraint, or accept
that the data do not determine both parameters and report a trade-off curve.

### 6.2 The closed-form family behind the non-uniqueness table

For a point mass at position $p$ and depth $h$, the two readings are $g_1$ at
$x_1$ and $g_2$ at $x_2$. Their **ratio** is

$$\frac{g_1}{g_2} = \left[
\frac{(x_2-p)^{2}+h^{2}}{(x_1-p)^{2}+h^{2}}\right]^{3/2}
\;\Longrightarrow\;
r \equiv \left(\frac{g_1}{g_2}\right)^{2/3}
= \frac{(x_2-p)^{2}+h^{2}}{(x_1-p)^{2}+h^{2}}.$$

Solving for $h^{2}$ given a *chosen* $p$:

$$h^{2} = \frac{(x_2-p)^{2} - r\,(x_1-p)^{2}}{r - 1},$$

and then the mass follows from the amplitude, $m = g_1[(x_1-p)^{2}+h^{2}]^{3/2}
/(Gh)$. This is how the table in Section 5.4 was produced, without any iteration:
the ratio determines a curve in parameter space, and each point on the curve is a
model that fits. Note also the constraint $h^{2} > 0$, which limits how far the
position can be moved before the family runs out (the demonstration's positions are
limited to $p \lesssim 25$ m for the given data).

### 6.3 Why an over-determined system has no exact solution

Three stations and two unknowns give three equations. Unless the data are
noiseless and the model exactly right, no pair $(m, h)$ satisfies all three, so
$\mathbf{f} = \mathbf{0}$ has no solution. The standard reformulation is **least
squares**: minimise $\|\mathbf{f}\|^{2}$, whose stationarity condition is
$J^{\mathsf{T}}\mathbf{f} = \mathbf{0}$ — the normal equations of Gauss–Newton.
This is the bridge from this lesson to
[01-14 Optimization](../14-optimization/README.md): inversion is root finding with
more equations than unknowns, and the Jacobian's conditioning decides what can be
resolved.

### 6.4 Over-determined, but still not unique

Over-determination improves conditioning but does not guarantee uniqueness in a
nonlinear problem. A classic geophysical example is the two-layer refraction
problem: many picks determine apparent velocities well, yet a trade-off between
layer thickness and velocity contrast can persist. The test is not "do I have more
data than parameters?" but "does the Jacobian have full rank at the solution?" —
and that must be checked numerically.

## 7. Python demonstration

```bash
python3 code/systems_demo.py
```

`code/systems_demo.py` uses only the standard library. It contains a Gaussian
elimination routine with partial pivoting, a residual checker, and a Newton
solver for systems with a forward-difference Jacobian and a backtracking line
search. It covers: a two-masses linear inversion; a $3\times3$ system with a
residual check; a nearly singular system and its amplification; fixed-point
iteration versus Newton; the nonlinear (mass, depth) inversion with log-scaled
unknowns; and the under-determined three-parameter problem.

Observed output worth dwelling on:

```text
  station x =     0 m: 4.1712e-16  6.2874e-17
station x =   400 m: 1.4748e-16  8.2395e-17
  mass 1: true 3.0000e+11 kg, recovered 3.000000e+11 kg
  mass 2: true 8.0000e+11 kg, recovered 8.000000e+11 kg
max residual: 1.355e-20
det(A) = 2.5097e-32, cond_inf(A) = 10.799
```

```text
change in solution: 0.5000 for a relative
data change of 5.0e-09  ->  amplification ~1.000e+08
```

```text
 assumed position      mass (kg)    depth (m)   max |residual|
                0   5.000000e+11     350.0000        2.711e-20
             -250   2.280006e+12    1128.0514        0.000e+00
```

| Observation | Consequence in geophysics |
|---|---|
| both masses recovered to full precision | a well-posed geometry inverts cleanly; check $\kappa$, not just success |
| a $5\times10^{-9}$ data change moves the answer by 0.5 | near-parallel equations make an inversion meaningless without uncertainty |
| Newton converges from a 5× wrong guess in 7 steps | log-scaled parameters make a nonlinear inversion robust |
| three models, one data set, all residuals zero | under-determination is invisible to the residual; count unknowns |

## 8. Exercises

Ten graded exercises with worked solutions are in
[`exercises/05-systems-of-equations-exercises.md`](./exercises/05-systems-of-equations-exercises.md)
and
[`exercises/05-systems-of-equations-solutions.md`](./exercises/05-systems-of-equations-solutions.md).

**★1.** Solve by substitution and check: $2x + y = 7$, $x - y = 2$.

**★★2.** For the nearly dependent system of Section 4.2 with $\epsilon = 10^{-6}$,
compute $\det A$, the exact solution for $\mathbf{b} = (2,2)$, and the solution for
$\mathbf{b} = (2 + 10^{-6}, 2)$. Compare the amplification with the $\epsilon =
10^{-8}$ case.

**★★★3.** Design an experiment that measures how the Newton iteration count for
the two-parameter (mass, depth) inversion depends on the starting guess, and
report the size of the region of convergence around the true model. State the
method, the result and its limitations.

## 9. Common mistakes

1. **Judging a solution by its residual alone.** The residual is cheap and
   insensitive; the error is what you want and requires $\kappa$.
2. **Inverting a nearly singular system and reporting the answer to many digits.**
   If $\kappa \sim 10^{8}$, the answer has about eight fewer digits than the data.
3. **Forgetting that nonlinear systems can have several solutions.** Report the
   starting point and, where relevant, the other solutions.
4. **Using raw, unscaled unknowns in a Newton iteration.** Mixed scales wreck the
   Jacobian; parameterise logs or ratios.
5. **Assuming over-determination implies uniqueness in a nonlinear problem.** Check
   the rank of the Jacobian.
6. **Dividing by a determinant to solve a system by hand for $n > 3$.** Use
   elimination; Cramer's rule is an order of magnitude more work and less
   accurate.
7. **Treating an under-determined problem as a failure.** It is information: the
   data constrain a combination of parameters, and that combination is worth
   reporting.

## 10. Real-world applications

- **Potential-field inversion.** Mass/depth/position trade-offs are the classical
  ambiguity; modern practice reports a family of models or a Bayesian posterior.
  See [07-gravity-geodesy](../../07-gravity-geodesy/README.md).
- **Refraction and travel-time inversion.** Layer thicknesses and velocities from
  arrival times; over-determined in principle, with a persistent
  thickness–velocity trade-off.
- **Seismic tomography.** Thousands of equations, tens of thousands of unknowns:
  under-determined, regularised, and solved iteratively.
- **Geodetic strain from GNSS.** A linear system mapping site velocities to a
  strain-rate field; the conditioning depends on the geometry of the network.
- **Least-squares fitting of any model.** Linear regression is the
  exactly-determined-to-over-determined case of this lesson, with the normal
  equations as the workhorse.
- **Nonlinear parameter estimation.** Earthquake source parameters (moment,
  depth, mechanism) or a hydrologic model's parameters are estimated by
  Gauss–Newton or a variant, with all of the convergence behaviour discussed in
  Section 5.

## 11. Further reading

- **Strang, G. (2016). *Introduction to Linear Algebra* (5th ed.). Wellesley–
  Cambridge Press.** Chapters 1–2 and 7. Level: beginner to intermediate. The
  clearest introduction to elimination, singularity and the geometry of systems.
- **Trefethen, L. N., & Bau, D. (1997). *Numerical Linear Algebra*. SIAM.**
  Lectures 20–23 on Gaussian elimination, pivoting and stability. Level:
  intermediate. The standard short treatment.
- **Golub, G. H., & Van Loan, C. F. (2013). *Matrix Computations* (4th ed.).
  Johns Hopkins University Press.** Chapter 3. Level: graduate. For the error
  analysis behind the residual-versus-error bound.
- **Aster, R. C., Borchers, B., & Thurber, C. H. (2018). *Parameter Estimation
  and Inverse Problems* (2nd ed.). Academic Press.** Level: intermediate to
  advanced. The geophysical inverse-problem setting, including the linearised
  (Gauss–Newton) approach to nonlinear problems and the treatment of
  non-uniqueness.
- **Menke, W. (2012). *Geophysical Data Analysis: Discrete Inverse Theory*
  (3rd ed.). Academic Press.** Level: intermediate. The classical reference for
  over-determined, under-determined and mixed-determined systems in geophysics.

> Note on citations: bibliographic details are given so you can locate the works;
> editions vary and page numbers are deliberately omitted. This repository does not
> reproduce copyrighted text.

## 12. Related lessons

- [04 Polynomials, Roots and Asymptotic Behaviour](./04-polynomials-roots.md) —
  the scalar root-finding case that Newton for systems generalises.
- [01 Algebraic Manipulation and Solving Equations](./01-algebraic-manipulation.md)
  — substitution for small systems.
- [01-01-05 Absolute vs Relative Error, Conditioning and Stability](../01-arithmetic/05-error-and-conditioning.md)
  — the conditioning framework used in Section 4.
- [01-07 Linear Algebra](../07-linear-algebra/README.md) — the systematic theory:
  rank, factorisation, least squares.
- [01-14 Optimization](../14-optimization/README.md) — Gauss–Newton and the
  least-squares formulation of Section 6.3.
- [18-inverse-problems](../../18-inverse-problems/README.md) — regularisation and
  the professional treatment of under-determined systems.

## Self-assessment checklist

- [ ] I can classify a system by linearity and by the count of equations versus
      unknowns.
- [ ] I can solve a $3\times3$ linear system by elimination and check the residual.
- [ ] I can explain why a small residual does not imply a small error.
- [ ] I can write down Newton's method for a system, including the role of the
      Jacobian.
- [ ] I can explain what scaling does for a nonlinear iteration.
- [ ] I can describe a geophysical trade-off as a one-parameter family of fitting
      models and say what extra information would resolve it.
