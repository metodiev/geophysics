# Exercises — 17-01-02 Reflectance, Emissivity and Spectral Signatures

Attempt these before reading the
[solutions](./02-reflectance-and-emissivity-solutions.md). The lesson is
[02 Reflectance, Emissivity and Spectral Signatures](../02-reflectance-and-emissivity.md).
All models are **SYNTHETIC**; the physical constants are exact SI values.

Constants: $h = 6.62607015\times10^{-34}\ \mathrm{J\,s}$,
$c = 2.99792458\times10^{8}\ \mathrm{m\,s^{-1}}$,
$k_B = 1.380649\times10^{-23}\ \mathrm{J\,K^{-1}}$.

## ★ Foundational

**★1.** A surface has $\rho = 0.25$ and is illuminated with
$E = 1000\ \mathrm{W\,m^{-2}}$. Compute its Lambertian radiance and state the
unit.

**★2.** A surface has $\rho = 0.12$ and $\tau = 0.03$ at some wavelength. Compute
its absorptance and its emissivity by Kirchhoff's law.

**★3.** Compute the brightness temperature of a measured radiance
$L = 8.00\times10^{6}\ \mathrm{W\,m^{-2}\,sr^{-1}\,m^{-1}}$ at
$\lambda = 10.8\ \mathrm{\mu m}$. Is it above or below the true surface
temperature if $\varepsilon < 1$?

## ★★ Applied

**★★4.** Derive $L = \rho E/\pi$ by integrating the BRDF over the hemisphere.
Then show numerically what error results if the $1/\pi$ is omitted for
$\rho = 0.363$, $E = 800\ \mathrm{W\,m^{-2}}$.

**★★5.** The sensitivity of a retrieved temperature to emissivity is
$\lambda k_B T^{2}/(hc)$. Compute it at $\lambda = 10.8\ \mathrm{\mu m}$,
$T = 300\ \mathrm{K}$, and use it to find the temperature bias for assumed
emissivities that are $1\%$, $5\%$ and $10\%$ too high when the true emissivity
is $0.95$.

**★★6.** Using the demonstration's notional band means, compute the normalised
difference $(R_{\rm NIR}-R_{\rm red})/(R_{\rm NIR}+R_{\rm red})$ for the
soil-like, vegetation-like and water-like surfaces, and interpret the three
values.

**★★7.** The demonstration reports broadband albedos of $0.395$ (solar-like
illumination) and $0.416$ (reddened illumination) for the soil-like surface.
Compute the relative change and explain, in terms of the reflectance curve's
slope, why the reddened value is larger.

## ★★★ Research-oriented

**★★★8.** Sensor radiance is $L_b = g\rho_b + \beta_b$ with $g$ a common
multiplicative gain and $\beta_b$ an additive path radiance in band $b$ that
differs between bands. Analyse the ratio $R = L_2/L_1$: show that it cancels $g$
exactly when $\beta_1 = \beta_2 = 0$, and derive the residual error when
$\beta_b \ne 0$. State the condition on $\beta/\rho$ for the ratio to remain
usable to $1\%$.

**★★★9.** A field campaign measures directional reflectance at five view zenith
angles. Specify the measurement and processing steps needed to report a
hemispherical reflectance with a stated uncertainty, and name the two largest
error sources. A specification that could not be executed is a failed answer.
