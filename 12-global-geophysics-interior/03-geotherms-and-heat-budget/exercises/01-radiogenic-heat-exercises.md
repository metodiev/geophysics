# Exercises — 12-03-01 Radiogenic Heat Production and Mantle Geotherms

Attempt these before reading the
[solutions](./01-radiogenic-heat-solutions.md). Lesson:
[01 Radiogenic Heat Production and Mantle Geotherms](../01-radiogenic-heat.md).
All models in this module are **SYNTHETIC** teaching models; the isotope data and
compositions below are adopted inputs, not measurements.

## ★ Foundational

**★1.** Compute the specific heat production $H$ of an adopted parent with
$T_{1/2} = 10.0\ \mathrm{Gyr}$, $M = 200\ \mathrm{g\,mol^{-1}}$,
$Q_{\text{tot}} = 40\ \mathrm{MeV}$ and $f_\nu = 0.05$. Show the units at each
step and state the result in $\mathrm{\mu W\,kg^{-1}}$.

**★2.** A synthetic rock has $\rho = 2800\ \mathrm{kg\,m^{-3}}$,
$1.5\ \mathrm{ppm}$ U, $6.0\ \mathrm{ppm}$ Th and $1.5\ \mathrm{wt\%}$ K. Using
the demonstration's adopted specific productions
($H_{^{238}\mathrm{U}} = 97.56$, $H_{^{235}\mathrm{U}} = 570.07$,
$H_{^{232}\mathrm{Th}} = 25.89$, $H_{^{40}\mathrm{K}} = 38.97\
\mathrm{\mu W\,kg^{-1}}$, with isotopic fractions 0.9927, 0.0072, 1.0 and
$1.17\times10^{-4}$), compute the volumetric heat production $A$.

**★3.** A province has $q_0 = 70 \pm 7\ \mathrm{mW\,m^{-2}}$ and
$A_0h = 12 \pm 4\ \mathrm{mW\,m^{-2}}$. Compute $q_{\text{mantle}}$ with its
uncertainty and state which input dominates it.

## ★★ Applied

**★★4.** With $A_0h$ held fixed at $10\ \mathrm{mW\,m^{-2}}$, show that the
radiogenic fraction $A_0h/q_0$ decreases monotonically as $q_0$ increases, and
find the $q_0$ at which it equals 0.20. Then explain in two sentences why the
statement fails when $A_0$ varies between provinces.

**★★5.** A cold anomaly of $\Delta T = -150\ \mathrm{K}$ is assumed beneath a
region with $\rho = 3800\ \mathrm{kg\,m^{-3}}$ and $g = 9.81\
\mathrm{m\,s^{-2}}$. Compute the depth deflection of a transition with
$m = +2.5\ \mathrm{MPa\,K^{-1}}$ and of one with $m = -2.0\
\mathrm{MPa\,K^{-1}}$, and state the resulting change in the separation between
them. Then repeat for a 20% error in each Clapeyron slope and report the error in
the inferred temperature.

**★★6.** Using $T_{\text{ad}}(z) = T_p\exp(\alpha g z/c_p)$ with
$\alpha = 3\times10^{-5}\ \mathrm{K^{-1}}$, $g = 9.81\ \mathrm{m\,s^{-2}}$,
$c_p = 1250\ \mathrm{J\,kg^{-1}\,K^{-1}}$ and $T_p = 1500\ \mathrm{K}$, compute
$T_{\text{ad}}$ at 660 km and at 2891 km, and the error the constant-gradient
approximation makes at each depth.

## ★★★ Research-oriented

**★★★7.** Repeat the Clapeyron calculation of ★5 with a depth-dependent $g$.
Use $g(z) \approx g_s(1 - z/R)$ with $R = 6371\ \mathrm{km}$ and evaluate $g$ at
the mean depth of each transition, then bound the systematic error introduced by
using the surface value. State whether the error is random or systematic.

**★★★8.** The neutrino fraction is the reason K-40 is a weak heat source. Design
an observational test that would *measure* the fraction of decay energy escaping
as neutrinos rather than assume it. Specify the observable, its units, the
scaling with the amount of U and Th in the Earth, and one way the measurement
could be biased.

## Notes on answers

A defensible answer states its assumptions, carries units through every step, and
reports the uncertainty alongside the number. Answers that quote
$q_{\text{mantle}}$ without saying that it is a difference of two measured
quantities will lose marks regardless of the arithmetic.
