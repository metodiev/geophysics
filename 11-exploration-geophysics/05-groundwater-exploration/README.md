# Module 11-05 — Groundwater Exploration Geophysics

**Stages:** advanced → doctoral · **Prerequisites:** the electrical and EM
methods (folder [09](../../09-electrical-em-methods/README.md)), rock physics
([05-04](../../05-core-geophysics/04-rock-physics/README.md)) and the exploration
framing of [11-01](../01-exploration-workflow/README.md).

This module maps an aquifer with geophysics and is organised around one honest
difficulty: **no method measures water.** Electrical methods measure bulk
conductivity, which responds to salinity, porosity, saturation and clay in one
lumped number. Seismic methods measure elastic moduli, and Gassmann tells us that
the compressional speed responds to the pore fluid while the shear speed barely
does. Gravity measures saturated mass. Every lesson derives the relation that
links a measurement to a water property and then measures how many different
aquifers could have produced the same reading.

The module is therefore as much about **uncertainty accounting** as about
methods. It uses one synthetic rock- and fluid-model set throughout (a stated
dry frame, quartz moduli, air and water properties), so that the same numbers
reappear in the resistivity, seismic and airborne lessons and can be compared.
Where a relation is empirical — Archie's exponents, the $\lambda/3$ surface-wave
sampling rule, the low-induction-number weighting — the lesson says so and quotes
the value used. The final lesson converts an anomaly into a drilling
recommendation with an explicit error rate, because that is what the survey is
for.

**All models and data in this module are SYNTHETIC.** No real aquifer, site,
borehole or water sample is used, and no depth, salinity or yield is quoted from
a published measurement.

## Learning objectives

By the end of this module you will be able to:

1. **Derive** the Ghyben-Herzberg relation for a sharp fresh/salt interface and
   use it with an explicit density contrast.
2. **Apply** Archie's law and **demonstrate** that one bulk conductivity is
   consistent with a family of salinity/porosity/saturation combinations.
3. **Compute** Gassmann fluid substitution and **explain** why $v_p$ is a
   saturation indicator and $v_s$ is not.
4. **Compute** apparent resistivities, skin depths and depths of investigation,
   and **state** the acquisition and threshold each depends on.
5. **Map** the admitted model set of a layered-earth inversion and read its
   least-determined direction.
6. **Recover** a refraction depth from a crossover distance and **quantify** its
   error for a stated velocity error and contrast.
7. **Compute** the sampling depth of a surface-wave dispersion curve and
   **quantify** the ambiguity between two profiles that fit it.
8. **Derive** the diffusive diffusion depth and the sensitivity kernel of an
   airborne EM system, and **compute** its depth of investigation.
9. **State** the conductance equivalence of a thin layer and explain why AEM
   products are delivered as conductance maps.
10. **Convert** a geophysical anomaly into a decision with Bayes' rule, and
    **quote** the expected number of false positives at a stated prior.

## Prerequisites

- [11-01 The Exploration Workflow](../01-exploration-workflow/README.md) — a
  survey answers a question; here the question is water supply.
- [09 Electrical and EM Methods](../../09-electrical-em-methods/README.md) — DC
  resistivity, ERT, TEM and their inversions.
- [08-05 Controlled-Source EM](../../08-geomagnetism-electromagnetism/05-controlled-source-em/05-airborne-em.md)
  — the airborne systems.
- [05-04 Rock Physics](../../05-core-geophysics/04-rock-physics/README.md) —
  Archie's law and Gassmann substitution.
- [06-10 Refraction and Near-Surface Seismology](../../06-seismology/10-refraction-and-near-surface-seismology/README.md)
  — refraction and MASW.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Geophysical Signatures of Aquifers and Saline Interfaces](01-aquifer-signatures.md) | advanced | Ghyben-Herzberg, Archie and Gassmann; one conductivity, many aquifers |
| 02 | [EM and ERT for Groundwater Mapping](02-em-and-ert-groundwater.md) | graduate | The forward relations, and the admitted set of a sounding |
| 03 | [Seismic Refraction and Surface Waves for Aquifers](03-seismic-groundwater.md) | graduate | $v_p$ sees the fluid, $v_s$ sees the frame; resolution trades with depth |
| 04 | [Airborne EM for Regional Aquifer Mapping](04-airborne-groundwater.md) | doctoral | Diffusion depth, conductance equivalence, and the base rate of drilling |

## Suggested path

**If you are new to groundwater geophysics:** lessons 01 → 02 → 03 in order,
running each demonstration. Lesson 01 fixes the vocabulary of ambiguity that the
other three quantify.

**If you already know ERT:** read 01 §3.2-3.4 (Archie, Gassmann, the slab), then
02 §3.4 and 03 §3.4 for the two resolution analyses, then 04.

**If you work with AEM data:** 04 in full, plus 02 §3.3 for the conductance
concept and 01 §3.2 for the conductivity ambiguity that no inversion can remove.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-aquifer-signatures.md`](01-aquifer-signatures.md) | Lesson 01 |
| [`02-em-and-ert-groundwater.md`](02-em-and-ert-groundwater.md) | Lesson 02 |
| [`03-seismic-groundwater.md`](03-seismic-groundwater.md) | Lesson 03 |
| [`04-airborne-groundwater.md`](04-airborne-groundwater.md) | Lesson 04 |
| [`exercises/`](exercises) | Graded exercises with worked solutions for every lesson |
| [`code/`](code) | Four runnable, print-only demonstrations |

## How to run the demos

Use the project virtual environment, from the module's `code/` directory:

```bash
cd 11-exploration-geophysics/05-groundwater-exploration/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python aquifer_signatures_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python em_and_ert_groundwater_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python seismic_groundwater_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python airborne_groundwater_demo.py
```

Every demo prints labelled results with units, uses a fixed random seed
(`np.random.default_rng(20261014)`), requires no network access, and exits 0.
Each demo's printed numbers are the ones quoted in its lesson.

## Mastery checkpoint

Complete this without notes:

> A dry-region survey combines an ERT profile, a refraction line and a ground
> TEM sounding over the same line. The ERT images a $20\ \Omega\,\mathrm{m}$
> zone at $30$-$55\ \mathrm{m}$; refraction gives $1200\ \mathrm{m\,s^{-1}}$
> above a refractor at $18\ \mathrm{m}$; TEM gives $S = 2.6\ \mathrm{S}$.
> **(a)** Convert the resistivity to a conductivity and list three
> interpretations consistent with it. **(b)** State whether the refraction
> refractor can be the water table, and what you would need to check. **(c)**
> Convert $S$ into the two most extreme plausible layer models. **(d)** Using a
> regional prior of $15\%$ that a conductive zone is a usable aquifer, and
> $P(\text{conductive}\mid\text{aquifer}) = 0.8$,
> $P(\text{conductive}\mid\text{clay}) = 0.35$, compute the posterior and the
> expected number of productive holes if you drill ten anomalies. **(e)** State
> which single additional measurement would reduce the largest remaining
> uncertainty, and why.

A worked version of the interface and Bayes steps appears in the lesson-01 and
lesson-04 [solutions](exercises/04-airborne-groundwater-solutions.md).

## Common pitfalls

1. **Calling a conductive anomaly water.** Clay, salinity, mineralisation and
   culture all lower resistivity.
2. **Quoting a depth without a velocity or conductivity model.** Every depth here
   is conditional on one.
3. **Quoting a layer thickness where only the conductance is resolved.**
4. **Treating $v_s$ as a saturation indicator.** Gassmann leaves $\mu$ unchanged.
5. **Forgetting the base rate.** A good survey in a region with few aquifers
   still produces mostly dry targets.

## Related modules

- [11-01 The Exploration Workflow](../01-exploration-workflow/README.md) — the
  decision framing this module implements.
- [11-04 Geothermal Exploration Geophysics](../04-geothermal-exploration-geophysics/README.md)
  — the same conductive-clay-cap ambiguity in a different resource.
- [11-07 Exploration Case Studies](../07-exploration-case-studies/README.md) —
  arid-region groundwater explored as an argument archetype.
- [14 Hydrology and Hydrogeophysics](../../14-hydrology-hydrogeophysics/README.md)
  — where a geophysical product becomes a water-resource statement.
- [09 Electrical and EM Methods](../../09-electrical-em-methods/README.md) and
  [18 Inverse Problems](../../18-inverse-problems/README.md) — the theory behind
  the inversions used here.
