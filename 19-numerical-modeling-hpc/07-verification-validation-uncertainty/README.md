# Module 19-07 — Verification, Validation and Numerical Uncertainty

**Stages:** research · **Prerequisites:** modules
[19-01](../01-numerical-foundations/README.md),
[19-02](../02-finite-difference-methods/README.md); the idea of a discretisation
error; some experience of running a simulation code.

This is the module that makes the difference between *computing* and *claiming*.
Every later simulation in this folder, and every simulation you write yourself,
produces numbers; this module is the discipline that decides which of those numbers
may be believed and to what precision. It is built around one honest difficulty:
**a simulation is a scientific claim only if it has been verified against an exact
solution and validated against an independent model, and numerical error is not
uncertainty.** A converged solution to the wrong equations is still wrong, and no
amount of refinement will reveal it.

The module separates the three activities by their reference. *Code verification*
compares the code with an exact solution of the same equations, and the evidence is
the *rate* at which the error falls — the order of accuracy. *Solution
verification* compares solutions on different grids with each other and produces a
discretisation error estimate for the functional you actually report. *Validation*
compares the model with data it did not generate, and it is a prediction test, not
a fit. Each lesson states which of the three it is doing, and what the other two
would have to add.

All models and data in this module are **SYNTHETIC**. Every problem is defined here,
its exact solution is derived here, and every number is printed by a demonstration
you can run. No figure is quoted from a published benchmark or a measurement.

## Learning objectives

By the end of this module you will be able to:

1. **Distinguish** code verification, solution verification and validation by their
   references, and **name** the error each one cannot detect.
2. **Construct** a manufactured solution, its source and its boundary data, and
   **measure** the order of accuracy of a code against it.
3. **Predict** a scheme's error at a stated grid spacing from its leading truncation
   term, and **check** the prediction against the measured error.
4. **Estimate** a discretisation error for a functional of interest from three
   grids, with the asymptotic range and the safety factor stated.
5. **Recognise** the two floors that limit refinement — round-off, set by the
   condition number, and the solver tolerance — and **separate** them from
   discretisation error.
6. **Design** a calibration/validation split, **compute** a reduced chi-square, and
   **report** the admitted set of models rather than a best fit.
7. **Demonstrate** the exact degeneracy between a physical constant and a freely
   fitted parameter, and **state** what it implies for the words "the model is
   validated".
8. **Write** a benchmark specification complete enough to reproduce a comparison
   table, including gauge, norm, source discretisation and cost metric.
9. **Explain** why agreement between independently written codes is not evidence of
   correctness, with a measured example.
10. **Decide** whether a method is applicable to a problem at all, before comparing
    accuracies.
11. **Report** a numerical result with its functional, discretisation error estimate,
    solver tolerance and model-form caveat, each labelled.
12. **Judge** when a discretisation study is not worth quoting because model-form
    uncertainty dominates it.

## Prerequisites

- [19-01 Numerical Foundations for Simulation](../01-numerical-foundations/README.md)
  — truncation error, order of accuracy, consistency, stability and dispersion.
- [19-02 Finite-Difference Methods](../02-finite-difference-methods/README.md) —
  the operators used as test subjects throughout this module.
- [03-12 Numerical Simulation in Python](../../03-scientific-computing/12-numerical-simulation-python/README.md)
  — a working 1-D solver you can apply the tests to.
- [18-06 Uncertainty Quantification](../../18-inverse-problems/06-uncertainty-quantification/README.md)
  — where discretisation error sits in an uncertainty budget (helpful, not
  essential).

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Code Verification: Order-of-Accuracy and Manufactured Solutions](01-code-verification.md) | research | The rate of convergence is the evidence; a machine-precision residual is not |
| 02 | [Solution Verification and Discretisation Error Estimation](02-solution-verification.md) | research | Richardson extrapolation and the GCI, the asymptotic range, and the two floors |
| 03 | [Model Validation Against Observations](03-model-validation.md) | research | A prediction test, not a fit; and a constant that multiplies a fitted parameter is invisible |
| 04 | [Standard Benchmark Problems and Community Comparisons](04-benchmark-problems.md) | research | A comparison is only as meaningful as its specification; agreement is not verification |

## Suggested path

**If you write simulation code:** lesson 01 first, and apply it to your own solver
this week. Lesson 02 next, because it is what you will need for every production
run afterwards.

**If you consume simulation results:** lesson 03, then lesson 02 §5 (the floors) —
those are the two places where a published number is most often over-claimed.

**If you are preparing a comparison or a benchmark suite:** lesson 04, then lesson
01 for the verification method, then the exercises at ★★★ level in all four
lessons.

**If you have one afternoon:** read lesson 01 §5 and lesson 03 §5; they are the
measurements, and they are the parts that change behaviour.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-code-verification.md`](01-code-verification.md) | Lesson 01 |
| [`02-solution-verification.md`](02-solution-verification.md) | Lesson 02 |
| [`03-model-validation.md`](03-model-validation.md) | Lesson 03 |
| [`04-benchmark-problems.md`](04-benchmark-problems.md) | Lesson 04 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Four runnable demonstrations |

## How to run the demos

Use the project virtual environment, which provides NumPy and SciPy:

```bash
cd 19-numerical-modeling-hpc/07-verification-validation-uncertainty/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python code_verification_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python solution_verification_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python model_validation_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python benchmark_problems_demo.py
```

Every demo prints labelled results with units, uses a fixed random seed
(`np.random.default_rng(20261014)`), runs in under a second, needs no network
access and writes no files. Each is print-only: no figures, no interactive
windows.

## Mastery checkpoint

Complete this without notes:

> You are handed a forward-modelling code for a geophysical observable, together
> with a report that says "the model is validated: residuals are consistent with
> the noise, and the code has a residual of $10^{-13}$". **(a)** State which of the
> three activities the report has actually performed, and which it has not.
> **(b)** Design the code-verification study you would run first, including the
> manufactured solution, the norm and the grids. **(c)** Give two model parameters
> in the report whose fitted values would absorb a $2$ per cent error in a physical
> constant, and state what independent measurement would reveal it. **(d)** State
> the discretisation error you would attach to the reported functional, and the two
> extra numbers a reader needs to reproduce your estimate. **(e)** For each number
> in your answer, label it **measured**, **derived** or **chosen**.

A worked version of (a)–(d) appears in the module's exercise sets, in the ★★★
problems of lessons 01 and 03.

## Common pitfalls across this module

1. **Treating a small residual as verification.** A wrong code solves its own
   equations exactly; lesson 01 measures $1.83\times10^{-13}$ alongside a $2$ per
   cent error.
2. **Reporting a single error value.** Without a refinement sequence, the order is
   unknown and two schemes of different order can have the same error (lesson 01
   §5).
3. **Quoting a fit as validation.** Only withheld prediction tests a model; lesson
   03 measures the self-validation trap at $\chi^{2}_{\text{red}} = 0.75$ against
   $16.4$ for the truth it rejects.
4. **Believing a passing validation certifies the physics or the constants.**
   Lesson 03 exhibits the degeneracy to machine precision.
5. **Refining past the floor.** Beyond the round-off and tolerance limits, more
   resolution makes the answer worse (lesson 02 §5).
6. **Comparing methods without a specification.** Gauge, norm, source
   discretisation and cost metric each move a ranking (lesson 04 §5).

## Related modules

- [19-01 Numerical Foundations for Simulation](../01-numerical-foundations/README.md)
  and [19-02 Finite-Difference Methods](../02-finite-difference-methods/README.md)
  — the theory and the operators verified here.
- [19-08 Geophysical Simulation Case Studies](../08-geophysical-simulation-case-studies/README.md)
  — the module that applies this discipline to five complete simulations.
- [19-06 High-Performance and Parallel Computing](../06-hpc-and-parallel-computing/README.md)
  — cost, reproducibility and provenance for the studies this module specifies.
- [18-inverse-problems](../../18-inverse-problems/README.md) — non-uniqueness,
  uncertainty taxonomy and reporting.
- [05-03-05 Validating Forward Codes Against Analytic Benchmarks](../../05-core-geophysics/03-forward-modelling-principles/05-forward-model-validation.md)
  — the geophysical forward-modelling route into the same material.
- [13-05-03 Benchmarking Geodynamic Codes](../../13-geodynamics-tectonics/05-geodynamic-modelling/03-benchmarking-geodynamics.md)
  — community comparison in practice.
