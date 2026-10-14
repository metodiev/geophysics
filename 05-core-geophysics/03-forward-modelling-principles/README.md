# Module 05-03 — Forward Modelling Principles

**Stages:** intermediate → graduate · **Prerequisites:** modules 01 and 02,
especially [02-08-01 Gravitational Potential](../../02-physics/08-potential-theory/01-gravitational-potential.md)
and [01-09-04 Laplace and Poisson Equations](../../01-mathematics/09-partial-differential-equations/04-laplace-poisson.md).

Forward modelling is the map from a model of the subsurface to the data it would
produce. It is the foundation of every interpretation and every inversion: you
cannot judge a model, or estimate one, without being able to predict its data.

This module covers the formal statement, the analytical solutions that serve as
intuition and as benchmarks, superposition, discretisation and its error
taxonomy, and the verification/validation discipline that makes a modelling
result trustworthy.

## Learning objectives

1. Write the forward problem as a linear system with physics in the kernel, and
   explain why the kernel is ill-conditioned.
2. Derive the sphere and 2-D line-mass solutions and the depth rules they imply,
   including the shape dependence of depth estimates.
3. Apply superposition, know which methods obey it, and know where it fails.
4. Measure a convergence order, use manufactured solutions, and distinguish
   modelling error from discretisation error.
5. Build a benchmark suite that provably fails when the code is wrong.

## Lessons

| # | Lesson | Level | Key idea |
|---|---|---|---|
| 01 | [The Forward Problem: From Model to Data](./01-forward-problem.md) | intermediate | Linearity in the kernel; ill-conditioning |
| 02 | [Analytical Solutions for Simple Bodies](./02-analytical-solutions.md) | advanced | Depth rules are shape-dependent |
| 03 | [Superposition and Building Complex Models](./03-superposition.md) | intermediate | Linear in the field, not always in the parameter |
| 04 | [Numerical Forward Modelling and Discretisation](./04-numerical-forward-modelling.md) | graduate | Every answer has an error you chose |
| 05 | [Validating Forward Codes Against Analytic Benchmarks](./05-forward-model-validation.md) | graduate | A test that cannot fail is not a test |

## Materials

| Path | Contents |
|---|---|
| [`01-forward-problem.md`](./01-forward-problem.md) | Lesson 01 |
| [`02-analytical-solutions.md`](./02-analytical-solutions.md) | Lesson 02 |
| [`03-superposition.md`](./03-superposition.md) | Lesson 03 |
| [`04-numerical-forward-modelling.md`](./04-numerical-forward-modelling.md) | Lesson 04 |
| [`05-forward-model-validation.md`](./05-forward-model-validation.md) | Lesson 05 |
| [`exercises/`](./exercises/) | Graded problem sets with worked solutions |
| [`code/`](./code/) | Four runnable demonstrations, listed below |

## Demos

| Script | What it measures |
|---|---|
| [`code/prism_gravity_demo.py`](./code/prism_gravity_demo.py) | Closed form vs Gauss-Legendre vs adaptive quadrature; thin-sheet limit |
| [`code/annihilator_nonuniqueness_demo.py`](./code/annihilator_nonuniqueness_demo.py) | Equivalent sources, an exact null vector, and instability with depth |
| [`code/dipole_vs_body_demo.py`](./code/dipole_vs_body_demo.py) | Sphere = dipole exactly; prism approaching it; magnetometer geometry |
| [`code/validation_benchmarks.py`](./code/validation_benchmarks.py) | Manufactured-solution order, quadrature convergence, injected-bug test |

Run them with the project virtual environment:

```bash
cd /Users/miroslav/Documents/workspace/geophysics/05-core-geophysics/03-forward-modelling-principles
for f in code/*.py; do /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python "$f"; done
```

Every script is offline, prints labelled results with units, uses
`np.random.default_rng(seed)` where randomness is needed, quotes node counts and
measured orders rather than wall-clock times, and exits 0.

## Mastery checkpoint

A prism with density contrast 500 kg/m³ occupies $x,y \in [-100,100]$ m,
$z \in [50,250]$ m. **(a)** State the three independent ways to compute its
$g_z$ at the origin and the measured agreement. **(b)** Show that a prism is not
exactly a dipole and state the measured convergence of the difference. **(c)**
Construct a model that fits a synthetic data set to machine precision but is
wrong by a factor of 6 in depth. **(d)** Explain what additional information
would exclude the wrong model. Sections 6.1 and 6.3 of lessons 01 and 02 and the
non-uniqueness demo contain the numbers.

## Common pitfalls

1. Believing the inverse problem is as tractable as the forward problem.
2. Using a depth rule without naming the assumed shape.
3. Assuming magnetic superposition at high susceptibility.
4. Refining a grid and calling the change "convergence."
5. Reporting agreement without a measured number or a stated tolerance.
6. Forgetting to inject a bug to prove the test can fail.

## Related modules

- [05-01 What Geophysics Measures](../01-what-geophysics-measures/README.md)
- [05-02 Fields and Observables](../02-geophysical-fields-and-observables/README.md)
- [05-04 Rock Physics](../04-rock-physics/README.md)
- [18-inverse-problems](../../18-inverse-problems/README.md)
- [19-numerical-modeling-hpc](../../19-numerical-modeling-hpc/README.md)
