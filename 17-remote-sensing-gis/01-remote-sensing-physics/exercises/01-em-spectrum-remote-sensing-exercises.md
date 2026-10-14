# Exercises — 17-01-01 The Electromagnetic Spectrum and Sensing Windows

Attempt these before reading the
[solutions](./01-em-spectrum-remote-sensing-solutions.md). The lesson is
[01 The Electromagnetic Spectrum and Sensing Windows](../01-em-spectrum-remote-sensing.md).
All models are **SYNTHETIC**; the physical constants are exact SI values.

Constants you may need: $h = 6.62607015\times10^{-34}\ \mathrm{J\,s}$,
$c = 2.99792458\times10^{8}\ \mathrm{m\,s^{-1}}$,
$k_B = 1.380649\times10^{-23}\ \mathrm{J\,K^{-1}}$,
$\sigma = 5.670374419\times10^{-8}\ \mathrm{W\,m^{-2}\,K^{-4}}$,
$b = 2.897771955\times10^{-3}\ \mathrm{m\,K}$,
$S = 1361\ \mathrm{W\,m^{-2}}$.

## ★ Foundational

**★1.** A candidate band has $\lambda = 3.70\ \mathrm{\mu m}$. Compute its
frequency in THz and its photon energy in eV. Show the arithmetic.

**★2.** A cloud top is at $T = 220\ \mathrm{K}$. Compute its Wien peak
wavelength, its Stefan-Boltzmann exitance, and the ratio of that exitance to the
Earth's at $288\ \mathrm{K}$.

**★3.** Define optical depth $\tau$ and transmittance $T$. If $T = 0.50$, what is
$\tau$? If $\tau = 3$, what is $T$?

## ★★ Applied

**★★4.** Using the demonstration's synthetic atmosphere, the transmittance at
$2.70\ \mathrm{\mu m}$ is $0.015$. Compute the *round-trip* transmittance for
reflected sunlight at this wavelength and state whether the band is usable.

**★★5.** At $0.66\ \mathrm{\mu m}$ the synthetic transmittance is $0.773$; at
$11.0\ \mathrm{\mu m}$ it is $0.498$. A reflected-solar sensor and a thermal
sensor both observe a surface. Compute the two-way loss for the reflected case
and the one-way loss for the thermal case, and state which band loses more
fractional signal to the atmosphere.

**★★6.** Compute the Rayleigh scattering weight at $0.45\ \mathrm{\mu m}$ and at
$0.65\ \mathrm{\mu m}$ relative to $0.55\ \mathrm{\mu m}$, and state one
consequence for a blue-band versus a red-band surface reflectance product.

**★★7.** A blackbody at $400\ \mathrm{K}$ is observed in the $8$–$13\
\mathrm{\mu m}$ window. Compute its spectral radiance at $10\ \mathrm{\mu m}$ and
compare with the Earth's at $288\ \mathrm{K}$.

## ★★★ Research-oriented

**★★★8.** Design a two-band ratio index that is invariant to a multiplicative
gain (sensor gain or a uniform change in illumination) but sensitive to a surface
property. State the index algebraically, prove the invariance, and state the
assumption about the atmosphere that makes the invariance fail.

**★★★9.** The demonstration reports a greenhouse gap of $33.4\ \mathrm{K}$ for
$A = 0.30$. Derive $\partial T_{\rm eff}/\partial A$ at that point and use it to
state how much the effective temperature changes for a $0.01$ change in albedo.
Then explain in two sentences why this sensitivity does *not* mean the surface
temperature changes by the same amount.
