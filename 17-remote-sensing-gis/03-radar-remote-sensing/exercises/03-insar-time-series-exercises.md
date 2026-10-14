# Exercises — 17-03-03 InSAR Time Series: PS-InSAR and SBAS

Attempt these before reading the
[solutions](./03-insar-time-series-solutions.md). The lesson is
[03 InSAR Time Series](../03-insar-time-series.md). All models are
**SYNTHETIC** teaching values.

Values from the lesson's demonstration: $\lambda = 5.6565\ \mathrm{cm}$,
$\cos 35^\circ = 0.8192$, pair noise $\sigma_\varphi = 0.50\ \mathrm{rad}
= 2.251\ \mathrm{mm}$ of LOS, $1\ \mathrm{rad} = 4.502\ \mathrm{mm}$ of LOS.

## ★ Foundational

**★1.** A network has 30 acquisition dates forming a single connected component.
State the rank of the incidence matrix and the dimension of its null space, and
describe in one sentence what the null vector means physically.

**★2.** Three dates give pair differences $d_{12} = +1.80$ rad,
$d_{23} = -0.60$ rad, $d_{13} = +2.40$ rad. Compute the closure phase and state
whether it indicates an integer cycle slip, a gross error, or nothing wrong.

**★3.** Convert a phase precision of $\sigma_\varphi = 0.50$ rad into millimetres
of line-of-sight displacement at $\lambda = 5.6565\ \mathrm{cm}$, and into a rate
uncertainty for a network whose longest baseline is 1.0 yr.

## ★★ Applied

**★★4.** A network of 20 dates splits into components of 7 and 13 dates. **(a)**
State the rank and null-space dimension. **(b)** Which of the following is
determined by the data: the rate within component 1, the rate within component 2,
the difference in offset between the components? Justify each answer with the
incidence-matrix argument.

**★★5.** With the lesson's noiseless residuals, a model at 90% of the true
velocity gives $\gamma_t = 0.9991$ on a network with baselines up to 0.70 yr and
$0.9916$ on a network with baselines up to 2.43 yr. Explain the mechanism that
makes the longer-baseline network more sensitive, and compute the residual phase
expected on a 2.0 yr baseline for a 10% velocity error of
$12\ \mathrm{mm\,yr^{-1}}$ at $\lambda = 5.6565\ \mathrm{cm}$,
$\theta = 35^\circ$.

**★★6.** A processing chain reports a rate of $11.88\ \mathrm{mm\,yr^{-1}}$ from
a 40-date network with no seasonal term. The demonstration measures a
$+0.464\ \mathrm{mm\,yr^{-1}}$ bias from exactly that omission on a
$12\ \mathrm{mm\,yr^{-1}}$ signal. State the corrected rate, and state what else
must be reported before the corrected number can be used.

## ★★★ Research-oriented

**★★★7.** Design a network for a study that must detect a
$0.5\ \mathrm{mm\,yr^{-1}}$ trend over 3 years in a vegetated area, using the
quantities in this lesson. State: the baseline distribution you would choose and
why, how many dates and why, the model you would fit, the diagnostics you would
report, and the one measurement that would fail first. Justify each choice with
a number from the lesson rather than an adjective. A specification that could not
be executed is a failed answer.

**★★★8.** The lesson assumes independent pair errors. In reality pairs sharing
an acquisition share that date's atmospheric screen. Argue quantitatively how
this changes the expected $\sqrt{M}$ improvement: state which off-diagonal
covariance terms are non-zero, predict how the measured log-log slope of Section
3.3 would change if the shared-screen component dominated, and describe a control
experiment that could distinguish the two regimes in real data.
