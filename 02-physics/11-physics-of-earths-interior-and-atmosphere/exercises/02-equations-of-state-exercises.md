# Exercises — 02-11-02 Equations of State and High-Pressure Mineral Physics

Attempt these **closed-book** before opening the
[solutions](./02-equations-of-state-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/eos_mineral_physics_demo.py`](../code/eos_mineral_physics_demo.py)
require you to run it and report its actual output.

**Every problem that asks for a pressure, a density or a temperature requires you
to state the equation of state, the thermal term if any, and the anchor of any
integrated adiabat.** The mineral parameters in the demo are **nominal,
illustrative** values quoted to two significant figures, not measured constants;
treat them as such throughout.

---

## ★ Foundational

**★1.** The second-order Birch–Murnaghan equation is
$P_2 = \tfrac32K_0(x^7-x^5)$ with $x = (V_0/V)^{1/3}$.

(a) Evaluate $P_2$ at $V/V_0 = 0.9$ for $K_0 = 128$ GPa.
(b) Show that $P_2(V_0) = 0$.
(c) Show that $-V\,\mathrm{d}P_2/\mathrm{d}V$ evaluated at $V = V_0$ equals
$K_0$, and explain why this must hold for any acceptable equation of state.
(d) Evaluate the same derivative at $V/V_0 = 0.9$ and state whether it is larger
or smaller than $K_0$. Give the physical reason.

---

**★2.** The third-order form is
$P_3 = P_2\left[1 + \tfrac34(K_0'-4)(x^2-1)\right]$.

(a) Show algebraically that $P_3 = P_2$ identically when $K_0' = 4$.
(b) For $K_0 = 128$ GPa, $K_0' = 4.2$ and $V/V_0 = 0.9$, evaluate both $P_2$ and
$P_3$ and report the difference.
(c) State why the third-order term is proportional to $(K_0'-4)$ rather than to
$K_0'$.
(d) For which of forsterite ($K_0'=4.2$) and hcp iron ($K_0'=5.0$) does the
third-order term matter more, at the same $K_0$ and the same compression?

---

**★3.** A layer has $\rho = 3300$ kg m⁻³, $v_p = 8.1$ km/s and $v_s = 4.5$ km/s.

(a) Compute $\phi = v_p^2 - \tfrac43v_s^2$ in km² s⁻².
(b) Compute $K = \rho\phi$ in GPa. **State the factor by which you converted
$\phi$.**
(c) Compute the Adams–Williamson gradient $\mathrm{d}\rho/\mathrm{d}z = \rho g/\phi$
at $g = 9.81$ m/s², in kg m⁻³ km⁻¹.
(d) State the two assumptions that this gradient carries.

---

**★4.** Entropy and the adiabat.

(a) Write the entropy differential $\mathrm{d}S = (c_p/T)\,\mathrm{d}T -
\alpha V\,\mathrm{d}P$ and set $\mathrm{d}S = 0$ to obtain
$(\mathrm{d}T/\mathrm{d}P)_S$.
(b) Use $\gamma = \alpha K/(\rho c_p)$ to show that
$(\mathrm{d}T/\mathrm{d}P)_S = \gamma T/K$.
(c) Multiply by $\mathrm{d}P/\mathrm{d}z = \rho g$ to obtain
$(\mathrm{d}T/\mathrm{d}z)_s = \gamma gT/\phi$.
(d) Evaluate it for $\gamma = 1.5$, $g = 9.9$ m/s², $T = 1700$ K and
$\phi = 3.861\times10^7$ m² s⁻², and state the temperature change over 375 km.

---

**★5.** Thermal pressure.

(a) Write the linearised thermal equation of state
$P(V,T) \approx P(V,T_{\text{ref}}) + \alpha K(T-T_{\text{ref}})$ and state what
each symbol is.
(b) Compute the thermal pressure for $\alpha = 2.5\times10^{-5}$ K⁻¹,
$K = 650$ GPa and $T - T_{\text{ref}} = 2525$ K.
(c) The total pressure at that depth is 135 GPa. Report the thermal contribution
as a percentage.
(d) State why this is described as "not a correction".

---

## ★★ Applied

**★★6.** Inverting the equation of state.

(a) Explain why $P(V)$ is monotonic decreasing for a physically sensible
equation of state, and why that justifies a bisection inversion.
(b) Invert $P_2 = 10$ GPa for $K_0 = 128$ GPa, $K_0' = 4$, to four decimal places
in $V/V_0$. Perform at least four bisection steps by hand and report the
bracketing interval after each.
(c) Verify your answer by substituting back.
(d) The demo reports round-trip residuals of order $10^{-13}$ GPa after 200
bisection iterations. Explain why the residual is limited by the bisection
tolerance and not by the equation of state.

---

**★★7.** Third-order sensitivity at high compression. For periclase with
$K_0 = 160$ GPa:

(a) Find $V/V_0$ at which $P_2 = 100$ GPa, and the corresponding $V/V_0$ at which
$P_3 = 100$ GPa with $K_0' = 5$.
(b) Report the percentage difference in the implied volume.
(c) Report the difference $P_3 - P_2$ at the volume found in (a) for $K_0'=5$.
(d) Explain the practical consequence for interpreting a diffraction experiment in
which the unit-cell volume is measured and the pressure is inferred from an
equation of state.

---

**★★8.** Seismic parameters across the core–mantle boundary.

(a) Compute $\phi$ and $K$ just above the CMB using $\rho = 5570$ kg m⁻³,
$v_p = 13.7$ km/s, $v_s = 7.3$ km/s.
(b) Compute $\phi$ and $K$ just below the CMB using $\rho = 9900$ kg m⁻³,
$v_p = 8.0$ km/s, $v_s = 0$.
(c) Compute the ratio of the CMB density to the density just above it, and the
ratio of $\phi$ below to $\phi$ above.
(d) Explain in two sentences why the *opposite* directions of those two ratios
force a compositional rather than a thermal interpretation.

---

**★★9.** The isothermal-EOS shortfall.

(a) Take $\rho_0 = 4400$ kg m⁻³, $K_0 = 283$ GPa, $K_0' = 4$ and compress
isothermally to $\rho = 5570$ kg m⁻³. Compute $V/V_0$ and the Birch–Murnaghan
pressure.
(b) Compare with the hydrostatic pressure at the CMB, 134.6 GPa, and report the
shortfall as a percentage.
(c) Name the two missing physical effects, and state the direction in which each
pushes the required pressure.
(d) Explain why the *phase-change* term would be removed by choosing a reference
state just below 660 km rather than just above it.

---

**★★10.** Integrating an adiabat.

(a) Starting at $T = 1900$ K at 660 km, integrate
$(\mathrm{d}T/\mathrm{d}z)_s = \gamma gT/\phi$ with $\gamma = 1.5$ over the
intervals 660–1000 km ($g = 9.947$, $\phi = 6.428\times10^7$ m² s⁻²) and
1000–2000 km ($g = 9.883$, $\phi = 7.126\times10^7$ m² s⁻²), recomputing the
gradient from the current temperature at each step.
(b) Report $T$ at 1000 km and at 2000 km.
(c) Compare with the demo's values (2050 K and 2476 K) and explain any difference.
(d) State what the calculation does **not** determine, and what would.

---

## ★★★ Research-oriented

**★★★11.** Verification of an equation-of-state implementation.

(a) Design a three-part verification suite for a Birch–Murnaghan implementation.
One part must test the value, one the derivative, and one the thermodynamic
consistency.
(b) Explain why the round-trip test of ★6 is necessary but *not sufficient*: give
a one-line modification of the code that passes the round trip and is still
wrong.
(c) Explain what "thermodynamic consistency" means here — what quantity must be
independent of the path by which it is computed — and how you would test it.
(d) The demo's parameters are nominal. Explain how you would propagate a 5 per
cent uncertainty in $K_0$ into the density at 135 GPa, and state whether the
resulting uncertainty would be dominated by that or by $K_0'$.

---

**★★★12.** Where the isothermal equation of state breaks down.

(a) The demo reports a 20 per cent shortfall in the CMB pressure from an
isothermal, single-phase equation of state. Attribute that shortfall
quantitatively: use $\alpha K\Delta T$ from ★5 to estimate the thermal part, and
account for the rest with the phase-change argument.
(b) Your attribution in (a) uses a *nominal* $\alpha$. State which direction of
error in $\alpha$ would make the thermal contribution smaller, and what
observational test could distinguish a thermal shortfall from a compositional one.
(c) A colleague fits $K_0$ and $K_0'$ to the isothermal compression data and then
uses the fit to compute the density at the CMB. Write two sentences explaining to
them what is missing and why it matters at the 10 per cent level.
(d) Explain why the same objection does *not* apply to using an isothermal
equation of state to compare two candidate mineral assemblages at the same
pressure, provided the temperature is the same for both.

---

**★★★13.** The observational test of a compositional core.

The claim of lesson §5 is that the *pattern* of a misfit between a predicted and
an observed $(v_p,v_s,\rho)$ discriminates composition from temperature.

(a) A candidate assemblage at the right $(P,T)$ predicts both $v_p$ and $v_s$
5 per cent too high and $\rho$ 1 per cent too low. Argue what that pattern
suggests and why.
(b) A different candidate predicts $v_p$ correct, $v_s$ 2 per cent low and $\rho$
correct. Argue what that suggests, and which elastic modulus has been misjudged.
(c) Explain why a *scalar* velocity misfit is much less informative than the
pattern.
(d) State the observation that would falsify the compositional interpretation of
the CMB outright, and why it is not observed.
