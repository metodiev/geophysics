# Solutions — 16-07-04 Impacts, Vulnerability and Risk Assessment

> **Read after attempting the exercises.** Numbers were computed, not estimated by
> hand; the arithmetic is shown.

Lesson: [04 Impacts, Vulnerability and Risk](../04-impacts-and-risk.md).

---


## ★ Foundational

## ★1 — Expected damage from a discrete hazard

$$\mathbb{E}[d] = \sum_i p_i\,d(h_i)
= 0.6(0) + 0.3(0.25) + 0.1(1.00) = 0.075 + 0.100 = 0.175.$$

$$\mathrm{EAD} = V\,\mathbb{E}[d] = 2000 \times 0.175
= \mathbf{350\ \mathrm{MU\,yr^{-1}}}.$$

Note that the median hazard ($h = 0.5\ \mathrm{m}$) produces no damage at all,
yet the expected damage is substantial: the expectation is carried by the rare
deep event.

---

## ★2 — Units

| Quantity | Symbol | Unit |
|---|---|---|
| hazard intensity | $h$ | m (here; any intensity unit) |
| exposure | $V$ | MU |
| damage function | $d(h)$ | dimensionless, in $[0,1]$ |
| hazard density | $f(h)$ | per unit of $h$ |
| expected annual damage | EAD | MU per year |

$$\left[V \int d(h) f(h)\,\mathrm{d}h\right]
= [V] \times [d] \times [f] \times [\mathrm{d}h]
= \mathrm{MU} \times 1 \times \frac{1}{\mathrm{m}} \times \mathrm{m}
= \mathrm{MU}.$$

EAD is in MU per year because the distribution is the *annual* hazard
distribution, so the expectation is already a per-year expectation. ✔

---

## ★3 — Exposure growth

$$(1.03)^{40} = e^{40\ln 1.03} = e^{40\times0.0295588} = e^{1.182352} = 3.262.$$

In words: at $3\%$ growth per year over $40$ years the exposed value is
**$3.26$ times** its starting value, before any change in the hazard, the damage
function, or prices. Exposure growth at this rate is a first-order effect on
risk, not a correction.

---

## ★★ Applied

## ★★4 — Design level and its changed return period

The 1-in-50 depth corresponds to an annual exceedance probability of $0.02$, so
$z_{0.98} = 2.0537$ and

$$h_{50} = \exp\!\left(\ln 1.0 + 0.40\times2.0537\right) = \exp(0.821480)
= 2.274\ \mathrm{m}.$$

After shifting the median to $1.20\ \mathrm{m}$, the standardised variable at the
same level is

$$z = \frac{\ln 2.274 - \ln 1.20}{0.40} = \frac{0.821480 - 0.182322}{0.40}
= 1.5979,$$

and $\Pr(h \ge 2.274) = \Phi(-1.5979) = 0.05503\ \mathrm{yr^{-1}}$. The new return
period is

$$1/0.05503 = 18.17\ \mathrm{yr}, \qquad
\text{frequency ratio} = \frac{0.05503}{0.02} = 2.75.$$

A $20\%$ change in the median makes the design level exceedable $2.75$ times as
often.

---

## ★★5 — Dependence in compound events

Marginals $p_r = 0.0238$, $p_s = 0.0181$.

Independence: $p_r p_s = 0.0238 \times 0.0181 = 0.0004308$.

At $\rho = 0.6$ the demonstration gives $0.0049$:

$$\frac{0.0049}{0.0004308} = 11.4.$$

The independence assumption understates the joint exceedance probability by a
factor of about **$11$** at a correlation of $0.6$. Independence is not a neutral
default; it is an assumption with a large numerical consequence, and it must be
stated and, where possible, estimated from the data.

---

## ★★6 — Combining factors

$$\text{combined EAD factor} = 1.30 \times 1.50 = 1.950.$$

With adaptation reducing damage by $25\%$ relative to the no-adaptation case:

$$1.950 \times 0.75 = 1.4625.$$

The **smallest single contribution** is the adaptation factor ($0.75$, the only
factor below $1$), but it is not the smallest *change*: the hazard factor $1.30$
is a $30\%$ increase, the exposure factor $1.50$ a $50\%$ increase, and adaptation
a $25\%$ decrease. Exposure dominates, so a report that highlights the hazard
factor as the main driver would be misreading the arithmetic.

---

## ★★★ Research-oriented

## ★★★7 — Exposure versus hazard (design)

**Data to generate.** A synthetic record of annual flood damage, annual maximum
hazard intensity, and annually measured exposed asset value, over $50$ years. Build
the hazard from a distribution whose median shifts by a known amount from year
$25$; build exposure by compounding a known growth rate; keep the damage function
fixed and known.

**Estimator.** Fit
$\text{damage}_t = d(h_t)\,V_t + \epsilon_t$, estimating the hazard distribution
parameters (separately for the two halves of the record) and the exposure
trajectory. Then compare the two multiplicative factors,
$\widehat{\text{hazard factor}} = \mathbb{E}[d]_{\text{late}}/\mathbb{E}[d]_{\text{early}}$
and $\widehat{\text{exposure factor}} = V_{\text{late}}/V_{\text{early}}$.

**Identification problem.** Only the *product* $d(h_t)V_t$ is observed. Without an
independent measurement of $V_t$ (asset registers, census, insurance exposure) or
of $d$ (damage curves), the two factors cannot be separated: a doubling of
exposure with a fixed hazard is observationally identical to a fixed exposure with
a hazard whose damage expectation doubles. The identification comes from external
data, not from the damage series.

**Falsification of exposure dominance.** The exposure-dominance hypothesis is
falsified if, when $V_t$ is measured independently and its trajectory is imposed,
the residual damage trend still requires a significant hazard change to fit. A
result that the residual trend is flat, and the fitted hazard parameters are
consistent between halves, supports exposure dominance for this dataset — for the
modelled world, not in general.

---

## ★★★8 — Why the damage ratio exceeds the hazard ratio

The demonstration's values are
$\mathbb{E}[d]_{1.00} = 0.1362$ and $\mathbb{E}[d]_{1.15} = 0.1887$, a ratio of
$1.386$. The ratio of the medians is only $1.15$. The damage expectation responds
**more** than proportionally.

The reason is the shape of the tail integral. Only the upper tail of the hazard
contributes to damage, and a multiplicative shift of a lognormal median moves
probability into the tail multiplicatively: at depth $h$ the exceedance
probability changes from $\Phi(-z)$ to $\Phi(-z+\ln 1.15/\sigma)$, and in the far
tail the ratio of small probabilities grows without bound. The damage function's
own convexity in the ramp region ($d \propto (h-h_0)^{1.5}$) reinforces the
effect.

General condition: the proportional change in $\mathbb{E}[d]$ exceeds the
proportional change in the hazard median whenever the damage-weighted mass of the
distribution sits in a region where the **exceedance probability is
log-concave and steeply decreasing** — effectively, whenever damage depends on
the tail rather than on the bulk. A damage function that saturates *below* the
shifted median — for example a structure already destroyed at $h = 1.0\
\mathrm{m}$, so that $d(h) = 1$ for all larger $h$ — violates it: once the median
is above the saturation depth, further hazard increase cannot raise expected
damage, and EAD becomes insensitive to the hazard. That is the physical example:
**full saturation converts a tail problem into a binary one**, and adaptation that
caps damage at a low threshold removes the sensitivity to further hazard change.
