# Exercises — 13-06-03 Glacial Isostatic Adjustment: Ice, Viscosity and Sea Level

Attempt these before reading the
[solutions](./03-glacial-isostatic-adjustment-solutions.md). The lesson is
[03 Glacial Isostatic Adjustment](../03-glacial-isostatic-adjustment.md) and its
numbers come from
[`code/glacial_isostatic_adjustment_demo.py`](../code/glacial_isostatic_adjustment_demo.py).
All models are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** Compute $\tau = 4\pi\eta/(\rho g\lambda)$ for $\eta = 5\times10^{20}$ Pa s,
$\rho = 3300$ kg/m³, $g = 9.81$ m/s² and $\lambda = 2500$ km, in years.

**★2.** Compute the equilibrium deflection $w_{\text{eq}} = (\rho_i/\rho_m)h$ for a
2.5 km ice load with $\rho_i = 917$ and $\rho_m = 3300$ kg/m³.

**★3.** For $\tau = 4000$ yr and an ice-free interval of 12 kyr, compute the
remaining fraction of the deflection, $\exp(-t/\tau)$.

## ★★ Applied

**★★4.** With the deflection from ★2 and the decay from ★3, compute the
present-day uplift rate in mm/yr, and state which two factors it combines.

**★★5.** Explain in three sentences why the present-day uplift rate has a maximum
at an intermediate viscosity, and use the lesson's measured values to locate
that maximum at $\lambda = 3000$ km.

**★★6.** For a 2 km ice load over $10^{6}$ km² with an ocean area of
$3.6215\times10^{14}$ m², compute the eustatic sea-level change in metres and
compare it with the measured isostatic deflection at the load centre.

**★★7.** The lesson measures a present-day relative sea-level rate of
$-8.944$ mm/yr at the load centre and $-4.472$ mm/yr at a flank site. Explain the
ratio and state what a sea-level record at the flank alone would imply about
global ice volume if the solid-Earth response were ignored.

## ★★★ Research-oriented

**★★★8.** A target uplift of 10.0 mm/yr is matched by $\eta = 1.0\times10^{21}$
Pa s with a 2.24 km ice sheet and by $\eta = 1.0\times10^{22}$ Pa s with a 6.69 km
ice sheet. Design the observation that would discriminate between them, stating
the observable, the wavelength band and the precision required.

**★★★9.** Design a synthetic recovery test for the viscosity profile: state the
"truth", the observables, the metric, and what a successful recovery would look
like, including the resolution of the recovered profile that you would claim.

**★★★10.** The model neglects the water load and self-gravitation. Explain
qualitatively how each changes (a) the relaxation time and (b) the relative
sea-level prediction near the ice margin, and state which of the two effects you
expect to dominate at $\lambda = 3000$ km.
