# Exercises — 23-01-02 Planning a Field Campaign: Objectives, Permits, Logistics

Attempt these before reading the
[solutions](./02-field-planning-solutions.md). The lesson is
[02 Field Planning](../02-field-planning.md). All rates, probabilities and costs
are **SYNTHETIC** teaching values. In every part, calendar days and productive
days are different quantities and must be reported separately.

## ★ Foundational

**★1.** A survey needs $D = 15$ productive days. The daily working probability is
$w = 0.45$ and days are treated as independent. Compute the expected calendar
length $\mathbb{E}[T]$, its standard deviation $\operatorname{sd}(T)$ and the
ratio $\mathbb{E}[T]/D$. State the unit of each.

**★2.** For the campaign of ★1: compute $P(T > 40\ \mathrm{d})$ (a) exactly, by
recognising the event as a binomial statement, and (b) with a normal
approximation including a continuity correction. Also compute the 90th and 95th
percentiles of $T$ from the normal approximation. Say which of the two
calculations you would put in a contract.

**★3.** A two-state weather model has $P(\text{wet} \mid \text{wet}) = 0.70$ and
$P(\text{wet} \mid \text{dry}) = 0.25$. Compute the stationary wet fraction, the
stationary working fraction and the first-pass calendar estimate $D/w$ for
$D = 15$.

## ★★ Applied

**★★4.** Derive $\mathbb{E}[T] = D/w$ and
$\operatorname{Var}(T) = D(1-w)/w^{2}$ from the representation of the campaign
as a sum of waiting times, stating the distribution of each wait and the identity
of the sum.

**★★5.** A persistent-weather simulation of a 20-productive-day campaign reports
a mean of $39.03\ \mathrm{d}$ and a standard deviation of $6.12\ \mathrm{d}$.
Compute the number of contracted calendar days needed for the overrun
probability to be at most 10 %, and the number needed for at most 5 %. Compare
the 10 % answer with the simulated 90th percentile of $47.0\ \mathrm{d}$ and
comment on the agreement.

**★★6.** Using a mobilisation charge of 25 000 units and a daily rate of
2400 units/day, compute the expected and 90th-percentile cost of the campaign of
★★5. Then compute the cost of adding a two-day buffer to the contract, and
compare it with the difference between the two models' 90th-percentile costs
(independent 130 600 units, persistent 137 800 units).

## ★★★ Research-oriented

**★★★7.** You want to estimate $w$ from a campaign's own logs, to a 95 %
confidence half-width of ±0.05. State the estimator, compute the number of
campaign days required using the variance at $w = 0.5$ and again at
$w = 0.45$, and name two reasons the estimate from field logs is biased.

**★★★8.** Design a study that replaces the assumed $w$ with one fitted from a
daily precipitation or wind record for the site: state the data you would obtain
and from whom, the model you would fit, the validation you would run, the
decision the fitted model would change, and three things the model still would
not predict. A specification that could not be executed is a failed answer.
