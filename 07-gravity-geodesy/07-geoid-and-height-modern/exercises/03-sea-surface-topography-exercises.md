# Exercises — 07-07-03 Sea Surface Topography and the Marine Geoid

Attempt these before reading the
[solutions](./03-sea-surface-topography-solutions.md). The lesson is
[03 Sea Surface Topography](../03-sea-surface-topography.md). **All models and
data in this module are SYNTHETIC.**

Constants: $g = 9.81\ \mathrm{m\,s^{-2}}$,
$\Omega = 7.2921150\times10^{-5}\ \mathrm{rad\,s^{-1}}$,
$f = 2\Omega\sin\varphi$ (so $f = 8.3652\times10^{-5}$ at $35^\circ$N,
$9.3746\times10^{-5}$ at $40^\circ$N, $1.1172\times10^{-4}$ at $50^\circ$N).

## ★ Foundational

**★1.** Compute the cross-stream sea-surface slope required to drive a
$0.5\ \mathrm{m\,s^{-1}}$ geostrophic current at $50^\circ$N, in millimetres of
height per kilometre.

**★2.** Using a constant-slope estimate, compute the geostrophic velocity implied
by a $2.0\ \mathrm{m}$ dynamic topography across a $200\ \mathrm{km}$ jet at
$35^\circ$N. State why the estimate is an upper bound for a real jet.

**★3.** Compute the scale of the geoid relative to the MDT for $N = 100\
\mathrm{m}$ and a $1.5\ \mathrm{m}$ MDT, and state what relative accuracy the
geoid needs.

## ★★ Applied

**★★4.** Compute the velocity error produced by a $3\ \mathrm{cm}$ geoid error at
wavelengths of $100$, $300$ and $1000\ \mathrm{km}$ at $40^\circ$N, and state
which of those scales matters for a jet of $100\ \mathrm{km}$ width.

**★★5.** Explain why a $20$-year altimetric mean does not reduce a geoid error,
and state precisely what it does reduce. Support the answer with a variance
argument.

**★★6.** Two MDT products are compared and differ by $8\ \mathrm{cm}$ in the
region of a western boundary current. List the three possible causes in order of
likelihood and state the diagnostic that distinguishes them.

## ★★★ Research-oriented

**★★★7.** Design a validation experiment for an MDT product: specify the
independent data, the diagnostic at each scale, the noise model, and the
degeneracy that remains even if the validation passes.

**★★★8.** Design a synthetic experiment that measures how much an error in the
inverted-barometer correction contaminates a geoid-based transport estimate, and
state which observable distinguishes it from a geoid error of the same size.
