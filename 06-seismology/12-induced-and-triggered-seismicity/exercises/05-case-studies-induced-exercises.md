# Exercises — 06-12-05 Documented Case Studies: Basel, Oklahoma, Groningen, Pohang

Attempt these before reading the
[solutions](./05-case-studies-induced-solutions.md). The lesson is
[05 Case Studies: Basel, Oklahoma, Groningen, Pohang](../05-case-studies-induced.md);
all numbers are printed by
[`../code/natural_vs_induced_demo.py`](../code/natural_vs_induced_demo.py). All
models are **SYNTHETIC**. The four named settings are used as *argument
archetypes*; no measured value from any of them is quoted, and this lesson makes
no factual claims about those projects.

## ★ Foundational

**★1.** An operations window lasts 16 months inside a 20-year catalogue. Compute
the probability that a randomly timed natural swarm falls inside it, and state
what assumption that calculation makes.

**★2.** State what an AUC of 0.5 means for a discriminant, and interpret the
demonstration's two values for the statistic "median distance from the well":
$0.965$ against ordinary natural swarms and $0.745$ against adversarial ones.

**★3.** The demonstration fits induced $b = 0.873 \pm 0.044$ and natural
$b = 0.899 \pm 0.045$. Form the difference and its combined standard error, and
state whether the two are distinguishable.

## ★★ Applied

**★★4.** The demonstration's Rule A is "induced if (median distance from the well
$< 4\ \mathrm{km}$) AND (depth-KS $p < 0.05$)", and Rule B adds
"(time-correlation $p < 0.05$)". Rule A calls $600/600$ induced sequences
correctly and also calls $600/600$ adversarial natural swarms induced; Rule B calls
$600/600$ correctly with $50/600$ false positives. Compute the false-positive rates
and state where all of Rule B's discriminating power sits.

**★★5.** Verify the demonstration's coincidence arithmetic: with $p = 0.0667$ per
window, compute $P(\text{at least one coincidence})$ for 1, 5, 10 and 30
independent windows and compare with $0.0667$, $0.2918$, $0.4984$ and $0.8738$.

**★★6.** The demonstration measures a false-positive rate of $0.0047$ for its 5%
time-correlation test on 1500 natural swarms, yet Rule B wrongly classifies
$50/600 = 8.3\%$ of adversarial swarms. If the time clause alone carried the
nominal $0.05$ rate, how many of the 600 would be misclassified? Reconcile the
three numbers and state which of them is a property of the *population
construction* rather than of nature.

## ★★★ Research-oriented

**★★★7.** Design a decision rule for attribution that reports a *posterior
probability* rather than a binary verdict, given the four statistics available
(median distance, depth test, time correlation, $b$-value). Specify the prior, the
likelihood for each statistic, and the one item of information you would need that
this module's models do not contain.

**★★★8.** The demonstration's adversarial natural swarms are placed at the well,
at the injection depth, and inside the operations window. Argue whether this is a
realistic null hypothesis or a strawman: state the physical settings in which such
a swarm is plausible, the ones in which it is not, and how the choice changes the
conclusion.

**★★★9.** A regulator asks which single additional observation would most reduce
the ambiguity in a specific case. Using the demonstration's AUC table, rank the
four statistics by how much new information each would need to become decisive, and
justify the ranking quantitatively. A ranking stated without a quantity is a failed
answer.
