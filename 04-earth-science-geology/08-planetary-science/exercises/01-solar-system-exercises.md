# Exercises — 04-08-01 Solar System Architecture and Formation

Attempt these **closed-book** before opening the
[solutions](./01-solar-system-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Take $G = 6.6743\times10^{-11}$ m³ kg⁻¹ s⁻², $1\ \mathrm{au}
= 1.495\,978\,707\times10^{11}$ m, $L_\odot = 3.828\times10^{26}$ W,
$\sigma = 5.670\,374\times10^{-8}$ W m⁻² K⁻⁴, $k = 1.380\,649\times10^{-23}$
J K⁻¹ and $1\ \mathrm{u} = 1.660\,539\times10^{-27}$ kg.

Problems referring to
[`../code/solar_system_demo.py`](../code/solar_system_demo.py) require you to run
it and report its actual output.

---

## ★ Foundational

**★1.** A body orbits the Sun at 2.5 au.

(a) Compute its orbital period using $T^2 = 4\pi^2a^3/(GM)$ with
$GM_\odot = 1.327\,124\,4\times10^{20}$ m³ s⁻².
(b) Compute its orbital speed.
(c) Check (b) against the scaling $v \propto a^{-1/2}$ using the Earth's
29.79 km s⁻¹.
(d) State which of the inputs in (a) is measured and which is defined.

---

**★2.** Take an albedo of 0.3.

(a) Compute the equilibrium temperature at 0.39, 1.0 and 5.2 au.
(b) State where the factor of 4 in the flux balance comes from.
(c) The Earth's measured mean surface temperature is about 288 K. Compute the
greenhouse increment.
(d) State why (c) is a measurement of the atmosphere rather than of the surface.

---

**★3.** Water ice is stable against sublimation over geological times below
about 170 K at low pressure.

(a) Compute the heliocentric distance at which $T_\mathrm{eq} = 170$ K.
(b) Compute it for 200 K and for 273 K.
(c) State why the giant planets are all beyond the outer of these distances and
what that has to do with their formation.
(d) State two quantities the answer depends on that are not properties of the
planet.

---

**★4.** A body has $GM = 4.9\times10^{12}$ m³ s⁻² and a radius of
$1.5\times10^6$ m.

(a) Compute its escape speed.
(b) Compute the thermal speed of CO₂ (44.009 u) at 300 K.
(c) Compute the Jeans parameter $\lambda$ and state whether CO₂ is retained by
the criterion $\lambda > 25$.
(d) State what happens to $\lambda$ if the temperature is doubled, and why the
dependence is what it is.

---

## ★★ Applied

**★★5.** Run the demo's section 1.

(a) Report the derived $GM_\odot$ and the tabulated value, and the relative
difference.
(b) Report the value of $GM_\text{Earth} + GM_\text{Moon}$ and the fraction of
$GM_\odot$ it represents, and explain what the coincidence means.
(c) Compute the orbital period of a body at 3 au and the orbital speed at that
distance.
(d) State why the sidereal year is needed rather than the tropical year, in one
sentence.

---

**★★6.** Run the demo's section 4.

(a) Report $\lambda$ for H₂, He, N₂ and CO₂ on the Earth at 1000 K and the
retention verdict for each.
(b) Compute the exospheric temperature at which $\lambda = 25$ for H₂ on the
Earth, and compare it with the Earth's actual exospheric temperature of order
1000 K.
(c) Report the water-on-Mars case and explain why the criterion's answer is
wrong.
(d) State what the criterion is useful for, given that it can be wrong.

---

**★★7.** Run the demo's section 3.

(a) Report the total planetary orbital angular momentum, Jupiter's share and the
Sun's mass share.
(b) Report the Sun's angular-momentum share for the two moment-of-inertia
coefficients.
(c) Compute the orbital angular momentum of a one-Earth-mass body at 30 au and
compare it with Neptune's.
(d) State the angular-momentum problem in one sentence, and state which parts of
your answer to (b) are robust.

---

## ★★★ Research-oriented

**★★★8.** A body is made of rock ($\rho = 3500$ kg m⁻³) and ice
($\rho = 1000$ kg m⁻³), with an ice mass fraction of 0.40.

(a) Compute its uncompressed mean density from the two-component mixing relation.
(b) A spacecraft measures a mean density 20 per cent higher than (a), because the
body is self-compressed. Invert the uncompressed relation for the implied ice
mass fraction, and state the error.
(c) Repeat (b) for a 10 per cent compression.
(d) State, in no more than five sentences, why the same measured density
corresponds to a range of compositions and what a mission would need in order to
narrow it.

---

**★★★9.** The ice line scales with the star's luminosity.

(a) Derive the scaling of the ice-line distance with $L$ at fixed condensation
temperature.
(b) Compute the ice-line distance for $T_\mathrm{eq} = 170$ K around stars of
$0.1$, $1$ and $10\ L_\odot$.
(c) Derive how the equilibrium temperature at a fixed distance scales with $L$
and explain the consequence for the habitable zone of a low-mass star.
(d) State one reason the ice line in a real disk is not simply the distance at
which $T_\mathrm{eq}$ equals a condensation temperature.
