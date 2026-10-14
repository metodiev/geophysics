# Solutions — 03-03-08 scipy.special and scipy.stats in Practice

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output; values marked *measured* come from a modified
> or independent calculation, stated where used.

---

## ★1 — The diffusion solution

**(a)** $\kappa t = 1.2\times10^{-6} \times 100 \times 3.15576\times10^{7} =
3.7869\times10^{3}$ m², so $2\sqrt{\kappa t} = 123.06$ m and the argument is
$50/123.06 = \mathbf{0.40630}$, matching the table's 0.406254 (the difference is
in the last two digits because the table's value is computed from the same
constants with full precision).

**(b)** $\mathrm{erfc}(0.406254) = 0.565609$, as tabulated. The third column is
$T/\Delta T$ and is dimensionless; the fourth column is $T = 12 \times
0.565609 = 6.7873$ K.

**(c)** $u = 1000/123.06 = 8.125$ (full precision 8.125075), and
$\mathrm{erfc}(8.125) = 1.13\times10^{-30}$. So
$T = 12 \times 1.13\times10^{-30} = 1.4\times10^{-29}$ K, which is zero to every
physically meaningful precision — it is below the temperature change produced by
a single phonon in any conceivable sample. The printed 0.000000 is the correct
statement that the surface disturbance has not reached 1 km in 100 years: the
diffusion length is $\sqrt{\kappa t} = 61.5$ m.

**(d)** $q = k\Delta T/\sqrt{\pi\kappa t} = 2.5\times12/\sqrt{1.1897\times10^{4}}
= 30/109.07 = 0.27505\ \mathrm{W\,m^{-2}} = \mathbf{275.0}$ mW m⁻². The ratio to
the 1000 yr value is exactly $\sqrt{10} = 3.162$, and
$86.9769 \times 3.162 = 275.0$ — consistent. The $t^{-1/2}$ decay of this
perturbation is what makes the palaeoclimate correction to a heat-flow
measurement large for a recent surface change and negligible for an old one.

---

## ★2 — The error-function family

**(a)** $\mathrm{erfc}(x) = 2\Phi(-x\sqrt2)$, where $\Phi$ is the standard
normal CDF (`scipy.special.ndtr`). Equivalently
$\mathrm{erf}(x) = 2\Phi(x\sqrt2) - 1$.

**(b)** $\mathrm{erf}(8) = 1 - 1.12\times10^{-29}$, and the nearest double to
that number is exactly 1.0, because double precision has a spacing of
$1.1\times10^{-16}$ near 1. Subtracting the two gives exactly zero — silent
cancellation, no error, no warning.

**(c)** $\mathrm{erfc}(4) = e^{-16}\,\mathrm{erfcx}(4) =
1.12535\times10^{-7} \times 0.1369995 = 1.54173\times10^{-8}$, matching the
tabulated 1.541726e-08. The route works because both factors are computed
accurately: `erfcx` supplies the $O(1)$ prefactor and the exponential supplies
the small magnitude.

**(d)** $\ln\mathrm{erfc}(30) = \ln\mathrm{erfcx}(30) - 30^2 =
\ln(0.01879589) - 900 = -3.97412 - 900 = \mathbf{-903.97412}$. The direct route
fails because $e^{-900} \approx 10^{-391}$, below the smallest representable
double ($4.9\times10^{-324}$), so `erfc(30)` underflows to zero and its
logarithm is $-\infty$. Working in the log domain is the only way to keep the
information, and it is the correct approach for any diffusion problem where the
argument exceeds about 25.

---

## ★3 — The Aki–Utsu estimator

**(a)** $\hat b = \log_{10}e / (\bar m - m_c)$, equivalently
$\hat b = \hat\beta/\ln 10$ with $\hat\beta = 1/(\bar m - m_c)$.

**(b)** $\mathrm{SE} = 0.981599/\sqrt{1500} = 0.981599/38.7298 = \mathbf{0.025345}$,
as reported.

**(c)** $b = \log_{10}e/\text{scale} = 0.434294/0.442436 = \mathbf{0.981599}$,
identical to the closed form to seven digits (the demo reports agreement to
$4.4\times10^{-16}$).

**(d)** It tells you that the estimator is *unbiased in expectation* and that a
single sample's discrepancy of 0.73 standard errors is entirely ordinary: about
47% of samples would lie farther from the truth than this one. It does *not*
tell you that the truth is 0.98, nor that the model is right, nor that the
completeness threshold is correct — all of which are separate assumptions (§4
and §5).

---

## ★4 — Cumulative least squares

**(a)** $0.852307/0.981599 = 0.8683$, i.e. the least-squares value is 13.2%
below the MLE.

**(b)** The quoted standard error comes from the ordinary least-squares formula
$\sigma^2(A^TA)^{-1}$, which assumes the residuals are independent with common
variance. The cumulative counts are neither: each event contributes to every
bin below its magnitude, so a single large event shifts many "observations" in
the same direction. The formula therefore measures something that is not the
sampling variability of $\hat b$; the value 0.017304 is smaller than the MLE's
0.025345, i.e. it is not merely wrong but over-confident.

**(c)** $r^2$ measures the fraction of the *variance of the fitted ordinate*
explained by the line, and a cumulative count curve is a monotonically
decreasing, nearly log-linear sequence — it is easy to fit well. $r^2$ says
nothing about independence, and the dependence is what invalidates the
standard error. The same point applies to any regression of cumulative
quantities: the plot is smooth because it is integrated, not because the
residuals are well behaved.

**(d)** Check for repeated contributions, e.g. confirm
`counts[i] == (m >= edges[i]).sum()` and note that consecutive counts differ by
the number of events in the bin — i.e. the series is a cumulative sum of
independent counts, so its increments are independent but its levels are not.
A one-line demonstration is that the *increments* are uncorrelated when shuffled
while the levels are essentially perfectly correlated.

---

## ★5 — Goodness of fit and calibration

**(a)** The first row compares the data with a distribution whose parameter was
*estimated from those same data*, so the null distribution of the KS statistic
is not the tabulated one. The second row compares the data with the *true*
distribution (a luxury available only because the sample is synthetic), for
which the tabulated KS null distribution applies exactly.

**(b)** The calibrated p-value (0.728) is smaller than the naive one (0.863).
Estimating the parameter makes the fitted distribution hug the data, which
reduces $D$ compared with what an *independent* draw from the same fitted
distribution would give; keeping $D$ fixed and using the wrong (specified-case)
null distribution therefore overstates the p-value. The discrepancy is
necessarily in this direction: fitting can only reduce $D$ in expectation.

**(c)** The fitted $b = 1.1840$ is a plausible-looking number — it is within the
range of published b-values — while the calibrated $p = 0.0005$ says the data
are not exponential at all. Together they show that **a fitted parameter carries
no evidence for the model that produced it**, and that the goodness-of-fit test
is not an optional extra.

**(d)** Pseudocode:

```
D_obs = KS statistic of (data - mc) against an exponential fitted to it
for r in 1..R:
    sim    = exponential(scale = D_obs's scale, size = n)
    D_sim  = KS statistic of sim against an exponential fitted to sim
    count += (D_sim >= D_obs)
p = (count + 1) / (R + 1)
```

The Monte-Carlo standard error of a p-value is $\sqrt{p(1-p)/R}$, so for
$p \approx 0.05$ and an accuracy of 0.01 you need $R \ge 0.05\times0.95/0.01^2 =
475$, i.e. **500 replications** as a minimum and 2000 for comfort (the demo uses
2000, and the $+1$ in numerator and denominator makes the estimator usable at
$p = 0$).

---

## ★6 — Correlation, sample size and the number to report

**(a)** $n = 10$: $0.949 - 0.326 = 0.623$. $n = 20\,000$:
$0.365 - 0.340 = 0.025$. Ratio $= 24.9$.

**(b)** $\sqrt{20\,000/10} = 44.7$, which is larger than the measured 24.9. The
$n^{-1/2}$ law applies to the standard error of the **Fisher $z$**
transformation, not to the asymmetric interval in $r$: in $z$ units the widths
are $2\times1.96/\sqrt{n-3}$, which gives
$\sqrt{19\,997/7} = 53.5$ — the exact scaling. Mapping back through
$r = \tanh z$ compresses the large-$r$, small-$n$ interval, so the width in $r$
grows more slowly than $n^{-1/2}$ here. This is a good example of a
transformation that restores a simple scaling law, and of why the confidence
procedure is defined in the transformed variable.

**(c)** The Pearson p-value is computed from a $t$ statistic with $n-2 = 19\,998$
degrees of freedom and a value of order $0.35\times\sqrt{20\,000} \approx 50$;
the corresponding tail probability is of order $10^{-400}$, which underflows the
smallest representable double long before it reaches print. The correct
reporting is "$p < 10^{-308}$" or, better, the confidence interval.

**(d)** The 95% confidence interval for $\rho$. It is on the same scale as the
quantity of interest, it narrows at a known rate, and it makes the sample size's
role visible: $[+0.326, +0.949]$ at $n = 10$ and $[+0.340, +0.365]$ at
$n = 20\,000$ are statements a reader can act on, while $p$ values 300 orders of
magnitude apart are not.

---

## ★7 — t against z

**(a)** $11.0264 \pm 2.0687\times0.9019 = 11.0264 \pm 1.8658$, giving
$[9.1606, 12.8922]$, matching the tabulated $[9.1607, 12.8921]$ to the printed
precision.

**(b)** $1 - 1.96/2.06866 = 1 - 0.94746 = 0.05254$, i.e. **5.25%**, as stated.

**(c)** $2F_t(1.96; 23) - 1 = 2\times0.96890 - 1 = 0.93780$, i.e. 93.78%
coverage. So a nominal 95% interval built with the normal quantile actually
covers 93.8% of the time.

**(d)** The requirement is that the two quantiles differ by less than 1%, i.e.
$t_{0.975}(\nu) < 1.96/0.99 = 1.9798$. *Computed*: $t = 2.009$ at $\nu = 50$,
1.9840 at $\nu = 100$, **1.9799 at $\nu = 120$**, 1.9759 at 150 and 1.9719 at
200. So $\nu \gtrsim 120$, i.e. **$n \gtrsim 122$ samples**, is where the
z-interval is within 1% of the t-interval. Below about 30 samples the
difference exceeds 3%, and it is never exactly zero.

---

## ★8 — Lognormal summaries

**(a)** With $\log_{10}k \sim N(-1, 1.2^2)$ the natural-log parameters are
$\mu_{\ln} = -1\times\ln10 = -2.3026$ and $\sigma_{\ln} = 1.2\times\ln10 =
2.7631$. The population median is $10^{-1} = \mathbf{0.1}$ mD. The mean is

$$E[k] = e^{\mu_{\ln} + \sigma_{\ln}^2/2} = e^{-2.3026 + 3.8175} =
e^{1.5149} = \mathbf{4.548}\ \text{mD},$$

so the mean exceeds the median by a factor of **45.5**.

**(b)** The distribution is extremely heavy-tailed: the standard deviation is
$\sqrt{(e^{\sigma_{\ln}^2}-1)}\,E[k] = 45.5\times4.548 = 206.8$ mD, so the
standard error of the mean for $n = 400$ is $206.8/20 = 10.34$ mD — **more than
twice the sample mean itself**. The measured sample mean of 1.783 mD lies
$(4.548-1.783)/10.34 = 0.27$ standard errors below the population mean, i.e. it
is a perfectly ordinary draw from a distribution whose mean is essentially
unmeasurable at this sample size. The demo's 400-sample median (0.0882) is, by
contrast, within 12% of the population median — the median of a lognormal is
efficiently estimated (its standard error is $\sigma_{\ln}/\sqrt n$ in the log
domain), which is why it is the statistic to report.

**(c)** "Lognormal" means exactly "normal in the logarithm", so Shapiro–Wilk on
$\log k$ tests the model's defining assumption rather than a consequence of it,
and it is the most powerful such test available. $p = 0.29$ means the data are
consistent with normality in the log domain; it does **not** prove normality,
and it cannot exclude a distribution that is close to but not exactly lognormal
(truncation, a mixture of two populations, a physical upper bound). The
correct statement is "no evidence against lognormality at this sample size".

**(d)** Two sentences: "Permeability is approximately lognormal with a median of
0.088 mD ($n = 400$, geometric mean 0.078 mD); the arithmetic mean of 1.78 mD is
20 times the median and its standard error exceeds its own value, so it should
not be used as a summary." and "Any linear average of these values — an
effective permeability, an arithmetic mean, a total flow — is dominated by the
largest few samples and should be reported with the median alongside."

---

## ★9 — A two-network catalogue

**(a)** $\mathrm{SE} = 0.94/\sqrt{8000} = \mathbf{0.01051}$, so the reported
$\pm0.011$ is consistent with (slightly larger than) the asymptotic formula.
Consistency to two significant figures is all the formula can offer, and it
assumes independent events — a catalogue with aftershocks violates that, making
the true uncertainty larger.

**(b)** Two possibilities. First, **the catalogue is not complete at the stated
$m_c$**: a deficit of small events inflates $D$ systematically. Second, the
**events are not independent**: a large mainshock with many aftershocks
produces a local bump in the magnitude distribution, and any clustered sample
shows a larger $D$ than an independent one. They are distinguished by the
residual pattern: incompleteness appears as a one-sided excess of *small*
magnitudes near the threshold, while clustering appears as an excess near the
*main shock's* magnitude, at the top of the distribution. Plotting the
signed CDF residual against magnitude separates the two immediately.

**(c)** Mixing two networks means the catalogue's detection probability is
$\approx 1$ above 2.8 and between 0 and 1 over $[2.2, 2.8]$. The mixture misses
small events preferentially, so the observed magnitude distribution is *steeper*
than the true one — the fitted $b$ is **too high**, and the deficit is
concentrated just above 2.2. The fix is either to truncate the analysis at the
*maximum* of the two completeness thresholds ($m_c = 2.8$ for the merged
catalogue) or to model the detection probability explicitly and fit the joint
likelihood; the first is what most studies do, at a cost of discarding half the
events. Note that this is a *different* effect from §4's estimator bias: the
estimator is right and the data are wrong.

**(d)** The **b-value stability plot**: compute $\hat b$ from equation (4) using
only events above a trial threshold $m_{\mathrm{tr}}$, and plot $\hat b$
against $m_{\mathrm{tr}}$. For a complete catalogue the curve is flat above
$m_c$ within its error bars; for an incomplete one it rises steeply and
flattens only above the true completeness level. The threshold at which the
curve becomes flat *is* the estimated $m_c$, and the flat portion's value is the
estimate to quote. Two extra numbers make the analysis complete: the sensitivity
of the flat level to the assumed $m_c$ (a systematic error that no statistical
error bar covers), and the maximum-magnitude check that the sample is not
truncated at the top.
