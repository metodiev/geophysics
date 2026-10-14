---
id: 21-01-05
title: "Nonparametric Statistics and Kernel Density Estimation"
level: graduate
prereqs: ["01-13-05", "01-13-08"]
estimated_minutes: 60
tags: [statistics, nonparametric, rank-tests, kernel-density, bandwidth-selection]
---

# Nonparametric Statistics and Kernel Density Estimation

## Learning objectives

By the end of this lesson you will be able to:

1. **Construct** the empirical cumulative distribution function and **state**
   the Glivenko-Cantelli and Dvoretzky-Kiefer-Wolfowitz guarantees.
2. **Compute** the sign test, the Wilcoxon signed-rank statistic and the
   Mann-Whitney $U$ statistic, and **apply** their normal approximations.
3. **Explain** how rank tests buy distributional robustness and what they give
   up in power.
4. **Estimate** a density by kernel smoothing and **derive** the bias-variance
   trade-off in the bandwidth.
5. **Apply** the Silverman and Scott bandwidth rules and **evaluate** the kernel
   estimate against a known truth by integrated squared error.
6. **Diagnose** when a rank test or a single-bandwidth density estimate answers
   the wrong question.

All data in this lesson are **SYNTHETIC**: two Gaussian groups, a set of paired
differences, and a two-component mixture for the density estimate. No measured
value enters, and the estimates below constrain only the demonstration's model.

## Prerequisites

- [01-13-05 Sampling Distributions, Law of Large Numbers and CLT](../../01-mathematics/13-probability-and-statistics-foundations/05-sampling-and-clt.md) —
  why the rank statistics are asymptotically normal.
- [01-13-08 Hypothesis Testing, p-Values and Power](../../01-mathematics/13-probability-and-statistics-foundations/08-hypothesis-testing.md) —
  the testing framework the rank tests sit in.
- [21-01-03 Resampling: Bootstrap, Jackknife, Permutation Tests](03-resampling.md) —
  the computational alternative to a rank test.

## 1. Intuition: keep the order, discard the scale

A parametric test converts data into standard errors through an assumed
distribution. A rank test keeps only the **order** of the observations and
throws the magnitudes away, and in doing so it stops caring about the shape of
the distribution. The price is power: when the parametric assumptions hold, the
rank test is less efficient; when they fail — heavy tails, outliers, strong
skew — it is often far better.

The same idea drives kernel density estimation. Instead of assuming a family,
place a small smooth bump at each observation and add them up. The bump width,
the bandwidth, is then the only assumption, and it is a visible one: too narrow
and the estimate is a spike for every sample point, too wide and every structure
is smoothed away.

## 2. The empirical distribution function

For a sample $x_1,\dots,x_n$ the ECDF is

$$\hat F_n(x) = \frac1n\sum_{i=1}^{n}\mathbf 1\{x_i \le x\},$$

a step function with a jump of $1/n$ at each observation. It is an unbiased
estimate of $F(x)$ at every $x$, with
$\operatorname{Var}\hat F_n(x) = F(x)(1-F(x))/n$. Two uniform results justify
using it as a stand-in for $F$:

- **Glivenko-Cantelli**: $\sup_x |\hat F_n(x) - F(x)| \to 0$ almost surely.
- **Dvoretzky-Kiefer-Wolfowitz**: for $\varepsilon > 0$,
  $P\big(\sup_x|\hat F_n - F| > \varepsilon\big) \le 2e^{-2n\varepsilon^{2}}$,
  so the sup-distance shrinks like $n^{-1/2}$ with no assumption on $F$.

That last line is the honest statement of the nonparametric promise: the *body*
of any distribution can be estimated to $n^{-1/2}$ accuracy without a model.
Nothing here says anything about the extreme tail, where the ECDF is a single
step and no uniform bound helps.

## 3. Rank tests

**Sign test.** Under the null that a paired difference has median zero, the
number of positive differences is $\mathrm{Binomial}(n, 1/2)$. The test ignores
magnitudes entirely, so it is robust to any contamination, but weak.

**Wilcoxon signed-rank test.** Rank the absolute differences, sum the ranks of
the positive ones:

$$W^{+} = \sum_{i : d_i > 0} R_i, \qquad
\mathbb E[W^{+}] = \frac{n(n+1)}{4}, \qquad
\operatorname{Var}(W^{+}) = \frac{n(n+1)(2n+1)}{24}.$$

**Mann-Whitney (Wilcoxon rank-sum) test.** For two independent groups of sizes
$n_1, n_2$, the statistic

$$U = \#\{(i,j) : a_i > b_j\}$$
counts the pairs ordered one way. Under the null that the two samples are drawn
from the same distribution,

$$\mathbb E[U] = \frac{n_1 n_2}{2}, \qquad
\operatorname{Var}(U) = \frac{n_1 n_2 (n_1+n_2+1)}{12},$$

so $z = (U - \mathbb E[U])/\sqrt{\operatorname{Var}(U)}$ is approximately
standard normal. The Mann-Whitney null is *stochastic equality*: it is sensitive
to a difference in location but also, in a less interpretable way, to a
difference in shape.

## 4. Kernel density estimation

The kernel density estimate is

$$\hat f(x; h) = \frac{1}{nh}\sum_{i=1}^{n} K\!\left(\frac{x - x_i}{h}\right),$$

with $K$ a normalised kernel (the Gaussian here) and $h$ the **bandwidth**.
Expanding $f$ about $x$ gives the leading bias and variance,

$$\mathbb E\hat f(x) - f(x) \approx \frac{h^{2}}{2}\,f''(x)\!\!\int u^{2}K(u)\,
\mathrm du, \qquad
\operatorname{Var}\hat f(x) \approx \frac{f(x)}{nh}\!\!\int K^{2}(u)\,\mathrm du,$$

and integrating the squared bias and the variance gives the mean integrated
squared error

$$\mathrm{MISE}(h) \approx \frac{h^{4}}{4}\!\left(\int u^{2}K\right)^{2}\!\!\int
(f'')^{2}
+ \frac{1}{nh}\!\int K^{2} .$$

Minimising over $h$ makes the two terms equal and gives $h_{\text{opt}} \propto
n^{-1/5}$ — the slow $n^{-1/5}$ rate is the well-known cost of estimating a
density nonparametrically. Two plug-in rules from the Gaussian reference replace
the unknown $\int (f'')^{2}$:

$$h_{\text{Silverman}} = 1.06\,\min\!\Big(s,\ \frac{\mathrm{IQR}}{1.349}\Big)
n^{-1/5}, \qquad h_{\text{Scott}} = 1.06\,s\,n^{-1/5} \times \frac{1}{1.06} .$$

Both assume a single smooth mode; both under-smooth multi-modal data or
over-smooth it in the wrong direction.

## 5. Worked example

The demonstration draws $40 + 40$ Gaussian values with a true shift of
$0.4\sigma$, then replaces $5$ of the second group with values at $8\sigma$.

**Clean two-sample test.** Means $0.035$ versus $0.196$, medians $0.165$ versus
$0.077$. Welch's $t = -0.723$ ($p = 0.4717$) and Mann-Whitney $U = 743.0$
($p = 0.5867$) agree: no evidence of a difference. Both are under-powered at
this effect size, and the demonstration's point is that they agree when the
model is right.

**Contaminated.** The means become $0.035$ and $1.105$ while the medians stay at
$0.165$ and $0.200$. The $t$ test now reports $t = -2.278$, $p = 0.0270$ —
significant at the $5\ \%$ level, and entirely an artefact of five fabricated
values. Mann-Whitney reports $U = 678.0$, $p = 0.2423$: no evidence. The rank
test's normal approximation checks arithmetically, since
$\mathbb E[U] = 800$, $\mathrm{sd}(U) = \sqrt{40\cdot40\cdot81/12} = 103.9$ and
$z = (678-800)/103.9 = -1.17$.

**Paired tests.** On $30$ differences with mean $+0.089$ and median $-0.017$,
the Wilcoxon signed-rank gives $W = 226.0$, $p = 0.9032$, and the sign test
gives $15$ of $30$ positive, $p = 1.0000$. Neither finds anything, correctly.

**Density.** The sample is $200$ values, half from $\mathcal N(0,1)$ and half
from $\mathcal N(2.5,1)$, with subgroup means $-0.116$ and $+2.483$ and sample
standard deviation $1.663$. The rules give $h = 0.6108$ (Silverman) and
$h = 0.5762$ (Scott). Sweeping the bandwidth exposes the decision:

| $h$ | $\hat f(0)$ | $\hat f(1.25)$ | $\hat f(2.5)$ | modes |
|---|---|---|---|---|
| 0.20 | 0.199 | 0.163 | 0.154 | 5 |
| 0.40 | 0.199 | 0.174 | 0.184 | 3 |
| 0.61 | 0.187 | 0.185 | 0.184 | 2 |
| 1.00 | 0.168 | 0.186 | 0.168 | 1 |

At $h = 0.20$ the estimate has five modes, four of them spurious. At the
automatic bandwidth the two true modes survive but the dip between them is
$0.002$ deep on a peak of $0.19$ — an $1\ \%$ trough, i.e. the bimodality is
essentially unresolved. At $h = 1.0$ the estimate is unimodal and wrong.

**Chosen by a known truth.** Against the exact mixture, the integrated squared
error is $0.00223$ at Silverman's bandwidth, $0.00216$ at Scott's, and $0.00214$
at the oracle $h = 0.550$ found on a grid. Silverman's rule is $4.2\ \%$ worse
than the oracle — a small penalty, but note that the oracle was available only
because the truth was known.

## Assumptions and regime of validity

1. **Exchangeability for rank tests.** Mann-Whitney's null is that the groups
   are identically distributed; a difference in shape alone rejects it and the
   "location shift" interpretation is then wrong.
2. **Independence.** Rank tests assume independent observations; ties and
   serial correlation both distort the null distribution.
3. **Ties.** With heavily discretised data the rank statistics need tie
   corrections; the continuous approximations above do not apply.
4. **Smoothness for the density.** The MISE expansion needs $f$ twice
   differentiable; for a spike train or a strongly discrete variable it fails.
5. **The bandwidth rule assumes unimodality.** Silverman and Scott both scale
   with a single spread measure and therefore under-smooth mixtures.
6. **A density is not a tail.** The kernel estimate near the largest
   observation is dominated by one kernel and says almost nothing beyond it.

## The honest summary

Nonparametric methods trade assumptions for data. The ECDF converges uniformly
at $n^{-1/2}$ without a model, rank tests keep their nominal level under
contamination that destroys a $t$ test, and the kernel estimate encodes its one
assumption — the bandwidth — in a visible, checkable way. In the demonstration
five outliers turned a non-significant $t$ test into $p = 0.027$ while
Mann-Whitney stayed at $p = 0.24$; and a bandwidth of $0.61$ resolved two
components whose trough was only $1\ \%$ of the peak height. What none of this
establishes is a tail probability or a detection threshold: nonparametric
methods are honest about the body and silent about the extremes, which is
exactly where hazard questions live.

## Python demonstration

[`code/nonparametric_demo.py`](./code/nonparametric_demo.py) prints every number
quoted above. It:

1. runs Welch and Mann-Whitney tests on clean and contaminated groups;
2. runs Wilcoxon signed-rank and the sign test on paired differences;
3. prints kernel density estimates across a bandwidth sweep and counts modes;
4. selects a bandwidth by integrated squared error against the true mixture.

```bash
cd 21-statistics-bayesian-ml/01-statistics-in-practice/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python nonparametric_demo.py
```

It runs in well under a second and prints only text.

## Exercises

Graded problems are in
[`exercises/05-nonparametric-methods-exercises.md`](./exercises/05-nonparametric-methods-exercises.md)
with worked solutions in
[`exercises/05-nonparametric-methods-solutions.md`](./exercises/05-nonparametric-methods-solutions.md).
The ★★★ problems ask you to design a power study and a bandwidth-selection
experiment.

## Mastery checkpoint

Without notes, two independent samples of $n_1 = n_2 = 40$ give Mann-Whitney
$U = 678.0$, and a kernel density estimate of a two-component sample uses
$h = 0.6108$ with sample standard deviation $1.663$ and $n = 200$.

1. Compute $\mathbb E[U]$, $\mathrm{sd}(U)$ and the normal $z$, and state the
   approximate two-sided $p$-value.
2. Compute Scott's bandwidth from the same inputs and explain the difference
   from Silverman's.
3. State what the $z$ in part 1 assumes about the two distributions.
4. State the one number that the kernel estimate leaves out and why it matters
   for a hazard question.

## Common pitfalls

1. **Reading Mann-Whitney as a test of medians.** It tests stochastic equality;
   equal medians with different shapes can still reject.
2. **Ignoring ties.** Rank statistics with many tied values need corrections.
3. **Choosing the bandwidth after seeing the answer.** Selecting $h$ to make the
   picture you wanted is p-hacking in a density.
4. **Reporting a density beyond the data.** The estimate near the extremes is
   controlled by one or two kernels.
5. **Assuming nonparametric means assumption-free.** Exchangeability,
   independence and smoothness are assumptions too.
6. **Using the sign test when magnitudes matter.** It discards information and
   is the least powerful of the three rank tests here.

## Where this is used

- **Geochemistry**: comparing two populations of assays with heavy tails.
- **Seismology**: nonparametric magnitude distributions and $b$-value tests
  where the magnitude law is uncertain.
- **Hydrology**: empirical flood-frequency curves and the plotting-position
  conventions that accompany them.
- **Geodesy**: comparing GNSS station velocities between networks without a
  Gaussian error model.
- **Paleoclimate**: density estimates of proxy values where a parametric family
  is not defensible.

## Related lessons

- [21-01-03 Resampling: Bootstrap, Jackknife, Permutation Tests](03-resampling.md) —
  the computational route to the same distribution-free inference.
- [21-01-01 Descriptive Statistics, Robust Measures and Outliers](01-descriptive-statistics.md) —
  the robust summaries that rank statistics replace.
- [21-01-02 Choosing Probability Models for Earth Data](02-probability-models-earth.md) —
  what to assume instead of smoothing.
- [21-02-02 Variograms, Covariance and Model Fitting](../02-geostatistics/02-variograms.md) —
  the empirical-structure estimation problem in space rather than in value.
- [01-13-08 Hypothesis Testing, p-Values and Power](../../01-mathematics/13-probability-and-statistics-foundations/08-hypothesis-testing.md) —
  the power and level framework.

## Self-assessment checklist

- [ ] I can build an ECDF and state its uniform convergence guarantee.
- [ ] I can compute the sign, signed-rank and Mann-Whitney statistics.
- [ ] I can apply the normal approximations and state their assumptions.
- [ ] I can write the KDE and derive the MISE trade-off.
- [ ] I can apply Silverman's and Scott's rules and judge when they fail.
- [ ] I can name what a density estimate does not constrain.
