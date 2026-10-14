# Exercises — 11-07-02 Case Study: Basin Analysis and Play Assessment

Attempt these before reading the
[solutions](./02-case-study-basin-solutions.md). The lesson is
[02 Case Study: Basin Analysis and Play Assessment](../02-case-study-basin.md).
All models are **SYNTHETIC** argument archetypes: no real basin, play, field or
well is used, and no site-specific number is quoted.

## ★ Foundational

**★1.** Four independent play elements have probabilities $0.5, 0.6, 0.7, 0.8$.
Compute the independent chance of success, and state in one sentence why it is a
model rather than a measurement.

**★2.** An amplitude anomaly has $\mathrm{TPR} = 0.8$ and $\mathrm{FPR} = 0.4$.
Compute the posterior at priors of $0.1$ and $0.4$, and the expected number of dry
wells per 10 drilled anomalies at the lower prior.

**★3.** A well costs $C$ and the mean gross value of a success is $6C$. Compute
the break-even probability of commercial success and the EMV at $q = 0.40$.

## ★★ Applied

**★★4.** Five elements have probabilities $0.7, 0.7, 0.7, 0.7, 0.7$. Compute the
independent chance and the joint chance if they share a common factor with
$\rho = 0.5$ (you may reason qualitatively about the direction, but give a
number for the independent case). Explain why the correlated value is the larger
one.

**★★5.** At a posterior of $0.35$ with a lognormal resource whose mean gross
value is $5C$ and whose $P(\text{gross} < C) = 0.25$, compute the probability of
a profitable outcome and the EMV. State which number a board should be shown.

**★★6.** A survey has $\mathrm{TPR} = 0.8$, $\mathrm{FPR} = 0.15$ and costs
$0.1\,\mathbb{E}[V]$, where $\mathbb{E}[V]$ is the mean gross value of a success;
a well costs $0.5\,\mathbb{E}[V]$. For priors of $0.05$, $0.45$ and $0.70$,
compute the blind EV, the survey EV and the VOI, and identify the prior at which
the survey is most valuable.

## ★★★ Research-oriented

**★★★7.** Write a play assessment for a frontier basin with the five elements,
each with its evidence and its uncertainty, quoting no real numbers. State the
correlation structure you would assume, justify it, and give the decision rule
that converts the assessment into a drilling sequence.

**★★★8.** The lesson's shared-factor model uses one correlation parameter for all
element pairs. Design a more defensible model: name two pairs of elements that
should be strongly coupled and one that should be nearly independent, state how
you would estimate each coupling from data you could obtain, and describe how the
change would move the chance of success and the drill decision.
