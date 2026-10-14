# Module 14-05 — Time-Lapse and Monitoring Hydrogeophysics

**Stages:** research · **Prerequisites:** modules 14-01, 14-02 and 14-03;
basic inverse theory.

**All models and data in this module are SYNTHETIC.** No field site, tracer
test, borehole, monitoring campaign or published measurement is used, and no
number is quoted from a real survey.

This module is about the difference between two measurements of the same place.
A single geophysical survey gives a state: a resistivity, a concentration, a
water content, with all the ambiguity that the petrophysical link carries. Two
surveys, separated in time, give a *change*, and the change is usually what the
hydrologist actually asked for. Time-lapse differencing is therefore the most
powerful idea in hydrogeophysics and the one most often over-interpreted: the
subtraction removes the static background and, with it, the evidence of what the
background was; a differenced image cannot tell you whether the change is water
content, salinity or temperature; and the inversion that produces it is
underdetermined by a margin that must be reported alongside the picture.

All three lessons are built around that tension. Each develops a forward model
first, verifies it against something computable independently — an analytic
limit, a mass balance, a homogeneous solution — and only then inverts it. Each
lesson then measures what the inversion does *not* determine: the equivalence
class of a saturation change, the null space of a cross-hole geometry, the
confidence of a data-assimilation system that has been fed a biased observation.
The recurring result is that time-lapse monitoring constrains changes well and
states poorly, and that a monitoring programme is only defensible when it says
which independent measurement breaks the ambiguity it cannot break itself.

## Learning objectives

By the end of this module you will be able to:

1. **Derive** the forward response of a moving wetting front for a surface array.
2. **Map** between resistivity, saturation and pore-water conductivity with a
   stated petrophysical model, and **state** the equivalence class that a single
   ratio leaves open.
3. **Decide** detectability against a stated error model, and **choose** the
   electrode geometry that makes a given change visible.
4. **Build** a cross-borehole data kernel, **determine** its rank, and **report**
   the null-space dimension and the effective number of resolved parameters.
5. **Interpret** a breakthrough curve, stating the detection threshold that
   defines every arrival time and the integration window that defines every mass
   recovery.
6. **Reconcile** a temperature-derived seepage velocity with a petrophysical
   concentration estimate, in a common set of units.
7. **Write** a data-assimilation problem as a forecast model, an observation
   operator and error models, and **compute** the Kalman update.
8. **Diagnose** an inconsistent assimilation from innovation statistics and
   **demonstrate** that a biased observation operator produces a confident,
   wrong analysis.
9. **Report** a time-lapse result with its regularisation, its resolution and the
   range of interpretations it admits.

## Prerequisites

- [14-01 Hydrology Fundamentals](../01-hydrology-fundamentals/README.md) —
  Darcy's law, the unsaturated zone and groundwater flow.
- [14-02 Hydrogeophysical Methods](../02-hydrogeophysics-methods/README.md) —
  the single-survey methods whose forward models this module time-steps.
- [14-03 Petrophysical Relations for Saturated Media](../03-petrophysics-hydrology/README.md) —
  Archie's law and the velocity/saturation relations.
- [18-inverse-problems](../../18-inverse-problems/README.md) — regularisation,
  resolution and the null space, used in every lesson.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Time-Lapse ERT for Infiltration and Transport](01-time-lapse-ert.md) | research | A ratio cannot separate saturation from salinity; the array decides what is detectable |
| 02 | [Cross-Borehole Monitoring and Tracer Tests](02-cross-borehole-monitoring.md) | research | A threshold defines the arrival time; the ray geometry defines the null space |
| 03 | [Assimilating Geophysical Data into Hydrological Models](03-geophysical-data-assimilation-hydrology.md) | research | A biased observation operator produces a confident, wrong state; analysis skill is not forecast skill |

## Suggested path

**If you are new to monitoring:** lesson 01 in order, running the demonstration
twice — once as written and once with a different noise level — then lesson 02's
Section 2 for the geometry argument.

**If you come from geophysics and want the hydrology:** lesson 01 §2–§3 (the
petrophysical link and the forward model), then lesson 03, whose whole argument
is about what happens when a geophysical estimate is fed into a hydrological
model.

**If you are preparing a monitoring programme:** lesson 01 §4 (detectability and
array design), lesson 02 §5–§8 (coverage, rank and detection limits) and lesson
03 §5–§7 (survey interval, bias and verification).

## Materials in this module

| Path | Contents |
|---|---|
| [`01-time-lapse-ert.md`](01-time-lapse-ert.md) | Lesson 01 |
| [`02-cross-borehole-monitoring.md`](02-cross-borehole-monitoring.md) | Lesson 02 |
| [`03-geophysical-data-assimilation-hydrology.md`](03-geophysical-data-assimilation-hydrology.md) | Lesson 03 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Three runnable demonstrations |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy and Matplotlib:

```bash
cd 14-hydrology-hydrogeophysics/05-hydrogeophysical-monitoring/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python time_lapse_ert_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python cross_borehole_monitoring_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python geophysical_data_assimilation_hydrology_demo.py
```

Every demo prints labelled results with units, uses a fixed random seed
(`np.random.default_rng(20261014)`), is print-only (no figures, no
`plt.show()`), and exits 0. They require no network access and each finishes in
under two seconds.

## Mastery checkpoint

Complete this without notes:

> A surface ERT array with spacings 0.5–16 m monitors an infiltration experiment
> in a SYNTHETIC soil ($\phi = 0.35$, $m = 1.80$, $n = 2.00$,
> $\rho_w = 10\ \Omega\,\mathrm{m}$). The time-lapse ratio at $a = 0.5$ m is
> 0.30 and at $a = 16$ m is 0.94. **(a)** Convert the first value into a water
> content for the "all saturation" member of the equivalence family, and state
> the other member at the same ratio. **(b)** Decide whether the change is
> detectable at 1% noise, and name the spacing that carries the depth
> information. **(c)** State the two measurements that would break the
> saturation–salinity ambiguity. **(d)** A colleague proposes to add a
> cross-borehole survey with 6 electrode levels in each of two boreholes across a
> 10 m section; state the maximum rank of the resulting data kernel for a
> 40 × 20 grid and the effective number of resolved parameters you would expect
> to report. **(e)** The water content is then assimilated into a soil-moisture
> model, and a bias of $-9\%$ is present in the petrophysical operator; state
> what happens to the analysis error and to the reported uncertainty.

A worked version of (a)–(c) is in the lesson-01
[solutions](exercises/01-time-lapse-ert-solutions.md); (d) is lesson 02 §5 and (e)
is lesson 03 §6.

## Common pitfalls across this module

1. **Reading a difference image as a water-content map.** It is a
   resistivity-change map; the water content is one member of an equivalence
   class.
2. **Choosing regularisation to make the picture look right.** The weight is part
   of the result.
3. **Quoting an arrival time without its threshold, or a recovery without its
   window.** Both appeared as factors of several in the demonstrations.
4. **Assuming differencing removes all systematics.** A drift of a third of the
   noise level produced an artefact of 9% of the plume amplitude.
5. **Treating a geophysical observation as unbiased.** A plausible exponent error
   gave a multiplicative bias of $-8.8\%$, which the filter converted into a
   confident, wrong state.
6. **Verifying a monitoring system on the data it assimilated.** The
   demonstration's analysis error barely moved under a 15% forcing bias while the
   5-day forecast error tripled.

## Related modules

- [14-01 Hydrology Fundamentals](../01-hydrology-fundamentals/README.md) — the
  physics that every observation in this module is ultimately about.
- [14-02 Hydrogeophysical Methods](../02-hydrogeophysics-methods/README.md) — the
  acquisition and single-survey interpretation.
- [14-04 Contaminant and Environmental Geophysics](../04-contaminant-and-environmental/README.md) —
  the applications this monitoring serves.
- [14-06 Integrated Catchment Studies](../06-integrated-catchment-studies/README.md) —
  the same measurements aggregated to the catchment scale.
- [18-03 Regularisation and Stabilisation](../../18-inverse-problems/03-regularization/README.md) —
  the general theory of the trade-off each lesson measures.
