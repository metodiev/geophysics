# Solutions — 01-06-05 Line and Surface Integrals; Flux and Circulation

> **Read this after attempting the exercises, not before.**
>
> Throughout, $G = 6.674\times10^{-11}$ and $1\ \mathrm{mGal} =
> 10^{-5}\ \mathrm{m\,s^{-2}}$.

---

## ★1 — Arclength of a helix

**(a)** $\mathbf{r}'(t) = (-a\sin t,\ a\cos t,\ c)$ and

$$\lvert\mathbf{r}'(t)\rvert = \sqrt{a^2\sin^2 t + a^2\cos^2 t + c^2}
= \sqrt{a^2+c^2}.$$

**(b)** $dl = \lvert\mathbf{r}'(t)\rvert\,dt = \sqrt{a^2+c^2}\,dt$ — **constant**.
A curve parametrised so that the speed is constant is said to be parametrised by
arclength up to a scale factor.

**(c)**

$$L = \int_0^{2\pi}\sqrt{a^2+c^2}\,dt = 2\pi\sqrt{a^2+c^2}.$$

**Check.** For $c = 0$ the helix degenerates to a circle of radius $a$ and
$L = 2\pi a$ ✓. For $a = 0$ it degenerates to a segment of the $z$ axis of height
$2\pi c$ and $L = 2\pi c$ ✓. Both limits are correct, which is the kind of check
worth doing before trusting a formula.

---

## ★2 — Travel time along a straight ray

**(a)** The straight line from $(0,0,0)$ to $(3000, 4000, 12000)$ m (the endpoint
converted from kilometres) is

$$\mathbf{r}(t) = t\,(3000,\ 4000,\ 12000), \qquad t \in [0,1],$$

so $z(t) = 12000 t$ m.

**(b)** With $v(z) = v_0 + \alpha z = 3000 + 0.2\,z$ and
$\lvert\mathbf{r}'\rvert = \sqrt{3000^2+4000^2+12000^2} = \sqrt{1.69\times10^{8}}
= 13000$ m (constant, because the path is straight),

$$T = \int_0^1 \frac{\lvert\mathbf{r}'\rvert}{v(z(t))}\,dt
= \int_0^1 \frac{13000}{3000 + 2400t}\,dt .$$

The substitution is not needed: the integrand is already of the form
$(A + Bt)^{-1}$.

**(c)**

$$T = 13000\int_0^1\frac{dt}{3000+2400t}
= \frac{13000}{2400}\ln\left(\frac{3000+2400}{3000}\right)
= 5.41667\ln(1.8) = 5.41667 \times 0.587787
= 3.18384\ \mathrm{s}.$$

$$\boxed{T = 3.1838\ \mathrm{s}}$$

**Two remarks.** First, the answer is *shorter* than the straight-line travel time
at constant $v_0 = 3000$ m/s, which would be $13000/3000 = 4.333$ s — because the
ray spends its later part in faster material. Second, the line integral was
trivial here only because the path was chosen in advance. In a general velocity
field the path itself is unknown and is determined by the stationarity condition
(Section ★★★9): the integral and the path must be solved for together.

---

## ★3 — Surface element of a sloping plane

**(a)** For $z = g(x,y) = 2x+3y$, the upward normal is proportional to
$(-g_x,\ -g_y,\ 1) = (-2,-3,1)$, so

$$d\mathbf{A} = (-2,\ -3,\ 1)\,dx\,dy .$$

**(b)**

$$dA = \sqrt{1 + g_x^2 + g_y^2}\,dx\,dy = \sqrt{1+4+9}\,dx\,dy = \sqrt{14}\,dx\,dy .$$

**(c)**

$$\text{Area} = \int_0^1\!\!\int_0^1 \sqrt{14}\,dx\,dy = \sqrt{14} = 3.74166 .$$

The projected area is $1$, so the surface is $3.74$ times larger than its
projection. **The factor $\sqrt{14}$ is exactly what a terrain correction must
account for**: a survey that computes quantities per unit *projected* area
underestimates them by this factor on a slope of this steepness. (A gradient of
$(2,3)$ corresponds to a slope angle of
$\arctan\sqrt{13} = 74.5^\circ$, which is extreme, and the factor is correspondingly
large — the same formula on a gentle $5^\circ$ slope gives only $1.004$.)

---

## ★4 — Flux and orientation

$\mathbf{F} = (0,0,z)$; on the disk $z = 3$, $\mathbf{F} = (0,0,3)$ and the
upward normal is $\hat{z}$, so $\mathbf{F}\cdot d\mathbf{A} = 3\,dA$ and

$$\Phi = 3 \times \text{area} = 3 \times \pi(2)^2 = 12\pi = 37.699 .$$

On the disk at $z = -3$ with the **same** (upward) normal, $\mathbf{F} = (0,0,-3)$
and $\mathbf{F}\cdot\hat{z} = -3$, so $\Phi = -12\pi = -37.699$.

**The orientation choice changes the sign and nothing else.** A flux is a signed
quantity: it answers "how much crosses the surface, and in which direction". Any
statement of a flux result that does not state the orientation is incomplete, and
this is the most common source of sign errors in this part of the subject.

---

## ★★5 — Path independence for a gradient field

$\mathbf{F} = (2xy,\ x^2,\ 0)$. Since

$$\nabla\times\mathbf{F} = \left(0-0,\ 0-0,\ \frac{\partial(x^2)}{\partial x}
- \frac{\partial(2xy)}{\partial y}\right) = (0,0,2x-2x) = \mathbf{0}$$

on all of $\mathbb{R}^3$, which is simply connected, a potential exists:
$\phi = x^2y$ gives $\phi_x = 2xy$ ✓, $\phi_y = x^2$ ✓, $\phi_z = 0$ ✓.

**(a) Straight line** from $(0,0,0)$ to $(2,3,0)$:
$\mathbf{r}(t) = (2t, 3t, 0)$, $\mathbf{r}' = (2,3,0)$,
$\mathbf{F}(\mathbf{r}(t)) = (2\cdot2t\cdot3t,\ 4t^2,\ 0) = (12t^2,\ 4t^2,\ 0)$, so

$$\int_C\mathbf{F}\cdot d\mathbf{l} = \int_0^1\left(12t^2\cdot2 + 4t^2\cdot3\right)dt
= \int_0^1 36t^2\,dt = 12 .$$

**(b) Two segments.** Along $(0,0,0)\to(2,0,0)$: $y = 0$, so $\mathbf{F} = (0,x^2,0)$
and $d\mathbf{l} = (dx,0,0)$ give $\mathbf{F}\cdot d\mathbf{l} = 0$. Along
$(2,0,0)\to(2,3,0)$: $x = 2$, $\mathbf{F} = (4y, 4, 0)$, $d\mathbf{l} = (0,dy,0)$, so

$$\int_0^3 4\,dy = 12 .$$

**Comparing with the potential.** $\phi(2,3,0) - \phi(0,0,0) = 4\cdot3 - 0 = 12$,
matching both routes. The second path is instant to evaluate; the first required a
substitution. **This is exactly the practical value of a potential: it converts a
path integral into a subtraction at the endpoints.**

The lesson's Section 3.1 proved the general statement — the integrand
$\nabla\phi\cdot\mathbf{r}'(t)$ is a total derivative — and this exercise is that
proof instantiated twice.

---

## ★★6 — Gravity of a uniform disk

**(a)** With the disk at depth $h$ below the station, a ring of radius $\rho$ and
width $d\rho$ carries mass $2\pi\sigma\rho\,d\rho$ and is at distance
$\sqrt{\rho^2+h^2}$ from the station. Its vertical contribution is
$G(2\pi\sigma\rho\,d\rho)\,h/(\rho^2+h^2)^{3/2}$, so the surface integral reduces
to

$$g_z = 2\pi G\sigma h\int_0^R \frac{\rho\,d\rho}{\left(\rho^2+h^2\right)^{3/2}} .$$

**(b)** Since
$\int\rho(\rho^2+h^2)^{-3/2}d\rho = -(\rho^2+h^2)^{-1/2}$,

$$g_z = 2\pi G\sigma h\left[-\frac{1}{\sqrt{\rho^2+h^2}}\right]_0^R
= 2\pi G\sigma\left(1 - \frac{h}{\sqrt{R^2+h^2}}\right).$$

**(c)** With $\sigma = 10^5\ \mathrm{kg\,m^{-2}}$ and $h = 100$ m,
$2\pi G\sigma = 4.19340\times10^{-5}\ \mathrm{m\,s^{-2}} = 4.19340$ mGal:

| $R$ (m) | $h/\sqrt{R^2+h^2}$ | $g_z$ (m/s²) | $g_z$ (mGal) |
|---|---|---|---|
| $10^3$ | 0.099504 | $3.77614\times10^{-5}$ | 3.77614 |
| $10^4$ | 0.0099995 | $4.15147\times10^{-5}$ | 4.15147 |
| $10^6$ | $9.99999\times10^{-5}$ | $4.19298\times10^{-5}$ | 4.19298 |

**(d)** The infinite-sheet limit is $2\pi G\sigma = 4.19340$ mGal. The fractional
shortfalls are

$$R = 10^3\ \mathrm{m}:\ 9.95\%, \qquad R = 10^4\ \mathrm{m}:\ 1.00\%, \qquad
R = 10^6\ \mathrm{m}:\ 1.0\times10^{-4}.$$

The approach to the limit is $O(h/R)$, not $O(h^2/R^2)$: to be within 1 %, the
sheet must be about 100 times wider than the observation height. **This is the
quantitative content of "the Bouguer slab approximation",** and it is why terrain
corrections matter even for large survey areas on high topography.

**Independent check.** The same closed form was verified against direct radial
quadrature in the module demonstration, agreeing to between
$2.9\times10^{-8}$ and $2.6\times10^{-7}$ relative over the same range of $R$.

---

## ★★7 — Flux through a spherical cap

**(a)** On the sphere of radius $R$, $\mathbf{g}\cdot\hat{r} = -GM/R^2$ and
$dA = R^2\sin\theta\,d\theta\,d\phi$, so

$$\Phi = \int_0^{2\pi}\!\!\int_0^{\alpha}
\left(-\frac{GM}{R^2}\right)R^2\sin\theta\,d\theta\,d\phi
= -GM\cdot2\pi\left[-\cos\theta\right]_0^{\alpha}
= -2\pi GM\left(1-\cos\alpha\right).$$

Note that $R$ has cancelled: the flux depends on the cone's half-angle, not on the
radius.

**(b)** At $\alpha = \pi$, $1-\cos\pi = 2$, so $\Phi = -4\pi GM$ ✓ — Gauss's law
for a point mass.

**(c)** The solid angle subtended by the cap at the mass is
$\Omega = 2\pi(1-\cos\alpha)$, and

$$\Phi = -GM\,\Omega .$$

Equivalently, the flux through the **conical surface** $\theta = \alpha$
(outward normal pointing away from the axis) plus the cap must equal $-4\pi GM$
for a closed surface. For the cone with its apex at the mass, the field lies along
the cone's generators, so $\mathbf{g}\cdot d\mathbf{A} = 0$ on the cone itself
(the normal is perpendicular to $\hat{r}$). Hence the cone contributes nothing and
the cap carries the whole flux. **The interpretation is the solid-angle one: the
flux is proportional to the solid angle subtended, with $-GM$ per steradian.** The
constant of proportionality is fixed by the full sphere giving $-4\pi GM$ for
$4\pi$ steradians.

Numerically, with $\alpha = \pi/2$ and $M = 10^{12}$ kg, $\Phi = -2\pi GM
= -4.1934\times10^{2}$ m³/s².

---

## ★★8 — Draped surface area over topography

**(a)** $h = 200\sin(0.01x)\cos(0.01y)$, so

$$h_x = 200(0.01)\cos(0.01x)\cos(0.01y) = 2\cos(0.01x)\cos(0.01y),$$

$$h_y = -2\sin(0.01x)\sin(0.01y),$$

$$\sqrt{1+h_x^2+h_y^2}
= \sqrt{1 + 4\left[\cos^2(0.01x)\cos^2(0.01y)
+ \sin^2(0.01x)\sin^2(0.01y)\right]} .$$

**(b)** At $x = y = 0$: $h_x = 2$, $h_y = 0$, factor $= \sqrt{5} = 2.23607$.

At the point where $\lvert\nabla h\rvert$ is largest in
$\lvert x\rvert, \lvert y\rvert \le 157$ m: the bracket
$\cos^2 a\cos^2 b + \sin^2 a\sin^2 b$ (with $a = 0.01x$, $b = 0.01y$, so
$0 \le a, b \le \pi/2$) reaches its maximum value of $1$ at $a = b = 0$ and again
at $a = b = \pi/2$, that is at $x = y = 0$ and at
$x = y = 157$ m. In both cases the factor is

$$\sqrt{1+4} = \sqrt{5} = 2.23607 .$$

(At intermediate points the bracket can be as small as $0$, at $a = \pi/2$,
$b = 0$, where the surface is locally flat and the factor is $1$.)

**(c)** The largest fractional excess is

$$\sqrt{5} - 1 = 1.23607, \quad\text{that is}\quad 123.6\%.$$

**Interpretation.** The surface undulation has amplitude 200 m and wavelength
$2\pi/0.01 = 628$ m, a maximum slope of $200 \times 0.01 \times \sqrt{2} \approx
2.83$ — a $71^\circ$ slope. Such terrain is extreme, and the point of the exercise
is the formula and the size of the effect, not the realism of the parameters.
At the more typical maximum slope of $10^\circ$ the factor is $1.015$, a 1.5 %
correction — which is exactly the order of the terrain correction that must be
applied before a gravity anomaly can be interpreted.

---

## ★★★9 — The refraction problem, stationarity and Snell's law

**Setup.** Source at the surface $z=0$; receiver at horizontal offset $X = 2000$ m
on the same surface; interface at depth $h_1 = 500$ m; $v_1 = 3000$ m/s above,
$v_2 = 5000$ m/s below. The two-segment path crosses the interface at horizontal
distance $x$ from the source, making angles $\theta_1$, $\theta_2$ **measured from
the vertical**, so that

$$l_1 = \sqrt{x^2+h_1^2}, \qquad l_2 = \sqrt{(X-x)^2+h_1^2}, \qquad
\sin\theta_1 = \frac{x}{l_1}, \qquad \sin\theta_2 = \frac{X-x}{l_2}.$$

**(a)** The travel time is the sum of two line integrals of slowness along
straight segments,

$$T(x) = \int_{\text{seg 1}}\frac{dl}{v_1} + \int_{\text{seg 2}}\frac{dl}{v_2}
= \frac{\sqrt{x^2+h_1^2}}{v_1} + \frac{\sqrt{(X-x)^2+h_1^2}}{v_2},$$

which is a function of the single parameter $x$ — or, equivalently, of the ray
parameter $p = \sin\theta_1/v_1$.

**(b)** Differentiating,

$$\frac{dT}{dx} = \frac{x}{v_1\sqrt{x^2+h_1^2}}
- \frac{X-x}{v_2\sqrt{(X-x)^2+h_1^2}}
= \frac{\sin\theta_1}{v_1} - \frac{\sin\theta_2}{v_2} .$$

Setting $dT/dx = 0$ gives

$$\frac{\sin\theta_1}{v_1} = \frac{\sin\theta_2}{v_2},$$

which is **Snell's law**. Fermat's principle is the statement that the physical
ray makes $T$ stationary; the stationarity condition *is* Snell's law, so the two
are not independent postulates.

Note the two terms have opposite signs, as they must: moving the crossing point to
the right lengthens the upper segment and shortens the lower one, and only at the
balance point is the sum stationary.

**(c)** Solving $\sin\theta_2 = (v_2/v_1)\sin\theta_1$ together with the geometric
constraint $x + (X-x) = X$, i.e.
$h_1\left(\tan\theta_1+\tan\theta_2\right) = X$, by bisection on $\theta_1$:

$$\theta_1 = 35.0433^\circ, \qquad \theta_2 = 73.1352^\circ,$$

$$x = 350.667\ \mathrm{m}, \qquad X - x = 1649.333\ \mathrm{m},$$

$$l_1 = 610.711\ \mathrm{m}, \qquad l_2 = 1723.456\ \mathrm{m},$$

$$T = \frac{610.711}{3000} + \frac{1723.456}{5000}
= 0.203570 + 0.344691 = \boxed{0.548261\ \mathrm{s}} .$$

**Verification of the stationarity condition:**

$$\frac{\sin\theta_1}{v_1} = 1.91398\times10^{-4}\ \mathrm{s\,m^{-1}}, \qquad
\frac{\sin\theta_2}{v_2} = 1.91398\times10^{-4}\ \mathrm{s\,m^{-1}} .$$

Agreement to all displayed digits. Also note that the critical angle is
$\arcsin(v_1/v_2) = 36.870^\circ$, and the solution has
$\theta_1 = 35.043^\circ$, below the critical angle — as it must be for a
transmitted ray to exist at all.

**(d)** The direct arrival travelling in the upper layer at $v_1$ takes

$$T_{\text{direct}} = \frac{X}{v_1} = \frac{2000}{3000} = 0.666667\ \mathrm{s},$$

which is **0.1184 s slower** than the refracted path. The refracted arrival is the
first arrival because the ray spends 1723 m of its 2334 m path (74 %) in the faster
medium even though it must dive to 500 m depth. At small offsets the geometry
penalises the dive and the direct arrival wins; the two travel-time curves cross,
and beyond the crossover the refracted arrival remains first.

**The general lesson.** A physical law was *obtained* from a stationarity
condition rather than postulated alongside it. That structure — an action or a
travel-time functional plus a variational principle — is how the ray equations,
the elastodynamic equations and the least-squares normal equations are all
derived, and it is why the calculus of variations is worth learning later. See
[01-14 Optimization and Variational Methods](../../14-optimization/README.md) and
[06-seismology](../../../06-seismology/README.md).

## ★★★10 — Flux of a point-mass field through cubes

**Method.** The flux was computed face by face with a midpoint rule of $n$ cells
per side, summing the oriented contributions $\mathbf{g}\cdot\hat{n}$ times the
cell area. The mass is $M = 10^{12}$ kg at the origin.

**(a)** For any cube (indeed any closed surface) containing the mass,

$$\oint\mathbf{g}\cdot d\mathbf{A} = -4\pi GM
= -4\pi(6.674\times10^{-11})(10^{12})
= -838.679575\ \mathrm{m^{3}\,s^{-2}} .$$

**(b)** Measured:

| $a$ (m) | centre (m) | $n$ | flux (m³/s²) | relative error |
|---|---|---|---|---|
| 200 | $(0,0,0)$ | 200 | $-838.684712$ | $6.13\times10^{-6}$ |
| 2000 | $(0,0,0)$ | 200 | $-838.684712$ | $6.13\times10^{-6}$ |
| 2000 | $(500,0,0)$ | 200 | $-838.684691$ | $6.10\times10^{-6}$ |
| 2000 | $(500,0,0)$ | 600 | $-838.680143$ | $6.78\times10^{-7}$ |

**(c)** Reported above. The off-centre cube gives essentially the same error as the
centred one.

**(d)** Two observations, both instructive.

- **The error is independent of the cube's size.** This is not a coincidence: the
  field $\mathbf{g} = -GM\hat{r}/r^2$ is scale-invariant, so doubling the cube and
  doubling the cell size produce a geometrically identical discretisation. It is a
  useful reminder that the accuracy of a quadrature is governed by the *ratio* of
  the cell size to the length scale of the integrand, not by either alone.
- **The error is insensitive to the cube's position, to the accuracy measured.** I
  expected the off-centre cube to be worse, because its closest face lies only
  1500 m from the mass. It is not: the error changed from
  $6.13\times10^{-6}$ to $6.10\times10^{-6}$. The reason is that the integrand
  near that face is still smooth on the discretisation scale — the cell size is
  $4000/200 = 20$ m against a 1500 m distance to the source, a ratio of 0.013 — so
  the local truncation error is not materially larger there. **The expectation was
  wrong, and only the measurement settled it.**

  The expectation would become correct for a much closer face: if the nearest
  source-face distance approached the cell size, the integrand's curvature would
  dominate and the error would grow.

- **The error is second order in the cell size.** Refining from $n = 200$ to
  $n = 600$ (a factor of 3 in the cell size) reduced the relative error by a
  factor of 9.0, exactly the $h^2 \propto n^{-2}$ of the midpoint rule applied to
  a smooth integrand.

**Limitations.** (i) The flux is a cancellation of six large face integrals, so
the accuracy is limited by the *relative* error of the largest face, not by the
smallest — a general hazard in flux computations. (ii) The measurement cannot
distinguish a second-order convergence constant from slightly different values; a
finer sequence of $n$ would be needed to pin the order to more than one significant
figure. (iii) All of this concerns a *smooth* field away from its source; a source
close to a face, or on it, would change the analysis completely.
