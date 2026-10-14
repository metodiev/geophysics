---
id: 11-01-03
title: "Cost, Risk and Value of Information in Exploration"
level: doctoral
prereqs: ["11-01-01", "11-01-02", "21-03-01", "18-06-06"]
tags: [exploration-geophysics, value-of-information, decision-theory, risk, expected-value]
---

# Cost, Risk and Value of Information in Exploration

The first two lessons of this module built the funnel and the detectability
calculation. This one asks the question that decides whether either is worth
running: **what is a measurement worth before you buy it?** The answer is not a
property of the measurement. It is a property of the *decision* the measurement
changes, and it can be computed exactly for a stated decision problem. This lesson
derives the expected value of perfect information (EVPI) and of sample information
(EVSI), shows that a useless test is worth exactly zero, prices a test and the
optimal number of repeats, and then shows why value-of-information arithmetic is
itself a model whose inputs are uncertain.

**All models and data in this module are SYNTHETIC.** The success value, failure
cost, prior probability, test quality and test price below are chosen teaching
values, not figures from any real project, tender or company report.

## Learning objectives

By the end of this lesson you will be able to:

1. **Formulate** a drill-or-walk decision as an expected-monetary-value problem
   and **derive** the indifference probability $p^{*}=K/(W+K)$.
2. **Derive** the expected value of perfect information in closed form,
   $\mathrm{EVPI} = \min(pW,(1-p)K)$, and **explain** why it peaks exactly at the
   indifference probability.
3. **Apply** a likelihood ratio to update a prior into two posteriors, and
   **compute** the expected value of sample information
   $\mathrm{EVSI} = \sum_o \mathbb{P}(o)V(p|o)-V(p)$.
4. **Prove** that EVSI is never negative, that a test with
   sensitivity equal to its false-positive rate has EVSI exactly zero, and that
   the maximum price worth paying for a test is its EVSI.
5. **Compute** the optimal number of repeat tests from a concave EVSI and a
   linear cost, and **state** the independence assumption that makes the answer
   too optimistic.
6. **Demonstrate** that $E[V(p)] \ne V(E[p])$ and **quantify** the error made by
   plugging a best-estimate probability into a convex value function.
7. **State** the circumstances under which information has zero or negative net
   value, and why a value-of-information study is itself a model.

## Prerequisites

- [11-01-01 Exploration Lifecycle](01-exploration-lifecycle.md) — the staged
  structure whose decisions this lesson prices.
- [11-01-02 Targeting Strategy and Method Selection](02-targeting-and-strategy.md)
  — detection probability $P_d$ as the bridge from a survey to a decision.
- [21-03-01 The Bayesian Paradigm](../../21-statistics-bayesian-ml/03-bayesian-inference/01-bayesian-paradigm.md)
  — prior, likelihood and posterior.
- [18-06-06 Decision Under Uncertainty](../../18-inverse-problems/06-uncertainty-quantification/06-decision-under-uncertainty.md)
  — the general treatment of which this lesson is a special case.

## 1. The decision, written down

A decision problem has three ingredients: **states**, **actions** and a
**payoff**. Strip an exploration prospect to its essentials:

| | deposit ($S_1$) | barren ($S_2$) |
|---|---|---|
| **drill** ($a_1$) | $+W$ | $-K$ |
| **walk** ($a_2$) | $0$ | $0$ |

$W$ is the net value of a discovery *after* all costs (MUSD), and $K$ is the sunk
cost of a program that fails. With prior probability $p = \mathbb{P}(S_1)$, the
expected monetary value of drilling is

$$\mathrm{EMV}(a_1) = pW - (1-p)K, \qquad \mathrm{EMV}(a_2) = 0 .$$

The action rule is "drill if $\mathrm{EMV}(a_1) > 0$", and the **indifference
probability** solves $pW = (1-p)K$:

$$\boxed{\;p^{*} = \frac{K}{W+K}\;}$$

With the synthetic values $W = 500$ and $K = 60$ MUSD, $p^{*} = 60/560 =
0.10714$. The decision value function used throughout is its upper envelope

$$V(p) = \max\bigl(0,\; pW-(1-p)K\bigr) .$$

Three properties of $V$ matter for everything that follows: it is **piecewise
linear**, **convex** in $p$, and **flat at zero** below $p^{*}$. Convexity is why
information is valuable (a posterior spread around $p$ beats a point mass), and
flatness is why information can be worthless (if every posterior stays below
$p^{*}$, nothing changes).

## 2. The expected value of perfect information

Let an oracle reveal the true state *before* the decision. You then earn
$\max_a u(a,s)$ for each state instead of $\max_a \mathbb{E}_s[u(a,s)]$. The
difference is the expected value of perfect information:

$$\mathrm{EVPI} = \mathbb{E}_s\!\left[\max_a u(a,s)\right]
- \max_a \mathbb{E}_s\!\left[u(a,s)\right].$$

Evaluating the first term with the table above,

$$\mathbb{E}_s\!\left[\max_a u\right]
= p\max(W,0) + (1-p)\max(-K,0) = pW,$$

$$\mathrm{EVPI} = pW - \max\bigl(0, pW-(1-p)K\bigr)
= \begin{cases} pW & p < p^{*}\\ (1-p)K & p \ge p^{*}\end{cases}
= \boxed{\min\bigl(pW,\,(1-p)K\bigr)} .$$

The identity $\min$ is worth deriving rather than memorising: for $p<p^{*}$ the
second term is 0 and $\mathrm{EVPI} = pW$; for $p>p^{*}$ the second term is
$pW-(1-p)K$ and the difference is $(1-p)K$; exactly at $p^{*}$ both branches equal
$(1-p^{*})K = p^{*}W = KW/(W+K)$.

*Numerical check.* At $p = 0.15$: $\min(0.15\times500,\,0.85\times60)
= \min(75,51) = 51.00$ MUSD. The demonstration confirms the closed form against an
explicit state-and-action enumeration at seven values of $p$, agreeing to
$3.6\times10^{-15}$ MUSD at worst (the largest, $p = 0.80$).

**EVPI peaks at $p = p^{*}$.** A grid search over $2\times10^{5}$ values of $p$
locates the maximum at $p = 0.10715$, and the peak value is
$KW/(W+K) = 53.571$ MUSD. Information is worth most where the decision is *hard*.
At $p = 0.02$ the EVPI is $10.00$ MUSD and at $p = 0.80$ it is $12.00$ MUSD: a
confident explorer needs no advice. This is the single most transferable result in
the lesson, and it is the reason a "high-confidence, low-risk" program cannot
justify an expensive survey by VOI arguments.

## 3. Imperfect information: from a survey to two posteriors

A real survey returns a noisy indicator: an anomaly may be present ($+$) or
absent ($-$). Its operating characteristics are the **sensitivity** or true
positive rate $\mathrm{TPR} = \mathbb{P}(+|S_1)$ and the **false-positive rate**
$\mathrm{FPR} = \mathbb{P}(+|S_2)$. The marginal probability of a positive and the
two posteriors follow from Bayes' theorem:

$$\mathbb{P}(+) = p\,\mathrm{TPR} + (1-p)\,\mathrm{FPR}, \qquad
p_{+} = \frac{p\,\mathrm{TPR}}{\mathbb{P}(+)}, \qquad
p_{-} = \frac{p\,(1-\mathrm{TPR})}{1-\mathbb{P}(+)}.$$

Only the **likelihood ratio** at the observed outcome,
$\Lambda_{+} = \mathrm{TPR}/\mathrm{FPR}$, enters the update; the rest of the ROC
curve is irrelevant for a *given* outcome.

*Numerical check* (SYNTHETIC, $p = 0.15$, $\mathrm{TPR} = 0.80$,
$\mathrm{FPR} = 0.20$):

$$\mathbb{P}(+) = 0.15(0.80) + 0.85(0.20) = 0.12 + 0.17 = 0.290,$$

$$p_{+} = 0.12/0.290 = 0.41379, \qquad
p_{-} = 0.15(0.20)/0.710 = 0.042254 .$$

The decision after a positive is to drill with $V(p_{+}) = 171.72$ MUSD; after a
negative it is to walk, with $V(p_{-}) = 0$. **The test's entire value is created
in the branch where it changes the action.**

A Monte-Carlo check with $4\times10^{5}$ synthetic prospects returns
$\mathbb{P}(+) = 0.291457$, $p_{+} = 0.417042$ and $p_{-} = 0.042686$ against the
analytic $0.290000$, $0.413793$ and $0.042254$, within the binomial standard error
of about $0.0014$ for the posterior proportion.

## 4. EVSI, and why a useless test is worth exactly zero

Define the expected value of sample information for one test, before its cost:

$$\boxed{\;\mathrm{EVSI} = \mathbb{E}_o\bigl[V(p|o)\bigr] - V(p)
= \mathbb{P}(+)V(p_{+}) + \mathbb{P}(-)V(p_{-}) - V(p)\;}$$

For the numbers above: $0.290(171.724) + 0.710(0) - 24.000
= 49.800 - 24.000 = 25.800$ MUSD.

**EVSI is never negative.** Proof: the strategy "ignore the observation and take
the same action as before the test" is always feasible, and $V$ is defined as the
best achievable value; therefore $\mathbb{E}_o[V(p|o)] \ge V(p)$. The inequality
is strict only when the observation sometimes changes the action.

**A test with $\mathrm{TPR} = \mathrm{FPR}$ has EVSI = 0 exactly.** Then
$\Lambda = 1$ at both outcomes, so $p_{+} = p_{-} = p$ and
$\mathbb{E}_o[V] = V(p)$. The demonstration verifies this numerically for
$\mathrm{TPR} = \mathrm{FPR} = 0.5$, $0.7$ and $0.9$: EVSI $= 0.000\times10^{0}$
MUSD in each case. **Accuracy is not value.** A test that is 90% accurate but
equally likely to fire on a barren prospect as on a deposit changes nothing, and
should not be bought at any price.

The EVSI/EVPI ratio measures how much of the ideal a test recovers:

| TPR | FPR | EVSI (MUSD) | EVSI − cost (MUSD) |
|---|---|---|---|
| 0.50 | 0.50 | 0.000 | −3.000 |
| 0.60 | 0.50 | −0.000 | −3.000 |
| 0.80 | 0.20 | 25.800 | 22.800 |
| 0.90 | 0.10 | 38.400 | 35.400 |
| 0.95 | 0.05 | 44.700 | 41.700 |
| 0.99 | 0.01 | 49.740 | 46.740 |

EVPI is $51.00$ MUSD, so the $\mathrm{TPR} = 0.80$, $\mathrm{FPR} = 0.20$ test
recovers $50.6\%$ of it.

## 5. The price of a test, and how many

The **maximum price worth paying** for a test is exactly its EVSI: above that
price the net expected gain is negative. That gives a clean procurement statement:
with EVSI $= 25.800$ MUSD, a quoted price of $3.0$ MUSD leaves a net gain of
$22.800$ MUSD, and the survey is worth running.

Repeating a test is an optimal-stopping problem. Each test is applied to the
current posterior, and the sequence stops at the first positive (you act) or after
a fixed number of negatives (you walk). Evaluating this by backward induction:

| $n$ tests | EVSI (MUSD) | net of cost | marginal |
|---|---|---|---|
| 1 | 25.800 | 22.800 | 22.800 |
| 2 | 29.640 | 23.640 | 0.840 |
| 3 | 29.640 | 20.640 | −3.000 |
| 4 | 29.640 | 17.640 | −3.000 |

**Two tests are optimal; the third adds nothing and costs 3 MUSD.** EVSI is
bounded above by EVPI and here saturates after two tests, while the cost is
linear, so a finite optimum must exist. The saturation is not an accident of the
numbers: after two negatives $p = 0.0109$, and no further negative can change the
decision, so the third test only pays in a branch whose probability is already
small.

The demonstration checks the backward induction against an explicit enumeration of
the four outcome classes of a three-test program (0, 1, 2 negatives then a
positive, plus all-negative), with probabilities $0.2900$, $0.1600$, $0.1136$ and
$0.4364$: the enumerated expectation is $53.6400000000$ MUSD and the recursion
gives $53.6400000000$ MUSD, a difference of $0$.

## 6. Worked example — the frontier of buying information

An explorer holds ten independent prospects identical to the SYNTHETIC one above.
By construction $W = 500$ MUSD is the value of a discovery **net of every cost
including the drilling that found it**, and $K = 60$ MUSD is the loss on a
program that fails. This accounting convention is the one that prevents the
commonest error, which is to subtract $K$ a second time.

1. **No information.** Drill all ten: $10 \times 24.000 = 240.0$ MUSD.
2. **Perfect information.** Drill only the deposits: $10 \times pW =
   10 \times 75.000 = 750.0$ MUSD. The difference, $750.0 - 240.0 = 510.0$
   MUSD, is exactly $10 \times \mathrm{EVPI}(0.15) = 10 \times 51.00$: the closed
   form and the two scenarios agree, which is the check.
3. **The imperfect test at 3.0 MUSD per prospect.** Net expected value per
   prospect $= 24.000 + 25.800 - 3.000 = 46.800$ MUSD, so $468.0$ MUSD over ten
   against $240.0$ MUSD blind. The test captures
   $25.800/51.00 = 50.6\%$ of the perfect-information value, and the remaining
   $49.4\%$ is unreachable at any price because the test is noisy.

The trap this example exposes: if $W$ had been defined *gross* of drilling cost,
step 2 would need $10\,pK = 90$ MUSD subtracted, and a careless calculation that
used the net-$W$ table with the gross-$W$ arithmetic would double-count $K$. Every
VOI number is only interpretable alongside the payoff table that produced it.

## 7. The flaw of averages

Suppose the prior probability is not known exactly but distributed,
$p \sim \mathrm{Beta}(1.8, 10.2)$ with mean $0.15$ — a SYNTHETIC statement of "we
believe about 15%, and we are not certain". The value function is convex in $p$,
so Jensen's inequality applies:

$$\mathbb{E}[V(p)] \ge V(\mathbb{E}[p]) .$$

Quadrature over a fine grid gives

| Quantity | Value |
|---|---|
| $\mathbb{E}[p]$ | 0.150000 |
| $V(\mathbb{E}[p])$ | 24.0000 MUSD |
| $\mathbb{E}[V(p)]$ | 34.1866 MUSD |
| Jensen gap | **+10.1866 MUSD (+42.4%)** |

Plugging the best-estimate probability into the value function **understates** the
expected value by $42\%$. The reason is that the decision is an option: the
upside branch is retained and the downside branch is truncated at zero by the
"walk" option. Any analysis that reports a single point value from a single point
probability is, for this decision structure, biased downward — and by an amount
that grows with the spread of the probability. The same mechanism produces the
"volatility increases option value" result of real-options analysis, of which this
two-action problem is the smallest possible example.

## 8. Portfolio risk and a shared failure mode

Twenty independent prospects at $p = 0.15$ give $\mathbb{E}[\text{deposits}]
= 3.00$ and $\mathbb{P}(\text{at least one}) = 1-0.85^{20} = 0.9612$. Now suppose
the whole belt concept can be wrong: with probability $q$ the concept fails and
then *every* prospect is barren. This is a shared failure mode, not an independent
one:

| $q$ | $\mathbb{P}(\text{at least one})$ | $\mathbb{E}[\text{deposits}]$ |
|---|---|---|
| 0.00 | 0.9612 | 3.00 |
| 0.20 | 0.7690 | 2.40 |
| 0.40 | 0.5767 | 1.80 |
| 0.60 | 0.3845 | 1.20 |

Two things change. The mean falls proportionally, as it must — but the
**probability of a complete failure rises much faster than the mean falls**:
at $q = 0.20$ the mean is down $20\%$ while $\mathbb{P}(\text{zero})$ goes from
$0.039$ to $0.231$, nearly a sixfold increase. A portfolio is a diversification
device against independent risk and no device at all against a wrong regional
concept, which is exactly the risk that regional geophysics is bought to reduce.
The correlation structure, not the number of targets, sets the portfolio's tail.

## 9. Assumptions and regime of validity

1. **Risk neutrality.** $V$ maximises expected money. A company that is
   capital-constrained, or an individual whose career ends with one dry hole, is
   not risk neutral, and for them the correct objective is a utility, not an EMV.
   Every number in this lesson is a risk-neutral benchmark.
2. **$W$ and $K$ are known constants.** They are estimates with their own ranges,
   and $\mathrm{EVPI} = \min(pW,(1-p)K)$ *increases* with the uncertainty in them
   rather than averaging it out. This is the second-order uncertainty that
   dominates real VOI studies.
3. **Two actions only.** No option to delay, to expand, to sell the prospect, or
   to drill a cheaper first hole. Real options are worth more than the "act now"
   value computed here.
4. **Tests are conditionally independent given the state.** Two repeat surveys via
   the same physics on the same line are strongly correlated; the optimal-$n$
   calculation above is therefore optimistic, and the correlation reduces EVSI
   toward the single-test value (see [11-02-07](../02-mineral-exploration/07-multi-method-targeting.md)).
5. **The indicator is calibrated.** TPR and FPR are assumed to be known
   *conditional on the target model being right*. If the target model is wrong, the
   "test" is measuring something else and the ROC curve is fiction.
6. **No timing.** A survey that arrives after the budget cycle, or after a
   competitor has staked the ground, has had its value destroyed by delay. VOI
   computed without a clock systematically overvalues slow information.
7. **The decision model is correct.** Every value here is conditional on the
   payoff table. Change $K$, and $p^{*}$ moves; change the number of actions, and
   $V$ changes shape; get the prior wrong, and EVSI is computed at the wrong place
   on a curve that is steep near $p^{*}$ and flat far from it. **A
   value-of-information study is a model, and it is the one model in this module
   whose output is a dollar figure.** That is why it deserves more scepticism than
   the geophysics.

## 10. Units, scaling and consistency checks

| Quantity | Unit | Check |
|---|---|---|
| $W$, $K$ | MUSD | money per decision |
| $p$ | – | probability |
| EMV | MUSD | $pW$ is money ✔ |
| EVPI, EVSI | MUSD | differences of \(V\) values ✔ |
| EVSI/EVPI | – | both MUSD, ratio dimensionless ✔ |

Four identities make good self-checks on any VOI calculation:

1. $\mathrm{EVPI} \ge \mathrm{EVSI} \ge 0$;
2. $\mathrm{EVPI} = \min(pW,(1-p)K)$ for this payoff table;
3. $\mathrm{EVPI} = 0$ at $p = 0$ and at $p = 1$;
4. $\mathrm{EVSI} = 0$ whenever $\mathrm{TPR} = \mathrm{FPR}$, for any $p$.

If any of these fails numerically, the code is wrong, and the demonstration
verifies all four.

## 11. Exercises

Full sets with worked solutions:
[`exercises/03-cost-benefit-exercises.md`](exercises/03-cost-benefit-exercises.md)
and
[`exercises/03-cost-benefit-solutions.md`](exercises/03-cost-benefit-solutions.md).

## Mastery checkpoint

Without notes:

> A SYNTHETIC prospect has $W = 800$ MUSD, $K = 100$ MUSD and prior
> $p = 0.08$. A survey has $\mathrm{TPR} = 0.70$, $\mathrm{FPR} = 0.10$ and costs
> $5$ MUSD. **(a)** Compute $p^{*}$ and the EMV of drilling now. **(b)** Compute
> $\mathbb{P}(+)$, $p_{+}$, $p_{-}$. **(c)** Compute EVSI and the net expected
> gain, and state whether the survey is worth buying. **(d)** Compute the EVPI and
> the fraction of it the survey captures. **(e)** State the two assumptions whose
> failure would most reduce your answer, and say which you would test first.

A worked version of (a)–(d) is in the
[solutions](exercises/03-cost-benefit-solutions.md).

## Common pitfalls

1. **Buying accuracy instead of value.** A test that is accurate but does not
   change an action has EVSI = 0; report the ROC *jointly*, not one number.
2. **Comparing "with information" and "without" totals that count different
   costs.** Both sides must include the same drilling and head-office costs.
3. **Reporting EVPI as achievable.** EVPI is an upper bound; only EVSI is
   purchasable.
4. **Ignoring the price.** EVSI is the maximum price, not the value of the survey
   in the ground; net EVSI is the decision-relevant quantity.
5. **Plugging a mean probability into a convex value function.** The Jensen gap in
   §7 was $+42\%$; the bias has a direction and a size, and both are computable.
6. **Assuming repeat tests are independent.** They usually are not, and the
   optimal-$n$ table above is optimistic for that reason.
7. **Treating EVPI as scale-free.** $\min(pW,(1-p)K)$ is proportional to the money
   at stake, so a VOI result cannot be transferred between projects without
   carrying the whole payoff table.
8. **Forgetting that the answer moves with the prior.** EVSI is computed at $p$;
   near $p^{*}$ it is steeply sensitive, and far from $p^{*}$ it is nearly flat.

## Related modules

- [11-01-01 Exploration Lifecycle: Reconnaissance to Reserve Definition](01-exploration-lifecycle.md)
  — the sequential decisions that a real program optimises over.
- [11-01-02 Targeting Strategy and Method Selection](02-targeting-and-strategy.md)
  — where the $P_d$ that feeds this lesson's likelihood ratio comes from.
- [11-02-07 Multi-Method Targeting and Prospectivity Analysis](../02-mineral-exploration/07-multi-method-targeting.md)
  — what happens to EVSI when the tests are correlated.
- [18-06-06 Decision Under Uncertainty](../../18-inverse-problems/06-uncertainty-quantification/06-decision-under-uncertainty.md)
  — the general theory, including utility and real options.
- [05-07-05 Reporting Geophysical Results with Honest Uncertainty](../../05-core-geophysics/07-interpretation-and-integration/05-reporting-results.md)
  — how to write down a $P_d$ or a probability so that this arithmetic can be
  checked by a reader.
