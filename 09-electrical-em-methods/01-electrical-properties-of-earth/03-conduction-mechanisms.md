---
id: 09-01-03
title: "Electrolytic, Electronic and Surface Conduction"
level: graduate
prereqs: ["09-01-02", "02-07-06"]
tags: [electrical-methods, conduction-mechanisms, brine, electrolytic, surface-conduction, bounds]
---

# Electrolytic, Electronic and Surface Conduction

A measured conductivity is a sum. Current reaches the far electrode by whatever
path is connected, and three mechanisms compete for it: ions in the pore water
(**electrolytic**), electrons in a connected metallic or semi-metallic phase
(**electronic**), and an excess of cations adsorbed at mineral surfaces
(**surface**). This lesson writes the sum down, derives the electrolytic term
from mobilities, and quantifies the single most damaging ambiguity in
resistivity interpretation: a conductive mineral that is present is
indistinguishable from one that is connected.

**All models and data in this module are SYNTHETIC.** The samples, the
surface-conductivity constant and the activity correction used below are chosen
teaching values. The Faraday constant, the elementary charge and the Avogadro
number are exact SI-defined constants, and the ionic mobilities are standard
handbook limiting mobilities of the ions named.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the ionic conductivity of a dilute electrolyte from the Nernst–
   Einstein relation and compute it from concentrations and mobilities.
2. **Explain** why the ideal model is exactly linear in concentration and
   identify the physical reason real brines are not.
3. **Compute** the parallel and series bounds on a two-phase mixture and use
   them to show that connectivity, not conductivity, controls the answer.
4. **Decompose** a measured conductivity into an Archie term and a surface term
   and **quantify** the porosity error made by ignoring the second.
5. **Compute** a mechanism budget for a sample and decide which mechanism
   dominates.
6. **State** which measurement or model would be needed to break the
   connectivity ambiguity.

## Prerequisites

- [09-01-02 Archie's Law, Porosity and Saturation](02-archies-law.md) —
  the formation factor and the electrolytic term.
- [02-07-06 EM Fields in Conductors: Skin Depth and Diffusion](../../02-physics/07-electromagnetism/06-em-in-conductors.md) —
  conductivity in a continuum, drift velocity and current density.

## 1. Electrolytic conduction from mobilities

An ion of charge $q_i = z_i e$ drifts at velocity $v_i = \mu_i E$ in a field
$E$, where $\mu_i$ is the mobility ($\mathrm{m^2\,V^{-1}s^{-1}}$). The current
density it carries is $n_i q_i v_i$ with $n_i$ the number density, so

$$\sigma_w = \sum_i n_i z_i e\,\mu_i z_i e
= F \sum_i c_i z_i^2\mu_i, \qquad F = eN_A,$$

where $c_i$ is the molar concentration and $F$ the Faraday constant. For a 1:1
electrolyte with $z = 1$:

$$\sigma_w = F\,c\left(\mu_+ + \mu_-\right).$$

This is the Nernst–Einstein relation in its simplest form, and it is *exactly
linear* in $c$. The demonstration prints the constants and the table:

| $c$ (mol/L) | $10^{-4}$ | $10^{-3}$ | $10^{-2}$ | 0.1 | 0.5 | 1.0 | 5.0 |
|---|---|---|---|---|---|---|---|
| $\sigma_w$ ($\mathrm{S\,m^{-1}}$) | 0.0013 | 0.0126 | 0.1264 | 1.2640 | 6.3198 | 12.6396 | 63.1979 |
| molar conductivity ($\mathrm{S\,m^2\,mol^{-1}}$) | 0.01264 | 0.01264 | 0.01264 | 0.01264 | 0.01264 | 0.01264 | 0.01264 |

with $F = 96485.332123\ \mathrm{C\,mol^{-1}}$ and $F(\mu_+ + \mu_-) = 0.01264\
\mathrm{S\,m^2\,mol^{-1}}$. The molar conductivity is constant to five digits in
every row — that is what "ideal" means, and it is a property of the model, not a
claim about the ocean.

## 2. Why real brines are sublinear

At high concentration the ions interact: the atmosphere around each ion is
polarised, mobilities fall, and the linear relation overestimates $\sigma_w$.
The demo uses a SYNTHETIC teaching correction
$\sigma_w = \Lambda c\,(1 - \alpha\sqrt{c})$ with $\alpha = 0.5$, chosen only to
show the shape:

| $c$ (mol/L) | 0.001 | 0.01 | 0.1 | 0.5 | 1.0 | 2.0 |
|---|---|---|---|---|---|---|
| ratio to ideal | 0.984 | 0.950 | 0.842 | 0.646 | **0.500** | 0.293 |
| implied $\rho_w$ ($\Omega\,\mathrm{m}$) | 80.39 | 8.33 | 0.94 | 0.245 | 0.158 | 0.135 |

The synthetic correction halves $\sigma_w$ at 1 mol/L. The teaching point is not
the coefficient — it is that **a salinity inferred from $\sigma_w$ without a
brine model can be wrong by a factor of two, in the direction that makes a
saline plume look fresh.** In practice $\rho_w$ is measured on a sample or taken
from a chart for the specific water chemistry; it is not predicted from a
formula.

## 3. Electronic conduction: connectivity is the question

A rock is a two-phase mixture, and the conductivity of a mixture is bounded.
For a volume fraction $\phi$ of pore fluid with grain conductivity
$\sigma_g$ (SYNTHETIC: $10^{4}\ \mathrm{S\,m^{-1}}$ for a connected sulphide,
$10^{-6}\ \mathrm{S\,m^{-1}}$ for a dry silicate):

$$\sigma_\text{parallel} = (1-\phi)\sigma_g + \phi\sigma_p, \qquad
\sigma_\text{series} = \left[\frac{1-\phi}{\sigma_g} +
\frac{\phi}{\sigma_p}\right]^{-1}.$$

The demo's table for $\phi = 0.20$:

| pore $\sigma_p$ | silicate, parallel | silicate, series | sulphide, parallel | sulphide, series |
|---|---|---|---|---|
| 0.01 | $2.0008\times10^{-3}$ | $1.2500\times10^{-6}$ | $8.0000\times10^{3}$ | $5.0000\times10^{-2}$ |
| 0.10 | $2.0001\times10^{-2}$ | $1.2500\times10^{-6}$ | $8.0000\times10^{3}$ | $4.9998\times10^{-1}$ |
| 1.00 | $2.0000\times10^{-1}$ | $1.2500\times10^{-6}$ | $8.0002\times10^{3}$ | $4.9980$ |

Units: $\mathrm{S\,m^{-1}}$. The bounds differ by more than five decades in the
sulphide case and more than three in the silicate case. A single conductivity
measurement therefore **cannot** distinguish "no sulphide" from "unconnected
sulphide", and the *same* rock can be a resistor or a conductor depending on
whether the metallic grains touch. This is not a modelling subtlety; it is the
reason induced polarisation exists (module
[09-03 Induced Polarisation](../03-induced-polarisation/README.md)), because
polarisation responds to the *presence* of polarisable grain surfaces while
conduction responds to their *connection*.

## 4. The three-term decomposition and its cost

Take a synthetic clay-bearing sand: $\phi = 0.25$, so $F = \phi^{-2} = 16$,
$\sigma_w = 0.50\ \mathrm{S\,m^{-1}}$, and a SYNTHETIC surface term
$\sigma_s = 0.05325\ \mathrm{S\,m^{-1}}$. The measured value is the *sum*

$$\sigma = \frac{\sigma_w}{F} + \sigma_s = 0.03125 + 0.05325
= 0.08450\ \mathrm{S\,m^{-1}},$$

so the surface term carries $63.0\%$ of the current. Reading the same number
with Archie alone:

$$F_\text{app} = \frac{\sigma_w}{\sigma} = 5.917, \qquad
\phi_\text{app} = F_\text{app}^{-1/2} = 0.4111$$

against a true $0.25$ — a $+64.4\%$ error. The demo goes further and asks what
happens if $\sigma_s$ is *known* only to within a factor: assuming it is 10%,
30% or 50% of the total gives $\phi = 0.3900$, $0.3439$ and $0.2907$. Every
defensible value of the surface term still leaves tens of per cent of porosity
error, because

$$\phi = \left(\frac{\sigma_w}{\sigma - \sigma_s}\right)^{1/2}$$

is a square root of a *difference* of two comparable numbers: the worst
conditioned step in the whole workflow.

## 5. Mechanism budget

| SYNTHETIC sample | $\phi$ | $\sigma_w$ | $\sigma_s$ | $\sigma$ | electrolytic | surface |
|---|---|---|---|---|---|---|
| clean sandstone | 0.25 | 0.50 | 0 | 0.0312 | 100.0% | 0.0% |
| clay-bearing sand | 0.25 | 0.50 | 0.0532 | 0.0845 | 37.0% | 63.0% |
| marine clay | 0.45 | 2.50 | 0.600 | 1.1062 | 45.8% | 54.2% |

Units: $\sigma$ in $\mathrm{S\,m^{-1}}$. Two rocks with the *same* porosity and
the *same* pore-water conductivity differ by a factor of 2.7 in conductivity
because of the clay fabric. Any interpretation that ignores the third column
will attribute the difference to porosity or salinity, and it has no way to
know.

## 6. Worked example: budget of an ore-grade rock

A synthetic sample has $\phi = 0.20$, $\sigma_p = 0.5\ \mathrm{S\,m^{-1}}$,
grain conductivity $10^{4}\ \mathrm{S\,m^{-1}}$ and 3% by volume of connected
sulphide. Compute two extreme models, stating which bound applies:

- **Matrix-supported (series):** the sulphide is isolated, so the current must
  cross it: $\sigma \approx \phi\sigma_p = 0.1\ \mathrm{S\,m^{-1}}$, i.e.
  $\rho \approx 10\ \Omega\,\mathrm{m}$; the sulphide is invisible.
- **Connected (parallel):** if the sulphide network spans the sample, its
  contribution is $\approx 0.03\times10^{4} = 300\ \mathrm{S\,m^{-1}}$, three
  orders above the pore-fluid contribution.

The measurement cannot tell these apart without additional information — which
is exactly what the induced-polarisation measurement of module 09-03 supplies,
by measuring the *surface area* of the polarised grains rather than their
connection.

## 7. Regime of validity

1. **Ohmic, linear, isotropic media.** No non-linear electrode effects; the
   electrode interface is treated as a boundary condition, not a mechanism.
2. **Dilute-electrolyte mobilities.** The mobility coefficients are infinite-
   dilution values; the correction of Section 2 is a teaching shape, and real
   work uses measured $\rho_w$.
3. **Two-phase bounds are bounds.** They bracket the mixture conductivity; they
   do not predict it. Only a textural model (or a measurement) closes the gap.
4. **Surface conduction is modelled empirically.** The constant relating
   conductivity to the cation excess has no first-principles value here; see
   [09-01-04](04-clay-and-surface-conduction.md).
5. **No polarisation in this lesson.** Everything above is the DC limit; the
   frequency dependence belongs to [09-01-05](05-temperature-and-pressure-effects.md)
   and module 09-03.

## 8. Mastery checkpoint

1. Derive $\sigma_w = F c(\mu_+ + \mu_-)$ from $v = \mu E$ and $J = \sum n q v$.
2. Compute $\sigma_w$ for $c = 0.05\ \mathrm{mol/L}$ with the printed constants,
   and give $\rho_w$.
3. A sand has $\phi = 0.30$, $m = 2$, $\sigma_w = 0.2\ \mathrm{S\,m^{-1}}$ and
   measures $\sigma = 0.05\ \mathrm{S\,m^{-1}}$. Compute $\sigma_s$ and the
   porosity error made by ignoring it.
4. Explain in three sentences why a conductivity anomaly alone is weak evidence
   for sulphide mineralisation.

## 9. Common pitfalls

1. **Adding conductivities when resistivities were measured.** The sum is in
   $\sigma$; $1/\rho_1 + 1/\rho_2 \ne 1/(\rho_1 + \rho_2)$.
2. **Assuming a salinity from $\sigma_w$ linearly.** Section 2 shows a factor of
   two at 1 mol/L even in a smooth model.
3. **Treating the bounds as predictions.** They span five decades.
4. **Forgetting the $\sigma_s$ subtraction is ill-conditioned.** The square root
   of a small difference amplifies whatever error is in either term.
5. **Reading a low resistivity as a low-resistivity *rock*.** It is usually
   water, clay or connectivity — in that order of frequency.

## 10. Related modules

- [09-01-02 Archie's Law, Porosity and Saturation](02-archies-law.md).
- [09-01-04 Clay Effects, CEC and Membrane Polarisation](04-clay-and-surface-conduction.md) —
  the surface term in detail.
- [09-01-05 Temperature, Pressure and Frequency Dependence](05-temperature-and-pressure-effects.md).
- [09-03 Induced Polarisation](../03-induced-polarisation/README.md) — the
  measurement designed to separate presence from connectivity.
- [02-07-06 EM Fields in Conductors: Skin Depth and Diffusion](../../02-physics/07-electromagnetism/06-em-in-conductors.md).

## 11. Demonstration and exercises

- [`code/conduction_mechanisms_demo.py`](code/conduction_mechanisms_demo.py)
  prints the Nernst–Einstein table, the synthetic activity correction, the
  parallel/series bounds, the three-term decomposition and the mechanism budget.
- [Exercises](exercises/03-conduction-mechanisms-exercises.md) and
  [worked solutions](exercises/03-conduction-mechanisms-solutions.md).
