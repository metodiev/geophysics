# Module 09-07 — EM Data Processing, QC and Uncertainty

**Stages:** graduate → research · **Prerequisites:** modules 09-02 and 09-05;
basic statistics and linear algebra.

This module is about the gap between a measurement and a number that can be
quoted. It is built around one honest difficulty: **the error that matters most is
usually the one that does not average down.** Stacking $N$ repeats reduces
incoherent noise as $\sqrt{N}$ — and does nothing whatever to a powerline line
whose phase is locked to the acquisition clock, which is why a 256-repeat stack in
the demonstration still carries the same 22.5 $\Omega\,\mathrm{m}$ error it started
with. Despiking removes six spikes on a synthetic transient and flags 156 clean
samples while doing it. A drift fit in the wrong window removes part of the signal
and changes the fitted decay exponent by 20%. Every one of those statements is a
*measurement* from a synthetic record whose truth is known, and every one of them
is invisible in a plot of the result.

The module's discipline is therefore to make each step's cost explicit. Lesson 01
classifies the error terms and measures what stacking, robust estimators and
reference channels can and cannot fix. Lesson 02 walks the processing chain step
by step and measures, for each step, the noise it removes and the bias it
introduces on an ideal record. Lesson 03 assembles the survivors into an
uncertainty budget: a covariance matrix whose coverage has been *measured* against
Monte Carlo, a systematic term that no interval can see, and an admissible set that
shows how much of a reported number is the prior rather than the data.

All models and data in this module are **SYNTHETIC**. The two-layer earth is an
exact teaching model; the decay shape, spike population, drift amplitude, gain
error and parameter bounds are chosen values, and no instrument, site or published
figure is referenced.

## Learning objectives

By the end of this module you will be able to:

1. Classify measurement error into incoherent noise, coherent noise and
   systematic error, and predict which terms stacking can reduce.
2. Propagate a potential measurement error into apparent resistivity through the
   geometric factor, and predict its spacing dependence.
3. Measure the $\sqrt{N}$ law for incoherent noise and demonstrate the failure of
   the same law for a phase-locked coherent line.
4. Choose between mean, median and trimmed-mean stacking from measured rms errors
   at a stated contamination rate, and state the claim that choice encodes.
5. Recognise exact degeneracy between a coherent line and a DC level, and design
   an acquisition (rather than a filter) that removes it.
6. Design a despiking rule whose detection scale follows the local noise, and
   measure its true-hit and false-positive rates separately.
7. Derive the bias of a low-pass filter from the curvature of the decay, and
   choose the filter length against a stated gate-accuracy requirement.
8. Write a reproducible processing log that records rejected parameters and the
   measurement that motivated each rejection.
9. Compute a linearised parameter covariance, interpret its correlation matrix,
   and measure its coverage by Monte Carlo.
10. Quantify a systematic error in units of the nominal standard error, and
    explain why better data make it more significant.
11. Report an admissible set instead of an optimum, and state the prior that a
    bounded search imposes.

## Prerequisites

- [09-02 DC Resistivity Methods](../02-dc-resistivity/README.md) — geometric
  factors, apparent resistivity and two-layer forward modelling.
- [09-05 Applied Electromagnetic Methods](../05-em-methods-applications/README.md) —
  the soundings whose late-time windows dominate the noise budget.
- [05-06 Data Processing Principles](../../05-core-geophysics/06-data-processing-principles/README.md) —
  filtering, stacking and estimation vocabulary.
- [21-statistics-bayesian-ml](../../21-statistics-bayesian-ml/README.md) —
  covariance, bootstrap and coverage as general tools.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [EM Noise, Coupling and Cultural Effects](01-em-noise-and-coupling.md) | graduate | Coherent noise does not average down; a locked line is exactly degenerate with the DC level |
| 02 | [EM Processing Workflow and Data Editing](02-em-processing-workflow.md) | graduate | Every processing step is a biased estimator; measure the bias, not just the noise removed |
| 03 | [Quantifying Uncertainty in EM Interpretation](03-em-uncertainty.md) | research | A covariance is a lower bound; measure its coverage, then add the terms it cannot see |

## Suggested path

**If you are new to EM processing:** read 01, then 02, running each demonstration.
Lesson 02's §7 (the fitted exponent) is the single most useful quality-control
idea in the module, and it costs one synthetic run.

**If you already process data:** read 01 §5 (the design-matrix degeneracy) and
then all of 03. The first is a trap that arithmetic cannot escape; the second is
what a defensible published interval looks like.

**If you are preparing a research project:** read 03 §4–7 (coverage, systematic
error, the admissible set) and the ★★★ exercises. Together they are the recipe for
an uncertainty section that survives review.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-em-noise-and-coupling.md`](01-em-noise-and-coupling.md) | Lesson 01 |
| [`02-em-processing-workflow.md`](02-em-processing-workflow.md) | Lesson 02 |
| [`03-em-uncertainty.md`](03-em-uncertainty.md) | Lesson 03 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Three runnable demonstrations |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib and
SymPy:

```bash
cd 09-electrical-em-methods/07-em-data-processing-and-qc/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python em_noise_and_coupling_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python em_processing_workflow_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python em_uncertainty_demo.py
```

Every demo prints labelled results with units, uses a fixed random seed
(`np.random.default_rng(20261014)`), needs no network access, and exits 0. The
three together run in about fifteen seconds, the noise demonstration
being the slowest at roughly eleven.

## Mastery checkpoint

Complete this without notes.

> A Wenner sounding uses spacings 1 to 64 m with a $2\%$ relative error per datum,
> and a $50\ \mathrm{Hz}$ line is present.
> **(a)** State how the error in apparent resistivity scales with spacing and why.
> **(b)** You have 64 repeats. State the error reduction you can expect for
> incoherent noise, and the reduction you will get for a line whose phase is
> identical in every repeat. Then state the phase advance per repeat that would
> reduce the line by a factor of 50.
> **(c)** A despiker flags 40 samples of a 1024-sample record. State two numbers you
> need before deciding whether to accept the edit, and what each measures.
> **(d)** The sounding is inverted for $(\rho_1, \rho_2, H)$ and the covariance
> gives $\sigma_H = 0.26$ m with $\mathrm{corr}(\rho_2,H) = +0.69$. A gain error of
> $3\%$ is later found. State which parameter it biases, by roughly how many
> $\sigma$, and whether the residual reveals it.
> **(e)** A sounding whose longest spacing is 20 m admits $\rho_2$ between 187 and
> $1500\ \Omega\,\mathrm{m}$. Write the one sentence you would publish.

A worked version of (b) appears in the lesson-01
[solutions](exercises/01-em-noise-and-coupling-solutions.md), and a worked version
of (d) and (e) appears in the lesson-03
[solutions](exercises/03-em-uncertainty-solutions.md).

## Common pitfalls across this module

1. **Reporting the noise removed and not the bias introduced.** Both are numbers,
   and the bias is the one that survives into the interpretation.
2. **Averaging a coherent line.** It has a phase; check it before stacking.
3. **Trusting the standard error of the mean.** It measures precision under
   assumptions that data often violate.
4. **Choosing a filter or a drift window by eye.** Choose against the fastest
   timescale and a measured gate error.
5. **Quoting a covariance as "the uncertainty".** It is the noise term only; the
   systematic and model terms are usually larger.
6. **Reporting an optimum without the admissible set.** The optimum is one member
   of a ridge, and the ridge is the result.

## Related modules

- [09-06 Borehole Electrical and EM Methods](../06-borehole-electrical/README.md) —
  the borehole counterpart, with its own resolution limits and error budget.
- [09-02 DC Resistivity Methods](../02-dc-resistivity/README.md) and
  [09-05 Applied Electromagnetic Methods](../05-em-methods-applications/README.md) —
  the measurements whose processing and uncertainty this module quantifies.
- [18-inverse-problems](../../18-inverse-problems/README.md) — resolution, null
  space and regularisation bias in general.
- [21-statistics-bayesian-ml](../../21-statistics-bayesian-ml/README.md) —
  bootstrap, coverage and posterior sampling.
- [22-data-engineering-reproducibility](../../22-data-engineering-reproducibility/README.md) —
  provenance and processing logs.
