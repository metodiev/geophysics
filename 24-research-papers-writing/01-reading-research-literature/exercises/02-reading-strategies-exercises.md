# Exercises — 24-01-02 Reading Strategies: Skim, Map, Deep-Read, Critique

Attempt these before reading the
[solutions](./02-reading-strategies-solutions.md). The lesson is
[02 Reading Strategies](../02-reading-strategies.md). All models are
**SYNTHETIC** teaching values.

## ★ Foundational

**★1.** A queue holds $120$ papers with a $20\%$ relevance prior. A triage rule
has sensitivity $0.85$ and specificity $0.90$. Using expected counts
$N_{\mathrm{TP}} = \text{sens}\cdot R$,
$N_{\mathrm{FP}} = (1-\text{spec})(N-R)$, compute the confusion counts, the
precision, the recall and $F_1$.

**★2.** With a skim at $3\ \mathrm{min}$, a map at $12\ \mathrm{min}$ and a deep
read at $45\ \mathrm{min}$, compute the hours for (a) deep-reading all $120$
papers, and (b) skimming all $120$ and deep-reading only the screen positives
from ★1. Express the saving as a percentage.

**★3.** Compute the information yield in content-units per hour for three passes:
$y = 0.20$ at $3\ \mathrm{min}$, $y = 0.50$ at $12\ \mathrm{min}$ and $y = 0.90$ at
$40\ \mathrm{min}$.

## ★★ Applied

**★★4.** Derive the prior relevance rate $p$ at which a two-pass strategy costs the
same as brute force, for $N = 240$ papers, skim $3\ \mathrm{min}$, deep read
$45\ \mathrm{min}$, sensitivity $0.90$ and specificity $0.82$. Show that no
$p \in [0,1]$ achieves break-even, and then compute the specificity that *would*
produce break-even at $p = 0.25$.

**★★5.** Using Bayes' rule, compute the expected precision of the screen of ★4 at
$p = 0.25$. Compare it with the measured precision of $64.7\%$ in the
demonstration and state whether the difference is within sampling noise, giving
the standard error you used.

**★★6.** In the demonstration the two-pass strategy captures $152.8$ of the
$228.0$ content-units that brute force captures, for $42.1\%$ of the time. If the
skim pass were made more careful so that its yield rose from $0.30$ to $0.50$,
compute the new content captured and the new percentage of brute force. Then state
the cost of that improvement in hours per paper.

## ★★★ Research-oriented

**★★★7.** Design a prospective study that measures whether the false negatives of
your triage rule matter. State the population of papers, the follow-up period, the
outcome that would count a paper as "should have been read", the sample size
justification, and the bias you cannot remove.

**★★★8.** Specify a calibration experiment for your own triage performance: how
you would estimate sensitivity and specificity prospectively, in what order the
labels are obtained so that the estimates are not circular, the target precision
of each estimate ($\pm 0.10$), and the number of papers required for each under a
binomial model.
