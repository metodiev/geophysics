# Exercises — 02-05-03 Second Law, Entropy and Irreversibility

Attempt these **closed-book** before opening the
[solutions](./03-second-law-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to [`../code/second_law_demo.py`](../code/second_law_demo.py)
require you to run it and report its actual output.

---

## ★ Foundational

**★1.** One megajoule of heat is delivered to a body at 350 K, and separately to
a body at 1200 K.

(a) Compute the entropy change in each case.
(b) State which delivery does more damage to the availability of the energy, and
why.
(c) Compute the maximum work that could have been extracted by running a
reversible engine between 350 K and a 280 K reservoir.
(d) State, in one sentence, why the answer to (c) is smaller than 1 MJ.

---

**★2.** Heat crosses from a hot boundary at 1200 K to a cold boundary at 280 K,
carrying a flux of 60 mW m⁻².

(a) Compute the entropy produced per unit area and per unit time.
(b) Recompute for a hot boundary at 800 K.
(c) Show explicitly that reversing the direction of the heat gives a negative
entropy production and state what that means physically.
(d) Compute the global entropy production if the whole Earth's surface conducted
like that, using an area of 5.10 × 10¹⁴ m².

---

**★3.** A geothermal plant operates between 180 °C and 20 °C.

(a) Compute the Carnot efficiency.
(b) A real plant on the same resource achieves 9 per cent. Compute the fraction
of the Carnot bound achieved.
(c) Compute the change in Carnot efficiency if the sink is cooled to 5 °C and
state whether that is a realistic engineering option.
(d) State why the Carnot figure is a bound and not a target.

---

**★4.** Crystallising basalt releases $L = 4\times10^5$ J kg⁻¹ at 1500 K, and the
rock has $c_p = 840$ J kg⁻¹ K⁻¹.

(a) Compute the entropy of fusion per kilogram.
(b) Compute the entropy change in heating the rock from 300 K to 1500 K,
$\Delta s = c_p\ln(T_2/T_1)$.
(c) Compute the ratio of (a) to (b) and state what it says about where the
irreversibility is concentrated.
(d) Explain why the ratio is not the fraction of *energy* released as latent heat.

---

## ★★ Applied

**★★5.** Run the demo, Section 2.

(a) Report the entropy production per unit area for the four temperature pairs
tabulated.
(b) Explain why the row with $T_h = T_c$ gives exactly zero.
(c) Explain why $T_h = 1600$ K, $T_c = 283$ K gives more than
$T_h = 800$ K, $T_c = 283$ K for the same flux.
(d) State what would happen physically if a measurement returned a negative value.

---

**★★6.** The lithosphere as an entropy producer.

(a) Derive $\sigma = k|\nabla T|^2/T^2$ from the entropy balance
$\rho\partial s/\partial t + \nabla\cdot(\mathbf q/T) = \sigma$ with
$\mathbf q = -k\nabla T$.
(b) Integrate it for a linear geotherm $T = T_0 + Gz$ and obtain equation (8) of
the lesson.
(c) Evaluate it for $T_0 = 280$ K, $T_H = 1200$ K, $H = 80$ km,
$k = 3.0$ W m⁻¹ K⁻¹.
(d) Explain why the same heat flux concentrated into a steeper gradient produces
more entropy.

---

**★★7.** A district heating scheme takes 90 °C water and delivers heat to
buildings at 60 °C, discarding it at 40 °C. The resource supplies 20 MW thermal.

(a) Compute the Carnot bound between 90 °C and 40 °C.
(b) Compute the exergy (available work) of the 20 MW relative to a 5 °C ambient.
(c) Explain why the scheme is economically sensible despite the low Carnot
efficiency, in second-law language.
(d) Compare with generating electricity from the same resource at 8 per cent
efficiency and state the trade-off.

---

**★★8.** Secular cooling.

(a) Write the entropy production associated with a heat-loss deficit
$\dot Q$ between interior temperature $T_i$ and surface temperature $T_s$.
(b) Evaluate it for $\dot Q = 31$ TW, $T_i = 1600$ K, $T_s = 283$ K.
(c) Compare it with the conductive entropy production of lesson §2.3
($3.9\times10^{10}$ W K⁻¹) and with the radiative figure
($4.56\times10^{14}$ W K⁻¹).
(d) State which of the three is a genuine upper bound on "the Earth's entropy
production" and why the other two are not directly comparable to it.

---

**★★9.** A heat pump delivers 4 kW of heat into a house at 40 °C from a ground
loop at 5 °C, consuming 1 kW of electricity.

(a) Compute the coefficient of performance.
(b) Compute the Carnot bound on the COP.
(c) Verify that the second law is satisfied.
(d) Explain why a COP above the Carnot value would be a perpetual-motion machine.

---

## ★★★ Research-oriented

**★★★10.** The entropy budget of a convecting mantle. Viscous dissipation adds a
term $\sigma_{\text{vis}} = \tau_{ij}\dot\varepsilon_{ij}/T$ to equation (6).

(a) Show dimensionally that $\tau\dot\varepsilon$ is a power per unit volume and
that $\tau\dot\varepsilon/T$ is an entropy production per unit volume per unit
time.
(b) For a mantle with a mean shear stress of $10^6$ Pa and a strain rate of
$10^{-15}$ s⁻¹ at 2000 K, compute $\sigma_{\text{vis}}$.
(c) Integrate over the mantle volume ($8.889\times10^{20}$ m³) and compare with
the conductive entropy production of §2.3 of the lesson.
(d) State what fraction of the mantle's radiogenic and secular heat release is
converted to heat by viscous dissipation, and why that fraction must be
comparable to the ratio of the convective to the total flux. Comment on how
uncertain the answer is.

**★★★11.** Reversibility and the limits of the second law in geophysics.

(a) State the two limits in which a terrestrial heat engine could approach
Carnot, and explain why neither is available to a geothermal plant.
(b) Consider a hypothetical device that extracts heat from the deep Earth at
1600 K and rejects it at 283 K and claim a 90 per cent efficiency. Show
quantitatively that this violates the second law.
(c) A colleague argues that because mantle convection is irreversible, the
mantle "generates" heat and therefore the Earth cannot be cooling. Identify the
error in the reasoning, using the first and second laws.
(d) Explain why the entropy produced by mantle convection is a *smaller*
fraction of the energy transported than the entropy produced by the Earth's
radiation budget, and what sets that fraction.
