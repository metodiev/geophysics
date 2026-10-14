# Exercises — 07-01-04 Gravity Reductions: Free-Air, Bouguer, Isostatic and Terrain

Attempt these before reading the
[solutions](./04-gravity-reduction-solutions.md). The lesson is
[04 Gravity Reductions](../04-gravity-reduction.md). All models are
**SYNTHETIC** teaching values. Use $G = 6.67430\times10^{-11}\
\mathrm{m^{3}\,kg^{-1}\,s^{-2}}$, $1\ \mathrm{mGal} = 10^{-5}\
\mathrm{m\,s^{-2}}$, and the measured lesson values where they apply:
free-air coefficient $0.308555\ \mathrm{mGal\,m^{-1}}$ at $45^\circ$,
slab coefficient $0.111969\ \mathrm{mGal\,m^{-1}}$ for
$\rho = 2670\ \mathrm{kg\,m^{-3}}$, and normal gravity from the closed-form
values quoted in the questions.

## ★ Foundational

**★1.** Compute the free-air correction for elevations of $250\ \mathrm{m}$,
$1500\ \mathrm{m}$ and $4000\ \mathrm{m}$ using the $45^\circ$ coefficient, and
express each as a fraction of $1\ \mathrm{mGal}$.

**★2.** Compute the simple Bouguer slab correction at $1500\ \mathrm{m}$ for
$\rho = 2200$, $2670$ and $3000\ \mathrm{kg\,m^{-3}}$. State the difference in
mGal between the extreme densities and what fraction of the free-air term that is.

**★3.** For a uniform-density surface at $45^\circ$, compute the three gradients:
observed $g$ versus elevation, free-air anomaly versus elevation, and simple
Bouguer anomaly versus elevation. State in one sentence why the third is zero.

## ★★ Applied

**★★4.** A SYNTHETIC hill is a flat-topped cylinder of height $H = 100\
\mathrm{m}$ and radius $R = 500\ \mathrm{m}$ with $\rho = 2400\
\mathrm{kg\,m^{-3}}$. Compute the terrain correction for (a) a station at the
centre of its top and (b) a station on the floor of the equivalent cylindrical
valley of the same depth and radius. Explain the factor between the two answers.

**★★5.** A SYNTHETIC station at $50^\circ$ latitude has elevation
$2200\ \mathrm{m}$, reading $980\,651.000\ \mathrm{mGal}$,
$\gamma(50^\circ) = 981\,070.2136\ \mathrm{mGal}$, free-air coefficient
$0.3085175\ \mathrm{mGal\,m^{-1}}$ and Bouguer density $2600\
\mathrm{kg\,m^{-3}}$. Compute the complete Bouguer anomaly, then recompute it with
$h = 2210\ \mathrm{m}$ (a 10 m surveying error) and with $\rho = 2300\
\mathrm{kg\,m^{-3}}$.

**★★6.** In the lesson's Nettleton experiment the uncorrelated case recovered
$2775\ \mathrm{kg\,m^{-3}}$ against a truth of $2750$, while the correlated case
recovered $2875$. For each case, compute the anomaly error at an elevation of
$600\ \mathrm{m}$ caused by the density error alone, and state which case would be
dangerous for an interpretation and why.

## ★★★ Research-oriented

**★★★7.** Design a survey specification that guarantees the Bouguer correction is
accurate to $0.05\ \mathrm{mGal}$ from the finite extent of the terrain, given a
station height $h$. State how you would choose the terrain-model radius, how you
would test the choice, and what the answer depends on besides $h$.

**★★★8.** Construct a full error budget for a SYNTHETIC $200$-station survey with
$500\ \mathrm{m}$ of relief, giving each input an uncertainty (elevation,
position, density, terrain model, instrument repeatability). Propagate them into
the anomaly, state which dominates, and identify the design change that would
reduce the total uncertainty the most per unit cost.

**★★★9.** Explain why the *isostatic* anomaly is logically different from the
Bouguer anomaly, and design a test that would reveal whether an isostatic
reduction used the correct compensation model. State what would falsify your test.
