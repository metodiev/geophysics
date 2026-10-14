---
id: 05-03-05
title: "Validating Forward Codes Against Analytic Benchmarks"
level: graduate
prereqs: ["05-03-04"]
tags: [verification, validation, benchmarks, tolerance, reproducibility]
---

# Validating Forward Codes Against Analytic Benchmarks

## Learning objectives

1. **Distinguish** verification (solving the equations right) from validation
   (solving the right equations).
2. **Construct** a benchmark suite with a stated tolerance, a stated grid, and
   a test that provably fails when the code is wrong.
3. **Choose** benchmarks that exercise different code paths, not the same path
   five times.
4. **Report** a validation result so a reviewer can reproduce and challenge it.
5. **Recognise** the difference between a modelling discrepancy and a
   numerical error, and say how to tell them apart.

## Prerequisites

- [05-03-04 Numerical Forward Modelling and Discretisation](./04-numerical-forward-modelling.md)

## 1. Intuition

A forward code is a claim. Validation is the evidence for the claim. The
evidence is not "it looks right"; it is "it reproduces a quantity whose value is
known independently, to a tolerance stated in advance, with a test that fails
when the code is wrong."

Most published modelling studies would be stronger if they contained a table
like the one in Section 6.

## 2. Definitions

**Verification.** Confirming that the code solves the stated equations
correctly. Benchmarks: closed-form solutions, manufactured solutions,
conservation laws, symmetry properties, convergence orders.

**Validation.** Confirming that the equations represent reality, by comparison
with observation. Not achievable by code alone; needs data.

**Benchmark.** A problem with a known answer. It must be independent of the
code under test — reusing the same formula in the reference would prove nothing.

**Tolerance.** The largest error considered acceptable, chosen *before* running
and justified by the intended use, not by the result.

**Round-off floor.** The error level below which a tolerance is meaningless
($\approx 10^{-15}$ relative for double precision, more for long summations).

## 3. Construction of a benchmark suite

A useful suite covers:

1. **A closed form.** E.g. the prism formula against an independent quadrature.
   Exercises the kernel and the assembly.
2. **An exact non-obvious identity.** E.g. a uniformly magnetised sphere equals
   a point dipole outside it (shell theorem). Exercises the magnetisation
   integration and the field projection.
3. **A limit.** E.g. a wide, thin prism approaches $2\pi G\rho t$. Exercises the
   geometry handling.
4. **A manufactured solution.** Exercises the PDE stencil and boundary
   conditions.
5. **A symmetry.** E.g. an anomaly must be symmetric about a symmetric body.
   Cheap and very effective at catching indexing errors.
6. **A conservation or invariance property.** E.g. adding a constant density to
   an infinite layer changes nothing.

**Independence is the key requirement.** Where possible, write the reference in
a different code path (different algorithm, different library) so that a shared
bug cannot hide.

## 4. Units and dimensional analysis

Every benchmark must state: the physical quantity, its SI and field units, the
grid or node count, the measured error, and the tolerance.

| Benchmark | Quantity | Unit | Reference method | Tolerance rationale |
|---|---|---|---|---|
| Prism vs quadrature | $g_z$ | mGal | Gauss-Legendre | round-off floor ~1e-15 |
| Sphere vs dipole | $\lvert\mathbf{B}\rvert$ | nT | analytic dipole | shell theorem exact |
| Thin prism vs slab | $g_z$ | mGal | $2\pi G\rho t$ | finite-size residual ~2e-3 |
| Manufactured Poisson | $u$ | m$^2$s$^{-2}$ | analytic $u$ | order-2 truncation |
| Symmetry | $g_z(x)$ | mGal | mirror image | round-off |

## 5. Assumptions

1. **The reference is right.** A wrong reference makes a correct code fail. Use
   published formulas with sources, and cross-check the reference itself against
   a third method where possible.
2. **The tolerance is meaningful.** Above the round-off floor and below the
   physical uncertainty of the application.
3. **The test is sensitive.** It must fail for a plausible bug, demonstrated by
   injecting one.
4. **The benchmark exercises the same code path as production.** A test that
   only touches a special case proves little.

## 6. Worked examples (measured)

**6.1 Prism gravity.** Closed form versus Gauss-Legendre ($n=120$) versus
scipy adaptive quadrature: 1.021214 mGal from all three, relative differences
$1.8\times10^{-15}$ and $1.3\times10^{-15}$. Reference: Nagy (1966) closed form.

**6.2 Sphere magnetism.** Uniformly magnetised sphere (radius 100 m,
$\mathbf{M} = 5$ A/m downward) versus point dipole at 250 m, 400 m and 1000 m:
relative differences $1.5\times10^{-14}$, $1.0\times10^{-15}$,
$5.1\times10^{-15}$. Exact, as the shell theorem requires.

**6.3 Prism versus dipole.** Relative difference $1.29\times10^{-1}$ at 200 m
falling to $4.88\times10^{-4}$ at 3200 m, a factor of $\approx4.0$ per doubling
of distance — a *modelling* difference (octupole term), not a code error. The
test to distinguish: refine the grid; if the discrepancy does not change, it is
modelling, not discretisation.

**6.4 Manufactured solution.** Measured convergence orders 2.0013, 2.0003,
2.0001; fitted slope 2.000559 over four grids. Tolerance stated in advance as
$|p-2| < 0.01$.

**6.5 A test that fails when it should.** With a deliberate 2% scaling error
introduced, the relative error rises from $4.0\times10^{-15}$ to
$2.000\times10^{-2}$, failing the $10^{-6}$ tolerance by seven orders of
magnitude.

## 7. Python demonstration

Run `code/validation_benchmarks.py`. It is the benchmark suite described above:
manufactured solution with measured order, quadrature convergence, a
closed-form/independent-integral cross-check, and the injected-bug test. Every
number quoted in this lesson comes from it.

## 8. Exercises, mistakes, applications

Exercises: [`exercises/05-forward-model-validation-exercises.md`](./exercises/05-forward-model-validation-exercises.md).

**Common mistakes.** (1) Using the same formula in the code and the reference.
(2) Choosing the tolerance after seeing the error. (3) Benchmarking only the
easy case (e.g. a body centred at the origin). (4) Reporting "agreement is good"
with no number. (5) Concluding validation from verification: reproducing your
own equations does not make them right.

**Applications.** Gravity and magnetic modelling packages (prism, polyhedron);
seismic finite-difference codes; EM layered and 3-D codes; every serious
inversion package ships a benchmark suite built this way
([18-08-02 Synthetic Testing](../../18-inverse-problems/08-practical-inversion-workflow/02-synthetic-testing.md)).

## Extended worked example: a complete validation table for the module's codes

The four demonstrations in this module form a single benchmark suite. Stating
their measured results in one place is what a validation section in a paper or a
report should look like.

| Test | Reference (independent) | Quantity | Measured result | Tolerance | Pass? |
|---|---|---|---|---|---|
| Prism gravity, closed form vs Gauss–Legendre ($n=120$) | Nagy (1966) closed form | $g_z$ | rel. diff. $1.8\times10^{-15}$ | $10^{-10}$ | yes |
| Prism gravity, closed form vs scipy adaptive | scipy `tplquad` | $g_z$ | rel. diff. $1.3\times10^{-15}$ | $10^{-10}$ | yes |
| Quadrature convergence, $n = 4,8,16,32,64$ | $n = 200$ quadrature | $g_z$ | $1.19\times10^{-2}\to3.98\times10^{-15}$ | monotone | yes |
| Thin wide prism vs infinite slab | $2\pi G\rho t$ | $g_z$ | rel. diff. $1.98\times10^{-3}$ | $5\times10^{-3}$ | yes |
| Sphere vs point dipole (250 m, 400 m, 1000 m) | analytic dipole | $\lvert\mathbf{B}\rvert$ | $1.5\times10^{-14}$, $1.0\times10^{-15}$, $5.1\times10^{-15}$ | $10^{-10}$ | yes |
| Prism vs dipole, $r$ = 200→3200 m | analytic dipole | $\lvert\mathbf{B}\rvert$ | $1.29\times10^{-1}\to4.88\times10^{-4}$, factor 4.0/doubling | modelling | n/a |
| Manufactured Poisson, 4 grids | analytic $u$ | $u$ | order 2.0013, 2.0003, 2.0001; fitted 2.000559 | $\lvert p-2\rvert<0.01$ | yes |
| Injected 2% kernel error | $n=200$ quadrature | $g_z$ | rel. err. $2.000\times10^{-2}$ | must fail $10^{-6}$ | fails as required |
| Explicit diffusion, 3 grids | $\delta=\sqrt{2D/\omega}$ | decay length | $4.87\times10^{-3}$, $1.53\times10^{-3}$, $6.99\times10^{-4}$ | monotone | yes |

**How to read the table.** The first five rows are *verification*: the code
reproduces a quantity whose value is known independently, and the tolerance is
set above the round-off floor and below any physical significance. Row six is a
*modelling* difference deliberately left unexplained by the code test — the
prism genuinely is not a dipole. Row seven is an order measurement, which is
stronger than a point comparison because it constrains the *rate* of convergence.
Row eight is the meta-test: proof that the suite can fail.

**Tolerances justified, not chosen.** $10^{-10}$ for the geometry tests: two
orders of magnitude above the double-precision round-off floor
($\approx10^{-15}$ for a few hundred operations) and far below any physical
uncertainty in a density or a position. $\lvert p-2\rvert<0.01$ for the order
test: the four-grid fit achieved 2.00056, so the tolerance is met with a factor
of twenty to spare, and a tolerance of 0.001 would be too tight for four grids
because the asymptotic regime is only approximately reached.

**What this suite does not cover.** It says nothing about the *physics*: whether
a prism represents a real orebody, whether a homogeneous cell is an adequate
parameterisation, or whether the depth-to-cell-size ratio makes the
discretisation meaningful. Those are modelling questions, and the honest place
to record them is a "known limitations" paragraph alongside the table, not a
pass/fail column.

## 9. Further reading

- **Roache, P. J. *Verification and Validation in Computational Science and
  Engineering*.** Level: graduate. The canonical text.
- **Oberkampf, W. L. & Trucano, T. G. (2002).** Verification and validation in
  computational fluid dynamics. *Progress in Aerospace Sciences* 38, 209–272.
  Level: graduate. The taxonomy used here.
- **Nagy, D. (1966).** The gravitational attraction of a right rectangular
  prism. *Geophysics* 31, 362–371. The reference closed form.

## 10. Related lessons

- [05-03-04 Numerical Forward Modelling and Discretisation](./04-numerical-forward-modelling.md)
- [05-03-02 Analytical Solutions for Simple Bodies](./02-analytical-solutions.md)
- [18-08-02 Synthetic Testing](../../18-inverse-problems/08-practical-inversion-workflow/02-synthetic-testing.md)
- [22-data-engineering-reproducibility](../../22-data-engineering-reproducibility/README.md)

## Self-assessment checklist

- [ ] I can distinguish verification from validation.
- [ ] I can design six benchmarks covering different code paths.
- [ ] I can state a tolerance and justify it by the application.
- [ ] I can tell a modelling discrepancy from a numerical error.
- [ ] I can report a validation table a reviewer could reproduce.
