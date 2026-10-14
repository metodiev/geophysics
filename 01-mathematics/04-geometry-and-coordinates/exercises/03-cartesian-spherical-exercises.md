# Exercises — 01-04-03 Cartesian, Cylindrical and Spherical Coordinates

Attempt these **closed-book**. Solutions are in
[`03-cartesian-spherical-solutions.md`](./03-cartesian-spherical-solutions.md).
Difficulty: ★ foundational · ★★ applied · ★★★ research-oriented.

Unless stated otherwise, spherical coordinates are $(r, \theta, \phi)$ with
$\theta$ the **colatitude** from $+z$ and $\phi$ the azimuth anticlockwise from
$+x$; and $(x, y, z) = (\text{east, north, up})$ with units of kilometres for
Earth-scale problems. Use the WGS84 ellipsoid $a = 6378.137$ km,
$1/f = 298.257223563$ where an ellipsoid is needed.

---

## ★ Foundational

**★1.** Convert to cylindrical and spherical coordinates:

(a) $(3, 4, 0)$
(b) $(-3, 4, -12)$
(c) $(0, 0, -7)$

Then convert each answer back to Cartesian and compare. For which point(s) is the
azimuth undefined, and why is that not a bug?

---

**★2.** Volume and solid angle.

(a) Write the Jacobian matrix of the Cartesian-to-spherical transformation.
(b) Evaluate its determinant.
(c) Integrate $d\Omega = \sin\theta\,d\theta\,d\phi$ over a full sphere and state
what the result defines.
(d) Integrate the volume element over a sphere of radius $R = 10$ (any units) and
compare with $4\pi R^{3}/3$. Comment on the size of the disagreement and its
origin.

---

**★3.** Spherical caps on $R = 6371.0088$ km.

(a) Compute the area of a cap of half-angle $5°$ and of $30°$.
(b) Compute the area of a cap of half-angle $90°$ and state what it is.
(c) Express the $5°$ cap as a fraction of the whole sphere.
(d) Compute the area of a $0.1° \times 0.1°$ grid cell at $10°$N and at $80°$N on
the same sphere, and state the ratio. What does the ratio imply about the number of
grid cells needed to sample a fixed physical area at the two latitudes?

---

## ★★ Applied

**★★4.** Geocentric rectangular coordinates.

For an ILLUSTRATIVE point at $40°$N, $20°$E, $h = 0$ km:

(a) Compute the ECEF coordinates assuming a sphere of radius $a = 6378.137$ km.
(b) Compute them on the WGS84 ellipsoid, using the prime vertical radius
$N(\varphi)$.
(c) Compute the geocentric radius in each case and state the difference.
(d) Compute the geocentric latitude in the ellipsoidal case and compare with the
geodetic latitude.
(e) Recover the geodetic latitude from your answer to (b) and state the error.

---

**★★5.** Geodetic versus geocentric latitude.

(a) Derive $\tan\varphi_{\text{geocentric}} = (1-e^{2})\tan\varphi_{\text{geodetic}}$
from the ECEF transformation.
(b) Evaluate the difference at $0°$, $15°$, $30°$, $45°$, $60°$, $75°$ and $90°$,
and tabulate it.
(c) Convert each difference into a ground distance in kilometres and state where
the maximum occurs.
(d) State one workflow in which confusing the two produces a wrong answer, and
what the size of the error would be.

---

**★★6.** Direction cosines.

A ray leaves a source with take-off angle $i$ from the downward vertical and
azimuth $A$ clockwise from north.

(a) Write the unit vector in east–north–up components.
(b) Evaluate it for $i = 0°, 30°, 60°, 90°$ with $A = 0°$ and with $A = 135°$.
(c) Verify that the norm is 1 in every case.
(d) A colleague's implementation uses $(\cos A\sin i,\ \sin A\sin i,\ -\cos i)$.
State precisely what that vector describes and at which azimuths the error
vanishes.

---

**★★7.** The chord identity.

(a) Prove $d_{\text{chord}} = 2R\sin(\Delta/2)$ for two points separated by
central angle $\Delta$.
(b) For a point at $(45°\text{N}, 10°\text{E})$ on $R = 6371.0088$ km, compute its
Cartesian coordinates.
(c) For the point at $(45.5°\text{N}, 10.5°\text{E})$, compute the Cartesian
distance between the two points. Report it to the metre.
(d) Compute the same distance from the central angle with the chord identity and
compare. State which route you would use in production and why.

---

**★★8.** The pole problem.

(a) Compute the north–south and east–west lengths of one degree of arc at
latitudes $60°$, $80°$ and $89.9°$ on a sphere of radius $6371.0088$ km, and the
ratio.
(b) Describe what happens to a regular $0.1° \times 0.1°$ latitude–longitude grid
as it approaches the pole, in terms of the number of cells per unit area.
(c) A dipole geomagnetic anomaly is gridded on a regular latitude–longitude grid
and contoured. Describe the artefact that will appear near the pole and explain
its cause.

---

## ★★★ Research-oriented

**★★★9.** Ill-conditioning near the polar axis.

(a) Compute the great-circle azimuth from $(89.9999°\text{N}, 0°\text{E})$ to
$(89.9999°\text{N}, 90°\text{E})$, and to $(89.9999°\text{N}, 180°\text{E})$.
Explain the second result geometrically.
(b) Perturb the starting latitude by $10^{-6}°$, $10^{-5}°$ and $10^{-4}°$ and
report the change in each azimuth.
(c) Express the amplification as a ratio of output change to input change and
comment on whether an azimuth measured near the pole is meaningful.
(d) Repeat at $89.9°$N and $89°$N and report how the amplification scales with
distance from the pole.
(e) State what a practitioner should do when a calculation requires an azimuth
within a degree of the pole, and what other coordinate choice removes the problem.

---

**★★★10.** Verifying an ECEF implementation globally.

(a) Implement the forward transformation (geodetic latitude, longitude, height) to
ECEF on WGS84, and a closed-form inverse.
(b) Round-trip over a global grid of latitudes from $-89°$ to $89°$ in $2°$ steps,
longitudes in $10°$ steps, and heights of $0$ and $5000$ m. Report the worst error
in latitude, longitude and height separately, and the location of the worst case.
(c) Repeat with a restricted grid reaching $89.9999°$N and report whether the
latitude recovery degrades near the pole.
(d) Explain why the closed-form inverse is accurate at the pole even though the
*azimuth* there is undefined, and what this says about the difference between an
undefined coordinate and an inaccurate one.
(e) State the limits of your verification: what class of error would pass it?

---

## Extension ideas

- Implement a local east–north–up frame at a given geodetic position (the rotation
  from ECEF to ENU), and use it to convert a GNSS velocity triplet from ECEF to
  east–north–up. Verify the rotation by checking that a purely vertical ENU velocity
  maps to an ECEF vector parallel to the local ellipsoidal normal.
- Compute the solid angle subtended by a rectangular region bounded by two
  meridians and two parallels, and compare with the product of its angular extents
  — the discrepancy is a curvature effect and it has a closed form.
