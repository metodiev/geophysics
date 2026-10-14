# Exercises — 06-13-03 Volcano Seismology: LP Events, Tremor and Eruption Forecasting

Attempt these before reading the
[solutions](./03-volcano-seismology-solutions.md). The lesson is
[03 Volcano Seismology](../03-volcano-seismology.md). All models are
**SYNTHETIC** teaching models.

## ★ Foundational

**★1.** An LP event has a spectral peak at $1.50\ \mathrm{Hz}$ and a
$-3\ \mathrm{dB}$ width of $0.075\ \mathrm{Hz}$. Compute $Q$, the damping
constant $\sigma = \pi f_0/Q$ and the decay time $1/\sigma$, with units. State
how long the ringing lasts (take $6\tau$).

**★2.** For ★1, compute the size of the peak shift:
$f_{\text{peak}} = f_0\sqrt{1 - 1/(4Q^{2})}$. Express it as a percentage of $f_0$
and state whether it is measurable with a $0.01\ \mathrm{Hz}$ spectral resolution.

**★3.** Define RSAM in words and as an equation, give its units for a velocity
record, and state the one free parameter.

## ★★ Applied

**★★4.** A precursor has hit rate $h = 0.9$ and false-alarm rate $f = 0.25$.
Compute the precision at base rates $p = 0.4$, $0.05$ and $0.002$. Then compute
the effect of halving $f$ to $0.125$ at $p = 0.002$, and compare it with the
effect of raising $h$ to $0.99$ at the same $p$.

**★★5.** Using the lesson's measured RSAM table, an observatory wants a mean
latency under $20\ \mathrm{s}$ and fewer than $5$ false alarms per quiet period
of $415.9\ \mathrm{s}$. State which window(s) satisfy each requirement, and
whether any window satisfies both. Give the arithmetic for your choice.

**★★6.** A resonance is fitted with a single damped oscillator, but the data
contain a second peak at twice the frequency with half the amplitude. Explain in
three sentences how the single-mode fit will distribute the misfit between $Q$
and the amplitude, and state whether the recovered $Q$ will be biased high or
low.

## ★★★ Research-oriented

**★★★7.** Design a monitoring protocol for a volcano whose eruptions have a base
rate of $1$ per $30$ days of unrest. Specify the observable, the band, the
window, the threshold rule, the alarm logic (how many crossings, over what
duration), the expected latency and false-alarm rate you would defend, and the
reporting format. State explicitly which numbers your protocol needs from data
you do not yet have.

**★★★8.** The lesson shows that a detector's optimum window differs between a
narrowband and a broadband objective. Construct the analogous argument for
volcanic monitoring: give one volcanic target that is narrowband (a dispersed LP
phase you intend to invert for $Q$) and one that is broadband (tremor envelope),
and state for each the window, the gauge/threshold choice, and what the choice
sacrifices. Then state one situation in which the two objectives conflict
directly, and how you would resolve it in an operational setting.
