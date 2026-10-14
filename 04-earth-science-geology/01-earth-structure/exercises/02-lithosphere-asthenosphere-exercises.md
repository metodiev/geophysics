# Exercises — 04-01-02 Lithosphere, Asthenosphere and the Rheological Definition

Attempt these **closed-book** before opening the
[solutions](./02-lithosphere-asthenosphere-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/lithosphere_asthenosphere_demo.py`](../code/lithosphere_asthenosphere_demo.py)
require you to run it and report its actual output. Use $g = 9.81$ m/s² and the
Julian year $3.15576\times10^7$ s.

---

## ★ Foundational

**★1.** A rock has $\eta = 1.0\times10^{20}$ Pa·s and $\mu = 6.5\times10^{10}$ Pa.

(a) Compute $\tau_M = \eta/\mu$ in seconds and in years.
(b) Compute the Deborah number for a seismic period of 1 s and for a load
lasting 1 Ma.
(c) State which regime applies in each case.

---

**★2.** Airy isostasy.

(a) Compute the root-to-topography ratio $r/h$ for $\rho_c = 2750$ and
$\rho_m = 3300$ kg/m³.
(b) Compute the root beneath 3 km of topography.
(c) Compute the Moho depth beneath it, taking the regional Moho as 35 km.
(d) Explain in one sentence what the ratio would be if the mantle density were
larger.

---

**★3.** Flexure.

(a) Compute the flexural rigidity $D = ET_e^3/[12(1-\nu^2)]$ for $E = 70$ GPa,
$T_e = 20$ km and $\nu = 0.25$.
(b) Compute the flexural parameter $\alpha = (D/\rho_m g)^{1/4}$.
(c) State the load width above which flexural support dominates buoyancy.

---

## ★★ Applied

**★★4.** Post-glacial rebound.

(a) Compute the relaxation time for a load of wavelength 2500 km with
$\eta = 10^{21}$ Pa·s and $\rho = 3300$ kg/m³.
(b) Invert: what viscosity is required for an observed 5000 a relaxation at that
wavelength?
(c) State how the answer changes if the same 5000 a is observed at a wavelength
of 5000 km, and give the physical reason.

---

**★★5.** The temperature sensitivity of viscosity.

(a) Using $\eta \propto \exp(E_a/RT)$ with $E_a = 300$ kJ/mol, compute the ratio
$\eta(1600\,\text{K})/\eta(1700\,\text{K})$.
(b) Compute the ratio over the range 1500 to 1700 K.
(c) Compute the temperature rise at 1600 K that reduces the viscosity by a
factor of ten.
(d) Compare (c) with the 200 K anomaly that a lithosphere–asthenosphere boundary
might involve, and state the implication for the rheological contrast.

---

**★★6.** The seismic signature of the same anomaly.

Take $v_s = 4500$ m/s and $\mathrm{d}v_s/\mathrm{d}T = -0.5$ m/s per K.

(a) Compute the velocity change for the temperature rise in ★5(c).
(b) Express it as a percentage.
(c) State the ratio between the viscosity change (a factor of ten) and the
velocity change, and explain why the two columns move on completely different
scales.

---

## ★★★ Research-oriented

**★★★7.** Invert the demo's rebound table.

(a) Run the demo and record the $\eta$ column for wavelengths 1000, 3000 and
6000 km.
(b) Fit a power law $\eta \propto \lambda^m$ to those three points and report
$m$.
(c) Explain why $m$ is what it is, working from $\tau = 2\eta k/\rho g$ and the
assumption of a fixed observed $\tau$.
(d) State what a rebound dataset with five wavelengths would give that three
would not.

---

**★★★8.** Run
[`../code/lithosphere_asthenosphere_demo.py`](../code/lithosphere_asthenosphere_demo.py)
and report:

(a) the Maxwell relaxation times for the asthenosphere and the mantle, and the
Deborah numbers for a 1 s seismic wave and for plate motion;
(b) the computed span of the Deborah number across the five loads, in orders of
magnitude;
(c) $\alpha$ and $D$ at $T_e = 60$ km;
(d) the Airy root and Moho depth for $h = 4$ km;
(e) the $\eta/\eta_0$ values at 1300 K and 1900 K and the ratio between them;
(f) the $\mathrm{d}v_s/v_s$ values at the same two temperatures;
(g) three sentences on what the ratio in (e) divided by the ratio in (f) says
about the difficulty of mapping the asthenosphere seismically.

---

**★★★9.** Critique the Maxwell model. State three ways in which the real
mantle's rheology differs from a single-relaxation-time Maxwell solid, and for
each, name an observation that the Maxwell model therefore mis-predicts.
