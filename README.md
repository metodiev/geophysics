# Geophysics: From Beginner to Independent Researcher

A self-contained, dependency-checked geophysics curriculum. It runs from
school-level arithmetic to doctoral and research-professional practice across
27 thematic folders, and it is designed to be **studied in order, verified by
running code, and extended by writing new lessons**.

The guiding principle is that you should finish able to do four things
independently:

1. **Read** a research paper in geophysics and judge whether its methods,
   data, and uncertainty treatment actually support its conclusions.
2. **Process** real geophysical data from a credible open archive into a
   defensible result.
3. **Model** a physical process numerically, and know how to prove the
   numerical result is correct.
4. **Quantify** and communicate uncertainty without overclaiming.

---

## Start here

| If you want to... | Go to |
|---|---|
| Understand what this repository is and how it is organised | [00-orientation](./00-orientation/README.md) |
| See the full contents and current progress | [CURRICULUM.md](./CURRICULUM.md) |
| Know which topics depend on which, and in what order to study | [curriculum map](./00-orientation/02-curriculum-map/README.md) |
| Set up your Python environment | [environment setup](./00-orientation/03-how-to-use-this-repo/02-environment-setup.md) |
| Know what geophysics actually is | [what is geophysics](./00-orientation/04-orientation-geophysics/01-what-is-geophysics.md) |
| Look up a symbol, unit, formula, textbook, or dataset | [reference library](./26-reference-library/README.md) |

---

## Repository layout

The 27 numbered folders follow a deliberate progression: **foundations**
(01–03), **Earth context** (04–05), **domain methods** (06–17), **shared
mathematics of inference and computation** (18–22), and **practice,
communication, and integration** (23–26).

```
00-orientation                       How to study, prerequisites, progress tracking
01-mathematics                       Arithmetic to functional analysis; the language of the subject
02-physics                           Mechanics, waves, elasticity, thermo, fluids, EM, potential theory
03-scientific-computing              Python, NumPy/SciPy/pandas, ObsPy, PyGMT, testing, packaging
04-earth-science-geology             Earth structure, plate tectonics, stratigraphy, hazards
05-core-geophysics                   Property contrasts, forward modelling, rock physics, survey design
06-seismology                        Elastic waves, ray theory, sources, tomography, reflection, hazard
07-gravity-geodesy                   Gravity, the geoid, GNSS, satellite gravimetry, Earth tides
08-geomagnetism-electromagnetism     The geomagnetic field, induction, magnetotellurics
09-electrical-em-methods             Resistivity, IP, self-potential, controlled-source EM
10-gpr-near-surface                  Ground-penetrating radar and shallow-subsurface methods
11-exploration-geophysics            Mineral, hydrocarbon, geothermal, groundwater, geotechnical
12-global-geophysics-interior        Reference Earth models, mineral physics, core, normal modes
13-geodynamics-tectonics             Rheology, mantle convection, plate kinematics, modelling
14-hydrology-hydrogeophysics         Aquifers, contaminant transport, hydrogeophysical monitoring
15-oceanography-marine               Physical oceanography and marine geophysical methods
16-atmosphere-climate                Atmospheric physics, radiation, climate models, attribution
17-remote-sensing-gis                Optical/thermal/radar sensing, InSAR, GIS, geospatial analysis
18-inverse-problems                  Ill-posedness, regularisation, Bayesian inference, UQ
19-numerical-modeling-hpc            FD/FE/spectral methods, verification, parallel computing
20-signal-processing                 LTI systems, filtering, spectral analysis, deconvolution
21-statistics-bayesian-ml            Statistics, geostatistics, Bayesian inference, machine learning
22-data-engineering-reproducibility  Formats, pipelines, containers, open science
23-field-methods-instruments         Fieldwork, instrumentation, laboratory measurement
24-research-papers-writing           Reading, writing, presenting, ethics, publication
25-projects-capstone                 Staged projects and an original capstone study
26-reference-library                 Glossary, symbols, units, formulas, textbooks, datasets
```

---

## Setup

### Nothing to install, to validate the repository

The repository's quality gate uses the **Python standard library only**:

```bash
python3 tools/check_all.py       # structure, links, formulas, duplicates
python3 tools/build_index.py     # regenerate CURRICULUM.md
python3 tools/verify_links.py    # confirm cited URLs are verified
```

This works on a bare Python 3.9+ installation.

### Installing the scientific stack

Lesson code needs NumPy, SciPy, ObsPy, and friends. Use an isolated
environment:

```bash
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

`requirements.txt` is organised by tier so you can install only what a given
track needs. For a fully pinned, interpreter-inclusive setup prefer conda:

```bash
conda env create -f environment.yml
conda activate geophysics
```

See [environment setup](./00-orientation/03-how-to-use-this-repo/02-environment-setup.md)
for troubleshooting, including what to do when a wheel is unavailable for a
very new Python version.

---

## How content is organised

Every **folder** has a `README.md` index. Every **module** is a folder with its
own `README.md` stating learning objectives, prerequisites, and a mastery
checkpoint. Every **lesson** is a numbered Markdown file.

```text
01-mathematics/
└── 01-arithmetic/
    ├── README.md                                 module index, objectives, checkpoint
    ├── 01-number-systems-and-precision.md        lesson
    ├── 02-orders-of-magnitude.md
    ├── exercises/
    │   ├── 01-number-systems-and-precision-exercises.md
    │   └── 01-number-systems-and-precision-solutions.md
    └── code/
        └── number_systems_demo.py
```

Lessons share a common anatomy, enforced by `tools/check_all.py`:

> learning objectives · prerequisites · intuition · precise definitions ·
> equations in LaTeX · step-by-step derivations · physical interpretation ·
> assumptions and validity · units and dimensional analysis · worked examples ·
> Python demonstration · graded exercises (★/★★/★★★) · solutions ·
> common mistakes · real-world applications · further reading · related lessons

The rationale for this structure, and the conventions in detail, are in
[how to use this repository](./00-orientation/03-how-to-use-this-repo/README.md)
and the [lesson template](./00-orientation/03-how-to-use-this-repo/04-contribution-workflow.md).

---

## Honesty about data and uncertainty

This repository is built to a strict evidence standard, because a curriculum
that quietly invents datasets teaches exactly the wrong habit:

- **Every external link is verified** before it is cited, with the observed
  HTTP status recorded in [`tools/verified_links.tsv`](./tools/verified_links.tsv).
  `tools/verify_links.py` fails the build if a cited URL is not in that record.
  Links that returned `404` or were unreachable are listed there as
  **rejected, do not cite**.
- **Datasets are labelled** `SYNTHETIC` (generated, reproducible offline),
  `OBSERVED` (real, from an institutional archive with a verified URL), or
  `ILLUSTRATIVE` (hand-constructed teaching numbers).
- **No fabricated citations, findings, or datasets.** Where a fact or URL
  could not be verified, the text says so explicitly instead of guessing.
- **Uncertainty is reported, not hidden.** Lessons that produce a number also
  ask what its error bar is and what assumptions that error bar rests on.

---

## Progress tracking

[`CURRICULUM.md`](./CURRICULUM.md) is generated and reports real coverage:
which lessons exist on disk, per module and per folder. Regenerate it after
adding content. The full implementation plan and batch schedule live in
[`tools/curriculum_plan.py`](./tools/curriculum_plan.py) and
[the study roadmap](./00-orientation/01-study-roadmap/README.md).

```bash
python3 tools/build_index.py     # refresh coverage
python3 tools/check_all.py       # confirm nothing is broken
```

---

## Contributing to the curriculum

1. Add the lesson to [`tools/curriculum_plan.py`](./tools/curriculum_plan.py)
   (id, slug, title, level).
2. Copy the lesson anatomy from
   [`01-mathematics/01-arithmetic/01-number-systems-and-precision.md`](./01-mathematics/01-arithmetic/01-number-systems-and-precision.md),
   which is the reference exemplar.
3. Run `python3 tools/check_all.py` and fix anything it reports.
4. Run `python3 tools/build_index.py` to refresh coverage.

---

## Licensing and attribution

Code in this repository is provided for teaching and research use. **Data,
figures, and text from external sources remain subject to their own licences**;
each dataset lesson states its source and the terms under which it may be
reused. When you publish work derived from these archives, cite the original
data provider as well as the archive.

