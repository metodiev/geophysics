# Exercises — 16-04-01 Components of the Climate System and Their Timescales

Attempt these before reading the
[solutions](./01-climate-system-components-solutions.md). The lesson is
[01 Components of the Climate System and Their Timescales](../01-climate-system-components.md).
All models are **SYNTHETIC** teaching values. Use
$\rho_w = 1025\ \mathrm{kg\,m^{-3}}$, $c_{p,w} = 3985\ \mathrm{J\,kg^{-1}K^{-1}}$,
$\sigma = 5.670374419\times10^{-8}\ \mathrm{W\,m^{-2}K^{-4}}$,
$c_p = 1004\ \mathrm{J\,kg^{-1}K^{-1}}$, $p_s = 1.013\times10^5$ Pa,
$g = 9.81\ \mathrm{m\,s^{-2}}$, $T = 288$ K, $L_f = 3.34\times10^5\
\mathrm{J\,kg^{-1}}$, $\rho_i = 917\ \mathrm{kg\,m^{-3}}$.

## ★ Foundational

**★1.** Compute the heat capacity per unit area $C$ of a 300 m ocean layer and
its Planck relaxation time $C/(4\sigma T^3)$. Express $C$ as a multiple of the
atmospheric column's heat capacity.

**★2.** Compute the heat needed to raise a 50 m mixed layer by 0.6 K, and state
the e-folding time for the Planck response to remove it. Give both the energy
and the time with units.

**★3.** Compute $\lambda_0 = 4\sigma T^3$ at $T = 273$ K and at $T = 300$ K, and
state which temperature gives the longer relaxation time for the same
reservoir.

## ★★ Applied

**★★4.** For a two-box ocean, derive the fast quasi-steady surface temperature
$T_m = F/(\lambda+\gamma)$ by holding the deep ocean fixed, and compute the fast
fraction $\lambda/(\lambda+\gamma)$ for $\gamma = 1.0$ and
$\gamma = 0.4\ \mathrm{W\,m^{-2}K^{-1}}$ with $\lambda = 5.418\
\mathrm{W\,m^{-2}K^{-1}}$. Which gives the larger transient warming, and what
happens to the equilibrium temperature in each case?

**★★5.** Show that the two-box system's equilibrium has $T_m = T_d = F/\lambda$
for any $\gamma > 0$, and explain in one sentence why the coupling term must
vanish there.

**★★6.** An ice sheet is 2500 m thick and accumulates at 0.25 m yr⁻¹.
**(a)** Compute its mass-balance timescale.
**(b)** Compute its thermal timescale $H^2/\kappa$ with
$\kappa = k/(\rho_i c_i) = 1.1424\times10^{-6}$ m² s⁻¹.
**(c)** Compute the heat needed to melt 2500 m of ice per unit area and express
it in kelvin of the 50 m mixed layer's heat capacity.

## ★★★ Research-oriented

**★★★7.** The lesson's two-layer model uses a constant $\gamma$. Design a
numerical experiment that tests the sensitivity of the *transient* surface
temperature to $\gamma$ while holding the equilibrium fixed. State the range of
$\gamma$ you would use, the diagnostic you would plot against what abscissa, and
the result that would show that transient response is governed by $\gamma$ and
not by $F$. Say explicitly what assumption of the two-box model your design
cannot test.
