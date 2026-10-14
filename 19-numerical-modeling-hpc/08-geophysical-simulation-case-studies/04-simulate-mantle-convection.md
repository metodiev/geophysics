---
id: 19-08-04
title: "Simulating Mantle Convection"
level: research
prereqs: ["19-07-01", "19-07-02", "13-02-01"]
tags: [numerical-modelling, verification, mantle-convection, rayleigh-benard, linear-stability, nusselt-number]
---

# Simulating Mantle Convection

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the non-dimensional Rayleigh-Bénard problem and the Rayleigh number
   from the Boussinesq equations.
2. **Verify** a conduction solver against an exact solution with internal heating
   and **measure** its order of accuracy.
3. **Derive** the marginal-stability eigenvalue problem for free-slip boundaries
   and the exact critical Rayleigh number $27\pi^{4}/4$.
4. **Compute** the critical Rayleigh number from a discretised operator and
   **measure** its convergence to the exact value.
5. **Compute** the unstable band of wavenumbers at a stated supercritical Rayleigh
   number, and **state** what it implies for the resolution a simulation needs.
6. **Verify** a time-dependent convection solver against exact linear theory, and
   **state** honestly why the heat transport of a short demonstration run is not a
   Nusselt number.

## Prerequisites

- [19-07-01 Code Verification: Order-of-Accuracy and Manufactured Solutions](../07-verification-validation-uncertainty/01-code-verification.md)
  and [19-07-02 Solution Verification](../07-verification-validation-uncertainty/02-solution-verification.md).
- [13-02-01 Rayleigh-Benard Convection Applied to the Mantle](../../13-geodynamics-tectonics/02-mantle-convection/01-rayleigh-benard-mantle.md)
  — the physics this lesson simulates.

All models and data in this module are **SYNTHETIC**: a chosen Rayleigh number,
box and resolution. The critical Rayleigh number and the linear growth rate are
exact results for the stated equations, and every other number is printed by this
lesson's demonstration.

## 1. Intuition: convection is a stability problem before it is a flow

The mantle convects because a fluid heated from below becomes unstable. That
sentence has a quantitative form, and the quantitative form is the reason
convection modelling has a well-defined verification problem: **below a critical
Rayleigh number the conduction solution is stable, and above it a band of
wavenumbers grows.** Both the threshold and the growth rates follow from an
eigenvalue problem that can be solved exactly for the idealised (free-slip,
constant-viscosity, Boussinesq) case, and that exact solution is a benchmark of the
rare kind: it tests the *linear physics* directly rather than through a flow field.

A convection code therefore has three distinct things to verify, and the
demonstration does all three:

1. **The conduction solution.** With internal heating, the steady purely conductive
   temperature profile has a closed form and the discretisation either reproduces it
   at its design order or it does not.
2. **The stability threshold.** The discrete operator's eigenvalues give a critical
   Rayleigh number that must converge to the exact $27\pi^{4}/4$ as the grid is
   refined.
3. **The time integration.** A small perturbation of the conduction state grows
   exponentially at a rate that exact linear theory predicts, so a short linear run
   verifies the time stepping and the buoyancy coupling without ever entering the
   nonlinear regime.

What is left — the heat transport of the fully nonlinear flow — is the hard part,
and Section 5.6 explains why a demonstration cannot deliver it and what a
defensible number would require.

## 2. Definitions

**Boussinesq approximation.** Density variations are retained only in the buoyancy
term; the flow is incompressible.

**Rayleigh number.** With $\alpha$ the thermal expansivity, $g$ gravity, $\Delta T$
the temperature drop, $d$ the layer depth, $\kappa$ the thermal diffusivity and
$\nu$ the kinematic viscosity,

$$\mathrm{Ra} = \frac{\alpha g\Delta T d^{3}}{\kappa\nu},$$

the ratio of buoyant driving to diffusive and viscous damping.

**Nusselt number.** The ratio of the actual heat transport to the purely conductive
transport, $\mathrm{Nu} = \langle -\,\mathrm{d}T/\mathrm{d}z\rangle_{\text{wall}}$
in the units where the conductive flux is unity. $\mathrm{Nu} = 1$ below the
threshold, $\mathrm{Nu} > 1$ above it.

**Marginal stability.** The condition that a disturbance neither grows nor decays,
$\sigma = 0$ in the normal-mode ansatz $e^{\sigma t}$.

**Unstable band.** The set of horizontal wavenumbers with positive growth rate at a
stated $\mathrm{Ra}$.

## 3. Derivations

### 3.1 The non-dimensional problem

Non-dimensionalise lengths by $d$, time by $d^{2}/\kappa$, and temperature by
$\Delta T$. With the Prandtl number $\mathrm{Pr} = \nu/\kappa$, the linearised
equations about the conduction state $T_0 = 1 - z$ are

$$\partial_t\zeta = \mathrm{Pr}\left(\nabla^{2}\zeta - \mathrm{Ra}\,\partial_x\theta\right),
\qquad
\partial_t\theta = \nabla^{2}\theta - w ,$$

where $\theta$ is the temperature perturbation, $\zeta = \nabla^{2}\psi$ the
vorticity, $w = -\partial_x\psi$ the vertical velocity, and the sign of the
buoyancy term follows from taking $\partial_z$ of the horizontal momentum equation
minus $\partial_x$ of the vertical one. **Getting this sign right is the single
commonest error in a convection code, and Section 5.4 shows the measurable symptom
of getting it wrong: every perturbation decays at every Rayleigh number.**

### 3.2 Conduction with internal heating

For $-k T'' = H_0(1 + z^{2}/d^{2})$ on $(0,d)$ with $T(0) = T_0$ and $T(d) = T_1$,

$$T(z) = T_0 + C_1 z - \frac{H_0}{k}\left(\frac{z^{2}}{2} + \frac{z^{4}}{12}\right),
\qquad C_1 = (T_1 - T_0) + \frac{7}{12}\frac{H_0}{k},$$

verified by differentiation. The quartic term matters: with a quadratic or cubic
exact solution the three-point stencil would reproduce it *exactly*, and the
"convergence test" would measure nothing at all (the demonstration's first version
did precisely that, and the fix is one exponent).

### 3.3 The marginal-stability eigenvalue problem

Eliminating $\theta$ and $w$ between the steady linear equations gives, with
$D = \mathrm{d}/\mathrm{d}z$ and normal modes $\propto e^{\mathrm{i}kx}$,

$$(D^{2} - k^{2})^{3}\Psi = -k^{2}\,\mathrm{Ra}\,\Psi .$$

For free-slip boundaries $\Psi = \sin(n\pi z)$ is admissible, and
$(D^{2}-k^{2})\sin(n\pi z) = -(n^{2}\pi^{2}+k^{2})\sin(n\pi z)$, so

$$\mathrm{Ra}(n,k) = \frac{(n^{2}\pi^{2} + k^{2})^{3}}{k^{2}} .$$

Minimising over $k$ at fixed $n = 1$: $\mathrm{d}\mathrm{Ra}/\mathrm{d}k = 0$ gives
$2k^{2} = \pi^{2}$, i.e. $k_c = \pi/\sqrt{2}$, and

$$\mathrm{Ra}_c = \frac{(3\pi^{2}/2)^{3}}{\pi^{2}/2}
= \frac{27\pi^{6}/8}{\pi^{2}/2} = \frac{27\pi^{4}}{4} = 657.5114 ,$$

with critical wavelength $2\pi/k_c = 2\sqrt{2}\,d$. **The lowest mode at the
critical wavenumber is the first to convect, and both numbers are exact.**

### 3.4 The linear growth rate

Keeping the time derivatives, the two-field system has determinant

$$(\sigma + \lambda)^{2} = k_{\text{eff}}^{2}\,\frac{\mathrm{Ra}}{\lambda},
\qquad \lambda = k_x^{2} + k_z^{2}
\;\Longrightarrow\;
\sigma = -\lambda + k_{\text{eff}}\sqrt{\frac{\mathrm{Ra}}{\lambda}},$$

using the discrete eigenvalues of the operators actually implemented. The threshold
$\sigma = 0$ reproduces $\mathrm{Ra} = \lambda^{3}/k_{\text{eff}}^{2}$, the
$(\text{wavenumber})^{3}$ form of Section 3.3. This is the relation the
demonstration tests: it involves the time step, the buoyancy coupling and the
Poisson solve together, so a sign or factor error anywhere in the coupling shows up
as a wrong growth rate.

## 4. Resolution requirements

Two length scales set the cost:

- **The thermal boundary layer.** Its thickness scales as $\mathrm{Ra}^{-1/3}$ in
  the classical boundary-layer scaling, so a run at $\mathrm{Ra} = 10^{7}$ needs an
  order of magnitude more vertical points than one at $\mathrm{Ra} = 10^{4}$, and
  this is the requirement that pushes geodynamics onto supercomputers.
- **The critical wavelength.** A box narrower than $2\sqrt{2}$ layer depths cannot
  contain the most unstable mode, so a small domain under-resolved in aspect ratio
  may not convect at all whatever the Rayleigh number.

The demonstration measures the unstable band — how it widens with $\mathrm{Ra}$ —
because that width is exactly the range of cell sizes the grid must be able to
represent.

## 5. Measured evidence

The demonstration `code/simulate_mantle_convection_demo.py` runs in about $8$ s.

### 5.1 Conduction with internal heating

$-k T'' = H_0(1+z^{2}/d^{2})$, $H_0 = 3$ W m$^{-3}$, $k = 3$ W m$^{-1}$K$^{-1}$,
$T_0 = 300$ K, $T_1 = 1300$ K, $d = 1$:

| $N$ | $\Delta z$ | max $\lvert T_{\text{num}} - T_{\text{exact}}\rvert$ (K) | order |
|---:|---:|---:|---:|
| 8 | 0.12500 | $3.2552\times10^{-4}$ | — |
| 16 | 0.06250 | $8.1380\times10^{-5}$ | 2.000 |
| 32 | 0.03125 | $2.0345\times10^{-5}$ | 2.000 |
| 64 | 0.01562 | $5.0863\times10^{-6}$ | 2.000 |
| 128 | 0.00781 | $1.2716\times10^{-6}$ | 2.000 |

Exactly second order, as the three-point stencil predicts. A conduction benchmark is
the cheapest and most useful test in geodynamics: every convection code must
reproduce it before any flow is trusted.

### 5.2 The critical Rayleigh number from the discrete operator

Building $(A_1 - k^{2}I)^{3}$ with $A_1$ the one-dimensional Dirichlet second
difference and solving the eigenvalue problem for each $k$ on a fine grid:

| $N$ | $\mathrm{Ra}_c$ (discrete) | error vs $27\pi^{4}/4$ | order |
|---:|---:|---:|---:|
| 8 | 640.806070 | $1.6705\times10^{1}$ | — |
| 16 | 653.300169 | $4.2112\times10^{0}$ | 1.988 |
| 32 | 656.456590 | $1.0548\times10^{0}$ | 1.997 |
| 64 | 657.247622 | $2.6374\times10^{-1}$ | 2.000 |
| 128 | 657.445805 | $6.5559\times10^{-2}$ | 2.008 |

The discrete operator's threefold action converges to the exact value at second
order, and the minimising $k$ approaches $\pi/\sqrt{2} = 2.2214$ to within the
$7.5\times10^{-3}$ spacing of the $k$ scan (the demonstration prints the column). This is code
verification against an exact analytic result applied to a *stability* operator
rather than to a boundary-value problem, and it catches exactly the class of error
— a wrong coefficient in the linearised equations — that a conduction test cannot
see.

### 5.3 The unstable band

For $\mathrm{Ra}$ above $\mathrm{Ra}_c$ a band of wavenumbers grows:

| $\mathrm{Ra}/\mathrm{Ra}_c$ | $k_{\min}$ | $k_{\max}$ | width | fastest $k$ |
|---:|---:|---:|---:|---:|
| 1.01 | 2.0358 | 2.4207 | 0.3849 | 2.2233 |
| 1.50 | 1.2215 | 3.7779 | 2.5563 | 2.2233 |
| 2.00 | 0.9847 | 4.4391 | 3.4545 | 2.2233 |
| 10.00 | 0.3925 | 8.1058 | 7.7134 | 2.2233 |

At $10\,\mathrm{Ra}_c$ the band spans a factor of $20$ in wavelength, so a
simulation must represent features from about $0.8$ to about $16$ layer depths —
which is the quantitative statement behind "a convection model needs a wide box".

### 5.4 The time integration against exact linear theory

A $10^{-4}$-amplitude perturbation is time-stepped with the advection switched off
and the growth rate fitted after the decaying mode has died away:

| $\mathrm{Ra}$ | $\lambda$ (fundamental mode) | predicted $\sigma$ | measured $\sigma$ | difference |
|---:|---:|---:|---:|---:|
| 2500 | 14.7833 | 14.0224 | 13.7998 | −1.588% |
| 10000 | 14.7833 | 42.8281 | 42.5390 | −0.675% |

The measured growth rate reproduces the discrete linear-theory prediction to
better than $1.6$ per cent. Two remarks. First, **including the initial transient
in the fit biases it low by tens of per cent** — the first version of the
demonstration measured $6.9$ instead of $14.0$ at $\mathrm{Ra} = 2500$ — which is
a lesson about exponential fitting, not about convection. Second, the same
signature appears if the buoyancy term has the wrong sign: then *every* measured
$\sigma$ is negative, and the run never convects. A single linear-growth measurement
distinguishes "the physics is wrong" from "the resolution is wrong".

### 5.5 The nonlinear run, and its invariant

Free-slip top and bottom, periodic sides, $\mathrm{Pr} = 1$, box
$2\sqrt{2} \times 1$. Records are $(t, \mathrm{Nu}, \max\lvert\theta\rvert)$, where
$\max\lvert\theta\rvert \le 1$ is a physical invariant of $T$ (it stays between the
boundary values):

| $\mathrm{Ra}$ | grid | late records |
|---:|---|---|
| 2500 | $48\times24$ | $0.33:1.85/0.42$, $0.42:2.97/0.56$, $0.50:2.95/0.54$ |
| 10000 | $64\times32$ | $0.20:5.09/0.63$, $0.25:5.03/0.63$, $0.30:5.04/0.62$ |
| 10000 | $96\times48$ | $0.13:4.92/0.69$, $0.17:4.50/0.58$, $0.20:5.10/0.63$ |

The Nusselt number settles near $2.9$ at $\mathrm{Ra} = 2500$ and near $5.0$ at
$\mathrm{Ra} = 10^{4}$, and the invariant is respected in every record.

### 5.6 Why those Nusselt numbers are not a result

Refining $64\times32$ to $96\times48$ at the same $\mathrm{Ra}$ moves
$\mathrm{Nu}$ by per cent-level amounts — the same size as the effect being
measured. The runs are also only a fraction of a diffusion time long, and the
averaging window is three records. **A defensible Nusselt number needs a resolution
study in both directions, a run many diffusion times long, and a stated averaging
window**, none of which fits a twenty-second demonstration. The honest conclusion is
the one the demonstration prints: it establishes the machinery (an exact conduction
benchmark, an exact stability threshold reproduced at second order, a time
integration verified against linear theory) and it does not establish $\mathrm{Nu}$.

## 6. Assumptions and regime of validity

1. **Boussinesq, constant viscosity, constant properties.** Temperature-dependent
   viscosity changes the planform, the boundary-layer structure and the heat
   transport; it needs its own verification.
2. **Free-slip boundaries in the stability analysis.** Rigid boundaries raise
   $\mathrm{Ra}_c$ to $1707.76$ for the same geometry, so the exact benchmark is for
   the free-slip problem and must not be quoted for a no-slip code.
3. **Two-dimensional, aspect ratio $2\sqrt{2}$.** A box that cannot contain the
   critical wavelength cannot convect; a wider box admits more modes and a
   different mean flow.
4. **Pr = 1.** Mantle convection is $\mathrm{Pr} \sim 10^{23}$: this demonstration
   is not the mantle, it is the equations the mantle is modelled with.
5. **A grid that resolves the thermal boundary layer.** At
   $\mathrm{Ra} = 10^{4}$ the layer is a few per cent of the depth; a coarse grid
   overestimates heat transport, and the demonstration's $64\times32$ result is
   evidence of that.
6. **What is not established.** Anything about the Earth's mantle: the viscosity
   structure, the internal heating distribution, the plate-like surface behaviour
   and the temperature-dependence of every property are model choices, not
   measurements made here.

## 7. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| Rayleigh number | $\mathrm{Ra}$ | dimensionless | $\alpha g\Delta T d^{3}/(\kappa\nu)$ |
| Prandtl number | $\mathrm{Pr}$ | dimensionless | $\nu/\kappa$ |
| Nusselt number | $\mathrm{Nu}$ | dimensionless | conductive flux = 1 |
| wavenumber | $k$ | m$^{-1}$ (here $d^{-1}$) | $k_c = \pi/\sqrt{2}$ per layer depth |
| growth rate | $\sigma$ | $\kappa/d^{2}$ | set to 1 by the scaling |
| heat production | $H_0$ | W m$^{-3}$ | |

A useful sanity check: $\mathrm{Ra}$ is invariant under any consistent change of
units, and the critical wavenumber is a *pure number* per layer depth. If a
$\mathrm{Ra}_c$ comes out as $10^{6}$ or $10^{-3}$, a length has been raised to the
wrong power.

## 8. Worked examples

### Example 1 — the critical Rayleigh number by hand

$\mathrm{Ra}(1,k) = (\pi^{2}+k^{2})^{3}/k^{2}$. Differentiating with respect to
$q = k^{2}$: $\mathrm{d}/\mathrm{d}q\left[(\pi^{2}+q)^{3}q^{-1}\right] =
(\pi^{2}+q)^{2}(2q-\pi^{2})/q^{2}$, zero at $q = \pi^{2}/2$, i.e.
$k_c = \pi/\sqrt{2} = 2.2214$. Then

$$\mathrm{Ra}_c = \frac{(\pi^{2} + \pi^{2}/2)^{3}}{\pi^{2}/2}
= \frac{(1.5\pi^{2})^{3}}{0.5\pi^{2}} = 6.75\pi^{4} = 657.5114 ,$$

where $\pi^{4} = 97.4091$. The critical wavelength is
$2\pi/k_c = 2\sqrt{2} = 2.8284$ layer depths — the demonstration's numbers exactly.

### Example 2 — the growth rate by hand

At $\mathrm{Ra} = 2500$ in a box whose fundamental mode has $k_x = 2\pi/L_x =
2.2214$ (because $L_x = 2\sqrt{2}$) and $k_z = \pi$:
$\lambda = k_x^{2} + k_z^{2} = 4.935 + 9.870 = 14.805$ and

$$\sigma = -14.805 + 2.2214\sqrt{2500/14.805}
= -14.805 + 2.2214\times12.997 = -14.805 + 28.874 = 14.07 .$$

The demonstration measures $13.80$ using the *discrete* $\lambda = 14.7833$, which
predicts $14.02$: the residual $0.2$ per cent is the finite-difference symbol
against the continuum one. Both agree that the e-folding time is about $0.07$
diffusion times, which is why a perturbation reaches finite amplitude within a few
tenths of a diffusion time.

### Example 3 — the cost of resolving the boundary layer

At $\mathrm{Ra} = 10^{4}$ a boundary layer of thickness $0.05$ layer depths needs
$\Delta z \le 0.02$ to be resolved by a few points, i.e. $N_z \ge 50$; the
demonstration uses $32$, which is why its $\mathrm{Nu}$ is not converged. Raising
$\mathrm{Ra}$ to $10^{7}$ shrinks the layer by a further factor of $10$ and pushes
$N_z$ past $500$, with the horizontal resolution scaling accordingly: **the cost of
a mantle convection model grows faster than linearly in the Rayleigh number, and it
is the boundary layer, not the interior, that sets it.**

### Example 4 — a verification statement

> Verification: conduction with internal heating against the exact quartic
> profile, order $2.000$ at five resolutions; critical Rayleigh number from the
> discrete operator, second-order convergence to the exact $27\pi^{4}/4 =
> 657.5114$ with $k_c = \pi/\sqrt{2}$; linear growth rate against the exact
> discrete prediction, agreement to $1.6$ per cent after the transient, at two
> Rayleigh numbers. Not verified: the nonlinear heat transport. The reported
> $\mathrm{Nu} \approx 2.9$ and $5.0$ move by per cent-level amounts when the grid
> is refined, so they are quoted as a demonstration of the machinery, not as
> results.

## 9. Python demonstration

```bash
cd 19-numerical-modeling-hpc/08-geophysical-simulation-case-studies/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python simulate_mantle_convection_demo.py
```

Print-only, no file output, no network, exits 0, about $8$ s.

## 10. Exercises

[`exercises/04-simulate-mantle-convection-exercises.md`](exercises/04-simulate-mantle-convection-exercises.md)
and
[`exercises/04-simulate-mantle-convection-solutions.md`](exercises/04-simulate-mantle-convection-solutions.md)
include deriving $\mathrm{Ra}_c$, computing the unstable band, and designing a
resolution study for a stated Nusselt number.

## 11. Applications

- **Mantle convection modelling.** Ra, Nu and the boundary-layer scaling are the
  language of the field
  ([13-02-02 Numerical Modelling of Mantle Convection](../../13-geodynamics-tectonics/02-mantle-convection/02-convection-numerical.md)).
- **Community benchmarking.** Geodynamics has an established benchmark culture
  precisely because the linear threshold and the conduction solution give exact
  targets ([13-05-03 Benchmarking Geodynamic Codes](../../13-geodynamics-tectonics/05-geodynamic-modelling/03-benchmarking-geodynamics.md)).
- **Other convecting fluids.** The same equations describe the outer core, magma
  chambers and industrial flows, with different Prandtl numbers and boundary
  conditions.
- **Nonlinear stability in general.** Convection is the archetype of a problem
  where the linear theory is exactly solvable and the nonlinear regime is not,
  which is why it is the standard test case for any new solver.

## 12. Further study

- [13-02-01](../../13-geodynamics-tectonics/02-mantle-convection/01-rayleigh-benard-mantle.md)
  and [13-02-02](../../13-geodynamics-tectonics/02-mantle-convection/02-convection-numerical.md).
- [19-07-01](../07-verification-validation-uncertainty/01-code-verification.md) and
  [19-07-02](../07-verification-validation-uncertainty/02-solution-verification.md).
- [19-03-05 FEM in Geophysics](../03-finite-element-and-volume/05-fem-geophysics.md)
  — the alternative discretisation for the same equations.

## Mastery checkpoint

Without notes:

> A free-slip Rayleigh-Bénard box is $2\sqrt{2}$ layer depths wide and one deep.
> **(a)** State the critical Rayleigh number and the wavenumber of the first mode,
> and show by differentiation that they minimise the exact branch. **(b)** At
> $\mathrm{Ra} = 5000$ compute the growth rate of the fundamental mode and its
> e-folding time in diffusion units. **(c)** State the vertical resolution needed if
> the thermal boundary layer is $5$ per cent of the depth and must be covered by
> four points. **(d)** Explain in two sentences why a demonstration run cannot report
> a Nusselt number, and name the two studies that would make one publishable.

Worked answers appear in
[`exercises/04-simulate-mantle-convection-solutions.md`](exercises/04-simulate-mantle-convection-solutions.md).

## Common pitfalls

1. **The buoyancy sign.** With the wrong sign every perturbation decays at every
   Rayleigh number; the linear-growth measurement of Section 5.4 is the test.
2. **Fitting an exponential through its transient.** The demonstration measured
   $6.9$ instead of $14.0$ until the decaying mode was excluded.
3. **Quoting a Nusselt number from an unconverged grid.** Refining $64\times32$ to
   $96\times48$ moves the answer by the size of the effect.
4. **Using the free-slip threshold for a no-slip code.** $\mathrm{Ra}_c$ is not
   $27\pi^{4}/4$ when the boundaries are rigid.
5. **A box too narrow for the critical wavelength.** It cannot convect, and no
   refinement helps.
6. **Forgetting the invariant.** $\max\lvert\theta\rvert \le 1$ is free to monitor
   and is the first sign of an under-resolved run.

## Related modules

- [19-08 Geophysical Simulation Case Studies](README.md).
- [19-07 Verification, Validation and Numerical Uncertainty](../07-verification-validation-uncertainty/README.md).
- [13-geodynamics-tectonics](../../13-geodynamics-tectonics/README.md).
- [19-02 Finite-Difference Methods](../02-finite-difference-methods/README.md) and
  [19-03 Finite Element and Finite Volume Methods](../03-finite-element-and-volume/README.md).

## Self-assessment checklist

- [ ] I can derive $\mathrm{Ra}_c = 27\pi^{4}/4$ and $k_c = \pi/\sqrt{2}$.
- [ ] I can verify a conduction solver against an exact profile.
- [ ] I can compute a discrete critical Rayleigh number and its convergence order.
- [ ] I can compute a linear growth rate and test a time integrator with it.
- [ ] I can compute the unstable wavenumber band at a stated $\mathrm{Ra}$.
- [ ] I can state what a defensible Nusselt number requires.
