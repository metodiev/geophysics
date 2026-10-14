# Module 14-04 — Contaminant and Environmental Geophysics

**Stages:** graduate → research · **Prerequisites:** modules
[14-01](../01-hydrology-fundamentals/README.md),
[14-03](../03-petrophysics-hydrology/README.md),
[09-02](../../09-electrical-em-methods/02-dc-resistivity/README.md) and
[09-04](../../09-electrical-em-methods/04-self-potential-and-mise-a-la-masse/README.md).

Environmental geophysics is the part of hydrogeophysics where the target is a
*change*: a plume, a leachate, an intrusion, a reaction product, a phase change.
This module treats five archetypes, and in each one the physical chain from the
target to the measurement is written out explicitly — transport, then
petrophysics, then the survey — and then attacked. Every lesson ends with the
same two questions: what else could produce this measurement, and is the
measurement precise enough for the decision it is meant to inform?

The five archetypes are deliberately different in mechanism, because the failure
modes differ. A conservative tracer is a transport problem with a linear property
model. A landfill leachate is the same transport with a layered-earth sounding
attached. Seawater intrusion is a density-driven interface with a
forty-to-one amplification between the head and the interface. Acid mine drainage
manufactures its own tracer by a reaction whose stoichiometry is the source term.
Permafrost is a phase change, where the property contrast is the largest in the
module and the quantity that models need is the least directly observable.

**All models and data in this module are SYNTHETIC.** Tracers are generic
idealised ionic solutes in arbitrary concentration units; the sites are
archetypes; the layering, end-member conductivities, reaction stoichiometry
inputs and soil properties are chosen teaching values. **No real contaminant,
spill, site, licence, regulation or discharge limit is described or implied
anywhere in this module.** The only numbers used as constants are standard atomic
weights, the molar masses they imply, the equivalent weight of calcium
carbonate, the latent heat of fusion of water, the densities of fresh water and
seawater, and the moduli and densities of water, air and ice.

## Learning objectives

By the end of this module you will be able to:

1. Derive and solve the one-dimensional advection–dispersion equation, and
   compute a front position, a retardation factor and a transition width.
2. Convert a tracer concentration to a pore-fluid conductivity and then to a
   bulk resistivity, stating every model in the chain.
3. Compute a detection threshold from a stated survey repeatability, and use it
   to screen a site for feasibility.
4. Derive the two-layer Wenner apparent resistivity from the image solution,
   verify it against both analytic limits, and report an admitted set of models
   rather than a single answer.
5. Derive the Dupuit leachate mound and the Ghyben–Herzberg interface, and
   explain the rôle of the $40{:}1$ amplification in coastal aquifer management.
6. Compute the stoichiometric sulphate and acidity yields of sulphide oxidation
   and carry them through a water balance to a discharge concentration.
7. Derive the Stefan thaw-depth solution, verify it against its energy balance,
   and explain why a velocity-derived ice content is a bracket.
8. Quantify the ambiguity between a clay-rich rock with fresh water and a clean
   rock with brackish water, and state the independent measurement that resolves
   it.

## Prerequisites

- [Module 14-01 Hydrology Fundamentals](../01-hydrology-fundamentals/README.md) —
  Darcy's law, aquifer properties, groundwater chemistry and well hydraulics.
- [Module 14-03 Petrophysical Relations for Saturated Media](../03-petrophysics-hydrology/README.md) —
  Archie's law, the saturation relations and the error-amplification discipline
  that this module applies to a field problem.
- [Module 09-02 DC Resistivity and ERT](../../09-electrical-em-methods/02-dc-resistivity/README.md) —
  arrays, sounding curves, apparent resistivity and inversion.
- [Module 09-04 Self-Potential and Mise-à-la-Masse](../../09-electrical-em-methods/04-self-potential-and-mise-a-la-masse/README.md) —
  the redox and streaming sources behind the self-potential signatures.
- [Module 02-06 Fluid Mechanics](../../02-physics/06-fluid-mechanics/README.md) —
  buoyancy and porous-medium flow, used in the saline-intrusion derivation.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Contaminant Plumes and Their Geophysical Signature](01-contaminant-plumes.md) | doctoral | Three separate models in a chain; the detection threshold scales with the background |
| 02 | [Landfill Investigation and Leachate Mapping](02-landfill-investigation.md) | graduate | A sounding returns an admitted set, not a pair of numbers |
| 03 | [Seawater Intrusion and Coastal Aquifer Monitoring](03-saline-intrusion.md) | doctoral | A $40{:}1$ lever between head and interface; clay mimics salinity |
| 04 | [Acid Mine Drainage and Mining Environmental Geophysics](04-acid-mine-drainage.md) | doctoral | The source term is a reaction, and its arithmetic is exact |
| 05 | [Permafrost Monitoring with Geophysics](05-permafrost-monitoring.md) | research | The largest contrast, the least directly observable target |

## Suggested path

**If you are new to environmental geophysics:** lessons 01, 02 and 03 in order,
running each demonstration. Lesson 01 supplies the chain that the other four
reuse; lesson 03 supplies the largest and most transferable contrast.

**If you already work with resistivity surveys:** read 01 §7–8 (detection and
time-lapse), 02 §3 and §6 (the forward model and the admitted set), then 03 §8
(the clay ambiguity) and all of 05.

**If you are preparing a research project:** 01 §9, 03 §9, 04 §9 and 05 §8 (the
assumption sections) plus the ★★★ exercises; each asks for a programme design,
and a design that could not be executed is a failed answer.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-contaminant-plumes.md`](01-contaminant-plumes.md) | Lesson 01 |
| [`02-landfill-investigation.md`](02-landfill-investigation.md) | Lesson 02 |
| [`03-saline-intrusion.md`](03-saline-intrusion.md) | Lesson 03 |
| [`04-acid-mine-drainage.md`](04-acid-mine-drainage.md) | Lesson 04 |
| [`05-permafrost-monitoring.md`](05-permafrost-monitoring.md) | Lesson 05 |
| [`code/`](code) | Five runnable demonstrations, one per lesson |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib,
pandas and SymPy:

```bash
cd 14-hydrology-hydrogeophysics/04-contaminant-and-environmental/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python contaminant_plumes_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python landfill_investigation_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python saline_intrusion_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python acid_mine_drainage_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python permafrost_monitoring_demo.py
```

Every demo is print-only (no figures, no `plt.show()`), uses the fixed seed
`np.random.default_rng(20261014)` where it needs randomness, prints labelled
results with units and the label `SYNTHETIC` on model inputs, runs in under a
second, needs no network access, and exits 0.

## Mastery checkpoint

Complete this without notes.

> A synthetic aquifer ($\theta = 0.30$, $\rho_b = 1855\ \mathrm{kg\,m^{-3}}$,
> $\phi = 0.30$, $m = 2$) receives a generic ionic tracer with
> $v = 0.050\ \mathrm{m\,day^{-1}}$, $\alpha_L = 1.0\ \mathrm{m}$ and
> $K_d = 0.05\ \mathrm{mL\,g^{-1}}$. **(a)** Compute $R$, the solute velocity and
> the front position at $10$ years. **(b)** Compute the 10–90% transition width
> then, and state which quantity grew faster. **(c)** With
> $\sigma_w = 0.050 + 1.0\times10^{-4}C\ \mathrm{S\,m^{-1}}$, compute the bulk
> resistivity at the background and at $C = 1000$ CU. **(d)** With a $2\%$
> one-sigma repeatability, compute the smallest detectable concentration and
> explain how it changes if $(i)$ the background becomes ten times more
> conductive, and $(ii)$ the survey is repeated with a four-times better
> repeatability. **(e)** A conductive anomaly is mapped; name three mechanisms
> other than the tracer and the measurement that excludes each.

## Common pitfalls

1. **Reporting a concentration from a resistivity without the chain.** Write the
   three models; if you cannot, it is a hypothesis.
2. **Skipping the water balance in a dissolved-load calculation.** The
   concentration is inversely proportional to the percolation ratio, and the
   ratio dominates the answer.
3. **Treating a sounding as a unique model.** Report the admitted set at a stated
   noise level.
4. **Reading the transition zone as the interface.** They differ by a width that
   is often a large fraction of the depth.
5. **Treating resistivity as linear in salinity.** A saline fraction of $0.10$
   is about half of the log contrast.
6. **Inverting an SP amplitude for a source strength.** $\rho I$ is not
   separable.
7. **Attributing a thaw-depth change to warming.** $\Delta T$, $k$ and $\theta$
   are not separable by geophysics.
8. **Designing a time-lapse survey with the smallest spacings.** They are the
   least sensitive to the target.

## Related modules

- [Module 14-01 Hydrology Fundamentals](../01-hydrology-fundamentals/README.md).
- [Module 14-02 Hydrogeophysical Methods](../02-hydrogeophysics-methods/README.md) —
  the surveys whose outputs these lessons consume.
- [Module 14-03 Petrophysical Relations for Saturated Media](../03-petrophysics-hydrology/README.md) —
  the transforms the chain uses.
- [Module 14-05 Time-Lapse and Monitoring Hydrogeophysics](../05-hydrogeophysical-monitoring/README.md) —
  the systematic treatment of repeatability and differencing.
- [Module 14-06 Integrated Catchment and Watershed Studies](../06-integrated-catchment-studies/README.md) —
  the scale at which these five archetypes are regulated in practice.
- [Module 09-02 DC Resistivity and ERT](../../09-electrical-em-methods/02-dc-resistivity/README.md)
  and [Module 09-04 Self-Potential and Mise-à-la-Masse](../../09-electrical-em-methods/04-self-potential-and-mise-a-la-masse/README.md).
- [Module 04-06 Petroleum and Mineral Systems](../../04-earth-science-geology/06-petroleum-and-mineral-systems/README.md) —
  the resource systems that generate the environmental liabilities.
