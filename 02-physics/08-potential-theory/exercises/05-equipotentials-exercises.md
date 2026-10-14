# Exercises — 02-08-05 Equipotential Surfaces, Geoid and Level Surfaces

Attempt these **closed-book** before opening the
[solutions](./05-equipotentials-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/equipotential_geoid_demo.py`](../code/equipotential_geoid_demo.py)
require you to run it and report its actual output. Use the WGS 84 defining
parameters $a = 6\,378\,137$ m, $1/f = 298.257\,223\,563$,
$\omega = 7.292\,115\times10^{-5}$ rad s$^{-1}$,
$GM_\oplus = 3.986\,004\,418\times10^{14}$ m$^3$ s$^{-2}$, and
$G = 6.674\,30\times10^{-11}$ m$^3$ kg$^{-1}$ s$^{-2}$.

---

## ★ Foundational

**★1.** This exercise is about definitions; answer in one or two sentences each.

(a) Define the geoid.
(b) Define the reference ellipsoid.
(c) Define the geoid undulation and state its sign convention.
(d) State which of the three surfaces (geoid, ellipsoid, topography) is an
equipotential and which is a convention.
(e) State why mean sea level is not exactly the geoid.

---

**★2.** $q$ and the flattening.

(a) Compute $q = \omega^2a^3/GM$ from the defining parameters.
(b) Compute the flattening $f$ from $1/f$.
(c) Compute the polar semi-axis $b = a(1-f)$ and the polar–equatorial difference
$a - b$.
(d) Compute $J_2$ from the hydrostatic relation $J_2 = (2f-q)/3$.
(e) State why $1/f$ and $f$ are easily confused and what the numerical consequence
of the confusion is.

---

**★3.** Bruns' formula.

(a) State Bruns' formula and define every symbol.
(b) A disturbing potential of $T = 9.8$ m$^2$ s$^{-2}$ acts where
$\gamma = 9.8$ m s$^{-2}$. Compute $N$.
(c) Compute $N$ for $T = 98$ m$^2$ s$^{-2}$.
(d) State the order in $T/\gamma$ to which Bruns' formula is valid and how the
error scales.

---

**★4.** Deflection of the vertical.

(a) State the definition of the deflection of the vertical in terms of
$\nabla U$ and the ellipsoidal normal.
(b) An anomalous horizontal acceleration of $1.0\times10^{-4}$ m s$^{-2}$ acts where
$\gamma = 9.8$ m s$^{-2}$. Compute the deflection in radians and arcseconds.
(c) Convert $1$ arcsec to radians.
(d) Explain, in one sentence, why the deflection is a derivative-like quantity and
what that implies about its depth sensitivity compared with a gravity anomaly.

---

## ★★ Applied

**★★5.** Run
[`../code/equipotential_geoid_demo.py`](../code/equipotential_geoid_demo.py).

(a) Report the cosines in the perpendicularity test at $h = 10^{-3}$ and
$h = 10^{-6}$ rad, and the ratio between them.
(b) Report the sphericity spread with $\omega = 0$.
(c) Report the model flattening and the WGS 84 datum flattening and their ratio.
(d) Report the best-fit ellipsoid's polar semi-axis and the worst residual.
(e) Report $J_2$ from $(2f-q)/3$, the homogeneous value, and the ratio.
(f) Report the worst relative difference between Bruns' formula and the solved level
surface over the two anomaly tables.
(g) Report the peak deflection in arcseconds.

---

**★★6.** A shallow mass anomaly.

(a) Take a sphere of radius $5000$ m and density contrast $300$ kg m$^{-3}$ with
its centre $10000$ m below the surface. Compute its mass.
(b) Compute the disturbing potential directly above it.
(c) Compute the geoid undulation with Bruns' formula.
(d) State whether a $0.1$ m geoid undulation is useful for exploration, and what
that implies about what geoid data measure.

---

**★★7.** A deeper, broader anomaly.

(a) Take a sphere of radius $20000$ m and density contrast $250$ kg m$^{-3}$ with
its centre $40000$ m deep. Compute its mass.
(b) Compute the geoid undulation directly above it.
(c) Compute the deflection of the vertical at horizontal offsets of $0$, $10000$,
$20000$, $40000$ and $80000$ m, and locate approximately where it peaks.
(d) State the ratio of the two anomalies' geoid undulations and the ratio of their
gravity anomalies, and explain the difference in terms of depth.

---

**★★8.** The level surface of a rotating point mass.

(a) Write $U(r,\theta)$ for a rotating point-mass Earth.
(b) Show that $U$ is not harmonic and give the value of $\nabla^2$ of the
centrifugal term.
(c) Solve $U(r,\theta) = U_0$ for $r(0^\circ)$ and $r(90^\circ)$ with $U_0$ fixed by
the equatorial radius $a$.
(d) Compute the model flattening and compare with the datum flattening, and explain
the difference physically.

---

## ★★★ Research-oriented

**★★★9.** Geoid versus ellipsoid: a structural argument.

(a) Explain why an equipotential of a rotating fluid body cannot be exactly an
ellipsoid unless the body is homogeneous and certain higher-order conditions hold.
(b) Show that for a homogeneous body in hydrostatic equilibrium the relation
$J_2 = (2f-q)/3$ is exact to first order in $q$, and state what it would take to
make the level surface exactly an ellipsoid.
(c) Discuss the "hydrostatic excess" of $J_2$ in the Earth: what it is, what it
implies about the support of the equatorial bulge, and which observations constrain
it.
(d) State which of your answers are derived and which are statements about the real
Earth that require data, and name the data source.

---

**★★★10.** The relation between geoid undulation and gravity anomaly.

(a) Starting from $N = T/\gamma$ with $T$ harmonic, write $T$ in spherical harmonics
and express $N$ as a series in the coefficients.
(b) Take the radial derivative of $T$ to obtain the gravity anomaly
$\Delta g = -\partial T/\partial r - 2T/r$ (the free-air anomaly) and relate the two
series coefficient by coefficient.
(c) Show that the ratio of the two series is a function of degree alone, and
therefore that a geoid anomaly emphasises low degrees relative to a gravity anomaly.
(d) Compute the degree-dependent factor for $l = 2$ and $l = 100$ with
$a = 6\,378\,137$ m, and state the practical consequence for interpreting a gravity
map versus a geoid map.

Report measured values only if you verify them numerically, and state which of
your results are analytic.
