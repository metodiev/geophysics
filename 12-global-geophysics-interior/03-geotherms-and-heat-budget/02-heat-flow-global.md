---
id: 12-03-02
title: "Global Heat Flow and Its Distribution"
level: graduate
prereqs: ["12-03-01", "02-05-06", "05-09-01"]
tags: [global-geophysics, earth-interior, heat-flow, seafloor-age, lithosphere, hydrothermal]
---

# Global Heat Flow and Its Distribution

**All models and data in this module are SYNTHETIC.** The sea-floor age
distribution, the province heat-flow values, the conductivities and the areas
used below are adopted inputs of a teaching model. They are representative
rather than measured, and no real borehole, survey or station appears anywhere in
this lesson. Every number is printed by
[`code/heat_flow_global_demo.py`](./code/heat_flow_global_demo.py).

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the half-space cooling heat-flow law $q \propto t^{-1/2}$ and
   **identify** the constant $q\sqrt{t}$ that makes it a clock.
2. **Explain** what the plate model adds, and **quantify** how much the two
   models disagree at old ages and why the disagreement is not a mistake.
3. **Invert** a heat-flow measurement for sea-floor age and **show** that the
   relative age error is exactly twice the relative flux error.
4. **Integrate** a synthetic age distribution against both models to obtain the
   oceanic and global heat loss in terawatts, and **state** the sensitivity of
   the total to the young, hot bins.
5. **Compute** the near-ridge heat-flow deficit and **interpret** it as an
   advective (hydrothermal) transport, not as a measurement error.
6. **Regress** provincial heat flow against heat production and **report** the
   reduced heat flow and depth scale with a defensible interval.
7. **Separate** what a heat-flow map measures from what a thermal model computes
   in the same map.

## Prerequisites

- [01 Radiogenic Heat Production and Mantle Geotherms](01-radiogenic-heat.md) —
  where the crustal and mantle production terms come from.
- [02-05-06 Geotherms, Heat Flow and the Earth's Thermal Budget](../../02-physics/05-thermodynamics/06-geotherms.md) —
  the half-space cooling solution this lesson measures.
- [05-09-01 Measuring Terrestrial Heat Flow](../../05-core-geophysics/09-geothermal-and-heat-flow-methods/01-heat-flow-measurement.md) —
  what a borehole measurement actually delivers and how it is reduced.

## 1. The one-line idea

A heat-flow map looks like a map of temperature. It is closer to being a map of
**age** and of **water circulation**. The lithosphere cools as it ages, so the
conducted flux falls; where water circulates through young, hot rock it removes
the heat *before* conduction can, so the conducted flux measured at the surface
is smaller than the model predicts. Both effects are large, and they point in
opposite directions, which is why a global heat-loss number is a model output
rather than a measurement.

This lesson keeps three quantities strictly apart:

- the **model flux** $q_{\text{model}}(t)$, a function of age from a cooling
  model;
- the **measured flux** $q_{\text{obs}}$, what boreholes and probes report;
- the **lost flux** $q_{\text{lost}} = q_{\text{model}} - q_{\text{obs}}$, the
  part that left the lithosphere by advection.

The Earth's energy budget needs the third quantity. No instrument measures it
directly.

## 2. Precise definitions

**Half-space cooling.** A semi-infinite solid with surface temperature fixed at
$T_s$ and initial temperature $T_m$ has surface flux (see
[02-05-04](../../02-physics/05-thermodynamics/04-heat-conduction.md))

$$q(t) = \frac{k\,\Delta T}{\sqrt{\pi \kappa t}},
\qquad \Delta T = T_m - T_s,$$

with $k$ the thermal conductivity and $\kappa$ the thermal diffusivity. The
thermal boundary layer thickness is $d(t) = 2\sqrt{\kappa t}$.

**The $q\sqrt{t}$ invariant.** Multiplying by $\sqrt{t}$,

$$q\sqrt{t} = \frac{k\,\Delta T}{\sqrt{\pi\kappa}} = \text{constant},$$

which depends only on rock and mantle properties, not on age. Any table of
$q$ versus age can therefore be *tested* rather than merely displayed: if the
earthquake-free portion of the sea floor follows half-space cooling, the
$q\sqrt{t}$ column must be flat.

**Plate model.** If the cooling lithosphere has a base at fixed temperature at
depth $d$, the solution is a series,

$$q(t) = \frac{k\,\Delta T}{d}
\left[1 + 2\sum_{n=1}^{\infty}\exp\!\left(-\frac{n^2\pi^2\kappa t}{d^2}\right)\right]
\;\longrightarrow\; \frac{k\,\Delta T}{d}\ \text{as}\ t \to \infty .$$

The flux now *flattens* instead of decaying. The extra parameter $d$ is the
price: the plate model trades a falsifiable one-parameter law for a two-parameter
law that fits old sea floor but must have its $d$ supplied from outside.

**Reduced heat flow.** If continental heat flow is regressed on surface heat
production across provinces, $q_0 = q_{\text{reduced}} + A_0 h$, then
$q_{\text{reduced}}$ is the flux left after the radiogenic column has been
subtracted, and the slope $h$ is a depth scale — *if* the exponential-source
model is the right one.

## 3. Derivations and results

### 3.1 The half-space law, tabulated and tested

With the adopted $k = 3.0\ \mathrm{W\,m^{-1}\,K^{-1}}$,
$\kappa = 10^{-6}\ \mathrm{m^2\,s^{-1}}$ and $\Delta T = 1300\ \mathrm{K}$:

| Age (Ma) | $q$ (mW m⁻²) | $q\sqrt{t}$ | $2\sqrt{\kappa t}$ (km) |
|---|---|---|---|
| 1 | 391.7 | 391.7 | 11.2 |
| 2 | 277.0 | 391.7 | 15.9 |
| 5 | 175.2 | 391.7 | 25.1 |
| 10 | 123.9 | 391.7 | 35.5 |
| 20 | 87.6 | 391.7 | 50.2 |
| 40 | 61.9 | 391.7 | 71.1 |
| 80 | 43.8 | 391.7 | 100.5 |
| 120 | 35.8 | 391.7 | 123.1 |
| 160 | 31.0 | 391.7 | 142.1 |

The constant column is the test, and it passes exactly because the model is
analytic. The measured spread printed by the demonstration is
$0.00\times10^{0}\ \mathrm{mW\,m^{-2}}$ — the demonstration's own arithmetic
confirms the algebra rather than the Earth.

### 3.2 Where the plate model wins, and by how much

Adopting $d = 90\ \mathrm{km}$ gives the asymptotic flux
$k\Delta T/d = 43.3\ \mathrm{mW\,m^{-2}}$. The ratio
$q_{\text{plate}}/q_{\text{half-space}}$ is

| Age (Ma) | 1 | 5 | 20 | 40 | 80 | 120 | 160 |
|---|---|---|---|---|---|---|---|
| ratio | 1.000 | 1.000 | 1.000 | 1.003 | 1.081 | 1.236 | 1.405 |

Two conclusions, and the second is the more important.

- At young ages the two models are **indistinguishable** — to three decimal
  places below 20 Ma — because the cooling front has not reached the base. This
  is a built-in consistency check, and the demonstration verifies it
  independently: at $0.5\ \mathrm{Ma}$ the ratio is $1.0000$, and the base is
  first felt at $d^2/\kappa = 256.7\ \mathrm{Ma}$.
- At old ages the plate model is **40% higher**. The old sea floor is where the
  physics lives and where the half-space model fails: half-space cooling predicts
  31.0 mW m⁻² at 160 Ma, while the plate model predicts 43.5, and observed old
  sea floor is much closer to the latter.

A further internal inconsistency is worth stating plainly: the half-space model's
own boundary-layer thickness at 160 Ma is $2\sqrt{\kappa t} = 142\ \mathrm{km}$,
not the 90 km the plate model assumes. The two models do not merely differ in
their flux; they disagree about the thickness of the object they are modelling.

### 3.3 Heat flow as a clock, and its error amplification

Invert the half-space law:

$$t = \left(\frac{k\Delta T}{q\sqrt{\pi\kappa}}\right)^{2},\qquad\text{so}\qquad
\frac{\delta t}{t} = 2\,\frac{\delta q}{q}.$$

The demonstration tabulates it for a flux error of
$\delta q = 5\ \mathrm{mW\,m^{-2}}$:

| True age (Ma) | $q$ (mW m⁻²) | $\delta t$ (Ma) | $\delta t / t$ |
|---|---|---|---|
| 5 | 175.2 | 0.3 | 0.060 |
| 20 | 87.6 | 2.5 | 0.125 |
| 60 | 50.6 | 13.9 | 0.231 |

The amplification is exact, not approximate: a 5 mW m⁻² error is a 5.7% flux
error at 20 Ma and therefore an 12.5% age error. **A heat-flow age is twice as
uncertain as the heat flow that produced it**, which is why heat-flow ages
matter for young lithosphere and are superseded by magnetic anomalies for old
lithosphere.

### 3.4 Global heat loss from a synthetic age distribution

Adopt the sea-floor age distribution of the demonstration over
$3.6\times10^{14}\ \mathrm{m^2}$, with flux from the plate model:

| Age bin (Ma) | Area ($10^{14}\,\mathrm{m^2}$) | $q_{\text{plate}}$ (mW m⁻²) |
|---|---|---|
| 0–2 | 0.054 | 391.7 |
| 2–5 | 0.108 | 209.4 |
| 5–10 | 0.252 | 143.0 |
| 10–20 | 0.504 | 101.1 |
| 20–30 | 0.432 | 78.3 |
| 30–50 | 0.720 | 62.1 |
| 50–80 | 0.720 | 50.5 |
| 80–120 | 0.432 | 45.2 |
| 120–180 | 0.378 | 43.6 |

Integrating gives

$$Q_{\text{ocean}} = 28.2\ \mathrm{TW},\qquad
Q_{\text{continent}} = 65\ \mathrm{mW\,m^{-2}}\times2.0\times10^{14}\
\mathrm{m^2} = 13.0\ \mathrm{TW},$$

$$Q_{\text{total}} = 41.2\ \mathrm{TW},\qquad
\bar q = \frac{41.2\ \mathrm{TW}}{5.6\times10^{14}\ \mathrm{m^2}}
= 73.5\ \mathrm{mW\,m^{-2}}.$$

Three observations that a single number hides:

- **The young bins carry the budget.** 26% of the sea floor is younger than
  20 Ma and it carries 46% of the oceanic loss. Any error in the area of the
  youngest bins propagates almost undamped into the global total.
- **The model choice barely matters for the total** (27.3 TW half-space versus
  28.2 TW plate, a 3.1% difference), because most of the area is young enough
  that the two models agree. The plate model matters *locally* at old ages, not
  *globally* in the sum.
- **$Q_{\text{total}}$ is a model output.** It is an integral of a model flux
  over a model age distribution. Its uncertainty is dominated by the age
  distribution, not by the conductivity.

### 3.5 The near-ridge deficit: 4.6 TW of water

Adopt a measured/model ratio that suppresses conduction close to the ridge,

$$r(t) = 1 - 0.8\,e^{-t/8\ \mathrm{Ma}},$$

so that at 1 Ma only 29% of the model flux is conducted, and by 30 Ma the ratio
is 0.995. Weighted by the same areas, the missing flux integrates to

$$\Delta Q = 4.6\ \mathrm{TW} = 16\%\ \text{of the plate-model oceanic loss},$$

carried mostly in the 0–10 Ma bins (1.49 + 1.17 + 1.13 TW of the 4.6 TW total).

The point of the exercise is interpretive. That heat is not lost from the budget;
it leaves the lithosphere **by advection** — cold seawater goes down, hot
mineralised water comes back up. A heat-flow map near a mid-ocean ridge is
therefore a map of hydrothermal circulation, and the *conducted* flux there
under-reports the total loss by a factor that no conduction model can recover.
Recovering $\Delta Q$ requires either vent-fluid flux measurements or a coupled
flow model, and the number above is only as good as the adopted $r(t)$.

### 3.6 Provincial regression and what it assumes

Adopt six provinces with known production $A_0 = 0.4, 0.7, 1.0, 1.4, 1.9,
2.5\ \mathrm{\mu W\,m^{-3}}$, a true model
$q_0 = 40 + 10A_0\ \mathrm{mW\,m^{-2}}$, and scatter of standard deviation
$4\ \mathrm{mW\,m^{-2}}$ drawn from the demonstration's fixed seed. The
least-squares fit returns

$$q_{\text{reduced}} = 40.6 \pm 12.2\ \mathrm{mW\,m^{-2}},
\qquad h = 9.2 \pm 8.1\ \mathrm{km},$$

with the intervals at 95% confidence on 4 degrees of freedom. The adopted values
were 40.0 mW m⁻² and 10.0 km.

The regression "works" — the point estimates are close — but the honest reading
is the interval: **$h$ is resolved only to within a factor of seven** by six
provinces with a realistic scatter. Three assumptions are doing hidden work:

1. every province shares one $q_{\text{reduced}}$ and one $h$;
2. $A_0$ is known without error (it is not — it comes from the trace-element
   inventory of [01](01-radiogenic-heat.md), with its own scatter);
3. the exponential-source model is the right functional form, which §3.1 of
   [01](01-radiogenic-heat.md) showed is an adopted choice.

An error in $A_0$ is not random with respect to the regression: a systematic
overestimate of $A_0$ in high-production provinces biases the slope downward,
and the bias is invisible in the standard error.

## 4. Assumptions and regime of validity

1. **The cooling model applies to normal sea floor.** It says nothing about
   seamounts, hot-spot swells, oceanic plateaus or sediment-covered crust, where
   the thermal structure is not a simple cooling history.
2. **The surface boundary condition is a constant temperature.** A variable
   bottom-water temperature over glacial cycles perturbs the shallowest part of
   the geotherm and contaminates heat-flow measurements on young crust.
3. **The age distribution is adopted.** Global heat loss scales with it almost
   linearly, and the adopted distribution is the largest single uncertainty in
   $41.2\ \mathrm{TW}$.
4. **Hydrothermal suppression is phenomenologically imposed** through $r(t)$
   rather than computed. A physically derived $r(t)$ requires a permeability
   field, which is not measured on the ridge scale.
5. **The regression assumes no errors in the independent variable.** With
   realistic $A_0$ errors the slope is biased toward zero (regression dilution),
   so the reported $h$ in §3.6 is an *upper* bound on any true depth scale.
6. **Terrestrial areas and fluxes are single numbers.** Continental heat flow
   varies by a factor of three between provinces; $13.0\ \mathrm{TW}$ is a mean
   of a wide distribution.

## 5. Worked example: from one borehole to a global share

A synthetic borehole on 15 Ma sea floor reports
$q_{\text{obs}} = 92\ \mathrm{mW\,m^{-2}}$.

1. **Model flux.** $q_{\text{model}}(15) = 391.7/\sqrt{15} = 101.1\
   \mathrm{mW\,m^{-2}}$ (half-space; the plate model agrees to 0.1% here).
2. **Deficit.** $r(15) = 1 - 0.8e^{-15/8} = 0.877$, so
   $q_{\text{obs}}/q_{\text{model}} = 0.91$ — the borehole is 9% below the
   model, consistent with a partly ventilated aquifer.
3. **If instead the deficit were zero,** the flux would be
   $5.4\ \mathrm{mW\,m^{-2}}$ higher, and the heat-flow age inverted from the
   measurement would be off by $\delta t/t = 2\times(92/101.1 - 1) = -18\%$:
   $12.3\ \mathrm{Ma}$ instead of 15.
4. **Ascribing the deficit to advection** attributes
   $5.4\ \mathrm{mW\,m^{-2}}$ to water. Whether that is defensible depends
   entirely on whether the *measured* number has been correctly reduced — a
   sediment thickness correction is often larger than the deficit being
   interpreted.

## 6. Mastery checkpoint

Without notes:

> Oceanic crust of age $t = 25\ \mathrm{Ma}$ has a measured surface heat flow of
> $74\ \mathrm{mW\,m^{-2}}$. **(a)** Compute the half-space model flux with
> $k = 3.0$, $\kappa = 10^{-6}$ and $\Delta T = 1300$ in their SI values.
> **(b)** Compute the model's boundary-layer thickness and compare it with the
> 90 km used by the plate model. **(c)** State whether the measurement is above
> or below the model and give two physically distinct explanations.
> **(d)** If the measurement is taken at face value, convert the discrepancy into
> an age error. **(e)** Name the measurement you would need to decide between
> your two explanations.

## 7. Common pitfalls

1. **Reporting a global heat loss without its age distribution.** The same flux
   map supports totals that differ by tens of per cent through the young bins
   alone.
2. **Treating the half-space law as valid at all ages.** It is excellent below
   20 Ma and fails by 40% at 160 Ma.
3. **Calling the near-ridge deficit a measurement problem.** It is advection.
   Calling it an error leads to "correcting" a number that is right.
4. **Quoting a heat-flow age without the factor of two.** The relative age error
   is twice the relative flux error, exactly.
5. **Reading a regression slope as a depth without its interval.** Six provinces
   gave $h = 9.2 \pm 8.1\ \mathrm{km}$ here, from a true 10.0 km.
6. **Confusing conducted with total oceanic heat loss.** They differ by the
   advective term, which is exactly the term the budget needs.

## 8. Python demonstration

[`code/heat_flow_global_demo.py`](./code/heat_flow_global_demo.py) prints, in
seven labelled sections: the half-space table with its invariant; the plate
model and the ratio table; the age-inversion error table; the binned age
distribution with oceanic, continental and total losses; the near-ridge deficit
integration; the provincial regression with confidence intervals; and the
verification set (series convergence, the small-age limit, and a cross-check of
the regression against the normal equations). It exits 0 in a fraction of a
second.

```bash
cd 12-global-geophysics-interior/03-geotherms-and-heat-budget/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python heat_flow_global_demo.py
```

## 9. Exercises

Full sets with worked solutions are in
[`exercises/02-heat-flow-global-exercises.md`](./exercises/02-heat-flow-global-exercises.md)
and
[`exercises/02-heat-flow-global-solutions.md`](./exercises/02-heat-flow-global-solutions.md).

- **★** Compute $q$ at 3, 30 and 100 Ma from $q\sqrt{t} = 391.7$ and state the
  units of the constant.
- **★★** Show that $\delta t/t = 2\delta q/q$ by differentiating the inverted
  law, and evaluate the age error at 100 Ma for a 5% flux error.
- **★★** Recompute the global oceanic heat loss with the 0–2 Ma bin doubled and
  all other bins scaled to keep the total area constant. Report the change.
- **★★★** Design a test that distinguishes "the plate model with $d = 90$ km" from
  "the half-space model with a suppressed flux at old ages", and state what
  observation would discriminate them.

## 10. Related modules

- [01 Radiogenic Heat Production and Mantle Geotherms](01-radiogenic-heat.md) —
  the crustal and mantle production terms that appear in the global budget.
- [03 Thermal Evolution and Secular Cooling](03-thermal-evolution.md) — what the
  shortfall between production and loss does to the planet.
- [02-05 Thermodynamics](../../02-physics/05-thermodynamics/README.md) — the
  conduction equations and the geotherm used here.
- [05-09 Geothermal and Heat-Flow Methods](../../05-core-geophysics/09-geothermal-and-heat-flow-methods/README.md) —
  the measurement chain that produces $q_{\text{obs}}$.
- [12-01 Seismic Structure of the Earth](../01-seismic-structure-of-the-earth/README.md) —
  the lithosphere thickness from seismology, an independent constraint on $d$.
- [13-geodynamics-tectonics](../../13-geodynamics-tectonics/README.md) — plates,
  ridges and the kinematics that generate the age distribution used here.
