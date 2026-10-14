# Exercises — 02-02-07 Central Forces, Orbits and the Earth-Moon-Sun System

Attempt these **closed-book** before opening the
[solutions](07-central-forces-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Use $GM_\oplus = 3.986\,004\,418\times10^{14}$ m³ s⁻² (defining, WGS 84) and
$R = 6\,371$ km (nominal). Where an astronomical or measured quantity is needed,
state it as an input and say where it must be obtained. State a regime of
validity with every numerical answer in ★★ and ★★★.

---

## ★ Foundational

**★1.** (a) Show that the torque about the centre for a central force vanishes.
(b) Deduce that angular momentum is conserved and that the motion is planar.
(c) Show that the areal velocity is $L/2m$.

---

**★2.** A satellite orbits at 400 km altitude. (a) Compute the orbital speed and
the period, and convert the period to hours. (b) Compute the specific orbital
energy. (c) State whether the orbit is bound.

---

**★3.** (a) State Kepler's third law in terms of $\mu = GM$. (b) Compute the
period of a circular orbit with $a = 26\,600$ km. (c) Verify that $T^{2}/a^{3}$
equals $4\pi^{2}/\mu$ for both this orbit and the 400 km orbit.

---

**★4.** (a) Write vis-viva. (b) Compute the speed at periapsis and apoapsis for an
orbit with $a = 10^{7}$ m and $e = 0.3$. (c) Compute the ratio
$v_{\text{peri}}/v_{\text{apo}}$ and derive it from the orbit geometry.

---

## ★★ Applied

**★★5.** (a) Invert Kepler's third law to express $GM$ in terms of $a$ and $T$.
(b) For a satellite at $a = 26\,600$ km and $T$ as computed in ★3, compute $GM$
and compare with the defining value. (c) Compute the relative sensitivity
$\delta(GM)/GM$ for a 1 m error in $a$ and for a 1 ms error in $T$. (d) Explain
why this method gives $GM$ far better than dividing it by $G$ would give the mass.

---

**★★6.** The shell theorem and its look-alikes.

(a) State the shell theorem, including the interior case.
(b) Write the field of a point mass at depth $d$ observed at horizontal offset
$\rho$, and the field of a uniform sphere of mass $M$ and radius $a$ observed at
distance $z \ge a$.
(c) For a compact body of mass $M$ at depth $d = 500$ m, compare the point-mass
profile at $\rho = 0$ and $\rho = 500$ m; then compute the fractional error made
by using the point-mass formula for a *sphere of radius* $a = 100$ m at
$\rho = 0$ (i.e. treating a 100 m sphere as a point at its centre of 500 m).
(d) State the general rule for choosing between the formulas.

---

**★★7.** An eccentric orbit has $a = 10^{7}$ m and $e = 0.3$.
(a) Compute the periapsis and apoapsis distances. (b) Compute the period.
(c) Compute the specific energy. (d) Compute the semi-latus rectum two ways
($a(1-e^{2})$ and $h^{2}/\mu$ using the periapsis values) and confirm they agree.

---

**★★8.** The Earth–Moon system. (a) Write the two-body $\mu$ and explain how it
differs from $GM_\oplus$. (b) State which body's orbit the barycentre lies inside,
and why "the Moon orbits the Earth" is a convenient fiction. (c) Explain the
angular-momentum exchange in one paragraph, using the words *tide*,
*delay* and *torque*. (d) State which numbers in that story are measured and
therefore must be taken from IERS rather than derived here.

---

## ★★★ Research-oriented

**★★★9.** $J_2$ and orbit precession. For an Earth oblateness term with
$\mu J_2 = 1.08\times10^{-3}\mu$ (take $J_2$ as a given measured input), the nodal
regression rate is approximately
$\dot\Omega = -\tfrac32 J_2 (R/p)^{2}n\cos i$.

(a) Compute $\dot\Omega$ in degrees per day for a 500 km orbit at inclinations 0°,
53°, 90° and 98°.
(b) Find the inclination for a sun-synchronous orbit (state the required rate and
where it comes from).
(c) Explain why the nodal regression is a *signal* in satellite geodesy rather
than a nuisance.
(d) State the perturbation that becomes larger than $J_2$ as the orbit rises, and
at roughly what altitude the crossover lies.

---

**★★★10.** Tidal acceleration as a field gradient.

(a) Show that the differential acceleration between the centre of the Earth and a
point displaced by $R_\oplus$ towards the Moon scales as $GM_mR_\oplus/d^{3}$.
(b) Express the ratio of the tidal acceleration to the Moon's central
acceleration at the Earth, and compute its order of magnitude using
$R_\oplus/d \sim 10^{-2}$.
(c) Explain why the tides are semi-diurnal rather than diurnal, using the two
bulges of the tidal field.
(d) State which part of this is a model and which is measured.
