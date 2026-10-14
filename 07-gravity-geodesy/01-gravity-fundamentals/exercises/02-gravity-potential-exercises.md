# Exercises — 07-01-02 Gravitational Potential, Equipotentials and the Geoid

Attempt these before reading the
[solutions](./02-gravity-potential-solutions.md). The lesson is
[02 Gravitational Potential, Equipotentials and the Geoid](../02-gravity-potential.md).
All models are **SYNTHETIC** teaching values. Use
$G = 6.67430\times10^{-11}\ \mathrm{m^{3}\,kg^{-1}\,s^{-2}}$,
$1\ \mathrm{mGal} = 10^{-5}\ \mathrm{m\,s^{-2}}$ and, where needed,
$\gamma = 9.820250\ \mathrm{m\,s^{-2}}$ from the spherical model.

## ★ Foundational

**★1.** A SYNTHETIC point mass $M = 3.00\times10^{11}\ \mathrm{kg}$ sits at the
origin. Compute $U$ at $r = 1000\ \mathrm{m}$ and $r = 3000\ \mathrm{m}$, and the
field magnitude at both radii. State the units of each number.

**★2.** For $U = -GM/r$, compute the three second derivatives
$\partial^{2}U/\partial x^{2}$, $\partial^{2}U/\partial y^{2}$,
$\partial^{2}U/\partial z^{2}$ for a point mass at the origin, and show by
algebra that their sum is zero everywhere except at $r = 0$. State which equation
this proves.

**★3.** In scale-free units ($G = M = R = 1$) for a uniform sphere, evaluate $U$
and $g$ at $r = 0.5$ from the interior formulae, and verify
$\nabla^{2}U = 4\pi G\rho$ at that point by direct calculation. Also state $U$ at
the centre and its ratio to the surface value.

## ★★ Applied

**★★4.** A SYNTHETIC mass excess $M = 8.00\times10^{11}\ \mathrm{kg}$ lies
$2000\ \mathrm{m}$ below a station with $\gamma = 9.820250\
\mathrm{m\,s^{-2}}$. Compute (a) the anomalous potential, (b) the gravity anomaly
in mGal, (c) the geoid undulation in mm, and (d) verify the identity
$N/\Delta g = z/\gamma$.

**★★5.** A SYNTHETIC planet rotates five times faster than the Earth
($\omega = 3.6461\times10^{-4}\ \mathrm{rad\,s^{-1}}$) but has the same
$a = 6\,378\,137\ \mathrm{m}$, $b = 6\,356\,752.314\ \mathrm{m}$ and
$GM = 3.986004418\times10^{14}\ \mathrm{m^{3}\,s^{-2}}$. (a) Compute $m$. (b)
Using the uniform-fluid (Maclaurin) result $f = \tfrac54 m$, compute $f$ and then
$J_2 = \tfrac23 f - \tfrac13 m$. (c) State plainly whether the first-order
relations used here are trustworthy at this rotation rate, and why.

**★★6.** For the $500\ \mathrm{m}$ sphere of the lesson
($M = 1.398009\times10^{12}\ \mathrm{kg}$, density $2670\ \mathrm{kg\,m^{-3}}$),
compute the peak gravity anomaly and the geoid undulation at centre depths
$800\ \mathrm{m}$ and $1600\ \mathrm{m}$. By what factor does each quantity
change, and what does the difference of the two factors tell you about the depth
sensitivity of the geoid compared with the anomaly?

## ★★★ Research-oriented

**★★★7.** Design a numerical experiment that measures how the level-surface
residual of Section 5.4 falls as harmonics $J_2, J_2+J_4, J_2+J_4+J_6,\dots$ are
included. Specify the potential, the sampling of the ellipsoid, the residual
metric, the expected scaling, and one check that would show the result is limited
by arithmetic rather than by physics.

**★★★8.** Show, with an explicit family and a numerical demonstration, that
different radial mass distributions produce identical exterior potentials. Then
state precisely what *is* determined by the exterior potential of an isolated
body, and give one geophysical consequence.

**★★★9.** A national vertical datum is to be modernised so that heights refer to a
geoid determined from satellite and terrestrial data. Identify the conventions
that must be fixed (at least three), state what stays arbitrary, and explain how
you would detect that a published model uses a different reference potential from
the one you assumed.
