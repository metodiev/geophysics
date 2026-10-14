# Exercises — 23-02-04 Active-Source Fieldwork: Sources, Spreads, Shooting Patterns

Attempt these before reading the
[solutions](./04-active-source-fieldwork-solutions.md). The lesson is
[04 Active-Source Fieldwork](../04-active-source-fieldwork.md). All values are
**SYNTHETIC**.

## ★ Foundational

**★1.** A split spread has 72 channels at a 12.5 m receiver interval. Compute the
midpoint fold for shot intervals of 25 m and 50 m. State the unit of the fold.

**★2.** The same survey is shot 500 times with 144 traces per shot, 3000 samples
per trace and 4 bytes per sample. Compute the number of traces and the data volume
in MB.

## ★★ Applied

**★★3.** Noise between stacks is correlated with $\rho = 0.02$. For $M = 24$
stacks compute the noise variance factor, the achieved gain, the effective stack
count and the loss in dB relative to the uncorrelated case. State the asymptotic
gain as $M \to \infty$ and check your value against it.

**★★4.** A two-layer refraction model has $V_1 = 800\ \mathrm{m/s}$,
$V_2 = 2800\ \mathrm{m/s}$ and $h = 15\ \mathrm{m}$. Compute the critical angle,
the intercept time, the crossover distance, $\partial h/\partial t_i$, and the
depth change produced by a 1 ms intercept-time error.

## ★★★ Research-oriented

**★★★5.** Design an acquisition for a target at 30 m depth with a target depth
accuracy of ±1 m using a two-layer refraction interpretation: state the velocity
information you need and how you would obtain it, the required offset range, the
receiver spacing and spread length, the number of shots per kilometre, and the
resulting sensitivity of depth to the velocities and to a 2 ms pick error. Show
the arithmetic. A specification that could not be executed is a failed answer.

**★★★6.** Specify a repeatability test for a source and receiver spread: state
the measurement, the metric with units, the acceptance threshold, the causes of
failure it detects, and two things it cannot establish. A specification that could
not be executed during a survey is a failed answer.
