# Solutions — 04-02-04 Plate Motion Frames, Euler Poles and Global Models

> **Read this after attempting the exercises, not before.** Where a value is
> attributed to the demo it is the demo's actual output.

---

## ★1 — Speed on a small circle

**(a)** $0.50 \times \pi/180 = 8.727\times10^{-3}$ rad/Ma.

**(b)** $v = \omega R\sin\Delta = 8.727\times10^{-3} \times 6371 \times \sin 40°
= 55.61 \times 0.643 = 35.7$ km/Ma $= 35.7$ mm/a.

**(c)** Zero at the pole ($\sin 0° = 0$) and $55.6$ km/Ma at 90°.

**(d)** $v = \omega R\sin\Delta$ with $\Delta$ the angular distance from the pole;
the motion follows a **small circle** about the pole.

---

## ★2 — A site velocity

**(a)** Using spherical trigonometry, the angular distance between (50° N,
120° W) and (20° N, 130° W) is
$\cos\Delta = \sin50\sin20 + \cos50\cos20\cos10 = 0.766\times0.342 +
0.643\times0.940\times0.985 = 0.262 + 0.595 = 0.857$, so $\Delta = 31.0°$.

**(b)** $\omega = 0.70\times\pi/180 = 1.222\times10^{-2}$ rad/Ma, so
$v = 1.222\times10^{-2}\times6371\times\sin31.0° = 77.85\times0.515 = 40.1$ mm/a.

**(c)** The demo reports exactly `east 39.18, north -8.69` mm/a for this site and
pole, which gives a speed of $\sqrt{39.18^2 + 8.69^2} = 40.1$ mm/a, consistent
with (b).

**(d)** The azimuth is $\arctan(39.18/(-8.69))$ measured clockwise from north, so
about $102.5°$ — east-south-east. It is perpendicular to the great circle joining
the site to the pole, which is what a small circle about the pole requires.

---

## ★3 — Finite and instantaneous rotations

**(a)** $0.70 \times 30 = 21.0°$.

**(b)** No. A 21° rotation is well outside the regime in which the rotation
vector approximates a vector sum; the demo's closure error is already 3 per cent
at 13.8°.

**(c)** Three — the three components of the instantaneous angular velocity
vector, equivalently a pole position and a rate.

**(d)** Three as well, but they compose as matrices rather than add as vectors,
so a circuit has to be closed by matrix multiplication.

---

## ★4 — A pole at the north pole

**(a)**
$v = 6.981\times10^{-3} \times 6371 \times \sin 90° = 44.48$ km/Ma
$= 44.48$ mm/a.
The azimuth is due east (90°), since the velocity is
$\boldsymbol\omega\times\mathbf{r}$ with $\boldsymbol\omega$ along $+z$.

**(b)** At 40° N: $44.48\sin(90°-40°) = 44.48\cos40° = 34.07$ mm/a, due east. At
40° S: the same magnitude, $34.07$ mm/a, also due east — because the angular
distance from the pole is 130° in that case and $\sin130° = \sin50° = \cos40°$.

**(c)** All three velocities are due east, which puts the pole on the rotation
axis such that every site's motion is perpendicular to its meridian. Taking the
ratio of the speeds to $\cos(\text{latitude})$ gives $44.48/1 = 34.07/0.766
= 34.07/0.766 = 44.48$, a constant, so the pole is at the north geographic pole
and the rate is $44.48/6371$ rad/Ma $= 6.981\times10^{-3}$ rad/Ma $= 0.400$ °/Ma.

**(d)** It was easy because the pole coincides with a geographic pole, which makes
every velocity due east and the speed a simple function of latitude. It would be
hard — and in the limit impossible — if the pole lay in the direction of a site's
radius, because the rotation about that direction produces no velocity at that
site.

---

## ★★5 — Rank deficiency

**(a)** Rank 3, with singular values approximately
$[9010, 8873, 1565]$. The two sites are not antipodal, so the combined design
matrix is complete.

**(b)** Rank 2, with singular values $[9010, 9010, 0]$.

**(c)** Because the two sites are **antipodal**: $\mathbf{r}_2 = -\mathbf{r}_1$, so
$[\mathbf{r}_2]_\times = -[\mathbf{r}_1]_\times$ and the six rows of the design
matrix span only the same three-dimensional space as the first site's three
rows — one of which is already a null direction. Antipodal sites carry identical
information.

**(d)** Sites must be spread **around** the pole, not clustered and not antipodal —
roughly evenly distributed in azimuth about the rotation, which is why a global
GNSS network determines a pole far better than a local one.

---

## ★★6 — The frame problem

**(a)** The additional rotation contributes `east -8.34, north -28.89` mm/a at
this site.

**(b)** `east 20.00 - 8.34 = 11.66`, `north 5.00 - 28.89 = -23.89` mm/a.

**(c)** It is unchanged, to the last digit, because the same rigid rotation was
applied to both plates. The relative motion is a difference of two velocities and
the added term cancels exactly.

**(d)** A frame in which one plate is fixed (a "Pacific-fixed" or "Africa-fixed"
frame); a no-net-rotation frame, defined by requiring the surface integral of the
velocity to vanish; and a frame tied to an external physical reference, such as
the geomagnetic field, the hotspots, or a geodetic frame like ITRF.

---

## ★★★7 — Closure error growth

**(a)** The relative errors are 0.16, 0.81, 1.62 and 3.25 per cent at maximum
angles of 0.7°, 3.4°, 6.9° and 13.8°. The angle ratios are 1, 4.86, 9.86 and
19.7 and the error ratios are 1, 5.1, 10.1 and 20.3 — the two are proportional to
within a few per cent, so the relative error is approximately linear in the
rotation angle.

**(b)** Because the vector-sum defect is the commutator of the two rotations,
which is of second order in the angles, while the normalising denominator (the
sum of the rotation magnitudes) is of first order. A second-order term divided by
a first-order term is first order — so the *relative* error grows linearly with
the angle even though the absolute defect grows quadratically.

**(c)** Extrapolating linearly from 3.25 per cent at 13.8° gives about 14 per cent
at 60°.

**(d)** Compose the rotation matrices (or quaternions) rather than adding
rotation vectors, and carry the composition through the circuit. The demo shows
that the two disagree by a per cent at a few degrees and by tens of per cent at
60°, which is far larger than the discrepancy between published reconstructions.

---

## ★★★8 — The demo's output

**(a)** Speeds and small-circle values at the six sites — 72.22/72.22, 45.26/45.26,
34.45/34.45, 42.70/42.70, 72.69/72.69, 67.87/67.87 mm/a — agree to the printed
precision in every row, with azimuths from 55.6° to 164.1°.

**(b)** `AB = [0.05 0.02 0.01]`, `BC = [-0.01 0.04 0.02]`,
`CA = [-0.04 -0.05944 -0.03109]`; the vector sum has magnitude `0.001230 rad`
against `0.178697 rad` of total rotation, a relative error of `1.22 %`.

**(c)** Recovered pole `latitude -45.06 deg, longitude 110.13 deg, rate
0.600 deg/Ma`; errors `0.06 deg`, `0.13 deg`, `0.000 deg/Ma`; rank `3 of 3`.

**(d)** `RMS horizontal residual = 0.880 mm/a`, against 1 mm/a of noise added per
horizontal component — so the fit has recovered the noise level rather than
over-fitting.

**(e)** One site: `rank 2 of 3`, singular values `[6.371e+03, 6.371e+03,
2.368e-13]`, unconstrained direction pointing at the site's own pole `(20.0,
40.0)`. Two sites: `rank 3 of 3`, singular values `[9009.955, 7696.646,
4684.115]`.

**(f)** `east 16.61, north -10.45 mm/a` for the difference between the two frames
at the site.

**(g)** The demo verifies that the machinery implements Euler's theorem — the
closed form and the vector computation agree, the circuit closes by composition,
the inversion recovers its own input and the noise level in the residual. It does
not verify anything about the Earth, because the poles and the velocity field are
synthetic. Applying the same machinery to a documented plate-motion solution's
published poles, and checking the reconstruction against an independent
observation, is the step that would test the Earth rather than the code.

---

## ★★★9 — Units

| Combination | Unit of $\boldsymbol\omega\times\mathbf{r}$ | A velocity a geodesist quotes? |
|---|---|---|
| km and rad/Ma | km/Ma | Yes — numerically identical to mm/a |
| m and rad/a | m/a | Yes — divide by $10^{-3}$ to get mm/a |
| m and rad/Ma | m/Ma = $10^{-6}$ m/a | No — too small by $10^{-3}$ |
| km and °/Ma | km·°/Ma | No — degrees are not radians |

The one conversion to remember is $1\ \text{km/Ma} = 1\ \text{mm/a}$, plus the
radian conversion $\pi/180$ when an angle is given in degrees. With those two,
every combination above becomes usable, and the danger of a silent factor of
$10^{3}$ or $10^{9}$ disappears.
