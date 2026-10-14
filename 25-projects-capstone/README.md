# 25 — Projects and Capstone

**Stages:** beginner → research

This folder is where the curriculum stops teaching methods and starts asking for
results. Every lesson here is a **project specification**: a question, a named dataset,
a sequence of steps, a deliverable, a success criterion, a set of failure modes and a
rubric. The 31 projects run from a first plot of a seismogram to a defended capstone, and
the difficulty that increases across them is not the mathematics — it is the *appraisal*.
A beginner project succeeds when the code runs and the output is right; a doctoral
project succeeds when the author can say which parts of the answer the data determined,
which parts the method determined, and which parts remain unknown.

That thread is worth stating once, plainly, because it organises the whole folder:
**a project is not finished when it produces a number; it is finished when it produces
the number together with the statement of what the number depends on.** The projects
below are built so that the dependence is measurable rather than rhetorical. Where a
result is dominated by an assumed background velocity, the project measures the
dependence. Where the resolution is limited by wavelength, the project reports the
wavelength. Where the number of parameters is itself unknown, the project infers it and
then validates the inference against a case with a known answer. A reader who finishes
this folder should be able to look at any published geophysical estimate and say which
of its terms are data, which are assumptions, and how much of the quoted uncertainty the
assumptions account for.

Three distinctions recur often enough to state once:

- **Deliverable versus method.** Each project names the artefact it will produce — a
  map, a model, a coefficient, a resolution length, a release — and the practical
  criterion by which a reader can tell whether it was produced. "A velocity model" is
  not a deliverable; "a velocity model with a resolution length stated per depth" is.
- **Resolution versus accuracy versus detection.** A feature can be detected long
  before it can be resolved, and resolved long before its amplitude is accurate. The
  projects measure all three separately: the H-K half-maximum region, the tomography
  point-spread function, the full-waveform half-period criterion, the power calculation
  of the capstone design.
- **Statistics versus systematics, and what more work buys.** Every project's
  uncertainty has a statistical term that shrinks with data and a systematic term that
  does not. Reporting the split is what turns an error bar into a plan; the capstone
  lessons make the arithmetic explicit (a systematic term at $64\%$ of the variance caps
  the benefit of halving the measurement error at $15\%$).

None of the demos in this folder require data downloads: each lesson's executable
companion is **print-only and SYNTHETIC**, seeded with `np.random.default_rng(20261014)`,
and prints the exact numbers that appear in the lesson text and in the exercise
solutions. Where a lesson names a real archive, it cites only a URL already registered in
`tools/verified_links.tsv`, and the project's steps are unchanged when the synthetic data
are replaced by the real download.

## Learning objectives for the folder

By the end of this folder you will be able to:

1. **Specify** a project: question, data (with its count and noise), method, deliverable,
   success criterion, failure modes and rubric.
2. **Compute** the constraint that decides whether the project is answerable — a
   signal-to-noise ratio, a minimum detectable effect, a resolution length, a
   travelling-wave wavelength, a half-maximum region.
3. **Verify** a method against a case with a known answer before applying it to an
   unknown one, and report the verification as a result.
4. **Separate** what the data determined from what the method or the prior determined,
   and quantify the second.
5. **Report** uncertainty in the form the evidence supports: a budget with its split, a
   resolution statement per depth, or a posterior over a model space.
6. **Reproduce** someone else's published number, and quantify the method dependence
   rather than declaring agreement or disagreement.
7. **Plan and defend** a study: a schedule with a critical path, a provenance log, an
   audited manuscript, a reproducible release and a question-impact analysis.

## Modules

| # | Module | Stage | Projects | What it develops |
|---|--------|-------|----------|------------------|
| 01 | [Beginner Projects](./01-beginner-projects/README.md) | beginner | 4 | units, plotting, a first map, a first inversion, reading a seismogram |
| 02 | [Intermediate Projects](./02-intermediate-projects/README.md) | intermediate | 5 | travel-time curves, a gravity model, Fourier analysis, refraction interpretation, a quantitative porosity estimate |
| 03 | [Advanced Projects](./03-advanced-projects/README.md) | advanced | 6 | magnetic modelling, ERT inversion, a seismic processing flow, climate data, GNSS strain, inversion with uncertainty |
| 04 | [Graduate Projects](./04-graduate-projects/README.md) | graduate | 6 | finite-difference wave propagation, MT inversion, InSAR time series, catalogue statistics, joint inversion, receiver functions |
| 05 | [Doctoral Projects](./05-doctoral-projects/README.md) | doctoral | 5 | tomography with resolution tests, full-waveform inversion, geodynamic model–data comparison, trans-dimensional Bayes, reproducing a published result |
| 06 | [Capstone Research](./06-capstone-research/README.md) | research | 5 | design, proposal, execution, write-up and release, defence and peer critique |

Each lesson has three companions: `exercises/<stem>-exercises.md` (a graded scaffold of
the project's key quantitative step), `exercises/<stem>-solutions.md` (the worked
reference solution) and `code/<slug>_demo.py` (a small, self-contained implementation of
one piece of the project that prints the expected artefact).

## How to study this folder

1. **Choose by stage, not by subject.** The module list above is a ladder; the projects
   in module 01 assume only that you can load a file and make a plot, and the projects in
   module 05 assume the inference material of folders 18 and 21.
2. **Read the question section and the honest summary first.** Knowing what a project
   concludes prevents the most common failure of a project — producing a figure and
   calling it a result.
3. **Run the demo before reading the method.** Its printed numbers are the reference
   values the exercises are graded against, and the first exercise in each lesson is
   usually to reproduce one of them by hand.
4. **Do the ★★★ item with your own project.** In every lesson it asks you to remove the
   project's central assumption, which is the step from executing a method to doing a
   study.
5. **Keep the artefacts.** Reports, registries, schedules and audits produced for one
   project are the templates for the next; the capstone of module 06 is an assembly of
   them.

## Where this folder sits in the curriculum

The projects draw on the subject modules throughout the repository — seismology (06),
potential fields (08), electrical methods (09), geodynamics (13), inverse problems (18),
signal processing (20), statistics and machine learning (21) and data engineering (22) —
and they are the place where those subjects have to produce a number that someone else
can check. Module 06 is the terminal module of the project track: the capstone it
describes is a real research study, and the standard it applies is the one used in
professional practice.

## Conventions

- Every demo is runnable with the repository environment:
  `/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python <demo>.py`.
- Demos print only — no files, no plots, no network — so that a lesson's numbers are
  reproducible by anyone with the repository.
- Numbers quoted in lesson prose, in the exercises and in the solutions are the demo's
  printed output. Where a value is derived rather than printed, the derivation is shown.
- Synthetic data are labelled **SYNTHETIC** in every lesson and in every demo's output.
