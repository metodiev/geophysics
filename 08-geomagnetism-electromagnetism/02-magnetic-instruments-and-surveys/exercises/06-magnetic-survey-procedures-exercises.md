# Exercises — 08-02-06 Magnetic Survey Design, Diurnal Correction and Levelling

Attempt these before reading the
[solutions](./06-magnetic-survey-procedures-solutions.md). The lesson is
[06 Magnetic Survey Design, Diurnal Correction and Levelling](../06-magnetic-survey-procedures.md).
All survey parameters are **SYNTHETIC** teaching values.

Use the synthetic axial dipole coefficient $g_1^0 = -30000\ \mathrm{nT}$,
$a = 6371\ \mathrm{km}$ and $1\ \mathrm{deg} = 111.195\ \mathrm{km}$.

## ★ Foundational

**★1.** A diurnal variation is a $20\ \mathrm{nT}$ sinusoid of 24-hour period.
Compute the peak residual left by correcting with a base reading taken 10 minutes
late.

**★2.** Compute the north–south main-field gradient (nT/km) at $40^{\circ}$
latitude for the synthetic dipole, and the field span across a 30 km
north–south survey there.

**★3.** A target anomaly has a wavelength of $80\ \mathrm{m}$. State the line
spacing under the quarter-wavelength rule and the Nyquist threshold.

## ★★ Applied

**★★4.** A reference model is applied 3 years out of date with a secular
variation of $-40\ \mathrm{nT\,yr^{-1}}$. Compute the resulting error in
$g_1^0$, then state (with the lesson's 0.1883% shape-factor change) how much that
error varies across a 20 km survey at $45^{\circ}$ latitude, and compare it with
a 1 km position error at $4.5\ \mathrm{nT\,km^{-1}}$.

**★★5.** A levelling adjustment uses six lines and nine tie-line crossings and
leaves a residual mistie of $0.4\ \mathrm{nT}$. State what the adjustment
determines, what it assumes, and what it cannot remove at all.

**★★6.** An error budget has contributions of 0.2, 0.8, 1.5 and 0.3 nT. Compute
the quadrature sum, the dominant term's share of the variance, and the
contribution of the smallest term as a percentage. State which improvement would
halve the total.

## ★★★ Research-oriented

**★★★7.** Design a ground magnetic survey for a target whose expected anomaly is
$5\ \mathrm{nT}$ at $20\ \mathrm{m}$ depth with a strike length of at least
$100\ \mathrm{m}$. State the sensor, the station spacing, the line spacing, the
base-station arrangement, the levelling scheme and the expected total
uncertainty. State which single term you would spend more money on. A
specification that could not be executed is a failed answer.

**★★★8.** Derive the residual of a lagged diurnal correction for a general
signal $D(t)$: show that it equals $\delta\,\dot D(t)$ to first order in the lag.
Then show that a *linear* drift is removed exactly up to a constant offset
(absorbed by levelling) while a *curved* drift leaves a residual that varies with
time. State the sampling interval this implies for the base station.
