# Exercises — 23-05-06 IoT and Autonomous Sensor Networks for Earth Monitoring

Attempt these before reading the
[solutions](./06-iot-sensor-networks-solutions.md). The lesson is
[06 IoT and Autonomous Sensor Networks](../06-iot-sensor-networks.md). All values are
**SYNTHETIC**.

## ★ Foundational

**★1.** A node samples one component at 50 Hz with two bytes per sample. Compute its
byte rate, its bit rate and its daily volume, then the volume of 12 nodes over 90 days.

**★2.** That node's data must cross a 25 kbit/s link. Compute the airtime per day and
compare it with a 1 % duty-cycle limit: give the shortfall factor and the volume the
limit does allow.

## ★★ Applied

**★★3.** An event lasts 1 s and the node records a 4 s window per wake. Compute the
detection probability at wake intervals of 600, 120 and 30 s, and the wake interval
required for a probability of 0.80, with the acquisition duty cycle it implies.

**★★4.** A radio link has 10 dBm transmit power, 0 dBi at each end and a receiver
sensitivity of −110 dBm. Compute the allowable path loss, the free-space range at
868 MHz, and the range under an empirical model with a path-loss exponent of 3.5 and
60 dB at 10 m — first with no margin, then with a 20 dB fade margin.

## ★★★ Research-oriented

**★★★5.** A 20-node array has a per-node survival probability of 0.90 and requires at
least 16 nodes operating. Compute the availability with independent failures, then
recompute it for a design in which, with probability 0.05, a shared firmware fault
removes four nodes at once (the remaining nodes then survive independently). State what
the difference means for a campaign, and what the same common-cause event would do if
the requirement were 18 nodes instead of 16.

**★★★6.** Design the data and telemetry plan for a 40-node, 4-month campaign sampling
three components at 100 Hz, with one visit per node and a 1 % duty-cycle radio limit.
Produce: the raw and compressed volumes; the airtime needed and the shortfall; the four
options of the lesson with the one you choose and why; the detection probability you
will achieve and where it will be stated; the health telemetry each report will carry;
and one paragraph on what the plan cannot deliver.
