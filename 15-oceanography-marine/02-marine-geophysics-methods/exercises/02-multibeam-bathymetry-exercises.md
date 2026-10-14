# Exercises — 15-02-02 Multibeam Bathymetry and Swath Mapping

Attempt these before reading the
[solutions](./02-multibeam-bathymetry-solutions.md). The lesson is
[02 Multibeam Bathymetry](../02-multibeam-bathymetry.md). All parameters are
**SYNTHETIC** teaching values.

Constants: $1\ \mathrm{kn} = 0.514444\ \mathrm{m\,s^{-1}}$,
$c_{\text{ref}} = 1500\ \mathrm{m\,s^{-1}}$,
$1^\circ = 0.0174533\ \mathrm{rad}$.

## ★ Foundational

**★1.** Compute the swath width and the outer-beam slant range for
$z = 800\ \mathrm{m}$ and $\theta_{\max} = 65^\circ$. State the width-to-depth
ratio.

**★2.** Compute the nadir across-track footprint for $z = 800\ \mathrm{m}$ and
$\Delta\theta = 1^\circ$, and state its units.

**★3.** Show that a fractional error $\epsilon$ in the assumed sound speed
produces a depth error $\delta z/z = \epsilon$ exactly, starting from
$R = ct/2$. State the single assumption.

## ★★ Applied

**★★4.** Derive $\ell_{\text{across}} = z\,\Delta\theta/\cos^{2}\theta$ from
$R = z/\cos\theta$, and evaluate it at $\theta = 0^\circ$, $45^\circ$ and
$65^\circ$ for $z = 800\ \mathrm{m}$ and $\Delta\theta = 1^\circ$. State the
growth factor at each angle.

**★★5.** A survey must be accurate to $\pm3\ \mathrm{m}$ in $1200\ \mathrm{m}$ of
water. If the sound-speed term is allowed half the budget, what fractional
sound-speed accuracy is required, and what is that in
$\mathrm{m\,s^{-1}}$?

**★★6.** At $z = 1500\ \mathrm{m}$ with $\theta_{\max} = 60^\circ$, compute the
cross-track displacement produced by roll biases of $0.02^\circ$, $0.10^\circ$ and
$0.50^\circ$, and compare each with the outer-beam across-track footprint for
$\Delta\theta = 1^\circ$.

**★★7.** A vessel steams at $6\ \mathrm{kn}$ with a ping rate of $12\ \mathrm{Hz}$
and a beam spacing of $0.5^\circ$, in water $1200\ \mathrm{m}$ deep. Compute
(a) the along-track ping spacing, (b) the across-track beam spacing at nadir,
(c) the ratio between them, and (d) the sounding density at nadir in
soundings per $\mathrm{m^{2}}$.

## ★★★ Research-oriented

**★★★8.** A new bathymetric grid is delivered with no metadata beyond a cell
size. Design a verification procedure that would detect and, if possible,
quantify a uniform sound-speed scale error in it. State the independent reference
the test requires, the size of the error you could detect, and the failure mode
that would make the test give a false all-clear. A specification that could not be
executed is a failed answer.

**★★★9.** The lesson claims that a sound-speed error is coherent across a swath
while an attitude error is largest at the swath edges. Construct a synthetic
experiment that would separate the two in a single survey line: state the
covariates you would fit, the degeneracy you expect between them, and one
additional piece of data that breaks it. Derive the mathematical form of each
error's spatial signature.
