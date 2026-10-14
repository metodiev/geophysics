# Solutions — 21-08-01 Experimental and Survey Design for Earth Studies

> Read after attempting. Lesson:
> [01 Experimental Design](../01-experimental-design.md). Numbers are
> **SYNTHETIC**, printed by
> [`code/experimental_design_demo.py`](../code/experimental_design_demo.py).

---

## ★1 — Verifying the printed standard errors

$$\operatorname{se}(\hat\beta) = \frac{\sigma}{\sqrt{\sum_i(t_i-\bar t)^2}}
= \frac{\sigma}{\mathrm{sd}(t)\sqrt{n}} .$$

**Evenly spaced design:** $\mathrm{sd}(t) = 1.480$ yr, $n = 24$,

$$\operatorname{se} = \frac{5.0}{1.480\times\sqrt{24}}
= \frac{5.0}{1.480\times4.8990} = \frac{5.0}{7.2506} = 0.6896 \approx 0.690\
\text{mm/yr} ✔$$

**First-year design:** $\mathrm{sd}(t) = 0.276$ yr,

$$\operatorname{se} = \frac{5.0}{0.276\times4.8990} = \frac{5.0}{1.3521}
= 3.698 \approx 3.699\ \text{mm/yr} ✔$$

Both reproduce the printed values, which confirms that the design enters the
precision *only* through $\mathrm{sd}(t)\sqrt n$: the same $n = 24$ gives errors
differing by a factor of $5.4$ on geometry alone.

---

## ★2 — Efficiency as a sample-size factor

Efficiency is defined as the ratio of the best standard error to the design's, so
the sample-size factor is the reciprocal of the efficiency squared:

| Design | efficiency | $n$ factor |
|---|---|---|
| two campaigns, 12 at each end | $1.00$ | $1.0$ |
| three campaigns of 8 months | $0.73$ | $1.9$ |
| even, 24 monthly points | $0.66$ | $2.3$ |
| first year only, 24 points | $0.12$ | $66.7$ |

The largest factor is $66.7$ — the first-year design needs about $67$ times as much
data as the two-campaign design for the same precision, and the printed
$n$-for-power column ($2\,578$ against $38.6$ points) shows the same ratio
($66.8$). Quoting the factor rather than the ratio of standard errors is the more
useful form: it is the currency in which a campaign is actually paid for.

---

## ★3 — The aliased constant

At annual sampling every epoch has the seasonal phase $\varphi$, so the seasonal
contribution to the sample is the constant $A\sin\varphi$ with $A = 3.0$ mm:

| $\varphi$ (rad) | $\sin\varphi$ | aliased constant (mm) |
|---|---|---|
| $0$ | $0.000$ | $0.000$ |
| $0.7$ | $0.644$ | $+1.933$ ✔ (the printed value) |
| $\pi/2$ | $1.000$ | $+3.000$ |

The aliased term **vanishes when the sampling epoch coincides with a zero crossing
of the seasonal cycle** ($\varphi = 0$ or $\pi$). This is a trap worth naming: a
campaign scheduled at the same calendar date every year, chosen because it matches
a zero crossing, shows no seasonal bias at all — until the season shifts, a station
is visited a month late, or a second site with a different phase is added. The
design decision that looks safest is the one whose safety depends on an assumption
that is never stated.

---

## ★★4 — The sample-size formula

The requirement is that the expected estimate be $z_{1-\alpha/2} + z_{1-\beta} = 2.8016$
standard errors from zero:

$$\frac{\sigma}{\mathrm{sd}(t)\sqrt n} \le \frac{\beta_{\text{target}}}{2.8016}
\;\Longrightarrow\;
n \ge \left(\frac{2.8016\,\sigma}{\beta_{\text{target}}\,\mathrm{sd}(t)}\right)^2 .$$

**Two-campaign design:** $\mathrm{sd}(t) = 2.255$ yr,

$$n \ge \left(\frac{2.8016\times5.0}{1.0\times2.255}\right)^2
= \left(\frac{14.008}{2.255}\right)^2 = 6.212^2 = 38.6 \approx 39\ \text{points}
✔$$

**Doubling the interval to 10 years, same points per year.** If the number of
points also doubles (same density), $\mathrm{sd}(t)$ doubles and $n$ is unchanged;
the precision improves by $\sqrt2$ for the same *density* but at twice the cost, so
the metric to quote is the cost per unit precision. If instead the **same total
number of points** is spread over 10 years, $\mathrm{sd}(t)$ doubles and the
requirement falls by a factor of four:

$$n \ge \left(\frac{14.008}{4.510}\right)^2 = 3.106^2 = 9.6 \approx 10\
\text{points} .$$

That is the lever-arm argument in its purest form: four times fewer observations,
for four times the duration, at the same precision — which is why long-baseline
monitoring beats frequent visiting, and why the two cheapest currencies in
geophysics are *time* and *geometry*, not instruments.

---

## ★★5 — The exact two-point design

Twelve points at $t = 0$ and twelve at $t = 5$ yr: the sample takes only two
values, each with weight $1/2$, so

$$\mathrm{sd}(t) = \frac{5.0 - 0.0}{2} = 2.500\ \text{yr}, \qquad
\operatorname{se}(\hat\beta) = \frac{5.0}{2.500\times4.8990} = 0.408\
\text{mm/yr} .$$

The demonstration's two-campaign design spreads each campaign over six months, so
its $\mathrm{sd}(t) = 2.255$ yr and its error is $0.453$ mm/yr: the six-month
spread costs

$$\frac{0.453 - 0.408}{0.408} = 11\%\
\text{ in precision, i.e. } \left(\frac{0.453}{0.408}\right)^2 = 1.23$$

times the observations for the same precision — a $23\%$ penalty for the logistic
convenience of keeping a crew on site for a season. The lesson is not that the
spread is wrong (it may buy better monument checks, more days of satellite
coverage, or a mean over weather), it is that the penalty is computable before the
campaign and should be stated as part of its cost.

---

## ★★6 — A clustered survey's design effect

With $m = 5$ measurements per site and an intra-cluster correlation
$\rho = 0.6$, the variance of the mean is inflated by the design effect

$$\text{DEFF} = 1 + (m-1)\rho = 1 + 4\times0.6 = 3.4 .$$

With $20 \times 5 = 100$ measurements, the **effective sample size** is

$$n_{\text{eff}} = \frac{n}{\text{DEFF}} = \frac{100}{3.4} = 29.4 ,$$

so a standard error computed as $s/\sqrt{100}$ is too small by
$\sqrt{3.4} = 1.84$: the honest error is $s/\sqrt{29.4}$, nearly twice as wide.

The remedy is a design choice, not an analysis one: either increase the number of
**sites** (which is what the design effect says is the scarce resource), or reduce
the within-site correlation by measuring at different times or with different
instruments. Five measurements at one site are one observation with a smaller
error, not five observations — and the arithmetic above is the exact statement of
how much smaller.

---

## ★★★7 — Designing for a seasonal amplitude

**Precision formula.** For a sinusoid of known period fitted together with a
constant and a trend, the amplitude's standard error is approximately

$$\operatorname{se}(\hat A) \approx \sigma\sqrt{\frac{2}{n}} ,$$

*independent* of the sampling dates, provided the sampling resolves the cycle
evenly. This is the crucial contrast with the trend, whose precision depends
entirely on the geometry.

**Geometry.** Sample at a rate that gives the cycle a non-degenerate distribution
of phases: about four or more epochs per period, or equivalently epochs spaced
uniformly modulo the period. Aliasing is avoided by construction if the epochs are
not commensurate with 12 months.

**Constraint.** With $n = 60$ monthly epochs and $\sigma = 5$ mm,
$\operatorname{se}(\hat A) = 5\sqrt{2/60} = 0.913$ mm, against the measured
$0.934$ — the demonstration's number.

**Trade with the trend.** A single campaign serves both objectives only if it is
long enough for the trend (a wide span of $t$) *and* dense enough for the seasonal
cycle (at least four epochs per period). Those pull in opposite directions on
cost: monthly sampling for five years (60 points) satisfies both, while an annual
design satisfies neither well. The design that resolves the trade explicitly is
usually **monthly during a few long campaigns**, which combines a wide span with
seasonal resolution and needs about $24$–$36$ points rather than $60$. Report both
standard errors — that of the trend and that of the amplitude — because a design
optimised for one can be poor for the other, and the reader cannot guess which
objective was optimised.

---

## ★★★8 — Heterogeneous measurement variance

**Model.** Let the scatter of a measurement at time $t_i$ be $\sigma_i$, growing
with the time since the previous visit: $\sigma_i^2 = \sigma_0^2 +
\kappa\,\Delta t_i$ (a random-walk-like decay of an antenna or monument's
positional memory). The trend is estimated by **weighted least squares** with
weights $w_i = 1/\sigma_i^2$:

$$\hat\beta_w = \frac{\sum_i w_i(t_i-\bar t_w)(y_i-\bar y_w)}
{\sum_i w_i(t_i-\bar t_w)^2}, \qquad
\operatorname{se}(\hat\beta_w) = \frac{1}{\sqrt{\sum_i w_i(t_i-\bar t_w)^2}},$$

with $\bar t_w = \sum w_i t_i/\sum w_i$ — the *weighted* mean of the sampling times.

**Design criterion.** Maximise the weighted leverage
$\sum_i w_i(t_i-\bar t_w)^2$ subject to a budget of $n$ visits.

**Optimal schedule.** With variance increasing in the inter-visit gap, the
optimum is *not* the two-point design of ★★5: it is a schedule that visits often
enough to keep $\sigma_i$ low while still placing enough weight at the ends of the
interval. The optimum is found by numerical optimisation of the criterion over the
visit times, and its structure is typically a cluster of visits at each end **with
regular intervals inside each cluster** to control $\sigma_i$ — a quantitative
version of the campaign design chosen for logistic reasons in ★★5.

**Reported uncertainty.** Report $\operatorname{se}(\hat\beta_w)$ from the actual
schedule, and state both the variance model (with the estimated $\kappa$) and the
weights used. Two designs compared without stating whether the weights were
optimal for the same $\kappa$ are not comparable.

---

## ★★★9 — A monitoring network with an alarm budget

**Statistic.** A change of $2$ mm over one year is detected by a trend statistic
over a 1-year window, or — better for sequential monitoring — by a cumulative sum
of the standardised residuals from the reference model, as in the monitoring
schemes of
[21-06-09](../../06-ml-in-geophysics/09-ml-pitfalls-geophysics.md). The
one-decimal-per-decade false-alarm requirement translates to an in-control average
run length of about $10 \times 365 = 3\,650$ daily epochs (or $10$ annual epochs
for an annual test), so for a daily statistic choose the threshold to give
ARL$_0 = 3\,650$.

**Threshold and sizing.** With per-epoch scatter $\sigma_s$ and a single station,
the year-long mean has standard error $\sigma_s/\sqrt{n_{\text{eff}}}$ where
$n_{\text{eff}}$ is set by the station's own noise correlation; requiring it to be
$2\ \mathrm{mm}/2.8016 = 0.71$ mm gives $n_{\text{eff}}$, hence the observation
rate. With $S$ stations the noise is reduced by $\sqrt S$ if their errors are
independent — so if one station needs $n$ observations for the target, four
independent stations need $n/4$ each. That $\sqrt S$ law is the entire argument for
networks.

**The design feature that dominates.** **Common-mode noise**, not instrument
precision. If all stations share a reference-frame or atmosphere-correlated error
(a real common-mode error, as is typical for regional networks), then $\sqrt S$
never materialises: the network's error is bounded below by the common mode
however many stations are added. The design question is therefore not "how many
stations" but "how much of the error is common", and the answer requires either
independent reference frames, an independent measurement technique at the same
sites, or an explicit common-mode estimate — which must be measured, not assumed,
because the whole scaling of the network hinges on it.
