# Exercises — 06-09-08 Time-Lapse (4-D) Seismic and Reservoir Monitoring

Attempt these before reading the
[solutions](./08-4d-seismic-solutions.md). The lesson is
[08 4-D Seismic](../08-4d-seismic.md). All models are **SYNTHETIC** teaching
values.

## ★ Foundational

**★1.** Two surveys have a difference rms of $0.05$ and mean trace rms of
$0.40$. Compute NRMS under the lesson's convention (rms difference divided by
the mean rms of the two traces) and state the result in per cent.

**★2.** The demonstration's detection table lists the 3-sigma difference floor
as $0.00424$ for a noise rms of $0.001$ and $0.04243$ for $0.010$. Verify both
numbers from the noise rms, and state the factor that relates the difference
noise to the individual-survey noise.

**★3.** The demonstration's top reservoir interface has a baseline two-way time
of $0.5385\ \mathrm{s}$ with a reservoir velocity of $3000\
\mathrm{m\,s^{-1}}$. Compute the interface depth. Then compute the time at which
the same interface would appear in the monitor ($v = 3180\ \mathrm{m\,s^{-1}}$,
$+6.0\%$) under a uniform velocity change, and state the direction of the time
shift. Finally state whether the demonstration's own two reflection-coefficient
changes (top $+0.0386 \to +0.0676$, base $+0.1356 \to +0.1069$) are consistent
with a *local* reservoir change or with a global velocity change, and why.

## ★★ Applied

**★★4.** Derive the $\sqrt{2}$ factor relating the difference noise to the
individual-survey noise, and state the assumption it requires. Then state what
the factor becomes if the two surveys have *correlated* noise (a repeatable
acquisition signature).

**★★5.** A feasibility study has single-survey noise $\sigma = 0.015$ and an
expected 4-D signal of $0.060$ inside the reservoir window. Using a $3\sigma$
threshold on the difference, decide whether the survey is feasible, and compute
the margin as a ratio.

**★★6.** The demonstration reports a difference rms of $0.02543$ inside the
reservoir window and $0.00422$ outside it, a ratio of $6.02$. Explain what the
ratio measures, what value it would take for a *random* difference, and why the
*spatial pattern* rather than the amplitude is the discriminator.

## ★★★ Research-oriented

**★★★7.** Design a 4-D QC plan. List the metrics you would compute, the window
in which each is computed, the decision each supports, and the threshold that
would halt the survey. Include at least one metric that tests the *spatial*
plausibility of the difference and one that tests the *repeatability* of the
acquisition.

**★★★8.** The demonstration's non-uniqueness section (lesson text) shows that a
velocity change and a density change can produce the same 4-D amplitude at one
angle. Design the measurement that separates them, and state what it costs.
