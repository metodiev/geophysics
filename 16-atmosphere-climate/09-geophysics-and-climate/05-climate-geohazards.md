---
id: 16-09-05
title: "Climate-Geohazard Interactions (Sea Level, Permafrost, Slopes)"
level: research
prereqs: ["16-09-02", "16-07-04", "13-07-01"]
tags: [atmosphere, climate, geohazards, sea-level, permafrost, slope-stability, compound-events]
---

# Climate-Geohazard Interactions (Sea Level, Permafrost, Slopes)

> **All models and data in this module are SYNTHETIC.** The hazard distributions,
> ground-ice contents, slope geometry and strength parameters in
> `code/climate_geohazards_demo.py` are chosen teaching values. No real coastline,
> permafrost site, slope, event, instrument or published projection is used.

A climate change becomes a geohazard by pushing a *threshold* in a mechanical or
hydrological system. That is the whole mechanism, and it has three recurring
features. First, the climate enters as a **boundary condition**, not as a force:
sea level offsets the effective defence height, thaw depth releases water and
removes ice, precipitation raises pore pressure. Second, the response is
**threshold-dominated**, so a modest change in the boundary condition produces a
large change in the frequency of failure. Third, the failure is usually
**compound**: a coastal flood needs a surge *and* a high river stage, and their
dependence, not just their levels, sets the probability.

This lesson quantifies all three with numbers from a demonstration: a sea-level
rise of $0.50\ \mathrm{m}$ cuts the return period of a synthetic compound coastal
flood from $28.3$ to $14.0$ years with the defences unchanged; an active layer
deepening from $1.0$ to $1.8\ \mathrm{m}$ in soil with $30\%$ excess ice produces
$0.24\ \mathrm{m}$ of settlement; and a slope's factor of safety crosses one
between pore-pressure ratios of $0.4$ and $0.5$. Each is a mechanical statement
first and a climate statement second, and the counterfactual that makes it a
climate statement is named explicitly at the end.

## Learning objectives

By the end of this lesson you will be able to:

1. **Explain** how a climate change enters a geohazard as a boundary condition,
   and identify the threshold it moves.
2. **Compute** the joint and union exceedance probability of a compound coastal
   event with a stated dependence, with and without a sea-level rise.
3. **Quantify** the change in return period of a compound event under a shift of
   one driver, and explain why different summaries respond differently.
4. **Derive** permafrost thaw settlement from excess-ice content and the change in
   active-layer thickness, and state what makes it damaging.
5. **Compute** the factor of safety of an infinite slope as a function of the
   pore-pressure ratio, and **find** the threshold crossing.
6. **State** the counterfactual behind each climate-geohazard statement, and
   **distinguish** the hazard statement from the risk statement.
7. **Report** a geohazard projection with its dependence assumption, its
   threshold and its uncertainty.

## Prerequisites

- [16-09-02 Geodesy for Sea Level, Ice Mass and Water Storage](02-geodesy-climate.md) —
  where the sea-level change comes from and how well it is known.
- [16-07-04 Impacts, Vulnerability and Risk Assessment](../07-climate-extremes-and-attribution/04-impacts-and-risk.md) —
  the hazard–exposure–vulnerability framing this lesson feeds.
- [13-07-01 Erosion, Uplift and Thermochronology](../../13-geodynamics-tectonics/07-geomorphology-tectonics-climate/01-erosion-and-uplift.md) —
  the surface-process context for slope and landscape response.

## 1. The hazard chain

For a coastal, permafrost or slope hazard, the chain is

$$\text{climate change} \;\to\; \text{boundary condition} \;\to\;
\text{mechanical or hydrological state} \;\to\; \text{threshold crossing}
\;\to\; \text{failure}.$$

- **Coastal flooding.** Sea-level rise enters as an *offset* to the effective
  defence level: the surge height needed to overtop a structure falls by the rise.
- **Permafrost.** Warming deepens the active layer; melting excess ice removes
  supporting volume and releases water, producing settlement and raising pore
  pressures.
- **Slopes.** Wetter or thawing ground raises the pore-pressure ratio $r_u$, which
  reduces effective stress and therefore shear strength.

In every case the climate variable is a *state*, and the hazard is a *crossing*.
That is why the same physical change can be harmless in one setting and
catastrophic in another: the distance from the operating state to the threshold is
a property of the site, not of the climate.

## 2. Compound coastal flooding

Take two synthetic drivers: a storm surge $S$ (lognormal, median
$1.20\ \mathrm{m}$, log-scale $0.35$) and a river stage $R$ (lognormal, median
$1.00\ \mathrm{m}$, log-scale $0.40$), coupled by a Gaussian copula with
correlation $\rho = 0.50$. The defence level is $1.80\ \mathrm{m}$ and the river
flood stage is $1.70\ \mathrm{m}$. The events of interest are

$$A = \{S > 1.80\ \mathrm{m}\}, \qquad B = \{R > 1.70\ \mathrm{m}\},$$

and both $\Pr(A \cap B)$ (a compound flood) and $\Pr(A \cup B)$ matter, depending
on whether the impact requires both drivers or either. With no sea-level rise the
demonstration computes

$$\Pr(A \cap B) = 0.03536\ (\text{return period } 28.3\ \mathrm{yr}),
\qquad \Pr(A \cup B) = 0.18030.$$

Now add a sea-level rise of $0.50\ \mathrm{m}$, which lowers the effective surge
threshold to $1.30\ \mathrm{m}$ and changes nothing else:

$$\Pr(A \cap B) = 0.07139\ (\text{return period } 14.0\ \mathrm{yr}),
\qquad \Pr(A \cup B) = 0.43048.$$

Three things are worth reading off, and the third is the subtle one.

1. **The compound event's return period halves** ($28.3 \to 14.0$ years) with the
   defences unchanged.
2. **The union probability more than doubles** ($0.180 \to 0.430$), because
   "either driver" is far more sensitive to a shift of one driver than "both".
3. **The two ratios differ** ($2.02\times$ for the joint, $2.39\times$ for the
   union), and neither is the reciprocal of the marginal exceedance change. *Every
   summary of the hazard has its own sensitivity*, so a statement of the form "the
   risk doubles" is incomplete without naming the metric.

Sweeping the rise makes the nonlinearity explicit:

| sea-level rise (m) | $\Pr(A\cap B)$ | return period (yr) | factor vs today |
|---|---|---|---|
| 0.00 | 0.03536 | 28.3 | 1.00× |
| 0.20 | 0.04914 | 20.4 | 1.39× |
| 0.50 | 0.07139 | 14.0 | 2.02× |
| 0.80 | 0.08724 | 11.5 | 2.47× |
| 1.00 | 0.09139 | 10.9 | 2.58× |

The response *saturates*: the second half-metre adds much less than the first,
because the effective threshold has moved deep into a region where the surge
distribution's density is falling. **A linear extrapolation of "risk per metre"
would be wrong in both directions** — too large at small rises, too small at large
ones — and only the calculation, not the intuition, gives the sensitivity.

## 3. Permafrost thaw settlement

When ice-rich permafrost thaws, the water that leaves the column as drainage (or
is expelled by consolidation) removes volume, and the ground surface subsides. To
first order, the settlement is the product of the **excess-ice volume fraction**
and the **newly thawed thickness**:

$$\Delta z = f_{\text{ice}} \times \left(h_{\text{warm}} - h_{\text{now}}\right).$$

The demonstration uses $f_{\text{ice}} = 0.30$ with the active layer deepening
from $1.0$ to $1.8\ \mathrm{m}$:

$$\Delta z = 0.30 \times (1.8-1.0) = 0.30 \times 0.80
= \mathbf{0.240\ m}.$$

Two properties make this a hazard rather than a curiosity. It is **large** — $24\%$
of a $1\ \mathrm{m}$ embankment's height — and it is **differential**, because the
ice content varies laterally, so a structure spanning varying ground is bent
rather than uniformly lowered. The linear scaling is also the sensitivity: a thaw
of $0.4\ \mathrm{m}$ instead of $0.8\ \mathrm{m}$ gives $0.120\ \mathrm{m}$ of
settlement, and the estimate is only as good as the excess-ice fraction, which is
the poorly known input (from boreholes, and highly variable).

## 4. Slope stability as pore pressure rises

For a shallow slab on a slope, the **infinite-slope** model gives the factor of
safety

$$F = \frac{c' + \left(\gamma z\cos^{2}\beta - u\right)\tan\phi'}
{\gamma z \sin\beta\cos\beta},$$

where $c'$ and $\phi'$ are effective strength parameters, $\gamma$ the unit
weight, $z$ the slab thickness, $\beta$ the slope angle and $u$ the pore
pressure. Writing the pore-pressure ratio $r_u = u/(\gamma z)$ — the standard
convenient form because it is dimensionless and bounded:

$$F = \frac{c'}{\gamma z\sin\beta\cos\beta}
+ \frac{\cos^{2}\beta\,(1-r_u)\tan\phi'}{\sin\beta\cos\beta}.$$

The demonstration uses $\gamma = 18.0\ \mathrm{kN\,m^{-3}}$,
$c' = 5.0\ \mathrm{kPa}$, $\phi' = 30^\circ$, $\beta = 22^\circ$ and
$z = 3.0\ \mathrm{m}$:

| $r_u$ | factor of safety | state |
|---|---|---|
| 0.0 | 1.696 | stable |
| 0.2 | 1.410 | stable |
| 0.4 | 1.124 | stable |
| 0.5 | **0.981** | failure |

The factor of safety crosses one between $r_u = 0.4$ and $r_u = 0.5$. Note that
the *first* term is the cohesion contribution and the second carries the entire
$r_u$ dependence; for a cohesionless soil ($c' = 0$) the threshold has a closed
form, $F = 1$ when

$$\tan\beta = (1-r_u)\tan\phi',$$

so a rise in $r_u$ directly erodes the friction that holds the slope. For the
numbers above the cohesion term is $5.0/(18\times3\times0.375\times0.927) = 0.267$
and the friction term at $r_u = 0$ is $1.429$, summing to $1.696$ — the friction
term dominates, which is the common situation on natural slopes.

**The climate statement is about $r_u$, not about the slope.** "The slope will
fail" is not a climate statement; "the probability that $r_u$ exceeds $0.45$ in a
given year has changed by a factor of $X$" is. The slope has no probability; the
pore pressure does.

## 5. The counterfactual, and the difference from a risk statement

Every climate-geohazard statement needs the same four elements as an event
attribution ([16-07-03](../07-climate-extremes-and-attribution/03-event-attribution.md)),
applied to a mechanical threshold:

1. **The hazard metric and threshold.** Here: surge $> 1.80\ \mathrm{m}$ *and*
   river $> 1.70\ \mathrm{m}$; or $r_u > 0.45$; or settlement exceeding a stated
   tolerance.
2. **The counterfactual.** The same distributions with the mean sea level (or the
   thaw depth, or the precipitation and temperature regime) set to its
   pre-change value, everything else held equal. This is a *modelled* world.
3. **The probabilistic statement with its uncertainty.** *"Under a
   $0.50\ \mathrm{m}$ rise, the joint exceedance probability rises from $0.0354$
   to $0.0714$ (return period $28.3 \to 14.0$ years), conditional on the stated
   marginals and a copula correlation of $0.50$; the sensitivity to the
   correlation is ..."*
4. **Exposure and vulnerability, which are separate.** The loss from a compound
   flood depends on what is behind the defence and how it fails; that is
   [16-07-04](../07-climate-extremes-and-attribution/04-impacts-and-risk.md)'s
   subject, and it usually dominates the hazard change in the loss arithmetic.

The distinction matters because a defensible coastal or slope statement is
**conditional**: conditional on the dependence assumption, on the threshold, and
on the counterfactual. Naming the condition is not hedging; it is the difference
between a projection and an assertion.

## 6. Assumptions and regime of validity

1. **Stationary marginals apart from the applied shift.** The demonstration moves
   one marginal's location; a change in the *variance* or in the *dependence*
   gives a different answer, and both are physically plausible.
2. **A stated copula.** $\rho = 0.50$ is a choice; independence would give a much
   smaller joint probability, and the demonstration's own sensitivity is a factor
   of several between $\rho = 0$ and $\rho = 0.9$.
3. **A fixed defence level.** Real defences degrade, are raised, or fail
   progressively; the calculation keeps the structure fixed to isolate the hazard
   change.
4. **A first-order settlement model.** Excess-ice content, drainage and
   consolidation all matter; the linear product is a scaling statement, not a
   prediction for a site.
5. **An infinite-slope idealisation.** It assumes a shallow, planar failure
   surface and neglects three-dimensional geometry, progressive failure and
   vegetation; it is standard precisely because it gives the right *threshold*
   behaviour, not because it predicts the exact factor of safety.
6. **A static pore-pressure profile.** Real $r_u$ varies with rainfall, snowmelt
   and thaw; the hazard statement is about the distribution of $r_u$, which is a
   hydrology problem.
7. **No climate change in the hazard statistics beyond the applied shift.** A
   changing *intensity* distribution, not only a rising mean, changes the answer.

## 7. Python demonstration

[`code/climate_geohazards_demo.py`](code/climate_geohazards_demo.py) builds the
three synthetic systems and prints labelled results with units. It:

1. computes the joint and union exceedance probabilities of a compound coastal
   event with and without a sea-level rise;
2. sweeps the rise and reports the return-period change;
3. computes permafrost thaw settlement from excess ice and the active-layer
   change, with a sensitivity;
4. computes an infinite-slope factor of safety against the pore-pressure ratio
   and locates the threshold crossing;
5. states the counterfactual each statement requires.

Every number in this lesson is printed by that demonstration.

## Mastery checkpoint

> The demonstration's compound coastal hazard has surge (lognormal median
> $1.20\ \mathrm{m}$, log-scale $0.35$), river stage (median $1.00\ \mathrm{m}$,
> log-scale $0.40$), copula correlation $0.50$, and thresholds $1.80$ and
> $1.70\ \mathrm{m}$.
>
> **(a)** Write $\Pr(A \cap B)$, $\Pr(A \cup B)$ and the inclusion–exclusion
> relation, and explain why a compound-flood impact may need either the
> intersection or the union.
> **(b)** A $0.50\ \mathrm{m}$ rise takes the compound return period from $28.3$ to
> $14.0$ years. Explain in one paragraph why the defences are unchanged yet the
> risk changed.
> **(c)** The joint ratio is $2.02\times$ and the union ratio $2.39\times$. State
> why a report of "the risk doubles" is incomplete.
> **(d)** With $30\%$ excess ice and an active layer deepening from $1.0$ to
> $1.8\ \mathrm{m}$, compute the settlement, and state the input that dominates
> its uncertainty.
> **(e)** For $\gamma = 18\ \mathrm{kN\,m^{-3}}$, $c' = 5\ \mathrm{kPa}$,
> $\phi' = 30^\circ$, $\beta = 22^\circ$ and $z = 3\ \mathrm{m}$, compute $F$ at
> $r_u = 0$ and $r_u = 0.5$ and state the crossing point.
> **(f)** State the counterfactual required before calling any of (a)–(e) a
> climate statement.

## Common pitfalls

1. **Reporting "the risk doubles" without the metric.** The joint and union
   probabilities changed by different factors.
2. **Assuming independence for compound drivers.** Dependence is a first-order
   term, as [16-07-04](../07-climate-extremes-and-attribution/04-impacts-and-risk.md)
   also measures.
3. **Extrapolating linearly in sea level.** The response saturated in the
   demonstration's table.
4. **Treating settlement as uniform.** Differential settlement is what damages
   infrastructure.
5. **Confusing a factor of safety with a probability.** $F$ is deterministic given
   $r_u$; the hazard is the distribution of $r_u$.
6. **Omitting the counterfactual.** A geohazard projection without one is not a
   climate statement.
7. **Forgetting exposure and vulnerability.** A defence that is raised changes the
   risk without changing the hazard.

## Related modules

- [16-09-02 Geodesy for Sea Level, Ice Mass and Water Storage](02-geodesy-climate.md) —
  how the sea-level change itself is measured and budgeted.
- [16-09-01 Seismic and Geodetic Monitoring of Cryosphere Change](01-seismic-monitoring-climate.md) —
  monitoring the cryospheric changes that drive the permafrost and slope hazards.
- [16-07-04 Impacts, Vulnerability and Risk Assessment](../07-climate-extremes-and-attribution/04-impacts-and-risk.md) —
  the risk arithmetic this lesson's hazards feed.
- [16-07-03 Event Attribution Methodology and Its Limits](../07-climate-extremes-and-attribution/03-event-attribution.md) —
  the counterfactual logic applied to a hazard chain.
- [13-07 Geomorphology, Tectonics and Climate](../../13-geodynamics-tectonics/07-geomorphology-tectonics-climate/README.md) —
  the longer-timescale surface processes behind slope and landscape change.
- [06-11 Earthquake Statistics and Hazard](../../06-seismology/11-earthquake-statistics-and-hazard/README.md) —
  the hazard-curve and return-period bookkeeping in its mature form.

## Self-assessment checklist

- [ ] I can identify the boundary condition and the threshold in a hazard chain.
- [ ] I can compute joint and union exceedance probabilities with dependence.
- [ ] I can quantify a return-period change under a shift of one driver.
- [ ] I can derive thaw settlement from excess ice and active-layer change.
- [ ] I can compute an infinite-slope factor of safety and locate the crossing.
- [ ] I can state the counterfactual behind a climate-geohazard statement.
