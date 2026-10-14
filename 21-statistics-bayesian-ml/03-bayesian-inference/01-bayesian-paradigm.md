---
id: 21-03-01
title: "The Bayesian Paradigm and Subjective Probability"
level: doctoral
prereqs: ["01-13-01", "01-13-06"]
estimated_minutes: 70
tags: [bayesian, subjective-probability, prior, posterior, exchangeability, credible-interval]
---

# The Bayesian Paradigm and Subjective Probability

## Learning objectives

By the end of this lesson you will be able to:

1. **State** the three ingredients of a Bayesian analysis and **write** Bayes'
   theorem for a parameter.
2. **Justify** the use of a prior through exchangeability and de Finetti's
   theorem rather than through convenience.
3. **Distinguish** a credible interval from a confidence interval and **state**
   what each is a statement about.
4. **Compute** a posterior on a grid, its mean, its mode and an equal-tailed
   credible interval, and **check** it against a closed form.
5. **Explain** sequential updating and sufficiency, and **demonstrate** that the
   order of evidence does not change the answer.
6. **Quantify** prior sensitivity in prior-equivalent sample units and **state**
   when a conclusion is prior-dominated.

Every data set in this lesson is **SYNTHETIC**: a Bernoulli sequence with a
stated probability, generated in the demonstration. No measured value is used,
and the posteriors below constrain only that synthetic experiment.

## Prerequisites

- [01-13-01 Probability Axioms, Conditional Probability and Bayes' Rule](../../01-mathematics/13-probability-and-statistics-foundations/01-probability-axioms.md) —
  the theorem this lesson applies to parameters.
- [01-13-06 Point Estimation, Bias, Consistency and Efficiency](../../01-mathematics/13-probability-and-statistics-foundations/06-estimation-theory.md) —
  the frequentist alternative the Bayesian answer is compared with.
- [21-01-02 Choosing Probability Models for Earth Data](../01-statistics-in-practice/02-probability-models-earth.md) —
  the likelihood side of the construction.

## 1. Intuition: probability as a state of knowledge

The Bayesian view treats probability as a measure of a rational agent's belief,
not as a long-run frequency. That single change of meaning is what allows the
same formalism to describe a coin, a fault slip rate and the permeability of an
un-drilled block: all three are uncertain to *us*, and the mathematics of belief
applies to all three.

The machinery is Bayes' theorem. For data $y$, a parameter $\theta$ and a prior
density $p(\theta)$,

$$p(\theta \mid y) = \frac{p(y \mid \theta)\,p(\theta)}{p(y)},
\qquad
p(y) = \int p(y\mid\theta)\,p(\theta)\,\mathrm d\theta .$$

Three statements carry all the meaning: the **prior** says what values were
plausible before the data; the **likelihood** says how well each value explains
what was observed; the **posterior** is the compromise, weighted by how much
information each carries. The denominator is a normalising constant — the
**evidence** — which matters only when comparing models.

## 2. Where the prior comes from: exchangeability

The objection to priors is that they are subjective. The Bayesian answer is that
they are *derivable* when the data have a symmetry. Observations are
**exchangeable** if the joint distribution is invariant under permutation: no
observation is special, so the order carries no information. de Finetti's
theorem states that exchangeable observations are, for a Bayesian agent,
conditionally independent and identically distributed given some latent
parameter, with a unique prior over that parameter. The prior is therefore not an
arbitrary insertion; it is what exchangeability plus the data imply.

That argument gives the shape, not the numbers. Whether the prior for a
slip rate should be broad or concentrated near a published catalogue value is a
scientific judgement about the region, and the honest response is to state it,
use it, and report how much the answer depends on it (Section 6).

## 3. Priors, named honestly

- **Proper**: integrates to one. Required for the evidence and for the posterior
  predictive.
- **Improper**: does not integrate, such as a uniform prior on the whole real
  line. It may still give a proper posterior; it must never be reported as a
  probability.
- **Informative**: concentrated on values the analyst has a reason to expect.
- **Weakly informative**: broad enough to let the data speak, narrow enough to
  keep the posterior proper and the computation stable.
- **Reference / non-informative**: chosen to let the data dominate as far as
  possible. "Non-informative" is a misnomer — a uniform prior on a rate is
  informative after a log transform.

## 4. Sufficiency, sequential updating and the likelihood principle

A statistic $s(y)$ is **sufficient** for $\theta$ if $p(y \mid \theta) =
h(y)\,g(s(y)\mid\theta)$. If so, Bayes' theorem gives the same posterior from
$s(y)$ as from $y$. Two consequences matter operationally:

- **Sequential updating is exact.** Today's posterior is tomorrow's prior, and
  $p(\theta\mid y_1, y_2) = p(\theta\mid y_1, y_2)$ computed in any order. The
  demonstration confirms it to the last digit: updating $3$ of $10$ then $4$ of
  $20$ gives $\mathrm{Beta}(9,25)$ and a mean of $0.264706$, identical to
  updating all $30$ at once.
- **Stopping rules do not matter.** Because only the realised data enter the
  likelihood, an experiment stopped early for a reason that depends on the data
  gives the same posterior. This is the likelihood principle, and it is a
  genuine divergence from frequentist inference, where the sampling plan enters
  the $p$-value.

## 5. Credible versus confidence intervals

A $95\ \%$ **credible interval** is a set $C$ with $p(\theta \in C \mid y) = 0.95$
under the posterior. It is a statement about $\theta$: *given the model and the
data, there is a $95\ \%$ probability that $\theta$ lies in this set.*

A $95\ \%$ **confidence interval** is a procedure with the property that, in
repeated sampling, $95\ \%$ of the intervals it produces cover the true fixed
$\theta$. It is a statement about the procedure, and the interval computed from
one sample either covers or does not.

The two can coincide numerically — for a large sample and a flat prior they
nearly do — but they mean different things, and a geophysicist quoting "a
$95\ \%$ probability that the velocity is between $3.1$ and $3.4\ \mathrm{km/s}$"
is making a credible-interval claim whether or not the method supports it.

## 6. Worked example: prior sensitivity, measured

The demonstration draws $30$ Bernoulli trials with true probability $0.45$ and
observes $7$ successes (an unlucky draw, which is itself instructive). The
maximum-likelihood estimate is $k/n = 0.2333$. Three priors give three
posteriors:

| prior | prior mean | posterior mean | $95\ \%$ credible interval | MAP |
|---|---|---|---|---|
| uniform $\mathrm{Beta}(1,1)$ | 0.5000 | 0.2500 | [0.1185, 0.4110] | 0.2335 |
| weak $\mathrm{Beta}(2,2)$ | 0.5000 | 0.2647 | [0.1330, 0.4225] | 0.2500 |
| sceptical $\mathrm{Beta}(20,20)$ | 0.5000 | 0.3857 | [0.2760, 0.5015] | 0.3825 |

The posterior means are exactly $(a+k)/(a+b+n)$, and the grid values agree with
the closed forms to $6\times10^{-17}$.

**Reading the table.** The sceptical prior has a prior-equivalent sample size of
$a+b-2 = 38$ observations, larger than the $30$ actually collected, so it moves
the posterior mean from $0.2500$ to $0.3857$ — a shift of $0.136$, comparable to
the width of the credible interval. With a $38$-observation prior and $30$
observations of data the analysis is **prior-dominated**, and no amount of
posterior arithmetic can fix that. The weakly informative $\mathrm{Beta}(2,2)$,
equivalent to $2$ observations, moves the mean by only $0.015$.

**The posterior predictive.** Under $\mathrm{Beta}(2,2)$ the probability that the
next trial succeeds is $(a+k)/(a+b+n) = 0.264706$ — the posterior mean, because
the predictive of a Bernoulli is the mean of $p$. This is the quantity a
forecaster needs, and it is available immediately from the posterior.

## 7. Assumptions and regime of validity

1. **The likelihood is correct.** A wrong likelihood cannot be rescued by any
   prior; a Bayesian analysis inherits every modelling assumption of the
   frequentist one.
2. **The prior is stated.** An unstated prior is still a prior, and one that
   cannot be checked.
3. **Exchangeability holds.** Sequential, spatially clustered or truncated data
   break it, and then a hierarchical or time-series model is required.
4. **The posterior must be proper** for credible intervals to mean anything;
   improper priors need a check.
5. **Computational error is separate.** Grid, MCMC and variational posteriors
   carry their own errors; the demonstration checks the grid against a closed
   form precisely because that check is not automatic.
6. **The credible interval summarises a distribution.** Reporting its endpoints
   without the distribution hides skew and multimodality.

## The honest summary

Bayesian inference is a bookkeeping rule for combining prior information with
data, and its honesty depends entirely on the prior being declared and its
influence measured. In the demonstration the same $30$ observations gave
posterior means of $0.2500$, $0.2647$ and $0.3857$ under three priors: a spread
of $0.136$ that is comparable to the credible-interval width, produced purely by
the choice of prior. The prior-equivalent sample size made that visible —
$0$, $2$ and $38$ observations — and it is the number to report. What the
demonstration does **not** establish is which prior is right: that is a
scientific judgement, and the honest analysis reports the sensitivity rather than
hiding behind a single default.

## Python demonstration

[`code/bayesian_paradigm_demo.py`](./code/bayesian_paradigm_demo.py) prints every
number quoted above. It:

1. computes three grid posteriors and checks each against its closed form;
2. verifies that sequential and batch updating agree exactly;
3. tabulates the prior-equivalent sample size and the posterior predictive.

```bash
cd 21-statistics-bayesian-ml/03-bayesian-inference/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python bayesian_paradigm_demo.py
```

It runs in about half a second and prints only text.

## Exercises

Graded problems are in
[`exercises/01-bayesian-paradigm-exercises.md`](./exercises/01-bayesian-paradigm-exercises.md)
with worked solutions in
[`exercises/01-bayesian-paradigm-solutions.md`](./exercises/01-bayesian-paradigm-solutions.md).
The ★★★ problems ask you to design the prior-sensitivity experiment.

## Mastery checkpoint

Without notes, $7$ successes in $30$ trials with a $\mathrm{Beta}(2,2)$ prior
give $\mathrm{Beta}(9,25)$, posterior mean $0.2647$ and credible interval
$[0.1330, 0.4225]$.

1. Compute the posterior mean from the formula and state the prior-equivalent
   sample size.
2. Compute the posterior mode and explain why it differs from the mean.
3. State the posterior predictive probability of the next success.
4. A colleague replaces the prior with $\mathrm{Beta}(20,20)$ and reports
   $0.3857$. State whether the analysis is prior-dominated and why.

## Common pitfalls

1. **Reading a confidence interval as a credible interval.** They answer
   different questions.
2. **Hiding the prior.** An undeclared prior cannot be assessed; state it and its
   prior-equivalent sample size.
3. **Using an improper prior and reporting the evidence.** The evidence needs a
   proper prior.
4. **Believing "non-informative" is neutral.** A uniform prior is informative on
   any transformed scale.
5. **Ignoring sufficiency and re-running the analysis.** The posterior is a
   sufficient summary; there is nothing to gain from revisiting the raw data.
6. **Reporting a credible interval from a skewed posterior as a symmetric
   range.** The equal-tailed interval here is $[0.1330, 0.4225]$, not
   $0.2647 \pm 0.145$.

## Where this is used

- **Seismic hazard**: slip-rate and recurrence parameters with catalogue priors.
- **Reservoir characterisation**: facies probabilities combining logs and
  seismic.
- **Geodesy**: velocity fields with prior constraints from plates.
- **Climate attribution**: detection and attribution is a Bayesian comparison of
  competing explanations.
- **Machine learning**: regularisation is a prior, and every penalised fit is a
  maximum a posteriori estimate.

## Related lessons

- [21-03-02 Conjugate Priors and Analytic Posteriors](02-conjugate-priors.md) —
  the families whose posteriors can be written in closed form.
- [21-03-03 Hierarchical Models and Exchangeability](03-hierarchical-models.md) —
  what to do when groups of data are exchangeable but not identical.
- [21-03-06 Bayesian Workflow and Principled Model Building](06-bayesian-workflow.md) —
  the practical protocol for the sensitivity analysis of Section 6.
- [18-05 Bayesian Inversion and Inference](../../18-inverse-problems/05-bayesian-inversion/README.md) —
  the same construction for infinite-dimensional inverse problems.
- [21-04-04 Regularisation: Ridge, Lasso, Early Stopping](../04-machine-learning-fundamentals/04-regularization-ml.md) —
  priors seen as penalties.

## Self-assessment checklist

- [ ] I can write Bayes' theorem and name each term.
- [ ] I can justify a prior through exchangeability.
- [ ] I can distinguish credible from confidence intervals.
- [ ] I can compute a grid posterior and check it against a closed form.
- [ ] I can demonstrate sequential updating and sufficiency.
- [ ] I can quantify prior sensitivity in prior-equivalent sample units.
