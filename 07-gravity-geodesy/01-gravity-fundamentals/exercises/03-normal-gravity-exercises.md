# Exercises — 07-01-03 Reference Ellipsoid, Normal Gravity and Clairaut's Theorem

Attempt these before reading the
[solutions](./03-normal-gravity-solutions.md). The lesson is
[03 Reference Ellipsoid, Normal Gravity and Clairaut's Theorem](../03-normal-gravity.md).
All models are **SYNTHETIC** teaching values. The reference values of the lesson
are $a = 6\,378\,137\ \mathrm{m}$, $f = 1/298.257223563$,
$GM = 3.986004418\times10^{14}\ \mathrm{m^{3}\,s^{-2}}$,
$\omega = 7.292115\times10^{-5}\ \mathrm{rad\,s^{-1}}$; use
$1\ \mathrm{mGal} = 10^{-5}\ \mathrm{m\,s^{-2}}$ and
$1^\circ$ of latitude $\approx 111.32\ \mathrm{km}$ of arc.

## ★ Foundational

**★1.** A SYNTHETIC planet has
$a = 6\,400\,000\ \mathrm{m}$, $f = 1/300$,
$GM = 3.986004418\times10^{14}\ \mathrm{m^{3}\,s^{-2}}$ and
$\omega = 7.292115\times10^{-5}\ \mathrm{rad\,s^{-1}}$. Compute $b$, $e^{2}$,
$e'^{2}$ and $m$.

**★2.** For the planet of ★1, compute $J_2$ from the first-order relation and
then the first-order $\gamma_{e}$ and $\gamma_{p}$ in mGal.

**★3.** For the planet of ★1, verify Clairaut's relation $\beta + f = \tfrac52 m$
using the $\gamma_{e}$, $\gamma_{p}$ of ★2, and report the relative residual.

## ★★ Applied

**★★4.** For the planet of ★1, evaluate Somigliana's formula at
$0^\circ$, $30^\circ$, $45^\circ$, $60^\circ$, $90^\circ$ and state the full
latitude range of normal gravity in mGal. If a station at $30^\circ$ reads
$972\,610.00\ \mathrm{mGal}$, compute the anomaly, and compute the anomaly the
same reading would give at $45^\circ$.

**★★5.** A SYNTHETIC survey line at $45^\circ$ latitude runs $25\ \mathrm{km}$ due
north while climbing $250\ \mathrm{m}$. Using the measured coefficients
$0.8131\ \mathrm{mGal\,km^{-1}}$ (latitude) and
$-0.3086\ \mathrm{mGal\,m^{-1}}$ (free air), compute the two corrections and their
ratio. Which one dominates?

**★★6.** Using the reference values of the lesson, take the exact Somigliana
values at $0^\circ, 10^\circ, \dots, 90^\circ$, fit
$\gamma/\gamma_{e} - 1 = \beta\sin^{2}\varphi + \beta_1\sin^{4}\varphi$ by least
squares, and report $\beta$, $\beta_1$ and the maximum residual. Compare $\beta$
with $(\gamma_{p}-\gamma_{e})/\gamma_{e}$ and explain the difference.

## ★★★ Research-oriented

**★★★7.** Design an experiment that tests whether a SYNTHETIC planet is in
hydrostatic equilibrium. Specify which quantities you would determine, from which
kind of data, how you would compare them with the hydrostatic relation, and what
result would let you conclude "non-hydrostatic". Include at least one control
that would show your method recovers hydrostatic equilibrium when it is true.

**★★★8.** The normal field depends on four parameters. Set up the least-squares
problem of estimating corrections
$(\delta a, \delta f, \delta GM, \delta\omega)$ from $N$ gravity observations at
different latitudes on the ellipsoid. State the design matrix, discuss which
parameters are separable and which are not, and identify the direction in
parameter space that the data cannot constrain. Give a numerical example of a
parameter combination with a very small effect.

**★★★9.** Propagate a relative uncertainty of $1\times10^{-8}$ in $a$,
$1\times10^{-5}$ in $f$ and $1\times10^{-9}$ in $GM$ through Somigliana's formula
at $45^\circ$ by finite differences. Report which of the three dominates the
uncertainty in $\gamma$ in mGal, and explain why that ordering is not obvious.
