# Exercises — 02-10-03 Radiative Transfer, Blackbody Radiation and Kirchhoff's Law

Attempt these **closed-book** before opening the
[solutions](./03-radiative-transfer-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/radiative_transfer_demo.py`](../code/radiative_transfer_demo.py)
require you to run it and report its actual output.

Use $\sigma = 5.670\,374\,419\times10^{-8}$ W m⁻² K⁻⁴ (exact),
$c_2 = hc/k_B = 1.438\,777\times10^{-2}$ m K and
$c_1 = 2hc^2 = 1.191\,043\times10^{-16}$ W m². State units on every answer, and
state when an answer is per micrometre rather than per metre.

---

## ★ Foundational

**★1.** The Planck function at $\lambda = 10\ \mu$m, for $T = 300$ K, 500 K and
1000 K.

(a) Compute $B_\lambda(T)$ at each temperature, in W m⁻² sr⁻¹ µm⁻¹.
(b) Compute the ratio of the 1000 K value to the 300 K value and explain why it
is not the same as the ratio of the fluxes.
(c) Compute the flux $\sigma T^4$ at each temperature.
(d) State which of your three temperatures corresponds to a typical terrestrial
surface and which to a hot geological surface.

---

**★2.** A blackbody is at 300 K, 500 K and 1000 K.

(a) Compute the flux $\sigma T^4$ for each.
(b) Compute the radiative heat-transfer coefficient $4\sigma T^3$ for each.
(c) Compute the wavelength of peak emission for each.
(d) State the ratio of the flux at 1000 K to that at 300 K and comment on the
implication for detecting a hot target against a warm background.

---

**★3.** Wien's law.

(a) Compute the peak wavelength for a body at 400 K.
(b) Compute the temperature of a body whose peak emission is at 4.0 µm.
(c) Compute the peak wavelength of the Sun at 5772 K and state which band it
falls in.
(d) State whether the peak of $B_\nu$ occurs at the frequency $c/\lambda_{\max}$,
and explain.

---

**★4.** A radiometer measures a monochromatic radiance of
8.0 W m⁻² sr⁻¹ µm⁻¹ at 11 µm.

(a) Compute the brightness temperature.
(b) State whether the brightness temperature is above or below the true kinetic
temperature if the surface emissivity is 0.95, and justify the direction without
computing.
(c) Compute the kinetic temperature implied if the emissivity is 0.95 and the
surface is opaque and isothermal.
(d) State the two reasons the answer to (c) may be wrong in the field.

---

## ★★ Applied

**★★5.** Run sections 2 and 3 of
[`../code/radiative_transfer_demo.py`](../code/radiative_transfer_demo.py).

(a) Report the numerically integrated value of $\int x^3/(e^x-1)\,\mathrm dx$
and its relative difference from $\pi^4/15$.
(b) Report $\sigma$ computed from the numerically integrated Planck function and
its relative difference from the exact value.
(c) Report the value of $x$ and of the Wien constant that the demo obtains.
(d) Explain why $\sigma$ may be quoted with all its displayed digits while an
emissivity may not.

---

**★★6.** A rock surface is at 320 K with an emissivity of 0.96 in the thermal
infrared.

(a) Compute its emitted flux.
(b) Compute the brightness temperature if the emissivity is assumed to be 1.
(c) Compute the error introduced by that assumption.
(d) State how the error changes if the emissivity is 0.90 instead, and give the
general rule for the sign and size of the error.

---

**★★7.** An isothermal layer at 265 K with optical depth $\tau = 0.5$ lies above
a black surface at 300 K. The observation is at 11 µm.

(a) Compute the radiance leaving the top of the layer.
(b) Compute the brightness temperature.
(c) Compute the emissivity of the layer.
(d) State which of the surface and the layer dominates the measurement, and what
happens at $\tau = 5$.

---

**★★8.** A planet has an albedo of 0.25 and absorbs a solar constant of
1361 W m⁻².

(a) Compute the effective radiating temperature.
(b) Compute the sensitivity $\mathrm dT_e/\mathrm dS$.
(c) Compute the change in $T_e$ produced by a 1 per cent change in $S$.
(d) Compute the temperature that a grey single-layer atmosphere would predict for
this planet, and state whether a grey model is adequate.

---

## ★★★ Research-oriented

**★★★9.** Derive the radiative transfer equation and its formal solution.

(a) Derive $\mathrm dI/\mathrm d\tau = -I + S$ from the absorption and emission
over a path element, defining each symbol and the sign convention.
(b) Show that for a plane-parallel medium with no scattering and an isothermal
layer over a surface of radiance $I_s$ the emergent radiance is
$I = B(1-e^{-\tau}) + I_se^{-\tau}$.
(c) Show that the emissivity of an isothermal slab is exactly $1-e^{-\tau}$,
identifying which limit of (b) is being used and why the result is a statement of
Kirchhoff's law rather than a definition.
(d) Explain why a scattering medium requires the source function to be modified
and what additional quantity must then be specified.

---

**★★★10.** A single-layer atmosphere of emissivity $\epsilon_a$ in the infrared
and unit transmission in the visible lies over a black surface.

(a) Write the surface energy balance and the top-of-atmosphere balance, and
eliminate the layer temperature to show that

$$T_s = T_e\left(\frac{2}{2-\epsilon_a}\right)^{1/4},
\qquad T_e = \left(\frac{S(1-a)}{4\sigma}\right)^{1/4} .$$

(b) Compute the value of $\epsilon_a$ that reproduces a surface temperature of
288 K for $S = 1361$ W m⁻² and $a = 0.30$.
(c) Compute $T_s$ for $\epsilon_a = 1$ and compare with (b).
(d) Using the band fractions the demo computes at 288 K, explain in terms of the
atmospheric window why the fitted $\epsilon_a$ is less than 1 and why a single
grey emissivity cannot describe the real atmosphere.

---

**★★★11.** A thermal infrared radiometer has a 1 per cent radiance calibration
error.

(a) Compute the temperature error this produces at 8, 10, 12 and 14 µm for a
300 K surface.
(b) State which wavelength is most sensitive to temperature and which is most
sensitive to emissivity, and why those are different questions.
(c) A split-window retrieval uses two bands at 11 and 12 µm. Explain what
information the difference between the two measurements carries.
(d) State the two systematic errors that a split-window algorithm does **not**
remove.
