# Exercises — 17-03-07 Radar Altimetry and Sea/Ice Surface Height

Attempt these before reading the
[solutions](./07-radar-altimetry-solutions.md). The lesson is
[07 Radar Altimetry](../07-radar-altimetry.md). All models are **SYNTHETIC**
teaching values.

Constants: $c = 299\,792\,458\ \mathrm{m\,s^{-1}}$,
$g = 9.80665\ \mathrm{m\,s^{-2}}$,
$\Omega = 7.292\,115\times10^{-5}\ \mathrm{rad\,s^{-1}}$,
M2 period $12.4206012\ \mathrm{h}$, $SWH = 4\sigma_z$.

## ★ Foundational

**★1.** A return arrives $5.3347\ \mathrm{ms}$ after transmission. Compute the
range. If the platform altitude is $800\,000\ \mathrm{m}$, give the height of the
surface above the reference ellipsoid, and state the two corrections you have
ignored.

**★2.** Compute the pulse-limited footprint radius and area for
$\tau = 2\ \mathrm{ns}$ at $h = 900\ \mathrm{km}$.

**★3.** A leading edge rises from 10% to 90% over $0.80\ \mathrm{m}$ of range.
Compute the SWH using the measured conversion factor, and state which regime the
$1\ \mathrm{ns}$ flat-pulse correction belongs to.

## ★★ Applied

**★★4.** **(a)** Compute the geostrophic speed for a $2\ \mathrm{cm}$ rise over
$50\ \mathrm{km}$ at $60^\circ$ N. **(b)** Repeat at $10^\circ$ N and comment on
what the result implies about altimetry near the equator.

**★★5.** **(a)** Compute the aliased period of the M2 tide for a 15-day repeat
cycle. **(b)** If the goal is to resolve M2 rather than alias it, state the
property the repeat cycle must have and why.

**★★6.** A freeboard measurement of $F = 0.40\ \mathrm{m}$ has an uncertainty of
$\pm0.03\ \mathrm{m}$. Using the teaching densities, give the thickness and its
uncertainty from the freeboard alone, and then the additional uncertainty from a
$\pm0.002\ \mathrm{g\,cm^{-3}}$ uncertainty in $\rho_i$. Which term dominates?

## ★★★ Research-oriented

**★★★7.** Design the error budget for a study that must detect a
$5\ \mathrm{cm\,s^{-1}}$ surface current at $45^\circ$ N with a
$1\ \mathrm{cm}$ height difference over $20\ \mathrm{km}$. State the required
height precision, the spatial averaging you would use and its resolution cost,
the corrections you would apply, and the correction you expect to dominate.
Justify each number from the lesson. A specification that could not be executed
is a failed answer.

**★★★8.** The demonstration measures the leading-edge ratio as 0.6550 at
$SWH = 1\ \mathrm{m}$ and 0.6406 at $SWH = 8\ \mathrm{m}$, against the ideal
0.6407. **(a)** Explain, in terms of the pulse-limited contribution, why the ratio
is larger at small wave heights. **(b)** Derive the value the ratio would take in
the limit $SWH \to 0$ for a $1\ \mathrm{ns}$ pulse, and check it against the
measured $0.6550$. **(c)** State what this implies for a wave-height retrieval
from a very calm sea.
