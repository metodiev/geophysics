---
id: 01-12-06
title: "Numerical ODE Solvers: Euler, Runge-Kutta, Implicit and Adaptive"
level: graduate
prereqs: ["01-05-04", "01-08-01", "01-08-07"]
estimated_minutes: 90
tags: [numerical-methods, ode-solvers, runge-kutta, stiffness, stability]
---

# Numerical ODE Solvers: Euler, Runge-Kutta, Implicit and Adaptive

## Learning objectives

By the end of this lesson you will be able to:

1. **Distinguish** order of accuracy from linear stability, and explain why
   consistency plus stability implies convergence for a one-step method.
2. **Derive** the stability limit $h < 2/\lambda$ of explicit Euler from its
   amplification factor, and predict the growth rate above it.
3. **Contrast** A-stability and L-stability, with the trapezoidal rule as the
   example that is A-stable but rings on stiff transients.
4. **Implement** forward Euler, Heun, classical RK4, backward Euler and the
   trapezoidal rule, and measure each order from its error sequence.
5. **Describe** adaptive step-size control by step doubling, and explain the
   measured case where its error estimator fails on a stiff problem.
6. **Model** radiogenic decay, thermal relaxation and a damped seismic oscillator
   as ODEs, and validate each against its closed-form solution.

## Prerequisites

[01-05-04 Taylor Series](../05-single-variable-calculus/04-taylor-series.md) —
the source of every truncation term. [01-08-01 First-Order
ODEs](../08-ordinary-differential-equations/01-first-order-odes.md) — the
equations being solved and their closed-form solutions.
[01-08-07 Stiff Systems and Numerical Stability Challenges](../08-ordinary-differential-equations/07-stiff-systems.md)
— the phenomenon that dominates §5 here, treated there from the mathematical side.

## 1. Intuition: order and stability are different questions

Two questions must be answered about any time-stepping scheme, and confusing them
is the most expensive mistake in computational geophysics.

- **Order** answers: if the step is small, how fast does the error vanish? It is
  a statement about accuracy, and it is read off from the local truncation error.
- **Stability** answers: for a *fixed* step, does the computed solution stay
  bounded? It is a statement about the spectrum of the problem, and it can fail
  completely at any step size.

The classical example is explicit Euler, whose order understates its usefulness
(for stiff problems it is useless) and whose stability limit has nothing to do
with its accuracy. Against that, the trapezoidal rule is second order and
unconditionally stable — and still the *wrong* choice for a stiff transient,
because it does not damp the fast mode. Three properties, three different
answers.

The picture to keep in mind is that a numerical ODE solve is a map applied
repeatedly. Every one-step method can be written as
$y_{k+1} = R(h\lambda)y_k$ on the model problem $y' = \lambda y$, where $R$ is the
method's **stability function**. Accuracy is the statement $R(z) =
\mathrm e^{z} + O(z^{p+1})$; stability is the statement $|R(z)|\le1$ for the
$z$ at hand. The two are independent conditions on the same function.

## 2. Precise definitions

### 2.1 The methods

For $y' = f(t,y)$, $y(t_n)=y_n$, with step $h$:

$$\text{forward Euler:}\quad y_{n+1} = y_n + h f(t_n,y_n),$$

$$\text{Heun (RK2):}\quad y_{n+1} = y_n + \tfrac{h}{2}\left[f(t_n,y_n)
+ f(t_n+h,\,y_n+hf(t_n,y_n))\right],$$

$$\text{classical RK4:}\quad y_{n+1} = y_n + \tfrac{h}{6}(k_1+2k_2+2k_3+k_4),$$

with $k_1=f(t_n,y_n)$, $k_2=f(t_n+\tfrac h2, y_n+\tfrac h2k_1)$,
$k_3=f(t_n+\tfrac h2, y_n+\tfrac h2k_2)$, $k_4=f(t_n+h, y_n+hk_3)$;

$$\text{backward Euler:}\quad y_{n+1} = y_n + h f(t_{n+1},y_{n+1}),$$

$$\text{trapezoidal:}\quad y_{n+1} = y_n + \tfrac{h}{2}\left[f(t_n,y_n)
+ f(t_{n+1},y_{n+1})\right].$$

The last two are implicit: $y_{n+1}$ appears on both sides, and each step requires
a root find — a scalar Newton iteration, in the demonstration.

### 2.2 Order of a one-step method

A method has order $p$ if the **local truncation error** — the residual obtained
by substituting the exact solution into the scheme — is $O(h^{p+1})$. The global
error after a fixed time interval is then $O(h^p)$, because $O(1/h)$ steps each
contribute $O(h^{p+1})$.

### 2.3 Stability, A-stability and L-stability

Apply the method to $y' = \lambda y$ with $\mathrm{Re}\,\lambda<0$ and write
$y_{n+1} = R(z)y_n$ with $z = h\lambda$. Then:

- **Absolute stability** requires $|R(z)|\le1$; the set of such $z$ is the
  stability region.
- **A-stability** means the whole left half-plane is in the stability region: no
  step restriction at all for a decaying problem.
- **L-stability** additionally requires $R(z)\to0$ as $\mathrm{Re}\,z\to-\infty$,
  i.e. the method damps infinitely fast modes completely.

Explicit Euler has $R(z) = 1+z$, so $|R|\le1$ on the real axis requires
$h\lambda \in[-2,0]$. Backward Euler has $R(z) = 1/(1-z)$, which is bounded by 1
throughout the left half-plane *and* tends to 0 — it is L-stable. The trapezoidal
rule has $R(z) = (1+z/2)/(1-z/2)$, which is A-stable and tends to $-1$: it
preserves the magnitude of the fast mode instead of annihilating it. That single
fact is what the demonstration's $h=0.5$ row measures.

## 3. Derivations

### 3.1 Orders from Taylor expansion

Forward Euler's local truncation error is the first omitted Taylor term,
$\tfrac{h^2}{2}y''$, so the scheme is order 1. Heun is constructed so that the
$h^2$ term matches the Taylor expansion's, leaving $O(h^3)$: order 2. RK4 matches
through $h^4$, leaving $O(h^5)$: order 4. Matching $m$ Taylor terms requires $m$
function evaluations at distinct abscissae (the Butcher barrier), so order 4
needs 4 evaluations and order 5 needs at least 6.

Backward Euler's truncation error is $-\tfrac{h^2}{2}y''$: also order 1, with the
opposite sign. The trapezoidal rule is the average of the two, so the $h^2$ terms
cancel and the local error is $O(h^3)$: order 2. The demonstration measures
1.00, 2.01, 4.01, 1.00 and 2.00 for the five methods — including the two implicit
ones, whose orders are unaffected by their implicitness.

### 3.2 The stability limit, and the growth above it

For explicit Euler, $R(z) = 1+z$, so on the real axis the stability condition is

$$|1+h\lambda|\le1 \iff -2 \le h\lambda \le 0 \iff h \le \frac{2}{\lambda}.$$

For the demonstration's stiff problem with $\lambda = 50\ \mathrm{s^{-1}}$, the
limit is $h \le 0.04$. The measured behaviour straddling it:

| $n$ | $h$ | max error on $[0,1]$ | verdict |
|---|---|---|---|
| 20 | 0.050000 | $3.327\times10^{3}$ | unstable |
| 22 | 0.045455 | $2.015\times10^{2}$ | unstable |
| 25 | 0.040000 | $1.136$ | marginal |
| 26 | 0.038462 | $1.070$ | stable |
| 200 | 0.005000 | $5.151\times10^{-2}$ | stable |

and the per-step multiplier, measured directly from the recursion, agrees with
$|1-\lambda h|$ to $7\times10^{-18}$: at $h=0.0401$ the multiplier is 1.005, at
$h=0.06$ it is 2.000. **The blow-up is the predicted instability, not a coding
accident**, and it is invisible in the local truncation error, which is small
throughout.

### 3.3 Implicit methods and the L-stability distinction

At steps far above the explicit limit the two implicit methods stay bounded:

| $h$ | explicit Euler | backward Euler | trapezoidal |
|---|---|---|---|
| 0.05 | $3.327\times10^{3}$ | $2.852\times10^{-4}$ | $3.461\times10^{-6}$ |
| 0.10 | $1.050\times10^{6}$ | $5.835\times10^{-4}$ | $1.952\times10^{-4}$ |
| 0.25 | $1.753\times10^{4}$ | $1.583\times10^{-3}$ | $2.749\times10^{-1}$ |
| 0.50 | $5.788\times10^{2}$ | $4.863\times10^{-3}$ | $7.253\times10^{-1}$ |

Note $h=0.5$: the *second-order* trapezoidal rule is 150 times worse than the
*first-order* backward Euler. The reason is the stability function's limit: the
fast mode decays like $\mathrm e^{-50t}$, but the trapezoidal rule multiplies it
by $-1$ per step instead of by 0, so it persists as a ringing oscillation. For a
stiff problem in which the fast modes carry no information, L-stability is worth
more than an extra order. For one in which their decay is the signal, the reverse
holds.

### 3.4 Adaptive stepping by step doubling

The idea is to estimate the local error without knowing the solution: take one
step of size $h$ and two of size $h/2$, and use

$$\text{error} \approx \frac{|y_{\text{two}} - y_{\text{one}}|}{2^{p+1}-1} .$$

Accept when the estimate is below the tolerance, and either grow or shrink $h$ by
a factor proportional to $(\text{tol}/\text{err})^{1/(p+1)}$. For a smooth
problem this works well. On the non-stiff $y'=y^2$ with the closed-form solution
$1/(1-t)$, integrated to $t=0.95$:

| tol | steps | rejected | relative error | f evals | uniform panels for the same error |
|---|---|---|---|---|---|
| $10^{-6}$ | 18 | 14 | $2.49\times10^{-6}$ | 352 | 256 |
| $10^{-8}$ | 38 | 17 | $2.84\times10^{-8}$ | 605 | 512 |
| $10^{-10}$ | 93 | 26 | $1.38\times10^{-10}$ | 1 309 | 2 048 |
| $10^{-12}$ | 231 | 28 | $6.55\times10^{-13}$ | 2 849 | 8 192 |

The relative error tracks the tolerance, the step shrinks automatically as the
timescale $1/y$ collapses toward $t=1$, and the work is a fraction of the uniform
grid of comparable accuracy.

### 3.5 Where the estimator fails

The same controller on the stiff transient gives

| tol | steps | rejected | final error | error/tol | measured slope |
|---|---|---|---|---|---|
| $10^{-4}$ | 55 | 14 | $4.566\times10^{-3}$ | 45.7 | – |
| $10^{-6}$ | 658 | 19 | $4.690\times10^{-4}$ | 469 | 0.49 |
| $10^{-8}$ | 6 704 | 22 | $4.369\times10^{-5}$ | 4 369 | 0.52 |

The tolerance is missed by factors of tens to thousands, and the error falls like
$\mathrm{tol}^{0.5}$ rather than like $\mathrm{tol}$: **it is not the quantity the
estimator is controlling.** The reason is structural. Step doubling assumes the
local error is the smooth $Ch^5$ term of RK4. With $\lambda h$ of order 1, the
error is instead dominated by the mismatch between the RK4 stability polynomial
$R(\lambda h)$ and $\mathrm e^{\lambda h}$, which does not scale like $h^5$. The
estimator therefore underestimates, the controller enlarges the step, and the
accepted steps are too large near the transient.

Two things should be said about this result. First, the measured exponent 0.5 is
*reported, not derived*: I have not analysed the stiff error balance, and the
honest statement is that the observed error is proportional to the square root of
the requested tolerance over the range measured. Second, the correct response is
not a smaller safety factor — it is a stiffness-aware or implicit method. Uniform
RK4 on the same problem needs 128 steps for $10^{-6}$ and 1 024 for $10^{-10}$,
i.e. it beats the adaptive controller outright, because a uniform grid cannot be
fooled by an estimator that assumes the wrong error model.

## 4. Physical interpretation

### 4.1 Radiogenic decay

A radionuclide with half-life $T_{1/2}$ obeys $y' = -\lambda y$ with
$\lambda = \ln2/T_{1/2}$. For $T_{1/2} = 1.25$ Gyr, $\lambda =
1.757161\times10^{-17}\ \mathrm{s^{-1}}$. After 4.5 Gyr,
$\lambda t = 2.495330$ decay constants, and the surviving fraction is
$8.2469\%$. The numerical difficulty is set by the dimensionless product
$\lambda t$, not by the physical duration: a 4.5 Gyr integration is *cheap*,
because 2.5 decay constants are easy for every method (RK4 with 40 steps gives
$2.7\times10^{-8}$ error here). Stiffness in geochronology comes from a *decay
chain* with widely different constants, not from the length of the interval — and
that is where a general-purpose explicit solver becomes unusable.

### 4.2 Thermal relaxation

A shallow layer relaxing toward a fixed surface temperature obeys
$T' = -k(T-T_s)$ with $k = 1/\tau$, $\tau = 30$ yr $= 1.0563\times10^{-9}\
\mathrm{s^{-1}}$ in the demonstration's units. Over 100 years (3.3 relaxation
times) the exact change from 12 °C toward 8 °C is to
$8.142695973389$ °C. All methods succeed here; RK4 with 200 steps reaches
$3.1\times10^{-10}$ °C. The interesting regime is $k t \gg 1$, where an explicit
method must still resolve the transient to remain stable even though the
transient is long over — the practical motivation for implicit geothermal and
palaeoclimate solvers.

### 4.3 Damped seismic oscillator

For $m\ddot x + c\dot x + kx = 0$ written as a first-order system with
$m=1$ kg, $c=0.4$ N s/m, $k=25$ N/m, the natural frequency is
$\omega_0 = 5.000000$ rad/s, the damping ratio $\zeta = 0.040000$ and the damped
frequency $\omega_d = 4.995998$ rad/s. RK4 on the system measures orders 2.84,
3.30, 3.77, 3.90 and 3.96 as $n$ grows from 10 to 320 — the approach to 4 that a
pre-asymptotic sequence shows. The computed energy ratio at $t=2$ s agrees with
the closed-form value $0.46604676743663964$ to the accuracy of the integration,
and the energy decreases monotonically, as $\mathrm dE/\mathrm dt = -cv^2 \le 0$
requires.

That last check matters more than it looks. A scheme that *grew* the energy would
be displaying its own instability, and over a long seismogram that is the failure
mode that matters. RK4 is not symplectic, so for an undamped oscillator it drifts
slowly in energy even when stable; symplectic integrators preserve the
qualitative energy behaviour instead of the exact trajectory.

## 5. Assumptions and regime of validity

| Method | Order | Stability | Use when |
|---|---|---|---|
| Forward Euler | 1 | $h\le2/\lvert\lambda\rvert$ | teaching, or a non-stiff problem with a tiny accuracy requirement |
| Heun (RK2) | 2 | $h\le2/\lvert\lambda\rvert$ | cheap non-stiff work |
| RK4 | 4 | $h\lesssim2.78/\lvert\lambda\rvert$ | the default explicit workhorse |
| Backward Euler | 1 | A- and L-stable | stiff problems where accuracy needs are modest |
| Trapezoidal | 2 | A-stable, not L-stable | stiff problems needing order 2, without severe transients |
| Adaptive RK4 | 4 | as RK4 | smooth problems with localised features |

Three caveats.

1. **The stability limit quoted is for the real-axis model problem.** For complex
   $\lambda$, or for a system, the limit depends on the whole spectrum; a system
   is stable when every eigenvalue lies in the method's stability region. A
   single fast decaying mode in an otherwise slow system sets the explicit step
   limit for the whole integration.
2. **$\lambda$ must be an estimate.** For a nonlinear problem the relevant
   quantity is the largest eigenvalue of the Jacobian $\partial f/\partial y$
   along the trajectory. Quoting a stiffness ratio without saying how the
   Jacobian was estimated is not a statement.
3. **Order is asymptotic.** The measured orders 2.84 and 3.30 for RK4 at coarse
   steps are not evidence of a lower order, but they are evidence that a
   convergence study must reach the asymptotic range before its numbers mean
   anything.

## 6. Python demonstration

`code/ode_solvers.py` implements the five methods, the adaptive step-doubling
controller and the three geophysical problems, and measures every order it
quotes. Selected output:

```text
  y' = -y, y(0) = 1, exact y(1) = 0.36787944117144233  (non-stiff, lambda = 1)
      n            Euler             Heun              RK4   backward Euler      trapezoidal
     40        4.647e-03        3.905e-05        1.223e-09        4.551e-03        1.916e-05
    320        5.756e-04        6.002e-07        2.933e-13        5.741e-04        2.994e-07
  measured orders (final ratio):
              Euler:   1.00     Heun:   2.01      RK4:   4.01
   backward Euler:   1.00  trapezoidal:   2.00

  Growth per step at the limit, model problem y' = -lambda y:
           h    |1 - lambda h|    measured ratio    difference
      0.0399          0.995000          0.995000      0.00e+00
      0.0401          1.005000          1.005000      0.00e+00
      0.0600          2.000000          2.000000      0.00e+00

          h    explicit Euler    backward Euler     trapezoidal
     0.2500         1.753e+04         1.583e-03       2.749e-01
     0.5000         5.788e+02         4.863e-03       7.253e-01

        tol   steps  rejected   final error   error/tol   slope
      1e-04      55        14     4.566e-03       45.66       -
      1e-06     658        19     4.690e-04      469.03    0.49
      1e-08    6704        22     4.369e-05     4368.55    0.52
```

### What to observe, and why it matters

| Observation | Consequence |
|---|---|
| Orders 1, 2, 4 for explicit, 1 and 2 for implicit | implicitness changes stability, not order |
| Multiplier equals $\lvert1-\lambda h\rvert$ to $10^{-18}$ | the instability is predicted, and the threshold is exactly $2/\lambda$ |
| Trapezoidal worse than backward Euler at $h=0.5$ | A-stability without L-stability lets the fast mode ring |
| Adaptive meets tolerance on $y'=y^2$ | step doubling works when the error model is right |
| Adaptive misses the tolerance by $3\,000\times$ when stiff | the estimator controls the wrong term; slopes 0.49 and 0.52 |
| Uniform RK4 beats adaptive on the stiff problem | the fix is a better method, not a smaller safety factor |
| RK4 orders 2.84 → 3.96 as $n$ grows | orders must be measured in the asymptotic range |

> **Breaking exercise.** Change `lam` in `report_stiffness` from 50 to 5 and
> predict, before running, the new explicit-Euler stability limit and the number
> of steps it implies for $[0,1]$. Then run it and check the error table's verdict
> column against your prediction.

## 7. Common mistakes

1. **Treating the stability limit as advice.** Above $h=2/\lambda$ the error grows
   by exactly $|1-\lambda h|$ per step, without limit. The scheme does not
   degrade; it fails.
2. **Choosing an explicit method because it is accurate.** Order is irrelevant to
   stability. A fourth-order explicit method has a *finite* stability region too.
3. **Using the trapezoidal rule on a stiff transient and blaming the physics.**
   The ringing is the stability function's limit approaching $-1$.
4. **Believing an adaptive stepper honours its tolerance.** Measured failures by
   factors of 45 to 4369 on a stiff problem, with the error scaling as
   $\mathrm{tol}^{0.5}$.
5. **Measuring an order at coarse steps.** RK4 reports 2.84 at $n=10$; the order
   is 4. Refine until the order is stable before quoting it.
6. **Ignoring round-off in very long integrations.** A symplectic or
   energy-preserving scheme is needed for millions of steps; RK4 drifts in energy
   and the drift, not the local error, becomes the limiting factor.
7. **Forgetting that a system's step limit is set by its fastest mode.** A single
   stiff component forces the whole integration to take small steps, and that is
   the definition of stiffness in practice.

## 8. Real-world applications

- **Thermal evolution of the lithosphere and of sedimentary basins.** Diffusion
  problems are stiff whenever the grid is fine, and implicit time stepping is
  standard; [01-09-02](../09-partial-differential-equations/02-heat-equation.md)
  gives the diffusive timescale that sets the physical step of interest.
- **Geochronology.** Decay chains with half-lives spanning many orders of
  magnitude are the textbook stiff system, and the concentration of the
  intermediate nuclides determines whether a dating method is usable.
- **Seismic and engineering seismology.** Ground-motion simulation with
  rate-and-state friction or viscoelastic rheology produces stiff systems; the
  oscillation and energy checks of §4.3 are the standard validation.
- **Geodynamics.** Mantle convection couples a stiff temperature-dependent
  viscosity to a slow flow; the stiffness ratio is the ratio of viscosities, and
  implicit or semi-implicit schemes are mandatory. See
  [19 Numerical Modeling and HPC](../../19-numerical-modeling-hpc/README.md).
- **Orbital and satellite dynamics.** Symplectic integrators for long-term
  integration of satellite orbits, where energy drift — not local error — is the
  quantity that matters.

## 9. Further reading

- **Hairer, E., Nørsett, S. P., & Wanner, G. (1993). *Solving Ordinary
  Differential Equations I: Nonstiff Problems* (2nd ed.). Springer.** Level:
  graduate. The reference for order conditions, step-size control and the design
  of embedded Runge–Kutta pairs.
- **Hairer, E., & Wanner, G. (1996). *Solving Ordinary Differential Equations II:
  Stiff and Differential-Algebraic Problems* (2nd ed.). Springer.** Level:
  graduate. A-stability, L-stability and the stiff error analysis that §3.5
  measures.
- **Butcher, J. C. (2016). *Numerical Methods for Ordinary Differential
  Equations* (3rd ed.). Wiley.** Level: graduate. The complete theory, including
  the order barrier quoted in §3.1.
- **Press, W. H., Teukolsky, S. A., Vetterling, W. T., & Flannery, B. P. (2007).
  *Numerical Recipes* (3rd ed.). Cambridge University Press.** Level: advanced
  undergraduate to graduate. The practical chapter on stiff sets and the
  Rosenbrock methods that production codes use.
- **Sussman, G. J., & Wisdom, J. (2001). *Structure and Interpretation of
  Classical Mechanics*. MIT Press.** Level: undergraduate to graduate. The
  clearest discussion of symplectic integration and energy behaviour for
  oscillatory systems.

> Note on citations: bibliographic details are given so you can locate the works.
> This repository does not host or reproduce copyrighted text; confirm current
> editions and availability through your library before citing.

## 10. Exercises

Full statements and difficulty grading are in
[`exercises/06-ode-solvers-exercises.md`](./exercises/06-ode-solvers-exercises.md),
with worked solutions in
[`exercises/06-ode-solvers-solutions.md`](./exercises/06-ode-solvers-solutions.md).

**★1.** Compute the exact solution and one Euler step for $y'=-3y$, $y(0)=2$ at
$h=0.1$, and state the exact error.

**★2.** Derive the stability limit of Heun's method and compare it with Euler's.

**★3.** Show that backward Euler is L-stable and that the trapezoidal rule is not.

**★4.** For $\lambda=50\ \mathrm{s^{-1}}$, how many explicit Euler steps are
needed to integrate $t\in[0,1]$ at the stability limit? What is the error?

**★★5.** Derive the amplification factor of the implicit trapezoidal rule,
sketch $|R(z)|$ on the negative real axis, and explain the ringing at large $h$.

**★★6.** Show that the two-step Adams–Bashforth method is order 2 and state its
stability interval, then compare with Heun.

**★★7.** A code uses RK4 with $h=10^{-3}$ s on a problem whose Jacobian has an
eigenvalue $-2\times10^{4}$. Show that the scheme is unstable, and compute the
step that would be stable.

**★★8.** Reproduce the adaptive failure of §3.5 conceptually: explain what the
step-doubling estimate is measuring when $\lambda h \approx 1$ and why it is
smaller than the true error.

**★★★9.** Implement a semi-implicit scheme for the damped oscillator (implicit in
the damping term, explicit in the restoring force) and measure both its order and
its stability limit. Report the numbers and the trade-off.

**★★★10.** A geothermal forward model is reported to run with explicit Euler at
a step of one year, on a system whose fastest relaxation time is one month.
Diagnose the report, predict the observed behaviour, and state the two remedies
in order of preference with their costs.

## 11. Self-assessment checklist

- [ ] I can derive the order of a one-step method from its local truncation error.
- [ ] I can derive the stability limit $2/\lambda$ and predict the growth above it.
- [ ] I can state the stability function of Euler, backward Euler and the
      trapezoidal rule, and classify each by A-stability and L-stability.
- [ ] I can explain why an implicit method can be more accurate at a large step
      than an explicit method at a small one.
- [ ] I can describe step doubling and state what it estimates.
- [ ] I can explain, with the measured numbers, why the estimator fails on a
      stiff problem and what to do instead.
- [ ] I can validate an oscillator integration by comparing its energy against the
      closed-form energy, and say why that check catches instabilities a residual
      check misses.

## Related lessons

- [01-12-05 Direct vs Iterative Linear Solvers and Convergence](./05-linear-solvers.md)
  — the linear solve inside every implicit step and every Newton iteration of an
  implicit method.
- [01-12-07 Discretising PDEs: Consistency, Stability, Convergence](./07-pde-discretisation.md)
  — the same stability analysis in the presence of a spatial discretisation.
- [01-12-03 Numerical Differentiation and Finite-Difference Stencils](./03-numerical-differentiation.md)
  — the stencils used when the right-hand side requires spatial derivatives.
- [01-08-07 Stiff Systems and Numerical Stability Challenges](../08-ordinary-differential-equations/07-stiff-systems.md)
  — the mathematical treatment of stiffness that this lesson solves numerically.
- [14 Optimization](../14-optimization/README.md) — the Newton iteration used
  inside each implicit step, and its convergence criteria.
- [19 Numerical Modeling and HPC](../../19-numerical-modeling-hpc/README.md) —
  time-stepping choices in production geodynamics and climate codes.
