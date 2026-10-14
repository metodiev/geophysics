---
id: 00-02-02
title: "Prerequisite Dependency Graph and Valid Study Orders"
level: beginner
prereqs: ["00-02-01"]
estimated_minutes: 45
tags: [curriculum, prerequisites, study-planning]
---

# Prerequisite Dependency Graph and Valid Study Orders

## Learning objectives

- Read the curriculum's prerequisite structure as a directed graph, and explain
  what an edge means and what it does not mean.
- Identify the layers of the graph and the sets of folders that may be studied in
  parallel.
- Detect an invalid study order — an order that violates an edge — before
  spending weeks on it.
- Produce a personal study order for a chosen goal by topologically sorting the
  folders you actually need, rather than all 27.

## Prerequisites

[Master Curriculum Map: How the 27 Folders Connect](./01-master-map.md), which
gives the contents and layering that this lesson turns into ordered
prerequisites.

## 1. What a prerequisite edge means

An edge $A \rightarrow B$ ("$B$ requires $A$") means one of three specific
things, and it is worth knowing which one you are looking at:

1. **Notation prerequisite.** $B$ uses symbols or operations introduced in $A$.
   Example: [06-seismology](../../06-seismology/README.md) uses partial
   derivatives, so it requires
   [01-mathematics/06-multivariable-calculus](../../01-mathematics/06-multivariable-calculus/README.md).
2. **Concept prerequisite.** $B$ assumes a physical or mathematical idea whose
   justification lives in $A$. Example: seismic inversion assumes the
   ill-posedness argument developed in
   [18-inverse-problems/01-inverse-problem-foundations](../../18-inverse-problems/01-inverse-problem-foundations/README.md).
3. **Tool prerequisite.** $B$ assumes you can *do* something built in $A$.
   Example: any lesson with a Python demonstration requires
   [03-scientific-computing/01-python-fundamentals](../../03-scientific-computing/01-python-fundamentals/README.md).

What an edge does **not** mean:

- It does not mean "finish all of $A$". A seismology lesson that needs vector
  calculus needs the gradient, divergence and their physical meaning — not
  functional analysis.
- It does not mean the two must be studied years apart. A notation prerequisite
  is often best satisfied by one afternoon of targeted reading immediately before
  the dependent lesson (this is exactly what the
  [diagnostic](../01-study-roadmap/03-self-assessment.md) is for).
- It does not mean the dependency is symmetric or transitive by default. Chains
  are transitive; direct usefulness is not.

The authoritative machine-readable statement of what exists is
[`tools/curriculum_plan.py`](../../tools/curriculum_plan.py); the graph below
is the human-readable view of the same structure.

## 2. The graph

Layers run top to bottom. An arrow means "is required by". Folders inside the
same box have no edge between them and can be taken in any order, or in
parallel.

```text
LAYER 0  ── 00-orientation
                │
LAYER 1  ── 01-mathematics     02-physics     03-scientific-computing
                │                  │                  │
                └────────┬─────────┴──────────┬───────┘
                         v                    v
LAYER 2  ──────────── 04-earth-science-geology   03 → 22-data-engineering
                         │
                         v
LAYER 3  ────────────── 05-core-geophysics ────────── 23-field-methods-instruments
                         │
        ┌────────────────┼───────────────────┬──────────────────┐
        v                v                   v                  v
LAYER 4  06-seismology  07-gravity-geodesy  08-geomagnetism-EM  09-electrical-em
             │  │            │                  │                 │
             │  └────────────┤                  v                 v
             │               │             (induction, MT)  10-gpr-near-surface
             v               v                  │                 │
LAYER 5  20-signal-processing 17-remote-sensing-gis  ─────────────┤
             │                    │  │                             │
             │                    │  └──► InSAR, GNSS              │
             v                    v                                v
LAYER 6  12-global-interior  15-oceanography-marine   11-exploration 14-hydrology
             │    │              │                       │              │
             v    v              v                       │              │
LAYER 7  13-geodynamics-tectonics  16-atmosphere-climate │              │
             │         │                │                │              │
             └────┬────┴────────┬───────┘                │              │
                  v             v                         │              │
LAYER 8   19-numerical-modeling-hpc   21-statistics-Bayesian-ML         │
                  │             │                                    │
                  └──────┬──────┘                                    │
                         v                                            │
LAYER 9   18-inverse-problems  ◄─────────────────────────────────────┘
                         │
                         v
LAYER 10  24-research-papers-writing ──► 25-projects-capstone ◄── 23, all domains

ALONGSIDE (no prerequisites, no dependents)
          26-reference-library
```

## 3. The edges, spelled out

The two columns are the useful form: scan the right column for the folder you
want, and the left column is what must be available first.

| Folder you want | Prerequisites to have available |
|---|---|
| 01-mathematics | Arithmetic only; nothing else |
| 02-physics | 01 (algebra, calculus for mechanics and waves) |
| 03-scientific-computing | Arithmetic; programming assumed from zero |
| 04-earth-science-geology | None beyond school science; 01/02 help for structure and tectonics |
| 05-core-geophysics | 01, 02, 03 (units, physical reasoning, plotting) |
| 06-seismology | 02 (oscillations and waves, elasticity), 01 (multivariable calculus, PDEs), 03 |
| 07-gravity-geodesy | 02 (mechanics, potential theory), 01 (vector calculus, spherical coordinates) |
| 08-geomagnetism-electromagnetism | 02 (electromagnetism), 01 (vector calculus, PDEs) |
| 09-electrical-em-methods | 08 (induction concepts) or 02/07 (electromagnetism), 05 |
| 10-gpr-near-surface | 02/07 and 09 (EM basics); 20 helpful for processing |
| 11-exploration-geophysics | 05 plus at least two of 06–10; 23 for acquisition realism |
| 12-global-geophysics-interior | 05, 06, 07, 08 (one or more of 06–08 depending on module) |
| 13-geodynamics-tectonics | 02 (fluids, continuum mechanics), 04 (tectonics), 19 for modelling |
| 14-hydrology-hydrogeophysics | 09 or 10, 04, 21 for geostatistics and uncertainty |
| 15-oceanography-marine | 02 (fluids, thermodynamics), 06 and 07 for marine methods |
| 16-atmosphere-climate | 02 (thermodynamics, radiation, fluids), 19 and 21 for modelling |
| 17-remote-sensing-gis | 03 (geospatial Python), 07 (geodesy, reference frames) |
| 18-inverse-problems | 01 (linear algebra, ODEs/PDEs, numerical methods), 21 helpful, 19 for large problems |
| 19-numerical-modeling-hpc | 01 (numerical methods, PDEs), 03 (NumPy and profiling) |
| 20-signal-processing | 01 (Fourier analysis, complex numbers), 03 |
| 21-statistics-bayesian-ml | 01 (probability and statistics foundations), 03 |
| 22-data-engineering-reproducibility | 03; feeds every data-heavy folder |
| 23-field-methods-instruments | 05; benefits from the relevant domain folder (06, 07, 09, 10) |
| 24-research-papers-writing | Any one domain at working depth; 03 for reproducible practice |
| 25-projects-capstone | 05, 18, 23, 24 and at least one domain at working depth |
| 26-reference-library | None |

Read this table as *sufficient*, not *minimal*. It is quite possible to do a
specific [06-seismology](../../06-seismology/README.md) module on earthquake
location having done only part of 01 and 02. What is never possible is to invert
a seismic dataset defensibly without the inversion foundations from 18, however
much Python you know.

## 4. Valid study orders

A **valid order** is any order in which every folder appears after all of its
prerequisites. There are very many valid orders; the graph constrains sequences,
not schedules. Three observations make planning tractable.

### 4.1 The must-come-first backbone

Exactly one chain is non-negotiable for quantitative work:

```text
01-mathematics  →  02-physics  →  05-core-geophysics  →  domain folder
```

plus `03-scientific-computing` alongside 01/02 if you intend to compute anything.
Everything else is a branch.

### 4.2 Safe parallel pairs

These pairs have no edge between them and share prerequisites, so they can be
studied concurrently without creating a notation debt:

| Pair | Why they work together |
|---|---|
| 01-mathematics + 03-scientific-computing | Same material from two directions: derive by hand, then implement |
| 02-physics + 04-earth-science-geology | Physical laws and Earth setting; each gives the other examples |
| 06-seismology + 20-signal-processing | Methods and the tools used to process their data |
| 07-gravity-geodesy + 17-remote-sensing-gis | Potential fields and the satellite/geodetic observations of them |
| 08-geomagnetism-electromagnetism + 09-electrical-em-methods | Same governing equations; 09 applies what 08 develops |
| 16-atmosphere-climate + 15-oceanography-marine | Coupled system; heat and moisture exchange is the shared physics |
| 21-statistics-bayesian-ml + 18-inverse-problems | Inference, from two directions: statistics and inverse theory |
| 23-field-methods-instruments + any domain folder | Acquisition realism immediately after method theory |

### 4.3 Orders that trap learners

Each of these looks reasonable and fails:

1. **Domain first, foundations never.** Starting at 06 because earthquakes are
   interesting. You will follow two lessons and then hit a partial differential
   equation with no notation for it.
2. **Foundations forever.** Doing all 111 planned mathematics lessons before any
   geophysics. Reasonable-sounding, and it is why people abandon curricula at
   chapter four. Fix: satisfy prerequisites *just in time*.
3. **Inversion before forward modelling.** Inverting data you cannot forward
   model means you cannot test the inversion, and testing is the only way to
   know it works.
4. **Capstone before a domain.** [25-projects-capstone](../../25-projects-capstone/README.md)
   has no content of its own; it composes domains. Project folders require a
   domain at working depth.
5. **Machine learning before statistics.** Statistical inference is what makes an
   ML result interpretable in Earth science, where the data are sparse, noisy and
   spatially correlated.
6. **Deferring writing.** [24-research-papers-writing](../../24-research-papers-writing/README.md)
   is a practice, not a final task. Starting it at doctoral stage costs you the
   years in which you could have been writing.

## 5. Building your own order

The procedure is a topological sort restricted to the folders you need.

**Step 1 — State the goal as a capability.** "Process a seismic reflection line
from an open archive into an interpretable section." Vague goals produce
unbounded plans.

**Step 2 — List the candidate folders.** From the [master map](./01-master-map.md),
this goal suggests 01, 02, 03, 05, 06, 20, 22, and 18 if you will invert.

**Step 3 — Close over prerequisites.** Add what those folders need: 01 and 02
pull in their own earlier mathematics and physics; 06 pulls in elasticity. The
closure is usually smaller than the full curriculum and larger than your first
list.

**Step 4 — Topologically sort.** Order the closure so that no folder precedes its
prerequisites. Where you have freedom, interleave a foundation with an
application in the same study period.

**Step 5 — Assign checkpoints, not folders, as goals.** For each stage of the
order, write the artefact you will produce (see
[Research Milestones](../01-study-roadmap/05-milestones.md)). Artefacts are
testable; folder completion is not.

**Step 6 — Re-plan at each stage transition.** Re-take the
[diagnostic](../01-study-roadmap/03-self-assessment.md); the closure shrinks as
mastery grows.

### Worked example

Goal: *"Locate local earthquakes from a regional network and map the seismicity."*

```text
Closure:      01 (arithmetic, trigonometry, geometry/coordinates,
                  single-variable calculus, linear algebra, probability)
              02 (measurement and physical reasoning, oscillations and waves,
                  elasticity)
              03 (Python, NumPy, plotting, ObsPy and seismic data)
              05 (what geophysics measures, forward modelling principles)
              06 (elastic waves, ray theory and travel times, sources,
                  location and magnitude, statistics and hazard)
              18 (foundations of inverse problems, linear inverse problems)
              21 (statistics in practice) — for uncertainty on locations
              22 (reproducible workflows) — so the result is reproducible

Valid order:  01 → 02 → 03 → 05 → 06 (waves, rays) → 18 → 06 (location)
               with 21 and 22 read alongside once data work begins
```

Note the deliberate interleaving: 06 is entered twice. That is normal and it is
what the graph permits — the second entry has the prerequisites of the first
entry *plus* 18.

## 6. When the graph disagrees with your background

Prior experience can shortcut an edge, but it should be *certified*, not assumed.
The certification is the [diagnostic](../01-study-roadmap/03-self-assessment.md):
if you can retrieve the prerequisite content under closed-book conditions and
produce the artefact, the edge is satisfied for your purposes. If you can only
recognise the content, it is not.

Two rules that keep this honest:

- **Shortcut by evidence, never by familiarity.** "I have used Python" is not
  evidence for a tool prerequisite; "I have written and debugged a script that
  converts units and plots a profile" is.
- **Re-take the diagnostic after a break.** Edges satisified two years ago may
  not be satisfied now, and the failure will appear as an inexplicable difficulty
  with the dependent material.

## Common mistakes

1. **Reading the graph as a straight line.** It is a partial order; most folders
   have several equally valid positions in a plan.
2. **Starting domain work with none of the foundations.** The usual cause of
   abandonment.
3. **Completing a folder instead of satisfying a prerequisite.** The unit of
   progress is the checkpoint artefact.
4. **Missing a tool prerequisite because it is not "academic".** Version control,
   testing and reproducible environments are prerequisites for research-grade
   work, not optional extras.
5. **Ignoring the parallel-safe pairs.** Serialising everything wastes the
   natural pairing of theory with computation.

## Real-world applications

- **Research degree planning.** A PhD timeline is a topological sort of methods
  you must be able to execute before a deadline, and committee reviews check
  exactly this ordering.
- **Team capability planning.** No individual covers the whole graph; teams are
  assembled so that the edges are covered across members.
- **Project estimation.** The closure calculation in section 5 is the same
  reasoning used to estimate what a new project requires before you promise a
  deliverable.

## Further reading

- Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022).
  *Introduction to Algorithms* (4th ed.), chapters on elementary graph
  algorithms. MIT Press. — Topological sort and depth-first search, which is
  literally the procedure in section 5.
- Wiggins, G., & McTighe, J. (2005). *Understanding by Design* (2nd ed.).
  Association for Supervision and Curriculum Development. — On designing a
  sequence backwards from the target capability.
- Lowrie, W., & Fichtner, A. (2020). *Fundamentals of Geophysics* (3rd ed.).
  Cambridge University Press. — Useful for checking which physics a given
  geophysical method actually requires.
  These are bibliographic records; confirm availability through your library or a
  DOI resolver before citing them yourself.

## Related lessons

- [Master Curriculum Map: How the 27 Folders Connect](./01-master-map.md)
- [Domain Tracks: Seismology, Potential Fields, EM, Climate, Near-Surface](./03-domain-tracks.md)
- [Cross-Cutting Skills: Mathematics, Computing, Inverse Theory](./04-cross-cutting.md)
- [Diagnostic Self-Assessment and Placement Quiz](../01-study-roadmap/03-self-assessment.md)
