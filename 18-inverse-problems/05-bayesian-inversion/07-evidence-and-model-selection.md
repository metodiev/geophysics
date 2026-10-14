---
id: 18-05-07
title: "Bayesian Evidence and Model Selection"
level: research
prereqs: ["18-05-01", "18-05-03", "18-05-06"]
tags: [inverse-problems, bayesian, uncertainty-quantification, evidence, model-selection, bayes-factors, occam]
---

# Bayesian Evidence and Model Selection

All models and data in this module are **SYNTHETIC**. The polynomial family, the
coefficient prior width and the noise level are chosen teaching values. Every
number quoted is printed by
[`code/evidence_and_model_selection_demo.py`](./code/evidence_and_model_selection_demo.py).

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** the evidence (marginal likelihood) as an integral over the
   parameters, and **explain** why it is the normalising constant of one model and
   the comparison criterion between models.
2. **Derive** the exact evidence for a linear-Gaussian model by integrating the
   coefficients out analytically.
3. **Decompose** the evidence into a best-fit likelihood and an Occam factor, and
   **verify** numerically that the factor equals the ratio of posterior to prior
   volume times the prior density at the mode.
4. **Derive** the Laplace approximation to the evidence and state the conditions
   under which it is exact.
5. **Compare** the evidence against BIC and AIC, and state precisely the different
   questions they answer.
6. **Compute** a Bayes factor and read it with the prior width attached, including
   the Jeffreys-Lindley behaviour.
7. **Explain** why model selection consistency is an asymptotic statement, and
   demonstrate that a finite sample can select the wrong model.

## Prerequisites

- [18-05-01 Bayes' Theorem as an Inverse-Problem Formulation](01-bayes-inverse-formulation.md)
  — the posterior and its normalising constant.
- [18-05-03 Priors: Informative, Reference and Their Influence](03-priors.md) —
  the prior width whose effect on the evidence is measured in Section 6.
- [18-05-06 Posterior Summaries](06-posterior-summary.md) — the posterior volume
  that appears in the Occam factor.
- [18-08-02 Synthetic Testing, Checkerboards and Recovery Tests](../08-practical-inversion-workflow/02-synthetic-testing.md)
  — the workflow in which model selection is used.

## 1. Intuition: models are compared the way parameters are estimated

Given two candidate models $M_0$ and $M_1$ that predict the same data, which
should be reported? A hypothesis test answers a question about a null model. The
Bayesian answer compares the **probabilities of the data under each model**,
integrated over everything the model leaves free:

$$
\frac{p(M_1\mid d)}{p(M_0\mid d)}
= \frac{p(d\mid M_1)}{p(d\mid M_0)}\cdot\frac{p(M_1)}{p(M_0)}
= B_{10}\cdot\frac{p(M_1)}{p(M_0)} .
$$

The ratio of evidences $B_{10}$ is the **Bayes factor**. With equal model priors
it is the posterior odds.

The quantity $p(d\mid M)$ is the *only* thing one model can contribute, and it is
subtle: it is not the fit, and it is not the best-fit likelihood. It is the
average of the likelihood over the prior. A model that can fit the data well only
in a tiny corner of its parameter space has a small evidence, because most of the
average is spent on parameter values that fit badly. That is where Occam's razor
comes from in this framework — not from a penalty term bolted on, but from the
averaging itself.

## 2. Definition and the exact linear-Gaussian case

$$
p(d\mid M) = \int p(d\mid c, M)\,p(c\mid M)\,\mathrm{d}c .
$$

In general this integral is as hard as any other high-dimensional integral, and it
is the reason the evidence is harder to compute than the posterior — the posterior
is a *measure* and can be sampled, whereas the evidence is a *number*. Two routes
are available: analytic for special models, and semi-analytic when the integrand
is nearly Gaussian.

**The analytically tractable case.** Let $c \sim \mathcal{N}(0,\tau^2 I)$ be the
coefficients of a linear model with design matrix $\Phi$ (columns $\phi_j$, one
row per datum $x_i$), and let the data be $d = \Phi c + e$ with
$e \sim \mathcal{N}(0,\sigma^2 I)$ and $\sigma$ known. Then $d$ is linear in a
Gaussian, so marginally

$$
d \sim \mathcal{N}\!\left(0,\ \sigma^2 I + \tau^2\Phi\Phi^{\top}\right),
$$

because $\operatorname{Cov}(\Phi c) = \tau^2\Phi\Phi^{\top}$. The evidence follows
in closed form:

$$
\ln p(d\mid M) = -\frac{1}{2}\Bigl[N\ln 2\pi + \ln\lvert C\rvert + d^{\top}C^{-1}d\Bigr],
\qquad
C = \sigma^2 I + \tau^2\Phi\Phi^{\top}.
$$

This is what the demonstration evaluates for polynomial orders $k = 0,1,2,3$; it
is the exact answer, not an approximation, and it is the reference against which
the Laplace approximation and numerical quadrature are checked.

## 3. The Occam factor, derived and measured

Take the posterior mode $\hat c$ and approximate the integrand by a Gaussian around
it. Writing $H = -\nabla\nabla\ln p(c\mid d)$ for the negative Hessian at the mode,

$$
p(d\mid M) = \int p(d\mid c,M)p(c\mid M)\mathrm{d}c
\;\approx\;
p(d\mid\hat c,M)\,p(\hat c\mid M)\,(2\pi)^{M/2}\,\lvert H\rvert^{-1/2}.
$$

Group the terms after the best-fit likelihood:

$$
\underbrace{p(\hat c\mid M)\,(2\pi)^{M/2}\lvert H\rvert^{-1/2}}
_{\text{Occam factor}}
=
\underbrace{\frac{V_{\text{post}}}{V_{\text{prior}}}}_{\text{volume ratio}}
\times
\underbrace{\frac{p(\hat c\mid M)}{\max_c p(c\mid M)}}_{\text{prior at the mode}},
$$

since $(2\pi)^{M/2}\lvert H\rvert^{-1/2}$ is the posterior volume of the Gaussian
approximation and $p(\hat c\mid M)$ carries the reciprocal of the prior volume.

The **volume ratio** is the whole idea. A model with more parameters has a larger
prior volume; unless the likelihood shrinks that volume by at least as much, the
evidence falls. The demonstration verifies the decomposition numerically on the
12-point SYNTHETIC data set (Sections 4–5), and the two sides agree to five
decimal places:

| $k$ | Occam factor $p(d\mid M_k)/e^{\ln\mathcal{L}(\hat c)}$ | posterior/prior volume | prior at the mode | product |
|---|---|---|---|---|
| 0 | 0.12608 | 0.14286 | 0.88256 | 0.12608 |
| 1 | 0.02030 | 0.03202 | 0.63412 | 0.02030 |
| 2 | 0.00523 | 0.01211 | 0.43162 | 0.00523 |
| 3 | 0.00193 | 0.00683 | 0.28173 | 0.00193 |

The volume ratio falls by a factor of $4.5$, then $2.6$, then $1.8$ as the order
rises, while the best-fit likelihood improves each time. The product is what the
evidence reports.

## 4. Worked example: evidence, BIC and AIC on one data set

The SYNTHETIC data are $12$ points on $x \in [-1,1]$ generated from
$y = 0.5 + x$ with $\sigma = 0.5$ noise; the coefficient prior is
$\mathcal{N}(0,1^2)$ and the model prior is uniform over $k = 0,\dots,3$. The
demonstration reports:

| $k$ | dim | log evidence | BIC | AIC | posterior $P(M_k)$ |
|---|---|---|---|---|---|
| 0 | 1 | $-20.4768$ | 39.297 | 38.812 | 0.0015 |
| 1 | 2 | $-15.3904$ | 27.957 | 26.987 | 0.2351 |
| 2 | 3 | $-14.8061$ | 26.560 | 25.105 | **0.4218** |
| 3 | 4 | $-15.0170$ | 27.468 | 25.528 | 0.3416 |

with

$$
\text{BIC} = -2\ln\mathcal{L}_{\max} + M\ln N,
\qquad
\text{AIC} = -2\ln\mathcal{L}_{\max} + 2M .
$$

Three observations, each of which is a general lesson.

**The evidence prefers the quadratic, and the data were generated by a straight
line.** With $12$ points and a coefficient prior of width $1$, the marginal
likelihood of $k=2$ is slightly higher than that of $k=1$. This is not a bug; it
is the finite-sample behaviour of an average over a prior. Section 7 shows the
sample-size dependence.

**BIC and AIC disagree with each other and with the evidence.** BIC prefers $k=2$
too, by a slightly larger margin; AIC has the smallest penalty and would rank
$k=2$ and $k=3$ almost equally. The formulas are all derived from approximations
to the evidence under different conditions, so their disagreement is expected
rather than alarming. What matters is to say which criterion was used:
AIC estimates the expected predictive performance of the fitted model; BIC
approximates $-2$ times the log evidence under a particular prior; the evidence
itself is what the Bayes factor requires.

**The best-fit likelihood always improves with order.** Any model of order $k+1$
contains every model of order $k$, so $\mathcal{L}_{\max}$ cannot fall. The
measured best-fit log-likelihoods are

$$
-18.4059,\quad -11.4934,\quad -9.5524,\quad -8.7642
\ \text{in decreasing order of } k,
$$

yet the evidence rises then falls. That gap *is* the Occam factor, and quoting
the best-fit likelihood as evidence of a good model is precisely the error this
framework exists to prevent.

## 5. The Laplace approximation, and when it is exact

Replacing the integrand by a Gaussian gives

$$
\ln p(d\mid M) \approx
\ln\!\bigl[p(d\mid\hat c,M)\,p(\hat c\mid M)\bigr]
+ \frac{M}{2}\ln 2\pi - \frac{1}{2}\ln\lvert H\rvert .
$$

For a linear model with a Gaussian prior and Gaussian noise this is not an
approximation: the integrand *is* Gaussian, so the formula is exact. The
demonstration confirms this:

| $k$ | exact log evidence | Laplace | difference |
|---|---|---|---|
| 0 | $-20.4768$ | $-20.4768$ | $0.000000$ |
| 1 | $-15.3904$ | $-15.3904$ | $-0.000000$ |
| 2 | $-14.8061$ | $-14.8061$ | $0.000000$ |
| 3 | $-15.0170$ | $-15.0170$ | $-0.000000$ |

The residual is at the level of double-precision solver error. The lesson is
two-sided. On the one hand, the Laplace route is cheap and exact enough for
linear-Gaussian problems. On the other, **its accuracy must be verified whenever
the integrand is not Gaussian** — a bounded prior, a nonlinear forward model, or
a multimodal likelihood all break the assumption, and a Laplace evidence that has
not been checked against a second route is a number of unknown quality. The
demonstration provides the second route by brute-force quadrature: for $k=0$ a
$121$-point grid and for $k=1$ a $14\,641$-point grid. The relative errors against
the analytic values are $6.55\times10^{-12}$ and $2.00\times10^{-15}$,
respectively: quadrature and analytics agree.

## 6. Bayes factors and the prior width

The Bayes factor is a ratio of evidences, so it inherits the prior dependence of
each. The demonstration computes $\log_{10}B_{10}$ for a linear model against a
constant, as the coefficient prior width $\tau$ varies:

| $\tau$ | $\log_{10}B_{10}$ | $P(M_0\mid d)$ | $P(M_1\mid d)$ |
|---|---|---|---|
| 0.1 | 0.4410 | 0.2659 | 0.7341 |
| 0.3 | 1.6799 | 0.0205 | 0.9795 |
| 1.0 | 2.2090 | 0.0061 | 0.9939 |
| 3.0 | 1.8753 | 0.0131 | 0.9869 |
| 10.0 | 1.3696 | 0.0409 | 0.9591 |
| 100.0 | 0.3713 | 0.2984 | 0.7016 |

The Bayes factor rises to a maximum near $\tau \approx 1$ and then falls as the
prior is made wider. This is the **Jeffreys-Lindley effect**: as the prior on the
extra parameter becomes diffuse, the evidence of the more complex model is
diluted over a growing parameter volume while its best-fit region does not grow,
so the simpler model is increasingly favoured. In the limit the Bayes factor
becomes arbitrarily large in favour of the simpler model.

The practical consequences:

1. **A Bayes factor without a stated prior width is incomplete.** The measured
   $\log_{10}B_{10}$ spans $0.3713$ to $2.2090$ across the table, a factor of
   $10^{1.8377} = 68.8$ in the Bayes factor itself.
2. **"Evidence" is not the same as posterior belief.** The posterior odds include
   the model prior, which for physical models is rarely uniform — some models are
   more plausible before the data arrive, and saying so is part of the analysis.
3. **Very weak and very strong priors both create artefacts.** A prior so tight
   that the data are irrelevant forces the posterior; a prior so wide that the
   marginal likelihood is dominated by the prior's tails makes the comparison a
   statement about the prior.
4. **Conventions for interpreting a Bayes factor exist, but they are conventions.**
   Report the number, the prior, and what decision it changes; do not report a
   verbal label as if it were a calculation.

## 7. Does the evidence find the true model as the sample grows?

The Occam penalty for an extra coefficient grows roughly as
$\frac{1}{2}M\ln N$ in the BIC approximation, while a spurious improvement in the
best-fit likelihood does not grow with $N$. The demonstration re-runs the whole
comparison with the same family and prior width but different sample sizes:

| $n$ | $\log_{10}B_{21}$ | $P(k=0)$ | $P(k=1)$ | $P(k=2)$ | $P(k=3)$ |
|---|---|---|---|---|---|
| 12 | 0.2538 | 0.0015 | 0.2351 | 0.4218 | 0.3416 |
| 24 | 0.7000 | 0.0000 | 0.1173 | 0.5879 | 0.2949 |
| 48 | $-0.5329$ | 0.0000 | **0.7074** | 0.2074 | 0.0853 |
| 96 | 0.0357 | 0.0000 | 0.3680 | 0.3995 | 0.2325 |

The sequence is not monotone. At $n = 12$ and $n = 24$ the quadratic is preferred;
at $n = 48$ the evidence moves to the true linear model, as consistency predicts;
at $n = 96$ this particular noise realisation pushes it back to the quadratic.
The honest reading is the correct one and it matters for reporting:

- Model selection consistency is a statement about the limit as $n\to\infty$ along
  a fixed data-generating process; it says nothing about one data set.
- A Bayes factor is a **decision made on the data at hand**. It should be
  reported with the probability of the alternatives, and its sensitivity to the
  prior should be quantified, not concealed behind a single number.
- Where the decision matters, add an independent diagnostic: a synthetic recovery
  test, a residual analysis, or a second data type. That is the subject of
  [18-08-02](../08-practical-inversion-workflow/02-synthetic-testing.md).

## 8. Alternatives and their place

Three other criteria are commonly used, and it is worth being precise about what
each measures.

- **$F$-tests and likelihood-ratio tests** compare nested models and require the
  models to be nested and the asymptotic distribution of the statistic to be
  valid. They give a $p$-value, not a probability that a model is correct.
- **AIC** estimates the expected predictive performance of the fitted model,
  targeting the model that would predict best, and is asymptotically equivalent
  to leave-one-out cross-validation. It deliberately does not target the true
  model, and it cannot be used as a posterior model probability.
- **Cross-validation** estimates predictive performance directly and needs no
  likelihood normalisation, at the cost of recomputing the inversion for each
  fold — an entirely practical matter when each inversion is a large forward
  solve.

For a decision that needs a probability over models, the evidence is the right
object. For a decision that needs a predictor, a predictive criterion may be the
better and cheaper tool.

## 9. Assumptions and regime of validity

1. **The evidence is a prior average.** Any statement about it is conditional on
   the prior, and the measured Jeffreys-Lindley table shows how much.
2. **The model prior matters as much as the likelihood.** Equal priors are a
   default, not a finding.
3. **Numerical evidence needs two routes.** The demonstration's Laplace values
   happen to be exact; in a nonlinear problem they are not, and the quadrature or
   thermodynamic check is mandatory.
4. **Nested families hide non-uniqueness.** A polynomial of order $k$ is not a
   physical model; in real work the candidate models should be physically
   distinguishable, or the comparison degenerates into curve fitting.
5. **Beware improper priors in a Bayes factor.** A Bayes factor between improper
   priors is meaningless, because the ratio of two arbitrary constants is
   arbitrary. Use proper priors, or state the truncation that makes them proper.
6. **The evidence is one number per model.** It cannot report *where* models
   disagree; the difference of posteriors is often more useful than the ratio of
   evidences.

## 10. Demonstration and exercises

[`code/evidence_and_model_selection_demo.py`](./code/evidence_and_model_selection_demo.py)
computes the exact evidence, the Laplace approximation, the Occam decomposition,
the BIC and AIC comparisons, the prior-width sweep and the sample-size sweep, and
verifies the analytics against grid quadrature. It prints all tables above with
units and exits $0$ in about a third of a second. Exercises and solutions:
[`exercises/07-evidence-and-model-selection-exercises.md`](./exercises/07-evidence-and-model-selection-exercises.md),
[`exercises/07-evidence-and-model-selection-solutions.md`](./exercises/07-evidence-and-model-selection-solutions.md).

## Mastery checkpoint

**(a)** Derive the marginal distribution of $d$ for a linear-Gaussian model with
prior $\mathcal{N}(0,\tau^2I)$, and state the covariance.
**(b)** For an $M$-parameter model, show that the Occam factor falls as
$\tau^{-M}$ when the prior is widened and the data information is fixed.
**(c)** A colleague reports $B_{10} = 30$ supporting a two-layer model. List the
three pieces of information required before that number can be interpreted.
**(d)** Explain why an AIC difference cannot be converted into a posterior model
probability.
**(e)** Using the measured table of Section 7, state whether the sample-size study
supports the claim "the evidence identifies the true model at $n\ge 48$".

## Common pitfalls

1. **Quoting the best-fit likelihood as evidence.** The measured best-fit
   likelihood improves with every added coefficient; the evidence does not.
2. **Reporting a Bayes factor without the prior width.** Measured to move by a
   factor of $70$ in $\log_{10}$ terms across plausible widths.
3. **Treating the Bayes factor as a $p$-value.** It is a ratio of averaged
   likelihoods, with no sampling distribution involved.
4. **Using improper priors.** The ratio is then arbitrary.
5. **Assuming the Laplace approximation is exact.** It was here, and the
   demonstration shows why: the integrand was Gaussian. Check, do not assume.
6. **Believing a model-selection result is a proof of the model.** Section 7
   demonstrates that a finite sample can prefer the wrong model.
7. **Comparing models that are not physically distinguishable.** The result is
   then a statement about the parameterisation, not about the Earth.

## Further reading

- **Kass, R. E., & Raftery, A. E. (1995). Bayes factors. *Journal of the American
  Statistical Association*, 90(430), 773–795.** Level: research. Definitions,
  approximations and the interpretation conventions of Section 6.
- **Lindley, D. V. (1957). A statistical paradox. *Biometrika*, 44(1/2),
  187–192.** Level: research. The original statement of the effect measured in
  Section 6.
- **Bartlett, M. S. (1957). A comment on D. V. Lindley's statistical paradox.
  *Biometrika*, 44(3/4), 533–534.** Level: research. The response that clarifies
  why the paradox is a property of the prior, not a defect of Bayes' theorem.
- **MacKay, D. J. C. (2003). *Information Theory, Inference, and Learning
  Algorithms*. Cambridge University Press.** Level: research. The Occam factor
  derived as a volume ratio, in the form used in Section 3.
- **Gelman, A., Hwang, J., & Vehtari, A. (2014). Understanding predictive
  information criteria. *Statistics and Computing*, 24(6), 997–1016.** Level:
  research. Why AIC, DIC, WAIC and cross-validation answer predictive questions
  and not model-probability questions.

## Related modules

- [01 Bayes' Theorem as an Inverse-Problem Formulation](01-bayes-inverse-formulation.md).
- [03 Priors: Informative, Reference and Their Influence](03-priors.md).
- [06 Posterior Summaries](06-posterior-summary.md) — the posterior volume that
  appears in the Occam factor.
- [08 Trans-Dimensional and Reversible-Jump MCMC](08-trans-dimensional.md) — an
  alternative route to the same probabilities that never computes an integral.
- [18-08-02 Synthetic Testing, Checkerboards and Recovery Tests](../08-practical-inversion-workflow/02-synthetic-testing.md).
- [18-08-04 Reporting Inversion Results Responsibly](../08-practical-inversion-workflow/04-reporting-inversion.md).
