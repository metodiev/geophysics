# Exercises — 01-14-05 Global Optimisation: Simulated Annealing, Genetic Algorithms

Attempt these **closed-book** before opening the
[solutions](./05-global-optimization-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Conventions: a run of a stochastic method is reported as a **success rate over
seeds with a budget in objective evaluations**, never as a single model. "Reaching
the global basin" means reaching a point whose misfit is within the stated
tolerance of the global minimum; "reaching the true model" means matching the
model the data were generated from. Those are different statements and both must
be reported.

Problems referring to
[`../code/global_optimization_demo.py`](../code/global_optimization_demo.py)
require you to run it and report its actual output.

---

## ★ Foundational

**★1.** Consider the one-parameter misfit $\phi(v) = 1 - \cos(2\pi v)$ on the
domain $[-3,3]$.

(a) List every global minimum and the value of the misfit there.
(b) State how many local minima the function has, and why "the minimum" is not a
well-posed request for a model.
(c) Starting a local method at $v_0 = 0.37$, state where it converges and explain
why the answer is a statement about the starting point rather than about the data.
(d) State what a global optimiser can and cannot report about this objective.

---

**★2.** Derive the aliasing family of the lesson's Section 4.1 misfit.

The predicted and observed arrival times are

$$t_{\text{pred}}(x) = \frac{x}{v_1} + \frac{x^{2}}{4v_2}, \qquad
t_{\text{obs}}(x) = \frac{x}{2} + \frac{x^{2}}{12},$$

at offsets $x = 1,2,3,4$ km, with the misfit
$\sum_x\left[1 - \cos\left(2\pi\Delta t(x)/0.5\right)\right]$ and
$\Delta t = t_{\text{pred}} - t_{\text{obs}}$.

(a) Set $v_2 = 3$ and derive the condition on $v_1$ that makes the misfit vanish
identically, giving the family $v_1 = 2/(1-2m)$ for integer $m$.
(b) List the members of the family inside $[1,3]$ km/s and the arrival-time
difference at each offset for each member.
(c) Compute the misfit at $(v_1,v_2) = (1,3)$ and at the true model $(2,3)$, and
state what the comparison proves.
(d) Now let $v_2$ vary as well and state whether the family grows or shrinks, with
the reason.

---

**★★3.** Restarts as a strategy.

(a) With a single-start success probability $\theta = 0.2$, how many independent
restarts give at least a $95$ per cent chance of reaching the global basin?
Derive the formula and solve it for the smallest integer $n$.
(b) The lesson measures $\theta = 0.382$ for coordinate descent from 576 starts on
its two-parameter misfit. Redo (a) with that value.
(c) Verify the lesson's claim that five restarts give $91$ per cent.
(d) State the assumption that makes the restarts independent, and name a case in
which it fails.

---

**★★4.** Design an annealing schedule for a three-parameter problem with a budget
of $50\,000$ objective evaluations.

(a) State an initial temperature $T_0$ chosen from the objective's typical uphill
step $\Delta_{\text{typ}}$, and justify the choice with a probability
computation: what acceptance probability does your $T_0$ give for a step of size
$\Delta_{\text{typ}}$?
(b) State a geometric cooling rate $\rho$ such that the temperature falls by three
orders of magnitude over the budget, and show the arithmetic.
(c) Compare your $\rho$ with the lesson's $0.9995$ at $20\,000$ evaluations by
computing the final temperature ratio in both cases.
(d) State the neighbourhood rule you would use and why it must shrink with the
temperature.

---

## ★★ Applied

**★★5.** Acceptance probabilities.

(a) Tabulate $\exp(-\Delta/T)$ for $\Delta/T = 1, 2, 5, 10, 20$.
(b) State the two limits $T\to0$ and $T\to\infty$ and what the chain does in each.
(c) The lesson's §4.6 repeats an annealing run with $\rho = 0.995$ instead of
$0.9995$ over the same budget. Compute the final temperature ratio in both cases
and the number of iterations at which the fast schedule's temperature has fallen
to $1$ per cent of $T_0$.
(d) Explain why the success *rate* barely changed while the median final misfit
degraded by five orders of magnitude, and what diagnostic should replace a
success rate.

---

**★★6.** Cost accounting for a genetic algorithm.

(a) The lesson's GA uses population 40, 60 generations, and reports a median of
2320 evaluations to reach a zero misfit. Convert that to generations and explain
why it is not 2400.
(b) Compare the median evaluation counts of the GA (2320) and annealing (20125)
and express the ratio.
(c) Explain why the comparison is not a statement that the GA is "better", using
the lesson's best-so-far table for budgets $200$, $1000$, $5000$, $20000$.
(d) State the four quantities of Section 2.5 that must be reported for any
stochastic method, and give the value of each for the annealing run of §4.3.

---

**★★7.** Derive the escape probability from a basin.

A local minimum is surrounded by a barrier of height $\Delta$ above it; a proposal
points over the barrier with probability $p$ per attempt.

(a) Write the probability of escaping over $K$ attempts at temperature $T$.
(b) Show that the required $K$ grows exponentially in $\Delta/T$, and evaluate the
factor by which it grows when $\Delta/T$ increases from $5$ to $10$.
(c) With $p = 0.1$, $\Delta/T = 3$, compute the number of attempts for a
$99$ per cent escape probability.
(d) Explain what this implies about the relative importance of the cooling
schedule and the proposal distribution.

---

**★★8.** Measured behaviour of the fitted objectives.

From the demonstration's tables, state and interpret:

(a) the number of local minima on the $400\times400$ grid, the grid minimum, and
the misfit at the true model of §4.1;
(b) the fraction of the 576 coordinate-descent runs that reached a zero-misfit
model and the fraction that reached the true model, with the difference explained;
(c) the annealing success rates (zero misfit and true model) and the GA's, and
what the *difference between the two methods* proves about the data;
(d) the effect of restricting $v_1\in[1.8,2.2]$ km/s on both methods, and the
general lesson about priors versus search effort.

---

## ★★★ Research-oriented

**★★★9.** Implement annealing on $\phi(v) = 1 - \cos(2\pi v)$ over $[-3,3]$ and
measure which of the equivalent minima you obtain.

Use the following protocol so that the results are comparable: initial point
$v_0$ drawn uniformly from $[-3,3]$; proposals
$v' = v + \mathcal{N}(0,\sigma^{2})$ with
$\sigma = 0.5\,T/T_0 + 0.02$, reflected at the boundaries by rejecting the
proposal; acceptance by the Metropolis rule; best-so-far recorded; budget
$20\,000$ evaluations; $T_0 = 0.5$; 50 seeds.

(a) Run with $\rho = 0.9995$ and with $\rho = 0.995$. For each, report the
fraction of runs reaching misfit $< 10^{-6}$, the fraction landing within $10^{-3}$
of $v = 0$, and the median final misfit.
(b) Explain why the "success rate" is uninformative for this objective and which
statistic replaces it.
(c) State whether either cooling rate produces a better *model* on this objective,
and explain why the usual intuition that slower cooling is always better does not
apply here — then say under what change to the objective it would apply.
(d) Change the objective to one with a *single* global minimum, for example
$\phi(v) = (v-0.5)^{2} - 0.1\cos(10\pi v)$ on $[-3,3]$, and state — with reasons,
not numbers — how your two statistics would change.

---

**★★★10.** The search cannot substitute for information.

The demonstration repeats the local-descent experiment with the misfit period
changed from $0.5$ s to $1.0$ s and $2.0$ s.

(a) State the measured number of local minima and the fraction of descents
reaching the truth for each period.
(b) Explain the trend from the aliasing criterion: when does phase wrapping stop
being a risk?
(c) Compute the predicted range of $\Delta t$ over the offsets for each period and
compare it with the period, stating the ratio that diagnoses the risk.
(d) State the two ways to remove the risk and, for each, the cost in survey effort
versus search effort, referring to the lesson's numbers.
