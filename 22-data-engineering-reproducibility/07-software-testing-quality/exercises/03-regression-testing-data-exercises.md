# Exercises — 22-07-03 Regression Testing Against Known Results

Attempt these before reading the
[solutions](./03-regression-testing-data-solutions.md). The lesson is
[03 Regression Testing Against Known Results](../03-regression-testing-data.md).
Numbers refer to the measurements and the **SYNTHETIC** pipeline model of
`code/regression_testing_data_demo.py`.

## ★ Foundational

**★1.** State the three obligations a regression test carries, and which of them a
tolerance does not satisfy.

**★2.** A computation's round-off floor is measured at 4e-13 relative.

(a) State the tolerance you would choose and why. (b) Compute the headroom over the floor
and the smallest error the test can still catch. (c) State what you would record next to the
tolerance in the test file.

**★3.** State the eight fields of a recorded golden value and which one prevents it from
being reblessed to whatever the code prints.

## ★★ Applied

**★★4.** A code computes the sample variance of a series with a mean of $5\times10^7$ and a
standard deviation of 2.

(a) State why $\mathbb{E}[x^2] - \mathbb{E}[x]^2$ is a poor choice and at which magnitude
the cancellation appears (work out the magnitude of the two terms). (b) State the two
assertions you would add that a stored value would not provide. (c) State the dtype issue
that makes the formula *unusable* rather than merely inaccurate.

**★★5.** A pipeline has stages with costs (hours): `load` 0.3, `qc` 0.7, `grid` 1.2,
`invert` 5.0, `post` 2.0, `figures` 0.5, `report` 0.2, where `qc` needs `load`, `grid` needs
`qc`, `invert` needs `grid`, `post` needs `invert`, `figures` needs `post`, `report` needs
`figures`.

(a) Compute the total pipeline cost. (b) For each stage, compute the number and cost of the
stages invalidated by a change to it, and the share of the pipeline. (c) State which stage is
the best candidate for a cached, content-addressed key and why.

**★★6.** A team's comparison uses `rtol=1e-14` on a floating-point sum and the suite fails
on a new machine.

(a) State the two possible explanations and the measurement that distinguishes them.
(b) Compute the false-alarm share for legitimate refactors at 1e-14 and at 1e-12 from the
lesson's table, and state the change you would make. (c) State what you would check before
loosening the tolerance, and what loosening it to 1e-3 would stop catching.

## ★★★ Research-oriented

**★★★7.** Design the regression-testing layer for a seismic processing pipeline that
produces migrated images from field data.

State: the golden artefacts (and why each is small), the tolerance and its measured
justification for each, the properties asserted instead of stored values, the cache keys for
each stage, the reblessing process (who approves, what the pull request must say), and the
one class of change the layer cannot detect.

**★★★8.** A group wants to compare their code against a commercial package that provides no
source and changes version twice a year.

Design the comparison procedure: state what can be compared (values, statistics, gradients,
derived quantities), the tolerance measurement you would perform on a fixed case, the
versioning and recording of the reference outputs, the handling of a version change, and the
honest statement to publish. State the two ways the comparison could mislead.

**★★★9.** A reviewer argues that a large reference-output file is fine because "it is the
actual result and we compare it bitwise, so we catch everything".

Analyse the claim with the lesson's numbers: state the false-alarm rate for legitimate
refactors and its consequence for the suite's lifetime, what bitwise comparison genuinely
catches, the three assertions you would add in place of the bytes, and the storage and review
costs of the large file. State the criterion for when bitwise comparison *is* the right
choice.
