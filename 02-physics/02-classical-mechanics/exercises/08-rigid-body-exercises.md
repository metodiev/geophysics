# Exercises — 02-02-08 Rigid-Body Dynamics, Precession and the Earth's Rotation

Attempt these **closed-book** before opening the
[solutions](08-rigid-body-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Use $\omega_\oplus = 7.292\,115\times10^{-5}$ rad s⁻¹, $a = 6\,378\,137$ m and
$1/f = 298.257\,223\,563$ (all defining, WGS 84). For the forced-precession
problems take the sidereal year as 365.256 days and the obliquity as 23.439°, and
**label them as nominal** (to be verified from an almanac or IERS). State a
regime of validity with every numerical answer in ★★ and ★★★.

---

## ★ Foundational

**★1.** Write Euler's equations for a rigid body in principal axes.
(a) Explain what the terms $(I_2-I_3)\omega_2\omega_3$ represent physically.
(b) Simplify them for a symmetric top with $I_1 = I_2 = A$, $I_3 = C$.
(c) State why the equations are exact for a rigid body and where the rigid-body
assumption fails for the Earth.

---

**★2.** A symmetric top has $A = B = 1$ and $C = 1.5$ (arbitrary units) spinning
with $\omega_3 = 3$ rad/s. (a) Show that $\omega_3$ is constant.
(b) Compute the precession rate $\Omega = \omega_3(C-A)/A$ and the period.
(c) State what this motion corresponds to for the Earth.

---

**★3.** From the WGS 84 defining parameters: (a) compute the polar semi-axis
$b = a(1-f)$; (b) compute $H = (C-A)/A = (a^{2}-b^{2})/(a^{2}+b^{2})$ for a
uniform-density spheroid; (c) compute the free precession period $2\pi/(\omega H)$
in days.

---

**★4.** Name the two quadratic invariants of the torque-free motion of an
asymmetric top, and explain why the *components* of $\boldsymbol{\omega}$ are not
conserved.

---

## ★★ Applied

**★★5.** Using $H = 0.00335843$ (from ★3), the nominal sidereal year and the
nominal obliquity: (a) compute $\omega/n$; (b) compute the solar-only precession
rate in rad/s and in arcsec/yr ($1\ \mathrm{rad} = 206\,264.81$ arcsec);
(c) compute the resulting precession period in years; (d) state which
contributions to the observed precession are missing from this calculation.

---

**★★6.** Sensitivity. (a) Recompute the precession rate and period for
$H = 0.0033$, 0.0032 and 0.0030. (b) Show that the period scales as $1/H$ and
verify the scaling numerically. (c) Explain why the precession rate is therefore
a measurement of the Earth's *internal mass distribution*, given that the
astronomical inputs are external.

---

**★★7.** An asymmetric top has $A = 1$, $B = 1.5$, $C = 2$ and initial
$\boldsymbol{\omega} = (1, 0.2, 3)$ rad/s. (a) Compute $|\mathbf{L}|^{2}$ and
$T_{\text{rot}}$. (b) State how you would verify numerically that they are
conserved. (c) Explain what a *polhode* is and why it is confined.

---

**★★8.** Classify each observable and name its driver:
(a) the axis direction in space changing secularly;
(b) the axis direction in space varying periodically;
(c) the axis direction moving *in the body*;
(d) the rotation rate changing by fractions of a millisecond per year.

---

## ★★★ Research-oriented

**★★★9.** A rigid-spheroid model gives $H = 0.00335843$ and a free period of
296.945 days. The observed free wobble is longer.

(a) List three physical effects that lengthen it and explain the mechanism of
each.
(b) Explain why a *smaller* $H$ lengthens the period, in terms of the restoring
torque.
(c) State how the observed value must be obtained, and why a textbook value is
not adequate for a modern study.
(d) Explain why the persistence of the free wobble is itself a physical result
about dissipation.

---

**★★★10.** Design a nutation test. You wish to use the observed nutation
amplitudes to constrain the fluid outer core's moment of inertia.

(a) State which torque terms and which Earth-response parameters enter the
nutation amplitudes, and which are already well known.
(b) State the observations needed and their required precision.
(c) Explain why the amplitudes are the diagnostic and not the periods.
(d) State one systematic error that could mimic a core-inertia change, and how
you would distinguish it.
