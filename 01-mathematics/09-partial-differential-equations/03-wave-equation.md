---
id: 01-09-03
title: "The Wave Equation and Its Physical Content"
level: advanced
prereqs: ["01-09-01", "01-06-07"]
estimated_minutes: 90
tags: [partial-differential-equations, wave-equation, d-alembert, characteristics, cfl-condition]
---

# The Wave Equation and Its Physical Content

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** $u_{tt} = c^2u_{xx}$ from a mechanical continuum, obtaining $c$ in
   terms of the material parameters rather than quoting it.
2. **Verify by substitution** that $u = F(x-ct) + G(x+ct)$ solves the equation
   for arbitrary $F$ and $G$, and interpret the two families as one-way waves.
3. **Read** the physical content of $c$: a material property, a finite
   propagation speed, the slope of characteristics, and the reason that first
   arrivals invert for structure.
4. **Derive** the Courant–Friedrichs–Lewy condition $c\,\Delta t \le \Delta x$
   for the explicit leapfrog scheme, from both the domain-of-dependence argument
   and a von Neumann analysis, and predict the growth rate when it is violated.
5. **Explain** why $\sigma = 1$ makes the scheme exact in one dimension, and why
   that exactness does not generalise to higher dimensions or variable velocity.
6. **Connect** the equation to the methods that use it: seismic body and surface
   waves, acoustic logging, ground-penetrating radar, tsunamis and the Earth's
   normal modes.

## Prerequisites

- [01-09-01 Classification of PDEs](./01-classification.md) — the hyperbolic
  class and the characteristic equation.
- [01-06-07 Vector Identities and Their Role in Geophysics](../06-multivariable-calculus/07-vector-identities.md)
  — the derivation of the elastic P/S wave equations from the momentum balance
  in a continuum.
- [01-06-04 Divergence, Curl and Physical Meaning](../06-multivariable-calculus/04-divergence-and-curl.md)
  — curl and divergence as the operations that separate P from S motion.
- [02-physics/03-oscillations-and-waves](../../02-physics/03-oscillations-and-waves/README.md)
  — the single-oscillator and standing-wave picture that this lesson generalises
  to a continuum.

## 1. Intuition: the equation of a plucked string, and of the Earth

Hold a rope taut and flick one end. A pulse travels down it, reflects, and comes
back. The speed does not depend on how hard you flick it, only on how tight the
rope is and how heavy; the shape of the pulse is preserved as it travels. Nothing
in that description involves diffusion or equilibrium: the disturbance
*propagates*, at a finite, measurable speed, and the two directions of travel are
independent of each other.

That is the entire physical content of

$$\frac{\partial^2 u}{\partial t^2} = c^2\frac{\partial^2 u}{\partial x^2}.$$

Three features distinguish it from the diffusion equation of
[01-09-02](./02-heat-equation.md):

- **Two time derivatives**, so the equation is symmetric under $t \to -t$:
  information can travel backwards as well as forwards, and no arrow of time
  appears.
- **A finite speed $c$**, replacing the diffusive spreading rate. The distance
  covered is proportional to time, not to its square root, so a wave front does
  not slow down.
- **No smoothing.** The equation preserves the shape of a pulse (for constant
  $c$), so sharp features stay sharp. Sharpness is information that diffusion
  destroys and waves conserve, which is exactly why seismic data are so much
  more informative than a diffused field.

## 2. Derivation from a continuum

### 2.1 The transverse vibration of a string

Let $u(x,t)$ be the transverse displacement of a string of *linear* density
$\rho_l$ (mass per unit length) under tension $T$. Consider the segment between
$x$ and $x+\Delta x$. Its mass is $\rho_l\Delta x$ and its transverse
acceleration is $u_{tt}$. For small slopes, $\partial u/\partial x \ll 1$, the
transverse component of the tension at each end is $T\,\partial u/\partial x$
evaluated at that end, and Newton's second law gives

$$\rho_l\,\Delta x\,u_{tt}
= T\left[u_x(x+\Delta x,t) - u_x(x,t)\right].$$

Dividing by $\Delta x$ and letting $\Delta x \to 0$:

$$\rho_l\,u_{tt} = T\,u_{xx}
\qquad\Longrightarrow\qquad
u_{tt} = c^2u_{xx}, \qquad c = \sqrt{\frac{T}{\rho_l}} . \tag{1}$$

Two things to note. First, the derivation used *only* Newton's second law and a
small-angle approximation; no wave was assumed. Second, the speed depends on the
ratio of restoring force to inertia, and only on that. Insert a plausible
laboratory value, $T = 100$ N and $\rho_l = 0.01\ \mathrm{kg\,m^{-1}}$, and
$c = \sqrt{10^4} = 100\ \mathrm{m\,s^{-1}}$: a wave crosses a 10 m rope in a
tenth of a second. Flicking harder changes the amplitude and not the speed, and
that independence is the signature of a *linear* wave equation.

### 2.2 The continuum limit, verified numerically

Why is the continuum version legitimate? Because it is the limit of a chain of
masses. For $N$ masses $m$ spaced $a$ apart joined by springs of stiffness $k$,

$$m\frac{d^2y_i}{dt^2} = k\left(y_{i+1} - 2y_i + y_{i-1}\right) . \tag{2}$$

Substituting the trial mode $y_i(t) = \sin(q\,i\,a)\cos(\omega t)$ and using the
identity $\sin(A+a) - 2\sin A + \sin(A-a) = -4\sin^2(a/2)\sin A$ gives the exact
dispersion relation of the chain,

$$\omega(q) = 2\sqrt{\frac{k}{m}}\,\left|\sin\frac{qa}{2}\right| ,
\qquad\text{so}\qquad
\frac{\omega}{q} \to a\sqrt{\frac{k}{m}} \quad (qa \to 0). \tag{3}$$

The demonstration evaluates (2) with the exact left-hand side and reports the
relative residual, then lists the speed:

```text
  assumed m = 1.0 kg, k = 1.0 N/m, a = 1.0 m  ->  c = a sqrt(k/m) = 1.000000 m/s

    q a (rad)   omega (exact)   omega/q (speed)   speed / c   relative residual
      0.04909      0.04908246        0.99989960    0.999900            1.13e-14
      0.09817      0.09813535        0.99959845    0.999598            9.28e-15
      0.39270      0.39018064        0.99358685    0.993587            4.61e-16
      1.57080      1.41421356        0.90031632    0.900316            2.56e-16
```

The residual is at round-off for every wavenumber: the trial mode solves the
discrete equations exactly, not approximately, so the chain result is a theorem
rather than a fit. Two physical readings:

- **The continuum limit is the long-wavelength limit.** At $qa = 0.049$ the
  lattice reproduces the continuum speed to four decimal places; at
  $qa = \pi/2$, where the wavelength is only four masses long, the speed is
  10 % low.
- **A discrete lattice is dispersive, and that is not a numerical artefact — it
  is physics.** A real crystal behaves this way too. The same phenomenon appears
  in a finite-difference grid, which is why a coarse mesh distorts short
  wavelengths and why numerical dispersion is a familiar artefact of seismic
  modelling.

### 2.3 The elastic continuum

For a homogeneous, isotropic, linearly elastic solid with Lamé parameters
$\lambda$ and $\mu$ and density $\rho$, the momentum balance plus Hooke's law
gives the elastodynamic equation

$$\rho\,\mathbf{u}_{tt} = (\lambda + \mu)\nabla(\nabla\cdot\mathbf{u})
+ \mu\nabla^2\mathbf{u} .$$

Applying the Helmholtz decomposition $\mathbf{u} = \nabla\phi + \nabla\times
\boldsymbol{\psi}$ — the step worked through with vector identities in
[01-06-07](../06-multivariable-calculus/07-vector-identities.md) — separates this
into two scalar wave equations:

$$\phi_{tt} = \alpha^2\nabla^2\phi, \quad
\alpha^2 = \frac{\lambda + 2\mu}{\rho}; \qquad
\psi_{tt} = \beta^2\nabla^2\psi, \quad
\beta^2 = \frac{\mu}{\rho}. \tag{4}$$

The scalar field $\phi$ describes **P** motion (particles parallel to
propagation, a divergence), and $\psi$ describes **S** motion (particles
perpendicular, a curl). This is why a seismic survey can measure two independent
elastic constants from two arrival times: the two wave speeds are two
combinations of $\lambda$, $\mu$ and $\rho$, and they carry different
information about the rock.

Insert illustrative rock values, $\rho = 2700\ \mathrm{kg\,m^{-3}}$,
$\lambda = \mu = 3.0\times10^{10}$ Pa:

$$\alpha = \sqrt{\frac{3.0\times10^{10} + 2\times3.0\times10^{10}}{2700}}
= \sqrt{\frac{9.0\times10^{10}}{2700}} = 5774\ \mathrm{m\,s^{-1}}, \qquad
\beta = \sqrt{\frac{3.0\times10^{10}}{2700}} = 3333\ \mathrm{m\,s^{-1}} .$$

Both are in the range of laboratory and field measurements for crustal rock, and
the ratio $\alpha/\beta = \sqrt{3}$ reflects the choice $\lambda = \mu$. Poisson's
ratio is tied to that ratio by
$\nu = (\alpha^2 - 2\beta^2)/(2(\alpha^2 - \beta^2))$, so a real measurement of
$\alpha/\beta$ is a measurement of $\nu$ — an excellent illustration that a PDE
and its parameters are the same object seen twice.

### 2.4 The shallow-water and acoustic analogues

The same equation governs many other media, and the table is worth keeping,
because it is the reason "wave equation" problems in geophysics all look alike:

| Medium | Quantity | Speed |
|---|---|---|
| String | transverse displacement | $\sqrt{T/\rho_l}$ |
| Elastic solid | $\phi$ / $\boldsymbol{\psi}$ | $\sqrt{(\lambda+2\mu)/\rho}$, $\sqrt{\mu/\rho}$ |
| Fluid | pressure | $\sqrt{1/(\rho\kappa)}$ ($\kappa$ = compressibility) |
| Shallow water ($h \ll$ wavelength) | surface elevation | $\sqrt{gh}$ |
| Low-loss dielectric (GPR) | electric field | $c_0/\sqrt{\epsilon_r}$ |

The shallow-water entry is a good test of physical reasoning: with $h = 4000$ m,
$c = \sqrt{9.81\times4000} = 198\ \mathrm{m\,s^{-1}} \approx 713\ \mathrm{km\,h^{-1}}$,
which is the observed speed of a tsunami in open ocean — and the amplitude
increase at the shore follows from the same equation through the reduction in
$h$, not from any additional physics.

## 3. Solution by characteristics: d'Alembert's formula

We showed in [01-09-01](./01-classification.md) §3.2 that the change of
variables $\xi = x - ct$, $\eta = x + ct$ reduces the wave equation to
$u_{\xi\eta} = 0$, whose general solution is

$$u(x,t) = F(x - ct) + G(x + ct). \tag{5}$$

The lines $x - ct = \text{const}$ and $x + ct = \text{const}$ are the
characteristics, and $F$ and $G$ are **one-way waves**: the profile $F$ moves
right without changing shape, and $G$ moves left. Verify by substitution with the
chain rule:

$$\frac{\partial}{\partial t}F(x-ct) = -cF', \quad
\frac{\partial^2}{\partial t^2}F(x-ct) = c^2F'', \quad
\frac{\partial^2}{\partial x^2}F(x-ct) = F'',$$

so $u_{tt} = c^2u_{xx}$ term by term for any twice-differentiable $F$ and $G$.
That is the whole proof, and it is worth seeing the demonstration's numerical
version of it: central differences of an exact travelling pulse must produce a
residual that vanishes at the rate the discretisation allows.

```text
  c = 1.5, F(x) = exp(-x^2) cos(3x), G(x) = 0.5 F(x)
  differentiated at x = 0.3, t = 0.4

           h     |u_tt - c^2 u_xx|   order
    1.00e-01             3.934e-03        
    5.00e-02             9.609e-04    2.03
    2.50e-02             2.388e-04    2.01
    1.25e-02             5.960e-05    2.00
    6.25e-03             1.490e-05    2.00
```

Order 2, as the second-order differences require, so what remains is truncation
error and the identity is confirmed. One special case is worth noting: if the
time step and the space step are *equal* and $c = 1$, the two difference
operators sample exactly the same points along the characteristic and the
residual is *identically zero*. That is the same alignment of stencil and
characteristic that makes the leapfrog scheme exact at Courant number 1, Section
5.3.

### 3.1 Characteristics and Riemann invariants

Define the combinations

$$w_\pm = u_t \mp c\,u_x .$$

Then $w_\pm$ satisfies the one-way equation $\partial_t w_\pm \pm c\,\partial_x
w_\pm = 0$, so $w_+$ is constant along $dx/dt = +c$ and $w_-$ along $dx/dt = -c$.
The demonstration verifies this numerically with central differences:

```text
  c = 2.0, u = F(x - ct) + 0.3 F(x + ct), F(x) = exp(-x^2)

         t   x = x0 + ct     u_t - c u_x   x = x0 - ct     u_t + c u_x
       0.0        0.0000    0.0000000000        0.0000    0.0000000000
       0.1        0.2000   -0.0000000001       -0.2000   -0.0000000001
       0.2        0.4000   -0.0000000002       -0.4000   -0.0000000003
       0.3        0.6000    0.0000000001       -0.6000   -0.0000000002
```

Each invariant is constant to $10^{-10}$ along its own characteristic. This is
the mathematical statement of a physical fact that seismology is built on: **the
disturbance at $(x_0,0)$ can only influence points inside the cone
$\lvert x - x_0\rvert \le ct$.** Nothing outside it can carry that information,
which is why first-arrival times constrain structure, why rays are useful at all,
and — as the next section shows — why an explicit numerical scheme must respect
the same cone.

### 3.2 Standing waves

Adding a right-going wave to its mirror image gives a **standing wave**

$$u = \tfrac{1}{2}f(x - ct) + \tfrac{1}{2}f(x + ct).$$

On a finite interval with fixed ends the only admissible motions are standing
waves with discrete frequencies. For a string of length $L$ pinned at both ends,

$$u_n(x,t) = \sin\!\left(\frac{n\pi x}{L}\right)\cos(\omega_n t), \qquad
\omega_n = \frac{n\pi c}{L} , \tag{6}$$

and each $n$ is a normal mode. The demonstration checks (6) directly: each mode
is an exact solution (residuals $10^{-10}$ to $10^{-11}$ at $h = 10^{-3}$,
which is cancellation error in the second differences, not model error), the
refinement study gives order 2.00, and the eigenfunctions are orthogonal,

$$\int_0^L\sin\frac{n\pi x}{L}\sin\frac{m\pi x}{L}\,dx = \frac{L}{2}\delta_{nm},$$

checked numerically to 9 decimal places. The same construction in three
dimensions with free-surface boundary conditions produces the Earth's normal
modes, whose measured frequencies constrain the radial structure of the planet;
[01-09-05](./05-separation-of-variables.md) develops the machinery.

## 4. Energy, impedance and what reflection measures

Multiply the wave equation by $u_t$ and integrate over a fixed interval with
fixed ends:

$$\frac{d}{dt}\int \left(\tfrac{1}{2}u_t^2 +
\tfrac{1}{2}c^2u_x^2\right)dx = 0 . \tag{7}$$

The bracket is a **conserved energy density**: kinetic ($\tfrac12 u_t^2$) plus
elastic ($\tfrac12 c^2u_x^2$). Compare the diffusion equation, where the
corresponding quantity decays monotonically — that monotone decay is the energy
proof of uniqueness in [01-09-07](./07-boundary-value-problems.md). Energy
conservation is why a wave can carry a signal over thousands of kilometres
without losing it to smoothing, and why seismic amplitudes can be inverted for
attenuation, which is a *departure* from this idealisation.

At a boundary or interface where $c$ changes, (7) forces continuity of $u$ and of
the flux $c^2u_x$ (for a string, of $T u_x$; in general, of the quantity
$Z u_t$ with $Z = \rho c$ the **acoustic impedance**). The resulting reflection
coefficient for normal incidence is

$$R = \frac{Z_2 - Z_1}{Z_2 + Z_1} .$$

This formula is the basis of seismic reflection interpretation: $R$ is determined
by the impedance contrast, so amplitudes are interpreted as contrasts in $\rho c$,
and a large $R$ at a known interface (a water bottom, a coal seam) is used to
calibrate the amplitudes of unknown ones.

## 5. Numerical solution and the CFL condition

### 5.1 The leapfrog scheme

Discretise with a second-order central difference in *both* variables (the
explicit **leapfrog** scheme):

$$u^{n+1}_j = 2u^n_j - u^{n-1}_j + \sigma^2\left(u^n_{j+1} - 2u^n_j +
u^n_{j-1}\right), \qquad \sigma = \frac{c\,\Delta t}{\Delta x} . \tag{8}$$

Two time levels are needed, so the initial velocity must be handled explicitly.
For $u_t(x,0) = 0$ the second-order start is

$$u^{-1}_j = u^0_j + \tfrac{1}{2}\sigma^2\left(u^0_{j+1} - 2u^0_j +
u^0_{j-1}\right).$$

Using $u^{-1}_j = u^0_j$ instead is only first-order accurate and pollutes the
whole solution with an $O(\Delta t)$ error — an error caught while producing this
lesson's demonstration, and one worth remembering: **initial conditions must be
imposed to the same order as the interior scheme.** Section 5 measures both
initialisations on the standing-wave problem: at $N = 20$ the maximum error is
$5.43\times10^{-4}$ with the second-order start and $2.87\times10^{-2}$ with the
naive one — a factor of 53, rising to 863 at $N = 320$, which is the signature of
an error falling like $\Delta t$ rather than $\Delta t^2$. With the correct start
the measured convergence order is 2:

```text
      N   Courant    max error   order
     20      0.48    5.425e-04        
     40      0.49    1.413e-04    1.94
     80      0.50    3.603e-05    1.97
    160      0.50    9.097e-06    1.99
    320      0.50    2.285e-06    1.99
```

(The script reports the *achieved* Courant number, because the time step has to
be rounded to an integer number of steps between the two requested times; on the
coarsest grids that rounding is visible in the third digit. Reporting the
achieved value rather than the requested one is the difference between a
verification and a coincidence.)

### 5.2 The CFL condition, by two arguments

**Domain of dependence.** The stencil (8) reaches one cell to each side per step,
so after $n$ steps the numerical solution at a point depends on data within $n$
cells. The exact solution depends on data within $ct = \sigma n \Delta x/\Delta x$
— that is, within $\sigma n$ cells. The scheme can only be convergent if its
dependence region *contains* the exact one:

$$\sigma n \ge n \quad\Longrightarrow\quad \sigma \le 1 . \tag{9}$$

This is the Courant–Friedrichs–Lewy condition. It is not a technicality about
round-off; it says that a scheme which never saw the right data cannot produce
the right answer.

**Von Neumann analysis.** Put $u^n_j = g^n\mathrm{e}^{\mathrm{i}j\theta}$ in (8):

$$g^2 - 2\left(1 - 2\sigma^2\sin^2\frac{\theta}{2}\right)g + 1 = 0 .$$

The product of the roots is 1, so the scheme is stable if and only if both roots
have modulus 1, i.e. if and only if

$$\left\lvert 1 - 2\sigma^2\sin^2\frac{\theta}{2}\right\rvert \le 1
\quad\text{for all } \theta \quad\Longleftrightarrow\quad \sigma \le 1 .$$

For $\sigma > 1$ the alternating grid mode $\theta = \pi$ is amplified by

$$\lvert g\rvert = \frac{\lvert 2 - 4\sigma^2\rvert +
\sqrt{(2-4\sigma^2)^2 - 4}}{2} . \tag{10}$$

The demonstration runs that mode and compares the measurement with (10):

```text
     sigma  steps   final max|u|  observed growth/step    theory     verdict
      0.50   2000         0.7609              0.999863  1.000000      stable
      0.90   2000            2.3              1.000416  1.000000      stable
      1.01    200      8.159e+24              1.332166  1.326584    UNSTABLE
      1.05    100      3.155e+27              1.883603  1.877328    UNSTABLE
```

The agreement to three decimal places is the verification: the instability is
exponential with exactly the predicted rate, and no amount of care in the coding
removes it. A run at $\sigma = 1.05$ grows by $10^{27}$ in a hundred steps.

### 5.3 Why $\sigma = 1$ is exact in one dimension

At $\sigma = 1$ the stencil lies exactly on the characteristics of the
one-dimensional problem, so it computes the exact translation of the initial
data instead of approximating it. The demonstration confirms this with a
standing wave, $\sigma$ set to exactly 1.0:

```text
(b) At sigma = 1.0 exactly (N = 99, dx = dt = 0.01) the standing-wave
    error is 4.441e-16 (achieved sigma = 1.000000)
```

Round-off, not truncation error. And with a compact travelling pulse at
$\sigma = 1$:

```text
  predicted support    = [0.460000, 0.540000]
  numerical support    = [0.461667, 0.538333]
  max error vs exact   = 6.439e-15   (round-off level)
  max |u| beyond cone  = 0.000e+00   (exactly zero)
```

Two cautions about this exactness, because it is often over-claimed:

- it holds for **constant** $c$ in **one** spatial dimension; with variable
  velocity, the characteristic does not coincide with the grid anywhere except
  by accident, and the scheme returns to second-order accuracy;
- in two or three dimensions no single $\Delta t$ puts the stencil on the
  characteristics for all directions, so a CFL condition
  $\sigma \le 1/\sqrt{d}$ in $d$ dimensions is required and exactness is lost.

Even in one dimension with constant velocity, $\sigma = 1$ is rarely used in
practice: the scheme is then neutrally stable, so any error introduced by a
variable-velocity region, a boundary or round-off never decays.

### 5.4 Other numerical issues that follow from the physics

- **Numerical dispersion.** Because a grid is a lattice, the discrete dispersion
  relation is (3), not $\omega = ck$: short wavelengths travel at the wrong
  speed. The remedy is more points per wavelength (typically 8–10 for a
  second-order scheme), or a higher-order or spectral method.
- **Absorbing boundaries.** The physical Earth does not end, but the
  computational box does. [01-09-07](./07-boundary-value-problems.md) measures a
  first-order one-way boundary condition leaving 0.07 % of the incident
  amplitude, against 100 % for a fixed boundary.
- **Elastic versus acoustic.** An acoustic (scalar) approximation suppresses
  S waves and mode conversions; it is appropriate for a fluid and for the deep
  marine water column, and inappropriate for the shallow sub-surface, where
  shear modulus contrasts dominate the reflections.
- **Variable velocity.** Section 6 of the demonstration repeats the convergence
  study with $c(x) = 1 + 0.5\sin(2\pi x)$ and a time step set by $c_{\max}$, and
  finds order 2 still (1.97, 1.98, 1.96, 2.00): second-order accuracy survives the
  variation because the coefficient is smooth. What does *not* survive is the
  exactness at $\sigma = 1$, since no single $\Delta t/\Delta x$ can place the
  stencil on the characteristics at every node once $c$ varies.

## 6. What the equation implies about data

| Property | Consequence for measurement |
|---|---|
| Finite speed $c$ | arrival times are measurable and invertible for $c(x)$ |
| Reversibility | time-reversal and back-propagation (migration) are meaningful operations |
| Energy conservation | amplitudes carry attenuation information, because any decay is a departure from the ideal |
| Shape preservation (constant $c$) | resolution is limited by the source and the recording, not by the medium |
| Two speeds in an elastic solid | P and S arrivals give two independent elastic parameters |
| Dispersion in a lattice or a real crystal | velocity depends on frequency, so a single $c$ is a long-wavelength limit |

Read the second row again: the wave equation is the only one of the three
canonical equations that can be run backwards. Migration and time-reversal
imaging exist because of it, and they are the reason seismic imaging is so much
sharper than potential-field interpretation. Compare the backward diffusion
problem of [01-09-07](./07-boundary-value-problems.md), where the same
backward-running idea destroys the data.

## 7. Common mistakes

1. **Believing $c$ depends on amplitude or frequency.** For the linear,
   non-dispersive equation it does not. If a measured velocity depends on
   frequency (as in surface waves, or in real rock over a wide band) then the
   model is dispersion and the governing equation is no longer (1);
   [01-mathematics/11-06 Dispersion Relations](../11-complex-analysis/06-dispersion-relations.md)
   treats the general theory.
2. **Using a first-order start for the initial velocity.** It reduces the whole
   solution to first order. Use $u^{-1}_j$ from the Taylor expansion.
3. **Forgetting the factor $c$ in the CFL number.** The condition is
   $\sigma = c\Delta t/\Delta x \le 1$, not $\Delta t \le \Delta x$. In a model
   with velocities varying by a factor of five, the largest velocity sets the
   time step for the whole mesh.
4. **Assuming $\sigma = 1$ buys exactness in two dimensions.** It does not; the
   limit is $1/\sqrt{2}$ in 2-D for the standard five-point stencil.
5. **Treating numerical dispersion as a physical observation.** A coarse grid
   makes short wavelengths too slow. Before attributing a velocity variation to
   geology, refine the grid and re-measure.
6. **Assuming that a fixed (Dirichlet) boundary is "simple".** It reflects
   100 % of the incident energy and will contaminate any solution that is meant
   to radiate. Boundary conditions are physics; choose them.
7. **Confusing particle velocity with wave speed.** $u_t$ is the particle
   velocity at a point and can be many orders of magnitude smaller than $c$.
8. **Omitting the elastic boundary conditions.** At a free surface the traction
   vanishes, which for a scalar acoustic model means a pressure-release condition
   (a sign flip on reflection); using a rigid condition instead inverts the
   polarity of every surface reflection.

## 8. Real-world applications

- **Seismic reflection and refraction.** Travel times of the hyperbolic PDE
  invert for $c(x,z)$; amplitudes, via the impedance formula of Section 4,
  constrain $\rho c$ and hence lithology. Most of the seismic method is the
  geometry of the characteristics.
- **Earthquake seismology.** First arrivals, moveout and the ratio of P to S
  travel times give $\alpha/\beta$ and hence Poisson's ratio; the same
  characteristics carry the focal-mechanism information.
- **Global normal modes.** Free oscillations after a great earthquake are the
  standing-wave solutions (6) of a spherical elastic Earth; their measured
  frequencies are among the strongest constraints on density and elasticity in
  the deep interior.
- **Ground-penetrating radar.** In low-loss media the electric field obeys the
  wave equation with $c = c_0/\sqrt{\epsilon_r}$, so a measured two-way travel
  time gives the depth and the dielectric constant. This is the wave-regime
  counterpart to the magnetotelluric skin depth of
  [01-09-02](./02-heat-equation.md).
- **Acoustic logging.** A borehole sonic tool measures the speed of the
  tube wave and the formation P wave with the same equation, and converts them
  to porosity and lithology through rock physics.
- **Tsunami warning.** The shallow-water wave equation propagates the initial
  sea-surface disturbance, and $\sqrt{gh}$ explains both the open-ocean speed
  and the amplification at the coast.
- **Numerical modelling.** Every seismic modelling code is a discretisation of
  this equation (or its elastic generalisation), and every one of them carries a
  CFL limit, a dispersion budget and an absorbing-boundary problem.

## 9. Further reading

- **Aki, K., & Richards, P. G. (2002). *Quantitative Seismology* (2nd ed.).
  University Science Books.** Level: graduate. The definitive treatment of the
  elastodynamic equation, its Green's functions, and the interpretation of
  amplitudes.
- **Whitham, G. B. (1974). *Linear and Nonlinear Waves*. Wiley.** Level:
  graduate. Characteristics, dispersion relations and the nonlinear theory;
  Chapter 1 is the best short account of d'Alembert's solution and its
  limitations.
- **Telford, W. M., Geldart, L. P., & Sheriff, R. E. (1990). *Applied
  Geophysics* (2nd ed.). Cambridge University Press.** Level: intermediate.
  The seismic and radar methods read at the level of the wave equation.
- **Feynman, R. P., Leighton, R. B., & Sands, M. (1964). *The Feynman Lectures
  on Physics*, Vol. I, Ch. 47–49. Addison-Wesley.** Level: beginner upward.
  The clearest physical treatment of normal modes and of why a lattice
  disperses.
- **LeVeque, R. J. (2002). *Finite Volume Methods for Hyperbolic Problems*.
  Cambridge University Press.** Level: graduate. The modern reference for the
  CFL condition, upwind and high-resolution schemes, and for what happens when
  the PDE is nonlinear.
- **Igel, H. (2017). *Computational Seismology*. Oxford University Press.**
  Level: graduate. Practical finite-difference modelling of the wave equation,
  including dispersion analysis and absorbing boundaries.

> Note on citations: bibliographic details are given so you can locate the works.
> This repository does not host or reproduce copyrighted text; confirm current
> editions and availability through your library before citing.

## 10. Exercises

Solutions are in
[`exercises/03-wave-equation-solutions.md`](./exercises/03-wave-equation-solutions.md).

**★1.** For $T = 250$ N and $\rho_l = 0.02\ \mathrm{kg\,m^{-1}}$, compute $c$ and
the travel time over 15 m.

**★2.** Verify by substitution that $u = \sin(kx)\cos(\omega t)$ solves
$u_{tt} = c^2u_{xx}$ provided $\omega = ck$. State what this says about the
frequencies of a pinned string of length $L$.

**★3.** Compute $\alpha$ and $\beta$ from (4) for
$\rho = 2600\ \mathrm{kg\,m^{-3}}$, $\lambda = 2.0\times10^{10}$ Pa,
$\mu = 1.5\times10^{10}$ Pa. Then compute Poisson's ratio from
$\nu = (\alpha^2-2\beta^2)/(2(\alpha^2-\beta^2))$ and comment on the value.

**★4.** A tsunami crosses 1000 km of ocean of depth 4 km. Compute the travel
time and state the assumptions of the shallow-water approximation.

**★★5.** Derive the CFL condition from the von Neumann analysis in full,
including the completion of the square and the determination of the stability
boundary. State where the alternating mode $\theta = \pi$ enters.

**★★6.** For $\sigma = 1.02$ compute the modulus of the amplification factor
from (10) and predict the factor by which an initial error of $10^{-12}$ grows
in 500 steps. Then say whether the failure would be visible in single precision
(about 7 decimal digits) after 500 steps.

**★★7.** Show that the leapfrog scheme with $\sigma = 1$ reduces to
$u^{n+1}_j = u^n_{j+1} + u^n_{j-1} - u^{n-1}_j$ and verify that
$u^n_j = f(j\Delta x - n\Delta t)$ satisfies it for any $f$. Under what
condition on the initial velocity does this make the scheme exact?

**★★8.** The energy (7) is conserved. Show that a scheme which damps energy
cannot be energy-preserving but may still converge; explain why a
non-dissipative scheme (like leapfrog) is preferred for long records but is
vulnerable to parasitic modes.

**★★★9.** Implement the leapfrog scheme for the wave equation with a
variable velocity $c(x) = 1 + 0.5\sin(2\pi x)$ and measure the convergence order
against a grid-refinement reference at fixed final time. Report the order you
observe, explain why the $\sigma = 1$ exactness of the constant-velocity case
does not survive, and state how you chose the time step.

**★★★10.** A modelling code uses a uniform grid with $\Delta x = 10$ m and
$c_{\max} = 6000\ \mathrm{m\,s^{-1}}$. A colleague proposes
$\Delta t = 2\ \mathrm{ms}$. Compute $\sigma$; state whether the run will be
stable; if not, propose a time step and state the cost penalty in wall-clock
time relative to their proposal. Then discuss the trade-off between the CFL
limit and grid dispersion for 40 Hz data with 8 points per wavelength.

## 11. Self-assessment checklist

- [ ] I can derive the string wave equation and identify $c$ in terms of
      measurable parameters.
- [ ] I can verify d'Alembert's solution by substitution and state what each
      one-way family represents.
- [ ] I can derive the CFL condition by two independent arguments and reproduce
      the amplification factor for $\sigma > 1$.
- [ ] I can explain why $\sigma = 1$ is exact in 1-D and why that exactness does
      not survive in 2-D or with variable velocity.
- [ ] I can state why the wave equation is time-reversible and why that is the
      foundation of migration.
- [ ] I can compute a P and S velocity from $\lambda$, $\mu$ and $\rho$ and
      connect their ratio to Poisson's ratio.
- [ ] I can explain the difference between a reflecting and an absorbing
      boundary in terms of energy, not terminology.

## Related lessons

- [01-09-01 Classification of PDEs](./01-classification.md) — where the
  hyperbolic class and its two characteristic families were established.
- [01-09-02 The Diffusion/Heat Equation and Diffusive Timescales](./02-heat-equation.md)
  — the same mathematics without the finite speed, and why that changes what the
  data can see.
- [01-09-05 Separation of Variables and Boundary Conditions](./05-separation-of-variables.md)
  — normal modes of a bounded string and of a layered medium.
- [01-09-07 Boundary and Initial-Boundary Value Problems](./07-boundary-value-problems.md)
  — reflecting versus radiating boundaries, measured.
- [02-physics/03-oscillations-and-waves](../../02-physics/03-oscillations-and-waves/README.md)
  — the oscillator and standing-wave picture that this lesson extends to a
  continuum.
- [02-physics/04-elasticity-and-continuum-mechanics](../../02-physics/04-elasticity-and-continuum-mechanics/README.md)
  — the derivation of (4) from stress and strain.
- [06-seismology](../../06-seismology/README.md) — the equation in its natural
  habitat: rays, arrivals, normal modes and attenuation.
- [01-mathematics/11-complex-analysis](../11-complex-analysis/README.md) — the
  Laplace and Fourier machinery used for transient and harmonic wave problems.
