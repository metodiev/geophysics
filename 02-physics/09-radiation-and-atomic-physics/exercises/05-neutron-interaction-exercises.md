# Exercises — 02-09-05 Neutron Interactions and Borehole Nuclear Measurements

Attempt these **closed-book** before opening the
[solutions](./05-neutron-interaction-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/neutron_interaction_demo.py`](../code/neutron_interaction_demo.py)
require you to run it and report its actual output. **Every answer must state
whether a cross section is a tabulated 2200 m/s value, an effective value over a
thermal spectrum, or a model input**, and must give the compilation for the first
two.

Tabulated values to use (state them): thermal (2200 m/s) absorption cross
sections in barns: H 0.332, O 0.00019, C 0.0035, Si 0.171, Cl 33.5; elastic
scattering: H 20.4, O 4.232, C 4.74;
$N_A = 6.022\,140\,76 \times 10^{23}$ mol⁻¹, $1\ \mathrm{barn} = 10^{-24}$ cm²;
$k_B = 1.380\,649 \times 10^{-23}$ J K⁻¹;
$m_n = 1.674\,927\,5 \times 10^{-27}$ kg.

---

## ★ Foundational

**★1.** (a) Compute the kinetic energy of a neutron of speed 2200 m s⁻¹, in eV.
(b) Compute $\tfrac32 k_BT$ at 293.6 K, in eV.
(c) Compute the ratio of the two and explain which convention a tabulated
"thermal" cross section uses.
(d) State the physical reason a $1/v$ absorber's effective cross section over a
Maxwellian spectrum is *lower* than its 2200 m/s value.

---

**★2.** (a) Compute $\xi$ for $A = 1.008$ and for $A = 12.011$ from
$\xi = 1 + \frac{(A-1)^2}{2A}\ln\frac{A-1}{A+1}$.
(b) Compute the maximum fractional energy loss $4A/(1+A)^2$ for each.
(c) Compute $\ln(E_0/E_\mathrm{th})$ for a 4.5 MeV source neutron slowing to
0.025 eV.
(d) Compute the mean number of collisions to thermalise for each nuclide and
state which moderates better per collision.

---

**★3.** A thermal neutron in water. Water has
$N_\mathrm{H} = 6.6857 \times 10^{22}$ cm⁻³ and
$N_\mathrm{O} = 3.3429 \times 10^{22}$ cm⁻³.

(a) Compute $\Sigma_a$ for hydrogen, for oxygen and for water.
(b) Compute the absorption mean free path.
(c) Compute $\Sigma_s$ for water and the scattering mean free path.
(d) Explain what the ratio of the two mean free paths tells you about neutron
transport in water.

---

## ★★ Applied

**★★4.** The moderating ratio. Graphite has $\rho = 1.70$ g cm⁻³,
$M = 12.011$ g mol⁻¹, $\sigma_a = 0.0035$ b and $\sigma_s = 4.74$ b.

(a) Compute $N$, $\Sigma_a$ and $\Sigma_s$.
(b) Compute the moderating ratio $\xi\Sigma_s/\Sigma_a$ using your $\xi$ from ★2.
(c) Compare with the demo's graphite value and with its values for water (62.2)
and heavy water (4476.6).
(d) Explain, in terms of the cross sections, why heavy water beats light water
even though hydrogen needs fewer collisions to slow down.

---

**★★5.** The gas effect. Sandstone: $\rho_\mathrm{ma} = 2.65$,
$\rho_\mathrm{water} = 1.00$, true porosity 0.25, gas density 0.10 g cm⁻³,
gas is methane ($\mathrm{CH}_4$).

(a) Compute the hydrogen index of the gas.
(b) Compute the bulk density and the density porosity $\phi_D$ at
$S_g = 0.5$.
(c) Compute the model neutron porosity $\phi_N$ at $S_g = 0.5$ and the separation
$\phi_D - \phi_N$.
(d) Explain why the separation, and not either reading, is the gas indicator.

---

**★★6.** The photoelectric factor of calcite ($\mathrm{CaCO_3}$).

(a) Compute $Z_\mathrm{eff} = \left(\sum n_iZ_i^4/\sum n_iZ_i\right)^{1/3}$.
(b) Compute $\mathrm{Pe} = (Z_\mathrm{eff}/10)^{3.6}$.
(c) Compute $2Z/A$ and the electron density index at
$\rho = 2.71$ g cm⁻³.
(d) Compare (b) with the commonly published calcite Pe of 5.08, state the
percentage difference, and explain why the *ordering* of the matrix Pe values is
a stronger conclusion than the absolute agreement.

---

## ★★★ Research-oriented

**★★★7.** Run [`../code/neutron_interaction_demo.py`](../code/neutron_interaction_demo.py)
and report:

(a) the two thermal-energy conventions and their ratio;
(b) $\xi$ and the collisions to thermalise for hydrogen and for silicon;
(c) the absorption and scattering mean free paths in water;
(d) the moderating ratios for the four media;
(e) the hydrogen index of gas at 0.20 g cm⁻³ and of liquid methane;
(f) the computed and published Pe for quartz and dolomite, with the percentage
differences;
(g) the fraction of captures on chlorine in seawater;
(h) two sentences on which outputs are exact computations, which are tabulated
and which are declared model inputs.

---

**★★★8.** Interpretation.

(a) A shale interval reads 35 per cent apparent neutron porosity while its
density porosity is 12 per cent. Give the physical reason and name the
independent measurement needed to correct it.
(b) A gas-bearing sand shows the two porosities diverging; a barite-weighted mud
changes the density response. Explain which of the three logs in the suite is
least affected and why.
(c) A formation's neutron response is said to be "set by its strongest absorber".
Using the demo's figures for 1 g L⁻¹ of boron, quantify the statement for a pore
fluid containing 500 ppm of boron.
(d) Explain why a thermal-neutron measurement cannot be interpreted as a
porosity without knowing the matrix, in terms of the moderating ratio of the
matrix compared with that of water.
