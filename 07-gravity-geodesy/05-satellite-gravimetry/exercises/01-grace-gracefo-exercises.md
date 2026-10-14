# Exercises — 07-05-01 GRACE and GRACE-FO: Mission Concept and Data Products

Attempt these before reading the
[solutions](./01-grace-gracefo-solutions.md). The lesson is
[01 GRACE and GRACE-FO](../01-grace-gracefo.md). **All models and data in this
module are SYNTHETIC**; the orbit, noise and Love-number values are teaching
values, not mission parameters.

Useful constants: $G = 6.67430\times10^{-11}\ \mathrm{m^{3}\,kg^{-1}\,s^{-2}}$,
$GM = 3.986004418\times10^{14}\ \mathrm{m^{3}\,s^{-2}}$,
$R = 6371\ \mathrm{km}$ (rounded), $\rho_w = 1000\ \mathrm{kg\,m^{-3}}$.

## ★ Foundational

**★1.** For a synthetic circular orbit at $h = 450\ \mathrm{km}$ compute the
period $T$, the speed $v$, the number of revolutions per day and the equatorial
track spacing. State the unit of each.

**★2.** A synthetic surface load changes degree 2 by $\Delta C_{20} =
3\times10^{-11}$. Compute the equivalent water height using
$k_2 = -0.30$, $\rho_e = 5513.4\ \mathrm{kg\,m^{-3}}$ and $R = 6371\ \mathrm{km}$.
State in one sentence why this number is not the depth of a local lake.

**★3.** The demonstration reports a downward-continuation amplification of
$4.89$ at degree 20. Recompute it from $a/R = 1.07848$ and state what it means
for a coefficient noise of $2\times10^{-12}$ at that degree.

## ★★ Applied

**★★4.** Re-derive the identity
$\delta a_\rho = -Gm\rho/q^{3}$ for a point mass below the link midpoint,
stating the symmetry argument. Then evaluate it for a synthetic
$5\ \mathrm{cm}$ water-equivalent anomaly over a disc of radius $200\ \mathrm{km}$,
using $q = 500\ \mathrm{km}$ and $\rho = 200\ \mathrm{km}$, and compare with a
stated noise of $1\times10^{-10}\ \mathrm{m\,s^{-2}}$.

**★★5.** Using the demonstration's amplification factor $a/R = 1.07848$, find
the highest degree for which the continuation amplification stays below
$3\times$, and state the corresponding half-wavelength $\pi R/l$. Compare with
the $10\times$ answer of $l = 29$.

**★★6.** A synthetic orbit at $h = 500\ \mathrm{km}$ has a repeat cycle of
$61$ days. A colleague proposes halving the cycle to $30$ days to double the
temporal resolution. Using the orbit geometry of the demonstration, state the
number of revolutions in each cycle, and give one reason the proposal is not
free.

## ★★★ Research-oriented

**★★★7.** Design a numerical experiment to measure the **leakage** of a
synthetic disc anomaly of radius $300\ \mathrm{km}$ into the coefficients that
would be used to report a *neighbouring* region. Specify: how you will forward
model the mass into coefficients, which degree range you will keep, which filter
you will apply, what metric you will report, and what you expect to see as the
filter radius grows. A specification that could not be executed is a failed
answer.

**★★★8.** The EWH conversion uses a degree-dependent factor $(2l+1)/(1+k_l)$
with $k_2 = -0.30$. Suppose the quoted $k_l$ were wrong by $10\%$ for all
$l \ge 2$ but correct at $l = 0,1$. Show how the error propagates into
(i) a single coefficient's EWH, and (ii) a spatially uniform national-scale
mass trend whose power is concentrated between degrees 2 and 8. State which of
the two is more robust and why.
