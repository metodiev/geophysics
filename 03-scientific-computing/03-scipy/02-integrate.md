---
id: 03-03-02
title: "scipy.integrate: Quadrature and ODE Integration"
level: intermediate
prereqs: ["03-03-01", "01-05-05", "02-05-04"]
estimated_minutes: 75
tags: [numerical-integration, quadrature, ode-solver, gravity, decay]
---

# scipy.integrate: Quadrature and ODE Integration

Two questions, one subpackage. The first is "what is the value of this
integral?", which is how a gravity anomaly of an arbitrary body is computed
and how a potential field is reduced to a number. The second is "how does
this quantity evolve?", which is how a cooling magma body, a radioactive
decay chain and a diffusing perturbation are predicted. Both are answered by
`scipy.integrate`, and both share a property that decides whether the answer
means anything: **an integrator will return a number whether or not the
problem was well posed.**

This lesson therefore works in the opposite order to a function reference. It
establishes the accuracy of the tools against integrals whose values are
known, then uses them for the two geophysical tasks, and it reports the
measured agreement at every step.

Run the demonstration before reading on:

```
.venv/bin/python 03-scientific-computing/03-scipy/code/integrate_demo.py
```

## Learning objectives

By the end of this lesson you will be able to:

1. **Choose** between an adaptive rule (`quad`) and a fixed rule
   (`fixed_quad`, `simpson`, `trapezoid`) from the smoothness of the
   integrand and the number of evaluations you can afford.
2. **Report** the accuracy of a quadrature against a closed-form value rather
   than against the routine's own error estimate.
3. **Handle** an improper integral with infinite limits, and an integrand with
   an integrable endpoint singularity, by stating the structure to `quad`.
4. **Compute** the vertical gravity anomaly of an arbitrary polygonal body by
   quadrature, and **validate** the quadrature against two exact limits before
   trusting it.
5. **Solve** an initial-value problem with `solve_ivp`, verify the result
   against its analytic solution, and use a conservation law as an
   independent check.
6. **Decide** when a stiff solver is required, using function-evaluation
   counts rather than intuition.
7. **State** what `quad`'s returned `abserr` is and is not, and give a
   case where it is misleadingly small.

## Prerequisites

- [03-03-01 SciPy Organisation and When to Use Which Subpackage](./01-scipy-overview.md)
  — the subpackage map and the residual-based verification habit.
- [01-05-05 Integration](../../01-mathematics/05-single-variable-calculus/05-integration.md)
  — what a definite integral is and what the trapezoid rule approximates.
- [02-05-04 Heat Conduction, Fourier's Law and Thermal Diffusivity](../../02-physics/05-thermodynamics/04-heat-conduction.md)
  — the decay and diffusion problems solved numerically in §4.
- [01-06-02 Multiple Integrals](../../01-mathematics/06-multivariable-calculus/02-multiple-integrals.md)
  — the volume integrals of §3.

## 1. What `quad` actually does

`scipy.integrate.quad` is a Python wrapper around QUADPACK's `QAGS`
(A.1), an **adaptive Gauss–Kronrod** rule with extrapolation. The algorithm
is worth stating precisely, because every one of its failure modes follows
from it:

1. Place a 21-point Gauss–Kronrod rule on the interval. The 21 points are
   shared between a 10-point Gauss rule (accurate for smooth integrands) and
   the 21-point Kronrod rule that extends it.
2. Compare the two estimates of the integral. **Their difference is the error
   estimate** returned as `abserr`.
3. If the estimate exceeds the requested tolerance, bisect the interval with
   the largest estimated error and recurse.
4. When the subdivision stops improving, apply the epsilon-algorithm (a
   sequence extrapolation) to the subdivision results.

The consequence is the one line in the demo that matters most:

```
    quad (adaptive Gauss-Kronrod, QUADPACK QAGS)
      value = 3.141592653589793   |error| = 0.00e+00   reported abserr = 3.49e-14
      function evaluations actually used: 21
```

`quad` computed $\int_0^1 4/(1+x^2)\,dx = \pi$ to the last bit of double
precision, with 21 evaluations of the integrand, and reported an error
estimate of $3.5\times10^{-14}$. That reported error is not the true error —
the true error is zero at the printing precision, and the estimate is
pessimistic by three orders of magnitude, which is the direction you want.
**`abserr` is an estimate of the error of the *last* rule comparison, not a
guarantee.** §3 shows the case where it misleads completely.

## 2. Fixed rules, and what they cost

An adaptive rule assumes the integrand is smooth between the points it
chooses. When the integrand is only known on a grid — which is the normal
situation for measured data — the only available rules are fixed ones.
`fixed_quad` applies a Gauss–Legendre rule of chosen order to the whole
interval, and `trapezoid`/`simpson` integrate a sampled array.

Measured on the same integrand:

```
    rule                              value                    |error|
    fixed_quad (Gauss-Legendre), n= 2 3.147540983606557       5.95e-03
    fixed_quad (Gauss-Legendre), n= 3 3.141068139963168       5.25e-04
    fixed_quad (Gauss-Legendre), n= 5 3.141592639884753       1.37e-08
    fixed_quad (Gauss-Legendre), n=10 3.141592653590047       2.54e-13
    fixed_quad (Gauss-Legendre), n=20 3.141592653589793       0.00e+00
    trapezoid on n=11                 3.139925988907159       1.67e-03
    simpson   on n=11                 3.141592613939215       3.97e-08
    trapezoid on n=101                3.141575986923129       1.67e-05
    simpson   on n=101                3.141592653589754       3.95e-14
    trapezoid on n=1001               3.141592486923126       1.67e-07
    simpson   on n=1001               3.141592653589793       0.00e+00
```

Three facts, all of them visible in the numbers:

- **A Gauss rule beats a Newton–Cotes rule at the same node count.** Ten
  Gauss nodes give $2.5\times10^{-13}$ where 101 trapezoid nodes give
  $1.7\times10^{-5}$. Gauss nodes cluster towards the ends of the interval,
  where the integrand's curvature is largest, and the rule is exact for
  polynomials to degree $2n-1$.
- **The convergence rates are the textbook ones, with one instructive
  exception.** Going from 11 to 101 trapezoid nodes (a factor of 9.2 in $n$)
  reduces the error from $1.67\times10^{-3}$ to $1.67\times10^{-5}$: a factor
  of 100, i.e. exactly $n^{-2}$. The Simpson errors go from $3.97\times10^{-8}$
  to $3.95\times10^{-14}$ — a factor of $10^{6}$ where $n^{-4}$ predicts only
  $7.1\times10^{3}$, so the observed order is $n^{-6}$. The reason is in the
  error term: Simpson's leading contribution is proportional to
  $f'''(b)-f'''(a)$, and for this integrand
  $f'''(x) = 96x(1-x^{2})(1+x^{2})^{-4}$ vanishes at *both* endpoints, so the
  $n^{-4}$ term cancels and the next one governs. The trapezoid rule's leading
  term, by contrast, is $\frac{h^{2}}{12}[f'(b)-f'(a)] = \frac{1}{6n^{2}}$ — a
  constant of exactly $1/6$, which the measured values match to better than 1%.
- **The trapezoid rule's error here is enormous in relative terms.** For an
  integral of size $\pi$, an absolute error of $10^{-3}$ is four significant
  digits lost. This is not a defect of the rule; it is the cost of not being
  allowed to choose where to sample.

## 3. Improper integrals and structured integrands

Two further properties of `quad` decide whether it is usable on a real
problem.

**Infinite limits are handled directly.** QUADPACK maps
$[a,\infty)$ to a finite interval and applies the same adaptive machinery,
with a transformation that concentrates points where the integrand decays:

```
    integral_0^inf  exp(-x) dx  = 1.000000000000000  (exact 1)      |error| = 0.00e+00
    integral_-inf^inf exp(-x^2) dx = 1.772453850905516  (exact sqrt(pi) = 1.772453850905516)  |error| = 0.00e+00
```

Both are exact to the last printed digit. This is the property that makes an
infinite slab or a half-space integral tractable without truncation, and it
is used in §4.

**An integrable singularity is handled; a feature the rule cannot see is
not.** The demo contrasts the two cases:

```
    integral_0^1 x^(-1/2) dx = 1.999999999999999  (exact 2)   |error| = 6.66e-16
      an integrable endpoint singularity; QUADPACK extrapolates it
    integral_0^1 (spike of width 1e-4, exact 1.0):
      without points=  0.000000   reported abserr 0.00e+00   |error| 1.00e+00
      with    points=  1.000000   reported abserr 1.11e-14   |error| 1.10e-13
```

The $x^{-1/2}$ singularity is *algebraic and at an endpoint*, which is a case
QUADPACK's extrapolation was designed for: the answer is right to
$7\times10^{-16}$. The narrow spike is a different matter. It is a perfectly
ordinary function, but it is zero everywhere the rule samples, so the rule
returns **zero with a reported `abserr` of zero** — a confidently wrong
answer. Passing `points=[0.5, 0.5 + 1e-4]` forces a subdivision at the
feature and recovers the exact value to $1.1\times10^{-13}$.

The lesson generalises: **the algorithm samples where its own error estimator
says the error is, so structure it cannot see is structure it cannot
integrate.** For a gravity kernel with a discontinuity at a body boundary, for
a velocity model with a first-order interface, and for any measured profile
with a fault crossing it, `points=` is part of the problem statement.

## 4. The gravity anomaly of an arbitrary body

With the quadrature validated, the geophysical task is the vertical
attraction of a two-dimensional body of unlimited strike — the model behind
every profile gravity survey over a ridge, a dyke or a sediment-filled basin.
For a body with cross-section $S$ and density contrast $\Delta\rho$,

$$g_z(x_0) = 2G\Delta\rho \iint_S \frac{z}{(x-x_0)^2 + z^2}\,dx\,dz . \tag{1}$$

The double integral is reduced to a single one by integrating $z$ in closed
form. With $z_1(x)$ and $z_2(x)$ the lower and upper boundaries of the body at
abscissa $x$,

$$\int_{z_1}^{z_2} \frac{z\,dz}{(x-x_0)^2+z^2}
 = \tfrac12 \ln \frac{(x-x_0)^2 + z_2^2}{(x-x_0)^2 + z_1^2} , \tag{2}$$

so one adaptive quadrature over $x$ remains — and it is a quadrature over a
*smooth* integrand, which is precisely the case §2 says `quad` is good at.
The demo splits the $x$ range at every vertex abscissa so that no quadrature
interval straddles a corner of the polygon, where the derivative of
$z_1(x)$ or $z_2(x)$ jumps.

### 4.1 Validate the engine before using it

Two exact limits are available, and both are independent of the quadrature.

**The infinite slab.** A wide, thin body must approach
$g_z = 2\pi G\Delta\rho t$. The demo runs three half-widths and predicts that
the residual is the field of the two missing tails, which for a decay of the
integrand like $x^{-2}$ scales as $1/W$:

```
     half-width W (km)     gz (mGal)  exact (mGal)    relative
                   200     12.440613     12.580759    1.11e-02
                  2000     12.566743     12.580759    1.11e-03
                 20000     12.579358     12.580759    1.11e-04
```

The relative difference falls by exactly a factor of ten for each factor of
ten in $W$. That is not a coincidence and not a numerical artefact: it is the
$1/W$ tail of the neglected field, and the agreement between prediction and
measurement is what makes the quadrature trustworthy.

**The circular cross-section.** Outside a circular body of radius $R$ with its
axis at depth $z_c$, the field is exactly that of a line mass at the axis —
the two-dimensional analogue of the shell theorem:

$$g_z(x) = \frac{2G\pi R^2 \Delta\rho\, z_c}{x^2 + z_c^2} . \tag{3}$$

This is a *closed form*, and the same quadrature engine reproduces it to
$6\times10^{-16}$ at every station:

```
        x (km)   quadrature (mGal)  line mass (mGal)    relative
          -6.0         9.280887867       9.280887867    5.84e-16
           0.0        22.645366396      22.645366396    3.59e-16
           7.0         7.650461620       7.650461620    3.54e-16
```

The demo then replaces the circle by an inscribed $n$-gon and separates the
two errors that such a substitution creates:

```
           n   R_eff (m)  quadrature err  geometry err
          16      2961.5        1.84e-06      2.55e-02
          64      2997.6        3.33e-16      1.61e-03
         256      2999.8        8.88e-16      1.00e-04
        1024      3000.0        4.00e-15      6.27e-06
```

The quadrature error is at round-off in every row. The geometry error falls
as $n^{-2}$ — a factor of 4 per doubling of $n$ — which is the area deficit
$1 - \tfrac{n}{2}\sin(2\pi/n)/\pi$ of an inscribed polygon, and the numbers
$2.55\times10^{-2}, 1.61\times10^{-3}, 1.00\times10^{-4}, 6.27\times10^{-6}$
do fall by a factor of about 16 per factor of 4 in $n$. **This is the pattern
to look for whenever a model is replaced by a discretisation: separate the
error of the solver from the error of the model, because only the second one
is physics.**

### 4.2 The arbitrary body

The demo's body is a synthetic nine-vertex convex polygon with a 300 kg m⁻³
density contrast, 38.370 km² in cross-section and 1.0–6.4 km deep:

```
      x (km)     gz (mGal)
       -12.0        4.0803
        -9.0        7.5328
        -6.0       16.8315
        -3.0       30.3256
         0.0       33.0864
         3.0       22.9707
         6.0       11.1717
         9.0        5.6294
        12.0        3.3097
    maximum 33.0864 mGal at x = 0 km
```

Two independent checks follow. The same integral on a 601 × 601 grid with
Simpson's rule — a different algorithm sharing no code — agrees to
$1.2\times10^{-5}$ to $2.9\times10^{-5}$ relative, which is the grid's
resolution limit rather than the quadrature's. And the three-dimensional
analogue, integrating a uniform sphere over its volume in spherical polar
coordinates, reproduces the point-mass value:

```
    volume quadrature  gz = 94.355693 mGal
    point mass G*M/d^2    = 94.355693 mGal
    relative difference   = 1.15e-16
```

That last check is the shell theorem recovered numerically from a volume
integral, and it is the strongest single verification in this lesson: the
integrand has a singularity in the naive Cartesian formulation, the
coordinates are curved, the limits are finite and the answer is known.

## 5. `solve_ivp`: decay, chains and stiffness

`scipy.integrate.solve_ivp` solves $y' = f(t,y)$ from an initial state. It
takes a `method` argument that selects the algorithm family and a `t_eval`
array that does *not* affect the steps taken — an important distinction,
because the solver still chooses its own step sizes and interpolates to the
requested times.

### 5.1 Verified against the exponential

For a single decaying species with $\lambda = \ln 2/t_{1/2}$ and
$t_{1/2} = 10^9$ yr (a chosen input, not a literature value),

```
     t (t_half)         solve_ivp          analytic     |err|
            0.0    1.000000000000    1.000000000000  0.00e+00
            0.5    0.707106781181    0.707106781187  5.29e-12
            1.0    0.500000000007    0.500000000000  7.00e-12
            4.0    0.062500000004    0.062500000000  3.63e-12
    steps taken 95, function evaluations 566, max relative error 5.81e-11
```

The maximum relative error is $5.8\times10^{-11}$ for a requested
`rtol=1e-10`, so the tolerance is respected and the solver is not silently
lying. Note the shape of the error: it does not grow with time, because the
solver's step control keeps the *local* error per step at the tolerance and
the problem is smooth. For a stiff or chaotic problem that would not be true.

### 5.2 A conservation law as an independent check

Add a daughter species that receives everything the parent loses. In exact
arithmetic the sum is constant; numerically it is a check on the integration:

```
     t (t_half)        parent      daughter           sum         D/P
            0.0   1.000000000   0.000000000   1.000000000    0.000000
            1.0   0.500000000   0.500000000   1.000000000    1.000000
            4.0   0.062500000   0.937500000   1.000000000   15.000000
    The sum stays 1 to round-off, and D/P -> 1
```

The sum is $1.000000000$ at every output time — to nine decimals, which is
the printing precision — and $D/P = 1$ at one half-life. **Secular
equilibrium was not imposed; it emerged.** A conserved quantity that stays
conserved is the cheapest and strongest correctness check available for an
ODE solution, and it is worth finding one for every problem you solve.

### 5.3 Exponentially different errors on the same integral

The demo finishes with a **stiff** problem:
$y' = -1000(y-\cos t) - \sin t$ with exact solution $y=\cos t$. The solution
is as smooth as a cosine; the *equation* is stiff, which is a statement about
the rate of decay of perturbations, not about the answer:

```
    method     steps    nfev   njac     max |err|
    RK45        2197   13190      0      4.30e-09
    BDF           81     166      2      7.85e-09
    Radau         41     306      2      7.69e-09
```

All three reach the requested tolerance. `RK45` needs 13 190 function
evaluations against `BDF`'s 166 — a factor of 79 — because an explicit
method's step is limited by *stability*, not accuracy: it must resolve the
fast transient even though the solution does not contain it. `BDF` and
`Radau` form and factor a Jacobian (the `njac = 2` column) and take large
steps with it. `Radau` takes the fewest steps (41) at a higher cost per step
(306 evaluations against 166).

The rule this produces:

> If the solution is smooth and the function evaluations are cheap, use
> `RK45`. If the number of evaluations explodes as the problem gets stiffer —
> or if the step size collapses to a tiny fraction of the interval — the
> problem is stiff and you want `BDF` or `Radau`.

Note that you cannot detect stiffness from the answer. The demo's three
methods agree to $10^{-9}$; only the cost tells the story.

## Worked code

A complete, runnable version of §4 in twenty lines, showing the two-line
reduction that makes it cheap:

```python
import math
import numpy as np
from scipy import constants, integrate

G = constants.G

def gz_polygon(poly, rho, x0, eps=1e-12):
    """Vertical attraction of a 2-D polygon of unlimited strike (SI units)."""
    xs = sorted({p[0] for p in poly})

    def inner(x):
        zs = []
        for i in range(len(poly)):
            x1, z1 = poly[i]
            x2, z2 = poly[(i + 1) % len(poly)]
            if x1 != x2 and min(x1, x2) <= x <= max(x1, x2):
                zs.append(z1 + (x - x1) * (z2 - z1) / (x2 - x1))
        if len(zs) < 2:
            return 0.0
        z1, z2 = min(zs), max(zs)
        return 0.5 * math.log(((x - x0) ** 2 + z2 * z2)
                              / ((x - x0) ** 2 + z1 * z1))

    total = 0.0
    for lo, hi in zip(xs[:-1], xs[1:]):
        total += integrate.quad(inner, lo, hi, epsabs=eps, epsrel=eps)[0]
    return 2.0 * G * rho * total
```

and the ODE half of the lesson:

```python
lam = math.log(2.0) / (1.0e9 * 3.15576e7)      # s-1, t_half = 1e9 yr
sol = integrate.solve_ivp(lambda t, y: [-lam * y[0]],
                          (0.0, 4.0e9 * 3.15576e7), [1.0],
                          method="RK45", rtol=1e-10, atol=1e-14,
                          dense_output=True)
print(sol.nfev, sol.t.size)                    # cost, for the method discussion
print(sol.sol([0.0, 1.0e9 * 3.15576e7])[0])    # 1.0, 0.5
```

## Physical interpretation

Equation (1) is the statement that a gravity anomaly is the sum of the
contributions of every element of mass, with a $1/r^2$ weighting and a
geometric factor $z/r$ for the vertical component. Every gravity-forward
code you will meet is a version of it: a polygon formula (Talwani's line
integral), a prism formula (closed-form antiderivatives), or a numerical
quadrature like the one above. The polygon method is usually preferred
because it is exact for a polygon and much faster; the quadrature is worth
having because it works for a body whose boundary is not polygonal — an
ellipse, a density contour, a salt body digitised from a seismic section —
and because it makes the physics of the kernel visible.

The two validation cases are the two limits a geophysicist uses to sanity-
check any gravity model. The slab limit gives the amplitude scale: a 1 km
slab of 300 kg m⁻³ contrast produces 12.6 mGal, and that number should be
recoverable from any forward code on request. The circular limit is the
textbook target shape and tests the shape of the falloff.

The ODE half carries the module's thermal physics. The single-species decay
is the radiogenic heat production of a reservoir, and the daughter-chain
check is the secular-equilibrium principle that makes the present-day
heat-production inventory of the Earth computable from isotope ratios
(see [02-05-04](../../02-physics/05-thermodynamics/04-heat-conduction.md)
for the thermal context and
[12-global-geophysics-interior](../../12-global-geophysics-interior/README.md)
for the budget). The stiffness discussion is the same mathematics that
appears as the diffusion problem when it is discretised in space: an
explicit time step in a diffusion solver is limited by $\Delta t \le
\Delta x^2/(2\kappa)$, which is stiffness.

## Assumptions and limits

- **`quad` assumes the integrand is smooth between its sample points.** A
  discontinuity, a kink or a narrow feature must be declared with `points=`,
  or the answer will be wrong with a small reported error (§3).
- **`quad`'s `abserr` is a local error estimate of a rule comparison, not a
  bound.** A small `abserr` alongside a spike-shaped integrand is the
  counterexample the demo prints: `abserr = 0.00e+00` and a 100% error.
- **Adaptive quadrature needs a callable integrand.** For sampled data, use
  `simpson` or `trapezoid` and accept $n^{-4}$ or $n^{-2}$ convergence.
- **`solve_ivp` assumes the right-hand side is deterministic and Lipschitz.**
  It has no mechanism for a stochastic differential equation; for those, use
  a dedicated SDE solver.
- **`method='RK45'` is the default because it is robust, not because it is
  fast.** On a stiff problem it is slower by an order of magnitude and gives
  no warning (§5.3).
- **The polygon quadrature assumes constant density contrast and unlimited
  strike.** Real bodies are three-dimensional and heterogeneous; the 2-D
  model is an approximation whose error is set by the along-strike dimension.

## Python demonstration

[`code/integrate_demo.py`](./code/integrate_demo.py) contains all the output
quoted above. The parts worth modifying:

- Change the polygon in `body` to a non-convex one and watch the
  min/max intersection logic in `polygon_intersections` fail — this is the
  assumption of convexity, made explicit. A correct treatment of a
  non-convex cross-section needs the region to be decomposed into convex
  pieces or the boundary to be integrated directly.
- Change the requested `epsabs`/`epsrel` in `gz_profile` to `1e-6` and
  re-run the validation table: the quadrature error becomes comparable to the
  geometry error, and the two columns in the $n$-gon table stop being
  separable.
- Set `method="LSODA"` in the stiffness comparison. It switches between
  explicit and implicit automatically, which is why it is `odeint`'s default
  and why it often needs a hand-tuned `rtol` to be competitive.
- Raise `rtol` on the stiff problem from `1e-8` to `1e-3` and compare the
  `nfev` counts. The cost of an ODE solve is not monotone in the tolerance
  for any one method, but the *differences* between methods grow.

## Common mistakes

- **Reporting `quad`'s `abserr` as the accuracy of the integral.** It is an
  estimate, it can be zero when the answer is wrong, and it does not include
  the error in the model that produced the integrand.
- **Using `quad` on tabulated data.** `quad` needs a callable; interpolating
  the data and then integrating the interpolant hides the interpolation error
  inside the integral.
- **Forgetting that `t_eval` does not control the steps.** A spotless table of
  output values can hide a solver that took $10^5$ internal steps, and the
  `nfev` count is where that shows.
- **Assuming a stiff problem announces itself.** It does not: the solution is
  smooth, the answer is right, and only the cost is wrong.
- **Comparing a numerical answer to a published number instead of to a
  derivation.** The point of §4.1 is that the reference must be
  *independent* — a formula, not another code.
- **Confusing the discretisation error with the solver error.** In the
  $n$-gon table the quadrature error is $10^{-16}$ and the geometry error is
  $10^{-2}$; reporting the former as the latter's accuracy is a category
  error.

## Real-world applications

- **Gravity and magnetic modelling.** Every 2-D forward modelling package
  contains a polygon or prism routine derived from equation (1); the
  quadrature here is the fallback for irregular boundaries and the reference
  against which such a routine is tested.
- **Potential-field inversion.** The forward operator is an integral over the
  subsurface; the inverse problem multiplies that operator by its transpose,
  so the accuracy and the cost of the quadrature set the resolution of the
  recovered model.
- **Heat-flow and thermal history.** Radioactive decay chains, magma cooling
  and borehole temperature histories are all initial-value problems; the
  conservation check of §5.2 is the standard verification in each.
- **Radiocarbon and isotope dating.** The same first-order decay with a
  measured half-life; the error in the age is dominated by the half-life
  uncertainty, not by the solver.
- **Reservoir and hydrological modelling.** A reservoir's pressure and
  temperature evolution is a stiff system, and the choice between an explicit
  and an implicit scheme is exactly the choice measured in §5.3.
- **Orbit propagation.** Where the ODE is smooth and the tolerances are
  tight, `RK45` with `rtol=1e-12` is standard practice, and `DOP853` (in
  `solve_ivp`) is the higher-order member of the same family.

## Further reading

- **Press, W. H., Teukolsky, S. A., Vetterling, W. T., & Flannery, B. P.
  *Numerical Recipes: The Art of Scientific Computing* (3rd ed., Cambridge
  University Press, 2007).** Chapter 4 covers quadrature and the
  Gauss–Kronrod idea, and Chapter 17 covers stiff ODEs and the BDF family;
  the book is the standard source for *why* the routines are shaped the way
  they are. Level: intermediate to advanced.
- **Heath, M. T. *Scientific Computing: An Introductory Survey* (2nd ed.,
  SIAM, 2018).** The clearest treatment of error control in quadrature and in
  initial-value problems, with the convergence orders derived rather than
  tabulated. Level: intermediate.
- **Blakely, R. J. *Potential Theory in Gravity and Magnetic Applications*
  (Cambridge University Press, 1995).** The geophysical setting of §3 and §4,
  including the prism and polygon formulas. Level: graduate.
- **Telford, W. M., Geldart, L. P., & Sheriff, R. E. *Applied Geophysics*
  (2nd ed., Cambridge University Press, 1990).** The anomaly shapes of §4.2
  in the context of a real survey. Level: intermediate.
- **Hairer, E., & Wanner, G. *Solving Ordinary Differential Equations II:
  Stiff and Differential-Algebraic Problems* (2nd ed., Springer, 1996).** The
  definitive account of what stiffness is and how the implicit methods
  handle it. Level: doctoral.
- **Turcotte, D. L., & Schubert, G. *Geodynamics* (3rd ed., Cambridge
  University Press, 2014).** The thermal and geodynamic problems whose
  solutions are the ODEs of §5. Level: graduate.

> Note on citations: bibliographic details are given so that you can locate
> the works. This repository does not host or reproduce copyrighted text;
> confirm editions and availability through your library before citing them
> yourself.

## Related lessons

- [01 SciPy Organisation and When to Use Which Subpackage](./01-scipy-overview.md)
  — where `quad` sits in the subpackage map.
- [03 scipy.optimize](./03-optimize.md) — the inverse of integration in the
  sense that matters here: finding the parameters that best explain data.
- [06 scipy.sparse](./06-sparse.md) §5 — what an implicit stiff step becomes
  when the ODE is a discretised partial differential equation.
- [07 scipy.ndimage and scipy.linalg](./07-ndimage-linalg.md) — the spatial
  side of potential-field modelling.
- [01-12-04 Numerical Integration](../../01-mathematics/12-numerical-methods/04-numerical-integration.md)
  — the same rules derived from Taylor series rather than called.
- [01-05-06 Improper Integrals](../../01-mathematics/05-single-variable-calculus/06-improper-integrals.md)
  — what the infinite limits of §3 mean.
- [02-05-04 Heat Conduction, Fourier's Law and Thermal Diffusivity](../../02-physics/05-thermodynamics/04-heat-conduction.md)
  — the diffusion problem whose finite-difference solution is verified in the
  same spirit as §4.1.

Exercises:
[`exercises/02-integrate-exercises.md`](./exercises/02-integrate-exercises.md)
and
[`exercises/02-integrate-solutions.md`](./exercises/02-integrate-solutions.md).

## Self-assessment checklist

- [ ] I can state what `quad`'s algorithm is and where its error estimate
      comes from. (§1)
- [ ] I can predict the convergence order of the trapezoid and Simpson rules
      and read it off a table. (§2)
- [ ] I can integrate over an infinite limit without truncating. (§3)
- [ ] I can recognise an integrand whose structure requires `points=`, and
      explain the confidently wrong answer that appears without it. (§3)
- [ ] I can reduce a double integral to a single one by integrating in closed
      form. (§4)
- [ ] I can validate a gravity routine against the infinite-slab and
      line-mass limits. (§4.1)
- [ ] I can separate a quadrature error from a geometry error in a
      discretisation study. (§4.1)
- [ ] I can verify an ODE solution against its analytic form and against a
      conservation law. (§5.1, §5.2)
- [ ] I can detect stiffness from cost rather than from the solution. (§5.3)
- [ ] I can say what `abserr` is not, and give the counterexample that proves
      it. (§1, §3)
