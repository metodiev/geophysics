# Exercises — 15-05-03 Coastal Aquifers and Submarine Groundwater Discharge

Attempt these before the
[solutions](./03-coastal-aquifers-marine-solutions.md). The lesson is
[03 Coastal Aquifers and Submarine Groundwater Discharge](../03-coastal-aquifers-marine.md).
All models and data are **SYNTHETIC** teaching values; the model constants are
those printed by `code/coastal_aquifers_marine_demo.py`.

## ★ Foundational

**★1.** With $\rho_f=1000$ and $\rho_s=1024\ \mathrm{kg\,m^{-3}}$, compute the
Ghyben–Herzberg factor and the interface depth for a fresh head of
$1.5\ \mathrm{m}$ above sea level.

**★2.** For a strip island of width 2 km with a recharge of $0.8\
\mathrm{m\,yr^{-1}}$, $K=20\ \mathrm{m\,day^{-1}}$ and $\Delta\rho=24\
\mathrm{kg\,m^{-3}}$, compute $h(0)$, the interface depth at the centre and the
lens thickness. Convert both $w$ and $K$ to $\mathrm{m\,s^{-1}}$ first and show
those conversions.

**★3.** Compute the bulk resistivity of a clean sand with $\phi=0.30$, $m=2.0$
and a pore fluid of $10\ \mathrm{g\,kg^{-1}}$ salinity, using
$\sigma_f=0.114S\ \mathrm{S\,m^{-1}\,(g\,kg^{-1})^{-1}}$.

## ★★ Applied

**★★4.** An interface lies at 60 m below sea level and a well is screened 30 m
above it. Compute the maximum drawdown before upconing reaches the screen, then
the pumping rate it corresponds to, with $T=0.02\ \mathrm{m^2\,s^{-1}}$ and
$\ln(R/r_w)=7.5$. Give the answer in $\mathrm{m^3\,day^{-1}}$.

**★★5.** Compute the tidal decay length for $T=0.01\ \mathrm{m^2\,s^{-1}}$,
$S=0.1$ and the principal lunar semidiurnal tide (period 12.42 h). State how far
inland the tidal pore-pressure signal is still 37% of its beachface amplitude.

**★★6.** A lens has a volume of $5\times10^{5}\ \mathrm{m^3}$ per metre of
shoreline and a recharge of $4000\ \mathrm{m^3\,yr^{-1}}$ per metre. Compute the
residence time, then state what it becomes if the island width doubles with the
recharge rate and $K$ unchanged.

## ★★★ Research-oriented

**★★★7.** An island 3 km wide supports a lens whose interface is at 40 m. Design
the survey that maps the interface and the recharge: specify the land ERT
(arrays, spacings, target depths), the marine or towed EM component, the
borehole/water-level observations, and for each the measured quantity and the
modelled quantity. State the two model assumptions that would most bias the
salinity map and the one measurement that would test each.

**★★★8.** An SGD study measures a total discharge of $1.0\times10^{4}\
\mathrm{m^3\,yr^{-1}}$ per metre of shoreline with a radon budget, and a fresh
component of $2000\ \mathrm{m^3\,yr^{-1}}$ per metre from a water balance.
**(a)** Compute the recirculated fraction. **(b)** State what each estimate
measures and which is more uncertain. **(c)** Design the measurement that would
separate a genuinely larger fresh discharge from a larger recirculation, and
state the quantity that neither measurement constrains.
