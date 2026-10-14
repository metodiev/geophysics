---
id: 01-13-01
title: "Probability Axioms, Conditional Probability and Bayes' Rule"
level: intermediate
prereqs: ["01-01-05", "01-02-05"]
estimated_minutes: 90
tags: [probability, bayes-rule, conditional-probability, uncertainty, base-rates]
---

# Probability Axioms, Conditional Probability and Bayes' Rule

## Learning objectives

By the end of this lesson you will be able to:

1. **State** the three Kolmogorov axioms and use them operationally — the
   complement rule, inclusion–exclusion for a union, and additivity for
   disjoint events — without consulting a text.
2. **Define** conditional probability from its ratio, distinguish $P(A \mid B)$
   from $P(B \mid A)$, and decide when two events may be treated as independent
   and when that assumption is a physical claim rather than a convenience.
3. **Derive** Bayes' rule in two lines from the definition of conditional
   probability, and use it in both its probability form and its odds form.
4. **Update** a discrete subsurface model as measurements accumulate, and
   explain why the order of measurements does not matter.
5. **Compute** the positive predictive value of a detection from a prior, a
   sensitivity and a specificity, and explain why rare-target detection is hard
   even with a good instrument.
6. **Identify** the assumptions on which a Bayesian update rests — the
   likelihood model, the prior, and the independence of successive data — and
   state what happens when they fail.

## Prerequisites

[01-01-05 Absolute vs Relative Error, Conditioning and Stability](../01-arithmetic/05-error-and-conditioning.md)
for the vocabulary of uncertainty, and
[01-02-05 Linear and Nonlinear Systems of Equations](../02-algebra/05-systems-of-equations.md)
for the idea of a model with free parameters. The linear-algebra picture of a
survey as a map from model space to data space, developed in
[01-07 Linear Algebra](../07-linear-algebra/README.md), is used for framing but
is not yet needed mathematically.

## 1. Why probability is the natural language of measurement

Every number a geophysicist reports is a measurement of something that is not
directly accessible. A gravimeter does not weigh the Earth; it reports a voltage
that depends on the local acceleration, on the instrument's internal state, on
the tide, on the elevation of the ground beneath it, and on a dozen corrections
that were applied to the raw reading. A travel time is not a rock property: it
is a pick. A resistivity is not a rock property either, at least not until you
have assumed a model in which a resistivity may appear.

There are therefore two distinct reasons a geophysical statement is uncertain,
and it pays to keep them apart from the first lesson:

- **Measurement uncertainty.** The quantity being measured has a definite value
  (or would have, if the experiment were different), but the instrument and the
  environment add noise. Repeat readings differ.
- **Model uncertainty.** The quantity of interest does not exist independently
  of the parameterisation. Asking for "the depth to basement" presupposes a
  definition of basement and a geometry; different defensible choices give
  different answers, and no improvement in instrumentation resolves the
  disagreement.

Probability is the apparatus that lets both be expressed in the same units and
propagated together. The purpose of this module is to build that apparatus, and
the purpose of this lesson is to lay the foundation stone: the axioms, and the
single most useful formula in the whole subject — Bayes' rule.

**The governing attitude of the module.** Uncertainty is not a confession of
weakness appended to a result. It is a physical quantity with units, a
magnitude, and a behaviour under averaging. A depth of $750 \pm 26$ m and a depth
of $750$ m are different scientific claims, and only the first is honest.

## 2. Sample space, events and the three axioms

### 2.1 The sample space

An **experiment** is any procedure with an uncertain outcome. The **sample
space** $\Omega$ is the set of all outcomes that could occur. An **event** $A$ is
a subset of $\Omega$; $P(A)$ is a number attached to that subset.

The sample space must be fixed *before* probabilities are assigned, and choosing
it is a modelling decision, not a mathematical one. In a gravity survey:

- If one measurement is made at one station, then a natural $\Omega$ is the
  real line: every possible reading is an outcome, and "the reading exceeds
  979 812.30 mGal" is an event.
- If instead the outcome of interest is whether the reading is contaminated by a
  passing vehicle, then $\Omega = \{\text{clean}, \text{contaminated}\}$ and the
  reading itself is not modelled at all.

Both are legitimate. The second is not an approximation of the first; it answers
a different question. Most of the difficulty in applying probability in the
Earth sciences lies here, in deciding what the experiment actually is.

### 2.2 The axioms

Kolmogorov's axioms, in the form used throughout this module:

$$
\begin{aligned}
&\text{(A1) Non-negativity:} && P(A) \ge 0 \quad \text{for every event } A, \\
&\text{(A2) Normalisation:} && P(\Omega) = 1, \\
&\text{(A3) Additivity:} && P(A \cup B) = P(A) + P(B) \quad \text{if } A \cap B = \varnothing.
\end{aligned}
$$

(A3) is stated for two events; the full axiom extends it to any countable
collection of pairwise disjoint events. Everything else in probability theory is
derived from these three lines.

Three immediate consequences, all of which get used constantly:

**Complement.** Since $A$ and its complement $A^{c}$ are disjoint and their
union is $\Omega$, (A3) and (A2) give

$$P(A^{c}) = 1 - P(A).$$

**Union of overlapping events (inclusion–exclusion).** $A \cup B$ can be written
as the union of the disjoint pieces $A$ and $B \setminus A$, and independently
as $(A \cap B) \cup (B \setminus A) \cup (A \setminus B)$. Comparing the two
decompositions gives

$$P(A \cup B) = P(A) + P(B) - P(A \cap B).$$

The subtraction corrects for double counting; the formula reduces to (A3)
exactly when the events are disjoint.

**Monotonicity.** If $A \subseteq B$ then $P(A) \le P(B)$, because
$B \setminus A$ is disjoint from $A$ and has non-negative probability.

### 2.3 The axioms at work

The script `code/probability_axioms.py` walks through a two-station detection
problem. Suppose a regional seismic event registers at each of two stations with
probability $0.85$, independently, and that a station either registers the event
or does not. These are illustrative numbers chosen to make the arithmetic
legible; they are not measurements of any real network.

```
  P(station triggers)              = 0.85
  Axiom 1 (complement): P(no trigger) = 1 - P(trigger) = 0.1500
  Independence: P(both trigger)        = 0.85^2       = 0.7225
  P(at least one) = 1 - P(neither)     = 1 - 0.15^2   = 0.9775
  Inclusion-exclusion check: P(A)+P(B)-P(A and B)     = 0.9775
```

The two routes to $P(\text{at least one})$ — the complement route and
inclusion–exclusion — agree, as they must, and the agreement is a useful check
on any hand calculation. The substantive observation is that going from one
station to two raised the detection probability from $0.85$ to $0.9775$: the
gain from redundancy is largest when the single-station probability is already
high, because the miss probability is what is being squared.

Note carefully what made the calculation possible: the assumption of
**independence**. If the two stations share a power supply, a communications
link, or a software trigger, their failures are correlated and
$P(\text{both trigger}) > 0.85^{2}$. Independence is never a mathematical fact
about instruments; it is a physical claim that must be argued from the
architecture of the experiment, and it is one of the most frequently violated
assumptions in quantitative Earth science.

## 3. Conditional probability

### 3.1 Definition

For events $A$ and $B$ with $P(B) > 0$, the **conditional probability of $A$
given $B$** is

$$P(A \mid B) = \frac{P(A \cap B)}{P(B)}.$$

Read it as a rescaling. Conditioning on $B$ is equivalent to declaring that the
new sample space is $B$; division by $P(B)$ renormalises so that the new total
probability is $1$.

Rearranged, the definition gives the **multiplication rule**:

$$P(A \cap B) = P(A \mid B)\,P(B) = P(B \mid A)\,P(A).$$

Two events are **independent** if $P(A \cap B) = P(A)P(B)$, equivalently
$P(A \mid B) = P(A)$: knowing that $B$ happened tells you nothing about $A$.

### 3.2 The asymmetry that matters

$P(A \mid B)$ and $P(B \mid A)$ are different numbers, generally separated by a
large factor, and confusing them is the single most consequential error in
applied probability. Two examples, both worth memorising:

- $P(\text{travelling through granite} \mid \text{measured velocity } 6.0
  \text{ km/s})$ is not $P(\text{measured velocity } 6.0 \text{ km/s} \mid
  \text{travelling through granite})$. The second is an instrument property; the
  first is a statement about the rock, and it depends on how common granite is
  along the profile.
- $P(\text{orebody} \mid \text{magnetic anomaly})$ is not
  $P(\text{magnetic anomaly} \mid \text{orebody})$. An orebody almost always
  produces an anomaly; an anomaly is very often produced by something else.

The whole of Bayes' rule exists to convert one into the other, and the
conversion factor is the base rate — Section 6.

## 4. Bayes' rule

### 4.1 Derivation

Write the multiplication rule twice:

$$P(A \mid B)P(B) = P(A \cap B) = P(B \mid A)P(A).$$

Divide by $P(B)$, which is positive whenever conditioning on $B$ is meaningful:

$$
\boxed{\,P(A \mid B) = \frac{P(B \mid A)\,P(A)}{P(B)}\,}
$$

That is the entire derivation. It contains no modelling assumption beyond
$P(B) > 0$; every controversy about Bayesian methods concerns the *inputs*, not
the rule.

For a partition $\{H_1, \dots, H_n\}$ of $\Omega$ (mutually exclusive,
collectively exhaustive), the denominator expands by (A3):

$$P(B) = \sum_{k=1}^{n} P(B \mid H_k)\,P(H_k),$$

which is sometimes called the **law of total probability**. Substituting,

$$P(H_j \mid B) = \frac{P(B \mid H_j)\,P(H_j)}{\sum_k P(B \mid H_k)\,P(H_k)}.$$

The four ingredients have standard names, and they are worth using precisely
because they force you to say what you are assuming:

| Term | Name | Geophysical reading |
|---|---|---|
| $P(H_j)$ | **prior** | What you believed about the model before the survey |
| $P(B \mid H_j)$ | **likelihood** | How probable the observed data are if that model holds |
| $P(H_j \mid B)$ | **posterior** | What you believe now |
| $P(B)$ | **evidence** | A normalising constant; it guarantees the posterior sums to 1 |

### 4.2 The odds form, and why it is the working form

Dividing the posterior for hypothesis $H_1$ by that for $H_2$ cancels the
evidence:

$$\frac{P(H_1 \mid B)}{P(H_2 \mid B)} = \frac{P(H_1)}{P(H_2)} \times
\frac{P(B \mid H_1)}{P(B \mid H_2)}.$$

In words: **posterior odds = prior odds × likelihood ratio.** Evidence
accumulates multiplicatively in the odds, or additively in the log-odds, which
is why log-odds are the natural bookkeeping scale for a long campaign of
measurements.

Using the illustrative numbers of Section 5, the prior odds of a low-velocity
wedge against a flat-layered section are $0.40/0.60 = 0.6667$ and the likelihood
ratio is $0.70/0.20 = 3.5$, so the posterior odds are $2.3333$ and the posterior
probability is $2.3333/(1 + 2.3333) = 0.70$. This reproduces the direct
calculation exactly, as it must.

### 4.3 Sequential updating, and order independence

Now feed a second, independent measurement with the same likelihoods into the
first posterior. The script reports:

```
  Prior (from measurement 1): P(H1) = 0.700000
  Evidence P(d2) = 0.550000
  Posterior P(H1|d1,d2) = 0.890909
```

because $0.70 \times 0.70 / (0.70 \times 0.70 + 0.30 \times 0.20) = 0.49/0.55 =
0.890909$. Two independent measurements with a likelihood ratio of $3.5$ each
give posterior odds $0.6667 \times 3.5 \times 3.5 = 8.1667$, hence probability
$0.890909$.

Two observations follow, and both matter for practice.

**Order does not matter.** Updating with $d_1$ then $d_2$ gives the same
posterior as updating with $d_2$ then $d_1$, because both routes multiply the
same three numbers. Bayes' rule is a bookkeeping method for evidence, not a
recipe whose result depends on the sequence of arrival.

**Independence is doing real work here.** The calculation multiplies the two
likelihood ratios as if the measurements were unrelated. Two picks made by the
same analyst on the same record, or two gravity readings at the same station
with the same instrument drift, are not independent, and multiplying their
likelihood ratios overstates the evidence. The honest handling of correlated
data requires a joint likelihood, which is the subject of
[01-13-03 Expectation, Variance and Moments](./03-expectation-variance.md) and
of every real inverse problem in
[18 Inverse Problems](../../18-inverse-problems/README.md).

## 5. Bayesian updating of a subsurface model

The abstract formula becomes concrete the moment the hypotheses are geological.
Consider a refraction profile whose data are a set of travel-time residuals, and
suppose two competing interpretations are on the table:

- $H_1$: a low-velocity wedge is present, $P(H_1) = 0.40$;
- $H_2$: the section is flat-layered, $P(H_2) = 0.60$.

The observed residual is larger than the array's noise level; call that event
$d$. The forward model plus an assumed noise model gives
$P(d \mid H_1) = 0.70$ and $P(d \mid H_2) = 0.20$. Both numbers are *model
outputs*, not data: they come from propagating the assumed velocity structure
and noise distribution into the data space. Then

$$P(d) = 0.40(0.70) + 0.60(0.20) = 0.28 + 0.12 = 0.40,$$

$$P(H_1 \mid d) = \frac{0.28}{0.40} = 0.700.$$

The demonstration script verifies this by simulation — one million synthetic
pairs of (model, data) drawn with seed 20240117:

```
  trials                     = 1,000,000
  analytic  P(H1|d)          = 0.700000
  simulated P(H1|d)          = 0.701248
  difference                 = 0.001248
```

The agreement is what it should be for a million trials, where the standard
error on an estimated proportion near $0.7$ is about $4.6\times10^{-4}$; the
observed difference is under three standard errors.

**What the example teaches, and what it does not.** It teaches the mechanics of
the update and the meaning of each factor. It does not demonstrate that the
likelihoods $0.70$ and $0.20$ are correct; changing them changes the posterior,
and no amount of data analysis will reveal a likelihood that was assumed rather
than measured. In a real study the likelihood comes from the physics of the
forward problem, and the priors come from regional geology, previous surveys, or
explicitly from a requirement that the answer be insensitive to them.

**Continuous parameters.** With a continuous model $m$ and continuous data $d$,
the same rule reads

$$p(m \mid d) \propto p(d \mid m)\,p(m),$$

where the proportionality hides an integral over model space. That expression is
the starting point for every Bayesian inversion, and it is the reason the
inverse-problems literature is full of questions about priors, about
parameterisation, and about whether the posterior can be sampled at all. For
linear forward models with Gaussian noise and Gaussian priors the posterior is
Gaussian in closed form, which is why that case dominates the textbooks; see
[18 Inverse Problems](../../18-inverse-problems/README.md).

## 6. Base rates: why rare-target detection is hard

### 6.1 The arithmetic

Let a target be present with **prevalence** $\pi$ (this is the prior), let a test
detect a present target with **sensitivity** $\text{Se}$, and let it correctly
return negative for an absent target with **specificity** $\text{Sp}$. The
probability of a positive test is

$$P(+) = \text{Se}\,\pi + (1 - \text{Sp})(1 - \pi),$$

and the quantity that matters to the person reading the result is the
**positive predictive value**,

$$\text{PPV} = P(\text{target} \mid +) =
\frac{\text{Se}\,\pi}{\text{Se}\,\pi + (1 - \text{Sp})(1 - \pi)}.$$

The demonstration evaluates this at a prevalence of $0.01$ for two specificities,
with sensitivity held at $0.95$:

```
  prevalence 0.010, sensitivity 0.950, specificity 0.90
    P(positive test)          = 0.108500
    P(target | positive) PPV  = 0.087558  (8.76 % of 'hits' are real)
  prevalence 0.010, sensitivity 0.950, specificity 0.99
    P(target | positive) PPV  = 0.489691  (48.97 % of 'hits' are real)
```

Read those two numbers again. An instrument with $95\%$ sensitivity and $90\%$
specificity, used to hunt a target present in one case in a hundred, produces
positives that are real fewer than one time in eleven. Improving specificity
from $90\%$ to $99\%$ — a modest-sounding change — raises that to about one in
two. The sensitivity was never the problem; the false-positive rate times the
large number of true negatives was.

### 6.2 Why this is a geophysical fact, not a statistical curiosity

The structure is generic: any survey that scans a large region for a rare
target is in this regime. A few examples of the pattern, without attaching
invented numbers to them:

- **Mineral exploration.** An aeromagnetic anomaly is far commoner than an
  orebody. The relevant question after detection is not "did we see an anomaly?"
  but "given that we saw an anomaly, how likely is it that an orebody is
  present?" — and the answer depends on the base rate of orebodies in that
  terrane, which is exactly the quantity nobody measures.
- **Earthquake forecasting.** A precursor signal that appears before some large
  earthquakes is uninformative unless its false-alarm rate is also known. Over a
  catalog with far more quiet days than large events, even a small false-positive
  rate swamps the true positives. This is the substance of the long-running
  criticism of precursor claims.
- **Change detection in InSAR or repeat gravity.** The area surveyed is enormous
  compared with the area that actually deformed or gained mass. A per-pixel
  detection threshold that looks conservative becomes an unmanageable number of
  false alarms when applied to $10^{8}$ pixels.
- **Anomaly picking in geophysical logs.** A detector tuned on a target interval
  can appear to perform well on a test set that is half target; performance is
  governed by the prevalence of the target in the full run.

### 6.3 Simulation check

The script's first Monte Carlo verifies the PPV formula end to end, with seed
20240117:

```
  simulated trials            = 1,000,000
  analytic PPV                = 0.087558
  simulated PPV               = 0.087083
  absolute difference in PPV  = 0.000474
  standard error of simulated PPV = 0.000858  (0.55 SE)
```

The simulated value is well within one standard error of the analytic one. This
is the pattern to insist on throughout the module: a formula and its simulation
should agree, and the *size* of the agreement should be quoted against the Monte
Carlo error, not asserted as "good agreement".

## 7. Combining evidence: naive Bayes

When several measurements are conditionally independent given the model, the
likelihoods multiply and the odds form becomes a sum in log-odds:

$$\log \frac{P(H_1 \mid d_1, \dots, d_n)}{P(H_2 \mid d_1, \dots, d_n)}
= \log\frac{P(H_1)}{P(H_2)} + \sum_{i=1}^{n} \log
\frac{P(d_i \mid H_1)}{P(d_i \mid H_2)}.$$

Each measurement contributes a fixed number of "decibans" of evidence, and the
total is their sum. This decomposition is why the log-odds scale is used for
receiver-operating-characteristic analysis, for the probabilistic interpretation
of potential-field anomaly picks, and for the scoring of geological scenarios.

The word *naive* in naive Bayes is a warning, not a description of the
approximation's quality. Conditional independence is a strong physical claim,
and classification problems in the Earth sciences routinely violate it:
neighbouring seismic traces, adjacent gravity stations, and pixels in a
satellite image are all strongly correlated. When it is violated, the sum
over-counts the evidence, often by a factor comparable to the length of the
correlation scale divided by the sampling interval. The correction is to
subsample to approximately independent measurements, or to model the
correlation explicitly; the correct response is never to ignore it.

## 8. Assumptions and regime of validity

Bayes' rule is a theorem. What may be wrong is everything you put into it.

1. **The sample space is right.** If a rare but real outcome has been left out of
   $\Omega$, the posterior is not merely imprecise, it is excluding a true
   possibility. Model-space truncation is the commonest form of this error.
2. **The likelihood is right.** $P(d \mid m)$ must predict the distribution of
   the *observed* data quantity, including its error structure — bias,
   correlated noise, and outliers. A likelihood that is too narrow produces a
   posterior that is too confident, which is the most damaging failure mode
   because it looks like a strong result.
3. **The prior is defensible.** A prior may be informative (regional geology), or
   weakly informative (bounded ranges on physically positive quantities), or
   deliberately uninformative (a Jeffreys prior for a scale parameter). What it
   may not be is unexamined. The right test is sensitivity: report how much the
   posterior moves when the prior is varied within the range of defensible
   choices.
4. **Independence is argued, not assumed.** See Sections 4.3 and 7.
5. **The partition is complete.** The denominator of Bayes' rule sums the
   likelihood over every hypothesis. If the true model is not in the list, the
   posterior is a statement about the best of a wrong set, and it will usually
   appear pleasingly sharp because nothing in the calculation knows that the
   truth was omitted.

A useful discipline: state the prior, the likelihood and the independence
assumption explicitly, in that order, before quoting a posterior probability.
Most disagreements about "what the probability really is" are disagreements
about one of those three, and stating them converts an argument into a
calculation.

## 9. Python demonstration

The script is `code/probability_axioms.py`; run it with

```
python3 probability_axioms.py
```

It uses only the standard library and a fixed seed (20240117 and 20240118 for
the two simulations), so every printed number is reproducible. The six sections
are: axiom arithmetic for two detectors, the two-hypothesis update, sequential
updating, the base-rate table, the Monte Carlo check of the base-rate formula, and
the Monte Carlo check of the two-hypothesis update. Verbatim excerpts from the
four substantive sections appear in Sections 2.3, 4.3, 5 and 6.3 above.

**What to look at, and why.**

| Output | What it establishes |
|---|---|
| inclusion–exclusion equals the complement route | the axioms are consistent on this example |
| posterior $0.700000$ and simulated $0.701248$ | the update arithmetic is right, and the simulation agrees to $0.0012$ |
| PPV $0.087558$ at $\text{Sp}=0.90$ | a good test on a rare target mostly reports false positives |
| PPV $0.489691$ at $\text{Sp}=0.99$ | specificity, not sensitivity, governs rare-target detection |
| simulated PPV within $0.55$ standard errors | the simulation agrees with the formula by the right criterion |

**Breaking exercise.** Change `prevalence` in the base-rate section to `0.10`
and to `0.001` and predict the two PPV values before running. Then decide, by
inspection, the prevalence below which a specificity of $0.90$ makes positive
results "not evidence of anything" in your own field.

## 10. Common mistakes

1. **Transposing the conditional.** Confusing $P(\text{ore} \mid \text{anomaly})$
   with $P(\text{anomaly} \mid \text{ore})$. The first is what you want; the
   second is what a forward model gives you; the conversion is Bayes' rule and it
   requires the base rate.
2. **Ignoring the base rate.** Reporting "the test was positive with 95 %
   sensitivity" as though the probability of a target were 95 %.
3. **Multiplying likelihood ratios of dependent measurements.** Twice the
   apparent evidence from one measurement looked at twice, or from two adjacent
   stations.
4. **Treating independence as default.** Independence must be justified by the
   design of the experiment, not by the absence of an obvious coupling.
5. **Using a prior because it is convenient.** A conjugate prior is a
   computational convenience and a physical claim; those two roles must be
   separated.
6. **Reporting a posterior to more digits than the prior justifies.** With a
   prior of 0.40 stated to two decimal places, a posterior of 0.700000 implies a
   knowledge of the inputs that does not exist.
7. **Forgetting that $P(B) > 0$ is required.** Conditioning on an event of
   probability zero is undefined, and in a continuous setting this is not a
   technicality: it is the reason likelihoods are densities and not
   probabilities.

## 11. Real-world applications

- **Magnetics and gravity for rare targets.** Detection probabilities and
  specificity determine the number of follow-up ground surveys; the arithmetic of
  Section 6 is the business case for a survey design.
- **Earthquake catalogues.** Rate estimation, magnitude-of-completeness
  correction and declustering are all conditional-probability statements, and the
  difference between "$P(M \ge 6 \text{ this year})$" and "$P(\text{this year is
  in the tail})$" is a conditional-probability distinction.
- **Medical-style decision framing in environmental geophysics.** Contaminant
  plumes are rare relative to the area surveyed; the positive predictive value of
  a geophysical screening method governs whether screening or direct sampling is
  the better use of a budget.
- **Data assimilation.** Weather and ocean forecasting update a model state
  sequentially using exactly the Bayes machinery of Section 4.3, with the
  subtlety that the model's own uncertainty is propagated forward between
  updates; the 4D-Var and ensemble Kalman methods are approximations to this
  recursion.
- **Machine learning.** A classifier's output is $P(\text{class} \mid
  \text{features})$, the function it actually learns is related to the
  likelihood, and the base rate enters implicitly through the training set's
  composition. Class-imbalanced geoscience datasets fail in the way Section 6
  predicts. [21 Statistics, Bayesian Methods and Machine Learning](../../21-statistics-bayesian-ml/README.md)
  develops this.

## 12. Further reading

- **Jaynes, E. T. (2003). *Probability Theory: The Logic of Science*. Cambridge
  University Press.** Level: advanced. The most thorough defence of the view that
  probability is the extension of logic to incomplete information; Chapter 1 is a
  readable statement of the position, and Chapter 4 contains the derivation
  and discussion of Bayes' rule. Locate through your library.
- **Ross, S. M. *A First Course in Probability*.** Level: intermediate. A
  conventional, clean introduction to axioms and conditional probability, with
  many exercises. Any recent edition will do.
- **Tarantola, A. (2005). *Inverse Problem Theory and Methods for Model
  Parameter Estimation*. SIAM.** Level: graduate. The canonical geophysics text
  for Bayesian inversion; Chapters 1 and 2 develop the algebra of this lesson in
  the continuous, model-and-data-space setting actually used in practice.
- **Sivia, D. S. and Skilling, J. *Data Analysis: A Bayesian Tutorial*.** Level:
  intermediate to advanced. Short, example-driven, and written for physical
  scientists; the treatment of priors and of the base-rate fallacy is directly
  applicable.
- **Gelman, A., Carlin, J. B., Stern, H. S., Dunson, D. B., Vehtari, A. and
  Rubin, D. B. *Bayesian Data Analysis*.** Level: advanced. The standard
  reference for the applied statistical practice of everything in this module;
  the chapters on prior choice and on model checking are the ones to read first.

> Note on citations: bibliographic details are given so the works can be located.
> This repository does not host or reproduce copyrighted text; confirm current
> editions and availability through your library.

## 13. Related lessons

- [02 Random Variables, PMFs, PDFs and CDFs](./02-random-variables.md) — turns
  the events of this lesson into random variables with distributions.
- [03 Expectation, Variance and Moments](./03-expectation-variance.md) — the
  quantities that summarise a posterior.
- [08 Hypothesis Testing, p-Values and Power](./08-hypothesis-testing.md) —
  the frequentist counterpart of the decision problem in Section 6, and the
  place where multiple comparisons manufacture false discoveries.
- [01-07 Linear Algebra](../07-linear-algebra/README.md) — model space, data
  space, and the linear systems that carry likelihoods in practice.
- [18 Inverse Problems](../../18-inverse-problems/README.md) — the continuous
  form of the update in Section 5, with regularisation and resolution.
- [21 Statistics, Bayesian Methods and Machine Learning](../../21-statistics-bayesian-ml/README.md)
  — priors, hierarchical models, sampling, and the p-hacking discussion.

## Exercises

Attempt the exercises closed-book before reading the solutions:
[`exercises/01-probability-axioms-exercises.md`](./exercises/01-probability-axioms-exercises.md),
with worked answers in
[`exercises/01-probability-axioms-solutions.md`](./exercises/01-probability-axioms-solutions.md).

## Self-assessment checklist

- [ ] I can state the three axioms and derive the complement and
      inclusion–exclusion rules from them.
- [ ] I can compute $P(A \mid B)$ from a table of joint probabilities and can
      explain why it differs from $P(B \mid A)$.
- [ ] I can derive Bayes' rule from the multiplication rule in two lines, from
      memory.
- [ ] I can update a discrete model twice in sequence and show that the order of
      the two updates does not change the result.
- [ ] I can compute a positive predictive value from a prevalence, a sensitivity
      and a specificity, and I can explain why specificity dominates the answer
      when the prevalence is small.
- [ ] I can list the five assumptions of Section 8 and say what goes wrong when
      each fails.
- [ ] I have run `code/probability_axioms.py`, and I can explain why the
      simulated PPV differs from the analytic one by less than a standard error.
