# Solutions — 25-02-01 Project: Travel-Time Curves and 1-D Velocity Structure

> Read after attempting. Lesson:
> [01 Travel-Time Curves](../01-travel-time-curves.md). All values are
> **SYNTHETIC** teaching numbers printed by
> [`code/travel_time_curves_demo.py`](../code/travel_time_curves_demo.py).

---

## ★1 — Intercept time and crossover

Critical angle:

$$\sin\theta_c = \frac{V_1}{V_2} = \frac{6.00}{8.10} = 0.74074,
\qquad \theta_c = 47.79°.$$

Intercept time:

$$t_i = \frac{2H_1\sqrt{V_2^{2}-V_1^{2}}}{V_1 V_2}
= \frac{80.0 \times \sqrt{65.61 - 36.00}}{6.00 \times 8.10}
= \frac{80.0 \times 5.4415}{48.60} = 8.9572\ \mathrm{s}.$$

Crossover:

$$X_c = 2H_1\sqrt{\frac{V_2+V_1}{V_2-V_1}}
= 80.0 \times \sqrt{\frac{14.10}{2.10}}
= 80.0 \times 2.5912 = 207.30\ \mathrm{km}.$$

---

## ★2 — Branch comparison

$$T_\text{direct}(100) = \frac{100}{5.90} = 16.9492\ \mathrm{s},
\qquad
T_\text{head}(100) = \frac{100}{8.05} + 7.3797 = 12.4224 + 7.3797 = 19.8021\ \mathrm{s}.$$

$$T_\text{direct}(250) = \frac{250}{5.90} = 42.3729\ \mathrm{s},
\qquad
T_\text{head}(250) = \frac{250}{8.05} + 7.3797 = 31.0559 + 7.3797 = 38.4356\ \mathrm{s}.$$

The **direct** wave is first at 100 km; the **head** wave is first at 250 km.
At the crossover both give the same time:

$$T_\text{direct}(163.02) = \frac{163.02}{5.90} = 27.6305\ \mathrm{s},
\qquad
T_\text{head}(163.02) = \frac{163.02}{8.05} + 7.3797 = 20.2516 + 7.3797 = 27.6313\ \mathrm{s},$$

which agree to $0.0008\ \mathrm{s}$ — a rounding difference against the
demonstration's single value $27.6310\ \mathrm{s}$.

---

## ★3 — Slope uncertainty

Velocities are recovered as $V_2 = 1/b$, so by the delta method

$$\sigma_{V_2} = \left|\frac{\mathrm{d}V_2}{\mathrm{d}b}\right|\sigma_b
= \frac{\sigma_b}{b^{2}} = \sigma_b V_2^{2}.$$

Inverting:

$$\sigma_b = \frac{\sigma_{V_2}}{V_2^{2}} = \frac{0.0114}{8.0573^{2}}
= \frac{0.0114}{64.92} = 1.756\times10^{-4}\ \mathrm{s\,km^{-1}}.$$

Unit: **seconds per kilometre**, the same unit as the slope $b$, since
$\mathrm{km\,s^{-1}}$ velocity divided by $(\mathrm{km\,s^{-1}})^{2}$ reduces to
$\mathrm{s\,km^{-1}}$.

---

## ★4 — The depth and its dominant uncertainty

$$H_1 = \frac{a V_1 V_2}{2\sqrt{V_2^{2}-V_1^{2}}},
\qquad a = 7.4138\ \mathrm{s},\ V_2 = 8.0573\ \mathrm{km\,s^{-1}}.$$

| $V_1$ (km s⁻¹) | $\sqrt{V_2^2 - V_1^2}$ | $H_1$ (km) |
|---|---|---|
| 5.60 | 5.7926 | 28.87 |
| 5.90 | 5.4877 | 32.11 |
| 6.20 | 5.1377 | 35.99 |

The spread from the extreme values is $35.99 - 28.87 = 7.12\ \mathrm{km}$, i.e.
$24.6\%$ of $28.87$ km, or $\pm 3.56\ \mathrm{km}$ about the central value.

The statistical depth uncertainty propagated from $\sigma_{V_2} = 0.0114\
\mathrm{km\,s^{-1}}$ is far smaller: since $H \propto V_2/\sqrt{V_2^2-V_1^2}$,
the relative sensitivity is
$1 + V_1^{2}/(V_2^{2}-V_1^{2}) \approx 1 + 0.45 = 1.45$, so
$\sigma_H \approx 1.45 \times 32.11 \times (0.0114/8.0573) = 0.066\ \mathrm{km}$.

$$\frac{\text{model-assumption error}}{\text{statistical error}}
= \frac{3.56}{0.066} \approx 54.$$

**The assumed overburden velocity is 54 times more important than the fit
precision.** Reporting $H_1 = 32.11 \pm 0.07\ \mathrm{km}$ and omitting the
$\pm 3.6\ \mathrm{km}$ model term is the defect this item tests.

---

## ★5 — Branch selection and conditioning

Picks at 200, 220, …, 500 km: $N = (500-200)/20 + 1 = 16$ picks, all on the head
branch because $200 > 163.02\ \mathrm{km}$.

Extending to 180 km adds the offset 180, giving 17 picks. The effect on the slope
estimate follows from the lever arm of a straight-line fit: the standard error of
the slope is approximately

$$\sigma_b \approx \frac{\sigma_t}{\sqrt{\sum_i (X_i - \bar X)^{2}}}.$$

Adding $X = 180\ \mathrm{km}$ grows the offset span from 300 km to 320 km
($+6.7\%$) and the spread term by roughly $6\%$, so $\sigma_b$ — and therefore
$\sigma_{V_2}$ — falls by only about $3\%$. Against that, the new point sits just
$17\ \mathrm{km}$ past the crossover, where the head branch leads the direct
branch by only $0.77\ \mathrm{s}$; a picked direct arrival there would raise the
slope, and hence lower $V_2$, by much more than the $3\%$ gained. The correct rule
is to select the branch with a margin — begin well past $X_c$, here at
$200\ \mathrm{km}$ — and to spend the effort on better picks rather than on
extending the selection toward the kink.

---

## ★6 — The intercept is a reduced-time constant

The head-wave branch is

$$T_\text{head}(X) - \frac{X}{V_2} = t_i = \text{constant}.$$

At $X = 500\ \mathrm{km}$:

$$T_\text{head}(500) = \frac{500}{8.05} + 7.3797 = 62.1118 + 7.3797 = 69.4915\ \mathrm{s},$$

$$T_\text{head}(500) - \frac{500}{8.05} = 69.4915 - 62.1118 = 7.3797\ \mathrm{s}
= t_i\ \checkmark$$

The reduced travel time removes the along-interface travel, leaving only the delay
accumulated on the down-and-up legs. That is exactly why the intercept — and not
the absolute time — carries the depth information, and why $t_i$ is the natural
quantity to invert in the tau-p domain.

---

## ★★★7 — Resolving a 5 km layer at 30 km depth

**Geometry.** A target interface at 30 km depth under a lid of unknown velocity
requires offsets well past the crossover for that interface. With a lid of
$V_1 \approx 6.0\ \mathrm{km\,s^{-1}}$ over a target interval of
$V_2 \approx 7.0\ \mathrm{km\,s^{-1}}$, the head-wave intercept is

$$t_i = \frac{2H\sqrt{V_2^{2}-V_1^{2}}}{V_1V_2}
= \frac{60 \times 3.606}{42.0} = 5.151\ \mathrm{s},$$

and the crossover

$$X_c = 2H\sqrt{\frac{V_2+V_1}{V_2-V_1}} = 60 \times 3.606 = 216.4\ \mathrm{km}.$$

**Array.** Offsets from 10 to $450\ \mathrm{km}$, spacing $5\ \mathrm{km}$ near
the expected crossover ($200$–$260\ \mathrm{km}$) to resolve the kink, and
$20\ \mathrm{km}$ beyond it. The longest offset must exceed $2X_c$ for the target
slope to be well determined ($450 > 433$).

**Branch-selection rule.** The target branch is fitted only for $X > 1.2X_c
\approx 260\ \mathrm{km}$, where it leads the lid branch by more than the pick
uncertainty, and the two segments are fitted separately, never with one line.

**Estimator.** Weighted least squares on the reduced travel times
$T - X/V_2$ against $X$; the target velocity comes from the slope of the target
segment alone, the lid velocity from the near-offset segment, and the thickness
from the target intercept after subtracting the lid's contribution
$2H_1\sqrt{V_2^2-V_1^2}/(V_1V_2)$.

**Resolution decision.** The 5 km layer is resolved only if the target branch is
observed over a span long enough to determine its slope: the slope uncertainty is
$\sigma_b \approx \sigma_t/\sqrt{\sum(X_i-\bar X)^2}$, and the resulting thickness
uncertainty must be smaller than 5 km. With $\sigma_t = 0.05\ \mathrm{s}$ and
$N = 10$ picks spanning 200 km,
$\sum(X_i-\bar X)^{2} \approx L^{2}/12 \approx 3.3\times10^{4}\ \mathrm{km^{2}}$, so
$\sigma_b \approx 2.7\times10^{-4}\ \mathrm{s\,km^{-1}}$, i.e.
$\sigma_{V_2}/V_2 \approx \sigma_b V_2 \approx 0.19\%$ — the measurement is not the
limit.

**The dominating term.** With the lid velocity known only to $\pm5\%$, the
thickness inherits roughly

$$\frac{\delta H}{H} \approx \frac{V_1^{2}}{V_2^{2}-V_1^{2}}\cdot\frac{\delta V_1}{V_1}
= \frac{36}{13}\times0.05 = 0.138,$$

so a 30 km thickness carries a $\pm 4.1\ \mathrm{km}$ model error — comparable to
the 5 km layer itself. **Therefore the layer is not resolved by this geometry
unless the lid velocity is independently constrained** (by a borehole, a
coincident reflection profile, or the direct branch over a very long near-offset
spread). Stating that, and the offset at which the target branch first becomes
the first arrival ($216\ \mathrm{km}$), is the answer.
