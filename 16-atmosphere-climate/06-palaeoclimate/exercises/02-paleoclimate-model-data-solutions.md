# Solutions — 16-06-02 Model-Data Comparison in Palaeoclimate

> Read after attempting the exercises. Lesson:
> [02 Model-Data Comparison in Palaeoclimate](../02-paleoclimate-model-data.md).

---

## ★1 — Deriving the scalar update

The posterior density is proportional to the product

$$p(x\mid y) \propto \exp\!\left[-\frac{(x-\mu_p)^{2}}{2\sigma_p^{2}
} - \frac{(y-x)^{2}}{2\sigma_o^{2}}\right].$$

Collect the terms quadratic and linear in $x$:

$$-\frac12\left[x^{2}\left(\frac{1}{\sigma_p^{2}}+\frac{1}{\sigma_o^{2}}\right)
- 2x\left(\frac{\mu_p}{\sigma_p^{2}}+\frac{y}{\sigma_o^{2}}\right)\right] + \text{const}.$$

For a Gaussian, the coefficient of $x^{2}/2$ is $1/\sigma_{\text{post}}^{2}$, so

$$\frac{1}{\sigma_{\text{post}}^{2}} = \frac{1}{\sigma_p^{2}}+\frac{1}{\sigma_o^{2}}
\quad\Longrightarrow\quad
\sigma_{\text{post}}^{2} = \frac{\sigma_p^{2}\sigma_o^{2}}{\sigma_p^{2}+\sigma_o^{2}}
= (1-G)\sigma_p^{2},$$

with $G = \sigma_p^{2}/(\sigma_p^{2}+\sigma_o^{2}) \in [0,1]$. The mean is

$$\mu_{\text{post}} = \sigma_{\text{post}}^{2}\left(\frac{\mu_p}{\sigma_p^{2}}
+\frac{y}{\sigma_o^{2}}\right)
= \mu_p + G\,(y-\mu_p).$$

Precision (inverse variance) adds; variance does not.

---

## ★2 — Balanced update

$$G = \frac{2.5^{2}}{2.5^{2}+1.0^{2}} = \frac{6.25}{7.25} = 0.8621.$$

$$\mu_{\text{post}} = 282.0 + 0.8621\,(286.0-282.0) = 282.0 + 3.4483
= 285.45\ \mathrm{K}.$$

$$\sigma_{\text{post}} = \sqrt{(1-0.8621) \times 6.25} = \sqrt{0.1379 \times 6.25}
= \sqrt{0.8621} = 0.9285\ \mathrm{K}.$$

The observation (standard deviation $1.0\ \mathrm{K}$) is more informative than
the prior ($2.5\ \mathrm{K}$), so the posterior sits $86\%$ of the way to the
observation and its variance is $13.8\%$ of the prior's.

---

## ★3 — Posterior error from a biased observation

With $\mu_p$ unbiased, the posterior mean is displaced by

$$\Delta = G \times \text{bias} = 0.8621 \times 1.0 = 0.862\ \mathrm{K}.$$

$$\mu_{\text{post}}^{\text{true}} = 282.0 + 0.8621\,(285.0-282.0)
= 284.586\ \mathrm{K}.$$

The report would be $285.45\ \mathrm{K}$, i.e. $0.862\ \mathrm{K}$ too warm,
while the posterior standard deviation ($0.9285\ \mathrm{K}$) is unchanged. A
bias in one input produces a bias in the output of the same sign, weighted by the
gain, and it leaves no signature in the spread.

---

## ★4 — Verifying the gain

The gain formula uses variances:

$$G = \frac{\sigma_p^{2}}{\sigma_p^{2}+\sigma_{\text{obs}}^{2}}.$$

With $\sigma_p = 2.0\ \mathrm{K}$ (variance $4.0\ \mathrm{K^{2}}$) and
$\sigma_{\text{obs}} = 0.5399\ \mathrm{K}$ (variance $0.2915\ \mathrm{K^{2}}$):

$$G = \frac{4.0}{4.0+0.2915} = \frac{4.0}{4.2915} = 0.9321.$$

The demonstration's value is reproduced: the observation's "standard deviation"
is being taken to be its **measured RMSE**, i.e. the total scatter of the
reconstruction against the truth, not the injected measurement noise alone. That
is a modelling choice worth stating, because it folds the calibration error into
what the update treats as random observational error.

---

## ★5 — Understating the observation error

**Assumed gain.** With assumed observation variance $0.25\ \mathrm{K^{2}}$:

$$G_{\text{assumed}} = \frac{4.0}{4.25} = 0.9412,
\qquad
\sigma_{\text{reported}}^{2} = (1-0.9412)\times4.0 = 0.2352\ \mathrm{K^{2}}.$$

**Actual error variance.** The estimator is
$\hat x = \mu_p + G(y-\mu_p)$, so with prior error $e_p$ and observation error
$e_o$ the error is $(1-G)e_p + Ge_o$. With independent errors of variances
$4.0$ and $1.0\ \mathrm{K^{2}}$:

$$\mathrm{Var}(\hat x) = (1-G)^{2}(4.0) + G^{2}(1.0)
= (0.0588)^{2}(4.0) + (0.9412)^{2}(1.0)
= 0.0138 + 0.8859 = 0.8997\ \mathrm{K^{2}}.$$

The actual RMSE is $0.9485\ \mathrm{K}$, against a reported standard deviation of
$0.485\ \mathrm{K}$.

**Optimal.** With the correct variance, $G = 4/5 = 0.8$ and

$$\mathrm{Var} = (0.2)^{2}(4.0) + (0.8)^{2}(1.0) = 0.16+0.64
= 0.80\ \mathrm{K^{2}},\qquad \text{RMSE} = 0.8944\ \mathrm{K}.$$

**Ratios.** The reported variance is $0.2352$ against an actual $0.8997$: it
understates the error variance by a factor of $3.8$ (standard deviation by
$1.96$). Using the wrong weight also costs accuracy: RMSE $0.9485$ against the
optimal $0.8944$, a $6\%$ penalty. Understating the observation error makes a
reconstruction both overconfident and less accurate.

---

## ★6 — Small spread, biased answer

The posterior spread is a function of the *stated* variances only: it answers
"how tightly do the prior and the observation agree?" If the prior and proxy
agree closely — or if the proxy error is declared small — the posterior is tight
regardless of whether either input is unbiased. The bias enters through the
means: the estimator is $\mu_p + G(y-\mu_p)$, so a biased observation shifts the
posterior by $G$ times the bias, and no term of the variance formula sees it. The
spread and the bias are therefore independent properties, and a reconstruction
must report both — which requires an independent comparison, since neither the
prior nor the proxy can supply one.

---

## ★7 — Separating calibration error from structural model error (specification)

**Data needed.** (i) A calibration period with co-located instrumented climate
and proxy measurements, to estimate calibration error. (ii) A set of independent
palaeoclimate observations for the target period, withheld from the
reconstruction. (iii) At least two models (or one model with perturbed closures)
so that structural spread is measurable.

**Diagnostic.** Decompose the reconstruction error against the withheld
observations into (a) the mean bias, which measures the transportability of the
calibration and the model's mean-state error together, and (b) the scatter, which
measures the random terms. Then repeat the reconstruction with each model
separately: if the bias changes sign or magnitude between models, structural
error dominates; if it is common to all models, the calibration is the likely
cause.

**Confound that cannot be removed.** The withheld observations are proxies too,
so they carry their own calibration error. If the reconstruction is calibrated
against the same proxy family, the comparison partially tests the calibration
against itself, and the resulting agreement is optimistic. Only an independent
proxy type, or an absolutely dated and independently calibrated archive, breaks
the circularity.

---

## ★8 — Why a 20th-century validation does not transfer

The validation tests the reconstruction in the regime where it was calibrated:
the modern relationship between the proxy and the climate variable, the modern
mean state, the modern seasonal cycle and the modern atmospheric circulation. A
glacial period may differ in all four, and the demonstration quantifies what
happens when even one of them changes: a changed sensitivity produced a
$+0.794\ \mathrm{K}$ bias in the changed-regime experiment of
[16-05-04 Downscaling](../../05-climate-models/04-downscaling.md), and a wrong
slope produced $+0.299\ \mathrm{K}$ in this lesson's table. A $0.3\ \mathrm{K}$
modern agreement therefore says nothing about the same reconstruction under a
different mean state.

What else is required: (i) a test of the *relationship's* stability, for example
by showing the calibration holds across an interval with a substantial climate
excursion already known from independent evidence; (ii) independent constraints
on the specific mechanism that changed (for example a second proxy sensitive to a
different variable); (iii) explicit propagation of the structural uncertainty
implied by the range of plausible calibrations, reported as a range rather than a
line.
