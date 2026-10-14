---
id: 01-12-07
title: "Discretising PDEs: Consistency, Stability, Convergence"
level: graduate
prereqs: ["01-05-04", "01-09-01", "01-09-03"]
estimated_minutes: 90
tags: [numerical-methods, pde-discretisation, stability, cfl, von-neumann]
---

# Discretising PDEs: Consistency, Stability, Convergence

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** consistency, stability and convergence for a linear finite-difference
   scheme, and state the Lax equivalence theorem precisely.
2. **Derive** the local truncation error of the FTCS heat scheme from Taylor
   expansions, and its amplification factor from a von Neumann substitution.
3. **Carry out** a von Neumann stability analysis for any constant-coefficient
   linear scheme, and interpret the result physically.
4. **Derive** the CFL condition for the leapfrog wave scheme and the upwind
   advection scheme, and predict the growth rate when it is violated.
5. **Explain** why the centred-difference advection scheme is unstable for *every*
   step size, and what stabilisation costs.
6. **Measure** convergence orders under refinement and explain why the heat
   equation forces $\Delta t \sim \Delta x^2$ while a wave equation does not.

## Prerequisites

[01-05-04 Taylor Series](../05-single-variable-calculus/04-taylor-series.md),
[01-09-01 Classification of PDEs](../09-partial-differential-equations/01-classification.md)
and [01-09-03 The Wave Equation and Its Physical Content](../09-partial-differential-equations/03-wave-equation.md)
— which already derives the CFL condition from the domain of dependence. This
lesson adds the Fourier (von Neumann) analysis, the equivalence theorem, and
measured convergence rates.

## 1. Intuition: three words that must not be confused

- **Consistency** says the scheme *is trying to solve the right equation*: as the
  grid is refined, the difference between the scheme and the PDE vanishes. It is
  a local, algebraic property and it is easy to verify.
- **Stability** says the scheme *does not amplify error*: the amplification
  factor of every Fourier mode stays bounded as the number of steps grows. It is
  a property of the scheme and the step ratio, and it is the binding constraint in
  practice.
- **Convergence** says the computed solution *approaches the true solution*. It is
  what you actually want, and for a linear problem it follows from the other two.

The single most useful theorem in numerical PDEs is the statement that ties them
together:

> **Lax equivalence theorem.** For a consistent linear finite-difference scheme
> approximating a well-posed linear initial-value problem, stability is necessary
> and sufficient for convergence, and the convergence order equals the order of
> the local truncation error.

The practical force of the theorem is that consistency is almost always easy and
*stability is almost always the hard part*. So the working method is: verify
consistency algebraically, prove stability by Fourier analysis, and then claim
convergence — and confirm with a measured refinement study, because the theorem
is an asymptotic statement and codes have bugs.

## 2. Precise definitions

### 2.1 The model problems and their schemes

**Diffusion**, $u_t = \kappa u_{xx}$ on $(0,1)$ with $u=0$ at both ends. The
explicit forward-time centred-space (FTCS) scheme with $r = \kappa\Delta t/\Delta x^2$ is

$$u_i^{n+1} = u_i^n + r\left(u_{i-1}^n - 2u_i^n + u_{i+1}^n\right).$$

The implicit **Crank–Nicolson** scheme averages the spatial operator between the
old and new time levels, giving a tridiagonal system at each step.

**Wave propagation**, $u_{tt}=c^2u_{xx}$. The leapfrog scheme with Courant number
$\sigma = c\Delta t/\Delta x$ is

$$u_i^{n+1} = 2u_i^n - u_i^{n-1} + \sigma^2\left(u_{i-1}^n - 2u_i^n
+ u_{i+1}^n\right).$$

**Advection**, $u_t + cu_x = 0$. Forward Euler in time with an **upwind** spatial
difference is

$$u_i^{n+1} = u_i^n - \sigma\left(u_i^n - u_{i-1}^n\right),$$

and with a **centred** spatial difference

$$u_i^{n+1} = u_i^n - \tfrac{\sigma}{2}\left(u_{i+1}^n - u_{i-1}^n\right).$$

All three are parameterised by a single ratio, and that ratio is what the
stability condition constrains.

### 2.2 Local truncation error

Substitute the exact solution into the scheme and expand. The residual is the
**local truncation error** (LTE). A scheme is **consistent** if
$\text{LTE}\to0$ as the grid is refined, of order $p$ in space and $q$ in time if
$\text{LTE} = O(\Delta x^p) + O(\Delta t^q)$.

### 2.3 von Neumann stability

Take the scheme on an infinite uniform grid, and substitute the Fourier mode

$$u_i^n = G^n\,\mathrm e^{\mathrm i\theta i}, \qquad \theta = k\Delta x \in[-\pi,\pi].$$

The scheme reduces to $G(\theta)$ times the mode, because the operator is
constant-coefficient and the grid is uniform. The scheme is **stable** if
$|G(\theta)|\le1$ for every $\theta$; the condition $|G(\theta)|\le 1+\epsilon
\Delta t$ gives **practical** stability. $G$ is the **amplification factor**, and
$\theta=\pi$ — the Nyquist mode, alternating sign from cell to cell — is almost
always the worst case. For a two-level scheme in time the ansatz gives a
quadratic for $G$, and stability means both roots satisfy $|G|\le1$.

## 3. Derivations

### 3.1 Consistency of FTCS

Expanding about $(t_n,x_i)$,

$$\frac{u^{n+1}_i-u^n_i}{\Delta t} = u_t + \frac{\Delta t}{2}u_{tt} + O(\Delta t^2),
\qquad
\frac{u^n_{i+1}-2u^n_i+u^n_{i-1}}{\Delta x^2} = u_{xx}
+ \frac{\Delta x^2}{12}u_{xxxx}+O(\Delta x^4).$$

Subtracting $\kappa$ times the second from the first gives

$$\text{LTE} = \frac{\Delta t}{2}u_{tt} - \frac{\kappa\Delta x^2}{12}u_{xxxx}
+ O(\Delta t^2,\Delta x^4) = O(\Delta t) + O(\Delta x^2).$$

So FTCS is consistent, first order in time and second order in space. Since
$u_{tt} = \kappa u_{xxxx}$ for a solution of the heat equation, the two terms are
of the same order whenever $\Delta t \sim \Delta x^2$ — and that is exactly the
relationship stability will force.

### 3.2 von Neumann analysis of FTCS

Substituting the mode into the scheme and dividing by $G^n\mathrm e^{\mathrm
i\theta i}$ gives

$$G = 1 + r\left(\mathrm e^{-\mathrm i\theta}-2+\mathrm e^{\mathrm i\theta}\right)
= 1 - 2r(1-\cos\theta) = 1 - 4r\sin^2\frac{\theta}{2}.$$

This is real, so stability requires $-1\le G\le1$. The lower bound at
$\theta=\pi$ (where $\sin^2(\theta/2)=1$) gives

$$1-4r \ge -1 \quad\Longleftrightarrow\quad r \le \tfrac12 .$$

The demonstration measures $G$ directly by taking one step on the highest mode
$\sin((n-1)\pi x)$ of a grid of 40 cells and comparing the max norm ratio with
$|1-4r\sin^2(\theta/2)|$:

| $r$ | prediction | measured | max $\lvert u\rvert$ after 20 steps | verdict |
|---|---|---|---|---|
| 0.40 | 0.597534 | 0.597534 | $3.37\times10^{-5}$ | stable |
| 0.50 | 0.996917 | 0.996917 | $9.40\times10^{-1}$ | marginal |
| 0.51 | 1.036856 | 1.036856 | $2.06$ | unstable |
| 0.80 | 2.195068 | 2.195068 | $6.75\times10^{6}$ | unstable |

The measured factor equals the prediction to every digit printed. Two features
are worth extracting. First, the stability limit is a limit on the *ratio*
$\kappa\Delta t/\Delta x^2$: refining the grid requires $\Delta t$ to shrink as
$\Delta x^2$, which is the practical cost of an explicit diffusion solver.
Second, at $r$ exactly $\tfrac12$ the factor is $-1$: the mode neither grows nor
decays but alternates in sign, producing the classic sawtooth. Marginal stability
is not accuracy.

### 3.3 Convergence and the order a refinement study sees

With $r$ fixed at 0.4 (so $\Delta t = 0.4\Delta x^2$) and a manufactured solution
$u = \mathrm e^{-\pi^2t}\sin \pi x$, the measured errors on $[0,0.05]$ are
$3.454\times10^{-3}$ at $n=10$ falling to $1.355\times10^{-5}$ at $n=160$, with
orders 1.99, 2.00, 2.00, 2.00. Since $\Delta t \sim \Delta x^2$, the first-order
time error is $O(\Delta x^2)$ and the observed order is 2 — the two terms are
balanced, and the theorem's claim that the convergence order equals the
truncation order is visibly satisfied.

Crank–Nicolson, refining $\Delta x$ and $\Delta t$ together, also measures order
2.00. At $r=5$ — ten times the explicit stability limit — it produces
$1.31\times10^{-4}$ where FTCS blows up to $1.08\times10^{4}$: unconditional
stability in exchange for a tridiagonal solve per step, as
[01-12-05](./05-linear-solvers.md) prices it.

### 3.4 The CFL condition for the wave equation

The leapfrog ansatz gives, after dividing by $G^{n}\mathrm e^{\mathrm i\theta i}$,

$$G^2 - 2aG + 1 = 0, \qquad a = 1 - 2\sigma^2\sin^2\frac{\theta}{2},$$

so $G = a \pm\sqrt{a^2-1}$. If $|a|\le1$ the roots are a complex-conjugate pair
on the unit circle and $|G|=1$: the scheme is neutral, which is exactly what a
wave equation requires. If $|a|>1$ the roots are real and one exceeds 1 in
modulus. The worst case is again $\theta=\pi$:

$$|a|>1 \iff |1-2\sigma^2|>1 \iff \sigma>1 .$$

The measured growth per step over a 60-step run on the Nyquist mode:

| $\sigma$ | $\lvert G\rvert$ predicted | measured growth per step | verdict |
|---|---|---|---|
| 0.50 | 1.00000000 | 1.00000000 | stable |
| 0.99 | 1.00000000 | 0.99754175 | stable |
| 1.00 | 1.00000000 | 1.00000000 | neutral |
| 1.01 | 1.32658443 | 1.32658443 | unstable |
| 1.05 | 1.87732804 | 1.87732804 | unstable |

The measured growth reproduces the unstable root to eight digits — an
unambiguous identification of the mechanism. As in
[01-09-03](../09-partial-differential-equations/03-wave-equation.md), the same
condition follows from the domain of dependence: information cannot travel more
than one cell per time step, so $\sigma\le1$ is the statement that the numerical
domain of dependence contains the physical one.

Refining with $\sigma$ fixed at 0.5 gives measured orders 1.95, 1.98 and 1.99 —
second order, because the leapfrog stencil is second order in both $\Delta x$ and
$\Delta t$ and holding the Courant number fixed refines both together. **This is
the structural difference from the heat equation**: an explicit diffusive scheme
is *forced* to $\Delta t\sim\Delta x^2$, an explicit hyperbolic scheme only needs
$\Delta t \sim \Delta x$.

### 3.5 Why central differences for advection are unconditionally unstable

For $u_t + cu_x = 0$ with forward Euler in time and central differences in space,

$$G = 1 - \mathrm i\sigma\sin\theta \quad\Longrightarrow\quad
|G|^2 = 1 + \sigma^2\sin^2\theta > 1 \quad\text{for every }\sigma>0,\ \theta\ne0.$$

There is no step size that makes this stable: reducing $\Delta t$ only slows the
divergence. The demonstration confirms $|G|$ measured equals $|G|$ predicted for
every combination tried, e.g. 1.11803399 at $\sigma=0.5$, $\theta=\pi/2$. The
upwind scheme has

$$|G|^2 = 1 - 2\sigma(1-\sigma)(1-\cos\theta),$$

which is $\le1$ exactly when $0\le\sigma\le1$ — conditionally stable with the
same CFL limit, and only first order. The general lesson is that the *symmetric*
discretisation is the unstable one, and that the cure (upwinding, artificial
dissipation, or a more careful time integration such as Lax–Wendroff) always
costs either order or an energy-like quantity.

## 4. Physical interpretation

Each stability condition has a physical reading, and reading it that way is what
turns the algebra into intuition.

- **$r\le\tfrac12$ for the heat equation** says that the diffusive spread per time
  step must not exceed what the grid can carry: $\sqrt{2\kappa\Delta t}\lesssim
  \Delta x$, since the fundamental solution spreads as $\sqrt{\kappa t}$.
- **$\sigma\le1$ for the wave equation** says the numerical domain of dependence
  must contain the physical one. A physical wave moves $c\Delta t$; the stencil
  reaches $\Delta x$.
- **Upwind vs centred advection** says that a scheme must "look" in the direction
  the information travels. Central differences look both ways and therefore carry
  information backwards, which the forward Euler step then converts into growth.
- **The Nyquist mode being the worst case** says that the least resolvable
  structure determines the step limit. A grid that cannot resolve a feature
  cannot be trusted to carry it either.

## 5. Assumptions and regime of validity

| Statement | Requires |
|---|---|
| von Neumann analysis gives the stability condition | constant coefficients, uniform grid, linear scheme, and that a single Fourier norm controls the norm of interest |
| The measured order equals the design order | refinement in the asymptotic range; a smooth exact solution; a grid-aligned initial condition |
| Lax equivalence gives convergence | linearity, consistency, stability, and a well-posed problem |
| Crank–Nicolson is stable for any $\Delta t$ | $A$ has no eigenvalues with positive real part; it is not L-stable (see [01-12-06](./06-ode-solvers.md)) |
| The measured $\lvert G\rvert$ equals the prediction | the mode is an exact eigenvector of the scheme on the grid used (periodic, or the highest Dirichlet mode) |

Three omissions deserve explicit mention, because the analysis above is a
*local* one.

1. **Boundary conditions.** von Neumann analysis says nothing about boundaries.
   An unstable boundary treatment destabilises a scheme that is interior-stable,
   and it does so with a growth rate the interior analysis never sees.
2. **Variable coefficients and nonlinearity.** Real media are heterogeneous and
   velocities vary. The stability condition becomes a condition on the *worst*
   ratio over the grid — the reason production CFL conditions are local,
   $\max_i c_i\Delta t/\Delta x \le 1$ — and nonlinear schemes need entropy
   conditions for reasons the linear analysis cannot supply.
3. **The norm.** von Neumann analysis bounds the $\ell^2$ norm of each Fourier
   mode. Other norms (maximum norm, energy) may grow more slowly, less slowly, or
   not at all; the analysis is a statement about one norm, and for practical work
   that is usually the right one.

A fourth point is about what stability does *not* buy. A stable scheme can still
be inaccurate — Crank–Nicolson at $r=5$ is stable and returns a solution whose
error is set by $\Delta t$, not by stability. And a stable scheme can still be
non-dissipative in an unwanted way: the leapfrog scheme carries a spurious
computational mode (the second root of the quadratic), which must be damped at
startup and can be excited by boundary conditions or forcing.

## 6. Python demonstration

`code/pde_discretisation.py` implements FTCS, Crank–Nicolson, leapfrog wave and
both advection schemes, and measures amplification factors and convergence orders.
Selected output:

```text
         r    |G| prediction     measured/step    max |u| after 20 steps     verdict
      0.40          0.597534          0.597534                 3.367e-05      stable
      0.50          0.996917          0.996917                 9.401e-01      stable
      0.51          1.036856          1.036856                 2.062e+00    UNSTABLE
      0.80          2.195068          2.195068                 6.745e+06    UNSTABLE

       n        dx     max error at t = 0.05   order
      10    0.1000                 3.454e-03
      40    0.0250                 2.170e-04    2.00
     160    0.0063                 1.355e-05    2.00

     sigma   a = 1-2s^2sin^2  |G| max theory   amplitude x60  late growth/step    verdict
     0.500          0.500000      1.00000000      1.0000e+00        1.00000000     stable
     1.000         -1.000000      1.00000000      1.0000e+00        1.00000000     stable
     1.010         -1.040200      1.32658443      1.3267e+07        1.32658443   UNSTABLE
     1.050         -1.205000      1.87732804      1.7363e+16        1.87732804   UNSTABLE

     sigma   theta     |G| central    |G| upwind  measured central   measured upwind
      0.50  1.5708      1.11803399    0.70710678        1.11803399        0.70710678
      1.00  1.5708      1.41421356    1.00000000        1.41421356        1.00000000
```

### What to observe, and why it matters

| Observation | Consequence |
|---|---|
| Measured $G$ equals $|1-4r\sin^2(\theta/2)|$ exactly | the von Neumann factor is a property of the scheme, verifiable to round-off |
| $r=0.5$ gives $G=-1$, bounded sawtooth | marginal stability is not accuracy |
| FTCS order 2 with $\Delta t\sim\Delta x^2$ | the forced time-step scaling balances the two truncation terms |
| Crank–Nicolson stable at $r=5$ | unconditional stability buys the step restriction at the cost of a solve |
| Measured wave growth 1.32658443 at $\sigma=1.01$ | the instability is the identified root, not numerical noise |
| Leapfrog order 2 at fixed $\sigma$ | hyperbolic schemes need only $\Delta t\sim\Delta x$ |
| Central advection $\lvert G\rvert>1$ for all $\sigma$ | no step size fixes an unconditionally unstable scheme |
| Upwind $\lvert G\rvert\le1$ exactly for $\sigma\le1$ | the CFL condition appears from the algebra, not from a picture |

> **Breaking exercise.** In `report_heat_stability`, change the initial condition
> from the highest mode to the *lowest* mode $u=\sin(\pi x)$ and predict, before
> running, what the measured per-step factor will be at $r=0.4$. Then run it and
> explain why the stability limit is invisible in that measurement.

## 7. Common mistakes

1. **Refining the grid to fix an unstable scheme.** Stability is set by the ratio
   $r$ or $\sigma$; halving $\Delta x$ while keeping $\Delta t$ makes things worse,
   not better.
2. **Using central differences for advection "because they are second order".**
   They are unconditionally unstable with forward Euler. Order is worthless
   without stability.
3. **Assuming the interior analysis covers the boundaries.** von Neumann says
   nothing about boundary conditions, and unstable boundaries are a common
   failure in production codes.
4. **Reading "unconditionally stable" as "unconditionally accurate".**
   Crank–Nicolson is stable at any step and first-order-in-time accurate at large
   steps.
5. **Testing convergence by halving $\Delta x$ only.** Convergence order depends on
   how $\Delta t$ is tied to $\Delta x$. Report both, or fix the ratio and say so.
6. **Forgetting the spurious mode of a multistep scheme.** Leapfrog carries two
   roots; the physical one and a computational one. Startup and boundary handling
   must not excite the second.
7. **Quoting a CFL number without saying what velocity it used.** With variable
   velocity the condition is a maximum over the grid, and the maximum may be at a
   cell you did not think about.

## 8. Real-world applications

- **Seismic wave modelling.** Every finite-difference code carries a CFL check,
  usually as a hard assertion. The 1.327 growth factor per step for a Courant
  number 1% above the limit is why the check is a crash rather than a warning: a
  1 000-step run amplifies round-off by $10^{122}$.
- **Reservoir simulation.** Diffusion-dominated pressure and saturation equations
  are solved implicitly, because the explicit stability requirement
  $\Delta t\sim\Delta x^2$ is prohibitive at reservoir grid spacing.
- **Groundwater and contaminant transport.** Upwind and TVD-limited schemes are
  standard precisely because centred advection is unconditionally unstable; the
  choice of limiter is a choice of how much numerical diffusion to accept.
- **Glacial and mantle flow.** Stokes problems are elliptic and are solved
  implicitly, but the advected temperature field is hyperbolic and needs a
  stabilised scheme; mixing the two in one code is where most CFL bugs occur.
- **Atmospheric and oceanic models.** Semi-implicit and split-explicit schemes
  exist to avoid the acoustic and gravity-wave CFL limits while keeping the
  advective step economical. See [16 Atmosphere and Climate](../../16-atmosphere-climate/README.md).
- **Magnetotellurics and EM induction.** The diffusive regime gives $r$-type
  limits; the wave regime (GPR) gives CFL limits. The same rock and the same grid
  can be in either regime depending on frequency, as
  [01-09-01](../09-partial-differential-equations/01-classification.md) notes.

## 9. Further reading

- **Richtmyer, R. D., & Morton, K. W. (1967). *Difference Methods for Initial
  Value Problems* (2nd ed.). Interscience.** Level: graduate. The classical
  source for the Lax equivalence theorem and the von Neumann analysis.
- **Strikwerda, J. C. (2004). *Finite Difference Schemes and Partial Differential
  Equations* (2nd ed.). SIAM.** Level: graduate. The clearest modern treatment,
  with the stability analysis of every scheme in this lesson.
- **LeVeque, R. J. (2007). *Finite Difference Methods for Ordinary and Partial
  Differential Equations*. SIAM.** Level: graduate. Particularly good on
  boundary conditions and on why the interior analysis is insufficient.
- **Lax, P. D., & Richtmyer, R. D. (1956). Survey of the stability of linear
  finite difference equations. *Communications on Pure and Applied Mathematics*,
  9, 267–293.** Level: graduate. The original equivalence theorem.
- **Gustafsson, B., Kreiss, H.-O., & Oliger, J. (1995). *Time Dependent Problems
  and Difference Methods*. Wiley.** Level: graduate. The full theory, including
  the stability theory for variable coefficients that §5 flags.

> Note on citations: bibliographic details are given so you can locate the works.
> This repository does not host or reproduce copyrighted text; confirm current
> editions and availability through your library before citing.

## 10. Exercises

Full statements and difficulty grading are in
[`exercises/07-pde-discretisation-exercises.md`](./exercises/07-pde-discretisation-exercises.md),
with worked solutions in
[`exercises/07-pde-discretisation-solutions.md`](./exercises/07-pde-discretisation-solutions.md).

**★1.** Derive the local truncation error of FTCS and state its order in
$\Delta x$ and $\Delta t$.

**★2.** Show that the leapfrog wave scheme is consistent to second order in both
variables.

**★3.** For $\kappa = 10^{-6}\ \mathrm{m^2\,s^{-1}}$ and $\Delta x = 10$ m,
compute the maximum explicit time step.

**★4.** Carry out the von Neumann analysis of the upwind advection scheme and
obtain the CFL condition.

**★★5.** Show that the centred advection scheme with forward Euler is
unconditionally unstable, and compute $\lvert G\rvert$ at $\sigma=0.5$,
$\theta=\pi/2$.

**★★6.** Obtain the amplification factor of Crank–Nicolson for the heat equation
and show $|G|\le1$ for all $r>0$. Sketch $|G|$ against $\theta$ for $r=0.5$ and
$r=5$.

**★★7.** Derive the Lax–Wendroff scheme for advection from a Taylor expansion in
time and show that it is second order with $\lvert G\rvert\le1$ for
$\sigma\le1$.

**★★8.** A code uses FTCS with $\Delta x = 2$ m, $\kappa = 10^{-7}\
\mathrm{m^2\,s^{-1}}$ and $\Delta t = 30$ s. Compute $r$, state whether it is
stable, and give the largest stable $\Delta t$.

**★★★9.** Implement and measure the order of convergence of the leapfrog wave
scheme for a *travelling* (non-standing) initial condition, with and without a
damped startup. Report the measured orders and the effect of the startup on the
spurious mode.

**★★★10.** A modelling code crashed with a CFL violation after 400 time steps
although the reported Courant number was 0.85. Using §5, list the three most
likely causes and the diagnostic that would distinguish them, and state why the
reported number can be misleading.

## 11. Self-assessment checklist

- [ ] I can define consistency, stability and convergence and state the Lax
      equivalence theorem.
- [ ] I can carry out a von Neumann analysis for any constant-coefficient linear
      two- or three-level scheme.
- [ ] I can derive the FTCS condition $r\le\tfrac12$ and the wave condition
      $\sigma\le1$.
- [ ] I can explain why the heat equation forces $\Delta t\sim\Delta x^2$ and the
      wave equation does not.
- [ ] I can predict the growth rate above a stability limit, and I have checked a
      prediction numerically.
- [ ] I can explain why central-difference advection is unconditionally unstable
      and what upwinding costs.
- [ ] I can state three things von Neumann analysis does not cover.

## Related lessons

- [01-12-06 Numerical ODE Solvers: Euler, Runge-Kutta, Implicit and Adaptive](./06-ode-solvers.md)
  — the same stability question in a single variable, where A-stability can be
  stated exactly.
- [01-12-03 Numerical Differentiation and Finite-Difference Stencils](./03-numerical-differentiation.md)
  — the stencils assembled here into a scheme, and the source of the truncation
  terms.
- [01-12-05 Direct vs Iterative Linear Solvers and Convergence](./05-linear-solvers.md)
  — the solve inside every implicit step.
- [01-09-03 The Wave Equation and Its Physical Content](../09-partial-differential-equations/03-wave-equation.md)
  — the CFL condition from the domain of dependence, and the physical content of
  the wave scheme.
- [01-09-07 Boundary and Initial-Boundary Value Problems](../09-partial-differential-equations/07-boundary-value-problems.md)
  — well-posedness, and the boundary treatment this lesson's analysis omits.
- [19 Numerical Modeling and HPC](../../19-numerical-modeling-hpc/README.md) —
  these schemes as production codes, with stability checks, boundary conditions
  and parallelism.
