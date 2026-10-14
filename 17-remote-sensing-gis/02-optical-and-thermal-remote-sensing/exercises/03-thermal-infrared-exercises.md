# Exercises — 17-02-03 Thermal Infrared: Land Surface Temperature and Heat Flow

Attempt these before reading the
[solutions](./03-thermal-infrared-solutions.md). The lesson is
[03 Thermal Infrared: Land Surface Temperature and Heat Flow](../03-thermal-infrared.md).
All parameters are **SYNTHETIC** teaching values.

Constants: $h = 6.62607015\times10^{-34}\ \mathrm{J\,s}$,
$c = 2.99792458\times10^{8}\ \mathrm{m\,s^{-1}}$,
$k_B = 1.380649\times10^{-23}\ \mathrm{J\,K^{-1}}$.

Reference values from the lesson: NEΔT $= 0.14\ \mathrm{K}$;
$k = 2.5\ \mathrm{W\,m^{-1}\,K^{-1}}$; $\alpha = 1.0\times10^{-6}\
\mathrm{m^{2}\,s^{-1}}$; anomaly layer $L = 25\ \mathrm{m}$;
$\partial T/\partial\ln\varepsilon = 67.56\ \mathrm{K}$ at $10.8\ \mathrm{\mu m}$,
$300\ \mathrm{K}$.

## ★ Foundational

**★1.** Compute $\lambda k_BT^{2}/(hc)$ at $\lambda = 12.0\ \mathrm{\mu m}$,
$T = 290\ \mathrm{K}$, and hence the temperature error produced by a $2\%$
emissivity error.

**★2.** Compute the thermal skin depth for a semi-diurnal period of $12\ \mathrm{h}$.

**★3.** Compute the surface temperature anomaly produced by a $0.15\
\mathrm{W\,m^{-2}}$ flux anomaly crossing $50\ \mathrm{m}$ of material with
$k = 3.0\ \mathrm{W\,m^{-1}\,K^{-1}}$, and express it in units of NEΔT.

## ★★ Applied

**★★4.** Derive the split-window relation
$T_s \approx T_{b,1} + a(T_{b,1}-T_{b,2}) + b$ from the two-band brightness
temperatures, and state explicitly which physical term it cancels and which
physical term it retains.

**★★5.** For the diurnal and annual waves, compute the amplitude factor at
$0.60\ \mathrm{m}$ depth and interpret the difference in terms of what a
$0.60\ \mathrm{m}$ soil-temperature measurement records.

**★★6.** A band spans $9$–$11\ \mathrm{\mu m}$. Compute the band-averaged Planck
radiance at $300\ \mathrm{K}$ and compare it with the band-centre value; state
whether the approximation is acceptable for a retrieval with a $0.1\ \mathrm{K}$
error budget.

**★★7.** Using NEΔT $= 0.14\ \mathrm{K}$, compute the minimum detectable flux
anomaly at $3\sigma$ for an anomaly expressed over (a) $10\ \mathrm{m}$ and (b)
$100\ \mathrm{m}$ with $k = 2.5\ \mathrm{W\,m^{-1}\,K^{-1}}$, and comment.

## ★★★ Research-oriented

**★★★8.** Two thermal bands provide two radiance measurements. Show that they do
not determine the surface temperature and both emissivities without an additional
constraint, count the unknowns and equations, and specify two physically
defensible constraints. State which one you would use for a bare-rock target and
why.

**★★★9.** Design an observation strategy to detect a $0.1\ \mathrm{W\,m^{-2}}$
geothermal flux anomaly with the synthetic instrument of this module. State the
acquisition times, the ancillary data required, the confounds you must model, and
the specific test that would distinguish a real geothermal anomaly from an
energy-balance artefact. A specification that could not be executed is a failed
answer.
