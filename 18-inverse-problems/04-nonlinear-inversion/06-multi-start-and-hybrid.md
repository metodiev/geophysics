---
id: 18-04-06
title: "Multi-Start, Hybrid and Memetic Strategies"
level: research
prereqs: ["18-04-04", "18-04-05"]
tags: [inverse-problems, regularization, optimization, nonlinear-inversion, multi-start, hybrid, memetic]
---

# Multi-Start, Hybrid and Memetic Strategies

## Learning objectives

1. **Derive** the multi-start success law $1-(1-p)^{k}$ from independence of starts and **compute** the budget for a stated success probability.
2. **Measure** the single-start success probability $p$ of a local search on a declared multi-modal objective and **relate** it to the basin volume fraction.
3. **Explain** why $p$ is smaller than the basin volume when a tilt can pull a local search out of its basin, and **measure** both numbers.
4. **Test** the multi-start law against trials and **report** the residual gap together with the sampling error on $p$.
5. **Construct** a coarse-to-fine (hybrid) strategy and **compare** its cost and success with pure multi-start and with annealing at equal budget.
6. **Measure** how $p$ falls with dimension and **compute** the resulting budget growth per parameter.
7. **State** the assumptions under which the multi-start law holds and the ways in which a real misfit surface violates them.

## Prerequisites

- [Global Search: Monte Carlo, Simulated Annealing, Genetic Algorithms](04-global-search.md) — basin and tolerance volumes, and the budget arithmetic reused here.
- [Neighbourhood and Very Fast Simulated Annealing](05-neighbourhood-algorithms.md) — the alternative to multi-start that the hybrid strategy borrows from.
- [Gradient, Gauss-Newton and Full Newton Methods](02-gradient-and-newton.md) — the local search that each start runs.

All models and data in this module are SYNTHETIC.

## 1. The strategy and its arithmetic

Multi-start is the simplest hybrid: run a local optimiser from $k$ independent random starts and keep the best result. If one start finds the global minimum with probability $p$ independently of the others, the probability that at least one of $k$ starts does is

$$
P_k = 1 - (1-p)^{k} .
\tag{1.1}
$$

Inverting (1.1) gives the budget rule used throughout practice:

$$
k(P) = \frac{\ln(1-P)}{\ln(1-p)} .
\tag{1.2}
$$

For $P = 0.95$ and $p = 0.122$ (measured below) this gives

$$
k = \frac{\ln 0.05}{\ln 0.878} = \frac{-2.9957}{-0.13014} = 23.0 ,
\tag{1.3}
$$

so 23 starts buy a 95% chance. The whole method therefore reduces to one measurable number, $p$, and to the two assumptions behind (1.1): independence of starts, and a $p$ that does not depend on which starts have already been tried.

## 2. The objective and the measured $p$

The demo `code/multistart_hybrid_demo.py` uses

$$
f(u) = 1 - \sum_{k=1}^{5} d_k \exp\!\left(-\frac{\lVert u - c_k\rVert^{2}}{2\cdot0.30^{2}}\right) + 0.05\, t^{\mathsf T}u ,
\tag{2.1}
$$

five wells of depths 1.00 to 0.60 on the box $[-1,1]^{n}$, with a local search that is L-BFGS-B with an analytic gradient. The bound is not cosmetic: the tilt makes (2.1) unbounded below outside the box, so an unbounded local search diverges rather than finding a minimum. Measured:

```
  reference global minimum, n = 2: f = -0.635366
  reference global minimum, n = 4: f = -0.000807
  success tolerance: final f within 0.05 of the reference minimum.

   n   starts   starts reaching the global basin   measured p   basin volume fraction
   2       400                                  150        0.375                  0.2014
   4       400                                   49        0.122                  0.1482
```

At $n = 4$, $p = 0.122$ is *below* the basin volume fraction 0.1482, and at $n = 2$ it is *above* it (0.375 against 0.2014). The two discrepancies have the two mechanisms named in the demo: a start inside the global basin can be pulled out of it by the tilt, which lowers $p$; and a start outside it can walk in along the tilt, which raises it. The measured near-equality at $n = 2$ is therefore a coincidence of the two effects, not a law. What is a law is (1.1), given $p$.

## 3. The law tested against trials

The law is checked at $n = 4$ with 200 trials per value of $k$:

```
   k starts   measured success   predicted 1-(1-p)^k   difference
          1              0.150                 0.123        0.027
          2              0.175                 0.230       -0.055
          3              0.270                 0.324       -0.054
          4              0.335                 0.407       -0.072
          6              0.565                 0.543        0.022
```

The measured column is monotone in $k$, as (1.1) requires, and tracks the prediction to within about two standard errors (the 200-trial standard error is at most 0.035). The residuals at $k = 2$ to 4 are negative and the leading explanation is the sampling error on $p$ itself: the demo measured $p = 0.122$ from 400 starts, whose standard error is $\sqrt{0.122\cdot0.878/400} = 0.016$. A budget read from a measured $p$ therefore has to carry that error, not only the closed form.

## 4. A worked budget comparison

Three strategies at a common target of 95% success:

```
   strategy              local searches   forward evaluations (median)   success over 25 runs
   multi-start BFGS                       23                            310                 0.96
   annealing                               -                           4000                 0.12
   hybrid: 2000 samples + 5 polish                -                           2043                 0.92
```

The arithmetic behind the multi-start row is (1.3) with the measured $p$: 23 starts, and the median cost per start is $310/23 = 13.5$ forward evaluations, so the whole strategy costs 310 evaluations. The hybrid row spends 2000 samples of a cheap global stage and then 5 local polishes of about 9 evaluations each, for 2043 evaluations and a 0.92 success rate. Annealing at 4000 evaluations reaches only 0.12 here, because the schedule of lesson 18-04-04 was not long enough for this objective; the demo prints its own schedule parameters so the comparison can be audited.

The honest reading of the table is that a well-implemented multi-start with a measured $p$ is the cheapest route to a high success rate *on this declared objective*, and that the cost of a local search is what makes it cheap: 13.5 evaluations per polish against 4000 for the annealer. On a real problem where one forward evaluation is expensive and the misfit has thousands of local minima, the ranking can invert, and only a measurement with the real forward operator can decide.

## 5. How the budget grows with dimension

```
   n   measured p (100 starts)   predicted starts for 95%
   2                        0.350                          7
   4                        0.090                         32
   6                        0.020                        148
```

The 95% budget grows by roughly a factor of two per added parameter at these well radii, so $n = 10$ asks for thousands of local searches and $n = 20$ for millions; and each local search costs forward evaluations. This is the quantitative form of the curse of dimensionality already met in [Global Search](04-global-search.md), now expressed in the currency of starts. Multi-start is a good strategy at small $n$, a usable one at moderate $n$, and a hopeless one at large $n$; the crossover is measured, and the measurement is cheap.

## 6. What makes it memetic

A memetic algorithm adds local improvement to a population method, i.e. it is a hybrid in the sense of Section 4 with several parents. The measured comparison shows why the local stage matters: a population method with a $10^{3}$-evaluation budget improves its best model very little compared with 13.5 evaluations of a local polish applied to the best few samples. The two ingredients have different jobs — the population finds promising regions, the polish resolves them — and a hybrid that spends its budget on both in the right proportion beats either alone at equal cost. The proportion is a tuning parameter with no universal value, and the demo's choice (2000 samples, 5 polishes) is declared as such.

## 7. Assumptions and regime of validity

- **Starts are independent and identically distributed.** If starts are drawn by a stratified or Latin-hypercube rule, they are negatively correlated and (1.1) is conservative; the measured success then exceeds the prediction, which is a testable signature.
- **$p$ does not drift within a run.** A local search that adapts its own tolerances changes $p$ between starts; the demo uses a fixed configuration for that reason.
- **Box bounds are physical.** The measured divergence outside the box is a modelling error, not an algorithmic one; parameters that cannot be negative or cannot exceed a depth must be bounded.
- **The success tolerance is declared.** Every rate above is defined at $\tau = 0.05$ on a dimensionless misfit. Raising $\tau$ raises $p$ and shortens the budget nonlinearly.
- **The reference minimum is known.** On real data $p$ can only be estimated from the fraction of starts that reach the best value found, which is an upper bound on the true $p$ and biases (1.2) optimistically.

## Mastery checkpoint

1. Derive (1.1) and (1.2) and reproduce the arithmetic of (1.3) with the measured $p$.
2. From the 400-start measurement, compute the standard error of $p$ and the resulting uncertainty on the 23-start budget.
3. Explain the two mechanisms by which $p$ can differ from the basin volume fraction, and say which dominates at $n = 4$ in the measured data.
4. Reproduce the evaluation arithmetic in the multi-start row of Section 4.
5. Compute the budget for 95% success at $n = 6$ from the measured $p$ and check it against the printed value.
6. Design an experiment to test the independence assumption, and state what correlation would do to the measured success.

## Common pitfalls

- **Assuming $p$ equals the basin volume fraction.** Measured, it does not, and the sign of the difference changed with dimension.
- **Budgeting from a single-start run.** One start measures $p$ with an error of about $\sqrt{p(1-p)}$, which at $p = 0.12$ is 0.32 — useless.
- **Letting the local search run unbounded.** The measured divergence is a modelling error that shows up as a nonsensically low objective.
- **Comparing a hybrid with a pure method without equalising evaluations.** Both rows of Section 4 print their evaluation counts.
- **Extrapolating the law with a fixed $p$.** Section 5 shows $p$ falling tenfold between $n = 2$ and $n = 6$.

## Related modules

- [Global Search: Monte Carlo, Simulated Annealing, Genetic Algorithms](04-global-search.md) — the sampling arithmetic this lesson specialises.
- [Neighbourhood and Very Fast Simulated Annealing](05-neighbourhood-algorithms.md) — the learned-proposal alternative to independent starts.
- [Convergence Diagnosis and Local-Minimum Traps](07-convergence-and-local-minima.md) — how to check that the best of $k$ starts is a minimum at all.

## Materials

- Demo: `code/multistart_hybrid_demo.py` (print-only, about 3 s, exit 0).
- Exercises: `exercises/06-multi-start-and-hybrid-exercises.md` with solutions in `exercises/06-multi-start-and-hybrid-solutions.md`.

All models and data in this module are SYNTHETIC.
