# Exercises — 25-05-05 Project: Reproducing a Published Geophysical Result

Attempt these before reading the
[solutions](./05-reproduce-published-result-solutions.md). The project is
[05 Reproducing a Published Result](../05-reproduce-published-result.md); all numbers
are **SYNTHETIC** and printed by
[`code/reproduce_result_demo.py`](../code/reproduce_result_demo.py):

| Quantity | Value |
|---|---|
| published claim | $K/(t+c)^p$ with $c = 0.05$ d and $p = 1.10 \pm 0.03$ |
| generating model (truth) | $K = 150$, $c = 0.05$ d, $p = 1.10$, window $T = 30$ d |
| catalogue | 956 events complete from $t=0$; 437 of them in the first 12 h |
| route A, full MLE | $K = 151.3 \pm 7.7$, $c = 0.0529 \pm 0.0102$, $p = 1.1185 \pm 0.0308$; $\mathrm{corr}(c,p) = +0.81$ |
| route B, binned log–log | $p = 1.0213$; bin rates 2150, 1020, 400, 190, 90, 54, 23, 10, 4 events/day |
| route C, $c$ fixed at 0.01 d | $p = 0.9592$ |
| route D, censored at 12 h | $K = 214.9 \pm 67.1$, $c = 0.3899 \pm 0.3127$, $p = 1.2498 \pm 0.1197$; 519 events |
| goodness of fit | 956 observed vs 956.6 expected; 519 vs 525.1 censored |
| method spread | $p$ spans 0.2907 $= 4.8 \times$ the published $\pm 0.03$ |

## ★ Foundational

**★1.** Write the modified-Omori log-likelihood for a catalogue complete from $t_0$
over a window $T$, including the window integral, and give its $p = 1$ limit. State
what each term contributes.

**★2.** State the four reproduction tiers and, for each, what a disagreement at that
tier does and does not falsify. Which tier is each of routes A–D?

**★3.** Using route A, compute the deviation of $p$ from the claim in units of (i) the
published standard error and (ii) the fit's own standard error. Explain why both
numbers belong in a reproduction report.

## ★★ Applied

**★★4.** Route C fixes $c$ at 0.01 d. Compute the change in $p$ relative to route A in
units of route A's standard error, and explain, using $\mathrm{corr}(c,p) = +0.81$,
why fixing a correlated parameter introduces a bias rather than merely reducing the
number of fitted parameters.

**★★5.** Route B fits a straight line to the log–log histogram. Using the printed bin
rates and bin edges (0, 0.1, 0.2, 0.5, 1, 2, 4, 8, 15, 30 days), recompute the
regression by hand for at least two points, and state two reasons why the slope
differs from the maximum-likelihood value (bin midpoints, and equal weighting of bins
with very different counts).

**★★6.** Route D loses the 437 events in the first 12 hours. Show that the fitted
parameters change by more than the *published* uncertainty while the fit's own
standard error grows by a factor 3.9. Then state whether route D falsifies the claim,
and what it does establish.

**★★7.** The full-catalogue fit recovers $K = 151.3 \pm 7.7$ against a true 150 and
$c = 0.0529 \pm 0.0102$ against a true 0.05. Compute the deviations in units of the
fitted standard errors and state whether the estimator is unbiased *for this dataset*.
Explain why one dataset cannot establish unbiasedness in general.

**★★8.** The total counts agree (956 against 956.6). Explain why this is *not* evidence
that the fit is correct, using the $K$–$p$ trade-off: show how a larger $p$ with a
larger $K$ can leave the integrated count nearly unchanged while changing the shape.

## ★★★ Research-oriented

**★★★9.** Choose a real published quantitative geophysical claim (a fitted exponent, a
rate coefficient, a threshold, a scaling relation) and write the full reproduction
plan: the claim with the definition of its uncertainty; the method-choices table with
the unstated choices flagged and your chosen values justified; the independently
derived estimator; the data query and filters; the goodness-of-fit statistics; the
two alternative method choices whose spread you will quantify; the tier you can reach
and the tier you cannot; and the exact wording of the conclusion you would be willing
to defend for (i) agreement within the published uncertainty, (ii) agreement only
under the original estimator, and (iii) disagreement under every defensible
estimator. Your answer must explain what additional evidence would distinguish "the
claim is wrong" from "the claim is method-dependent".
