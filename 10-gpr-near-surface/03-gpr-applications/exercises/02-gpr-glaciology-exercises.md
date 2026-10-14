# Exercises — 10-03-02 GPR for Glacier Thickness and Internal Stratigraphy

Attempt these before reading the
[solutions](./02-gpr-glaciology-solutions.md). The lesson is
[02 GPR for Glacier Thickness and Internal Stratigraphy](../02-gpr-glaciology.md).
All models and data in this module are **SYNTHETIC**: the ice thickness, firn
density, absorption coefficients and ages below are teaching values. The only
non-chosen numbers are physical constants and standard material values
($c = 0.299792458\ \mathrm{m\,ns^{-1}}$,
$\rho_{\mathrm{ice}} = 917\ \mathrm{kg\,m^{-3}}$,
$\varepsilon_{\mathrm{ice}} = 3.17$,
$\varepsilon_w = 80.1$, $R = 8.314462618\ \mathrm{J\,mol^{-1}K^{-1}}$).

## ★ Foundational

**★1.** Firn of density $600\ \mathrm{kg\,m^{-3}}$ over ice of
$\varepsilon_r = 3.17$. Compute the pore fraction, the firn permittivity from
CRIM, the firn speed, the two-way time through $30\ \mathrm{m}$ of it, and the
wavelength in firn at $20\ \mathrm{MHz}$.

**★2.** A bed is recorded at a two-way time of $14\,253.46\ \mathrm{ns}$. Convert
it to a depth with $\varepsilon_r = 3.17$ and with $\varepsilon_r = 3.40$. Give
both depths, the difference in metres and per cent, and the value predicted by
the linear sensitivity.

**★3.** State the units of $E_a/R$ and of $1/T - 1/T_0$, and verify that the
Arrhenius exponent is dimensionless.

## ★★ Applied

**★★4.** An $800\ \mathrm{m}$ bed is recorded with a $2\ \mathrm{ns}$ pick
standard deviation and the ice permittivity is known only to $3\%$. Compute the
depth standard deviation contributed by each term and the total, and state which
term dominates.

**★★5.** Ice over two different beds. Compute $R$ for ice
($\varepsilon_r = 3.17$) over water ($\varepsilon_r = 80.1$) and over rock
($\varepsilon_r = 5.0$); compute each in dB relative to the air/ice surface echo
($R = -0.2807$) and in dB relative to each other. State what a measurement of the
bed amplitude must additionally account for before either number can be used.

**★★6.** Using the lesson's Arrhenius absorption model with the SYNTHETIC
coefficients $\alpha_0 = 0.020\ \mathrm{dB\,m^{-1}}$ at $-20\ ^\circ\mathrm{C}$
and $E_a = 6.0\times10^{4}\ \mathrm{J\,mol^{-1}}$, compute the one-way
attenuation at $-25\ ^\circ\mathrm{C}$ and the depths at which a $60\ \mathrm{dB}$
and a $100\ \mathrm{dB}$ two-way budget are spent. Explain in one sentence why the
answer at $-25\ ^\circ\mathrm{C}$ is not simply a linear interpolation between the
$-20$ and $-30\ ^\circ\mathrm{C}$ values.

## ★★★ Research-oriented

**★★★7.** A station reports a thickness between two internal horizons computed
with a uniform-ice conversion and, separately, with a firn + ice conversion, and
finds the same number to $0.001\ \mathrm{m}$. Prove algebraically that this
cancellation is exact, state the two conditions it requires, and compute the
thickness error introduced if the firn thickness differs by $5\ \mathrm{m}$
between the two horizon locations (firn density $500\ \mathrm{kg\,m^{-3}}$, ice
$\varepsilon_r = 3.17$, thickness about $252\ \mathrm{m}$).

**★★★8.** Two internal horizons are picked at $3000\ \mathrm{ns}$ and
$6000\ \mathrm{ns}$; a dated core gives the age gap as $500\ \mathrm{a}$. Compute
the accumulation rate with $\varepsilon_r = 3.17$ and with
$\varepsilon_r = 3.2334$. State three assumptions the arithmetic inherits that
the radar cannot test, and for each say what independent measurement would test
it.

**★★★9.** Design an amplitude-based procedure to map the bed condition (water /
saturated till / rock) along a $10\ \mathrm{km}$ profile at $20\ \mathrm{MHz}$.
Your answer must specify the reference amplitude, the corrections that must be
applied to a bed echo before it can be compared with the reference, the spatial
resolution you will claim, and the way you will report a bed that is
intermediate between two of the three cases. A specification that could not be
executed is a failed answer.
