# Exercises — 14-05-03 Assimilating Geophysical Data into Hydrological Models

Attempt these before reading the
[solutions](./03-geophysical-data-assimilation-hydrology-solutions.md). The
lesson is [03 Data Assimilation](../03-geophysical-data-assimilation-hydrology.md).
All models are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** Derive the systematic error in an ERT water-content estimate when the
cementation exponent is assumed to be $m_{\text{asm}}$ while the true value is
$m_{\text{true}}$, starting from $\rho/\rho_w = \phi^{-m}S^{-n}$ with
$S = \theta/\phi$. Show that the error is multiplicative in $\theta$.

**★2.** For $\phi = 0.40$, $m_{\text{true}} = 1.80$, $m_{\text{asm}} = 1.60$ and
$n = 2.00$, compute the ratio $\theta_{\text{obs}}/\theta$ and the bias at
$\theta = 0.10$ and $\theta = 0.30\ \mathrm{m^3\,m^{-3}}$.

**★3.** A scalar ensemble forecast has mean 0.150 and sd
$0.025\ \mathrm{m^3\,m^{-3}}$; an observation with sd $0.012$ reads 0.180.
Compute the Kalman gain, the analysis mean and the analysis sd.

## ★★ Applied

**★★4.** Using the same forecast as ★3, suppose the observation operator has a
multiplicative bias of $-9\%$ (the value it reports is $0.91$ times the truth
while the state is $0.180$ *after* the operator, i.e. the true state is
$0.180/0.91 = 0.198$). Compute the analysis mean the filter produces and the
error it will report; compare both with the unbiased answer to ★3. State the
sign of both errors.

**★★5.** In the demonstration the innovation mean is $-0.00811\
\mathrm{m^3\,m^{-3}}$ with an innovation sd of about 0.012 over 75 updates.
Compute the standard error of the mean and the number of standard errors. Repeat
for a study with only 10 updates, and state the practical consequence.

**★★6.** The demonstration's spread-to-error ratio is 1.883 in the unbiased case
and 0.785 in the biased case. Interpret both: which is a *safe* error, which is
*dangerous*, and what would you change in the filter in each case?

## ★★★ Research-oriented

**★★★7.** Design a calibration experiment for the petrophysical observation
operator that would have removed the bias in the demonstration. State the
measurement, its required accuracy, the spatial and temporal sampling, and the
residual error you would expect to remain. Quantify the effect on the analysis
RMSE using the demonstration's numbers as the starting point.

**★★★8.** The demonstration's 5-day forecast RMSE rises from 0.00519 to
0.01564 m³ m⁻³ when the rainfall forcing is 15% low, while the analysis RMSE
barely moves. Write a one-page verification protocol for an operational
assimilation system that would detect such a structural error before it matters,
naming the statistics, the frequency and the threshold at which you would act.
