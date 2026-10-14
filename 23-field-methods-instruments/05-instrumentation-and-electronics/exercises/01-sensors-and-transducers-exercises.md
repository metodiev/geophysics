# Exercises — 23-05-01 Sensors and Transducers: Principles and Selection

Attempt these before reading the
[solutions](./01-sensors-and-transducers-solutions.md). The lesson is
[01 Sensors and Transducers](../01-sensors-and-transducers.md). All values are
**SYNTHETIC**.

## ★ Foundational

**★1.** A displacement sensor has a full scale of 2 mm and a resolution of 5 nm.
Compute its dynamic range in dB and its equivalent bits. Then state why a real
recording system needs more bits than the equivalent-bit count suggests.

**★2.** A 120 Ω strain gauge with $G_F = 2.1$ is strained by 50 µε and wired in a
quarter bridge excited at 2.5 V. Compute $\Delta R$ and the bridge output in µV.

## ★★ Applied

**★★3.** The same gauge and excitation as ★2 are wired in a full bridge (four active
gauges). State the output, and the ratio to the quarter-bridge answer, and explain
where the factor comes from.

**★★4.** A piezoelectric sensor has $C = 2$ nF and the amplifier input resistance is
500 MΩ. Compute the high-pass corner, the response at 0.05 Hz and at 1 Hz, and state
whether this sensor can measure a 0.01 Hz ground strain.

**★★5.** A 5 kΩ resistor at 290 K is used with a band of 100 Hz. Compute its Johnson
noise. Then compute the smallest strain that the 120 Ω, $G_F = 2.1$, 2.5 V
quarter-bridge channel of ★2 could resolve in the same band at 300 K, and state
whether the wire resistance or the gauge noise dominates.

## ★★★ Research-oriented

**★★★6.** A pressure sensor will be deployed for six months at 40 m depth with a
resolution requirement of 1 Pa. Specify the sensing principle, the band, the dynamic
range needed in dB and bits, the dominant environmental threat with the quantity that
governs it, the two-point calibration you would perform, and the check you would
repeat at each service visit. Justify the principle against two alternatives you
reject.
