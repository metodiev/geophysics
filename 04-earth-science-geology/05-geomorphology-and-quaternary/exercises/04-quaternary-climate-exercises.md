# Exercises — 04-05-04 Quaternary Climate Change and Landscape Records

Attempt these **closed-book** before opening the
[solutions](./04-quaternary-climate-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/quaternary_climate_demo.py`](../code/quaternary_climate_demo.py)
require you to run it and report its actual output. **Every answer must state
whether the quantity is computed from a formula, read from a model, or a proxy
that requires a calibration.**

Values to use: $S_0 = 1361$ W m⁻²; $A_{\mathrm{ocean}} = 3.61\times10^{14}$ m²;
mean ocean depth 3700 m; $\rho_i = 917$ kg m⁻³; $\rho_w = 1000$ kg m⁻³;
ice $\delta^{18}\mathrm{O}$ relative to the ocean $-35$‰; $k = 2.5$ W m⁻¹ K⁻¹;
$\rho c = 2.43\times10^{6}$ J m⁻³ K⁻¹; $1$ yr $= 3.15576\times10^{7}$ s.

---

## ★ Foundational

**★1.** Take $e = 0.0167$, $\varepsilon = 23.44^\circ$ and the perihelion at solar
longitude $\varpi = 282^\circ$.

(a) Compute the distance factor $(a/r)^{2} \approx 1 + 2e\cos(\lambda-\varpi)$ at
$\lambda = 282^\circ$ and at $\lambda = 102^\circ$.
(b) Compute the solar declination at the June solstice ($\lambda = 90^\circ$) from
$\sin\delta = \sin\varepsilon\sin\lambda$.
(c) Compute the sunrise hour angle $H_0 = \arccos(-\tan\varphi\tan\delta)$ at
$\varphi = 65^\circ$N, and the day length in hours ($2H_0$ expressed in degrees
divided by 15° per hour).
(d) Recompute the day length at $\varphi = 45^\circ$N.

---

**★2.** The global annual mean insolation is, to first order in $e$, $S_0/4$.

(a) Compute $S_0/4$.
(b) The demo reports the global annual mean for $\varepsilon = 22.0^\circ$ and
$\varepsilon = 24.5^\circ$. Report both values.
(c) Explain why they agree with each other but not exactly with $S_0/4$.

---

**★3.** An ice sheet covers $A = 3\times10^{6}$ km² to a mean thickness
$H = 1800$ m.

(a) Compute its volume in m³ and its sea-level equivalent
$\Delta z = (\rho_i/\rho_w)AH/A_{\mathrm{ocean}}$ in metres.
(b) Compute the ocean mass $M_o$ and the ice mass $M_i$, and the resulting
$\delta^{18}\mathrm{O}$ shift
$\delta' = (M_o\delta_o - M_i\delta_i)/(M_o - M_i)$ in per mille.
(c) Compute the ratio of (b) to (a), in per mille per metre, and the number of
metres of sea-level change per per mille.
(d) State the two assumptions of the one-box model that matter most for a
palaeoclimate interpretation.

---

## ★★ Applied

**★★4.** The thermal diffusivity of crustal rock is
$\alpha = k/(\rho c) = 32.47$ m² yr⁻¹.

(a) Compute the diffusion length $2\sqrt{\alpha t}$ for a surface event 15 ka ago.
(b) For a step cooling of $\Delta T = -7$ K at 15 ka, compute the temperature
anomaly remaining at 400 m and at 800 m.
(c) Compute the anomaly at 200 m for a step 1 ka ago with the same $\Delta T$.
(d) State which of these depths would be contaminated by a steady-state heat-flow
measurement, and which would not.

---

**★★5.** A heat-flow site has a measured gradient of 30 K km⁻¹ and
$k = 2.5$ W m⁻¹ K⁻¹.

(a) Compute the steady-state heat flow in mW m⁻².
(b) For a step cooling of $-5$ K at 100 ka, compute the transient gradient at
500 m from
$\partial T/\partial z = -\Delta T\,\exp(-z^{2}/4\alpha t)/\sqrt{\pi\alpha t}$.
(c) Compute the transient as a percentage of the steady heat flow, and state
whether the correction makes the inferred heat flow larger or smaller.
(d) State what a palaeoclimate correction does to a heat-flow map, and why an
uncorrected map has a *spatial pattern* of bias.

---

**★★6.** High-latitude summer insolation is the classical Milankovitch target.

(a) Compute the value at 75°N, $\lambda = 90^\circ$, for
$\varepsilon = 23.44^\circ$ and for $\varepsilon = 24.5^\circ$ (use the demo, or
the formula of the lesson with $H_0$ handled for polar day).
(b) Compute the percentage change.
(c) Compute $S_0/4$ again and state whether the *global* annual mean changed.
(d) Explain in three sentences why a change in the seasonal distribution can
drive glaciation even though the annual total is fixed.

---

## ★★★ Research-oriented

**★★★7.** Run [`../code/quaternary_climate_demo.py`](../code/quaternary_climate_demo.py)
and report:

(a) the daily insolation at the four cardinal solar longitudes for the five
latitudes, and the annual means;
(b) the global annual mean at $\varepsilon = 22.0^\circ$, $24.5^\circ$ and with
the perihelion longitude moved, plus $S_0/4$;
(c) the 65°N summer insolation for the three obliquities and the percentage
difference between the extremes;
(d) the precession table for the four perihelion longitudes;
(e) the sea-level equivalents and isotope shifts for the three ice-sheet cases;
(f) the diffusion lengths at the six times and the anomaly table;
(g) the transient gradient at 500 m for a 100 ka event and the resulting
percentage of a 75 mW m⁻² heat flow.

(h) In three sentences, state which of these outputs is a derivation, which is a
model result dependent on declared inputs, and which is an inference that would
require a dated record to be believed.

---

**★★★8.** Interpretation and its limits.

(a) A marine $\delta^{18}\mathrm{O}$ record shows a shift of $+1.0$‰. Using the
ratio computed in ★3(c), compute the sea-level change it implies, and state two
reasons the true change could differ by tens of metres.
(b) A borehole temperature profile is inverted for a ground-surface history, and
the result shows a 2 K warming starting 150 years ago. List three alternative
explanations for the same profile, and state the observation that would rule each
out.
(c) A moraine crest at 1800 m elevation is dated, and an equilibrium-line
depression is computed from it. State the two model inputs the palaeoclimate
conclusion rests on, and say which one a single moraine cannot constrain.
(d) Explain why the same thermal transient is described as a *signal* in one
paper and as a *correction* in another, and what determines which it is.
