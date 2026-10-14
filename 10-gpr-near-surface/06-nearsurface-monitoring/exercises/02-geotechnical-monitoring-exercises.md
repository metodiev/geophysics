# Exercises — 10-06-02 Monitoring Dams, Embankments and Foundations

Attempt these before reading the
[solutions](./02-geotechnical-monitoring-solutions.md). The lesson is
[02 Monitoring Dams, Embankments and Foundations](../02-geotechnical-monitoring.md).
All models are **SYNTHETIC** teaching values; reference numbers come from
`code/geotechnical_monitoring_demo.py`. Unless stated otherwise, use the
line-electrode (2-D) conventions of the lesson: current per unit electrode length
and $\rho_a = \pi\,\Delta V/(2I\ln 2)$.

## ★ Foundational

**★1.** A line-electrode Wenner array has $a = 4\ \mathrm{m}$ and injects
$I = 0.05\ \mathrm{A\,m^{-1}}$ into a homogeneous half-space of
$\rho = 50\ \Omega\,\mathrm{m}$. Compute $\Delta V$, the transfer resistance, and
$\rho_a$. State why $\rho_a$ must come out equal to $50\ \Omega\,\mathrm{m}$.

**★2.** From the measured depth table ($-29.14\%$ at $1\ \mathrm{m}$, $-14.66\%$
at $2\ \mathrm{m}$, $-7.16\%$ at $3\ \mathrm{m}$ front depth, spacing
$2\ \mathrm{m}$), compute the ratio of the anomaly between successive metres and
state the rule of thumb it supports.

**★3.** State in two sentences what an ERT monitoring array measures and what an
engineer's question about the same asset is. Do not claim that they are the same.

## ★★ Applied

**★★4.** A front at $2\ \mathrm{m}$ produces a $-14.66\%$ change in $\rho_a$ at a
$2\ \mathrm{m}$ spacing. Convert it to a relative conductivity change under a
uniform-change assumption, then to a relative water-content change with
$m = 1.5$ and fixed $\sigma_w$. State the two largest assumptions.

**★★5.** A permanent array gives 400 quadrupoles per epoch with a $1\%$
one-sigma error. Compute (a) the expected number of measurements exceeding
$2\sigma$ under the null hypothesis, (b) the family-wise false-alarm probability,
(c) the Bonferroni-corrected threshold, and (d) its amplitude penalty.

**★★6.** The same wetting front is monitored with spacings of $2$ and $8\
\mathrm{m}$. Using the measured tables for a front at $3$–$4\ \mathrm{m}$ depth,
state which spacing you would deploy and why, and the anomaly you expect.

## ★★★ Research-oriented

**★★★7.** Design a permanent monitoring array for a $6\ \mathrm{m}$ high
embankment whose target is a wetting front at $2$–$4\ \mathrm{m}$ depth. State the
electrode spacing and layout, the expected anomaly, the detection threshold with
its multiplicity correction, the coupling-drift controls, and the falsification
test. A specification that could not be executed is a failed answer.

**★★★8.** A single quadrupole shows a $-15\%$ change while its neighbours are
within $\pm 1\%$. Specify the sequence of tests that decides whether this is
hardware, a localised real change, or a statistical fluctuation, and give the
expected outcome of each test.
