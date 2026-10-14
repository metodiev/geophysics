# 14 — Hydrology, Hydrogeophysics and Environmental Geophysics

**Stages:** intermediate → research

In the shallow subsurface, almost every geophysical signal is a signal about
water. Resistivity is controlled by the water content and the conductivity of the
pore fluid; seismic velocity responds to saturation through the bulk modulus and
the density; permittivity is dominated by the dielectric contrast between water
and everything else; density and gravity respond to the mass of the water; and
temperature, self-potential and NMR all have hydrological interpretations that
are their primary ones. That is the opportunity of this folder: the shallow
geophysical methods are not merely capable of answering hydrological questions,
they are *sensitive* to the quantities hydrology wants — and sensitive in ways
that a piezometer, a borehole or a flow measurement is not.

It is also the folder's central honest difficulty. **A geophysical change is a
hydrological statement only when a petrophysical link is stated and its ambiguity
acknowledged.** A resistivity drop of a factor of three may be a wetting front, a
salinity front, a temperature change or an artefact of a drifting electrode, and
the measurement alone cannot say which: the resistivity depends on the *product*
of a pore-geometry term and the pore-fluid conductivity, and one number per
location cannot separate a product. Every lesson in this folder therefore either
derives that ambiguity, quantifies it, or shows what additional measurement
removes it — and states which of the three it is doing. Where a lesson presents a
water content, it names the Archie exponents; where it presents a velocity, it
names the saturation model; where it presents a storage volume, it names the
specific yield and says who measured it.

A second difficulty follows from the first. Hydrology is about fluxes — recharge,
discharge, exchange, capture — and geophysics is mostly about states and
geometry. Converting one into the other requires a link (a porosity, a specific
yield, a dispersivity), and the link is usually the least-measured part of the
chain. The folder's later modules make this explicit: the catchment storage is
dominated by the specific yield, which no refraction survey measures; the
reach-scale exchange flux is a Darcy velocity in one method and a seepage
velocity in another, differing by an effective porosity that neither measures;
and the sustainable yield of an aquifer is a decision with a probability
attached, not a number. An integrated study is limited by its least-identified
link, and the skill this folder teaches is saying which link that is.

The folder is organised as a progression of scales. Modules 01–03 establish the
hydrology and the petrophysics: the water balance and Darcy's law, the geophysical
methods used in the shallow subsurface, and the relations — Archie, Gassmann,
Kozeny–Carman — that connect what is measured to what is wanted. Module 04 applies
them to contaminants and environmental problems, where the ambiguity is the point
rather than an inconvenience. Module 05 adds time: two surveys, a difference, and
the resolution and detection analysis that makes a monitoring programme
defensible. Module 06 integrates to the catchment and the water-resource
decision, where the uncertainty budget, not the estimate, is the deliverable.

## Learning objectives for the folder

By the end of this folder you will be able to:

1. **Close** a hydrological water balance over a record, and **distinguish** the
   quantities it measures from those it merely reassigns.
2. **Apply** Darcy's law to compute a specific discharge, a transmissivity and a
   leakage between compartments, with units and sign conventions stated.
3. **Compute** the response of an unconfined or confined aquifer to pumping, and
   **report** the aquifer parameters a pumping test does and does not determine.
4. **Map** between resistivity, saturation and pore-water conductivity with a
   stated petrophysical model, and **quantify** the equivalence it leaves open.
5. **Choose** a geophysical method and geometry for a stated hydrological target,
   and **justify** the choice by a sensitivity or detection calculation.
6. **Derive** the forward response of the shallow methods used here — ERT
   soundings, EM induction, refraction, GPR, microgravity — and **verify** each
   against an analytic limit or an independent calculation.
7. **Invert** shallow geophysical data, and **report** the regularisation, the
   resolution and the range of models consistent with the data.
8. **Detect** a change in a time-lapse data set against a stated error model, and
   **design** the array that makes a given change visible.
9. **Interpret** a contaminant, salinity or permafrost target in terms of the
   petrophysical link it requires, and **name** the ambiguity it carries.
10. **Measure** a reach-scale groundwater–surface water exchange flux by at least
    two methods, **state** what each measures, and **reconcile** them.
11. **Estimate** recharge by at least two independent methods and **explain**
    their disagreement rather than averaging it away.
12. **Assimilate** a geophysical estimate into a hydrological model, and
    **demonstrate** how a biased observation operator produces a confident, wrong
    state.

## Modules

Modules are in dependency order. Module numbers are *not* difficulty labels.

| # | Module | Focus | Why it matters downstream |
|---|---|---|---|
| 01 | [Hydrology Fundamentals for Geophysicists](./01-hydrology-fundamentals/README.md) | The hydrologic cycle, aquifers, Darcy's law, well hydraulics, groundwater chemistry, the unsaturated zone | The vocabulary and the physics every later module assumes: what a head, a flux and a storage coefficient mean |
| 02 | [Hydrogeophysical Methods](./02-hydrogeophysics-methods/README.md) | ERT, EM and TDEM, seismics, GPR, surface NMR, microgravity, borehole methods | The shallow-subsurface toolkit, each method with its sensitivity and its depth range |
| 03 | [Petrophysical Relations for Saturated Media](./03-petrophysics-hydrology/README.md) | Porosity–permeability, Archie, velocity–saturation and Gassmann, proxy construction | The link between what is measured and what is wanted — and the source of the ambiguity |
| 04 | [Contaminant and Environmental Geophysics](./04-contaminant-and-environmental/README.md) | Plumes, landfill leachate, seawater intrusion, acid mine drainage, permafrost | The applied problems where a geophysical image is the only practical monitoring tool |
| 05 | [Time-Lapse and Monitoring Hydrogeophysics](./05-hydrogeophysical-monitoring/README.md) | Time-lapse ERT, cross-borehole monitoring and tracers, data assimilation | The time dimension, and the analysis that makes monitoring defensible |
| 06 | [Integrated Catchment and Watershed Studies](./06-integrated-catchment-studies/README.md) | Catchment characterisation, groundwater–surface water interaction, water-resource assessment | The integration of all of it into a water balance, a flux and a decision |

## The dependency spine

```text
14-01 Hydrology fundamentals ──┬──> 14-02 Hydrogeophysical methods ──┬──> 14-04 Contaminant & environmental
        │                      │                                     │
        │                      ├──> 14-03 Petrophysical relations ────┤
        │                      │          │                          │
        │                      │          └──> 14-05 Monitoring ─────┴──> 14-06 Integrated catchment
        │                      │                    │
        └──────────────────────┴────────────────────┴──> 04 Earth science, 09 Electrical/EM, 10 GPR, 11 Exploration
```

Four rules of thumb follow:

1. **No water content before the petrophysical link.** Module 03 is a
   prerequisite for every interpretation in 04, 05 and 06, because it is what
   turns a resistivity or a velocity into a hydrological quantity.
2. **A state is not a flux.** Modules 01–04 give states and geometry; 05 adds
   change; 06 converts both into fluxes. The conversion always imports a
   parameter (a porosity, a specific yield, a dispersivity) that must be named.
3. **Every ambiguity is resolved by an independent measurement, not by a better
   inversion.** The salinity/saturation equivalence, the velocity/thickness
   trade-off and the null space of a cross-hole survey are all properties of the
   physics and the geometry, and each lesson says which extra measurement (or
   which assumption) breaks it.
4. **The uncertainty budget is the deliverable.** A storage volume, an exchange
   flux or a sustainable yield is only usable with the distribution of the
   quantity and the list of what was assumed; the later modules are written so
   that the budget, not the estimate, is the result.

## Which modules do you actually need?

| Goal | Minimum path |
|---|---|
| Understand what groundwater is and how it moves | 01 |
| Plan or interpret a shallow geophysical survey | 01, 02 |
| Convert a resistivity or a velocity into a water content | 01, 02, 03 |
| Map a contaminant plume or a saline intrusion | 01, 02, 03, 04 |
| Monitor a change over time | 01, 02, 03, 05 |
| Feed geophysics into a hydrological model | 01, 03, 05 |
| Characterise a catchment | 01, 02, 03, 05, 06 |
| Assess recharge or a sustainable yield | 01, 02, 06 (with 03 for any geophysical estimate) |
| Work on permafrost or other coupled thermal problems | 01, 02, 04 (optionally 09, 10) |

## Suggested paths

**If you are new to hydrogeology:** modules 01 and 02 in full, in order, running
each demonstration and doing the exercises. They are the two modules on which the
rest of the folder stands. Then take module 03 — the petrophysical links — before
attempting any interpretation, because every later lesson assumes you can state
one.

**If you come from geophysics and want the hydrology:** read
[01-02](./01-hydrology-fundamentals/02-aquifer-types-and-properties.md),
[01-03](./01-hydrology-fundamentals/03-hydraulic-head-darcy.md) and
[03-02](./03-petrophysics-hydrology/02-archie-and-saturation.md), then
[14-06-01](./06-integrated-catchment-studies/01-catchment-characterisation.md).
Those four carry the content that the remaining lessons apply; skim module 01's
descriptive sections for vocabulary.

**If you are preparing a monitoring programme:** module 05 in full, with
[04-04](./04-contaminant-and-environmental/04-acid-mine-drainage.md) for an
application where time-lapse is the only practicable method, and module 06's
lesson 02 for the reach-scale boundary conditions that monitoring usually has to
satisfy.

**If you are preparing a water-resource assessment:** modules 01 and 06, with
[14-03-04](./03-petrophysics-hydrology/04-geophysical-proxy-relations.md) and
[14-02-06](./02-hydrogeophysics-methods/06-gravity-for-groundwater.md) for the
two measurements — a proxy relation and a storage-change estimate — that
constrain the quantities a water balance cannot.

**If you are preparing a research project:** the resolution, detection and
equivalence analyses of module 05 (Sections 5–8 of each lesson) and the error
budgets of module 06, plus the ★★★ exercises throughout. Each is a worked example
of stating what a data set does *not* determine.

## Mastery checkpoint for the folder

Produce one integrated artefact:

> **From a geophysical measurement to a hydrological statement, with its
> ambiguity named.** Choose a SYNTHETIC shallow-subsurface scenario of your own
> construction (you may generate it with the forward models in these modules):
> a soil profile, an aquifer reach, a plume, or a small catchment. Then:
> (a) state the hydrological quantity you want and the quantity a geophysical
> method actually measures; (b) state the petrophysical link between them, with
> its parameters and their values, and derive the ambiguity the link leaves open;
> (c) design the survey or the monitoring programme for the target, justifying
> the geometry with a detection calculation against a stated error model;
> (d) carry out the forward calculation, verify it against an analytic limit or a
> mass balance, and then invert or interpret it; (e) report the result with its
> resolution or equivalence class, the regularisation or the assumption that
> fixed the answer, and the uncertainty budget that dominates it; (f) name the
> one additional measurement that would most reduce that dominant uncertainty, and
> say what it would cost. The point of the checkpoint is (a), (b), (f) — the
> accounting — not the numbers.

A worked version of the (a)–(b) portion for a resistivity estimate appears in the
module 05 lesson-01 exercises, and the (e) portion in the module 06 lesson-03
solutions.

## Conventions used throughout

| Symbol | Meaning | Typical unit |
|---|---|---|
| $\theta$ | Volumetric water content | m³/m³ (often written as %) |
| $S$ | Saturation, $S = \theta/\phi$ | dimensionless |
| $\phi$ | Porosity | dimensionless |
| $\rho$ | Bulk electrical resistivity | Ω·m |
| $\rho_w$ | Pore-water resistivity | Ω·m |
| $\sigma$ | Electrical conductivity, $\sigma = 1/\rho$ | S/m |
| $m, n$ | Archie cementation and saturation exponents | dimensionless |
| $K$ | Hydraulic conductivity | m/d (or m/s) |
| $T$ | Transmissivity, $T = Kb$ | m²/d |
| $S_s, S_y$ | Specific storage; specific yield | m⁻¹; dimensionless |
| $h$ | Hydraulic head (or depth to water, where stated) | m |
| $q$ | Specific discharge (Darcy flux), $q = -K\nabla h$ | m/d |
| $v$ | Seepage (pore-water) velocity, $v = q/n_e$ | m/d |
| $n_e$ | Effective (mobile) porosity | dimensionless |
| $Q$ | Discharge or pumping rate | m³/d (stream: m³/s where stated) |
| $c$ | Solute concentration | kg/m³ or mg/L |
| $D_L, D_T$ | Longitudinal and transverse dispersion coefficients | m²/d |
| $\alpha_L$ | Dispersivity, $\alpha_L = D_L/v$ | m |
| $\kappa$ | Thermal diffusivity | m²/s |
| $d$ | Thermal skin depth, $d=\sqrt{2\kappa/\omega}$ | m |
| $\Delta h$ | Head difference | m |

Full definitions are in the
[symbol handbook](../26-reference-library/02-symbols-and-units/01-symbol-handbook.md);
the rounded constants these modules use as anchors are in the
[constant handbook](../26-reference-library/02-symbols-and-units/03-constant-handbook.md).

## A caution about numbers in this folder

Hydraulic conductivities, porosities, dispersivities, recharge rates, Archie
exponents and salinities **vary** — between regions, between formations and
between analysts of the same data. Where this folder gives a number it gives a
*teaching value* with its units and its provenance: a synthetic model, or a named
standard constant (for example the limiting molar conductivity of NaCl, used in
module 05's tracer lesson). It never gives an unsourced figure with the authority
of a measurement, and it names no real catchment, aquifer, well or reach.

Every demonstration is reproducible from the code in its module's `code/`
directory, is print-only (no figures and no `plt.show()`), uses a fixed random
seed (`np.random.default_rng(20261014)`), and requires no network access.
Unless a lesson explicitly says otherwise, **all models and data in this folder
are SYNTHETIC**, and every derived number in a lesson is printed by the
demonstration that accompanies it.

## How to use the code

Every module carries a `code/` directory of self-contained demonstrations and an
`exercises/` directory of graded problems with worked solutions. Run a module's
demos with the project virtual environment, from the module's `code/` directory;
each module README lists its own commands. For example:

```bash
cd 14-hydrology-hydrogeophysics/01-hydrology-fundamentals/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python hydrologic_cycle_demo.py
```

The demonstrations print labelled results with units rather than plotting,
because the numbers — and their units and their sensitivity to an assumption —
are the result. Where a lesson quotes a value, the demonstration that produced it
is named in the lesson's own demonstration section, and the section of its output
is identified.

The repository-wide quality gate, which checks structure, frontmatter, links and
LaTeX, is documented in
[03-quality-gate](../00-orientation/03-how-to-use-this-repo/03-quality-gate.md).

## Where this folder sits

Hydrology and hydrogeophysics sit between the Earth-context folders and the
applied and mathematical ones, and they are the shallowest of the geophysical
applications. The folder assumes
[04-earth-science-geology](../04-earth-science-geology/README.md) for what the
shallow subsurface is made of and
[05-core-geophysics](../05-core-geophysics/README.md) for what a geophysical
measurement is. It depends on
[09-electrical-em-methods](../09-electrical-em-methods/README.md),
[10-gpr-near-surface](../10-gpr-near-surface/README.md) and
[06-seismology/10](../06-seismology/10-refraction-and-near-surface-seismology/README.md)
for the physics and the acquisition of the methods it time-steps and integrates,
and on [18-inverse-problems](../18-inverse-problems/README.md),
[20-signal-processing](../20-signal-processing/README.md) and
[21-statistics-bayesian-ml](../21-statistics-bayesian-ml/README.md) for the
inversion, filtering and uncertainty machinery it uses. It supplies the shallow
subsurface context to
[11-exploration-geophysics](../11-exploration-geophysics/README.md),
[16-atmosphere-climate](../16-atmosphere-climate/README.md) and
[17-remote-sensing-gis](../17-remote-sensing-gis/README.md), and its field
practice is shared with
[23-field-methods-instruments](../23-field-methods-instruments/README.md).
