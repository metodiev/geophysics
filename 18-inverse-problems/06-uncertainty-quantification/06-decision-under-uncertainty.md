---
id: 18-06-06
title: "Decision-Making Under Uncertainty and Value of Information"
level: research
prereqs: ["18-05-06", "18-06-01", "11-01-01"]
tags: [inverse-problems, uncertainty-quantification, decision-theory, value-of-information, risk]
---

# Decision-Making Under Uncertainty and Value of Information

All models and data in this module are **SYNTHETIC**. The resource volume, the
prices, the survey reliability and the hazard loss are chosen teaching values, and
the currency unit is dimensionless. Every number quoted is printed by
[`code/decision_under_uncertainty_demo.py`](./code/decision_under_uncertainty_demo.py).

## Learning objectives

By the end of this lesson you will be able to:

1. **Write** a decision problem as a set of actions, states and a loss, and
   **compute** the expected value of each action from a posterior.
2. **Derive** the break-even threshold of a binary decision and the cost-loss ratio
   of a protection decision.
3. **Derive** the expected value of perfect information as a difference of two
   expectations, and **verify** it against a closed form.
4. **Compute** the expected value of sample information from an imperfect survey,
   and **explain** why it can be exactly zero.
5. **Convert** expected values into certainty equivalents under risk aversion, and
   **find** the risk tolerance at which a decision changes.
6. **State** when information is worth acquiring, and when the value of information
   is a property of the decision rather than of the data.
7. **Report** a decision analysis so that the loss function, the prior and the
   assumed reliability are auditable.

## Prerequisites

- [18-05-06 Posterior Summaries: Marginals, Credible Intervals, Correlations](../05-bayesian-inversion/06-posterior-summary.md)
  — the posterior the decision averages over.
- [18-06-01 Taxonomy of Uncertainty: Aleatory, Epistemic, Structural](01-uncertainty-taxonomy.md)
  — which uncertainty the decision is exposed to.
- [11-01-01 The Exploration Lifecycle](../../11-exploration-geophysics/01-exploration-workflow/01-exploration-lifecycle.md)
  — the domain workflow in which these decisions are actually taken.

## 1. Intuition: uncertainty matters only through the decision it changes

An uncertainty report that does not change a decision has, for that decision, no
value. This is not a rhetorical point; it is computable. The value of information is
the difference between the expected value of acting with the information and the
expected value of acting without it, and it is zero whenever the information cannot
change the optimal action.

Three consequences follow, and they are the practical content of this lesson.

- **A very uncertain parameter that does not affect the action is not worth
  measuring.** The width of a posterior interval is not a measure of its importance.
- **A well-determined quantity can be worth a lot** if a small change in it flips a
  decision — the marginal case.
- **The value of information depends on the loss function**, so two users with
  different costs get different answers from the same data.

This is why the lesson sits at the end of the module: it is the reason the earlier
lessons bother to quantify anything at all.

## 2. The framework

A decision problem has three parts.

- **Actions** $a \in \mathcal{A}$: drill or not, protect or not, acquire the survey
  or not.
- **States** $V$: the unknown quantity, with posterior $p(V\mid d)$.
- **Loss** $L(a, V)$: what it costs to take action $a$ when the state is $V$; or,
  equivalently, a value (negative loss).

The **Bayes action** minimises the posterior expected loss,

$$
a^{*} = \arg\min_a \mathbb{E}_{V\mid d}\bigl[L(a,V)\bigr] .
$$

For a binary decision with a value $P V - C$ for acting and $0$ for not acting, the
action is taken when $\mathbb{E}[V\mid d] > C/P$: the **break-even volume**. The
demonstration's SYNTHETIC posterior is lognormal with median $8$ and
log-standard-deviation $0.6$, in volume units of $10^6\ \mathrm{m^3}$, so

$$
\mathbb{E}[V] = \exp\!\left(\ln 8 + \tfrac{0.6^2}{2}\right) = 9.5777,
$$

and with a value of $5$ per unit:

| cost | $\mathbb{E}[V]\cdot\text{value} - \text{cost}$ | action | $P(V > V^*)$ |
|---|---|---|---|
| 20.0 | $+27.8887$ | drill | 0.8760 |
| 40.0 | $+7.8887$ | drill | 0.5000 |
| 48.0 | $-0.1113$ | do not drill | 0.3806 |

At cost $48$ the project is rejected with $\mathbb{E}[V] = 9.5777$ only $0.23\%$
below the break-even mean $9.6$, even though $P(V > V^*) = 0.3806$. **The mean, not the
exceedance probability, prices the project** — and the two answers differ because
the distribution is skewed. A report that gives only $P(V>V^*)$ is answering a
question nobody asked.

### 2.1 The cost-loss ratio

For a protection decision — spend $C$ to protect, suffer $L$ if the hazard occurs,
nothing if it does not — the expected costs are $C$ for protecting and $pL$ for
not, so protection is optimal when

$$
p > \frac{C}{L} .
$$

The threshold is the **cost-loss ratio**, and it is a property of the economics, not
of the geophysics. At $C/L$ exactly, the two actions have identical expected cost and
the decision is a coin tossed by the posterior — which, as Section 5 shows, is
exactly where information is worth the most.

## 3. Expected value of perfect information, derived

The EVPI is the most a decision maker should pay for information that reveals the
true state before the action is chosen:

$$
\text{EVPI} = \mathbb{E}_V\!\left[\max_a \mathbb{E}\bigl[\text{value}\mid a, V\bigr]\right]
- \max_a \mathbb{E}_V\bigl[\text{value}(a,V)\bigr] .
$$

Two facts make it computable. First, it is by construction non-negative: the
expectation of a maximum is at least the maximum of expectations. Second, for the
binary drilling problem with a lognormal $V$ it has a closed form — the lognormal
option value:

$$
\mathbb{E}\bigl[\max(0, PV - C)\bigr]
= P\left[\mathbb{E}[V]\,\Phi(d_1) - \frac{C}{P}\,\Phi(d_2)\right],
$$

$$
d_1 = \frac{\mu + \sigma^2 - \ln(C/P)}{\sigma}, \qquad d_2 = d_1 - \sigma,
$$

with $V$ lognormal$(\mu,\sigma^2)$ and $\Phi$ the standard normal CDF. The
demonstration computes the EVPI both by simulation and from this formula:

| cost | EV without information | $\mathbb{E}[\max(0,\text{value})]$ simulated | EVPI simulated | EVPI closed form |
|---|---|---|---|---|
| 20.0 | $27.8887$ | $28.4983$ | $0.6096$ | $0.5831$ |
| 40.0 | $7.8887$ | $14.7726$ | $6.8839$ | $6.8664$ |
| 48.0 | $0.0000$ | $11.2651$ | $11.2651$ | $11.2508$ |

The two routes agree to within the Monte Carlo error, which is the standard of
evidence used throughout this module. **The EVPI rises as the decision becomes
marginal**: $0.58$ at cost $20$ where the decision is clear, $6.87$ at cost $40$,
and $11.25$ at cost $48$ where the project is nearly indifferent. Information is
worth most where it could change the action — not where the resource is largest.

## 4. Expected value of sample information, and a measured zero

A survey does not reveal $V$; it returns an indicator. The demonstration assumes a
binary indicator with sensitivity $p(\text{signal}\mid V > V_{\text{ind}})$ and
specificity $p(\text{no signal}\mid V \le V_{\text{ind}})$, with
$V_{\text{ind}} = 10$ volume units — deliberately *not* the break-even volume,
because a real survey measures something related to but different from the
decision quantity. With $p_{\text{sens}} = p_{\text{spec}}$ as given:

| $p_{\text{sens}}$, $p_{\text{spec}}$ | $P(\text{signal})$ | $\mathbb{E}[V\mid\text{signal}]$ | $\mathbb{E}[V\mid\text{no signal}]$ | EVSI (cost 20) | EVSI (cost 48) |
|---|---|---|---|---|---|
| 0.90, 0.90 | 0.3836 | 14.2623 | 6.6502 | 0.0000 | 8.9430 |
| 0.80, 0.80 | 0.4129 | 12.8412 | 7.2698 | 0.0000 | 6.6920 |
| 0.70, 0.70 | 0.4420 | 11.6063 | 7.9578 | 0.0000 | 4.4339 |
| 0.55, 0.55 | 0.4855 | 10.0321 | 9.1348 | 0.0000 | 1.0489 |
| 1.00, 1.00 (perfect) | 0.3550 | — | — | 0.6196 | 11.2508 |

Three readings, in order of importance.

**The same survey is worth nothing at cost $20$ and several units at cost $48$.**
At cost $20$ the decision is to drill whatever the signal says — every conditional
mean is above the break-even $4.0$ — so better information cannot change the action
and its value is exactly zero. At cost $48$ the decision is marginal, and the signal
flips it: the conditional means straddle the break-even $9.6$. **A survey is worth
what the decisions it changes are worth, and nothing more.**

**The value of the survey increases with its reliability**, monotonically in the
table from $0.55$ to $0.90$, and reaches the EVPI at a perfect sensor. The
perfect row is computed analytically rather than by simulation, because with
$p_{\text{sens}} = p_{\text{spec}} = 1$ the "no signal" subset is empty and a
simulated conditional mean is undefined.

**The survey's accuracy is not the survey's value.** The indicator separates
$V > 10$ from $V \le 10$, whereas the decision hinges on $V^* = 9.6$ at cost $48$
and on $4.0$ at cost $20$. A survey that is accurate about the wrong threshold buys
little. This is the practical form of the general rule: **the value of information
depends on the decision, the loss function and the prior, not on the data alone.**

## 5. Risk aversion, and where it changes the answer

Expected value is the right rule for a decision maker who is risk neutral. Others
are not. Under an exponential utility $U(x) = -\exp(-Ax)$, the **certainty
equivalent** of a random payoff is

$$
\text{CE} = -\frac{1}{A}\ln \mathbb{E}\bigl[e^{-A x}\bigr],
$$

which is the sure amount that the decision maker values equally to the lottery. The
demonstration computes the CE of drilling against the SYNTHETIC posterior:

| $A$ (per currency unit) | CE of drilling | action |
|---|---|---|
| 0.000 | $27.8522$ | drill |
| 0.005 | $25.6282$ | drill |
| 0.010 | $23.7833$ | drill |
| 0.020 | $20.8233$ | drill |
| 0.050 | $14.9639$ | drill |
| 0.100 | $9.3700$ | drill |
| 0.300 | $0.0441$ | drill |

and locates the flip by bisection at $A = 0.30164$ per currency unit, i.e. a risk
tolerance of $1/A = 3.315$ currency units. Note the shape: the CE at $A = 0$ is
$27.8522$, slightly below the expected value $27.8887$ because of the Monte Carlo
sampling of the payoff distribution; the two agree within the simulation error.

The point is not that risk aversion is right or wrong. It is that it changes the
action, and that it must therefore be stated. A report that gives "the expected
value is positive, so drill" has silently assumed risk neutrality, and a decision
maker with a different risk tolerance will decline the same project. Both are
legitimate; only the unstated one is a problem.

## 6. Where the value of information is largest

The demonstration's last section computes, by quadrature over a uniform prior on the
hazard probability, the value of perfect information for a protection decision with
loss $L = 50$ as a function of the protection cost $C$:

| $C$ | $C/L$ | $\mathbb{E}$[cost] without information | $\mathbb{E}$[cost] with perfect information | value of information |
|---|---|---|---|---|
| 5.0 | 0.100 | 5.0000 | 4.7500 | 0.2500 |
| 12.5 | 0.250 | 12.5000 | 10.9376 | 1.5624 |
| **25.0** | **0.500** | 25.0000 | 18.7501 | **6.2499** |
| 37.5 | 0.750 | 25.0000 | 23.4377 | 1.5623 |
| 45.0 | 0.900 | 25.0000 | 24.7502 | 0.2498 |

The value of information is largest when the cost-loss ratio is $0.5$ — that is,
when the decision threshold sits in the middle of the range the prior admits — and
smallest when it sits at either end, where the action is nearly certain whatever the
truth turns out to be. The table is symmetric about $C = L/2$, which is a check on
the computation as much as a result.

**Reporting rule.** Give the action, the loss function, the prior, the assumed
reliability of the information, and the EVSI with a statement of what it is compared
against. "The survey is worth acquiring" is not a finding unless the survey's cost
is stated and is below the EVSI.

## 7. Assumptions and regime of validity

1. **The loss function is the decision.** Change $C$ or $L$ and the action changes;
   a decision analysis without a stated loss function is not reproducible.
2. **The posterior must be the one used in the action.** Using a different
   distribution for the decision than for the report is a frequent and invisible
   error.
3. **Expected value is a choice.** Risk aversion changes the answer, as measured;
   state the utility or state that it is linear.
4. **Information is not free.** The EVSI must be compared with the acquisition cost,
   and the acquisition cost must include the time value of the delay.
5. **The likelihood of the information is assumed.** The EVSI is conditional on the
   survey's sensitivity and specificity; the demonstration shows the answer moving
   with them, and an unquantified reliability makes the EVSI unreliable.
6. **The state space must include the outcome that matters.** A binary action on a
   continuous volume is a simplification; decisions with three or more actions, or
   with sequential options, need the full dynamic-programming treatment, and the
   value of information can rise because later decisions also improve.
7. **A positive EVPI does not mean the information is obtainable.** It is an upper
   bound on what *any* survey could be worth.

## 8. Demonstration and exercises

[`code/decision_under_uncertainty_demo.py`](./code/decision_under_uncertainty_demo.py)
computes the break-even thresholds, the EVPI by simulation and by the closed-form
lognormal option value, the EVSI for four survey reliabilities at two costs, the
certainty equivalent under exponential utility with the flip located by bisection,
and the value of perfect information as a function of the cost-loss ratio. It prints
every table above with units and exits $0$ in about two seconds. Exercises and
solutions:
[`exercises/06-decision-under-uncertainty-exercises.md`](./exercises/06-decision-under-uncertainty-exercises.md),
[`exercises/06-decision-under-uncertainty-solutions.md`](./exercises/06-decision-under-uncertainty-solutions.md).

## Mastery checkpoint

**(a)** Derive the break-even volume $V^* = C/P$ from the expected value of drilling,
and state the condition in terms of $\mathbb{E}[V]$.
**(b)** Explain in two sentences why $\mathbb{E}[\max_a\text{value}] \ge
\max_a\mathbb{E}[\text{value}]$, and therefore why the EVPI cannot be negative.
**(c)** In the measured table the EVSI at cost $20$ is $0.0000$ for every imperfect
survey. Explain why that is exact rather than approximate.
**(d)** A colleague reports that a parameter has a wide credible interval and
therefore the survey that would narrow it must be valuable. State the error and the
computation that would settle the question.

## Common pitfalls

1. **Confusing $P(V > V^*)$ with $\mathbb{E}[V] > V^*$.** They differ whenever the
   distribution is skewed, and the measured example has $P = 0.3806$ with the
   decision already negative.
2. **Valuing information without a decision.** Measured: EVSI is exactly zero when
   the action cannot change.
3. **Using a symmetric interval for a skewed posterior in the decision.** The mean
   is not the median; the decision uses the mean, and the interval does not.
4. **Assuming risk neutrality silently.** The measured flip occurs at $A = 0.3016$,
   within the range a real decision maker might hold.
5. **Forgetting the acquisition cost.** A positive EVSI is not a business case.
6. **Assuming a survey's reliability.** The EVSI moved by a factor of $8.5$ across
   the reliability values in the table.
7. **Treating the EVPI as an achievable gain.** It is an upper bound.

## Further reading

- **Raiffa, H., & Schlaifer, R. (1961). *Applied Statistical Decision Theory*.
  Harvard Business School.** Level: research. The original development of the value
  of information.
- **Howard, R. A. (1966). Information value theory. *IEEE Transactions on Systems
  Science and Cybernetics*, 2(1), 22–26.** Level: research. EVPI and EVSI in the
  form used here.
- **Berger, J. O. (1985). *Statistical Decision Theory and Bayesian Analysis*
  (2nd ed.). Springer.** Level: research. Bayes actions, loss functions and
  admissibility.
- **Pratt, J. W. (1964). Risk aversion in the small and in the large.
  *Econometrica*, 32(1/2), 122–136.** Level: research. The exponential utility and
  the interpretation of its coefficient used in Section 5.

## Related modules

- [01 Taxonomy of Uncertainty: Aleatory, Epistemic, Structural](01-uncertainty-taxonomy.md)
  — which uncertainty the decision is exposed to.
- [05 Visualising and Communicating Uncertainty](05-uncertainty-visualisation.md) —
  the figures a decision is made from; the two lessons share the demand for an
  auditable statement.
- [18-05-06 Posterior Summaries](../05-bayesian-inversion/06-posterior-summary.md)
  and [18-05-07 Bayesian Evidence and Model Selection](../05-bayesian-inversion/07-evidence-and-model-selection.md)
  — the quantities a decision consumes.
- [06-seismology/11-04 Probabilistic Seismic Hazard Assessment](../../06-seismology/11-earthquake-statistics-and-hazard/04-psha.md)
  — a discipline organised around exactly this cost-loss logic.
- [11-01-03 Cost-Benefit Analysis in Exploration](../../11-exploration-geophysics/01-exploration-workflow/03-cost-benefit.md)
  — the domain version of Section 2.
