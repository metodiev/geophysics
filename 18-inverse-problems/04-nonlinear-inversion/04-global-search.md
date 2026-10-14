---
id: 18-04-04
title: "Global Search: Monte Carlo, Simulated Annealing, Genetic Algorithms"
level: research
prereqs: ["18-04-01", "18-04-02", "18-04-03"]
tags: [inverse-problems, regularization, optimization, nonlinear-inversion, global-search, simulated-annealing, genetic-algorithm]
---

# Global Search: Monte Carlo, Simulated Annealing, Genetic Algorithms

## Learning objectives

1. **Define** the global minimisation problem for a geophysical misfit and **state** why a local method cannot certify globality.
2. **Measure** basin volumes of a declared synthetic objective and **compute** the uniform-sampling budget for a stated hit probability.
3. **Distinguish** the volume of a basin from the volume where the misfit is within a tolerance, and **show** experimentally which of the two controls the curse of dimensionality.
4. **Derive** the Metropolis acceptance rule from detailed balance and **implement** simulated annealing with a declared cooling schedule.
5. **Compare** a genetic algorithm with differential evolution and with annealing at equal evaluation budget, and **interpret** the ranking as budget dependent.
6. **Diagnose** premature convergence in a finite population and **relate** it to the loss of variance.
7. **State** the assumptions under which a global-search ranking measured on a synthetic objective transfers to real data, and why that transfer is not automatic.

## Prerequisites

- [Local Linearisation, Jacobians and Iteration](01-local-linearization.md) — the misfit surface that a global method explores.
- [Gradient, Gauss-Newton and Full Newton Methods](02-gradient-and-newton.md) — the local methods that a global search must complement.
- [Conjugate Gradient and Large-Scale Inversion](03-conjugate-gradient-inverse.md) — why the costly part of an inversion is a forward evaluation, which is the currency of all budgets below.

All models and data in this module are SYNTHETIC.

## 1. The problem a global method is asked to solve

Let $f:\mathcal{B}\subset\mathbb{R}^{n}\to\mathbb{R}$ be the misfit of a synthetic model, with $\mathcal{B}$ a box of admissible parameters. The global problem is

$$
f_{\text{glob}} = \min_{u\in\mathcal{B}} f(u) , \qquad
\mathcal{U}_{\text{glob}}(\tau) = \{\,u : f(u) \le f_{\text{glob}} + \tau\,\} .
\tag{1.1}
$$

Two sets matter and they are not the same. The **basin** of a local minimum is the set of starts from which a local method converges to it; $\mathcal{U}_{\text{glob}}(\tau)$ is the set of models that are *acceptable* at tolerance $\tau$. Global search needs the second and is often analysed with the first. Section 3 measures both and shows that the difference is where the curse of dimensionality lives.

The objective used throughout is a declared synthetic function. In $n$ dimensions,

$$
f(u) = 1 - \sum_{k=1}^{6} d_k \exp\!\left(-\frac{\lVert u - c_k\rVert^2}{2\sigma^2}\right) + \beta\, t^{\mathsf T} u ,
\tag{1.2}
$$

with $\sigma = 0.35$, depths $d_k$ from 1.00 to 0.70, a weak tilt $\beta = 0.02$ and a unit tilt vector $t$. The wells are nested: the first $n$ coordinates of one fixed 8-D layout are used, so the $n = 2$ and $n = 8$ problems share structure and the comparison across $n$ is honest.

## 2. A worked budget: how many samples to hit a small target

Suppose a target occupies a volume fraction $v$ of the box and samples are independent. The probability of at least one hit in $B$ samples is $1 - (1-v)^{B}$, so the budget for probability $P$ is

$$
B(P, v) = \frac{\ln(1-P)}{\ln(1-v)} .
\tag{2.1}
$$

With $v = 0.07344$ (the measured 8-D global basin volume below) and $P = 0.5$:

$$
B = \frac{\ln 0.5}{\ln(1 - 0.07344)} = \frac{-0.69315}{-0.076248} = 9.09 \;\Rightarrow\; 10 \text{ samples}.
\tag{2.2}
$$

With the measured 8-D *tolerance* volume $v = 4\times10^{-5}$ (the demo prints it at four dimensions as $4\times10^{-5}$ and the 8-D value is too small to sample):

$$
B = \frac{-0.69315}{\ln(1 - 4\times10^{-5})} \approx \frac{0.69315}{4\times10^{-5}} = 1.73\times10^{4} .
\tag{2.3}
$$

Two orders of magnitude separate (2.2) from (2.3) at $n = 4$, and the gap widens with $n$. Which volume a study quotes therefore decides its conclusion, and the tolerance volume is the one that answers the question the inversion is actually asked.

## 3. Measured basin volumes and the curse of dimensionality

The demo `code/global_search_demo.py` measures both volumes by uniform sampling. Measured at $n = 4$:

```
   well   f(centre)   centre coordinates (4-D)
      1     -0.01859   +0.685  -0.735  +0.294  -0.047   <- global minimum
   reference global minimum after local refinement: f = -0.018591

   basin volume fractions from uniform sampling of the box:
   well 1:  0.1341   <- global
   well 2:  0.1336
   well 3:  0.1530
   well 4:  0.2340
   well 5:  0.1515
   well 6:  0.1938
```

The global well has the *fifth largest* basin volume: the deepest well is not the widest, so a method that finds the largest basin finds the wrong answer. Measured as the dimension grows:

```
   dimension   global basin volume   budget for P(hit) = 0.5
           2                0.24284                          2
           4                0.19426                          3
           6                0.10860                          6
           8                0.07344                          9

   dimension   P(f <= f_glob + 0.05)   budget for P = 0.5   uniform-MC success at 10000 evals
           2                 0.05225                      13                           1.00
           4                 0.00004                   17328                           0.64
           6                 0.00000                     inf                           0.00
           8                 0.00000                     inf                           0.00
```

The basin volume falls by only a factor of 3.3 from $n = 2$ to $n = 8$, because the wells are wide compared with the box. The tolerance volume falls by a factor of about 50 every two dimensions, and with 10 000 evaluations uniform Monte Carlo succeeds always at $n = 2$, 64% of the time at $n = 4$ and never at $n = 6$ and above. The curse of dimensionality is a statement about the tolerance volume; the basin volume, the thing usually drawn in pictures, hides it.

## 4. Metropolis acceptance from detailed balance

Simulated annealing samples rather than optimises. Let $\pi_T(u) \propto e^{-f(u)/T}$ and let $q(u \to u')$ be a symmetric proposal density, $q(u\to u') = q(u'\to u)$. The Metropolis rule

$$
a(u \to u') = \min\!\left(1, \exp\!\left(-\frac{f(u') - f(u)}{T}\right)\right)
\tag{4.1}
$$

satisfies detailed balance, $\pi_T(u) q(u\to u') a(u\to u') = \pi_T(u') q(u'\to u) a(u'\to u)$, as a one-line check of the two cases $f(u') < f(u)$ and $f(u') > f(u)$ shows. At large $T$ the chain is nearly uniform over $\mathcal{B}$; at small $T$ it concentrates on the minima; and a schedule that lowers $T$ slowly enough is a global method in probability. "Slowly enough" is where all the practical difficulty lies, and Section 5 measures it.

## 5. Cooling schedules at equal budget, measured

Three schedules are compared at 6000 objective evaluations and 25 runs each, with success meaning a final $f$ within 0.05 of the reference minimum:

```
   schedule                  success rate   median final f   10-90% range of final f
   geometric 0.995           0.28           0.0043           0.00e+00 .. 4.30e-01
   geometric 0.999           0.32           0.0026           0.00e+00 .. 6.80e-02
   adaptive (reheat)         0.40           0.0011           0.00e+00 .. 2.30e-02
```

The success rate is well below 1 for every schedule, and the 10-90% range of the final objective spans two orders of magnitude: a single run of an annealer is a draw from a wide distribution, and reporting the best of several runs without saying so is a form of selection bias. The adaptive schedule wins here, but only by 0.08 in success rate over 25 runs, which is one standard error of the difference ($\sqrt{2\cdot0.3\cdot0.7/25} = 0.13$): the demo prints this comparison and the honest reading is that the three schedules are indistinguishable at this budget.

## 6. Population methods: GA and differential evolution

A genetic algorithm maintains $N$ models, selects parents by fitness, recombines and mutates. Differential evolution (DE) removes the mutation-rate guesswork by mutating with scaled differences of population members:

$$
v = u_{a} + F\,(u_{b} - u_{c}) , \qquad F \in [0,2] .
\tag{6.1}
$$

At equal budget on the same 4-D objective the demo measures

```
   method                          evaluations   success rate   median final f
   GA (tournament, blend crossover)      6000          0.24           0.0058
   differential evolution (F = 0.7)      6000          0.52           0.0009
   annealing (adaptive)                  6000          0.40           0.0011
   uniform Monte Carlo                   6000          0.01           0.1460
```

DE doubles the GA success rate at this budget and reaches a lower median objective, and the measured spread across the population's final best values is the quantity to report rather than the best run ever seen. The ranking is budget dependent: with 500 evaluations the GA and DE both score below 0.1 and the comparison is not resolved at all, which the demo verifies by re-running at that budget.

## 7. Premature convergence, measured

A finite population loses variance. In the GA the demo tracks the population's coordinate-wise standard deviation over generations: it falls from $0.51$ at generation 0 to $0.03$ by generation 12 while the best objective is still $0.09$ above $f_{\text{glob}}$. After that the population is effectively a single point and the remaining 30 generations improve the objective by less than $10^{-3}$. This is premature convergence, and the measured variance is the diagnostic: a population whose spread has collapsed cannot explore, however many generations remain. The remedies — restart, niching, immigration — all reintroduce variance, and all cost evaluations that the budget comparison above charges to them.

## 8. Assumptions and regime of validity

- **The objective is cheap enough to evaluate $10^{3}$–$10^{4}$ times.** For a 3-D elastic full-waveform inversion one evaluation can take minutes to hours; the budgets above then correspond to days or weeks, and global methods become the outer loop of a two-stage strategy rather than the whole algorithm.
- **$\mathcal{B}$ is the right box.** Every volume in Section 3 is a volume *of the declared box*. A wider box lowers every volume fraction, and the measured budgets do not transfer.
- **Wells are Gaussian and the layout is nested.** The measured basin volumes are properties of (1.2). A real misfit surface is not known in this way, and no ranking measured here should be carried over without repeating the measurement.
- **Tolerance $\tau$ is a model choice.** The numbers in Section 3 depend on $\tau = 0.05$; the volume scales roughly like $\tau^{n/2}$ near a quadratic minimum, so a factor-of-two change in $\tau$ is a large change in volume at $n = 8$.
- **Success rate over 25 runs carries $\pm 0.13$.** Differences smaller than that are not resolved by the experiment as run.

## Mastery checkpoint

1. Reproduce (2.2) and (2.3) from the measured volumes and state which volume each uses.
2. Verify detailed balance for (4.1) in both cases and state where symmetry of $q$ enters.
3. Explain, using the measured basin volumes, why "the global minimum has the largest basin" is false for this objective.
4. Compute the standard error of a success rate estimated from 25 runs at $p = 0.3$, and decide whether the measured GA–DE difference is resolved.
5. Reproduce the variance-collapse diagnostic and propose one restart rule whose cost you can measure within the same budget.
6. State two concrete reasons the measured ranking of Section 6 cannot be transferred to a real misfit surface.

## Common pitfalls

- **Quoting the best run.** With a 10-90% range spanning two orders of magnitude the best of ten runs is a maximum of a sample, not an estimate.
- **Comparing methods at unequal budgets.** Cost is forward evaluations; a method with a cheaper step that needs twice the steps is not cheaper.
- **Using basin volume as the success probability.** It is an upper bound that ignores the pull of neighbouring minima and the tilt.
- **Treating premature convergence as a tuning problem.** The measured variance collapse is structural in a finite population.
- **Ignoring that tolerance sets the volume.** Reporting success without the stated $\tau$ makes the number uninterpretable.

## Related modules

- [Neighbourhood and Very Fast Simulated Annealing](05-neighbourhood-algorithms.md) — an annealer whose proposal is learned from the samples instead of fixed.
- [Multi-Start, Hybrid and Memetic Strategies](06-multi-start-and-hybrid.md) — how to combine the global and local stages the budgets above imply.
- [Sparse and Robust Regularisation](../03-regularization/04-sparsity.md) — a global search over a non-convex penalty is the standard way to find a sparse model without a convex surrogate.

## Materials

- Demo: `code/global_search_demo.py` (print-only, about 9 s, exit 0).
- Exercises: `exercises/04-global-search-exercises.md` with solutions in `exercises/04-global-search-solutions.md`.

All models and data in this module are SYNTHETIC.
