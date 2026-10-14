# Module 11-06 — Geotechnical and Engineering Geophysics

**Stages:** advanced → doctoral · **Prerequisites:** the near-surface seismic and
EM methods ([06-10](../../06-seismology/10-refraction-and-near-surface-seismology/README.md),
[10-04](../../10-gpr-near-surface/04-near-surface-seismic-and-geotechnical/01-spt-cpt-crosshole.md)),
the electrical methods ([09](../../09-electrical-em-methods/README.md)) and the
exploration framing of [11-01](../01-exploration-workflow/README.md).

Engineering geophysics is the branch of the subject where a measurement becomes a
design decision, and the module is organised around the asymmetry of the two ways
a measurement can be wrong. In a resource survey, a missed anomaly is a missed
opportunity; in a tunnel, a dam or a clearance survey, a missed feature is an
accident or a failure. That difference changes what has to be reported: the
**false-negative rate** becomes the headline number, and every method must arrive
with the mode in which it fails.

The module therefore works from the engineering quantity back to the observable,
not the other way round. It derives the small-strain stiffness from $v_s$ and the
settlement that follows from it, the gravity anomaly of a void and its detection
limit, the self-potential profile and the temperature signature of seepage, the
magnetic dipole anomaly of a buried object with its $m^{1/3}$ depth scaling, and
the weighted-average apparent conductivity of a waste site. Each derivation is
followed by a measurement of what it cannot resolve — a trade-off, an equivalence,
a false-alarm rate, or a clearance probability that collapses as the number of
targets grows.

**All models and data in this module are SYNTHETIC.** No real site, structure,
borehole, survey, ordinance item or clearance specification is used, and no
design value, code requirement or observed rate is quoted.

## Learning objectives

By the end of this module you will be able to:

1. **Convert** a measured $v_s$ into $G_{\max}$ and $E$, and **compute** $v_{s30}$
   with its dependence on the profile and its truncation.
2. **Derive** the elastic settlement of a circular footing and **quantify** its
   sensitivity to a velocity error and a strain-dependent modulus.
3. **Compute** a microgravity detection limit for a void and **state** the
   degeneracy between radius, depth and density contrast.
4. **Compute** the value of information of a survey and **state** when a survey
   destroys value.
5. **Propagate** a picking error into a refraction depth and **compute** the
   thickness of a low-velocity zone that remains undetectable.
6. **Derive** the self-potential profile of a seepage dipole and the
   advection-diffusion temperature profile, and **convert** each into a bounded
   statement about flow.
7. **Derive** the magnetic dipole anomaly of a buried object and **compute** the
   probability of detection against a stated noise and threshold.
8. **Compute** the GPR aperture required for a self-calibrating hyperbola.
9. **Compute** a clearance probability $\mathrm{POD}^{n}$ and the false-alarm
   budget that trades digs against missed objects.
10. **Compute** the apparent conductivity of a waste section, its conductance
    equivalence and the false-discovery rate of an anomaly rule.

## Prerequisites

- [11-01 The Exploration Workflow](../01-exploration-workflow/README.md) — the
  objective-driven framing, and value of information.
- [06-10 Refraction and Near-Surface Seismology](../../06-seismology/10-refraction-and-near-surface-seismology/README.md)
  and [10-04 Near-Surface Seismic and Geotechnical Methods](../../10-gpr-near-surface/04-near-surface-seismic-and-geotechnical/01-spt-cpt-crosshole.md).
- [09-02 DC Resistivity](../../09-electrical-em-methods/02-dc-resistivity/01-resistivity-principle.md)
  and [09-04 Self-Potential](../../09-electrical-em-methods/04-self-potential-and-mise-a-la-masse/01-self-potential-sources.md).
- [08-03 Magnetic Anomalies and Modelling](../../08-geomagnetism-electromagnetism/03-magnetic-anomalies-and-modelling/04-magnetic-forward-modelling.md)
  and [10-01 GPR Principles](../../10-gpr-near-surface/01-gpr-principles/02-gpr-velocity-and-depth.md).
- [18-06 Uncertainty Quantification](../../18-inverse-problems/06-uncertainty-quantification/06-decision-under-uncertainty.md).

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Site Investigation: Objectives and Method Selection](01-site-investigation.md) | advanced | The product is a ground model; $v_s \to$ stiffness $\to$ settlement, voids, and when a survey is worth its cost |
| 02 | [Geophysics for Tunnels, Dams and Foundations](02-tunnelling-and-dams.md) | doctoral | Look-ahead and seepage: picking error, thin-zone blindness, SP and temperature tracers |
| 03 | [Buried Objects, UXO Detection and Clearance](03-buried-objects-uxo.md) | graduate | The dipole anomaly, POD against depth, GPR aperture, and $\mathrm{POD}^{n}$ |
| 04 | [Landfill, Waste and Brownfield Site Assessment](04-landfill-and-waste.md) | graduate | Weighted-average conductivity, conductance equivalence, magnetic clutter, false-discovery rate |

## Suggested path

**If you are new to engineering geophysics:** lesson 01 first — it sets up the
objective-driven selection and the stiffness/settlement chain that the rest of the
module references. Then 03 for the detection statistics, then 02 and 04.

**If you already do near-surface seismic:** read 01 §3.1-3.2 (stiffness,
settlement, $v_{s30}$), then 02 §3.1-3.2 for the picking-error and thin-zone
arithmetic.

**If you work on contaminated land or UXO:** lessons 03 and 04 in full, plus 01
§3.5 for the value-of-information framing that decides whether to survey at all.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-site-investigation.md`](01-site-investigation.md) | Lesson 01 |
| [`02-tunnelling-and-dams.md`](02-tunnelling-and-dams.md) | Lesson 02 |
| [`03-buried-objects-uxo.md`](03-buried-objects-uxo.md) | Lesson 03 |
| [`04-landfill-and-waste.md`](04-landfill-and-waste.md) | Lesson 04 |
| [`exercises/`](exercises) | Graded exercises with worked solutions for every lesson |
| [`code/`](code) | Four runnable, print-only demonstrations |

## How to run the demos

Use the project virtual environment, from the module's `code/` directory:

```bash
cd 11-exploration-geophysics/06-geotechnical-and-engineering/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python site_investigation_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python tunnelling_and_dams_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python buried_objects_uxo_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python landfill_and_waste_demo.py
```

Every demo prints labelled results with units, uses a fixed random seed
(`np.random.default_rng(20261014)`), requires no network access, and exits 0.
Each demo's printed numbers are the ones quoted in its lesson.

## Mastery checkpoint

Complete this without notes:

> A proposed supermarket site has a MASW profile ($260\ \mathrm{m\,s^{-1}}$ to
> $7\ \mathrm{m}$, $520\ \mathrm{m\,s^{-1}}$ below), a gravity survey at
> $5\ \mu\mathrm{Gal}$ resolution, and a magnetic survey for buried obstructions.
> **(a)** Compute $G_{\max}$, $v_{s30}$ and the settlement of a
> $R = 2\ \mathrm{m}$, $q = 180\ \mathrm{kPa}$ flexible footing with a stated
> strain reduction factor. **(b)** Compute the largest air-filled void that is
> *not* detectable at $6\ \mathrm{m}$ depth in $2500\ \mathrm{kg\,m^{-3}}$ rock.
> **(c)** A $900\ \mathrm{nT}$ magnetic anomaly is found; compute the depth of the
> object if its moment is $50\ \mathrm{A\,m^{2}}$. **(d)** With a prior
> probability of $0.15$ that a magnetic anomaly is a buried obstruction,
> $\mathrm{TPR} = 0.9$ and $\mathrm{FPR} = 0.55$, compute the expected number of
> productive digs if ten anomalies are excavated. **(e)** State which single
> additional measurement would most reduce the largest remaining uncertainty, and
> why.

A worked version of (a) and (c) appears in the lesson-01 and lesson-03
[solutions](exercises/03-buried-objects-uxo-solutions.md).

## Common pitfalls

1. **Reporting a section rather than a ground model.** State what was measured and
   what was inferred.
2. **Using a small-strain modulus as a design modulus.** The strain reduction is
   usually larger than the measurement error.
3. **Quoting a detection rate without a false-negative count.** On a structure or
   a clearance site, the miss rate is the product.
4. **Reading depth or flow rate from an amplitude.** Both are degenerate with
   geometry and with a coupling coefficient.
5. **Surveying without a pre-stated decision rule.** A survey that does not
   change an action has no value of information.

## Related modules

- [11-05 Groundwater Exploration Geophysics](../05-groundwater-exploration/README.md)
  — the same conductivity and seismic physics in a water-resource setting.
- [11-07 Exploration Case Studies](../07-exploration-case-studies/README.md) —
  the engineering and groundwater decisions re-examined as argument archetypes.
- [10-gpr-near-surface](../../10-gpr-near-surface/README.md) — the dielectric
  methods used for shallow structure and objects.
- [23-04 Electrical and EM Fieldwork](../../23-field-methods-instruments/04-electrical-em-fieldwork/01-ert-fieldwork.md)
  — the acquisition practice behind these surveys.
- [14-04 Contaminant and Environmental Geophysics](../../14-hydrology-hydrogeophysics/04-contaminant-and-environmental/01-contaminant-plumes.md)
  — the hydrogeological context of a waste site.
