# Exercises — 04-06-04 Aquifer Types and Groundwater Occurrence

Attempt these **closed-book** before opening the
[solutions](./04-groundwater-aquifers-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/groundwater_aquifers_demo.py`](../code/groundwater_aquifers_demo.py)
require you to run it and report its actual output. **State whether each quantity
is a rock property, a fluid property or a well-and-aquifer property together, and
never quote a recharge or a safe yield as a measurement.**

Values to use: $g = 9.81$ m s⁻²; $\rho_w = 1000$ kg m⁻³;
$\varepsilon_w = 81$, $\varepsilon_s = 5$, $\varepsilon_a = 1$;
$c = 2.99792458\times10^{8}$ m s⁻¹; $1$ day $= 86\,400$ s.

---

## ★ Foundational

**★1.** A sand aquifer has a hydraulic conductivity of $2\times10^{-4}$ m s⁻¹ and
is 20 m thick. The hydraulic gradient is $5\times10^{-4}$ and the flow is through
a cross-section 500 m wide.

(a) Compute the volumetric flow rate in m³ s⁻¹.
(b) Convert it to m³ day⁻¹.
(c) Compute the transmissivity in m² s⁻¹ and in m² day⁻¹.
(d) State whether the flow rate would change if the water temperature rose, and
why.

---

**★2.** A confined aquifer has a specific storage of
$S_s = 2\times10^{-6}$ m⁻¹ and a thickness of 40 m. An adjacent unconfined
aquifer of the same material has a specific yield of 0.20.

(a) Compute the storativity of the confined aquifer.
(b) Compute the ratio $S_y/S$.
(c) Compute the volume of water released from 1 km² for a 1 m head decline in
each case.
(d) State which aquifer would show a large water-level change for a small change
in storage, and why.

---

**★3.** A clean sand has a porosity of 0.25 and contains water of resistivity
8 Ω m. Archie's law applies with $a = 1$ and $m = 2$.

(a) Compute the formation factor.
(b) Compute the saturated rock resistivity.
(c) Recompute the rock resistivity at a water saturation of 0.5, using $n = 2$.
(d) State which of the four inputs ($a$, $m$, $n$, $\rho_w$) is most often
violated in a real aquifer, and how.

---

## ★★ Applied

**★★4.** A confined aquifer has $T = 0.02$ m² s⁻¹ and $S = 2\times10^{-4}$. A
well pumps at $Q = 0.06$ m³ s⁻¹.

(a) Compute $u$ at $r = 150$ m after 2 days.
(b) Compute the well function $W(u) = E_1(u)$ at that value.
(c) Compute the drawdown.
(d) Recompute the drawdown at 20 days and state the ratio to (c).

---

**★★5.** An unconfined aquifer has a specific yield of 0.12. The water table rises
1.2 m during a recharge season in which no pumping occurs.

(a) Compute the recharge in mm yr⁻¹ using $R = S_y\Delta h/\Delta t$ with
$\Delta t = 1$ yr.
(b) Recompute for $S_y = 0.06$ and for $S_y = 0.24$.
(c) State why the answer is a consistency check rather than a measurement.
(d) Name two conditions under which the method fails completely.

---

**★★6.** A sand has a porosity of 0.25; the solid permittivity is 5, water 81,
air 1.

(a) Compute the effective permittivity at full saturation using CRIM.
(b) Compute the radar velocity at full saturation, in m/ns.
(c) Recompute both for a water content of 0.05.
(d) Compute the GPR reflection coefficient between the two states and state why
the water table is such a strong radar reflector.

---

## ★★★ Research-oriented

**★★★7.** Run [`../code/groundwater_aquifers_demo.py`](../code/groundwater_aquifers_demo.py)
and report:

(a) the Darcy flow rate and transmissivity for the four $K$ and $b$ pairs;
(b) the specific storage and the three storativities, and the $S_y/S$ ratio;
(c) the specific capacity at the four $T$–$S$ pairs;
(d) the check value of $E_1(1)$ and the drawdown table for the five times and
three radii;
(e) the recharge and its sensitivity to $S_y$;
(f) the formation factor and saturated resistivity at the five porosities, and the
partial-saturation resistivities;
(g) the CRIM permittivities, velocities and Archie resistivities at the five
saturations, and the dry-versus-saturated reflection coefficient.

(h) In three sentences, say which outputs are derived from a physical relation,
which are empirical fits, and which are model conventions.

---

**★★★8.** Interpretation and its limits.

(a) A resistivity survey finds a 200 Ω m unit at 30 m depth. List three different
things it could be, and state one additional measurement for each that would
discriminate.
(b) A fractured granite and an alluvial sand have the same transmissivity in
pumping tests. Explain why the *exploration* problem is nevertheless completely
different, and which physical property carries the signal in each case.
(c) A saline intrusion is mapped by EM at a coastal site. Explain why the anomaly
is nearly independent of the rock type, and name the physical property that is
actually measured.
(d) A recharge estimate from water-table fluctuation gives 150 mm yr⁻¹ while a
catchment water balance gives 250 mm yr⁻¹. Give three reasons the two could
differ by that amount, and state which is testable with geophysics.
