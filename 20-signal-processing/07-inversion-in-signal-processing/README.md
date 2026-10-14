# Module 20-07 — Inverse Methods in Signal Processing

**Stages:** research · **Prerequisites:** modules 20-04 and 20-01; the language of
inverse problems from folder 18.

This module is about the point where signal processing stops being linear
algebra and becomes a statement about what the signal *is*. Every lesson here
takes the same convolutional or sampling operator and adds a prior — that
reflectivity is sparse, that a spectrum has few lines, that a trace is generated
by a small family of wavelets — and then measures what the prior buys and what it
costs. The costs are always the same three: a shrinkage bias, a dependence on a
dictionary or basis that was chosen rather than measured, and resolution claims
that hold only while the prior is true.

The second theme is that **sparsity is a model, not a property of data**. A
demonstration in this module will happily return a sparse answer from a signal
that is not sparse, because the penalty says so. Each lesson therefore pairs its
positive result with a control experiment: a matrix that cannot recover what it
should, a generator whose dictionary is absent, a ramp that a step detector
describes as four steps. The mastery checkpoints ask for the assumption, not the
algorithm.

All models and data in this module are **SYNTHETIC**. No real trace, survey,
dataset or published number is used.

## Learning objectives

By the end of this module you will be able to:

1. **Formulate** deconvolution and sparse reconstruction as penalised inverse
   problems, and **state** the norm, the operator and the noise model.
2. **Derive** and **verify** the proximal operator of the L1 norm, and
   **implement** ISTA and FISTA with a correct step size.
3. **Check** first-order optimality of a sparse solution, including the
   subgradient condition at the exactly-zero entries.
4. **Measure** the residual–sparsity–shrinkage trade-off and **choose** a penalty
   against a stated requirement.
5. **Compute** the coherence of a sensing matrix and **use** it to predict
   whether a given undersampling scheme can succeed.
6. **Measure** a phase transition in the number of samples and **report** it with
   its empirical uncertainty rather than as a scaling law with a borrowed
   constant.
7. **Distinguish** a sparse representation claim from a sparse inversion claim,
   and **test** each under the conditions it requires.
8. **Design** a held-out evaluation of a dictionary choice, and **state** why
   in-sample evaluation measures the experimenter.

## Prerequisites

- [20-04-01 Deconvolution: Concept, Ill-Posedness and Stabilisation](../04-deconvolution-and-inverse-filtering/01-deconvolution-concept.md)
  — the convolutional model and the classical stabilisers.
- [20-01-03 Convolution, Correlation and Filtering](../01-signals-and-systems/03-convolution-and-filters.md)
  — the discrete convolution matrix, its adjoint and its conditioning.
- [20-01-05 Sampling, Nyquist and Reconstruction](../01-signals-and-systems/05-sampling-theory.md)
  — aliasing, which §3 of lesson 02 turns into a null-space measurement.
- [18-02-02 Underdetermined Problems](../../18-inverse-problems/02-linear-inverse-problems/02-underdetermined.md)
  — what a null space forces you to choose, and how a norm makes the choice.
- [18-03-04 Sparsity](../../18-inverse-problems/03-regularization/04-sparsity.md)
  — the general theory this module applies to signals.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Sparse and L1 Deconvolution](01-sparse-deconvolution.md) | research | L1 restores a spike train and shrinks every amplitude; the shrinkage is a bias, not scatter |
| 02 | [Compressive Sensing and Data Reconstruction](02-compressive-sensing-signals.md) | research | Uniform subsampling admits an alias set that fits exactly; the phase transition is measured, not quoted |
| 03 | [Sparse Representations for Seismic Data](03-sparsity-seismic.md) | research | The dictionary that approximates best is the one that recovers worst, and the winner depends on the generator |

## Suggested path

**If you are new to sparse methods:** lesson 01 in full, running the
demonstration and checking the penalty table against the resolution table.
Lesson 02 §1–§3 then gives the sampling side; §4–§5 can wait.

**If you come from inverse theory:** read 01 §2–§3 (the proximal step and FISTA),
then 02 §2–§3 (coherence and the null space) and 03 §3 (why redundancy costs
coherence). The unfamiliar content will be the measurement practice, not the
theory.

**If you are preparing a research project:** 01 §4–§7 (the trade-off and the
assumptions), 02 §5–§6 (restricted eigenvalues and the validity limits) and
03 §5.1 (held-out dictionary selection), plus the ★★★ exercises of every lesson.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-sparse-deconvolution.md`](01-sparse-deconvolution.md) | Lesson 01 |
| [`02-compressive-sensing-signals.md`](02-compressive-sensing-signals.md) | Lesson 02 |
| [`03-sparsity-seismic.md`](03-sparsity-seismic.md) | Lesson 03 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Three runnable demonstrations |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib and
ObsPy:

```bash
cd 20-signal-processing/07-inversion-in-signal-processing/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python sparse_deconvolution_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python compressive_sensing_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python sparse_representations_demo.py
```

Every demo prints labelled results with units, uses a fixed random seed
(`np.random.default_rng(20261014)`), needs no network access and exits 0.

## Mastery checkpoint

Complete this without notes:

> A 400-sample trace at 4 ms is generated by 12 spikes convolved with a 30 Hz
> Ricker wavelet, plus noise at 5 % of the signal rms. **(a)** State the L1
> objective and the closed form of its proximal operator. **(b)** From the
> measured table, choose a penalty that keeps the residual below 12 % and the
> amplitude bias above 0.85, and say what the choice costs in resolution.
> **(c)** Explain why the same data give 19 nonzero samples under L1 and 351
> samples above $10^{-3}$ under L2 at matched residual. **(d)** State the
> subgradient condition at a zero entry and what it means. **(e)** You are asked
> to recover this trace from 40 randomly chosen samples. State which of the three
> failures measured in lesson 02 you would check first, and with which number.

A worked version of (a)–(d) appears in the lesson-01
[solutions](exercises/01-sparse-deconvolution-solutions.md).

## Common pitfalls across this module

1. **Reporting shrunk amplitudes as amplitudes.** The L1 solution is biased
   downward by an amount that grows with the penalty.
2. **Comparing estimators at different residuals.** Match the fit or the
   comparison is about the fit.
3. **Quoting a recovery threshold without its constant.** $m \sim
   k\log(n/k)$ hides a constant that depends on the dictionary and the design.
4. **Reading the largest peak as the answer.** Uniform subsampling admits a whole
   alias set; the ambiguity, not the winner, is the result.
5. **Assuming a redundant dictionary is better.** It approximates better and
   recovers worse, by the same coherence.
6. **Scoring a dictionary on the data it was built from.** The in-sample table is
   a positive control, not a result.

## Related modules

- [20-04 Deconvolution and Inverse Filtering](../04-deconvolution-and-inverse-filtering/README.md)
  — the L2 branch and the classical estimators these lessons generalise.
- [20-05 Noise and Random Signals](../05-noise-and-random-signals/README.md) —
  the noise models that make "the residual" a meaningful statement.
- [18-03 Regularisation](../../18-inverse-problems/03-regularization/README.md) —
  sparsity, total variation and parameter choice in full generality.
- [21-04 Machine Learning Fundamentals](../../21-statistics-bayesian-ml/04-machine-learning-fundamentals/README.md)
  — dictionaries learned from data, and the same bias–variance accounting.
