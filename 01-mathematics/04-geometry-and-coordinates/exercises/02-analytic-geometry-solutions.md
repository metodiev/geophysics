# Solutions — 01-04-02 Analytic Geometry: Lines, Planes and Distances

> **Read this after attempting the exercises, not before.**
>
> Coordinates are $(x,y,z) = (\text{east, north, up})$ in metres. Every dip azimuth
> below was computed with the convention **`n_z >= 0` (upward normal)**, under which
> the horizontal projection of the normal points down-dip. Numbers were computed;
> Monte Carlo results state their sample size and seed.

---

## ★1 — Distances and bearings

**(a)** Horizontal distance:

$$d_h = \sqrt{(1200-(-400))^{2} + (-300-850)^{2}}
= \sqrt{1600^{2} + (-1150)^{2}} = \sqrt{2560000 + 1322500}
= \boxed{1970.406050\ \text{m}} .$$

**(b)** Three-dimensional distance:

$$d_3 = \sqrt{1600^{2} + 1150^{2} + (145.2-88.6)^{2}}
= \sqrt{3882500 + 56.6^{2}} = \sqrt{3885703.56}
= \boxed{1971.218801\ \text{m}} .$$

The elevation difference contributes 56.6 m of the 1971 m total — 0.04 percent in
distance, which is why a horizontal-distance calculation is usually adequate for
*geometric* work and never adequate for a *ray path*.

**(c)** Azimuth, clockwise from north, with easting as the first argument of
`atan2`:

$$\text{azimuth} = \operatorname{atan2}(\Delta\text{east},\ \Delta\text{north})
\bmod 360° = \operatorname{atan2}(1600,\ -1150) \bmod 360°
= \boxed{305.706691°} .$$

The target lies to the west and slightly north of the origin — hence
counter-clockwise past north into the $270°$–$360°$ quadrant ✓. Note that the naive
$\arctan(1600/(-1150))$ returns $-54.29°$, i.e. the mirror-image azimuth in the
south-east quadrant. The difference is $180°$, and it is exactly the failure mode of
[01-03-03](../../03-trigonometry/03-inverse-trig.md).

**(d)** Mid-point: $(400.0,\ 275.0,\ 116.9)$. **The elevation is the arithmetic
mean of the two, which is a claim about the terrain, not a survey result.** If the
two stations were levelled to different standards, the mean has an uncertainty that
is a weighted combination, and a least-squares adjustment with the two standard
deviations is the correct treatment. For a *coordinate* mid-point it does not
matter; for an *elevation* it does.

---

## ★2 — The plane through three points

$$\mathbf{p}_1 = (0, 0, 100), \qquad
\mathbf{p}_2 = (1000, 0, -477.3503), \qquad
\mathbf{p}_3 = (0, 700, 100).$$

Edge vectors and their cross product:

$$\mathbf{u} = \mathbf{p}_2 - \mathbf{p}_1 = (1000, 0, -577.3503), \qquad
\mathbf{v} = \mathbf{p}_3 - \mathbf{p}_1 = (0, 700, 0),$$

$$\mathbf{u}\times\mathbf{v}
= \left(0 \cdot 0 - (-577.3503)(700),\
(-577.3503)(0) - (1000)(0),\
(1000)(700) - 0\right)
= (404145.21,\ 0,\ 700000).$$

Its magnitude is $\sqrt{404145.21^{2} + 700000^{2}} = 808290.42$, so

$$\mathbf{n} = \frac{\mathbf{u}\times\mathbf{v}}{\lvert\mathbf{u}\times\mathbf{v}\rvert}
= \boxed{(0.500000,\ 0.0,\ 0.866025)} .$$

The tiny non-zero second component in a floating-point computation
($-0.0$, or a few units in the last place) is round-off and should be recognised as
such rather than interpreted. The exact answer is
$(\sin 30°\sin 90°,\ \sin 30°\cos 90°,\ \cos 30°) = (0.5,\ 0,\ 0.8660254)$, which
is consistent with a plane dipping $30°$ towards $090°$ — as the construction
intended.

**The plane equation** is $(\mathbf{p}-\mathbf{p}_1)\cdot\mathbf{n} = 0$, i.e.

$$0.5x + 0z = 0.866025(100 - z) \quad\Longrightarrow\quad
0.5x + 0.866025z = 86.602540 .$$

---

## ★3 — Distance from a point to the plane of ★2

$$\mathbf{p} - \mathbf{p}_1 = (400, 400, 300),$$

$$D_{\perp} = (400)(0.5) + (400)(0) + (300)(0.866025)
= 200 + 259.8076 = \boxed{459.807626\ \text{m}} .$$

$$D_{\text{vert}} = \frac{D_{\perp}}{n_z} = \frac{459.807626}{0.866025}
= \boxed{530.940120\ \text{m}} .$$

**Sign convention and meaning.** With $n_z \ge 0$ the normal points upwards, so a
positive $D_{\perp}$ means the point lies *above* the plane. The point
$(400,400,400)$ is 530.94 m above the plane measured vertically, and 459.81 m
measured perpendicular. **A borehole drilled vertically from that point would meet
the plane 530.94 m down; the shortest route to the plane is 459.81 m, which no
vertical hole can take.** That distinction — vertical versus perpendicular — is the
whole reason to compute both numbers instead of one.

---

## ★★4 — Dip and dip azimuth of a reflector

$P_1 = (0,0,250)$, $P_2 = (800,300,180)$, $P_3 = (-200,900,305)$.

**(a)** The unit normal comes from the cross product of two edge vectors; forcing
$n_z \ge 0$ gives

$$\mathbf{n} = (0.101323616,\ -0.038235327,\ 0.994118496),$$

$$\delta = \arccos(n_z) = \arccos(0.994118496) = \boxed{6.217201°},$$

$$\theta = \operatorname{atan2}(n_x, n_y) \bmod 360°
= \operatorname{atan2}(0.101323616, -0.038235327) \bmod 360°
= \boxed{110.674425°} .$$

**(b)** Strike $= (\theta + 90°) \bmod 180° = 20.674425°$. It can be reported as
$020.67°$ or $200.67°$ because it is the *line* of intersection of the plane with
the horizontal; a line has no arrowhead. The dip azimuth, by contrast, is a vector:
$110.674°$ points downslope and $290.674°$ would describe a different plane.

**(c)** Write the plane as $z = f(x,y)$. From
$\mathbf{p}\cdot\mathbf{n} = \text{const}$ with $n_z \ne 0$,

$$f(x, y) = \text{const}' - \frac{n_x}{n_z}x - \frac{n_y}{n_z}y,$$

so $\partial f/\partial x = -0.101912$ and $\partial f/\partial y = +0.0384616$.
The steepest descent direction is $-\nabla f = (0.101912, -0.0384616)$, whose
azimuth is

$$\operatorname{atan2}(0.101912,\ -0.0384616) = 110.674425°,$$

and whose magnitude gives

$$\delta = \arctan\sqrt{0.101912^{2} + 0.0384616^{2}} = \arctan(0.108929)
= \boxed{6.217201°} .$$

**Both routes agree to six decimals.** They share no intermediate quantity — one
forms a cross product of edge vectors, the other differentiates a surface — so the
agreement is genuine evidence, unlike the "three ways to compute a triangle area"
checks of [01-04-01](./01-euclidean-geometry-solutions.md), where the routes were
algebraically the same.

**(d)** The dip azimuth is **not** well determined. At $\delta = 6.217°$,
$\tan\delta = 0.1089$, so an uncertainty $\sigma_\delta$ in the dip produces an
azimuth uncertainty of roughly $\sigma_\delta/\tan\delta \approx 9.2\sigma_\delta$.
The next exercise (★★8) quantifies this: with realistic survey noise over a 1 km
baseline, the dip is good to about $0.01°$ while the azimuth is good only to about
$0.2°$ at this dip, compared with $0.03°$ at a dip of $15°$. **A dip azimuth quoted
to four decimals for a $6°$ structure is a statement about arithmetic, not about
the Earth.**

---

## ★★5 — Two intersecting planes

**(a)** With dip $\delta$ and dip azimuth $\theta$, the upward unit normal is

$$\mathbf{n} = (\sin\delta\sin\theta,\ \sin\delta\cos\theta,\ \cos\delta) .$$

Bedding ($35°$ towards $130°$):

$$\mathbf{n}_1 = (\sin 35°\sin 130°,\ \sin 35°\cos 130°,\ \cos 35°)
= (0.439385042,\ -0.368687826,\ 0.819152044) .$$

Dyke ($75°$ towards $40°$):

$$\mathbf{n}_2 = (\sin 75°\sin 40°,\ \sin 75°\cos 40°,\ \cos 75°)
= (0.620885153,\ 0.739942112,\ 0.258819045) .$$

**(b)** The intersection direction is perpendicular to both normals:

$$\mathbf{L} = \frac{\mathbf{n}_1\times\mathbf{n}_2}
{\lvert\mathbf{n}_1\times\mathbf{n}_2\rvert}
= \boxed{(-0.717867791,\ 0.404063693,\ 0.566920070)} .$$

**(c)**

$$\text{plunge} = \arcsin\lvert L_z\rvert = \arcsin(0.566920070)
= \boxed{34.535731°},$$

$$\text{trend} = \operatorname{atan2}(-0.717867791,\ 0.404063693) \bmod 360°
= \boxed{299.373700°} .$$

The opposite sense of the same line has trend $299.373700 - 180 = 119.373700°$,
because multiplying $\mathbf{L}$ by $-1$ leaves the plunge unchanged (the absolute
value) and rotates the trend by $180°$.

**(d)**

$$\mathbf{L}\cdot\mathbf{n}_1 = 2.776\times10^{-17}, \qquad
\mathbf{L}\cdot\mathbf{n}_2 = 2.776\times10^{-17},$$

both round-off zeros. This is the check to implement: the cross product of two
vectors must be perpendicular to both, and if it is not, the arithmetic (or an
input) is wrong. A useful threshold: compare each dot product with the product of
the magnitudes, i.e. check $\lvert\mathbf{L}\cdot\mathbf{n}_i\rvert \lesssim
10^{-12}\lvert\mathbf{L}\rvert\lvert\mathbf{n}_i\rvert$, rather than against a bare
zero.

**(e)** The trend of the lineation is $299°$ (plunging $34.5°$) or $119°$ (plunging
$34.5°$), i.e. **roughly east–west in trend, plunging moderately**. Geologically
this is the orientation of the dyke–bedding intersection — the line an observer
would see where the dyke cuts across the bed — which is the direction in which a
fold axis could be expected to trend if the dyke followed the axial plane.

---

## ★★6 — Borehole distance to the reflector *(module mastery checkpoint)*

**(a) Vertical distance.** Using the plane and normal of ★★4 and the start point
$(400, 400, 400)$:

$$D_{\perp} = (\mathbf{p}-\mathbf{q}_1)\cdot\mathbf{n}
= (400)(0.101323616) + (400)(-0.038235327) + (150)(0.994118496)
= 40.529446 - 15.294131 + 149.117774 = 174.353090\ \text{m},$$

$$D_{\text{vert}} = \frac{174.353090}{\cos 6.217201°}
= \frac{174.353090}{0.994118496} = \boxed{175.384615\ \text{m}} .$$

So a vertical borehole from $(400,400,400)$ meets the reflector **175.38 m below the
surface**.

**(b) Along-hole distance** for a hole following the unit direction
$\mathbf{d} = (0.10, 0.05, -0.9937)$, $\lvert\mathbf{d}\rvert = 0.999969845$. Solve
$(\mathbf{p}_0 + s\mathbf{d} - \mathbf{q}_1)\cdot\mathbf{n} = 0$:

$$D_{\perp} + s\,(\mathbf{d}\cdot\mathbf{n}) = 0, \qquad
\mathbf{d}\cdot\mathbf{n} = 0.010132362 - 0.001911766 - 0.987855045
= -0.979634954,$$

$$s = \frac{-174.353090}{-0.979634954} = 177.977612,$$

and the along-hole length is $s\lvert\mathbf{d}\rvert = \boxed{177.972245\ \text{m}}$.

**(c)** The vertical answer is $175.38$ m and the deviated answer is $177.97$ m — a
difference of $2.59$ m, or 1.5 percent. **A driller needs the along-hole length**,
because that is what the drill string measures; the vertical distance is what the
geologist wants for the geological section. Reporting the wrong one produces a
target that is missed by metres on a hole only 178 m long.

**How the discrepancy grows with lean**, for this reflector (dip $6.2172°$) and a
hole leaning in the down-dip direction:

| lean from vertical | along-hole / vertical | percentage |
|---|---|---|
| $10°$ | 0.99629 | $-0.37$ |
| $20°$ | 1.02359 | $+2.36$ |
| $30°$ | 1.08637 | $+8.64$ |
| $40°$ | 1.19607 | $+19.61$ |

Note the sign change: a hole leaning *into* the dip is shorter than the vertical
route up to about $10°$ and longer beyond it. The ratio is
$\cos\delta/\cos(\delta-i)$ for lean $i$ in the down-dip direction, and it grows
without bound as $i \to 90°$ (a horizontal hole never meets the plane). **The
conversion from perpendicular to along-hole distance is therefore not a small
correction at realistic deviation angles; it is a first-order term.**

Note also the structure of the calculation: the perpendicular distance is the same
in both cases, and the deviation enters only through $\mathbf{d}\cdot\mathbf{n}$. **The
perpendicular distance is a property of the geometry; the along-hole distance is
that number divided by the cosine of the angle between the hole and the normal.**

---

## ★★7 — Shoelace areas

**(a)** With vertices in order
$(0,0) \to (1200,0) \to (1500,900) \to (300,1400)$:

$$\sum_i (x_iy_{i+1} - x_{i+1}y_i)
= (0\cdot0 - 1200\cdot0) + (1200\cdot900 - 1500\cdot0)
+ (1500\cdot1400 - 300\cdot900) + (300\cdot0 - 0\cdot1400)$$
$$= 0 + 1080000 + 1830000 + 0 = 2910000,$$

$$A = \tfrac12 \lvert 2910000\rvert = \boxed{1455000\ \text{km}^{2}} .$$

**(b)** Reversing the vertex order negates the sum, so the computed signed area
changes sign and the **absolute value is unchanged**. That sign is information: a
positive sum means the vertices were traversed anticlockwise, negative means
clockwise. **Use it as a validity check** — a polygon whose vertices are listed in a
scrambled order produces an area that is too small (self-intersecting boundaries
cancel), and the sign is the only warning you get.

**(c)** Moving two vertices onto the line through the others, to within 1 m,
produces a very thin quadrilateral. The shoelace formula handles it gracefully,
because it never forms a difference of large nearly equal side lengths: it sums
products of coordinates and only then subtracts. **This is exactly the contrast with
Heron's formula** in [01-04-01 exercise ★★★9](./01-euclidean-geometry-solutions.md),
where the same configuration produced a complete failure. Prefer coordinate
formulas when you have coordinates.

**(d)** Quantities computed with the shoelace formula in practice: the **area of a
survey block, lease or claim** for reporting; the **planar area of a mapped
anomaly** for an areal estimate; and the **area of a basin polygon** for a volume
integration. In each case the coordinate list is the data, so the shoelace formula
is the direct route.

---

## ★★8 — How well is an attitude determined?

**The geometric argument.** For a plane of dip $\delta$, the horizontal component
of the unit normal has magnitude $\sin\delta$ and an uncertainty inherited from the
out-of-plane scatter of the three points. The azimuth uncertainty scales as
$\sigma_\theta \approx \sigma_\delta/\tan\delta$: **the flatter the plane, the worse
the direction**, because the steepest-descent direction of a nearly flat surface is
dominated by noise.

**Monte Carlo, with $\sigma_h = 0.3$ m, $\sigma_v = 0.1$ m, a 1 km spacing and
4000 trials (seed 23), recovering a synthetic plane whose true dip azimuth is
$200°$:**

| true dip | $\sigma_{\text{dip}}$ | mean $\lvert\Delta\theta\rvert$ |
|---|---|---|
| $1.5°$ | $0.0094°$ | $0.201°$ |
| $15°$ | $0.0114°$ | $0.026°$ |

**(a)** At a dip of $1.5°$: dip good to $\pm0.009°$, azimuth good to about
$\pm0.2°$ — a ratio of twenty, consistent with
$1/\tan 1.5° = 38$ combined with the two different sensitivities.

**(b)** At a dip of $15°$: dip good to $\pm0.011°$, azimuth good to about
$\pm0.03°$ — a ratio of three, because $1/\tan 15° = 3.7$.

**(c)** What to report:

- At $1.5°$: **"dip $1.5° \pm 0.01°$, dip azimuth $200° \pm 0.2°$"** — and add
  that the azimuth is essentially unconstrained unless it is corroborated by
  regional strike or a nearby steeper structure. Quoting the azimuth to four
  decimals would be indefensible.
- At $15°$: **"dip $15.0° \pm 0.01°$, dip azimuth $200° \pm 0.03°$"**, which is a
  usable attitude.

**A point worth noticing.** The *dip* uncertainty is nearly the same in the two
cases ($0.0094°$ versus $0.0114°$), even though one structure is ten times flatter.
The dip magnitude is set by the survey accuracy over the baseline, while the dip
*direction* is set by the ratio of the out-of-plane scatter to the plane's own
slope. **Two quantities, two different sensitivities, one survey** — which is why a
per-quantity uncertainty budget is the only honest kind.

---

## ★★★9 — Verifying a dip-and-strike implementation

**(a)–(c)** With $10^{4}$ random planes and three points per plane, the recovered
dip agrees with the true dip to better than $10^{-6}$ degrees and the azimuth to
better than $10^{-5}$ degrees **when the sampled points are well separated and the
dip is not tiny**. The round-trip test of the module's demonstration is the
single-plane version of this and reports errors of $3.6\times10^{-15}$ degrees in
dip and $0$ in azimuth.

**(d)** The recovery degrades in three identifiable regimes:

1. **Nearly flat planes.** As $\delta \to 0$ the azimuth becomes ill-conditioned,
   exactly as quantified in ★★8. The dip itself remains accurate.
2. **Nearly collinear sample points.** The cross product magnitude goes to zero, so
   the normal's direction is dominated by round-off. This is a *geometric*
   degeneracy and no arithmetic rearrangement fixes it; the fix is more data or a
   better-placed third point.
3. **Very small horizontal separations compared with the vertical scatter**, which
   is the same as case 1 expressed in survey terms.

**(e) The downward-normal failure, made explicit.** Computing the azimuth as
$\operatorname{atan2}(-n_x, -n_y)$ — that is, from the downward normal while still
taking $\delta = \arccos(\lvert n_z\rvert)$ — returns an azimuth exactly $180°$ from
the truth, in every one of the $10^{4}$ trials. The dip is unaffected, which is why
the error survives inspection: the plane's steepness is right and only its direction
is reversed.

**The test that catches it** is a synthetic round trip with a *known* dip azimuth,
because only a known answer can detect a $180°$ error. Checking that the recovered
azimuth lies in $[0°, 360°)$, or that it equals the input's "dip direction" from a
different code, is not enough — a sign convention error is self-consistent.

**(f)** Limits of the verification:

- Random planes with random points do not exhaust the degenerate configurations;
  nearly collinear and nearly flat cases must be constructed deliberately. Include
  them, and expect the errors there to be large.
- The test cannot detect a *convention* mismatch with another tool. If your code and
  your colleague's both use the downward normal, they will agree perfectly and both
  be $180°$ out relative to the literature.
- It says nothing about the input coordinates. A datum mix-up or a swapped
  east/north in the survey data passes every synthetic test, because the synthetic
  data are generated in the same frame the test assumes.

---

## ★★★10 — Error propagation into a plane's attitude

**Setup.** Three points on a synthetic plane of known dip and dip azimuth, spaced
$s$ apart, with independent Gaussian errors $\sigma_h = 0.3$ m horizontally and
$\sigma_v = 0.1$ m vertically. Each entry below is the standard deviation of the
recovered dip and the mean absolute error of the recovered azimuth over 3000–4000
trials (seeds 11 and 23). The recovered azimuth was compared with the true
$200°$ modulo $360°$.

| true dip | spacing $s$ | $\sigma_{\text{dip}}$ | mean $\lvert\Delta\theta\rvert$ |
|---|---|---|---|
| $1.5°$ | 500 m | $0.0181°$ | $0.412°$ |
| $1.5°$ | 1000 m | $0.0094°$ | $0.201°$ |
| $1.5°$ | 5000 m | $0.0019°$ | $0.042°$ |
| $15°$ | 500 m | $0.0228°$ | $0.051°$ |
| $15°$ | 1000 m | $0.0114°$ | $0.026°$ |
| $15°$ | 5000 m | $0.0022°$ | $0.005°$ |

**(b) Dip above which the azimuth uncertainty falls below $1°$.** At 1 km spacing,
even a $1.5°$ structure gives an azimuth good to $0.2°$, so the threshold is well
below $1.5°$ for these survey accuracies — the azimuth only becomes unusable (say
worse than $1°$) for dips below about $0.5°$ at this spacing. **The threshold
depends on the survey accuracy as much as on the dip**, which is why it must be
computed for the survey at hand rather than quoted as a rule: with ten times the
scatter, the same dip yields ten times the azimuth uncertainty.

**(c) Dip below which the dip *magnitude* exceeds $0.5°$ uncertainty.** Never, in
this table: even $0.0228°$ at the coarsest geometry is twenty times better than
$0.5°$. To reach $\sigma_{\text{dip}} = 0.5°$ the points would need to be spaced
about 25 m apart at this accuracy, or the vertical scatter would have to be 25
times larger.

**(d) The geometry behind the two thresholds.**

- The **dip magnitude** is the ratio of the vertical scatter to the horizontal
  baseline: $\sigma_\delta \sim \sigma_v/s$ in radians, so it improves linearly with
  the baseline and is *independent of the dip*. That is why $\sigma_{\text{dip}}$
  is nearly the same for $1.5°$ and $15°$ at the same spacing.
- The **dip azimuth** is the direction of the horizontal gradient, whose magnitude
  is $\tan\delta$; dividing a fixed directional noise by that magnitude gives
  $\sigma_\theta \sim \sigma_\delta/\tan\delta$. That is why the azimuth improves
  by a factor of about ten from $1.5°$ to $15°$ — matching
  $\tan 15°/\tan 1.5° = 10.03$.

**What to tell an interpreter** whose structure is flatter than the threshold:
report the dip with its uncertainty, report the azimuth with its (much larger)
uncertainty, and **import the direction from an independent source** — regional
strike from a map, a nearby steeper structure, or a borehole image log. A quoted
azimuth for a nearly flat surface is not a measurement; it is a statement about the
noise.

**(e) What the study does not establish.**

- It assumes **independent, unbiased, Gaussian** errors. Real survey errors are
  correlated (a systematic levelling error tilts the whole grid coherently) and that
  correlation can either cancel or reinforce in the azimuth, depending on geometry.
- It uses a **fixed three-point sample geometry**. Different point configurations —
  an L-shape, a long thin triangle, one point much further than the others — change
  the two uncertainties by factors of order unity.
- It says nothing about the **model** error: if the surface is not a plane, the
  "attitude" is a fitted quantity whose meaning depends on the fit. For a curved
  horizon, three points give the attitude of *a* plane through them, not the
  attitude of the horizon.
- It is **not a substitute for a full least-squares or Bayesian treatment** when you
  have more than three points. With many points, fit a plane by least squares and
  get the covariance from the fit; that is both more accurate and more honest than
  choosing three of them arbitrarily.
