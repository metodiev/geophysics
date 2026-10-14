# Solutions — 11-07-03 Case Study: Geothermal Field Development

> **Read after attempting the exercises.** Numbers were computed, not estimated by
> hand. All values are **SYNTHETIC** argument archetypes; no site-specific number
> is quoted anywhere in this lesson.

Lesson: [03 Case Study: Geothermal Field Development](../03-case-study-geothermal.md).

---

## ★1 — Heat in place and recoverable heat

$$ V = 8\times10^{6}\ \mathrm{m^{2}} \times 1.2\times10^{3}\ \mathrm{m}
= 9.6\times10^{9}\ \mathrm{m^{3}}, $$

$$ H = \rho c\,V\,\Delta T = (2.5\times10^{6})(9.6\times10^{9})(90)
= 2.16\times10^{18}\ \mathrm{J} = 2.16\ \mathrm{EJ}. $$

Recoverable at $0.10$: $H_{\text{rec}} = 0.216\ \mathrm{EJ}$.

**Convention reminder.** "P90" means a 90% probability of *exceeding* the value,
i.e. the conservative case. This answer is a deterministic calculation, not a
percentile; it becomes one only when the three inputs are given distributions.

---

## ★2 — Power per well and wells needed

$$ P_{\text{well}} = \frac{\dot m\,c_p\,\Delta T_{\text{wh}}\,\eta}{10^{6}}
= \frac{(30)(4200)(100)(0.10)}{10^{6}} = 1.26\ \mathrm{MWe}. $$

$$ N_{\text{wells}} = \frac{10}{1.26} = 7.94 \approx 8\ \text{wells}. $$

Note this is a *producing* well count, not a *drilled* well count: a development
drills more wells than it produces from, and the difference is part of the
resource-to-reserve conversion.

---

## ★3 — MT conductor posterior

$$ \mathrm{PPV} = \frac{0.2(0.8)}{0.2(0.8)+0.8(0.5)}
= \frac{0.16}{0.56} = 0.286. $$

So 29% of conductors indicate a productive reservoir, and 71% do not.

---

## ★4 — Expected event counts

$$ P(M \ge m \mid M \ge 0) = 10^{-b m} = 10^{-1.1m}: $$

$$ P(M \ge 2) = 10^{-2.2} = 6.31\times10^{-3}
\;\Longrightarrow\; 5000(6.31\times10^{-3}) = 31.5\ \text{events}, $$
$$ P(M \ge 3) = 10^{-3.3} = 5.01\times10^{-4}
\;\Longrightarrow\; 5000(5.01\times10^{-4}) = 2.5\ \text{events}. $$

A traffic-light level at $M = 3$ would trigger about 2 to 3 times over this
sequence, regardless of any site-specific fault. Report the count with the level.

---

## ★5 — Recovery-factor sensitivity

$$ \text{recoverable} = H\,R, \qquad
\bar P_{e} = \frac{H\,R\,\eta}{30\ \mathrm{yr}}; $$

| $R$ | recoverable (EJ) | average $\bar P_e$ (MWe) |
|---|---|---|
| 0.05 | 0.15 | 15.8 |
| 0.10 | 0.30 | 31.7 |
| 0.20 | 0.60 | 63.4 |

The answer is **linear in the recovery factor**, which is an engineering
assumption, and the range 0.05-0.20 is entirely plausible a priori. So the largest
single uncertainty in this estimate is not the reservoir volume or the
temperature; it is a number the geophysics cannot measure. That is the lesson's
central warning about resource arithmetic.

---

## ★6 — Expected value of a slim hole

$$ \mathrm{EV} = \mathrm{PPV}\,(20C) - C. $$

At a prior of $0.30$: $\mathrm{PPV} = \frac{0.24}{0.24+0.35} = 0.407$,
$\mathrm{EV} = 0.407(20C) - C = 7.14C$.

At a prior of $0.10$: $\mathrm{PPV} = \frac{0.08}{0.08+0.45} = 0.151$,
$\mathrm{EV} = 0.151(20C) - C = 2.02C$.

Both are positive, and the higher-prior case is more than three times as
attractive. The decision is driven by the **prior** and by the **value ratio**
$V/C = 20$; the MT result only shifts it. This is why the first question a
reviewer should ask about a geothermal prospect is what the regional prior is and
how it was established, not what the MT section looks like.

---

## ★7 — Exploration programme (specification)

| Method | What it measures | False-positive mode |
|---|---|---|
| Magnetotellurics (broadband, array) | Resistivity structure: the conductive clay cap and the deeper resistive reservoir | A conductive layer that is saline brine, graphite or a sedimentary clay rather than an alteration cap |
| Gravity (and microgravity where accessible) | Density structure: the dense intrusive, the basin geometry, the reservoir's structural closure | A dense unit unrelated to the thermal system |
| Microseismicity (temporary array) | Permeability: where the reservoir is fractured and deforming | Tectonic seismicity unrelated to the reservoir; detection bias from an inadequate network |
| Regional geology and geochemistry | Heat source, structural controls, fluid chemistry | (non-geophysical) |
| Temperature-gradient slim holes (verification) | The actual temperature gradient and a fluid sample | A gradient that is local to a fault |

**Decision rule, stated in advance.** Locate the clay cap (the conductor's top)
and the resistive reservoir beneath it; require a coincident gravity low (or the
structural closure) and a microseismic lineament indicating permeability; rank
sites by the posterior probability of a productive reservoir. Drill a
temperature-gradient slim hole when the posterior exceeds the break-even set by
the slim-hole cost and the value of the information it provides — and treat that
information (the actual gradient) as the largest single update to the posterior.

**Falsifiability.** The programme's final product is a ranked list with an
explicit criterion and a stated error rate; a later dry slim hole that met the
criterion counts against the criterion, and the criterion should then be
re-examined.

---

## ★8 — Traffic-light protocol (specification)

Assume a monitoring network with a stated detection capability (for example,
complete for $M \ge M_c$ within a stated radius) and a forecast sequence of
$N$ events above a reference magnitude.

| Level | Trigger | Action |
|---|---|---|
| Green | seismicity at or below the forecast background | normal operation |
| Amber | exceedance of a stated rate or a single event above $M_1$ | reduce injection rate/pressure, increase monitoring, notify |
| Red | a single event above $M_2$, or a sustained rate above the amber level | stop injection, bleed off pressure, review before resumption |

**Expected stoppages.** With $b = 1$ and $N = 5000$ events above $M = 0$, the
expected count above $M_2 = 2.5$ is
$5000 \times 10^{-2.5} = 15.8$. If the red level is $M_2 = 3.0$, the expectation
is $5000 \times 10^{-3} = 5.0$ stoppages. These counts are part of the protocol,
not an aside: a regulator and an operator must agree on them before the project
starts, because they determine whether the operation is viable.

**What the protocol does not control.** The $b$-value, the total number of events
and the coupling between injection and the largest event. A protocol limits the
*consequence* of exceeding a threshold; it does not prevent the threshold from
being exceeded.

**The measurement that would most improve it.** A **site-specific, high-quality
catalogue with a stated completeness magnitude** at the small end: the forecast
counts above a modest magnitude, which are the leading indicators, are only
usable if the network truly detects and locates them. Without that, the protocol
is triggered by the largest events only — which is exactly the tail it is trying
to avoid.

---

## Worked mastery checkpoint

**(a) Heat in place and recoverable heat.**

$$ V = 10\times10^{6}\ \mathrm{m^{2}} \times 800\ \mathrm{m}
= 8.0\times10^{9}\ \mathrm{m^{3}}, $$
$$ H = (2.5\times10^{6})(8.0\times10^{9})(120) = 2.4\times10^{18}\ \mathrm{J}
= 2.4\ \mathrm{EJ}, $$
$$ H_{\text{rec}} = 0.08(2.4) = 0.192\ \mathrm{EJ}. $$

**(b) Wells needed.**

$$ P_{\text{well}} = \frac{(40)(4200)(90)(0.10)}{10^{6}} = 1.512\ \mathrm{MWe}, $$
$$ N = \frac{25}{1.512} = 16.5 \approx 17\ \text{wells}. $$

**(c) MT posterior.**

$$ \mathrm{PPV} = \frac{0.2(0.8)}{0.2(0.8)+0.8(0.5)} = \frac{0.16}{0.56} = 0.286. $$

**(d) Expected large events.** With $b = 1$ and $N = 5000$ events above
$M = 0$:

$$ P(M \ge 2 \mid M \ge 0) = 10^{-2} = 0.01
\;\Longrightarrow\; 5000(0.01) = 50\ \text{events}. $$

Fifty $M \ge 2$ events are expected in the sequence. A traffic-light level at
$M = 2$ would therefore be exceeded routinely, which makes it useless as a
decision trigger unless it is expressed as a *rate* or as a larger single-event
threshold; the expected count is what turns a threshold into a protocol.
