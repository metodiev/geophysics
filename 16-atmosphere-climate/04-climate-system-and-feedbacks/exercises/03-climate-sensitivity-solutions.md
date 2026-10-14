# Solutions — 16-04-03 Climate Sensitivity: Definitions and Estimation

> **Read after attempting the exercises.** Numbers were computed, not estimated
> by hand.

Lesson: [03 Climate Sensitivity](../03-climate-sensitivity.md).

---

## ★1 — ECS, TCR and their ratio

$$\text{ECS} = \frac{F_{2\times}}{|\lambda|} = \frac{3.7}{4.0}
= 0.9250\ \mathrm{K},$$

$$\text{TCR} \approx \frac{F_{2\times}}{|\lambda|+\kappa}
= \frac{3.7}{4.0+0.76} = 0.7773\ \mathrm{K},$$

$$\frac{\text{TCR}}{\text{ECS}} = \frac{0.7773}{0.9250} = 0.840 .$$

A stronger feedback (larger $|\lambda|$) reduces *both* numbers, and it reduces
ECS proportionally more than TCR, so the ratio rises. That is a general
property of the approximation: TCR/ECS $= |\lambda|/(|\lambda|+\kappa)$.

---

## ★2 — Doubling times and pathway dependence

$$t_{2}(0.5\%) = \frac{\ln2}{\ln1.005} = \frac{0.69315}{0.0049875}
= 139.0\ \mathrm{yr},$$

$$t_{2}(2\%) = \frac{\ln2}{\ln1.02} = \frac{0.69315}{0.019803}
= 35.0\ \mathrm{yr}.$$

**The slower pathway (0.5% yr⁻¹) gives the larger TCR**, because the system has
139 years instead of 35 to approach equilibrium before the forcing reaches
$F_{2\times}$. TCR is defined *at* the doubling, so it depends on how long the
forcing took to get there. ECS does not.

---

## ★3 — Would doubling ECS double TCR?

**No.** Both follow $F/|\lambda|$ only in their limiting forms, and the two have
different governors: ECS depends on the equilibrium feedback alone, while TCR
depends additionally on $\kappa$ and on the trajectory. In the approximation,
$\text{TCR} = F_{2\times}/(|\lambda|+\kappa)$ and
$\text{ECS} = F_{2\times}/|\lambda|$: doubling ECS by halving $|\lambda|$ gives

$$\text{TCR}' = \frac{F_{2\times}}{|\lambda|/2 + \kappa},$$

which is less than double for $\kappa>0$. Numerically with $|\lambda| = 3.5$,
$\kappa = 0.759$: ECS rises from 1.0571 to 2.1143 K (doubling, by construction),
while TCR rises from 0.8688 to $3.7/(1.75+0.759) = 1.4747$ K, an increase of
69.7% against ECS's 100%. **Part of the doubled equilibrium response is held
back by the ocean, so TCR cannot double when ECS does.**

---

## ★4 — TCR versus ocean heat uptake

$$|\lambda| = 3.5\ \mathrm{W\,m^{-2}K^{-1}}:
\quad \text{TCR}(\kappa) = \frac{3.7}{3.5+\kappa}.$$

| $\kappa$ (W m⁻² K⁻¹) | TCR (K) |
|---|---|
| 0.4 | 0.9487 |
| 0.8 | 0.8605 |
| 1.4 | 0.7551 |
| $\to0$ | 1.0571 |

**The limit $\kappa\to0$ is ECS.** Physically, $\kappa\to0$ means the ocean takes
up no heat at all during the transient, so the surface must reach its
equilibrium temperature by the time the forcing doubles — the distinction
between transient and equilibrium responses disappears. Conversely, an ocean
that absorbs heat efficiently (large $\kappa$) keeps the surface far from
equilibrium.

---

## ★5 — Median, range and skew

With $\lambda$ uniform on $[-3.5,-2.0]$, $u = |\lambda|$ is uniform on
$[2.0,3.5]$ and $\text{ECS} = 3.7/u$ **decreases** with $u$. Hence the median
ECS corresponds to the median $u$: $\text{median}\,\text{ECS} = 3.7/2.75
= 1.345$ K.

Percentiles invert: the 5th percentile of ECS corresponds to the 95th of $u$:
$3.7/3.425 = 1.080$ K; and the 95th of ECS to the 5th of $u$:
$3.7/2.075 = 1.783$ K. A $2\times10^6$-point Monte Carlo gives 1.346, 1.080 and
1.784 K, confirming the inversion.

Half-widths about the median: $1.783-1.345 = 0.438$ above and
$1.345-1.080 = 0.265$ below, a ratio of **1.65**.

**Comment.** A symmetric uncertainty statement ("$1.35 \pm 0.3$ K") would put
the same weight on the two sides and would understate the upper tail by about
40%. For a reciprocal relationship the skew is not a detail — it is the shape of
the answer, and it is why the 5–95% interval should be quoted as an *interval*.

---

## ★6 — A regression that disagrees with its own forcing

**(a)** $\text{ECS} \approx F_{2\times}/|\text{slope}| = 3.7/4.5
= 0.8222$ K.

**(b)** The intercept (3.88) exceeds the true forcing (3.7) by 4.9%, and the
slope exceeds $|\lambda|$ at $T=0$ — the same pattern the lesson's table
produces when $|\lambda|$ *increases* with temperature: curvature in
$N(\Delta T)$ tilts both the fitted slope and the fitted intercept up. So yes,
the pattern is consistent with a strengthening amplification.

**(c)** The diagnostic that separates this from other causes is the **window
dependence**: recompute the regression over several window lengths. A
drift-induced bias moves the slope systematically and monotonically with window
length while $R^2$ stays high; an error from noise, or from a mis-specified
forcing, does not produce that pattern.

---

## ★7 — Why $R^2 = 0.998$ does not establish ECS

The argument has three steps.

1. **The regression is fitting a different quantity than ECS.** The fitted slope
   is a trajectory-weighted average of $|\lambda(T)|$ over the temperatures the
   window sampled:
   $\text{slope} \approx -[|\lambda_0| + c\,T_w]$ where $T_w$ is a weighted mean
   temperature. ECS is governed by $|\lambda|$ at the *equilibrium* temperature,
   which the window never reaches.
2. **The evidence is in the lesson's table.** Every window there has
   $R^2 > 0.996$, yet the implied ECS moves from 0.8268 K (20 yr) to 0.7439 K
   (2000 yr), a 10% spread, monotonically with window length. A statistic that
   stays at 0.998 while the answer moves by 10% cannot be validating the answer.
3. **$R^2$ measures the residual of a fit, not the bias of a parameter.** A
   nearly straight line through nearly collinear points will always fit well.
   Reporting $R^2$ is reporting that the straight-line model is adequate; it is
   not reporting that the slope equals the feedback parameter at equilibrium.

**Diagnostic to request.** The slope (and the implied ECS) as a function of
window length, with $R^2$ shown alongside. A **monotone trend** in that curve —
the pattern in the lesson's table — indicates drift-induced bias. A slope that
is flat in window length, within its own uncertainty, indicates that the
feedback is approximately state-independent over the sampled range, which is the
condition under which the regression estimate is meaningful for ECS.

---

## ★8 — How long a ramp is needed? (specification)

**Metric.** $\varepsilon(\tau) = |\text{ECS}_\text{Gregory}(\tau) -
\text{ECS}_\text{true}|/\text{ECS}_\text{true}$, where
$\text{ECS}_\text{Gregory}(\tau)$ comes from a Gregory regression on the first
$\tau$ years of the ramp.

**Plot.** $\varepsilon$ against $\tau$ on a logarithmic abscissa, and — this is
the important second panel — the *local slope* $\mathrm{d}\ln\varepsilon /
\mathrm{d}\ln\tau$ or simply the sequence of successive differences, to show
whether the curve is still moving.

**Result that would show stability rather than one lucky window.**
$\varepsilon(\tau)$ falls and then remains below the 10% threshold with no
monotone trend across a range of windows — for example within 10% for every
$\tau$ from 100 to 400 years. A single value of $\tau$ at which the error
happens to be small (as in the lesson's table, where the shortest windows are
closest to the truth) is not evidence: the estimate must be *stable* in
$\tau$, not merely accurate at one point. Because the lesson's model has a
feedback that strengthens with warming, the long-window estimates drift away
from the truth, so this design would reveal a minimum rather than a plateau —
which is itself the informative outcome and should be reported as such.
