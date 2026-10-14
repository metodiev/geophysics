# Exercises — 10-06-03 Monitoring Contaminant Transport with Geophysics

Attempt these before reading the
[solutions](./03-contaminant-monitoring-solutions.md). The lesson is
[03 Monitoring Contaminant Transport](../03-contaminant-monitoring.md). All models
are **SYNTHETIC** teaching values; reference numbers come from
`code/contaminant_monitoring_demo.py`. Use $z_{0.95} = 1.6449$ for one-sided 95%
confidence.

## ★ Foundational

**★1.** An aquifer has a Darcy flux $q = 0.15\ \mathrm{m/day}$ and an effective
porosity $n_e = 0.25$. Compute the pore velocity, the arrival time at a monitoring
point $20\ \mathrm{m}$ downstream, and the dispersion coefficient for
$\alpha_L = 1.0\ \mathrm{m}$.

**★2.** From the measured aliasing table, state the survey interval that retains
90% of the plume peak, the interval that halves it, and the interval at which the
peak is essentially missed.

**★3.** State in three sentences why a conductivity change caused by a plume is
not a concentration measurement, and name the two measurements that make it one.

## ★★ Applied

**★★4.** A plume produces a conductivity rise of $20\ \mathrm{mS\,m^{-1}}$ at the
monitoring point, with a measurement noise of $2\ \mathrm{mS\,m^{-1}}$. Compute the
detection power at a $2\sigma$ threshold, and the smallest rise the survey could
claim to have detected with 95% probability.

**★★5.** Quantify the error in the inferred concentration produced by (a) a 25%
calibration error (both signs) and (b) a $2\ \mathrm{mS\,m^{-1}}$ background error,
for the $20\ \mathrm{mS\,m^{-1}}$ rise of ★4. Which error dominates, and does the
answer change for a $120\ \mathrm{mS\,m^{-1}}$ rise?

**★★6.** Using the pulse physics of the demonstration (peak at
$13.40$ days, passage of $12.3$ days for a five-day release), specify the survey
interval you would use and the fraction of the peak you expect to capture. State
the systematic error this leaves in any reported concentration.

## ★★★ Research-oriented

**★★★7.** Design a monitoring programme for a plume expected to pass a compliance
well over six months. State the survey interval, the geophysical method and its
expected conductivity resolution, the calibration measurements, the detection
claim with its power, the confounders, and the falsification test. A specification
that could not be executed is a failed answer.

**★★★8.** The predicted arrival time is 30 days and the measured conductivity
change appears at 45 days. List the five most likely causes in order of prior
probability, and state the measurement that tests each one.
