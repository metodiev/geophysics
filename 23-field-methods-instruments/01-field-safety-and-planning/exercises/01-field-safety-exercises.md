# Exercises — 23-01-01 Field Safety, Risk Assessment and Remote-Area Protocols

Attempt these before reading the
[solutions](./01-field-safety-solutions.md). The lesson is
[01 Field Safety](../01-field-safety.md). All ratings, probabilities and costs
are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** A register lists six hazards with $(L, S)$ ratings (2,5), (3,4), (4,2),
(1,5), (2,2) and (3,3). Compute each risk score $R = LS$, the total, the mean
and the ranking from highest to lowest. State which hazard has the highest
severity and where the product places it.

**★2.** Apply a control that halves the likelihood rating of every hazard in ★1,
with a floor of 1 (so $L = 1$ stays 1). Recompute the scores, the total and the
percentage reduction. How many hazards still score 5 or more?

**★3.** A campaign lasts 21 days and the per-check-in omission probability is
$p = 0.03$. Compute the number of check-ins, the expected number of alarms and
the probability of at least one alarm for $\tau = 8\ \mathrm{h}$ and
$\tau = 24\ \mathrm{h}$. Give the ratio of the two expected alarm counts.

## ★★ Applied

**★★4.** For $\tau = 18\ \mathrm{h}$, grace $g = 1.5\ \mathrm{h}$ and rescue
window $W = 12\ \mathrm{h}$, compute the expected wait to the next check-in, the
expected detection delay and the probability that the alarm is raised inside the
window. State the unit of each quantity.

**★★5.** A protocol must give $P(t_{\text{alarm}} \le W) \ge 0.95$ with
$W = 8\ \mathrm{h}$ and $g = 2\ \mathrm{h}$. Solve for the largest admissible
$\tau$, round down to a convenient value, and then compute the expected number of
alarms and the probability of at least one alarm over a 30-day campaign at
$p = 0.02$.

**★★6.** A severity-5 hazard starts at $L = 4$. Two controls are available, each
of which halves the likelihood rating, with a floor of 1. Compute the score
before, between and after the controls, and the reduction. Explain in two
sentences why the residual score cannot be brought below 5 by any number of
likelihood controls.

## ★★★ Research-oriented

**★★★7.** Design an experiment that measures the *alarm burden* of a check-in
protocol as a function of $\tau$ over a real campaign: state the metric
(alarms per 1000 person-days), the data you would log, the model you would fit,
and how you would separate a genuine incident from an omission. A specification
that could not be executed with a field notebook and a spreadsheet is a failed
answer.

**★★★8.** The omission probability $p$ in ★3 is assumed, not measured. Assuming
each check-in is an independent Bernoulli trial with a true (unknown) $p$,
compute the minimum number of check-ins needed so that observing *zero* alarms
would bound $p$ below 1 % with 95 % confidence. State the estimator, the
assumption, and one reason the assumption is optimistic for a real camp.
