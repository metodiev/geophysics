---
id: 01-06-03
title: "Jacobians, Coordinate Transformations and Volume Elements"
level: intermediate
prereqs: ["01-06-01", "01-06-02", "01-07-02"]
estimated_minutes: 90
tags: [multivariable-calculus, jacobian, coordinate-transformations, uncertainty]
---

# Jacobians, Coordinate Transformations and Volume Elements

## Learning objectives

By the end of this lesson you will be able to:

1. **Write down** the Jacobian matrix of a coordinate transformation and compute
   its determinant for the polar, cylindrical and spherical maps.
2. **Derive** the volume elements $dA = r\,dr\,d\phi$, $dV = \rho\,d\rho\,d\phi\,dz$
   and $dV = r^2\sin\theta\,dr\,d\theta\,d\phi$ from the determinant, and explain
   each factor geometrically.
3. **Explain** the multivariate chain rule as matrix multiplication, and deduce
   that determinants multiply along a chain of transformations.
4. **Transform** a gradient between coordinate systems, including the
   $1/r$ and $1/(r\sin\theta)$ factors, and say why an inverse transpose appears.
5. **Propagate** a covariance matrix through a nonlinear coordinate change using
   $\mathbf{C}_y \approx \mathbf{J}\,\mathbf{C}_x\,\mathbf{J}^{\mathsf T}$, and
   state precisely when that linearisation is trustworthy.
6. **Identify** where a transformation fails: points of non-invertibility, the
   singularities of spherical coordinates, and the branch and datum choices in
   geographic coordinates.

## Prerequisites

- [01-06-01 Partial Derivatives, Gradients and Directional Derivatives](./01-partial-derivatives.md)
  — the Jacobian's entries are partial derivatives, and the gradient
  transformation is a corollary of the chain rule derived there.
- [01-06-02 Multiple Integrals and Change of Variables](./02-multiple-integrals.md)
  — the Jacobian determinant appears there as a factor in an integral; here it
  is derived rather than quoted.
- [01-07-02 Matrices, Matrix Multiplication and Linear Maps](../07-linear-algebra/02-matrices-and-operations.md)
  — the Jacobian is a matrix and the chain rule is matrix multiplication.
- [01-13-09 Error and Uncertainty Propagation](../13-probability-and-statistics-foundations/09-error-propagation.md) —
  the statistics behind the covariance transformation of Section 4.5.

## 1. Intuition: a coordinate system is an instrument, and every instrument distorts

You cannot integrate density over an ore body without deciding what
coordinates to use. The choice is not cosmetic. It determines whether the limits
are constants or functions, whether the arithmetic is three lines or three
pages, and whether the answer is limited by the discretisation or by round-off.

The Jacobian is the price of the choice. It answers one question:

> If I move by one unit in each *coordinate*, how much physical space do I
> actually cover, and in which directions?

Three facts make the whole lesson:

1. The **Jacobian matrix** is the local linearisation of a coordinate map. It is
   the best linear approximation of a curved transformation at a point.
2. Its **determinant** is the local volume scale factor — the ratio of physical
   volume to coordinate volume — and that single number is what appears in every
   integral.
3. Its **entries** are the partial derivatives that transform derivatives,
   and they are the same numbers that transform uncertainties.

One object, three uses. That economy is why the Jacobian is worth a lesson of
its own rather than a footnote in a change-of-variables section.

## 2. Precise definitions

### 2.1 The Jacobian matrix

Let $\mathbf{g}: (u_1,\dots,u_n) \mapsto (x_1,\dots,x_n)$ be a differentiable
map. Its **Jacobian matrix** at a point is

$$\mathbf{J} = \frac{\partial(x_1,\dots,x_n)}{\partial(u_1,\dots,u_n)}
= \begin{pmatrix}
\dfrac{\partial x_1}{\partial u_1} & \cdots & \dfrac{\partial x_1}{\partial u_n} \\[2mm]
\vdots & \ddots & \vdots \\[2mm]
\dfrac{\partial x_n}{\partial u_1} & \cdots & \dfrac{\partial x_n}{\partial u_n}
\end{pmatrix},
\qquad J_{ij} = \frac{\partial x_i}{\partial u_j}.$$

Rows are output components, columns are input coordinates. Its **Jacobian
determinant** is written $\det \mathbf{J}$ or, confusingly but conventionally,
$\partial(x_1,\dots,x_n)/\partial(u_1,\dots,u_n)$ — the same symbol as the
matrix. In this lesson the notation is spelled out whenever it matters.

### 2.2 The linear approximation

Differentiability means that near a point $\mathbf{u}_0$,

$$\mathbf{g}(\mathbf{u}_0 + \delta\mathbf{u}) \approx \mathbf{g}(\mathbf{u}_0)
+ \mathbf{J}(\mathbf{u}_0)\, \delta\mathbf{u},
\qquad
\delta\mathbf{x} \approx \mathbf{J}\,\delta\mathbf{u},$$

with an error that is $o(\lvert\delta\mathbf{u}\rvert)$. Everything in
Sections 3 and 4 is this one statement used repeatedly. The image of a small
coordinate box is, to first order, a parallelepiped whose volume is
$\lvert \det \mathbf{J} \rvert$ times the volume of the box.

### 2.3 The inverse function theorem

If $\det \mathbf{J} \neq 0$ at $\mathbf{u}_0$, then $\mathbf{g}$ is invertible
in some neighbourhood of $\mathbf{u}_0$, and the inverse map has Jacobian
$\mathbf{J}^{-1}$. If $\det \mathbf{J} = 0$, the map is locally degenerate: it
flattens an $n$-dimensional region into something of lower dimension, and no
unique inverse exists.

**This is not a technicality.** It is exactly the statement that spherical
coordinates fail on the polar axis, that longitude is undefined at the North
Pole, and that a map projection is not invertible at its singular point. Section
4.6 gives the geophysical consequences.

### 2.4 Orientation

The sign of $\det \mathbf{J}$ records whether the map preserves or reverses
handedness. A right-handed $(u,v,w)$ mapped to a right-handed $(x,y,z)$ gives a
positive determinant; swapping two axes flips the sign. Volume integrals use the
absolute value; surface integrals of a flux do **not**, because swapping the
orientation of a surface is precisely a sign change in the flux. This distinction
becomes essential in Lesson 05.

## 3. Derivations

### 3.1 The determinant as a volume ratio

Take a small box in coordinate space with sides $\Delta u_1, \dots, \Delta u_n$
aligned with the coordinate axes. Its image under $\mathbf{g}$ is, to first
order, the parallelepiped spanned by the vectors
$\mathbf{J}_{1}\Delta u_1, \dots, \mathbf{J}_{n}\Delta u_n$, where
$\mathbf{J}_{j}$ is the $j$-th column of $\mathbf{J}$. The volume of a
parallelepiped spanned by columns is the absolute value of the determinant of the
matrix they form. Hence

$$\Delta V_{\text{physical}} = \lvert \det \mathbf{J} \rvert \,
\Delta u_1 \cdots \Delta u_n + o(\text{volume}).$$

Refining the partition and summing gives the change-of-variables formula of
[01-06-02](./02-multiple-integrals.md). $\square$

In one dimension this is the familiar substitution rule
$\int f(x)\,dx = \int f(x(u))\, \lvert dx/du \rvert\, du$: the "Jacobian" is
$dx/du$, and the absolute value is there for the same reason.

### 3.2 Determinants multiply along a chain

If $\mathbf{x} = \mathbf{f}(\mathbf{y})$ and $\mathbf{y} = \mathbf{g}(\mathbf{u})$,
then the chain rule in matrix form is

$$\mathbf{J}_{\mathbf{f}\circ\mathbf{g}} = \mathbf{J}_{\mathbf{f}}\,
\mathbf{J}_{\mathbf{g}},$$

and therefore, by multiplicativity of the determinant,

$$\det \mathbf{J}_{\mathbf{f}\circ\mathbf{g}}
= \det \mathbf{J}_{\mathbf{f}} \cdot \det \mathbf{J}_{\mathbf{g}}.$$

Practically: **convert in two steps and multiply the two volume factors.** Going
from spherical to Cartesian via cylindrical, for instance, the factors are
$r$ and $r\sin\theta$-style corrections that compose into $r^2\sin\theta$. It is
also a useful check: if your composed scale factor is not the product of the
individual ones, one of the determinants is wrong.

### 3.3 Spherical coordinates, determinant computed

Let $x = r\sin\theta\cos\phi$, $y = r\sin\theta\sin\phi$, $z = r\cos\theta$. Then

$$\mathbf{J} = \begin{pmatrix}
\sin\theta\cos\phi & r\cos\theta\cos\phi & -r\sin\theta\sin\phi \\
\sin\theta\sin\phi & r\cos\theta\sin\phi & \phantom{-}r\sin\theta\cos\phi \\
\cos\theta & -r\sin\theta & 0
\end{pmatrix}.$$

Expanding along the third row,

$$\det \mathbf{J}
= \cos\theta\left(r^2\sin^2\theta\cos^2\phi + r^2\sin^2\theta\sin^2\phi\right)
+ r\sin\theta\left(r\sin^2\theta\cos^2\phi + r\sin^2\theta\sin^2\phi\right),$$

and since $\cos^2\phi + \sin^2\phi = 1$ in both brackets,

$$\det \mathbf{J} = r^2\sin\theta\cos^2\theta + r^2\sin^3\theta
= r^2\sin\theta\left(\cos^2\theta + \sin^2\theta\right) = r^2\sin\theta .$$

Hence

$$dV = r^2\sin\theta\, dr\, d\theta\, d\phi,$$

with the same geometric reading as in [01-06-02](./02-multiple-integrals.md):
$dr$, $r\,d\theta$ and $r\sin\theta\, d\phi$ are the three side lengths.

The determinant vanishes where $r = 0$ or $\sin\theta = 0$. At $r = 0$ the
origin is represented once, not once per $(\theta,\phi)$; along the polar axis
the longitude $\phi$ is free. Notice what happens in the integral: at the axis
the factor $\sin\theta$ also makes the integrand vanish, so the coordinate
redundancy is harmless *for an integral* and harmless *for a smooth field*, but
not harmless for a grid-based solver, where it produces a singular matrix.

### 3.4 Transforming the gradient

Let $f$ be a scalar field expressed both in Cartesian coordinates
$(x_1,x_2,x_3)$ and in some coordinates $(u_1,u_2,u_3)$ with Jacobian
$\mathbf{J}$, $J_{ij} = \partial x_i/\partial u_j$. The chain rule gives, for
each $u_j$,

$$\frac{\partial f}{\partial u_j}
= \sum_i \frac{\partial f}{\partial x_i}\frac{\partial x_i}{\partial u_j}
= \sum_i (\nabla_x f)_i\, J_{ij},
\qquad\text{that is}\qquad
\nabla_u f = \mathbf{J}^{\mathsf T} \nabla_x f .$$

Inverting,

$$\boxed{\;\nabla_x f = \left(\mathbf{J}^{\mathsf T}\right)^{-1} \nabla_u f
= \left(\mathbf{J}^{-1}\right)^{\mathsf T} \nabla_u f\;}$$

The inverse *transpose* appears, not the inverse. This is the most commonly
mis-remembered formula in the whole subject, and it is why the spherical gradient
has $1/r$ and $1/(r\sin\theta)$ rather than $r$ and $r\sin\theta$: the inverse
Jacobian divides by the length scale, and then the transpose redistributes the
factors into the right components. Writing
$\nabla_u f = (\partial f/\partial r, \partial f/\partial\theta, \partial f/\partial\phi)$,

$$(\mathbf{J}^{-1})^{\mathsf T} =
\begin{pmatrix}
1 & 0 & 0\\
0 & 1/r & 0\\
0 & 0 & 1/(r\sin\theta)
\end{pmatrix}
\quad\Longrightarrow\quad
\nabla_x f = \frac{\partial f}{\partial r}\hat{r}
+ \frac{1}{r}\frac{\partial f}{\partial\theta}\hat{\theta}
+ \frac{1}{r\sin\theta}\frac{\partial f}{\partial\phi}\hat{\phi}.$$

Section 5.4 checks each component against a Cartesian computation.

### 3.5 Transforming a covariance

Let $\mathbf{x}$ be a random vector with covariance
$\mathbf{C}_x = \mathrm{E}[(\mathbf{x}-\bar{\mathbf{x}})(\mathbf{x}-\bar{\mathbf{x}})^{\mathsf T}]$,
and let $\mathbf{y} = \mathbf{g}(\mathbf{x})$. Setting
$\delta\mathbf{y} \approx \mathbf{J}\delta\mathbf{x}$ and taking expectations,

$$\mathbf{C}_y \approx \mathbf{J}\, \mathbf{C}_x\, \mathbf{J}^{\mathsf T}.$$

Note the shape of the formula: the transformation is a **congruence**
transformation, so $\mathbf{C}_y$ is symmetric whenever $\mathbf{C}_x$ is. In
the special case $\mathbf{C}_x = \sigma^2\mathbf{I}$ the result is
$\mathbf{C}_y = \sigma^2\mathbf{J}\mathbf{J}^{\mathsf T}$, whose eigenvalues are
$\sigma^2$ times the squared singular values of $\mathbf{J}$. A coordinate change
can rotate an uncertainty ellipsoid and stretch it, but it cannot create
certainty: when $\mathbf{J}$ is invertible,
$\det\mathbf{C}_y = (\det\mathbf{J})^2\det\mathbf{C}_x$, so a singular
$\mathbf{C}_x$ stays singular.

**When the linearisation is valid.** The neglected term is
$\tfrac12 \delta\mathbf{x}^{\mathsf T} \mathbf{H}_k \delta\mathbf{x}$ for each
output component $k$. Write $L$ for the length scale on which $\mathbf{g}$
curves, and $\sigma$ for the size of the perturbation. The linearisation is safe
when $\sigma \ll L$. If it is not, the higher-order terms produce a **bias** in
the mean as well as a change in the spread, and Monte Carlo is the honest tool
(see [01-13-09](../13-probability-and-statistics-foundations/09-error-propagation.md)).
Section 5.5 measures both routes on a case where the linearisation happens to be
excellent, and the agreement between them is what licenses using it.

### 3.6 Worked example: geodetic against geocentric latitude

Geodetic latitude $\varphi$ is the angle between the ellipsoid normal and the
equatorial plane; geocentric latitude $\psi$ is the angle between the radius
vector to a point and the equatorial plane. They differ because the Earth is
flattened. With $e^2$ the first eccentricity squared,

$$\tan\psi = \left(1 - e^2\right)\tan\varphi, \qquad 1 - e^2 = (1-f)^2,$$

where $f$ is the flattening. This is a one-dimensional nonlinear map
$\varphi \mapsto \psi$, and its Jacobian is the single derivative

$$\frac{d\psi}{d\varphi}
= (1-e^2)\frac{\sec^2\varphi}{\sec^2\psi}
= (1-e^2)\frac{1 + \tan^2\varphi}{1 + (1-e^2)^2\tan^2\varphi}.$$

Using the flattening of the WGS84 ellipsoid, $f = 1/298.257223563$ — the
defining value published in the standard; always confirm ellipsoid constants
against the current official definition before using them in production — the
map gives:

| $\varphi$ (deg) | $\psi$ (deg) | $\varphi - \psi$ (arcmin) | $d\psi/d\varphi$ |
|---|---|---|---|
| 0 | 0.00000 | 0.0000 | 0.99331 |
| 15 | 14.90407 | 5.7560 | 0.99419 |
| 30 | 29.83364 | 9.9819 | 0.99663 |
| 45 | 44.80758 | 11.5454 | 0.99998 |
| 60 | 59.83308 | 10.0154 | 1.00335 |
| 75 | 74.90351 | 5.7896 | 1.00583 |
| 90 | 90.00000 | 0.0000 | 0.99331 |

Two readings, both important in practice.

- The difference reaches **11.5 arcmin** — about $0.19^\circ$, or roughly 21 km
  on the ground — near $45^\circ$ latitude. A geocentric and a geodetic latitude
  can therefore never be used interchangeably, and the error is smooth and
  latitude-dependent, not random.
- The Jacobian stays within $0.6\%$ of unity. The map is very nearly
  **isometric**: it barely changes length scales. What it does instead is
  **offset** them. A near-unit Jacobian with a nonzero offset is exactly the kind
  of error that survives quality control, because every individual comparison
  looks fine.

## 4. Physical interpretation

**Geodesy is applied Jacobians.** Converting between geocentric Cartesian,
geodetic and local topocentric frames — a routine operation inside every
GNSS processing package — is a composition of Jacobians, and the accumulated
determinant is the volume scale factor used in geodetic boundary-value problems.
See [07-04 Geodesy and Reference Frames](../../07-gravity-geodesy/04-geodesy-reference-frames/README.md).

**Map projections are maps, with maps' pathologies.** A projection from the
sphere to the plane has a position-dependent Jacobian. Its singular values give
the local stretch in the two principal directions; a conformal projection has
equal singular values (no shape distortion) and varying determinant (area
distortion); an equal-area projection has constant determinant and varying
singular values (shape distortion). This is the entire theory of projection
distortion, and it is a statement about one matrix.

**Uncertainty transformation is the daily use.** A GNSS solution comes with a
covariance matrix in a local frame. Every time it is rotated into another frame,
resampled onto a grid, or converted from polar to Cartesian, the covariance must
be transformed with $\mathbf{J}\,\mathbf{C}\,\mathbf{J}^{\mathsf T}$. Failing to
do so produces uncertainty ellipses that are the wrong shape and, because
$\mathbf{C}$ is not diagonal after the change, correlated errors that subsequent
least-squares stages then treat as independent.
[18-02-06 Data Weighting and Error Covariance Specification](../../18-inverse-problems/02-linear-inverse-problems/06-weighting-and-covariance.md)
shows what goes wrong downstream.

**Tensors do not transform like vectors.** The gradient formula of Section 3.4
involves $\mathbf{J}^{-1}$ transposed, and a divergence involves still another
combination. A second-order tensor — stress, strain, the gravity gradient
tensor — transforms with $\mathbf{J}$ acting on *both* indices. This is why the
tensor algebra of
[01-15-02 Tensor Algebra, Transformation Laws and Invariants](../15-tensors-and-differential-geometry/02-tensor-algebra.md)
is a separate subject rather than a corollary of this lesson.

**Where the transformation is singular, so is your data.** Longitude is
undefined at the poles; a grid of $\phi$ values near a pole collapses; the
horizontal components of a magnetic field are meaningless there. Every one of
these is $\det\mathbf{J} = 0$ wearing a geological hat.

## 5. Python demonstration

The companion script
[`code/jacobian_transformations.py`](./code/jacobian_transformations.py) checks
each claim numerically, including the covariance transformation against Monte
Carlo. It uses only the standard library.

### 5.1 Determinants from finite differences

```text
polar        (r,theta)    -> (x,y)
   at (3.0, 0.7):  numeric det J = 3.000000001   analytic = 3.000000000   rel. diff = 2.266e-10
cylindrical  (rho,phi,z)  -> (x,y,z)
   at (3.0, 0.7, 1.5):  numeric det J = 3.000000000   analytic = 3.000000000   rel. diff = 1.444e-10
spherical    (r,theta,phi)-> (x,y,z)
   at (3.0, 0.7, 1.5):  numeric det J = 5.797959186   analytic = 5.797959185   rel. diff = 1.060e-10
```

The determinants were formed from finite differences of the *map*, not from the
formulas being tested. For the spherical case, $r^2\sin\theta = 9\times
\sin(0.7) = 5.797959\dots$, and the numerical value agrees to ten significant
figures.

### 5.2 The determinant doing the work of an integral

```text
spherical element, r^2 sin(theta) dr dtheta dphi = 4.1887901393
Cartesian Monte Carlo, 400000 samples          = 4.1881000000
exact 4*pi/3                                     = 4.1887902048
```

Same volume, two coordinate systems: one integral in the right coordinates, one
sampling in the wrong ones. The quadrature is accurate to $1.6\times10^{-8}$;
the Monte Carlo to roughly $1/\sqrt{N} = 1.6\times10^{-3}$.

### 5.3 A shell integral, against the closed form

```text
shell 6.0e+05 m < r < 1.2e+06 m, rho = 2700 kg/m^3
numeric 4*pi*rho*r^2 dr                  = 1.710032e+22 kg
exact 4*pi*rho*(b^3-a^3)/3               = 1.710032e+22 kg
relative difference                      = 8.929e-11
```

The $r^2$ in the integrand is the Jacobian determinant. Delete it and the result
has the wrong units; get it wrong by a factor of $r$ and the answer is off by
the outer radius.

### 5.4 The gradient in spherical coordinates, component by component

The script computes $\nabla f$ in Cartesian coordinates at a point
$r = 5\times10^6$ m, $\theta = 0.9$, $\phi = 1.2$, projects it onto the
orthonormal spherical basis, and compares with the formula of Section 3.4:

```text
component   grad f . e_i (from Cartesian)   formula   relative difference
       r      -4.9777090408e-06     -4.9777090396e-06     2.306e-10
   theta       2.0711493045e-05      2.0711493042e-05     1.348e-10
     phi       6.6553061859e-06      6.6553061875e-06     2.394e-10
```

Three components, three parts in $10^{10}$. The $1/r$ and $1/(r\sin\theta)$
factors are confirmed for the field used.

### 5.5 Covariance propagation: the Jacobian against Monte Carlo

A station at $r = 6.371\times10^6$ m (a conventional mean Earth radius),
$\theta = \pi/4$, $\phi = \pi/6$ has independent coordinate uncertainties
$\sigma_r = 5$ m, $\sigma_\theta = \sigma_\phi = 10^{-6}$ rad. The transformed
Cartesian covariance is computed twice: analytically as
$\mathbf{J}\,\mathbf{C}\,\mathbf{J}^{\mathsf T}$, and by drawing 500 000 samples
and forming the sample covariance.

```text
Cartesian covariance from J C J^T  (m^2):
    2.9670e+01   5.4127e+00  -6.7505e+00
    5.4127e+00   2.3420e+01  -3.8974e+00
   -6.7505e+00  -3.8974e+00   3.2795e+01
Cartesian covariance from Monte Carlo (m^2):
    2.9688e+01   5.3983e+00  -6.8002e+00
    5.3983e+00   2.3541e+01  -3.9011e+00
   -6.8002e+00  -3.9011e+00   3.2806e+01
diagonal relative differences between the two:
   sigma_x^2: 2.9670e+01 vs 2.9688e+01   relative difference = 6.000e-04
   sigma_y^2: 2.3420e+01 vs 2.3541e+01   relative difference = 5.153e-03
   sigma_z^2: 3.2795e+01 vs 3.2806e+01   relative difference = 3.358e-04
Monte Carlo noise floor on a variance is sqrt(2/N) = 2.000e-03 in relative terms.
```

Three observations worth more than the numbers.

1. **The off-diagonal terms are not small.** The covariance is about
   $5.4\ \mathrm{m^2}$ against variances near $24\ \mathrm{m^2}$, a correlation
   of about $0.21$. A pipeline that keeps only the diagonal has discarded that
   correlation, and every later least-squares stage will then treat correlated
   errors as independent.
2. **The diagonal entries are all around 24–33 m²**, whereas the input
   uncertainties were 5 m radial and 6.4 m tangential. The transformation has
   redistributed the uncertainty but not changed its total order of magnitude.
3. **The Monte Carlo differences are at the noise floor**, which the script
   prints as $\sqrt{2/N} = 2.0\times10^{-3}$. The largest observed difference,
   $5.2\times10^{-3}$, is about $2.6$ standard errors — consistent with noise,
   and a useful reminder that "the two methods disagree by 0.5%" is not evidence
   of a bug when the estimator's own uncertainty is 0.2%.

> **Breaking exercise.** Increase $\sigma_\theta$ and $\sigma_\phi$ to
> $10^{-3}$ rad and predict, before running, whether the linearised
> $\mathbf{J}\mathbf{C}\mathbf{J}^{\mathsf T}$ will still match the Monte Carlo
> result. At $r = 6.371\times10^6$ m a $10^{-3}$ rad angular error is 6.4 km of
> arc; work out the size of the neglected second-order term before you run it.

## 6. Exercises

Ten graded exercises are in
[`exercises/03-jacobians-exercises.md`](./exercises/03-jacobians-exercises.md)
and worked solutions in
[`exercises/03-jacobians-solutions.md`](./exercises/03-jacobians-solutions.md).

## 7. Common mistakes

1. **Using $\mathbf{J}$ instead of $(\mathbf{J}^{-1})^{\mathsf T}$ to transform a
   gradient.** The two agree only in the trivial case $\mathbf{J} = \mathbf{I}$.
   Section 3.4 exists because this error is so common.
2. **Confusing the matrix with its determinant.** They share the symbol
   $\partial(x,y,z)/\partial(r,\theta,\phi)$ and nothing else.
3. **Forgetting the absolute value in a volume integral, and adding it where it
   does not belong in a flux.** Orientation matters for surfaces; volume is
   positive.
4. **Assuming a transformation is invertible everywhere because it is invertible
   almost everywhere.** Spherical coordinates are not invertible at $r=0$ or
   $\sin\theta=0$, and that is a real numerical problem on a lat–long grid.
5. **Leaving correlations out of a covariance after a coordinate change.** The
   off-diagonal terms in Section 5.5 are not small.
6. **Applying $\mathbf{J}\mathbf{C}\mathbf{J}^{\mathsf T}$ when the
   linearisation is invalid.** The signal is that the perturbation is comparable
   to the curvature scale of the map; the remedy is Monte Carlo, and the
   consequence of ignoring it is a systematic bias, not merely extra spread.
7. **Quoting and using ellipsoid parameters from memory.** Datums change and
   definitions are amended; take constants from the official definition, not
   from a lecture note.
8. **Assuming geodetic and geocentric latitude agree.** They differ by up to
   11.5 arcmin, as Section 3.6 shows.

## 8. Real-world applications

- **GNSS and geodetic coordinate conversion.** Every receiver solution is in a
  Cartesian frame and every map is in a geodetic one; the conversion is a
  composition of Jacobians, and its determinant is the local volume factor. See
  [07-04 Geodesy and Reference Frames](../../07-gravity-geodesy/04-geodesy-reference-frames/README.md).
- **Map projections and survey grids.** Area and shape distortion are the
  singular values and determinant of the projection Jacobian. Choosing a
  projection is choosing which distortion to accept, and that choice should be
  based on the operation being performed — measuring area favour of an
  equal-area projection, measuring angle a conformal one.
- **Uncertainty budgets in geophysics.** Transforming a gravity station's
  position covariance into a frame in which the survey is gridded; resampling an
  airborne magnetic dataset with its error covariance; converting moment-tensor
  uncertainties between frames.
- **Grid design.** The Jacobian determinant is why a uniform lat–long grid
  oversamples the poles, and why spherical harmonic analysis is done with
  weighted quadrature rather than by averaging grid values.
- **Spherical harmonic analysis of the gravity and magnetic fields.** The
  orthogonality relations used to solve for the coefficients carry the
  $\sin\theta$ factor of the Jacobian; omitting it biases the low-degree
  coefficients. See
  [07-05-03 Spherical Harmonic Solutions and Coefficient Interpretation](../../07-gravity-geodesy/05-satellite-gravimetry/03-spherical-harmonic-solutions.md).
- **Moment-tensor and focal-mechanism conversions.** A tensor transforms with
  two Jacobian factors, and doing it with one gives a plausible-looking but
  wrong mechanism; see
  [01-15-03 Strain and Stress Tensors as Physical Tensors](../15-tensors-and-differential-geometry/03-strain-and-stress-tensors.md).

## 9. Further reading

- **Marsden, J. E., & Tromba, A. *Vector Calculus.* W. H. Freeman.** The
  inverse function theorem and the change-of-variables theorem in the form used
  here. Level: intermediate. Check your library for the current edition.
- **Spivak, M. *Calculus on Manifolds.* Addison-Wesley.** The Jacobian as the
  derivative of a map between normed spaces, and the determinant as the volume
  factor. Level: advanced.
- **Hofmann-Wellenhof, B., & Moritz, H. *Physical Geodesy.* Springer.** The
  standard treatment of geodetic coordinate systems and of the transformations
  of Section 3.6, written by geodesists for geodesists. Level: graduate.
- **Snyder, J. P. *Map Projections: A Working Manual.* US Geological Survey
  Professional Paper 1395.** The classic reference on projections, including
  the distortion formulas that follow from the projection Jacobian. Level:
  intermediate. Published by the USGS; check current availability.
- **Telford, W. M., Geldart, L. P., & Sheriff, R. E. (1990). *Applied
  Geophysics* (2nd ed.). Cambridge University Press.** Coordinate conventions and
  field-component definitions used in survey practice. Level: intermediate.

> Note on citations: bibliographic details above are given so that you can
> locate the works. This repository does not host or reproduce copyrighted text,
> and you should confirm editions and current availability through your library
> before citing them yourself.

## 10. Related lessons

- [01 Partial Derivatives, Gradients and Directional Derivatives](./01-partial-derivatives.md) —
  the gradient, whose transformation is derived here.
- [02 Multiple Integrals and Change of Variables](./02-multiple-integrals.md) —
  the integral whose factor is the determinant derived here.
- [04 Divergence, Curl and Physical Meaning](./04-divergence-and-curl.md) — the
  first-order operators that inherit their coordinate forms from this lesson.
- [07 Vector Identities and Their Role in Geophysics](./07-vector-identities.md) —
  identities that must hold in every coordinate system.
- [01-04-03 Cartesian, Cylindrical and Spherical Coordinates](../04-geometry-and-coordinates/03-cartesian-spherical.md) —
  the geometry of the three systems.
- [01-15-04 Differential Operators in Curvilinear Coordinates](../15-tensors-and-differential-geometry/04-curvilinear-coordinates.md) —
  the general machinery for arbitrary coordinates.
- [18-02-06 Data Weighting and Error Covariance Specification](../../18-inverse-problems/02-linear-inverse-problems/06-weighting-and-covariance.md) —
  what goes wrong when covariances are transformed carelessly.

## Self-assessment checklist

- [ ] I can write the Jacobian matrix of a given map, with rows as outputs.
      (Section 2.1)
- [ ] I can derive $dV = r^2\sin\theta\,dr\,d\theta\,d\phi$ by expanding the
      determinant. (Section 3.3)
- [ ] I can explain the small-box argument for why the determinant is a volume
      ratio. (Section 3.1)
- [ ] I can state why determinants multiply along a chain and use that as a check
      on a two-step conversion. (Section 3.2)
- [ ] I can transform a gradient between coordinate systems and explain why an
      inverse transpose appears. (Section 3.4)
- [ ] I can transform a covariance matrix and name the conditions under which
      the linearisation fails. (Section 3.5)
- [ ] I can explain what a zero Jacobian determinant means physically in a
      geodetic context. (Sections 2.3, 4)
- [ ] I can state the maximum discrepancy between geodetic and geocentric
      latitude and why it is systematic. (Section 3.6)
- [ ] I can say why a near-unity Jacobian can still hide a serious error.
      (Section 3.6)
