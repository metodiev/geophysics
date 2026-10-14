# Exercises — 23-05-02 Amplification, Filtering and Analog-Digital Conversion

Attempt these before reading the
[solutions](./02-signal-conditioning-solutions.md). The lesson is
[02 Signal Conditioning](../02-signal-conditioning.md). All values are
**SYNTHETIC**.

## ★ Foundational

**★1.** An amplifier has $e_n = 5\ \mathrm{nV/\sqrt{Hz}}$ and
$i_n = 0.5\ \mathrm{pA/\sqrt{Hz}}$. Compute the source resistance at which its noise
figure is minimised, and state the relation used.

**★2.** Compute the input-referred noise at that resistance at $T = 300$ K, giving
the source, current and voltage contributions separately.

## ★★ Applied

**★★3.** Two stages have $F_1 = 2$, $G_1 = 50$ and $F_2 = 10$. Compute
$F_{\text{total}}$ in linear units and in dB. Then compute it with the stages
reversed, and state the lesson.

**★★4.** A converter has a measured SINAD of 84 dB. Compute its effective number of
bits, and the oversampling ratio required to gain a further two bits.

## ★★★ Research-oriented

**★★★5.** Design a front end for a 1 kΩ source whose signal band ends at 40 Hz,
with a 24-bit converter, an 80 dB attenuation requirement at $f/f_c = 3$ and a
target of 18 effective bits: state the amplifier's noise requirements, the gain and
its staging, the filter order and type, the sample rate and the oversampling ratio,
and the checks you would make on the assembled circuit. Show the arithmetic and
state one assumption the design cannot verify analytically.

**★★★6.** Specify a measurement of the effective number of bits of an assembled
front end (including the amplifier): state the stimulus, the analysis, the metric
with units, the number of samples, and two effects that a converter-only ENOB test
would miss. A specification that could not be executed in a laboratory is a failed
answer.
