---
id: 11-01-01
title: "Exploration Lifecycle: Reconnaissance to Reserve Definition"
level: intermediate
prereqs: ["05-01-01", "05-05-01", "04-06-02"]
tags: [exploration-geophysics, exploration-lifecycle, resources-and-reserves, cut-off-grade, decision-making]
---

# Exploration Lifecycle: Reconnaissance to Reserve Definition

Exploration is not a measurement campaign with a report at the end. It is a
**sequence of irreversible spending decisions**, each of which buys information
that may justify the next one. This lesson builds the quantitative skeleton of
that sequence: the probability funnel, the size and grade distributions that a
deposit is drawn from, and the cut-off grade that converts a *geological* tonnage
into an *economic* reserve.

**All models and data in this module are SYNTHETIC.** The stage probabilities,
costs, distributions, metal prices and discount rates used here are chosen
teaching values. No number in this lesson is a published statistic for any real
belt, company or deposit.

## Learning objectives

By the end of this lesson you will be able to:

1. **Describe** the exploration lifecycle as a funnel of conditional decisions,
   and **compute** the overall probability of success and the expected spend per
   discovery from stage costs and advance probabilities.
2. **Explain** why the expected spend is a geometric series rather than a sum of
   stage costs, and **quantify** the difference for a given program.
3. **Compute** quantiles and moments of a lognormal deposit-size distribution, and
   **explain** why the mean exceeds the median and why the tail carries most of
   the metal.
4. **Derive** the ore-tonnage, head-grade and contained-metal curves for a grade
   distribution, and **show** that contained metal decreases monotonically with
   the cut-off grade.
5. **Derive** the marginal break-even cut-off $c^{*}=C/(rP)$ and **demonstrate**
   that it is independent of the grade distribution.
6. **Quantify** how mill capacity and a discount rate push the optimal cut-off
   above break-even, and **state** what that implies for a "reserve tonnage".
7. **Distinguish** a resource from a reserve, and **state** which inputs of a
   reserve statement are measurements and which are choices.

## Prerequisites

- [05-01-01 The Central Idea: Property Contrasts Produce Signals](../../05-core-geophysics/01-what-geophysics-measures/01-physical-property-contrast.md)
  — the detection logic that every stage of the funnel depends on.
- [05-05-01 Survey Planning: Objectives, Target Resolution, Budget](../../05-core-geophysics/05-survey-design-and-acquisition/01-survey-planning.md)
  — how a single stage is designed and costed.
- [04-06-02 Mineral Deposit Types and Their Geophysical Signatures](../../04-earth-science-geology/06-petroleum-and-mineral-systems/02-mineral-deposits.md)
  — what is being looked for, and why deposit classes differ.

## 1. The lifecycle as a decision chain

A grassroots program moves through stages that differ in *spatial scale*, *cost*
and *what is decided*:

| Stage | Typical question | Decision bought |
|---|---|---|
| Regional reconnaissance | Where, in a $10^4\ \mathrm{km^2}$ region, is the geology permissive? | Where to spend the next dollar |
| Prospect delineation | Is there an anomaly, and is it geologically explained? | Whether to acquire ground |
| Target definition | Where exactly is the body, how deep, how big? | Whether to drill |
| Discovery drilling | Does mineralisation exist at that location? | Whether to delineate |
| Resource definition | How much, at what grade, at what confidence? | Whether to engineer |
| Feasibility / reserve | Does it pay, under a stated price and discount rate? | Whether to build |

Three structural facts follow, and they are the subject of this lesson:

1. **Each stage is entered by the survivors of the previous one.** Cost is spent
   on failures, not only on successes, so the *expected* spend per discovery is
   much larger than the sum of the stage budgets.
2. **The size and grade of whatever is found are random.** They are drawn from a
   heavy-tailed distribution, so the mean outcome is driven by rare large
   deposits, and any single discovery is more likely to be small than large.
3. **The final number, the reserve, is not a measurement.** It is a profit
   calculation, and it moves with the price, the recovery and the discount rate —
   none of which is a geological observation.

## 2. The funnel: conditional probabilities and the geometric series

Let stage $i$ have cost $C_i$ (MUSD) and let $p_i$ be the probability of
*advancing* from stage $i$ to stage $i+1$, conditional on having entered stage
$i$. The probability that a single attempt reaches the end is

$$P_{\text{success}} = \prod_{i=1}^{n} p_i .$$

Stage $i$ is entered with probability $S_{i-1} = \prod_{j<i} p_j$, so the expected
spend *per attempt* is the **geometric-type series**

$$\mathbb{E}[\text{spend}] = \sum_{i=1}^{n} S_{i-1}\,C_i,
\qquad S_0 = 1 .$$

Note what this is *not*: it is not $\sum_i C_i$. A program that ran every stage
unconditionally would be a sum of budgets; a staged program pays later stage
costs only in the fraction of attempts that survive to them.

### Worked example 1 — the funnel of the demonstration model

The SYNTHETIC program of `code/exploration_lifecycle_demo.py` has
$C = (0.60, 2.50, 6.00, 24.0, 40.0, 55.0)$ MUSD and
$p = (0.35, 0.30, 0.25, 0.55, 0.60, 1.00)$.

Overall success probability:

$$P_{\text{success}} = 0.35 \times 0.30 \times 0.25 \times 0.55 \times 0.60
= 0.008662 \approx \frac{1}{115}.$$

Expected spend, term by term ($S_{i-1} C_i$):

$$0.600 + 0.35(2.50) + 0.105(6.00) + 0.02625(24.0)
+ 0.0144375(40.0) + 0.0086625(55.0)$$
$$= 0.600 + 0.875 + 0.630 + 0.630 + 0.5775 + 0.4764
= 3.789\ \mathrm{MUSD}.$$

Expected spend per discovery:

$$\frac{3.789}{0.008662} = 437.4\ \mathrm{MUSD}.$$

The unconditional stage sum is $128.1$ MUSD — 34 times larger. **Staging is the
whole of the risk management**: it converts a $\$128$ M program that fails most of
the time into a $\$3.8$ M experiment per attempt, repeated until something
survives. This arithmetic is printed in section 1 of the demo.

## 3. Size and grade: the distributions a deposit is drawn from

Deposit tonnages in a population are, by long experience of many belts,
right-skewed. A **lognormal** model is the standard first description: if
$\ln T \sim \mathcal{N}(\mu,\sigma^2)$ then

$$\mathbb{E}[T] = e^{\mu + \sigma^{2}/2}, \qquad
\mathrm{median}(T) = e^{\mu}, \qquad
\mathbb{P}(T > t) = \Phi\!\left(-\frac{\ln t - \mu}{\sigma}\right).$$

The mean is larger than the median by the factor $e^{\sigma^{2}/2}$: with
$\sigma = 1.10$ that factor is $e^{0.605} = 1.83$. The mean is therefore *not* a
size one should expect to find; it is the long-run average, dominated by the tail.

### Worked example 2 — the size distribution of the SYNTHETIC population

With median $30\ \mathrm{Mt}$ and $\sigma = 1.10$:

$$\mathbb{E}[T] = 30\,e^{1.10^{2}/2} = 30 \times 1.8311 = 54.9\ \mathrm{Mt}.$$

$$\mathbb{P}(T > 100\ \mathrm{Mt}) = \Phi\!\left(
-\frac{\ln 100 - \ln 30}{1.10}\right)
= \Phi\!\left(-\frac{4.6052 - 3.4012}{1.10}\right)
= \Phi(-1.0945) = 0.1369 .$$

With a population mean grade of $0.50\%$ Cu, the contained metal of a $100\ \mathrm{Mt}$
deposit is $100\times10^{6} \times 0.005 = 500\ \mathrm{kt}$ Cu. The measured
quantiles of the demo are $7.3\ \mathrm{Mt}$ (P10), $30.0\ \mathrm{Mt}$ (P50) and
$122.8\ \mathrm{Mt}$ (P90): **the P90 is 17 times the P10** because the
distribution is multiplicative. A program's expected metal is set by the P90–P99
range, while a *given* discovery is more likely than not to be below the mean.

## 4. Grade, cut-off and the tonnage–grade curve

Inside one deposit, grade is also variable, and a mining operation does not treat
all of it as ore. Fix a deposit of $T_{\text{tot}}$ tonnes with grade density
$f(g)$ (mass fraction). Above a cut-off $c$:

$$T(c) = T_{\text{tot}}\int_{c}^{\infty} f(g)\,\mathrm{d}g
= T_{\text{tot}}\,\mathbb{P}(G > c),$$

$$\bar g(c) = \mathbb{E}[G \mid G > c]
= \frac{\int_c^{\infty} g f(g)\,\mathrm{d}g}{\mathbb{P}(G>c)},
\qquad
Q(c) = T(c)\,\bar g(c).$$

For a lognormal grade model, using $z(c) = (\ln c - \mu_g)/\sigma_g$,

$$\mathbb{P}(G>c) = \Phi(-z), \qquad
\mathbb{E}[G\mid G>c] = e^{\mu_g + \sigma_g^{2}/2}\,
\frac{\Phi(\sigma_g - z)}{\Phi(-z)} .$$

**Contained metal is not conserved.** $Q(c)$ decreases monotonically with $c$:
raising the cut-off discards rock that contains metal. The cut-off does not
create or protect metal; it protects *margin per tonne*. That trade is the entire
subject of the next section.

### Worked example 3 — the tonnage–grade curve

The demo deposit has $T_{\text{tot}} = 100\ \mathrm{Mt}$, median grade
$0.30\%$ Cu and $\sigma_g = 0.60$, so $e^{\mu_g+\sigma_g^2/2} = 0.003 \times
e^{0.18} = 0.359\%$ Cu mean grade. At a cut-off of $0.20\%$ Cu:

$$z = \frac{\ln 0.002 - \ln 0.003}{0.60} = \frac{-0.405465}{0.60} = -0.6758,
\qquad \Phi(-z) = \Phi(0.6758) = 0.7504,$$

$$T = 100 \times 0.7504 = 75.0\ \mathrm{Mt},$$

$$\bar g = 0.003597 \times \frac{\Phi(0.60 + 0.6758)}{\Phi(0.6758)}
= 0.003597 \times \frac{0.89900}{0.75035} = 0.004303 = 0.430\%\ \mathrm{Cu},$$

$$Q = 75.0 \times 10^{6} \times 0.004303 = 322.9\ \mathrm{kt\ Cu}.$$

At a $0.50\%$ cut-off the demo gives $19.7\ \mathrm{Mt}$ at $0.730\%$ Cu, or
$143.9\ \mathrm{kt}$ — **less than half the metal**, in a quarter of the tonnes.

## 5. The optimal cut-off: break-even, then capacity, then discounting

### 5.1 Break-even grade

Let $r$ be metallurgical recovery, $P$ the metal price (USD per tonne of contained
metal) and $C$ the mining-plus-processing cost (USD per tonne of ore). The margin
on a tonne of grade $g$ is $rPg - C$, so the grade at which a tonne neither earns
nor loses is

$$\boxed{\,c_{\text{be}} = \frac{C}{rP}\,}.$$

With $C = 15\ \mathrm{USD/t}$, $r = 0.88$ and $P = 9000\ \mathrm{USD/t}$:

$$c_{\text{be}} = \frac{15}{0.88 \times 9000} = \frac{15}{7920}
= 0.001894 = 0.1894\%\ \mathrm{Cu}.$$

### 5.2 Why that is also the optimum when nothing couples one tonne to another

Total undiscounted profit is

$$\Pi(c) = T_{\text{tot}} \int_{c}^{\infty}\left(rPg - C\right) f(g)\,\mathrm{d}g .$$

Differentiating with respect to the lower limit,

$$\frac{\mathrm{d}\Pi}{\mathrm{d}c}
= -T_{\text{tot}}\left(rPc - C\right) f(c) = 0
\;\Longrightarrow\;
c^{*} = \frac{C}{rP} = c_{\text{be}} .$$

Two things are worth pausing on. First, the stationarity condition is
**independent of $f$**: the optimum cut-off of an unconstrained operation does not
depend on the grade distribution at all. Second, the demonstration confirms it
numerically — the optimiser returns $0.1894\%$ Cu, identical to $c_{\text{be}}$ to
four decimals.

### 5.3 Capacity and discounting move the optimum up

Real operations have a fixed mill throughput. If the mill processes
$M = 8\ \mathrm{Mt/yr}$, the mine life at cut-off $c$ is $L(c) = T(c)/M$, and the
net present value at discount rate $\rho$ is

$$\mathrm{NPV}(c) = M \times 10^{6}\left(rP\bar g(c) - C\right)
\frac{1-(1+\rho)^{-L(c)}}{\rho} - \text{capital}.$$

Now the tonnes are no longer equivalent: a low cut-off adds tonnes that can only
be processed *after* the higher-grade tonnes, so their revenue arrives later and
is discounted. The demo measures the consequence:

| discount rate | optimal cut-off | mine life | NPV |
|---|---|---|---|
| 0% | 0.1894% Cu | 9.73 yr | 1082.8 MUSD |
| 5% | 0.2399% Cu | 8.07 yr | 784.4 MUSD |
| 10% | 0.2800% Cu | 6.82 yr | 596.6 MUSD |
| 20% | 0.3387% Cu | 5.25 yr | 373.1 MUSD |
| 35% | 0.3974% Cu | 4.00 yr | 195.2 MUSD |

The optimal cut-off rises from $0.1894\%$ to $0.3974\%$ Cu as the discount rate
rises from 0 to 35% — **+0.21 percentage points**, which removes a large fraction
of the reserve tonnage. The deposit is unchanged. A reserve tonnage is a statement
about a *plan*, and the plan depends on money, not on rock.

## 6. Resource versus reserve, and what is measured

The distinction is a confidence statement plus an economic filter:

| Term | Content | Dominated by |
|---|---|---|
| **Resource** | Tonnage and grade with a stated geological confidence | Drill density; continuity of mineralisation |
| **Reserve** | The part of the resource that pays under a stated plan | Price, recovery, costs, discount rate, permitting |

Confidence is *bought with drilling*. On a regular grid of spacing $s$ over an
area $A$ the hole count is $n = A/s^{2}$, so refining a $400\ \mathrm{m}$ grid to
$100\ \mathrm{m}$ costs **16 times the holes** for the same area. The demo prints
$9$, $38$, $150$ and $600$ holes for $400$, $200$, $100$ and $50\ \mathrm{m}$
spacing over $1.5\ \mathrm{km^{2}}$. The cost of moving a tonnage from a low to a
high confidence class therefore scales as $(s_{\text{old}}/s_{\text{new}})^{2}$;
it is a *sampling* decision, not a geophysical one, though geophysics is what
makes a coarser grid sufficient.

Applying the funnel to exploration targets gives the last piece of honest
arithmetic. For $N$ independent targets each with probability $p$:

$$\mathbb{E}[\text{discoveries}] = Np, \qquad
\mathbb{P}(\text{at least one}) = 1-(1-p)^{N}, \qquad
\mathbb{P}(\text{none}) = (1-p)^{N}.$$

With $N=12$ and $p=0.05$: $\mathbb{E}=0.60$, $\mathbb{P}(\text{at least one})
= 0.460$, $\mathbb{P}(\text{none}) = 0.540$. **The expectation can be near one
while the median outcome is still nothing.** Reporting the expectation without
the distribution is the commonest way an exploration program is mis-represented.

## 7. Assumptions and regime of validity

1. **Independence of stages and targets.** The product rule in §2 assumes the
   conditional probabilities are the analyst's best estimates and are applied
   consistently. In reality the same team, the same commodity and the same belt
   correlate the outcomes; a shared failure mode (a wrong regional concept) makes
   the portfolio formula optimistic.
2. **Stationary distributions.** The lognormal models are assumed not to change
   with the area explored or with time. They are *population* distributions; an
   individual deposit is a single draw, and no statement here bounds its size.
3. **Constant recovery and grade-independent metallurgy.** The neat result
   $c^{*}=C/(rP)$ requires $r$ to be independent of $g$. Recovery usually
   *increases* with grade (better liberation, more sulphide), which raises the
   optimum above break-even for a second, metallurgical reason.
4. **One metal, one product.** No by-product credits, penalties, royalties or
   taxes are modelled. Each of them shifts $c_{\text{be}}$, and by-product credits
   can move it a long way.
5. **The cut-off is applied to a grade distribution, not to selective mining
   units.** Real operations classify by block with grade control; the *effective*
   cut-off then differs from the design cut-off. The measured optimum is a
   design-guide, not an operating rule.
6. **Lognormal is a choice.** It is convenient (closed forms, multiplicative
   structure) and it is not unique: a bootstrap of any real-size sample would
   replace it, and the tail — which drives the mean — is the least constrained
   part of any such model.
7. **The economic parameters are SYNTHETIC.** Prices, costs and discount rates
   here are teaching values.

## 8. Units, dimensional analysis and a check

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| stage cost | $C_i$ | MUSD |  |
| advance probability | $p_i$ | – | dimensionless, $0\le p_i\le 1$ |
| tonnage | $T$ | Mt ($10^{6}$ t) |  |
| grade | $g$ | mass fraction (or %) | dimensionless |
| contained metal | $Q = Tg$ | Mt of metal | $\mathrm{Mt}\times 1 = \mathrm{Mt}$; reported here in kt |
| metal price | $P$ | USD/t metal |  |
| ore cost | $C$ | USD/t ore |  |
| break-even grade | $C/(rP)$ | $\dfrac{\mathrm{USD/t\ ore}}{\mathrm{USD/t\ metal}}$ | dimensionless ✔ |

The unit check of $c_{\text{be}}$ is the one that matters: a cost per tonne of
**ore** divided by a price per tonne of **metal** is a grade, because the
recovery is dimensionless. Writing "*$\$15/\mathrm{t}$ divided by
$\$9000/\mathrm{t}$*" and getting $0.0017$ is the same calculation with $r=1$;
forgetting $r$ understates the cut-off and overstates the reserve.

The demonstration verifies both probability integrals against their closed forms:
the numeric ore fraction above $0.25\%$ Cu agrees with the lognormal survival
function to $2.2\times10^{-16}$ (machine precision), and the numerical head grade
agrees with the analytic expression to $6.9\times10^{-15}$ percentage points.

## 9. Worked example 4 — reading a reserve statement

A company reports "$77.8\ \mathrm{Mt}$ at $0.42\%$ Cu" for the SYNTHETIC deposit
above. Read it as follows.

1. **$77.8\ \mathrm{Mt}$ is ore, not rock.** The demo's reserve at a $9000\
   \mathrm{USD/t}$ price is $77.83\ \mathrm{Mt}$ at a $0.1894\%$ cut-off.
2. **$0.42\%$ is a head grade, not the median grade.** The median grade of the
   deposit is $0.30\%$; the head grade is higher because the cut-off removes the
   low-grade half.
3. **Contained metal is $77.83 \times 0.0042 = 327\ \mathrm{kt}$ Cu** — matching
   the demo's $328.3\ \mathrm{kt}$ to rounding.
4. **The price assumption is the biggest lever.** At $6000\ \mathrm{USD/t}$ the
   same deposit yields $53.62\ \mathrm{Mt}$ ($271\ \mathrm{kt}$ Cu): a $31.1\%$
   reduction in tonnage from a $33\%$ price fall. At $14000\ \mathrm{USD/t}$ it
   yields $93.36\ \mathrm{Mt}$ ($352.8\ \mathrm{kt}$), $+19.9\%$.
5. **Nothing in items 1–4 is a measurement of the deposit's size.** Only the
   grade distribution, the continuity and the drill density are; the rest is the
   plan.

## 10. Python demonstration

`code/exploration_lifecycle_demo.py` prints, with units:

1. the stage table, the overall $P_{\text{success}} = 0.008662$ and the expected
   spend per discovery (3.789 and 437.4 MUSD);
2. lognormal size quantiles (P10 $7.3$ to P99 $387.7\ \mathrm{Mt}$) and
   $\mathbb{P}(T>100\ \mathrm{Mt}) = 0.1369$;
3. the tonnage–grade–metal table versus cut-off;
4. the optimal cut-off at break-even, then versus discount rate, with life and NPV;
5. portfolio arithmetic for three $(N,p)$ pairs;
6. the price sensitivity of the reserve and the drill-density scaling;
7. numeric-versus-closed-form verification of the two integrals.

Run it with the project virtual environment:

```bash
cd 11-exploration-geophysics/01-exploration-workflow/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python exploration_lifecycle_demo.py
```

## 11. Exercises

See
[`exercises/01-exploration-lifecycle-exercises.md`](exercises/01-exploration-lifecycle-exercises.md)
and the worked
[`solutions`](exercises/01-exploration-lifecycle-solutions.md). The ★★★ problems
ask you to design, not merely evaluate.

## Mastery checkpoint

Without notes:

> A SYNTHETIC program has two stages: geophysics at $4$ MUSD with a probability
> $0.20$ of a drillable target, then drilling at $25$ MUSD with a probability
> $0.30$ of a discovery; the metallurgy of the discovered deposit has
> $r = 0.85$. **(a)** Compute the overall probability of success and the expected
> spend per discovery. **(b)** The deposit grades lognormally with median
> $0.40\%$ Cu and $\sigma_g = 0.55$; compute the mass fraction and head grade
> above a $0.25\%$ cut-off for $60\ \mathrm{Mt}$ of rock, and the contained metal.
> **(c)** Compute the break-even cut-off at $8000\ \mathrm{USD/t}$ and explain why
> a higher cut-off reduces contained metal. **(d)** State the three inputs to a
> reserve statement that are choices rather than measurements, and explain which
> one you would test first.

A worked version of (a)–(c) is in the
[solutions](exercises/01-exploration-lifecycle-solutions.md).

## Common pitfalls

1. **Summing stage costs.** The expected spend is a geometric series; the
   unconditional sum overstates the committed capital by an order of magnitude.
2. **Quoting an expected tonnage as "the" deposit size.** The mean of a
   right-skewed distribution is not typical. Report quantiles.
3. **Treating contained metal as fixed.** Raising the cut-off always discards
   metal; only margin per tonne improves.
4. **Assuming the optimal cut-off depends on the grade distribution.** In the
   unconstrained case it does not: $c^{*}=C/(rP)$ contains no $f(g)$.
5. **Forgetting the discount rate.** It is a first-order control on the reserve,
   not a footnote.
6. **Confusing the confidence classification with the economic filter.** A
   measured resource is still not a reserve; a reserve is a resource times a plan.
7. **Reporting the expectation of a portfolio without its distribution.** With
   $Np$ near one, the most likely outcome can still be zero discoveries.

## Related modules

- [11-01-02 Targeting Strategy and Method Selection](02-targeting-and-strategy.md)
  — how the geophysical spend inside stage 1–3 is allocated.
- [11-01-03 Cost, Risk and Value of Information in Exploration](03-cost-benefit.md)
  — what a geophysical survey is *worth* before it is flown.
- [11-02-01 Geophysical Signatures of Major Deposit Types](../02-mineral-exploration/01-deposit-signatures.md)
  — what stage-1 regional data can actually see.
- [05-07-05 Reporting Geophysical Results with Honest Uncertainty](../../05-core-geophysics/07-interpretation-and-integration/05-reporting-results.md)
  — the reporting conventions this lesson's numbers must obey.
