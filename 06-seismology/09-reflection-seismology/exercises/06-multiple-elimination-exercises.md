# Exercises — 06-09-06 Multiple Attenuation: SRME, Radon and Deconvolution

Attempt these before reading the
[solutions](./06-multiple-elimination-solutions.md). The lesson is
[06 Multiple Elimination](../06-multiple-elimination.md). All models are
**SYNTHETIC** teaching values.

## ★ Foundational

**★1.** Compute the parabolic curvature $q = 1/(2t_0v^{2})$ for a primary at
$t_0 = 1.2\ \mathrm{s}$, $v = 2400\ \mathrm{m\,s^{-1}}$ and for a multiple at
$t_0 = 2.0\ \mathrm{s}$, $v = 1500\ \mathrm{m\,s^{-1}}$. State the ratio
$q_{\text{mult}}/q_{\text{prim}}$ and its units.

**★2.** Verify the demonstration's two curvatures, $8.000\times10^{-8}$ and
$1.929\times10^{-7}\ \mathrm{s\,m^{-2}}$ (primary $t_0 = 1.00\ \mathrm{s}$,
$v = 2500\ \mathrm{m\,s^{-1}}$; multiple $t_0 = 1.80\ \mathrm{s}$,
$v = 1200\ \mathrm{m\,s^{-1}}$), and confirm the printed ratio $2.41$.

## ★★ Applied

**★★3.** Derive the parabolic (small-offset) approximation of hyperbolic moveout
and state the neglected term explicitly with its order in $x$.

**★★4.** In the demonstration, muting 4 of 31 curvature rows preserves $85.2\%$
of the primary and leaves $84.4\%$ of the multiple, so the
primary/multiple amplitude ratio moves only from $1.240$ to $1.251$. Explain
why a curvature mute is so blunt here, and propose one change to the
*inversion* (not the mute) that would sharpen it.

**★★5.** The demonstration's predictive deconvolution reduces a periodic
multiple's amplitude from $0.8000$ to $0.3220$ (a factor $2.48$) while leaving
the primary at $1.0000$. Compute the attenuation in decibels and state the
second effect of predictive deconvolution that the table does *not* show.

## ★★★ Research-oriented

**★★★6.** Design a three-stage multiple-attenuation sequence for a marine data
set with strong water-bottom multiples. For each stage state the mechanism it
exploits, the QC number that shows it worked, and the failure mode that would
make the *next* stage worse. Order the stages and justify the order.

**★★★7.** The Radon round-trip residual is $1.30\%$ with 400 LSQR iterations.
State what would happen to the mute's selectivity if the residual were instead
$30\%$, and design the experiment that would establish the dependence of the
mute trade-off (primary preserved versus multiple removed) on the number of
iterations.
