# Exercises — 02-11-04 Atmospheric Structure, Hydrostatic Balance and Lapse Rates

Attempt these **closed-book** before opening the
[solutions](./04-atmospheric-structure-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/atmospheric_structure_demo.py`](../code/atmospheric_structure_demo.py)
require you to run it and report its actual output.

**Every problem that asks for a temperature, a pressure or a height requires you
to state whether you assumed an isothermal layer, a constant lapse rate, or the
standard atmosphere's defined profile.** Sea-level pressure 101 325 Pa and
standard gravity 9.806 65 m s⁻² are **exact** by definition; the molar mass of air
and $c_p$ are **nominal**; the standard atmosphere's layer structure is a
**defined standard**.

---

## ★ Foundational

**★1.** With $R_{\text{air}} = R/M_{\text{air}} = 8.314\,462\,618\,153\,24/0.028\,9644
= 287.058$ J kg⁻¹ K⁻¹ and $g = 9.806\,65$ m s⁻²:

(a) Compute the scale height $H = R_{\text{air}}T/g$ at $T = 288.15$ K and at
$T = 300$ K.
(b) State the height over which the pressure falls by a factor of $e$ and the
height over which it halves, for an isothermal atmosphere.
(c) Compute the fraction of the atmosphere's mass lying below $H$, $2H$ and $3H$.
(d) State one reason why the scale height for water is not defined by the same
formula.

---

**★2.** The dry adiabatic lapse rate.

(a) Starting from $\mathrm{d}h = v\,\mathrm{d}P$ for an adiabatic parcel,
$\mathrm{d}h = c_p\,\mathrm{d}T$ for an ideal gas, and
$\mathrm{d}P = -\rho g\,\mathrm{d}z$ for the environment, derive
$\Gamma_d = g/c_p$.
(b) Evaluate it for $g = 9.806\,65$ m s⁻² and $c_p = 1005$ J kg⁻¹ K⁻¹.
(c) Verify the same value from
$\Gamma_d = \frac{\gamma-1}{\gamma}\cdot\frac{g}{R_{\text{air}}}$ with
$\gamma = 1.4$.
(d) Name the four assumptions of the derivation and say which one fails in a
cloud.

---

**★3.** An isothermal atmosphere at $T = 288.15$ K has $p_0 = 101\,325$ Pa at
$z = 0$.

(a) Compute $p$ at 5.5 km.
(b) Compute the height at which $p = p_0/2$.
(c) Explain why this is *not* the correct pressure at 5.5 km in the real
troposphere.
(d) A student says "the pressure at 5.5 km is half the surface pressure because
$e^{-z/H} = 1/2$". Identify what is right and what is wrong in that statement.

---

**★4.** Potential temperature and stability.

(a) Define potential temperature and state its physical meaning.
(b) Show that $\mathrm{d}\theta/\mathrm{d}z > 0$ implies stability, and state
against which adiabat.
(c) Write $N^2$ in terms of $g$, $T$, $\Gamma_d$ and $\Gamma$, and state the
meaning of each sign of $N^2$.
(d) A layer has $T = 250$ K and an actual lapse rate of 12 K km⁻¹. Compute $N^2$
and state what happens to the layer.

---

## ★★ Applied

**★★5.** The power law for a constant lapse rate.

(a) Integrate $\mathrm{d}P/P = -g\,\mathrm{d}z/(R_{\text{air}}T)$ with
$T = T_0+\Gamma' z$ (where $\Gamma' = \mathrm{d}T/\mathrm{d}z$) to obtain
$p = p_0(T/T_0)^{g/(\Gamma R_{\text{air}})}$ with
$\Gamma = -\mathrm{d}T/\mathrm{d}z$.
(b) Evaluate the exponent $g/(R_{\text{air}}\Gamma)$ for the standard troposphere
with $\Gamma = 6.5$ K km⁻¹.
(c) Compute $p$ at 5 km in the standard troposphere.
(d) Compare with the isothermal value at 5 km and explain the direction of the
difference.

---

**★★6.** A dry-adiabatic troposphere. Suppose the tropospheric lapse rate were
$\Gamma_d = 9.758$ K km⁻¹ instead of 6.5 K km⁻¹, with the same surface conditions.

(a) Compute $T$ at 5 km.
(b) Compute $p$ at 5 km using the power law with the dry-adiabatic exponent.
(c) Compare with the standard-atmosphere value and explain the direction.
(d) Compute $N^2$ at the surface for this profile and state what it means for the
layer's stability.

---

**★★7.** The standard atmosphere's pressures.

(a) State the seven breakpoint heights and lapse rates of the standard atmosphere
and the sea-level conditions.
(b) Integrate layer by layer to obtain the pressure at 11 km, 20 km and 32 km.
(c) Report the fraction of the surface pressure at each of those heights.
(d) Explain why the temperature at 20 km is the same as at 11 km, and what the
lapse rate between them is.

---

**★★8.** The atmosphere's mass.

(a) Derive $M_{\text{atm}} = 4\pi R^2p_0/g$ from hydrostatic balance.
(b) Evaluate it for the Earth and express it as a fraction of
$M_\oplus = 5.972\times10^{24}$ kg.
(c) Evaluate it for a body of the same radius but $g = 3.71$ m s⁻², and explain
the direction of the change.
(d) State the two assumptions that limit (b), and the direction of the error each
introduces.

---

## ★★★ Research-oriented

**★★★9.** Another planet's atmosphere. A body has a CO₂ atmosphere with molar
mass 44.01 g mol⁻¹, surface temperature 210 K and $g = 3.71$ m s⁻².

(a) Compute $R_{\text{specific}}$ for CO₂.
(b) Compute the scale height.
(c) Estimate the dry adiabatic lapse rate using $c_p \approx 843$ J kg⁻¹ K⁻¹,
and state the assumption.
(d) Compare the scale height with the Earth's at similar temperature and explain
the difference in terms of the formula.

---

**★★★10.** Stability through the real profile.

(a) Using the demo's output, report $\theta$ at 0, 5, 11 and 47 km.
(b) Report $N$ at the same heights and the corresponding buoyancy periods.
(c) Explain why $N$ approximately doubles across the tropopause, using
$N^2 = (g/T)(\Gamma_d-\Gamma)$.
(d) A colleague says "the troposphere is unstable because temperature decreases
with height". Refute that in two sentences using your answers to (a).

---

**★★★11.** Why the observed lapse rate is not the dry adiabat.

(a) State the observed tropospheric value (6.5 K km⁻¹) and the dry adiabat
(9.758 K km⁻¹) and compute the ratio.
(b) Explain the role of latent heat, and describe qualitatively how the *moist*
adiabatic lapse rate depends on temperature.
(c) Explain the role of radiative-convective equilibrium, and why the
radiative-equilibrium profile would be *steeper* than the dry adiabat.
(d) Explain why the observed profile is an average over latitude rather than a
single adiabat, and what that implies for using the standard atmosphere at a
particular place.

---

**★★★12.** Verification of a hydrostatic integration.

(a) State the verification test used in the demo and the measured discrepancy.
(b) Explain why the discrepancy being at the level of $10^{-16}$ (rather than,
say, $10^{-4}$) is the *correct* outcome for this test, and how it differs from
the verification logic of lesson [01](../01-pressure-density-depth.md) §8.
(c) Suggest a coding error that this test would *not* catch, and state how you
would catch it.
(d) The demonstration uses the same temperature function in the numerical
integration and in the analytic comparison. Explain how that makes the test
weaker, and how to strengthen it.
