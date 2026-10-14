# Solutions — 11-07-01 Case Study: Porphyry Copper District

> **Read after attempting the exercises.** Numbers were computed, not estimated by
> hand. All values are **SYNTHETIC** argument archetypes; no site-specific number
> is quoted anywhere in this lesson.

Lesson: [01 Case Study: Porphyry Copper District](../01-case-study-porphyry.md).

---

## ★1 — Likelihood ratio and posterior

$$ \mathrm{LR} = \frac{\mathrm{TPR}}{\mathrm{FPR}} = \frac{0.65}{0.20} = 3.25. $$

$$ \mathrm{PPV}(p = 0.01) = \frac{0.01(0.65)}{0.01(0.65)+0.99(0.20)}
= \frac{0.0065}{0.2045} = 0.0318, $$
$$ \mathrm{PPV}(p = 0.10) = \frac{0.10(0.65)}{0.10(0.65)+0.90(0.20)}
= \frac{0.065}{0.245} = 0.2653. $$

---

## ★2 — Targets per discovery

$$ \frac{1}{\mathrm{PPV}} = \frac{1}{0.0318} = 31.5. $$

About **31 drilled anomalies per discovery** at a 1% base rate, with an indicator
that is by any measure a good one.

---

## ★3 — Magnetic depth from a half-width

$$ \text{compact: } z = \frac{x_{1/2}}{0.766} = \frac{180}{0.766}
= 235\ \mathrm{m}, \qquad
\text{cylinder: } z = x_{1/2} = 180\ \mathrm{m}. $$

A 30% difference from the shape assumption, on a noiseless profile.

---

## ★4 — Combined indicators

With $p = 0.02$ and $\mathrm{LR} = 0.7/0.2 = 3.5$, the posterior odds are
$(p/(1-p))\mathrm{LR}^{n}$:

| $n$ | posterior |
|---|---|
| 1 | 0.0667 |
| 2 | 0.2000 |
| 3 | 0.4667 |

If two of the three share a cause, they cannot both be counted: the effective
number of indicators falls to **2** (one representative of the shared cause, plus
the third), giving **0.2000**.

$$ \text{ratio} = \frac{0.4667}{0.2000} = 2.33. $$

The correlated treatment gives **less than half** the independent probability, at
$n = 3$ — and the gap widens with every further indicator, because the
independent model multiplies by $\mathrm{LR}$ each time while the correlated
model does not.

---

## ★5 — Break-even and decision

$$ q^{*} = \frac{C}{V} = \frac{C}{50C} = 0.02. $$

$$ \mathbb{E}[\text{hole}] = q(50C) - C = C(50q - 1): $$

| $q$ | expected value | decision |
|---|---|---|
| 0.01 | $-0.5C$ | do not drill |
| 0.03 | $+0.5C$ | drill |
| 0.10 | $+4.0C$ | drill |

The break-even is a 2% chance of a discovery when a discovery pays 50 times a
hole. The decision is dominated by the ratio $V/C$, not by the survey's
resolution.

---

## ★6 — What shape did the interpreter assume?

With $x_{1/2} = 300\ \mathrm{m}$:

$$ \text{compact: } z = \frac{300}{0.766} = 392\ \mathrm{m}; \qquad
\text{cylinder: } z = 300\ \mathrm{m}. $$

A reported depth of 400 m is consistent with the **compact (dipole)** assumption;
a cylinder assumption would have given 300 m. The interpreter must state which
shape was assumed, because the *data* (the half-width) do not distinguish them.

---

## ★7 — Targeting statement (specification)

**Target.** A covered porphyry copper system in a magmatic arc: an intrusive
centre with a zoned alteration assemblage, sought to a depth of a few hundred
metres beneath post-mineral cover.

**Evidence suite.** (i) Regional magnetics for the intrusive-centre magnetic
high; (ii) gravity for the dense intrusive and for depth-to-basement under cover;
(iii) IP/chargeability for the sulphide shell; (iv) EM or MT for the conductive
clay shell; (v) geology and geochemistry for the arc setting and pathfinder
elements. Each is a proxy, and each is listed with the process it proxies.

**Claimed link.** The magnetic high marks magnetite in the potassic core; the
conductive shell marks phyllic alteration; the chargeability high marks the
sulphide shell. The link is asserted as a *conceptual model*, adequate only if
the alteration zonation is intact and not overprinted.

**Alternatives, per indicator.** Magnetic high: skarn, serpentinite, magnetic
sediments, remanence-flipped bodies. Conductivity high: clay-rich host, weathered
zone, saline groundwater. Chargeability high: barren pyrite (the commonest),
graphite, clay. Any of these can produce the whole suite, which is why the
statement must say which evidence would *falsify* the porphyry hypothesis — for
example a chargeability high with an immobile-element geochemistry incompatible
with an arc intrusion.

**Base rate.** A number taken from the belt's own history of drilled targets of
this class (not from the literature of a different belt), quoted with the
definition of "economic" used. It is the largest single lever on the decision.

**Decision rule, stated in advance.** Drill a hole when the posterior exceeds
the break-even $C/V$; rank targets by posterior and drill in order until the
marginal expected value falls below zero; report the expected drill count
$1/\mathrm{PPV}$ alongside the target list.

**Falsifiability.** The statement is falsifiable because it names the observations
that would overturn it, and because its decision rule can be checked against the
next few holes.

---

## ★8 — A better dependence model

**Processes that couple the indicators.**

1. **The intrusive and hydrothermal system** couples magnetics (magnetite),
   conductivity (clay) and, through the sulphide shell, chargeability. These are
   *not* conditionally independent given "economic"; they are all manifestations
   of the same body.
2. **The cover.** Post-mineral cover suppresses magnetic, radiometric and
   geochemical indicators *together*, so cover depth is a common cause of
   "no indicator" across the whole suite.
3. **The host rock.** A conductive, clay-rich host rock raises conductivity
   everywhere and changes the detection performance of the conductivity
   indicator, and it changes the geochemical background.

**Which pairs to model as dependent.** Magnetics-conductivity (coupled by the
hydrothermal system) and magnetics-chargeability (coupled by magnetite and
sulphide zoning) are the leading dependences; geochemistry-geology coupling is
usually handled differently (geochemistry is partly definitional of the target).

**How to estimate the dependence.** Three routes, in increasing cost:
(a) from a **training set** of previously drilled targets in the same belt with
known outcomes: fit a joint model (for example a probit model with a shared
latent factor, or a log-linear model) and estimate the conditional dependence
directly; (b) from **unlabelled data** over known barren and known economic
systems elsewhere in the belt, used to estimate the conditional likelihoods
$P(\text{indicator A}, \text{indicator B} \mid \text{state})$ as a pair rather
than assuming a product; (c) from a **physics-based forward model** that
generates synthetic indicator fields from a stochastic geological model, giving
the dependence implied by the geology rather than by any drilling.

**Effect on the decision.** Counting the magnetic and conductivity indicators as
one, rather than two, can move a posterior from near-certainty to the low tens of
per cent (Section 3.2). At a break-even of a few per cent that may not change the
drill/do-not-drill answer — but it changes the **ranking** of targets and the
**expected number of holes per discovery**, which is the quantity the programme
is budgeted on. A target that looked like the best in the district can fall
several places once the correlated indicators are counted honestly.

---

## Worked mastery checkpoint

**(a) Single-indicator posterior for the IP high** ($\mathrm{LR} = 3.0$), with
$p = 0.015$:

$$ \mathrm{PPV} = \frac{0.015(0.75)}{0.015(0.75)+0.985(0.25)}
= \frac{0.01125}{0.2575} = 0.0437. $$

**(b) Combined.** Independent, all three:

$$ \text{odds} = \frac{0.015}{0.985}(3.25)(2.0)(3.0) = 0.2969
\;\Longrightarrow\; P = \frac{0.2969}{1.2969} = 0.229. $$

Counting the magnetic and conductivity indicators as **one** (they share the
intrusive cause), the effective set is two indicators — the shared representative
and the IP high:

$$ \text{odds} = \frac{0.015}{0.985}(3.25)(3.0) = 0.1485
\;\Longrightarrow\; P = 0.129. $$

The independent treatment nearly doubles the probability.

**(c) Decision.** $q^{*} = C/(60C) = 0.0167$. Both the independent (0.229) and
the correlated (0.129) posteriors exceed the break-even, so **drill** either way
— but the expected value differs by a factor of about 4
($0.229(60C)-C = 12.7C$ against $0.129(60C)-C = 6.7C$), and the *ranking* against
other targets changes materially.

**(d) The measurement that would most reduce the uncertainty:** a drill test (or,
cheaper and earlier, an immobile-element geochemistry programme) that tests the
arc affinity and the alteration's copper content. The base rate and the
correlated indicators are the dominant uncertainties, and only a hole — or an
indicator whose false-positive population is genuinely different — can reduce
them.
