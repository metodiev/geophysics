# Solutions — 21-07-05 Point Processes and Seismicity Rate Models

> Read after attempting. Lesson:
> [05 Point Processes](../05-point-processes.md). Numbers are **SYNTHETIC**,
> printed by [`code/point_processes_demo.py`](../code/point_processes_demo.py).

---

## ★1 — Window probabilities

For a Poisson count $N$ with expectation $\Lambda$,
$\Pr(N = k) = e^{-\Lambda}\Lambda^k/k!$, so

$$\Pr(\ge 1) = 1 - e^{-\Lambda}, \qquad
\Pr(\ge 3) = 1 - e^{-\Lambda}\left(1 + \Lambda + \frac{\Lambda^2}{2}\right) .$$

**$\Lambda = 1.126$:** $\Pr(\ge1) = 1 - e^{-1.126} = 1 - 0.32435 = 0.67565$,
against the printed $0.6757$ ✔.
$\Pr(\ge3) = 1 - 0.32435(1 + 1.126 + 0.633938) = 1 - 0.32435 \times 2.75994
= 1 - 0.89517 = 0.10483$, against the printed $0.1049$ ✔.

**$\Lambda = 40.770$:** $e^{-40.77} \approx 2.0\times10^{-18}$, so both
probabilities are 1 to every decimal the demonstration prints ✔.

The lesson of the pair is the shape of the conversion: at a mean of 1.1 events,
"at least one" and "at least three" differ by a factor of 6; at a mean of 41 they
are both certainty. A rate forecast is therefore most informative exactly where
the decision threshold bites, and least informative where the outcome is already
decided.

---

## ★2 — The Omori decay and the information in the time span

$$\lambda(\tau) = \frac{K}{(\tau+c)^p}, \qquad
K = 7.35,\ c = 0.1\ \text{day},\ p = 1.10 .$$

| $\tau$ (days) | $(\tau+c)^{-1.1}$ | rate (events/day) |
|---|---|---|
| 1 | $1.1^{-1.1} = 0.90046$ | $6.618$ |
| 100 | $100.1^{-1.1} = 0.006303$ | $0.04633$ |

$$\text{ratio} = \frac{6.618}{0.04633} = 142.9 .$$

The ratio depends on the exponent through the *span*, not the absolute times:

$$\frac{\lambda(\tau_2)}{\lambda(\tau_1)}
= \left(\frac{\tau_1 + c}{\tau_2 + c}\right)^{p}
= 91.0^{\,p}\ \text{for } \tau_1 = 1,\ \tau_2 = 100 .$$

So $p = 1.00$ gives $91.0$, $p = 1.10$ gives $142.9$ and $p = 1.30$ gives
$91.0^{1.3} = 352$. The information about $p$ is the *leverage* of the τ span: a
catalogue that covers only 1–10 days has a span ratio of 9.2 and a predicted ratio
of $9.2^{p}$ — a 20% change in $p$ moves the observable ratio by only about 20%,
whereas the same change over 1–100 days moves it by 48%. This is why a p estimate
from a short sequence is poorly constrained regardless of how many events it
contains, and why extensible windows matter more than event count for this
parameter.

---

## ★3 — Background versus aftershocks after the mainshock

Expected background in the $2650$ days after the mainshock:
$0.020 \times 2650 = 53.0$ events. Simulated aftershocks in that period: $63$.

The two populations are **comparable in size**, which is the practical problem. If
the background events were counted as aftershocks, the fitted productivity would be
inflated by a factor of about $116/63 = 1.84$, and the decay would be biased flat,
because the background contributes a constant rate that dominates at large τ. If
aftershocks were counted as background, the decay would be biased steep. The
declustering rule — how events are assigned to the two populations — is therefore a
first-order modelling choice, not a preprocessing detail, and the fit must state
which rule was used (see ★★★8).

---

## ★★4 — The dispersion index of a clustered catalogue

**Poisson.** For $N(T) \sim \text{Poisson}(\lambda T)$ the mean and variance are
both $\lambda T$, so the index is exactly 1.

**Two-component catalogue.** Let $m_d$ be the day's *expected* count: $\lambda_0$
from the background, plus an aftershock contribution that is non-zero only near the
mainshock. By the law of total variance, with Poisson counts given $m_d$,

$$\mathrm{Var}(N_d) = \mathbb{E}\left[m_d\right] + \mathrm{Var}(m_d),
\qquad
\mathbb{E}[N_d] = \bar m ,$$

$$\text{index} = 1 + \frac{\mathrm{Var}(m_d) - \bar m}{\bar m} .$$

A burst therefore raises the index precisely through the day-to-day variance of the
rate.

**Illustration with a 5-day burst.** Put all $63$ aftershocks in five days
($\bar m_{\text{burst}} = 12.6$ events/day) and none elsewhere, $p = 5/3650 =
0.00137$:

$$\mathrm{Var}(m_d) = 0.00137 \times 12.6^2 - (0.00137\times12.6)^2
= 0.2176 - 0.0003 = 0.2173,$$

$$\bar m = 0.02 + 0.01726 = 0.03726, \qquad
\text{index} = 1 + \frac{0.2173 - 0.03726}{0.03726} = 5.83 .$$

**Against the measurement.** The measured index is $3.708$ on the true Omori
decay, which spreads the same $63$ events over tens of days rather than five. From
the measured variance, $\mathrm{Var}(m_d) = 0.1392 - 0.0200 = 0.1192$ and hence

$$\sum_d m_d^2 = 3650 \times (0.1192 + 0.01726^2) = 436.2\
(\text{events/day})^2,$$

against $\sum_d m_d^2 = 63 \times 0.01726 = 1.09$ if the same events were spread
uniformly. The measured sum is 400 times larger: a few days carry almost all of the
rate. The 5-day model overshoots because the real decay is gradual; the range
$3.7$–$5.8$ brackets the effect, and both are far from the Poisson value of 1.

---

## ★★5 — How many aftershocks resolve the exponent?

**Generator.** A single Omori sequence with known $(K, c, p)$, sweeping the number
of aftershocks $A \in \{20, 50, 100, 200, 500, 1000\}$ by scaling $K$ and keeping
$c$ and $p$ fixed. For each $A$ and each of $R = 200$ realisations: fit $p$ by
**maximum likelihood of the point process** (not by binning, which adds a
discretisation bias), and record $\hat p$ and the profile-likelihood interval.

**Metric.** The standard deviation of $\hat p$ across realisations, as a function
of $A$; report the linear regression of $\log \mathrm{SE}$ against $\log A$ and
check that its slope is $-0.5$.

**Sizing.** The demonstration's binned fit at $31$ events gives
$\mathrm{SE} = 0.130$. Under the $1/\sqrt{A}$ scaling, a three-standard-error
resolution of $\pm 0.05$ requires $\mathrm{SE} \le 0.0167$:

$$A \ge 31 \times \left(\frac{0.130}{0.0167}\right)^2
= 31 \times 60.6 \approx 1900\ \text{aftershocks} .$$

So **about 1 900 events**, i.e. sixty times the demonstration's sequence, are needed
to pin $p$ to a few hundredths — and that is for a *single, isolated* sequence with
the correct $c$ assumed. In practice one pools many sequences, which trades the
precision of a single fit for the assumption that they share parameters. Both the
pooled count and the assumed homogeneity belong in the report.

---

## ★★6 — Verifying a 30-day aftershock forecast

**Reference.** The climatological rate — the long-run mean rate of the same
catalogue, above the same magnitude threshold — expressed as a Poisson count for
the same 30-day window. It is the standard, free baseline of
[04 Forecast Evaluation](../04-forecast-evaluation.md).

**Metric for a rate forecast.** Two complements are needed:

1. a **proper scoring rule for counts**: the log-likelihood of the observed count
   under the forecast distribution, or the discrete CRPS/ranked probability score.
   Report it per window and averaged over windows;
2. **calibration of the probability**: the forecast $\Pr(\ge1)$ and $\Pr(\ge3)$
   against the observed frequency, in a reliability table with binomial intervals —
   the rate analogue of the coverage table in lesson 04.

Report a skill score only as a ratio of the proper scores, and state the reference:
a skill score against a climatology that ignores the mainshock is nearly guaranteed
to be positive, so the interesting reference is a *conditional* one (a standard
Omori forecast with textbook parameters), and the claim worth testing is
improvement over that.

**Split.** Estimate the model's parameters on sequences *other* than the ones being
verified; the verification windows come from held-out sequences, and the split must
be by sequence, never by window, because windows from one sequence share the same
conditioning event.

**Effective sample size.** The independent unit is the **sequence** (one mainshock
per forecast horizon), not the window: windows within a sequence are correlated
through the common mainshock and through the shared parameters. With $S$ held-out
sequences, the calibration tables have $S$ independent observations, so resolving a
probability to $\pm0.05$ at three standard errors needs about $S \ge 230$
sequences — which is why operational verification pools years of catalogue and
reports intervals rather than point comparisons.

---

## ★★★7 — Testing the Poisson assumption on a correct rate

**Construction.** Take the correct (or estimated) conditional rate $\lambda(t)$,
partition the catalogue into windows of fixed length $T$, and compute for each
window the expected count $\Lambda_i = \int_{T_i}\lambda\,\mathrm dt$ and the
observed count $N_i$. Under the non-homogeneous Poisson model the standardised
residuals

$$z_i = \frac{N_i - \Lambda_i}{\sqrt{\Lambda_i}}$$

should be approximately standard normal (for $\Lambda_i$ large enough) and
independent.

**Statistic and null.** The **number test**: $\chi^2 = \sum_i (N_i - \Lambda_i)^2 /
\Lambda_i$, which is $\chi^2_{n-1}$ under the null. The **dispersion test**: the
sample variance of $z_i$, which is 1 under the null with sampling variance
$2/(n-1)$.

**Departure expected.** If the process has clustering *beyond* the imposed rate —
secondary aftershocks, swarms, a time-varying background — then $\mathrm{Var}(z) >
1$ and $\chi^2 > n-1$: the window counts are over-dispersed relative to Poisson,
exactly as the demonstration's index of $3.708$ shows at daily resolution. If the
imposed rate is too smooth (an Omori law fitted with a wrong $p$), the departure is
also structured in time: the residuals run positive early and negative late, or
vice versa.

**Remedy, in order.** (i) A rate model with more structure — ETAS with secondary
triggering — so that the clustering is *in* the rate rather than in the residual;
(ii) a **negative binomial** (over-dispersed) count distribution for the residual
scatter, with the over-dispersion parameter estimated and reported, which fixes the
probabilities without fixing the physics; (iii) a **magnitude- or time-dependent
completeness correction** if the departure traces the detection threshold rather
than the Earth. The test to insist on is the variance of $z$, because it is the one
statistic that decides whether any quoted $\Pr(\ge1)$ is trustworthy.

---

## ★★★8 — Does the declustering rule change the exponent?

**Rules compared.** (i) **No declustering** — fit an ETAS-type model, or an Omori
law, to the whole catalogue, accepting that the background inflates the early rate;
(ii) **Gardner–Knopoff windows** — remove events inside space–time–magnitude windows
after each larger event; (iii) **nearest-neighbour declustering** — assign each
event to the parent that most likely triggered it, and keep the background set;
(iv) **Reasenberg** — a cluster-based rule with its own interaction parameters.

**Metric.** For each rule and each of $S$ independent synthetic catalogues with
known parameters: the estimated $(\hat K, \hat c, \hat p)$ with profile-likelihood
standard errors, the number of events assigned to the aftershock and background
populations, and the resulting 30-day forecasts.

**Result pattern that shows rule-dependence.**

| Pattern | Interpretation |
|---|---|
| $\hat p$ differs across rules by more than the within-rule standard errors, consistently, on the same catalogue | the parameters are **rule-dependent**: a statement about the analysis, not the Earth |
| $\hat p$ is stable across rules but differs between catalogues with different true parameters | the parameters are **Earth-dependent** |
| the rule-dependence grows as the background/aftershock ratio approaches 1 (here $53$ against $63$) | the ambiguity is greatest exactly where the two populations are comparable, which is the practical case |

The discriminating measurement is the *paired* one: apply all rules to the same
catalogue, and compare the differences with the paired uncertainty from the
bootstrap over sequences. A spread of $0.1$–$0.2$ in $\hat p$ across rules, against
individual standard errors of $0.05$, makes the parameters unusable without
declaring the rule — and the appropriate response is to report the spread across
rules as an additional uncertainty component, as one would for any nuisance choice.

---

## ★★★9 — A traffic-light protocol

**Statistic.** A trailing-window rate above a magnitude threshold, e.g. the number
of events with $M \ge M_c$ in the last 24 hours (a count) or the corresponding rate
in events/day. Prefer counts over a fixed window, because the count's null
distribution is known (Poisson) and its false-alarm rate is computable; a smoothed
rate introduces a bandwidth and a phase lag that both need justification.

**Calibration data.** Analogue sequences from similar settings, or a full
simulation study, used to set two thresholds (amber and red) such that (i) the
background catalogue crosses them at a specified rate and (ii) the sequences of
operational concern cross them within a specified time. Both requirements must be
stated, because they trade against each other.

**False-alarm control.** Specify the average run length: with a background of
$\lambda_0 = 0.02$ events/day, a 24-hour count threshold $k$ has a false-alarm
probability per day of $\Pr[N_{\text{day}} \ge k \mid \lambda_0]$, and the expected
number of false alarms per year is $365$ times that. For an operational target of
one false alarm per year, $k$ follows from $\Pr[N \ge k] \le 1/365 = 0.00274$ at
$\lambda_0 = 0.02$ — a threshold of $3$ events in a day (Poisson tail
$\approx 1.3\times10^{-3}$ per day at that rate). The arithmetic is the contract
with operations; the *rate* must be re-estimated as the network and the
induced activity change, or the false-alarm rate silently drifts.

**Response.** Escalation actions per colour, with a specified return-to-green rule
(for example, N days below the amber threshold), a named decision-maker, and a
documented log of every alarm with the data that triggered it — so that the
protocol's own performance can be audited later, which is the only way a
traffic-light scheme improves.

**The property that invalidates the whole scheme: catalogue incompleteness.**
A trailing-window rate is only observable above the network's detection threshold.
When a sequence begins, small events appear that the network may not detect
reliably; when a station is added or removed, the threshold changes. The observed
rate then moves for **instrumental** reasons, and a protocol keyed to the observed
rate will fire late during the onset of a sequence (the events are real but
undetected — actually an under-count) or spuriously after a network change (an
over-count). The scheme must therefore (i) key on a magnitude range demonstrably
complete at all times in the window, (ii) monitor network performance continuously
and record it beside every alarm, and (iii) freeze and re-estimate the thresholds
after any network change. A protocol without a completeness monitor measures the
network, not the Earth.
