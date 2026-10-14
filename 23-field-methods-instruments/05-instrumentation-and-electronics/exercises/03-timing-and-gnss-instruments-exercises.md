# Exercises — 23-05-03 Timing, GNSS Disciplining and Clock Accuracy

Attempt these before reading the
[solutions](./03-timing-and-gnss-instruments-solutions.md). The lesson is
[03 Timing and GNSS Instruments](../03-timing-and-gnss-instruments.md). All values
are **SYNTHETIC**.

## ★ Foundational

**★1.** A clock has a fractional error of $2.5\times10^{-7}$. Compute the time
error after 6 h and after 15 days, and the apparent distance error after 6 h at an
apparent velocity of 2.5 km/s.

**★2.** A station's holdover is $5\times10^{-8}$ per day. Compute the drift per day
and the time a 0.5 ms timing budget survives.

## ★★ Applied

**★★3.** PPS jitter is 30 ns rms and 400 pulses are averaged. Compute the effective
jitter. Then state the one component of the PPS error that averaging cannot reduce.

**★★4.** An oscillator has $\sigma_y(1\ \mathrm{s}) = 5\times10^{-12}$. Compute
$\sigma_y(1000\ \mathrm{s})$ under white-frequency-noise scaling, and the accumulated
*random* time error over one day. Compare that with the *systematic* error over the
same day for the same oscillator.

## ★★★ Research-oriented

**★★★5.** Design the timing plan for a 30-station temporary array whose science
requires a 0.5 ms relative timing accuracy: state the reference and its
disciplining, the holdover you would require and how you would verify it, the
maintenance re-visit interval, the logging you would keep, and the check made at a
site visit. Show the arithmetic.

**★★★6.** Specify a test that establishes the *absolute* timing offset of a
recording system against a reference: state the equipment, the method, the metric
with units, the repeatability required, and the two systematic effects that the test
cannot distinguish. A specification that could not be executed in the field is a
failed answer.
