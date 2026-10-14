# Exercises — 07-05-04 Mass Concentration Solutions, Leakage and Filtering

Attempt these before reading the
[solutions](./04-mascons-and-leakage-solutions.md). The lesson is
[04 Mass Concentration Solutions, Leakage and Filtering](../04-mascons-and-leakage.md).
**All models and data in this module are SYNTHETIC.**

Constants from the demonstration: $R = 6371\ \mathrm{km}$,
$\rho_w = 1000\ \mathrm{kg\,m^{-3}}$, $\rho_e = 5513.4\ \mathrm{kg\,m^{-3}}$,
$F = \pi R / L = 500\ \mathrm{km}$ at $L = 40$, filter kernel
$W_l = \exp\!\left(-\dfrac{l(l+1)\sigma^{2}}{2R^{2}}\right)$.

## ★ Foundational

**★1.** Compute the mass contained in a disc of radius $200\ \mathrm{km}$ and
$25\ \mathrm{cm}$ of water-equivalent thickness, and its contribution to the
global mean water-equivalent height.

**★2.** Evaluate the Gaussian kernel $W_l$ at $l = 5$, $15$ and $30$ for
$\sigma = 250\ \mathrm{km}$, and state what each value means for a coefficient of
that degree.

**★3.** State, in one sentence each, what a spherical-harmonic solution assumes
about the mass field and what a mascon solution assumes.

## ★★ Applied

**★★4.** The demonstration measures a $-34.2\%$ bias for a $300\ \mathrm{km}$ cap
at $L = 40$ and $+1.0\%$ for a $1200\ \mathrm{km}$ cap. Explain, with the
resolution scale $F$, why the sign changes, and state the region-size rule of
thumb the numbers support.

**★★5.** Using the demonstration's leakage table (annulus $400$–$700\ \mathrm{km}$:
$4.560\ \mathrm{cm}$ at $\sigma = 0$, $5.501\ \mathrm{cm}$ at
$\sigma = 400\ \mathrm{km}$, $2.817$ at $1600\ \mathrm{km}$, against a
$2.00\ \mathrm{cm}$ background), compute the excess at each width and state which
width minimises the leakage into that annulus.

**★★6.** Two identical $300\ \mathrm{km}$ discs sit $1443\ \mathrm{km}$ apart. The
contamination of one cap by the other is $+0.710\ \mathrm{cm}$ at
$\sigma = 0$, $+0.121\ \mathrm{cm}$ at $\sigma = 400\ \mathrm{km}$ and
$+0.402\ \mathrm{cm}$ at $\sigma = 1600\ \mathrm{km}$. Explain both the rise at
small $\sigma$ and the rise at large $\sigma$, and state what "matched filter"
means here.

## ★★★ Research-oriented

**★★★7.** Design a numerical experiment that measures the leakage of a synthetic
disc anomaly into the coefficients used to report a *neighbouring* region.
Specify the truth, the forward model, the observation operator, the filter, the
metric and the prediction.

**★★★8.** The demonstration's forward model is linear and verified to
$1.7\times10^{-9}$. Explain why the non-uniqueness of the inversion is therefore
not a numerical artefact, and state where the ambiguity actually resides.
