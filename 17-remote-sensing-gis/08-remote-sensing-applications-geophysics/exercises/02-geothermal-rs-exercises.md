# Exercises — 17-08-02 Thermal Remote Sensing for Geothermal Systems

Attempt these before reading the
[solutions](./02-geothermal-rs-solutions.md). The lesson is
[02 Thermal Remote Sensing for Geothermal Systems](../02-geothermal-rs.md). All
models and values are **SYNTHETIC** teaching numbers.

## ★ Foundational

**★1.** State whether the brightness temperature of a surface of emissivity
$\varepsilon = 0.9$ is above or below its true temperature, and why. The
Planck inverse is exact — so where does the error come from?

**★2.** With $k = 2.0\ \mathrm{W\,m^{-1}\,K^{-1}}$ and $z = 20\ \mathrm{m}$,
compute the surface temperature anomaly sustained by a heat flux of
$0.15\ \mathrm{W\,m^{-2}}$.

**★3.** State the units of heat flux, thermal conductivity, the geothermal
gradient, and thermal inertia.

## ★★ Applied

**★★4.** Using the detection numbers of the lesson ($\mathrm{NE}\Delta T = 0.20\
\mathrm{K}$, $k = 2.0$, $z = 20\ \mathrm{m}$), compute the smallest flux
detectable on noise alone, and the flux equivalent to a $0.02$ emissivity error
that moves the temperature by $1.37\ \mathrm{K}$. Which dominates?

**★★5.** Interpolate the emissivity table linearly to estimate the temperature
error at $\varepsilon = 0.93$, given $-3.45\ \mathrm{K}$ at $0.95$ and
$-6.99\ \mathrm{K}$ at $0.90$.

**★★6.** Using the thermal-inertia table ($A_0 = 12.0\ \mathrm{K}$ diurnal),
compute the diurnal amplitude at inertia $750$ and compare it with inertia
$3000$.

## ★★★ Research-oriented

**★★★7.** Design a validation of a land-surface-temperature retrieval for
geothermal work. State the reference measurements, the emissivity source, the
atmosphere treatment, the metric, and the one confound that could manufacture a
false anomaly. A specification that could not be executed is a failed answer.

**★★★8.** The lesson claims the detection limit is set by the emissivity model,
not the detector. Argue both for and against this claim, and state the condition
under which a better detector *would* improve detection.
