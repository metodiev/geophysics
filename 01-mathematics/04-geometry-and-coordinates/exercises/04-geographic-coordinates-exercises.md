# Exercises — 01-04-04 Geographic Coordinates, Datums and Map Projections

Attempt these **closed-book**. Solutions are in
[`04-geographic-coordinates-solutions.md`](./04-geographic-coordinates-solutions.md).
Difficulty: ★ foundational · ★★ applied · ★★★ research-oriented.

WGS84 has $a = 6378.137$ km and $1/f = 298.257223563$; both are exact by
definition. Give every answer with the reference surface you used.

---

## ★ Foundational

**★1.** Derive, showing each step:

(a) the flattening $f$;
(b) the first eccentricity squared $e^{2} = f(2-f)$;
(c) the semi-minor axis $b = a(1-f)$;
(d) the second eccentricity squared $e'^{2} = (a^{2}-b^{2})/b^{2}$;
(e) the polar flattening $a - b$.

Then state which of these are definitions and which are derived.

---

**★2.** Meridian arcs.

(a) State the radius of curvature in the meridian $M(\varphi)$ and explain why it
is largest at the pole.
(b) Evaluate $M(\varphi)$ at the equator and at the pole, and explain the two
values in terms of $a$ and $b$.
(c) Compute the length of one degree of latitude at $0°$, $45°$ and $90°$.
(d) State the length of the quarter meridian, and the historical significance of
that number.

---

**★3.** Longitude.

(a) Compute the length of one degree of longitude at $0°$, $30°$, $45°$, $60°$ and
$80°$ using the equatorial radius.
(b) State the factor by which a degree of longitude is shorter at $60°$ than at the
equator, and check it against the cosine.
(c) A regional survey spans $2°$ of longitude at $60°$N. How wide is it in
kilometres, and what would a naive calculation using 111 km per degree give?

---

## ★★ Applied

**★★4.** Mercator distortion.

(a) State the projection equations and derive the scale factor.
(b) Tabulate the scale factor and the area inflation at $30°$, $45°$, $60°$ and
$80°$.
(c) At what latitude does the area inflation reach a factor of 10?
(d) State, in one sentence, for what purpose Mercator is suitable and for what it
is not.

---

**★★5.** UTM.

(a) For longitudes $10°$E, $25°$E, $-74°$ and $-0.1°$, give the UTM zone number
and the central meridian of that zone.
(b) State the four standard UTM parameters and explain the purpose of each.
(c) On the spherical transverse Mercator, the scale factor at $45°$N and $6°$ from
the central meridian is $1.002342$. By how much is a true 10.000 km line drawn
longer on the map?
(d) Explain why $k_0 = 0.9996$ rather than 1.

---

**★★6.** *(Module mastery checkpoint, part (c).)* A reflector is mapped on a UTM
grid at $45°$N, $6°$ from the zone's central meridian, where the projection scale
factor is $1.002342$.

(a) A 10.000 km grid spacing is drawn as how many kilometres on the map?
(b) By how much is a mapped area of $100\ \text{km} \times 100\ \text{km}$ in
error, to first order?
(c) Explain how the *gradient* of the scale factor matters for a strain-rate
calculation computed by differencing projected coordinates.
(d) Would the distortion change the dip and dip azimuth computed from the same
three points? Justify your answer quantitatively.

---

**★★7.** Sphere or ellipsoid? For each measurement, state whether the spherical
approximation is adequate and justify it with a number.

(a) A $2$ km baseline for a gravity survey, with positions good to $0.05$ m.
(b) An epicentral distance of $9000$ km, with arrival times good to $0.2$ s.
(c) An area of a $50\ \text{km} \times 50\ \text{km}$ concession, reported to
$0.1$ percent.
(d) A GNSS velocity of $20$ mm/yr measured over $500$ m between two stations.

---

**★★8.** False eastings and northings.

(a) Why does UTM use a false easting of $500\,000$ m?
(b) Why does the southern hemisphere use a false northing of $10\,000\,000$ m, and
what is the consequence if it is omitted?
(c) A point has UTM easting $612\,345$ m in zone 32. Estimate its distance from the
zone's central meridian, stating your approximation and why it is only an estimate.

---

## ★★★ Research-oriented

**★★★9.** Map a projection's distortion quantitatively.

Using the spherical transverse Mercator of the module's demonstration (or your own
implementation):

(a) Compute the scale factor $k(\varphi, \lambda)$ over a full UTM zone
($\lambda = -3°$ to $+3°$) at latitudes $0°$, $30°$, $60°$ and $80°$, on a
$0.25° \times 0.25°$ grid, by finite differences along both the meridian and the
parallel.
(b) Verify that the two directional scale factors agree everywhere, and report the
worst disagreement. What property of the projection does this confirm?
(c) Report the maximum and minimum $k$ over the zone at each latitude, and where
each occurs.
(d) Compare your maximum $|k - 1|$ with the value the choice of $k_0 = 0.9996$ was
intended to achieve.
(e) State clearly that your calculation is for the *spherical* transverse Mercator
and describe the two ways the ellipsoidal case differs.

---

**★★★10.** The cost of numerical integration for meridian arcs.

(a) Compute the quarter meridian by Simpson's rule with $n = 100$, $1000$, $10\,000$
and $100\,000$ intervals, and report each result and its error against the $10^{5}$
value.
(b) Report the empirical convergence exponent.
(c) Determine the interval count needed for 1 mm accuracy, and state whether it is
practical.
(d) Integrate the same expression with a step of $10°$ and $1°$, and explain the
error pattern in terms of where the integrand varies fastest.
(e) State which approach you would use in production, and why.

---

## Extension ideas

- Compute the meridian arc length between two latitudes on the sphere and on the
  ellipsoid, and report the difference as a function of latitude band. This is the
  quantity behind "one degree of latitude is not constant".
- Implement an equal-area projection (for example Lambert azimuthal equal-area) and
  compute its area error on a spherical cap where the answer is known, then compare
  its angular distortion against Mercator's.
