# Exercises — 23-07-01 Case Study: Deploying a Temporary Seismic Array

Attempt these before reading the
[solutions](./01-case-study-seismic-array-solutions.md). The lesson is
[01 Case Study: A Temporary Seismic Array](../01-case-study-seismic-array.md). All values are
**SYNTHETIC**.

## ★ Foundational

**★1.** A target is 2 km lateral extent at 15 km depth, with a dominant wavelength of 3 km.
Compute the required aperture. Then compute the maximum station spacing from the aliasing
limit and state the number of stations needed for a spacing at **half** the aliasing limit —
and the number if the spacing equals the limit.

**★2.** A campaign has 30 stations, 4.0 h of work per station and a four-person crew. Compute
the station-hours, the person-days, and the days to install with one and with two crews.

## ★★ Applied

**★★3.** Compute the raw and 3:1-compressed data volume for 30 stations recording 200 Hz, three
components, four bytes per sample, for 45 days. Then compute how many campaigns one 8 TB disk
holds, and state which resource the arithmetic shows to be the constraint.

**★★4.** A station sleeps at 60 µA, acquires at 40 mA and transmits at 200 mA for 30 s per
day. Compute the average current and the battery life on a 30 Ah battery of which 60 % is
usable, at acquisition duties of 1/4 and 1/24; then state how many visits a 45-day deployment
needs for each.

**★★5.** With per-station survival 0.85, 30 stations at 900 m spacing and a target whose
$\lambda z = 45\ \mathrm{km^{2}}$ (for example $\lambda = 3$ km at $z = 15$ km), compute the
nominal aperture and resolution cell, the expected number of stations alive, the expected
aperture and resolution, and the resolution loss caused by exactly two failures.

## ★★★ Research-oriented

**★★★6.** You must design a 45-day, 30-station array for a 2 km target at 15 km depth with
$\lambda = 3$ km, a land-access budget of 10 sites per week, a 30 Ah battery per station, one
vehicle per crew and a requirement that the array still meets its resolution in 80 % of
deployments.

Produce the plan: the geometry with the margin you choose and its justification; the
installation schedule and the crew trade; the acquisition duty cycle and the visit plan with
the arithmetic for both; the data volume and the download bench; the availability calculation
showing the 80 % requirement is met; the QC that runs *during* the campaign; and the three
risks with the mitigation for each.
