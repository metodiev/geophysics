# Solutions — 06-12-04 Traffic-Light Protocols, Monitoring and Mitigation

> **Read after attempting the exercises.** Numbers were computed; demonstration
> values are quoted directly.

Lesson: [04 Traffic-Light Protocols, Monitoring and Mitigation](../04-monitoring-and-mitigation.md).

---

## ★1 — Exceedance arithmetic

$$\text{rate}(M_t) = 100 \times 10^{-1.0(M_t-1.0)} .$$

**$M_t = 3.0$:** rate $= 100 \times 10^{-2} = 1.000\ \mathrm{yr^{-1}}$, and

$$P(\ge 1 \text{ in 1 yr}) = 1 - e^{-1.000} = 1 - 0.367879 = 0.6321 ✔$$

**$M_t = 4.0$:** rate $= 100 \times 10^{-3} = 0.100\ \mathrm{yr^{-1}}$, and

$$P(\ge 1 \text{ in 1 yr}) = 1 - e^{-0.100} = 1 - 0.904837 = 0.0952 ✔$$

Both match. Note what these numbers are: a statement about the *catalogue*. A
threshold at a magnitude whose rate is one per year will be tripped about once a
year whether the seismicity is induced or not — the arithmetic measures the
protocol's exposure, not the operation's effect.

---

## ★2 — Expected crossings

Expected crossings $=$ rate $\times$ programme length $\times$ sites.

| $M_t$ | rate (yr$^{-1}$) | 1 site, 10 yr | 20 sites, 10 yr |
|---|---|---|---|
| 2.0 | $10.000$ | $100.00$ | $2000.00$ |
| 3.0 | $1.000$ | $10.00$ | $200.00$ |

Both match the demonstration ($100.00/2000.00$ and $10.00/200.00$).

The dependence on the number of sites is **exactly linear**: with $S$ monitored
sites the expected number of red events is $S$ times the single-site value. That is
why a protocol calibrated at one site becomes a jurisdictional policy question at
twenty: the number that has to be acceptable to an operator is the basin-wide
count, not the per-site rate.

---

## ★3 — Expected maximum

$$E[M_{\max}] = M_c + \frac{\ln N + \gamma_E}{b\ln 10}
= 1.0 + \frac{\ln 1000 + 0.5772}{1.0 \times 2.302585}
= 1.0 + \frac{6.907755 + 0.5772}{2.302585} = 1.0 + \frac{7.484955}{2.302585}
= 1.0 + 3.2507 = 4.2507 .$$

The demonstration prints $4.251$ for the model and $4.249$ for the measured mean
over 20 000 simulated sequences ✔.

---

## ★4 — Events needed for a 50% chance

$$N_{50\%} \approx 0.693 \times 10^{b(M_t - M_c)} .$$

For $M_t = 5.0$, $b = 1$, $M_c = 1$:

$$N_{50\%} = 0.693 \times 10^{4} = 6930 ✔$$

matches the demonstration's table entry.

The exact expression is
$P(M_{\max} > M_t) = 1 - (1 - 10^{-b(M_t-M_c)})^N$; setting this to $0.5$ and using
$\ln(1-x) \approx -x$ for small $x$ gives $N \approx \ln 2 \times
10^{b(M_t-M_c)} = 0.693\times10^{b\Delta M}$.

The growth is **exponential in $\Delta M$**: each additional magnitude unit costs a
factor of $10^{b} = 10$ more events. So raising the threshold from 4 to 5 does not
halve the protection, it multiplies the waiting time by ten — and lowering the
threshold by 0.3 reduces the required events by only a factor of two. This is the
quantitative reason a protocol cannot be made safe by "collecting more data":
the required $N$ grows faster than any plausible injection programme can supply it.

---

## ★5 — The Gumbel spread

$$\text{spread} = \frac{1}{b\ln 10}\ln\!\left(\frac{\ln 0.05}{\ln 0.95}\right)
= \frac{1}{2.302585}\ln\!\left(\frac{-2.995732}{-0.051293}\right)
= \frac{\ln(58.4064)}{2.302585} = \frac{4.067755}{2.302585} = 1.7666 .$$

This matches the demonstration's $1.766$. The measured spreads $1.696$, $1.765$,
$1.771$ and $1.746$ for $N = 10 \ldots 10000$ fluctuate around it with no trend.

**What constancy means.** The uncertainty of the largest event does **not** shrink
as more events are recorded. A protocol that says "we will decide once we have seen
enough events" is waiting for a convergence that does not occur: a hundredfold
increase in $N$ moves the expected maximum by one magnitude unit and leaves the
5–95% spread unchanged. The only honest use of $N$ is in the *mean*, and the mean is
not the quantity a regulator cares about.

---

## ★6 — The missing Euler–Mascheroni term

Naive formula: $E[M_{\max}] \approx M_c + \log_{10}N/b$. With $N = 1000$,
$b = 1$: $1.0 + 3.0 = 4.000$.

Correct formula: $M_c + (\ln N + \gamma_E)/(b\ln 10) = 4.2507$ (★3).

Difference:

$$4.2507 - 4.0000 = 0.2507 \approx 0.251 ✔$$

The dropped term is $\gamma_E/(b\ln 10) = 0.5772/2.302585 = 0.2507$ — the
Euler–Mascheroni constant of the Gumbel limit. The naive version uses
$\log_{10}N$ in place of $\log_{10}N + \gamma_E/\ln 10$, i.e. it omits the
zero-mode of the extreme-value distribution. The offset is small in absolute terms
but it is systematic, and it grows as $1/b$: for $b = 0.8$ (a plausible induced
value) it becomes $0.313$ magnitude units, comparable to the difference between two
traffic-light thresholds.

---

## ★★★7 — Interior versus boundary optima (worked derivation)

$$\text{cost}(M_t) = c_{\text{trip}}\,\text{rate}(M_t)
+ c_{\text{dmg}}\,\lambda_{\text{dmg}}e^{-\text{rate}(M_t)W},
\qquad \text{rate}(M_t) = n_010^{-b(M_t-M_c)} .$$

Write $r \equiv \text{rate}(M_t)$. Since $r$ decreases monotonically with $M_t$, we
may optimise over $r$ and then invert. Differentiating,

$$\frac{\mathrm{d}\,\text{cost}}{\mathrm{d}r}
= c_{\text{trip}} - c_{\text{dmg}}\lambda_{\text{dmg}}We^{-rW}
= 0
\;\Longrightarrow\;
r^{*} = \frac{1}{W}\ln\!\left(\frac{c_{\text{dmg}}\lambda_{\text{dmg}}W}
{c_{\text{trip}}}\right).$$

An **interior** optimum exists iff $r^{*} > 0$, i.e. iff

$$\frac{c_{\text{dmg}}\lambda_{\text{dmg}}W}{c_{\text{trip}}} > 1 .$$

Otherwise the derivative has one sign everywhere and the optimum is at a boundary.

Checking the demonstration's pairs with $\lambda_{\text{dmg}} = 0.100\
\mathrm{yr^{-1}}$ and $W = 0.05\ \mathrm{yr}$:

| $c_{\text{trip}}$ | $c_{\text{dmg}}$ | ratio $c_{\text{dmg}}\lambda W/c_{\text{trip}}$ | optimum |
|---|---|---|---|
| $10^{6}$ | $10^{9}$ | $5.0$ | interior, $r^{*} = 32.19$, $M_t^{*} = 1.49$ |
| $10^{6}$ | $10^{10}$ | $50.0$ | interior, $r^{*} = 78.24$, $M_t^{*} = 1.11$ |
| $10^{7}$ | $10^{9}$ | $0.5$ | **boundary** |
| $10^{5}$ | $10^{10}$ | $500.0$ | interior in $r$, but $M_t^{*}$ falls below the tabulated range → boundary |
| $10^{6}$ | $10^{8}$ | $0.5$ | **boundary** |

For the two boundary cases the model says stopping at *every* event is cheaper than
any threshold: the cost of a stoppage is small relative to the damage avoided, and
$r^{*}<0$ means "there is no rate low enough that further raising the threshold
repays the lost warning".

The point of the exercise is that $c_{\text{trip}} = 10^{7}$ versus $10^{6}$ —
a tenfold change in one cost — removes the rationale for having a threshold at
all. A traffic-light threshold is therefore an output of a cost model, and the cost
model is a policy input, not a physical measurement.

---

## ★★★8 — Gumbel limit of the maximum (derivation)

**Setup.** Gutenberg-Richter gives, for magnitudes $\ge M_c$, the complementary CDF

$$P(M > m) = 10^{-b(m-M_c)},\qquad m \ge M_c .$$

For $N$ independent draws, $P(M_{\max} \le m) = \left[1 -
10^{-b(m-M_c)}\right]^{N}$.

**Step 1 — exponential form.** Let $y = 10^{-b(m-M_c)}$ so $m = M_c -
\log_{10}y/b$, and $P(M_{\max} \le m) = (1-y)^N$.

**Step 2 — tail limit.** Put $m = M_c + \dfrac{\ln N + x}{b\ln 10}$, i.e. choose the
scaling so that the maximum stays in the tail. Then
$y = 10^{-b(m-M_c)} = e^{-(\ln N + x)} = e^{-x}/N$, and

$$(1 - y)^{N} = \left(1 - \frac{e^{-x}}{N}\right)^{N}
\;\xrightarrow[N\to\infty]{}\;
\exp\!\left(-e^{-x}\right),$$

which is the standard Gumbel CDF.

**Step 3 — quantiles.** Solve $\exp(-e^{-x}) = q$ for $x$:
$x = -\ln(-\ln q)$. The 5% and 95% quantiles are
$x_{0.05} = -\ln(-\ln 0.05)$ and $x_{0.95} = -\ln(-\ln 0.95)$, and converting back
to magnitude units (divide by $b\ln 10$) gives the spread

$$\Delta = \frac{1}{b\ln 10}\left[\ln(-\ln 0.05) - \ln(-\ln 0.95)\right]
= \frac{1}{b\ln 10}\ln\!\left(\frac{\ln 0.05}{\ln 0.95}\right) = 1.7666 .$$

**Approximations used.** (i) Events are **independent** in magnitude and time —
real catalogues have aftershocks, which violate this and make the effective $N$
smaller. (ii) The limit is **asymptotic in $N$**: the demonstration's measured
spreads ($1.696$ at $N = 10$) show the fixed-$N$ corrections, which vanish only
slowly. Neither approximation affects the qualitative result that the spread does
not shrink with $N$.

---

## ★★★9 — What can and cannot be certified

**Can honestly be stated.**

1. **A catalogue statement.** Given the observed rate and $b$-value, the probability
   of at least one event above $M_t$ in a stated period is
   $1 - (1 - 10^{-b(M_t-M_c)})^N$ — the demonstration's §4 arithmetic, with its
   inputs printed.
2. **A stoppage statement.** The expected number of threshold crossings per site
   per year is rate$(M_t)$, and across the jurisdiction it is that number times the
   number of sites (★2).
3. **A compliance statement.** The protocol is an auditable rule: given the
   monitored magnitudes and the thresholds, whether the operator complied is a
   matter of record.

**Cannot honestly be stated.** "The project cannot produce an event above
magnitude 4." Nothing in the exceedance arithmetic contains a maximum magnitude:
every threshold can be exceeded given enough events (the demonstration's table
shows $P(M_{\max}>M_t)$ rising toward 1 with $N$ for every $M_t$), and the jump
from a statistical statement to a physical bound requires a mechanism — finite
fault area, finite available energy, finite stress drop — that the statistics do
not supply and about which the physically motivated models disagree. The honest
certification is a *probability* at a stated threshold over a stated period.

**Falsification.** The certification is falsified by a single well-located,
well-magnituded event above $M_t$ attributable to the operation, together with a
completeness demonstration that it could not have been detected-but-uncatalogued.
In practice the difficulty is the attribution, not the detection: see
[05 Case Studies](../05-case-studies-induced.md) for why the arrow from a
catalogue to a cause is the weakest link in the chain.
