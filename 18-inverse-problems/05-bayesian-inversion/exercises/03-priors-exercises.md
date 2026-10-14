# Exercises — 18-05-03 Priors: Informative, Reference and Their Influence

Lesson: [03 Priors: Informative, Reference and Their Influence](../03-priors.md).
Attempt these before reading the [solutions](./03-priors-solutions.md).
All models are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** One datum $d = 2.0$ with $\sigma = 0.5$. For prior standard deviations
$s_0 = 0.25$ and $s_0 = 4.0$, compute the shrinkage factor $K$, the posterior mean
and the posterior standard deviation.

**★2.** With $N = 25$ data of $\sigma = 2$, find the prior standard deviation $s_0$
at which the prior supplies **exactly** half of the posterior precision.

**★3.** Derive the Jeffreys prior for a Poisson rate $\lambda$ from
$p(k\mid\lambda) = \lambda^{k}e^{-\lambda}/k!$. Give the posterior for an observed
count $k_{\text{obs}} = 3$, its mean and its mode.

## ★★ Applied

**★★4.** With $N = 16$ data of $\sigma = 0.5$ and a prior of width $s_0 = 1$,
compute the prior share of the posterior precision. Then state how much the
posterior mean could be moved by choosing $m_0$ a full prior standard deviation
away from the data mean, and whether that is acceptable in a study claiming to
measure the parameter.

**★★5.** Explain with one calculation why a flat prior on $\sigma$ and a flat prior
on $\log\sigma$ give different credible intervals for $\sigma$, and state which of
the two is invariant under $\sigma \to 1/\sigma$. Quote the measured interval
difference from the demonstration.

**★★6.** Two SYNTHETIC measurements $(0.30,\,0.34)$ with $\sigma = 0.12$ are
inverted under a uniform prior on $[0,0.5]$. Compute the posterior mean, standard
deviation and the mass within $0.02$ of the bound. Repeat for
$(0.60,\,0.64)$. State the summary you would report in each case.

## ★★★ Research-oriented

**★★★7.** Design a study that quantifies the sensitivity of a two-layer
travel-time inversion to the prior on layer thickness. State the priors to be
compared, the metric, the number of replicas, and how you would decide that the
result is "prior-dominated".

**★★★8.** A bounded inversion reports a posterior that piles up at the upper
bound with $60\%$ of its mass. List three mutually exclusive explanations, and
give the diagnostic that distinguishes each.
