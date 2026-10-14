# Exercises — 15-02-03 Side-Scan Sonar and Seafloor Imaging

Attempt these before reading the
[solutions](./03-side-scan-sonar-solutions.md). The lesson is
[03 Side-Scan Sonar](../03-side-scan-sonar.md). All parameters are **SYNTHETIC**
teaching values.

Constants: $c = 1500\ \mathrm{m\,s^{-1}}$,
$1^\circ = 0.0174533\ \mathrm{rad}$.

## ★ Foundational

**★1.** For a tow altitude $h = 12\ \mathrm{m}$, compute the ground range, the
grazing angle and the geometric stretch $\mathrm{d}x/\mathrm{d}r$ at slant ranges
$14\ \mathrm{m}$, $25\ \mathrm{m}$ and $90\ \mathrm{m}$. State which end of the
record is geometrically worst and why.

**★2.** Compute the blind-zone ground range for $h = 12\ \mathrm{m}$ and a first
return at $14\ \mathrm{m}$.

**★3.** Convert a backscatter intensity ratio of 0.02 into decibels, and a
pressure amplitude ratio of 0.02 into decibels. State which one the target
strength TS uses.

## ★★ Applied

**★★4.** Derive $\ell_{\text{across}} = c\tau/(2\sin g)$ from the projection of
the pulse onto an inclined seafloor, and evaluate it at $g = 60^\circ$,
$20^\circ$ and $5^\circ$ for $\tau = 0.08\ \mathrm{ms}$. State the floor that no
geometry can beat.

**★★5.** Under the $\sin^{2}$ backscatter model, compute the target strength at
grazing angles $40^\circ$ and $8^\circ$, and give the difference in dB and as an
intensity ratio.

**★★6.** Using the demonstration's sonar-equation budget
($\mathrm{SL} = 220\ \mathrm{dB}$, $\alpha = 0.10\ \mathrm{dB\,m^{-1}}$,
$\mathrm{NL} = 50\ \mathrm{dB}$, $\mathrm{DI} = 20\ \mathrm{dB}$,
$\mathrm{DT} = 10\ \mathrm{dB}$, $h = 20\ \mathrm{m}$), compute EL at
$R = 220\ \mathrm{m}$ and at $R = 280\ \mathrm{m}$ and state between which ranges
the detection limit falls.

**★★7.** The tow is raised from $20\ \mathrm{m}$ to $50\ \mathrm{m}$ at a fixed
maximum slant range of $180\ \mathrm{m}$. Compute (a) the ground half-width before
and after, (b) the far-edge grazing angle before and after, (c) the across-track
resolution at the far edge before and after for $\tau = 0.1\ \mathrm{ms}$, and
(d) state what was gained and what was lost.

## ★★★ Research-oriented

**★★★8.** Design a survey and analysis to measure the angular backscatter
exponent $n$ of a seafloor patch under the model $I(g) = \sin^{n}g$. State how you
break the circularity between the angular correction and the angular response,
what geometry gives you the widest range of grazing angles, and the systematic
that would bias $n$ if you ignored it. A specification that could not be executed
is a failed answer.

**★★★9.** The demonstration measures a 1.59x range gain from halving the
absorption coefficient. Derive the asymptotic relation between a factor $k$ change
in $\alpha$ and the resulting range change at large $\alpha R$, and state the
range of $\alpha R$ over which the demonstration's measured exponent is valid.
