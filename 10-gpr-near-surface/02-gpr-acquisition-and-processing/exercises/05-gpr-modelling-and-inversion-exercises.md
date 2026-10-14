# Exercises — 10-02-05 GPR Modelling and Full-Waveform Inversion

Attempt before the [solutions](./05-gpr-modelling-and-inversion-solutions.md).
Lesson: [05 Modelling and Inversion](../05-gpr-modelling-and-inversion.md).
All models **SYNTHETIC**.

## ★ Foundational

**★1.** Compute the CFL limit for $h = 0.015\ \mathrm{m}$ and
$v_{\max} = 0.11\ \mathrm{m\,ns^{-1}}$, and state whether
$\Delta t = 0.045\ \mathrm{ns}$ is stable.

**★2.** Write the convolutional forward model for reflectors at $1.0$ and
$2.5\ \mathrm{m}$ with $R = +0.2$ and $-0.15$, $v = 0.1\ \mathrm{m\,ns^{-1}}$,
and give their two-way times.

**★3.** Convert a misfit of $9.8166$ to $7.4751$ into dB.

## ★★ Applied

**★★4.** A modelled reflection arrives $0.25\ \mathrm{ns}$ late at
$h = 0.02\ \mathrm{m}$. Compute the error at $h = 0.01\ \mathrm{m}$ if it scales
as $h^{1.6}$ (the observed trend) and state what test you would run to confirm
the trend.

**★★5.** State the adjoint equation for the scheme of equation (1.3) and explain
in one sentence why its solution is obtained by running the same recursion
backwards.

**★★6.** A starting model is wrong by $8\ \mathrm{ns}$ in travel time at
$f_0 = 200\ \mathrm{MHz}$. Compute the fraction of a period and decide whether
cycle skipping is a risk, using the measured first spurious minimum at
$0.91$ of a period.

## ★★★ Research-oriented

**★★★7.** Design a verification suite for an FDTD GPR modelling code before it
is used for inversion: list five tests, the quantity each measures, and the
criterion for passing.

**★★★8.** One FWI iteration with $10\%$ noise and four starting models gives
values $0.1010$, $0.0999$, $0.0972$ and $0.1009\ \mathrm{m\,ns^{-1}}$ at a fixed
location, against a true anomaly of $+0.040\ \mathrm{m\,ns^{-1}}$ on a
$0.100\ \mathrm{m\,ns^{-1}}$ background. Compute the mean, the standard deviation
and the fraction of the true contrast they represent, and state how you would
report the result.
