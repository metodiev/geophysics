# Solutions — 11-07-04 Case Study: Arid-Region Groundwater Exploration

> **Read after attempting the exercises.** Numbers were computed, not estimated by
> hand. All values are **SYNTHETIC** argument archetypes; no site-specific number
> is quoted anywhere in this lesson.

Lesson: [04 Case Study: Arid-Region Groundwater Exploration](../04-case-study-groundwater.md).

---

## ★1 — Posterior given an AEM anomaly

$$ \mathrm{PPV} = \frac{p\,\mathrm{TPR}}{p\,\mathrm{TPR}+(1-p)\,\mathrm{FPR}}
= \frac{0.10(0.65)}{0.10(0.65)+0.90(0.20)}
= \frac{0.065}{0.245} = 0.265. $$

---

## ★2 — Holes per productive well

$$ \frac{1}{\mathrm{PPV}} = \frac{1}{0.265} = 3.77, \qquad
\text{dry fraction} = 1 - 0.265 = 0.735. $$

About four holes per productive well, with nearly three quarters dry. This is the
number to put in the programme's budget, and it is the number a survey report
usually omits.

---

## ★3 — Annual recharge

$$ \text{recharge} = 0.15\ \mathrm{m} \times 0.04 \times 8\times10^{8}\ \mathrm{m^{2}}
= 4.8\times10^{6}\ \mathrm{m^{3}\,yr^{-1}}. $$

Both factors — the rainfall and the recharge coefficient — are hydrological
estimates, not geophysical measurements.

---

## ★4 — Staged selection counts

$$ P(\text{AEM anomaly}) = p\,\mathrm{TPR} + (1-p)\mathrm{FPR}
= 0.10(0.65)+0.90(0.20) = 0.245, $$

$$ \text{AEM anomalies} = 200 \times 0.245 = 49\ \text{sites}. $$

Assuming conditional independence, the joint flag probability is

$$ P(\text{both}) = p\,\mathrm{TPR}_1\mathrm{TPR}_2
+ (1-p)\mathrm{FPR}_1\mathrm{FPR}_2
= 0.10(0.65)(0.85) + 0.90(0.20)(0.10) = 0.05525 + 0.018 = 0.07325, $$

$$ \text{retained by TDEM} = 200 \times 0.07325 = 14.65\ \text{sites}. $$

---

## ★5 — Net value of the three strategies

| Strategy | Productive wells found | Programme cost | Net value (at $80$/well) |
|---|---|---|---|
| Drill all 200 | $200(0.10) = 20.0$ | $200(10) = 2000.0$ | $1600 - 2000 = -400.0$ |
| AEM then drill | $200(0.10)(0.65) = 13.0$ | $10 + 49(10) = 500.0$ | $1040 - 500 = +540.0$ |
| AEM + TDEM then drill | $200(0.10)(0.65)(0.85) = 11.05$ | $10 + 24.5 + 146.5 = 181.0$ | $884 - 181 = +703.0$ |

**Recommendation: AEM + TDEM then drill.** It finds the fewest productive wells
and creates the most value, because the expensive drilling is concentrated on the
smallest, best-selected set. Blind drilling finds the most water and loses
money — the clearest possible demonstration that "wells found" is not the
objective function.

The recommendation is conditional on the cost and value inputs: if a productive
well were worth only $20$ instead of $80$, the AEM-only strategy would be
preferred (the TDEM stage's $15.1$ units of extra cost would not be repaid).
**State the inputs with the recommendation.**

---

## ★6 — Sustainable well count and depletion time

$$ N = \frac{4.8\times10^{6}}{0.4\times10^{6}} = 12\ \text{wells at steady state}. $$

With 20 wells:

$$ \text{abstraction} = 20(0.4\times10^{6}) = 8.0\times10^{6}\
\mathrm{m^{3}\,yr^{-1}}, $$
$$ t = \frac{200\times10^{6}}{8.0\times10^{6} - 4.8\times10^{6}} = 62.5\ \text{years}. $$

Sixty-two years sounds long, and it is the product of two uncertain estimates (a
storage volume and a recharge rate). The honest statement is the **range**, not
the 62.5: at half the storage it is
$100/(8.0-4.8) = 31.3$ years; at half the recharge it is
$200/(8.0-2.4) = 35.7$ years; at both it is
$100/(8.0-2.4) = 17.9$ years. Each of those is a plausible hydrological
assessment, and none of them is a geophysical result.

---

## ★7 — Exploration recommendation (specification)

**Target.** A productive borehole in an arid region: sufficient saturated
thickness, adequate water quality (a stated salinity threshold), and a sustainable
abstraction rate.

**Two-stage survey.** (i) Regional airborne EM over the whole block to map
conductance and to rank sub-blocks; (ii) ground TDEM or ERT over the top-ranked
anomalies to resolve layered conductance and to place holes. Supplement with
gravity for basin geometry and with refraction or MASW for the water table where
saturation changes $v_p$ appreciably.

**The prior, and how to establish it.** The base rate is the fraction of *past*
boreholes in the same geological setting that met the productivity and quality
threshold. Establish it from the regional borehole register, not from the
literature of another region, and quote the threshold and the record's time span.
If no register exists, say that the prior is elicited and treat the posterior as
an expert judgement until the first few holes give a measured rate.

**Decision rule, stated in advance.** Rank anomalies by conductance and structural
position; drill in descending order until the marginal expected value (using the
posterior and the cost/value ratio) falls below zero; report the expected dry-hole
rate and the number of holes implied.

**Sustainability caveat.** Recharge, storage and the regional water balance are
outside the survey. State the estimated recharge with its range, and the
abstraction it supports, in the same report. A survey that says "there is water"
without that statement is incomplete, and in an arid region it is misleading.

---

## ★8 — When the two stages are not independent

**The situation.** Both AEM and TDEM respond to bulk conductivity, which is
raised by **clay** as well as by water. In a region with a widespread conductive
clay-rich unit (a palaeosol, a weathered horizon, or a lacustrine clay), many
sites are flagged by *both* methods for the same geological reason: **the shared
false-positive cause**. That is positive conditional dependence on the dry
branch of the likelihood.

**The consequence.** The staged strategy's specificity is overstated. The
number of retained sites is larger than the independent calculation predicts,
because the dry sites that are flagged by AEM are much more likely to be flagged
by TDEM than the independence assumption implies. With more dry sites drilled,
the cost per productive well rises toward — and in the limit can exceed — the
single-stage value, and the recommendation of ★5 can reverse.

**The calculation to make.** Rather than the product of the two FPRs, use the
conditional value $P(\text{TDEM}+ \mid \text{AEM}+, \text{dry})$, which is the
number that should be measured — from sites where both were flagged and a hole
later showed no water. The whole staged calculation then becomes conditional on
the AEM result rather than assuming a shared FPR.

**Design change that restores some independence.** Add a method whose
false-positive population is *different*: gravity or microgravity for the
structural trap and for the saturated mass, or seismic refraction for the water
table where the $v_p$ contrast exists. Both respond to different physics
(density, elasticity) and therefore fail for different reasons, so their
combination discriminates the clay false positive from the water anomaly in a way
that two conductivity methods cannot.

---

## Worked mastery checkpoint

**(a) Posterior after the AEM stage.**

$$ \mathrm{PPV} = \frac{0.10(0.65)}{0.10(0.65)+0.90(0.20)}
= \frac{0.065}{0.245} = 0.265. $$

**(b) Anomaly counts.**

$$ P(\text{AEM}+) = 0.10(0.65)+0.90(0.20) = 0.245
\;\Longrightarrow\; 200(0.245) = 49\ \text{anomalies}, $$
$$ P(\text{both}) = 0.10(0.65)(0.85)+0.90(0.20)(0.10) = 0.07325
\;\Longrightarrow\; 200(0.07325) = 14.65\ \text{sites retained}. $$

**(c) Net value.** With a well cost of 10 and a productive well worth 80
(AEM cost $0.05$ per site, TDEM $0.5$ per site):

| Strategy | Productive wells | Cost | Net value |
|---|---|---|---|
| Drill all 200 | $200(0.10) = 20.0$ | $2000$ | $-400$ |
| AEM then drill anomalies | $200(0.10)(0.65) = 13.0$ | $10 + 490 = 500$ | $+540$ |
| AEM + TDEM then drill | $200(0.10)(0.65)(0.85) = 11.05$ | $10+24.5+146.5 = 181$ | $+703$ |

The staged strategy finds the fewest wells and creates the most value.

**(d) Recharge.**

$$ 0.15\ \mathrm{m} \times 0.04 \times 8\times10^{8}\ \mathrm{m^{2}}
= 4.8\times10^{6}\ \mathrm{m^{3}\,yr^{-1}}. $$

**None of it is a geophysical measurement.** The rainfall and the recharge
coefficient are hydrological estimates; the geophysics constrains the aquifer's
extent, its conductance and its structure, which is a different statement about a
different uncertainty.
