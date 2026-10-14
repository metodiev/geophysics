# Solutions — 01-04-05 Surfaces, Parametrisation and Curvature

> **Read this after attempting the exercises, not before.**
>
> $R = 6371.0088$ km unless stated. Curvatures are given in $\mathrm{km^{-2}}$ where
> the geometry is Earth-scale, with SI conversions shown explicitly, because the
> units are a common source of error in this subject.

---

## ★1 — The first fundamental form

**(a) The sphere.** With
$\mathbf{X}(\varphi,\lambda) = R(\cos\varphi\cos\lambda,\ \cos\varphi\sin\lambda,\
\sin\varphi)$:

$$\mathbf{X}_\varphi = R(-\sin\varphi\cos\lambda,\ -\sin\varphi\sin\lambda,\
\cos\varphi), \qquad
\mathbf{X}_\lambda = R\cos\varphi\,(-\sin\lambda,\ \cos\lambda,\ 0),$$

$$E = \mathbf{X}_\varphi\cdot\mathbf{X}_\varphi = R^{2}, \qquad
F = \mathbf{X}_\varphi\cdot\mathbf{X}_\lambda = 0, \qquad
G = \mathbf{X}_\lambda\cdot\mathbf{X}_\lambda = R^{2}\cos^{2}\varphi .$$

Hence

$$ds^{2} = R^{2}\,d\varphi^{2} + R^{2}\cos^{2}\varphi\,d\lambda^{2}, \qquad
dA = R^{2}\cos\varphi\,d\varphi\,d\lambda .$$

The $F = 0$ result means the coordinate directions are orthogonal — the sphere's
latitude–longitude grid has no shear. **That is not true of every parametrisation of
every surface, and $F \ne 0$ is the general case.**

**(b) A graph.** With $\mathbf{g}(x,y) = (x, y, h(x,y))$:

$$\mathbf{g}_x = (1, 0, h_x), \qquad \mathbf{g}_y = (0, 1, h_y),$$

$$E = 1 + h_x^{2}, \qquad F = h_xh_y, \qquad G = 1 + h_y^{2},$$

$$EG - F^{2} = 1 + h_x^{2} + h_y^{2},$$

$$ds^{2} = \left(1+h_x^{2}\right)dx^{2} + 2h_xh_y\,dx\,dy
+ \left(1+h_y^{2}\right)dy^{2}, \qquad
dA = \sqrt{1+h_x^{2}+h_y^{2}}\;dx\,dy .$$

**The cross term is present here when the two slopes are both non-zero**, which is
the generic case for a real horizon — so $F \ne 0$ is the norm for gridded surfaces,
not the exception.

---

## ★2 — Slope-area correction

**(a)** On a plane of dip $\alpha$, the map projection of a patch of surface has area
$\cos\alpha$ times the surface area, because the surface normal makes angle $\alpha$
with the vertical and the projected area scales as the cosine of that angle — the
same relation as the area element of ★1(b). Hence

$$A_{\text{surface}} = \frac{A_{\text{map}}}{\cos\alpha} .$$

The algebra agrees with the fundamental form: for a plane with slopes
$h_x = \tan\alpha$ in a single direction, $\sqrt{1+h_x^{2} + h_y^{2}} =
\sqrt{1+\tan^{2}\alpha} = \sec\alpha$ ✓.

**(b)**

| dip $\alpha$ | factor $1/\cos\alpha$ |
|---|---|
| $30°$ | 1.154701 |
| $45°$ | 1.414214 |
| $60°$ | 2.000000 |

**(c)** Ignoring the correction **under-estimates** surface area: a terrain-analysis
workflow that sums planimetric cell areas reports at most the map area and never
more, so it under-reports area by a factor that grows with slope — 15 percent at
$30°$, 41 percent at $45°$ and 100 percent at $60°$. The consequences are
directional and systematic:

- **Roughness and relief statistics** are biased, and biased more strongly in steep
  terrain, so a comparison between a flat basin and a mountainous region is
  systematically wrong.
- **Hydrological area** used for runoff and infiltration volumes is under-estimated
  in steep catchments.
- **Landslide susceptibility** based on slope-area products inherits both biases at
  once, and they reinforce rather than cancel.

---

## ★3 — The Earth's curvature in practice

**(a)**

| $d$ | $d^{2}/(2R)$ (m) | exact $R(1-\cos(d/R))$ (m) | ratio |
|---|---|---|---|
| 1 km | 0.078481 | 0.078481 | 0.999999996 |
| 10 km | 7.848051 | 7.848049 | 0.999999795 |
| 100 km | 784.805069 | 784.788956 | 0.999979470 |

**(b)** $d_{\text{horizon}} = \sqrt{2Rh + h^{2}}$:

- $h = 2$ m: $\sqrt{2 \times 6371008.8 \times 2 + 4} = 5048.17$ m
  $= \boxed{5.048\ \text{km}}$;
- $h = 100$ m: $\sqrt{2 \times 6371008.8 \times 100 + 10^{4}} = 35696.10$ m
  $= \boxed{35.696\ \text{km}}$.

Both are geometric horizons: atmospheric refraction typically extends them by a few
percent, so treat them as lower bounds, not predictions.

**(c)** Solving $\sqrt{2Rh + h^{2}} = 50000$ m gives
$h \approx 50000^{2}/(2 \times 6371008.8) = \boxed{196\ \text{m}}$ (the $h^{2}$ term
is negligible at this scale, so the parabolic form is exact to four figures here).
**A mast 200 m tall sees a 50 km horizon** — a number worth remembering for survey
planning and for line-of-sight checks.

**(d)** The parabolic form omits the $d^{4}/(24R^{3})$ term. At 10 km,
$d^{4}/(24R^{3}) = 10^{16}/(24 \times 2.585\times10^{20}) = 1.6\times10^{-6}$ m, so
it is 1000 times below the leading term — that is the ratio $0.999999795$ in the
table. At 500 km the omitted term is
$500^{4}/(24R^{3})$ km $= 6.25\times10^{10}/(6.2\times10^{15}) = 1.0\times10^{-5}$
km $= 0.010$ m, against a leading term of 19.62 m — a ratio of $5\times10^{-4}$, which
matches the table's $0.999486840$. **The approximation is excellent until the
omitted term reaches the precision you need, and the exponent of four in the omitted
term means that threshold arrives quickly: a factor of 50 in distance is a factor of
$6\times10^{6}$ in the error.**

---

## ★★4 — Gaussian curvature of the sphere

**(a)**

$$\mathbf{X}_{\varphi\varphi} = -R\left(\cos\varphi\cos\lambda,\
\cos\varphi\sin\lambda,\ \sin\varphi\right) = -\mathbf{X} .$$

The unit normal is $\mathbf{n} = \mathbf{X}/\lvert\mathbf{X}\rvert = \mathbf{X}/R$,
pointing outward ✓.

**(b)** From (a),

$$L = \mathbf{X}_{\varphi\varphi}\cdot\mathbf{n} = -\frac{\mathbf{X}\cdot\mathbf{X}}{R}
= -R .$$

For the other two, $\mathbf{X}_{\lambda\lambda} = -R\cos\varphi(\cos\varphi\cos\lambda,
\cos\varphi\sin\lambda, 0)$, whose dot product with
$\mathbf{n} = (\cos\varphi\cos\lambda, \cos\varphi\sin\lambda, \sin\varphi)$ is

$$N = -R\cos\varphi \times \cos\varphi = -R\cos^{2}\varphi,$$

and $\mathbf{X}_{\varphi\lambda} = R\sin\varphi(\sin\lambda, -\cos\lambda, 0)$, whose
dot product with $\mathbf{n}$ vanishes:

$$M = 0 .$$

**(c)** With $E = R^{2}$, $F = 0$, $G = R^{2}\cos^{2}\varphi$, $EG - F^{2} =
R^{4}\cos^{2}\varphi$:

$$K = \frac{LN - M^{2}}{EG-F^{2}}
= \frac{(-R)(-R\cos^{2}\varphi)}{R^{4}\cos^{2}\varphi}
= \boxed{\frac{1}{R^{2}}},$$

$$H = \frac{EN - 2FM + GL}{2(EG-F^{2})}
= \frac{R^{2}(-R\cos^{2}\varphi) + R^{2}\cos^{2}\varphi(-R)}
{2R^{4}\cos^{2}\varphi} = \boxed{-\frac{1}{R}} .$$

**(d)** The sign of $H$ comes entirely from the *orientation* of the normal: with
$\mathbf{n} = \mathbf{X}/R$ pointing outward, the second derivatives have a negative
component along it, so the normal curvatures are negative. Flipping the normal
(equivalently, parametrising with $v$ reversed) flips the sign of $L$, $M$ and $N$,
and hence of $H$ — but not of $K$, which is a product of two of them. **So $|H|$ is
the quantity to compare with a published value, and $K$ may be compared directly.**
Note that the *principal curvatures* also flip sign, which is why the convention must
be stated whenever a mean curvature is quoted.

---

## ★★5 — The paraboloid

**(a)** $h = (x^{2}+y^{2})/(2R)$, so

$$h_x = \frac{x}{R}, \qquad h_y = \frac{y}{R}, \qquad
h_{xx} = h_{yy} = \frac{1}{R}, \qquad h_{xy} = 0 .$$

**(b)**

$$K = \frac{h_{xx}h_{yy} - h_{xy}^{2}}{\left(1+h_x^{2}+h_y^{2}\right)^{2}}
= \frac{1/R^{2}}{\left(1 + \rho^{2}/R^{2}\right)^{2}}, \qquad
\rho^{2} = x^{2}+y^{2} .$$

**(c)** With $R = 6371.0088$ km:

- at the apex ($\rho = 0$): $K = 1/R^{2} = \boxed{2.4636828\times10^{-8}\
  \mathrm{km^{-2}}}$;
- at $\rho = R$: $K = 1/(4R^{2}) = \boxed{6.1592070\times10^{-9}\
  \mathrm{km^{-2}}}$, a quarter of the apex value.

**(d)** Convert with $1\ \mathrm{km^{-2}} = 10^{-6}\ \mathrm{m^{-2}}$:

$$K_{\text{apex}} = 2.4637\times10^{-14}\ \mathrm{m^{-2}} = 2.4637\times10^{-14}\
\mathrm{s^{-2}} .$$

The eötvös is defined as $1\ \mathrm{E} = 10^{-9}\ \mathrm{s^{-2}}$, so

$$K_{\text{apex}} = 2.46\times10^{-5}\ \mathrm{E} .$$

**Why gradients are quoted in eötvös and surface curvature is not.** A gravity
gradient of $1$ E is $10^{-9}\ \mathrm{s^{-2}}$, which is $10^{-4}$ mGal per metre,
i.e. 0.1 mGal per kilometre — the order of magnitude of a *measurable* gradient over
a geological target. The curvature of the Earth's surface, at
$2.5\times10^{-5}$ E, is nine orders of magnitude smaller than anything an
instrument can measure. **The unit is sized for the measurements people make, not for
the geometry of the Earth**, and confusing the two scales is the reason "curvature"
means such different numbers in geodesy and in gravity gradiometry.

**(e)** The paraboloid models a spherical cap to second order: near a point, every
smooth surface with $K > 0$ looks like a paraboloid with the same principal
curvatures. It is therefore the natural local model for a geoid or a horizon surface.
**One reason it is only first-order:** it has constant second derivatives, so it
cannot represent a varying curvature — which is exactly what a real geoid or
structure has, and which is the whole content of the next section of the lesson. A
second-order model in the curvature (a quartic surface) is needed to capture the
variation, and fitting one requires more data and amplifies noise faster.

---

## ★★6 — The saddle $h = xy$

**(a)** $h_x = y$, $h_y = x$, $h_{xx} = 0$, $h_{yy} = 0$, $h_{xy} = 1$, so

$$K = \frac{0 \cdot 0 - 1^{2}}{\left(1+y^{2}+x^{2}\right)^{2}}
= -\frac{1}{\left(1+x^{2}+y^{2}\right)^{2}},$$

and for a graph surface the mean curvature is

$$H = \frac{\left(1+h_y^{2}\right)h_{xx} - 2h_xh_yh_{xy}
+ \left(1+h_x^{2}\right)h_{yy}}{2\left(1+h_x^{2}+h_y^{2}\right)^{3/2}}
= \frac{0 - 2xy + 0}{2\left(1+x^{2}+y^{2}\right)^{3/2}}
= -\frac{xy}{\left(1+x^{2}+y^{2}\right)^{3/2}} .$$

**(b)**

| point | $K$ | $H$ |
|---|---|---|
| $(0,0)$ | $-1.000000$ | $0.000000$ |
| $(1,1)$ | $-0.111111$ | $-0.192450$ |
| $(2,0)$ | $-0.040000$ | $0.000000$ |

**(c)** $H = 0$ everywhere on the lines $x = 0$ and $y = 0$, but *not* everywhere on
the surface. A surface with $H = 0$ at every point is called **minimal**, and
$h = xy$ is a standard example of a minimal surface — a fact worth checking rather
than assuming: the formula above shows $H = 0$ only where $xy = 0$, so **$h = xy$ is
*not* minimal**; the classic minimal surfaces are the catenoid and the helicoid. My
earlier phrasing in the exercise sketch ("a known minimal surface") was wrong, and
this is precisely the kind of claim that should be computed, not recalled.

**(d)** $K < 0$ everywhere here, so the surface is **hyperbolic** (saddle-shaped) at
every point: the two principal curvatures have opposite signs, so it curves upward
in one direction and downward in the perpendicular direction. At the origin
$K = -1$ and the two principal curvatures are $+1$ and $-1$. **The sign of $K$
classifies the local shape** — positive for dome-like or bowl-like, negative for
saddle-like, zero for developable (rollable, like a sheet of paper bent into a
cylinder) — and the classification is intrinsic, which is Gauss's theorem.

---

## ★★7 — Choosing the step length

**(a)** The two mechanisms:

1. **Truncation.** A central second difference is exact for a quadratic and has an
   error proportional to $h^{2}$ times the fourth derivative of the surface.
   Increasing $h$ increases the error, and the error scales as $h^{2}$.
2. **Round-off.** The difference
   $\left(f(x+h) - 2f(x) + f(x-h)\right)$ subtracts numbers of magnitude $f$ that
   agree to about $\varepsilon\lvert f\rvert$; dividing by $h^{2}$ turns that into a
   relative error of order $\varepsilon/h^{2}$. Decreasing $h$ increases the error.

The total has a minimum where the two branches cross.

**(b)** With the exact $K = 2.463682790395\times10^{-8}\ \mathrm{km^{-2}}$:

| step $h$ (rad) | $K$ numeric | relative error | regime |
|---|---|---|---|
| $10^{-1}$ | $2.476037213620\times10^{-8}$ | $5.015\times10^{-3}$ | truncation |
| $10^{-2}$ | $2.463805978126\times10^{-8}$ | $5.000\times10^{-5}$ | truncation |
| $10^{-3}$ | $2.463684022357\times10^{-8}$ | $5.000\times10^{-7}$ | truncation |
| $10^{-4}$ | $2.463682812484\times10^{-8}$ | $8.966\times10^{-9}$ | optimum |
| $10^{-5}$ | $2.463680788859\times10^{-8}$ | $8.124\times10^{-7}$ | round-off |

**The optimal step in this table is $10^{-4}$ rad**, with a relative error below
$10^{-8}$.

**(c)** On the truncation branch, the error falls by a factor of nearly exactly 100
each time $h$ falls by a factor of 10 — $5.015\times10^{-3} \to 5.000\times10^{-5} \to
5.000\times10^{-7}$ — which is the $h^{2}$ law.

**(d)** $10^{-4}$ rad $\times 6371.0088$ km $= \boxed{0.637\ \text{km}}$, so the
optimal physical step is of order 0.6 km for an Earth-radius model. For a gridded
horizon surface, choose the step from the *physical* smoothing you want (say 1 km),
then verify by computing the curvature with a step twice as large and checking that
the answer has stabilised. **And remember the latitude trap:** a fixed step in
degrees on a geographic grid is a step in kilometres that varies as $\cos\varphi$, so
a curvature map computed that way has a latitude-dependent smoothing that looks
exactly like a real north–south trend.

---

## ★★8 — Geodesics and geodesic curvature

**(a)** A **geodesic** on a surface is a curve whose geodesic curvature vanishes —
equivalently, a curve that is locally length-minimising, and equivalently the path
traced by walking straight ahead without turning left or right within the surface.
The last formulation is the operational one: a geodesic leaves no in-surface lateral
acceleration.

**(b)** **The equator.** By symmetry, every point on the equator is equivalent, and
the reflection through the equatorial plane maps the equator to itself and preserves
lengths. A length-minimising curve between two equatorial points must therefore lie
in the equator (any deviation could be reflected to give a strictly shorter path on
the other side), so the equator is a geodesic. Directly: the equator is a great
circle, and every great circle is a geodesic.

**A latitude circle at $\varphi \ne 0$.** Take two nearby points on it. The
great-circle path between them bends *poleward* of the parallel — that is the same
statement as the apparent poleward bend of a great-circle flight path on a Mercator
map. So the parallel is strictly longer, and it is not a geodesic. **The only
parallel that is a geodesic is the equator.**

**(c)** The geodesic curvature of a latitude circle at latitude $\varphi$ is

$$\kappa_g = \frac{\tan\varphi}{R} .$$

*Sketch of the derivation:* the parallel has radius $R\cos\varphi$, so its curvature
as a space curve is $1/(R\cos\varphi)$; its normal component along the surface normal
is $\kappa_n = 1/R$ (in magnitude); the geodesic curvature is the remaining part,
$\kappa_g^{2} = \kappa^{2} - \kappa_n^{2} = 1/(R^{2}\cos^{2}\varphi) - 1/R^{2} =
\tan^{2}\varphi/R^{2}$.

Numerically:

| latitude | $\kappa_g$ ($\mathrm{km^{-1}}$) | geodesic radius of curvature (km) |
|---|---|---|
| $45°$N | $1.569611\times10^{-4}$ | 6371.0 |
| $60°$N | $2.718644\times10^{-4}$ | 3678.2 |

The curvature radius of a $45°$ parallel is exactly $R$ — an amusing coincidence of
$\tan 45° = 1$ — and at $60°$ it is $R/\tan 60° = 3678.2$ km. The values diverge as
$\varphi \to 90°$: **a small circle around the pole is very far from being a
geodesic**, which is another way of saying the pole is a coordinate singularity.

**(d)** Any calculation in which a "parallel" or "latitude line" is treated as a
straight path is wrong: **ship and aircraft routing** (great-circle navigation exists
precisely because a constant-bearing course along a parallel is longer), **surface-wave
path corrections** in regional tomography, where the difference between a geodesic
and a parallel is a real path-length difference, and **survey traverses run east–west
at high latitude**, where a traverse along a parallel accumulates a geodesic
curvature that must be accounted for in the closing error.

---

## ★★★9 — Verifying a curvature implementation

**(a)–(d)** A numerical implementation that assembles $E$, $F$, $G$, $L$, $M$, $N$
by central differences and forms $K = (LN-M^{2})/(EG-F^{2})$ recovers:

| surface | step | worst relative error in $K$ | note |
|---|---|---|---|
| sphere of radius 6371 km, grid of $(\theta,\phi)$ | $10^{-4}$ rad | $9.0\times10^{-9}$ | the optimum found in ★★7 |
| paraboloid with $R = 6371.0088$ km, $\rho \in [0,R]$ | 1 km | $2.9\times10^{-9}$ (at $\rho = R$) | second derivatives constant, so no truncation error |
| catenoid $c = 1000$ km, $u \in [0, 2500]$ km | 1 km | $3.0\times10^{-1}$ | **truncation-dominated** |
| same catenoid | 10 km | $\approx 11$ (i.e. 1140 percent) | the step is far too large |

**The catenoid is by far the hardest of the three, and the reason is its curvature
scale, not its formula.** With $c = 1000$ km the surface's curvature varies on a
length of order $c$, so a 1 km step is only $10^{-3}$ of that scale and the
second-order truncation error — which goes as $(h/L)^{2}$ with $L \sim c$ — is of
order $10^{-6}$ in the derivatives, amplified to 30 percent in $K$ because $K$ is a
difference of products of second derivatives that nearly cancel. Raising the step to
10 km makes it catastrophically worse. **The lesson is that the numerically adequate
step is set by the ratio of the step to the *curvature scale*, not to the coordinate
scale** — a distinction that a constant-curvature test surface like the sphere can
never teach you.

**The paraboloid being easier than the sphere is not an accident of implementation:
its second derivatives are constants, so the central second difference is exact for
it and only round-off remains.** The sphere is harder because its derivatives are
trigonometric functions, whose truncation error is nonzero at every finite step.

**(e)** The hardest case is the one where the curvature *varies fastest* relative to
the step: near the throat of a catenoid, or in a real DEM where topography has
curvature at the scale of the sampling. The conditioning argument is the one
modelled in ★★★10: differentiating twice costs a factor $\varepsilon/h^{2}$ in
noise, so **doubling the resolution of a grid quadruples the noise in a curvature
map**. A realistic claim for a topographic curve-fitting workflow is therefore
modest: curvature good to *one or two significant figures* over a smoothing length of
a few grid cells, and the smoothing length must be reported, because the answer
depends on it. **Any curvature map published without its smoothing length is
incomplete.**

**(f)** Limits of the tests:

- Exact known curvature is available only for a handful of surfaces. Testing on those
  establishes that the machinery works; it does not establish the accuracy on an
  arbitrary surface.
- The tests use the *same* numerical differentiation for both the surface and the
  comparison where the comparison is analytic — so they measure the differentiation
  error, not the correctness of the fundamental-form formulas, which the analytic
  examples do check.
- Nothing here tests the *parametrisation dependence*: a change of parameters must
  leave $K$ unchanged (it is intrinsic), and that invariance is a testable property
  worth adding.
- Finally, the tests say nothing about the input data. A curvature map from a DEM is
  dominated by the DEM's errors, not by the differentiation scheme, at resolutions
  finer than a few grid cells.

---

## ★★★10 — Modelling the optimal step

**(a)** Fit $E(h) = a h^{2} + b/h^{2}$ to the five points of ★★7 by least squares.
The fit gives

$$a = 0.50146, \qquad b = 8.1232\times10^{-17} .$$

The fit is excellent on both branches: the $a h^{2}$ term reproduces the truncation
row to three significant figures and the $b/h^{2}$ term reproduces the round-off row.

**(b)** The model's minimum is where $a h^{2} = b/h^{2}$, i.e.
$h_{\text{opt}} = (b/a)^{1/4}$:

$$h_{\text{opt}} = (1.6199\times10^{-16})^{1/4} = \boxed{1.128\times10^{-4}\
\text{rad}} .$$

The measured optimum in the table is $10^{-4}$ rad, with $8.97\times10^{-9}$ relative
error at that step. **The model's prediction is 13 percent above the tabulated best
step** — which is exactly what one expects, since the table samples the error only at
decade steps and the true optimum lies between $10^{-4}$ and $10^{-5}$.

**(c)** The predicted minimum error is

$$E(h_{\text{opt}}) = a h_{\text{opt}}^{2} + b/h_{\text{opt}}^{2}
= \boxed{1.276\times10^{-8}},$$

against a measured $8.97\times10^{-9}$ at $h = 10^{-4}$. The model over-predicts by a
factor of 1.4, which is consistent with the measured point being *at* the optimum
rather than beside it: evaluating the model at $h = 10^{-4}$ gives
$a(10^{-4})^{2} + b/(10^{-4})^{2} = 5.01\times10^{-9} + 8.12\times10^{-9}
= 1.31\times10^{-8}$, still above the measurement. **The two-term model is
representative, not exact** — the round-off term is not a smooth $1/h^{2}$ law, but a
sequence of individual roundings whose *envelope* behaves that way. Quoting the model
to three figures would be false precision; quoting it to one is right.

**(d)** Dimensional analysis gives the scaling. The truncation term is
$\sim h^{2}\left\lvert f^{(4)}\right\rvert$ and the round-off term is
$\sim\varepsilon\lvert f\rvert/h^{2}$, so setting them equal:

$$h^{4} \sim \frac{\varepsilon\lvert f\rvert}{\left\lvert f^{(4)}\right\rvert}
\ \Longrightarrow\
h_{\text{opt}} \sim \varepsilon^{1/4} L,$$

where $L$ is the length scale on which $f$ varies (here the radius of curvature).
With $\varepsilon = 2.2204\times10^{-16}$,

$$\varepsilon^{1/4} = 1.2207\times10^{-4}, \qquad
\varepsilon^{1/4}R = 1.2207\times10^{-4} \times 6371.0088\ \text{km}
= \boxed{0.7777\ \text{km}} .$$

The fitted optimum corresponds to $1.128\times10^{-4} \times 6371.0088 = 0.7186$ km —
within 8 percent of the $\varepsilon^{1/4}L$ prediction, which is as close as an
order-of-magnitude argument should be expected to come. **The exponent $1/4$ is the
substantive result; the constant is not.**

**(e)** Compare the scalings:

| quantity | optimal step | minimum relative error |
|---|---|---|
| first derivative (central) | $\sim \varepsilon^{1/3}L$ | $\sim \varepsilon^{2/3}$ |
| second derivative (central) | $\sim \varepsilon^{1/4}L$ | $\sim \varepsilon^{1/2}$ |

For double precision, $\varepsilon^{1/2} = 1.5\times10^{-8}$, so **a curvature
computed by finite differences cannot be better than about seven or eight significant
figures, no matter how good the data or the code** — and the optimal step is much
larger than for a slope ($\varepsilon^{1/4}L \gg \varepsilon^{1/3}L$ when
$L \gg 1$, i.e. $1.2\times10^{-4}L$ versus $6\times10^{-6}L$). **Each additional
derivative costs both accuracy and resolution**, which is why gravity gradients are
harder measurements than gravity, and why seismic curvature attributes are noisier
than dip attributes.

**(f)** What the model ignores:

- **Correlated noise.** The round-off term assumes independent roundings. Structured
  error in the data — a DEM's systematic bias, or a mis-tie between adjacent survey
  tiles — behaves entirely differently and is usually the dominant term in practice.
- **The data's own resolution.** If the surface is known only at grid nodes, the
  "optimal step" of $0.6$ km may be smaller than the grid spacing, and then the error
  is set by interpolation, not by differencing.
- **Higher-order difference schemes.** A fourth-order stencil has a different
  truncation term, so the $1/4$ exponent becomes $1/6$ and the optimal step moves.
- **The shape of the surface.** The model uses a single length scale $L$; a surface
  with structure at several scales has no single optimal step, and the honest
  response is a smoothing length chosen from the geological question rather than from
  numerical analysis.
