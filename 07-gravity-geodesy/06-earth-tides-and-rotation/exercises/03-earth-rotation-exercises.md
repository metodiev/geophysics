# Exercises — 07-06-03 Earth Rotation, Polar Motion, LOD and Excitation

Attempt these before reading the
[solutions](./03-earth-rotation-solutions.md). The lesson is
[03 Earth Rotation](../03-earth-rotation.md). **All models and data in this
module are SYNTHETIC.**

Constants used throughout (from the demonstration's stated model):
$C = 8.4022\times10^{37}\ \mathrm{kg\,m^{2}}$,
$\Omega = 7.2921150\times10^{-5}\ \mathrm{rad\,s^{-1}}$,
$\mathrm{LOD} = 86164\ \mathrm{s}$,
$H = (C-A)/A = 0.00327$ (stated synthetic value),
$M = 5.9722\times10^{24}\ \mathrm{kg}$, $R = 6371\ \mathrm{km}$,
$1\ \mathrm{rad} = 206264.8\ \mathrm{arcsec}$.

## ★ Foundational

**★1.** Compute the axial angular momentum that corresponds to a LOD change of
$0.5\ \mathrm{ms}$. State the sign relationship in one sentence.

**★2.** Compute the rigid Euler wobble period for $H = 0.00300$ and for
$H = 0.00350$, and state the percentage change in the period for a $17\%$ change
in $H$.

**★3.** A zonal wind is $20\ \mathrm{m\,s^{-1}}$ everywhere in the northern
hemisphere and zero in the southern. Estimate the axial angular momentum using
the thin-shell formula, stating each factor with its units, and compute the
resulting LOD change.

## ★★ Applied

**★★4.** Verify the $(2/3)M\Omega R^{2}$ factor for a thin shell analytically.
Then state what changes for a thick shell in which the mass is concentrated at
$r < R$, and give the factor for a mass concentrated at $r = R/2$.

**★★5.** A forcing with a 400-day period has excitation amplitude
$\chi_0 = 1.0\times10^{-8}$. Compute the steady pole displacement in mas. Repeat
for a 305-day forcing.

**★★6.** The demonstration's jet gives $H_3 = 5.798\times10^{26}\
\mathrm{kg\,m^{2}\,s^{-1}}$ and a LOD change of $+8.154\ \mathrm{ms}$. A
colleague quotes the same wind with the Earth's mass in the momentum integral and
gets a $10^{6}$-times larger number. Explain what physical error produces that,
and state the check that would catch it.

## ★★★ Research-oriented

**★★★7.** Design a synthetic experiment that measures the effect of omitting the
fluid core on an inferred free-wobble period, and state what observation would
distinguish a core effect from a damping term. Specify the model, the synthetic
data, the analysis and the diagnostic.

**★★★8.** The excitation budget for polar motion is usually written as a sum of
atmosphere, ocean, land water and cryosphere terms. Design a numerical experiment
that measures the *degeneracy* between two of these terms, and state the
additional measurement (or model) that breaks it.
