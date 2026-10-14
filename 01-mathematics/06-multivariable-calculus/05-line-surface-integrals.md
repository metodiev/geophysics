---
id: 01-06-05
title: "Line and Surface Integrals; Flux and Circulation"
level: advanced
prereqs: ["01-06-02", "01-06-04"]
estimated_minutes: 90
tags: [multivariable-calculus, flux, circulation, surface-integrals, potential-fields]
---

# Line and Surface Integrals; Flux and Circulation

## Learning objectives

By the end of this lesson you will be able to:

1. **Parametrise** a curve and a surface, and write the arclength element and
   the surface element without consulting a table of special cases.
2. **Compute** the line integral of a scalar field (a length-weighted average or
   a travel time) and of a vector field (work, or circulation).
3. **Compute** the surface integral of a scalar field, including over a
   non-planar surface, and the **flux** of a vector field, with the orientation
   chosen correctly and stated.
4. **Derive** the potential difference between two points as a line integral,
   and explain what path independence buys you in practice.
5. **Derive** the flux of an inverse-square field through a closed surface using
   solid angle, and thereby obtain Gauss's law without ever using a sphere.
6. **Recognise** the physical measurements that are line and surface integrals:
   travel time, work, heat flux, mass flux, circulation, and the flux of a
   potential field through a datum.

## Prerequisites

- [01-06-02 Multiple Integrals and Change of Variables](./02-multiple-integrals.md) —
  the integrals here are obtained by restricting a multiple integral to a curve
  or a surface.
- [01-06-04 Divergence, Curl and Physical Meaning](./04-divergence-and-curl.md) —
  flux and circulation are the quantities whose *densities* are the divergence
  and the curl; this lesson computes the integrals themselves.
- [01-06-01 Partial Derivatives, Gradients and Directional Derivatives](./01-partial-derivatives.md) —
  tangent vectors and the gradient used throughout.
- [01-04-03 Cartesian, Cylindrical and Spherical Coordinates](../04-geometry-and-coordinates/03-cartesian-spherical.md) —
  the parametrisations used in the examples.

## 1. Intuition: measurements are integrals over curves and surfaces

A gravimeter measures a field at a point. Almost everything else measures an
integral.

| Measurement | Kind of integral | Integrand | Physical reading |
|---|---|---|---|
| Seismic travel time along a ray | line, scalar | slowness $1/v$ | $\int_{\text{ray}} dl/v$ |
| Work done moving a mass in a field | line, vector | $\mathbf{g}\cdot d\mathbf{l}$ | potential difference |
| Circulation of a magnetic field | line, vector | $\mathbf{B}\cdot d\mathbf{l}$ | enclosed current, times $\mu_0$ |
| Heat leaving a rock volume | surface, vector | $\mathbf{q}\cdot d\mathbf{A}$ | energy per second |
| Groundwater discharge through a cross-section | surface, vector | $\mathbf{v}\cdot d\mathbf{A}$ | volume per second |
| Gravity flux through a closed surface | surface, vector | $\mathbf{g}\cdot d\mathbf{A}$ | enclosed mass, times $-4\pi G$ |
| Bouguer slab correction | surface, scalar | $\rho\, t$ integrated | mass per unit area |

Two of these are so important that they get their own names. The **flux** of
$\mathbf{F}$ through an oriented surface is

$$\Phi = \iint_S \mathbf{F}\cdot d\mathbf{A},$$

and the **circulation** of $\mathbf{F}$ around a closed curve is

$$\Gamma = \oint_C \mathbf{F}\cdot d\mathbf{l}.$$

These are the two quantities that Lesson 04's operators differentiate, and the
two that Lesson 06's theorems relate to volume and surface integrals
respectively.

## 2. Precise definitions

### 2.1 Curves and their arclength element

A **parametrised curve** is a differentiable map
$\mathbf{r}(t) = (x(t), y(t), z(t))$ for $t \in [a,b]$. Its velocity is
$\mathbf{r}'(t)$ and its **speed** is $\lvert\mathbf{r}'(t)\rvert$. The arclength
element is

$$dl = \lvert \mathbf{r}'(t)\rvert\, dt .$$

*Why.* Over a small $\Delta t$ the displacement is approximately
$\mathbf{r}'(t)\Delta t$, so the distance travelled is
$\lvert\mathbf{r}'\rvert\Delta t$. Dividing a partition into pieces and letting
$\Delta t\to 0$ gives the arclength integral
$L = \int_a^b \lvert\mathbf{r}'(t)\rvert\, dt$. $\square$

### 2.2 Line integrals of a scalar field and of a vector field

For a scalar field $f$ (for example temperature, or slowness),

$$\int_C f\, dl = \int_a^b f(\mathbf{r}(t))\, \lvert\mathbf{r}'(t)\rvert\, dt .$$

This is a length-weighted average of $f$ along the curve, multiplied by the
length. **Travel time is exactly this integral** with $f = 1/v$.

For a vector field $\mathbf{F}$,

$$\int_C \mathbf{F}\cdot d\mathbf{l}
= \int_a^b \mathbf{F}(\mathbf{r}(t))\cdot \mathbf{r}'(t)\, dt ,$$

where $d\mathbf{l} = \mathbf{r}'(t)\,dt$ is the vector line element. This is
**work** if $\mathbf{F}$ is a force, and a **circulation** when the curve is
closed.

### 2.3 Surfaces, and the surface element as a cross product

A **parametrised surface** is a map
$\mathbf{r}(u,v)$ from a region $D$ of the $(u,v)$ plane into space. Its tangent
vectors are $\mathbf{r}_u = \partial\mathbf{r}/\partial u$ and
$\mathbf{r}_v = \partial\mathbf{r}/\partial v$. The **surface element** is the
area of the small parallelogram they span:

$$d\mathbf{A} = (\mathbf{r}_u \times \mathbf{r}_v)\, du\, dv,
\qquad dA = \lvert \mathbf{r}_u \times \mathbf{r}_v\rvert\, du\, dv .$$

The vector surface element already carries the orientation: the normal points in
the direction of $\mathbf{r}_u\times\mathbf{r}_v$ by the right-hand rule. Swapping
$u$ and $v$ reverses both the cross product and the sign of the flux — which is
why orientation is not optional in a flux integral and irrelevant in a scalar
surface integral.

For a surface given as a graph $z = g(x,y)$ over a region $D$ in the $xy$-plane,
the same formula with $u = x$, $v = y$ gives

$$dA = \sqrt{1 + \left(\frac{\partial g}{\partial x}\right)^2
+ \left(\frac{\partial g}{\partial y}\right)^2}\, dx\, dy,$$

and $d\mathbf{A} = (-g_x, -g_y, 1)\,dx\,dy$ for the upward normal. For a
horizontal plane, $g$ is constant and this reduces to
$dA = dx\,dy$ — which is why flat-datum surveys are so much easier to invert
than draped ones.

### 2.4 Flux and circulation defined

$$\Phi = \iint_S \mathbf{F}\cdot d\mathbf{A}, \qquad
\Gamma = \oint_C \mathbf{F}\cdot d\mathbf{l}.$$

For a **closed** surface the conventional orientation is outward, and one writes
$\oint$ with a circle. For a closed curve the orientation is chosen by the
right-hand rule relative to a chosen normal, which becomes explicit in Stokes'
theorem.

### 2.5 Conservative fields and potentials

$\mathbf{F}$ is **conservative** on a region if there is a scalar $\phi$ with
$\mathbf{F} = \nabla\phi$ there — in this module's gravity convention, that is
$\mathbf{g} = \nabla V$. On a simply connected region this is equivalent to
$\nabla\times\mathbf{F} = \mathbf{0}$ ([01-06-04](./04-divergence-and-curl.md),
Section 3.6). The two consequences used constantly are:

$$\int_C \mathbf{F}\cdot d\mathbf{l}\ \text{is path-independent},
\qquad
\oint_C \mathbf{F}\cdot d\mathbf{l} = 0\ \text{for every closed } C .$$

## 3. Derivations

### 3.1 A potential difference is a line integral

Let $\mathbf{F} = \nabla\phi$ and let $C$ be any curve from $\mathbf{p}_0$ to
$\mathbf{p}_1$, parametrised by $\mathbf{r}(t)$ with $t\in[0,1]$. Then

$$\int_C \mathbf{F}\cdot d\mathbf{l}
= \int_0^1 \nabla\phi(\mathbf{r}(t))\cdot\mathbf{r}'(t)\, dt
= \int_0^1 \frac{d}{dt}\Bigl[\phi(\mathbf{r}(t))\Bigr] dt
= \phi(\mathbf{p}_1) - \phi(\mathbf{p}_0).$$

The chain rule converts the line integral into an ordinary one-dimensional
integral of a total derivative, which the fundamental theorem of calculus
evaluates at the endpoints. $\square$

**This is the single most useful fact in potential-field work.** It says that the
integral of a conservative field depends only on the endpoints, so no ray path
needs to be known, and it is the reason a potential is worth defining at all: the
potential converts a path integral into a subtraction.

### 3.2 Flux: two worked surface elements

**A sphere of radius $R$.** Parametrise with the spherical angles,
$\mathbf{r}(\theta,\phi) = R(\sin\theta\cos\phi, \sin\theta\sin\phi, \cos\theta)$.
The tangent vectors are $\mathbf{r}_\theta$ and $\mathbf{r}_\phi$, and

$$\lvert \mathbf{r}_\theta \times \mathbf{r}_\phi \rvert = R^2\sin\theta,
\qquad \hat{n} = \hat{r} .$$

So $d\mathbf{A} = R^2\sin\theta\, d\theta\, d\phi\, \hat{r}$: the familiar
$r^2\sin\theta$ of the spherical volume element appears again, now as a surface
element. (For a volume it was $r^2\sin\theta\,dr\,d\theta\,d\phi$; the extra $dr$
is the only difference, which is exactly what "integrate the surface element
radially" means.)

**A horizontal sheet at depth.** Let a plane surface at height $h$ above a point
$\mathbf{p}$ be viewed from $\mathbf{p}$ by a solid angle $\Omega$. The apparent
area element is $dA_\perp = D^2\, d\Omega$ where $D$ is the distance and the
normal is along the line of sight. This relation is the entire content of the
next subsection.

### 3.3 Flux of an inverse-square field by solid angle

Let a point mass $M$ sit at the origin and let $S$ be any closed surface that
encloses it. The field is $\mathbf{g} = -GM\hat{r}/r^2$. At a surface element
whose outward normal makes an angle $\gamma$ with $\hat{r}$,

$$\mathbf{g}\cdot d\mathbf{A} = -\frac{GM}{r^2}\cos\gamma\, dA .$$

Now $dA\cos\gamma$ is the **projected** area of the element on a plane
perpendicular to the line of sight, so $dA\cos\gamma/r^2$ is precisely the solid
angle $d\Omega$ subtended by the element at the origin. Hence

$$\mathbf{g}\cdot d\mathbf{A} = -GM\left(\frac{\cos\gamma\,dA}{r^2}\right)
= -GM\, d\Omega, \qquad
\oint_S \mathbf{g}\cdot d\mathbf{A} = -GM\oint_S d\Omega = -4\pi GM .$$

The last step uses the fact that any closed surface enclosing the origin
subtends the full solid angle $4\pi$. $\square$

**Read what this proof did.** It never used a sphere, never assumed a symmetric
surface, and never mentioned mass distribution. Three consequences follow
immediately, and all three are used throughout later modules:

1. **The flux depends only on the enclosed mass**, so the surface can be a cube,
   a tetrahedron or a draped topographic surface (Section 5.2 verifies this for a
   cube numerically).
2. **Newton's shell theorem follows**: any spherically symmetric redistribution of
   the same mass produces the same external field, and any spherically symmetric
   shell produces no field inside its cavity.
3. **The "field" is not required to be differentiable on the surface.** Only the
   flux is needed, which is why this form survives the singularities that
   Section 3.3 of [01-06-04](./04-divergence-and-curl.md) could not.

### 3.4 Circulation and Ampère's law

The same argument run one dimension lower gives Stokes' theorem. For the magnetic
field of a long straight wire, $\mathbf{B} = \frac{\mu_0 I}{2\pi\rho}\hat{\phi}$,
and a circular loop of radius $\rho$ centred on the wire has
$d\mathbf{l} = \rho\,d\phi\,\hat{\phi}$, so

$$\oint \mathbf{B}\cdot d\mathbf{l}
= \int_0^{2\pi}\frac{\mu_0 I}{2\pi\rho}\,\rho\, d\phi = \mu_0 I .$$

The radius cancels. **That cancellation is the whole physical content of
Ampère's law**: the circulation measures the enclosed current and nothing else,
just as the solid-angle argument showed that the flux measures the enclosed mass
and nothing else. Section 5.4 verifies the cancellation numerically to a relative
error of $2.3\times10^{-13}$.

### 3.5 Gravity of a sheet, by explicit surface integration

An infinite plane sheet of areal density $\sigma$ produces a **uniform** field
perpendicular to itself, of magnitude $2\pi G\sigma$ — independent of the
distance from the sheet. Derive it by surface integration rather than quoting it.

Take the sheet to be the plane $z = 0$ and the observation point at height $h$
above it. The vertical component from the ring between radii $\rho$ and
$\rho + d\rho$ is

$$dg_z = G\sigma \frac{h}{(\rho^2 + h^2)^{3/2}}\, 2\pi\rho\, d\rho .$$

Integrating over the disk of radius $R$ (columns of the sheet beyond $R$ are
neglected for now):

$$g_z(R) = 2\pi G\sigma h\int_0^R \frac{\rho\,d\rho}{(\rho^2+h^2)^{3/2}}
= 2\pi G\sigma\left(1 - \frac{h}{\sqrt{R^2+h^2}}\right),$$

using $\int \rho(\rho^2+h^2)^{-3/2}d\rho = -(\rho^2+h^2)^{-1/2}$. Letting
$R\to\infty$ gives the infinite-sheet result $g_z = 2\pi G\sigma$, **independent
of $h$**. Section 5.6 confirms both the closed form and the limit numerically.

This is the Bouguer slab correction of gravity surveying, and it is the reason
slab-corrected anomalies do not attenuate with elevation over a wide,
uniform-density layer. Stacking sheets of density $\rho$ and thickness $dz$ gives
the slab formula $g_z = 2\pi G\rho t$ — and, as Lesson 08 shows, three quite
different slabs can produce it.

### 3.6 Travel time is a line integral, and Fermat is a stationarity statement

Seismic travel time between two points is

$$T = \int_{\text{ray}} \frac{dl}{v} .$$

Fermat's principle states that the ray path is a stationary point of $T$ among
all paths joining the endpoints. This is a statement in the calculus of
variations, but its geometric content is visible from the eikonal relation
$\lvert\nabla T\rvert = 1/v$ of
[01-06-01](./01-partial-derivatives.md): the gradient of the travel-time field
points along the ray, so rays are everywhere orthogonal to wavefronts. Reading a
travel-time field as a solution of a partial differential equation, rather than
integrating along rays, is the numerical approach used in eikonal solvers.

## 4. Physical interpretation

**Flux measures what passes through, circulation measures what goes around.**
The pair is exhaustive for a vector field: whatever a field does, it either
crosses surfaces or circulates around loops. That is why the two integral
theorems of Lesson 06 (divergence and Stokes) together determine a field from its
sources and its circulations.

**Orientation is a physical choice, not a convention to be memorised.** The
outward normal of a closed surface is the direction of *leaving the volume*:
that is why the gravitational flux through a closed surface is
$-4\pi GM$ rather than $+4\pi GM$ — the field points inward while the normal
points outward. Change the convention and every sign in the physics changes with
it. Write the orientation down whenever you state a flux result.

**A through-going flux can be huge while the divergence is zero.** In a
steady-state heat flow problem $\nabla\cdot\mathbf{q} = 0$ everywhere, and yet
the flux through any closed surface may be large in magnitude — equal and
opposite on the two sides. Confusing "zero divergence" with "no flux" is the
most common conceptual error in this part of the subject.

**Not every surface integral is a flux.** The scalar surface integral
$\iint_S f\, dA$ — total mass per unit area over a map sheet, total heat content
per unit area of a plate — has no orientation. Mixing the two up produces sign
errors that look like physics.

**Datum choice is a surface-integral question.** Reducing gravity data to a
common datum, continuing a field upward, or resampling an airborne drape onto a
flat surface all involve integrals over surfaces that are not planes. Section
2.3's $\sqrt{1+g_x^2+g_y^2}$ factor is the price, and on steep topography it is
not small. See
[07-04-04 Gravity Reductions: Free-Air, Bouguer, Isostatic and Terrain](../../07-gravity-geodesy/01-gravity-fundamentals/04-gravity-reduction.md)
and [05-05 Survey Design and Data Acquisition Principles](../../05-core-geophysics/05-survey-design-and-acquisition/README.md).

## 5. Python demonstration

Two companion scripts compute the integrals of this lesson. Both use only the
standard library.

### 5.1 Flux through a cube: the shape does not matter

`code/integral_theorems_demo.py` integrates $\mathbf{g}$ explicitly over the six
faces of a $1000\ \mathrm{m}$ cube centred on a $10^{12}$ kg point mass:

```text
n =  60:  flux of g through the cube = -838.736660 m^3/s^2   relative error = 6.807e-05
n = 240:  flux of g through the cube = -838.683143 m^3/s^2   relative error = 4.254e-06
exact -4*pi*G*M = -838.679575 m^3/s^2
```

The value is the same one that came out of a spherical surface in
`code/divergence_curl_demo.py`:

```text
n_theta = 400: surface integral = -838.681730 m^3/s^2   relative error = 2.570e-06
exact -4*pi*G*M = -838.679575 m^3/s^2
```

Sphere and cube, the same answer. This is Section 3.3 confirmed: only the
enclosed mass matters. The two scripts' quadrature errors are of the same order,
which is a further check that neither is accidentally exact.

### 5.2 Circulation and curl over a disk

```text
circulation of F on the unit circle        = 6.2831853072
m = 200:  flux of curl F over the disk = 6.2856000000
m = 800:  flux of curl F over the disk = 6.2831500000
exact 2*pi                                 = 6.2831853072
```

The field is $\mathbf{F} = (-y, x, 0)$, whose curl is $(0,0,2)$; the circle
integral gives $2\pi$ and the surface integral of the curl over the disk gives
the same $2\pi$, converging as the disk quadrature is refined. That equality is
Stokes' theorem, and Lesson 06 derives it.

### 5.3 Ampère's law, where the radius cancels

```text
loop integral of B . dl around a circle of radius 50 m = 6.283185307e-03 T m
mu0 * I                                                  = 6.283185307e-03 T m
relative error                                           = 2.337e-13
```

### 5.4 The gravity of a disk and of a sheet

`code/potential_theory_demo.py` evaluates the disk integral of Section 3.5 both
by quadrature and from the closed form:

```text
disk radius R =      1000 m: numeric = 3.7761392980e-05   closed form = 3.7761391902e-05   rel. diff = 2.853e-08
disk radius R =     10000 m: numeric = 4.1514663014e-05   closed form = 4.1514659918e-05   rel. diff = 7.458e-08
disk radius R =   1000000 m: numeric = 4.1929796054e-05   closed form = 4.1929785342e-05   rel. diff = 2.555e-07
R -> infinity gives 2*pi*G*sigma = 4.1933978740e-05 m/s^2
```

The quadrature was done in the variable $\rho = h\sinh u$, which turns the radial
integral into $G\sigma\int 2\pi\tanh u\,\mathrm{sech}\,u\,du$ — an integral whose
antiderivative is $-2\pi\,\mathrm{sech}\,u$, so it converges to $2\pi G\sigma$
without ever needing a large numerical range. Watch the closed form approach
$2\pi G\sigma$ only slowly: the departure is $O(h/R)$, not $O(h^2/R^2)$, because
$1 - h/\sqrt{R^2+h^2} \approx 1 - h/R$. A "large enough" sheet is larger than
intuition suggests.

### 5.5 A scalar surface integral worth knowing: the mean value property

For a harmonic function the average over a sphere equals the value at the
centre:

```text
n = 100:  sphere average of V = 1.334853827e-02   V at the centre = 1.334800000e-02   rel. diff = 4.033e-05
n = 400:  sphere average of V = 1.334803364e-02   V at the centre = 1.334800000e-02   rel. diff = 2.520e-06
same test for f = x^2 + y^2 + z^2: sphere average = 1000002.570215   centre value = 0.000000
```

The first function is $V = GM/D$ with the source outside the sphere; the second
is $f = x^2+y^2+z^2$, whose Laplacian is $6$. The mean value property holds for
the first and fails by 100 % for the second. **It is a test of harmonicity, not a
general property of averages**, and it is a surface integral either way. Lesson
08 uses it to prove uniqueness.

> **Breaking exercise.** Take the cube of Section 5.1 and move the point mass
> just outside one face. Predict, before running, whether the flux will be zero
> exactly or merely small, and estimate the relative size of the residual
> quadrature error. Then run it and reconcile.

## 6. Exercises

Ten graded exercises are in
[`exercises/05-line-surface-integrals-exercises.md`](./exercises/05-line-surface-integrals-exercises.md)
and worked solutions in
[`exercises/05-line-surface-integrals-solutions.md`](./exercises/05-line-surface-integrals-solutions.md).

## 7. Common mistakes

1. **Forgetting the arclength factor.** Writing
   $\int_C f\,dt$ instead of $\int_C f\lvert\mathbf{r}'\rvert\,dt$ is correct only
   for a curve parametrised at unit speed. For a ray with a slowing velocity, it
   is a travel-time error of exactly the factor $v$.
2. **Reversing a curve or a surface without changing the sign.** Orientation is
   part of the value of a flux or circulation integral, not a presentational
   detail.
3. **Using $dA = dx\,dy$ on a non-horizontal surface.** The factor
   $\sqrt{1+g_x^2+g_y^2}$ is exactly what terrain corrections exist to account
   for.
4. **Believing that zero divergence means zero flux.** Section 4 has the
   counterexample; it is the commonest error in this part of the subject.
5. **Assuming a "large enough" sheet behaves as an infinite one.** Section 5.4
   shows the approach is $O(h/R)$: to be within 1 % of the infinite-sheet value
   requires a sheet radius of order $100h$.
6. **Assuming path independence without checking the domain.** On a non-simply
   connected domain a curl-free field need not be a gradient, and path
   independence fails; [01-06-04](./04-divergence-and-curl.md) Section 3.6 gives
   the counterexample.
7. **Confusing the scalar surface integral with the flux.** Only one of them has
   a sign.
8. **Neglecting the drape.** An airborne or shipborne survey measures on a
   non-planar surface; the surface element of Section 2.3 is not $dx\,dy$, and
   processing it as if it were introduces a systematic error correlated with
   topography.

## 8. Real-world applications

- **Travel-time tomography.** Travel time is the line integral of slowness along
  a ray, and inversion for the slowness field is one of the standard inverse
  problems of seismology; the discretisation of the line integral is the
  forward operator. See [06-seismology](../../06-seismology/README.md).
- **Gravity reductions and terrain corrections.** The free-air, Bouguer and
  terrain corrections are all surface integrals over the topography, with the
  $\sqrt{1+g_x^2+g_y^2}$ factor of Section 2.3. See
  [07-01-04 Gravity Reductions: Free-Air, Bouguer, Isostatic and Terrain](../../07-gravity-geodesy/01-gravity-fundamentals/04-gravity-reduction.md).
- **Magnetotellurics and EM induction.** Impedance estimates are ratios of field
  components, but the underlying physics is Faraday's law in circulation form:
  the measured electric field around a loop is the rate of change of magnetic
  flux through it. See
  [08-04-02 Magnetotellurics](../../08-geomagnetism-electromagnetism/04-electromagnetic-induction/02-magnetotellurics.md).
- **Darcy flux and catchment water balances.** Discharge through a
  cross-section is the flux integral of Darcy velocity; aquifer-scale water
  balances are stated as flux equalities over closed surfaces.
- **Heat-flow measurements.** Borehole heat flux is
  $\mathbf{q}\cdot d\mathbf{A}$ on a horizontal surface, and the sign convention
  determines whether a positive number means heat leaving the Earth.
- **Upward and downward continuation.** Both are surface integrals over the
  measurement datum, with kernels that grow or decay with wavenumber; the
  surface element is the reason draped surveys need special kernels. See
  [07-03-05 Derivatives, Upward/Downward Continuation and Euler Deconvolution](../../07-gravity-geodesy/03-gravity-anomalies-and-modelling/05-derivatives-and-filters.md).
- **Solid earth tides and loading.** The response of the Earth to a surface load
  is expressed as a surface integral of the load over the sphere.

## 9. Further reading

- **Marsden, J. E., & Tromba, A. *Vector Calculus.* W. H. Freeman.** Line and
  surface integrals, orientation, and the parametrisations of Sections 2.1–2.4.
  Level: intermediate. Check your library for the current edition.
- **Schey, H. M. *Div, Grad, Curl, and All That.* W. W. Norton.** The solid-angle
  argument of Section 3.3 is treated here in the most accessible form available.
  Level: beginner to intermediate.
- **Griffiths, D. J. *Introduction to Electrodynamics.* Cambridge University
  Press.** Chapters 1–2 and 5 for flux, circulation and the physical readings of
  Section 4. Level: intermediate. Any recent edition.
- **Blakely, R. J. (1995). *Potential Theory in Gravity and Magnetic
  Applications.* Cambridge University Press.** The surface integrals of potential
  theory — single and double layers, equivalent strata — and their convergence
  conditions. Level: advanced.
- **Telford, W. M., Geldart, L. P., & Sheriff, R. E. (1990). *Applied
  Geophysics* (2nd ed.). Cambridge University Press.** Terrain corrections and
  datum reductions as they are computed in practice. Level: intermediate.
- **Cerveny, V. *Seismic Ray Theory.* Cambridge University Press.** The line
  integral of Section 3.6 developed into a full theory of rays and travel times.
  Level: graduate.

> Note on citations: bibliographic details above are given so that you can
> locate the works. This repository does not host or reproduce copyrighted text,
> and you should confirm editions and current availability through your library
> before citing them yourself.

## 10. Related lessons

- [04 Divergence, Curl and Physical Meaning](./04-divergence-and-curl.md) —
  the densities whose integrals are computed here.
- [06 Gauss, Stokes and Green Theorems](./06-integral-theorems.md) — the theorems
  that convert between these integrals.
- [02 Multiple Integrals and Change of Variables](./02-multiple-integrals.md) —
  volume integrals, and the change of variables that makes them tractable.
- [08 Potential Fields, Laplace and Poisson Equations](./08-potential-theory.md) —
  where the flux argument of Section 3.3 becomes Gauss's law and then Poisson's
  equation.
- [04-05 Surfaces, Parametrisation and Curvature](../04-geometry-and-coordinates/05-surfaces-and-curvature.md) —
  the differential geometry of the surfaces parametrised here.
- [07-01-04 Gravity Reductions: Free-Air, Bouguer, Isostatic and Terrain](../../07-gravity-geodesy/01-gravity-fundamentals/04-gravity-reduction.md) —
  surface integrals at the centre of gravity processing.

## Self-assessment checklist

- [ ] I can parametrise a straight line, a circle, a sphere and a graph surface,
      and write the correct element for each. (Sections 2.1, 2.3)
- [ ] I can derive $dl = \lvert\mathbf{r}'\rvert dt$ and
      $dA = \lvert\mathbf{r}_u\times\mathbf{r}_v\rvert du\,dv$ from the geometry
      of a small displacement. (Sections 2.1, 2.3)
- [ ] I can compute a travel time as a line integral of slowness. (Sections 2.2,
      3.6)
- [ ] I can prove that a potential difference is a line integral and say what
      that buys in practice. (Section 3.1)
- [ ] I can derive the flux of an inverse-square field through a closed surface
      by the solid-angle argument, without assuming symmetry. (Section 3.3)
- [ ] I can derive the gravity of an infinite sheet and say why it is
      height-independent. (Section 3.5)
- [ ] I can state the orientation convention for a closed surface and explain the
      sign of the gravitational flux. (Section 4)
- [ ] I can say why a zero divergence is compatible with a large through-going
      flux. (Section 4)
- [ ] I can decide, for a given geophysical operation, whether the relevant
      integral is a scalar surface integral or a flux. (Section 4)
