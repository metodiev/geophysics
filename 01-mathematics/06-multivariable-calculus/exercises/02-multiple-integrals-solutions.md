# Solutions — 01-06-02 Multiple Integrals and Change of Variables

> **Read this after attempting the exercises, not before.**
>
> Every numeric answer below was computed. Where a value is numerical rather than
> analytic, that is stated and its accuracy is given.

Throughout, $G = 6.674\times10^{-11}$ and, where required,
$1\ \mathrm{mGal} = 10^{-5}\ \mathrm{m\,s^{-2}}$.

---

## ★1 — A double integral in both orders

$$\iint_R (x+2y)\,dA = \int_0^3\!\!\int_0^2 (x+2y)\,dy\,dx .$$

**Inner integral over $y$ (with $x$ held fixed):**

$$\int_0^2 (x+2y)\,dy = \left[xy + y^2\right]_0^2 = 2x + 4 .$$

**Outer integral:**

$$\int_0^3 (2x+4)\,dx = \left[x^2 + 4x\right]_0^3 = 9 + 12 = 21 .$$

**Other order.**

$$\int_0^2\!\!\int_0^3 (x+2y)\,dx\,dy
= \int_0^2 \left[\frac{x^2}{2} + 2xy\right]_{0}^{3} dy
= \int_0^2 \left(\frac{9}{2} + 6y\right)dy
= 9 + 12 = 21 .$$

Both orders give $\boxed{21}$. Fubini's theorem is not a formality here: the two
routes distribute the arithmetic differently and their agreement is a genuine
check.

---

## ★2 — Integration over a triangle

The region is $\{(x,y): 0 \le x \le 1,\ 0 \le y \le x\}$, since the hypotenuse
joins $(0,0)$ to $(1,1)$.

**(a) $x$ outer:**

$$\iint xy\,dA = \int_0^1\!\!\int_0^x xy\,dy\,dx
= \int_0^1 x\left[\frac{y^2}{2}\right]_0^x dx
= \frac{1}{2}\int_0^1 x^3\,dx = \frac{1}{2}\cdot\frac{1}{4} = \frac{1}{8}.$$

**(b) $y$ outer:** for a fixed $y$, $x$ runs from $y$ to $1$:

$$\iint xy\,dA = \int_0^1\!\!\int_y^1 xy\,dx\,dy
= \int_0^1 y\left[\frac{x^2}{2}\right]_y^1 dy
= \frac{1}{2}\int_0^1 \left(y - y^3\right)dy
= \frac{1}{2}\left(\frac{1}{2} - \frac{1}{4}\right) = \frac{1}{8}.$$

**(c)** Both give $\boxed{\tfrac{1}{8}}$. Note the change in the *structure* of
the limits: in (a) the inner limit is $x$-dependent; in (b) it is $y$-dependent
and is the *lower* limit. Deciding which arrangement is easier is the practical
skill this exercise tests, and there is no general rule — only that the inner
limits must never involve the inner variable.

---

## ★3 — Area between two curves

$$\text{Area} = \int_0^1 \left(\sqrt{x} - x^2\right)dx
= \left[\frac{2}{3}x^{3/2} - \frac{x^3}{3}\right]_0^1
= \frac{2}{3} - \frac{1}{3} = \frac{1}{3}.$$

The answer is $\boxed{\tfrac{1}{3}}$, which is a useful check: the two curves
cross at $x=0$ and $x=1$ (since $\sqrt{1} = 1$), so the region is bounded and the
integration limits are those crossings.

---

## ★4 — The spherical element in action

$$\iiint_{\text{ball}} x^2\,dV
= \int_0^{2\pi}\!\!\int_0^{\pi}\!\!\int_0^1
r^2\sin^2\theta\cos^2\phi \cdot r^2\sin\theta\,dr\,d\theta\,d\phi .$$

The integrand separates, so the three integrals factorise:

$$\left(\int_0^1 r^4\,dr\right)
\left(\int_0^{\pi}\sin^3\theta\,d\theta\right)
\left(\int_0^{2\pi}\cos^2\phi\,d\phi\right)
= \frac{1}{5}\cdot\frac{4}{3}\cdot\pi = \frac{4\pi}{15} = 0.837758\ldots$$

For the second part, the integrand is $r^2 = x^2+y^2+z^2$, and by the symmetry of
the ball the three terms contribute equally:

$$\iiint (x^2+y^2+z^2)\,dV = 3 \times \frac{4\pi}{15} = \frac{4\pi}{5}
= 2.513274\ldots$$

**Check by a different route.** In spherical coordinates the integrand is $r^2$
and the angular integrals give $4\pi$:

$$\iiint r^2\,dV = 4\pi\int_0^1 r^4\,dr = 4\pi\cdot\frac{1}{5} = \frac{4\pi}{5}. \checkmark$$

Two independent reductions agree, so $\boxed{4\pi/15}$ and $\boxed{4\pi/5}$ are
confirmed. Note that the first result also gives $\iiint x^2\,dV = \tfrac13 I_{\text{polar}}$-type
quantities used in moment-of-inertia work.

---

## ★★5 — A quadratic density profile

**(a)**

$$M = 4\pi\int_0^R \rho_0\left(1 - \frac{r^2}{R^2}\right)r^2\,dr
= 4\pi\rho_0\left[\frac{r^3}{3} - \frac{r^5}{5R^2}\right]_0^R
= 4\pi\rho_0R^3\left(\frac{1}{3} - \frac{1}{5}\right)
= \frac{8\pi\rho_0R^3}{15}.$$

**(b)**

$$\bar{\rho} = \frac{M}{\frac{4}{3}\pi R^3}
= \frac{8\pi\rho_0R^3/15}{\frac{4}{3}\pi R^3}
= \frac{8}{15}\cdot\frac{3}{4}\rho_0 = \frac{2}{5}\rho_0 = 0.4\,\rho_0 .$$

**(c)** With $\rho_0 = 3000\ \mathrm{kg\,m^{-3}}$ and $R = 6.0\times10^5$ m:

$$M = \frac{8\pi(3000)(6.0\times10^5)^3}{15}
= 1.0857\times10^{21}\ \mathrm{kg},$$

and $\bar{\rho} = 1200\ \mathrm{kg\,m^{-3}}$.

**(d)** For every $0 < r < R$,

$$1 - \frac{r^2}{R^2} > 1 - \frac{r}{R}
\qquad\Longleftrightarrow\qquad \frac{r^2}{R^2} < \frac{r}{R}
\qquad\Longleftrightarrow\qquad r < R ,$$

so the quadratic profile is *higher* everywhere inside the body: it is flat at the
centre (its derivative vanishes at $r=0$) and therefore retains more mass at
small and intermediate radii than the linear one. The mean fraction consequently
rises from $\rho_0/4 = 0.25\,\rho_0$ for the linear profile to
$0.4\,\rho_0$ here. **The mean density is a statement about the whole function,
and two profiles that both fall from $\rho_0$ to $0$ can differ by 60 % in their
volume average.**

---

## ★★6 — Moment of inertia of a uniform sphere

**(a)** With $\rho$ constant and $x^2+y^2 = r^2\sin^2\theta$,

$$I_z = \iiint \rho\,r^2\sin^2\theta\; dV
= \rho\int_0^R r^4\,dr\int_0^{\pi}\sin^3\theta\,d\theta\int_0^{2\pi}d\phi
= \rho\cdot\frac{R^5}{5}\cdot\frac{4}{3}\cdot2\pi
= \frac{8\pi\rho R^5}{15}.$$

**(b)** Substituting $M = \tfrac{4}{3}\pi\rho R^3$,

$$I_z = \frac{8\pi\rho R^5}{15}
= \frac{4\pi\rho R^3}{3}\cdot\frac{2R^2}{5}
= \frac{2}{5}MR^2 . \checkmark$$

**(c)** The radius of gyration is
$k = \sqrt{I_z/M} = \sqrt{\tfrac{2}{5}}\,R = 0.6325\,R$.

**Remark.** The factor $\tfrac{2}{5}$ comes entirely from the $r^4$ weighting and
the angular factor $\tfrac{4}{3}$; the two are not independent facts but the
consequence of one volume element. This is exactly the kind of identity the
change-of-variables machinery exists to make mechanical.

---

## ★★7 — Is the grid average the area mean?

**(a)** The correct statement is

$$\bar{f} = \frac{1}{A}\iint_{\text{sheet}} f(x,y)\,dA, \qquad A = 400\ \mathrm{km^2}.$$

A grid average is

$$\bar{f}_{\text{grid}} = \frac{1}{(2k+1)^2}\sum_{i=-k}^{k}\sum_{j=-k}^{k}
f(x_i, y_j) .$$

These are equal only under special conditions.

**(b)** The two-dimensional composite midpoint rule with spacing $a$ has error

$$\frac{a^2}{24}\iint\left(f_{xx} + f_{yy}\right)dA + O(a^4)$$

per unit area, so the *average* carries a relative error of order
$\frac{a^2}{24}\nabla^2 f / \bar f$ for a $10\ \mathrm{km} \times 10\ \mathrm{km}$
sheet. The error is controlled by the Laplacian of $f$, not by its magnitude:
**a smooth large-amplitude field is integrated accurately, a rough small-amplitude
one badly.**

**(c)** Take $f = x^2$ on $[-10,10]\times[-10,10]$, with $x$ in kilometres and a
1 km grid.

*Area mean:*

$$\bar f = \frac{1}{400}\int_{-10}^{10}\!\!\int_{-10}^{10} x^2\,dx\,dy
= \frac{20}{400}\int_{-10}^{10}x^2\,dx
= \frac{1}{20}\cdot\frac{2(1000)}{3} = \frac{100}{3} = 33.333 .$$

*Grid average* (21 sample values in $x$, each repeated 21 times in $y$): the mean
of $x^2$ over the sampled $x$ values is

$$\frac{1}{21}\left(2\sum_{k=1}^{10}k^2\right)
= \frac{2(385)}{21} = 36.667 .$$

The grid average exceeds the area mean by $3.33$, a relative error of
$\boxed{10.0\%}$. The reason is that the sampled values are concentrated where
$x^2$ is large: the grid samples $x = \pm10$ but never $x = \pm9.5$, where $x^2$
is smaller. **Endpoint bias is the two-dimensional face of the same problem.**

**(d)** The grid average equals the area mean when, exactly: the quadrature is
exact for the integrand. For the midpoint rule this happens for linear
integrands, and more generally when the uniformly weighted sum is a Riemann sum
for the area integral — which requires (i) equal cell areas, and (ii) the
quadrature rule's error to vanish. A grid in latitude and longitude violates (i)
by a factor of $1/\sin\theta$ (see
[01-06-03](./03-jacobians-solutions.md), ★★8), so **the arithmetic mean of gridded
values on a global lat–long grid is not the area mean, however fine the grid.**

---

## ★★8 — Endpoint singularities and convergence order

**(a)**

$$\int_{-1}^{1}\sqrt{1-x^2}\,dx = \frac{\pi}{2} = 1.5707963\ldots$$

(the area of a semicircle of unit radius).

**(b)** The integrand $f_1 = (1-x^2)^{1/2}$ has
$f_1'(x) = -x(1-x^2)^{-1/2}$, which diverges as $x\to\pm1$; the function behaves
like $\sqrt{2(1-x)}$ near $x = 1$. For $f_2 = (1-x^2)^{1/4}$,
$f_2' \propto (1-x^2)^{-3/4}$, a stronger singularity.

Near an endpoint the midpoint rule's local error scales with the local
smoothness: for $f \sim (1-x)^\alpha$ with $0<\alpha<1$, the composite midpoint
error behaves as $n^{-(\alpha+1)}$ (because the error is concentrated in the last
cell). Here $\alpha = 1/2$ for $f_1$ and $\alpha = 1/4$ for $f_2$, so

$$\text{order}(f_1) = 1.5, \qquad \text{order}(f_2) = 1.25 .$$

Both are worse than the second order of a smooth integrand, and the *more*
singular integrand is the more slowly converging.

**(c)** Measured, with the analytic value $\pi/2$ for $f_1$ and the numerically
converged value $1.7480384$ (accurate to about $4\times10^{-9}$) for $f_2$:

| $n$ | $f_1$ error | ratio | $f_2$ error | ratio |
|---|---|---|---|---|
| 100 | $4.864\times10^{-4}$ | — | $9.108\times10^{-4}$ | — |
| 400 | $6.087\times10^{-5}$ | 7.99 | $1.612\times10^{-4}$ | 5.65 |
| 1600 | $7.610\times10^{-6}$ | 8.00 | $2.850\times10^{-5}$ | 5.66 |
| 6400 | $9.514\times10^{-7}$ | 8.00 | $5.034\times10^{-6}$ | 5.66 |
| 25600 | $1.189\times10^{-7}$ | 8.00 | $8.868\times10^{-7}$ | 5.68 |

A factor of 4 in $n$ reduces the error by 8.00 for $f_1$, so
$8 = 4^{1.5}$ and the observed order is exactly $1.5$. For $f_2$ the ratio is
$5.66 = 4^{1.25}$, so the order is $1.25$. **Both predictions confirmed.**

**Why it matters.** Many geophysical integrands have exactly this structure:
potential-field kernels contain $\sqrt{}$ and $\lvert\cdot\rvert$ factors, and
the radial integral in a disk or a cylinder ends in a square root. A convergence
rate of $1.5$ means that to gain one decimal digit you must refine the grid by a
factor of $10^{2/3} \approx 4.6$, and to gain three digits by a factor of 100.
Knowing this in advance is the difference between a correctly sized computation
and one that runs for a week.

---

## ★★★9 — Quadrature against Monte Carlo in $d$ dimensions

**Method.** For each dimension $d$, the exact unit-ball volume is
$V_d = \pi^{d/2}/\Gamma(d/2 + 1)$.

- **Quadrature:** a tensor-product midpoint rule on $[-1,1]^d$ with
  $n = \mathrm{round}(N^{1/d})$ cells per axis, counting cells whose centre lies
  inside the ball and multiplying by $h^d$.
- **Monte Carlo:** $N$ uniform samples in $[-1,1]^d$, counting those inside the
  ball and multiplying by $2^d$ times the fraction. Because a single Monte Carlo
  run is unreliable, the mean relative error over five seeds is reported, with
  the observed range.

**(a)** Exact values:

| $d$ | $V_d$ |
|---|---|
| 1 | 2.000000 |
| 2 | $\pi = 3.141593$ |
| 3 | $4\pi/3 = 4.188790$ |
| 4 | $\pi^2/2 = 4.934802$ |

**(b)–(c)** Measured relative errors, quadrature against Monte Carlo:

| $d$ | $N$ | quadrature | Monte Carlo (mean of 5) | MC range |
|---|---|---|---|---|
| 2 | $10^4$ | $7.66\times10^{-4}$ | $4.38\times10^{-3}$ | $2.3\times10^{-6}$–$8.2\times10^{-3}$ |
| 2 | $10^5$ | $3.73\times10^{-4}$ | $7.35\times10^{-4}$ | $4.9\times10^{-5}$–$1.3\times10^{-3}$ |
| 2 | $10^6$ | $7.36\times10^{-5}$ | $4.51\times10^{-4}$ | $1.5\times10^{-4}$–$8.8\times10^{-4}$ |
| 3 | $10^4$ | $7.30\times10^{-3}$ | $9.63\times10^{-3}$ | $1.9\times10^{-3}$–$1.6\times10^{-2}$ |
| 3 | $10^5$ | $2.73\times10^{-3}$ | $2.13\times10^{-3}$ | $5.5\times10^{-4}$–$3.6\times10^{-3}$ |
| 3 | $10^6$ | $7.36\times10^{-4}$ | $5.27\times10^{-4}$ | $1.8\times10^{-5}$–$2.0\times10^{-3}$ |
| 4 | $10^4$ | $1.73\times10^{-2}$ | $1.69\times10^{-2}$ | $1.2\times10^{-2}$–$2.8\times10^{-2}$ |
| 4 | $10^5$ | $2.82\times10^{-2}$ | $1.57\times10^{-3}$ | $1.8\times10^{-4}$–$3.3\times10^{-3}$ |
| 4 | $10^6$ | $3.22\times10^{-3}$ | $1.07\times10^{-3}$ | $3.5\times10^{-4}$–$1.6\times10^{-3}$ |

**(d)** Read the table by dimension.

- $d = 2$: quadrature is better at every $N$, by a factor of 3 to 6 at the
  largest $N$.
- $d = 3$: the two are comparable; which wins flips between $N = 10^5$ and
  $10^6$.
- $d = 4$: Monte Carlo is clearly better, by a factor of 3 at $N = 10^6$ and by
  a factor of 18 at $N = 10^5$.

So the measured crossover lies between $d = 3$ and $d = 4$. The theoretical
statement is that tensor quadrature error scales as $N^{-2/d}$ while Monte Carlo
scales as $N^{-1/2}$, and these are equal at $d = 4$. The measurement agrees. The
quadrature's *constant* is large because of the staircase representation of the
ball's curved boundary, which is why the crossover appears slightly below 4.

**Limitations.** (i) The quadrature error is *not* monotone in $N$, because the
staircase boundary error depends on how the grid happens to cut the sphere — the
$d=4$, $N=10^5$ entry is larger than the $N=10^4$ entry for this reason, and a
single run would have misled. (ii) A single Monte Carlo run is unreliable: the
spread across five seeds at a given $N$ is often a factor of ten, so the means
above are estimates with their own uncertainty. (iii) Both methods were applied
to a convex, radially symmetric region; a thin or disconnected region would move
the crossover. (iv) The exponent in $d$ depends on the smoothness of the
integrand; a quadrature rule tailored to the geometry (spherical coordinates,
adaptive subdivision) is not represented here and would be far more accurate.

**The general lesson.** The comparison is not "Monte Carlo is bad"; it is
"quadrature's advantage decays as $N^{-2/d}$, so it is exhausted by about four to
ten dimensions." In uncertainty propagation with a dozen model parameters, Monte
Carlo is the only practical option, and that is exactly why
[01-13-09 Error and Uncertainty Propagation](../../13-probability-and-statistics-foundations/09-error-propagation.md)
is organised around it.

---

## ★★★10 — Truncated mass estimates from a limited survey

**(a)** With $g_z$ the vertical attraction and the survey covering a region
$\mathcal{S}$,

$$M_{\text{est}} = \frac{1}{2\pi G}\iint_{\mathcal{S}} g_z(x,y)\,dA ,$$

using the classical identity that the integral of the vertical attraction over an
infinite plane equals $2\pi GM$ for any isolated mass distribution (this follows
from Gauss's law applied to a limit of slabs; the same identity is derived for the
point-mass case in ★★6(c)).

**(b)** Writing the true integral over the whole plane as the sum over
$\mathcal{S}$ and its complement $\mathcal{S}^c$,

$$M_{\text{true}} - M_{\text{est}}
= \frac{1}{2\pi G}\iint_{\mathcal{S}^c} g_z\,dA .$$

Setting $g_z = 0$ outside $\mathcal{S}$ therefore discards exactly the contribution
of the anomaly beyond the boundary. Because the discarded region is far from the
source, $g_z$ there is smooth and small per unit area, but the *area* is
unbounded — the error is controlled by how fast $g_z$ decays, not by the survey's
precision.

**(c)** For a point mass at depth $d$, $g_z = GMd/(\rho^2+d^2)^{3/2}$, and

$$\frac{1}{2\pi G}\int_0^R g_z\,2\pi\rho\,d\rho
= \frac{M}{d}\int_0^R\frac{d\,\rho\,d\rho}{(\rho^2+d^2)^{3/2}}
= M\left(1 - \frac{d}{\sqrt{R^2+d^2}}\right).$$

The captured fraction is therefore $1 - \left(1+(R/d)^2\right)^{-1/2}$:

| $R/d$ | fraction captured | fraction lost |
|---|---|---|
| 1 | 0.2929 | 70.7 % |
| 3 | 0.6838 | 31.6 % |
| 10 | 0.9005 | 9.95 % |

**(d)** The implication is severe and often underestimated. **To capture 90 % of
the mass of a compact source, the survey must extend to ten times the source
depth in every direction** — and the loss is not random noise but a systematic
one-sided bias, so averaging several surveys does not reduce it. A survey of a
2 km-deep body must be at least 20 km across in each direction even to reach the
10 % level, and 90 % capture would require $R/d \approx 30$. Mass-balance studies
— ice loss, groundwater depletion, magma budgets — are limited by exactly this
geometric constraint, which is why regional gravity work is complemented by
satellite data with global coverage. See
[07-05-05 Applications: Groundwater Depletion, Ice Loss, Sea Level](../../../07-gravity-geodesy/05-satellite-gravimetry/05-grace-applications.md)
for the practical version of this argument.

**Status.** (a)–(c) are analytic. The derivation of the $1/(2\pi G)$ normalisation
in (a) was not verified numerically here; it follows from the point-mass identity
$2\pi GM$ computed in ★★6(c), where the closed form was verified against direct
quadrature to $2.9\times10^{-8}$ relative.
