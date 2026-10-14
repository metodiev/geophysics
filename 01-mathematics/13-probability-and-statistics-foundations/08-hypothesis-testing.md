---
id: 01-13-08
title: "Hypothesis Testing, p-Values and Power"
level: advanced
prereqs: ["01-13-07"]
estimated_minutes: 90
tags: [hypothesis-testing, p-value, statistical-power, multiple-comparisons, false-discovery]
---

# Hypothesis Testing, p-Values and Power

## Learning objectives

By the end of this lesson you will be able to:

1. **Frame** a scientific question as a pair of hypotheses, state the Type I and
   Type II error probabilities, and describe the trade-off between them.
2. **State** the Neyman–Pearson lemma and use it to justify a likelihood-ratio
   test as the most powerful test of a given size for simple hypotheses.
3. **Derive** the distribution of the p-value under the null hypothesis and
   demonstrate that it is uniform.
4. **Derive** the power of a two-sided $z$ test as a function of effect size,
   sample size and noise, and verify the formula by simulation.
5. **Compute** the sample size required to detect a stated effect with a stated
   power, and explain why the calculation belongs in survey design.
6. **State** what a p-value does and does not measure, and give the correct
   frequentist replacement for the questions it is usually misused to answer.
7. **Quantify** the inflation of false discoveries caused by running many tests and
   by testing repeatedly as data accumulate, and apply a correction.

## Prerequisites

[01-13-07 Confidence Intervals and Their Correct Interpretation](./07-confidence-intervals.md)
for the coverage and interval framework that makes decisions quantitative, and
[01-13-05 Sampling Distributions, Law of Large Numbers and CLT](./05-sampling-and-clt.md)
for the normal approximation used in every calculation below.

## 1. The decision problem

A hypothesis test is a decision rule. The ingredients are:

- a **null hypothesis** $H_0$, conventionally the claim that nothing is happening —
  no anomaly, no velocity contrast, no change between epochs, no correlation;
- an **alternative** $H_1$, the claim that something is;
- a **test statistic** $T$ whose distribution is known under $H_0$;
- a **rejection region**, the set of values of $T$ that lead to rejecting $H_0$.

Two errors are possible, and they are not symmetric in cost:

| | $H_0$ true | $H_0$ false |
|---|---|---|
| Reject $H_0$ | **Type I error**, probability $\alpha$ | correct, probability $1-\beta$ = **power** |
| Fail to reject $H_0$ | correct, probability $1-\alpha$ | **Type II error**, probability $\beta$ |

The **size** of the test is $\alpha$, and $1 - \beta$ is its **power**. For a fixed
test statistic, $\alpha$ and $\beta$ move in opposite directions: lowering the
threshold for declaring a detection raises false alarms and reduces misses, and
raising it does the reverse. There is no threshold that makes both small; the only
way to improve both at once is to acquire more data, which is what Section 5
quantifies.

**The asymmetry is a modelling choice, not a mathematical one.** In a
contaminant-detection survey, a missed plume is worse than a false alarm, so the
test should be designed with high power at the cost of size. In a follow-up drilling
programme, a false target wastes far more money than a missed small prospect, so the
threshold should be conservative. Stating the loss function first, and deriving the
threshold from it, is the whole of decision theory; a fixed $5\%$ convention is a
convenient default and a poor substitute for the argument.

Two points about the logic of "failing to reject" deserve emphasis at the outset:

- **Failure to reject is not evidence of absence.** A test with low power fails to
  reject under almost any alternative. The correct statement is "the data are
  compatible with $H_0$", and the useful supplement is the confidence interval,
  which displays *how* compatible and in what range.
- **The null hypothesis is rarely exactly true.** A velocity contrast of exactly
  zero, a correlation of exactly zero, a difference of exactly zero: these are
  idealisations. With enough data every null hypothesis is false, which is why
  statistical significance and scientific importance are different questions.

## 2. Likelihood-ratio tests

For simple hypotheses — a single parameter value under each — the **Neyman–Pearson
lemma** states that the test that rejects $H_0$ for small values of the likelihood
ratio $\Lambda = L(H_0)/L(H_1)$ is most powerful among all tests of the same size.
In other words: to detect a specific alternative with a fixed false-alarm rate,
threshold the likelihood ratio and nothing else.

For an example that will be used throughout this lesson, let $X_1, \dots, X_n$ be
independent $\mathcal{N}(\mu, \sigma^2)$ with $\sigma$ known, and test
$H_0: \mu = \mu_0$ against $H_1: \mu \ne \mu_0$. The log-likelihood ratio is
proportional to $-(\bar X - \mu_0)^2$, so the test rejects for large
$|\bar X - \mu_0|$, equivalently for large

$$|z| = \left|\frac{\bar X - \mu_0}{\sigma/\sqrt n}\right|.$$

Under $H_0$, $z \sim \mathcal{N}(0,1)$. With a two-sided test at size $\alpha$, the
rejection region is $|z| > z_{1-\alpha/2}$, and $\alpha = 0.05$ corresponds to
$1.959964$.

The likelihood-ratio construction generalises to composite hypotheses, where it
produces the $t$ test, the $F$ test and the chi-squared tests of nested models. The
common structure is that a test statistic measures the improvement in fit obtained
by allowing the extra parameters, scaled by the noise level.

## 3. What a p-value is

The **p-value** is the probability, computed under $H_0$, of obtaining a test
statistic at least as extreme as the one observed:

$$p = P_{H_0}\left(|T| \ge |t_{\text{obs}}|\right).$$

It is a measure of the *surprise* of the data under the null hypothesis, on the
scale of the test statistic. It is not a measure of the probability that $H_0$ is
true, and it is not a measure of the size of the effect.

### 3.1 The p-value is uniform under the null

For a continuous test statistic the p-value is itself a random variable, and under
$H_0$ it is uniform on $(0,1)$. The argument is the probability integral transform
of lesson 02. Write $F$ for the CDF of $|T|$ under $H_0$, so that $p = 1 -
F(|t_{\text{obs}}|)$. Then for $u \in (0,1)$,

$$P(p \le u) = P\left(F(|T|) \ge 1 - u\right) = P\left(|T| \ge F^{-1}(1-u)\right)
= u,$$

where the last step uses the definition of $F$ and the continuity that eliminates
atoms. Since the CDF of the uniform is exactly the identity, $p \sim
\text{Uniform}(0,1)$.

The demonstration verifies this with $100\,000$ simulated experiments, each
$z$-testing $n = 25$ Gaussian observations against a true null, seed 20240124:

```
  H0 true, n = 25, reps = 100,000
    fraction of p-values below 0.01 = 0.010640
    fraction of p-values below 0.05 = 0.049840
    fraction of p-values below 0.10 = 0.099520
    fraction of p-values below 0.50 = 0.499190
    max |F_emp - Uniform|            = 0.001912   (noise scale 0.003162)
    mean of the p-values             = 0.500356   (uniform 0.5)
```

Every fraction matches its nominal level to within Monte Carlo error, the maximum
deviation from uniformity is below the noise scale $n^{-1/2} = 0.0032$, and the mean
is $0.500$. This uniformity is the source of everything in Sections 7 and 8: it
means that a threshold of $0.05$ rejects a true null exactly $5\%$ of the time
*per test*, and that any procedure that looks at many p-values is collecting
uniform random numbers and selecting the smallest.

### 3.2 The misinterpretation, stated once and precisely

The p-value answers: *if the null hypothesis were true, how often would data look
at least this extreme?* It does not answer:

- *What is the probability that the null hypothesis is true?* That is a posterior
  probability and requires a prior, which is the base-rate calculation of lesson 01.
  A p-value of $0.03$ is entirely compatible with a $50\%$ chance that $H_0$ is
  true when the prior odds favour $H_0$ heavily.
- *How large is the effect?* A tiny effect measured with great precision can have a
  minuscule p-value, and a large effect measured with poor precision can have a
  large one.
- *How likely is this result to replicate?* The p-value is computed under $H_0$ and
  contains no information about the distribution of p-values under $H_1$; that
  distribution is the power, and it depends on the effect size.

The practical response is to report the *estimate and its interval* alongside the
test result. The interval answers the question the reader actually has — how large
is the effect, and what range of values is compatible with the data — and the
p-value adds nothing to it that the interval does not contain.

## 4. Power

The **power** of a test is the probability of rejecting $H_0$ when a particular
alternative holds: $1 - \beta$. For the two-sided $z$ test of Section 2 with true
mean $\mu = \mu_0 + \delta$ and known $\sigma$,

$$z = \frac{\bar X - \mu_0}{\sigma/\sqrt n}
= \underbrace{\frac{\bar X - \mu}{\sigma/\sqrt n}}_{\sim \mathcal{N}(0,1)}
+ \frac{\delta\sqrt n}{\sigma},$$

so $z \sim \mathcal{N}(\delta\sqrt n/\sigma, 1)$ under the alternative, and the
rejection probability is

$$1 - \beta = P\left(|z| > z_{1-\alpha/2}\right)
= \Phi\left(\frac{\delta\sqrt n}{\sigma} - z_{1-\alpha/2}\right)
+ \Phi\left(-\frac{\delta\sqrt n}{\sigma} - z_{1-\alpha/2}\right).$$

The second term is negligible whenever the first is not, because it is the
probability of rejecting in the *opposite* direction; but retaining it makes the
formula exact and makes the symmetry of the test visible.

Three consequences follow immediately, and all three are quantitative versions of
things usually stated vaguely:

- **Power depends on the combination $\delta\sqrt n/\sigma$.** Doubling the sample
  size is equivalent to doubling the effect size, and equivalent to halving the
  noise. A "signal-to-noise ratio" for a detection is exactly this quantity.
- **Large effects are easy; small ones are expensive.** Because the argument grows
  as $\sqrt n$, the sample size needed grows as $1/\delta^2$.
- **A test with size $\alpha$ has power $\alpha$ when $\delta = 0$.** This is the
  definition of size, and it is a useful check on any power calculation.

The demonstration compares the formula with simulation for $n = 25$,
$\sigma = 1$, $\alpha = 0.05$, with $20\,000$ replicates per point:

```
   effect delta   power (theory)   power (simulated)
           0.00         0.050000            0.050700
           0.20         0.170075            0.168500
           0.40         0.516005            0.518650
           0.60         0.850839            0.850600
           0.80         0.979327            0.979250
           1.00         0.998817            0.998550
```

Every simulated value is within about two Monte Carlo standard errors of the
formula, whose standard error at these proportions and replicate counts is between
$0.0009$ and $0.0015$. The important entries are the middle ones: to detect an
effect of $0.4\sigma$ with $25$ observations the test is barely better than a coin
toss, and only above $0.6\sigma$ — an effect larger than half the noise level —
does it become reliable.

## 5. Sample size from a power requirement

Setting $1 - \beta$ to a target and neglecting the second term,

$$\Phi\left(\frac{\delta\sqrt n}{\sigma} - z_{1-\alpha/2}\right) = 1 - \beta
\ \Longrightarrow\ \frac{\delta\sqrt n}{\sigma} = z_{1-\alpha/2} + z_{1-\beta},$$

hence

$$n = \left(\frac{(z_{1-\alpha/2} + z_{1-\beta})\,\sigma}{\delta}\right)^{2}.$$

Note that $n$ is inversely proportional to $\delta^2$: detecting an effect half as
large requires four times the data. This single scaling relation governs the cost of
most geophysical surveys.

The demonstration applies it to a concrete design question — how many picks are
needed to detect a travel-time delay of $0.05$ s when the pick scatter is $0.10$ s,
at $\alpha = 0.05$ and $90\%$ power:

```
  pick scatter sigma = 0.1 s, delay to detect = 0.05 s
  z(0.975) = 1.959964, z(0.90) = 1.281552
  required n = ((z_a + z_b) sigma / delta)^2 = 42.029692
  so 43 picks are needed for 90 % power at alpha = 0.05
    n =  40: power theory 0.885379, simulated 0.884700
    n =  42: power theory 0.899799, simulated 0.902800
    n =  43: power theory 0.906375, simulated 0.907050
    n =  60: power theory 0.972127, simulated 0.973250
```

The continuous formula gives $42.03$, so $n = 42$ is a hair short of $90\%$ and
$n = 43$ clears it. The simulation cannot resolve that hair — at $20\,000$
replicates the standard error on an estimated power near $0.9$ is about $0.002$ —
and it lands either side. Reporting the simulated value as confirmation of the
45th percentage point would be over-reading the simulation; reporting it as
confirmation of the formula to within Monte Carlo noise is exactly right.

**Why this calculation belongs in the design phase.** It converts an accuracy
target into a count of measurements, and it does so before any data exist. A survey
that is designed with a power calculation can state in advance what it will be able
to detect; a survey designed without one will report "no significant anomaly" at
whatever effect size it happened to be unable to see, and there will be no way to
distinguish a real absence from an uninformative experiment.

## 6. Multiplicity: how false discoveries are manufactured

### 6.1 The family-wise error rate

If $m$ hypotheses are tested independently, each at size $\alpha$, and all null
hypotheses are true, the probability of at least one rejection is

$$P(\text{at least one rejection}) = 1 - (1 - \alpha)^{m},$$

because the probability of no rejection in any of them is $(1-\alpha)^{m}$. This is
the **family-wise error rate (FWER)**, and it grows alarmingly fast: $0.05$ for one
test, $0.40$ for ten, $0.92$ for fifty, and effectively certain for a thousand.

The derivation of the correction is the union bound. For events $A_i$, $P(\bigcup_i
A_i) \le \sum_i P(A_i)$; setting each $P(A_i) = \alpha/m$ makes the sum $\alpha$.
The resulting **Bonferroni** procedure — reject a hypothesis only if its p-value is
below $\alpha/m$ — controls the FWER at $\alpha$ whatever the dependence between the
tests, at the cost of reduced power per test.

Both are measured in the demonstration, with $200\,000$ simulated studies. The
smallest p-value in a study is drawn from its exact null distribution, since the
minimum of $m$ independent uniforms is Beta$(1, m)$ and can be sampled as
$1 - U^{1/m}$:

```
       m    1-(1-a)^m   observed FWER   Bonferroni a/m   observed FWER
       1     0.050000        0.050670         0.050000        0.050670
      10     0.401263        0.402225         0.005000        0.049035
      50     0.923055        0.925230         0.001000        0.048700
     100     0.994079        0.994175         0.000500        0.049580
    1000     1.000000        1.000000         0.000050        0.048075
```

The uncorrected column matches the formula at every $m$; the Bonferroni column
holds near $0.049$ throughout, at the price of a threshold of $0.00005$ for a
thousand tests. That price is real: discovering a genuine effect at that threshold
requires a very powerful individual test. Where many tests are run with modest
power — a genome-wide scan, a band-by-band spectral search, a cell-by-cell
anomaly detector — Bonferroni is conservative and the **false discovery rate**
(Benjamini–Hochberg) controls the expected *proportion* of false discoveries among
the rejections instead, which is usually the more relevant quantity.

### 6.2 The problem of hidden multiplicity

The arithmetic above applies when the number of tests is known and stated. The
serious version of the problem is the multiplicity that is *not* counted. Searching
over:

- several processing flows before choosing one to report;
- a range of filter cut-offs, window lengths or inversion regularisation
  parameters;
- a set of candidate source mechanisms or velocity models;
- a map of many cells, of which the significant ones are shown;
- a choice of study area, time window or magnitude threshold;

each increases the effective number of tests. The demonstration's most striking
number concerns the last kind, in the form of optional stopping: testing the growing
sample after each new observation, and stopping as soon as the p-value drops below
$0.05$. Under a true null hypothesis, with $4000$ simulated studies per row:

```
    stop at n_max   observed rate    nominal
               30        0.164250       0.05
              100        0.266500       0.05
             1000        0.459500       0.05
```

At $n_{\max} = 30$ the "false discovery rate" is $16\%$ instead of $5\%$; with a
thousand observations available it is $46\%$. Almost half of such studies would
declare a discovery that does not exist, while every individual test was
nominally at the $5\%$ level. The nominal level applies to *one* test decided in
advance; each additional look spends significance, and the p-value at the moment of
stopping is not the p-value of the experiment.

### 6.3 What to do

1. **State the number of tests in advance** and apply a correction, or use a
   procedure (group-sequential, Bonferroni-Holm, Benjamini–Hochberg) designed for
   the multiplicity that exists.
2. **Pre-register the analysis** where the field permits: the hypothesis, the
   statistic, the sample size and the stopping rule, before the data are examined.
3. **Report the effect size and its interval**, not only the p-value. A discovery
   with an interval that spans practically irrelevant values is not a useful
   discovery, however small its p-value.
4. **Randomise and split.** Hold out a portion of the data from the search and use
   it to confirm the finding at the nominal level. A finding that survives an
   independent test was not manufactured by multiplicity.
5. **Be suspicious of the smallest p-value.** In an exploratory scan it is the
   extreme of a uniform sample, and its distribution is known: the smallest of $m$
   tests has expected value about $1/(m+1)$. The threshold for declaring it
   interesting should be set accordingly.

The question is discussed from the machine-learning side, including the
distinction between exploratory and confirmatory analysis and the practice of
cross-validation, in
[21 Statistics, Bayesian Methods and Machine Learning](../../21-statistics-bayesian-ml/README.md).

## 7. Choosing and reporting a test

**Choose the test from the structure of the data**, not from habit:

- Comparing a mean with a hypothesised value: the $z$ test for known $\sigma$, the
  $t$ test otherwise.
- Comparing two means: the two-sample $t$ test; a paired test when the same
  stations are measured twice, which is far more powerful because it removes the
  between-station variance.
- Comparing distributions of counts: the chi-squared test of independence, or
  Fisher's exact test for small counts.
- Comparing a whole distribution with a model: Kolmogorov–Smirnov or
  Cramér–von Mises, both built on the probability integral transform of lesson 02.
- Comparing two distributions: the two-sample Kolmogorov–Smirnov test, or a
  permutation test when the sample is small.
- Testing a correlation or a trend: rank-based tests (Spearman, Kendall, Mann–Kendall)
  are robust to heavy tails where the Pearson test is not.

**Report** the test statistic, the degrees of freedom, the p-value, the estimated
effect with its interval, the sample size, and the number of tests performed. Those
six items make the result auditable; omitting the last two is what makes a
literature uninterpretable in aggregate.

**Non-parametric and permutation tests** deserve a mention because they sidestep
the distributional assumptions that this lesson has repeatedly found to be binding.
A permutation test computes the test statistic under every rearrangement of the
group labels, giving an exact p-value under the sharp null hypothesis of
exchangeability, with no distributional assumption at all. For a heavy-tailed
parent it is often the only defensible route, and it is computationally trivial for
moderate samples.

## 8. Beyond the dichotomy: what to report instead

The $5\%$ threshold is a convention, and it discards most of the information in the
data. The alternatives are not exotic; most of them are already in this module.

- **The estimate and its confidence interval.** The interval is the honest summary
  of what the data support, and it answers the reader's question about magnitude.
- **The p-value as a continuous measure** of the compatibility of the data with
  $H_0$, reported without reference to a threshold, and interpreted with the
  knowledge that it is uniform under the null. Many fields now prefer this.
- **A Bayes factor**, the ratio of the marginal likelihoods of the two hypotheses,
  which measures evidence for one against the other and does not suffer from the
  "reject with enough data" pathology, at the price of requiring priors.
- **A power calculation reported alongside the result.** "The survey had $90\%$
  power to detect a $0.05$ s delay" is a far more useful sentence than "the result
  was not significant".
- **Effect sizes in physical units.** A velocity contrast of $0.03$ km/s with an
  interval of $[-0.01, 0.07]$ km/s is a scientific statement; its p-value of $0.14$
  is a footnote.

## 9. Assumptions and regime of validity

1. **The null distribution must be right.** Every p-value is computed under $H_0$,
   and it is only as good as the distributional assumption. Using a normal
   approximation for heavy-tailed data, or an independence assumption for
   correlated data, produces p-values that are not uniform under the null.
2. **The test must have been decided in advance.** A p-value computed after
   choosing the test, the data subset, the transformation and the stopping point
   is not a p-value at the stated level.
3. **Multiplicity must be counted.** All of it, including the choices that are
   embarrassing to report.
4. **Power must be adequate for the claim being made.** A non-significant result
   from an underpowered study carries almost no information, and reporting it as
   evidence of absence is a logical error.
5. **Statistical significance is not physical significance.** Both must be
   reported, and the second must be argued in the units of the problem.
6. **The model must match the design.** Paired designs need paired tests,
   clustered data need cluster-robust methods, and repeated measures need methods
   that account for within-unit correlation.

## 10. Python demonstration

Run

```
python3 hypothesis_testing.py
```

from `code/`. Standard library only; seed 20240124, with offsets for the internal
blocks. Four sections: the null distribution of the p-value, the power curve against
its formula, the FWER with and without Bonferroni correction plus the optional
stopping experiment, and the sample-size calculation for a travel-time delay.
Outputs are quoted verbatim in Sections 3.1, 4, 5 and 6.

**A note on the approach taken to multiplicity in the script.** The FWER section
does not simulate $m$ full experiments per study, because that would be
$10^{8}$ Gaussian draws for the largest $m$ and would take minutes. Instead it uses
the exact null distribution of the smallest of $m$ p-values — Beta$(1,m)$, sampled
as $1 - U^{1/m}$ — which Section 3.1 has already established is correct. This is a
case where a result proved earlier in the same lesson replaces a slow simulation,
and it is worth noticing that the demonstration gets both speed and accuracy from
doing the theory first.

**Breaking exercise.** Change the optional-stopping experiment so that the
p-value is evaluated only every tenth observation instead of at every $k$. Predict
whether the false discovery rate will be lower and by roughly how much, given that
the number of opportunities to stop has fallen by a factor of ten but each look is
still at a sample of growing size. Then run it. The answer illustrates that the
inflation depends on the number of looks and on how much the test statistic moves
between them.

## 11. Common mistakes

1. **Reading a p-value as the probability that $H_0$ is true.** It is
   $P(\text{data this extreme} \mid H_0)$, a different conditional (lesson 01).
2. **Treating $p < 0.05$ as proof and $p > 0.05$ as disproof.** The threshold is a
   convention; the gradient of evidence is continuous.
3. **Ignoring power.** A non-significant result from an underpowered study is
   uninformative, not negative.
4. **Running many tests and reporting the winner.** Section 6.
5. **Testing repeatedly and stopping on significance.** The measured inflation is
   $0.16$ to $0.46$ in Section 6.2.
6. **Conflating significance with importance.** With large $n$, every null
   hypothesis is false; with small $n$, no effect is significant.
7. **Using an unpaired test for paired data**, or vice versa. The paired test
   removes between-unit variance and is often several times more powerful.
8. **Reporting a p-value without the test, the degrees of freedom or the number of
   tests.** The result becomes unauditable.
9. **Assuming a non-parametric test is free.** It is free of distributional
   assumptions, not of assumptions about independence and exchangeability, and it
   has lower power when a parametric model was in fact correct.
10. **Choosing the hypothesis after seeing the data and calling the result
    confirmatory.** This is the multiplicity of Section 6.2 in its least visible
    form.

## 12. Real-world applications

- **Anomaly detection.** A threshold on a gridded field is a test at every cell;
  the number of cells is the multiplicity, and the false-alarm rate must be computed
  on it, not per cell.
- **Change detection between epochs.** Repeat gravity or InSAR surveys produce
  differences whose significance depends on the combined noise of two surveys, and
  the correlation between them (lesson 09).
- **Magnitude-of-completeness estimation.** Testing whether a catalogue is complete
  below a candidate magnitude involves a family of tests; the reported completeness
  magnitude inherits the multiplicity.
- **Model selection in inversion.** Comparing regularisation parameters or
  parameterisations across many trials; a single "$p < 0.05$ improvement" is not
  evidence unless the search is accounted for.
- **Clinical-style trials in environmental health.** Community-level interventions
  are tested with pre-registered designs and power calculations, and the
  geophysics of exposure mapping enters through the measurement error, which
  attenuates the estimated effect.
- **Machine-learning benchmark comparisons.** Comparing classifiers on a test set
  uses paired tests on the same items; the multiplicity comes from the number of
  models tried, which is why benchmark results without a held-out confirmation
  should be treated as exploratory. See
  [21 Statistics, Bayesian Methods and Machine Learning](../../21-statistics-bayesian-ml/README.md).

## 13. Further reading

- **Casella, G. and Berger, R. L. *Statistical Inference*.** Level: advanced.
  Hypothesis testing, the Neyman–Pearson lemma, uniformly most powerful tests and
  the power function, in the standard treatment.
- **Lehmann, E. L. and Romano, J. P. *Testing Statistical Hypotheses*.** Level:
  doctoral. The comprehensive reference, including the theory of multiple testing
  and step-down procedures.
- **Wasserstein, R. L. and Lazar, N. A. (2016). The ASA's statement on p-values:
  context, process, and purpose. *The American Statistician*, 70(2).** Level:
  intermediate. Six principles about p-values and scientific inference, written for
  practitioners; confirm the current version and access through your library.
- **Benjamini, Y. and Hochberg, Y. (1995). Controlling the false discovery rate: a
  practical and powerful approach to multiple testing. *Journal of the Royal
  Statistical Society B*, 57(1), 289–300.** Level: advanced. The original FDR
  procedure referred to in Section 6.1.
- **Good, P. *Permutation, Parametric and Bootstrap Tests of Hypotheses*.** Level:
  intermediate to advanced. The resampling route to tests that do not rely on
  distributional assumptions, which is the practical answer for heavy-tailed data.
- **Ioannidis, J. P. A. (2005). Why most published research findings are false.
  *PLoS Medicine*, 2(8), e124.** Level: intermediate. The argument of Section 6
  taken to its conclusion, with the base-rate arithmetic of lesson 01 at its centre.

> Note on citations: bibliographic details are given so the works can be located.
> This repository does not host or reproduce copyrighted text; confirm editions
> and availability through your library.

## 14. Related lessons

- [01 Probability Axioms, Conditional Probability and Bayes' Rule](./01-probability-axioms.md)
  — the base-rate arithmetic behind the misinterpretation of a p-value.
- [05 Sampling Distributions, Law of Large Numbers and CLT](./05-sampling-and-clt.md)
  — the distributions the test statistics follow.
- [06 Point Estimation, Bias, Consistency and Efficiency](./06-estimation-theory.md)
  — the estimation counterpart of every test here.
- [07 Confidence Intervals and Their Correct Interpretation](./07-confidence-intervals.md)
  — the interval that should accompany every p-value.
- [09 Error and Uncertainty Propagation](./09-error-propagation.md) — the
  measurement-error attenuation referred to in Section 12.
- [21 Statistics, Bayesian Methods and Machine Learning](../../21-statistics-bayesian-ml/README.md)
  — p-hacking, exploratory versus confirmatory analysis, cross-validation and the
  Bayesian alternatives.
- [18 Inverse Problems](../../18-inverse-problems/README.md) — model selection and
  the reality of testing many parameterisations.

## Exercises

[`exercises/08-hypothesis-testing-exercises.md`](./exercises/08-hypothesis-testing-exercises.md),
with solutions in
[`exercises/08-hypothesis-testing-solutions.md`](./exercises/08-hypothesis-testing-solutions.md).

## Self-assessment checklist

- [ ] I can set up a test by naming $H_0$, $H_1$, the statistic, the rejection
      region and the loss, and state the Type I and Type II error probabilities.
- [ ] I can state the Neyman–Pearson lemma and derive the likelihood-ratio test for
      a simple normal location problem.
- [ ] I can prove that a p-value is uniform under the null and verify it by
      simulation.
- [ ] I can derive the power of a two-sided $z$ test and use it to compute the
      sample size for a stated power.
- [ ] I can explain the three things a p-value does not measure, and give the
      quantity that answers each.
- [ ] I can compute the FWER for $m$ independent tests and apply a Bonferroni
      correction.
- [ ] I can quantify the inflation of false discoveries caused by optional
      stopping, and I can name the design choice that prevents it.
- [ ] I have run `code/hypothesis_testing.py` and can explain why the observed
      "discovery rate" reaches $0.46$ with a thousand looks at a true null.
