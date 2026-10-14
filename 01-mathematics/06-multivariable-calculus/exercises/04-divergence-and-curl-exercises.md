# Exercises — 01-06-04 Divergence, Curl and Physical Meaning

Attempt these **closed-book** before opening the
[solutions](./04-divergence-and-curl-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Use $G = 6.674\times10^{-11}$ and, where a magnetic field is required,
$\mu_0 = 4\pi\times10^{-7}$ H/m.

---

## ★ Foundational

**★1.** Compute $\nabla\cdot\mathbf{F}$ and $\nabla\times\mathbf{F}$.

(a) $\mathbf{F} = (x^2,\ 2xy,\ -z)$
(b) $\mathbf{F} = (y z,\ x z,\ x y)$
(c) $\mathbf{F} = (x,\ y,\ z)$
(d) $\mathbf{F} = (-y,\ x,\ 0)$

---

**★2.** For each field of ★1, state whether it is irrotational
($\nabla\times\mathbf{F} = \mathbf{0}$), solenoidal
($\nabla\cdot\mathbf{F} = 0$), both, or neither.

---

**★3.** The velocity of a rigid body rotating with angular velocity
$\boldsymbol{\Omega} = (0,0,\Omega)$ is $\mathbf{v} =
\boldsymbol{\Omega}\times\mathbf{r}$.

(a) Compute $\nabla\cdot\mathbf{v}$ and $\nabla\times\mathbf{v}$.
(b) State what the second result says about the vorticity of rigid rotation, and
explain why "the fluid is rotating" and "the flow has vorticity" are not the same
statement.
(c) Evaluate the magnitude of the vorticity for
$\Omega = 7.2921\times10^{-5}$ rad/s, and state its units.

---

**★4.** The gravitational field of a point mass $M$ at the origin is
$\mathbf{g} = -GM\hat{r}/r^2$.

(a) Compute $\nabla\cdot\mathbf{g}$ at $\mathbf{r} = (700, 400, -900)$ m.
(b) Compute $\nabla\times\mathbf{g}$ at the same point.
(c) Compute $\lvert\mathbf{g}\rvert$ at that point for $M = 10^{12}$ kg, and state
the ratio of your answers to (a) and (b) to the natural scale $\lvert\mathbf{g}\rvert/r$.

---

## ★★ Applied

**★★5.** A long straight wire carries a current $I = 2.5$ kA along the $z$ axis,
so $\mathbf{B} = \frac{\mu_0 I}{2\pi\rho}\hat{\phi}$.

(a) Compute $\oint\mathbf{B}\cdot d\mathbf{l}$ around a circle of radius 25 m and
state the enclosed current.
(b) Repeat for a radius of 100 m. State why the answer does not change.
(c) Compute $\nabla\times\mathbf{B}$ at a point $(\rho,\phi,z) = (40, 0.3, 12)$
with $\rho$ in metres, and explain how the curl can be zero everywhere off the
wire while the circulation is not.

---

**★★6.** Repeat the wire of ★★5 but with the loop replaced by a square of side
$2a$ centred on the wire, in the plane $z = 0$.

(a) Compute $\oint\mathbf{B}\cdot d\mathbf{l}$ around the square by direct
integration of the four sides.
(b) Show that the result is $\mu_0I$ independent of $a$.
(c) State which theorem you have just verified, and what it requires of the field
on the path.

---

**★★7.** A uniform ball of radius $a$ and density $\rho$ has gravitational field
magnitude $g(r) = \frac{4}{3}\pi G\rho r$ for $r \le a$ and
$g(r) = \frac{GM}{r^2}$ for $r \ge a$.

(a) Compute $\nabla\cdot\mathbf{g}$ inside and outside the ball.
(b) Evaluate $\nabla\cdot\mathbf{g}$ numerically at $r = 0.5a$ using central
differences with the field expressed in Cartesian coordinates, and compare with
$-4\pi G\rho$.
(c) Explain why the answer inside is not simply $-4\pi G\rho$ at every point if
you sample the divergence on a grid that straddles the boundary.

---

**★★8.** Decide, for each field, whether a scalar potential exists on the stated
domain, and justify your answer.

(a) $\mathbf{F} = (2xy,\ x^2 - z^2,\ -2yz)$ on all of $\mathbb{R}^3$.
(b) $\mathbf{F} = \left(\dfrac{-y}{x^2+y^2},\ \dfrac{x}{x^2+y^2},\ 0\right)$ on
$\mathbb{R}^3$ minus the $z$ axis.
(c) $\mathbf{F} = (y,\ -x,\ 0)$ on the unit disk in the plane.

For (a), if a potential exists, find it.

---

## ★★★ Research-oriented

**★★★9.** Verify numerically that the magnetic field of a dipole is
divergence-free, and characterise the numerical floor.

Take $\mathbf{B} = \frac{\mu_0}{4\pi}\frac{3(\mathbf{m}\cdot\hat{r})\hat{r} -
\mathbf{m}}{r^3}$ with $|\mathbf{m}| = 8\times10^{22}$ A m² along $z$, and
evaluate $\nabla\cdot\mathbf{B}$ by central differences at a sequence of points
along the ray $\mathbf{r} = t(5,3,4)$ Mm for $t = 1, 2, 4$.

(a) Report the measured divergence and the natural scale $\lvert\mathbf{B}\rvert/r$
at each point.
(b) Report the ratio and explain how it depends on the finite-difference step.
(c) Repeat with steps $h = 10^2$, $10^3$ and $10^4$ m at the fixed point
$\mathbf{r} = (5,3,4)$ Mm and state the observed convergence order.
(d) State what the exercise does and does not establish about $\nabla\cdot\mathbf{B}=0$.

---

**★★★10.** Gauss's law through a curved surface. A point mass of $10^{12}$ kg is
at the origin. Consider the closed surface formed by a cube of side 2 km centred
on the mass, but with its top face (the face at $z = +1$ km) replaced by a
hemisphere of radius 1 km bulging upward.

(a) Compute the flux of $\mathbf{g}$ through this surface analytically, using
Gauss's law, and state it in m³/s².
(b) Explain why the answer is independent of the deformation, and identify the
precise hypotheses of the divergence theorem that are being used.
(c) Describe how you would compute the flux numerically, and estimate the order of
the quadrature error for a midpoint rule with $n$ cells per face.
(d) If the surface instead enclosed half the mass distribution, what would the
flux be, and why does the answer require the divergence theorem applied to each
piece rather than to the whole?
