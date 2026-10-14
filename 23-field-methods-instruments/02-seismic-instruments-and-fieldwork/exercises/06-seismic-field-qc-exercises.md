# Exercises — 23-02-06 Field QC: Noise Checks, Continuity, Station Uptime

Attempt these before reading the
[solutions](./06-seismic-field-qc-solutions.md). The lesson is
[06 Field QC](../06-seismic-field-qc.md). All values are **SYNTHETIC**.

## ★ Foundational

**★1.** A station loses 4 gaps of 3 hours each during a 45-day deployment. Compute
its uptime, and state the expected number of samples lost at 100 sps.

**★2.** A network's MTBF is 30 days and its MTTR is 4 hours. Compute the
availability and the annual downtime in hours. Then compute the availability if
the MTTR is halved, and state which intervention is the cheaper lever.

## ★★ Applied

**★★3.** A noise QC population contains 40 stations. A one-sided threshold is
expected to flag 5 % of a Gaussian population by chance. Compute the expected
number of false positives. If the observed number of flagged stations is 12, state
what you would conclude and what check you would run before naming any station as
faulty.

**★★4.** A station's band-limited rms is $1.0\times10^{-6}\ \mathrm{m/s}$, while
an independent estimate of the true ground noise at the site — from a co-located
reference sensor — is $2.5\times10^{-6}\ \mathrm{m/s}$. Compute the ratio in dB. A
ground-coupling resonance with damping $h_c = 0.5$ at frequency $f_c$ is one
candidate explanation: find the $f_c$ that produces this deficit at 10 Hz. State
one other cause of a frequency-independent amplitude factor, and say what you would
do about the station.

## ★★★ Research-oriented

**★★★5.** Design a daily QC loop for a 25-station, 60-day aftershock deployment:
state the tests, the order, the thresholds and how each threshold was chosen, the
time budget per day, the actions the loop can trigger, and the three failure classes
it cannot detect. A specification that could not be executed by a two-person field
team is a failed answer.

**★★★6.** Specify a study that measures the effect of station outages on the
network's magnitude of completeness: state the data you would use, the estimator,
the metric, the control for the operating configuration, and two confounding
effects. A specification that could not be executed is a failed answer.
