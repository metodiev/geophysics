# Exercises — 25-01-01 Project: Units, Conversions and First Scientific Plots

Attempt these before reading the
[solutions](./01-units-and-plotting-solutions.md). The project is
[01 Units and Plotting](../01-units-and-plotting.md). Every value below is a
**SYNTHETIC** teaching number, and the demonstration's printed values are:

| Quantity | Demonstration value |
|---|---|
| g from $GM/R^{2}$ | $9.8203\ \mathrm{m\,s^{-2}}$ |
| free-air gradient | $3.0828\times10^{-6}\ \mathrm{m\,s^{-2}\,m^{-1}}$ = $0.3083\ \mathrm{mGal\,m^{-1}}$ |
| Bouguer slab at $2670\ \mathrm{kg\,m^{-3}}$ | $1.1197\times10^{-6}\ \mathrm{m\,s^{-2}\,m^{-1}}$ = $0.1120\ \mathrm{mGal\,m^{-1}}$ |
| free-air / Bouguer ratio | $2.7533$ |
| anomaly ratio | $33.095$ ppm |
| 2.4 km at 5.80 km/s | $0.4138\ \mathrm{s}$ |
| profile depth mean ± SEM | $2392.6 \pm 5.21\ \mathrm{m}$ |

## ★ Foundational

**★1.** Convert each row to SI and state the factor used: $1.5\ \mathrm{mGal}$;
$2.67\ \mathrm{g\,cm^{-3}}$; $5.80\ \mathrm{km\,s^{-1}}$; $2.4\ \mathrm{km}$;
$48\,000\ \mathrm{nT}$.

**★2.** Compute the free-air gradient in mGal m⁻¹ using
$g = 9.8203\ \mathrm{m\,s^{-2}}$ and $R = 6.371\times10^{6}\ \mathrm{m}$, and
state its unit. Then compute the Bouguer gradient for $\rho = 2900\
\mathrm{kg\,m^{-3}}$.

**★3.** A formula in a report reads $\Delta g = 2\pi G \rho h$, with $\Delta g$ in
m s⁻², $\rho$ in kg m⁻³ and $h$ in m. Check it dimensionally and state whether
the two sides agree.

## ★★ Applied

**★★4.** A gravity station is 250 m higher than the reference station and the
rock density is $2670\ \mathrm{kg\,m^{-3}}$. Using the two gradients of the
demonstration, compute the free-air correction and the Bouguer correction in
mGal, and the combined correction. State the sign of each if the station is
*higher* than the reference.

**★★5.** The demonstration's figure caption must match its axes. For the
120-station profile, (a) compute the horizontal extent in km if the spacing were
doubled to 500 m; (b) compute the standard error of the mean if the profile held
only 30 stations at the same scatter standard deviation of $57.1\ \mathrm{m}$;
(c) state which caption lines change in each case.

**★★6.** A colleague converts $2.67\ \mathrm{g\,cm^{-3}}$ to
$2.67\ \mathrm{kg\,m^{-3}}$ and then computes a Bouguer gradient of
$1.12\times10^{-9}\ \mathrm{m\,s^{-2}\,m^{-1}}$. State the factor they lost, the
correct value, and one sanity check that would have caught it.

## ★★★ Research-oriented

**★★★7.** Design a unit-hygiene procedure for a whole survey: state where the
conversion happens (ingestion, storage, plotting, or reporting), how the unit of
every stored column is recorded, one automated test that fails the pipeline when
a unit is missing, and how the procedure handles a derived column whose unit
follows from two others. A procedure that could not be implemented is a failed
answer.
