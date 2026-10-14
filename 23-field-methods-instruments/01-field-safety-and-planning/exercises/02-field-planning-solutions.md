# Solutions — 23-01-02 Planning a Field Campaign: Objectives, Permits, Logistics

> Read after attempting. Lesson:
> [02 Field Planning](../02-field-planning.md). All values are **SYNTHETIC**.

---

## ★1 — Expected length and its spread

$$\mathbb{E}[T] = \frac{D}{w} = \frac{15}{0.45} = 33.333\ \mathrm{d},$$

$$\operatorname{sd}(T) = \frac{\sqrt{D(1-w)}}{w}
= \frac{\sqrt{15 \times 0.55}}{0.45} = \frac{\sqrt{8.25}}{0.45}
= \frac{2.8723}{0.45} = 6.383\ \mathrm{d}.$$

Units: $D$ is a count of productive days (dimensionless), $w$ dimensionless,
$\mathbb{E}[T]$ and $\operatorname{sd}(T)$ in calendar days.

Ratio $\mathbb{E}[T]/D = 33.333/15 = 2.222$: the calendar cost of a productive
day is $1/w$ days, and $1/0.45 = 2.222$.

---

## ★2 — Overrun probability and percentiles

**(a) Exact.** The campaign has not finished after $t$ calendar days exactly when
fewer than $D$ working days have occurred in those $t$ days. With independent
days, the number of working days in $t$ days is
$X \sim \mathrm{Binomial}(t, w)$, so

$$P(T > t) = P(X \le D-1).$$

For $t = 40$, $D = 15$, $w = 0.45$:
$X \sim \mathrm{Binomial}(40, 0.45)$ with mean $18$ and variance $9.9$, and

$$P(T > 40) = P(X \le 14) = 0.1326 .$$

**(b) Normal approximation with continuity correction.**

$$z = \frac{40.5 - 33.333}{6.383} = \frac{7.167}{6.383} = 1.1228, \qquad
P(T > 40) \approx 1 - \Phi(1.1228) = 0.1308 .$$

Without the continuity correction the value is $0.1481$, so the correction moves
the answer by $0.017$ — closer to the exact $0.1326$ than the uncorrected value
is to it.

**Percentiles.** $T_{90} = 33.333 + 1.2816 \times 6.383 = 33.333 + 8.181
= 41.51\ \mathrm{d}$ and $T_{95} = 33.333 + 1.6449 \times 6.383
= 33.333 + 10.499 = 43.83\ \mathrm{d}$.

**Which to quote in a contract.** The exact binomial value: a contract is a
statement about a probability, and the normal approximation is a convenience that
has no contractual status. Report the exact probability and state the
independence assumption explicitly, since that assumption is what the contract
actually depends on.

---

## ★3 — Stationary working fraction of a two-state model

$$\pi_{\text{wet}} = \frac{P(\text{wet} \mid \text{dry})}
{P(\text{wet} \mid \text{dry}) + 1 - P(\text{wet} \mid \text{wet})}
= \frac{0.25}{0.25 + 0.30} = \frac{0.25}{0.55} = 0.454545 .$$

$$\pi_{\text{work}} = 1 - 0.454545 = 0.545455, \qquad
\frac{D}{\pi_{\text{work}}} = \frac{15}{0.545455} = 27.50\ \mathrm{d}.$$

Note what this number is and is not. It is the *long-run average rate* argument:
15 productive days at a rate of 0.545 working days per calendar day. It is not
the expectation of the stopping time of the persistent process; the simulation in
the lesson shows that the true mean exceeds $D/w$ at the same stationary rate
(with $D = 20$: $39.03$ d against $37.14$ d). Treat $27.50\ \mathrm{d}$ as a
lower bound on the persistent-weather schedule.

---

## ★★4 — Derivation from waiting times

Let the calendar days be independent Bernoulli working days with probability $w$.
Define $G_i$ as the number of calendar days from the moment the $(i-1)$-th
working day is completed to the moment the $i$-th working day is completed. Each
$G_i$ is the waiting time to the next success in a sequence of independent
Bernoulli trials, so $G_i \sim \mathrm{Geometric}(w)$ on $\{1, 2, 3, \dots\}$ and
$G_1, \dots, G_D$ are independent and identically distributed.

The campaign length is exactly the sum of these $D$ waits,
$T = \sum_{i=1}^{D} G_i$, since no calendar day is counted twice and every day up
to the last working day belongs to exactly one wait. For a geometric variable on
$\{1,2,\dots\}$ with success probability $w$,

$$\mathbb{E}[G_i] = \frac{1}{w}, \qquad
\operatorname{Var}(G_i) = \frac{1-w}{w^{2}} .$$

Linearity of expectation and independence of the summands give

$$\mathbb{E}[T] = \sum_{i=1}^{D} \mathbb{E}[G_i] = \frac{D}{w}, \qquad
\operatorname{Var}(T) = \sum_{i=1}^{D} \operatorname{Var}(G_i)
= \frac{D(1-w)}{w^{2}} .$$

Taking the square root gives
$\operatorname{sd}(T) = \sqrt{D(1-w)}/w$. Neither result requires any
approximation; both are exact for independent days. Note also the special case
$w = 1$: $\mathbb{E}[T] = D$ and $\operatorname{sd}(T) = 0$, as it must be.

---

## ★★5 — Contract length for a stated overrun risk

Model $T$ as normal with mean $39.03\ \mathrm{d}$ and standard deviation
$6.12\ \mathrm{d}$ (the demonstration's persistent-weather values).

For a 10 % overrun risk, $\Phi^{-1}(0.90) = 1.2816$:

$$t_{0.10} = 39.03 + 1.2816 \times 6.12 = 39.03 + 7.84 = 46.87\ \mathrm{d}
\;\Rightarrow\; 47\ \mathrm{d}.$$

For a 5 % overrun risk, $\Phi^{-1}(0.95) = 1.6449$:

$$t_{0.05} = 39.03 + 1.6449 \times 6.12 = 39.03 + 10.07 = 49.10\ \mathrm{d}
\;\Rightarrow\; 50\ \mathrm{d}.$$

**Comparison.** The simulation's 90th percentile is $47.0\ \mathrm{d}$, and the
normal calculation gives 46.87 d. The agreement — 0.3 % — is because the
stopping-time distribution is not strongly skewed once $D = 20$ waits are summed.
The normal approximation would be worse for small $D$ (say $D = 3$), where the
sum of geometric variables is visibly right-skewed.

---

## ★★6 — Cost, buffers and the price of an assumption

$C_{\text{mob}} = 25\,000$ units, $c_{\text{day}} = 2400$ units/day.

Expected cost, using the same normal model as ★★5:

$$\mathbb{E}[\text{cost}] = 25\,000 + 2400 \times 39.03
= 25\,000 + 93\,672 = 118\,672\ \text{units},$$

which matches the demonstration's persistent-weather value of 118 683 units to
within rounding of the mean (39.03 d).

90th-percentile cost:

$$\text{cost}_{90} = 25\,000 + 2400 \times 46.87
= 25\,000 + 112\,488 = 137\,488\ \text{units},$$

against the demonstration's 137 800 units — a 0.2 % difference, again from the
normal approximation to the simulated percentile.

**Two-day buffer.** $2 \times 2400 = 4800$ units. It buys the difference between
a 47-day and a 45-day commitment.

**Comparison with the model difference.** The two models' 90th-percentile costs
differ by $137\,800 - 130\,600 = 7200$ units. So the schedule risk introduced by
ignoring weather persistence costs about 1.5 days of crew time — and it is a
*forecast error*, not a hedge. Buying a two-day buffer is a 4800-unit hedge that
covers any source of delay; treating days as independent is a 7200-unit
underestimate that covers nothing. The correct comparison for a decision is
therefore: hedge cost 4800 units versus expected loss from a 12.9 %-higher overrun
probability, which depends on the daily cost of an overrun (extended crew time,
penalty clauses, lost science).

---

## ★★★7 — How many days to estimate $w$?

**Estimator.** Let $X$ be the number of working days in $n$ campaign days, with
$X \sim \mathrm{Binomial}(n, w)$ under the independence assumption. The
estimator is $\hat w = X/n$ with standard error
$\mathrm{se}(\hat w) = \sqrt{\hat w (1-\hat w)/n}$. The 95 % half-width is
$1.96 \,\mathrm{se}$.

**Sample size.** Setting $1.96\sqrt{w(1-w)/n} = 0.05$:

$$n = \frac{1.96^{2}\, w(1-w)}{0.05^{2}} .$$

- At $w = 0.5$ (the worst case, $w(1-w) = 0.25$):
  $n = 3.8416 \times 0.25 / 0.0025 = 384.2$, so **$n \ge 385$ days**.
- At $w = 0.45$ ($w(1-w) = 0.2475$):
  $n = 3.8416 \times 0.2475 / 0.0025 = 380.3$, so **$n \ge 381$ days**.

A 385-day requirement is about 13 months of continuous on-site time, or roughly
17 five-day field weeks per year for three years. This is the quantitative reason
institutional schedules are calibrated from multi-year meteorological records
rather than from one campaign.

**Two sources of bias.**

1. **Selection of days.** The days actually worked are the days the crew decided
   the weather was workable. A decision rule that becomes more permissive as the
   deadline approaches makes $w$ appear to rise, so logs from a pressured
   campaign overstate $w$ relative to a meteorological criterion.
2. **Conditioning on the survey area.** A campaign abandons the difficult ground
   first, so the observed $w$ is measured on the subset of days and sites where
   work was possible by construction — a survivorship bias that inflates $\hat w$.

A third, weaker effect is that days are not independent, so the nominal binomial
standard error understates the true uncertainty even when $\hat w$ is unbiased.

---

## ★★★8 — Fitting the working probability to a real record

**Data.** A daily series of precipitation amount, snowfall depth, wind speed and
minimum temperature for the nearest station with a long, quality-controlled
record, obtained from the national meteorological service. Requirements: at least
10 years of daily values, documented instrument changes, and a station no more
than a stated distance and elevation difference from the survey area. Record the
station identifier, the period, and the version of the dataset as received.

**Model.** Define a binary "workable" day by a threshold rule that is fixed
*before* fitting (for example: precipitation below a stated amount, wind below a
stated speed, no fresh snow above a stated depth). Fit a first-order two-state
Markov chain to the resulting binary series by counting the four transition
types and forming $\hat P(\text{unworkable} \mid \text{unworkable})$ and
$\hat P(\text{unworkable} \mid \text{workable})$; report the counts with each
estimate. Then run the schedule simulation of the lesson with those two
probabilities rather than with an assumed $w$.

**Validation.** Split the record by year: fit on all years but one and predict the
held-out year's unworkable fraction and its mean run length. Report the prediction
error for both. A model that predicts the long-run fraction but not the run
length is not adequate for schedule risk, because Section 4 shows the tails are
driven by run length.

**Decision it changes.** The contracted number of calendar days (★★5), the
mobilisation date, and the size of the contingency — and, if the fitted
persistence is large enough, the choice of season.

**What it still does not predict.** (i) Within-day workability: a day can be
"unworkable" for two hours and fine afterwards, and a daily binary model cannot
see that. (ii) Access and permit timing, which are the critical path in most
campaigns and are driven by people, not weather. (iii) Equipment failures and
crew illness, which are independent of weather but add days in the same way.
Reporting a schedule distribution built only on weather as if it covered all
sources of delay is the most common overstatement in a field plan.
