# Exercises — 04-01-04 Igneous, Sedimentary and Metamorphic Rocks

Attempt these **closed-book** before opening the
[solutions](./04-rock-types-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/rock_types_demo.py`](../code/rock_types_demo.py) require you to run it
and report its actual output. Use $g = 9.81$ m/s² and $z = P/(\rho g)$ for
depth from pressure.

---

## ★ Foundational

**★1.** A modal analysis gives $Q = 20$, $A = 25$, $P = 35$ per cent of the
Q+A+P total, with 20 per cent mafic minerals.

(a) Normalise Q, A and P to 100 per cent.
(b) Compute $A/(A+P)$ as a percentage.
(c) Name the rock from the QAPF fields (alkali feldspar granite above 90 per
cent, syenogranite 65–90, monzogranite 35–65, granodiorite 10–35, tonalite below
10 per cent, for $Q$ between 20 and 60).
(d) State the colour index and why it matters more than the name.

---

**★2.** Grain size.

(a) Convert 0.5 mm and 0.0625 mm to phi.
(b) Assign a Wentworth class to each.
(c) Convert 2 mm to phi and assign a class.
(d) State the reference unit in the phi formula and what happens if a grain size
in micrometres is substituted.

---

**★3.** Metamorphic facies.

Using the lesson's rules ($P \ge 1.2$ GPa gives eclogite; $P \ge 0.6$ GPa and
$T < 350$ °C gives blueschist; then $T < 200$ zeolite, $< 300$
prehnite-pumpellyite, $< 500$ greenschist, $< 700$ amphibolite), classify:

(a) 0.80 GPa, 600 °C.
(b) 0.45 GPa, 250 °C.
(c) 1.30 GPa, 500 °C.
(d) 0.70 GPa, 300 °C.

---

## ★★ Applied

**★★4.** Folk and Ward statistics. A sample's cumulative curve has
$\phi_5 = 1.024$, $\phi_{16} = 1.462$, $\phi_{50} = 2.318$, $\phi_{84} = 3.388$,
$\phi_{95} = 3.954$.

(a) Compute $M_z$.
(b) Compute $\sigma_I$ from the two-term formula.
(c) Classify the sorting (under 0.35 very well sorted, 0.50 well, 0.71
moderately well, 1.00 moderately, 2.00 poorly).
(d) Convert the median to millimetres and assign a Wentworth class.

---

**★★5.** Depth from pressure.

(a) Compute the depth corresponding to 0.8 GPa at $\rho = 2900$ kg/m³.
(b) Compute it at $\rho = 2500$ kg/m³.
(c) Compute the pressure at 35 km for an average crustal density of 2750 kg/m³.
(d) State why a single conversion factor is a poor habit in the mantle.

---

**★★6.** Two density contrasts by two different mechanisms.

(a) From the lesson's property table, compute the bulk-density contrast between
a granite ($\rho_g = 2.65$, $\phi = 0.01$) and a sandstone ($\rho_g = 2.68$,
$\phi = 0.25$), both dry.
(b) Compute the contrast between a gabbro ($\rho_g = 3.00$, $\phi = 0.02$) and a
peridotite ($\rho_g = 3.30$, $\phi = 0.005$).
(c) State which contrast is mineralogical and which is porosity-driven, and by
what test you would distinguish them in the field.

---

## ★★★ Research-oriented

**★★★7.** Sensitivity of a classification. Take the blueschist boundary in the
lesson's rules and move it from $T < 350$ °C to $T < 300$ °C.

(a) Reclassify the standard continental geotherm's 25 km point (0.69 GPa,
345 °C).
(b) Reclassify the cold subduction geotherm's 35 km point (0.96 GPa, 360 °C).
(c) State how many rows of the three-geotherm table change.
(d) Write two sentences on what that sensitivity says about the use of box
classifications, and what a petrologist does instead.

---

**★★★8.** Run [`../code/rock_types_demo.py`](../code/rock_types_demo.py) and
report:

(a) the five QAPF classifications and whether each check printed `OK`;
(b) the sorting value and its class, and the median grain size and its Wentworth
class;
(c) the facies at 35 km for all three geotherms, with the temperature at each;
(d) the bulk-density ranges for sandstone and granite from the property table;
(e) the facies returned for the extended geotherm at 45 km, and why it is
labelled a partial melt rather than a metamorphic rock;
(f) two sentences on which outputs are computed and which are tabulated.

---

**★★★9.** A bimodal sample. A sediment consists of 60 per cent medium sand
(0.25 to 0.5 mm) and 40 per cent gravel (4 to 8 mm).

(a) Compute the graphical mean $M_z$ from the percentiles such a distribution
would have, and state where it falls relative to the two modes.
(b) Compute $\sigma_I$ and state whether the value describes a depositional
process or a mixture.
(c) State what a sedimentologist would report instead of a single mean and
sorting.
(d) State what a geophysicist predicting permeability from the mean grain size
would get wrong.
