# Exercises — 16-08-03 Homogenisation, Bias Adjustment and Uncertainty

Attempt these before reading the
[solutions](./03-climate-data-homogenisation-solutions.md). The lesson is
[03 Homogenisation, Bias Adjustment and Uncertainty](../03-climate-data-homogenisation.md).
All models and numbers are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** A station carries a step of $0.30\ \mathrm{K}$ from year 50 of a 100-year
record. Using $\sum_t(t-\bar t)^{2} = 83{,}325$ and
$\sum_{t\ge50}(t-\bar t) = 1250$, compute the trend the step produces.

**★2.** Explain, in two sentences, why a neighbour-difference series removes the
regional climate signal but not a network-wide instrument change.

**★3.** A delta-change adjustment adds a model's simulated change of
$+2.5\ \mathrm{K}$ to an observed series with mean $12.0\ ^\circ\mathrm{C}$ over
the reference period. State the adjusted future mean, and which property of the
observed series the method preserves.

## ★★ Applied

**★★4.** A neighbour differenced series has mean $0.05\ \mathrm{K}$ and standard
deviation $0.30\ \mathrm{K}$ before a candidate break year, and mean
$0.55\ \mathrm{K}$ and standard deviation $0.28\ \mathrm{K}$ after it, with
$n = 10$ on each side. Compute the split-mean $t$-statistic and state whether it
exceeds a threshold of $3.0$.

**★★5.** The demonstration measures a detection rate of $0.65$ for a
$0.30\ \mathrm{K}$ step. A network has 1000 stations with such a break. Compute
the expected number of undetected steps, and the trend bias each undetected step
imposes (use a step at year 40 of an 80-year record, where
$\sum_{t\ge40}(t-\bar t) = 800$ and $\sum_t(t-\bar t)^2 = 42{,}660$).

**★★6.** A model has historical mean $10.0\ \mathrm{K}$ and future mean
$13.0\ \mathrm{K}$; the observed historical mean is $11.0\ \mathrm{K}$, all with
the same standard deviation. Compute the corrected future mean and the reported change for
(a) a transfer function built on the historical model–observation pair, and
(b) a transfer function that maps the future model onto the historical observed
distribution.

## ★★★ Research-oriented

**★★★7.** Design a calibrated breakpoint detection rule for a network of $N$
stations. Specify the test statistic, how you would obtain a null distribution
that accounts for the scan's multiplicity and the spatial correlation between
stations, and the metric you would use to report the rule's performance.

**★★★8.** A station's record contains a gradual exposure change (a ramp of
$+0.4\ \mathrm{K}$ spread over 25 years) rather than a step. Explain what a
single-break, step-based homogenisation method does to the trend in this record,
and specify an experiment that would measure the resulting error. State the
result that would show step-based homogenisation is adequate despite the ramp.
