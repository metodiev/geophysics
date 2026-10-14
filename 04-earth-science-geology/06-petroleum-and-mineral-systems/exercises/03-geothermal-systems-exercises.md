# Exercises — 04-06-03 Geothermal Systems, Heat Flow and Resource Assessment

Attempt these **closed-book** before opening the
[solutions](./03-geothermal-systems-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/geothermal_systems_demo.py`](../code/geothermal_systems_demo.py) require
you to run it and report its actual output. **The heat in place is a physical
quantity and may be computed. Any recovery factor, capacity or reserve is an
engineering quantity; state it symbolically at most, and never as a fact.**

Values to use: $g = 9.81$ m s⁻²; $\mu_0 = 4\pi\times10^{-7}$ H m⁻¹;
$\rho_w = 1000$ kg m⁻³; $c_p = 4186$ J kg⁻¹ K⁻¹;
$\alpha_\mathrm{thermal} = 5\times10^{-4}$ K⁻¹;
$\mu = 2.5\times10^{-4}$ Pa s; $\lambda = 2.0$ W m⁻¹ K⁻¹.

---

## ★ Foundational

**★1.** A borehole in a sedimentary basin has a thermal conductivity of
3.0 W m⁻¹ K⁻¹ and a gradient of 35 K km⁻¹; the surface temperature is 10 °C.

(a) Compute the heat flow in mW m⁻².
(b) Compute the temperature at 2 km assuming a purely linear profile.
(c) Recompute the heat flow if the conductivity were 2.0 W m⁻¹ K⁻¹ with the same
gradient, and state which of the two inputs a heat-flow study controls better.
(d) State why a heat-flow map is described as the product of two measured fields.

---

**★2.** A heat flow of 60 mW m⁻² enters a rock column of
$k = 2.5$ W m⁻¹ K⁻¹ that contains a distributed radiogenic source of
3 µW m⁻³; the surface temperature is 10 °C.

(a) Compute the temperature at 4 km without the source term.
(b) Compute it with the source term.
(c) Compute the difference.
(d) State why the difference is negligible at 1 km and significant at 4 km.

---

**★3.** A magnetotelluric survey works at periods up to 100 s over a half-space
of resistivity 20 Ω m.

(a) Compute the skin depth at 10 s.
(b) Compute it at 100 s.
(c) Compute the resistivity–period product that would give a skin depth of 5 km.
(d) State what is being measured and what is *not* being measured by the method.

---

## ★★ Applied

**★★4.** A saturated layer has a permeability of $10^{-13}$ m², a thickness of
1500 m and a temperature contrast of 120 K across it.

(a) Compute the porous-media Rayleigh number.
(b) Compare it with the critical value $4\pi^{2}$ and state the regime.
(c) Compute the layer thickness at which the layer would be exactly critical.
(d) State which two inputs of the calculation are the least well known and by how
much they would have to change to reverse the conclusion.

---

**★★5.** A geothermal reservoir is 5 km³ of rock with a density of
2700 kg m⁻³, a heat capacity of 900 J kg⁻¹ K⁻¹ and a temperature excess of 150 K
above the reference.

(a) Compute the heat in place in joules and in PJ.
(b) Express the recoverable heat symbolically in terms of a recovery factor $R$
and state the units of $R$.
(c) Compute how the heat in place changes if the volume is doubled and if the
temperature excess is doubled, and state which is the larger effect per unit of
relative change.
(d) State three things the recovery factor depends on that are not geophysical.

---

**★★6.** The demo reports the Cagniard apparent resistivity of a section
consisting of a 500 m thick, 5 Ω m cap over a 500 Ω m half-space.

(a) Report the apparent resistivity at 0.01, 1, 100 and 10 000 s.
(b) Compute the ratio of the 1 s value to the true cap resistivity, and of the
10 000 s value to the true basement resistivity.
(c) Explain why an interpreter who read only the 1 s value would conclude that the
reservoir is a conductor.
(d) State the period range that would be required for a *thicker* cap, and why.

---

## ★★★ Research-oriented

**★★★7.** Run [`../code/geothermal_systems_demo.py`](../code/geothermal_systems_demo.py)
and report:

(a) three of the heat-flow values from the conductivity–gradient table;
(b) the temperature profile with and without the radiogenic source at 1, 2, 3 and
5 km;
(c) the Rayleigh number and the ratio to $4\pi^{2}$ for the five $H$–$\Delta T$
cases;
(d) the heat in place for the three volumes and temperature contrasts, and the
thermal power for the three mass flow rates at two temperature contrasts;
(e) the skin depth at 1, 10 and 100 s for 1, 10 and 1000 Ω m;
(f) the apparent resistivity table for the three sections at seven periods, and
the check on the half-space column;
(g) the temperature excess for the three anomalous heat flows at 0.5, 1, 2 and
3 km.

(h) In three sentences, state which outputs are derived formulas, which are
parameterisations, and which are engineering inputs.

---

**★★★8.** Interpretation and its limits.

(a) A temperature log is straight over 2 km with a constant gradient. State what
that implies about the heat transport regime, and name two processes that would
produce the same appearance without conduction being the mechanism.
(b) An MT survey images a conductive layer at 1 km. A colleague calls it "the
geothermal reservoir". Rewrite the statement correctly, and state what additional
measurement would test it.
(c) A prospectus gives a resource figure with a stated recovery factor of 10 per
cent. Explain, in three sentences, why that number cannot be checked by any
geophysical survey, and what a geophysical study *can* contribute to the estimate.
(d) A heat-flow map shows a 20 mW m⁻² anomaly over a 50 km wide area. List three
possible causes, one of which is not thermal, and state the observation that would
discriminate each.
