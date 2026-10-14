# Solutions — 06-11-03 Why Deterministic Prediction Is Considered Unattainable

> Read after attempting the exercises. Numbers were computed from the relations of
> the lesson. All values are **SYNTHETIC**.

Lesson: [03 Prediction Limits](../03-earthquake-prediction-limits.md).

---

## ★1 — the exponential wait distribution

**(a)** $P(\text{event in }40\ \mathrm{yr}) = 1 - e^{-40/400} = 1 - e^{-0.1}
= 1 - 0.9048 = 0.0952$.

**(b)** $P(\text{no event in }400\ \mathrm{yr}) = e^{-1} = 0.3679$. Just over a
third of 400-year intervals contain no event, even though the mean recurrence is
exactly 400 years.

**(c)** By memorylessness the expected additional wait is the full mean recurrence,
**400 years** — not less, and not dependent on the 200 years already elapsed. The
demonstration measures a mean excess of 199.79 yr against a theory of 200.00 yr on
its 200-year-recurrence process, confirming the same statement numerically.

---

## ★2 — resolution of a b-value difference

$$\sigma_{\Delta b} \approx b\sqrt{\frac{2}{N}}
= 1.00\sqrt{\frac{2}{200}} = 1.00\times0.1000 = 0.1000.$$

A 2-s.e. difference is $2\times0.1000 = 0.20$. So a reported b-value difference
between two 200-event windows must exceed 0.20 before it is worth discussing —
this is the $\sqrt N$ penalty of [lesson 01](01-gutenberg-richter-solutions.md)'s
sample-size arithmetic.

---

## ★3 — Bayes with a weaker test

$$P(E\mid A) = \frac{P(A\mid E)P(E)}
{P(A\mid E)P(E) + P(A\mid\bar E)P(\bar E)}
= \frac{0.60\times8.210\times10^{-4}}
{0.60\times8.210\times10^{-4} + 0.10\times0.99918}.$$

Numerator: $4.926\times10^{-4}$. Denominator:
$4.926\times10^{-4} + 0.099918 = 0.100411$.

$$P(E\mid A) = \frac{4.926\times10^{-4}}{0.100411} = 4.91\times10^{-3},
\qquad \text{gain} = \frac{4.91\times10^{-3}}{8.210\times10^{-4}} = 5.98.$$

Doubling the false-alarm probability from 0.05 to 0.10 halves the gain from 11.9 to
6.0: **the false-alarm rate is the binding constraint, not the sensitivity.**

---

## ★4 — is CV = 0.85 from 50 intervals evidence?

The 5%–95% range for $n = 50$ under the Poisson null is $0.790$–$1.217$, and
$P(\mathrm{CV} < 0.8) = 0.060$. A measured $0.85$ is:
(i) inside the 90% range, and (ii) *above* the value that 6% of Poisson samples fall
below. It is therefore entirely consistent with Poisson: no evidence of
quasi-periodic recurrence.

To change the answer one would need either a value below $0.790$ with those 50
intervals (i.e. in the lower 5% tail), or a much larger number of intervals — the
table shows the range tightening to $0.886$–$1.113$ at $n = 200$. Note also that a
genuinely quasi-periodic sequence has a *theoretical* CV below 1; data can only
detect that if the intervals are numerous enough that the Poisson range is
narrower than the effect.

---

## ★5 — posterior, gain and alarm fraction

With $P(E) = 1.0\times10^{-3}$, sensitivity $0.80$, false-alarm probability
$0.01$:

$$P(E\mid A) = \frac{0.80\times10^{-3}}{0.80\times10^{-3} + 0.01\times0.999}
= \frac{8.00\times10^{-4}}{8.00\times10^{-4} + 9.99\times10^{-3}}
= \frac{8.00\times10^{-4}}{1.079\times10^{-2}} = 0.0741.$$

Gain $= 0.0741/10^{-3} = 74.1$.

Alarm fraction:
$\nu = 0.80\times10^{-3} + 0.01\times0.999 = 1.079\times10^{-2}$, i.e. the test is
in alarm 1.1% of the time.

So the honest headline is: **"a 74-fold rate increase, held for 1.1% of the
time"** — not "a 7% chance of an earthquake".

---

## ★6 — twenty tests at the 5% level

Each test rejects with probability 0.05 under the null, independently:

$$P(\text{at least one flag}) = 1 - (1 - 0.05)^{20} = 1 - 0.95^{20}
= 1 - 0.3585 = 0.642.$$

Nearly two chances in three that pure noise produces at least one "significant"
precursor when 20 series are examined. The demonstration measures the same
mechanism at 500 series (21 flagged, 4.2%).

**Consequence:** the claim must be reported together with the number of series
examined and the search protocol, and the appropriate $p$-value must be corrected
for multiplicity — or, better, the precursor must be tested prospectively on data
that did not contribute to its discovery.

---

## ★7 — specification of a prospective test

**Forecast format.** A *rate* forecast, not a binary alarm: for each forecast
window (say 30 days) and each target region, state
$\hat\lambda$ for $M\ge M_0$ from the precursor model and from the baseline model,
plus the information gain $\log_2(\hat\lambda_\text{prec}/\hat\lambda_\text{base})$.

**Alarm budget.** Pre-declare the fraction of time the model will be in the
"elevated" state, e.g. $\nu \le 5\%$ per year. A binary alarm with no stated
fraction is unfalsifiable: an always-on alarm "predicts" every event and carries
probability gain 1.

**Score.** Use a likelihood-based score (for example the log-likelihood ratio of
the observed event count under the forecast rate versus the baseline rate,
summed over windows), reported with an interval, plus the Molchan-style pair
(alarm fraction $\nu$, miss rate $\tau$). Declare the score before the data are
seen.

**Evaluation period.** Long enough to accumulate events: for a $0.01\ \mathrm{yr^{-1}}$
target, ten events take of order 1000 years of regional exposure, so the test must
aggregate many regions, and the aggregation rule itself must be pre-declared.

**Failure criterion.** State in advance what would falsify the precursor: for
example, information gain per window not distinguishable from zero at the 5% level
after the pre-declared period, or a score below the baseline.

**Why a bare alarm cannot be evaluated:** without the alarm fraction, the pair
(sensitivity, false-alarm probability) is unidentified; the same hit rate can come
from a 1%-of-time alarm with a real precursor or a 100%-of-time alarm with none.
The gain and the alarm fraction must be reported together, as in Section 4 of the
lesson.

---

## ★8 — the false-alarm probability for a 90% posterior

Setting the posterior to $0.9$ with sensitivity $0.50$ and prior $p = 10^{-3}$,
solve for the false-alarm probability $f$:

$$0.9 = \frac{0.5\,p}{0.5\,p + f(1-p)}
\;\Longrightarrow\;
f = \frac{0.5\,p\,(1-0.9)}{0.9\,(1-p)}
= \frac{0.5\times10^{-3}\times0.1}{0.9\times0.999}.$$

Numerator $= 5.0\times10^{-5}$; denominator $= 0.8991$:

$$f = 5.56\times10^{-5} \;\approx\; 1\ \text{false alarm in } 18\,000
\text{ quiet windows}.$$

**Why more data does not fix deterministic prediction.** In the Bayes expression
the prior enters only through $P(E)$ — the probability that the *next window*
contains the event. It is set by the tectonic rate and the length of the window,
not by the size of the catalogue. A larger catalogue sharpens the *test's*
parameters (sensitivity and $f$ can be estimated more precisely) but it cannot
raise $P(E)$ for a short window, and the algebra above shows that the required $f$
is proportional to $P(E)$ itself. Making the window longer raises $P(E)$, but a
longer window is no longer a prediction of a particular day.

**Why a rate forecast is different.** An aftershock forecast's baseline rate is
*itself* observable in the same catalogue: the ETAS parameters $(K, \alpha, p, c)$
are estimated from many sequences, each sequence adding information, so the
predicted rate converges on the truth. Its score is an average over a population of
windows, so it can be improved by accumulating data — the same mechanism that makes
the Section 6 rate ratio (about 1300× on the first day) checkable and correctable.
