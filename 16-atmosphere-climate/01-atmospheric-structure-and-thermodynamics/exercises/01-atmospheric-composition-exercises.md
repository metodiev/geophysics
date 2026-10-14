# Exercises — 16-01-01 Atmospheric Composition and Vertical Structure

Attempt these before reading the
[solutions](./01-atmospheric-composition-solutions.md). The lesson is
[01 Atmospheric Composition](../01-atmospheric-composition.md). All models are
**SYNTHETIC** teaching values, and the constants $R^{*} = 8.314462618\
\mathrm{J\,mol^{-1}\,K^{-1}}$ and $g = 9.80665\ \mathrm{m\,s^{-2}}$ are standard.

## ★ Foundational

**★1.** A dry-air sample has mole fractions
$x_{\mathrm{N_2}} = 0.79$, $x_{\mathrm{O_2}} = 0.20$ and
$x_{\mathrm{Ar}} = 0.01$ (a deliberately crude two-plus-one model). Compute the
mean molar mass and $R_d$, and state the units of each intermediate quantity.

**★2.** For that sample compute $c_p$ and $c_v$ using $\gamma = 1.4$ and verify
Mayer's relation. For a $10\ \mathrm{kg}$ parcel, how much energy raises its
temperature by $5\ \mathrm{K}$ at constant pressure?

**★3.** Compute the scale height $H = R_d T/g$ for $T = 250\ \mathrm{K}$ and for
$T = 300\ \mathrm{K}$ using the $R_d$ of ★1, and state the physical meaning of
$H$ in one sentence.

**★4.** Using the isothermal model with $H$ from the $288\ \mathrm{K}$ case,
compute the pressure ratio $p/p_0$ at $z = 2\ \mathrm{km}$ and at
$z = 7\ \mathrm{km}$.

## ★★ Applied

**★★5.** Derive the polytropic solution
$p = p_0(T/T_0)^{g/(R_d\Gamma)}$ from $\mathrm{d}p/\mathrm{d}z = -\rho g$ and the
ideal-gas law, showing both integration steps. Then compute $p/p_0$ at
$5\ \mathrm{km}$ for $\Gamma = 6.5\ \mathrm{K\,km^{-1}}$ and for
$\Gamma = 9.8\ \mathrm{K\,km^{-1}}$ with $T_0 = 288.15\ \mathrm{K}$, and explain
in one sentence which is the drier atmosphere.

**★★6.** In the lesson's model the column mass is $p_0/g$ with
$p_0 = 101325\ \mathrm{Pa}$. An observing site sits at $1500\ \mathrm{m}$ and
records $842\ \mathrm{hPa}$. Compute (a) the column mass above that site,
(b) the ratio to the standard column mass, and (c) how much of the atmospheric
mass lies *below* the site, as a fraction. State the two assumptions.

**★★7.** Derive the virtual temperature relation
$T_v = T\big/\big[1-(e/p)(1-\varepsilon)\big]$ from
$p = \rho_d R_d T + \rho_v R_v T$, and show that it reduces to
$T_v \approx T(1+0.608q)$ for small $q$. Evaluate the density error of ignoring
the moisture correction at $p = 850\ \mathrm{hPa}$, $T = 280\ \mathrm{K}$,
$q = 0.008\ \mathrm{kg\,kg^{-1}}$.

**★★8.** The demonstration reports a root-mean-square molecular speed of
$506.5\ \mathrm{m\,s^{-1}}$ for N₂ at $288.15\ \mathrm{K}$. Compute the same
quantity for water vapour (18.0153 g mol⁻¹) and for CO₂ (44.0095 g mol⁻¹), and
state why the aerosol particles of
[16-02-06](../../02-radiation-and-energy-balance/06-aerosols-and-clouds-radiation.md)
behave completely differently.

## ★★★ Research-oriented

**★★★9.** The lesson claims the isothermal pressure model is wrong by $10.2\%$ at
$8\ \mathrm{km}$. Design a numerical experiment that decides whether the
polytropic model or a *piecewise* profile taken from a synthetic $T(z)$ table is
the better predictor, given that you may generate your own "measured"
$T(z)$ with a stated noise level. Specify: the generator, the metric, the
baseline you compare against, the expected ranking, and the one measurement that
would reverse the ranking. A specification that could not be executed is a
failed answer.

**★★★10.** The total-mass formula $M = p_0 A/g$ is exact given $p_0$ and $A$.
Discuss what "exact" means when $g$ varies with latitude and height by $0.5\%$
and when $p_0$ is a standard value rather than a measurement. Propose an error
budget that separates the *definitional* part from the *physical* part, and state
which term dominates the total uncertainty. Be explicit about what you are
assuming.

**★★★11.** In §3.1 the lesson observes that a $100\ \mathrm{ppm}$ change in CO₂
changes $R_d$ by $5\times10^{-5}$ but changes the radiative balance far more.
Quantify the first claim exactly for a change from 420 to 1000 ppm and state,
in one paragraph, why a quantity that is negligible for the ideal-gas law can be
central elsewhere. Do not invent the radiative numbers; state only what you can
compute or cite as a standard constant.
