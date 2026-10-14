# Exercises — 22-02-01 The Reproducibility Problem in the Computational Sciences

Attempt these before reading the
[solutions](./01-reproducibility-crisis-solutions.md). The lesson is
[01 The Reproducibility Problem](../01-reproducibility-crisis.md). All statistical
numbers use the **SYNTHETIC** model of `code/reproducibility_crisis_demo.py`:
unit noise $\sigma = 1$, two-sided $\alpha = 0.05$,
$\text{power} = \Phi(\delta\sqrt{n} - 1.959964)$.

## ★ Foundational

**★1.** Classify each failure as repeatability, reproducibility or replicability,
and name its category from the lesson's taxonomy: (a) a figure that changes when
the script is re-run without a seed; (b) a reader's run that uses newer library
versions and gets different numbers; (c) a second field campaign that finds a
weaker effect.

**★2.** Compute the power for an effect of $\delta = 0.4$ (in units of $\sigma$)
at $n = 20$, $n = 50$ and $n = 100$, using
$\text{power} = \Phi(\delta\sqrt{n} - 1.959964)$. State the expected replication
rate of a significant result at each $n$.

**★3.** For the demonstration's row $n = 30$, $\delta = 0.5$: state the power, the
number of significant studies out of 20 000, and the measured replication rate.
Explain in one sentence why the second and third numbers agree.

## ★★ Applied

**★★4.** Find the sample size for 80 % power at $\delta = 0.3$ by inverting
$1.959964 + 0.8416 = 0.3\sqrt{n}$, and check the answer against the
demonstration's power table ($n = 100$ gives 0.516 at $\delta = 0.2$; use the
$\delta = 0.3$ row of the replication table for a sanity check).

**★★5.** A study with 50 % power reports a significant effect of 0.6. Using the
lesson's winner's-curse table as a guide, state whether the reported value is more
likely to over- or under-state the true effect, and estimate the true effect if
the inflation factor is 1.2.

**★★6.** A paper tests 15 relationships, of which the authors believe about two
are real, and reports three significant at an uncorrected 5 % level. Using the
lesson's multiplicity model, estimate the expected number of false discoveries
and the false discovery proportion, stating the two inputs your estimate depends
on.

## ★★★ Research-oriented

**★★★7.** Design a replication study for a published effect of 0.3 in units of
the noise, with a sample size chosen for 90 % power, and state: the sample size,
the pre-registered decision rule, the prediction for the replication's effect
size (accounting for the winner's curse), and what you would report about the
original study if the replication is not significant. A specification that could
not be executed is a failed answer.

**★★★8.** The lesson's false discovery proportion is computed for 10 % of
hypotheses being truly non-zero. Derive the FDP as a function of the level
$\alpha$, the number of tests $m$, and the prior $\pi_1$, and find the prior at
which the mean FDP falls below 0.20 for $m = 20$ and $\alpha = 0.05$ (assume
power 1 for the true effects).

**★★★9.** Propose a measurement of the *repeatability* of a group's own pipelines
— not reproducibility, which needs a second team — and state the statistic, the
number of runs needed, and the confounder that would make the measurement
misleading. State what the measurement cannot tell you about the result's
correctness.
