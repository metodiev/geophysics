---
id: 01-13-04
title: "Common Distributions and Their Earth-Science Roles"
level: intermediate
prereqs: ["01-13-03"]
estimated_minutes: 90
tags: [distributions, gaussian, lognormal, power-law, extreme-values, poisson]
---

# Common Distributions and Their Earth-Science Roles

## Learning objectives

By the end of this lesson you will be able to:

1. **Name the mechanism**, not the formula, that produces each of the Gaussian,
   exponential, Poisson, gamma and Weibull, lognormal, Pareto and Gumbel
   distributions, and say which geophysical observable each mechanism describes.
2. **Derive** the Poisson PMF as the limit of a binomial, and show that
   exponential waiting times and Poisson counts are two views of one process.
3. **Derive** the mean, median and mode of a lognormal variable from the
   normality of its logarithm, and explain why the median is the honest central
   estimate.
4. **Derive** the Gumbel distribution as the limit law of the maximum of
   exponentially distributed samples.
5. **Explain** why a tail exponent below two makes a sample variance meaningless,
   and below one makes a sample mean meaningless, and demonstrate the failure
   numerically.
6. **Estimate** a power-law tail exponent with the Hill estimator and state the
   conditions under which the estimate is trustworthy.
7. **Choose** a distribution for a stated physical mechanism, and say what
   diagnostic would falsify the choice.

## Prerequisites

[01-13-03 Expectation, Variance and Moments](./03-expectation-variance.md) for
means, variances and the condition that a moment must exist, and
[01-13-02 Random Variables, PMFs, PDFs and CDFs](./02-random-variables.md) for
densities, CDFs and transformations.

## 1. A catalogue of mechanisms, not a menu of formulas

There is a strong temptation, on meeting a list of distributions, to treat it as a
menu: several shapes, pick the one that fits. That attitude produces fitted
distributions with no meaning. The productive attitude is the opposite: **ask what
process generated the numbers, and the distribution follows.**

The organising principle of this lesson is that each of the workhorse
distributions arises from one of a small number of generative mechanisms:

| Mechanism | Distribution | Canonical Earth-science instance |
|---|---|---|
| Sum of many small independent additive contributions | **Gaussian** | instrument error, elevation error, stacked random noise |
| Constant hazard in time or space | **exponential** (gaps), **Poisson** (counts) | earthquake recurrence above completeness, waiting times |
| Hazard that varies with time | **Weibull / gamma** | fracture spacing, wind speed, component lifetime |
| Product of many small positive contributions | **lognormal** | permeability, porosity, ore grade, hydraulic conductivity |
| Scale-invariant fragmentation or preferential growth | **power law / Pareto** | fracture lengths, fault scarp heights, magnitudes of released energy |
| Maximum of a large sample from a light-tailed parent | **Gumbel** | annual maximum flood, extreme storm surge, largest ground motion |

Everything below either derives one of these or exhibits it numerically. All the
numbers quoted come from `code/distributions_demo.py` (seed 20240120), and each
one has been computed rather than asserted.

## 2. The Gaussian: additive contributions

### 2.1 Why sums are Gaussian

If $X_1, \dots, X_n$ are independent with finite variance, then the standardised
sum converges in distribution to a standard Gaussian as $n \to \infty$. That is
the central limit theorem, proved and demonstrated in
[05 Sampling Distributions, Law of Large Numbers and CLT](./05-sampling-and-clt.md);
here it is enough to see the mechanism in action. The demonstration adds twelve
uniform$(0,1)$ variables:

```
  sum of 12 U(0,1): analytic mean 6, variance 1
  empirical mean     = 6.000345
  empirical variance = 0.997430
  fraction within 1.96 sd = 0.951025   (Gaussian: 0.950000)
```

Mean, variance and the central $95\%$ interval all match the Gaussian prediction.
Twelve is a small number, and the reason this works so well is that the uniform
parent is bounded and symmetric, so the third moment vanishes and the leading
correction to normality is correspondingly weak.

The empirical basis for the Gaussian error model is therefore this: **any
measured quantity whose error is the accumulated effect of many small independent
influences is approximately Gaussian.** Station elevation from a levelling
traverse, a temperature reading from a thermistor, and the residual in a
least-squares fit all qualify.

### 2.2 What the mechanism requires, and where it fails

The hypothesis is *additive* and *many small independent* contributions. Each
qualifier can fail, and each failure produces a recognisable departure:

- **Multiplicative instead of additive.** The product of many small positive
  factors is lognormal, not Gaussian (Section 5). This is why permeability is not
  Gaussian.
- **One dominant contribution.** If a single error source dominates — a constant
  mis-tie, a clock jump, a single bad pick — the sum is not approximately Gaussian
  even though many smaller terms exist. A histogram then shows a heavy tail on
  one side.
- **Bounded support.** A Gaussian assigns positive probability to negative
  velocities, negative depths and negative permeabilities. When the standard
  deviation is small compared with the mean, the implied error is negligible, and
  nobody worries. When it is not, the Gaussian model asserts that physically
  impossible values occur with appreciable probability, and that assertion
  propagates into inversions as a boundary artefact.
- **Heavy tails.** The theorem needs finite variance. For data whose spread is
  driven by rare large values, the Gaussian approximation to the distribution of
  the *mean* fails outright, and no sample size repairs it — the demonstration in
  lesson 05 measures rejection rates of $42\%$ at $n = 10$ falling only to $22\%$
  at $n = 10\,000$ for a tail exponent of $1.5$.

## 3. The exponential and the Poisson: constant hazard

### 3.1 From binomial to Poisson

Consider $n$ independent trials in a time interval of length $T$, each with
success probability $p = \lambda T/n$, so that the expected number of successes is
$\lambda T$ regardless of $n$. The probability of exactly $k$ successes is
binomial:

$$P(N = k) = \binom{n}{k} p^k (1-p)^{n-k}.$$

Let $n \to \infty$ with $\lambda T$ fixed. Then $\binom{n}{k} \approx n^k/k!$,
$p^k = (\lambda T/n)^k$, and $(1-p)^{n-k} \approx e^{-\lambda T}$. Collecting,

$$P(N = k) \to \frac{(\lambda T)^k}{k!}e^{-\lambda T},$$

which is the **Poisson PMF** with mean $\lambda T$. Because this is a limit of a
valid PMF, it sums to one automatically; the demonstration verifies the
normalisation directly (Section 2.1 of lesson 02) and confirms the mean–variance
equality.

### 3.2 Exponential gaps give Poisson counts

The Poisson distribution over counts and the exponential distribution over gaps
are the same process viewed two ways, and the demonstration proves the link by
simulation rather than by assertion. Drawing gaps from an exponential density with
rate $\lambda = 1.5$ and counting how many arrivals fall in a window of length
$T = 4$:

```
  inter-arrival ~ Exp(1.5), observation window T = 4.0
  analytic Poisson(lam*T) mean = 6.000000, variance = 6.000000
  empirical mean               = 6.002110
  empirical variance           = 6.005336
  P(count = 0) analytic        = 0.002479
  P(count = 0) empirical       = 0.002445
```

Every quantity agrees within simulation error, including the small probability of
no arrivals at all.

### 3.3 The mechanism in geophysics

A constant hazard means the probability that an event occurs in the next instant
does not depend on how long it has been since the last one. For earthquakes above
a completeness magnitude this is approximately true over decades, and it is why
Poisson models remain the default null hypothesis in probabilistic seismic hazard
assessment even though clustering is well documented. For *gridded* space rather
than time, the analogue is a spatially homogeneous Poisson point process, which is
the null model against which spatial clustering of seismicity, ore occurrences and
pockmarks is tested.

**Where it fails, predictably.** Any process with memory violates constant hazard.
Aftershock sequences give a hazard that decays as a power of elapsed time
(Omori-type decay); volcanic unrest gives a hazard that increases as a system
approaches failure; hydrological recharge gives a hazard with a seasonal cycle.
The appropriate diagnostic is a plot of the empirical hazard rate against time; a
constant line is the hypothesis, and any structure in the plot is a statement
about the physical mechanism.

## 4. Gamma and Weibull: hazard that changes

The exponential is the special case of a whole family in which the hazard rate is
not constant. Two parameterisations are worth knowing, because the geophysical
literature uses both.

The **gamma** distribution with shape $k$ and scale $\theta$ has density

$$f(x) = \frac{x^{k-1}e^{-x/\theta}}{\Gamma(k)\theta^{k}}, \qquad x \ge 0,$$

with $E[X] = k\theta$ and $\operatorname{Var}(X) = k\theta^2$. Sums of $k$
independent exponentials with rate $1/\theta$ are gamma$(k, \theta)$, which is why
the gamma describes a time to the $k$-th event rather than the first.

The **Weibull** distribution with shape $k$ and scale $\lambda$ has CDF

$$F(x) = 1 - e^{-(x/\lambda)^{k}},$$

so its hazard rate is $h(x) = (k/\lambda)(x/\lambda)^{k-1}$: increasing for
$k > 1$, constant at $k = 1$ (recovering the exponential), decreasing for
$k < 1$. A decreasing hazard is the signature of a population in which early
events remove the fragile members, and an increasing hazard the signature of
accumulating damage.

Geophysically, Weibull models appear wherever a failure process has a
size-dependence: the spacing of fractures in a layer (a threshold process on
layer thickness), the strength of rock specimens under a given load, and the
distribution of wind speeds at a site — the last being a staple of wind-resource
assessment and of the parameterisation of wave generation.

**Regime of validity.** Neither the gamma nor the Weibull has a bounded upper
tail, so neither can represent a physical upper limit such as a maximum possible
magnitude or a maximum flood level for a fixed catchment. When such a limit
exists and matters, a truncated, tapered or generalised-extreme-value model is
required, and the choice is a physical argument about the limit, not a fitting
convenience.

## 5. The lognormal: multiplicative contributions

### 5.1 Derivation

Let $X = \prod_{i=1}^{n} W_i$ with $W_i > 0$ independent. Taking logarithms,

$$\ln X = \sum_{i=1}^{n} \ln W_i,$$

a sum of independent variables, so by the central limit theorem $\ln X$ is
approximately normal. Thus $X$ is **lognormal**: $\ln X \sim \mathcal{N}(\mu,
\sigma^2)$.

The moments follow by evaluating the moment generating function of the normal at
$\sigma^2$:

$$E[X] = e^{\mu + \sigma^2/2}, \qquad \text{median}(X) = e^{\mu},
\qquad \text{mode}(X) = e^{\mu - \sigma^2},$$

$$\operatorname{Var}(X) = \left(e^{\sigma^2} - 1\right)e^{2\mu + \sigma^2}.$$

Note the ordering: for $\sigma > 0$, mode $<$ median $<$ mean. The mean always
exceeds the median, and the gap grows with $\sigma$. The demonstration evaluates
all of them with $\mu = 0$, $\sigma = 1$, $n = 300\,000$:

```
  analytic mean   = exp(mu + sigma^2/2) = 1.648721
  empirical mean                        = 1.652657
  analytic median = exp(mu)             = 1.000000
  empirical median                      = 1.001817
  fraction of samples above the mean    = 0.307670
```

Both moments agree with the closed forms, and — the number that matters — only
$30.8\%$ of the samples exceed the mean. The mean is not a typical value. In a
permeability field with $\sigma_{\ln} = 1$, the arithmetic mean permeability is
exceeded by fewer than one third of the samples, and an estimate of recoverable
fluid based on the arithmetic mean will be optimistic unless the flow is
genuinely controlled by the arithmetic mean of permeability, which for
parallel-layered flow it is not.

### 5.2 Why it is the right model for so many rock properties

Take permeability. Its value at a point reflects the product of grain size, sorting,
cementation, diagenesis and fracture density, each of which contributes a
multiplicative factor to the flow path. A product of many independent positive
factors is lognormal by the derivation above. The same argument applies to ore
grade, to hydraulic conductivity, to porosity, and to the size of clasts produced
by repeated crushing.

The corresponding practical rules:

- Summarise by the **median** or by **geometric-mean-type** quantities, not the
  arithmetic mean, when the quantity is lognormal and the process is multiplicative.
- Test lognormality by examining the histogram of $\ln X$, not of $X$. The
  diagnostic is that $\ln X$ looks symmetric; the failure mode is a $\ln X$
  distribution with its own long tail, which suggests genuinely heavy-tailed
  behaviour calling for a power-law model instead.
- Carry the units. $e^{\mu}$ has the units of $X$, but $\mu$ and $\sigma$ do not;
  they are in log-units, and comparing a log-$\sigma$ of $1$ with a physical
  standard deviation is meaningless.

## 6. Power laws: scale-invariant processes

### 6.1 Where power laws come from

A positive variable $X \ge x_{\min}$ has a **power-law (Pareto) tail** if

$$P(X > x) = \left(\frac{x}{x_{\min}}\right)^{-\alpha}, \qquad x \ge x_{\min},$$

with **tail exponent** $\alpha > 0$. Equivalently the density is
$f(x) = \alpha x_{\min}^{\alpha} x^{-\alpha-1}$.

The generative mechanism is **scale invariance**. Suppose a fragmentation process
breaks objects so that the distribution of fragment sizes produced from an object
of size $s$ is a scaled copy of the distribution from any other size. Then the
size distribution is the only one invariant under the rescaling, and it is a power
law. Rock fragmentation, fault growth by linkage, and the size distribution of
landslides all have this character at some range of scales, and the
Gutenberg–Richter magnitude distribution discussed in lesson 02 is the same
statement in logarithmic variables: an exponential in magnitude is a power law in
energy, with $\alpha = b/1.5$.

### 6.2 Moments, and why they fail

$$\text{mean} = \frac{\alpha}{\alpha - 1}\ x_{\min} \ (\alpha > 1), \qquad
\text{variance} = \frac{\alpha}{(\alpha-1)^2(\alpha-2)}\ x_{\min}^2 \ (\alpha > 2),$$

and the $k$-th moment exists only for $\alpha > k$. The demonstration makes the
consequences visible for $\alpha = 2.5$ (mean and variance exist, fourth moment
does not) and $\alpha = 1.5$ (mean exists, variance does not):

```
  Pareto(alpha = 2.5), P(X > x) = x^-alpha for x >= 1
    analytic mean   = alpha/(alpha-1)  = 1.666667 (finite)
    empirical mean                     = 1.664791
    analytic variance = alpha/((a-1)^2(a-2)) = 2.222222 (finite)
    empirical variance                 = 1.789740
    empirical median                   = 1.319618
    analytic median = 2^(1/alpha)      = 1.319508
    Hill alpha estimate from top 20000     = 2.480756
    P(X > 100): empirical = 0.00000250, analytic = 0.00001000
  Pareto(alpha = 1.5), P(X > x) = x^-alpha for x >= 1
    analytic mean   = alpha/(alpha-1)  = 3.000000 (finite)
    empirical mean                     = 2.952879
    analytic variance      = INFINITE (alpha <= 2)
    empirical variance                 = 167.779931 (driven by the single largest draw)
    empirical median                   = 1.587746
    analytic median = 2^(1/alpha)      = 1.587401
    Hill alpha estimate from top 20000     = 1.493105
    P(X > 100): empirical = 0.00100500, analytic = 0.00100000
```

Four readings of this output deserve attention.

**The medians are excellent.** $1.319618$ against $2^{1/2.5} = 1.319508$ and
$1.587746$ against $2^{1/1.5} = 1.587401$: quantiles are stable even when moments
are not. This is the practical reason to report quantiles for heavy-tailed data.

**The Hill estimator works, with bias.** The Hill estimator uses the largest $k$
order statistics, $\hat\alpha = 1 / \overline{\ln(X_{(i)}/X_{(n-k)})}$. It returns
$2.4808$ for a true $2.5$ and $1.4931$ for a true $1.5$. The small underestimate
is characteristic: the estimator is biased low for finite samples and for
thresholds below which the power law does not hold exactly. It is also sensitive
to the choice of $k$ — a dependence that standard practice handles by plotting
$\hat\alpha$ against $k$ and looking for the region where it is stable, and that
careless practice ignores.

**The variance of the $\alpha=2.5$ sample is low and unstable.** The empirical
variance is $1.7897$ against an analytic $2.2222$, and the running values do not
settle:

```
    alpha = 2.5: n=1000:     1.6337  n=10000:     1.9062  n=100000:     1.7854  n=400000:     1.7897
    alpha = 1.5: n=1000:    52.7407  n=10000:    76.7115  n=100000:   186.8350  n=400000:   167.7799

  Sample variance for alpha = 2.5 over 400 independent samples of n = 10000
    analytic variance        = 2.222222
    mean of the estimates    = 2.062239  (itself unconverged: the estimator's own variance diverges)
    median of the estimates  = 1.688539
    fraction below analytic  = 0.7850
```

The estimator is *unbiased in expectation* — its mean would converge to $2.2222$
if the fourth moment existed — yet $78.5\%$ of samples of size $10\,000$ return a
value below the truth, and the median estimate is $1.689$. The distribution of the
estimator is so strongly right-skewed that its typical value is far below its
mean, and the mean itself has not converged after $400$ repetitions because the
estimator's own variance is infinite. Reporting a sample variance for
$\alpha = 2.5$ data is therefore reporting a number whose uncertainty cannot be
quantified; a robust scale, or a quantile, is the honest alternative.

**The tail probability at $x = 100$ for $\alpha = 2.5$ needs more data than the
sample provides.** The model predicts $1.0\times10^{-5}$, so $400\,000$ draws
contain about four expected exceedances; the observed count was one. The
empirical value $2.5\times10^{-6}$ is not evidence against the model — it is the
sample size talking. Only the $\alpha = 1.5$ case, with about $400$ expected
exceedances, gives a well-determined comparison.

### 6.3 Regime of validity

- A power law holds over a *range* of scales, not everywhere. Above some scale a
  physical upper bound intervenes; below some scale the mechanism changes.
  Reporting a single $\alpha$ for the whole range hides both.
- Finite-sample estimation of $\alpha$ is biased and the bias depends on the
  threshold. Two studies that choose different thresholds will report different
  exponents from the same data; stating the threshold is part of stating the
  result.
- A straight line on a log–log survival plot is necessary but not sufficient
  evidence for a power law; a lognormal tail also looks nearly straight over a
  limited range, and the two are notoriously hard to distinguish in samples of
  the size that Earth-science datasets actually provide. Where the distinction
  matters — in extrapolating to a once-in-a-century event — a hard look at both
  fits, and at the scale range each is supported by, is required.

## 7. The Gumbel and the extreme-value family

### 7.1 Derivation for an exponential parent

Let $M_n = \max(X_1, \dots, X_n)$ with $X_i$ i.i.d. Exp$(1)$. Then for $x > 0$,

$$P(M_n \le x) = \left[P(X_1 \le x)\right]^n = (1 - e^{-x})^{n}.$$

Write $(1-e^{-x})^n = \exp\left(n\ln(1-e^{-x})\right)$ and use
$\ln(1-u) \approx -u$ for small $u$, which is accurate when $x$ is large enough
that $e^{-x}$ is small. Then

$$P(M_n \le x) \approx \exp\left(-n e^{-x}\right)
= \exp\left(-e^{-(x - \ln n)}\right).$$

Shifting by $\ln n$ gives a distribution independent of $n$:

$$Y = M_n - \ln n, \qquad P(Y \le y) = e^{-e^{-y}},$$

the **Gumbel** distribution, with mean equal to the Euler–Mascheroni constant
$\gamma \approx 0.5772$ and variance $\pi^2/6$. The demonstration checks it with
blocks of $1000$ exponentials and $40\,000$ blocks:

```
         y     P(Y <= y) emp      exp(-e^-y)
    -1.000          0.065250        0.065988
     0.000          0.368925        0.367879
     1.000          0.693275        0.692201
     2.000          0.872525        0.873423
  empirical mean of Y = 0.578372  (Gumbel mean = Euler-Mascheroni = 0.577216)
```

The empirical CDF tracks $e^{-e^{-y}}$ at every point and the mean is within
$0.002$ of $\gamma$, which is the size of Monte Carlo error here.

### 7.2 Why the mechanism is different from the CLT

The central limit theorem is about sums; extreme-value theory is about maxima.
The two produce different limit laws from the same parents, and both are
distributions of *statistics* rather than of the data. The
Fisher–Tippett–Gnedenko theorem states that the maximum of a large i.i.d. sample,
suitably standardised, has a limit distribution of only three possible types: the
Gumbel (light tails with exponential decay, including the Gaussian and the
exponential), the Fréchet (power-law tails), and the Weibull (bounded support).
They are combined into the **generalised extreme value (GEV)** distribution with a
shape parameter that interpolates between them.

**Geophysical use.** The quantity of interest in flood, storm-surge, extreme
rainfall and maximum-ground-motion estimation is not the typical value but the
largest over a period of years. Yearly maxima are extracted and fitted with the
GEV; a positive shape parameter means a Fréchet-type tail and therefore an
unbounded and heavy upper tail, which has direct consequences for the design of
defences. The block-maxima approach and the peaks-over-threshold alternative (with
the generalised Pareto distribution for exceedances) are the two standard
formulations.

**Regime of validity.** The theory needs independent observations, or at least a
declustering that produces approximately independent exceedances. Consecutive
storm-surge values within one storm are not independent events, and treating them
as such overstates the effective sample size and understates the return-level
uncertainty. The extrapolation also assumes the tail form holds *beyond* the range
of the data, which is untestable; the honest report includes the extrapolation
distance and the sensitivity of the answer to the fitted shape parameter.

## 8. Choosing a distribution: a working procedure

1. **State the mechanism.** Additive error, constant hazard, multiplicative
   factors, scale-invariant fragmentation, or an extreme of a sample. If none of
   these describes the process, none of the standard distributions is likely to be
   right, and a mixture or an empirical distribution is more honest.
2. **Look at the right scale.** Lognormal is symmetric in $\ln x$; power law is
   linear in $\log S(x)$ against $\log x$; exponential is linear in $\log S(x)$
   against $x$. Plotting on the wrong scale makes every candidate look wrong.
3. **Check the moments you intend to use.** Before quoting a mean, confirm that
   the mean exists and, if you will quote its uncertainty, that the variance does.
   Plot $\ln(\text{sample mean})$ against $\ln n$: if it climbs, stop.
4. **Use quantiles for the tail, and say which quantile.** The $99$th percentile
   is a stable summary of a heavy-tailed sample; the sample variance is not.
5. **Test on the part of the range you intend to use.** A fit validated over the
   bulk says nothing about the tail, and the tail is usually the part that
   matters.
6. **Report the extrapolation distance.** If the application needs a
   once-in-a-century value and the record is thirty years long, say so.

## 9. Assumptions and regime of validity (summary)

1. **Every one of these distributions is a model of a mechanism.** Fitting one is
   a hypothesis about the generating process, and the hypothesis, not the fit, is
   what should be defended.
2. **The support must be physical.** Gaussian errors on a strictly positive
   quantity, an unbounded Weibull for a bounded quantity, and an untruncated power
   law where a physical maximum exists are all model errors with consequences in
   the tail.
3. **Independence is required for the derivations, not for the shapes.** Poisson
   counts, Gumbel maxima and lognormal products are all derived from independence;
   real data with clustering or spatial correlation produce over-dispersion and
   biased exponents.
4. **Moment existence is a prerequisite, not a technicality.** Without the second
   moment there is no finite-variance error bar; without the first there is no
   meaningful average.
5. **Sample size limits what may be claimed.** Exceedance probabilities below
   roughly $10/n$ cannot be estimated from $n$ observations without a model, and
   then only to the extent the model is right.

## 10. Python demonstration

Run

```
python3 distributions_demo.py
```

from `code/`. Standard library only; seed 20240120, with $+1$ to $+5$ for the
internal simulation blocks. Five sections: Gaussian from sums, exponential gaps
producing Poisson counts, lognormal from products, Pareto with Hill estimation and
the variance study, and Gumbel as the maximum of exponentials. Every table quoted
in this lesson is taken verbatim from that run.

**How to read the run time and the ensemble sizes.** The script draws between
$10^{5}$ and $4\times10^{5}$ values per section, which is between one and ten
seconds of standard-library Python. That is the right order of magnitude for a
teaching demonstration; it is two to four orders of magnitude short of what a
serious tail estimate needs, which is exactly why the $\alpha = 2.5$ exceedance
comparison above is uninformative and the $\alpha = 1.5$ one is not.

**Breaking exercise.** In the Pareto section, change the Hill window from the
largest $5\%$ of the sample to the largest $1\%$ and to the largest $20\%$, and
report how the estimate of $\alpha$ moves for each parent. Then explain why a
practitioner plots $\hat\alpha$ against window size rather than quoting a single
value. Finally, increase $n$ by a factor of ten and observe which of the two
parents improves more.

## 11. Common mistakes

1. **Averaging lognormal data.** The arithmetic mean of a lognormal sample is
   dominated by a few large values and exceeds the median; the geometric mean is
   the natural central estimate for multiplicative processes.
2. **Quoting a standard deviation for a tail exponent below two.** The variance
   does not exist, so no finite-sample estimate of it converges.
3. **Fitting a power law to a lognormal.** Over two or three decades the two are
   nearly indistinguishable, and the choice changes the extrapolation.
4. **Confusing the maximum with the mean.** Extreme-value statistics exist because
   the distribution of the largest event is a different family from the
   distribution of a typical event.
5. **Using a Poisson model on a catalogue with aftershocks.** Over-dispersion is
   the symptom; a variance-to-mean ratio well above one is the diagnostic.
6. **Treating a Gumbel fit as a physical limit.** A Gumbel shape cannot represent
   a finite upper bound; if a bound exists, the Gumbel form will place non-zero
   probability above it.
7. **Reporting a tail exponent without its threshold.** The estimate is a function
   of the threshold, so the threshold is part of the result.
8. **Averaging several independent estimates as if they were independent
   samples.** Studies usually share data, methods or calibration, which is the correlation
   problem of lesson 03 in the form it takes in meta-analysis.

## 12. Real-world applications

- **Probabilistic seismic hazard.** Magnitude–frequency relations (exponential or
  tapered), Poisson occurrence, and ground-motion models with lognormal
  variability; the product of the three is combined over all source–site pairs.
- **Flood and coastal defence.** Fitting a GEV distribution to annual maxima gives
  the hundred-year return level that structures are designed for, and the
  uncertainty in that level is dominated by the uncertainty in the tail shape.
- **Reservoir characterisation.** Permeability and porosity as lognormal fields,
  with the median for volumetrics and a range of quantiles for flow simulation.
- **Mineral resource estimation.** Grade distributions are typically lognormal,
  and the difference between the arithmetic and geometric means is the difference
  between an optimistic and a defensible tonnage estimate.
- **Fracture and fault statistics.** Length distributions that are power law over
  the mapped range, with an exponent that governs the relative importance of many
  small structures against a few large ones — a question with direct consequences
  for fluid flow and for seismic hazard.
- **Instrument specification.** Repeatability quoted as a standard deviation is a
  Gaussian claim; check it against repeat measurements before propagating it.

## 13. Further reading

- **Coles, S. (2001). *An Introduction to Statistical Modeling of Extreme
  Values*. Springer.** Level: graduate. The standard reference for Section 7,
  including the GEV and generalised Pareto formulations and the practical
  diagnostics.
- **Sornette, D. (2004). *Critical Phenomena in Natural Sciences*. Springer.**
  Level: graduate. The best treatment of why power laws arise, and of the
  statistical pitfalls in Section 6.2.
- **Clauset, A., Shalizi, C. R. and Newman, M. E. J. (2009). Power-law
  distributions in empirical data. *SIAM Review*, 51(4), 661–703.** Level:
  advanced. The definitive practical guide to fitting and, more importantly, to
  testing a power law against alternatives; locate through your library.
- **Aitchison, J. and Brown, J. A. C. *The Lognormal Distribution*.** Level:
  advanced. The classical treatment of Section 5, including the estimation theory
  for lognormal means and medians.
- **Bury, K. *Statistical Distributions in Engineering*.** Level: intermediate to
  advanced. A clear engineering treatment of the gamma and Weibull families and
  their hazard-rate interpretation.
- **Ross, S. M. *Introduction to Probability Models*.** Level: intermediate.
  Poisson processes, waiting times and their interrelations, at the level of
  Section 3.

> Note on citations: bibliographic details are given so the works can be located.
> This repository does not host or reproduce copyrighted text; confirm editions
> and availability through your library.

## 14. Related lessons

- [02 Random Variables, PMFs, PDFs and CDFs](./02-random-variables.md) — the
  machinery, including the transformation from magnitude to energy used here.
- [03 Expectation, Variance and Moments](./03-expectation-variance.md) — why
  moment existence is a prerequisite rather than a technicality.
- [05 Sampling Distributions, Law of Large Numbers and CLT](./05-sampling-and-clt.md)
  — the theorem behind the Gaussian and the lognormal mechanisms, and the case
  where it fails.
- [07 Confidence Intervals and Their Correct Interpretation](./07-confidence-intervals.md)
  — how coverage behaves when the assumed distribution is wrong.
- [18 Inverse Problems](../../18-inverse-problems/README.md) — Gaussian and
  lognormal priors in practice, and the covariance matrices they imply.
- [21 Statistics, Bayesian Methods and Machine Learning](../../21-statistics-bayesian-ml/README.md)
  — heavier-tailed models, mixtures and the fitting of distributions.

## Exercises

[`exercises/04-distributions-exercises.md`](./exercises/04-distributions-exercises.md),
with solutions in
[`exercises/04-distributions-solutions.md`](./exercises/04-distributions-solutions.md).

## Self-assessment checklist

- [ ] I can name the generative mechanism for each of the Gaussian, exponential,
      Poisson, lognormal, Pareto and Gumbel distributions.
- [ ] I can derive the Poisson PMF as a limit of the binomial and state the
      assumption about the rate that the limit requires.
- [ ] I can derive the mean, median and variance of a lognormal variable and
      explain why the fraction above the mean is below one half.
- [ ] I can state the conditions for the mean and variance of a Pareto variable to
      exist, and demonstrate what happens when they do not.
- [ ] I can compute a Hill estimate of a tail exponent and describe how the answer
      depends on the threshold.
- [ ] I can derive the Gumbel limit for the maximum of $n$ exponentials, including
      the $\ln n$ shift.
- [ ] I can choose a distribution for a stated physical mechanism and name a
      diagnostic that would falsify the choice.
