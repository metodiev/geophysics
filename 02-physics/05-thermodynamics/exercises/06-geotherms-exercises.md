# Exercises — 02-05-06 Geotherms, Heat Flow and the Earth's Thermal Budget

Attempt these **closed-book** before opening the
[solutions](./06-geotherms-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to [`../code/geotherms_demo.py`](../code/geotherms_demo.py)
require you to run it and report its actual output.

**Every geotherm answer must state its three inputs:** the transport mechanism,
the source distribution and the boundary conditions. Numbers in this exercise set
are nominal unless stated otherwise.

---

## ★ Foundational

**★1.** Derive the steady geotherm for $A(z) = A_0e^{-z/h}$ with $z$ downward,
constant $k$, surface temperature $T_0$ and surface heat flow $q_0$.

(a) Integrate the heat equation once and impose the surface gradient condition.
(b) Integrate again and obtain $T(z)$.
(c) Obtain $q(z)$ and identify its limit as $z\gg h$.
(d) Show that the surface heat flow equals the mantle contribution plus all of
the crustal production, and state the assumption this rests on.

---

**★2.** With $T_0 = 283.15$ K, $q_0 = 55$ mW m⁻², $A_0 = 1.0$ µW m⁻³,
$h = 10$ km and $k = 2.5$ W m⁻¹ K⁻¹:

(a) Compute $q_{\text{mantle}}$.
(b) Compute the radiogenic fraction of the surface heat flow.
(c) Compute the temperature at 35 km.
(d) Compute the mean gradient over the top 35 km.

---

**★3.** For the rock and parameters of ★2:

(a) Compute the temperature at 50 km.
(b) Compute the gradient between 35 km and 50 km and compare it with the mean
gradient over 0–35 km.
(c) Explain why the deeper gradient is smaller.
(d) State at what depth the geotherm becomes linear and why.

---

**★4.** Half-space cooling.

(a) Write $q(t)$ and $d(t)$ for a cooling half-space.
(b) For $k = 3.2$ W m⁻¹ K⁻¹, $\rho = 3300$ kg m⁻³, $c_p = 1250$ J kg⁻¹ K⁻¹ and
$\Delta T = 1300$ K, compute $\kappa$, $q$ and $d$ at 10, 40 and 70 Ma.
(c) Verify the invariant $q\sqrt t$.
(d) State which departure from the model you expect at each of those three ages,
and why.

---

## ★★ Applied

**★★5.** Run the demo, Section 1.

(a) Report the geotherm table for the three provinces.
(b) Report the lithosphere thickness by both criteria.
(c) Explain why the radiogenic fraction is highest for the craton.
(d) Explain why the 100 km and 150 km columns are a *reductio* rather than a
temperature prediction.

---

**★★6.** Global heat loss.

(a) With continental heat flow 65 mW m⁻² over 29 per cent of 5.10 × 10¹⁴ m² and
oceanic 100 mW m⁻² over the rest, compute the global mean and the total loss.
(b) Compute the total for mean values of 75 and 95 mW m⁻².
(c) State what the spread of the answers tells you about the precision of any
statement that begins "the Earth loses X TW".
(d) Explain why the global mean is not a value a drill hole can measure.

---

**★★7.** Radiogenic inventory.

(a) Compute the continental crustal power for 1.479 × 10¹⁴ m² of crust 35 km
thick with $A = 1.0$ µW m⁻³.
(b) Compute the mantle power for a mantle volume of $8.889\times10^{20}$ m³ with
$A = 0.01$ µW m⁻³.
(c) Recompute both with the concentrations doubled and state the change in each.
(d) State which of the two is more poorly constrained in reality, and why.

---

**★★8.** Secular cooling.

(a) With a 45 TW loss and a 14.6 TW production, compute the deficit.
(b) Convert the deficit to a cooling rate for a mantle of
$4.0\times10^{24}$ kg and $c_p = 1250$ J kg⁻¹ K⁻¹, in K per 10⁹ yr.
(c) Recompute for a production of 20 TW and state the change.
(d) State two reasons the real cooling rate is lower than your answer.

---

**★★9.** Run the demo, Section 3.

(a) Report the deficit for the demo's assumptions.
(b) Report the implied cooling rate.
(c) State which single input dominates the uncertainty and how much the answer
moves if it is halved.
(d) Explain why the correct way to report this result is as an order of magnitude
with its assumptions.

---

## ★★★ Research-oriented

**★★★10.** Construction and critique of a geotherm for a named setting.

(a) Choose a tectonic setting (craton, extensional basin, volcanic arc, oceanic
plateau) and state the three inputs of your geotherm with the values you adopt.
(b) Build the geotherm with the exponential-source model and compute the
temperature at the Moho and at the lithosphere base.
(c) Identify which of your inputs you cannot defend from a source you have
verified, and say so explicitly.
(d) State two observations that would falsify your geotherm.

**★★★11.** The thermal budget as an inverse problem. The surface heat loss is
measured; the radiogenic production is inferred from composition.

(a) Write the budget as $\dot Q_{\text{loss}} = \dot Q_{\text{rad}} + \dot Q_{\text{cool}}$
and identify which terms are measured, which are computed and which are assumed.
(b) Explain why the residual $\dot Q_{\text{cool}}$ is not an independent
measurement of anything.
(c) State what observation would convert the radiogenic term from an assumption to
a measurement, and what its current uncertainty is (say so if you cannot verify
a value).
(d) Discuss, in three sentences, why a budget whose residual is a third of its
largest term should be reported with its assumptions rather than as a result.
