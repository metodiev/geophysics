---
id: 19-02-03
title: "Boundary Conditions: Dirichlet, Neumann, Absorbing, PML"
level: research
prereqs: ["19-02-01", "19-01-03", "19-02-02"]
tags: [numerical-modelling, hpc, boundary-conditions, absorbing, pml, sponge]
---

# Boundary Conditions: Dirichlet, Neumann, Absorbing, PML

A model is finite; the Earth is not. Every simulation therefore ends at a
boundary the physics does not have, and the boundary's reflection coefficient is
part of the answer whether it is measured or not. This lesson derives the two
physical conditions (Dirichlet and Neumann), shows how their discretisation
controls the global order of a solution, then measures the residual reflection
of a one-way (Mur) condition and of a graded sponge layer — including the
non-monotonic behaviour that makes the damping strength something to be
calibrated rather than chosen. **All models and data in this module are
SYNTHETIC.** Every number quoted here is printed by
`code/fd_boundary_conditions_demo.py`.

## Learning objectives

By the end of this lesson you will be able to:

1. **Implement** a Neumann condition with a two-point one-sided difference and
   with a ghost node, and **measure** the global order each produces.
2. **Explain** why a single first-order boundary treatment limits the order of
   the whole solution, and **state** the equivalent statement for time stepping.
3. **Measure** the reflection coefficients of a Dirichlet (pressure-release) and
   a free-surface boundary and **show** that they are the values the condition
   imposes.
4. **Implement** a first-order one-way condition, **measure** its residual
   reflection, and **demonstrate** that it converges at second order.
5. **Design** a graded sponge layer and **calibrate** its two parameters by
   measurement, explaining why stronger damping is not monotonically better.
6. **State** the assumptions under which each boundary treatment is valid, and
   in particular what happens to them at oblique incidence.

## Prerequisites

- [19-02-01 Deriving Finite-Difference Operators via Taylor Expansion](01-fd-derivation.md) —
  the one-sided stencils used at boundaries.
- [19-01-03 Consistency, Stability and the Lax Equivalence Theorem](../01-numerical-foundations/03-consistency-stability.md) —
  why a boundary can limit the order or destroy stability.
- [19-02-02 High-Order and Compact Stencils; Staggered Grids](02-fd-stencils.md) —
  the interior stencils whose order the boundary must not spoil.

## 1. Intuition: the boundary is part of the model

A physical boundary condition constrains the solution on a set of measure zero in
space, and yet it can decide the answer everywhere, because elliptic problems
propagate boundary information inwards and hyperbolic problems reflect it back.
Three regimes matter in practice:

- **physical walls** — a free surface (pressure release, reflection $-1$ in
  pressure) or a rigid boundary (reflection $+1$);
- **open boundaries** — the model must let waves out as if nothing were there.
  In the continuum this means a one-way condition; on a grid it means minimising
  a residual reflection;
- **artificial absorbers** — a layer of graded damping appended to the domain,
  the practical ancestor of the perfectly matched layer (PML).

The honest difficulty is that an *exact* absorbing boundary condition for a
discrete scheme is non-local in both space and time: it must carry the whole
history of the boundary values. Every practical absorber is therefore an
approximation with a measurable reflection, and the measurement is the only
defence against a model whose output is dominated by its own edges.

## 2. Precise definitions

**Dirichlet.** $u = g$ on the boundary. In acoustics, $p = 0$ is a
pressure-release surface; the reflection coefficient for pressure is $-1$ exactly.

**Neumann.** $\partial u/\partial n = q$. For an acoustic free surface the normal
velocity vanishes, giving a pressure reflection coefficient $+1$.

**Ghost node.** A fictitious node outside the domain used to enforce a Neumann
condition without a one-sided formula. For a uniform grid and $u'(0) = 0$, the
ghost value is set by symmetry, $u_{-1} = u_{1}$; for a general flux $q$,
$u_{-1} = u_{1} - 2hq$.

**One-way (Mur / Engquist–Majlaus) condition.** In one dimension the outgoing
characteristic satisfies $u_t + c\,u_x = 0$ at the boundary; the standard
second-order-accurate discretisation at $x = 0$ is

$$u_0^{n+1} = u_1^{n} + \frac{C-1}{C+1}\left(u_1^{n+1} - u_0^{n}\right),
\qquad C = \frac{c\,dt}{h}.$$

**Reflection coefficient.** $R = A_{\text{reflected}}/A_{\text{incident}}$,
measured on the pulse amplitude at a receiver, with the sign carrying the
polarity.

**Sponge layer (damped layer).** A region in which the equation carries an
artificial damping term, $u_{tt} = c^{2}\nabla^{2}u - \sigma(x)\,u_t$, with
$\sigma$ ramped from zero to $\sigma_{\max}$ over a layer of thickness
$L_{\text{sp}}$.

## 3. Derivations

### 3.1 Neumann: one-sided versus ghost node

Take $-u''(x) = \tfrac{\pi^{2}}{4}\cos\!\big(\tfrac{\pi x}{2}\big)$ on $(0,1)$
with $u'(0) = 0$ and $u(1) = 0$; the exact solution is
$u = \cos(\pi x/2)$. The source is deliberately non-zero **on** the boundary,
which is what makes the two treatments differ.

*Two-point one-sided.* Apply $(-u_0 + u_1)/h = 0$, i.e. $u_1 = u_0$. The exact
solution has $u(h) - u(0) = -\pi^{2}h^{2}/8 + O(h^{4})$, so the discrete
condition is wrong by $O(h)$ in the *value* at the boundary:

$$u_0^{h} = u_0 - \frac{\pi^{2}}{8}h + O(h^{2}),$$

and that error propagates into the interior: the whole solution becomes
first-order.

*Ghost node.* Set $u_{-1} = u_1$ (since $u'(0) = 0$) and apply the interior
operator at the boundary: $(2u_0 - 2u_1)/h^{2} = f_0$. Then the boundary row has
the same truncation order as the interior and the solution stays second order.

Measured $\max|u_h - u|$ over all nodes:

| $n$ | $h$ | one-sided (2 pt) | order | ghost node | order |
|---|---|---|---|---|---|
| 20 | 0.05000 | $6.117083\times10^{-2}$ | — | $5.142005\times10^{-4}$ | — |
| 40 | 0.02500 | $3.071399\times10^{-2}$ | 0.9939 | $1.285204\times10^{-4}$ | 2.0003 |
| 80 | 0.01250 | $1.538913\times10^{-2}$ | 0.9970 | $3.212824\times10^{-5}$ | 2.0001 |
| 160 | 0.00625 | $7.702596\times10^{-3}$ | 0.9985 | $8.031943\times10^{-6}$ | 2.0000 |
| 320 | 0.00313 | $3.853306\times10^{-3}$ | 0.9992 | $2.007979\times10^{-6}$ | 2.0000 |

At the finest grid the one-sided error is $1920$ times larger than the ghost-node
error with the same number of unknowns. **A first-order boundary condition
contaminates a second-order interior**, and no amount of interior refinement fixes
it; notice also that the observed orders for the one-sided case approach one from
below (0.9939, 0.9970, …), the same signature seen in
[19-01-03](../01-numerical-foundations/03-consistency-stability.md).

A three-point one-sided formula
$(-3u_0+4u_1-u_2)/(2h) = 0$ restores second order in principle; the ghost node is
usually preferred because it needs one extra unknown rather than a wider stencil
and keeps the matrix symmetric.

### 3.2 Physical boundaries reflect exactly

The demonstration places a pulse in a 1-D acoustic domain, a receiver in front of
the boundary, and measures $R = A_{\text{ref}}/A_{\text{inc}}$ on a second run in
which the boundary is absorbing (used only to isolate the travelling pulse):

| boundary | $h$ (m) | measured $R$ | 20 log$_{10}\lvert R\rvert$ (dB) |
|---|---|---|---|
| Dirichlet (pressure release) | 2.00 | $-1.00014789$ | 0.00 |
| Dirichlet | 1.00 | $-0.99998028$ | $-0.00$ |
| Dirichlet | 0.50 | $-0.99998107$ | $-0.00$ |
| free surface (Neumann) | 2.00 | $+1.00014789$ | 0.00 |
| free surface | 1.00 | $+0.99998028$ | $-0.00$ |
| free surface | 0.50 | $+0.99998107$ | $-0.00$ |

Both are the imposed values to $2\times10^{-5}$, and both are *supposed* to be
1 in magnitude: a physical boundary is not a defect, it is the model. The
residual $1.5\times10^{-4}$ at $h = 2$ m is dispersion and discretisation at the
boundary node, not leakage.

### 3.3 A one-way condition leaves a small, convergent residue

The same measurement for the first-order one-way condition, refined in $h$ at
fixed $C = 0.99$:

| $h$ (m) | measured $\lvert R\rvert$ | ratio to previous | dB |
|---|---|---|---|
| 2.00 | $5.53692239\times10^{-6}$ | — | $-105.13$ |
| 1.00 | $1.38262242\times10^{-6}$ | 4.0047 | $-117.19$ |
| 0.50 | $3.45513784\times10^{-7}$ | 4.0016 | $-129.23$ |
| 0.25 | $8.63741233\times10^{-8}$ | 4.0002 | — |

Each halving of $h$ quarters the reflection, so the one-way condition is
**second-order accurate**: its residual reflection is $O(h^{2})$. That is not a
coincidence — the condition is a second-order approximation to the exact
characteristic condition, and the reflection is the truncation error of that
approximation.

The $-129$ dB level is below any physical signal, so in one dimension the
one-way condition is effectively exact. In two and three dimensions it is not:
the one-dimensional form is exact only for **normal incidence**, and at angle
$\theta$ from normal the Engquist–Majlaus condition retains an $O(\sin^{2}\theta)$
reflection proportional to the square of the incidence angle. Two-dimensional
production codes therefore add a sponge (next section) or a full PML.

### 3.4 Sponge layers: two parameters and no free lunch

The demonstration appends a layer to a Dirichlet wall, with
$\sigma(x) = \sigma_{\max}\left((L_{\text{sp}}-x)/L_{\text{sp}}\right)^{2}$, and
measures the residual reflection as a function of the layer width and the peak
damping:

| layer (cells) | $\sigma_{\max} = 0.05$ | 0.20 | 0.50 | 1.00 |
|---|---|---|---|---|
| 10 | 0.9964 | 0.9860 | 0.9666 | 0.9394 |
| 20 | 0.9746 | 0.9097 | 0.8267 | 0.7778 |
| 40 | 0.8652 | 0.6494 | 0.6054 | 0.6468 |
| 80 | 0.5788 | 0.4016 | 0.4810 | 0.5399 |

Three measured facts.

- **Wider is better** at fixed damping: $0.9964 \to 0.5788$ for $\sigma_{\max} =
  0.05$ as the layer grows from 10 to 80 cells.
- **Stronger is not better**: at 80 cells, $\sigma_{\max} = 0.2$ gives
  $0.4016$ but $\sigma_{\max} = 1.0$ gives $0.5399$. The ramp itself reflects
  when the impedance changes too abruptly, so there is an interior optimum.
- The best point of this scan is $80$ cells with $\sigma_{\max} = 0.2$:
  $\lvert R\rvert = 4.016\times10^{-1}$, i.e. $-7.9$ dB. That is *poor* in
  absolute terms because the pulse used here is broad-band and only about two
  pulse widths fit in the layer; the calibration is the point, not the number.

The scaling that makes the calibration transferable: the time a wave spends in
the layer is $L_{\text{sp}}/c$, so the dimensionless group is
$\sigma_{\max}L_{\text{sp}}/c$. A well-tuned PML achieves $-60$ dB or better by
matching the impedance analytically instead of grading a loss — this lesson
measures the primitive version so that the better one has a baseline to beat.

## 4. Worked example: sizing an absorbing layer from a reflection target

*A 2-D acoustic model with $c = 2000\ \mathrm{m\,s^{-1}}$, $h = 10$ m needs a
spurious reflection below $-40$ dB ($\lvert R\rvert \le 0.01$) from its edges.*

1. From the measured table, a sponge of width $W$ cells with tuned
   $\sigma_{\max}$ behaves approximately as $\lvert R\rvert \approx
   0.4016\,(80/W)$ for $W$ between 20 and 80 cells at $\sigma_{\max} = 0.2$:
   the measured $0.4016$ at $W = 80$, $0.6494$ at $W = 40$ (predicted $0.803$),
   $0.9097$ at $W = 20$ (predicted $1.61$ — the formula fails below
   $W\approx40$, and the measurement is what tells you so).
2. To reach $\lvert R\rvert = 0.01$ the scaling would demand $W \approx
   3200$ cells, i.e. $32$ km, which is absurd: the sponge's reflection falls
   roughly as $1/W$ here, and the target is two orders of magnitude below the
   best measured value.
3. Conclusion: **the primitive sponge cannot meet $-40$ dB in 2-D at reasonable
   cost.** Either accept a larger reflection, enlarge the domain and window the
   data before the reflection arrives (the standard practice in exploration
   seismics), or implement a PML, whose reflection falls exponentially in the
   layer thickness because the impedance is matched by construction.
4. Whichever route is taken, state the number: an unmeasured boundary condition
   is an unstated model assumption.

## 5. Assumptions and regime of validity

1. **Normal incidence for the one-way condition.** The measured $-129$ dB
   applies to a plane wave hitting the boundary at $90^{\circ}$. At $30^{\circ}$
   the same condition reflects about $25\,\%$ in the classical Engquist–Majlaus
   estimate; two-dimensional tests must be oblique to be meaningful.
2. **Constant $C$ along the refinement.** The second-order convergence of the
   residual reflection was measured at $C = 0.99$; at $C = 1$ the one-way
   condition becomes exact in one dimension, and at small $C$ the interior
   dispersion dominates the measurement.
3. **Ghost nodes assume a uniform grid and an aligned boundary.** On a
   curvilinear grid the ghost position must be computed from the actual
   geometry, or the order is lost.
4. **The sponge is a modelling term, not a boundary condition.** It adds
   physical damping inside the domain, so reflections are traded for a change of
   the wavefield in the layer; the receiver must stay outside it.
5. **Order statements are about the interior.** A second-order boundary
   treatment keeps a second-order interior second order; it does not make a
   first-order interior better.
6. **Reflection measurements are geometry specific.** An aperture or a periodic
   wrap-around can be mistaken for a boundary reflection; the demonstration
   removes the direct arrival and the far-wall return by differencing against a
   uniform run, and that bookkeeping is part of the method.

## 6. Python demonstration

`code/fd_boundary_conditions_demo.py` prints:

1. the Neumann problem solved with a two-point one-sided condition and with a
   ghost node, with the observed orders $0.9992$ and $2.0000$;
2. measured reflection coefficients for Dirichlet, free surface and a one-way
   boundary at three grid spacings;
3. the second-order convergence of the one-way residual reflection (ratios
   $4.0047$, $4.0016$, $4.0002$);
4. the sponge scan over four layer widths and four damping strengths, with the
   best configuration identified.

```bash
cd 19-numerical-modeling-hpc/02-finite-difference-methods/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python fd_boundary_conditions_demo.py
```

## Mastery checkpoint

Without notes:

> A 1-D acoustic model on $(0,L)$ has a pressure-release wall at $x = 0$ and must
> be transparent at $x = L$. **(a)** State the exact reflection coefficient at
> each end and the condition that imposes it. **(b)** Implement the Neumann
> condition at a *rigid* wall with a ghost node and give the ghost value.
> **(c)** If the transparent end is implemented by a first-order one-way
> condition, state the order of its residual reflection and how you would measure
> it. **(d)** Explain why a sponge layer needs two parameters calibrated and why
> one of them is not monotonic.

Part (d) is worked, with the measured table, in
[`exercises/03-fd-boundary-conditions-solutions.md`](exercises/03-fd-boundary-conditions-solutions.md).

## Common pitfalls

1. **Settling for a first-order boundary treatment.** Measured: a $1920\times$
   larger error at the same resolution.
2. **Assuming a one-way condition works at all angles.** It is exact only at
   normal incidence; the two-dimensional oblique reflection is $O(\sin^{2}\theta)$.
3. **Cranking up the sponge damping.** §3.4 measures the optimum; beyond it the
   reflection grows again.
4. **Putting receivers inside the absorber.** The layer damps the signal, so an
   amplitude measured there is a property of the sponge.
5. **Forgetting the sign convention.** Dirichlet in pressure gives $-1$,
   free surface $+1$; mixing them inverts polarity and doubles amplitude errors.
6. **Not measuring the boundary at all.** The reflection is part of the answer;
   an unstated one is an unreported model assumption.

## Related modules

- [19-02-05 Finite-Difference Acoustic and Elastic Wave Propagation](05-fd-wave-propagation.md) —
  the same scheme in two dimensions, where oblique incidence matters.
- [19-01-03 Consistency, Stability and the Lax Equivalence Theorem](../01-numerical-foundations/03-consistency-stability.md) —
  why a boundary can break stability.
- [03-07 SymPy and Symbolic Computation](../../03-scientific-computing/07-sympy/README.md) —
  a practical way to derive one-sided and ghost-node rows without errors.
- [01-09-07 Boundary and Initial-Boundary Value Problems](../../01-mathematics/09-partial-differential-equations/07-boundary-value-problems.md).
- [Module 19-02 Finite-Difference Methods](README.md).

Exercises and worked solutions:
[`exercises/03-fd-boundary-conditions-exercises.md`](exercises/03-fd-boundary-conditions-exercises.md)
and
[`exercises/03-fd-boundary-conditions-solutions.md`](exercises/03-fd-boundary-conditions-solutions.md).
