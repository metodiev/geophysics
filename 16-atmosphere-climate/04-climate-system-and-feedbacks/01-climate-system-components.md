---
id: 16-04-01
title: "Components of the Climate System and Their Timescales"
level: beginner
prereqs: ["16-01-02", "16-02-04"]
tags: [atmosphere, climate, climate-system, timescales, heat-capacity, ocean-heat-uptake]
---

# Components of the Climate System and Their Timescales

The climate system is not one object. It is a set of reservoirs — atmosphere,
ocean, sea ice, land surface, ice sheets, biosphere, sediments — that exchange
heat, water and carbon at different rates, and the single most useful thing to
know about each one is **how long it remembers a change**. The atmosphere
forgets a temperature anomaly in about three weeks. A 50 m ocean mixed layer
takes a year. The deep ocean takes centuries. An ice sheet takes millennia, and
its interior takes a hundred times longer than that again.

That spread is the reason two true statements can sound contradictory. A
forcing applied today produces almost all of its *fast* response within a few
years, and the rest over centuries; so "the warming so far" and "the warming
committed" are different numbers, and so are "the warming in 20 years" and "the
eventual warming". This lesson builds the arithmetic that separates them, using
only heat capacities and one response timescale per reservoir, and it ends with
the reason climate discussions are so often about *time*: the same energy
imbalance means different things depending on which reservoir is absorbing it.

All models and data in this module are **SYNTHETIC**. The depths, layer
thicknesses and temperatures below are chosen teaching values printed by
[`code/climate_system_components_demo.py`](code/climate_system_components_demo.py).
No observation of any ocean, ice sheet or atmosphere is used. The specific heats
of water and air, the latent heat of fusion, surface pressure and gravity are
standard constants; the Stefan–Boltzmann constant is exact in SI.

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** the heat capacity per unit area of the atmosphere, an ocean layer
   and an ice sheet, and **express** each as an equivalent thickness of water.
2. **Derive** the Planck feedback parameter $\lambda_0 = 4\sigma T^3$ and
   **compute** the radiative relaxation time of any reservoir as $C/\lambda_0$.
3. **Explain** why that relaxation time is a lower bound on a real response
   time.
4. **Derive** the two timescales of a coupled two-layer ocean from the
   eigenvalues of its linear system, and **obtain** the exact equilibrium from
   the same algebra.
5. **Compute** the committed but unrealised warming at a given time and explain
   its dependence on the coupling coefficient rather than on the forcing.
6. **Distinguish** the mass-balance and thermal timescales of an ice sheet and
   say which question each answers.
7. **Estimate** the heat required to melt a given thickness of ice and compare
   it with an ocean heat budget.
8. **State** which part of a response is fast, which is slow, and what sets each.

## Prerequisites

- [16-01-02 Hydrostatic Balance and Pressure-Height Relations](../01-atmospheric-structure-and-thermodynamics/02-hydrostatic-balance.md) —
  the relation $p = \rho g H$ used to convert surface pressure into an
  atmospheric mass per unit area.
- [16-02-04 Earth Energy Balance and Global Mean Temperature](../02-radiation-and-energy-balance/04-earth-energy-balance.md) —
  the top-of-atmosphere imbalance that forces every response computed here.

## 1. Intuition: the system is a set of memories

A reservoir's memory is

$$\tau \sim \frac{\text{energy it can absorb per kelvin}}
{\text{rate at which it can lose energy per kelvin}} = \frac{C}{\lambda}.$$

The numerator is a **heat capacity per unit area** (J m⁻² K⁻¹) and the
denominator a **feedback parameter** (W m⁻² K⁻¹). Both are simple to estimate,
and their ratio tells you which reservoir will have responded by the time you
look and which will still be equilibrating. Everything else in this lesson is
bookkeeping on that ratio.

The atmosphere is thin and low in heat capacity; the ocean is thick and high in
heat capacity; ice has a moderate capacity but a huge *latent* requirement to
change phase. Those three facts generate the whole timescale spectrum.

## 2. Definitions

| Term | Meaning used here |
|---|---|
| Reservoir | A subsystem treated as having a single temperature and heat capacity per unit area |
| Heat capacity per unit area $C$ | Energy needed to raise 1 m² of the reservoir by 1 K, J m⁻² K⁻¹ |
| Feedback parameter $\lambda$ | Rate of change of net top-of-atmosphere flux with surface temperature, W m⁻² K⁻¹ |
| Planck response $\lambda_0$ | The $\lambda$ of a blackbody: $4\sigma T^3$, always negative (stabilising) |
| Relaxation time $\tau$ | $C/\lambda$: the e-folding time of a temperature anomaly in that reservoir alone |
| Coupling coefficient $\gamma$ | Heat exchange rate between two reservoirs per kelvin of their temperature difference, W m⁻² K⁻¹ |
| Commitment | Warming that the system will inevitably realise given the current imbalance |

## 3. Heat capacities per unit area

### 3.1 The atmosphere

Hydrostatic balance says the mass of the atmospheric column above 1 m² is
$p_s/g$. Multiplying by the specific heat at constant pressure:

$$\boxed{\;C_\text{atm} = \frac{c_p\,p_s}{g}
= \frac{1004\times1.013\times10^5}{9.81}
= 1.0368\times10^7\ \mathrm{J\,m^{-2}K^{-1}}.\;}$$

Divided by the volumetric heat capacity of water ($\rho c_p = 1025\times3985
= 4.085\times10^6\ \mathrm{J\,m^{-3}K^{-1}}$), that is **2.54 m of water**. The
entire atmospheric column stores as much heat per kelvin as the top two and a
half metres of the ocean — a fact worth memorising, because it explains why the
ocean dominates the system's memory.

### 3.2 Water, ice and land

For a layer of thickness $h$, $C = \rho c_p h$. The demonstration prints:

| component | depth / thickness | $C$ (J m⁻² K⁻¹) | $C/C_\text{atm}$ |
|---|---|---|---|
| atmosphere (whole column) | 1 atm | $1.0368\times10^7$ | 1.00 |
| ocean mixed layer | 50 m | $2.0423\times10^8$ | 19.70 |
| ocean mixed layer | 100 m | $4.0846\times10^8$ | 39.40 |
| ocean mixed layer | 200 m | $8.1692\times10^8$ | 78.80 |
| ocean | 1000 m | $4.0846\times10^9$ | 393.98 |
| ocean | 3800 m | $1.5522\times10^{10}$ | 1497.14 |
| ice sheet ($\rho = 917$, $c = 2100$) | 1000 m | $1.9257\times10^9$ | 185.74 |
| ice sheet | 3000 m | $5.7771\times10^9$ | 557.23 |
| land, 10 m skin ($\rho c_p = 2\times10^6$) | 10 m | $2.0000\times10^7$ | 1.93 |

A 50 m mixed layer already outranks the whole atmosphere by a factor of twenty,
and the full ocean by three orders of magnitude. The land "skin" that responds
to a season is comparable to the atmosphere. Every statement about "the climate
response time" is therefore a statement about *which reservoir* is meant.

## 4. Radiative relaxation times

A body at temperature $T$ radiates $\sigma T^4$. For a small perturbation,

$$\lambda_0 = \frac{\mathrm{d}(\sigma T^4)}{\mathrm{d}T} = 4\sigma T^3
= 4(5.670374419\times10^{-8})(288)^3
= 5.418\ \mathrm{W\,m^{-2}K^{-1}},$$

using the chosen reference temperature $T = 288$ K. Then $\tau = C/\lambda_0$:

| component | $C$ (J m⁻² K⁻¹) | $\tau = C/\lambda_0$ | in |
|---|---|---|---|
| atmosphere | $1.0368\times10^7$ | $1.9135\times10^6$ s | 22.1 d |
| ocean, 50 m | $2.0423\times10^8$ | $3.7694\times10^7$ s | 1.20 yr |
| ocean, 100 m | $4.0846\times10^8$ | $7.5388\times10^7$ s | 2.39 yr |
| ocean, 3800 m | $1.5522\times10^{10}$ | $2.8647\times10^9$ s | 90.84 yr |
| ice sheet, 3000 m | $5.7771\times10^9$ | $1.0663\times10^9$ s | 33.81 yr |

**Read the last column with care.** These are *lower bounds* on a real response
time, for three reasons: the reservoir must exchange heat with its neighbours to
radiate at all; positive feedbacks make the effective $\lambda$ smaller and
every $\tau$ longer; and the ice entry is not even a radiation problem —
3 km of ice cannot radiate its thermal anomaly from its interior, it must
conduct it to the surface, and Section 6 shows that conduction is the binding
constraint.

## 5. Two reservoirs in contact: the two-layer ocean

### 5.1 The model and its eigenvalues

Take a mixed layer of capacity $C_m$ coupled to a deep ocean of capacity $C_d$
by $\gamma$, with a prescribed forcing $F$:

$$C_m\frac{\mathrm{d}T_m}{\mathrm{d}t} = F - \lambda T_m - \gamma(T_m - T_d),
\qquad
C_d\frac{\mathrm{d}T_d}{\mathrm{d}t} = +\gamma(T_m - T_d).$$

In matrix form $\dot{\mathbf X} = \mathbf M\mathbf X + \mathbf f$ with

$$\mathbf M = \begin{pmatrix}
-(\lambda+\gamma)/C_m & \gamma/C_m\\
\gamma/C_d & -\gamma/C_d\end{pmatrix},
\qquad \mathbf f = \begin{pmatrix} F/C_m\\ 0\end{pmatrix}.$$

The two timescales are the reciprocals of the eigenvalues of $\mathbf M$, which
for $C_d\gg C_m$ separate into a **fast** mixed-layer mode and a **slow**
deep-ocean mode. Their ratio is $\approx C_d(\lambda+\gamma)/(C_m\gamma)$, so a
thick deep ocean and a weak coupling produce a very stiff system: the
demonstration's numbers give $1.058$ yr and $700.1$ yr, a ratio of 660.

### 5.2 The equilibrium, and what a commitment is

Setting the derivatives to zero gives the exact equilibrium

$$\mathbf X_\text{eq} = -\mathbf M^{-1}\mathbf f
\quad\Longrightarrow\quad
T_m = T_d = \frac{F}{\lambda} = \frac{3.7}{5.418} = 0.6829\ \mathrm{K}.$$

Both boxes must arrive at the *same* temperature, because at equilibrium the
coupling term carries no heat. That equality is a check on the algebra, not on
the ocean. The demonstration prints the exact exponential solution:

| time (yr) | $T_m$ (K) | $T_d$ (K) | $T_m/T_\text{eq}$ | $T_d/T_\text{eq}$ |
|---|---|---|---|---|
| 1 | 0.3696 | 0.0003 | 0.541 | 0.001 |
| 2 | 0.5134 | 0.0011 | 0.752 | 0.002 |
| 5 | 0.5997 | 0.0038 | 0.878 | 0.006 |
| 10 | 0.6056 | 0.0087 | 0.887 | 0.013 |
| 20 | 0.6067 | 0.0182 | 0.889 | 0.027 |
| 50 | 0.6099 | 0.0461 | 0.893 | 0.068 |
| 100 | 0.6150 | 0.0900 | 0.901 | 0.132 |
| 200 | 0.6240 | 0.1689 | 0.914 | 0.247 |
| 500 | 0.6445 | 0.3481 | 0.944 | 0.510 |
| 1000 | 0.6641 | 0.5190 | 0.973 | 0.760 |
| 2000 | 0.6784 | 0.6436 | 0.993 | 0.943 |
| 5000 | 0.6828 | 0.6824 | 1.000 | 0.999 |

At 10 years the surface has done 88.7% of its eventual work while the deep
ocean has done 1.3%. The difference between the two columns *is* the
commitment: warming that the energy already in the system will produce, and
that no change of forcing can avoid unless it can be radiated first.

The fast fraction has a closed form. On the fast mode the deep ocean is
effectively fixed, so $F = (\lambda+\gamma)T_m$ and

$$\frac{T_m^\text{fast}}{T_\text{eq}} = \frac{\lambda}{\lambda+\gamma}
= \frac{5.418}{6.118} = 0.8856 .$$

The demonstration's 10-year value is 0.8868, and the small excess is the slow
mode already contributing. **The transient response is set by $\gamma$**, not by
the forcing: the same forcing with a larger $\gamma$ gives a *cooler* surface at
every time and the same equilibrium.

## 6. Ice sheets: two timescales, both called "the" one

- **Mass balance:** $\tau_\text{mass} = H/\dot b$ with $H$ the thickness and
  $\dot b$ the accumulation rate. For $H = 3000$ m and $\dot b = 0.3$ m yr⁻¹,
  $\tau_\text{mass} = 10^4$ yr; for a 3000 m sheet accumulating at 1 m yr⁻¹,
  3000 yr.
- **Thermal diffusion:** $\tau_\text{therm} = H^2/\kappa$ with
  $\kappa = k/(\rho c) = 2.2/(917\times2100) = 1.1424\times10^{-6}\ \mathrm{m^2\,s^{-1}}$,
  giving $2.5\times10^5$ yr through 3 km.

The demonstration's table spans 1000–30000 yr for the mass-balance timescale and
$2.8\times10^4$–$2.5\times10^5$ yr for the thermal one. Both are correct answers
to different questions — "how fast can the shape change?" versus "how fast can
the interior temperature change?" — and quoting one without saying which is a
category error.

Ice also has a **latent** requirement that dwarfs its sensible heat capacity.
Melting 1000 m of ice per unit area takes

$$L_f\rho_i h = (3.34\times10^5)(917)(1000) = 3.063\times10^{11}\
\mathrm{J\,m^{-2}},$$

which is **75 K worth** of the heat capacity of a 1 km ocean column
($4.08\times10^9$ J m⁻² K⁻¹). No plausible ocean temperature change supplies
that; what supplies it is a sustained energy *flux*. Heat budgets, not
temperatures, decide melt.

## 7. The system as coupled memories

| component | timescale | what sets it |
|---|---|---|
| atmosphere (radiative) | ~3 weeks | $C/(4\sigma T^3)$ |
| land surface skin | hours to days | diurnal energy balance |
| ocean mixed layer | months to 1 yr | $C_m/\lambda$ |
| upper ocean / thermocline | 1–10 yr | wind and buoyancy coupling |
| deep ocean | $10^2$–$10^3$ yr | $C_d/\gamma$ |
| sea ice | months to years | growth and melt balance |
| ice sheets (mass balance) | $10^3$–$10^4$ yr | $H/\dot b$ |
| ice sheets (thermal) | $10^5$ yr | $H^2/\kappa$ |
| carbon cycle (atmosphere) | $10^1$–$10^2$ yr | ocean and land uptake |
| carbon cycle (carbonate) | $10^3$–$10^4$ yr | ocean chemistry |
| carbon cycle (silicate) | $10^5$ yr | weathering |

Every entry is a model or a scaling and each is conditional on the mechanism in
the last column. The point of the table is the spread — seven orders of
magnitude — and the consequence: **a statement of the form "the climate will
respond in $X$ years" is incomplete unless $X$'s mechanism is named.**

## 8. Assumptions and regime of validity

1. **One temperature per reservoir.** A box model cannot represent a vertical
   or horizontal structure, so it cannot represent, for example, the difference
   between polar amplification and tropical warming.
2. **Linear feedback.** $\lambda$ is treated as a constant. It is a derivative,
   and it changes as the climate moves (see [16-04-02](02-climate-feedbacks.md)).
3. **Chosen reservoir geometry.** A 50 m mixed layer and a 3350 m deep ocean are
   teaching values. Every timescale in Sections 5 and 7 scales with them.
4. **Constant $\gamma$.** The coupling between mixed layer and deep ocean is
   itself a parameterisation of overturning and diffusion; it is not a
   measurable constant of nature.
5. **No ice, no carbon, no biology** are coupled in Sections 3–6. Those add
   reservoirs with their own capacities and couplings.
6. **No spatial transport.** Every number here is a global or per-unit-area
   average; regional responses can differ in sign.

## 9. Worked examples

### Example 1 — a heat capacity and a timescale from scratch

$$C_\text{atm} = \frac{c_pp_s}{g} = \frac{1004\times1.013\times10^5}{9.81}
= 1.0368\times10^7\ \mathrm{J\,m^{-2}K^{-1}},$$

$$\tau_\text{atm} = \frac{C_\text{atm}}{4\sigma T^3}
= \frac{1.0368\times10^7}{5.418}
= 1.9135\times10^6\ \mathrm{s} = 22.1\ \mathrm{d}.$$

Equivalent water thickness:
$C_\text{atm}/(\rho_wc_{p,w}) = 1.0368\times10^7/4.085\times10^6
= 2.538$ m.

### Example 2 — the fast and slow responses

With $\lambda = 5.418$, $\gamma = 0.7$ W m⁻² K⁻¹ and $F = 3.7$ W m⁻²:

- fast (quasi-steady, deep ocean unchanged):
  $T_m = F/(\lambda+\gamma) = 3.7/6.118 = 0.6048$ K, which is
  $\lambda/(\lambda+\gamma) = 88.6\%$ of equilibrium;
- equilibrium: $T = F/\lambda = 0.6829$ K;
- committed but unrealised at 10 years: $0.6829 - 0.6056 = 0.077$ K, i.e. 11.3%
  of the eventual response, which arrives over centuries.

### Example 3 — the heat needed to melt ice

For a 1 m thickness: $L_f\rho_i = 3.34\times10^5\times917
= 3.063\times10^8\ \mathrm{J\,m^{-2}}$. Divided by the mixed layer's heat
capacity ($2.0423\times10^8$ J m⁻² K⁻¹) that is 1.5 K of the entire 50 m mixed
layer per metre of ice — which is why ice melt is a slow, flux-limited process
and not a threshold crossed when the water reaches some temperature.

## 10. Python demonstration

[`code/climate_system_components_demo.py`](code/climate_system_components_demo.py)
prints every number above in five labelled sections: heat capacities and their
ratios; the Planck relaxation times; the two-layer ocean with its eigenvalues,
exact equilibrium, exponential response and commitment; the two ice-sheet
timescales and the melt heat budget; and the summary table. It uses the exact
matrix exponential rather than time stepping, because the two ocean modes
differ by a factor of 660 and no single explicit step size resolves both. It
runs in a fraction of a second, needs no network, and exits 0.

## 11. Exercises

Full sets with worked solutions are in
[`exercises/01-climate-system-components-exercises.md`](exercises/01-climate-system-components-exercises.md)
and
[`exercises/01-climate-system-components-solutions.md`](exercises/01-climate-system-components-solutions.md).

- **★** Compute $C$ and $\tau$ for a 200 m ocean layer, and express $C$ as an
  equivalent thickness of water and as a multiple of $C_\text{atm}$.
- **★** Compute the heat required to raise a 50 m mixed layer by 0.6 K, and
  state how long the Planck response would take to radiate it away.
- **★★** Derive the fast fraction $\lambda/(\lambda+\gamma)$ and evaluate it for
  $\gamma = 1.0$ and $\gamma = 0.4$ W m⁻² K⁻¹, stating which gives the larger
  transient warming.
- **★★** Show that the equilibrium temperature of both boxes is $F/\lambda$ by
  setting both derivatives to zero, and state why the coupling term must vanish
  at equilibrium.
- **★★★** A colleague says the deep ocean's 700-year timescale means the
  climate responds on 700-year timescales. Using the table in Section 5.2,
  state precisely what is wrong with the claim and what the correct statement
  is.

## 12. Common mistakes

1. **Comparing heat capacities without dividing by area.** $C$ here is per
   square metre; total heat capacities depend on the reservoir's extent.
2. **Treating $\tau = C/\lambda_0$ as the response time.** It is a lower bound
   that ignores transport, coupling and feedbacks.
3. **Using one timescale for the ocean.** There are at least two, and they
   differ by a factor of hundreds.
4. **Confusing the equilibrium response with the realised one.** Section 5.2's
   two columns are the whole point.
5. **Quoting "the ice-sheet timescale".** Section 6 has two, and they differ by
   an order of magnitude depending on the question.
6. **Assuming melt happens when the water is warm enough.** It happens when the
   heat *flux* delivers $3.063\times10^{11}$ J m⁻² for 1000 m of ice.

## Mastery checkpoint

Complete this without notes.

> A slab ocean model has a 75 m mixed layer over a deep ocean of capacity
> $C_d = 1.2\times10^{10}$ J m⁻² K⁻¹, coupled by $\gamma = 0.8\
> \mathrm{W\,m^{-2}K^{-1}}$, with $\lambda = 5.418$ W m⁻² K⁻¹ and a step forcing
> of 3.7 W m⁻².
> **(a)** Compute the mixed layer's heat capacity and its Planck relaxation time.
> **(b)** Compute the equilibrium temperature $F/\lambda$ and the fast
> quasi-steady temperature $F/(\lambda+\gamma)$, and express the latter as a
> fraction of the former.
> **(c)** State whether the ratio $C_d/C_m$ is larger or smaller than in the
> lesson, and what that does to the slow timescale.
> **(d)** Compute the heat needed to melt 2 m of ice per unit area and compare
> it with the mixed layer's heat capacity.
> **(e)** State one assumption in this model that limits its use for a statement
> about polar amplification.

A worked version of (a)–(c) appears in the lesson-01
[solutions](exercises/01-climate-system-components-solutions.md).

## Common pitfalls

- **Forgetting that $\lambda$ is a derivative.** It is evaluated at a
  temperature; it changes with the state.
- **Adding timescales.** Coupled reservoirs do not have additive timescales;
  they have eigenvalues, and the system's response is a sum of exponentials.
- **Reading a per-unit-area number as a global one.** Multiply by the area when
  a total energy matters, and remember the ocean covers about 71% of the surface.
- **Ignoring the latent heat term in any ice calculation.**
- **Assuming a single deep-ocean box represents the thermocline.** The real
  ocean's uptake has structure that one box cannot carry.

## Related modules

- [02 Feedbacks: Water Vapour, Ice-Albedo, Cloud, Carbon](02-climate-feedbacks.md) —
  what determines $\lambda$, and why it is not a constant.
- [03 Climate Sensitivity: Definitions and Estimation](03-climate-sensitivity.md) —
  how $F$, $\lambda$ and $\gamma$ combine into equilibrium and transient
  sensitivities.
- [04 Natural Variability: ENSO, NAO, PDO, Solar and Volcanic](04-natural-variability.md) —
  variability on the timescales catalogued here.
- [05 The Carbon Cycle: Reservoirs, Fluxes and Perturbations](05-carbon-cycle.md) —
  the carbon reservoirs whose timescales appear in the Section 7 table.
- [16-02 Radiation and Energy Balance](../02-radiation-and-energy-balance/README.md) —
  where the forcing $F$ comes from.
- [15-01 Physical Oceanography](../../15-oceanography-marine/01-physical-oceanography/README.md) —
  the ocean circulation that makes $\gamma$ a parameterisation rather than a
  constant.
- [12-03 Geotherms and the Earth's Heat Budget](../../12-global-geophysics-interior/03-geotherms-and-heat-budget/README.md) —
  the same heat-budget reasoning applied to the solid Earth.
