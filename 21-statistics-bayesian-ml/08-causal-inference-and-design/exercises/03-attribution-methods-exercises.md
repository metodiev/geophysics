# Exercises — 21-08-03 Attribution in Climate and Hazard Science

Attempt these before reading the
[solutions](./03-attribution-methods-solutions.md). The lesson is
[03 Attribution Methods](../03-attribution-methods.md). All numbers are
**SYNTHETIC**, printed by
[`code/attribution_methods_demo.py`](../code/attribution_methods_demo.py).

Setup: 2000 seasons per world; counterfactual covariate $X \sim \mathcal N(0,1)$,
factual $X \sim \mathcal N(1,1)$; event probability
$\mathrm{sigmoid}(-2.0 + 1.5X)$; exact marginal probabilities $0.19005$ and
$0.41240$.

| Quantity | Value | 95% bootstrap |
|---|---|---|
| events, counterfactual / factual | $378$ / $800$ | — |
| probability ratio | $2.116$ | $1.903$ to $2.346$ |
| attributable fraction | $0.527$ | $0.475$ to $0.574$ |
| return period (counterfactual / factual) | $5.3$ / $2.5$ seasons | — |
| logistic $a$, $b$, $c$ | $-1.994 \pm 0.145$, $+1.545 \pm 0.113$, $-0.145 \pm 0.180$ | — |
| conditional risk ratio $\exp(c)$ | $0.865$ | $0.723$ to $1.036$ |

Rarer events ($a$ is the logit intercept):

| $a$ | cf events | fact events | PR | 95% interval | width |
|---|---|---|---|---|---|
| $-2.0$ | 374 | 811 | 2.17 | 1.95 to 2.42 | 0.46 |
| $-3.5$ | 123 | 385 | 3.13 | 2.60 to 3.80 | 1.21 |
| $-4.5$ | 56 | 188 | 3.36 | 2.55 to 4.58 | 2.03 |

## ★ Foundational

**★1.** Derive $\mathrm{FAR} = 1 - 1/\mathrm{PR}$ from the definitions, compute it
for $\mathrm{PR} = 1.2$, $2.116$ and $5$, and state the limit as
$\mathrm{PR} \to 1$.

**★2.** Convert the measured probability ratio into the return-period ratio and
verify against the printed $5.3$ and $2.5$ seasons. State what a return period of
$2.5$ seasons means for a statement about a specific season.

**★3.** Compute the relative standard error of a ratio of counts with
$n_{\text{cf}} = 378$ and $n_{\text{fact}} = 800$, and compare with the measured
interval width of $0.443$ on a ratio of $2.116$ (i.e. $\pm21\%$).

## ★★ Applied

**★★4.** Explain why the conditional risk ratio $\exp(c)$ is consistent with 1
while the marginal ratio is $2.116$, and construct a modified generator in which
$\exp(c) > 1$. State what physical situation the modification represents.

**★★5.** Design the experiment that measures the ensemble size needed to attribute
an event with a counterfactual frequency of $1/100$ seasons to $\pm20\%$ at 95%
confidence. State the generator, the metric, the sizing and the assumption about
independence between ensemble members.

**★★6.** The covariate definition differs between the observational series and the
model ensemble by a bias of $0.3$ in the covariate units. Compute the resulting bias
in the probability ratio for this generator, using the fitted $b = 1.545$, and state
which way it moves the attribution.

## ★★★ Research-oriented

**★★★7.** Design the sensitivity analysis for the choice of event threshold. State
the family of thresholds, the metric, the plot, and the threshold-selection rule
that would keep the analysis pre-specified.

**★★★8.** Design an attribution study for a compound event (two variables exceeding
their thresholds together). State the event definition, the covariate, the statistic,
the additional assumptions over a single-variable event, and the failure mode that
compound analysis introduces.

**★★★9.** A study reports a probability ratio of 12 for a rare event and a
modelled change in return period from 100 to 8 years. Specify the audit you would
perform, listing the five quantities you would request and, for each, the result
that would falsify the claim.
