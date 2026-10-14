# Solutions — 03-05-03 Maps, Cross-Sections and Geological Symbology

> **Read this after attempting the exercises, not before.** Values attributed to
> the demonstration are its actual output.

---

## ★1 — A degree of longitude

**(a)** $111.319\cos\varphi$ km:

| $\varphi$ | 1° longitude (km) |
|---|---|
| 0° | 111.319 |
| 45° | 78.714 |
| 60° | 55.660 |

**(b)** Fractional error of the sphere against the WGS84 geodesic:

| $\varphi$ | spherical | geodesic | fractional error |
|---|---|---|---|
| 0° | 111.319 | 111.319 | 0.000 % |
| 45° | 78.714 | 78.846 | 0.167 % |
| 60° | 55.660 | 55.799 | 0.250 % |

**(c)** The error grows because the ellipsoid's east–west radius of curvature
departs from the equatorial radius by an amount proportional to the flattening, and
the departure is largest toward the pole. It is small because the flattening itself
is small ($f \approx 1/298.3$): the spherical approximation is good to a few parts
in a thousand for distance, which is why the *distortion* of a Cartesian lon/lat
plot — a factor of $1/\cos\varphi$, i.e. up to 2 at 60° — completely dominates the
ellipsoid correction. The sphere is adequate for the distortion argument and
inadequate for a geodetic coordinate.

---

## ★2 — A 4° × 4° map

**(a)** $4 \times 55.799 = 223.196$ km at 60°N.

**(b)** $4 \times 111.421 = 445.684$ km.

**(c)** $223.196/445.684 = 0.5008$.

**(d)** A Cartesian plot of longitude against latitude gives 4° of longitude the
same width in pixels as 4° of latitude, so the implied ratio is 1.000. The map is
too wide by a factor $445.684/223.196 = 2.00$: an equidimensional feature appears
twice as elongated east–west as it is. Across a region spanning 58°–62°N the error
varies from 0.470 to 0.530 of the width, so the shear is not even constant and
cannot be corrected by a single stretch.

---

## ★3 — Vertical exaggeration

**(a)** Horizontal $= 400/6.4 = 62.5$ km/in; vertical $= 40/2.4 = 16.667$ km/in;
$\mathrm{VE} = 62.5/16.667 = 3.75$.

**(b)** Vertical $= 60/2.4 = 25$ km/in; $\mathrm{VE} = 62.5/25 = 2.50$.

**(c)** Vertical $= 40/4.8 = 8.333$ km/in; $\mathrm{VE} = 62.5/8.333 = 7.50$.

**(d)** Increasing the panel height, which increases the vertical scale and so
reduces VE. Reducing the depth extent of the section (b) also reduces VE but
usually means cutting data; the panel height is the parameter the author controls
without losing information.

---

## ★4 — Symbology

| Symbol | Assertion |
|---|---|
| 1. Dashed line | (b) structure inferred or concealed |
| 2. Line with proportional tick | (d) dip magnitude and direction known here |
| 3. Triangle at a borehole | (a) a measurement was made here |
| 4. Contour interval 5 mGal | (e) gradient quantised at a stated level |
| 5. Colour bar with $v_{\min} = -v_{\max}$ | (c) signed field, neutral colour at zero |

---

## ★5 — Running the demonstration

**(a)** The first four rows of the geodesic table:

```text
        0.0          111.319          110.574      1.0000    1.0000
       30.0           96.486          110.861      0.8667    0.8660
       45.0           78.846          111.142      0.7083    0.7071
       60.0           55.799          111.421      0.5013    0.5000
```

**(b)** Mercator:

```text
        60.0          222264.8        2.0101      2.0000     0.0050
        80.0          640936.3        5.7964      5.7588     0.0065
```

The relative differences are 0.50 % at 60° and 0.65 % at 80°.

**(c)** All three panels report `aspect=1.0`, and each prints
`coastlines drawn` when the Natural Earth data are available and cached.

**(d)** Vertical exaggeration 3.750, and the 1:1 panel would be 0.640 in tall at
the same 400 km width — a strip 3.8 times thinner than the panel drawn.

---

## ★6 — Apparent and true dip

**(a)** $\tan\theta_{\text{app}} = 3.75\tan\theta$:

| true dip | apparent dip |
|---|---|
| 5° | 18.16° |
| 10° | 33.47° |
| 30° | 65.21° |

**(b)** $\theta = \arctan(\tan 45^\circ/3.75) = \arctan(0.26667) = 14.93^\circ$.

**(c)** Because the relation is $\tan\theta_{\text{app}} = \mathrm{VE}\tan\theta$,
not $\theta_{\text{app}} = \mathrm{VE}\,\theta$. The tangent is nonlinear, so the
error is a function of the dip: at VE = 3.75 the exaggeration adds 13.2° to a 5°
dip and 35.2° to a 30° dip. A constant offset cannot represent that, and the
correction must be applied as an arctangent.

---

## ★7 — Scale bars on Mercator

**(a)** Scale factor $= 1/\cos 60^\circ = 2.000$ (the ellipsoidal numerical value
from the demonstration is 2.0101). A bar correct at the equator understates true
distance by a factor of 2.0.

**(b)** $1/\cos 80^\circ = 5.759$ by the sphere, 5.796 by the ellipsoid.

**(c)** Three options: use a projection that is conformal but with a scale bar
labelled with its reference latitude; draw the scale bar at the map's central
latitude and state that it applies there; or avoid Mercator entirely — a conic
projection (Lambert Conformal Conic) is the conventional choice for a mid-latitude
regional map and keeps the scale variation small across the sheet.

---

## ★8 — Projections

**(a)** Global station density: an **equal-area** projection (e.g. Equal Earth or
Mollweide). It preserves area, which is the quantity being displayed, and
sacrifices local shape. A Mercator map would misstate the density by a factor of
$1/\cos^2\varphi$.

**(b)** Regional fault orientations at 40°N: a **conformal** projection (Lambert
Conformal Conic). It preserves local angles, so fault strikes and the angles
between conjugate sets are correct, and sacrifices area — which is acceptable
because area is not the message.

**(c)** The Arctic: an **azimuthal** projection centred on the pole (stereographic
for a conformal polar map, or a polar equal-area if extent is the message). Any
cylindrical projection is unusable because the scale factor diverges at the pole.

**(d)** Global anomaly intensities: an **equal-area** projection, and the intensities
compared through the colour bar rather than through apparent map size. A
compromise such as Robinson trades some area fidelity for a more familiar shape and
is acceptable if the caption says so.

---

## ★9 — Measuring on an exaggerated section

**(a)** Horizontal distance $= 20\ \text{mm} \times 4.706\ \text{km/mm} =
94.12$ km. Depth difference $= 15\ \text{mm} \times 0.7273\ \text{km/mm} =
10.91$ km. Apparent dip $= \arctan(10.91/94.12) = \arctan(0.11593) = 6.61^\circ$.

**(b)** True dip $= \arctan(0.11593/3.75) = \arctan(0.030915) = 1.77^\circ$.

**(c)** The horizontal distance is unaffected: the horizontal scale of the page is
not changed by exaggerating the depth axis, so a 20 mm horizontal separation is
20 mm of the stated horizontal scale whatever the VE. The depth difference *is*
affected, because it was obtained by multiplying a page length by the vertical
scale. Hence the quotient — the apparent dip — is wrong by the full factor, and
the two measurements cannot be corrected independently.

---

## ★10 — Publishing a map and a section

**(a)** The six decisions, in order: (1) the coordinate reference system and datum
for the map, and the line along which the section is taken; (2) the projection and
its central meridian/parallel; (3) the data CRS passed to every plotting call;
(4) the map extent and the section's horizontal extent and depth range; (5) the
palette class for each quantity and, for a diverging one, the centre value; (6) the
vertical exaggeration of the section, or the panel aspect that sets it.

**(b)** The decisions that change the numbers a reader extracts are (1) — because
distances and azimuths depend on the datum and CRS — (3), because a wrong data CRS
displaces every point, and (6), because every dip and depth difference depends on
the exaggeration.

**(c)** The decisions that change only the interpretation are (2) and (5). One
concrete example for (2): an equal-area projection makes two anomalies of equal
integrated size look equal, while a conformal projection makes two faults of equal
strike look equally straight — the same data support "these anomalies carry equal
mass" under one choice and "these faults are equally oriented" under the other.
Neither statement is false; they are different arguments, and the caption must say
which one the figure is making.
