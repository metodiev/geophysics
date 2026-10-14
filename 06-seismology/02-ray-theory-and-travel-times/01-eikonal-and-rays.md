---
id: 06-02-01
title: "Eikonal Equation, Rays and Fermat's Principle"
level: graduate
prereqs: ["06-01-01", "06-01-02", "01-09-03", "01-06-01"]
tags: [seismology, ray-theory, eikonal, fermat, travel-time, numerical]
---

# Eikonal Equation, Rays and Fermat's Principle

Seismology needs one number more often than any other: how long does the wave
take to get from there to here? The full answer requires solving the elastic
wave equation in a heterogeneous Earth and reading the arrival off the
seismogram. The cheaper answer replaces the wave by a **ray** and the wavefield
by a **travel-time function** $T(\mathbf{x})$, defined so that a surface of
constant $T$ is a wavefront and the ray is the curve perpendicular to it. That
reduction is exact only in the limit of infinite frequency, and the whole of
this lesson is an attempt to say precisely what is lost in exchange for the
simplification.

Two statements carry the theory. The first is the **eikonal equation**,

$$|\nabla T|^{2} = \frac{1}{v(\mathbf{x})^{2}},$$

a first-order nonlinear partial differential equation for the travel-time field.
The second is **Fermat's principle**, that the actual ray between two points is
the one whose travel time is stationary. They are not two theories but one
theorem and its variational shadow, and deriving both — and checking numerically
that they agree — is what this lesson does.

The honest difficulty appears at the edges of the theory. Ray theory assigns a
travel time but no amplitude, so it cannot by itself say how loud an arrival is;
it breaks down where rays focus (caustics) and where no ray exists at all
(shadows); and it carries no error bar whatsoever, so every uncertainty attached
to a ray result has to be carried in from the data or the model. Those three
limitations are announced here and paid off in
[05 Shadow Zones, Triplications and the Low-Velocity Zone](05-shadow-zones.md),
[06 Wavefront Tracking and the Fast Marching Method](06-wavefront-tracking.md)
and in the exercises of every lesson in this module.

**All models and data in this module are SYNTHETIC.** The velocity models are
chosen teaching values, not measurements, and no station, event or waveform from
the real Earth appears anywhere in this module. Where a demonstration uses a
standard reference model that ships with the software (ObsPy's `iasp91`), that
model is named, it is not data collected for this repository, and every number
quoted below is printed by the demonstration in `code/`, not recalled from a
publication.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the eikonal equation $|\nabla T|^{2} = v^{-2}$ from the scalar wave
   equation with a high-frequency (ray-series) trial solution, and **state** the
   two conditions under which the derivation is allowed.
2. **Derive** the ray equations as the characteristic equations of the eikonal
   equation, and **show** that they are equivalent to Fermat's principle.
3. **Verify** a closed-form travel-time field by substituting it into the eikonal
   equation and measuring the residual of the numerical gradient.
4. **Measure** the convergence order of a grid eikonal solver and **explain** why
   a four-point stencil can only be first order for a circular wavefront.
5. **Evaluate** the local validity condition $f^{-1}\,|\mathrm{d}v/\mathrm{d}z| \ll 1$
   for stated gradients and frequencies, and **identify** the regime where ray
   theory must not be used.
6. **Propagate** a picking error and a velocity error into a distance, and
   **state** why ray theory never supplies an uncertainty of its own.

## Prerequisites

- [06-01-01 From Hooke's Law and Newton to the Elastodynamic Equation](../01-elastic-wave-propagation/01-wave-equation-elastic.md)
  — the wave equation that is reduced here.
- [06-01-02 P and S Waves: Particle Motion, Speeds and Polarisation](../01-elastic-wave-propagation/02-p-and-s-waves.md)
  — the speed $v$ that appears in the eikonal equation.
- [01-09-03 The Wave Equation and Its Physical Content](../../01-mathematics/09-partial-differential-equations/03-wave-equation.md)
  — second-order hyperbolic equations and their characteristics.
- [01-06-01 Partial Derivatives, Gradients and Directional Derivatives](../../01-mathematics/06-multivariable-calculus/01-partial-derivatives.md)
  — the gradient and directional derivative used throughout.

## 1. The high-frequency reduction

Write the displacement for one wave type as a scalar field $u(\mathbf{x}, t)$
satisfying

$$\nabla^{2}u - \frac{1}{v(\mathbf{x})^{2}}\frac{\partial^{2} u}{\partial t^{2}} = 0 ,$$

which is what the elastodynamic equation becomes for a body wave in a medium
whose parameters vary slowly (the derivation is in
[06-01-01](../01-elastic-wave-propagation/01-wave-equation-elastic.md)). Look for
a solution that oscillates at a single, large, angular frequency $\omega$ with a
slowly varying amplitude $A$:

$$u(\mathbf{x}, t) = A(\mathbf{x})\,e^{\,i\omega\left(T(\mathbf{x}) - t\right)} .$$

$T(\mathbf{x})$ has units of time and is called the **travel-time function** or
**phase function**. Its level sets $T = \text{const}$ are the wavefronts. Now
differentiate. Since

$$\nabla u = \left(\nabla A + i\omega A \nabla T\right)e^{i\omega(T-t)},
\qquad
\partial_{t}^{2} u = -\omega^{2} A\, e^{i\omega(T-t)},$$

the Laplacian produces terms of order $\omega^{2}$, $\omega^{1}$ and $\omega^{0}$.
Substituting and collecting powers of $\omega$:

$$\omega^{2}A\left(\frac{1}{v^{2}} - |\nabla T|^{2}\right)
+ i\omega\left(2\nabla A\cdot\nabla T + A\nabla^{2}T\right)
+ \nabla^{2}A = 0 .$$

Since $\omega$ is taken to be arbitrarily large, the three groups must vanish
in turn. The order-$\omega^{2}$ equation is the **eikonal equation**:

$$\boxed{\;|\nabla T|^{2} = \frac{1}{v^{2}}\;}$$

The order-$\omega$ equation is the **transport equation**,
$2\nabla A\cdot\nabla T + A\nabla^{2}T = 0$, which would determine the amplitude
$A$ (and hence the geometric spreading) — we do not solve it here, and that
omission is the reason ray theory gives times without amplitudes. The
order-$\omega^{0}$ term is discarded as negligible at high frequency.

**Reading the equation.** $|\nabla T|$ is the slowness vector magnitude: the
travel time increases by $1/v$ per metre along the direction of steepest
descent of $T$, which is the local propagation direction. The eikonal equation
is *isotropic* in form only because $v = v(\mathbf{x})$ is scalar; anisotropy
replaces it with a direction-dependent slowness.

## 2. Rays as characteristics, and Fermat's principle

The eikonal equation is a first-order nonlinear PDE, and its solution can be
built from characteristic curves. Write it as $H(\mathbf{x}, \mathbf{p}) = 0$
with $\mathbf{p} \equiv \nabla T$ and

$$H = \tfrac{1}{2}\left(|\mathbf{p}|^{2} - v^{-2}\right).$$

The characteristic equations of such an $H$ are Hamilton's equations with $H$ as
the Hamiltonian and $T$ as the running "action":

$$\frac{\mathrm{d}\mathbf{x}}{\mathrm{d}\sigma} = \frac{\partial H}{\partial \mathbf{p}} = \mathbf{p},
\qquad
\frac{\mathrm{d}\mathbf{p}}{\mathrm{d}\sigma} = -\frac{\partial H}{\partial \mathbf{x}}
= -\frac{1}{2}\nabla\!\left(v^{-2}\right) = \frac{\nabla v}{v^{3}} .
$$

The curve $\mathbf{x}(\sigma)$ is a **ray**, and its tangent is $\mathbf{p} =
\nabla T$: rays are orthogonal to wavefronts, which is exactly the geometric
statement we started from. Differentiate $\mathbf{p} = \nabla T$ along the ray
and use $\mathrm{d}T/\mathrm{d}\sigma = |\mathbf{p}|^{2} = v^{-2}$ to convert
$\sigma$ into travel time: with $\mathrm{d}s = v\,\mathrm{d}\sigma$ the arc
length,

$$\frac{\mathrm{d}}{\mathrm{d}s}\!\left(\frac{1}{v}\frac{\mathrm{d}\mathbf{x}}{\mathrm{d}s}\right)
= \nabla\!\left(\frac{1}{v}\right),$$

the standard form of the ray equation. In a homogeneous medium the right-hand
side vanishes and rays are straight lines.

**Fermat's principle.** Define the travel time functional along an arbitrary
curve $\Gamma$ joining $\mathbf{x}_1$ to $\mathbf{x}_2$,

$$T[\Gamma] = \int_{\Gamma}\frac{\mathrm{d}s}{v(\mathbf{x}(s))}.$$

Setting the first variation to zero, $\delta T = 0$, gives precisely the ray
equation above. So the ray is a *stationary* curve of $T[\Gamma]$ — a minimum for
most configurations, a saddle or maximum at some — and "shortest time" is a
convenient fiction rather than the statement. The equivalence is a theorem, not
an analogy: the characteristics of the eikonal equation and the stationary points
of the travel-time functional are the same curves.

Section 7 verifies the equivalence on a concrete field: the field satisfies the
eikonal equation to the accuracy of a numerical gradient, and its rays are
faster than a straight line joining the same two points.

## 3. A closed form that can be tested, not remembered

For a velocity that increases linearly with depth,
$v(z) = v_0 + g z$ with constant $g > 0$, the travel-time field relative to a
point source at the surface has the closed form

$$T(x, z) = \frac{1}{g}\,\mathrm{arccosh}\!\left(1 +
\frac{g^{2}\left(x^{2}+z^{2}\right)}{2\,v_0\left(v_0 + g z\right)}\right).$$

The right way to read such a formula is as a *candidate*, to be tested. The
demonstration `code/eikonal_and_rays_demo.py` evaluates it on a grid, takes the
numerical gradient, and prints the largest value of the dimensionless residual

$$R = |\nabla T|\, v(z) - 1$$

over the interior. Two facts come out of the run. With $v_0 = 2000\
\mathrm{m\,s^{-1}}$ and $g = 0.50\ \mathrm{s^{-1}}$, $T(0,0)$ evaluates to
$0.000000\times10^{0}$ s, so the field is correctly anchored at the source, and
the maximum residual is $1.490\times10^{-3}$ — the truncation error of a
second-order numerical gradient, not a failure of the formula. The closed form
*is* a solution of the eikonal equation to that accuracy, which is what makes it
usable as a reference.

**Why a linear gradient?** Because its rays are exactly circular arcs, so it
provides a case where every quantity — path, travel time, turning depth — is
known independently, and any numerical method can be checked against it. That
same model is used again in
[04 Ray Tracing in Laterally Varying Media](04-ray-tracing.md).

## 4. Solving the eikonal equation on a grid

Analytic solutions exist for few velocity fields, so the eikonal equation is
usually solved numerically. The idea is to discretise $|\nabla T| = 1/v$ with an
*upwind* difference: at each node, the derivative is taken from whichever
neighbour already has the smaller travel time, so information flows outward from
the source and no node is updated from a value that depends on itself.

For a uniform grid of spacing $h$ the four-point stencil is

$$\left(\frac{\max\left(D^{-}_{x}T,\,-D^{+}_{x}T,\,0\right)^{2}
+ \max\left(D^{-}_{z}T,\,-D^{+}_{z}T,\,0\right)^{2}}{h^{2}}\right) = \frac{1}{v^{2}},$$

a quadratic in the unknown $T$ at each node. Solving the nodes in increasing
order of travel time, accepting a node permanently once it is the smallest
remaining, is the **fast marching method** (Section 4 of the demonstration);
sweeping the whole grid repeatedly in alternating directions until nothing
changes is the **fast sweeping method** (developed in
[06 Wavefront Tracking and the Fast Marching Method](06-wavefront-tracking.md)).
Both are used in `code/eikonal_and_rays_demo.py`, which validates them against
the exact circular wavefront in a homogeneous medium.

The measured errors are

| grid spacing $h$ | grid size | max absolute error | max relative error |
|---|---|---|---|
| 200 m | 61 × 61 | 91.645 ms | $1.208\times10^{-1}$ |
| 100 m | 121 × 121 | 53.557 ms | $1.208\times10^{-1}$ |
| 50 m | 241 × 241 | 30.733 ms | $1.208\times10^{-1}$ |
| 25 m | 481 × 481 | 17.371 ms | $1.208\times10^{-1}$ |

for $v = 3000\ \mathrm{m\,s^{-1}}$ on a 12 km square with the source in a corner.
Halving the grid spacing roughly halves the error — the fitted convergence order
is **0.800** — and the *maximum relative* error is stuck at $12.08\%$ because it
occurs in the few cells nearest the source, where the error is a fixed fraction
of a tiny travel time and does not improve with refinement. On the linear
gradient the same comparison against the closed form gives $60.291$ ms at
$h = 100$ m falling to $15.957$ ms at $h = 25$ m, a measured order of **0.959**.

First order is not an implementation defect. The exact solution of the
homogeneous problem is a circular wavefront, and the true ray to a diagonal
neighbour crosses the cell diagonally, while the four-point stencil can only
combine axis-aligned steps. The staircase approximates the diagonal, and a
staircase converges to a diagonal at first order in $h$. The lesson to carry
forward is a habit: **state the order, and check it**, because the order is what
tells you how far you can trust a number you cannot compare with an analytic
solution.

## 5. The regime in which ray theory is allowed

The reduction in Section 1 discarded a term of order $\omega^{0}$ against $\omega^{2}$;
converting that hierarchy into a statement about the medium, the dimensionless
group that must be small is the fractional change of velocity over one
wavelength,

$$\varepsilon \equiv \frac{\lambda}{v}\left|\frac{\mathrm{d}v}{\mathrm{d}z}\right|
= \frac{1}{f}\left|\frac{\mathrm{d}v}{\mathrm{d}z}\right| \ll 1 ,$$

where $\lambda = v/f$ has been used — so the criterion is independent of the
velocity and depends only on the gradient and the frequency. The demonstration
prints the following table at $f = 10$ Hz on the $2000 + 0.5z$ model:

| $\mathrm{d}v/\mathrm{d}z$ (s⁻¹) | $v$ (m s⁻¹) | $\lambda$ (m) | $\varepsilon$ |
|---|---|---|---|
| 0.050 | 2000.0 | 200.00 | 0.0050 |
| 0.200 | 2000.0 | 200.00 | 0.0200 |
| 0.500 | 2000.0 | 200.00 | 0.0500 |
| 2.000 | 2000.0 | 200.00 | 0.2000 |
| 10.000 | 2000.0 | 200.00 | 1.0000 |

At 10 Hz a gradient of $10\ \mathrm{s^{-1}}$ changes the velocity by 100 per cent
within a single wavelength: $\varepsilon = 1$, the wavefront is no longer locally
planar, and the ray description has no meaning. A gradient of
$2\ \mathrm{s^{-1}}$ gives $\varepsilon = 0.2$ and is already marginal. This is
why ray theory works beautifully for teleseismic body waves (tens of metres of
wavelength change little over a wavelength in the mantle) and fails for
high-frequency waves crossing a sharp interface — where the correct apparatus is
reflection and transmission coefficients, not rays.

## 6. Assumptions and the regime of validity

The eikonal equation is a **leading-order asymptotic** description, and the
following must hold for it to be the right tool:

1. **High frequency, relative to the medium.** $\varepsilon \ll 1$ as in
   Section 5. There is no fixed frequency below which rays stop working; the
   criterion couples the frequency to the gradient.
2. **No edges, no caustics, no shadows.** The derivation assumes the wavefront
   is smooth and single-valued. Where rays focus, $|\nabla T|$ stays finite but
   the *amplitude* $A$ diverges, and the transport equation we dropped is exactly
   the one that carries that divergence. Where no ray reaches a point, the
   eikonal solution is undefined and the observed energy there is diffracted or
   scattered. That failure is measured in
   [05 Shadow Zones, Triplications and the Low-Velocity Zone](05-shadow-zones.md).
3. **Only the first arrival, for the standard solvers.** A grid eikonal solver
   returns the *minimum* travel time at each node. Any later arrival that shares
   the node is invisible to it, which means a triplication cannot be represented
   by a fast marching solution at all. Getting later arrivals requires either
   solving the transport equation along specified rays or tracking wavefronts
   with mode separation.
4. **Isotropy.** $|\nabla T| = 1/v$ presumes a scalar speed. In an anisotropic
   medium the slowness depends on direction and the eikonal equation must be
   replaced by its anisotropic form (see
   [06-01-08 Wave Propagation in Anisotropic Media](../01-elastic-wave-propagation/08-anisotropic-propagation.md)).
5. **Travel times, not amplitudes — and not uncertainty.** Nothing in this
   lesson produces an error bar.

## 7. Worked examples

### Example 1 — the closed form, and Fermat's principle, on the same model

Take $v_0 = 2000\ \mathrm{m\,s^{-1}}$, $g = 0.50\ \mathrm{s^{-1}}$, and ask for
the travel time from the source at $(0,0)$ to the point $(6.0, 3.0)$ km.

1. The argument of the arccosh:
   $g^{2}(x^{2}+z^{2}) = 0.25 \times (36 + 9)\times10^{6} = 1.125\times10^{7}$;
   $2 v_0 (v_0 + g z) = 4000 \times (2000 + 1500) = 1.400\times10^{7}$;
   the ratio is $0.803571$, so the argument is $1.803571$.
2. $\mathrm{arccosh}(1.803571) = 1.195313$, giving
   $T = 1.195313 / 0.50 = 2.39059\ \mathrm{s}$.
3. The straight-line distance is
   $\sqrt{6000^{2} + 3000^{2}} = 6708.20$ m, so the *implied* mean speed along
   the chord is $6708.20 / 2.39059 = 2806.1\ \mathrm{m\,s^{-1}}$.
4. Now compute the time along the chord — a deliberately non-stationary path.
   With $\mathrm{d}s = \sqrt{1 + (x/z)^{2}}\,\mathrm{d}z = \sqrt{5}\,\mathrm{d}z$,
   $$T_{\text{chord}} = \int_{0}^{3000}\frac{\sqrt{5}\;\mathrm{d}z}{2000 + 0.5z}
   = 2\sqrt{5}\,\ln\frac{3500}{2000} = 2.50268\ \mathrm{s}.$$
5. The stationary path is shorter in time by $2.50268 - 2.39059 =
   0.11209$ s, i.e. $4.689\%$. Fermat's principle is confirmed as a *measurement*
   on this model: the ray beats the straight line, and by the amount the theory
   predicts.

### Example 2 — what a grid solver returns, and how well

On the same model the fast marching solution at $h = 25$ m is within
$15.957$ ms of the closed form at the worst node, on travel times of order one
second — a relative error of about $1\%$ at the worst node and far less away
from the source. The measured order is $0.959$. Quoting a grid travel time
without the grid spacing is therefore meaningless: the discretisation error is
first order in $h$, so it is a *documented* number, not noise.

### Example 3 — the uncertainty that ray theory does not provide

Put a receiver at $(6.0, 6.0)$ km in a homogeneous $v = 3000\ \mathrm{m\,s^{-1}}$
medium and suppose the arrival is picked with a stated uncertainty of
$\sigma_t = 5.0$ ms on an exact time of $2.828427$ s. Inverting $r = v t$ over
4000 realisations gives a distance of $8485.165 \pm 14.933$ m, against a true
$8485.281$ m — a relative scatter of $0.176\%$. Now hold the time fixed and
mis-specify the velocity instead: a 0.5 per cent velocity error moves the same
distance by $42.43$ m, **2.8 times** the picking scatter. The eikonal solver
returned the first number and knew nothing about the second; both had to be
supplied from outside. This is the sense in which a ray result is never more
certain than its inputs.

## 8. Python demonstration

`code/eikonal_and_rays_demo.py` runs in a few seconds and prints four labelled
sections with units:

1. **Fast marching on a homogeneous medium, refined in $h$** — the closed-form
   circular wavefront against the grid solution at four spacings, with the fitted
   convergence order ($0.800$) and the stuck maximum relative error
   ($1.208\times10^{-1}$).
2. **A linear gradient** — $T(0,0) = 0$, the eikonal residual of the closed form
   ($1.490\times10^{-3}$), and the grid-versus-closed-form errors and order
   ($0.959$).
3. **The validity condition** — the $\varepsilon$ table of Section 5.
4. **What a picking error does to a distance** — the Monte Carlo of Example 3,
   including the statement that a 0.5 per cent velocity error outweighs a 5 ms
   pick.

Run it with the project virtual environment:

```bash
cd 06-seismology/02-ray-theory-and-travel-times/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python eikonal_and_rays_demo.py
```

## Mastery checkpoint

Complete this without notes:

> A homogeneous medium has $v = 3000\ \mathrm{m\,s^{-1}}$. **(a)** Write the
> travel-time field for a point source at the origin and verify that it satisfies
> the eikonal equation exactly. **(b)** State the ray equation for a medium with
> $\nabla v = 0$ and say what its solutions are. **(c)** For
> $v(z) = 2000 + 0.5z\ \mathrm{m\,s^{-1}}$ at $f = 25$ Hz, compute $\varepsilon$
> and decide whether a ray description is defensible. **(d)** A grid solver on a
> 100 m grid returns a travel time to a receiver 8 km away; state the sign of the
> error you expect from the staircase effect and the order in $h$ in which it
> falls. **(e)** Name the two things the eikonal equation does not give you.

A worked version of (a)–(c) appears in the lesson
[solutions](exercises/01-eikonal-and-rays-solutions.md).

## Common pitfalls

1. **Treating the eikonal equation as exact.** It is the leading term of an
   asymptotic series; the discarded term is the one that gives amplitudes, and
   the discarded term is the one that diverges at a caustic.
2. **Quoting a grid travel time without the grid spacing.** First order in $h$
   means the number changes by tens of milliseconds when the grid is refined.
3. **Using ray theory across a sharp interface.** $\varepsilon \ll 1$ fails there
   by construction; the correct apparatus is reflection and transmission
   coefficients.
4. **Expecting a standard eikonal solver to return later arrivals.** It returns
   the first arrival by construction, so a triplication is invisible to it.
5. **Believing "shortest time" literally.** The ray is a *stationary* path; in
   strongly heterogeneous media it can be a saddle.
6. **Asking a ray for its error bar.** There is none; propagate the input
   uncertainties yourself, as in Example 3.

## Related modules

- [06-01 Elastic Wave Propagation](../01-elastic-wave-propagation/README.md) —
  where the wave equation being reduced here comes from.
- [02 Snell's Law, Layered Media and the Travel-Time Curve](02-snell-and-layering.md) —
  the eikonal equation specialised to a stack of constant-velocity layers.
- [03 The tau-p Transform and Intercept Time](03-tau-p.md) — the same travel
  times rearranged into a slowness domain.
- [04 Ray Tracing in Laterally Varying Media](04-ray-tracing.md) — the ray
  equations of Section 2 solved as a two-point boundary-value problem.
- [05 Shadow Zones, Triplications and the Low-Velocity Zone](05-shadow-zones.md) —
  measured, not asserted: what happens where the eikonal equation has no
  single-valued solution.
- [06 Wavefront Tracking and the Fast Marching Method](06-wavefront-tracking.md) —
  the two grid solvers compared in detail.
- [19-numerical-modeling-hpc](../../19-numerical-modeling-hpc/README.md) — the
  systematic treatment of discretisation, order and stability.

## Exercises

Full sets with worked solutions are in
[`exercises/01-eikonal-and-rays-exercises.md`](./exercises/01-eikonal-and-rays-exercises.md)
and
[`exercises/01-eikonal-and-rays-solutions.md`](./exercises/01-eikonal-and-rays-solutions.md).
