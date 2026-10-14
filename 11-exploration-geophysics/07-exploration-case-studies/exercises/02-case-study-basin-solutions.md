# Solutions — 11-07-02 Case Study: Basin Analysis and Play Assessment

> **Read after attempting the exercises.** Numbers were computed, not estimated by
> hand. All values are **SYNTHETIC** argument archetypes; no site-specific number
> is quoted anywhere in this lesson.

Lesson: [02 Case Study: Basin Analysis and Play Assessment](../02-case-study-basin.md).

---

## ★1 — Independent play chance

$$ \mathrm{CoS} = 0.5 \times 0.6 \times 0.7 \times 0.8 = 0.168. $$

It is a model because the multiplication **assumes** the four elements are
independent, and in a basin they usually share at least one controlling process
(a thermal history, a tectonic event, or a sedimentation regime). The product is
the value of the joint probability *under that assumption*, not the joint
probability itself.

---

## ★2 — Amplitude anomaly posterior

$$ \mathrm{PPV}(p = 0.1) = \frac{0.1(0.8)}{0.1(0.8)+0.9(0.4)}
= \frac{0.08}{0.44} = 0.182, $$
$$ \mathrm{PPV}(p = 0.4) = \frac{0.32}{0.32+0.24} = 0.571. $$

At the lower prior, $1 - 0.182 = 0.818$ of flagged anomalies are brine or
lithology, so 10 anomalies contain about **8.2 dry wells**. The anomaly triples
the prior (0.1 to 0.18) and is still a poor basis for a drilling programme.

---

## ★3 — Break-even and EMV

$$ q^{*} = \frac{C}{\mathbb{E}[V_{\text{gross}}]} = \frac{C}{6C} = 0.167. $$

$$ \mathrm{EMV} = q\,\mathbb{E}[V_{\text{gross}}] - C = 0.40(6C) - C = 1.4C. $$

A positive EMV of $1.4C$ per well. Note the risk: $q = 0.40$ means a 60% chance of
a dry hole, so a single well is far more likely to fail than to succeed even
though the EMV is positive. The EMV is a portfolio quantity.

---

## ★4 — High, equal marginals with a shared factor

Independent:

$$ \mathrm{CoS} = 0.7^{5} = 0.168. $$

With a shared factor at $\rho = 0.5$, the same construction as the demonstration
(a common normal deviate plus an independent one, each element present when the
sum exceeds its threshold) gives a joint chance of about **0.36** — more than
twice the independent value.

**Why the correlated value is larger.** With all marginals above 0.5, each element
is individually more likely present than absent. Under positive correlation the
elements move together, so the "all present" configuration is visited more often
than scattered configurations would give, and the joint probability rises toward
the smallest marginal (0.7) as $\rho \to 1$. The independent product is therefore
the *pessimistic* end of the range for a play whose elements are all individually
probable and positively correlated.

---

## ★5 — Success and profit

$$ P(\text{profitable}) = q\,P(V_{\text{gross}} \ge C) = 0.35(1-0.25) = 0.2625. $$

$$ \mathrm{EMV} = q\,\mathbb{E}[V_{\text{gross}}] - C = 0.35(5C) - C = 0.75C. $$

**Which number to show a board.** Both, with the distinction stated: the EMV
($+0.75C$ per well) describes the portfolio, and the probability of a profitable
outcome (26%) describes the single well. A board deciding on *one* well should
see the 26%; a board deciding on a *programme* should see the EMV and the number
of wells. Presenting only the EMV, or only the probability, misrepresents the
decision at hand.

---

## ★6 — Value of information by prior

Let $\mathbb{E}[V_g] = V$ (mean gross), so the well cost is $0.5V$ and the survey
cost is $0.1V$. Blind EV $= \max(0,\, pV - 0.5V)$.

For each prior, compute $P(+) = p(0.8) + (1-p)(0.15)$, the posterior
$q_{+} = 0.8p/P(+)$, $q_{-} = 0.2p/(1-P(+))$, and

$$ \mathrm{EV}_{\text{survey}} = -0.1V + P(+)\max(0, q_{+}V - 0.5V)
+ (1-P(+))\max(0, q_{-}V - 0.5V). $$

| $p$ | EV blind | $P(+)$ | $q_{+}$ | $q_{-}$ | EV survey | VOI |
|---|---|---|---|---|---|---|
| 0.05 | $0$ | 0.1825 | 0.219 | 0.012 | $-0.100V$ | $-0.100V$ |
| 0.45 | $0$ | 0.4425 | 0.814 | 0.161 | $+0.039V$ | $+0.039V$ |
| 0.70 | $+0.200V$ | 0.6050 | 0.926 | 0.354 | $+0.158V$ | $-0.042V$ |

**Most valuable at $p = 0.45$.** At $p = 0.05$ no result justifies a well
($q_{+} = 0.219$ is far below the 0.5 break-even), so the survey cannot change
anything and its cost is lost. At $p = 0.70$ the blind EV is already positive, so
a positive survey result only confirms the decision; the negative branch occurs
39.5% of the time and would stop a well, but that saving does not cover the
survey cost — so the survey *reduces* value at this prior. The intermediate prior
is where the survey both flips the decision and is likely to do so.

---

## ★7 — Frontier play assessment (specification)

**Elements and evidence.**

| Element | Evidence I would use | Uncertainty |
|---|---|---|
| Source | Analogue basin modelling, regional geochemistry, any well penetrations | Large: no calibration in a frontier |
| Reservoir | Seismic facies, inversion where data quality allows, regional analogues | Large: diagenesis unknown |
| Seal | Seismic continuity, structural history | Moderate |
| Trap | Seismic structure and closure mapping; the geophysical contribution is strongest here | Small-to-moderate: geometry is measurable |
| Timing | Burial history against trap formation | Moderate-to-large |

**Correlation structure.** I would assume a shared thermal/tectonic factor
coupling **source and timing** (both depend on the burial history) and a shared
depositional factor coupling **reservoir and seal** (both depend on the
stratigraphic succession), with the two groups nearly independent. In the
demonstration's construction that means two shared factors rather than one, with
each group's internal correlation high and the cross-group correlation low.

**Justification.** The couplings are geological, not statistical: a single
subsidence history sets maturity and the age of trap formation together, and a
single depositional episode sets both the reservoir facies and the sealing
mudstone. Choosing one correlation parameter for all pairs would average over
both mechanisms and misstate both.

**Decision rule.** Rank prospects by posterior chance of *commercial* success
(using the EMV, not the CoS); drill in order until the marginal EMV falls below
zero; state the number of wells implied and the assumed correlation structure
explicitly, so that a reviewer can test the sensitivity of the ranking to the
correlation.

---

## ★8 — A more defensible dependence model

**Pairs to couple strongly.**

1. **Source and timing.** Both are functions of the burial history; a single
   subsidence model makes them move together. Modelled as a shared thermal
   factor, with the coupling estimated from the range of burial histories
   consistent with the available maturity indicators.
2. **Reservoir and seal.** Both are stratigraphic; a change in the depositional
   model (a shelf instead of a slope, a transgression instead of a regression)
   changes both together. Modelled as a shared stratigraphic factor, with the
   coupling estimated from the distribution of net-to-gross and seal thickness in
   analogue wells or outcrop analogues.

**Pair to treat as nearly independent.**

3. **Trap and source.** Trap geometry is structural (fault and fold geometry),
   source is thermal. They can be coupled through tectonics, but the coupling is
   weaker and, crucially, *measurable*: the trap is imaged by seismic and the
   source is inferred from the basin model, so the two evidence streams are
   partly independent.

**How to estimate each coupling.** (a) From a **drilled-outcome database** in the
same or an analogue basin: fit a joint (multivariate probit or log-linear) model
to the element-presence vectors of previously drilled prospects. (b) From
**stochastic basin models**: generate many burial/depositional histories, derive
element presence from each, and compute the implied correlation directly — this
gives the dependence implied by the geology rather than by any drilling. (c) From
**expert elicitation with a structured protocol** (for example asking for
conditional probabilities $P(\text{source}\mid\text{timing})$ rather than
marginals), used when data are absent and labelled as elicited.

**Effect on the chance of success and the decision.** Coupling two pairs
strongly, instead of assuming one common factor, typically moves the joint chance
*downward* relative to a single global factor (because the two groups are then
allowed to fail independently) but *upward* relative to the independent product.
The decision changes mainly through the **ranking**: prospects whose elements are
coupled through the same mechanism lose their apparent diversification, while
prospects whose elements derive from independent evidence streams keep it. In a
portfolio sense, that is the difference between betting on one basin hypothesis
several times and betting on several.

---

## Worked mastery checkpoint

**(a) Chance of success.**

$$ \mathrm{CoS}_{\text{ind}} = 0.55(0.65)(0.75)(0.80)(0.90) = 0.193. $$

With a shared factor at $\rho = 0.4$, the joint chance is **higher** — of order
$0.33$, applying the demonstration's ratio of about $1.7$ for $\rho = 0.4$ to
these marginals. The direction is upward because all five marginals exceed 0.5
and the elements move together; a scatter of failures is less likely than a
common success or a common failure.

**(b) DHI posterior.** With $p = 0.193$, $\mathrm{TPR} = 0.75$,
$\mathrm{FPR} = 0.30$:

$$ \mathrm{PPV} = \frac{0.193(0.75)}{0.193(0.75)+0.807(0.30)}
= \frac{0.1448}{0.1448+0.2421} = 0.374. $$

**(c) EMV and break-even.** With a well cost $C$ and a mean gross value $8C$:

$$ \mathrm{EMV} = 0.374(8C) - C = 2.99C - C = 1.99C, \qquad
q^{*} = \frac{C}{8C} = 0.125. $$

The posterior of 0.374 is well above the break-even of 0.125, so the well is
justified on these numbers.

**(d) The additional survey** costs $0.2C$ with $\mathrm{TPR} = 0.8$,
$\mathrm{FPR} = 0.15$. Then $P(+) = 0.374(0.8)+0.626(0.15) = 0.393$,
$q_{+} = 0.299/0.393 = 0.761$ and
$q_{-} = 0.374(0.2)/0.607 = 0.123$:

$$ \mathrm{EV}_{\text{survey}} = -0.2C + 0.393\left(0.761(8C)-C\right)
+ 0.607\max(0,\ 0.123(8C)-C) = -0.2C + 0.393(5.09C) + 0 = 1.80C. $$

$$ \text{VOI} = 1.80C - 1.99C = -0.19C. $$

**Do not run the survey.** The blind decision is already positive, so a positive
result adds little; the negative branch ($q_{-} = 0.123$, essentially at
break-even) saves almost nothing, and the survey cost is not recovered. This is
the non-monotonicity of Section 3.4: value of information is largest at
intermediate priors, where the decision can actually change.
