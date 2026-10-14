# Exercises — 07-05-03 Spherical Harmonic Solutions and Coefficient Interpretation

Attempt these before reading the
[solutions](./03-spherical-harmonic-solutions-solutions.md). The lesson is
[03 Spherical Harmonic Solutions and Coefficient Interpretation](../03-spherical-harmonic-solutions.md).
**All models and data in this module are SYNTHETIC.**

Constants: $GM = 3.986004418\times10^{14}\ \mathrm{m^{3}\,s^{-2}}$,
$R = 6371\ \mathrm{km}$, $\gamma = 9.80665\ \mathrm{m\,s^{-2}}$ (conventional
standard gravity), $1\ \mathrm{mGal} = 10^{-5}\ \mathrm{m\,s^{-2}}$. In the
$4\pi$ normalisation, $\bar P_{20}(1) = \sqrt{5}$ and
$\bar P_{20}(0) = -\sqrt{5}/2$.

## ★ Foundational

**★1.** A synthetic model has a single zonal coefficient $C_{20} =
2.0\times10^{-5}$ and all others zero. Compute the geoid undulation $N$ and the
gravity anomaly $\Delta g$ at the equator, showing each factor with its units.

**★2.** How many coefficients does a model complete to $L = 75$ contain, and
what half-wavelength $\pi R/L$ does that imply? State why the count grows as
$L^{2}$ while the resolution improves only as $1/L$.

**★3.** Verify by dimensional analysis that $GM/(R\gamma)$ is a length, and that
$(GM/R^{2})C_{lm}$ is an acceleration.

## ★★ Applied

**★★4.** Derive $\Delta g = -\partial T/\partial r - 2T/r = (GM/R^{2})\sum(l-1)
[\ldots]$ from $T \propto r^{-(l+1)}$ per degree. State the boundary condition
you use and where the $l+1$ becomes $l-1$.

**★★5.** Using the synthetic laws $\sigma_{l} = 1.0\times10^{-5}(2/l)^{2}$ and
$\epsilon_{l} = 3.0\times10^{-9}l^{1/2}$ (a synthetic error spectrum), find the
crossover degree to the nearest integer and the corresponding half-wavelength.
State what the coefficients above that degree represent.

**★★6.** Two analyses publish coefficient sets that differ by $2\%$ at degree
15 and $40\%$ at degree 120. Using the crossover argument, explain which
difference is more likely to be a difference in *data* and which in
*regularisation*, and state the one report item that would settle it.

## ★★★ Research-oriented

**★★★7.** Design a numerical experiment that demonstrates that high-degree
coefficients of an inverted model are determined by the chosen regularisation
rather than by the data. Specify the truth model, the forward operator, the noise
level, the regularisation family, and the diagnostic that reveals the effect.
Predict the shape of the curve you would plot.

**★★★8.** Bruns' formula uses $\gamma$ (normal gravity). Compute the relative
change in $N$ if $\gamma$ is taken as a constant $9.80665\ \mathrm{m\,s^{-2}}$
instead of varying with latitude over the range of a normal gravity formula
(use $\gamma_{0} = 9.7803$ and $\gamma_{90} = 9.8322\ \mathrm{m\,s^{-2}}$ as
*stated synthetic* extremes). State whether this matters for a $1\ \mathrm{cm}$
geoid target, and what an analyst must therefore do.
