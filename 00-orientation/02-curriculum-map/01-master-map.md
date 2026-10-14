---
id: 00-02-01
title: "Master Curriculum Map: How the 27 Folders Connect"
level: beginner
prereqs: ["00-01-02"]
estimated_minutes: 40
tags: [curriculum, navigation, study-planning]
---

# Master Curriculum Map: How the 27 Folders Connect

## Learning objectives

- Describe the four functional layers of the curriculum and name the folders
  that belong to each.
- Explain, for any folder, what it contains, what it depends on, and which
  folders depend on it.
- Distinguish a *topic* map (what the folders cover) from a *difficulty* map
  (what level each lesson is written at).
- Construct a defensible study route for a stated goal using the map plus the
  [dependency graph](./02-dependency-graph.md).

## Prerequisites

[The Six Stages and Their Mastery Checkpoints](../01-study-roadmap/02-six-stages.md)
for the stage vocabulary used throughout, and
[Repository Navigation and File Naming Conventions](../03-how-to-use-this-repo/01-navigation.md)
for how folders, modules and lessons are laid out on disk.

## 1. Why a folder map is necessary

The curriculum contains 27 topic folders, 216 modules and more than a thousand
planned lessons. (Those counts are read from the plan itself and grow as lessons
are written; [CURRICULUM.md](../../CURRICULUM.md) always reports the current
figures.) Reading that table alphabetically, or in folder order, is possible;
understanding *why* folder 18 comes after folder 05 is what makes the order
usable.

Three questions the map answers:

1. **What is in here?** Each folder has one subject, stated in its title.
2. **What does it need?** Each folder declares prerequisites in its `README.md`
   and, more precisely, in the dependency graph.
3. **What does it feed?** Where the skill will be used next — which is usually
   what motivates a topic that otherwise feels abstract.

## 2. The four layers

The 27 folders are not a flat list. They are grouped into four functional layers,
which the root [README](../../README.md) also states:

| Layer | Folders | Function |
|---|---|---|
| Orientation | 00 | How to study, what depends on what, how to run and extend the repository |
| Foundations | 01–03 | Mathematics, physics, scientific computing: the language and the tools |
| Earth context and methods | 04–17 | Earth science background, core geophysics, then the domain methods |
| Inference and computation | 18–22 | Inverse problems, numerical modelling, signal processing, statistics, data engineering |
| Practice and integration | 23–26 | Fieldwork and instruments, writing, projects, reference library |

Two features of this arrangement cause most of the confusion:

- **The inference layer (18–22) is not "last" in the sense of advanced-only.** It
  is the shared toolkit that domain folders in 06–17 draw on. A seismology
  inversion needs [18-inverse-problems](../../18-inverse-problems/README.md)
  before the seismology module that uses it. That is why the dependency graph
  interleaves folders instead of running 01→27.
- **Folder 26 is a reference library, not a course.** It is designed to be read
  out of order, at any stage, whenever you need a symbol, unit, formula,
  textbook or dataset.

## 3. The folders in detail

The table gives, for each folder, its subject; where it sits in the layers; and —
the column that matters most for planning — what typically comes next.

### Orientation

| Folder | Modules / lessons | Subject | Feeds into |
|---|---|---|---|
| [00-orientation](../../00-orientation/README.md) | 4 / 18 | Method, curriculum map, repository use, what geophysics is | everything; read once, revisit at stage transitions |

### Foundations

| Folder | Modules / lessons | Subject | Feeds into |
|---|---|---|---|
| [01-mathematics](../../01-mathematics/README.md) | 16 / 111 | Arithmetic to functional analysis; the language of the subject | 02, 18, 19, 20, 21, and every quantitative method |
| [02-physics](../../02-physics/README.md) | 11 / 73 | Mechanics, waves, elasticity, thermodynamics, fluids, electromagnetism, potential theory | 05, 06, 07, 08, 09, 10, 12, 13, 16 |
| [03-scientific-computing](../../03-scientific-computing/README.md) | 13 / 86 | Python, NumPy/SciPy/pandas, plotting, ObsPy, PyGMT, testing, packaging | 05 onwards; all computation-heavy folders |

### Earth context and core

| Folder | Modules / lessons | Subject | Feeds into |
|---|---|---|---|
| [04-earth-science-geology](../../04-earth-science-geology/README.md) | 8 / 37 | Earth structure, plate tectonics, stratigraphy, structural geology, hazards | 05, 11, 12, 13, 14 |
| [05-core-geophysics](../../05-core-geophysics/README.md) | 9 / 48 | What is measured, forward modelling, rock physics, survey design, processing, logging | 06–20 |

[05-core-geophysics](../../05-core-geophysics/README.md) is the hinge of the
curriculum: it is the first folder that is *about* geophysics rather than about a
contributing discipline, and it defines the property-contrast vocabulary that
every domain folder reuses.

### Domain methods

| Folder | Modules / lessons | Subject | Notes |
|---|---|---|---|
| [06-seismology](../../06-seismology/README.md) | 13 / 79 | Elastic waves, rays, sources, location, tomography, reflection, hazard | Largest method folder; underpins 12, 13, 25 |
| [07-gravity-geodesy](../../07-gravity-geodesy/README.md) | 7 / 35 | Gravity, instruments, anomalies, reference frames, satellite gravimetry, tides | Underpins 12, 15, 17 |
| [08-geomagnetism-electromagnetism](../../08-geomagnetism-electromagnetism/README.md) | 6 / 34 | The geomagnetic field, induction, magnetotellurics | Underpins 09, 12, 17 |
| [09-electrical-em-methods](../../09-electrical-em-methods/README.md) | 7 / 31 | Resistivity, induced polarisation, self-potential, controlled-source EM | Underpins 10, 11, 14 |
| [10-gpr-near-surface](../../10-gpr-near-surface/README.md) | 6 / 26 | Ground-penetrating radar and shallow-subsurface methods | Applied arm of 09; feeds 14, 23 |
| [11-exploration-geophysics](../../11-exploration-geophysics/README.md) | 7 / 31 | Mineral, hydrocarbon, geothermal, groundwater, geotechnical workflows | Integrates 06–10 |
| [12-global-geophysics-interior](../../12-global-geophysics-interior/README.md) | 7 / 25 | Reference Earth models, mineral physics, core, planetary interiors | Integrates 06, 07, 08, 13 |
| [13-geodynamics-tectonics](../../13-geodynamics-tectonics/README.md) | 7 / 26 | Rheology, mantle convection, plate kinematics, geodynamic modelling | Needs 19 for modelling |
| [14-hydrology-hydrogeophysics](../../14-hydrology-hydrogeophysics/README.md) | 6 / 28 | Aquifers, contaminant transport, hydrogeophysical monitoring | Integrates 09, 10, 21 |
| [15-oceanography-marine](../../15-oceanography-marine/README.md) | 6 / 26 | Physical oceanography and marine geophysical methods | Needs 06, 07, 16 |
| [16-atmosphere-climate](../../16-atmosphere-climate/README.md) | 9 / 43 | Atmospheric physics, radiation, circulation, climate models, attribution | Needs 02, 19, 21 |
| [17-remote-sensing-gis](../../17-remote-sensing-gis/README.md) | 8 / 41 | Optical, thermal and radar sensing, InSAR, GIS, geospatial analysis | Needs 03, 07; feeds 13, 16, 23 |

### Inference, computation and statistics

| Folder | Modules / lessons | Subject | Notes |
|---|---|---|---|
| [18-inverse-problems](../../18-inverse-problems/README.md) | 9 / 52 | Ill-posedness, regularisation, nonlinear and Bayesian inversion, uncertainty quantification | The methodological core of the whole curriculum |
| [19-numerical-modeling-hpc](../../19-numerical-modeling-hpc/README.md) | 8 / 39 | Finite difference, finite element, spectral methods, verification, parallel computing | Needed by 13, 16, 18 |
| [20-signal-processing](../../20-signal-processing/README.md) | 8 / 37 | LTI systems, Fourier analysis, filtering, deconvolution, array processing | Needed by 06, 10, 17 |
| [21-statistics-bayesian-ml](../../21-statistics-bayesian-ml/README.md) | 9 / 53 | Statistics, geostatistics, Bayesian inference, machine learning | Needed by 14, 16, 18 |
| [22-data-engineering-reproducibility](../../22-data-engineering-reproducibility/README.md) | 7 / 34 | Formats, pipelines, containers, databases, open science | Needed by every data-heavy project |

### Practice and integration

| Folder | Modules / lessons | Subject | Notes |
|---|---|---|---|
| [23-field-methods-instruments](../../23-field-methods-instruments/README.md) | 7 / 38 | Fieldwork, instrumentation, laboratory measurement, safety | Turns theory into an operation |
| [24-research-papers-writing](../../24-research-papers-writing/README.md) | 6 / 31 | Reading, writing, presenting, research rigour, publication | Needed for M5 and M6 in [Research Milestones](../01-study-roadmap/05-milestones.md) |
| [25-projects-capstone](../../25-projects-capstone/README.md) | 6 / 31 | Staged projects from beginner to a capstone study | Where everything is integrated |
| [26-reference-library](../../26-reference-library/README.md) | 6 / 33 | Glossary, symbols and units, formula handbook, textbooks, datasets, open educational resources | Consultation only; no prerequisites |

## 4. How to read the table

**"Feeds into" is not a strict dependency.** It lists where a folder's content is
needed. A strict, ordered version of the same information — including the
direction of each edge and the folders that can be studied in parallel — is the
[dependency graph](./02-dependency-graph.md).

**Module and lesson counts are structural, not a workload.** They show where the
mass of the curriculum sits. Mathematics and seismology are deliberately deep
because almost everything else rests on them. A count of 111 planned mathematics
lessons does not mean you must read all of them before doing geophysics; see
[diagnostic placement](../01-study-roadmap/03-self-assessment.md).

**Levels live in the lessons, not the folders.** Every lesson declares a level in
its frontmatter, and each folder has a *stage range* (`beginner→research` and so
on) rather than a single difficulty. Folder 06 contains both "what a seismogram
looks like" and decades-old open problems.

## 5. Three worked routes

These illustrate how the map is used in practice. They are plans, not
prescriptions.

**Route A — "I want to understand earthquakes and seismic hazard."**

```text
00-orientation
  → 01-mathematics (arithmetic → single-variable calculus → linear algebra)
  → 02-physics (measurement → mechanics → oscillations and waves → elasticity)
  → 03-scientific-computing (Python → NumPy → plotting → ObsPy)
  → 05-core-geophysics (what geophysics measures → forward modelling principles)
  → 06-seismology (elastic waves → rays → sources → location and magnitude
                   → hazard statistics)
  → 20-signal-processing and 18-inverse-problems in parallel, as the
    seismology modules call for them
```

**Route B — "I want to find and manage groundwater."**

```text
00-orientation
  → 01-mathematics, 03-scientific-computing, 02-physics/07-electromagnetism
  → 05-core-geophysics
  → 09-electrical-em-methods (electrical properties → DC resistivity → IP)
  → 10-gpr-near-surface (GPR principles → acquisition → applications)
  → 14-hydrology-hydrogeophysics (hydrology fundamentals → hydrogeophysics
                                  → contaminant transport → integrated catchments)
  → 21-statistics-bayesian-ml for geostatistics and uncertainty
```

**Route C — "I want to work on climate and the Earth system."**

```text
00-orientation
  → 01-mathematics (calculus, ODEs/PDEs, statistics)
  → 02-physics (thermodynamics → fluids → radiation)
  → 03-scientific-computing (pandas, gridded data, plotting)
  → 16-atmosphere-climate (structure → radiation → circulation → climate system
                           → climate models → observation and data)
  → 17-remote-sensing-gis for the observational side
  → 15-oceanography-marine for ocean heat transport, and 12-global-geophysics-interior
    for ice-mass and sea-level constraints from gravity and geodesy
```

Notice that all three routes share the same spine — 01, 02, 03, 05 — and diverge
afterwards. That spine is why the foundations are worth doing properly rather
than skipping towards the interesting parts.

## 6. Where the map stops being enough

The map tells you what depends on what. It does not tell you:

- **How long anything takes.** Depends on prior background, available hours, and
  how much you derive versus read.
- **Which parts you can skip.** The [diagnostic](../01-study-roadmap/03-self-assessment.md)
  and the stage checkpoints answer that for you, per folder.
- **What is research-current.** The curriculum teaches durable methods; for the
  current state of a field, read the recent literature via
  [24-research-papers-writing/01-reading-research-literature](../../24-research-papers-writing/01-reading-research-literature/README.md).

## Common mistakes

1. **Reading folder order as difficulty order.** Folder 18 is not "after" folder
   06 in difficulty; both contain beginner and research material.
2. **Skipping the inference layer until the end.** Regularisation and uncertainty
   are needed long before folder 25.
3. **Treating 26-reference-library as a course to complete.** It is a lookup
   table.
4. **Planning by folder count instead of by checkpoint.** "Finish 01" is not a
   goal; "derive and verify the wave equation" is.
5. **Ignoring parallel study.** Several folders are designed to be studied
   concurrently, for example mathematics alongside computing, and signal
   processing alongside seismology.

## Real-world applications

- **Choosing a specialisation.** Comparing two routes from this map is exactly
  what an MSc or PhD application requires you to justify.
- **Curriculum design and teaching.** The same layer-and-prerequisite logic is
  how degree programmes sequence modules, and how employer training paths are
  built.
- **Team planning.** A multi-disciplinary survey team is a live instance of this
  map: geodesy for reference frames, potential fields and EM for property
  contrasts, seismology for geometry, and inversion to combine them.

## Further reading

- Feynman, R. P., Leighton, R. B., & Sands, M. (1963–65). *The Feynman Lectures
  on Physics*, Vol. I, Ch. 1. Addison-Wesley. — On why understanding a subject
  means knowing where each piece sits relative to the others, rather than
  remembering each piece separately.
- Wiggins, G., & McTighe, J. (2005). *Understanding by Design* (2nd ed.).
  Association for Supervision and Curriculum Development. — "Backward design":
  start from the capability you want and derive the sequence of study, which is
  the logic behind the routes in section 5.
- Lowrie, W., & Fichtner, A. (2020). *Fundamentals of Geophysics* (3rd ed.).
  Cambridge University Press. — A broad survey of the subject; useful as a
  cross-check on how the folders here relate.
  These are bibliographic records; confirm availability through your library or a
  DOI resolver before citing them yourself.

## Related lessons

- [Prerequisite Dependency Graph and Valid Study Orders](./02-dependency-graph.md)
- [Domain Tracks: Seismology, Potential Fields, EM, Climate, Near-Surface](./03-domain-tracks.md)
- [Cross-Cutting Skills: Mathematics, Computing, Inverse Theory](./04-cross-cutting.md)
- [The Six Stages and Their Mastery Checkpoints](../01-study-roadmap/02-six-stages.md)
