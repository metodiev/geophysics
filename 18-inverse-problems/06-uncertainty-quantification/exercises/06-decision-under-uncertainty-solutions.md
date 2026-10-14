# Solutions — 18-06-06 Decision-Making Under Uncertainty and Value of Information

> Read after attempting the exercises. Numbers were computed, not estimated.
> Lesson: [06 Decision-Making Under Uncertainty and Value of Information](../06-decision-under-uncertainty.md).

---

## ★1 — Break-even volume

Acting gives $P V - C$, not acting gives $0$. Taking expectations under the posterior,

$$
\mathbb{E}[P V - C] = P\,\mathbb{E}[V] - C > 0
\ \Longleftrightarrow\
\mathbb{E}[V] > \frac{C}{P} = V^{*} .
$$

The rule is stated on the **posterior mean**, not on the exceedance probability.
The two agree only for a symmetric posterior about $V^{*}$.

---

## ★2 — Why the EVPI cannot be negative

$$
\text{EVPI} = \mathbb{E}_V\bigl[\max_a \text{value}(a,V)\bigr]
- \max_a \mathbb{E}_V\bigl[\text{value}(a,V)\bigr] .
$$

For every $V$, $\max_a \text{value}(a,V) \ge \text{value}(a_0,V)$ where $a_0$ is the
Bayes action. Taking expectations, $\mathbb{E}[\max_a \text{value}] \ge
\mathbb{E}[\text{value}(a_0,V)] = \max_a\mathbb{E}[\text{value}]$, so the difference
is non-negative. Knowing the truth can never hurt a decision maker who then acts
optimally.

---

## ★3 — Cost-loss ratio

$$
p^{*} = \frac{C}{L} = \frac{5}{50} = 0.1000 .
$$

Protect when the posterior probability of the hazard exceeds $0.1$; do not protect
below it. At exactly $0.1$ the two actions have the same expected cost ($5$ either
way), so the decision is indifferent and information has its maximum value there.

---

## ★★4 — Expected value and the action

$$
\mathbb{E}[V] = \exp\!\left(\ln 8 + \tfrac{0.6^{2}}{2}\right)
= 8\,e^{0.18} = 8 \times 1.197217 = 9.577737 .
$$

$$
\mathbb{E}[\text{value}] = 5(9.577737) - 20 = 47.888687 - 20 = 27.888687,
$$

$$
V^{*} = \frac{C}{P} = \frac{20}{5} = 4.0000 .
$$

Since $\mathbb{E}[V] = 9.5777 > 4.0000$, the action is taken. Note that
$P(V > V^{*}) = 0.8760$ as well, so in this case the two criteria agree — they need
not, and they disagree at cost $48$ where $P(V>V^{*}) = 0.3806$ but the decision is
negative.

---

## ★★5 — Certainty equivalent under risk aversion

The expected value is $27.8887$ and the certainty equivalent is $9.3700$: a decision
maker with $A = 0.1$ values the lottery exactly as they would value $9.37$ in cash,
about a third of its expected value. The difference is the **risk premium**,
$27.8887 - 9.3700 = 18.5187$ currency units, which that decision maker would pay to
avoid the downside (a certain loss of the drilling cost with probability $0.124$).

The risk tolerance is

$$
\frac{1}{A} = \frac{1}{0.1} = 10\ \text{currency units} .
$$

The demonstration locates the flip in the action by bisection at the much larger
$A = 0.30164$, i.e. a risk tolerance of $3.315$ units.

---

## ★★6 — Why the EVSI is zero at cost 20 and positive at cost 48

At cost $20$ the break-even volume is $V^{*} = 4.0$. Every conditional mean in the
table exceeds it — $\mathbb{E}[V\mid\text{signal}]$ ranges from $10.03$ to $14.26$
and $\mathbb{E}[V\mid\text{no signal}]$ from $6.65$ to $9.13$, all above $4.0$. Since
the optimal action is *drill* in both branches, the information cannot change the
action, and

$$
\text{EVSI} = \sum_s P(s)\max_a \mathbb{E}[\text{value}\mid a,s]
- \max_a \mathbb{E}[\text{value}\mid a] = 0 .
$$

At cost $48$ the break-even is $9.6$; the positive-signal branch has
$\mathbb{E}[V\mid\text{signal}]$ above it and the negative-signal branch below it, so
the signal flips the action and the EVSI is positive — from $1.0489$ at a
$55\%$-accurate sensor to $8.9430$ at $90\%$, against a perfect-information value of
$11.2508$.

---

## ★★7 — Why the EVPI rises with the cost

The EVPI is the gain from resolving the uncertainty *before* choosing. At cost $20$
the project is comfortably profitable: the decision is to drill regardless, so
resolution changes nothing and the EVPI is $0.58$ — the small residual comes from the
region where $V$ is so low that drilling would not be worth it even though the mean
says it is. At cost $48$ the expected value is $-0.1113$, essentially at the
indifference point: knowing $V$ would let the decision maker drill in the profitable
realisations and decline in the loss-making ones, and that option is worth $11.25$.

**Conclusion for a decision maker:** information is worth buying where the decision
is close to indifferent. Where the decision is already clear, no survey can improve
it; where it is deeply unfavourable, the survey is worth at most the value of
avoiding the residual risk, which is small. The most valuable information is
purchased at the margin.

---

## ★★8 — Value of information for a monitoring network

- **Actions:** no action; increase monitoring and inspection; shut in and remediate.
- **States:** the size and location of a leak or induced event, summarised by a scalar
  (for example an annual probability of exceeding a regulatory threshold).
- **Loss function:** regulatory penalty plus remediation cost plus reputational cost,
  all stated numerically, with the option of a risk-averse utility if the operator's
  behaviour suggests one.
- **Candidate designs:** the existing network, plus $k$ additional stations at
  candidate locations, characterised by their detection sensitivity and specificity
  from a transport model.
- **Computation:** for each design, draw the state from the prior; simulate the
  sensor responses with the stated reliability; form the posterior by reweighting (or
  by an explicit likelihood if the sensor model is analytic); compute the Bayes action
  and its expected loss; average over designs and states. The EVSI of a design is the
  reduction in expected loss relative to the current network, minus the network's
  cost.
- **Reporting:** per design, the EVSI with its Monte Carlo standard error, the
  sensitivity of the ranking to the assumed sensor reliability, and the decision the
  information would change.

**How the study could be wrong despite correct arithmetic:** if the loss function is
wrong — a penalty set to a nominal value that does not reflect the operator's real
exposure — the ranking of designs can be inverted. EVSI is a property of the loss
function, so an arithmetic error is the least likely failure.
