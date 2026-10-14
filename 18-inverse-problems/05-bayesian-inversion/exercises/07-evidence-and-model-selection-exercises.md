# Exercises — 18-05-07 Bayesian Evidence and Model Selection

Lesson: [07 Bayesian Evidence and Model Selection](../07-evidence-and-model-selection.md).
Attempt these before reading the [solutions](./07-evidence-and-model-selection-solutions.md).
All models are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** Derive the marginal distribution of $d$ for a linear model
$d = \Phi c + e$ with $c\sim\mathcal{N}(0,\tau^2I)$ and
$e\sim\mathcal{N}(0,\sigma^2I)$, and state the covariance of $d$.

**★2.** Show that when the prior is widened, $\tau \to \alpha\tau$, the Occam
factor of an $M$-parameter model falls like $\alpha^{-M}$ if the posterior volume
is unchanged.

**★3.** Write the formulas for BIC and AIC, and state in one sentence the question
each answers.

## ★★ Applied

**★★4.** For four SYNTHETIC data $y = (1.1,\,0.9,\,1.2,\,0.8)$, a model
$y = c + e$ with $\sigma = 0.5$, and a prior $c\sim\mathcal{N}(0,1)$, compute:
(a) the posterior mode $\hat c$ and its posterior standard deviation; (b) the exact
log evidence; (c) the Laplace approximation and its difference from the exact
value; (d) the Occam factor and its decomposition into a volume ratio and the
prior density at the mode.

**★★5.** Continuing ★★4, compute BIC and state whether BIC and the exact log
evidence would agree on comparing this model with a two-parameter model, given that
the two-parameter best-fit log likelihood is $-1.05$.

**★★6.** A Bayes factor of $B_{10} = 30$ is reported for a two-layer over a
one-layer model, with equal model priors. Compute the posterior probability of each
model, then state the three additional pieces of information required before the
number can be interpreted.

## ★★★ Research-oriented

**★★★7.** Design a model-selection study for choosing the number of layers in a
synthetic 1-D velocity profile. State the family, the priors, the criterion, the
verification route for the evidence calculation, and how you would demonstrate that
the selection is not an artefact of the prior width.

**★★★8.** Explain the Jeffreys-Lindley effect in terms of averaged likelihoods, and
state what it implies for the practice of reporting Bayes factors in a field where
prior widths are conventional rather than physical.
