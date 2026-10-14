# Exercises — 01-06-05 Line and Surface Integrals; Flux and Circulation

Attempt these **closed-book** before opening the
[solutions](./05-line-surface-integrals-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Use $G = 6.674\times10^{-11}$ unless stated otherwise.

---

## ★ Foundational

**★1.** For the curve $\mathbf{r}(t) = (a\cos t,\ a\sin t,\ ct)$ with
$t \in [0, 2\pi]$:

(a) compute $\mathbf{r}'(t)$ and $\lvert\mathbf{r}'(t)\rvert$;
(b) write the arclength element $dl$ and state whether it is constant;
(c) compute the total arclength.

---

**★2.** A ray travels in a straight line from the origin to the point
$(3, 4, 12)$ km through a medium whose velocity varies as
$v = v_0 + \alpha z$ with $v_0 = 3000$ m/s and $\alpha = 0.2\ \mathrm{s^{-1}}$.

(a) Parametrise the ray by the parameter $t \in [0,1]$ and write $z(t)$.
(b) Write the travel time as a line integral of slowness and state the
substitution you would use.
(c) Compute it (the resulting integral is elementary).

---

**★3.** For the surface $z = g(x,y) = 2x + 3y$ over the unit square
$0 \le x \le 1$, $0 \le y \le 1$:

(a) compute the vector surface element $d\mathbf{A}$ for the upward normal;
(b) compute the scalar surface element $dA$;
(c) compute the area of the surface, and compare it with the area of its
projection.

---

**★4.** Compute the flux of $\mathbf{F} = (0,0,z)$ upward through the disk
$x^2+y^2 \le 4$ in the plane $z = 3$, and then through the same disk in the plane
$z = -3$. State the effect of the orientation choice.

---

## ★★ Applied

**★★5.** For $\mathbf{F} = (2xy,\ x^2,\ 0)$, show that
$\int_C \mathbf{F}\cdot d\mathbf{l}$ is path-independent and evaluate it from
$(0,0,0)$ to $(2,3,0)$ along (a) the straight line and (b) the path consisting of
the two segments $(0,0)\to(2,0)\to(2,3)$.

Identify the potential $\phi$ with $\nabla\phi = \mathbf{F}$ and confirm that
both answers equal $\phi(2,3,0) - \phi(0,0,0)$.

---

**★★6.** A disk of radius $R$ carries an areal density $\sigma$ and lies at
depth $h$ below the observation point, which is on the axis.

(a) Write the vertical attraction as a surface integral and reduce it to a
one-dimensional radial integral, stating each step.
(b) Evaluate it in closed form.
(c) Take $\sigma = 10^5\ \mathrm{kg\,m^{-2}}$ and $h = 100$ m. Compute $g_z$ for
$R = 10^3$, $10^4$ and $10^6$ m, and give each in mGal.
(d) Compute the infinite-sheet limit and state the fractional shortfall at each
radius.

---

**★★7.** A point mass $M$ is at the origin. Compute the flux of
$\mathbf{g} = -GM\hat{r}/r^2$ through the circular cap of the sphere of radius
$R$ defined by $0 \le \theta \le \alpha$.

(a) Show that the flux equals $-2\pi GM(1 - \cos\alpha)$.
(b) Verify that the value for a full sphere ($\alpha = \pi$) is $-4\pi GM$.
(c) Use the result to derive the flux through the curved surface of a cone of
half-angle $\alpha$ with apex at the mass, and comment on the "solid angle"
interpretation.

---

**★★8.** A survey is flown over terrain whose elevation above the datum is
$h(x,y) = 200\sin(0.01x)\cos(0.01y)$ m, with $x$ and $y$ in metres.

(a) Compute $h_x$ and $h_y$, and hence the surface element factor
$\sqrt{1+h_x^2+h_y^2}$.
(b) Evaluate the factor at $x = y = 0$ and at the point where $\lvert\nabla h\rvert$
is largest in the region $\lvert x\rvert, \lvert y\rvert \le 157$ m.
(c) Compute the fractional area excess of the draped surface over its projection
for the largest value found in (b).

---

## ★★★ Research-oriented

**★★★9.** Write a program that computes the travel time of a two-segment ray
through a two-layer medium: a straight segment in the upper layer (velocity
$v_1$, thickness $h_1$) from a source to a point on the interface, then a straight
segment in the lower layer (velocity $v_2$) to a receiver at horizontal offset
$X$ on the surface, with the interface at depth $h_1$.

(a) Write the travel time as a function of the ray parameter (the horizontal
slowness $p$) and state the line integral that produced it.
(b) Show by differentiation that the travel time is stationary when
$\sin\theta_1/v_1 = \sin\theta_2/v_2$, that is Snell's law.
(c) Numerically find the stationary ray for $v_1 = 3000$ m/s, $v_2 = 5000$ m/s,
$h_1 = 500$ m and $X = 2000$ m, and report the travel time to five significant
figures.
(d) Compare it with the travel time of a straight line from source to receiver
through the upper layer only, and with the direct wave; state which is faster and
why the refracted arrival can be the first arrival at large offsets.

---

**★★★10.** Flux of a point-mass field through a cube: independence of position
and size.

Use the field of a point mass $M = 10^{12}$ kg at the origin, and a cube of side
$2a$ centred at $\mathbf{c} = (0,0,0)$.

(a) Compute the flux analytically for any $a$ and state the result.
(b) Compute it numerically for $a = 200$ m and $a = 2000$ m, with a midpoint rule
of at least 200 cells per face, and report the relative error against the analytic
value.
(c) Repeat for a cube centred at $(500, 0, 0)$ m with $a = 2000$ m, so that the
mass is still inside but off-centre. Report the relative error.
(d) Explain the observed dependence of the quadrature error on the position of the
cube, in terms of how well the midpoint rule resolves $\mathbf{g}$ near the faces
closest to the source.
