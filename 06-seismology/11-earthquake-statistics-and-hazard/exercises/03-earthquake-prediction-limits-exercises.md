# Exercises — 06-11-03 Why Deterministic Prediction Is Considered Unattainable

Attempt these before reading the
[solutions](./03-earthquake-prediction-limits-solutions.md). The lesson is
[03 Prediction Limits](../03-earthquake-prediction-limits.md). All models and data
in this module are **SYNTHETIC**.

## ★ Foundational

**★1.** A fault has a stationary Poisson rate $\lambda = 1/400\ \mathrm{yr^{-1}}$.
Compute (a) the probability of at least one event in the next 40 years, (b) the
probability of no event in the next 400 years, and (c) the expected additional
wait after 200 years with no event.

**★2.** Two windows of $N = 200$ events each have b-values estimated from the same
Gutenberg-Richter population with $b = 1.00$. Compute the expected standard
deviation of their difference and the difference required for a 2-s.e. claim.

**★3.** A test has sensitivity $0.60$ and false-alarm probability $0.10$; the
prior probability of the target event in the window is $P(E) = 8.210\times10^{-4}$
(the value for a $0.01\ \mathrm{yr^{-1}}$ rate and a 30-day window). Compute
$P(E\mid A)$ and the probability gain.

## ★★ Applied

**★★4.** The demonstration reports that for 50 intervals of a Poisson process the
5%–95% range of the measured coefficient of variation is $0.790$–$1.217$, and
$P(\mathrm{CV}<0.8) = 0.060$. A study measures $\mathrm{CV} = 0.85$ from 50
intervals and claims quasi-periodic recurrence. Is that supported? Justify with a
number, and state what additional data would change the answer.

**★★5.** A precursor has sensitivity $0.80$ and false-alarm probability $0.01$,
applied to a window with prior $P(E) = 1.0\times10^{-3}$. Compute the posterior,
the probability gain and the alarm fraction (the probability that the test issues
an alarm on a randomly chosen window).

**★★6.** A retrospective study examines 20 candidate precursor series, all pure
noise, each at the 5% significance level. Compute the probability that at least one
is flagged. State the consequence for how such a claim should be reported.

## ★★★ Research-oriented

**★★★7.** Design a pre-registered, prospective test for a claimed precursor.
Specify the forecast format (alarm or rate), the score, the alarm budget, the
evaluation period, and the failure criterion. Explain why a binary alarm with no
stated alarm fraction cannot be evaluated.

**★★★8.** Derive the false-alarm probability required to reach a 90% posterior
with sensitivity $0.50$ and prior $1\times10^{-3}$, and evaluate it. Then explain,
with the algebra, why no increase in the number of records or the length of the
catalogue improves that requirement for a deterministic prediction, whereas it
does improve an aftershock rate forecast.
