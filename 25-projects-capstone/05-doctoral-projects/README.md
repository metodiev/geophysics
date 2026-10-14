# Module 05 — Doctoral-Level Projects

Doctoral projects are distinguished from graduate ones not by difficulty but by what
they *attack*: each of these five is built around an inference that is only partially
identifiable, so the project's real deliverable is a statement of what the data can and
cannot settle. The instrumentation is standard; the appraisal is not.

## Lessons

| # | Project | The hard part | Effort |
|---|---------|---------------|--------|
| [01](./01-tomography-project.md) | Local Earthquake Tomography with Resolution Tests | separating data-determined structure from damping-determined structure; the source-location–velocity coupling | 240 min |
| [02](./02-full-waveform-inversion-project.md) | A Small-Scale Full-Waveform Inversion | cycle skipping, the adjoint validated by finite differences, resolution in wavelengths | 240 min |
| [03](./03-geodynamic-model-data.md) | Geodynamic Model-Data Comparison | a model's range of validity; separating model error from noise; quantities that are only determined as products | 240 min |
| [04](./04-bayesian-inversion-project.md) | Trans-Dimensional Bayesian Inversion | the number of parameters as an inferred quantity; validating an MCMC against an exact reference | 260 min |
| [05](./05-reproduce-published-result.md) | Reproducing a Published Geophysical Result | extracting the method from the claim; quantifying the method dependence | 260 min |

Each lesson has a companion pair under [`exercises/`](./exercises): a graded scaffold
of the project's key quantitative step (★ recall, ★★ apply, ★★★ design) and a worked
reference solution whose numbers are cross-checked against the demo's printed output.

## Demos

| Demo | What it prints |
|------|----------------|
| `tomography_demo.py` | ray geometry and coverage, a damping table with the discrepancy principle, amplitude recovery, checkerboard and point-spread resolution tests |
| `full_waveform_inversion_demo.py` | the CFL and resolution limits, an adjoint gradient test against finite differences, three inversions showing one convergence and two cycle skips |
| `geodynamic_model_demo.py` | half-space and plate-model fits to synthetic depth and heat flow, $\chi^2/\text{dof}$, systematic residuals, and the parameter products each observable determines |
| `transdimensional_demo.py` | an exact enumerated posterior over the layer count, three reversible-jump chains with acceptance rates, and the sampler's demonstrated bias |
| `reproduce_result_demo.py` | four estimation routes to a published aftershock exponent, with uncertainties, correlations and the method-dependence spread |

All demos are print-only, seeded with `np.random.default_rng(20261014)`, labelled
**SYNTHETIC**, use no network, write no files, exit 0, and run in a few seconds each.

## The pattern these five projects share

1. **Formulate the inference with its assumptions explicit.** Every one of these
   projects states the assumed quantity that would ruin the result if it were wrong —
   the background velocity, the source wavelet, the thermal expansivity, the prior on
   the number of parameters, the estimator.
2. **Quantify what the data determine.** A resolution length, a half-maximum region, a
   wavelength limit, an acceptance rate, a method-dependence spread. Numbers, not
   adjectives.
3. **Separate what the data determined from what the method determined.** The damping,
   the starting model, the prior, the estimator. This is the doctoral skill.
4. **Validate against something with a known answer** before applying the machinery to
   the unknown — a synthetic model, an analytic solution, an exact enumeration.

## How to study this module

1. Read the project's question and the *honest summary* section first, then work
   forwards. Knowing what the project concludes prevents the common failure of
   producing a plot and calling it a result.
2. Run the demo and record its printed numbers; the exercises are graded against them.
3. Do the ★ and ★★ exercises with the demo closed.
4. Write the ★★★ item as a one-page memo. In every case it asks you to remove the
   project's central assumption.
5. Attempt the project on real data only after the synthetic version reproduces the
   printed numbers.

## Where this leads

These projects are the technical preparation for the capstone of
[Module 06](../06-capstone-research/README.md). Each is deliberately laid out in the
form a capstone proposal needs — a question, a dataset, a method with its assumptions
stated, a deliverable and a definition of success — and each ends with the appraisal
material that belongs in a capstone's uncertainty section.

## Prerequisites

The numerical and inference background of
[18 Inverse Problems](../../18-inverse-problems/README.md) and
[21 Statistics, Bayesian Inference and Machine Learning](../../21-statistics-bayesian-ml/README.md),
plus the method modules linked from each lesson. Python environment:
`/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python` (numpy, scipy,
matplotlib, pandas, scikit-learn).
