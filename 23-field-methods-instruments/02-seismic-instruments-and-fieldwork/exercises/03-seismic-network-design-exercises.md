# Exercises — 23-02-03 Seismic Network Design and Station Siting

Attempt these before reading the
[solutions](./03-seismic-network-design-solutions.md). The lesson is
[03 Seismic Network Design](../03-seismic-network-design.md). All values are
**SYNTHETIC**.

## ★ Foundational

**★1.** Six stations each detect an event with probability $p = 0.5$, and three
coincident detections are required to declare it. Compute $P_{\text{net}}$
exactly, and state how the answer would change if the threshold were raised to
four detections.

**★2.** Six stations have azimuths 10°, 25°, 40°, 200°, 215° and 230° as seen
from the target area. Compute the azimuthal gap. State whether you would accept
this geometry for accurate epicentre location, and name the cheapest change that
would improve it.

## ★★ Applied

**★★3.** A full ring of 16 stations has $V = 6.0\ \mathrm{km/s}$ and
$\sigma_t = 0.05\ \mathrm{s}$. Compute $\sigma_h$ from the closed form. Then
compute the number of stations required for $\sigma_h = 0.10\ \mathrm{km}$, and
state the assumption that makes this scaling exact.

**★★4.** A ring array of radius 1 km is used at $f = 2\ \mathrm{Hz}$. Compute the
slowness resolution from the first zero of the Bessel response, and convert it to
an apparent-velocity resolution at $V = 3.0\ \mathrm{km/s}$. Give the units.

## ★★★ Research-oriented

**★★★5.** Design a temporary network for detecting $M \ge 1.5$ with at least 90 %
probability, using the lesson's logistic per-station detection curve
($M_{50} = 1.2$, $s = 0.25$) and a coincidence threshold of four detections.
Compute the minimum number of stations, then state how you would site them, the
resulting azimuthal gap, the expected $\sigma_h$ for $V = 6\ \mathrm{km/s}$ and
$\sigma_t = 0.05\ \mathrm{s}$, and the one requirement that would force you to add
stations. Show the arithmetic.

**★★★6.** Specify a study that measures the *achieved* magnitude of completeness
of a deployed network from a catalogue: state the data, the estimator, the metric
and its uncertainty, and at least two ways the estimate is biased specifically
because the catalogue was produced by the same network being assessed. A
specification that could not be executed is a failed answer.
