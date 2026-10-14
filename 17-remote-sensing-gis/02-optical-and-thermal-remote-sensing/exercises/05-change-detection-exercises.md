# Exercises — 17-02-05 Change Detection and Time-Series Analysis

Attempt these before reading the
[solutions](./05-change-detection-solutions.md). The lesson is
[05 Change Detection and Time-Series Analysis](../05-change-detection.md).
All scenes and series are **SYNTHETIC** teaching values.

Reference values from the lesson: gain $g = 1.10$; per-band noise
$\sigma = 0.004$; true trend $5.0\times10^{-4}$ per month; AR coefficient
$\rho = 0.6$; drift $2.0\times10^{-4}$ per month.

## ★ Foundational

**★1.** Compute the difference and the ratio for (a) $\rho_1 = 0.12$,
$\rho_2 = 0.15$; and (b) $\rho_1 = 0.12$, $\rho_2 = 0.132$ produced by a gain
$g = 1.10$. Which estimator reports (b) as a change, and by how much?

**★2.** With per-band noise $\sigma = 0.008$ reflectance units, compute the
standard deviation of a difference image and the smallest change detectable at
$2\sigma$ in a single pixel.

**★3.** State what a multiplicative gain does to a difference image and to a
ratio image, and which of the two is invariant to the gain.

## ★★ Applied

**★★4.** Compute the fraction of pairwise slopes contaminated by a fraction
$\varepsilon$ of contaminated observations for $\varepsilon = 0.10$, $0.20$,
$0.293$ and $0.50$. Interpret each value in terms of the median's reliability.

**★★5.** Compute the Mann–Kendall $S$, $\operatorname{var}(S)$ and $z$ by hand for
the series $y = (1, 2, 3, 4, 5)$. State whether the trend is significant at the
$5\%$ level, and state one assumption the test has made.

**★★6.** A series has mean reflectance $0.42$ and carries an uncorrected gain
drift of $5\times10^{-4}$ per month. Compute the spurious trend it produces, and
compare it with a true trend of $2\times10^{-4}$ per month. Over how many months
does the artefact equal the true change?

**★★7.** Compute the relative noise of a ratio change image for two dark bands
$\rho_1 = \rho_2 = 0.05$ with $\sigma = 0.005$, and compare with a bright case
$\rho_1 = \rho_2 = 0.40$. State the practical consequence.

## ★★★ Research-oriented

**★★★8.** Design a change-detection workflow for a target change of $0.02$
reflectance units in a single band. State the required per-band noise, the
registration accuracy, the radiometric normalisation target, the estimator, the
threshold and the multiple-testing control, and check each requirement against the
others for consistency. A specification that could not be executed is a failed
answer.

**★★★9.** A colleague reports a significant greening trend
($z = +3.2$, $p < 0.01$) from a $90$-month satellite index record over a
seasonal landscape. Specify the three checks you would require before accepting
the result, and state for each what the outcome would look like if the trend were
an artefact of (i) an uncorrected gain drift, (ii) autocorrelated noise, and (iii)
a change in the observed phenological phase.
