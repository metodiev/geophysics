# Solutions — 14-06-03 Water Resource Assessment and Sustainable Yield

> **Read after attempting the exercises.** Numbers were computed, not estimated.

Lesson: [03 Water Resource Assessment](../03-water-resource-assessment.md).

---

## ★1 — Recharge from a rise

$$R = S_y\Delta h = 0.10 \times 0.85 = 0.085\ \mathrm{m}
= 85\ \mathrm{mm\,a^{-1}},
\qquad
R = 0.15 \times 0.85 = 127.5\ \mathrm{mm\,a^{-1}}.$$

Ratio $= 1.50$, the ratio of the specific yields. The lesson's demonstration gives
85.1 mm/a for the first case (its measured rise is 0.8514 m, not 0.85 m); the
0.1% difference is the point of reporting the rise you actually used.

---

## ★2 — Chloride mass balance

$$R = P\frac{\mathrm{Cl}_{\text{dep}}}{\mathrm{Cl}_{\text{gw}}}
= 800 \times \frac{0.5}{12.0} = 33.3\ \mathrm{mm\,a^{-1}},$$

and with $\mathrm{Cl}_{\text{gw}} = 8.0$ mg/L:

$$R = 800 \times \frac{0.5}{8.0} = 50.0\ \mathrm{mm\,a^{-1}}.$$

The relation is inverse: a *lower* groundwater chloride implies *more* recharge
(more water diluting the same chloride input). This is also the direction in
which the method fails silently: an aquifer with a chloride source (halite,
fertiliser, road salt, seawater) shows a high $\mathrm{Cl}_{\text{gw}}$ and the
method reports a recharge that is too low — which is the direction the
demonstration's disagreement takes.

---

## ★3 — Stream depletion at 20 years

$$L\sqrt{\frac{S}{4Tt}} = 1500\sqrt{\frac{0.10}{4 \times 200 \times 7300}}
= 1500\sqrt{1.71233\times10^{-8}} = 1500 \times 1.30856\times10^{-4}
= 0.19628,$$

$$\frac{Q_{\text{stream}}}{Q} = \operatorname{erfc}(0.19628) = 0.7813,$$

so **78.1%** of the pumpage is captured from the stream at 20 years and 21.9%
comes from storage (with the remainder of the aquifer's other boundaries, which
this two-boundary idealisation ignores).

---

## ★4 — Depletion, storage and cumulative volume at $Q = 800\ \mathrm{m^3\,d^{-1}}$

At 5 years the fraction is $\operatorname{erfc}(\cdot) = 0.5788$ (the lesson's
table). Then

$$Q_{\text{stream}} = 0.5788 \times 800 = 463.0\ \mathrm{m^3\,d^{-1}},
\qquad
Q_{\text{storage}} = 800 - 463.0 = 337.0\ \mathrm{m^3\,d^{-1}}.$$

The cumulative volume captured over the five years scales linearly with $Q$:

$$V = 688872 \times \frac{800}{1000} = 551098\ \mathrm{m^3} \approx
5.51\times10^{5}\ \mathrm{m^3}.$$

(The scaling is exact because the *fraction* depends only on $T$, $S$, $L$ and
$t$, not on $Q$; the volume is the fraction integrated and then multiplied by
$Q$.) As a check, the mean captured rate over the period is
$551098/(5\times365) = 302.0\ \mathrm{m^3\,d^{-1}} = 0.378Q$, consistent with a
fraction that rises from 0.2145 at one year to 0.5788 at five.

---

## ★5 — Uncertainty in the time to 10% depletion

$$t_{10} = \frac{L^2S}{4T\alpha^2} = \frac{(1500)^2(0.10)}{4T(1.1631)^2}
= \frac{2.25\times10^5}{5.4112\,T} = \frac{41571}{T}\ \mathrm{d}.$$

- $T = 100\ \mathrm{m^2\,d^{-1}}$: $t_{10} = 415.7$ d $= 1.14$ yr.
- $T = 200$: $t_{10} = 207.9$ d $= 0.57$ yr (the lesson's value).
- $T = 400$: $t_{10} = 103.9$ d $= 0.28$ yr.

**Implication.** A licence written on the median ($0.57$ yr) is wrong by a factor
of two in either direction, and the direction matters for the regulator: a *low*
$T$ (a tight aquifer) means the stream is affected *later*, so the licence
condition is met for longer than expected; a *high* $T$ means the impact arrives
in a quarter of a year and the licensed rate may already have breached the
tolerance before the first monitoring campaign reports. The asymmetry of the
consequence — not of the distribution — is the reason a factor-of-two parameter
uncertainty cannot be handled by quoting a central value.

---

## ★6 — Permitted pumping at three depletion fractions

$$Q_{\text{perm}} = 0.10 \times 4320 = 432\ \mathrm{m^3\,d^{-1}},
\qquad Q \le \frac{Q_{\text{perm}}}{\operatorname{erfc}(\cdot)}.$$

- Nominal fraction 0.5788: $Q \le 432/0.5788 = 746\ \mathrm{m^3\,d^{-1}}$.
- Optimistic fraction 0.384: $Q \le 432/0.384 = 1125\ \mathrm{m^3\,d^{-1}}$.
- Pessimistic fraction 0.803: $Q \le 432/0.803 = 538\ \mathrm{m^3\,d^{-1}}$.

(These match the demonstration's Monte Carlo 5–95% range of 538 to 1125 m³/d.)

**Decision consequence.** A licence at the nominal 746 m³/d has roughly a 15–25%
chance of exceeding the agreed stream-depletion tolerance at the five-year
horizon (whatever quantile of the parameter distribution you attach to the
nominal figure, the range spans it). The defensible answers are therefore: license
the **lower bound of the plausible range** (538 m³/d) if the tolerance is
binding and the cost of breach is high; license the nominal figure with an
**adaptive condition** (a trigger requiring a rate reduction if the monitored
depletion exceeds the tolerance); or license the upper figure only with a
demonstrated measurement of $T$ and $S$ at that site — which is what a pump test
buys.

---

## ★7 — Monitoring for a licence breach within a year (specification)

**What must be detected.** Depletion of the stream attributable to the well,
against a *tolerance* of 432 m³/d at five years — but the requirement is to detect
a breach *within one year*, by which time the expected depletion is
$0.2145 \times Q$. At the licensed rate of 746 m³/d that is
$160\ \mathrm{m^3\,d^{-1}}$, i.e. **37% of the tolerance**.

**Instruments.**

1. A **rated stream gauge** at the affected reach, with a stage–discharge rating
   measured (not extrapolated) over the relevant flow range, and a second gauge
   above the well's cone of influence to difference against. Required precision:
   the difference of two gauges must resolve 160 m³/d on a low flow of
   4320 m³/d, i.e. **3.7% on each**, which is achievable for a rated weir and
   marginal for a natural section.
2. **Observation piezometers** between the well and the stream, with a logger at
   15-minute resolution, to measure the head gradient — this is the measurement
   that is *attributable* to the well (a streamflow change can have other
   causes).
3. **Pumping records** at the well, with the cumulative volume (a licence is
   usually written on volume, not rate).

**Frequency.** Continuous stage and head; a monthly discharge measurement to
maintain the rating; a pumping record daily.

**Statistic and compliance test.** A **paired, flow-adjusted difference** between
the two gauges: regress the below-well discharge against the above-well discharge
over a *baseline* period (before pumping, or over periods with the pump off), then
test whether the residual during pumping exceeds zero by more than its 95%
prediction interval. This removes the weather signal, which is much larger than
the abstraction signal.

**Error characteristics to accept.** A false-alarm rate of 5% (the standard
consequence of using a 95% interval, applied to *monthly* aggregates rather than
to instantaneous readings), and a detection probability above 80% for a depletion
equal to the tolerance. The second requirement is what forces the precision
calculation above; a system that can only detect a breach at 100% of the
tolerance is not a monitoring programme, it is a post-mortem.

**Precision needed, quantified.** To resolve 160 m³/d on 4320 m³/d with a 95%
test, the standard error of the flow-adjusted difference must be below about
$160/1.96 = 82\ \mathrm{m^3\,d^{-1}}$, i.e. **1.9% of the low flow**. That is a
demanding requirement for a natural stream and the reason the observation wells
(nominally 1 mm of head ≈ a few m³/d of flux) are the primary instrument, with
the stream gauges providing the corroborating evidence.

---

## ★8 — Sustainable yield at a hearing (model answer)

> "There is no single number, and I would be misleading you if I gave you one.
> Here are the numbers I can defend, and what each depends on.
>
> **The water that arrives** is a recharge of about 85–90 mm/a over the
> 20 km² assessment area, from a water-table fluctuation analysis (which requires
> a specific yield of 0.10 and a rise window I will give you), and about 33 mm/a
> from a chloride mass balance (which requires the chloride in deposition and in
> recharge, both of which I have assumed and both of which I would measure before
> relying on them). Averaged over the area, that is of order 4700 m³/d. That
> number answers 'how much water arrives?' — not 'how much can be taken?'
>
> **The change caused by pumping** is a stream depletion that grows with time: at
> a well 1.5 km from the stream, in an aquifer with $T = 200\
> \mathrm{m^2\,d^{-1}}$ and $S = 0.10$, the fraction of each cubic metre pumped
> that comes from the stream rises from about 21% at one year to 58% at five and
> 78% at twenty. If your tolerance is 10% of a low-flow discharge of
> 4320 m³/d — and that tolerance, that low-flow figure and the five-year horizon
> are *your* decisions, not mine — then the permitted rate is 746 m³/d.
>
> **How well do I know that?** The parameters are uncertain, and propagating them
> gives a 5–95% range of 538 to 1125 m³/d. If we license 746 m³/d, the chance of
> exceeding the tolerance within five years is of order 15–25%. If the tolerance is
> a hard legal limit, I recommend licensing 538 m³/d, or licensing 746 m³/d with a
> condition that the rate be reduced if the monitoring shows the tolerance being
> approached.
>
> **What would improve the number?** A multi-day pump test for $T$ and $S$ at this
> site — which is the single measurement that converts the range above into a
> point — and two years of baseline streamflow and head data to establish what
> 'no impact' looks like."

**Why it contains more than one number and at least one probability.** The first
number (recharge) is a *budget*; the second (capture-limited rate) is a
*consequence at a chosen tolerance and horizon*; and the probability is the only
honest way to combine an uncertain parameter set with a decision threshold.
Giving one number would imply that the tolerance, the horizon and the parameters
are all known — three claims the assessment cannot support.
