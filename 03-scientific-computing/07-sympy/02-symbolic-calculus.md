---
id: 03-07-02
title: "Symbolic Differentiation, Integration and Limits"
level: intermediate
prereqs: ["03-07-01"]
estimated_minutes: 90
tags: [sympy, calculus, differentiation, integration, limits, potential-fields]
---

# Symbolic Differentiation, Integration and Limits

Most of the analysis in this curriculum reduces to three operations: take a
derivative, take an integral, take a limit. Done numerically, each one carries a
step size or a tolerance that has to be defended, and each one fails in a
characteristic regime — cancellation for differences, endpoint singularities for
quadrature, and complete loss of significance for a limit. Done symbolically,
all three are exact and none of those regimes exists.

This lesson develops the three operations on geophysical problems where the
answer is already known independently, so that every symbolic result is checked
against something: Laplace's equation, a closed-form geotherm, a standard
integral, a finite-difference estimate. The verifications are the point.

```bash
.venv/bin/python 03-scientific-computing/07-sympy/code/symbolic_calculus_demo.py
```

## Learning objectives

By the end of this lesson you will be able to:

1. **Differentiate** a scalar field in Cartesian coordinates and **verify**
   Laplace's equation by simplifying it to zero.
2. **Integrate** a body's contribution to a potential shell by shell and **check**
   the result at the boundary.
3. **Find** the stationary points of a wavelet analytically and **compare** them
   with a grid search, quoting both.
4. **Evaluate** definite integrals symbolically and **compare** them with adaptive
   quadrature, including a case where the two disagree.
5. **Compute** a limit symbolically and **explain**, with measured numbers, the
   floating-point failure the symbol avoids.
6. **Turn** a derivative into a physical flux with units, and **verify** the
   closed form.

## Prerequisites

- [03-07-01 Symbolic Variables, Expressions and Assumptions](./01-symbolic-basics.md)
  — symbols, assumptions and exact arithmetic.
- [01-05-05 Integration](../../01-mathematics/05-single-variable-calculus/05-integration.md)
  — what a definite integral is, and the techniques this lesson automates.

## 1. Intuition: a derivative is a rule, not a difference

The finite difference is an *approximation* of the derivative:

$$f'(x) \approx \frac{f(x+h) - f(x-h)}{2h}, \qquad \text{error} =
\frac{h^2}{6}f'''(x) + O(h^4),$$

and the error has two terms fighting each other: the truncation term falls as
$h^2$, while the round-off term *grows* as $\epsilon/h$ because the two function
values approach each other. There is therefore an optimal $h$, and it depends on
the machine. The demonstration measures this whole trade:

```
  analytic dT/dz at z = 0.05 m: -2.675469439489e+01 K/m
       h (m)   central difference (K/m)   relative error
       2e-02        -2.673466118340e+01        7.488e-04
       5e-03        -2.675344152799e+01        4.683e-05
       1e-03        -2.675464427818e+01        1.873e-06
       2e-04        -2.675469239021e+01        7.493e-08
       5e-05        -2.675469426960e+01        4.683e-09
       1e-05        -2.675469438991e+01        1.861e-10
       1e-06        -2.675469439506e+01        6.493e-12
       1e-07        -2.675469438884e+01        2.259e-10
       1e-08        -2.675469437108e+01        8.898e-10
  best h in the scan: 1e-06 m, relative error 6.493e-12
```

Read the two regimes: from $h = 2\times10^{-2}$ to $h = 10^{-6}$ the error falls
by a factor of $1.15\times10^{8}$, i.e. almost exactly as $h^{2}$
($(2\times10^{-2}/10^{-6})^2 = 4\times10^{8}$; the factor-of-four shortfall is
because the leading truncation term is not exactly $h^2$ over this range), and
then it *rises* again. The symbolic derivative has no $h$ at all: the answer is
exact, and the only error is in representing it as a float.

## 2. Precise definitions

**Partial derivative.** `sp.diff(expr, x)` differentiates an expression with
respect to a symbol, treating others as constants.

**Definite integral.** `sp.integrate(expr, (x, a, b))` returns the exact value
when a closed form exists, or an unevaluated `Integral` when it does not.

**Improper integral.** A definite integral with an infinite or singular limit.
SymPy handles many of them, e.g. `sp.integrate(sp.exp(-u**2), (u, 0, sp.oo))`.

**Limit.** `sp.limit(expr, x, 0)` computes the limiting value, with
`dir="+"` or `"-"` for one-sided limits.

**Series.** `sp.series(expr, x, x0, n)` returns a truncated expansion with an
order term; `.removeO()` drops the term for further algebra.

## 3. Derivation: the potential of a point mass, and Laplace's equation

For a point mass the potential is $V = -GM/r$. In Cartesian coordinates with
$r = \sqrt{x^2+y^2+z^2}$, the gradient components follow by the chain rule. The
demonstration computes them symbolically and simplifies:

```
  V(r) = - \frac{G M}{r}
  gradient components:
      dV/dx = \frac{G M x}{\left(x^{2} + y^{2} + z^{2}\right)^{\frac{3}{2}}}
      dV/dy = \frac{G M y}{\left(x^{2} + y^{2} + z^{2}\right)^{\frac{3}{2}}}
      dV/dz = \frac{G M z}{\left(x^{2} + y^{2} + z^{2}\right)^{\frac{3}{2}}}
  |grad V| = \frac{G M}{x^{2} + y^{2} + z^{2}}
  |grad V| - GM/(x^2+y^2+z^2) simplifies to: 0
  Laplacian of V, symbolic: 0
```

Two verifications with exact residuals:

$$\left|\nabla V\right| - \frac{GM}{r^2} = 0, \qquad \nabla^2 V =
\sum_{i}\frac{\partial^2 V}{\partial x_i^2} = 0 \quad (r > 0).$$

The second is Laplace's equation, and the qualification $r>0$ is the interesting
part: the expression's domain *excludes the source*, and outside it the field is
harmonic. Symbolic simplification returning exactly 0 is a different statement
from a numerical Laplacian being small — the first says the equation holds for
every point in the domain, the second says it held at one point to one precision.

### 3.1 Inside a uniform sphere, by integration

The potential inside a body is built from shells. For a shell of radius $s$ and
mass $4\pi\rho s^2\,ds$:

- for $s < r$ the shell acts as a point mass at the centre, contributing
  $-G\,(4\pi\rho s^2 ds)/r$;
- for $s > r$ the shell contributes nothing to the field, but adds
  $-G\,(4\pi\rho s^2 ds)/s$ to the potential.

So

$$V(r) = -G\int_0^r \frac{4\pi\rho s^2}{r}\,ds
- G\int_r^R \frac{4\pi\rho s^2}{s}\,ds,$$

and the demonstration evaluates this pair of integrals symbolically:

```
  V(r) for r <= R = \frac{2 \pi G \rho \left(- 3 R^{2} + r^{2}\right)}{3}
  g(r) = -dV/dr   = - \frac{4 \pi G r \rho}{3}
  g(R) + GM/R^2 with M = (4/3)pi rho R^3: 0
  V(R) = -4*pi*G*R**2*rho/3
  and V(R) + GM/R = 0, i.e. the interior solution matches -GM/R at the surface
```

Two exact checks, both zero:

$$g(R) = -\frac{4\pi G \rho R}{3} = -\frac{GM}{R^2}, \qquad
V(R) = -\frac{4\pi G \rho R^2}{3} = -\frac{GM}{R}.$$

The interior field is linear in $r$ — a result that follows from two integrals and
a division, with no chance of a dropped $\frac43$.

### 3.2 A note on the sign of the flux

$g = -\mathrm{d}V/\mathrm{d}r$ gives a *negative* value inside the sphere, because
$g$ here is the radial component of the attraction, directed inward. The
demonstration measures `g(R) + GM/R^2 = 0`, i.e. $g(R) = -GM/R^2$. Keeping the
sign convention explicit in the print statement is worth the line: sign errors in
potential-field work are otherwise found by their consequences.

## 4. Stationary points: the Ricker wavelet

The Ricker wavelet is the standard seismic source wavelet,

$$w(t) = \left(1 - 2\pi^2 f^2 t^2\right)e^{-\pi^2 f^2 t^2},$$

with peak frequency $f$. The demonstration differentiates it and solves for the
stationary points:

```
  w(t)  = \left(- 2 \pi^{2} f^{2} t^{2} + 1\right) e^{- \pi^{2} f^{2} t^{2}}
  w'(t) = \left(4 \pi^{4} f^{4} t^{3} - 6 \pi^{2} f^{2} t\right) e^{- \pi^{2} f^{2} t^{2}}
  stationary points: [0, -sqrt(6)/(2*pi*f), sqrt(6)/(2*pi*f)]
      t = 0  ->  w = 1 = 1.0000000
      t = -sqrt(6)/(2*pi*f)  ->  w = -2*exp(-3/2) = -0.44626032
      t = sqrt(6)/(2*pi*f)  ->  w = -2*exp(-3/2) = -0.44626032
  trough time for f = 32 Hz: \frac{\sqrt{6}}{2 \pi f} = 0.01218276 s
```

The exact side-lobe amplitude is

$$w\!\left(\pm\frac{\sqrt{6}}{2\pi f}\right) = -2e^{-3/2} = -0.44626032,$$

which is a number you can put in a methods section: the Ricker's first side lobe
is 44.63 % of its peak, inverting the phase.

Against that, a grid search:

```
  grid spacing: 1.0e-07 s; minimum found on the grid at t = -0.0121828 s
  exact trough at t = -0.0121828 s; |difference| = 3.75e-08 s (0.37 grid steps)
```

The grid search recovered the trough to 0.37 of a grid step, which is as good as
that grid can be. The symbol has no step. **Use the grid to check the symbol; do
not use the grid to replace it.**

## 5. Quadrature: symbolic against adaptive

```
  Gaussian tail (0, inf)   exact = sqrt(pi)/2 = 0.886226925452758
                           quad  = 0.886226925452758   |difference| = 1.110e-16
  arctan integral (0, 1)   exact = pi/4 = 0.785398163397448
                           quad  = 0.785398163397448   |difference| = 0.000e+00
  Beta(3/2, 5/2) (0, 1)    exact = pi/16 = 0.196349540849362
                           quad  = 0.196349540835266   |difference| = 1.410e-11
```

The first two agree to the last bits. The third does not, and the reason is
instructive: the integrand $\sqrt{u}(1-u)^{3/2}$ has a derivative that is
singular at both endpoints, so quad's default absolute tolerance is never
reached, and it returns its best effort. **A quadrature's error estimate is a
statement about the integrand's smoothness**, and an integrand with a
square-root endpoint is not smooth. SymPy's answer is exact:

$$\int_0^1 u^{1/2}(1-u)^{3/2}\,du = B\!\left(\tfrac32, \tfrac52\right)
= \frac{\Gamma(3/2)\Gamma(5/2)}{\Gamma(4)} = \frac{\pi}{16}.$$

Both tools are needed and neither is redundant: the symbol gives the closed form
that can be differentiated and printed; quadrature gives an answer where no
closed form exists.

## 6. Limits, and the failure the symbol never has

$$\lim_{u\to 0}\frac{1-\cos u}{u^2} = \frac12,$$

and the series form is

$$\frac{1-\cos u}{u^2} = \frac12 - \frac{u^2}{24} + O(u^4).$$

The demonstration evaluates the naive float expression at three arguments:

```
  lim_(u->0) (1 - cos u)/u^2 = 1/2
  series form of the same ratio: 1/2 - u**2/24 + O(u^4)
      float evaluation at u = 1e-03: 0.499999958325503   relative error vs 1/2 = 8.335e-08
      float evaluation at u = 1e-05: 0.500000041370185   relative error vs 1/2 = 8.274e-08
      float evaluation at u = 1e-08: 0.000000000000000   relative error vs 1/2 = 1.000e+00
  cos(1e-8) in binary64: np.float64(1.0)  (so 1 - cos(1e-8) is exactly 0.0)
```

At $u = 10^{-8}$ the numerator is exactly zero because $\cos u$ rounds to
$1.0$: the ratio returns 0 and the relative error is 1.0, i.e. total. The
error at $u = 10^{-3}$ and $10^{-5}$ is flat at $\sim8\times10^{-8}$, which is
the *rounding* error of the subtraction, not the truncation error of the series
— consistent with the general expectation that the error of this evaluation
behaves like $\epsilon/u^2$ until it saturates.

The lesson generalises: **wherever a formula subtracts two nearly equal
quantities, the symbolic form is the fix, not more precision.** Rewriting
$1-\cos u$ as $2\sin^2(u/2)$ removes the cancellation entirely, at any precision.

## 7. A derivative with units: heat flux

The temperature of a half-space whose surface is suddenly changed by $\Delta T$
is

$$T(z,t) = T_0 + \Delta T\,\mathrm{erfc}\!\left(\frac{z}{2\sqrt{\kappa t}}\right),$$

and the flux is $q = -k\,\partial T/\partial z$. Differentiating symbolically:

$$\frac{\partial T}{\partial z} = -\frac{\Delta T}{\sqrt{\pi\kappa t}}
\exp\!\left(-\frac{z^2}{4\kappa t}\right).$$

The demonstration verifies the closed form (the difference simplifies to exactly
0) and evaluates a diurnal case:

```
  parameters: k = 1.0 W/m/K, kappa = 1.0e-06 m^2/s, dT = 10.0 K, z = 0.05 m, t = 43200 s (12 h)
      z/(2 sqrt(kappa t)) = 0.120281 (dimensionless similarity variable)
      T - T0              = +8.649288 K
      dT/dz               = -26.754694 K m^-1
      q = -k dT/dz        = +26.754694 W m^-2
```

Dimensional checks, both of which the code satisfies by construction:

$$\left[\frac{z}{2\sqrt{\kappa t}}\right] =
\frac{\mathrm{m}}{\sqrt{\mathrm{m^2\,s^{-1}}\cdot \mathrm{s}}} = 1
\quad\text{(dimensionless)},$$

$$[q] = \mathrm{W\,m^{-1}\,K^{-1}}\cdot\mathrm{K\,m^{-1}} =
\mathrm{W\,m^{-2}}.$$

A flux of 27 W/m² into the ground over a 12-hour cycle, driven by a 10 K surface
amplitude, is the right order for dry soil. **The dimensional analysis is not a
formality here**: it is what tells you the similarity variable is dimensionless,
which is the statement that the solution depends on $z$ and $t$ only through their
combination.

## 8. Series: a statement about a limit, with a measured range

```
  exact   : \frac{1}{\left(\epsilon^{2} + 1\right)^{\frac{3}{2}}}
  series  : \frac{15 \epsilon^{4}}{8} - \frac{3 \epsilon^{2}}{2} + 1
  operation count: exact 5, series 8
      eps = 0.05: exact 0.9962616847, truncated 0.9962617187, relative error 3.421e-08
      eps =  0.1: exact 0.9851853368, truncated 0.9851875000, relative error 2.196e-06
      eps =  0.3: exact 0.8787397112, truncated 0.8801875000, relative error 1.648e-03
      eps =  0.5: exact 0.7155417528, truncated 0.7421875000, relative error 3.724e-02
  worst relative error over the four test values: 3.724e-02
```

The truncated series is *longer* to evaluate than the closed form (8 operations
against 5) and is only useful where $\epsilon$ is small. The error grows as the
first omitted term, here $\epsilon^6$: from $\epsilon=0.05$ to $\epsilon=0.1$ it
grows by a factor of 64.2 against the predicted $2^6 = 64$.

That is the honest way to use an expansion: derive it symbolically, then **measure
the range over which it is good enough for the purpose**, and state the range.

## 9. Assumptions and limitations

- **SymPy's `integrate` is not guaranteed to terminate** on a hard integral. If it
  hangs, restructure the problem or integrate numerically.
- **The symbol cannot know the physics.** A closed form is exact for the model;
  whether the model is right is not a symbolic question.
- **`erfc` underflows.** At $z/(2\sqrt{\kappa t}) = 50$ the temperature contrast is
  below the smallest normal double; the demonstration's earlier draft used
  parameters that put the argument at 50 and produced a Gaussian underflow, which
  is why the final parameters are a shallow diurnal case. Choose parameters in
  the range where the physics is resolvable.
- **Series order is a choice.** `sp.series(..., n)` truncates; whether the
  remainder is negligible is a measurement, as in Section 8.
- **No timing statements.** The lesson quotes the number of grid points, the
  number of quadrature calls' tolerances, and operation counts — never run times.

## 10. Worked examples

### 10.1 The gravity gradient tensor of a point mass, symbolically

The nine components $\partial^2 V/\partial x_i \partial x_j$ follow from two
differentiations:

$$\frac{\partial^2 V}{\partial x_i \partial x_j} = GM\left(
\frac{\delta_{ij}}{r^{3}} - \frac{3x_i x_j}{r^{5}}\right),$$

and SymPy returns exactly that form. Two contractions are worth computing, and I
checked both symbolically rather than by hand:

$$\sum_i \frac{\partial^2 V}{\partial x_i^2} = GM\left(\frac{3}{r^3} -
\frac{3r^2}{r^5}\right) = 0 \qquad \text{(Laplace's equation)},$$

$$\sum_{i,j}\frac{\partial^2 V}{\partial x_i\partial x_j}x_i x_j
= GM\left(\frac{r^2}{r^3} - \frac{3r^4}{r^5}\right) = -\frac{2GM}{r}.$$

The first is the tracelessness of the tensor; the second says the *radial*
second derivative is $-2GM/r^3$, which is the quantity measured by a
gravitational gradiometer. The demonstration's verification for a single
component is `H_zz = GM(x^2 + y^2 - 2z^2)/r^5`, which is what a hand
differentiation has to reproduce, and the trace check is two lines of code
instead of a page of algebra.

### 10.2 Why the flux sign is worth checking symbolically

The demonstration's flux is *positive* for a *positive* surface temperature
change: heat flows into the ground. A sign error in the definition of $q$ or in
the direction of $z$ flips it. Symbolic verification cannot detect which
convention you intended, so the check is: evaluate at a known point and compare
with the physical expectation, which is what the parameters in Section 7 do.

## 11. Python demonstration

`code/symbolic_calculus_demo.py` runs in eight parts:

| Part | Establishes | Key measured output |
|---|---|---|
| 1 | Gradient, magnitude, Laplacian | residual `0`, Laplacian `0` |
| 2 | Interior potential by integration | `g(R) + GM/R^2: 0` |
| 3 | Ricker extrema | trough at `0.01218276 s` for $f=32$ Hz; side lobe $-2e^{-3/2}$ |
| 4 | Quadrature against `quad` | `1.110e-16`, `0.000e+00`, `1.410e-11` |
| 5 | Limits and cancellation | relative error `8.3e-08` then `1.000e+00` |
| 6 | Flux from a derivative | `q = +26.754694 W m^-2` |
| 7 | Series truncation | worst relative error `3.724e-02` at $\epsilon = 0.5$ |
| 8 | Finite differences | best $h = 10^{-6}$ m, relative error `6.493e-12` |

Part 8 is the bridge back to numerical work: the symbolic derivative is the
reference against which a difference scheme is judged, and the measurement shows
the $h^2$ regime and the round-off wall in one table.

## 12. Exercises

Solutions are in
[`exercises/02-symbolic-calculus-solutions.md`](./exercises/02-symbolic-calculus-solutions.md).

### ★ Foundational

**★1.** Differentiate with respect to $x$: (a) $3x^4 - 2x$,
(b) $\sin(kx)e^{-ax}$, (c) $\ln(x^2+a^2)$, (d) $\mathrm{erf}(x/2)$.

**★2.** Evaluate: (a) $\int_0^{1} x^2\,dx$,
(b) $\int_0^{\infty} x e^{-x}\,dx$, (c) $\int_0^{\pi}\sin^2\theta\,d\theta$.

**★3.** Compute $\lim_{x\to0}\frac{\sin x}{x}$ and
$\lim_{x\to0}\frac{e^x-1-x}{x^2}$, symbolically and by series.

**★4.** State the two error terms in a central difference and which way each
scales with $h$.

### ★★ Applied

**★★5.** Derive symbolically the depth at which the vertical attraction of a
point mass at depth $d$ beneath the surface has its maximum horizontal gradient,
and evaluate it for $d = 1000$ m. Report the exact expression and the value.

**★★6.** Verify by symbolic differentiation that the flux
$q(z,t) = k\Delta T\,e^{-z^2/(4\kappa t)}/\sqrt{\pi\kappa t}$ satisfies the heat
equation $\partial T/\partial t = \kappa\,\partial^2 T/\partial z^2$ for the
temperature of Section 7. Report the residual.

**★★7.** Compute $\int_0^1 \frac{dx}{1+x^2}$ symbolically and by
`scipy.integrate.quad`. Report both values, the exact difference as a float, and
which of the two you would quote with a tolerance and why.

**★★8.** Reproduce the Ricker side-lobe ratio. Derive $w$ at its extrema, evaluate
the ratio to the peak, and report it to four significant figures as a fraction
and in decibels.

### ★★★ Research-oriented

**★★★9.** Build the gravitational attraction of a vertical cylinder of radius
$a$, depth range $[z_1, z_2]$ and density $\rho$, by integrating the point-mass
kernel over the cross-section symbolically (in cylindrical coordinates). Verify
the result against a numerical double integral for three geometries, report the
relative differences, and state which of the two routes you would use for a
survey of 10 000 stations and why.

**★★★10.** Quantify the finite-difference optimum. For the diffusion gradient of
Section 7, map the relative error of the central difference over $h$ from
$10^{-1}$ to $10^{-9}$ m, report the empirical exponent of the truncation regime,
the minimum error and the $h$ at which it occurs, and compare the measured
minimum with the classical estimate $h_{\text{opt}} \approx (\epsilon\,
|f|/|f'''|)^{1/3}$ using your measured derivative values. State where the
comparison fails and why.

## 13. Common mistakes

1. **Using a finite difference where a symbolic derivative is available.** The
   step size is a new free parameter with no physical meaning.
2. **Trusting a quadrature on a non-smooth integrand.** Check the endpoint
   behaviour.
3. **Taking a limit numerically.** At $u = 10^{-8}$ the measured relative error is
   total.
4. **Assuming `integrate` always works.** Restructure when it does not.
5. **Forgetting that a series has a range.** Measure the error, do not assume it.
6. **Dropping the domain.** Laplace's equation holds for $r>0$; the exclusion is
   part of the result.
7. **Losing the sign convention.** State it in the cell that prints the number.

## 14. Real-world applications

- **Potential-field modelling.** Gradients, second derivatives and upward
  continuation are all derivatives; deriving them symbolically removes the step
  size from the error budget.
- **Thermal and hydrological problems.** The `erfc` family produces closed-form
  fluxes, whose derivatives are exact and whose units are checkable.
- **Seismic source wavelets.** Analytic extrema and side-lobe ratios are the
  quantities quoted in methods sections.
- **Error propagation.** Symbolic partial derivatives give the sensitivity
  coefficients an error budget needs.
- **Model comparison.** Subtracting two approximations symbolically gives their
  exact difference, which is the honest way to say what one adds over the other.

## 15. Further reading

- **SymPy documentation** (sympy.org). Level: intermediate. The calculus
  sections: `diff`, `integrate`, `limit`, `series`, including the `Integral` form
  returned when no closed form exists.
- **scipy.integrate documentation** (scipy.org). Level: intermediate. `quad`,
  `dblquad` and the meaning of `epsabs` and `epsrel`, which Section 5 relies on.
- **Abramowitz, M. & Stegun, I. A. (1964). *Handbook of Mathematical Functions*.**
  Level: reference. The `erf`/`erfc` family and the Beta function used above.
- **Carslaw, H. S. & Jaeger, J. C. (1959). *Conduction of Heat in Solids* (2nd
  ed.). Oxford University Press.** Level: advanced. The half-space solution of
  Section 7, derived rather than quoted.
- **Trefethen, L. N. & Bau, D. (1997). *Numerical Linear Algebra*. SIAM.**
  Lecture 1. Level: advanced. A short, sharp account of the finite-difference
  trade-off measured in Section 1.

> Note on citations: bibliographic details are given so you can locate the works.
> This repository does not host or reproduce copyrighted text.

## 16. Related lessons

- [01 Symbolic Variables, Expressions and Assumptions](./01-symbolic-basics.md)
- [03 Symbolic Solvers for Algebraic and Differential Equations](./03-solving-equations.md)
- [04 Symbolic Tensors and Index Notation](./04-tensor-symbolic.md)
- [05 Generating Fast Numerical Code from Symbolic Results](./05-code-generation.md)
- [03-03-02 scipy.integrate: Quadrature and ODE Integration](../03-scipy/02-integrate.md)
  — the numerical counterpart of Section 5.

## 17. Self-assessment checklist

- [ ] I can differentiate a field in Cartesian coordinates and verify Laplace's
      equation by simplification. (§3)
- [ ] I can integrate a body's potential shell by shell and check the boundary
      value. (§3.1)
- [ ] I can find a wavelet's extrema exactly and quote the side-lobe ratio. (§4)
- [ ] I can explain why `quad` falls short on a square-root endpoint. (§5)
- [ ] I can state the argument range where a naive float limit fails. (§6)
- [ ] I can turn a symbolic derivative into a flux with units. (§7)
- [ ] I can measure the range over which a truncated series is usable. (§8)
- [ ] I know when to stop increasing a finite-difference precision. (§1)
