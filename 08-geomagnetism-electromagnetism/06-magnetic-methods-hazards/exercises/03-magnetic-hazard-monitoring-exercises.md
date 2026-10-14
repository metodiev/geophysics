# Exercises — 08-06-03 Magnetic Monitoring of Volcanoes and Faults

Attempt these before reading the
[solutions](./03-magnetic-hazard-monitoring-solutions.md). The lesson is
[03 Magnetic Hazard Monitoring](../03-magnetic-hazard-monitoring.md). All models
are **SYNTHETIC** teaching values with $\mu_0=4\pi\times10^{-7}\ \mathrm{H\,m^{-1}}$
exact.

## ★ Foundational

**★1.** Compute the moment change implied by a $2\ \mathrm{nT}$ field change at
$800\ \mathrm{m}$ depth. State the equivalent magnetised volume at
$M=1\ \mathrm{A\,m^{-1}}$.

**★2.** Rank the following by standard deviation in a monitoring record: the
secular variation trend ($11\ \mathrm{nT}$), a source transient ($2\ \mathrm{nT}$),
the diurnal variation ($6\ \mathrm{nT}$), instrument drift ($0.3\ \mathrm{nT}$),
noise ($0.5\ \mathrm{nT}$). Which are spatially coherent?

**★3.** A differenced record has single-sample noise of $0.5\ \mathrm{nT}$ per
station. Compute the noise of the difference and state why the detection limit of
an estimator that averages thousands of samples is much smaller.

## ★★ Applied

**★4.** The estimator's scatter is measured as $0.04\ \mathrm{nT}$ over 200 null
realisations. Set a $3\sigma$ threshold, decide whether a $0.3\ \mathrm{nT}$ change
is significant, and state the false-alarm rate you would quote if one null
realisation in 200 exceeded the threshold.

**★5.** A source at $1\ \mathrm{km}$ depth is monitored by a station $2\ \mathrm{km}$
off-axis. Using the geometric factor
$(2d^2-\rho^2)/(\rho^2+d^2)^{5/2}$ relative to its value at $\rho=0$, compute the
reduction and state the sign of the anomaly.

**★6.** A $1\ \mathrm{nT}$ change is observed over 120 days. Compute the trend
accuracy required for the systematic ambiguity to stay below a third of the signal,
and say whether a single reference station can deliver it.

## ★★★ Research-oriented

**★7.** Design a monitoring network for a volcano whose hydrothermal system lies at
$1\ \mathrm{km}$ depth. Specify the station layout, the reference distance, the
sampling rate, the detection threshold, the false-alarm rate you will publish, and
the independent observables you will deploy to attribute a detection to a mechanism.

**★8.** A colleague reports a $0.5\ \mathrm{nT}$ change over 6 months and attributes
it to magma intrusion. Write the three questions you would ask about the analysis
before accepting the claim, and state the one measurement that would most directly
test it.
