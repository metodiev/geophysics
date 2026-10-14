# Exercises — 02-05-07 Thermodynamic Phase Equilibria and Mantle Mineralogy

Attempt these **closed-book** before opening the
[solutions](./07-phase-equilibria-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/phase_equilibria_demo.py`](../code/phase_equilibria_demo.py) require you
to run it and report its actual output.

Pressures at the CMB, ICB and centre are **adopted model values**; Clapeyron
slopes and melting temperatures at depth are **nominal**. Do not quote them as
measurements.

---

## ★ Foundational

**★1.** A melting transition has $L = 6\times10^5$ J kg⁻¹, $T_m = 2000$ K and
$\Delta V = +3\times10^{-6}$ m³ kg⁻¹.

(a) Compute $\Delta S$.
(b) Compute $\mathrm{d}P/\mathrm{d}T$ and $\mathrm{d}T/\mathrm{d}P$.
(c) State the sign of $\Delta V$ and explain in words why it gives that sign for
$\mathrm{d}T/\mathrm{d}P$.
(d) State what would happen if $\Delta V$ were negative.

---

**★2.** The ice–water transition.

(a) Using $L = 3.34\times10^5$ J kg⁻¹, $T = 273.15$ K, $\rho_{\text{ice}} = 917$
and $\rho_{\text{water}} = 1000$ kg m⁻³, compute $\Delta v$.
(b) Compute $\mathrm{d}T/\mathrm{d}P$ in K MPa⁻¹.
(c) State the measured value you would compare it with and whether your answer
agrees.
(d) Explain why the same formula with $\Delta v > 0$ describes almost every
silicate.

---

**★3.** The 410 km discontinuity has $\gamma = \mathrm{d}P/\mathrm{d}T = +2.5$
MPa K⁻¹ and $\Delta V < 0$.

(a) Compute $\Delta S$ from $\gamma\Delta V$ with
$\Delta V = -0.5\times10^{-6}$ m³ mol⁻¹.
(b) Compute the latent heat at 1900 K.
(c) Interpret the sign of $\Delta S$ in terms of the structure of the product
phase.
(d) Explain why neither the sign nor the magnitude was assumed.

---

**★4.** Using $P = \rho g z$ with $\rho = 3400$ kg m⁻³, estimate the pressure at
410 km. Compare with the commonly quoted 13.5 GPa and state why the estimate is
imperfect.

---

## ★★ Applied

**★★5.** Depth shifts of the discontinuities.

(a) Write the relation between a geotherm perturbation and a boundary's depth
shift.
(b) Compute the shift of the 410 for $\pm200$ K with $\gamma = +3$ MPa K⁻¹ and
$\rho = 3400$ kg m⁻³.
(c) Compute the shift of the 660 for $\pm200$ K with $\gamma = -3$ MPa K⁻¹,
$\rho = 4000$ kg m⁻³ and $g = 9.9$ m s⁻².
(d) Explain how the two shifts together change the thickness of the transition
zone, and what a seismologist would measure.

---

**★★6.** The core adiabat.

(a) Write the isentropic gradient in terms of $\alpha$, $T$, $\rho$ and $c_p$.
(b) Compute it for $\alpha = 1.2\times10^{-5}$ K⁻¹, $T = 4500$ K,
$\rho = 11\,500$ kg m⁻³ and $c_p = 700$ J kg⁻¹ K⁻¹.
(c) With $P_{\text{CMB}} = 135$ GPa and $P_{\text{ICB}} = 329$ GPa, compute the
adiabatic temperature rise across the outer core.
(d) State what would happen to the adiabatic rise if the outer core were stably
stratified rather than convecting, and why that matters for the inner core.

---

**★★7.** The melting curve required by a solid inner core.

(a) With $T_{\text{ad}}(P_{\text{CMB}}) = 4000$ K, $T_m(P_{\text{CMB}}) = 3600$ K
and the answer to ★6(b), compute the average melting slope required for the
curves to meet at the ICB.
(b) Compare it with the adiabatic slope.
(c) State the condition on the two slopes for a solid inner core to exist at all.
(d) Explain what the observation of a solid inner core therefore constrains.

---

**★★8.** Run the demo, Sections 3 and 4.

(a) Report the adiabatic slope and the required melting slope.
(b) Report the four rows of the location table.
(c) State how much hotter the centre is than the top of the outer core.
(d) State the size of the margin between $T_m$ and $T_{\text{ad}}$ at the centre
and what that implies about the robustness of the conclusion.

---

**★★9.** Decompression melting.

(a) State the lithostatic pressure gradient, the mantle adiabat slope and the
range of dry-peridotite solidus slopes, in the units used in the lesson.
(b) Explain why the slopes' relative sizes, not their absolute values, decide
whether decompression melting occurs.
(c) With a potential temperature of 1573 K and first melting observed at 65 km,
compute the solidus temperature the model requires at that depth.
(d) Explain why the parcel's temperature *falls* on ascent yet it melts.

---

## ★★★ Research-oriented

**★★★10.** Latent heat and entropy of inner-core growth.

(a) Using $r = 1221$ km and $\rho = 12\,800$ kg m⁻³, compute the inner core's
volume and mass.
(b) With $L = 2.5\times10^5$ J kg⁻¹, compute the cumulative latent heat and the
entropy released, with the temperature you adopt stated.
(c) Compute the present-day latent power for growth rates of 0.5 and 1.0 mm yr⁻¹.
(d) State why the growth rate is not directly measurable and what observational
constraints bound it.

**★★★11.** Phase-rule analysis and disequilibrium.

(a) State the Gibbs phase rule and identify $C$, $P$ and the meaning of the
number 2.
(b) For an anhydrous peridotite melting in the system CaO–MgO–Al₂O₃–SiO₂, give
$C$ and compute the variance at a point where $(Mg,Fe)_2SiO_4$ and melt coexist.
(c) Explain why the observed 410 km discontinuity is sharp while the 520 km
feature is diffuse, using the Clapeyron slopes of the lesson.
(d) Explain, using the concept of relaxation time, why a fast-subducting slab may
contain metastable olivine below 410 km, and what seismic signature that would
produce.

**★★★12.** A thermodynamic consistency check.

(a) Write the condition for two phases to coexist and differentiate it to obtain
Clausius–Clapeyron.
(b) Given an observed boundary with $\gamma > 0$ and an independently determined
$\Delta V < 0$, show that the entropy change is negative and state whether this is
physically plausible for a densification.
(c) Two published estimates of $\Delta V$ for the same transition differ by a
factor of 2. Compute the resulting spread in $\Delta S$ at fixed $\gamma$ and
state what measurement would settle it.
(d) Explain why the *depth* of a discontinuity is a better-constrained quantity
than the *slope* of its Clapeyron curve, and what that means for how the boundary
should be used to infer mantle temperature.
