---
id: 13-05-02
title: "Solving the Stokes Equations for Mantle Flow"
level: research
prereqs: ["13-05-01", "13-02-01", "13-02-02", "19-03-03"]
tags: [geodynamics, tectonophysics, stokes-flow, convection, rayleigh-number, iterative-solvers]
---

# Solving the Stokes Equations for Mantle Flow

> **All models and data in this module are SYNTHETIC.** The viscosity, Rayleigh
> number and Nusselt numbers below are computed from a chosen Boussinesq model,
> not measured from the mantle. Every number is printed by
> [`code/stokes_flow_solvers_demo.py`](code/stokes_flow_solvers_demo.py).

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the Rayleigh number by non-dimensionalising the Boussinesq Stokes
   system and **compute** it for a stated set of parameters.
2. **Derive** the stream-function/vorticity formulation of infinite-Prandtl
   convection and show that the linearised growth rate of a normal mode is
   $\sigma(k,l) = -(k^2+l^2\pi^2) + Ra\,k^2/(k^2+l^2\pi^2)^2$.
3. **Derive** the critical Rayleigh number $Ra_c = (k^2+l^2\pi^2)^3/k^2$, obtain
   $27\pi^4/4$ for an unbounded layer and $8\pi^4$ for a unit-aspect box, and
   **measure** the box value by linear extrapolation of a growth rate.
4. **Solve** the discrete Stokes problem with a fast Poisson solver and
   **verify** it to round-off.
5. **Measure** the Nusselt number as a function of Rayleigh number and
   **explain** why the fitted exponent is not the asymptotic $1/3$.
6. **Quantify** the resolution and advection-scheme error in a reported Nusselt
   number.
7. **Distinguish** a large viscosity *variation* from a sharp viscosity
   *contrast* by measuring the condition number and the conjugate-gradient
   iteration count for each.

## Prerequisites

- [13-05-01 Finite Element and Finite Volume Methods](01-finite-element-geodynamics.md) —
  the discretisations used here, and the inf-sup condition for Stokes elements.
- [13-02-01 Rayleigh-Bénard Convection Applied to the Mantle](../02-mantle-convection/01-rayleigh-benard-mantle.md) —
  the physical picture this lesson makes quantitative.
- [13-02-02 Numerical Modelling of Mantle Convection](../02-mantle-convection/02-convection-numerical.md) —
  the modelling context.
- [19-03-03 Finite Element Assembly](../../19-numerical-modeling-hpc/03-finite-element-and-volume/03-fem-assembly.md) —
  assembling the operators.

## 1. From forces to a number: the Rayleigh number

Mantle flow is slow enough that inertia is negligible: the momentum balance is
the Stokes equation,

$$-\nabla p + \nabla\!\cdot\!\bigl(2\eta\,\boldsymbol{\dot\varepsilon}\bigr)
+ \rho\,\boldsymbol{g} = \boldsymbol{0}, \qquad \nabla\!\cdot\!\boldsymbol{u} = 0 ,$$

coupled to energy transport and incompressibility. With the Boussinesq
approximation, $\rho = \rho_0[1 - \alpha(T-T_0)]$, and a layer of depth $d$ with
temperature contrast $\Delta T$, the buoyancy that drives flow is
$\rho_0 g \alpha \Delta T$.

Scaling lengths by $d$, time by $d^2/\kappa$, velocity by $\kappa/d$ and pressure
by $\eta\kappa/d^2$, the momentum equation becomes

$$-\nabla' p' + \nabla'\!\cdot\!\bigl(2\boldsymbol{\dot\varepsilon}'\bigr)
+ Ra\,T'\,\hat{\boldsymbol{z}} = \boldsymbol{0} , \qquad
Ra = \frac{\rho_0 g \alpha \Delta T d^3}{\kappa\eta} ,$$

so **one dimensionless number** controls the pattern. The demonstration computes
it for a chosen parameter set:

| quantity | symbol | value |
|---|---|---|
| density | $\rho_0$ | 3300 kg/m³ (chosen) |
| thermal expansivity | $\alpha$ | $3.0\times10^{-5}$ K$^{-1}$ (chosen) |
| temperature contrast | $\Delta T$ | 3000 K (chosen) |
| layer depth | $d$ | $2.90\times10^{6}$ m (chosen) |
| thermal diffusivity | $\kappa$ | $1.0\times10^{-6}$ m²/s (chosen) |
| viscosity | $\eta$ | $1.0\times10^{21}$ Pa s (chosen) |
| **Rayleigh number** | $Ra$ | $\mathbf{7.106\times10^{7}}$ |

and the associated scales: viscous diffusion time $d^2/\kappa = 8.410\times10^{18}$ s,
convective velocity scale $\kappa/d = 3.448\times10^{-13}$ m/s, buoyancy stress
$\rho_0 g\alpha\Delta T d = 8.449\times10^{9}$ Pa, and a Stokes velocity from that
stress $d^2\rho_0 g\alpha\Delta T/\eta = 2.450\times10^{-5}$ m/s. Note the two
velocity scales differ by eight orders of magnitude: the first is the diffusive
velocity, the second is what buoyancy can actually drive. Which one is "the"
velocity scale is a choice that changes what $Ra$ means, and papers that quote
$Ra$ without its scaling are unreadable.

## 2. Stream function and vorticity

For incompressible flow in two dimensions a stream function $\psi$ exists with

$$u = \frac{\partial\psi}{\partial y}, \qquad w = -\frac{\partial\psi}{\partial x},
\qquad \omega = \frac{\partial w}{\partial x} - \frac{\partial u}{\partial y}
= -\nabla^2\psi .$$

Taking the curl of the Stokes equation eliminates the pressure and leaves, for
infinite Prandtl number and constant viscosity,

$$\nabla^2\omega = -Ra\,\frac{\partial T}{\partial x} .$$

The energy equation for the perturbation $\theta$ about the conductive profile
$T_{\text{cond}} = 1 - y$ is

$$\frac{\partial\theta}{\partial t} = \nabla^2\theta + w
- \boldsymbol{u}\cdot\nabla\theta ,$$

where the term $+w$ is the advection of the conductive profile and is exact; only
the perturbation's self-advection is discretised. Free-slip boundaries give
$\psi = \omega = 0$ on the boundary, which is what makes the sine transform
usable, and adiabatic side walls require $\partial\theta/\partial x = 0$ there.

## 3. Derivation: the linear growth rate and the critical Rayleigh number

Linearise about the conductive state and take a normal mode
$\theta \propto \cos(kx)\sin(l\pi y)$, $l = 1, 2, \ldots$ The choice of cosine in
$x$ is forced by the adiabatic side walls (a sine would not satisfy
$\partial\theta/\partial x = 0$), and the sine in $y$ by the fixed-temperature
boundaries. Then

$$\nabla^2\theta = -(k^2 + l^2\pi^2)\theta, \qquad
\frac{\partial\theta}{\partial x} = -k\sin(kx)\sin(l\pi y),$$

and $\nabla^4\psi = Ra\,\partial\theta/\partial x$ gives
$\psi = -Ra\,k\,\theta/(k^2+l^2\pi^2)^2$, hence
$w = -\partial\psi/\partial x = Ra\,k^2\theta/(k^2+l^2\pi^2)^2$. Substituting
into the energy equation:

$$\boxed{\ \sigma(k,l) = -(k^2+l^2\pi^2) + \frac{Ra\,k^2}{(k^2+l^2\pi^2)^2}\ }$$

The conduction state is unstable when $\sigma > 0$, i.e.

$$Ra > Ra_c(k,l) = \frac{(k^2+l^2\pi^2)^3}{k^2} .$$

Minimising over $k$ for $l = 1$ gives $k_c = \pi/\sqrt{2}$ and

$$Ra_c = \frac{27\pi^4}{4} = 657.51$$

for a horizontally unbounded layer with free-slip boundaries. **In a box of
aspect ratio one the admissible wavenumbers are $k = n\pi$, so the first mode to
go unstable has $k = \pi$ and**

$$Ra_c^{\text{box}} = \frac{(2\pi^2)^3}{\pi^2} = 8\pi^4 = 779.27 .$$

That the box value exceeds the layer value is not a detail: it is the statement
that confining a convective layer to one wavelength's width stabilises it.

## 4. Verification: three measured checks

**(a) The Poisson solver.** The operator $\nabla^2$ with zero Dirichlet data is
diagonal in the two-dimensional sine basis, so one orthonormal DST-I pair solves
it exactly. The demonstration verifies this by a round trip:
$\max|\text{solve}(\nabla^2 u) - u| = 5.662\times10^{-15}$ — round-off. Against
the continuum solution $\sin(\pi x)\sin(\pi y)$ of
$\nabla^2u = -2\pi^2u$ it errs by $3.423\times10^{-4}$, which is the $O(h^2)$
truncation error of the discrete operator with $h^2 = 4.165\times10^{-4}$. The
measured cost is 0.047 ms per $48\times48$ solve, which is why this route is
preferred to a sparse direct solve for constant-coefficient problems.

**(b) The growth rates.** Sampling the mode amplitude in the window where it lies
between $10^{-12}$ and $10^{-6}$ (well below the amplitude of order $0.1$ at
which non-linear saturation sets in) and fitting $\ln A$ against $t$:

| mode | $\sigma$ analytic | $\sigma$ measured | relative difference |
|---|---|---|---|
| $k=\pi,\ l=1$ | 30.9214 | 30.3061 | 1.99% |
| $k=2\pi,\ l=1$ | $-16.9252$ | $-19.0021$ | 12.27% |
| $k=\pi,\ l=2$ | $-41.2423$ | $-41.7546$ | 1.24% |

The three modes include one growing and two decaying, so the test is not
sensitive to the sign convention, and the largest discrepancy is 12% — the size
of the discretisation error in the effective wavenumbers.

**(c) The critical Rayleigh number.** Since $\sigma$ is *linear* in $Ra$ for a
fixed mode, the analytic relation can be inverted by a straight-line fit:

| $Ra$ | 900 | 1200 | 1600 | 2000 |
|---|---|---|---|---|
| $\sigma$ measured | 2.5350 | 10.1180 | 20.2180 | 30.3061 |

The fitted slope is $2.5246\times10^{-2}$ per unit $Ra$ against the analytic
$1/(4\pi^2) = 2.5330\times10^{-2}$, and extrapolating to $\sigma = 0$ gives

$$Ra_c^{\text{measured}} = 799.39 \quad\text{against}\quad 8\pi^4 = 779.27
\quad (+2.58\%).$$

Refining the grid moves the measured value toward the analytic one (Section 7 of
the benchmarking lesson shows $813.65$ at $N=24$, $799.39$ at $N=40$ and $791.69$
at $N=64$). This is what verification looks like: a target that is known exactly,
a measured departure, and a demonstration that the departure vanishes with
refinement.

## 5. Non-linear convection: the Nusselt number

$Nu$ is the ratio of the actual heat flux to the conductive flux. The
demonstration evaluates it two ways — from the bottom temperature gradient and
from the volume average $1 + \langle wT\rangle$ — which must agree as
$h \to 0$:

| $Ra$ | $Nu$ (bottom flux) | $Nu$ (volume average) | $v_{\text{rms}}$ | steps to steady state |
|---|---|---|---|---|
| $1.0\times10^{3}$ | 1.4166 | 1.4089 | 4.5456 | 5200 |
| $3.0\times10^{3}$ | 3.1013 | 2.9913 | 17.3353 | 1800 |
| $1.0\times10^{4}$ | 4.9788 | 4.5125 | 41.3094 | 1600 |
| $3.0\times10^{4}$ | 7.4369 | 6.1120 | 84.0054 | 2400 |

Fitting $Nu = a\,Ra^{\beta}$:

- over $10^3 \le Ra \le 3\times10^4$: $Nu = 0.0588\,Ra^{0.4770}$;
- over $3\times10^3 \le Ra \le 3\times10^4$: $Nu = 0.1487\,Ra^{0.3801}$.

The exponent is falling with $Ra$ **and is not $1/3$ over either range**. That is
the correct result, not a defect: the boundary-layer argument that gives
$Nu \sim Ra^{1/3}$ is asymptotic, and near onset $Nu - 1$ is proportional to
$Ra - Ra_c$ instead. Reporting the exponent of a power-law fit without stating
the fitting range is therefore uninformative; the honest statement is the pair
(range, exponent) together with the resolution at which it was measured.

## 6. Worked example: how big is the discretisation error?

*Problem.* You report $Nu = 4.98$ for $Ra = 10^4$ from a $32\times32$ grid. How
much of that is the grid?

1. Run the same case at three resolutions (Section 4 of the demonstration):
   $5.0799$ at $N=24$, $4.9788$ at $N=32$, $4.9015$ at $N=48$.
2. Assume a smooth second-order error, $Nu(h) = Nu_0 + c\,h^2$, and eliminate
   $c$ between $N=24$ ($h = 0.0400$) and $N=48$ ($h = 0.0204$):
   $c = (5.0799-4.9015)/(0.0400^2-0.0204^2) = 150.7$, so
   $Nu_0 = 4.9015 - 150.7\times0.0204^2 = 4.8388$.
3. The $N=32$ value differs from the extrapolated one by
   $|4.9788-4.8388|/4.8388 = 2.89\%$.
4. Now add the advection-scheme error. The first-order upwind scheme at
   $N=32$ gives $Nu = 5.1891$, a 4.2% difference from central — the same size as
   the grid error. At this resolution the two errors cannot be separated, and
   neither can be shown to be negligible.

*Answer:* the uncertainty on the reported $Nu$ is several per cent, and both
contributions must be quoted. The Grid Convergence Index machinery for turning
step 2 into a formal uncertainty band is developed in
[13-05-03](03-benchmarking-geodynamics.md).

## 7. Why mantle-flow solvers are hard

The folklore is that a viscosity contrast of $10^{5}$ or more is what defeats a
Stokes solver. The demonstration tests the folklore by measuring, for
$-\nabla\!\cdot(\eta\nabla u) = 1$ on a unit square with $u = 0$ on the boundary,
the condition number of the dense operator at $N=16$ and the number of
unpreconditioned conjugate-gradient iterations at $N=32$:

| contrast | smooth $\eta$: cond | smooth: CG iterations | sharp step in $\eta$: cond | sharp: CG iterations |
|---|---|---|---|---|
| 1 | $1.165\times10^{2}$ | 66 | $1.165\times10^{2}$ | 66 |
| $10^{2}$ | $1.669\times10^{2}$ | 68 | $4.675\times10^{3}$ | 582 |
| $10^{4}$ | $1.678\times10^{2}$ | 68 | $4.631\times10^{5}$ | 1592 |
| $10^{6}$ | $1.678\times10^{2}$ | 68 | $4.631\times10^{7}$ | 2497 |

A six-order-of-magnitude viscosity *variation* that is smooth changes the
condition number by 44% and the iteration count by 3%; the same variation across
a *sharp interface* changes the condition number in proportion to the contrast
and multiplies the work by 38.

The reason is the lowest eigenmode: for a smooth coefficient it averages the
viscosity and the spectrum barely moves, while a stiff region bounded by a sharp
interface can translate almost rigidly, which is a near-null mode of the
operator. This is why real codes invest in multigrid or Schur-complement
preconditioners, and why the number to quote with a variable-viscosity result is
not the contrast but the *gradient* of the contrast on the discretisation scale.

## 8. Assumptions and regime of validity

1. **Infinite Prandtl number, Boussinesq, constant viscosity, free slip.** The
   stream-function formulation requires 2-D incompressible flow; three-
   dimensional or compressible convection needs a different solver.
2. **The linear stability result is for the linearised problem.** The measured
   growth rates are fitted in the small-amplitude window; a perturbation of
   order 0.1 no longer grows at the linear rate.
3. **The Nusselt number is a steady-state diagnostic.** The demonstration stops
   when $Nu$ changes by less than $10^{-4}$ between checks 200 steps apart; that
   stopping rule does not prove a steady state exists (Section 4 of
   [13-05-03](03-benchmarking-geodynamics.md) shows a scheme for which it does
   not).
4. **The extrapolated $Nu_0$ assumes a smooth $O(h^2)$ error.** A boundary layer
   at fixed width violates that assumption, and the Richardson estimate is then
   optimistic.
5. **The viscosity-contrast numbers are for a Poisson-like operator.** A Stokes
   operator and a temperature-dependent viscosity add couplings that change the
   counts, though the mechanism is the same.
6. **Nothing here is calibrated to the Earth.** The parameters are chosen to make
   $Ra$ interesting, not to be a mantle.

## Mastery checkpoint

Without notes:

1. Derive $Ra = \rho_0 g\alpha\Delta T d^3/(\kappa\eta)$ from the Stokes and energy
   equations, and state each scaling choice.
2. Derive $\sigma(k,l)$ and $Ra_c(k,l)$; then compute $Ra_c$ for $k = \pi$,
   $l = 1$ and for $k = \pi/\sqrt{2}$, and explain the difference in one
   sentence.
3. Estimate, without running anything, the growth rate at $Ra = 5000$ for the
   $(k=\pi, l=1)$ mode, and say whether the mode grows.
4. State two independent checks that would catch a sign error in the buoyancy
   coupling of a convection code.
5. Given $Nu = 4.98$ at $N=32$ and $4.90$ at $N=48$, estimate $Nu(h\to0)$ and the
   uncertainty, and name the assumption behind the estimate.
6. A colleague reports a very long run time and blames the viscosity contrast of
   $10^{6}$. What single diagnostic distinguishes the bad explanation from the
   good one?

## Common pitfalls

1. **Quoting $Ra$ without the scaling.** Different non-dimensionalisations
   absorb different powers of $d$, $\kappa$ and $\eta$.
2. **Reading a power law off a fit.** The measured exponent falls from 0.48 to
   0.38 as the fitting range moves; only the pair (range, exponent) is a result.
3. **Assuming the GCI-style extrapolation.** With unresolved boundary layers the
   observed order is not the formal order and the extrapolation is biased.
4. **Blaming the viscosity contrast in the abstract.** Smooth contrast was
   measured to be almost free; sharp contrast is what costs.
5. **Trusting a stopping rule.** "The diagnostic stopped changing" is a
   hypothesis, testable by watching the diagnostic over a long window.
6. **Forgetting that the Nusselt number is only one diagnostic.** Two grids that
   agree on $Nu$ can disagree by several per cent on the interior temperature
   field.

## Related modules

- [13-05-01 Finite Element and Finite Volume Methods](01-finite-element-geodynamics.md) —
  the discretisations and the inf-sup condition.
- [13-05-03 Benchmarking Geodynamic Codes](03-benchmarking-geodynamics.md) —
  the verification workflow built on these diagnostics.
- [13-02-01 Rayleigh-Bénard Convection Applied to the Mantle](../02-mantle-convection/01-rayleigh-benard-mantle.md) —
  the physical problem.
- [13-04-01 Crustal Deformation from GNSS and Strain Rates](../04-tectonophysics-deformation/01-crustal-deformation-gps.md) —
  the observations a model like this is meant to explain.
- [19-05 Integral Equation and Boundary Methods](../../19-numerical-modeling-hpc/05-integral-equation-and-boundary-methods/README.md) —
  the alternative solution strategy for constant-coefficient problems.

Companion exercises:
[`exercises/02-stokes-flow-solvers-exercises.md`](exercises/02-stokes-flow-solvers-exercises.md)
and
[`exercises/02-stokes-flow-solvers-solutions.md`](exercises/02-stokes-flow-solvers-solutions.md).
Run the demonstration with

```bash
cd 13-geodynamics-tectonics/05-geodynamic-modelling/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python stokes_flow_solvers_demo.py
```
