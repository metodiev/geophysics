# Exercises — 08-02-04 Gradiometers, Arrays and Noise Rejection

Attempt these before reading the
[solutions](./04-gradiometers-arrays-solutions.md). The lesson is
[04 Gradiometers, Arrays and Noise Rejection](../04-gradiometers-arrays.md).
All source parameters and noise floors are **SYNTHETIC** teaching values.

Use $\mu_0 = 4\pi\times10^{-7}\ \mathrm{H\,m^{-1}}$.

## ★ Foundational

**★1.** For two sensors with equal noise and correlation $\rho$, compute
$\sigma_{\text{diff}}/\sigma$ and the rejection factor $\sigma/\sigma_{\text{diff}}$
for $\rho = 0.95$, $\rho = 0.99$ and $\rho = 0.9999$.

**★2.** A synthetic dipole with moment $m = 25\ \mathrm{A\,m^2}$ lies $8.0\
\mathrm{m}$ below a sensor, on the axis. Compute $|B|$ and
$|\partial B/\partial z|$.

**★3.** State which of the two gradient-tensor properties — symmetry and zero
trace — follows from $\nabla\cdot\mathbf{B} = 0$ and which from
$\nabla\times\mathbf{B} = 0$, and say how many independent components remain.

## ★★ Applied

**★★4.** For the dipole of ★2, and noise floors of $0.05\ \mathrm{nT}$ (total
field) and $0.005\ \mathrm{nT\,m^{-1}}$ (gradient over a 1 m baseline), compute
the signal-to-noise ratio of each measurement and decide which instrument detects
the target at the 3$\sigma$ level.

**★★5.** Compute the gradiometer response $2\sin(\pi L/\lambda)$ at
$L/\lambda = 0.02$ and $0.2$, express each as a percentage of the fully resolved
response, and find the $L/\lambda$ at which the response is exactly half of the
full value.

**★★6.** Sensor A has a sensitivity 1% higher than sensor B. If the common field
is $50000\ \mathrm{nT}$, what apparent difference does the mismatch create, and
how does it compare with a $1\ \mathrm{nT}$ target anomaly? State the calibration
tolerance needed for a $0.1\ \mathrm{nT}$ target.

## ★★★ Research-oriented

**★★★7.** Design a gradiometer survey for a target expected at $3\ \mathrm{m}$
depth with an anomaly of a few nanotesla. State the baseline, the sensor-matching
tolerance, the orientation tolerance, the expected noise floor, and one
instrument-level test that would reveal a baseline error. A specification that
could not be executed is a failed answer.

**★★★8.** Derive the depth estimate that a field/gradient ratio gives for (a) a
point dipole and (b) a two-dimensional line of dipoles (a horizontal cylinder
striking across the profile, for which the field falls as $r^{-2}$). State the
assumption each formula makes and how an error in that assumption propagates into
the depth.
