# Exercises — 02-05-02 First Law, Work and Energy Balances

Attempt these **closed-book** before opening the
[solutions](./02-first-law-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to [`../code/first_law_demo.py`](../code/first_law_demo.py)
require you to run it and report its actual output.

Use the geophysical sign convention throughout: $\mathrm{d}U = \delta Q -
\delta W$, with $\delta Q > 0$ into the system and $\delta W > 0$ done by the
system. State it in every answer.

---

## ★ Foundational

**★1.** A closed system undergoes two steps. Step 1: $Q = +2.0$ MJ,
$W = +1.2$ MJ. Step 2: $Q = -0.5$ MJ, $W = +0.8$ MJ.

(a) Compute $\Delta U$ for each step.
(b) Compute the cycle total and state what it must be.
(c) State what would have to change in the sign convention for your answer to
(b) to differ, and whether the physics would change.

---

**★2.** A rock has $\alpha = 3\times10^{-5}$ K⁻¹, $T = 1500$ K,
$\rho = 3300$ kg m⁻³, $c_p = 1250$ J kg⁻¹ K⁻¹.

(a) Compute the adiabatic gradient $\mathrm{d}T/\mathrm{d}P$ in K GPa⁻¹.
(b) Convert it to $\mathrm{d}T/\mathrm{d}z$ in K km⁻¹.
(c) Compute the temperature change of a parcel descending 50 km.
(d) State whether this heating could create a mantle plume on its own, with
reasoning rather than a one-word answer.

---

**★3.** A geothermal well produces 80 kg s⁻¹ of water dropping from 180 °C to
40 °C, with $c_p = 4186$ J kg⁻¹ K⁻¹.

(a) Compute the thermal power.
(b) If the conversion efficiency is 11 per cent, compute the electrical output
and the rejected heat.
(c) Verify that the first law is satisfied.
(d) Compute the Carnot bound for these temperatures and state what the gap
represents.

---

**★4.** State, for each of the following, whether $H$ or $U$ is the natural state
function, and why: (i) a closed parcel of mantle rock, (ii) a flowing geothermal
wellbore, (iii) a magma chamber losing heat to its walls at constant volume.

---

## ★★ Applied

**★★5.** Run the demo, Section 2.

(a) Report $\mathrm{d}T/\mathrm{d}P$ and $\mathrm{d}T/\mathrm{d}z$ for the mantle,
the crust and the outer core.
(b) Report the dry atmospheric value.
(c) Explain the factor of ~26 between the mantle and the atmospheric gradients in
terms of $\alpha$.
(d) Explain why the *crustal* solid gradient is *smaller* than the mantle's even
though the crust is colder.

---

**★★6.** A hydrothermal system circulates 50 kg s⁻¹ of water through an aquifer,
heating it by 60 K at a depth of 2 km.

(a) Compute the advected heat transport rate.
(b) The recharge water cools by 30 K on the way down through the rock (a closed
system). Compute the enthalpy change per kilogram and the total.
(c) Compare the two rates and explain what the difference represents.
(d) State whether the recharge leg's temperature change is adiabatic or
conductive, and why that matters.

---

**★★7.** A geothermal plant of 12 MWe operates on a reservoir at 220 °C with a
25 °C sink.

(a) Compute the Carnot bound.
(b) Compute the thermal input required for the stated output at 40 per cent of
Carnot, and then at 60 per cent.
(c) Compute the mass flow required in each case for a 160 K temperature drop with
$c_p = 4186$ J kg⁻¹ K⁻¹.
(d) State which engineering choice the difference between the two answers governs.

---

**★★8.** Chemical and phase-change energy budgets.

(a) For 1 m³ of basalt ($\rho = 2900$ kg m⁻³, $c_p = 840$ J kg⁻¹ K⁻¹,
$L = 4\times10^5$ J kg⁻¹), compute the sensible heat released cooling from
1500 K to 300 K.
(b) Compute the latent heat.
(c) Write the continuum heat equation with latent heat represented as an extra
term in the effective heat capacity, and state the interval over which it must be
applied.
(d) Explain why a first-law audit of a magma-chamber model that omits latent heat
still "balances" and yet gives the wrong answer.

---

**★★9.** Internal heat generation.

(a) Write the steady 1-D heat equation with an exponentially decaying source
$A(z) = A_0e^{-z/h}$ using $z$ downward.
(b) Integrate it once and impose $\mathrm{d}T/\mathrm{d}z = q_0/k$ at $z = 0$ to
obtain $\mathrm{d}T/\mathrm{d}z$.
(c) Show that $\mathrm{d}T/\mathrm{d}z$ tends to a constant as $z\gg h$ and
identify that constant physically.
(d) With $A_0 = 1.5$ µW m⁻³ and $h = 12$ km, compute the contribution of the
radiogenic layer to the surface heat flow.

---

## ★★★ Research-oriented

**★★★10.** The adiabat with a phase transition. A rising parcel passes through a
transition that absorbs latent heat $L$ at mass fraction $f$.

(a) Write the first law for the parcel including the latent term and show that the
effective heat capacity becomes $c_p^{\text{eff}} = c_p + L\,f/(\Delta T)$, where
$\Delta T$ is the temperature interval over which the transition occurs.
(b) Compute the ratio $c_p^{\text{eff}}/c_p$ for a transition with
$L = 3\times10^4$ J kg⁻¹ released over 20 K.
(c) Compute the resulting adiabatic gradient relative to the transition-free case
and state whether the adiabat becomes flatter or steeper at the transition.
(d) Explain how this produces a "step" in the mantle adiabat that is detectable in
the seismic velocities, and what other observational signature accompanies it.

**★★★11.** Joule–Thomson and wellbore enthalpy. For a fluid flowing through a
throttle with no work and no heat exchange, $h$ is constant.

(a) State why $\mathrm{d}h = 0$ and what happens to the temperature when
$(\partial h/\partial P)_T \ne 0$.
(b) For a flashing geothermal fluid entering a separator at 200 °C and leaving at
150 °C, explain in first-law terms where the energy for vapour production comes
from, given that the separator adds no heat.
(c) Compute the fraction of liquid that flashes, given the enthalpy of saturated
liquid at 200 °C and 150 °C ($h_f$) and of saturated vapour at 150 °C ($h_g$),
using $x = (h_{f,1} - h_{f,2})/(h_{g,2} - h_{f,2})$. Adopt values from a steam
table you can cite, state them, and show the arithmetic.
(d) State two assumptions of the calculation and where each fails in a real
separator.
