# Module 18-04 — Nonlinear Inversion and Optimisation

**Stages:** graduate → research · **Prerequisites:** modules 18-01, 18-02 and
18-03; [05-03 Forward Modelling Principles](../../05-core-geophysics/03-forward-modelling-principles/README.md).

This module is about what changes when the forward map is not linear. In that
case there is no kernel to factorise and no single solve to regularise: the
answer is the output of an *iteration*, and everything a reader needs to judge it
— whether it stopped at a minimum, whether the minimum is global, and how much of
the model space the data cannot separate — has to be established separately.
Lessons 01–03 cover the local methods that descend from a point (linearisation
and its Jacobian, the step rules, and matrix-free conjugate gradients for large
problems); lessons 04–06 cover the global methods that sample and search a
declared objective (Monte Carlo, simulated annealing, genetic algorithms,
neighbourhood sampling, multi-start and hybrids); lesson 07 collects the
diagnostics that decide whether any of them has produced an answer.

The organising idea is that **a started optimisation is not a converged answer
until its Hessian, its budget and its non-uniqueness are reported**. Every lesson
therefore carries three things: a derivation of the method, a measurement of the
rate or budget it actually achieves, and a measurement of the way it fails —
linear convergence once noise sets the residual floor, semiconvergence of an
iterative solve, premature collapse of a contracting sampler, a target volume too
small for blind sampling, or a stopping rule that certifies a numerically flat
point. The comparisons are always made at *equal cost* and against a *declared*
synthetic objective, so that the ranking is a measurement rather than a
reputation.

All models and data in this module are **SYNTHETIC**. The local-method lessons
use the exact forward model $d(t) = A e^{-\alpha t}$, whose Jacobian is analytic,
so the kernel is a real forward operator; the global-method lessons use a
declared sum-of-Gaussian-well misfit surface whose minima and volumes are known
exactly. Model parameters, station grids, well layouts and noise levels are
teaching values, and every number quoted in a lesson is printed by a
demonstration in [`code/`](code).

## Learning objectives

By the end of this module you will be able to:

1. Formulate a nonlinear inverse problem as a sequence of linearised
   subproblems, verify a Jacobian against finite differences, and state what the
   linearisation assumes and when it fails.
2. Derive the steepest-descent, Gauss–Newton, full-Newton and
   Levenberg–Marquardt steps, state the per-iteration cost and convergence rate
   of each, and measure the rate on a problem with a prescribed spectrum.
3. Implement a matrix-free conjugate-gradient iteration for a large, rank-
   deficient kernel, and diagnose semiconvergence from the model error, model
   norm and residual together.
4. Define the global minimisation problem, measure basin and target volumes, and
   compute the sampling budget those volumes imply as the dimension grows.
5. Describe the neighbourhood algorithm and very fast simulated annealing,
   measure their contraction and acceptance behaviour, and diagnose premature
   collapse.
6. Derive the multi-start success law $1-(1-p)^{k}$, measure $p$, and build a
   coarse-to-fine hybrid strategy that meets a stated success probability at a
   stated cost.
7. Assemble a convergence report — stationary point, Hessian eigenvalues,
   gradient-tolerance parameter cost, linearised covariance and the
   near-equivalent set — that is defensible to a reviewer.

## Prerequisites

- [18-03-02 Tikhonov Regularisation and the Smoothing Trade-Off](../03-regularization/02-tikhonov.md) —
  the linear estimator that lesson 07 extends to a nonlinear problem.
- [18-03-03 Choosing the Trade-Off: L-Curve, GCV, Discrepancy Principle](../03-regularization/03-parameter-choice.md) —
  the parameter-choice logic that an early-stopping iteration index replaces.
- [18-01-01 Forward vs Inverse Problems and the Practical Asymmetry](../01-inverse-problem-foundations/01-forward-and-inverse.md) —
  why the forward map is cheap and its inverse is not.
- [18-02-03 The Generalised (Moore-Penrose) Inverse](../02-linear-inverse-problems/03-generalized-inverse.md) —
  the singular-value coordinates that a rank-deficient iteration must respect.
- [01-07-10 Matrix Calculus](../../01-mathematics/07-linear-algebra/10-matrix-calculus.md) —
  the Jacobian and Hessian this module differentiates.
- [01-14-02 Unconstrained Optimisation](../../01-mathematics/14-optimization/02-unconstrained.md) —
  the step rules of lesson 02 in their general form.
- [05-03-01 The Forward Problem: From Model to Data](../../05-core-geophysics/03-forward-modelling-principles/01-forward-problem.md) —
  how the nonlinear forward model is built.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Local Linearisation, Jacobians and Iteration](01-local-linearization.md) | graduate | Analytic Jacobian verified to $10^{-9}$; the linearisation error is $\mathcal O(\lVert\delta\rVert^{2})$; a Gauss–Newton iteration is quadratic only on a zero-residual problem and linear once noise sets the floor |
| 02 | [Gradient, Gauss-Newton and Full Newton Methods](02-gradient-and-newton.md) | graduate | At $\kappa=100$, 1287 steepest-descent iterations against 17 for CG; 348 against 5 to reach the same answer; the full Hessian turns indefinite (−0.18) at a large residual |
| 03 | [Conjugate Gradient and Large-Scale Inversion](03-conjugate-gradient-inverse.md) | research | An 800-cell kernel whose $K^{\mathsf T}K$ is numerically rank-deficient: the CG model error falls to $0.54$ and then rises to $10^{7}$ — semiconvergence, with the iteration index a regularisation parameter |
| 04 | [Global Search: Monte Carlo, Simulated Annealing, Genetic Algorithms](04-global-search.md) | research | The basin volume falls by 3.3× from $n=2$ to $n=8$, but the target volume falls ~50× per two dimensions: the 50% budget grows from 13 samples to 17328 |
| 05 | [Neighbourhood and Very Fast Simulated Annealing](05-neighbourhood-algorithms.md) | research | Cell contraction is violent — inscribed radius $0.138\to10^{-4}$ in four generations — and a naive implementation collapses to $-0.376$ against a reference $-0.833$ |
| 06 | [Multi-Start, Hybrid and Memetic Strategies](06-multi-start-and-hybrid.md) | research | One measurement of $p$ becomes a budget — 23 starts for 95% — but $p$ falls from 0.35 at $n=2$ to 0.02 at $n=6$, so brute-force multi-start does not scale |
| 07 | [Convergence Diagnosis and Local-Minimum Traps](07-convergence-and-local-minima.md) | doctoral | Every stopped run reports "CONVERGENCE": the tight rule finds two true minima, a loose $f$-tolerance stops on a degenerate point, and a $10^{-2}$ tolerance admits a near-equivalent set 0.29 km wide |

## Suggested path

**If you are new to nonlinear inversion:** lessons 01 → 02 → 07, running each
demonstration. Lesson 01 establishes the iteration and its two regimes; lesson 02
is the only place the four step rules are compared at equal cost; lesson 07 is
the shortest route to seeing why a stopped run is not yet an answer.

**If you have used a nonlinear least-squares solver before:** read 01 §6 (the
measured basin), 02 §5 (where Gauss–Newton and Newton differ), and 03 §4–5
(rank deficiency and semiconvergence) — those are the results that decide whether
a solver is safe to trust on a given problem.

**If you are choosing a global method:** 04 §3 (the curse of dimensionality,
measured as a target volume) and §5–7 (schedules and premature convergence), then
05 and 06. The transferable result is that a ranking depends on the dimension and
the budget, both of which must be measured, not assumed.

**If you are preparing a research project:** 03 §5–6 (early stopping and why
preconditioning is not regularisation), 06 §5 (budget growth with dimension) and
07 §3–6 (the convergence report and the near-equivalent set), plus the ★★★
exercises.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-local-linearization.md`](01-local-linearization.md) | Lesson 01 |
| [`02-gradient-and-newton.md`](02-gradient-and-newton.md) | Lesson 02 |
| [`03-conjugate-gradient-inverse.md`](03-conjugate-gradient-inverse.md) | Lesson 03 |
| [`04-global-search.md`](04-global-search.md) | Lesson 04 |
| [`05-neighbourhood-algorithms.md`](05-neighbourhood-algorithms.md) | Lesson 05 |
| [`06-multi-start-and-hybrid.md`](06-multi-start-and-hybrid.md) | Lesson 06 |
| [`07-convergence-and-local-minima.md`](07-convergence-and-local-minima.md) | Lesson 07 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Seven runnable demonstrations |

| Script | What it measures |
|---|---|
| [`code/local_linearization_demo.py`](code/local_linearization_demo.py) | Finite-difference Jacobian check, second-order residual, Gauss–Newton rate with and without noise, basin of attraction |
| [`code/gradient_newton_demo.py`](code/gradient_newton_demo.py) | Steepest-descent and CG rates on a $\kappa=100$ system, five methods on one start, where the full Hessian becomes indefinite |
| [`code/conjugate_gradient_inverse_demo.py`](code/conjugate_gradient_inverse_demo.py) | Spectrum of a large kernel, matrix-free CG against LSQR, semiconvergence, a stopping rule and its failure, preconditioning |
| [`code/global_search_demo.py`](code/global_search_demo.py) | Basin and target volumes, the curse of dimensionality, cooling schedules at equal budget, a genetic algorithm, an equal-cost comparison |
| [`code/neighbourhood_annealing_demo.py`](code/neighbourhood_annealing_demo.py) | Voronoi-cell contraction and acceptance, premature collapse, the VFSA Cauchy proposal, a ranking at equal cost |
| [`code/multistart_hybrid_demo.py`](code/multistart_hybrid_demo.py) | Measured $p$, the multi-start success law against trials, the cost of 95% success for four strategies, budget growth with dimension |
| [`code/convergence_diagnostics_demo.py`](code/convergence_diagnostics_demo.py) | Every stationary point from a grid of starts, three stopping rules, the gradient tolerance's parameter cost, linearised covariance, the near-equivalent set |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib and
pandas:

```bash
cd 18-inverse-problems/04-nonlinear-inversion/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python local_linearization_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gradient_newton_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python conjugate_gradient_inverse_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python global_search_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python neighbourhood_annealing_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python multistart_hybrid_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python convergence_diagnostics_demo.py
```

Every demo prints labelled results with units, seeds its random numbers with
`np.random.default_rng(20261014)`, uses no network access and exits 0. The
longest, `global_search_demo.py`, runs in under ten seconds.

## Mastery checkpoint

Complete this without notes, using the demonstrations only to check arithmetic:

> A colleague inverts a 1-D profile with a nonlinear forward model and reports
> "converged". **(a)** They quote a final gradient norm of $10^{-3}$ but no
> Hessian. State the two things the number does *not* certify and the one
> quantity that would settle whether the point is a minimiser. **(b)** They now
> solve a large, poorly conditioned version with conjugate gradients and stop
> after 60 iterations because the residual is flat. From the semiconvergence
> table, state what is happening to the model error and the model norm, and the
> diagnostic that catches it. **(c)** They switch to a global search and report
> that annealing beat uniform sampling at $n=4$. State the measured result in
> sections 2 and 5 that makes this claim budget-dependent, and what a reader
> should ask for. **(d)** Finally they report a single best model. State why the
> answer to an inverse problem is a set, and the measurement of 07 §6 that
> demonstrates it.

Worked versions of (a)–(d) appear in the lesson solutions at ★★★ level.

## Common pitfalls across this module

1. **Treating "converged" as "solved".** Every stopped run in 07 §2 emits a
   convergence message; a loose $f$-tolerance stops the best-basin start on a
   point with Hessian eigenvalues $(-0.0018, 0)$, and the flat outer region has
   a degenerate Hessian for every rule. Report $\lVert\nabla f\rVert$, the
   Hessian eigenvalues and the termination message together.
2. **Reading a solver's rate off the textbook.** Gauss–Newton is quadratic only
   on a zero-residual problem; with $0.5\%$ noise it is linear and stops at the
   noise floor in four or five steps. The promised rate and the measured rate are
   different objects.
3. **Running an iterative solver to "convergence".** With a rank-deficient
   kernel the CG model error falls to $0.54$ and then rises to $10^{7}$ while the
   residual improves; the iteration index is a regularisation parameter, and a
   residual-only stopping rule fails catastrophically at $5\%$ noise.
4. **Comparing global methods by reputation.** At $n=4$ and 10000 evaluations,
   uniform sampling still succeeds 40% of the time while the annealer reaches 84%;
   the ordering is a property of the declared objective and the budget, not a
   universal law.
5. **Assuming more search is the answer.** The target volume falls about 50×
   per two dimensions, so the multi-start budget for 95% grows from 7 starts at
   $n=2$ to 148 at $n=6$; high-dimensional inversion has to exploit structure,
   not brute force.
6. **Quoting a best model as *the* model.** A $10^{-2}$ misfit tolerance already
   admits a near-equivalent set 0.29 km wide, and the two parameters are
   correlated ($-0.11$); an answer without its equivalence class is overclaimed.

## Related modules

- [18-01 Inverse Problem Foundations](../01-inverse-problem-foundations/README.md) —
  ill-posedness and the model–data mapping that make iteration necessary.
- [18-02 Linear Inverse Problems](../02-linear-inverse-problems/README.md) —
  the exact linear solution this module iterates towards.
- [18-03 Regularisation and Stabilisation](../03-regularization/README.md) —
  the penalties and parameter-choice rules that a nonlinear iteration reuses.
- [18-05 Bayesian Inversion and Inference](../05-bayesian-inversion/README.md) —
  the probabilistic answer to the non-uniqueness measured in lesson 07.
- [18-06 Uncertainty Quantification](../06-uncertainty-quantification/README.md) —
  how the linearised covariance and the equivalence class become error bars.
- [18-07 Joint and Multi-Physics Inversion](../07-joint-and-multi-physics-inversion/README.md) —
  the coupled objectives these local and global methods are asked to minimise.
- [01-14 Optimisation](../../01-mathematics/14-optimization/README.md) —
  the general optimisation theory behind the step rules of lesson 02.
- [05-03 Forward Modelling Principles](../../05-core-geophysics/03-forward-modelling-principles/README.md) —
  the forward models being inverted.
