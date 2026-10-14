# Exercises — 21-01-07 Extreme Value Theory for Geohazards

Attempt these before reading the
[solutions](./07-extreme-value-theory-solutions.md). The lesson is
[07 Extreme Value Theory](../07-extreme-value-theory.md). All data are
**SYNTHETIC**; numbers quoted from the demonstration reproduce its output.

## ★ Foundational

**★1.** Classify each of the following fitted shape parameters as Gumbel, Fréchet
or Weibull, and state the corresponding domain of attraction and tail
behaviour: (a) $\hat\xi = +0.63$; (b) $\hat\xi = -0.12$; (c) $\hat\xi = -0.001$.

**★2.** Compute the Gumbel ($\xi = 0$) return level for $\mu = 0$,
$\sigma = 1$ at $T = 10$ and $T = 100$.

**★3.** For a $T$-block return level $z_T$, compute the probability that it is
exceeded at least once in $T$ consecutive blocks, for $T = 10$ and $T = 100$.
Comment on the answer.

## ★★ Applied

**★★4.** Using the demonstration's fit $\hat\mu = 7.6615$,
$\hat\sigma = 4.9415$, $\hat\xi = +0.6297$, evaluate the GEV return level at
$T = 100$ and compare with the printed $141.957$. Then evaluate it at $T = 10$
and compare with $32.184$.

**★★5.** The GPD fit above $u = 7.664$ gives $\hat\beta = 5.1507$,
$\hat\xi = 0.5831$, with the threshold recurrence rate $\lambda_u = 1.0$
exceedance per $20$-observation block. Compute the threshold-model return level
$z_T = u + (\beta/\xi)[(T\lambda_u)^{\xi} - 1]$ at $T = 100$ and compare with the
GEV value $141.957$. State why the two can differ.

**★★6.** From the mean-excess table, the slope between $u = 7.664$ and
$u = 10.651$ is $+1.2010$. Invert it to recover the implied $\xi$ and compare
with the fitted $\hat\xi = 0.5831$. State why a mean-excess slope is a noisier
estimate of $\xi$ than a maximum-likelihood fit.

## ★★★ Research-oriented

**★★★7.** Specify a **threshold-selection study** that measures the bias and
variance of the GPD shape estimate as a function of the exceedance fraction for
synthetic Fréchet data with a known $\xi$. State the exceedance fractions, the
replicate count, the diagnostics you would use on real data, and the prediction
for the bias at low and high thresholds. A specification that could not be
executed is a failed answer.

**★★★8.** Design a **declustering study** for a synthetic series of clustered
extremes with an estimated extremal index $\theta < 1$. State the cluster
identification rule, the declustering runs parameter, the quantity that the
extremal index rescales, and the way you would verify that the declustered
series is approximately i.i.d.
