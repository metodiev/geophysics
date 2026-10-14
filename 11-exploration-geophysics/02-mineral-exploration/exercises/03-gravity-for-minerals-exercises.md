# Exercises — 11-02-03 Gravity for Chromite, Massive Sulphide and Iron Ore

Attempt these before reading the
[solutions](./03-gravity-for-minerals-solutions.md). The lesson is
[03 Gravity for Minerals](../03-gravity-for-minerals.md). All contrasts,
geometries, noise and reduction densities are **SYNTHETIC** teaching values.

Useful: $G = 6.67430\times10^{-11}\ \mathrm{m^{3}\,kg^{-1}\,s^{-2}}$,
$1\ \mathrm{mGal} = 10^{-5}\ \mathrm{m\,s^{-2}}$, $g = 9.80665\
\mathrm{m\,s^{-2}}$, $a = 6.371\times10^{6}\ \mathrm{m}$,
$\sqrt{2^{2/3}-1} = 0.766421$.

## ★ Foundational

**★1.** A SYNTHETIC chromite body is modelled as (a) a sphere and (b) an infinite
horizontal cylinder, both of radius $R = 90\ \mathrm{m}$ with their centre or axis
at $z = 180\ \mathrm{m}$, and $\Delta\rho = 450\ \mathrm{kg\,m^{-3}}$. Compute
both peak anomalies and their ratio.

**★2.** For the cylinder of ★1, compute the excess mass per unit length
$\lambda$ and verify the peak anomaly against $2G\lambda/z$.

**★3.** For a measured half-width at half-maximum of $180\ \mathrm{m}$, state the
depth implied by the cylinder rule and the depth implied by the sphere rule.

**★4.** Compute the free-air gradient from $2g/a$ and the Bouguer slab coefficient
$2\pi G\rho$ for $\rho = 2400\ \mathrm{kg\,m^{-3}}$, both in
$\mathrm{mGal\,m^{-1}}$; then compute the net correction for $200\ \mathrm{m}$ of
relief at that density.

## ★★ Applied

**★★5.** A SYNTHETIC 2-D anomaly has a peak of $2.400\ \mathrm{mGal}$ and a
half-width at half-maximum of $300\ \mathrm{m}$ on a profile across strike.
Compute the depth, $\lambda$ and the density contrast for a radius of
$120\ \mathrm{m}$. Then compute the radius that would be required if the body were
a sphere fitting the same two numbers, and state which model the data cannot
exclude.

**★★6.** Using the window-efficiency formula
$\lambda_{\text{rec}}/\lambda = (2/\pi)\arctan(X/z)$, compute the window half-length
$X$ needed to recover $90\%$ and $95\%$ of the mass of a body at
$z = 400\ \mathrm{m}$, and state the practical consequence for a survey whose
stations cover $3\ \mathrm{km}$ each side of the anomaly.

**★★7.** A survey must resolve a $0.5\ \mathrm{mGal}$ target over terrain with
$80\ \mathrm{m}$ of relief. Compute the free-air and Bouguer contributions at
$\rho = 2670\ \mathrm{kg\,m^{-3}}$, the residual if the height is in error by
$0.5\ \mathrm{m}$, and the height accuracy needed for a $0.02\ \mathrm{mGal}$
budget.

**★★8.** From the lesson's regional-removal table, compute the fractional change
in the residual peak and in the implied depth between the linear and quadratic
regional models, and between the quadratic and cubic models. State what the second
comparison tells you about the choice.

## ★★★ Research-oriented

**★★★9.** Construct an explicit exact non-uniqueness for 2-D gravity and verify it
numerically: an infinite horizontal sheet of surface density $\sigma$ produces the
same vertical attraction at every height, so a model may be altered by adding a
sheet of $+\sigma$ at one depth and one of $-\sigma$ at another without changing
the field. Write down the composite model, verify the cancellation to machine
precision, and state what this implies about the information content of a gravity
map with respect to density layering.

**★★★10.** Design a survey that distinguishes a cylinder from a sphere using the
minimum number of measurements, given that a single profile cannot. State the
geometry, the discriminating quantity, the number of stations required for a
stated confidence, and the way you would test the design on a synthetic
benchmark before committing to it.

**★★★11.** A massive sulphide target has an uncertain density contrast spanning
$300$–$900\ \mathrm{kg\,m^{-3}}$. Propagate that range through (a) the peak
amplitude, (b) the depth from the half-width, and (c) the mass from the excess-mass
integral, and state which of the three quantities is robust and which is not.
