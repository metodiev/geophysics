# Module 01-05 — Single-Variable Calculus

**Stages:** beginner → intermediate · **Prerequisites:** none (mathematics modules
are self-contained; [01-01](../01-arithmetic/README.md) and
[01-02](../02-algebra/README.md) are helpful but not required)

This module builds the calculus a geophysicist actually uses: limits as the language
of approximation, derivatives as rates of change, Taylor expansions as the machinery
of linearisation, and integration as the bookkeeping of physical totals. It finishes
with improper integrals and series, because the potentials, transforms and iterative
solvers of later modules live in exactly those two settings.

The order is not the traditional order of a calculus course, and that is deliberate.
Limits come first because an idealisation without an error term is not a modelling
statement. Taylor series come *before* integration because linearisation — not
quadrature — is what most geophysical computation is made of. Series are last because
by then you have three chapters of reasons to care about convergence rates.

Throughout, each technique is used on a real quantity: a velocity gradient, a
geothermal gradient, a strain rate, the free-air correction, a heat budget, the
moment of inertia of a planet, the ray parameter of a seismic arrival.

## Learning objectives

By the end of this module you will be able to:

1. State and use the $\varepsilon$–$\delta$ definition of a limit, classify
   discontinuities in Earth models, and determine the leading asymptotic behaviour of
   a quantity and the rate at which it approaches its limit.
2. Compute derivatives from first principles and by the rules, interpret a derivative
   physically with its units, and choose a finite-difference step from the data's
   precision rather than for convenience.
3. Write the Taylor polynomial of a function with its Lagrange remainder, quantify the
   error of any approximation you use, and linearise a nonlinear model while stating
   where the linearisation fails.
4. Set up and evaluate physical integrals — mass, moment of inertia, accumulated heat,
   mean values — with the correct differential and a dimensional check, and estimate
   the quadrature error of any numerical evaluation.
5. Decide whether an improper integral converges, identify integrable versus fatal
   singularities, and remove a singularity by substitution rather than by brute-force
   refinement.
6. Judge the convergence and the *rate* of a series or an iteration, bound the
   truncation error of an expansion, and explain the difference between a convergent
   and an asymptotic series.

## Lessons

| # | Lesson | Level | Key idea |
|---|---|---|---|
| 01 | [Limits, Continuity and the Idea of Approximation](./01-limits-and-continuity.md) | beginner | Every idealisation is a limit; the error term is the modelling statement |
| 02 | [Derivatives and Rates of Change](./02-derivatives.md) | beginner | A derivative is a local linear model with units; finite differences have a precision floor |
| 03 | [Differentiation Rules and Implicit Differentiation](./03-differentiation-rules.md) | beginner | Rules are compressed limits; implicit differentiation handles constraints |
| 04 | [Taylor Series, Linearisation and Small-Angle Approximations](./04-taylor-series.md) | intermediate | Linearisation buys tractability; the remainder is the receipt |
| 05 | [Integration Techniques and Definite Integrals](./05-integration.md) | intermediate | An integral is a low-pass filter on a function, evaluated with a known error order |
| 06 | [Improper Integrals, Singularities and Convergence](./06-improper-integrals.md) | intermediate | Integrability is decided by the weight, not by the singularity |
| 07 | [Sequences, Series and Convergence Tests](./07-sequences-and-series.md) | intermediate | Convergence is not enough; the rate decides whether a method is usable |

## Suggested path

**If calculus is new to you:** all seven lessons in order, with the exercises. Budget
12–18 hours of genuine work. Do not skip lesson 04: it is the one that later modules
assume.

**If you have a standard calculus course behind you:** attempt the ★★ exercises in
lessons 04, 06 and 07 first. If you can do the Lagrange remainder bound in
[01-05-04](./04-taylor-series.md) ★2 and the $p$-integral classification in
[01-05-06](./06-improper-integrals.md) ★1 without notes, you can skip to
[Module 01-06](../06-multivariable-calculus/README.md).

**If you are an experienced practitioner:** read the "when it fails" material —
Section 3.4 of [01-05-01](./01-limits-and-continuity.md) on the $(a/z)^{2}$ far-field
rate, Section 3.4 of [01-05-02](./02-derivatives.md) on noise-limited differentiation,
Section 3.9 of [01-05-07](./07-sequences-and-series.md) on asymptotic series. Those
three arguments recur constantly in inverse theory.

**If you are heading for seismology or potential fields:** prioritise
[01-05-03](./03-differentiation-rules.md) (the ray parameter derivation),
[01-05-04](./04-taylor-series.md) (moveout and linearised inversion) and
[01-05-06](./06-improper-integrals.md) (potentials and slabs).

## Materials in this module

| Path | Contents |
|---|---|
| [`01-limits-and-continuity.md`](./01-limits-and-continuity.md) … [`07-sequences-and-series.md`](./07-sequences-and-series.md) | The seven lessons |
| [`exercises/`](./exercises) | One exercise set and one fully worked solution set per lesson |
| [`code/limits_demo.py`](./code/limits_demo.py) | Numerical limits, jump continuity, far-field convergence, cancellation |
| [`code/derivatives_demo.py`](./code/derivatives_demo.py) | Velocity gradient, free-air gradient, geothermal flux, strain rate, noise-limited differentiation |
| [`code/differentiation_rules_demo.py`](./code/differentiation_rules_demo.py) | Every rule checked numerically; implicit slopes; ray parameter |
| [`code/taylor_linearisation_demo.py`](./code/taylor_linearisation_demo.py) | Taylor truncation, small angles, free-air and Bouguer coefficients, moveout, $3u^{2}$ |
| [`code/integration_demo.py`](./code/integration_demo.py) | Quadrature orders on physical integrands; moment of inertia; heat totals |
| [`code/improper_integrals_demo.py`](./code/improper_integrals_demo.py) | $p$-tests, substitution, Gaussian and Fourier integrals, the Bouguer slab limit |
| [`code/series_convergence_demo.py`](./code/series_convergence_demo.py) | Geometric and harmonic series, ratio test, fixed-point and Newton rates, asymptotic $E_1$ |

All demonstrations use the Python standard library only, so they run in any
environment in which Python itself does. They print tables rather than plotting:
the numbers are the point, and you are meant to predict them before running.

## Mastery checkpoint

Complete this without notes. It is the module's own summary of itself.

> A gravimeter sits at a site that is uplifting at 4 mm/yr. The local velocity model
> is $v(z) = 1600 + 0.6z$ m/s, the crustal geotherm is $25$ K/km with
> $k = 2.5$ W m⁻¹ K⁻¹, and the region is a half-space of density
> $2670$ kg/m³. **(a)** Compute the rate of change of the free-air-corrected gravity
> at the site, in µGal/yr, and state the two derivatives you multiplied and why they
> multiply. **(b)** Estimate the parabolic moveout error at 2 km offset for a
> reflector with $t_0 = 1.5$ s in this velocity model, and say whether the parabolic
> approximation is adequate. **(c)** Compute the total heat flowing through a
> $50\ \mathrm{km}\times50\ \mathrm{km}$ area, in MW, and state which of the inputs
> limits your confidence. **(d)** Decide whether
> $\int_1^{\infty}e^{-z}/z\,dz$ converges and whether
> $\int_0^{1}\ln z\,dz$ converges, justifying each in one line. **(e)** A solver's
> error ratio per iteration is $0.94$. Estimate the number of iterations for
> $10^{-9}$ accuracy, and explain in one sentence why you would not use that solver.

Worked versions of the components appear as follows: (a) is the chain-rule
calculation of [01-05-03](./03-differentiation-rules.md) Section 3.3, applied in the
same way as the elevation-uncertainty problem of [01-05-02](./02-derivatives.md)
★★★8; (b) is [01-05-04](./04-taylor-series.md) ★★★6; (c) is
[01-05-05](./05-integration.md) Section 3.4; (d) is
[01-05-06](./06-improper-integrals.md) ★1; (e) is
[01-05-07](./07-sequences-and-series.md) ★★4.

## Common pitfalls across this module

1. **Quoting a limit or an approximation without its error term.** The number is the
   easy half; the error bound is the part that makes it usable.
2. **Shrinking the finite-difference step.** Differentiation amplifies noise as
   $1/h$ and round-off as $1/h$; the right step is large, and it is chosen from the
   data's precision.
3. **Expanding in a dimensional quantity.** The expansion parameter must be a ratio of
   like quantities: $z/R$, $x/(vt_0)$, $\delta m/m_0$, $\theta$.
4. **Trusting a linearisation because the residual is small.** Validity is governed by
   the *model* perturbation, as the $3u^{2}$ rule of
   [01-05-04](./04-taylor-series.md) shows.
5. **Assuming an integral converges because the region looks finite.** Both
   $\int_1^{\infty}dx/x$ and $\int_0^{1}dx/x$ diverge; check the exponent.
6. **Confusing converged with convergent.** An algebraic tail of $1/L$ needs enormous
   ranges; an exponential tail does not.
7. **Judging a series or a solver by its first few values.** The harmonic series looks
   convergent for ten million terms. Measure the rate, not the values.
8. **Treating a divergent asymptotic series as broken.** Truncate it at the smallest
   term: it is how multipole expansions are used.

## Related modules

- [01-01 Arithmetic and Numerical Reasoning](../01-arithmetic/README.md) — the
  precision and floating-point limits that this module keeps bumping into.
- [01-02 Algebra, Functions and Modelling](../02-algebra/README.md) — the functions
  differentiated here, especially exponentials and decay laws.
- [01-03 Trigonometry and Periodic Phenomena](../03-trigonometry/README.md) — the
  identities behind the trigonometric derivatives and the small-angle regime.
- [01-06 Multivariable and Vector Calculus](../06-multivariable-calculus/README.md) —
  the direct continuation: gradients, multiple integrals, Jacobians.
- [01-07 Linear Algebra](../07-linear-algebra/README.md) — where derivatives become
  Jacobians and series become eigenvalues.
- [01-09 Partial Differential Equations](../09-partial-differential-equations/README.md) —
  the diffusion, Laplace and wave equations built from these derivatives and integrals.
- [01-10 Fourier Analysis and Spectral Methods](../10-fourier-analysis/README.md) —
  improper integrals over the whole axis, and what convergence means there.
- [01-11 Complex Numbers and Analysis](../11-complex-analysis/README.md) — contour
  integration and residue methods for the integrals of lesson 06.
- [01-12 Numerical Methods for Mathematical Problems](../12-numerical-methods/README.md) —
  quadrature, root finding and error control in production form.
- [18-inverse-problems](../../18-inverse-problems/README.md) — linearisation, Jacobians
  and iterative solvers: lessons 04 and 07 applied at scale.
