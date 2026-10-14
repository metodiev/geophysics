# Exercises — 07-01-01 Newtonian Gravitation, Field and Acceleration

Attempt these before reading the
[solutions](./01-newtonian-gravity-solutions.md). The lesson is
[01 Newtonian Gravitation, Field and Acceleration](../01-newtonian-gravity.md).
All models are **SYNTHETIC** teaching values; use
$G = 6.67430\times10^{-11}\ \mathrm{m^{3}\,kg^{-1}\,s^{-2}}$ and
$1\ \mathrm{mGal} = 10^{-5}\ \mathrm{m\,s^{-2}}$.

## ★ Foundational

**★1.** A point mass $M = 2.00\times10^{11}\ \mathrm{kg}$ sits at the origin.
Compute the field magnitude at $r = 500\ \mathrm{m}$ and $r = 1000\ \mathrm{m}$,
give both in $\mathrm{m\,s^{-2}}$ and in mGal, and state the ratio of the two
magnitudes.

**★2.** Two equal masses of $5.00\times10^{11}\ \mathrm{kg}$ are placed at
$x = -1500\ \mathrm{m}$ and $x = +1500\ \mathrm{m}$. Compute the field vector at
$(0, 0, 0)$ and at $(+750, 0, 0)$, in $\mathrm{m\,s^{-2}}$, and state why the
first calculation needs no arithmetic beyond symmetry.

**★3.** Convert $3.50\ \mathrm{mGal}$ into $\mathrm{m\,s^{-2}}$ and into µGal,
showing the chain of factors. State how many µGal a modern relative meter's
resolution of $3\times10^{-8}\ \mathrm{m\,s^{-2}}$ corresponds to.

## ★★ Applied

**★★4.** A SYNTHETIC survey finds a symmetric anomaly of peak
$2.00\ \mathrm{mGal}$ and half-width $x_{1/2} = 450\ \mathrm{m}$. Estimate the
centre depth of the body, then, for $\Delta\rho = 350\ \mathrm{kg\,m^{-3}}$,
estimate its radius. State which of your two answers would change if the density
contrast were actually $700\ \mathrm{kg\,m^{-3}}$.

**★★5.** A station at elevation $0\ \mathrm{m}$ reads
$g = 982\,025.05\ \mathrm{mGal}$ in the spherical model of the lesson. Using the
measured free-air coefficient $0.308280\ \mathrm{mGal\,m^{-1}}$, predict the
reading at $+620\ \mathrm{m}$, and compare it with the value obtained directly
from $g = GM/r^{2}$ with $r = R_{\text{mean}} + 620\ \mathrm{m}$. Explain the
sign and size of any difference.

**★★6.** The demonstration reports the interior shell residual as
$6.59\times10^{-5}$ of $GM/R^{2}$ at $N = 500$ and $8.59\times10^{-7}$ at
$N = 8000$. By what factor did the residual fall when $N$ increased by a factor
of $16$? What scaling does that suggest, and what would you expect at
$N = 32000$? State why the exact theorem is still exactly true.

## ★★★ Research-oriented

**★★★7.** Design a numerical experiment that measures how large the error of the
point-mass approximation becomes for a non-spherical body. Use a spheroid of
polar semi-axis $b$ and equatorial semi-axis $a$, vary the depth-to-size ratio
$z/a$ over at least two decades, and define the error metric precisely (which
component, at which station, normalised by what). Predict the scaling you expect
before running it, and state what would falsify your prediction.

**★★★8.** A gravity null is sometimes used to argue that a buried body is
"symmetric". Specify an observation set that could distinguish (i) a genuine
absence of mass from (ii) two bodies whose vertical attractions cancel at that
point. Give the minimum number of stations, their geometry, and the quantity you
would plot.

**★★★9.** The lesson derives $\mathrm{d}g/\mathrm{d}r = -2g/r$ for a sphere. Show
that for an observation point above a *thin infinite sheet* of surface density
$\sigma$, $\mathrm{d}g_z/\mathrm{d}z = 0$ outside the sheet, and reconcile the two
results. Which one applies to a Bouguer slab correction, and why does the answer
matter for the interpretation of a plateau?
