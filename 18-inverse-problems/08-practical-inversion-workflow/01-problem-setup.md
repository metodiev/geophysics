---
id: 18-08-01
title: "Setting Up a Solvable Inverse Problem"
level: graduate
prereqs: ["18-01-04", "18-03-01"]
tags: [inverse-problems, workflow, parameterisation, discretisation, resolution]
---

# Setting Up a Solvable Inverse Problem

> All models and data in this module are **SYNTHETIC**. The kernels, grids, noise
> levels and weights are chosen teaching ingredients; no number below is a
> measurement of the Earth.

## Learning objectives

By the end of this lesson you will be able to:

1. **Translate** a physical question into a data count, a noise level and a
   parameterisation, and **state** which of the three is fixed by the experiment.
2. **Compute** $\operatorname{tr}R$ and $\min\operatorname{diag}R$ for competing
   discretisations of the same physical problem and **use** them to choose one.
3. **Explain** why fitting the data better is not evidence for a better model,
   using a measured misfit-versus-model-error table.
4. **Decide** from the noise level whether a candidate cell is a parameter of the
   problem or a choice of grid.
5. **Write** a setup statement that a reviewer can check: what is measured, with
   what error, what is parametrised, and what is assumed.

## Prerequisites

- [18-01-04 Discretisation, Parameterisation and Model Choice](../01-inverse-problem-foundations/04-discretisation-reality.md) —
  the discretisation is a choice, not the Earth.
- [18-03-01 Why Regularisation Is Physically and Statistically Justified](../03-regularization/01-why-regularize.md) —
  a grid you cannot resolve must be regularised.

## 1. The three numbers you need before you invert

Every inversion setup is decided by three numbers:

- $p$, the number of independent observations;
- $\sigma$, the data error (measured, or assumed and then stated);
- $n$, the number of model parameters, together with the sensitivity matrix $G$.

Two of the three are set by the experiment. $p$ and $\sigma$ are what the survey
actually delivered; $n$ is a **choice**. The mistake this lesson exists to
prevent is choosing $n$ last, to make the model look detailed, and then treating
the result as if the data had determined it.

The formal object that decides the matter is the model resolution matrix

$$R = C\,G^{T}C_d^{-1}G, \qquad
C = \left(G^{T}C_d^{-1}G + P_0\right)^{-1},$$

with $P_0$ the regularisation. $\operatorname{diag}R \in [0,1]$: a cell with
$R_{jj}\approx1$ is recovered, a cell with $R_{jj}\approx0$ is a weighted average
of its neighbours or is unresolved, and $\operatorname{tr}R$ is the number of
**effective parameters** the data support.

## 2. Worked example: four discretisations of one problem

`code/problem_setup_demo.py` fixes 12 observations with $\sigma = 1.0$ over a
20 km depth range, uses Gaussian sensitivity kernels of half-width 3 km, and
refines the grid from 6 to 80 cells. A cell of thickness $\Delta z$ contributes
in proportion to $\Delta z$, so refining the grid makes each cell's individual
signature smaller — the physical fact that decides the whole trade-off.

| cells | rank at $10^{-3}$ | $\operatorname{tr}R$ | $\min\operatorname{diag}R$ | $\operatorname{cond}(G^{T}G+\lambda D^{T}D)$ |
|---|---|---|---|---|
| 6 | 6 | 5.80 | 0.948 | $2.29\times10^{2}$ |
| 12 | 9 | 6.28 | 0.428 | $9.32\times10^{2}$ |
| 20 | 9 | 6.46 | 0.266 | $1.26\times10^{3}$ |
| 40 | 9 | 6.72 | 0.138 | $2.21\times10^{3}$ |
| 80 | 9 | 6.98 | 0.072 | $3.92\times10^{3}$ |

$\operatorname{tr}R$ rises slowly from 5.80 to 6.98 while
$\min\operatorname{diag}R$ falls from 0.948 to 0.072. The grid spends more
unknowns to buy a marginally larger number of parameters, **each resolved worse**.
The rank saturates at 9 once $n\ge12$, because the data cannot support more than
nine independent directions at this cut — and, more importantly, because each
individual cell has become too small to move the data.

## 3. Misfit is not the objective

Fitting the same synthetic data with 12, 40 and 80 cells:

| cells | chi per datum | model error (rms) |
|---|---|---|
| 12 | 0.851 | 0.6921 |
| 40 | 0.424 | 2.3886 |
| 80 | 0.626 | 1.6234 |

All three reach the stated noise level or below, so **the misfit cannot choose
between them**. The finest model reaches the lowest misfit *and* the largest
error against the truth: extra cells are extra freedom for the noise to enter. A
model with more parameters is not a better model — it is a different one.

## 4. Choosing the grid from the noise level

For each candidate discretisation, compare the data signature of one cell with
the noise:

| cells | cell size (km) | $\|G_{:,j}\|$ (one cell) | $\|G_{:,j}\|/\sigma$ |
|---|---|---|---|
| 6 | 3.33 | 6.0087 | 6.0 |
| 12 | 1.67 | 3.0044 | 3.0 |
| 20 | 1.00 | 1.8026 | 1.8 |
| 40 | 0.50 | 0.9013 | 0.9 |
| 80 | 0.25 | 0.4507 | 0.5 |

Once a cell's effect on the data falls below the noise, the cell is not a
parameter of the problem — it is a choice of grid. State the noise level first;
then the grid follows. If a finer grid is required for a reason external to the
data (agreeing with a geological model, for example), say so, and report the
resolution length of the resulting model.

## 5. Numeric demonstration

```bash
cd 18-inverse-problems/08-practical-inversion-workflow/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python problem_setup_demo.py
```

Four sections: the four parameterisations; resolution diagonals; misfit versus
model error; the sensitivity-to-noise comparison. Print-only, seeded, exits 0 in
well under a second.

## 6. Assumptions and regime of validity

1. **The kernel is known.** All resolution statements are conditional on $G$;
   a wrong kernel makes a confident, wrong resolution claim.
2. **A stated noise level.** Every threshold here is in units of $\sigma$. With
   an assumed $\sigma$, the conclusion is an assumption too.
3. **Linearisation.** For nonlinear problems $G$ is the local Jacobian and all
   statements are local; re-derive them at convergence.
4. **Independence of observations.** Correlated data errors change
   $\operatorname{tr}R$; use the error covariance, not a single $\sigma$.
5. **The physical question precedes the grid.** If the question is "how thick is
   the layer", a two-cell parameterisation answers it better than a 200-cell one.

## Mastery checkpoint

Without notes: **(a)** Define $R$ and $\operatorname{tr}R$ and state what each
diagonal entry means. **(b)** From the two tables, choose a grid for a study that
must resolve 1-km layers and justify the choice with numbers. **(c)** Explain why
the 40-cell model reaches the lowest misfit and the largest error. **(d)** State
the four items a setup statement must contain.

## Common pitfalls

1. **Choosing the grid for visual smoothness.** That is choosing the answer's
   resolution.
2. **Reporting the misfit as evidence of quality.** Section 3 is the counterexample.
3. **Leaving $n$ implicit.** "A 1 km grid" is a claim about resolution; make it.
4. **Regularising one grid and comparing it with an unregularised another.** The
   comparison is then about the penalty.
5. **Forgetting that a cell must move the data more than the noise** to be
   anything other than a smooth interpolation parameter.

## Related modules

- [02 Synthetic Testing, Checkerboards and Recovery Tests](02-synthetic-testing.md) —
  how to measure the resolution you just chose.
- [03 Assessing a Model: Resolution, Artifacts, Alternatives](03-model-assessment.md).
- [18-01-04 Discretisation, Parameterisation and Model Choice](../01-inverse-problem-foundations/04-discretisation-reality.md).
- [18-03-03 Choosing the Trade-Off: L-Curve, GCV, Discrepancy Principle](../03-regularization/03-parameter-choice.md).

Code: [`code/problem_setup_demo.py`](code/problem_setup_demo.py).
Exercises: [`exercises/01-problem-setup-exercises.md`](exercises/01-problem-setup-exercises.md).
