# Solutions — 01-04-04 Geographic Coordinates, Datums and Map Projections

> **Read this after attempting the exercises, not before.**
>
> WGS84 throughout, with $a = 6378.137$ km and $1/f = 298.257223563$. All values
> were computed by the numerical methods described, not read from a table.

---

## ★1 — The ellipsoid from two definitions

**(a)** $f = 1/298.257223563 = 3.3528106647\times10^{-3}$.

**(b)** $e^{2} = f(2-f) = 3.3528106647\times10^{-3} \times 1.9966471893
= 6.694379990\times10^{-3}$.

It is worth seeing *why* $e^{2} = f(2-f)$. With $b = a(1-f)$,

$$e^{2} = \frac{a^{2}-b^{2}}{a^{2}}
= \frac{a^{2} - a^{2}(1-f)^{2}}{a^{2}} = 1-(1-f)^{2} = 2f - f^{2} = f(2-f) .$$

**(c)** $b = a(1-f) = 6378.137 \times 0.9966471893 = 6356.752314$ km.

**(d)** $e'^{2} = (a^{2}-b^{2})/b^{2}$. Since $a^{2}-b^{2} = e^{2}a^{2}$ and
$b^{2} = a^{2}(1-f)^{2}$,

$$e'^{2} = \frac{e^{2}}{(1-f)^{2}}
= \frac{6.694379990\times10^{-3}}{0.9933056200} = 6.739497\times10^{-3} .$$

**(e)** $a - b = 6378.137 - 6356.752314 = 21.384686$ km.

**Definitions versus derived quantities.** $a$ and $1/f$ are **definitions**: they
are exact by the definition of WGS84, and no measurement uncertainty attaches to
them. $f$, $e^{2}$, $b$, $e'^{2}$ and $a-b$ are all **derived** from them by exact
algebra, so they are also exact — the only uncertainty in a printed value is the
rounding in the print. **The uncertainty in a geodetic result comes from the datum
realisation and from the geoid, not from the ellipsoid parameters.**

---

## ★2 — Meridian arcs

**(a)**

$$M(\varphi) = \frac{a(1-e^{2})}{\left(1-e^{2}\sin^{2}\varphi\right)^{3/2}} .$$

It is largest at the pole because the denominator is smallest there: at
$\varphi = 90°$, $\sin^{2}\varphi = 1$ and the denominator $(1-e^{2})^{3/2}$ is at
its minimum, so $M$ is at its maximum. Physically, the pole is the flattest part of
the ellipsoid in the north–south direction, and a flatter curve has a larger radius
of curvature.

**(b)**

- At the equator: $M(0) = a(1-e^{2}) = a b^{2}/a^{2} = b^{2}/a = 6356.752314^{2} / 6378.137 =
  \boxed{6335.439327}$ km. Note it equals $b^{2}/a$, which is a useful exact identity.
- At the pole: $M(90°) = a(1-e^{2})/(1-e^{2})^{3/2} = a/\sqrt{1-e^{2}} = a^{2}/b =
  6378.137^{2}/6356.752314 = \boxed{6399.593626}$ km.

**Both are exact algebraic identities**, which makes them ideal unit tests: they must
hold to round-off, and they will catch a misplaced exponent in the formula.

**(c)** The length of a degree is $M(\varphi) \times \pi/180$:

| latitude | $M$ (km) | one degree (km) |
|---|---|---|
| $0°$ | 6335.439327 | $\boxed{110.574276}$ |
| $45°$ | 6367.381816 | $\boxed{111.131777}$ |
| $90°$ | 6399.593626 | $\boxed{111.693980}$ |

**(d)** Integrating $M$ from the equator to the pole gives the quarter meridian
$\boxed{10001.966\ \text{km}}$. **Its historical significance:** the metre was
defined as one ten-millionth of this distance, so the definition implies a unit of

$$\frac{10001966\ \text{m}}{10^{7}} = 1000.1966\ \text{m},$$

about 0.20 m longer than the metre as now defined. **State the claim precisely:** it
is a statement about the *meridian definition* under the modern ellipsoid, not about
the accuracy of the 18th-century measurement, which was limited by the survey's own
errors and by the unknown shape of the geoid along the arc.

---

## ★3 — Longitude

**(a)** A degree of longitude at latitude $\varphi$ is
$(2\pi a/360)\cos\varphi = 111.3195\cos\varphi$ km:

| latitude | one degree of longitude |
|---|---|
| $0°$ | 111.32 km |
| $30°$ | 96.41 km |
| $45°$ | 78.71 km |
| $60°$ | 55.66 km |
| $80°$ | 19.33 km |

**(b)** At $60°$ the factor is $111.3195/55.66 = 2.0000$, and
$1/\cos 60° = 2$ exactly ✓. The coincidence of a factor of exactly two at $60°$ is
worth remembering as a mental anchor.

**(c)** $2°$ of longitude at $60°$N is $2 \times 55.66 = 111.32$ km. A naive
calculation using 111 km per degree gives 222 km — **exactly a factor of two too
large.** This is the most common regional-survey error in this module, and it is
invisible unless the survey is east–west: a $2°$ north–south survey would give 222
km and be right.

---

## ★★4 — Mercator distortion

**(a)** Spherical Mercator:

$$x = R\lambda, \qquad y = R\ln\tan\!\left(\frac{\pi}{4}+\frac{\varphi}{2}\right).$$

North–south scale: $\dfrac{dy}{d\varphi} = R\sec\varphi$ against a true distance of
$R\,d\varphi$, so $k = \sec\varphi$. East–west scale:
$\dfrac{dx}{d\lambda} = R$ against a true distance of $R\cos\varphi\,d\lambda$, so
$k = 1/\cos\varphi = \sec\varphi$ as well. **The two directional scales are equal, in
every direction — that is what conformal means**, and its price is the area factor
$k^{2} = \sec^{2}\varphi$.

**(b)**

| latitude | $k = \sec\varphi$ | area inflation $k^{2}$ |
|---|---|---|
| $30°$ | 1.154701 | 1.3333 |
| $45°$ | 1.414214 | 2.0000 |
| $60°$ | 2.000000 | 4.0000 |
| $80°$ | 5.758770 | 33.1634 |

**(c)** $\sec^{2}\varphi = 10$ gives $\cos\varphi = 1/\sqrt{10} = 0.31622777$, so
$\varphi = 71.565051° \approx \boxed{71.6°}$. Poleward of about $72°$, a Mercator map
inflates area by more than a factor of 10.

**(d)** Mercator is suitable **for navigation and for any application where a
constant bearing should be a straight line, and for local survey work at low
latitude**. It is unsuitable **for area statistics, for comparison of regions at
different latitudes, and for any global map whose purpose is spatial comparison**,
because the area distortion reaches a factor of 4 at $60°$ and 33 at $80°$.

---

## ★★5 — UTM

**(a)** Zone number $= \lfloor(\lambda+180°)/6°\rfloor + 1$, and the zone's central
meridian is $-180° + 6°(z-1) + 3°$:

| longitude | zone | central meridian |
|---|---|---|
| $10°$E | 32 | $9°$E |
| $25°$E | 35 | $27°$E |
| $74°$W ($-74°$) | 18 | $75°$W |
| $0.1°$W ($-0.1°$) | 30 | $3°$W |

**Check by hand.** Zone 32 spans $6°$E to $12°$E and its central meridian is
$9°$E ✓ ($10°$E lies inside). Zone 18 spans $78°$W to $72°$W with a central meridian
at $75°$W ✓ ($74°$W lies inside, 1° east of the centre).

**(b)** The four standard parameters and their purposes:

| parameter | value | purpose |
|---|---|---|
| zone width | $6°$ of longitude, 60 zones | keeps the worst distortion bounded by limiting distance from the central meridian |
| central scale factor $k_0$ | 0.9996 | balances the sign of the scale error across the zone |
| false easting | 500 000 m | makes all eastings positive within a zone, so no negative coordinates |
| false northing | 0 m (N), 10 000 000 m (S) | makes all northings positive in both hemispheres |

**Confirm these against the current official specification of the datum you use
before quoting them.** They are the standard values, but standards are revised and
national grids sometimes differ.

**(c)** A true 10.000 km line is drawn as
$10.000 \times 1.002342 = \boxed{10.02342}$ km, i.e. **23.42 m longer**.

**(d)** With $k_0 = 1$ the scale factor would be 1 on the central meridian and
greater than 1 everywhere else, reaching about 1.00137 at the zone edge on the
equator — an error of one sign only, and larger at its worst. Reducing $k_0$ to
0.9996 makes the map *smaller* than the ground at the central meridian
($-0.04$ percent) and *larger* than the ground at the zone edge ($+0.097$ percent at
the equator), so the worst error in magnitude falls from about $0.14$ percent to
about $0.10$ percent. **The purpose is to centre the error distribution on zero**, so
that distortions of opposite sign partly cancel in a large survey rather than
accumulating.

---

## ★★6 — The mastery-checkpoint distortion budget

**(a)** $10.000 \times 1.002342 = 10.023420$ km, so the map overstates a 10 km
spacing by $\boxed{23.42\ \text{m}}$.

**(b)** Areas scale as the square of the linear scale factor:

$$k^{2} = 1.002342^{2} = 1.004689,$$

so a mapped $100 \times 100$ km area is too large by $0.4689$ percent, i.e. by
$\boxed{46.9\ \text{km}^{2}}$ out of $10\,000$ km². **Note the doubling: a 0.23
percent linear error becomes a 0.47 percent area error.** Area quantities are always
twice as sensitive as linear ones, and a 1 percent area budget therefore allows only
a 0.5 percent linear error.

**(c)** Strain rate is computed by *differencing* positions, so what matters is the
**gradient** of the scale factor, not its value. Two points 10 km apart near the
same location have nearly equal scale factors, and their difference in scale is tiny
compared with the common factor — so a uniform scale error largely cancels in the
difference. But the scale factor varies across a zone (from 0.9996 to 1.00097 over
3° of longitude in the spherical model), so over a whole zone the difference in
scale between two distant points is of order $10^{-3}$, which is 1000 ppm — far
larger than a crustal strain rate of tens of nanostrain per year measured over a
region. **Crustal deformation studies must therefore work in geodetic coordinates or
in a locally correct projection, not in a national grid**, and the correction cannot
be a single number.

**(d)** The two angles behave differently, and the reason is instructive.

**The dip azimuth is exactly preserved.** The projection is conformal, so it
preserves angles in the horizontal plane, and the dip azimuth is an angle between
horizontal directions. A common scale factor in the two horizontal directions does
not change it, at any dip.

**The dip magnitude is not preserved**, because the projection scales the
horizontal coordinates and leaves the elevations alone. A dip is an angle measured
*against the vertical*, so the ratio of horizontal to vertical distance changes:

$$\tan\delta_{\text{map}} = \frac{\tan\delta}{k}
\qquad\Longrightarrow\qquad
\delta_{\text{map}} = \arctan\!\left(\frac{\tan\delta}{k}\right).$$

| true dip | mapped dip | change |
|---|---|---|
| $6.2172°$ | $6.202787°$ | $-0.0144°$ |
| $15°$ | $14.966526°$ | $-0.0335°$ |
| $30°$ | $29.941997°$ | $-0.0580°$ |
| $45°$ | $44.932985°$ | $-0.0670°$ |

At $k = 1.002342$ the change at $30°$ is $0.058°$ — **about five times the
$\pm0.0114°$ dip uncertainty of a 1 km survey with 0.1 m vertical accuracy**
(exercise ★★8 of [01-04-02](./02-analytic-geometry-solutions.md)). So for an attitude
budget at the $0.01°$ level, the projection scale must be corrected before computing
the dip, or the computation must be done in geodetic coordinates.

**The general statement worth carrying away:** a conformal projection preserves
*map-plane* angles, which is why azimuths and horizontal angles survive it — but any
angle that involves the vertical, including dips, slopes and take-off angles, is
distorted whenever the map's scale factor differs from 1.

---

## ★★7 — Sphere or ellipsoid?

The procedure: convert the difference into the quantity you interpret, and compare
with the measurement uncertainty.

**(a)** A 2 km baseline with 0.05 m positions. The relevant ellipsoidal correction is
the ratio of the local radius of curvature to the mean sphere: at mid latitudes
$N \approx 6388$ km against $6371$ km, a difference of 0.27 percent, i.e. **5.4 m
over 2 km**. That is 100 times the 0.05 m positioning accuracy, so **the sphere is
not adequate**; use an ellipsoidal or a local projection with a stated scale factor.
The naive "2 km is short, so the sphere is fine" reasoning is wrong, and it is wrong
by two orders of magnitude.

**(b)** 9000 km with 0.2 s timing. At 8 km/s a 0.2 s uncertainty corresponds to
1.6 km. The ellipsoidal correction over a 9000 km path is of order $0.2$ percent,
i.e. **18 km, or about 2.3 s**. That exceeds the timing uncertainty by an order of
magnitude, so **the ellipsoid is required**.

**(c)** A $50 \times 50$ km area to 0.1 percent. Area scales as the square of the
linear correction: 0.27 percent linear gives **0.54 percent in area** — five times
the target. So even at 50 km the sphere is **not** adequate for an area to 0.1
percent; use an equal-area projection, which is the correct tool for area work.

**(d)** A 20 mm/yr velocity over a 500 m baseline. The linear correction at 0.27
percent of 500 m is 1.35 m — huge compared with 20 mm/yr, **but** a velocity is a
*difference* of positions of the same station at different times, and the scale
correction is the same at both epochs, so it cancels almost entirely. What remains is
the change in scale factor between the two stations (0.01 m over 500 m at most) and
the differential motion. So **the sphere is adequate for the velocity**, while being
inadequate for the position. **The lesson: the same geometric error is significant
or not depending on which quantity you compute from it**, and the decision must be
made per quantity, not per survey.

---

## ★★8 — False eastings and northings

**(a)** Without it, a zone's central meridian would have eastings of zero, and points
west of it would have negative eastings. Negative coordinates are a nuisance in
databases (sorting, string formatting, unsigned storage) and an easy source of sign
errors in users' arithmetic. Setting the central meridian to 500 000 m makes **all**
eastings inside a zone lie between roughly 100 km and 900 km. The cost is that the
easting is not a distance — one must subtract 500 000 m to recover the offset from
the central meridian, as in **(c)**.

**(b)** Southern-hemisphere UTM would otherwise have negative northings (zero at the
equator, decreasing southward). Adding 10 000 000 m makes them positive. **The
consequence of omitting it in a mixed dataset is a 10 000 km offset**: points
straddling the equator differ by 10 000 km in northing, so a map appears torn or a
distance calculation is absurd by a factor of thousands. The signature is a set of
noisy northings for one hemisphere and clean ones for the other, which is why the
hemisphere must be recorded alongside the coordinates — a UTM coordinate is
incomplete without its zone *and* its hemisphere.

**(c)** Offset from the central meridian: $612\,345 - 500\,000 = 112\,345$ m
projected. Dividing by the local scale factor ($\approx 1.0023$ at that offset)
gives a true ground distance of about

$$\frac{112345}{1.0023} \approx \boxed{112\,087\ \text{m}},$$

i.e. **about 112.1 km**, versus 112.345 km if you read the easting as a distance — a
difference of 258 m, or 0.23 percent.

**Why it is only an estimate:** the scale factor varies along the line from the
central meridian to the point, so the correct ground distance requires an integral of
$1/k$ along the path, not a single division. The projection also blends the
meridional and parallel distances, so "distance from the central meridian" is not
exactly the easting minus the false easting even before scaling. **Both effects are of
the same order (0.2 percent), which is why a single-number correction is adequate for
reconnaissance and inadequate for a survey.**

---

## ★★★9 — Mapping a projection's distortion

**(a)–(c)** Implementing the spherical transverse Mercator
$x = k_0R\operatorname{atanh}(\cos\varphi\sin\lambda)$,
$y = k_0R\operatorname{atan2}(\tan\varphi,\cos\lambda)$ with $k_0 = 0.9996$,
$R = 6371$ km, and measuring the scale factor by central differences along the
meridian and along the parallel, gives over a full zone
($\lambda = -3° \ldots +3°$):

| latitude | $k$ at $\lambda = 0°$ | $\lambda = 1°$ | $\lambda = 2°$ | $\lambda = 3°$ |
|---|---|---|---|---|
| $0°$ | 0.999600000 | 0.999752267 | 1.000209300 | 1.000971797 |
| $30°$ | 0.999600000 | 0.999714194 | 1.000056871 | 1.000628318 |
| $60°$ | 0.999600000 | 0.999638060 | 0.999752221 | 0.999942420 |
| $80°$ | 0.999600000 | 0.999604590 | 0.999618356 | 0.999641282 |

- **Minimum $k$ over the zone: 0.999600000**, attained everywhere on the central
  meridian.
- **Maximum $k$ over the zone: 1.000971797**, attained at the equator at the zone
  edge ($\lambda = 3°$).
- So $\max\lvert k-1\rvert = 9.718\times10^{-4}$, i.e. **about 1 part in 1029**,
  and $\max\lvert k - k_0\rvert = 1.372\times10^{-3}$ at the same place.

**(b) Conformality.** Scanning the whole zone on a $0.25°$ grid and comparing the
meridional and parallel scale factors, the two agree to about $10^{-8}$ in relative
terms — the limit set by the finite-difference step, not by the projection. **The
agreement confirms that the projection is conformal**: one number describes the local
distortion in every direction, so the shape of a small region is preserved. **A
projection that is not conformal would show a directional dependence here, and that
dependence is exactly what its users must account for.**

**(d)** The value of $k_0$ was chosen to balance the error: the map is too small by
0.04 percent on the central meridian and too large by 0.097 percent at the zone edge
on the equator. The maximum departure from unity is therefore about **1 part in
1000**, which is the bound the choice of 0.9996 from 1 was intended to achieve: with
$k_0 = 1$ the departure at the zone edge would be 0.137 percent (1 part in 730) and
of a single sign.

**(e)** **Both the numbers above and the whole calculation are for the *spherical*
transverse Mercator.** Real UTM is defined on the ellipsoid, and it differs in two
ways:

1. **The algebra is longer.** The ellipsoidal transverse Mercator uses a
   meridional-arc series and a conformal latitude, and the scale factor acquires
   additional terms in the flattening. The structure — exact $k_0$ on the central
   meridian, growing distortion away from it, conformality everywhere — is
   unchanged.
2. **The numbers differ slightly**, by terms of order $e^{2} \approx 0.0067$ times
   the departures shown, i.e. in the fifth significant figure of $k$. Since the
   departures themselves are of order $10^{-3}$, the ellipsoidal correction to the
   distortion is of order $10^{-5}$ — small, but the *scale factor printed by a
   projection library* will differ from these values in that digit, and quoting these
   as "the UTM scale factor" would be wrong.

---

## ★★★10 — The cost of numerical integration

**(a)** Simpson's rule on $M(\varphi')$ from $0$ to $\pi/2$, against a reference
value computed with $2\times10^{6}$ intervals
($10001.965729312107$ km):

| intervals $n$ | quarter meridian (km) | error |
|---|---|---|
| 2 | 10001.965729 | $-35.25$ m |
| 4 | 10001.965729 | $-1.3\times10^{-4}$ m ($-0.13$ mm) |
| 6 | 10001.965729 | $+6.1\times10^{-7}$ m ($+0.6$ µm) |
| 10 | 10001.965729 | $+6.1\times10^{-7}$ m |
| 100 | 10001.965729 | $+6.1\times10^{-7}$ m |
| 1000 | 10001.965729 | $+6.3\times10^{-7}$ m |
| 100000 | 10001.965729 | $+6.2\times10^{-7}$ m |

**(b)** **There is no measurable convergence exponent beyond $n = 6$.** The error
falls from 35 m at $n = 2$ to 0.6 µm at $n = 6$ — a factor of $6\times10^{7}$ — and
then stops falling, because it has reached the round-off floor of double precision on
a quantity of order $10^{7}$ m (a relative level of $\sim10^{-13}$, accumulated over
the summation). **Report the observed behaviour honestly rather than fitting a
slope to noise:** the correct statement is "Simpson's rule converges so fast on this
smooth integrand that it reaches round-off at six intervals, so the order cannot be
measured."

**(c)** Sub-millimetre accuracy requires only $n = 6$ intervals. That is trivially
practical, and it means the "how many intervals" question is the *wrong* question
here.

**(d)** Coarser steps than a degree are where the trouble lies. The integrand
$M(\varphi)$ varies by about 1 percent over the quarter meridian and is smooth, but
Simpson's rule on $n = 2$ — steps of $45°$ — misses that variation and is 35 m wrong.
The pattern is a single picture: the error is largest where the integrand's curvature
is greatest, which for $M(\varphi)$ is near the equator (where the third derivative is
largest), and it falls by five orders of magnitude as soon as the step resolves the
variation.

**(e)** In production, **use a fixed quadrature of a few hundred intervals** — it is
exact to round-off, costs nothing, and removes an entire class of error. Do not use a
series expansion unless you have verified its truncation error, because the series
coefficients are easy to transcribe wrongly and their error is silent. **And always
compare against a case you know**: the quarter meridian has no independent closed
form, but the *pole* and *equator* identities of ★2(b) — $M(0) = b^{2}/a$ and
$M(90°) = a^{2}/b$ — do, and they will catch a formula error in the integrand
immediately.
