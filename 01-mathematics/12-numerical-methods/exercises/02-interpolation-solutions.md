# Solutions — 01-12-02 Interpolation, Splines and Approximation Theory

> **Read this after attempting the exercises, not before.**
>
> Numbers were computed rather than estimated. Where a result depends on a random
> realisation (★9) the seed and the measured values are both given, so the numbers
> are reproducible but should be read as one instance of a distribution.

---

## ★1 — Lagrange cardinals and evaluation

For nodes $x_0=0,x_1=1,x_2=3$:

$$\ell_0(x) = \frac{(x-1)(x-3)}{(0-1)(0-3)} = \frac{(x-1)(x-3)}{3},$$

$$\ell_1(x) = \frac{(x-0)(x-3)}{(1-0)(1-3)} = \frac{-x(x-3)}{2},$$

$$\ell_2(x) = \frac{(x-0)(x-1)}{(3-0)(3-1)} = \frac{x(x-1)}{6}.$$

At $x=2$: $\ell_0(2) = (1)(-1)/3 = -1/3$, $\ell_1(2) = -2(-1)/2 = 1$,
$\ell_2(2) = 2(1)/6 = 1/3$. The weights sum to 1, as they must. With
$y=(1,2,0)$,

$$p(2) = 1\left(-\tfrac13\right) + 2(1) + 0\left(\tfrac13\right)
= \boxed{\tfrac53 = 1.6667}.$$

**Check.** The weights $\ell_i(2)$ are a partition of unity at every $x$, so a
constant data set would be reproduced exactly; the sum $1$ is therefore a
verification of the arithmetic, not a coincidence.

---

## ★2 — Newton form and agreement

Divided differences:

| order | $i=0$ | $i=1$ | $i=2$ |
|---|---|---|---|
| 0 | $1$ | $2$ | $0$ |
| 1 | – | $(2-1)/(1-0) = 1$ | $(0-2)/(3-1) = -1$ |
| 2 | – | – | $(-1-1)/(3-0) = -2/3$ |

The Newton form is

$$p(x) = 1 + 1\,(x-0) - \tfrac23 (x-0)(x-1),$$

so

$$p(2) = 1 + 2 - \tfrac23(2)(1) = 3 - \tfrac43 = \boxed{\tfrac53}.$$

The two forms agree, as they must: they are the same polynomial expressed in
different bases. The demonstration measures the difference between the two forms
on 41 points as $7.1\times10^{-15}$ — round-off only. Deductions made:
(i) adding a fourth node costs one new divided difference, whereas the Lagrange
form must be rebuilt; (ii) the Newton form is more stable to evaluate because each
term is built by Horner's rule rather than by a product of quotients.

---

## ★3 — The node factor and an error bound

For nodes at $-1,0,1$, $\omega(x) = (x+1)x(x-1) = x^3-x$. Differentiating,
$3x^2-1=0$ gives $x=\pm1/\sqrt3$, and

$$\lvert\omega(1/\sqrt3)\rvert = \left\lvert\tfrac{1}{3\sqrt3}
- \tfrac{1}{\sqrt3}\right\rvert = \frac{2}{3\sqrt3} = 0.384900 .$$

The interpolation error formula gives, for $n=2$,

$$\lvert f(x)-p_2(x)\rvert \le \frac{\max\lvert f'''\rvert}{3!}\max\lvert\omega\rvert
= \frac{\mathrm e}{6}\cdot\frac{2}{3\sqrt3} = \boxed{0.17437},$$

since $\max\lvert f'''\rvert = \mathrm e$ for $f=\mathrm e^x$ on $[-1,1]$. The
actual error at $n=2$ is smaller — the bound is pessimistic by a factor of a few —
but its *scaling* is the point: $\max|\omega|\sim 2^{n-1}/(n+1)$ grows with $n$
while $\max|f^{(n+1)}|/(n+1)!$ shrinks, and the bound is useful only while the
second effect wins.

---

## ★4 — Linear interpolation in a well log

Linear interpolation between $(1000,0.19)$ and $(1001,0.21)$ at 1001.4 m:

$$y = 0.19 + 0.4\,(0.21-0.19) = \boxed{0.198}.$$

The interpolation error formula for a straight line through two nodes is

$$\lvert f(x)-p_1(x)\rvert = \frac{\lvert f''(\xi)\rvert}{2}(x-a)(b-x)
= \frac{2\times10^{-4}}{2}(0.4)(0.6) = 2.4\times10^{-5}.$$

So the value at 1001.4 m is $0.1980 \pm 0.000024$ from curvature alone — entirely
negligible against the logging tool's own uncertainty, which for a neutron or
density log is of order $10^{-2}$ in the same units. **The interpolation is not
the limiting error**, and saying so is part of the analysis: a curvature error
five hundred times smaller than the instrument error is not worth a better
interpolant.

---

## ★5 — Deriving the moment system

Let $s_i'' = M_i$ and $h_i = x_{i+1}-x_i$. Since $s''$ is linear on
$[x_i,x_{i+1}]$, integrating twice gives the spline in the form

$$s(x) = y_i + b_i(x-x_i) + \frac{M_i}{2}(x-x_i)^2
+ \frac{M_{i+1}-M_i}{6h_i}(x-x_i)^3,$$

where continuity of $s$ at both ends of the interval is already imposed and $b_i$
is the (so far unknown) slope at $x_i$. Continuity of $s$ at $x_{i+1}$ gives

$$b_{i+1} = b_i + h_i\,\frac{M_i+M_{i+1}}{2} . \tag{A}$$

Continuity of $s'$ at $x_{i+1}$ gives, from the same expression,

$$b_i + h_i\frac{2M_i+M_{i+1}}{6} = b_i + \frac{h_i^2}{6}(2M_i+M_{i+1})/h_i
\ \text{(left)}\ =\ b_{i+1} - h_i\frac{M_{i+1}}{3}\ \text{(right)} .$$

Eliminating $b_i$ and $b_{i+1}$ between the last two relations yields

$$h_{i-1}M_{i-1} + 2(h_{i-1}+h_i)M_i + h_iM_{i+1}
= 6\left(\frac{y_{i+1}-y_i}{h_i} - \frac{y_i-y_{i-1}}{h_{i-1}}\right),
\qquad i=1,\dots,n-1 .$$

**Uniqueness.** The matrix is symmetric, tridiagonal, and **strictly diagonally
dominant**: the diagonal entry is $2(h_{i-1}+h_i)$ against the off-diagonal
magnitudes $h_{i-1}+h_i$. A strictly diagonally dominant matrix is nonsingular, so
the moments are unique, and the Thomas algorithm solves the system in $O(n)$
operations. Either end condition (natural or clamped) adds two equations to a
still-dominant system and preserves both properties.

---

## ★6 — A natural spline worked out

Nodes $0,1,2,3$ with $h_i=1$ and $y=(0,1,1,0)$. The two interior equations are

$$4M_1 + M_2 = 6\left[(y_2-y_1)-(y_1-y_0)\right] = 6(0-1) = -6,$$

$$M_1 + 4M_2 = 6\left[(y_3-y_2)-(y_2-y_1)\right] = 6(-1-0) = -6 .$$

Subtracting gives $3M_1-3M_2=0$, so $M_1=M_2$, and then $5M_1=-6$:

$$M_1 = M_2 = -1.2, \qquad M_0=M_3=0 .$$

On $[1,2]$ with $h=1$, $y_1=1$:

$$b_1 = \frac{y_2-y_1}{h} - \frac{h(2M_1+M_2)}{6}
= 0 - \frac{2(-1.2)+(-1.2)}{6} = \frac{3.6}{6} = 0.6 .$$

At $x=1.5$, $\mathrm dx = 0.5$:

$$s(1.5) = 1 + 0.6(0.5) + \frac{-1.2}{2}(0.25)
+ \frac{M_2-M_1}{6h}(0.125) = 1 + 0.3 - 0.15 + 0 = \boxed{1.15}.$$

**Comment on the end condition.** The data rise from 0 to 1 and then fall to 0, so
the true curvature at $x=0$ and $x=3$ is not zero — a natural spline forces
$s''=0$ there and therefore distorts the fit at the ends. For this data a clamped
condition with the true slopes (which are about $+1.5$ and $-1.5$) would be
better, and the measured max-norm consequence is the order-2-versus-order-4
difference in the lesson's table.

---

## ★7 — Why the Runge error grows

The error formula is $\lvert f-p_n\rvert = \frac{\lvert f^{(n+1)}(\xi)\rvert}{(n+1)!}
\lvert\omega(x)\rvert$. For $f(x)=1/(1+25x^2)$ the derivatives grow like $25^n$
near the origin (the nearest singularities of $f$ are at $x=\pm\mathrm i/5$, so
the radius of convergence of the Taylor series about 0 is $1/5$), while
$(n+1)!$ grows super-exponentially. The *node factor* for equispaced nodes
satisfies

$$\max_{[-1,1]}\lvert\omega(x)\rvert \sim \frac{2^{n-1}}{n+1}
\qquad\text{(large } n),$$

which grows like $2^n$. So the bound behaves as $\sim (25/2)^n/(n+1)$ — the
derivative growth wins, and the error grows.

**Measured factor.** From the lesson's table the equispaced errors at $n=8,12,16,20,24$
are $1.045, 3.663, 14.39, 59.79, 257.0$. The ratios are

$$\frac{3.663}{1.045}=3.5,\quad \frac{14.39}{3.663}=3.9,\quad
\frac{59.79}{14.39}=4.2,\quad \frac{257.0}{59.79}=4.3,$$

so the error grows by a factor of about **4.3 per four added nodes**, i.e. about
$1.44$ per node, consistent with the $25/2\to$ effective ratio once the $(n+1)!$
suppression is accounted for. Chebyshev nodes replace $\omega$ by a scaled
Chebyshev polynomial whose maximum is $2^{-n}$, converting the growing node factor
into a decaying one; the measured errors then fall monotonically
($4.60\times10^{-1}$ at $n=4$ to $8.17\times10^{-3}$ at $n=24$).

---

## ★8 — Extrapolating a gravity profile

The honest answer has three parts. First, I would not extrapolate by
interpolation at all: 1500 m is 500 m beyond the last station, and no interpolant
has an error bound outside its node range — a cubic spline's error grows like the
cube of the distance from the nearest node, and there is no reason to believe the
growth is physical. Second, if a value is genuinely required, it must come from a
*model*: fit a source geometry (a prism, a body with a depth and a density) that
reproduces the measured profile, and evaluate the model's field at 1500 m. The
model's extrapolation is as good as the model's physics, which is a much stronger
statement than an interpolant's. Third, I would report the extrapolation as a
model prediction with an uncertainty from the range of acceptable models, not as
an interpolated value.

**Why "I will use a cubic spline" is not an answer.** It specifies a numerical
convenience, not a physical assumption. Two splines — natural and clamped, or one
spline with and without a datum at 1000 m — give different answers at 1500 m, and
nothing in the choice is testable against data out there. Specifying the method
without specifying the model is exactly the confusion between interpolation and
inference that this lesson is about.

---

## ★★★9 — Polynomial, spline and least squares under 1% noise

**Setup.** 21 equispaced nodes on $[-1,1]$, values
$f(x_i)(1+0.01\epsilon_i)$ with $\epsilon_i\sim N(0,1)$ and seed 7; the error is
the maximum over a 1001-point grid. A degree-6 least-squares fit is built by
solving the $7\times7$ normal equations for a monomial basis.

| Method | max error, noise-free | max error, 1% noise |
|---|---|---|
| Interpolating polynomial (21 nodes) | 59.77 | 59.19 |
| Natural cubic spline | 0.003182 | 0.008487 |
| Degree-6 least squares | – | 0.2297 |

with the Chebyshev-node variant of the interpolant reaching $4.60\times10^{-1}$ at
$n=4$ and $8.17\times10^{-3}$ at $n=24$ in the lesson's table.

**Reading the table.** The ranking is spline < least squares < interpolating
polynomial, and the *reasons are different in each pair*:

1. **Interpolating polynomial versus spline.** For the interpolant the noise is
  irrelevant: $59.77$ noise-free against $59.19$ with noise. The error is entirely
  the Runge phenomenon — the node factor $\max\lvert\omega\rvert$ — and the data
  error is six orders of magnitude smaller. This is the clearest possible
  demonstration that *the node distribution, not the data quality, is the limiting
  factor* for equispaced high-degree interpolation.
2. **Spline versus least squares.** Here noise does matter: the spline's error
  rises from $0.00318$ to $0.00849$ when noise is added, because interpolation
  passes through the data exactly and inherits the noise. But the degree-6 fit is
  *worse* ($0.2297$), because a single global polynomial of degree 6 cannot
  represent a function with curvature concentrated near the origin: its **model
  error** exceeds the spline's noise sensitivity by a factor of 27.

**The general lesson**, and the reason the naive expectation ("approximation beats
interpolation under noise") fails here: the comparison is between two error
sources — model error and noise sensitivity — and either can dominate. A spline
is a *local* model whose model error is small for a smooth function at this
sampling density, so it wins on both counts. A low-degree global polynomial has
small noise sensitivity but large model error. To make least squares win one must
either raise the degree (and then the fit begins to interpolate the noise) or
choose a basis matched to the function.

---

## ★★★10 — Critique of a bicubic-spline gravity map

**What can legitimately be inferred at 1 km scale.** The map is a smooth
interpolation of a 5 km grid, so it faithfully represents the field's behaviour at
scales *above* about 10 km — the Nyquist limit of the source grid. Any feature
with a wavelength longer than roughly four grid cells is represented with the
spline's interior accuracy, which for a gravity field is high (the field is
harmonic and smooth). The map is therefore a legitimate aid for regional trends,
for continuation to a common datum, and for locating the edges of large bodies.

**What cannot.** Below the grid spacing the map contains no information from the
data; it contains the spline's interpolating assumption. A 1 km feature on the map
is a *shape the spline chose*, not an observation. In particular:
(i) apparent short-wavelength anomalies may be overshoot from step-like changes
between adjacent grid values — the lesson measures a cubic spline overshooting a
unit step by $0.107$ and undershooting by $-0.131$;
(ii) the map's power spectrum below the grid Nyquist is the spline kernel's
spectrum, not the field's;
(iii) any derivative computed from the map — vertical gradient, tilt derivative,
horizontal-gradient magnitude — amplifies that artificial short-wavelength content
(see [01-12-03](../03-numerical-differentiation.md)).

**Diagnostic for overshoot.** Two cheap tests:

1. **Grid-halving.** Recompute the map from a 2.5 km grid (or from every second
   original datum). Genuine features persist and converge; spline artefacts change
   their amplitude and position. The overshoot of a spline at a step scales with
   the step height and is independent of refinement, so it will not shrink like a
   genuine anomaly.
2. **Monotonicity sweep.** For each grid cell, check whether the interpolated field
   leaves the range of its four surrounding data values. Every excursion is an
   overshoot, and its map is a map of spurious anomalies. A shape-preserving
   interpolant (monotone or PCHIP-type) should produce an empty sweep, at the cost
   of the $O(h^4)$ interior order.

A third test, if the data allow, is to compare against an independent dataset at
1 km scale: the difference between the two is the residual the spline invented,
and it is usually the most convincing evidence for a reviewer.
