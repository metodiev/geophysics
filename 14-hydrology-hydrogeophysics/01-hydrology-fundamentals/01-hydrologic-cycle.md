---
id: 14-01-01
title: "The Hydrologic Cycle and Water Balance"
level: beginner
prereqs: ["01-01-03", "02-06-01", "04-06-04"]
tags: [hydrology, hydrogeophysics, water-balance, catchment, baseflow, residence-time]
---

# The Hydrologic Cycle and Water Balance

Before any geophysical method can be pointed at groundwater, someone has to know
what the water is doing and how much of it there is. That accounting is the
**water balance**: a statement that water is conserved in a defined region over a
defined time. Everything else in this folder — porosity, permeability, head,
well tests, salinity, resistivity — is a refinement of one of the terms.

**All models and data in this module are SYNTHETIC.** The catchment, the rainfall
series and the discharge series used below are invented teaching values. They are
not measurements of any real basin, and no published inventory is quoted.

## Learning objectives

By the end of this lesson you will be able to:

1. **Draw** the hydrologic cycle as stores and fluxes, and **name** the boundary
   of a control volume for which a balance is being written.
2. **Write** the water-balance equation $P = ET + Q + \Delta S$ and **state** the
   sign convention and the units of every term.
3. **Convert** a depth of water in millimetres to a volume in cubic metres over a
   stated catchment area, and explain the exact identity $1\ \mathrm{mm}$ over
   $1\ \mathrm{km^2} = 1000\ \mathrm{m^3}$.
4. **Compute** a runoff coefficient, an evaporative index and a mean residence
   time from a closed balance.
5. **Quantify** the error amplification that makes the storage-change term
   $\Delta S$ the least reliable number in a water balance.
6. **Separate** baseflow from a hydrograph with a stated filter time constant,
   and **explain** why the baseflow index is a definition rather than a
   measurement.

## Prerequisites

- [01-01-03 Units and Dimensional Analysis](../../01-mathematics/01-arithmetic/03-units-and-dimensional-analysis.md)
  — prefixes, unit conversion and the habit of carrying units through arithmetic.
- [02-06-01 Fluid Statics](../../02-physics/06-fluid-mechanics/01-fluid-statics.md)
  — pressure in a fluid, which becomes hydraulic head in
  [03 Hydraulic Head and Darcy's Law](03-hydraulic-head-darcy.md).
- [04-06-04 Aquifer Types and Groundwater Occurrence](../../04-earth-science-geology/06-petroleum-and-mineral-systems/04-groundwater-aquifers.md)
  — the geological vocabulary of aquifers that this module quantifies.

---

## 1. The cycle as stores and fluxes

The hydrologic cycle is not a picture of arrows; it is a **balance sheet**. Water
sits in stores (oceans, ice, groundwater, soil moisture, lakes, rivers,
atmosphere) and moves between them along fluxes (precipitation, evaporation,
transpiration, runoff, infiltration, recharge, groundwater discharge). The
physical content is one sentence long:

> In a region and over a time interval, the change in storage equals what flows in
> minus what flows out.

Choose the region — a catchment above a river gauge, a soil column, an aquifer, a
continent — and the balance becomes an equation in numbers. Choose it badly, and
the balance silently omits a flux. The single most common error in a water balance
is not arithmetic; it is a control volume whose boundary cuts through a flow path
nobody counted.

For a **catchment** (a topographic drainage divide, closed except for the river
outlet and the atmosphere), the balance over a year is:

$$P = ET + Q + \Delta S,$$

with $P$ precipitation, $ET$ evapotranspiration, $Q$ streamflow at the outlet, and
$\Delta S$ the change in water stored in the catchment (soil moisture, groundwater,
snow, surface water). This is the equation used for the rest of the lesson.

## 2. Definitions, symbols and units

Hydrogeology measures water in **depth** units (mm, m), not litres, because the
quantity of interest is how much water is available per unit area. Table 1 fixes
the vocabulary.

| Quantity | Symbol | Unit | Comment |
|---|---|---|---|
| precipitation | $P$ | mm yr$^{-1}$ | a depth rate, not a volume |
| evapotranspiration | $ET$ | mm yr$^{-1}$ | evaporation + plant transpiration |
| streamflow (runoff) | $Q$ | mm yr$^{-1}$ | depth equivalent discharged at the outlet |
| storage change | $\Delta S$ | mm yr$^{-1}$ | positive when the region gains water |
| catchment area | $A$ | km$^2$ | 1 km$^2$ = $10^6$ m$^2$ |
| volume | $V$ | m$^3$ | $V = \text{depth} \times A$ |
| discharge (rate) | $Q_v$ | m$^3$ s$^{-1}$ | what a gauging station actually measures |
| runoff coefficient | $Q/P$ | – | dimensionless, 0 to 1 |
| residence time | $\tau$ | yr or d | store volume divided by throughput |

The exact conversion that makes depth units practical:

$$1\ \mathrm{mm} \text{ over } 1\ \mathrm{km^2}
= 10^{-3}\ \mathrm{m} \times 10^{6}\ \mathrm{m^2}
= 10^{3}\ \mathrm{m^3}.$$

So "10 mm of rain over 250 km$^2$" is $2.5 \times 10^{6}\ \mathrm{m^3}$ of water,
with no lookup table required. Guard this identity: mixing mm yr$^{-1}$ with
m$^3$ s$^{-1}$ without converting is the second most common error in a balance,
and a factor of $10^3$ hides inside it.

For completeness, a discharge of $Q$ mm yr$^{-1}$ over an area $A$ km$^2$ is a
volumetric rate of

$$Q_v = \frac{Q \times 10^{-3}\ \mathrm{m} \times A \times 10^{6}\ \mathrm{m^2}}
{3.15576 \times 10^{7}\ \mathrm{s}}
\ \; \mathrm{m^3\,s^{-1}},$$

using 1 yr = 365.25 d = $3.15576 \times 10^{7}$ s (a defined constant, since the
Julian year is exactly 365.25 d of 86400 s).

## 3. Why the balance equation has this form

Let the control volume be the catchment, bounded below by an impermeable base of
the modelled system and above by the atmosphere. Conservation of mass for water
over a time interval $\Delta t$ states

$$\underbrace{\text{mass in}}_{\text{precipitation}}
- \underbrace{\text{mass out}}_{\text{ET} + \text{streamflow}}
= \Delta(\text{mass stored}).$$

Dividing by $\rho_w A$ and by the interval converts every term into a depth. Water
is treated as incompressible here — a density change of $1$ part in $10^{4}$
corresponds to roughly $2\ \mathrm{K}$ of warming (the volumetric thermal
expansion of liquid water near $20\ ^\circ\mathrm{C}$ is about
$2 \times 10^{-4}\ \mathrm{K^{-1}}$), and a balance written in mm yr$^{-1}$
cannot resolve that. The assumption is that the same $\rho_w = 1000\
\mathrm{kg\,m^{-3}}$ converts every term, which makes the mass balance
indistinguishable from a volume balance.

Three assumptions are therefore baked into the equation, and each can fail:

1. **The boundary is closed.** Groundwater flowing across the topographic divide
   is a flux nobody measured. Karst and fractured systems routinely break this.
2. **The time interval is long enough.** Over one storm, a catchment can store or
   release water, so $\Delta S \neq 0$; over many years, $\Delta S$ is usually
   small compared with $P$, which is what makes the long-term balance useful.
3. **The terms are independent measurements.** They are not: $Q$ is measured at a
   gauge, $P$ at a few rain gauges, $ET$ usually by a model, and $\Delta S$ almost
   never directly. Section 5 shows the price of that.

## 4. Worked example — closing the balance of a synthetic catchment

**Synthetic catchment** (chosen teaching values, not a real basin):
$A = 250\ \mathrm{km^2}$, $P = 850\ \mathrm{mm\,yr^{-1}}$,
$ET = 480\ \mathrm{mm\,yr^{-1}}$, $Q = 320\ \mathrm{mm\,yr^{-1}}$.

**Step 1 — the residual.** With $P$, $ET$ and $Q$ given, the balance *defines*
$\Delta S$:

$$\Delta S = P - ET - Q = 850 - 480 - 320 = +50\ \mathrm{mm\,yr^{-1}}.$$

The positive sign says the catchment gained $50\ \mathrm{mm}$ of water this year —
groundwater levels rose, or snow accumulated, or soil moisture increased.

**Step 2 — the ratios.** Runoff coefficient $Q/P = 320/850 = 0.376$;
evaporative index $ET/P = 480/850 = 0.565$. The two must sum with
$\Delta S/P = 50/850 = 0.059$ to 1:
$0.376 + 0.565 + 0.059 = 1.000$. This is a useful arithmetic check on any published
balance before believing it.

**Step 3 — volumes.** With $1\ \mathrm{mm}$ over $1\ \mathrm{km^2} = 10^3\
\mathrm{m^3}$:

$$V_P = 850 \times 10^{-3} \times 250 \times 10^{6}
= 2.125 \times 10^{8}\ \mathrm{m^3\,yr^{-1}},$$
$$V_Q = 320 \times 10^{-3} \times 250 \times 10^{6}
= 8.00 \times 10^{7}\ \mathrm{m^3\,yr^{-1}},$$
$$V_{\Delta S} = 50 \times 10^{-3} \times 250 \times 10^{6}
= 1.25 \times 10^{7}\ \mathrm{m^3\,yr^{-1}}.$$

**Step 4 — as a mean discharge.** $8.00 \times 10^{7}\ \mathrm{m^3\,yr^{-1}}
/ 3.15576 \times 10^{7}\ \mathrm{s\,yr^{-1}} = 2.535\ \mathrm{m^3\,s^{-1}}$. A
gauging station on this synthetic river would read about $2.54\
\mathrm{m^3\,s^{-1}}$ on average, i.e. $2535\ \mathrm{L\,s^{-1}}$.

**What the numbers do and do not say.** They say nothing about depth to water,
storage, or whether the $+50\ \mathrm{mm}$ is in soil or in rock. A balance is a
constraint on fluxes, not an image of the subsurface. Turning it into an image is
the job of the geophysical methods in
[module 14-02](../02-hydrogeophysics-methods/README.md).

## 5. Worked example — why $\Delta S$ is fragile

Suppose each large term carries the error a real field campaign might have: 5% on
$P$, 10% on $ET$ (evapotranspiration is rarely known better), 5% on $Q$. Because
$\Delta S = P - ET - Q$ is a **difference**, the absolute errors do not shrink with
the residual; they add in quadrature or, worst-case, linearly.

| Term | Value (mm yr$^{-1}$) | Assumed error | Shift in $\Delta S$ | Shift as % of $\Delta S$ |
|---|---|---|---|---|
| $P$ | 850 | $\pm$5% = $\pm$42.5 | $+42.5$ | 85% |
| $ET$ | 480 | $\pm$10% = $\pm$48.0 | $-48.0$ | 96% |
| $Q$ | 320 | $\pm$5% = $\pm$16.0 | $-16.0$ | 32% |

Read the third column as: if $P$ is really 5% higher, the inferred storage gain
doubles. **A single 5% error in precipitation is 85% of the quantity being
reported.** The lesson is quantitative, not rhetorical: for a term as small as
$\Delta S$, the balance equation does not measure storage change, it only
constrains it. To get $\Delta S$ to 6% you would have to measure $Q$ to 0.32% —
better than most gauges, and impossible for $ET$ from a water balance at all.

The practical response is to break the closure: measure one term independently.
Repeat surveys of a water table measure $\Delta S$ in the saturated zone directly;
[06 Microgravity and Satellite Gravity for Water Storage Change](../02-hydrogeophysics-methods/06-gravity-for-groundwater.md)
measures it from outside the catchment entirely. Neither is exact, but each turns
one unknown into a measurement, which is the only real cure for the cancellation.

## 6. Residence time — how long water stays

For a store in steady state, the **mean residence time** (or turnover time) is the
stored volume divided by the throughput:

$$\tau = \frac{V}{Q_v}.$$

**Synthetic example.** The catchment's groundwater store is
$V = 1.5 \times 10^{8}\ \mathrm{m^3}$ and the annual discharge is
$8.0 \times 10^{7}\ \mathrm{m^3\,yr^{-1}}$:

$$\tau = \frac{1.5 \times 10^{8}}{8.0 \times 10^{7}}
= 1.875\ \mathrm{yr},
\qquad 1.875\ \mathrm{yr} \times 365.25\ \mathrm{d\,yr^{-1}}
= 684.8\ \mathrm{d}.$$

Interpretation: on average a molecule of water spends about 1.9 years in
groundwater before reaching the river. Residence time is the single best
one-number summary of an aquifer's vulnerability — a contaminant released into a
store with $\tau = 20$ yr has two decades to travel before it reaches a receptor,
and two decades in which to be detected.

Two cautions. First, $\tau = V/Q$ is a mean: the distribution of ages in a real
aquifer is broad, and a tracer (chloride, tritium, a noble gas) measures a
different moment of that distribution than $V/Q$ does. Second, $V$ here is the
*drainable* or *mobile* volume; if $V$ is taken as total water in the rock, $\tau$
is inflated by the ratio of total to mobile porosity, which for a clay-rich unit
can be an order of magnitude or more. State which $V$ you used.

## 7. Hydrographs, baseflow and a warning about definitions

A river responds to rain quickly and then decays slowly. The part of the flow that
comes from groundwater discharge is called **baseflow**; the rest is stormflow or
quickflow. Separating them matters because baseflow is a direct measurement of
groundwater discharge and therefore the term $Q$ in the balance is really two
terms with different physics.

The demonstration uses a **first-order low-pass filter** with a stated time
constant $\tau_f$: the baseflow estimate is the solution of

$$h(t) = e^{-\Delta t/\tau_f}\,h(t-\Delta t) + \left(1 - e^{-\Delta t/\tau_f}\right) Q(t),
\qquad Q_b(t) = \min\big(h(t),\, Q(t)\big).$$

Applied to a synthetic daily series of 365 days (mean precipitation
$4.02\ \mathrm{mm\,d^{-1}}$, mean discharge $1.575\ \mathrm{mm\,d^{-1}}$, peak
$3.399\ \mathrm{mm\,d^{-1}}$, annual total $574.8\ \mathrm{mm}$ — a separate
synthetic series from the annual balance above), the baseflow index depends
strongly on the filter constant:

| $\tau_f$ (d) | baseflow index | baseflow (mm yr$^{-1}$) | stormflow (mm yr$^{-1}$) |
|---|---|---|---|
| 5 | 0.950 | 545.8 | 29.0 |
| 10 | 0.902 | 518.5 | 56.3 |
| 30 | 0.756 | 434.7 | 140.0 |
| 60 | 0.639 | 367.1 | 207.7 |
| 120 | 0.525 | 301.8 | 273.0 |

The baseflow index moves from 0.53 to 0.95 — a factor of 1.8 — **without any data
changing**. Baseflow is a *definition*, not an observable. The honest way to use it
is to fix $\tau_f$ from an independent fact: the recession constant of the
catchment. Section 8 shows how to measure that constant from the data.

## 8. Verification — measuring the recession constant

Between storms, discharge decays. If the catchment behaves as a single linear
reservoir, $Q(t) = Q_0 e^{-t/\tau}$, so a plot of $\ln Q$ against $t$ is a straight
line of slope $-1/\tau$. Fitting the longest clean recession in the synthetic
series (days 178 to 216, 39 days) gives slope $-0.03232\ \mathrm{d^{-1}}$, hence

$$\tau_{\text{fit}} = \frac{1}{0.03232} = 30.94\ \mathrm{d}$$

against a true storage constant of $30.00\ \mathrm{d}$ in the model that generated
the data: a **3.1% error**, and in the right direction to be explained by the
window not being perfectly rain-free. The implied drainable storage,
$\tau_{\text{fit}} \times \bar{Q} = 30.94 \times 1.575 = 48.72\ \mathrm{mm}$, is
the depth of water the catchment can release from storage per unit of its
recession.

This is the pattern to adopt everywhere in this folder: **fit a constant to data,
then check it against a quantity you already know.** Here the model's own
constant is the answer key; in the field, an independent aquifer test or a
geophysical estimate plays that role.

## 9. Python demonstration

`code/hydrologic_cycle_demo.py` performs all of the above and prints labelled
results with units. It:

1. closes the annual balance and reports the residual, the two ratios, the
   volumes and the mean discharge in m$^3$ s$^{-1}$;
2. tabulates the effect of a stated error in $P$, $ET$ and $Q$ on $\Delta S$;
3. prints the mm-to-m$^3$ conversion table;
4. computes the residence time of the synthetic store;
5. separates baseflow for five filter constants and reports the baseflow index;
6. recovers the storage constant from a recession by least squares
   ($30.94\ \mathrm{d}$ against $30.00\ \mathrm{d}$).

```bash
cd 14-hydrology-hydrogeophysics/01-hydrology-fundamentals/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python hydrologic_cycle_demo.py
```

## 10. Assumptions and regime of validity

1. **Closed control volume.** Flow across the boundary (inter-catchment
   groundwater, imported/exported water, river regulation) must be zero or
   quantified. In karst, assume it is not zero until shown otherwise.
2. **Incompressible, constant-density water.** Safe for the $10^{-4}$-level
   accuracy of a mm yr$^{-1}$ balance; not safe in a geothermal or density-driven
   problem (see [05 Groundwater Chemistry and Salinity](05-groundwater-chemistry.md)).
3. **The interval is long relative to the store's memory.** One year is shorter
   than the residence time of a deep aquifer, so an annual $\Delta S$ is a
   transient, not a trend; several years are needed to see a trend.
4. **Areal averages are meaningful.** A few rain gauges represent 250 km$^2$ only
   in the sense of an average; orographic gradients make that assumption worth
   several per cent, i.e. comparable with $\Delta S$ itself.
5. **Precipitation is the only input.** Snowmelt, irrigation return flow, sewage
   effluent and inter-basin transfer are extra inputs that must be added
   explicitly.
6. **The linear-reservoir recession model** used in Section 8 fails on karst
   springs (which often show a two-slope or exponential-plus-linear recession) and
   on catchments where ET continues to draw from storage during the recession.

## Mastery checkpoint

A neighbouring synthetic catchment has $A = 400\ \mathrm{km^2}$,
$P = 700\ \mathrm{mm\,yr^{-1}}$, $Q = 210\ \mathrm{mm\,yr^{-1}}$ and a measured
storage gain of $80\ \mathrm{mm\,yr^{-1}}$ from repeat water-level surveys.

**(a)** Compute $ET$ from the balance and the three ratios $Q/P$, $ET/P$,
$\Delta S/P$; verify they sum to 1. **(b)** Convert $P$ and $Q$ to
m$^3$ s$^{-1}$. **(c)** If the storage estimate could be wrong by
$\pm 20\ \mathrm{mm}$, what range of $ET$ is consistent with the balance?
**(d)** The mean residence time is claimed as 4.2 yr; what stored volume in
m$^3$ does that imply, and is it plausible given the annual discharge?
**(e)** A colleague reports a baseflow index of 0.85 with no filter constant
quoted. What single question do you ask?

Worked answers are in the exercises below; part (e) is the one that matters.

## Common pitfalls

1. **Mixing depth and volume.** Reporting $Q$ as $2.5\ \mathrm{m^3\,s^{-1}}$ in a
   balance written in mm yr$^{-1}$. Convert, and carry the units through.
2. **Quoting $\Delta S$ with one significant figure at best.** A residual of two
   large terms inherits their errors amplified; see Section 5.
3. **A control volume that leaks.** Inter-catchment groundwater flow is invisible
   in the balance and common in karst and faulted terrain.
4. **Treating one year as a trend.** Groundwater storage responds to multi-year
   rainfall cycles; a single positive $\Delta S$ is not recovery.
5. **Reporting a baseflow index without the filter definition.** The number is
   meaningless without the time constant and the filter equation.
6. **Confusing residence time with travel time.** $\tau = V/Q$ is a mean for the
   whole store; a particle's travel time depends on its path.

## Related modules

- [02 Hydrogeophysical Methods](../02-hydrogeophysics-methods/README.md) — how the
  stores and fluxes of this lesson are actually imaged.
- [02 Aquifers, Porosity, Permeability and Storativity](02-aquifer-types-and-properties.md) —
  the rock properties that give $V$ and $\Delta S$ a geological meaning.
- [04-06-04 Aquifer Types and Groundwater Occurrence](../../04-earth-science-geology/06-petroleum-and-mineral-systems/04-groundwater-aquifers.md) —
  the geological classification underlying the store.
- [15-oceanography-marine](../../15-oceanography-marine/README.md) — the largest
  store in the cycle, and where most runoff eventually goes.
- [16-atmosphere-climate](../../16-atmosphere-climate/README.md) — the
  atmospheric store whose fluxes set $P$ and $ET$.

## Code and exercises

- Demonstration: [`code/hydrologic_cycle_demo.py`](code/hydrologic_cycle_demo.py)
- Exercises: [`exercises/01-hydrologic-cycle-exercises.md`](exercises/01-hydrologic-cycle-exercises.md)
- Worked solutions: [`exercises/01-hydrologic-cycle-solutions.md`](exercises/01-hydrologic-cycle-solutions.md)
