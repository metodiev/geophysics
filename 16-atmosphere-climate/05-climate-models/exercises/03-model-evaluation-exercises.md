# Exercises — 16-05-03 Model Evaluation, Skill and Benchmarking

Attempt these before reading the [solutions](./03-model-evaluation-solutions.md).
Lesson: [03 Model Evaluation, Skill and Benchmarking](../03-model-evaluation.md).
All models and data are **SYNTHETIC**. The demonstration's truth has
$\sigma_o = 5.804\ \mathrm{K}$; run
[`../code/model_evaluation_demo.py`](../code/model_evaluation_demo.py) for the
full table.

## ★ Foundational

**★1.** A model has bias $+1.5\ \mathrm{K}$ and CRMSD $0.5\ \mathrm{K}$.
Compute its RMSE. State the general relation between bias, CRMSD and RMSE.

**★2.** Show algebraically that adding a constant $c$ to every model value
leaves both the correlation $r$ and the CRMSD unchanged.

**★3.** A model has mean squared error $2.5\ \mathrm{K^{2}}$ against a
climatological reference with mean squared error
$\sigma_o^{2} = 33.686\ \mathrm{K^{2}}$. Compute the skill score and interpret
it.

## ★★ Applied

**★★4.** The demonstration's *misplaced* model has
$\sigma_m/\sigma_o = 1.0049$ and $r = 0.8567$ against
$\sigma_o = 5.804\ \mathrm{K}$. Compute $\sigma_m$, the CRMSD and the RMSE, and
state why RMSE and CRMSD nearly coincide for this model.

**★★5.** The *smoothed* model has $\sigma_m/\sigma_o = 0.2991$ and
$r = 0.9961$. Compute its CRMSD and compare it with the misplaced model's.
Which term of the Taylor identity dominates in each case?

**★★6.** An evaluation reports $r = 0.45$ on $N = 100$ monthly values with a
lag-1 autocorrelation of $r_1 = 0.5$. Compute the effective sample size, the
approximate $95\%$ critical correlation, and state whether $r = 0.45$ is
significant.

## ★★★ Research-oriented

**★★★7.** Design a verification protocol for a seasonal forecast system using
feature-based (object-based) metrics. State the feature definition, the matching
rule, the attributes scored, and two ways the protocol can be gamed.

**★★★8.** A model update improves RMSE by $10\%$ while degrading the $99$th
percentile of daily temperature by $1\ \mathrm{K}$. Explain how both can be true
simultaneously, and state which result a heat-mortality warning system should
weight more heavily.
