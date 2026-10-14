# Module 01-14 — Optimization and Variational Methods

**Stage:** advanced → graduate · **Prerequisites:**
[01 Convexity, Stationarity and Optimality Conditions](./01-convexity.md) is this
module's own foundation, and it in turn needs
[07 Linear Algebra](../07-linear-algebra/README.md) (positive definiteness,
eigenvalues, the SVD),
[12 Numerical Methods](../12-numerical-methods/README.md) (linear solvers,
conditioning and the root-finding inside every descent step) and
[06 Multivariable and Vector Calculus](../06-multivariable-calculus/README.md)
(gradients, Hessians, integration by parts).

Every geophysical measurement is an inverse problem, and every inverse problem
that is not solved in closed form is solved by **optimisation**. This module is the
mathematics of that step: what a minimum *is*, how to reach one, when the one you
reached is the wrong one, and what the answer's uncertainty has to do with the
curvature you walked through to get there.

The organising idea is that two questions decide every algorithm and they must be
answered separately:

> **Is the objective convex, and is the problem well conditioned?** Convexity says
> there is one answer and any descent method finds it. Conditioning says how many
> digits of that answer you can actually compute.

The module is built so that each lesson answers one question a practitioner
actually asks.

| Lesson | The question it answers | The number that decides |
|---|---|---|
| 01 Convexity | Is there one answer, or several? | the curvature $\nabla^{2}\phi$ and its positive definiteness |
| 02 Unconstrained | How do I walk downhill efficiently? | the Hessian's condition number, and the BFGS memory |
| 03 Constrained | What does a constraint cost? | the multiplier $\lambda$, in misfit per unit of constraint |
| 04 Least squares | What is the workhorse, and where does it fail? | $\kappa(G)$, and $\kappa^{2}$ for the normal equations |
| 05 Global optimisation | The minimum is not always the model — what then? | the success rate per budget, and the aliasing period |
| 06 Variational calculus | How do I optimise over functions? | the mesh's $\kappa\sim h^{-2}$ against its $O(h^{2})$ accuracy |
| 07 Linear programming | When is the answer a decision list? | the shadow price of each specification |

Each lesson states the assumptions its methods need before applying them, and
every number in the module was produced by a script in `code/` that uses the Python
standard library only — including exact rational arithmetic for the linear-programming
results, so that "optimal" is a certificate rather than a tolerance.

## Learning objectives

By the end of this module you will be able to:

1. **Decide** whether a misfit is convex, and use stationarity plus curvature to
   classify a stationary point as a minimum, maximum or saddle, including the
   degenerate cases where the second-order test is inconclusive.
2. **Choose** a descent method — steepest descent, Newton, Gauss–Newton,
   quasi-Newton, conjugate gradient — from the cost of a gradient and the
   conditioning of the problem, and predict its convergence rate before running it.
3. **State** the KKT conditions for a constrained problem, interpret every
   multiplier as a price, and use complementarity to say which constraints bind.
4. **Derive** the normal equations three ways, explain why $\kappa(G^{\mathsf T}G)
   = \kappa(G)^{2}$ makes the textbook route numerically wrong for ill-conditioned
   kernels, and choose between normal equations, QR and the SVD on the evidence.
5. **Implement** Gauss–Newton and Levenberg–Marquardt, bound the step with a trust
   region, and diagnose the three standard failures: a singular $J^{\mathsf T}J$, an
   unbounded step, and convergence to a wrong local minimum.
6. **Report** the output of a global search as a distribution — seeds, budget,
   success rate, best-so-far — and distinguish "found the global minimum of the
   misfit" from "recovered the model", giving a geophysical example of each.
7. **Derive** the Euler–Lagrange equation including its boundary term, decide
   whether a boundary condition is imposed or natural, and discretise a functional
   directly rather than discretising its equation.
8. **Cast** an L1 or Chebyshev fit and an allocation problem as linear programs,
   read the dual as a price list, and verify a shadow price by differentiating the
   optimal value.

## Lessons

| # | Lesson | Level | Key idea |
|---|---|---|---|
| 01 | [Convexity, Stationarity and Optimality Conditions](./01-convexity.md) | advanced | Convexity is what makes an answer *the* answer, and curvature is what makes it *computable* |
| 02 | [Unconstrained Minimisation: Gradient, Newton, Quasi-Newton](./02-unconstrained.md) | advanced | Newton is the fastest method you cannot afford; quasi-Newton is the one you can |
| 03 | [Constrained Optimisation and Lagrange Multipliers](./03-constrained.md) | advanced | A constraint is not a nuisance but a price, and KKT conditions are the exchange rate |
| 04 | [Linear and Nonlinear Least Squares](./04-least-squares.md) | advanced | The derivation gives the normal equations and the conditioning forbids them |
| 05 | [Global Optimisation: Simulated Annealing, Genetic Algorithms](./05-global-optimization.md) | graduate | The global minimum of the misfit need not be the Earth |
| 06 | [Calculus of Variations and Its Geophysical Uses](./06-variational-calculus.md) | graduate | Discretise the energy, not the equation, and the boundary conditions come free |
| 07 | [Linear Programming and Geophysical Applications](./07-linear-programming.md) | graduate | When the objective is linear the optimum is a vertex, and optimality comes with a certificate |

## Suggested path

**If you are following the mathematics folder in order:** lessons 01–04 are the
advanced core and take roughly 14 hours with the exercises. They are the
prerequisite for essentially all numerical geophysics: nothing in
[18 Inverse Problems](../../18-inverse-problems/README.md) makes sense without
lesson 04 in particular. Lessons 05–07 are graduate material and take another
12 hours; they can be read in any order, but 05 and 07 build on 03 and 04.

**If you are here from a geophysics application:**

| You are working on | Read |
|---|---|
| Travel-time or waveform inversion | [04](./04-least-squares.md) in full, then [02](./02-unconstrained.md) §4–5 |
| Potential-field inversion and depth–amplitude trade-offs | [04](./04-least-squares.md) §4.2–4.5, [05](./05-global-optimization.md) §3.2 |
| Refraction, surface-wave or MT inversion with several basins | [05](./05-global-optimization.md) in full |
| Bounded model parameters, damping and priors | [03](./03-constrained.md) in full, [04](./04-least-squares.md) §6 |
| Flexure, free-surface and geoid problems | [06](./06-variational-calculus.md) §3.2, §4 |
| 4D-Var and adjoint data assimilation | [06](./06-variational-calculus.md) §2.3, §10 |
| Robust trend fitting on profiles with blunders | [07](./07-linear-programming.md) §4.2–4.3 |
| Mixture, blending and resource-allocation problems | [07](./07-linear-programming.md) §3.4, §4.1 |
| Survey design and resolution analysis | [04](./04-least-squares.md) §4.3, [05](./05-global-optimization.md) §4.8 |

**If you already run inversions professionally:** attempt ★★★9 of
[04](./04-least-squares.md) and ★★★9 of [05](./05-global-optimization.md). If the
conditioning argument and the arguments-model distinction both come out cleanly,
use this module as a reference and go to
[18 Inverse Problems](../../18-inverse-problems/README.md) for the appraisal
machinery that goes beyond finding one model.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-convexity.md`](./01-convexity.md) … [`07-linear-programming.md`](./07-linear-programming.md) | The seven lessons |
| [`exercises/`](./exercises) | One exercise set and one worked solution set per lesson, graded ★ to ★★★ |
| [`code/convexity_demo.py`](./code/convexity_demo.py) | Curvature along random directions, the second-order test at a degenerate point, and the gap between convexity and numerical conditioning |
| [`code/unconstrained_demo.py`](./code/unconstrained_demo.py) | Steepest descent, Newton, BFGS and nonlinear conjugate gradient on a quadratic and on the Rosenbrock valley; measured iteration counts against the condition number |
| [`code/constrained_demo.py`](./code/constrained_demo.py) | Equality and inequality constraints, KKT residuals, active-set behaviour and multipliers verified against finite differences |
| [`code/least_squares_demo.py`](./code/least_squares_demo.py) | Normal equations versus Householder QR with exact rational reference solutions; Gauss–Newton and Levenberg–Marquardt on a gravity profile; weighting; an outlier and a leverage study |
| [`code/global_optimization_demo.py`](./code/global_optimization_demo.py) | Basin counting by restarted descent, simulated annealing with a cooling schedule, a genetic algorithm, and the aliasing family of a cycle-skipped misfit |
| [`code/variational_calculus_demo.py`](./code/variational_calculus_demo.py) | The direct method with a measured convergence order, a numerical first variation, a free end with an emergent natural condition, a Rayleigh quotient, and the conditioning price of refinement |
| [`code/linear_programming_demo.py`](./code/linear_programming_demo.py) | A two-phase simplex in exact rational arithmetic; L1 and Chebyshev fits; strong duality; a shadow price verified by differentiation |

Every script runs with `python3 code/<script>.py` and imports nothing outside the
standard library. The numbers quoted in the lessons are the outputs of these
scripts.

## Mastery checkpoint

You have mastered this module when you can do all of the following unaided:

- [ ] State the first- and second-order optimality conditions, and give a function
      where the second-order test is inconclusive at a minimum you can identify.
- [ ] Explain what convexity buys — uniqueness, and that any local minimum is
      global — and say what it does *not* buy.
- [ ] Derive the Newton step from a second-order Taylor expansion and give the
      convergence rate, the cost per step, and the reason a quasi-Newton method is
      usually preferred.
- [ ] Write the KKT conditions for a problem with equality and inequality
      constraints, and interpret each multiplier as the price of its constraint.
- [ ] Derive the normal equations by differentiation and by projection, and explain
      the two ways they fail: rank deficiency and squared conditioning.
- [ ] Predict the numerical error of the normal-equation, QR and SVD routes from
      $\kappa$ and the unit round-off, and choose between them on evidence.
- [ ] Write a Gauss–Newton step, explain why its curvature model is $J^{\mathsf T}J$
      and not the true Hessian, and say when that difference stops being harmless.
- [ ] Explain Levenberg–Marquardt damping as a trust region, and say why the
      damping must be reduced rather than held fixed.
- [ ] Report a stochastic method's result as a distribution with a budget, and give
      a geophysical case where the global misfit minimum is not the true model.
- [ ] Derive the Euler–Lagrange equation including the boundary term, and say which
      end conditions are imposed and which become natural.
- [ ] Set up a linear program for an L1 or Chebyshev fit, state the dual, and verify
      a shadow price by differentiating the optimal value.

## Common pitfalls across this module

1. **Confusing a small misfit with a good model.** The residual measures
   $Gm - d$, not $m - m_{\text{true}}$; the gap is the condition number, and for
   the normal equations it is the *square* of the data condition number.
2. **Forming $G^{\mathsf T}G$ because the derivation produced it.** Measured:
   at $\kappa(G) = 4\times10^{8}$ the computed $G^{\mathsf T}G$ has determinant
   exactly zero and the normal-equation route fails, while QR still recovers both
   parameters to nine digits.
3. **Treating a global search as a way to remove ambiguity.** Measured on a
   cycle-skipped misfit: annealing found a zero-misfit model on 20 of 20 seeds and
   the *true* model on 2 of 20 — the search reports a distribution over the models
   the data admit, not the Earth.
4. **Reading a local method's answer as the answer.** A converged-looking run can
   be at $h = 1645$ where the truth is $h = 20$, because the residual can be made
   small in a flattened region of the misfit; bound the step and check the model.
5. **Dropping the boundary term of a first variation.** It is exactly where
   natural boundary conditions come from; dropping it silently imposes
   $\delta y = 0$ where the physics wants a free surface.
6. **Quoting an uncertainty without the residuals that calibrated it.** The scale
   factor comes from $\|r\|^{2}/(n-p)$, so $(J^{\mathsf T}J)^{-1}$ alone
   understates or overstates the error bars by that factor.
7. **Comparing L1 and L2 fits by their own cost.** Each is worse than the other by
   the other's measure; what is comparable is the sensitivity to a blunder, and the
   lesson measures that as a factor of 8.8.
8. **Trusting an LP solution from an infeasible or unbounded problem.** A solver
   must distinguish optimal, infeasible and unbounded, and say which it returned.
9. **Refining a variational discretisation for accuracy without watching
   conditioning.** Accuracy improves as $O(h^{2})$ while $\kappa$ degrades as
   $h^{-2}$; the crossover in binary64 is at about $10^{4}$ cells per unit length.
10. **Holding the Levenberg–Marquardt weight fixed.** The path is then a damped
    descent that converges slowly — measured as 295 iterations against 4 on a
    scalar problem — so the schedule, not the damping constant, is the method.

## Related modules

- [07 Linear Algebra](../07-linear-algebra/README.md) — the prerequisite: positive
  definiteness, eigenvalues, the SVD and the conditioning everything here depends
  on.
- [12 Numerical Methods](../12-numerical-methods/README.md) — the solvers inside
  every step of every method in this module, and the stability analysis that the
  global-optimisation lesson's schedules are a special case of.
- [06 Multivariable and Vector Calculus](../06-multivariable-calculus/README.md) —
  gradients, Hessians and the integration by parts that produces the natural
  boundary conditions of lesson 06.
- [13 Probability and Statistics Foundations](../13-probability-and-statistics-foundations/README.md)
  — the maximum-likelihood reading of least squares, and the covariance that comes
  out of the curvature.
- [18 Inverse Problems](../../18-inverse-problems/README.md) — where every idea in
  this module is used at scale, together with the appraisal tools (resolution
  matrices, null spaces, Bayesian sampling) that go beyond optimisation.
- [19 Numerical Modeling and HPC](../../19-numerical-modeling-hpc/README.md) — the
  large-scale setting: sparse Jacobians, adjoints and parallel evaluation of the
  objective.
- [05 Core Geophysics](../../05-core-geophysics/README.md) — the applications whose
  inversions these methods are designed for.
- [21 Statistics and Bayesian ML](../../21-statistics-bayesian-ml/README.md) — the
  same optimisers applied to machine-learning objectives, and the sampling
  alternative to a single optimum.
