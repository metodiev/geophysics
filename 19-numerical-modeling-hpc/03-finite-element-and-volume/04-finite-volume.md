---
id: 19-03-04
title: "Finite Volume Methods and Conservative Discretisation"
level: research
prereqs: ["19-03-01", "19-02-05", "19-01-04"]
tags: [numerical-modelling, finite-volume, conservation, upwind, flux-form, numerical-modelling, convergence]
---

# Finite Volume Methods and Conservative Discretisation

**All models and data in this module are SYNTHETIC.** Every initial condition,
velocity and mesh below is a chosen teaching model, and every number is printed
by [`code/finite_volume_demo.py`](./code/finite_volume_demo.py).

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the cell-centred finite-volume update from the integral form of a
   conservation law, and **state** exactly what makes it conservative.
2. **Measure** the numerical diffusion of the first-order upwind scheme and
   **compare** it with the closed-form coefficient $a\Delta x(1-C)/2$.
3. **Distinguish** dissipation from dispersion using the amplification factor of
   a scheme, and **verify** a scheme's amplification factor against its closed
   form.
4. **Demonstrate** that a non-conservative discretisation of the same equation
   does not conserve mass, and **quantify** the loss.
5. **Derive** the harmonic-mean face transmissibility and **measure** the error
   of the arithmetic mean on both a smooth and a discontinuous coefficient.
6. **Measure** the convergence order of upwind and second-order fluxes, and
   **explain** why the measured second-order rate is not 2.
7. **State** which of conservation, monotonicity and accuracy a given scheme
   delivers, and **give up** the one it does not.

## Prerequisites

- [19-03-01 Weak Formulation and the Galerkin Method](01-fem-weak-form.md) — the
  flux form and the harmonic mean appear there as Section 6.
- [19-02-05 Finite-Difference Acoustic and Elastic Wave Propagation](../02-finite-difference-methods/05-fd-wave-propagation.md) —
  flux-form finite differences as the starting point of wave modelling.
- [19-01-04 Numerical Dispersion, Dissipation and Grid Anisotropy](../01-numerical-foundations/04-numerical-dispersion-diffusion.md) —
  the vocabulary of dispersion and dissipation used throughout.

## 1. The integral form is the definition

A conservation law in differential form is a statement about a continuum that
can fail whenever the solution is not smooth:

$$\frac{\partial u}{\partial t} + \frac{\partial F(u)}{\partial x} = 0. \tag{1.1}$$

Written for a cell $C_i = [x_{i-1/2}, x_{i+1/2}]$ of width $\Delta x_i$, the
integral form is

$$\frac{\mathrm{d}}{\mathrm{d}t}\int_{C_i} u\,\mathrm{d}x
= F(u_{i-1/2}) - F(u_{i+1/2}). \tag{1.2}$$

This is not an approximation. It says that the rate of change of the cell average
is the flux in at the left face minus the flux out at the right face, and it
remains true across a shock. The finite-volume method discretises (1.2)
directly:

$$u_i^{n+1} = u_i^{n} - \frac{\Delta t}{\Delta x_i}
\left(F_{i+1/2} - F_{i-1/2}\right), \tag{1.3}$$

where the *same* face flux $F_{i+1/2}$ is used by cells $i$ and $i+1$. That
single decision — one flux per face, shared — is what makes the scheme
conservative, and everything else in this lesson follows from it.

### 1.1 Summing (1.3) proves conservation

Sum (1.3) over all cells of a periodic domain:

$$\sum_i \left(u_i^{n+1} - u_i^{n}\right)\Delta x_i
= -\Delta t\sum_i\left(F_{i+1/2} - F_{i-1/2}\right) = 0, \tag{1.4}$$

because every interior face appears once with a $+$ and once with a $-$. The
discrete total is unchanged **identically**, not approximately. The
demonstration measures exactly that with a variable wave speed
$a(x) = 1 + 0.5\sin(2\pi x)$ m/s, a uniform mesh of 200 cells and 200 steps:

| scheme | total mass $M = \sum u_i\Delta x$ | drift from the initial value |
|---|---|---|
| initial condition | 0.125331413732 | — |
| flux form of $\partial_t u + \partial_x(au) = 0$ | 0.125331413732 | $+0.000\times10^{0}$ |
| pointwise form of $\partial_t u + a\,\partial_x u = 0$ | 0.071842691370 | $-4.268\times10^{-1}$ |

The flux form loses **nothing** across 200 steps. The advective form — the same
equation analytically, discretised without faces — loses **43%** of the mass
while looking entirely reasonable in the code.

The two equations are not even the same equation once $a$ varies:
$\partial_t u + \partial_x(au) = 0$ and $\partial_t u + a\partial_xu = 0$ differ
by $u\,\partial_xa$. Only one of them is a conservation law, and only a
discretisation built on faces can preserve a total that the underlying equation
preserves.

## 2. Upwind: the first-order flux, and its measured diffusion

For $a > 0$, the flux at face $i+1/2$ is taken from the upwind side,
$F_{i+1/2} = a\,u_i$, giving

$$u_i^{n+1} = u_i^{n} - C\left(u_i^n - u_{i-1}^n\right), \qquad
C = \frac{a\,\Delta t}{\Delta x}. \tag{2.1}$$

A Taylor expansion of (2.1) about $(x_i,t_n)$ gives

$$u_t + a u_x = \frac{a\Delta x}{2}(1 - C)\,u_{xx} + \dots \tag{2.2}$$

so the leading error is a **diffusion term** with coefficient
$D_{\rm num} = \tfrac12 a\Delta x(1-C)$. The scheme is consistent with the
advection–diffusion equation, not with the advection equation, and the diffusion
vanishes only if $\Delta x \to 0$.

The demonstration measures it by advecting a Gaussian for one period and
tracking its variance, which grows as $\sigma^2(t) = \sigma^2(0) + 2D_{\rm num}t$:

| $N$ | $\Delta x$ (m) | CFL | measured $2D_{\rm num}$ (m²/s) | $a\Delta x(1-C)$ |
|---|---|---|---|---|
| 100 | 0.01000 | 0.8 | 0.00199987 | 0.00200000 |
| 200 | 0.00500 | 0.8 | 0.00099986 | 0.00100000 |
| 400 | 0.00250 | 0.8 | 0.00049986 | 0.00050000 |
| 400 | 0.00250 | 0.4 | 0.00149986 | 0.00150000 |

The measured coefficient equals the closed form to five digits at every
resolution and every CFL. This is a measurement, not a quotation: the variance
of a Gaussian under a scheme is a property of that scheme, and the closed form
predicts it. Note also the fourth row: lowering the CFL from 0.8 to 0.4 at fixed
$\Delta x$ *triples* the diffusion, because $(1-C)$ grows. Reducing the timestep
is not a cure for first-order error.

## 3. Accuracy on smooth data, and the measured rates

With a smooth Gaussian ($\sigma = 0.15$ m) advected one period and the error
measured in $\mathrm{L}^1$:

| $N$ | $\Delta x$ (m) | upwind $\mathrm{L}^1$ | order | Lax–Wendroff $\mathrm{L}^1$ | order |
|---|---|---|---|---|---|
| 100 | 0.01000 | $3.6497\times10^{-2}$ | — | $2.0362\times10^{-3}$ | — |
| 200 | 0.00500 | $1.9169\times10^{-2}$ | 0.929 | $5.3572\times10^{-4}$ | 1.926 |
| 400 | 0.00250 | $9.8378\times10^{-3}$ | 0.962 | $1.4300\times10^{-4}$ | 1.906 |
| 800 | 0.00125 | $4.9855\times10^{-3}$ | 0.981 | $3.9468\times10^{-5}$ | 1.857 |
| 1600 | 0.00063 | $2.5098\times10^{-3}$ | 0.990 | $1.1313\times10^{-5}$ | 1.803 |

Two honest readings:

1. **Upwind reaches order 1** (0.990 on the finest pair), approaching from below.
   At $N = 1600$ its error is $221.8$ times the Lax–Wendroff error on the same
   mesh, and that ratio grows with refinement. That is the practical cost of
   first order, expressed as a number rather than as an adjective.
2. **Lax–Wendroff does not reach order 2 over this range**: 1.926, 1.906, 1.857,
   1.803 — decreasing. Its leading error is dispersive and grid-scale, and the
   $\mathrm{L}^1$ norm of a grid-scale ripple has its own rate. A convergence
   study must quote the measured order, not the advertised one, and must say
   which norm produced it.

### 3.1 Dissipation versus dispersion, measured exactly

Both schemes can be characterised exactly on a single Fourier mode. For
$u_j^n = G^n e^{\mathrm{i}\theta j}$ with $\theta = k\Delta x$, one Lax–Wendroff
step multiplies the solution by

$$G(\theta) = 1 - C^2(1-\cos\theta) - \mathrm{i}\,C\sin\theta . \tag{3.1}$$

The demonstration applies the scheme to the mode, divides, and compares with
(3.1) and with the exact phase speed $a$:

| $\theta$ (rad) | $C$ | $|G_{\rm num} - G_{\rm closed}|$ | phase speed $/a$ |
|---|---|---|---|
| $\pi/8$ | 0.5 | $5.6\times10^{-17}$ | 0.981082 |
| $\pi/4$ | 0.5 | $1.1\times10^{-16}$ | 0.928054 |
| $\pi/2$ | 0.5 | $1.1\times10^{-16}$ | 0.748668 |
| $3\pi/4$ | 0.5 | $1.2\times10^{-16}$ | 0.469119 |

The first column verifies the *implementation* against exact algebra — a check
that is worth doing because it is unforgiving. The last column is the physics:
Lax–Wendroff has $|G| = 1$ (no dissipation) but a phase speed that falls to
$0.469a$ at $\theta = 3\pi/4$. It does not damp a wave, it **retards** it, and a
jump therefore becomes a train of oscillations rather than a wider ramp. Upwind
is the opposite: $|G| < 1$ and its error is the diffusion measured in Section 2.

### 3.2 Monotonicity: what the same schemes do to a jump

A square pulse of unit height and width 0.2 m, one half-period of advection at
CFL 0.8:

| scheme | $\max u$ | $\min u$ | total variation |
|---|---|---|---|
| data | 1.000000 | 0.000000 | 2.000000 |
| upwind | 0.999995 | $+0.000000$ | 1.999990 |
| Lax–Wendroff | 1.174417 | $-0.174417$ | 3.003499 |

Upwind never leaves the range of the data — no new extrema, total variation
preserved — but it smears the jump. Lax–Wendroff overshoots by 17%, undershoots
below zero, and increases the total variation by 50%. **Both properties cannot be
had from a linear scheme of order greater than one**; that is the content of
Godunov's theorem, and it is why production codes use nonlinear limiters. What
this lesson insists on is the *measurement*: 17% and 50% are numbers a user can
check against a requirement, while "second-order accurate" is not.

## 4. Graded meshes and the face transmission

For the steady problem $-(a u')' = f$ on a graded mesh, the finite-volume
unknown is the cell average and the coefficient lives at faces. Across a face
between half-cells of the same material, transmissibility is that material's
value; across a face between two materials in series,

$$T_{\rm harm} = \frac{2a_La_R}{a_L + a_R}. \tag{4.1}$$

The demonstration solves $-(a u')' = 0$, $u(0)=0$, $u(1)=1$, $a = 1+4x$ on a
uniform mesh and compares the finite-volume scheme with a naive pointwise
difference that averages $a$ arithmetically at the nodes:

| $N$ | $\Delta x$ (m) | FV error | order | naive error | order |
|---|---|---|---|---|---|
| 20 | 0.05000 | $2.6787\times10^{-3}$ | — | $4.6781\times10^{-2}$ | — |
| 40 | 0.02500 | $7.2031\times10^{-4}$ | 1.895 | $2.6862\times10^{-2}$ | 0.800 |
| 80 | 0.01250 | $1.8693\times10^{-4}$ | 1.946 | $1.4430\times10^{-2}$ | 0.897 |
| 160 | 0.00625 | $4.7625\times10^{-5}$ | 1.973 | $7.4837\times10^{-3}$ | 0.947 |

Finest-pair orders: **1.973** for the flux form and **0.947** for the naive
difference. Both converge, but not at the same rate, and the naive form's leading
error is a misplaced coefficient rather than a truncation term. For a
*discontinuous* $a$ the naive form does not converge to the right answer at all:
that measurement is in lesson [01](01-fem-weak-form.md), Section 6, where the
harmonic mean is exact to round-off and the arithmetic mean is first order with
an error of $1.00\Delta x$ at a $10^6{:}1$ contrast.

## 5. Burgers' equation: when the form of the equation changes the answer

$$u_t + \left(\tfrac12 u^2\right)_x = 0 \quad\text{(conservative)}, \qquad
u_t + u\,u_x = 0 \quad\text{(advective)}. \tag{5.1}$$

Analytically these are the same equation where $u$ is smooth. Across a shock they
are not: the conservative form selects the weak solution whose shock speed obeys
the Rankine–Hugoniot condition, and the non-conservative form need not.

Riemann data $u = 1$ for $x < 0.25$ and $u = 0$ for $x > 0.25$ give an exact shock
speed $\tfrac12(u_L + u_R) = 0.5$ m/s, so after $t = 0.4$ s the shock should sit
at $x = 0.45$ m. The demonstration integrates both forms on a 400-cell mesh at
CFL 0.4, using the exact Godunov flux for the conservative form and a pointwise
upwind difference for the advective form:

| discretisation | measured shock position | measured shock speed |
|---|---|---|
| conservative Godunov | 0.4501 m after 0.4000 s | 0.5002 m/s |
| advective upwind | 0.2500 m after 0.4000 s | 0.0000 m/s |

The conservative scheme reproduces the Rankine–Hugoniot speed to three digits -
the residual comes from locating a smeared shock by linear interpolation. The
advective scheme's shock **does not move at all**: its upwind difference at the
shock uses the downstream state $u_i = 0$, so the update there is zero. An
entire family of results — shock speeds, arrival times, front positions — is
inaccessible to a scheme that discretises the wrong form, however small its
truncation error looks.

## 6. A fully worked cell update, by hand

Take linear advection with $a = 1$ m/s, $\Delta x = 0.01$ m, CFL $C = 0.8$, and
the three cell values $u_{i-1} = 1.0$, $u_i = 0.6$, $u_{i+1} = 0.2$ (all
dimensionless). Then:

1. **Fluxes.** $F_{i+1/2} = a u_i = 0.60$ and $F_{i-1/2} = au_{i-1} = 1.00$
   m/s — the upwind values, since $a > 0$.
2. **Update.** $u_i^{n+1} = 0.6 - 0.8(0.60 - 1.00) = 0.6 + 0.32 = 0.92$.
3. **Conservation check on the pair.** Cell $i+1$ updates with the same internal
   face flux: $u_{i+1}^{n+1} = 0.2 - 0.8(0.20 - 0.60) = 0.52$. The total change
   over the pair is $(0.92-0.60) + (0.52-0.20) = 0.32+0.32 = 0.64$, and the net
   boundary flux of the pair is $C(F_{i-1/2} - F_{i+3/2}) = 0.8(1.00 - 0.20) =
   0.64$. The shared internal face $F_{i+1/2} = 0.60$ cancelled identically: it
   appears with opposite signs in the two cells and nowhere else.
4. **Numerical diffusion.** $D_{\rm num} = \tfrac12(1)(0.01)(1-0.8) =
   1.0\times10^{-3}$ m²/s, so over one step the diffusion length is
   $\sqrt{2D_{\rm num}\Delta t} = \sqrt{2(10^{-3})(0.008)} = 4.0\times10^{-3}$ m
   — 40% of a cell, every step.
5. **Stability.** $C = 0.8 \le 1$; at $C = 1$ the scheme is exact for pure
   advection ($D_{\rm num}=0$), which is why it is not a coincidence that the
   measurement at CFL 0.8 scales with $(1-C)$.

## 7. Assumptions and regime of validity

1. **One-dimensional, Cartesian, uniform cells** except in Sections 4 and the
   graded-mesh measurement. On an unstructured mesh the face flux must be
   projected along the face normal, and the conservation proof (1.4) survives
   only if each face is shared by exactly two cells.
2. **Explicit time stepping with $C \le 1$ for upwind advection.** The measured
   diffusion coefficient presumes a stable CFL; the derivation (2.2) is a Taylor
   expansion about a stable step.
3. **Smooth solutions** for the order measurements of Section 3. Across a jump
   the pointwise order is not defined, and total variation is the appropriate
   measure — which is why Section 3.2 reports it instead of an order.
4. **Scalar conservation laws.** For systems (elasticity, magnetohydrodynamics,
   two-phase flow) the same construction applies face by face, but the
   characteristic decomposition needed to choose the upwind side is a separate
   problem.
5. **A flux that is a function of the conserved variable only.** For source terms
   and for non-conservative products the discrete balance acquires an extra term
   and the exact conservation of a naive update can be lost.
6. **Double precision for the conservation measurement.** The measured drift of
   $0.000\times10^{0}$ is a statement about exact cancellation in the summation;
   in single precision the same scheme would show a drift of order $10^{-7}$ per
   step, which is round-off and not physics.

## 8. Mastery checkpoint

Complete this without notes.

> Solve $u_t + (a(x)u)_x = 0$ with $a(x) = 2 + \cos(2\pi x)$ m/s on a periodic
> domain of length 1 m, using cell-centred finite volumes with upwind fluxes,
> $\Delta x = 0.005$ m and CFL 0.5.
>
> **(a)** State the two-line reason the scheme conserves $\sum u_i\Delta x$
> exactly.
> **(b)** Compute the numerical diffusion coefficient and the distance over which
> a sharp front is smeared after $t = 0.5$ s.
> **(c)** Predict the $\mathrm{L}^1$ order you would measure on smooth data, and
> state why it is not 2.
> **(d)** A colleague discretises the same physical problem as
> $u_t + a(x)u_x = 0$ with a pointwise upwind difference and reports a mass error
> of 40% after a few hundred steps. Diagnose the cause in one sentence and give
> the minimal fix.
> **(e)** State one requirement you would impose on the scheme if the solution
> develops a shock, and one property you must give up to achieve it.

A worked version appears with the
[exercises](exercises/04-finite-volume-exercises.md).

## 9. Common pitfalls

1. **Discretising the advective form of a conservation law.** Measured: 43% mass
   loss in 200 steps, and a Burgers shock that does not move.
2. **Treating numerical diffusion as negligible at high resolution.** It is
   exactly $a\Delta x(1-C)/2$, first order, and the measured values above span
   $2.0\times10^{-3}$ to $5.0\times10^{-4}$ m²/s; at $N=1600$ upwind is still
   222 times worse than a second-order scheme.
3. **Reducing $\Delta t$ to gain accuracy.** At fixed $\Delta x$, going from CFL
   0.8 to 0.4 *increased* the measured diffusion from $5.0\times10^{-4}$ to
   $1.5\times10^{-3}$ m²/s.
4. **Quoting an order without the norm.** The same Lax–Wendroff run gives 1.926
   or 1.803 depending on the refinement pair; and monotonicity is a statement
   about extrema, not about any norm.
5. **Averaging transport coefficients at faces.** Arithmetic averaging gives a
   first-order error whose size grows with the contrast; harmonic averaging is
   exact for a two-material series face.
6. **Assuming a stabilised high-order scheme is monotone.** Lax–Wendroff is
   stable, second-order in the interior, and produces a 17% overshoot at a jump.
7. **Testing conservation on a uniform mesh only.** On a uniform mesh a
   pointwise centred difference is also conservative; the non-conservation
   appears with a variable coefficient or a graded mesh, which is why the
   measurement uses both.

## 10. Related modules

- [19-03-05 FEM in Geophysics: EM, Geodynamics and Seismology](05-fem-geophysics.md) —
  the same flux ideas inside an element-based code.
- [19-05-01 Volume and Surface Integral Equations](../05-integral-equation-and-boundary-methods/01-integral-equations.md) —
  the other way to build a method directly from a conservation or reciprocity
  statement.
- [19-08-03 Simulating EM Diffusion in Conductive Media](../08-geophysical-simulation-case-studies/03-simulate-em-diffusion.md) —
  a production problem in which the face conductance is the whole game.
- [19-01-04 Numerical Dispersion, Dissipation and Grid Anisotropy](../01-numerical-foundations/04-numerical-dispersion-diffusion.md) —
  the general theory behind Sections 2–3.
- [09-02-06 Resistivity Forward Modelling](../../09-electrical-em-methods/02-dc-resistivity/06-resistivity-forward-modelling.md) —
  the geophysical problem whose discretisation this lesson justifies.

## Materials

- Demonstration: [`code/finite_volume_demo.py`](./code/finite_volume_demo.py).
- Exercises: [`exercises/04-finite-volume-exercises.md`](./exercises/04-finite-volume-exercises.md)
  with worked [solutions](./exercises/04-finite-volume-solutions.md).
