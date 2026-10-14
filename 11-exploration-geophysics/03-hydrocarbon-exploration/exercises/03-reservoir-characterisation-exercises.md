# Exercises — 11-03-03 Reservoir Characterisation and Property Prediction

Attempt these before reading the
[solutions](./03-reservoir-characterisation-solutions.md). The lesson is
[03 Reservoir Characterisation and Property Prediction](../03-reservoir-characterisation.md).
All models are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** A sand has $\phi = 0.22$, $K_m = 36.6$ GPa, $\mu_m = 45.0$ GPa,
$\phi_c = 0.40$, $\rho_m = 2650\ \mathrm{kg\,m^{-3}}$ and brine
($K = 2.2$ GPa, $\rho = 1000\ \mathrm{kg\,m^{-3}}$). Compute $K_{\text{dry}}$,
$\mu_{\text{dry}}$, $K_{\text{sat}}$ by Gassmann, then $v_p$, $v_s$, $\rho$,
impedance and $v_p/v_s$. Show every intermediate quantity.

**★2.** For a mixture of 70% gas and 30% brine (by pore volume), compute
$K_{\text{fl}}$ and $\rho_{\text{fl}}$ and state the two mixing laws used.

**★3.** State the units of acoustic impedance in SI and in MRayl, and convert
$Z = 9.7\times10^{6}\ \mathrm{kg\,m^{-2}\,s^{-1}}$ into MRayl.

## ★★ Applied

**★★4.** Using the model of ★1, substitute gas ($S_g = 0.7$): compute the new
$K_{\text{sat}}$, $v_p$, $\rho$, impedance and the percentage change in
impedance. Separate the contribution of the density change from that of the
velocity change.

**★★5.** Two facies have $\text{AI} = 9.7$ and $10.3$ MRayl and $v_p/v_s = 1.466$
and $1.511$, with $\sigma_{\text{AI}} = 0.5$ MRayl and
$\sigma_{v_p/v_s} = 0.045$. Compute the separation in standard deviations for
AI alone and for the two attributes jointly, and state what the difference means
for a classification.

**★★6.** A cell contains 60% net sand ($\phi = 0.20$, brine, properties from
★1 and the lesson) and 40% shale ($v_p = 2.80\ \mathrm{km\,s^{-1}}$,
$\rho = 2450\ \mathrm{kg\,m^{-3}}$). Compute the cell density, the cell velocity
by the transit-time average and the cell impedance. State which of the two
averages is exact and why.

## ★★★ Research-oriented

**★★★7.** A prospect has a base rate of 0.04 and an attribute pair giving a
likelihood ratio of 12. Compute the posterior for four priors (0.50, 0.20, 0.05,
0.02) and state the threshold you would use if a dry hole costs 1 and a
discovery returns 8. Justify the threshold with the expected-value arithmetic.

**★★★8.** Construct a rock-physics ambiguity: find two (porosity, gas
saturation) pairs that give the same impedance within 0.5% but $v_p/v_s$
differing by more than 2%. State the numerical method you used, the tolerance,
and the interpretation you would write for a cell whose measured attributes are
the average of the two.
