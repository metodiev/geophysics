# Solutions — 18-03-06 Physical Constraints, Bounds and Feasible Model Sets

> **Read after attempting the exercises.** Numbers were computed; demonstration
> values are quoted as printed.

Lesson: [06 Physical Constraints, Bounds and Feasible Model Sets](../06-constraints.md).
All models are **SYNTHETIC**.

---

## ★1 — PAVA projection of $(2, 0.5, 1.5)$

Scan left to right: push $2$; push $0.5$ (means $2 \ge 0.5$, no violation); push
$1.5$ (means $0.5 < 1.5$, violation) → merge the last two blocks:

$$\text{merged mean} = \frac{0.5+1.5}{2} = 1.0, \qquad P(y) = (2, 1, 1).$$

**Check.** Objective at $P(y)$:
$(2-2)^2+(0.5-1)^2+(1.5-1)^2 = 0+0.25+0.25 = 0.5$. At the feasible alternative
$(2, 1.5, 1.5)$: $0 + 1 + 0 = 1.0 > 0.5$. At $(1.5,1.5,1.5)$:
$0.25+1+0 = 1.25$. The PAVA answer is best of the three, and it is the exact
projection, not an approximation.

---

## ★2 — KKT at a bound

**(a) $m \ge 1$, minimising $(m-4)^2$.** The unconstrained minimiser $m = 4$
satisfies $4 \ge 1$, so the constraint is **inactive** and the multiplier is
$\lambda = 0$. The solution is $m^\star = 4$.

**(b) $m \ge 5$.** The unconstrained minimiser $4 < 5$ violates the constraint, so
it is **active** and $m^\star = 5$. The gradient there is $2(5-4) = 2 > 0$, which
points *into* the feasible set ($m$ increasing is allowed), so the KKT
stationarity condition for $m \ge 5$ reads: gradient $= \lambda \ge 0$ with
$\lambda = 2$. The estimate is biased by $4-5 = -1$, and no data can remove that
bias while the bound stands.

---

## ★3 — Box projection

$$P_{[0,3]}(-1, 1.5, 7) = (0, 1.5, 3).$$

Two components are **active** (indices 1 and 3, at the lower and upper bounds);
one is inactive. The active count is the part of the answer supplied by the prior
rather than by the data, and it is the number to report alongside the model.

---

## ★★4 — Where the damage lands

| region | constrained RMS | unconstrained RMS | ratio |
|---|---|---|---|
| negative lobe (18 cells) | 0.7591 | 0.0543 | 13.98 |
| positive lobe (30 cells) | 0.1369 | 0.0535 | 2.56 |
| whole model (48 cells) | 0.4773 | 0.0538 | 8.87 |

The **positive lobe** is the informative row: nothing there violates the
constraint, yet its error more than doubles. A false constraint is not a local
operation; it re-shapes the whole fit because the optimal values of all cells are
coupled through the data. A practitioner who checks only the violating cells
underestimates the harm by a factor of about 3.5.

---

## ★★5 — What the residual says

$$\frac{\chi^2}{n} = \frac{1121.428}{48} = 23.36\ \text{in units of }\sigma^2,$$

i.e. each datum is misfit by about $\sqrt{23.36} = 4.8$ times the noise standard
deviation on average. A reader should conclude that the non-negativity constraint
is **positively rejected** by the data: the assumed noise model and the imposed
prior cannot both be true. The corollary is uncomfortable and worth stating: the
constraint is almost certainly physically correct for *density* in a real survey,
so the honest conclusion would be that either the noise is underestimated or the
physical model (a single density-contrast sheet) is inadequate.

---

## ★★6 — The trade with a true prior

$$\text{misfit increase} = \frac{1.485-1.000}{1.000} = 48.5\%, \qquad
\text{accuracy gain} = \frac{0.1675}{0.0447} = 3.75 .$$

**One-sentence report.** "Imposing monotonicity costs 48.5% additional
$\chi^2$ — from exactly the noise level to $1.49\,n\sigma^2$ — and reduces the
model error by a factor of $3.75$; the constraint is accepted because the
geology requires it, and the misfit is stated so that a reader can test that
claim."

---

## ★★★7 — POCS contraction model

With a constant contraction factor $c = 0.99187$ per iteration and a starting
distance $d_{10} = 0.415721$:

$$d_{400} = d_{10}\,c^{390} = 0.415721\times0.99187^{390}
= 0.415721\times4.143\times10^{-2} = 1.722\times10^{-2}.$$

$$\text{measured } d_{400} = 1.723\times10^{-2}.$$

Agreement to three significant figures. The convergence model — a constant
geometric factor independent of the iterate — is therefore correct for this
problem, which is what one expects for alternating projections onto two convex
sets that do not meet: the limit is a cycle and the distance contracts
geometrically. The practical corollary is that the contraction factor, not the
distance, is the diagnostic: a factor of $0.992$ means 400 iterations buy a
factor of 25, and no feasible number of iterations will bring the residual to
zero.

---

## ★★★8 — Detection threshold of a false bound

**Statistic.** $\Delta\chi^2 = \chi^2_{\text{constrained}}-\chi^2_{\text{unconstrained}}$
divided by $n\sigma_e^2$, as a function of the imposed violation
$\delta = m_{\mathrm{true,peak}} - m_{\mathrm{hi}}$.

**Design.** Fix the synthetic model; impose upper bounds
$m_{\mathrm{hi}} \in \{3.0, 2.9, \dots, 2.0\}$ (so
$\delta \in \{0, 0.1, \dots, 1.0\}$); for each, run the constrained inversion over
$\ge100$ noise realisations at each of four noise levels and record the median
$\Delta\chi^2/(n\sigma_e^2)$, plus the fraction of realisations in which
$\Delta\chi^2$ exceeds the $95\%$ point of a $\chi^2$ with the appropriate degrees
of freedom.

**Predicted scaling.** $\Delta\chi^2$ is quadratic in the forced violation (the
data must accommodate a perturbation linear in $\delta$), while the detection
level is a fixed multiple of $n\sigma_e^2$. Hence

$$\delta_{\min} \propto \sigma_e :$$

halving the noise halves the bound violation that can be detected. This is
testable and is the quantitative form of "a weak constraint error hides in the
noise".

**Falsification.** A threshold independent of $\sigma_e$ would indicate that the
detected quantity is not the forced misfit but something else (e.g. a numerical
artefact of the solver), and would make the residual test useless as an audit of
constraints.
