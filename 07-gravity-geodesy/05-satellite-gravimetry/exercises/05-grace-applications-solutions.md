# Solutions — 07-05-05 Applications: Groundwater Depletion, Ice Loss, Sea Level

> **Read after attempting the exercises.** Numbers were computed, not estimated
> by hand. All values are **SYNTHETIC** teaching values.

Lesson: [05 Applications](../05-grace-applications.md).

Constants: $\rho_w = 1000\ \mathrm{kg\,m^{-3}}$,
$A_{\text{ocean}} = 3.6113\times10^{14}\ \mathrm{m^{2}}$.

---

## ★1 — Mass rate and sea-level rate

$$A = 2\times10^{5}\ \mathrm{km^{2}} = 2\times10^{11}\ \mathrm{m^{2}},$$
$$\Delta M = \rho_w\,\Delta h\,A = 1000 \times 0.040 \times 2\times10^{11}
= 8.0000\times10^{12}\ \mathrm{kg\,yr^{-1}},$$
$$\Delta \mathrm{SL} = \frac{\Delta M}{\rho_w A_{\text{ocean}}}
= \frac{8.0000\times10^{12}}{1000 \times 3.6113\times10^{14}}
= 2.215\times10^{-5}\ \mathrm{m\,yr^{-1}} = 0.0222\ \mathrm{mm\,yr^{-1}} .$$

**Check the scale:** $10^{6}\ \mathrm{km^{2}}$ at $1\ \mathrm{cm\,yr^{-1}}$ gave
$0.0277\ \mathrm{mm\,yr^{-1}}$ in the lesson. Here the area is five times smaller
and the trend four times larger, so the expected sea-level rate is
$(4/5)\times0.0277 = 0.0222$ ✔.

---

## ★2 — The seasonal-omission bias

Bias: $-1.072 - (-1.000) = -0.072\ \mathrm{cm\,yr^{-1}}$, i.e. the fitted trend
is *more negative* than the truth by $0.072\ \mathrm{cm\,yr^{-1}}$, which is
larger than the fit's own standard error of $0.063$.

**Why a bias and not just noise:** a seasonal term is a *deterministic* function
of time. Over a finite record, the projection of $\sin(2\pi t/12+\phi)$ onto the
basis functions $\{1, t\}$ is not zero: the sinusoid is not orthogonal to a
straight line on an interval that contains only a few cycles. So the least-squares
fit distributes some of the seasonal amplitude into the slope, and the amount
depends on the record length and on the phase $\phi$ — but not on the noise. Averaging
over many noise realisations would not remove it; only fitting the seasonal term
does.

---

## ★3 — Significance

$$|b|/\sigma_b = 1.20/0.30 = 4.0
\quad\Longrightarrow\quad
\text{a zero trend is excluded at } 4\sigma .$$

With $\sigma_b = 0.45\ \mathrm{cm\,yr^{-1}}$: $1.20/0.45 = 2.67$, which is below
$3\sigma$. So the trend would be "detected" at the conventional $2\sigma$ level
but not at the stricter $3\sigma$ level — and the honest report of a marginal
detection states the ratio rather than the word "detected".

---

## ★4 — Corrections and the corrected uncertainty

Corrections: solid-Earth $= +0.40\ \mathrm{cm\,yr^{-1}}$ (so subtract $0.40$ from
the measured trend) and leakage $= -0.05\ \mathrm{cm\,yr^{-1}}$ (add $0.05$):

$$b_{\text{corr}} = -1.20 - 0.40 + 0.05 = -1.55\ \mathrm{cm\,yr^{-1}},$$
$$\sigma = \sqrt{0.30^{2} + 0.20^{2} + 0.02^{2}} = \sqrt{0.0900 + 0.0400 + 0.0004}
= \sqrt{0.1304} = 0.361\ \mathrm{cm\,yr^{-1}} .$$

**Which term dominates:** the statistical error ($0.30$) still dominates, but the
solid-Earth correction ($0.20$) contributes $44\%$ of the variance. The leakage
term ($0.02$) contributes $0.3\%$ and is negligible. Report as
$-1.55 \pm 0.36\ \mathrm{cm\,yr^{-1}}$ and state the three contributions
separately, because a reader who wants to improve the number needs to know which
term to attack.

---

## ★5 — Correcting, and what to improve

$$b_{\text{corr}} = -2.0 + 0.8 = -1.20\ \mathrm{cm\,yr^{-1}},$$
$$\sigma = \sqrt{0.5^{2} + (0.5\times0.8)^{2}} = \sqrt{0.25 + 0.16}
= \sqrt{0.41} = 0.640\ \mathrm{cm\,yr^{-1}} .$$

The correction uncertainty is $0.40$, i.e. $39\%$ of the total variance
($0.16/0.41 = 0.39$).

**What to do:** reducing the correction uncertainty from $0.40$ to $0.20$ would
lower $\sigma$ from $0.640$ to $\sqrt{0.25+0.04} = 0.539$, a $16\%$ improvement.
Extending the record from $T$ to $2T$ reduces the statistical term from $0.50$ to
$0.50/2^{3/2} = 0.177$, giving $\sigma = \sqrt{0.031+0.16} = 0.437$, a $32\%$
improvement. **Here more data wins**, because the statistical term still
dominates; in the lesson's checkpoint the reverse was true. The point is that the
answer depends on the numbers, so the comparison must be made rather than
assumed.

---

## ★6 — Predicting the error from a scaling law

$$\sigma(T) \propto T^{-3/2}.$$

Four years, from the two-year value: $0.563/2^{1.5} = 0.563/2.828
= 0.199\ \mathrm{cm\,yr^{-1}}$.

Twenty years, from the ten-year value: $0.035/2^{1.5} = 0.0124\
\mathrm{cm\,yr^{-1}}$.

**Why the twenty-year prediction is optimistic:** the $T^{-3/2}$ law assumes white
noise and a purely linear trend. Over twenty years, real interannual variability
(droughts, floods, multi-year oscillations) is *not* white: it is a low-frequency
signal that projects onto the trend and is not reduced by longer records at the
predicted rate. The demonstration's own two-year fit ($-1.166$) already departs
from the ten-year value ($-1.025$) by much more than the formal error, which is
the same effect in miniature.

---

## ★7 — Testing a partition with the spatial pattern (specification)

1. **Truth model.** A partition of a synthetic total mass-change field into three
   components, each with a *stated spatial signature*: e.g. a groundwater
   component confined to a lowland polygon with a smooth interior taper, an
   ice-mass component on a stated plateau, and a solid-Earth component with a
   broad, regionally uniform trend. Choose amplitudes so that the *total* is
   dominated by one component but the *pattern* differs.
2. **Forward model.** Expand each component into coefficients with the layer
   formula of [04](../04-mascons-and-leakage.md), sum them, truncate at
   $L = 40$, and add per-coefficient white noise.
3. **Observation operator.** Apply the same $400\ \mathrm{km}$ Gaussian filter to
   both the synthetic observations and each candidate model prediction — the
   "filter both sides" rule. This is essential: comparing filtered data with
   unfiltered models manufactures a pattern difference.
4. **Diagnostic.** For each candidate partition, compute the residual field and
   its *spatial* $\chi^{2}=\mathbf{r}^{\mathsf T}C^{-1}\mathbf{r}$ using the
   coefficient covariance. Report $\chi^{2}$ per independent coefficient, not the
   total mass residual.
5. **Alternative hypothesis rejected.** Given the truth being partition A, the
   test should reject a partition B whose total agrees with A but whose
   *pattern* is wrong — for example one that puts half of the lowland signal on
   the plateau. Test this by constructing B explicitly.
6. **What it still cannot distinguish.** Any two partitions whose difference lies
   in the null space of the (truncated, filtered) observation operator — e.g. a
   redistribution of mass within one filter kernel width, or a swap of two
   components with the same spatial footprint. The test has power against
   *spatially distinguishable* alternatives only, and the report should name the
   ones it cannot see.

---

## ★8 — Effect of correlated errors (specification)

1. **Truth and observation.** Reuse the lesson's synthetic basin trend, but draw
   the monthly coefficient errors from a Gaussian with a *non-diagonal*
   covariance: white in time, and spatially correlated in degree with a
   correlation length of a few degrees (a decaying covariance in $\ell$ and $m$,
   normalised to a stated per-coefficient variance).
2. **Procedure.** Forward the correlated errors through the same filter and
   basin integration to produce a synthetic monthly basin series; repeat
   $500$ times; fit the trend with seasonals each time; measure the *empirical*
   standard deviation of the fitted trends.
3. **Control.** Repeat with diagonal (white) errors of the same per-coefficient
   variance, and with the formal least-squares error from a single realisation.
4. **Prediction and direction.** Correlated errors add *coherently* over the
   coefficients that make up the basin average, so the empirical trend error
   should exceed the formal error computed from white noise — typically by a
   factor of a few, and the factor should grow as the correlation length grows
   toward the basin size. In the limit of a correlation length larger than the
   basin, the error behaves like a single random number per month and the trend
   error inflates by roughly the square root of the number of effectively
   independent coefficients.
5. **What the experiment establishes.** That the formal error of a basin trend is
   a *lower bound* whose tightness depends on an assumption (independence) that
   real solutions violate most strongly exactly where basins are largest — i.e.
   where the reported trends matter most.
