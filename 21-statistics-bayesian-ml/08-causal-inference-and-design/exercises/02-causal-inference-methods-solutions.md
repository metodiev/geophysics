# Solutions — 21-08-02 Causal Inference Methods and Counterfactuals

> Read after attempting. Lesson:
> [02 Causal Inference](../02-causal-inference-methods.md). Numbers are
> **SYNTHETIC**, printed by
> [`code/causal_inference_methods_demo.py`](../code/causal_inference_methods_demo.py).

---

## ★1 — Decomposing the difference in means

By consistency, the observed outcome is the potential outcome for the treatment
received, so $\mathbb E[Y\mid D=1] = \mathbb E[Y(1)\mid D=1]$ and
$\mathbb E[Y\mid D=0] = \mathbb E[Y(0)\mid D=0]$. Add and subtract
$\mathbb E[Y(0)\mid D=1]$:

$$\mathbb E[Y\mid D=1] - \mathbb E[Y\mid D=0]
= \underbrace{\mathbb E[Y(1) - Y(0)\mid D=1]}_{\text{effect on the treated}}
+ \underbrace{\mathbb E[Y(0)\mid D=1] - \mathbb E[Y(0)\mid D=0]}_{\text{selection bias}} .$$

The second term compares the *untreated* potential outcomes of two groups that
were not assigned at random. Equivalently, adding and subtracting
$\mathbb E[Y(1)\mid D=0]$ and $\mathbb E[Y(0)\mid D=1]$ decomposes the difference
into the ATE plus the difference of the two selection terms,

$$\mathbb E[Y\mid D=1] - \mathbb E[Y\mid D=0] = \mathrm{ATE}
+ \left[\mathbb E[Y(0)\mid D=1] - \mathbb E[Y(0)\mid D=0]\right]
- \left[\mathbb E[Y(1)\mid D=1] - \mathbb E[Y(1)\mid D=0]\right],$$

which vanishes exactly when the treated and untreated groups are exchangeable in
*both* potential outcomes. Exchangeability is therefore not one assumption about
the groups' comparability but a statement about both counterfactual arms, and it is
what randomisation provides by construction.

---

## ★2 — Predicting the unadjusted bias

With $Y = \beta D + \gamma_Z Z + \varepsilon$ and $D$ correlated with $Z$, the
omitted-variable form of the selection bias is

$$\text{bias} = \gamma_Z\left(\mathbb E[Z\mid D=1] - \mathbb E[Z\mid D=0]\right)
= 1.0 \times 1.112 = +1.112 .$$

The measured bias is $+1.179$, which is $0.067$ above the prediction — $0.6$ of the
$\pm0.109$ standard error of the unadjusted estimate. The two are the same number
to within sampling error, and the arithmetic makes the point that **the
unadjusted estimate's error is not noise: it is a computable function of the
confounding imbalance.** That is what makes the bias diagnosable rather than
merely regrettable.

---

## ★3 — Biases of the four estimators

| Estimator | Estimate | Bias | Bias as % of the ATE |
|---|---|---|---|
| unadjusted | $+3.179$ | $+1.179$ | $59.0\%$ |
| regression on $D$, $Z$ | $+2.116$ | $+0.116$ | $5.8\%$ |
| inverse-probability weighting | $+2.241$ | $+0.241$ | $12.1\%$ |
| propensity stratification | $+2.231$ | $+0.231$ | $11.6\%$ |

**Most precise:** regression, with a half-width of $\pm0.103$ against $\pm0.150$
for IPW. **Least biased:** regression again ($+0.116$). That the same estimator
wins both columns is a property of this generator — a linear outcome model with a
Gaussian confounder is exactly regression's home ground. With a nonlinear outcome
model or a poorly specified propensity model, the ranking would change, which is
why a study must report the diagnostics of *its* estimator rather than relying on a
general preference.

---

## ★★4 — The omitted-variable formula and the conditional imbalance

**Formula.** If the true model is
$Y = \beta D + \gamma_Z Z + \gamma_U U + \varepsilon$ and the estimated model omits
$U$, then the bias of $\hat\beta$ is

$$\text{bias} = \gamma_U\,\hat\beta_{U\cdot D\mid Z},$$

where $\hat\beta_{U\cdot D\mid Z}$ is the coefficient on $D$ in the regression of
$U$ on $(D, Z)$ — equivalently, the partial correlation of $U$ with $D$ after
partialling out $Z$ (Frisch–Waugh–Lovell).

**Prediction here.** $\gamma_U = 0.8$ and
$\hat\beta_{U\cdot D\mid Z} = +1.605$, so

$$\text{bias} = 0.8 \times 1.605 = +1.284 ,$$

against the measured $+1.233$: a difference of $0.051$, well inside the
$\pm0.124$ interval.

**Why conditional rather than marginal.** The marginal imbalance
$\mathbb E[U\mid D=1] - \mathbb E[U\mid D=0] = +1.083$ is what an *unadjusted*
comparison would see, but the regression conditions on $Z$, and conditioning
changes how much of $D$'s variation is attributable to $U$. Because
$D = \mathbf 1\{Z+U>0\}$, holding $Z$ fixed leaves $U$ as the only remaining source
of variation in $D$, so the residual association between $U$ and $D$ is
*stronger* than the marginal one: $1.605 > 1.083$.

The consequence is counter-intuitive and worth memorising: **adjusting for a
measured confounder can increase the bias from an unmeasured one** when the two are
associated. The direction must be reasoned about in each study; it cannot be assumed
that "more adjustment is safer".

---

## ★★5 — Balance diagnostics for a weighting or matching study

**Statistic.** For every covariate $X_k$, the **standardised mean difference**
between the treatment arms, before and after weighting or matching:

$$\mathrm{SMD}_k = \frac{\bar X_{k,\text{treated}} - \bar X_{k,\text{control}}}
{\sqrt{\left(s_{k,\text{treated}}^2 + s_{k,\text{control}}^2\right)/2}} .$$

Report the **absolute** value, since the sign is uninformative. Add the variance
ratio $s^2_{\text{treat}}/s^2_{\text{control}}$, which detects a difference in
dispersion that the mean difference misses, and the propensity-score distributions
of the two arms (overlap and the tails where weights explode).

**Threshold.** The conventional rule is $\lvert\mathrm{SMD}\rvert < 0.1$ after
adjustment, with the *before* column printed beside it so the reader sees what the
adjustment accomplished. The threshold is a convention, not a test; a covariate
with $\mathrm{SMD} = 0.15$ that has a large outcome coefficient can matter more
than one at $0.05$ with a small coefficient, so report both columns and the
outcome model.

**What an imbalance implies.** Residual confounding in the direction of the
covariate's outcome coefficient, of magnitude approximately
$\gamma_k \times \mathrm{SMD}_k \times s_k$. That is the same arithmetic as ★★4:
an imbalance is a bias, and its size is computable from the outcome model. An
unbalanced covariate therefore belongs in the sensitivity analysis, not only in an
appendix table.

---

## ★★6 — Weights, variance and the effective sample size

The treated units carry weights $1/e(Z)$; the effective sample size of a weighted
estimator is

$$n_{\text{eff}} = \frac{\left(\sum_i w_i\right)^2}{\sum_i w_i^2} ,$$

so the variance of a weighted mean is inflated by $n/n_{\text{eff}}$ relative to an
unweighted one.

**Propensity uniform on $[0.02, 0.98]$.** With $w = 1/e$,

$$\mathbb E[w] = \frac{1}{0.96}\ln\frac{0.98}{0.02} = \frac{3.892}{0.96} = 4.054,
\qquad
\mathbb E[w^2] = \frac{1}{0.96}\left(\frac{1}{0.02} - \frac{1}{0.98}\right)
= \frac{49.98}{0.96} = 52.06 ,$$

$$\frac{n_{\text{eff}}}{n} = \frac{\mathbb E[w]^2}{\mathbb E[w^2]}
= \frac{16.44}{52.06} = 0.316 .$$

So IPW uses about **32% of the sample**, and its standard error is inflated by
$1/\sqrt{0.316} = 1.78$ relative to an unweighted estimator. The demonstration's
numbers show exactly this: IPW's half-width is $0.150$ against the regression's
$0.103$, a ratio of $1.46$ — the right order, with the difference explained by the
continuous $Z$ doing more work in the regression than the weights do.

**If the minimum propensity fell to $0.001$.** Then
$\mathbb E[w^2] \approx 1000$ while $\mathbb E[w] \approx 6.92$, so
$n_{\text{eff}}/n = 47.9/1000 = 0.048$: about **5% of the sample**, a standard
error inflated by $4.6$. A single near-deterministic propensity value therefore
destroys the estimator — which is why overlap is reported, why trimming or
overlap-weighted estimands exist, and why "the propensity model converged" is not a
diagnostic.

---

## ★★★7 — A sensitivity analysis for unmeasured confounding

**Family.** A single unmeasured confounder $U$ (standardised, without loss of
generality) entering (i) the outcome with coefficient $\gamma$ and (ii) the
treatment with a partial association $\delta$ — the coefficient of $U$ in a model
for $D$ given the measured covariates. Both are stated in units comparable to the
measured covariates so a reader can judge plausibility. The bias is approximately
$\gamma\,\delta$ (the same form as ★★4).

**Metric.** The adjusted estimate as a function of $(\gamma, \delta)$:
$\hat\beta(\gamma,\delta) = \hat\beta_{\text{obs}} - \gamma\delta$.

**Output.** Three things, in this order:

1. **The bias factor / E-value:** the smallest $\gamma = \delta = t$ (in standardised
   units) that would reduce the effect to zero. Solving
   $t^2 = \hat\beta_{\text{obs}}$ gives $t = \sqrt{\hat\beta_{\text{obs}}}$; for the
   demonstration's biased estimate of $3.233$ with a claimed effect of $2.116$ that
   is $t = \sqrt{1.233} = 1.11$ standardised units — a surprisingly modest
   confounder.
2. **A reference point in the same units:** the strongest *measured* covariate's
   normalised association with the outcome and with the treatment. A reader can then
   ask whether an unmeasured confounder stronger than every measured one is
   plausible, which is a scientific question rather than a statistical one.
3. **The contour**, not a single number: report $\hat\beta$ for a grid of
   $(\gamma,\delta)$ and mark the region where the effect changes sign or falls
   below the smallest effect of interest.

**Calibration to the problem.** State the units explicitly: "a $1\sigma$ shift in the
unmeasured variable raises the outcome by $\gamma$ events per year and raises the
probability of treatment by $\delta$". A sensitivity analysis reported only in
dimensionless multipliers cannot be argued with, and therefore cannot be used.

---

## ★★★8 — A study where interference is the phenomenon

**Estimand.** The effect of an **allocation**, not of an individual's treatment:
$\mathbb E[Y(\mathbf d)]$ for a treatment vector $\mathbf d$ over wells in a shared
aquifer, and the contrast between the observed allocation and a specified
counterfactual allocation (for example, the same total injected volume spread over
fewer wells). Writing the estimand at the allocation level is the substantive
change: the individual-level ATE of
[02 Causal Inference](../02-causal-inference-methods.md) is not identified when one
unit's treatment changes another's outcome.

**Design.** Cluster randomisation, with the cluster being the unit over which
interference operates — an aquifer, a pressure compartment, a district. Options:

- **cluster-randomised allocation**: randomise the injection schedule across
  compartments, with all wells inside a compartment receiving the same allocation;
- **stepped-wedge**: compartments switch from the control to the treatment
  allocation at randomly assigned times, which also gives within-compartment
  temporal variation and is easier to justify ethically when monitoring is
  beneficial;
- **a spatial exposure design**: keep the assignment fixed but specify and measure
  an exposure model (distance-weighted injection volume) whose coefficients become
  the estimand.

**Estimator.** With cluster randomisation, the estimand is estimated at the cluster
level — a cluster-level difference, a difference-in-differences across clusters, or
a hierarchical model with cluster random effects — and the inference must respect
the number of *clusters*, not the number of wells. With a spatial exposure design,
fit an exposure-response model whose interference structure is pre-specified (for
example an exponential kernel in distance) and report the kernel's scale with its
uncertainty.

**Why unit-level randomisation fails.** If well A is treated and its neighbour B is
not, B experiences A's treatment through pressure diffusion, so the "control" arm is
contaminated and the contrast no longer measures the effect of an allocation —
it measures the effect of a partial allocation, which is a different (and usually
smaller) quantity. Worse, the contamination is *directional and physical*: it grows
with proximity and with time, so it cannot be treated as random noise, and no
covariate adjustment restores the contrast. The remedy is to randomise at the level
at which the interference is contained (or to model it explicitly), never to
pretend it is absent.

---

## ★★★9 — "No effect" versus "undetectable"

**Sequence.**

1. **Pre-specify the smallest effect of interest (SESOI).** From the physics or the
   decision rule, not from the data: the injection rate at which a regulatory
   threshold is crossed, the deformation a structure tolerates, the seismic rate at
   which a traffic light must change colour.
2. **Compute the minimum detectable effect (MDE)** of the design:
   $\mathrm{MDE} = (z_{1-\alpha/2} + z_{1-\beta})\,\operatorname{se}(\hat\beta)$,
   with $\operatorname{se}$ from the actual sampling geometry
   ([21-08-01](./01-experimental-design-solutions.md)) and an effective sample size
   that accounts for clustering and temporal correlation.
3. **Compare them.** If $\mathrm{MDE} < \mathrm{SESOI}$, a null result is
   informative: the data bound the effect below the threshold of interest. If
   $\mathrm{MDE} > \mathrm{SESOI}$, the study is **inconclusive**, and the honest
   statement is a bound ("the data are consistent with effects up to $X$"), never
   "the treatment has no effect".
4. **Test equivalence if that is the claim.** A two-one-sided-test (TOST) against
   $\pm\mathrm{SESOI}$ converts the bound into a formal equivalence claim with a
   stated level.
5. **Re-do the MDE under identification assumptions.** Admit a bias term of the size
   the sensitivity analysis of ★★★7 allows: every $\operatorname{se}$ above is a
   *statistical* uncertainty, and a confounding bias of $\gamma\delta$ shifts the
   estimate without widening any interval. If the admissible bias exceeds the SESOI
   — as in the demonstration, where a plausible confounder moves the estimate by
   $1.233$ against an interval of $\pm0.124$ — then the study cannot distinguish the
   hypotheses regardless of how much data are collected. Reporting the interval
   alone in that situation misrepresents what is known.

**Reported output.** SESOI and its source; MDE and the design quantities that set
it; the estimate with its interval; the bound implied if the effect is
indistinguishable from zero; and the sensitivity of the bound to the identification
assumptions, quoting the strongest measured covariate as a benchmark. A study that
reports only the estimate and its interval has answered a question nobody asked.
