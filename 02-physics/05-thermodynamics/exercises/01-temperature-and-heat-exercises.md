# Exercises — 02-05-01 Temperature, Heat, Internal Energy and Specific Heat

Attempt these **closed-book** before opening the
[solutions](./01-temperature-and-heat-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/temperature_heat_demo.py`](../code/temperature_heat_demo.py) require
you to run it and report its actual output.

All rock properties in these problems are **nominal** unless a problem states
that a measurement is given. Carry that status through your answers.

---

## ★ Foundational

**★1.** A cubic metre of granite ($\rho = 2700$ kg m⁻³, $c_p = 790$ J kg⁻¹ K⁻¹) is
warmed by 100 K.

(a) Compute the energy required.
(b) Express it in kWh.
(c) A 5 kW heater supplies that energy with no losses. How long does it take?
(d) State whether this is energy or power, and what you had to assume to answer
(c).

---

**★2.** A sandstone has porosity $\phi = 0.20$, mineral density
$\rho_{\min} = 2650$ kg m⁻³, mineral specific heat $c_{\min} = 790$ J kg⁻¹ K⁻¹,
and is fully water-saturated (water: 1000 kg m⁻³, 4186 J kg⁻¹ K⁻¹).

(a) Compute the bulk density.
(b) Compute the volumetric heat capacity of the saturated rock, using the
porosity-weighted mixture rule.
(c) Compute the same for the dry rock.
(d) State the ratio and explain why it is not equal to the ratio of the
densities.

---

**★3.** A basalt has $\alpha = 2\times10^{-5}$ K⁻¹, $K_T = 45$ GPa,
$\rho = 2900$ kg m⁻³ and $c_p = 840$ J kg⁻¹ K⁻¹ at 300 K.

(a) Compute $c_p - c_v$ from $c_p - c_v = \alpha^2TK_T/\rho$.
(b) Express it as a fraction of $c_p$.
(c) State whether the demonstration's Dulong–Petit value for bridgmanite
matches the *measured* room-temperature specific heat of a rock, and explain any
discrepancy.

---

**★4.** A magma with $\rho = 2750$ kg m⁻³ and $c_p = 900$ J kg⁻¹ K⁻¹ cools from
1400 K to 300 K, crystallising with $L = 3.5\times10^5$ J kg⁻¹.

(a) Compute the sensible heat released per cubic metre.
(b) Compute the latent heat released per cubic metre.
(c) Compute the latent fraction of the total.
(d) Explain why the answer to (c) matters more than its numerical value.

---

## ★★ Applied

**★★5.** Compute the Dulong–Petit specific heat of forsterite, Mg₂SiO₄
($M = 140.69$ g mol⁻¹, 7 atoms per formula unit), and compare it with the nominal
mantle value of 1250 J kg⁻¹ K⁻¹. State the regime in which the comparison is
expected to hold and what happens at 100 K.

---

**★★6.** Run the demo and read Section 3.

(a) Report the stored energy of a 1 km³ magma body cooling 1500 → 300 K, and the
latent part of it.
(b) Convert it to GW-years and state the conversion you used.
(c) If the body delivers that energy over 10 000 years, what average power does
that represent, in MW?
(d) Explain, in two sentences, why the answer to (c) is not a property of the
magma.

---

**★★7.** An aquifer-based thermal store occupies 1 km² of ground 50 m thick, is
fully saturated, and is cycled through $\Delta T = 10$ K. Use the rock properties
of ★2.

(a) Compute the rock volume and the total energy stored.
(b) Express it in GWh.
(c) Compute the number of 100 m² detached houses (peak heating load 5 kW each)
that this could supply for 8 hours per day for 100 days, ignoring losses.
(d) State the three assumptions that dominate the answer's uncertainty.

---

**★★8.** A magma crystallises over an interval $\Delta T_{\text{xtal}}$ rather
than at a single temperature.

(a) Write the effective volumetric heat capacity inside the interval, including
latent heat.
(b) Compute the plateau factor (the ratio of effective to sensible heat capacity)
for $\Delta T_{\text{xtal}} = 200$ K and for 50 K, using the properties of ★4.
(c) Explain why the factor is larger for a narrower interval.
(d) State why the plateau is not perfectly flat in a real magma.

---

**★★9.** Uncertainty in the heat content of a rock body.

(a) Write the fractional uncertainty in $Q = \rho c_p V\Delta T$ in terms of the
fractional uncertainties in $\rho$, $c_p$, $V$ and $\Delta T$, assuming they are
independent.
(b) With $\rho$ known to 3 per cent, $c_p$ to 10 per cent, $V$ to 15 per cent and
$\Delta T$ to 2 per cent, compute the total.
(c) State which term dominates and what measurement would most improve the
answer.

---

## ★★★ Research-oriented

**★★★10.** The Dulong–Petit limit is a high-temperature result, and the low-
temperature behaviour is governed by the Debye model, whose low-$T$ limit is

$$c_v \to \frac{12\pi^4}{5}\,nR\left(\frac{T}{\Theta_D}\right)^3 .$$

(a) Evaluate the coefficient $12\pi^4/5$ and verify it equals 233.78.
(b) Compute $c_v$ for forsterite at $T = \Theta_D/10$ with $\Theta_D = 500$ K.
(c) Compute it at $T = \Theta_D/20$ and verify the $T^3$ scaling between the two.
(d) State carefully why this single-$\Theta_D$ formula is an idealisation for a
complex silicate, and what a real heat-capacity measurement would show instead.
Do not quote a measured value you have not verified.

**★★★11.** Latent heat and the shape of a cooling curve. A 100 m thick sill has
$\rho = 2750$ kg m⁻³, $c_p = 900$ J kg⁻¹ K⁻¹ and $L = 3.5\times10^5$ J kg⁻¹.

(a) Compute the total heat released per unit area of sill, per unit temperature
of sensible cooling over 1100 K, plus the latent heat.
(b) Assume conduction removes heat at a constant 100 W m⁻² from both faces.
Compute the time to release the total.
(c) Compute the fraction of that time spent inside a 100 K crystallisation
interval, and hence the plateau duration.
(d) State which of your assumptions is the most severe in a real sill, and what
happens to the cooling curve when it fails.
