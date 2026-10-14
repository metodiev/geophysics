# Exercises — 09-06-02 Borehole Radar and Directional Probing

Attempt these before reading the
[solutions](./02-borehole-radar-solutions.md). The lesson is
[02 Borehole Radar and Directional Probing](../02-borehole-radar.md).
All models are **SYNTHETIC** teaching values; the speed of light is a standard
constant.

## ★ Foundational

**★1.** At 200 MHz, compute the phase velocity, the wavelength and the
half-wave resolution for $\varepsilon_r = 4$, $9$ and $25$. State the answer in
metres.

**★2.** A monostatic single-hole survey in $\varepsilon_r = 6$ rock
($v = 1.2239\times10^{8}\ \mathrm{m\,s^{-1}}$) records a reflection at 130.7 ns.
Compute the range, and state two independent quantities that could make that
range wrong by 10%.

**★3.** A cross-hole pick over a straight 20.0 m path is 168.5 ns. Compute the
velocity and the relative permittivity. State the assumption that connects the
permittivity to a water content.

## ★★ Applied

**★4.** For $\varepsilon_r = 9$ and $\sigma = 0.002\ \mathrm{S\,m^{-1}}$ at
200 MHz, compute the loss tangent, the low-loss attenuation in Np/m and in dB/m,
and the two-way amplitude loss over 20 m. Then repeat for
$\sigma = 0.02\ \mathrm{S\,m^{-1}}$ and comment on which of the two is a radar
measurement.

**★5.** A target lies 8.0 m from a single borehole. Give the range, the arc
length left unresolved by a $\pm20^\circ$ antenna, and the arc left by an
omnidirectional antenna. State the criterion you would use to decide whether the
antenna is adequate for a borehole siting decision.

**★6.** The demonstration's cross-hole survey has 80 cells and 64 rays and a
measured rank of 59. Explain why the rank is not 64, and state what the missing
directions do to a model reported from the inversion.

## ★★★ Research-oriented

**★★★7.** Design a two-borehole radar survey whose ray matrix has rank at least
90% of the number of cells. State the cell size, the borehole separation, the
source and receiver depth pattern, the frequency and the expected singular
spectrum, and defend the design against the straight-ray assumption. You may not
use a third borehole.

**★★★8.** The demonstration finds a null-space direction along which a model
perturbation of the same size as the target changes the data by
$6.4\times10^{-14}$ of the picking error. Design an experiment that would make
that direction observable, and state the physical quantity you are adding to the
measurement. A specification that could not be executed is a failed answer.
