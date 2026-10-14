# Exercises — 17-04-04 Satellite Laser Ranging, DORIS and VLBI

Attempt these before reading the
[solutions](./04-satellite-laser-ranging-solutions.md). The lesson is
[04 Satellite Laser Ranging, DORIS and VLBI](../04-satellite-laser-ranging.md).
All models are **SYNTHETIC** teaching values.

Constants: $c = 299\,792\,458\ \mathrm{m\,s^{-1}}$,
$\Omega = 7.292\,115\times10^{-5}\ \mathrm{rad\,s^{-1}}$,
$1\ \mathrm{mas} = 4.8481\times10^{-9}\ \mathrm{rad}$.

## ★ Foundational

**★1.** Convert 250 ps of round-trip timing precision into millimetres of range,
and state what else must be removed from a laser range besides the time-of-flight.

**★2.** A beacon transmits at $f_0 = 2\ \mathrm{GHz}$ and the satellite's range
rate is $\dot\rho = +5\ \mathrm{km\,s^{-1}}$. Compute the Doppler shift, with sign,
and say whether the satellite is approaching or receding.

**★3.** Compute the maximum geometric delay for a $3000\ \mathrm{km}$ baseline and
the angular precision implied by $5\ \mathrm{ps}$ of delay noise.

## ★★ Applied

**★★4.** A laser station has 2000 normal points over 8 years with $5\ \mathrm{mm}$
of noise and a $7\ \mathrm{mm}$ annual signal. **(a)** Estimate the formal velocity
scatter from the straight-line formula. **(b)** State two systematic errors that
would dominate over it and why averaging cannot remove them.

**★★5.** The lesson measures a correlation of $-1.000000$ between a constant range
bias and a global scale for 40 stations spanning $2.9\ \mathrm{km}$ of radius.
**(a)** Explain in one sentence why the degeneracy is so complete. **(b)** Compute
the fractional radius spread, and state how much larger the spread would have to
be to reduce the correlation to $-0.99$.

**★★6.** For a $6000\ \mathrm{km}$ baseline, compute the delay change produced by a
$0.05\ \mathrm{ms}$ UT1 error, and compare it with a $5\ \mathrm{ps}$ delay
precision. State what the comparison implies about which quantity is measured.

## ★★★ Research-oriented

**★★★7.** Design the tie between a VLBI antenna, a laser ranging station and a GNSS
receiver on the same site, for a frame at the $1\ \mathrm{mm}$ level. Specify the
local survey you would perform, the reference points you would use, the systematic
effects you must model, and how you would validate the tie. Justify each number
from the lesson. A specification that could not be executed is a failed answer.

**★★★8.** DORIS is processed in two modes: with the station coordinates assumed
known (for orbit determination) and with them estimated (for geodetic
positioning). **(a)** Explain why the same observations support both, in terms of
which parameters the least-squares problem solves for. **(b)** State the
observational consequence of using the first mode's coordinates as if they were
the second's. **(c)** Explain how this example illustrates the general rule about
parameters that mimic the signature of the error under study.
