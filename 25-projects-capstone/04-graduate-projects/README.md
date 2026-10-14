# Module 04 — Graduate Projects

Project specifications at graduate level: each one is a small research study with a
stated question, a named dataset, a sequence of steps, a deliverable, a success
criterion and a rubric. The common thread is that the *inference* is the hard part —
each project ends by asking how much of the answer is the data and how much is the
assumption.

## Lessons

| # | Project | Method core | Estimate of effort |
|---|---------|-------------|--------------------|
| [01](./01-fd-wave-propagation-project.md) | Finite-Difference Wave Propagation | explicit staggered-grid FD, CFL, numerical dispersion, convergence order | 200 min |
| [02](./02-mt-1d-2d-inversion.md) | 1-D and 2-D MT Inversion | magnetotelluric impedances, layered forward model, regularisation, model appraisal | 200 min |
| [03](./03-insar-deformation-project.md) | InSAR Deformation Time Series | phase-to-displacement, unwrapping, atmospheric screening, linear/slip inversion | 200 min |
| [04](./04-earthquake-catalog-analysis.md) | Earthquake Catalogue Analysis | completeness $M_c$, $b$-value, declustering, rate and hazard estimates | 200 min |
| [05](./05-joint-inversion-project.md) | Joint Inversion of Two Datasets | multi-kernel objective, relative weighting, resolution trade-off | 200 min |
| [06](./06-receiver-function-project.md) | Crustal Structure from Receiver Functions | H-K stacking, $H$–$V_p/V_s$ trade-off, resolution region | 200 min |

Each lesson has a companion pair under [`exercises/`](./exercises):

- `NN-<slug>-exercises.md` — a graded scaffold of the project's key quantitative
  step (★ recall/derive, ★★ apply/compute, ★★★ design/research).
- `NN-<slug>-solutions.md` — the worked reference solution, with every number
  cross-checked against the demo's printed output.

Each lesson has a runnable companion under [`code/`](./code):

| Demo | What it prints |
|------|----------------|
| `fd_wave_demo.py` | a 1-D FD solution against the analytic solution and the observed convergence order |
| `mt_inversion_demo.py` | apparent resistivity/phase for a layered model and the recovered layered structure |
| `insar_timeseries_demo.py` | the deformation time series, the secular rate and the residual scatter |
| `catalogue_hazard_demo.py` | the magnitude–frequency curve, $M_c$, $b$-value and the declustered rate |
| `joint_inversion_demo.py` | the two single-dataset inversions and the joint one, with their resolutions |
| `receiver_function_demo.py` | the three Moho phase times, the H-K peak and the single-phase trade-off |

All demos are print-only, seeded with `np.random.default_rng(20261014)`, labelled
**SYNTHETIC**, use no network, write no files, and exit 0.

## Data policy

Where a lesson names a real archive it cites only a URL registered in
`tools/verified_links.tsv` (IRIS/EarthScope FDSN, USGS, Copernicus/ASF, GFZ GEOFON,
…). Where no such URL exists the project is built on **SYNTHETIC** data generated
in the demo, and the lesson says so explicitly. The synthetic routes are designed to
be replaced by real data downloads without changing any of the analysis steps.

## How to study this module

1. Read a lesson's question and data sections, and decide what the answer *should*
   look like before reading the method.
2. Run the demo. Write down its printed numbers — those are the reference values
   the exercises are graded against.
3. Do the ★ and ★★ exercises with the demo closed. Then reread the solutions.
4. Do the ★★★ exercise as a design memo (one page, no code). It asks what would
   have to be added to remove the project's central assumption.
5. Only then attempt the project on real or larger synthetic data, and keep the
   deliverable, success criterion and rubric in front of you as the checklist.

## Prerequisites

These projects assume the numerical and inference background of
[18 Inverse Problems](../../18-inverse-problems/README.md) and
[20 Signal Processing](../../20-signal-processing/README.md), and the geophysics
background of the relevant method modules linked from each lesson. The Python
toolchain is the repository virtual environment
(`/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python`, numpy, scipy,
matplotlib, pandas, scikit-learn).

## Where this leads

These projects are the direct preparation for
[06 Capstone Research](../06-capstone-research/README.md): each one already contains
the four elements a capstone proposal needs — a question, a dataset, a method with
stated assumptions, and a definition of success. A capstone is one of these,
executed at full scale and defended. Candidates that combine two of these projects
into one study (e.g. 03 + 05, or 02 + 06) are also listed as starting points in
[25-06-01](../06-capstone-research/01-capstone-design.md).
