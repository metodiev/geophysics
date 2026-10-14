# Exercises — 15-01-06 Ocean-Atmosphere Coupling and ENSO

Attempt these before reading the
[solutions](./06-ocean-atmosphere-coupling-solutions.md). The lesson is
[06 Ocean-Atmosphere Coupling](../06-ocean-atmosphere-coupling.md). All models
are **SYNTHETIC** teaching values.

Constants: $\rho_{\text{air}} = 1.225\ \mathrm{kg\,m^{-3}}$,
$c_p = 1005\ \mathrm{J\,kg^{-1}\,K^{-1}}$,
$L_v = 2.501\times10^{6}\ \mathrm{J\,kg^{-1}}$,
$C_D = 1.2\times10^{-3}$, $C_H = 1.1\times10^{-3}$, $C_E = 1.2\times10^{-3}$.

## ★ Foundational

**★1.** For $U = 4.0\ \mathrm{m\,s^{-1}}$,
$T_s - T_a = -2.0\ \mathrm{K}$ and $q_s - q_a = -4.0\ \mathrm{g\,kg^{-1}}$,
compute $\tau$, $H$ and $LE$ with units.

**★2.** State which of the three bulk formulas is quadratic in wind speed and
derive the rule for how a fractional error in $U$ propagates to each flux.

**★3.** Write the two recharge-oscillator equations and give the physical
meaning of $R$, $\gamma$, $\epsilon$ and $r$.

## ★★ Applied

**★★4.** For $R = 0.8\ \mathrm{yr^{-1}}$, $r = 0.6\ \mathrm{yr^{-1}}$,
$\gamma = 1.0\ ^\circ\mathrm{C\,(m\,yr)^{-1}}$ and
$\epsilon = 2.9\ \mathrm{m\,(^\circ C\,yr)^{-1}}$, compute $\operatorname{tr}A$,
$\det A$, the eigenvalues, the period and the $e$-folding time. State whether the
mode grows or decays and whether it oscillates.

**★★5.** Derive the condition for the oscillation to disappear,
$\gamma\epsilon = Rr + (R-r)^{2}/4$, and solve it for $r = 0.8\ \mathrm{yr^{-1}}$
with $\gamma = 1.0$ and $\epsilon = 2.7174$. Compare with the lesson's value of
$R = 2.797$ for $r = 0.5$.

**★★6.** The lesson's neutral case has $\epsilon/r = 5.4348\
\mathrm{m\,^\circ C^{-1}}$ and the damped case $2.1266$. Both have a
4.00-year period. (a) State the ratio between them. (b) Explain in two sentences
how two models with the same period can have such different steady thermocline
responses.

**★★7.** Starting from $R = 0.5$, $r = 0.5$, $\gamma = 1.0$,
$\epsilon = 2.7174$, compute $\lambda$ after (a) doubling $R$ and (b) halving
$r$. Report the period and growth rate in each case and state which coefficient
changes the period more.

## ★★★ Research-oriented

**★★★8.** Design a test that would distinguish "damped oscillator driven by
noise" from "self-sustained oscillation" using a synthetic record of length you
choose. State the statistic, the record length, the discriminating feature, and
the assumption about the noise that the test relies on. Then state which of the
two hypotheses the demonstration's own diagnostics (spectrum, segment-to-segment
period scatter, skewness) can and cannot separate.

**★★★9.** The demonstration forces only the $T$ equation with noise. Derive the
transfer function for the case where both equations are forced with independent
white noise, and state qualitatively how the response spectrum's *shape* changes
while the eigenfrequencies do not.
