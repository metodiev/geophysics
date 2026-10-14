# Solutions — 21-04-01 ML Taxonomy: Supervised, Unsupervised, Reinforcement

> Read after attempting. Lesson:
> [01 ML Taxonomy](../01-ml-taxonomy.md). Numbers quoted from the demonstration
> reproduce its output.

---

## ★1 — Classifying the tasks

| task | paradigm | label or reward |
|---|---|---|
| (a) porosity from a density log | supervised **regression** | measured core porosity |
| (b) grouping traces by waveform | **unsupervised** | none; the objective is internal |
| (c) deciding where to drill next | **reinforcement learning** | realised information or value of the well |
| (d) predicting detection | supervised **classification** | the observed binary detection outcome |

The dichotomy that matters is (b) against the rest: only in (b) is there no
external quantity against which the answer can be checked, so its validation must
be structural or geological.

---

## ★2 — Irreducible error versus measured error

With a perfect model the training MSE would be the noise variance,

$$\sigma^{2} = 0.3^{2} = 0.0900 .$$

The measured value is $0.0859$, **below** the irreducible level. That is not a
contradiction: the training MSE is computed on the same $200$ points used to fit
the parameters, so it is a downward-biased estimate of the true risk — the
optimiser has fitted part of the noise in this particular sample. The bias is of
order $p\sigma^{2}/n = 2\times0.09/200 = 0.0009$, which comfortably accounts for
the $0.0041$ gap together with sampling variation. The correct conclusion is that
the model has recovered the signal and the gap is the in-sample optimism that
[21-04-03](../03-model-assessment.md) exists to remove.

---

## ★3 — Successive reductions and the elbow

| transition | WCSS | reduction |
|---|---|---|
| $k = 2 \to 3$ | $1230.23 \to 303.25$ | $75.4\ \%$ |
| $k = 3 \to 4$ | $303.25 \to 260.47$ | $14.1\ \%$ |
| $k = 4 \to 5$ | $260.47 \to 223.85$ | $14.1\ \%$ |

The first reduction is five times the next two, so the **elbow is at $k = 3$** —
the true number of clouds. The remaining $14\ \%$ steps continue indefinitely,
which is why the objective alone cannot choose $k$ and a criterion such as the
silhouette or an information penalty is required.

---

## ★★4 — Empirical risk minimisation for two familiar models

$$\hat f = \arg\min_{f \in \mathcal F} \frac{1}{n}\sum_{i=1}^{n}
\ell\big(y_i, f(x_i)\big) + \lambda\,\Omega(f).$$

**(a) Ridge regression.** $\mathcal F$ = linear functions $f(x) = \beta_0 +
\beta^{\mathsf T}x$; $\ell = (y - f(x))^{2}$; $\Omega = \|\beta\|_2^{2}$.

**(b) Logistic regression with an $L_2$ penalty.** $\mathcal F$ = logistic
functions $p(x) = \sigma(\beta_0 + \beta^{\mathsf T}x)$; $\ell = -y\ln p -
(1-y)\ln(1-p)$; $\Omega = \|\beta\|_2^{2}$.

Both are convex in $\beta$ (the first quadratic, the second log-convex), so each
has a unique optimum and no local-minimum problem. That is the reason these two
remain the default baseline in every applied paper, including in geophysics.

---

## ★5 — Bandit regret

Optimal expected reward over $2000$ pulls at the best mean $0.65$:

$$2000 \times 0.65 = 1300 .$$

Measured reward $1269$, so

$$\text{regret} = 1300 - 1269 = 31, \qquad
\frac{31}{1300} = 2.38\ \% .$$

A policy that always pulled the best arm would have zero regret in expectation.
The $31$ units are the price of exploring: at $\epsilon = 0.10$ roughly $200$
pulls are spread over arms whose means are below $0.65$, and the average shortfall
of those arms is $(0.65-0.20 + 0.65-0.50 + 0.65-0.40)/3 = 0.283$, giving an
expected regret near $200\times0.283/1 \approx 57$ in the worst case — the
measured $31$ is lower because the greedy part of the policy mostly ignores the
weakest arm, so the exploration is not uniform in practice.

---

## ★6 — Coefficient recovery ratios

$$\frac{\hat\beta_1}{\beta_1} = \frac{0.9111}{1.2} = 0.759, \qquad
\frac{\hat\beta_2}{\beta_2} = \frac{-0.8054}{-0.8} = 1.007 .$$

The first coefficient is recovered at $76\ \%$ of its truth while the second is
recovered almost exactly. The asymmetry is not a bias in the estimator — maximum
likelihood is consistent — but a small-sample effect: with $n = 400$ and labels
drawn from the probabilities, the standard error of $\hat\beta_1$ is of order
$0.1$, so the observed deficit is about $2.9$ standard errors, plausible but
large. The two coefficients are also estimated jointly and their errors are
correlated, so one can be low while the other is on target. A single fit cannot
distinguish "small-sample fluctuation" from "misspecification"; that requires
either a larger $n$ or a Monte-Carlo study of the estimator's distribution.

---

## ★★★7 — Regret of three bandit policies

**Environment.** The demonstration's four-armed Bernoulli bandit with means
$(0.20, 0.50, 0.65, 0.40)$, horizon $T = 2000$ pulls.

**Policies.** (i) $\epsilon$-greedy with $\epsilon = 0.1$; (ii) upper confidence
bound, UCB1, choosing $\arg\max_a \big[\bar r_a + \sqrt{2\ln t / n_a}\big]$;
(iii) Thompson sampling with $\mathrm{Beta}(1 + \text{successes},
1 + \text{failures})$ posteriors and one draw per step.

**Replicates.** $M = 2000$ independent runs (different seeds) per policy; record
the cumulative regret $\sum_t (\mu^{*} - \mu_{a_t})$ and the mean over runs.

**Metric.** Mean regret at $T = 2000$ with its standard error, and the regret
curves versus $t$; the curves are the informative object, since the asymptotic
regret grows only logarithmically for UCB and Thompson and linearly for
$\epsilon$-greedy.

**Prediction.** At $T = 2000$: $\epsilon$-greedy regret of order $30$–$60$ units
(the demonstration measured $31$ for one run), UCB1 in the $10$–$20$ range, and
Thompson sampling similar to or slightly below UCB1. The ordering at short
horizons may reverse, since Thompson explores in proportion to posterior
uncertainty and is efficient early; reporting the curves rather than a single
number is what makes the comparison honest.

---

## ★★★8 — Does an unsupervised clustering recover the truth?

**Data-generating process.** Generate $J = 4$ facies as Gaussian clouds with
means on a $2$-D grid, covariances of a stated elongation and orientation, and
proportions $(\pi_1,\dots,\pi_4)$. Sample $n_j \sim \mathrm{Multinomial}$ counts.

**Algorithms.** $k$-means with $k$ fixed at the true $4$; Gaussian mixtures with
$k$ fitted by BIC; and agglomerative clustering with Ward linkage.

**External metric.** The adjusted Rand index between the recovered partition and
the true facies labels, and the cluster-to-facies confusion matrix. The Rand
index is external — it uses the labels the algorithm never saw — which is exactly
what an unsupervised method needs for validation.

**Replicates.** $M = 500$ data sets per configuration, sampling the proportions
and the covariances from stated ranges.

**The failure condition.** The clustering can post a *good* objective value and
still fail whenever the clouds are strongly elongated and interleaved: $k$-means
assigns points to the nearest mean, which cuts the elongated clouds across their
long axis, so the within-cluster sum of squares falls while the Rand index
against the truth falls too. The study's headline is the pair (objective,
Rand index) plotted against the elongation; the point where the objective keeps
improving while the Rand index deteriorates is the quantitative statement that a
low objective is not evidence of recovered structure.
