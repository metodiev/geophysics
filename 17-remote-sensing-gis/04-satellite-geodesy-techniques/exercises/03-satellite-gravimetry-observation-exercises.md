# Exercises — 17-04-03 Satellite Gravimetry as an Observation System

Attempt these before reading the
[solutions](./03-satellite-gravimetry-observation-solutions.md). The lesson is
[03 Satellite Gravimetry](../03-satellite-gravimetry-observation.md). All models
are **SYNTHETIC** teaching values.

Constants: $GM = 3.986\,004\,418\times10^{14}\ \mathrm{m^{3}\,s^{-2}}$,
$R_E = 6371\ \mathrm{km}$, $J_2 = 1.082\,626\,68\times10^{-3}$,
$G = 6.674\,30\times10^{-11}\ \mathrm{m^{3}\,kg^{-1}\,s^{-2}}$,
M2 period $12.4206012\ \mathrm{h}$.

## ★ Foundational

**★1.** Compute the orbital speed and period for a circular orbit at
$300\ \mathrm{km}$ altitude.

**★2.** Compute the attenuation $(d/(d+h))^{2}$ at $h = 250\ \mathrm{km}$ for
anomalies at $d = 5$, $50$ and $200\ \mathrm{km}$, and state which the orbit is
suited to.

**★3.** For a 5-day repeat cycle, compute the M2 alias period.

## ★★ Applied

**★★4.** **(a)** Compute the equatorial ground-track spacing for a repeat cycle of
12 revolutions. **(b)** State what that spacing means for the along-track sampling
of the static field. **(c)** If the mission also needs a 4-day repeat to separate
a seasonal signal, is that compatible with 12 revolutions? Explain.

**★★5.** The drag acceleration at $250\ \mathrm{km}$ is $3.0\times10^{-6}\ \mathrm{m\,s^{-2}}$
and the scientific signal is $5\times10^{-8}\ \mathrm{m\,s^{-2}}$. **(a)** What
fraction of the drag must be known? **(b)** State why no thermosphere model
achieves it, and what is done instead. **(c)** What does the accelerometer's own
calibration error then become?

**★★6.** **(a)** For a mass anomaly at $100\ \mathrm{km}$ depth, compute the mass
required to produce $1\times10^{-8}\ \mathrm{m\,s^{-2}}$ at $250\ \mathrm{km}$
altitude. **(b)** Compare with the $9.364\times10^{12}\ \mathrm{kg}$ required for a
surface mass, and interpret the ratio.

## ★★★ Research-oriented

**★★★7.** Design the orbit and the measurement concept for a mission that must
resolve the seasonal cycle of a $20\ \mathrm{km}$-deep mass anomaly with an
amplitude of $2\times10^{-8}\ \mathrm{m\,s^{-2}}$ at the satellite. Specify the
altitude, the repeat cycle, the instrument suite, the error terms you must control
and the alias structure you would choose. Justify each number from the lesson. A
specification that could not be executed is a failed answer.

**★★★8.** The lesson's crossover-degree table is computed from a *synthetic*
spectrum $\sigma_n = A/n^2$ and a *synthetic* noise. **(a)** State precisely how
the reported solution above the crossover degree should be described, and why
calling those coefficients "measured" is wrong. **(b)** If the true spectrum were
steeper (say $n^{-3}$), predict the direction of the change in the crossover
degree and justify it. **(c)** Explain how a higher-altitude orbit shifts the
crossover degree in *both* directions, naming the competing effects.
