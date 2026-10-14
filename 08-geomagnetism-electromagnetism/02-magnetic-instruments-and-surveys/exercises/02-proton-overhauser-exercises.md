# Exercises — 08-02-02 Proton Precession and Overhauser Magnetometers

Attempt these before reading the
[solutions](./02-proton-overhauser-solutions.md). The lesson is
[02 Proton Precession and Overhauser Magnetometers](../02-proton-overhauser.md).
All sensor parameters are **SYNTHETIC** teaching values; the proton gyromagnetic
ratio is a standard constant.

Use $\gamma_p = 2.6752218744\times10^{8}\ \mathrm{rad\,s^{-1}\,T^{-1}}$.

## ★ Foundational

**★1.** Compute the precession frequency at $B = 45000\ \mathrm{nT}$.

**★2.** A frequency counter resolves $1.0\ \mathrm{mHz}$. What field change does
that correspond to?

**★3.** For $T_2^{*} = 2.0\ \mathrm{s}$, compute the fraction of the initial
signal amplitude remaining after 1.0 s, 2.0 s and 6.0 s of precession.

## ★★ Applied

**★★4.** From the lesson's table, the frequency error is 0.00552604 Hz at
SNR $= 1$ and 0.00005598 Hz at SNR $= 100$. Verify the $1/\mathrm{SNR}$ law, and
compute the SNR needed for a 0.01 nT field precision at the same counting time.

**★★5.** A pulsed sensor polarises for 5.0 s, acquires for 1.0 s, and has 0.3 s
of overhead. Compute the cycle time, the duty cycle and the number of readings
per hour. Compare with a continuous sensor sampled at the same 1.0 s cadence and
state the ratio of readings per hour.

**★★6.** Using the counting-time table (SNR fixed at 10), estimate the counting
time needed to reach 0.01 nT, first by assuming the steep $T^{-3/2}$ scaling and
then by reading the table. Explain the discrepancy.

## ★★★ Research-oriented

**★★★7.** Specify a scalar magnetometer for a survey that must reach 0.05 nT
precision with one reading per 2 s, naming the target SNR, the counting time, the
duty cycle and the sensor-amplitude requirement. State which requirement is
hardest and how you would test the finished instrument. A specification that
could not be executed is a failed answer.

**★★★8.** Derive the Cramér–Rao bound for the frequency of a sinusoid of
amplitude $A$ observed for a time $T$ at sampling rate $f_s$ in white noise of
standard deviation $\sigma$: show that
$\sigma_f \propto \sigma/(A\,T^{3/2})$, and explain why a damped signal with
envelope time $T_2^{*}$ cannot follow that law beyond $T \sim T_2^{*}$.
