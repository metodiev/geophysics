# Exercises — 24-06-03 Interactive Publications and Notebooks as Articles

Attempt these before reading the
[solutions](./03-notebooks-as-publications-solutions.md). The lesson is
[03 Notebooks as Publications](../03-notebooks-as-publications.md). All numbers are
**SYNTHETIC** teaching values.

## ★ Foundational

**★1.** A notebook has $25$ cells, each executed out of source order with probability
$0.30$, and each such execution creating a hidden dependency with probability $0.03$.
Compute the per-cell hazard and the probability of at least one hidden dependency.

**★2.** Compute the same probability for $5$, $10$, $50$ and $100$ cells, and state the
trend in one sentence.

**★3.** State the three observable symptoms of hidden state and which of them is
visible without running the notebook.

## ★★ Applied

**★★4.** A notebook fails on a clean re-run with probability $0.30$ from hidden state
and $0.04$ from environment differences. Compute the probability that it fails for at
least one reason and the probability that it reproduces cleanly.

**★★5.** Pinning the environment reduces the environment failure probability from
$0.05$ to $0.01$ while hidden state remains at $0.30$. Compute total failure before
and after pinning, and the same two numbers if hidden state were removed. State which
change matters more.

**★★6.** A $100$-cell notebook reproduces with probability $0.35$. Compute the
reproduction probability of five $20$-cell notebooks, each reproducing with probability
$0.86$, both as "all five reproduce" and as "at least four reproduce".

## ★★★ Research-oriented

**★★★7.** Design a study measuring whether an automated execution-order test in
continuous integration reduces the rate of notebooks that fail on a reader's machine.
State the unit, the outcome, the design, and the confound that repositories adopting
the test are also better maintained.

**★★★8.** Specify an analysis of notebooks in published supplementary material: the
sampling, the three offline-checks used to detect hidden state without executing
anything, the agreement statistic between coders, and why offline detection
underestimates the true failure rate.
