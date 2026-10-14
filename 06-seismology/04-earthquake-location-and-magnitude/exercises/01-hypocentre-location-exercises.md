# Exercises — 06-04-01 Hypocentre Location: Arrival Times, Inversions and Error Ellipses

Attempt these before reading the
[solutions](./01-hypocentre-location-solutions.md). The lesson is
[01 Hypocentre Location](../01-hypocentre-location.md). All models are
**SYNTHETIC** teaching values.

## ★ Foundational

**★1.** A station lies 42 km west and 60 km north of a trial hypocentre at
7.5 km depth, and the medium has $v = 6000\ \mathrm{m\,s^{-1}}$. Compute the
source–station distance $d$, then $\partial T/\partial x$ and
$\partial T/\partial z$, and state the unit of each.

**★2.** State why $\partial T/\partial t_0 = 1$ exactly, and give its unit.

**★3.** A single station has one arrival time. Explain, in two sentences, why
this gives a Jacobian of rank 1 out of 4 parameters.

## ★★ Applied

**★★4.** The demonstration's wide array gives marginal standard deviations
$\sqrt{C_{xx}} = 269.1\ \mathrm{m}$, $\sqrt{C_{yy}} = 243.9\ \mathrm{m}$,
$\sqrt{C_{zz}} = 466.4\ \mathrm{m}$ and $\sqrt{C_{t_0t_0}} = 0.0399\ \mathrm{s}$.
Compute the 95 per cent marginal depth bound $1.96\sqrt{C_{zz}}$, and explain why
the longest 95 per cent semi-axis of the joint ellipsoid is $1488.2\ \mathrm{m}$,
larger than any marginal value.

**★★5.** A station sits 30 km from a source in a medium with
$v = 6000\ \mathrm{m\,s^{-1}}$. Holding the arrival time fixed at
$T = 5.050\ \mathrm{s}$, tabulate the origin time required for depths 2, 5, 10,
15 and 20 km. State the size of the depth error that a 0.05 s origin-time error
would cause.

**★★6.** Given $\cos(\partial T/\partial z, \partial T/\partial t_0) = 0.9998$ for
5 stations in a 4 km aperture, estimate the condition number penalty qualitatively
and explain why the matrix is nonetheless exactly rank-deficient.

## ★★★ Research-oriented

**★★★7.** Design a surface network of 8 stations that would keep
$\cos(\partial T/\partial z, \partial T/\partial t_0)$ below 0.5 for an event at
8 km depth, assuming a homogeneous half-space. State the geometry, predict the
cosine from the formula, and give one reason your design might fail in reality.

**★★★8.** The Gauss-Newton iteration converged to the exact hypocentre from
$(20, 0, 15)\ \mathrm{km}$ in four steps on exact data. Construct a starting
model and a station geometry for which the iteration instead converges to a
local minimum of the residual, and describe the observable symptom that would
reveal it.
