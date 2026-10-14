# Exercises — 17-01-04 Spatial, Spectral, Temporal and Radiometric Resolution

Attempt these before reading the
[solutions](./04-resolution-concepts-solutions.md). The lesson is
[04 Spatial, Spectral, Temporal and Radiometric Resolution](../04-resolution-concepts.md).
The instrument is a **SYNTHETIC** teaching geometry.

Default parameters: $H = 700\ \mathrm{km}$, $D = 0.30\ \mathrm{m}$,
IFOV $= 10\ \mathrm{\mu rad}$, pitch $= 12\ \mathrm{\mu rad}$,
$R_E = 6371\ \mathrm{km}$, $N = 14.3$ orbits/day,
$L_{\max} = 5.0\times10^{7}\ \mathrm{W\,m^{-2}\,sr^{-1}\,m^{-1}}$,
$\mathrm{NE}\Delta L = 2.0\times10^{4}\ \mathrm{W\,m^{-2}\,sr^{-1}\,m^{-1}}$,
$b = 12$ bits.

## ★ Foundational

**★1.** Compute the GSD for $H = 600\ \mathrm{km}$ and
IFOV $= 15\ \mathrm{\mu rad}$. Then compute it for the same detector at $45°$
off-nadir (flat-Earth $\sec^{2}\phi$ rule).

**★2.** A detector has a ground pitch of $5\ \mathrm{m}$. Compute its Nyquist
frequency and the smallest spatial wavelength it can represent.

**★3.** Compute the Airy spot on the ground at $\lambda = 0.66\ \mathrm{\mu m}$ for
the default parameters and compare it with the GSD.

## ★★ Applied

**★★4.** Find the detector pitch (on the ground) that puts the optical cut-off
exactly at the sampling Nyquist frequency, i.e. $f_c = f_N$, at
$\lambda = 0.66\ \mathrm{\mu m}$ for $D = 0.30\ \mathrm{m}$ and
$H = 700\ \mathrm{km}$. Comment on the feasibility.

**★★5.** Compute $\mathrm{NE}\Delta T$ at $300\ \mathrm{K}$ and at
$320\ \mathrm{K}$ for the default $\mathrm{NE}\Delta L$ at $10.8\ \mathrm{\mu m}$,
and explain the direction of the change.

**★★6.** Using the revisit formula, compute the equatorial revisit time for a
$250\ \mathrm{km}$ swath with one and with two satellites. What swath would be
needed for a $2$-day revisit with one satellite?

**★★7.** Show that the contrast at a design's own Nyquist frequency is
$\mathrm{MTF}_{\rm net} = \operatorname{sinc}(1/2)\,(1 - 1/(2wf_c))$, and evaluate
it for $w = 8.40\ \mathrm{m}$ and $f_c = 0.64935\ \mathrm{cycles\,m^{-1}}$.

## ★★★ Research-oriented

**★★★8.** A single thermal band measures a pixel radiance of
$1.0213\times10^{7}\ \mathrm{W\,m^{-2}\,sr^{-1}\,m^{-1}}$ at
$10.8\ \mathrm{\mu m}$ over a $300\ \mathrm{K}$ background. Parametrise the
null space by finding the target temperature implied by assumed fractional covers
$f = 0.01, 0.10, 0.50$, and state precisely what a second band at a different
wavelength adds. Give the algebra of the two-band system.

**★★★9.** Specify a synthetic instrument for a task with three stated
requirements (a $20\ \mathrm{m}$ GSD in the visible, a $0.2\ \mathrm{K}$
$\mathrm{NE}\Delta T$ at $300\ \mathrm{K}$, and a $5$-day equatorial revisit),
checking each requirement against the geometry and stating which one forces the
others. A specification that could not be executed is a failed answer.
