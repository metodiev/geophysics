# Exercises — 10-04-02 Shear-Wave Velocity Modelling and Site Classification

Attempt these before reading the
[solutions](./02-shear-wave-velocity-modelling-solutions.md). The lesson is
[02 Shear-Wave Velocity Modelling and Site Classification](../02-shear-wave-velocity-modelling.md).
All models and data in this module are **SYNTHETIC**: the profiles, densities,
footing, shaking parameters and uncertainties are teaching values. The empirical
relations used (liquefaction screening, modulus reduction, code site-class
boundaries) are attributed and labelled as relations.

## ★ Foundational

**★1.** A three-layer profile: $4\ \mathrm{m}$ at $160\ \mathrm{m\,s^{-1}}$,
$10\ \mathrm{m}$ at $240\ \mathrm{m\,s^{-1}}$, $16\ \mathrm{m}$ at
$420\ \mathrm{m\,s^{-1}}$. Compute $V_{S30}$ and the weight $w_i$ of each layer.
State which layer dominates and by what factor over the smallest weight.

**★2.** For $V_s = 300\ \mathrm{m\,s^{-1}}$ and $\rho = 1900\ \mathrm{kg\,m^{-3}}$,
compute $G_{\max}$ and $E$ for $\nu = 0.35$. State which part of the calculation is
exact and which is an assumption.

**★3.** A $V_{S30}$ of $352\ \mathrm{m\,s^{-1}}$ is reported. Assign the site class
using the code boundaries A $>1500$, B $760$–$1500$, C $360$–$760$, D $180$–$360$,
E $<180\ \mathrm{m\,s^{-1}}$, and state how far the value is from the nearest
boundary and what that implies if the velocity uncertainty is $6\%$.

## ★★ Applied

**★★4.** With $\tau_{\max} = 50\ \mathrm{kPa}$, compute the reference strain
$\gamma_r$ and the operative modulus at $\gamma = 5\times10^{-4}$ for
$V_s = 300\ \mathrm{m\,s^{-1}}$ and $\rho = 1900\ \mathrm{kg\,m^{-3}}$. Then
compute the settlement of a $2\ \mathrm{m}$ square footing at $120\ \mathrm{kPa}$
with (a) $G_{\max}$ and (b) the operative modulus, and give the ratio.

**★★5.** Using the lesson's screening conventions
($CSR = 0.65(\sigma_v/\sigma'_v)(a_{\max}/g)r_d$,
$r_d = 1-0.00765z$), a profile with $\gamma = 18\ \mathrm{kN\,m^{-3}}$ above and
$20\ \mathrm{kN\,m^{-3}}$ below a $3\ \mathrm{m}$ water table, compute $CSR$ at
$3$ and $6\ \mathrm{m}$ for $a_{\max} = 0.25\,g$. State why $CSR$ increases with
depth even though $r_d$ decreases.

**★★6.** A $V_{S30}$ with $8\%$ uncertainty has a central value $20\
\mathrm{m\,s^{-1}}$ above a code class boundary. Using a Gaussian approximation,
compute the probability that the site is classified in the lower class, and state
what an engineer should be told.

## ★★★ Research-oriented

**★★★7.** A site has a soft layer at $18$–$24\ \mathrm{m}$ that a $30\ \mathrm{m}$
profile includes and a $20\ \mathrm{m}$ profile cannot. Quantify the $V_{S30}$
difference for a profile of your construction, state the class consequences, and
design the measurement programme that would settle which profile is correct. A
specification that could not be executed is a failed answer.

**★★★8.** Two profiles have the same $V_{S30}$ of $300\ \mathrm{m\,s^{-1}}$: A is
$10\ \mathrm{m}$ at $180$ over $20\ \mathrm{m}$ at $400$; B is uniform at
$300\ \mathrm{m\,s^{-1}}$. Compute both settlements for a $2\ \mathrm{m}$ square
footing at $150\ \mathrm{kPa}$ using an operative modulus at $\gamma = 10^{-3}$
($\rho = 1900\ \mathrm{kg\,m^{-3}}$, $\tau_{\max} = 50\ \mathrm{kPa}$), and state
what the comparison says about using a single number to describe a site.

**★★★9.** The lesson reports $FS_N = 0.42$ and $FS_V = 0.78$ at $2\ \mathrm{m}$ for
the same layer. Construct the argument you would make to a reviewer that neither
number is "the" factor of safety, and specify the measurements that would reduce
the disagreement to less than a factor of $1.3$. Be quantitative about each
measurement's contribution.
