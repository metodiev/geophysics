# Exercises — 13-01-03 Lithospheric Strength, Effective Elastic Thickness and Flexure

Attempt these before reading the
[solutions](./03-lithospheric-strength-solutions.md). The lesson is
[03 Lithospheric Strength](../03-lithospheric-strength.md). All models are
**SYNTHETIC**; $g = 9.81\ \mathrm{m\,s^{-2}}$ and
$E = 70\ \mathrm{GPa}$, $\nu = 0.25$, $\Delta\rho = 2300\ \mathrm{kg\,m^{-3}}$
where stated.

## ★ Foundational

**★1.** Compute the flexural rigidity $D$ and the flexural parameter $\alpha$ for
$T_e = 15$ km.

**★2.** For $T_e = 20$ km, compute $D$ and $\alpha$, then compute the deflection
at the load from a line load $V_0 = 2\times10^{12}\ \mathrm{N\,m^{-1}}$ for a
continuous plate and for a broken plate.

**★3.** State the unit of $\alpha$, and verify by dimensional analysis that
$\alpha = (D/\Delta\rho g)^{1/4}$ has that unit.

## ★★ Applied

**★★4.** Derive the isostatic-area identity
$\int_{-\infty}^{\infty}w\,\mathrm{d}x = V_0/(\Delta\rho g)$ for the line-load
solution, showing the integral explicitly. State in one sentence what physical
statement the identity encodes.

**★★5.** A synthetic deflection profile has a central amplitude of 1500 m under a
known line load $V_0 = 3\times10^{12}\ \mathrm{N\,m^{-1}}$ on a continuous plate.
Invert the two relations $w(0) = V_0\alpha^{3}/(2D)$ and
$\alpha^{4} = D/(\Delta\rho g)$ for $\alpha$, $D$ and $T_e$. State which of the
two data (load or deflection) dominates the error in $T_e$.

**★★6.** Using the parameter $\alpha$ from ★2, decide whether a load of half-width
30 km is "narrow" or "wide" by computing $a/\alpha$ and interpolating the
measured table in the lesson. Give the ratio $w(0)/w_{\text{Airy}}$ you expect.

## ★★★ Research-oriented

**★★★7.** The lesson's yield-strength-envelope calculation gives
$T_e = 83.8$, $49.5$ and $24.4$ km at curvatures of $10^{-8}$, $10^{-7}$ and
$10^{-6}\ \mathrm{m^{-1}}$. Compute the power-law exponent in
$T_e\propto\kappa^{p}$ from these numbers and compare it with the perfectly
plastic limit $p = -1/2$. Explain in two sentences why the measured exponent is
smaller in magnitude.

**★★★8.** Design an inversion for $T_e$ that treats the load density as unknown.
State the parameterisation, the data, the forward model, the misfit, the
regularisation if any, and the diagnostic that would reveal the
$T_e$–load-density trade-off. State what a *successful* inversion would report.

**★★★9.** A flexure study reports $T_e = 30 \pm 2$ km from a deflection profile
and a strength-envelope calculation gives $T_e = 50$ km for the same region with
a 20 K/km geotherm and $\kappa = 10^{-7}\ \mathrm{m^{-1}}$. Give three
physically distinct explanations for the discrepancy and, for each, one
measurement that would test it.
