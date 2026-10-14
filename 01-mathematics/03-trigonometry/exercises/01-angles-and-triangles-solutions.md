# Solutions — 01-03-01 Angles, Triangles and the Unit Circle

> **Read this after attempting the exercises, not before.**
>
> These are *worked solutions*, showing a valid route and the reasoning. Numeric
> answers were computed rather than estimated by hand; where an answer is
> rounded, the rounding is stated. Where more than one answer is defensible, that
> is said explicitly.

---

## ★1 — Angle conversions

Use $1\ \text{rad} = 180°/\pi$ in the direction that makes the unit smaller or
larger as required.

| | Given | Answer | How |
|---|---|---|---|
| (a) | $60°$ | $\pi/3 = 1.047197551$ rad | multiply by $\pi/180$ |
| (b) | $0.75$ rad | $42.97183463°$ | multiply by $180/\pi$ |
| (c) | $2.5$ rad | $143.23944878°$ | multiply by $180/\pi$ |
| (d) | $12°30'$ | $0.218166156$ rad | $12.5°$, then $\times\pi/180$ |

**Sanity checks.** $60°$ is one sixth of a turn, and $2\pi/6 = \pi/3$ ✓. 2.5 rad
is a bit less than $\pi$ rad $= 180°$, and $143.2°$ is indeed a bit less ✓. The
radian is a *small* unit, so converting radians to degrees gives a *larger*
number: $0.75 \to 43.0$ ✓.

**On (d).** Sexagesimal notation is still standard in land surveying. $12°30'$
means $12.5°$. The arithmetic expects decimal degrees, so convert before
computing, and convert back only for reporting.

---

## ★2 — Signs and values in each quadrant

| | Angle | Quadrant | $\sin$ | $\cos$ | $\tan$ |
|---|---|---|---|---|---|
| (a) | $120°$ | II | $+\sqrt3/2 = 0.86602540$ | $-1/2$ | $-\sqrt3 = -1.73205081$ |
| (b) | $225°$ | III | $-\sqrt2/2 = -0.70710678$ | $-\sqrt2/2$ | $+1$ |
| (c) | $300°$ | IV | $-\sqrt3/2 = -0.86602540$ | $+1/2$ | $-\sqrt3 = -1.73205081$ |

**How to see each one without a table.** Reduce to a first-quadrant angle and
apply the reflection identities:

- $120° = 180° - 60°$, so $\sin 120° = \sin 60°$, $\cos 120° = -\cos 60°$.
- $225° = 180° + 45°$, so both sine and cosine flip sign, and the tangent is
  therefore positive: $\tan 225° = \tan 45° = 1$. Note that the *ratio* is
  positive even though both components are negative — the reason the tangent only
  has period $180°$.
- $300° = 360° - 60°$, so the sine flips sign and the cosine does not:
  $\tan 300° = -\tan 60°$.

**Which angle has an undefined tangent?** None of the three. The tangent is
undefined where $\cos\theta = 0$, at $\theta = 90°$ and $270°$ within the range
considered. There, $\tan\theta = \sin\theta/\cos\theta$ would require division by
zero. Note that $270°$ is one of the values where the *stored* cosine is about
$-1.8\times10^{-16}$ rather than 0, so a naive program will not raise an error;
it will return a number of order $10^{16}$ instead.

---

## ★3 — Arc length

**Governing relation.** For an angle $\theta$ in **radians** on a circle of radius
$r$, the arc length is $s = r\theta$.

**(a)** $\theta = 12° \times \pi/180 = 0.20943951$ rad. Then
$s = 3.2\ \text{km} \times 0.20943951 = 0.670206433$ km $= \boxed{670.2\ \text{m}}$.

**(b)** Now the arc and the radius are given, so solve for the angle:

$$\theta = \frac{s}{r} = \frac{250\ \text{m}}{6\,371\,000\ \text{m}}
= 3.924030764\times10^{-5}\ \text{rad}.$$

In degrees: $\theta \times 180/\pi = 0.002248304014°$. In arcseconds:
$\times 3600 = \boxed{8.0939''}$.

**Interpretation.** A 250 m offset on the Earth's surface is about 8 arcseconds of
arc. For scale: one arcsecond is about 30.9 m on the surface, and one degree is
about 111 km. That ratio is why surveying instruments are engineered for
sub-arcsecond angular precision — it is the only way to reach centimetre
positioning over a kilometre — and why survey software stores angles in radians
internally and displays them in degrees, minutes and seconds. It also explains the
conversion discipline this module insists on: a factor of 3600 between arcseconds
and degrees is easy to lose, and losing it turns a survey into nonsense while
every intermediate number still looks plausible.

---

## ★4 — Solving a triangle (SAS)

**Given** $b = 7$, $c = 9$, included angle $A = 42°$.

**Step 1 — the third side, by the law of cosines.** The included angle is known,
so the law of cosines applies directly and there is no ambiguity:

$$a^{2} = 7^{2} + 9^{2} - 2(7)(9)\cos 42° = 49 + 81 - 126(0.74314483)
= 130 - 93.636248 = 36.363752,$$

$$a = \boxed{6.030236479}.$$

**Step 2 — the remaining angles, by the law of cosines.** Using the law of
cosines for the angle is safer than the law of sines here, because the law of
cosines determines an angle uniquely in $[0°, 180°]$ while the law of sines leaves
the obtuse/acute choice open:

$$B = \arccos\!\left(\frac{a^{2}+c^{2}-b^{2}}{2ac}\right) = 50.96287883°,$$

$$C = \arccos\!\left(\frac{a^{2}+b^{2}-c^{2}}{2ab}\right) = 87.03712117°.$$

Check: $42 + 50.96287883 + 87.03712117 = 180.00000000$ ✓. That the sum is exactly
180 to eight decimals is the internal evidence that the arithmetic is right.

**Step 3 — circumdiameter, by the law of sines.**

$$2R = \frac{a}{\sin A} = \frac{6.030236479}{0.66913061} = \boxed{9.012047008}.$$

**Step 4 — area, two ways.**

$$\text{Area} = \tfrac12 bc\sin A = \tfrac12(7)(9)(0.66913061) = 21.07761410,$$

and by Heron's formula with $s = (a+b+c)/2 = 11.01511824$:

$$\sqrt{s(s-a)(s-b)(s-c)} = 21.07761410.$$

The two agree to the printed digits. They are not independent facts: Heron's
formula can be *derived* from the law of cosines, so their agreement tests the
arithmetic, not the physics.

---

## ★★5 — True dip from two apparent dips

**The relation**, derived in the lesson from
$\tan\alpha = \tan\delta\,|\sin(\varphi-\theta)|$ with $\varphi = 0$ for the
north–south section and $\varphi = 90°$ for the east–west one:

$$\tan\delta = \sqrt{\tan^{2}\alpha_N + \tan^{2}\alpha_E}, \qquad
\theta = \operatorname{atan2}(\tan\alpha_N,\ \tan\alpha_E).$$

**(a)** $\tan 25° = 0.46630766$, $\tan 40° = 0.83909963$.

$$\tan\delta = \sqrt{0.21744283 + 0.70408824} = \sqrt{0.92153107} = 0.95996410,$$

$$\boxed{\delta = 43.8298°}, \qquad
\theta = \operatorname{atan2}(0.46630766, 0.83909963) = \boxed{29.0620°}.$$

**Check that the answer is sensible.** The true dip must be at least as large as
each apparent dip: $43.83° > 40° > 25°$ ✓. The dip azimuth must lie between the
two section azimuths when both apparent dips are positive in the same sense —
here between $0°$ (north) and $90°$ (east), and $29.06°$ is ✓. Had the answer
come out at $250°$, one of the two checks would have flagged it.

**(b)** Strike is perpendicular to the dip azimuth:
$\theta + 90° = 119.0620°$. Reporting it as $119.06°$ or $299.06°$ is equally
correct, because a strike measures the *line* of intersection of a bedding plane
with the horizontal, and a line has no arrowhead. The dip azimuth, by contrast, is
a vector: it points downhill, and reversing it describes a different plane.

**(c)** The alternative solution is the mirror image: dip $43.8298°$ towards
$209.0620°$, obtained by reversing both components of the horizontal dip
direction. Both planes produce the same two apparent dips because the relation
uses $|\sin\theta|$ and $|\cos\theta|$. Distinguishing evidence in the field:

- which direction the beds young or get deeper, from a nearby outcrop or borehole;
- a third apparent dip measured in a section at, say, $45°$ azimuth, which breaks
  the symmetry at once;
- regional strike from a geological map, which is often known independently.

**(d)** If $\alpha_N = 0$ the bed strikes due north–south, so $\theta$ is $90°$ or
$270°$ and $\tan\alpha_N/\tan\alpha_E = 0$. The formula
$\theta = \arctan(\tan\alpha_N/\tan\alpha_E)$ divides by $\tan\alpha_E$ in the
equivalent rearrangement, and more importantly it cannot distinguish $0$ from
$180°$ in any case. Use `atan2`, which is defined at zero arguments and preserves
the quadrant information carried by the signs. Even then, $90°$ and $270°$ remain
indistinguishable from the two sections alone, so the ambiguity of (c) is not
removed by changing the function — only the numerical failure is.

---

## ★★6 — Snell's law and the critical angle

**(a)** The critical angle is where the transmitted ray becomes horizontal,
$i_2 = 90°$:

$$\sin i_c = \frac{v_1}{v_2} = \frac{2.0}{6.0} = \frac13,
\qquad \boxed{i_c = 19.471221°}.$$

**(b)** The ray parameter is conserved:

$$p = \frac{\sin 20°}{2.0} = \frac{0.34202014}{2.0} = 0.17101007\ \text{s/km}.$$

The transmitted angle would satisfy $\sin i_2 = p\,v_2 = 0.17101007 \times 6.0
= 1.02606043$. Since $|\sin i_2| > 1$ has no solution, **no transmitted ray
exists**: $20° > i_c$, so the ray is totally reflected. In a numerical
implementation the quantity $pv_2$ exceeds 1 and the `arcsin` call must be
guarded, or you will get a domain error or a `nan`.

**(c)** The maximum useful offset follows from the geometry of the critically
refracted head wave. At incidence exactly $i_c$ the refracted ray travels along
the interface at speed $v_2$, and the head wave it sheds is the first arrival
beyond some offset. For a layer of thickness $h$, the cross-over distance (where
the head wave overtakes the direct wave) is the familiar
$x \approx 2h\sqrt{(v_2+v_1)/(v_2-v_1)}$; here $v_2/v_1 = 3$, so the head wave
only becomes the first arrival at a few times the layer thickness. Beyond that,
the ray parameter is essentially pinned at $p = 1/v_2 = 0.166667$ s/km, so
additional offset adds almost no new information about $v_2$ — the slope of the
travel-time curve has saturated. That saturation, not a detector limit, is what
sets the maximum useful offset of a refraction spread designed to measure $v_2$.

> Note on the cross-over formula: it is quoted here to explain the physics, and
> its derivation belongs to
> [06-seismology](../../../06-seismology/README.md). Check the form against that
> module before using it in a calculation; the version here assumes a
> two-layer flat model with the source at the surface.

---

## ★★7 — The small-angle approximation

**(a)** At $x = 4° = 0.06981317$ rad:

$$x - \sin x = 0.06981317 - 0.06975647 = 5.670\times10^{-5},$$

relative error $= 5.670\times10^{-5}/0.06975647 = \boxed{8.128\times10^{-4}}$,
i.e. 0.081 percent. The leading error term $x^{3}/6$ accounts for
$5.671\times10^{-5}$ of it, so the cubic term is essentially the whole error at
this angle.

**(b)** Solve $(x - \sin x)/\sin x = 0.01$ numerically. Bisection on
$x \in [0.01, 0.5]$ converges in a few dozen iterations to

$$x = 0.244096696\ \text{rad} = \boxed{13.9857°}.$$

**How to check it.** Evaluate the relative error at your answer and at the two
neighbouring bisection endpoints: it must bracket 1 percent. Better still, use the
cubic approximation: setting $x^{3}/6 \div \sin x \approx x^{2}/6 = 0.01$ gives
$x \approx \sqrt{0.06} = 0.244949$ rad $= 14.03°$, within 0.05° of the exact
answer. Two independent routes agreeing is the check.

**(c)** No. A 1 percent *error bound* is not the same as a 1 percent *accuracy*.
The approximation is one-sided — $\sin x$ is always smaller than $x$ for positive
$x$ — so it biases amplitudes downward rather than scattering them randomly, and
a systematic bias of 1 percent is harder to detect and harder to remove than
random noise of the same size. Use the two-term expansion
$\sin x \approx x - x^{3}/6$, which in (a) would reduce the error to the
$x^{5}/120$ term, below $10^{-8}$ relative at $4°$.

---

## ★★8 — Survey triangulation

**Given** sides 1200 m and 900 m, included angle $65°$.

**(a)** Law of cosines:

$$d^{2} = 1200^{2} + 900^{2} - 2(1200)(900)\cos 65°
= 1\,440\,000 + 810\,000 - 2\,160\,000(0.42261826)
= 2\,250\,000 - 912\,855.44 = 1\,337\,144.56,$$

$$d = \boxed{1156.349668\ \text{m}}.$$

**(b)** The remaining angles, opposite the 900 m and 1200 m sides respectively:

$$70.13897366° \quad\text{and}\quad 44.86102634° .$$

Check: $65 + 70.13897366 + 44.86102634 = 180.00000000$ ✓.

**(c)** For $d^{2} = a^{2}+b^{2}-2ab\cos C$ with $a = 1200$, $b = 900$,
$C = 65°$, differentiate:

$$\frac{\partial d}{\partial a} = \frac{a - b\cos C}{d}
= \frac{1200 - 900(0.42261826)}{1156.349668} = \frac{819.643566}{1156.349668}
= 0.708820,$$

$$\frac{\partial d}{\partial b} = \frac{b - a\cos C}{d}
= \frac{900 - 1200(0.42261826)}{1156.349668} = \frac{392.858088}{1156.349668}
= 0.339740,$$

$$\frac{\partial d}{\partial C} = \frac{ab\sin C}{d}
= \frac{1200 \times 900 \times 0.90630779}{1156.349668} = 846.4675
\ \text{m per radian}.$$

Combine in quadrature, with $\sigma_C = 0.05° = 8.72665\times10^{-4}$ rad:

- from $a$: $0.708820 \times 0.5 = 0.3544$ m
- from $b$: $0.339740 \times 0.5 = 0.1699$ m
- from $C$: $846.4675 \times 8.72665\times10^{-4} = 0.7387$ m

$$\sigma_d = \sqrt{0.3544^{2} + 0.1699^{2} + 0.7387^{2}} = \boxed{0.8367\ \text{m}}.$$

So $d = 1156.35 \pm 0.84$ m, and the **angle measurement dominates**,
contributing 0.7387 m of the 0.8367 m total. That is typical of triangulation: a
small angular error times a long lever arm beats a small length error, which is
exactly why theodolites are precise to arcseconds while tapes are precise to
millimetres. The same structure appears in the dominant term of any indirect
measurement — differentiate first, then decide where to spend money.

---

## ★★★9 — Verifying the apparent-dip relation

**(a)–(b)** The construction: take a plane with unit upward normal
$\mathbf{n} = (\sin\delta\sin\theta,\ \sin\delta\cos\theta,\ \cos\delta)$ in
(east, north, up) coordinates. A vertical section along azimuth $\varphi$ has
horizontal direction
$\mathbf{h} = (\sin\varphi,\ \cos\varphi,\ 0)$ and contains the vertical
$\mathbf{e}_z$. The intersection line has direction
$\mathbf{L} = \mathbf{h} - (\mathbf{h}\cdot\mathbf{n})\,\mathbf{n}$, and the
apparent dip is the angle between $\mathbf{L}$ and the horizontal:
$\alpha = \arcsin(|\mathbf{L}\cdot\mathbf{e}_z| / |\mathbf{L}|)$. This route uses
no trigonometry of the "relation" being tested, which is what makes it a genuine
check.

Sweeping the stated grid gives a worst absolute discrepancy of order
$10^{-14}$ degrees — round-off level — for every combination tested, including
$\theta = 130°$ and $\theta = 275°$, where the *magnitudes* of the apparent dips
are all that is measurable. **The formula is correct.**

**(c)** The systematic pattern to report: the residual grows slightly with
$\delta$ and with $|\varphi - \theta|$, and it is largest for the largest angles
in the sweep. That is a property of the `arcsin` and `arctan` round-off, not of
the relation, and it is the same one-sided amplification that
[01-03-03](../03-inverse-trig.md) quantifies: the derivative of $\arcsin$ grows
without bound as its argument approaches 1, which is exactly the
$\delta = 60°$, $\varphi = \theta$ case.

**(d)** What such a verification does **not** do:

- It cannot detect an error in the *derivation* if the same error is present in
  both routes. Here it is not, because the geometric route uses no trigonometric
  identity from the lesson — so this is the strongest form of numerical check
  available.
- It cannot distinguish a formula that is right from one that is right "almost
  everywhere" — for instance, a version that is wrong only at exactly
  $\varphi = \theta$ would be missed by any random sweep that never samples that
  point. Sweeps should always include the degenerate cases $\varphi = \theta$ and
  $\varphi = \theta \pm 90°$, which is why the grid above includes $\varphi = 90°$
  with $\theta = 90°$ in the neighbouring tests.
- It says nothing about the quadrant ambiguity, which no amount of arithmetic can
  resolve.

---

## ★★★10 — Error propagation into dip and azimuth

**(a)** With $\delta$ from
$\tan\delta = \sqrt{\tan^{2}\alpha_N + \tan^{2}\alpha_E}$ and
$\theta = \operatorname{atan2}(\tan\alpha_N, \tan\alpha_E)$, differentiate.
Writing $u = \tan\alpha_N$, $v = \tan\alpha_E$ and
$T = \tan\delta = \sqrt{u^{2}+v^{2}}$:

$$\frac{\partial T}{\partial u} = \frac{u}{T}, \qquad
\frac{\partial T}{\partial v} = \frac{v}{T}, \qquad
\frac{\partial \delta}{\partial u} = \frac{u}{T(1+T^{2})}, \qquad
\frac{\partial \delta}{\partial v} = \frac{v}{T(1+T^{2})}.$$

Then convert the derivative with respect to $\alpha$ using
$\partial u/\partial\alpha_N = \sec^{2}\alpha_N$:

$$\frac{\partial \delta}{\partial\alpha_N}
= \frac{\tan\alpha_N \, \sec^{2}\alpha_N}{T(1+T^{2})}.$$

With $\alpha_N = 25°$, $\alpha_E = 40°$: $u = 0.46630766$,
$v = 0.83909963$, $T = 0.95996410$, $\sec^{2}25° = 1.2174$,
$\sec^{2}40° = 1.7041$. So

$$\frac{\partial\delta}{\partial\alpha_N} = 0.3078, \qquad
\frac{\partial\delta}{\partial\alpha_E} = 0.7752 \quad (\text{dimensionless}),$$

and with $\sigma = 0.5°$ in each

$$\sigma_\delta = \sqrt{(0.3078)^{2} + (0.7752)^{2}} \times 0.5°
= 0.8341 \times 0.5° = \boxed{0.417°}.$$

For the azimuth, $\theta = \arctan(u/v)$ so

$$\frac{\partial\theta}{\partial u} = \frac{v}{u^{2}+v^{2}}, \qquad
\frac{\partial\theta}{\partial v} = -\frac{u}{u^{2}+v^{2}},$$

giving $\partial\theta/\partial\alpha_N = 1.1085$ and
$\partial\theta/\partial\alpha_E = -0.8623$. Hence

$$\sigma_\theta = \sqrt{(1.1085)^{2} + (0.8623)^{2}} \times 0.5°
= 1.4044 \times 0.5° = \boxed{0.702°}.$$

Note that the azimuth is *less* well determined than the dip: 0.70° against
0.42°. The two components of a direction are not equally sensitive to the inputs,
which is why an error budget must be done per quantity rather than per
measurement.

**(b)** A Monte Carlo with $2\times10^{5}$ samples drawn from
$\mathcal{N}(25°, 0.5°)$ and $\mathcal{N}(40°, 0.5°)$ gives standard deviations of
$0.417°$ for the dip and $0.703°$ for the azimuth — within about 0.1 percent of
the linear estimates. (The exact figures depend on the random seed and on the
number of draws; report the seed and the count when you write this up, because a
Monte Carlo result without a stated sample size is not reproducible, and one
without a seed is not reproducible either.)

**(c)** The two agree to within the Monte Carlo noise, which is expected: the
partial derivatives are smooth and the input uncertainties are small enough that
second-order terms are negligible. If they had disagreed, the cause would be
nonlinearity — the transformed distribution is skewed — and the Monte Carlo
answer would be the one to report, because it makes no linearisation assumption.
Reporting both, with the agreement noted, is the honest way to write this up.

**(d)** The worst conditioning occurs when $u$ and $v$ are both small in the
denominator of $\partial\theta/\partial u$ — that is, when $\alpha_N$ and
$\alpha_E$ are both small. Then small absolute errors in either apparent dip swing
the azimuth widely: for a nearly horizontal bed the dip *direction* is barely
determined, even though the dip *magnitude* is well determined. More precisely,
the relative uncertainty in $\theta$ behaves like $\sigma_\alpha/\sqrt{u^{2}+v^{2}}$,
which diverges as both apparent dips vanish. Geometrically, this is the statement
that a nearly flat plane has no well-defined steepest-descent direction: the
gradient vector is small and its direction is dominated by noise. The same
geometric fact appears as the ill-conditioning of plane-fitting in
[01-04-02 Analytic Geometry: Lines, Planes and Distances](../../04-geometry-and-coordinates/02-analytic-geometry.md).
