# Exercises — 04-01-01 Crust, Mantle, Core: Seismological and Geochemical Evidence

Attempt these **closed-book** before opening the
[solutions](./01-layered-earth-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/layered_earth_demo.py`](../code/layered_earth_demo.py) require you to
run it and report its actual output. Unless a problem says otherwise, use
$G = 6.674\times10^{-11}$ m³ kg⁻¹ s⁻², $R = 6371$ km and
$g = 9.81$ m/s².

---

## ★ Foundational

**★1.** A two-layer model has a crust of density 2750 kg/m³ from the surface to
30 km depth, and a mantle of density 3350 kg/m³ below.

(a) Compute the volume of the crustal shell and its mass.
(b) Compute the surface gravity from a total Earth mass of $5.9722\times10^{24}$
kg and compare with the standard value 9.80665 m/s².
(c) Compute the lithostatic pressure at the base of the crust from
$P = \rho g h$.
(d) Express (c) in GPa and state the crustal depth that corresponds to 1 GPa.

---

**★2.** Unit conversions, all of which appear in this lesson.

(a) A P velocity of 13.7 km/s: convert to m/s.
(b) A density of 5570 kg/m³: convert to g/cm³.
(c) Compute $K = \rho(v_p^2 - \frac43 v_s^2)$ for $\rho = 5570$ kg/m³,
$v_p = 13.7$ km/s and $v_s = 7.3$ km/s, in GPa.
(d) State the unit of $K/\rho$ and of $\sqrt{K/\rho}$.

---

**★3.** The ray that grazes the core–mantle boundary.

(a) Compute its ray parameter $p = r_\text{CMB}/v_p$ with $r_\text{CMB} = 3480$
km and $v_p = 13.7$ km/s. State the unit.
(b) Compute $\sin\theta_\text{core} = p\,v_\text{core}/r_\text{CMB}$ for
$v_\text{core} = 8.0$ km/s.
(c) Is the transmitted ray bent toward the boundary or away from it? State how
that direction produces the P-wave shadow.
(d) Repeat (b) for $v_\text{core} = 16$ km/s and state what happens.

---

## ★★ Applied

**★★4.** A two-layer Earth: a core of density 11 000 kg/m³ out to 3480 km, and a
mantle of density 4500 kg/m³ above it to 6371 km.

(a) Compute the mass of each layer and the total.
(b) Compute $I = \frac{8\pi}{3}\int_0^R \rho r^4\,\mathrm{d}r$ for the two-layer
model, using $I = \frac{8\pi}{15}(\rho_c r_c^5 + \rho_m(R^5 - r_c^5))$.
(c) Compute $I/(MR^2)$ and compare with the observed 0.3307.
(d) The two-layer value is too high. Explain in one sentence what feature of the
real Earth the model is missing.

---

**★★5.** Using the same two-layer model, compute the pressure at the centre.

(a) Compute the gravity at the core–mantle boundary from the core mass alone.
(b) Compute the pressure increase across the mantle as $\bar\rho_m g_m h$ with
$g_m$ the mean gravity over the mantle layer.
(c) Compute the pressure increase across the core similarly.
(d) Sum to get the central pressure and compare with the demo's 356.6 GPa.

---

**★★6.** The shadow-zone sweep.

(a) For a mantle of constant velocity $v$, the grazing-ray distance is
$\Delta = 2[\arcsin(p/r_\text{min}) - \arcsin(p/R)]$ with $p = r_\text{CMB}/v$.
Evaluate it by hand for $v_s = 7.3$ km/s, $r_\text{min} = 3480$ km and
$R = 6371$ km.
(b) Compare your answer with the demo's model value of 90.4° and with the
observed ~103°.
(c) State which end of the demo's alpha sweep your value corresponds to and why.

---

## ★★★ Research-oriented

**★★★7.** Refining the model. Add a single extra node to the lower mantle of the
demo, at radius 3980 km, with $v_p = 13.2$ km/s, $v_s = 7.1$ km/s and
$\rho = 5370$ kg/m³.

(a) Recompute the S grazing-ray distance and report the change from 90.4°.
(b) State whether the change moves the value toward or away from 103° and give
the physical reason.
(c) Adjust the extra node's velocity until the computed $\Delta_S$ is within 1°
of 103°, and report the velocity you needed.
(d) Comment on whether a model tuned this way has been *tested*.

---

**★★★8.** Run [`../code/layered_earth_demo.py`](../code/layered_earth_demo.py)
and report:

(a) the model mass, the model surface gravity and the model moment-of-inertia
factor, each next to its tabulated value and the percentage difference;
(b) the gravity at the core–mantle boundary and an explanation of why it exceeds
the surface value;
(c) the computed pressure at the core–mantle boundary, the inner-core boundary
and the centre;
(d) the S grazing-ray distance and travel time;
(e) the P distances for the grazing mantle ray and for the same ray transmitted
into the core, with the turning radius;
(f) the $\Delta_S$ values at $\alpha = 1, 2, 4$ and the value closest to the
observed boundary;
(g) two sentences on which numbers in the output are computed and which are
tabulated.

---

**★★★9.** Critique. For each of the following inputs to the demo's model, state
whether it is a *definition*, a *measurement*, or an *assumption*, and what it
would take to test it: the Earth radius; the density of the outer core; the
sharpness of the core–mantle boundary; the statement that $v_s = 0$ in the outer
core; the depth of the 660 km discontinuity.
