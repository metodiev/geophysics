# Exercises — 02-05-05 Convection, Radiation and Combined Heat Transfer

Attempt these **closed-book** before opening the
[solutions](./05-convection-radiation-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/convection_radiation_demo.py`](../code/convection_radiation_demo.py)
require you to run it and report its actual output.

---

## ★ Foundational

**★1.** A magma chamber is 2 km thick with $\Delta T = 300$ K,
$\rho = 2600$ kg m⁻³, $\alpha = 5\times10^{-5}$ K⁻¹, $\kappa = 10^{-6}$ m² s⁻¹ and
$\eta = 10^4$ Pa s.

(a) Compute the Rayleigh number, using $g = 9.806\,65$ m s⁻².
(b) Compute the critical value ratio.
(c) Compute Nu from $\mathrm{Nu} = 0.1\,\mathrm{Ra}^{1/3}$.
(d) State whether the chamber is in the conductive or the convective regime, and
whether the answer would change if $\eta$ were $10^8$ Pa s.

---

**★2.** Compute $\sigma T^4$ and $4\sigma T^3$ at $T = 500$ K, using
$\sigma = 5.670\,374\,419\times10^{-8}$ W m⁻² K⁻⁴.

(a) Give both values with units.
(b) State which quantity is the flux and which is the heat-transfer coefficient.
(c) Compare $4\sigma T^3$ with a typical natural-convection coefficient in air of
15 W m⁻² K⁻¹ and state which mode dominates.
(d) State the two physical assumptions behind $\sigma T^4$ and what a real rock
surface does differently.

---

**★3.** The Earth's effective radiating temperature.

(a) Write $T_e$ in terms of the absorbed flux.
(b) Compute $T_e$ for albedo 0.20, 0.25, 0.30 and 0.35 with $S = 1361$ W m⁻²
(adopted).
(c) Compute the change in $T_e$ between albedo 0.35 and 0.25.
(d) Explain why a change in albedo is a first-order climate lever while the
geothermal flux is not.

---

**★4.** Wien's law.

(a) Compute Wien's constant from $h$, $c$, $k_B$ and $x = 4.965\,114$.
(b) Compute the peak wavelength for $T = 1000$ K, 288 K and 5772 K.
(c) State which band each falls in.
(d) Explain why the Sun's and the Earth's spectra barely overlap and what
geophysical consequence follows.

---

## ★★ Applied

**★★5.** Run the demo, Sections 1 and 2.

(a) Report Ra and Nu for the four systems.
(b) Report $q_{\text{cond}}$ and $q_{\text{conv}}$ for the whole mantle.
(c) Compare the mantle $q_{\text{conv}}$ with the observed global mean heat flow
of ~90 mW m⁻² and state the accuracy honestly.
(d) State three ways the real mantle violates the assumptions of equation (11).

---

**★★6.** A lava lake 5 m deep, with $\Delta T = 300$ K, $\rho = 2600$ kg m⁻³,
$\alpha = 5\times10^{-5}$ K⁻¹, $\kappa = 10^{-6}$ m² s⁻¹ and
$\eta = 100$ Pa s.

(a) Compute Ra and Nu.
(b) Compute the conductive flux and the convective flux.
(c) Compute the radiative flux at 1400 K.
(d) Rank the three and state which mechanism controls the lake's heat loss.

---

**★★7.** Groundwater and heat flow.

(a) Write the Péclet number and define each symbol.
(b) For $\kappa = 1.157\times10^{-6}$ m² s⁻¹ and $L = 2$ km, compute the velocity
at which $\mathrm{Pe} = 1$, in m yr⁻¹.
(c) A fault zone transmits 0.05 m yr⁻¹. Compute Pe.
(d) Explain how a hydrothermal system can carry a heat flux far above the
conductive value through rock whose $k$ has not changed.

---

**★★8.** Run the demo, Sections 6 and 7.

(a) Report the value of Wien's constant the demo computes.
(b) Report the crossover velocity for $\mathrm{Pe} = 1$ at $L = 1$ km.
(c) State which number in (b) you would quote to a hydrogeologist and why.
(d) Explain why the Péclet number is the wrong tool for the mantle and what is
used instead.

---

**★★9.** A basalt flow has a surface at 1100 K and air at 290 K above it.

(a) Compute the radiative flux, assuming $\epsilon = 1$.
(b) Compute it with $\epsilon = 0.9$ and state the change.
(c) Compute the convective flux with $h = 12$ W m⁻² K⁻¹.
(d) Compute the share of each and state what happens to the ranking as the surface
cools to 600 K.

---

## ★★★ Research-oriented

**★★★10.** Boundary-layer scaling.

(a) Derive $\delta \sim d\,\mathrm{Ra}^{-1/3}$ from the marginal-stability
condition $\rho g\alpha\Delta T\delta^3/(\kappa\eta) \sim \mathrm{Ra}_c$.
(b) Hence derive $\mathrm{Nu} \sim \mathrm{Ra}^{1/3}$ with the prefactor
$0.1$.
(c) Compute $\delta$ and $q_{\text{conv}}$ for the mantle of the demo.
(d) State four assumptions of the derivation and, for each, what the real mantle
does instead. Estimate whether each failure makes the real flux larger or smaller
than the scaling predicts.

**★★★11.** Radiative transfer versus a grey atmosphere.

(a) Show that a planet with a single-layer atmosphere of emissivity 1 in the
infrared and 0 in the visible has a surface temperature
$T_s = 2^{1/4}T_e$.
(b) Compute $T_s$ for $T_e = 255$ K.
(c) Explain why the real Earth's $T_s$ is 288 K rather than your answer to (b),
in terms of the wavelength dependence of atmospheric absorption.
(d) State why a single grey emissivity cannot reproduce both the absorbed solar
and the emitted terrestrial fluxes.
