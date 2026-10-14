# Module 18-02 — Linear Inverse Problems

**Stages:** advanced → doctoral · **Prerequisites:** [18-01 Foundations of Inverse
Problems](../01-inverse-problem-foundations/README.md), especially lessons 03 and
05; [01-07 Linear Algebra](../../01-mathematics/07-linear-algebra/README.md) for the
SVD and projections.

This module solves the linear inverse problem in full, in the three regimes that
occur in practice: overdetermined (more data than parameters), underdetermined
(more parameters than data) and **mixed determined** — usually the real case, where
some combinations of parameters are pinned down and others are invisible. The
central honest difficulty is that all three are handled by one formula, the
generalised inverse, and that this formula contains a **choice**: it returns the
minimum-norm least-squares model, which is the model closest to the origin in the
norm you happened to pick, not the model the Earth has. Two demonstrations contrast
three selection rules that fit identical data to machine precision and disagree
completely about where the anomaly is.

The second difficulty is numerical and statistical at once. The singular value
decomposition makes the trade-off between resolution and noise explicit — lesson 04
measures the optimum truncation moving from $k=8$ to $k=5$ when the noise grows ten
times — and lesson 06 shows that the *reported uncertainty* is only as good as the
error covariance you assumed: with correlated noise, assuming independence
understated the standard error by a factor of about **30** in the measured example.
Every number in these lessons is printed by a demonstration you can run in about a
second, with units.

All models and data in this module are **SYNTHETIC**.

## Learning objectives

By the end of this module you will be able to:

1. Write and solve the overdetermined problem, and distinguish the normal
   equations from a QR/SVD route on conditioning grounds.
2. Derive the minimum-norm solution, verify its two defining properties, and
   explain why the resulting picture is a selection rule, not a measurement.
3. Recognise a mixed-determined problem and solve it with the Moore–Penrose
   inverse, verifying the four defining conditions.
4. Read the singular value decomposition as a list of independent experiments, and
   use data importance to plan or prune a survey.
5. Compute model resolution, kernel widths, the information matrix and the model
   covariance, and verify the whole apparatus against a synthetic recovery test.
6. Specify an error covariance, whiten the problem, and state what ignoring it
   costs in both efficiency and reported uncertainty.

## Prerequisites

- [18-01-03 Null Space, Non-Uniqueness and Equivalence Classes](../01-inverse-problem-foundations/03-null-space.md) —
  the feasible set and resolved combinations.
- [18-01-05 Model Space, Data Space and Mappings Between Them](../01-inverse-problem-foundations/05-model-space-data-space.md) —
  range, orthogonal complement and projectors.
- [01-07-07 Orthogonality, Projections and Least Squares](../../01-mathematics/07-linear-algebra/07-orthogonality.md) —
  the projection theorem behind the normal equations.
- [01-07-08 Singular Value Decomposition](../../01-mathematics/07-linear-algebra/08-svd.md) —
  the factorisation every demonstration here uses.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Overdetermined Problems and Least Squares](01-overdetermined.md) | advanced | Derive the normal equations; the covariance is the result, not a decoration |
| 02 | [Underdetermined Problems and Minimum-Norm Solutions](02-underdetermined.md) | advanced | Three rules, one fit, three different Earths; sparsity is not smallness |
| 03 | [The Generalised (Moore-Penrose) Inverse](03-generalized-inverse.md) | graduate | One formula for all regimes, unique but not continuous |
| 04 | [SVD Analysis: Model Resolution and Data Importance](04-svd-analysis-inverse.md) | doctoral | A duplicate ray buys no resolution; variance grows 14× where misfit falls |
| 05 | [Resolution and Information Matrices in Interpretation](05-resolution-matrices.md) | doctoral | $R_{jj}$ is not resolution; combinations beat cells by 3.35× |
| 06 | [Data Weighting and Error Covariance Specification](06-weighting-and-covariance.md) | graduate | Ignoring correlation understated the error by a factor 26.6–33.2 |

## Suggested path

**If you are new to least squares:** lessons 01 and 02 in order, then 03. Run each
demonstration and check one number per table by hand (the companions provide the
arithmetic).

**If you already fit data regularly:** 01 §4–§5 (covariance and $\chi^{2}$), 04
(truncation), 06 (weighting) — those three cover the errors that survive into
publication.

**If you are preparing a research project:** 02 §5 (selection rules), 03 §5–§6
(continuity and the damping trap), 04 §3–§7 (data importance and the measured
trade-off), 05 §4–§8 (resolution and the end-to-end verification), plus the ★★★
problems.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-overdetermined.md`](01-overdetermined.md) | Lesson 01 |
| [`02-underdetermined.md`](02-underdetermined.md) | Lesson 02 |
| [`03-generalized-inverse.md`](03-generalized-inverse.md) | Lesson 03 |
| [`04-svd-analysis-inverse.md`](04-svd-analysis-inverse.md) | Lesson 04 |
| [`05-resolution-matrices.md`](05-resolution-matrices.md) | Lesson 05 |
| [`06-weighting-and-covariance.md`](06-weighting-and-covariance.md) | Lesson 06 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Six runnable, print-only demonstrations |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib and
SymPy:

```bash
cd 18-inverse-problems/02-linear-inverse-problems/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python overdetermined_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python underdetermined_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python generalized_inverse_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python svd_analysis_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python resolution_matrices_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python weighting_and_covariance_demo.py
```

Every demonstration prints labelled results with units, uses the fixed seed
`np.random.default_rng(20261014)`, needs no network access and exits 0; none plots,
and the longest takes about one second. One demonstration additionally solves small
linear programmes with `scipy.optimize.linprog` to obtain exact feasible intervals.

## Mastery checkpoint

Complete this without notes:

> A transmission experiment has 12 rays, 16 cells and numerical rank 8 at a
> relative tolerance of $10^{-10}$. **(a)** State $\dim\operatorname{range}(G)$,
> $\dim\mathcal{N}(G)$ and $\operatorname{tr}R$, and say what each number means in
> one sentence. **(b)** Two rays are exact duplicates: what happens to the rank and
> to their importances when a third duplicate is added? **(c)** Write the complete
> solution set and say which member the generalised inverse returns. **(d)** The
> estimator's per-cell standard deviations are 0.0032–0.0171 s while a three-cell
> average has 0.0028 s; explain the difference and how it should change your
> reporting. **(e)** The errors are known to be correlated with $\rho=0.7$: name
> the transformation you apply and the check you run afterwards.

Worked versions of (a)–(d) appear in the lesson-03
[solutions](exercises/03-generalized-inverse-solutions.md) and lesson-05
[solutions](exercises/05-resolution-matrices-solutions.md).

## Common pitfalls across this module

1. **Using the normal equations out of habit.** The condition number is squared;
   measured $\kappa(G^{\!\top}G)/\kappa(G)^{2} = 1.000000$.
2. **Reporting a model without a covariance.** A parameter value alone is not a
   result.
3. **Treating the minimum-norm model as "the" model.** It is one member of an
   affine family, chosen by a rule.
4. **Reading $R_{jj}$ as resolution.** Kernel width is resolution.
5. **Assuming a misfit near the noise norm means success.** It is the expected
   outcome of a correct fit.
6. **Ignoring correlation.** The estimate stays unbiased; the quoted error can be
   thirty times too small.
7. **Choosing a truncation by eye.** Measure the bias–variance curve.

## Related modules

- [18-01 Foundations of Inverse Problems](../01-inverse-problem-foundations/README.md) —
  the vocabulary, the counting arguments and the equivalence classes.
- [18-03 Regularisation and Stabilisation](../03-regularization/README.md) — what to
  do when the linear inverse is unstable.
- [18-04 Nonlinear Inversion and Optimisation](../04-nonlinear-inversion/README.md) —
  the same linear algebra repeated inside an iteration.
- [01-14 Optimization and Variational Methods](../../01-mathematics/14-optimization/README.md) —
  the optimisation view of least squares.
- [06-06 Seismic Tomography](../../06-seismology/06-seismic-tomography/README.md) —
  the largest practical user of these matrices.
