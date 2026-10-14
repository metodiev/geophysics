---
id: 18-04-05
title: "Neighbourhood and Very Fast Simulated Annealing"
level: research
prereqs: ["18-04-03", "18-04-04"]
tags: [inverse-problems, regularization, optimization, nonlinear-inversion, neighbourhood-algorithm, simulated-annealing, global-search]
---

# Neighbourhood and Very Fast Simulated Annealing

## Learning objectives

1. **Describe** the neighbourhood algorithm as sampling inside the Voronoi cell of the current best model and **derive** the cell's inscribed ball.
2. **Measure** the contraction of the inscribed radius and the acceptance fraction over generations, and **explain** the two competing effects.
3. **Diagnose** premature collapse: a naive neighbourhood search that pays for its contraction with a worse answer than plain sampling at equal cost.
4. **Derive** the very fast simulated annealing (VFSA) Cauchy proposal and **explain** why a heavy-tailed proposal outperforms a Gaussian one at low temperature.
5. **Measure** a VFSA success rate against budget and cooling constant and **quantify** the run-to-run spread.
6. **Compare** the neighbourhood and VFSA strategies at equal evaluation budget and **state** which quantity makes the comparison fair.
7. **State** the assumptions under which the measured contraction and success rates transfer to a real misfit surface.

## Prerequisites

- [Conjugate Gradient and Large-Scale Inversion](03-conjugate-gradient-inverse.md) — the local solver that either strategy must eventually hand its best model to.
- [Global Search: Monte Carlo, Simulated Annealing, Genetic Algorithms](04-global-search.md) — basin and tolerance volumes, the sampling budgets, and the Metropolis rule used again here.

All models and data in this module are SYNTHETIC.

## 1. The objective and the reference answer

Both algorithms are applied to

$$
f(u) = 1 - \sum_{k=1}^{5} d_k \exp\!\left(-\frac{\lVert u - c_k\rVert^{2}}{2\sigma^{2}}\right) + \beta\, t^{\mathsf T}u ,
\qquad \sigma = 0.30,\quad \beta = 0.05 ,
\tag{1.1}
$$

with five wells of depths 1.00 to 0.60, laid out so that the first $n$ coordinates of one fixed 4-D set give the $n$-dimensional problem. The demo `code/neighbourhood_annealing_demo.py` first finds the reference minimum by a dense local search and reports it as measured:

```
  reference global minimum, n = 2: f = -0.832720
  reference global minimum, n = 4: f = -0.012397
  success tolerance: final f within 0.05 of the reference minimum.
  DECLARED synthetic function: no ranking below should be transferred to
  a real misfit surface without repeating the measurement.
```

All success rates below are relative to that declared reference and that declared tolerance.

## 2. The neighbourhood algorithm and its inscribed ball

The neighbourhood algorithm (NA) keeps a set of evaluated models. It chooses one model as the current best, constructs the Voronoi cell of that model with respect to all evaluated samples, and draws new models uniformly inside that cell. The effect is a sampling density that concentrates automatically where the best model is.

Drawing uniformly inside a Voronoi cell is not cheap in high dimensions, so the demo uses the ball inscribed in the cell: if the best model has nearest sample neighbour at distance $r_1$, the ball of radius

$$
r_{\text{ins}} = \tfrac12 \min_{j \neq \text{best}} \lVert u_{\text{best}} - u_j \rVert
\tag{2.1}
$$

lies entirely inside the cell, so sampling inside it is both valid and cheap. Its volume fraction relative to the box $[-1,1]^{n}$ is

$$
\frac{V_{\text{ball}}}{V_{\text{box}}} = \frac{\pi^{n/2}}{2^{n}\,\Gamma(n/2 + 1)}\; r_{\text{ins}}^{\,n} .
\tag{2.2}
$$

Measured for one run at $n = 2$ with 640 evaluations and 39 generations:

```
   generation   inscribed radius   ball volume / box volume
            1           0.137896                  1.493e-02
            2           0.019011                  2.839e-04
            5           0.000101                  8.050e-09
           10           0.000000                  2.281e-16
           20           0.000000                  2.025e-20
           39           0.000000                  4.831e-21

   generation   measured acceptance fraction   inscribed radius
            1                        0.02900           0.137896
           10                        0.01900           0.000000
```

The contraction is violent: the inscribed radius falls from 0.138 to $1.0\times10^{-4}$ in four generations, and the volume fraction falls by seven orders of magnitude in the same time. Yet the measured acceptance fraction barely changes, from 0.029 to 0.019. The reason is that the cell keeps its *orientation* relative to the unknown good direction: once the best model sits in a bad region, the samples continue to be drawn around it, and the acceptance rate is dominated by whether the local region has any improvement left, not by the radius.

## 3. The failure mode: premature collapse, measured

The same run finishes at

```
  best value found = -0.375501 against the reference -0.832720
```

That is 0.46 above the reference, i.e. nine times the success tolerance, and worse than a plain random search of the same cost on this objective. The mechanism is visible in Section 2: having committed to the best of a 16-point initial sample, the search never revisits that commitment. This is the honest difficulty of the family — the contraction is what makes NA fast where it works and is exactly what makes it brittle where it fails — and the demo prints it rather than a hand-picked good run.

The standard remedies all cost evaluations: a larger initial sample, simultaneous treatment of several cells (rescaling each cell's sampling rate), or an explicit restart when the acceptance fraction falls below a threshold for a stated number of generations. Any of them can be implemented and measured with the same harness, and the measurement, not the algorithm's reputation, should decide.

## 4. Very fast simulated annealing: the Cauchy proposal

VFSA keeps the Metropolis acceptance rule of [Global Search](04-global-search.md) but replaces the proposal. With temperature $T_k$ at step $k$, the proposal for each coordinate is

$$
\Delta u_i = \mathrm{sgn}(r_i - 0.5)\, T_k \left[\left(1 + \frac{1}{T_k}\right)^{\lvert 2 r_i - 1 \rvert} - 1\right] ,
\qquad r_i \sim U(0,1) ,
\tag{4.1}
$$

with temperature

$$
T_k = T_0\, c^{k} .
\tag{4.2}
$$

The distribution of $\Delta u_i$ at fixed $T_k$ is a Cauchy-like heavy-tailed law: as $T_k \to 0$ the exponent $1 + 1/T_k$ grows, so the proposal becomes very local for most draws while still allowing rare long jumps. That is the difference from a Gaussian proposal, whose tails are thin: at low temperature a Gaussian chain cannot leave a basin at all, whereas a Cauchy chain can, and the acceptance probability of a long jump is set by the Metropolis ratio rather than by the proposal.

## 5. A worked acceptance calculation

Take $T = 0.5$, and consider a proposal that raises the objective by $\Delta f = 0.4$. The acceptance probability is

$$
a = \exp\!\left(-\frac{0.4}{0.5}\right) = e^{-0.8} = 0.4493 .
\tag{5.1}
$$

At $T = 0.05$ the same worsening is accepted with probability

$$
a = \exp\!\left(-\frac{0.4}{0.05}\right) = e^{-8} = 3.355\times10^{-4} .
\tag{5.2}
$$

So a schedule that cools by a factor of ten changes an uphill move's acceptance probability by a factor $e^{7.2} = 1339$. That is the mechanism by which the temperature controls whether the chain explores or exploits, and it is why (4.2) is the only real tuning knob in the method. The demo's cooling constant $c = 0.995$ with $T_0 = 0.5$ means the temperature reaches $0.05$ after $k = \ln(0.1)/\ln(0.995) = 459$ steps.

## 6. Measured success against budget

VFSA is run 8 times per budget on the same objective, and success is again a final $f$ within 0.05 of the reference:

```
   budget   success rate over 8 runs   median final f   median distance to the global well
     1000                       0.50           0.046261                            0.4688
     4000                       0.25           0.099863                            1.1832
```

The larger budget scores *worse*. With 8 runs the standard error of a success rate near 0.4 is 0.17, so 0.50 against 0.25 is not a resolved difference; the median final $f$ does fall and the median distance to the global well rises, which is what a longer cooling schedule at a fixed starting temperature does: more steps at high temperature means more wandering, and if the schedule is not long enough to cool again afterwards the run ends far from any well. Reporting this rather than hiding it is the point: at these budgets the VFSA implementation is not reliable, and the measured spread is the evidence.

## 7. Ranking the two strategies at equal cost

```
   method                                  evaluations   success rate over 12 runs   median final f
   neighbourhood algorithm (640 evals)             640          0.25                       -0.3755
   VFSA (1000 evals, T0 = 0.5, c = 0.995)         1000          0.50                        0.0463
   uniform Monte Carlo (1000 evals)               1000          0.17                        0.3100
```

At these tiny budgets both structured methods beat uniform sampling, the NA implementation is the worst of the three structured options because of the collapse of Section 3, and every success rate carries an uncertainty larger than the gaps between rows. The comparison is fair only because it is made at equal evaluation count, and the count is the currency; the demo prints the evaluation count of every row for that reason.

## 8. Assumptions and regime of validity

- **Small dimension and small budget.** These measurements are at $n = 2$ and $n = 4$ with hundreds to thousands of evaluations. The inscribed-ball fraction (2.2) falls like $r^{n}$ and like $\Gamma(n/2+1)^{-1}$, so at $n = 20$ the ball is a hopeless proxy for the cell and the naive NA is expected to fail harder than measured here.
- **The reference minimum is known.** Success is defined against a reference obtained by dense local search on a declared function. On real data no such reference exists, so "success rate" is not a quantity a field inversion can report at all.
- **The tolerance 0.05 is a model choice.** Success rates scale with $\tau$, and the volumes measured in [Global Search](04-global-search.md) show how strongly.
- **The proposal is Cauchy-like by construction.** The heavy-tail benefit claimed in Section 4 is a property of (4.1); a Gaussian proposal at the same schedule would need its own measurement, and the demo prints a Gaussian variant for exactly that reason.
- **No free lunches.** The NA contraction and the VFSA heavy tail are both priors about the misfit surface. Neither replaces the forward evaluations they consume.

## Mastery checkpoint

1. Derive (2.1) from the definition of the Voronoi cell and explain why the inscribed ball is inside the cell but the circumscribed ball is not.
2. Reproduce (2.2) numerically for the measured radii in Section 2 and compare with the printed volume fractions.
3. Compute the acceptance probabilities (5.1) and (5.2) and the step at which the schedule reaches $T = 0.05$.
4. From the measured success rates and run counts, compute the standard error of each row in Section 7 and decide which differences are resolved.
5. Design a restart rule for the NA whose threshold is a measured quantity from Section 2, and say what you would measure to show it works.
6. State three reasons why a success rate measured here cannot be quoted for a field dataset.

## Common pitfalls

- **Reporting the best run of an annealer.** Section 6 shows the median and the spread matter more than the maximum.
- **Cooling too fast, or not cooling far enough.** The measured worse-with-more-budget result is what an unbalanced schedule looks like.
- **Trusting a contraction without a restart rule.** Section 3 measured a run nine times worse than the tolerance.
- **Using a Gaussian proposal at low temperature.** Its tails are too thin; the chain freezes in place.
- **Comparing runs at unequal evaluation counts.** The count, not wall-clock, is the honest currency.

## Related modules

- [Global Search: Monte Carlo, Simulated Annealing, Genetic Algorithms](04-global-search.md) — the Metropolis rule and the budget arithmetic reused here.
- [Multi-Start, Hybrid and Memetic Strategies](06-multi-start-and-hybrid.md) — the coarse-to-fine alternative to a learned proposal.
- [Convergence Diagnosis and Local-Minimum Traps](07-convergence-and-local-minima.md) — what to check about the model either method returns.

## Materials

- Demo: `code/neighbourhood_annealing_demo.py` (print-only, about 3 s, exit 0).
- Exercises: `exercises/05-neighbourhood-algorithms-exercises.md` with solutions in `exercises/05-neighbourhood-algorithms-solutions.md`.

All models and data in this module are SYNTHETIC.
