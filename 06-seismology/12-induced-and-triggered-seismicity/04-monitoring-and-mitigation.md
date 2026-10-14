---
id: 06-12-04
title: "Traffic-Light Protocols, Monitoring and Mitigation"
level: graduate
prereqs: ["06-12-01", "06-12-03"]
tags: [traffic-light, monitoring, mitigation, magnitude-completeness, decision-theory]
---

# Traffic-Light Protocols, Monitoring and Mitigation

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** the rate at which a stated magnitude threshold is exceeded from a
   Gutenberg–Richter model, and convert that into an expected number of
   operational stoppages per site and per basin.
2. **Derive** the probability that the largest event in a sequence of $N$ events
   exceeds a stated magnitude, and state why that probability cannot be made
   small by any choice of threshold.
3. **Compute** $\mathrm{E}[M_{\max}]$ correctly, including the
   Euler–Mascheroni term that the commonly quoted $\log_{10}N/b$ form omits.
4. **Explain** why the distribution of $M_{\max}$ does not narrow as the catalogue
   grows, and why this is the central obstacle to bounding induced event size.
5. **Design** a monitoring programme whose magnitude of completeness is stable
   through the sequence, and explain why a drifting $M_c$ mimics a rate change.
6. **Construct** and criticise a decision-theoretic cost model, and state why the
   resulting threshold is a policy choice rather than a physical limit.

## Prerequisites

- [06-12-01 Causes of Induced Seismicity](./01-induced-seismicity-causes.md)
  — the mechanisms a protocol is trying to manage.
- [06-12-03 Rate-and-State Friction and the Dieterich Seismicity Model](./03-rate-state-triggering.md)
  — the rate response that a rate-based criterion uses.
- [06-11-01 The Gutenberg–Richter Law](../11-earthquake-statistics-and-hazard/01-gutenberg-richter.md)
  — magnitude–frequency relations, $a$- and $b$-values, and $M_c$.

## 1. Intuition: a traffic light is a contract, not a discovery

A traffic-light protocol says: *if the ground shakes this hard, we do this.* It is
a contract between an operator, a regulator and a community. The magnitude
thresholds in it have the same logical status as a speed limit. They are chosen so
that the consequences — the number of stoppages, the probability of catching a
large event, the cost — are acceptable, and they can be argued about precisely
because their consequences can be computed.

This lesson computes those consequences. It also derives the single most
inconvenient fact in the subject: **the distribution of the largest event in a
sequence does not get narrower as the catalogue grows.** No protocol, and no
amount of monitoring, can convert a magnitude threshold into a guarantee.

## 2. Precise definitions

### 2.1 The exceedance rate

For magnitudes above a completeness magnitude $M_c$, the Gutenberg–Richter law
gives the number of events above $M$:

$$N(M) = N(M_c)\,10^{-b(M - M_c)}
\qquad\text{and hence}\qquad
\dot N(M) = \dot N(M_c)\,10^{-b(M-M_c)},$$

where $\dot N(M_c)$ is a rate (events per unit time) and $b$ is dimensionless.
The rate at or above a threshold $M_t$ is therefore

$$\lambda(M_t) = \dot N(M_c)\,10^{-b(M_t - M_c)}.$$

If events are Poisson in time, the probability of at least one exceedance in a
window $T$ is $1 - e^{-\lambda T}$.

### 2.2 The three lights

A typical design has three levels, and each level needs four things specified:

| Level | Criterion | Operational response | Why the response is the hard part |
|---|---|---|---|
| Green | below amber | normal operations | — |
| Amber | an event of magnitude $\ge M_a$, or a rate increase | reduce rate or volume; review | reducing rate is slow to change $\Delta p$; the pressure field has memory |
| Red | an event of magnitude $\ge M_r$ | stop; possibly bleed off | stopping removes the *source*, but the pressure change already in the rock diffuses onwards for months |

**The timescale mismatch is the central operational difficulty.** From
lesson [06-12-02](./02-pore-pressure-triggering.md), the pressure front moves as
$\sqrt{4Dx_ct}$, so a change made now affects the far field only later, and a
change made now does not undo the pressure already there.

### 2.3 Magnitude of completeness and why it must be watched

$M_c$ is the magnitude above which the catalogue is complete. It depends on the
station network, the noise level, the detection algorithm and the event rate
itself (small events get lost in the coda of larger ones). **A rising event rate
raises $M_c$**, which suppresses the apparent rate at low magnitudes and can
convert a real rate increase into an apparent decrease. Every rate-based criterion
is therefore only as good as its $M_c$ history.

## 3. Derivations

### 3.1 The exceedance arithmetic and the number of stoppages

With $\lambda(M_t)$ as in §2.1, the expected number of crossings at one site over
a programme of length $T$ is $\lambda(M_t)T$, and across $S$ sites it is
$S\,\lambda(M_t)T$. Both are **linear in $S$**, which is the fact that makes a
threshold administratively expensive in a mature basin: a threshold calibrated for
one well becomes $S$ times as many stoppages across a jurisdiction.

### 3.2 The distribution of the largest event

**Step 1 — the per-event exceedance probability.** For a GR population with
completeness $M_c$, the probability that a randomly chosen event exceeds $M_t$ is
the ratio of rates:

$$p_t = \frac{\dot N(M_t)}{\dot N(M_c)} = 10^{-b(M_t - M_c)}.$$

**Step 2 — independence.** If the $N$ events are independent,

$$P(M_{\max} > M_t) = 1 - (1 - p_t)^N
\qquad\Longrightarrow\qquad
P(M_{\max} \le M_t) = \left(1 - 10^{-b(M_t-M_c)}\right)^N .$$

**Step 3 — the number of events for a 50 % chance.** Setting the left side to
$1/2$,

$$N_{50} = \frac{\ln 2}{\ln\!\left[\left(1 - 10^{-b(M_t-M_c)}\right)^{-1}\right]}
\ \approx\ \frac{\ln 2}{10^{-b(M_t-M_c)}} = 0.693\times10^{b(M_t-M_c)},$$

because the logarithm in the denominator expands to $10^{-b(M_t-M_c)}$ for
$p_t = 10^{-b(M_t-M_c)} \ll 1$. The $N$ needed grows only as $10^{b\Delta
M}$ — a factor of ten per magnitude unit at $b = 1$.

**Step 4 — the expected maximum.** Order statistics of $N$ exponential variables
give, with $\sigma_M = 1/(b\ln 10)$ the magnitude scale,

$$\mathrm{E}[M_{\max}] = M_c + \sigma_M\left(H_N\right)
\ \approx\ M_c + \frac{\ln N + \gamma_E}{b\ln 10},
\qquad \gamma_E = 0.5772,$$

using $H_N \approx \ln N + \gamma_E$. The commonly quoted
$\mathrm{E}[M_{\max}] = M_c + \log_{10}N/b$ omits $\gamma_E$, which is
$\gamma_E/(b\ln 10) = 0.251$ magnitude units at $b = 1$. The demonstration
measures this offset directly.

**Step 5 — the spread.** The same order-statistic result gives a 5–95 % range for
$M_{\max}$ of

$$\Delta M_{5\text{–}95} = \sigma_M\ln\!\left(\frac{\ln 0.05}{\ln 0.95}\right)
= \frac{1}{b\ln 10}\ln\!\left(\frac{\ln 0.05}{\ln 0.95}\right) = 1.766\ \text{at } b=1,$$

**independent of $N$.** That is the punchline: more events move the *centre* of
the distribution by $\log_{10}N/b$ and leave the *width* unchanged.

### 3.3 Why no physical bound can be derived from the statistics

A statistical bound on $M_{\max}$ would need either (i) a physical mechanism that
stops rupture at a finite size, or (ii) a statistical convergence that the above
shows does not occur. Physical arguments exist — finite fault area, finite
available stress drop, finite energy — but they require knowing the fault
geometry and the stress state at depth, both of which are poorly constrained. The
honest statement is that **the largest possible induced event is a property of the
unknown fault population, not of the operation**, and that the available models do
not agree closely enough to bound it.

There is one structural physical constraint worth stating carefully, because it is
often overclaimed: a rupture cannot run past the end of a fault, so the largest
possible event *on a specific mapped fault of length $L$* is bounded by a
magnitude–area scaling. That is a bound on a *given fault*, not on the region, and
it says nothing about faults that have not been mapped.

### 3.4 A cost model, and what it shows

A protocol's threshold can be derived from a cost model if one is willing to state
the costs. A minimal version:

$$\text{cost}(M_t) = c_{\text{trip}}\,\lambda(M_t)
+ c_{\text{dmg}}\,\lambda(M_{\text{dmg}})\,
e^{-\lambda(M_t)W},$$

where $W$ is the *precursor-awareness window* — how long before a damaging event a
red alert would still be operationally useful. The first term grows as $M_t$
falls (more stoppages); the second grows as $M_t$ rises (less warning).

**Step 1 — differentiate.** With $\lambda$ the variable, $c_1 = c_{\text{trip}}$,
$c_2 = c_{\text{dmg}}\lambda(M_{\text{dmg}})$:

$$\frac{\mathrm{d}\,\text{cost}}{\mathrm{d}\lambda}
= c_1 - c_2 W e^{-\lambda W} = 0
\qquad\Longrightarrow\qquad
\lambda^* = \frac{1}{W}\ln\!\left(\frac{c_2 W}{c_1}\right).$$

**Step 2 — invert to a magnitude.**
$$M_t^* = M_c - \frac{1}{b}\log_{10}\!\left(\frac{\lambda^*}{\dot N(M_c)}\right).$$

**Step 3 — read the structure.** $M_t^*$ depends on the ratio of costs, the
awareness window and the seismicity rate — *not* on any rock property. That is the
formal statement of "the threshold is policy".

## 4. Physical interpretation

Three readings of the derivation:

1. **A protocol manages rate, not size.** What stopping injection does is remove
   the $\gamma$ factor in the Dieterich response and let the pressure field decay.
   It cannot change $b$ or the tail of the magnitude distribution.
2. **The monitoring problem is the $M_c$ problem.** With a well-designed local
   network, $M_c$ can be pushed low and held stable, which is what makes a rate
   criterion usable. With a sparse network, $M_c$ moves with the sequence and
   every rate statistic is contaminated.
3. **Amber is the interesting light.** Green and red are binary; amber is where
   the physics of §3.4 of lesson 2 (the pressure field's memory) meets the
   operational reality that a rate reduction takes months to matter.

## 5. Assumptions and their consequences

| Assumption | Consequence if violated |
|---|---|
| Gutenberg–Richter holds to arbitrarily large $M$ | Real finite catalogs show curvature; a physical maximum would steepen the tail and make large events less likely than the extrapolation |
| $b$ constant in time | A $b$-value change during a sequence changes every exceedance probability |
| Events independent | Aftershocks cluster, so the count over a window has over-dispersion; exceedance probabilities are underestimated |
| Poisson occurrence | Real sequences are clustered; a Poisson protocol under-reacts to bursts |
| $M_c$ constant and known | A drifting $M_c$ mimics a rate change, in either direction |
| Magnitude estimates unbiased | Network changes mid-sequence recalibrate magnitudes; a bias of 0.2 units shifts exceedance rates by a factor of 1.58 at $b=1$ |
| Costs stated and stable | They are political, not technical; they change between jurisdictions and over time |
| The damaging magnitude is known | It depends on exposed assets, not on seismology |

## 6. Units and dimensional analysis

| Quantity | Symbol | Dimension | Note |
|---|---|---|---|
| Magnitude | $M$ | 1 | Not a physical unit; logarithmic and conventional |
| $b$-value | $b$ | 1 | Per magnitude unit |
| Rate | $\dot N$ | events/time | Per year or per day — state which |
| Exceedance rate | $\lambda$ | 1/time | |
| Programme length | $T$ | time | |
| Number of sites | $S$ | 1 | |
| Magnitude scale | $\sigma_M$ | 1 | $\sigma_M = 1/(b\ln10)$ magnitude units per natural log |
| Critical stress, pressure | $\Delta CFS$, $\Delta p$ | Pa | Same dimension as each other |

**Dimensionless check.** $\lambda T$ must be dimensionless for $1-e^{-\lambda T}$ to
make sense; a rate per year multiplied by a window in days is wrong by 365. This
is the single most common arithmetic error in protocol calculations, and it
changes a probability from 0.9 to 0.3.

**Magnitude–rate consistency.** Because $10^{-b\Delta M}$ is a ratio,
$a$-values and $b$-values fitted over different magnitude windows are not
interchangeable unless the reference $M_c$ is carried with them.

## 7. Worked examples

### 7.1 How many stoppages?

**Problem.** A catalogue has $\dot N(M_c = 1.0) = 100$ events/yr and $b = 1.0$
(a SYNTHETIC pair, stated in the demonstration). A protocol sets red at
$M_t = 2.5$. How many red events per site per year, and per 20-site basin over
10 years?

**Step 1 — exceedance rate.**
$$\lambda = 100 \times 10^{-1.0\times(2.5-1.0)} = 100\times10^{-1.5}
= 100 \times 0.0316 = 3.16\ \text{events/yr}.$$

**Step 2 — recurrence.** $1/\lambda = 0.316$ yr $= 116$ days.

**Step 3 — basin total.** $3.16 \times 20 \times 10 =
\mathbf{632}$ stoppages. The demonstration prints 632.46, computed the same way.

The number to put in front of a regulator is 632, not 2.5.

### 7.2 The chance of an event one unit above the threshold

**Problem.** Same parameters, a sequence of 1000 events. What is the probability
of at least one event of $M \ge 3.5$?

**Step 1 — per-event probability.**
$$p = 10^{-b(3.5-M_c)} = 10^{-2.5} = 3.16\times10^{-3}.$$

**Step 2 — the sequence.**
$$P = 1 - (1-3.16\times10^{-3})^{1000} = 1 - e^{-3.19} = 0.958.$$

**Step 3 — interpretation.** The protocol does not exclude a larger event; it
does not even make one unlikely. It monitors one. The demonstration prints 0.958.

**Step 4 — the events needed for a 50 % chance.** $N_{50} = 0.693/3.16\times10^{-3}
= 219$. So with about 220 events of $M \ge 1$, the odds are even that at least one
of them is $M \ge 3.5$.

### 7.3 The distribution of the maximum, measured

The demonstration simulates 20 000 sequences at each of four catalogue sizes with
$b = 1.0$, $M_c = 1.0$:

| $N$ | $\mathrm{E}[M_{\max}]$ (corrected) | measured mean | measured median | 5 % | 95 % | 95–5 spread |
|---|---|---|---|---|---|---|
| 10 | 2.251 | 2.270 | 2.175 | 1.590 | 3.286 | 1.696 |
| 100 | 3.251 | 3.254 | 3.158 | 2.529 | 4.294 | 1.765 |
| 1000 | 4.251 | 4.249 | 4.164 | 3.524 | 5.295 | 1.771 |
| 10000 | 5.251 | 5.251 | 5.160 | 4.527 | 6.273 | 1.746 |

Read three things:

1. The corrected formula matches the measured mean to two decimals; the
   uncorrected $\log_{10}N/b$ would be low by 0.25 in every row.
2. The **spread is constant** at 1.70–1.77, converging to the Gumbel value 1.766.
3. A hundredfold increase in catalogue size moves the expected maximum by one
   magnitude unit and does not narrow the distribution **at all**.

This is the quantitative reason no monitoring programme can bound induced event
size.

### 7.4 The threshold that a cost model produces

With the demonstration's toy cost model, $W = 0.05$ yr and a damaging magnitude of
4.0 ($\lambda_{\text{dmg}} = 0.100$/yr — all SYNTHETIC):

| $c_{\text{trip}}$ | $c_{\text{dmg}}$ | optimal $M_t$ | interior optimum? |
|---|---|---|---|
| 1.0e6 | 1.0e9 | 1.49 | yes |
| 1.0e6 | 1.0e10 | 1.11 | yes |
| 1.0e7 | 1.0e9 | 5.00 (boundary) | no — model says never bother stopping |
| 1.0e5 | 1.0e10 | 1.00 (boundary) | no |
| 1.0e6 | 1.0e8 | 5.00 (boundary) | no |

A tenfold change in the cost ratio moves the optimal threshold by nearly half a
magnitude unit, and in three of five cases removes the rationale for a threshold
at all. **The calculation is a toy, and it is stated as one so that it can be
argued with; its point is the structure, not the numbers.** Note that the
analytically derived $\lambda^*$ from §3.4 reproduces the grid-search optimum:
$32.19$ per year gives $M_t^* = 1.49$ for the first row.

## 8. Python demonstration

`code/traffic_light_demo.py`:

1. tabulates the exceedance rate, mean recurrence and probabilities for a range
   of thresholds;
2. computes expected crossings per site and per basin;
3. simulates the distribution of $M_{\max}$ and reports mean, median and the
   5–95 spread;
4. tabulates $P(M_{\max} > M_t)$ and the $N_{50}$ values;
5. solves the toy cost model by grid search and analytically, and compares them.

Exercises against the output: set `B_VALUE = 0.8` and predict whether the number
of stoppages at $M_t = 2.5$ rises or falls; set `N_SITES = 200` and check the
linearity claim of §3.1.

## 9. Exercises

### ★ Foundational

**★1.** With $\dot N(M_c = 0) = 1000$/yr and $b = 1$, compute the rate at or above
$M = 1, 2, 3$ and the mean recurrence of each.

**★2.** Compute $p_t = 10^{-b(M_t-M_c)}$ for $b = 1$, $M_c = 0.5$, $M_t = 2.5$.
Then compute $P(M_{\max} > 2.5)$ for $N = 100$ and $N = 1000$.

**★3.** State the dimensions of $\lambda$, $T$, $b$ and $\sigma_M$, and verify
that $\sigma_M = 1/(b\ln 10)$ has magnitude units.

### ★★ Applied

**★★4.** A protocol triggers red on any event of $M \ge 2.0$. With
$\dot N(M_c=1) = 30$/yr and $b = 1.1$, compute the expected number of red events
per year, and the probability of at least one red event in the first month of
operations.

**★★5.** Using §3.2, compute the $\Delta M$ over which $N_{50}$ grows by a factor
of 100 for $b = 1.0$ and for $b = 0.8$. Comment on why a lower $b$ is more
dangerous for the same rate.

**★★6.** A network upgrade lowers $M_c$ from 1.5 to 0.5 mid-sequence. Explain,
with a numerical example using $b = 1$, how this appears in a rate plot and why a
naive rate criterion would fire.

**★★7.** Using the demonstration's $\mathrm{E}[M_{\max}]$ table, estimate the
number of events needed to make the median $M_{\max}$ exactly 4.0 for $b = 1$,
and state the 5–95 range you would expect at that catalogue size.

### ★★★ Research

**★★★8.** Derive $P(M_{\max} > M_t)$ allowing for magnitude uncertainty: suppose
each reported magnitude has Gaussian error $\sigma_M = 0.2$. Show how the
exceedance probability changes for a threshold $M_t = 3.0$ and comment on the
direction of the bias.

**★★★9.** Replace the Poisson assumption with an ETAS cluster model and show that
the variance of the count over a fixed window exceeds the mean. Derive the
over-dispersion factor for a branching ratio $n$ and state the consequence for a
protocol that assumes Poisson statistics.

**★★★10.** Argue, with an explicit magnitude–area relation and a stated fault
geometry, that a mapped fault of length $L$ bounds the event size on *that* fault.
Then construct the case for and against using that bound in a regulatory setting,
and identify the single measurement that would most reduce the uncertainty.

## 10. Common mistakes

1. **Mixing rate units.** A rate per year times a window in days is wrong by 365.
2. **Quoting thresholds as if they were physical constants.** They are the output
   of a cost model.
3. **Claiming a maximum magnitude from statistics.** The 5–95 spread of
   $M_{\max}$ is constant at about 1.77 magnitude units regardless of $N$.
4. **Using $\mathrm{E}[M_{\max}] = M_c + \log_{10}N/b$.** It omits
   $\gamma_E/(b\ln10) = 0.251$ at $b = 1$.
5. **Ignoring the $M_c$ history.** A drifting $M_c$ mimics a rate change.
6. **Assuming Poisson statistics for clustered sequences.** Aftershocks make the
   counts over-dispersed and the exceedance probabilities optimistic.
7. **Extrapolating a GR fit far beyond the observed magnitude range.** The tail is
   the least constrained part of the fit.
8. **Assuming that stopping injection stops the seismicity.** The pressure change
   already in the rock keeps diffusing.
9. **Conflating magnitude with consequence.** Damage depends on ground motion,
   depth and exposure, not on $M$ alone.
10. **Treating a red light as evidence that an event was induced.** It is a
    response rule, not an attribution.

## 11. Real-world applications

- **Regulatory design.** The exceedance arithmetic is what turns a proposed
  threshold into a number of stoppages per year for a jurisdiction to consider.
- **Operator planning.** Amber levels are set to give enough warning time that the
  action can be completed before the pressure field has moved further.
- **Induced-seismicity hazard assessment.** Combining the rate model of lesson 3
  with the ground-motion models of
  [06-11-05](../11-earthquake-statistics-and-hazard/05-ground-motion-models.md).
- **Monitoring network design.** Array geometry and detection thresholds are
  chosen to hold $M_c$ low and stable; distributed acoustic sensing
  ([06-13-04](../13-planetary-and-exploration-seismology/04-distributed-acoustic-sensing.md))
  is one way to raise the density of channels cheaply.
- **Communication.** Reporting an exceedance probability rather than a guarantee
  is the honest form of a public statement, and it is defensible.
- **Data services.** Real-time catalogue feeds used in monitoring come from the
  [USGS FDSN event service](https://earthquake.usgs.gov/fdsnws/event/1/query)
  and [ComCat](https://earthquake.usgs.gov/data/comcat/), with programmatic
  access via the
  [ObsPy FDSN client](https://docs.obspy.org/packages/autogen/obspy.clients.fdsn.client.Client.html).

## 12. Further reading

- **Utsu, T., Ogata, Y., & Matsu'ura, R. S. *The centenary of the Omori formula
  for a decay law of aftershock activity*, J. Phys. Earth (1995).** The statistical
  background to any rate criterion.
- **Woessner, J., & Wiemer, S. *Assessing the quality of earthquake catalogues:
  estimating the magnitude of completeness*, BSSA (2005).** The $M_c$ estimation
  problem, and why the $M_c$ history is a first-order issue.
- **Cornell, C. A. *Engineering seismic risk analysis*, BSSA (1968).** The
  probabilistic framework that the exceedance arithmetic of §3.1 is a special
  case of.
- **Bommer, J. J., Oates, S., Cepeda, J. M., Lindholm, C., Bird, J., Torres, R.,
  Marroquín, G., & Rivas, J. *Control of hazard due to seismicity induced by a hot
  fractured rock geothermal project*, Eng. Geol. (2006).** A protocol described
  in full, with its operational consequences.
- **Majer, E. L., et al. *Induced seismicity associated with enhanced geothermal
  systems*, Geothermics (2007).** Mitigation options and their physical basis.
- **USGS Earthquake Hazards Program at <https://earthquake.usgs.gov>.** The
  authoritative catalogue and magnitude conventions.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 13. Related lessons

- [06-12-01 Causes of Induced Seismicity](./01-induced-seismicity-causes.md) —
  what the protocol is trying to control.
- [06-12-02 Pore-Pressure Diffusion and Triggering Mechanisms](./02-pore-pressure-triggering.md)
  — why a stoppage does not immediately stop the pressure field.
- [06-12-03 Rate-and-State Friction and the Dieterich Seismicity Model](./03-rate-state-triggering.md)
  — the rate criterion in its mechanism-level form.
- [06-12-05 Documented Case Studies](./05-case-studies-induced.md) — protocols as
  they were actually applied.
- [06-11-01 The Gutenberg–Richter Law](../11-earthquake-statistics-and-hazard/01-gutenberg-richter.md)
  — the magnitude–frequency relation used throughout.

Exercises:
[`exercises/04-monitoring-and-mitigation-exercises.md`](./exercises/04-monitoring-and-mitigation-exercises.md)
and
[`exercises/04-monitoring-and-mitigation-solutions.md`](./exercises/04-monitoring-and-mitigation-solutions.md).

## Self-assessment checklist

- [ ] I can compute an exceedance rate and convert it to stoppages per basin.
      (§3.1, §7.1)
- [ ] I can compute $P(M_{\max} > M_t)$ and $N_{50}$. (§3.2, §7.2)
- [ ] I can state the corrected $\mathrm{E}[M_{\max}]$ and the size of the omitted
      term. (§3.2, §7.3)
- [ ] I can quote the measured 5–95 spread and say that it is independent of $N$.
      (§7.3)
- [ ] I can explain why no statistical argument bounds induced event size. (§3.3)
- [ ] I can describe the $M_c$ problem and one way a drifting $M_c$ fools a rate
      criterion. (§2.3, §5)
- [ ] I can write a cost model, solve it analytically and say why the answer is a
      policy choice. (§3.4, §7.4)
- [ ] I can state the units of every quantity and the unit trap in $\lambda T$.
      (§6)
- [ ] I can say what a protocol can and cannot promise. (§4, §3.3)
