# Solutions — 16-05-05 CMIP, Model Intercomparison and Ensemble Design

> Read after attempting the exercises. Lesson:
> [05 Model Intercomparison and Ensemble Design](../05-coupled-model-intercomparison.md).

---

## ★1 — Members for a target standard error

$$\frac{\sigma_i}{\sqrt N} \le 0.05
\quad\Longrightarrow\quad
\sqrt N \ge \frac{0.4}{0.05} = 8
\quad\Longrightarrow\quad
N \ge 64.$$

Since the standard error falls as $1/\sqrt N$, halving the target requires four
times the members: a target of $0.025\ \mathrm{K}$ would need $N \ge 256$.

---

## ★2 — Structural standard deviation

Mean:

$$\bar M = \frac{1.5+2.5+5.0}{3} = \frac{9.0}{3} = 3.0\ \mathrm{K}.$$

Deviations: $-1.5$, $-0.5$, $+2.0$; squares $2.25$, $0.25$, $4.00$; sum $6.50$.
With $N-1 = 2$:

$$\sigma_{\text{struct}} = \sqrt{\frac{6.50}{2}} = \sqrt{3.25}
= 1.803\ \mathrm{K}.$$

(With $N$ in the denominator the value would be $\sqrt{2.167} = 1.472\
\mathrm{K}$; the choice must be stated, and with three models the difference is
$22\%$.)

---

## ★3 — Total spread

Internal part with $N = 25$:

$$\frac{\sigma_i}{\sqrt N} = \frac{0.5}{5} = 0.1\ \mathrm{K}.$$

Total:

$$\sigma_{\text{total}} = \sqrt{3.25 + 0.1^{2}} = \sqrt{3.26}
= 1.806\ \mathrm{K}.$$

Compare $\sqrt{3.25} = 1.803\ \mathrm{K}$: the internal contribution of
$0.1\ \mathrm{K}$ moves the total by $0.003\ \mathrm{K}$, i.e. $0.17\%$. With a
structural spread of $1.803\ \mathrm{K}$, the members per model are almost
irrelevant.

---

## ★4 — Where the total spread saturates

| $N$ | internal part (K) | total spread (K) | excess over structural |
|---|---|---|---|
| 1 | 0.5000 | $\sqrt{3.25+0.25} = 1.871$ | $3.8\%$ |
| 4 | 0.2500 | $\sqrt{3.25+0.0625} = 1.820$ | $0.94\%$ |
| 16 | 0.1250 | $\sqrt{3.25+0.0156} = 1.807$ | $0.24\%$ |
| 100 | 0.0500 | $\sqrt{3.25+0.0025} = 1.8035$ | $0.03\%$ |
| 10000 | 0.0050 | $\sqrt{3.25+0.000025} = 1.80301$ | $0.0007\%$ |

The value is within $1\%$ of structural at $N = 4$ already. The general
condition is $\sigma_i^{2}/N \le 0.0201\,\sigma_{\text{struct}}^{2}$, i.e.

$$N \ge \frac{1}{0.0201}\left(\frac{\sigma_i}{\sigma_{\text{struct}}}\right)^{2}.$$

With $\sigma_i/\sigma_{\text{struct}} = 0.5/1.803 = 0.277$ the bound gives
$N \ge 3.8$, consistent with the table.

---

## ★5 — Two weighting conventions

Member-weighted (every member counts once):

$$\bar M_{\text{member}} = \frac{10(2.0)+40(3.0)+50(4.0)}{10+40+50}
= \frac{20+120+200}{100} = 3.40\ \mathrm{K}.$$

Model-weighted (every model counts once):

$$\bar M_{\text{model}} = \frac{2.0+3.0+4.0}{3} = 3.00\ \mathrm{K}.$$

Difference: $0.40\ \mathrm{K}$ — $13\%$ of the model-mean value, produced purely
by the choice of weighting and the unequal member counts. Neither is privileged;
the estimator must be named.

---

## ★6 — Why inverse-variance weighting is unavailable

Inverse-variance weighting assigns model $k$ the weight
$w_k \propto 1/\sigma_k^{2}$, where $\sigma_k$ is that model's internal
variability. In practice $\sigma_k$ is estimated from the model's *own* ensemble,
which is expensive and often unavailable — many archived models contribute a
single run. Even when it is available, the estimate is itself noisy for small
ensembles, and the weights inherit that noise.

The assumption most likely to fail is **exchangeability**: inverse-variance
weighting is optimal when the models are independent draws about a common mean,
but real model families share code, parameterisations and institutional history,
so their errors are correlated and their spread does not estimate a population
variance. When that fails, the weights are precise-looking but meaningless.

---

## ★7 — Ensemble design (specification)

**Pilot information.** From a small pilot, measure the internal variability
$\sigma_i$ as the spread among members of one model, and the structural spread
$\sigma_{\text{struct}}$ as the spread among the available models' ensemble means.

**Target.** State a target total standard uncertainty $\tau$ and require

$$\sigma_{\text{struct}}^{2} + \frac{\sigma_i^{2}}{N} \le \tau^{2}
\quad\Longrightarrow\quad
N \ge \frac{\sigma_i^{2}}{\tau^{2}-\sigma_{\text{struct}}^{2}}.$$

If $\tau \le \sigma_{\text{struct}}$, the target is unreachable: report the
structural floor and stop. Otherwise choose the smallest $N$ satisfying the
bound, round up, and add members for the number of models $K$ that the study can
afford: the design is $(K, N)$ with a stated weighting.

**Assumption the design cannot test.** That the available models bracket the
plausible physics. If every model in the archive shares a bias — for example an
unresolved process that all parameterise the same way — the ensemble is
confidently centred on a wrong value, and no combination of members or models
reveals it.

---

## ★8 — Critique of a multi-model standard error

**What the standard error measures.** The dispersion of the eight ensemble
means about their own average, divided by $\sqrt 8$. It measures how tightly the
eight *opinions* cluster.

**What it omits.** (i) It treats the eight models as independent draws, but they
share code and parameterisations; the effective number of independent models is
smaller, so the quoted error is too small. (ii) It omits any bias common to all
eight, which no spread can detect. (iii) It omits forcing uncertainty. (iv) It
depends on the sample — an archive of eight particular models is not a random
sample, so the standard error is not an unbiased estimator of any population
quantity.

**Diagnostic that would reveal the problem.** Cluster the models by shared
components (atmospheric core, land-surface scheme, ocean model) and recompute the
spread between clusters and within clusters. If the within-cluster spread is much
smaller than the between-cluster spread, the models are not independent and the
$\sqrt 8$ divisor is unjustified. Report the spread and the cluster structure
together, and describe the mean as "the mean of the available models" rather than
as a best estimate with a sampling error.
