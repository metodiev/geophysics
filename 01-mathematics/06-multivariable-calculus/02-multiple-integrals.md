---
id: 01-06-02
title: "Multiple Integrals and Change of Variables"
level: intermediate
prereqs: ["01-05-05", "01-06-01"]
estimated_minutes: 90
tags: [multivariable-calculus, integration, volume-elements, mass]
---

# Multiple Integrals and Change of Variables

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** the double and triple integral as a limit of Riemann sums over a
   region, and explain what quantity the sum represents physically.
2. **Evaluate** a multiple integral by iterating one-dimensional integrals, and
   justify the freedom to choose the order of iteration.
3. **Choose** the integration order that makes the limits of the inner integral
   simple, and explain why this choice is a modelling decision rather than a
   matter of taste.
4. **State and apply** the change-of-variables theorem, including the Jacobian
   determinant, and use the polar, cylindrical and spherical volume elements
   correctly.
5. **Compute** the mass, mean value, first moments and moment of inertia of a
   body with a position-dependent density, and say which of these the physics
   of a survey actually requires.
6. **Predict** how quadrature error behaves when the integrand has a
   singularity, and recognise the cases where Monte Carlo beats quadrature and
   the cases where the reverse holds.

## Prerequisites

- [01-05-05 Integration Techniques and Definite Integrals](../05-single-variable-calculus/05-integration.md)
  — every multiple integral here is a stack of those.
- [01-06-01 Partial Derivatives, Gradients and Directional Derivatives](./01-partial-derivatives.md)
  — the Jacobian used in Section 4 is built from partial derivatives.
- [01-04 Floating-Point Representation, Round-Off and Catastrophic Cancellation](../01-arithmetic/04-floating-point.md) —
  the summation error behaviour in Section 6 is that lesson applied.
- [01-03 Units, SI Conventions and Dimensional Analysis](../01-arithmetic/03-units-and-dimensional-analysis.md)
  — the units attached to the results below.

## 1. Intuition: integration is how a body becomes a number

A measurement is a number. A model is a distribution of properties in space. The
integral is the bridge: it is the operator that turns a description of the
subsurface into the quantity an instrument would record.

| Physical question | Integral that answers it |
|---|---|
| What is the mass of this ore body? | $M = \int\!\!\int\!\!\int_{\text{body}} \rho\, dV$ |
| What does its gravity anomaly look like? | $g_z(\mathbf{r}) = G \int\!\!\int\!\!\int \rho(\mathbf{r}')\dfrac{z - z'}{\lvert \mathbf{r}-\mathbf{r}'\rvert^{3}}\, dV'$ |
| What is the average porosity of a reservoir? | $\bar{\phi} = \dfrac{1}{V}\int\!\!\int\!\!\int \phi\, dV$ |
| How much heat is stored in a rock volume? | $Q = \int\!\!\int\!\!\int \rho\, c\, T\, dV$ |
| What is the reducing-to-pole operator for a magnetic anomaly? | a convolution, that is, an integral over one or two variables |

Every one of these is a multiple integral over a region of the Earth, and in
every case the practical difficulty is the same: the region is not a
rectangular box, so the integration limits depend on the integration variables.
Choosing which variable goes on the outside is what makes the difference
between a five-line calculation and a page of algebra.

Two ideas carry the whole lesson:

1. **Iteration.** A multiple integral is just a sequence of single integrals,
   and the order of the sequence does not change the answer.
2. **Change of variables.** A coordinate system that matches the symmetry of
   the body converts an awkward region into a box, at the price of a
   position-dependent factor — the Jacobian — which accounts for the fact that a
   small step in a coordinate is not a small physical distance.

## 2. Precise definitions

### 2.1 The double integral over a rectangle

Partition the rectangle $R = [a,b]\times[c,d]$ into $mn$ sub-rectangles of sides
$\Delta x$, $\Delta y$, pick any sample point $(x_i^*, y_j^*)$ inside each, and
form the Riemann sum

$$S_{mn} = \sum_{i=1}^{m}\sum_{j=1}^{n} f(x_i^*, y_j^*)\, \Delta x\, \Delta y .$$

If $S_{mn}$ tends to the same finite limit for every sequence of refinements and
every choice of sample points, that limit is the **double integral**

$$\iint_R f(x,y)\, dA = \iint_R f(x,y)\, dx\, dy .$$

The symbol $dA$ denotes the area element; in Cartesian coordinates
$dA = dx\,dy$. For $f \ge 0$ the integral is the volume under the surface
$z = f(x,y)$; for $f$ of either sign it is that volume with the sign attached, or
— more usefully — the total of the quantity $f$ per unit area.

### 2.2 Integrals over a general region

Let $D$ be a bounded region. Define

$$\iint_D f\, dA = \iint_R f\cdot \chi_D\, dA,$$

where $\chi_D$ is $1$ inside $D$ and $0$ outside and $R$ is any rectangle
containing $D$. The boundary of $D$ has zero area, so the value of $f$ there is
irrelevant: **this is the formal reason you never worry about the edge of an ore
body.**

In practice one avoids the indicator function by writing variable limits. If
$D = \{(x,y) : a \le x \le b,\; g_1(x) \le y \le g_2(x)\}$, then

$$\iint_D f\, dA = \int_a^b \!\left( \int_{g_1(x)}^{g_2(x)} f(x,y)\, dy \right) dx .$$

The inner integral is a single-variable integral whose result still depends on
$x$; the outer one then removes that dependence.

### 2.3 Iterated integrals and Fubini's theorem

If $f$ is continuous on the rectangle $[a,b]\times[c,d]$, then

$$\int_a^b \!\left( \int_c^d f(x,y)\, dy \right) dx
= \int_c^d \!\left( \int_a^b f(x,y)\, dx \right) dy .$$

This is **Fubini's theorem**. It fails only in pathological cases that do not
arise for the continuous densities of this curriculum, and it has an immediate
practical reading: *if one order of integration is hard, try the other.*
Section 5 checks both orders numerically.

The same statement for three variables justifies writing a volume integral as
three nested one-dimensional integrals in any order.

### 2.4 Change of variables

Suppose $x = x(u,v)$ and $y = y(u,v)$ map a region $D^*$ of the $(u,v)$ plane
one-to-one and onto $D$, with continuous partial derivatives. Then

$$\iint_D f(x,y)\, dx\, dy
= \iint_{D^*} f\bigl(x(u,v),\, y(u,v)\bigr)\,
\left\lvert \frac{\partial(x,y)}{\partial(u,v)} \right\rvert\, du\, dv ,$$

where the **Jacobian determinant** is

$$\frac{\partial(x,y)}{\partial(u,v)}
= \det \begin{pmatrix} \dfrac{\partial x}{\partial u} & \dfrac{\partial x}{\partial v} \\[2mm]
\dfrac{\partial y}{\partial u} & \dfrac{\partial y}{\partial v} \end{pmatrix}.$$

The absolute value is required because an orientation-reversing map has a
negative determinant while an area is positive. Lesson 03 develops the
Jacobian properly; here it is enough to know what it is for: **it is the local
ratio of physical volume to coordinate volume.**

### 2.5 The three standard volume elements

| Coordinates | Map | Volume element |
|---|---|---|
| Polar $(r,\phi)$ | $x = r\cos\phi,\ y = r\sin\phi$ | $dA = r\, dr\, d\phi$ |
| Cylindrical $(\rho,\phi,z)$ | $x = \rho\cos\phi,\ y = \rho\sin\phi$ | $dV = \rho\, d\rho\, d\phi\, dz$ |
| Spherical $(r,\theta,\phi)$ | $x = r\sin\theta\cos\phi,\ y = r\sin\theta\sin\phi,\ z = r\cos\theta$ | $dV = r^2 \sin\theta\, dr\, d\theta\, d\phi$ |

The spherical element has a purely geometric reading, which is worth more than
the determinant. At a point with spherical coordinates
$(r,\theta,\phi)$, a small coordinate step $(dr, d\theta, d\phi)$ describes a
curvilinear box with side lengths $dr$, $r\,d\theta$ and
$r\sin\theta\, d\phi$ along the three mutually orthogonal unit directions
$\hat{r}$, $\hat{\theta}$, $\hat{\phi}$. Multiplying gives
$dV = r^2\sin\theta\, dr\, d\theta\, d\phi$. The factors of $r$ and
$\sin\theta$ are exactly the corrections from an angle to an arc length; in
Lesson 03 the same factors appear as the determinant of the Jacobian matrix.

## 3. Derivations

### 3.1 From a Riemann sum to an iterated integral

For $f$ continuous on $R = [a,b]\times[c,d]$, group the Riemann sum by rows:

$$S_{mn} = \sum_{i=1}^{m} \left( \sum_{j=1}^{n} f(x_i^*, y_j^*)\, \Delta y \right) \Delta x .$$

The bracket is a Riemann sum for $\int_c^d f(x_i^*, y)\, dy$, so as
$n \to \infty$ it tends to $F(x_i^*)$ with $F(x) = \int_c^d f(x,y)\,dy$. But $F$
is continuous on $[a,b]$ (because $f$ is uniformly continuous on the compact
rectangle), so summing the $F(x_i^*)$ against $\Delta x$ is a Riemann sum for
$\int_a^b F(x)\,dx$. Hence the limit is the iterated integral. $\square$

The compactness argument is the reason continuity is enough. Physically it says:
*you may integrate a density over a region by sweeping one coordinate at a
time.*

### 3.2 Mass, mean value and the $r^2$ weighting

For a body occupying a volume $\Omega$ with density $\rho(\mathbf{r})$,

$$M = \iiint_\Omega \rho\, dV, \qquad
\bar{\rho} = \frac{M}{\lvert \Omega \rvert} = \frac{1}{V}\iiint_\Omega \rho\, dV,$$

and the **centre of mass** has components
$\bar{x}_i = \frac{1}{M}\iiint x_i \rho\, dV$.

For a spherically symmetric body, $\rho = \rho(r)$, and the spherical element
gives

$$M = \int_0^{2\pi}\!\!\int_0^{\pi}\!\!\int_0^{R} \rho(r)\, r^2\sin\theta\,
dr\, d\theta\, d\phi = 4\pi \int_0^{R} \rho(r)\, r^2\, dr .$$

This formula deserves to be read carefully, because it is counter-intuitive on
first contact. It says that in a volume average the material at radius $r$ is
weighted by $r^2$, not by $1$. One might expect the outer part of a sphere to
matter little because it is thin; in fact the outer shells contain most of the
volume, and $r^2$ is the statement of that. The consequence is quantitative and
important: a body whose *centre* is very dense can still have a modest mean
density. Section 5 computes a case where the central density is
$3500\ \mathrm{kg\,m^{-3}}$ and the mean is $875\ \mathrm{kg\,m^{-3}}$, exactly
a quarter.

### 3.3 Why the moments matter: two concrete integrals

**Moment of inertia.** For a rigid body rotating about the $z$ axis,

$$I_z = \iiint \rho\, (x^2 + y^2)\, dV .$$

The radius of gyration is $k = \sqrt{I_z/M}$. This is the integral that converts
a density model into the rotational response used in studies of the Earth's
rotation and of isostatic rebound.

**Total stored heat.** For a temperature field $T(\mathbf{r})$ in a medium of
density $\rho$ and specific heat capacity $c$,

$$Q = \iiint \rho\, c\, T\, dV .$$

Because the integrand is a product of three fields, this integral cannot be
reduced to a one-dimensional quadrature unless the fields are themselves
spherically symmetric. It is the standard illustration of the practical point
in Section 1: the difficulty of a multiple integral is almost always geometric,
not analytic.

### 3.4 A change of variables done twice, as a check

Evaluate the integral of $f(x,y) = x^2 + y^2$ over the disk of radius $a$.

*Cartesian, one order.* With $-a \le x \le a$ and
$-\sqrt{a^2-x^2} \le y \le \sqrt{a^2-x^2}$:

$$\iint_D (x^2+y^2)\, dA = \int_{-a}^{a}\!\left[\left(x^2 y + \frac{y^3}{3}\right)
\right]_{y=-\sqrt{a^2-x^2}}^{\,y=+\sqrt{a^2-x^2}} dx
= \int_{-a}^{a} 2x^2\sqrt{a^2-x^2} + \frac{2}{3}(a^2-x^2)^{3/2}\, dx .$$

*Polar.* With $x^2+y^2 = r^2$ and $dA = r\,dr\,d\phi$:

$$\iint_D (x^2+y^2)\, dA = \int_0^{2\pi}\!\!\int_0^{a} r^2 \cdot r\, dr\, d\phi
= 2\pi \cdot \frac{a^4}{4} = \frac{\pi a^4}{2}.$$

The polar route is three lines. The Cartesian route requires the substitution
$x = a\sin u$ twice and produces the same answer with far more opportunity for
error. **That difference is the reason change of variables exists.**

## 4. Physical interpretation

**An integral is a forward model.** The gravity integral in Section 1 is the
most important example in this whole curriculum: it maps the unknown —
a density distribution — to the observable. Discretising it (replace the
integral by a finite sum over cells) produces a matrix, and inverting that
matrix is the subject of [18-inverse-problems](../../18-inverse-problems/README.md).
The quadrature error you measure in this lesson is therefore not an abstract
concern; it is one of the error terms in a real inversion.

**The volumes you integrate over are rarely boxes.** A sedimentary basin, a
salt diapir, a magma chamber and a survey area are all irregular. The practical
consequence is that the integration limits must come from a geometric model —
a surface, a fault plane, a horizon — and errors in that model propagate into
the integral. This is the same *model-choice* problem discussed in
[18-01-04 Discretisation, Parameterisation and Model Choice](../../18-inverse-problems/01-inverse-problem-foundations/04-discretisation-reality.md),
appearing here as a question about limits rather than about basis functions.

**Average versus volume average.** Two different averages are in routine use and
they are not interchangeable. The **volume average** is $\frac{1}{V}\int\rho\,dV$;
a **mass average** is $\frac{1}{M}\int \rho\, \phi\, dV$ for a property $\phi$.
Bulk density from a density log is a volume average over the logged interval,
whereas the mass fraction of a mineral is a mass average. Confusing them is a
standard error in petrophysical arithmetic.

**When the integral does not converge.** If the integrand has a $1/r$ singularity
that survives after multiplying by the $r^2$ element, the integral may diverge.
The gravitational potential of a point mass is the borderline case: $\rho$ is
itself a delta function, and the potential $\int \rho/D\,dV$ is finite for any
observation point not inside the source. But the *field* integral
$\int \rho\, \hat{D}/D^3\, dV$ is finite only because the $1/D^2$ singularity is
cancelled by symmetry. Break the symmetry — for example, sample the field on the
boundary of the source — and the integral becomes singular. This is why
analytical forward models of polyhedra and prisms are stated with care about
which surfaces may contain the station.

## 5. Python demonstration

The companion script
[`code/multiple_integrals_demo.py`](./code/multiple_integrals_demo.py) checks
every claim above numerically with the standard library alone.

```python
def midpoint_2d(f, xa, xb, ya, yb, n):
    """Composite midpoint rule for the integral over a rectangle."""
    hx = (xb - xa) / n
    hy = (yb - ya) / n
    total = 0.0
    for i in range(n):
        x = xa + (i + 0.5) * hx
        for j in range(n):
            y = ya + (j + 0.5) * hy
            total += f(x, y)
    return total * hx * hy
```

### 5.1 A rectangle, two orders, and the exact value

Observed output for $\iint_{[0,2]\times[0,1]}(x^2+y^2)\,dA$, whose exact value is
$10/3$:

```text
exact value                          = 3.3333333333
order dx dy (x outer):
   n =  10: value = 3.3250000000   error = 8.333e-03
   n =  50: value = 3.3330000000   error = 3.333e-04
   n = 200: value = 3.3333125000   error = 2.083e-05
order dy dx (y outer):
   n =  10: value = 3.3250000000   error = 8.333e-03
   n =  50: value = 3.3330000000   error = 3.333e-04
   n = 200: value = 3.3333125000   error = 2.083e-05
```

The two orders agree digit for digit, and the error falls by a factor of 25 for
each factor of 5 in $n$: the midpoint rule is second order, so error
$\propto n^{-2}$. Nested one-dimensional quadrature inherits the order of the
innermost rule.

### 5.2 A region that is not a rectangle

The area between $y = x$ and $y = x^2$ on $[0,1]$ is $1/6$, obtained by doing the
inner integral analytically so that only one numerical integral remains:

```text
exact area                          = 0.1666666667
   n =  20: area = 0.1668750000   error = 2.083e-04
   n = 100: area = 0.1666750000   error = 8.333e-06
   n = 500: area = 0.1666670000   error = 3.333e-07
```

Second order again. The outer integration is over a fixed interval; the geometry
was absorbed into the inner limits, which is the standard strategy.

### 5.3 An integrand with a singular derivative

Area of a disk of radius 4, computed as $\int_{-R}^{R}2\sqrt{R^2-x^2}\,dx$:

```text
exact area = pi*R^2                  = 50.26548246
   n =  50: area = 50.30945138   error = 4.397e-02
   n = 200: area = 50.27098973   error = 5.507e-03
   n = 800: area = 50.26617122   error = 6.888e-04
```

Each factor of 4 in $n$ cuts the error by about 8, that is
error $\propto n^{-1.5}$. The midpoint rule is second order for smooth
integrands, and only order $3/2$ here because the integrand's derivative is
infinite at the endpoints. **The order of a quadrature rule is a property of the
pair (rule, integrand), not of the rule alone.** Recognising this is what lets
you decide whether a finer grid will actually help.

### 5.4 Volume of the unit ball: quadrature against Monte Carlo

```text
Monte Carlo (4e5 samples)           = 4.197460
spherical element, 4*pi*r^2 dr      = 4.188789942987
exact 4*pi/3                        = 4.188790204786
Monte Carlo relative error          = 2.070e-03
```

The spherical-element quadrature uses 4000 intervals and is accurate to
$2.6\times10^{-7}$ absolute, that is $6.3\times10^{-8}$ relative; the Monte
Carlo estimate uses 400 000 samples and is accurate to $2.0\times10^{-3}$
relative, close to the theoretical $1/\sqrt{N} = 1.6\times10^{-3}$.

This comparison is the whole reason quadrature is preferred in low dimensions
and Monte Carlo is preferred in high ones. Quadrature error in $d$ dimensions
with $n$ points per axis decays like $N^{-2/d}$: in three dimensions that is
$N^{-2/3}$, so beating Monte Carlo's $N^{-1/2}$ requires a great many points. By
about ten dimensions, quadrature has lost decisively. Section 9 of
[01-13 Probability and Statistics Foundations](../13-probability-and-statistics-foundations/09-error-propagation.md)
develops this comparison for uncertainty propagation, where the dimension is the
number of model parameters.

### 5.5 Mass and mean density of a body with a linear density profile

Take $\rho(r) = \rho_0(1 - r/R)$ with $\rho_0 = 3500\ \mathrm{kg\,m^{-3}}$ and
$R = 3\times10^{5}$ m. Then

$$M = 4\pi\rho_0\int_0^R \left(1 - \frac{r}{R}\right) r^2\, dr
= 4\pi\rho_0\left(\frac{R^3}{3} - \frac{R^4}{4R}\right)
= \frac{\pi \rho_0 R^3}{3}.$$

```text
   n =   200: M = 9.896141e+19 kg   error = 1.237e+15 kg
   n =  2000: M = 9.896018e+19 kg   error = 1.237e+13 kg
   n = 20000: M = 9.896017e+19 kg   error = 1.237e+11 kg
exact pi*rho0*R^3/3                 = 9.896017e+19 kg
model volume 4*pi*R^3/3             = 1.130973e+17 m^3
mean density M/V                    = 875.000000 kg/m^3   (exactly rho0/4 = 875.0)
```

Two things to notice. The error falls by 100 per decade of $n$, as expected for
a smooth integrand. And the mean density is exactly $\rho_0/4$: the body is
*not* light, but the volume average is dominated by the outer, lighter half.

> **Breaking exercise.** Change the density law in the demo to
> $\rho(r) = \rho_0(1 - r^2/R^2)$ and work out by hand what the mean density
> should be before running it. Then check. (Hint: it is not $\rho_0/4$.)

## 6. Exercises

Ten graded exercises are in
[`exercises/02-multiple-integrals-exercises.md`](./exercises/02-multiple-integrals-exercises.md)
and worked solutions in
[`exercises/02-multiple-integrals-solutions.md`](./exercises/02-multiple-integrals-solutions.md).

## 7. Common mistakes

1. **Writing the Jacobian factor once instead of once per condition.** With two
   coordinate changes in sequence, multiply the two Jacobians; it is easy to
   silently drop one.
2. **Forgetting the absolute value.** A change of variables with negative
   determinant yields a negative "volume" if the bars are omitted.
3. **Dropping the $r^2$ in $4\pi\int\rho r^2\,dr$.** This single omission turns a
   volume integral into an area integral and changes the mass by a factor with
   the dimensions of length.
4. **Putting the wrong variables in the limits.** The inner limits may depend
   only on the outer variables, never on the inner one. A limit that mentions
   its own variable is always an error.
5. **Assuming second-order convergence.** Section 5.3 shows order $3/2$ for a
   square-root endpoint. Integrands with algebraic singularities are common in
   geophysics: potential-field kernels, resistivity kernels, travel-time
   integrals.
6. **Believing Monte Carlo is always worse.** It is worse in one dimension and
   better in high-dimensional parameter spaces; the crossover is around a few
   dimensions. Choosing the wrong one wastes orders of magnitude of compute.
7. **Treating a volume average and a mass average as the same thing.** They
   differ whenever the property is correlated with density.
8. **Integrating a singular kernel at a station that lies on the source
   boundary.** The result is finite only in special geometries; a naive
   quadrature will return a large, wrong number rather than failing.

## 8. Real-world applications

- **Potential-field forward modelling.** The gravity and magnetic integrals of
  Section 1 are evaluated by discretising the body into cells. Prism and
  polyhedron formulas are analytic versions of the same integral, derived
  precisely to avoid the quadrature error measured in Section 5. See
  [07-03-03 Forward Modelling in 2-D and 3-D](../../07-gravity-geodesy/03-gravity-anomalies-and-modelling/03-forward-modelling-2d3d.md)
  and [05-03-02 Analytical Solutions for Simple Bodies](../../05-core-geophysics/03-forward-modelling-principles/02-analytical-solutions.md).
- **Reservoir volumes.** Gross rock volume is a triple integral over a seismic
  horizon-bounded region. The uncertainty in the limits dominates the
  uncertainty in the arithmetic.
- **Heat and ice budgets.** Glacial isostatic adjustment models integrate
  density over a spherical Earth with a radially varying profile; the $r^2$
  weighting of Section 3.2 is the reason deep structure contributes
  substantially to the total mass.
- **Moment of inertia and the Earth's rotation.** The non-hydrostatic part of
  the inertia tensor regulates the Chandler wobble and the length-of-day; it is
  a volume integral of the density field that is only weakly constrained.
- **Averaging borehole logs.** A log-derived average is a depth integral; the
  arithmetic mean of the samples equals the integral only if the samples are
  evenly spaced, which in a real log they are not.
- **Groundwater storage.** Total storage change is $\int\!\!\int\!\!\int
  S_s\, \Delta h\, dV$ from a head field, which is why satellite gravimetry
  (a mass integral) and well hydrographs (a point measurement) do not always
  agree; see [07-05 Satellite Gravimetry](../../07-gravity-geodesy/05-satellite-gravimetry/README.md).

## 9. Further reading

- **Marsden, J. E., & Tromba, A. *Vector Calculus.* W. H. Freeman.** Chapters on
  double and triple integrals, Fubini's theorem and the change-of-variables
  theorem. Level: intermediate. Check your library for the current edition.
- **Spivak, M. *Calculus on Manifolds.* Addison-Wesley.** A short, austere
  treatment in which the change-of-variables theorem is proved properly and the
  Jacobian is given its real meaning. Level: advanced; useful once, then kept.
- **Davis, P. J., & Rabinowitz, P. *Methods of Numerical Integration.* Dover.**
  The reference for the error orders used in Section 5, including the effect of
  endpoint singularities. Level: advanced.
- **Telford, W. M., Geldart, L. P., & Sheriff, R. E. (1990). *Applied
  Geophysics* (2nd ed.). Cambridge University Press.** The discretised forms of
  the potential-field integrals as they are actually computed in surveys.
  Level: intermediate.
- **Blakely, R. J. (1995). *Potential Theory in Gravity and Magnetic
  Applications.* Cambridge University Press.** Chapter 2 for the volume,
  surface and line integrals of potential theory and the conditions under which
  each is valid. Level: advanced.

> Note on citations: bibliographic details above are given so that you can
> locate the works. This repository does not host or reproduce copyrighted text,
> and you should confirm editions and current availability through your library
> before citing them yourself.

## 10. Related lessons

- [01 Partial Derivatives, Gradients and Directional Derivatives](./01-partial-derivatives.md) —
  the differential counterpart, and the source of the Jacobian's entries.
- [03 Jacobians, Coordinate Transformations and Volume Elements](./03-jacobians.md) —
  the Jacobian developed properly, with the volume elements derived from it.
- [04 Divergence, Curl and Physical Meaning](./04-divergence-and-curl.md) —
  divergence as the derivative of exactly the flux integral this lesson
  evaluates.
- [05 Line and Surface Integrals; Flux and Circulation](./05-line-surface-integrals.md) —
  integrals over lower-dimensional objects.
- [01-05-05 Integration Techniques and Definite Integrals](../05-single-variable-calculus/05-integration.md) —
  the one-dimensional toolkit.
- [01-12 Numerical Methods for Mathematical Problems](../12-numerical-methods/README.md) —
  quadrature in practice, including adaptive rules not used here.
- [01-13-09 Error and Uncertainty Propagation](../13-probability-and-statistics-foundations/09-error-propagation.md) —
  Monte Carlo against quadrature in higher dimensions.

## Self-assessment checklist

- [ ] I can write the double integral over a region as an iterated integral with
      the correct limits, in either order. (Section 2.2)
- [ ] I can state Fubini's theorem and give the continuity condition it needs.
      (Section 2.3)
- [ ] I can write the change-of-variables formula from memory, with the absolute
      value on the Jacobian. (Section 2.4)
- [ ] I can derive the spherical volume element geometrically, by multiplying
      three arc lengths. (Section 2.5)
- [ ] I can explain why $r^2$ appears in the mass integral and what it implies
      about the relative contribution of the deep Earth. (Section 3.2)
- [ ] I can compute the mean density of a body with a given $\rho(r)$ and say
      whether it is closer to the central or the surface density. (Section 5.5)
- [ ] I can look at an integrand and predict whether refining the grid will give
      second-order or fractional-order convergence. (Section 5.3)
- [ ] I can state the dimensional dependence that makes Monte Carlo competitive
      above a few dimensions. (Section 5.4)
- [ ] I can describe two different physical averages of the same data and say
      which one a given measurement produces. (Section 4)
