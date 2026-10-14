# Exercises — 07-05-05 Applications: Groundwater Depletion, Ice Loss, Sea Level

Attempt these before reading the
[solutions](./05-grace-applications-solutions.md). The lesson is
[05 Applications](../05-grace-applications.md). **All models and data in this
module are SYNTHETIC**; the basins, trends, noise and corrections are teaching
values.

Constants: $\rho_w = 1000\ \mathrm{kg\,m^{-3}}$,
$R = 6371\ \mathrm{km}$ (rounded; mean Earth radius in the notation of this
module), ocean fraction $0.708$ (stated), so
$A_{\text{ocean}} = 3.6113\times10^{14}\ \mathrm{m^{2}}$.

## ★ Foundational

**★1.** A synthetic basin of $2\times10^{5}\ \mathrm{km^{2}}$ loses
$4.0\ \mathrm{cm\,yr^{-1}}$ of equivalent water. Compute the mass loss rate in
$\mathrm{kg\,yr^{-1}}$ and the global sea-level equivalent in
$\mathrm{mm\,yr^{-1}}$.

**★2.** The demonstration's plain linear fit returns
$-1.072\ \mathrm{cm\,yr^{-1}}$ for a truth of $-1.000\ \mathrm{cm\,yr^{-1}}$.
State the sign and size of the bias, and explain in two sentences why omitting a
seasonal term produces a *bias* rather than extra noise.

**★3.** A trend is fitted as $b = -1.20 \pm 0.30\ \mathrm{cm\,yr^{-1}}$. Is a
zero trend excluded at $3\sigma$? State what the answer would be for
$\pm 0.45\ \mathrm{cm\,yr^{-1}}$ instead.

## ★★ Applied

**★★4.** A record gives $b = -1.20 \pm 0.30\ \mathrm{cm\,yr^{-1}}$ before
corrections. A solid-Earth correction of $+0.40 \pm 0.20\ \mathrm{cm\,yr^{-1}}$
and a leakage contribution of $-0.05 \pm 0.02\ \mathrm{cm\,yr^{-1}}$ must be
applied. Report the corrected rate with its uncertainty (combine in quadrature)
and state which term dominates the final error.

**★★5.** A basin of $10^{6}\ \mathrm{km^{2}}$ has a measured trend of
$-2.0 \pm 0.5\ \mathrm{cm\,yr^{-1}}$ and a solid-Earth correction uncertain by
$50\%$ of a nominal $+0.8\ \mathrm{cm\,yr^{-1}}$. Compute the corrected trend and
error, and state whether improving the correction or extending the record would
reduce the final uncertainty more.

**★★6.** The demonstration measured trend standard errors of
$0.563\ \mathrm{cm\,yr^{-1}}$ at two years and $0.035\ \mathrm{cm\,yr^{-1}}$ at
ten. Given the $T^{-3/2}$ scaling, predict the error at four years and at twenty
years, and state one reason the prediction for twenty years is optimistic.

## ★★★ Research-oriented

**★★★7.** Design a study that tests a water-budget partition using the *spatial
pattern* of mass change rather than the total. Specify the truth model, the
forward model, the observation operator (including the filter), the noise, the
diagnostic, and the alternative hypothesis you would be able to reject. State
what you could not distinguish even if the diagnostic passes.

**★★★8.** The demonstration's month-to-month noise is drawn independently, but
real gravity solutions have strongly correlated errors, largest at low degree.
Design a synthetic experiment that measures the effect of this correlation on a
reported basin trend's error bar, and state the direction of the effect you
expect and why.
