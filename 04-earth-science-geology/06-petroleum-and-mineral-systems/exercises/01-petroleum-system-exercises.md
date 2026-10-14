# Exercises — 04-06-01 Source, Reservoir, Seal and Trap

Attempt these **closed-book** before opening the
[solutions](./01-petroleum-system-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/petroleum_system_demo.py`](../code/petroleum_system_demo.py) require
you to run it and report its actual output. **Every rate must name the coefficient
it depends on, and no answer may quote a reserve, a recovery factor or a
production volume.**

Values to use: $R = 8.314$ J mol⁻¹ K⁻¹; $g = 9.81$ m s⁻²;
$1$ yr $= 3.15576\times10^{7}$ s;
$A = 10^{13}$ s⁻¹, $E_a = 2.0\times10^{5}$ J mol⁻¹ for the single-reaction kinetic
model; $\rho_\mathrm{water} = 1030$ kg m⁻³.

---

## ★ Foundational

**★1.** A basin has a surface temperature of $15\ ^\circ$C and a geothermal
gradient of 30 K km⁻¹.

(a) Compute the temperature at 3 km.
(b) Compute the depths of the $60\ ^\circ$C and $120\ ^\circ$C limits of the
liquid-hydrocarbon window in this basin.
(c) Recompute both depths for a gradient of 20 K km⁻¹.
(d) State in one sentence why the window is a temperature interval rather than a
depth interval.

---

**★2.** Using the single-reaction model with $E_a = 2.0\times10^{5}$ J mol⁻¹ and
$A = 10^{13}$ s⁻¹:

(a) Compute the rate constant at $110\ ^\circ$C.
(b) Compute the isothermal time to 10 per cent conversion in years.
(c) Compute the same time at $90\ ^\circ$C and the ratio to (b).
(d) State what is wrong with using this single reaction to predict the maturity
of a real source rock.

---

**★3.** A mudstone follows Athy's law with $\phi_0 = 0.45$ and $c = 2500$ m.
Grain density is 2650 kg m⁻³ and pore water 1030 kg m⁻³.

(a) Compute the porosity at 1500 m.
(b) Compute the bulk density at 1500 m.
(c) Compute both at 3000 m.
(d) State which of the two depths has a larger *rate* of density increase per
metre, and why.

---

## ★★ Applied

**★★4.** A seal has an interfacial tension of $0.025$ N m⁻¹ and a
characteristic pore-throat radius of $0.5$ µm.

(a) Compute the capillary entry pressure.
(b) Compute the maximum gas column the seal supports, taking
$\rho_\mathrm{gas} = 200$ kg m⁻³ and $\rho_\mathrm{water} = 1050$ kg m⁻³.
(c) Compute the maximum oil column for $\rho_\mathrm{oil} = 750$ kg m⁻³.
(d) State which of the four inputs the answer is most sensitive to, and by what
power.

---

**★★5.** A shale has $\rho = 2450$ kg m⁻³ and $v_P = 3200$ m s⁻¹.

(a) Compute its acoustic impedance.
(b) Compute the reflection coefficient at its top contact with a brine sand of
$\rho = 2150$ kg m⁻³ and $v_P = 2800$ m s⁻¹.
(c) Compute it for a gas sand of $\rho = 2000$ kg m⁻³ and $v_P = 2500$ m s⁻¹.
(d) Compute the ratio of the two amplitudes and state the polarity of each.

---

**★★6.** A reservoir at 3 km depth has an average overburden density of
2400 kg m⁻³ and a pore fluid of density 1030 kg m⁻³.

(a) Compute the vertical stress and the hydrostatic pore pressure.
(b) Compute the vertical effective stress.
(c) Recompute the effective stress if the pore pressure is 1.5 times hydrostatic.
(d) State the percentage change in effective stress and explain why this matters
for a velocity–depth trend.

---

## ★★★ Research-oriented

**★★★7.** Run [`../code/petroleum_system_demo.py`](../code/petroleum_system_demo.py)
and report:

(a) the depths of the 60 °C and 120 °C limits for the three gradients;
(b) the rate constant and the 10 per cent conversion time at 60, 100 and 180 °C;
(c) the heating-rate table, giving the temperature at 10 per cent conversion for
each heating rate;
(d) the porosity, bulk density, vertical stress and effective stress at 500 m and
at 4 km;
(e) the one-way and two-way travel times at 1 and 4 km;
(f) the seal capacities for gas and oil, and the sensitivity to the throat radius;
(g) the reflection coefficients for shale over brine sand, gas sand and limestone,
and the gas/brine amplitude ratio;
(h) the organic-carbon mass for the two source-rock volumes.

(i) In three sentences, identify which of these outputs are computed from a
derived relation, which rest on a parameterisation, and which would have to come
from a measurement in a real study.

---

**★★★8.** Interpretation and its limits.

(a) A prospect has a large four-way closure and a bright seismic amplitude at the
crest. Give two mechanisms that produce a bright amplitude without a commercial
accumulation, and state the observation that would discriminate.
(b) The same source rock generates on a fast-subsidence margin at a greater depth
than on a slow one. Explain why, using the kinetic calculation, and state the
consequence for a play that is mapped by present-day depth alone.
(c) A seal is reported with a single entry pressure. Explain why that is
inadequate and what an appropriate presentation would be.
(d) A colleague proposes to estimate the hydrocarbon volume from a time map and
the amplitude anomaly. List, in order of expected magnitude, the three largest
uncertainties in that estimate, and state which of them is not geophysical.
