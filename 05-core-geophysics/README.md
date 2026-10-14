# 05 — Core Geophysics: Principles and Methods

**Stages:** intermediate → graduate

Every geophysical method — seismic, gravity, magnetic, electrical, electromagnetic,
radar — is a variation on one idea: **a contrast in a physical property produces a
measurable signal**. A rock is not "detected"; a *difference* between two rocks is
detected. Everything else in this folder is the working-out of that sentence.
What property does each method respond to? What does the signal look like as a
function of the geometry? What limits the resolution, and at what depth? When two
different Earth models produce the same data, how do we choose between them? This
folder answers those questions once, in method-independent terms, so that the
domain folders (06–17) can go straight to their own physics without re-deriving
the common foundations each time.

The organising principle is that this folder is about **the shared machinery of
measurement and inference**, not about any one technique. It is deliberately
placed after the mathematics (01), physics (02) and computing (03) foundations and
after the Earth context (04), and before the domain methods. Everything it states
is used by at least three later folders.

Three distinctions recur often enough to state once:

- **The forward problem versus the inverse problem.** A forward model predicts
  data from a model; an inverse problem estimates a model from data. Geophysics
  is mostly inverse, but it is *only ever* solved through forward models, and
  this folder builds both: the analytic and numerical forward models of module 03
  and the non-uniqueness analysis that comes with inverting them.
- **Resolution versus penetration.** Energy that reaches deep enough to see a
  target is, by the physics of diffusion or of long wavelengths, too coarse to
  resolve it finely. Module 01 states the trade-off, and every later method is an
  instance of it.
- **Measured versus inferred versus assumed.** A field reading is measured; an
  anomaly is computed; a depth is inferred from the anomaly under an assumed
  model; a rock type is a further inference on top of that. Every lesson labels
  where on that chain it is operating, because the uncertainty lives in the
  assumptions, not in the reading.

## Learning objectives for the folder

By the end of this folder you will be able to:

1. **Identify** the physical-property contrast each geophysical method responds
   to, and predict, from a stated target and background, whether a signal will be
   detectable.
2. **Classify** methods by source and receiver geometry, by active versus passive
   acquisition, and by the field quantity measured.
3. **State** the resolution–depth trade-off quantitatively for a chosen method,
   and choose a method whose resolution and penetration match a stated objective.
4. **Explain** why geophysical inverse problems are non-unique, and demonstrate at
   least one exact non-uniqueness for a simple body.
5. **Distinguish** scalar and vector fields, obtain a field from its potential,
   and interpret gradients and their units.
6. **Reduce** raw observations to anomalies — removing drift, tides, instrument
   bias and a reference field — and state what each reduction assumes.
7. **Build** forward models analytically for a sphere, a sheet and a dyke, and
   numerically for an arbitrary body, and **validate** the numerical code against
   the analytic benchmark.
8. **Use** rock-physics relations — porosity–density–velocity, effective-medium
   bounds, Gassmann fluid substitution, empirical velocity–clay relations — and
   state the regime in which each is valid.
9. **Design** a survey: choose the array geometry, fold, offsets and spatial
   sampling that meet a target resolution while avoiding spatial aliasing.
10. **Process** a data set end to end — editing, correction, enhancement, statics,
    gain, merging, levelling — and document it so the result is reproducible.
11. **Interpret** anomalies qualitatively and quantitatively, integrate multiple
    methods, ground-truth the result, and report it with an honest uncertainty.
12. **Interpret** borehole logs, tie them to seismic, and estimate petrophysical
    quantities with their uncertainty.

## Modules

Modules are in dependency order. Module numbers are *not* difficulty labels.

| # | Module | Focus | Why it matters downstream |
|---|---|---|---|
| 01 | [What Geophysics Measures and Why](./01-what-geophysics-measures/README.md) | Property contrasts, method taxonomy, the resolution–depth trade-off, non-uniqueness, method selection | The framing that every domain folder assumes |
| 02 | [Geophysical Fields and Observables](./02-geophysical-fields-and-observables/README.md) | Scalar and vector fields, potentials, units, noise and drift, reduction to anomalies | The language in which all field data is expressed |
| 03 | [Forward Modelling Principles](./03-forward-modelling-principles/README.md) | The forward problem, analytic bodies, superposition, numerical modelling, validation | The engine of every inversion in folders 06–22 |
| 04 | [Rock Physics and Property Relations](./04-rock-physics/README.md) | Porosity–density–velocity, effective-medium theory, Gassmann, clay models, anisotropy, attenuation, Archie's law | Links a geophysical property to a rock and a fluid |
| 05 | [Survey Design and Data Acquisition Principles](./05-survey-design-and-acquisition/README.md) | Survey planning, array geometry and fold, spatial sampling, GNSS positioning, acquisition QC | The decisions that bound the quality of every later result |
| 06 | [Data Processing Principles](./06-data-processing-principles/README.md) | The processing pipeline, noise suppression, statics, gain, gridding and levelling, reproducibility | The method-independent processing every survey needs |
| 07 | [Interpretation and Geological Integration](./07-interpretation-and-integration/README.md) | Qualitative and quantitative interpretation, multi-method integration, ground truthing, reporting, pitfalls | Turns a processed anomaly into a geological statement |
| 08 | [Borehole and Well-Log Geophysics](./08-geophysical-logging/README.md) | The borehole environment, gamma, resistivity, porosity and imaging logs, VSP, log interpretation | The ground truth for surface methods and the link to petrophysics |
| 09 | [Geothermal and Heat-Flow Methods](./09-geothermal-and-heat-flow-methods/README.md) | Heat-flow measurement, thermal conductivity, geothermal exploration geophysics | The thermal branch of the geophysical toolkit |

## The dependency spine

```text
05-01 What geophysics measures ──┬──> every domain folder (06–17) and 21
        │                        │
        └──> 05-02 Fields & observables ──> 07 Gravity, 08 Geomagnetism, 09 EM methods
                │
                ├──> 05-03 Forward modelling ──> 18 Inverse problems, 19 Numerical/HPC
                │
                ├──> 05-04 Rock physics ──> 11 Exploration, 14 Hydrology, 06 Seismology
                │
                ├──> 05-05 Survey design ──> 23 Field methods
                │
                └──> 05-06 Processing ──> 20 Signal processing
                        │
                        ├──> 05-07 Interpretation ──> 24 Research & writing
                        ├──> 05-08 Well logging ──> 11 Exploration, 14 Hydrology
                        └──> 05-09 Heat flow ──> 12 Interior, 13 Geodynamics
```

Three rules of thumb follow:

1. **Modules 01 and 02 before any domain folder.** A method's reach and its
   limits are set by the contrast it sees and the field it measures, and a
   domain folder that opens with a formula assumes you already know both.
2. **Module 03 is the engine, module 04 is the dictionary.** Forward modelling
   computes the signal a *physics* model produces; rock physics supplies the
   *physical properties* that model needs. Neither is useful without the other,
   and both are assumed in folders 06–17.
3. **Modules 05–08 are the workflow.** Design, acquire, process, interpret, and
   ground-truth. It is the sequence of an actual survey, and reading it in order
   is the shortest way to see why each step constrains the next.

## Which modules do you actually need?

| Goal | Minimum path |
|---|---|
| Understand what geophysics can and cannot see | 01, 02 |
| Build or trust a forward model | 03 |
| Convert a measurement into a rock property | 04 |
| Plan and run a field survey | 01, 05, 06 |
| Process and interpret survey data | 05, 06, 07 |
| Work with borehole data or petrophysics | 04, 08 |
| Work in geothermal exploration | 04, 09 |
| Work in exploration, mining or petroleum | 01, 04, 05, 06, 07 |
| Work in geodynamics or the deep interior | 02, 03, 04, 09 |

## Suggested paths

**If you are new to applied geophysics:** read modules 01 and 02 in full — they are
short and they set every term the rest of the repository uses. Then take module 03
(the forward problem, with its analytic and numerical halves) and module 04 (rock
physics). Only after those four should you pick a domain folder, because each
domain folder assumes this vocabulary.

**If you come from physics or mathematics and want the geophysics:** read
[01-03](./01-what-geophysics-measures/03-resolution-depth-tradeoff.md) for the
resolution limits and
[01-04](./01-what-geophysics-measures/04-ambiguity-and-nonuniqueness.md) for the
non-uniqueness argument — they are the two ideas that most distinguish geophysical
inference from ordinary parameter estimation. Then
[03-05](./03-forward-modelling-principles/05-forward-model-validation.md) for how
a numerical model is proved correct, and
[04-03](./04-rock-physics/03-gassmann-fluid-substitution.md) for the fluid
substitution that ties elastic properties to saturation.

**If you are here only to run surveys:** modules 05, 06 and 07 in order, with
module 03 as reference. Read
[05-03](./05-survey-design-and-acquisition/03-spatial-sampling-theory.md) before
you design a grid, and
[07-06](./07-interpretation-and-integration/06-interpretation-pitfalls.md) before
you interpret one.

**If you already know one method well:** read
[01-04](./01-what-geophysics-measures/04-ambiguity-and-nonuniqueness.md) and then
[07-03](./07-interpretation-and-integration/03-multi-method-integration.md). The
first tells you why your method alone cannot settle the answer; the second tells
you what to add.

## Mastery checkpoint for the folder

Produce one integrated artefact:

> **Design, forward-model and defend a survey.** Choose a target (a buried
> channel, an ore body, a fracture zone, a geothermal reservoir — state it
> precisely with a depth, a size and a property contrast). Then: (a) predict, from
> the property contrast, which two or three methods could see it, and which could
> not; (b) choose one method and justify the choice against the
> resolution–penetration trade-off; (c) build a forward model of the target —
> analytic if the geometry admits it, numerical otherwise — and validate the
> numerical model against an analytic benchmark; (d) design the survey geometry
> and spatial sampling that will resolve it without aliasing; (e) list the
> processing steps you will apply and the assumption each one imports; (f) state
> the non-uniqueness that remains after processing and the additional measurement
> — a second method, a borehole, a pit — that would most reduce it. A worked
> version of (c) and (d) appears in the module 03 and module 05 exercises; the
> point of the checkpoint is the chain of reasoning, not any single number.

This single exercise links modules 01, 03, 04, 05 and 07, and it is the reasoning
that the domain folders
[06-seismology](../06-seismology/README.md),
[11-exploration-geophysics](../11-exploration-geophysics/README.md) and
[14-hydrology-hydrogeophysics](../14-hydrology-hydrogeophysics/README.md) will
assume you can already do.

## Conventions used throughout

| Symbol | Meaning | Typical unit |
|---|---|---|
| $\phi$ | Porosity (volume fraction) | dimensionless |
| $\rho$ | Mass density | kg/m³, or g/cm³ in rock physics |
| $v_p, v_s$ | P- and S-wave speeds | m/s or km/s |
| $K$ | Bulk modulus | GPa |
| $\mu$ | Shear modulus | GPa |
| $\sigma$ | Electrical conductivity | S/m |
| $k$ | Permeability | m², or darcy in petrophysics |
| $\kappa$ | Thermal conductivity | W m⁻¹ K⁻¹ |
| $g$ | Gravitational acceleration (anomaly) | m/s², or mGal (1 mGal = 10⁻⁵ m/s²) |
| $B, T$ | Magnetic flux density | nT (1 nT = 10⁻⁹ T) |
| $Q$ | Quality factor (attenuation) | dimensionless |
| $S/N$ | Signal-to-noise ratio | dimensionless |

Full definitions are in the
[symbol handbook](../26-reference-library/02-symbols-and-units/01-symbol-handbook.md);
the rounded property values this folder uses as nominal anchors are in
[26-02-03 Physical Constants and Earth Parameters with Sources](../26-reference-library/02-symbols-and-units/03-constant-handbook.md).

## A caution about numbers in this folder

Property contrasts, resolutions, penetration depths and rock-physics parameters
**vary** — between sites, between rock types, and between instruments. Where this
folder gives a number it gives a *teaching value* with its units and its
provenance (a synthetic model, or a named standard constant), never an unsourced
figure with the authority of a measurement. Every demonstration is reproducible
from the code in its module's `code/` directory, is print-only, uses a fixed
random seed (`np.random.default_rng(20261014)`), and requires no network access.
Unless a lesson explicitly says otherwise, **all models and data in this folder
are SYNTHETIC**.

## How to use the code

Every module carries a `code/` directory of self-contained demonstrations and an
`exercises/` directory of graded problems with worked solutions. Run a module's
demos with the project virtual environment, from the module's `code/` directory;
each module README lists its own commands. For example:

```bash
cd 05-core-geophysics/03-forward-modelling-principles/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python validation_benchmarks.py
```

The repository-wide quality gate, which checks structure, frontmatter, links and
LaTeX, is documented in
[03-quality-gate](../00-orientation/03-how-to-use-this-repo/03-quality-gate.md).

## Where this folder sits

This is the first folder of the **domain methods** block. It assumes the
mathematical and physical foundations of
[01-mathematics](../01-mathematics/README.md) and
[02-physics](../02-physics/README.md), the computational practice of
[03-scientific-computing](../03-scientific-computing/README.md), and the Earth
context of [04-earth-science-geology](../04-earth-science-geology/README.md). It
supplies the shared principles on which
[06-seismology](../06-seismology/README.md) and every method-specific folder from
07 to 17 is built, and it is the source of the forward-model validation practice
that [18-inverse-problems](../18-inverse-problems/README.md) formalises.
