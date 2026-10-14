# Exercises — 10-05-03 Thermal Methods for Shallow Subsurface Investigation

Attempt these before reading the
[solutions](./03-thermal-nearsurface-solutions.md). The lesson is
[03 Thermal Methods](../03-thermal-nearsurface.md). All models are **SYNTHETIC**
teaching values; reference numbers come from
`code/thermal_nearsurface_demo.py`. Use $\gamma = 0.57722$ and
$P_{\text{year}} = 365.25$ days.

## ★ Foundational

**★1.** Granite has $k = 2.50\ \mathrm{W\,m^{-1}\,K^{-1}}$,
$\rho = 2650\ \mathrm{kg\,m^{-3}}$,
$c = 790\ \mathrm{J\,kg^{-1}\,K^{-1}}$. Compute $\kappa$ and the annual damping
depth $\mu$.

**★2.** At what depth is the daily temperature wave attenuated to 1% of its
surface amplitude in dry soil ($\kappa = 2.50\times10^{-7}\ \mathrm{m^2\,s^{-1}}$)?
State the general expression you used.

**★3.** State the SI units of $k$, $\rho c$, $\kappa$ and $e = \sqrt{k\rho c}$,
and verify by dimensional analysis that $\mu = \sqrt{2\kappa/\omega}$ is a length.

## ★★ Applied

**★★4.** A borehole record gives annual amplitudes of $6.0$ and $2.0\ \mathrm{K}$
at $0.5$ and $2.5\ \mathrm{m}$, and a phase lag of $45$ days. Compute $\kappa$ by
the amplitude-ratio method and by the phase-lag method. State whether the
disagreement is explained by a $0.05\ \mathrm{K}$ sensor error, and what it means.

**★★5.** A needle probe with $q = 1.00\ \mathrm{W\,m^{-1}}$ and
$r = 1.5\ \mathrm{mm}$ gives $T = 0.2412\ \mathrm{K}$ at $50\ \mathrm{s}$ and
$0.3324\ \mathrm{K}$ at $200\ \mathrm{s}$. Compute the slope against $\ln t$, the
conductivity, and the earliest time at which a measurement is within 1% of the
logarithmic approximation.

**★★6.** A $0.05\ \mathrm{K}$ sensor error gives a $5.9\%$ one-sigma diffusivity
uncertainty for the sensor pair of the lesson. How many independent daily cycles
must be averaged to bring the uncertainty to $2\%$, and what assumption about the
noise does that rely on?

## ★★★ Research-oriented

**★★★7.** A geothermal gradient is to be measured in a $30\ \mathrm{m}$ borehole.
Specify the measurement plan that would separate the geothermal flux from the
annual surface wave: the sensor depths, the record length, the model, the metric,
and the falsification test.

**★★★8.** Specify an experiment that would test whether a buried object of
contrasting effusivity can be detected from the surface temperature alone. State
the forcing, the observable, the metric, the strongest confounder, and the
result that would make you abandon the method.
