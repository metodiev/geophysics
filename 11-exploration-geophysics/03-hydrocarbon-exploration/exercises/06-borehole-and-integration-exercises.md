# Exercises — 11-03-06 Integrating Borehole Data with Seismic

Attempt these before reading the
[solutions](./06-borehole-and-integration-solutions.md). The lesson is
[06 Integrating Borehole Data with Seismic](../06-borehole-and-integration.md).
All models are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** A sonic log gives $v_p = 3.20\ \mathrm{km\,s^{-1}}$ and a density log
$2.35\ \mathrm{g\,cm^{-3}}$ at one depth, and $3.60\ \mathrm{km\,s^{-1}}$ and
$2.42\ \mathrm{g\,cm^{-3}}$ at the next. Compute the acoustic impedances and the
reflection coefficient.

**★2.** For $v(z) = 1900 + 0.40z$ m/s, compute the two-way time to 2 km and the
depth that would be inferred from that time if the analyst used
$v_0 = 2000\ \mathrm{m\,s^{-1}}$ with the same gradient.

**★3.** State why the density average in a net-to-gross cell is exact and the
velocity average is only exact for the transit time, in two sentences.

## ★★ Applied

**★★4.** A tie requires shifts of 20 ms at 1.0 s and 44 ms at 2.0 s. Diagnose
the problem and estimate the fractional velocity error. State what you would
change in the model, and the depth error at 2.5 km if you did not.

**★★5.** A two-component stack is 35% sand ($v_p = 3.50$, $v_s = 2.00\,
\mathrm{km\,s^{-1}}$, $\rho = 2250\ \mathrm{kg\,m^{-3}}$) and 65% shale
($v_p = 2.85$, $v_s = 1.60$, $\rho = 2400$). Compute the Backus $C_{33}$,
$C_{11}$ and the vertical and horizontal P velocities, then verify the vertical
velocity against the travel-time average.

**★★6.** A 30 Hz zero-phase synthetic correlates at 0.62 with the seismic. A 60°
phase error is then proposed. Using the demonstration's table, state the
correlation and the picked-lobe displacement you would expect, and the depth
error at 3 km.

## ★★★ Research-oriented

**★★★7.** Design a calibration programme for a target at 3.2 km in a basin
where regional velocity-function form is unknown. State the measurement types,
their depth sampling, the model forms you would test, the metric for choosing
between them, and the expected depth accuracy. Justify the number of levels with
the demonstration's noise study.

**★★★8.** Derive the Backus expressions for $C_{33}$ and $C_{11}$ for a
two-component layered medium from the strain and stress continuity conditions,
and show that $C_{11} > C_{33}$ for any contrast in the elastic moduli. State
the wavelength condition that the derivation assumes.
