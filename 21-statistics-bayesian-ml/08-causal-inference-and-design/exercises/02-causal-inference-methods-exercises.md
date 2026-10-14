# Exercises — 21-08-02 Causal Inference Methods and Counterfactuals

Attempt these before reading the
[solutions](./02-causal-inference-methods-solutions.md). The lesson is
[02 Causal Inference](../02-causal-inference-methods.md). All numbers are
**SYNTHETIC**, printed by
[`code/causal_inference_methods_demo.py`](../code/causal_inference_methods_demo.py).

Study: $n = 2000$; $Z \sim \mathcal N(0,1)$ measured, $U \sim \mathcal N(0,1)$
unmeasured; $D = \mathbf 1\{Z+U>0\}$; $Y = 2.0D + 1.0Z + \varepsilon$; true ATE
$2.000$; treated fraction $0.499$; $\mathbb E[Z|D=1] - \mathbb E[Z|D=0] = 1.112$.

| Estimator | no unmeasured $U$ | with $0.8U$ |
|---|---|---|
| unadjusted difference | $+3.179 \pm 0.109$ | $+3.997$ |
| regression on $D$, $Z$ | $+2.116 \pm 0.103$ | $+3.233 \pm 0.124$ |
| inverse-probability weighting | $+2.241 \pm 0.150$ | $+3.392$ |
| propensity-quintile stratification | $+2.231$ | — |

With $U$ in the outcome: the marginal $U$ imbalance is $+1.083$, and the
coefficient of $D$ in a regression of $U$ on $(D, Z)$ is $+1.605$. The propensity
scores span $0.020$ to $0.980$.

## ★ Foundational

**★1.** Show algebraically that
$\mathbb E[Y|D=1] - \mathbb E[Y|D=0] = \mathrm{ATE} + \mathbb E[Y(0)|D=1] -
\mathbb E[Y(0)|D=0]$, and identify the second term as the selection bias.

**★2.** Using the confounding imbalance $1.112$ and the outcome coefficient $1.0$ on
$Z$, predict the unadjusted bias and compare it with the measured $+1.179$. State
the remaining discrepancy and its source.

**★3.** Compute the bias of each adjusted estimator in the no-$U$ case as a
percentage of the true effect, and state which estimator is the most precise and
which the least biased.

## ★★ Applied

**★★4.** State the omitted-variable formula, use it to predict the regression's bias
in the $U$ case, and explain why the relevant imbalance is the conditional $+1.605$
rather than the marginal $+1.083$.

**★★5.** Design the balance diagnostics that a weighting or matching study must
report. State the statistic, the threshold, and what an imbalance would imply for
the estimate.

**★★6.** Compute the weight distribution's effect on the estimate's variance: for a
propensity range $[0.02, 0.98]$, compute the maximum weight and the effective
sample size of the weighted estimator, and state what changes if the minimum
propensity falls to $0.001$.

## ★★★ Research-oriented

**★★★7.** Design a sensitivity analysis for unmeasured confounding: specify the
family of unmeasured confounders, the metric, the calibration of the sensitivity
parameters in the units of the problem, and the reported output.

**★★★8.** Design a study in which interference between units is the phenomenon of
interest (for example induced seismicity across a shared aquifer). State the
estimand, the design, the estimator, and why randomisation at the unit level fails.

**★★★9.** Specify the analysis that would distinguish "the treatment has no effect"
from "the treatment has an effect but the study cannot detect it", including the
power calculation, the minimum detectable effect, and the sensitivity of both to
the identification assumptions.
