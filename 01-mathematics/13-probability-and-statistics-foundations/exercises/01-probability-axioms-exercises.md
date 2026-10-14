# Exercises — 01-13-01 Probability Axioms, Conditional Probability and Bayes' Rule

Attempt these closed-book before reading
[the solutions](./01-probability-axioms-solutions.md). The lesson is
[01-13-01](../01-probability-axioms.md).

Marking: ★ foundational, ★★ applied, ★★★ research-oriented.

Where a question asks for a probability, give it to four decimal places and say
what you rounded. Where a question asks you to choose a number, state the
assumption you chose it under — the assumption is part of the answer.

---

## ★ Foundational

**★1.** Two independent alarms each trigger on a genuine event with probability
$0.9$ and $0.8$ respectively. Compute (a) the probability that neither triggers,
(b) the probability that at least one triggers, (c) the probability that exactly
one triggers.

**★2.** A regional exploration programme examined 200 prospects. Forty contained a
target of interest. Of the 40 with a target, 34 gave a geophysical anomaly; of the
160 without, 24 gave an anomaly anyway.

(a) Compute $P(\text{anomaly})$.
(b) Compute $P(\text{target} \mid \text{anomaly})$.
(c) Compute $P(\text{anomaly} \mid \text{target})$.
(d) Which of (b) and (c) would you want when deciding whether to drill, and which
one does a forward model give you?

**★3.** For events with $P(A) = 0.4$, $P(B) = 0.5$ and $P(A \cap B) = 0.15$,
compute $P(A \cup B)$, $P(A^{c} \cap B^{c})$ and $P(A \cap B^{c})$.

**★4.** Three competing interpretations of a seismic section have priors
$0.20$, $0.30$, $0.50$. An observed amplitude ratio has likelihoods $0.60$,
$0.30$, $0.10$ under the three. Compute the evidence and the three posterior
probabilities.

---

## ★★ Applied

**★★5.** A prior puts odds of $1{:}3$ on hypothesis $H_1$ against $H_2$. Two
independent measurements arrive; their likelihood ratios for $H_1$ over $H_2$ are
$5$ and $2$. Compute the posterior odds and the posterior probability of $H_1$.

**★★6.** A screening method has sensitivity $0.98$ and specificity $0.95$, applied
where the target is present in $0.2\%$ of cases.

(a) Compute the probability of a positive result and the positive predictive value.
(b) Find the specificity required for the positive predictive value to reach $0.5$,
holding prevalence and sensitivity fixed.

**★★7.** A per-cell anomaly detector has a false-positive rate of $0.02$ and a
detection rate of $1.0$ on a grid of $10^{6}$ cells that contains, on average, $10$
genuine targets. Estimate the positive predictive value. What does the number say
about the usefulness of the per-cell test?

**★★8.** Two stations each detect a regional event with probability $0.85$, but
they share a power supply, so $P(\text{both detect}) = 0.80$ rather than the
independence value. Compute $P(\text{at least one detects})$ and compare it with
the independent case. By how many percentage points does the shared failure cost
you?

---

## ★★★ Research-oriented

**★★★9.** Derive the positive predictive value formula

$$\text{PPV} = \frac{\text{Se}\,\pi}{\text{Se}\,\pi + (1 - \text{Sp})(1 - \pi)}$$

from the definitions of sensitivity, specificity and prevalence. Then show
(i) that PPV increases with specificity, (ii) that PPV tends to $0$ as the
prevalence tends to $0$ for fixed Se and Sp, and (iii) that PPV $= 1$ only when
$\text{Sp} = 1$ or $\pi = 1$. Explain in one sentence what $\partial\text{PPV}/
\partial\text{Sp}$ being large when $\pi$ is small means operationally.

**★★★10.** You are asked to design a Monte Carlo study that verifies the PPV
formula of ★6 to a relative precision of $1\%$. The number of positive results
$P$ is random. Using the fact that the estimator $\widehat{\text{PPV}} = T/P$ with
$T \sim \text{Binomial}(P, \text{PPV})$ has relative standard error approximately

$$\frac{1}{\sqrt{P}}\sqrt{\frac{1 - \text{PPV}}{\text{PPV}}},$$

compute the number of positive results required, and hence the number of trials
needed. State every assumption you use, and explain why this design is preferable
to choosing an arbitrary round number of trials.

**★★★11.** A catalogue lists "precursor" signals and claims a detection rate of
$60\%$: six large events in ten are preceded by one. Over the same period there
were $400$ large events in $30\,000$ days, and signals of this kind occur on $2\%$
of quiet days.

(a) Compute the probability that a randomly chosen day carries a precursor, using
the claimed detection rate and the given false-signal rate.
(b) Compute the probability that a large event occurs on a precursor-bearing day,
given the base rate of large events, and compare it with the base rate itself.
(c) Explain why (b), and not the claimed $60\%$, is the quantity a decision-maker
needs, and state which assumption in (b) is least credible.

Use the numbers as stated and note explicitly where the independence assumption is
being made and why it is not credible.
