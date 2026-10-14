---
id: 06-02-03
title: "The tau-p Transform and Intercept Time"
level: graduate
prereqs: ["06-02-01", "06-02-02", "01-05-05"]
tags: [seismology, tau-p, intercept-time, radon, slowness, non-uniqueness]
---

# The tau-p Transform and Intercept Time

The previous lesson built a travel-time curve $T(X)$ — arrival time against
surface offset — and read it as a list of straight branches. This lesson changes
the variable to make that reading systematic. Define the **intercept time**

$$\tau(p) \equiv T(p) - p\,X(p),$$

where $p$ is the ray parameter of the arrival and $X(p)$ is the offset at which
that ray returns. The pair of functions $X(p)$, $T(p)$ and the pair $p$,
$\tau(p)$ carry exactly the same information, but the second pair is the one in
which a layered Earth becomes a *linear* problem: for a stack of layers,

$$\tau(p) = 2\sum_i h_i\,\eta_i(p), \qquad
\eta_i(p) = \sqrt{v_i^{-2} - p^{2}},$$

which is linear in the thicknesses $h_i$ once the velocities are known. That is
the reason the transform exists.

The function $\tau(p)$ is the **Legendre transform** of $T(X)$, up to sign, and
the price of the transformation is honest and unavoidable: it is exactly the kind
of operation that turns small errors in the data into large errors in the result.
Section 6 measures that price numerically. The deeper structural point is that
$\tau(p)$ and $T(X)$ are interchangeable *only* while the travel-time curve is
single-valued in $p$. Where the curve folds — a triplication — the transform
still exists but no longer determines the Earth, and
[05 Shadow Zones, Triplications and the Low-Velocity Zone](05-shadow-zones.md)
measures that failure directly.

**All models and data in this module are SYNTHETIC.** The linear-gradient layer
($v = 3000 + 0.40z\ \mathrm{m\,s^{-1}}$ over 20 km) and the single layer used in
the worked examples are chosen teaching models. Where the demonstration compares
with a travel-time engine it uses the standard `iasp91` reference model
distributed with ObsPy — a named reference model, not data collected for this
repository — and every number below is printed by `code/tau_p_demo.py`, never
recalled from a publication.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** $\tau(p) = T - pX$ from the plane-wave decomposition of a
   seismogram and **state** what $\tau$ measures physically.
2. **Derive** Benndorf's relation $\mathrm{d}\tau/\mathrm{d}p = -X$ and explain
   why it makes $\tau(p)$ the Legendre transform of the travel-time curve.
3. **Show** that separating a branch into its "runs along a layer" and "travels
   through the layers above" parts is exactly the statement
   $\mathrm{d}T/\mathrm{d}X = p$.
4. **Compute** $\tau(p)$ in closed form for a single layer over a half space and
   for a linear gradient, and **verify** the latter against numerical quadrature.
5. **Check** the spherical identity $p = r\sin i / v$ along a ray path and
   **report** the percentiles of its violation rather than only its worst case.
6. **Quantify** how a picking error propagates through $\mathrm{d}\tau/\mathrm{d}p$
   into an offset, and **state** the trade-off between slowness resolution and
   slowness noise.
7. **State** the condition (single-valued $X(p)$) under which $\tau(p)$ can be
   inverted, and **recognise** the situation in which it cannot.

## Prerequisites

- [01 Eikonal Equation, Rays and Fermat's Principle](01-eikonal-and-rays.md) —
  the slowness vector and the eikonal equation.
- [02 Snell's Law, Layered Media and the Travel-Time Curve](02-snell-and-layering.md)
  — the branches and intercept times transformed here.
- [01-05-05 Integration Techniques and Definite Integrals](../../01-mathematics/05-single-variable-calculus/05-integration.md)
  — the integrals that define $X(p)$ and $T(p)$.

## 1. Where $\tau$ comes from: the slant stack

Consider a seismic experiment with sources and receivers on a line, and assume
the arrivals we care about are nearly plane waves crossing the array with
horizontal slowness $p$. For a receiver at offset $x$, the arrival time of that
plane wave is

$$t(x) = \tau + p\,x ,$$

where $\tau$ is the time at $x = 0$ — the **intercept time**. Summing a record
section along all such lines is the slant stack, and the result as a function of
$(p, \tau)$ is the $\tau$-$p$ panel: every arrival collapses to a point at its own
ray parameter and intercept time.

For a layered Earth the plane-wave description is not an approximation but an
organising principle, because Snell's law makes $p$ a constant of the motion
along each ray (Section 1 of [02](02-snell-and-layering.md)). Each ray, from a
particular source–receiver geometry, is labelled by exactly one $p$, and the
"arrival time minus its own offset times its own slowness" is a quantity that
depends only on the layers the ray traversed — not on where it came back to the
surface. That is why $\tau$ is the natural coordinate for layered structure.

For a stack of layers the two functions are obtained by integrating over depth,

$$X(p) = 2\int_{0}^{z_t} \frac{p}{\eta(z)}\,\mathrm{d}z, \qquad
T(p) = 2\int_{0}^{z_t} \frac{1}{v^{2}(z)\,\eta(z)}\,\mathrm{d}z,$$

with $\eta(z) = \sqrt{v(z)^{-2} - p^{2}}$ and $z_t$ the turning depth where
$\eta(z_t) = 0$, i.e. $v(z_t) = 1/p$. For constant-velocity layers the integrals
collapse to the sums of Section 2 of [02](02-snell-and-layering.md).

## 2. Benndorf's relation, and the Legendre transform

Differentiate the definition $\tau = T - pX$ with respect to $p$. Along a branch
the arrival time depends on the offset through $\mathrm{d}T/\mathrm{d}X = p$
(which is the definition of the ray parameter as the *apparent slowness*), so

$$\mathrm{d}\tau = \mathrm{d}T - p\,\mathrm{d}X - X\,\mathrm{d}p
= \frac{\mathrm{d}T}{\mathrm{d}X}\mathrm{d}X - p\,\mathrm{d}X - X\,\mathrm{d}p
= -X\,\mathrm{d}p ,$$

i.e.

$$\boxed{\;\frac{\mathrm{d}\tau}{\mathrm{d}p} = -X(p)\;}$$

**Benndorf's relation**. Two consequences follow immediately.

- $(T, X)$ and $(\tau, -p)$ are a Legendre-transform pair: either function
  determines the other, by
  $$T = \tau + pX = \tau - p\frac{\mathrm{d}\tau}{\mathrm{d}p},
  \qquad X = -\frac{\mathrm{d}\tau}{\mathrm{d}p}.$$
- The *curvature* of $\tau(p)$ is the inverse of the curvature of $T(X)$:
  $\mathrm{d}^{2}\tau/\mathrm{d}p^{2} = -\mathrm{d}X/\mathrm{d}p$ is negative
  where $\mathrm{d}T/\mathrm{d}X$ increases with offset, which is the normal
  case, and changes sign at a fold. **The sign change is where the transform
  stops being invertible**, and that is a physical event on the record, not an
  artefact.

In the angular language of the classical literature, $\tau(p)$ is the "delay
function" or "intercept function", and the inversion of $\tau(p)$ for $v(z)$ is
the Herglotz–Wiechert inversion. Its structure is exactly the linear relation
above: writing $\tau(p)/2 = \sum_i h_i\eta_i(p)$ exhibits the thicknesses as
coefficients multiplying known functions of $p$.

## 3. Two closed forms

### 3.1 A single layer over a half space

For one layer of thickness $h$ and speed $v_1$ over a half space of speed
$v_2 > v_1$, the reflected branch at offset $X$ has ray parameter $p$ satisfying
$X = 2h\,p/\eta_1$, and

$$\tau(p) = 2h\,\eta_1(p) = 2h\sqrt{v_1^{-2} - p^{2}}, \qquad 0 \le p \le 1/v_1 .$$

Taking $h = 5.00$ km and $v_1 = 6.00\ \mathrm{km\,s^{-1}}$: at vertical incidence
($p = 0$), $\tau = 2(5)/6 = 1.6667$ s; at the critical ray parameter of the
$v_2 = 6.50\ \mathrm{km\,s^{-1}}$ half space, $p = 1/6.50 = 0.153846\
\mathrm{s\,km^{-1}}$ and
$\tau = 2(5)\sqrt{0.027778 - 0.023669} = 0.641026$ s. The offset there is
$X = 2h\,p/\eta_1 = 24.000$ km, the critical offset of
[02](02-snell-and-layering.md) — the same number, obtained in the slowness domain.
**The head-wave intercept of the previous lesson is simply $\tau$ evaluated at
$p = 1/v_2$.**

### 3.2 A linear gradient

For $v(z) = v_0 + Gz$ over $0 < z < H$, the quadratures above have closed forms.
With $\theta_0$ defined by $\sin\theta_0 = p\,v_0$ (the take-off angle at the
surface, measured from the vertical),

$$X(p) = \frac{2}{Gp}\sqrt{1 - (pv_0)^{2}}, \qquad
T(p) = \frac{2}{G}\ln\frac{1}{\tan(\theta_0/2)},$$

valid while the turning depth $(1/p - v_0)/G$ lies inside the layer. This is the
model the demonstration integrates numerically, and it is the model used again in
[04 Ray Tracing in Laterally Varying Media](04-ray-tracing.md), where the same
rays are shown to be circular arcs.

## 4. The demonstration's measurements

`code/tau_p_demo.py` integrates the gradient layer by quadrature in the ray
angle and forms $\tau = T - pX$ on a grid of 59 valid ray parameters from
$9.299662\times10^{-5}$ to $3.174603\times10^{-4}\ \mathrm{s\,m^{-1}}$. Its
quadrature reproduces the closed forms of Section 3.2 to better than one part in
$10^{6}$ (checked before writing these numbers, over the whole branch). Selected
rows of the printed table:

| $p$ (s m⁻¹) | $X$ (km) | $T$ (s) | $\tau$ (s) | $-\mathrm{d}\tau/\mathrm{d}p$ (km) |
|---|---|---|---|---|
| $9.299662\times10^{-5}$ | 51.6306 | 9.7484 | 4.9469 | 50.4957 |
| $1.858782\times10^{-4}$ | 22.3288 | 5.9421 | 1.7916 | 22.3324 |
| $2.787597\times10^{-4}$ | 9.8347 | 3.0798 | 0.3382 | 9.8344 |

The last two columns are the two sides of Benndorf's relation: the numerical
derivative of $\tau$ and the independently computed offset $X$. Over the interior
of the branch their worst relative difference is $8.272\times10^{-4}$, which is
the truncation error of a finite difference on a 59-point grid and not a
discrepancy in the physics. At the middle of the branch the demonstration reports
$\mathrm{d}T/\mathrm{d}X = 2.051946971\times10^{-4}\ \mathrm{s\,m^{-1}}$ against
$p = 2.052284704\times10^{-4}\ \mathrm{s\,m^{-1}}$ — the other half of the same
identity, that the ray parameter *is* the apparent slowness.

### 4.1 The spherical version

In a sphere the conserved quantity is not $\sin i / v$ but

$$p = \frac{r\sin i}{v} \qquad (\mathrm{s\,rad^{-1}}),$$

$r$ being the radius at the point where the angle $i$ is measured. The
demonstration checks this directly on a ray path from the `iasp91` reference
model: for P at $60^\circ$ from a 10 km source, the path has 286 points, its
turning depth is 1547.96 km, and the engine reports $p = 393.8188\
\mathrm{s\,rad^{-1}} = 6.87343506\ \mathrm{s\,deg^{-1}}$. Measuring $\sin i$
from the path geometry and forming $r\sin i/v$ at every point gives a median of
$393.8164\ \mathrm{s\,rad^{-1}}$, a median relative deviation of
$9.193\times10^{-6}$, a 95th percentile of $1.433\times10^{-4}$ — and a worst
case of $1.853\times10^{-1}$.

That worst case deserves a sentence, because reporting only the median would be
misleading. The angle is *read* by differencing neighbouring path points, so its
error blows up where the ray is nearly horizontal and the radial distance between
adjacent samples goes to zero. Over 95 per cent of the path the identity holds to
better than $1.4\times10^{-4}$; the tail is a finite-difference artefact of the
measurement, not a failure of the conservation law. **A percentile is the honest
way to report a residual that is not uniform along the path.**

The same section verifies $p = \mathrm{d}T/\mathrm{d}\Delta$ by central
differencing the travel-time curve of the reference model and comparing with the
ray parameter the engine attaches to each arrival: the relative differences run
from $2.1\times10^{-7}$ at $20^\circ$ to $3.0\times10^{-5}$ at $60^\circ$ and
$2.8\times10^{-6}$ at $95^\circ$, the size expected from a $0.01^\circ$ central
difference. Numerically differentiating a travel-time curve *is* the definition
of the ray parameter, and here it is executed on a real travel-time engine.

## 5. Non-uniqueness: what the transform can and cannot invert

The transform pair is a bijection **on a branch**. The qualifier is the whole
difficulty:

1. **Folds.** Where $\mathrm{d}T/\mathrm{d}X$ is not monotonic — a triplication —
   several rays with different $p$ share one offset. Then $X(p)$ is not
   invertible, $\tau(p)$ still exists but its branches must be separated before
   it can be used, and $\mathrm{d}^{2}\tau/\mathrm{d}p^{2}$ changes sign exactly
   at the fold. This is measured, not asserted, in
   [05](05-shadow-zones.md).
2. **Gaps.** Where no ray turns (a shadow), the functions are simply not defined
   for a range of $p$. A slowness interval with no data is not a slowness
   interval with zero velocity contrast.
3. **Velocity–thickness ambiguity inside the linear relation.** Even a perfect
   $\tau(p)$ gives only $\sum_i h_i\eta_i(p)$ for the assumed $v_i$. The
   thicknesses are recoverable only in proportion to the velocities supplied —
   the same trade-off quantified in [02](02-snell-and-layering.md) Section 5.
4. **A hidden layer leaves no gap to notice.** For a low-velocity layer, $\eta$
   is imaginary over the relevant $p$ range and no branch exists; $\tau(p)$ simply
   contains nothing about that layer. Non-uniqueness here is not a broad
   posterior distribution over models; it is complete silence.

## 6. The price of differentiation

Benndorf's relation says that recovering geometry requires differentiating
$\tau(p)$. That is the instability of the method, and it can be measured. Take
the gradient branch sampled at 121 ray parameters from $1.500\times10^{-4}$ to
$3.000\times10^{-4}\ \mathrm{s\,m^{-1}}$, i.e. spacing
$\mathrm{d}p = 1.250\times10^{-6}\ \mathrm{s\,m^{-1}}$; over that range the offset
$X$ runs from 7.74 to 28.85 km. Add Gaussian picking noise of
$\sigma_T = 10.0$ ms to the travel times and form
$X_{\text{rec}} = -\mathrm{d}\tau/\mathrm{d}p$ by central differences.

| quantity | value |
|---|---|
| $X$ recovered from clean data (truncation only) | 0.711 m worst case |
| mean $\lvert X_{\text{rec}} - X\rvert$ over 300 noise realisations | 4473.411 m |
| worst mean error on the branch | 5044.240 m |
| relative to the smallest $X$ on the branch | 65.200 % |
| predicted by $\sigma_T/(\sqrt{2}\,\mathrm{d}p)$ | 5656.854 m |

Two things make this table worth its space. First, the *prediction* from the
central-difference error formula, $\sigma_T/(\sqrt{2}\,\mathrm{d}p) =
5656.854$ m, is within about 20 per cent of the measured worst case: the
instability is elementary and computable in advance. Second, the noise term
exceeds the truncation term by a factor of about **7100**. Refining the $p$ grid
to gain slowness resolution *buys* slowness noise in inverse proportion — halving
$\mathrm{d}p$ doubles the error — which is the same resolution-versus-variance
trade-off that a water level makes in deconvolution, expressed in a different
variable. The genuine gain from the $\tau$-$p$ transform is not resolution; it is
that a curved travel-time branch becomes a straight line in $\tau(p)$ **for a
single layer**, so the parameter estimation becomes a regression problem with a
well-understood error, rather than a curve-fitting exercise.

## 7. Assumptions and the regime of validity

1. **Laterally homogeneous, isotropic layers.** $p$ is conserved only because the
   medium does not vary horizontally. A dipping interface or lateral heterogeneity
   destroys the conservation law and with it the transform's meaning as a
   depth-labelling device.
2. **A single-valued branch.** As in Section 5: no folds, no gaps, or folds and
   gaps explicitly separated and labelled.
3. **Known velocities if thicknesses are wanted.** $\tau(p) = 2\sum h_i\eta_i(p)$
   is linear in $h$ only with $v$ supplied.
4. **Ray theory's high-frequency limit.** $\tau$ is an arrival-time description;
   it says nothing about amplitude, and it cannot represent a wave that travels by
   diffraction rather than by turning.
5. **Independent, zero-mean picking errors** for the error scaling of Section 6;
   correlated errors (a mis-picked reference time, a clock error) propagate
   differently and are not covered by $\sigma_T/(\sqrt{2}\,\mathrm{d}p)$.

## 8. Worked examples

### Example 1 — $\tau(p)$ for a single layer, and the offset it implies

A layer of thickness $h = 5.00$ km with $v_1 = 6.00\ \mathrm{km\,s^{-1}}$ over a
half space with $v_2 = 6.50\ \mathrm{km\,s^{-1}}$.

1. $\tau(0) = 2h/v_1 = 1.6667$ s.
2. At $p = 0.10\ \mathrm{s\,km^{-1}}$:
   $\eta_1 = \sqrt{0.027778 - 0.01} = 0.133333\ \mathrm{s\,km^{-1}}$;
   $\tau = 2(5)(0.133333) = 1.3333$ s;
   $X = 2h p/\eta_1 = 10(0.10)/0.133333 = 7.500$ km;
   check $T = \tau + pX = 1.3333 + 0.7500 = 2.0833$ s, which is also
   $2h/(v_1\cos i)$ with $\sin i = 0.6$: $\cos i = 0.8$,
   $2(5)/(6\times0.8) = 2.0833$ s. ✔
3. At $p = 1/v_2 = 0.153846\ \mathrm{s\,km^{-1}}$:
   $\eta_1 = \sqrt{0.027778 - 0.023669} = 0.064104$;
   $\tau = 0.641026$ s, $X = 24.000$ km — the head-wave intercept and critical
   offset of [02](02-snell-and-layering.md), recovered from $\tau(p)$.

### Example 2 — inverting a gradient branch

For the demonstration's gradient, $v_0 = 3000\ \mathrm{m\,s^{-1}}$ and
$G = 0.40\ \mathrm{s^{-1}}$. Take $p = 2.787597\times10^{-4}\
\mathrm{s\,m^{-1}}$, the fifth row of the table in Section 4.

1. $\sin\theta_0 = p v_0 = 0.836279$, so $\theta_0 = 56.7493^\circ$.
2. $X = \dfrac{2}{Gp}\sqrt{1 - (pv_0)^{2}}
   = \dfrac{2}{1.115039\times10^{-4}}\sqrt{0.300637}
   = 17936.6 \times 0.548304 = 9834.7$ m $= 9.8347$ km ✔ matches the table.
3. $T = \dfrac{2}{G}\ln\dfrac{1}{\tan(\theta_0/2)}
   = 5\,\ln\dfrac{1}{\tan 28.3746^\circ}
   = 5\ln 1.851420 = 3.0798$ s ✔ matches the table.
4. $\tau = T - pX = 3.0798 - 2.787597\times10^{-4}(9834.7) = 3.0798 - 2.7415
   = 0.3382$ s ✔.

Three numbers in the table are reproduced by hand from the closed forms, which is
the check that the table and the formulas describe the same object.

### Example 3 — a sensitivity statement made in advance

Suppose a study needs offsets to 1 km. Section 6's formula says the error is
$\sigma_T/(\sqrt{2}\,\mathrm{d}p)$; solving for the allowable spacing,
$\mathrm{d}p = \sigma_T/(\sqrt{2}\times1000\ \mathrm{m})$. With
$\sigma_T = 10$ ms that gives $\mathrm{d}p \approx 7.1\times10^{-6}\
\mathrm{s\,m^{-1}}$, i.e. roughly 28 points across the $2\times10^{-4}\
\mathrm{s\,m^{-1}}$ band used above — and a *finer* grid than that is not an
improvement, it is a noise amplifier. This is the practical form of the trade-off:
the p-spacing is chosen from the pick uncertainty and the required offset
accuracy, not from a wish for resolution.

## 9. Python demonstration

`code/tau_p_demo.py` prints four labelled sections:

1. **$X(p)$, $T(p)$ and Benndorf's relation** — the quadrature, the table of
   Section 4, and the worst relative difference ($8.272\times10^{-4}$).
2. **$p = \mathrm{d}T/\mathrm{d}\Delta$ measured from a travel-time engine** — the
   numerical derivative of the reference-model curve against the engine's own ray
   parameter, to a few parts in $10^{5}$ or better.
3. **The spherical identity $p = r\sin i / v$** — its percentile profile along a
   real ray path from the reference model.
4. **Differentiating $\tau$** — the noise-amplification table of Section 6,
   including the *predicted* value $\sigma_T/(\sqrt{2}\,\mathrm{d}p)$ alongside the
   measured one.

```bash
cd 06-seismology/02-ray-theory-and-travel-times/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python tau_p_demo.py
```

## Mastery checkpoint

Complete this without notes:

> A branch has $X(p) = 40.0$ km at $p = 1.30\times10^{-4}\ \mathrm{s\,m^{-1}}$ and
> $T = 6.400$ s there; at $p = 1.40\times10^{-4}\ \mathrm{s\,m^{-1}}$ the measured
> intercept is $\tau = 0.8000$ s. **(a)** Compute $\tau$ at
> $p = 1.30\times10^{-4}$, with units. **(b)** Estimate the offset at the midpoint
> $p = 1.35\times10^{-4}$ using Benndorf's relation and a central difference, and
> state the approximation you made. **(c)** A colleague measures $\tau$ to
> $\pm 5$ ms and the ray parameters of neighbouring traces are
> $2\times10^{-6}\ \mathrm{s\,m^{-1}}$ apart. Estimate the induced offset error
> and compare it with the 40 km offset. **(d)** State in one sentence what a
> triplication does to the invertibility of $\tau(p)$.

A worked version of (a)–(c) appears in the lesson
[solutions](exercises/03-tau-p-solutions.md).

## Common pitfalls

1. **Differentiating a coarse $\tau(p)$ and reporting the result as structure.**
   The derivative is dominated by picking noise unless the spacing is chosen
   against a stated $\sigma_T$.
2. **Treating $\tau(p)$ as if it were a direct measurement of depth.** It is
   $2\sum h_i\eta_i(p)$: a weighted sum, with the weights supplied by an assumed
   velocity model.
3. **Ignoring the fold.** Where $\mathrm{d}^{2}\tau/\mathrm{d}p^{2}$ changes sign,
   the transform has stopped being one-to-one and the branches must be separated
   first.
4. **Reporting only the median residual of a check.** Section 4.1's worst case is
   two orders of magnitude worse than its median; both numbers are part of the
   result.
5. **Confusing $p$ in $\mathrm{s\,m^{-1}}$ with $p$ in $\mathrm{s\,deg^{-1}}$ or
   $\mathrm{s\,rad^{-1}}$.** The conversion is a factor $\pi/180$ between
   $\mathrm{s\,rad^{-1}}$ and $\mathrm{s\,deg^{-1}}$, and it is a common source of
   three-digit errors.

## Related modules

- [06-01 Elastic Wave Propagation](../01-elastic-wave-propagation/README.md) —
  the wave physics that the slowness description approximates.
- [01 Eikonal Equation, Rays and Fermat's Principle](01-eikonal-and-rays.md) and
  [02 Snell's Law, Layered Media and the Travel-Time Curve](02-snell-and-layering.md) —
  the curve and the conservation law that are transformed here.
- [04 Ray Tracing in Laterally Varying Media](04-ray-tracing.md) — where these
  integrals are evaluated for media in which the closed forms do not exist.
- [05 Shadow Zones, Triplications and the Low-Velocity Zone](05-shadow-zones.md) —
  the folds and gaps that break the inversion, measured.
- [06-06 Seismic Tomography](../06-seismic-tomography/README.md) — the same
  slowness information inverted in two and three dimensions.
- [18-inverse-problems](../../18-inverse-problems/README.md) — the systematic
  treatment of unstable derivatives and regularisation.

## Exercises

Full sets with worked solutions are in
[`exercises/03-tau-p-exercises.md`](./exercises/03-tau-p-exercises.md) and
[`exercises/03-tau-p-solutions.md`](./exercises/03-tau-p-solutions.md).
