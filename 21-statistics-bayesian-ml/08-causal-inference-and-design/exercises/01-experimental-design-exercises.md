# Exercises — 21-08-01 Experimental and Survey Design for Earth Studies

Attempt these before reading the
[solutions](./01-experimental-design-solutions.md). The lesson is
[01 Experimental Design](../01-experimental-design.md). All numbers are
**SYNTHETIC**, printed by
[`code/experimental_design_demo.py`](../code/experimental_design_demo.py).

Setup: measurement scatter $\sigma = 5.0$ mm, true rate $1.0$ mm/yr, seasonal
amplitude $3.0$ mm with a 12-month period, interval $5.0$ years, 24 points per
design, detection target 80% power at the two-sided 5% level.

| Design | $\mathrm{sd}(t)$ (yr) | $\operatorname{se}(\hat\beta)$ (mm/yr) | $n$ for power | efficiency |
|---|---|---|---|---|
| even, 24 monthly points | 1.480 | 0.690 | 89.6 | 0.66 |
| first year only, 24 points | 0.276 | 3.699 | 2578.1 | 0.12 |
| two campaigns, 12 at each end | 2.255 | 0.453 | 38.6 | 1.00 |
| three campaigns of 8 months | 1.644 | 0.621 | 72.6 | 0.73 |

Aliasing: monthly sampling recovers $3.802 \pm 0.934$ mm seasonal amplitude and
$+0.783 \pm 0.458$ mm/yr trend; annual sampling aliases the seasonal onto the
intercept as $+1.933$ mm and gives $+2.042 \pm 1.581$ mm/yr, a precision ratio of
$3.45$.

## ★ Foundational

**★1.** Verify the printed slope standard errors from
$\operatorname{se} = \sigma/\sqrt{\sum(t_i-\bar t)^2}$ for the evenly spaced and
the first-year designs, using $\mathrm{sd}(t)$ and $n = 24$.

**★2.** Convert the efficiency column into the factor by which the sample size
changes, for each of the four designs, and state the largest factor.

**★3.** Compute the aliased constant $A\sin\varphi$ for a $3.0$ mm seasonal signal
at phase $\varphi = 0$, $0.7$ and $\pi/2$ radians, and state for which phases the
aliased term vanishes.

## ★★ Applied

**★★4.** Derive the sample-size formula
$n \ge (2.8016\,\sigma/(\beta\,\mathrm{sd}(t)))^2$ and evaluate it for the
two-campaign design. Then compute the required $n$ if the interval is extended from
5 to 10 years at the same number of points per year.

**★★5.** Design the *exact* two-point campaign (12 points at $t = 0$, 12 at
$t = 5$ yr) and compute its $\mathrm{sd}(t)$ and slope standard error. Compare with
the demonstration's two-campaign design and state the precision cost of spreading
each campaign over six months.

**★★6.** A survey samples 20 sites stratified by land use, with 5 measurements per
site. The within-site correlation of the measurements is $\rho = 0.6$. Compute the
design effect $1 + (m-1)\rho$ for $m = 5$, and the effective sample size. State the
consequence for the reported standard error of the mean.

## ★★★ Research-oriented

**★★★7.** Design a campaign whose primary target is a *seasonal amplitude* rather
than a trend. State the sampling geometry, the precision formula, the aliasing
constraint, and the trade with the trend that the same data would provide.

**★★★8.** Design a campaign with heterogeneous measurement variance (scatter
growing with the time since the previous visit). State the estimator, the design
criterion, the optimal visit schedule and the reported uncertainty.

**★★★9.** A monitoring network must detect a change of $2$ mm within one year with
a false-alarm rate of one per decade. Specify the statistic, the threshold, the
number of stations needed, and the design feature that dominates the answer.
