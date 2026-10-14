# Solutions — 01-15-06 Differential Geometry of the Earth's Surface and Sphere

> **Read this after attempting the exercises, not before.** Every number below was
> computed: metrics by differencing the parametrisation, areas and arcs by
> quadrature, distances by the haversine formula, and ellipsoidal quantities from
> the WGS 84 parameters. $R = 6371$ km unless stated.

---

## ★1 — The torus

**(a)** With $\mathbf x(u,v) = \left((R + a\cos v)\cos u,\
(R+a\cos v)\sin u,\ a\sin v\right)$:

$$\frac{\partial\mathbf x}{\partial u} = \left(-(R+a\cos v)\sin u,\
(R+a\cos v)\cos u,\ 0\right), \qquad
\frac{\partial\mathbf x}{\partial v} = \left(-a\sin v\cos u,\
-a\sin v\sin u,\ a\cos v\right).$$

Their lengths give $g_{uu} = (R+a\cos v)^{2}$ and $g_{vv} = a^{2}$, and their dot
product is

$$a(R+a\cos v)\left(\sin u\cos u - \cos u\sin u\right) = 0,$$

so $g_{uv} = 0$. The metric is

$$g = \begin{pmatrix}(R+a\cos v)^{2} & 0\\ 0 & a^{2}\end{pmatrix}, \qquad
ds^{2} = (R+a\cos v)^{2}du^{2} + a^{2}dv^{2}.$$

**(b)** $g_{uv} = 0$ is exactly the statement of orthogonality: the parameter curves
meet at right angles everywhere. That is why the scale factors $h_u = R+a\cos v$ and
$h_v = a$ can be read off the diagonal.

**(c)** $\sqrt{\det g} = a(R + a\cos v)$, so

$$dA = a(R+a\cos v)\,du\,dv, \qquad
A = \int_0^{2\pi}\!\!\int_0^{2\pi}a(R+a\cos v)\,dv\,du
= 2\pi a\left[2\pi R + a\underbrace{\int_0^{2\pi}\cos v\,dv}_{0}\right]
= \boxed{4\pi^{2}Ra}.$$

For $R = 2$ m, $a = 0.5$ m: $A = 4\pi^{2}(2)(0.5) = 39.478418$ m$^{2}$. The
independence of $a^{2}$ is the classical result: a torus's area is that of the
cylinder swept by the tube's centreline.

**(d)** At $v = 0.3$: $g_{uu} = (2 + 0.5\cos0.3)^{2} = (2.477601)^{2} = 6.138840$
and $g_{vv} = 0.25$. The parametrisation is smooth everywhere on the torus as long
as $a < R$; if $a = R$ the inner tube closes on itself at $v = \pi$ and the metric's
$g_{uu}$ vanishes there (a *horn torus*), and for $a>R$ the surface self-intersects.
So the degeneracy is a property of the parametrisation's domain, not of the surface
as an abstract object — the same distinction as the polar singularity in spherical
coordinates.

---

## ★2 — Lengths on the sphere

**(a)** Along a meridian $d\phi = 0$, so $ds = R\,d\theta$ and one degree of
latitude is

$$R\frac{\pi}{180} = 6371(0.0174533) = \boxed{111.1949}\ \text{km},$$

**independent of latitude** on a sphere — a consequence of spherical symmetry, and
the reason a degree of latitude is the natural unit for comparing ellipsoidal and
spherical models.

**(b)** Along a parallel $d\theta = 0$, so $ds = R\sin\theta\,d\phi$ and one degree
of longitude is $R(\pi/180)\sin\theta = 111.1949\cos(\text{latitude})$ km:

| latitude | one degree of longitude (km) | fraction of the equatorial value |
|---|---|---|
| $0^\circ$ | 111.1949 | 1.0000 |
| $45^\circ$ | 78.6267 | 0.7071 |
| $60^\circ$ | 55.5975 | 0.5000 |
| $89^\circ$ | 1.9405 | 0.0175 |

The ratios are $\cos(\text{latitude})$ exactly — the table *is* that identity, and
the $89^\circ$ entry is the reason a polar survey grid cannot be a latitude–longitude
grid.

**(c)** A great-circle arc of central angle $\alpha$ has length $R\alpha$, so
$30^\circ = \pi/6$ rad gives

$$s = 6371\frac{\pi}{6} = \boxed{3335.848}\ \text{km}.$$

**(d)** The great-circle arc is invariant under every rotation of the sphere,
including a rotation about the polar axis; a degree of latitude is invariant under
rotations about the polar axis but not under rotations that move the poles; a degree
of longitude is invariant under neither. That hierarchy is worth remembering: the
only distance on a sphere that does not depend on the coordinate choice is the
great-circle distance, which is why it is the quantity every global geophysical
calculation uses.

---

## ★3 — Areas on the sphere

**(a)** A cap of half-angle $\alpha$ subtends the colatitude range $[0,\alpha]+$ the
mirror image, i.e. $[0,\alpha]$ from the pole, so

$$A = R^{2}\int_0^{2\pi}\!\!\int_0^{\alpha}\sin\theta\,d\theta\,d\phi
= 2\pi R^{2}(1 - \cos\alpha) = 2\pi(6371)^{2}(1 - \cos30^\circ)
= \boxed{3.416784\times10^{7}}\ \text{km}^{2}.$$

**(b)** A lune bounded by two meridians separated by $\alpha$:

$$A = R^{2}\int_0^{\alpha}\!\!\int_0^{\pi}\sin\theta\,d\theta\,d\phi
= 2\alpha R^{2},$$

so for $\alpha = 90^\circ = \pi/2$, $A = \pi R^{2} = 1.275161\times10^{8}$ km$^{2}$
— exactly one quarter of the sphere, as it must be, since $90^\circ$ is a quarter of
$360^\circ$.

**(c)** The octant triangle (vertices on three mutually perpendicular directions,
e.g. the north pole and two points $90^\circ$ apart on the equator) has all three
angles equal to $\pi/2$, so the angular excess is

$$A + B + C - \pi = \frac{3\pi}{2} - \pi = \frac{\pi}{2},$$

and its area is $R^{2}\pi/2 = \boxed{6.375806\times10^{7}}$ km$^{2}$.

**(d)** The total surface area is $4\pi R^{2} = 5.100645\times10^{8}$ km$^{2}$, and
$(4\pi R^{2})/8 = \pi R^{2}/2$ — exactly the value in (c) ✓. So the octant triangle
is one eighth of the sphere, which is the statement that the three mutually
perpendicular directions divide the sphere into eight congruent pieces, each with
angular excess $\pi/2$. Gauss–Bonnet therefore gives curvature "in one line, with no
series and no approximation", as the lesson says.

---

## ★4 — London to New York

**(a)** With $\varphi_1 = 51.5^\circ$, $\lambda_1 = -0.13^\circ$,
$\varphi_2 = 40.7^\circ$, $\lambda_2 = -74.0^\circ$, the haversine formula

$$a = \sin^{2}\frac{\Delta\varphi}{2} + \cos\varphi_1\cos\varphi_2\sin^{2}
\frac{\Delta\lambda}{2}, \qquad d = 2R\arcsin\sqrt a ,$$

gives $a = 0.0674996$ and $d = \boxed{5570.834}$ km.

**(b)** The initial bearing (azimuth measured clockwise from north) is

$$\beta = \operatorname{atan2}\!\left(\sin\Delta\lambda\cos\varphi_2,\
\cos\varphi_1\sin\varphi_2 - \sin\varphi_1\cos\varphi_2\cos\Delta\lambda\right)
= \boxed{288.3175^\circ},$$

i.e. a west-north-west course.

**(c)** On a sphere a geodesic's azimuth changes continuously except along a
meridian or the equator: the great circle between two mid-latitude points is not a
rhumb line, so the heading at the destination differs from the heading at the start
(here by about $40^\circ$). In Cartesian geometry a straight line has one direction
everywhere; the difference is the curvature of the surface expressed in the
*coordinate* frame, and it is why navigation follows great circles rather than
constant bearings (which are longer but easier to steer).

**(d)** The relative error of the parallel-arc approximation is
$(d/R)^{2}\tan^{2}\varphi/24$ (exercise ★★★10). A travel-time error of 0.1 s at
$6\ \mathrm{km\,s^{-1}}$ is a distance error of 0.6 km, i.e. a relative error of
$0.6/d$. Setting $0.6/d = (d/R)^{2}\tan^{2}\varphi/24$ with $\varphi = 45^\circ$
($\tan^{2} = 1$):

$$d^{3} = 0.6\times24\times R^{2} = 14.4\,(6371)^{2} = 5.845\times10^{8}
\quad\Longrightarrow\quad d = \sqrt[3]{5.845\times10^{8}} = 836.1\ \text{km}.$$

So beyond roughly **840 km** at mid-latitude, a flat-Earth distance used for a
travel-time calculation introduces more than 0.1 s — which is why regional
tomography switches to spherical geometry well before continental scale.

---

## ★★5 — Gauss–Bonnet three ways

**(a)** Take vertices at unit vectors $\mathbf a$, $\mathbf b$, $\mathbf c$ with
angular separations on the order of $60^\circ$ (the demonstration's triangle has
interior angles $1.373401$, $1.361763$ and $0.879437$ rad). The interior angle at
$\mathbf a$ is obtained from the spherical law of cosines for angles, using the
side lengths $\arccos(\mathbf a\cdot\mathbf b)$ etc.

**(b)** The angle sum is $3.614601$ rad, so the excess is

$$\text{excess} = 3.614601 - \pi = 0.473008\ \text{rad}, \qquad
A = R^{2}\,\text{excess} = \boxed{1.919923\times10^{7}}\ \text{km}^{2}.$$

**(c)** The algebraic identity for the excess,

$$\text{excess} = 2\arctan\!\left(
\frac{|\mathbf a\cdot(\mathbf b\times\mathbf c)|}
{1 + \mathbf a\cdot\mathbf b + \mathbf b\cdot\mathbf c + \mathbf c\cdot\mathbf a}
\right),$$

`atan2`-based, returns $0.473008196938$ rad — identical to the angle-sum route to
$\pm1.7\times10^{-16}$. A Monte Carlo estimate with 400 000 uniform points gives
$0.037637$ of the sphere's area, i.e. $1.919755\times10^{7}$ km$^{2}$ with a
two-sigma uncertainty of $3.07\times10^{5}$ km$^{2}$: the Gauss–Bonnet value lies
$0.01\sigma$ from the sampled mean, which is the coincidence to expect and not a
verification of the sampling.

**(d)** The three routes must agree because (b) is the *definition* of the excess,
(c) is an identity that follows from the spherical trigonometry of the triangle, and
the Monte Carlo is an independent estimate of the same area. A disagreement beyond
the Monte Carlo's own sampling error would mean either that the triangle's sides
were not geodesics (so Gauss–Bonnet does not apply) or that the angles were
computed from the wrong law of cosines. This is why the identity in (c) is worth
using in code: it is a closed form with no trigonometry recursion, and it serves as
the check on any angle-based implementation.

---

## ★★6 — Curvature from a small circle

**(a)** A geodesic circle of radius $\rho$ around a pole of the sphere is the
latitude circle at colatitude $\theta = \rho/R$, whose circumference is
$2\pi R\sin\theta = 2\pi R\sin(\rho/R)$. $\square$

**(b)** Expanding $\sin x = x - x^{3}/6 + O(x^{5})$ with $x = \rho/R$:

$$C(\rho) = 2\pi R\left(\frac{\rho}{R} - \frac{\rho^{3}}{6R^{3}}\right) + O(\rho^{5})
= 2\pi\rho - \frac{\pi\rho^{3}}{3R^{2}} + O(\rho^{5})
= 2\pi\rho - \frac{\pi\rho^{3}K}{3} + O(\rho^{5}),$$

with $K = 1/R^{2}$. $\square$

**(c)** The deficit $\Delta = 2\pi\rho - C(\rho) = \pi\rho^{3}K/3$, so
$K = 3\Delta/(\pi\rho^{3})$:

| $\rho$ | $2\pi\rho$ (m) | $C$ on the sphere (m) | deficit (m) | $K$ estimate (m$^{-2}$) |
|---|---|---|---|---|
| 100 m | 628.318531 | 628.318530692 | $2.580\times10^{-8}$ | $2.463684\times10^{-14}$ |
| 1 km | 6283.185307 | 6283.185281380 | $2.580\times10^{-5}$ | $2.463683\times10^{-14}$ |
| 10 km | 62831.853072 | 62831.827272173 | $2.580\times10^{-2}$ | $2.463682\times10^{-14}$ |

All three agree with $1/R^{2} = 2.463683\times10^{-14}$ m$^{-2}$, and the deficit
grows as $\rho^{3}$ while its *relative* size grows as $\rho^{2}$: at $\rho = 1$ km
the deficit is a fractional $4.1\times10^{-9}$ of the circumference.

**(d)** No single distance measurement can reveal curvature because the deficit is
smaller than any realistic measurement uncertainty at survey scales — $2.6\times
10^{-2}$ m in 62.8 km at $\rho = 10$ km, i.e. $4\times10^{-7}$ relative, far below
the accuracy of a distance measurement. What *can* detect it is the **closure of a
network**: measure the angles and distances of a triangle and check whether the
angle sum exceeds $\pi$ by the amount the enclosed area demands. The excess is
$A/R^{2}$, which for a $100$ km triangle of area $\sim2\times10^{3}$ km² is
$5\times10^{-5}$ rad $\approx 10$ arcsec — at the resolution of a classical
theodolite, which is exactly why historic triangulation networks could measure the
Earth's curvature without ever leaving its surface.

---

## ★★7 — The ellipsoid's metric

**(a)** With $a = 6378137$ m, $f = 1/298.257223563$ and
$e^{2} = 2f - f^{2} = 0.006694379990$:

$$M(\varphi) = \frac{a(1-e^{2})}{\left(1-e^{2}\sin^{2}\varphi\right)^{3/2}}, \qquad
N(\varphi) = \frac{a}{\left(1-e^{2}\sin^{2}\varphi\right)^{1/2}},$$

giving $M(0) = 6335439.3$ m, $N(0) = 6378137.0$ m, $M(90^\circ) = 6399593.6$ m,
$N(90^\circ) = 6399593.6$ m. At $45^\circ$: $M = 6367381.8$ m,
$N = 6388838.3$ m.

**(b)** One degree of latitude is $M(\pi/180)$:

$$M(0)\frac{\pi}{180} = \boxed{110.574}\ \text{km}, \qquad
M(90^\circ)\frac{\pi}{180} = \boxed{111.694}\ \text{km},$$

a range of $1.120$ km — 1.0 per cent — which no spherical model contains.

**(c)** Integrating the meridional element $M(\varphi)\,d\varphi$ from $0$ to
$\pi/4$ by quadrature gives

$$s(45^\circ) = \boxed{4984.9444}\ \text{km},$$

against the spherical value $R(\pi/4) = 5003.7717$ km: a difference of
$-18.8273$ km, i.e. $-0.376$ per cent. As an independent check, the same quadrature
over the whole quadrant gives $10\,001\,965.729$ m, which is the published WGS 84
quarter-meridian value — a number the computation was never given, which makes it
the strongest available verification of the implementation.

**(d)** North–south distances are set by the **meridional** radius of curvature $M$,
because a meridian's length element is $M\,d\varphi$. East–west distances are set by
the **normal** radius $N$, because a parallel's length element is
$(N\cos\varphi)\,d\lambda$: the parallel is a circle of radius $N\cos\varphi$, not
of radius $a\cos\varphi$, because $N$ is the radius of the *local* sphere
approximating the surface in the prime-vertical direction. They differ by up to
$0.3$ per cent, and using $R = 6371$ km for both is the approximation that fails
first.

---

## ★★8 — The two latitudes

**(a)** With $\tan\psi = (1-e^{2})\tan\varphi$, $(1-e^2) = 0.993305620$:

| geodetic $\varphi$ | geocentric $\psi$ | difference |
|---|---|---|
| $0^\circ$ | $0.000000^\circ$ | $0.0000'$ |
| $30^\circ$ | $29.833636^\circ$ | $9.9819'$ |
| $45^\circ$ | $44.807577^\circ$ | $11.5454'$ |
| $60^\circ$ | $59.833076^\circ$ | $10.0154'$ |
| $90^\circ$ | $90.000000^\circ$ | $0.0000'$ |

The difference peaks near $45^\circ$ and vanishes at both ends.

**(b)** At $45^\circ$ the angular difference is $11.5454' = 0.0033598$ rad (in
geocentric measure) and the corresponding surface displacement along the meridian is
of order $R\times0.0033598 \approx 21.4$ km. (The exact displacement depends on which
radius is used to convert; the point is that it is kilometres, not metres.)

**(c)** A GNSS receiver reports **geodetic** latitude on the datum it is configured
with (WGS 84 by default); gravity models and their normal-gravity reference fields
are also expressed in geodetic latitude. Geocentric latitude appears in orbital
mechanics and in some spherical-harmonic formulations, where the "latitude" of a
satellite is naturally geocentric. The two are related by the flattening, so
converting requires the ellipsoid — and mixing them displaces a point by
kilometres, against GNSS precision of centimetres.

**(d)** At the poles the surface normal is along the rotation axis, and the
geocentric direction to a point on the axis is also along it; near the equator the
normal and the radius vector are both in the equatorial plane. So the difference
must vanish at both ends and be maximal near the middle — which is what the table
shows, with a smooth maximum near $45^\circ$ rather than exactly at $45^\circ$
because the relevant deformation is of $\tan$ through the factor $(1-e^{2})$.

---

## ★★★9 — Geodesics on the ellipsoid

**(a)** With $g_{\varphi\varphi} = M^{2}$ and
$g_{\lambda\lambda} = (N\cos\varphi)^{2}$ and no cross term, the geodesic equations
are

$$\ddot\varphi + \Gamma^{\varphi}_{\;\varphi\varphi}\dot\varphi^{2}
+ \Gamma^{\varphi}_{\;\lambda\lambda}\dot\lambda^{2} = 0, \qquad
\ddot\lambda + 2\Gamma^{\lambda}_{\;\varphi\lambda}\dot\varphi\dot\lambda = 0,$$

with the Christoffel symbols from
$\Gamma^{k}_{\;ij} = \tfrac12g^{kl}(\partial_ig_{jl} + \partial_jg_{il} -
\partial_lg_{ij})$. The only non-trivial ones are

$$\Gamma^{\varphi}_{\;\varphi\varphi} = \frac{M'}{M}, \qquad
\Gamma^{\varphi}_{\;\lambda\lambda}
= -\frac{1}{2M^{2}}\frac{d}{d\varphi}\left[(N\cos\varphi)^{2}\right]
= \frac{N\cos\varphi\left(N\sin\varphi - N'\cos\varphi\right)}{M^{2}}, \qquad
\Gamma^{\lambda}_{\;\varphi\lambda} = \Gamma^{\lambda}_{\;\lambda\varphi}
= \frac{N'}{N} - \tan\varphi,$$

where the primes are $d/d\varphi$. These were checked against finite differences of
the metric: at $\varphi = 0.8$ rad the numerical values are $0.0100719856$,
$0.5014217808$ and $-1.0262812286$, against the closed forms $0.0100719856$,
$0.5014217807$ and $-1.0262812286$.

**(b)** $g_{ij}$ does not depend on $\lambda$, so $\lambda$ is a cyclic coordinate
and the conjugate momentum is conserved:

$$\frac{\partial L}{\partial\dot\lambda} = g_{\lambda\lambda}\dot\lambda
= (N\cos\varphi)^{2}\dot\lambda = \text{const},$$

which is **Clairaut's relation**: $N\cos\varphi\sin\alpha = $ constant along the
geodesic, with $\alpha$ the azimuth measured from north. In the spherical limit
$N\to R$ and it reduces to $R\sin\theta\sin\alpha = $ const, the angular-momentum
statement the lesson derives for the sphere. $\square$

**(c)** Compute the Christoffel symbols from the metric by central differences of
$M$ and $N$ (or analytically from their closed forms), then integrate the two
second-order equations with a classical RK4 at a step small enough that the
conserved quantity is preserved: the check is that $N\cos\varphi\sin\alpha$ stays
constant to high precision along a numerically integrated geodesic. A second,
independent check is to integrate the *variational* problem instead — minimise
$\int ds$ by a shooting method on the initial azimuth — and confirm that the two
trajectories agree to the integration tolerance. Without a conserved-quantity check,
a wrong Christoffel sign produces a smooth, plausible, wrong path.

**(d)** The ellipsoidal geodesic is required whenever the *positioning* accuracy
target is below the spherical error, i.e. roughly below $0.3$ per cent of the
distance, which is the order of the flattening effect. Numerically: the spherical
model errs by ~$18.8$ km in a quarter meridian, so for a $1000$ km baseline the
spherical geodesic is wrong by hundreds of metres — negligible for a travel-time
residual at 0.1 s ($600$ m) but decisive for GNSS baselines, for a national
triangulation network, for geoid computation and for any repeated gravity survey
where station coordinates must be consistent to metres. The practical criterion is
therefore: use the ellipsoid when the distance error must be under ~0.1 per cent
(GNSS, geodesy, reference frames) and spherical geometry when the *geophysical*
signal is far larger than that (global tomography, plate-motion rates, tsunami
travel times at basin scale).

---

## ★★★10 — The flat-Earth error, propagated

**(a)** and **(b)** For two points on the $45^\circ$N parallel separated by a
parallel arc $d = R\cos\varphi\,\Delta\lambda$:

| $d$ (km) | great-circle distance (km) | relative error of the parallel arc | $(d/R)^{2}/24$ | ratio |
|---|---|---|---|---|
| 100 | 99.9990 | $-1.027\times10^{-5}$ | $1.0265\times10^{-5}$ | 1.0000 |
| 500 | 499.8716 | $-2.568\times10^{-4}$ | $2.5663\times10^{-4}$ | 1.0005 |
| 1000 | 998.9713 | $-1.0287\times10^{-3}$ | $1.0265\times10^{-3}$ | 1.0022 |
| 2000 | 1991.7166 | $-4.1424\times10^{-3}$ | $4.1061\times10^{-3}$ | 1.0087 |
| 3000 | 2971.7410 | $-9.4200\times10^{-3}$ | $9.2388\times10^{-3}$ | 1.0196 |

The leading term is derived by expanding
$2R\arcsin\!\left(\cos\varphi\sin\frac{\Delta\lambda}{2}\right)$:

$$\text{relative error} = -\frac{(\Delta\lambda)^{2}\sin^{2}\varphi}{24}
= -\frac{(d/R)^{2}\tan^{2}\varphi}{24} + O\!\left(\frac{d^{4}}{R^{4}}\right),$$

using $d = R\cos\varphi\,\Delta\lambda$. At $\varphi = 45^\circ$,
$\tan^{2}\varphi = 1$ and the coefficient is exactly 1, which is why the ratio
column is $1.000$ to $1.002$ — the drift is the next term, growing as
$(d/R)^{2}$. At $30^\circ$ the predicted coefficient is $\tan^{2}30^\circ = 1/3$,
and a direct evaluation at $d = 1000$ km gives a ratio of $0.334$: the general form
is confirmed, and the apparent exactness at $45^\circ$ is the coincidence
$\tan45^\circ = 1$.

**(c)** For two points on the same **meridian** the parallel-arc formula does not
apply: a meridian *is* a great circle, so the great-circle distance equals the
meridional arc exactly (to $10^{-16}$ in the computed values). The error is
therefore not small but **zero**: the flat-Earth error is entirely a
north–south/east–west asymmetry, and it appears only when the path has an
east–west component. At the equator the same reasoning applies through
$\tan^{2}\varphi = 0$: an equatorial parallel is itself a great circle, so the
error vanishes there too.

**(d)** Travel-time errors at $6\ \mathrm{km\,s^{-1}}$ for the $45^\circ$ rows:
$0.0002$ s at 100 km, $0.021$ s at 500 km, $0.171$ s at 1000 km, $1.381$ s at
2000 km, $4.710$ s at 3000 km. For a target precision of 0.05 s, the distance at
which the spherical treatment becomes mandatory satisfies
$(d/R)^{2}/24 = 0.05\times6/d$, i.e.
$d^{3} = 0.3(24)R^{2} = 2.923\times10^{8}$ and $d = 663$ km. So:

* below about **$650$ km** at mid-latitude, a flat-Earth distance is adequate for a
  0.05 s travel-time budget;
* at **$1000$ km** it already costs 0.17 s, three times the budget;
* at **$2000$ km** it costs 1.4 s, larger than most tomographic anomalies.

Note the approximate character of the criterion: it assumes a mid-latitude
east–west path, and the error scales as $\tan^{2}\varphi$, so the same 0.05 s budget
is met up to **957 km** at $30^\circ$N, up to $663$ km at $45^\circ$N, and only up to
**460 km** at $60^\circ$N (verified by direct evaluation: 0.0501 s, 0.0501 s and
0.0500 s respectively). At the equator the error is identically zero, because an
equatorial parallel *is* a great circle.
