# Exercises — 07-02-05 Airborne and Marine Gravity: Platforms and Eotvos Corrections

Attempt these before reading the
[solutions](./05-airborne-marine-gravity-solutions.md). The lesson is
[05 Airborne and Marine Gravity: Platforms and Eotvos Corrections](../05-airborne-marine-gravity.md).
All models are **SYNTHETIC**. Use
$\omega = 7.292115\times10^{-5}\ \mathrm{rad\,s^{-1}}$,
$1\ \mathrm{knot} = 0.514444\ \mathrm{m\,s^{-1}}$,
$1\ \mathrm{mGal} = 10^{-5}\ \mathrm{m\,s^{-2}}$ and the measured lesson values
where they apply.

## ★ Foundational

**★1.** Derive the Eötvös coefficient for speeds in knots from $\omega$ and the
definition of the knot, and state how many mGal per knot the correction is at the
equator on a due-east heading.

**★2.** A SYNTHETIC ship sails at $8\ \mathrm{m\,s^{-1}}$ at latitude $60^\circ$ on
a heading of $135^\circ$. Compute the Eötvös correction. Then compute it for the
reciprocal heading of $315^\circ$ at the same speed and latitude.

**★3.** Compute $V^{2}/R$ in mGal for a ship turning at $6\ \mathrm{m\,s^{-1}}$ with
a 3 km radius, and state why a marine survey normally avoids using data from turns.

## ★★ Applied

**★★4.** A SYNTHETIC aircraft platform derives the low-frequency part of its
vertical acceleration from GNSS positions with $\sigma_{z} = 0.02\ \mathrm{m}$ and a
hand-off at $0.004\ \mathrm{Hz}$. Compute the resulting gravity-band noise in mGal,
and compute what $\sigma_{z}$ would be needed for a $1\ \mathrm{mGal}$ contribution.

**★★5.** For an aircraft at $70\ \mathrm{m\,s^{-1}}$ and $45^\circ$ latitude
($A = 721.88\ \mathrm{mGal}$ at the cardinal east-west heading), compute the heading
sensitivity in mGal per degree at headings of $30^\circ$ and $60^\circ$, and the
error contributed by a $0.05^\circ$ heading uncertainty at each.

**★★6.** A SYNTHETIC marine grid has 8 east-west and 6 north-south lines. Compute
the number of cross-overs and the number of degrees of freedom of a line-bias
adjustment that determines one bias per line with one gauge constraint. Then state
why the residual after adjustment cannot be smaller than the cross-over noise.

## ★★★ Research-oriented

**★★★7.** Design a flight plan for a SYNTHETIC airborne survey targeting
$2\ \mathrm{mGal}$: line direction, line spacing, altitude, airspeed, turn policy and
tie-line crossing. Show the budget, state the navigation accuracy required, and say
which single design change would most improve the result.

**★★★8.** Specify how you would determine the band hand-off frequency between GNSS
and an accelerometer for a moving-platform survey, given measured noise levels for
both sensors and a stated target. Include the criterion, the test that would reveal
a wrong hand-off, and the shape of the error spectrum you expect if the hand-off is
set too high or too low.

**★★★9.** A cross-over adjustment of a SYNTHETIC survey leaves a residual of
$1.5\ \mathrm{mGal}$ against a stated cross-over noise of $0.4\ \mathrm{mGal}$.
Enumerate the physical causes consistent with this, rank them by how they would
appear in the residual (spatially, in time, with heading), and specify the analysis
that would identify each.
