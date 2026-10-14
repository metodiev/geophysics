---
id: 13-05-01
title: "Finite Element and Finite Volume Methods in Geodynamics"
level: research
prereqs: ["13-01-01", "01-09-08", "19-03-01", "19-03-02"]
tags: [geodynamics, tectonophysics, numerical-modelling, finite-element, finite-volume, discretisation]
---

# Finite Element and Finite Volume Methods in Geodynamics

> **All models and data in this module are SYNTHETIC.** The convergence tests,
> elements and fluxes below are computed from problems chosen for this lesson,
> not from measured rocks. Every number quoted is printed by
> [`code/finite_element_geodynamics_demo.py`](code/finite_element_geodynamics_demo.py),
> which you can run.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the weak form of a boundary-value problem and show that the
   Galerkin discretisation of the 1-D Poisson problem is nodally exact when the
   load is integrated exactly.
2. **Measure** the order of accuracy of a discretisation by grid refinement and
   **state** what a measured order does and does not prove.
3. **Assemble** the discrete divergence matrix $B$ for a velocity–pressure pair
   and **compute** the inf-sup constant $\beta_h$ from the generalised
   eigenvalue problem, rather than quoting that one element is unstable.
4. **Distinguish** a stable element pair (Q2-P1) from an unstable one (Q1-Q1) by
   the behaviour of $\beta_h$ with mesh refinement, and **explain** why a
   pressure-stabilisation term changes it.
5. **Derive** the first-order upwind numerical diffusivity $D_{\text{num}} =
   |u|h/2$ and **verify** it to machine precision as an operator identity.
6. **Predict** the cell-Péclet threshold $Pe_h = 2$ at which central
   differencing loses monotonicity, and **measure** it.
7. **Explain** why the flux form conserves a tracer to round-off while the
   advective form does not.

## Prerequisites

- [13-01-01 Momentum, Mass and Energy Balances](../01-geodynamic-principles/01-momentum-mass-energy.md) —
  the balance laws these discretisations approximate.
- [01-09-08 Weak Solutions and Variational Formulation](../../01-mathematics/09-partial-differential-equations/08-weak-solutions.md) —
  the weak form and integration by parts.
- [19-03-01 The Finite Element Weak Form](../../19-numerical-modeling-hpc/03-finite-element-and-volume/01-fem-weak-form.md) —
  the general theory this lesson applies.
- [19-03-04 Finite Volume Methods](../../19-numerical-modeling-hpc/03-finite-element-and-volume/04-finite-volume.md) —
  the flux-conservative view.

## 1. Why the discretisation is part of the tectonics

A geodynamic model reports velocities, stresses, temperatures and uplift rates.
Every one of those is produced by a discrete approximation to a continuum
problem, and the approximation has a *character*: some schemes conserve mass and
others do not, some lose monotonicity above a threshold, and some element pairs
admit pressure modes that the equations do not contain. Those properties are not
implementation details. They determine whether a reported number is the answer to
the question that was asked.

This lesson is about the three discretisation facts that matter most in solid-
Earth dynamics:

- **Finite elements** for the Stokes problem, where the question is which
  velocity–pressure pair can represent an incompressible flow at all;
- **finite volumes** for the energy equation, where the question is whether heat
  and tracers are conserved and whether the advection scheme overshoots;
- **the gap between a formal order of accuracy and an observed one**, which is
  where most published benchmark disagreements actually live.

Nothing here is specific to the Earth: the tests are analytic problems chosen so
that the exact answer is known. That is the point. A scheme that cannot reproduce
$\sin(\pi x)$ or an exponential boundary layer will not reproduce a mantle.

## 2. The weak form, and what Galerkin does with it

Take the Poisson problem on $(0,1)$,

$$-u''(x) = f(x), \qquad u(0) = u(1) = 0 .$$

Multiply by a test function $v$ that vanishes at the ends, integrate over the
domain and integrate by parts once:

$$\int_0^1 u'(x)v'(x)\,\mathrm{d}x = \int_0^1 f(x)v(x)\,\mathrm{d}x
\qquad \text{for all admissible } v .$$

The second derivative has been moved onto the test function, so the trial space
need only have square-integrable first derivatives. For piecewise-linear ("P1",
"hat") basis functions $\varphi_i$ this gives the linear system with the familiar
element stiffness $k_e = \frac{1}{h}\begin{pmatrix}1&-1\\-1&1\end{pmatrix}$.

**The weak form does not ask for more smoothness than the physics has.** That is
its whole value in geodynamics: viscosity may jump across a lithospheric
boundary, and the weak form integrates the jump instead of differentiating
through it.

## 3. Derivation: the 1-D P1 solution is nodally exact

Let $u_h$ be the P1 Galerkin solution and let $e_i = u_h(x_i) - u(x_i)$ be its
error at node $i$. The discrete equations at an interior node $i$ are

$$\frac{-u_h(x_{i-1}) + 2u_h(x_i) - u_h(x_{i+1})}{h} = \int
f(x)\varphi_i(x)\,\mathrm{d}x .$$

Subtract the same identity written for the exact solution. Because the exact
solution satisfies $\int u'v' = \int fv$ for every admissible $v$, the difference
$g = u_h - u$ satisfies

$$g(x_{i-1}) - 2g(x_i) + g(x_{i+1}) = 0$$

for every interior node, with $g(0) = g(1) = 0$: a discrete Laplace equation
whose solution is zero. The nodal values are therefore exact *provided the load
integral is evaluated exactly*. The $L^2$ error that remains is the
interpolation error of the exact solution between the nodes, which is
$O(h^2)$.

This is a rare exact result, and it is worth knowing because it isolates the
error source: with an exact load the visible error is interpolation, not the
scheme. Quadrature of the load is a separate approximation with its own error.

## 4. Worked example: measuring an order of accuracy

The demonstration solves $-u'' = f$ with the manufactured solution
$u = \sin(\pi x)$, so $f = \pi^2\sin(\pi x)$, on uniform meshes. Measured errors:

| $n$ elements | $h$ | $L^2$ error | observed order | $H^1$ error | observed order |
|---|---|---|---|---|---|
| 8 | 0.125 | $1.360\times10^{-2}$ | — | $1.430\times10^{-2}$ | — |
| 16 | 0.0625 | $3.406\times10^{-3}$ | 1.998 | $3.570\times10^{-3}$ | 2.002 |
| 32 | 0.03125 | $8.518\times10^{-4}$ | 1.999 | $8.922\times10^{-4}$ | 2.001 |
| 64 | 0.015625 | $2.130\times10^{-4}$ | 2.000 | $2.230\times10^{-4}$ | 2.000 |
| 128 | 0.0078125 | $5.324\times10^{-5}$ | 2.000 | $5.576\times10^{-5}$ | 2.000 |

The measured maximum nodal error at $n = 64$ is $6.049\times10^{-9}$ — five
orders of magnitude below the $L^2$ error, which is the nodal exactness of
Section 3 showing up as a number, limited by the Simpson quadrature of the load.

Replacing the exact load integral by nodal (mass-lumped) quadrature changes the
picture in an instructive way:

| $n$ | $L^2$ error (lumped) | order | max nodal error |
|---|---|---|---|
| 8 | $4.605\times10^{-3}$ | — | $1.295\times10^{-2}$ |
| 16 | $1.140\times10^{-3}$ | 2.015 | $3.219\times10^{-3}$ |
| 32 | $2.842\times10^{-4}$ | 2.004 | $8.036\times10^{-4}$ |
| 64 | $7.101\times10^{-5}$ | 2.001 | $2.008\times10^{-4}$ |
| 128 | $1.775\times10^{-5}$ | 2.000 | $5.020\times10^{-5}$ |

The order is unchanged, and at the coarsest mesh the lumped $L^2$ error is
*smaller* than the exact one. Two honest conclusions follow. First, mass lumping
costs accuracy but not order in this problem; a numerical experiment that only
quotes an order cannot see the constant. Second, the coincidence at $n=8$ is
exactly the kind of single-mesh agreement that a benchmark comparison must not
be built on — which is the subject of
[13-05-03](03-benchmarking-geodynamics.md).

## 5. The inf-sup condition, measured rather than asserted

The Stokes problem couples velocity and pressure through incompressibility. In
weak form it asks for $(\boldsymbol{u},p)$ with

$$a(\boldsymbol{u},\boldsymbol{v}) + b(\boldsymbol{v},p) = (\boldsymbol{f},\boldsymbol{v}),
\qquad b(\boldsymbol{u},q) = 0$$

for all admissible $(\boldsymbol{v},q)$, with
$b(\boldsymbol{v},q) = -\int q\,\nabla\!\cdot\!\boldsymbol{v}$.
Solvability of the *discrete* problem requires the inf-sup (Ladyzhenskaya–Babuška–Brezzi)
condition

$$\beta_h = \inf_{q_h \ne 0}\ \sup_{\boldsymbol{v}_h \ne 0}
\frac{b(\boldsymbol{v}_h,q_h)}{\|\boldsymbol{v}_h\|_1\,\|q_h\|_0} \;\ge\; \beta_0 > 0 ,$$

and the constant must be bounded *away from zero uniformly in $h$*, not merely
positive on one mesh. The discrete test is a generalised eigenvalue problem:
with $B$ the matrix of $b(\cdot,\cdot)$, $M_v$ the velocity $H^1$ mass matrix and
$M_p$ the pressure $L^2$ mass matrix,

$$\beta_h^2 = \lambda_{\min}^{\text{positive}}\bigl(B M_v^{-1} B^{\mathsf{T}},\;
M_p\bigr).$$

The constant pressure mode always gives $\lambda = 0$; any further near-zero
eigenvalue is a *spurious* mode. The demonstration assembles $B$, $M_v$ and $M_p$
element by element on a structured quadrilateral mesh and measures:

| $n$ (elements per side) | Q1-Q1 $\beta_h$ | Q1-Q1 near-zero modes | Q2-P1 $\beta_h$ | Q2-P1 near-zero modes |
|---|---|---|---|---|
| 4 | $1.912\times10^{-1}$ | 8 | $4.723\times10^{-1}$ | 1 |
| 6 | $1.425\times10^{-1}$ | 8 | $4.649\times10^{-1}$ | 1 |
| 8 | $1.100\times10^{-1}$ | 8 | $4.612\times10^{-1}$ | 1 |
| 12 | $7.462\times10^{-2}$ | 8 | $4.569\times10^{-1}$ | 1 |

Three measured facts:

- Equal-order Q1-Q1 has **eight** near-zero pressure modes on every mesh, not
  four, not "some": the discrete problem is rank-deficient by more than the
  constant mode, and the extra modes are the checkerboard patterns.
- $\beta_h$ decays like $h^{0.859}$ for Q1-Q1 (fitted by the demonstration over
  the four meshes) — it is not bounded away from zero, so the pair fails the
  condition *in the limit*, even on meshes where it happens to give a plausible
  answer.
- Taylor–Hood Q2-P1 has exactly one near-zero mode (the constant) and
  $\beta_h$ is constant to three digits across a factor of three in $h$.

Adding the pressure-Laplacian term $\varepsilon h^2 \int \nabla p\cdot\nabla q$
with $\varepsilon = 1$ to the pressure operator removes the spurious modes and
the stabilised $\beta_h$ becomes (measured)

| $n$ | $\beta_h$ (stabilised) | near-zero modes |
|---|---|---|
| 4 | $1.004$ | 1 |
| 8 | $7.159\times10^{-1}$ | 1 |
| 12 | $6.355\times10^{-1}$ | 1 |

The stabilisation is a *modelling choice*, not a neutral repair: it penalises
pressure gradients and therefore changes the pressure solution. That trade — a
solvable discrete problem in exchange for a modified one — is stated in the
lesson it belongs to, [13-05-02](02-stokes-flow-solvers.md).

The demonstration also verifies the assembly independently: for the constant
pressure, $\|M_v^{-1}B^{\mathsf{T}}\mathbf{1}\|_\infty = 1.678\times10^{-17}$
(the mode is annihilated to round-off), while for a random pressure it is
$1.491\times10^{-1}$ (it is not). An assembly bug that mixed up $M_v$ and $M_p$
would show up here.

## 6. Finite volumes: upwinding, monotonicity and numerical diffusion

The cell-centred finite-volume scheme for steady advection–diffusion writes the
flux at each face as $F = uT_{\text{face}} - D\,\partial_x T$, and the
arithmetic mean for $T_{\text{face}}$ is the central scheme while the upstream
cell value is the upwind scheme. Because the two differ only in the face
diffusion, the upwind scheme is *exactly* the central scheme with

$$D_{\text{eff}} = D + \frac{|u|h}{2}.$$

The demonstration verifies this as an operator identity on a periodic domain
(the amplitudes of the matrix entries agree to $0.000\times10^{0}$ and at worst
$2.274\times10^{-13}$, i.e. round-off) and then measures the consequences on the
same smooth solution:

| $n$ | central error | order | upwind error | order |
|---|---|---|---|---|
| 5 | $3.035\times10^{-1}$ | — | $4.902\times10^{-1}$ | — |
| 10 | $6.558\times10^{-2}$ | 2.210 | $2.693\times10^{-1}$ | 0.864 |
| 20 | $1.606\times10^{-2}$ | 2.030 | $1.402\times10^{-1}$ | 0.941 |
| 40 | $3.972\times10^{-3}$ | 2.015 | $7.255\times10^{-2}$ | 0.951 |
| 80 | $9.930\times10^{-4}$ | 2.000 | $3.688\times10^{-2}$ | 0.976 |

Central differencing is second order; upwind is first order, and the measured
exponent converges to 1 from below. The numerical diffusion is therefore
*visible in the order*, and any reported diffusivity or thermal structure that
comes from a first-order upwind energy equation carries an $O(h)$ bias.

On the Dirichlet outflow problem — where the exact solution is an exponential
boundary layer — the same two schemes behave differently again:

| $Pe$ | $Pe_h$ | central $L^\infty$ error | non-monotone amplitude | upwind $L^\infty$ error |
|---|---|---|---|---|
| 1 | 0.03 | $2.433\times10^{-2}$ | $0$ | $1.486\times10^{-3}$ |
| 5 | 0.12 | $1.174\times10^{-1}$ | $0$ | $2.062\times10^{-2}$ |
| 20 | 0.50 | $3.935\times10^{-1}$ | $0$ | $7.657\times10^{-2}$ |
| 100 | 2.50 | $9.179\times10^{-1}$ | $1.111\times10^{-1}$ | $2.036\times10^{-1}$ |

Two things to notice. Upwind's error is *smaller* here, because the solution has
a boundary layer that central differencing mishandles when the layer is
unresolved; this is the well-known reversal of the smooth-solution verdict, and
it is the reason the two cases are presented separately. And central differencing
loses monotonicity exactly when $Pe_h > 2$: bisecting on the amplitude of the
non-monotone excursion, the demonstration measures a **threshold cell Péclet
number of 2.000**, which is the classical value.

A final warning from the same tables: at $Pe = 20$ the measured convergence rate
of *both* schemes over $n = 10\ldots160$ is about $0.9$, not 1 or 2. Formal
orders describe smooth solutions on fine meshes; a boundary layer at fixed
physical width does not refine with the mesh.

## 7. Conservation: two forms of the same equation

Advecting a passive tracer in a variable velocity field can be written in flux
form, $\partial_t T = -\partial_x(uT)$, or in advective form,
$\partial_t T = -u\,\partial_x T$. They are algebraically identical in the
continuum. Discretely they are not. Integrate both for $4000$ steps with
$U_{\max} = 0.25$ on a periodic grid and measure the total:

| form | total at the end | initial | relative drift |
|---|---|---|---|
| flux (upwind faces) | 0.125331413732 | 0.125331413732 | $0.000\times10^{0}$ |
| advective (upwind difference) | 0.153348923086 | 0.125331413732 | $2.235\times10^{-1}$ |

The flux form telescopes over periodic faces and conserves to round-off; the
advective form has no such identity when the velocity is not uniform and drifts
by 22% in $4000$ steps. For a chemical tracer, a radiogenic heat source or a
melt fraction, that is the difference between a result and an artefact.

## 8. Assumptions and regime of validity

1. **The exact-load result of Section 3 is 1-D and P1-specific.** In 2-D and for
   higher-order elements the nodal solution is not exact, and the error is the
   usual $O(h^p)$ with constants that depend on the solution's derivatives.
2. **The inf-sup measurement uses a structured quad mesh with fully Dirichlet
   velocity.** $\beta_h$ depends on the mesh topology and on the boundary
   conditions; the *trend* with $h$ is the portable statement, not the value.
3. **The $Pe_h = 2$ threshold is for the interior scheme on a uniform grid.**
   Graded meshes, variable coefficients and boundary layers move it. The
   threshold says when monotonicity fails, not when the answer becomes wrong.
4. **$D_{\text{eff}} = D + |u|h/2$ is an operator identity, not a physical
   diffusivity.** It quantifies the *first-order* upwind bias; higher-order
   schemes have their own, smaller, equivalent.
5. **Conservation statements require the flux form on a conforming mesh with
   consistent faces.** A flux form whose faces are interpolated from
   non-conservative reconstructions loses the property.
6. **All problems here have analytic solutions.** A scheme that passes these
   tests is verified, not validated: nothing in this lesson says the equations
   describe the Earth (see [13-05-03](03-benchmarking-geodynamics.md)).

## 9. Worked example: choosing a scheme for a mantle thermal solve

*Problem.* A convection model must advect heat with velocities up to
$|u| = 5\ \mathrm{cm\,yr^{-1}}$ on a mesh with $h = 20\ \mathrm{km}$, where the
thermal diffusivity is the model's own; the model reports $Nu$ to a target of 2%.

1. Convert the velocity: $5\ \mathrm{cm\,yr^{-1}} = 0.05\ \mathrm{m}/3.1557\times10^{7}\
\mathrm{s} = 1.58\times10^{-9}\ \mathrm{m\,s^{-1}}$.
2. Take a mantle-like diffusivity $\kappa = 1.0\times10^{-6}\ \mathrm{m^2\,s^{-1}}$
   (a chosen teaching value). The added upwind diffusivity is
   $|u|h/2 = 1.58\times10^{-9}\times2.0\times10^{4}/2 = 1.58\times10^{-5}\
   \mathrm{m^2\,s^{-1}}$.
3. That is $1.58\times10^{-5}/1.0\times10^{-6} = 15.8$ times the physical
   diffusivity: a first-order upwind energy equation would conduct heat 16 times
   too fast. The cell Péclet number is $|u|h/\kappa = 31.6 \gg 2$, so central
   differencing is also non-monotone at this resolution.
4. Conclusion: neither elementary scheme is usable at this resolution. The
   options are to refine until $|u|h/\kappa \lesssim 2$ (here $h \lesssim
   1.3\ \mathrm{km}$, a 15-fold refinement in each direction), or to use a
   higher-order scheme whose numerical diffusivity is $O(h^p)$ with $p \ge 2$.

This arithmetic is the reason mantle-convection codes use high-order or spectral
advection schemes, and why a "converged" convection model must demonstrate
$h$-independence of $Nu$ rather than assert it.

## Mastery checkpoint

Without notes:

1. Derive the weak form of $-u'' = f$ and state why the trial space needs only
   $H^1$.
2. Explain in three sentences why the 1-D P1 Galerkin solution is nodally exact,
   and state which approximation then limits the nodal accuracy.
3. Compute $\beta_h$ for a one-element Q1-Q1 mesh by hand if you can; if not,
   state precisely what the generalised eigenvalue problem is and what the
   near-zero modes mean.
4. Show that the upwind face flux equals the central face flux with
   $D_{\text{eff}} = D + |u|h/2$, and derive the cell-Péclet threshold $2$ from
   the requirement that the resulting matrix be an M-matrix.
5. For $|u| = 5\ \mathrm{cm/yr}$, $h = 20\ \mathrm{km}$, $\kappa = 10^{-6}\
   \mathrm{m^2/s}$, compute both $Pe_h$ and the numerical diffusivity ratio, and
   state your recommendation.
6. State one diagnostic that would reveal a non-conservative advection
   discretisation in a running model.

## Common pitfalls

1. **Quoting one order of accuracy.** An order is measured over a range and is
   only meaningful where the asymptotic regime holds; the boundary-layer table
   in Section 6 shows both schemes returning $\approx 0.9$.
2. **Treating "the matrix was invertible" as stability.** Q1-Q1 systems are
   frequently invertible on coarse meshes while failing the inf-sup condition in
   the limit; the measured $\beta_h \sim h^{0.859}$ is the evidence.
3. **Using an unstable element pair because it "looks fine".** Spurious pressure
   modes appear as checkerboard pressure that does not refine away.
4. **Confusing numerical and physical diffusion.** An upwind energy equation has
   a diffusivity $|u|h/2$ that appears nowhere in the physics; the demonstration
   measures it as an operator identity so that it can be subtracted or reduced.
5. **Writing the advective form and calling it conservative.** The measured 22%
   drift is the price.
6. **Comparing a code against another code that shares the discretisation.**
   Shared errors cancel; that is
   [13-05-03](03-benchmarking-geodynamics.md).

## Related modules

- [13-05-02 Solving the Stokes Equations for Mantle Flow](02-stokes-flow-solvers.md) —
  where these elements and solvers are used for convection.
- [13-05-03 Benchmarking Geodynamic Codes](03-benchmarking-geodynamics.md) —
  how to turn these measurements into a verification claim.
- [13-01-01 Momentum, Mass and Energy Balances](../01-geodynamic-principles/01-momentum-mass-energy.md) —
  the equations being discretised.
- [19-03 Finite Element and Finite Volume Methods](../../19-numerical-modeling-hpc/03-finite-element-and-volume/README.md) —
  the general treatment, of which this is the geodynamic application.
- [19-01 Numerical Foundations for Simulation](../../19-numerical-modeling-hpc/01-numerical-foundations/README.md) —
  consistency, stability and convergence in general.

Companion exercises:
[`exercises/01-finite-element-geodynamics-exercises.md`](exercises/01-finite-element-geodynamics-exercises.md),
with worked solutions in
[`exercises/01-finite-element-geodynamics-solutions.md`](exercises/01-finite-element-geodynamics-solutions.md).
Run the demonstration with

```bash
cd 13-geodynamics-tectonics/05-geodynamic-modelling/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python finite_element_geodynamics_demo.py
```
