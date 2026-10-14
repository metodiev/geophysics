# Solutions — 01-13-01 Probability Axioms, Conditional Probability and Bayes' Rule

> **Read this after attempting the exercises, not before.**
>
> These are worked solutions showing one valid route and the reasoning behind it.
> Where a numeric answer is given it was computed, not estimated by hand. Where a
> probability is quoted to four decimal places, the rounding is stated. Several
> problems have more than one defensible answer once an assumption is introduced;
> where that is so, the assumption is named.

---

## ★1 — Two independent alarms

With $P(A) = 0.9$ and $P(B) = 0.8$ and independence, $P(A \cap B) = 0.72$.

**(a) Neither triggers.**

$$P(A^{c} \cap B^{c}) = P(A^{c})P(B^{c}) = 0.1 \times 0.2 = \boxed{0.0200}$$

**(b) At least one triggers.** By the complement rule, with the complement of "at
least one" being "neither":

$$P(A \cup B) = 1 - 0.02 = \boxed{0.9800}$$

Check by inclusion–exclusion: $0.9 + 0.8 - 0.72 = 0.98$. The two routes agree, as
the axioms require.

**(c) Exactly one triggers.** The event is $(A \cap B^{c}) \cup (A^{c} \cap B)$,
a union of disjoint events, so the probabilities add:

$$P(\text{exactly one}) = 0.9 \times 0.2 + 0.1 \times 0.8 = 0.18 + 0.08 =
\boxed{0.2600}$$

**What to notice.** Adding a second alarm raised the detection probability only
from $0.90$ to $0.98$, because what independence squares is the *miss*
probability, here $0.10$. Redundancy pays best when the individual miss probability
is already small, and the same arithmetic is why three stations are worth much less
than a third station on top of two.

---

## ★2 — Exploration prospects

The counts define everything; no probabilities need to be assumed.

| | Target | No target | Total |
|---|---|---|---|
| Anomaly | 34 | 24 | 58 |
| No anomaly | 6 | 136 | 142 |
| Total | 40 | 160 | 200 |

**(a)** $P(\text{anomaly}) = 58/200 = \boxed{0.2900}$.

**(b)** $P(\text{target} \mid \text{anomaly}) = 34/58 = \boxed{0.5862}$.

**(c)** $P(\text{anomaly} \mid \text{target}) = 34/40 = \boxed{0.8500}$ (this is the
sensitivity of the method).

**(d)** The decision to drill needs (b): given that we saw an anomaly, how likely is
a target? A forward model gives (c): given a target, how likely is an anomaly. The
two differ by a factor of $0.8500/0.5862 = 1.45$ in this example — and in exploration
the factor is usually far larger, because targets are far rarer than in this
data set. The conversion from (c) to (b) is Bayes' rule, and the missing ingredient
is the prior $P(\text{target}) = 0.20$, which is unusually high here precisely
because these 200 prospects were preselected.

---

## ★3 — Axiom arithmetic

**Union.**

$$P(A \cup B) = P(A) + P(B) - P(A \cap B) = 0.4 + 0.5 - 0.15 = \boxed{0.7500}$$

**Neither.** By De Morgan, $A^{c} \cap B^{c} = (A \cup B)^{c}$, so

$$P(A^{c} \cap B^{c}) = 1 - 0.75 = \boxed{0.2500}$$

**Only $A$.** $A \cap B^{c}$ is disjoint from $A \cap B$, and their union is $A$:

$$P(A \cap B^{c}) = P(A) - P(A \cap B) = 0.4 - 0.15 = \boxed{0.2500}$$

**A sanity check worth doing.** All four cells of the $2 \times 2$ table must sum to
one: $P(A \cap B) = 0.15$, $P(A \cap B^{c}) = 0.25$, $P(A^{c} \cap B) = 0.35$,
$P(A^{c} \cap B^{c}) = 0.25$. The sum is $1.00$. Building the table is often faster
and safer than applying formulae one at a time.

---

## ★4 — Three hypotheses

**Evidence**, by the law of total probability:

$$P(d) = 0.20(0.60) + 0.30(0.30) + 0.50(0.10) = 0.12 + 0.09 + 0.05 =
\boxed{0.2600}$$

**Posteriors**, each prior times likelihood divided by the evidence:

| Hypothesis | Prior | Likelihood | Prior × Likelihood | Posterior |
|---|---|---|---|---|
| $H_1$ | 0.20 | 0.60 | 0.12 | $0.12/0.26 = 0.4615$ |
| $H_2$ | 0.30 | 0.30 | 0.09 | $0.09/0.26 = 0.3462$ |
| $H_3$ | 0.50 | 0.10 | 0.05 | $0.05/0.26 = 0.1923$ |

The posteriors sum to $1.0000$, which is the arithmetic check that the evidence was
computed correctly. The most dramatic change is $H_3$: prior $0.50$, posterior
$0.19$. A hypothesis can lose to two others without either of them becoming
dominant — which is the honest description of an ambiguous dataset.

---

## ★5 — Sequential updating in odds form

**Posterior odds = prior odds × likelihood ratio**, and for independent measurements
the likelihood ratios multiply:

$$\text{posterior odds} = \frac{1}{3} \times 5 \times 2 = \frac{10}{3} =
\boxed{3.3333}$$

**Posterior probability.** For odds $a{:}b$ the probability is $a/(a+b)$:

$$P(H_1 \mid d_1, d_2) = \frac{10}{10 + 3} = \boxed{0.7692}$$

**Check by the long route.** Updating once: prior $P(H_1) = 1/4 = 0.25$, and with
likelihood ratio $5$ the posterior odds are $5/3$, so $P(H_1) = 5/8 = 0.625$. Updating
again with likelihood ratio $2$: odds $\frac{5}{3}\times 2 = \frac{10}{3}$, hence
$P = 10/13 = 0.7692$. The orders give the same answer, because multiplying the three
numbers is commutative.

**A caution that the exercise is designed to provoke.** The two likelihood ratios
were given as independent. If the two measurements were made by the same analyst on
the same record, treating them as independent overstates the evidence by an amount
equal to the correlation between them, and $0.7692$ is then too confident.

---

## ★6 — Screening at low prevalence

**(a)** With $\pi = 0.002$, $\text{Se} = 0.98$, $\text{Sp} = 0.95$:

$$P(+) = 0.98(0.002) + 0.05(0.998) = 0.00196 + 0.0499 = \boxed{0.0519}$$

$$\text{PPV} = \frac{0.00196}{0.05186} = \boxed{0.0378}$$

Fewer than four positives in a hundred are real. The false positives come from the
$0.998$ of the population without the target multiplied by the $5\%$ false-positive
rate: $0.0499$, which is twenty-five times the true-positive contribution $0.00196$.

**(b)** Set the PPV to $0.5$:

$$\frac{\text{Se}\,\pi}{\text{Se}\,\pi + (1-\text{Sp})(1-\pi)} = 0.5
\ \Longrightarrow\ \text{Se}\,\pi = (1-\text{Sp})(1-\pi).$$

Solving for the false-positive rate,

$$1 - \text{Sp} = \frac{\text{Se}\,\pi}{1-\pi} = \frac{0.98 \times 0.002}{0.998}
= 0.001964,$$

so

$$\text{Sp} = 1 - 0.001964 = \boxed{0.9980}$$

**Reading the answer.** To make half of the positives real, the false-positive rate
must fall from $5\%$ to $0.2\%$ — a factor of $25$ — while sensitivity is held fixed.
The requirement is set by the ratio $\pi/(1-\pi)$, not by the sensor's quality as
usually advertised. This is the arithmetic behind the cost of screening programmes
for rare conditions, and it applies unchanged to rare geophysical targets.

---

## ★7 — A detector on a large grid

Expected false alarms:

$$0.02 \times 10^{6} = 20\,000.$$

Expected true detections: $10$ (detection rate $1.0$).

$$\text{PPV} \approx \frac{10}{10 + 20\,000} = \boxed{0.0005}$$

One in two thousand positives is real. The per-cell test is not useless — it reduces
the search area by a factor of $2000$ — but the phrase "the detector fired" carries
essentially no information about a specific cell, and the follow-up budget, not the
detector's sensitivity, determines whether the programme is viable. The correct
response is to raise the threshold until the expected number of false alarms is
comparable with the expected number of targets, and to accept the loss of sensitivity
that this entails, or to exploit spatial coherence: genuine targets cluster, and
false alarms do not, which is a physical argument that Bayes' rule alone cannot
supply.

---

## ★8 — Correlated detectors

$$P(A \cup B) = P(A) + P(B) - P(A \cap B) = 0.85 + 0.85 - 0.80 = \boxed{0.9000}$$

Under independence the value was $1 - 0.15^{2} = 0.9775$. The shared power supply
costs $0.9775 - 0.9000 = \boxed{7.75}$ percentage points of detection probability,
even though each station individually performs exactly as specified.

**The general statement.** Redundancy is only as good as the independence of its
failure modes. Two stations on the same power supply, the same communications link
and the same processing pipeline behave, for the purposes of the failure they share,
like one station. The design question is not "how many stations?" but "which
failures are shared between them?" — a question about the acquisition architecture,
not about the physics.

---

## ★9 — Deriving the PPV formula

**Derivation.** Let $T$ be the event "target present" and $+$ the event "test
positive". The definitions are $P(+ \mid T) = \text{Se}$, $P(- \mid T^{c}) =
\text{Sp}$ and $P(T) = \pi$. Bayes' rule gives

$$P(T \mid +) = \frac{P(+ \mid T)P(T)}{P(+)}.$$

The denominator, by the law of total probability over the partition
$\{T, T^{c}\}$,

$$P(+) = P(+ \mid T)P(T) + P(+ \mid T^{c})P(T^{c})
= \text{Se}\,\pi + (1 - \text{Sp})(1 - \pi),$$

using $P(+ \mid T^{c}) = 1 - P(- \mid T^{c}) = 1 - \text{Sp}$. Substituting,

$$\text{PPV} = \frac{\text{Se}\,\pi}{\text{Se}\,\pi + (1 - \text{Sp})(1 - \pi)}.
\qquad \blacksquare$$

**(i) Monotonicity in Sp.** Differentiate with respect to $\text{Sp}$. Writing
$D$ for the denominator, $\partial D/\partial\text{Sp} = -(1-\pi)$ and

$$\frac{\partial \text{PPV}}{\partial \text{Sp}}
= -\frac{\text{Se}\,\pi}{D^{2}}\frac{\partial D}{\partial \text{Sp}}
= \frac{\text{Se}\,\pi (1-\pi)}{D^{2}} > 0,$$

so PPV increases with specificity for any $0 < \pi < 1$ and $\text{Se} > 0$.

**(ii) The limit of vanishing prevalence.** As $\pi \to 0$ with Se and Sp fixed, the
numerator is $O(\pi)$ while the denominator tends to $1 - \text{Sp}$, a positive
constant (unless $\text{Sp} = 1$). Hence PPV $\to 0$ linearly in $\pi$. Rare targets
are hard for a structural reason, not because instruments are imperfect.

**(iii) When PPV reaches one.** The PPV equals $1$ if and only if the second term in
the denominator vanishes, that is if $(1-\text{Sp})(1-\pi) = 0$, so either
$\text{Sp} = 1$ or $\pi = 1$. Perfect specificity makes every positive real;
no false-positive path exists. Ubiquitous target makes the question vacuous.

**Operational meaning of the large derivative.** When $\pi$ is small, $\partial
\text{PPV}/\partial\text{Sp} = \text{Se}\,\pi(1-\pi)/D^{2}$ is large in absolute terms
only because $D$ is small, and small changes in specificity move the PPV a great
deal. Concretely, in ★6 raising specificity by $0.048$ moved the PPV from $0.038$ to
$0.5$ — a change of more than a factor of ten. Effort spent on the false-positive
rate is therefore worth an order of magnitude more than the same effort spent on
sensitivity, whenever the target is rare.

---

## ★10 — Designing a Monte Carlo check

**Required number of positives.** With a relative standard error target of $r = 0.01$
and the stated approximation,

$$r^{2} = \frac{1}{P}\frac{1 - \text{PPV}}{\text{PPV}}
\ \Longrightarrow\ P = \frac{1 - \text{PPV}}{\text{PPV}\,r^{2}}.$$

With $\text{PPV} = 0.037794$ from ★6(a),

$$P = \frac{0.962206}{0.037794 \times 10^{-4}} = 2.5460\times10^{5}.$$

**Trials required.** Each trial is positive with probability $P(+) = 0.05186$, so

$$N = \frac{P}{P(+)} = \frac{2.5460\times10^{5}}{0.05186} = 4.9098\times10^{6}.$$

**Assumptions, stated explicitly.**

1. $T \mid P$ is binomial with parameters $(P, \text{PPV})$, so
   $\operatorname{Var}(T/P) \approx \text{PPV}(1-\text{PPV})/P$ by the delta method.
2. The relative standard error of the PPV estimate is dominated by the binomial
   variation of $T$; the variation in $P$ itself contributes at the same order and
   would need the variance of the ratio of two random quantities, which is a
   second-order correction at these numbers.
3. Trials are independent, and the outcome of one trial does not affect the
   population composition. In a real exploration programme it does — a discovered
   prospect is removed from the pool — which is why simulation studies of this kind
   are used for checking arithmetic rather than for operational forecasting.

**Why not a round number.** Choosing "$10^{6}$ trials because it looks large" gives a
relative standard error of about $2.2\%$, which is enough to detect a gross error in
the formula and not enough to check it to the precision quoted. Deriving the count
from the required precision, the way the power calculation of
[01-13-08](../08-hypothesis-testing.md) derives a sample size, makes the cost of the
claim explicit: five million trials to pin one probability to one per cent. That is
the honest price.

---

## ★11 — A precursor claim

Let $E$ denote a large event on a given day and $\text{Pr}$ a precursor signal on
that day. The base rate of large events is

$$P(E) = \frac{400}{30\,000} = 0.013333.$$

**(a) Probability of a precursor on a randomly chosen day.** Using the claimed
detection rate $P(\text{Pr} \mid E) = 0.60$ and the quiet-day rate
$P(\text{Pr} \mid E^{c}) = 0.02$, the law of total probability gives

$$P(\text{Pr}) = 0.60(0.013333) + 0.02(0.986667) = 0.008000 + 0.019733
= \boxed{0.027733}.$$

**(b) Probability of a large event on a precursor day.** By Bayes' rule,

$$P(E \mid \text{Pr}) = \frac{P(\text{Pr} \mid E)P(E)}{P(\text{Pr})}
= \frac{0.008000}{0.027733} = \boxed{0.288462}.$$

**(c) Why this is the quantity that matters.** The base rate $P(E) = 0.013333$ is what
a decision-maker faces without the precursor. The claim raises it to $0.2885$, a lift
of a factor of $21.6$ — a genuinely large lift, and far from useless. But it is not
$0.60$, and the two are different questions: $0.60$ is the *detection rate*
$P(\text{Pr} \mid E)$, and $0.2885$ is the *predictive value* $P(E \mid \text{Pr})$.
Only the second supports a decision to act on a precursor.

**Which assumption is least credible.** The calculation of $P(\text{Pr})$ treats the
precursor rate on quiet days as independent of the event rate, which is exactly the
hypothesis under test. If precursors are caused by the same tectonic loading that
produces events, the quiet-day rate is not $0.02$ but a spatially and temporally
varying quantity, and a catalogue assembled by searching many regions and windows
will have a much higher effective false-signal rate than the nominal $2\%$ — the
multiplicity problem of [01-13-08](../08-hypothesis-testing.md) Section 6 in a
different guise. The detection rate quoted in the claim is also almost always
estimated on the same data used to search for the precursors, which biases it upward.
Both corrections reduce $P(E \mid \text{Pr})$, and neither can be made from the
numbers given. The correct conclusion is that the claimed $60\%$ is not the quantity
that would justify action, and the quantity that would justify action has not been
estimated.
