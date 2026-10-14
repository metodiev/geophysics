---
id: 26-03-01
title: "Formula Sheet: Mathematics and Calculus"
level: intermediate
prereqs: []
estimated_minutes: 30
tags: [reference, formulas, mathematics]
---

# Formula Sheet: Mathematics and Calculus

The mathematics used by the rest of the curriculum, compressed into tables with
the conditions attached. Every entry states where it is valid; a formula without
its assumptions is a trap.

## How to use this page

Look up the identity, the rule, or the error term. Conditions are given in the
same row as the formula, because most mistakes in geophysical mathematics are
conditions that were silently dropped. Numbers quoted in the worked example come
from `code/formulas_mathematics_demo.py`, which is print-only and exits 0.

*Provenance:* no measured data appear on this page. The worked example is
**SYNTHETIC** — it is computed from the formulas themselves.

## 1. Algebra, series and asymptotics

| Formula | Conditions |
|---|---|
| $(a+b)^n = \sum_{k=0}^{n}\binom{n}{k}a^{n-k}b^k$ | integer $n \ge 0$ |
| $\dfrac{1}{1-x} = \sum_{k=0}^{\infty}x^{k}$ | $\lvert x \rvert < 1$ |
| $e^{x} = \sum_{k=0}^{\infty}\dfrac{x^{k}}{k!}$ | all $x$; converges for every $x$ |
| $\ln(1+x) = \sum_{k=1}^{\infty}(-1)^{k+1}\dfrac{x^{k}}{k}$ | $-1 < x \le 1$ |
| $\sin x = \sum_{k=0}^{\infty}(-1)^{k}\dfrac{x^{2k+1}}{(2k+1)!}$ | all $x$ |
| $\cos x = \sum_{k=0}^{\infty}(-1)^{k}\dfrac{x^{2k}}{(2k)!}$ | all $x$ |
| $e^{i\theta} = \cos\theta + i\sin\theta$ | Euler; all $\theta$ |
| $\lvert e^{i\theta}\rvert = 1$ | the identity behind phasor notation |
| $a^{3} \pm b^{3} = (a \pm b)(a^{2} \mp ab + b^{2})$ | all $a$, $b$ |
| $\sum_{k=1}^{n} k = \dfrac{n(n+1)}{2}$, $\sum_{k=1}^{n}k^{2} = \dfrac{n(n+1)(2n+1)}{6}$ | integer $n \ge 1$ |
| Geometric sum $\sum_{k=0}^{n-1} r^{k} = \dfrac{1-r^{n}}{1-r}$ | $r \ne 1$ |

**Convergence is part of the formula.** The Taylor series for $e^{x}$ converges
everywhere, but the series for $\ln(1+x)$ diverges for $x > 1$; using it there
gives a wrong answer that looks like a numerical problem.

## 2. Differentiation

| Formula | Conditions |
|---|---|
| $(fg)' = f'g + fg'$ | product rule |
| $\left(\dfrac{f}{g}\right)' = \dfrac{f'g - fg'}{g^{2}}$ | $g \ne 0$ |
| $\dfrac{d}{dx}f(g(x)) = f'(g(x))\,g'(x)$ | chain rule |
| $\dfrac{d}{dx}\ln x = \dfrac{1}{x}$ | $x > 0$ |
| $\dfrac{d}{dx}e^{ax} = a\,e^{ax}$ | all $a$, $x$ |
| $\dfrac{d}{dx}\sin(ax) = a\cos(ax)$ | all $a$, $x$ |
| $\dfrac{d}{dx}\tanh x = \operatorname{sech}^{2}x$ | all $x$ |
| $\dfrac{d}{dx}\arctan x = \dfrac{1}{1+x^{2}}$ | all $x$ |
| $\dfrac{d}{dx}\operatorname{erf}(x) = \dfrac{2}{\sqrt{\pi}}e^{-x^{2}}$ | the Gaussian normalisation |
| $\dfrac{\partial}{\partial x}\bigl\lvert \mathbf{r}\bigr\rvert = \dfrac{x}{\lvert \mathbf{r}\rvert}$ | $\lvert \mathbf{r}\rvert \ne 0$; used for every point-source kernel |

## 3. Taylor expansion and numerical derivatives

For $f$ with $n+1$ continuous derivatives on an interval containing $a$:

$$f(a+h) = f(a) + h f'(a) + \frac{h^{2}}{2}f''(a) + \cdots + \frac{h^{n}}{n!}f^{(n)}(a) + R_{n}$$

with $R_{n} = \dfrac{h^{n+1}}{(n+1)!}f^{(n+1)}(\xi)$ for some $\xi$ between $a$
and $a+h$.

| Approximation | Error order | Practical note |
|---|---|---|
| $f'(a) \approx [f(a+h) - f(a)]/h$ | $O(h)$ | forward difference |
| $f'(a) \approx [f(a+h) - f(a-h)]/(2h)$ | $O(h^{2})$ | centred; the default choice |
| $f''(a) \approx [f(a+h) - 2f(a) + f(a-h)]/h^{2}$ | $O(h^{2})$ | second derivative |
| $\nabla^{2}f \approx \sum_{i}[f(x_i+h) - 2f(x_i) + f(x_i-h)]/h^{2}$ | $O(h^{2})$ | the Laplacian stencil used in every finite-difference model |

**The optimal step is not "as small as possible".** Round-off grows like
$\epsilon/h$ while truncation falls like $h^{p}$, so the total error is minimised
at an intermediate $h$ of order $\epsilon^{1/(p+2)}$. For double precision and a
centred first derivative that is near $10^{-5}$ relative step size.

## 4. Integration

| Integral | Result | Conditions |
|---|---|---|
| $\int x^{n}\,dx$ | $x^{n+1}/(n+1) + C$ | $n \ne -1$ |
| $\int dx/x$ | $\ln\lvert x\rvert + C$ | $x \ne 0$ |
| $\int e^{ax}\,dx$ | $e^{ax}/a + C$ | $a \ne 0$ |
| $\int \sin(ax)\,dx$ | $-\cos(ax)/a + C$ | $a \ne 0$ |
| $\int \dfrac{dx}{1+x^{2}}$ | $\arctan x + C$ | all $x$ |
| $\int_{0}^{\infty} e^{-ax}\,dx$ | $1/a$ | $a > 0$ |
| $\int_{-\infty}^{\infty} e^{-a x^{2}}\,dx$ | $\sqrt{\pi/a}$ | $a > 0$ |
| $\int_{-\infty}^{\infty} e^{-a x^{2}}e^{ibx}\,dx$ | $\sqrt{\pi/a}\,e^{-b^{2}/(4a)}$ | $a > 0$; the Gaussian transform pair |
| $\int_{0}^{\infty} x^{n}e^{-x}\,dx$ | $\Gamma(n+1)$ | $n > -1$ |
| Integration by parts $\int u\,dv$ | $uv - \int v\,du$ | the workhorse for boundary terms |

### Quadrature rules with their error terms

| Rule | Approximation | Error |
|---|---|---|
| Trapezoid | $h\left[\tfrac{1}{2}f_0 + f_1 + \cdots + f_{n-1} + \tfrac{1}{2}f_n\right]$ | $-\dfrac{(b-a)h^{2}}{12}f''(\xi)$ |
| Simpson (even $n$) | $\dfrac{h}{3}\left[f_0 + 4f_1 + 2f_2 + 4f_3 + \cdots + f_n\right]$ | $-\dfrac{(b-a)h^{4}}{180}f^{(4)}(\xi)$ |
| Midpoint | $h\sum_{i=1}^{n} f\!\left(a + (i-\tfrac{1}{2})h\right)$ | $+\dfrac{(b-a)h^{2}}{24}f''(\xi)$ |

All three require the stated derivatives to exist on the interval; Simpson also
requires a uniform grid and an even number of intervals.

## 5. Vector calculus

| Identity | Conditions |
|---|---|
| $\nabla\cdot(\phi\mathbf{A}) = \phi\nabla\cdot\mathbf{A} + \mathbf{A}\cdot\nabla\phi$ | differentiable fields |
| $\nabla\times(\phi\mathbf{A}) = \phi\nabla\times\mathbf{A} + \nabla\phi\times\mathbf{A}$ | differentiable fields |
| $\nabla\cdot(\nabla\times\mathbf{A}) = 0$ | always |
| $\nabla\times(\nabla\phi) = \mathbf{0}$ | a gradient field is irrotational |
| $\nabla\times(\nabla\times\mathbf{A}) = \nabla(\nabla\cdot\mathbf{A}) - \nabla^{2}\mathbf{A}$ | always |
| $\nabla\cdot(\mathbf{A}\times\mathbf{B}) = \mathbf{B}\cdot(\nabla\times\mathbf{A}) - \mathbf{A}\cdot(\nabla\times\mathbf{B})$ | always |
| $\oint_{\partial S}\mathbf{A}\cdot d\mathbf{l} = \int_{S}(\nabla\times\mathbf{A})\cdot d\mathbf{S}$ | Stokes, for a piecewise-smooth surface |
| $\oint_{\partial V}\mathbf{A}\cdot d\mathbf{S} = \int_{V}\nabla\cdot\mathbf{A}\,dV$ | divergence theorem |
| $\int_{V}(\phi\nabla^{2}\psi + \nabla\phi\cdot\nabla\psi)\,dV = \oint_{\partial V}\phi\nabla\psi\cdot d\mathbf{S}$ | Green's first identity |

## 6. Differential operators in the three coordinate systems

Assumed: $f$ twice differentiable; the singular points of the curvilinear forms
($r=0$, $\rho=0$) are excluded.

| Operator | Cartesian | Cylindrical $(\rho,\varphi,z)$ | Spherical $(r,\theta,\phi)$ |
|---|---|---|---|
| Gradient | $(\partial_x f, \partial_y f, \partial_z f)$ | $(\partial_\rho f, \tfrac{1}{\rho}\partial_\varphi f, \partial_z f)$ | $(\partial_r f, \tfrac{1}{r}\partial_\theta f, \tfrac{1}{r\sin\theta}\partial_\phi f)$ |
| Divergence | $\partial_x A_x + \partial_y A_y + \partial_z A_z$ | $\tfrac{1}{\rho}\partial_\rho(\rho A_\rho) + \tfrac{1}{\rho}\partial_\varphi A_\varphi + \partial_z A_z$ | $\tfrac{1}{r^{2}}\partial_r(r^{2}A_r) + \cdots$ |
| Laplacian | $\partial_x^{2} + \partial_y^{2} + \partial_z^{2}$ | $\tfrac{1}{\rho}\partial_\rho(\rho\,\partial_\rho f) + \tfrac{1}{\rho^{2}}\partial_\varphi^{2}f + \partial_z^{2}f$ | $\tfrac{1}{r^{2}}\partial_r(r^{2}\partial_r f) + \tfrac{1}{r^{2}\sin\theta}\partial_\theta(\sin\theta\,\partial_\theta f) + \tfrac{1}{r^{2}\sin^{2}\theta}\partial_\phi^{2}f$ |
| Volume element | $dx\,dy\,dz$ | $\rho\,d\rho\,d\varphi\,dz$ | $r^{2}\sin\theta\,dr\,d\theta\,d\phi$ |

$$ \nabla^{2}\frac{1}{r} = 0 \qquad (r \ne 0) $$

This single identity is why the $1/r$ potential of a point mass satisfies
Laplace's equation everywhere outside the source.

## 7. Ordinary differential equations

| Equation | Solution | Conditions |
|---|---|---|
| $y' + ay = 0$ | $y = y_0e^{-ax}$ | constant $a$ |
| $y'' + 2\beta y' + \omega_0^{2}y = 0$ | $e^{-\beta t}\bigl(A\cos\omega_d t + B\sin\omega_d t\bigr)$, $\omega_d = \sqrt{\omega_0^{2}-\beta^{2}}$ | underdamped, $\beta < \omega_0$ |
| $y'' + \omega_0^{2}y = 0$ | $A\cos\omega_0 t + B\sin\omega_0 t$ | undamped |
| $y'' - k^{2}y = 0$ | $Ae^{kt} + Be^{-kt}$ | exponential growth or decay |
| $y' + ay = b$ | $y = b/a + Ce^{-at}$ | steady state $b/a$ |

**Regime check.** The discriminant $\beta^{2} - \omega_0^{2}$ decides oscillation
versus decay. Writing an oscillatory solution where the system is overdamped is
a common and silent error; verify by computing the discriminant numerically.

## 8. Partial differential equations: classification

For a second-order linear equation
$A u_{xx} + 2Bu_{xy} + Cu_{yy} + \cdots = 0$, classify by
$\Delta = B^{2} - AC$:

| Class | $\Delta$ | Canonical example | Geophysical appearance |
|---|---|---|---|
| Elliptic | $< 0$ | $\nabla^{2}u = 0$ | potential fields, steady-state flow |
| Parabolic | $= 0$ | $u_t = \kappa u_{xx}$ | heat conduction, diffusion, EM induction |
| Hyperbolic | $> 0$ | $u_{tt} = c^{2}u_{xx}$ | wave propagation, seismic modelling |

The classification tells you which boundary conditions give a well-posed
problem: elliptic equations need boundary data all around, parabolic equations
need an initial condition plus boundary data, hyperbolic equations need both
initial value and initial rate.

Analytic solutions used repeatedly in this curriculum:

| Equation | Solution | Conditions |
|---|---|---|
| $u_t = \kappa u_{xx}$, $u(x,0) = \delta(x)$ | $u = \dfrac{1}{\sqrt{4\pi\kappa t}}e^{-x^{2}/(4\kappa t)}$ | infinite domain; width grows as $\sqrt{\kappa t}$ |
| $u_t = \kappa u_{xx}$, periodic surface $u(0,t)=A\cos\omega t$ | $u = A\,e^{-z/\delta}\cos(\omega t - z/\delta)$, $\delta = \sqrt{2\kappa/\omega}$ | semi-infinite half-space |
| $u_{tt} = c^{2}u_{xx}$ | $f(x-ct) + g(x+ct)$ | d'Alembert form |

The diffusion skin depth $\delta = \sqrt{2\kappa/\omega}$ is the same algebraic
shape as the electromagnetic skin depth, with $\kappa$ replaced by
$1/(\mu\sigma)$.

## 9. Transforms

Forward Fourier transform used in this repository (with $\omega = 2\pi f$):

$$ \hat{f}(\omega) = \int_{-\infty}^{\infty} f(t)e^{-i\omega t}\,dt $$

| Property | Statement |
|---|---|
| Linearity | $\mathcal{F}\{af + bg\} = a\hat{f} + b\hat{g}$ |
| Shift | $\mathcal{F}\{f(t-t_0)\} = e^{-i\omega t_0}\hat{f}(\omega)$ |
| Scaling | $\mathcal{F}\{f(at)\} = \tfrac{1}{\lvert a\rvert}\hat{f}(\omega/a)$ |
| Derivative | $\mathcal{F}\{f'(t)\} = i\omega\hat{f}(\omega)$ |
| Convolution | $\mathcal{F}\{f \ast g\} = \hat{f}\hat{g}$ |
| Parseval | $\int\lvert f(t)\rvert^{2}dt = \tfrac{1}{2\pi}\int\lvert\hat{f}(\omega)\rvert^{2}d\omega$ |

| Laplace pair | $f(t)$ | $F(s) = \int_0^\infty f(t)e^{-st}dt$ |
|---|---|---|
| exponential | $e^{-at}$ | $1/(s+a)$ |
| ramp | $t$ | $1/s^{2}$ |
| sinusoid | $\sin(\omega t)$ | $\omega/(s^{2}+\omega^{2})$ |
| step | $1$ | $1/s$ |

## 10. Special functions and distributions

| Object | Definition | Notes |
|---|---|---|
| Dirac delta | $\int_{-\infty}^{\infty}\delta(t-t_0)\phi(t)\,dt = \phi(t_0)$ | distribution, not a function; units of 1/time if $t$ is time |
| Heaviside step | $H(t) = 1$ for $t>0$, $0$ for $t<0$ | $dH/dt = \delta$ |
| Sifting with a function | $\delta(g(t)) = \sum_k \delta(t-t_k)/\lvert g'(t_k)\rvert$ | $t_k$ simple zeros of $g$ |
| Error function | $\operatorname{erf}(x) = \tfrac{2}{\sqrt{\pi}}\int_0^{x}e^{-u^{2}}du$ | $\operatorname{erf}(\infty)=1$; complement is $\operatorname{erfc}$ |
| Gamma function | $\Gamma(n+1) = n!$ for integer $n$ | $\Gamma(1/2) = \sqrt{\pi}$ |
| Bessel $J_0$ | solution of $y'' + y'/x + y = 0$ | appears in cylindrical diffusion problems |

## Worked example (numbers from the verification script)

The script `code/formulas_mathematics_demo.py` checks five of the formulas above
with explicit arithmetic. Excerpts of its output:

| Check | Exact value | Computed value | Error |
|---|---|---|---|
| Trapezoid for $\int_0^1 e^{x}dx$, $h = 0.25$ | $1.718281828$ | $1.727221905$ | $+8.940\times10^{-3}$ |
| Simpson for the same integral | $1.718281828$ | $1.718318842$ | $+3.701\times10^{-5}$ |
| Forward difference for $\cos 1$ | $+0.5403023059$ | $+0.5402602314$ | $-4.207\times10^{-5}$ |
| Centred difference for $\cos 1$ | $+0.5403023059$ | $+0.5403023050$ | $-9.004\times10^{-10}$ |
| Taylor series, $N = 10$ terms of $e^{1}$ | $2.7182818285$ | $2.7182815256$ | $-3.029\times10^{-7}$ |
| $\nabla^{2}(1/r)$ at $r = 2.50$ m | $0$ | $0.000\times10^{0}$ m⁻¹ | — |

Two lessons in one table: Simpson ($h^{4}$) beats the trapezoid rule ($h^{2}$)
by more than two orders of magnitude at the same step, and the centred
difference beats the forward difference by five orders of magnitude at the same
$h$. The *order* of an approximation is the thing to look up on this page; the
constant in front of it is problem-dependent.

## Assumptions and regime of validity

- Series converge only inside the stated radius; truncating a divergent series
  produces large, plausible-looking errors.
- Finite differences require smoothness on the scale of $h$; across a
  discontinuity (a layer boundary) no difference formula converges.
- Quadrature error terms assume the stated derivative exists and is bounded;
  integrals of discontinuous integrands need adaptive or split schemes.
- The curl and divergence identities assume fields differentiable on the domain
  and, for the integral theorems, a domain with piecewise-smooth boundary.
- Curvilinear Laplacians are written for the coordinate ranges $\rho > 0$,
  $r > 0$, $0 < \theta < \pi$; the axis is excluded.

## Verification script

[`code/formulas_mathematics_demo.py`](./code/formulas_mathematics_demo.py) —
print-only, seeded with `default_rng(20261014)`, runs in under a second and
exits 0. It prints the quadrature, finite-difference, series, Laplacian and
complex-exponential checks quoted above, each labelled with units, under a
`PROVENANCE: SYNTHETIC` banner.

## Related pages

- [Formula Sheet: Linear Algebra, SVD and Numerics](./02-formulas-linear-algebra-numerics.md)
- [Dimensional Analysis Quick Reference](../02-symbols-and-units/04-dimensional-analysis-reference.md)
- [Symbol Handbook: Notation Used Throughout](../02-symbols-and-units/01-symbol-handbook.md)
- [01-mathematics folder overview](../../01-mathematics/README.md)
- [19-numerical-modeling-hpc folder overview](../../19-numerical-modeling-hpc/README.md)
