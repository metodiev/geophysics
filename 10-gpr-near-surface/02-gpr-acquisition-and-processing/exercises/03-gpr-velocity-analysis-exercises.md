# Exercises — 10-02-03 Velocity Analysis and CMP Sounding

Attempt before the [solutions](./03-gpr-velocity-analysis-solutions.md). Lesson:
[03 Velocity Analysis](../03-gpr-velocity-analysis.md). All models **SYNTHETIC**.

## ★ Foundational

**★1.** Compute the semblance of a two-trace window where the traces are
identical (state the value) and where the second trace is the negative of the
first (state the value).

**★2.** An event has $t_0 = 50.0\ \mathrm{ns}$ and its amplitude arrives at
$58.0\ \mathrm{ns}$ at $x = 3.0\ \mathrm{m}$. Compute $v$.

**★3.** Compute the ray parameter $p$ corresponding to
$v = 0.075\ \mathrm{m\,ns^{-1}}$ in the GPR convention, with units.

## ★★ Applied

**★★4.** For $v = 0.0740\ \mathrm{m\,ns^{-1}}$, $t_0 = 66.7\ \mathrm{ns}$ and
$x = 4.0\ \mathrm{m}$, compute the analytic velocity error from a
$0.25\ \mathrm{ns}$ pick error. Compare it with the measured $0.9$-of-peak
semblance width of $0.0020\ \mathrm{m\,ns^{-1}}$ and interpret the difference.

**★★5.** Repeat ★★4 for $x_{\max} = 1.0\ \mathrm{m}$ and state the design
consequence for a zero-offset (monostatic) profile.

**★★6.** Two picks are $(40.0\ \mathrm{ns}, 0.0600)$ and $(67.3\ \mathrm{ns},
0.0740)$. Compute the interval velocity and the change produced by a $+5\%$ error
in each of the four inputs in turn.

## ★★★ Research-oriented

**★★★7.** A semblance scan gives a peak of $0.9956$ at
$v = 0.0740\ \mathrm{m\,ns^{-1}}$ for a two-layer event whose exact forward model
has $v_{\text{nmo}} = 0.0735$. Explain why a *high* semblance value coexists with
a biased velocity, and state what you would report.

**★★★8.** Design a velocity-analysis programme that determines the interval
velocity of a $1.5$–$3.0\ \mathrm{m}$ layer to $5\%$ in a medium with
$v_1 = 0.06$ and $v_2 = 0.09\ \mathrm{m\,ns^{-1}}$, giving the offsets, the
expected semblance width and one independent cross-check.
