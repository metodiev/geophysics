# Solutions — 25-05-05 Project: Reproducing a Published Geophysical Result

Reference solutions. Every number is printed by
[`code/reproduce_result_demo.py`](../code/reproduce_result_demo.py); all data are
**SYNTHETIC**.

## ★1. The censored log-likelihood

For $\lambda(t) = K/(t+c)^p$ and a catalogue of $n$ event times complete from $t_0$
over a window ending at $T$:

$$\ell(K,c,p) = \sum_{i=1}^{n}\Bigl[\log K - p\log(t_i+c)\Bigr]
- \frac{K}{1-p}\Bigl[(T+c)^{1-p} - (t_0+c)^{1-p}\Bigr],\qquad p \ne 1,$$

$$\ell(K,c,1) = n\log K - \sum_i \log(t_i+c) - K\log\frac{T+c}{t_0+c}.$$

The first sum is the *shape* information — how the observed times are distributed; the
second term is the expected number of events in the window, obtained by integrating
the intensity, and it fixes the *scale* $K$ and couples the parameters to $T$ and
$t_0$. Omitting it (fitting only the first sum) is the classic error that gives a
rate model with no absolute rate; using the wrong $t_0$ while restricting the data
gives $K = 8500$, $c = 6.3$ d, $p = 2.31$ on this catalogue.

## ★2. Reproduction tiers, and routes A–D

| tier | repeated | can falsify | this project |
|---|---|---|---|
| T1 | authors' code, same data | nothing beyond the environment | — |
| T2 | independent code, same method | implementation errors | route A is T2 |
| T3 | independent method, same data | robustness of the claim to the method | routes B, C are T3 |
| T4 | independent dataset, same method | generality of the claim | route D is T4-like |
| T5 | new question, new data | importance of the claim | — |

Route A repeated the stated method (maximum likelihood, same window, same
completeness) with independent code — **T2**. Routes B and C kept the data and changed
the estimator or the parameterisation — **T3**. Route D changed the data by censoring
it, which is a data choice rather than an independent dataset, so it is a
*data-dependence test on a synthetic catalogue* and not T4 in the strong sense;
stating that honestly is part of the answer.

## ★3. Deviations in two units

Route A: $p = 1.1185$, claim $1.10 \pm 0.03$, fit's own error $0.0308$.

$$\text{vs published: } \frac{1.1185 - 1.10}{0.03} = +0.62\ \sigma_\text{published},
\qquad
\text{vs own: } \frac{1.1185 - 1.10}{0.0308} = +0.60\ \sigma_\text{fit}.$$

Both belong in the report because they answer different questions. The first is
"does my result agree with the paper's claim, judged by the paper's own precision?";
the second is "is the difference large compared with *my* precision?". When the two
differ by a large factor — as they do for route D, where the deviation is $+5.0$
published $\sigma$ but only $+1.25$ of the fit's own $\sigma$ — the disagreement is
about precision, not about the result, and the report must say so.

## ★4. Fixing a correlated parameter

$$\frac{0.9592 - 1.1185}{0.0308} = -5.2\ \sigma_\text{fit},$$

and the change is $-12.8\%$ of the true $p$. The mechanism is the correlation
$\mathrm{corr}(c,p) = +0.81$: in the complete-catalogue fit, increasing $c$ and
increasing $p$ both flatten the early decay, so the data constrain a *combination* of
them far better than either individually. Fixing $c$ at a wrong value removes one
degree of freedom but adds a *bias* of order
$\rho\,\sigma_p$ — here about $0.81 \times 0.0308 \approx 0.025$ per standard
deviation of the $c$ error, and the assumed $c = 0.01$ is $4.2$ of its own standard
errors ($0.0102$) from the fitted $0.0529$. Fixing a correlated parameter is therefore
not a conservative simplification: it converts an honest uncertainty into a
systematic error, and the error is invisible unless the truth is known (as it is
here) or the alternative fits are run.

## ★5. Why the binned regression differs

The bins and rates are

| bin (d) | 0–0.1 | 0.1–0.2 | 0.2–0.5 | 0.5–1 | 1–2 | 2–4 | 4–8 | 8–15 | 15–30 |
|---|---|---|---|---|---|---|---|---|---|
| midpoint | 0.05 | 0.15 | 0.35 | 0.75 | 1.5 | 3 | 6 | 11.5 | 22.5 |
| count | 215 | 102 | 120 | 95 | 90 | 108 | 92 | 70 | 60 |
| rate (d⁻¹) | 2150 | 1020 | 400 | 190 | 90 | 54 | 23 | 10 | 4 |

For the first and last points, the regression fits
$\log \text{rate} = \beta_0 - p\log(\text{midpoint})$:

$$\log 2150 = 7.673,\quad \log 0.05 = -3.00;\qquad
\log 4 = 1.386,\quad \log 22.5 = 3.114,$$

so the endpoint slope is approximately
$(7.673-1.386)/(3.114-3.000) = 55$, which shows how little leverage the last bin has
compared with the first — the least-squares slope $p = 1.0213$ is dominated by the
middle bins, where the counts are similar.

Two reasons for the difference from the MLE ($1.1185$):

1. **Bin midpoints are not the mean of a decaying rate.** In the 0–0.1 d bin the rate
   falls by a factor $\left(\frac{0.05+0.1}{0.05}\right)^{1.1} = 2.9$, so the bin
   rate corresponds to a time near the *geometric* mean, not the arithmetic midpoint;
   the substitution distorts the high-curvature early bins most.
2. **Equal weighting in log space.** The regression weights every bin equally although
   the early bins contain hundreds of events and the last bin tens; the MLE weights
   each event equally. The estimator that puts half its leverage on bins with $4$
   events per day is not estimating the same quantity.

A third, related effect is that the binned route effectively imposes $c = 0$ in the
regression's functional form, and $c$ and $p$ are correlated at $+0.81$ — so the
discrepancy is the same mechanism as route C, appearing through the estimator rather
than through a parameter choice.

## ★6. Does route D falsify the claim?

Route D: $p = 1.2498 \pm 0.1197$ against the claim $1.10 \pm 0.03$.

- Against the claim's precision: $(1.2498-1.10)/0.03 = +5.0$ published standard
  errors — nominally a rejection.
- Against its own precision: $(1.2498-1.10)/0.1197 = +1.25$ standard errors — not a
  rejection at all; the fitted 95% interval $[1.02, 1.48]$ comfortably contains 1.10.
- The fit's standard error is $0.1197/0.0308 = 3.9$ times route A's.

So route D does **not** falsify the claim. It establishes something different and more
useful: that losing the first 12 hours costs a factor of 3.9 in precision *and* shifts
the central estimate by $+0.13$, with $c$ moving from $0.0529$ to $0.3899$ and $K$
from 151 to 215. The correct statement is: "with a catalogue complete only after 12 h,
the decay exponent is not measurable to better than $\pm 0.12$ at the 68% level, and
the parameters are biased through the $c$–$p$ degeneracy; the claim of
$\pm 0.03$ therefore implicitly asserts a completeness start better than 12 h." That
is a statement about what the paper's uncertainty *implies* about its data.

## ★7. Is the estimator unbiased here?

$$K:\ \frac{151.3-150}{7.7} = +0.17\ \sigma,\qquad
c:\ \frac{0.0529-0.05}{0.0102} = +0.28\ \sigma .$$

Both are well under one standard error, so on this dataset the estimator shows no
detectable bias. That is *not* a demonstration of unbiasedness: a single realization
carries one draw of noise, and a bias of order the standard error would be invisible.
Establishing unbiasedness requires many synthetic realizations of the *same* model
(typically $\ge 100$) and a check that the mean of the estimates equals the truth to
within the standard error of the mean, together with a check that the nominal
confidence intervals contain the truth at the nominal rate (coverage). The
demonstration deliberately uses one catalogue and therefore supports only the weaker
claim: "the estimator recovered the truth on this realization".

## ★8. Why agreement of the totals is not evidence

The expected count in the window is

$$N(T) = \frac{K}{1-p}\Bigl[(T+c)^{1-p} - (t_0+c)^{1-p}\Bigr] .$$

Along a curve in $(K, p)$ satisfying $N = \text{const}$ the total is unchanged while
$p$ changes. With $c = 0.05$ d, $T = 30$ d and $t_0 = 0$:

| $p$ | $\frac{1}{1-p}\bigl[(T+c)^{1-p}-(t_0+c)^{1-p}\bigr]$ | $K$ for $N = 956.6$ |
|---|---|---|
| 1.00 | 6.3986 | 149.5 |
| 1.10 | 6.3772 | 150.0 |
| 1.25 | 6.7505 | 141.7 |
| 1.50 | 8.5794 | 111.5 |

So $p = 1.00$ with $K = 149.5$ and $p = 1.10$ with $K = 150.0$ give the *same* total
count to within $0.4\%$, and $p = 1.50$ still reproduces the total with
$K = 111.5$, a change of only a factor $1.34$. The total count is therefore almost
blind to the exponent over the range that matters, and only the *shape* of the time
distribution discriminates. This is why a reproduction report must include a shape
statistic (the fraction of events in each time decade, say) and cannot rely on count
agreement — and why the route C fit, which reproduces the total well, still misses $p$
by $5$ standard errors.

## ★★★9. A full reproduction plan

**Claim.** Take a published result of the form "the aftershock decay exponent for
sequence $S$ is $p = 1.10 \pm 0.03$ (one standard error, maximum-likelihood,
$\Delta M \ge 2.5$, complete from the mainshock origin time, window 30 d)".

**Method-choices table** (unstated choices flagged):

| choice | paper states | our value | justification |
|---|---|---|---|
| estimator | MLE | MLE (route A) | matches the claim |
| uncertainty type | one standard error? **not stated** | Hessian-based; also bootstrap | report both |
| completeness start $t_0$ | "complete from the mainshock" | $t_0 = 0.01$ d, sensitivity at 0.1/0.5 d | route D shows this matters |
| which parameters fitted | "fitted $K$, $c$, $p$" | all three | routes C shows the alternative |
| magnitude filter | $\Delta M \ge 2.5$ **not stated** | from the catalogue's own magnitude of completeness | a time-varying $\Delta M$ mimics steeper decay |
| window $T$ | 30 d | 30 d, sensitivity at 15/60 d | $T$ enters the integral |
| binning (only for route B) | n/a | decade bins, empty bins kept | route B is the classical check |

**Estimator.** Written from scratch as in ★1, with the $p = 1$ limit implemented, the
window integral included, and the Hessian computed by finite differences; verified
against a synthetic catalogue with known parameters *before* touching real data
(estimator recovery to a fraction of a standard error; the demonstration does exactly
this and gets $K$ and $c$ to $0.2$–$0.3\sigma$).

**Data.** Catalogued query with explicit filters, the resulting count, and the
completeness start estimated from the magnitude–frequency distribution in short time
windows rather than assumed (a declining detection threshold after a mainshock is the
most common cause of a spuriously high $p$).

**Goodness of fit.** Total count; the fraction of events in each time decade of the
window; a Kolmogorov–Smirnov or binned $\chi^2$ test of the fitted intensity against
the event times, with the caveat that parameters were fitted.

**Alternative method choices.** (1) $c$ fixed at a plausible value (route C); (2) the
binned log–log regression (route B); optionally (3) a Bayesian fit with a wide prior
on $p$, which differs from the MLE only in small samples and provides a cleaner
interval.

**Tier.** T2 for the headline number (independent code, same method), T3 for the
method-dependence spectrum, T4 unreachable without an independent dataset.

**Wording, in the three cases.**

1. *Agreement within the published uncertainty.* "The published value is reproduced
   by an independent implementation of the stated method ($p = 1.10 \pm 0.05$,
   $0.6$ published standard errors from the claim), and the residual method dependence
   spans $\pm 0.15$, larger than the published uncertainty. The numeric claim stands;
   its precision is a property of the chosen estimator."
2. *Agreement only under the original estimator.* "The claim is reproducible with the
   estimator the paper used, but not with the alternatives: a binned regression gives
   $p = 1.02$ ($-2.6$ published standard errors) and fixing $c$ gives $0.96$. The
   result is therefore estimator-conditional, and the paper's statement that $p$ is
   'well determined' is not supported — what is well determined is the pair
   $(c, p)$ along a degenerate direction."
3. *Disagreement under every defensible estimator.* "Under the stated method, the
   censored and uncensored catalogues, and both parameterisations, the exponent lies
   outside the published interval; the discrepancy is larger than the method spread,
   so it is not explained by an estimator choice. What remains unexamined is the
   catalogue completeness (T4), which this study cannot test."

**What would distinguish "the claim is wrong" from "the claim is method-dependent".**
A discrepancy that persists across estimators with a *small* method spread points to
the claim being wrong; a discrepancy that moves with the estimator while the fitted
standard errors stay small points to method dependence. The discriminating evidence is
therefore (i) the method-dependence spread measured on the *same* dataset, (ii) the
fit's own standard errors, and (iii) an independent dataset — in that order of cost,
and only the last one can convert "method-dependent" into "wrong".
