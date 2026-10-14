# Exercises — 01-06-03 Jacobians, Coordinate Transformations and Volume Elements

Attempt these **closed-book** before opening the
[solutions](./03-jacobians-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Several problems ask you to modify
[`../code/jacobian_transformations.py`](../code/jacobian_transformations.py).
Do that literally and report what the machine returns.

---

## ★ Foundational

**★1.** Write the Jacobian matrix of each map and compute its determinant.

(a) $x = 2u + v,\quad y = u - 3v$
(b) $x = uv,\quad y = u/v$ (for $v \ne 0$)
(c) $x = r\cos\theta,\quad y = r\sin\theta$
(d) $x = \rho\cos\phi,\quad y = \rho\sin\phi,\quad z = z$

---

**★2.** Compute $\det\mathbf{J}$ for the spherical map
$x = r\sin\theta\cos\phi$, $y = r\sin\theta\sin\phi$, $z = r\cos\theta$ by
expanding along the third row, and identify the points at which the determinant
vanishes.

---

**★3.** Use a change of variables to evaluate the volume of the region

$$E = \left\{(x,y,z) : \frac{x^2}{a^2} + \frac{y^2}{b^2} + \frac{z^2}{c^2} \le 1
\right\},$$

that is, an ellipsoid with semi-axes $a,b,c$. State the substitution and the
Jacobian you used.

---

**★4.** State the determinant of the Jacobian matrix of the map
$(x_1,\dots,x_n) \mapsto (\lambda x_1,\dots,\lambda x_n)$ for a scalar
$\lambda$, and state the volume scale factor of the corresponding
$n$-dimensional region. From that, state how the volume of the ellipsoid in ★3
relates to the volume of the unit ball in three dimensions.

---

## ★★ Applied

**★★5.** A GNSS station is described by geodetic coordinates with independent
standard uncertainties $\sigma_\varphi = 10^{-8}$ rad in latitude,
$\sigma_\lambda = 10^{-8}$ rad in longitude and $\sigma_h = 0.01$ m in
ellipsoidal height, at $\varphi = 45^\circ$ and $\lambda = 0$, on a sphere of
radius $R = 6.371\times10^6$ m. Use the spherical approximation (treat the height
as the radial coordinate).

(a) Write the Jacobian matrix of the map $(\varphi,\lambda,h) \mapsto (x,y,z)$
with $x = (R+h)\cos\varphi\cos\lambda$, and convert $\varphi$ to colatitude if
you prefer; be explicit about your convention.
(b) Compute the transformed covariance matrix $\mathbf{J}\,\mathbf{C}\,
\mathbf{J}^{\mathsf T}$ numerically.
(c) State the horizontal position uncertainty in metres, and compare it with the
0.01 m vertical uncertainty. Which dominates, and by how much?

---

**★★6.** A cylindrical map projection maps the sphere
$(R\sin\theta\cos\phi, R\sin\theta\sin\phi, R\cos\theta)$ to the plane via
$(u,v) = (R\phi,\ R(\pi/2 - \theta))$. For a small region, treat $\theta$ as
constant so the map is effectively two-dimensional in $(\phi,\theta)$ near that
latitude.

(a) Compute the two-dimensional Jacobian determinant of this map near latitude
$\theta$.
(b) Interpret the determinant as the local area distortion factor and evaluate it
at $\theta = 90^\circ$, $45^\circ$ and $10^\circ$.
(c) State which latitudes this projection distorts most, in which direction, and
why.

---

**★★7.** Consider the map $\mathbf{g}(u,v) = (u^3 - 3uv^2,\ 3u^2v - v^3)$.

(a) Compute the Jacobian determinant as a function of $(u,v)$.
(b) Find the set on which the determinant vanishes.
(c) State what the vanishing of the Jacobian determinant implies about
invertibility, and verify your conclusion at a specific point by computing the map
at two distinct points that give the same image.

---

**★★8.** A spherical coordinate system is used to grid a global gravity model.

(a) Compute the volume of the cell spanned by
$\Delta r = 10^4$ m, $\Delta\theta = \Delta\phi = 0.01$ rad at
$r = 6.4\times10^6$ m, $\theta = 90^\circ$ and at $\theta = 1^\circ$, using
$dV = r^2\sin\theta\, d\theta\, d\phi\, dr$.
(b) Report the ratio of the two cell volumes.
(c) Explain why a gridded field averaged with equal weight per cell is biased, and
state the correct weighting.

## ★★★ Research-oriented

**★★★9.** The first-order covariance transformation
$\mathbf{C}_y = \mathbf{J}\mathbf{C}_x\mathbf{J}^{\mathsf T}$ is an
approximation. Study its breakdown numerically for the map
$(r,\theta) \mapsto (x,y) = (r\cos\theta, r\sin\theta)$ with $r = 1$,
$\theta = 0$, $\sigma_r = 10^{-3}$ and $\sigma_\theta$ varying over
$\{10^{-6}, 10^{-3}, 10^{-2}, 3\times10^{-2}, 10^{-1}\}$ rad.

(a) Compute $\mathbf{C}_y$ from the Jacobian and from a Monte Carlo simulation
with at least $10^5$ samples, and tabulate the relative difference for each
$\sigma_\theta$.
(b) Estimate the Monte Carlo noise floor and state whether each difference is
significant.
(c) Identify the value of $\sigma_\theta$ at which the linearisation visibly
fails, and relate it to the curvature scale of the map.
(d) State a practical rule for deciding when you must use Monte Carlo.

---

**★★★10.** Derive the volume element for prolate spheroidal coordinates
$x = a\sinh\mu\sin\nu\cos\phi$, $y = a\sinh\mu\sin\nu\sin\phi$,
$z = a\cosh\mu\cos\nu$, where $\mu \ge 0$, $0 \le \nu \le \pi$,
$0 \le \phi < 2\pi$.

(a) Compute the Jacobian determinant.
(b) Compute the volume of the spheroid $\mu \le \mu_0$ by integrating the volume
element, and check your answer against the ellipsoid formula with semi-axes
$a\sinh\mu_0$, $a\sinh\mu_0$ and $a\cosh\mu_0$.
(c) Verify the determinant numerically at three values of $(\mu,\nu,\phi)$.
(d) Explain in one sentence why spheroidal coordinates are natural for modelling a
flattened Earth or an ellipsoidal ore body.
