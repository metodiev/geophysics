# Solutions — 01-14-05 Global Optimisation: Simulated Annealing, Genetic Algorithms

> **Read this after attempting the exercises, not before.** Numbers attributed to
> the demonstration are the output of
> [`../code/global_optimization_demo.py`](../code/global_optimization_demo.py);
> numbers attributed to "the experiment here" were computed with the protocol
> stated in the exercise, and the seeds are given so the run is reproducible.

---

## ★1 — One parameter, seven answers

**(a)** $\phi(v) = 1 - \cos 2\pi v$ vanishes exactly where $\cos 2\pi v = 1$, i.e.
at every integer. On $[-3,3]$:

$$v \in \{-3,\ -2,\ -1,\ 0,\ 1,\ 2,\ 3\}, \qquad \phi = 0\ \text{at each.}$$

**(b)** The function is smooth and periodic with period 1, so it has exactly those
seven local minima on the closed interval (each is also a global minimum, and
there are no others). "Find the minimum" therefore has seven equally valid
answers, and an optimiser that returns one of them has not distinguished
anything: the *value* is the same at all seven, so no misfit comparison can rank
them.

**(c)** From $v_0 = 0.37$ any descent method converges to the nearest minimum,
$v = 0$: the basin of $v=0$ is $(-0.5, 0.5)$, and the starting value alone decides
which of the seven you get. The answer is a statement about the start, not about
the data, because the data are equally satisfied by every integer.

**(d)** A global optimiser can report the minimum misfit (zero) and the *set* of
models attaining it within the tolerance. It cannot report which member of that
set is the Earth, and it cannot manufacture information to break the tie. The
honest output is the set plus the misfit differences between its members.

---

## ★2 — The aliasing family

**(a)** With $v_2 = 3$ the quadratic terms agree ($x^{2}/12$ both), leaving

$$\Delta t(x) = x\left(\frac12 - \frac{1}{v_1}\right)
= \frac{x}{2}\left(1 - \frac{2}{v_1}\right)
\equiv x\alpha, \qquad \alpha = \frac12 - \frac{1}{v_1}.$$

The misfit vanishes when $\Delta t(x)$ is an integer multiple of $T = 0.5$ s for
every offset, i.e. when $\alpha = m/2$ for integer $m$:

$$\frac12 - \frac{1}{v_1} = \frac{m}{2}
\quad\Longrightarrow\quad
v_1 = \frac{2}{1 - 2m}. \qquad\square$$

**(b)** Inside $[1,3]$ km/s: $m = -1$ gives $v_1 = 2/3$ (outside), so only

$$m = 0 \Rightarrow v_1 = 2 \ (\text{the true model}), \qquad
m = -1 \Rightarrow v_1 = 1 .$$

At $v_1 = 1$, $\alpha = 1/2$, so $\Delta t(x) = x/2 = (0.5, 1.0, 1.5, 2.0)$ s at
$x = 1,2,3,4$ — every value an exact multiple of the period. At $v_1 = 2$,
$\alpha = 0$ and $\Delta t = (0,0,0,0)$.

**(c)** The misfit is $0.000\times10^{0}$ at **both** models: $(1,3)$ and $(2,3)$.
The comparison proves that the misfit cannot distinguish them — they are not a
near-tie, they are an exact tie at machine precision. The grid's "global minimum"
$(1.0,3.0)$ is therefore not the Earth, and the phrase "global minimum" has an
answer that is wrong as geophysics.

**(d)** Allowing $v_2$ to vary **grows** the family: the quadratic term
$x^{2}\left(\frac{1}{12} - \frac{1}{4v_2}\right)$ now contributes, and because it
is positive for $v_2 > 3$ and negative for $v_2 < 3$ it can offset the linear term
at some offsets. The misfit is a finite sum over four offsets, so the exact
zero-set is the solution of four congruences in two unknowns
$(1/v_1, 1/(4v_2))$; the lesson's re-run with a longer period shows the same effect
quantitatively (fewer local minima, more descents reaching the truth), which is the
practical statement that the family shrinks when the *data* stop aliasing.

---

## ★★3 — Restarts

**(a)** With independent restarts each of success probability $\theta$, the
probability of at least one success in $n$ restarts is $1 - (1-\theta)^{n}$.
Requiring $1 - (1-\theta)^{n}\ge 0.95$:

$$n \ge \frac{\ln 0.05}{\ln(1-\theta)} = \frac{-2.9957}{-0.22314} = 13.43
\quad\Longrightarrow\quad n = \boxed{14}.$$

Check: $1 - 0.8^{14} = 0.9560 \ge 0.95$, and $1 - 0.8^{13} = 0.9450 < 0.95$.

**(b)** With $\theta = 0.382$:

$$n \ge \frac{\ln 0.05}{\ln 0.618} = \frac{-2.9957}{-0.4812} = 6.225
\quad\Longrightarrow\quad n = \boxed{7},$$

with $1 - 0.618^{7} = 0.9656$ and $1 - 0.618^{6} = 0.9443$.

**(c)** $1 - (1 - 0.382)^{5} = 1 - 0.618^{5} = 1 - 0.09015 = 0.90985$, i.e.
$91.0$ per cent — the lesson's figure is correct.

**(d)** The restarts must be **statistically independent**, which requires that the
starting models be drawn independently and that the method have no memory between
runs. The assumption fails whenever the restarts are correlated — for instance
when they are drawn on a coarse grid whose spacing exceeds a basin's width, or when
the "success" of a run is judged by the same local criterion that produced it (as
in a bootstrap-selected starting model). The honest check is to run two
independent batches and compare the success rates; if they differ by more than the
binomial scatter, the independence assumption is already suspect.

---

## ★★4 — Designing a schedule

**(a)** Let $\Delta_{\text{typ}}$ be the typical uphill step the objective
presents (the median increase of a random proposal). Choosing

$$T_0 = \frac{\Delta_{\text{typ}}}{\ln 2} = 1.4427\,\Delta_{\text{typ}}$$

gives an acceptance probability $\exp(-\Delta_{\text{typ}}/T_0) = \exp(-\ln2) =
0.5$ for a step of exactly that size: half of the typical uphill moves are
accepted at the start, so the chain explores rather than descends. Larger $T_0$
wanders without structure; much smaller $T_0$ makes the run a random-restart
descent. The number is a design choice, but it is a *stated* one, which is what
matters.

**(b)** Requiring $T_{\text{end}}/T_0 = 10^{-3}$ over $K = 50\,000$ iterations
with $T_{k+1} = \rho T_k$:

$$\rho = \left(\frac{T_{\text{end}}}{T_0}\right)^{1/K}
= 10^{-3/50000} = \mathrm{e}^{-6.9078/50000}
= \mathrm{e}^{-1.3816\times10^{-4}} = \boxed{0.99986185}.$$

**(c)** The lesson's $\rho = 0.9995$ over $20\,000$ iterations gives

$$\frac{T_{\text{end}}}{T_0} = \mathrm{e}^{20000\ln 0.9995}
= \mathrm{e}^{-10.0025} = 4.53\times10^{-5},$$

i.e. a factor of $22$ lower than the three-order design, and it was measured to be
adequate for that objective. For $K = 50\,000$ the same cooling *per iteration*
would overshoot the intended range; the correct statement of a schedule is
therefore the ratio $T_{\text{end}}/T_0$ and the budget, not "$\rho$" alone.

**(d)** The neighbourhood must shrink with the temperature, for example the
Gaussian proposal $\sigma_k = \sigma_0\,T_k/T_0$ used in the experiment of ★★★9.
The reason is that the acceptance probability and the proposal scale do different
jobs: $T_k$ controls *what* is accepted, and $\sigma_k$ controls *what is
proposed*. A fixed $\sigma$ at low temperature proposes steps far too large to be
accepted, so the chain stalls and wastes the budget; a $\sigma$ that shrinks like
$T$ keeps the acceptance rate roughly constant and turns the low-temperature phase
into a local-optimisation-like refinement. A final local polish (a descent method
started from the best point) is the standard last step, because annealing
converges in distribution and never exactly.

---

## ★★5 — Acceptance probabilities and the cost of cooling too fast

**(a)**

| $\Delta/T$ | 1 | 2 | 5 | 10 | 20 |
|---|---|---|---|---|---|
| $\exp(-\Delta/T)$ | $3.679\times10^{-1}$ | $1.353\times10^{-1}$ | $6.738\times10^{-3}$ | $4.540\times10^{-5}$ | $2.061\times10^{-9}$ |

**(b)** $T\to0$ accepts only improvements (a random-restart descent); $T\to\infty$
accepts everything (an unbiased random walk over the domain). The method works in
between, and the schedule is what brings the chain from the second limit to the
first while it is still able to cross barriers.

**(c)** Over $20\,000$ iterations:
$\rho = 0.9995$ gives $T_{\text{end}}/T_0 = 4.53\times10^{-5}$;
$\rho = 0.995$ gives $\mathrm{e}^{20000\ln0.995} = \mathrm{e}^{-100.25} =
3.3\times10^{-44}$. The fast schedule reaches $1$ per cent of $T_0$ after
$k = \ln(0.01)/\ln(0.995) = 919$ iterations, against
$k = \ln(0.01)/\ln(0.9995) = 9205$ for the slow one.

**(d)** The success *rate* barely moved because the objective's zero-set is
substantial — there are many models with misfit below $10^{-3}$, so even a
collapsed chain that has become a local descent usually lands in one of them. What
degraded is the *quality within that set*: with $\rho = 0.995$ the chain stops
exploring after $\sim900$ iterations and the best point it finds is set by a
single random start, so the median final misfit was $1.196\times10^{-5}$ against
$0.000$ for the slow schedule — five orders of magnitude. A success rate at a
fixed tolerance is a step function and hides exactly this; the diagnostic to report
is the **distribution of the final misfit** (or the best-so-far curve against
budget), not the number of runs that crossed some threshold.

---

## ★★6 — Cost accounting

**(a)** The GA evaluates the objective once per individual in the initial
population and once per child thereafter, so a run of $G$ generations with
population $P$ costs about $P(G+1)$ evaluations: $2320/40 = 58$, so the median run
terminated after about **58 generations** — earlier than the 60-generation cap,
because the run stopped (or was truncated) once the misfit reached zero. The
declared budget is 2400 evaluations; the median *used* is 2320, which is the number
that matters for comparison.

**(b)** $20125/2320 = 8.67$: the GA used about **$8.7$ times fewer** evaluations
than annealing to reach a zero misfit on this objective.

**(c)** "Better" is not supported by that ratio, because the two methods have
different cost *profiles*. The best-so-far table shows annealing at
$0.000\times10^{0}$ from a budget of $200$ evaluations upward, while the GA needs
$20\,000$ to reach zero — the reverse ordering of the medians — because annealing's
trajectory happens to hit a zero-misfit model almost immediately on this
two-dimensional objective while the GA must build one through recombination. The
honest conclusion is that the methods are ordered by *how* they spend the budget,
and that the ordering reverses with the objective's dimension and ruggedness.
Report the best-so-far curve; do not rank methods by a single budget.

**(d)** The four quantities are evaluations of the objective, the budget, the
success rate over seeds, and the best-so-far as a function of budget. For the
annealing run of §4.3: $20\,125$ median evaluations used, budget $20\,000$
evaluations per run (with the polish accounting for the small excess), success rate
$20/20$ at misfit $<10^{-3}$ but only $2/20$ at the true model, and a best-so-far
that is already $0$ at a budget of $200$ evaluations.

---

## ★★7 — Escape probability

**(a)** Each attempt escapes with probability $p\exp(-\Delta/T)$, so

$$P_{\text{escape}}(K) = 1 - \left(1 - p\,\mathrm{e}^{-\Delta/T}\right)^{K}.$$

**(b)** Setting the bracket to $q = 1 - p\mathrm{e}^{-\Delta/T}$ and requiring
$P \ge 1-\eta$ gives $K \ge \ln\eta/\ln q \approx \ln(1/\eta)/\left(p\mathrm{e}^{-\Delta/T}\right)$
for small $p\mathrm{e}^{-\Delta/T}$: the attempt count grows **exponentially** in
$\Delta/T$. Going from $\Delta/T = 5$ to $10$ divides
$\mathrm{e}^{-\Delta/T}$ by $\mathrm{e}^{5} = 148.4$, i.e. it multiplies the
required attempts by about **$148$**.

**(c)** With $p = 0.1$, $\Delta/T = 3$: $p\mathrm{e}^{-3} = 0.1\times0.049787 =
4.9787\times10^{-3}$, and

$$K = \frac{\ln(0.01)}{\ln(1 - 4.9787\times10^{-3})}
= \frac{-4.6052}{-4.9911\times10^{-3}} = \boxed{923}\ \text{attempts}.$$

**(d)** The exponential sensitivity to $\Delta/T$ is why the schedule matters more
than the proposal: a tenfold improvement in $p$ (a better-shaped proposal) reduces
$K$ tenfold, whereas a temperature a factor $\mathrm{e}$ higher reduces it by
$\mathrm{e}^{5}\approx148$-fold at $\Delta/T = 5$. Proposals determine *how often*
the barrier is offered; temperature determines *whether* the offer is taken, and it
enters exponentially.

---

## ★★8 — Reading the measured tables

**(a)** On the $400\times400$ grid the demonstration counts **48 local minima**,
finds the grid minimum $0.000\times10^{0}$ at $(1.0000, 3.0000)$ — the aliased
model — and confirms that the misfit at the true model $(2,3)$ is also
$0.000\times10^{0}$. The grid minimum is not the Earth: with an exact tie, the
grid returns whichever of the tied models happens to be a node of the grid.

**(b)** Of the 576 coordinate-descent runs, $249$ ($43.2$ per cent) reached a
zero-misfit model and $220$ ($38.2$ per cent) reached the *true* model. The
difference of $29$ runs is the population that found the aliased family instead:
about five per cent of all starts — and about $12$ per cent of the successful
starts — were funnelled into a basin whose minimum is a wrong model. "Success" and
"correctness" are therefore distinct statistics, and the gap measures how much of
model space drains to the wrong answer.

**(c)** Annealing: $20/20$ runs reached misfit $<10^{-3}$ (100 per cent) but only
$2/20$ ($10$ per cent) reached the true model. The GA: $20/20$ zero-misfit and
$15/20$ ($75$ per cent) true. Both methods are certain to find *a* zero-misfit
model and they disagree about which one by a factor of $7.5$ in the rate. That
difference cannot come from the data — the two models fit them exactly — so it
proves that the reported model depends on the search method, which is the lesson's
central claim.

**(d)** Restricting $v_1\in[1.8,2.2]$ km/s raised local descent from $38.2$ to
$58.9$ per cent ($339$ of $576$) and made annealing effectively deterministic for
the truth ($20$ of $20$ within the budget). The lesson: a prior removes the
competitor rather than out-searching it, and it is *cheaper* than more search
effort — but it is also an assumption, and if the restriction is wrong the answer
is wrong with certainty rather than with probability. Search effort cannot
substitute for information; it can only sample the information present.

---

## ★★★9 — Which of the seven minima do you get?

The experiment here is a Markov chain with the protocol stated in the exercise:
uniform start on $[-3,3]$, Gaussian proposals with
$\sigma = 0.5\,T/T_0 + 0.02$, Metropolis acceptance, best-so-far recorded, budget
$20\,000$, $T_0 = 0.5$, and **50 seeds**. Success is "misfit $<10^{-6}$"; landing
is "within $10^{-3}$ of $v = 0$".

| cooling rate | runs with misfit $<10^{-6}$ | runs landing on $v=0$ | median final misfit |
|---|---|---|---|
| $\rho = 0.9995$ | 50 of 50 | 6 of 50 | $5.1\times10^{-11}$ |
| $\rho = 0.995$ | 50 of 50 | 13 of 50 | $2.2\times10^{-11}$ |

**(b)** The success rate is 100 per cent for both schedules and conveys nothing:
the objective has seven exactly equivalent minima, so "did you reach a minimum?"
is answered yes by any chain that ends anywhere near an integer. The statistic that
carries information is the **distribution over the basins** — here, how often the
run ends at $v = 0$ against the other six integers — and, more generally, the
distribution of the final misfit or the set of models reached.

**(c)** Neither cooling rate produces a *better model*: both terminate at models
whose misfit is at the level of round-off, and the seven minima are exactly
equivalent, so there is no accuracy argument for either. What the cooling rate
controls here is the **distribution over the equivalent minima** — 6 of 50 against
13 of 50 at $v = 0$ — and the intuition "slower cooling is always better" fails not
because faster cooling is better, but because on an objective whose zero-set is
degenerate the notion of a better answer has no content: "did the run reach the
minimum?" is answered yes by any chain that settles near any integer. Where the
intuition *is* right is the case with a narrow global minimum among shallow
competitors, and the lesson's §4.6 supplies that counterexample with numbers: the
fast schedule kept a $95$ per cent success rate while the median final misfit
degraded by five orders of magnitude. The two results together make the point of
this exercise — the objective decides whether the schedule matters, so the schedule
must be justified from the objective rather than from a rule of thumb.

**(d)** With a single narrow global minimum, both statistics change in the expected
direction: the success rate becomes informative again (runs that freeze too early
get trapped in one of the shallower local minima created by the cosine ripple, and
the rate falls), and the basin distribution degenerates to a two-point statistic
(correct or not) rather than a seven-way one. The slow schedule should be expected
to win on both, because escaping a shallow local minimum requires accepted uphill
moves, which is exactly what a fast schedule removes. The measured version of this
statement is the lesson's §4.6.

---

## ★★★10 — Information beats search

**(a)** Measured, from the demonstration's table:

| misfit period (s) | local minima | grid minimum | descents reaching the truth |
|---|---|---|---|
| $0.5$ | 61 | $3.230\times10^{-4}$ | $59$ of $144$ ($41.0$ per cent) |
| $1.0$ | 9 | $8.075\times10^{-5}$ | $78$ of $144$ ($54.2$ per cent) |
| $2.0$ | 5 | $2.019\times10^{-5}$ | $137$ of $144$ ($95.1$ per cent) |

**(b)** The trend is the aliasing criterion operating in reverse. Phase wrapping
is harmless when the *predicted* spread of $\Delta t$ over the recorded offsets is
small compared with the period: then a model can never be wrong by a whole period,
so the wrap-around minima are not reachable and the families of §★★2 do not exist.
Doubling the period halves the number of periods spanned by the data, and the local
minima fall from 61 to 5 — an order of magnitude — while the success rate rises
from 41 to 95 per cent.

**(c)** The diagnostic is the ratio
$R = \left(\max_x\Delta t - \min_x\Delta t\right)/T$. Writing
$\Delta t(x) = x\alpha + x^{2}\beta$ with $\alpha = 1/2 - 1/v_1$ and
$\beta = 1/12 - 1/(4v_2)$, over $x\in[1,4]$ the spread is
$\max(3\alpha + 15\beta)$-type combinations of the two terms. The risk is present
when $R$ exceeds about $1$ — one full period of possible error — and it is
removed when $R\ll1$; the lesson's table is the same statement measured with $T$
as the control variable, and the halving of the minima count per doubling of $T$
is the visible signature.

**(d)** Two remedies, with their costs:

* **Record data that does not alias.** The lesson's §4.8(b) shows the effect: at
  $T = 2.0$ s the number of local minima falls by an order of magnitude and local
  descent becomes reliable ($95.1$ per cent). The cost is survey effort —
  broader-band or longer-offset acquisition — and it is the only remedy that adds
  information.
* **Impose a prior.** Restricting $v_1\in[1.8,2.2]$ km/s raised local descent to
  $58.9$ per cent and made annealing deterministic for the truth, at the cost of
  a hard assumption that is wrong exactly when it matters (a genuinely fast or
  slow shallow layer).
* (A third, weaker remedy is more search: restarts or a global method. It raises
  the probability of *a* zero-misfit answer without changing the set of tied
  models — as §4.2–4.4 measured: $43.2$ per cent zero-misfit against $38.2$ per
  cent correct — so it improves the success rate while leaving the
  ambiguity untouched.)

Stated briefly: search effort samples the existing ambiguity; survey design
removes it.
