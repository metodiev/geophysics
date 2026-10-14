---
id: 01-06-01
title: "Partial Derivatives, Gradients and Directional Derivatives"
level: intermediate
prereqs: ["01-05-02", "01-05-03", "01-05-04", "01-07-01"]
estimated_minutes: 90
tags: [multivariable-calculus, gradient, partial-derivatives, potential-fields]
---

# Partial Derivatives, Gradients and Directional Derivatives

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** partial derivatives from the limit definition and from the rules
   of single-variable calculus applied one variable at a time.
2. **Define** the gradient as a vector, and explain why the gradient is a
   physical object while the individual partial derivatives are not.
3. **Derive** the result that the directional derivative in a unit direction
   $\hat{u}$ is $\nabla f \cdot \hat{u}$, and deduce from it both the direction
   and the magnitude of steepest ascent.
4. **Use** the total differential as a first-order model, and apply it to
   linearisation, sensitivity analysis and uncertainty propagation.
5. **Obtain** a physical field as the gradient of a potential, with the sign
   convention stated explicitly and checked numerically.
6. **Recognise** the three ways the gradient fails: insufficient
   differentiability, coordinate singularities, and confusion between the
   partial derivative in a chosen coordinate system and the physical
   derivative along a direction.

## Prerequisites

- [01-05-02 Derivatives and Rates of Change](../05-single-variable-calculus/02-derivatives.md)
  and [01-05-03 Differentiation Rules and Implicit Differentiation](../05-single-variable-calculus/03-differentiation-rules.md)
  — everything here is those rules applied one variable at a time.
- [01-05-04 Taylor Series, Linearisation and Small-Angle Approximations](../05-single-variable-calculus/04-taylor-series.md)
  — the total differential is the multivariate Taylor expansion truncated at
  first order.
- [01-07-01 Vectors, Vector Spaces and Basis](../07-linear-algebra/01-vectors-and-spaces.md)
  — the gradient is a vector, and the dot product is how it is used.
- [01-04 Floating-Point Representation, Round-Off and Catastrophic Cancellation](../01-arithmetic/04-floating-point.md)
  — Section 6 of this lesson measures a derivative numerically, and the
  round-off floor comes straight from that lesson.

## 1. Intuition: the Earth is a function of three variables

Almost every quantity a geophysicist measures is a function of position. Write
it $f(x, y, z)$. It is a **scalar field**: one number at each point of space.

| Scalar field | What its gradient gives you | Governing relation |
|---|---|---|
| Temperature $T$ in the crust | Direction and rate of conductive heat flow | $\mathbf{q} = -k \nabla T$ (Fourier) |
| Hydraulic head $h$ in an aquifer | Direction and rate of groundwater flow | $\mathbf{v} = -\frac{k}{\mu}(\nabla p - \rho \mathbf{g})$ (Darcy) |
| Gravitational potential $V$ | The gravitational acceleration vector | $\mathbf{g} = \nabla V$ (convention, Section 5) |
| Magnetic scalar potential $V_m$ outside sources | The magnetic field | $\mathbf{H} = -\nabla V_m$ |
| First-arrival travel time $T$ from a source | Ray direction; magnitude gives slowness | $\lvert \nabla T \rvert = 1/v$ (eikonal) |
| Elevation $z(x,y)$ over a survey | Slope and aspect, the steepest uphill direction | $\lvert \nabla z \rvert = \tan(\text{slope})$ |

The pattern is not a coincidence and it is not a set of analogies. In every row
the gradient of a *potential* or a *field* is the physically meaningful vector,
and the physical law relating them is a gradient. This is why the gradient is
the first operator to learn properly, and why the rest of this module is largely
about the second-order operators built from it.

There is one hazard to state at the outset. **A partial derivative is not a
physical quantity on its own.** The number $\partial f/\partial x$ depends on
which direction you chose to call $x$. Rotate the survey grid and
$\partial f/\partial x$ changes. The gradient, by contrast, does not change: it
is the same arrow, expressed in whatever basis you prefer. Distinguishing the
coordinate artefact from the physical object is the main conceptual work of this
lesson.

## 2. Precise definitions

### 2.1 Partial derivative

Let $f$ be defined on an open set containing $\mathbf{p} = (x_0, y_0, z_0)$. The
**partial derivative with respect to $x$** at $\mathbf{p}$ is

$$\frac{\partial f}{\partial x}(\mathbf{p})
= \lim_{h \to 0} \frac{f(x_0 + h,\, y_0,\, z_0) - f(x_0,\, y_0,\, z_0)}{h}.$$

Every other variable is held fixed. Because that is all it is, the
single-variable rules apply verbatim: to differentiate $f = x^2 y + y z^3$ with
respect to $x$, treat $y$ and $z$ as constants and get $2xy$.

### 2.2 Higher-order partial derivatives and the symmetry theorem

Repeated differentiation gives $\partial^2 f/\partial x \partial y$ and so on.
The order in which the differentiations are performed does not matter, provided
the second partials are continuous:

$$\frac{\partial^2 f}{\partial x \partial y}
= \frac{\partial^2 f}{\partial y \partial x}
\qquad\text{(Clairaut--Schwarz theorem, for } C^2 \text{ functions).}$$

This is not a triviality: it is the reason the **Hessian matrix** of second
derivatives is symmetric, and therefore the reason gravity gradient tensors are
symmetric and have real eigenvalues. The theorem fails if the second partials
are merely required to exist pointwise. Since the physical fields in this
curriculum are smooth away from sources, the theorem applies where they are
defined.

### 2.3 The gradient

The **gradient** of $f$ is the vector of its partial derivatives,

$$\nabla f = \left( \frac{\partial f}{\partial x},\;
\frac{\partial f}{\partial y},\; \frac{\partial f}{\partial z} \right).$$

The symbol $\nabla$ ("del") is an operator, not a number: it acts on whatever
follows it to produce a vector. Note carefully what is and is not claimed. The
formula above is written in Cartesian coordinates. In another coordinate system
the same vector has different components — for spherical coordinates,

$$\nabla f = \frac{\partial f}{\partial r}\,\hat{r}
+ \frac{1}{r}\frac{\partial f}{\partial \theta}\,\hat{\theta}
+ \frac{1}{r \sin\theta}\frac{\partial f}{\partial \phi}\,\hat{\phi},$$

and the two expressions describe the same arrow at the same point. The
$1/r$ and $1/(r\sin\theta)$ factors are not decoration: they correct for the
fact that a small change in $\theta$ is a small *distance* $r\,d\theta$.
[01-06-03](./03-jacobians.md) verifies this formula numerically.

### 2.4 Directional derivative

Take a unit vector $\hat{u}$ and move from $\mathbf{p}$ along the straight line
$\mathbf{p} + t\hat{u}$. The **directional derivative** is

$$D_{\hat{u}} f(\mathbf{p})
= \lim_{t \to 0} \frac{f(\mathbf{p} + t\hat{u}) - f(\mathbf{p})}{t}.$$

This is the physical derivative: how fast $f$ changes per metre travelled in a
stated direction. It is coordinate-free.

### 2.5 The total differential

For a differentiable $f$, a small displacement
$d\mathbf{r} = (dx, dy, dz)$ produces the change

$$df = \frac{\partial f}{\partial x}\,dx
+ \frac{\partial f}{\partial y}\,dy
+ \frac{\partial f}{\partial z}\,dz = \nabla f \cdot d\mathbf{r}.$$

The first equality is the definition; the second is the compact statement that
the total differential is the gradient contracted with the displacement. This is
the multivariate first-order Taylor expansion and it is the workhorse of
sensitivity analysis.

### 2.6 Differentiability is stronger than having partial derivatives

It is tempting to assume that if all the partial derivatives exist then $f$ is
well behaved. It is not true. The standard counterexample is

$$f(x,y) = \frac{xy}{x^2 + y^2}\ \ (x,y) \neq (0,0), \qquad f(0,0) = 0.$$

Both partial derivatives exist at the origin and both equal $0$, because $f$
vanishes along both axes. Yet $f$ is not even continuous at the origin: along
the line $y = x$ it equals $1/2$ at every nonzero point. A function whose
gradient exists but which jumps cannot have a meaningful directional derivative
in the direction $(1,1)/\sqrt{2}$.

The correct sufficient condition is: if the partial derivatives exist and are
**continuous** in a neighbourhood (a $C^1$ function), then $f$ is differentiable
and the formulas of this lesson hold. This matters physically because the
potentials of this curriculum are $C^1$ everywhere except at the sources
themselves, and it is exactly at the sources that integral theorems will have to
do work that pointwise differentiation cannot (Lesson 06).

## 3. Derivations

### 3.1 The directional derivative is $\nabla f \cdot \hat{u}$

Let $\hat{u} = (u_1, u_2, u_3)$ be a unit vector and define the composite
function of one variable $g(t) = f(\mathbf{p} + t\hat{u})$. Then
$D_{\hat{u}} f(\mathbf{p}) = g'(0)$.

Apply the multivariate chain rule. With $x(t) = x_0 + t u_1$ and so on,
$dx/dt = u_1$, and

$$g'(t) = \frac{\partial f}{\partial x}\frac{dx}{dt}
+ \frac{\partial f}{\partial y}\frac{dy}{dt}
+ \frac{\partial f}{\partial z}\frac{dz}{dt}
= \nabla f \cdot \hat{u}.$$

Setting $t = 0$:

$$\boxed{\,D_{\hat{u}} f = \nabla f \cdot \hat{u}\,}$$

Two consequences follow immediately and both are used constantly.

**(a) The direction of steepest ascent.** Since $\hat{u}$ is a unit vector,

$$D_{\hat{u}} f = \lvert \nabla f \rvert \cos\psi,$$

where $\psi$ is the angle between $\nabla f$ and $\hat{u}$. This is maximised by
$\cos\psi = 1$, that is by $\hat{u}$ parallel to $\nabla f$. Hence:

> **The gradient points in the direction of greatest increase of $f$, and its
> magnitude is the rate of increase in that direction.**

Physically: heat flows *down* the temperature gradient, water flows *down* the
head gradient, and the field of a mass points *down* its potential — with the
sign depending on the convention you chose for the potential.

**(b) The gradient is perpendicular to level surfaces.** Set $f(\mathbf{p}) = c$
and let $\mathbf{r}(s)$ be any curve lying in that level set. Then
$f(\mathbf{r}(s)) = c$ identically, so

$$0 = \frac{d}{ds} f(\mathbf{r}(s)) = \nabla f \cdot \mathbf{r}'(s).$$

Since $\mathbf{r}'(s)$ is an arbitrary tangent direction to the level surface,
$\nabla f$ is orthogonal to every one of them. In potential-field work this is
the statement that **field lines cross equipotential surfaces at right angles**,
which is why equipotential maps and field-line maps carry the same information.

### 3.2 The gradient of a radial function

A computation used repeatedly in gravity: for a function of the distance alone,
$f(\mathbf{r}) = F(r)$ with $r = \lvert \mathbf{r} \rvert$,

$$\nabla f = F'(r)\, \hat{r}, \qquad \hat{r} = \mathbf{r}/r .$$

*Derivation.* Compute $\partial r/\partial x = x/r$ from
$r^2 = x^2 + y^2 + z^2$, then apply the chain rule:
$\partial f/\partial x = F'(r)\,\partial r/\partial x = F'(r) x/r$. Collecting
the three components gives $F'(r)(x,y,z)/r = F'(r)\hat{r}$. $\square$

Applying this to $F(r) = 1/r$ gives the identity that the whole of potential
theory rests on:

$$\nabla\!\left(\frac{1}{r}\right) = -\frac{\hat{r}}{r^2}.$$

Its divergence, $\nabla \cdot (\hat{r}/r^2) = 4\pi \delta^3(\mathbf{r})$ away
from the origin, is the reason Laplace's equation needs a source term; Lesson 07
verifies that identity numerically.

### 3.3 The gradient of the gravitational potential

Adopt the convention used throughout this module and stated in full in
Section 4: the potential of a point mass $M$ at the origin is
$V(\mathbf{r}) = GM/r$, and the field is $\mathbf{g} = \nabla V$. Then by
Section 3.2,

$$\mathbf{g} = GM \nabla\!\left(\frac{1}{r}\right) = -\frac{GM}{r^2}\,\hat{r},$$

which has magnitude $GM/r^2$ and points toward the mass. That is Newtonian
gravitation, obtained as one line of the chain rule. The intermediate result
$\partial V/\partial z = -GM z/r^3$ is what a gravimeter measures, up to sign.

### 3.4 Linearisation, sensitivity and uncertainty

Write the first-order model of a quantity $q$ that depends on parameters
$(a_1, \dots, a_n)$ as $q = f(\mathbf{a})$. A small perturbation
$\delta\mathbf{a}$ produces

$$\delta q \approx \nabla f \cdot \delta \mathbf{a}
= \sum_i \frac{\partial f}{\partial a_i} \delta a_i .$$

Each $\partial f/\partial a_i$ is a **sensitivity**: the change in the observable
per unit change in the parameter. If the parameter errors are independent with
standard uncertainties $\sigma_i$, the first-order uncertainty in $q$ is

$$\sigma_q^2 \approx \sum_i \left( \frac{\partial f}{\partial a_i} \right)^2 \sigma_i^2 .$$

Two warnings that the formula itself does not carry. First, linearisation is
only valid while the perturbation is small compared with the scale on which $f$
curves; when it is not, the neglected second-order term is a *bias*, not noise.
Second, when the $a_i$ are correlated the cross terms do not vanish, and the
correct object is the Jacobian-transformed covariance matrix — the subject of
[01-06-03](./03-jacobians.md).

### 3.5 Worked example: how much does a station mislocation matter?

A compact body of mass $M$ sits at depth $d$ beneath the origin. A gravimeter
at horizontal position $(x,y)$ on the surface records the downward component

$$g_z(x,y) = \frac{GM d}{(x^2 + y^2 + d^2)^{3/2}} .$$

Differentiating with respect to $x$ (and using Section 3.2 on the radial
factor):

$$\frac{\partial g_z}{\partial x}
= -\frac{3 GM d x}{(x^2 + y^2 + d^2)^{5/2}} .$$

Take $M = 10^{11}$ kg, $d = 800$ m and put the station at $x = 400$ m,
$y = 0$. Then

$$g_z = \frac{6.674\times10^{-11} \times 10^{11} \times 800}{(400^2 + 800^2)^{3/2}}
= 7.462\times10^{-6}\ \mathrm{m\,s^{-2}} = 0.746\ \mathrm{mGal},$$

and

$$\frac{\partial g_z}{\partial x}
= -\frac{3 (6.674\times10^{-11})(10^{11})(800)(400)}
{(400^2+800^2)^{5/2}}
= -1.119\times10^{-8}\ \mathrm{s^{-2}}.$$

The partial derivative of a field with respect to a horizontal coordinate has
units of acceleration per metre, that is $\mathrm{s^{-2}}$. So a 10 m
horizontal position error produces an anomaly error of
$1.12\times10^{-7}\ \mathrm{m\,s^{-2}} = 0.011$ mGal — comparable to or larger
than the repeatability quoted for modern relative gravimeters. That is why
station coordinates, not instrument precision, often limit a microgravity
survey. The arithmetic is linearised: it is trustworthy because $\delta x = 10$ m
is small compared with the 800 m length scale of the anomaly.

## 4. Physical interpretation

**The gradient converts a potential into a field.** Everything in gravity,
magnetics, self-potential and (in a modified sense) heat flow is read this way.
The sign convention is the single most common source of error in the literature,
so state it every time.

| Potential defined as | Field from it | Poisson equation |
|---|---|---|
| $V = G\int \rho / D \, dV'$ (gravity, geodesy) | $\mathbf{g} = \nabla V$ | $\nabla^2 V = -4\pi G \rho$ |
| $\Phi = -G\int \rho / D \, dV'$ (physics) | $\mathbf{g} = -\nabla \Phi$ | $\nabla^2 \Phi = +4\pi G \rho$ |
| $V_m$ with $\mathbf{H} = -\nabla V_m$ (magnetics) | $\mathbf{H} = -\nabla V_m$ | $\nabla^2 V_m = \nabla \cdot \mathbf{M}$ |

Here $D = \lvert \mathbf{r} - \mathbf{r}' \rvert$. The two gravity rows describe
identical physics: $V = -\Phi$. Mixing them produces an apparent sign error in
the field, and nothing in the data will tell you which convention the previous
author used. In magnetics the sign differs again because the potential is
defined to give the field with a minus sign. **Write the convention down before
using any formula.** The remainder of this module uses the first row.

**The gradient is a flux driver, and a pressure gradient is not a force.** In
Darcy's law as written in Section 1, the flow is driven by the *combination* of
a pressure gradient and the gravitational body force. In a hydrostatic column
the two cancel exactly and nothing flows even though the pressure gradient is
large. A student who reads a pressure gradient as "the driving force" will
predict flow in a static aquifer.

**Where the gradient does not exist.** Three situations recur.

1. **At a source.** The potential of a point mass has a genuine singularity at
   the mass; the potential of a surface distribution is finite but its gradient
   is discontinuous across the surface. This is not a pathology to be
   normalised away. It is the physical content of Poisson's equation, and it is
   why the integral theorems of Lesson 06 are needed to relate fields to
   sources.
2. **At a coordinate singularity.** On the polar axis, $\hat{\theta}$ and
   $\hat{\phi}$ are undefined and the formula in Section 2.3 breaks down, even
   though the physical gradient is perfectly well defined. The same occurs at
   the centre of a spherical grid and on a map projection's standard point.
3. **When the surface is not differentiable.** A topographic surface digitised
   from a DEM is not differentiable anywhere. $\lvert \nabla z \rvert$ is then
   a finite-difference estimate of slope with an error you must control, not a
   derivative. Every slope map in GIS is this computation, and the choice of
   stencil is a modelling decision.

## 5. Python demonstration

The companion script
[`code/gradient_and_field.py`](./code/gradient_and_field.py) computes every
claim above numerically. It uses only the standard library, so no environment is
required beyond Python itself.

```python
# Central differences, and the gradient of a potential, from the demo script.
def grad_central(f, p, h):
    x, y, z = p
    gx = (f(x + h, y, z) - f(x - h, y, z)) / (2.0 * h)
    gy = (f(x, y + h, z) - f(x, y - h, z)) / (2.0 * h)
    gz = (f(x, y, z + h) - f(x, y, z - h)) / (2.0 * h)
    return (gx, gy, gz)

mass = 1.0e11                      # kg, a synthetic compact body
p = (400.0, -300.0, 1200.0)        # observation point, |r| = 1300 m
r = norm(p)
analytic = tuple(-G * mass * c / r ** 3 for c in p)   # grad(GM/r)
```

Observed output of `python3 gradient_and_field.py` (synthetic masses
throughout):

```text
observation point          = (400.0, -300.0, 1200.0) m,  |r| = 1300.0 m
V at the point             = 5.133846e-03 m^2/s^2
numeric grad V   (h = 1 m) = (-1.215111e-06,  9.113329e-07, -3.645336e-06)
analytic grad V            = (-1.215112e-06,  9.113336e-07, -3.645335e-06)
relative error             = 4.541e-07
|grad V|                   = 3.949112e-06 m/s^2 = 0.3949 mGal
```

```text
central difference, step h:
   h =    10.0 m    relative error = 4.541e-05
   h =     1.0 m    relative error = 4.541e-07
   h =     0.1 m    relative error = 4.541e-09
   h =    0.01 m    relative error = 5.113e-11
   h =   0.001 m    relative error = 7.222e-11
forward difference dV/dx, h = 1 m: relative error = 8.942e-04
```

### What to observe, and why it matters

| Observation | Consequence for geophysics |
|---|---|
| Central-difference error falls by 100 per decade of $h$ | The stencil is second-order accurate: halving the grid spacing quarter the error, which is why finer surveys pay off quadratically |
| The error stops improving at $h = 0.01$ m and worsens at $0.001$ m | Round-off divides by $2h$: the two errors (truncation falling, round-off rising) cross over, and the best step is neither the smallest nor the largest. See [01-04 Floating Point](../01-arithmetic/04-floating-point.md) |
| Forward differences err by $8.9\times10^{-4}$ where central differences err by $4.5\times10^{-7}$ | The extra function evaluation buys two orders of accuracy; every practical derivative is a central or higher-order stencil |
| $\nabla V \cdot \hat{w} = 1.1\times10^{-22}$ for $\hat{w}$ tangent to the level sphere | Machine zero: the gradient really is normal to the equipotential |
| The central difference along $\hat{w}$ is exactly $0$, while $V$ changes by $-1.5\times10^{-5}$ over $t = 100$ m | The leading term vanishes; the change is purely second order, which is the quantitative version of "perpendicular" |

The script also verifies the eikonal relation $\lvert \nabla T \rvert = 1/v$ for
a homogeneous medium to a relative difference of $7.8\times10^{-10}$, and
computes the gravity gradient tensor of a point mass:

```text
g_z at the surface         = 1.042812e-05 m/s^2 = 1.0428 mGal
d2V/dz2 (numeric, 1 m grid)= 2.607035e-08 1/s^2
2*G*M/depth^3              = 2.607031e-08 1/s^2
T_zz = dg_z/dz (numeric)   = -2.607039e-08 1/s^2 = -26.0704 E
T_zz = -2*G*M/depth^3      = -2.607031e-08 1/s^2 = -26.0703 E
```

The second derivative of the potential is $+2GM/d^3$ and the vertical gradient
of the downward gravity field is $-2GM/d^3$; the sign difference is the survey
convention, and the magnitude is what a gravity gradiometer measures. The
Eötvös unit used above is $1\ \mathrm{E} = 10^{-9}\ \mathrm{s^{-2}}$.

> **Breaking exercise.** Change `h` in the demo to `1e-2` and `1e-5` and
> predict, before running, which of the two gives the smaller error. Then
> explain in one sentence why the answer is not "the smaller one".

## 6. Exercises

Ten graded exercises, with a route through the harder ones, are in
[`exercises/01-partial-derivatives-exercises.md`](./exercises/01-partial-derivatives-exercises.md);
worked solutions are in
[`exercises/01-partial-derivatives-solutions.md`](./exercises/01-partial-derivatives-solutions.md).
Attempt them closed-book. Several require you to run and modify the
demonstration, which is deliberate.

## 7. Common mistakes

1. **Treating $\partial f/\partial x$ as the rate of change "in the $x$
   direction" without saying which $x$.** In spherical coordinates the partial
   derivative with respect to $\theta$ is not a rate per metre; it is a rate per
   radian, and it must be divided by $r$ before it becomes one.
2. **Confusing the gradient with the total derivative of a time series.**
   $\partial T/\partial t$ at a fixed point (Eulerian) and $dT/dt$ following a
   moving fluid parcel (Lagrangian) differ by the advective term
   $\mathbf{v}\cdot\nabla T$. In heat-flow and mantle-convection problems this
   distinction is the whole physics.
3. **Assuming the gradient exists because the partials do.** Section 2.6 gives
   the counterexample, and real digitised surfaces are worse than the
   counterexample.
4. **Mixing sign conventions.** With $V = GM/r$ the field is $+\nabla V$; with
   $\Phi = -GM/r$ it is $-\nabla \Phi$. Getting this wrong flips every anomaly in
   an interpretation.
5. **Reading a pressure gradient as the flow driver.** In a static column the
   pressure gradient is balanced by gravity and no flow occurs.
6. **Propagating uncertainties with the first-order formula outside its range.**
   When the perturbation is comparable to the curvature scale of $f$, the
   neglected quadratic term biases the answer; the honest option is Monte Carlo,
   as in [01-06-03](./03-jacobians.md).
7. **Choosing the finite-difference step "as small as possible".** Section 5
   shows the error rising again below $h = 0.01$ m. The optimum is
   problem-dependent and should be measured, not assumed.

## 8. Real-world applications

- **Gravity and magnetic interpretation.** Every "field from a potential"
  relation in [07-gravity-geodesy](../../07-gravity-geodesy/README.md) and
  [08-geomagnetism-electromagnetism](../../08-geomagnetism-electromagnetism/README.md)
  is a gradient. The vertical derivative $\partial V/\partial z$ is what a
  gravimeter measures; the horizontal derivatives are what modern gradient
  surveys measure directly.
- **Gravity gradiometry.** Second derivatives of the potential — the components
  of the Hessian — separate the effect of shallow from deeper structure because
  the field of a compact source falls off as $r^{-3}$ in the gradient tensor
  rather than $r^{-2}$. The demo computes exactly this $-2GM/d^3$ result.
- **Seismic ray tracing.** The eikonal equation $\lvert \nabla T \rvert = 1/v$
  is a statement about the gradient of a travel-time field. Numerical solutions
  are finite-difference solutions of that partial differential equation, so
  eikonal solvers inherit the accuracy and round-off behaviour measured in
  Section 5.
- **Heat-flow and geothermal studies.** Conductive heat flux is
  $\mathbf{q} = -k\nabla T$. Taking an illustrative continental gradient of
  $25\ \mathrm{K\,km^{-1}}$ and $k = 2.5\ \mathrm{W\,m^{-1}\,K^{-1}}$ gives
  $q = 62.5\ \mathrm{mW\,m^{-2}}$, the right order for stable continental crust;
  real values vary substantially with geology and must be measured.
- **Hydrology.** Darcy's law is a gradient statement, and groundwater models
  solve for the head field whose gradient is the flow.
- **DEM and slope analysis.** Terrain slope and aspect are $\lvert \nabla z
  \rvert$ and the direction of $-\nabla z$; the finite-difference question of
  Section 5 is a routine GIS decision.
- **Uncertainty in station positioning.** Section 3.5 is the standard estimate:
  a 10 m station error contributes about 0.011 mGal in that geometry, which is
  comparable to the repeatability of modern relative gravimeters.

## 9. Further reading

- **Marsden, J. E., & Tromba, A. *Vector Calculus.* W. H. Freeman.** The
  standard rigorous undergraduate treatment; the chapters on partial
  derivatives, the gradient and differentiability cover Sections 2–3 at greater
  length. Level: intermediate. Check your library for the current edition.
- **Schey, H. M. *Div, Grad, Curl, and All That.* W. W. Norton.** An unusually
  readable account aimed at exactly the intuition in Section 4, with physical
  arguments rather than proofs. Level: beginner to intermediate.
- **Blakely, R. J. (1995). *Potential Theory in Gravity and Magnetic
  Applications.* Cambridge University Press.** Chapter 1 is the canonical
  treatment of the sign conventions and of the potential--field relations that
  Section 4 tabulates. Level: advanced. This is the standard reference for
  gravity and magnetic potential theory and is worth owning.
- **Telford, W. M., Geldart, L. P., & Sheriff, R. E. (1990). *Applied
  Geophysics* (2nd ed.). Cambridge University Press.** The applied counterpart:
  the same gradients used in survey practice and interpretation. Level:
  intermediate.
- **Turcotte, D. L., & Schubert, G. *Geodynamics.* Cambridge University
  Press.** Used here for the heat-flow and advection discussion in Sections 4
  and 7; any recent edition. Level: advanced.

> Note on citations: bibliographic details above are given so that you can
> locate the works. This repository does not host or reproduce copyrighted text,
> and you should confirm editions and current availability through your library
> before citing them yourself.

## 10. Related lessons

- [02 Multiple Integrals and Change of Variables](./02-multiple-integrals.md) —
  accumulates the quantity whose gradient this lesson differentiates.
- [03 Jacobians, Coordinate Transformations and Volume Elements](./03-jacobians.md) —
  the gradient formula in arbitrary coordinates, and the proper propagation of
  correlated uncertainty.
- [04 Divergence, Curl and Physical Meaning](./04-divergence-and-curl.md) — the
  other two first-order operators built from $\nabla$.
- [01-05-02 Derivatives and Rates of Change](../05-single-variable-calculus/02-derivatives.md)
  and [01-05-04 Taylor Series, Linearisation and Small-Angle Approximations](../05-single-variable-calculus/04-taylor-series.md)
  — the one-variable tools this lesson extends.
- [01-07-01 Vectors, Vector Spaces and Basis](../07-linear-algebra/01-vectors-and-spaces.md) —
  the algebra of the vectors produced here.
- [02-08-01 Newtonian Gravitational Potential and Field](../../02-physics/08-potential-theory/01-gravitational-potential.md) —
  the physics course's treatment of the same relations.
- [07-03-01 Interpreting Anomalies: Geometry, Depth and Amplitude Rules](../../07-gravity-geodesy/03-gravity-anomalies-and-modelling/01-anomaly-interpretation.md) —
  where the sensitivities of Section 3.5 become interpretation rules.

## Self-assessment checklist

Work through this without notes. If any item is not a clear "yes", reread the
section named beside it.

- [ ] I can compute a partial derivative from the limit definition and from the
      ordinary rules, and explain what "holding the others fixed" means
      geometrically. (Section 2.1)
- [ ] I can state the Clairaut--Schwarz theorem, its continuity hypothesis, and
      one physical consequence (symmetry of the Hessian). (Section 2.2)
- [ ] I can derive $D_{\hat{u}} f = \nabla f \cdot \hat{u}$ from the chain rule
      without looking it up. (Section 3.1)
- [ ] I can explain why the gradient is perpendicular to level surfaces, and say
      what that means for an equipotential map. (Section 3.1)
- [ ] I can convert between the two gravity sign conventions and say which one I
      am using. (Section 4)
- [ ] I can derive $\nabla(1/r) = -\hat{r}/r^2$ and explain why its divergence is
      a delta function. (Sections 3.2, 3.3)
- [ ] I can write down the first-order uncertainty formula and state the
      condition under which it fails. (Section 3.4)
- [ ] I can explain why the central-difference error rises again for very small
      steps, and estimate roughly where the optimum lies. (Section 5)
- [ ] I can compute $\lvert \nabla z \rvert$ for a topographic surface and say
      why the answer is not a derivative. (Section 4)
- [ ] I can give one geophysical example each of the gradient acting as a field
      relation, a flux law, and a ray-direction rule. (Section 1)
