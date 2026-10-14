# Exercises — 01-13-07 Confidence Intervals and Their Correct Interpretation

Attempt these closed-book before reading
[the solutions](./07-confidence-intervals-solutions.md). The lesson is
[01-13-07](../07-confidence-intervals.md).

Marking: ★ foundational, ★★ applied, ★★★ research-oriented.

State the coverage property explicitly in every answer about interpretation.

---

## ★ Foundational

**★1.** A mean of $12$ is computed from $n = 25$ observations with known
$\sigma = 4$. Construct the $95\%$ two-sided confidence interval and state its width.

**★2.** How many observations are needed for the $95\%$ interval of ★1 to have a
half-width of $0.5$ with the same $\sigma$?

**★3.** A mean of $20$ and a sample standard deviation of $3$ come from $n = 10$
observations. Construct the $95\%$ interval, stating the degrees of freedom and the
critical value used. Comment on how much wider it is than the known-$\sigma$ interval.

**★4.** Mark each statement true or false and justify in one sentence:

(a) There is a $95\%$ probability that the true parameter lies in the realised
$95\%$ interval.
(b) If the experiment were repeated many times, $95\%$ of the intervals constructed
would contain the parameter.
(c) A $99\%$ interval is wider than a $95\%$ interval built from the same data.
(d) An interval that does not contain zero proves the absence of an effect.

---

## ★★ Applied

**★★5.** An instrument has a systematic offset of $+0.3$ units, reading noise
$\sigma = 1$, and $n = 25$ readings are averaged. Using the normal approximation with
half-width $1.96\sigma/\sqrt n$, compute the probability that the interval covers the
true value. Explain the direction of the failure and what happens as $n$ grows.

**★★6.** A dataset is believed to follow a Pareto distribution with tail exponent
$\alpha = 2.5$. State whether the sample standard deviation is a suitable basis for a
confidence interval, and explain the role of the fourth moment in your answer.

**★★7.** Two independent experiments estimate the same quantity. Experiment A gives
$10.0 \pm 1.0$ and experiment B gives $12.0 \pm 1.0$ (both $95\%$ intervals). Do the
intervals overlap? Compute the interval for the difference and state whether the
difference is significant at $5\%$. Comment on the practice of comparing intervals
by eye.

**★★8.** A depth is $d = vT/2$ with $v = 3000 \pm 100$ m/s and $T = 0.500 \pm
0.005$ s, each uncertainty being one standard deviation. Using the delta method,
compute $d$ and its standard deviation, then construct an approximate $95\%$ interval.

---

## ★★★ Research-oriented

**★★★9.** Let $\bar X \sim \mathcal{N}(\mu + \delta, \sigma^{2}/n)$ and let the
interval be $\bar X \pm z_{1-\alpha/2}\sigma/\sqrt n$.

(a) Derive the coverage probability as a function of $\delta$, $n$ and $\sigma$.
(b) Show that coverage tends to $0$ as $n \to \infty$ for any fixed $\delta \ne 0$.
(c) Show that coverage is monotone decreasing in $|\delta|$ for fixed $n$.
(d) Explain, in two sentences, what this says about the value of more data in the
presence of an unmodelled systematic error.

**★★★10.** You plan a simulation to measure the coverage of a $95\%$ interval to a
standard error of $0.002$. Compute the number of replications required, state the
formula, and explain why the required number depends on the true coverage being
measured.

**★★★11.** A ratio $R = A/B$ is estimated with $\hat A = 100 \pm 2$ and
$\hat B = 10 \pm 2$ (each uncertainty is one standard deviation, and the two
estimates are independent).

(a) Compute $R$ and its delta-method standard deviation, and the resulting symmetric
$95\%$ interval.
(b) Explain why the symmetric interval may be poor here, naming the feature of the
distribution of $1/B$ that causes it.
(c) State how you would construct a better interval, and give the Monte Carlo
quantiles you would expect to find for comparison (you may reason qualitatively, or
compute them if you have the tools).
