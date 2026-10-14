# Exercises — 15-02-05 Marine Gravity and Magnetic Surveys

Attempt these before reading the
[solutions](./05-marine-gravity-magnetics-solutions.md). The lesson is
[05 Marine Gravity and Magnetics](../05-marine-gravity-magnetics.md). All models
are **SYNTHETIC** teaching values.

Constants: $\Omega = 7.292115\times10^{-5}\ \mathrm{s^{-1}}$,
$R = 6.371\times10^{6}\ \mathrm{m}$, $g = 9.80665\ \mathrm{m\,s^{-2}}$,
$G = 6.674\times10^{-11}\ \mathrm{m^{3}\,kg^{-1}\,s^{-2}}$,
$\mu_0 = 4\pi\times10^{-7}\ \mathrm{H\,m^{-1}}$,
$1\ \mathrm{kn} = 0.514444\ \mathrm{m\,s^{-1}}$,
$1\ \mathrm{mGal} = 10^{-5}\ \mathrm{m\,s^{-2}}$.

## ★ Foundational

**★1.** Derive the two Eötvös coefficients in mGal per knot and per
$\mathrm{knot^{2}}$, starting from $2\Omega\cos\phi\,u$ and $V^{2}/R$.

**★2.** Compute the Eötvös correction for a 12 kn eastward line at $35^\circ$N,
both terms separately, and state the sign of each.

**★3.** Compute the free-air gradient $-2g/R$ in mGal per metre and state its sign
for a station *below* the reference surface.

## ★★ Applied

**★★4.** Compute the free-air and Bouguer corrections for a seabed station at
$2500\ \mathrm{m}$ depth with a density contrast of $1800 - 1030\
\mathrm{kg\,m^{-3}}$. State which correction needs a density and which needs only
a depth.

**★★5.** Compute the dipole field magnitude and the inclination at magnetic
latitudes $20^\circ$ and $70^\circ$ using $m = 8.0\times10^{22}\
\mathrm{A\,m^{2}}$. Verify the polar-to-equatorial ratio of 2.

**★★6.** A survey at $40^\circ$N steams at 9 kn. Compute the Eötvös errors
produced by (a) a $2^\circ$ heading error on a line at $30^\circ$ from north, and
(b) a speed error of 0.2 kn on the same line. State which dominates.

**★★7.** A symmetric magnetic anomaly from a vertical dipole has zero crossings
4.5 km apart. (a) Compute the dipole's depth. (b) State the anomaly's peak value if
the moment is $3.0\times10^{10}\ \mathrm{A\,m^{2}}$ and the depth from (a).

## ★★★ Research-oriented

**★★★8.** Design a marine gravity survey whose *total* Eötvös error is below
0.5 mGal at 10 kn, stating the heading and speed tolerances you need, the survey
geometry you would use, and the residual term you cannot remove by geometry alone.
A specification that could not be executed is a failed answer.

**★★★9.** The lesson notes that reduction to the pole requires the magnetisation
direction as an input, and that remanence is common. Design a test that would
detect a wrong assumed magnetisation direction in a reduced-to-pole grid, and state
the observable that a wrong direction distorts. Derive the mathematical form of the
distortion.
