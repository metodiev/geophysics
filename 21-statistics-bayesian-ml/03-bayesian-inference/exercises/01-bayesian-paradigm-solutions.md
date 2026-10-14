# Solutions — 21-03-01 The Bayesian Paradigm and Subjective Probability

> Read after attempting. Lesson:
> [01 The Bayesian Paradigm](../01-bayesian-paradigm.md). Numbers quoted from
> the demonstration reproduce its output.

---

## ★1 — Beta(3,4) updated

Prior $\mathrm{Beta}(3,4)$ with $k = 5$ successes in $n = 12$ trials gives

$$\mathrm{Beta}(a+k,\ b+n-k) = \mathrm{Beta}(8, 11) .$$

$$\text{mean} = \frac{a}{a+b} = \frac{8}{19} = 0.421053 ,$$

$$\text{mode} = \frac{a-1}{a+b-2} = \frac{7}{17} = 0.411765 ,$$

$$\text{variance} = \frac{ab}{(a+b)^{2}(a+b+1)}
= \frac{8\times11}{19^{2}\times20} = \frac{88}{7220} = 0.012188 ,$$

$$\text{sd} = 0.110400 .$$

The posterior mean sits between the prior mean $3/7 = 0.4286$ and the
maximum-likelihood estimate $5/12 = 0.4167$ — the prior is weak and the two are
close, so the posterior barely moves from either.

---

## ★2 — Prior-equivalent sample size

A $\mathrm{Beta}(a,b)$ prior carries $a - 1$ prior successes and $b - 1$ prior
failures, hence

$$n_0 = (a-1) + (b-1) = a + b - 2 .$$

- $\mathrm{Beta}(3,4)$: $n_0 = 5$.
- $\mathrm{Beta}(1,1)$ (uniform): $n_0 = 0$.
- $\mathrm{Beta}(2,2)$ (weak): $n_0 = 2$.
- $\mathrm{Beta}(20,20)$ (sceptical): $n_0 = 38$.

The last of these exceeds the demonstration's $30$ observations, which is exactly
why it moved the posterior mean to $0.3857$.

---

## ★3 — Posterior predictive

$$\Pr(\text{next success} \mid y) = \mathbb E[p \mid y] = \frac{a}{a+b}
= \frac{8}{19} = 0.421053 .$$

For a Bernoulli likelihood the predictive equals the posterior mean, so no extra
integration is needed. The interpretation is the one a forecaster wants: given
the prior and the twelve observations, the probability of a success next time is
$42.1\ \%$ — not the maximum-likelihood $41.7\ \%$, and not the prior $42.9\ \%$.

---

## ★★4 — Deriving the Beta-Binomial update

$$p(\theta \mid k) \propto p(k\mid\theta)\,p(\theta)
= \binom{n}{k}\theta^{k}(1-\theta)^{n-k}\cdot
\frac{\theta^{a-1}(1-\theta)^{b-1}}{B(a,b)} .$$

Collect the powers of $\theta$ and of $(1-\theta)$:

$$p(\theta\mid k) \propto \theta^{(a+k)-1}(1-\theta)^{(b+n-k)-1} ,$$

which is the kernel of $\mathrm{Beta}(a+k, b+n-k)$. The discarded constants are
$\binom{n}{k}$ and $1/B(a,b)$; neither depends on $\theta$, so neither affects
the shape or the location of the posterior. The normalising constant of the
posterior is $1/B(a+k, b+n-k)$, recovered by requiring the density to integrate
to one — which is why the demonstration's grid posterior agrees with the closed
form to $6\times10^{-17}$.

The word "conjugate" means precisely this: the prior and posterior belong to the
same family, so updating is an arithmetic operation on the parameters.

---

## ★★5 — One trial, zero successes

**Posterior.** Uniform $\mathrm{Beta}(1,1)$ prior, $k = 0$, $n = 1$ gives
$\mathrm{Beta}(1,2)$, whose CDF is $F(\theta) = 1 - (1-\theta)^{2}$.

Solve $F = 0.975$: $(1-u)^{2} = 0.025$, so $u = 1 - 0.15811 = 0.84189$.
Solve $F = 0.025$: $(1-l)^{2} = 0.975$, so $l = 1 - 0.98742 = 0.01258$.

$$C_{\text{credible}} = [0.0126,\ 0.8419] .$$

**Clopper-Pearson.** For $k = 0$ successes in $n = 1$ trials the two-sided
$95\ \%$ interval is

$$C_{\text{confidence}} = \big[0,\ 1 - 0.025^{1}\big] = [0,\ 0.975] .$$

**The difference in meaning.** The credible interval says: given the uniform
prior and the single observation, the probability that $\theta$ lies in
$[0.0126, 0.8419]$ is $0.95$. The confidence interval says: if we repeated the
one-trial experiment many times and used this recipe, $95\ \%$ of the intervals
produced would contain the fixed true $\theta$. The lower endpoint of $0$ is not
a claim that $\theta$ might be zero with any posterior probability; it is an
artefact of a procedure designed to guarantee coverage. For $k = 0$ the two
intervals differ in both endpoints, and neither is wrong.

---

## ★★6 — How much data to overcome the prior

With prior-equivalent size $n_0$ and prior mean $m_0$, the posterior mean is a
weighted average:

$$\bar\theta_{\text{post}} = \frac{n_0 m_0 + n\,\hat\theta_{\text{MLE}}}{n_0 + n},
\qquad
\bar\theta_{\text{post}} - \hat\theta_{\text{MLE}}
= \frac{n_0\,(m_0 - \hat\theta_{\text{MLE}})}{n_0 + n} .$$

Setting the difference to $0.01$:

$$n_0(0.5 - 0.2333) = 0.01\,(n_0 + n)
\;\Longrightarrow\;
38\times0.26667 = 0.01(38 + n)$$
$$10.133 = 0.38 + 0.01n
\;\Longrightarrow\;
n = \frac{9.753}{0.01} = 975 .$$

So about **$975$ observations** would be needed to bring the posterior mean
within $0.01$ of the maximum-likelihood estimate under that prior — thirty-two
times the data actually available. The demonstration's analysis is therefore
prior-dominated in a strong, quantifiable sense, and no amount of posterior
arithmetic changes it.

---

## ★★★7 — Prior-sensitivity study for a slip rate

**Quantity.** A fault's mean slip rate $s$ in mm/yr, with a Poisson or
renewal likelihood for the number of palaeoearthquake events in a known interval.

**Priors.** Five priors on $\log s$: (i) a broad uniform over
$[0.01, 100]\ \mathrm{mm/yr}$; (ii) a lognormal centred on the regional average
with a factor-of-three standard deviation; (iii) the same centred on a nearby
fault's rate with a factor-of-two deviation; (iv) an informative prior from a
published slip-rate compilation with a $20\ \%$ relative deviation; (v) the
improper Jeffreys prior for a Poisson rate. State each **prior-equivalent sample
size** in number of events.

**Metric.** The posterior mean and $95\ \%$ credible interval of $s$; the
sensitivity index $S = (\bar\theta_{\max} - \bar\theta_{\min}) /
\text{posterior sd}$, the shift in the posterior mean across priors expressed in
posterior standard deviations.

**Data.** $M = 500$ synthetic event series generated from a stated true rate,
each with the same exposure and catalogue length, so that the study separates
prior sensitivity from sampling noise.

**Declaring prior-dominance.** Report the analysis as prior-dominated when
$S > 1$ — the spread of answers across reasonable priors exceeds one posterior
standard deviation — or when the prior-equivalent sample size exceeds the number
of observed events. Both criteria are computable, and both should be reported in
the paper.

---

## ★★★8 — Calibration of credible intervals

**Data-generating process.** $M = 10\,000$ replicates of a binomial experiment
with $n = 20$ and a true probability $\theta_{\text{true}} = 0.3$. For each
replicate, compute the $95\ \%$ equal-tailed credible interval under

- the **correct** prior: $\mathrm{Beta}(3,7)$, centred at $0.3$;
- a **wrong but weak** prior: $\mathrm{Beta}(1,1)$;
- a **wrong and strong** prior: $\mathrm{Beta}(20,5)$, centred at $0.8$ — badly
  mis-specified.

**Metric.** The realised coverage, the fraction of the $10\,000$ intervals that
contain $\theta_{\text{true}} = 0.3$; and the mean interval width.

**Replicate count.** With $M = 10\,000$ the standard error of a coverage estimate
near $0.95$ is $\sqrt{0.95\times0.05/10\,000} = 0.0022$, so a $1\ \%$ departure
from nominal is resolved at $4.5\sigma$.

**Prediction.** The correct prior gives coverage $0.95$ within Monte-Carlo error.
The weak uniform prior also gives $0.95$: with $n = 20$ the data dominate, and
the interval is slightly wider. The **strong wrong prior under-covers badly** —
coverage of order $0.6$–$0.7$ — because the posterior is pulled towards $0.8$
while the intervals remain narrow. The headline is the coverage-versus-prior-misspecification
table: a Bayesian credible interval is calibrated when the prior is right and,
unlike a confidence interval, it makes **no** guarantee when the prior is wrong.
