---
id: 01-09-07
title: "Boundary and Initial-Boundary Value Problems"
level: graduate
prereqs: ["01-09-02", "01-09-05"]
estimated_minutes: 90
tags: [partial-differential-equations, boundary-conditions, well-posedness, energy-methods, absorbing-boundaries]
---

# Boundary and Initial-Boundary Value Problems

## Learning objectives

By the end of this lesson you will be able to:

1. **State** Hadamard's three conditions for a well-posed problem and apply them
   to a specific initial-boundary value problem.
2. **Count** the boundary and initial conditions each class requires, and justify
   the count from the characteristics rather than from convention.
3. **Classify** the standard boundary conditions — Dirichlet, Neumann, Robin,
   radiation, free surface, interface — and say what each asserts physically.
4. **Prove** uniqueness and stability for the heat and wave initial-boundary value
   problems using energy methods, and interpret monotone energy decay.
5. **Implement** a boundary condition to the same order as the interior scheme,
   and show that a one-sided difference destroys the global order.
6. **Demonstrate** that the backward heat problem is ill posed, quantify the noise
   amplification, and explain why regularisation, not a better algorithm, is the
   response.
7. **Distinguish** reflecting from radiating wave boundaries and measure the
   residual reflection of a first-order absorbing condition.

## Prerequisites

- [01-09-05 Separation of Variables and Boundary Conditions](./05-separation-of-variables.md)
  — the boundary-condition types in the context of an explicit solution.
- [01-09-02 The Diffusion/Heat Equation and Diffusive Timescales](./02-heat-equation.md)
  — the parabolic equation used throughout.
- [01-09-01 Classification of PDEs](./01-classification.md) — why the classes
  differ in the data they require.
- [01-06-06 Gauss, Stokes and Green Theorems](../06-multivariable-calculus/06-integral-theorems.md)
  — the divergence theorem, used in the energy proofs.

## 1. Intuition: a PDE is only half of a problem

An equation on its own has infinitely many solutions. A *problem* is an equation
plus enough auxiliary data to single one out, and the interesting question is what
"enough" means. The answer is supplied by the classification of
[01-09-01](./01-classification.md), and it is one of the most practically useful
facts in applied mathematics: **if you get the count wrong, the problem either has
no solution or has infinitely many, and no numerical scheme can repair that.**

Three things must be true for a problem to be usable
(**well posedness** in the sense of Hadamard):

1. **Existence** — at least one solution exists.
2. **Uniqueness** — at most one solution exists.
3. **Stability** — the solution depends continuously on the data: a small change
   in the data produces a small change in the solution, measured in a stated norm.

Condition 3 is the one that is habitually forgotten and the one that decides
whether a computation is meaningful. Section 6 shows a problem that satisfies (1)
and (2) but fails (3) so badly that no finite-precision computation can solve it.

## 2. How many conditions, and where

| Class | Time order | Boundary conditions | Initial conditions | Typical problem |
|---|---|---|---|---|
| Elliptic | none | one on **every** boundary point | none | Dirichlet/Neumann/Robin |
| Parabolic | first in $t$ | one at each spatial boundary, for $t>0$ | one (the state) | initial-boundary value |
| Hyperbolic | second in $t$ | one per **incoming** characteristic at each boundary | two (state and velocity) | Cauchy or initial-boundary value |
| First order | first | one per incoming characteristic | one | inflow/outflow transport |

The counts follow from the characteristics, not from a table:

- **Elliptic has no characteristics**, so no direction is special and no boundary
  point is different from any other: every boundary point must carry data, and
  exactly one condition per point (two would overspecify, none would underdetermine).
- **Parabolic has one characteristic family**, which is the family of lines of
  constant $x$ in $(x,t)$. At the initial surface $t=0$ the state must be given;
  at each spatial boundary the single characteristic *entering* the domain must
  carry a condition. Because the characteristics of the diffusion equation are
  degenerate (all parallel to the $x$-axis), this resolves to the familiar rule:
  one condition at each end, for all $t>0$.
- **Hyperbolic has two families**, so a boundary point can have two incoming
  characteristics, one, or none. The count is one condition **per incoming
  characteristic**. On a subsonic inflow boundary there is one incoming and one
  outgoing characteristic, so one condition is required and the other quantity
  must be computed; on an outflow boundary none is required. This is the rule that
  is routinely violated in numerical work by applying a Dirichlet condition at an
  outflow boundary.
- **A Cauchy problem** (data on a non-characteristic curve) requires data on the
  whole curve; data on a characteristic is never sufficient.

### 2.1 Compatibility conditions

The data are not independent of each other. If the initial state does not satisfy
the boundary condition at $t = 0$ — for example $u(x,0) = 1$ everywhere with
$u(0,t) = 0$ for $t>0$ — then the solution is discontinuous at the corner
$(0,0)$, and the series or transform solution converges to $\tfrac12$ there rather
than to either value. This is not a paradox; it is a statement that the data were
inconsistent, and the resolution is either to accept the discontinuity (as the
physics of switching on a cold boundary at $t=0$ does) or to smooth the data so
that the initial state satisfies the boundary conditions to a stated order.
**Compatibility is the one part of problem specification that no solver checks for
you, and it produces the strangest-looking numerical artefacts.**

## 3. The classification of boundary conditions

| Name | Mathematical statement | Physical meaning (heat) | Physical meaning (elastic waves) |
|---|---|---|---|
| Dirichlet | $u = f$ | prescribed temperature | prescribed displacement |
| Neumann | $\partial_n u = g$ | prescribed flux (insulating if $g=0$) | prescribed traction (free surface if $g=0$) |
| Robin | $\partial_n u + h(u - u_\infty) = g$ | convective loss to a reservoir | spring or radiation damping |
| Radiation (Sommerfeld) | outgoing wave only | — | truncation boundary of a numerical domain |
| Free surface | zero traction | — | the Earth's surface; reflects with a sign change |
| Interface | $u$ and flux continuous | perfect thermal contact | welded contact |
| Periodic | $u$ and derivatives match | cyclic symmetry | infinite repetition of a unit cell |

Three practical points.

**Dirichlet and Neumann are not interchangeable.** In the diffusion problem they
change the eigenvalues and hence every timescale: with one end insulated and one
fixed, the slowest decay rate is $\pi^2/4$; with both ends fixed it is $\pi^2$. A
factor of four in the relaxation time follows from one boundary condition, which
is why an incorrect boundary condition is not a small error.

**A free surface reflects; a radiation condition does not.** In elasticity the
free surface is a genuine, physical reflector, and the reflection is part of the
signal — surface reflections and mode conversions are the whole basis of
near-surface seismology. A radiation condition, by contrast, is a numerical
fiction: it asserts that nothing comes in from outside so that the truncated
domain behaves as though it were infinite. Confusing them produces models in which
real reflections are suppressed or spurious ones created.

**Interface conditions must be written in flux form.** Continuity of
$k\,\partial_n T$ (not of $\partial_n T$) across a conductivity contrast, because
the conserved quantity is the flux. Writing continuity of the derivative is a
common error and produces a spurious heat source or sink that scales with the
conductivity contrast.

## 4. Uniqueness and stability by energy methods

### 4.1 The heat equation

Let $u$ satisfy $u_t = \kappa u_{xx}$ on $0<x<L$ with homogeneous Dirichlet data
and let $w$ be the difference of two solutions with the same data. Multiply the
equation for $w$ by $w$ and integrate:

$$\frac{1}{2}\frac{d}{dt}\int_0^L w^2\,dx = \kappa\int_0^L w\,w_{xx}\,dx
= \kappa\left[w\,w_x\right]_0^L - \kappa\int_0^L w_x^2\,dx .$$

The boundary terms vanish, so

$$\frac{d}{dt}\int_0^L w^2\,dx = -2\kappa\int_0^L w_x^2\,dx \le 0 . \tag{1}$$

Three consequences follow at once:

- $w \equiv 0$ if it starts at zero, so the solution is **unique**;
- the energy is **non-increasing**, so small initial perturbations stay small in
  the $L^2$ norm — **stability**, with the sharper statement from the maximum
  principle that $\max\lvert u\rvert$ is also non-increasing;
- the decay is **strict** unless $w$ is constant, and with homogeneous Dirichlet
  data the only constant solution is zero, so the decay is strict for any nonzero
  perturbation.

The demonstration verifies the monotonicity numerically, using the deviation from
the equilibrium rather than the raw square:

```text
         t               E
      0.00     0.236865177
      0.80     0.002064977
      2.00     0.000015368
      4.00     0.000000004
      8.00     0.000000000

  Monotonically decreasing at every step: True
```

The subtlety is worth stating, because it was found by looking at the numbers
rather than by looking at the equations. For an inhomogeneous boundary condition
(the Robin problem relaxing to an ambient value $u_\infty$) it is
$\int (u - u_\infty)^2\,dx$ that must decay; the raw $\int u^2\,dx$ *grows*,
because the equilibrium state is not zero. "The energy decreases" is only a
statement about the energy of the *perturbation from equilibrium*.

### 4.2 The wave equation

Multiplying $u_{tt} = c^2u_{xx}$ by $u_t$ and integrating gives exact
conservation of kinetic plus elastic energy,

$$\frac{d}{dt}\int_0^L\left(\tfrac12u_t^2 + \tfrac12c^2u_x^2\right)dx = 0
\qquad\text{(with fixed ends),}$$

so uniqueness and stability hold for the same reason but with a *different
conclusion about decay*: the wave problem conserves energy, it does not dissipate
it. This is why a wave code run for a long time accumulates boundary violations,
while a diffusion code damps them.

## 5. Non-homogeneous data: Green's functions and Duhamel

The general linear initial-boundary value problem can be written as a
superposition of three elementary responses:

$$u = u_{\text{hom}} + u_{\text{source}} + u_{\text{boundary}} ,$$

where each term is a convolution with the appropriate Green's function:

- **initial data** → convolution with the *initial-value* Green's function
  (the fundamental solution of [01-09-02](./02-heat-equation.md) for heat, the
  d'Alembert kernels for waves);
- **a source term** → convolution in time with the same fundamental solution
  (**Duhamel's principle**: the response to a time-dependent source is the
  integral over the source's history of the impulse response);
- **boundary data** → convolution with the *boundary* Green's function, which
  solves the homogeneous equation with a unit boundary excitation.

Duhamel's principle is worth stating in words because it is used constantly: **a
time-dependent forcing can be regarded as a sequence of instantaneous kicks, and
the response is the superposition of the responses to those kicks.** Its
discretisation is the basis of step-by-step time integration, and its analytic
form is the reason linear time-invariant geophysical systems can be described by
an impulse response at all.

## 6. Ill-posedness: the backward heat problem

### 6.1 The statement

Consider the heat equation and ask for the state at an *earlier* time given the
state now: the **backward heat problem**. On a bounded interval with homogeneous
Dirichlet data, each mode evolves as $\exp(-\kappa\lambda_nt)$, so running
backwards multiplies mode $n$ by $\exp(+\kappa\lambda_nt)$. The demonstration
computes the amplification:

```text
      N    decay exp(-(N pi)^2 t)  amplification to invert
      1                 6.105e-01                1.638e+00
      2                 1.389e-01                7.199e+00
      5                 4.386e-06                2.280e+05
     10                 3.702e-22                2.701e+21
     20                 1.878e-86                5.325e+85
```

With $N = 20$ the amplification is $5.3\times10^{85}$. A relative data error of
$10^{-6}$ therefore produces an error of $10^{79}$ in the recovered initial state.

### 6.2 The measurement

The demonstration runs the *forward* problem twice, once from a smooth initial
condition and once with a $10^{-6}$ noise mode added, and measures how much of the
noise survives:

```text
    noise survived to t = 0.05          = 2.220e-16
    predicted noise amplitude          = 1.878e-92
    finite-difference truncation error = 8.673e-06
```

The noise has been destroyed: what survives is round-off, and it is three orders of
magnitude below the discretisation error of the forward solve. Notice the
methodology — the noise's fate is measured by differencing two runs, not by
comparing against an analytic solution, because the analytic comparison would be
dominated by truncation error and would hide the effect being measured. **Choose
the diagnostic that isolates the quantity you claim to have measured.**

### 6.3 What this means, and what to do

The backward heat problem fails condition 3 of Hadamard's list while satisfying
conditions 1 and 2. It is not that solutions do not exist or are not unique; it is
that the map from data to solution is not continuous, and the discontinuity is
exponential in the wavenumber. Three consequences:

- **No algorithm fixes this.** The information is not in the data. A "better"
  solver produces a better-resolved version of the same amplified noise.
- **The correct response is to change the problem.** Add a model constraint (a
  norm, smoothness, boundedness) and solve a *regularised* problem whose solution
  is stable and whose difference from the true solution can be bounded. This is
  Tikhonov regularisation, and [18-inverse-problems](../../18-inverse-problems/README.md)
  is about it.
- **The same structure appears elsewhere.** Downward continuation of potential
  fields ([01-09-04](./04-laplace-poisson.md) §6) and deconvolution of a
  band-limited seismogram are backward problems of the same kind.

## 7. Numerical implementation of boundary conditions

### 7.1 Impose them to the same order as the interior scheme

A second-order interior scheme paired with a first-order boundary treatment is a
first-order method overall, and the degradation is often blamed on the physics.
The standard cure for a derivative boundary condition is a **ghost node**: extend
the grid one point outside the domain and use the central-difference form of the
boundary condition to eliminate the ghost value. For the insulated condition
$u_x(0,t) = 0$ this gives $u_{-1} = u_1$, and the update at $x=0$ becomes

$$u^{n+1}_0 = u^n_0 + \frac{2\kappa\Delta t}{\Delta x^2}\left(u^n_1 - u^n_0\right),$$

which is second-order accurate. Measured against the exact solution
$u = \cos(\pi x/2)\exp(-\pi^2t/4)$ for the problem with an insulated left end and
a fixed right end:

```text
      N         dx       r     max error   order
     25     0.0400   0.396     4.931e-05        
     50     0.0200   0.399     1.252e-05    1.98
    100     0.0100   0.400     3.139e-06    2.00
    200     0.0050   0.400     7.848e-07    2.00
```

Order 2, confirming that the ghost-node treatment preserves the interior accuracy.
A one-sided difference for the same condition would give order 1 and, in a
long-time integration, a systematic error in the equilibrium.

### 7.2 Verify that the discrete solution satisfies the discrete condition

A boundary condition is a statement the solution must satisfy, not a separate
calculation. For the Robin problem the demonstration reports the flux residual
after the solution has relaxed:

```text
  Bi = 10.0, N = 50, run to t = 8.0
  max |u - u_amb| at the end          = 2.505e-08
  the Robin condition residual: -u_x(1) - Bi(u(1)-1) = 7.233e-11
```

Both statements are checked: the solution has reached the physically forced
equilibrium (insulated far end plus convective surface forces $u = u_\infty$), and
the discrete flux balance is satisfied to truncation-error level. This is the
consistency check for boundary conditions, and it is cheap.

### 7.3 Reflecting versus radiating wave boundaries

For the wave equation the choice is starker, and it is a modelling decision rather
than a numerical detail. The demonstration runs a compact right-going pulse on a
domain with (a) a fixed (Dirichlet) right boundary and (b) a first-order one-way
outflow (Mur) condition,

$$u^{n+1}_N = u^n_{N-1} + \frac{\nu-1}{\nu+1}\left(u^{n+1}_{N-1} - u^n_N\right),
\qquad \nu = \frac{c\Delta t}{\Delta x},$$

which is exact for normal incidence:

```text
                boundary      t = 0.7      t = 1.0      t = 1.6
         Dirichlet u = 0   4.1147e-02   9.9728e-01   9.9696e-01
       one-way absorbing   1.0026e+00   7.2592e-04   6.0586e-04
```

At $t = 0.7$ the pulse is still inside the domain in both runs (amplitude about
1). By $t = 1.0$ the fixed boundary has returned the pulse with amplitude 0.997,
while the absorbing condition has left $7.3\times10^{-4}$ — a reflection
coefficient of about $10^{-3}$, limited by the first-order accuracy of the
condition. Nothing else in the numerical modelling of waves is more commonly
mis-handled: an absorbing boundary that the code believes is reflecting (or vice
versa) turns a physical interpretation into an artefact.

Two refinements are standard. A higher-order one-way condition improves the
reflection coefficient at the cost of complexity, and a **sponge** or perfectly
matched layer damps the field over a region of several cells. Both are exercises
in matching the *continuous* radiation condition rather than in numerical
bookkeeping.

## 8. Common mistakes

1. **Applying the wrong number of conditions.** One at each spatial boundary for
   parabolic problems, one *per incoming characteristic* for hyperbolic ones, one
   at every boundary point for elliptic ones. Over-specifying produces a scheme
   that cannot converge; under-specifying produces a null space.
2. **Ignoring corner compatibility.** If the initial data violate the boundary
   data at $t=0$, expect a genuine discontinuity there, and decide explicitly
   whether it is physical.
3. **Imposing a derivative boundary condition with a one-sided difference.**
   Second order in the interior plus first order at the boundary is a first-order
   method. Use a ghost node.
4. **Checking only the interior solve.** Always evaluate the boundary condition
   residual on the discrete solution, as Section 7.2 does; it is the only way to
   catch a mis-implemented ghost node.
5. **Using the raw energy when the equilibrium is non-zero.** The decaying
   quantity is the deviation from equilibrium. Measured naively, the energy of a
   relaxing system *increases*.
6. **Assuming a fixed boundary is a neutral choice.** It reflects 100 % of
   incident wave energy and constrains the diffusive relaxation rate, changing
   timescales by factors of order unity.
7. **Believing a better solver can solve an ill-posed problem.** The backward heat
   problem amplifies noise by $10^{85}$; regularisation changes the problem, and
   that is the only route.
8. **Applying a Dirichlet condition at a subsonic outflow boundary.** The
   characteristic leaves the domain there and carries no information inward;
   imposing a value over-specifies and reflects.
9. **Confusing interface continuity of $u$ with continuity of $\partial_n u$.**
   The conserved flux is what must match.

## 9. Real-world applications

- **Borehole and palaeoclimate inversion.** A backward heat problem. Every
  published surface-temperature reconstruction from a borehole profile makes a
  regularisation choice; Section 6 is why, and
  [18-inverse-problems](../../18-inverse-problems/README.md) is how.
- **Thermal modelling of a reservoir or a buried pipeline.** Dirichlet surface
  temperatures, Robin conditions against air, and Neumann conditions on insulated
  faces; the resulting timescales change by factors of order unity with the
  boundary condition.
- **Aquifer boundary conditions.** A river is a Dirichlet (or leaky) boundary, a
  no-flow fault is Neumann, and a "constant-head" far-field boundary is a
  modelling choice that can control the answer.
- **Seismic modelling.** Absorbing boundaries, free surfaces and elastic interface
  conditions determine whether the modelled section contains real reflections,
  artefacts, or both. The reflection coefficient measured in Section 7.3 is a
  standard quality metric.
- **Radar and electromagnetic modelling.** GPR and EM problems need radiating
  boundaries in the air half-space and conducting behaviour in the ground; a
  wrongly specified boundary turns a diffusive decay into a spurious reflection.
- **Geothermal reservoir simulation.** The boundary conditions on the model edges
  (insulated, fixed temperature, prescribed flux) control the predicted lifetime
  of the resource more than the interior discretisation does.
- **Time-lapse monitoring.** Detecting a small change requires that the boundary
  conditions be reproduced *identically* between surveys, because a boundary
  change can masquerade as a subsurface change.

## 10. Further reading

- **Hadamard, J. (1923). *Lectures on Cauchy's Problem in Linear Partial
  Differential Equations*. Yale University Press.** Level: graduate. The origin of
  the well-posedness conditions of Section 1.
- **Evans, L. C. (2010). *Partial Differential Equations* (2nd ed.). AMS.**
  Level: graduate. Energy methods, maximum principles, existence for the heat and
  wave equations, and the modern treatment of boundary-value problems.
- **Strauss, W. A. (2007). *Partial Differential Equations: An Introduction*
  (2nd ed.). Wiley.** Level: advanced undergraduate upward. The clearest
  introduction to energy methods and to well-posedness for the classical
  equations.
- **Carslaw, H. S., & Jaeger, J. C. (1959). *Conduction of Heat in Solids*
  (2nd ed.). Oxford University Press.** Level: graduate. The boundary-condition
  catalogue of Section 3 with the solutions for every combination.
- **Tikhonov, A. N., & Arsenin, V. Y. (1977). *Solutions of Ill-Posed Problems*.
  Wiley.** Level: graduate. The classical treatment of the regularisation that
  Section 6.3 requires.
- **Engl, H. W., Hanke, M., & Neubauer, A. (1996). *Regularization of Inverse
  Problems*. Kluwer.** Level: graduate. Modern regularisation theory, including
  the backward heat problem as a worked example.
- **Igel, H. (2017). *Computational Seismology*. Oxford University Press.**
  Level: graduate. Absorbing boundaries, free surfaces and interface conditions in
  practice.

> Note on citations: bibliographic details are given so you can locate the works.
> This repository does not host or reproduce copyrighted text; confirm current
> editions and availability through your library before citing.

## 11. Exercises

Solutions are in
[`exercises/07-boundary-value-problems-solutions.md`](./exercises/07-boundary-value-problems-solutions.md).

**★1.** State Hadamard's three conditions and say which is violated by the
backward heat problem. Give the amplification for mode $n = 8$ at $t = 0.1$ with
$\kappa = 1$ and $L = 1$.

**★2.** Count the conditions required for (a) $\nabla^2V = 0$ on a disc;
(b) $u_t = \kappa u_{xx}$ on a rod; (c) $u_{tt} = c^2u_{xx}$ on a string. Justify
each count from the characteristics.

**★3.** Write the energy identity for the heat equation with homogeneous Robin
data and show that the energy $\int w^2\,dx$ still decays.

**★4.** A rod has $u(x,0) = 1$ everywhere, $u(0,t) = 0$ and $u(L,t) = 0$. State
the compatibility failure at the corners and describe qualitatively what the exact
solution does at $(0,0)$.

**★★5.** Derive the ghost-node update for a Robin condition
$-u_x(L,t) = h(u(L,t) - u_\infty)$ and show that the resulting discrete condition
is second-order accurate.

**★★6.** Duhamel's principle: write the solution of $u_t = \kappa u_{xx} + f(x,t)$
with zero initial and boundary data as an integral over the source history, and
state what the kernel is.

**★★7.** For a reflection coefficient of $10^{-3}$, compute the amplitude after
ten reflections of a wave in a computational box and compare with a single
reflection of a physical interface with a 10 % impedance contrast. Comment on the
adequacy of a first-order absorbing condition for a 100-period simulation.

**★★8.** Show that the backward heat problem with a cutoff at wavenumber $N_c$
(i.e. discarding modes above $N_c$) has an amplification bounded by
$\exp(\kappa N_c^2\pi^2 t)$ and choose $N_c$ so that a data error of $10^{-6}$ is
amplified by at most $10^{3}$ for $\kappa = 1$, $L = 1$, $t = 0.05$.

**★★★9.** Implement the heat equation with (a) Dirichlet and (b) Robin boundary
conditions at both ends with the same initial condition, and measure the decay of
the first mode in each case. Report the two rates, compare them with the
eigenvalues you predict, and explain the difference physically.

**★★★10.** A numerical model of a reservoir is run for 30 years of simulation
and then inverted for a change in rock properties between two surveys. Using the
mathematics of Sections 6 and 7, write a short design note: which boundary
conditions must be identical between the two runs, why an absorbing boundary is
not appropriate for the ground surface, and what regularisation you would apply to
the time-lapse inversion. Justify each choice.

## 12. Self-assessment checklist

- [ ] I can state Hadamard's three conditions and identify which one fails for a
      given problem.
- [ ] I can count the required conditions for each class from the characteristics.
- [ ] I can classify a boundary condition and state its physical meaning in heat
      and in elasticity.
- [ ] I can prove uniqueness and decay for the heat problem by the energy method,
      including the non-homogeneous-equilibrium subtlety.
- [ ] I can implement a derivative boundary condition to second order with a ghost
      node and verify it on the discrete solution.
- [ ] I can quantify the ill-posedness of the backward heat problem and state why
      regularisation changes the problem rather than solving it.
- [ ] I can distinguish reflecting from radiating boundaries and measure the
      residual reflection of a first-order absorbing condition.

## Related lessons

- [01-09-01 Classification of PDEs](./01-classification.md) — the source of the
  condition counts in Section 2.
- [01-09-02 The Diffusion/Heat Equation and Diffusive Timescales](./02-heat-equation.md)
  — the equation whose boundary conditions this lesson organises, and the
  timescales they control.
- [01-09-05 Separation of Variables and Boundary Conditions](./05-separation-of-variables.md)
  — the same conditions seen through explicit eigenfunction solutions.
- [01-09-08 Weak Solutions, Variational Forms and Well-Posedness](./08-weak-solutions.md)
  — well-posedness in the variational setting, and natural versus essential
  boundary conditions.
- [01-09-04 Laplace and Poisson Equations in Earth Systems](./04-laplace-poisson.md)
  — the elliptic case in detail, including downward continuation as a backward
  problem.
- [18-inverse-problems](../../18-inverse-problems/README.md) — regularisation, the
  practitioner's answer to Sections 6 and 7.
- [19-numerical-modeling-hpc](../../19-numerical-modeling-hpc/README.md) —
  boundary conditions in production modelling codes.
