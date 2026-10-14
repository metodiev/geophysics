---
id: 03-13-02
title: "Testing Numerical Code Against Analytic Solutions"
level: advanced
prereqs: ["03-13-01", "03-03-02", "01-09-02"]
estimated_minutes: 100
tags: [verification, convergence, analytic-solutions, discretisation, tolerance, richardson]
---

# Testing Numerical Code Against Analytic Solutions

Lesson 01 assumed you had a reference value. For a formula copied from a paper
that is often true. For a finite-difference solver, a quadrature, or an
iterative inversion it is not: the whole difficulty is that you have one
implementation and no truth to compare it with. This lesson is about
manufacturing truth — deriving a closed-form solution independently of the code,
and asserting on the *rate* at which the code's error vanishes rather than on
any single number it produced.

The distinction has names in the computational-science literature. **Code
verification** asks "am I solving the equations right?" and is answered by
analytic solutions and order-of-accuracy tests. **Solution verification** asks
"how accurate is this particular numerical solution?" and is answered by
convergence studies. **Validation** asks "are these the right equations?" and is
answered only by measurement. A test suite can do the first two. It cannot do
the third, and confusing them is the most common methodological error in
computational geophysics.

## Learning objectives

By the end of this lesson you will be able to:

1. **Distinguish** verification, solution verification and validation, and say
   which one a given test is doing.
2. **Derive** an analytic reference solution independently of the code, and
   explain why an independent derivation is the only kind that can find a bug.
3. **Measure** an observed order of convergence from a grid sequence, and assert
   on the order rather than on a single error.
4. **Explain and demonstrate** that refining a step size is not a monotone
   improvement, and identify the two competing error terms from measurement.
5. **Separate** discretisation error, round-off error and quadrature error in a
   numerical experiment, and state which one limits the achievable tolerance.
6. **Write** a verification test whose tolerance is justified by the
   discretisation error, and a guard test for the stability condition.

## Prerequisites

- [03-13-01 pytest: Tests, Fixtures, Parametrisation and Approximate Comparisons](./01-pytest-basics.md)
  — the suite machinery this lesson builds on.
- [03-03-02 scipy.integrate](../03-scipy/02-integrate.md) — `quad`, adaptive
  quadrature and the error estimate it returns.
- [01-09-02 The Heat Equation](../../01-mathematics/09-partial-differential-equations/02-heat-equation.md)
  — separation of variables, which produces the analytic solutions used here.

## 1. What counts as truth

Three reference sources are available, in decreasing order of trustworthiness.

| Source | Independent of the code? | Catches a wrong equation? | Cost |
|---|---|---|---|
| A closed-form solution | yes, if derived by hand | yes | minutes |
| A conservation law or symmetry | yes | sometimes | minutes |
| A golden output from a previous run | no | no | seconds |

Only the first two are *verification*. The third is *regression testing*: it
detects that something changed, which is genuinely useful, but it cannot detect
that the answer was wrong from the beginning. The distinction is not academic.
`code/coverage_demo.py` contains a plant: a free-air correction with the wrong
sign, worth 61.72 mGal at 100 m of relief, together with a "regression" test
whose expected value was captured from the buggy code. Line coverage is 90.9%,
the suite passes, and the defect is now pinned in place. Only a reference
derived *outside* the code can refute it.

The two analytic references used in this lesson are the transient decay of a
Fourier mode in one dimension,

$$u(x,t) = e^{-\kappa \pi^2 t / L^2}\sin\!\left(\frac{\pi x}{L}\right),
\qquad \kappa = 10^{-6}\ \mathrm{m^2\,s^{-1}},\ L = 1\ \mathrm{m},\ t = 2\times10^4\ \mathrm{s},$$

and, for a steady problem, $-\mathrm{d}^2u/\mathrm{d}x^2 = \sin(\pi x)$ on
$(0,1)$ with $u(0) = u(1) = 0$, whose solution is
$u = \sin(\pi x)/\pi^2$. Both were obtained by separating variables, before any
code was written.

## 2. The explicit scheme and its two error terms

The FTCS discretisation of $u_t = \kappa u_{xx}$ is

$$u_j^{n+1} = u_j^{n} + r\left(u_{j+1}^n - 2u_j^n + u_{j-1}^n\right),
\qquad r = \frac{\kappa\,\Delta t}{\Delta x^2},\qquad r \le \tfrac12 .$$

The stability bound $r \le \tfrac12$ is not an implementation detail; it is a
*guard test*, and Section 6 writes it as one. For the sine mode, the scheme is
exactly $(1 - 4r s^2)^{n_t}$ with $s = \sin(\pi \Delta x/2L)$, so the error can
be expanded in closed form. Writing
$A = \kappa\pi^2 t/L^2$, $\phi = \pi^2\Delta x^2/(12L^2)$ and
$B = \kappa^2 t \pi^4/L^4$:

$$\ln u_{\text{num}} - \ln u_{\text{exact}}
= \underbrace{+A\phi}_{\text{spatial, fixed}} - \underbrace{\tfrac12 B\,\Delta t}_{\text{temporal}}
+ \mathcal{O}(\Delta t^2).$$

**The two terms carry opposite signs.** With the parameters above,
$A\phi = 4.0587\times10^{-6}$ and $\tfrac12 B \Delta t = 9.7409\times10^{-6}$ at
$\Delta t = 10$ s. The prediction of the model is that they cancel at

$$\Delta t^\ast = \frac{2A\phi}{B} = 4.17\ \mathrm{s}.$$

The measurement confirms it and shows why a naive convergence study misleads:

| $n_t$ | $\Delta t$ (s) | $r$ | measured $\max\lvert u_{\text{num}} - u_{\text{exact}}\rvert$ |
|---|---|---|---|
| 2000 | 10.0 | 0.400 | $4.6645\times10^{-6}$ |
| 4000 | 5.0 | 0.200 | $6.6633\times10^{-7}$ |
| 8000 | 2.5 | 0.100 | $1.3327\times10^{-6}$ |
| 16000 | 1.25 | 0.050 | $2.3322\times10^{-6}$ |

Halving $\Delta t$ from 10 s to 5 s reduces the error by a factor 7. Halving it
twice more makes the error **larger**, by factors 2 and 1.75. The error is a
difference of two terms that passed through zero between 5 s and 2.5 s, exactly
as the 4.17 s prediction says.

> **Consequence for testing.** A convergence test must show two or more
> refinements moving the error the *same* way. A single refinement is not
> evidence of anything, and a tolerance chosen from a single grid is a
> measurement of one point on a non-monotone curve.

## 3. Order of accuracy, measured

The steady problem gives a clean order measurement. The three-point second
difference converges as $\mathcal{O}(h^2)$, so the observed order

$$p = \log_2\frac{\lVert e_h \rVert}{\lVert e_{h/2} \rVert}$$

should approach 2. The measured values, from `code/analytic_solutions_demo.py`:

| $n$ | $h$ | $\max\lvert u_h - u_{\text{exact}}\rvert$ | observed $p$ |
|---|---|---|---|
| 8 | $1.111\times10^{-1}$ | $1.019379\times10^{-3}$ | — |
| 16 | $5.882\times10^{-2}$ | $2.876115\times10^{-4}$ | 1.8255 |
| 32 | $3.030\times10^{-2}$ | $7.647078\times10^{-5}$ | 1.9111 |
| 64 | $1.538\times10^{-2}$ | $1.972041\times10^{-5}$ | 1.9552 |
| 128 | $7.752\times10^{-3}$ | $5.007489\times10^{-6}$ | 1.9775 |
| 256 | $3.891\times10^{-3}$ | $1.261675\times10^{-6}$ | 1.9887 |

Mean of the last three orders: **1.9738**. The sequence rises monotonically
towards 2 from below, which is the signature of an $\mathcal{O}(h^2)$ term plus
an $\mathcal{O}(h^4)$ correction — the leading error is being cancelled, so the
observed order is asymptotically $2 - \mathcal{O}(h^2)$.

**This is the assertion to write**, not the error at one grid:

```python
def test_rate_steady_second_order():
    errors = []
    for n in (32, 64, 128, 256):
        _, u, ue = asd.solve_steady_sine(n)
        errors.append(float(np.max(np.abs(u - ue))))
    orders = [math.log2(errors[i] / errors[i + 1]) for i in range(len(errors) - 1)]
    assert all(1.85 < o < 2.15 for o in orders), orders
```

The band is two-sided on purpose. A first-order scheme fails the lower bound; a
scheme that is accidentally *better* than the theory — usually because it
converges to the wrong limit, or because the manufactured solution is too
special — fails the upper bound. A one-sided test accepts both errors.

### 3.1 Why the rate is the right assertion

The error at one grid is $e = C h^p$, and $C$ is a property of the *problem and
the solution*, not of the scheme. Change the source term and $C$ changes by
orders of magnitude while $p$ does not. A test that asserts an absolute error is
therefore a test that has hard-coded the problem; a test that asserts $p$ is a
test of the method. That is the whole reason the computational-science
literature reports "second-order accurate" rather than "an error of $10^{-6}$".

### 3.2 Richardson extrapolation

Given three grids and $2^p \approx 4$, the *observed* order and a higher-order
estimate of the limit follow from

$$u_{\text{ext}} = u_h + \frac{u_h - u_{h/2}}{2^p - 1}.$$

This is not a test; it is a *diagnostic*. When the extrapolated value jumps
between grid triples, the asymptotic regime has not been reached and the order
you measured is not the order of the scheme. Use it as a smell test:

```python
def richardson(e_coarse, e_medium, e_fine):
    p = math.log2(e_coarse / e_medium)
    if abs(p - math.log2(e_medium / e_fine)) > 0.1:
        raise ValueError(f"not converging at a consistent rate: p1={p}")
    return p
```

Reporting a Richardson-extrapolated value without that consistency check is one
of the ways a "converged" answer is really a pre-asymptotic one.

## 4. Quadrature: verifying an integral against the shell theorem

The gravity anomaly of a uniform sphere computed by brute-force midpoint
quadrature, on the axis at depth $d$, is

$$g_z = G\rho \int_0^R\!\!\int_0^{\pi}\!\!\int_0^{2\pi}
\frac{d + s\cos\theta}{\left(d^2 + s^2 + 2ds\cos\theta\right)^{3/2}}
\,s^2\sin\theta \;\mathrm{d}\varphi\,\mathrm{d}\theta\,\mathrm{d}s .$$

Newton's shell theorem says the exterior field of a spherically symmetric body is
*exactly* $GM/d^2$ for every $d \ge R$. So the difference between the quadrature
and $GM/d^2$ is **pure numerical error** and must fall as the rule is refined.
Measured, with $R = 100$ m, $\rho = 3000$ kg m$^{-3}$:

| grid $(n_s, n_\theta, n_\varphi)$ | points | relative error at $d = 1000$ m | at $d = 110$ m |
|---|---|---|---|
| 20, 40, 60 | 0.05 M | $3.634\times10^{-4}$ | $2.738\times10^{-3}$ |
| 40, 80, 120 | 0.38 M | $9.083\times10^{-5}$ | $6.484\times10^{-4}$ |
| 60, 120, 180 | 1.30 M | $4.037\times10^{-5}$ | $2.860\times10^{-4}$ |
| 100, 200, 300 | 6.00 M | $1.453\times10^{-5}$ | $1.026\times10^{-4}$ |
| 160, 320, 480 | 24.58 M | $5.677\times10^{-6}$ | $4.002\times10^{-5}$ |

The error falls by roughly a factor 2.5 to 4 per doubling of the mesh — between
first and second order, consistent with a midpoint rule on an integrand whose
effective smoothness degrades as the field point approaches the source. At
$d = 110$ m ($1.1R$) the finest grid, 24.58 million points, still carries
$4.0\times10^{-5}$ of relative error, **seven times** the error at $d = 1000$ m
for the same work. That is the measured reason production gravity codes use
closed-form prism kernels instead of quadrature.

Two lessons follow, and both are test-design lessons:

1. **Converge the quadrature before interpreting any difference.** A first
   attempt at this experiment reported the $d = 500$ m quadrature as "agreeing
   with the point-mass formula to $3.9\times10^{-5}$", implying that the sphere's
   finite size mattered. It does not: the shell theorem is exact. The difference
   was entirely quadrature error, and the claim was measurement error, not
   physics. This is exactly the failure mode Section 1 warns about.
2. **Cost scales with proximity.** A tolerance of $10^{-5}$ is cheap at
   $d = 10R$ and expensive at $d = 1.1R$. State the tolerance *and* the regime.

### 4.1 An independent quadrature

`scipy.integrate.quad` is an independent implementation of a different rule
(adaptive Gauss–Kronrod). Comparing against it is weaker than comparing against
a closed form but far stronger than comparing against yourself. Measured:
$\int_0^1 e^{-x}\mathrm{d}x$ against $1 - e^{-1}$,

| method | value | error |
|---|---|---|
| `quad(..., epsabs=1e-12, epsrel=1e-12)` | 0.6321205588285577 | 0.000e+00 |
| exact $1-e^{-1}$ | 0.6321205588285577 | — |
| `quad`'s own reported error estimate | — | $7.018\times10^{-15}$ |

The measured error is zero to the last bit, while `quad` *reports* $7\times
10^{-15}$. That is not a contradiction: the reported value is an estimate of the
quadrature error, and the two implementations agree to the last representable
digit. It is, however, a reminder that an error *estimate* is not a bound.

## 5. Round-off: the floor no refinement removes

Every refinement experiment has a floor, and it is not zero. For the central
difference of $\sin$ at $x = 1$ the measured error reached a minimum of
$1.114\times10^{-11}$ at $h = 10^{-5}$ and then *rose* as $\mathcal{O}(u/h)$
dominated. For an $\mathcal{O}(h^2)$ method the floor is around
$u^{2/3} \approx 3.7\times10^{-11}$ relative; for the $\mathcal{O}(h)$ forward
difference, $u^{1/2} = 1.49\times10^{-8}$ absolute, which is what the previous
lesson measured.

$$\text{total error} \;\approx\; C h^p \;+\; \frac{K u}{h^{q}} .$$

Setting the derivative to zero gives the optimal step and the achievable floor.
Two design consequences:

- **A tolerance below the floor is a test of the compiler.** If a double
  precision algorithm converges to $10^{-12}$ relative and you assert
  $10^{-15}$, you have asserted something about the platform.
- **A refinement study must stop before the floor.** Three points on the
  asymptotic branch, all above the floor, or the observed order is meaningless.
  In the steady-convergence table above the finest grid reaches
  $1.26\times10^{-6}$, four orders above the floor, which is why the order
  sequence is still clean.

## 6. Python demonstration

`code/analytic_solutions_demo.py` runs all three experiments and prints the
tables above; `code/test_analytic_solutions.py` turns each into an assertion.
Both run offline under the project virtual environment:

```bash
.venv/bin/python 03-scientific-computing/13-testing-profiling-packaging/code/analytic_solutions_demo.py
.venv/bin/pytest 03-scientific-computing/13-testing-profiling-packaging/code/test_analytic_solutions.py -q
```

Measured result of the suite in this environment:

```
13 passed in 0.07s
```

The four kinds of test in that file, in increasing order of usefulness:

```python
def test_single_grid_transient_heat():
    """A correct-looking assertion that would also pass for a broken scheme."""
    _, u, ue = asd.ftcs_heat_sine(nx=201, nt=2000, kappa=KAPPA, length=LENGTH, t_end=2.0e4)
    np.testing.assert_allclose(u, ue, atol=1e-5, rtol=0.0)
```

```python
def test_rate_refinement_is_not_monotone_in_dt():
    """A measured fact, encoded so that nobody 'fixes' it later."""
    errs = []
    for nt in (2000, 4000, 8000):
        _, u, ue = asd.ftcs_heat_sine(201, nt, KAPPA, LENGTH, 2.0e4)
        errs.append(float(np.max(np.abs(u - ue))))
    assert errs[1] < errs[0]           # coarsening dt helps at first ...
    assert errs[2] > errs[1]           # ... and then stops helping
    assert errs[2] / errs[1] == pytest.approx(2.0, rel=0.1)
```

```python
@pytest.mark.parametrize("depth_m", [1000.0, 500.0, 300.0])
def test_shell_theorem_quadrature(depth_m):
    q = asd.sphere_gravity_quadrature(radius, density, depth_m, 60, 120, 180)
    exact = asd.G_SI * mass / depth_m**2 * asd.GAL_PER_MS2
    np.testing.assert_allclose(q, exact, rtol=1.0e-4)   # the measured quadrature error
```

```python
def test_stability_guard_rejects_oversized_step():
    with pytest.raises(ValueError, match="unstable"):
        asd.ftcs_heat_sine(nx=51, nt=10, kappa=KAPPA, length=LENGTH, t_end=2.0e4)
```

The first is a *smoke test with a number in it*: its tolerance, $10^{-5}$, was
chosen to sit above the measured spatial floor ($4.06\times10^{-6}$) and below
what a wrong $\Delta t$ scaling would produce ($4.66\times10^{-6}+
4.06\times10^{-6}$). It is defensible, and it is still the weakest test in the
file, because it would pass for any scheme with roughly the right dissipation.
The second is a measured fact about the scheme, encoded so that a future reader
cannot "simplify" it into a monotone assertion. The third compares against an
independent exact result. The fourth is a *guard*: it asserts that the code
refuses a configuration whose results cannot be trusted, which is a claim worth
more than any number the code produces.

## 7. Assumptions and limits

- **A matching analytic solution verifies the code, not the model.** Agreement
  with the heat equation says nothing about whether conduction is the right
  physics for a given geothermal problem. That is validation, and it needs data.
- **A manufactured solution must exercise the terms you care about.** Choosing
  $u = \sin(\pi x)$ with constant coefficients leaves variable-coefficient and
  advection terms untested.
- **Orders measured on non-smooth problems are not the scheme's order.** A
  discontinuity or a singularity caps the observed rate at the smoothness of the
  solution, which is why the quadrature above degrades as $d \to R$.
- **A convergence rate does not bound the error constant.** Two second-order
  schemes can differ by orders of magnitude in absolute error.
- **The stability bound $r \le 1/2$ is specific** to explicit FTCS on the
  constant-coefficient diffusion equation in one dimension. Do not transplant it
  to another stencil or another dimension without re-deriving it.

## 8. Common mistakes

1. Asserting an error at one grid, in a formula whose prefactor you have not
   measured, and calling it a convergence test.
2. Refining once and concluding the code is convergent.
3. Refining past the round-off floor and reporting the resulting noise as a
   loss of accuracy in the method.
4. Comparing against a golden file produced by the same code and calling it
   verification.
5. Interpreting a difference between two numerical methods as physics when the
   mesh has not been converged — the error made and corrected in Section 4.
6. Choosing a tolerance from a run of the code rather than from the
   discretisation, which makes the test a tautology.
7. Forgetting that the *stability* guard is also a test, and discovering the
   instability in a production run instead.
8. Quoting an order of convergence without the grid range and the errors it came
   from; the number is not reproducible otherwise.

## 9. Real-world applications

- **Geodynamic and thermal modelling.** Every published mantle-convection code
  has a benchmark suite (for example the blankenbach-style steady convection
  cases) whose purpose is exactly Section 3: measure the rate, compare with
  other codes, report the discrepancy.
- **Seismic wave propagation.** Order-of-accuracy tests on the spatial stencil
  decide the grid points per wavelength a production survey must carry, which is
  a cost decision worth millions of dollars in acquisition and compute.
- **Potential-field modelling.** The shell-theorem experiment in Section 4 is
  the standard verification for a tesseroid or prism kernel: compare against
  $GM/d^2$ where the closed form is exact, and separately measure the cost as
  the observation point approaches the source.
- **Inversion codes.** Verifying an adjoint by finite differences of the
  objective function, and verifying a forward solver against a layered analytic
  response, is the minimum evidence that published inversion images mean what
  they claim.

## 10. Further reading

- **Roache, P. J. (1998). *Verification and Validation in Computational Science
  and Engineering*. Hermosa.** Level: advanced. The source of the
  verification/validation distinction and of the grid-convergence index in
  Section 3.2.
- **Oberkampf, W. L. & Roy, C. J. (2010). *Verification and Validation in
  Scientific Computing*. Cambridge University Press.** Level: advanced. The
  systematic treatment, including code vs solution verification.
- **Salari, K. & Knupp, P. (2000). *Code Verification by the Method of
  Manufactured Solutions*. Sandia Report SAND2000-1444.** Level: intermediate.
  The technique of choosing a solution first and deriving the source term that
  makes it exact — the method that makes Section 1's first row available for any
  equation.
- **Higham, N. J. (2002). *Accuracy and Stability of Numerical Algorithms*
  (2nd ed.). SIAM.** Chapters 1 and 3. Level: advanced. Round-off floors and the
  optimal step-size analysis of Section 5.
- **SciPy.** [`scipy.integrate.quad`](https://scipy.org) — the adaptive
  quadrature and its error estimate used in Section 4.1.
- **NumPy.** [`assert_allclose`](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_allclose.html)
  — the comparison used throughout, with `rtol=1e-7, atol=0` defaults.

> Note on citations: bibliographic details are given so you can locate the
> works. This repository does not host or reproduce copyrighted text.

## 11. Related lessons

- [03-13-01 pytest: Tests, Fixtures, Parametrisation and Approximate Comparisons](./01-pytest-basics.md)
  — the tolerance and comparison machinery used here.
- [03-13-03 Profiling CPU and Memory](./03-profiling.md) — the cost side of the
  refinement trade-off: doubling the mesh costs $2^d$.
- [03-13-08 Reproducible Environments](./08-reproducible-environment.md) — why an
  order-of-accuracy measurement may not reproduce on another BLAS.
- [03-03-02 scipy.integrate](../03-scipy/02-integrate.md) — quadrature and ODE
  integration, with the residual checks this lesson formalises.
- [01-01-05 Error, Conditioning and Stability](../../01-mathematics/01-arithmetic/05-error-and-conditioning.md)
  — conditioning and stability, which decide the round-off floor of Section 5.

## 12. Self-assessment checklist

- [ ] I can say whether a given test of mine is verification, solution
      verification or validation, without hedging. (§1)
- [ ] I can derive an analytic solution for a simple PDE independently of my
      code. (§1)
- [ ] I can compute an observed order of convergence from a grid sequence and
      state the asymptotic range. (§3)
- [ ] I can explain why asserting on $p$ is better than asserting on $e_h$. (§3.1)
- [ ] I know from measurement that refining a step can *increase* the error, and
      I can name the two competing terms. (§2)
- [ ] I can distinguish quadrature error from physical difference, and I know
      what happens when I get that wrong. (§4)
- [ ] I can estimate the round-off floor of a scheme and keep my refinement
      study above it. (§5)
- [ ] I can write a stability guard test. (§6)
- [ ] I can say what my tolerance is justified by, in one sentence, for every
      assertion in my suite. (§8)
