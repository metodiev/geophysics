# Module 14-06 — Integrated Catchment and Watershed Studies

**Stages:** research → doctoral · **Prerequisites:** modules 14-01 to 14-05 and
14-06's own first lesson; basic statistics.

**All models and data in this module are SYNTHETIC.** The catchments, streams,
aquifers, water tables, tracer injections and rainfall series are idealised
teaching constructions. No real catchment, gauge, well or published measurement
is named or quoted, and no site-specific number appears.

This module is where the folder's measurements become a description of a whole
place. That step is not a matter of collecting more of them: it is a matter of
deciding which of the quantities you have are *measurements*, which are
*inferences*, which are *assumptions* and which are *decisions* — and of
knowing which of the four is holding up the answer. The three lessons build that
audit in increasing scale: a catchment characterised from a water balance, a
hydrograph, five refraction soundings and a storage estimate; a reach-scale
exchange flux measured four different ways that do not measure the same thing;
and a water-resource assessment whose final number is a decision with a
probability attached.

The honest difficulty the module keeps returning to is that integration does not
average uncertainty away. The catchment storage is dominated by the specific
yield, which none of the geophysics measures. The exchange flux is a Darcy
velocity in one method and a seepage velocity in another, and the effective
porosity that converts them is measured by neither. The sustainable yield that a
decision needs is a range of a factor of two wide. In each case the integrated
answer is narrower than its inputs and the narrowness is an artefact of the
reporting, not a property of the catchment. Recognising that, and writing the
assumptions down where a reader can find them, is the skill this module teaches.

## Learning objectives

By the end of this module you will be able to:

1. **Close** a catchment water balance and **show** by sensitivity analysis that
   closure is not validation.
2. **Separate** a hydrograph and **report** a baseflow index as a range with its
   filter parameter.
3. **Recover** a regolith thickness from a refraction sounding, **quantify** its
   velocity trade-off and **propagate** its uncertainty into a storage volume.
4. **Demonstrate** the equifinality of a recession and explain why the implied
   storage is unbounded at the limit.
5. **Compute** a reach-scale exchange flux by four methods, **state** what each
   measures with units, and **reconcile** them through a named assumption.
6. **Derive** the periodic temperature solution, the skin depth, and the
   symmetry that makes the phase sign-blind and the amplitude sign-sensitive.
7. **Estimate** recharge by two independent methods and **explain** their
   disagreement without averaging them.
8. **Compute** stream depletion and capture with the image-well solution, and
   **separate** capture from storage depletion.
9. **Propagate** parameter uncertainty into a distribution and **formulate** a
   sustainable yield as a decision with a receptor, a horizon and a tolerance.

## Prerequisites

- [14-01 Hydrology Fundamentals](../01-hydrology-fundamentals/README.md) — water
  balance, aquifer properties, well hydraulics.
- [14-02 Hydrogeophysical Methods](../02-hydrogeophysics-methods/README.md) —
  seismics, ERT and gravity for the geometry and the storage.
- [14-05 Time-Lapse and Monitoring Hydrogeophysics](../05-hydrogeophysical-monitoring/README.md) —
  the observations and their equivalence classes.
- [04-06-04 Aquifer Types and Groundwater Occurrence](../../04-earth-science-geology/06-petroleum-and-mineral-systems/04-groundwater-aquifers.md) —
  the geological description the idealised profiles stand for.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Integrated Catchment Characterisation](01-catchment-characterisation.md) | research | The geophysics constrains geometry; the storage is dominated by a parameter it cannot see |
| 02 | [Groundwater-Surface Water Interaction](02-groundwater-surface-water.md) | research | The methods measure different quantities; the inconsistency is the measurement |
| 03 | [Water Resource Assessment and Sustainable Yield](03-water-resource-assessment.md) | doctoral | Recharge and capture answer different questions; the yield is a decision with a probability |

## Suggested path

**If you are new to catchment studies:** lesson 01 in order — its Sections 2, 4
and 5 are the spine of everything else — then lesson 02's Sections 1–3.

**If you come from monitoring and want the water balance:** lesson 01 §2–§3, then
lesson 03 §2–§3 for the two recharge methods and why they disagree.

**If you are preparing a water-resource assessment:** lesson 03 in full, with
lesson 01 §5 (the storage error budget) and lesson 02 §6 (the reconciliation
table) as the two tools it uses.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-catchment-characterisation.md`](01-catchment-characterisation.md) | Lesson 01 |
| [`02-groundwater-surface-water.md`](02-groundwater-surface-water.md) | Lesson 02 |
| [`03-water-resource-assessment.md`](03-water-resource-assessment.md) | Lesson 03 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Three runnable demonstrations |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy and Matplotlib:

```bash
cd 14-hydrology-hydrogeophysics/06-integrated-catchment-studies/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python catchment_characterisation_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python groundwater_surface_water_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python water_resource_assessment_demo.py
```

Every demo prints labelled results with units, uses a fixed random seed
(`np.random.default_rng(20261014)`), is print-only (no figures, no
`plt.show()`), and exits 0. They require no network access and each finishes in
about two seconds or less.

## Mastery checkpoint

Complete this without notes:

> A SYNTHETIC $12.0\ \mathrm{km^2}$ catchment has, over one water year,
> $P = 807.6$ mm and $Q = 159.2$ mm, with a water-level rise implying
> $\Delta S = 19.6$ mm. **(a)** Compute ET and the evaporation ratio.
> **(b)** The ET estimate is found to be 10% too high; compute the implied
> $\Delta S$ and state what a water balance can and cannot establish.
> **(c)** A reach within the catchment has a piezometer pair 8 m apart reading a
> head difference of 0.32 m (aquifer above stream) with
> $K = 2.5\ \mathrm{m\,d^{-1}}$; compute the Darcy flux and, for $n_e = 0.25$,
> the seepage velocity. **(d)** A diurnal temperature pair gives an amplitude
> ratio of 0.2765 and a phase lag of 3.3295 h; compute the velocity from each and
> state which is consistent with (c). **(e)** A refraction sounding gives an
> intercept of 8.09 ms and a refracted slope of $0.400\ \mathrm{ms\,m^{-1}}$ with
> $v_1 = 600\ \mathrm{m\,s^{-1}}$; compute the thickness, and the catchment
> storage for $S_y = 0.10$ with its dominant uncertainty.

The arithmetic is lessons 01 §8, 02 §8 and 03 §8; the reconciliation of (c) and
(d) is lesson 02 §6.

## Common pitfalls across this module

1. **Presenting a closed water balance, or a single filter parameter, or a
   perfectly fitting recession, as validation.** Each is a bookkeeping
   consequence of an assumption; the lessons quantify each.
2. **Quoting a storage volume without the specific yield's uncertainty.** It
   dominated by an order of magnitude in the demonstration.
3. **Mixing Darcy velocities with seepage velocities.** They differ by the
   effective porosity, which none of the four reach methods measured.
4. **Averaging two recharge estimates that disagree by a factor of 2.6.**
   The disagreement is the result; report the pair and the reason.
5. **Treating the end-of-period depletion as if it applied throughout.** It
   overstated the first year's volume by a factor of 2.5.
6. **Reporting a sustainable yield without naming the receptor, the horizon and
   the tolerance.** Those three are the decision; the hydrology only informs it.

## Related modules

- [14-01 Hydrology Fundamentals](../01-hydrology-fundamentals/README.md) — the
  theory this module applies at the catchment scale.
- [14-05 Time-Lapse and Monitoring Hydrogeophysics](../05-hydrogeophysical-monitoring/README.md) —
  the observations and their ambiguities.
- [14-04 Contaminant and Environmental Geophysics](../04-contaminant-and-environmental/README.md) —
  the water-quality questions that constrain a yield as often as the quantity.
- [18-06 Uncertainty Quantification](../../18-inverse-problems/06-uncertainty-quantification/README.md) —
  the framework for the decision in lesson 03.
- [21-01 Statistics in Geophysical Practice](../../21-statistics-bayesian-ml/01-statistics-in-practice/README.md) —
  the resampling and regression tools used in the error budgets.
