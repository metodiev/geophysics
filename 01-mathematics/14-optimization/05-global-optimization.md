---
id: 01-14-05
title: "Global Optimisation: Simulated Annealing, Genetic Algorithms"
level: graduate
prereqs: ["01-14-01", "01-14-04"]
estimated_minutes: 90
tags: [global-optimization, simulated-annealing, genetic-algorithms, multimodal]
---

# Global Optimisation: Simulated Annealing, Genetic Algorithms

## Learning objectives

By the end of this lesson you will be able to:

1. **Explain** the difference between "reaching the global minimum of the
   misfit" and "recovering the Earth model", and give a geophysical example where
   they differ.
2. **Measure** the basin of attraction of a global minimum by running a local
   method from a grid of starting models, and interpret the fraction as the
   success probability of a restarted local search.
3. **Implement** simulated annealing with a geometric cooling schedule and a
   shrinking neighbourhood, and report a success rate with its evaluation cost.
4. **Implement** a genetic algorithm with tournament selection, crossover and
   mutation, and compare its cost per successful run with annealing's.
5. **Explain** how phase wrapping produces an aliasing family of zero-misfit
   models, and predict the family from the travel-time formula.
6. **Choose** between a global search, a better prior, and better data, and
   justify the choice with measured numbers.

## Prerequisites

[01-14-01 Convexity, Stationarity and Optimality Conditions](./01-convexity.md)
for basins and curvature, and
[01-14-04 Linear and Nonlinear Least Squares](./04-least-squares.md) for the local
solver that every global method uses as its final step.

## 1. Intuition: the misfit is not the answer

Every global-optimisation method exists because a misfit can have several
minima. But there is a deeper problem, and this lesson is built around it: **the
global minimum of your misfit need not be the model you are looking for.** The
misfit encodes what the data can see; if two very different models produce
identical data, both are global minima, and the search has no basis for
preferring either.

That is not a hypothetical. It happens in every branch of geophysics:

| Method | Mechanism | Consequence |
|---|---|---|
| Refraction / waveform | phase wrapping: an arrival error of one full period is invisible | family of aliased velocity models |
| MT | the transverse-electric/transverse-magnetic trade-off and layer-thickness ambiguity | equivalent conductivity structures |
| Gravity | a deep large body and a shallow small one produce nearly the same anomaly | depth–amplitude trade-off |
| Magnetics | remanent magnetisation direction versus induced | multiple acceptable geometries |
| Reflection static corrections | a cycle-skip in a pick | systematic long-wavelength error |

Global methods attack the *first* problem (multiple minima with different misfit
values) and cannot touch the second (multiple minima with the same misfit). Both
need to be understood, and Section 4 shows the difference numerically: on a
two-parameter cycle-skipped misfit, annealing finds a zero-misfit model on **20
of 20** seeds, and the true model on **2 of 20**.

There is a second, more practical point. Global methods are stochastic. Their
output is therefore a *report* — "success rate $X$ per cent at a budget of $N$
evaluations" — not a single number. Any paper quoting one model from one
annealing run has thrown away the only statistic that matters.

## 2. Precise definitions

### 2.1 Basins and local minima

For a continuous objective $f$ on a domain $\mathcal{D}$, the **basin of
attraction** of a local minimiser $m^{*}$ under a descent map $\mathcal{L}$ is

$$\mathcal{B}(m^{*}) = \{m \in \mathcal{D} :
\lim_{k\to\infty} \mathcal{L}^{k}(m) = m^{*}\}. \tag{2.1}$$

$\mathcal{L}$ might be gradient descent with a fixed step, Gauss–Newton with a
line search, or a coordinate-descent sweep. The basin depends on $\mathcal{L}$,
which is often forgotten: "the basin of the global minimum" is not a property of
$f$ alone.

### 2.2 Exploitation and exploration

Every method needs both. **Exploitation** means testing small moves that can
improve the objective (a local descent step). **Exploration** means accepting
moves that make it worse, so that the trajectory can leave a basin. Simulated
annealing makes the trade explicit through a temperature; a genetic algorithm
through selection pressure and mutation rate.

### 2.3 Simulated annealing

Draw a proposal $m' = m + \eta$ with $\eta$ from a symmetric distribution, and
accept it with probability

$$P_{\text{accept}} = \min\left(1,\ \exp\left(-\frac{f(m') - f(m)}{T}\right)\right),
\tag{2.2}$$

where $T$ is a temperature that decreases. Two limits are instructive:
$T \to 0$ accepts only improvements (a random-restart descent), and $T \to \infty$
accepts everything (a random walk). A **geometric schedule** $T_{k+1} = \rho T_k$
with $\rho$ close to $1$ is what makes the method work: the chain must be cooled
slowly enough to equilibrate, and Section 4.6 measures what happens when it is
not. In practice the sequence is finished with a **local polish**, because
annealing converges in distribution but never exactly.

### 2.4 A genetic algorithm

Maintain a population $\{m^{(1)}, \dots, m^{(N)}\}$. Each generation:

1. **Select** parents by tournament: draw $k$ at random, keep the best.
2. **Recombine** two parents into a child (blend crossover: $c_i \sim
   U[\min(a_i,b_i) - \tfrac{1}{2}\Delta_i,\ \max(a_i,b_i) + \tfrac{1}{2}\Delta_i]$
   with $\Delta_i = |a_i - b_i|$).
3. **Mutate** with a small probability $\pi$ by adding $\mathcal{N}(0, \sigma^{2})$.
4. Carry over the best one or two unchanged (**elitism**), so the best-so-far
   never degrades.

The two hyperparameters that matter are the population size and the mutation
rate; a population that is too small converges to a local minimum quickly, and a
mutation rate that is too high destroys the accumulation of good partial
solutions.

### 2.5 Cost accounting

Never compare global methods by iteration count. Compare:

- **evaluations** of the objective (the expensive operation),
- the **budget** allocated,
- the **success rate** over seeds,
- and ideally the **best-so-far** as a function of budget, since an operational
  code is usually stopped early.

## 3. Derivations

### 3.1 Why annealing can escape a basin

Let the current point be at a local minimum and suppose the nearest lower point
requires crossing a barrier of height $\Delta$. A proposal of the right size is
accepted with probability $\exp(-\Delta/T)$ per attempt. Over a schedule of
length $K$ the probability of crossing at least once is roughly
$1 - (1 - p\exp(-\Delta/T))^{K}$ where $p$ is the probability that a proposal
points over the barrier. Two consequences:

- The method can escape any barrier of finite height given enough time, which is
  the theoretical reason to use it.
- The required time grows exponentially with $\Delta/T$, which is why annealing
  is expensive and why the cooling schedule matters more than the proposal
  distribution.

### 3.2 The aliasing family, derived

For the two-parameter cycle-skipped misfit of Section 4.1,

$$t_{\text{pred}}(x) = \frac{x}{v_1} + \frac{x^{2}}{4v_2},
\qquad
t_{\text{obs}}(x) = \frac{x}{2} + \frac{x^{2}}{12},$$

with $v_2 = 3$ the second terms cancel and the arrival-time error becomes

$$\Delta t(x) = x\left(\frac{1}{2} - \frac{1}{v_1}\right)
= \frac{x}{2}\left(1 - \frac{2}{v_1}\right). \tag{3.1}$$

The misfit is $\sum_x [1 - \cos(2\pi \Delta t(x)/T)]$ with period $T = 0.5$ s, so
it vanishes whenever $\Delta t(x)$ is an integer multiple of $T$ for every offset
$x$ — that is, whenever $\frac{1}{2}\left(1 - 2/v_1\right) = m$ for an integer
$m$, i.e.

$$v_1 = \frac{2}{1 - 2m}, \qquad m \in \mathbb{Z}:\quad
m = 0 \Rightarrow v_1 = 2, \quad m = -1 \Rightarrow v_1 = 1 . \tag{3.2}$$

Both are inside the domain $[1,3]$ km/s. The demonstration prints exactly this
table, including the arrival-time differences $(-0.5, -1.0, -1.5, -2.0)$ s for
$v_1 = 1$ and $(0,0,0,0)$ for $v_1 = 2$, with misfit $0.000\times10^{0}$ in both
cases. **Two models fit the data exactly and the misfit cannot distinguish them.**

This is the single most important calculation in the lesson. It tells you that
the appropriate response to "the inversion found a different model" is often not
"run the optimiser longer" but "ask whether the data can see the difference".

### 3.3 How much of model space drains to the global basin

Without an analytic argument, the practical quantity is the fraction of starting
models that reach the global basin. If a fraction $\theta$ of random starts
converges to the global minimum, then (independent) restarts give success
probability $1 - (1-\theta)^{r}$ after $r$ restarts: with $\theta = 0.05$, ten
restarts give $40$ per cent and fifty give $92$ per cent. Restarts are often
cheaper than annealing and are embarrassingly parallel — but the independence
assumption is usually optimistic, because a *designed* set of starting models is
correlated.

### 3.4 Constraining, penalising, or re-weighting

A prior changes the objective. Three ways to make the aliasing family disappear:

1. **A bound** $v_1 \in [1.8, 2.2]$ km/s, e.g. from a well log: removes
   $v_1 = 1$ from the feasible set entirely. Measured effect: annealing reaches
   the truth on $20$ of $20$ seeds (Section 4.8).
2. **A penalty** $\alpha (v_1 - 2)^{2}$: makes $v_1 = 1$ a higher-misfit model,
   so it stops being a global minimum, but it also biases the estimate if the
   penalty is too strong.
3. **Better data**: shortening the *invisibility* — a longer period, richer
   low-frequency content, or a wider offset range. Measured: with period $2.0$ s
   the number of local minima falls from $61$ to $5$ and local descents reach the
   truth in $137$ of $144$ starts ($95.1$ per cent) instead of $59$ ($41.0$ per
   cent).

**Option 3 is the only one that adds information.** Options 1 and 2 encode what
you already believed; option 3 changes what the data determine. That distinction
is the geophysical content of this lesson.

## 4. Numerical results

All numbers come from
[`code/global_optimization_demo.py`](./code/global_optimization_demo.py), which
uses a fixed list of seeds (0–19) so the success rates are reproducible.

### 4.1 The objective

A SYNTHETIC two-parameter misfit
$\sum_i [1 - \cos(2\pi \Delta t_i / 0.5\,\text{s})]$ with
$t = x/v_1 + x^{2}/(4v_2)$ at offsets $x = 1, 2, 3, 4$ km, on
$v_1 \in [1.0, 3.0]$, $v_2 \in [1.5, 6.0]$ km/s, with the true model
$(v_1, v_2) = (2.0, 3.0)$.

| quantity | measured |
|---|---|
| $400\times400$ grid minimum | $0.000\times10^{0}$ at $(1.0000, 3.0000)$ |
| local minima counted on the grid | $48$ |
| grid points with misfit $< 10^{-10}$ | $1$ |
| misfit at the true model | $0.000\times10^{0}$ |

The grid's global minimum is *not* the true model: it is the aliased model
$v_1 = 1.0$ from (3.2). The problem statement "find the global minimum" has an
answer, and that answer is wrong as geophysics.

### 4.2 Local descent: what one start buys

Coordinate descent with a shrinking step from a $24 \times 24$ grid of starting
models (576 starts):

| outcome | count | fraction |
|---|---|---|
| reached a model with zero misfit | $249$ | $43.2$ per cent |
| reached the *true* model | $220$ | $38.2$ per cent |

A local method from a single "reasonable" start therefore has a success
probability of about $0.38$ here, and restarts are a legitimate strategy: the
formula of Section 3.3 predicts $1 - (1-0.382)^{5} = 91$ per cent after five
restarts. It also shows that the notion "the basin of the global minimum" needs
the caveat of (2.1): almost half of model space drains to a basin whose minimum
is not the Earth.

### 4.3 Simulated annealing

Budget $20\,000$ evaluations, geometric cooling with $\rho = 0.9995$ per
iteration, a neighbourhood that shrinks with the temperature, and a local polish
at the end:

| statistic | value |
|---|---|
| seeds tested | $20$ |
| runs reaching misfit $< 10^{-3}$ | $20$ (100 per cent) |
| runs reaching the **true** model | $2$ (10 per cent) |
| median evaluations used | $20\,125$ |
| exemplary models found | $(1.0000, 3.0000)$ with misfit $0.0$; $(2.0000, 3.0000)$ with misfit $6.6\times10^{-15}$ |

Annealing is *reliable at its job* — it found a zero-misfit model on every seed
— and the models it found are, nine times in ten, the aliased one. This is the
cleanest possible statement of the lesson's theme.

### 4.4 A genetic algorithm

Population $40$, $60$ generations, tournament selection, blend crossover,
Gaussian mutation with probability $0.25$, elitism of two:

| statistic | value |
|---|---|
| runs reaching a zero-misfit model | $20$ of $20$ (100 per cent) |
| runs reaching the **true** model | $15$ of $20$ (75 per cent) |
| median evaluations used | $2320$ |
| mean evaluations used | $2320.0$ |

Both methods are certain to find *a* zero-misfit model, and they disagree about
which: annealing lands in the $v_1 = 1.0$ basin nine times in ten, the genetic
algorithm in the true basin three times in four. **The choice depends on the
search method, not on the data**, because the data cannot distinguish the two
models. Also note the cost: the genetic algorithm used $2320$ evaluations to
reach a zero misfit, an order of magnitude fewer than annealing's $20\,125$.

### 4.5 Grid and random search: the cost of a guarantee

| method | budget | best misfit found |
|---|---|---|
| grid $60\times60$ | $3600$ | $4.185\times10^{-3}$ |
| random search, seed 0 | $3600$ | $3.426\times10^{-2}$ |
| genetic algorithm (median) | $2320$ | $0$ |
| simulated annealing (median) | $20\,125$ | $0$ |

A grid gives a *guarantee* of not missing a basin wider than the grid spacing,
which is worth something. It is also $10^{2}$–$10^{5}$ times more expensive than
a directed search at equal quality for a two-parameter problem, and hopeless
beyond about four parameters: the number of grid points grows exponentially with
dimension. Uniform random sampling is strictly worse than a grid for the same
budget (it can miss regions entirely) and its best value after $3600$ evaluations
was $3.4\times10^{-2}$, eight times worse than the grid's.

### 4.6 Badly configured annealing: the schedule is the method

Repeating Section 4.3 with cooling rate $0.995$ instead of $0.9995$ — a change of
one character:

| statistic | fast cooling | Section 4.3 |
|---|---|---|
| runs reaching misfit $< 10^{-3}$ | $19$ of $20$ | $20$ of $20$ |
| median final misfit | $1.196\times10^{-5}$ | $0.000\times10^{0}$ |

The temperature collapses before the chain explores the domain, and the run
degenerates into a local search from a random start. The success *rate* barely
changed, so a practitioner who only counted successes would not notice; the
median final misfit changed by five orders of magnitude, which is what a residual
plot would show.

### 4.7 Best-so-far as a function of budget

| budget (evaluations) | SA best (median of 5 seeds) | GA best (median of 5 seeds) |
|---|---|---|
| $200$ | $0.000\times10^{0}$ | $1.325\times10^{-2}$ |
| $1000$ | $0.000\times10^{0}$ | $3.446\times10^{-6}$ |
| $5000$ | $0.000\times10^{0}$ | $6.687\times10^{-10}$ |
| $20\,000$ | $0.000\times10^{0}$ | $0.000\times10^{0}$ |

The genetic algorithm improves monotonically with budget here, from
$10^{-2}$ to zero; annealing finds a zero-misfit model even at the smallest
budget, because this objective is two-dimensional and its zero-set is
substantial. On a harder objective the ordering reverses. The honest reading is
that **these two methods are not ordered by quality, only by cost profile**, and
that the cost profile must be measured on the problem at hand.

### 4.8 Two ways to remove the aliasing

**(a) A prior.** Restricting $v_1 \in [1.8, 2.2]$ km/s:

| method | reaching the true model |
|---|---|
| local descent from $576$ starts | $339$ ($58.9$ per cent) |
| simulated annealing, $20$ seeds | $20$ of $20$ |

Local descent improves from $38.2$ to $58.9$ per cent — better, but not
certain — because the objective is still multi-modal in $v_2$. Annealing becomes
*deterministic in effect*: with the aliasing competitor removed, it always finds
the truth within the budget.

**(b) Better data.** Repeating the whole local-descent experiment with a longer
misfit period:

| period (s) | local minima | grid minimum | descents reaching the truth |
|---|---|---|---|
| $0.5$ | $61$ | $3.230\times10^{-4}$ | $59$ of $144$ ($41.0$ per cent) |
| $1.0$ | $9$ | $8.075\times10^{-5}$ | $78$ of $144$ ($54.2$ per cent) |
| $2.0$ | $5$ | $2.019\times10^{-5}$ | $137$ of $144$ ($95.1$ per cent) |

The number of local minima falls by an order of magnitude and local descent
becomes reliable. Nothing about the optimiser changed; the *data* stopped
aliasing. This is why the geophysical literature on "low-frequency content" in
seismic data and on long-period MT data is really a literature about the geometry
of the misfit.

## 5. Physical interpretation

**A global search is a way of asking how many answers the data admit.** Its
useful output is not the best model but the *set* of models with comparable
misfit, plus the misfit differences between them. Reporting that set is what
turns an inversion into a statement about resolution.

**Aliasing is information loss, and it is diagnosable.** When the period of the
observable is comparable to the range of predicted values, models separated by a
period are indistinguishable. The diagnosis is cheap: compute the predicted
range of $\Delta t$ and compare it with the period. If it exceeds one period, you
have an aliasing risk before you run anything.

**Search effort cannot substitute for information.** Section 4.8 measures $38.2$
per cent versus $95.1$ per cent for the *same* algorithm on *different data*.
Modern inversions that report "we used 5000 restarts" are reporting effort, not
information.

**Randomness is a feature, and it must be reported.** A stochastic method's
result is a distribution. Seeds, budgets, success rates and the cost profile
belong in the methods section, exactly as uncertainty belongs in the results.

**Global and local methods are complements.** Every practical workflow runs a
global search to identify basins and then a local inversion inside the chosen
one; the global phase decides *which* model family, the local phase produces the
best model in it and its covariance.

## 6. Assumptions and regime of validity

1. **Bounded domain.** Both methods assume a box. The bounds are physical
   information and they change the answer (Section 4.8); report them.
2. **Finite budget.** Success rates are budget-dependent. A rate quoted without
   a budget is meaningless, as is a convergence curve without a stopping rule.
3. **The proposal distribution shapes the result.** Annealing with a step
   distribution too small will never cross a barrier; too large and it is a
   random walk. The demonstration shrinks the step with the temperature, which is
   a heuristic, not a theorem.
4. **Temperature schedules are heuristics.** Logarithmic cooling is provably
   convergent for a particular idealised proposal; geometric cooling is what is
   used and it is not provably convergent. Every claim of "global" convergence
   here is a claim about the budget.
5. **No guarantee of the true model.** Nothing in these methods addresses the
   aliasing family; that requires a prior or better data (Section 3.4).
6. **Dimension.** Basins and barrier heights behave differently in 2-D and in
   $10^{3}$-D. Success rates do not extrapolate across dimension, and the
   demonstration is a two-parameter problem for exactly that reason.
7. **Seeding.** Reported rates are only comparable if the random seeds are
   shared, which the demonstration does by using the same 20 seeds throughout.

## 7. Python demonstration

The companion script is
[`code/global_optimization_demo.py`](./code/global_optimization_demo.py), with
eight sections; it uses `random.Random(seed)` throughout so that every number is
reproducible with the standard library alone.

| Section | Measured | Interpretation |
|---|---|---|
| 1, objective | grid minimum $0.0$ at $(1.0, 3.0)$, $48$ local minima | the global minimum is an aliased model, not the truth |
| 2, family | $v_1 = 1$ and $v_1 = 2$ both give misfit $0$ | two exact solutions, from (3.2) |
| 3, descent | $249/576$ reach zero misfit, $220/576$ reach the truth | a single start succeeds $38$ per cent of the time |
| 4, annealing | $20/20$ reach zero misfit, $2/20$ the truth, median $20\,125$ evaluations | reliability at the wrong task |
| 5, genetic algorithm | $20/20$ zero misfit, $15/20$ the truth, median $2320$ evaluations | same conclusion, different trade |
| 6, grid/random | $4.19\times10^{-3}$ and $3.43\times10^{-2}$ at $3600$ evaluations | guarantees are expensive |
| 7, fast cooling | median final misfit $1.196\times10^{-5}$ against $0.0$ | the schedule is the method |
| 8, fixes | prior: $20/20$ truth; period $2.0$ s: $137/144$ descents to truth | priors and data, not effort |

> **Breaking exercise.** In Section 3, replace the coordinate descent with
> Gauss–Newton from [01-14-04](./04-least-squares.md) — the misfit is
> differentiable, so it is a one-line change — and re-measure the fraction of
> starts reaching the truth. Predict first whether a second-order local method
> has a *larger* or *smaller* basin than coordinate descent, then run it. The
> answer depends on the descent map $\mathcal{L}$ of (2.1), which is the point.

## 8. Exercises

Full set and worked solutions:
[`exercises/05-global-optimization-exercises.md`](./exercises/05-global-optimization-exercises.md)
and
[`exercises/05-global-optimization-solutions.md`](./exercises/05-global-optimization-solutions.md).
Four to start with:

**★1.** For a one-parameter misfit $\phi(v) = 1 - \cos(2\pi v)$, list every
global minimum on $[-3, 3]$ and explain why a local method's answer is
arbitrary.

**★2.** Derive the aliasing family for the misfit of Section 4.1 with the period
held at $0.5$ s and $v_2$ free, and state whether the family grows or shrinks.

**★★3.** With a start-success probability $\theta = 0.2$, how many restarts give
a $95$ per cent chance of reaching the global basin, assuming independence? What
does the demonstration's measured $\theta$ give for this problem?

**★★4.** Design an annealing schedule for a three-parameter problem with a
budget of $50\,000$ evaluations, state the initial temperature and the cooling
rate, and justify both from the objective's typical uphill step.

## 9. Common mistakes

1. **Reporting one annealing run as the answer.** The output of a stochastic
   method is a distribution; quote the rate.
2. **Confusing "found the global minimum" with "found the model".** Section 4.1
   is the counterexample, and it is not contrived.
3. **Comparing global methods by iteration count.** Compare evaluations, budget
   and success rate (Section 2.5).
4. **Choosing the design of the search instead of the design of the survey.**
   Section 4.8(b) is the evidence: better data beat better search.
5. **Ignoring the bounds.** They are prior information; a run with
   $v_1 \in [0, 100]$ km/s is a different (and worse-posed) problem.
6. **Believing that a genetic algorithm's population prevents premature
   convergence.** Without enough mutation, a population converges to one basin
   just as a single trajectory does.
7. **Cooling too fast, and reporting only the success rate.** Section 4.6 kept a
   $95$ per cent success rate while the median final misfit degraded by five
   orders of magnitude.
8. **Forgetting the local polish.** Annealing's final point is a sample from a
   low-temperature distribution, not a minimiser.

## 10. Real-world applications

- **Refraction and surface-wave inversion.** One-dimensional velocity profiles
  from dispersion curves are multi-modal in layer thickness; annealing and
  neighbourhood algorithms are standard, with the aliasing of Section 3.2 as the
  known failure mode.
- **Magnetotelluric inversion.** Conductivity layering produces equivalent
  models; global methods map the misfit basins and the equivalence families are
  reported as such.
- **Potential-field (gravity, magnetic) inversion.** Depth–amplitude trade-offs
  are handled with parameterised bodies and bounds, and the search documents how
  many distinct models fit.
- **Full-waveform inversion.** Multi-scale (frequency continuation) is the
  practical alternative to global search: start with data whose $\Delta t$
  variation is below one period, which is exactly the mitigation of Section 3.4
  option 3.
- **Reservoir history matching.** Ensemble and evolutionary methods dominate
  because each objective evaluation is a reservoir simulation, making the
  evaluation budget the binding constraint.
- **Machine-learning hyperparameter search.** Random search, Bayesian
  optimisation and evolutionary search are the same trade-offs with a different
  objective; the cost-accounting discipline of Section 2.5 is what transfers.

## 11. Further reading

- **Kirkpatrick, S., Gelatt, C. D., & Vecchi, M. P. (1983). Optimization by
  simulated annealing. *Science*, 220(4598), 671–680.** Level: accessible
  original paper. The source of the temperature idea; check your library for
  current access.
- **Holland, J. H. *Adaptation in Natural and Artificial Systems*. MIT Press.**
  Level: advanced. The classical statement of genetic algorithms.
- **Goldberg, D. E. *Genetic Algorithms in Search, Optimization and Machine
  Learning*. Addison-Wesley.** Level: intermediate. The practical reference,
  including the selection and crossover operators of Section 2.4.
- **Sen, M. K., & Stoffa, P. L. *Global Optimization Methods in Geophysical
  Inversion* (2nd ed.). Cambridge University Press.** Level: graduate. Written
  for this audience: annealing, genetic algorithms, neighbourhood algorithms and
  their use on real geophysical objectives, with the statistics reported rather
  than one answer.
- **Tarantola, A. *Inverse Problem Theory and Methods for Model Parameter
  Estimation*. SIAM.** Level: graduate. Why multiple models are the honest
  output of an inversion.
- **Sambridge, M., & Mosegaard, K. (2002). Monte Carlo methods in geophysical
  inverse problems. *Reviews of Geophysics*, 40(3).** Level: graduate. A survey
  that treats global search and sampling as one subject; confirm access through
  your library.

> Note on citations: bibliographic details above are given so that you can locate
> the works. This repository does not host or reproduce copyrighted text, and you
> should confirm editions and current availability through your library before
> citing them yourself.

## 12. Self-assessment checklist

- [ ] I can define a basin of attraction and explain its dependence on the
      descent map.
- [ ] I can implement simulated annealing with a geometric schedule and a
      shrinking neighbourhood.
- [ ] I can implement a genetic algorithm with tournament selection and elitism.
- [ ] I can measure a success rate over seeds and report it with its budget.
- [ ] I can derive the aliasing family of a periodic misfit and predict whether a
      given dataset is at risk.
- [ ] I can explain why a prior and better data are different remedies, with the
      demonstration's numbers.
- [ ] I can compare a global method with restarted local descent on cost.

## 13. Related lessons

- [01-14-01 Convexity, Stationarity and Optimality Conditions](./01-convexity.md) —
  why multiple basins exist and what they mean.
- [01-14-02 Unconstrained Minimisation](./02-unconstrained.md) — the local solver
  used as the polish step.
- [01-14-03 Constrained Optimisation and Lagrange Multipliers](./03-constrained.md) —
  bounds as prior information (Section 4.8's option 1).
- [01-14-04 Linear and Nonlinear Least Squares](./04-least-squares.md) — the
  objective being minimised, and its own failure modes.
- [01-14-06 Calculus of Variations](./06-variational-calculus.md) — optimisation
  over functions, where parameterisation is itself a choice.
- [01-18 Inverse Problems](../../18-inverse-problems/README.md) — non-uniqueness
  as the central subject, with the appraisal tools that go beyond a search.
