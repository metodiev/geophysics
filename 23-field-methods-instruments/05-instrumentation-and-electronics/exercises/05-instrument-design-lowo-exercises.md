# Exercises — 23-05-05 Building Low-Cost Instruments for Teaching and Research

Attempt these before reading the
[solutions](./05-instrument-design-lowo-solutions.md). The lesson is
[05 Instrument Design for Low-Cost Builds](../05-instrument-design-lowo.md). All
values are **SYNTHETIC**.

## ★ Foundational

**★1.** A synthetic moving-coil sensor has $S = 25$ V/(m/s) and a $200\ \Omega$ coil.
The requirement is $2\times10^{-6}$ m/s in a $40$ Hz band. Compute the signal voltage
at the requirement and the sensor's Johnson noise, and state the single-sample SNR in
dB if the sensor noise were the only noise.

**★2.** A 16-bit converter with $\pm1.25$ V full scale is used. Compute its LSB and the
quantization noise rms, and the SNR of the ★1 signal against that quantization noise
alone.

## ★★ Applied

**★★3.** The pre-amplifier has $e_n = 8\ \mathrm{nV/\sqrt{Hz}}$ and the band is
$40$ Hz. Compute (a) the amplifier's referred noise; (b) the crossover gain $G^{*}$ at
which quantization and amplifier noise are equal, using the ★2 quantization noise;
(c) the total noise at $G^{*}$ and the resulting SNR for the ★1 signal.

**★★4.** A logger sleeps at 30 µA, acquires at 4 mA for 0.5 % of the time and
transmits at 100 mA for 5 s per day. The battery is 10 Ah of which 60 % is usable.
Compute the average current and the deployment life in days, then state which term you
would attack first and why.

**★★5.** A TCXO-class oscillator has a fractional error of 0.02 ppm. Compute its error
per day and the resynchronisation interval for a 5 ms tolerance. Then state how the
design changes if the science needs 5 ms *relative* between nodes rather than
5 ms absolute.

## ★★★ Research-oriented

**★★★6.** Design a six-month unattended seismic station with a synthetic sensor of
$S = 30$ V/(m/s), a required detection level of $1\times10^{-6}$ m/s in the DC–50 Hz
band, a 20 Ah battery (70 % usable) and no mains power. Produce: the written
requirement; the noise budget with the dominant term identified; the gain you would
choose and the crossover that justifies it; the duty cycle and the resulting service
interval; the timing plan with the oscillator and the resynchronisation interval; the
calibration and test access; and one paragraph stating what the build cannot deliver.
Every number must be computed, not asserted.

**★★★7.** Two designs are offered for the same requirement: (A) gain 100 with a
24-bit converter, and (B) gain 1000 with a 32-bit sigma-delta converter. Using the
lesson's cost-effectiveness table, compute the noise floor of each and the noise floor
per unit of relative cost, state which is better on that metric, and then state two
reasons to prefer (A) anyway.
