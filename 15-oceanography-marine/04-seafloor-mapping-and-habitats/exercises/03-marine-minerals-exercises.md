# Exercises — 15-04-03 Marine Minerals and Deep-Sea Mining Geophysics

Attempt these before the
[solutions](./03-marine-minerals-solutions.md). The lesson is
[03 Marine Minerals and Deep-Sea Mining Geophysics](../03-marine-minerals.md).
All models and data are **SYNTHETIC** teaching values; the model constants are
those printed by `code/marine_minerals_demo.py`.

## ★ Foundational

**★1.** Compute the maximum gravity anomaly of a buried sphere with
$\Delta\rho=800\ \mathrm{kg\,m^{-3}}$, radius $50\ \mathrm{m}$ and depth
$500\ \mathrm{m}$, in both $\mathrm{m\,s^{-2}}$ and mGal.

**★2.** Compute the skin depth in seawater of resistivity
$0.30\ \Omega\,\mathrm{m}$ at 0.5 Hz, and the attenuation in dB through 1500 m of
that water.

**★3.** Compute the wet tonnage for an area of $200\ \mathrm{km^{2}}$ with a mean
nodule abundance of $12\ \mathrm{kg\,m^{-2}}$, and the contained nickel at a grade
of 1.2%.

## ★★ Applied

**★★4.** An experimental variogram gives $\gamma(250\ \mathrm{m})=6.29$,
$\gamma(1000\ \mathrm{m})=13.42$ and $\gamma(4000\ \mathrm{m})=17.89$
$(\mathrm{kg\,m^{-2}})^{2}$. Fit an exponential model: state the sill, then solve
for the nugget and the range using the first two lags. Show the arithmetic and
verify against the third lag.

**★★5.** A kriging study reports a mean kriging standard deviation of
$2.66\ \mathrm{kg\,m^{-2}}$, and a validation against 60 measured cells gives an
RMS error of $5.30\ \mathrm{kg\,m^{-2}}$. Compute the ratio, state whether the
kriging variance is optimistic or conservative, and give the two candidate
explanations that a variogram estimate could provide.

**★★6.** For a coefficient of variation of 0.8 and a target relative error of 15%
at 95% confidence, compute the sample count from
$n=(1.96\,\mathrm{cv}/\varepsilon)^{2}$. Then, using the lesson's measured ratios
of 3.0–8.5 between the true area-mean error and the naive formula, compute the
sample count actually required and state the implication for survey design.

## ★★★ Research-oriented

**★★★7.** A licence area contains a suspected SMS mound, roughly 150 m across, at
1200 m water depth with 20 m of sediment cover. Design the detection programme:
state for each method (multibeam and backscatter, sub-bottom profiling, magnetics,
gravity, deep-towed EM) the anomaly expected, the noise level achievable, the
detection verdict, and the resulting decision. Then state the one measurement that
would confirm a sulphide body rather than an alteration halo, and the false-positive
sources that a conductive anomaly has in this setting.

**★★★8.** A tonnage estimate must be quoted to within a factor of three. Design
the survey: for each of area, abundance, thickness, grade and recovery, state how
you would estimate it, whether it is measured or modelled, and the contribution to
the final range. Explain how the between-area variance of the lesson's §3.4 enters
your design, and state the one number in your final report that is not a
geophysical measurement.
