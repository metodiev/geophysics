---
id: 19-01-02
title: "Truncation Error, Order of Accuracy and Convergence Rates"
level: doctoral
prereqs: ["19-01-01", "01-12-07", "01-12-03"]
tags: [numerical-modelling, hpc, truncation-error, order-of-accuracy, richardson, verification]
---

# Truncation Error, Order of Accuracy and Convergence Rates

"The code is second order" is a claim about a limit, and that limit is either
measured or the claim is worthless. This lesson separates four things that are
routinely conflated — the local truncation error, the global discretisation
error, the observed order of accuracy, and the algebraic error of an iterative
solver — and shows how to measure the third from solutions alone, with no
knowledge of the exact answer. It ends at the point where refinement stops
helping, because round-off grows as fast as truncation falls.

**All models and data in this module are SYNTHETIC**: the manufactured problem
and its solution are chosen teaching functions. Every number quoted here is
printed by `code/convergence_and_error_demo.py`.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the leading truncation term of a difference operator from its
   moments, and **predict** the constant that multiplies $h^{p}$.
2. **Distinguish** local truncation error from global discretisation error and
   explain why the global error usually has the same order as the local one.
3. **Measure** the observed order of accuracy from solutions on three nested
   grids, without using the exact solution.
4. **Extrapolate** with Richardson's method and **state** the improvement it buys
   in terms of the next term in the error expansion.
5. **Compute** a grid-convergence index and **compare** it with the true error to
   expose the conservative safety factor.
6. **Predict** the optimal step size at which truncation and round-off balance,
   and **explain** why further refinement makes a result worse.

## Prerequisites

- [19-01-01 Discretisation: Grids, Nodes, Cells and Degrees of Freedom](01-discretisation-concepts.md) —
  grids, DOF and the discrete norm.
- [01-12-03 Numerical Differentiation and Finite-Difference Stencils](../../01-mathematics/12-numerical-methods/03-numerical-differentiation.md) —
  the stencils whose error constants are derived here.
- [01-12-07 Discretising PDEs: Consistency, Stability, Convergence](../../01-mathematics/12-numerical-methods/07-pde-discretisation.md) —
  the framework these measurements verify.

## 1. Intuition: three different errors and a limit

A simulation that halts after a tolerance is met has solved the *discrete*
problem approximately. The discrete problem is a *different problem* from the
continuous one. Three errors therefore exist:

- **algebraic error** — how far the solved linear system is from the exact
  solution of the discrete equations. Controlled by tolerances.
- **discretisation error** — how far the exact solution of the discrete
  equations is from the exact solution of the continuous equations. Controlled
  by $h$, and the subject of this lesson.
- **modelling error** — how far the continuous equations are from the Earth.
  Controlled by physics, and out of scope here.

Order of accuracy is the exponent $p$ in

$$e_h \equiv \|u_h - u\| \approx C\,h^{p}$$

as $h \to 0$ at fixed ratios of the other discretisation parameters. A scheme
with $p = 2$ and $C = 10^{3}$ is *worse* than a scheme with $p = 1$ and
$C = 10^{-2}$ on every grid you can afford; that is why the constant must be
measured alongside the order.

## 2. Precise definitions

**Local truncation error (LTE).** Apply the discrete operator $L_h$ to the exact
solution $u$: $\tau_h = L_h u - (L u)$. It is a *residual* — what the scheme
leaves over when handed a perfect answer.

**Order of accuracy.** A scheme is *consistent of order $p$* when
$\tau_h = O(h^{p})$ as $h\to0$ with the other parameters held in proportion.
Consistency is a statement about a limit, not about any finite grid.

**Global error.** $e_h = u_h - u$. For a stable scheme with a $p$-th-order
consistent discretisation of a well-posed problem, $e_h = O(h^{p})$: the
$O(h^{-1})$ amplification of the local error by $h^{-1}$ steps is exactly
cancelled by the extra factor of $h$ in the local error. That sentence is the
whole content of the textbook phrase "first-order accurate".

**Observed order.** For nested grids with refinement ratio $r$, the three-grid
estimate

$$p_{\text{obs}} = \frac{\ln\left(\left|u_{3}-u_{2}\right| /
\left|u_{2}-u_{1}\right|\right)}{\ln r}$$

uses only computed solutions. It is the honest measurement, because it does not
assume that the leading term is the only one present.

## 3. Derivations

### 3.1 Truncation constants from Taylor series

Expand around $x_0$ and collect powers of $h$. For $f = \sin$ at
$x_0 = 0.5$ rad the exact derivatives are $f' = 0.87758256$, $f'' = -0.47942554$:

| operator | leading error | value at $h = 0.01$ |
|---|---|---|
| forward difference, $f'$ | $+\tfrac{h}{2}f''$ | $-0.2397128\,h$ |
| central difference, $f'$ | $-\tfrac{h^{2}}{6}f'''$ | $-0.1462638\,h^{2}$ |
| central 5-point, $f'$ | $-\tfrac{h^{4}}{30}f^{(5)}$ | $-0.0292528\,h^{4}$ |
| central difference, $f''$ | $+\tfrac{h^{2}}{12}f''''$ | $+0.0399521\,h^{2}$ |

The demonstration computes the actual error and divides by $h^{p}$:

| operator | measured error$/h^{p}$ | exact Taylor value |
|---|---|---|
| forward $f'$ | $-0.2411734$ | $-0.2397128$ |
| central $f'$ | $-0.1462630$ | $-0.1462638$ |
| central 5-point $f'$ | $-0.0292525$ | $-0.0292528$ |
| central $f''$ | $+0.0399520$ | $+0.0399521$ |

Agreement to five or six figures at $h = 0.01$. The forward difference deviates
in the third figure because its next term is $O(h^{2})$ relative to its leading
term, while the central stencils have no $h^{3}$/[odd] term to spoil the ratio.
The general receipt is: the order $p$ is the smallest integer with a non-zero
moment $\sum_i w_i \xi_i^{p}$, and the constant is that moment divided by $p!$.

### 3.2 A manufactured problem with a closed-form solution

Nothing above required a PDE. For a convergence study we need one, with an exact
solution. Take the one-dimensional Poisson problem

$$-u''(x) = \pi^{2}\sin(\pi x),\quad x\in(0,1),\qquad u(0) = u(1) = 0,$$

whose exact solution is $u = \sin(\pi x)$. Discretising with the three-point
operator on $x_i = i h$, $h = 1/n$, gives the linear system
$T_h u_h = f_h$ with $T_h = h^{-2}\,\mathrm{tridiag}(-1,2,-1)$.

Insert the exact solution: because $T_h u = -u'' - \tfrac{h^{2}}{12}u'''' + O(h^{4})$,

$$T_h u = f - \frac{h^{2}}{12}u'''' + O(h^{4})
       = f - \frac{h^{2}}{12}\pi^{4}\sin(\pi x) + O(h^{4}).$$

Writing $e = u - u_h$ and subtracting,

$$T_h e = -\frac{h^{2}\pi^{4}}{12}\sin(\pi x) + O(h^{4})
        = -\frac{h^{2}\pi^{2}}{12}\,f.$$

Since $T_h$ inverts the operator that $u$ satisfies, the smooth part of the error
is proportional to $u$ itself:

$$e \approx -\frac{h^{2}\pi^{2}}{12}\,u
\qquad\Longrightarrow\qquad
\max|e| \approx \frac{\pi^{2}}{12}\,h^{2} = 0.822467\,h^{2}.$$

This is an *exact* prediction of the constant, not a fit. The demonstration
measures it:

| $n$ cells | $h$ | $\max|e|$ | $\max|e|/h^{2}$ | observed order |
|---|---|---|---|---|
| 10 | 0.100000 | $8.265417\times10^{-3}$ | 0.826542 | — |
| 20 | 0.050000 | $2.058707\times10^{-3}$ | 0.823483 | 2.005349 |
| 40 | 0.025000 | $5.142005\times10^{-4}$ | 0.822721 | 2.001335 |
| 80 | 0.012500 | $1.285204\times10^{-4}$ | 0.822530 | 2.000334 |
| 160 | 0.006250 | $3.212824\times10^{-5}$ | 0.822483 | 2.000083 |

The column $\max|e|/h^{2}$ walks towards $0.822467$ from above, and the
solution-difference estimate $p_{\text{obs}}$ — computed with no knowledge of the
exact solution — reaches $2.000417$ on the two finest grids. Both statements are
needed: the constant alone cannot distinguish a correct scheme from a
consistent-but-wrong one, and the order alone says nothing about the size of the
error you will actually see.

### 3.3 Richardson extrapolation and what it is worth

If $e_h = C h^{p} + O(h^{q})$ with $q > p$ and the grids nest, then

$$u_{\text{ext}} = u_{h} + \frac{u_{h} - u_{2h}}{2^{p}-1}$$

cancels the leading term. In the demonstration the fine solution
($n = 160$) has $\max|e| = 3.212824\times10^{-5}$ and the extrapolated value has
$\max|e| = 9.907975\times10^{-9}$ — an improvement factor of $3242$. That factor
is *not* the textbook $2^{p} = 4$: cancellation of the $h^{2}$ term exposes the
$h^{4}$ term, and for this particular solution the $h^{4}$ coefficient happens to
be $6.5$ against $0.82$ for $h^{2}$, which is what turns a factor of four into
three thousand. The honest statement is that extrapolation removes the term you
know about; how much better the answer becomes depends on the ratio of the
coefficients, which is why the improvement factor must be measured and not
assumed.

### 3.4 A grid-convergence index is a conservative error bar

Roache's index converts the solution difference into an error estimate,

$$\text{GCI} = F_s\,\frac{\left|u_{h}-u_{2h}\right| / \left|u_{h}\right|}
{2^{p}-1},\qquad F_s = 1.25\ \text{(a chosen safety factor)},$$

referred here to the peak amplitude so that no division by a zero of the
solution occurs. The demonstration finds

$$\text{GCI} = 0.004015\ \%,\qquad
\text{true relative error of } u_h = 0.003213\ \%,\qquad
\frac{\text{GCI}}{\text{true error}} = 1.2496.$$

The ratio is $F_s$ itself, to three figures, because the extra term in the
denominator is negligible at this resolution. That is the diagnostic value of
the index: it is not an estimate of the error but a *bound with a stated safety
factor*, and when the measured ratio departs from $F_s$ the error expansion is
not behaving as assumed — most often because the observed order is wrong.

### 3.5 The floor: round-off grows as truncation falls

Every stencil is a difference of nearly equal numbers, so its absolute error
contains a round-off term that scales as $u\,\|f\|/h^{2}$ with
$u = \varepsilon_{\text{mach}} = 2.220\times10^{-16}$. The two terms balance at

$$h_{\text{opt}} \sim \left(\frac{c\,u}{C}\right)^{1/4}$$

for a second-order difference, giving a floor that cannot be crossed by
refinement. Measuring the second derivative of $\sin$ at $x_0 = 0.5$:

| $h$ | measured error | $h^{2}/12 + 4u/h^{2}$ |
|---|---|---|
| $10^{-1}$ | $3.993881\times10^{-4}$ | $8.333\times10^{-4}$ |
| $10^{-3}$ | $3.997020\times10^{-8}$ | $8.422\times10^{-8}$ |
| $10^{-4}$ | $4.462626\times10^{-10}$ | $8.965\times10^{-8}$ |
| $10^{-5}$ | $-4.047851\times10^{-7}$ | $8.882\times10^{-6}$ |
| $10^{-6}$ | $3.123657\times10^{-5}$ | $8.882\times10^{-4}$ |
| $10^{-8}$ | $4.794255\times10^{-1}$ | $8.882\times10^{0}$ |

The smallest error occurs at $h = 1.081\times10^{-4}$ with $|e| =
1.621\times10^{-9}$. Fitting the round-off-dominated columns gives a measured
coefficient $|e|h^{2}/u = 0.1121$ — the worst-case bound $4u/h^{2}$ overestimates
by $36\times$, which is why the observed floor sits below the pessimistic
prediction. Feeding the *measured* coefficient back into the balance gives
$h_{\text{opt}} = (12cu)^{1/4} = 1.315\times10^{-4}$, against the measured
$1.081\times10^{-4}$. The lesson is that the classical scalings are right and the
constants are not — the constants are measurable properties of your arithmetic.

## 4. Worked example: auditing a claimed order

*A report states that a solver is second-order accurate in space and shows
errors $e = 4.0\times10^{-3}$ on a 50-cell grid and $1.0\times10^{-3}$ on a
100-cell grid. Is the claim supported?*

1. Ratio of errors: $4.0$; ratio of step sizes: $2$; observed order
   $p = \ln 4/\ln 2 = 2.00$. The claim is consistent with the two numbers.
2. But two grids give a two-point order estimate, and that estimate is
   contaminated by any higher-order term. With a third grid at 200 cells the
   same scheme should give $2.5\times10^{-4}$; if it gives
   $3.1\times10^{-4}$ the asymptotic regime has not been reached and the
   three-grid formula $p=\ln[(u_3-u_2)/(u_2-u_1)]/\ln 2$ returns something
   smaller than two. In the demonstration this formula returns $2.000417$ on the
   $80/160$ pair, i.e. the scheme *is* in its asymptotic regime there.
3. State the constant too: $e/h^{2} = 4.0\times10^{-3}/4\times10^{-4}$ per cell
   squared — for this normalisation $10$ — which is the number that tells a
   reader what resolution is needed for a target error.
4. Refine once more and watch for the floor. If $e$ stops falling, the round-off
   term of §3.5 has taken over and the reported order will collapse to zero or
   become negative.

## 5. Assumptions and regime of validity

1. **Asymptotic regime.** $e_h \approx C h^{p}$ requires $h$ small enough that
   the next term is negligible. Every table above shows the constant still
   moving in the first two rows: that is the non-asymptotic regime.
2. **Nested grids.** The three-grid formula and Richardson extrapolation assume
   the coarse grid nodes are a subset of the fine ones, or that a consistent
   transfer (interpolation) is used. Interpolating the coarse solution onto the
   fine grid introduces an error of the *same order* as the discretisation error
   and destroys the extrapolation.
3. **Fixed ratios.** The order is measured at fixed CFL number (or fixed
   diffusion number); refining $h$ while holding $dt$ changes the scheme being
   measured.
4. **Smooth solutions.** The truncation analysis assumes enough derivatives to
   exist. At a material interface or a shock the order locally drops — often to
   zero — while the global $L^{1}$ order can still be one.
5. **Norm dependence.** $L^{\infty}$, $L^{1}$ and $L^{2}$ orders can differ. All
   numbers here are $L^{\infty}$ over the grid, and the norm is part of the
   claim.
6. **Deterministic round-off.** The floor of §3.5 is a property of IEEE double
   precision and this stencil; single precision moves it by a factor
   $(2^{29})^{1/4} \approx 118$ to larger $h$, and a different formula moves the
   measured coefficient.

## 6. Python demonstration

`code/convergence_and_error_demo.py` performs four experiments and prints each
number above:

1. measured truncation constants against their exact Taylor values;
2. the manufactured Poisson problem on five nested grids, with two independent
   order estimates and the predicted constant $\pi^{2}/12$;
3. Richardson extrapolation and a grid-convergence index with its safety factor;
4. the round-off floor, an empirical round-off coefficient, and the optimal step
   size implied by it.

```bash
cd 19-numerical-modeling-hpc/01-numerical-foundations/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python convergence_and_error_demo.py
```

## Mastery checkpoint

Without notes:

> A solver is run on three nested grids with refinement ratio $r = 2$, giving
> $\|u_h - u_{2h}\| = 1.6\times10^{-4}$ and
> $\|u_{2h} - u_{4h}\| = 6.4\times10^{-4}$ in the $L^{\infty}$ norm, and an exact
> solution is available for a manufactured case. **(a)** Compute the observed
> order. **(b)** Compute the Richardson-extrapolated solution's expected error
> and state which term limits it. **(c)** Give the GCI with $F_s = 1.25$ and say
> what it bounds. **(d)** If the errors instead came out as
> $1.55\times10^{-4}$ and $6.4\times10^{-4}$, explain what has gone wrong and
> name two possible causes.

The arithmetic for (a)–(c) is in
[`exercises/02-convergence-and-error-solutions.md`](exercises/02-convergence-and-error-solutions.md).

## Common pitfalls

1. **Quoting an order without the constant.** Both are needed to size a grid.
2. **Fitting a line to two grids.** Two points always give a slope; they do not
   give evidence that the slope is the order.
3. **Comparing errors on non-nested grids.** The interpolation error is the same
   order as the discretisation error and swamps the difference.
4. **Refining past the floor.** Beyond $h_{\text{opt}}$ the answer gets worse;
   the measured coefficient here makes that ceiling concrete.
5. **Treating GCI as the error.** It is an upper bound with a stated safety
   factor; the ratio to the true error is a diagnostic, not a coincidence.
6. **Mixing the algebraic and discretisation errors.** Reporting a solver
   tolerance as an accuracy claim confuses two unrelated limits.

## Related modules

- [19-01-03 Consistency, Stability and the Lax Equivalence Theorem](03-consistency-stability.md) —
  why order alone does not imply convergence.
- [19-01-04 Numerical Dispersion, Dissipation and Grid Anisotropy](04-numerical-dispersion-diffusion.md) —
  the errors that refinement does not remove.
- [03-12-04 Verification vs Validation: Benchmarks and Convergence Tests](../../03-scientific-computing/12-numerical-simulation-python/04-verification-and-validation.md) —
  the verification practice built on these estimates.
- [19-02-06 FD for Diffusion, Laplace and Poisson Problems](../02-finite-difference-methods/06-fd-diffusion-and-potential.md) —
  the 2-D version of the manufactured problem, with the same constant.
- [Module 19-01 Numerical Foundations for Simulation](README.md).

Exercises and worked solutions:
[`exercises/02-convergence-and-error-exercises.md`](exercises/02-convergence-and-error-exercises.md)
and
[`exercises/02-convergence-and-error-solutions.md`](exercises/02-convergence-and-error-solutions.md).
