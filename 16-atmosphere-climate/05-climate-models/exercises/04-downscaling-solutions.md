# Solutions — 16-05-04 Downscaling: Statistical and Dynamical

> Read after attempting the exercises. Lesson:
> [04 Downscaling](../04-downscaling.md).

---

## ★1 — Lapse-rate correction

$$T = T_c + \Gamma\,(h_c - h_f).$$

Point at $0.05\ \mathrm{km}$:

$$T = 288.0 + 6.0\,(0.30-0.05) = 288.0 + 6.0(0.25) = 288.0 + 1.5
= 289.5\ \mathrm{K}.$$

Point at $0.90\ \mathrm{km}$:

$$T = 288.0 + 6.0\,(0.30-0.90) = 288.0 - 6.0(0.60) = 288.0 - 3.6
= 284.4\ \mathrm{K}.$$

The within-box spread produced is $289.5 - 284.4 = 5.1\ \mathrm{K}$, all of it
from the orography term.

---

## ★2 — Units

$T_c$ is in K; $h_c$ and $h_f$ are in km; $\Gamma$ is in
$\mathrm{K\,km^{-1}}$. The product $\Gamma(h_c-h_f)$ has
$(\mathrm{K\,km^{-1}})(\mathrm{km}) = \mathrm{K}$, so the two terms of the sum
are both temperatures and the equation is consistent. Note that if $\Gamma$ were
given per metre, the product would be $10^{3}$ times larger — the commonest unit
error in this calculation.

---

## ★3 — A constant predictor cannot add structure

Inside a coarse box the only predictor supplied by the coarse model is the box
mean, which is a single number; any function of it is also a single number, so
every fine point inside the box receives the same prediction and the within-box
structure stays unresolved. Adding energy, or smoothing, or fitting a nonlinear
function of that constant changes nothing, because the information needed to
distinguish two points in the same box is absent from the input.

---

## ★4 — Fractions of variance removed

Fraction of the *total* fine-scale variance removed by the lapse correction:

$$1 - \frac{0.0697}{6.3487} = 1 - 0.01098 = 0.9890.$$

Fraction of the *raw residual* variance removed:

$$1 - \frac{0.0697}{1.5100} = 1 - 0.04616 = 0.9538.$$

The two numbers answer different questions, and both are useful. The first says
that fine orography explains $98.9\%$ of the total fine-scale variance in this
synthetic transect — a large number because the injected noise is small
($0.30\ \mathrm{K}$) relative to the orographic signal. The second says that of
the variance the coarse model *failed* to capture, $95.4\%$ is explained by a
fine predictor. Reporting only one of them invites the reader to assume the
other.

---

## ★5 — Bias from a changed relationship

Model prediction: $\hat T_f = a + b T_c$. Target truth:
$T_f = a' + b' T_c = a + (b-b')\bar T_c + b' T_c$.

Bias at predictor value $T_c$:

$$\hat T_f - T_f = \left[a + bT_c\right] - \left[a + (b-b')\bar T_c + b'T_c\right]
= (b-b')\left(T_c - \bar T_c\right).$$

Averaging over the target period:

$$\overline{\text{bias}} = (b-b')\left(\bar T_c^{\,\text{target}}
- \bar T_c^{\,\text{train}}\right).$$

The bias **vanishes if and only if** either the relationship is unchanged
($b'=b$) or the target period's mean predictor equals the training period's mean.
A warmer target period therefore produces a bias proportional to the warming and
to the change in sensitivity. This is the mechanism behind the demonstration's
$+0.794\ \mathrm{K}$ bias in the changed-regime experiment, and the reason the
error is systematic rather than random.

---

## ★6 — Recovering physics versus knowing it

The analytic lapse method uses the exact $\Gamma$ and therefore has only the
noise floor and any model error in its residual: RMSE $0.229\ \mathrm{K}$. The
hybrid estimates $\Gamma$ from data and obtains $-6.880$ instead of
$-6.500\ \mathrm{K\,km^{-1}}$ — an error of $0.380\ \mathrm{K\,km^{-1}}$. Over a
within-box orography standard deviation of $0.146\ \mathrm{km}$ that coefficient
error alone contributes about $0.055\ \mathrm{K}$ of RMSE, and the fit also
absorbs sampling noise from the training half, the shortfall in the intercept
(bias $+0.086\ \mathrm{K}$), and any imperfection in the assumed noise model.

The general point: a method that *recovers* a coefficient from limited data
cannot beat one that *knows* it, unless the known value is wrong. When the true
$\Gamma$ is unknown — the normal case — the fitted coefficient is preferable,
provided its uncertainty is propagated; a fixed value that is wrong produces a
bias that grows with elevation range, which is exactly the failure mode in the
changed-regime test.

---

## ★7 — Detecting non-stationarity without truth (specification)

**Diagnostic.** Monitor the *predictor–predictand relationship* rather than the
predictand. Concretely: fit the statistical downscaling on successive independent
sub-periods and test whether the coefficients differ by more than their sampling
error. A second diagnostic compares the physical relationship in the coarse model
between a training and a target period, using the same predictors.

**Data needed.** A long reanalysis or observational record with the same
predictor set, plus the coarse model's target-period predictors. The method does
not need target-period fine observations.

**What it can conclude.** If the fitted coefficients are stable across
sub-periods and the coarse model's relationship is unchanged, non-stationarity is
*not detected* — a useful but weaker statement than "absent". If the coefficients
differ significantly, the statistical product is not transportable and the
expected bias is $(b-b')(\bar T^{\text{target}}-\bar T^{\text{train}})$.

**What it cannot conclude.** It cannot bound the bias quantitatively without an
assumption about the functional form of the change, and it cannot rule out a
change that happened outside the sampled sub-periods.

---

## ★8 — Hybrid design (specification)

**Dynamical component.** A limited-area model nested in the coarse fields,
intended to supply the response of the fine-scale flow to the large-scale state:
terrain-forced circulations, land–sea contrasts, coastal gradients and
orographic precipitation. Its boundary conditions come from the coarse model, so
it inherits their errors.

**Statistical component.** A bias correction of the dynamical output against
observed local distributions, intended to remove the residual mean and variance
error of the dynamical model at station locations.

**Testing that the correction has not absorbed dynamical error.** Hold out a
period and a region: fit the correction without them, then evaluate the hybrid
against independent observations in the held-out period. If the correction has
merely absorbed the dynamical model's systematic error, its coefficients will
change substantially between the training and held-out fits, and its skill will
collapse out of sample. Report both the in-sample and out-of-sample skill, and
report the fitted coefficients for each training split — a correction whose
parameters are unstable is a symptom, whatever its in-sample score.
