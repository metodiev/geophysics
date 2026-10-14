# Exercises — 04-05-03 Fluvial, Coastal and Aeolian Systems

Attempt these **closed-book** before opening the
[solutions](./03-fluvial-coastal-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/fluvial_coastal_demo.py`](../code/fluvial_coastal_demo.py) require you
to run it and report its actual output. **Every empirical coefficient you use must
be named as empirical**, and every transport rate you report must carry the
coefficient and the threshold it depends on.

Values to use: $\rho_s = 2650$ kg m⁻³; $\rho_w = 1000$ kg m⁻³;
$\rho_a = 1.225$ kg m⁻³; $\mu_w = 1.002\times10^{-3}$ Pa s; $g = 9.81$ m s⁻²;
Shields $\tau^{*}_c = 0.045$; $\kappa = 0.40$; Manning $n = 0.030$;
Bagnold $A = 0.10$, $C = 1.75$; breaker index $\gamma = 0.78$;
$1$ yr $= 3.15576\times10^{7}$ s.

---

## ★ Foundational

**★1.** A quartz grain of diameter $d = 0.5$ mm settles in still water.

(a) Using the drag balance, the drag coefficient
$C_D = \frac{24}{\mathrm{Re}}(1 + 0.15\,\mathrm{Re}^{0.687})$ and iteration,
compute $v_s$ and the Reynolds number.
(b) Compute $C_D$ at that Reynolds number.
(c) Compute the Stokes velocity and the percentage error of Stokes' law.
(d) State in one sentence why Stokes' law fails here.

---

**★2.** The bed shear stress in steady uniform flow is
$\tau_b = \rho_w g h S$ and the Shields threshold is
$\tau_c = \tau^{*}_c(\rho_s - \rho_w) g d$.

(a) Compute $\tau_c$ for $d = 2$ mm.
(b) Compute $\tau_b$ for $h = 1.5$ m and $S = 2\times10^{-4}$.
(c) Compute the ratio $\tau_b/\tau_c$ and state whether the bed is mobile.
(d) Compute $\tau_c$ for $d = 0.5$ mm and for $d = 5$ mm, and state which of the
three sizes is mobile at the stress of part (b).

---

**★3.** A rectangular channel is $W = 30$ m wide, $D = 1.2$ m deep with
$S = 8\times10^{-4}$ and $n = 0.030$.

(a) Compute the hydraulic radius $R_h = A/P$.
(b) Compute the depth-averaged velocity from Manning's equation.
(c) Compute the discharge $Q$.
(d) Compute the Froude number and state the flow regime.

---

## ★★ Applied

**★★4.** A wave has period $T = 10$ s.

(a) Compute its deep-water celerity $c_0 = gT/2\pi$ and wavelength
$L_0 = c_0 T$.
(b) Compute the shallow-water celerity $\sqrt{gh}$ at $h = 1$ m and $h = 3$ m.
(c) At what depth does the shallow-water limit ($kh \le 0.3$) begin to apply?
Estimate it by scaling from the demo's table entry for $T = 8$ s, $h = 5$ m
($kh = 0.592$), using $kh \propto \sqrt{h}$ in the shallow limit, and state that
the estimate is approximate.
(d) Compute the breaking depth and breaking height for $H_0 = 3$ m, $T = 10$ s
from $h_b^{5/2} = H_0^{2}c_{g0}/(\gamma^{2}\sqrt{g})$ with $c_{g0} = c_0/2$ and
$H_b = \gamma h_b$.

---

**★★5.** Suspension and wind transport.

(a) Compute the Rouse number for $v_s = 0.05$ m s⁻¹ and $u_{*} = 0.08$ m s⁻¹,
and name the transport regime.
(b) Recompute for $u_{*} = 0.16$ m s⁻¹ and name the new regime.
(c) Compute the aeolian threshold friction velocity for $d = 0.3$ mm.
(d) Compute Bagnold's potential flux at $u_{*} = 0.45$ m s⁻¹ in kg m⁻¹ s⁻¹ and in
tonnes per metre per year, and state in what sense it is an upper bound.

---

**★★6.** The Bruun rule is $R = S L^{*}/(B + h^{*})$.

(a) Compute $R$ for $S = 4$ mm yr⁻¹, $L^{*} = 8000$ m, $B = 1.5$ m,
$h^{*} = 18$ m.
(b) Recompute for $L^{*} = 16000$ m and state the ratio to (a).
(c) State the three assumptions of the model and one situation in which each
fails.
(d) The closure depth $h^{*}$ is often approximated by a multiple of the breaking
wave height. Explain why that makes $R$ depend on the wave climate even though
$S$ appears as an independent variable.

---

## ★★★ Research-oriented

**★★★7.** Run [`../code/fluvial_coastal_demo.py`](../code/fluvial_coastal_demo.py)
and report:

(a) the settling velocity, Reynolds number and Stokes error for 0.0625, 0.25 and
1.0 mm;
(b) the Shields threshold for the six size classes and the mobility ratio for the
$h = 2$ m, $S = 3\times10^{-4}$ flow;
(c) the Manning velocity, discharge and Froude number for the four channel cases,
and the hydraulic-geometry exponents with their sum;
(d) the wave table for all five cases, and the breaking depth for the four
$H_0$–$T$ pairs;
(e) the Rouse number for the four size classes at $u_{*} = 0.05$ m s⁻¹;
(f) the aeolian threshold for the five sizes and the potential flux at the three
shear velocities;
(g) the Bruun retreat for the three cases.

(h) In three sentences, identify which of these outputs are computed from a
derived relation, which rest on an empirical coefficient, and which are
conventions or parameterisations.

---

**★★★8.** Interpretation and its limits.

(a) A point-bar sand body is $8$ m thick and $200$ m wide inside a floodplain of
silty clay. Name the two property contrasts most likely to image it, and one
method for each. Explain why the total sand fraction of the floodplain is a poor
predictor of its yield.
(b) A dune field has a measured crest-to-crest spacing of 120 m and a height of
10 m. The wind data give a potential flux of $200$ m³ m⁻¹ yr⁻¹. Explain why the
observed dune migration rate corresponds to a much smaller actual flux, and name
three processes responsible.
(c) A shoreline is retreating at $1.6$ m yr⁻¹ and the local sea-level trend is
$4$ mm yr⁻¹. Using the Bruun rule, compute the implied $L^{*}/(B + h^{*})$, and
state two independent observations that would test whether the retreat is
Bruun-type at all.
(d) A hydraulic-geometry study quotes exponents $b = 0.5$, $f = 0.4$, $m = 0.2$.
State what is wrong with them and what constraint they violate.
