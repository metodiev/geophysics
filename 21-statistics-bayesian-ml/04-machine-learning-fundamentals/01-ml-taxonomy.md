---
id: 21-04-01
title: "ML Taxonomy: Supervised, Unsupervised, Reinforcement"
level: advanced
prereqs: ["01-13-06", "21-01-04"]
estimated_minutes: 55
tags: [machine-learning, taxonomy, supervised-learning, unsupervised-learning, reinforcement-learning]
---

# ML Taxonomy: Supervised, Unsupervised, Reinforcement

## Learning objectives

By the end of this lesson you will be able to:

1. **Classify** a learning problem as supervised, unsupervised or reinforcement
   learning from its data and its objective.
2. **Write** the empirical risk minimisation objective and **name** the loss for
   regression, classification and clustering.
3. **Distinguish** the i.i.d. sampling assumption from the sequential assumption
   of reinforcement learning, and **state** what breaks when it fails.
4. **Compute** a linear regression by gradient descent and **verify** it against
   the closed form.
5. **Interpret** an unsupervised objective as a statement about structure rather
   than about truth.
6. **State** which paradigm a geophysical task belongs to and what its labels or
   rewards actually are.

All data in this lesson are **SYNTHETIC**, generated in the demonstration. No
measured value is used, and no accuracy quoted below transfers to a real data
set.

## Prerequisites

- [01-13-06 Point Estimation, Bias, Consistency and Efficiency](../../01-mathematics/13-probability-and-statistics-foundations/06-estimation-theory.md) —
  the estimation framework that empirical risk minimisation generalises.
- [21-01-04 Linear, Multiple and Robust Regression](../01-statistics-in-practice/04-regression.md) —
  the regression the first section re-derives as learning.
- [21-03-06 Bayesian Workflow and Principled Model Building](../03-bayesian-inference/06-bayesian-workflow.md) —
  the model-checking discipline that machine learning inherits.

## 1. Intuition: three questions, three data structures

Machine learning is not one method but three questions asked of three kinds of
data:

- **Supervised learning** has paired examples $(x_i, y_i)$ and asks for a
  function that predicts $y$ from $x$. It is regression if $y$ is continuous and
  classification if it is a label.
- **Unsupervised learning** has only $x_i$ and asks for structure — clusters,
  latent factors, densities. The objective must be invented, because there is no
  $y$ to compare against.
- **Reinforcement learning** has an agent that acts and receives rewards, and
  asks for a policy that maximises cumulative reward. The data are generated
  *by* the learner, so the i.i.d. assumption is replaced by a sequential one.

The distinction is not academic. It determines what can be validated: a
supervised model is validated on held-out pairs, an unsupervised model only
against internal criteria or domain judgement, and a reinforcement learner only
by the reward it accumulates in the environment.

## 2. Supervised learning as empirical risk minimisation

Given a loss $\ell$ and a hypothesis class $\mathcal F$, the learner solves

$$\hat f = \arg\min_{f \in \mathcal F} \frac{1}{n}\sum_{i=1}^{n}
\ell\big(y_i, f(x_i)\big) + \lambda\,\Omega(f),$$

where the first term is the **empirical risk** and $\Omega$ the **regulariser**.
The standard losses are the squared error $\ell = (y - f(x))^{2}$ for regression,
the logistic (cross-entropy) loss
$\ell = -y\ln p - (1-y)\ln(1-p)$ for binary classification, and the hinge loss
for a margin classifier. Ridge regression, logistic regression, support vector
machines and neural networks are all instances of this one template, differing
only in $\mathcal F$, $\ell$ and $\Omega$.

The assumption that makes the empirical average estimate the true risk is that
the examples are **i.i.d. draws from the same distribution** as the examples the
model will meet in use. Every failure of generalisation in this module — leakage,
non-stationarity, extrapolation — is a failure of that assumption in disguise.

## 3. Unsupervised learning as invented structure

Without labels there is no risk to minimise, so an objective must be chosen. Two
standard choices:

$$k\text{-means:} \quad \min_{\{C_j\}} \sum_{j=1}^{k}\sum_{x \in C_j}
\|x - \mu_j\|^{2}, \qquad
\text{PCA:} \quad \max_{u:\|u\|=1} \operatorname{Var}(u^{\mathsf T}x).$$

Both are statements about *what structure should be considered interesting*.
k-means asserts that clusters are spherical and equal in scale; PCA asserts that
high variance is signal. Neither is a claim about the data-generating process, and
a model that optimises them well can still be describing noise — which is why an
unsupervised result is validated by an external criterion, not by its objective.

## 4. Reinforcement learning and the sequential assumption

An agent observes a state $s_t$, takes an action $a_t$, receives reward $r_t$ and
transitions to $s_{t+1}$, seeking to maximise

$$J = \mathbb E\Big[\sum_{t=0}^{\infty}\gamma^{t} r_t\Big], \qquad \gamma \in [0,1).$$

Two features distinguish it from the other paradigms. The **data distribution
depends on the policy**: acting well changes what is observed, so the agent must
explore to learn and exploit to score, and the trade between them is the central
difficulty. And the **reward is the only supervision**, so credit must be
assigned across long sequences of actions — a problem with no analogue in
supervised learning.

## 5. Worked example

The demonstration implements one small instance of each paradigm.

**Supervised regression.** $200$ points from $y = 1.5 + 0.8x + \mathcal N(0,
0.3^{2})$. Four hundred steps of gradient descent with rate $0.1$ reach
$\hat\beta_0 = 1.4900$, $\hat\beta_1 = 0.7870$ against the truth $1.5$ and $0.8$,
and the normal equations give identical values to four decimals. The training MSE
is $0.0859$ against a noise variance of $0.09$ — the model has recovered the
signal and no more. That agreement is the sanity check every learner should
pass: when a closed form exists, gradient descent must reproduce it.

**Supervised classification.** $400$ points with log-odds $1.2x_1 - 0.8x_2$
give fitted coefficients $+0.9111$ and $-0.8054$ on the two features with an
intercept of $+0.1103$, recovering the true signs and approximate magnitudes, and
a training accuracy of $0.7125$ against a base rate of $0.5150$. The accuracy is
well above chance but far from perfect, because the label was drawn from the
probabilities rather than thresholded — the intrinsic noise caps what any model
can achieve, which is the subject of
[21-04-02](02-bias-variance.md).

**Unsupervised clustering.** Three Gaussian clouds of $100$ points each give a
within-cluster sum of squares of $1230.23$ at $k = 2$, $303.25$ at $k = 3$,
$260.47$ at $k = 4$ and $223.85$ at $k = 5$. The objective falls monotonically,
so it cannot choose $k$; the elbow between $k = 3$ and $k = 4$ does, and the
recovered cluster sizes at $k = 3$ are $[100, 100, 100]$ — the truth.

**Reinforcement learning.** A four-armed bandit with means
$(0.20, 0.50, 0.65, 0.40)$ and an $\epsilon = 0.1$ greedy policy over $2000$
pulls earns $1269$ of a possible $1300$ reward, a regret of $31$ units or
$2.4\ \%$. The pulls are $39, 54, 1857, 50$: the policy explores everywhere and
concentrates on the best arm, which is the explore-exploit trade made visible.

## Assumptions and regime of validity

1. **i.i.d. sampling for supervised and unsupervised learning.** Non-stationarity,
   leakage and shifting distributions break it, and the model degrades silently.
2. **The loss must match the decision.** Squared error on a skewed target weights
   large values; cross-entropy on an imbalanced problem needs a reweighted
   threshold.
3. **The hypothesis class must contain the truth, or a good approximation.**
   A model that cannot represent the relationship will not find it.
4. **Unsupervised objectives are choices.** k-means asserts spherical clusters;
   PCA asserts that variance is signal.
5. **Reinforcement learning needs a stationary environment and a defined reward.**
   A reward that is wrong or a policy that corrupts the data produces confident,
   useless policies.
6. **Regularisation is not optional.** Without $\Omega$, empirical risk
   minimisation will fit noise; see
   [21-04-04](04-regularization-ml.md).

## The honest summary

The three paradigms differ in what they can be validated against, and that
difference matters more than the algorithms. In the demonstration a gradient
descent reproduced the closed-form regression coefficients to three decimals and
a clustering objective found the true three groups — but only because the data
were generated to be exactly what the models assume. The $2.4\ \%$ bandit regret
is a statement about a stationary bandit with known reward means, not about any
geophysical decision problem. What the numbers do **not** establish is that a
model will generalise: that requires the i.i.d. assumption, a held-out sample,
and the checks of [21-04-03](03-model-assessment.md).

## Python demonstration

[`code/ml_taxonomy_demo.py`](./code/ml_taxonomy_demo.py) prints every number
quoted above. It:

1. fits a linear model by gradient descent and compares it with the closed form;
2. fits a logistic regression and reports coefficients and accuracy;
3. runs k-means for several $k$ and reports the within-cluster sum of squares;
4. runs an $\epsilon$-greedy bandit and reports regret.

```bash
cd 21-statistics-bayesian-ml/04-machine-learning-fundamentals/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python ml_taxonomy_demo.py
```

It runs in about a tenth of a second and prints only text.

## Exercises

Graded problems are in
[`exercises/01-ml-taxonomy-exercises.md`](./exercises/01-ml-taxonomy-exercises.md)
with worked solutions in
[`exercises/01-ml-taxonomy-solutions.md`](./exercises/01-ml-taxonomy-solutions.md).

## Mastery checkpoint

Without notes, a gradient-descent fit of $y = 1.5 + 0.8x$ reaches
$\hat\beta = (1.4900, 0.7870)$ with training MSE $0.0859$, and a $k$-means run
gives within-cluster sums of squares $1230.23$, $303.25$, $260.47$ for
$k = 2, 3, 4$.

1. Compute the training MSE you would expect if the model recovered the truth
   exactly, given a noise standard deviation of $0.3$.
2. State why the clustering objective cannot choose $k$.
3. Classify these tasks: (i) predicting lithology from well logs, (ii) finding
   facies without labels, (iii) choosing a drilling location to maximise
   information. State the paradigm of each.
4. State the assumption that supervised learning makes about the data it will
   meet in deployment.

## Common pitfalls

1. **Confusing the objective with truth.** An unsupervised objective is a choice;
   a low value is not evidence of real structure.
2. **Validating a supervised model on its training data.** It measures memory,
   not generalisation.
3. **Ignoring the base rate.** An accuracy of $84\ \%$ means little without the
   class balance.
4. **Applying supervised methods to a non-stationary process.** The i.i.d.
   assumption fails and the error estimate is optimistic.
5. **Treating a reward as a ground truth.** In reinforcement learning the reward
   *is* the specification, and the model optimises it whether or not it is right.
6. **Skipping the closed-form check.** Every learner should be tested where the
   answer is known.

## Where this is used

- **Supervised**: lithology prediction from logs, phase picking, magnitude
  estimation, denoising with paired examples.
- **Unsupervised**: facies clustering, seismic attribute analysis, anomaly
  detection in monitoring networks.
- **Reinforcement learning**: adaptive survey design, sensor placement,
  sequential drilling decisions, and control of active sources.
- **Hybrid**: self-supervised pretraining followed by supervised fine-tuning, the
  subject of [21-05-07](../05-deep-learning/07-self-supervised.md).

## Related lessons

- [21-04-02 Bias-Variance Trade-Off, Underfitting and Overfitting](02-bias-variance.md) —
  what the empirical risk does not capture.
- [21-04-03 Cross-Validation, Metrics and the Danger of Leakage](03-model-assessment.md) —
  how the i.i.d. assumption is tested.
- [21-04-08 Clustering and Unsupervised Structure Discovery](08-clustering.md) —
  the unsupervised paradigm in detail.
- [21-04-04 Regularisation: Ridge, Lasso, Early Stopping](04-regularization-ml.md) —
  the $\Omega$ term of the empirical risk.
- [21-06-09 Pitfalls: Spurious Correlations, Non-Stationarity, Extrapolation](../06-ml-in-geophysics/09-ml-pitfalls-geophysics.md) —
  what happens when the assumptions of this lesson fail on real Earth data.

## Self-assessment checklist

- [ ] I can classify a task into one of the three paradigms.
- [ ] I can write empirical risk minimisation and name the standard losses.
- [ ] I can state the i.i.d. assumption and what breaks it.
- [ ] I can reproduce a closed-form solution by gradient descent.
- [ ] I can explain why an unsupervised objective cannot validate itself.
- [ ] I can state the explore-exploit trade and why it has no supervised analogue.
