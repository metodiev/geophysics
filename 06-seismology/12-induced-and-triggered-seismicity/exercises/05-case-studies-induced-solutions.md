# Solutions — 06-12-05 Documented Case Studies: Basel, Oklahoma, Groningen, Pohang

> **Read after attempting the exercises.** Numbers were computed; demonstration
> values are quoted directly. All populations are MODEL constructions.

Lesson: [05 Case Studies: Basel, Oklahoma, Groningen, Pohang](../05-case-studies-induced.md).

---

## ★1 — Coincidence probability

16 months $= 16 \times 30.44 \approx 487$ days (the demonstration's stated
window). A 20-year catalogue is $20 \times 365 = 7300$ days. For a swarm whose
time is uniform and independent of the operations,

$$P(\text{inside the window}) = \frac{487}{7300} = 0.06671 ,$$

which is the demonstration's $0.0667$.

**Assumption.** The swarm time is uniform over the catalogue and *independent of
the operations*. That is exactly the null hypothesis being tested — so the
arithmetic cannot be used to argue that a coincidence is surprising. It computes
how often coincidence happens *by construction* when there is no causal link at
all.

---

## ★2 — Interpreting AUC

AUC is the probability that a randomly chosen positive scores higher than a
randomly chosen negative. **AUC $= 0.5$ means the statistic carries no
information** about the label; AUC $= 1.0$ means perfect separation.

- **$0.965$ against ordinary natural swarms.** The ordinary swarms were generated
  away from the well, so "median distance from the well" separates them almost
  perfectly. That is a property of the *models*, and it is the trap: the statistic
  looks excellent because the null hypothesis was made easy.
- **$0.745$ against adversarial swarms.** Once the natural swarms are sited at the
  well, the AUC collapses toward 0.5 (the demonstration measures $0.496$ for the
  depth statistic — literally no information). The honest reading of a
  single working statistic is therefore its AUC against the *hardest* plausible
  null, not the easiest.

---

## ★3 — $b$-value difference

$$b_{\text{ind}} - b_{\text{nat}} = 0.873 - 0.899 = -0.026 .$$

Combined standard error, assuming independence:

$$\sigma = \sqrt{0.044^2 + 0.045^2} = \sqrt{0.001936 + 0.002025}
= \sqrt{0.003961} = 0.0629 .$$

$$z = \frac{-0.026}{0.0629} = -0.41 .$$

$|z| \ll 2$, so the two $b$-values are **not distinguishable**: the difference is
$0.4\sigma$. The demonstration's AUC for the $b$-value statistic ($0.479$ against
ordinary swarms, $0.465$ against adversarial) confirms it — below 0.5, i.e. no
information. A $b$-value difference of this size is exactly the kind of
non-result that gets reported as a trend when the standard error is not printed.

---

## ★★4 — Rule A and Rule B

| rule | induced called induced | adversarial natural called induced |
|---|---|---|
| A (distance + depth) | $600/600 = 1.000$ | $600/600 = 1.000$ |
| B (A + time correlation) | $600/600 = 1.000$ | $50/600 = 0.0833$ |

Rule A has a **100% false-positive rate** on adversarial natural swarms: it calls
every one of them induced. Since it also calls every induced sequence induced, its
apparent accuracy is $0.5$ — it is separating nothing and is equivalent to
answering "induced" to every question.

Rule B's false-positive rate is $8.3\%$, and it retains $100\%$ true positives. All
of the discriminating power therefore sits in the **last clause**, the time
correlation. That clause is a coincidence test, and ★1/★★5 price the coincidence:
it works here only because the adversarial population was constructed to sit
inside the window but *not* to track the injection rate month by month.

---

## ★★5 — Coincidence with several windows

$$P(\text{at least one}) = 1 - (1 - p)^{m}, \qquad p = 0.06671 .$$

| $m$ (windows) | $1-(0.93329)^{m}$ | demonstration |
|---|---|---|
| 1 | $0.06671$ | $0.0667$ |
| 5 | $0.29193$ | $0.2918$ |
| 10 | $0.49854$ | $0.4984$ |
| 30 | $0.87392$ | $0.8738$ |

All four agree to within $1\times10^{-4}$, the difference being the demonstration's
rounded per-window probability.

The conclusion is the one that matters for a mature basin: with tens of operations
windows, a coincidence between a natural swarm and somebody's injection is
**expected**, not surprising. Testing the coincidence without correcting for the
number of windows is a multiple-comparisons error with a known size.

---

## ★★6 — Three different rates

- Nominal rate of the 5% time test: $0.05$.
- Measured rate on 1500 random natural swarms: $0.0047$ — the test is
  **conservative** in this configuration (a Pearson correlation $p$-value on 24
  mostly-zero monthly counts is not uniformly distributed, so fewer than 5% of
  null swarms reach $p<0.05$).
- Observed rate on the 600 adversarial swarms under Rule B: $50/600 = 0.0833$.

If the time clause carried the nominal rate alone, the expected misclassifications
would be $600 \times 0.05 = 30$; with the *measured* rate it would be
$600 \times 0.0047 = 2.8$. The observed $50$ is **larger than both**, which is the
quantitative statement that the adversarial population is not a random sample:
it was constructed to lie inside the operations window, so the last clause has more
to work with than a random swarm would.

**Which number is a property of the population construction:** the $8.3\%$. It is
a *worst case built by construction*, not a rate to be expected in nature. What the
measurement does establish is that the widely used spatial-plus-depth rule (Rule A)
has zero discriminating power against a swarm sited in the reservoir, and that all
of the burden falls on a test whose per-window false-positive probability is a few
per cent while the number of windows is large.

---

## ★★★7 — A posterior instead of a verdict (specification)

**Quantity.** $P(\text{induced} \mid \text{statistics})$ via Bayes:

$$P(\text{ind} \mid \mathbf s) = \frac{P(\mathbf s \mid \text{ind})\,\pi_{\text{ind}}}
{P(\mathbf s \mid \text{ind})\,\pi_{\text{ind}} + P(\mathbf s \mid \text{nat})\,\pi_{\text{nat}}}.$$

**Prior $\pi$.** Must be stated and defended: the base rate of induced versus
natural swarms of a given size in the region, from a regional catalogue over a
long period *excluding* operations windows. This is the item that most changes the
answer and is usually left implicit.

**Likelihoods.** For each statistic, build the distribution under each hypothesis
from the *hardest plausible* null — i.e. adversarial swarms, not ordinary ones.
For the median distance and depth statistics these can be computed directly from
the geometry; for $b$ the demonstration shows the two distributions overlap almost
completely (AUC $\approx 0.48$), so that statistic contributes a likelihood ratio
near 1 and should be dropped rather than given a spurious weight. The time
correlation requires a model of the swarm's own temporal clustering.

**The missing item.** A **detection and location-error model** — in particular the
depth uncertainty. The demonstration's depth statistic achieves $1.000$ AUC against
ordinary swarms and $0.496$ against adversarial ones, and the transition depends
entirely on how reliably "at reservoir depth" can be asserted for individual
events. Without a location-error model, the depth likelihood is not computable, and
the posterior inherits an unquantified bias.

---

## ★★★8 — Is the adversarial null a strawman?

**A strawman argument would be:** "no natural swarm can be at the well, at
reservoir depth, inside the window, so the adversarial case is irrelevant."

**The physics that makes it realistic.**

1. **Fluid pathways and faults do not respect the well's location.** A natural
   swarm on a pre-existing fault that happens to pass near an injection well is
   plausible; that is the setting in which the inference is genuinely hard, and it
   is exactly the setting in which regulators have to decide.
2. **Reservoir depths are also common crustal depths.** Depths of $2$–$4\
   \mathrm{km}$ are ordinary for crustal seismicity in many regions, so "at
   reservoir depth" is not a rare coincidence.
3. **Long operations windows.** Once a basin has tens of windows (★★5: 50%
   chance of at least one coincidence for 10 windows), the time coincidence is
   expected.

**Where it is not realistic.** A swarm *simultaneously* at the well, at reservoir
depth, inside the window *and* with a rate that tracks the injection month by
month is genuinely unlikely to be natural: the month-by-month correlation is the
part that the adversarial construction does **not** reproduce (its rate-vs-injection
Pearson $r = 0.195$, $p = 0.36$, versus $r = 0.948$, $p = 2\times10^{-12}$ for the
induced population).

**How the choice changes the conclusion.** Using ordinary natural swarms gives
AUCs of $0.96$–$1.00$ and supports the comfortable conclusion that the statistics
work; using adversarial swarms gives AUCs of $0.47$–$0.75$ and supports the honest
conclusion that location and depth carry no information at all. The correct
practice is to report both, because the truth for a given case lies somewhere
between and the *only* evidence that moves it is the temporal tracking.

---

## ★★★9 — Ranking by how much evidence each statistic needs

Use the adversarial AUCs as the measure of current information and ask what a
statistic would need to become decisive (AUC $> 0.9$):

| statistic | adversarial AUC | needed change | verdict |
|---|---|---|---|
| time correlation with injection | $1.000$ | none | already decisive |
| median distance from the well | $0.745$ | large: AUC must rise by $0.155$ | needs a *prior* constraint on permissible fault geometries near the well |
| depth KS against regional | $0.496$ | essentially total: no information | needs a location-error model and a regional depth distribution, i.e. a different measurement, not more events |
| $b$-value versus regional $b$ | $0.465$ | no information, and below chance | should be dropped from the rule |

**Ranking (most to least valuable additional observation):**

1. **Continuous injection-rate and pressure time series at the well**, because it
   is the input to the only statistic that already separates the populations
   (targeted discrimination at AUC $1.000$); its value is not to improve that
   statistic but to make it possible to argue that the temporal tracking is not
   itself a coincidence with some unobserved operational variable.
2. **A location-error model** (temporary array or network upgrade), which converts
   the depth statistic from $0.496$ into something usable; without it the depth
   claim is unfalsifiable.
3. **Regional structural mapping of faults near the well**, which constrains
   $\pi_{\text{ind}}$ through the geometry, i.e. attacks the prior rather than the
   likelihood. This is the item regulators most often omit.
4. **More events** — least valuable, because every statistic here is already
   computed on samples of hundreds and the limitations are systematic (★★8), not
   statistical. This is the same conclusion as in
   [02 Pore-Pressure Triggering](../02-pore-pressure-triggering.md), where random
   location error shrank with catalogue size but systematic velocity bias did not.
