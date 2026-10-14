---
id: 01-09-01
title: "Classification of PDEs: Elliptic, Parabolic, Hyperbolic"
level: advanced
prereqs: ["01-06-08"]
estimated_minutes: 90
tags: [partial-differential-equations, classification, elliptic, parabolic, hyperbolic]
---

# Classification of PDEs: Elliptic, Parabolic, Hyperbolic

## Learning objectives

By the end of this lesson you will be able to:

1. **Identify** the order, linearity and principal part of a second-order partial
   differential equation, and classify it from the discriminant
   $B^2 - AC$ of that principal part.
2. **Derive** the classification from the characteristic equation, and reduce
   each class to its canonical form by an explicit change of variables.
3. **State** which data an equation of each class requires — boundary data,
   initial data, or both — and explain why the requirement follows from the
   mathematics and not from convention.
4. **Map** the three classes onto the three families of geophysical measurement:
   elliptic to potential fields and steady flow, parabolic to everything that
   diffuses, hyperbolic to everything that propagates.
5. **Explain** how one physical process changes class with frequency, using the
   electromagnetic example (GPR propagates, magnetotellurics diffuses), and why
   the same rock obeys two different equations in two different experiments.
6. **Predict** the qualitative behaviour of a solution — smoothing, propagation
   or global equilibration — from the class alone, before solving anything.

## Prerequisites

- [01-06-08 Potential Fields, Laplace and Poisson Equations](../06-multivariable-calculus/08-potential-theory.md)
  — the elliptic prototype, harmonic functions and the uniqueness theorems we
  generalise here.
- [01-06-06 Gauss, Stokes and Green Theorems](../06-multivariable-calculus/06-integral-theorems.md)
  — the divergence theorem, used to turn conservation statements into PDEs.
- [01-06-07 Vector Identities and Their Role in Geophysics](../06-multivariable-calculus/07-vector-identities.md)
  — in particular the identities that produce the diffusion and wave equations.
- [01-05-xx Single-Variable Calculus](../05-single-variable-calculus/README.md) —
  ordinary differential equations, which we meet again as the characteristic
  equations of a PDE.

## 1. Intuition: three equations, three families of measurement

Almost every partial differential equation in geophysics is one of three
equations, or a cousin of one of them:

$$\nabla^2 u = 0 \quad\text{(Laplace)}, \qquad
\frac{\partial u}{\partial t} = \kappa \nabla^2 u \quad\text{(diffusion)},
\qquad
\frac{\partial^2 u}{\partial t^2} = c^2 \nabla^2 u \quad\text{(wave)}.$$

These are not three arbitrary formulas. They are the three possible answers to
the question *what happens to a disturbance?*:

| Equation | What a disturbance does | What that means for measurement |
|---|---|---|
| Laplace / Poisson | Nothing moves; the field adjusts instantly and globally | The measurement sees a steady state that encodes the whole boundary and the whole source distribution at once |
| Diffusion | It spreads, smooths and decays, with no finite speed | A measurement constrains the source only through a decay factor, and timing gives you $\tau \sim L^2/\kappa$ rather than a velocity |
| Wave | It travels at a finite speed $c$ along rays | Arrival times, moveout and phases are measurable, so the data are far more informative |

This is the organising idea of the module, and it is worth stating as flatly as
possible: **the three canonical PDEs are the three families of geophysical
measurement.** Gravity, magnetics, DC resistivity, self-potential and
steady-state groundwater flow are elliptic. Heat flow, pore-pressure diffusion,
aquifer response and controlled-source electromagnetics in the diffusive regime
are parabolic. Seismic body and surface waves, GPR, acoustic logging and
normal-mode seismology are hyperbolic. When a paper tells you which equation
governs its data, it has told you what the data can and cannot see.

The classification is therefore not a labelling exercise. It determines:

- **which data you must collect** (boundary values, an initial state, or both);
- **how informative the data are** (a diffused field is a smoothed source; an
  arrival time is a sharp constraint);
- **what the numerics must be** (a large linear solve, or a time march with a
  Courant step limit);
- **what the inverse problem looks like** (and, as
  [01-09-04](./04-laplace-poisson.md) shows, why elliptic inversion is
  intrinsically non-unique).

## 2. Precise definitions

### 2.1 Order, linearity, homogeneity

A **partial differential equation** of order $m$ relates an unknown function
$u$ of several independent variables to its partial derivatives up to order $m$.
The equation is **linear** if $u$ and its derivatives appear only to the first
power with coefficients depending on the independent variables alone. It is
**homogeneous** if there is no term free of $u$. We work with second-order
linear equations in two independent variables, which is enough to see everything:

$$A\,u_{xx} + 2B\,u_{xy} + C\,u_{yy} + D\,u_x + E\,u_y + F\,u = G, \tag{1}$$

where $A,\dots,G$ may depend on $x$ and $y$ but not on $u$. We write
$u_{xx} = \partial^2 u/\partial x^2$ and so on.

The terms containing the highest derivatives, here $A u_{xx} + 2B u_{xy} +
C u_{yy}$, form the **principal part**. Only the principal part decides the
class, and that is not a technicality: the lower-order terms change the solution
but never the kind of problem you are solving. Water diffusing with a source is
still water diffusing.

### 2.2 The discriminant

The classification is read from the **discriminant** of the principal part,

$$\Delta = B^2 - AC. \tag{2}$$

| | Condition | Class | Prototype |
|---|---|---|---|
| $\Delta < 0$ | | **elliptic** | $u_{xx} + u_{yy} = 0$ |
| $\Delta = 0$ | | **parabolic** | $u_t = u_{xx}$ |
| $\Delta > 0$ | | **hyperbolic** | $u_{tt} = c^2 u_{xx}$ |

The analogy with the conic sections $Ax^2 + 2Bxy + Cy^2 = 1$ is exact, and not
a coincidence: the same quadratic form describes both. Note the factor of 2 in
front of $B$ in (1) — it makes the discriminant clean, and omitting it is one of
the two most common errors in the whole subject. The other is forgetting that
$A$, $B$ and $C$ may themselves be functions, so an equation can be elliptic in
one region and hyperbolic in another (**mixed type**, e.g. the Tricomi equation
$u_{xx} - x\,u_{yy} = 0$: elliptic for $x<0$, hyperbolic for $x>0$).

### 2.3 The same test in $n$ dimensions

For a second-order linear equation in $n$ variables, take the symmetric
coefficient matrix $A_{ij}$ of the principal part, $A_{ij}u_{x_ix_j}$, and look at
its eigenvalues. Replace $x_1$ by a time-like variable in the usual way: the
equation is

- **elliptic** if all eigenvalues have the same sign and none vanishes;
- **parabolic** if exactly one eigenvalue vanishes (and the remaining ones
  share a sign);
- **hyperbolic** if one eigenvalue has one sign and the rest have the opposite
  sign.

For $n = 2$ this reduces to (2). Both versions are used in practice: the
$2\times2$ discriminant when the equation is written out, the eigenvalue test
when it comes from a continuum mechanics derivation with an anisotropic
coefficient matrix.

## 3. Derivation: where the classification comes from

### 3.1 The characteristic equation

Look for curves $y = y(x)$ along which the equation degenerates to an ordinary
differential equation — the **characteristics**. Parametrise a curve by $s$ and
let $u$ be given on it. Along the curve, differentiation gives

$$u_x = u_s s_x , \qquad u_{xx} = u_{ss} s_x^2 + \dots,$$

and a short calculation (carried out in full in most textbooks, and exactly the
computation that produces the eikonal equation when reapplied to rays)
shows that the second derivatives along the curve cannot be determined from the
data on the curve precisely when

$$A\left(\frac{dy}{dx}\right)^2 - 2B\frac{dy}{dx} + C = 0. \tag{3}$$

Solving (3),

$$\frac{dy}{dx} = \frac{B \pm \sqrt{B^2 - AC}}{A}
= \frac{B \pm \sqrt{\Delta}}{A}. \tag{4}$$

Read the consequences off the sign of $\Delta$:

- $\Delta > 0$: two distinct real families of characteristics. Data propagate
  along them, and the equation is **hyperbolic**.
- $\Delta = 0$: one real family. There is a single direction along which data
  propagate, and that direction is time. The equation is **parabolic**.
- $\Delta < 0$: no real characteristics. No direction in the plane is special,
  so no direction is privileged and information diffuses everywhere at once.
  The equation is **elliptic**.

The classification is thus a statement about whether the equation possesses
preferred directions, and that is exactly the difference between propagation and
smoothing. It is also why the CFL condition of
[01-09-03](./03-wave-equation.md) is a *hyperbolic* phenomenon: the grid must
contain the real characteristics, and an elliptic problem has none to contain.

### 3.2 Reduction to canonical form

Choose new coordinates $(\xi,\eta)$ constant along the characteristics. Carrying
out the change of variables in (1) collapses the principal part to one of three
forms:

| Class | Canonical form | Meaning of the coordinates |
|---|---|---|
| Hyperbolic | $u_{\xi\eta} = \dots$, or $u_{\xi\xi} - u_{\eta\eta} = \dots$ | $\xi,\eta$ constant on the two characteristic families |
| Parabolic | $u_{\xi\xi} = \dots$ | $\eta$ is the single characteristic coordinate (time) |
| Elliptic | $u_{\xi\xi} + u_{\eta\eta} = \dots$ | $\xi + i\eta$ is a complex characteristic; no real ones |

For the wave equation in the form $-c^2u_{xx} + u_{tt} = 0$ (treating $x$ and
$t$ as the two independent variables, so $A = -c^2$, $B = 0$, $C = 1$) the
characteristics are $x \mp ct = \text{const}$ and the canonical form is
$u_{\xi\eta} = 0$, whose general solution is $u = F(\xi) + G(\eta) = F(x - ct) +
G(x + ct)$: **d'Alembert's solution, obtained with no physics at all.**
[01-09-03](./03-wave-equation.md) supplies the physics; the mathematics has
already supplied the shape.

**Worked check.** For the heat equation $u_t = \kappa u_{xx}$ with independent
variables $(x,t)$, the principal part is $-1\cdot u_{xx} + 0\cdot u_{xt} +
0\cdot u_{tt}$, so $A = -1$, $B = 0$, $C = 0$ and $\Delta = 0 - 0 = 0$:
parabolic, as claimed. For Laplace's equation $u_{xx} + u_{yy} = 0$, $A = C = 1$
and $B = 0$, so $\Delta = -1 < 0$: elliptic. For the wave equation
$A = -c^2$, $B = 0$, $C = 1$, so $\Delta = +c^2 > 0$: hyperbolic. All three are
confirmed by the demonstration in Section 7.

### 3.3 An important caveat

The discriminant classifies the *principal part as a quadratic form*. It says
nothing about whether the equation is a good model, or whether the
coefficients are physically admissible. A diffusivity $\kappa < 0$ is still
"parabolic" and backwards in time, and the resulting problem is catastrophically
ill posed — the subject of [01-09-07](./07-boundary-value-problems.md). Always
check the sign of the physical coefficient, not just the discriminant.

## 4. The three families as geophysical measurements

### 4.1 Elliptic: potential fields and steady flow

$$\nabla^2 V = 0 \ \text{outside sources}, \qquad
\nabla^2 V = -4\pi G\rho \ \text{inside a mass}.$$

The same equation, with different names for the potential, describes the
magnetic potential outside a magnetised body, the electric potential in a DC
resistivity survey, self-potential, and the hydraulic head in steady
groundwater flow, $\nabla\cdot(K\nabla h) = 0$. No time appears. The field at
every point is determined by the boundary and by the source distribution at the
same instant.

The consequences for measurement are severe and worth naming:

- **No arrival times.** There is no travel time to measure, so there is no
  tomographic-style constraint. The data are amplitudes of a field sampled on a
  surface.
- **Smoothing with distance.** The field above a source is an average over a
  growing region; deeper or smaller bodies are exponentially less evident.
- **Non-uniqueness.** Because the solution is determined by boundary data, and
  because many source distributions share the same exterior harmonic field,
  the inverse problem has a null space. Two equivalence classes are exhibited
  numerically in [01-09-04](./04-laplace-poisson.md).

### 4.2 Parabolic: everything that diffuses

$$\frac{\partial u}{\partial t} = \kappa \nabla^2 u .$$

The equation has one time derivative and two space derivatives, so it treats
time differently from space: it is not symmetric under $t\to-t$. This
arrow of time is physical — heat flows from hot to cold — and it is why the
problem needs an initial condition *and* boundary conditions, but only for
$t > 0$.

Four geophysical problems are governed by this one equation, as
[01-09-02](./02-heat-equation.md) develops in detail: heat flow and
palaeoclimate, pore-pressure diffusion and induced seismicity, groundwater and
aquifer response, and electromagnetic induction with its skin depth. In every
case the diagnostic number is the diffusive timescale
$\tau \sim L^2/\kappa$, not a velocity.

### 4.3 Hyperbolic: everything that propagates

$$\frac{\partial^2 u}{\partial t^2} = c^2 \nabla^2 u .$$

Two time derivatives, and an exact symmetry under $t \to -t$: the equation is
reversible, so propagation is not a one-way process. Data are needed on a
space-like surface (an initial displacement *and* an initial velocity), and
information travels at exactly $c$ along the characteristics. Seismic P and S
waves in an isotropic elastic solid, acoustic waves in a borehole fluid, GPR in
a low-loss dielectric, and the normal modes of the whole Earth all obey this
form, as developed in [01-09-03](./03-wave-equation.md).

### 4.4 One rock, two equations: why the class depends on the experiment

The electromagnetic example settles any doubt that the classification is
bookkeeping. The full Maxwell system is hyperbolic: in vacuum, light propagates.
Inside a conductor, the displacement current is negligible compared with the
conduction current and the field is governed instead by

$$\nabla^2 \mathbf{E} = \mu\sigma \frac{\partial \mathbf{E}}{\partial t}
\quad\text{— a diffusion equation},$$

discussed in the earthquake and geophysics literature as the skin-depth equation
and derived from the vector identities in
[01-06-07](../06-multivariable-calculus/07-vector-identities.md). The
dimensionless number that decides which regime applies is $\sigma/(\omega
\epsilon)$:

| Regime | Condition | Equation | Geophysical method |
|---|---|---|---|
| Propagation | $\sigma \ll \omega\epsilon$ | hyperbolic | ground-penetrating radar in dry sand or ice |
| Diffusion | $\sigma \gg \omega\epsilon$ | parabolic | magnetotellurics, transient EM, airborne EM |

So **the same limestone is a wave medium for a 100 MHz radar pulse and a
diffusive medium for a 1 Hz magnetotelluric sounding.** The classification is a
property of the equation, and the equation is a property of the experiment as
much as of the rock. This single example is the best answer to the question
"why does geophysics need three different equations?"

## 5. What each class predicts before you solve anything

The table below is the practical payoff. It is what lets you read an abstract
and know what kind of data are inside it.

| Property | Elliptic | Parabolic | Hyperbolic |
|---|---|---|---|
| Principal part sign | $\Delta < 0$ | $\Delta = 0$ | $\Delta > 0$ |
| Characteristics | none real | one family | two families |
| Required data | boundary | initial + boundary | initial + boundary, on a space-like surface |
| Time-reversible? | no time | no | yes |
| Disturbance spread | instant, global | infinite speed, decaying | finite speed $c$ |
| Typical diagnostic scale | none (no length scale in the operator) | $\tau \sim L^2/\kappa$ | $L = ct$ |
| Smoothing in time? | n/a | strong | none (energy conserved) |
| Numerical method | large linear system, O($N^2$) iterations for a relaxation | implicit or stabilised explicit time step | explicit time step with CFL limit |
| Inverse problem character | non-unique without prior information | non-unique, strongly smoothed | better conditioned; travel times are informative |

Two of these rows are worth pausing over, because they are where students lose
marks in real work.

**Infinite propagation speed for the diffusion equation.** Suppose a compactly
supported initial heat pulse. The exact solution is nonzero at *every* point for
any $t > 0$, so the mathematical propagation speed is infinite. The amplitude
outside the original support decays like $\exp(-L^2/4\kappa t)$, so it is
unobservable in practice, but it is not zero, and a code that assumes compact
support will be wrong in the last digits. The demonstration in Section 7
measures the leakage directly: for a compact pulse on a grid, the largest value
outside the original support grows from $6.1\times10^{-6}$ after one step to
$7.7\times10^{-2}$ after fifty. Set against that, the wave equation gives
*exactly* zero outside the cone. Parabolic means no light cone; hyperbolic means
a light cone. Nothing else in the classification matters as much as that.

**The cost of an elliptic solve.** An elliptic problem has no preferred
direction, so every interior value depends on every boundary value. Discretised,
it becomes a linear system whose relaxation count grows like $N^2$ (or $N$ with
an optimal over-relaxation factor, as Section 7 measures). The
steady-state problem is therefore an algebra problem, not a time march — which
is exactly why gravity and magnetic modelling codes are built around linear
solvers.

## 6. Well-posedness: the question the classification does not answer

A problem is **well posed in the sense of Hadamard** when

1. a solution exists,
2. the solution is unique, and
3. the solution depends continuously on the data.

Classification is necessary but not sufficient for well-posedness. Two examples
make the distinction concrete in later lessons:

- the **backward heat equation** is parabolic, and grossly ill posed:
  [01-09-07](./07-boundary-value-problems.md) measures a noise mode amplified by
  $5.3\times10^{85}$ for a modest wavenumber;
- the **Dirichlet problem for Laplace's equation** is elliptic and well posed:
  [01-09-04](./04-laplace-poisson.md) proves uniqueness and demonstrates that
  two different numerical starting guesses converge to the same discrete field
  to $7\times10^{-11}$.

The classification tells you what the equation *is*. Well-posedness tells you
whether the problem you have posed with it is *answerable*. Both questions must
be asked, and [01-09-08](./08-weak-solutions.md) builds the weak formulation that
answers them for the equations that geophysics actually uses, where the
coefficients jump across layer boundaries and the sources are delta functions.

## 7. Python demonstration

The script `code/pde_classification.py` (provided in this module) does two
things: it classifies the canonical equations from their coefficients, and it
then solves one member of each class and measures the error against an exact
solution, so that the classification is tied to observed behaviour.

Classification is four lines:

```python
def classify(a: float, b: float, c: float) -> tuple[str, float]:
    """Return (class, discriminant) for A u_xx + 2B u_xy + C u_yy = 0."""
    disc = b * b - a * c
    if disc < 0.0:
        return "elliptic", disc
    if disc > 0.0:
        return "hyperbolic", disc
    return "parabolic", disc
```

Applied to the canonical equations, with the independent variables taken as the
pair in which the equation is posed:

```text
equation                              A    B    C      D  class
----------------------------------------------------------------------
Laplace    u_xx + u_yy = 0          1.0  0.0  1.0   -1.0  elliptic
Heat       u_t = k u_xx             1.0  0.0  0.0    0.0  parabolic
Wave       u_tt = c^2 u_xx         -1.0  0.0  1.0    1.0  hyperbolic
Degenerate u_xx + 2u_xy + u_yy = 0  1.0  1.0  1.0    0.0  parabolic
Tricomi     u_xx - x u_yy = 0 (x>0)  1.0  0.0 -1.0    1.0  hyperbolic
```

Note the second-to-last row: $u_{xx} + 2u_{xy} + u_{yy} = 0$ is
$(\partial_x + \partial_y)^2 u = 0$, degenerate on the single characteristic
family $y - x = \text{const}$, and correctly reported parabolic. The first-order
equation $u_t + c u_x = 0$ has no principal part and is **not classified by
$\Delta$ at all**; it is handled by characteristics in
[01-09-06](./06-characteristics.md).

The three classes then behave differently, measurably:

**Parabolic.** For $u_t = u_{xx}$ on $(0,1)$ with $u(0)=u(1)=0$ and
$u(x,0)=\sin\pi x$, the exact solution is $\mathrm{e}^{-\pi^2t}\sin\pi x$. An
explicit scheme with $\kappa\,\Delta t/\Delta x^2 = 0.4$ gives

```text
    N  r = k dt/dx^2     max error   order
   10         0.3781     2.604e-03        
   20         0.3938     7.662e-04    1.77
   40         0.3983     2.049e-04    1.90
   80         0.3996     5.278e-05    1.96
  160         0.3999     1.338e-05    1.98
```

Second-order convergence, and the error decays as the grid refines.

**Hyperbolic.** For $u_{tt} = u_{xx}$ with the same boundary data and a standing
wave initial condition $u(x,0)=\sin\pi x$, exact solution $\sin\pi x\cos\pi t$:

```text
    N     CFL     max error   order
   10   0.458     1.476e-03        
   20   0.525     3.741e-04    1.98
   40   0.512     1.001e-04    1.90
   80   0.506     2.588e-05    1.95
  160   0.503     6.580e-06    1.98
```

Second-order convergence here too, but for a different reason: the leapfrog
stencil is second order in both $\Delta x$ and $\Delta t$, and holding the
Courant number fixed refines both. That is not the case for the parabolic
scheme, where $\Delta t\sim\Delta x^2$ is forced by stability.

**The light cone.** Setting a compact pulse in motion and asking for the
numerical support:

```text
  steps                = 120,  t = 0.200000,  c t = 0.200000
  cell dx              = 0.001667   (= c dt, Courant number 1)
  predicted support    = [0.460000, 0.540000]
  numerical support    = [0.461667, 0.538333]
  max error vs exact   = 6.439e-15   (round-off level)
  max |u| beyond cone  = 0.000e+00   (exactly zero)
```

At Courant number 1 the stencil lies exactly on the characteristics, so the
translation is reproduced to round-off and the solution is *identically* zero
outside the cone. Nothing like this happens for the diffusion equation, where
the same experiment leaks $6.1\times10^{-6}$ after a single step.

**Elliptic.** Poisson's equation solved by Jacobi relaxation shows the cost of
globality:

```text
    N        dx  iterations    max error   iters*N^2
   10    0.0909         369    6.755e-03       3.690
   20    0.0476        1241    1.861e-03       3.103
   40    0.0244        4286    4.857e-04       2.679
```

The accuracy improves with refinement, but the iteration count grows like $N^2$:
every unknown is coupled to every other, exactly as the absence of
characteristics requires.

> **Breaking exercise.** Change the wave demonstration to Courant number 1.01
> and predict before running whether the error will grow linearly or
> exponentially in the step count. Then run it: the observed growth per step is
> $1.332$ against the von Neumann prediction $1.327$, an exponential
> instability, not a degrade-in-accuracy. The CFL argument is the topic of
> [01-09-03](./03-wave-equation.md).

## 8. Common mistakes

1. **Dropping the factor 2 on $B$.** Writing the principal part as $Au_{xx} +
   Bu_{xy} + Cu_{yy}$ and then testing $B^2 - 4AC$ gives the right answer only
   by accident of matching the other convention. Write $2B$ and test
   $B^2 - AC$, or write $B$ and test $B^2 - 4AC$; never mix them.
2. **Classifying the whole equation instead of the principal part.** The
   lower-order terms $D u_x + Eu_y + Fu$ never change the class. A diffusion
   equation with a source, a sink and advection is still a diffusion equation.
3. **Forgetting that the coefficients may vary.** With $A$, $B$, $C$ functions
   of position the class can change across the domain — the standard example is
   a flow that is subsonic in one region and supersonic in another.
4. **Assuming a hyperbolic equation always has a classical solution.** For
   nonlinear conservation laws the characteristics cross and the classical
   solution ceases to exist; [01-09-06](./06-characteristics.md) measures the
   gradient of $u_t + u u_x = 0$ diverging as $1/(1-t)$. A weak solution is
   required, which is where [01-09-08](./08-weak-solutions.md) begins.
5. **Believing that "no characteristics" means "no propagation".** Elliptic
   problems have no real characteristics, yet the field above a body is entirely
   determined by it. The absence of characteristics means the absence of a
   *preferred direction*, not the absence of information.
6. **Treating the diffusion equation as a wave equation with a velocity.**
   There is no velocity. Quoting "the heat took 10 Myr to travel 100 km" is a
   statement about $\tau \sim L^2/\kappa$; the word "travel" is a metaphor, and
   using it in a paper invites a referee's objection.
7. **Choosing the numerics from habit rather than from the class.** An explicit
   scheme for an elliptic problem does not converge faster with more steps; it
   converges to the solution of a different problem. An implicit scheme for a
   wave equation destroys the finite propagation speed that the data measure.

## 9. Real-world applications

- **Gravity and magnetic interpretation.** Elliptic: the field is a smoothed,
  non-unique functional of the source. Every "depth to source" estimate carries
  an assumed model class, which is why the same anomaly supports several
  published depths and the disagreement is not a mistake by one author.
- **Basin thermal history.** Parabolic: the thermal timescale
  $\tau \sim L^2/\kappa$ with $\kappa \approx 10^{-6}\ \mathrm{m^2\,s^{-1}}$
  gives 317 Myr for $L = 100$ km, so a thick lithosphere cannot have reached
  steady state within its own age and palaeoclimate reconstructions must solve
  the time-dependent problem, not the steady one.
- **Induced seismicity.** Parabolic: pore-pressure fronts inferred from
  triggered-event delays imply hydraulic diffusivities in a range that is
  debated; [01-09-02](./02-heat-equation.md) shows which permeability and
  storage values would be required for a one-year delay at 5 km, and why those
  values are uncomfortably high for intact rock.
- **Magnetotellurics versus GPR.** Same physics, different class. The skin depth
  $\delta = \sqrt{1/(\pi f \mu_0 \sigma)}$ sets the depth of investigation for
  the diffusive regime; the propagation velocity and the dielectric permittivity
  set it for the wave regime. A survey designed without knowing which regime
  applies will be misinterpreted.
- **Numerical modelling.** Every modelling code inherits its stability
  properties from the class: CFL-limited explicit time stepping for wave
  propagation, implicit or stabilised schemes for diffusion, and linear solvers
  for steady state. Choosing the wrong family is the most expensive mistake in
  the subject, because it is discovered after the run.
- **Global seismology.** Hyperbolic with a twist: the Earth is anelastic and
  heterogeneous, so the equation is hyperbolic to leading order and weakly
  dispersive and attenuating beyond it. Normal modes, ray theory and the
  eikonal equation all descend from the hyperbolic parent.

## 10. Further reading

- **Courant, R., & Hilbert, D. (1962). *Methods of Mathematical Physics*, Vol.
  II. Interscience.** Level: graduate. The classical account of classification,
  characteristics and canonical forms; still the source most other books follow.
- **John, F. (1991). *Partial Differential Equations* (4th ed.).
  Springer.** Level: advanced undergraduate to graduate. Concise, rigorous, and
  unusually good on the classification and on the Cauchy problem.
- **Evans, L. C. (2010). *Partial Differential Equations* (2nd ed.). AMS.**
  Level: graduate. The modern reference. Chapter 2 is the classification and the
  four canonical equations; later chapters build the weak theory that
  [01-09-08](./08-weak-solutions.md) introduces.
- **Farlow, S. J. (1993). *Partial Differential Equations for Scientists and
  Engineers*. Dover.** Level: intermediate. The most accessible treatment of
  classification with worked examples, if you want practice rather than proofs.
- **Hadamard, J. (1923). *Lectures on Cauchy's Problem in Linear Partial
  Differential Equations*. Yale University Press.** Level: graduate. The origin
  of the notion of a well-posed problem used in Section 6.

> Note on citations: bibliographic details are given so you can locate the works.
> This repository does not host or reproduce copyrighted text; confirm current
> editions and availability through your library before citing.

## 11. Exercises

Attempt them closed-book. Solutions are in
[`exercises/01-classification-solutions.md`](./exercises/01-classification-solutions.md).

**★1.** Classify each equation, stating the principal part and the
discriminant: (a) $u_{xx} + 4u_{xy} + 4u_{yy} = 0$; (b) $u_{xx} + u_{xy} +
u_{yy} = 0$; (c) $u_{xx} - 4u_{yy} = 0$; (d) $3u_{xx} + 2u_{xy} + 3u_{yy} = 0$.

**★2.** State which data each of the following problems requires, and why:
(a) $u_t = \kappa u_{xx}$ on $0<x<1$, $t>0$; (b) $\nabla^2 V = 0$ in a region;
(c) $u_{tt} = c^2u_{xx}$ on $0<x<1$, $t>0$.

**★3.** For the convection-diffusion equation $u_t + v u_x = \kappa u_{xx}$,
classify it when (a) $\kappa = 0$, (b) $v = 0$, (c) both nonzero. Which
geophysical process is described in each case?

**★4.** Show that $u_{xx} + 2u_{xy} + u_{yy} = 0$ has the single characteristic
family $y - x = \mathrm{const}$ and find its general solution by introducing
$\xi = y - x$, $\eta = y$.

**★★5.** Derive the characteristic equation (3) by the argument of Section 3.1
completed: write $u$ as a function of $\xi$ and $\eta$ with a change of
variables that makes $u_\xi$ the derivative along the curve, and show that the
coefficient of $u_{\xi\xi}$ vanishes exactly when (3) holds.

**★★6.** The electromagnetic skin depth in a conductor is
$\delta = \sqrt{2/(\omega\mu\sigma)}$. For a rock of conductivity
$\sigma = 0.01\ \mathrm{S\,m^{-1}}$ at $f = 1$ Hz, compute $\delta$ using
$\mu = \mu_0 = 4\pi\times10^{-7}$ (state units), then decide whether a
100 MHz GPR pulse in the same rock is better described by the wave equation or
by the diffusion equation, given a relative permittivity of 6 (assume
$\mu = \mu_0$). State the criterion you used.

**★★7.** An equation has principal part $A u_{xx} + 2Bu_{xy} + Cu_{yy}$ with
$A = 1$, $B = x$, $C = 1 - y$. Find the regions of the $(x,y)$ plane in which
it is elliptic, parabolic and hyperbolic, and sketch the dividing curves.

**★★8.** The heat equation is parabolic. Explain why replacing
$\partial u/\partial t$ by $\partial^2 u/\partial t^2 + \alpha\partial
u/\partial t$ (a telegraph/viscoelastic-like modification, with $\alpha > 0$)
changes the class, and compute the discriminant to show for which $\alpha$ the
change occurs. Which physical process does the modified equation describe?

**★★★9.** Design a numerical experiment that distinguishes elliptic, parabolic
and hyperbolic behaviour using *only* the response to a localised disturbance at
a single interior point. Specify the diagnostic you would measure, the expected
scaling of that diagnostic with grid spacing for each class, and how you would
falsify the classification. Report the experiment you ran, with numbers, and the
limits of your conclusion.

**★★★10.** A paper reports that a magnetic anomaly can be explained either by
a magnetised body at 4 km depth or by a larger, less magnetised body at 8 km.
Using only the classification of the governing equation and the properties of
harmonic functions, write a critique of the claim that one of the two must be
"wrong". State what additional data would break the tie. (You do not need to
model the anomaly; argue from the equation.)

## 12. Self-assessment checklist

- [ ] I can compute the discriminant of a second-order linear operator and name
      the class, including the factor-of-2 convention.
- [ ] I can state which data each class requires, and derive the requirement
      from the characteristic equation rather than from memory.
- [ ] I can give at least three geophysical examples of each class, with the
      name of a real method for each.
- [ ] I can explain why the same rock is a wave medium for radar and a diffusive
      medium for magnetotellurics, including the criterion in terms of
      $\sigma/(\omega\epsilon)$.
- [ ] I can predict, from the class alone, whether a compact disturbance
      produces an exactly zero region (a cone) or a small nonzero tail.
- [ ] I can explain why an elliptic discretisation needs a linear solver whereas
      a hyperbolic one needs a Courant-limited time step.
- [ ] I can state Hadamard's three conditions and give one parabolic example
      that fails them (the backward heat equation).

## Related lessons

- [01-09-02 The Diffusion/Heat Equation and Diffusive Timescales](./02-heat-equation.md)
  — the parabolic class developed with the four geophysical subdisciplines and
  the derivation of $\tau \sim L^2/\kappa$.
- [01-09-03 The Wave Equation and Its Physical Content](./03-wave-equation.md) —
  the hyperbolic class, d'Alembert's solution, characteristics and the CFL
  condition.
- [01-09-04 Laplace and Poisson Equations in Earth Systems](./04-laplace-poisson.md)
  — the elliptic class, harmonic functions, uniqueness, and why uniqueness does
  not make inversion unique.
- [01-09-06 Method of Characteristics and First-Order PDEs](./06-characteristics.md)
  — first-order equations, which this lesson deliberately leaves unclassified.
- [01-06-08 Potential Fields, Laplace and Poisson Equations](../06-multivariable-calculus/08-potential-theory.md)
  — the prerequisite treatment of the elliptic prototype.
- [02-physics Physics for Geophysics](../../02-physics/README.md) — the physical
  derivations that supply $c$, $\kappa$ and the boundary conditions.
