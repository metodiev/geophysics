# Solutions — 06-02-04 Ray Tracing in Laterally Varying Media

> **Read after attempting the exercises.** Numbers were computed, not estimated
> by hand; where a problem admits more than one defensible answer it is said so.

Lesson: [04 Ray Tracing in Laterally Varying Media](../04-ray-tracing.md).

---

## ★1 — Ray parameter and arc radius

$$p = \frac{\sin i_0}{v_0} = \frac{0.5}{2500} = 2.000000\times10^{-4}\
\mathrm{s\,m^{-1}},$$
$$R = \frac{v_0}{G\sin i_0} = \frac{2500}{0.60 \times 0.5}
= 8333.33\ \mathrm{m} = 8.333\ \mathrm{km}.$$

The radius is a length: $\mathrm{(m\,s^{-1})/(s^{-1})} = \mathrm{m}$.

---

## ★2 — Turning depth, offset and time

$$z_t = R - \frac{v_0}{G} = 8333.33 - \frac{2500}{0.60}
= 8333.33 - 4166.67 = 4166.67\ \mathrm{m} = 4.167\ \mathrm{km},$$

$$X = 2R\cos\theta_0 = 2(8333.33)(0.866025) = 14433.8\ \mathrm{m}
= 14.434\ \mathrm{km},$$

$$T = \frac{2}{G}\ln\frac{1}{\tan(i_0/2)}
= \frac{2}{0.60}\ln\frac{1}{\tan 15^\circ}
= 3.333333 \times 1.316958 = 4.389860\ \mathrm{s}.$$

Since $\theta_0 = i_0$ at the surface (the take-off angle *is* the angle from the
vertical), $\theta_0/2 = 15^\circ$.

---

## ★3 — Dimensional check of the ray equation

$\mathrm{d}\mathbf{x}/\mathrm{d}s$ is dimensionless (length over arc length), so
$v^{-1}\mathrm{d}\mathbf{x}/\mathrm{d}s$ has units $\mathrm{s\,m^{-1}}$ — a
slowness. Differentiating with respect to $s$ (metres) gives
$\mathrm{s\,m^{-2}}$. The right-hand side
$\nabla(v^{-1}) = -v^{-2}\nabla v$ has units
$(\mathrm{m\,s^{-1}})^{-2}(\mathrm{m\,s^{-1}\,m^{-1}}) = \mathrm{s^2\,m^{-2}}
\times \mathrm{s^{-1}} = \mathrm{s\,m^{-2}}$. ✔ Both sides agree, as they must —
and the check catches exactly the error of integrating in depth instead of in arc
length.

---

## ★4 — The two-point problem

Exact. With $X = (2v_0/G)\cot i_0$:

$$\cot i_0 = \frac{GX}{2v_0} = \frac{0.60 \times 10000}{2 \times 2500} = 1.200000
\quad\Longrightarrow\quad i_0 = 39.8056^\circ,$$

$$p = \frac{\sin 39.8056^\circ}{2500} = \frac{0.640185}{2500}
= 2.560738\times10^{-4}\ \mathrm{s\,m^{-1}},$$

$$T = \frac{2}{0.60}\ln\frac{1}{\tan 19.9028^\circ}
= 3.333333 \times 1.015973 = 3.386577\ \mathrm{s}.$$

By bracketing. At $30^\circ$, $X = (2 \times 2500/0.60)\cot 30^\circ
= 8333.33(1.732051) = 14433.8$ m; at $45^\circ$,
$X = 8333.33(1.000000) = 8333.3$ m. Linear interpolation in $i_0$:

$$i_0 \approx 30^\circ + 15^\circ\frac{14433.8 - 10000.0}{14433.8 - 8333.3}
= 30^\circ + 15^\circ(0.726795) = 40.902^\circ .$$

Interpolation error: $40.902^\circ - 39.806^\circ = 1.096^\circ$ — a 2.8 %
error in angle from a two-point bracket, which is why the bracket is only the
first step and refinement (bisection or Newton) is the second. Note that the
bracket *does* establish uniqueness here: $X(i_0)$ is monotone decreasing, so
there is exactly one root in $(30^\circ, 45^\circ)$.

---

## ★5 — Time errors across the comparison

| Δ | engine $T$ (s) | tracer $T$ (s) | error (s) | relative error |
|---|---|---|---|---|
| 30° | 370.2639 | 370.0524 | $-0.2115$ | $-5.7\times10^{-4}$ |
| 45° | 496.9685 | 496.9802 | $+0.0117$ | $+2.4\times10^{-5}$ |
| 60° | 608.2804 | 608.3122 | $+0.0318$ | $+5.2\times10^{-5}$ |
| 75° | 703.2422 | 703.3190 | $+0.0768$ | $+1.1\times10^{-4}$ |
| 90° | 781.3348 | 782.1434 | $+0.8086$ | $+1.0\times10^{-3}$ |

The agreement is best between 45° and 75° (better than $1.2\times10^{-4}$
relative, and better than 0.08 s absolute). It degrades at both ends: at 30° the
ray turns at shallow depth where the model is sampled most coarsely in the
tracer's tabulated window, and at 90° the ray turns within a few kilometres of the
core–mantle boundary, where the velocity falls from 13.6906 to
$8.0140\ \mathrm{km\,s^{-1}}$. The lesson's statement is that this degradation is
*located and explained*, not averaged away: the failure carries information about
the discretisation, which is exactly what a validation exercise is for.

---

## ★6 — Which error dominates

$$R = \frac{113.162}{0.5000} = 226.3 .$$

The model error is 226 times the quadrature error. Improving the answer therefore
means improving the *model*: refine the velocity parameterisation, or average over
an ensemble of accepted models, or acquire more data. Halving the integration step
would change the answer at the 0.5 ms level — invisible against a 113 ms model
term. This is the same conclusion the wavefront-tracking demonstration reaches
from the other direction in Lesson 06.

---

## ★7 — Validation plan for a two-dimensional tracer

- **Reference case.** Place a smooth, laterally varying perturbation on a linear
  gradient, e.g. $v(x,z) = 2500 + 0.60z + \delta\,x$ with
  $\delta$ small enough that the perturbation of the geometry remains perturbative
  ($\delta L/v \ll 1$ over the model width $L$). For small $\delta$ the travel time
  can be obtained by first-order perturbation theory about the 1-D arc solution,
  which gives an independent (semi-analytic) reference. A second, fully independent
  route is to compute the same travel time with a grid eikonal solver and compare
  all three.
- **Quantities to compare.** Travel time and the surface offset at which the ray
  emerges, each with units, and the *ray path itself* in the $(x, z)$ plane.
- **Convergence.** Repeat with the integration step halved twice and report the
  fitted order; a tracer whose error does not fall when the step is halved has a
  bug, not a discretisation.
- **Multi-arrival check.** Shoot a fan of take-off angles covering $180^\circ$ of
  incidence, record *every* root of $X(i_0) = X^{\ast}$ by detecting sign changes
  across the fan rather than stopping at the first, and compare the count with the
  number of arrivals the reference solution predicts. If the tracer returns one
  root where the reference predicts three, it is returning only the first arrival;
  the demonstration's own Section 5 naming of folds and shadows is the prediction
  to test against.

---

## ★8 — The nature of the 90° failure

Local slope from the two rows straddling $90^\circ$:

$$\frac{\mathrm{d}T}{\mathrm{d}\Delta} \approx \frac{781.3348 - 703.2422}{90 - 75}
= \frac{78.0926}{15} = 5.206173\ \mathrm{s\,deg^{-1}} .$$

Predicted time error from the distance error:

$$5.206173 \times 0.163307 = 0.850205\ \mathrm{s}.$$

Measured time error: $782.1434 - 781.3348 = 0.8086$ s. The prediction is within
5 % of the measurement ($0.8086/0.850205 = 0.951$).

What the agreement shows: the tracer's distance and time errors are *consistent
with the model's own travel-time curve* — the tracer found a genuine ray, but one
that surfaces $0.163^\circ$ away from the requested distance. The failure is in
the ray parameter (or equivalently in the quadrature that maps it to a distance),
not in the time computation, and it is therefore repairable by solving the
two-point problem more accurately rather than by changing the physics.
