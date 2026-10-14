# Exercises — 13-01-02 Rheology: Elastic, Viscous, Plastic and Power-Law Creep

Attempt these before reading the
[solutions](./02-rheology-of-earth-solutions.md). The lesson is
[02 Rheology](../02-rheology-of-earth.md). All flow laws are **SYNTHETIC**
teaching laws with the constants given in the lesson; $R = 8.314\
\mathrm{J\,mol^{-1}\,K^{-1}}$ and $g = 9.81\ \mathrm{m\,s^{-2}}$ are standard.

## ★ Foundational

**★1.** For $\eta = 5\times10^{20}\ \mathrm{Pa\,s}$ and
$\mu = 70\ \mathrm{GPa}$, compute the Maxwell relaxation time in years and the
Deborah number at an observation time of 1 Myr. State in one sentence what the
result means physically.

**★2.** Using the SYNTHETIC olivine-like law ($n = 3.5$,
$E = 350\ \mathrm{kJ\,mol^{-1}}$, $A = 2\times10^{-28}\ \mathrm{Pa^{-n}\,s^{-1}}$),
compute $\eta_{\text{eff}}$ at $\sigma = 50\ \mathrm{MPa}$ and $T = 1600$ K.

**★3.** Compute the brittle strength at 15 km depth for
$\mu_f = 0.60$, $\lambda_p = 0.40$, $\rho = 2750\ \mathrm{kg\,m^{-3}}$. State the
unit and explain in one sentence why $\lambda_p$ reduces the strength.

## ★★ Applied

**★★4.** The lesson's table gives brittle–ductile transition depths of 21.63 km
(crust) and 69.45 km (mantle) at 10 K/km, and 11.76 km and 37.28 km at 20 K/km.
Estimate the transition depths at 15 K/km, state the assumption you used, and say
whether the interpolation is likely to be accurate.

**★★5.** **(a)** A flow law has $n = 3.5$. State the log–log slope of
$\eta_{\text{eff}}$ against stress and against strain rate, and compute both
numbers. **(b)** A shear zone $5\ \mathrm{km}$ thick and another
$50\ \mathrm{km}$ thick both accommodate $30\ \mathrm{mm\,yr^{-1}}$ of
relative motion. Using the strain-rate-controlled form
$\eta_{\text{eff}} = \eta_0(\dot\varepsilon/\dot\varepsilon_0)^{(1-n)/n}$
with $n = 3.5$ and $\eta_0 = 10^{21}\ \mathrm{Pa\,s}$ at
$\dot\varepsilon_0 = 10^{-14}\ \mathrm{s^{-1}}$, compute the effective
viscosity and the shear stress in each zone, and state which zone is *weaker*
and which carries the *larger stress*. Explain the apparent paradox in one
sentence.

**★★6.** A postseismic time series shows a stress step 50% relaxed after 5 years.
Using the Maxwell model, compute the viscosity responsible. State one reason the
answer could be wrong by an order of magnitude.

## ★★★ Research-oriented

**★★★7.** Design a laboratory experiment that would resolve $A$, $n$ and $E$
simultaneously. State the stress range, the temperature range, the number of
experiments, the noise model and the metric by which you would judge the
parameters resolved. Explain why $A$ and $E$ will always be strongly correlated.

**★★★8.** A numerical convection code uses a temperature- and stress-dependent
viscosity. Explain why $\eta_{\text{eff}}$ must be re-evaluated at every
nonlinear iteration rather than once at the start, and describe the failure mode
that appears if it is not.

**★★★9.** The lesson claims that "a single number called the viscosity of the
mantle does not exist". Write 150–250 words making that claim precise: state what
*is* well defined, what quantities it depends on, and one observational
consequence of the dependence.
