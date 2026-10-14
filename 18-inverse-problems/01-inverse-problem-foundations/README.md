# Module 18-01 — Foundations of Inverse Problems

**Stages:** advanced → doctoral · **Prerequisites:** [05-03 Forward Modelling
Principles](../../05-core-geophysics/03-forward-modelling-principles/README.md)
and [01-07 Linear Algebra](../../01-mathematics/07-linear-algebra/README.md);
[01-16 Functional Analysis for Inverse Problems](../../01-mathematics/16-functional-analysis/README.md)
helps for lessons 02 and 05.

This module fixes the vocabulary of the whole folder and, more importantly, the
habit of honesty that the rest of it depends on. It is built around one central
difficulty: **the forward problem and the inverse problem are not symmetric, and
the forward calculation gives you no warning at all.** Gravity is smooth,
bounded, cheap to evaluate and always defined; its inverse multiplies a
$0.1\%$ data error into a $16.7\%$ model error, and the demonstration in lesson 01
measures that number rather than asserting it.

The second honest difficulty is that *non-uniqueness is a counting result, not an
apology.* Lesson 03 derives an exactly $11$-dimensional null space, constructs
two models whose densities differ by $50\ \mathrm{kg\,m^{-3}}$ in every layer and
which produce **bit-identical** data, and then solves for the exact feasible
interval of every single cell — so the answer to "how non-unique is it?" is a
table of intervals, not a caveat. Lesson 02 does the same for Hadamard's three
conditions, one at a time, and shows that a discretised problem *always* satisfies
the stability condition while its continuum limit does not.

Every number you will read in these lessons was printed by a demonstration you can
run, with units, in under a second, using a fixed random seed. All models and data
in this module are **SYNTHETIC**.

## Learning objectives

By the end of this module you will be able to:

1. State forward and inverse problems for an experiment and write the
   discretised linear model with correct units in the kernel.
2. Measure the error amplification of an inverse problem and convert it into a
   data-error budget before acquisition.
3. Test Hadamard's existence, uniqueness and stability conditions one at a time
   and decide which has failed from measured numbers.
4. Derive a null space, construct the equivalence class, and report per-parameter
   feasible intervals instead of a single model.
5. Explain why discretised problems are never ill posed and yet their refinements
   reproduce an unbounded inverse.
6. Decompose model and data space into informed and uninformed parts, and predict
   the unfittable fraction of noise.
7. Justify a parameterisation, a basis and a damping parameter as modelling
   choices with measurable consequences.

## Prerequisites

- [05-03-01 The Forward Problem: From Model to Data](../../05-core-geophysics/03-forward-modelling-principles/01-forward-problem.md) —
  the map from model to data and its ill-conditioning.
- [01-07-04 Rank, Null Space and Solvability](../../01-mathematics/07-linear-algebra/04-rank-and-nullspace.md) —
  the four fundamental subspaces.
- [01-07-08 Singular Value Decomposition](../../01-mathematics/07-linear-algebra/08-svd.md) —
  the basis used by every demonstration here.
- [01-16-05 Ill-Posedness in the Sense of Hadamard](../../01-mathematics/16-functional-analysis/05-ill-posedness.md) —
  the continuum statement that the matrices approximate.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Forward vs Inverse Problems and the Practical Asymmetry](01-forward-and-inverse.md) | advanced | A $0.1\%$ data error becomes a $16.7\%$ model error; the gain is a property of the design |
| 02 | [Hadamard's Conditions: Existence, Uniqueness, Stability](02-hadamard-well-posedness.md) | graduate | Twelve independent measurements buy twelve layers; the discrete problem is never ill posed, its limit is |
| 03 | [Null Space, Non-Uniqueness and Equivalence Classes](03-null-space.md) | graduate | Two models 50 kg/m³ apart in every layer give identical gravity; report intervals, not cells |
| 04 | [Discretisation, Parameterisation and Model Choice](04-discretisation-reality.md) | doctoral | The grid, the basis and the damping rule all move the answer, measurably |
| 05 | [Model Space, Data Space and Mappings Between Them](05-model-space-data-space.md) | graduate | $70\%$ of white noise is unfittable; the inverse map is set-valued and needs a rule |

## Suggested path

**If you are new to inverse problems:** lessons 01–03 in order, running each
demonstration and checking one number from each table by hand before moving on.
Lesson 03 is the one that changes how you write conclusions.

**If you already invert data but want the theory:** 01 §4–§5 (the budget), then
02 §4–§6 (refinement and tolerance), then 05 §4–§7 (projectors and why the normal
equations are a trap).

**If you are preparing a research project:** 01 §7 (scale invariance as a design
tool), 03 §5–§6 (interval reporting), 04 §4–§7 (effective rank, equivalence-class
sampling, basis choice), plus the ★★★ problems in every companion.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-forward-and-inverse.md`](01-forward-and-inverse.md) | Lesson 01 |
| [`02-hadamard-well-posedness.md`](02-hadamard-well-posedness.md) | Lesson 02 |
| [`03-null-space.md`](03-null-space.md) | Lesson 03 |
| [`04-discretisation-reality.md`](04-discretisation-reality.md) | Lesson 04 |
| [`05-model-space-data-space.md`](05-model-space-data-space.md) | Lesson 05 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Five runnable, print-only demonstrations |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib and
SymPy:

```bash
cd 18-inverse-problems/01-inverse-problem-foundations/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python forward_and_inverse_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python hadamard_well_posedness_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python null_space_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python discretisation_reality_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python model_space_data_space_demo.py
```

Every demonstration prints labelled results with units, uses the fixed seed
`np.random.default_rng(20261014)`, needs no network access and exits 0. None of
them plots; none of them takes more than a second.

## Mastery checkpoint

Complete this without notes:

> A layered gravity experiment has seven readings, of which two are exact
> negatives, and you plan a $100$-layer parameterisation. **(a)** State the
> numerical rank and the dimension of the effective null space at a relative
> tolerance of $10^{-10}$, and explain why the rank is not seven. **(b)** The
> smallest retained singular value is $1.02\times10^{-8}$ of the largest: compute
> the projector error you should expect. **(c)** Name the three numbers you must
> quote when reporting a density at a chosen depth, and why a single value is
> dishonest. **(d)** A colleague proposes doubling the number of stations in the
> same spread to fix the resolution. Evaluate the proposal with the
> scale-invariance argument.

A worked version of (a)–(b) appears in the lesson-02
[solutions](exercises/02-hadamard-well-posedness-solutions.md) and lesson-04
[solutions](exercises/04-discretisation-reality-solutions.md).

## Common pitfalls across this module

1. **Judging an inverse problem by its forward map.** Smooth, bounded and cheap
   says nothing about the inverse.
2. **Reporting a rank without a tolerance.** Three tolerances, three rank answers,
   all defensible.
3. **Saying "non-unique" and stopping.** Report the dimension, the directions and
   the effect on the quantity you are actually interpreting.
4. **Using the normal equations.** Same null space, squared condition number.
5. **Treating the parameterisation as bookkeeping.** The grid, basis and damping
   move the reported answer by per-cent amounts in the demonstrations.
6. **Calling a single noise realisation a systematic result.** Use ensembles.

## Related modules

- [18-02 Linear Inverse Problems](../02-linear-inverse-problems/README.md) — the
  overdetermined, underdetermined and mixed cases in full generality.
- [18-03 Regularisation and Stabilisation](../03-regularization/README.md) — what
  to do when the inverse problem is unbounded.
- [05-03 Forward Modelling Principles](../../05-core-geophysics/03-forward-modelling-principles/README.md) —
  the forward operator from the modelling side.
- [01-16 Functional Analysis for Inverse Problems](../../01-mathematics/16-functional-analysis/README.md) —
  the infinite-dimensional setting.
- [20-07 Inverse Methods in Signal Processing](../../20-signal-processing/07-inversion-in-signal-processing/README.md) —
  the same mathematics in the time-series setting.
