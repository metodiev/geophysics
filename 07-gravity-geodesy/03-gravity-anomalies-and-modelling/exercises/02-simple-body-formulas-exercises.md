# Exercises — 07-03-02 Analytical Formulas for Sphere, Cylinder, Sheet and Dyke

Attempt these before reading the
[solutions](./02-simple-body-formulas-solutions.md). The lesson is
[02 Analytical Formulas](../02-simple-body-formulas.md). Use
$G = 6.67430\times10^{-11}\ \mathrm{m^{3}\,kg^{-1}\,s^{-2}}$ and
$1\ \mathrm{mGal} = 10^{-5}\ \mathrm{m\,s^{-2}}$.

## ★ Foundational

**★1.** Evaluate the infinite-sheet formula for
$\Delta\rho = 250\ \mathrm{kg\,m^{-3}}$ and $t = 100\ \mathrm{m}$, in both
$\mathrm{m\,s^{-2}}$ and mGal.

**★2.** Show that the 2-D kernel $z'/(u^{2}+z'^{2})$ has the dimensions of
$1/\mathrm{length}$, and hence that
$2G\Delta\rho\times(\mathrm{length})$ is an acceleration.

**★3.** State the value of the semi-infinite sheet anomaly at $x = 0$, in terms of
the slab value, and say why the thickness drops out of the ratio.

## ★★ Applied

**★★4.** Differentiate the semi-infinite sheet formula

$$g_z(x) = 2G\Delta\rho\left[\tfrac{\pi}{2}(z_2-z_1)
+ z_2\arctan\tfrac{x}{z_2} - z_1\arctan\tfrac{x}{z_1}
+ \tfrac{x}{2}\ln\tfrac{x^{2}+z_2^{2}}{x^{2}+z_1^{2}}\right]$$

with respect to $x$ and show that the derivative vanishes at $x = 0$ and has its
maximum magnitude there.

**★★5.** A dyke has an $800\ \mathrm{m}$-wide rectangular cross-section from
$400\ \mathrm{m}$ to $4000\ \mathrm{m}$ depth, with
$\Delta\rho = 350\ \mathrm{kg\,m^{-3}}$. Compute the anomaly at $x = 0$ and at
$x = 2000\ \mathrm{m}$, and compare with the infinite-slab value for the same
thickness.

**★★6.** Repeat ★5 for a $200\ \mathrm{m}$-wide dyke and state what the comparison
shows about the slab approximation.

## ★★★ Research-oriented

**★★★7.** Derive $J(u) = \tfrac{1}{2}\left[P(u,z_2)-P(u,z_1)\right]$ from the
inner depth integral, verify $J'(u) = \tfrac{1}{2}\ln\left[(u^{2}+z_2^{2})/(u^{2}+z_1^{2})\right]$,
and confirm the slab limit $x_1\to-\infty$, $x_2\to+\infty$ analytically.

**★★★8.** For a $200\ \mathrm{m}$-thick horizontal sheet at $500\ \mathrm{m}$ depth,
find the half-width at which a finite rectangle reaches $99\%$ of the infinite-slab
value, and state the rule that follows for the minimum survey extent needed to
justify a slab reduction.
