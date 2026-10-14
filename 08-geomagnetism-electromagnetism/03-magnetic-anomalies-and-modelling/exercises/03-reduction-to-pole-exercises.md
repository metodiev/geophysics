# Exercises — 08-03-03 Reduction to the Pole and Equator

Attempt these before reading the
[solutions](./03-reduction-to-pole-solutions.md). The lesson is
[03 Reduction to the Pole and Equator](../03-reduction-to-pole.md). All models are
**SYNTHETIC**.

## ★ Foundational

**★1.** State the RTP filter in the wavenumber domain and identify the direction
in the $(k_x,k_y)$ plane along which it is singular when
$\hat m = \hat f = \hat x$ (the equator).

**★2.** Write the anomaly of a point dipole as two directional derivatives of
$1/r$ and state which quantity in the expression is the depth and which are the
directions.

**★3.** For the demonstration's synthetic dipole (moment $2.00\times10^{9}$
A m$^2$ at 3.0 km depth) compute the pole-equivalent on-axis anomaly from
$(\mu_0/4\pi)(2m/z^{3})$.

## ★★ Applied

**★★4.** Using the demonstration's inclination table (peak displacement 1.2 km
and peak 9.098 nT at $I = 45^\circ$; 2.0 km at $I = 30^\circ$; 2.8 km at
$I = 15^\circ$), state the trend and give one sentence of physical explanation.

**★★5.** A survey has 0.20 nT rms noise. Using the noise-gain table
(1.44 at $45^\circ$, 3.48 at $20^\circ$, 8.93 at $10^\circ$), compute the noise
level in each RTP product. If the target anomaly is 5 nT, state the inclination
below which RTP should not be attempted.

**★★6.** In the demonstration, RTP at $I = 45^\circ$ recovers the pole peak to
$-0.09\%$ while the noise-injected data have a peak-to-background ratio of 12.9
against 91 before filtering. Reconcile these two statements: what is preserved
and what is not?

## ★★★ Research-oriented

**★★★7.** The Poisson relation is verified in the demonstration by finite
differences with errors $2.96\times10^{-2}$, $8.66\times10^{-3}$,
$2.37\times10^{-3}$ and $6.21\times10^{-4}$ at $h = 0.2, 0.1, 0.05, 0.025$ km.
Compute the three successive error ratios and state the order of convergence.

**★★★8.** Design an experiment to measure how much damage RTP does when its
central assumption is wrong: take a data set produced by an induced body and
apply RTP using a magnetisation direction rotated $30^\circ$ from the truth.
State the metric, the reference, and the expected qualitative result.

**★★★9.** The demonstration tapers the grid with a flat-top window before
transforming. Explain, with the shape of the $1/r$ spectrum in mind, why a taper
is needed and what it costs.
