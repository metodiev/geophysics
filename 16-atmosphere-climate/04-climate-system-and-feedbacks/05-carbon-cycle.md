---
id: 16-04-05
title: "The Carbon Cycle: Reservoirs, Fluxes and Perturbations"
level: doctoral
prereqs: ["16-04-01", "16-04-02"]
tags: [atmosphere, climate, carbon-cycle, reservoirs, airborne-fraction, carbon-feedbacks]
---

# The Carbon Cycle: Reservoirs, Fluxes and Perturbations

Carbon moves between an atmosphere that holds a little of it and an ocean and
lithosphere that hold almost all of it. The perturbation problem is therefore
asymmetric in a way that is easy to state and hard to overstate: the atmosphere
contains about **2.3%** of the carbon in the atmosphere-plus-deep-ocean system
in this module's chosen inventories, so a change that is significant
atmospherically is a rounding error in the reservoirs it is exchanging with —
and yet the *time* scales of those exchanges are what decide how long the
perturbation lasts.

Two results in this lesson are structural rather than numerical, and both are
routine sources of error:

1. **A pulse has no single lifetime.** The demonstration's impulse response
   leaves 63% of a pulse in the atmosphere after 10 years, 37% after a century
   and 20% after ten thousand years. The tail is set by the coefficient that
   does not decay — the part that ocean chemistry and, ultimately, silicate
   weathering can remove only over millennia. Quoting "the residence time of
   CO₂" as one number discards exactly the fraction that matters at long
   horizons.
2. **The airborne fraction is a ratio of two growing quantities**, so it changes
   with time: in the demonstration's synthetic pathway it falls from 0.699 at 25
   years to 0.388 at 300 years as the sinks fill. An airborne fraction quoted
   without its window is not defined, and a constant one is not a law.

All models and data in this module are **SYNTHETIC**. Reservoir inventories,
impulse-response coefficients, emission pathways and uptake parameters are
**chosen teaching values** printed by
[`code/carbon_cycle_demo.py`](code/carbon_cycle_demo.py); they are
order-of-magnitude conventional magnitudes used to make the arithmetic
concrete, not measurements of the real carbon cycle. No scenario and no policy
figure is quoted.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the ppm-to-GtC conversion from surface pressure, gravity, molar
   masses and the Earth's area, and **state** the convention dependence that
   makes the constant differ between sources at the few-per-cent level.
2. **Compare** reservoir inventories and **explain** why the atmosphere's small
   share of the total dominates the *observable* signal.
3. **Use** an impulse response function to compute the fraction of a pulse
   remaining at several times, and **explain** why the result is a spectrum of
   timescales rather than a lifetime.
4. **Perform** the mass-balance check that any response function must satisfy,
   and **state** the constraint that a wrong set of coefficients violates.
5. **Compute** the airborne fraction along a pathway and **demonstrate** its
   time dependence.
6. **Distinguish** the $\beta$ and $\gamma$ uptake parameters by their
   mechanisms and their timescales.
7. **Compute** the warming per unit cumulative emissions from a chosen set of
   coefficients, and **state** why it varies with the range and is not a
   constant of nature.
8. **State** which of these results are physics, which are conventions and which
   are parameterisations.

## Prerequisites

- [16-04-01 Components of the Climate System and Their Timescales](01-climate-system-components.md) —
  the reservoir-and-timescale framework this lesson specialises to carbon.
- [16-04-02 Feedbacks: Water Vapour, Ice-Albedo, Cloud, Carbon](02-climate-feedbacks.md) —
  where $\beta$ and $\gamma$ were introduced as feedback parameters.
- [16-01-01 Atmospheric Composition and Vertical Structure](../01-atmospheric-structure-and-thermodynamics/01-atmospheric-composition.md) —
  the composition of the atmosphere and the role of the trace gases.

## 1. Intuition: a small atmosphere exchanging with a large ocean

The atmosphere is a thin shell of low heat capacity and, for carbon, a small
reservoir. Both facts push in the same direction: the atmosphere responds
quickly and is *sensitive*, while the reservoirs it exchanges with respond
slowly and are *large*. Three consequences follow:

- The measured signal — an atmospheric concentration — is a small residual of
  large gross fluxes, so it is informative but noisy.
- The long-term fate of an emitted pulse is decided by ocean chemistry, not by
  atmospheric physics.
- Any statement about "how long CO₂ stays in the atmosphere" is a statement
  about the *slowest* exchange, and therefore about the largest reservoir.

## 2. Definitions

| Term | Meaning used here |
|---|---|
| GtC | $10^{12}$ kg of carbon |
| ppm | Mixing ratio by mole, parts per million |
| Reservoir | A carbon store treated as well mixed on the timescale of interest |
| Flux | Transfer rate between reservoirs, GtC yr⁻¹ |
| Impulse response $a(t)$ | Fraction of an emitted pulse still in the atmosphere at time $t$ |
| Airborne fraction | Atmospheric excess divided by cumulative emissions, at a stated time |
| $\beta$ | Uptake per unit atmospheric excess |
| $\gamma$ | Additional uptake per kelvin of warming, GtC K⁻¹ |
| Residence time | Reservoir size divided by throughput; **not** the same as the decay time of a perturbation |

## 3. From ppm to GtC

The whole conversion is geometry and the ideal gas law in hydrostatic form. The
mass of the atmospheric column per unit area is $p_s/g$; multiply by the surface
area and by the mass fraction of carbon in air:

$$m_\text{atm} = \frac{p_s}{g}\,4\pi a^2
= \frac{1.013\times10^5}{9.81}\times5.1006\times10^{14}
= 5.267\times10^{18}\ \mathrm{kg},$$

$$1\ \mathrm{ppm} = 10^{-6}\,m_\text{atm}\frac{M_C}{M_\text{air}}
= 10^{-6}(5.267\times10^{18})(0.41460) = 2.1837\ \mathrm{GtC}.$$

The demonstration prints the checks ($2\ \mathrm{ppm} = 4.37$ GtC,
$100\ \mathrm{ppm} = 218.4$ GtC) and also the convention dependence: the
commonly quoted $2.12$ GtC per ppm corresponds to an atmospheric mass of
$5.123\times10^{18}$ kg, **2.8% less** than the value obtained from the adopted
sea-level pressure, because the real atmospheric mass is obtained by
integrating the actual pressure field, which is lower over high terrain.
**The derivation is the transferable content; the constant inherits whatever
convention about the atmosphere goes into it.** ([16-04-02](02-climate-feedbacks.md)
used the 2.124 GtC per ppm convention for its equilibrium budgets; the 2.8%
difference is a convention, not a discrepancy.)

## 4. Inventories and where the carbon is

| reservoir | inventory (GtC) |
|---|---|
| atmosphere (at 400 ppm) | 873.5 |
| land biosphere | 550.0 |
| soils and permafrost | 1500.0 |
| surface ocean | 900.0 |
| deep ocean | 37000.0 |
| fossil and rock reservoir | 4000.0 |

All six are **chosen** magnitudes. The structural point does not depend on
them: the atmosphere holds about **2.3%** of the atmosphere-plus-deep-ocean
total. Perturbing the atmospheric concentration measurably therefore requires
moving mass that is tiny relative to the reservoirs it exchanges with — which is
why a 1% change in the deep ocean's inventory would be invisible, while a 1%
change in the atmosphere's is not.

## 5. The impulse response: a pulse is not a lifetime

Write the fraction of a pulse remaining in the atmosphere as a sum of
exponentials plus a non-decaying part:

$$a(t) = a_0 + \sum_i a_i\mathrm{e}^{-t/\tau_i},\qquad
\text{demonstration: } (a,\tau) = (0.20,\infty), (0.30, 3.5),
(0.30, 30), (0.20, 400)\,\mathrm{yr}.$$

| time (yr) | fraction remaining | mass in the atmosphere for a 1000 GtC pulse |
|---|---|---|
| 1 | 0.9151 | 915.1 GtC |
| 10 | 0.6273 | 627.3 |
| 100 | 0.3665 | 366.5 |
| 1000 | 0.2164 | 216.4 |
| 10000 | 0.2000 | 200.0 |

Three readings:

- **There is no single lifetime.** A pulse is 63% airborne after a decade and 20%
  after ten millennia; the descriptive "residence time" depends entirely on the
  window.
- **The tail is structural, not a modelling convenience.** The non-decaying
  coefficient stands for the fraction whose removal requires carbonate and
  silicate chemistry operating over millennia. Removing it would make the model
  report a reassuringly finite lifetime that the chemistry does not support.
- **The sinks are the complement.** After 100 years, 633.5 GtC of the original
  1000 GtC is elsewhere; the total column is constant by construction, so the
  meaningful test is not that the total adds up but that **no sink ever becomes
  a source**, which a badly chosen set of coefficients (in particular any
  negative $a_i$, or coefficients summing to more than one) will violate.

## 6. A pathway: the airborne fraction over time

The demonstration ramps emissions linearly from 0 to $10\ \mathrm{GtC\,yr^{-1}}$
over 100 years and holds them for 200 more, convolving the emission rate with
the impulse response:

| time (yr) | cumulative emissions (GtC) | atmospheric excess (GtC) | airborne fraction |
|---|---|---|---|
| 25 | 31.6 | 22.1 | 0.699 |
| 50 | 125.6 | 77.3 | 0.615 |
| 100 | 501.2 | 266.9 | 0.532 |
| 150 | 1001.2 | 471.4 | 0.471 |
| 200 | 1501.2 | 648.7 | 0.432 |
| 300 | 2501.2 | 971.5 | 0.388 |

The airborne fraction is a **ratio of two growing quantities** and it falls by a
factor of 1.8 across the run as the sinks fill. Any statement of the form "about
half of the CO₂ we emit stays in the atmosphere" is therefore a statement about
a particular interval, with a particular set of sink coefficients, and does not
generalise. Note also the consistency check the demonstration prints: the
*minimum* sink value over the run is 0.000 GtC, i.e. the uptake never becomes an
emission. That is the constraint a response function must satisfy.

## 7. Two uptake parameters, two mechanisms

The equilibrium budget used in [16-04-02](02-climate-feedbacks.md) §9 was

$$\Delta C = \frac{E - \gamma\Delta T}{1+\beta},
\qquad
F = F_{2\times}\frac{\ln\!\left(1+\Delta C/C_0\right)}{\ln2}.$$

| case | $\Delta C$ (GtC) | airborne fraction | $\Delta T$ (K) |
|---|---|---|---|
| $\beta$ only ($\gamma = 0$) | 500.0 | 0.500 | 0.648 |
| reference ($\beta = 1$, $\gamma = 100$) | 469.2 | 0.469 | 0.616 |
| weak uptake ($\beta = 0.5$) | 615.9 | 0.616 | 0.762 |
| strong uptake ($\beta = 2.0$) | 318.4 | 0.318 | 0.447 |
| strong climate feedback ($\gamma = 300$) | 416.2 | 0.416 | 0.559 |

$\beta$ controls the *share* of an emission that stays airborne; $\gamma$
controls how much that share shrinks as the climate warms. They act in the same
direction and on different timescales: $\beta$ acts within decades as the ocean
mixed layer and land biosphere equilibrate, $\gamma$ over the decades to
centuries over which the temperature itself evolves. **Both are
parameterisations of unresolved processes.** The table demonstrates the
sensitivity; it does not estimate either one.

## 8. Cumulative emissions and warming

Running the same equilibrium budget at several emission totals:

| emissions (GtC) | $\Delta C$ (GtC) | ppm | $\Delta T$ (K) | $\Delta T$ per 1000 GtC |
|---|---|---|---|---|
| 250 | 116.0 | 419 | 0.181 | 0.723 |
| 500 | 232.9 | 473 | 0.341 | 0.682 |
| 1000 | 469.2 | 581 | 0.616 | 0.616 |
| 2000 | 947.9 | 800 | 1.043 | 0.521 |
| 4000 | 1918.4 | 1245 | 1.632 | 0.408 |

A least-squares slope gives 0.3803 K per 1000 GtC, but the *increment* falls
from 0.723 to 0.408 K per 1000 GtC across the range, and the largest departure
from the fitted line is 0.109 K. So:

- the relation is close to linear at the low end **over a doubling or so of
  cumulative emissions**, which is why a "warming per 1000 GtC" is a useful
  first-order tool;
- it is not a constant of nature: it changes with $\beta$, $\gamma$, the
  feedback parameter, the *pathway*, and — most importantly here — it is derived
  from an *equilibrium* budget while the real system is transient.

## 9. What is physics, what is convention, what is a parameterisation

This distinction is the practical lesson of the module, so state it explicitly:

| result | status |
|---|---|
| ppm ↔ GtC conversion | **derivation** from constants; the number carries a convention (~3%) |
| impulse response shape (exponential sum) | **parameterisation**; the coefficients are chosen |
| non-decaying fraction of the response | **structural**; it follows from carbonate chemistry operating over millennia |
| airborne fraction declining with time | **structural** consequence of a decaying response function |
| airborne fraction's numerical value | **assumption-dependent** |
| $\beta$, $\gamma$ | **parameterisations** of unresolved uptake |
| logarithmic forcing $F_{2\times}\ln(C/C_0)/\ln2$ | **derivation** for small perturbations, with $F_{2\times}$ itself a model input |
| warming per 1000 GtC | **model output**, valid over a limited range |

## 10. Assumptions and regime of validity

1. **A linear response function.** $a(t)$ assumes the sinks respond
   proportionally to the perturbation. Saturation, nutrient limitation and
   changes in ocean chemistry all break this at large perturbations.
2. **Chosen coefficients.** Every $a_i$ and $\tau_i$ is a teaching value; the
   *structure* — one fast, one intermediate, one slow, one effectively permanent
   component — is what the lesson transfers.
3. **Inventories as single well-mixed boxes.** No spatial structure, no
   permafrost dynamics, no land-use change.
4. **Equilibrium carbon budget.** Sections 7 and 8 solve an equilibrium; the
   real system is transient, and the transient response is smaller and slower.
5. **No feedbacks on $\beta$ and $\gamma$ themselves.** Both are held constant.
6. **The warming model is one-dimensional.** A single global temperature with a
   constant feedback parameter.
7. **No policy content.** The pathway is a synthetic ramp chosen for arithmetic;
   no scenario and no target is implied or evaluated.

## 11. Worked examples

### Example 1 — the conversion, and its sensitivity

$p_s/g = 1.013\times10^5/9.81 = 1.0332\times10^4\
\mathrm{kg\,m^{-2}}$; $4\pi a^2 = 5.1006\times10^{14}$ m²; so
$m_\text{atm} = 5.267\times10^{18}$ kg. With $M_C/M_\text{air} =
12.011/28.97 = 0.41460$,

$$1\ \mathrm{ppm} = 10^{-6}\times5.267\times10^{18}\times0.41460
= 2.184\times10^{12}\ \mathrm{kg} = 2.1837\ \mathrm{GtC}.$$

A 2.8% change in $m_\text{atm}$ changes the constant by 2.8% and every ppm
calculated from a GtC budget by the same factor.

### Example 2 — how long is a pulse still a pulse?

For a pulse emitted at $t=0$, the fraction remaining is $a(t)$. At 100 years,
$a = 0.20 + 0.30\mathrm{e}^{-100/3.5} + 0.30\mathrm{e}^{-100/30}
+ 0.20\mathrm{e}^{-100/400}$; the exponentials evaluate to
$3.6\times10^{-13}$, $0.0107$ and $0.1558$, so

$$a(100) = 0.20 + 0.0000 + 0.0107 + 0.1558 = 0.3665,$$

matching the table. At 1000 years: $0.20 + 0.20\mathrm{e}^{-2.5} = 0.20 + 0.0164
= 0.2164$ ✔.

### Example 3 — the airborne fraction is not a constant

At 100 years, cumulative emissions are 501.2 GtC and the atmospheric excess is
266.9 GtC, so the airborne fraction is 0.532. At 300 years, the same model and
the same pathway give $971.5/2501.2 = 0.388$. A change of a factor of 1.8 with
no change in the coefficients: the ratio's time dependence is entirely
kinematic.

## 12. Python demonstration

[`code/carbon_cycle_demo.py`](code/carbon_cycle_demo.py) prints every number
above in six labelled sections: the derivation of the ppm-to-GtC conversion with
its convention dependence; the inventories; the impulse response with the
per-time-remaining table and pulse mass balance; the ramp experiment with the
airborne-fraction trajectory and its consistency checks; the $\beta$–$\gamma$
sensitivity table; and the cumulative-emissions versus warming table with its
slope and curvature. It needs no network, runs in a fraction of a second, and
exits 0.

## 13. Exercises

Full sets with worked solutions are in
[`exercises/05-carbon-cycle-exercises.md`](exercises/05-carbon-cycle-exercises.md)
and
[`exercises/05-carbon-cycle-solutions.md`](exercises/05-carbon-cycle-solutions.md).

- **★** Compute the atmospheric mass per unit area and the total, and hence the
  GtC equivalent of 1 ppm using $M_C/M_\text{air} = 0.4146$.
- **★** Using the demonstration's impulse response, compute the fraction
  remaining at 30 years and at 400 years.
- **★★** For a pulse of 2000 GtC, compute the mass in the atmosphere and in the
  sinks at 10, 100 and 1000 years, and verify that the total is conserved.
- **★★** Using $\Delta C = (E-\gamma\Delta T)/(1+\beta)$ with
  $|\lambda| = 4.0$, $F_{2\times} = 3.7$, $C_0 = 800$ GtC, compute the airborne
  fraction and $\Delta T$ for $E = 2000$ GtC with $\beta = 1.5$,
  $\gamma = 150$.
- **★★★** The demonstration's increment per 1000 GtC falls from 0.723 to 0.408 K
  across its range. Identify which of the two sources of curvature (the
  logarithmic forcing and the $\gamma$ term) dominates at the high end, and
  describe the calculation that would separate them.

## 14. Common mistakes

1. **Quoting "the residence time of CO₂".** Section 5's table is the
   counterexample; residence time (inventory/throughput) is a different
   quantity from the decay time of a perturbation.
2. **Treating the airborne fraction as a constant.** Section 6 shows it falling
   by a factor of 1.8 with fixed coefficients.
3. **Forgetting the non-decaying part of the response.** It is what makes the
   long-horizon result different from a simple exponential decay.
4. **Confusing the ppm-to-GtC factor between sources.** A 3% convention
   difference propagates to every converted value.
5. **Reading a warming-per-1000-GtC slope as a constant.** Section 8 gives its
   range and its curvature.
6. **Treating $\beta$ and $\gamma$ as measurements.** They are
   parameterisations of unresolved uptake.
7. **Forgetting that an equilibrium budget overstates a transient response.**

## Mastery checkpoint

Complete this without notes.

> A pulse of 3000 GtC is emitted at $t=0$ into the demonstration's synthetic
> carbon cycle, and the temperature responds with $F_{2\times} = 3.7\
> \mathrm{W\,m^{-2}}$ and $|\lambda| = 4.0\ \mathrm{W\,m^{-2}K^{-1}}$.
> **(a)** Compute the atmospheric excess at 10, 100 and 1000 years from the
> impulse response.
> **(b)** State the mass in the sinks at each time and verify conservation.
> **(c)** Explain in two sentences why the atmospheric excess falls quickly at
> first and then very slowly.
> **(d)** Compute the equilibrium airborne fraction from
> $\Delta C = (E-\gamma\Delta T)/(1+\beta)$ with $\beta = 1$, $\gamma = 100$
> GtC K⁻¹, and state whether it is larger or smaller than the 100-year transient
> value, and why.
> **(e)** State one convention and one parameterisation that a reader would need
> to know to reproduce your numbers.

A worked version of (a)–(d) appears in the lesson-05
[solutions](exercises/05-carbon-cycle-solutions.md).

## Common pitfalls

- **Adding a "residence time" to a "response time".** They are different
  quantities with different definitions.
- **Fitting a single exponential to a multi-timescale response.**
- **Comparing budgets computed with different ppm conventions.**
- **Assuming sinks remain proportional at large perturbation.** They do not,
  and the linear response function cannot represent the change.
- **Quoting a carbon-budget remainder without the $\beta$ and $\gamma$ it
  assumed.**

## Related modules

- [01 Components of the Climate System and Their Timescales](01-climate-system-components.md) —
  the timescale framework, including the carbon entries of its summary table.
- [02 Feedbacks: Water Vapour, Ice-Albedo, Cloud, Carbon](02-climate-feedbacks.md) —
  the $\beta$–$\gamma$ framework in its feedback context.
- [03 Climate Sensitivity: Definitions and Estimation](03-climate-sensitivity.md) —
  the temperature side of this budget.
- [04 Natural Variability: ENSO, NAO, PDO, Solar and Volcanic](04-natural-variability.md) —
  the variability that must be separated from the forced carbon signal.
- [16-08 Climate Observations and Data Products](../08-climate-observation-and-data/README.md) —
  how concentrations and fluxes are actually measured.
- [15-01 Physical Oceanography](../../15-oceanography-marine/01-physical-oceanography/README.md) —
  the circulation that ventilates the deep ocean and sets the long sink.
- [16-09 Geophysics Applied to Climate Science](../09-geophysics-and-climate/README.md) —
  the geophysical monitoring of carbon storage.
