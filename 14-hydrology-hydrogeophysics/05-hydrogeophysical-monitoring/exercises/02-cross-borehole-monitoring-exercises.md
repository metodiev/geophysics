# Exercises — 14-05-02 Cross-Borehole Monitoring and Tracer Tests

Attempt these before reading the
[solutions](./02-cross-borehole-monitoring-solutions.md). The lesson is
[02 Cross-Borehole Monitoring](../02-cross-borehole-monitoring.md). All models
are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** The SYNTHETIC aquifer has $K = 5.0\ \mathrm{m\,d^{-1}}$,
$i = 0.10$ and $n_e = 0.25$. Compute the Darcy flux and the seepage velocity,
with units.

**★2.** Using $M = 2.0$ kg/m, $D_L = 1.0$ and $D_T = 0.1\ \mathrm{m^2\,d^{-1}}$,
$v = 2.0\ \mathrm{m\,d^{-1}}$ and $x = 5.0$ m, compute the centreline
concentration at $t = 2.50$ d and at $t = 1.00$ d, and say which is closer to the
peak.

**★3.** Define the "first arrival" at 1% of the peak for the demonstration's
curve and state, in one sentence, why the number is not a property of the
aquifer alone.

## ★★ Applied

**★★4.** Compute the arrival time and the implied velocity for the thresholds
0.1%, 1%, 5% and 50% of the peak (the demonstration gives 0.490, 0.610, 0.750 and
1.240 d). State the ratio between the largest and the smallest, and design a
reporting convention that removes the ambiguity.

**★★5.** A cross-hole survey has 5 electrode levels per borehole in two
boreholes over a $40\times20$ grid. Compute the number of rays, the rank and the
null-space dimension, and state what happens to each if a third borehole with 5
levels is added in the same plane (consider only the pairs that involve the new
borehole).

**★★6.** Using the demonstration's linear mixing model,
$\sigma_w = 0.050 + 0.2156\,c$ with $c$ in kg/m³, and $\phi = 0.25$, $m = 1.8$,
compute the bulk conductivity for $c = 0.01$ kg/m³ and decide whether the change
is detectable against an absolute noise of 0.010 dex on $\log_{10}\rho_a$.

## ★★★ Research-oriented

**★★★7.** The lesson shows that a smoothness penalised inversion of the same 36
ray averages recovers a smooth plume with correlation 0.71 and a blocky box with
correlation 0.42. Design an acquisition or processing change that would let you
distinguish the two *from the data*, and state the cost. Quantify what your
change does to the rank of the data kernel.

**★★★8.** You are asked to monitor a plume that may migrate laterally out of the
plane between two boreholes. Propose an experimental design (geometry,
measurement types, survey interval) that can detect the departure rather than
smearing it, and state explicitly which assumptions of the straight-ray
tomography your design violates and why that is acceptable.
