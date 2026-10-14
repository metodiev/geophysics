# Exercises — 06-13-01 Planetary Seismology: InSight and Lunar Seismic Experiments

Attempt these before reading the
[solutions](./01-planetary-seismology-solutions.md). The lesson is
[01 Planetary Seismology](../01-planetary-seismology.md). All models are
**SYNTHETIC** straight-ray half-space values.

## ★ Foundational

**★1.** A source at $\Delta = 30.0\ \mathrm{km}$, $h = 20.0\ \mathrm{km}$ is
recorded with $V_p = 6.00\ \mathrm{km\,s^{-1}}$,
$V_s = 3.46\ \mathrm{km\,s^{-1}}$. Compute the slant range $R$, $t_P$, $t_S$ and
the S−P time, with units.

**★2.** For ★1, compute the incidence angle $i$ from $\tan i = \Delta/h$ and state
whether the station is in the geometry where polarisation is most informative.

**★3.** A pick uncertainty of $\sigma_t = 0.03\ \mathrm{s}$ is quoted for the S−P
time of ★1. Compute $\sigma_R$ and express it as a percentage of $R$. State
which quantity sets the conversion.

## ★★ Applied

**★★4.** Keep the S−P time of ★1 fixed and tabulate the $({\Delta}, h)$ pairs
that reproduce it exactly for $\Delta = 5, 15, 30, 50, 120\ \mathrm{km}$ (allow
$h = 0$ where the required depth would be negative). State in one sentence what
the table proves about single-station depth determination.

**★★5.** The velocity model of ★1 is wrong: $V_p/V_s$ is $4\%$ too large, with
$V_p$ held fixed. Recompute $R$ from the measured S−P time and report the
distance error in km and in per cent. Compare it with the pick error of ★3 and
state which dominates.

**★★6.** An analyst measures an incidence angle of $63.43^{\circ}$ at
$\Delta/h = 2$. Using $\mathrm{d}\ln\Delta/\mathrm{d}i = 2/\sin 2i$, compute the
fractional distance error for a $2^{\circ}$ polarisation error, with units.

## ★★★ Research-oriented

**★★★7.** A mission can carry either (i) one broadband three-component station,
(ii) two stations, or (iii) one station plus a short refraction profile that
measures $V_p$ to $1\%$ and $V_p/V_s$ to $2\%$. Using the numbers of the lesson,
quantify which option locates events best, state the assumption each option
relies on, and give the diagnostic you would use to test that assumption with the
data actually acquired.

**★★★8.** The lesson's §4 family has one free parameter when the velocity model
is unknown. Extend the counting argument to the case where the station also
records a second phase (e.g. a $P$-to-$S$ converted arrival or a surface
reflection) whose moveout is a function of depth only. State how many
observations and unknowns there are, whether the degeneracy is broken, and what
new assumption the extra phase introduces. Justify each count.
