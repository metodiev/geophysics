# Exercises — 21-03-06 Bayesian Workflow and Principled Model Building

Attempt these before reading the
[solutions](./06-bayesian-workflow-solutions.md). The lesson is
[06 Bayesian Workflow](../06-bayesian-workflow.md). All data are **SYNTHETIC**;
numbers quoted from the demonstration reproduce its output.

## ★ Foundational

**★1.** List the seven stages of the workflow and, for each, state one thing the
stage can falsify.

**★2.** A prior predictive simulation with a $\mathrm{Gamma}(2, \text{rate }1)$
prior gives counts with a $95\ \%$ range of $[0, 7]$ and a mean of $1.9709$; the
observed data have range $[0, 6]$ and mean $1.9000$. State the conclusion and one
prior that this check would have rejected.

**★3.** Exact leave-one-out gives $\mathrm{elpd} = -64.92$ for a plug-in model
and $-64.94$ for a conjugate model with a difference standard error of $0.12$.
Compute the $z$-score of the difference and state the conclusion.

## ★★ Applied

**★★4.** Write the Bayesian $p$-value for a posterior predictive check and
explain why the check statistic must be chosen before the posterior is inspected.

**★★5.** The demonstration reports $\mathrm{lppd} = -64.08$ and
$p_{\text{WAIC}} = 0.87$. Compute the WAIC, convert it to an elpd scale, and
compare it with the exact LOO value of $-64.94$.

**★★6.** A posterior predictive check gives an observed dispersion of $0.8853$
against a replicated $95\ \%$ range of $[0.6022, 1.5501]$, with $67.2\ \%$ of
replicates at least as dispersed. State what the check has established and what
it has not.

## ★★★ Research-oriented

**★★★7.** Specify a **check-calibration study** that measures the power of a
posterior predictive check to detect a specific misspecification: a Poisson model
fitted to over-dispersed counts. State the data-generating process, the check
statistic, the replicate count, and the predicted detection rate as a function of
the dispersion. A specification that could not be executed is a failed answer.

**★★★8.** Design a **workflow-reproducibility study**: an experiment that
measures how often two analysts, given the same data and the same seven-stage
protocol, reach materially different posterior summaries. State what varies
between the analysts, the metric, the replicate count, and the predicted
sensitivity to the prior choice.
