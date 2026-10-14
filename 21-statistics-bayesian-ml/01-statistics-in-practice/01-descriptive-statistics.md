---
id: 21-01-01
title: "Descriptive Statistics, Robust Measures and Outliers"
level: intermediate
prereqs: ["01-13-03", "01-13-04"]
estimated_minutes: 45
tags: [statistics, robust-statistics, outliers, breakdown-point, descriptive-statistics]
---

# Descriptive Statistics, Robust Measures and Outliers

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** the mean, median and trimmed mean of a sample, and **explain**
   which of them is a location estimate of what.
2. **Compute** the standard deviation, interquartile range and median absolute
   deviation, and **apply** the $0.6745$ factor that makes the MAD a
   Gaussian-consistent scale.
3. **Define** the breakdown point of an estimator and **measure** it for the
   mean and the median on a contaminated sample.
4. **Diagnose** outliers with the classical $z$-score and the modified
   $z$-score, and **explain** masking when a gross outlier hides moderate ones.
5. **Quantify** the efficiency price of robustness and **decide** when that
   price is worth paying.
6. **State** what a single descriptive number does not constrain.

All models and data in this lesson are **SYNTHETIC**: a porosity-like sample is
drawn from a stated normal distribution and contaminated by spikes that are
placed by hand. No measured porosity enters, and no number is quoted from a
published data set.

## Prerequisites

- [01-13-03 Expectation, Variance and Moments](../../01-mathematics/13-probability-and-statistics-foundations/03-expectation-variance.md) —
  the moments being estimated.
- [01-13-04 Common Distributions and Their Earth-Science Roles](../../01-mathematics/13-probability-and-statistics-foundations/04-distributions.md) —
  why lognormal and heavy-tailed laws appear in Earth data.
- [03-02-01 ndarray Creation, dtypes, Shapes and Strides](../../03-scientific-computing/02-numpy/01-ndarray-basics.md) —
  the vector operations used in the demonstration.

## 1. Intuition: a summary is a decision, not a fact

A descriptive statistic answers a question you chose to ask. "What is the
typical porosity of this formation?" has at least four defensible answers — the
mean, the median, a trimmed mean, and the mode — and they agree only when the
sample is symmetric and clean. The moment one measurement is wrong, the answers
separate, and the size of the separation is the whole subject of this lesson.

The intuition is a tug-of-war. The **mean** is a weighted average in which every
observation pulls with equal force, so a single observation at the far edge pulls
hard. The **median** is the middle order statistic: it counts, it does not sum,
so far-away values pull only through their ranks and their magnitudes are
irrelevant. Robust statistics formalises "how far a value can move the estimate"
with two numbers, the **breakdown point** and the **influence function**, and
then makes the trade with efficiency explicit.

## 2. Location estimators and their arithmetic

For a sample $x_1,\dots,x_n$, the sample mean, the sample median and the
$\alpha$-trimmed mean are

$$\bar x = \frac{1}{n}\sum_{i=1}^{n} x_i, \qquad
\tilde x = \text{middle order statistic}, \qquad
\bar x_{\alpha} = \frac{1}{n-2g}\sum_{i=g+1}^{n-g} x_{(i)},$$

where $x_{(i)}$ is the $i$-th order statistic and $g = \lfloor \alpha n \rfloor$.
The trimmed mean discards the $g$ smallest and $g$ largest values and averages
the rest; it interpolates between the mean ($\alpha = 0$) and the median
($\alpha \to 0.5$).

The **influence function** of an estimator $T$ is the change produced by adding
one observation at value $x$ to a large sample,

$$\mathrm{IF}(x; T) = \lim_{\varepsilon \to 0}
\frac{T\big((1-\varepsilon)F + \varepsilon\,\delta_x\big) - T(F)}{\varepsilon}.$$

For the mean, $\mathrm{IF}(x) = x - \mu$: unbounded, so a single arbitrary value
can move it arbitrarily. For the median, $\mathrm{IF}(x) = \operatorname{sign}(x -
\tilde\mu) / (2 f(\tilde\mu))$: bounded, because the density $f$ at the median
sets the exchange rate between one observation and the shift it buys.

## 3. Scale estimators

Scale is harder than location because the classical estimator, the standard
deviation

$$s = \sqrt{\frac{1}{n-1}\sum_{i=1}^{n}(x_i - \bar x)^2},$$

squares every deviation, so it is more sensitive to outliers than the mean is.
Two robust alternatives are the **interquartile range** $\mathrm{IQR} =
x_{(3n/4)} - x_{(1n/4)}$ and the **median absolute deviation**

$$\mathrm{MAD} = \operatorname{median}_i\,\big|x_i - \operatorname{median}_j x_j\big|.$$

For a Gaussian sample, $\mathrm{IQR} = 1.349\,\sigma$ and
$\mathrm{MAD} = 0.6745\,\sigma$, so dividing by those constants makes each a
consistent estimate of $\sigma$ when the model is Gaussian. The MAD carries no
information about the tails beyond the interquartile range — that is exactly why
it is robust, and exactly why it cannot detect a heavy tail.

## 4. Robustness: breakdown and masking

The **finite-sample breakdown point** is the smallest fraction of arbitrary
contamination that can move the estimator by an arbitrary amount. For the mean it
is $1/n$ — one bad value suffices. For the median it is $\approx 0.5$: as long as
fewer than half the sample is corrupt, the median stays inside the range of the
good data.

Masking is the practical consequence. If the scale used to standardise the data
is itself computed from the contaminated sample, one gross outlier inflates that
scale and hides the moderate outliers. The classical $z$-score

$$z_i = \frac{x_i - \bar x}{s}$$

uses $\bar x$ and $s$, both contaminated. The **modified $z$-score**

$$M_i = \frac{0.6745\,(x_i - \tilde x)}{\mathrm{MAD}}$$

uses the median and the MAD, both resistant, and is compared with the same
threshold. A common convention is $|M_i| > 3.5$.

## 5. Worked example: the synthetic porosity sample

The demonstration draws $n = 200$ values from $\mathcal N(50, 10^2)$ in per cent
and replaces the first 10 with spikes at $200\ \%$.

**Location.** The clean mean is $49.012\ \%$, the median $49.060\ \%$ and the
$10\,\%$ trimmed mean $49.095\ \%$ — all consistent with the true value
$50\ \%$ to within the sampling error $\sigma/\sqrt n = 10/\sqrt{200} = 0.707\ \%$.
After contamination the mean moves to $56.336\ \%$, a shift of $+7.325\ \%$ that
matches the exact prediction

$$\Delta \bar x = \frac{10 \times 200 - \sum_{i=1}^{10} x_i}{200} = +7.325\ \%,$$

while the median moves by only $+0.574\ \%$.

**Scale.** The clean standard deviation is $9.866\ \%$ and the contaminated one
$34.386\ \%$ — a factor of $3.5$. The MAD moves from $6.879$ to $7.146\ \%$, and
${\rm MAD}/0.6745$ from $10.199$ to $10.594\ \%$, a change of under $4\ \%$.

**Masking.** Adding one value at $2000\ \%$ raises the standard deviation from
$9.87$ to $138.55\ \%$. At the $3.5$ threshold the classical $z$-score then finds
only $1$ of the $5$ planted spikes, while the modified $z$-score finds all $5$.

**Breakdown.** The mean passes $60\ \%$ at a contamination fraction of $0.08$. The
median stays inside the clean data range until the fraction reaches $0.50$, which
is the theoretical breakdown point.

## 6. Efficiency: the price of robustness

Robustness is not free. On clean Gaussian data the sample median has variance
$\pi/2$ times that of the mean, so its efficiency is $2/\pi = 0.6366$. For the
$n = 200$ sample above, $3000$ Monte-Carlo ensembles give a standard deviation of
$0.7267\ \%$ for the mean and $0.8886\ \%$ for the median, a relative efficiency
of $0.6688$ — consistent with the theoretical $0.6366$ within the ensemble
scatter. The median pays about $36\ \%$ extra variance for a breakdown point that
is $100$ times larger.

## 7. Shape as a diagnostic

Skewness and excess kurtosis detect departure from the Gaussian assumption:

$$\gamma_1 = \frac{\mathbb E[(X-\mu)^3]}{\sigma^3}, \qquad
\gamma_2 = \frac{\mathbb E[(X-\mu)^4]}{\sigma^4} - 3 .$$

The clean sample gives $\gamma_1 = -0.058$ and $\gamma_2 = -0.321$, both
consistent with a Gaussian. The contaminated sample gives $\gamma_1 = +3.639$ and
$\gamma_2 = +12.777$; the large positive kurtosis is the signature of a mixture
of a body with a small number of extreme values, and it warns that any moment
higher than the second is being driven by a handful of samples.

## Assumptions and regime of validity

1. **The sample is representative of the population.** Robustness protects
   against outliers, not against a biased sampling plan.
2. **The contamination is a minority.** The median's guarantee holds below a
   fraction of $0.5$; above it the robust estimator is controlled by the
   contamination.
3. **Independence.** All the sampling errors quoted above assume independent
   observations. Correlated samples inflate the effective variance; the
   correction is the integrated autocorrelation time of
   [20-05-01 Stochastic Processes](../../20-signal-processing/05-noise-and-random-signals/01-stochastic-processes.md).
4. **The Gaussian consistency constants are model-dependent.** $0.6745$ is
   $\Phi^{-1}(3/4)$; it is a Gaussian convention, not a universal constant.
5. **Trimming must be declared.** A $10\ \%$ trimmed mean is not comparable with
   the untrimmed mean unless the trimming fraction is reported.

## The honest summary

A mean, a standard deviation and a correlation are three numbers that a single
bad observation can control. The median, the MAD and the IQR are robust
alternatives that answer the same question at a measurable cost in efficiency.
Which you report is a decision about the data-generating process, and a robust
statistic without a stated contamination model is as unexamined as a classical
one. The demonstration's specific numbers apply to a Gaussian body with
$5\ \%$ point contamination at $200\ \%$; they do **not** tell you the
contamination fraction of any real porosity log, which is a property of the
instrument and must be measured.

## Python demonstration

[`code/descriptive_statistics_demo.py`](./code/descriptive_statistics_demo.py)
prints every number quoted above. It:

1. compares the mean, median and trimmed mean with and without contamination;
2. compares the standard deviation, IQR and MAD, and prints the consistency
   factor $\mathrm{MAD}/0.6745$;
3. shows masking with one gross spike and four moderate ones;
4. tabulates estimators against the contamination fraction and measures the
   breakdown point;
5. measures the efficiency of the mean and the median over $3000$ ensembles;
6. prints skewness and excess kurtosis.

```bash
cd 21-statistics-bayesian-ml/01-statistics-in-practice/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python descriptive_statistics_demo.py
```

It runs in about half a second and prints only text.

## Exercises

Graded problems are in
[`exercises/01-descriptive-statistics-exercises.md`](./exercises/01-descriptive-statistics-exercises.md)
with worked solutions in
[`exercises/01-descriptive-statistics-solutions.md`](./exercises/01-descriptive-statistics-solutions.md).
The ★★★ problems ask you to design robustness experiments rather than repeat the
ones above.

## Mastery checkpoint

Without notes, for the sample
$\{4.1, 5.2, 4.8, 5.0, 5.3, 4.9, 120.0\}$ in per cent porosity:

1. Compute the mean, the median and the $1$-of-$7$ trimmed mean.
2. Compute the standard deviation and the MAD, and the corresponding
   Gaussian-consistent scales.
3. State the breakdown point of each location estimator you used.
4. Which single number would you report as "typical", and what does your answer
   assume about the $120.0$ value?

## Common pitfalls

1. **Reporting a mean without its scatter.** A mean of $56.3\ \%$ with a standard
   error of $2.4\ \%$ and one of $0.7\ \%$ are different claims.
2. **Using the standard deviation as a robust scale.** It is as sensitive as the
   mean; use the IQR or the MAD when contamination is possible.
3. **Standardising with contaminated parameters.** The classical $z$-score uses
   the mean and the standard deviation, so one gross spike masks the rest.
4. **Assuming a robust estimator is unbiased.** The median of a skewed sample
   estimates the median, not the mean; they differ by the skewness.
5. **Trimming without declaring it.** A trimmed mean is a different estimator for
   every trimming fraction.
6. **Reading kurtosis as a physical property.** Excess kurtosis of $+12.8$ here
   is caused by ten fabricated values.

## Where this is used

- **Well-log quality control**: preserving a median-based summary when a few
  spikes are instrument artefacts.
- **Geochemical assay reporting**: trimmed means are standard because a single
  mis-assayed sample otherwise dominates a batch.
- **Seismic amplitude analysis**: RMS amplitudes are means of squares and
  inherit the mean's unbounded influence.
- **Geodetic and geochemical time series**: robust trend estimation replaces
  least squares when offsets and outliers are present.
- **Hazard catalogues**: magnitude completeness and rate estimates quote robust
  location measures.

## Related lessons

- [21-01-02 Choosing Probability Models for Earth Data](02-probability-models-earth.md) —
  the distribution to which these summaries are attached.
- [21-01-03 Resampling: Bootstrap, Jackknife, Permutation Tests](03-resampling.md) —
  uncertainty for estimators whose formula you do not have.
- [21-01-04 Linear, Multiple and Robust Regression](04-regression.md) — the same
  robustness question for a fitted model.
- [21-01-05 Nonparametric Statistics and Kernel Density Estimation](05-nonparametric-methods.md) —
  inference without a distributional assumption.
- [01-13-06 Point Estimation, Bias, Consistency and Efficiency](../../01-mathematics/13-probability-and-statistics-foundations/06-estimation-theory.md) —
  the general theory these estimators instantiate.

## Self-assessment checklist

- [ ] I can compute the mean, median and trimmed mean and say which is which.
- [ ] I can convert between the MAD, the IQR and a Gaussian scale.
- [ ] I can state and measure a breakdown point.
- [ ] I can explain masking and choose a robust standardisation.
- [ ] I can quote the efficiency cost of a robust estimator.
- [ ] I can say what my reported summary does not constrain.
