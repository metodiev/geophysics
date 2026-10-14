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

### 3.1 Richardson extrapolation and the grid-convergence index, derived

An order measurement gives more than a number. If the error behaves as
$E(h) = Ch^p$, then two resolutions determine both $C$ and the value the
solution is converging *to*.

Let $u_1 = u(h)$, $u_2 = u(h/r)$ for a refinement ratio $r$ (usually 2). Then

$$u_1 - u_\text{exact} = Ch^p, \qquad u_2 - u_\text{exact} = C(h/r)^p,$$

so dividing and solving for $p$:

$$p = \frac{\log\!\left[(u_1-u_2)/(u_3-u_2)\right]}{\log r}
\quad\text{(three grids)}, \qquad\text{or}\qquad
p = \frac{\log(E_1/E_2)}{\log r}\quad\text{(if }u_\text{exact}\text{ is known)} .$$

Eliminating $C$ gives the **Richardson-extrapolated** value

$$u_\text{exact} \approx u_2 + \frac{u_2-u_1}{r^p-1},$$

and the **grid-convergence index**, a conservative uncertainty estimate:

$$\text{GCI} = F_s\,\frac{\lvert u_2-u_1\rvert/r^p}{\,r^p-1\,},
\qquad F_s \approx 1.25 .$$

**Measured application** to the manufactured-solution study of Section 6.4, where
the exact solution is known and $r = 2$:
$E_1 = 5.142005\times10^{-4}$ at $h = 0.025$,
$E_2 = 1.285204\times10^{-4}$ at $h = 0.0125$:

$$p = \frac{\log(5.142005\times10^{-4}/1.285204\times10^{-4})}{\log 2}
= 2.000334,$$

$$\text{GCI} = 1.25\,\frac{1.285204\times10^{-4}}{2^{2.000334}-1}
= 5.3534\times10^{-5},$$

and the Richardson error estimate at the finer grid is

$$u_2 + \frac{u_2-u_1}{r^p-1} \;\Rightarrow\;
\text{error} \approx \frac{E_2 - E_1/r^p}{r^p-1}
= \frac{1.285204\times10^{-4}-3.212824\times10^{-5}}{3.0003}
= 3.2121\times10^{-5},$$

against the actual error $E_2 = 3.2128\times10^{-5}$ — agreement to 0.02%.

**Physical interpretation.** Richardson extrapolation works because the leading
error term is *systematic*, not random: it is a known power of $h$ with a smooth
coefficient. That is exactly the property a benchmark is designed to expose, and
it fails (giving nonsense) when the observed order is not the asymptotic one —
for instance in a pre-asymptotic regime, or when the error is dominated by a
discontinuity. **Always check that $p$ is close to the scheme's nominal order
before trusting an extrapolation.**

### 3.2 Why an order test is more sensitive than a point comparison

A tolerance test asks "is the error below $\tau$?" An order test asks "does the
error behave as $h^p$?" The second catches a wider class of bugs.

Consider two ways a code can be wrong:

- **A multiplicative error**, $u_\text{num} = (1+\delta)u_\text{exact}$. The
  discretisation error is $\delta u_\text{exact}$, which is *independent of $h$*,
  so the measured order is 0 while the correct code gives 2. Detected by both
  tests, provided $\delta > \tau$.
- **A lower-order error term**, e.g. a mis-stencilled boundary closure
  contributing $O(h)$ instead of $O(h^2)$. At coarse resolution the second-order
  term dominates and the error looks acceptable; at fine resolution the
  first-order term takes over. A single-tolerance test at one resolution can miss
  this entirely; the order test cannot, because the slope changes.

**Concretely, from the demonstration:** the correct code passes a $10^{-6}$
tolerance at relative error $3.981\times10^{-15}$; a 2% kernel error fails at
$2.000\times10^{-2}$; and the manufactured-solution study returns orders
2.0013, 2.0003, 2.0001, whose *constancy* is the evidence that no hidden
lower-order term is present. **Report the order, not just the error.**

### 3.3 Choosing a tolerance from the application, derived

A tolerance is defensible only if it is tied to a physical uncertainty. Let the
forward model feed an inversion whose input parameters are uncertain by a
fraction $\delta_p$, and let the numerical error be $\epsilon$. Then

$$\epsilon \ll \delta_p \quad\text{is required, typically}\quad
\epsilon \le \delta_p/10 .$$

**Numbers.** Densities in a rock-physics workflow are uncertain by 5–10%
(they depend on mineralogy and porosity,
[05-04-01](../04-rock-physics/01-porosity-density-velocity.md)). So a numerical
tolerance of $10^{-2}$ is defensible and $10^{-6}$ is wasteful — it costs grid
points for precision that the physics cannot use. Conversely, for a
*differential* quantity, such as the change in anomaly produced by a 1% density
change, the numerical error must be far below 1% or the difference is
meaningless: here $\epsilon \le 10^{-3}$ is justified.

**The rule in words.** Ask what question the model's output will answer. If the
answer is "is this anomaly 3 mGal or 3.2 mGal?", a 1% tolerance suffices. If the
answer is "which of two models differing by 1% fits better?", the tolerance must
be an order of magnitude smaller than that difference — and the *grid* must be
chosen accordingly, using the derived ppw rule of
[05-03-04](./04-numerical-forward-modelling.md).

### 3.4 Verification and validation, as a table of measurable criteria

The distinction of Section 2 becomes operational when each row carries a test that
can fail.

| question | activity | test that can fail | what it cannot detect |
|---|---|---|---|
| Does the code solve the stated equations correctly? | verification | manufactured solution order; closed-form comparison; conservation check | wrong equations |
| Are the stated equations adequate for the earth? | validation | comparison with independent data; prediction of an unused observable | a code bug that mimics the data |
| Is the discretisation adequate at the working resolution? | verification | measured error at the *chosen* grid, not an asymptotic limit | modelling error |
| Is the tolerance defensible? | both | error $\le$ physical uncertainty (Section 3.3) | wrong physical inputs |
| Has round-off become the limit? | verification | error stops falling with refinement | all of the above |

**The asymmetry that matters.** Verification can be completed by one person with a
workstation. Validation cannot: it requires data the modeller does not control.
**A report that claims "validated" on the basis of manufactured solutions has
mis-described its evidence**, and this table is the language for saying so
precisely.

### 3.5 What would falsify this code? A worked analysis

A validation is only as strong as the falsification it survives. Take the prism
gravity code of this module and ask, explicitly, what would show it wrong.

| candidate failure | test | would the suite catch it? |
|---|---|---|
| wrong kernel prefactor | closed-form/quadrature comparison | **yes** — a 2% perturbation gives $2.000\times10^{-2}$ against a $10^{-6}$ tolerance |
| transposed coordinates | thin-sheet limit, symmetry | **partly** — the thin-sheet limit is symmetric, so only an asymmetric test catches it |
| wrong sign of $z$ | closed-form comparison | **yes** — the sign flips |
| wrong quadrature weights | convergence study | **yes** — convergence order collapses |
| wrong physical model (point mass used where a prism is required) | far-field test | **yes, and it is the *measured* 13% discrepancy at $200$ m** |
| wrong *equations* (e.g. ignoring a layer) | nothing in this suite | **no** — requires validation against data |

**The honest conclusion.** Five of the six candidate failures are caught; the sixth
— wrong physics — is not, and cannot be, by a suite that only checks the code
against itself and the literature. Stating that explicitly, with the quantification
of each catch, is what turns a benchmark table into a validation.

**The quantitative version of "the test is sensitive".** A test with tolerance
$\tau$ catches a bug of relative size $\delta$ iff $\delta > \tau$. Because the
suite is passed only if *every* test passes, its detection threshold is
$\min_i\tau_i$ — **one loose tolerance weakens the whole suite.** That is the
argument for keeping every tolerance in a suite at the same order of magnitude,
and for stating each one's justification rather than choosing round numbers.

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

### 6.6 Worked example: a complete expected-versus-measured validation

Good validation predicts the error *before* measuring it. Here is the full cycle
for the prism gravity code.

**Prediction.** The closed form and the quadrature share the model but not the
algebra, so their difference should be pure round-off: for a few hundred
floating-point operations, of order $\sqrt{N}\epsilon_\text{mach}
\approx 20\cdot2.2\times10^{-16} = 4\times10^{-15}$ relative. **Predicted
tolerance: $10^{-12}$**, two orders of safety margin.

**Measurement.** Closed form versus Gauss–Legendre ($n = 120$):
$1.825\times10^{-15}$; closed form versus `scipy.tplquad`: $1.327\times10^{-15}$
(estimated absolute error $7.9\times10^{-18}$).

**Verdict.** Both are *below* the predicted floor, and the prediction was
justified rather than fitted. This is what distinguishes a validation from a
conformity check.

**Second prediction — the thin-sheet limit.** A prism of half-width 50 km and
thickness 20 m should approach $2\pi G\rho t$ with a *modelling* residual from
its finite lateral extent and thickness, of order (thickness/half-width) effects
and edge truncation. Measured: 0.418528 mGal against 0.419359 mGal — a relative
$1.98\times10^{-3}$. **Predicted $10^{-2}$, measured $2\times10^{-3}$:**
consistent, and the residual is *irreducible by refinement* because it is
geometric, which the demonstration states explicitly.

**Third prediction — the injected bug.** Perturbing the kernel by a factor 1.02
should produce a relative error of exactly 0.02, detectable against a $10^{-6}$
tolerance. Measured: $2.000\times10^{-2}$. The test is demonstrably sensitive.

**The pattern.** Predict the magnitude and the *kind* of each expected
discrepancy (round-off, discretisation, or modelling), then measure. A
discrepancy larger than predicted by more than the safety factor is a bug; one of
the wrong *kind* is a modelling error; one that does not shrink with refinement
is either modelling or round-off, and the measured order tells you which.

### 6.7 A shortcut that fails: comparing a code against itself

**The shortcut.** Validate by running the code on a fine grid and a coarse grid
and checking that the answers agree to a few percent.

**Why it fails.** Both runs share every line of code. A systematic bug — a wrong
constant, a transposed index, a metres/kilometres confusion — appears in both and
cancels in the comparison. The measured agreement then reflects only
*discretisation*, which is exactly the error a convergence study is designed to
measure, not the error a benchmark is designed to catch.

**Quantified example.** A kernel with a 2% scaling error, run at two
resolutions, gives two answers differing by the discretisation error
($\sim10^{-12}$ relative for this smooth problem) *and both wrong by 2%*. The
self-comparison passes at $10^{-12}$ while the code is wrong at the $10^{-2}$
level — a false positive.

**What to do instead.** Compare against an *independent* implementation of the
same quantity: a closed form from the literature, an integral evaluated by a
different algorithm, an exact limit, or a manufactured solution. Where a truly
independent reference is impossible, say so — "verified to be self-consistent"
is a much weaker claim than "verified against an analytic solution", and the
difference must appear in the report.

### 6.8 Extended worked example: a complete validation table for the module's codes

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
