# Solutions — 04-04-05 Reading Geological Maps and Constructing Cross-Sections

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output.

---

## ★1 — Attitude from coefficients

**(a)** $\delta = \arctan\sqrt{a^2 + b^2} = \arctan\sqrt{0.140625 + 0.003086} =
\arctan 0.37909 = 20.76^\circ$, the demo's `dip 20.76`.

**(b)** $\theta_d = \operatorname{atan2}(-a, -b) = \operatorname{atan2}(0.375,
0.055556) = 81.57^\circ$, the demo's `dip azimuth: 81.57`.

**(c)** $\text{strike} = \theta_d - 90^\circ = -8.43^\circ \equiv 351.57^\circ$,
the demo's `strike 351.57`.

**(d)** The dip azimuth is the direction of **steepest descent**, which is along
$-\nabla z$ because $z$ is elevation and increases upwards. Reversing the sign
gives a strike 180° out and exactly the same dip magnitude — a result that passes
every inspection that does not involve a section or an outcrop pattern, which is
why the error is dangerous.

---

## ★2 — Thickness

**(a)** $t = v\cos\delta = 100\cos 60^\circ = 50.0$ m.

**(b)** $v/t = 1/\cos 60^\circ = 2.000$: the borehole overstates the true thickness
by a factor of two.

**(c)** At 30°: $t = 86.60$ m and $v/t = 1.155$.

**(d)** An isopach map shows **true (isopachous) thickness**, the perpendicular
distance between two bounding surfaces. A borehole measures **vertical thickness**.
The two differ by $\cos\delta$, and the correction is the whole of the exercise.

---

## ★3 — Three points

**(a)** The design matrix is

$$\begin{pmatrix} 0 & 0 & 1 \\ 1200 & 0 & 1 \\ 400 & 900 & 1 \end{pmatrix},
\qquad \mathbf{d} = \begin{pmatrix} 400 \\ -50 \\ 200 \end{pmatrix}.$$

**(b)** Three unknowns $(a, b, c)$ and three equations: exactly determined, so the
least-squares solution is an exact solve. With a fourth borehole the system becomes
over-determined and the fit becomes a genuine least squares, which is the honest
treatment of redundant data.

**(c)** The two edge vectors in map coordinates are
$\mathbf{e}_1 = (1200, 0)$ and $\mathbf{e}_2 = (400, 900)$, so

$$\text{area} = \tfrac12|1200 \times 900 - 0 \times 400| = 540\,000 \text{ m}^2.$$

**(d)** A large triangle means the three elevation measurements sample the plane
over a long baseline, so a given elevation error produces a small attitude error.
A small triangle means the same error rotates the plane much more, and the failure
is silent: the returned strike and dip still look like a strike and a dip. The demo
reports the area alongside every solution for this reason.

---

## ★4 — The demo

**(a)** Both methods give `z = -0.28867513 x +0.50000000 y +144.33756730` for the
synthetic strike-60/dip-30 plane, with a largest coefficient difference of
`1.283e-12`.

**(b)** `residuals of the three points against the fitted plane: 7.769e-10 m`.

**(c)** Both methods recover `strike 60.0000, dip 30.0000` against the input
`strike 60.0000, dip 30.0000`, with errors `1.251e-12` and `6.398e-11` degrees.

**(d)** It verifies that the geometry is being handled in a consistent frame — in
particular that the sign convention in the dip azimuth is the same in both
constructions. It does **not** verify the geology: it cannot detect that the map
coordinates were misread, that a borehole was assigned to the wrong hole, or that
the marker correlated between the holes is not the same horizon. Those are
geological errors, and no amount of arithmetic will find them.

---

## ★5 — The round trip and its failure

**(a)** `worst error over the suite: strike 5.684e-14 deg, dip 1.421e-14 deg` over
eight attitudes from 0° to 350° in strike and 5° to 75° in dip.

**(b)** `400,000` m². It was held fixed so that the comparison isolates the effect
of the attitude alone: if the triangle changed between cases, a difference in the
error could be a geometric effect rather than an algorithmic one.

**(c)** The demo's near-collinear table gives, with 0.5 m of elevation error,
strike errors of `0.6028`, `85.2611` and `149.9740` degrees at triangle areas of
25 000, 500 and 0.5 m² respectively — the first from the row at third point
(1000, 50), the second at (1000, 1) and the third at (1000, 0.001).

**(d)** The failure is **silent**. The solver returns a strike and a dip in every
case, with full floating-point precision, and the answer with a 150° strike error
is indistinguishable from a good answer unless the triangle area (or the condition
number of the design matrix, which reaches $2 \times 10^6$ in the demo) is
reported. In the field this happens when three measurement sites are nearly along
one line — a ridge, a road, a coastline — and the temptation to use them is
strongest exactly there.

---

## ★6 — A prediction and an outcrop

**(a)** $z = -0.375(1500) - 0.055556(600) + 400 = -562.5 - 33.33 + 400 =
-195.83$ m, the demo's `marker elevation -195.83 m`.

**(b)** $500 - (-195.83) = 695.83$ m, the demo's `depth 695.83 m`.

**(c)** By refitting the plane with the predicted point included and reporting how
much the coefficients change: `4.172e-11`, i.e. nothing. The check matters because
a prediction that is merely close to the plane is a different object from one that
is on it, and only the latter can be used to site a well.

**(d)** The outcrop trace is the line where $z = 0$, which for a planar bed is
straight. Its direction must be the strike because every point on it has the same
elevation, and the strike is the horizontal direction within the plane — the demo
prints `trace direction azimuth: 171.57` against `strike 351.57`, a difference of
`0.00e+00` once both are reduced modulo 180, and it verifies that points 500 m
along the trace in either direction have zero elevation.

---

## ★7 — Designing a survey

**(a)** From the three boreholes the marker is
$z = -0.37500000x - 0.05555556y + 400$, giving strike `351.57` and dip `20.76`.

**(b)** The triangle area is
$\tfrac12|1200 \times 900 - 0 \times 400| = 540\,000$ m². The smallest
axis-aligned rectangle containing the three collars is
$1200 \times 900 = 1.08 \times 10^6$ m², so the triangle occupies about
**50 per cent** of it — a well-conditioned configuration. (A triangle can never
exceed half the rectangle, since the rectangle can be split into two congruent
triangles.)

**(c)** A fourth borehole **cannot improve the plane at all** if the three existing
points are consistent, because three non-collinear points determine a plane
exactly: adding a fourth point either agrees with the plane (adding nothing) or
disagrees (in which case what you have is redundancy, i.e. a test). The fourth hole
should therefore be placed to **test** the plane and to extend it, not to improve
it. The natural choice is at the largest distance from the centroid along the
direction of steepest descent, e.g. near $(1500, 600)$ as in ★6: it is far from the
triangle, so an inconsistency with the plane cannot be attributed to a small
baseline, and the disagreement (or agreement) is informative. The condition number
that governs the *propagated* error of the fitted plane from noisy data does
improve with a fourth well placed far away — which is the real reason to drill it,
and the improvement is in the error bar, not the central value.

**(d)** Two independent sources: (i) the **measurement error** in collar position
and elevation and in the depth to the marker, which propagates into the
coefficients and can be estimated from the residuals if there are more than three
wells; and (ii) the **geological error** from correlating a different horizon, a
faulted or folded interval between wells, or a marker that is not a plane. The
first is estimated by least squares; the second can only be estimated by an
independent observation — a seismic line, an outcrop, or a fourth well's
stratigraphy — and it is usually the larger of the two.

---

## ★8 — Cutting a bed with a fault

**(a)** Setting the two right-hand sides equal and collecting terms:

$$(-0.375 - 0.866025)x + (-0.055556 - 1.5)y + (400 - 0) = 0$$

$$-1.241025x - 1.555556y + 400 = 0,$$

which is the equation of a straight line in the map plane. Eliminating $z$ is what
turns two surfaces into one line.

**(b)** For $Ax + By + C = 0$ with $A = -1.241025$ and $B = -1.555556$, the
direction is $(-B, A) = (1.555556, -1.241025)$, normalised to
$(0.7817, -0.6237)$. Its azimuth is $\operatorname{atan2}(0.7817, -0.6237) =
128.6^\circ$. The demo's analogous case gives `cutoff line azimuth: 139.11` for a
different fault attitude; the construction is the same.

**(c)** From the line equation with $y = 0$: $x = 400/1.241025 = 322.31$ m, and
substituting into the bed equation gives
$z = -0.375(322.31) - 0 + 400 = 279.13$ m. Substituting the same point into the
fault equation gives $z = 0.866025(322.31) + 0 = 279.13$ m. Both agree, which is
what it means for the point to lie in both planes. The demo does this check at
five positions along the line and reports residuals of `0.00e+00` and
`5.68e-14` — the second being the round-off floor of the arithmetic.

**(d)** The line is the **trace of the cutoff**: on the map the bed's outcrop stops
at the fault and resumes offset on the other side. In a cross-section the
separation of the two cut-offs measured along the fault trace is the
**stratigraphic separation along the fault**, and it is **not the slip** because
the slip is a vector in the fault plane whereas the separation is a distance
between two stratigraphic surfaces measured in a stated direction. They coincide
only for pure dip-slip motion on a section perpendicular to strike. The demo
prints the same caution, and the point recurs in
[04-04-02 §3](./02-faults-solutions.md).
