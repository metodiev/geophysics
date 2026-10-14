# Exercises — 01-15-06 Differential Geometry of the Earth's Surface and Sphere

Attempt these **closed-book** before opening the
[solutions](./06-differential-geometry-earth-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Conventions: $R = 6371$ km for the spherical Earth (state it when you use it);
$\theta$ is colatitude and $\phi$ longitude; for the ellipsoid use the WGS 84
values $a = 6378137$ m and $1/f = 298.257223563$ so that $e^{2} = 2f - f^{2}$;
latitude is **geodetic** unless stated. Report distances in km to four decimals
where the problem asks for a comparison.

Problems referring to
[`../code/sphere_geometry_demo.py`](../code/sphere_geometry_demo.py) require you to
run it and report its actual output.

---

## ★ Foundational

**★1.** A torus is parametrised by
$\mathbf x(u,v) = \left((R + a\cos v)\cos u,\ (R+a\cos v)\sin u,\ a\sin v\right)$.

(a) Compute the two tangent vectors and the metric $g_{ij}$.
(b) Show the parameter curves are orthogonal.
(c) Compute $dA$ and the total area.
(d) Evaluate $g_{uu}$ and $g_{vv}$ at $R = 2$, $a = 0.5$, $v = 0.3$, and state
where the parametrisation is degenerate.

---

**★2.** Lengths on the sphere.

(a) Compute the length of one degree of latitude and state whether it depends on
latitude.
(b) Compute the length of one degree of longitude at latitudes $0^\circ$,
$45^\circ$, $60^\circ$ and $89^\circ$.
(c) Compute the length of a great-circle arc spanning $30^\circ$ of central angle.
(d) State which of the three is invariant under rotation of the sphere about its
axis and which is not.

---

**★3.** Areas on the sphere.

(a) Compute the area of a spherical cap of half-angle $30^\circ$.
(b) Compute the area of a lune bounded by two meridians $90^\circ$ apart.
(c) Compute the area of the octant triangle whose vertices are three mutually
perpendicular directions.
(d) Verify that (c) is one eighth of the total area, and state what the angular
excess of that triangle is.

---

**★4.** Great-circle distance and initial bearing.

For London $(51.5^\circ\mathrm{N}, 0.13^\circ\mathrm{W})$ and New York
$(40.7^\circ\mathrm{N}, 74.0^\circ\mathrm{W})$:

(a) Compute the great-circle distance using the haversine formula.
(b) Compute the initial bearing.
(c) Explain why the *final* bearing differs from the initial one, unlike the
Cartesian case.
(d) State at what distance the flat-Earth approximation produces a travel-time
error of 0.1 s at $6\ \mathrm{km\,s^{-1}}$.

---

## ★★ Applied

**★★5.** Verify Gauss–Bonnet three ways on a triangle of your choosing.

(a) Construct a geodesic triangle on the sphere and compute its interior angles
using the spherical law of cosines for angles.
(b) Compute the area as $R^{2}(A+B+C-\pi)$.
(c) Verify it with the algebraic identity
$2\arctan_{2}\!\left(|\mathbf a\cdot(\mathbf b\times\mathbf c)|,\
1 + \mathbf a\cdot\mathbf b + \mathbf b\cdot\mathbf c + \mathbf c\cdot\mathbf a\right)$.
(d) Explain why the three routes must agree and what a disagreement would signify.

---

**★★6.** Curvature from a small circle.

(a) Show that a geodesic circle of surface radius $\rho$ on a sphere is a latitude
circle whose circumference is $2\pi R\sin(\rho/R)$.
(b) Expand to obtain $C(\rho) = 2\pi\rho - \pi\rho^{3}K/3 + O(\rho^{5})$.
(c) Compute the circumference deficit $2\pi\rho - C(\rho)$ at $\rho = 100$ m,
$1$ km and $10$ km, and the implied $K$.
(d) Explain why a single distance measurement cannot detect curvature, and what
kind of measurement can.

---

**★★7.** The ellipsoid's metric.

(a) Compute $M(\varphi)$ and $N(\varphi)$ at $\varphi = 0^\circ$ and
$90^\circ$ for WGS 84.
(b) Compute one degree of latitude at the equator and at the pole.
(c) Compute the meridian arc from the equator to $45^\circ$ by quadrature, and
compare it with the spherical value.
(d) State which of the two curvatures (meridional or normal) sets the north–south
and which the east–west distance, and why they differ.

---

**★★8.** The two latitudes.

(a) For geodetic latitudes $0^\circ$, $30^\circ$, $45^\circ$, $60^\circ$,
$90^\circ$, compute the geocentric latitude and the difference in arc minutes.
(b) Translate the $45^\circ$ difference into a surface displacement.
(c) State which latitude a GNSS receiver reports and which a gravity model uses.
(d) Explain why the difference vanishes at the equator and the poles.

---

## ★★★ Research-oriented

**★★★9.** The geodesic equation on the ellipsoid.

(a) Write the geodesic equation
$\ddot u^{k} + \Gamma^{k}_{\;ij}\dot u^i\dot u^j = 0$ for the ellipsoid metric
$g_{\varphi\varphi} = M^{2}$, $g_{\lambda\lambda} = (N\cos\varphi)^{2}$.
(b) Show that $\lambda$ is a cyclic coordinate and derive the conserved quantity
(Clairaut's relation).
(c) State the numerical scheme you would use for the Christoffel symbols and for
the integration, and the check that validates it.
(d) State which reference frame and which application require the ellipsoidal
geodesic rather than a spherical great circle, with a numerical criterion.

---

**★★★10.** The flat-Earth error, propagated into a travel time.

(a) For two points on the $45^\circ\mathrm{N}$ parallel separated by a parallel arc
of $100$, $500$, $1000$ and $3000$ km, compute the great-circle distance and the
relative error of the parallel arc.
(b) Show that the relative error is $(d/R)^{2}\tan^{2}\varphi/24$ to leading order,
evaluate the coefficient at $45^\circ$ and check it against your numbers, then
verify the prediction at a second latitude of your choosing.
(c) Repeat for two points on the same meridian and explain the difference — and
explain why the error vanishes at the equator.
(d) Propagate each error into a travel-time residual at
$6\ \mathrm{km\,s^{-1}}$ and decide, with numbers, at what distance the spherical
treatment becomes mandatory for a target precision of 0.05 s.

---

## Self-check

Before opening the solutions, state for each distance whether it is an arc on the
sphere, a chord through the Earth, or a path on the ellipsoid. Confusing a chord
with an arc is the most common error in this subject, and its size is
$(d/R)^{2}/24$ — the same quantity computed in ★★★10.
