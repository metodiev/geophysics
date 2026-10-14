# Solutions — 01-06-03 Jacobians, Coordinate Transformations and Volume Elements

> **Read this after attempting the exercises, not before.**
>
> Every determinant quoted as "numeric" below was computed by finite differences
> of the map itself, not from the formula it is being used to check.

---

## ★1 — Jacobians of four maps

**(a)** $x = 2u+v$, $y = u-3v$:

$$\mathbf{J} = \begin{pmatrix} 2 & 1 \\ 1 & -3\end{pmatrix}, \qquad
\det\mathbf{J} = -6 - 1 = -7 .$$

The map is linear, so the determinant is constant: it stretches areas by 7 and
reverses orientation.

**(b)** $x = uv$, $y = u/v$:

$$\mathbf{J} = \begin{pmatrix} v & u \\ \tfrac{1}{v} & -\tfrac{u}{v^2}\end{pmatrix},
\qquad
\det\mathbf{J} = v\left(-\frac{u}{v^2}\right) - u\left(\frac{1}{v}\right)
= -\frac{2u}{v}.$$

The determinant vanishes on $u = 0$, where the map collapses the $u$-axis to a
point; the map is not invertible there.

**(c)** $x = r\cos\theta$, $y = r\sin\theta$:

$$\mathbf{J} = \begin{pmatrix} \cos\theta & -r\sin\theta \\ \sin\theta & r\cos\theta
\end{pmatrix}, \qquad
\det\mathbf{J} = r\cos^2\theta + r\sin^2\theta = r .$$

**(d)** $x = \rho\cos\phi$, $y = \rho\sin\phi$, $z = z$:

$$\mathbf{J} = \begin{pmatrix} \cos\phi & -\rho\sin\phi & 0\\ \sin\phi & \rho\cos\phi & 0\\ 0&0&1\end{pmatrix},
\qquad \det\mathbf{J} = \rho .$$

Note that (c) and (d) are the same $2\times2$ block: the cylindrical map is the
polar map with an inert third coordinate.

---

## ★2 — The spherical determinant

$$\mathbf{J} = \begin{pmatrix}
\sin\theta\cos\phi & r\cos\theta\cos\phi & -r\sin\theta\sin\phi \\
\sin\theta\sin\phi & r\cos\theta\sin\phi & \phantom{-}r\sin\theta\cos\phi \\
\cos\theta & -r\sin\theta & 0
\end{pmatrix}.$$

Expanding along the third row, whose entries are $\cos\theta$, $-r\sin\theta$
and $0$,

$$\det\mathbf{J} = \cos\theta\,M_{31} + r\sin\theta\,M_{32},$$

where $M_{3j}$ is the minor obtained by deleting row 3 and column $j$:

$$M_{31} = \det\begin{pmatrix} r\cos\theta\cos\phi & -r\sin\theta\sin\phi\\
r\cos\theta\sin\phi & r\sin\theta\cos\phi\end{pmatrix}
= r^2\sin\theta\cos\theta\left(\cos^2\phi + \sin^2\phi\right)
= r^2\sin\theta\cos\theta,$$

$$M_{32} = \det\begin{pmatrix} \sin\theta\cos\phi & -r\sin\theta\sin\phi\\
\sin\theta\sin\phi & \phantom{-}r\sin\theta\cos\phi\end{pmatrix}
= r\sin^2\theta\cos^2\phi + r\sin^2\theta\sin^2\phi
= r\sin^2\theta .$$

Therefore

$$\det\mathbf{J} = r^2\sin\theta\cos^2\theta + r^2\sin^3\theta
= r^2\sin\theta\left(\cos^2\theta + \sin^2\theta\right)
= r^2\sin\theta . $$

**Numerical confirmation** (from
[`../code/jacobian_transformations.py`](../code/jacobian_transformations.py)): at
$(r,\theta,\phi) = (3, 0.7, 1.5)$ the finite-difference determinant is
$5.797959186$ against $r^2\sin\theta = 5.797959185$, a relative difference of
$1.06\times10^{-10}$.

**Where it vanishes.** $r = 0$ (the origin is one point represented by every
$(\theta,\phi)$) and $\sin\theta = 0$ (the polar axis is one line represented by
every $\phi$). Both are genuine coordinate singularities: the map is not
invertible there, and no amount of numerical care changes that.

---

## ★3 — Volume of an ellipsoid

Substitute

$$x = au, \qquad y = bv, \qquad z = cw .$$

The Jacobian matrix is diagonal with entries $(a,b,c)$, so

$$\det\mathbf{J} = abc,$$

and the region $x^2/a^2+y^2/b^2+z^2/c^2 \le 1$ becomes the unit ball
$u^2+v^2+w^2 \le 1$. Hence

$$V = \iiint_{\text{ellipsoid}}dx\,dy\,dz
= abc\iiint_{\text{unit ball}}du\,dv\,dw
= \frac{4}{3}\pi abc .$$

---

## ★4 — Uniform scaling

The Jacobian of $\mathbf{x}\mapsto\lambda\mathbf{x}$ is $\lambda\mathbf{I}$, so
$\det\mathbf{J} = \lambda^n$ in $n$ dimensions, and volumes scale by
$\lambda^n$ — as they must, since scaling a length by $\lambda$ scales a $d$-dimensional
volume by $\lambda^d$.

The ellipsoid of ★3 is the image of the unit ball under the scaling
$(u,v,w)\mapsto(au,bv,cw)$, so its volume is $abc$ times the unit ball's:
$abc\cdot\tfrac{4}{3}\pi$, agreeing with the direct computation. **Two routes to
the same formula is the point.** The determinant is what makes the scaling
argument legitimate, since the map is linear.

---

## ★★5 — GNSS position uncertainty transformed to Cartesian

**(a)** Using colatitude $\theta = \pi/2 - \varphi = 45^\circ$ and
$x = (R+h)\sin\theta\cos\lambda$, $y = (R+h)\sin\theta\sin\lambda$,
$z = (R+h)\cos\theta$ with $\lambda = 0$, the Jacobian at $(R,\theta,\lambda) =
(6.371\times10^6,\ 0.785398,\ 0)$ is

$$\mathbf{J} = \begin{pmatrix}
\sin\theta\cos\lambda & R\cos\theta\cos\lambda & -R\sin\theta\sin\lambda\\
\sin\theta\sin\lambda & R\cos\theta\sin\lambda & \phantom{-}R\sin\theta\cos\lambda\\
\cos\theta & -R\sin\theta & 0
\end{pmatrix}
= \begin{pmatrix}
7.0711\times10^{-1} & 4.50498\times10^{6} & 0\\
0 & 0 & 4.50498\times10^{6}\\
7.0711\times10^{-1} & -4.50498\times10^{6} & 0
\end{pmatrix}.$$

**(b)** With $\mathbf{C} = \mathrm{diag}(\sigma_r^2,\sigma_\theta^2,\sigma_\lambda^2)
= \mathrm{diag}(10^{-4}, 10^{-16}, 10^{-16})$ and
$\mathbf{C}_y = \mathbf{J}\mathbf{C}\mathbf{J}^{\mathsf T}$ (all in m²):

$$\mathbf{C}_y = \begin{pmatrix}
2.0795\times10^{-3} & 0 & -1.9794\times10^{-3}\\
0 & 2.0295\times10^{-3} & 0\\
-1.9794\times10^{-3} & 0 & 2.0795\times10^{-3}
\end{pmatrix}.$$

So $\sigma_x = \sigma_z = 0.04560$ m and $\sigma_y = 0.04505$ m.

**(c)** Reading this in the local frame is more informative. The three input
uncertainties convert to local displacements of

$$\sigma_E = R\sin\theta\,\sigma_\lambda = 0.04505\ \mathrm{m}, \quad
\sigma_N = R\,\sigma_\theta = 0.06371\ \mathrm{m}, \quad
\sigma_U = \sigma_h = 0.010\ \mathrm{m}.$$

The **horizontal** uncertainty is therefore 4.5 to 6.4 times larger than the
vertical one, and the horizontal *variance* exceeds the vertical by a factor of
20 to 41. The Cartesian components come out at 0.045 m each because they are a
45° rotation of the local frame, which mixes the 0.0637 m north component with
the 0.010 m up component.

**Two lessons.**

1. **The Jacobian is what converts an angular precision into a length.** A very
   precise-looking $10^{-8}$ rad is 6.4 cm on the Earth's surface. Angular
   uncertainties are only interpretable once multiplied by a radius.
2. **The off-diagonal terms are not negligible.** $C_{xz}$ is $-1.98\times10^{-3}$
   m², comparable to the diagonal entries, because the radial and north
   displacements mix into $x$ and $z$ at 45° latitude. A pipeline that keeps only
   the diagonal has discarded structure of the same size as the structure it
   keeps.

**A caution on the convention.** I used colatitude, so the middle coordinate is
$\theta$, not the geodetic latitude $\varphi$; the Jacobian changes form if you
use the other convention. This is not pedantry: it is the most common source of
sign and factor errors in geodetic code (see
[01-06-03](../03-jacobians.md) Section 3.6 for the geodetic–geocentric
distinction).

---

## ★★6 — Local area distortion of a cylindrical projection

**(a)** Near latitude $\theta$ (colatitude), the map sends
$(\phi,\theta)\mapsto(u,v) = (R\phi,\ R(\pi/2-\theta))$. The Jacobian is

$$\mathbf{J} = \begin{pmatrix}
\partial u/\partial\phi & \partial u/\partial\theta\\
\partial v/\partial\phi & \partial v/\partial\theta
\end{pmatrix}
= \begin{pmatrix} R & 0\\ 0 & -R\end{pmatrix},
\qquad \det\mathbf{J} = -R^2 .$$

**(b)** The determinant gives the ratio of map area to $(\phi,\theta)$ area:
$\lvert\det\mathbf{J}\rvert = R^2$ per unit $(\phi,\theta)$. The true sphere
element is $R^2\sin\theta$ per unit $(\phi,\theta)$. The **area distortion
factor** — map area divided by true area — is therefore

$$\frac{R^2}{R^2\sin\theta} = \frac{1}{\sin\theta}.$$

| $\theta$ | $\sin\theta$ | distortion factor |
|---|---|---|
| $90^\circ$ (equator) | 1.0000 | 1.000 |
| $45^\circ$ | 0.7071 | 1.414 |
| $10^\circ$ (near pole) | 0.1736 | 5.759 |

**(c)** The projection distorts **high latitudes** most, stretching them
east–west. The reason is that a degree of longitude is a distance
$R\sin\theta\,d\phi$ on the sphere but is drawn as $R\,d\phi$ on the map: the
map uses the equatorial length for every latitude. The distortion is entirely a
statement about the ratio of two determinants, and it is why an unweighted mean of
grid values in a lat–long grid over-represents the poles (compare
[02-multiple-integrals-solutions](./02-multiple-integrals-solutions.md), ★★7(d)).

---

## ★★7 — The map $(u,v)\mapsto(u^3-3uv^2,\ 3u^2v-v^3)$

**(a)** Writing the map as the real and imaginary parts of $z\mapsto z^3$ with
$z = u+iv$, the Jacobian is

$$\mathbf{J} = \begin{pmatrix}
3u^2-3v^2 & -6uv\\
6uv & 3u^2-3v^2
\end{pmatrix},
\qquad
\det\mathbf{J} = \left(3u^2-3v^2\right)^2 + 36u^2v^2
= 9\left(u^2+v^2\right)^2 .$$

For an analytic map, $\det\mathbf{J} = \lvert f'(z)\rvert^2$, and here
$f'(z) = 3z^2$, so $\lvert f'\rvert^2 = 9\lvert z\rvert^4$ — the same result. The
matrix is a scaled rotation, which is the local statement that conformal maps are
angle-preserving.

**(b)** $\det\mathbf{J} = 0$ only at $u = v = 0$.

**Numerical confirmation:** at $(u,v) = (1,0)$, $(0.3,0.7)$ and
$(-0.5,\sqrt{3}/2)$ the finite-difference determinants are $9.00000000$,
$3.02760000$ and $9.00000000$, against $9(u^2+v^2)^2 = 9.00000000$, $3.02760000$
and $9.00000000$.

**(c)** The vanishing determinant at the origin means the map is **not locally
invertible** there — every direction near the origin is mapped to a single
direction — and the inverse function theorem gives no neighbourhood where an
inverse exists. Everywhere else the map is locally invertible.

It is nevertheless **not globally one-to-one**: it is three-to-one, since
$z^3 = (z\omega)^3$ whenever $\omega^3 = 1$. A concrete pair:

$$(u,v) = (1,\ 0) \quad\text{and}\quad (u,v) = \left(-\tfrac{1}{2},\
\tfrac{\sqrt{3}}{2}\right)$$

both map to $(1,0)$. Evaluating the map at the second point numerically gives
$(1.000000,\ 1.1\times10^{-16})$ — the same image to round-off.

**The lesson.** Local invertibility and global invertibility are different
properties, and the Jacobian determinant speaks only to the first. In geophysics
the same distinction appears whenever a transformation is many-to-one: a
reflection travel time maps two different reflectors to the same time, and no
amount of local analysis of the forward operator detects it.

---

## ★★8 — Cell volumes on a spherical grid

**(a)** Using $dV = r^2\sin\theta\,dr\,d\theta\,d\phi$ with
$\Delta r = 10^4$ m and $\Delta\theta = \Delta\phi = 0.01$ rad:

At $\theta = 90^\circ$ ($\sin\theta = 1$):

$$\Delta V = (6.4\times10^6)^2 \times 1 \times 10^4 \times (0.01)^2
= 4.0960\times10^{13}\ \mathrm{m^3}.$$

At $\theta = 1^\circ$ ($\sin\theta = 0.0174524$):

$$\Delta V = 4.096\times10^{13} \times 0.0174524
= 7.1485\times10^{11}\ \mathrm{m}^3 .$$

**(b)** Ratio $= 1/\sin(1^\circ) = 57.30$.

**(c)** A cell at $1^\circ$ colatitude contains 57 times less volume than a cell
at the equator, so giving every cell equal weight in an average is equivalent to
weighting the polar regions 57 times too heavily. The correct average is

$$\bar f = \frac{\sum_{\text{cells}} f_{\text{cell}}\,\sin\theta_{\text{cell}}}
{\sum_{\text{cells}} \sin\theta_{\text{cell}}} ,$$

that is, **weight by $\sin\theta$** — the Jacobian determinant surviving into the
discrete sum. The same factor appears in the orthogonality relations of spherical
harmonics, which is why spherical harmonic coefficients are estimated with
weighted quadrature rather than by averaging grid values.

---

## ★★★9 — Where the linearised covariance transformation breaks

**Method.** For the map $(r,\theta)\mapsto(x,y) = (r\cos\theta, r\sin\theta)$ with
$r = 1$, $\theta = 0$, $\sigma_r = 10^{-3}$, the linearised covariance is
$\mathbf{C}_y = \mathbf{J}\mathbf{C}_x\mathbf{J}^{\mathsf T}$ with
$\mathbf{J} = \begin{pmatrix}\cos\theta & -r\sin\theta\\ \sin\theta &
r\cos\theta\end{pmatrix}$, and the Monte Carlo covariance used $2\times10^5$
samples per case.

**Results (m²):**

| $\sigma_\theta$ (rad) | $C_{xx}$ Jacobian | $C_{xx}$ Monte Carlo | rel. diff. | $C_{yy}$ Jacobian | $C_{yy}$ Monte Carlo | rel. diff. |
|---|---|---|---|---|---|---|
| $10^{-6}$ | $1.0000\times10^{-6}$ | $9.9897\times10^{-7}$ | 1.0 % | $1.0000\times10^{-12}$ | $9.9783\times10^{-13}$ | 0.2 % |
| $10^{-3}$ | $1.0000\times10^{-6}$ | $9.9897\times10^{-7}$ | 1.0 % | $1.0000\times10^{-6}$ | $9.9783\times10^{-7}$ | 0.2 % |
| $10^{-2}$ | $1.0000\times10^{-6}$ | $1.0036\times10^{-6}$ | 0.4 % | $1.0000\times10^{-4}$ | $9.9773\times10^{-5}$ | 0.2 % |
| $3\times10^{-2}$ | $1.0000\times10^{-6}$ | $1.3969\times10^{-6}$ | **40 %** | $9.0000\times10^{-4}$ | $8.9725\times10^{-4}$ | 0.3 % |
| $10^{-1}$ | $1.0000\times10^{-6}$ | $5.0023\times10^{-5}$ | **4900 %** | $1.0000\times10^{-2}$ | $9.8797\times10^{-3}$ | 1.2 % |

**(b)** The Monte Carlo noise floor on a variance estimate with $N = 2\times10^5$
is $\sqrt{2/N} = 3.2\times10^{-3}$, that is 0.32 % relative. So the 1.0 % and 0.4 %
discrepancies at small $\sigma_\theta$ are a few standard errors — marginal but
plausibly real; the 40 % and 4900 % discrepancies are enormous and definitive.

**(c)** The linearisation fails between $\sigma_\theta = 10^{-2}$ and
$3\times10^{-2}$ rad, and the reason is arithmetic. At $\theta = 0$,
$x = r\cos\theta \approx r(1-\theta^2/2)$, so the neglected second-order term in
$x$ has size $r\sigma_\theta^2/2$. Setting this equal to the first-order
uncertainty $\sigma_r = 10^{-3}$:

$$\frac{(3\times10^{-2})^2}{2} = 4.5\times10^{-4} \approx \frac{\sigma_r}{2},$$

so at that point the quadratic term is half the linear one. **The criterion is
"second-order term comparable to the first-order spread", and it is checkable in
advance.**

Notice also *where* the failure appears: $C_{yy}$ stays accurate throughout,
because $y = r\sin\theta \approx r\theta$ is linear at $\theta = 0$ to the order
that matters. The breakdown is directional, and a single scalar error metric
would hide it.

**(d)** Practical rule: compute the ratio
$\rho = \tfrac12\lvert\delta\mathbf{x}^{\mathsf T}\mathbf{H}\delta\mathbf{x}\rvert
/ \lvert\mathbf{J}\delta\mathbf{x}\rvert$ using the largest plausible $\delta$.
If $\rho \lesssim 0.1$, the linearised covariance is adequate. If
$\rho \gtrsim 0.3$, use Monte Carlo (or a second-order expansion). In this example
$\rho = 0.45$ at $\sigma_\theta = 3\times10^{-2}$, which is the point at which the
column changed from percent-level to tens-of-percent discrepancies.

**Interpretation for geophysics.** A covariance matrix fed into a least-squares
inversion is nearly always a linearised one. The table shows that it can be wrong
by a factor of 50 in variance while looking entirely reasonable on paper. The
cases where it matters are exactly the cases where the transformation is strongly
nonlinear over the uncertainty — large angles, large distances on a sphere, or
near-singular coordinate points.

---

## ★★★10 — Prolate spheroidal coordinates

**(a)** With

$$x = a\sinh\mu\sin\nu\cos\phi, \quad
y = a\sinh\mu\sin\nu\sin\phi, \quad z = a\cosh\mu\cos\nu,$$

the coordinate surface $\mu = \text{const}$ is a prolate spheroid (an ellipse
rotated about the $z$ axis), and $\nu$ plays the role of a "latitude" on it. The
three scale factors are

$$h_\mu = h_\nu = a\sqrt{\sinh^2\mu + \sin^2\nu}, \qquad
h_\phi = a\sinh\mu\sin\nu,$$

and since the coordinates are orthogonal the volume element is the product:

$$dV = a^3\sinh\mu\,\sin\nu\left(\sinh^2\mu + \sin^2\nu\right)
d\mu\,d\nu\,d\phi .$$

(This was verified by finite-differencing the map itself at three points; the
numeric and analytic determinants agreed to between $1.8\times10^{-11}$ and
$2.4\times10^{-10}$ relative.)

**(b)** Integrating over the spheroid $\mu \le \mu_0$:

$$V = \int_0^{2\pi}\!\!\int_0^{\pi}\!\!\int_0^{\mu_0}
a^3\sinh\mu\,\sin\nu\left(\sinh^2\mu+\sin^2\nu\right)d\mu\,d\nu\,d\phi .$$

The $\phi$ integral gives $2\pi$. Using
$\int_0^{\pi}\sin\nu\,d\nu = 2$ and
$\int_0^{\pi}\sin^3\nu\,d\nu = \tfrac{4}{3}$ to separate the two terms,

$$V = 2\pi a^3\int_0^{\mu_0}\sinh\mu\left(2\sinh^2\mu + \tfrac{4}{3}\right)d\mu
= \frac{4\pi}{3}a^3\cosh\mu_0\left(\cosh^2\mu_0 - 1\right)
= \frac{4\pi}{3}a^3\sinh^2\mu_0\cosh\mu_0 .$$

The check: the spheroid has semi-axes $a\sinh\mu_0$, $a\sinh\mu_0$ and
$a\cosh\mu_0$, so its volume by the ellipsoid formula $\tfrac{4}{3}\pi abc$ is

$$\frac{4}{3}\pi\left(a\sinh\mu_0\right)^2\left(a\cosh\mu_0\right)
= \frac{4\pi}{3}a^3\sinh^2\mu_0\cosh\mu_0 . \checkmark$$

Two independent routes agree, which is the whole purpose of the check.

**(c)** Numeric determinants (finite differences of the map, $h = 10^{-6}$) against
$\lvert\det\mathbf{J}\rvert = a^3\sinh\mu\sin\nu(\sinh^2\mu+\sin^2\nu)$ with
$a = 2$:

| $(\mu,\nu,\phi)$ | numeric | analytic | relative difference |
|---|---|---|---|
| $(0.5, 1.0, 0.3)$ | 3.43637981 | 3.43637981 | $1.8\times10^{-11}$ |
| $(1.2, 2.0, 1.1)$ | 34.09736880 | 34.09736881 | $1.8\times10^{-10}$ |
| $(2.5, 0.4, 4.0)$ | 692.80661053 | 692.80661037 | $2.4\times10^{-10}$ |

**(d)** Spheroidal coordinates are natural whenever the body or the boundary is
approximately an ellipsoid of revolution, because then one coordinate surface
**is** the boundary: a flattened Earth, a magma chamber, an ellipsoidal ore body
or a stretched inclusion has a constant-$\mu$ or constant-$\nu$ surface, so the
integration limits become constants instead of functions and the boundary
condition is imposed on a coordinate surface. That is the same argument as using
spherical coordinates for a sphere, one level of geometric generality further.
