# Exercises — 22-03-05 Automated Quality Control and Flagging

Attempt these before reading the
[solutions](./05-data-quality-control-solutions.md). The lesson is
[05 Automated Quality Control and Flagging](../05-data-quality-control.md). All
numbers refer to the **SYNTHETIC** model of `code/data_quality_control_demo.py`:
2000 samples at 1 Hz, unit variance, scenarios of 12 spikes at $12\sigma$ and 100
spikes at $4\sigma$, 5 % and 30 % missing.

## ★ Foundational

**★1.** State the two error types a flagging rule can make, and for a geophysical
archive give one concrete cost of each.

**★2.** For a two-sided $3\sigma$ rule on Gaussian noise: (a) compute the
false-positive probability; (b) compute the expected number of false positives in a
2000-sample record; (c) state what the budget becomes at $2\sigma$.

**★3.** Write the robust rule of the lesson, explain the factor 1.4826, and state which
two statistics it uses.

## ★★ Applied

**★★4.** Read the demonstration's confusion matrices and answer: (a) for the 12
spikes at $12\sigma$, state the precision and recall of the naive and the robust rule;
(b) for the 100 spikes at $4\sigma$, do the same and state which rule you would use;
(c) explain in two sentences why the naive rule's precision is 1.000 in the second
scenario while its recall is 0.470.

**★★5.** The demonstration measures the threshold stability: 2.933 (clean), 4.094
(12 spikes at $12\sigma$) and 4.041 (100 spikes at $4\sigma$) for the naive rule,
against 2.924, 2.927 and 3.222 for the robust rule.

(a) Compute the ratios to the clean value for each rule. (b) Explain quantitatively
why a single $12\sigma$ value in 2000 samples raises the standard deviation by the
amount implied here. (c) State the consequence for a paper that reports "we flag at
$3\sigma$" without saying how the scale was estimated.

**★★6.** A record is 30 % missing and the gaps are filled with zeros.

(a) State the measured effect on the standard deviation and the number of fake zeros.
(b) Compute the direction and rough size of the resulting bias in the mean, and compare
it with the measured values ($+0.02781$ with NaN, $+0.02065$ with zeros).
(c) State the two representational changes that remove the problem.

## ★★★ Research-oriented

**★★★7.** Design a QC procedure for a 40-station accelerometer network, stating the
rule sequence, the scale estimator per rule, the confusion-matrix evaluation plan, the
flag vocabulary, the storage of raw and flagged values, and the audit trail. State the
one rule decision that cannot be automated and how you would present it to a user.

**★★★8.** The lesson's confusion matrices use injected spikes as ground truth. Design a
labelling scheme for a real record that does not inject anything: state the evidence
used to label a sample as bad, the inter-analyst agreement you would require, and the
two ways the labels could be biased in favour of the rule being tested. State what the
evaluation cannot establish.

**★★★9.** Correlated noise reduces the effective sample size
([20-05-01](../../../20-signal-processing/05-noise-and-random-signals/01-stochastic-processes.md)).
Derive or measure how the sampling error of an MAD-based scale estimate depends on the
effective sample size, and state the practical consequence for a station whose record
is dominated by long-period noise. State what you would measure before quoting a
threshold for that station.
