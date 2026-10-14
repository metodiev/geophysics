# Exercises — 04-06-05 Unconventional Resources: Shale, Tight Gas, Hydrates

Attempt these **closed-book** before opening the
[solutions](./05-unconventional-resources-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/unconventional_resources_demo.py`](../code/unconventional_resources_demo.py)
require you to run it and report its actual output. **State clearly which
quantities are physical and which are engineering or economic. No recovery factor,
estimated ultimate recovery, resource volume or reserve may be quoted as a fact.**

Values to use: $g = 9.81$ m s⁻²; $\rho_w = 1030$ kg m⁻³;
$\rho_\mathrm{grain} = 2650$ kg m⁻³, $\rho_\mathrm{brine} = 1050$ kg m⁻³,
$\rho_\mathrm{gas} = 200$ kg m⁻³; $K_w = 2.8$ GPa, $K_g = 0.05$ GPa,
$K_\mathrm{min} = 36$ GPa.

---

## ★ Foundational

**★1.** A sandstone has a porosity of 0.15, a dry-frame bulk modulus of 10 GPa
and a mineral bulk modulus of 37 GPa; the pore fluid has a bulk modulus of
2.5 GPa.

(a) Compute the saturated bulk modulus from Gassmann's equation.
(b) State by how much the saturated modulus exceeds the dry one, in per cent.
(c) Explain in one sentence why the saturated rock is stiffer than the dry rock.
(d) State the one assumption of Gassmann's equation that makes the *shear*
modulus usable as a lithology indicator.

---

**★2.** The shear modulus of the rock in ★1 is 8 GPa, and the porosity is 0.30
with a grain density of 2650 kg m⁻³.

(a) Compute the bulk density when fully saturated with brine
($\rho = 1050$ kg m⁻³) and when fully saturated with gas ($\rho = 200$ kg m⁻³).
(b) Compute $v_P$ and $v_S$ for both cases, using the fluid-substituted bulk
moduli of the demo's model if you prefer (brine: 13.02 GPa, gas: 8.10 GPa).
(c) Compute the $v_P/v_S$ ratio for both.
(d) State which velocity is the better lithology indicator and why.

---

**★3.** A shale has $v_P = 4200$ m s⁻¹, $v_S = 2400$ m s⁻¹ and
$\rho = 2550$ kg m⁻³.

(a) Compute Poisson's ratio.
(b) Compute Young's modulus.
(c) State which of the two is more sensitive to an error in $v_S$.
(d) State whether the rock is more likely to be quartz-rich or clay-rich, and why.

---

## ★★ Applied

**★★4.** A brittleness index is defined as the mean of
$(E - 10\ \text{GPa})/50\ \text{GPa}$ and $(0.40 - \nu)/0.20$, each clamped to
$[0,1]$.

(a) Compute the index for the shale of ★3 (from its $E$ and $\nu$).
(b) Compute it for a clay-rich shale with $\rho = 2500$ kg m⁻³,
$v_P = 3100$ m s⁻¹, $v_S = 1600$ m s⁻¹.
(c) State the ordering of the two rocks and whether it is robust.
(d) State what is physical and what is conventional in this calculation.

---

**★★5.** A hydrate stability calculation uses a water depth of 1000 m, a
bottom-water temperature of 3 °C, a geothermal gradient of 35 K km⁻¹, and a
locally linearised dissociation boundary
$T_\mathrm{diss}(P) = 12.5\ ^\circ\mathrm{C} + 0.90\,(P - P_\mathrm{floor})$
with $P$ in MPa.

(a) Compute $P_\mathrm{floor}$ and the pressure gradient in the sediment.
(b) Compute the depth below the seafloor at which the geotherm intersects the
dissociation boundary.
(c) Recompute for a bottom-water temperature of 5 °C.
(d) State the two constants of the phase boundary that a real assessment must
replace, and why.

---

**★★6.** A tight sandstone has a liquid permeability of $5\times10^{-17}$ m² and a
Klinkenberg slip factor of $1.5\times10^{6}$ Pa.

(a) Compute the reported gas permeability at mean pressures of 2 MPa and 15 MPa.
(b) Compute the ratios to the liquid permeability.
(c) Explain why the reported value falls with pressure although the rock does not
change.
(d) Compute the closure stress for $\sigma_v = 45$ MPa, $\alpha = 0.75$,
$p = 20$ MPa and $\nu = 0.28$.

---

## ★★★ Research-oriented

**★★★7.** Run
[`../code/unconventional_resources_demo.py`](../code/unconventional_resources_demo.py)
and report:

(a) the Gassmann table: fluid modulus, saturated modulus, density, $v_P$, $v_S$,
$v_P/v_S$ and $\nu$ for the eight saturations;
(b) the three cases — fully brine, 10 per cent gas, fully gas — with the percentage
changes in $v_P$ and $v_S$;
(c) the moduli and the brittleness indices for the two shale types;
(d) the hydrostatic pressure at the seafloor, the pressure gradient, the boundary
slope, the base of the stability zone, and its sensitivity table;
(e) the BSR reflection coefficient and its polarity;
(f) the Klinkenberg ratios at the five pressures, and the closure stress at the
five Poisson's ratios.

(g) In three sentences, state which outputs are physical, which rest on a
parameterisation, and which would be engineering inputs in a real assessment.

---

**★★★8.** Interpretation and its limits.

(a) A seismic amplitude anomaly over a shale play is interpreted as a fully
gas-charged interval. Using the fizz-gas calculation, explain why the same
amplitude is equally consistent with a 10 per cent gas saturation, and state what
measurement would discriminate.
(b) A prospectus states that a hydrate accumulation "contains" a very large volume
of gas inferred from the areal extent of a BSR. Identify the three separate
assumptions in that statement, and say which are unphysical to assert from seismic
data alone.
(c) A brittleness map from a seismic inversion is used to select drilling
locations. Give two reasons the map could be misleading, and state one
non-geophysical input that the selection also depends on.
(d) A colleague proposes to convert the calculated heat in place of a hot
sedimentary aquifer into an energy capacity by multiplying by a recovery factor of
0.1. State precisely what is wrong with that as a *geophysical* claim, and what
would have to be done to make the number defensible.
