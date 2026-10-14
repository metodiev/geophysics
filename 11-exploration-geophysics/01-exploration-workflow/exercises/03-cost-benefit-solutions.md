# Solutions — 11-01-03 Cost, Risk and Value of Information in Exploration

> **Read after attempting the exercises.** Numbers below were computed, not
> estimated. All payoffs, probabilities and prices are **SYNTHETIC** teaching
> values. Throughout, $V(p) = \max(0, pW-(1-p)K)$ and
> $\mathrm{EVPI} = \min(pW,(1-p)K)$.

Lesson: [03 Cost, Risk and Value of Information](../03-cost-benefit.md).

---

## ★1 — Indifference probability and EMV

$$p^{*} = \frac{K}{W+K} = \frac{80}{480} = 0.16667 .$$

| $p$ | EMV drill $= pW-(1-p)K$ | decision |
|---|---|---|
| 0.10 | $40 - 72 = -32.00$ | walk |
| 0.20 | $80 - 64 = +16.00$ | drill |
| 0.40 | $160 - 48 = +112.00$ | drill |

---

## ★2 — EVPI

$$\mathrm{EVPI} = \min(pW,(1-p)K).$$

- $p = 0.10$: $\min(40, 72) = 40.00$ MUSD.
- $p = 0.16667$: $\min(66.667, 66.667) = 66.667$ MUSD.
- $p = 0.60$: $\min(240, 32) = 32.00$ MUSD.

Largest at the indifference probability, where the two branches of the formula
meet at $KW/(W+K) = 80\times400/480 = 66.667$ MUSD. Information is worth most
where the decision is hardest: at $p=0.10$ you are already fairly sure to walk, and
at $p=0.60$ fairly sure to drill, so in neither case does information change much.

---

## ★3 — Posteriors

$$\mathbb{P}(+) = 0.20(0.75) + 0.80(0.25) = 0.15 + 0.20 = 0.35,$$
$$p_{+} = 0.15/0.35 = 0.428571, \qquad
p_{-} = 0.20(0.25)/0.65 = 0.076923 .$$

Decisions: $V(p_{+}) = 0.428571(400) - 0.571429(80) = 171.43 - 45.71
= 125.71$ MUSD → **drill**; $V(p_{-}) = 30.77 - 73.85 = -43.08 < 0$ → **walk**.

---

## ★4 — Why TPR = FPR gives zero value

If $\mathrm{TPR} = \mathrm{FPR} = r$, then
$\mathbb{P}(+) = p r + (1-p) r = r$ and

$$p_{+} = \frac{pr}{r} = p, \qquad
p_{-} = \frac{p(1-r)}{1-r} = p .$$

Both posteriors equal the prior, so $\mathbb{E}_o[V(p|o)] = V(p)$ and
$\mathrm{EVSI} = 0$. In words: the observation is independent of the state, so it
carries no information, and no amount of accuracy in an irrelevant measurement is
worth anything.

---

## ★5 — EVSI, maximum price, EVPI fraction

$$\mathrm{EVSI} = \mathbb{P}(+)V(p_{+}) + \mathbb{P}(-)V(p_{-}) - V(p)
= 0.35(125.7143) + 0.65(0) - 16.0000 = 44.0000 - 16.0000
= 28.0000\ \mathrm{MUSD}.$$

**Maximum price = 28.000 MUSD.** At a quoted price of 4 MUSD the net expected gain
is $28.000 - 4 = 24.000$ MUSD: buy it.

$$\mathrm{EVPI} = \min(0.20\times400,\,0.80\times80) = \min(80,64)
= 64.000\ \mathrm{MUSD},$$
$$\frac{\mathrm{EVSI}}{\mathrm{EVPI}} = \frac{28.000}{64.000} = 43.75\% .$$

---

## ★6 — EVSI near and far from the indifference point

Same test ($\mathrm{TPR}=0.75$, $\mathrm{FPR}=0.25$), same $W=400$, $K=80$.

**Prior $p = 0.16667$** (= $p^{*}$):
$\mathbb{P}(+) = 0.16667(0.75)+0.83333(0.25) = 0.33333$;
$p_{+} = 0.125/0.33333 = 0.375$; $p_{-} = 0.16667(0.25)/0.66667 = 0.0625$.
$V(p) = 0$, $V(p_{+}) = 100$, $V(p_{-}) = 0$, so
$\mathrm{EVSI} = 0.33333(100) = 33.333$ MUSD.

**Prior $p = 0.02$**: $\mathbb{P}(+) = 0.02(0.75)+0.98(0.25) = 0.26$;
$p_{+} = 0.015/0.26 = 0.057692$; $p_{-} = 0.02(0.25)/0.74 = 0.006757$.
Now $p_{+} < p^{*} = 0.16667$, so $V(p_{+}) = 0$ and $V(p_{-}) = 0$:
$$\mathrm{EVSI} = 0.26(0) + 0.74(0) - 0 = 0.000\ \mathrm{MUSD}.$$

**At $p = 0.02$ the survey is worth exactly nothing**, because *no possible
outcome* of it makes drilling attractive: even a positive result only lifts the
belief to 5.8%, far below the 16.7% break-even. This is the flat-zero branch of
$V$ doing the work, and it is the standard reason a very low-prior greenfields
area cannot justify geophysics by VOI arguments alone. The ordering implication:
run the survey where the *likelihoods* can move the posterior across $p^{*}$, not
where the anomaly is expected to be largest.

---

## ★7 — Quality versus price

$\mathrm{FPR} = 0.15$, prior $p = 0.20$, $W = 400$, $K = 80$, $V(p) = 16.000$.

| TPR | $\mathbb{P}(+)$ | $p_{+}$ | $V(p_{+})$ | EVSI (MUSD) | price | net (MUSD) |
|---|---|---|---|---|---|---|
| 0.70 | 0.26000 | 0.53846 | 178.46 | 30.400 | 2 | 28.400 |
| 0.85 | 0.29000 | 0.58621 | 201.38 | 42.400 | 4 | 38.400 |
| 0.95 | 0.31000 | 0.61290 | 214.19 | 50.400 | 14 | 36.400 |

Both factors improve with quality: $\mathbb{P}(+)$ rises (more true positives for
the same false-positive rate) and $V(p_{+})$ rises (a positive is more diagnostic,
so the posterior is higher), while $p_{-}$ falls further into the worthless region.
EVSI is therefore strongly increasing in TPR.

**Ranked by EVSI:** TPR = 0.95 first. **Ranked by net expected gain:** TPR = 0.85
first (38.4 against 36.4 MUSD). The quantity that changed the ranking is the
**price**: EVSI is the maximum a test is worth, not its value in the ground, and
the marginal $8.0$ MUSD of EVSI between TPR $=0.85$ and $0.95$ costs $10.0$ MUSD.
The general rule: buy while the marginal EVSI exceeds the marginal price, and stop
when it does not — which is the same first-order condition as the optimal-$n$
calculation in the lesson.

---

## ★8 — Jensen gap for $p \sim \mathrm{Beta}(2,8)$

$\mathbb{E}[p] = 2/(2+8) = 0.200$.

$$V(\mathbb{E}[p]) = V(0.20) = 0.20(400) - 0.80(80) = 80 - 64 = 16.000\ \mathrm{MUSD}.$$

$$\mathbb{E}[V(p)] = \int_0^1 \max\bigl(0,\;400p - 80(1-p)\bigr)\,
\frac{p^{1}(1-p)^{7}}{B(2,8)}\,\mathrm{d}p
= 31.009\ \mathrm{MUSD}\quad\text{(quadrature on a $4\times10^{5}$-point grid)}.$$

**Jensen gap $= +15.009$ MUSD $= +93.8\%$.** Because $V$ is convex, using the mean
probability understates the expected value — here nearly doubles it. The gap grows
with the spread of the prior: it is zero for a point prior and largest for a prior
straddling $p^{*} = 0.16667$, which this Beta(2,8) distribution does.

---

## ★9 — "Information is never worth much"

**Support, in the narrow case.** For a single prospect with $p \ll p^{*}$,
$\mathrm{EVPI} = pW$. With $p = 0.02$ and $W = 400$ this is 8 MUSD, and §6 of the
solutions shows that with a realistic test the *EVSI* is exactly zero. So for one
low-prior prospect with a test that cannot cross $p^{*}$, the manager is right, and
the right conclusion is to buy no geophysics — not to buy a cheap version of it.

**Rebut, quantitatively.**

1. **Scale with the number of shared decisions.** A regional program makes one
   decision for many prospects. With $N = 20$ prospects at $p = 0.15$ (lesson
   values $W = 500$, $K = 60$), the total EVPI is
   $20 \times \min(75, 51) = 1020$ MUSD — *larger than $W$ itself*. The manager's
   bound $(1-p)K \le K = 60$ is a **per-prospect** bound and says nothing about a
   portfolio.
2. **Compare per unit area, not per prospect.** A belt survey covering
   $2000\ \mathrm{km^{2}}$ at $60$ USD/km² (SYNTHETIC) costs $0.12$ MUSD. Against
   1020 MUSD of EVPI, the survey costs $0.012\%$ of the information value, and even
   capturing $1\%$ of the EVPI (10.2 MUSD) pays for it 85 times over.
3. **The "over the whole belt" step matters.** Each individual prospect is one
   draw; the survey's *coverage* is what makes it affordable per prospect.

**The assumption that makes the argument true:** a single isolated prospect, a
prior far from $p^{*}$, a test whose posteriors also stay far from $p^{*}$, and no
portfolio. Relax any one and the conclusion reverses — which is why VOI arguments
must always state the decision unit.

---

## ★10 — Adding a third action

Payoffs: $A_1$ = small program $(W=800, K=100)$, $A_2$ = walk (0), $A_3$ = large
program $(W = 2000, K = 300)$. Indifference probabilities
$p^{*}_1 = 100/900 = 0.11111$ and $p^{*}_3 = 300/2300 = 0.13043$.

Prior $p = 0.05$, test $\mathrm{TPR} = 0.70$, $\mathrm{FPR} = 0.10$:

$$\mathbb{P}(+) = 0.05(0.70)+0.95(0.10) = 0.13,\quad
p_{+} = 0.035/0.13 = 0.26923,\quad p_{-} = 0.05(0.3)/0.87 = 0.017241.$$

**Two-action problem:**

$$V_2(0.05) = \max(0,\;40-95) = 0,\qquad
V_2(p_{+}) = 215.38 - 73.08 = 142.31,\qquad V_2(p_{-}) = 0,$$
$$\mathrm{EVSI}_2 = 0.13(142.31) + 0.87(0) - 0 = 18.50\ \mathrm{MUSD}.$$

**Three-action problem:**

$$V_3(0.05) = \max(0,\;0,\;100-285) = 0 \quad\text{(unchanged)},$$
$$V_3(p_{+}) = \max(142.31,\;538.46-219.23) = 319.23,\qquad
V_3(p_{-}) = 0,$$
$$\mathrm{EVSI}_3 = 0.13(319.23) - 0 = 41.50\ \mathrm{MUSD}.$$

**The survey is worth more than twice as much (18.50 → 41.50 MUSD) in the
three-action problem, and the survey itself did not change.** The mechanism: $A_3$
is *never* optimal without information (it is negative at the prior and at both
posteriors except $p_{+}$), so $V(p)$ is unchanged; but at the high posterior a
larger project is now available, so $\mathbb{E}_o[V(p|o)]$ rises. This is the
general rule — **an action that only ever becomes optimal after observing the
information strictly increases the value of that information.**

The rule needs its condition. Add instead a cheap reconnaissance program
$(W=300, K=10)$: it is optimal *at the prior* ($V = 5.5 > 0 = V_2(0.05)$), so both
terms of EVSI change, and the arithmetic gives
$\mathrm{EVSI} = 0.13(142.31) + 0.87(0) - 5.5 = 13.00$ MUSD — **less than the
two-action value of 18.50 MUSD**. When the new action is a substitute for
information (cheap drilling that answers the same question), it destroys survey
value; when it is a complement (a bigger commitment that only makes sense if the
survey is positive), it creates it. The check is mechanical: evaluate the new
action at the prior and at every posterior, and see which term moves.

---

## ★11 — Auditing a value-of-information study (specification)

**Inputs to propagate.** (i) the prior $p$ — do not use a point value; (ii) the
success value $W$; (iii) the failure cost $K$; (iv) the test's operating
characteristics, as a **joint** ROC uncertainty (correlated errors in TPR and FPR),
derived from repeat lines rather than asserted.

**Quantity to report.** Not a single dollar figure. Report the **distribution of
net EVSI**, $N = \mathrm{EVSI} - \text{price}$, as a fan chart with the
$P(N > 0)$ and the $P(N < 0)$; and the **switch-point**: the value of the
geophysical parameter (for example TPR, or the anomaly amplitude threshold) at
which the sign of $N$ changes. Also report the same for $\mathrm{EVPI}$, so the
reader can see the unreachable ceiling.

**Detecting a payoff-table-driven conclusion.** Compute the sensitivity of
$\mathrm{sign}(N)$ to $W$ and $K$ alone, with the geophysics held fixed
($\mathrm{TPR} = \mathrm{FPR}$). If the conclusion "buy the survey" survives
arbitrary geophysical quality, then the geophysics is not what is driving it: the
study is a statement about the commodity price and the drilling cost. Report
$\partial N/\partial \mathrm{TPR}$ against
$\partial N/\partial W$ — the ratio says where the money actually is.

**Distinguishing a genuinely non-positive EVSI from a mis-specified action set.**
EVSI is *provably* non-negative over the real action set, so a negative EVSI is
always a bug: either the action set omits the option of ignoring the observation
(the usual cause — an implementation that forces an action instead of allowing
"take the prior-optimal action"), or the value function is not the upper envelope
of the available actions, or the posteriors are not normalised
($\mathbb{P}(+)\,\mathbb{E}[p|+] + \mathbb{P}(-)\,\mathbb{E}[p|-] = p$ — check
this identity every time). The tests to run: (1) EVSI $= 0$ when
$\mathrm{TPR} = \mathrm{FPR}$; (2) EVSI $\le$ EVPI; (3) EVSI $= 0$ when $p = 0$ or
$p = 1$; (4) adding an action never lowers $V(p)$. If all four hold and net EVSI
is negative, the negative is real and it is a statement about the price, not about
the information.
