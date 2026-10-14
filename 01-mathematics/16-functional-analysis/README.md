# Module 01-16 — Functional Analysis for Inverse Problems

**Stage:** graduate → doctoral · **Prerequisites:**
[07 Linear Algebra](../07-linear-algebra/README.md) (vector spaces, orthogonality,
projections, the SVD), [05 Single-Variable Calculus](../05-single-variable-calculus/README.md)
(integration, sequences and series, convergence), [06 Multivariable and Vector
Calculus](../06-multivariable-calculus/README.md) (integrals over regions, integral
theorems), [09 Partial Differential Equations](../09-partial-differential-equations/README.md)
(weak formulations and adjoints), [08 Ordinary Differential Equations](../08-ordinary-differential-equations/README.md)
(Sturm–Liouville theory).

This module is where the mathematics of geophysics stops being a description of
fields and becomes a description of *inference*. It is the last module of the
mathematics folder, and its whole purpose is to make
[18 Inverse Problems](../../18-inverse-problems/README.md) rigorous. The organising
idea is one line long:

> **An inverse problem is a statement about an operator, and the questions we ask
> of it — is it unique, is it stable, how much does it resolve — are questions
> about that operator's spectrum.**

Every lesson therefore develops its mathematics from the geophysical problem it
serves and then measures something numerically:

| Abstraction | The geophysical question it answers |
|---|---|
| Function spaces, norms | how wrong is a model, and in what sense — $L^2$ penalises outliers gently, $L^1$ does not |
| Hilbert spaces, orthogonal expansions | Fourier and spherical-harmonic expansions as projections; least squares as a projection onto a finite-dimensional subspace |
| Operators, adjoints, compactness | the adjoint is what makes gradient computation possible: adjoint tomography, full-waveform inversion |
| Spectral theory | eigenfunction bases, why the Earth's normal modes are discrete, what a resolution matrix means |
| Ill-posedness (Hadamard) | existence, uniqueness, stability — and how each fails differently in gravity and electromagnetic inversion |
| Tikhonov regularisation, L-curve | the trade-off, derived, demonstrated, and shown to be sensitive to the parameter |
| Discretisation, convergence, semiconvergence | what happens to the answer as the grid is refined, and why a residual below the noise is bad news |

## Learning objectives

By the end of this module you will be able to:

1. **Choose** a norm for a misfit and justify it from the noise model, with a
   numerical demonstration that the choice changes the fitted parameters.
2. **Project** a field onto an orthonormal basis, verify orthonormality under the
   correct measure (including the sphere's $\sin\theta$ weight), and interpret a
   truncated expansion as the best $L^2$ approximation at that order.
3. **Derive** an adjoint by integration by parts, track its boundary terms, and
   verify it with a dot-product test and a finite-difference gradient.
4. **Compute** the singular spectrum of a compact operator, explain why its
   singular values must decay, and state what the decay costs.
5. **Define** the three Hadamard conditions, diagnose which fails in a given
   inverse problem, and state the distinct remedy for each.
6. **Derive** the Tikhonov estimator, the filter factors and the resolution
   matrix, and choose the regularisation parameter by the L-curve, the discrepancy
   principle and generalised cross-validation — reporting where the rules disagree.
7. **Measure** the semiconvergence of an iterative inversion and locate the
   optimal stopping index from the noise level.
8. **Report** an inversion honestly: residual, model norm, effective number of
   resolved parameters, and the discretisation the numbers belong to.

## Lessons

| # | Lesson | Level | Key idea |
|---|---|---|---|
| 01 | [Vector Spaces of Functions, Norms and Inner Products](./01-function-spaces.md) | graduate | Measuring how wrong a model is; the choice of norm is a physical choice |
| 02 | [Hilbert Spaces and Orthogonal Expansions](./02-hilbert-spaces.md) | graduate | Least squares is a projection; spherical harmonics are the basis geophysics uses |
| 03 | [Linear Operators, Adjoints and Compactness](./03-operators.md) | doctoral | The adjoint is the engine of every gradient in modern inversion |
| 04 | [Spectral Theory of Operators and Eigenfunction Bases](./04-spectral-theory.md) | doctoral | Why the Earth's modes are discrete, and what a resolution matrix means |
| 05 | [Ill-Posedness in the Sense of Hadamard](./05-ill-posedness.md) | graduate | Existence, uniqueness, stability — three failures, three remedies |
| 06 | [Tikhonov Regularisation and the L-Curve](./06-regularization-theory.md) | graduate | The bias–variance trade-off, derived and demonstrated, including how sensitive it is |
| 07 | [Discretisation, Convergence and Regularisation Discrepancy](./07-discretization-convergence.md) | doctoral | Refining a mesh does not add information; a residual below the noise is a warning |

## How to work through the module

**If you are following the mathematics folder in order:** all seven lessons, in
order, with the exercises. Lessons 01, 02, 05 and 06 are the core and take roughly
16–20 hours with the exercises. Lessons 03, 04 and 07 are doctoral-level and are
the natural preparation for [18 Inverse Problems](../../18-inverse-problems/README.md);
they may be taken later, but lesson 03 should precede lesson 06 and lesson 06 must
precede lesson 07.

**If you are here from a geophysics application:**

| You are working on | Read |
|---|---|
| Gravity, magnetics, potential fields | [01](./01-function-spaces.md) §8, [05](./05-ill-posedness.md) in full, [06](./06-regularization-theory.md) §2–6 |
| Seismic or electromagnetic inversion | [03](./03-operators.md) §3–5, [05](./05-ill-posedness.md) §4–6, [06](./06-regularization-theory.md) in full |
| Adjoint codes and full-waveform inversion | [03](./03-operators.md) in full, [07](./07-discretization-convergence.md) §7 |
| Resolution and uncertainty statements | [04](./04-spectral-theory.md) §6, [06](./06-regularization-theory.md) §3 and §10 |
| Gravity/topography fields and their spectra | [02](./02-hilbert-spaces.md) §5, [04](./04-spectral-theory.md) §5 |
| Numerical code development and grid design | [01](./01-function-spaces.md) §6, [07](./07-discretization-convergence.md) in full |

**If you already invert data for a living:** attempt ★★★8 of
[05](./05-ill-posedness.md), ★★★8 of [06](./06-regularization-theory.md) and
★★★8 of [07](./07-discretization-convergence.md) first. If all three come out
cleanly, use the module as a reference and go directly to
[18 Inverse Problems](../../18-inverse-problems/README.md).

## Mastery checkpoint

You have mastered this module when you can do all of the following unaided:

- [ ] Choose a misfit norm from a noise model and defend the choice numerically.
- [ ] Verify that a set of functions is orthonormal under a stated measure, and
      explain what breaks when the measure is wrong.
- [ ] Project a field onto an orthonormal basis and state the error of a
      truncation as the norm of the discarded part.
- [ ] Derive the adjoint of a differential operator with its boundary terms and
      pass a dot-product test.
- [ ] Compute a gradient of a misfit with one adjoint solve and check it against a
      finite difference.
- [ ] Define compactness, identify it in a geophysical operator, and state what it
      costs.
- [ ] Compute the eigenvalues of a discretised Sturm–Liouville problem and explain
      why the spectrum of a bounded body is discrete.
- [ ] Compute a resolution matrix, read its trace and its rows, and say what they
      do not tell you.
- [ ] Diagnose which Hadamard condition fails in a given problem and prescribe the
      correct remedy.
- [ ] Derive the Tikhonov estimator and its filter factors from scratch.
- [ ] Choose a regularisation parameter by three rules, report where they disagree
      by more than a factor of ten, and explain the disagreement.
- [ ] Demonstrate semiconvergence and choose a stopping rule from the noise level.
- [ ] Explain why refining a mesh does not add information and why a residual below
      the noise level is evidence of a mistake.

## A note on verification

Every numerical result quoted in this module was produced by the scripts in
`code/`, which use the Python standard library only and can be run directly
(`python3 code/<script>.py`) with no packages installed. Each script builds its own
small dense-linear-algebra toolbox — Gaussian elimination, a cyclic Jacobi
eigensolver, quadrature rules — so that the singular value expansions, filter
factors and resolution matrices quoted in the text can be checked line by line.

Three conventions are followed throughout, and they were adopted because breaking
them caused errors during the writing of this module:

- **Every error is reported with its norm.** A truncation error, a misfit and a
  model error are three different numbers, and an unlabelled one is uninterpretable.
- **Every discretised claim names its discretisation.** A condition number, a
  resolution width and an effective parameter count all depend on the grid; the
  place where this matters is lesson 07, and it was found the hard way in lesson 05.
- **Where a claim could not be verified it is not stated.** Several expected
  behaviours did not appear in the experiments (for instance, the L-curve corner
  turned out *not* to be near the model-error minimum, and removing the inverse
  crime did *not* produce a residual floor). The text reports what was measured,
  and says so when a demonstration was left open rather than completed.

## Related modules

- [07 Linear Algebra](../07-linear-algebra/README.md) — the finite-dimensional
  version of every construction here, and the SVD that makes them computable.
- [08 Ordinary Differential Equations](../08-ordinary-differential-equations/README.md)
  — Sturm–Liouville theory, where eigenfunction bases come from physically.
- [09 Partial Differential Equations](../09-partial-differential-equations/README.md)
  — weak solutions, Lax–Milgram and the adjoint derived in a variational setting.
- [10 Fourier Analysis and Spectral Methods](../10-fourier-analysis/README.md) —
  the transform machinery behind the expansions of lesson 02.
- [12 Numerical Methods for Mathematical Problems](../12-numerical-methods/README.md)
  — the forward-side treatment of consistency, stability and convergence that
  lesson 07 contrasts with the inverse-side treatment.
- [14 Optimization and Variational Methods](../14-optimization/README.md) — the
  numerical side of the least-squares problems regularised here.
- [18 Inverse Problems](../../18-inverse-problems/README.md) — the destination:
  this module's abstractions used operationally, with covariance, Bayesian
  formulations and resolution reporting.
- [19 Numerical Modeling and HPC](../../19-numerical-modeling-hpc/README.md) —
  discretisation and solver decisions in production codes.
- [21 Statistics, Bayesian Inference and Machine Learning](../../21-statistics-bayesian-ml/README.md)
  — the probabilistic reading of the regularisation parameter.
