---
id: 19-07-04
title: "Standard Benchmark Problems and Community Comparisons"
level: research
prereqs: ["19-07-01", "19-07-02", "19-01-04"]
tags: [numerical-modelling, verification, benchmarking, community-comparison, norms, reproducibility]
---

# Standard Benchmark Problems and Community Comparisons

## Learning objectives

By the end of this lesson you will be able to:

1. **Write** a benchmark specification complete enough that a reader can
   reproduce it: equations, domain, boundary data, gauge, source discretisation,
   norm, grid sequence, functional and cost metric.
2. **Derive** the coefficients of a fourth-order second-derivative stencil from its
   symbol, and **state** its leading truncation term.
3. **Explain** why a differential equation with a null space (such as the periodic
   Laplacian) defines a *family* of benchmarks, and **compute** the ambiguity when
   the gauge is unspecified.
4. **Measure** the spread between two defensible discretisations of the same
   benchmark, and **compare** it with each code's error against the exact solution.
5. **Show** that agreement between independent codes is not verification, and
   **state** what a comparison table actually tests.
6. **Decide** whether a method is applicable to a benchmark at all, from its
   boundary-condition and smoothness assumptions.

## Prerequisites

- [19-07-01 Code Verification: Order-of-Accuracy and Manufactured Solutions](01-code-verification.md)
  — the refinement study that every benchmark comparison rests on.
- [19-07-02 Solution Verification](02-solution-verification.md) — how much of a
  difference between two codes is discretisation error.
- [19-01-04 Numerical Dispersion, Dissipation and Grid Anisotropy](../01-numerical-foundations/04-numerical-dispersion-diffusion.md)
  — the scale on which geometric choices produce measurable error.

All models and data in this module are **SYNTHETIC**. Every benchmark in this
lesson is defined here, its exact solution is derived here, and every number is
printed by the lesson's demonstration. No figure is quoted from a published
benchmark suite.

## 1. Intuition: the two things a benchmark can do

A benchmark problem is a small, completely specified calculation whose answer is
known, used to compare methods or codes on equal terms. It can do exactly two
things, and it is worth keeping them apart.

**It can verify a code.** If the benchmark's reference solution is exact for the
equations the code claims to solve, agreement within a stated tolerance is
evidence of correctness — for those equations, on that problem class. This is the
use of [01 Code Verification](01-code-verification.md).

**It can compare methods or codes on cost and accuracy.** Here the benchmark is an
accounting device: it fixes the problem and the figure of merit, and it reports
accuracy against work. This is what "community comparison" means, and the
comparison is far weaker than it looks. Two codes can agree to machine precision
because they share a convention; the demonstration measures exactly that. Two
codes can disagree by $O(h^{2})$ while both are correct; the demonstration measures
that too. And a method can be excluded by a benchmark's boundary conditions rather
than by its accuracy.

The practical conclusion, which this lesson exists to make unavoidable, is that
**a comparison table is only as meaningful as its specification.** Every
unstated choice — the gauge, the norm, the treatment of the source, the definition
of the functional, the way cost is counted — is a degree of freedom that can move
the ranking without moving the physics.

## 2. Definitions

**Benchmark problem.** A problem statement with (i) the equations, (ii) the
domain and boundary data, (iii) the gauge where the operator has a null space,
(iv) the definition of every discretised quantity, (v) the exact or reference
solution, and (vi) the figure of merit.

**Figure of merit.** The scalar on which methods are compared: an error norm at a
stated resolution, the resolution needed for a stated tolerance, or the work
needed for a stated tolerance.

**Verification benchmark.** The reference is exact for the code's equations
(analytic or manufactured).

**Validation benchmark.** The reference is independent data
([03 Model Validation](03-model-validation.md)). The two are often confused, and a
paper that reports the first while implying the second has overclaimed.

**Null space.** The set of non-trivial functions mapped to zero by the operator. A
null space makes the solution non-unique and the benchmark under-specified until a
gauge is imposed.

## 3. Writing a benchmark specification

The checklist below is the one this lesson's demonstration satisfies. Each line is
a choice that can change a reported number; leaving one out is what makes
comparisons irreproducible.

1. **Equation**, with signs and coefficients: $-u'' = f$ on $[0,1)$.
2. **Domain and boundary data**, including periodicity or the type of each
   boundary condition. A periodic method cannot represent a Dirichlet problem
   (Section 5.4 measures the failure).
3. **Exact solution**, and how it was obtained: substitution, an eigenvalue
   relation, or a manufactured source.
4. **Gauge**, where the operator has a null space: here "the mean of $u$ is
   zero".
5. **Source discretisation**: nodal sampling or cell averaging (Section 5.2).
6. **Norm**, with the discrete weight: the discrete $L^{2}$ norm
   $\lVert e\rVert = \sqrt{h\sum_i e_i^{2}}$; and whether any restriction to the
   interior was applied.
7. **Grid sequence**: the values of $N$ and the refinement ratio $r$.
8. **Functional of interest**, if one is reported ([02](02-solution-verification.md)).
9. **Cost metric**: unknowns, non-zeros, floating-point operations or wall time,
   and on what hardware if it is time.
10. **Solver tolerance**, which sets a floor that no accuracy claim can go below.

## 4. Derivations

### 4.1 A fourth-order second-derivative stencil from its symbol

Let the stencil act on $\theta_j = e^{\mathrm{i}j\theta}$. It has the symbol
(times $1/h^{2}$)

$$S(\theta) = \frac{1}{h^{2}}\sum_{j} a_j e^{\mathrm{i}j\theta}.$$

With symmetry $a_{-j} = a_j$ and $u'' = -k^{2}u$ for $u = e^{\mathrm{i}kx}$, we
require

$$a_0 + 2a_1\cos\theta + 2a_2\cos 2\theta = -\theta^{2} + O(\theta^{6}).$$

Expanding $\cos\theta = 1 - \theta^{2}/2 + \theta^{4}/24 - \theta^{6}/720$ and
$\cos 2\theta = 1 - 2\theta^{2} + (2/3)\theta^{4} - (4/45)\theta^{6}$, three
conditions determine the three coefficients:

$$\text{const: } a_0 + 2a_1 + 2a_2 = 0, \qquad
\theta^{2}: a_1 + 4a_2 = 1, \qquad
\theta^{4}: \frac{a_1}{12} + \frac{4a_2}{3} = 0 .$$

Multiplying the last by $12$ gives $a_1 + 16a_2 = 0$, so $a_2 = -1/12$,
$a_1 = 4/3$ and $a_0 = -5/2$. Scaling by $12$:

$$\frac{-u_{i-2} + 16u_{i-1} - 30u_i + 16u_{i+1} - u_{i+2}}{12h^{2}}
= u'' + O(h^{4}),$$

with the $\theta^{6}$ coefficient equal to $1/90$, so the leading error is
$-\frac{h^{4}}{90}u^{(6)}$. This is the stencil the demonstration uses as its
fourth-order method, and the measured order verifies the derivation.

### 4.2 Why the gauge is not a detail

On the periodic domain the discrete second-difference matrix $L_h$ maps the
constant vector to zero: it has a null space. Two consequences follow immediately.

- **Solvability.** $L_h u = f$ has a solution only if $f$ is orthogonal to the
  null space, i.e. $\sum_i f_i = 0$. A source with non-zero mean has no periodic
  solution at all, and a solver that "works" on it is silently solving something
  else.
- **Non-uniqueness.** When it is solvable, the solution is determined only up to an
  additive constant. An error norm computed against a specific exact solution then
  depends on the gauge choice, and can be made arbitrarily large by choosing a
  different one.

A benchmark that omits the gauge therefore does not have a figure of merit. The
demonstration imposes "mean of $u$ is zero" in its specification and sets the
$k = 0$ Fourier mode of the source to zero.

### 4.3 The two legitimate source discretisations

For a continuum source $f$, a discretisation may sample it at nodes,

$$f_i = f(x_i),$$

or average it over the cell,

$$f_i = \frac{1}{h}\int_{x_i - h/2}^{x_i + h/2} f(x)\,\mathrm{d}x
\;\approx\; \frac{f(x_i - h/2) + f(x_i + h/2)}{2}.$$

Both are consistent, both are second-order accurate approximations of the same
continuum problem, and both converge. They do **not** give the same discrete
solution: the difference is $O(h^{2})$, exactly the size of each one's error. A
benchmark that does not fix this choice cannot distinguish "the codes disagree
because one is wrong" from "the codes disagree because they discretise the source
differently".

## 5. Measured evidence

The demonstration `code/benchmark_problems_demo.py` solves one benchmark three
ways and then probes the specification with four experiments. The benchmark is the
periodic problem

$$-u'' = (2\pi)^{2}\sin(2\pi x) \ \text{ on } [0,1), \qquad
u(x) = \sin(2\pi x),$$

solved exactly in Fourier space for each method (the discrete operator is
circulant, so this is the exact solution of the discrete equations rather than an
iterative approximation), with the mean mode set to zero.

### 5.1 Three methods, measured orders

| $N$ | FD2 error | order | FD4 error | order | spectral error |
|---:|---:|---:|---:|---:|---:|
| 8 | $3.750\times10^{-2}$ | — | $2.841\times10^{-3}$ | — | $5.363\times10^{-17}$ |
| 16 | $9.158\times10^{-3}$ | 2.03 | $1.843\times10^{-4}$ | 3.95 | $1.457\times10^{-16}$ |
| 32 | $2.276\times10^{-3}$ | 2.01 | $1.164\times10^{-5}$ | 3.99 | $1.416\times10^{-16}$ |
| 64 | $5.682\times10^{-4}$ | 2.00 | $7.292\times10^{-7}$ | 4.00 | $1.594\times10^{-16}$ |
| 128 | $1.420\times10^{-4}$ | 2.00 | $4.561\times10^{-8}$ | 4.00 | $1.545\times10^{-16}$ |

FD2 and FD4 converge at their design orders $2$ and $4$. The spectral method
reaches round-off at $N = 8$ and **cannot be improved**: the error is then the
accumulated round-off of the transform, not a discretisation error, and it even
wanders slightly ($5.4\times10^{-17}$ to $1.6\times10^{-16}$) with $N$. Reporting
"spectral, $10^{-16}$" as an accuracy is a claim about a method's floor, not about
the physics.

### 5.2 The hidden choice, measured

The same FD2 operator with the source sampled at nodes and averaged over cells:

| $N$ | $\lVert u_{\text{nodal}} - u_{\text{cell-avg}}\rVert$ | FD2 error vs exact |
|---:|---:|---:|
| 8 | $5.668\times10^{-2}$ | $3.750\times10^{-2}$ |
| 16 | $1.376\times10^{-2}$ | $9.158\times10^{-3}$ |
| 32 | $3.416\times10^{-3}$ | $2.276\times10^{-3}$ |
| 64 | $8.524\times10^{-4}$ | $5.682\times10^{-4}$ |

The spread between the two defensible codes is **larger than either one's error**
(measured ratio $1.51$, $1.50$, $1.50$, $1.50$), and the algebra of §4.3 gives the
limit exactly. For this Fourier pair, with $\theta = kh$, the nodal solve returns
$u_{\text{nodal}} \approx (1 + \theta^{2}/12)\sin(2\pi x)$ while the cell-averaged
source multiplies the answer by $\cos(\theta/2) \approx 1 - \theta^{2}/8$, so
measurement error to solution error is $(\theta^{2}/8)/(\theta^{2}/12) = 3/2$. A
comparison table that does not state this choice cannot interpret a factor-of-$1.5$
disagreement.

### 5.3 Agreement is not verification

At $N = 64$, with the source multiplied by $1.01$ in two codes written to the same
specification:

| quantity | measured |
|---|---:|
| $\lVert u_B - u_C\rVert / \lVert u\rVert$ | $0.000\times10^{0}$ |
| $\lVert u_B - u_{\text{exact}}\rVert / \lVert u\rVert$ | $1.081\times10^{-2}$ |
| $\lVert u_A - u_{\text{exact}}\rVert / \lVert u\rVert$ (correct code) | $8.036\times10^{-4}$ |

The two wrong codes agree *exactly* — they share the same discretisation, so their
difference is zero — while both are $1.08$ per cent from the exact solution, which
is $13$ times the correct code's error. Agreement is a test of shared assumptions.
Only the comparison with an exact solution tests correctness.

### 5.4 A method excluded by the boundary conditions

The periodic spectral solver applied to the Dirichlet problem
$-u'' = \pi^{2}\sin(\pi x)$, $u(0) = u(1) = 0$:

| $N$ | spectral (periodic) error | FD2 (Dirichlet) error |
|---:|---:|---:|
| 16 | $6.777\times10^{-1}$ | $2.208\times10^{-3}$ |
| 32 | $6.782\times10^{-1}$ | $5.595\times10^{-4}$ |
| 64 | $6.783\times10^{-1}$ | $1.409\times10^{-4}$ |
| 128 | $6.783\times10^{-1}$ | $3.536\times10^{-5}$ |

The periodic answer is wrong by $O(1)$ and does not improve, while FD2 converges
at order $2$. Refinement cannot fix a method applied outside its problem class:
the periodic solver returns the periodic function closest to the answer, and
$\sin(\pi x)$ is not periodic on $[0,1)$. **Applicability is decided before
accuracy, not after.**

### 5.5 Cost for a stated tolerance

Resolution needed for the discrete RMS error to fall below a tolerance:

| tolerance | FD2 ($N$) | FD4 ($N$) | spectral ($N$) |
|---:|---:|---:|---:|
| $10^{-2}$ | 16 | 8 | 4 |
| $10^{-4}$ | 256 | 32 | 4 |
| $10^{-6}$ | $>512$ | 64 | 4 |

On a smooth periodic problem the spectral method wins outright, FD4 needs $8$
times fewer unknowns than FD2 for $10^{-6}$ and has a five-point rather than
three-point stencil, and FD2 cannot reach $10^{-6}$ within the tested range. Every
one of those statements is about this benchmark: its smoothness, its periodicity
and its geometry. Transferring the ranking to a rough or irregular problem
requires a new benchmark that measures the transfer.

## 6. Assumptions and regime of validity

1. **The benchmark's equations are the code's equations.** Otherwise the benchmark
   verifies nothing about the code (it may still be a useful manufactured problem
   for a different code).
2. **The exact solution is exact for the *benchmark*, not for the Earth.** A
   benchmark is a verification device; it is not validation
   ([03](03-model-validation.md)).
3. **Comparisons are made at equal specification.** Equal equation, domain, gauge,
   source discretisation, norm and tolerance. Any unstated difference is a
   confound.
4. **The cost metric is stated.** Wall time comparisons without hardware, problem
   size or tolerance are not reproducible; unknown counts and non-zeros are.
5. **Applicability precedes accuracy.** A method outside its class can produce a
   smooth, plausible, $O(1)$-wrong answer (Section 5.4).
6. **What a community comparison cannot show.** It cannot show that the equations
   are adequate for the Earth, and it cannot detect an error shared by every code
   that follows the same specification.

## 7. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| error norm | $\lVert e\rVert$ | unit of the solution | carries the $\sqrt{h}$ of the discrete measure |
| relative error | — | dimensionless | norm divided by a norm of the exact solution |
| tolerance | — | dimensionless | state whether absolute or relative |
| resolution | $N$ or $h$ | count or length | $N$ has no meaning without the domain length |
| cost | unknowns, nnz, flops, s | — | state the metric and the hardware |

A benchmark table with a dimensional error or an unlabelled "$N$" is not
reproducible. The rule is simple: every number in the table must have the same
meaning for every row.

## 8. Worked examples

### Example 1 — the FD4 stencil, checked

From §4.1, $a_0 = -(30/12) = -2.5$, $a_1 = 16/12 = 1.3333$,
$a_2 = -1/12 = -0.08333$. Check the constant term:
$-2.5 + 2(1.3333) + 2(-0.08333) = -2.5 + 2.6667 - 0.1667 = 0$ ✔.
Check the $\theta^{2}$ term: $a_1 + 4a_2 = 1.3333 - 0.3333 = 1$ ✔.
Check the $\theta^{4}$ term:
$a_1/12 + 4a_2/3 = 0.11111 - 0.11111 = 0$ ✔.
The measured orders $3.95$, $3.99$, $4.00$ in Section 5.1 are the empirical
counterpart of those algebraic identities.

### Example 2 — the cost arithmetic for a tolerance

To reach $10^{-6}$ RMS on this benchmark: FD4 needs $N = 64$, FD2 needs more than
$512$. Using $N$ as the cost proxy and noting the FD4 stencil is five-point against
FD2's three-point, FD4 needs at least $\lceil 512/64\rceil = 8$ times fewer
unknowns, so even with the extra $5/3$ work per unknown it needs about $4.8$ times
less work. The spectral method needs $N = 4$: it is not in the same competition on
a periodic smooth problem. **But if the solution had a discontinuity, the spectral
method's algebraic convergence would lose to any fixed-order scheme** — a
statement that would have to be benchmarked separately, with a problem defined for
the purpose.

### Example 3 — quantifying a missing gauge

Suppose the mean of $u$ were not fixed and two codes returned
$u_1 = \sin(2\pi x)$ and $u_2 = \sin(2\pi x) + c$. The discrete $L^{2}$ norm of the
difference is $\lvert c\rvert$, so with $c = 0.5$ the two codes "disagree" by
$0.5$ while both solve the problem correctly. With the exact solution
$\sin(2\pi x)$, the *error* of code 2 is also $\lvert c\rvert$: both codes would be
judged wrong by an unbounded amount determined entirely by the gauge. Fixing the
mean to zero removes the freedom, and that is why the specification has a line for
it.

### Example 4 — a specification that would reproduce these numbers

> Periodic Poisson benchmark. Equation: $-u'' = (2\pi)^{2}\sin(2\pi x)$ on
> $[0,1)$, periodic. Exact solution $u = \sin(2\pi x)$. Gauge: mean of $u$ zero,
> imposed by setting the $k=0$ Fourier mode of the source to zero. Source
> discretisation: nodal sampling. Norm: discrete RMS, $\sqrt{\frac{1}{N}\sum_i
> e_i^{2}}$. Grids: $N = 8, 16, 32, 64, 128$, ratio $2$. Methods: three-point FD2,
> five-point FD4, Fourier spectral; all solved by diagonalisation of the circulant
> operator, so no solver tolerance enters. Cost metric: $N$ and stencil width.
> Reported: the table of §5.1.

That paragraph is the minimum a reader needs. Every experiment in Section 5 was
obtained by changing exactly one line of it.

## 9. Python demonstration

```bash
cd 19-numerical-modeling-hpc/07-verification-validation-uncertainty/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python benchmark_problems_demo.py
```

Prints the specification, the three-method order table, the hidden-choice spread,
the shared-bug experiment, the applicability failure and the cost table, in
$0.2$ s, with no network access and no file I/O.

## 10. Exercises

[`exercises/04-benchmark-problems-exercises.md`](exercises/04-benchmark-problems-exercises.md)
and
[`exercises/04-benchmark-problems-solutions.md`](exercises/04-benchmark-problems-solutions.md)
ask for a benchmark specification from scratch, a comparison of two specifications
that differ in one line, and a critical review of a comparison table with a hidden
confound.

## 11. Applications

- **Cross-code validation programmes.** A benchmark suite agreed in advance is
  what allows a community to compare codes written by different groups
  ([13-05-03 Benchmarking Geodynamic Codes](../../13-geodynamics-tectonics/05-geodynamic-modelling/03-benchmarking-geodynamics.md)).
- **Method selection.** The cost table of §5.5 is the form in which a method
  choice can be justified in a proposal.
- **Regression testing.** A benchmark with a stored reference value is a test that
  can fail in a build system
  ([03-13-02 Testing Scientific Code](../../03-scientific-computing/13-testing-profiling-packaging/02-testing-scientific-code.md)).
- **Reproducibility.** Recording the specification alongside the numbers is what
  makes a comparison checkable years later
  ([22-02-05 Data Versioning and Provenance Tracking](../../22-data-engineering-reproducibility/02-reproducible-workflows/05-data-versioning.md)).

## 12. Further study

- [19-07-01](01-code-verification.md), [19-07-02](02-solution-verification.md),
  [19-07-03](03-model-validation.md) — the three activities a benchmark serves.
- [19-01-04](../01-numerical-foundations/04-numerical-dispersion-diffusion.md) —
  the geometric error terms that make method rankings problem-specific.
- [19-04-01 Spectral Methods: Basis Choice and Exponential Convergence](../04-spectral-and-pseudospectral/01-spectral-methods.md)
  — why the spectral method wins here and when it does not.

## Mastery checkpoint

Without notes:

> You are asked to benchmark three codes for the 2-D acoustic wave equation on a
> square with absorbing boundaries, reporting accuracy against run time.
> **(a)** List the specification lines you must fix before any comparison is
> meaningful, and say which one you expect to be omitted in practice most often.
> **(b)** Two codes agree to $10^{-14}$ while a third differs from both by
> $3\times10^{-3}$; give the two hypotheses you would test first, in order.
> **(c)** One code is a spectral method and one is fourth-order finite difference;
> on a smooth problem the spectral code is $10^{6}$ times more accurate, yet its
> run time is similar. Explain how to present that honestly using a stated
> tolerance rather than raw errors. **(d)** State one comparison that no benchmark
> of this kind can make, and name the activity that would.

Worked answers appear in
[`exercises/04-benchmark-problems-solutions.md`](exercises/04-benchmark-problems-solutions.md).

## Common pitfalls

1. **Reporting errors without the gauge.** With a null space in the operator the
   "error" is an arbitrary constant (Section 4.2).
2. **Comparing at unstated cost.** Accuracy alone ranks a method that costs a
   thousand times more above one that is adequate for the purpose.
3. **Using agreement as verification.** The demonstration measures exact agreement
   between two codes that are both $1$ per cent wrong.
4. **Ignoring the source discretisation.** It moves the answer by more than either
   code's error (Section 5.2).
5. **Comparing across problem classes.** A periodic method on a Dirichlet problem
   is wrong by $O(1)$ and stays wrong (Section 5.4).
6. **Quoting a spectral error as accuracy.** At $10^{-16}$ the number is
   round-off; the informative statement is the resolution at which the floor is
   reached.

## Related modules

- [19-07 Verification, Validation and Numerical Uncertainty](README.md).
- [19-08 Geophysical Simulation Case Studies](../08-geophysical-simulation-case-studies/README.md)
  — benchmarks applied to geophysical simulation.
- [19-02 Finite-Difference Methods](../02-finite-difference-methods/README.md) —
  the FD2 and FD4 operators used here.
- [19-04 Spectral and Pseudospectral Methods](../04-spectral-and-pseudospectral/README.md).
- [13-geodynamics-tectonics](../../13-geodynamics-tectonics/README.md) — a field
  with an established benchmarking culture.
- [22-data-engineering-reproducibility](../../22-data-engineering-reproducibility/README.md)
  — provenance for the numbers a benchmark produces.

## Self-assessment checklist

- [ ] I can write a benchmark specification whose numbers could be reproduced.
- [ ] I can derive a fourth-order stencil from its symbol and state its leading
      error.
- [ ] I can explain the gauge problem and quantify its effect.
- [ ] I can measure the spread between two defensible discretisations.
- [ ] I can explain why code agreement is not verification.
- [ ] I can decide applicability before accuracy.
