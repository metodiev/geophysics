# Exercises — 08-02-05 Airborne Magnetic Surveys and Compensation

Attempt these before reading the
[solutions](./05-airborne-magnetic-surveys-solutions.md). The lesson is
[05 Airborne Magnetic Surveys and Compensation](../05-airborne-magnetic-surveys.md).
All aircraft, target and survey parameters are **SYNTHETIC** teaching values.

Use $\mu_0 = 4\pi\times10^{-7}\ \mathrm{H\,m^{-1}}$.

## ★ Foundational

**★1.** Write the permanent, induced and eddy interference terms and state how
many coefficients each needs.

**★2.** A dipole body with moment $m = 800\ \mathrm{A\,m^2}$ lies $25\
\mathrm{m}$ below the surface. Compute the anomaly at the surface and at $50\
\mathrm{m}$ altitude, and the fraction retained.

**★3.** For a target wavelength of $250\ \mathrm{m}$, compute the line spacing
under the quarter-wavelength rule and the minimum spacing that satisfies the
Nyquist condition.

## ★★ Applied

**★★4.** A compensation fit on an aircraft manoeuvre gives residuals of
$2.10\ \mathrm{nT}$ (3 coefficients), $0.41\ \mathrm{nT}$ (9) and
$0.39\ \mathrm{nT}$ (18), with a sensor noise floor of $0.35\ \mathrm{nT}$. State
which model you would adopt and why.

**★★5.** The permanent coefficients of an aircraft change by 25% between flights.
If the uncompensated interference had an rms of $4.0\ \mathrm{nT}$ and was
attributable entirely to the permanent terms, estimate the residual left by a
stale solution, and state one processing consequence.

**★★6.** A survey is flown at $80\ \mathrm{m}$ altitude with a $350\
\mathrm{m}$ shortest target wavelength. Compute (a) the line spacing under the
quarter-wavelength rule, (b) the along-line sample interval under the same rule,
and (c) the retention of a wavelength-700 m anomaly by the spacing you chose in
(a).

## ★★★ Research-oriented

**★★★7.** Design a compensation experiment for an aircraft whose interference is
believed to include a large field-dependent (nonlinear) term. State the manoeuvres,
the model you will fit, the model you will compare it against, the metric, and the
cruise flight that would falsify the linear model. A specification that could not
be executed is a failed answer.

**★★★8.** Derive the altitude dependence of the anomaly of a dipole at depth $d$
observed at height $h$, and show that the *apparent* depth recovered from an
inversion that assumes $h = 0$ is $d + h$ only for the on-axis field. Then explain
why a varying drape across a survey area imposes an apparent gradient, and how
that is distinguished from a geological gradient (state the test).
