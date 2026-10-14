# Exercises — 15-01-01 Seawater Properties: Temperature, Salinity, Density

Attempt these before reading the
[solutions](./01-seawater-properties-solutions.md). The lesson is
[01 Seawater Properties](../01-seawater-properties.md). All models and data are
**SYNTHETIC** teaching values.

Unless a problem says otherwise, use the teaching equation of state
$\rho = \rho_0[1 - \alpha(T-T_0) + \beta(S-S_0) + \kappa p]$ with
$\rho_0 = 1027.0\ \mathrm{kg\,m^{-3}}$, $T_0 = 10\ ^\circ$C,
$S_0 = 35.0\ \mathrm{g\,kg^{-1}}$, $\alpha = 1.70\times10^{-4}\
{}^\circ\mathrm{C}^{-1}$, $\beta = 7.60\times10^{-4}\
\mathrm{(g\,kg^{-1})^{-1}}$, $\kappa = 4.40\times10^{-6}\ \mathrm{dbar^{-1}}$,
$g = 9.81\ \mathrm{m\,s^{-2}}$ and $\sigma = \rho - 1000$.

## ★ Foundational

**★1.** Compute $\sigma_t$ for $(T,S) = (5.0\ ^\circ\mathrm{C},
34.5\ \mathrm{g\,kg^{-1}})$ at $p = 0$. Show every term and state the unit of
each.

**★2.** State the units of $\alpha$, $\beta$ and $\kappa$, and verify by
dimensional analysis that $\alpha(T-T_0) + \beta(S-S_0) + \kappa p$ is
dimensionless.

**★3.** Using $p \approx \rho_0 g z/10^{4}$, compute the pressure in dbar at
$z = 3000\ \mathrm{m}$ and the compression contribution
$\kappa p \rho_0$ to the density there, in $\mathrm{kg\,m^{-3}}$ and as a
percentage of $\rho_0$.

## ★★ Applied

**★★4.** A station has $T = 22.0\ ^\circ$C, $S = 35.80\ \mathrm{g\,kg^{-1}}$ at
the surface and $T = 6.0\ ^\circ$C, $S = 35.00\ \mathrm{g\,kg^{-1}}$ at 1000 m.
(a) Compute $\sigma_t$ at both levels. (b) Treat the column as two layers and
compute $N^{2}$ as one finite difference, with $z$ positive downward. State the
buoyancy period. (c) Repeat using in-situ density at 1000 m by adding the
compression term at $p = 1007$ dbar. By what factor does the column appear more
stable than it is?

**★★5.** For the two water masses A $(14.00\ ^\circ$C,
$35.500\ \mathrm{g\,kg^{-1}})$ and B $(2.00\ ^\circ\mathrm{C},
33.289\ \mathrm{g\,kg^{-1}})$ and the curved equation of state
$\rho = \rho_0[1 - (\alpha_0\Delta T + \tfrac12\Delta_\alpha\Delta T^{2})
+ \beta\Delta S + \kappa p]$ with $\Delta_\alpha = 1.50\times10^{-5}\
{}^\circ\mathrm{C}^{-2}$ and $\Delta T = T - 10$: (a) verify that A and B have
equal density; (b) compute the density of the 50/50 mixture and the mean of the
two densities; (c) state the cabbeling anomaly and the sign convention you used.
(d) Now set $\Delta_\alpha = 0$ and show algebraically that the anomaly vanishes
for *any* two water masses.

**★★6.** An echo sounder assumes $c = 1500\ \mathrm{m\,s^{-1}}$ and reports a
depth of $4000\ \mathrm{m}$. The true sound speed along the path is
$1540\ \mathrm{m\,s^{-1}}$. (a) Compute the true depth. (b) Repeat for a true
speed of $1460\ \mathrm{m\,s^{-1}}$. (c) State the fractional depth error in each
case and compare it with the fractional speed error.

## ★★★ Research-oriented

**★★★7.** Design a measurement programme that would distinguish "the water
column is statically stable" from "the column is stable with respect to
adiabatic displacement". State the instruments, the sampling, the quantity you
would compute, and the size of the effect you must resolve. A specification that
could not be executed is a failed answer.

**★★★8.** The lesson measures a maximum linear-versus-curved discrepancy of
$3.081\ \mathrm{kg\,m^{-3}}$ over $T \in [0,30]\ ^\circ$C,
$S \in [33,37]\ \mathrm{g\,kg^{-1}}$. (a) Derive the largest discrepancy
analytically from $\tfrac12\Delta_\alpha\Delta T^{2}$ and check it against the
measured value. (b) State the largest $|\Delta T|$ for which the linear equation
of state is good to $0.01\ \mathrm{kg\,m^{-3}}$ given this $\Delta_\alpha$.
(c) Explain why the cabbeling result of the lesson is a *structural* result even
though its magnitude is not transferable.
