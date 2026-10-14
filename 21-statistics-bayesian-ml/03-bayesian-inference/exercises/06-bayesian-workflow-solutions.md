# Solutions — 21-03-06 Bayesian Workflow and Principled Model Building

> Read after attempting. Lesson:
> [06 Bayesian Workflow](../06-bayesian-workflow.md). Numbers quoted from the
> demonstration reproduce its output.

---

## ★1 — The stages and what each can falsify

| stage | can falsify |
|---|---|
| 1. specify the model | whether the likelihood and prior encode the scientific claim actually made |
| 2. prior predictive check | a prior that excludes the observed scale or structure |
| 3. compute the posterior | a sampler or optimiser that has not converged, or a wrong target |
| 4. posterior predictive check | a likelihood that cannot reproduce a chosen feature of the data |
| 5. model comparison | a model that predicts held-out data worse than a competitor |
| 6. sensitivity | a conclusion that depends on an arbitrary prior choice |
| 7. report | an analysis that cannot be repeated or checked by another analyst |

Each stage falsifies something different, which is why running only stages 1 and
3 — the common shortcut — leaves the two most informative checks untested.

---

## ★2 — Prior predictive check

The observed range $[0, 6]$ lies inside the predictive range $[0, 7]$, and the
observed mean $1.9000$ is within $0.07$ of the predictive mean $1.9709$. The
prior is **compatible** with the data, so it survives the check.

A prior that the check **would** have rejected is one centred far from the
observed scale — for instance a $\mathrm{Gamma}(200, 10)$ prior with mean $20$,
whose predictive $95\ \%$ range would be roughly $[12, 28]$ and would exclude
every observed value. This is the value of the check: it costs one simulation and
catches an impossible specification before any posterior is computed, where the
error would otherwise appear only as an implausible answer.

---

## ★3 — Is the comparison decisive?

$$z = \frac{\Delta\mathrm{elpd}}{\mathrm{se}(\Delta)}
= \frac{-64.94 - (-64.92)}{0.12} = \frac{-0.02}{0.12} = -0.17 .$$

A $0.17\sigma$ difference. The two models are **indistinguishable**: the
conjugate model's extra structure buys nothing detectable at $N = 40$ on
near-Poisson data. The correct report states the difference **with its standard
error**, notes that it is far below the usual $2\sigma$ threshold, and prefers the
simpler model on parsimony grounds. Quoting "$-64.94$ versus $-64.92$" as a win
for the plug-in model would be a misuse of the comparison.

---

## ★★4 — The Bayesian $p$-value and why the statistic is fixed first

$$p_B = \Pr\big(T(y^{\text{rep}}) \ge T(y)\big),$$

estimated by the fraction of posterior-predictive replicates whose statistic
$T(y^{\text{rep}})$ is at least as large as the observed $T(y)$.

**Why the statistic must be chosen first.** $p_B$ has no calibration: it is not a
uniform random variable under the null, and there is no correction for the number
of statistics examined. Computing many statistics and reporting the most extreme
turns the check into a search, exactly as reporting the smallest of many
$p$-values does in frequentist practice. Pre-specifying $T$ — ideally a feature
the model is suspected of getting wrong — keeps the check honest; reporting the
full simulated distribution rather than a single number makes it informative even
when it passes.

---

## ★★5 — WAIC arithmetic and the cross-check

$$\mathrm{WAIC} = -2(\mathrm{lppd} - p_{\text{WAIC}})
= -2(-64.08 - 0.87) = -2(-64.95) = 129.90 .$$

On the elpd scale,

$$\frac{\mathrm{WAIC}}{-2} = -64.95 .$$

The exact leave-one-out value for the same model is $-64.94$, so the two agree to
$0.01$ — an order of magnitude smaller than the LOO standard error of $4.40$. The
agreement is the evidence that the posterior is close enough to normal, and $n = 40$
large enough, for the asymptotic approximation to hold here. It is worth
remembering that this is a *check*, not a guarantee: on a smaller or more skewed
posterior, WAIC and LOO can differ substantially, and the exact or PSIS-based LOO
is then the reference.

---

## ★★6 — What the predictive check established

**Established.** The Poisson model, with the fitted rate, reproduces the
dispersion of the data: the observed variance/mean ratio $0.8853$ sits well
inside the replicated $95\ \%$ range $[0.6022, 1.5501]$, with $67.2\ \%$ of
replicates at least as dispersed. There is no evidence of over-dispersion or
under-dispersion at this sample size, so the Poisson assumption is **not
contradicted** for that feature.

**Not established.** Three things at least:

1. That the model is **right** — a passing check is the absence of a
   contradiction, not a confirmation.
2. That **other** features are reproduced — the check examined the dispersion and
   the mean only, and a model can match both while failing, for example, on the
   autocorrelation of the counts or on the tail.
3. That the model **extrapolates** — the check is confined to the range of the
   observed data, and a larger exposure or a different regime is untested.

---

## ★★★7 — Power of a posterior predictive check

**Data-generating process.** Counts generated as
$y_i \sim \mathrm{Poisson}(\lambda_i)$ with
$\lambda_i \sim \mathrm{Gamma}(\phi, \phi/\mu)$; then $\operatorname{Var}(y)/\mu
= 1 + \mu/\phi$, so the over-dispersion is controlled by the single parameter
$\phi$. Sweep $\mu/\phi \in \{0, 0.1, 0.25, 0.5, 1, 2\}$ from Poisson
($\phi \to \infty$) to strongly over-dispersed.

**Model fitted.** A Poisson with a $\mathrm{Gamma}(2,1)$ prior on the rate.

**Check statistic.** The dispersion index $\operatorname{Var}(y)/\operatorname{mean}(y)$,
the same statistic the demonstration used, pre-specified.

**Replicates.** $M = 2000$ synthetic data sets per over-dispersion level, each of
$n = 100$ observations, with $S = 500$ predictive draws each. The estimated
detection rate has a standard error below $1.2\ \%$ at $M = 2000$.

**Prediction.** At $\phi = \infty$ (genuinely Poisson) the detection rate is the
nominal $5\ \%$ — the check is calibrated. It rises with over-dispersion: about
$20\ \%$ at a ratio of $1.1$, $60\ \%$ at $1.25$, and above $99\ \%$ at $1.5$ and
beyond. With $n = 100$ the check is therefore a sensitive instrument for moderate
over-dispersion, and the headline is the curve of detection rate against
$\mu/\phi$ — the power of the check, which is what determines whether a passing
result is informative or merely uninformative.

---

## ★★★8 — Workflow reproducibility across analysts

**What varies.** Hold the data and the seven-stage protocol fixed, and vary the
genuinely discretionary choices:

1. the prior family and its parameters (e.g. $\mathrm{Gamma}(2,1)$ versus
   $\mathrm{Gamma}(0.5, 0.5)$ versus a lognormal);
2. the predictive-check statistic, chosen independently by each analyst;
3. the decision rule for declaring a model comparison decisive (a threshold on
   $z$, and whether parsimony breaks ties);
4. the MCMC burn-in fraction and the $\hat R$ threshold adopted.

**Metric.** The pairwise difference in the reported posterior mean and in the
width of the reported $95\ \%$ credible interval, expressed in posterior standard
deviations; and the rate at which two analysts **disagree about the conclusion**
(for example, whether a trend is non-zero).

**Replicates.** $M = 200$ analysts $\times$ 200 data sets, drawn by sampling the
discretionary choices from a plausible distribution and re-running the analysis.
The resulting distribution of conclusions is the quantity of interest — a
"multiverse" analysis.

**Prediction.** Posterior **means** are robust: the prior-equivalent sample size
makes the mean shift by well under one posterior standard deviation across
reasonable priors, as the module's demonstrations show. Posterior **interval
widths** and the **conclusion** are much more sensitive: with a prior-equivalent
size comparable to $n$, the interval width varies by tens of per cent and the
disagreement rate on a marginal conclusion can exceed $20\ \%$. The headline is
the asymmetry — report the mean, and report the sensitivity of the interval and
the decision.
