# Exercises — 06-09-02 Reflection Processing Flow: Deconvolution, NMO, Stack, Migration

Attempt these before reading the
[solutions](./02-processing-flow-solutions.md). The lesson is
[02 Processing Flow](../02-processing-flow.md). All models are **SYNTHETIC**
teaching values.

## ★ Foundational

**★1.** A reflection has zero-offset two-way time $t_0 = 1.0\ \mathrm{s}$ and
velocity $v = 2500\ \mathrm{m\,s^{-1}}$. Compute its two-way time at
$x = 1500\ \mathrm{m}$ and the moveout $\Delta t$ in milliseconds.

**★2.** Using the demonstration's values $t_0 = 1.4251\ \mathrm{s}$ and
$v_{\text{rms}} = 2848.1\ \mathrm{m\,s^{-1}}$, compute the *hyperbolic* time at
$x = 3002\ \mathrm{m}$ and compare with the printed $1.7725\ \mathrm{s}$. State
the size of the exact-minus-hyperbolic residual at that offset.

## ★★ Applied

**★★3.** Derive $t(x) = \sqrt{t_0^{2} + x^{2}/v^{2}}$ from the mirror-image
geometry of a single horizontal interface, and state precisely where the
derivation assumes a constant velocity.

**★★4.** The demonstration measures the stacking improvement at folds 4, 8 and
16 as $2.04$, $2.98$ and $4.48$, against $\sqrt{N} = 2.00$, $2.83$, $4.00$.
Compute the ratio measured/predicted at each fold, and state whether the
stacking is better or worse than the $\sqrt{N}$ law and what that implies about
the noise.

**★★5.** The demonstration's *coherent* event is attenuated only from $1.000$ to
$0.916$ after a 16-fold stack. Compute what the ratio would be if the event
averaged down like random noise, and state in one sentence why the difference is
the reason SRME and Radon methods exist.

## ★★★ Research-oriented

**★★★7.** Design a processing sequence for a marine data set with a strong
water-bottom multiple and a deep target. Justify the position of deconvolution,
velocity analysis, NMO, mute, Radon/demultiple and migration, and state for each
step the QC measurement that would show it had failed. You do not need to run
it, but a sequence whose steps are not independently testable is a failed
answer.

**★★★8.** The demonstration's stacked peak sits at $1.428\ \mathrm{s}$ against an
expected $1.4251\ \mathrm{s}$, and the maximum hyperbolic residual over the spread
is $79.06\ \mathrm{ms}$. State which of the two numbers limits the accuracy of a
stacked pick for a *velocity* analysis, and design a measurement that would
separate the NMO-stretch bias from the stacking-time quantisation.
