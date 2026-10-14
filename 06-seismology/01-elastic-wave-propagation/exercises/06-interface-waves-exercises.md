# Exercises — 06-01-06 Interface Waves, Head Waves and the Total Wavefield

Attempt these before reading the
[solutions](./06-interface-waves-solutions.md). The lesson is
[06 Interface Waves, Head Waves and the Total Wavefield](../06-interface-waves.md);
all numbers are printed by
[`../code/interface_waves_demo.py`](../code/interface_waves_demo.py). All models
are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** For $v_1 = 1500\ \mathrm{m\,s^{-1}}$, $v_2 = 3000\ \mathrm{m\,s^{-1}}$,
$H = 20\ \mathrm{m}$, compute the critical angle, the head-wave intercept time and
the crossover distance, showing the unit of each factor.

**★2.** A refraction line over a SYNTHETIC layer gives a head-wave intercept time
of $15\ \mathrm{ms}$ and an apparent velocity of $2500\ \mathrm{m\,s^{-1}}$. If
$v_1 = 1500\ \mathrm{m\,s^{-1}}$, compute $H$ and state which physical quantity the
apparent velocity measures.

**★3.** State the condition on the velocity contrast for a head wave to exist, and
describe in two sentences what happens to the wavefield when the condition fails
(the hidden-layer case).

## ★★ Applied

**★★4.** The demonstration compares its analytic arrival times with a
grid-shortest-path calculation. At $x = 400\ \mathrm{m}$ it reports relative
differences of $2.733\times10^{-2}$ ($\Delta x = 4\ \mathrm{m}$),
$1.777\times10^{-2}$ ($\Delta x = 2\ \mathrm{m}$) and $1.299\times10^{-2}$
($\Delta x = 1\ \mathrm{m}$). Compute the measured order of convergence from the
two consecutive ratios, and state what order a second-order scheme would show.

**★★5.** The demonstration's trapped-mode scan reports every root with
$c/\min(v_s) \ge 0.980676$. State the derivation of the bound
$0 < c < \min(v_{s1},v_{s2})$, then explain why a measured *lower* bound of
$0.980676$ (rather than 0) is an informative statement about the contrast, and
what it implies for identifying the arrival on a record.

**★★6.** At the root $c = 2894.2775\ \mathrm{m\,s^{-1}}$ the demonstration reports
a smallest/largest singular-value ratio of $5.916\times10^{-16}$, while 5% away
from the root it reports $1.542\times10^{-1}$. Explain what is being measured,
why a *rank* test is stronger than a sign change of the determinant, and by what
factor the two numbers differ.

## ★★★ Research-oriented

**★★★7.** Design an experiment that locates the existence boundary of the trapped
mode as a function of the density ratio $\rho_2/\rho_1$ at fixed
$v_{s2}/v_{s1} = 1.00$. State the scan range, the root-finding tolerance, the
resolution in density ratio, and the exact quantity you would report. A
specification that could not be executed is a failed answer.

**★★★8.** The lesson states that head-wave *amplitudes* are not computed, because
they require an asymptotic treatment of a branch-line integral. Specify a
numerical experiment that would measure the head wave's amplitude decay with
offset, state the functional form you would fit, and say what physical assumption
the asymptotic result needs that a purely numerical experiment would not.

**★★★9.** The scan finds no trapped mode at $v_{s2}/v_{s1} = 0.60$ for any of the
five density ratios tried. State precisely what this does and does not prove, and
describe the single numerical change that would convert the statement from "not
found" to a genuine exclusion.
