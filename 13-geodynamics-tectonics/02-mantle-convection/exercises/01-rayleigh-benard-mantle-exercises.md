# Exercises — 13-02-01 Rayleigh-Benard Convection Applied to the Mantle

Attempt these before reading the
[solutions](./01-rayleigh-benard-mantle-solutions.md). The lesson is
[01 Rayleigh-Benard Convection](../01-rayleigh-benard-mantle.md). All parameter
sets are **SYNTHETIC**; $g = 9.81\ \mathrm{m\,s^{-2}}$ is standard and
$Ra_c = 27\pi^{4}/4$ is exact.

## ★ Foundational

**★1.** Using $\rho_0 = 3300\ \mathrm{kg\,m^{-3}}$,
$\alpha = 3\times10^{-5}\ \mathrm{K^{-1}}$,
$\kappa = 10^{-6}\ \mathrm{m^{2}\,s^{-1}}$, $\Delta T = 1300$ K,
$d = 700$ km and $\eta = 10^{21}\ \mathrm{Pa\,s}$, compute $Ra$.

**★2.** Write $27\pi^{4}/4$ as a decimal and compute the critical wavelength
$2\pi/k_c$ with $k_c = \pi/\sqrt{2}$, in units of $d$.

**★3.** For $Ra = 10^{6}$, compute the boundary-layer thickness and the Nusselt
number from the scaling laws. State one reason the Nusselt number you compute is
only an order-of-magnitude estimate.

## ★★ Applied

**★★4.** Derive $k_c^{2} = \pi^{2}/2$ by minimising $Ra(k) = (\pi^{2}+k^{2})^{3}/
k^{2}$, showing the derivative and the resulting $Ra_c$.

**★★5.** The lesson measures $Ra_c = 1707.8$ for no-slip boundaries. Compute the
ratio with the free-slip value and state two physical consequences of a no-slip
lid for mantle convection.

**★★6.** For an activation energy of $300\ \mathrm{kJ\,mol^{-1}}$, a boundary-layer
temperature drop of 150 K and an interior temperature of 1550 K, compute the
viscosity contrast across the boundary layer. What does it do to the *effective*
Rayleigh number?

## ★★★ Research-oriented

**★★★7.** Starting from the boundary-layer force balance, derive the velocity
scaling $u\sim(\kappa/d)Ra(\delta/d)^{2}$ and evaluate it for the whole-mantle
parameter set. The lesson's measured value is $0.26\ \mathrm{m\,yr^{-1}}$ against
a synthetic reference plate speed of $0.030\ \mathrm{m\,yr^{-1}}$. State what that
discrepancy does and does not say about the scaling.

**★★★8.** Design a numerical experiment to distinguish bottom heating from
internal heating in a convecting layer. State the configuration, the diagnostic,
the expected signature of each hypothesis, and the run length. A specification
that could not be executed is a failed answer.
