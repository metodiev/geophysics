# Exercises — 07-02-01 Absolute Gravimeters: Free-Fall and Interferometry

Attempt these before reading the
[solutions](./01-absolute-gravimeters-solutions.md). The lesson is
[01 Absolute Gravimeters: Free-Fall and Interferometry](../01-absolute-gravimeters.md).
All models are **SYNTHETIC**. Use
$1\ \mathrm{\mu Gal} = 10^{-8}\ \mathrm{m\,s^{-2}}$ and the lesson's measured
sensitivities where they apply: $2.625\ \mathrm{\mu Gal}$ per nanometre of position
noise, $3.066\ \mathrm{\mu Gal}$ per nanosecond of timing jitter (both for the
$0.200\ \mathrm{m}$, 700-sample drop), $308.280\ \mathrm{\mu Gal\,m^{-1}}$ for the
vertical gradient, and the drag rule "bias $= -\tfrac12\times$ terminal drag".

## ★ Foundational

**★1.** A SYNTHETIC drop covers $h = 0.150\ \mathrm{m}$ in
$t = 0.1748\ \mathrm{s}$. Compute $g$ from $g = 2h/t^{2}$. Then compute how much $g$
changes if the time is wrong by $+0.1\ \mathrm{ms}$, and state what that implies
about the two-point method.

**★2.** For a $0.150\ \mathrm{m}$ drop and a SYNTHETIC wavelength of
$633.0\ \mathrm{nm}$, compute the displacement per fringe and the total fringe count
$2h/\lambda$.

**★3.** Three SYNTHETIC samples of a drop are $t = 0$, $0.05$, $0.10\ \mathrm{s}$ with
$z = 0$, $0.01227531$, $0.04910125\ \mathrm{m}$. Fit
$z = z_{0} + v_{0}t + \tfrac12 gt^{2}$ (three equations, three unknowns) and state
$g$ exactly. Explain why three noiseless points give the exact answer and why real
data need many more.

## ★★ Applied

**★★4.** Using the measured sensitivities, compute the uncertainty of $g$ from one
drop with $1\ \mathrm{nm}$ of position noise *and* $1\ \mathrm{ns}$ of timing
jitter, treating them as independent. Then compute the number of drops needed to
reduce this to $0.5\ \mathrm{\mu Gal}$ (random terms only), and state whether that
would achieve a $0.5\ \mathrm{\mu Gal}$ accurate value.

**★★5.** The terminal drag deceleration in a SYNTHETIC drop is
$150\ \mathrm{\mu Gal}$. Compute the resulting bias in the fitted $g$ and the drag
coefficient that would keep the bias below $2\ \mathrm{\mu Gal}$ for a drop of
$0.2018\ \mathrm{s}$ with $g = 9.820250\ \mathrm{m\,s^{-2}}$.

**★★6.** A SYNTHETIC tide of amplitude $1.2\times10^{-6}\ \mathrm{m\,s^{-2}}$ with a
period of $12.4\ \mathrm{h}$ runs during a $30$-minute drop set starting at zero
phase. Compute the mean tidal acceleration over the set, the value at the midpoint,
their difference, and the peak-to-peak change across the set. State whether a
midpoint correction is adequate for a $1\ \mathrm{\mu Gal}$ claim.

## ★★★ Research-oriented

**★★★7.** Design an absolute-gravity measurement that claims $1\ \mathrm{\mu Gal}$
(1σ) in the combined budget. List every systematic term from the lesson with a
target value, show the quadrature sum, and state which term dominates. Specify the
number of drops and the set structure, and say what would falsify your claim.

**★★★8.** Design an intercomparison between two SYNTHETIC absolute gravimeters at
the same station. Specify the measurement protocol, how you would separate a
station difference from an instrument difference, what statistics you would use,
and how you would detect a shared bias (for example the same tide model) that the
comparison cannot reveal.

**★★★9.** You may spend a fixed total time on a station. Extra drops improve the
random term as $1/\sqrt{n}$; extra time also changes the tidal mean and allows more
repeats of an independent check. Using the lesson's numbers, compute the allocation
that minimises the total uncertainty for a stated budget, and state the assumption
that makes your allocation wrong.
