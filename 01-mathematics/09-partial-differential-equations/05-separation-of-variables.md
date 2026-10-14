---
id: 01-09-05
title: "Separation of Variables and Boundary Conditions"
level: advanced
prereqs: ["01-09-02", "01-09-03"]
estimated_minutes: 90
tags: [partial-differential-equations, separation-of-variables, sturm-liouville, boundary-conditions, eigenfunction-expansion]
---

# Separation of Variables and Boundary Conditions

## Learning objectives

By the end of this lesson you will be able to:

1. **Separate** a linear PDE into a pair of ODEs, identify the eigenvalue problem
   that the boundary conditions create, and say which of the two ODEs carries the
   eigenvalues.
2. **Solve** the 1-D heat-conduction problem in a slab with fixed end
   temperatures, computing the coefficients by projection, and check the answer
   against a numerical solution at second-order accuracy.
3. **Derive and use** the steady geothermal gradient in a layer with radiogenic
   production, including the sign and size of the curvature term, and state the
   condition under which steady state is admissible.
4. **Obtain** the normal modes of a bounded string, prove their orthogonality, and
   distinguish the *free* parameters (eigenvalues) from the *forced* ones
   (amplitudes of a particular initial condition).
5. **Handle non-homogeneous boundary conditions** by subtracting a steady state,
   and say when that trick fails.
6. **Recognise** the situations in which separation is impossible (irregular
   geometry, variable coefficients, non-separable domains) and therefore when a
   numerical method is the appropriate tool.

## Prerequisites

- [01-09-02 The Diffusion/Heat Equation and Diffusive Timescales](./02-heat-equation.md)
  — the equation being solved here, and the eigenfunctions (5) of that lesson.
- [01-09-03 The Wave Equation and Its Physical Content](./03-wave-equation.md) —
  the string modes, and the meaning of a normal mode.
- [01-05-xx Single-Variable Calculus](../05-single-variable-calculus/README.md) —
  linear ODEs with constant coefficients, and Fourier series.
- [01-07-xx Linear Algebra](../07-linear-algebra/README.md) — eigenvalues,
  eigenvector bases and orthogonality, used here in function space. (Planned.)

## 1. Intuition: turn one hard problem into infinitely many easy ones

Separation of variables is the single most productive technique for linear PDEs
with constant coefficients on simple domains. The idea is to look for solutions
that are products,

$$u(x,t) = X(x)\,T(t),$$

so that the PDE becomes a sum of terms each depending on one variable only. The
only way such a sum can vanish identically is if every term is constant — and
that constant is the **eigenvalue**. The PDE has then been converted into two
ordinary differential equations linked by a single number, and the boundary
conditions select the allowed values of that number.

The physical reading is the reason the method works so well in geophysics: many
systems respond to a disturbance as a sum of **standing patterns**, each of which
evolves in time independently. A cooling intrusion, a ringing bell, the Earth
after a great earthquake, a borehole temperature log — all are naturally described
as a sum of modes, each with its own decay rate or frequency. The method finds
those patterns. What it cannot do is find *non-separable* ones, and Section 7 is
about recognising that.

## 2. The method, in general form

### 2.1 Separation of a second-order linear equation

Consider

$$u_t = \kappa\,u_{xx}, \qquad 0 < x < L,\ t > 0 . \tag{1}$$

Substitute $u = X(x)T(t)$:

$$X T' = \kappa X'' T \qquad\Longrightarrow\qquad
\frac{T'}{\kappa T} = \frac{X''}{X} = -\lambda .$$

The left side depends only on $t$ and the right only on $x$, so both equal a
constant, which we have called $-\lambda$ (the minus sign makes $\lambda$
positive for the problems of interest). Two ODEs follow:

$$T' + \kappa\lambda T = 0 \qquad\text{(time)}, \qquad
X'' + \lambda X = 0 \qquad\text{(space)}. \tag{2}$$

The time equation is first order and trivial: $T(t) =
\mathrm{e}^{-\kappa\lambda t}$. **All the difficulty is in the space equation and
its boundary conditions**, which together form an **eigenvalue problem**.

### 2.2 The eigenvalue problem, from the boundary conditions

For (1) on a slab with both ends held at zero,

$$X(0) = 0, \qquad X(L) = 0 , \tag{3}$$

the solutions of $X'' + \lambda X = 0$ satisfying (3) are

$$X_n(x) = \sin\!\left(\frac{n\pi x}{L}\right), \qquad
\lambda_n = \left(\frac{n\pi}{L}\right)^2, \qquad n = 1,2,3,\dots \tag{4}$$

for $\lambda > 0$. (For $\lambda \le 0$ the only solution satisfying (3) is
$X \equiv 0$, so those values are not eigenvalues — this is worth checking once,
because it is where a "missing" solution usually hides.) Each eigenvalue carries
a decay rate $\kappa\lambda_n$, so the full solution is

$$u(x,t) = \sum_{n=1}^{\infty}b_n\sin\!\left(\frac{n\pi x}{L}\right)
\mathrm{e}^{-\kappa\lambda_n t} , \tag{5}$$

with the $b_n$ fixed by the initial condition $u(x,0) = f(x)$ through the
orthogonality relation

$$\int_0^L\sin\frac{n\pi x}{L}\sin\frac{m\pi x}{L}\,dx
= \frac{L}{2}\delta_{nm}
\qquad\Longrightarrow\qquad
b_n = \frac{2}{L}\int_0^L f(x)\sin\frac{n\pi x}{L}\,dx . \tag{6}$$

Equations (4)–(6) are the whole method: eigenvalues from the boundary
conditions, coefficients from projection onto the orthogonal eigenfunctions.

### 2.3 Why the eigenfunctions are orthogonal: Sturm–Liouville

The boundary-value problem $-(p\,X')' + qX = \lambda w X$ with suitable
boundary conditions is a **Sturm–Liouville problem**. Its eigenvalues are real
and can be ordered $\lambda_1 < \lambda_2 < \dots \to \infty$, its eigenfunctions
are orthogonal with respect to the weight $w$, and they form a complete basis for
the functions satisfying the boundary conditions. Completeness is the statement
that expansions like (5) converge; orthogonality is what makes the coefficients
computable one at a time by (6).

Two consequences used constantly in geophysics:

- **Higher modes always decay faster (or oscillate faster).** For the heat
  problem the rate is $\kappa\lambda_n \propto n^2$; for the wave problem the
  frequency is $\omega_n \propto n$. Either way the fine structure is in the high
  modes, and it is the first thing to be lost or mis-resolved.
- **The basis is fixed by the geometry and the boundary conditions, not by the
  data.** Change one boundary condition and every eigenfunction changes. This is
  the reason a modelling code that switches from a fixed to an insulated end must
  be re-verified, not merely re-run.

## 3. Worked example 1: heat conduction in a slab

Take (1) with $L = 1$, $\kappa = 1$, ends held at zero and a triangular initial
profile $f(x) = 2x$ for $x\le\tfrac12$, $2(1-x)$ for $x>\tfrac12$ — a localised
thermal pulse, which is the idealised version of a buried intrusion. From (6),
with the integral evaluated numerically by the midpoint rule on 4000 intervals:

```text
    b_1 = +0.810569, b_2 = +0.000000, b_3 = -0.090063, b_4 = -0.000000,
    b_5 = +0.032423, b_6 = -0.000000
```

Three facts are visible in that line. The even coefficients vanish, because the
pluck is symmetric about $x = \tfrac12$: the eigenfunctions $\sin(2\pi x)$,
$\sin(4\pi x),\dots$ are antisymmetric there and project to zero. The
coefficients fall off like $1/n^2$, which is the Fourier signature of a
continuous but not smooth function (the triangle has a corner). And the sign
alternates for odd $n$, so the high modes correct the peak rather than merely
rounding it off.

The solution (5) then competes with a finite-difference solve, and the
verification is exactly the second-order convergence the scheme should show:

```text
     N         dx    max |FD - exact|   order
    25   3.85e-02           6.715e-04        
    50   1.96e-02           1.763e-04    1.93
   100   9.90e-03           4.520e-05    1.96
   200   4.98e-03           1.143e-05    1.98
```

Note which is being verified: the *scheme* is checked against the series, not the
other way round. A truncated series is only acceptable as a reference if the
truncation error is shown to be below the discretisation error — Section 4 does
that.

## 4. Spectral convergence, and how many terms are enough

Truncating (5) at $N$ terms and comparing with a 400-term reference at
$t = 0.05$:

```text
      N    max truncation error
      1               1.061e-03
      2               1.061e-03
      3               1.422e-07
      5               5.214e-13
     10               0.000e+00
     15               0.000e+00
```

The error collapses long before the coefficients stop mattering, because each
term carries the factor $\exp(-\kappa\lambda_n t)$: at $t = 0.05$ the $n$-th mode
is attenuated by $\exp(-n^2\pi^2\times0.05)$, so mode 10 is suppressed by
$\mathrm{e}^{-49}$ and mode 15 by $\mathrm{e}^{-111}$. **This is the practical
reason eigenfunction expansions are the method of choice for diffusive problems
at moderate time:** a handful of terms is exact to machine precision, whereas a
finite-difference scheme must resolve the *initial* profile on a fine grid even
though the fine structure is destroyed almost immediately.

At short times the balance reverses: for $t \to 0$ many terms are needed to
represent $f$, and the series converges slowly. Good practice is to use the
series for $t$ larger than a fraction of the fastest resolved timescale and a
quadrature-based or numerical approach for very short times.

### 4.1 Verifying the eigenvalue

The decay rate of each mode is a measurable prediction. Initialising
$u = \sin(3\pi x)$ and tracking the amplitude at the midpoint:

```text
    measured decay rate of sin(3 pi x)      = 88.832165 per unit time
    eigenvalue of the PDE, kappa (3 pi)^2   = 88.826440
    discrete eigenvalue 4 kappa sin^2(3 pi dx/2)/dx^2 = 88.822351
    relative difference from the discrete value = 1.10e-04
```

The measurement is closer to the *discrete* eigenvalue than to the continuous
one, and that is the expected outcome: the finite-difference operator has its own
spectrum, which differs from the PDE spectrum by $O(\Delta x^2)$. The code
computes both and reports the comparison, so the reader can see that the small
discrepancy is discretisation and not physics — a distinction that matters when a
measured decay rate is being interpreted as a material property.

## 5. Worked example 2: steady conduction in a layered Earth

### 5.1 The equation and its solution

For steady heat conduction with uniform radiogenic production $A$ per unit volume
and $z$ measured downward,

$$\frac{d}{dz}\left(k\frac{dT}{dz}\right) + A = 0
\qquad\Longrightarrow\qquad
k\,T'' = -A . \tag{7}$$

Integrating twice with the surface heat flow $q_0$ (upward, with $T$ increasing
downward so that $q = k\,dT/dz$ at the surface):

$$T(z) = T_s + \frac{q_0}{k}z - \frac{A}{2k}z^2 . \tag{8}$$

The **sign of the quadratic term is negative**, and the physical reason is worth
stating: production adds heat along the path, so the upward heat flow must
*decrease* with depth, $q(z) = q_0 - Az$; a decreasing gradient means a concave
geotherm. Getting this sign wrong flips the curvature and changes the
temperature at depth by twice the curvature term.

**Verification by substitution.** With $T$ a quadratic, a central second
difference is exact, so $k T'' + A$ should vanish to round-off. The demonstration
reports $|kT'' + A| = 2.2\times10^{-13}$ at $z = 30$ km. The check is cheap and
worth automating, because it catches the sign error immediately.

### 5.2 Numbers, with every input stated

Take an illustrative set: $k = 2.5\ \mathrm{W\,m^{-1}K^{-1}}$,
$q_0 = 0.065\ \mathrm{W\,m^{-2}}$, $A = 10^{-6}\ \mathrm{W\,m^{-3}}$
(1 µW m$^{-3}$) and $T_s = 10\ ^\circ$C. Then the surface gradient is

$$\frac{q_0}{k} = \frac{0.065}{2.5} = 0.026\ \mathrm{K\,m^{-1}}
= 26\ \mathrm{K\,km^{-1}} ,$$

and the curvature term is $-Az^2/(2k)$:

| Depth (km) | $T$ with $A = 0$ (°C) | $T$ with $A$ (°C) | Curvature (°C) |
|---|---|---|---|
| 5 | 140.0 | 135.0 | $-5.0$ |
| 10 | 270.0 | 250.0 | $-20.0$ |
| 20 | 530.0 | 450.0 | $-80.0$ |
| 30 | 790.0 | 610.0 | $-180.0$ |
| 40 | 1050.0 | 730.0 | $-320.0$ |

Three lessons from the table:

- A quoted "geothermal gradient of 26 K/km" says nothing at depth unless the
  depth range and the production model are stated. At 30 km the difference
  between the linear and quadratic models is 180 °C, which is larger than most
  thermal interpretations' error bars.
- The parameters are illustrative and real values vary substantially: $k$ varies
  with lithology and porosity, $q_0$ varies by a factor of two between
  provinces, and $A$ varies by an order of magnitude between granite, basalt and
  sediment. Any specific number must come from the site.
- Real geotherms are curved for a second reason as well: $k$ changes with depth
  and temperature, so (7) must be solved with $k(z)$ and continuity of $T$ and
  $k\,dT/dz$ across layers. That is a layered *ordinary* differential equation,
  and it is solved by integrating the flux rather than by separation.

### 5.3 When is steady state admissible?

Equation (8) sets all time derivatives to zero, which asserts
$t \gg L^2/\kappa$. With $\kappa = 10^{-6}\ \mathrm{m^2\,s^{-1}}$ and
$L = 30$ km,

$$\tau = \frac{L^2}{\kappa} = \frac{9\times10^{8}}{10^{-6}}
= 9.0\times10^{14}\ \mathrm{s} = 28.5\ \mathrm{Myr} .$$

Where the lithosphere is younger than that — young oceanic crust, a recently
extended basin, a volcanic province — a steady geotherm is an assumption to be
tested, and the time-dependent equation must be solved. The demonstration prints
this check alongside the table so that the assumption is never silently made.

## 6. Worked example 3: vibration of a bounded string

For $u_{tt} = c^2u_{xx}$ on $0<x<L$ with $u(0,t) = u(L,t) = 0$, separation gives
the same space problem as before, but the time equation is oscillatory:

$$X'' + \lambda X = 0, \quad T'' + c^2\lambda T = 0
\qquad\Longrightarrow\qquad
u_n = \sin\!\left(\frac{n\pi x}{L}\right)\cos(\omega_n t), \quad
\omega_n = \frac{n\pi c}{L} . \tag{9}$$

The mode frequencies are the eigenvalues in disguise, and they are properties of
the *problem*: the equation, the length and the boundary conditions. The
amplitudes are properties of the *initial condition*. This division is the reason
a seismologist can use the Earth's normal-mode frequencies as a model constraint
while treating the excitation of a particular event as a separate problem. The
demonstration verifies each mode by substitution (residuals $10^{-10}$ at
$h = 10^{-3}$, pure cancellation error, with a refinement study returning order
2.00), and checks the orthogonality integral:

```text
     n   m      numerical    exact (L/2) delta_nm
     1   1    0.500000000             0.500000000
     1   2   -0.000000000             0.000000000
     3   3    0.500000000             0.500000000
     4   7   -0.000000000             0.000000000
```

Note the second-order requirement in the substitution check: with the space step
equal to the time step and $\omega = \pi c/L$, the two second differences sample
identical points and the residual collapses to round-off for *any* step size.
That is the same stencil-on-the-characteristic alignment that makes the leapfrog
scheme exact at Courant number 1, seen in [01-09-03](./03-wave-equation.md) §5.3.

## 7. Boundary conditions: the classification that drives everything

| Type | Statement | Physical example (heat) | Effect on the eigenvalues |
|---|---|---|---|
| Dirichlet | $u = f$ | fixed surface temperature | discrete set, $\lambda_n = (n\pi/L)^2$ |
| Neumann | $\partial u/\partial n = g$ | specified heat flux, insulated end ($g=0$) | discrete set shifted; the constant mode survives |
| Robin | $\partial u/\partial n + hu = g$ | convective loss to air | transcendental equation for $\lambda_n$; larger $h$ approaches Dirichlet |
| Mixed | different type at each end | fixed base, convecting top | still a Sturm–Liouville problem |
| Radiation (Sommerfeld) | outgoing wave, no incoming | absorbing truncation boundary | changes the *spectrum* from discrete to continuous |
| Free surface / traction-free | zero traction | the Earth's surface | couples P and S; the basis is no longer sines |

Three practical observations:

- **The type of boundary condition is physics, not a numerical convenience.** A
  fixed-temperature boundary removes an eigenvalue that an insulated one keeps:
  compare the slowest decay rate $\pi^2$ for Dirichlet–Dirichlet against
  $\pi^2/4$ for Neumann–Dirichlet in
  [01-09-07](./07-boundary-value-problems.md). A factor of four in the relaxation
  time follows from one change of boundary condition.
- **A non-homogeneous boundary condition breaks the eigenfunction expansion
  unless you first subtract a steady state.** If $u(0,t) = T_0$ and
  $u(L,t) = T_1$, write $u = v(x) + w(x,t)$ with $v$ the linear steady profile
  $v(x) = T_0 + (T_1 - T_0)x/L$; then $w$ satisfies the same equation with
  *homogeneous* boundary conditions and an initial condition $f(x) - v(x)$, and
  the machinery above applies. The trick fails when the steady state does not
  exist — for example when the boundary data are time-dependent, or when the
  equation itself has time-dependent coefficients.
- **Radiation conditions are qualitatively different.** A Sommerfeld condition
  selects the outgoing solution and turns a discrete eigenfunction problem into a
  continuous one. It is the boundary condition that makes a numerical domain act
  as though it were infinite, and [01-09-07](./07-boundary-value-problems.md)
  measures how well a first-order version performs.

### 7.1 Layered media: when eigenfunctions are not sines

If the medium is piecewise homogeneous, separation still works *within* each
layer, but the eigenfunctions are sines and cosines with different wavenumbers in
each layer, matched by continuity of $u$ and of the flux at each interface. The
frequencies are then the roots of a transcendental equation, not $n\pi c/L$, and
the mode shapes are not orthogonal in the simple sine sense. Standard tools:

- a **transfer-matrix** or propagator formulation, multiplying layer matrices;
- **dispersion relations**, solved numerically for each frequency (the same
  structure as surface-wave dispersion, treated in
  [01-mathematics/11-06 Dispersion Relations](../11-complex-analysis/06-dispersion-relations.md));
- for genuinely two- or three-dimensional heterogeneity, discretisation rather
  than separation.

The message is not that separation fails in the Earth; it is that the Earth
provides **piecewise** separability, and the bookkeeping across interfaces is
where the work lies.

## 8. Common mistakes

1. **Separating without checking the domain.** Separation needs the boundaries to
   align with coordinate surfaces. A wedge, a salt dome or a hill is not separable
   in Cartesian coordinates, and the appearance of a clean series solution is a
   sign that someone has built an unrepresentative model.
2. **Losing the eigenvalue problem.** The boundary conditions do not enter the
   time equation; they select the eigenvalues. Writing $u = X T$ and then solving
   the space equation with arbitrary $\lambda$ produces a formal solution that
   satisfies nothing.
3. **Forgetting the $\lambda \le 0$ case.** For Dirichlet conditions it gives only
   the zero solution, but for Neumann conditions $\lambda = 0$ is a genuine
   eigenvalue with a constant eigenfunction — and that constant mode is physically
   the last thing to decay, so omitting it changes long-time behaviour
   qualitatively.
4. **Using $\sin$ where the boundary conditions demand $\cos$.** An insulated end
   at $x = 0$ requires $X'(0) = 0$, hence cosines, hence $\lambda_n =
   ((n-\tfrac12)\pi/L)^2$ on a cosine basis if the other end is fixed. The
   eigenvalues change, and so does every decay rate.
5. **Truncating a series without checking the truncation error.** Section 4 does
   the check; a reference solution is only a reference once its own error is
   below the error being measured.
6. **Assuming the measured decay rate equals the material value.** The numerical
   eigenvalue differs by $O(\Delta x^2)$; the demonstration's $1.1\times10^{-4}$
   relative difference is discretisation, and interpreting it as rock property
   would be a quantitative error.
7. **Applying a steady-state correction when there is no steady state.**
   Time-dependent boundary data require a time-dependent particular solution, or
   Duhamel's principle, discussed in [01-09-07](./07-boundary-value-problems.md).
8. **Assuming orthogonality with the wrong weight.** For a non-uniform medium the
   eigenfunctions are orthogonal with respect to a weight function $w$, not
   uniformly. Projecting with the wrong weight gives coefficients that do not
   satisfy the equation.

## 9. Real-world applications

- **Borehole temperature logs.** The forward model of a surface temperature
  history is a sum of decaying modes; the inversion is a backward parabolic
  problem, and the eigenexpansion makes both the forward model and its
  ill-conditioning explicit.
- **Cooling of intrusions and lava lakes.** The leading eigenvalue gives the
  cooling timescale; the ratio of the first two eigenvalues tells you how quickly
  the profile becomes self-similar, which is why a single exponential fits the
  late-time cooling of a body so well.
- **Aquifer response.** Radial diffusion in a well test is a different geometry,
  but the same logic: eigenfunctions of the radial operator, with the wellbore
  condition as the boundary condition, and a theis-type solution as the
  fundamental response.
- **Normal modes of the Earth.** Free oscillations of a layered sphere are the
  eigenfunctions of the elastodynamic operator with a free surface, computed by
  exactly the layer-matching described in Section 7.1. Their frequencies are among
  the most precise constraints on deep-Earth structure.
- **Resonance in sedimentary basins.** A low-velocity basin traps waves; the
  resonant frequencies follow from the basin's eigenvalues, which is why
  earthquake damage concentrates in basins of particular depths and why
  microzonation studies measure the fundamental frequency.
- **Geothermal resource assessment.** The layered-Earth solution (7) with a
  measured surface gradient and a production model gives the temperature at
  target depth; the timescale check of Section 5.3 says whether a steady solution
  is admissible.
- **Wave propagation in boreholes.** Tube waves have their own eigenvalue problem
  because the boundary condition at the borehole wall couples fluid and solid.

## 10. Further reading

- **Farlow, S. J. (1993). *Partial Differential Equations for Scientists and
  Engineers*. Dover.** Level: intermediate. The clearest step-by-step treatment of
  separation of variables with worked boundary-value problems.
- **Haberman, R. (2013). *Applied Partial Differential Equations* (5th ed.).
  Pearson.** Level: intermediate to advanced. Sturm–Liouville theory, orthogonality
  and the completeness argument, with engineering applications.
- **Carslaw, H. S., & Jaeger, J. C. (1959). *Conduction of Heat in Solids*
  (2nd ed.). Oxford University Press.** Level: graduate. The authoritative
  catalogue of solutions for layered media, inhomogeneous boundary data and
  composite cylinders and spheres.
- **Turcotte, D. L., & Schubert, G. (2014). *Geodynamics* (3rd ed.). Cambridge
  University Press.** Level: advanced undergraduate upward. The thermal-structure
  and cooling problems of Sections 3 and 5 in their geophysical setting.
- **Dahlen, F. A., & Tromp, J. (1998). *Theoretical Global Seismology*. Princeton
  University Press.** Level: doctoral. Normal-mode theory; the rigorous version of
  Section 6 in a heterogeneous, self-gravitating, rotating Earth.
- **Courant, R., & Hilbert, D. (1962). *Methods of Mathematical Physics*, Vol. I.
  Interscience.** Level: graduate. The classical treatment of Sturm–Liouville
  theory and of the eigenfunction method.

> Note on citations: bibliographic details are given so you can locate the works.
> This repository does not host or reproduce copyrighted text; confirm current
> editions and availability through your library before citing.

## 11. Exercises

Solutions are in
[`exercises/05-separation-of-variables-solutions.md`](./exercises/05-separation-of-variables-solutions.md).

**★1.** Separate $u_t = \kappa u_{xx}$ on $0<x<L$ with $u_x(0,t) = 0$ and
$u(L,t) = 0$. Find the eigenvalues and eigenfunctions, and state whether
$\lambda = 0$ is allowed.

**★2.** For the triangular initial profile of Section 3, compute $b_1$ and $b_3$
analytically and compare with the numerical values 0.810569 and $-0.090063$.

**★3.** Using (8), compute $T$ at 15 km and 25 km for the illustrative parameters
of Section 5.2, and state how much of each value is due to the radiogenic term.

**★4.** Verify that $u = T_0 + (T_1 - T_0)x/L$ satisfies $u'' = 0$ and the
boundary conditions $u(0) = T_0$, $u(L) = T_1$. Then write down the problem
satisfied by $w = u - v$ for the heat equation with these boundary conditions.

**★★5.** For the string with $u(0,t) = 0$ and $u_x(L,t) = 0$, find the mode
frequencies and compare them with the fixed–fixed case of the same length. Which
is lower, and why does that make physical sense?

**★★6.** A 1 km thick layer has $\kappa = 10^{-6}\ \mathrm{m^2\,s^{-1}}$ and an
initial sinusoidal temperature perturbation of wavelength 200 km. Compute the
decay time of the fundamental from the eigenvalue, and reconcile the answer with
$\tau \sim L^2/\kappa$ using $L$ equal to a quarter of the wavelength.

**★★7.** Derive the transcendental equation for the eigenvalues of the Robin
problem $u_t = \kappa u_{xx}$, $u_x(0,t) = 0$, $-u_x(L,t) = h(u(L,t) - u_\infty)$
with homogeneous reduction $u_\infty = 0$. Show that as $h\to\infty$ the roots
approach the Dirichlet–Neumann eigenvalues, and state the physical meaning.

**★★8.** Derive the first two terms of the cooling of a sphere of radius $a$ with
a fixed zero surface temperature and a uniform initial temperature, using the
radial eigenfunctions. State, with numbers for granite, how the first two
eigenvalues compare and what that implies for fitting a single exponential to
observed cooling.

**★★★9.** Implement the eigenfunction solution for the slab problem with the
triangular initial profile and measure how many terms are required for a
$10^{-8}$ maximum-norm error at $t = 0.5$, $0.05$ and $0.005$. Report the counts,
explain the trend with $t$ using the modal attenuation factors, and state the
practical rule you would adopt.

**★★★10.** A borehole temperature profile is modelled with a layered conductivity
and a steady heat flow. Write out the layer-matching conditions, explain how they
give a transcendental equation for the modal decay rates, and describe an
algorithm that finds the slowest decay rate. State what would have to change for
the problem to become non-separable.

## 12. Self-assessment checklist

- [ ] I can carry out a separation, identify the eigenvalue problem, and say which
      equation carries the eigenvalues.
- [ ] I can compute eigenfunction expansion coefficients by projection and verify
      orthogonality numerically.
- [ ] I can solve the slab heat problem and check it against a numerical solution
      at second order.
- [ ] I can derive the geothermal gradient with production, get the sign right, and
      check whether steady state is admissible.
- [ ] I can obtain string mode frequencies and separate free (eigenvalue) from
      forced (amplitude) parameters.
- [ ] I can handle non-homogeneous boundary conditions by steady-state subtraction
      and say when that fails.
- [ ] I can recognise a non-separable problem and name the numerical alternative.

## Related lessons

- [01-09-02 The Diffusion/Heat Equation and Diffusive Timescales](./02-heat-equation.md)
  — where the eigenfunctions used here first appeared, together with the
  $L^2/\kappa$ timescale checked in Section 5.3.
- [01-09-03 The Wave Equation and Its Physical Content](./03-wave-equation.md) —
  the string modes and the CFL condition for their numerical solution.
- [01-09-04 Laplace and Poisson Equations in Earth Systems](./04-laplace-poisson.md)
  — the elliptic problems on finite domains whose solutions are also expansions
  of this kind.
- [01-09-07 Boundary and Initial-Boundary Value Problems](./07-boundary-value-problems.md)
  — the boundary-condition types in a well-posedness setting.
- [01-09-08 Weak Solutions, Variational Forms and Well-Posedness](./08-weak-solutions.md)
  — the variational alternative when no eigenbasis is available.
- [01-mathematics/10-fourier-analysis](../10-fourier-analysis/README.md) — the
  transform theory behind the expansion coefficients and their convergence.
- [01-mathematics/11-complex-analysis](../11-complex-analysis/README.md) — the
  Laplace transform, which handles the time dependence when separation fails.
