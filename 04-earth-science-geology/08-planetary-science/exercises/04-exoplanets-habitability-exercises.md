# Exercises — 04-08-04 Exoplanets, Habitability and Observational Constraints

Attempt these **closed-book** before opening the
[solutions](./04-exoplanets-habitability-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Take $G = 6.6743\times10^{-11}$ m³ kg⁻¹ s⁻²,
$GM_\odot = 1.327\,124\,4\times10^{20}$ m³ s⁻², $1\ \mathrm{au}
= 1.495\,978\,707\times10^{11}$ m, $R_\odot = 6.957\times10^8$ m,
$R_\oplus = 6.371\times10^6$ m, $M_\oplus = 5.9722\times10^{24}$ kg,
$L_\odot = 3.828\times10^{26}$ W and
$\sigma = 5.670\,374\times10^{-8}$ W m⁻² K⁻⁴.

Problems referring to
[`../code/exoplanets_demo.py`](../code/exoplanets_demo.py) require you to run it
and report its actual output.

---

## ★ Foundational

**★1.** A planet with $R_p = 0.02R_*$ transits its star.

(a) Compute the transit depth in parts per million.
(b) Compute the depth for $R_p = 0.1R_*$.
(c) State what the depth depends on and what it does not.
(d) State why a depth of 84 ppm is a space-instrument problem.

---

**★2.** A planet orbits a Sun-like star at $a = 0.1$ au.

(a) Compute the orbital period.
(b) Compute the geometric transit probability.
(c) Compute the transit duration for a central transit.
(d) State whether the probability or the period contributes more to the detection
yield at small $a$, and why.

---

**★3.** A planet of 5 Earth masses orbits a solar-mass star at 0.1 au in a
circular orbit.

(a) Compute the radial-velocity semi-amplitude using the scaling
$K \propto m_pP^{-1/3}$, given $K = 0.0894$ m s⁻¹ for an Earth-mass planet at
1 au.
(b) Compute the signal-to-noise relative to a stellar jitter of 1 m s⁻¹.
(c) State whether (a) is a mass or a minimum mass, and why.
(d) State what additional measurement resolves the ambiguity.

---

**★4.** Orbits are oriented isotropically.

(a) Derive $\mathrm{E}[\sin i]$ and evaluate it.
(b) Derive $\mathrm{E}[1/\sin i]$ and evaluate it.
(c) Compute the fraction of orbits with $\sin i < 0.3$.
(d) A survey reports a set of minimum masses whose mean is
$3\ M_\oplus$. Compute the expected mean true mass, and state the assumption.

---

## ★★ Applied

**★★5.** Run the demo's sections 1 and 2.

(a) Report the transit depths for $R_p/R_\oplus = 1$, 2, 4 and 11.2.
(b) Report the transit probabilities at 0.05, 0.2 and 1 au.
(c) Report the RV semi-amplitude for a one-Earth-mass planet at 1 au and at
0.05 au, and the mass required for $K = 1$ m s⁻¹ at each.
(d) State in one sentence why the observed exoplanet population is dominated by
close-in planets, using (b) and the period.

---

**★★6.** Run the demo's sections 4 and 5.

(a) Report the Monte Carlo means of $\sin i$ and $1/\sin i$ and their analytic
values.
(b) Report the fraction with $\sin i < 0.5$ and its analytic value.
(c) Report the freezing and boiling boundaries of the naive habitable zone, and
the same boundaries with 33 K of greenhouse warming.
(d) Report the measured mass–radius exponent and the two limiting exponents, and
state why the exponent is evidence that the model is behaving sensibly.

---

**★★7.** A planet's transit depth is known precisely, but the stellar radius is
uncertain by 8 per cent and the stellar mass by 2 per cent.

(a) Compute the planet's radius uncertainty.
(b) Compute the density uncertainty from (8).
(c) Compute the stellar radius precision required for a total density uncertainty
of 10 per cent, given the 2 per cent mass error.
(d) State which quantity in this problem should be reported first in an abstract,
and why.

---

## ★★★ Research-oriented

**★★★8.** The habitable zone depends on quantities that are not measured.

(a) Compute $T_\mathrm{eq}$ at 1 au for albedos of 0.1, 0.3 and 0.5.
(b) Compute the heliocentric distance at which $T_\mathrm{eq} = 273$ K for each
albedo, and express the range as a percentage of the middle value.
(c) A planet with $T_\mathrm{eq} = 255$ K has an atmosphere supplying 33 K of
warming; compute the distance at which a *bare* body with the same flux would
reach 273 K, and state what this says about the inner edge of the conventional
habitable zone.
(d) Discuss, in no more than six sentences, what observational measurement would
most reduce the uncertainty in a habitability assessment, and what model it would
still leave unconstrained.

---

**★★★9.** Two planets have the same mass of $5\ M_\oplus$ but different bulk
compositions: one is pure silicate with a zero-pressure density of
3500 kg m⁻³ and the other has a 50 per cent water-ice envelope with an
uncompressed mixture density of 1556 kg m⁻³.

(a) Compute the radius each would have if it did not compress, from
$R = (3M/4\pi\rho)^{1/3}$.
(b) State the sign of the error introduced by ignoring compression, and why it is
in that direction.
(c) The self-compressed silicate model of the demo gives 11 287 km for
5 Earth masses. Compute the fractional radius difference between the two
compositions using your uncompressed values, and state the radius precision a
mission would need to distinguish them.
(d) Discuss, in no more than six sentences, why a radius and a mass still do not
establish a composition, and what an atmospheric spectrum would add.
