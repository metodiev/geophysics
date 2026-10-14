---
id: 03-07-03
title: "Symbolic Solvers for Algebraic and Differential Equations"
level: advanced
prereqs: ["03-07-02"]
estimated_minutes: 120
tags: [sympy, solvers, odes, dsolve, root-finding, differential-equations]
---

# Symbolic Solvers for Algebraic and Differential Equations

Numerical solvers answer one question: what is the value here? Symbolic solvers
answer a different and often more useful one: **what is the solution, as a
function?**

That difference shows up most sharply in differential equations. A numerical
integrator gives you a trajectory for one set of parameters; `dsolve` gives you
the Bateman solution, with the two decay constants as symbols, valid for every
parameter pair — including the near-degenerate one where the numerical route
loses all its digits and the formula's denominator becomes a cancellation to
guard against.

This lesson walks through five equation types in increasing order of structure:
a polynomial with an exact factorisation, a transcendental equation with none, a
perturbation series derived by substitution, a linear ODE system, and a
boundary-value problem. Each symbolic result is checked against a numerical
route, and the agreement is quoted.

```bash
.venv/bin/python 03-scientific-computing/07-sympy/code/solving_equations_demo.py
```

## Learning objectives

By the end of this lesson you will be able to:

1. **Distinguish** the solution set a symbolic solver returns from the single
   root a numerical solver returns, and use each appropriately.
2. **Handle** the failure mode of `solve` on a transcendental equation, and
   **verify** a numerical root by its residual.
3. **Derive** a perturbation series by substituting an ansatz and solving order
   by order, then **measure** its truncation error against a root finder.
4. **Solve** a coupled linear ODE system symbolically and **verify** it against
   `solve_ivp` to a quoted tolerance.
5. **Solve** a boundary-value problem, **enter** the solution with units, and
   **account** for each term physically.
6. **Solve** a linear system symbolically and explain what the formula buys over
   the numbers.

## Prerequisites

- [03-07-02 Symbolic Differentiation, Integration and Limits](./02-symbolic-calculus.md)
- [03-03-03 scipy.optimize: Root Finding, Minimisation and Curve
  Fitting](../03-scipy/03-optimize.md) — the numerical solvers used as checks.

## 1. Intuition: the answer to "what is $x$?" has two shapes

A numerical root finder returns a number. It needs a bracket or a starting guess,
it converges to one root, and it says nothing about the others. A symbolic solver
returns an **expression** — or a set of expressions — that satisfies the equation,
and in doing so tells you about the structure: how many roots there are, whether
they are real, how they depend on the coefficients.

For an ODE the gap is wider. `solve_ivp` returns a sampled trajectory; `dsolve`
returns a family of functions. The demonstration's decay chain illustrates the
practical consequence:

```
  Eq(N2(t), N1_0*lambda1*exp(-lambda2*t)/(lambda1 - lambda2) - N1_0*lambda1*exp(-lambda1*t)/(lambda1 - lambda2))
  at t = 20000 a, N2/N1_0:
      closed form  = 9.110153911134706e-01
      solve_ivp    = 9.110153911134232e-01
      |difference| = 4.741e-14 (relative 5.204e-14)
  solve_ivp function evaluations: 1040, accepted steps: 173
```

The integrator took 173 accepted steps and 1040 function evaluations to reach the
formula's value to $5.2\times10^{-14}$ relative. The formula needed no steps, and
it still works when $\lambda_1 \to \lambda_2$, where the two exponentials in the
numerator and the $(\lambda_1 - \lambda_2)$ in the denominator cancel — a
catastrophic cancellation the symbolic route makes visible.

## 2. Precise definitions

**`solve`.** Returns solutions of an equation or system as an explicit list.
Raises `NotImplementedError` when it has no algorithm for the form.

**`solveset`.** Returns a *set* of solutions, with the domain stated. More honest
than `solve` about incomplete answers, and slower.

**`nsolve`.** Numerical root finding from a starting point, using the symbolic
expression for the residual and its derivatives.

**`dsolve`.** Solves ODEs and systems of ODEs. With `ics={...}` it applies
initial or boundary conditions and returns the particular solution.

**Residual.** The value of the equation's left-hand side at the reported
solution. For $E - e\sin E - M = 0$ at a candidate $E$, the residual is the
number that says how well the candidate satisfies it.

**Perturbation series.** An expansion $E = M + e\,a_1 + e^2 a_2 + \cdots$ whose
coefficients are found by substituting into the equation and matching powers.

## 3. Algebraic equations: exact, then verified

```
  polynomial: u**3 - 6*u**2 + 11*u - 6
  exact roots from solve(): [1, 2, 3]
  factored: (u - 3)*(u - 2)*(u - 1)
  nroots() numerical pass: [1.0000000, 2.0000000, 3.0000000]
  every exact root is an integer: True
  brentq on the bracket [1.5, 2.5]: 2.000000000000000
  |brentq - exact root 2| = 0.000e+00
```

The symbolic route found all three roots and factored the polynomial; the
numerical route found the one root inside a bracket that had to be supplied. The
difference is `0.000e+00` here because the root is exactly representable. That is
the coincidence to be careful about: **a numerical root that happens to be exact
is not evidence that numerical root finding is exact.**

## 4. Transcendental equations: what failure looks like

```
  solve(cos x = x, x) raised NotImplementedError: multiple generators [x, cos(x)]
  solveset(cos x - x, x, domain=S.Reals) -> ConditionSet(x, Eq(-x + cos(x), 0), Reals)
  nsolve from x0 = 1.0     : 0.73908513321516067229
  brentq on [0, 1]         : 0.73908513321515590
  difference               : 4.774e-15
  residual cos(x) - x      : +7.883e-15
```

Three points.

**The failure mode is an exception, not a wrong answer.** `solve` raises
`NotImplementedError`; code that calls it must handle that. `solveset` returns a
`ConditionSet`, which is a formal way of saying "the set of $x$ such that
$\cos x = x$" — true and not useful.

**The two numerical solvers agree to $4.8\times10^{-15}$**, which is about 20 ulp
for a value near 0.74. Neither is "more right"; they agree to the accuracy of
their stopping rules.

**The residual is the honest measure.** $\cos x - x = 7.9\times10^{-15}$ at the
reported root. For a function with $|f'|$ near 1, a root error of $10^{-15}$ gives
a residual of about $10^{-15}$; the factor of 8 between them comes from
$|f'| = |{-}\sin x - 1| \approx 1.67$ at that root. Quoting the residual is how
you avoid claiming more accuracy than you have.

## 5. Derivation: Kepler's equation by substitution

Kepler's equation relates the eccentric anomaly $E$ to the mean anomaly $M$ and
the eccentricity $e$:

$$E - e\sin E = M.$$

It has no closed-form solution, but it has a perturbation series, and deriving it
symbolically is a clean illustration of the technique. Substitute

$$E = M + e\,a_1 + e^2 a_2 + e^3 a_3,$$

expand $E - e\sin E - M$ to order $e^3$ and match powers. The demonstration does
exactly this:

```
  substitute E = M + e a1 + e^2 a2 + e^3 a3 into E - e sin E - M:
      Poly((a1**2*sin(M)/2 - a2*cos(M) + a3)*e**3 + (-a1*cos(M) + a2)*e**2 + (a1 - sin(M))*e, e, domain='EX')
      a1 = sin(M)
      a2 = sin(2*M)/2
      a3 = -3*sin(M)**3/2 + sin(M)
  third-order series: E = M - e**3*(3*sin(M)**2 - 2)*sin(M)/2 + e**2*sin(2*M)/2 + e*sin(M)
  standard form (3 sin3M - sinM)/8 for a3: 0
```

The last line is a check against the textbook coefficient: the demonstration
subtracts $(3\sin 3M - \sin M)/8$ from its own $a_3$ and gets exactly 0. Using
the identity $\sin 3M = 3\sin M - 4\sin^3 M$,

$$\frac{3\sin 3M - \sin M}{8} = \frac{8\sin M - 12\sin^3 M}{8} =
\sin M - \tfrac32\sin^3 M,$$

which is the form SymPy returned. **Deriving the series and checking it against
a published form is two minutes of work and removes the whole class of
sign-and-coefficient errors from the result.**

### 5.1 How good is the series? Measured

```
      second order (a1, a2)      = 1.186480145498093 rad; relative error 9.752e-04
      third order (a1, a2, a3)   = 1.186062034537465 rad; relative error 6.225e-04
       e    series(3rd) - brentq (rad)    relative
    0.01                     4.072e-09   4.038e-09
    0.05                     2.627e-06   2.518e-06
    0.2                     7.378e-04   6.225e-04
    0.4                     1.224e-02   8.782e-03
```

The root from `brentq` at $e = 0.2$, $M = 1$ rad is
$E = 1.185324203861382$ rad $= 67.9140742360°$.

Truncating after $e^3$ leaves an error of order $e^4$, so raising $e$ by a factor
of 5 should raise the error by $5^4 = 625$: the measured ratio between
$e = 0.01$ and $e = 0.05$ is $2.627\times10^{-6}/4.072\times10^{-9} = 645$, and
between $e = 0.05$ and $e = 0.2$ it is $7.378\times10^{-4}/2.627\times10^{-6} =
281$ against a predicted $4^4 = 256$. **The scaling is confirmed, which is what
turns "good for near-circular orbits" from a rule of thumb into a measurement.**

## 6. ODE systems: the decay chain

For a parent $N_1$ decaying into a daughter $N_2$:

$$\frac{dN_1}{dt} = -\lambda_1 N_1, \qquad \frac{dN_2}{dt} = \lambda_1 N_1 -
\lambda_2 N_2,$$

with $N_1(0) = N_1^0$ and $N_2(0) = 0$. `dsolve` returns

$$N_1(t) = N_1^0 e^{-\lambda_1 t}, \qquad
N_2(t) = \frac{N_1^0\lambda_1}{\lambda_1 - \lambda_2}
\left(e^{-\lambda_2 t} - e^{-\lambda_1 t}\right),$$

which is the Bateman solution. Evaluated at $t = 20000$ a with the measured
constants:

```
  decay constants: lambda1 = 1.209681e-04 /a (14C), lambda2 = 4.997456e-10 /a (an illustrative long-lived daughter)
      closed form  = 9.110153911134706e-01
      solve_ivp    = 9.110153911134232e-01
      |difference| = 4.741e-14 (relative 5.204e-14)
```

Two comments on the parameter choice, because honesty about synthetic data
matters: $\lambda_1$ is the real $^{14}$C decay constant; $\lambda_2$ is
**illustrative**, chosen to be long-lived, not a specific nuclide. The point of
the example is the structure of the solution, not the isotope.

The relative agreement of $5.2\times10^{-14}$ is the integrator's tolerance
(`rtol=1e-12` with the smaller of the two components setting the achievable
agreement), and the closed form needed no tolerance at all.

**Where the formula is hard and the integrator is easy:** at
$\lambda_1 \approx \lambda_2$ the formula's denominator vanishes and its two
exponentials nearly cancel. The symbolic system can be asked for the limit
directly (`sp.limit` on the expression as $\lambda_2 \to \lambda_1$), which gives

$$N_2(t) \to N_1^0 \lambda_1 t\, e^{-\lambda_1 t}
\qquad (\lambda_2 = \lambda_1),$$

the degenerate case that would be produced by a separate derivation. **The
symbolic route can be asked about a parameter regime the numerical route cannot
enter at all.**

## 7. The damped oscillator: an ansatz, verified

For $q'' + 2\zeta\omega_0 q' + \omega_0^2 q = 0$ with $\zeta < 1$, the
underdamped solution is

$$q(t) = e^{-\zeta\omega_0 t}\left(A\cos\omega_d t + B\sin\omega_d t\right),
\qquad \omega_d = \omega_0\sqrt{1-\zeta^2}.$$

The demonstration does not simply call `dsolve` — it proposes the ansatz,
substitutes it, and simplifies:

```
  ansatz: q(t) = exp(-zeta omega0 t) (A cos(omega_d t) + B sin(omega_d t))
  substituting it into the ODE, with omega_d^2 = omega0^2 (1 - zeta^2), leaves residual 0
  A = q0
  B = (omega0*q0*zeta + v0)/omega_d
  parameters: omega0 = 6.283185 rad/s (1 Hz), zeta = 0.05, omega_d = 6.275326411 rad/s, q(0) = 1, q'(0) = 0
  max |closed form - solve_ivp| over 601 samples: 8.945e-13
  damped period 2 pi/(omega0 sqrt(1-zeta^2)) = 1.001252349 s  (undamped: 1.000000000 s)
  from the grid extrema: q_max = 1.0000000000, q_min = -0.8544678815, delta measured = 0.157276365
  zeta recovered from the grid extrema = 0.050000004 (input 0.05)
```

Three results worth keeping:

**The residual is exactly zero.** Once $\omega_d^2 = \omega_0^2(1-\zeta^2)$ is
imposed, the ODE's left-hand side simplifies to 0 for all $t$ — an algebraic
identity, not a numerical near-cancellation.

**The closed form agrees with `solve_ivp` to $8.9\times10^{-13}$** over 601
samples, which is the integrator's error, not the formula's.

**The logarithmic decrement recovers $\zeta$ to 7 digits.** The measured ratio of
successive extrema is $q_{\min}/q_{\max} = -0.8544678815$, so

$$\delta = -\ln\left|\frac{q_{\min}}{q_{\max}}\right| = 0.157276365, \qquad
\zeta = \frac{\delta}{\sqrt{\pi^2 + \delta^2}} = 0.050000004,$$

against an input of 0.05. This is the seismological measurement of attenuation,
done here on a synthetic signal where the input is known — which is exactly how
you should validate a $Q$ or $\zeta$ estimator before trusting it on data.

### 7.1 The failure `dsolve` produced on its own

Called without telling it that $\zeta < 1$, `dsolve` returned the *overdamped*
form, containing $\sqrt{\zeta-1}\sqrt{\zeta+1}$. At $\zeta = 0.05$ that product
is imaginary, and the expression evaluated to `nan`. The lesson is not that
SymPy is wrong — the general solution genuinely has three branches — but that
**an assumption the symbol does not have is a wrong answer you will only notice
when it evaluates to `nan`.** This is the same point as in
[03-07-01](./01-symbolic-basics.md) and it is worth repeating because the failure
is silent in the algebra and loud only at the last step.

## 8. Linear systems, symbolically and numerically

```
  det(A) operation count: 17
  s1 = (b1*m22*m33 - b1*m23*m32 - b2*m12*m33 + b2*m13*m32 + b3*m12*m23 - b3*m13*m22)/(m11*m22*m33 - ...)
  concrete A and b -> symbolic solution  [ 2.16666667 -0.36111111  2.13888889]
                      numpy.linalg.solve [ 2.16666667 -0.36111111  2.13888889]
  max |difference| = 4.441e-16
  det(A) = 36.000000, cond(A) = 5.019958
  verification: max |A x - b| = 8.882e-16
```

The symbolic solution is a formula in the nine entries of $A$ — Cramer's rule,
which SymPy applied without being asked. The numerical solution is three numbers.
They agree to $4.4\times10^{-16}$ on this well-conditioned matrix ($\kappa = 5.0$),
and the verification residual is $8.9\times10^{-16}$.

What the formula buys: you can differentiate it with respect to $m_{11}$ and get
the sensitivity of $s_1$ to that datum, which is what an error budget needs. What
it costs: the formula grows as $n!$ in the number of operations, so it is a tool
for small systems and for structure, not for a 500-station inversion.

## 9. A boundary-value problem with units

Steady-state conduction with internal heat production:

$$k\frac{d^2T}{dz^2} + A = 0,$$

with $T(0) = T_{\text{surf}}$ and $k\,T'(0) = q_{\text{surf}}$ (flux upward,
depth $z$ increasing downward). `dsolve` with both conditions returns

$$T(z) = T_{\text{surf}} + \frac{q_{\text{surf}}}{k}z -
\frac{A}{2k}z^2,$$

and the demonstration evaluates it for representative continental values:

```
  general solution: -A*z**2/(2*k) + C1 + C2*z
      T(z) = -A*z**2/(2*k) + T_surf + q_surf*z/k
  k = 3.0 W/m/K, A = 1.0e-06 W/m^3, T(0) = 283.15 K, q(0) = 0.065 W/m^2
      T(30000 m) = 783.1500 K
      q(30000 m) = 0.035000000 W/m^2  (surface flux - A H = 0.035000000)
  closed-form difference q_surf - q(H): 30000.0*A W m^-2 = 0.030000000 W m^-2
  temperature at the base above the surface value: 500.0000 K; q_surf H/k = 650.0000 K, A H^2/(2k) = 150.0000 K
  the two contributions sum to 500.0000 K, which matches T(H) - T_surf to 0.00e+00 K
```

Every number here is a dimensional check as well as a value:

$$\left[\frac{q_{\text{surf}} z}{k}\right] =
\frac{\mathrm{W\,m^{-2}}\cdot\mathrm{m}}{\mathrm{W\,m^{-1}\,K^{-1}}} =
\mathrm{K}, \qquad
\left[\frac{A z^2}{k}\right] = \frac{\mathrm{W\,m^{-3}}\cdot\mathrm{m^2}}
{\mathrm{W\,m^{-1}\,K^{-1}}} = \mathrm{K}.$$

And the physics: the base flux is the surface flux *minus* the heat generated on
the way up, measured as $0.065 - 1.0\times10^{-6}\times30000 = 0.035\
\mathrm{W\,m^{-2}}$. The sign is the easiest thing in the whole lesson to get
backwards, and the units of $A H$ — $\mathrm{W\,m^{-2}}$ — are what catch it.
A 30 km column with these properties is $500$ K hotter at its base than at its
top: 650 K from the surface gradient minus 150 K from the radiogenic curvature.

## 10. Assumptions and limitations

- **`solve` is not complete.** It may return a subset, or raise. Use `solveset`
  with an explicit domain when you need to know what was found.
- **`dsolve` cannot solve most nonlinear ODEs**, and its output may be an
  unevaluated `Integral`. That is a result too.
- **Branch assumptions are yours to state.** Section 7.1 is the worked example.
- **Symbolic solutions of large systems are not tractable.** The operation count
  of a determinant grows factorially; keep the symbolic route for insight.
- **The integrals in `solve_ivp` and in `dsolve` are different objects.** One is
  a sampled approximation with a tolerance; the other is a formula. Comparing
  them (as Sections 6 and 7 do) tests the formula against the integrator and
  vice versa; neither is a proof of the other.
- **The decay constant for the daughter in Section 6 is illustrative**, not a
  specific nuclide. It is stated as such, and the conclusion does not depend on
  it.

## 11. Worked examples

### 11.1 Solving for a depth from a transcendental profile

Given $T(z) = 300\,\mathrm{K} - 25\,\mathrm{K}\cdot
\mathrm{erfc}(z/2000)$, find the depth at which $T = 290$ K. I did not test
whether this particular inverse is available in closed form from `solve`, so the
procedure below is the one to use whenever the symbolic route is uncertain:

1. Attempt the symbolic route and record what it returns — a solution, an empty
   list, or `NotImplementedError`.
2. Bracket the root from the physics: temperature increases with depth here, so
   the 290 K depth must lie between the surface and the depth where $T$ passes
   300 K minus 25 K. State the bracket before solving.
3. Solve with `brentq` and report the residual.
4. Compare with a second method (`nsolve`) and report the difference.

Step 2 is the one that is usually skipped and the one that prevents a solver from
returning a root in a physically absurd place.

### 11.2 A root with no closed form, done properly

For $\cos x = x$ the demonstration's procedure is the template:

1. Try the symbolic route and **record the failure mode**
   (`NotImplementedError`).
2. Bracket the root from the physics: $\cos 0 = 1 > 0$ and
   $\cos 1 = 0.5403 < 1$, so the root is in $(0, 1)$.
3. Solve with two independent methods and **compare** ($4.8\times10^{-15}$).
4. Quote the **residual** ($7.9\times10^{-15}$), not just the root.

That is what "verified" means for a numerical answer.

### 11.3 A boundary-value problem as a fitting model

The geotherm of Section 9 has three parameters: $q_{\text{surf}}$, $A$, $k$.
Measured surface heat flow and a published conductivity therefore predict the
temperature at depth, and the difference between that prediction and a borehole
log is the quantity of interest. Because the solution is closed-form, the
sensitivities $\partial T/\partial q_{\text{surf}}$ and $\partial T/\partial A$
are available symbolically — which is how the uncertainty in a fitted $A$ is
obtained rather than guessed.

## 12. Python demonstration

`code/solving_equations_demo.py` runs in seven parts:

| Part | Type | Verification |
|---|---|---|
| 1 | Cubic | three exact roots; `brentq` matches to `0.000e+00` |
| 2 | Transcendental | `NotImplementedError` recorded; two solvers agree to `4.774e-15` |
| 3 | Perturbation series | $a_3$ matches $(3\sin3M - \sin M)/8$ to 0; error scales as $e^4$ |
| 4 | Linear ODE system | closed form against `solve_ivp`: `5.204e-14` relative |
| 5 | Damped oscillator | residual 0; `8.945e-13` against `solve_ivp`; $\zeta$ recovered to 7 digits |
| 6 | Linear system | `4.441e-16` against `numpy.linalg.solve` |
| 7 | Boundary-value problem | two temperature contributions sum to the solution, residual `0.00e+00` |

The pattern in every part is the same: **derive symbolically, then check
numerically, and quote the residual.**

## 13. Exercises

Solutions are in
[`exercises/03-solving-equations-solutions.md`](./exercises/03-solving-equations-solutions.md).

### ★ Foundational

**★1.** Solve symbolically and state the number of real roots:
(a) $x^2 - 5x + 6 = 0$, (b) $x^2 + 1 = 0$, (c) $x^3 - x = 0$.

**★2.** For each, say whether `solve` will return an explicit solution and why:
(a) $\sin x = 0.5$, (b) $e^{-x} = x$, (c) $x^5 - x + 1 = 0$.

**★3.** Solve $T'(t) = -kT(t)$ with $T(0) = T_0$ by hand and with `dsolve`, and
state the dimensions of $k$ given that $T$ is a temperature.

**★4.** What is a residual, and why is it a better verification of a numerical
root than the number of iterations?

### ★★ Applied

**★★5.** Derive the Bateman solution for a *three*-member chain with `dsolve`,
and report the structure of the $N_3(t)$ term. Explain why the number of
exponentials equals the number of members.

**★★6.** Solve the damped oscillator for $\zeta = 1$ (critically damped) and
$\zeta = 2$ (overdamped) and report the three solution forms. Explain what
happens to the underdamped ansatz at $\zeta = 1$.

**★★7.** Solve a two-layer geotherm boundary-value problem: $T$ and
$k\,dT/dz$ continuous at the interface, with fixed surface temperature and fixed
basal flux. Report the closed form, the interface temperature, and the exact
agreement of the two solutions at the interface.

**★★8.** Kepler's series: derive the fourth-order coefficient $a_4$ by the same
substitution, verify your result against a published form, and report the
improvement in the error at $e = 0.2$ (quantitatively).

### ★★★ Research-oriented

**★★★9.** Build a synthetic validation for a $Q$ estimator. Generate a damped
sinusoid with known $\zeta$, add Gaussian noise at a stated SNR, estimate $\zeta$
from the logarithmic decrement of the extrema and from a spectral peak width,
and report both estimates with their errors. State which estimator you would use
on a 30-second teleseismic record and why.

**★★★10.** Assess the cost of the symbolic route. For a linear system of size
$n = 2, 3, 4, 5$, record the number of operations in the symbolic solution
(`count_ops` on the expression after `A.solve(b)`), and compare with the
$O(n^3)$ operation count of Gaussian elimination. Report both sequences, the
crossover size, and state the practical rule this implies for using the symbolic
route on inversion problems.

## 14. Common mistakes

1. **Calling `solve` without handling `NotImplementedError`.**
2. **Trusting `solve`'s output to be the complete solution set.** Use `solveset`
   with a domain when completeness matters.
3. **Quoting a numerical root without its residual.**
4. **Assuming `dsolve` knows your parameter regime.** Section 7.1.
5. **Using a perturbation series outside its measured range.** Section 5.1.
6. **Forgetting the degenerate case.** The Bateman solution at
   $\lambda_1 = \lambda_2$ needs the limit, not the formula.
7. **Comparing a formula to an integrator and calling the formula "proved".**
   It is verified against that code, not against the world.

## 15. Real-world applications

- **Geochronology.** Decay chains and their degenerate limits are exactly the
  Bateman expressions; batch models (U-series, cosmogenic nuclides) are small
  linear systems.
- **Heat flow provinces.** The geotherm of Section 9 is fitted to borehole data,
  and its sensitivities come from the closed form.
- **Orbital and tidal mechanics.** Kepler's equation and its series appear in
  every satellite-geodesy chain.
- **Attenuation measurement.** The logarithmic decrement of Section 7 is the
  standard estimator for $Q$ in a laboratory or borehole setting.
- **Inversion structure.** Small symbolic systems expose which data control which
  parameters, which is how a survey design is justified before any data are
  acquired.

## 16. Further reading

- **SymPy documentation** (sympy.org). Level: intermediate. The solvers guide:
  `solve`, `solveset`, `nsolve`, `dsolve`, and their documented limitations.
- **scipy.integrate documentation** (scipy.org). Level: intermediate. `solve_ivp`,
  its tolerance parameters, and the `nfev` counter that Section 6 quotes.
- **Brent, R. P. (1973). *Algorithms for Minimization without Derivatives*.
  Prentice-Hall.** Level: advanced. The root finder behind `brentq`, and the
  guarantee that makes a bracket a proof.
- **Press, W. H. et al. (2007). *Numerical Recipes* (3rd ed.). Cambridge
  University Press.** Chapter 17. Level: intermediate. A complementary treatment
  of the Bateman solution and its degenerate limit.
- **Bateman, H. (1910). The solution of a system of differential equations
  occurring in the theory of radioactive transformations. *Proc. Cambridge
  Philos. Soc.*, 15, 423–427.** Level: advanced. The original, for reference.

> Note on citations: bibliographic details are given so you can locate the works.
> This repository does not host or reproduce copyrighted text.

## 17. Related lessons

- [01 Symbolic Variables, Expressions and Assumptions](./01-symbolic-basics.md)
- [02 Symbolic Differentiation, Integration and Limits](./02-symbolic-calculus.md)
- [04 Symbolic Tensors and Index Notation](./04-tensor-symbolic.md)
- [05 Generating Fast Numerical Code from Symbolic Results](./05-code-generation.md)
- [03-03-03 scipy.optimize](../03-scipy/03-optimize.md) — the numerical half of
  every check in this lesson.

## 18. Self-assessment checklist

- [ ] I can say what `solve` returns that `brentq` cannot. (§3)
- [ ] I can handle the transcendental failure mode and verify by residual. (§4)
- [ ] I can derive a perturbation series and check it against a published form.
      (§5)
- [ ] I can measure the truncation error's scaling. (§5.1)
- [ ] I can solve a coupled linear ODE system and verify it. (§6)
- [ ] I can state why the underdamped ansatz needs an assumption. (§7.1)
- [ ] I can solve a boundary-value problem and account for each term
      dimensionally. (§9)
- [ ] I can say when the symbolic linear-solve route stops being practical. (§8)
