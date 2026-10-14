---
id: 16-06-02
title: "Model-Data Comparison in Palaeoclimate"
level: research
prereqs: ["16-06-01", "16-05-01", "18-05-01"]
tags: [atmosphere, climate, palaeoclimate, model-data-comparison, data-assimilation, calibration]
---

# Model-Data Comparison in Palaeoclimate

> All models and data in this module are **SYNTHETIC**. Every number below was
> printed by
> [`code/paleoclimate_model_data_demo.py`](code/paleoclimate_model_data_demo.py).
> The climate field, the proxies and the model prior are generated; no published
> reconstruction, calibration or proxy record is quoted.

## Learning objectives

By the end of this lesson you will be able to:

1. **Write down** a proxy system model linking a climate state to a measurable
   proxy, including an unmodelled local factor.
2. **Distinguish** calibration error, proxy noise and unmodelled factor, and
   **state** which of them produces bias rather than scatter.
3. **Derive** the scalar optimal-interpolation (Kalman-style) update and its
   variance reduction, and **interpret** the gain as a signal-to-noise ratio.
4. **Demonstrate** that the update reduces random error but cannot remove a
   proxy's systematic bias.
5. **Explain** why transporting a calibration to a different mean state
   introduces a bias, and **quantify** it in a synthetic example.
6. **State** where a reconstruction's uncertainty estimate comes from and what it
   omits.
7. **Design** a model-data comparison that separates calibration error from
   structural model error.

## Prerequisites

- [16-06-01 Palaeoclimate Proxies: Ice Cores, Sediments, Isotopes](01-paleoclimate-proxies.md) —
  where the proxy values and their calibrations come from.
- [16-05-01 Model Hierarchy: EBMs, EMICs, GCMs, ESMs](../05-climate-models/01-climate-model-hierarchy.md) —
  the model side of the comparison.
- [18-05-01 Bayesian Inverse Formulation](../../18-inverse-problems/05-bayesian-inversion/01-bayes-inverse-formulation.md) —
  the prior/likelihood/posterior structure used here in its simplest scalar form.

## 1. Intuition: two error models, one reconstruction

A palaeoclimate reconstruction combines two things: a model (or a prior) that
says something about the climate of the past, and proxy data that say something
else. Both are uncertain, and the uncertainties are of different kinds.

- The **prior** carries a *bias* if the model's mean state is wrong, and a
  *spread* if it represents internal variability.
- The **proxy** carries *noise*, which averages down at a single site over many
  samples, and a *systematic* component — the calibration, the seasonal
  weighting, the local environmental factor — which does not.

A data-assimilation or optimal-interpolation update is a weighted average of the
two. It is very good at reducing the random parts. It is structurally incapable
of detecting a bias in either input, because it assumes both are unbiased. That
one sentence is the content of this lesson; the rest is arithmetic.

## 2. Definitions

- **Proxy system model.** The forward map from climate state to proxy value,
  including any local environmental variables that affect the proxy but are not
  the climate variable of interest.
- **Calibration.** The fitted parameters of that map.
- **Unmodelled factor.** A variable in the proxy system model that the
  calibration ignores. It contributes an error that is correlated over time or
  space, so it does not average away.
- **Prior.** The model's estimate of the climate state, with its uncertainty.
- **Optimal interpolation / data assimilation.** An update that combines prior
  and observations using their stated uncertainties.
- **Gain.** The weight given to the observation, equal to
  $\sigma_{\text{prior}}^{2}/(\sigma_{\text{prior}}^{2}+\sigma_{\text{obs}}^{2})$
  in the scalar case.
- **Modern analogue.** A site or period with both proxy and instrumental data,
  used to fit the calibration.

## 3. Derivation: the scalar optimal-interpolation update

### 3.1 Setup

Let the true state at a location be $x$, estimate ahead of time the prior with
mean $\mu_p$ and variance $\sigma_p^{2}$, and let an observation $y$ satisfy

$$y = x + \varepsilon,\qquad \varepsilon\sim\mathcal{N}(0,\sigma_o^{2}),$$

with the prior and the observation error independent and both unbiased. The
posterior is Gaussian and, writing
$G = \sigma_p^{2}/(\sigma_p^{2}+\sigma_o^{2})$,

$$\boxed{\;\mu_{\text{post}} = \mu_p + G\,(y-\mu_p),
\qquad
\sigma_{\text{post}}^{2} = (1-G)\,\sigma_p^{2}.\;}$$

### 3.2 Reading the gain

- If $\sigma_o \ll \sigma_p$, then $G\to1$: the observation wins.
- If $\sigma_o \gg \sigma_p$, then $G\to0$: the prior wins.
- At $\sigma_o = \sigma_p$, the balanced case, $G = 1/2$ and
  $\sigma_{\text{post}}^{2} = \sigma_p^{2}/2$.

The demonstration computes the three cases
$(\sigma_p,\sigma_o) = (2,1)$, $(2,2)$ and $(2,4)$:

| prior sd (K) | observation sd (K) | gain | posterior sd (K) |
|---|---|---|---|
| 2.0 | 1.0 | 0.8000 | 0.8944 |
| 2.0 | 2.0 | 0.5000 | 1.4142 |
| 2.0 | 4.0 | 0.2000 | 1.7889 |

Note the asymmetry: a good observation (gain $0.8$) reduces the standard
deviation from $2.00$ to $0.89$ — a $55\%$ reduction. A poor one (gain $0.2$)
reduces it only from $2.00$ to $1.79$. Better data help disproportionately,
which is why network design is worth doing.

### 3.3 Where there is no data

Away from any observation the update has no term to apply: the posterior equals
the prior, and the posterior variance is the prior variance. In a spatially
complete reconstruction the error therefore grows with distance from data, and
the map shows the prior's structure where it is unconstrained. That is
information about the *model*, not about the past.

### 3.4 From one number to a field

The scalar result generalises directly. With state vector $\mathbf{x}$, prior
covariance $\mathbf{B}$, linear observation operator $\mathbf{H}$ and observation
error covariance $\mathbf{R}$,

$$\mathbf{x}_a = \mathbf{x}_b + \mathbf{K}\left(\mathbf{y}-H\mathbf{x}_b\right),
\qquad
\mathbf{K} = \mathbf{B}H^{\mathsf T}\left(H\mathbf{B}H^{\mathsf T}
+\mathbf{R}\right)^{-1},$$

$$\mathbf{P}_a = (\mathbf{I}-\mathbf{K}H)\mathbf{B}.$$

Every scalar remark survives the generalisation. The gain is still a
signal-to-noise ratio, now a matrix; variance is still reduced by the amount the
data constrain; and bias is still invisible, because it enters through the means
$\mathbf{x}_b$ and $\mathbf{y}$ and the formula contains only covariances. An
off-diagonal element of $\mathbf{B}$ or $\mathbf{R}$ (spatial correlation of
either prior error or proxy error) changes $\mathbf{K}$, so the assumption of
independent errors is not innocuous: correlated proxy errors across nearby sites
reduce the effective information and are the commonest reason a reconstruction is
more confident than it is accurate.

## 4. Measurement: what an unmodelled factor does

The demonstration builds a synthetic field on $40$ sites $\times$ $60$ time
steps with a spatial pattern, a temporal signal and a local environmental factor
that varies in space but not in time. The proxy is

$$P = 1.4\,T + 0.8\,\cos\text{-pattern} + \mathcal{N}(0,0.5^{2}),$$

while the analyst calibrates with the correct slope $1.4$ and ignores the
$\cos$-pattern. Reconstruction errors:

| case | RMSE (K) | bias (K) |
|---|---|---|
| modern period, ignored local factor | 0.534 | $+0.065$ |
| palaeo period, same relationship | 0.540 | $+0.071$ |
| palaeo period, calibration slope wrong by $40\%$ | 0.963 | $+0.299$ |
| palaeo period, true proxy sensitivity changed to $1.9$ | 0.755 | $+0.244$ |

The ignored local factor produces a small mean bias ($+0.065\ \mathrm{K}$)
because its spatial average happens to be near zero, and otherwise appears as
scatter ($\mathrm{RMSE} = 0.534\ \mathrm{K}$ against an injected noise of
$0.5\ \mathrm{K}$). A wrong slope and a changed sensitivity produce both larger
RMSE and larger bias: $+0.299\ \mathrm{K}$ and $+0.244\ \mathrm{K}$.

The general rule is worth stating: **a bias appears whenever the calibration
assumption fails in a way that is not averaged out.** An unmodelled factor that
is symmetric in space contributes scatter; one that is asymmetric, or that
correlates with the climate variable, contributes bias. Distinguishing the two
requires an independent check, which is exactly what a model-data comparison is
for.

## 5. Measurement: a biased proxy keeps a small apparent variance

Now run the scalar update with a deliberately biased observation. The prior is
the truth minus $0.5\ \mathrm{K}$ plus $2.0\ \mathrm{K}$ noise; the observation
is the biased reconstruction from above, with an actual error of
$0.5399\ \mathrm{K}$:

| quantity | value |
|---|---|
| prior RMSE | $2.0507\ \mathrm{K}$ |
| observation RMSE | $0.5399\ \mathrm{K}$ |
| gain | $0.9321$ |
| posterior RMSE | $0.5170\ \mathrm{K}$ |
| posterior variance | $0.2716\ \mathrm{K^{2}}$ (sd $0.5212\ \mathrm{K}$) |

The update improves the estimate — RMSE falls from $2.0507$ to $0.5170\
\mathrm{K}$ — and it does so by trusting the observation almost completely
($G = 0.9321$). The posterior standard deviation, $0.5212\ \mathrm{K}$, is
small. It is also **wrong as a total uncertainty**: the reconstruction still
carries the proxy's own bias, which the update never sees because both terms of
the gain formula assume unbiased inputs.

This is the mechanism behind a confident, biased reconstruction. Nothing in the
arithmetic is at fault; the fault is a modelling assumption that is not stated
in the uncertainty. The remedy is a *model-data comparison*: evaluate the
reconstruction against independent information, and report the residual bias
alongside the posterior spread.

## 6. Worked example: how much does a biased proxy cost?

*Problem.* Using the numbers above, suppose an analyst quotes the posterior
standard deviation, $0.5212\ \mathrm{K}$, as the uncertainty of the
reconstruction. What is the correct order of magnitude of the total error, and
what dominates it?

*Solution.*

1. The posterior spread is $\sigma_{\text{post}} = 0.5212\ \mathrm{K}$.
2. The measured posterior RMSE against the truth is $0.5170\ \mathrm{K}$. In
   this case the two nearly coincide, because the remaining error is dominated by
   scatter rather than a large bias.
3. But the observation's *systematic* component, measured as the RMSE of the
   observation against the truth ($0.5399\ \mathrm{K}$, of which part is bias),
   is not represented in $\sigma_{\text{post}}$ at all.
4. Compare with the calibration-transport case: there the bias alone was
   $+0.794\ \mathrm{K}$ in the demonstration's changed-regime experiment
   ([16-05-04 Downscaling](../05-climate-models/04-downscaling.md) makes the
   same point in a different setting), which is larger than the posterior
   standard deviation quoted above.

*Interpretation.* The stated uncertainty is a measure of *how much the available
data constrain the prior*, and the answer to a different question from *how
close the answer is to the truth*. A reconstruction must report both, and the
second can only be estimated against independent evidence.

## 7. Assumptions and regime of validity

1. **Both inputs are unbiased.** The gain formula is derived under that
   assumption. If either the prior or the observation has a bias, the posterior
   inherits a bias and the posterior variance does not reflect it (Section 5).
2. **Gaussian errors.** The update is optimal for Gaussian errors; for other
   error distributions it is a reasonable linear estimator but no longer
   optimal.
3. **Independence of errors.** Prior error and observation error are assumed
   independent. Proxy errors at nearby sites are often correlated by a shared
   local factor, which the scalar update ignores.
4. **Known error statistics.** $\sigma_o$ must be estimated from the calibration,
   and the estimate is itself uncertain; understating $\sigma_o$ increases the
   gain and makes the reconstruction overconfident.
5. **Spatially complete truth.** The example is a synthetic field whose statistics
   are known. In a real reconstruction the "truth" is exactly what is unknown, so
   validation must be done by withholding data (cross-validation) or by using an
   independent period.
6. **Age models.** Every comparison folds in dating uncertainty, which is a
   separate, often dominant, error term.

## 8. Units and dimensional analysis

| quantity | symbol | unit | check |
|---|---|---|---|
| climate state | $x$ | K | |
| proxy value | $P$ | proxy units | $a + bT$ |
| sensitivity | $b$ | proxy units per K | |
| prior/observation variance | $\sigma^{2}$ | $\mathrm{K^{2}}$ | |
| gain | $G$ | 1 | ratio of variances |
| posterior variance | | $\mathrm{K^{2}}$ | $(1-G)\sigma_p^{2}$ |

The gain is dimensionless because it is a ratio of variances. A computed gain
outside $[0,1]$ indicates that one variance is negative (an estimation error) or
that the variances were mismatched in units — for example a proxy variance in
proxy units divided by a prior variance in kelvin.

## 9. Python demonstration

[`code/paleoclimate_model_data_demo.py`](code/paleoclimate_model_data_demo.py):

1. builds a synthetic climate field, a proxy system model with an unmodelled
   local factor, and a calibration period;
2. reconstructs in the modern and a shifted palaeo period, and shows the bias
   produced by a wrong slope and by a changed proxy sensitivity;
3. computes the three scalar optimal-interpolation cases and their variance
   reductions;
4. applies the update with a biased proxy and compares posterior spread with
   actual error.

It is print-only, seeded with `np.random.default_rng(20261014)`, and exits 0.

## 10. Exercises

See [`exercises/02-paleoclimate-model-data-exercises.md`](exercises/02-paleoclimate-model-data-exercises.md)
and [`exercises/02-paleoclimate-model-data-solutions.md`](exercises/02-paleoclimate-model-data-solutions.md).

## Mastery checkpoint

> **(a)** Derive the scalar update from the product of two Gaussian densities and
> confirm that $G = \sigma_p^{2}/(\sigma_p^{2}+\sigma_o^{2})$.
> **(b)** With $\sigma_p = 3.0\ \mathrm{K}$ and $\sigma_o = 1.5\ \mathrm{K}$,
> compute the gain, the posterior mean given $\mu_p = 280.0\ \mathrm{K}$ and
> $y = 284.0\ \mathrm{K}$, and the posterior standard deviation.
> **(c)** The observation used in (b) is in fact biased by $+1.0\ \mathrm{K}$.
> Recompute the posterior mean and state by how much it is wrong.
> **(d)** Explain why a reconstruction that reports only its posterior spread can
> be simultaneously well-calibrated and far from the truth.

## Common pitfalls

1. **Treating the posterior spread as the total error.** It excludes bias in
   either input.
2. **Ignoring an unmodelled local factor.** Symmetric in space it appears as
   scatter; correlated with climate it appears as bias.
3. **Understating the proxy error to sharpen the reconstruction.** A smaller
   $\sigma_o$ raises the gain and makes the answer more confident, not more
   correct.
4. **Comparing model and proxy at different timescales.** A seasonal proxy
   against an annual-mean model output is a bias waiting to be discovered.
5. **Assuming error independence across sites.** Shared local factors make the
   errors correlated, which reduces the information in a network.
6. **Forgetting the age model.** Dating uncertainty is frequently the largest
   single term.

## Related modules

- [16-06 Palaeoclimate](README.md).
- [16-06-01 Palaeoclimate Proxies: Ice Cores, Sediments, Isotopes](01-paleoclimate-proxies.md) —
  the forward models inverted here.
- [16-05-03 Model Evaluation, Skill and Benchmarking](../05-climate-models/03-model-evaluation.md) —
  the metrics used to score a reconstruction.
- [18-05 Bayesian Inversion and Inference](../../18-inverse-problems/05-bayesian-inversion/README.md) —
  the general treatment, of which Section 3 is the scalar case.
- [21-02 Geostatistics](../../21-statistics-bayesian-ml/02-geostatistics/README.md) —
  spatial correlation and the network-design question.
