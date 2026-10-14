---
id: 19-07-01
title: "Code Verification: Order-of-Accuracy and Manufactured Solutions"
level: research
prereqs: ["19-01-02", "19-02-01", "03-12-04"]
tags: [numerical-modelling, verification, code-verification, manufactured-solutions, order-of-accuracy]
---

# Code Verification: Order-of-Accuracy and Manufactured Solutions

## Learning objectives

By the end of this lesson you will be able to:

1. **Distinguish** code verification, solution verification and validation, and
   **state** for each one which question it answers and which mistake it cannot
   detect.
2. **Derive** the leading truncation term of a finite-difference operator from
   Taylor expansion and **predict**, from that term alone, the error a scheme will
   produce at a stated grid spacing.
3. **Construct** a manufactured solution for a given operator, including the
   source term and the boundary data, and **explain** why the manufactured
   solution must be smooth and why its boundary values must be imposed exactly.
4. **Measure** the observed order of accuracy from a refinement study and
   **decide**, from the measurement, whether a code is converging at its design
   rate.
5. **Explain** why a machine-precision residual is consistent with an O(1) error,
   and **demonstrate** it with a deliberately wrong source term.
6. **Report** a verification result in the form a reader can falsify: operator,
   exact solution, norm, grid sequence, observed order, and tolerance.

## Prerequisites

- [19-01-02 Truncation Error, Order of Accuracy and Convergence Rates](../01-numerical-foundations/02-convergence-and-error.md)
  — the Taylor-expansion definition of order of accuracy used throughout.
- [19-02-01 Deriving Finite-Difference Operators via Taylor Expansion](../02-finite-difference-methods/01-fd-derivation.md)
  — the stencil algebra this lesson applies.
- [03-12-04 Verification vs Validation: Benchmarks and Convergence Tests](../../03-scientific-computing/12-numerical-simulation-python/04-verification-and-validation.md)
  — the practical Python form of the same tests.

All models and data in this module are **SYNTHETIC**. The partial differential
equations below are chosen teaching problems, and every number quoted is printed
by this lesson's demonstration.

## 1. Intuition: the difference between "it ran" and "it is right"

A simulation produces numbers. Almost nothing about the numbers tells you whether
they are right: a plausible-looking wavefield can be produced by a code with a
sign error in one term, and a beautifully smooth potential field can be produced
by a code that solves the wrong equation entirely. **Verification** is the
activity that establishes what the code actually solves. It has a specific form:
you construct a problem whose answer you know *exactly*, feed it to the code, and
measure how the error shrinks as you refine.

The second half of that sentence is the part that is usually missing. A single
comparison with an exact solution tells you the error at one resolution. It
cannot separate "a correct second-order scheme on a coarse grid" from "a wrong
first-order scheme on a fine grid" — both can have an error of $10^{-3}$. What
distinguishes them is the *rate*: halve the grid spacing and a second-order
scheme's error falls by a factor of four, a first-order scheme's by two, and a
wrong code's not at all. Order of accuracy is therefore not decoration; it is the
measurement that identifies the code.

There is a trap that has caught almost every modeller once. Both common *a
posteriori* checks are blind to the errors that matter most:

- the **residual** $\lVert A u_h - f_h \rVert$ measures whether the code solved
  *its own* discrete equations. A code with a wrong coefficient solves them
  exactly, so the residual is $10^{-14}$ and the solution is wrong by $2$ per cent.
- **agreement between two codes** measures whether they share assumptions. If they
  share the wrong one, they agree to machine precision and are jointly wrong.

Only comparison with an independently derived exact solution, and the *rate* at
which the difference disappears, is evidence of correctness.

## 2. Definitions

**Code verification** answers: *does the code solve the stated equations
correctly?* The reference is an exact solution, either analytic or manufactured,
of the same equations.

**Solution verification** answers: *how large is the discretisation error at the
resolution actually used?* The exact solution is not available; the reference is
a family of numerical solutions at different resolutions
([02 Solution Verification and Discretisation Error Estimation](02-solution-verification.md)).

**Validation** answers: *are the stated equations an adequate description of the
system?* The reference is independent data, not a solution of the same equations
([03 Model Validation Against Observations](03-model-validation.md)).

The three are different activities with different evidence. Section 6 states the
asymmetry between them.

**Order of accuracy.** Let $h$ be the grid spacing and $e(h)$ a norm of the
error. The scheme is of order $p$ if

$$e(h) = C h^{p} + O(h^{p+1}), \qquad C \neq 0,$$

in the limit $h \to 0$. The requirement $C \neq 0$ matters: an error that decays
faster than every power of $h$ (a spectral method on a smooth problem) has no
finite order, and an error that stops decaying (Section 5) has none either.

**Grid convergence.** The sequence $e(h_1) > e(h_2) > \dots \to 0$ as
$h_1 > h_2 > \dots \to 0$. Convergence is a prerequisite for order: a scheme can
converge without having a clean order if the solution is not smooth enough.

## 3. Deriving the order of accuracy

### 3.1 From Taylor series to the truncation term

For a smooth $u$, expand about $x_i$:

$$u_{i+1} = u_i + h u'_i + \frac{h^{2}}{2}u''_i
+ \frac{h^{3}}{6}u'''_i + \frac{h^{4}}{24}u''''_i + \dots$$

$$u_{i-1} = u_i - h u'_i + \frac{h^{2}}{2}u''_i
- \frac{h^{3}}{6}u'''_i + \frac{h^{4}}{24}u''''_i - \dots$$

Adding eliminates every odd derivative:

$$u_{i-1} + u_{i+1} = 2u_i + h^{2}u''_i + \frac{h^{4}}{12}u''''_i + O(h^{6}).$$

Divide by $h^{2}$ and rearrange:

$$\frac{u_{i-1} - 2u_i + u_{i+1}}{h^{2}}
= u''_i + \frac{h^{2}}{12}u''''_i + O(h^{4}).$$

The discrete operator therefore represents $u''$ with a **local truncation error**
$\tau_i = \frac{h^{2}}{12}u''''_i$. That single term predicts two things: the
scheme is second order, and the size of the error at a stated $h$. Section 8 does
that prediction and compares it with the measured error.

### 3.2 From local truncation to global error

The scheme solves

$$L_h u_h = -f_h, \qquad L_h(\cdot)_i = \frac{(\cdot)_{i-1} - 2(\cdot)_i + (\cdot)_{i+1}}{h^{2}},$$

for $-u'' = f$. Substituting the exact solution, $L_h u = -f - \tau + O(h^4)$, so
the error $e = u_h - u$ satisfies

$$L_h e = \tau + O(h^{4}).$$

For a stable scheme with an $M$-matrix structure, $\lVert L_h^{-1} \rVert =
O(1)$ for the second-difference operator with Dirichlet data, so
$\lVert e \rVert = O(\lVert \tau \rVert) = O(h^{2})$. **Local truncation error of
order $h^{q}$ plus stability gives global error of order $h^{q}$** — the same
consistency-plus-stability argument as the Lax equivalence theorem
([19-01-03](../01-numerical-foundations/03-consistency-stability.md)), specialised
to a steady problem.

### 3.3 What the observed order is

Given three grids with $h_3 = h_2/r$ and $h_2 = h_1/r$, and errors $e_1, e_2, e_3$
each dominated by the same term $Ch^{p}$:

$$e_1 - e_2 = C h_2^{p}(r^{p} - 1), \qquad e_3 = C h_3^{p},$$

so that

$$p \approx \frac{\ln\left|(e_1 - e_2)/(e_2 - e_3)\right|}{\ln r}.$$

With $r = 2$ the denominator is $\ln 2 = 0.6931$. The demonstration uses $r = 2$
and reports $p$ for each consecutive pair.

## 4. Manufactured solutions

The **method of manufactured solutions** (MMS) removes the need to find a
physical problem with a closed-form answer:

1. **Choose** a smooth function $u_m(x,y,t)$ that is not a solution of anything in
   particular.
2. **Substitute** it into the operator to obtain the source term
   $f = L(u_m)$. This step is symbolic, and it is where mistakes are made.
3. **Impose** $u_m$'s values (or its derivatives) as the boundary and initial
   data, exactly.
4. **Solve** the discrete problem, and compare $u_h$ with the sampled $u_m$.
5. **Refine** and measure the order.

Three properties of $u_m$ make the study meaningful:

- **Smoothness.** $u_m$ must have as many derivatives as the truncation analysis
  needs. A manufactured solution with a kink has a truncation error that is
  $O(1)$ near the kink and the measured order degrades — correctly, because the
  solution is not smooth.
- **Non-triviality.** $u_m$ should exercise every term of the operator. If
  $\nabla^{2}u_m = 0$ the diffusion term is never tested, and a bug in it is
  invisible.
- **Exact boundary data.** The boundary values must be imposed to machine
  precision; if the boundary data come from an interpolation or a measurement,
  their error usually dominates at fine grids.

For the Laplace problem of Section 3 the manufactured solution used in the
demonstration is $u_m = \sin(\pi x)\sin(2\pi y)$, whose source is exact:

$$\nabla^{2}u_m = -(\pi^{2} + 4\pi^{2})u_m = -5\pi^{2}u_m
\quad\Longrightarrow\quad f = -5\pi^{2}u_m .$$

### 4.1 Why a manufactured solution does not test the physics

MMS verifies that the code solves the stated equations, and only that. A wrong
*equation* (forgetting self-gravity, ignoring attenuation, dropping a term from the
momentum balance) is carried into $f$ and therefore reproduced exactly by the
code; the verification passes. That is the boundary of this method, and it is the
reason Section 6 exists.

## 5. Reading a refinement study: measured evidence

The demonstration `code/code_verification_demo.py` prints the following. The
1-D problem is $-u'' = \pi^{2}\sin(\pi x)$ on $(0,1)$ with homogeneous Dirichlet
data, solved with the three-point scheme of Section 3.

| $N$ | $h$ | discrete $L^{2}$ error | observed order |
|---:|---:|---:|---:|
| 16 | 0.06250 | $2.276\times10^{-3}$ | — |
| 32 | 0.03125 | $5.682\times10^{-4}$ | 2.002 |
| 64 | 0.01562 | $1.420\times10^{-4}$ | 2.001 |
| 128 | 0.00781 | $3.550\times10^{-5}$ | 2.000 |
| 256 | 0.00391 | $8.874\times10^{-6}$ | 2.000 |
| 512 | 0.00195 | $2.219\times10^{-6}$ | 2.000 |

The 2-D manufactured solution $u_m = \sin(\pi x)\sin(2\pi y)$ gives
$5.495\times10^{-3}$, $1.367\times10^{-3}$, $3.415\times10^{-4}$ and
$8.535\times10^{-5}$ at $N = 16, 32, 64, 128$, with orders $2.007$, $2.002$,
$2.000$: the same second order in two dimensions, at $O(N^{2})$ cost per solve.

Two further measurements calibrate what the test can see.

**A first-order scheme.** Replacing the second difference by the upwind
(backward) difference of a first derivative, applied to $au' = f$ with
$u = \sin(\pi x/2)$, gives errors $1.223\times10^{-2}$,
$5.978\times10^{-3}$, $2.955\times10^{-3}$, $1.469\times10^{-3}$,
$7.326\times10^{-4}$ at $N = 32 \dots 512$ and orders $1.032$, $1.016$, $1.008$,
$1.004$. The order is $1$, as the truncation analysis predicts, and note that the
first-order error at $N = 512$, $7.3\times10^{-4}$, is *smaller* than the
second-order Poisson error at $N = 32$, $5.7\times10^{-4}$ is close to it. A table
of single error values, without the refinement sequence, cannot order two schemes.

**A wrong source term.** Scaling the 2-D source by $1.02$ — a two per cent coding
or parameter error — gives, at $N = 128$, a relative residual
$\lVert Au - f\rVert/\lVert f\rVert = 1.83\times10^{-13}$ and a relative error
$\max|u - u_m|/\max|u| = 2.02\times10^{-2}$. Refining the wrong code gives errors
$1.139\times10^{-2}$, $1.035\times10^{-2}$, $1.009\times10^{-2}$,
$1.002\times10^{-2}$ — apparent orders $0.139$, $0.037$, $0.009$, converging to
zero. **The residual is at machine precision because the code solves the wrong
equations exactly, and the error converges to the size of the wrongness, not to
zero.** A verification study detects this immediately; a residual check cannot
detect it at all.

## 6. Assumptions and regime of validity

1. **The exact solution is the truth for the equations as coded.** A wrong
   reference makes a correct code fail, or a wrong code pass. Whenever possible,
   cross-check the reference against a second independent route (here: the
   analytic sphere and the quadrature of
   [03 Model Validation](03-model-validation.md)).
2. **The grids are in the asymptotic range.** The observed order equals the design
   order only once the leading truncation term dominates. At $N = 16$ the 2-D
   order reads $2.007$ rather than $2.000$; a single pair of coarse grids can
   misreport the order badly (Section 5 of
   [02 Solution Verification](02-solution-verification.md)).
3. **The solution is smooth enough.** MMS on a smooth $u_m$ cannot verify a
   shock-capturing or discontinuity-aware term; those need their own tests.
4. **The solver error is below the discretisation error.** An iterative solver
   stopped at a loose tolerance produces an error floor that mimics a
   non-convergent code.
5. **What MMS cannot see:** the adequacy of the equations, the correctness of the
   physical constants, and the numerical behaviour of terms that the manufactured
   solution does not excite. That is what Sections 2 and 5 of this lesson, and the
   whole of [03](03-model-validation.md), are for.

## 7. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| grid spacing | $h$ | m (here dimensionless) | |
| truncation term | $\tau$ | unit of $L(u)$ | $h^{2}u''''/12$ has the same unit as $u''$ |
| error norm | $\lVert e \rVert$ | unit of $u$ | the discrete $L^{2}$ norm carries a $\sqrt{h}$ |
| order | $p$ | dimensionless | ratio of logarithms of like quantities |
| residual | $\lVert Au-f \rVert$ | unit of $f$ | always compared as a relative value |

A dimension check catches a common MMS blunder: if the manufactured source is
derived with a sign or a factor wrong, the *units* usually still match, but the
observed order collapses. Units catch scale errors; the refinement study catches
consistency errors.

## 8. Worked examples

### Example 1 — predicting the measured error from the truncation term

For $u = \sin(\pi x)$, $u'''' = \pi^{4}\sin(\pi x)$. At $N = 16$,
$h = 1/16$, the predicted error from Section 3.1 is, using $L_h \approx
-\pi^{2}$ on this mode,

$$e \approx -\frac{h^{2}\pi^{2}}{12}\sin(\pi x)
= -\frac{(0.0625)^{2}(9.8696)}{12}\sin(\pi x)
= -3.213\times10^{-3}\sin(\pi x).$$

The discrete $L^{2}$ norm of this error over the interior is
$\sqrt{\int_{0}^{1} e^{2}\,dx} = 3.213\times10^{-3}\sqrt{1/2}
= 2.272\times10^{-3}$.

The demonstration measured $2.276\times10^{-3}$: agreement to $0.2$ per cent, the
residual being the $O(h^{4})$ terms neglected. This is what a verification study
buys — a number *predicted before the run*, not merely reported after it.

### Example 2 — a wrong source, quantified

Scale the source by $1.02$: the discrete problem becomes $L_h u_h = -f-m$ with
$f_m = 1.02 f$. Since the operator is linear and $L_h u = -f$ to $O(h^{2})$,

$$u_h = \frac{f_m}{f}u = 1.02\,u,$$

so the relative error is $2$ per cent and does *not* shrink with $h$. Measured:
$2.017\times10^{-2}$, with apparent order falling to $0.009$. The residual, by
contrast, is $1.83\times10^{-13}$ because the code is exactly solving its own
(wrong) system.

### Example 3 — the upwind scheme's order

For $au' = f$ with the backward difference,
$\frac{u_i - u_{i-1}}{h} = u'_i - \frac{h}{2}u''_i + O(h^{2})$, so
$\tau = -\frac{h}{2}u''$ and the global error is $O(h)$ provided the marching is
stable. The demonstration measures orders $1.032 \to 1.004$ as $N$ goes from $32$
to $512$ — the first-order rate, approached from above as the $O(h^{2})$ term
becomes negligible.

### Example 4 — what to report

A complete verification statement for the 2-D case:

> Operator: five-point Laplacian, Dirichlet data. Manufactured solution
> $u_m = \sin(\pi x)\sin(2\pi y)$, source $f = -5\pi^{2}u_m$ imposed exactly.
> Norm: discrete $L^{2}$ on the interior. Grids $N = 16, 32, 64, 128$. Errors
> $5.495\times10^{-3}$, $1.367\times10^{-3}$, $3.415\times10^{-4}$,
> $8.535\times10^{-5}$. Observed order $2.00 \pm 0.01$. Design order $2$.
> Solver: direct, so no tolerance floor. Verified for this operator and this
> solution family; **not** verified for the physical adequacy of the equations.

Every claim in that paragraph is falsifiable by a reader with the same code and
one afternoon. That is the standard.

## 9. Python demonstration

`code/code_verification_demo.py` runs the whole study in about $0.4$ s and prints
labelled results with units:

```bash
cd 19-numerical-modeling-hpc/07-verification-validation-uncertainty/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python code_verification_demo.py
```

It computes the 1-D and 2-D refinement tables, the upwind comparison, the
$2$ per cent wrong-source experiment with its residual, and a summary table of
what a convergence study catches. It exits 0 and needs no network access.

A caution worth internalising: the demonstration *is* the verification of the
small solver it contains, and nothing else. If you copy the solver into a larger
code and change the boundary data, the verification does not transfer.

## 10. Exercises

Graded problems with worked solutions:
[`exercises/01-code-verification-exercises.md`](exercises/01-code-verification-exercises.md)
and
[`exercises/01-code-verification-solutions.md`](exercises/01-code-verification-solutions.md).
They include deriving a fourth-order stencil and predicting its measured error,
designing a manufactured solution that a given bug cannot survive, and
constructing a factory of manufactured solutions whose order is a chosen value.

## 11. Applications

- **Every simulation code in this folder.** The seismic, gravity, EM, convection
  and climate codes of
  [08 Geophysical Simulation Case Studies](../08-geophysical-simulation-case-studies/README.md)
  are verified this way; the case-study lessons report the measured orders.
- **Community benchmarks.** Standard problems exist so that independent codes can
  be compared on the same terms
  ([04 Standard Benchmark Problems](04-benchmark-problems.md)); MMS is what makes
  a benchmark applicable to a code whose geometry differs from the benchmark's.
- **Production and regulatory codes.** The discipline of stating operator,
  solution, norm, grid sequence and observed order is what makes a verification
  report auditable, and it is the difference between "the code is verified" as a
  claim and as evidence.
- **Teaching numerical analysis.** MMS is the cheapest way to demonstrate a
  truncation-error derivation: the derivation predicts a number, and the run
  checks it.

## 12. Further study

- [19-01-02 Truncation Error, Order of Accuracy and Convergence Rates](../01-numerical-foundations/02-convergence-and-error.md)
  and [19-01-03 Consistency, Stability and the Lax Equivalence Theorem](../01-numerical-foundations/03-consistency-stability.md)
  — the theory this lesson applies.
- [02 Solution Verification](02-solution-verification.md) — what to do when no
  exact solution exists.
- [03 Model Validation](03-model-validation.md) — the step MMS cannot replace.
- The discipline's standard monographs are Roache's *Verification and Validation
  in Computational Science and Engineering* and Oberkampf & Roy's *Verification
  and Validation in Scientific Computing*; they are cited here as authorities on
  method, and no numeric value in this lesson is taken from them.

## Mastery checkpoint

Without notes:

> A colleague hands you a steady-state diffusion code and the statement "verified,
> the residual is $10^{-14}$". **(a)** State in one sentence why that is not
> evidence of correctness. **(b)** Construct the manufactured solution you would
> use for the operator $-\nabla\cdot(k\nabla u) = f$ with $k$ piecewise constant,
> and give the source term for the manufactured solution $u_m = \sin(\pi x)\sin(2\pi y)$
> with $k = 2$ in $x < 1/2$ and $k = 1$ in $x > 1/2$. **(c)** State which extra
> term your manufactured solution must contain for the interface condition to be
> exercised by the source, and why a solution that is smooth across the interface
> cannot test it. **(d)** Given errors $1.00\times10^{-2}$, $2.50\times10^{-3}$,
> $6.25\times10^{-4}$ on grids $h, h/2, h/4$, compute the observed order and say
> whether the code is acceptable at its design order 2.

A worked version of (b)–(d) appears in
[`exercises/01-code-verification-solutions.md`](exercises/01-code-verification-solutions.md).

## Common pitfalls

1. **Treating a small residual as verification.** A wrong code solves its own
   equations exactly; the demonstration measures $1.83\times10^{-13}$ alongside a
   $2$ per cent error.
2. **Reporting one error value.** With no refinement sequence the order is
   unknown, and the first-order scheme at $N = 512$ and the second-order scheme at
   $N = 32$ are within a factor of $1.3$ of each other.
3. **A manufactured solution that does not excite a term.** If a term of the
   operator is inactive on $u_m$, a bug in that term passes verification.
4. **Boundary data that are not exact.** Interpolated boundary values put a fixed
   error into the solution that stops the sequence converging at its design order.
5. **Confusing order with accuracy.** A fourth-order scheme on a coarse grid can be
   less accurate than a second-order scheme on a fine one; the order says how the
   error will behave, not how large it is.
6. **Claiming more than was tested.** A manufactured solution verifies the code
   against the equations as written. It cannot detect that the equations omit the
   physics that matters.

## Related modules

- [19-01 Numerical Foundations for Simulation](../01-numerical-foundations/README.md)
  — truncation error, stability and the equivalence theorem.
- [19-02 Finite-Difference Methods](../02-finite-difference-methods/README.md) —
  the operators verified here.
- [19-07-02 Solution Verification](02-solution-verification.md),
  [19-07-03 Model Validation](03-model-validation.md),
  [19-07-04 Benchmark Problems](04-benchmark-problems.md) — the rest of the
  discipline.
- [03-12 Numerical Simulation in Python](../../03-scientific-computing/12-numerical-simulation-python/README.md)
  — the same tests written as reusable Python.
- [05-03-05 Validating Forward Codes Against Analytic Benchmarks](../../05-core-geophysics/03-forward-modelling-principles/05-forward-model-validation.md)
  — the geophysical version of the benchmark suite.
- [13-05-03 Benchmarking Geodynamic Codes](../../13-geodynamics-tectonics/05-geodynamic-modelling/03-benchmarking-geodynamics.md)
  — community benchmarks in a mature modelling field.

## Self-assessment checklist

- [ ] I can state the difference between code verification, solution verification
      and validation, with the reference each one uses.
- [ ] I can derive the leading truncation term of the three-point second
      difference and predict the error at a stated $h$.
- [ ] I can construct a manufactured solution, its source, and its boundary data.
- [ ] I can compute an observed order from three grids and interpret a deviation
      from the design order.
- [ ] I can explain why a machine-precision residual coexists with an O(1) error.
- [ ] I can write a verification statement that a reader could falsify.
