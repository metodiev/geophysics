# Exercises — 01-04-05 Surfaces, Parametrisation and Curvature

Attempt these **closed-book**. Solutions are in
[`05-surfaces-and-curvature-solutions.md`](./05-surfaces-and-curvature-solutions.md).
Difficulty: ★ foundational · ★★ applied · ★★★ research-oriented.

Use $R = 6371.0088$ km for the Earth unless stated. Report curvature in consistent
units and say which.

---

## ★ Foundational

**★1.** Compute $E$, $F$ and $G$ for:

(a) the sphere $\mathbf{X}(\varphi,\lambda) = R(\cos\varphi\cos\lambda,
\cos\varphi\sin\lambda, \sin\varphi)$ with $u = \varphi$, $v = \lambda$;
(b) a graph surface $\mathbf{g}(x,y) = (x, y, h(x,y))$.

For each, write the arc-length element $ds^{2}$ and the area element $dA$.

---

**★2.** Slope-area correction. For a planar slope of dip $\alpha$:

(a) show that the surface area is $1/\cos\alpha$ times the planimetric (map) area;
(b) evaluate the factor at $30°$, $45°$ and $60°$;
(c) state what a terrain-analysis workflow that ignores the correction gets wrong,
and in which direction.

---

**★3.** The Earth's curvature in practice.

(a) Compute the drop below the tangent plane at $1$ km, $10$ km and $100$ km, both
exactly and with the parabolic approximation, and give the ratio.
(b) Compute the geometric horizon distance from heights of $2$ m and $100$ m.
(c) State the height above which the horizon exceeds $50$ km.
(d) Explain why the parabolic approximation is acceptable at 10 km and inadequate
at 500 km, with numbers.

---

## ★★ Applied

**★★4.** Derive $K = 1/R^{2}$ for the sphere from the fundamental forms.

(a) Compute $\mathbf{X}_{\varphi\varphi}$ and show that the outward normal is
$\mathbf{X}/R$.
(b) Compute $L$, $M$ and $N$.
(c) Compute $K$ and $H$.
(d) Explain the sign of $H$ and why only $|H|$ is comparable with published values.

---

**★★5.** The paraboloid $h(x,y) = (x^{2}+y^{2})/(2R)$ with $R = 6371.0088$ km.

(a) Compute $h_x$, $h_y$, $h_{xx}$, $h_{xy}$, $h_{yy}$.
(b) Use the graph formula
$K = (h_{xx}h_{yy} - h_{xy}^{2})/(1+h_x^{2}+h_y^{2})^{2}$ to obtain $K(\rho)$.
(c) Evaluate $K$ at the apex and at $\rho = R$.
(d) Convert both to SI units and state why gravity-gradient quantities are usually
quoted in eötvös rather than $\mathrm{s^{-2}}$.
(e) State the physical situation this surface models, and one reason it is only a
first-order approximation.

---

**★★6.** The saddle $h(x,y) = xy$ (any units).

(a) Compute the second derivatives and hence $K$ and $H$ from the graph formulas.
(b) Evaluate $K$ and $H$ at $(0,0)$, $(1,1)$ and $(2,0)$.
(c) State what $H = 0$ means, and whether this surface is a minimal surface.
(d) Explain what the sign of $K$ tells you about the local shape.

---

**★★7.** Numerical curvature: choose the step.

(a) State the two competing error mechanisms in a numerical second derivative.
(b) Using the measured data below for a sphere of radius $6371$ km (in $\mathrm{km^{-2}}$
units, with the exact value $2.463682790395\times10^{-8}$), tabulate the relative
error and identify the optimal step:

| step $h$ (rad) | $K$ numeric |
|---|---|
| $10^{-1}$ | $2.476037213620\times10^{-8}$ |
| $10^{-2}$ | $2.463805978126\times10^{-8}$ |
| $10^{-3}$ | $2.463684022357\times10^{-8}$ |
| $10^{-4}$ | $2.463682812484\times10^{-8}$ |
| $10^{-5}$ | $2.463680788859\times10^{-8}$ |

(c) Confirm the $h^{2}$ scaling of the truncation branch from the numbers.
(d) Convert the optimal step into kilometres and state how you would choose a step
for a gridded horizon surface.

---

**★★8.** Geodesics and geodesic curvature.

(a) Define a geodesic on a surface.
(b) Show that the equator is a geodesic of a sphere, and that a latitude circle at
latitude $\varphi \ne 0$ is not.
(c) Derive or quote the geodesic curvature of a parallel at latitude $\varphi$, and
evaluate it at $45°$N and $60°$N.
(d) State one geophysical context in which the distinction between a geodesic and a
parallel matters.

---

## ★★★ Research-oriented

**★★★9.** Verify a curvature implementation.

(a) Implement Gaussian and mean curvature numerically from the first and second
fundamental forms for a general parametrised surface.
(b) Test it on a sphere of radius $R$ over a grid of $(\theta,\phi)$ and report the
worst relative error in $K$ against the exact $1/R^{2}$.
(c) Test it on the paraboloid of ★★5 and report the worst error against the closed
form over $\rho \in [0, R]$.
(d) Test it on a surface of your own construction whose $K$ you can compute
analytically — for example a surface of revolution — and report which one is hardest
for your implementation.
(e) Explain the hardest case in terms of the conditioning of the numerical
derivatives, and state what accuracy a topographic curve-fitting workflow could
realistically claim.
(f) State the limits of your tests.

---

**★★★10.** Model the optimal step length.

(a) Model the total relative error of a second-order central second difference as
$E(h) = a h^{2} + b/h^{2}$, where the first term is truncation and the second is
round-off. Fit $a$ and $b$ to the data of ★★7.
(b) Predict the optimal step from your fit, and compare with the measured optimum.
(c) Predict the minimum achievable relative error, and compare with the measured
$8.97\times10^{-9}$.
(d) Show analytically that the optimal step scales as $\varepsilon^{1/4}$ times the
length scale, where $\varepsilon$ is machine epsilon, and check the constant against
your fit.
(e) Explain why a curvature calculation is intrinsically harder than a slope
calculation, in terms of this scaling.
(f) State the limits of the model: what does the two-term form $E(h)$ ignore?

---

## Extension ideas

- Compute the curvature of a real (or synthetic) topographic surface from a gridded
  DEM by fitting a quadratic to each $3\times3$ neighbourhood, and compare the
  Hessian-based curvature with the Gaussian curvature from the fundamental forms.
- Implement the geodesic equation on a surface of revolution numerically and verify
  that Clairaut's relation (a conserved quantity along the geodesic) holds — this is
  the surface analogue of the ray parameter, and it connects directly to
  [01-03-03](../../03-trigonometry/03-inverse-trig.md).
